# Clinical laboratory II — tumor markers (PSA trials ERSPC/PLCO, CA125 UKCTOCS, CEA FACS, AFP), thyroid
# tests and subclinical hypothyroidism, blood gases and lactate, HIV 4th-generation and syphilis serology,
# hepatitis B core antibody, immunohematology (type and screen, DAT, wrong blood in tube, SHOT), vancomycin
# TDM, CSF lactate, FIT and faecal calprotectin, presepsin, urine ACR, vitamin D and B12 testing, HPLC
# hemoglobinopathy screening, malaria RDTs and thick smears, Xpert MTB/RIF, laboratory automation.
# Sources: PubMed paper and review abstracts. Excerpts verbatim.
CATEGORY = "diagnosticMethods"
Q = [
# --- ERSPC PSA screening (19297566)
("19297566", "beginner", 0, "PSA-based screening reduced the rate of death from prostate cancer by 20%",
 ("In the European ERSPC trial, how much did PSA screening reduce the rate of death from prostate cancer?", ["About 20%", "About 80%", "Not at all", "About 50%"],
  "PSA screening lowered prostate cancer death by 20%, but at the cost of a high risk of overdiagnosis.", "About 20%."),
 ("En el ensayo europeo ERSPC, ¿cuánto redujo el tamizaje con PSA la tasa de muerte por cáncer de próstata?", ["Cerca del 20%", "Cerca del 80%", "Nada en absoluto", "Cerca del 50%"],
  "El tamizaje con PSA redujo un 20% la muerte por cáncer de próstata, pero con un alto riesgo de sobrediagnóstico.", "Cerca del 20%.")),
("19297566", "researcher", 1, "1410 men would need to be screened and 48 additional cases of prostate cancer would need to be treated to prevent one death",
 ("In ERSPC at a median of 9 years, how many men had to be screened with PSA to prevent one prostate cancer death?", ["About 48", "About 1410", "About 14", "About 100,000"],
  "1410 men had to be screened, and 48 extra cancers treated, to prevent one prostate cancer death.", "About 1410."),
 ("En ERSPC, con una mediana de 9 años, ¿a cuántos hombres había que tamizar con PSA para evitar una muerte por cáncer de próstata?", ["Unos 48", "Unos 1410", "Unos 14", "Unos 100.000"],
  "Había que tamizar a 1410 hombres y tratar 48 cánceres adicionales para evitar una muerte por cáncer de próstata.", "Unos 1410.")),

# --- PLCO prostate screening (19297565)
("19297565", "explorer", 2, "the rate of death from prostate cancer was very low and did not differ significantly between the two study groups",
 ("In the US PLCO trial, what was the effect of annual PSA screening on prostate cancer death after 7 to 10 years?", ["It halved prostate cancer deaths", "It doubled prostate cancer deaths", "No significant difference", "It eliminated deaths from metastases"],
  "Prostate cancer deaths were very low and similar in the screened and usual-care groups.", "No difference."),
 ("En el ensayo estadounidense PLCO, ¿qué efecto tuvo el PSA anual sobre la muerte por cáncer de próstata a los 7–10 años?", ["Redujo a la mitad esas muertes", "Duplicó esas muertes", "Ninguna diferencia significativa", "Eliminó las muertes por metástasis"],
  "Las muertes por cáncer de próstata fueron muy pocas y similares en el grupo tamizado y en el de atención habitual.", "Sin diferencia.")),
("19297565", "expert", 3, "Rates of screening in the control group increased from 40% in the first year to 52% in the sixth year for PSA testing",
 ("What major problem affected the usual-care control group of the PLCO prostate cancer trial?", ["Most controls refused follow-up", "Controls had far older ages", "Controls were given daily aspirin", "Many controls also had PSA tests"],
  "PSA testing in controls rose from 40% to 52%, contaminating the comparison.", "Contamination by PSA."),
 ("¿Qué problema importante afectó al grupo control de atención habitual del ensayo PLCO de cáncer de próstata?", ["La mayoría abandonó el seguimiento", "Los controles eran mucho mayores", "Los controles recibían aspirina todos los días", "Muchos controles también se hicieron PSA"],
  "El uso de PSA en los controles subió del 40% al 52%, lo que contaminó la comparación.", "Contaminación por PSA.")),

# --- UKCTOCS ovarian cancer screening with CA125 (26707054)
("26707054", "explorer", 0, "a mortality reduction over years 0-14 of 15% (95% CI -3 to 30; p=0·10) with MMS",
 ("In UKCTOCS, what did the primary analysis show for annual CA125-based multimodal screening on ovarian cancer deaths?", ["A non-significant 15% reduction", "A significant 50% reduction", "A significant 15% increase", "No effect in any period of follow-up"],
  "The 15% mortality reduction with multimodal screening was not statistically significant (p=0.10) in the primary analysis.", "Non-significant 15% drop."),
 ("En UKCTOCS, ¿qué mostró el análisis principal del tamizaje multimodal anual con CA125 sobre las muertes por cáncer de ovario?", ["Una reducción no significativa del 15%", "Una reducción significativa del 50%", "Un aumento significativo del 15%", "Ningún efecto en ningún periodo de seguimiento"],
  "La reducción del 15% en la mortalidad con el tamizaje multimodal no fue estadísticamente significativa (p=0,10) en el análisis principal.", "Baja no significativa del 15%.")),
("26707054", "curious", 1, "serum CA125 interpreted with use of the risk of ovarian cancer algorithm",
 ("In the UKCTOCS multimodal screening arm, how was each woman's serum CA125 result interpreted?", ["With one fixed cutoff for all women at 35 U/mL", "With the risk of ovarian cancer algorithm", "Only when combined with a pelvic MRI scan", "As a ratio to the patient's serum CEA"],
  "CA125 was interpreted with the risk of ovarian cancer algorithm, which looks at the pattern of values over time.", "ROCA algorithm."),
 ("En el brazo de tamizaje multimodal de UKCTOCS, ¿cómo se interpretaba el CA125 sérico de cada mujer?", ["Con un único punto de corte de 35 U/mL para todas", "Con el algoritmo de riesgo de cáncer de ovario", "Solo combinado con una resonancia pélvica", "Como cociente frente al CEA sérico"],
  "El CA125 se interpretaba con el algoritmo de riesgo de cáncer de ovario, que analiza el patrón de valores en el tiempo.", "Algoritmo ROCA.")),

# --- CEA after colorectal surgery, FACS trial (29579327)
("29579327", "researcher", 2, "no individual trend threshold achieved a sensitivity above 70 per cent (30 per cent missed recurrences)",
 ("In the FACS trial analysis, what limited the use of CEA trends alone to detect colorectal cancer recurrence?", ["Trends were less accurate than single values", "CEA cannot be measured after surgery", "No threshold exceeded 70% sensitivity", "CEA rose in every healthy patient"],
  "Even the best trend threshold missed about 30% of recurrences, so CEA must be combined with imaging and endoscopy.", "Sensitivity ≤70%."),
 ("En el análisis del ensayo FACS, ¿qué limitó usar solo las tendencias del CEA para detectar la recurrencia del cáncer colorrectal?", ["Las tendencias fueron peores que valores únicos", "El CEA no se puede medir tras la cirugía", "Ningún umbral superó 70% de sensibilidad", "El CEA subió en todos los pacientes sanos"],
  "Incluso el mejor umbral de tendencia omitió cerca del 30% de las recurrencias, por lo que el CEA debe combinarse con imágenes y endoscopia.", "Sensibilidad ≤70%.")),
("29579327", "explorer", 3, "Interpreting trends in CEA measurements instead of single CEA test results improves diagnostic accuracy for recurrence",
 ("According to the FACS trial, how could CEA be interpreted to better detect colorectal cancer recurrence?", ["Using only the first postoperative value", "Ignoring values below 20 μg/l", "Measuring it only every 5 years", "Following its trend over time"],
  "Trends raised the area under the ROC curve to at least 0.82, versus 0.62–0.75 for single values.", "Its trend."),
 ("Según el ensayo FACS, ¿cómo podía interpretarse el CEA para detectar mejor la recurrencia del cáncer colorrectal?", ["Usando solo el primer valor posoperatorio", "Ignorando valores menores de 20 μg/l", "Midiéndolo solo cada 5 años", "Siguiendo su tendencia en el tiempo"],
  "Las tendencias elevaron el área bajo la curva ROC a 0,82 o más, frente a 0,62–0,75 con valores únicos.", "Su tendencia.")),

# --- AFP plus ultrasound for HCC surveillance (29425931)
("29425931", "explorer", 0, "Addition of AFP to ultrasound significantly increases sensitivity of early HCC detection",
 ("In a meta-analysis of hepatocellular carcinoma surveillance in cirrhosis, what did adding alpha-fetoprotein to ultrasound do?", ["Raised early HCC sensitivity", "Made ultrasound fully unnecessary", "Raised specificity to 100%", "Lowered early HCC detection"],
  "Ultrasound plus AFP detected early HCC with 63% sensitivity versus 45% for ultrasound alone, at a small cost in specificity.", "More sensitive."),
 ("En un metaanálisis de vigilancia del carcinoma hepatocelular en cirrosis, ¿qué logró agregar alfafetoproteína a la ecografía?", ["Subió la sensibilidad en CHC temprano", "Volvió del todo innecesaria la ecografía", "Elevó la especificidad al 100%", "Redujo la detección del CHC temprano"],
  "La ecografía con AFP detectó el CHC temprano con 63% de sensibilidad frente a 45% sin AFP, con una leve pérdida de especificidad.", "Más sensible.")),
("29425931", "researcher", 1, "Ultrasound detected any stage HCC with 84% sensitivity (95% confidence interval [CI] 76%-92%), but early-stage HCC with only 47% sensitivity",
 ("What was the pooled sensitivity of ultrasound alone for early-stage hepatocellular carcinoma in patients with cirrhosis?", ["About 84%", "About 47%", "About 97.5%", "About 12%"],
  "Ultrasound found 84% of HCC at any stage but only 47% of early-stage tumors.", "About 47%."),
 ("¿Cuál fue la sensibilidad combinada de la ecografía sola para el carcinoma hepatocelular temprano en pacientes con cirrosis?", ["Cerca del 84%", "Cerca del 47%", "Cerca del 97,5%", "Cerca del 12%"],
  "La ecografía detectó el 84% de los CHC en cualquier estadio, pero solo el 47% de los tumores tempranos.", "Cerca del 47%.")),

# --- TRUST trial, subclinical hypothyroidism (28402245)
("28402245", "beginner", 2, "Levothyroxine provided no apparent benefits in older persons with subclinical hypothyroidism",
 ("In the TRUST trial, did levothyroxine help adults aged 65 or older with subclinical hypothyroidism?", ["Yes, it cured their tiredness", "Yes, it reduced heart attacks", "No, no apparent benefit", "It worsened their symptoms"],
  "Levothyroxine lowered TSH but did not improve hypothyroid symptoms or tiredness scores.", "No benefit."),
 ("En el ensayo TRUST, ¿la levotiroxina ayudó a adultos de 65 años o más con hipotiroidismo subclínico?", ["Sí, curó su cansancio", "Sí, redujo los infartos de miocardio", "No, sin beneficio aparente", "Empeoró sus síntomas"],
  "La levotiroxina bajó la TSH, pero no mejoró los síntomas de hipotiroidismo ni el cansancio.", "Sin beneficio.")),
("28402245", "researcher", 3, "persisting subclinical hypothyroidism (thyrotropin level, 4.60 to 19.99 mIU per liter; free thyroxine level within the reference range)",
 ("How did the TRUST trial define subclinical hypothyroidism for enrollment?", ["TSH under 0.1 with high free T4", "TSH over 20 with low free T4", "Normal TSH with only low free T3 levels", "TSH 4.6–19.99 with normal free T4"],
  "Patients had a persistently raised TSH (4.60–19.99 mIU/L) with free thyroxine in the reference range.", "High TSH, normal T4."),
 ("¿Cómo definió el ensayo TRUST el hipotiroidismo subclínico para la inclusión?", ["TSH menor de 0,1 con T4 libre alta", "TSH mayor de 20 con T4 libre baja", "TSH normal con solo T3 libre baja", "TSH 4,6–19,99 con T4 libre normal"],
  "Los pacientes tenían TSH persistentemente elevada (4,60–19,99 mUI/L) con tiroxina libre dentro del rango de referencia.", "TSH alta, T4 normal.")),

# --- Subclinical hypothyroidism and coronary heart disease (20858880)
("20858880", "explorer", 0, "particularly in those with a TSH concentration of 10 mIU/L or greater",
 ("In this individual-participant analysis of 11 cohorts, which adults with subclinical hypothyroidism had clearly higher coronary heart disease risk?", ["Those with TSH of 10 or more", "Those with TSH of 4.5 to 6.9", "Only women under 40", "Only those with a prior stroke"],
  "Risk rose with TSH and was clearly increased at TSH of 10 mIU/L or above (HR 1.89 for CHD events).", "TSH ≥10."),
 ("En este análisis de datos individuales de 11 cohortes, ¿qué adultos con hipotiroidismo subclínico tenían claramente más riesgo coronario?", ["Los que tenían TSH de 10 o más", "Los que tenían TSH de 4,5 a 6,9", "Solo mujeres menores de 40", "Solo quienes tuvieron un ACV"],
  "El riesgo subía con la TSH y era claramente mayor con TSH de 10 mUI/L o más (HR 1,89 para eventos coronarios).", "TSH ≥10.")),
("20858880", "researcher", 1, "Total mortality was not increased among participants with subclinical hypothyroidism",
 ("In the 2010 pooled cohort analysis of subclinical hypothyroidism, what happened to total (all-cause) mortality?", ["It doubled in all ages", "It was not increased", "It fell by about half", "It tripled in men only"],
  "Coronary risk rose at higher TSH, but overall mortality was not increased.", "Not increased."),
 ("En el análisis combinado de cohortes de 2010 sobre hipotiroidismo subclínico, ¿qué pasó con la mortalidad total?", ["Se duplicó en todas las edades", "No aumentó en absoluto", "Bajó cerca de la mitad", "Se triplicó solo en hombres"],
  "El riesgo coronario subió con TSH más alta, pero la mortalidad total no aumentó.", "No aumentó.")),

# --- Venous vs arterial blood gases (24383789)
("24383789", "beginner", 2, "PVBG analysis compares well with ABG analysis for pH estimations in adults but not to the PCO2 or PO2",
 ("According to a meta-analysis, which value from a peripheral venous blood gas agrees well with an arterial blood gas?", ["The PO2", "The PCO2", "The pH", "Oxygen saturation"],
  "Venous pH was only about 0.03 lower than arterial pH, but PCO2 and PO2 differed too much to substitute.", "pH."),
 ("Según un metaanálisis, ¿qué valor de una gasometría venosa periférica concuerda bien con la gasometría arterial?", ["La PO2", "La PCO2", "El pH", "La saturación"],
  "El pH venoso fue solo unos 0,03 más bajo que el arterial, pero la PCO2 y la PO2 diferían demasiado para sustituirse.", "El pH.")),

# --- Lactate clearance vs ScvO2 (20179283)
("20179283", "explorer", 3, "additional management to normalize lactate clearance compared with management to normalize ScvO2 did not result in significantly different in-hospital mortality",
 ("In the 2010 JAMA trial of early sepsis resuscitation, how did targeting lactate clearance compare with targeting ScvO2?", ["Lactate clearance doubled mortality", "ScvO2 halved mortality", "Lactate required arterial catheters", "No significant mortality difference"],
  "In-hospital mortality was 17% with lactate clearance and 23% with ScvO2, a non-significant difference.", "Similar mortality."),
 ("En el ensayo de JAMA de 2010 sobre reanimación temprana de la sepsis, ¿cómo se comparó apuntar a la depuración de lactato con apuntar a la ScvO2?", ["La depuración de lactato duplicó la mortalidad", "La ScvO2 redujo la mortalidad a la mitad", "El lactato exigió catéter arterial", "Sin diferencia significativa en mortalidad"],
  "La mortalidad hospitalaria fue 17% con depuración de lactato y 23% con ScvO2, una diferencia no significativa.", "Mortalidad similar.")),
("20179283", "researcher", 0, "lactate clearance of at least 10%",
 ("What lactate clearance target was used in the 2010 JAMA trial comparing lactate clearance with ScvO2 in sepsis?", ["At least 10%", "At least 50%", "At least 90%", "Exactly 0% (none)"],
  "The lactate group was resuscitated to achieve a lactate clearance of at least 10%.", "≥10%."),
 ("¿Qué meta de depuración de lactato se usó en el ensayo de JAMA de 2010 que comparó lactato con ScvO2 en la sepsis?", ["Al menos 10%", "Al menos 50%", "Al menos 90%", "Exactamente 0% (nada)"],
  "El grupo de lactato se reanimó hasta lograr una depuración de lactato de al menos 10%.", "≥10%.")),

# --- ANDROMEDA-SHOCK (30772908)
("30772908", "explorer", 1, "a resuscitation strategy targeting normalization of capillary refill time, compared with a strategy targeting serum lactate levels, did not reduce all-cause 28-day mortality",
 ("In the ANDROMEDA-SHOCK trial, which resuscitation target was compared with serum lactate in septic shock?", ["Central venous pressure", "Capillary refill time", "Urine output alone", "Cardiac troponin"],
  "Normalizing capillary refill time was compared with lactate targets; 28-day mortality was not significantly reduced.", "Capillary refill."),
 ("En el ensayo ANDROMEDA-SHOCK, ¿qué meta de reanimación se comparó con el lactato sérico en el choque séptico?", ["Presión venosa central medida", "Tiempo de llenado capilar", "Solo la diuresis", "Troponina cardíaca"],
  "Se comparó normalizar el tiempo de llenado capilar con metas de lactato; la mortalidad a 28 días no bajó de forma significativa.", "Llenado capilar.")),
("30772908", "researcher", 3, "Peripheral perfusion-targeted resuscitation was associated with less organ dysfunction at 72 hours",
 ("In ANDROMEDA-SHOCK, which secondary outcome favored capillary refill-guided over lactate-guided resuscitation?", ["Lower 90-day mortality", "Shorter hospital stays", "Fewer days on vasopressor drugs", "Less organ dysfunction at 72 h"],
  "The mean SOFA score at 72 hours was 5.6 versus 6.6, favoring peripheral perfusion targets.", "Less organ dysfunction."),
 ("En ANDROMEDA-SHOCK, ¿qué resultado secundario favoreció la reanimación guiada por llenado capilar frente a la guiada por lactato?", ["Menor mortalidad a 90 días", "Estancias hospitalarias más cortas", "Más días sin vasopresores", "Menos disfunción orgánica a 72 h"],
  "El SOFA medio a las 72 horas fue 5,6 frente a 6,6, a favor de las metas de perfusión periférica.", "Menos disfunción orgánica.")),

# --- Fourth-generation HIV testing in the ED (24970245)
("24970245", "curious", 2, "nearly one fourth of patients with undiagnosed HIV had acute infections",
 ("In an emergency department opt-out program using fourth-generation HIV tests, what share of new diagnoses were acute infections?", ["Fewer than 1 in 100", "Nearly all of them", "About one fourth", "About three fourths"],
  "18 of 78 new diagnoses (23%) were acute infections that older tests would have struggled to detect.", "About a quarter."),
 ("En un programa de tamizaje voluntario en urgencias con pruebas de VIH de cuarta generación, ¿qué proporción de nuevos diagnósticos fueron infecciones agudas?", ["Menos de 1 de cada 100", "Casi todos ellos", "Cerca de una cuarta parte", "Cerca de tres cuartas partes"],
  "18 de 78 nuevos diagnósticos (23%) fueron infecciones agudas que las pruebas anteriores habrían detectado con dificultad.", "Cerca de un cuarto.")),
("24970245", "beginner", 1, "fourth-generation antigen/antibody combination HIV assay",
 ("What does a fourth-generation HIV laboratory screening test detect?", ["Only HIV antibodies", "HIV antigen plus antibody", "Only CD4 cell counts", "Only the HIV RNA viral load"],
  "Fourth-generation assays combine detection of HIV antigen (p24) and antibodies, catching earlier infections.", "Antigen and antibody."),
 ("¿Qué detecta una prueba de laboratorio de tamizaje de VIH de cuarta generación?", ["Solo anticuerpos contra el VIH", "Antígeno y anticuerpo del VIH", "Solo el recuento de CD4", "Solo la carga viral de ARN"],
  "Las pruebas de cuarta generación combinan la detección del antígeno p24 y de anticuerpos, lo que capta infecciones más tempranas.", "Antígeno y anticuerpo.")),

# --- Fourth-generation HIV rapid tests in the field (26558545)
("26558545", "researcher", 2, "All reported 0% sensitivity of the HIV-1 p24 component for acute HIV-1 diagnosis",
 ("In field evaluations, how sensitive was the p24 antigen component of fourth-generation HIV rapid tests for acute HIV-1?", ["Over 99% in every study", "About 50% in every study", "Zero in every study", "About 80% in every study"],
  "All four studies (17,381 people) found 0% sensitivity of the p24 component; 26 acute infections were missed.", "0%."),
 ("En evaluaciones de campo, ¿qué sensibilidad tuvo el componente de antígeno p24 de las pruebas rápidas de VIH de cuarta generación para el VIH-1 agudo?", ["Más del 99% en cada estudio", "Cerca del 50% en cada estudio", "0% en todos los estudios", "Cerca del 80% en cada estudio"],
  "Los cuatro estudios (17.381 personas) hallaron 0% de sensibilidad del componente p24; se perdieron 26 infecciones agudas.", "0%.")),

# --- Syphilis reverse sequence algorithm (29020212)
("29020212", "expert", 3, "Of veterans with unknown/no prior therapy, only 45% had documentation of subsequent treatment, suggesting suboptimal interpretation of RSA results",
 ("In a Veterans Affairs facility using the syphilis reverse sequence algorithm, what problem was found among EIA+/VDRL−/TP-PA+ patients without known prior therapy?", ["Most were false positives due to HIV", "All had neurosyphilis", "The EIA was never reactive", "Only 45% had documented treatment"],
  "Fewer than half of those without prior therapy were documented as treated, suggesting the results were poorly interpreted.", "Only 45% treated."),
 ("En un centro de Veteranos que usaba el algoritmo inverso para sífilis, ¿qué problema se halló en pacientes EIA+/VDRL−/TP-PA+ sin tratamiento previo conocido?", ["La mayoría eran falsos positivos debidos al VIH", "Todos tenían neurosífilis", "El EIA nunca fue reactivo", "Solo el 45% tenía tratamiento registrado"],
  "Menos de la mitad de quienes no tenían tratamiento previo quedaron registrados como tratados, lo que sugiere una mala interpretación.", "Solo 45% tratados.")),

# --- Isolated anti-HBc (36087102)
("36087102", "explorer", 0, "isolated anti-HBc positivity was associated with an increased risk of liver-related and liver cancer mortality",
 ("In a Korean cohort of 609,299 adults, what was linked to isolated hepatitis B core antibody (anti-HBc) positivity?", ["Higher liver-related mortality", "Full protection from liver cancer", "No link with any liver outcome", "Mortality equal to HBsAg carriers"],
  "Isolated anti-HBc carried a hazard ratio of 1.69 for liver-related death, far below HBsAg carriers (27.0) but above unexposed adults.", "Higher liver mortality."),
 ("En una cohorte coreana de 609.299 adultos, ¿qué se asoció con la positividad aislada del anticuerpo contra el core de hepatitis B (anti-HBc)?", ["Mayor mortalidad de causa hepática", "Protección total contra cáncer hepático", "Ningún vínculo con desenlaces hepáticos", "Mortalidad igual a portadores de HBsAg"],
  "El anti-HBc aislado tuvo una razón de riesgo de 1,69 para muerte hepática, muy por debajo de los portadores de HBsAg (27,0) pero mayor que en no expuestos.", "Mayor mortalidad hepática.")),

# --- Type and screen vs Coombs crossmatch (36199420)
("36199420", "explorer", 1, "only ABO grouping, Rh typing, and antibody screening would be carried out with omission of routine Coombs crossmatch",
 ("In pretransfusion testing, which step does the 'type and screen' method leave out?", ["ABO blood grouping", "The Coombs crossmatch", "Rh(D) typing of the patient", "The antibody screen"],
  "Type and screen performs ABO grouping, Rh typing and an antibody screen, omitting the routine Coombs crossmatch.", "Coombs crossmatch."),
 ("En las pruebas pretransfusionales, ¿qué paso omite el método de 'tipificación y tamizaje'?", ["La tipificación ABO", "La prueba cruzada de Coombs", "La tipificación Rh(D) del paciente", "El tamizaje de anticuerpos"],
  "La tipificación y tamizaje hace grupo ABO, Rh y tamizaje de anticuerpos, y omite la prueba cruzada de Coombs de rutina.", "Prueba cruzada de Coombs.")),
("36199420", "researcher", 2, "13 patients with antibody would have been missed by antibody screen alone",
 ("In the Delhi comparison of type and screen versus Coombs crossmatch, what caution emerged?", ["Crossmatch missed every anti-D", "Antibody screening was always negative", "13 incompatible cases had negative screens", "Agreement between the two methods was perfect"],
  "Thirteen crossmatch-incompatible patients had negative antibody screens, so local screening cells need to cover indigenous antigens.", "Screen missed 13."),
 ("En la comparación de Delhi entre tipificación y tamizaje y prueba cruzada de Coombs, ¿qué advertencia surgió?", ["La prueba cruzada omitió todo anti-D", "El tamizaje siempre fue negativo", "13 incompatibles con tamizaje negativo", "La concordancia entre ambos métodos fue perfecta"],
  "Trece pacientes incompatibles en la prueba cruzada tuvieron tamizaje negativo, por lo que se necesitan células de tamizaje con antígenos locales.", "El tamizaje omitió 13.")),

# --- Direct antiglobulin test (autocontrol) in pretransfusion testing (3705135)
("3705135", "expert", 3, "Elimination of the autocontrol from routine pretransfusion testing, therefore, carries minimal risk to patients",
 ("In a study of 65,049 pretransfusion samples, what was concluded about the routine direct antiglobulin test (autocontrol)?", ["It should be done twice", "It caught most alloantibodies", "It replaced antibody screening", "It had low value; drop it"],
  "The DAT had low predictive value for early alloimmune responses, so removing it carries minimal risk and saves costs.", "Can be dropped."),
 ("En un estudio de 65.049 muestras pretransfusionales, ¿qué se concluyó sobre la prueba de antiglobulina directa de rutina (autocontrol)?", ["Debe hacerse dos veces", "Detectó la mayoría de aloanticuerpos", "Reemplazó al tamizaje de anticuerpos", "Aportó poco; puede omitirse"],
  "La PAD tuvo bajo valor predictivo para respuestas aloinmunes tempranas, así que eliminarla implica un riesgo mínimo y ahorra costos.", "Puede omitirse.")),

# --- Wrong blood in tube, Q-Probes (20670129)
("20670129", "beginner", 0, "Up to 20% of all mistransfusions are traced to patient misidentification and/or sample mislabeling errors",
 ("According to a CAP Q-Probes study of blood banks, which error made before samples reach the lab explains up to 20% of mistransfusions?", ["Sample mislabeling", "Expired reagents", "Freezer failures", "Wrong centrifuge speed"],
  "Patient misidentification and sample mislabeling cause up to 20% of mistransfusions, so labs reject mislabeled samples.", "Mislabeling."),
 ("Según un estudio Q-Probes del CAP en bancos de sangre, ¿qué error previo a la llegada de la muestra explica hasta el 20% de las transfusiones erróneas?", ["Mal etiquetado de muestras", "Reactivos vencidos", "Fallas del congelador", "Velocidad errónea de centrífuga"],
  "La identificación errónea del paciente y el mal etiquetado causan hasta el 20% de las transfusiones erróneas, por eso se rechazan muestras mal rotuladas.", "Mal etiquetado.")),

# --- SHOT ABO-incompatible transfusions (16325447)
("16325447", "curious", 1, "The commonest single error is failure to check at the bedside that the right blood is being given to the right patient",
 ("According to the UK SHOT haemovigilance scheme, what was the commonest single error behind ABO-incompatible transfusions?", ["Mistyping in the laboratory", "Failing the bedside check", "Faulty blood bags", "Donor misidentification"],
  "Most errors happened in clinical areas, and the single commonest was skipping the bedside identity check.", "Bedside check."),
 ("Según el sistema británico de hemovigilancia SHOT, ¿cuál fue el error individual más común en las transfusiones ABO incompatibles?", ["Error de tipificación en el laboratorio", "No verificar junto a la cama", "Bolsas de sangre defectuosas", "Error al identificar al donante"],
  "La mayoría de los errores ocurrieron en áreas clínicas, y el más común fue omitir la verificación de identidad junto a la cama.", "Verificación junto a la cama.")),

# --- Vancomycin TDM: trough vs AUC (29203493)
("29203493", "explorer", 2, "AUC-guided, Bayesian estimation-assisted vancomycin dosing was associated with decreased nephrotoxicity",
 ("In a prospective study, what was AUC-guided Bayesian vancomycin dosing associated with compared with trough targets?", ["More kidney injury", "Lower cure rates", "Less nephrotoxicity", "More blood draws needed"],
  "AUC-guided dosing cut nephrotoxicity, blood sampling and therapy duration without losing efficacy.", "Less nephrotoxicity."),
 ("En un estudio prospectivo, ¿con qué se asoció la dosificación bayesiana de vancomicina guiada por AUC frente a metas de valle?", ["Más lesión renal", "Menores tasas de curación", "Menos nefrotoxicidad", "Más extracciones de sangre"],
  "La dosificación guiada por AUC redujo la nefrotoxicidad, las muestras de sangre y la duración del tratamiento sin perder eficacia.", "Menos nefrotoxicidad.")),
("29203493", "researcher", 3, "Only 19% of all trough concentrations were therapeutic versus 70% of AUCs",
 ("In the trough versus AUC vancomycin dosing study, what share of trough concentrations were in the therapeutic range?", ["About 70%", "About 95%", "About 50.5%", "About 19%"],
  "Only 19% of troughs were therapeutic, compared with 70% of AUC values.", "About 19%."),
 ("En el estudio de vancomicina de valle frente a AUC, ¿qué proporción de las concentraciones valle estuvo en rango terapéutico?", ["Cerca del 70%", "Cerca del 95%", "Cerca del 50,5%", "Cerca del 19%"],
  "Solo el 19% de los valles fue terapéutico, frente al 70% de los valores de AUC.", "Cerca del 19%.")),

# --- CSF lactate in meningitis (21194480)
("21194480", "explorer", 0, "To distinguish bacterial meningitis from aseptic meningitis, CSF lactate is a good single indicator and a better marker compared to other conventional markers",
 ("In a meta-analysis of 25 studies, which cerebrospinal fluid marker best distinguished bacterial from aseptic meningitis?", ["CSF lactate", "CSF protein", "CSF glucose", "CSF leukocyte count"],
  "CSF lactate outperformed glucose, the CSF/plasma glucose ratio, protein and leukocyte count.", "CSF lactate."),
 ("En un metaanálisis de 25 estudios, ¿qué marcador del líquido cefalorraquídeo distinguió mejor la meningitis bacteriana de la aséptica?", ["Lactato en LCR", "Proteínas en LCR", "Glucosa en LCR", "Recuento de leucocitos en LCR"],
  "El lactato en LCR superó a la glucosa, el cociente glucosa LCR/plasma, las proteínas y el recuento de leucocitos.", "Lactato en LCR.")),
("21194480", "beginner", 1, "The utility of a cerebrospinal fluid (CSF) lactate assay for this purpose has been debated",
 ("In the meningitis meta-analysis on CSF lactate, what does the abbreviation CSF stand for?", ["Central serum fraction", "Cerebrospinal fluid", "Clotting stability factor", "Cell surface ferritin"],
  "CSF is cerebrospinal fluid, obtained by lumbar puncture to study meningitis.", "Cerebrospinal fluid."),
 ("En el metaanálisis sobre lactato en LCR y meningitis, ¿qué significa la sigla LCR?", ["Fracción sérica central", "Líquido cefalorraquídeo", "Factor de estabilidad de coágulo", "Ferritina de superficie celular"],
  "LCR es el líquido cefalorraquídeo, que se obtiene por punción lumbar para estudiar la meningitis.", "Líquido cefalorraquídeo.")),

# --- Fecal immunochemical test accuracy (24658694)
("24658694", "beginner", 2, "Fecal immunochemical tests are moderately sensitive, are highly specific",
 ("According to a 2014 meta-analysis, how do fecal immunochemical tests (FIT) perform for detecting colorectal cancer?", ["Both low sensitivity and low specificity", "Perfect in both measures", "Moderately sensitive, highly specific", "Highly sensitive, poorly specific"],
  "Pooled sensitivity was 0.79 and specificity 0.94, with high overall accuracy.", "Moderate sensitivity, high specificity."),
 ("Según un metaanálisis de 2014, ¿cómo funcionan las pruebas inmunoquímicas fecales (FIT) para detectar cáncer colorrectal?", ["Tanto baja sensibilidad como baja especificidad", "Perfectas en ambas medidas", "Moderadamente sensibles, muy específicas", "Muy sensibles, poco específicas"],
  "La sensibilidad combinada fue 0,79 y la especificidad 0,94, con alta exactitud global.", "Sensibilidad moderada, alta especificidad.")),
("24658694", "researcher", 3, "Sensitivity for CRC improved with lower assay cutoff values for a positive test result (for example, 0.89 [CI, 0.80 to 0.95] at a cutoff value less than 20 µg/g vs. 0.70 [CI, 0.55 to 0.81] at cutoff values of 20 to 50 µg/g) but with a corresponding decrease in specificity",
 ("In the FIT meta-analysis, how did using a lower positivity cutoff (below 20 µg/g) change test performance?", ["Lower sensitivity but higher specificity", "No change at all", "Both measures rose", "Higher sensitivity, lower specificity"],
  "Sensitivity rose to 0.89 below 20 µg/g versus 0.70 at 20–50 µg/g, while specificity fell.", "More sensitive, less specific."),
 ("En el metaanálisis de FIT, ¿cómo cambió el desempeño al usar un punto de corte más bajo (menos de 20 µg/g)?", ["Menor sensibilidad pero mayor especificidad", "Ningún cambio", "Ambas medidas subieron", "Mayor sensibilidad, menor especificidad"],
  "La sensibilidad subió a 0,89 con menos de 20 µg/g frente a 0,70 con 20–50 µg/g, mientras la especificidad bajó.", "Más sensible, menos específica.")),

# --- Faecal calprotectin for suspected IBD (20634346)
("20634346", "explorer", 0, "Screening by measuring faecal calprotectin levels would result in a 67% reduction in the number of adults requiring endoscopy",
 ("In the faecal calprotectin meta-analysis, by how much could screening cut endoscopies in adults with suspected inflammatory bowel disease?", ["About 67%", "About 6%", "About 99.5%", "About 25%"],
  "Testing calprotectin first would spare about two thirds of adults an endoscopy, at the cost of 6% delayed diagnoses.", "About 67%."),
 ("En el metaanálisis de calprotectina fecal, ¿cuánto podría reducir el tamizaje las endoscopias en adultos con sospecha de enfermedad inflamatoria intestinal?", ["Cerca del 67%", "Cerca del 6%", "Cerca del 99,5%", "Cerca del 25%"],
  "Medir primero la calprotectina evitaría la endoscopia en cerca de dos tercios de los adultos, a costa de un 6% de diagnósticos tardíos.", "Cerca del 67%.")),

# --- Presepsin (26192602)
("26192602", "researcher", 1, "presepsin showed a moderate diagnostic accuracy in differentiating sepsis from non-sepsis which prevented it from being recommended as a definitive test",
 ("What did a 2015 meta-analysis conclude about presepsin (sCD14-ST) for diagnosing sepsis?", ["Near-perfect; use it on its own", "Moderate; not a stand-alone test", "No better than chance at all", "More accurate than blood cultures"],
  "Pooled sensitivity was 0.78 and specificity 0.83: helpful, but not a definitive test on its own.", "Moderate accuracy."),
 ("¿Qué concluyó un metaanálisis de 2015 sobre la presepsina (sCD14-ST) para diagnosticar sepsis?", ["Casi perfecta; úsese sola", "Moderada; no es prueba única", "No mejor que el azar", "Más exacta que los hemocultivos"],
  "La sensibilidad combinada fue 0,78 y la especificidad 0,83: útil, pero no una prueba definitiva por sí sola.", "Exactitud moderada.")),

# --- Urine albumin-to-creatinine ratio and mortality (20483451)
("20483451", "researcher", 2, "ACR 1.1 mg/mmol (10 mg/g) or more are independent predictors of mortality risk in the general population",
 ("In the CKD Prognosis Consortium meta-analysis, which urine albumin-to-creatinine ratio independently predicted mortality in the general population?", ["300 mg/g or more", "30 mg/g or more only", "10 mg/g or more", "1000 mg/g or more"],
  "An ACR of 10 mg/g or more, below the classic 30 mg/g threshold, independently predicted mortality.", "≥10 mg/g."),
 ("En el metaanálisis del CKD Prognosis Consortium, ¿qué cociente albúmina/creatinina en orina predijo de forma independiente la mortalidad en la población general?", ["300 mg/g o más", "Solo 30 mg/g o más", "10 mg/g o más", "1000 mg/g o más"],
  "Un cociente de 10 mg/g o más, por debajo del clásico umbral de 30 mg/g, predijo la mortalidad de forma independiente.", "≥10 mg/g.")),

# --- USPSTF vitamin D screening (33847711)
("33847711", "curious", 3, "the current evidence is insufficient to assess the balance of benefits and harms of screening for vitamin D deficiency in asymptomatic adults",
 ("What did the USPSTF conclude in 2021 about screening asymptomatic adults for vitamin D deficiency?", ["Screen every adult yearly", "Screen only men over 50", "Screening is clearly harmful", "Evidence is insufficient"],
  "The task force issued an I statement: benefits and harms of routine vitamin D testing cannot be determined.", "Insufficient evidence."),
 ("¿Qué concluyó el USPSTF en 2021 sobre el tamizaje de deficiencia de vitamina D en adultos asintomáticos?", ["Tamizar a todo adulto cada año", "Tamizar solo a hombres de más de 50", "El tamizaje es claramente dañino", "La evidencia es insuficiente"],
  "El grupo emitió una declaración I: no se pueden determinar los beneficios y daños de medir la vitamina D de rutina.", "Evidencia insuficiente.")),

# --- Urinary methylmalonic acid for B12 deficiency (3551712)
("3551712", "expert", 0, "All 7 deficient patients had urinary methylmalonic acid levels greater than 5 micrograms/mg creatine (sensitivity, 100%",
 ("In a 1987 prospective evaluation, what was the sensitivity of urinary methylmalonic acid for clinical vitamin B12 deficiency?", ["100% (7 of 7)", "57% (4 of 7)", "71.4% (5 of 7)", "14% (1 of 7)"],
  "All 7 deficient patients had raised urinary methylmalonic acid, and specificity was 99%.", "100%."),
 ("En una evaluación prospectiva de 1987, ¿qué sensibilidad tuvo el ácido metilmalónico urinario para la deficiencia clínica de vitamina B12?", ["100% (7 de 7)", "57% (4 de 7)", "71,4% (5 de 7)", "14% (1 de 7)"],
  "Los 7 pacientes deficientes tenían ácido metilmalónico urinario elevado, y la especificidad fue del 99%.", "100%.")),

# --- HPLC newborn hemoglobinopathy screening (8653895)
("8653895", "explorer", 1, "Automated HPLC is used to test dried blood-spot specimens from newborns for hemoglobins (Hb) F, A, S, C, E, and D",
 ("In a large newborn screening program for sickle cell disease, which specimen was tested by automated HPLC?", ["Fresh cord serum", "Dried blood spots", "First-void urine", "Buccal saliva swabs"],
  "Automated HPLC analyzed dried blood spots for hemoglobins F, A, S, C, E and D in 2.5 million newborns.", "Dried blood spots."),
 ("En un gran programa de tamizaje neonatal de drepanocitosis, ¿qué muestra se analizaba por HPLC automatizada?", ["Suero fresco de cordón", "Gotas de sangre seca", "Primera orina", "Hisopado de saliva bucal"],
  "La HPLC automatizada analizó gotas de sangre seca para las hemoglobinas F, A, S, C, E y D en 2,5 millones de recién nacidos.", "Sangre seca.")),

# --- hrp2 deletion and false-negative malaria RDTs (22302847)
("22302847", "explorer", 2, "parasites that fail to produce HRP2 can cause patent bloodstream infections and false-negative RDT results",
 ("Why did some HRP2-based malaria rapid tests miss P. falciparum infections that were visible on thick smears?", ["Parasites had chloroquine resistance", "The RDTs had expired", "Parasites did not make HRP2", "Patients had sickle cell"],
  "Half of the false-negative samples lacked the hrp2 repeat region, so the parasites produced no HRP2 antigen.", "No HRP2."),
 ("¿Por qué algunas pruebas rápidas de malaria basadas en HRP2 no detectaron infecciones por P. falciparum visibles en gota gruesa?", ["Parásitos resistentes a cloroquina", "Las pruebas estaban vencidas", "Los parásitos no producían HRP2", "Pacientes con drepanocitosis"],
  "La mitad de las muestras falsamente negativas carecía de la región repetida de hrp2, así que los parásitos no producían antígeno HRP2.", "Sin HRP2.")),

# --- Thick smear, RDTs and qPCR in controlled malaria infection (35331251)
("35331251", "beginner", 3, "expert microscopy using Giemsa-stained thick blood smears (TBS)",
 ("In the Equatorial Guinea malaria challenge study, which stain was used on the thick blood smears read by expert microscopists?", ["Gram stain", "Ziehl-Neelsen stain", "India ink", "Giemsa stain"],
  "Malaria thick smears are stained with Giemsa, which colors the parasites for microscopy.", "Giemsa."),
 ("En el estudio de infección controlada de malaria en Guinea Ecuatorial, ¿qué tinción se usó en las gotas gruesas leídas por microscopistas expertos?", ["Tinción de Gram", "Tinción de Ziehl-Neelsen", "Tinta china", "Tinción de Giemsa"],
  "Las gotas gruesas para malaria se tiñen con Giemsa, que colorea los parásitos para el microscopio.", "Giemsa.")),
("35331251", "researcher", 0, "qPCR detected parasitaemia significantly earlier (3.5 days) than the other tests",
 ("In the controlled human malaria infection study in Equatorial Guinea, which test detected P. falciparum parasitemia earliest?", ["Quantitative PCR", "Thick blood smear", "Ultrasensitive RDT", "Conventional RDT"],
  "qPCR detected parasitemia about 3.5 days earlier than thick smears and rapid tests.", "qPCR."),
 ("En el estudio de infección controlada de malaria en Guinea Ecuatorial, ¿qué prueba detectó primero la parasitemia por P. falciparum?", ["PCR cuantitativa", "Gota gruesa", "PDR ultrasensible", "PDR convencional"],
  "La qPCR detectó la parasitemia unos 3,5 días antes que la gota gruesa y las pruebas rápidas.", "qPCR.")),

# --- Xpert MTB/RIF (20825313)
("20825313", "explorer", 1, "a single, direct MTB/RIF test identified 551 of 561 patients with smear-positive tuberculosis (98.2%) and 124 of 171 with smear-negative tuberculosis (72.5%)",
 ("In the 2010 Xpert MTB/RIF validation, how sensitive was a single test in smear-negative, culture-positive tuberculosis?", ["About 98%", "About 72%", "About 30%", "About 10.5%"],
  "One test found 72.5% of smear-negative cases, versus 98.2% of smear-positive cases.", "About 72%."),
 ("En la validación de Xpert MTB/RIF de 2010, ¿qué sensibilidad tuvo una sola prueba en tuberculosis con baciloscopia negativa y cultivo positivo?", ["Cerca del 98%", "Cerca del 72%", "Cerca del 30%", "Cerca del 10,5%"],
  "Una prueba detectó el 72,5% de los casos con baciloscopia negativa, frente al 98,2% de los positivos.", "Cerca del 72%.")),
("20825313", "beginner", 0, "provided sensitive detection of tuberculosis and rifampin resistance directly from untreated sputum in less than 2 hours",
 ("How long did the Xpert MTB/RIF test take to give a tuberculosis and rifampin-resistance result from sputum?", ["Under 2 hours", "About 6 weeks", "About 3 days", "About 2 to 3 weeks"],
  "The automated cartridge test gave results directly from sputum in less than 2 hours.", "Under 2 hours."),
 ("¿Cuánto tardaba la prueba Xpert MTB/RIF en dar un resultado de tuberculosis y resistencia a rifampicina a partir del esputo?", ["Menos de 2 horas", "Unas 6 semanas", "Unos 3 días", "Unas 2 a 3 semanas"],
  "La prueba automatizada en cartucho daba resultados directamente del esputo en menos de 2 horas.", "Menos de 2 horas.")),

# --- Xpert MTB/RIF Ultra (29198911)
("29198911", "researcher", 2, "this increase in sensitivity came at the expense of a decrease in specificity",
 ("Compared with Xpert MTB/RIF, what trade-off did Xpert Ultra show in the 2018 multicentre tuberculosis study?", ["Lower sensitivity but higher specificity", "Worse rifampicin detection", "Higher sensitivity, lower specificity", "No difference in anything"],
  "Ultra was more sensitive in paucibacillary and HIV-positive patients, but specificity dropped (96% vs 98%).", "More sensitive, less specific."),
 ("Frente a Xpert MTB/RIF, ¿qué compensación mostró Xpert Ultra en el estudio multicéntrico de tuberculosis de 2018?", ["Menor sensibilidad pero mayor especificidad", "Peor detección de rifampicina", "Mayor sensibilidad, menor especificidad", "Ninguna diferencia en nada"],
  "Ultra fue más sensible en enfermedad paucibacilar y en personas con VIH, pero la especificidad bajó (96% vs 98%).", "Más sensible, menos específica.")),

# --- Total laboratory automation and turnaround time (29118171)
("29118171", "explorer", 3, "Use of MALDI-TOF MS and TLA individually and together results in significant decreases in microbiology report TATs",
 ("What did total laboratory automation (TLA) together with MALDI-TOF do to microbiology turnaround times for urine cultures?", ["Increased them markedly", "Had no measurable effect", "Only reduced cost", "Significantly cut them"],
  "TLA and MALDI-TOF each shortened times to identification, susceptibility reports and negative results.", "Shortened them."),
 ("¿Qué efecto tuvo la automatización total del laboratorio (TLA) junto con MALDI-TOF sobre los tiempos de respuesta de urocultivos?", ["Los aumentó mucho", "No tuvo efecto medible", "Solo redujo costos", "Los acortó claramente"],
  "La TLA y el MALDI-TOF acortaron los tiempos hasta la identificación, el antibiograma y los resultados negativos.", "Los acortó.")),
]
