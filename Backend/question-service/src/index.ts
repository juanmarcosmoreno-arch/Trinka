import Anthropic from "@anthropic-ai/sdk";
import { generate, GenerateRequest, GenerationRefused } from "./generate.ts";

export interface Env {
  /** Claude API key (wrangler secret). Never shipped in the apps. */
  ANTHROPIC_API_KEY: string;
  /** Optional shared token the app sends as `Authorization: Bearer …` (abuse deterrent, not real auth). */
  APP_TOKEN?: string;
}

const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json; charset=utf-8" } });

export async function handle(request: Request, env: Env, makeClient = (key: string) => new Anthropic({ apiKey: key })) {
  const url = new URL(request.url);
  if (request.method === "GET" && url.pathname === "/health") return json({ ok: true });
  if (url.pathname !== "/v1/questions/drafts") return json({ error: "not_found" }, 404);
  if (request.method !== "POST") return json({ error: "method_not_allowed" }, 405);

  if (env.APP_TOKEN && request.headers.get("authorization") !== `Bearer ${env.APP_TOKEN}`) {
    return json({ error: "unauthorized" }, 401);
  }
  if (Number(request.headers.get("content-length") ?? 0) > 20_000) return json({ error: "too_large" }, 413);

  let body: GenerateRequest;
  try {
    body = GenerateRequest.parse(await request.json());
  } catch (error) {
    return json({ error: "invalid_request", detail: String(error).slice(0, 300) }, 400);
  }

  try {
    const result = await generate(makeClient(env.ANTHROPIC_API_KEY), body);
    console.log(JSON.stringify({ pmid: body.pmid, level: body.difficulty, accepted: result.drafts.length, rejected: result.rejected.length, model: result.model }));
    return json({ drafts: result.drafts });
  } catch (error) {
    if (error instanceof GenerationRefused) return json({ drafts: [], declined: true });
    if (error instanceof Anthropic.RateLimitError) return json({ error: "busy" }, 503);
    if (error instanceof Anthropic.APIError) {
      console.error("Claude API error", error.status, error.message);
      return json({ error: "upstream" }, 502);
    }
    console.error("Unexpected error", error);
    return json({ error: "internal" }, 500);
  }
}

export default {
  fetch: (request: Request, env: Env) => handle(request, env),
};
