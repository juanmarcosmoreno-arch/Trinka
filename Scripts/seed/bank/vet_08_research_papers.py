# Veterinary science VIII — research papers and consensus statements: African swine fever, FMD,
# canine parvovirus, calf respiratory disease and diarrhea, FIP antivirals, antimicrobial-use reduction,
# H5N1 in dairy cattle, brucellosis, canine leptospirosis.
# Sources: PubMed original papers and reviews (abstracts). Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- ASFV capsid structure (31624094)
("31624094", "researcher", 2, "which is built from 17,280 proteins, including one major (p72) and four minor",
 ("Which protein is the major capsid protein of African swine fever virus?", ["Hemagglutinin H5", "Glycoprotein gB", "Protein p72", "Protein VP2"],
  "The 4.1 Å structure showed a capsid of 17,280 proteins: major p72 plus four minor proteins.", "p72."),
 ("¿Cuál es la proteína principal de la cápside del virus de la peste porcina africana?", ["La hemaglutinina H5", "La glicoproteína gB", "La proteína p72", "La proteína VP2"],
  "La estructura a 4,1 Å mostró una cápside de 17.280 proteínas: la principal p72 y cuatro menores.", "p72.")),
("31624094", "explorer", 0, "a giant and complex DNA virus that causes a highly contagious and often lethal swine disease for which no vaccine is available",
 ("What kind of virus causes African swine fever?", ["A giant, complex DNA virus", "A small RNA retrovirus", "A prion-like protein", "A plant virus carried by pigs"],
  "ASFV is a giant, complex DNA virus causing a highly contagious and often lethal disease.", "Giant DNA virus."),
 ("¿Qué tipo de virus causa la peste porcina africana?", ["Un virus ADN gigante y complejo", "Un pequeño retrovirus de ARN", "Una proteína tipo prion", "Un virus vegetal portado por cerdos"],
  "El VPPA es un virus ADN gigante y complejo que causa una enfermedad muy contagiosa y a menudo mortal.", "Virus ADN gigante.")),

# --- ASFV and apoptotic bodies (37983498)
("37983498", "researcher", 3, "ASFV utilizes apoptotic bodies (ApoBDs) for infection and cell-cell transmission",
 ("How does African swine fever virus spread between macrophages, per this study?", ["Through the bloodstream only", "Through tunneling bacterial pili", "By fusing whole cells together", "Inside apoptotic bodies"],
  "Infected macrophages die and shed apoptotic bodies loaded with virus, which neighbors engulf.", "Apoptotic bodies."),
 ("Según este estudio, ¿cómo se disemina el virus de la peste porcina africana entre macrófagos?", ["Solo a través de la sangre", "Por pili bacterianos tipo túnel", "Fusionando células enteras", "Dentro de cuerpos apoptóticos"],
  "Los macrófagos infectados mueren y liberan cuerpos apoptóticos cargados de virus que las vecinas fagocitan.", "Cuerpos apoptóticos.")),
("37983498", "expert", 1, "the swine sera to ASFV exert no effect on the ApoBD-mediated transmission",
 ("Why does spread inside apoptotic bodies help ASFV evade the host?", ["It makes the virus stable to heat", "Serum antibodies can't block it", "It turns macrophages into B cells", "It removes the viral genome"],
  "Antibodies in swine sera did not affect transmission via apoptotic bodies, an immune-evasion route.", "Antibodies can't block it."),
 ("¿Por qué viajar dentro de cuerpos apoptóticos ayuda al VPPA a evadir al huésped?", ["Vuelve al virus estable al calor", "Los anticuerpos no la bloquean", "Convierte macrófagos en linfocitos B", "Elimina el genoma viral"],
  "Los anticuerpos de sueros porcinos no afectaron la transmisión por cuerpos apoptóticos, una vía de evasión.", "Los anticuerpos no lo frenan.")),

# --- FMD transmission and vaccines (29245054, 28040311)
("29245054", "researcher", 0, "incursions into FMD-free countries may be seeded by low-probability events such as fomite or wind-borne aerosol routes",
 ("How may foot-and-mouth disease enter a country that is free of it?", ["Via fomites or wind-borne aerosols", "Only through imported vaccines", "Only through infected travelers", "Through mosquitoes and hard ticks"],
  "Endemic spread relies on animal contacts, but incursions can come from rare fomite or airborne events.", "Fomites or wind."),
 ("¿Cómo puede ingresar la fiebre aftosa a un país libre de ella?", ["Por fómites o aerosoles en el viento", "Solo a través de vacunas importadas", "Solo por viajeros infectados", "Por mosquitos y garrapatas duras"],
  "En zonas endémicas se propaga por contactos entre animales, pero puede llegar por fómites o por el aire.", "Fómites o viento.")),
("28040311", "explorer", 2, "Foot-and-mouth disease (FMD) is a highly contagious disease of cloven-hoofed animals",
 ("Which animals does foot-and-mouth disease affect?", ["Horses and donkeys", "Poultry and wild birds", "Cloven-hoofed animals", "Dogs and cats"],
  "FMD affects cloven-hoofed animals: mainly cattle and pigs, plus sheep, goats and many wild species.", "Cloven-hoofed animals."),
 ("¿Qué animales afecta la fiebre aftosa?", ["Caballos y burros", "Aves de corral y silvestres", "Animales de pezuña hendida", "Perros y gatos"],
  "La aftosa afecta animales de pezuña hendida: sobre todo bovinos y cerdos, además de ovinos, caprinos y fauna.", "Pezuña hendida.")),

# --- Canine parvovirus variants (27389721)
("27389721", "explorer", 1, "CPV-2 emerged as a new virus in the late 1970s",
 ("When did canine parvovirus type 2 emerge as a new virus in dogs?", ["In the early 1900s", "In the late 1970s", "In the mid-1950s", "In the year 2010"],
  "CPV-2 appeared in the late 1970s and spread through the global dog population within 2 years.", "Late 1970s."),
 ("¿Cuándo surgió el parvovirus canino tipo 2 como un virus nuevo en perros?", ["A comienzos de 1900", "A fines de los 70", "A mediados de los 50", "En el año 2010"],
  "El CPV-2 apareció a fines de los 70 y en 2 años se extendió a la población canina mundial.", "Fines de los 70.")),
("27389721", "researcher", 3, "virus variants with the single change to Asp or Glu in the VP2 residue 426 were detected",
 ("What distinguishes the CPV-2b and CPV-2c variants?", ["A deletion of the whole VP1 gene", "Gain of an envelope from the host", "Loss of the viral capsid", "A single change at VP2 residue 426"],
  "CPV-2b and -2c differ by Asp or Glu at VP2 residue 426, changes linked to host-range shifts.", "VP2 residue 426."),
 ("¿Qué distingue a las variantes CPV-2b y CPV-2c?", ["La pérdida completa del gen VP1", "Ganar una envoltura del huésped", "La pérdida de la cápside viral", "Un cambio en el residuo 426 de VP2"],
  "CPV-2b y -2c difieren por Asp o Glu en el residuo 426 de VP2, cambios ligados al rango de huéspedes.", "Residuo 426 de VP2.")),

# --- CPV vaccination failures (32768213)
("32768213", "researcher", 0, "the presence of interfering titres of maternally-derived antibodies",
 ("What is the most important cause of canine parvovirus vaccination failure?", ["Interfering maternal antibodies", "Vaccines that contain no virus", "Dogs being immune to all vaccines", "Giving vaccines only in winter"],
  "Maternal antibodies neutralize vaccine virus in pups; non-responders and reversion are other causes.", "Maternal antibodies."),
 ("¿Cuál es la causa más importante de falla de la vacuna contra el parvovirus canino?", ["Anticuerpos maternos que interfieren", "Vacunas que no contienen virus", "Perros inmunes a todas las vacunas", "Vacunar solo en invierno"],
  "Los anticuerpos maternos neutralizan el virus vacunal en cachorros; otras causas son no respondedores y reversión.", "Anticuerpos maternos.")),

# --- Calf housing and BRD (32451032)
("32451032", "explorer", 2, "Housing factors that lead to poor ventilation and stagnant air are often considered the primary reasons for high levels of endemic disease",
 ("Which housing problem is often considered the main reason for endemic respiratory disease in calves?", ["Too much sunlight in the barn", "Feeding calves too much milk", "Poor ventilation and stagnant air", "Pens that are cleaned too often"],
  "Poor ventilation and stagnant air are commonly blamed, though study quality makes conclusions difficult.", "Poor ventilation."),
 ("¿Qué problema de instalaciones se considera a menudo la causa principal de enfermedad respiratoria en terneros?", ["Demasiada luz solar en el galpón", "Darles demasiada leche", "Mala ventilación y aire estancado", "Limpiar los corrales demasiado seguido"],
  "Se culpa a menudo a la mala ventilación y al aire estancado, aunque la calidad de los estudios limita las conclusiones.", "Mala ventilación.")),

# --- BRD treatment duration (26253265)
("26253265", "researcher", 1, "No data are available to define the optimal duration of antimicrobial exposure",
 ("What is known about the optimal duration of antimicrobial therapy for bovine respiratory disease?", ["It must always last 21 days", "No data define the optimal duration", "One single dose is always enough", "It must continue until slaughter"],
  "Data are lacking; human pneumonia studies suggest shorter courses can match longer ones.", "No data define it."),
 ("¿Qué se sabe sobre la duración óptima del antimicrobiano en la enfermedad respiratoria bovina?", ["Siempre debe durar 21 días", "No hay datos que la definan", "Una sola dosis siempre basta", "Debe seguir hasta la faena"],
  "Faltan datos; los estudios de neumonía humana sugieren que cursos más cortos pueden igualar a los largos.", "No hay datos.")),

# --- Calf diarrhea in Uruguay (33575990)
("33575990", "explorer", 3, "Unlike the other pathogens, Cryptosporidium spp. and rotavirus were associated with NCD",
 ("Which pathogens were associated with neonatal diarrhea in Uruguayan dairy calves?", ["Coronavirus and astrovirus", "BVDV and E. coli F5 (K99)", "Salmonella and Clostridium", "Cryptosporidium, rotavirus"],
  "Only Cryptosporidium and rotavirus were linked to diarrhea; Salmonella raised the risk of death.", "Cryptosporidium, rotavirus."),
 ("¿Qué patógenos se asociaron con la diarrea neonatal en terneros lecheros de Uruguay?", ["Coronavirus y astrovirus", "VDVB y E. coli F5 (K99)", "Salmonella y Clostridium", "Cryptosporidium, rotavirus"],
  "Solo Cryptosporidium y rotavirus se asociaron a diarrea; Salmonella aumentaba el riesgo de muerte.", "Cryptosporidium, rotavirus.")),
("33575990", "researcher", 2, "The preweaning dairy calf mortality risk in Uruguay is high (15.2%)",
 ("What is the preweaning mortality risk of dairy calves in Uruguay?", ["About 1.5%", "About 5%", "About 15%", "About 50%"],
  "Mortality before weaning is high, about 15.2%, and its causes were largely unknown.", "~15%."),
 ("¿Cuál es el riesgo de mortalidad predestete de terneros lecheros en Uruguay?", ["Cerca del 1,5%", "Cerca del 5%", "Cerca del 15%", "Cerca del 50%"],
  "La mortalidad antes del destete es alta, cerca del 15,2%, y sus causas eran poco conocidas.", "~15%.")),

# --- IL-6 in calf diarrhea (27209135)
("27209135", "researcher", 0, "the IL-6 concentration was significantly higher in nonrecovering calves",
 ("What did serum IL-6 at the start of diarrhea predict in calves?", ["Higher in non-recovering calves", "Lower in calves that later died", "The same in every calf", "Only the cause of the diarrhea"],
  "High initial IL-6 marked calves that would not recover, supporting closer monitoring.", "High in non-recovering."),
 ("¿Qué predecía la IL-6 sérica al inicio de la diarrea en terneros?", ["Más alta en los que no se recuperaron", "Más baja en los que luego murieron", "Igual en todos los terneros", "Solo la causa de la diarrea"],
  "Una IL-6 inicial alta señalaba a los terneros que no se recuperarían, lo que justifica vigilarlos más.", "Alta en los que no mejoran.")),

# --- FIP antivirals (39091389, 37551843)
("39091389", "explorer", 2, "GS-441524 and molnupiravir show similar effects and safety in cats with FIP",
 ("How did GS-441524 and molnupiravir compare for treating cats with FIP in this Japanese clinic?", ["GS-441524 was far superior", "Molnupiravir failed completely", "Similar effects and safety", "Both caused many deaths"],
  "Remission rates were similar (48/48 vs 51/52 completing), with transient liver changes.", "Similar."),
 ("¿Cómo se compararon GS-441524 y molnupiravir para tratar gatos con PIF en esta clínica japonesa?", ["GS-441524 fue muy superior", "El molnupiravir fracasó por completo", "Efectos y seguridad similares", "Ambos causaron muchas muertes"],
  "Las remisiones fueron similares (48/48 y 51/52 al completar), con cambios hepáticos pasajeros.", "Similares.")),
("39091389", "researcher", 1, "with most deaths within the first 10 days of starting treatment",
 ("When did most deaths occur among cats treated with antivirals for FIP?", ["After finishing the 84 days", "Within the first 10 days", "Around day 50 of therapy", "Only after relapse months later"],
  "Most of the 20 deaths happened in the first 10 days, before the drugs could take full effect.", "First 10 days."),
 ("¿Cuándo ocurrieron la mayoría de las muertes en gatos tratados con antivirales por PIF?", ["Al terminar los 84 días", "En los primeros 10 días", "Hacia el día 50 de terapia", "Solo tras recaídas meses después"],
  "La mayoría de las 20 muertes ocurrió en los primeros 10 días, antes del efecto pleno de los fármacos.", "Primeros 10 días.")),
("37551843", "researcher", 3, "Standard treatment duration was 84 days",
 ("What was the standard duration of molnupiravir treatment for FIP in this case series?", ["7 days", "14 days", "1 year", "84 days"],
  "Owners gave 10–20 mg/kg twice daily for 84 days; 14 of 18 cats completed treatment in remission.", "84 days."),
 ("¿Cuál fue la duración estándar del tratamiento con molnupiravir para PIF en esta serie de casos?", ["7 días", "14 días", "1 año", "84 días"],
  "Los dueños daban 10–20 mg/kg dos veces al día durante 84 días; 14 de 18 gatos terminaron en remisión.", "84 días.")),

# --- Canada broilers AMU reduction (34424161)
("34424161", "researcher", 0, "AMR in broiler chickens declined by 6%-38% after the decrease in prophylactic antimicrobial use",
 ("What happened to resistance in Canadian broilers after prophylactic antimicrobial use fell?", ["It declined by 6–38%", "It doubled in every bacterium", "It disappeared completely", "It did not change at all"],
  "AMR in Salmonella, E. coli and Campylobacter dropped 6–38% after the reduction strategy began in 2014.", "Fell 6–38%."),
 ("¿Qué pasó con la resistencia en pollos parrilleros canadienses al bajar el uso preventivo de antimicrobianos?", ["Bajó entre 6% y 38%", "Se duplicó en todas las bacterias", "Desapareció por completo", "No cambió en absoluto"],
  "La resistencia en Salmonella, E. coli y Campylobacter bajó 6–38% tras la estrategia iniciada en 2014.", "Bajó 6–38%.")),
("34424161", "expert", 2, "the withdrawal of individual compounds, such as cephalosporins and fluoroquinolones, prompted an increase in use of and resistance levels for other drug classes, such as aminoglycosides",
 ("What unintended effect followed the withdrawal of cephalosporins and fluoroquinolones in broilers?", ["No change in any other drug class", "Disease disappeared from the farms", "More aminoglycoside use, resistance", "Total use of antibiotics rose tenfold"],
  "Removing some classes shifted use, and resistance, toward others such as aminoglycosides.", "Aminoglycosides rose."),
 ("¿Qué efecto no deseado siguió al retiro de cefalosporinas y fluoroquinolonas en pollos?", ["Ningún cambio en otras clases", "La enfermedad desapareció de las granjas", "Más uso y resistencia a aminoglucósidos", "El uso total de antibióticos se decuplicó"],
  "Quitar algunas clases desplazó el uso, y la resistencia, hacia otras como los aminoglucósidos.", "Subieron los aminoglucósidos.")),

# --- Dutch success model (25421382)
("25421382", "explorer", 1, "resulted in a 56% reduction in antimicrobial use in farm animals in the Netherlands between 2007 and 2012",
 ("By how much did the Netherlands cut antimicrobial use in farm animals between 2007 and 2012?", ["About 6%", "About 56%", "About 16%", "About 96%"],
  "Compulsory and voluntary actions with clear goals cut use by 56%, aiming for 70% by 2015.", "~56%."),
 ("¿Cuánto redujo Países Bajos el uso de antimicrobianos en animales de granja entre 2007 y 2012?", ["Cerca del 6%", "Cerca del 56%", "Cerca del 16%", "Cerca del 96%"],
  "Acciones obligatorias y voluntarias con metas claras redujeron el uso 56%, con objetivo de 70% en 2015.", "~56%.")),
("25421382", "researcher", 3, "total therapeutic antimicrobial use in farm animals in the Netherlands doubled between 1990 and 2007",
 ("What had happened to Dutch farm-animal antimicrobial use between 1990 and 2007?", ["It had already fallen by half", "It stayed exactly the same", "It was banned completely", "It had doubled over that time"],
  "Use doubled before MRSA and ESBL reservoirs in animals and public pressure opened a window for change.", "It doubled."),
 ("¿Qué había pasado con el uso de antimicrobianos en animales de granja holandeses entre 1990 y 2007?", ["Ya había bajado a la mitad", "Se mantuvo exactamente igual", "Se prohibió por completo", "Se había duplicado"],
  "El uso se duplicó antes de que los reservorios de SARM y BLEE en animales y la presión pública abrieran el cambio.", "Se duplicó.")),

# --- H5N1 in dairy cattle (39535188)
("39535188", "researcher", 0, "replication of the virus in cows appears to be mainly confined to the mammary tissue, with high levels of viral loads detected in milk",
 ("Where does H5N1 mainly replicate in infected dairy cows?", ["In the mammary tissue", "In the brain and spinal cord", "In the rumen wall", "In the hooves and skin"],
  "Replication is mostly in the udder, with high viral loads in milk.", "Mammary tissue."),
 ("¿Dónde se replica principalmente el H5N1 en vacas lecheras infectadas?", ["En el tejido mamario", "En el cerebro y la médula", "En la pared del rumen", "En las pezuñas y la piel"],
  "La replicación ocurre sobre todo en la ubre, con cargas virales altas en la leche.", "Tejido mamario.")),
("39535188", "expert", 2, "This is believed to represent the first mammalian-to-human transmission report of the HPAIV H5N1",
 ("Why were human H5N1 cases in US dairy workers especially significant?", ["They were the first H5N1 cases ever", "They caused a large human pandemic", "First mammal-to-human H5N1 spread", "They proved the virus came from pigs"],
  "Infections attributed to exposure to cattle are believed to be the first mammal-to-human transmission of H5N1.", "Mammal to human."),
 ("¿Por qué fueron tan importantes los casos humanos de H5N1 en trabajadores de tambos de EE. UU.?", ["Fueron los primeros casos de H5N1", "Causaron una gran pandemia humana", "Primer contagio de mamífero a humano", "Probaron que el virus venía de cerdos"],
  "Las infecciones atribuidas al contacto con bovinos serían la primera transmisión de H5N1 de un mamífero a humanos.", "De mamífero a humano.")),

# --- Bovine brucellosis (33353489)
("33353489", "explorer", 1, "The most widely used vaccine strains to protect against Brucella infection and related abortions in cattle are strain 19 and RB51",
 ("Which vaccine strains are most widely used against brucellosis in cattle?", ["BCG and H37Rv", "Strain 19 and RB51", "Sterne 34F2 and Pasteur", "Rev-1 and S2"],
  "S19 and RB51 are the main cattle vaccines, though none is fully protective and safe.", "S19 and RB51."),
 ("¿Qué cepas vacunales se usan más contra la brucelosis bovina?", ["BCG y H37Rv", "Cepa 19 y RB51", "Sterne 34F2 y Pasteur", "Rev-1 y S2"],
  "S19 y RB51 son las principales vacunas bovinas, aunque ninguna es totalmente protectora y segura.", "S19 y RB51.")),
("33353489", "researcher", 3, "Isolation and identification remain the gold standard test",
 ("What remains the gold standard for diagnosing bovine brucellosis?", ["A single serum ELISA", "The rose bengal test alone", "Rectal palpation of the uterus", "Isolating the bacterium"],
  "Culture and identification remain the gold standard, though they require expertise.", "Isolation."),
 ("¿Qué sigue siendo el método de referencia para diagnosticar brucelosis bovina?", ["Un solo ELISA en suero", "Solo la prueba de rosa de bengala", "La palpación rectal del útero", "Aislar e identificar Brucella"],
  "El cultivo y la identificación siguen siendo el estándar de oro, aunque requieren experiencia.", "El aislamiento.")),

# --- Leptospirosis outbreak, Japan (34957279)
("34957279", "researcher", 2, "the odds of leptospirosis infection was 13.3 times higher (p = 0.044) in the dogs taken on walks along the riverbed",
 ("What was the main risk factor in the 2017 canine leptospirosis outbreak in Osaka?", ["Eating raw chicken", "Contact with stray cats", "Walks along a riverbed", "Recent rabies vaccination"],
  "Dogs walked along the same riverbed had 13.3-fold higher odds of infection.", "Riverbed walks."),
 ("¿Cuál fue el principal factor de riesgo del brote de leptospirosis canina de Osaka en 2017?", ["Comer pollo crudo", "El contacto con gatos callejeros", "Paseos por el lecho de un río", "Una vacuna antirrábica reciente"],
  "Los perros paseados por el mismo lecho del río tenían 13,3 veces más chances de infectarse.", "Paseos junto al río.")),
("34957279", "expert", 0, "L. interrogans serovar Australis was suspected to be the causative agent, for which no canine vaccine is available in Japan",
 ("Why was the suspected serovar in the Osaka outbreak a concern?", ["No canine vaccine covered it", "It only infects cats", "It is resistant to all drugs", "It cannot be detected by MAT"],
  "Serovar Australis was suspected, and no canine vaccine against it was available in Japan.", "No vaccine covered it."),
 ("¿Por qué preocupaba el serovar sospechado en el brote de Osaka?", ["Ninguna vacuna canina lo cubría", "Solo infecta a gatos", "Es resistente a todos los fármacos", "No se detecta con la MAT"],
  "Se sospechó del serovar Australis, para el que no había vacuna canina en Japón.", "Sin vacuna que lo cubra.")),

# --- ACVIM leptospirosis consensus (37861061)
("37861061", "researcher", 1, "including in small breed dogs from urban areas, puppies as young as 11 weeks of age",
 ("Which dogs does the updated ACVIM consensus say can get leptospirosis?", ["Only large rural hunting dogs", "Small urban dogs and pups too", "Only dogs that swim in lakes", "Only unvaccinated stray dogs"],
  "Disease occurs in small urban dogs, pups as young as 11 weeks, old dogs and inadequately vaccinated dogs.", "Small urban dogs too."),
 ("Según el consenso actualizado del ACVIM, ¿qué perros pueden tener leptospirosis?", ["Solo perros de caza grandes y rurales", "También chicos urbanos y cachorros", "Solo perros que nadan en lagos", "Solo perros callejeros sin vacunar"],
  "Ocurre en perros chicos urbanos, cachorros de 11 semanas, perros mayores y perros mal vacunados.", "También urbanos chicos.")),
]
