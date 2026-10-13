# Veterinary microbiology III — diseases of horses, cats, pigs, ruminants, poultry and rabbits; parasites
# of livestock and dogs; One Health and antimicrobial use in animals.
# Sources: PubMed reviews (abstracts). Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- Strangles (29424487)
("29424487", "beginner", 2, "Streptococcus equi Infections in Horses",
 ("Strangles is a disease of which animal?", ["Cattle", "Dogs", "Horses", "Chickens"],
  "Strangles is a contagious infection of horses caused by Streptococcus equi subsp. equi.", "Horses."),
 ("¿De qué animal es la enfermedad llamada adenitis equina (papera equina, 'strangles')?", ["Bovinos", "Perros", "Caballos", "Gallinas"],
  "La adenitis equina es una infección contagiosa de los caballos causada por Streptococcus equi subsp. equi.", "Caballos.")),
("29424487", "researcher", 0, "carrier states of strangles in the transmission of disease",
 ("Why are carrier horses important in strangles control?", ["Subclinical carriers keep shedding and infecting others", "Carriers become immune and shield the rest of the herd", "Carriers stop shedding once their fever resolves", "Carriers arise mainly from live-vaccine strains"],
  "Carrier states sustain transmission; detecting carriers (PCR, serology) is key to outbreak control.", "Carriers spread infection."),
 ("¿Por qué los caballos portadores son importantes en el control de la adenitis equina?", ["Los portadores subclínicos siguen eliminando e infectando", "Los portadores se vuelven inmunes y protegen al grupo", "Los portadores dejan de eliminar al ceder la fiebre", "Los portadores surgen sobre todo de cepas vacunales vivas"],
  "Los portadores mantienen la transmisión; detectarlos (PCR, serología) es clave para controlar brotes.", "Los portadores transmiten.")),

# --- Feline panleukopenia (30967253)
("30967253", "curious", 1, "Feline panleukopenia (FPL) is caused by a Carnivore protoparvovirus infection",
 ("What type of virus causes feline panleukopenia?", ["A coronavirus", "A parvovirus", "A retrovirus", "A herpesvirus"],
  "Feline panleukopenia is caused by feline parvovirus (Carnivore protoparvovirus), closely related to canine parvovirus.", "Parvovirus."),
 ("¿Qué tipo de virus causa la panleucopenia felina?", ["Un coronavirus", "Un parvovirus", "Un retrovirus", "Un herpesvirus"],
  "La panleucopenia felina la causa el parvovirus felino (Carnivore protoparvovirus), muy emparentado con el parvovirus canino.", "Parvovirus.")),
("30967253", "researcher", 3, "Feline panleukopenia has re-emerged in Australia in shelter cats associated with failure to vaccinate",
 ("What was associated with the re-emergence of feline panleukopenia in shelter cats?", ["Feeding raw meat diets", "Contaminated commercial cat food", "Disinfectant-resistant virus strains", "Failure to vaccinate cats"],
  "Panleukopenia re-emerged in shelters where cats were not vaccinated.", "Lack of vaccination."),
 ("¿Qué se asoció al resurgimiento de la panleucopenia felina en refugios?", ["Dietas de carne cruda", "Alimento comercial contaminado", "Cepas resistentes a desinfectantes", "Falta de vacunación de los gatos"],
  "La panleucopenia resurgió en refugios donde los gatos no estaban vacunados.", "Falta de vacunación.")),

# --- FCV (17296159)
("17296159", "explorer", 2, "the vaccines do not prevent infection and vaccinated cats can still become persistently infected",
 ("Which statement about feline calicivirus vaccination is correct?", ["It prevents infection and persistent carriage", "It blocks infection but not clinical disease", "It reduces disease but not infection or carriage", "It gives lifelong sterile immunity after one dose"],
  "FCV vaccines reduce clinical disease, but vaccinated cats can still be infected and become carriers; strain variability limits protection.", "Reduces disease, not infection."),
 ("¿Qué afirmación sobre la vacunación contra calicivirus felino es correcta?", ["Previene la infección y la portación persistente", "Bloquea la infección pero no la enfermedad clínica", "Reduce la enfermedad, no la infección ni la portación", "Da inmunidad estéril de por vida con una dosis"],
  "Las vacunas contra FCV reducen la enfermedad, pero los gatos vacunados pueden infectarse y quedar portadores; la variabilidad de cepas limita la protección.", "Reduce enfermedad, no infección.")),

# --- PCV2 (37431709)
("37431709", "expert", 0, "The cytokine imbalance and lymphocyte depletion, thus the impaired immunity, favors invasion of super- or co-infecting agents",
 ("How does porcine circovirus 2 increase the severity of disease in pigs?", ["It depletes lymphocytes, favoring co-infections", "It secretes a potent enterotoxin in the gut", "It forms resistant cysts in muscle tissue", "It blocks platelet aggregation and clotting"],
  "PCV2 disrupts interferon and cytokine pathways and depletes lymphocytes, so co-infections become more severe.", "Immunosuppression."),
 ("¿Cómo aumenta el circovirus porcino 2 la gravedad de la enfermedad en cerdos?", ["Depleta linfocitos y favorece las coinfecciones", "Secreta una enterotoxina potente en el intestino", "Forma quistes resistentes en el tejido muscular", "Bloquea la agregación plaquetaria y la coagulación"],
  "El PCV2 altera las vías del interferón y las citocinas y depleta linfocitos, agravando las coinfecciones.", "Inmunosupresión.")),

# --- PEDV (32502552)
("32502552", "explorer", 3, "a member of the genus Alphacoronavirus in the family Coronaviridae, causes acute diarrhea and/or vomiting, dehydration and high mortality in neonatal piglets",
 ("Porcine epidemic diarrhea virus is a…", ["Parvovirus causing reproductive failure in sows", "Bacterium causing colitis in growing pigs", "Flavivirus transmitted to pigs by mosquitoes", "Coronavirus causing lethal diarrhea in piglets"],
  "PEDV is an alphacoronavirus causing acute diarrhea, dehydration and high mortality in neonatal piglets.", "Coronavirus of piglets."),
 ("El virus de la diarrea epidémica porcina es un…", ["Parvovirus que causa fallas reproductivas en cerdas", "Bacteria que causa colitis en cerdos de engorde", "Flavivirus que los mosquitos transmiten a cerdos", "Coronavirus que causa diarrea letal en lechones"],
  "El PEDV es un alfacoronavirus que causa diarrea aguda, deshidratación y alta mortalidad en lechones neonatos.", "Coronavirus de lechones.")),
("32502552", "researcher", 1, "PEDV-specific IgA effector and memory B cells in orally primed sows play a critical role in sow lactogenic immunity and passive protection of piglets",
 ("How are newborn piglets protected against PEDV?", ["By antibiotics added to the sow's feed", "By milk IgA from orally primed sows", "By the piglet's own antibodies at birth", "By transplacental IgG received in the uterus"],
  "Sows primed orally produce IgA-secreting cells that pass protective antibodies to piglets in milk (lactogenic immunity); the porcine placenta does not transfer antibodies.", "Maternal IgA in milk."),
 ("¿Cómo se protege a los lechones recién nacidos contra el PEDV?", ["Con antibióticos en el alimento de la cerda", "Con IgA láctea de cerdas inmunizadas por vía oral", "Con anticuerpos propios del lechón al nacer", "Con IgG transplacentaria recibida en el útero"],
  "Las cerdas inmunizadas por vía oral generan células secretoras de IgA que pasan anticuerpos protectores en la leche (inmunidad lactogénica); la placenta porcina no transfiere anticuerpos.", "IgA materna en la leche.")),

# --- CSF (28430168)
("28430168", "researcher", 2, "wild boars are a reservoir host transmitting the virus sporadically also to pig farms",
 ("What role do wild boars play in classical swine fever?", ["They are resistant and shield farms from it", "They are dead-end hosts that cannot transmit it", "They are a reservoir that reinfects pig farms", "They spread it mainly to humans as a zoonosis"],
  "Wild boar act as reservoir hosts of CSF virus (a Pestivirus, not zoonotic) and can sporadically reintroduce it into domestic herds.", "Reservoir host."),
 ("¿Qué papel cumplen los jabalíes en la peste porcina clásica?", ["Son resistentes y protegen a las granjas", "Son huéspedes terminales que no lo transmiten", "Son reservorio que reintroduce el virus en granjas", "Lo transmiten sobre todo a humanos como zoonosis"],
  "Los jabalíes son reservorio del virus de la PPC (un Pestivirus, no zoonótico) y pueden reintroducirlo esporádicamente en granjas.", "Reservorio.")),
("28430168", "expert", 3, "Control strategies for epidemic outbreaks in free countries are mainly based on classical intervention measures; i.e., quarantine and strict culling of affected herds",
 ("How do CSF-free countries control an outbreak of classical swine fever?", ["Mass antibiotic treatment of the herds", "Routine vaccination of all domestic pigs", "Treating sick pigs with antiviral drugs", "Quarantine and culling of affected herds"],
  "Free countries rely on quarantine and culling; vaccination is only an emergency option there, while endemic regions use live vaccines.", "Quarantine and culling."),
 ("¿Cómo controlan un brote de peste porcina clásica los países libres?", ["Tratamiento antibiótico masivo de los rebaños", "Vacunación rutinaria de todos los cerdos", "Tratamiento antiviral de los cerdos enfermos", "Cuarentena y sacrificio de los rebaños afectados"],
  "Los países libres usan cuarentena y sacrificio; la vacunación es solo de emergencia, mientras que las zonas endémicas usan vacunas vivas.", "Cuarentena y sacrificio.")),

# --- Heartworm (21922235)
("21922235", "beginner", 1, "Any region where mosquitoes thrive will provide efficient dog-to-dog transportation for the microfilaria",
 ("How is canine heartworm transmitted between dogs?", ["Through contaminated food", "By mosquitoes", "By direct contact", "By fleas"],
  "Dirofilaria immitis microfilariae are carried from dog to dog by mosquitoes.", "Mosquitoes."),
 ("¿Cómo se transmite el gusano del corazón (dirofilariasis) entre perros?", ["Por comida contaminada", "Por mosquitos", "Por contacto directo", "Por pulgas"],
  "Las microfilarias de Dirofilaria immitis pasan de perro a perro a través de mosquitos.", "Mosquitos.")),
("21922235", "expert", 2, "the obligate symbiosis of D. immitis and the bacteria Wolbachia pipientis",
 ("Why is doxycycline used in canine heartworm treatment?", ["It kills the mosquito vectors on the dog", "It dissolves dead worms in the arteries", "It targets Wolbachia, the worm's symbiont", "It kills adult worms in place of melarsomine"],
  "D. immitis depends on its obligate symbiont Wolbachia; antibiotics like doxycycline target it, complementing (not replacing) melarsomine adulticide therapy.", "Targets Wolbachia."),
 ("¿Por qué se usa doxiciclina en el tratamiento de la dirofilariasis canina?", ["Mata a los mosquitos vectores sobre el perro", "Disuelve los gusanos muertos en las arterias", "Ataca a Wolbachia, simbionte del parásito", "Mata a los adultos en lugar de la melarsomina"],
  "D. immitis depende de su simbionte obligado Wolbachia; antibióticos como la doxiciclina lo atacan y complementan (no reemplazan) el tratamiento adulticida con melarsomina.", "Ataca a Wolbachia.")),

# --- Babesiosis (19967929)
("19967929", "curious", 3, "Babesiosis is a tick-borne disease affecting humans and many domestic and wild animals",
 ("How is babesiosis transmitted?", ["By mosquito bites", "By contaminated food", "By sandfly bites", "By tick bites"],
  "Babesiosis is a tick-borne protozoan disease of humans and animals.", "Ticks."),
 ("¿Cómo se transmite la babesiosis?", ["Por picaduras de mosquito", "Por alimentos contaminados", "Por picaduras de flebótomo", "Por picaduras de garrapata"],
  "La babesiosis es una enfermedad protozoaria transmitida por garrapatas que afecta a humanos y animales.", "Garrapatas.")),
("19967929", "explorer", 0, "characterised by haemolytic anaemia, icterus and haemoglobinuria",
 ("Which findings characterize canine babesiosis?", ["Hemolytic anemia, jaundice and hemoglobinuria", "Cough, nasal discharge and bronchopneumonia", "Alopecia, pruritus and crusting dermatitis", "Vomiting, bloody diarrhea and leukopenia"],
  "Babesia destroys red cells, causing hemolytic anemia, icterus and red-brown urine (hemoglobinuria).", "Hemolytic anemia."),
 ("¿Qué hallazgos caracterizan la babesiosis canina?", ["Anemia hemolítica, ictericia y hemoglobinuria", "Tos, secreción nasal y bronconeumonía", "Alopecia, prurito y dermatitis costrosa", "Vómitos, diarrea sanguinolenta y leucopenia"],
  "Babesia destruye glóbulos rojos y causa anemia hemolítica, ictericia y orina rojiza (hemoglobinuria).", "Anemia hemolítica.")),

# --- Haemonchus (27238006)
("27238006", "explorer", 1, "Haemonchus contortus is a highly pathogenic, blood-feeding nematode of small ruminants",
 ("What is Haemonchus contortus?", ["A one-host tick feeding on cattle", "A blood-feeding nematode of sheep and goats", "A tapeworm of the pig's small intestine", "A liver fluke infecting horses and donkeys"],
  "H. contortus is a blood-feeding stomach worm of small ruminants, a major cause of anemia and death.", "Blood-feeding nematode."),
 ("¿Qué es Haemonchus contortus?", ["Una garrapata de un huésped del bovino", "Un nematodo hematófago de ovinos y caprinos", "Una tenia del intestino delgado del cerdo", "Una duela hepática de caballos y burros"],
  "H. contortus es un nematodo hematófago del abomaso de pequeños rumiantes, causa importante de anemia y muerte.", "Nematodo hematófago.")),
("27238006", "researcher", 2, "the 'FAMACHA' conjunctival-colour index",
 ("What does the FAMACHA system assess in sheep and goats?", ["Body condition score as a sign of malnutrition", "Fecal egg counts of gastrointestinal worms", "Conjunctival color as a sign of Haemonchus anemia", "Hoof scoring to detect footrot lesions"],
  "FAMACHA scores eyelid conjunctival color to detect anemia and treat only the animals that need it, slowing resistance.", "Anemia via conjunctival color."),
 ("¿Qué evalúa el sistema FAMACHA en ovinos y caprinos?", ["La condición corporal como indicador de desnutrición", "El recuento de huevos de nematodos en heces", "El color conjuntival, signo de anemia por Haemonchus", "La puntuación de pezuñas para detectar pedero"],
  "FAMACHA puntúa el color de la conjuntiva para detectar anemia y tratar solo a los animales que lo necesitan, frenando la resistencia.", "Anemia por color conjuntival.")),

# --- Anthelmintic resistance (32029182)
("32029182", "researcher", 3, "Parasitic nematodes have biologic and genetic features that favor the development of drug resistance, making the emergence of resistant nematodes inevitable",
 ("Why is relying only on anthelmintics to control livestock nematodes unsustainable?", ["Anthelmintics destroy the rumen's microbial flora", "Most anthelmintics are now banned for livestock", "Dosing makes pasture larvae more infective", "Nematode biology makes resistance inevitable"],
  "Nematode biology and genetics make resistance inevitable; control must change to slow it (e.g., refugia, targeted treatment).", "Resistance is inevitable."),
 ("¿Por qué depender solo de antihelmínticos para controlar nematodos del ganado no es sostenible?", ["Los antihelmínticos destruyen la flora del rumen", "La mayoría de ellos están prohibidos en el ganado", "Las dosis vuelven más infectivas a las larvas del pasto", "La biología de los nematodos hace inevitable la resistencia"],
  "La biología y genética de los nematodos hacen inevitable la resistencia; hay que cambiar el control para frenarla (refugio, tratamientos dirigidos).", "Resistencia inevitable.")),

# --- Neospora (28942304)
("28942304", "explorer", 0, "It is considered to be one of the most important transmissible causes of reproductive failure in cattle",
 ("Neospora caninum is an important cause of what in cattle?", ["Abortion and reproductive failure", "Clinical mastitis in dairy cows", "Foot rot and lameness in adults", "Bronchopneumonia in young calves"],
  "Neosporosis is a leading transmissible cause of abortion and reproductive failure in cattle.", "Abortion."),
 ("¿De qué es causa importante Neospora caninum en bovinos?", ["Abortos y fallas reproductivas", "Mastitis clínica en vacas lecheras", "Pietín y cojera en adultos", "Bronconeumonía en terneros jóvenes"],
  "La neosporosis es una de las principales causas transmisibles de aborto y fallas reproductivas en bovinos.", "Abortos.")),
("28942304", "researcher", 1, "The horizontal route of transmission from the definitive host, the dog, occurs via ingestion of oocysts",
 ("Which animal is a definitive host of Neospora caninum?", ["The cat", "The dog", "The pig", "The horse"],
  "Dogs are definitive hosts and shed oocysts; cattle are infected horizontally from them or vertically (transplacental).", "The dog."),
 ("¿Qué animal es huésped definitivo de Neospora caninum?", ["El gato", "El perro", "El cerdo", "El caballo"],
  "Los perros son huéspedes definitivos y eliminan ooquistes; el ganado se infecta a partir de ellos (transmisión horizontal) o por vía transplacentaria (vertical).", "El perro.")),

# --- Trichomoniasis (23082032)
("23082032", "researcher", 2, "Bovine trichomoniasis is a sexually transmitted protozoan disease with a worldwide distribution",
 ("How is bovine trichomoniasis (Tritrichomonas foetus) transmitted?", ["By ticks feeding on the cows", "By biting flies around the eyes", "Sexually, during breeding", "Through contaminated drinking water"],
  "Bovine trichomoniasis is a sexually transmitted protozoan disease; testing bulls is the core of control.", "Sexually."),
 ("¿Cómo se transmite la tricomoniasis bovina (Tritrichomonas foetus)?", ["Por garrapatas que pican a las vacas", "Por moscas que se alimentan en los ojos", "Por vía sexual, durante el servicio", "Por agua de bebida contaminada"],
  "La tricomoniasis bovina es una protozoosis de transmisión sexual; controlar a los toros es la base del control.", "Sexual.")),

# --- IBV (33809420)
("33809420", "curious", 3, "Infectious bronchitis virus (IBV) is a major economic problem in commercial chicken farms",
 ("Infectious bronchitis is an important disease of…", ["Dairy cows", "Pigs", "Horses", "Chickens"],
  "Infectious bronchitis virus, a gammacoronavirus, causes respiratory and urogenital disease in chickens.", "Chickens."),
 ("La bronquitis infecciosa es una enfermedad importante de…", ["Vacas lecheras", "Cerdos", "Caballos", "Pollos"],
  "El virus de la bronquitis infecciosa, un gammacoronavirus, causa enfermedad respiratoria y urogenital en aves.", "Pollos.")),

# --- Clostridial (9689739)
("9689739", "researcher", 0, "Prevention and control strategies are frequently based upon amelioration, by immunoprophylaxis, of the effects of these molecules",
 ("How are clostridial diseases of sheep and goats mainly prevented?", ["Vaccination against their toxins", "Antibiotics in the drinking water", "Housing animals off contaminated pasture", "Routine deworming of the whole flock"],
  "Clostridial disease is toxin-mediated, so immunoprophylaxis (toxoid vaccines) is the main control strategy.", "Toxoid vaccination."),
 ("¿Cómo se previenen principalmente las clostridiosis de ovinos y caprinos?", ["Vacunando contra sus toxinas", "Con antibióticos en el agua de bebida", "Alojando a los animales fuera del pasto", "Desparasitando a todo el rebaño"],
  "Las clostridiosis están mediadas por toxinas, por eso la inmunoprofilaxis (vacunas con toxoides) es la principal medida.", "Vacunas con toxoides.")),

# --- RHDV2 (39344909)
("39344909", "explorer", 2, "causes a highly contagious disease with hepatic necrosis and disseminated intravascular coagulation",
 ("What does rabbit hemorrhagic disease virus 2 cause?", ["Papillomas and crusting lesions on the skin", "Chronic mucoid diarrhea in weaned kits", "Liver necrosis and disseminated coagulation", "Swollen eyelids and blindness from myxomas"],
  "RHDV2 (a lagovirus) causes a highly contagious disease with hepatic necrosis and DIC in rabbits and hares; it has spread almost globally since 2010.", "Liver necrosis and DIC."),
 ("¿Qué causa el virus de la enfermedad hemorrágica del conejo 2?", ["Papilomas y lesiones costrosas en la piel", "Diarrea mucoide crónica en gazapos destetados", "Necrosis hepática y coagulación diseminada", "Párpados hinchados y ceguera por mixomas"],
  "El RHDV2 (lagovirus) causa una enfermedad muy contagiosa con necrosis hepática y CID en conejos y liebres; se diseminó casi a todo el mundo desde 2010.", "Necrosis hepática y CID.")),

# --- Coccidiosis/NE (16191699)
("16191699", "expert", 3, "The risk of NE, due to the Gram-positive bacterium Clostridium perfringens, has increased in recent years because of the voluntary or legally required withdrawal of the use of certain in-feed antibiotic growth promoters",
 ("Why has necrotic enteritis (Clostridium perfringens) in chickens increased in recent years?", ["Emergence of new virulent avian reoviruses", "Higher stocking temperatures in broiler houses", "Heavier use of in-feed antibiotics", "Withdrawal of antibiotic growth promoters"],
  "Removing antibiotic growth promoters, which had anticlostridial activity, increased necrotic enteritis risk; coccidiosis predisposes to it.", "Growth promoter withdrawal."),
 ("¿Por qué aumentó en los últimos años la enteritis necrótica (Clostridium perfringens) en pollos?", ["Aparición de nuevos reovirus aviares virulentos", "Temperaturas más altas en los galpones", "Mayor uso de antibióticos en el alimento", "Retiro de antibióticos promotores de crecimiento"],
  "Retirar los promotores de crecimiento antibióticos, que tenían actividad anticlostridial, aumentó el riesgo de enteritis necrótica; la coccidiosis predispone.", "Retiro de promotores.")),

# --- Orf (28480985)
("28480985", "curious", 1, "a highly contagious zoonotic viral infection that threatens those who handle sheep and goats",
 ("Who is at risk of orf (contagious ecthyma) infection?", ["Vets who mostly treat dogs and cats", "People who handle sheep and goats", "Workers on fish and shrimp farms", "Beekeepers tending their hives"],
  "Orf is a parapoxvirus zoonosis acquired by people handling sheep and goats; it usually resolves in 3–6 weeks.", "Sheep and goat handlers."),
 ("¿Quiénes corren riesgo de infectarse con orf (ectima contagioso)?", ["Veterinarios que atienden perros y gatos", "Quienes manipulan ovejas y cabras", "Trabajadores de granjas de peces", "Apicultores que cuidan colmenas"],
  "El orf es una zoonosis por parapoxvirus que adquieren quienes manipulan ovinos y caprinos; suele resolverse en 3–6 semanas.", "Quienes manejan ovejas y cabras.")),

# --- Erysipelothrix (19733019)
("19733019", "explorer", 0, "Swine erysipelas caused by E. rhusiopathiae is the disease of greatest prevalence and economic importance",
 ("Which is the most important animal disease caused by Erysipelothrix rhusiopathiae?", ["Swine erysipelas", "Bovine mastitis", "Canine distemper", "Equine strangles"],
  "Swine erysipelas is the most prevalent and costly E. rhusiopathiae disease; in humans it causes erysipeloid.", "Swine erysipelas."),
 ("¿Cuál es la enfermedad animal más importante causada por Erysipelothrix rhusiopathiae?", ["Erisipela porcina", "Mastitis bovina", "Moquillo del perro", "Adenitis equina"],
  "La erisipela porcina es la enfermedad por E. rhusiopathiae más prevalente y costosa; en humanos causa erisipeloide.", "Erisipela porcina.")),
("19733019", "researcher", 3, "Infection due to E. rhusiopathiae in humans is occupationally related",
 ("How do humans usually acquire Erysipelothrix rhusiopathiae?", ["Through bites of infected mosquitoes", "From drinking contaminated well water", "From other people through respiratory droplets", "By handling infected animals or their products"],
  "Human infection (erysipeloid) is occupational — butchers, fish handlers, farmers — after contact with animals or their products.", "Occupational contact."),
 ("¿Cómo adquieren habitualmente los humanos Erysipelothrix rhusiopathiae?", ["Por picaduras de mosquitos infectados", "Por beber agua de pozo contaminada", "De otras personas a través de gotitas respiratorias", "Al manipular animales infectados o sus productos"],
  "La infección humana (erisipeloide) es ocupacional: carniceros, pescadores, productores, tras contacto con animales o sus productos.", "Contacto laboral.")),

# --- One Health (24634782)
("24634782", "beginner", 0, "It is the notion of combining human, animal, and environmental components to address global health challenges",
 ("What does the 'One Health' approach combine?", ["Human, animal and environmental health", "Hospital, primary and community care", "Food safety, trade and animal welfare law", "Clinical, laboratory and genomic medicine"],
  "One Health links human, animal and environmental health to tackle problems such as zoonoses.", "Human, animal, environment."),
 ("¿Qué combina el enfoque 'Una Salud' (One Health)?", ["La salud humana, la animal y la ambiental", "La atención hospitalaria, primaria y comunitaria", "La inocuidad, el comercio y el bienestar animal", "La medicina clínica, de laboratorio y genómica"],
  "Una Salud vincula la salud humana, animal y ambiental para abordar problemas como las zoonosis.", "Humana, animal, ambiental.")),

# --- Antimicrobials in food animals (29802609)
("29802609", "curious", 2, "Antimicrobials have been widely used in food animals for growth promotion since the 1950s",
 ("Since the 1950s, antimicrobials have been widely used in food animals for…", ["Carcass preservation", "Estrus synchronization", "Growth promotion", "Meat tenderizing"],
  "Antimicrobials were used as growth promoters; resistance that emerges can reach humans via food and contact.", "Growth promotion."),
 ("Desde los años 50, los antimicrobianos se usaron mucho en animales de producción para…", ["Conservar las canales", "Sincronizar el celo", "Promover el crecimiento", "Ablandar la carne"],
  "Los antimicrobianos se usaron como promotores de crecimiento; la resistencia que surge puede llegar al ser humano por alimentos y contacto.", "Promover el crecimiento.")),
("29802609", "explorer", 1, "Antimicrobial resistance emerges in animal production settings and frequently spreads to humans through the food chain and direct contact",
 ("How does antimicrobial resistance from animal production reach people?", ["Through antibiotic residues in pasteurized milk", "Through the food chain and direct contact", "Through live vaccines given to livestock", "Through mosquitoes biting livestock and people"],
  "Resistance arising on farms spreads to humans via food and direct contact — a One Health problem.", "Food chain and contact."),
 ("¿Cómo llega a las personas la resistencia antimicrobiana de la producción animal?", ["Por residuos antibióticos en la leche pasteurizada", "Por la cadena alimentaria y el contacto directo", "Por vacunas vivas aplicadas al ganado", "Por mosquitos que pican al ganado y a personas"],
  "La resistencia surgida en granjas pasa al ser humano por los alimentos y el contacto directo: un problema de Una Salud.", "Cadena alimentaria y contacto.")),
]
