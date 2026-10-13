# Veterinary science X — bacterial diseases of cattle: brucellosis vaccines (S19/RB51), Johne's disease,
# bovine genital campylobacteriosis, blackleg and botulism, Histophilus somni, shipping fever (Mannheimia,
# Pasteurella), pinkeye (Moraxella bovis), Salmonella Dublin, Trueperella pyogenes, anaplasmosis,
# actinobacillosis and lumpy jaw, Leptospira hardjo, listeriosis, contagious bovine pleuropneumonia.
# Sources: PubMed original papers and reviews (abstracts). Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- RB51 review: myths and facts (37853407)
("37853407", "beginner", 0, "Cattle brucellosis is a severe zoonosis of worldwide distribution caused by Brucella abortus and B. melitensis",
 ("Which bacteria cause cattle brucellosis, a severe zoonosis found worldwide?", ["Brucella abortus and B. melitensis", "Leptospira hardjo and L. pomona", "Clostridium chauvoei and C. septicum", "Listeria and Salmonella species"],
  "Cattle brucellosis is caused mainly by B. abortus, and also by B. melitensis when cattle live with small ruminants.", "Brucella species."),
 ("¿Qué bacterias causan la brucelosis bovina, una zoonosis grave presente en todo el mundo?", ["Brucella abortus y B. melitensis", "Leptospira hardjo y L. pomona", "Clostridium chauvoei y C. septicum", "Especies de Listeria y Salmonella"],
  "La brucelosis bovina la causa sobre todo B. abortus, y también B. melitensis cuando el ganado convive con pequeños rumiantes.", "Especies de Brucella.")),
("37853407", "researcher", 1, "data acumulated during cattle brucellosis eradication in Spain shows that S19-T/S is far more efficacious than RB51-T/S",
 ("According to a critical review of RB51, which strategy worked best during cattle brucellosis eradication in Spain?", ["RB51 vaccine plus test-and-slaughter", "S19 vaccine plus test-and-slaughter", "Test-and-slaughter with no vaccine", "Mass antibiotic treatment of herds"],
  "Spanish eradication data showed S19 with test-and-slaughter far outperformed RB51, which did no better than test-and-slaughter alone.", "S19 + test-and-slaughter."),
 ("Según una revisión crítica de la RB51, ¿qué estrategia funcionó mejor en la erradicación de la brucelosis bovina en España?", ["Vacuna RB51 más prueba y sacrificio", "Vacuna S19 más prueba y sacrificio", "Prueba y sacrificio sin vacunar", "Tratamiento antibiótico masivo del rodeo"],
  "Los datos de España mostraron que S19 con prueba y sacrificio superó con creces a RB51, que no fue mejor que la prueba y sacrificio sola.", "S19 + prueba y sacrificio.")),

# --- S19 vs RB51 meta-analysis (34328699)
("34328699", "researcher", 2, "the S19 vaccine at 109 CFU exhibited the highest protection rate",
 ("In a meta-analysis of Brucella abortus vaccine trials, which vaccine and dose gave the highest protection against abortion?", ["RB51 at 10^9 CFU", "RB51 at 10^10 CFU", "S19 at 10^9 CFU", "S19 at 10^7 CFU"],
  "S19 at 10^9 CFU had a vaccine efficacy of about 75% against abortion, followed by RB51 at 10^10 CFU (about 69%).", "S19 at 10^9 CFU."),
 ("En un metaanálisis de ensayos de vacunas contra Brucella abortus, ¿qué vacuna y dosis dio la mayor protección contra el aborto?", ["RB51 a 10^9 UFC", "RB51 a 10^10 UFC", "S19 a 10^9 UFC", "S19 a 10^7 UFC"],
  "La S19 a 10^9 UFC tuvo una eficacia de cerca del 75% contra el aborto, seguida por la RB51 a 10^10 UFC (cerca del 69%).", "S19 a 10^9 UFC.")),

# --- RB51 abortions in Wyoming (23942901)
("23942901", "explorer", 3, "Reproductive losses in the vaccinated herds were 5.3% (herd A) and 0.6% (herd B) and included abortions, stillbirths, premature calves",
 ("What happened when two herds of pregnant adult cattle in Wyoming were vaccinated with Brucella abortus RB51?", ["No reproductive effects were seen", "Only a short, mild fever appeared", "The bulls of both herds became infertile", "Some cows aborted or calved early"],
  "Losses of 5.3% and 0.6% included abortions and premature calves, and the RB51 vaccine strain was cultured from fetuses.", "Abortions, premature calves."),
 ("¿Qué ocurrió cuando dos rodeos de vacas adultas preñadas en Wyoming se vacunaron con Brucella abortus RB51?", ["No hubo efectos reproductivos", "Solo hubo una fiebre leve y breve", "Los toros de ambos rodeos quedaron infértiles", "Algunas vacas abortaron o parieron antes"],
  "Las pérdidas de 5,3% y 0,6% incluyeron abortos y terneros prematuros, y se cultivó la cepa vacunal RB51 de los fetos.", "Abortos y partos prematuros.")),

# --- MAP transmission to calves, systematic review (22211394)
("22211394", "beginner", 0, "The contact of calves with adult cow feces is the most important risk factor in MAP transmission",
 ("What is the most important risk factor for transmission of Johne's disease (MAP) to dairy calves?", ["Contact with adult cow feces", "Drinking from troughs with sheep", "Insect bites in the summer", "Sharing needles at vaccination"],
  "A systematic review found that calves' contact with adult cow manure is the key route of MAP infection.", "Adult cow feces."),
 ("¿Cuál es el factor de riesgo más importante para que los terneros lecheros se contagien de paratuberculosis (MAP)?", ["Contacto con heces de vacas adultas", "Beber en bebederos compartidos con ovejas", "Picaduras de insectos en verano", "Compartir agujas al vacunar"],
  "Una revisión sistemática halló que el contacto de los terneros con estiércol de vacas adultas es la vía clave de infección.", "Heces de vacas adultas.")),

# --- ELISA vs fecal culture for Johne's (11118724)
("11118724", "researcher", 1, "ELISA has a higher sensitivity in animals with a heavier bacterial load, i.e. high shedders (75%) compared to low shedders (15%)",
 ("For paratuberculosis in dairy cattle, how did serum ELISA sensitivity compare between high and low fecal shedders?", ["About 15% vs 75%", "About 75% vs 15%", "About 50% in both", "About 95% vs 90%"],
  "ELISA detects heavy shedders far better than light shedders, so it misses many early or low-level infections.", "75% vs 15%."),
 ("En la paratuberculosis del ganado lechero, ¿cómo fue la sensibilidad del ELISA en excretores altos frente a bajos?", ["Cerca de 15% vs 75%", "Cerca de 75% vs 15%", "Cerca de 50% en ambos", "Cerca de 95% vs 90%"],
  "El ELISA detecta mucho mejor a los grandes excretores que a los pequeños, por eso pasa por alto muchas infecciones leves.", "75% vs 15%.")),
("11118724", "explorer", 2, "The sensitivity of fecal culture to detect infected cattle on the first sampling was 38%",
 ("In a cohort of 954 cattle tested every 6 months, what was the sensitivity of the first fecal culture for Johne's disease?", ["About 98%", "About 80%", "About 38%", "About 5%"],
  "Only 38% of the cattle eventually found culture-positive were detected at the first sampling; repeated testing found many more.", "About 38%."),
 ("En una cohorte de 954 bovinos muestreados cada 6 meses, ¿qué sensibilidad tuvo el primer cultivo fecal para paratuberculosis?", ["Cerca de 98%", "Cerca de 80%", "Cerca de 38%", "Cerca de 5%"],
  "Solo el 38% de los bovinos luego positivos al cultivo se detectó en el primer muestreo; los muestreos repetidos hallaron muchos más.", "Cerca de 38%.")),

# --- Calf-to-calf MAP transmission (31429807)
("31429807", "expert", 3, "transmission among calves may be an important cause of persistent MAP infection on dairy farms",
 ("What did an experimental trial with group-housed Holstein calves conclude about Mycobacterium avium subsp. paratuberculosis?", ["Young calves are fully resistant to MAP", "MAP spreads only through colostrum", "Only adult cows can shed MAP", "MAP spreads between penmate calves"],
  "Contact-exposed penmates became infected, so calf-to-calf spread is a route current control programs ignore.", "Calf-to-calf spread."),
 ("¿Qué concluyó un ensayo con terneros Holstein alojados en grupo sobre Mycobacterium avium subsp. paratuberculosis?", ["Los terneros jóvenes son totalmente resistentes", "MAP se transmite solo por el calostro", "Solo las vacas adultas excretan MAP", "MAP se contagia entre terneros del corral"],
  "Los compañeros de corral expuestos se infectaron, así que el contagio entre terneros es una vía que los programas actuales ignoran.", "Contagio entre terneros.")),

# --- Genital campylobacteriosis in Spanish bulls (34957276)
("34957276", "beginner", 0, "Bovine genital campylobacteriosis (BGC) is a sexually transmitted disease that causes early reproductive failure",
 ("What kind of disease is bovine genital campylobacteriosis, caused by Campylobacter fetus venerealis?", ["A sexually transmitted disease", "A tick-borne blood disease", "A respiratory disease of calves", "A foodborne disease of feedlots"],
  "BGC spreads during natural breeding and causes early reproductive failure in extensively managed herds.", "Venereal disease."),
 ("¿Qué tipo de enfermedad es la campilobacteriosis genital bovina, causada por Campylobacter fetus venerealis?", ["Una enfermedad de transmisión sexual", "Una enfermedad de la sangre por garrapatas", "Una enfermedad respiratoria de terneros", "Una enfermedad alimentaria de feedlots"],
  "La campilobacteriosis genital se contagia en el servicio natural y causa fallas reproductivas tempranas en rodeos extensivos.", "Enfermedad venérea.")),
("34957276", "researcher", 1, "Infection was detected by PCR in 7.7 and 12.2% of the bulls and herds tested",
 ("In Spanish beef breeding bulls tested from 2011 to 2019, what share was PCR-positive for Campylobacter fetus venerealis?", ["About 45% of bulls", "About 7.7% of bulls", "About 0.1% of bulls", "About 25% of bulls"],
  "7.7% of 5,182 bulls and 12.2% of herds were positive, showing the disease is endemic in Spain.", "About 7.7%."),
 ("En toros reproductores de carne de España analizados entre 2011 y 2019, ¿qué proporción fue PCR positiva a Campylobacter fetus venerealis?", ["Cerca del 45% de los toros", "Cerca del 7,7% de los toros", "Cerca del 0,1% de los toros", "Cerca del 25% de los toros"],
  "El 7,7% de 5182 toros y el 12,2% de los rodeos fueron positivos, lo que muestra que la enfermedad es endémica en España.", "Cerca del 7,7%.")),

# --- Cfv PCR false positives (33121492)
("33121492", "expert", 2, "PCR assays solely directed to a subspecies target originate a high rate of false positive results",
 ("What problem did a study of 308 bull preputial samples find with PCR assays targeting only Campylobacter fetus venerealis genes?", ["They missed most true infections", "They needed live, viable bacteria", "They gave many false positives", "They cross-reacted with Brucella"],
  "ISCfe1 and parA homologues in other species such as C. portucalensis gave false positives, so species targets should be added.", "False positives."),
 ("¿Qué problema halló un estudio de 308 muestras prepuciales de toros con PCR dirigidas solo a genes de Campylobacter fetus venerealis?", ["No detectaban la mayoría de las infecciones", "Necesitaban bacterias vivas y viables", "Daban muchos falsos positivos", "Daban reacción cruzada con Brucella"],
  "Homólogos de ISCfe1 y parA en otras especies como C. portucalensis dieron falsos positivos; conviene sumar dianas de especie.", "Falsos positivos.")),

# --- La Pampa venereal eradication program (38441747)
("38441747", "researcher", 3, "The outcomes refute the notion that this program of venereal eradication was a success",
 ("What did a 2008-2021 analysis conclude about La Pampa's program to eradicate campylobacteriosis and trichomonosis by culling positive bulls?", ["It eradicated both diseases by 2015", "It eliminated trichomonosis only", "It was replaced by mass vaccination", "The data refuted its claimed success"],
  "The authors found the program was not a success and that many false positives led to culling healthy bulls.", "Not a success."),
 ("¿Qué concluyó un análisis 2008-2021 del programa de La Pampa para erradicar campilobacteriosis y tricomonosis sacrificando toros positivos?", ["Erradicó ambas enfermedades en 2015", "Eliminó solo la tricomonosis", "Se reemplazó por vacunación masiva", "Los datos refutaron su supuesto éxito"],
  "Los autores vieron que el programa no fue un éxito y que muchos falsos positivos llevaron a sacrificar toros sanos.", "No fue un éxito.")),

# --- Blackleg outbreak in Pakistan (32074087)
("32074087", "beginner", 0, "Clostridium chauvoei (C. chauvoei) is an anaerobic, histotoxic Gram-positive, bacterium causing fatal myonecrosis",
 ("What kind of lesion does Clostridium chauvoei, the cause of blackleg, produce in livestock?", ["Fatal muscle necrosis", "Benign skin warts", "Chronic cracks in the hooves", "A mild eye infection"],
  "C. chauvoei is an anaerobic, histotoxic bacterium that causes fatal myonecrosis with high mortality.", "Muscle necrosis."),
 ("¿Qué tipo de lesión produce Clostridium chauvoei, causante de la mancha (carbunclo sintomático), en el ganado?", ["Necrosis muscular mortal", "Verrugas benignas en la piel", "Grietas crónicas en las pezuñas", "Una infección ocular leve"],
  "C. chauvoei es una bacteria anaerobia e histotóxica que causa mionecrosis mortal con alta mortalidad.", "Necrosis muscular.")),
("32074087", "explorer", 1, "The muscles were swollen, dark to black and exhibited crepitation sounds at the time of incisions with a rancid odor",
 ("At necropsy during a blackleg outbreak in Punjab, Pakistan, how did the affected muscles look?", ["Pale, dry and calcified", "Dark to black and crepitant", "Bright red but otherwise normal", "Shrunken with white streaks"],
  "Swollen, dark muscle with gas crepitation and a rancid smell is the classic blackleg lesion.", "Dark and crepitant."),
 ("En la necropsia de un brote de mancha en Punyab, Pakistán, ¿cómo se veían los músculos afectados?", ["Pálidos, secos y calcificados", "Oscuros a negros y crepitantes", "Rojo brillante pero normales", "Retraídos con estrías blancas"],
  "El músculo hinchado y oscuro, con crepitación por gas y olor rancio, es la lesión clásica de la mancha.", "Oscuros y crepitantes.")),

# --- Blackleg costs in Laos (30779313)
("30779313", "researcher", 2, "being 122% of their annual household income from large ruminant sales",
 ("In a 2017 blackleg outbreak in Laos, how large were losses per affected household relative to its yearly income from cattle and buffalo sales?", ["About 12%", "About 2%", "About 122%", "About 250%"],
  "Mean losses of about USD 822 per household exceeded a full year of livestock sales income, favoring vaccination.", "About 122%."),
 ("En un brote de mancha en Laos en 2017, ¿cuánto representaron las pérdidas por hogar afectado frente a su ingreso anual por venta de bovinos y búfalos?", ["Cerca del 12%", "Cerca del 2%", "Cerca del 122%", "Cerca del 50%"],
  "Las pérdidas medias de unos 822 USD por hogar superaron un año entero de ingresos por venta de ganado, lo que favorece vacunar.", "Cerca del 122%.")),

# --- Type C botulism in feedlot (30408576)
("30408576", "explorer", 3, "A total of 1100 steers were affected, 1090 of which died within four days",
 ("In a Brazilian feedlot outbreak of type C botulism from contaminated corn silage, what happened to the affected steers?", ["Most recovered with antibiotics", "Few were affected and none died", "Only young calves were affected", "Nearly all of them died quickly"],
  "Of 1,100 affected steers, 1,090 died within four days; only ten recovered after antitoxin.", "Almost all died."),
 ("En un brote de botulismo tipo C en un feedlot de Brasil por silaje de maíz contaminado, ¿qué pasó con los novillos afectados?", ["La mayoría se curó con antibióticos", "Pocos enfermaron y ninguno murió", "Solo enfermaron terneros jóvenes", "Casi todos murieron rápidamente"],
  "De 1100 novillos afectados, 1090 murieron en cuatro días; solo diez se recuperaron con antitoxina.", "Casi todos murieron.")),

# --- Histophilus somni myocarditis (19429974)
("19429974", "researcher", 0, "Histologically, the lesion corresponded to acute necrotizing myocarditis with myriad intravascular and intralesional gram-negative coccobacilli",
 ("In backgrounded calves in Wyoming dying of fever and lethargy, what did the red focus in the left ventricular papillary muscle turn out to be?", ["Acute necrotizing myocarditis", "Chronic fibrosing endocarditis", "A benign cardiac lipoma", "A congenital septal defect"],
  "The lesion was necrotizing myocarditis full of gram-negative coccobacilli, identified as Histophilus somni.", "H. somni myocarditis."),
 ("En terneros de recría en Wyoming que morían con fiebre y letargo, ¿qué resultó ser el foco rojo en el músculo papilar del ventrículo izquierdo?", ["Miocarditis necrotizante aguda", "Endocarditis fibrosante crónica", "Un lipoma cardíaco benigno", "Un defecto septal congénito"],
  "La lesión era una miocarditis necrotizante llena de cocobacilos gramnegativos, identificados como Histophilus somni.", "Miocarditis por H. somni.")),

# --- H. somni susceptibility in Australia (35640408)
("35640408", "explorer", 1, "None of the 70 Australian H. somni isolates exhibited resistance to antimicrobials with CLSI breakpoints",
 ("How much antimicrobial resistance was found among 70 Histophilus somni isolates from Australian feedlot cattle?", ["Most resisted tulathromycin", "None was resistant", "All resisted tetracyclines", "Half resisted ceftiofur"],
  "No isolate was resistant to drugs with CLSI breakpoints, including first-line tetracyclines.", "None."),
 ("¿Cuánta resistencia antimicrobiana se halló en 70 aislamientos de Histophilus somni de bovinos de feedlot en Australia?", ["La mayoría resistía tulatromicina", "Ninguno era resistente", "Todos resistían tetraciclinas", "La mitad resistía ceftiofur"],
  "Ningún aislamiento fue resistente a los fármacos con puntos de corte CLSI, incluidas las tetraciclinas de primera línea.", "Ninguna.")),

# --- Mannheimia haemolytica in feedlots (25818224)
("25818224", "researcher", 2, "Most isolates were pan-susceptible (87.8%",
 ("Among Mannheimia haemolytica isolates from 5,498 cattle in four feedlots, what share was susceptible to all antimicrobials tested?", ["About 12%", "About 30%", "About 88%", "About 50%"],
  "Most isolates were pan-susceptible and multiply-resistant ones were rare (5.9%).", "About 88%."),
 ("Entre los aislamientos de Mannheimia haemolytica de 5498 bovinos de cuatro feedlots, ¿qué proporción fue sensible a todos los antimicrobianos?", ["Cerca del 12%", "Cerca del 30%", "Cerca del 88%", "Cerca del 50%"],
  "La mayoría de los aislamientos fue pansensible y los multirresistentes fueron raros (5,9%).", "Cerca del 88%.")),

# --- M. bovis and M. haemolytica in BRD (35979489)
("35979489", "beginner", 3, "Mannheimia haemolytica is widely regarded as the primary bacterial pathogen driving acute BRD",
 ("Which bacterium is widely regarded as the primary cause of acute bovine respiratory disease (shipping fever) in feedlot cattle?", ["Moraxella bovis", "Clostridium chauvoei", "Listeria monocytogenes", "Mannheimia haemolytica"],
  "M. haemolytica is considered the main bacterial driver of acute BRD, often after viral or stress triggers.", "M. haemolytica."),
 ("¿Qué bacteria se considera la causa principal de la enfermedad respiratoria bovina aguda (fiebre del transporte) en feedlots?", ["Moraxella bovis", "Clostridium chauvoei", "Listeria monocytogenes", "Mannheimia haemolytica"],
  "M. haemolytica se considera el principal agente bacteriano de la ERB aguda, a menudo tras virus o estrés.", "M. haemolytica.")),
("35979489", "researcher", 0, "The presence of M. bovis in nasal swabs collected on d7 post-arrival was significantly associated with an increase in the prevalence of M. haemolytica on d28",
 ("In 270 feedlot cattle, what early finding was linked to more Mannheimia haemolytica in nasal swabs on day 28?", ["Mycoplasma bovis on day 7", "BRSV vaccination at arrival", "A heavier weight at arrival", "Histophilus somni on arrival"],
  "M. bovis on day 7 raised M. haemolytica prevalence on day 28 by about 45 percentage points.", "M. bovis on day 7."),
 ("En 270 bovinos de feedlot, ¿qué hallazgo temprano se asoció con más Mannheimia haemolytica en hisopados nasales al día 28?", ["Mycoplasma bovis al día 7", "Vacunar contra BRSV al ingreso", "Mayor peso al ingreso", "Histophilus somni al ingreso"],
  "M. bovis al día 7 aumentó la prevalencia de M. haemolytica al día 28 en unos 45 puntos porcentuales.", "M. bovis al día 7.")),

# --- Pasteurella multocida aerosol pneumonia (2990648)
("2990648", "researcher", 1, "Two groups of five calves were exposed to aerosols of one of two types of P. multocida only, which produced lobar pneumonia in one calf of each group",
 ("When calves were exposed to aerosols of Pasteurella multocida alone, without prior bovine herpesvirus 1, how many developed lobar pneumonia?", ["All five calves per group", "One calf in each group", "No calf in either group", "Three calves per group"],
  "P. multocida alone caused pneumonia in only one calf per group; prior BHV-1 exposure gave extensive lesions.", "One per group."),
 ("Cuando se expuso a terneros a aerosoles de Pasteurella multocida sola, sin herpesvirus bovino 1 previo, ¿cuántos desarrollaron neumonía lobar?", ["Los cinco terneros de cada grupo", "Un ternero en cada grupo", "Ninguno en ningún grupo", "Tres terneros por grupo"],
  "P. multocida sola causó neumonía en un solo ternero por grupo; la exposición previa a BHV-1 dio lesiones extensas.", "Uno por grupo.")),

# --- Commercial Moraxella bovis vaccine RCT (28703672)
("28703672", "researcher", 2, "IBK was detected in 65 (59.1%) vaccinated calves and 62 (59.6%) unvaccinated calves",
 ("In a randomized blinded trial in Iowa beef calves, what was the effect of a commercial Moraxella bovis vaccine on pinkeye?", ["It halved pinkeye cases", "It cut pinkeye to under 5%", "About 59% got IBK in both groups", "It added about 30 kg at weaning"],
  "IBK incidence was nearly identical in vaccinated and control calves, and weaning weights did not differ.", "No effect."),
 ("En un ensayo aleatorizado y ciego en terneros de carne de Iowa, ¿qué efecto tuvo una vacuna comercial contra Moraxella bovis sobre la queratoconjuntivitis?", ["Redujo los casos a la mitad", "Bajó los casos a menos del 5% del rodeo", "Cerca del 59% enfermó en ambos grupos", "Sumó unos 30 kg al destete"],
  "La incidencia fue casi idéntica en vacunados y controles, y el peso al destete no difirió.", "Sin efecto.")),

# --- Intranasal cytotoxin vaccine (37693844)
("37693844", "beginner", 3, "Infectious bovine keratoconjunctivitis (IBK; pinkeye) is generally considered to be caused by corneal infections with Moraxella bovis",
 ("Which bacterium is generally considered the cause of pinkeye (infectious bovine keratoconjunctivitis) in cattle?", ["Listeria monocytogenes", "Brucella abortus", "Clostridium chauvoei", "Moraxella bovis"],
  "Pinkeye results from corneal infection with Moraxella bovis.", "Moraxella bovis."),
 ("¿Qué bacteria se considera la causa de la queratoconjuntivitis infecciosa bovina (ojo rosado) en el ganado?", ["Listeria monocytogenes", "Brucella abortus", "Clostridium chauvoei", "Moraxella bovis"],
  "El ojo rosado se debe a la infección de la córnea por Moraxella bovis.", "Moraxella bovis.")),
("37693844", "researcher", 0, "IBK-affected Vaccine group steers had a significantly lower number of observation weeks with severe ulcers",
 ("In a California field trial of an intranasal Moraxella bovis cytotoxin vaccine, what benefit was seen in steers that got pinkeye?", ["Fewer weeks with severe ulcers", "Far fewer steers got pinkeye", "No tear IgA response at all", "Larger and deeper corneal ulcers"],
  "The vaccine did not lower IBK incidence, but affected vaccinated steers had fewer weeks with severe ulcers.", "Milder ulcers."),
 ("En un ensayo de campo en California con una vacuna intranasal de citotoxina de Moraxella bovis, ¿qué beneficio se vio en novillos con ojo rosado?", ["Menos semanas con úlceras graves", "Muchos menos novillos enfermaron", "Ninguna respuesta de IgA en lágrimas", "Úlceras corneales más grandes"],
  "La vacuna no bajó la incidencia, pero los vacunados que enfermaron tuvieron menos semanas con úlceras graves.", "Úlceras más leves.")),

# --- Salmonella Dublin transmission, Denmark (17175050)
("17175050", "researcher", 1, "Across herds the R(0) was close to two",
 ("In four Danish dairy herds endemically infected with Salmonella Dublin, what was the estimated basic reproduction ratio (R0) among calves?", ["About 10", "About 2", "Below 0.5", "About 25"],
  "On average one infectious calf would produce about two new infectious calves in a fully susceptible group.", "About 2."),
 ("En cuatro tambos daneses con infección endémica por Salmonella Dublin, ¿cuál fue el número reproductivo básico (R0) estimado entre terneros?", ["Cerca de 10", "Cercano a 2", "Menor de 0,5", "Cerca de 25"],
  "En promedio, un ternero infeccioso produciría unos dos nuevos terneros infecciosos en un grupo totalmente susceptible.", "Cerca de 2.")),
("17175050", "explorer", 2, "environmental contamination from infectious calves plays an important role in transmitting Salmonella Dublin between calves",
 ("According to a Danish field study, what plays an important role in spreading Salmonella Dublin between young calves?", ["Airborne spread from the adult cows", "Bird droppings in stored feed", "Calves contaminating the environment", "Transmission by flies alone"],
  "Infectious calves contaminate their surroundings, which drives calf-to-calf spread.", "Environmental contamination."),
 ("Según un estudio de campo danés, ¿qué cumple un papel importante en la transmisión de Salmonella Dublin entre terneros?", ["Contagio aéreo desde vacas adultas", "Heces de aves en el alimento", "Terneros que contaminan el ambiente", "Solo la transmisión por moscas"],
  "Los terneros infecciosos contaminan su entorno, lo que impulsa el contagio entre terneros.", "Contaminación ambiental.")),

# --- Salmonella Dublin in crossbred calves (40043766)
("40043766", "researcher", 3, "Salmonella Dublin was associated with increased respiratory disease, though it did not affect growth or incidence of diarrhea",
 ("In 160 crossbred dairy calves at an Ontario calf facility, what was Salmonella Dublin positivity associated with?", ["Slower daily weight gain", "More episodes of diarrhea", "Lower overall mortality", "More respiratory disease"],
  "S. Dublin-positive calves had worse respiratory scores, with no effect on growth or diarrhea.", "Respiratory disease."),
 ("En 160 terneros lecheros cruza de una recría de Ontario, ¿con qué se asoció ser positivo a Salmonella Dublin?", ["Menor ganancia diaria de peso", "Más episodios de diarrea", "Menor mortalidad general", "Más enfermedad respiratoria"],
  "Los terneros positivos tuvieron peores puntajes respiratorios, sin efecto en el crecimiento ni en la diarrea.", "Enfermedad respiratoria.")),

# --- Trueperella pyogenes in metritis (30066209)
("30066209", "beginner", 0, "Trueperella pyogenes is one of the most important microorganisms causing metritis in post-partum cattle",
 ("Trueperella pyogenes is one of the most important causes of which disease in cows after calving?", ["Metritis", "Milk fever", "Displaced abomasum", "Ketosis"],
  "T. pyogenes is a key cause of postpartum uterine infection (metritis), often with E. coli or Fusobacterium.", "Metritis."),
 ("Trueperella pyogenes es una de las causas más importantes de ¿qué enfermedad en vacas después del parto?", ["Metritis", "Fiebre de leche", "Desplazamiento de abomaso", "Cetosis"],
  "T. pyogenes es una causa clave de infección uterina posparto (metritis), a menudo junto con E. coli o Fusobacterium.", "Metritis.")),
("30066209", "researcher", 1, "fimA and plo genes were identified in all tested isolates",
 ("Which virulence genes were found in every Trueperella pyogenes isolate from Iranian cows with clinical metritis?", ["cbpA and fimG", "fimA and plo", "nanH and fimE", "fimC and nanP"],
  "fimA (fimbriae) and plo (pyolysin) were universal, while other genes varied among isolates.", "fimA and plo."),
 ("¿Qué genes de virulencia se hallaron en todos los aislamientos de Trueperella pyogenes de vacas iraníes con metritis clínica?", ["cbpA y fimG", "fimA y plo", "nanH y fimE", "fimC y nanP"],
  "fimA (fimbrias) y plo (piolisina) estaban en todos, mientras que los demás genes variaban.", "fimA y plo.")),

# --- Boophilus transmission of anaplasmosis (8498744)
("8498744", "explorer", 2, "The 1-host tick Boophilus annulatus was found to transmit anaplasmosis in cattle transstadially",
 ("What did a study find about the one-host tick Boophilus annulatus and Anaplasma marginale in cattle?", ["It cannot carry A. marginale", "It transmits only Babesia", "It transmits it transstadially", "It transmits only via its eggs"],
  "Ticks moved from infected to susceptible calves transmitted anaplasmosis across life stages.", "Transstadial transmission."),
 ("¿Qué halló un estudio sobre la garrapata de un hospedador Boophilus annulatus y Anaplasma marginale en bovinos?", ["No puede portar A. marginale", "Solo transmite Babesia", "Lo transmite transestadialmente", "Lo transmite solo por los huevos"],
  "Las garrapatas pasadas de terneros infectados a susceptibles transmitieron la anaplasmosis entre estadios.", "Transmisión transestadial.")),

# --- A. centrale vaccine and field A. marginale (18387757)
("18387757", "researcher", 3, "an animal primarily infected with A. marginale, or with the related vaccine subspecies A. centrale can be infected with the heterologous subspecies, and carries both bacteria",
 ("Can cattle vaccinated with live Anaplasma centrale also become infected with field Anaplasma marginale?", ["No, the vaccine excludes it", "Only if they are splenectomized", "Only five years after vaccination", "Yes, they can carry both"],
  "Cross-infection experiments showed no infection exclusion: calves carried both subspecies at once.", "Yes, both."),
 ("¿Pueden los bovinos vacunados con Anaplasma centrale vivo infectarse también con Anaplasma marginale de campo?", ["No, la vacuna lo excluye", "Solo si están esplenectomizados", "Solo cinco años después de vacunar", "Sí, pueden portar ambos"],
  "Los experimentos de infección cruzada no mostraron exclusión: los terneros portaban ambas subespecies a la vez.", "Sí, ambos.")),

# --- Chemosterilization of carriers (33678368)
("33678368", "researcher", 0, "The results showed 50% efficacy of the OTC treatment to chemosterilize persistent A. marginale infections in cattle and the failure of the IMD treatment",
 ("In Argentina, how well did long-acting oxytetracycline and imidocarb clear persistent Anaplasma marginale infection in carrier steers?", ["OTC cleared 50%; imidocarb failed", "Both drugs cleared every infected steer", "Imidocarb cleared all; OTC failed", "Neither drug had any effect at all"],
  "Three doses of long-acting oxytetracycline sterilized half of the carriers, while imidocarb failed.", "OTC 50%, imidocarb failed."),
 ("En Argentina, ¿qué tan bien eliminaron la oxitetraciclina de larga acción y el imidocarb la infección persistente por Anaplasma marginale en novillos portadores?", ["OTC eliminó 50%; imidocarb falló", "Ambos eliminaron la infección en todos", "Imidocarb eliminó todo; la OTC falló", "Ninguno de los dos tuvo efecto alguno"],
  "Tres dosis de oxitetraciclina de larga acción esterilizaron a la mitad de los portadores, y el imidocarb falló.", "OTC 50%, imidocarb falló.")),

# --- Lymphatic actinobacillosis (29202671)
("29202671", "beginner", 1, "Bovine actinobacillosis is typically characterized by pyogranulomatous glossitis (wooden tongue)",
 ("What is the typical form of actinobacillosis in cattle?", ["Swelling of the hind legs", "Wooden tongue (glossitis)", "Inflammation of the eyes", "Abortion in late pregnancy"],
  "Actinobacillus lignieresii classically causes pyogranulomatous inflammation of the tongue, called wooden tongue.", "Wooden tongue."),
 ("¿Cuál es la forma típica de la actinobacilosis en el ganado bovino?", ["Hinchazón de las patas traseras", "Lengua de palo (glositis)", "Inflamación de los ojos", "Aborto al final de la preñez"],
  "Actinobacillus lignieresii causa clásicamente una inflamación piogranulomatosa de la lengua, llamada lengua de palo.", "Lengua de palo.")),
("29202671", "explorer", 2, "Seven of 8 cows recovered after treatment with sodium iodide",
 ("In outbreaks of lymphatic actinobacillosis in Uruguay, which treatment led to recovery in seven of eight cows?", ["Ivermectin", "Vitamin E", "Sodium iodide", "Tongue surgery"],
  "Sodium iodide, the classic treatment for actinobacillosis, cured most treated cows.", "Sodium iodide."),
 ("En brotes de actinobacilosis linfática en Uruguay, ¿qué tratamiento logró la recuperación de siete de ocho vacas?", ["Inyecciones de ivermectina", "Vitamina E y selenio", "Yoduro de sodio", "Extirpar la lengua"],
  "El yoduro de sodio, tratamiento clásico de la actinobacilosis, curó a la mayoría de las vacas tratadas.", "Yoduro de sodio.")),

# --- Lumpy jaw by Nocardia (38520249)
("38520249", "researcher", 3, "This is the first report of lumpy jaw caused by N. farcinica in a cow",
 ("A 3-year-old Holstein cow had a firm, ulcerated mandibular mass (lumpy jaw). What unusual agent was identified?", ["Actinobacillus lignieresii", "Actinomyces israelii", "Trueperella pyogenes", "Nocardia farcinica"],
  "Lumpy jaw is usually caused by Actinomyces bovis; this was the first bovine case due to Nocardia farcinica.", "Nocardia farcinica."),
 ("Una vaca Holstein de 3 años tenía una masa mandibular firme y ulcerada (actinomicosis o mandíbula abultada). ¿Qué agente inusual se identificó?", ["Actinobacillus lignieresii", "Actinomyces israelii", "Trueperella pyogenes", "Nocardia farcinica"],
  "La mandíbula abultada suele deberse a Actinomyces bovis; este fue el primer caso bovino por Nocardia farcinica.", "Nocardia farcinica.")),

# --- Leptospira hardjo outbreak (7210429)
("7210429", "explorer", 0, "Two milkers subsequently became ill and developed titres to the Hebdomadis serogroup",
 ("During a Leptospira hardjo outbreak with a sudden milk drop in a large dairy herd, what happened to the farm workers?", ["Two milkers became ill", "None showed any antibodies", "All were vaccinated in time", "Only the veterinarian got sick"],
  "Two milkers fell ill and seroconverted, showing that hardjo is a zoonosis for dairy workers.", "Two milkers ill."),
 ("Durante un brote de Leptospira hardjo con caída brusca de leche en un tambo grande, ¿qué pasó con los trabajadores?", ["Dos ordeñadores enfermaron", "Ninguno tuvo anticuerpos", "Todos se vacunaron a tiempo", "Solo enfermó el veterinario"],
  "Dos ordeñadores enfermaron y seroconvirtieron, lo que muestra que hardjo es una zoonosis para quienes ordeñan.", "Dos ordeñadores enfermos.")),

# --- Hardjo seroprevalence in Tanzania (37018175)
("37018175", "researcher", 1, "An overall seroprevalence of 13.0% (95% CI 11.6-14.5%) for Leptospira serovar Hardjo was found",
 ("What overall seroprevalence of Leptospira serovar Hardjo was found in 2,071 smallholder dairy cattle in Tanzania?", ["About 1%", "About 13%", "About 50%", "About 90%"],
  "Seroprevalence was 13% overall, reaching about 30% in the Iringa region.", "About 13%."),
 ("¿Qué seroprevalencia general de Leptospira serovar Hardjo se halló en 2071 vacas lecheras de pequeños productores en Tanzania?", ["Cerca del 1%", "Cerca del 13%", "Cerca del 50%", "Cerca del 90%"],
  "La seroprevalencia fue del 13% en general y llegó a cerca del 30% en la región de Iringa.", "Cerca del 13%.")),

# --- Pentavalent leptospiral vaccines vs hardjo-bovis (2610425)
("2610425", "expert", 2, "All control and all vaccinated steers became infected and shed serovar hardjo type hardjo-bovis in the urine",
 ("In a challenge study of pentavalent leptospiral vaccines containing serovar hardjo, what happened after exposure to hardjo-bovis?", ["No vaccinated steer was infected", "Only the hardjoprajitno vaccine protected", "All steers became infected and shed", "Only the controls had kidney lesions"],
  "Neither vaccine prevented infection or urinary shedding of hardjo-bovis.", "All infected and shed."),
 ("En un estudio de desafío con vacunas leptospirales pentavalentes con serovar hardjo, ¿qué pasó tras la exposición a hardjo-bovis?", ["Ningún vacunado se infectó", "Solo protegió la vacuna hardjoprajitno", "Todos se infectaron y excretaron", "Solo los controles tuvieron lesión renal"],
  "Ninguna de las vacunas evitó la infección ni la excreción urinaria de hardjo-bovis.", "Todos infectados y excretando.")),

# --- Encephalitic listeriosis diagnosis (15610491)
("15610491", "researcher", 3, "80.9% of the cases were immunohistochemically positive for the listerial antigen",
 ("In 42 ruminants with suspected listerial meningoencephalitis (circling disease), which method confirmed the most cases?", ["Routine bacterial culture", "Gram stain", "Serum antibodies", "Immunohistochemistry"],
  "Immunohistochemistry was positive in 80.9% of cases versus 47.6% by Gram stain and 28.5% by culture.", "Immunohistochemistry."),
 ("En 42 rumiantes con sospecha de meningoencefalitis por Listeria (enfermedad del giro), ¿qué método confirmó más casos?", ["Cultivo bacteriano", "Tinción de Gram", "Anticuerpos séricos", "Inmunohistoquímica"],
  "La inmunohistoquímica fue positiva en el 80,9% de los casos, frente al 47,6% con Gram y el 28,5% con cultivo.", "Inmunohistoquímica.")),

# --- Listeriosis outbreak in dairy cattle (21217050)
("21217050", "explorer", 0, "this outbreak was caused by an unusual L. monocytogenes serotype 4b strain, which was classified into lineage III",
 ("A severe listeriosis outbreak in a herd of 315 dairy cattle, with acute deaths, was caused by what kind of strain?", ["An unusual lineage III strain", "A common lineage I food strain", "A Listeria ivanovii strain", "A lineage II silage strain"],
  "Typing showed an unusual serotype 4b strain of lineage III with a new sigB allele, rare but more common in animals.", "Unusual lineage III."),
 ("Un brote grave de listeriosis en un tambo de 315 animales, con muertes agudas, fue causado por ¿qué tipo de cepa?", ["Una cepa inusual del linaje III", "Una cepa alimentaria común del linaje I", "Una cepa de Listeria ivanovii", "Una cepa del linaje II del silaje"],
  "La tipificación mostró una cepa inusual serotipo 4b del linaje III, con un alelo sigB nuevo, rara pero más común en animales.", "Linaje III inusual.")),

# --- Listeria risk factors on farms (16350271)
("16350271", "researcher", 1, "the bacterium was detected at a constant rate in cattle farm feedstuffs throughout the year",
 ("In a case-control study of ruminant farms, how did Listeria monocytogenes in cattle farm feedstuffs vary over the year?", ["It peaked in the summer", "It was constant all year", "It was never detected at all", "It peaked in winter"],
  "In small-ruminant feeds it peaked in winter, but in cattle feeds it was found at a steady rate year-round.", "Constant all year."),
 ("En un estudio de casos y controles en granjas de rumiantes, ¿cómo varió Listeria monocytogenes en los alimentos de las granjas bovinas durante el año?", ["Tuvo un pico en verano", "Fue constante todo el año", "Nunca se detectó", "Tuvo un pico en invierno"],
  "En alimentos de pequeños rumiantes tuvo un pico invernal, pero en los de bovinos se halló a tasa constante todo el año.", "Constante todo el año.")),

# --- CBPP outbreak in Ethiopia (28332650)
("28332650", "explorer", 2, "had spread to almost the entire herd (96.7%) within the eight-month observation period",
 ("How far did a contagious bovine pleuropneumonia outbreak on an Ethiopian research farm spread in eight months?", ["To about a tenth of the herd", "To about half the herd", "To almost the entire herd", "It stayed in one animal"],
  "CBPP reached 96.7% of the herd, and antibiotic treatment did little to stop the spread.", "Almost the whole herd."),
 ("¿Cuánto se extendió en ocho meses un brote de pleuroneumonía contagiosa bovina en una granja de investigación de Etiopía?", ["A cerca de un décimo del rodeo", "A cerca de la mitad del rodeo", "A casi todo el rodeo", "Quedó en un solo animal"],
  "La PCB alcanzó al 96,7% del rodeo, y el tratamiento antibiótico hizo poco para frenar el contagio.", "Casi todo el rodeo.")),
("28332650", "beginner", 3, "Newly purchased animals that were not tested and quarantined before being introduced onto the farm were suspected",
 ("What was suspected as the source of a contagious bovine pleuropneumonia outbreak on an Ethiopian research farm?", ["Wild buffalo grazing near the farm", "Contaminated stored hay", "A faulty vaccine batch", "Untested, unquarantined new cattle"],
  "Animals bought and introduced without testing or quarantine most likely brought in the infection.", "New untested cattle."),
 ("¿Qué se sospechó como origen de un brote de pleuroneumonía contagiosa bovina en una granja de investigación de Etiopía?", ["Búfalos salvajes que pastaban cerca", "Heno almacenado contaminado con heces", "Un lote de vacuna defectuoso", "Animales nuevos sin cuarentena"],
  "Animales comprados e ingresados sin análisis ni cuarentena probablemente introdujeron la infección.", "Animales nuevos sin control.")),

# --- CBPP diagnosis in Italy (10579536)
("10579536", "researcher", 0, "DNA of MmmSC was detected by PCR in 64 per cent of lung samples",
 ("In a CBPP outbreak in northern Italy, which method detected Mycoplasma mycoides subsp. mycoides in the most lung samples?", ["PCR of lung tissue", "Culture of lung tissue", "Immunohistochemistry", "Gross lung lesions"],
  "PCR was positive in 64% of lungs versus 19% by culture, so it was proposed as a rapid confirmatory test.", "Lung PCR."),
 ("En un brote de PCB en el norte de Italia, ¿qué método detectó Mycoplasma mycoides subsp. mycoides en más muestras de pulmón?", ["PCR de tejido pulmonar", "Cultivo de tejido pulmonar", "Inmunohistoquímica", "Lesiones pulmonares macroscópicas"],
  "La PCR fue positiva en el 64% de los pulmones frente al 19% del cultivo, por lo que se propuso como confirmación rápida.", "PCR de pulmón.")),

# --- T1/44 vaccine strain causing CBPP (15036531)
("15036531", "expert", 1, "These results clearly show that inoculation of T1/44 vaccine via the endobronchial route can lead to CBPP",
 ("What did endobronchial inoculation of the CBPP vaccine strain T1/44 into adult cattle in Namibia show?", ["It gave lifelong sterile immunity", "It can cause CBPP lesions", "It spread to every contact animal", "It was killed within a few hours"],
  "Inoculated cattle developed pleuropneumonia and sequesters, showing T1/44 retains pathogenicity.", "It can cause CBPP."),
 ("¿Qué mostró la inoculación endobronquial de la cepa vacunal T1/44 contra la PCB en bovinos adultos de Namibia?", ["Dio inmunidad estéril de por vida", "Puede causar lesiones de PCB", "Se contagió a todo animal en contacto", "Se eliminó en pocas horas"],
  "Los bovinos inoculados desarrollaron pleuroneumonía y secuestros, lo que muestra que T1/44 conserva patogenicidad.", "Puede causar PCB.")),
]
