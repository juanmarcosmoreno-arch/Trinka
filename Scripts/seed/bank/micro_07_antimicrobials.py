# General microbiology VII — antimicrobial agents, resistance in practice, stewardship and microbiota.
# Sources: StatPearls chapters and PubMed reviews (abstracts). Excerpts verbatim.
CATEGORY = "microbiology"
Q = [
# --- Penicillin (32119447)
("32119447", "beginner", 3, "within the β-lactam antibiotic class of drugs",
 ("To which antibiotic class does penicillin belong?", ["Aminoglycosides", "Macrolides", "Tetracyclines", "β-lactams"],
  "Penicillin is the founding member of the β-lactam class, which also includes cephalosporins and carbapenems.", "β-lactams."),
 ("¿A qué clase de antibióticos pertenece la penicilina?", ["Aminoglucósidos", "Macrólidos", "Tetraciclinas", "Betalactámicos"],
  "La penicilina es el miembro fundador de los betalactámicos, que incluyen también cefalosporinas y carbapenémicos.", "Betalactámicos.")),
("32119447", "curious", 1, "Penicillin functions by inhibiting the cross-linking of peptidoglycan within the cell wall",
 ("How does penicillin kill bacteria?", ["Blocking protein synthesis at the 30S ribosome", "Inhibiting peptidoglycan cross-linking in the cell wall", "Inhibiting DNA gyrase", "Disrupting the outer membrane like a detergent"],
  "Penicillin inhibits peptidoglycan cross-linking, weakening the wall so the cell lyses osmotically.", "Blocks cell wall cross-linking."),
 ("¿Cómo mata la penicilina a las bacterias?", ["Bloquea la síntesis proteica en el ribosoma 30S", "Inhibe el entrecruzamiento del peptidoglucano de la pared", "Inhibe la ADN girasa", "Rompe la membrana externa como un detergente"],
  "La penicilina inhibe el entrecruzamiento del peptidoglucano; la pared se debilita y la célula se lisa por ósmosis.", "Bloquea el entrecruzamiento de la pared.")),

# --- Cephalosporins (31855361)
("31855361", "explorer", 2, "Cefiderocol is a novel siderophore cephalosporin",
 ("What is special about cefiderocol?", ["It is a macrolide", "It only works on gram-positives", "It is a siderophore cephalosporin that hijacks iron uptake to enter gram-negatives", "It is an antifungal"],
  "Cefiderocol is a siderophore cephalosporin active against highly resistant gram-negatives such as P. aeruginosa and A. baumannii.", "Siderophore cephalosporin."),
 ("¿Qué tiene de especial el cefiderocol?", ["Es un macrólido", "Solo actúa sobre grampositivas", "Es una cefalosporina sideróforo que usa la captación de hierro para entrar en gramnegativas", "Es un antifúngico"],
  "El cefiderocol es una cefalosporina sideróforo activa contra gramnegativos muy resistentes como P. aeruginosa y A. baumannii.", "Cefalosporina sideróforo.")),
("31855361", "curious", 0, "The 5 generations of cephalosporins",
 ("How are cephalosporins traditionally grouped?", ["Into 5 generations", "Into 2 types only", "By the color of the vial", "By the fungus that produces them"],
  "Cephalosporins are grouped into five generations with differing spectra against gram-positive and gram-negative bacteria.", "Five generations."),
 ("¿Cómo se agrupan tradicionalmente las cefalosporinas?", ["En 5 generaciones", "Solo en 2 tipos", "Por el color del frasco", "Por el hongo que las produce"],
  "Las cefalosporinas se agrupan en cinco generaciones con distinto espectro frente a grampositivas y gramnegativas.", "Cinco generaciones.")),

# --- Vancomycin (29083794)
("29083794", "curious", 3, "Vancomycin is a tricyclic glycopeptide antibiotic used to treat severe gram-positive bacterial infections, including those caused by methicillin-resistant Staphylococcus aureus",
 ("Vancomycin is mainly used to treat…", ["Gram-negative urinary infections", "Fungal infections", "Viral pneumonia", "Severe gram-positive infections such as MRSA"],
  "Vancomycin, a glycopeptide cell-wall inhibitor, treats severe gram-positive infections including MRSA.", "Gram-positives incl. MRSA."),
 ("La vancomicina se usa principalmente para tratar…", ["Infecciones urinarias por gramnegativos", "Infecciones fúngicas", "Neumonía viral", "Infecciones graves por grampositivos como SAMR"],
  "La vancomicina, glicopéptido inhibidor de la pared, trata infecciones graves por grampositivos, incluido el SAMR.", "Grampositivos, incl. SAMR.")),

# --- Aminoglycosides (31082149)
("31082149", "explorer", 1, "Aminoglycosides have a broad spectrum of activity covering aerobic organisms, including gram-negative bacteria and mycobacteria",
 ("Which organisms do aminoglycosides typically cover?", ["Anaerobes only", "Aerobic organisms, including gram-negatives and mycobacteria", "Fungi", "Viruses"],
  "Aminoglycosides (gentamicin, amikacin, streptomycin…) cover aerobes; they need oxygen-dependent uptake, so anaerobes are resistant.", "Aerobes, gram-negatives, mycobacteria."),
 ("¿Qué organismos cubren típicamente los aminoglucósidos?", ["Solo anaerobios", "Organismos aerobios, incluidos gramnegativos y micobacterias", "Hongos", "Virus"],
  "Los aminoglucósidos (gentamicina, amikacina, estreptomicina…) cubren aerobios; su captación depende de oxígeno, por eso los anaerobios son resistentes.", "Aerobios, gramnegativos, micobacterias.")),

# --- Macrolides (31855339)
("31855339", "explorer", 0, "Clarithromycin is used to treat Helicobacter pylori infections in standard triple therapy protocol",
 ("Which macrolide is part of standard triple therapy for Helicobacter pylori?", ["Clarithromycin", "Azithromycin", "Erythromycin", "Fidaxomicin"],
  "Clarithromycin is used with a proton-pump inhibitor and amoxicillin (or metronidazole) in triple therapy.", "Clarithromycin."),
 ("¿Qué macrólido forma parte de la triple terapia estándar contra Helicobacter pylori?", ["Claritromicina", "Azitromicina", "Eritromicina", "Fidaxomicina"],
  "La claritromicina se usa con un inhibidor de bomba de protones y amoxicilina (o metronidazol) en la triple terapia.", "Claritromicina.")),

# --- Tetracyclines (31751095)
("31751095", "curious", 2, "Tetracyclines classify as protein synthesis inhibitor antibiotics and are considered to be broad-spectrum",
 ("How do tetracyclines act?", ["Inhibit cell wall synthesis", "Inhibit folate synthesis", "Inhibit bacterial protein synthesis", "Disrupt fungal membranes"],
  "Tetracyclines (doxycycline, minocycline, tigecycline) are broad-spectrum protein synthesis inhibitors.", "Protein synthesis inhibitors."),
 ("¿Cómo actúan las tetraciclinas?", ["Inhiben la síntesis de pared", "Inhiben la síntesis de folato", "Inhiben la síntesis proteica bacteriana", "Alteran membranas fúngicas"],
  "Las tetraciclinas (doxiciclina, minociclina, tigeciclina) son inhibidores de la síntesis proteica de amplio espectro.", "Inhiben la síntesis proteica.")),

# --- TMP-SMX (30020604)
("30020604", "explorer", 3, "The combination exerts a synergistic bactericidal effect by sequential inhibition of bacterial folate synthesis",
 ("Why are trimethoprim and sulfamethoxazole combined?", ["They block two different ribosomal subunits", "One kills fungi and the other bacteria", "To reduce cost only", "They inhibit two sequential steps of folate synthesis, acting synergistically"],
  "Sulfamethoxazole and trimethoprim block successive steps of bacterial folate synthesis, producing synergy.", "Sequential folate blockade."),
 ("¿Por qué se combinan trimetoprima y sulfametoxazol?", ["Bloquean dos subunidades ribosomales distintas", "Uno mata hongos y el otro bacterias", "Solo para bajar el costo", "Inhiben dos pasos sucesivos de la síntesis de folato, con efecto sinérgico"],
  "El sulfametoxazol y la trimetoprima bloquean pasos sucesivos de la síntesis bacteriana de folato, con sinergia.", "Bloqueo secuencial del folato.")),
("30020604", "researcher", 1, "treatment and prophylaxis of Pneumocystis jirovecii pneumonia and toxoplasmosis",
 ("Besides urinary infections, TMP-SMX is a drug of choice for treating and preventing…", ["Tuberculous meningitis", "Pneumocystis jirovecii pneumonia", "Candida esophagitis", "Influenza"],
  "TMP-SMX treats and prevents Pneumocystis pneumonia (and toxoplasmosis), key in HIV care.", "Pneumocystis pneumonia."),
 ("Además de infecciones urinarias, TMP-SMX es de elección para tratar y prevenir…", ["Meningitis tuberculosa", "Neumonía por Pneumocystis jirovecii", "Esofagitis por Candida", "Influenza"],
  "TMP-SMX trata y previene la neumonía por Pneumocystis (y la toxoplasmosis), clave en la atención del VIH.", "Neumonía por Pneumocystis.")),

# --- Metronidazole (30969550)
("30969550", "curious", 0, "Metronidazole is one of the mainstay drugs for the treatment of anaerobic bacterial infections, protozoal infections",
 ("Metronidazole is a mainstay against which organisms?", ["Anaerobic bacteria and protozoa", "Aerobic gram-positive cocci", "Mycobacteria", "Dermatophytes"],
  "Metronidazole treats anaerobic and microaerophilic bacteria and protozoa such as Entamoeba, Giardia and Trichomonas.", "Anaerobes and protozoa."),
 ("¿Contra qué organismos es pilar el metronidazol?", ["Bacterias anaerobias y protozoos", "Cocos grampositivos aerobios", "Micobacterias", "Dermatofitos"],
  "El metronidazol trata bacterias anaerobias y microaerófilas y protozoos como Entamoeba, Giardia y Trichomonas.", "Anaerobios y protozoos.")),

# --- Linezolid (30969615)
("30969615", "researcher", 2, "Linezolid is a synthetic oxazolidinone antimicrobial drug indicated for gram-positive infections",
 ("Linezolid belongs to which class and targets which bacteria?", ["Glycopeptide; gram-negatives", "Lipopeptide; anaerobes", "Oxazolidinone; gram-positives, including VRE", "Polymyxin; Pseudomonas"],
  "Linezolid is a synthetic oxazolidinone for gram-positive infections, including vancomycin-resistant enterococci.", "Oxazolidinone; gram-positives."),
 ("¿A qué clase pertenece el linezolid y contra qué bacterias actúa?", ["Glicopéptido; gramnegativas", "Lipopéptido; anaerobios", "Oxazolidinona; grampositivas, incluido ERV", "Polimixina; Pseudomonas"],
  "El linezolid es una oxazolidinona sintética para infecciones por grampositivos, incluidos enterococos resistentes a vancomicina.", "Oxazolidinona; grampositivas.")),

# --- Daptomycin (29261926)
("29261926", "expert", 3, "Daptomycin is a cyclic lipopeptide antibiotic derived from the organism Streptomyces roseosporus",
 ("Daptomycin is a…", ["β-lactam from Penicillium", "Aminoglycoside from Streptomyces griseus", "Glycopeptide from Amycolatopsis", "Cyclic lipopeptide from Streptomyces roseosporus"],
  "Daptomycin is a cyclic lipopeptide active against gram-positives including MRSA and VRE.", "Cyclic lipopeptide."),
 ("La daptomicina es un…", ["Betalactámico de Penicillium", "Aminoglucósido de Streptomyces griseus", "Glicopéptido de Amycolatopsis", "Lipopéptido cíclico de Streptomyces roseosporus"],
  "La daptomicina es un lipopéptido cíclico activo contra grampositivos, incluidos SAMR y ERV.", "Lipopéptido cíclico.")),

# --- Rifampin (32491420)
("32491420", "explorer", 1, "Rifampin exerts bactericidal antimicrobial effects by inhibiting DNA-dependent RNA polymerase",
 ("What is the target of rifampin?", ["DNA gyrase", "DNA-dependent RNA polymerase", "Peptidoglycan transpeptidase", "50S ribosome"],
  "Rifampin inhibits bacterial DNA-dependent RNA polymerase, blocking transcription.", "RNA polymerase."),
 ("¿Cuál es el blanco de la rifampicina?", ["ADN girasa", "ARN polimerasa dependiente de ADN", "Transpeptidasa del peptidoglucano", "Ribosoma 50S"],
  "La rifampicina inhibe la ARN polimerasa bacteriana dependiente de ADN y bloquea la transcripción.", "ARN polimerasa.")),

# --- Isoniazid (32491549)
("32491549", "researcher", 0, "INH functions as a prodrug activated by the catalase-peroxidase KatG",
 ("How is isoniazid activated inside Mycobacterium tuberculosis?", ["By the catalase-peroxidase KatG", "By gastric acid", "By human liver enzymes only", "It needs no activation"],
  "INH is a prodrug activated by mycobacterial KatG; katG mutations are a classic cause of INH resistance.", "KatG."),
 ("¿Cómo se activa la isoniazida dentro de Mycobacterium tuberculosis?", ["Por la catalasa-peroxidasa KatG", "Por el ácido gástrico", "Solo por enzimas hepáticas humanas", "No necesita activación"],
  "La INH es una prodroga activada por KatG micobacteriana; las mutaciones de katG son causa clásica de resistencia.", "KatG.")),
("32491549", "expert", 2, "inhibit the production of mycolic acids, the essential components of the mycobacterium's cell wall",
 ("Which mycobacterial cell-wall component does isoniazid prevent from being made?", ["Peptidoglycan", "Lipopolysaccharide", "Mycolic acids", "Teichoic acids"],
  "Activated INH inhibits mycolic acid synthesis, essential for the mycobacterial wall (and acid-fastness).", "Mycolic acids."),
 ("¿Qué componente de la pared micobacteriana impide sintetizar la isoniazida?", ["Peptidoglucano", "Lipopolisacárido", "Ácidos micólicos", "Ácidos teicoicos"],
  "La INH activada inhibe la síntesis de ácidos micólicos, esenciales para la pared micobacteriana (y la ácido-alcohol resistencia).", "Ácidos micólicos.")),

# --- CRE (31869168)
("31869168", "researcher", 3, "Structurally, carbapenems are similar to penicillins but have the addition of a pyrroline ring",
 ("Structurally, how do carbapenems differ from penicillins?", ["They lack a β-lactam ring", "They contain a macrolactone ring", "They are peptides", "They have an added pyrroline ring that protects the β-lactam ring"],
  "The pyrroline ring protects the β-lactam ring from many β-lactamases, giving carbapenems their broad spectrum.", "Pyrroline ring."),
 ("Estructuralmente, ¿en qué se diferencian los carbapenémicos de las penicilinas?", ["No tienen anillo betalactámico", "Tienen un anillo macrolactona", "Son péptidos", "Tienen un anillo pirrolina agregado que protege al anillo betalactámico"],
  "El anillo pirrolina protege al anillo betalactámico de muchas betalactamasas, de ahí su amplio espectro.", "Anillo pirrolina.")),
("31869168", "explorer", 1, "Bacteria may have multiple resistance mechanisms to carbapenems, but the most common is carbapenemase enzyme production",
 ("What is the most common mechanism of carbapenem resistance in Enterobacterales?", ["Thicker capsule", "Carbapenemase production", "Spore formation", "Loss of flagella"],
  "Carbapenemase production is most common; efflux pumps and porin loss also contribute.", "Carbapenemases."),
 ("¿Cuál es el mecanismo más común de resistencia a carbapenémicos en Enterobacterales?", ["Cápsula más gruesa", "Producción de carbapenemasas", "Formación de esporas", "Pérdida de flagelos"],
  "La producción de carbapenemasas es lo más frecuente; las bombas de eflujo y la pérdida de porinas también contribuyen.", "Carbapenemasas.")),
("31869168", "expert", 0, "extended-spectrum beta-lactamases (ESBL), which are enzymes that hydrolyze penicillins, third-generation cephalosporins, and monobactams",
 ("Which antibiotics do ESBLs typically hydrolyze?", ["Penicillins, third-generation cephalosporins and monobactams", "Carbapenems only", "Aminoglycosides", "Vancomycin"],
  "ESBLs hydrolyze penicillins, 3rd-generation cephalosporins and monobactams; carbapenems usually remain active.", "Penicillins, 3rd-gen cephalosporins, monobactams."),
 ("¿Qué antibióticos hidrolizan típicamente las BLEE?", ["Penicilinas, cefalosporinas de tercera generación y monobactámicos", "Solo carbapenémicos", "Aminoglucósidos", "Vancomicina"],
  "Las BLEE hidrolizan penicilinas, cefalosporinas de 3.ª generación y monobactámicos; los carbapenémicos suelen conservar actividad.", "Penicilinas, C3G, monobactámicos.")),

# --- Polymyxins (32491472)
("32491472", "researcher", 2, "infected by susceptible strains of gram-negative pathogens resistant most of the other antibiotic classes",
 ("When are polymyxins (e.g., colistin) typically used?", ["As first-line for strep throat", "For fungal infections", "As last-resort agents for multidrug-resistant gram-negatives", "To treat viral hepatitis"],
  "Polymyxins are reserved for multidrug-resistant gram-negatives (e.g., P. aeruginosa) resistant to most other classes.", "Last resort for MDR gram-negatives."),
 ("¿Cuándo se usan típicamente las polimixinas (p. ej., colistina)?", ["Como primera línea en faringitis", "Para infecciones fúngicas", "Como último recurso frente a gramnegativos multirresistentes", "Para hepatitis viral"],
  "Las polimixinas se reservan para gramnegativos multirresistentes (p. ej., P. aeruginosa) resistentes a casi todo lo demás.", "Último recurso.")),

# --- Nitrofurantoin (29262089)
("29262089", "explorer", 0, "it concentrates in the lower urinary tract while maintaining a low serum concentration",
 ("Why is nitrofurantoin useful for uncomplicated cystitis but not for systemic infections?", ["It concentrates in the lower urinary tract with low serum levels", "It only works in the lungs", "It is inactivated in urine", "It is only active against fungi"],
  "Nitrofurantoin reaches high urinary concentrations but low serum levels and spares bowel flora — ideal for lower UTIs.", "Concentrates in urine."),
 ("¿Por qué la nitrofurantoína sirve para cistitis no complicada pero no para infecciones sistémicas?", ["Se concentra en la vía urinaria baja con niveles séricos bajos", "Solo actúa en pulmones", "Se inactiva en la orina", "Solo es activa contra hongos"],
  "La nitrofurantoína alcanza altas concentraciones urinarias con bajos niveles séricos y respeta la flora intestinal: ideal para ITU bajas.", "Se concentra en orina.")),

# --- Stewardship (28882725)
("28882725", "curious", 1, "typically referring to programmes and interventions that aim to optimize antimicrobial use",
 ("What does \"antimicrobial stewardship\" refer to?", ["Developing new antibiotics", "Programs and interventions that optimize antimicrobial use", "Selling antibiotics without prescription", "Vaccinating livestock"],
  "Stewardship is a coherent set of actions promoting responsible antimicrobial use, in human and animal health (One Health).", "Optimizing antimicrobial use."),
 ("¿A qué se refiere el \"uso racional de antimicrobianos\" (antimicrobial stewardship)?", ["Desarrollar antibióticos nuevos", "Programas e intervenciones que optimizan el uso de antimicrobianos", "Vender antibióticos sin receta", "Vacunar ganado"],
  "El stewardship es un conjunto coherente de acciones para usar antimicrobianos de forma responsable, en salud humana y animal (Una Salud).", "Optimizar el uso.")),

# --- Gut microbiota (32887946)
("32887946", "explorer", 2, "may contribute to the metabolic health of the human host and, when aberrant, to the pathogenesis of various common metabolic disorders including obesity, type 2 diabetes",
 ("Which conditions have been associated with an altered gut microbiota?", ["Only infectious diarrhea", "Fractures and sprains", "Metabolic disorders such as obesity and type 2 diabetes", "Color blindness"],
  "Observational studies link aberrant gut microbiota to obesity, type 2 diabetes, fatty liver and cardiometabolic disease.", "Metabolic diseases."),
 ("¿Qué condiciones se han asociado a una microbiota intestinal alterada?", ["Solo diarrea infecciosa", "Fracturas y esguinces", "Trastornos metabólicos como obesidad y diabetes tipo 2", "Daltonismo"],
  "Estudios observacionales vinculan una microbiota alterada con obesidad, diabetes tipo 2, hígado graso y enfermedad cardiometabólica.", "Enfermedades metabólicas.")),
("32887946", "expert", 3, "research is moving from descriptive microbiota census analyses to cause-and-effect studies",
 ("What is the main limitation of much gut-microbiota research to date?", ["It cannot sequence DNA", "It only studies viruses", "It ignores diet entirely", "Many findings are associations; causal mechanisms are still being established"],
  "Much evidence is observational; the field is moving to cause-and-effect studies using multi-omics and experiments.", "Association ≠ causation."),
 ("¿Cuál es la principal limitación de gran parte de la investigación sobre microbiota?", ["No puede secuenciar ADN", "Solo estudia virus", "Ignora la dieta", "Muchos hallazgos son asociaciones; los mecanismos causales aún se están estableciendo"],
  "Buena parte de la evidencia es observacional; el campo avanza hacia estudios de causa-efecto con multiómica y experimentos.", "Asociación ≠ causalidad.")),
]
