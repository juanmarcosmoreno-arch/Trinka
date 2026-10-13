# Veterinary VII — original research: H5N1 in dairy cattle, canine rabies elimination, global
# antimicrobial use in livestock, Schmallenberg, FIP antivirals, leptospirosis vaccine titers,
# FMD 2001 genomics, bluetongue in Europe, Toxoplasma shedding, Echinococcus baiting, parvovirus in cats.
# Sources: PubMed original papers (abstracts). Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- H5N1 in dairy cattle (38683888, 39053575)
("38683888", "curious", 2, "an abrupt drop in milk production",
 ("Which sign did dairy cows infected with H5N1 avian influenza show in the US in 2024?", ["Severe lameness and hoof lesions", "Patchy hair loss on the udder", "An abrupt drop in milk yield", "Sudden blindness and head pressing"],
  "Infected cows had nonspecific illness, reduced feed intake and rumination, and an abrupt drop in milk.", "Milk drop."),
 ("¿Qué signo mostraron las vacas lecheras infectadas con influenza aviar H5N1 en EE. UU. en 2024?", ["Cojera grave y lesiones podales", "Caída de pelo en parches en la ubre", "Caída brusca de la producción de leche", "Ceguera súbita y presión de la cabeza"],
  "Las vacas infectadas tuvieron enfermedad inespecífica, menor consumo y rumia, y una caída brusca de la leche.", "Caída de leche.")),
("38683888", "explorer", 0, "fatal systemic influenza infection developed in domestic cats fed raw (unpasteurized) colostrum and milk from affected cows",
 ("What happened to cats on farms with H5N1-infected cows?", ["Cats fed raw milk died of influenza", "They developed only mild colds", "They were resistant to infection", "They spread the virus back to birds only"],
  "Raw (unpasteurized) milk transmitted the virus to cats, a warning about cross-species transmission.", "Fatal in cats via raw milk."),
 ("¿Qué les pasó a los gatos de tambos con vacas infectadas por H5N1?", ["Los que tomaron leche cruda murieron", "Solo tuvieron resfríos leves", "Fueron resistentes a la infección", "Solo devolvieron el virus a las aves silvestres"],
  "La leche cruda (sin pasteurizar) transmitió el virus a los gatos, una alerta sobre la transmisión entre especies.", "Mortal en gatos por leche cruda.")),
("39053575", "researcher", 3, "a distinct tropism of the virus for the epithelial cells lining the alveoli of the mammary gland in cows",
 ("Which tissue did H5N1 show a distinct tropism for in dairy cows?", ["The epithelium of the hoof", "Neurons of the brainstem", "Fibers of skeletal muscle", "Mammary alveolar epithelium"],
  "Virus replicated in mammary alveolar epithelium, explaining abundant virus in milk.", "Mammary epithelium."),
 ("¿Por qué tejido mostró H5N1 un tropismo marcado en vacas lecheras?", ["El epitelio del casco", "Neuronas del tronco encefálico", "Fibras del músculo esquelético", "El epitelio alveolar mamario"],
  "El virus se replicó en el epitelio alveolar mamario, lo que explica la gran cantidad de virus en la leche.", "Epitelio mamario.")),
("39053575", "expert", 1, "Whole viral genome sequences recovered from dairy cows, birds, domestic cats and a raccoon from affected farms indicated multidirectional interspecies transmissions",
 ("What did whole-genome sequencing reveal about H5N1 on affected dairy farms?", ["Only wild birds carried the virus", "Transmission among several species", "The cattle virus came from pigs", "The virus genomes were unrelated"],
  "Sequences showed transmission in several directions between species, and efficient cow-to-cow spread after cattle movement.", "Multidirectional."),
 ("¿Qué reveló la secuenciación genómica de H5N1 en tambos afectados?", ["Solo las aves silvestres portaban el virus", "Transmisión entre varias especies", "El virus bovino provenía de cerdos", "Los genomas virales no estaban relacionados"],
  "Las secuencias mostraron transmisión en varias direcciones entre especies y contagio eficiente entre vacas tras su traslado.", "Multidireccional.")),

# --- Canine rabies (19278295, 30747125)
("19278295", "explorer", 2, "the basic reproductive number for rabies, R0, is very low in our study area in rural Africa (approximately 1.2)",
 ("What was the basic reproductive number (R0) of canine rabies in rural Tanzania?", ["About 15", "About 5", "About 1.2", "About 0.5"],
  "A low R0 (<2 historically) supports the feasibility of controlling rabies by dog vaccination.", "~1.2."),
 ("¿Cuál fue el número reproductivo básico (R0) de la rabia canina en Tanzania rural?", ["Alrededor de 15", "Alrededor de 5", "Alrededor de 1,2", "Alrededor de 0,5"],
  "Un R0 bajo (<2 históricamente) respalda la factibilidad de controlar la rabia vacunando perros.", "~1,2.")),
("19278295", "researcher", 0, "rapid turnover of domestic dog populations has been a major obstacle to successful control in developing countries",
 ("What has been a major obstacle to controlling canine rabies in developing countries?", ["Rapid turnover of the dog population", "There is no effective rabies vaccine", "Rabies circulates only in wildlife", "Dogs cannot be vaccinated before 1 year"],
  "Births and deaths quickly dilute immunity, so regular pulse vaccination is needed between campaigns.", "Dog population turnover."),
 ("¿Cuál ha sido un obstáculo importante para controlar la rabia canina en países en desarrollo?", ["El rápido recambio de la población canina", "No existe una vacuna antirrábica eficaz", "La rabia circula solo en la fauna", "No se vacuna a perros antes del año"],
  "Los nacimientos y muertes diluyen rápido la inmunidad, por eso hacen falta vacunaciones periódicas entre campañas.", "Recambio de perros.")),
("30747125", "beginner", 3, "domestic dogs still remain a major reservoir for rabies",
 ("Which animal remains the major reservoir for human rabies in Africa and Asia?", ["Domestic cats", "Dairy cattle", "Bats, only", "Domestic dogs"],
  "Dogs cause most human rabies deaths there; mass dog vaccination is the proven control strategy.", "Dogs."),
 ("¿Qué animal sigue siendo el principal reservorio de la rabia humana en África y Asia?", ["Los gatos domésticos", "El ganado lechero", "Solo los murciélagos", "Los perros domésticos"],
  "Los perros causan allí la mayoría de las muertes humanas por rabia; vacunarlos masivamente es la estrategia probada.", "Perros.")),

# --- Global AMU in livestock (38217891)
("38217891", "explorer", 1, "we estimated a global annual AMU of 76 060 tonnes of antimicrobial active ingredients",
 ("About how many tonnes of antimicrobials are used each year in cattle, chicken and pig farming worldwide?", ["About 760 tonnes", "About 76,000 tonnes", "About 7.6 million tonnes", "About 76 tonnes"],
  "Estimated 76,060 tonnes per year (2019–2021 average), consistent with WOAH estimates.", "~76,000 t."),
 ("¿Aproximadamente cuántas toneladas de antimicrobianos se usan por año en la cría de bovinos, pollos y cerdos en el mundo?", ["Unas 760 t", "Unas 76.000 t", "Unos 7,6 millones de t", "Unas 76 t"],
  "Se estimaron 76.060 toneladas anuales (promedio 2019–2021), en línea con las estimaciones de la OMSA.", "~76.000 t.")),
("38217891", "researcher", 2, "of which 40 697 tonnes (or 53.5%) for cattle",
 ("Which livestock species accounted for the largest share of global antimicrobial use in this estimate?", ["Chickens", "Pigs", "Cattle", "Sheep"],
  "Cattle 53.5%, pigs 40.9% and chickens 5.6% of the estimated global use.", "Cattle."),
 ("¿Qué especie de producción concentró la mayor parte del uso mundial de antimicrobianos en esta estimación?", ["Gallinas", "Cerdos", "Bovinos", "Ovinos"],
  "Bovinos 53,5%, cerdos 40,9% y pollos 5,6% del uso mundial estimado.", "Bovinos.")),

# --- Schmallenberg (26601441)
("26601441", "explorer", 3, "which is transmitted by Culicoides biting midges",
 ("How is Schmallenberg virus transmitted?", ["By hard ticks", "By contaminated feed", "By direct contact only", "By Culicoides midges"],
  "Schmallenberg virus, first found in 2011 near the German-Dutch border, spreads via Culicoides midges.", "Midges."),
 ("¿Cómo se transmite el virus Schmallenberg?", ["Por garrapatas duras", "Por alimento contaminado", "Solo por contacto directo", "Por jejenes Culicoides"],
  "El virus Schmallenberg, hallado en 2011 cerca de la frontera germano-holandesa, se transmite por jejenes Culicoides.", "Jejenes.")),
("26601441", "researcher", 1, "an infection during a critical period of gestation can lead to abortion, stillbirth or the birth of severely malformed offspring",
 ("Why is Schmallenberg virus economically important despite mild disease in adults?", ["It kills most infected adult cattle", "Fetal infection causes abortion or malformations", "It contaminates milk with heat-stable toxins", "It causes permanent blindness in adult sheep"],
  "Adults show mild or no signs, but fetal infection causes losses, more so in sheep than cattle.", "Fetal damage."),
 ("¿Por qué el virus Schmallenberg es económicamente importante pese a ser leve en adultos?", ["Mata a la mayoría del ganado adulto infectado", "La infección fetal causa abortos o malformaciones", "Contamina la leche con toxinas termoestables", "Causa ceguera permanente en ovinos adultos"],
  "Los adultos tienen signos leves o ninguno, pero la infección fetal causa pérdidas, más en ovinos que en bovinos.", "Daño fetal.")),

# --- FIP (37112799, 34676775)
("37112799", "explorer", 0, "a 4-7-day course of oral GS-441524 antiviral stopped faecal FCoV shedding",
 ("What stopped fecal shedding of feline coronavirus in cats in this study?", ["Oral GS-441524 for a few days", "A long course of oral antibiotics", "An intranasal FCoV vaccine", "Switching to a raw-meat diet"],
  "A 4–7-day course of GS-441524 stopped shedding; none of the treated households' cats later developed FIP.", "GS-441524."),
 ("¿Qué detuvo la eliminación fecal del coronavirus felino en gatos en este estudio?", ["GS-441524 oral por unos días", "Un curso largo de antibióticos orales", "Una vacuna intranasal contra el FCoV", "Cambiar a una dieta de carne cruda"],
  "Un curso de 4 a 7 días de GS-441524 frenó la eliminación; ningún gato de esos hogares desarrolló luego PIF.", "GS-441524.")),
("37112799", "curious", 2, "up to 14% of cats infected with feline coronavirus (FCoV) develop feline infectious peritonitis (FIP)",
 ("What share of cats infected with feline coronavirus go on to develop FIP?", ["Nearly all of them", "Fewer than 1%", "Up to about 14%", "About 60%"],
  "Most FCoV infections are mild, but up to 14% develop potentially lethal FIP after weeks to months.", "Up to 14%."),
 ("¿Qué proporción de gatos infectados con coronavirus felino desarrolla PIF?", ["Casi todos los gatos", "Menos del 1%", "Hasta cerca del 14%", "Alrededor del 60%"],
  "La mayoría de las infecciones son leves, pero hasta 14% desarrolla PIF potencialmente mortal tras semanas o meses.", "Hasta 14%.")),
("34676775", "expert", 3, "monotherapies were ultimately determined to be the most effective in the inhibition of viral transcription",
 ("What did this in vitro screen conclude about combining antivirals against FIP virus?", ["Combinations were clearly superior", "No compound showed any activity", "Antibiotics outperformed antivirals", "Single drugs were the most effective"],
  "26 compounds were active (e.g., GC376, GS-441524); some combinations showed limited synergy, but monotherapies were most effective.", "Monotherapy best."),
 ("¿Qué concluyó este cribado in vitro sobre combinar antivirales contra el virus de la PIF?", ["Las combinaciones fueron claramente superiores", "Ningún compuesto mostró actividad", "Los antibióticos superaron a los antivirales", "Los fármacos solos fueron los más eficaces"],
  "26 compuestos fueron activos (como GC376 y GS-441524); algunas combinaciones mostraron sinergia limitada, pero las monoterapias fueron las más eficaces.", "Monoterapia mejor.")),

# --- Leptospira vaccine titers (24597674)
("24597674", "researcher", 2, "MAT titers ≥1 : 800 can develop after Leptospira spp. vaccination, which can complicate the clinical diagnosis of leptospirosis",
 ("Why can recent Leptospira vaccination complicate diagnosis in dogs?", ["The vaccine itself causes leptospirosis", "Vaccinated dogs cannot be tested at all", "Vaccine titers can mimic infection", "The vaccine destroys existing antibodies"],
  "Vaccine-induced titers vary and can be high, so a single titer may mislead; titers also do not predict protection.", "High vaccine titers."),
 ("¿Por qué una vacunación reciente contra Leptospira puede complicar el diagnóstico en perros?", ["La propia vacuna causa leptospirosis", "A los perros vacunados no se los puede analizar", "Los títulos vacunales simulan infección", "La vacuna destruye los anticuerpos existentes"],
  "Los títulos vacunales varían y pueden ser altos, así que un único título puede confundir; además no predicen protección.", "Títulos vacunales altos.")),

# --- FMD 2001 (16971422)
("16971422", "expert", 0, "the date at which FMDV first infected livestock in the United Kingdom was 7 February 2001",
 ("What did genetic analysis estimate about the start of the 2001 UK foot-and-mouth outbreak?", ["Around 7 February 2001", "Around mid-1995", "Around 30 September 2001", "It could not be estimated"],
  "Viral genomes accumulated ~1.5 substitutions per farm infection, enough to reconstruct transmission pathways.", "~7 Feb 2001."),
 ("¿Qué estimó el análisis genético sobre el comienzo del brote de fiebre aftosa del Reino Unido en 2001?", ["Alrededor del 7 de febrero de 2001", "A mediados de 1995", "Alrededor del 30 de septiembre de 2001", "No se pudo estimar"],
  "Los genomas acumularon ~1,5 sustituciones por granja infectada, suficiente para reconstruir las rutas de transmisión.", "~7 feb 2001.")),
("16971422", "researcher", 3, "nucleotide substitutions to accrue in the consensus sequence at an average rate of 1.5 substitutions per farm infection",
 ("Why could transmission pathways between farms be reconstructed from FMD virus genomes?", ["The virus never mutates during outbreaks", "Each farm had a different virus species", "Farmers recorded every animal contact", "The virus gained ~1.5 mutations per farm"],
  "Rapid mutation of this RNA virus leaves a genetic trail linking farms.", "Mutations as a trail."),
 ("¿Por qué se pudieron reconstruir las rutas de transmisión entre granjas a partir de genomas del virus de la aftosa?", ["El virus nunca muta durante los brotes", "Cada granja tenía una especie viral distinta", "Los productores registraron cada contacto", "El virus sumaba ~1,5 mutaciones por granja"],
  "La rápida mutación de este virus ARN deja un rastro genético que conecta las granjas.", "Mutaciones como rastro.")),

# --- Bluetongue 2006 (23273733)
("23273733", "explorer", 1, "Our model shows that wind is the most important factor affecting the incidence of the disease",
 ("During the 2006 bluetongue serotype 8 outbreak in northern Europe, which factor most affected disease incidence?", ["Breed", "Wind", "Farm size", "Herd age"],
  "Wind carrying infected midges was the most important factor, along with land cover, rain, temperature and animal transport.", "Wind."),
 ("Durante el brote de lengua azul serotipo 8 de 2006 en el norte de Europa, ¿qué factor afectó más la incidencia?", ["La raza", "El viento", "El tamaño", "La edad"],
  "El viento que arrastraba jejenes infectados fue el factor más importante, junto con la cobertura del suelo, la lluvia, la temperatura y el transporte de animales.", "Viento.")),

# --- Toxoplasma (29279081)
("29279081", "researcher", 0, "Protection against oocyst re-excretion occurred in 90%, 25%, and 33.4% of cats after 12, 24, and 36 months",
 ("What did this study find about Toxoplasma oocyst re-shedding in previously infected cats?", ["Protection waned, so cats can shed again", "Cats shed oocysts only once in life", "Adult cats never shed any oocysts", "Cats are not definitive hosts of T. gondii"],
  "Protection fell from 90% at 12 months to ~25–33% at 24–36 months, especially with heterologous strains.", "Protection wanes."),
 ("¿Qué halló este estudio sobre la reeliminación de ooquistes de Toxoplasma en gatos ya infectados?", ["La protección decae y pueden volver a eliminar", "Los gatos eliminan ooquistes una sola vez", "Los gatos adultos nunca eliminan ooquistes", "Los gatos no son huéspedes definitivos"],
  "La protección cayó de 90% a los 12 meses a ~25–33% a los 24–36 meses, sobre todo con cepas heterólogas.", "La protección disminuye.")),

# --- Echinococcus baiting (38576256)
("38576256", "explorer", 2, "most of the baits were consumed by not-owned dogs (82.2%)",
 ("In an Italian field test, who ate most praziquantel baits against Echinococcus granulosus?", ["Wild boars", "Red foxes", "Free-ranging dogs", "Badgers and hedgehogs"],
  "82% were eaten by the target not-owned dogs; double-layer baits even withstood drone drops from 25 m.", "Free-ranging dogs."),
 ("En una prueba de campo en Italia, ¿quién comió la mayoría de los cebos con praziquantel contra Echinococcus granulosus?", ["Jabalíes", "Zorros rojos", "Perros sueltos", "Tejones y erizos"],
  "El 82% lo consumieron los perros sin dueño objetivo; los cebos de doble capa resistieron incluso caídas desde drones a 25 m.", "Perros sin dueño.")),
("38576256", "curious", 0, "Cystic echinococcosis (CE), caused by the larval stage of the cestode Echinococcus granulosus",
 ("What causes cystic echinococcosis (hydatid disease)?", ["Larvae of the tapeworm Echinococcus", "A virus transmitted by dog bites", "A bacterium found in drinking water", "A fungus that lives in soil"],
  "Dogs carry the adult tapeworm; deworming free-ranging dogs with praziquantel limits transmission.", "Echinococcus larva."),
 ("¿Qué causa la equinococosis quística (hidatidosis)?", ["Larvas de la tenia Echinococcus", "Un virus transmitido por mordeduras", "Una bacteria del agua de bebida", "Un hongo que vive en el suelo"],
  "Los perros portan la tenia adulta; desparasitar a los perros sueltos con praziquantel limita la transmisión.", "Larva de Echinococcus.")),

# --- CPV in cats (34399298)
("34399298", "researcher", 3, "Faecal shedding of CPV by cats in multi-cat environments is uncommon suggesting that domestic cats are not significant reservoirs of CPV",
 ("Are healthy domestic cats an important reservoir of canine parvovirus?", ["Yes, most cats shed CPV continuously", "Yes, cats are the main source for dogs", "Cats cannot be infected by parvoviruses", "No; CPV shedding by cats was uncommon"],
  "Most parvovirus detected in cats was feline panleukopenia virus; CPV was rare.", "Not significant reservoirs."),
 ("¿Son los gatos domésticos sanos un reservorio importante del parvovirus canino?", ["Sí, la mayoría lo elimina en forma continua", "Sí, son la principal fuente para los perros", "Los gatos no se infectan con parvovirus", "No; la eliminación por gatos fue poco común"],
  "La mayor parte del parvovirus hallado en gatos era el de la panleucopenia felina; el canino fue raro.", "No son reservorio importante.")),
]
