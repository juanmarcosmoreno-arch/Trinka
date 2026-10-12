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
   (do the same for **TrinkaWatch**). Change the bundle IDs (`com.trinka.app`,
   `com.trinka.app.watchkitapp`) if they are taken in your account.
3. Pick the **Trinka** scheme and an iPhone simulator (or **TrinkaWatch** for the watch) and press ⌘R.

Optional: create `Config/Secrets.xcconfig` (git-ignored) with
```
NCBI_CONTACT_EMAIL = you@example.com
NCBI_API_KEY =
```
NCBI asks API clients for a contact e-mail; an API key raises the PubMed rate limit.

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
| Explore: discipline, difficulty (Curious / Explorer / Researcher), length | ✓ | |
| Discover: live PubMed search (discipline, topic, date, publication type), offline cache | ✓ | |
| Single study vs. evidence synthesis labels | ✓ | |
| Progress: answered, accuracy, streaks, favorites, 14-day chart, achievements | ✓ | streak, today's score |
| Friend challenges by code / group leaderboard (no account) | ✓ | |
| Light / dark / follow system | ✓ | (always dark) |
| English / Spanish | ✓ | ✓ |
| Haptics, optional timer, VoiceOver labels, Dynamic Type, Reduce Motion | ✓ | ✓ |

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
- The bundled bank (`TrinkaQuiz/Resources/SeedQuestions.json`) has 30 questions × 2 languages,
  one per article, from 30 real PubMed records fetched with E-utilities (3 per discipline).
  Each question stores the excerpt that supports its answer; the test suite re-checks all of them.
  Have a domain expert review them before a public release.
- AI generation is prepared, not enabled: `RemoteQuestionService` calls TRINKA's own backend
  (see `Backend/README.md`) — no AI keys in the apps. Drafts go through
  `QuestionVerificationPipeline`; survivors are only `needsReview` until a person approves them.

### Daily challenge and sync

`QuestionSelector.dailyChallenge` is seeded by the date, so iPhone and Watch build the same
challenge offline. The iPhone also sends today's pack and recent sessions to the watch via
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
- Question service backend + review tool; larger question bank.
- Online groups (Game Center / CloudKit).
