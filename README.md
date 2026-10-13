# TRINKA

**Science. Curiosity. Discovery.**

TRINKA turns research published in PubMed into short quiz challenges for iPhone and
Apple Watch. Every question cites a real, identifiable article and lets you open the source.

## Requirements

- Xcode 16 or newer (the project uses synchronized folders, project format 77)
- iOS 17+ / watchOS 10+ (SwiftData, Observation)

## Run it

1. Open `Trinka.xcodeproj`.
2. Select the **Trinka** target → *Signing & Capabilities* → choose your Team
   (do the same for **TrinkaWatch**). Change the bundle IDs (`com.micrusoperandi.trinka`,
   `com.micrusoperandi.trinka.watchkitapp`) if they are taken in your account.
3. Pick the **Trinka** scheme and an iPhone simulator (or **TrinkaWatch** for the watch) and press ⌘R.

Optional: create `Config/Secrets.xcconfig` (git-ignored) with
```
NCBI_CONTACT_EMAIL = you@example.com
NCBI_API_KEY =
QUESTION_SERVICE_HOST = trinka-question-service.<you>.workers.dev
QUESTION_SERVICE_TOKEN =
```
NCBI asks API clients for a contact e-mail; an API key raises the PubMed rate limit.
`QUESTION_SERVICE_*` enables topic quizzes once the service is deployed (`Backend/README.md`).

### Tests

The business logic (TrinkaCore, TrinkaQuiz, TrinkaPubMed) is plain Swift and is tested with
SwiftPM, on macOS or Linux:

```sh
cd Packages/TrinkaKit && swift test
```

## Features in this version

| Area | iPhone | Apple Watch |
|---|---|---|
| Daily challenge (5 questions, same for everyone each day, offline) | ✓ | ✓ (Quick Quiz) |
| Answer → verdict → explanation → small bibliographic reference → source | ✓ | ✓ (short) |
| 5 levels — Basic, Curious, Explorer, Researcher, Expert — chosen on Home; daily challenge adapts | ✓ | ✓ |
| Explore: discipline, level (or mixed), length | ✓ | |
| Discover: live PubMed search (discipline, topic, date, publication type), offline cache | ✓ | |
| Single study vs. evidence synthesis labels | ✓ | |
| Progress: answered, accuracy, streaks, favorites, 14-day chart, achievements | ✓ | streak, today's score |
| Questions about any topic (e.g. *Staphylococcus aureus*), generated from PubMed abstracts and checked against them | ✓ | |
| Friend challenges by code / group leaderboard (no account) | ✓ | |
| Light / dark / follow system | ✓ | (always dark) |
| English / Spanish | ✓ | ✓ |
| Haptics, practice timer (optional) and reading-time timer in daily and friend challenges, VoiceOver labels, Dynamic Type, Reduce Motion | ✓ | ✓ |

## Architecture

```
Trinka.xcodeproj
├── Trinka/              iOS app (screens + AppModel)
├── TrinkaWatch/         watchOS app (Quick Quiz + WatchModel)
├── Config/              Info.plist fragments, xcconfig
└── Packages/TrinkaKit/  Swift package with the shared modules
    ├── TrinkaCore         models, verification rules, scoring, streaks, achievements, stats
    ├── TrinkaQuiz         quiz engine, question selection, seed bank, friend-challenge codes
    ├── TrinkaPubMed       NCBI E-utilities client, XML parser, digests, cache, AI-generation contract
    ├── TrinkaPersistence  SwiftData models, ProgressStore, ChallengeStore
    ├── TrinkaSync         WatchConnectivity (application context + guaranteed user-info transfers)
    └── TrinkaUI           design system, logo, components, QuizSession, localized strings
```

Views talk to `AppModel` / `WatchModel`; business rules live in the package and have no UI
dependencies. No third-party dependencies.

### Question integrity

- A question is playable only if `QuestionValidator` passes: four distinct options, one correct
  answer, an explanation, a valid PMID, status `verified`, and a **supporting excerpt that
  appears verbatim in the article's title/abstract**.
- The bundled bank (`TrinkaQuiz/Resources/SeedQuestions.json`) holds exam-style questions in
  English and Spanish across five levels. Most are general knowledge (microbiology, immunology,
  veterinary science, infectious diseases), each grounded in a peer-reviewed reference chapter
  (StatPearls) or review article indexed in PubMed, with the excerpt that supports the answer.
  The build script and the test suite re-check every excerpt. Have a domain expert review them
  before a public release.
- To add or edit questions: add or change a file in `Scripts/seed/bank/` and run
  `python3 Scripts/seed/build_seed.py`. It fetches new articles from PubMed, rejects unsupported
  excerpts, bumps the bank version when the questions changed, and writes both the bundled bank
  and the published copy in `Content/`.
- Disciplines with fewer than 20 questions are hidden from pickers until they have more content.

### Updating questions without an App Store release

`Content/manifest.json` and `Content/questions-<version>.json` are the published bank. At launch,
the iPhone and Watch apps (`QuestionBankStore`) read the manifest from `QUESTION_BANK_BASE`
(default: this repository's default branch, via `HEAD` on `raw.githubusercontent.com`). If it announces a newer
version, they download the file, validate every question exactly like the bundled bank, and use it
from the next launch, so a day's challenge never changes mid-day. If anything fails (offline,
invalid file), the app keeps the questions it has. To publish: run the build script, commit,
and push to the default branch.

- Topic quizzes: the app searches PubMed and calls TRINKA's question service
  (`Backend/question-service`, a Cloudflare Worker using Claude; setup in `Backend/README.md`).
  No AI keys in the apps. Every generated question must quote its abstract verbatim; the service and
  the app (`QuestionVerificationPipeline`) both discard any that don't. Survivors are `autoVerified`
  and always labeled "generated automatically — checked against the abstract, without expert
  review"; only the bundled questions are `verified`.

### Daily challenge and sync

`QuestionSelector.dailyChallenge` is seeded by the date and the player's level, so iPhone and
Watch build the same challenge offline. Questions at the chosen level come first; when a level
has too few, the nearest levels fill in (one step easier before one step harder). The iPhone also sends today's pack and recent sessions to the watch via
`updateApplicationContext`; finished sessions travel both ways with `transferUserInfo`
(queued, guaranteed) and are de-duplicated by ID.

### Friend challenges

A challenge code (`TRK-XXXXX-XXXXX`) encodes discipline, difficulty, length, a seed and the
question-bank version (with a checksum). Everyone with the code plays the same questions, each
in their own language. Players share `trinka://result?...` links; opening one adds the result to
the local leaderboard (most correct, then fastest). Nothing is uploaded. Automatic online group
leaderboards (Game Center or CloudKit) are a planned next step.

## Brand

Palette and how to drop in the original logo files: `Design/Brand/README.md`.

## Roadmap

- HealthKit (opt-in, descriptive only; no diagnoses) — architecture leaves room, not in MVP.
- WidgetKit widgets and watch complications.
- Review tool for generated questions; larger reviewed bank; rate limiting / App Attest on the service.
- Online groups (Game Center / CloudKit).
