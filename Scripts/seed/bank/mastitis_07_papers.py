# Bovine mastitis VII — culture-guided and deferred treatment, vaccines in the field, S. aureus genotype B
# sanitation in Switzerland, raw milk cheese, S. agalactiae blitz therapy, Prototheca, sensors,
# bovine leukemia virus, dry cow therapy and resistance, MRSA, S. aureus cure factors.
# Sources: PubMed original papers and reviews (abstracts). Excerpts verbatim.
CATEGORY = "bovineMastitis"
Q = [
# --- On-farm testing strategy (33663824)
("33663824", "researcher", 2, "For subclinical mastitis, however, on-farm testing may lead to an unacceptable increase in use of antimicrobials",
 ("Why did the authors NOT advise on-farm testing as the routine approach for subclinical mastitis?", ["It never detects any bacteria", "It is too slow to read by farmers", "It led to more antimicrobial use", "It is banned in the Netherlands"],
  "With on-farm tests, about half of subclinical cases were treated versus 4% of controls.", "More antibiotics used."),
 ("¿Por qué los autores NO aconsejaron el cultivo en el tambo como rutina para la mastitis subclínica?", ["Nunca detecta bacterias", "Es muy lento de leer para el productor", "Llevó a usar más antimicrobianos", "Está prohibido en Países Bajos"],
  "Con los test en el tambo se trató cerca de la mitad de los casos subclínicos, frente al 4% de los controles.", "Más antibióticos.")),
("33663824", "explorer", 0, "A diagnosis and treatment strategy with on-farm testing is advised in cows with clinical mastitis to enhance prudent antimicrobial use",
 ("For which cows did the study recommend on-farm testing before treatment?", ["Cows with clinical mastitis", "Every cow at each milking", "Only dry cows at calving", "Only heifers before breeding"],
  "For clinical cases, on-farm tests led to more etiology-based, prudent treatment decisions.", "Clinical mastitis."),
 ("¿En qué vacas recomendó el estudio hacer el test en el tambo antes de tratar?", ["En vacas con mastitis clínica", "En todas las vacas en cada ordeño", "Solo en vacas secas al parto", "Solo en vaquillonas antes del servicio"],
  "En los casos clínicos, los test en el tambo llevaron a decisiones más prudentes y basadas en la etiología.", "Mastitis clínica.")),

# --- S. uberis cure predictors (27372580)
("27372580", "researcher", 3, "The probability of cure was higher among first- and second-parity animals than among older cows",
 ("Which cows had a higher probability of cure from S. uberis mastitis?", ["Older cows in late lactation", "Cows with many high SCC records", "Cows in their fifth lactation", "First- and second-parity cows"],
  "Younger cows and those with a single high SCC record cured more often, as with S. aureus.", "Young cows."),
 ("¿Qué vacas tenían más probabilidad de curarse de una mastitis por S. uberis?", ["Vacas viejas al final de la lactancia", "Vacas con muchos controles de RCS alto", "Vacas en su quinta lactancia", "Vacas de primer y segundo parto"],
  "Las vacas jóvenes y las con un solo RCS alto se curaban más, igual que con S. aureus.", "Vacas jóvenes.")),
("27372580", "explorer", 1, "Treatment of mastitis is the most common reason for use of antimicrobial agents in dairy cattle",
 ("What is the most common reason for antimicrobial use in dairy cattle?", ["Lameness and foot rot", "Treating mastitis", "Calf pneumonia", "Uterine infections"],
  "Mastitis treatment accounts for most antimicrobial use on dairy farms.", "Mastitis."),
 ("¿Cuál es el motivo más común de uso de antimicrobianos en el ganado lechero?", ["Cojeras y pietín", "Tratar la mastitis", "Neumonía de terneros", "Infecciones uterinas"],
  "El tratamiento de la mastitis explica la mayor parte del uso de antimicrobianos en los tambos.", "La mastitis.")),

# --- Deferred treatment NZ (32062434)
("32062434", "researcher", 0, "Antibiotic usage was 24 % less (95 % predictive interval = 12-47 %) in the selective group",
 ("How much less antibiotic was used with 24-hour deferred, culture-based treatment in New Zealand herds?", ["About 24% less", "About 74% less", "About 4% less", "It actually doubled"],
  "Selective treatment cut antibiotic use by 24% with no loss in bacteriological or clinical cure.", "~24% less."),
 ("¿Cuánto antibiótico menos se usó con el tratamiento diferido 24 h y guiado por cultivo en Nueva Zelanda?", ["Cerca de 24% menos", "Cerca de 74% menos", "Cerca de 4% menos", "En realidad se duplicó"],
  "El tratamiento selectivo redujo 24% el uso de antibióticos sin perder curas bacteriológicas ni clínicas.", "~24% menos.")),
("32062434", "explorer", 2, "in New Zealand's seasonal, pastoral dairy system, mastitis is dominated by Gram-positive organisms",
 ("Which organisms dominate mastitis in New Zealand's pasture-based dairy system?", ["Gram-negative coliforms", "Mycoplasma species", "Gram-positive bacteria", "Yeasts and algae"],
  "Unlike confinement systems with many gram-negatives, NZ pastoral herds face mostly gram-positive mastitis.", "Gram-positives."),
 ("¿Qué organismos dominan la mastitis en el sistema pastoril de Nueva Zelanda?", ["Coliformes gramnegativos", "Especies de Mycoplasma", "Bacterias grampositivas", "Levaduras y algas"],
  "A diferencia de los sistemas confinados con muchos gramnegativos, los rodeos pastoriles de NZ tienen sobre todo grampositivos.", "Grampositivas.")),

# --- Vaccine field trial, Germany (27354335)
("27354335", "researcher", 3, "the application of two different mastitis vaccines was not an appropriate tool to improve the considered parameters of udder health sustainably",
 ("What did this German field trial conclude about Startvac and a herd-specific S. aureus vaccine?", ["Both cured all chronic infections", "Both doubled the farm's milk yield", "Only the herd vaccine eliminated mastitis", "Neither gave a lasting benefit"],
  "Despite some lower S. aureus prevalence, neither vaccine improved udder health in a lasting way.", "No lasting benefit."),
 ("¿Qué concluyó este ensayo de campo alemán sobre Startvac y una vacuna autógena de S. aureus?", ["Ambas curaron todas las infecciones crónicas", "Ambas duplicaron la leche del tambo", "Solo la autógena eliminó la mastitis", "Ninguna dio un beneficio duradero"],
  "Pese a cierta baja en la prevalencia de S. aureus, ninguna vacuna mejoró la salud de ubre de forma sostenida.", "Sin beneficio duradero.")),

# --- MASTIVAC I field trial, Israel (12814700)
("12814700", "expert", 1, "the vaccinated cows in first and second lactation had 42 and 54%, respectively, lower SCCs and milk yields 0.5 kg per day higher",
 ("In the Israeli MASTIVAC field trial, what did vaccinated heifers show compared with controls?", ["No difference in any parameter", "Lower SCC and slightly more milk", "Higher SCC but more milk fat", "Complete absence of S. aureus"],
  "Infections were too few to compare, but vaccinated cows had 42–54% lower SCC and 0.5 kg/d more milk.", "Lower SCC, more milk."),
 ("En el ensayo de campo israelí con MASTIVAC, ¿qué mostraron las vaquillonas vacunadas frente a los controles?", ["Ninguna diferencia en nada", "Menos RCS y algo más de leche", "Más RCS pero más grasa", "Ausencia total de S. aureus"],
  "Las infecciones fueron muy pocas para comparar, pero las vacunadas tuvieron 42–54% menos RCS y 0,5 kg/d más leche.", "Menos RCS, más leche.")),

# --- S. aureus genotype B in Europe (26585469)
("26585469", "researcher", 2, "Staph. aureus GTB was found to be contagious, whereas Staph. aureus GTC and all the remaining genotypes were involved in individual cow disease",
 ("How does S. aureus genotype B (GTB) differ from other bovine genotypes such as GTC?", ["GTB only infects heifers", "GTB is always methicillin-resistant", "GTB spreads within herds", "GTB never causes clinical mastitis"],
  "GTB spreads within herds, while GTC and other genotypes cause disease in individual cows.", "GTB is contagious."),
 ("¿En qué se diferencia el genotipo B (GTB) de S. aureus de otros genotipos bovinos como GTC?", ["GTB solo infecta vaquillonas", "GTB siempre es resistente a meticilina", "GTB se contagia en el rodeo", "GTB nunca causa mastitis clínica"],
  "GTB se disemina dentro del rodeo, mientras que GTC y otros genotipos enferman a vacas individuales.", "GTB es contagioso.")),
("26585469", "explorer", 0, "CLB was situated in central Europe whereas the other CL were widely disseminated",
 ("Where in Europe was the S. aureus genotype B cluster mainly found?", ["In central Europe", "Only in Scandinavia", "Only in Spain and Portugal", "Evenly in every country"],
  "Cluster B was concentrated in central Europe; the other major clusters were widely spread.", "Central Europe."),
 ("¿En qué parte de Europa se halló sobre todo el grupo del genotipo B de S. aureus?", ["En Europa central", "Solo en Escandinavia", "Solo en España y Portugal", "Por igual en todos los países"],
  "El grupo B se concentraba en Europa central; los otros grupos principales estaban muy difundidos.", "Europa central.")),

# --- Ticino GTB eradication (38788844)
("38788844", "researcher", 1, "Twenty months after the start of the campaign, all of these herds were free from S. aureus GTB",
 ("How long did it take to free all GTB-positive herds in Ticino, Switzerland?", ["About 2 months", "About 20 months", "About 10 years", "It never succeeded"],
  "All 62 initially positive herds were GTB-free 20 months after the campaign started; 73% within 7 months.", "~20 months."),
 ("¿Cuánto tardó la campaña en liberar de GTB a todos los rodeos positivos de Ticino, Suiza?", ["Unos 2 meses", "Unos 20 meses", "Unos 10 años", "Nunca lo logró"],
  "Los 62 rodeos positivos estaban libres de GTB 20 meses después del inicio; el 73% en 7 meses.", "~20 meses.")),
("38788844", "expert", 3, "275 (93.9%) were treated successfully",
 ("What share of GTB-infected cows treated with antibiotics in the Ticino campaign were cured?", ["About 14%", "About 39%", "About 63%", "About 94%"],
  "275 of 293 treated cows (93.9%) became GTB-negative twice by qPCR; others were culled.", "~94%."),
 ("¿Qué proporción de vacas con GTB tratadas con antibióticos en la campaña de Ticino se curó?", ["Cerca del 14%", "Cerca del 39%", "Cerca del 63%", "Cerca del 94%"],
  "275 de 293 vacas tratadas (93,9%) dieron dos veces negativo por qPCR; las demás se descartaron.", "~94%.")),
("38788844", "researcher", 0, "achieved values that no longer differed statistically from those of GTB-free herds after only 2 mo",
 ("What happened to bulk tank SCC in herds under GTB sanitation?", ["Matched GTB-free herds in 2 months", "It rose steadily for two whole years", "It did not change at all", "It fell only after ten years"],
  "Bulk tank SCC dropped quickly and reached the level of GTB-free herds after just 2 months.", "Normal in 2 months."),
 ("¿Qué pasó con el RCS del tanque en los rodeos en saneamiento de GTB?", ["Igualó a los libres en 2 meses", "Subió sin parar durante dos años", "No cambió en absoluto", "Bajó recién a los diez años"],
  "El RCS del tanque bajó rápido y alcanzó el nivel de rodeos libres de GTB en solo 2 meses.", "Normal en 2 meses.")),

# --- GTB in raw milk cheese (24440268)
("24440268", "researcher", 2, "was found to be the most abundant subtype at the sample level (71.8%) as well as among the isolates (62.0%)",
 ("What was the most common S. aureus subtype contaminating Swiss raw milk cheeses?", ["A human hospital MRSA clone", "Livestock-associated CC398", "The mastitis genotype GTB", "Genotype C from single cows"],
  "Enterotoxigenic GTB was in 71.8% of contaminated cheeses, linking udder health to food safety.", "GTB."),
 ("¿Cuál fue el subtipo de S. aureus más común en quesos suizos de leche cruda contaminados?", ["Un clon de SARM hospitalario", "El CC398 asociado al ganado", "El genotipo GTB de mastitis", "El genotipo C de vacas aisladas"],
  "El GTB enterotoxigénico estaba en el 71,8% de los quesos contaminados: la salud de ubre se vincula con la inocuidad.", "GTB.")),

# --- GTB sanitation with qPCR (29753483)
("29753483", "researcher", 1, "the use of clean (instead of aseptically collected) milk samples facilitates sample collection in terms of time and costs",
 ("What practical advantage did the adlb-based qPCR offer for GTB herd sanitation?", ["It needs no milk samples at all", "It works on clean, non-aseptic samples", "It cures the cows during the test", "It detects every S. aureus genotype"],
  "Clean (not aseptic) samples can be taken by farm staff during routine milking, saving time and money.", "Clean samples are enough."),
 ("¿Qué ventaja práctica ofreció la qPCR del gen adlb para sanear rodeos con GTB?", ["No necesita muestras de leche", "Sirve con muestras limpias, no asépticas", "Cura a las vacas durante la prueba", "Detecta todos los genotipos de S. aureus"],
  "Se pueden usar muestras limpias (no asépticas), tomadas por el personal en el ordeño habitual: ahorra tiempo y dinero.", "Muestras limpias bastan.")),

# --- S. agalactiae review (9220132)
("9220132", "explorer", 3, "Protocols for therapy of all infected animals in a herd are generally successful in eradicating the pathogen from the herd",
 ("What usually eradicates Streptococcus agalactiae from a dairy herd?", ["Vaccinating only the heifers", "Changing the bedding to sand", "Waiting for cows to self-cure", "Treating every infected cow"],
  "S. agalactiae is very susceptible to antibiotics; herd-wide treatment plus good hygiene usually eradicates it.", "Treat all infected."),
 ("¿Qué suele erradicar a Streptococcus agalactiae de un rodeo lechero?", ["Vacunar solo a las vaquillonas", "Cambiar la cama por arena", "Esperar a que las vacas se curen solas", "Tratar a todas las vacas infectadas"],
  "S. agalactiae es muy sensible a los antibióticos; tratar a todo el rodeo con buena higiene suele erradicarlo.", "Tratar a todas.")),
("9220132", "researcher", 0, "Streptococcus agalactiae is an oblique parasite of the bovine mammary gland",
 ("Where does Streptococcus agalactiae mainly live, according to this review?", ["In the bovine udder", "In soil and bedding", "In the cow's rumen", "In flies around the barn"],
  "It is an obligate parasite of the udder, which is why herd-wide treatment can eliminate it.", "The udder."),
 ("Según esta revisión, ¿dónde vive principalmente Streptococcus agalactiae?", ["En la ubre bovina", "En el suelo y la cama", "En el rumen de la vaca", "En las moscas del galpón"],
  "Es un parásito obligado de la ubre, por eso tratar a todo el rodeo puede eliminarlo.", "En la ubre.")),

# --- Blitz therapy and S. aureus diagnosis (38921980)
("38921980", "expert", 2, "S. agalactiae showed shedding of bacteria 2.3 times greater than S. aureus",
 ("Why can S. agalactiae infections hide S. aureus in milk culture?", ["They kill S. aureus in the tube", "They change S. aureus into S. agalactiae", "They shed ~2.3 times more bacteria", "They make the milk too acidic"],
  "Heavy S. agalactiae shedding masks S. aureus; its detection rose during blitz therapy.", "Much higher shedding."),
 ("¿Por qué las infecciones por S. agalactiae pueden ocultar a S. aureus en el cultivo de leche?", ["Matan a S. aureus en el tubo", "Transforman a S. aureus en S. agalactiae", "Eliminan ~2,3 veces más bacterias", "Vuelven la leche demasiado ácida"],
  "La gran excreción de S. agalactiae enmascara a S. aureus; su detección aumentó durante la terapia blitz.", "Mucha más excreción.")),

# --- Prototheca (31959834, 36526458, 29780038)
("31959834", "researcher", 1, "P. zopfii GT-II is the genotype associated with acute mastitis and decreased milk production",
 ("Which Prototheca zopfii genotype is associated with acute mastitis?", ["Genotype I", "Genotype II", "Both equally", "Neither causes mastitis"],
  "GT-II (now P. bovis) invades mammary cells and triggers mitochondrial apoptosis; GT-I did not.", "Genotype II."),
 ("¿Qué genotipo de Prototheca zopfii se asocia con mastitis aguda?", ["El genotipo I", "El genotipo II", "Ambos por igual", "Ninguno causa mastitis"],
  "El GT-II (hoy P. bovis) invade células mamarias y desencadena apoptosis mitocondrial; el GT-I no.", "Genotipo II.")),
("36526458", "researcher", 3, "PHMB has the potential to be used for teat and milking-equipment disinfection",
 ("Which disinfectant showed the highest activity against biofilm-producing Prototheca bovis, alongside chlorhexidine?", ["Povidone-iodine", "Sodium hypochlorite", "Sodium dichloroisocyanurate", "Polyhexamethylene biguanide"],
  "PHMB and chlorhexidine inhibited P. bovis at very low concentrations, unlike iodine or hypochlorite.", "PHMB."),
 ("¿Qué desinfectante mostró, junto con la clorhexidina, la mayor actividad contra Prototheca bovis formadora de biofilm?", ["Povidona yodada", "Hipoclorito de sodio", "Dicloroisocianurato de sodio", "Polihexametileno biguanida"],
  "El PHMB y la clorhexidina inhibieron a P. bovis en concentraciones muy bajas, a diferencia del yodo o el hipoclorito.", "PHMB.")),
("29780038", "explorer", 0, "the source of infection is feces",
 ("According to this Japanese study, what is a likely source of Prototheca mastitis?", ["Feces from intestinal infection", "Contaminated antibiotic tubes", "Rainwater on pasture", "Bites from horn flies"],
  "P. zopfii genotype 2 was found in 38% of feces, only in the herd with protothecal mastitis.", "Feces."),
 ("Según este estudio japonés, ¿cuál es una fuente probable de la mastitis por Prototheca?", ["Heces por infección intestinal", "Pomos de antibiótico contaminados", "Agua de lluvia en la pastura", "Picaduras de mosca de los cuernos"],
  "Se halló P. zopfii genotipo 2 en el 38% de las heces, solo en el rodeo con mastitis por Prototheca.", "Las heces.")),

# --- Sensors (22163637)
("22163637", "researcher", 2, "A CM detection system should offer at least a sensitivity of 80% and a specificity of 99%",
 ("What minimum performance should a clinical mastitis sensor system offer?", ["Sensitivity 50%, specificity 50%", "Sensitivity 99%, specificity 80%", "Sensitivity 80%, specificity 99%", "Any sensitivity, specificity 70%"],
  "Detection should reach ≥80% sensitivity and ≥99% specificity within a time window of ≤48 hours.", "80% / 99%."),
 ("¿Qué desempeño mínimo debería tener un sistema de sensores para detectar mastitis clínica?", ["Sensibilidad 50%, especificidad 50%", "Sensibilidad 99%, especificidad 80%", "Sensibilidad 80%, especificidad 99%", "Cualquier sensibilidad, especificidad 70%"],
  "La detección debería lograr ≥80% de sensibilidad y ≥99% de especificidad en una ventana de ≤48 horas.", "80% / 99%.")),
("22163637", "explorer", 1, "None of the described studies satisfied the demands for CM detection models",
 ("How many published sensor detection models met the performance demands for clinical mastitis?", ["All of them", "None of them", "About half", "Only the newest one"],
  "Of 16 studies since 1992, none satisfied the requirements, partly due to varied time windows.", "None."),
 ("¿Cuántos modelos publicados de detección por sensores cumplían las exigencias para mastitis clínica?", ["Todos", "Ninguno", "Cerca de la mitad", "Solo el más nuevo"],
  "De 16 estudios desde 1992, ninguno cumplía los requisitos, en parte por las distintas ventanas de tiempo.", "Ninguno.")),

# --- BLV and mastitis (36424322)
("36424322", "researcher", 3, "The hazard ratio of subclinical mastitis for H-PVL cows was 2.61 times higher than that of non-infected cows",
 ("How did a high bovine leukemia virus proviral load affect subclinical mastitis risk?", ["It lowered the risk by half", "It had no effect at all", "It only affected beef cows", "About 2.6 times higher risk"],
  "High-proviral-load cows had a 2.61-fold hazard; half developed subclinical mastitis within 52 days.", "~2.6× higher."),
 ("¿Cómo afectó una carga proviral alta del virus de la leucosis bovina al riesgo de mastitis subclínica?", ["Lo redujo a la mitad", "No tuvo ningún efecto", "Solo afectó a vacas de carne", "Un riesgo ~2,6 veces mayor"],
  "Las vacas con carga proviral alta tenían un riesgo 2,61 veces mayor; la mitad tuvo mastitis subclínica en 52 días.", "~2,6 veces más.")),

# --- DCT and AMR post-calving (37546337)
("37546337", "expert", 0, "The study provided evidence that dry-cow IMM AMD was associated with AMR post-calving",
 ("What did this study find about antibiotic dry cow therapy and resistance after calving?", ["DCT was linked to more resistance", "DCT removed all resistance genes", "DCT had no link with resistance", "DCT only affected coliforms"],
  "CNS from treated cows showed higher resistance to drugs of the same class used at dry-off.", "Linked to resistance."),
 ("¿Qué halló este estudio sobre la terapia antibiótica de secado y la resistencia tras el parto?", ["Se asoció con más resistencia", "Eliminó todos los genes de resistencia", "No tuvo relación con la resistencia", "Solo afectó a los coliformes"],
  "Los ECN de vacas tratadas mostraron más resistencia a fármacos de la misma clase usada al secado.", "Asociada a resistencia.")),

# --- MRSA in bovine mastitis (21984431)
("21984431", "researcher", 2, "The establishment of the sequence type 398 (ST398) in farm animals, primarily pigs, in the early 2000's has provided a reservoir of infection for humans and dairy cattle",
 ("Which livestock-associated MRSA lineage, first established in pigs, became a reservoir for humans and dairy cows?", ["USA300", "CC151", "ST398", "CC97"],
  "LA-MRSA ST398 spread from pigs in the early 2000s and later caused bovine udder infections.", "ST398."),
 ("¿Qué linaje de SARM asociado al ganado, establecido primero en cerdos, se volvió reservorio para humanos y vacas?", ["USA300", "CC151", "ST398", "CC97"],
  "El SARM ST398 se difundió desde cerdos a inicios de los 2000 y luego causó infecciones de ubre bovinas.", "ST398.")),

# --- European S. aureus genomics (33097797)
("33097797", "expert", 3, "Compared to CC151, CC479 was associated with CM rather than SCM",
 ("Which S. aureus clonal complex was associated with clinical rather than subclinical mastitis in Europe?", ["CC151", "CC97", "CC398", "CC479"],
  "CC479 had 3.6-fold odds of clinical mastitis compared with the dominant CC151.", "CC479."),
 ("¿Qué complejo clonal de S. aureus se asoció con mastitis clínica más que subclínica en Europa?", ["CC151", "CC97", "CC398", "CC479"],
  "CC479 tuvo 3,6 veces más chances de mastitis clínica que el CC151 dominante.", "CC479.")),

# --- Danish lactational treatment trends (37419739)
("37419739", "researcher", 1, "the total number of lactational treatments appears to have decreased steadily over the study period, whereas treatment duration increased slightly",
 ("How did lactational mastitis treatment change in Danish herds from 2010 to 2019?", ["More treatments, each one shorter", "Fewer, slightly longer treatments", "No change in any respect", "Treatment was banned in 2015"],
  "Treatments decreased steadily while duration rose slightly; fewer samples were sent for pathogen analysis.", "Fewer, slightly longer."),
 ("¿Cómo cambió el tratamiento de mastitis en lactancia en los rodeos daneses entre 2010 y 2019?", ["Más tratamientos, cada uno más corto", "Menos tratamientos, algo más largos", "Ningún cambio en ningún aspecto", "Se prohibió tratar en 2015"],
  "Los tratamientos bajaron de forma constante y su duración aumentó un poco; se enviaron menos muestras a analizar.", "Menos y algo más largos.")),

# --- S. aureus cure factors (16702252)
("16702252", "researcher", 0, "The most important treatment factor affecting cure is treatment duration",
 ("Which treatment factor most affects the cure of S. aureus mastitis?", ["Treatment duration", "Time of day of the dose", "Brand of the teat dip", "Color of the drug tube"],
  "Longer treatment increases the chance of cure, though extended therapy is not always economical.", "Duration."),
 ("¿Qué factor del tratamiento influye más en la cura de la mastitis por S. aureus?", ["La duración del tratamiento", "La hora del día de la dosis", "La marca del sellador de pezón", "El color del pomo del fármaco"],
  "Tratar más tiempo aumenta la chance de cura, aunque la terapia prolongada no siempre es rentable.", "La duración.")),
("16702252", "explorer", 2, "Staphylococcus aureus mastitis in hind quarters has a low cure rate compared with front quarters",
 ("Which udder quarters have a lower cure rate for S. aureus mastitis?", ["Front quarters", "Left quarters", "Hind quarters", "Right quarters"],
  "Cure rates are lower in hind quarters, older cows, high SCC and long-standing infections.", "Hind quarters."),
 ("¿Qué cuartos de la ubre tienen menor tasa de cura de la mastitis por S. aureus?", ["Los cuartos delanteros", "Los cuartos izquierdos", "Los cuartos traseros", "Los cuartos derechos"],
  "La cura es menor en cuartos traseros, vacas viejas, RCS alto e infecciones de larga data.", "Los traseros.")),
("16702252", "expert", 3, "treatment of older animals, chronic infections, or penicillin-resistant isolates should be discouraged",
 ("For which S. aureus mastitis cases is treatment generally discouraged?", ["Young cows with penicillin-sensitive strains", "First-lactation heifers in early lactation", "Any cow with a single high SCC", "Old cows, chronic or penicillin-resistant cases"],
  "Treating young cows with penicillin-sensitive strains is often justified; old, chronic or resistant cases are not.", "Old, chronic, resistant."),
 ("¿En qué casos de mastitis por S. aureus se desaconseja en general tratar?", ["Vacas jóvenes con cepas sensibles a penicilina", "Vaquillonas en la lactancia temprana", "Cualquier vaca con un solo RCS alto", "Vacas viejas, crónicas o con cepas resistentes"],
  "Tratar vacas jóvenes con cepas sensibles suele justificarse; casos viejos, crónicos o resistentes no.", "Viejas, crónicas, resistentes.")),
]
