# Veterinary microbiology III — diseases of horses, cats, pigs, ruminants, poultry and rabbits; parasites
# of livestock and dogs; One Health and antimicrobial use in animals.
# Sources: PubMed reviews (abstracts). Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- Strangles (29424487)
("29424487", "beginner", 2, "Streptococcus equi Infections in Horses",
 ("Strangles is a disease of which animal?", ["Cattle", "Dogs", "Horses", "Chickens"],
  "Strangles is a contagious infection of horses caused by Streptococcus equi subsp. equi.", "Horses."),
 ("¿De qué animal es la enfermedad llamada adenitis equina (papera equina, 'strangles')?", ["Bovinos", "Perros", "Caballos", "Pollos"],
  "La adenitis equina es una infección contagiosa de los caballos causada por Streptococcus equi subsp. equi.", "Caballos.")),
("29424487", "researcher", 0, "carrier states of strangles in the transmission of disease",
 ("Why are carrier horses important in strangles control?", ["Subclinical carriers keep transmitting the infection", "Carriers are immune and protect the herd", "Carriers cannot shed bacteria", "Carriers only exist in vaccinated herds"],
  "Carrier states sustain transmission; detecting carriers (PCR, serology) is key to outbreak control.", "Carriers spread infection."),
 ("¿Por qué los caballos portadores son importantes en el control de la adenitis equina?", ["Los portadores subclínicos siguen transmitiendo la infección", "Los portadores son inmunes y protegen al grupo", "Los portadores no eliminan bacterias", "Solo hay portadores en rebaños vacunados"],
  "Los portadores mantienen la transmisión; detectarlos (PCR, serología) es clave para controlar brotes.", "Los portadores transmiten.")),

# --- Feline panleukopenia (30967253)
("30967253", "curious", 1, "Feline panleukopenia (FPL) is caused by a Carnivore protoparvovirus infection",
 ("What type of virus causes feline panleukopenia?", ["A coronavirus", "A parvovirus", "A retrovirus", "A herpesvirus"],
  "Feline panleukopenia is caused by feline parvovirus (Carnivore protoparvovirus), closely related to canine parvovirus.", "Parvovirus."),
 ("¿Qué tipo de virus causa la panleucopenia felina?", ["Un coronavirus", "Un parvovirus", "Un retrovirus", "Un herpesvirus"],
  "La panleucopenia felina la causa el parvovirus felino (Carnivore protoparvovirus), muy emparentado con el parvovirus canino.", "Parvovirus.")),
("30967253", "researcher", 3, "Feline panleukopenia has re-emerged in Australia in shelter cats associated with failure to vaccinate",
 ("What was associated with the re-emergence of feline panleukopenia in shelter cats?", ["A new antibiotic", "Climate change only", "Contaminated cat food", "Failure to vaccinate"],
  "Panleukopenia re-emerged in shelters where cats were not vaccinated.", "Lack of vaccination."),
 ("¿Qué se asoció al resurgimiento de la panleucopenia felina en refugios?", ["Un antibiótico nuevo", "Solo el cambio climático", "Alimento contaminado", "La falta de vacunación"],
  "La panleucopenia resurgió en refugios donde los gatos no estaban vacunados.", "Falta de vacunación.")),

# --- FCV (17296159)
("17296159", "explorer", 2, "the vaccines do not prevent infection and vaccinated cats can still become persistently infected",
 ("Which statement about feline calicivirus vaccination is correct?", ["It prevents all infection", "It is not available", "It reduces disease but does not prevent infection or persistent carriage", "It only works in dogs"],
  "FCV vaccines reduce clinical disease, but vaccinated cats can still be infected and become carriers; strain variability limits protection.", "Reduces disease, not infection."),
 ("¿Qué afirmación sobre la vacunación contra calicivirus felino es correcta?", ["Previene toda infección", "No existe vacuna", "Reduce la enfermedad pero no previene la infección ni la portación persistente", "Solo funciona en perros"],
  "Las vacunas contra FCV reducen la enfermedad, pero los gatos vacunados pueden infectarse y quedar portadores; la variabilidad de cepas limita la protección.", "Reduce enfermedad, no infección.")),

# --- PCV2 (37431709)
("37431709", "expert", 0, "The cytokine imbalance and lymphocyte depletion, thus the impaired immunity, favors invasion of super- or co-infecting agents",
 ("How does porcine circovirus 2 increase the severity of disease in pigs?", ["It causes lymphocyte depletion and immunosuppression, favoring co-infections", "It produces a potent exotoxin", "It forms spores in the gut", "It blocks blood clotting"],
  "PCV2 disrupts interferon and cytokine pathways and depletes lymphocytes, so co-infections become more severe.", "Immunosuppression."),
 ("¿Cómo aumenta el circovirus porcino 2 la gravedad de la enfermedad en cerdos?", ["Causa depleción linfocitaria e inmunosupresión, favoreciendo coinfecciones", "Produce una exotoxina potente", "Forma esporas en el intestino", "Bloquea la coagulación"],
  "El PCV2 altera las vías del interferón y las citocinas y depleta linfocitos, agravando las coinfecciones.", "Inmunosupresión.")),

# --- PEDV (32502552)
("32502552", "explorer", 3, "a member of the genus Alphacoronavirus in the family Coronaviridae, causes acute diarrhea and/or vomiting, dehydration and high mortality in neonatal piglets",
 ("Porcine epidemic diarrhea virus is a…", ["Parvovirus of adult sows", "Bacterium of the large intestine", "Flavivirus transmitted by mosquitoes", "Coronavirus causing severe diarrhea and high mortality in newborn piglets"],
  "PEDV is an alphacoronavirus causing acute diarrhea, dehydration and high mortality in neonatal piglets.", "Coronavirus of piglets."),
 ("El virus de la diarrea epidémica porcina es un…", ["Parvovirus de cerdas adultas", "Bacteria del intestino grueso", "Flavivirus transmitido por mosquitos", "Coronavirus que causa diarrea grave y alta mortalidad en lechones recién nacidos"],
  "El PEDV es un alfacoronavirus que causa diarrea aguda, deshidratación y alta mortalidad en lechones neonatos.", "Coronavirus de lechones.")),
("32502552", "researcher", 1, "PEDV-specific IgA effector and memory B cells in orally primed sows play a critical role in sow lactogenic immunity and passive protection of piglets",
 ("How are newborn piglets protected against PEDV?", ["By antibiotics in feed", "By lactogenic immunity: IgA in milk from orally primed sows", "By their own adaptive immunity at birth", "By heat lamps"],
  "Sows primed orally produce IgA-secreting cells that pass protective antibodies to piglets in milk (lactogenic immunity).", "Maternal IgA in milk."),
 ("¿Cómo se protege a los lechones recién nacidos contra el PEDV?", ["Con antibióticos en el alimento", "Con inmunidad lactogénica: IgA en la leche de cerdas inmunizadas por vía oral", "Con su propia inmunidad adaptativa al nacer", "Con lámparas de calor"],
  "Las cerdas inmunizadas por vía oral generan células secretoras de IgA que pasan anticuerpos protectores en la leche.", "IgA materna en la leche.")),

# --- CSF (28430168)
("28430168", "researcher", 2, "wild boars are a reservoir host transmitting the virus sporadically also to pig farms",
 ("What role do wild boars play in classical swine fever?", ["They are immune and protect farms", "They are dead-end hosts", "They are a reservoir that sporadically transmits the virus to pig farms", "They transmit it only to humans"],
  "Wild boar act as reservoir hosts of CSF virus (a Pestivirus) and can reintroduce it into domestic herds.", "Reservoir host."),
 ("¿Qué papel cumplen los jabalíes en la peste porcina clásica?", ["Son inmunes y protegen granjas", "Son huéspedes terminales", "Son reservorio y transmiten esporádicamente el virus a granjas", "Solo lo transmiten a humanos"],
  "Los jabalíes son reservorio del virus de la PPC (un Pestivirus) y pueden reintroducirlo en granjas.", "Reservorio.")),
("28430168", "expert", 3, "Control strategies for epidemic outbreaks in free countries are mainly based on classical intervention measures; i.e., quarantine and strict culling of affected herds",
 ("How do CSF-free countries control an outbreak of classical swine fever?", ["Mass antibiotic treatment", "Routine vaccination of all pigs", "Ignoring it until it burns out", "Quarantine and strict culling of affected herds"],
  "Free countries rely on quarantine and culling; vaccination is only an emergency option there, while endemic regions use live vaccines.", "Quarantine and culling."),
 ("¿Cómo controlan un brote de peste porcina clásica los países libres?", ["Tratamiento antibiótico masivo", "Vacunación rutinaria de todos los cerdos", "Ignorándolo", "Cuarentena y sacrificio estricto de los rebaños afectados"],
  "Los países libres usan cuarentena y sacrificio; la vacunación es solo de emergencia, mientras que las zonas endémicas usan vacunas vivas.", "Cuarentena y sacrificio.")),

# --- Heartworm (21922235)
("21922235", "beginner", 1, "Any region where mosquitoes thrive will provide efficient dog-to-dog transportation for the microfilaria",
 ("How is canine heartworm transmitted between dogs?", ["Through food", "By mosquitoes", "By direct contact", "Through water bowls"],
  "Dirofilaria immitis microfilariae are carried from dog to dog by mosquitoes.", "Mosquitoes."),
 ("¿Cómo se transmite el gusano del corazón (dirofilariasis) entre perros?", ["Por la comida", "Por mosquitos", "Por contacto directo", "Por los bebederos"],
  "Las microfilarias de Dirofilaria immitis pasan de perro a perro a través de mosquitos.", "Mosquitos.")),
("21922235", "expert", 2, "the obligate symbiosis of D. immitis and the bacteria Wolbachia pipientis",
 ("Why is doxycycline used in canine heartworm treatment?", ["It kills mosquitoes", "It dissolves blood clots", "It targets Wolbachia, an obligate bacterial symbiont of the worm", "It replaces melarsomine entirely"],
  "D. immitis depends on Wolbachia; antibiotics like doxycycline target the symbiont, complementing adulticide therapy.", "Targets Wolbachia."),
 ("¿Por qué se usa doxiciclina en el tratamiento de la dirofilariasis canina?", ["Mata mosquitos", "Disuelve coágulos", "Ataca a Wolbachia, una bacteria simbionte obligada del parásito", "Reemplaza por completo a la melarsomina"],
  "D. immitis depende de Wolbachia; antibióticos como la doxiciclina atacan al simbionte y complementan el tratamiento adulticida.", "Ataca a Wolbachia.")),

# --- Babesiosis (19967929)
("19967929", "curious", 3, "Babesiosis is a tick-borne disease affecting humans and many domestic and wild animals",
 ("How is babesiosis transmitted?", ["By mosquitoes", "By contaminated food", "By sexual contact", "By ticks"],
  "Babesiosis is a tick-borne protozoan disease of humans and animals.", "Ticks."),
 ("¿Cómo se transmite la babesiosis?", ["Por mosquitos", "Por alimentos contaminados", "Por contacto sexual", "Por garrapatas"],
  "La babesiosis es una enfermedad protozoaria transmitida por garrapatas que afecta a humanos y animales.", "Garrapatas.")),
("19967929", "explorer", 0, "characterised by haemolytic anaemia, icterus and haemoglobinuria",
 ("Which findings characterize canine babesiosis?", ["Hemolytic anemia, jaundice and hemoglobinuria", "Coughing and nasal discharge", "Hair loss and itching", "Lameness only"],
  "Babesia destroys red cells, causing hemolytic anemia, icterus and red-brown urine (hemoglobinuria).", "Hemolytic anemia."),
 ("¿Qué hallazgos caracterizan la babesiosis canina?", ["Anemia hemolítica, ictericia y hemoglobinuria", "Tos y secreción nasal", "Pérdida de pelo y prurito", "Solo cojera"],
  "Babesia destruye glóbulos rojos y causa anemia hemolítica, ictericia y orina rojiza (hemoglobinuria).", "Anemia hemolítica.")),

# --- Haemonchus (27238006)
("27238006", "explorer", 1, "Haemonchus contortus is a highly pathogenic, blood-feeding nematode of small ruminants",
 ("What is Haemonchus contortus?", ["A tick of cattle", "A blood-feeding nematode of sheep and goats", "A virus of pigs", "A fungus of horses' hooves"],
  "H. contortus is a blood-feeding stomach worm of small ruminants, a major cause of anemia and death.", "Blood-feeding nematode."),
 ("¿Qué es Haemonchus contortus?", ["Una garrapata bovina", "Un nematodo hematófago de ovinos y caprinos", "Un virus porcino", "Un hongo de los cascos"],
  "H. contortus es un nematodo hematófago del abomaso de pequeños rumiantes, causa importante de anemia y muerte.", "Nematodo hematófago.")),
("27238006", "researcher", 2, "the 'FAMACHA' conjunctival-colour index",
 ("What does the FAMACHA system assess in sheep and goats?", ["Body weight", "Wool quality", "Conjunctival color as an indicator of anemia from Haemonchus", "Hoof health"],
  "FAMACHA scores eyelid conjunctival color to detect anemia and treat only the animals that need it, slowing resistance.", "Anemia via conjunctival color."),
 ("¿Qué evalúa el sistema FAMACHA en ovinos y caprinos?", ["El peso corporal", "La calidad de la lana", "El color de la conjuntiva como indicador de anemia por Haemonchus", "La salud de las pezuñas"],
  "FAMACHA puntúa el color de la conjuntiva para detectar anemia y tratar solo a los animales que lo necesitan, frenando la resistencia.", "Anemia por color conjuntival.")),

# --- Anthelmintic resistance (32029182)
("32029182", "researcher", 3, "Parasitic nematodes have biologic and genetic features that favor the development of drug resistance, making the emergence of resistant nematodes inevitable",
 ("Why is relying only on anthelmintics to control livestock nematodes unsustainable?", ["Anthelmintics are too expensive", "They are banned worldwide", "Nematodes never become resistant", "Nematode biology makes resistance inevitable"],
  "Nematode biology and genetics make resistance inevitable; control must change to slow it (e.g., refugia, targeted treatment).", "Resistance is inevitable."),
 ("¿Por qué depender solo de antihelmínticos para controlar nematodos del ganado no es sostenible?", ["Son demasiado caros", "Están prohibidos en todo el mundo", "Los nematodos nunca se vuelven resistentes", "La biología de los nematodos hace inevitable la resistencia"],
  "La biología y genética de los nematodos hacen inevitable la resistencia; hay que cambiar el control para frenarla (refugio, tratamientos dirigidos).", "Resistencia inevitable.")),

# --- Neospora (28942304)
("28942304", "explorer", 0, "It is considered to be one of the most important transmissible causes of reproductive failure in cattle",
 ("Neospora caninum is an important cause of what in cattle?", ["Abortion and reproductive failure", "Mastitis", "Foot rot", "Pneumonia in calves only"],
  "Neosporosis is a leading transmissible cause of abortion and reproductive failure in cattle.", "Abortion."),
 ("¿De qué es causa importante Neospora caninum en bovinos?", ["Abortos y fallas reproductivas", "Mastitis", "Pietín", "Solo neumonía en terneros"],
  "La neosporosis es una de las principales causas transmisibles de aborto y fallas reproductivas en bovinos.", "Abortos.")),
("28942304", "researcher", 1, "The horizontal route of transmission from the definitive host, the dog, occurs via ingestion of oocysts",
 ("Which animal is a definitive host of Neospora caninum?", ["The cat", "The dog", "The pig", "The horse"],
  "Dogs are definitive hosts and shed oocysts; cattle are infected horizontally from them or vertically (transplacental).", "The dog."),
 ("¿Qué animal es huésped definitivo de Neospora caninum?", ["El gato", "El perro", "El cerdo", "El caballo"],
  "Los perros son huéspedes definitivos y eliminan ooquistes; el ganado se infecta a partir de ellos (transmisión horizontal) o por vía transplacentaria (vertical).", "El perro.")),

# --- Trichomoniasis (23082032)
("23082032", "researcher", 2, "Bovine trichomoniasis is a sexually transmitted protozoan disease with a worldwide distribution",
 ("How is bovine trichomoniasis (Tritrichomonas foetus) transmitted?", ["By ticks", "By flies", "Sexually, during breeding", "Through drinking water"],
  "Bovine trichomoniasis is a sexually transmitted protozoan disease; testing bulls is the core of control.", "Sexually."),
 ("¿Cómo se transmite la tricomoniasis bovina (Tritrichomonas foetus)?", ["Por garrapatas", "Por moscas", "Por vía sexual, en el servicio", "Por el agua de bebida"],
  "La tricomoniasis bovina es una protozoosis de transmisión sexual; controlar a los toros es la base del control.", "Sexual.")),

# --- IBV (33809420)
("33809420", "curious", 3, "Infectious bronchitis virus (IBV) is a major economic problem in commercial chicken farms",
 ("Infectious bronchitis is an important disease of…", ["Dairy cows", "Pigs", "Horses", "Chickens"],
  "Infectious bronchitis virus, a gammacoronavirus, causes respiratory and urogenital disease in chickens.", "Chickens."),
 ("La bronquitis infecciosa es una enfermedad importante de…", ["Vacas lecheras", "Cerdos", "Caballos", "Pollos y gallinas"],
  "El virus de la bronquitis infecciosa, un gammacoronavirus, causa enfermedad respiratoria y urogenital en aves.", "Aves.")),

# --- Clostridial (9689739)
("9689739", "researcher", 0, "Prevention and control strategies are frequently based upon amelioration, by immunoprophylaxis, of the effects of these molecules",
 ("How are clostridial diseases of sheep and goats mainly prevented?", ["Vaccination against their toxins", "Antibiotics in drinking water", "Keeping animals indoors", "Removing all soil"],
  "Clostridial disease is toxin-mediated, so immunoprophylaxis (toxoid vaccines) is the main control strategy.", "Toxoid vaccination."),
 ("¿Cómo se previenen principalmente las clostridiosis de ovinos y caprinos?", ["Vacunando contra sus toxinas", "Antibióticos en el agua", "Manteniendo los animales encerrados", "Eliminando el suelo"],
  "Las clostridiosis están mediadas por toxinas, por eso la inmunoprofilaxis (vacunas con toxoides) es la principal medida.", "Vacunas con toxoides.")),

# --- RHDV2 (39344909)
("39344909", "explorer", 2, "causes a highly contagious disease with hepatic necrosis and disseminated intravascular coagulation",
 ("What does rabbit hemorrhagic disease virus 2 cause?", ["Mild skin lesions", "Chronic diarrhea", "Highly contagious disease with liver necrosis and disseminated coagulation", "Blindness"],
  "RHDV2 (a lagovirus) causes hepatic necrosis and DIC in rabbits and hares; it has spread almost globally since 2010.", "Liver necrosis and DIC."),
 ("¿Qué causa el virus de la enfermedad hemorrágica del conejo 2?", ["Lesiones leves de piel", "Diarrea crónica", "Una enfermedad muy contagiosa con necrosis hepática y coagulación intravascular diseminada", "Ceguera"],
  "El RHDV2 (lagovirus) causa necrosis hepática y CID en conejos y liebres; se diseminó casi a todo el mundo desde 2010.", "Necrosis hepática y CID.")),

# --- Coccidiosis/NE (16191699)
("16191699", "expert", 3, "The risk of NE, due to the Gram-positive bacterium Clostridium perfringens, has increased in recent years because of the voluntary or legally required withdrawal of the use of certain in-feed antibiotic growth promoters",
 ("Why has necrotic enteritis (Clostridium perfringens) in chickens increased in recent years?", ["New virulent viruses", "Higher temperatures only", "Use of more antibiotics", "Withdrawal of in-feed antibiotic growth promoters with anticlostridial activity"],
  "Removing antibiotic growth promoters, which had anticlostridial activity, increased necrotic enteritis risk; coccidiosis predisposes to it.", "Growth promoter withdrawal."),
 ("¿Por qué aumentó en los últimos años la enteritis necrótica (Clostridium perfringens) en pollos?", ["Nuevos virus virulentos", "Solo temperaturas más altas", "Uso de más antibióticos", "El retiro de antibióticos promotores de crecimiento con actividad anticlostridial"],
  "Retirar los promotores de crecimiento antibióticos, que tenían actividad anticlostridial, aumentó el riesgo de enteritis necrótica; la coccidiosis predispone.", "Retiro de promotores.")),

# --- Orf (28480985)
("28480985", "curious", 1, "a highly contagious zoonotic viral infection that threatens those who handle sheep and goats",
 ("Who is at risk of orf (contagious ecthyma) infection?", ["People who handle sheep and goats", "Only veterinarians working with dogs", "Fish farmers", "Beekeepers"],
  "Orf is a parapoxvirus zoonosis acquired by people handling sheep and goats; it usually resolves in 3–6 weeks.", "Sheep and goat handlers."),
 ("¿Quiénes corren riesgo de infectarse con orf (ectima contagioso)?", ["Quienes manipulan ovejas y cabras", "Solo veterinarios de perros", "Piscicultores", "Apicultores"],
  "El orf es una zoonosis por parapoxvirus que adquieren quienes manipulan ovinos y caprinos; suele resolverse en 3–6 semanas.", "Quienes manejan ovejas y cabras.")),

# --- Erysipelothrix (19733019)
("19733019", "explorer", 0, "Swine erysipelas caused by E. rhusiopathiae is the disease of greatest prevalence and economic importance",
 ("Which is the most important animal disease caused by Erysipelothrix rhusiopathiae?", ["Swine erysipelas", "Bovine mastitis", "Canine distemper", "Equine strangles"],
  "Swine erysipelas is the most prevalent and costly E. rhusiopathiae disease; in humans it causes erysipeloid.", "Swine erysipelas."),
 ("¿Cuál es la enfermedad animal más importante causada por Erysipelothrix rhusiopathiae?", ["Erisipela porcina", "Mastitis bovina", "Moquillo canino", "Adenitis equina"],
  "La erisipela porcina es la enfermedad por E. rhusiopathiae más prevalente y costosa; en humanos causa erisipeloide.", "Erisipela porcina.")),
("19733019", "researcher", 3, "Infection due to E. rhusiopathiae in humans is occupationally related",
 ("How do humans usually acquire Erysipelothrix rhusiopathiae?", ["Through mosquito bites", "From contaminated drinking water", "From other people by droplets", "Occupationally, by contact with infected animals, their products or soil"],
  "Human infection (erysipeloid) is occupational — butchers, fish handlers, farmers — after contact with animals or their products.", "Occupational contact."),
 ("¿Cómo adquieren habitualmente los humanos Erysipelothrix rhusiopathiae?", ["Por picaduras de mosquito", "Por agua contaminada", "Por gotitas de otras personas", "Laboralmente, por contacto con animales infectados, sus productos o el suelo"],
  "La infección humana (erisipeloide) es ocupacional: carniceros, pescadores, productores, tras contacto con animales o sus productos.", "Contacto laboral.")),

# --- One Health (24634782)
("24634782", "beginner", 0, "It is the notion of combining human, animal, and environmental components to address global health challenges",
 ("What does the 'One Health' approach combine?", ["Human, animal and environmental health", "Only human hospitals", "Only veterinary clinics", "Only food production"],
  "One Health links human, animal and environmental health to tackle problems such as zoonoses.", "Human, animal, environment."),
 ("¿Qué combina el enfoque 'Una Salud' (One Health)?", ["La salud humana, animal y ambiental", "Solo hospitales humanos", "Solo clínicas veterinarias", "Solo la producción de alimentos"],
  "Una Salud vincula la salud humana, animal y ambiental para abordar problemas como las zoonosis.", "Humana, animal, ambiental.")),

# --- Antimicrobials in food animals (29802609)
("29802609", "curious", 2, "Antimicrobials have been widely used in food animals for growth promotion since the 1950s",
 ("Since the 1950s, antimicrobials have been widely used in food animals for…", ["Coloring meat", "Preserving eggs", "Growth promotion", "Making milk sweeter"],
  "Antimicrobials were used as growth promoters; resistance that emerges can reach humans via food and contact.", "Growth promotion."),
 ("Desde los años 50, los antimicrobianos se usaron mucho en animales de producción para…", ["Colorear la carne", "Conservar huevos", "Promover el crecimiento", "Endulzar la leche"],
  "Los antimicrobianos se usaron como promotores de crecimiento; la resistencia que surge puede llegar al ser humano por alimentos y contacto.", "Promover el crecimiento.")),
("29802609", "explorer", 1, "Antimicrobial resistance emerges in animal production settings and frequently spreads to humans through the food chain and direct contact",
 ("How does antimicrobial resistance from animal production reach people?", ["Only through the air", "Through the food chain and direct contact", "It never reaches people", "Only through vaccines"],
  "Resistance arising on farms spreads to humans via food and direct contact — a One Health problem.", "Food chain and contact."),
 ("¿Cómo llega a las personas la resistencia antimicrobiana de la producción animal?", ["Solo por el aire", "Por la cadena alimentaria y el contacto directo", "Nunca llega", "Solo por vacunas"],
  "La resistencia surgida en granjas pasa al ser humano por los alimentos y el contacto directo: un problema de Una Salud.", "Cadena alimentaria y contacto.")),
]
