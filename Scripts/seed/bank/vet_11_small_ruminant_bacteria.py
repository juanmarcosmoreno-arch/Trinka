# Small ruminant bacterial diseases — Brucella melitensis and Rev.1, Brucella ovis, Chlamydia abortus,
# Q fever in Dutch goats, Campylobacter abortion, caseous lymphadenitis, footrot, enterotoxemia, Johne's disease,
# CCPP, contagious agalactia, ovine mastitis, listeriosis, dermatophilosis, anthrax.
# Sources: PubMed paper and review abstracts. Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- Rev.1 vaccine (12414167)
("12414167", "explorer", 0, "Since first developed in the mid-1950s, the Brucella melitensis vaccine strain Rev.1 has been used worldwide",
 ("When was the Brucella melitensis Rev.1 vaccine for sheep and goats first developed?", ["In the mid-1950s", "In the early 1900s", "In the late 1980s", "In the 2010s"],
  "Rev.1 dates from the mid-1950s and has been used worldwide to protect small ruminants in endemic areas.", "Mid-1950s."),
 ("¿Cuándo se desarrolló por primera vez la vacuna Rev.1 de Brucella melitensis para ovinos y caprinos?", ["A mediados de los años 50", "A principios del siglo XX", "A fines de los años 80", "En la década de 2010"],
  "Rev.1 data de mediados de los años 50 y se ha usado en todo el mundo para proteger pequeños rumiantes en zonas endémicas.", "Mediados de los 50.")),
("12414167", "researcher", 1, "An omp2 based PCR method has been developed that traced the lineage of Israeli B. melitensis biovar 1 strains",
 ("In Israel, which tool was developed to trace Rev.1 vaccine strain lineage after cases of excretion in milk and a human infection?", ["A Rose Bengal plate agglutination test", "An omp2-based PCR method", "A skin test with brucellin allergen", "Whole-genome optical mapping"],
  "The omp2 locus served as an epidemiological tag distinguishing the Rev.1 vaccine strain from field strains.", "omp2 PCR."),
 ("En Israel, ¿qué herramienta se desarrolló para rastrear el linaje de la cepa vacunal Rev.1 tras casos de excreción en leche y una infección humana?", ["Una prueba de aglutinación con Rosa de Bengala", "Un método de PCR basado en omp2", "Una prueba cutánea con brucelina", "Un mapeo óptico del genoma completo"],
  "El locus omp2 sirvió como marcador epidemiológico para distinguir la cepa vacunal Rev.1 de las cepas de campo.", "PCR de omp2.")),

# --- Human B. melitensis outbreak from goats, Argentina (9537757)
("9537757", "beginner", 2, "Active brucellosis was diagnosed in 91.3% of the subjects in continuous contact with goats",
 ("In an Argentine farm outbreak of Brucella melitensis, which people were most often diagnosed with active brucellosis?", ["Those who often ate goat cheese", "Those who drank raw goat milk", "Those in daily contact with goats", "Those who never visited the farm"],
  "91.3% of people in continuous contact with goats had active brucellosis versus 32% with occasional contact.", "Constant goat contact."),
 ("En un brote de Brucella melitensis en un campo de Argentina, ¿qué personas tuvieron con más frecuencia brucelosis activa?", ["Las que comían queso de cabra", "Las que tomaban leche cruda de cabra", "Las en contacto diario con cabras", "Las que nunca visitaron el campo"],
  "El 91,3% de quienes tenían contacto continuo con cabras tuvo brucelosis activa, frente al 32% con contacto ocasional.", "Contacto con cabras.")),
("9537757", "explorer", 3, "All the 60 subjects denied consumption of goat cheese or milk",
 ("Why did the Argentine Brucella melitensis outbreak point to occupational rather than foodborne infection?", ["All patients had been vaccinated with Rev.1", "The goats on the farm were all seronegative", "Only laboratory staff became ill", "No subject had consumed goat cheese or milk"],
  "None of the 60 people ate goat dairy products; infection followed contact with infected goats or manure after caprine abortions.", "No dairy eaten."),
 ("¿Por qué el brote de Brucella melitensis en Argentina apuntó a una infección laboral y no alimentaria?", ["Todos habían sido vacunados con Rev.1", "Las cabras del campo eran todas seronegativas", "Solo enfermó personal de laboratorio", "Nadie había consumido queso ni leche de cabra"],
  "Ninguna de las 60 personas consumió lácteos de cabra; la infección siguió al contacto con cabras o estiércol infectados tras abortos caprinos.", "Sin consumo de lácteos.")),

# --- B. ovis in seronegative rams (2298657)
("2298657", "researcher", 0, "9 (37.5%) of 24 rams were actively excreting B ovis; 6 of those 9 rams were seronegative",
 ("In a 5-year Brucella ovis control program in Suffolk rams, what did semen culture reveal in the fifth year?", ["37.5% were shedding, most of them seronegative", "No ram was shedding the organism in semen", "All shedding rams had obvious epididymitis", "Only seropositive rams were shedding"],
  "Nine of 24 rams excreted B. ovis in semen, and six of those nine were seronegative carriers.", "Seronegative shedders."),
 ("En un programa de control de Brucella ovis de 5 años en carneros Suffolk, ¿qué reveló el cultivo de semen en el quinto año?", ["37,5% excretaba, la mayoría seronegativos", "Ningún carnero excretaba el germen en semen", "Todos los excretores tenían epididimitis evidente", "Solo excretaban los carneros seropositivos"],
  "Nueve de 24 carneros excretaban B. ovis en el semen, y seis de esos nueve eran portadores seronegativos.", "Excretores seronegativos.")),
("2298657", "explorer", 1, "It was hypothesized that vaccination protected rams against the clinical disease but not the carrier state",
 ("Why were few cases of epididymitis seen in a ram flock where many rams still shed Brucella ovis?", ["The rams were all too young to breed", "Vaccination prevented disease but not carriage", "The strain had lost its virulence genes", "Rams were treated with tetracycline yearly"],
  "Authors proposed that vaccination protected against clinical epididymitis but did not stop the carrier state.", "Vaccine stops disease, not carriage."),
 ("¿Por qué se vieron pocos casos de epididimitis en un lote de carneros donde muchos seguían excretando Brucella ovis?", ["Todos eran muy jóvenes para servir", "La vacuna evitaba la enfermedad, no el portador", "La cepa había perdido sus genes de virulencia", "Se trataba a los carneros con tetraciclina cada año"],
  "Los autores propusieron que la vacunación protegía contra la epididimitis clínica pero no evitaba el estado de portador.", "Evita enfermedad, no portación.")),

# --- B. ovis experimental infection (24138019)
("24138019", "researcher", 2, "Rams can begin shedding B. ovis in semen as early as 28 days after exposure",
 ("In rams experimentally infected with Brucella ovis, how soon could the organism first be shed in semen?", ["After about 7 days", "After about 6 months", "As early as 28 days", "Only after one full year"],
  "Shedding began at day 28 in one ram and by day 49 ten rams shed B. ovis; epididymitis appeared from day 36.", "~28 days."),
 ("En carneros infectados experimentalmente con Brucella ovis, ¿cuánto tardó como mínimo en aparecer el germen en el semen?", ["Unos 7 días", "Unos 6 meses", "Desde los 28 días", "Recién después de un año"],
  "La excreción comenzó el día 28 en un carnero y para el día 49 diez carneros excretaban B. ovis; la epididimitis apareció desde el día 36.", "~28 días.")),
("24138019", "researcher", 3, "The B. ovis ELISA test identified infected rams at an earlier stage than the CFT",
 ("Which serological test detected Brucella ovis-infected rams earliest in an experimental study?", ["Gel diffusion", "Complement fixation", "Rose Bengal", "ELISA test"],
  "ELISA picked up infected rams 19–36 days after exposure, earlier than the CFT; the gel diffusion test lagged behind shedding.", "ELISA."),
 ("¿Qué prueba serológica detectó antes a los carneros infectados con Brucella ovis en un estudio experimental?", ["Inmunodifusión", "Fijación del complemento", "Rosa de Bengala", "Prueba de ELISA"],
  "El ELISA detectó a los carneros infectados 19–36 días tras la exposición, antes que la FC; la inmunodifusión se retrasó respecto de la excreción.", "ELISA.")),

# --- Chlamydia abortus 1B vaccine (33946380)
("33946380", "beginner", 0, "Chlamydia abortus infects livestock species worldwide and is the cause of enzootic abortion of ewes (EAE)",
 ("Which bacterium causes enzootic abortion of ewes (EAE)?", ["Chlamydia abortus", "Brucella ovis", "Listeria monocytogenes", "Clostridium perfringens"],
  "Chlamydia abortus is the cause of enzootic abortion of ewes, a major cause of lamb loss worldwide.", "Chlamydia abortus."),
 ("¿Qué bacteria causa el aborto enzoótico de las ovejas (AEO)?", ["Chlamydia abortus", "Brucella ovis", "Listeria monocytogenes", "Clostridium perfringens"],
  "Chlamydia abortus es la causa del aborto enzoótico ovino, una causa importante de pérdida de corderos en el mundo.", "Chlamydia abortus.")),
("33946380", "researcher", 1, "The analysis provided no evidence of meaningful differences between vt and wt strains in terms of the measured pathological parameters",
 ("How did placental lesions from the live Chlamydia abortus 1B vaccine strain compare with those of wild-type infection in ewes?", ["Vaccine lesions were far milder", "No meaningful differences were found", "Only wild-type caused placentitis", "Vaccine lesions spared the cotyledons"],
  "Placental pathology from the vaccine-type strain was essentially indistinguishable from natural wild-type infection.", "No real difference."),
 ("¿Cómo se compararon las lesiones placentarias de la cepa vacunal viva 1B de Chlamydia abortus con las de la infección natural en ovejas?", ["Las vacunales eran mucho más leves", "No hubo diferencias relevantes", "Solo la cepa salvaje causó placentitis", "Las vacunales respetaban los cotiledones"],
  "La patología placentaria por la cepa vacunal fue prácticamente indistinguible de la infección natural por cepa salvaje.", "Sin diferencias reales.")),

# --- Dutch Q fever epidemic (22066649)
("22066649", "beginner", 2, "Pneumonia was the most common clinical presentation (62% in 2007 and 2008)",
 ("During the 2007–2010 Dutch Q fever epidemic, what was the most common presentation in notified patients?", ["Endocarditis", "Skin abscesses", "Pneumonia", "Meningitis"],
  "Pneumonia was seen in 62% of notified acute Q fever cases in 2007 and 2008.", "Pneumonia."),
 ("Durante la epidemia de fiebre Q en Países Bajos (2007–2010), ¿cuál fue la presentación más común en los pacientes notificados?", ["Endocarditis", "Abscesos cutáneos", "Neumonía", "Meningitis"],
  "La neumonía se observó en el 62% de los casos agudos notificados en 2007 y 2008.", "Neumonía.")),
("22066649", "explorer", 3, "Airborne transmission of contaminated dust particles from commercial dairy goat farms in densely populated areas has probably caused this epidemic",
 ("How was Coxiella burnetii most likely spread from dairy goat farms to people in the Dutch Q fever epidemic?", ["Raw goat milk sold at local markets", "Tick bites in the countryside", "Person-to-person respiratory spread", "Contaminated dust carried by the air"],
  "Only 3.2% of patients worked in agriculture; airborne dust from goat farms near dense populations was the probable route.", "Airborne dust."),
 ("¿Cómo se propagó probablemente Coxiella burnetii desde las granjas de cabras lecheras a las personas en la epidemia neerlandesa?", ["Por leche cruda de cabra en mercados", "Por picaduras de garrapatas en el campo", "Por contagio respiratorio entre personas", "Por polvo contaminado llevado por el aire"],
  "Solo el 3,2% de los pacientes trabajaba en el agro; el polvo aéreo de granjas cercanas a zonas pobladas fue la vía probable.", "Polvo por el aire.")),

# --- Goat manure and Q fever (24788538)
("24788538", "researcher", 0, "Proximity of contaminated land parcels predicted human cases better than proximity of QFPFs (80% vs. 58%, 0-5 km in 2009)",
 ("In the Netherlands, what predicted human Q fever cases better than proximity to Q fever-positive goat farms?", ["Fields spread with contaminated manure", "Proximity to cattle slaughterhouses", "Living near urban hospitals", "Distance to the nearest highway"],
  "Proximity to land parcels with contaminated goat manure predicted 80% of cases versus 58% for infected farms.", "Manured fields."),
 ("En Países Bajos, ¿qué predijo mejor los casos humanos de fiebre Q que la cercanía a granjas caprinas positivas?", ["Campos abonados con estiércol contaminado", "La cercanía a frigoríficos bovinos", "Vivir cerca de hospitales urbanos", "La distancia a la autopista más cercana"],
  "La cercanía a parcelas con estiércol caprino contaminado predijo el 80% de los casos, frente al 58% de las granjas infectadas.", "Campos abonados.")),

# --- Campylobacter clone SA (24648552)
("24648552", "researcher", 1, "since 2003 a highly pathogenic, tetracycline-resistant C. jejuni clone (named SA) has become the predominant cause of sheep abortions in the United States",
 ("What has been the predominant cause of sheep abortions in the United States since 2003?", ["Brucella ovis spread by infected rams", "A resistant C. jejuni clone (SA)", "Coxiella burnetii from dairy goats", "Campylobacter fetus subsp. venerealis"],
  "Clone SA (ST-8) of C. jejuni, highly pathogenic and tetracycline-resistant, became dominant in US ovine abortions.", "C. jejuni clone SA."),
 ("¿Cuál ha sido la causa predominante de abortos ovinos en Estados Unidos desde 2003?", ["Brucella ovis transmitida por carneros", "Un clon resistente de C. jejuni (SA)", "Coxiella burnetii de cabras lecheras", "Campylobacter fetus subsp. venerealis"],
  "El clon SA (ST-8) de C. jejuni, muy patógeno y resistente a tetraciclina, se volvió dominante en abortos ovinos en EE. UU.", "Clon SA de C. jejuni.")),
("24648552", "expert", 2, "the Great Britain isolates were essentially susceptible to most tested antibiotics, including tetracycline",
 ("How did Campylobacter jejuni sheep-abortion isolates from Great Britain differ from late US isolates?", ["They were all clone SA (ST-8)", "They were universally tetracycline-resistant", "They were diverse and tetracycline-susceptible", "They were Campylobacter fetus instead"],
  "British isolates spanned 19 STs without ST-8 and were susceptible, likely because tetracyclines are not used there for abortion control.", "Diverse, susceptible."),
 ("¿En qué se diferenciaban los aislamientos de Campylobacter jejuni de abortos ovinos de Gran Bretaña de los aislamientos recientes de EE. UU.?", ["Eran todos del clon SA (ST-8)", "Eran todos resistentes a tetraciclina", "Eran diversos y sensibles a tetraciclina", "Eran en realidad Campylobacter fetus"],
  "Los aislamientos británicos abarcaban 19 ST sin ST-8 y eran sensibles, quizás porque allí no se usan tetraciclinas para controlar abortos.", "Diversos y sensibles.")),

# --- Campylobacter abortion pathology (34311616)
("34311616", "explorer", 3, "Placentitis was the microscopic lesion identified most consistently in natural abortions (93%)",
 ("In natural Campylobacter abortions in sheep, which microscopic lesion was found most consistently?", ["Meningitis", "Hepatitis", "Myocarditis", "Placentitis"],
  "Placentitis was present in 93% of natural cases, often with bacterial colonies in chorionic villi.", "Placentitis."),
 ("En abortos ovinos naturales por Campylobacter, ¿qué lesión microscópica se halló con más regularidad?", ["Meningitis", "Hepatitis", "Miocarditis", "Placentitis"],
  "La placentitis estuvo presente en el 93% de los casos naturales, a menudo con colonias bacterianas en las vellosidades coriónicas.", "Placentitis.")),

# --- Caseous lymphadenitis in goats (11243659)
("11243659", "explorer", 0, "caseous lymphadenitis is a subacute disease with an incubation period of 8-9 days",
 ("After experimental intradermal infection of goats with Corynebacterium pseudotuberculosis, what was the incubation period of caseous lymphadenitis?", ["8–9 days", "1–2 days", "About 3 months", "Over a year"],
  "Gross caseous lesions appeared in draining lymph nodes from days 8–9 after infection.", "8–9 days."),
 ("Tras infectar cabras por vía intradérmica con Corynebacterium pseudotuberculosis, ¿cuál fue el período de incubación de la linfadenitis caseosa?", ["8–9 días", "1–2 días", "Unos 3 meses", "Más de un año"],
  "Las lesiones caseosas macroscópicas aparecieron en los ganglios de drenaje desde los días 8–9.", "8–9 días.")),
("11243659", "researcher", 1, "it is not detectable serologically until after 15 days of infection",
 ("In experimentally infected goats, when did caseous lymphadenitis become detectable by serology?", ["Within 48 hours", "Only after 15 days", "Only after 6 months", "Never during the trial"],
  "Agglutination titres appeared at 15–17 days and haemolysis-inhibition titres at 20–25 days.", "After 15 days."),
 ("En cabras infectadas experimentalmente, ¿cuándo pudo detectarse la linfadenitis caseosa por serología?", ["Dentro de las 48 horas", "Recién después de 15 días", "Recién después de 6 meses", "Nunca durante el ensayo"],
  "Los títulos de aglutinación aparecieron a los 15–17 días y los de inhibición de la hemólisis a los 20–25 días.", "Después de 15 días.")),

# --- CLA meat inspection Australia (31175223)
("31175223", "expert", 2, "reduced palpation from eleven carcase sites to the four sites most commonly affected",
 ("What alternative post-mortem inspection for caseous lymphadenitis was assessed in Australian sheep and goats?", ["Replacing palpation with routine serology", "Incising every lymph node in the carcase", "Palpating 4 common sites instead of 11", "Inspecting only the lungs and liver"],
  "Reducing palpation to the four most often affected sites missed few extra carcases with CLA in edible tissue and was adopted.", "4 sites, not 11."),
 ("¿Qué inspección post mortem alternativa para la linfadenitis caseosa se evaluó en ovinos y caprinos de Australia?", ["Reemplazar la palpación por serología", "Incidir todos los ganglios de la canal", "Palpar 4 sitios comunes en vez de 11", "Inspeccionar solo pulmones e hígado"],
  "Reducir la palpación a los cuatro sitios más afectados dejaba pasar pocas canales más con lesiones en tejido comestible y fue adoptado.", "4 sitios, no 11.")),

# --- Flock-specific footrot vaccination (18621488)
("18621488", "researcher", 3, "antigenic competition precludes effective vaccination with multivalent vaccines that contain all serogroups",
 ("Why can't a single multivalent vaccine containing all Dichelobacter nodosus serogroups effectively protect sheep against footrot?", ["Fimbriae are not immunogenic", "The vaccine causes lameness", "Serogroups share fimbriae", "Competition between antigens"],
  "Protection is largely serogroup-specific, and antigenic competition weakens responses when all serogroups are combined.", "Antigenic competition."),
 ("¿Por qué una sola vacuna multivalente con todos los serogrupos de Dichelobacter nodosus no protege bien a las ovejas contra el pietín?", ["Las fimbrias no son inmunógenas en ovinos", "La vacuna combinada causa cojera", "Los serogrupos tienen fimbrias idénticas", "Por competencia antigénica"],
  "La protección es en gran medida específica del serogrupo, y la competencia antigénica debilita la respuesta al combinarlos todos.", "Competencia antigénica.")),
("18621488", "explorer", 0, "Use of flock specific monovalent whole cell vaccines over whole flocks for only one season and culling of the few non-responders",
 ("Which approach eradicated footrot from two Australian pilot flocks?", ["Flock-specific vaccine and culling", "Monthly hoof trimming without vaccination", "Long-acting penicillin for all ewes", "Moving flocks to new pastures yearly"],
  "Monovalent whole-cell vaccines matched to the flock's serogroup, given for one season with culling of non-responders, eliminated the disease.", "Specific vaccine + culling."),
 ("¿Qué estrategia erradicó el pietín de dos majadas piloto en Australia?", ["Vacuna específica de la majada y descarte", "Despezuñado mensual sin aplicar vacunas", "Penicilina de larga acción a todas las ovejas", "Trasladar la majada a otra pastura cada año"],
  "Vacunas monovalentes de células enteras ajustadas al serogrupo, aplicadas una temporada con descarte de no respondedores, eliminaron la enfermedad.", "Vacuna específica + descarte.")),

# --- Footrot eradication in Nepal (12243270)
("12243270", "expert", 1, "There was no recurrence of virulent footrot after November 1993",
 ("What was the outcome of specific Dichelobacter nodosus vaccination of migrating sheep and goats in western Nepal?", ["Footrot spread to alpine wildlife", "No recurrence of virulent footrot", "Only goats were fully protected", "Benign strains disappeared first"],
  "With specific vaccination plus inspection and culling, virulent footrot never returned after November 1993; benign strains persisted.", "No recurrence after 1993."),
 ("¿Cuál fue el resultado de vacunar específicamente contra Dichelobacter nodosus a ovejas y cabras trashumantes del oeste de Nepal?", ["El pietín pasó a la fauna alpina", "El pietín virulento no reapareció tras 1993", "Solo se protegió a las cabras", "Desaparecieron primero las cepas benignas"],
  "Con vacuna específica, inspección y descarte, el pietín virulento no volvió tras noviembre de 1993; las cepas benignas persistieron.", "Sin recurrencia tras 1993.")),

# --- Zinc sulphate footbathing (11491224)
("11491224", "beginner", 2, "Repeated daily footbathing combined with prolonged exposure to a dry environment eradicated footrot in sheep",
 ("Which treatment eradicated footrot in a Merino sheep trial without paring the feet?", ["One injection of long-acting antibiotics", "Painting hooves with tar each month", "Daily zinc sulphate footbaths", "Feeding extra zinc in the daily ration"],
  "Five daily 10-minute baths in 15–18% zinc sulphate with surfactant, plus a dry environment, left no lesions for a year.", "Zinc sulphate footbaths."),
 ("¿Qué tratamiento erradicó el pietín en un ensayo con ovejas Merino sin despezuñar?", ["Una inyección de antibiótico de larga acción", "Pintar las pezuñas con alquitrán cada mes", "Pediluvios diarios con sulfato de zinc", "Agregar zinc extra a la ración diaria"],
  "Cinco baños diarios de 10 minutos en sulfato de zinc al 15–18% con surfactante, más un ambiente seco, no dejaron lesiones en un año.", "Pediluvios con sulfato de zinc.")),

# --- Enterotoxemia sheep vs goats (1892271)
("1892271", "researcher", 3, "Lesions were not observed in the gastrointestinal tract of the 4 lambs; however, severe hemorrhagic enterocolitis was found in the 4 goat kids",
 ("After intraduodenal infusion of Clostridium perfringens type D, how did gut lesions differ between lambs and goat kids?", ["Both species had identical colitis", "Only lambs showed enterocolitis", "Neither species showed any death", "Only goat kids had enterocolitis"],
  "Kids developed severe hemorrhagic enterocolitis while lambs had no gut lesions, which may explain species differences in vaccine response.", "Only kids."),
 ("Tras infundir Clostridium perfringens tipo D en el duodeno, ¿cómo difirieron las lesiones intestinales entre corderos y cabritos?", ["Ambas especies tuvieron igual colitis", "Solo los corderos tuvieron enterocolitis", "Ninguna especie llegó a morir", "Solo los cabritos tuvieron enterocolitis"],
  "Los cabritos desarrollaron enterocolitis hemorrágica grave y los corderos no tuvieron lesiones intestinales, lo que explicaría diferencias en la respuesta a la vacuna.", "Solo los cabritos.")),
("1892271", "explorer", 0, "The 4 lambs and 4 goat kids died within 25 hours of beginning the infusions",
 ("How quickly did lambs and goat kids die after intraduodenal infusion of Clostridium perfringens type D?", ["Within 25 hours", "After about 2 weeks", "After about 3 months", "None of them died"],
  "All eight animals died within 25 hours, reflecting the acute course of type D enterotoxemia.", "Within 25 h."),
 ("¿Qué tan rápido murieron corderos y cabritos tras la infusión duodenal de Clostridium perfringens tipo D?", ["En menos de 25 horas", "Tras unas 2 semanas", "Tras unos 3 meses", "Ninguno murió"],
  "Los ocho animales murieron en menos de 25 horas, reflejo del curso agudo de la enterotoxemia tipo D.", "Menos de 25 h.")),

# --- Johne's vaccination in Norwegian goats (4002570)
("4002570", "researcher", 1, "the infection rate was reduced from 53 to 1 per cent",
 ("How much did vaccination reduce the paratuberculosis infection rate in Norwegian goats (1967–82)?", ["From 53% to 30%", "From 53% to 1%", "From 10% to 5%", "It did not change"],
  "Post-mortem examination of 15,219 goats showed infection dropping from 53% to 1% after about 131,000 were vaccinated.", "53% to 1%."),
 ("¿Cuánto redujo la vacunación la tasa de paratuberculosis en cabras de Noruega (1967–82)?", ["Del 53% al 30%", "Del 53% al 1%", "Del 10% al 5%", "No cambió"],
  "La necropsia de 15.219 cabras mostró que la infección cayó del 53% al 1% tras vacunar a unas 131.000.", "Del 53% al 1%.")),
("4002570", "expert", 2, "infection occurred almost exclusively in goats which for some reason or other had not been vaccinated or which had been too old when vaccinated",
 ("In Norway's paratuberculosis vaccination program, which goats still became infected?", ["Mostly kids vaccinated at 2–4 weeks", "Mostly goats given two vaccine doses", "Unvaccinated or late-vaccinated goats", "Mostly bucks used for breeding"],
  "Infection was almost confined to goats that missed vaccination or received it too late; kids were vaccinated at 2–4 weeks of age.", "Unvaccinated or late."),
 ("En el programa noruego de vacunación contra la paratuberculosis, ¿qué cabras seguían infectándose?", ["Sobre todo cabritos vacunados a las 2–4 semanas", "Sobre todo cabras con dos dosis de vacuna", "Las no vacunadas o vacunadas ya mayores", "Sobre todo machos reproductores"],
  "La infección se limitó casi a cabras sin vacunar o vacunadas tarde; los cabritos se vacunaban a las 2–4 semanas.", "No vacunadas o tardías.")),

# --- CCPP review (30929577)
("30929577", "beginner", 3, "CCPP is not a zoonotic disease",
 ("Can people catch contagious caprine pleuropneumonia (CCPP) from goats?", ["Yes, by drinking raw goat milk", "Yes, through tick bites", "Yes, by inhaling barn dust", "No, it is not zoonotic"],
  "CCPP, caused by Mycoplasma capricolum subsp. capripneumoniae, affects goats but is not a zoonosis.", "No."),
 ("¿Pueden las personas contagiarse de pleuroneumonía contagiosa caprina (PNCC) a partir de cabras?", ["Sí, al tomar leche cruda", "Sí, por garrapatas", "Sí, al inhalar polvo", "No, no es una zoonosis"],
  "La PNCC, causada por Mycoplasma capricolum subsp. capripneumoniae, afecta a las cabras pero no es una zoonosis.", "No.")),
("30929577", "explorer", 0, "The latex agglutination test (LAT) is rapid, simple, and better test for field and real-time diagnosis",
 ("Which test does a comprehensive review recommend as rapid and simple for field diagnosis of CCPP?", ["Latex agglutination test", "Complement fixation test", "Mycoplasma culture alone", "Intradermal tuberculin test"],
  "LAT works on whole blood or serum, is more sensitive than CFT and easier than cELISA.", "Latex agglutination."),
 ("¿Qué prueba recomienda una revisión como rápida y simple para el diagnóstico de campo de la PNCC?", ["Aglutinación en látex", "Fijación del complemento", "Solo cultivo de micoplasmas", "Tuberculina intradérmica"],
  "La aglutinación en látex funciona con sangre entera o suero, es más sensible que la FC y más sencilla que el cELISA.", "Aglutinación en látex.")),

# --- CCPP in Qatar wildlife (17469281)
("17469281", "researcher", 1, "The preferred samples for diagnosis are the pleural fluid, which contains high numbers of Mycoplasma",
 ("After a CCPP outbreak in captive wild ungulates in Qatar, which sample was recommended as preferred for diagnosis?", ["Rectal swabs", "Pleural fluid", "Nasal hair", "Milk samples"],
  "Pleural fluid holds high numbers of mycoplasmas; hepatized lung at the lesion border is also useful.", "Pleural fluid."),
 ("Tras un brote de PNCC en ungulados silvestres en cautiverio en Qatar, ¿qué muestra se recomendó como preferida para el diagnóstico?", ["Hisopados rectales", "Líquido pleural", "Pelo nasal", "Muestras de leche"],
  "El líquido pleural contiene muchos micoplasmas; el pulmón hepatizado en el borde de la lesión también sirve.", "Líquido pleural.")),

# --- Contagious agalactia vaccine (7502465)
("7502465", "researcher", 2, "It is recommended that three doses of vaccine should be administered before, and one dose after each parturition",
 ("To control endemic contagious agalactia due to Mycoplasma agalactiae in a goat herd, which inactivated-vaccine schedule was recommended?", ["A single dose at weaning only", "One dose before kidding only", "Three doses pre-, one post-kidding", "Monthly doses throughout lactation"],
  "The schedule with more prepartum doses gave higher antibody titres and less mycoplasma shedding; herd isolation was also advised.", "Pre- and post-kidding doses."),
 ("Para controlar la agalaxia contagiosa endémica por Mycoplasma agalactiae en cabras, ¿qué esquema de vacuna inactivada se recomendó?", ["Una sola dosis al momento del destete", "Una dosis solo antes del parto", "Tres dosis preparto y una posparto", "Dosis mensuales en toda la lactancia"],
  "El esquema con más dosis preparto dio títulos mayores y menos excreción de micoplasmas; también se aconsejó aislar el rebaño.", "Dosis pre y posparto.")),

# --- Contagious agalactia genital lesions (14720185)
("14720185", "expert", 3, "M. putrefaciens was the only agent isolated from the genital lesions reported here",
 ("In a Spanish goat outbreak of contagious agalactia caused by two mycoplasmas, which one was isolated from the genital lesions?", ["Mycoplasma agalactiae", "Mycoplasma bovis", "Mycoplasma ovipneumoniae", "Mycoplasma putrefaciens"],
  "Only M. putrefaciens was found in genital lesions such as salpingitis, metritis and testicular degeneration.", "M. putrefaciens."),
 ("En un brote de agalaxia contagiosa caprina en España causado por dos micoplasmas, ¿cuál se aisló de las lesiones genitales?", ["Mycoplasma agalactiae", "Mycoplasma bovis", "Mycoplasma ovipneumoniae", "Mycoplasma putrefaciens"],
  "Solo M. putrefaciens se halló en lesiones genitales como salpingitis, metritis y degeneración testicular.", "M. putrefaciens.")),

# --- Mannheimia mastitis outbreak (27374911)
("27374911", "explorer", 0, "M. haemolytica was isolated from 80% of the samples that yielded cultivable microorganisms",
 ("In a clinical mastitis outbreak in Australian ewes during drought, which pathogen dominated the milk cultures?", ["Mannheimia haemolytica", "Streptococcus uberis", "Escherichia coli", "Mycoplasma agalactiae"],
  "M. haemolytica made up 80% of culture-positive samples, making it the main cause of the outbreak.", "M. haemolytica."),
 ("En un brote de mastitis clínica en ovejas australianas durante una sequía, ¿qué patógeno dominó los cultivos de leche?", ["Mannheimia haemolytica", "Streptococcus uberis", "Escherichia coli", "Mycoplasma agalactiae"],
  "M. haemolytica representó el 80% de las muestras con cultivo positivo y fue la causa principal del brote.", "M. haemolytica.")),
("27374911", "researcher", 1, "particularly during adverse climatic conditions and increased stocking rate",
 ("According to an Australian outbreak study, when is Mannheimia haemolytica mastitis especially important in sheep?", ["Only in housed dairy ewes in winter", "In drought and high stocking rates", "Only in flocks vaccinated for orf", "Mainly in rams kept with ewes"],
  "The outbreak occurred during drought, and authors stressed adverse climate and higher stocking rates.", "Drought, crowding."),
 ("Según un estudio de brote en Australia, ¿cuándo es especialmente importante la mastitis por Mannheimia haemolytica en ovejas?", ["Solo en ovejas lecheras estabuladas en invierno", "En sequía y con alta carga animal", "Solo en majadas vacunadas contra ectima", "Sobre todo en carneros junto a ovejas"],
  "El brote ocurrió en sequía, y los autores destacaron el clima adverso y la mayor carga animal.", "Sequía y hacinamiento.")),

# --- LukM leukotoxin (12626454)
("12626454", "expert", 2, "LukM/LukF'-PV is very active on PMN of ruminants and suggest that this leukotoxin could be the most active leukotoxin produced by mastitis isolates",
 ("Which Staphylococcus aureus toxin was proposed as the most active leukotoxin of mastitis isolates from cows, ewes and goats?", ["Panton-Valentine leukocidin", "Alpha-hemolysin", "LukM/LukF'-PV", "Toxic shock toxin-1"],
  "LukM/LukF'-PV strongly killed ruminant neutrophils, and lukM-positive isolates were far more leukotoxic.", "LukM/LukF'-PV."),
 ("¿Qué toxina de Staphylococcus aureus se propuso como la leucotoxina más activa de aislamientos de mastitis de vacas, ovejas y cabras?", ["Leucocidina de Panton-Valentine", "Alfa-hemolisina", "LukM/LukF'-PV", "Toxina del shock tóxico 1"],
  "LukM/LukF'-PV destruyó con fuerza los neutrófilos de rumiantes, y los aislamientos lukM positivos eran mucho más leucotóxicos.", "LukM/LukF'-PV.")),

# --- S. aureus gangrenous mastitis in ewes (22609990)
("22609990", "researcher", 3, "S. aureus isolates from gangrenous mastitis were mainly resistant to penicillins",
 ("Staphylococcus aureus from gangrenous mastitis of ewes in Turkey were mainly resistant to which drugs?", ["Vancomycin", "Tetracyclines", "Fluoroquinolones", "Penicillins"],
  "About a quarter resisted penicillin G or ampicillin (often blaZ-positive); all were oxacillin-susceptible and all formed biofilm.", "Penicillins."),
 ("Los Staphylococcus aureus de mastitis gangrenosa de ovejas en Turquía eran resistentes sobre todo a, ¿qué fármacos?", ["Vancomicina", "Tetraciclinas", "Fluoroquinolonas", "Penicilinas"],
  "Cerca de un cuarto resistía penicilina G o ampicilina (a menudo con blaZ); todos eran sensibles a oxacilina y formaban biopelícula.", "Penicilinas.")),

# --- Listeriosis in 67 sheep and goats (11829065)
("11829065", "beginner", 0, "vestibular ataxia, circling, head tilt and unilateral cranial nerve deficits",
 ("Which clinical signs are typical of listeriosis in sheep and goats?", ["Circling, head tilt and facial palsy", "Lumpy crusts on the wool of the back", "Swollen lymph nodes full of green pus", "Bloody diarrhea with sudden death"],
  "Listerial encephalitis causes vestibular ataxia, circling, head tilt and one-sided cranial nerve deficits.", "Circling, head tilt."),
 ("¿Qué signos clínicos son típicos de la listeriosis en ovinos y caprinos?", ["Marcha en círculos y cabeza ladeada", "Costras gruesas en la lana del lomo", "Ganglios hinchados con pus verdoso", "Diarrea con sangre y muerte súbita"],
  "La encefalitis por Listeria causa ataxia vestibular, marcha en círculos, cabeza ladeada y déficits de pares craneales de un lado.", "Círculos, cabeza ladeada.")),
("11829065", "expert", 1, "of nine animals treated with gentamicin and ampicillin, six survived",
 ("In 67 sheep and goats with listeriosis, which antibiotic treatment had the best survival?", ["Chloramphenicol alone", "Gentamicin + ampicillin", "Oxytetracycline alone", "Penicillin plus dexamethasone"],
  "Six of nine survived with gentamicin plus ampicillin, versus 1 of 15 with chloramphenicol and 2 of 11 with oxytetracycline.", "Gentamicin + ampicillin."),
 ("En 67 ovinos y caprinos con listeriosis, ¿qué tratamiento antibiótico tuvo mejor supervivencia?", ["Cloranfenicol solo", "Gentamicina + ampicilina", "Oxitetraciclina sola", "Penicilina más dexametasona"],
  "Seis de nueve sobrevivieron con gentamicina más ampicilina, frente a 1 de 15 con cloranfenicol y 2 de 11 con oxitetraciclina.", "Gentamicina + ampicilina.")),

# --- Listeriosis epizootic New York (9215449)
("9215449", "explorer", 2, "Corn silage was implicated as the source of a listeriosis epizootic",
 ("What was the source of a listeriosis epizootic in a New York sheep flock, even though the sheep were not fed it?", ["Imported rams", "Drinking water", "Corn silage", "Bird droppings"],
  "Ribotyping matched brain isolates to corn silage that cross-contaminated the sheep's haylage via a front-end loader.", "Corn silage."),
 ("¿Cuál fue la fuente de una epizootia de listeriosis en una majada de Nueva York, aunque las ovejas no la comían?", ["Carneros importados", "Agua de bebida", "Silaje de maíz", "Heces de aves"],
  "La ribotipificación vinculó los aislamientos cerebrales al silaje de maíz, que contaminó el henolaje de las ovejas por una pala cargadora.", "Silaje de maíz.")),

# --- Dermatophilosis and dipping (571715)
("571715", "researcher", 3, "sheep which had been dipped had more lesions and produced less wool than undipped sheep",
 ("In a trial on Merino sheep, how did dipping affect dermatophilosis (lumpy wool)?", ["It prevented all new lesions", "It had no measurable effect at all", "It only affected the young lambs", "More lesions and less wool"],
  "Dipped sheep had more lesions and lower wool production; arsenic dips seemed to aid healing, water or diazinon did not.", "More lesions."),
 ("En un ensayo con ovejas Merino, ¿cómo afectó el baño de inmersión a la dermatofilosis (lana en terrones)?", ["Evitó todas las lesiones nuevas", "No tuvo efecto medible", "Solo afectó a los corderos", "Causó más lesiones y menos lana"],
  "Las ovejas bañadas tuvieron más lesiones y menos lana; los baños con arsénico parecieron ayudar a sanar, los de agua o diazinón no.", "Más lesiones.")),

# --- Fleece rot and dermatophilosis review (18055136)
("18055136", "beginner", 0, "Fleece rot and dermatophilosis reduce health and production of sheep and predispose them to blow fly strike",
 ("Besides lowering production, what do fleece rot and dermatophilosis predispose sheep to?", ["Blowfly strike", "Bloat", "Pregnancy toxemia", "Foot-and-mouth disease"],
  "These bacterial skin diseases damage the fleece and attract blowflies, raising the risk of fly strike.", "Blowfly strike."),
 ("Además de bajar la producción, ¿a qué predisponen a las ovejas la podredumbre del vellón y la dermatofilosis?", ["A la miasis por moscas", "Al timpanismo", "A la toxemia de la preñez", "A la fiebre aftosa"],
  "Estas enfermedades bacterianas de la piel dañan el vellón y atraen moscas, lo que aumenta el riesgo de miasis.", "Miasis.")),
("18055136", "expert", 1, "prototype antibacterial vaccines have to date failed to provide protection against the diversity of isolates of Dermatophilus congolensis",
 ("Why have prototype vaccines against Dermatophilus congolensis in sheep failed so far?", ["The bacterium cannot be grown in the lab", "Field isolates are too diverse", "Sheep make no antibodies to it", "The disease is viral, not bacterial"],
  "Vaccines have not protected against the diversity of D. congolensis and Pseudomonas isolates in the field.", "Isolate diversity."),
 ("¿Por qué han fallado hasta ahora las vacunas prototipo contra Dermatophilus congolensis en ovejas?", ["No puede cultivarse en laboratorio", "Las cepas de campo son muy diversas", "Las ovejas no forman anticuerpos", "La enfermedad es viral, no bacteriana"],
  "Las vacunas no protegieron frente a la diversidad de aislamientos de D. congolensis y Pseudomonas en el campo.", "Diversidad de cepas.")),

# --- Anthrax diagnosis in sheep (16869902)
("16869902", "explorer", 2, "PCR provided the most reliable means for the detection of Bacillus anthracis in deteriorating blood samples",
 ("Which method most reliably detected Bacillus anthracis in deteriorating blood samples from sheep and cattle?", ["Smear", "Culture", "PCR assay", "Urine test"],
  "Multiplex PCR worked even on 15–17-day-old samples and on blood smears stored for 6 years.", "PCR."),
 ("¿Qué método detectó con más fiabilidad Bacillus anthracis en muestras de sangre deterioradas de ovinos y bovinos?", ["Frotis al microscopio", "Cultivo en agar", "Ensayo de PCR", "Gram de orina"],
  "La PCR múltiple funcionó incluso con muestras de 15–17 días y con frotis guardados 6 años.", "PCR.")),
("16869902", "researcher", 3, "the examination of blood smears (2-6 days) for encapsulated bacilli",
 ("In anthrax diagnosis from sheep and cattle blood, what is looked for when examining blood smears?", ["Spores inside red cells", "Gram-negative curved rods", "Acid-fast short rods", "Encapsulated bacilli"],
  "Smears are examined for capsulated bacilli, but this was reliable only for 2–6 days as samples deteriorated.", "Capsulated bacilli."),
 ("En el diagnóstico de carbunco a partir de sangre de ovinos y bovinos, ¿qué se busca al examinar los frotis?", ["Esporas en eritrocitos", "Bacilos gramnegativos", "Bacilos ácido-resistentes", "Bacilos con cápsula"],
  "En los frotis se buscan bacilos capsulados, pero solo fue fiable entre 2 y 6 días al deteriorarse las muestras.", "Bacilos capsulados.")),
]
