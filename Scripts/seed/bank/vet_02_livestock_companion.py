# Veterinary microbiology II — diseases of cattle, pigs, poultry, horses, dogs and cats; transboundary
# animal diseases and prions. Sources: PubMed reviews (abstracts). Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- Bovine mastitis (33509059, 32051050)
("33509059", "beginner", 1, "Bovine mastitis is the inflammation of the mammary glands/udder of bovines, caused by bacterial pathogens, in most cases",
 ("What is bovine mastitis?", ["Inflammation of the hoof", "Inflammation of the udder, usually bacterial", "A viral pneumonia of calves", "A parasitic disease of the liver"],
  "Mastitis is inflammation of the udder, most often caused by bacteria; it causes major losses in dairy farming.", "Udder inflammation."),
 ("¿Qué es la mastitis bovina?", ["Inflamación de la pezuña", "Inflamación de la ubre, generalmente bacteriana", "Una neumonía viral de terneros", "Una parasitosis hepática"],
  "La mastitis es la inflamación de la ubre, casi siempre bacteriana; causa grandes pérdidas en la lechería.", "Inflamación de la ubre.")),
("33509059", "curious", 3, "Routine diagnosis is based on clinical and subclinical forms of the disease",
 ("Which two forms of mastitis must dairy diagnosis consider?", ["Acute and congenital", "Viral and fungal only", "Bilateral and unilateral", "Clinical and subclinical"],
  "Mastitis can be clinical (visible changes) or subclinical (no visible signs, detected by tests such as somatic cell counts).", "Clinical and subclinical."),
 ("¿Qué dos formas de mastitis debe considerar el diagnóstico en tambo?", ["Aguda y congénita", "Solo viral y fúngica", "Bilateral y unilateral", "Clínica y subclínica"],
  "La mastitis puede ser clínica (cambios visibles) o subclínica (sin signos, detectada por pruebas como el recuento de células somáticas).", "Clínica y subclínica.")),
("32051050", "explorer", 0, "Mastitis may have a negative impact on human health by inducing antibiotic-resistant pathogens that may spread",
 ("Why is bovine mastitis also a public health concern?", ["It can select antibiotic-resistant pathogens that spread", "It causes mastitis in people who drink milk", "It is transmitted by mosquitoes", "It contaminates water with prions"],
  "Antibiotic use against mastitis can select resistant pathogens that may reach humans (One Health).", "Antibiotic resistance."),
 ("¿Por qué la mastitis bovina también es un problema de salud pública?", ["Puede seleccionar patógenos resistentes a antibióticos que se diseminan", "Causa mastitis a quienes toman leche", "La transmiten mosquitos", "Contamina el agua con priones"],
  "El uso de antibióticos contra la mastitis puede seleccionar patógenos resistentes que lleguen al ser humano (Una Salud).", "Resistencia antibiótica.")),
("33509059", "researcher", 2, "all of them lacked the efficacy to eliminate the associated etiological agent when used as a monotherapy",
 ("What has been a recurring limitation of mastitis treatments evaluated as single therapies?", ["They are too cheap", "They cannot be given to cows", "As monotherapy, none reliably eliminates the causative agent", "They all cause prion disease"],
  "Antibiotics, phages, probiotics and other options each lacked efficacy as monotherapy, driving interest in combined and preventive strategies.", "Monotherapy fails to eliminate."),
 ("¿Qué limitación recurrente mostraron los tratamientos de mastitis evaluados como terapia única?", ["Son demasiado baratos", "No se pueden dar a vacas", "Como monoterapia, ninguno elimina de forma fiable al agente", "Todos causan enfermedad priónica"],
  "Antibióticos, fagos, probióticos y otras opciones carecieron de eficacia como monoterapia, lo que impulsa estrategias combinadas y preventivas.", "La monoterapia no elimina.")),

# --- Bovine TB (39055751)
("39055751", "curious", 2, "is brought on by the Mycobacterium bovis bacteria, which can infect both people and animals",
 ("Which organism causes bovine tuberculosis?", ["Mycobacterium leprae", "Mycobacterium avium", "Mycobacterium bovis", "Brucella abortus"],
  "Bovine TB is caused by Mycobacterium bovis, a zoonotic pathogen of cattle and humans.", "Mycobacterium bovis."),
 ("¿Qué organismo causa la tuberculosis bovina?", ["Mycobacterium leprae", "Mycobacterium avium", "Mycobacterium bovis", "Brucella abortus"],
  "La TB bovina la causa Mycobacterium bovis, patógeno zoonótico de bovinos y humanos.", "Mycobacterium bovis.")),
("39055751", "explorer", 1, "The tuberculin test is the primary method for detecting bovine tuberculosis in cows",
 ("What is the primary test used to detect bovine tuberculosis in live cattle?", ["Blood culture", "Tuberculin skin test", "Rectal palpation", "Milk Gram stain"],
  "The tuberculin test is the main screening tool; positives are removed under test-and-cull programs.", "Tuberculin test."),
 ("¿Cuál es la prueba principal para detectar tuberculosis bovina en animales vivos?", ["Hemocultivo", "Prueba de tuberculina", "Palpación rectal", "Gram de la leche"],
  "La tuberculina es la principal herramienta de tamizaje; los positivos se eliminan en programas de prueba y sacrificio.", "Tuberculina.")),
("39055751", "researcher", 3, "developed nations have implemented routine testing and culling of infected animals under national mandatory programs",
 ("How have developed countries controlled bovine tuberculosis?", ["Treating all cattle with isoniazid", "Mass vaccination of humans", "Banning milk consumption", "Mandatory routine testing and culling of infected animals"],
  "National test-and-cull programs, plus milk pasteurization, have been key to controlling bovine TB.", "Test and cull."),
 ("¿Cómo controlaron los países desarrollados la tuberculosis bovina?", ["Tratando todo el ganado con isoniazida", "Vacunando masivamente a personas", "Prohibiendo la leche", "Pruebas obligatorias de rutina y sacrificio de animales infectados"],
  "Los programas nacionales de prueba y sacrificio, junto con la pasteurización, fueron clave para controlar la TB bovina.", "Prueba y sacrificio.")),

# --- FMD (38462419)
("38462419", "curious", 0, "The disease causes a highly contagious vesicular syndrome of cloven-hoofed animals",
 ("Foot-and-mouth disease affects…", ["Cloven-hoofed animals, causing a vesicular syndrome", "Only horses", "Only humans", "Only poultry"],
  "FMD is a highly contagious viral vesicular disease of cloven-hoofed animals (cattle, pigs, sheep, goats).", "Cloven-hoofed animals."),
 ("La fiebre aftosa afecta a…", ["Animales de pezuña hendida, con un síndrome vesicular", "Solo caballos", "Solo humanos", "Solo aves"],
  "La aftosa es una enfermedad vesicular viral muy contagiosa de animales de pezuña hendida (bovinos, cerdos, ovinos, caprinos).", "Pezuña hendida.")),
("38462419", "explorer", 2, "is an important determinant of global trade in animal products",
 ("Why does foot-and-mouth disease matter so much economically?", ["It kills most infected humans", "It contaminates crops", "Its presence restricts international trade in animal products", "It has no economic effect"],
  "FMD status determines access to international markets for meat and animal products.", "Trade restrictions."),
 ("¿Por qué la fiebre aftosa es tan importante económicamente?", ["Mata a la mayoría de los humanos infectados", "Contamina cultivos", "Su presencia restringe el comercio internacional de productos animales", "No tiene efecto económico"],
  "El estatus sanitario frente a la aftosa determina el acceso a mercados internacionales de carne y productos animales.", "Restricciones comerciales.")),

# --- ASF (30836106, 31743062)
("31743062", "explorer", 3, "African swine fever is a devastating disease that can result in death in almost all infected pigs",
 ("What is characteristic of African swine fever in domestic pigs?", ["It is mild and self-limited", "It infects humans", "It is caused by a bacterium", "It can kill almost all infected pigs"],
  "ASF can cause near-total mortality in domestic pigs; it does not infect humans.", "Very high mortality."),
 ("¿Qué caracteriza a la peste porcina africana en cerdos domésticos?", ["Es leve y autolimitada", "Infecta humanos", "La causa una bacteria", "Puede matar a casi todos los cerdos infectados"],
  "La PPA puede causar mortalidad casi total en cerdos domésticos; no infecta al ser humano.", "Mortalidad muy alta.")),
("31743062", "researcher", 1, "The African swine fever virus is an unusual complex DNA virus and is not related to other viruses. This has presented challenges for vaccine development",
 ("Why has vaccine development against African swine fever been so difficult?", ["The virus is an RNA virus that mutates daily", "ASFV is an unusual, complex DNA virus unrelated to other viruses", "Pigs do not produce antibodies", "The disease is not transmissible"],
  "ASFV is a large, complex DNA virus unlike others, complicating vaccine design.", "Complex, unique DNA virus."),
 ("¿Por qué ha sido tan difícil desarrollar una vacuna contra la peste porcina africana?", ["Es un virus ARN que muta a diario", "El VPPA es un virus ADN complejo e inusual, sin parentesco con otros", "Los cerdos no producen anticuerpos", "No es transmisible"],
  "El VPPA es un virus ADN grande y complejo, distinto de otros, lo que complica el diseño de vacunas.", "Virus ADN complejo y único.")),
("30836106", "expert", 0, "has heightened awareness of the threat posed by this devastating disease to the global pig industry and food security",
 ("Why is the recent spread of African swine fever to Europe and Asia a global concern?", ["It threatens the global pig industry and food security", "It has caused human pandemics", "It destroys wheat crops", "It contaminates drinking water with toxins"],
  "Spread beyond Africa to Europe, Russia, China and Southeast Asia threatens pork production and food security.", "Pig industry and food security."),
 ("¿Por qué la reciente diseminación de la PPA a Europa y Asia preocupa globalmente?", ["Amenaza a la industria porcina mundial y la seguridad alimentaria", "Causó pandemias humanas", "Destruye cultivos de trigo", "Contamina el agua con toxinas"],
  "Su expansión fuera de África a Europa, Rusia, China y el Sudeste Asiático amenaza la producción porcina y la seguridad alimentaria.", "Porcinos y seguridad alimentaria.")),

# --- Newcastle (37112843)
("37112843", "explorer", 2, "Its pathogen, Newcastle disease virus (NDV), is also a promising antitumor treatment candidate",
 ("Besides being a major poultry pathogen, Newcastle disease virus is studied as…", ["A vaccine against rabies", "A cause of human hepatitis", "A candidate antitumor (oncolytic) therapy", "A plant pathogen"],
  "NDV threatens poultry worldwide and is also explored as an oncolytic antitumor agent.", "Antitumor candidate."),
 ("Además de ser un patógeno avícola importante, el virus de Newcastle se estudia como…", ["Vacuna antirrábica", "Causa de hepatitis humana", "Candidato a terapia antitumoral (oncolítica)", "Patógeno vegetal"],
  "El VEN amenaza a la avicultura mundial y también se explora como agente oncolítico antitumoral.", "Candidato antitumoral.")),

# --- Canine parvovirus (20933134)
("20933134", "curious", 1, "canine parvoviral enteritis has remained a common and important cause of morbidity and mortality in young dogs",
 ("Which dogs are most affected by canine parvovirus enteritis?", ["Elderly dogs", "Young dogs (puppies)", "Only working dogs", "Only vaccinated adults"],
  "Since its emergence in 1978, parvoviral enteritis remains a major cause of illness and death in young dogs.", "Puppies."),
 ("¿Qué perros son los más afectados por la enteritis por parvovirus canino?", ["Perros ancianos", "Perros jóvenes (cachorros)", "Solo perros de trabajo", "Solo adultos vacunados"],
  "Desde su aparición en 1978, la enteritis por parvovirus sigue siendo una causa importante de enfermedad y muerte en cachorros.", "Cachorros.")),

# --- FeLV (32680664)
("32680664", "explorer", 3, "Feline leukemia virus (FeLV) is a retrovirus with global impact on the health of domestic cats that causes tumors (mainly lymphoma), bone marrow disorders, and immunosuppression",
 ("What type of virus is feline leukemia virus and what does it cause?", ["A herpesvirus causing conjunctivitis", "A parvovirus causing enteritis", "A coronavirus causing peritonitis", "A retrovirus causing lymphoma, marrow disorders and immunosuppression"],
  "FeLV is a retrovirus causing tumors (mainly lymphoma), bone marrow disorders and immunosuppression in cats.", "Retrovirus; lymphoma."),
 ("¿Qué tipo de virus es el de la leucemia felina y qué causa?", ["Un herpesvirus que causa conjuntivitis", "Un parvovirus que causa enteritis", "Un coronavirus que causa peritonitis", "Un retrovirus que causa linfoma, trastornos medulares e inmunosupresión"],
  "El FeLV es un retrovirus que causa tumores (sobre todo linfoma), trastornos de médula ósea e inmunosupresión en gatos.", "Retrovirus; linfoma.")),

# --- mcr-1 (33898852)
("33898852", "researcher", 0, "resistance genes (mcr - Mobilized Colistin Resistance - genes) that render last-resort drugs (Colistin) ineffective",
 ("What do mcr genes confer, and why does it matter for livestock?", ["Mobilized colistin resistance, compromising a last-resort drug used in farming and medicine", "Resistance to penicillin only", "Resistance to antifungals", "Virulence in plants"],
  "mcr genes mobilize colistin resistance; colistin use in livestock drives their spread, threatening a last-resort human drug.", "Colistin resistance."),
 ("¿Qué confieren los genes mcr y por qué importan en la ganadería?", ["Resistencia movilizable a colistina, comprometiendo un fármaco de último recurso usado en producción y medicina", "Solo resistencia a penicilina", "Resistencia a antifúngicos", "Virulencia en plantas"],
  "Los genes mcr movilizan la resistencia a colistina; su uso en ganadería favorece la diseminación y amenaza un fármaco humano de último recurso.", "Resistencia a colistina.")),

# --- BVDV (37900320)
("37900320", "researcher", 2, "the virus has evolved multiple strategies to evade the host's innate immunity and adaptive immunity",
 ("What helps bovine viral diarrhea virus persist in cattle herds?", ["It forms spores", "It is resistant to all disinfectants", "It evades innate and adaptive immunity through multiple strategies", "It only infects wild animals"],
  "BVDV evades type I interferon signaling, adaptive immunity and other defenses, promoting survival and spread.", "Immune evasion."),
 ("¿Qué ayuda al virus de la diarrea viral bovina a persistir en los rodeos?", ["Forma esporas", "Resiste todos los desinfectantes", "Evade la inmunidad innata y adaptativa con múltiples estrategias", "Solo infecta animales silvestres"],
  "El VDVB evade la señalización del interferón tipo I, la inmunidad adaptativa y otras defensas, favoreciendo su persistencia.", "Evasión inmune.")),

# --- Rinderpest (23798687)
("23798687", "beginner", 0, "culminated in 2011 with the UN Food and Agriculture Organization and the World Organization for Animal Health declaring global eradication of rinderpest",
 ("Which animal disease was declared globally eradicated in 2011?", ["Rinderpest", "Foot-and-mouth disease", "Rabies", "Anthrax"],
  "Rinderpest was declared eradicated in 2011 — only the second disease ever eradicated, after smallpox.", "Rinderpest."),
 ("¿Qué enfermedad animal se declaró erradicada del mundo en 2011?", ["Peste bovina", "Fiebre aftosa", "Rabia", "Carbunco"],
  "La peste bovina se declaró erradicada en 2011: la segunda enfermedad erradicada de la historia, tras la viruela.", "Peste bovina.")),
("23798687", "explorer", 1, "principally mass vaccination combined with zoosanitary procedures",
 ("Which conventional measures were the basis of rinderpest control?", ["Antibiotic treatment of all cattle", "Mass vaccination combined with zoosanitary procedures", "Insecticide spraying only", "Culling all wildlife"],
  "Mass vaccination plus zoosanitary measures drove the decline; innovations later solved last-mile surveillance challenges.", "Mass vaccination + zoosanitary measures."),
 ("¿Qué medidas convencionales fueron la base del control de la peste bovina?", ["Antibióticos a todo el ganado", "Vacunación masiva combinada con medidas zoosanitarias", "Solo insecticidas", "Eliminar toda la fauna silvestre"],
  "La vacunación masiva y las medidas zoosanitarias impulsaron la caída; luego innovaciones resolvieron la vigilancia de la última milla.", "Vacunación masiva + zoosanitarias.")),

# --- Bluetongue (7728636)
("7728636", "researcher", 3, "Bluetongue (BLU) is a noncontagious viral disease. The virus is a member of the Orbivirus genus",
 ("Which statement about bluetongue is correct?", ["It is a highly contagious bacterial disease", "It spreads by direct contact between sheep", "It is caused by a prion", "It is a noncontagious, vector-borne viral disease (Orbivirus) of ruminants"],
  "Bluetongue is a noncontagious Orbivirus disease of ruminants, transmitted by Culicoides midges, with 24 classic serotypes.", "Noncontagious Orbivirus."),
 ("¿Qué afirmación sobre la lengua azul es correcta?", ["Es una enfermedad bacteriana muy contagiosa", "Se transmite por contacto directo entre ovejas", "La causa un prion", "Es una enfermedad viral no contagiosa (Orbivirus) de rumiantes, transmitida por vectores"],
  "La lengua azul es una enfermedad por Orbivirus no contagiosa de rumiantes, transmitida por jejenes Culicoides, con 24 serotipos clásicos.", "Orbivirus no contagioso.")),

# --- PRRSV (39204065)
("39204065", "explorer", 0, "PRRSV infection in gestating gilts and sows induces important reproductive failure",
 ("What does PRRS virus cause in pregnant sows?", ["Reproductive failure", "Skin vesicles", "Hoof loss", "Blindness"],
  "PRRSV causes reproductive failure in sows and respiratory disease in piglets and growers.", "Reproductive failure."),
 ("¿Qué causa el virus del PRRS en cerdas gestantes?", ["Fallas reproductivas", "Vesículas en piel", "Pérdida de pezuñas", "Ceguera"],
  "El VPRRS causa fallas reproductivas en cerdas y enfermedad respiratoria en lechones y cerdos de engorde.", "Fallas reproductivas.")),
("39204065", "expert", 2, "PRRSV infection interferes with immunity in the respiratory tract, making PRRSV-infected pigs more susceptible to opportunistic secondary pathogens",
 ("Why do PRRSV-infected pigs often develop secondary infections?", ["They stop eating", "PRRSV produces antibiotics", "PRRSV impairs respiratory tract immunity", "Vaccines cause the infections"],
  "PRRSV interferes with respiratory immunity, predisposing to opportunistic secondary pathogens.", "Impaired respiratory immunity."),
 ("¿Por qué los cerdos con PRRSV suelen tener infecciones secundarias?", ["Dejan de comer", "El PRRSV produce antibióticos", "El PRRSV altera la inmunidad del tracto respiratorio", "Las vacunas causan las infecciones"],
  "El PRRSV interfiere con la inmunidad respiratoria y predispone a patógenos oportunistas secundarios.", "Inmunidad respiratoria alterada.")),

# --- Marek (27894330)
("27894330", "explorer", 1, "Marek's disease (MD), caused by Marek's disease virus (MDV), is a commercially important neoplastic disease of poultry",
 ("What kind of disease is Marek's disease in chickens?", ["A bacterial enteritis", "A neoplastic (tumor-causing) viral disease", "A fungal pneumonia", "A nutritional deficiency"],
  "Marek's disease is a herpesvirus-induced neoplastic (T-cell lymphoma) disease of poultry.", "Viral neoplastic disease."),
 ("¿Qué tipo de enfermedad es la enfermedad de Marek en pollos?", ["Una enteritis bacteriana", "Una enfermedad viral neoplásica (causa tumores)", "Una neumonía fúngica", "Una deficiencia nutricional"],
  "La enfermedad de Marek es una enfermedad neoplásica (linfoma T) inducida por un herpesvirus en aves.", "Viral neoplásica.")),
("27894330", "expert", 3, "vaccines are only capable of preventing neuropathy, oncogenic disease and immunosuppression, but are unable to prevent MDV transmission or infection, leading to emergence of increasingly virulent pathotypes",
 ("Why have increasingly virulent Marek's disease virus strains emerged?", ["Chickens stopped being vaccinated", "The virus became a bacterium", "Antibiotics selected them", "Vaccines prevent disease but not infection or transmission ('leaky' vaccines)"],
  "MD vaccines prevent disease but not infection or shedding, allowing more virulent pathotypes to evolve.", "Leaky vaccines."),
 ("¿Por qué surgieron cepas cada vez más virulentas del virus de Marek?", ["Se dejó de vacunar a los pollos", "El virus se convirtió en bacteria", "Los antibióticos las seleccionaron", "Las vacunas previenen la enfermedad pero no la infección ni la transmisión (vacunas 'imperfectas')"],
  "Las vacunas contra Marek previenen la enfermedad pero no la infección ni la excreción, permitiendo la evolución de patotipos más virulentos.", "Vacunas imperfectas.")),

# --- IBD (10935278)
("10935278", "researcher", 0, "the infection, when not fatal, leads to a degree of immunosuppression",
 ("What is a key consequence of non-fatal infectious bursal disease (Gumboro) in chickens?", ["Immunosuppression", "Feather color change", "Egg size increase", "Lifelong immunity to all viruses"],
  "IBDV damages the bursa of Fabricius, causing immunosuppression even when birds survive.", "Immunosuppression."),
 ("¿Cuál es una consecuencia clave de la enfermedad de Gumboro no mortal en pollos?", ["Inmunosupresión", "Cambio de color de plumas", "Huevos más grandes", "Inmunidad de por vida a todos los virus"],
  "El virus daña la bolsa de Fabricio y causa inmunosupresión incluso en aves que sobreviven.", "Inmunosupresión.")),

# --- Canine distemper (18501278)
("18501278", "researcher", 1, "several episodes of CDV disease in vaccinated animals have been reported",
 ("Why is ongoing surveillance of canine distemper virus recommended?", ["The virus infects only cats", "Disease has been reported in vaccinated dogs, possibly from new variants", "There is no vaccine", "It was eradicated in 2011"],
  "Distemper incidence has risen and cases in vaccinated dogs occur, so new variants and vaccine efficacy must be monitored.", "Cases in vaccinated dogs."),
 ("¿Por qué se recomienda vigilar el virus del moquillo canino?", ["Solo infecta gatos", "Se informaron casos en perros vacunados, quizá por nuevas variantes", "No hay vacuna", "Se erradicó en 2011"],
  "La incidencia del moquillo aumentó y hay casos en perros vacunados; hay que vigilar nuevas variantes y la eficacia vacunal.", "Casos en vacunados.")),

# --- FIP (39829669)
("39829669", "explorer", 2, "There are two pathotypes, namely those caused by FCoV, which are often referred to as feline enteric coronavirus and FIP virus",
 ("Which virus causes feline infectious peritonitis?", ["Feline leukemia virus", "Feline parvovirus", "A feline coronavirus pathotype (FIPV)", "Feline herpesvirus"],
  "Feline coronavirus has two pathotypes: the mild feline enteric coronavirus and the FIP virus.", "Feline coronavirus (FIPV)."),
 ("¿Qué virus causa la peritonitis infecciosa felina?", ["Virus de la leucemia felina", "Parvovirus felino", "Un patotipo de coronavirus felino (VPIF)", "Herpesvirus felino"],
  "El coronavirus felino tiene dos patotipos: el coronavirus entérico, leve, y el virus de la PIF.", "Coronavirus felino (VPIF).")),

# --- Johne's (23106497)
("23106497", "researcher", 3, "This statement concludes with an assessment of the evidence in favor of MAP as a potential zoonotic pathogen",
 ("Which organism causes Johne's disease (paratuberculosis), and what is debated about it?", ["Brucella abortus; whether it causes abortion", "Mycobacterium bovis; whether it causes TB", "Leptospira; whether it infects dogs", "M. avium subsp. paratuberculosis; whether it is zoonotic"],
  "Johne's disease is caused by MAP; its potential zoonotic role (e.g., Crohn's disease) remains controversial.", "MAP; zoonotic potential."),
 ("¿Qué organismo causa la paratuberculosis (enfermedad de Johne) y qué se debate?", ["Brucella abortus; si causa aborto", "Mycobacterium bovis; si causa TB", "Leptospira; si infecta perros", "M. avium subsp. paratuberculosis; si es zoonótico"],
  "La enfermedad de Johne la causa MAP; su posible papel zoonótico (p. ej., Crohn) sigue siendo controvertido.", "MAP; potencial zoonótico.")),

# --- S. suis (29122409)
("29122409", "explorer", 3, "Streptococcus suis is a major swine pathogen worldwide",
 ("Streptococcus suis is primarily a pathogen of…", ["Cattle", "Poultry", "Horses", "Pigs (and an emerging zoonosis)"],
  "S. suis is a major swine pathogen and an emerging zoonotic agent, mainly in Asia, causing meningitis and sepsis.", "Pigs."),
 ("Streptococcus suis es principalmente un patógeno de…", ["Bovinos", "Aves", "Caballos", "Cerdos (y una zoonosis emergente)"],
  "S. suis es un patógeno porcino importante y un agente zoonótico emergente, sobre todo en Asia, que causa meningitis y sepsis.", "Cerdos.")),

# --- LSD (37766268)
("37766268", "explorer", 1, "LSD is caused by lumpy skin disease virus (LSDV), a member of the Poxviridae family",
 ("Lumpy skin disease of cattle is caused by a member of which virus family?", ["Paramyxoviridae", "Poxviridae", "Reoviridae", "Herpesviridae"],
  "LSDV is a poxvirus causing multiple skin nodules in cattle and buffalo; it has spread from Africa to Asia and Europe.", "Poxviridae."),
 ("¿A qué familia pertenece el virus de la dermatosis nodular contagiosa bovina?", ["Paramyxoviridae", "Poxviridae", "Reoviridae", "Herpesviridae"],
  "El LSDV es un poxvirus que causa múltiples nódulos cutáneos en bovinos y búfalos; se expandió de África a Asia y Europa.", "Poxviridae.")),

# --- BSE (40092198)
("40092198", "curious", 2, "Bovine spongiform encephalopathy (BSE), also referred to as mad cow disease",
 ("Bovine spongiform encephalopathy is popularly known as…", ["Blue tongue", "Foot rot", "Mad cow disease", "Milk fever"],
  "BSE (mad cow disease) is a prion disease of cattle linked to variant CJD in humans.", "Mad cow disease."),
 ("La encefalopatía espongiforme bovina se conoce popularmente como…", ["Lengua azul", "Pietín", "Enfermedad de la vaca loca", "Fiebre de la leche"],
  "La EEB (vaca loca) es una enfermedad priónica bovina vinculada a la variante de ECJ en humanos.", "Vaca loca.")),
("40092198", "researcher", 0, "Feeding livestock MBM obtained from BSE-infected livestock contaminated with BSE prions is the only known risk factor for BSE development",
 ("What was the cause of the UK BSE epidemic?", ["Feeding cattle meat-and-bone meal contaminated with prions", "Contaminated water", "A mosquito-borne virus", "Genetic inbreeding only"],
  "Feeding prion-contaminated meat-and-bone meal is the only known risk factor; banning ruminant protein in feed prevents BSE.", "Contaminated meat-and-bone meal."),
 ("¿Cuál fue la causa de la epidemia de EEB en el Reino Unido?", ["Alimentar al ganado con harina de carne y hueso contaminada con priones", "Agua contaminada", "Un virus transmitido por mosquitos", "Solo consanguinidad"],
  "Dar harina de carne y hueso contaminada con priones es el único factor de riesgo conocido; prohibir proteína de rumiante en raciones previene la EEB.", "Harina de carne y hueso.")),
("40092198", "expert", 1, "Typically, the central nervous system is examined for prions to diagnose this illness",
 ("How is BSE usually diagnosed?", ["Blood culture from the live cow", "Examining central nervous system tissue for prions, usually post-mortem", "Milk Gram stain", "Fecal PCR for bacteria"],
  "Screening live animals is difficult; diagnosis relies on detecting prions in CNS tissue, typically after slaughter.", "Prions in CNS tissue."),
 ("¿Cómo se diagnostica habitualmente la EEB?", ["Hemocultivo del animal vivo", "Buscando priones en tejido del sistema nervioso central, en general post mortem", "Gram de la leche", "PCR fecal de bacterias"],
  "Es difícil tamizar animales vivos; el diagnóstico se basa en detectar priones en tejido nervioso, en general tras la faena.", "Priones en SNC.")),

# --- Scrapie (1617202)
("1617202", "expert", 2, "the genetic control of the incubation period in sheep",
 ("Which factor is known to control the incubation period of scrapie in sheep?", ["Diet only", "Climate", "Host genetics", "Shearing frequency"],
  "Sheep genetics (prion protein genotype) controls scrapie susceptibility and incubation, used in breeding-based control.", "Host genetics."),
 ("¿Qué factor controla el período de incubación del scrapie en ovinos?", ["Solo la dieta", "El clima", "La genética del huésped", "La frecuencia de esquila"],
  "La genética ovina (genotipo de la proteína priónica) controla la susceptibilidad e incubación, base del control por selección.", "Genética del huésped.")),

# --- Equine influenza (32152243)
("32152243", "researcher", 3, "subtype H7N7, which is believed extinct, and H3N8, which circulates worldwide",
 ("Which influenza A subtype currently circulates worldwide in horses?", ["H5N1", "H1N1", "H7N7", "H3N8"],
  "Equine influenza is caused by H3N8 (worldwide); H7N7 is believed extinct.", "H3N8."),
 ("¿Qué subtipo de influenza A circula actualmente en caballos a nivel mundial?", ["H5N1", "H1N1", "H7N7", "H3N8"],
  "La influenza equina la causa H3N8 (mundial); H7N7 se cree extinto.", "H3N8.")),

# --- Canine leptospirosis (20933138)
("20933138", "explorer", 0, "Testing today is highly based on serology (microscopic agglutination test)",
 ("Which serological test is classically used to diagnose leptospirosis in dogs?", ["Microscopic agglutination test (MAT)", "Coombs test", "Widal test", "Tuberculin test"],
  "The microscopic agglutination test is the reference serology, with PCR as a complement.", "MAT."),
 ("¿Qué prueba serológica se usa clásicamente para diagnosticar leptospirosis en perros?", ["Prueba de aglutinación microscópica (MAT)", "Prueba de Coombs", "Reacción de Widal", "Tuberculina"],
  "La aglutinación microscópica es la serología de referencia, con PCR como complemento.", "MAT.")),

# --- Salmonella poultry (38004824)
("38004824", "curious", 3, "Contaminated poultry eggs and meat products are the major sources of human Salmonella infection",
 ("What are the major sources of human Salmonella infection?", ["Fresh fruit only", "Tap water", "Insect bites", "Contaminated poultry eggs and meat"],
  "Poultry eggs and meat are the main sources of human non-typhoidal salmonellosis.", "Eggs and poultry meat."),
 ("¿Cuáles son las principales fuentes de infección humana por Salmonella?", ["Solo fruta fresca", "Agua de red", "Picaduras de insectos", "Huevos y carne de aves contaminados"],
  "Los huevos y la carne de aves son las principales fuentes de salmonelosis no tifoidea humana.", "Huevos y carne aviar.")),
("38004824", "expert", 1, "The principal virulence genes linked to Salmonella pathogenesis in poultry are located in Salmonella pathogenicity islands 1 and 2 (SPI-1 and SPI-2)",
 ("Where are Salmonella's principal virulence genes located?", ["On the flagellin gene only", "In Salmonella pathogenicity islands SPI-1 and SPI-2", "In the capsule", "In mitochondria"],
  "SPI-1 and SPI-2 encode type III secretion systems for invasion and intracellular survival.", "SPI-1 and SPI-2."),
 ("¿Dónde se ubican los principales genes de virulencia de Salmonella?", ["Solo en el gen de flagelina", "En las islas de patogenicidad SPI-1 y SPI-2", "En la cápsula", "En mitocondrias"],
  "SPI-1 y SPI-2 codifican sistemas de secreción tipo III para la invasión y la supervivencia intracelular.", "SPI-1 y SPI-2.")),

# --- Campylobacter poultry (36363726)
("36363726", "explorer", 2, "C. jejuni is the leading cause of human foodborne illness associated with poultry",
 ("Which bacterium is the leading cause of human foodborne illness linked to poultry?", ["Listeria monocytogenes", "Clostridium botulinum", "Campylobacter jejuni", "Vibrio cholerae"],
  "C. jejuni colonizes broilers almost as a commensal and is the leading poultry-associated foodborne pathogen.", "Campylobacter jejuni."),
 ("¿Qué bacteria es la principal causa de enfermedad alimentaria humana vinculada a las aves?", ["Listeria monocytogenes", "Clostridium botulinum", "Campylobacter jejuni", "Vibrio cholerae"],
  "C. jejuni coloniza a los pollos casi como comensal y es el principal patógeno alimentario asociado a aves.", "Campylobacter jejuni.")),
("36363726", "researcher", 0, "Strict biosecurity measures can decrease C. jejuni prevalence by more than 50% in broilers at market age",
 ("Which on-farm measure can reduce Campylobacter prevalence in broilers by more than half?", ["Strict biosecurity", "Feeding more corn", "Raising birds at higher density", "Removing all vaccines"],
  "Strict biosecurity can cut C. jejuni prevalence by over 50% at market age.", "Biosecurity."),
 ("¿Qué medida en granja puede reducir la prevalencia de Campylobacter en pollos a más de la mitad?", ["Bioseguridad estricta", "Dar más maíz", "Criar a mayor densidad", "Quitar todas las vacunas"],
  "La bioseguridad estricta puede reducir la prevalencia de C. jejuni en más de 50% a la edad de faena.", "Bioseguridad.")),

# --- Swine influenza (31988203)
("31988203", "explorer", 1, "Human and swine IAV are prone to interspecies transmission, leading to regular incursions from human to pig and vice versa",
 ("Which statement about swine influenza is correct?", ["It never reaches humans", "Influenza A viruses pass regularly from humans to pigs and vice versa", "It is caused by a bacterium", "It only infects wild boars"],
  "Bidirectional human–pig transmission shapes influenza evolution in both species, relevant to pandemic planning.", "Bidirectional transmission."),
 ("¿Qué afirmación sobre la influenza porcina es correcta?", ["Nunca llega a humanos", "Los virus influenza A pasan regularmente de humanos a cerdos y viceversa", "La causa una bacteria", "Solo infecta jabalíes"],
  "La transmisión bidireccional humano–cerdo moldea la evolución de la influenza en ambas especies, clave para planificar pandemias.", "Transmisión bidireccional.")),
]
