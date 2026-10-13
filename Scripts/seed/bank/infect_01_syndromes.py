# Infectious diseases I — clinical infectious syndromes, sepsis, healthcare-associated infections and
# infection prevention. Sources: StatPearls chapters (PubMed book records). Excerpts verbatim.
CATEGORY = "infectiousDiseases"
Q = [
# --- Meningitis (29261975)
("29261975", "beginner", 2, "Bacterial meningitis is a bacterial infection of the meninges, which is the protective covering for the brain and spinal cord",
 ("What tissue is inflamed in meningitis?", ["The lining of the lungs", "The heart valves", "The meninges covering the brain and spinal cord", "The kidney capsule"],
  "Meningitis is inflammation of the meninges; bacterial meningitis is a life-threatening emergency.", "The meninges."),
 ("¿Qué tejido se inflama en la meningitis?", ["El revestimiento de los pulmones", "Las válvulas cardíacas", "Las meninges que cubren el cerebro y la médula espinal", "La cápsula renal"],
  "La meningitis es la inflamación de las meninges; la bacteriana es una emergencia potencialmente mortal.", "Las meninges.")),

# --- Endocarditis (32491573)
("32491573", "curious", 1, "Infective endocarditis is an inflammatory condition of the endocardium, the inner lining of the heart, including the valves",
 ("Infective endocarditis affects…", ["The outer lining of the heart (pericardium)", "The inner lining of the heart, including the valves", "The coronary arteries only", "The heart muscle only"],
  "Endocarditis involves the endocardium and valves, usually from bacterial infection forming vegetations.", "Endocardium and valves."),
 ("La endocarditis infecciosa afecta…", ["El revestimiento externo del corazón (pericardio)", "El revestimiento interno del corazón, incluidas las válvulas", "Solo las coronarias", "Solo el músculo cardíaco"],
  "La endocarditis compromete el endocardio y las válvulas, por lo general por infección bacteriana con vegetaciones.", "Endocardio y válvulas.")),
("32491573", "researcher", 3, "the Osler triad—pneumonia, meningitis, and endocarditis—particularly in cases caused by Streptococcus pneumoniae",
 ("The Osler triad (pneumonia, meningitis and endocarditis) is classically caused by…", ["Staphylococcus aureus", "Enterococcus faecalis", "Viridans streptococci", "Streptococcus pneumoniae"],
  "Osler described the triad of pneumonia, meningitis and endocarditis, particularly with S. pneumoniae.", "S. pneumoniae."),
 ("La tríada de Osler (neumonía, meningitis y endocarditis) es causada clásicamente por…", ["Staphylococcus aureus", "Enterococcus faecalis", "Estreptococos del grupo viridans", "Streptococcus pneumoniae"],
  "Osler describió la tríada de neumonía, meningitis y endocarditis, sobre todo por S. pneumoniae.", "S. pneumoniae.")),

# --- Pyelonephritis (30137822)
("30137822", "curious", 0, "Pyelonephritis generally occurs as a complication of an ascending urinary tract infection",
 ("How does acute pyelonephritis usually develop?", ["As an ascending infection from the bladder to the kidney", "From a skin wound", "From inhaled bacteria", "From mosquito bites"],
  "Most pyelonephritis is an ascending UTI from bladder to kidney; hematogenous spread is less common.", "Ascending UTI."),
 ("¿Cómo se desarrolla habitualmente la pielonefritis aguda?", ["Como infección ascendente de la vejiga al riñón", "Desde una herida de piel", "Por bacterias inhaladas", "Por picaduras de mosquito"],
  "La mayoría de las pielonefritis son ITU ascendentes de vejiga a riñón; la vía hematógena es menos común.", "ITU ascendente.")),
("30137822", "explorer", 2, "The most common acute pyelonephritis symptoms are usually fever and flank pain",
 ("Which symptoms best distinguish pyelonephritis from simple cystitis?", ["Burning only", "Cough and sputum", "Fever and flank pain", "Rash and itching"],
  "Fever and flank pain point to upper tract (kidney) infection rather than cystitis.", "Fever and flank pain."),
 ("¿Qué síntomas distinguen mejor la pielonefritis de la cistitis simple?", ["Solo ardor", "Tos y expectoración", "Fiebre y dolor en flanco (lumbar)", "Exantema y prurito"],
  "La fiebre y el dolor lumbar indican infección alta (renal) más que cistitis.", "Fiebre y dolor lumbar.")),
("30137822", "researcher", 1, "Complicated pyelonephritis includes pregnant patients, patients with uncontrolled diabetes, kidney transplants, urinary anatomical abnormalities",
 ("Which patient has a COMPLICATED pyelonephritis?", ["A healthy non-pregnant young woman", "A pregnant woman", "A healthy man after his first UTI with normal anatomy", "Anyone with fever"],
  "Pregnancy, uncontrolled diabetes, transplants, anatomic abnormalities, kidney failure and immunosuppression make pyelonephritis complicated.", "Pregnancy."),
 ("¿Qué paciente tiene una pielonefritis COMPLICADA?", ["Una mujer joven sana no embarazada", "Una embarazada", "Un hombre sano con anatomía normal en su primera ITU", "Cualquiera con fiebre"],
  "El embarazo, la diabetes descontrolada, el trasplante, las anomalías anatómicas, la insuficiencia renal y la inmunosupresión la hacen complicada.", "Embarazo.")),

# --- CAP (28613500)
("28613500", "explorer", 3, "determining the appropriate level of care is important for improving outcomes",
 ("Beyond diagnosis, what early decision is key in community-acquired pneumonia?", ["Choosing the patient's diet", "Ordering genetic tests", "Scheduling vaccination for next year", "Deciding the appropriate level of care (outpatient, ward or ICU)"],
  "CAP ranges from mild outpatient illness to ICU-level disease; deciding where to treat improves outcomes.", "Level of care."),
 ("Además del diagnóstico, ¿qué decisión temprana es clave en la neumonía adquirida en la comunidad?", ["Elegir la dieta", "Pedir estudios genéticos", "Programar vacunas para el año siguiente", "Decidir el nivel de atención (ambulatorio, sala o UTI)"],
  "La NAC va de cuadros leves ambulatorios a casos de UTI; decidir dónde tratar mejora el pronóstico.", "Nivel de atención.")),

# --- Osteomyelitis (30335283)
("30335283", "beginner", 0, "Bone infection is called osteomyelitis",
 ("What is osteomyelitis?", ["Infection of bone", "Infection of the meninges", "Inflammation of a joint without infection", "A muscle tear"],
  "Osteomyelitis is infection of bone and its structures, usually by pyogenic bacteria.", "Bone infection."),
 ("¿Qué es la osteomielitis?", ["Infección del hueso", "Infección de las meninges", "Inflamación articular sin infección", "Un desgarro muscular"],
  "La osteomielitis es la infección del hueso y sus estructuras, generalmente por bacterias piógenas.", "Infección ósea.")),
("30335283", "researcher", 2, "Before the introduction of penicillin in the 1940s, management of osteomyelitis was mainly surgically",
 ("How was osteomyelitis managed before penicillin became available in the 1940s?", ["With vaccines", "With antifungals", "Mainly surgically, with high mortality from sepsis", "It was never treated"],
  "Before antibiotics, treatment was extensive surgical debridement, with high sepsis mortality; antibiotics greatly improved survival.", "Mainly surgery."),
 ("¿Cómo se trataba la osteomielitis antes de la penicilina (años 40)?", ["Con vacunas", "Con antifúngicos", "Principalmente con cirugía, con alta mortalidad por sepsis", "Nunca se trataba"],
  "Antes de los antibióticos se hacía desbridamiento quirúrgico extenso con alta mortalidad por sepsis; los antibióticos mejoraron mucho la supervivencia.", "Sobre todo cirugía.")),

# --- Septic arthritis (30844203)
("30844203", "curious", 3, "Septic arthritis is usually monoarticular involving one large joint such as the hip or knee",
 ("Which joint pattern is typical of septic arthritis?", ["Symmetric small joints of the hands", "All joints at once", "The spine only", "A single large joint such as the hip or knee"],
  "Septic arthritis is usually monoarticular in a large joint and is an orthopedic emergency.", "One large joint."),
 ("¿Qué patrón articular es típico de la artritis séptica?", ["Pequeñas articulaciones simétricas de las manos", "Todas las articulaciones a la vez", "Solo la columna", "Una sola articulación grande como cadera o rodilla"],
  "La artritis séptica suele ser monoarticular en una articulación grande y es una urgencia ortopédica.", "Una articulación grande.")),

# --- Cellulitis (31747177)
("31747177", "explorer", 1, "Beta-hemolytic streptococci most commonly cause cellulitis, typically group A streptococcus (Streptococcus pyogenes), followed by methicillin-sensitive Staphylococcus aureus",
 ("Which organisms most commonly cause non-purulent cellulitis?", ["Pseudomonas and E. coli", "Beta-hemolytic streptococci (mainly group A), then MSSA", "Candida species", "Anaerobes only"],
  "Cellulitis is usually due to beta-hemolytic streptococci (group A), followed by methicillin-sensitive S. aureus.", "Streptococci, then MSSA."),
 ("¿Qué organismos causan con más frecuencia la celulitis no purulenta?", ["Pseudomonas y E. coli", "Estreptococos betahemolíticos (sobre todo grupo A), luego SAMS", "Especies de Candida", "Solo anaerobios"],
  "La celulitis suele deberse a estreptococos betahemolíticos (grupo A), seguidos de S. aureus sensible a meticilina.", "Estreptococos, luego SAMS.")),
("31747177", "researcher", 0, "Cellulitis is an acute bacterial infection causing inflammation of the deep dermis and surrounding subcutaneous tissue",
 ("Which tissue layers does cellulitis involve?", ["The deep dermis and subcutaneous tissue", "Only the epidermis", "Muscle fascia only", "Bone"],
  "Cellulitis inflames the deep dermis and subcutaneous tissue, without an abscess.", "Deep dermis and subcutis."),
 ("¿Qué capas compromete la celulitis?", ["Dermis profunda y tejido subcutáneo", "Solo la epidermis", "Solo la fascia muscular", "El hueso"],
  "La celulitis inflama la dermis profunda y el tejido subcutáneo, sin absceso.", "Dermis profunda y subcutáneo.")),

# --- Necrotizing fasciitis (28613507)
("28613507", "explorer", 2, "This infection typically travels along the fascial plane, which has a poor blood supply, leaving the overlying tissues initially unaffected, potentially delaying diagnosis",
 ("Why is necrotizing fasciitis often diagnosed late?", ["It only affects bones", "It causes no pain", "It spreads along fascial planes while the overlying skin initially looks normal", "It is always viral"],
  "Infection spreads along poorly vascularized fascia while overlying skin may look unaffected early, delaying surgery.", "Skin looks normal early."),
 ("¿Por qué la fascitis necrotizante suele diagnosticarse tarde?", ["Solo afecta huesos", "No causa dolor", "Se extiende por los planos fasciales mientras la piel parece normal al principio", "Siempre es viral"],
  "La infección avanza por la fascia poco vascularizada y la piel puede verse normal al inicio, retrasando la cirugía.", "Piel normal al inicio.")),

# --- FUO (30335298)
("30335298", "researcher", 3, "FUO was defined as a temperature of 101 degrees Fahrenheit (38.3 degrees Centigrade) or higher with a minimum duration of three weeks",
 ("What was the classic Petersdorf–Beeson definition of fever of unknown origin?", ["Any fever over 37.5 °C", "Fever lasting 3 days", "Fever only in children", "≥38.3 °C for at least 3 weeks without diagnosis after one week of hospital study"],
  "Classic FUO: ≥38.3 °C for ≥3 weeks, undiagnosed after a week of hospital investigation; later revised into four subclasses.", "≥38.3 °C, ≥3 weeks."),
 ("¿Cuál era la definición clásica de Petersdorf y Beeson de fiebre de origen desconocido?", ["Cualquier fiebre mayor de 37,5 °C", "Fiebre de 3 días", "Fiebre solo en niños", "≥38,3 °C durante al menos 3 semanas sin diagnóstico tras una semana de estudio hospitalario"],
  "FOD clásica: ≥38,3 °C por ≥3 semanas, sin diagnóstico tras una semana de estudio; luego se revisó en cuatro subclases.", "≥38,3 °C, ≥3 semanas.")),
("30335298", "expert", 1, "Despite extensive workup and diagnostic advances, up to 51% of FUO cases remain undiagnosed",
 ("What fraction of fever-of-unknown-origin cases may remain undiagnosed despite workup?", ["Almost none", "Up to about half", "Exactly 10%", "All of them"],
  "Up to 51% of FUO cases remain undiagnosed despite extensive evaluation.", "Up to ~51%."),
 ("¿Qué fracción de los casos de fiebre de origen desconocido puede quedar sin diagnóstico pese al estudio?", ["Casi ninguno", "Hasta aproximadamente la mitad", "Exactamente 10%", "Todos"],
  "Hasta el 51% de las FOD quedan sin diagnóstico pese a una evaluación extensa.", "Hasta ~51%.")),

# --- CLABSI (28613641)
("28613641", "explorer", 0, "Most cases are preventable with proper aseptic techniques, surveillance, and management strategies",
 ("Which statement about central line–associated bloodstream infections is correct?", ["Most are preventable with aseptic technique and surveillance", "They are unavoidable", "They are caused only by viruses", "They are cheap to treat"],
  "CLABSIs are costly (~$46,000/case) but mostly preventable with asepsis, surveillance and good line management.", "Mostly preventable."),
 ("¿Qué afirmación sobre las bacteriemias asociadas a catéter central es correcta?", ["La mayoría son prevenibles con técnica aséptica y vigilancia", "Son inevitables", "Solo las causan virus", "Son baratas de tratar"],
  "Las BAC son costosas (~USD 46.000/caso) pero mayormente prevenibles con asepsia, vigilancia y buen manejo del catéter.", "Mayormente prevenibles.")),

# --- TSS (29083727)
("29083727", "explorer", 3, "Toxic shock syndrome (TSS) is an acute-onset illness characterized by fever, hypotension, sunburn-like rash, and end-organ damage",
 ("Which findings characterize toxic shock syndrome?", ["Slow weight loss and night sweats", "Painless genital ulcer", "Facial palsy", "Fever, hypotension, sunburn-like rash and organ damage"],
  "TSS presents acutely with fever, hypotension, a sunburn-like rash and end-organ dysfunction.", "Fever, hypotension, rash."),
 ("¿Qué hallazgos caracterizan al síndrome de shock tóxico?", ["Pérdida de peso lenta y sudores nocturnos", "Úlcera genital indolora", "Parálisis facial", "Fiebre, hipotensión, exantema tipo quemadura solar y daño orgánico"],
  "El SST se presenta de forma aguda con fiebre, hipotensión, exantema tipo quemadura solar y disfunción orgánica.", "Fiebre, hipotensión, exantema.")),
("29083727", "researcher", 2, "TSS was classically associated with high absorbency tampon use in menstruating women",
 ("With what was toxic shock syndrome classically associated?", ["Raw milk", "Tick bites", "High-absorbency tampon use", "Contact lenses"],
  "Classic TSS was linked to high-absorbency tampons; non-menstrual cases are now also recognized.", "High-absorbency tampons."),
 ("¿Con qué se asoció clásicamente el síndrome de shock tóxico?", ["Leche cruda", "Picaduras de garrapata", "Uso de tampones de alta absorción", "Lentes de contacto"],
  "El SST clásico se vinculó a tampones de alta absorción; hoy también se reconocen casos no menstruales.", "Tampones de alta absorción.")),

# --- Septic shock (28613689)
("28613689", "researcher", 0, "early identification remains the best therapeutic tool for sepsis treatment and management",
 ("According to sepsis care principles, what is the best therapeutic tool?", ["Early identification", "Waiting for culture results before acting", "Steroids for everyone", "Avoiding antibiotics"],
  "Early antimicrobials and bundles help, but early identification remains the best tool against sepsis.", "Early identification."),
 ("Según los principios del manejo de la sepsis, ¿cuál es la mejor herramienta terapéutica?", ["La identificación temprana", "Esperar los cultivos antes de actuar", "Corticoides para todos", "Evitar antibióticos"],
  "Los antibióticos tempranos y los paquetes de medidas ayudan, pero la identificación temprana es la mejor herramienta.", "Identificación temprana.")),
("28613689", "expert", 1, "the endothelium not only suffers microvascular injury but also activates the coagulation and complement cascades, which further exacerbate vascular injury, leading to capillary leak",
 ("In septic shock pathophysiology, which structure is the primary site of the response leading to capillary leak?", ["Bone marrow", "The endothelium", "Skeletal muscle", "The thyroid"],
  "The endothelium suffers microvascular injury and activates coagulation and complement, causing capillary leak and shock.", "Endothelium."),
 ("En la fisiopatología del shock séptico, ¿qué estructura es el sitio principal de la respuesta que causa fuga capilar?", ["Médula ósea", "El endotelio", "Músculo esquelético", "La tiroides"],
  "El endotelio sufre daño microvascular y activa la coagulación y el complemento, causando fuga capilar y shock.", "Endotelio.")),

# --- Sepsis (30725739)
("30725739", "curious", 2, "Sepsis has recently been re-defined as life-threatening organ dysfunction caused by a dysregulated host response to infection",
 ("How is sepsis currently defined (Sepsis-3)?", ["Any positive blood culture", "Fever above 38 °C", "Life-threatening organ dysfunction caused by a dysregulated host response to infection", "Infection of the blood by fungi only"],
  "Sepsis-3: life-threatening organ dysfunction from a dysregulated host response to infection.", "Organ dysfunction from dysregulated response."),
 ("¿Cómo se define hoy la sepsis (Sepsis-3)?", ["Cualquier hemocultivo positivo", "Fiebre mayor de 38 °C", "Disfunción orgánica potencialmente mortal causada por una respuesta desregulada del huésped a la infección", "Infección de la sangre solo por hongos"],
  "Sepsis-3: disfunción orgánica potencialmente mortal por una respuesta desregulada del huésped a la infección.", "Disfunción orgánica por respuesta desregulada.")),
("30725739", "explorer", 0, "derived from the Greek word sipsi",
 ("What does the Greek root of the word \"sepsis\" mean?", ["To make rotten", "Blood", "Heat", "Shock"],
  "Hippocrates introduced \"sepsis\", from a Greek word meaning \"to make rotten\".", "To make rotten."),
 ("¿Qué significa la raíz griega de la palabra \"sepsis\"?", ["Pudrir", "Sangre", "Calor", "Choque"],
  "Hipócrates introdujo \"sepsis\", de una palabra griega que significa \"pudrir\".", "Pudrir.")),
("30725739", "expert", 3, "Septic Shock:  Sepsis-induced hypotension despite adequate fluid resuscitation",
 ("In the classic consensus definitions, what defines septic shock?", ["Fever with chills", "Any tachycardia", "Lactate below 1", "Sepsis-induced hypotension despite adequate fluid resuscitation"],
  "Septic shock is sepsis with hypotension that persists despite adequate fluid resuscitation.", "Hypotension despite fluids."),
 ("En las definiciones de consenso clásicas, ¿qué define al shock séptico?", ["Fiebre con escalofríos", "Cualquier taquicardia", "Lactato menor de 1", "Hipotensión inducida por sepsis pese a una reanimación con fluidos adecuada"],
  "El shock séptico es sepsis con hipotensión que persiste pese a una reanimación adecuada con fluidos.", "Hipotensión pese a fluidos.")),

# --- Brain abscess (28722871)
("28722871", "researcher", 1, "brain abscesses often arise from local infections in areas such as the ear, teeth, sinuses, mastoid air cells, or epidural spaces",
 ("From where do brain abscesses most often arise?", ["Urinary tract infections", "Contiguous infections of the ear, teeth, sinuses or mastoid", "Skin infections of the feet", "Eye drops"],
  "Brain abscesses often spread from nearby ear, dental, sinus or mastoid infections, or hematogenously from lungs or heart.", "Contiguous head infections."),
 ("¿De dónde surgen con más frecuencia los abscesos cerebrales?", ["Infecciones urinarias", "Infecciones contiguas de oído, dientes, senos paranasales o mastoides", "Infecciones de piel de los pies", "Colirios"],
  "Los abscesos cerebrales suelen extenderse desde infecciones cercanas de oído, dientes, senos o mastoides, o por vía hematógena desde pulmón o corazón.", "Infecciones contiguas.")),

# --- PID (29763134)
("29763134", "explorer", 0, "Pelvic inflammatory disease is treated with antibiotics that cover its primary pathogens, including Neisseria gonorrhoeae and Chlamydia trachomatis",
 ("Which pathogens must antibiotic regimens for pelvic inflammatory disease cover?", ["Neisseria gonorrhoeae and Chlamydia trachomatis", "Candida and Trichomonas only", "Influenza and RSV", "Plasmodium species"],
  "PID is usually an ascending STI; treatment covers N. gonorrhoeae and C. trachomatis.", "Gonococcus and chlamydia."),
 ("¿Qué patógenos debe cubrir el tratamiento de la enfermedad pélvica inflamatoria?", ["Neisseria gonorrhoeae y Chlamydia trachomatis", "Solo Candida y Trichomonas", "Influenza y VSR", "Especies de Plasmodium"],
  "La EPI suele ser una ITS ascendente; el tratamiento cubre N. gonorrhoeae y C. trachomatis.", "Gonococo y clamidia.")),
("29763134", "researcher", 3, "long-term complications include ectopic pregnancy, infertility, and chronic pelvic pain",
 ("Which are long-term complications of pelvic inflammatory disease?", ["Cataracts", "Kidney stones", "Osteoporosis", "Ectopic pregnancy, infertility and chronic pelvic pain"],
  "Tubal damage from PID can cause ectopic pregnancy, infertility and chronic pelvic pain.", "Ectopic pregnancy, infertility."),
 ("¿Cuáles son complicaciones a largo plazo de la enfermedad pélvica inflamatoria?", ["Cataratas", "Cálculos renales", "Osteoporosis", "Embarazo ectópico, infertilidad y dolor pélvico crónico"],
  "El daño tubario por EPI puede causar embarazo ectópico, infertilidad y dolor pélvico crónico.", "Ectópico, infertilidad.")),

# --- Bacterial vaginosis (29083654)
("29083654", "explorer", 2, "Previously, bacterial vaginosis was known as Gardnerella vaginitis",
 ("Why was \"Gardnerella vaginitis\" renamed \"bacterial vaginosis\"?", ["Because it is caused by a virus", "Because it is a fungal infection", "Because it reflects overgrowth of various anaerobes, not Gardnerella alone", "Because it only affects men"],
  "BV reflects overgrowth of multiple anaerobes in the vaginal ecosystem, not a single organism.", "Polymicrobial anaerobic overgrowth."),
 ("¿Por qué la \"vaginitis por Gardnerella\" pasó a llamarse \"vaginosis bacteriana\"?", ["Porque la causa un virus", "Porque es una micosis", "Porque refleja sobrecrecimiento de varios anaerobios, no solo Gardnerella", "Porque solo afecta a hombres"],
  "La VB refleja el sobrecrecimiento de múltiples anaerobios del ecosistema vaginal, no de un solo organismo.", "Sobrecrecimiento polimicrobiano.")),

# --- Liver abscess (30855818)
("30855818", "explorer", 1, "The majority of these abscesses are categorized into pyogenic or amoebic",
 ("How are most liver abscesses classified?", ["Viral or prion", "Pyogenic or amoebic", "Allergic or toxic", "Congenital or traumatic"],
  "Most liver abscesses are pyogenic (often polymicrobial) or amoebic (Entamoeba histolytica).", "Pyogenic or amoebic."),
 ("¿Cómo se clasifican la mayoría de los abscesos hepáticos?", ["Virales o priónicos", "Piógenos o amebianos", "Alérgicos o tóxicos", "Congénitos o traumáticos"],
  "La mayoría de los abscesos hepáticos son piógenos (a menudo polimicrobianos) o amebianos (Entamoeba histolytica).", "Piógenos o amebianos.")),

# --- Travelers' diarrhea (29083755)
("29083755", "curious", 3, "Travelers' diarrhea is the most predictable travel-related illness",
 ("What is the most predictable travel-related illness?", ["Malaria", "Altitude sickness", "Jet lag", "Travelers' diarrhea"],
  "Travelers' diarrhea affects 10–70% of international travelers depending on destination; most cases are bacterial.", "Travelers' diarrhea."),
 ("¿Cuál es la enfermedad más predecible relacionada con viajes?", ["Malaria", "Mal de altura", "Jet lag", "Diarrea del viajero"],
  "La diarrea del viajero afecta al 10–70% de los viajeros según el destino; la mayoría es bacteriana.", "Diarrea del viajero.")),
("29083755", "researcher", 0, "with bacterial agents accounting for an estimated 80% to 90% of cases",
 ("What proportion of travelers' diarrhea is caused by bacteria?", ["About 80–90%", "About 5%", "About 30%", "None"],
  "Bacteria (e.g., enterotoxigenic E. coli) cause an estimated 80–90% of travelers' diarrhea.", "80–90%."),
 ("¿Qué proporción de la diarrea del viajero es bacteriana?", ["Alrededor del 80–90%", "Alrededor del 5%", "Alrededor del 30%", "Ninguna"],
  "Las bacterias (p. ej., E. coli enterotoxigénica) causan aproximadamente el 80–90% de la diarrea del viajero.", "80–90%.")),

# --- HAIs (32644738)
("32644738", "beginner", 1, "are acquired during healthcare delivery and are not present at the time of admission",
 ("What is a nosocomial (healthcare-associated) infection?", ["An infection present before admission", "An infection acquired during healthcare that was not present at admission", "Any viral infection", "An inherited disease"],
  "HAIs are acquired during healthcare and absent at admission; they are the most common adverse events in healthcare.", "Acquired during care."),
 ("¿Qué es una infección nosocomial (asociada a la atención de salud)?", ["Una infección presente antes de la internación", "Una infección adquirida durante la atención que no estaba al ingreso", "Cualquier infección viral", "Una enfermedad hereditaria"],
  "Las IAAS se adquieren durante la atención y no estaban al ingreso; son los eventos adversos más comunes en salud.", "Adquirida durante la atención.")),
("32644738", "curious", 2, "Risk factors include invasive procedures, surgeries, indwelling medical devices, and prosthetic implants",
 ("Which is a major risk factor for healthcare-associated infections?", ["Eating fruit", "Wearing glasses", "Indwelling medical devices such as catheters", "Being vaccinated"],
  "Invasive procedures, surgery, indwelling devices and implants increase HAI risk.", "Indwelling devices."),
 ("¿Cuál es un factor de riesgo importante de infecciones asociadas a la atención?", ["Comer fruta", "Usar anteojos", "Dispositivos permanentes como catéteres", "Estar vacunado"],
  "Los procedimientos invasivos, la cirugía, los dispositivos permanentes y los implantes aumentan el riesgo de IAAS.", "Dispositivos permanentes.")),

# --- Hand hygiene (29262113)
("29262113", "beginner", 3, "Hand hygiene is the most critical intervention for patient safety",
 ("What is the single most important intervention to prevent healthcare-associated infections?", ["Wearing a mask always", "Giving antibiotics to all patients", "Keeping windows closed", "Hand hygiene"],
  "Contaminated hands are the main source of HAIs; hand hygiene is the cornerstone of infection prevention.", "Hand hygiene."),
 ("¿Cuál es la intervención más importante para prevenir infecciones asociadas a la atención?", ["Usar siempre barbijo", "Dar antibióticos a todos", "Mantener ventanas cerradas", "La higiene de manos"],
  "Las manos contaminadas son la principal fuente de IAAS; la higiene de manos es la piedra angular de la prevención.", "Higiene de manos.")),
("29262113", "explorer", 0, "evidence-based infection control could prevent up to 70% of HAIs",
 ("Approximately what proportion of healthcare-associated infections could evidence-based infection control prevent?", ["Up to 70%", "Less than 1%", "Exactly 10%", "None"],
  "Evidence-based infection control could prevent up to 70% of HAIs, yet compliance with hand hygiene remains low.", "Up to 70%."),
 ("¿Qué proporción aproximada de las IAAS podría prevenir el control de infecciones basado en evidencia?", ["Hasta el 70%", "Menos del 1%", "Exactamente 10%", "Ninguna"],
  "El control de infecciones basado en evidencia podría prevenir hasta el 70% de las IAAS, pero la adherencia a la higiene de manos sigue baja.", "Hasta 70%.")),

# --- HIV OIs (30969609)
("30969609", "researcher", 2, "Opportunistic infections typically emerge when the absolute CD4+ count falls below 200 cells/mm³",
 ("Below which CD4+ count do opportunistic infections typically emerge in HIV?", ["1000 cells/mm³", "500 cells/mm³", "200 cells/mm³", "50,000 cells/mm³"],
  "Opportunistic infections typically appear when CD4+ falls below 200/mm³ (or <14%).", "200 cells/mm³."),
 ("¿Por debajo de qué recuento de CD4+ aparecen típicamente las infecciones oportunistas en el VIH?", ["1000 células/mm³", "500 células/mm³", "200 células/mm³", "50.000 células/mm³"],
  "Las infecciones oportunistas aparecen típicamente cuando los CD4+ caen por debajo de 200/mm³ (o <14%).", "200 células/mm³.")),
("30969609", "curious", 1, "certain infections that rarely cause disease in immunocompetent hosts",
 ("What is an opportunistic infection?", ["An infection acquired while traveling", "An infection that rarely causes disease in immunocompetent hosts but does in immunocompromised ones", "Any infection treated with antibiotics", "An infection from pets only"],
  "Opportunistic pathogens exploit immune compromise (e.g., low CD4+) to cause disease rarely seen in healthy hosts.", "Exploits immunodeficiency."),
 ("¿Qué es una infección oportunista?", ["Una infección adquirida al viajar", "Una infección que rara vez enferma a inmunocompetentes pero sí a inmunocomprometidos", "Cualquier infección tratada con antibióticos", "Una infección solo por mascotas"],
  "Los patógenos oportunistas aprovechan la inmunodepresión (p. ej., CD4+ bajos) para causar enfermedad rara en personas sanas.", "Aprovecha la inmunodeficiencia.")),
]
