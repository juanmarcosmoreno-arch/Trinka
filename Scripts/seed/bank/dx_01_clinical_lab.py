# Clinical laboratory I — eGFR CKD-EPI 2021, natriuretic peptides, D-dimer strategies (Wells, YEARS,
# ADJUST-PE), procalcitonin trials, blood cultures (number, contamination, time to positivity),
# hs-troponin 0/1h and point-of-care, laboratory errors and hemolysis, LDL estimation, urinalysis and
# urine culture, MALDI-TOF, rapid PCR panels, EUCAST RAST, pseudohyperkalemia, ESR/CRP, RET-He, HbA1c,
# smear review, ALT reference limits, aPTT vs anti-Xa, quality control.
# Sources: PubMed paper and review abstracts. Excerpts verbatim.
CATEGORY = "diagnosticMethods"
Q = [
# --- CKD-EPI 2021 race-free eGFR (34554658)
("34554658", "curious", 0, "race in eGFR equations is a social and not a biologic construct",
 ("Why did the 2021 CKD-EPI investigators develop new eGFR equations without a race term?", ["Race is a social, not biologic, construct", "Race had no effect on creatinine at all", "Cystatin C cannot be measured in Black people", "Regulators banned age and sex terms"],
  "The authors argued that race is a social construct, so they rebuilt the creatinine and cystatin C equations without it.", "Race is social."),
 ("¿Por qué los investigadores de CKD-EPI 2021 desarrollaron nuevas ecuaciones de TFGe sin el término de raza?", ["La raza es un constructo social, no biológico", "La raza no afectaba en nada a la creatinina", "La cistatina C no se mide en personas negras", "Los reguladores prohibieron la edad y el sexo"],
  "Los autores sostuvieron que la raza es un constructo social, así que rehicieron las ecuaciones de creatinina y cistatina C sin ella.", "La raza es social.")),
("34554658", "researcher", 1, "New creatinine-cystatin C equations without race were more accurate than new creatinine equations",
 ("In the 2021 CKD-EPI validation, which race-free equation estimated measured GFR most accurately?", ["Creatinine alone", "Creatinine plus cystatin C", "Cystatin C alone", "Urea plus creatinine clearance"],
  "Combining creatinine and cystatin C was more accurate and reduced differences between Black and non-Black participants.", "Creatinine + cystatin C."),
 ("En la validación de CKD-EPI 2021, ¿qué ecuación sin raza estimó la TFG medida con más exactitud?", ["Solo creatinina", "Creatinina más cistatina C", "Solo cistatina C", "Urea más aclaramiento de creatinina"],
  "Combinar creatinina y cistatina C fue más exacto y redujo las diferencias entre participantes negros y no negros.", "Creatinina + cistatina C.")),
("34554658", "expert", 2, "When the adjustment for Black race was omitted from the current eGFR equation, measured GFR in Blacks was underestimated (median, 7.1 ml per minute per 1.73 m2",
 ("In the CKD-EPI 2021 paper, what happened when the Black-race coefficient was simply dropped from the old creatinine equation?", ["It overestimated GFR by about 7 mL/min", "It became exact in all race and age groups", "It underestimated GFR by about 7 mL/min", "It only changed results in children"],
  "Just deleting the coefficient underestimated measured GFR in Black participants by a median of 7.1 mL/min/1.73 m2, so a refit was needed.", "Underestimated GFR."),
 ("En el artículo de CKD-EPI 2021, ¿qué pasó al quitar sin más el coeficiente de raza negra de la ecuación de creatinina previa?", ["Sobrestimó la TFG en unos 7 mL/min", "Se volvió exacta en todos los grupos", "Subestimó la TFG en unos 7 mL/min", "Solo cambió los resultados en niños"],
  "Borrar el coeficiente subestimó la TFG medida en participantes negros en una mediana de 7,1 mL/min/1,73 m2, por lo que hubo que reajustar.", "Subestimó la TFG.")),

# --- Breathing Not Properly: BNP (12124404)
("12124404", "explorer", 3, "The diagnostic accuracy of B-type natriuretic peptide at a cutoff of 100 pg per milliliter was 83.4 percent",
 ("In the Breathing Not Properly study of acute dyspnea, what was the diagnostic accuracy of bedside BNP at a 100 pg/mL cutoff?", ["About 55%", "About 99%", "About 65%", "About 83%"],
  "At 100 pg/mL, BNP correctly classified heart failure in 83.4% of 1586 emergency patients with dyspnea.", "83.4%."),
 ("En el estudio Breathing Not Properly sobre disnea aguda, ¿qué exactitud diagnóstica tuvo el BNP a la cabecera con un corte de 100 pg/mL?", ["Cerca del 55%", "Cerca del 99%", "Cerca del 65%", "Cerca del 83%"],
  "Con 100 pg/mL, el BNP clasificó bien la insuficiencia cardíaca en el 83,4% de 1586 pacientes de urgencias con disnea.", "83,4%.")),
("12124404", "researcher", 0, "The negative predictive value of B-type natriuretic peptide at levels of less than 50 pg per milliliter was 96 percent",
 ("In emergency patients with dyspnea, what negative predictive value did a BNP below 50 pg/mL have for heart failure?", ["96%", "50%", "71%", "100% in all subgroups"],
  "Very low BNP made heart failure unlikely, with a negative predictive value of 96%.", "96%."),
 ("En pacientes de urgencias con disnea, ¿qué valor predictivo negativo tuvo un BNP menor de 50 pg/mL para insuficiencia cardíaca?", ["96%", "50%", "71%", "100% en todos los subgrupos"],
  "Un BNP muy bajo hacía improbable la insuficiencia cardíaca, con un valor predictivo negativo del 96%.", "96%.")),

# --- D-dimer and DVT (14507948)
("14507948", "explorer", 1, "Two hundred eighteen patients (39 percent) in the D-dimer group did not require ultrasound imaging",
 ("In the randomized trial of D-dimer testing for suspected deep-vein thrombosis, what share of the D-dimer group avoided ultrasound?", ["About 5%", "About 39%", "About 90%", "None of them"],
  "Adding D-dimer to clinical probability spared ultrasound in 39% of patients without more missed clots.", "39%."),
 ("En el ensayo aleatorizado del dímero D ante sospecha de trombosis venosa profunda, ¿qué proporción del grupo dímero D evitó la ecografía?", ["Cerca del 5%", "Cerca del 39%", "Cerca del 90%", "Ninguno"],
  "Sumar el dímero D a la probabilidad clínica evitó la ecografía en el 39% sin más trombos no detectados.", "39%.")),
("14507948", "curious", 2, "Deep-vein thrombosis can be ruled out in a patient who is judged clinically unlikely to have deep-vein thrombosis and who has a negative D-dimer test",
 ("According to the Wells D-dimer trial, which outpatients with suspected DVT can safely skip ultrasound?", ["Anyone with a positive D-dimer", "All patients older than 40", "Clinically unlikely, negative D-dimer", "Patients with a swollen calf and no fever"],
  "Low clinical probability plus a negative D-dimer safely excludes DVT without imaging.", "Unlikely + negative D-dimer."),
 ("Según el ensayo de Wells con dímero D, ¿qué pacientes ambulatorios con sospecha de TVP pueden omitir la ecografía?", ["Cualquiera con dímero D positivo", "Todos los mayores de 40 años", "Probabilidad baja y dímero D negativo", "Solo quienes tienen la pantorrilla hinchada"],
  "Una probabilidad clínica baja más un dímero D negativo excluye la TVP sin imágenes.", "Baja probabilidad + dímero D negativo.")),

# --- YEARS algorithm (28549662)
("28549662", "researcher", 3, "In patients without YEARS items and D-dimer less than 1000 ng/mL",
 ("In the YEARS algorithm for suspected pulmonary embolism, which D-dimer threshold excludes PE when no YEARS items are present?", ["Below 250 ng/mL", "Below 500 ng/mL", "Below 5000 ng/mL", "Below 1000 ng/mL"],
  "Without YEARS items the cutoff is 1000 ng/mL; with one or more items it drops to 500 ng/mL.", "1000 ng/mL."),
 ("En el algoritmo YEARS para sospecha de embolia pulmonar, ¿qué umbral de dímero D excluye la EP si no hay ítems YEARS?", ["Menos de 250 ng/mL", "Menos de 500 ng/mL", "Menos de 5000 ng/mL", "Menos de 1000 ng/mL"],
  "Sin ítems YEARS el corte es 1000 ng/mL; con uno o más ítems baja a 500 ng/mL.", "1000 ng/mL.")),
("28549662", "explorer", 0, "the absolute 14% decrease of CTPA examinations in all ages",
 ("What was the main advantage of the YEARS algorithm over Wells' rule with a fixed D-dimer cutoff?", ["14% fewer CT angiograms", "Twice as many PEs detected", "No need for any blood tests", "Fewer deaths from cancer"],
  "YEARS avoided CTPA in 48% versus 34% of patients, an absolute 14% reduction across ages.", "Fewer CTPAs."),
 ("¿Cuál fue la principal ventaja del algoritmo YEARS frente a la regla de Wells con un corte fijo de dímero D?", ["14% menos angiotomografías", "El doble de EP detectadas", "No requerir análisis de sangre", "Menos muertes por cáncer"],
  "YEARS evitó la angio-TC en el 48% frente al 34% de los pacientes, una reducción absoluta del 14% en todas las edades.", "Menos angio-TC.")),

# --- ADJUST-PE (24643601)
("24643601", "explorer", 1, "an age-adjusted D-dimer cutoff, defined as age × 10 in patients 50 years or older",
 ("How did the ADJUST-PE study define the age-adjusted D-dimer cutoff (µg/L) for patients aged 50 or older?", ["Age plus 500", "Age × 10", "Age × 100", "Age divided by 2"],
  "A 75-year-old, for example, would have a cutoff of 750 µg/L instead of the fixed 500 µg/L.", "Age × 10."),
 ("¿Cómo definió el estudio ADJUST-PE el corte de dímero D ajustado por edad (µg/L) para pacientes de 50 años o más?", ["Edad más 500", "Edad × 10", "Edad × 100", "Edad dividida por 2"],
  "Por ejemplo, a los 75 años el corte sería 750 µg/L en lugar del fijo de 500 µg/L.", "Edad × 10.")),
("24643601", "researcher", 2, "increased the proportion of patients in whom PE could be excluded on the basis of D-dimer from 43 of 673 patients (6.4%",
 ("In ADJUST-PE patients aged 75 or older with nonhigh probability, how did the age-adjusted cutoff change PE exclusion by D-dimer?", ["From 30% down to 6%", "No change in the exclusion rate", "From 6% up to about 30%", "From 6% up to about 90%"],
  "Exclusion rose from 6.4% to 29.7% of elderly patients, without additional false negatives.", "6% → 30%."),
 ("En ADJUST-PE, en pacientes de 75 años o más sin probabilidad alta, ¿cómo cambió el corte ajustado la exclusión de EP por dímero D?", ["Bajó del 30% al 6%", "No cambió en absoluto", "Subió del 6% a cerca del 30%", "Subió del 6% a cerca del 90%"],
  "La exclusión subió del 6,4% al 29,7% de los ancianos, sin falsos negativos adicionales.", "Del 6% al 30%.")),

# --- SAPS procalcitonin ICU trial (26947523)
("26947523", "researcher", 3, "if procalcitonin concentration had decreased by 80% or more of its peak value",
 ("In the Dutch SAPS ICU trial, when was stopping antibiotics advised in the procalcitonin-guided arm?", ["When PCT rose above 2 μg/L", "When PCT doubled from its baseline value", "After exactly 14 days", "When PCT fell 80% from its peak"],
  "Discontinuation was advised when PCT fell by at least 80% from peak or to 0.5 μg/L or lower.", "80% fall from peak."),
 ("En el ensayo neerlandés SAPS en UCI, ¿cuándo se aconsejaba suspender antibióticos en el brazo guiado por procalcitonina?", ["Cuando la PCT superaba 2 μg/L", "Cuando la PCT se duplicaba", "Tras exactamente 14 días", "Cuando la PCT caía 80% del pico"],
  "Se aconsejaba suspender si la PCT bajaba al menos un 80% desde el pico o a 0,5 μg/L o menos.", "Caída del 80% del pico.")),
("26947523", "expert", 0, "Mortality at 28 days was 149 (20%) of 761 patients in the procalcitonin-guided group and 196 (25%) of 785 patients",
 ("What happened to 28-day mortality in the SAPS procalcitonin-guided group of critically ill patients?", ["It was lower, 20% vs 25%", "It was higher, 25% vs 20%", "It was identical in both arms", "It could not be measured"],
  "Shorter antibiotic courses guided by PCT were accompanied by significantly lower 28-day mortality.", "Lower mortality."),
 ("¿Qué pasó con la mortalidad a 28 días en el grupo guiado por procalcitonina del ensayo SAPS en pacientes críticos?", ["Fue menor, 20% vs 25%", "Fue mayor, 25% vs 20%", "Fue idéntica en ambos brazos", "No se pudo medir"],
  "Los tratamientos más cortos guiados por PCT se acompañaron de una mortalidad a 28 días significativamente menor.", "Menor mortalidad.")),

# --- ProHOSP (19738090)
("19738090", "explorer", 1, "The mean duration of antibiotics exposure in the PCT vs control groups was lower in all patients (5.7 vs 8.7 days",
 ("In the ProHOSP trial of lower respiratory tract infections, how long was mean antibiotic exposure with procalcitonin guidance versus control?", ["8.7 vs 5.7 days", "5.7 vs 8.7 days", "10 vs 10 days", "1 vs 14 days"],
  "PCT guidance cut antibiotic exposure by about 35% with similar adverse outcomes.", "5.7 vs 8.7 days."),
 ("En el ensayo ProHOSP de infecciones respiratorias bajas, ¿cuánto duró en promedio la exposición antibiótica con procalcitonina frente al control?", ["8,7 vs 5,7 días", "5,7 vs 8,7 días", "10 vs 10 días", "1 vs 14 días"],
  "Guiarse por PCT redujo la exposición antibiótica cerca de un 35% con desenlaces adversos similares.", "5,7 vs 8,7 días.")),
("19738090", "researcher", 2, "Antibiotic-associated adverse effects were less frequent in the PCT group (19.8% [n = 133] vs 28.1% [n = 193]",
 ("Besides shorter courses, what other benefit did procalcitonin guidance show in ProHOSP?", ["Higher pneumonia cure rates", "Faster resolution on chest X-rays", "Fewer antibiotic side effects", "Lower rates of influenza"],
  "Antibiotic-associated adverse effects fell from 28.1% to 19.8%.", "Fewer side effects."),
 ("Además de tratamientos más cortos, ¿qué otro beneficio mostró la guía por procalcitonina en ProHOSP?", ["Más curación de neumonía", "Radiografías torácicas normalizadas antes", "Menos efectos adversos de antibióticos", "Menos casos de influenza"],
  "Los efectos adversos asociados a antibióticos bajaron del 28,1% al 19,8%.", "Menos efectos adversos.")),

# --- How many blood cultures (17881544)
("17881544", "explorer", 3, "two blood cultures in a 24-h period will detect approximately 90% of bloodstream infections in adults",
 ("According to the Duke and Robert Wood Johnson review, what share of adult bloodstream infections do two blood cultures in 24 h detect?", ["About 50%", "About 70%", "Virtually 100%", "About 90%"],
  "Two cultures caught about 90% of episodes; the old axiom of near-total detection may not hold.", "About 90%."),
 ("Según la revisión de Duke y Robert Wood Johnson, ¿qué proporción de bacteriemias en adultos detectan dos hemocultivos en 24 h?", ["Cerca del 50%", "Cerca del 70%", "Prácticamente el 100%", "Cerca del 90%"],
  "Dos hemocultivos detectaron cerca del 90% de los episodios; la vieja idea de detección casi total no se sostiene.", "Cerca del 90%.")),
("17881544", "researcher", 0, "To achieve a detection rate of >99%, as many as four blood cultures may be needed",
 ("How many blood cultures in 24 h may be needed to detect more than 99% of adult bloodstream infections?", ["Up to four", "Just one", "Two at most", "At least ten"],
  "Cumulative sensitivity reached 99.8% only with the first four cultures.", "Up to four."),
 ("¿Cuántos hemocultivos en 24 h pueden necesitarse para detectar más del 99% de las bacteriemias en adultos?", ["Hasta cuatro", "Solo uno", "Dos como máximo", "Al menos diez"],
  "La sensibilidad acumulada llegó al 99,8% solo con los primeros cuatro hemocultivos.", "Hasta cuatro.")),

# --- ESC 0/1h hs-troponin meta-analysis (32597681)
("32597681", "researcher", 1, "Summary sensitivity and specificity in diagnosing AMI were 99% (95% CI 98-99%; I2 63%) and 91%",
 ("In a meta-analysis of the ESC 0/1-hour high-sensitivity troponin algorithm, what were pooled sensitivity and specificity for myocardial infarction?", ["91% and 99%", "99% and 91%", "75% and 75%", "60% and 99%"],
  "Across 11 studies and 19,213 patients, sensitivity was 99% and specificity 91%.", "99% / 91%."),
 ("En un metaanálisis del algoritmo 0/1 h de la ESC con troponina de alta sensibilidad, ¿cuáles fueron la sensibilidad y especificidad combinadas para infarto?", ["91% y 99%", "99% y 91%", "75% y 75%", "60% y 99%"],
  "En 11 estudios y 19.213 pacientes, la sensibilidad fue del 99% y la especificidad del 91%.", "99% / 91%.")),
("32597681", "expert", 2, "Cumulative all-cause mortality at 30 days in the rule-out group was 0.11%",
 ("In the 0/1-hour hs-troponin meta-analysis, what was 30-day all-cause mortality among patients assigned to rule-out?", ["About 5%", "About 2.8%", "About 0.1%", "About 10%"],
  "Mortality was 0.11% after rule-out versus 2.8% in the rule-in group, supporting safe early discharge.", "0.11%."),
 ("En el metaanálisis de troponina de alta sensibilidad 0/1 h, ¿cuál fue la mortalidad total a 30 días en los pacientes descartados?", ["Cerca del 5%", "Cerca del 2,8%", "Cerca del 0,1%", "Cerca del 10%"],
  "La mortalidad fue del 0,11% tras el descarte frente al 2,8% en el grupo de confirmación, lo que avala el alta precoz.", "0,11%.")),

# --- WESTCOR point-of-care troponin RCT (40202469)
("40202469", "researcher", 3, "resulting in a reduction in median LOS of 6 minutes",
 ("In the WESTCOR randomized trial, how much did point-of-care hs-troponin I with a 0/1-hour algorithm shorten emergency department stay?", ["By about 2 hours", "By about 1 hour", "By about 45 minutes", "By about 6 minutes"],
  "Median stay fell by just 6 minutes, below the 15-minute threshold judged clinically meaningful.", "About 6 minutes."),
 ("En el ensayo aleatorizado WESTCOR, ¿cuánto acortó la estadía en urgencias la troponina I de alta sensibilidad en el punto de atención con algoritmo 0/1 h?", ["Unas 2 horas", "Cerca de 1 hora", "Unos 45 minutos", "Unos 6 minutos"],
  "La mediana bajó solo 6 minutos, por debajo de los 15 minutos considerados clínicamente relevantes.", "Unos 6 minutos.")),

# --- Errors in a stat laboratory (17525103)
("17525103", "beginner", 0, "61.9% were preanalytical errors, 15% were analytical, and 23.1% were postanalytical",
 ("In the Padua stat laboratory study, in which phase of testing did most confirmed laboratory errors occur?", ["Preanalytical", "Analytical", "Postanalytical", "Equally in all phases"],
  "About 62% of errors were preanalytical, 23% postanalytical and only 15% analytical.", "Preanalytical."),
 ("En el estudio del laboratorio de urgencias de Padua, ¿en qué fase del proceso ocurrieron la mayoría de los errores confirmados?", ["Preanalítica", "Analítica", "Posanalítica", "Igual en todas las fases"],
  "Cerca del 62% de los errores fueron preanalíticos, el 23% posanalíticos y solo el 15% analíticos.", "Preanalítica.")),

# --- Martin/Hopkins LDL-C (24240933)
("24240933", "researcher", 1, "This equation assumes a fixed factor of 5 for the ratio of triglycerides to very low-density lipoprotein cholesterol",
 ("What assumption of the Friedewald equation did Martin and colleagues replace with an adjustable factor?", ["HDL is always 50 mg/dL", "A fixed TG:VLDL-C ratio of 5", "Total cholesterol equals LDL", "Triglycerides never exceed 150"],
  "The real TG:VLDL-C ratio varies with triglyceride and non-HDL levels, so they derived a 180-cell table of factors.", "Fixed ratio of 5."),
 ("¿Qué supuesto de la ecuación de Friedewald reemplazaron Martin y colegas por un factor ajustable?", ["El HDL siempre vale 50 mg/dL", "Una razón TG:VLDL-C fija de 5", "El colesterol total equivale al LDL", "Los triglicéridos nunca pasan de 150"],
  "La razón TG:VLDL-C real varía con los triglicéridos y el no-HDL, por eso derivaron una tabla de 180 factores.", "Razón fija de 5.")),
("24240933", "expert", 2, "The greatest improvement in concordance occurred in classifying LDL-C lower than 70 mg/dL, especially in patients with high triglyceride levels",
 ("Where did the novel Martin LDL-C method improve most over Friedewald in guideline risk classification?", ["LDL-C above 190 mg/dL in children", "Patients with no triglycerides", "LDL-C below 70 with high triglycerides", "Only in fasting samples from older adult men"],
  "Friedewald underestimates LDL-C at low levels with high triglycerides; the new method was far more concordant there.", "Low LDL, high TG."),
 ("¿Dónde mejoró más el nuevo método de Martin para el LDL-C frente a Friedewald en la clasificación de riesgo?", ["LDL-C mayor de 190 mg/dL en niños y adolescentes", "Pacientes sin triglicéridos", "LDL-C menor de 70 con triglicéridos altos", "Solo en muestras en ayunas de varones"],
  "Friedewald subestima el LDL-C bajo con triglicéridos altos; el nuevo método fue mucho más concordante allí.", "LDL bajo, TG altos.")),

# --- Initial specimen diversion device (28379370)
("28379370", "explorer", 3, "(2/904 [0.22%] ISDD vs 16/904 [1.78%] standard practice",
 ("In the emergency department trial of an initial specimen diversion device, how did blood culture contamination change?", ["From 0.2% up to 1.8%", "It did not change at all", "From 10% down to 9%", "From 1.8% down to 0.2%"],
  "Diverting the first portion of blood cut contamination about eightfold without losing true bacteremia.", "1.8% → 0.2%."),
 ("En el ensayo en urgencias con un dispositivo de desvío de la muestra inicial, ¿cómo cambió la contaminación de los hemocultivos?", ["Subió del 0,2% al 1,8%", "No cambió en absoluto", "Bajó del 10% al 9%", "Bajó del 1,8% al 0,2%"],
  "Desviar la primera porción de sangre redujo la contaminación unas ocho veces sin perder bacteriemias verdaderas.", "Del 1,8% al 0,2%.")),
("28379370", "curious", 0, "a device that diverts and sequesters the initial 1.5-2 mL portion of blood",
 ("What does an initial specimen diversion device do during blood culture collection?", ["Sets aside the first 1.5–2 mL", "Adds antibiotics to the bottle", "Warms the blood to 37 °C", "Doubles the blood volume drawn"],
  "The first portion presumably carries skin cells and microbes, so it is diverted away from the culture bottles.", "Diverts first blood."),
 ("¿Qué hace un dispositivo de desvío de la muestra inicial al extraer hemocultivos?", ["Aparta los primeros 1,5–2 mL", "Agrega antibióticos al frasco", "Calienta la sangre a 37 °C", "Duplica el volumen de sangre"],
  "La primera porción probablemente arrastra células y microbios de la piel, por eso se desvía de los frascos.", "Desvía la primera sangre.")),

# --- Time to positivity meta-analysis (35144551)
("35144551", "expert", 1, "TTP is not associated with mortality among patients with candidaemia",
 ("In a meta-analysis on blood culture time to positivity, in which bloodstream infections was short TTP NOT linked to mortality?", ["Gram-negatives", "Candidemia", "Gram-positives", "S. aureus"],
  "Short TTP predicted death and septic shock in Gram-positive and Gram-negative infections, but not in candidemia.", "Candidemia."),
 ("En un metaanálisis sobre el tiempo de positividad del hemocultivo, ¿en qué bacteriemias un TTP corto NO se asoció con mortalidad?", ["Por gramnegativos", "Candidemia", "Por grampositivos", "Por S. aureus"],
  "Un TTP corto predijo muerte y shock séptico en infecciones por grampositivos y gramnegativos, pero no en candidemia.", "Candidemia.")),

# --- Dipstick in febrile infants (36002228)
("36002228", "explorer", 2, "The most specific individual dipstick test for UTI was the presence of nitrites",
 ("In febrile infants aged 90 days or less, which single dipstick result was most specific for urinary tract infection?", ["Protein", "Leukocytes", "Nitrites", "Blood"],
  "Nitrites had about 91% specificity but only 42% sensitivity.", "Nitrites."),
 ("En lactantes febriles de 90 días o menos, ¿qué resultado aislado de la tira reactiva fue el más específico para infección urinaria?", ["Proteínas", "Leucocitos", "Nitritos", "Sangre"],
  "Los nitritos tuvieron cerca del 91% de especificidad pero solo 42% de sensibilidad.", "Nitritos.")),
("36002228", "researcher", 3, "The most sensitive individual dipstick test for UTI was the presence of leucocytes",
 ("In the UK and Ireland study of febrile infants, which dipstick result was the most sensitive for UTI?", ["Nitrites", "Ketone bodies", "Glucose", "Leukocytes"],
  "Leukocyte esterase including trace had a sensitivity of 0.87, making it the best rule-out marker.", "Leukocytes."),
 ("En el estudio de Reino Unido e Irlanda con lactantes febriles, ¿qué resultado de la tira fue el más sensible para infección urinaria?", ["Nitritos", "Cuerpos cetónicos", "Glucosa", "Leucocitos"],
  "La esterasa leucocitaria, incluyendo trazas, tuvo una sensibilidad de 0,87 y fue el mejor marcador para descartar.", "Leucocitos.")),

# --- MALDI-TOF routine identification (19583519)
("19583519", "beginner", 0, "The mean time required for MALDI-TOF mass spectrometry identification of 1 isolate was 6 minutes",
 ("In the Marseille study of routine MALDI-TOF identification, how long did identifying one bacterial isolate take on average?", ["About 6 minutes", "About 12 hours", "About 2 days", "About 2 weeks"],
  "MALDI-TOF identified an isolate in about 6 minutes at 22–32% of the cost of conventional methods.", "6 minutes."),
 ("En el estudio de Marsella sobre identificación rutinaria por MALDI-TOF, ¿cuánto tardó en promedio identificar un aislamiento bacteriano?", ["Unos 6 minutos", "Unas 6 horas", "Unos 2 días", "Unas 2 semanas"],
  "MALDI-TOF identificó cada aislamiento en unos 6 minutos, con un 22–32% del costo de los métodos convencionales.", "6 minutos.")),
("19583519", "researcher", 1, "were due to improper database entries",
 ("In the routine MALDI-TOF evaluation of 1660 isolates, what mostly caused missing or wrong identifications?", ["Dirty target plates", "Gaps in the reference database", "Poor Gram staining", "Overheated mass spectrometer lasers"],
  "Failures were mainly due to improper database entries; accuracy improved with at least 10 reference spectra per species.", "Database gaps."),
 ("En la evaluación rutinaria de MALDI-TOF con 1660 aislamientos, ¿qué causó sobre todo las identificaciones ausentes o erróneas?", ["Placas diana sucias", "Fallas en la base de referencia", "Tinciones de Gram deficientes", "Espectrómetros sobrecalentados"],
  "Los fallos se debieron sobre todo a entradas inadecuadas de la base; la exactitud mejoraba con al menos 10 espectros por especie.", "Fallas de la base.")),

# --- Rapid multiplex PCR blood culture panel RCT (26197846)
("26197846", "explorer", 2, "Time from BCB Gram stain to microorganism identification was shorter in the intervention group (1.3 hours) vs control (22.3 hours)",
 ("In the Mayo Clinic randomized trial of rapid multiplex PCR on positive blood cultures, how long did identification take after Gram stain?", ["About 22 h vs 1 h", "About 3 days vs 2 days", "About 1.3 h vs 22 h", "About 10 min vs 30 min"],
  "rmPCR identified organisms in 1.3 hours versus 22.3 hours with standard processing.", "1.3 h vs 22 h."),
 ("En el ensayo aleatorizado de la Clínica Mayo con PCR múltiple rápida en hemocultivos positivos, ¿cuánto tardó la identificación tras el Gram?", ["Unas 22 h vs 1 h", "Unos 3 días vs 2 días", "Unas 1,3 h vs 22 h", "Unos 10 min vs 30 min"],
  "La PCR rápida identificó los microorganismos en 1,3 horas frente a 22,3 horas con el procesamiento estándar.", "1,3 h vs 22 h.")),
("26197846", "expert", 3, "Groups did not differ in mortality, LOS, or cost",
 ("In the rapid multiplex PCR blood culture trial, what was the effect on mortality, length of stay and cost?", ["All three fell significantly", "Mortality rose in both rmPCR arms", "Only cost rose sharply", "No differences between groups"],
  "Despite less broad-spectrum use and fewer treated contaminants, hard outcomes did not differ.", "No differences."),
 ("En el ensayo de PCR múltiple rápida en hemocultivos, ¿qué efecto hubo sobre la mortalidad, la estadía y el costo?", ["Los tres bajaron significativamente", "La mortalidad subió con la PCR", "Solo el costo subió mucho", "Sin diferencias entre grupos"],
  "Pese a menos uso de amplio espectro y menos contaminantes tratados, los desenlaces duros no cambiaron.", "Sin diferencias.")),

# --- EUCAST RAST (32789506)
("32789506", "researcher", 0, "Categorical results at 4, 6 and 8 h of incubation were compared with results for EUCAST standard 16-20 h disc diffusion",
 ("In the European validation of EUCAST rapid antimicrobial susceptibility testing (RAST), after which incubation times were zones read?", ["4, 6 and 8 hours", "1, 2 and 3 hours", "24, 48 and 72 hours", "Only after 16–20 hours"],
  "RAST reads disc diffusion directly from positive blood cultures at 4, 6 and 8 h, versus 16–20 h for the standard method.", "4, 6 and 8 h."),
 ("En la validación europea del antibiograma rápido EUCAST (RAST), ¿tras qué tiempos de incubación se leían los halos?", ["4, 6 y 8 horas", "1, 2 y 3 horas", "24, 48 y 72 horas", "Solo tras 16–20 horas"],
  "RAST lee la difusión con discos directamente del hemocultivo positivo a las 4, 6 y 8 h, frente a 16–20 h del método estándar.", "4, 6 y 8 h.")),
("32789506", "explorer", 1, "The EUCAST RAST method can be implemented in routine laboratories without major investments",
 ("What practical conclusion did the 55-laboratory study draw about the EUCAST RAST method?", ["It needs a genome sequencer in every lab", "It needs no big investments", "It only works for yeasts and molds", "It replaces blood cultures entirely"],
  "RAST gave reliable results for key bloodstream pathogens after 4–6 h using ordinary disc diffusion materials.", "Low-cost, routine."),
 ("¿Qué conclusión práctica sacó el estudio de 55 laboratorios sobre el método RAST de EUCAST?", ["Requiere un secuenciador por laboratorio", "Se implementa sin grandes inversiones", "Solo funciona con hongos", "Reemplaza a los hemocultivos"],
  "RAST dio resultados fiables para los principales patógenos de bacteriemia tras 4–6 h con materiales comunes de difusión.", "Bajo costo, rutinario.")),

# --- Pseudohyperkalemia (25319088)
("25319088", "explorer", 2, "It has been increasingly seen in many hematological disorders such as leukocytosis and thrombocytosis",
 ("Besides hemolysis, which hematological conditions are classically linked to pseudohyperkalemia?", ["Iron deficiency anemia", "Hemophilia A and B", "High WBC or platelets", "Vitamin B12 deficiency anemia"],
  "Very high white cell or platelet counts release potassium in vitro, falsely raising the result.", "Leukocytosis, thrombocytosis."),
 ("Además de la hemólisis, ¿qué trastornos hematológicos se asocian clásicamente a la seudohiperpotasemia?", ["Anemia ferropénica", "Hemofilia A y B", "Leucocitosis y trombocitosis", "Anemia por déficit de vitamina B12"],
  "Recuentos muy altos de leucocitos o plaquetas liberan potasio in vitro y elevan falsamente el resultado.", "Leucocitosis, trombocitosis.")),
("25319088", "expert", 3, "plasma potassium levels are greater than the serum potassium levels because of heparin-induced cell membrane damage",
 ("What characterizes 'reverse pseudohyperkalemia' reported in leukemic patients?", ["Serum potassium exceeds plasma", "It appears only in urine", "It is caused by EDTA contamination", "Plasma exceeds serum potassium"],
  "In reverse pseudohyperkalemia, heparin damages fragile leukemic cells, so plasma potassium is higher than serum.", "Plasma > serum."),
 ("¿Qué caracteriza a la «seudohiperpotasemia inversa» descrita en pacientes con leucemia?", ["El potasio sérico supera al plasmático", "Aparece solo en la orina", "La causa la quelación por EDTA", "El plasmático supera al sérico"],
  "En la forma inversa, la heparina daña las células leucémicas frágiles y el potasio plasmático supera al sérico.", "Plasma > suero.")),

# --- ESR and CRP in giant cell arteritis (22119103)
("22119103", "explorer", 0, "CRP is a more sensitive marker than ESR for a positive TAB",
 ("In the temporal artery biopsy study of giant cell arteritis, which inflammatory marker was more sensitive?", ["C-reactive protein", "ESR", "Platelet count", "Serum ferritin level"],
  "Elevated CRP had 86.9% sensitivity versus 84.1% for elevated ESR.", "CRP."),
 ("En el estudio de biopsias de arteria temporal por arteritis de células gigantes, ¿qué marcador inflamatorio fue más sensible?", ["Proteína C reactiva", "VSG", "Recuento de plaquetas", "Ferritina"],
  "La PCR elevada tuvo 86,9% de sensibilidad frente a 84,1% de la VSG elevada.", "PCR.")),
("22119103", "researcher", 1, "Seven patients (4%) with a positive TAB for GCA had a normal ESR and CRP at diagnosis",
 ("In the giant cell arteritis biopsy series, what share of biopsy-positive patients had both a normal ESR and a normal CRP?", ["None of them", "About 4%", "About 25%", "About half"],
  "A small proportion (7 patients, 4%) had normal inflammatory markers, so normal values do not fully exclude GCA.", "About 4%."),
 ("En la serie de biopsias por arteritis de células gigantes, ¿qué proporción de pacientes con biopsia positiva tenía VSG y PCR normales?", ["Ninguno", "Cerca del 4%", "Cerca del 25%", "Cerca de la mitad"],
  "Una pequeña proporción (7 pacientes, 4%) tenía marcadores normales, por lo que no descartan del todo la ACG.", "Cerca del 4%.")),

# --- Reticulocyte hemoglobin equivalent (28299633)
("28299633", "curious", 2, "which is thought to reflect iron content in reticulocytes",
 ("What does the reticulocyte hemoglobin equivalent (RET-He), reported by hematology analyzers, reflect?", ["Bone marrow fat content", "Vitamin B12 in plasma", "Iron content in reticulocytes", "Lifespan of mature circulating platelets"],
  "RET-He is measured in the same tube as the complete blood count and mirrors recent iron supply to red cell production.", "Reticulocyte iron."),
 ("¿Qué refleja el equivalente de hemoglobina reticulocitaria (RET-He) que informan los analizadores hematológicos?", ["La grasa de la médula ósea", "La vitamina B12 plasmática", "El hierro en los reticulocitos", "La vida media de las plaquetas"],
  "El RET-He se mide en el mismo tubo del hemograma y refleja el aporte reciente de hierro a la eritropoyesis.", "Hierro reticulocitario.")),
("28299633", "researcher", 3, "The area under the curve for RET-He was 0.902",
 ("In a study of 211 patients, what area under the ROC curve did RET-He achieve for diagnosing iron deficiency?", ["0.50", "0.61", "0.71", "0.90"],
  "An AUC of 0.902 indicated high accuracy for identifying iron deficiency defined by ferritin below 12 ng/mL.", "0.90."),
 ("En un estudio con 211 pacientes, ¿qué área bajo la curva ROC alcanzó el RET-He para diagnosticar ferropenia?", ["0,50", "0,61", "0,71", "0,90"],
  "Un AUC de 0,902 indicó alta exactitud para identificar ferropenia definida por ferritina menor de 12 ng/mL.", "0,90.")),

# --- HbA1c in ARIC (20200384)
("20200384", "researcher", 0, "more strongly associated with risks of cardiovascular disease and death from any cause as compared with fasting glucose",
 ("In the ARIC cohort of nondiabetic adults, how did glycated hemoglobin compare with fasting glucose as a risk marker?", ["HbA1c was more strongly linked", "Fasting glucose was clearly better", "Neither predicted any outcome", "They were linked only to cancer"],
  "HbA1c predicted diabetes similarly and cardiovascular disease and death more strongly, supporting its diagnostic use.", "HbA1c stronger."),
 ("En la cohorte ARIC de adultos sin diabetes, ¿cómo se comparó la hemoglobina glucosilada con la glucemia en ayunas como marcador de riesgo?", ["La HbA1c se asoció más fuerte", "La glucemia en ayunas fue mejor", "Ninguna predijo ningún desenlace", "Solo se asociaron al cáncer"],
  "La HbA1c predijo la diabetes de forma similar y la enfermedad cardiovascular y la muerte con más fuerza, lo que apoya su uso diagnóstico.", "HbA1c más fuerte.")),

# --- Manual smear review criteria (12760283)
("12760283", "expert", 1, "This policy reduced manual LDCs by more than 70%",
 ("What happened when a high-volume hematology lab replaced reflex manual differentials with a microscopic smear scan to validate automated counts?", ["Manual counts tripled", "Manual counts fell by over 70%", "Analyzer flags were simply ignored", "Reporting errors rose sharply"],
  "Manual scans validated automated differentials, and full manual counts were only done when the scan found cells the instrument could not quantify.", "Over 70% fewer."),
 ("¿Qué pasó cuando un laboratorio de hematología de alto volumen cambió las fórmulas manuales reflejas por un barrido del frotis para validar el recuento automatizado?", ["Se triplicaron", "Bajaron más del 70%", "Se ignoraron las alarmas", "Subieron mucho los errores"],
  "El barrido validaba la fórmula automatizada y solo se hacía la manual completa si aparecían células que el equipo no cuantificaba.", "Más del 70% menos.")),

# --- Healthy ALT ranges (12093239)
("12093239", "researcher", 2, "Updated upper limits (for men, 500 nkat/L [30 U/L]; for women, 317 nkat/L [19 U/L])",
 ("What updated upper limits of normal for serum ALT did the Milan blood donor study propose?", ["60 U/L men, 50 U/L women", "40 U/L men, 30 U/L women", "30 U/L men, 19 U/L women", "10 U/L for both sexes"],
  "The new limits were lower than the then-current 40 and 30 U/L and better detected HCV viremia.", "30 and 19 U/L."),
 ("¿Qué límites superiores normales actualizados de ALT sérica propuso el estudio de donantes de sangre de Milán?", ["60 U/L varones, 50 U/L mujeres", "40 U/L varones, 30 U/L mujeres", "30 U/L varones, 19 U/L mujeres", "10 U/L para ambos sexos"],
  "Los nuevos límites eran más bajos que los vigentes de 40 y 30 U/L y detectaban mejor la viremia por VHC.", "30 y 19 U/L.")),
("12093239", "explorer", 3, "defined by using populations that included persons with subclinical liver disease",
 ("Why did Prati and colleagues argue that traditional 'normal' ALT limits were too high?", ["They were set in children only", "Analyzers of the time measured AST instead", "They excluded all women", "Reference groups had liver disease"],
  "Older reference populations included people with subclinical liver disease, inflating the upper limits.", "Hidden liver disease."),
 ("¿Por qué Prati y colegas sostuvieron que los límites «normales» tradicionales de ALT eran demasiado altos?", ["Se fijaron solo en niños", "Los equipos medían AST en su lugar", "Excluían a todas las mujeres", "Incluían hepatopatía subclínica"],
  "Las poblaciones de referencia antiguas incluían personas con enfermedad hepática subclínica, lo que inflaba los límites.", "Hepatopatía oculta.")),

# --- aPTT vs anti-Xa in mechanical circulatory support (38725133)
("38725133", "expert", 0, "aPTT and anti-Xa were concordant in 35.5% of paired observations and discordant in 64.5%",
 ("In heparin-treated patients on mechanical circulatory support, how often were simultaneous aPTT and anti-Xa results discordant?", ["About 65%", "About 5%", "About 20%", "Never"],
  "Most of 23,001 pairs were discordant, usually with aPTT higher than anti-Xa.", "About 65%."),
 ("En pacientes con asistencia circulatoria mecánica tratados con heparina, ¿con qué frecuencia fueron discordantes el TTPa y el anti-Xa simultáneos?", ["Cerca del 65%", "Cerca del 5%", "Cerca del 20%", "Nunca"],
  "La mayoría de los 23.001 pares fueron discordantes, casi siempre con TTPa más alto que el anti-Xa.", "Cerca del 65%.")),

# --- Urine culture collection technique (10979067)
("10979067", "explorer", 1, "Contamination rates for the 3 groups were nearly identical (29%, 32%, and 31%, respectively)",
 ("In a randomized study of young women with dysuria, how did the midstream clean-catch technique affect urine culture contamination?", ["It halved contamination", "No real difference", "It eliminated contamination", "It tripled contamination"],
  "Contamination was about 30% with or without cleansing, midstream collection or a tampon.", "No difference."),
 ("En un estudio aleatorizado en mujeres jóvenes con disuria, ¿cómo afectó la técnica de chorro medio con limpieza a la contaminación del urocultivo?", ["La redujo a la mitad", "Sin diferencia real", "La eliminó por completo", "La triplicó"],
  "La contaminación fue de cerca del 30% con o sin limpieza, chorro medio o tampón.", "Sin diferencia.")),

# --- Low-volume tubes and hemolysis (24360888)
("24360888", "researcher", 2, "The rate of hemolyzed specimens received from the ED increased from 3.5% using 5.0mL plastic serum tubes to 5.2%",
 ("When an emergency department switched from 5.0 mL to 3.5 mL serum tubes, what happened to the hemolysis rate?", ["It fell from 5.2% to 1.1%", "It stayed exactly the same", "It rose from 3.5% to 5.2%", "It fell to zero"],
  "Low-volume tubes did not reduce spurious hemolysis in an ED where most samples were drawn through catheters.", "It rose."),
 ("Cuando un servicio de urgencias pasó de tubos de suero de 5,0 mL a 3,5 mL, ¿qué ocurrió con la tasa de hemólisis?", ["Bajó del 5,2% al 1,1%", "Se mantuvo exactamente igual", "Subió del 3,5% al 5,2%", "Bajó a cero"],
  "Los tubos de bajo volumen no redujeron la hemólisis espuria en una urgencia donde casi todo se extraía por catéter.", "Subió.")),

# --- HbA1c point-of-care devices (29921132)
("29921132", "expert", 3, "The A1Care had a sigma of 1.4 and failed all criteria",
 ("In the evaluation of four HbA1c point-of-care devices against international quality targets, which device failed all criteria?", ["Afinion2", "Quo-Lab", "HbA1c 501", "A1Care"],
  "The A1Care had a sigma of 1.4, mainly from high imprecision, while the Afinion2 reached a sigma of 5.8.", "A1Care."),
 ("En la evaluación de cuatro equipos de HbA1c en el punto de atención frente a metas internacionales, ¿cuál no cumplió ningún criterio?", ["Afinion2", "Quo-Lab", "HbA1c 501", "A1Care"],
  "El A1Care tuvo un sigma de 1,4, sobre todo por alta imprecisión, mientras el Afinion2 alcanzó un sigma de 5,8.", "A1Care.")),

# --- Westgard multirules vs moving averages (34998790)
("34998790", "expert", 0, "For methods having Sigmas of 4 or greater, traditional single rule and multirule procedures with Ns up to 4 are most effective",
 ("According to Westgard and colleagues, which internal QC approach is most effective for methods of 4 Sigma or higher?", ["Single and multirule procedures", "Moving averages alone", "No QC is ever needed", "Daily recalibration without any controls"],
  "For high-Sigma methods, classic Westgard rules with few controls detect shifts best; moving averages help below 4 Sigma.", "Westgard rules."),
 ("Según Westgard y colegas, ¿qué enfoque de control interno es el más eficaz para métodos de 4 Sigma o más?", ["Reglas simples y multirreglas", "Solo promedios móviles", "Nunca hace falta control", "Recalibrar a diario sin usar controles"],
  "En métodos de alto Sigma, las reglas de Westgard con pocos controles detectan mejor los desvíos; los promedios móviles ayudan bajo 4 Sigma.", "Reglas de Westgard.")),

# --- ALT ULN variability across laboratories (19787805)
("19787805", "researcher", 1, "Wide variability in ALT ULN across different labs is more likely due to variable reference intervals of different chemical analyzers",
 ("In the Indiana statewide survey, what mainly explained the wide variability in ALT upper limits of normal between laboratories?", ["Patient diets in each county", "Analyzer reference intervals", "Seasonal changes in room temperature", "Errors in typing results"],
  "Most labs adopted the manufacturer's interval, so ULN varied with the analyzer brand rather than the local population.", "Analyzer intervals."),
 ("En la encuesta del estado de Indiana, ¿qué explicó sobre todo la gran variabilidad del límite superior normal de ALT entre laboratorios?", ["La dieta de cada condado", "Los intervalos del analizador", "Cambios de temperatura estacionales", "Errores al transcribir resultados"],
  "La mayoría usaba el intervalo del fabricante, así que el límite variaba con la marca del analizador y no con la población.", "Intervalos del analizador.")),
]
