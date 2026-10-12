# Question service (planned)

The apps never hold AI provider credentials. Question generation runs on a small backend
that TRINKA controls; the iOS client is `RemoteQuestionService` (TrinkaPubMed).

## `POST /v1/questions/drafts`

Request:
```json
{
  "pmid": "27516602",
  "title": "Eye lens radiocarbon reveals centuries of longevity in the Greenland shark…",
  "abstract": "…",
  "language": "es",
  "difficulty": "curious",
  "category": "generalScience"
}
```

Response:
```json
{
  "drafts": [
    {
      "pmid": "27516602",
      "language": "es",
      "category": "generalScience",
      "difficulty": "curious",
      "prompt": "…",
      "options": ["…", "…", "…", "…"],
      "correctOptionIndex": 0,
      "explanation": "…",
      "shortExplanation": "…",
      "supportingExcerpt": "revealed a life span of at least 272 years"
    }
  ]
}
```

Rules the backend must follow:
- Use only the supplied title/abstract; never cite another article.
- `supportingExcerpt` must be copied **verbatim** from the title or abstract (original language).
- Skip articles where a question would be ambiguous or would overstate a single study.

The client then runs `QuestionVerificationPipeline`: drafts whose excerpt isn't found in the
source, or that are malformed or attributed to another PMID, are discarded. Accepted drafts are
`needsReview` and are not playable until a reviewer marks them `verified`.
