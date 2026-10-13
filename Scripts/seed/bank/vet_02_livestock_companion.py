# Veterinary microbiology II — diseases of cattle, pigs, poultry, horses, dogs and cats; transboundary
# animal diseases and prions. Sources: PubMed reviews (abstracts). Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- Bovine mastitis (33509059, 32051050)
("33509059", "beginner", 1, "Bovine mastitis is the inflammation of the mammary glands/udder of bovines, caused by bacterial pathogens, in most cases",
 ("What is bovine mastitis?", ["Inflammation of the hoof wall", "Inflammation of the udder", "A viral pneumonia of young calves", "A parasitic disease of the liver"],
  "Mastitis is inflammation of the udder, most often caused by bacteria; it causes major losses in dairy farming.", "Udder inflammation."),
 ("¿Qué es la mastitis bovina?", ["Inflamación de la pared del casco", "Inflamación de la glándula mamaria", "Una neumonía viral de terneros jóvenes", "Una enfermedad parasitaria del hígado"],
  "La mastitis es la inflamación de la ubre, casi siempre bacteriana; causa grandes pérdidas en la lechería.", "Inflamación de la ubre.")),
("33509059", "curious", 3, "Routine diagnosis is based on clinical and subclinical forms of the disease",
 ("Which two forms of mastitis must dairy diagnosis consider?", ["Acute and congenital", "Viral and fungal only", "Bilateral and unilateral", "Clinical and subclinical"],
  "Mastitis can be clinical (visible changes) or subclinical (no visible signs, detected by tests such as somatic cell counts).", "Clinical and subclinical."),
 ("¿Qué dos formas de mastitis debe considerar el diagnóstico en tambo?", ["Aguda y congénita", "Solo viral y fúngica", "Bilateral y unilateral", "Clínica y subclínica"],
  "La mastitis puede ser clínica (cambios visibles) o subclínica (sin signos, detectada por pruebas como el recuento de células somáticas).", "Clínica y subclínica.")),
("32051050", "explorer", 0, "Mastitis may have a negative impact on human health by inducing antibiotic-resistant pathogens that may spread",
 ("Why is bovine mastitis also a public health concern?", ["It can select resistant bacteria", "It gives mastitis to people who drink milk", "It is transmitted by mosquitoes", "It contaminates water with prions"],
  "Antibiotic use against mastitis can select resistant pathogens that may reach humans (One Health).", "Antibiotic resistance."),
 ("¿Por qué la mastitis bovina también es un problema de salud pública?", ["Puede seleccionar bacterias resistentes", "Causa mastitis a quienes toman la leche", "La transmiten los mosquitos", "Contamina el agua con priones"],
  "El uso de antibióticos contra la mastitis puede seleccionar patógenos resistentes que lleguen al ser humano (Una Salud).", "Resistencia antibiótica.")),
("33509059", "researcher", 2, "all of them lacked the efficacy to eliminate the associated etiological agent when used as a monotherapy",
 ("What has been a recurring limitation of mastitis treatments evaluated as single therapies?", ["They are far too cheap to sell", "They cannot legally be given to cows", "None reliably clears the pathogen alone", "They all cause prion disease in cattle"],
  "Antibiotics, phages, probiotics and other options each lacked efficacy as monotherapy, driving interest in combined and preventive strategies.", "Monotherapy fails to eliminate."),
 ("¿Qué limitación recurrente mostraron los tratamientos de mastitis evaluados como terapia única?", ["Son demasiado baratos para venderse", "Legalmente no se pueden dar a las vacas", "Ninguno elimina bien al agente solo", "Todos causan enfermedad priónica"],
  "Antibióticos, fagos, probióticos y otras opciones carecieron de eficacia como monoterapia, lo que impulsa estrategias combinadas y preventivas.", "La monoterapia no elimina.")),

# --- Bovine TB (39055751)
("39055751", "curious", 2, "is brought on by the Mycobacterium bovis bacteria, which can infect both people and animals",
 ("Which organism causes bovine tuberculosis?", ["Mycobacterium leprae", "Mycobacterium avium", "Mycobacterium bovis", "Brucella abortus"],
  "Bovine TB is caused by Mycobacterium bovis, a zoonotic pathogen of cattle and humans.", "Mycobacterium bovis."),
 ("¿Qué organismo causa la tuberculosis bovina?", ["Mycobacterium leprae", "Mycobacterium avium", "Mycobacterium bovis", "Brucella abortus"],
  "La TB bovina la causa Mycobacterium bovis, patógeno zoonótico de bovinos y humanos.", "Mycobacterium bovis.")),
("39055751", "explorer", 1, "The tuberculin test is the primary method for detecting bovine tuberculosis in cows",
 ("What is the primary test used to detect bovine tuberculosis in live cattle?", ["Blood culture", "Tuberculin skin test", "Rectal palpation", "Gram stain of the milk"],
  "The tuberculin test is the main screening tool; positives are removed under test-and-cull programs.", "Tuberculin test."),
 ("¿Cuál es la prueba principal para detectar tuberculosis bovina en animales vivos?", ["Hemocultivo", "Prueba de tuberculina", "Palpación rectal", "Tinción de Gram de la leche"],
  "La tuberculina es la principal herramienta de tamizaje; los positivos se eliminan en programas de prueba y sacrificio.", "Tuberculina.")),
("39055751", "researcher", 3, "developed nations have implemented routine testing and culling of infected animals under national mandatory programs",
 ("How have developed countries controlled bovine tuberculosis?", ["Treating all cattle with isoniazid", "Mass vaccination of the human population", "Banning the sale of milk", "Routine testing and culling"],
  "National test-and-cull programs, plus milk pasteurization, have been key to controlling bovine TB.", "Test and cull."),
 ("¿Cómo controlaron los países desarrollados la tuberculosis bovina?", ["Tratando todo el ganado con isoniazida", "Vacunando en masa a la población humana", "Prohibiendo la venta de leche", "Pruebas de rutina y sacrificio"],
  "Los programas nacionales de prueba y sacrificio, junto con la pasteurización, fueron clave para controlar la TB bovina.", "Prueba y sacrificio.")),

# --- FMD (38462419)
("38462419", "curious", 0, "The disease causes a highly contagious vesicular syndrome of cloven-hoofed animals",
 ("Foot-and-mouth disease affects…", ["Cloven-hoofed animals", "Horses and donkeys only", "Only humans", "Only poultry flocks"],
  "FMD is a highly contagious viral vesicular disease of cloven-hoofed animals (cattle, pigs, sheep, goats).", "Cloven-hoofed animals."),
 ("La fiebre aftosa afecta a…", ["Los de pezuña hendida", "Solo caballos y burros", "Solo humanos", "Solo aves de corral"],
  "La aftosa es una enfermedad vesicular viral muy contagiosa de animales de pezuña hendida (bovinos, cerdos, ovinos, caprinos).", "Pezuña hendida.")),
("38462419", "explorer", 2, "is an important determinant of global trade in animal products",
 ("Why does foot-and-mouth disease matter so much economically?", ["It kills most of the humans it infects", "It contaminates crops in the field", "It restricts international trade", "It has no economic effect at all"],
  "FMD status determines access to international markets for meat and animal products.", "Trade restrictions."),
 ("¿Por qué la fiebre aftosa es tan importante económicamente?", ["Mata a la mayoría de los humanos infectados", "Contamina los cultivos en el campo", "Restringe el comercio internacional", "No tiene ningún efecto económico"],
  "El estatus sanitario frente a la aftosa determina el acceso a mercados internacionales de carne y productos animales.", "Restricciones comerciales.")),

# --- ASF (30836106, 31743062)
("31743062", "explorer", 3, "African swine fever is a devastating disease that can result in death in almost all infected pigs",
 ("What is characteristic of African swine fever in domestic pigs?", ["It is mild and self-limiting", "It readily infects humans", "It is caused by a gram-negative bacterium", "It kills nearly all infected pigs"],
  "ASF can cause near-total mortality in domestic pigs; it does not infect humans.", "Very high mortality."),
 ("¿Qué caracteriza a la peste porcina africana en cerdos domésticos?", ["Es leve y autolimitada", "Infecta con facilidad a humanos", "La causa una bacteria", "Mata a casi todos los cerdos"],
  "La PPA puede causar mortalidad casi total en cerdos domésticos; no infecta al ser humano.", "Mortalidad muy alta.")),
("31743062", "researcher", 1, "The African swine fever virus is an unusual complex DNA virus and is not related to other viruses. This has presented challenges for vaccine development",
 ("Why has vaccine development against African swine fever been so difficult?", ["It is an RNA virus that mutates daily", "It is a complex, unusual DNA virus", "Pigs do not produce any antibodies", "The disease is not transmissible at all"],
  "ASFV is a large, complex DNA virus unlike others, complicating vaccine design.", "Complex, unique DNA virus."),
 ("¿Por qué ha sido tan difícil desarrollar una vacuna contra la peste porcina africana?", ["Es un virus ARN que muta a diario", "Es un virus ADN complejo e inusual", "Los cerdos no producen anticuerpos", "La enfermedad no es transmisible"],
  "El VPPA es un virus ADN grande y complejo, distinto de otros, lo que complica el diseño de vacunas.", "Virus ADN complejo y único.")),
("30836106", "expert", 0, "has heightened awareness of the threat posed by this devastating disease to the global pig industry and food security",
 ("Why is the recent spread of African swine fever to Europe and Asia a global concern?", ["It threatens pig farming and food security", "It has caused several human pandemics", "It destroys wheat crops worldwide", "It contaminates drinking water with toxins"],
  "Spread beyond Africa to Europe, Russia, China and Southeast Asia threatens pork production and food security.", "Pig industry and food security."),
 ("¿Por qué la reciente diseminación de la PPA a Europa y Asia preocupa globalmente?", ["Amenaza la porcicultura y el alimento", "Causó varias pandemias humanas", "Destruye cultivos de trigo en el mundo", "Contamina el agua potable con toxinas"],
  "Su expansión fuera de África a Europa, Rusia, China y el Sudeste Asiático amenaza la producción porcina y la seguridad alimentaria.", "Porcinos y seguridad alimentaria.")),

# --- Newcastle (37112843)
("37112843", "explorer", 2, "Its pathogen, Newcastle disease virus (NDV), is also a promising antitumor treatment candidate",
 ("Besides being a major poultry pathogen, Newcastle disease virus is studied as…", ["A vaccine against rabies in dogs", "A cause of human viral hepatitis", "A candidate oncolytic therapy", "A pathogen of cereal crops"],
  "NDV threatens poultry worldwide and is also explored as an oncolytic antitumor agent.", "Antitumor candidate."),
 ("Además de ser un patógeno avícola importante, el virus de Newcastle se estudia como…", ["Una vacuna antirrábica para perros", "Una causa de hepatitis viral humana", "Un candidato a terapia oncolítica", "Un patógeno de cultivos de cereales"],
  "El VEN amenaza a la avicultura mundial y también se explora como agente oncolítico antitumoral.", "Candidato antitumoral.")),

# --- Canine parvovirus (20933134)
("20933134", "curious", 1, "canine parvoviral enteritis has remained a common and important cause of morbidity and mortality in young dogs",
 ("Which dogs are most affected by canine parvovirus enteritis?", ["Old dogs", "Young puppies", "Working dogs only", "Vaccinated adults only"],
  "Since its emergence in 1978, parvoviral enteritis remains a major cause of illness and death in young dogs.", "Puppies."),
 ("¿Qué perros son los más afectados por la enteritis por parvovirus canino?", ["Perros ancianos", "Cachorros jóvenes", "Solo perros de trabajo", "Solo adultos vacunados"],
  "Desde su aparición en 1978, la enteritis por parvovirus sigue siendo una causa importante de enfermedad y muerte en cachorros.", "Cachorros.")),

# --- FeLV (32680664)
("32680664", "explorer", 3, "Feline leukemia virus (FeLV) is a retrovirus with global impact on the health of domestic cats that causes tumors (mainly lymphoma), bone marrow disorders, and immunosuppression",
 ("What type of virus is feline leukemia virus and what does it cause?", ["A herpesvirus causing conjunctivitis", "A parvovirus causing enteritis", "A coronavirus causing peritonitis", "A retrovirus causing lymphoma"],
  "FeLV is a retrovirus causing tumors (mainly lymphoma), bone marrow disorders and immunosuppression in cats.", "Retrovirus; lymphoma."),
 ("¿Qué tipo de virus es el de la leucemia felina y qué causa?", ["Un herpesvirus que causa conjuntivitis", "Un parvovirus que causa enteritis", "Un coronavirus que causa peritonitis", "Un retrovirus que causa linfoma"],
  "El FeLV es un retrovirus que causa tumores (sobre todo linfoma), trastornos de médula ósea e inmunosupresión en gatos.", "Retrovirus; linfoma.")),

# --- mcr-1 (33898852)
("33898852", "researcher", 0, "resistance genes (mcr - Mobilized Colistin Resistance - genes) that render last-resort drugs (Colistin) ineffective",
 ("What do mcr genes confer, and why does it matter for livestock?", ["Resistance to colistin, a last resort", "Resistance to penicillin G and nothing else", "Resistance to antifungal drugs", "Virulence factors for plants"],
  "mcr genes mobilize colistin resistance; colistin use in livestock drives their spread, threatening a last-resort human drug.", "Colistin resistance."),
 ("¿Qué confieren los genes mcr y por qué importan en la ganadería?", ["Resistencia a colistina (último recurso)", "Solo resistencia a la penicilina G y nada más", "Resistencia a fármacos antifúngicos", "Factores de virulencia en plantas"],
  "Los genes mcr movilizan la resistencia a colistina; su uso en ganadería favorece la diseminación y amenaza un fármaco humano de último recurso.", "Resistencia a colistina.")),

# --- BVDV (37900320)
("37900320", "researcher", 2, "the virus has evolved multiple strategies to evade the host's innate immunity and adaptive immunity",
 ("What helps bovine viral diarrhea virus persist in cattle herds?", ["It forms highly resistant spores", "It resists all chemical disinfectants", "It evades innate and adaptive immunity", "It only infects wild animals, not cattle"],
  "BVDV evades type I interferon signaling, adaptive immunity and other defenses, promoting survival and spread.", "Immune evasion."),
 ("¿Qué ayuda al virus de la diarrea viral bovina a persistir en los rodeos?", ["Forma esporas muy resistentes", "Resiste todos los desinfectantes químicos", "Evade la inmunidad innata y adaptativa", "Solo infecta animales silvestres, no bovinos"],
  "El VDVB evade la señalización del interferón tipo I, la inmunidad adaptativa y otras defensas, favoreciendo su persistencia.", "Evasión inmune.")),

# --- Rinderpest (23798687)
("23798687", "beginner", 0, "culminated in 2011 with the UN Food and Agriculture Organization and the World Organization for Animal Health declaring global eradication of rinderpest",
 ("Which animal disease was declared globally eradicated in 2011?", ["Rinderpest", "Foot-and-mouth disease", "Rabies", "Anthrax"],
  "Rinderpest was declared eradicated in 2011 — only the second disease ever eradicated, after smallpox.", "Rinderpest."),
 ("¿Qué enfermedad animal se declaró erradicada del mundo en 2011?", ["Peste bovina", "Fiebre aftosa", "Rabia", "Carbunco"],
  "La peste bovina se declaró erradicada en 2011: la segunda enfermedad erradicada de la historia, tras la viruela.", "Peste bovina.")),
("23798687", "explorer", 1, "principally mass vaccination combined with zoosanitary procedures",
 ("Which conventional measures were the basis of rinderpest control?", ["Antibiotic treatment of all cattle in a region", "Mass vaccination plus zoosanitary steps", "Insecticide spraying alone", "Culling all of the wildlife"],
  "Mass vaccination plus zoosanitary measures drove the decline; innovations later solved last-mile surveillance challenges.", "Mass vaccination + zoosanitary measures."),
 ("¿Qué medidas convencionales fueron la base del control de la peste bovina?", ["Antibióticos a todo el ganado", "Vacunación masiva y zoosanidad", "Solo rociar insecticidas", "Eliminar toda la fauna silvestre"],
  "La vacunación masiva y las medidas zoosanitarias impulsaron la caída; luego innovaciones resolvieron la vigilancia de la última milla.", "Vacunación masiva + zoosanitarias.")),

# --- Bluetongue (7728636)
("7728636", "researcher", 3, "Bluetongue (BLU) is a noncontagious viral disease. The virus is a member of the Orbivirus genus",
 ("Which statement about bluetongue is correct?", ["A highly contagious bacterial disease", "It spreads by direct contact between sheep", "It is caused by a prion protein", "A noncontagious, insect-borne viral disease"],
  "Bluetongue is a noncontagious Orbivirus disease of ruminants, transmitted by Culicoides midges, with 24 classic serotypes.", "Noncontagious Orbivirus."),
 ("¿Qué afirmación sobre la lengua azul es correcta?", ["Una enfermedad bacteriana muy contagiosa", "Se transmite por contacto directo entre ovejas", "La causa una proteína priónica", "Una virosis no contagiosa transmitida por insectos"],
  "La lengua azul es una enfermedad por Orbivirus no contagiosa de rumiantes, transmitida por jejenes Culicoides, con 24 serotipos clásicos.", "Orbivirus no contagioso.")),

# --- PRRSV (39204065)
("39204065", "explorer", 0, "PRRSV infection in gestating gilts and sows induces important reproductive failure",
 ("What does PRRS virus cause in pregnant sows?", ["Reproductive failure", "Vesicles on the skin", "Loss of the hooves", "Sudden blindness"],
  "PRRSV causes reproductive failure in sows and respiratory disease in piglets and growers.", "Reproductive failure."),
 ("¿Qué causa el virus del PRRS en cerdas gestantes?", ["Fallas reproductivas", "Vesículas en la piel", "Pérdida de las pezuñas", "Ceguera súbita"],
  "El VPRRS causa fallas reproductivas en cerdas y enfermedad respiratoria en lechones y cerdos de engorde.", "Fallas reproductivas.")),
("39204065", "expert", 2, "PRRSV infection interferes with immunity in the respiratory tract, making PRRSV-infected pigs more susceptible to opportunistic secondary pathogens",
 ("Why do PRRSV-infected pigs often develop secondary infections?", ["They stop eating for weeks", "PRRSV produces its own antibiotics", "PRRSV impairs respiratory immunity", "The vaccines themselves cause infections"],
  "PRRSV interferes with respiratory immunity, predisposing to opportunistic secondary pathogens.", "Impaired respiratory immunity."),
 ("¿Por qué los cerdos con PRRSV suelen tener infecciones secundarias?", ["Dejan de comer durante semanas", "El PRRSV produce sus propios antibióticos", "El PRRSV altera la inmunidad respiratoria", "Las vacunas mismas causan las infecciones"],
  "El PRRSV interfiere con la inmunidad respiratoria y predispone a patógenos oportunistas secundarios.", "Inmunidad respiratoria alterada.")),

# --- Marek (27894330)
("27894330", "explorer", 1, "Marek's disease (MD), caused by Marek's disease virus (MDV), is a commercially important neoplastic disease of poultry",
 ("What kind of disease is Marek's disease in chickens?", ["A bacterial enteritis", "A tumor-causing viral disease", "A fungal pneumonia of chicks", "A nutritional deficiency disease"],
  "Marek's disease is a herpesvirus-induced neoplastic (T-cell lymphoma) disease of poultry.", "Viral neoplastic disease."),
 ("¿Qué tipo de enfermedad es la enfermedad de Marek en pollos?", ["Una enteritis bacteriana", "Una virosis que causa tumores", "Una neumonía fúngica de pollitos", "Una enfermedad por déficit nutricional"],
  "La enfermedad de Marek es una enfermedad neoplásica (linfoma T) inducida por un herpesvirus en aves.", "Viral neoplásica.")),
("27894330", "expert", 3, "vaccines are only capable of preventing neuropathy, oncogenic disease and immunosuppression, but are unable to prevent MDV transmission or infection, leading to emergence of increasingly virulent pathotypes",
 ("Why have increasingly virulent Marek's disease virus strains emerged?", ["Chickens stopped being vaccinated", "The virus turned into a bacterium", "Antibiotics selected the strains", "'Leaky' vaccines allow transmission"],
  "MD vaccines prevent disease but not infection or shedding, allowing more virulent pathotypes to evolve.", "Leaky vaccines."),
 ("¿Por qué surgieron cepas cada vez más virulentas del virus de Marek?", ["Se dejó de vacunar a los pollos", "El virus se convirtió en una bacteria", "Los antibióticos seleccionaron cepas", "Vacunas 'imperfectas' permiten contagio"],
  "Las vacunas contra Marek previenen la enfermedad pero no la infección ni la excreción, permitiendo la evolución de patotipos más virulentos.", "Vacunas imperfectas.")),

# --- IBD (10935278)
("10935278", "researcher", 0, "the infection, when not fatal, leads to a degree of immunosuppression",
 ("What is a key consequence of non-fatal infectious bursal disease (Gumboro) in chickens?", ["Immunosuppression", "Feather color change", "Egg size increase", "Lifelong immunity to all viruses"],
  "IBDV damages the bursa of Fabricius, causing immunosuppression even when birds survive.", "Immunosuppression."),
 ("¿Cuál es una consecuencia clave de la enfermedad de Gumboro no mortal en pollos?", ["Inmunosupresión", "Cambio de color de plumas", "Huevos más grandes", "Inmunidad de por vida a todos los virus"],
  "El virus daña la bolsa de Fabricio y causa inmunosupresión incluso en aves que sobreviven.", "Inmunosupresión.")),

# --- Canine distemper (18501278)
("18501278", "researcher", 1, "several episodes of CDV disease in vaccinated animals have been reported",
 ("Why is ongoing surveillance of canine distemper virus recommended?", ["The virus now infects only cats", "Cases occur in vaccinated dogs", "There is still no vaccine for dogs", "It was eradicated worldwide in 2011"],
  "Distemper incidence has risen and cases in vaccinated dogs occur, so new variants and vaccine efficacy must be monitored.", "Cases in vaccinated dogs."),
 ("¿Por qué se recomienda vigilar el virus del moquillo canino?", ["El virus ahora solo infecta gatos", "Hay casos en perros vacunados", "Todavía no hay vacuna para perros", "Se erradicó en el mundo en 2011"],
  "La incidencia del moquillo aumentó y hay casos en perros vacunados; hay que vigilar nuevas variantes y la eficacia vacunal.", "Casos en vacunados.")),

# --- FIP (39829669)
("39829669", "explorer", 2, "There are two pathotypes, namely those caused by FCoV, which are often referred to as feline enteric coronavirus and FIP virus",
 ("Which virus causes feline infectious peritonitis?", ["Feline leukemia virus", "Feline panleukopenia parvovirus", "A feline coronavirus (FIPV)", "Feline herpesvirus type 1"],
  "Feline coronavirus has two pathotypes: the mild feline enteric coronavirus and the FIP virus.", "Feline coronavirus (FIPV)."),
 ("¿Qué virus causa la peritonitis infecciosa felina?", ["Virus de la leucemia felina", "Parvovirus de la panleucopenia felina", "Un coronavirus felino (VPIF)", "Herpesvirus felino tipo 1"],
  "El coronavirus felino tiene dos patotipos: el coronavirus entérico, leve, y el virus de la PIF.", "Coronavirus felino (VPIF).")),

# --- Johne's (23106497)
("23106497", "researcher", 3, "This statement concludes with an assessment of the evidence in favor of MAP as a potential zoonotic pathogen",
 ("Which organism causes Johne's disease (paratuberculosis), and what is debated about it?", ["Brucella abortus; whether it causes abortion", "M. bovis; whether it causes tuberculosis", "Leptospira; whether it infects dogs", "M. avium paratuberculosis; zoonotic risk"],
  "Johne's disease is caused by MAP; its potential zoonotic role (e.g., Crohn's disease) remains controversial.", "MAP; zoonotic potential."),
 ("¿Qué organismo causa la paratuberculosis (enfermedad de Johne) y qué se debate?", ["Brucella abortus; si causa abortos en vacas", "M. bovis; si causa tuberculosis", "Leptospira; si infecta perros", "M. avium paratuberculosis; si es zoonosis"],
  "La enfermedad de Johne la causa MAP; su posible papel zoonótico (p. ej., Crohn) sigue siendo controvertido.", "MAP; potencial zoonótico.")),

# --- S. suis (29122409)
("29122409", "explorer", 3, "Streptococcus suis is a major swine pathogen worldwide",
 ("Streptococcus suis is primarily a pathogen of…", ["Dairy cattle", "Backyard poultry", "Riding horses", "Pigs (swine)"],
  "S. suis is a major swine pathogen and an emerging zoonotic agent, mainly in Asia, causing meningitis and sepsis.", "Pigs."),
 ("Streptococcus suis es principalmente un patógeno de…", ["Bovinos lecheros", "Aves de traspatio", "Caballos de silla", "Cerdos (porcinos)"],
  "S. suis es un patógeno porcino importante y un agente zoonótico emergente, sobre todo en Asia, que causa meningitis y sepsis.", "Cerdos.")),

# --- LSD (37766268)
("37766268", "explorer", 1, "LSD is caused by lumpy skin disease virus (LSDV), a member of the Poxviridae family",
 ("Lumpy skin disease of cattle is caused by a member of which virus family?", ["Paramyxoviridae", "Poxviridae", "Reoviridae", "Herpesviridae"],
  "LSDV is a poxvirus causing multiple skin nodules in cattle and buffalo; it has spread from Africa to Asia and Europe.", "Poxviridae."),
 ("¿A qué familia pertenece el virus de la dermatosis nodular contagiosa bovina?", ["Paramyxoviridae", "Poxviridae", "Reoviridae", "Herpesviridae"],
  "El LSDV es un poxvirus que causa múltiples nódulos cutáneos en bovinos y búfalos; se expandió de África a Asia y Europa.", "Poxviridae.")),

# --- BSE (40092198)
("40092198", "curious", 2, "Bovine spongiform encephalopathy (BSE), also referred to as mad cow disease",
 ("Bovine spongiform encephalopathy is popularly known as…", ["Bluetongue disease", "Foot rot", "Mad cow disease", "Milk fever"],
  "BSE (mad cow disease) is a prion disease of cattle linked to variant CJD in humans.", "Mad cow disease."),
 ("La encefalopatía espongiforme bovina se conoce popularmente como…", ["Lengua azul", "Pietín", "Vaca loca", "Fiebre de la leche"],
  "La EEB (vaca loca) es una enfermedad priónica bovina vinculada a la variante de ECJ en humanos.", "Vaca loca.")),
("40092198", "researcher", 0, "Feeding livestock MBM obtained from BSE-infected livestock contaminated with BSE prions is the only known risk factor for BSE development",
 ("What was the cause of the UK BSE epidemic?", ["Prion-tainted meat-and-bone meal", "Contaminated drinking water", "A mosquito-borne virus", "Genetic inbreeding of the cattle herds"],
  "Feeding prion-contaminated meat-and-bone meal is the only known risk factor; banning ruminant protein in feed prevents BSE.", "Contaminated meat-and-bone meal."),
 ("¿Cuál fue la causa de la epidemia de EEB en el Reino Unido?", ["Harinas de carne y hueso con priones", "Agua de bebida contaminada", "Un virus transmitido por mosquitos", "La consanguinidad de los rodeos"],
  "Dar harina de carne y hueso contaminada con priones es el único factor de riesgo conocido; prohibir proteína de rumiante en raciones previene la EEB.", "Harina de carne y hueso.")),
("40092198", "expert", 1, "Typically, the central nervous system is examined for prions to diagnose this illness",
 ("How is BSE usually diagnosed?", ["A blood culture taken from the live cow", "Brain tissue tests, usually post-mortem", "A Gram stain of the milk", "Fecal PCR for bacteria"],
  "Screening live animals is difficult; diagnosis relies on detecting prions in CNS tissue, typically after slaughter.", "Prions in CNS tissue."),
 ("¿Cómo se diagnostica habitualmente la EEB?", ["Hemocultivo del animal vivo", "Análisis cerebral post mortem", "Una tinción de Gram de la leche", "PCR fecal de bacterias"],
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
 ("Which serological test is classically used to diagnose leptospirosis in dogs?", ["Microscopic agglutination test", "Direct Coombs test", "Widal test", "Intradermal tuberculin skin test"],
  "The microscopic agglutination test is the reference serology, with PCR as a complement.", "MAT."),
 ("¿Qué prueba serológica se usa clásicamente para diagnosticar leptospirosis en perros?", ["Aglutinación microscópica (MAT)", "Prueba de Coombs directa", "Reacción de Widal", "Prueba de tuberculina intradérmica"],
  "La aglutinación microscópica es la serología de referencia, con PCR como complemento.", "MAT.")),

# --- Salmonella poultry (38004824)
("38004824", "curious", 3, "Contaminated poultry eggs and meat products are the major sources of human Salmonella infection",
 ("What are the major sources of human Salmonella infection?", ["Fresh fruit only", "Chlorinated tap water", "Biting insects", "Poultry eggs and meat"],
  "Poultry eggs and meat are the main sources of human non-typhoidal salmonellosis.", "Eggs and poultry meat."),
 ("¿Cuáles son las principales fuentes de infección humana por Salmonella?", ["Solo fruta fresca", "Agua de red clorada", "Insectos que pican", "Huevos y carne aviar"],
  "Los huevos y la carne de aves son las principales fuentes de salmonelosis no tifoidea humana.", "Huevos y carne aviar.")),
("38004824", "expert", 1, "The principal virulence genes linked to Salmonella pathogenesis in poultry are located in Salmonella pathogenicity islands 1 and 2 (SPI-1 and SPI-2)",
 ("Where are Salmonella's principal virulence genes located?", ["On the flagellin gene only", "In pathogenicity islands SPI-1/2", "In the polysaccharide capsule", "Inside the host's mitochondria"],
  "SPI-1 and SPI-2 encode type III secretion systems for invasion and intracellular survival.", "SPI-1 and SPI-2."),
 ("¿Dónde se ubican los principales genes de virulencia de Salmonella?", ["Solo en el gen de la flagelina", "En las islas SPI-1 y SPI-2", "En la cápsula de polisacárido", "Dentro de las mitocondrias del huésped"],
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
 ("Which statement about swine influenza is correct?", ["It never reaches humans", "Flu A passes between pigs and people", "It is caused by a gram-negative bacterium", "It only infects wild boars in forests"],
  "Bidirectional human–pig transmission shapes influenza evolution in both species, relevant to pandemic planning.", "Bidirectional transmission."),
 ("¿Qué afirmación sobre la influenza porcina es correcta?", ["Nunca llega a los humanos", "La influenza A pasa de cerdos a personas y al revés", "La causa una bacteria", "Solo infecta a los jabalíes de los bosques europeos"],
  "La transmisión bidireccional humano–cerdo moldea la evolución de la influenza en ambas especies, clave para planificar pandemias.", "Transmisión bidireccional.")),
]
