import assert from "node:assert/strict";
import { test } from "node:test";
import { generate, GenerateRequest, userPrompt, verify } from "../src/generate.ts";
import { handle } from "../src/index.ts";

const abstract =
  "The Greenland shark (Somniosus microcephalus), an iconic species of the Arctic Seas, grows slowly and reaches >500 centimeters (cm) in total length, suggesting a life span well beyond those of other vertebrates. Radiocarbon dating of eye lens nuclei from 28 female Greenland sharks (81 to 502 cm in total length) revealed a life span of at least 272 years. Our results show that the Greenland shark is the longest-lived vertebrate known.";

const request = GenerateRequest.parse({
  pmid: "27516602",
  title: "Eye lens radiocarbon reveals centuries of longevity in the Greenland shark (Somniosus microcephalus).",
  abstract,
  language: "es",
  difficulty: "beginner",
  count: 3,
});

const good = {
  prompt: "¿Dónde vive el tiburón de Groenlandia?",
  options: ["Mares árticos", "Ríos tropicales", "Lagos", "El Amazonas"],
  correctOptionIndex: 0,
  explanation: "Es una especie emblemática de los mares árticos.",
  shortExplanation: "En los mares árticos.",
  supportingExcerpt: "an iconic species of the Arctic   Seas",
};

test("keeps only questions whose excerpt is in the abstract and whose options are valid", () => {
  const { drafts, rejected } = verify(request, {
    category: "generalScience",
    questions: [
      good,
      { ...good, supportingExcerpt: "Greenland sharks live for 1000 years" },
      { ...good, options: ["A", "a", "B", "C"] },
      { ...good, correctOptionIndex: 4 },
      { ...good, options: ["A", "B", "C"] },
    ],
  });
  assert.equal(drafts.length, 1);
  assert.equal(rejected.length, 4);
  assert.equal(drafts[0].pmid, "27516602");
  assert.equal(drafts[0].difficulty, "beginner");
  assert.equal(drafts[0].language, "es");
});

test("never returns more than requested", () => {
  const { drafts } = verify({ ...request, count: 1 }, { category: "generalScience", questions: [good, good] });
  assert.equal(drafts.length, 1);
});

test("prompt carries level guidance and wraps the article as data", () => {
  const prompt = userPrompt(request);
  assert.match(prompt, /Basic:/);
  assert.match(prompt, /<article pmid="27516602">/);
  assert.match(prompt, /Spanish/);
});

test("request validation rejects bad input", () => {
  assert.throws(() => GenerateRequest.parse({ ...request, pmid: "abc" }));
  assert.throws(() => GenerateRequest.parse({ ...request, difficulty: "godlike" }));
  assert.throws(() => GenerateRequest.parse({ ...request, abstract: "short" }));
});

function fakeClient(response: object, capture?: (params: any) => void) {
  return {
    beta: {
      messages: {
        create: async (params: any) => {
          capture?.(params);
          return response;
        },
      },
    },
  } as any;
}

test("calls Claude with structured output and default fallbacks, then verifies", async () => {
  let sent: any;
  const client = fakeClient(
    { model: "claude-opus-5-5", stop_reason: "end_turn", content: [{ type: "text", text: JSON.stringify({ category: "generalScience", questions: [good] }) }] },
    (params) => (sent = params),
  );
  const result = await generate(client, request);
  assert.equal(result.drafts.length, 1);
  assert.equal(sent.model, "claude-opus-5-5");
  assert.equal(sent.fallbacks, "default");
  assert.deepEqual(sent.betas, ["server-side-fallback-2026-07-01"]);
  assert.equal(sent.output_config.format.type, "json_schema");
  assert.equal(sent.thinking, undefined, "thinking must not be disabled on Opus 5.5");
});

test("HTTP handler: auth, validation, refusal", async () => {
  const env = { ANTHROPIC_API_KEY: "test", APP_TOKEN: "secret" };
  const post = (body: unknown, token = "secret") =>
    new Request("https://svc/v1/questions/drafts", {
      method: "POST",
      headers: { authorization: `Bearer ${token}`, "content-type": "application/json" },
      body: JSON.stringify(body),
    });

  assert.equal((await handle(post(request, "wrong"), env)).status, 401);
  assert.equal((await handle(post({ ...request, pmid: "x" }), env)).status, 400);

  const refused = fakeClient({ model: "claude-opus-5-5", stop_reason: "refusal", stop_details: { category: "bio" }, content: [] });
  const res = await handle(post(request), env, () => refused);
  assert.equal(res.status, 200);
  assert.deepEqual(await res.json(), { drafts: [], declined: true });

  const ok = fakeClient({ model: "claude-opus-5-5", stop_reason: "end_turn", content: [{ type: "text", text: JSON.stringify({ category: "generalScience", questions: [good] }) }] });
  const okRes = await handle(post(request), env, () => ok);
  const payload: any = await okRes.json();
  assert.equal(payload.drafts.length, 1);
  assert.equal(payload.drafts[0].category, "generalScience");
});
