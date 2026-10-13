import Foundation

/// Scientific disciplines available in TRINKA.
///
/// Each category knows how to express itself as a PubMed query (MeSH terms) so the
/// same enum drives both the quiz filters and the research feed.
public enum ScienceCategory: String, CaseIterable, Codable, Hashable, Identifiable, Sendable {
    case microbiology
    case immunology
    case genetics
    case neuroscience
    case humanPhysiology
    case medicine
    case biotechnology
    case nutrition
    case veterinaryScience
    case generalScience
    case infectiousDiseases
    case diagnosticMethods
    case foodAnalysis
    case historyOfScience
    case bovineMastitis

    public var id: String { rawValue }

    /// Localization key used by the UI layer (`category.<rawValue>`).
    public var localizationKey: String { "category.\(rawValue)" }

    /// SF Symbol representing the category.
    public var symbolName: String {
        switch self {
        case .microbiology: "allergens"
        case .immunology: "shield.lefthalf.filled"
        case .genetics: "point.3.filled.connected.trianglepath.dotted"
        case .neuroscience: "brain.head.profile"
        case .humanPhysiology: "heart.text.square"
        case .medicine: "cross.case"
        case .biotechnology: "testtube.2"
        case .nutrition: "leaf"
        case .veterinaryScience: "pawprint"
        case .generalScience: "sparkles"
        case .infectiousDiseases: "facemask"
        case .diagnosticMethods: "stethoscope"
        case .foodAnalysis: "fork.knife"
        case .historyOfScience: "building.columns"
        case .bovineMastitis: "drop.fill"
        }
    }

    /// PubMed search expression for the discipline, built from MeSH headings.
    public var pubMedQuery: String {
        switch self {
        case .microbiology: "\"Microbiology\"[MeSH] OR \"Bacteria\"[MeSH] OR \"Microbiota\"[MeSH]"
        case .immunology: "\"Allergy and Immunology\"[MeSH] OR \"Immune System Phenomena\"[MeSH]"
        case .genetics: "\"Genetics\"[MeSH] OR \"Genome, Human\"[MeSH] OR \"Gene Editing\"[MeSH]"
        case .neuroscience: "\"Neurosciences\"[MeSH] OR \"Brain\"[MeSH] OR \"Neurons\"[MeSH]"
        case .humanPhysiology: "\"Physiological Phenomena\"[MeSH] OR \"Physiology\"[MeSH]"
        case .medicine: "\"Clinical Medicine\"[MeSH] OR \"Therapeutics\"[MeSH]"
        case .biotechnology: "\"Biotechnology\"[MeSH] OR \"Genetic Engineering\"[MeSH]"
        case .nutrition: "\"Nutritional Sciences\"[MeSH] OR \"Diet\"[MeSH]"
        case .veterinaryScience: "\"Veterinary Medicine\"[MeSH] OR \"Animal Diseases\"[MeSH]"
        case .generalScience: "\"Science\"[MeSH] OR \"Biodiversity\"[MeSH] OR \"Longevity\"[MeSH]"
        case .infectiousDiseases: "\"Communicable Diseases\"[MeSH] OR \"Infections\"[MeSH]"
        case .diagnosticMethods: "\"Diagnostic Techniques and Procedures\"[MeSH] OR \"Clinical Laboratory Techniques\"[MeSH]"
        case .foodAnalysis: "\"Food Analysis\"[MeSH] OR \"Food Microbiology\"[MeSH] OR \"Food Safety\"[MeSH]"
        case .historyOfScience: "\"History of Medicine\"[MeSH] OR \"Science/history\"[MeSH]"
        case .bovineMastitis: "\"Mastitis, Bovine\"[MeSH]"
        }
    }
}
