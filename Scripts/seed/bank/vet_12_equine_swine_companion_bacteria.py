# Veterinary bacteriology XII — bacterial diseases of horses (strangles, Rhodococcus equi, glanders, CEM,
# botulism, tetanus, Lawsonia, C. difficile), pigs (S. suis, APP, Glässer's disease, ileitis, erysipelas,
# B. suis, M. hyopneumoniae), dogs and cats (B. canis, leptospirosis, Bordetella, Ehrlichia, Bartonella, MRSP)
# and poultry (S. Enteritidis, Campylobacter, M. gallisepticum, fowl cholera).
# Sources: PubMed paper and review abstracts. Excerpts verbatim.
CATEGORY = "veterinaryScience"
Q = [
# --- Strangles carriers and PCR (11093626)
("11093626", "explorer", 0, "the predominant site of carriage was the guttural pouch",
 ("In three protracted strangles outbreaks, where did horses mainly carry Streptococcus equi after recovering?", ["In the guttural pouch", "In the tonsils of the gut", "In the hoof and coronary band", "In the urinary bladder"],
  "Endoscopy showed that silent S. equi carriers harbored the bacterium mostly in the guttural pouches.", "Guttural pouch."),
 ("En tres brotes prolongados de adenitis equina, ¿dónde portaban principalmente los caballos Streptococcus equi tras recuperarse?", ["En la bolsa gutural", "En las tonsilas del intestino", "En el casco y la banda coronaria", "En la vejiga urinaria"],
  "La endoscopia mostró que los portadores silenciosos de S. equi lo alojaban sobre todo en las bolsas guturales.", "Bolsa gutural.")),
("11093626", "researcher", 1, "Prolonged carriage of S. equi, which lasted up to 8 months, did not cease spontaneously before treatment",
 ("How long did silent Streptococcus equi carriage last in horses from protracted strangles outbreaks before treatment?", ["Never beyond two weeks", "Up to 8 months", "Exactly 48 hours", "About 10 years"],
  "Carriage lasted up to 8 months and did not stop on its own, so carriers had to be found and treated.", "Up to 8 months."),
 ("¿Cuánto duró la portación silenciosa de Streptococcus equi en caballos de brotes prolongados de adenitis antes del tratamiento?", ["Nunca más de dos semanas", "Hasta 8 meses", "Exactamente 48 horas", "Cerca de 10 años"],
  "La portación duró hasta 8 meses y no cesó sola, por lo que había que detectar y tratar a los portadores.", "Hasta 8 meses.")),

# --- Treating guttural pouch carriers (11093627)
("11093627", "researcher", 2, "Fourteen of 15 carriers were successfully treated by endoscopic removal of inflammatory material and antibiotic treatment, without surgical intervention",
 ("How were most Streptococcus equi guttural pouch carriers cleared in a study of 15 horses?", ["Bilateral pouch surgery in every single horse", "A single oral dose of ivermectin given twice", "Endoscopic debris removal plus antibiotics", "Vaccination alone, with no antibiotic given"],
  "Fourteen of 15 carriers were cleared by endoscopic removal of chondroids and pus plus antibiotics, without surgery.", "Endoscopy + antibiotics."),
 ("¿Cómo se eliminó la portación de Streptococcus equi en la bolsa gutural en la mayoría de 15 caballos estudiados?", ["Cirugía de ambas bolsas guturales en todos", "Una dosis oral de ivermectina repetida dos veces", "Retiro endoscópico del material y antibióticos", "Solo vacunación, sin ningún antibiótico"],
  "Catorce de 15 portadores se curaron con retiro endoscópico de condroides y pus más antibióticos, sin cirugía.", "Endoscopia + antibióticos.")),

# --- Serology misses carriers (32374892)
("32374892", "researcher", 3, "Only one of the nine carriers (11%) was seropositive using a cut-off of OD ≥ 0.5",
 ("How well did antigen A and C serology detect Streptococcus equi guttural pouch carriers among 287 horses entering quarantine?", ["It detected all nine carriers", "It detected eight of nine carriers", "It worked only in young foals", "Only one of nine was seropositive"],
  "Only 1 of 9 carriers was seropositive at the usual cut-off, so a negative serology does not rule out carriage.", "Poorly: 1 of 9."),
 ("¿Qué tan bien detectó la serología de antígenos A y C a los portadores de Streptococcus equi en la bolsa gutural entre 287 caballos en cuarentena?", ["Detectó a los nueve portadores", "Detectó a ocho de nueve portadores", "Solo funcionó en potrillos jóvenes", "Solo uno de nueve fue seropositivo"],
  "Solo 1 de 9 portadores fue seropositivo con el punto de corte habitual, así que una serología negativa no descarta la portación.", "Mal: 1 de 9.")),

# --- Strangvac (29398274)
("29398274", "expert", 0, "only three of 16 ponies vaccinated with Strangvac 4 became pyretic compared to all 16 placebo-vaccinated control ponies",
 ("In challenge studies of the Strangvac 4 recombinant strangles vaccine, how many vaccinated ponies developed fever?", ["Three of 16", "All 16 of 16", "Twelve of 16", "Eight of 16"],
  "Only 3 of 16 Strangvac 4 ponies became pyretic, versus all 16 placebo controls.", "3 of 16."),
 ("En los ensayos de desafío de la vacuna recombinante Strangvac 4 contra la adenitis equina, ¿cuántos ponis vacunados tuvieron fiebre?", ["Tres de 16", "Los 16 de 16", "Doce de 16", "Ocho de 16"],
  "Solo 3 de 16 ponis con Strangvac 4 tuvieron fiebre, frente a los 16 controles con placebo.", "3 de 16.")),
("29398274", "curious", 1, "causes strangles in the horse, which is characterised by abscessation of the lymph nodes of the head and neck",
 ("What lesion characterizes strangles, the horse disease caused by Streptococcus equi?", ["Ulcers on the cornea", "Abscessed head and neck lymph nodes", "Hoof wall separation", "Blistering of the skin of the back"],
  "Strangles is marked by abscesses in the lymph nodes of the head and neck.", "Lymph node abscesses."),
 ("¿Qué lesión caracteriza a la adenitis equina (papera), causada por Streptococcus equi?", ["Úlceras profundas en la córnea", "Abscesos en ganglios de cabeza y cuello", "Separación de la pared del casco delantero", "Ampollas en la piel del dorso"],
  "La adenitis equina se caracteriza por abscesos en los ganglios linfáticos de cabeza y cuello.", "Abscesos ganglionares.")),

# --- R. equi hyperimmune plasma trial (34738651)
("34738651", "researcher", 2, "The proportion of foals that developed pneumonia was the same between foals transfused with RE HIP (14%; 32/228) and PNAG HIP (14%; 30/215)",
 ("In a randomized trial in 460 foals, how did PNAG hyperimmune plasma compare with R. equi hyperimmune plasma for preventing pneumonia?", ["PNAG plasma halved the pneumonia rate", "R. equi plasma failed completely", "Both groups had about 14% pneumonia", "PNAG plasma caused fatal reactions"],
  "Pneumonia occurred in 14% of foals with either plasma, so PNAG plasma was not superior.", "No difference (14%)."),
 ("En un ensayo aleatorizado con 460 potrillos, ¿cómo se comparó el plasma hiperinmune anti-PNAG con el plasma anti-R. equi para prevenir neumonía?", ["El plasma PNAG redujo la neumonía a la mitad", "El plasma anti-R. equi falló por completo", "Ambos grupos tuvieron cerca de 14% de neumonía", "El plasma PNAG causó reacciones mortales"],
  "La neumonía apareció en el 14% de los potrillos con cualquiera de los plasmas; el PNAG no fue superior.", "Sin diferencia (14%).")),

# --- R. equi multidrug resistance (33853933)
("33853933", "beginner", 3, "it is a natural soil saprophyte that is an intracellular zoonotic pathogen that produces severe bronchopneumonia",
 ("Where does Rhodococcus equi, the cause of severe pneumonia in foals, naturally live?", ["Inside ticks", "In human skin", "In sea algae", "In the soil"],
  "R. equi is a soil saprophyte that can also act as an intracellular pathogen of foals and people.", "Soil."),
 ("¿Dónde vive naturalmente Rhodococcus equi, causa de neumonía grave en potrillos?", ["En garrapatas", "En la piel humana", "En algas marinas", "En el suelo"],
  "R. equi es un saprófito del suelo que también actúa como patógeno intracelular de potrillos y personas.", "El suelo.")),

# --- Glanders treatment (23134717)
("23134717", "researcher", 1, "Twenty three culture positive glanderous horses were successfully treated during a confined outbreak by applying a treatment protocol of 12 weeks duration",
 ("In a confined glanders outbreak, what happened to 23 culture-positive horses given a 12-week antibiotic protocol?", ["All relapsed within a month", "They were successfully treated", "Half died during treatment", "They became chronic carriers"],
  "A 12-week course of enrofloxacin, trimethoprim-sulfadiazine and then doxycycline cured all 23 horses, without relapse after immunosuppression.", "All cured."),
 ("En un brote confinado de muermo, ¿qué pasó con 23 caballos con cultivo positivo tratados 12 semanas con antibióticos?", ["Todos recayeron en un mes", "Fueron tratados con éxito", "La mitad murió durante el tratamiento", "Quedaron como portadores crónicos"],
  "Un esquema de 12 semanas con enrofloxacina, trimetoprima-sulfadiazina y luego doxiciclina curó a los 23 caballos, sin recaídas tras inmunosuprimirlos.", "Todos curados.")),
("23134717", "explorer", 2, "this treatment can only be an option in certain situations and should not replace the current \"testing and culling\" policy",
 ("Despite curing horses, what did the authors of a glanders treatment study conclude about control policy?", ["Testing and culling should be abolished", "All horses should get doxycycline yearly", "Treatment should not replace test and cull", "Glanders no longer needs reporting"],
  "Because of cost and duration, treatment is only for special cases such as valuable or wildlife animals; test-and-cull stays.", "Keep test and cull."),
 ("Pese a curar a los caballos, ¿qué concluyeron los autores de un estudio de tratamiento del muermo sobre la política de control?", ["Hay que abolir el sacrificio de positivos", "Todos los caballos deben recibir doxiciclina al año", "El tratamiento no debe reemplazar el sacrificio", "El muermo ya no requiere notificación"],
  "Por su costo y duración, tratar solo es opción en casos especiales, como animales valiosos o silvestres; se mantiene el diagnóstico y sacrificio.", "Mantener sacrificio.")),

# --- Glanders in Bahrain (25255232)
("25255232", "beginner", 3, "Glanders, caused by the gram-negative bacterium Burkholderia mallei",
 ("Which bacterium causes glanders, a zoonotic disease of horses and other solipeds?", ["Bacillus anthracis", "Clostridium tetani", "Streptococcus equi", "Burkholderia mallei"],
  "Glanders is caused by the gram-negative bacterium Burkholderia mallei.", "Burkholderia mallei."),
 ("¿Qué bacteria causa el muermo, una zoonosis de caballos y otros solípedos?", ["Bacillus anthracis", "Clostridium tetani", "Streptococcus equi", "Burkholderia mallei"],
  "El muermo lo causa la bacteria gramnegativa Burkholderia mallei.", "Burkholderia mallei.")),
("25255232", "researcher", 0, "The samples from the outbreak in Bahrain separated into two distinct clusters, suggesting a complex epidemiological background and evidence for the involvement of multiple B. mallei strains",
 ("What did genotyping of Burkholderia mallei from a glanders outbreak in Bahrain reveal?", ["Two clusters, from multiple strains", "One clone from a single stallion", "A strain from laboratory escape", "A virus, not a bacterium"],
  "The isolates split into two clusters, pointing to several strains and repeated introductions, probably via horse trade.", "Multiple strains."),
 ("¿Qué reveló la genotipificación de Burkholderia mallei de un brote de muermo en Baréin?", ["Dos grupos, de varias cepas", "Un solo clon de un padrillo", "Una cepa escapada de laboratorio", "Un virus, no una bacteria"],
  "Los aislados se dividieron en dos grupos, lo que indica varias cepas e introducciones repetidas, probablemente por comercio de caballos.", "Varias cepas.")),

# --- CEM (16728066)
("16728066", "beginner", 1, "Contagious equine metritis (CEM) is a sexually transmissible disease in mares",
 ("How is contagious equine metritis (CEM), caused by Taylorella equigenitalis, mainly spread?", ["By mosquito bites", "Sexually, at breeding", "Through dusty hay", "By drinking river water"],
  "CEM is a sexually transmissible disease of mares.", "Sexually."),
 ("¿Cómo se transmite principalmente la metritis contagiosa equina (MCE), causada por Taylorella equigenitalis?", ["Por picaduras de mosquitos", "Por vía sexual, en la monta", "Por heno con mucho polvo", "Por beber agua de río"],
  "La MCE es una enfermedad de transmisión sexual en las yeguas.", "Vía sexual.")),
("16728066", "expert", 2, "were all negative for T. equigenitalis . but in the PCR-assay 54 (49%) were positive for Taylorella -DNA",
 ("In 107 healthy mares that were culture-negative for Taylorella equigenitalis, what share tested PCR-positive?", ["None of them", "About 5%", "About 49%", "All of them"],
  "Nearly half were PCR-positive, suggesting Taylorella is endemic and of limited significance in breeding.", "~49%."),
 ("En 107 yeguas sanas con cultivo negativo para Taylorella equigenitalis, ¿qué proporción fue positiva por PCR?", ["Ninguna", "Cerca de 5%", "Cerca de 49%", "Todas"],
  "Casi la mitad fue positiva por PCR, lo que sugiere que Taylorella es endémica y de importancia limitada en la reproducción.", "~49%.")),

# --- Type C botulism (10935041)
("10935041", "explorer", 3, "It was hypothesized that the outbreak was a result of birds, presumably ravens, feeding at the burial site",
 ("How was preformed toxin thought to reach 12 horses and a mule in an Arizona type C botulism outbreak?", ["Through contaminated round-bale silage", "Through a faulty vaccine batch", "Through tick bites in pasture", "Via ravens feeding at a horse burial site"],
  "Toxin was found in soil and bird droppings at a nearby burial site; ravens likely carried it to the facilities.", "Ravens from burial site."),
 ("¿Cómo se cree que la toxina preformada llegó a 12 caballos y una mula en un brote de botulismo tipo C en Arizona?", ["Por ensilaje de rollos contaminado con tierra", "Por un lote de vacuna defectuoso", "Por picaduras de garrapatas", "Por cuervos que comían en un entierro"],
  "Se halló toxina en suelo y heces de aves de un sitio de entierro cercano; los cuervos probablemente la llevaron a las instalaciones.", "Cuervos del entierro.")),

# --- Tetanus titres (26284567)
("26284567", "researcher", 1, "are likely to have serum antibody titres consistent with protection against tetanus for more than 3 years",
 ("After three-dose basic immunisation from age 5 months, how long did horses keep protective tetanus antibody titres?", ["Less than 6 months", "More than 3 years", "Exactly 12 months", "Only 2 weeks"],
  "Titres stayed protective for over 3 years, suggesting tetanus booster guidelines for horses should be revised.", ">3 years."),
 ("Tras una inmunización básica de tres dosis desde los 5 meses, ¿cuánto tiempo mantuvieron los caballos títulos protectores contra el tétanos?", ["Menos de 6 meses", "Más de 3 años", "Exactamente 12 meses", "Solo 2 semanas"],
  "Los títulos siguieron protectores más de 3 años, lo que sugiere revisar las pautas de refuerzo antitetánico en caballos.", ">3 años.")),

# --- Lawsonia in foals (30850006)
("30850006", "explorer", 2, "causes equine proliferative enteropathy, mainly in horses around weaning",
 ("At what age does Lawsonia intracellularis mainly cause equine proliferative enteropathy?", ["In newborn foals", "In elderly horses", "Around weaning", "In pregnant mares"],
  "EPE mainly affects foals around weaning; the Danish cases were 6–7 months old.", "Around weaning."),
 ("¿A qué edad causa Lawsonia intracellularis principalmente la enteropatía proliferativa equina?", ["En potrillos recién nacidos", "En caballos ancianos", "Alrededor del destete", "En yeguas preñadas"],
  "La EPE afecta sobre todo a potrillos cerca del destete; los casos daneses tenían 6–7 meses.", "Cerca del destete.")),

# --- C. difficile colitis (15338908)
("15338908", "explorer", 0, "All horses positive for C. difficile were treated with beta-lactam antibiotics",
 ("Which antibiotics had all horses with Clostridium difficile-associated acute colitis received in a Swedish study?", ["Beta-lactams", "Fluoroquinolones", "Tetracyclines", "No antibiotics"],
  "C. difficile was found only in antibiotic-treated colitis cases, all of which had received beta-lactams.", "Beta-lactams."),
 ("¿Qué antibióticos habían recibido todos los caballos con colitis aguda asociada a Clostridium difficile en un estudio sueco?", ["Betalactámicos", "Solo fluoroquinolonas", "Solo tetraciclinas", "Ningún antibiótico"],
  "C. difficile se halló solo en colitis de caballos tratados con antibióticos, y todos habían recibido betalactámicos.", "Betalactámicos.")),

# --- S. suis Sichuan outbreak (16707046)
("16707046", "beginner", 1, "prohibiting backyard slaughtering ended the outbreak",
 ("What measure ended the 2005 human Streptococcus suis outbreak in Sichuan, China?", ["Vaccinating all farmers", "Banning backyard slaughter", "Closing all local schools", "Spraying insecticides"],
  "Farmers were infected while slaughtering sick or dead pigs; prohibiting backyard slaughter stopped the outbreak.", "Ban backyard slaughter."),
 ("¿Qué medida terminó el brote humano de Streptococcus suis de 2005 en Sichuan, China?", ["Vacunar a todos los granjeros", "Prohibir la faena casera", "Cerrar las escuelas", "Fumigar con insecticidas"],
  "Los granjeros se infectaron al faenar cerdos enfermos o muertos; prohibir la faena casera detuvo el brote.", "Prohibir la faena casera.")),
("16707046", "researcher", 3, "Sixty-one (28%) of the farmers had streptococcal toxic shock syndrome; 38 (62%) of them died",
 ("In the 2005 Sichuan Streptococcus suis outbreak, what happened to farmers with streptococcal toxic shock syndrome?", ["All recovered without sequelae", "About 5% of them died", "None needed hospital care", "About 62% of them died"],
  "Of 61 farmers with toxic shock syndrome, 38 (62%) died, an unusually high death ratio.", "62% died."),
 ("En el brote de Streptococcus suis de Sichuan en 2005, ¿qué pasó con los granjeros con síndrome de shock tóxico estreptocócico?", ["Todos se recuperaron sin secuelas", "Murió cerca del 5%", "Ninguno necesitó hospital", "Murió cerca del 62%"],
  "De 61 granjeros con shock tóxico murieron 38 (62%), una letalidad inusualmente alta.", "Murió el 62%.")),

# --- S. suis ST7 (16965698)
("16965698", "expert", 0, "These findings strongly suggest that ST-7 is an emerging, highly virulent S. suis clone",
 ("What did molecular typing show about the Streptococcus suis strain behind the 2005 Sichuan outbreak?", ["An emerging virulent clone, ST-7", "A mix of many unrelated serotypes", "A strain imported from Europe", "A strain of low virulence"],
  "Almost all human and pig isolates were ST-7, a single-locus variant of ST-1 with increased virulence.", "Clone ST-7."),
 ("¿Qué mostró la tipificación molecular de la cepa de Streptococcus suis del brote de Sichuan de 2005?", ["Un clon emergente virulento, ST-7", "Una mezcla de muchos serotipos distintos", "Una cepa importada de Europa", "Una cepa de baja virulencia"],
  "Casi todos los aislados humanos y porcinos eran ST-7, una variante de un solo locus de ST-1 con mayor virulencia.", "Clon ST-7.")),

# --- S. suis meningitis Vietnam (19413493)
("19413493", "explorer", 1, "S. suis was the most common pathogen and was detected in 151 (33.6%) of the patients",
 ("Among 450 adults with suspected bacterial meningitis in southern Vietnam, which pathogen was most common?", ["Neisseria meningitidis", "Streptococcus suis", "Haemophilus influenzae", "Listeria monocytogenes"],
  "S. suis, a pig-associated zoonosis, caused a third of cases and was the leading cause of adult meningitis.", "Streptococcus suis."),
 ("Entre 450 adultos con sospecha de meningitis bacteriana en el sur de Vietnam, ¿qué patógeno fue el más común?", ["Neisseria meningitidis", "Streptococcus suis", "Haemophilus influenzae", "Listeria monocytogenes"],
  "S. suis, una zoonosis ligada al cerdo, causó un tercio de los casos y fue la principal causa de meningitis en adultos.", "Streptococcus suis.")),

# --- APP serovars Germany (33472678)
("33472678", "researcher", 3, "Serotyping revealed a prominent role of serovar 2 in clinical cases (64% of all isolates)",
 ("Which Actinobacillus pleuropneumoniae serovar predominated in German pleuropneumonia outbreaks from 2010 to 2019?", ["Serovar 18", "Serovar 16", "Serovar 9/11", "Serovar 2"],
  "Serovar 2 made up 64% of isolates, followed by serovar 9/11 at about 15%.", "Serovar 2."),
 ("¿Qué serovar de Actinobacillus pleuropneumoniae predominó en los brotes de pleuroneumonía en Alemania de 2010 a 2019?", ["Serovar 18", "Serovar 16", "Serovar 9/11", "Serovar 2"],
  "El serovar 2 representó el 64% de los aislados, seguido del 9/11 con cerca del 15%.", "Serovar 2.")),

# --- APP review (38098987)
("38098987", "curious", 0, "This highly contagious disease produces high morbidity and mortality in the swine industry. However, no effective vaccine exists to prevent it",
 ("What does a review state about vaccines against porcine pleuropneumonia caused by Actinobacillus pleuropneumoniae?", ["No effective vaccine exists", "One vaccine has eradicated it", "Vaccines are banned in pigs", "Only oral vaccines work well"],
  "Despite high morbidity and mortality, no effective vaccine exists, so surface proteins are studied as new immunogens.", "None effective yet."),
 ("¿Qué afirma una revisión sobre las vacunas contra la pleuroneumonía porcina por Actinobacillus pleuropneumoniae?", ["Aún no existe una vacuna eficaz", "Una vacuna ya la erradicó", "Las vacunas están prohibidas en cerdos", "Solo funcionan bien las orales"],
  "Pese a su alta morbilidad y mortalidad, no hay vacuna eficaz, por eso se estudian proteínas de superficie como nuevos inmunógenos.", "Ninguna eficaz aún.")),

# --- Glässer's disease prevalence (32652336)
("32652336", "beginner", 1, "It is the causative agent of Glässer's disease, causing systemic infection and polyserositis, meningitis, and arthritis",
 ("What lesions does Glaesserella (Haemophilus) parasuis cause in pigs with Glässer's disease?", ["Diamond skin lesions and high fever", "Polyserositis, meningitis, arthritis", "Vesicles on the snout and feet", "Bloody diarrhea with no fever"],
  "Glässer's disease is a systemic infection with polyserositis, meningitis and arthritis.", "Polyserositis, arthritis."),
 ("¿Qué lesiones causa Glaesserella (Haemophilus) parasuis en cerdos con enfermedad de Glässer?", ["Lesiones romboidales en piel y fiebre", "Poliserositis, meningitis y artritis", "Vesículas en el hocico y las patas", "Diarrea con sangre y sin fiebre"],
  "La enfermedad de Glässer es una infección sistémica con poliserositis, meningitis y artritis.", "Poliserositis, artritis.")),
("32652336", "researcher", 2, "The overall prevalence of H. parasuis in pigs in China was 27.8 %",
 ("What overall prevalence of Haemophilus (Glaesserella) parasuis in Chinese pigs did a 41-article meta-analysis estimate?", ["About 2.8%", "About 87%", "About 27.8%", "About 0.3%"],
  "The pooled prevalence was 27.8%, highest in suckling piglets.", "~28%."),
 ("¿Qué prevalencia global de Haemophilus (Glaesserella) parasuis en cerdos de China estimó un metaanálisis de 41 artículos?", ["Cerca de 2,8%", "Cerca de 87%", "Cerca de 27,8%", "Cerca de 0,3%"],
  "La prevalencia combinada fue 27,8%, más alta en lechones lactantes.", "~28%.")),

# --- Vaccinating gilts vs piglets for Glässer's (12137419)
("12137419", "expert", 3, "The average daily liveweight gain of the pigs born to the vaccinated gilts was significantly greater than that of those born to the unvaccinated gilts, but the vaccination of the piglets had no effect",
 ("In a Glässer's disease challenge study, which vaccination strategy improved piglet growth?", ["Vaccinating only the piglets", "Neither strategy helped", "Vaccinating boars before mating", "Vaccinating the pregnant gilts"],
  "Piglets from vaccinated gilts grew faster and had fewer lesions; vaccinating piglets themselves had no effect.", "Vaccinate gilts."),
 ("En un estudio de desafío de enfermedad de Glässer, ¿qué estrategia de vacunación mejoró el crecimiento de los lechones?", ["Vacunar solo a los lechones", "Ninguna estrategia sirvió", "Vacunar a los verracos antes del servicio", "Vacunar a las cerdas preñadas"],
  "Los lechones de cerdas vacunadas crecieron más y tuvieron menos lesiones; vacunar a los lechones no tuvo efecto.", "Vacunar cerdas.")),

# --- Lawsonia vaccine meta-analysis (36288149)
("36288149", "researcher", 0, "the vaccination resulted in statistically significant reductions in bacterial fecal shedding",
 ("What did a meta-analysis find about commercial Lawsonia intracellularis vaccines for porcine proliferative enteropathy?", ["Less shedding and mortality", "No effect on any outcome", "Higher death rates in pigs", "Lower daily weight gain"],
  "Vaccination reduced fecal shedding and mortality and increased average daily weight gain.", "Less shedding, deaths."),
 ("¿Qué halló un metaanálisis sobre las vacunas comerciales contra Lawsonia intracellularis en la enteropatía proliferativa porcina?", ["Menos excreción y mortalidad", "Ningún efecto en nada", "Más muertes en los cerdos", "Menor ganancia diaria de peso"],
  "La vacunación redujo la excreción fecal y la mortalidad y aumentó la ganancia diaria de peso.", "Menos excreción y muertes.")),

# --- Swine erysipelas risk factors (32965781)
("32965781", "explorer", 1, "more attention should be given to the impacts of high temperature and precipitation on the swine erysipelas epidemic",
 ("Which environmental factors were linked to swine erysipelas outbreaks in China?", ["Cold, dry winter winds from the north", "High temperature and rainfall", "Farm altitude above 3,000 m", "Low soil salinity only"],
  "Extreme heat and precipitation raised the odds of erysipelas, and summer was the main epidemic season in South Central China.", "Heat and rain."),
 ("¿Qué factores ambientales se asociaron con los brotes de erisipela porcina en China?", ["Vientos fríos y secos de invierno", "Temperatura alta y lluvias", "Altitud superior a 3.000 m", "Solo baja salinidad del suelo"],
  "El calor extremo y las lluvias aumentaron el riesgo de erisipela, y el verano fue la principal estación epidémica en el centro-sur.", "Calor y lluvia.")),

# --- B. suis in feral swine (24484477)
("24484477", "explorer", 2, "brucellosis infections in feral swine within the US are typically caused by B. suis",
 ("Which Brucella species was isolated from feral swine in high-prevalence US areas?", ["Brucella abortus", "Brucella canis", "Brucella suis", "Brucella ovis"],
  "All 22 isolates were B. suis, mostly biovar 1.", "Brucella suis."),
 ("¿Qué especie de Brucella se aisló de cerdos asilvestrados en zonas de alta prevalencia de EE. UU.?", ["Brucella abortus", "Brucella canis", "Brucella suis", "Brucella ovis"],
  "Los 22 aislados fueron B. suis, sobre todo biovar 1.", "Brucella suis.")),

# --- M. hyopneumoniae vaccination and transmission (20605734)
("20605734", "researcher", 0, "The study indicates that vaccination does not significantly reduce the transmission of this respiratory pathogen",
 ("Did bacterin vaccination at 3 weeks reduce transmission of Mycoplasma hyopneumoniae in nursery pigs?", ["Not significantly", "Yes, it stopped it fully", "Yes, by about 90%", "It doubled transmission"],
  "The reproduction ratio was similar in vaccinated and unvaccinated pigs (0.71 vs 0.56).", "Not significantly."),
 ("¿Redujo la vacunación con bacterina a las 3 semanas la transmisión de Mycoplasma hyopneumoniae en lechones de recría?", ["No de forma significativa", "Sí, la frenó por completo", "Sí, en cerca de 90%", "Duplicó la transmisión"],
  "La tasa de reproducción fue similar en vacunados y no vacunados (0,71 frente a 0,56).", "No significativamente.")),

# --- B. canis kennel outbreak (38991314)
("38991314", "explorer", 2, "the transmission of B. canis in the breeding kennel was most likely caused by the introduction of one infected dog",
 ("How did Brucella canis most likely enter a Dutch breeding kennel in 2019?", ["Via contaminated dry dog food", "Through a visiting stray cat", "One infected dog brought in", "Through rats in the feed store"],
  "WGS put all isolates in one cluster, pointing to a single imported infected male dog.", "One imported dog."),
 ("¿Cómo entró probablemente Brucella canis a un criadero de perros neerlandés en 2019?", ["Por alimento balanceado contaminado", "Por un gato callejero que visitaba", "Por la llegada de un perro infectado", "Por ratas en el depósito de alimento"],
  "La secuenciación agrupó todos los aislados en un solo clúster, lo que apunta a un único macho importado infectado.", "Un perro importado.")),
("38991314", "researcher", 3, "antibodies against B. canis could be detected in 23 out of 69 dogs (34 %) by serum agglutination test",
 ("What share of contact dogs in a Dutch kennel had antibodies to Brucella canis after an infected dog arrived?", ["All 69 dogs", "About 3%", "About 90%", "About 34%"],
  "23 of 69 contact dogs (34%) were seropositive, and most of those were also culture-positive.", "~34%."),
 ("¿Qué proporción de perros de contacto de un criadero neerlandés tenía anticuerpos contra Brucella canis tras llegar un perro infectado?", ["Los 69 perros", "Cerca del 3%", "Cerca del 90%", "Cerca del 34%"],
  "23 de 69 perros de contacto (34%) fueron seropositivos, y la mayoría también tuvo cultivo positivo.", "~34%.")),

# --- Human B. canis outbreak (19653929)
("19653929", "curious", 0, "This outbreak involved six persons (three children and three adults), a bitch and three puppies which had close daily contact with the family",
 ("Who was involved in a reported human Brucella canis outbreak linked to dogs?", ["A family with a bitch and her puppies", "Workers at a large pig slaughterhouse", "Soldiers drinking raw camel milk", "Hunters of feral wild boars"],
  "Six family members (three children, three adults) were infected through close contact with a bitch and her puppies.", "A family with dogs."),
 ("¿Quiénes participaron en un brote humano de Brucella canis ligado a perros?", ["Una familia con una perra y cachorros", "Obreros de un gran matadero de cerdos", "Soldados que bebían leche de camella", "Cazadores de jabalíes asilvestrados"],
  "Seis integrantes de una familia (tres niños y tres adultos) se infectaron por contacto estrecho con una perra y sus cachorros.", "Familia con perros.")),

# --- Leptospirosis vaccine uptake UK (35864518)
("35864518", "explorer", 1, "almost half of the UK primary care attending population received a leptospirosis vaccine during the year",
 ("What share of UK dogs under primary veterinary care received a leptospirosis vaccine in one year?", ["Nearly all of them", "Almost half", "Less than 5%", "About one in ten"],
  "Of over 900,000 dogs, 49% got at least one leptospirosis vaccine during the 12 months.", "~49%."),
 ("¿Qué proporción de perros atendidos en clínicas del Reino Unido recibió una vacuna contra leptospirosis en un año?", ["Casi todos", "Casi la mitad", "Menos del 5%", "Cerca de uno de cada diez"],
  "De más de 900.000 perros, el 49% recibió al menos una vacuna contra leptospirosis en 12 meses.", "~49%.")),
("35864518", "beginner", 2, "Vaccination of dogs against leptospirosis is an important approach to preventing clinical disease, or reducing disease severity, as well as reducing transmission of the infection to humans",
 ("Besides protecting the dog, why is leptospirosis vaccination of dogs important?", ["It also prevents fleas", "It cures joint arthritis", "It cuts spread to humans", "It improves coat quality"],
  "Leptospirosis is zoonotic, so vaccinating dogs also reduces transmission to people.", "Less spread to humans."),
 ("Además de proteger al perro, ¿por qué es importante vacunar a los perros contra la leptospirosis?", ["También previene las pulgas", "Cura la artritis articular", "Reduce el contagio a humanos", "Mejora la calidad del pelaje"],
  "La leptospirosis es zoonótica, así que vacunar perros también reduce la transmisión a las personas.", "Menos contagio humano.")),

# --- Bordetella vaccine routes (27256028)
("27256028", "researcher", 3, "the intranasal route of delivery conferred superior clinical outcomes",
 ("In a randomized challenge trial in puppies, which Bordetella bronchiseptica vaccine route gave the best clinical protection?", ["The oral route", "Subcutaneous injection", "No route beat placebo", "The intranasal route"],
  "Intranasally vaccinated puppies coughed, sneezed and retched less than orally vaccinated or placebo puppies.", "Intranasal."),
 ("En un ensayo aleatorizado de desafío en cachorros, ¿qué vía de vacunación contra Bordetella bronchiseptica dio la mejor protección clínica?", ["La vía oral", "La inyección subcutánea", "Ninguna superó al placebo", "La vía intranasal"],
  "Los cachorros vacunados por vía intranasal tosieron, estornudaron y tuvieron arcadas menos que los de vía oral o placebo.", "Intranasal.")),

# --- Ehrlichia canis doxycycline (18196732)
("18196732", "researcher", 0, "doxycycline cleared E canis from the blood and tissues of experimentally infected dogs",
 ("What happened to dogs with chronic experimental Ehrlichia canis infection after 3–4 weeks of doxycycline?", ["E. canis was cleared from blood and tissues", "All dogs relapsed after dexamethasone was given", "Platelets fell to dangerous levels", "Antibodies rose sharply in all dogs"],
  "No E. canis DNA was found after treatment, even after dexamethasone was given to provoke relapse.", "Infection cleared."),
 ("¿Qué pasó con perros con infección crónica experimental por Ehrlichia canis tras 3–4 semanas de doxiciclina?", ["E. canis se eliminó de sangre y tejidos", "Todos recayeron tras la dexametasona", "Las plaquetas cayeron a niveles peligrosos", "Los anticuerpos subieron mucho en todos"],
  "No se detectó ADN de E. canis tras el tratamiento, ni siquiera al dar dexametasona para provocar recaídas.", "Infección eliminada.")),

# --- Bartonella in cats (7561200)
("7561200", "beginner", 1, "Cat exposure has been directly associated with the development of human Bartonella henselae infections, resulting in cat-scratch disease",
 ("Which bacterium, carried by cats, causes cat-scratch disease in people?", ["Pasteurella multocida", "Bartonella henselae", "Toxoplasma gondii", "Leptospira canicola"],
  "Human B. henselae infection, including cat-scratch disease, is directly linked to cat exposure.", "Bartonella henselae."),
 ("¿Qué bacteria, portada por los gatos, causa la enfermedad por arañazo de gato en las personas?", ["Pasteurella multocida", "Bartonella henselae", "Toxoplasma gondii", "Leptospira canicola"],
  "La infección humana por B. henselae, incluido el arañazo de gato, se asocia directamente con el contacto con gatos.", "Bartonella henselae.")),
("7561200", "explorer", 2, "Seroprevalences paralleled increasing climatic warmth (P < .02) and annual precipitation (P < .03)",
 ("How did Bartonella henselae seroprevalence in North American pet cats vary by region?", ["Highest in cold, dry Alaska", "Same in every region", "Higher in warm, humid areas", "Higher only in big cities"],
  "Seroprevalence rose with warmth and rainfall, likely reflecting more flea vectors.", "Warm, humid areas."),
 ("¿Cómo varió la seroprevalencia de Bartonella henselae en gatos de Norteamérica según la región?", ["Mayor en la fría y seca Alaska", "Igual en todas las regiones", "Mayor en zonas cálidas y húmedas", "Mayor solo en grandes ciudades"],
  "La seroprevalencia aumentó con el calor y la lluvia, probablemente por más pulgas vectoras.", "Zonas cálidas y húmedas.")),

# --- MRSP risk factors (24290489)
("24290489", "researcher", 3, "animals that had been hospitalised (OR 104.4, 95% CI 21.3-511.6, P<0.001)",
 ("In a German case-control study, which factor most strongly raised the risk of MRSP infection in dogs and cats?", ["Eating raw meat diets", "Living in rural farm areas", "Being a young puppy", "Previous hospitalisation"],
  "Hospitalisation carried an odds ratio over 100, pointing to a hospital-associated epidemiology.", "Hospitalisation."),
 ("En un estudio de casos y controles alemán, ¿qué factor elevó más el riesgo de infección por SPRM en perros y gatos?", ["Comer dietas de carne cruda", "Vivir en zonas rurales", "Ser un cachorro joven", "Haber estado hospitalizado"],
  "La hospitalización tuvo una razón de probabilidades mayor de 100, lo que sugiere una epidemiología hospitalaria.", "Hospitalización.")),

# --- S. Enteritidis vaccination Belgium (24268005)
("24268005", "researcher", 2, "While PT4 and PT21 were predominantly isolated in Belgium in layers and humans before 2007, a significant reduction of those PTs was observed in both populations in the period 2007-2010",
 ("What changed in Belgium after mandatory Salmonella Enteritidis vaccination of laying hens began in 2007?", ["PT4 and PT21 became more common", "Human cases disappeared entirely", "PT4 and PT21 fell in hens and humans", "Layers stopped carrying any Salmonella"],
  "The previously dominant phage types PT4 and PT21 dropped significantly in both layers and humans.", "PT4/PT21 declined."),
 ("¿Qué cambió en Bélgica tras la vacunación obligatoria de gallinas ponedoras contra Salmonella Enteritidis desde 2007?", ["PT4 y PT21 se volvieron más comunes", "Los casos humanos desaparecieron", "PT4 y PT21 bajaron en gallinas y humanos", "Las ponedoras dejaron de portar Salmonella"],
  "Los fagotipos antes dominantes, PT4 y PT21, bajaron significativamente tanto en ponedoras como en humanos.", "Bajaron PT4/PT21.")),

# --- Campylobacter in Danish broilers (25638473)
("25638473", "explorer", 3, "summer vs. winter; if the previous flock in the house was positive for Campylobacter",
 ("Which risk factors for Campylobacter colonization were identified in Danish broiler flocks?", ["Winter and new wood shavings", "Feeding extra wheat in starter", "Female-only flocks and dark houses", "Summer and a positive previous flock"],
  "Summer season and a Campylobacter-positive previous flock in the same house raised the risk.", "Summer, prior positive flock."),
 ("¿Qué factores de riesgo de colonización por Campylobacter se identificaron en lotes de pollos de engorde daneses?", ["El invierno y viruta nueva", "Más trigo en el iniciador", "Lotes solo de hembras y galpones oscuros", "El verano y un lote previo positivo"],
  "La estación de verano y un lote anterior positivo en el mismo galpón aumentaron el riesgo.", "Verano, lote previo positivo.")),

# --- M. gallisepticum review (36851345)
("36851345", "beginner", 0, "MG is transmitted both by horizontal and vertical routes",
 ("How is Mycoplasma gallisepticum transmitted in chickens?", ["Horizontally and vertically", "Only by mosquito bites", "Only through farm soil", "It is not transmissible at all"],
  "MG spreads between birds and also through the egg from hen to chick.", "Horizontal and vertical."),
 ("¿Cómo se transmite Mycoplasma gallisepticum en las gallinas?", ["Horizontal y verticalmente", "Solo por picadura de mosquitos", "Solo a través del suelo", "No es transmisible"],
  "MG se contagia entre aves y también por el huevo, de la gallina al pollito.", "Horizontal y vertical.")),

# --- Fowl cholera genomics (32118528)
("32118528", "beginner", 2, "Fowl cholera, caused by Pasteurella multocida",
 ("Which bacterium causes fowl cholera in chickens?", ["Vibrio cholerae", "Escherichia coli", "Pasteurella multocida", "Salmonella Gallinarum"],
  "Fowl cholera is caused by Pasteurella multocida, not by Vibrio cholerae.", "Pasteurella multocida."),
 ("¿Qué bacteria causa el cólera aviar en las gallinas?", ["Vibrio cholerae", "Escherichia coli", "Pasteurella multocida", "Salmonella Gallinarum"],
  "El cólera aviar lo causa Pasteurella multocida, no Vibrio cholerae.", "Pasteurella multocida.")),
("32118528", "expert", 3, "while a killed autogenous vaccine carrying LPS type L3 had been successful in protecting against challenge from L3 isolates it might have driven the emergence of the closely related clade 2",
 ("What did genomics suggest about the autogenous vaccine used against fowl cholera on a free-range chicken farm?", ["It caused fowl cholera itself", "It protected against all clades", "It was never given to the birds", "It may have driven an L1 clade"],
  "The L3-based killed vaccine protected against L3 isolates but may have selected the related LPS L1 clade 2, against which it failed.", "Selected new clade."),
 ("¿Qué sugirió la genómica sobre la vacuna autógena contra el cólera aviar usada en una granja de pollos camperos?", ["Ella misma causó el cólera aviar", "Protegió contra todos los clados", "Nunca se aplicó a las aves", "Pudo impulsar un clado L1"],
  "La vacuna inactivada con LPS L3 protegió contra aislados L3, pero pudo seleccionar el clado 2 (LPS L1), contra el que falló.", "Seleccionó nuevo clado.")),
]
