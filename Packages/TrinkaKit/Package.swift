// swift-tools-version: 5.10
import PackageDescription

/// TrinkaKit holds all of TRINKA's shared code.
/// The iOS and watchOS app targets in `Trinka.xcodeproj` link these libraries.
///
/// TrinkaCore, TrinkaQuiz and TrinkaPubMed are pure Swift + Foundation and also build on
/// Linux, so the business logic can be tested anywhere (`swift test`). The modules that need
/// Apple frameworks (SwiftData, WatchConnectivity, SwiftUI) are only declared on Apple hosts.

var products: [Product] = [
    .library(name: "TrinkaCore", targets: ["TrinkaCore"]),
    .library(name: "TrinkaPubMed", targets: ["TrinkaPubMed"]),
    .library(name: "TrinkaQuiz", targets: ["TrinkaQuiz"]),
]

var targets: [Target] = [
    // Domain models and pure business rules (no I/O, no UI).
    .target(name: "TrinkaCore"),

    // NCBI E-utilities client, PubMed parsing and question-generation contracts.
    .target(name: "TrinkaPubMed", dependencies: ["TrinkaCore"]),

    // Quiz engine, question bank and selection (with the bundled, source-verified seed bank).
    .target(
        name: "TrinkaQuiz",
        dependencies: ["TrinkaCore"],
        resources: [.copy("Resources/SeedQuestions.json")]
    ),

    .testTarget(name: "TrinkaCoreTests", dependencies: ["TrinkaCore"]),
    .testTarget(name: "TrinkaQuizTests", dependencies: ["TrinkaQuiz", "TrinkaCore"]),
    .testTarget(
        name: "TrinkaPubMedTests",
        dependencies: ["TrinkaPubMed", "TrinkaCore"],
        resources: [.copy("Fixtures")]
    ),
]

#if !os(Linux) && !os(Windows)
products += [
    .library(name: "TrinkaPersistence", targets: ["TrinkaPersistence"]),
    .library(name: "TrinkaSync", targets: ["TrinkaSync"]),
    .library(name: "TrinkaUI", targets: ["TrinkaUI"]),
]

targets += [
    // SwiftData models and the local progress store.
    .target(name: "TrinkaPersistence", dependencies: ["TrinkaCore", "TrinkaQuiz"]),

    // WatchConnectivity bridge between iPhone and Apple Watch.
    .target(name: "TrinkaSync", dependencies: ["TrinkaCore"]),

    // Design system, reusable SwiftUI components and localized strings.
    .target(
        name: "TrinkaUI",
        dependencies: ["TrinkaCore", "TrinkaQuiz"],
        resources: [.process("Resources")]
    ),
]
#endif

let package = Package(
    name: "TrinkaKit",
    defaultLocalization: "en",
    platforms: [
        .iOS(.v17),
        .watchOS(.v10),
        .macOS(.v14),
    ],
    products: products,
    targets: targets
)
