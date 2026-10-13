# General & clinical microbiology IX — more clinical bacteria: Nocardia, Vibrio, Stenotrophomonas,
# anaerobic and fastidious pathogens, botulism, Yersinia and the rickettsial diseases.
# Sources: StatPearls chapters (PubMed book records). Excerpts verbatim.
CATEGORY = "microbiology"
Q = [
# --- Nocardia (30252331)
("30252331", "explorer", 2, "Nocardia is typically weak acid-fast positive on microscopy with staining",
 ("Which staining property helps identify Nocardia?", ["Strongly acid-fast, like M. tuberculosis", "Gram-negative diplococci in pairs", "Weakly acid-fast branching gram-positive rods", "Gram-variable spore-forming rods in chains"],
  "Nocardia are branching gram-positive bacilli that are weakly acid-fast — unlike Actinomyces, which are not acid-fast.", "Weakly acid-fast."),
 ("¿Qué propiedad tintorial ayuda a identificar a Nocardia?", ["Fuertemente ácido-alcohol resistente, como M. tuberculosis", "Diplococos gramnegativos agrupados de a pares", "Bacilos grampositivos ramificados, débilmente ácido-resistentes", "Bacilos esporulados de Gram variable en cadenas"],
  "Nocardia son bacilos grampositivos ramificados débilmente ácido-alcohol resistentes, a diferencia de Actinomyces.", "Débilmente AAR.")),
("30252331", "researcher", 0, "Classically, Nocardia manifests as an opportunistic infection in immunocompromised hosts",
 ("In whom does nocardiosis classically occur?", ["Immunocompromised hosts", "Healthy young athletes", "Newborns in their first week", "Women during pregnancy"],
  "Nocardia, an environmental organism, typically causes opportunistic pulmonary, skin or disseminated disease in immunocompromised hosts.", "Immunocompromised."),
 ("¿En quiénes ocurre clásicamente la nocardiosis?", ["En inmunocomprometidos", "En atletas jóvenes sanos", "En recién nacidos de una semana", "En mujeres embarazadas"],
  "Nocardia, un organismo ambiental, causa típicamente enfermedad pulmonar, cutánea o diseminada oportunista en inmunocomprometidos.", "Inmunocomprometidos.")),

# --- V. vulnificus (32119291)
("32119291", "curious", 3, "Transmission of V vulnificus commonly occurs through consumption of contaminated seafood or exposure of open wounds to infected water",
 ("How is Vibrio vulnificus usually acquired?", ["Through bites from infected mosquitoes", "By inhaling contaminated household dust", "Through transfusion of stored blood", "Via raw seafood or seawater on wounds"],
  "V. vulnificus lives in warm seawater; infection follows raw seafood (e.g., oysters) or wound exposure.", "Seafood or seawater wounds."),
 ("¿Cómo se adquiere habitualmente Vibrio vulnificus?", ["Por picaduras de mosquitos infectados", "Inhalando polvo doméstico contaminado", "Por transfusiones de sangre almacenada", "Por mariscos crudos o mar en heridas"],
  "V. vulnificus vive en agua de mar templada; la infección sigue a mariscos crudos (p. ej., ostras) o a la exposición de heridas.", "Mariscos o heridas en agua de mar.")),
("32119291", "researcher", 1, "Vibrio vulnificus accounts for the highest number of seafood-related fatalities in the United States",
 ("Which pathogen causes the most seafood-related deaths in the United States?", ["Norovirus", "Vibrio vulnificus", "Hepatitis A virus", "Salmonella Enteritidis"],
  "V. vulnificus can cause necrotizing skin infection and sepsis with death within 24–48 h; mortality 18–50%.", "Vibrio vulnificus."),
 ("¿Qué patógeno causa más muertes relacionadas con mariscos en Estados Unidos?", ["Norovirus", "Vibrio vulnificus", "Virus de la hepatitis A", "Salmonella Enteritidis"],
  "V. vulnificus puede causar infección cutánea necrotizante y sepsis con muerte en 24–48 h; mortalidad 18–50%.", "Vibrio vulnificus.")),
("32119291", "expert", 2, "Rising ocean temperatures have allowed the organism to extend its range into more northern waters",
 ("Why is the geographic range of Vibrio vulnificus expanding?", ["New antibiotics used in aquaculture", "Widespread vaccination of farmed fish", "Rising sea surface temperatures", "Lower seafood consumption worldwide"],
  "Warming seas let V. vulnificus spread to more northern waters, increasing infections.", "Warmer oceans."),
 ("¿Por qué se está expandiendo el área geográfica de Vibrio vulnificus?", ["Nuevos antibióticos en acuicultura", "Vacunación masiva de peces de criadero", "El aumento de la temperatura del mar", "Menor consumo mundial de mariscos"],
  "El calentamiento del mar permite que V. vulnificus llegue a aguas más al norte, aumentando las infecciones.", "Mares más cálidos.")),

# --- V. parahaemolyticus (29083695)
("29083695", "explorer", 0, "it is a common cause of bacterial gastroenteritis in Asia, specifically in Japan",
 ("Where is Vibrio parahaemolyticus a common cause of bacterial gastroenteritis?", ["Asia, especially Japan", "Antarctica", "The Sahara", "Northern Canada only"],
  "V. parahaemolyticus, linked to raw seafood, is a common cause of gastroenteritis in Asia, especially Japan.", "Asia (Japan)."),
 ("¿Dónde es Vibrio parahaemolyticus una causa frecuente de gastroenteritis bacteriana?", ["Asia, sobre todo Japón", "Antártida", "El Sahara", "Solo el norte de Canadá"],
  "V. parahaemolyticus, ligado a mariscos crudos, es causa frecuente de gastroenteritis en Asia, sobre todo en Japón.", "Asia (Japón).")),

# --- Stenotrophomonas (34283489)
("34283489", "researcher", 3, "It is widely known as an opportunistic organism associated with high morbidity and mortality rates among immunocompromised patients",
 ("Which statement about Stenotrophomonas maltophilia is correct?", ["It mainly causes common colds in children", "It is a gram-positive coccus in clusters", "It is a mosquito-borne arbovirus of birds", "It is a multiresistant hospital bacillus"],
  "S. maltophilia is an emerging multidrug-resistant gram-negative bacillus causing serious infections in immunocompromised patients.", "MDR opportunistic GNB."),
 ("¿Qué afirmación sobre Stenotrophomonas maltophilia es correcta?", ["Causa sobre todo resfríos comunes en niños", "Es un coco grampositivo agrupado en racimos", "Es un arbovirus de aves que transmiten mosquitos", "Es un bacilo hospitalario multirresistente"],
  "S. maltophilia es un bacilo gramnegativo multirresistente emergente que causa infecciones graves en inmunocomprometidos.", "BGN oportunista multirresistente.")),

# --- Lemierre (29763021)
("29763021", "researcher", 1, "septic thrombophlebitis of the internal jugular vein(s)",
 ("What characterizes Lemierre syndrome?", ["Bacterial meningitis in premature newborns", "Septic jugular thrombophlebitis", "Acute viral hepatitis after travel abroad", "Severe pneumonia caused by Legionella"],
  "Lemierre syndrome: oropharyngeal infection spreading to septic thrombophlebitis of the internal jugular vein with anaerobic septicemia (classically Fusobacterium).", "Jugular septic thrombophlebitis."),
 ("¿Qué caracteriza al síndrome de Lemierre?", ["Meningitis bacteriana en prematuros", "Tromboflebitis séptica yugular", "Hepatitis viral aguda tras viajar al exterior", "Neumonía grave causada por Legionella"],
  "Síndrome de Lemierre: infección orofaríngea que se extiende a tromboflebitis séptica de la yugular interna con septicemia anaerobia (clásicamente Fusobacterium).", "Tromboflebitis yugular.")),

# --- Whipple (28722966)
("28722966", "explorer", 3, "Whipple disease is caused by a gram-positive bacteria, Tropheryma whippelii",
 ("Which organism causes Whipple disease?", ["Helicobacter pylori", "Giardia duodenalis", "Mycobacterium avium", "Tropheryma whipplei"],
  "Whipple disease is a systemic infection by the gram-positive Tropheryma whipplei, causing malabsorption, arthralgia and more.", "Tropheryma whipplei."),
 ("¿Qué organismo causa la enfermedad de Whipple?", ["Helicobacter pylori", "Giardia duodenalis", "Mycobacterium avium", "Tropheryma whipplei"],
  "La enfermedad de Whipple es una infección sistémica por el grampositivo Tropheryma whipplei, con malabsorción, artralgias y más.", "Tropheryma whipplei.")),

# --- RMSF (28613631)
("28613631", "curious", 2, "RMSF is the most severe and most common rickettsial infection in the Americas",
 ("What is the most severe and common rickettsial infection in the Americas?", ["Scrub typhus", "Q fever", "Rocky Mountain spotted fever", "Epidemic louse-borne typhus"],
  "Rocky Mountain spotted fever (Rickettsia rickettsii, tick-borne) is the most severe and common rickettsiosis in the Americas.", "RMSF."),
 ("¿Cuál es la rickettsiosis más grave y frecuente de América?", ["Tifus de los matorrales", "Fiebre Q", "Fiebre manchada de las Montañas Rocosas", "Tifus epidémico transmitido por piojos"],
  "La fiebre manchada (Rickettsia rickettsii, por garrapatas) es la rickettsiosis más grave y frecuente de América.", "Fiebre manchada.")),
("28613631", "expert", 0, "Delayed treatment, particularly in RMSF, is strongly associated with severe disease and death",
 ("Why should treatment start empirically when Rocky Mountain spotted fever is suspected?", ["Delay is linked to death and tests lag early", "The disease nearly always resolves alone", "Antibiotics stop working after confirmation", "Serology is reliably positive on day one"],
  "Lab confirmation is rarely available in the first week; delays in doxycycline increase severity and death.", "Delay kills."),
 ("¿Por qué el tratamiento debe iniciarse empíricamente ante sospecha de fiebre manchada?", ["El retraso se asocia a muerte y las pruebas tardan", "La enfermedad casi siempre se resuelve sola", "Los antibióticos dejan de servir tras confirmar", "La serología es positiva ya el primer día"],
  "La confirmación rara vez está disponible en la primera semana; demorar la doxiciclina aumenta la gravedad y la muerte.", "La demora mata.")),

# --- Ehrlichiosis (28722995)
("28722995", "explorer", 1, "Prompt administration of doxycycline significantly improves outcomes, and treatment should not be delayed pending diagnostic confirmation",
 ("What is the treatment of choice for ehrlichiosis?", ["High-dose penicillin G", "Doxycycline, given early", "Oral fluconazole for a week", "Intravenous vancomycin"],
  "Doxycycline improves outcomes in ehrlichiosis and other rickettsial diseases; don't delay for lab results.", "Doxycycline."),
 ("¿Cuál es el tratamiento de elección de la ehrlichiosis?", ["Penicilina G en dosis altas", "Doxiciclina, dada temprano", "Fluconazol oral por una semana", "Vancomicina intravenosa"],
  "La doxiciclina mejora el pronóstico de la ehrlichiosis y otras rickettsiosis; no hay que demorarla por los resultados.", "Doxiciclina.")),

# --- Relapsing fever (28722942)
("28722942", "researcher", 2, "caused by various spirochetes belonging to Borrelia species",
 ("Which organisms cause relapsing fever?", ["Rickettsia species", "Plasmodium species", "Borrelia spirochetes", "Leptospira spirochetes"],
  "Relapsing fever is caused by Borrelia spirochetes transmitted by ticks (TBRF) or lice (LBRF).", "Borrelia."),
 ("¿Qué organismos causan la fiebre recurrente?", ["Especies de Rickettsia", "Especies de Plasmodium", "Espiroquetas de Borrelia", "Espiroquetas de Leptospira"],
  "La fiebre recurrente la causan espiroquetas Borrelia transmitidas por garrapatas (FRTG) o piojos (FRTP).", "Borrelia.")),

# --- Kingella (31613470)
("31613470", "expert", 3, "Kingella kingae is now considered a significant cause of pediatric bacteremia and bone infections in children aged 6 to 48 months",
 ("Kingella kingae is an important cause of what in young children?", ["Urinary tract infection in teenagers", "Pneumonia in elderly nursing-home residents", "Meningitis in newborns under 1 month", "Bone and joint infections in toddlers"],
  "Improved diagnostics show K. kingae is a major cause of bacteremia and osteoarticular infection at 6–48 months.", "Bone and joint infections in toddlers."),
 ("¿De qué es causa importante Kingella kingae en niños pequeños?", ["Infección urinaria en adolescentes", "Neumonía en ancianos de residencias", "Meningitis en neonatos de menos de un mes", "Osteoartritis infecciosa en niños pequeños"],
  "Con mejores técnicas diagnósticas, K. kingae resultó causa importante de bacteriemia e infección osteoarticular de 6 a 48 meses.", "Infecciones osteoarticulares infantiles.")),

# --- Yersinia enterocolitica (29763012)
("29763012", "researcher", 0, "The infection is manifested as acute diarrhea, mesenteric adenitis, terminal ileitis, and pseudoappendicitis",
 ("Which presentation is characteristic of Yersinia enterocolitica infection?", ["Pseudoappendicitis from mesenteric adenitis", "A painless genital ulcer with adenopathy", "Unilateral facial palsy after a tick bite", "Painful bloody urine with flank pain"],
  "Y. enterocolitica causes diarrhea, mesenteric adenitis and terminal ileitis that can mimic appendicitis.", "Pseudoappendicitis."),
 ("¿Qué presentación es característica de la infección por Yersinia enterocolitica?", ["Seudoapendicitis por adenitis mesentérica", "Úlcera genital indolora con adenopatía", "Parálisis facial unilateral tras picadura", "Orina con sangre y dolor en el flanco"],
  "Y. enterocolitica causa diarrea, adenitis mesentérica e ileítis terminal que pueden simular una apendicitis.", "Seudoapendicitis.")),
("29763012", "expert", 2, "Humans acquire Yersinia after consumption of contaminated food, as well as a blood transfusion",
 ("Besides contaminated food, how can Yersinia enterocolitica be transmitted?", ["Mosquito bites", "Sexual contact", "Blood transfusion", "Inhaling fungal spores"],
  "Yersinia can grow at refrigeration temperatures, so contaminated stored blood can transmit it.", "Blood transfusion."),
 ("Además de alimentos contaminados, ¿cómo puede transmitirse Yersinia enterocolitica?", ["Picaduras de mosquito", "Contacto sexual", "Transfusión de sangre", "Inhalación de esporas"],
  "Yersinia puede crecer a temperatura de heladera, por eso la sangre almacenada contaminada puede transmitirla.", "Transfusión.")),

# --- Anaplasmosis (30020713)
("30020713", "explorer", 1, "is transmitted by Ixodes scapularis in the northeast United States",
 ("Which ticks transmit Anaplasma phagocytophilum (and Lyme disease)?", ["Aedes", "Ixodes", "Anopheles", "Culex"],
  "Ixodes ticks transmit anaplasmosis, Lyme disease, babesiosis and more, so co-infections occur.", "Ixodes."),
 ("¿Qué garrapatas transmiten Anaplasma phagocytophilum (y la enfermedad de Lyme)?", ["Aedes", "Ixodes", "Anopheles", "Culex"],
  "Las garrapatas Ixodes transmiten anaplasmosis, Lyme, babesiosis y más, por eso hay coinfecciones.", "Ixodes.")),

# --- Botulism (29083673)
("29083673", "beginner", 0, "Botulism is a rare but potentially fatal syndrome of diffuse, flaccid paralysis caused by botulinum neurotoxin",
 ("What does botulism cause?", ["Flaccid (limp) paralysis", "Spastic muscle rigidity", "Skin rash only", "Kidney stones"],
  "Botulinum neurotoxin blocks acetylcholine release, causing descending flaccid paralysis — unlike tetanus, which causes rigidity.", "Flaccid paralysis."),
 ("¿Qué causa el botulismo?", ["Parálisis flácida", "Rigidez muscular espástica", "Solo exantema", "Cálculos renales"],
  "La neurotoxina botulínica bloquea la liberación de acetilcolina y causa parálisis flácida descendente, a diferencia del tétanos, que causa rigidez.", "Parálisis flácida.")),
("29083673", "explorer", 3, "BoNT, the most potent poison known to man",
 ("Which substance is considered the most potent poison known?", ["Potassium cyanide", "Inland taipan venom", "Arsenic trioxide", "Botulinum neurotoxin"],
  "Botulinum neurotoxin is the most potent known poison and a bioterrorism concern.", "Botulinum toxin."),
 ("¿Qué sustancia se considera el veneno más potente conocido?", ["Cianuro de potasio", "Veneno de taipán", "Trióxido de arsénico", "Toxina botulínica"],
  "La neurotoxina botulínica es el veneno más potente conocido y una preocupación de bioterrorismo.", "Toxina botulínica.")),
("29083673", "researcher", 2, "The administration of polyvalent antitoxin to BoNT mitigates the clinical course of botulism. However, no true antidote exists",
 ("What is the main specific treatment of botulism?", ["A course of antibiotics alone", "A toxoid vaccine after symptoms begin", "Antitoxin plus supportive care", "High-dose corticosteroids for a week"],
  "Antitoxin limits progression but doesn't reverse paralysis; patients may need weeks of mechanical ventilation.", "Antitoxin + support."),
 ("¿Cuál es el tratamiento específico principal del botulismo?", ["Un tratamiento solo con antibióticos", "Una vacuna toxoide tras los síntomas", "Antitoxina más medidas de sostén", "Corticoides en dosis altas una semana"],
  "La antitoxina limita la progresión pero no revierte la parálisis; puede requerirse ventilación mecánica por semanas.", "Antitoxina + sostén.")),

# --- Scrub typhus (32644327)
("32644327", "researcher", 1, "The infection is transmitted to humans through the bite of larval trombiculid mites",
 ("How is scrub typhus (Orientia tsutsugamushi) transmitted?", ["Human body lice", "Larval trombiculid mites", "Fleas carried by urban rats", "Aedes aegypti mosquitoes"],
  "Scrub typhus is transmitted by larval trombiculid mites, often leaving a black eschar at the bite site.", "Chiggers."),
 ("¿Cómo se transmite el tifus de los matorrales (Orientia tsutsugamushi)?", ["Piojos corporales humanos", "Larvas de ácaros trombicúlidos", "Pulgas de ratas de ciudad", "Mosquitos Aedes aegypti en zonas urbanas"],
  "El tifus de los matorrales lo transmiten larvas de ácaros trombicúlidos y suele dejar una escara negra en la picadura.", "Larvas de ácaros.")),

# --- Typhus group (28846313)
("28846313", "explorer", 2, "Epidemic typhus is spread by the human body louse",
 ("How is epidemic typhus (Rickettsia prowazekii) transmitted?", ["By hard ticks", "By Anopheles mosquitoes", "By the human body louse", "By contaminated water"],
  "Epidemic typhus spreads by body lice, typically in war, disasters, refugee camps and overcrowding; murine typhus is flea-borne.", "Body louse."),
 ("¿Cómo se transmite el tifus epidémico (Rickettsia prowazekii)?", ["Por garrapatas duras", "Por mosquitos Anopheles", "Por el piojo corporal", "Por agua contaminada"],
  "El tifus epidémico lo transmite el piojo corporal, típicamente en guerras, desastres, campos de refugiados y hacinamiento; el murino, las pulgas.", "Piojo corporal.")),
("28846313", "curious", 0, "Murine typhus is a flea-borne zoonosis maintained primarily in rodents",
 ("Murine typhus is transmitted mainly by…", ["Fleas, with rodent reservoirs", "Human body lice in crowded places", "Hard ticks carried by dogs", "Phlebotomine sandflies at dusk"],
  "Murine typhus (Rickettsia typhi) is flea-borne and maintained in rodents.", "Fleas."),
 ("El tifus murino se transmite principalmente por…", ["Pulgas, con roedores de reservorio", "Piojos corporales en lugares hacinados", "Garrapatas duras de los perros", "Flebótomos que pican al atardecer"],
  "El tifus murino (Rickettsia typhi) se transmite por pulgas y se mantiene en roedores.", "Pulgas.")),
]
