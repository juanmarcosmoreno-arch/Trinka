# TRINKA question service

Creates quiz questions about any topic from PubMed abstracts, on demand. It's a small
Cloudflare Worker (`question-service/`) that calls Claude (Claude Opus 5.5). The AI API key
lives only here, as a secret — never in the iOS or watchOS apps.

## How it works

1. The app searches PubMed for the topic the user typed (e.g. *Staphylococcus aureus*).
2. For up to 5 articles with an abstract, it calls this service with the PMID, title, abstract,
   language and level.
3. The service asks Claude for questions in structured JSON. Every question must include a
   `supportingExcerpt` copied verbatim from the abstract.
4. The service discards any question whose excerpt isn't found in the title/abstract
   (case and whitespace-insensitive), or whose options are malformed. The app runs the same check
   again (`QuestionVerificationPipeline`).
5. Survivors are marked `autoVerified`: playable, always shown as **"Generated automatically —
   checked against the abstract, without expert review"**, with the source one tap away. Only the
   bundled, editorially reviewed questions are `verified`.

If a Claude safety classifier declines a request (possible for some biology topics), the service
asks the API to retry on its recommended fallback model (`fallbacks: "default"`). If that also
declines, the article is skipped (`{"drafts": [], "declined": true}`).

## Deploy (about 10 minutes)

You need a Cloudflare account (free plan works) and a Claude API key from
<https://platform.claude.com>. Then:

```sh
cd Backend/question-service
npm install
npx wrangler login                       # opens the browser
npx wrangler secret put ANTHROPIC_API_KEY
npx wrangler secret put APP_TOKEN        # optional: any long random string
npx wrangler deploy                      # prints https://trinka-question-service.<you>.workers.dev
curl https://trinka-question-service.<you>.workers.dev/health   # {"ok":true}
```

Connect the app: create `Config/Secrets.xcconfig` (git-ignored) with

```
QUESTION_SERVICE_HOST = trinka-question-service.<you>.workers.dev
QUESTION_SERVICE_TOKEN = <the APP_TOKEN, if you set one>
```

(host only, without `https://`), then rebuild. With no host configured, the app hides nothing but
explains that topic quizzes aren't set up.

**About `APP_TOKEN`:** it ships inside the app, so it only deters casual abuse; it is not real
authentication. Before a public launch, add rate limiting (Cloudflare rate-limiting rules or a
Workers rate-limit binding) and consider App Attest.

**Cost:** each article is one Claude request (title + abstract in, a few short questions out).
A 5-question quiz uses up to 5 requests. Monitor usage in the Claude Console.

## Develop

```sh
npm test          # unit tests (verification, request validation, HTTP handler) — no API calls
npm run typecheck
npx wrangler dev  # local server; put ANTHROPIC_API_KEY in .dev.vars (git-ignored)
```

## API

`POST /v1/questions/drafts` — `Authorization: Bearer <APP_TOKEN>` when configured.

Request:
```json
{
  "pmid": "27516602",
  "title": "Eye lens radiocarbon reveals centuries of longevity in the Greenland shark…",
  "abstract": "…",
  "language": "es",
  "difficulty": "beginner",
  "count": 3
}
```
`difficulty`: `beginner` · `curious` · `explorer` · `researcher` · `expert`. `count`: 1–5.
Optional `category` hint; otherwise the model classifies the article.

Response `200`:
```json
{
  "drafts": [
    {
      "pmid": "27516602",
      "language": "es",
      "category": "generalScience",
      "difficulty": "beginner",
      "prompt": "¿Dónde vive el tiburón de Groenlandia?",
      "options": ["En los mares árticos", "En ríos tropicales", "En lagos de montaña", "En el Amazonas"],
      "correctOptionIndex": 0,
      "explanation": "…",
      "shortExplanation": "…",
      "supportingExcerpt": "an iconic species of the Arctic Seas"
    }
  ]
}
```
Errors: `400` invalid request, `401` bad token, `413` too large, `502` upstream API error,
`503` rate-limited (retry later).
