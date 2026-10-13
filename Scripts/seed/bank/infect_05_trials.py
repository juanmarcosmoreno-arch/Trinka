# Infectious diseases V — landmark clinical trials and cohorts: dexamethasone in meningitis, 4-month TB
# regimen, HPV vaccine and cervical cancer, typhoid conjugate vaccine, RSV prefusion F vaccines,
# baloxavir, oral step-down for endocarditis and bone infection, daptomycin, 7 vs 14 days for bacteremia.
# Sources: PubMed trial abstracts. Excerpts verbatim.
CATEGORY = "infectiousDiseases"
Q = [
# --- Dexamethasone in adult meningitis (12432041)
("12432041", "researcher", 0, "Early treatment with dexamethasone improves the outcome in adults with acute bacterial meningitis and does not increase the risk of gastrointestinal bleeding",
 ("What did the European trial of dexamethasone in adult bacterial meningitis conclude?", ["Better outcome, no extra GI bleeding", "It increases deaths from gastric bleeding", "It only helps children, not adults", "It works only when given after 4 days"],
  "Early dexamethasone lowered unfavorable outcomes and deaths, especially in pneumococcal meningitis.", "Improves outcome."),
 ("¿Qué concluyó el ensayo europeo de dexametasona en meningitis bacteriana del adulto?", ["Mejor resultado, sin más sangrado", "Aumenta las muertes por sangrado gástrico", "Solo ayuda a niños, no a adultos", "Solo sirve si se da después de 4 días"],
  "La dexametasona temprana redujo los malos resultados y las muertes, sobre todo en la meningitis neumocócica.", "Mejora el resultado.")),
("12432041", "explorer", 2, "Dexamethasone (10 mg) or placebo was administered 15 to 20 minutes before or with the first dose of antibiotic",
 ("When was dexamethasone given in this meningitis trial?", ["A week after the antibiotics", "Only after the fever had resolved", "With the first antibiotic dose", "Only if the culture was negative"],
  "It was given 15–20 minutes before or with the first antibiotic dose, every 6 hours for four days.", "With the first antibiotic."),
 ("¿Cuándo se daba la dexametasona en este ensayo de meningitis?", ["Una semana después de los antibióticos", "Solo cuando la fiebre ya había cedido", "Con la primera dosis de antibiótico", "Solo si el cultivo era negativo"],
  "Se daba 15–20 minutos antes o junto con la primera dosis de antibiótico, cada 6 horas por cuatro días.", "Con el primer antibiótico.")),

# --- Dexamethasone in Vietnam (18077808)
("18077808", "expert", 3, "a beneficial effect appears to be confined to patients with microbiologically proven disease",
 ("In the Vietnamese trial, which patients benefited from dexamethasone for suspected meningitis?", ["All patients with fever and stiff neck", "Only those with probable meningitis", "Only those over 60 years of age", "Those with proven bacterial disease"],
  "Benefit was confined to confirmed bacterial meningitis; in probable cases, tuberculous meningitis may have caused harm.", "Proven disease only."),
 ("En el ensayo de Vietnam, ¿qué pacientes con sospecha de meningitis se beneficiaron con dexametasona?", ["Todos los que tenían fiebre y rigidez de nuca", "Solo los de meningitis probable", "Solo los mayores de 60 años", "Los de meningitis bacteriana confirmada"],
  "El beneficio se limitó a la meningitis bacteriana confirmada; en los casos probables, la meningitis tuberculosa pudo causar daño.", "Solo la comprobada.")),

# --- 4-month rifapentine TB regimen (33951360)
("33951360", "researcher", 1, "The efficacy of a 4-month rifapentine-based regimen containing moxifloxacin was noninferior to the standard 6-month regimen",
 ("Which shorter regimen was noninferior to the standard 6-month treatment for drug-susceptible tuberculosis?", ["Rifapentine alone for 2 months", "Rifapentine + moxifloxacin, 4 mo", "Isoniazid alone for 4 months", "Moxifloxacin alone for 3 months"],
  "Rifapentine with moxifloxacin for 4 months was noninferior; rifapentine without moxifloxacin was not.", "Rifapentine + moxifloxacin."),
 ("¿Qué esquema más corto no fue inferior al tratamiento estándar de 6 meses para la tuberculosis sensible?", ["Rifapentina sola por 2 meses", "Rifapentina + moxifloxacino, 4 m", "Isoniazida sola por 4 meses", "Moxifloxacino solo por 3 meses"],
  "Rifapentina con moxifloxacino por 4 meses no fue inferior; la rifapentina sin moxifloxacino no lo logró.", "Rifapentina + moxifloxacino.")),

# --- HPV vaccine and invasive cervical cancer (32997908)
("32997908", "explorer", 2, "The cumulative incidence of cervical cancer was 47 cases per 100,000 persons among women who had been vaccinated and 94 cases per 100,000 persons among those who had not been vaccinated",
 ("In the Swedish cohort, how did cervical cancer incidence compare between vaccinated and unvaccinated women?", ["It was the same in both groups", "It was higher in vaccinated women", "About half in the vaccinated", "It was zero in both groups"],
  "Cumulative incidence was 47 vs 94 per 100,000; protection was strongest when vaccinated before 17.", "About half."),
 ("En la cohorte sueca, ¿cómo se comparó la incidencia de cáncer de cuello uterino entre vacunadas y no vacunadas?", ["Fue igual en ambos grupos", "Fue mayor en las vacunadas", "La mitad en las vacunadas", "Fue cero en ambos grupos"],
  "La incidencia acumulada fue 47 frente a 94 por 100.000; la protección fue mayor si se vacunaron antes de los 17.", "Cerca de la mitad.")),
("32997908", "researcher", 0, "the incidence rate ratio was 0.12 (95% CI, 0.00 to 0.34) among women who had been vaccinated before the age of 17 years",
 ("Which women had the largest reduction in cervical cancer risk after quadrivalent HPV vaccination?", ["Those vaccinated before age 17", "Those vaccinated after age 30", "Those vaccinated during pregnancy", "Risk fell equally at every age"],
  "Before 17 the adjusted rate ratio was 0.12, versus 0.47 when vaccinated at 17–30.", "Before age 17."),
 ("¿Qué mujeres tuvieron la mayor reducción del riesgo de cáncer de cuello uterino con la vacuna tetravalente contra el VPH?", ["Las vacunadas antes de los 17 años", "Las vacunadas después de los 30", "Las vacunadas durante el embarazo", "El riesgo bajó igual a toda edad"],
  "Antes de los 17 la razón de tasas ajustada fue 0,12, frente a 0,47 si se vacunaron entre 17 y 30.", "Antes de los 17.")),

# --- Typhoid conjugate vaccine, Nepal (31800986)
("31800986", "researcher", 3, "vaccine efficacy, 81.6%",
 ("What efficacy did a single dose of typhoid conjugate vaccine show in Nepalese children?", ["About 18%", "About 41%", "About 99%", "About 82%"],
  "Blood culture-confirmed typhoid occurred in 7 TCV vs 38 control recipients: 81.6% efficacy.", "~82%."),
 ("¿Qué eficacia mostró una dosis de vacuna conjugada contra la fiebre tifoidea en niños de Nepal?", ["Cerca del 18%", "Cerca del 41%", "Cerca del 99%", "Cerca del 82%"],
  "Hubo fiebre tifoidea confirmada en 7 vacunados con TCV frente a 38 controles: 81,6% de eficacia.", "~82%.")),
("31800986", "expert", 1, "to receive either a TCV or a capsular group A meningococcal conjugate vaccine (MenA) as a control",
 ("What did the control group receive in the Nepal typhoid conjugate vaccine trial?", ["A saline placebo injection", "A meningococcal A vaccine", "An oral live typhoid vaccine", "No injection or vaccine at all"],
  "Controls got a MenA conjugate vaccine, so both groups received a useful vaccine.", "MenA vaccine."),
 ("¿Qué recibió el grupo control en el ensayo de la vacuna conjugada antitifoidea de Nepal?", ["Una inyección de placebo salino", "Una vacuna meningocócica A", "Una vacuna tifoidea oral viva", "Ninguna inyección ni vacuna"],
  "Los controles recibieron una vacuna conjugada MenA, así ambos grupos recibían una vacuna útil.", "Vacuna MenA.")),

# --- RSVpreF in pregnancy (37018474)
("37018474", "researcher", 2, "vaccine efficacy, 81.8%; 99.5% CI, 40.6 to 96.3",
 ("How effective was maternal RSVpreF vaccination against severe RSV illness in infants within 90 days of birth?", ["About 18%", "About 38%", "About 82%", "About 100%"],
  "Severe RSV lower respiratory illness fell 81.8% at 90 days and 69.4% at 180 days.", "~82%."),
 ("¿Qué eficacia tuvo vacunar a la madre con RSVpreF contra la enfermedad grave por VSR del bebé en los primeros 90 días?", ["Cerca del 18%", "Cerca del 38%", "Cerca del 82%", "Cerca del 100%"],
  "La enfermedad respiratoria baja grave por VSR bajó 81,8% a los 90 días y 69,4% a los 180.", "~82%.")),
("37018474", "explorer", 0, "we randomly assigned, in a 1:1 ratio, pregnant women at 24 through 36 weeks' gestation",
 ("When in pregnancy did women receive the RSVpreF vaccine in the MATISSE trial?", ["At 24 to 36 weeks", "In the first trimester", "Right after delivery", "Before conception"],
  "Vaccination at 24–36 weeks lets maternal antibodies cross the placenta to protect the newborn.", "24–36 weeks."),
 ("¿En qué momento del embarazo se aplicó la vacuna RSVpreF en el ensayo MATISSE?", ["Entre las semanas 24 y 36", "En el primer trimestre", "Justo después del parto", "Antes de la concepción"],
  "Vacunar entre las semanas 24 y 36 permite que los anticuerpos maternos crucen la placenta y protejan al recién nacido.", "Semanas 24–36.")),

# --- RSVpreF in older adults (37018468)
("37018468", "researcher", 3, "vaccine efficacy, 85.7%; 96.66% CI, 32.0 to 98.7",
 ("In adults ≥60 years, how effective was RSVpreF against RSV lower respiratory illness with ≥3 symptoms?", ["About 15%", "About 45%", "About 65%", "About 86%"],
  "Efficacy was 66.7% for illness with ≥2 symptoms and 85.7% with ≥3 symptoms.", "~86%."),
 ("En adultos de 60 años o más, ¿qué eficacia tuvo RSVpreF contra la enfermedad respiratoria baja por VSR con ≥3 síntomas?", ["Cerca del 15%", "Cerca del 45%", "Cerca del 65%", "Cerca del 86%"],
  "La eficacia fue 66,7% para enfermedad con ≥2 síntomas y 85,7% con ≥3 síntomas.", "~86%.")),

# --- Baloxavir (30184455, 40267424)
("30184455", "explorer", 1, "Baloxavir marboxil is a selective inhibitor of influenza cap-dependent endonuclease",
 ("How does baloxavir work against influenza?", ["It blocks neuraminidase", "It blocks the viral endonuclease", "It blocks the M2 ion channel", "It is a live attenuated vaccine"],
  "Baloxavir blocks the viral cap-dependent endonuclease, a different target from oseltamivir.", "Cap-dependent endonuclease."),
 ("¿Cómo actúa el baloxavir contra la influenza?", ["Bloquea la neuraminidasa", "Inhibe la endonucleasa viral", "Bloquea el canal iónico M2", "Es una vacuna viva atenuada"],
  "El baloxavir bloquea la endonucleasa viral dependiente de cap, un blanco distinto del oseltamivir.", "Endonucleasa dependiente de cap.")),
("30184455", "researcher", 2, "Baloxavir was associated with greater reductions in viral load 1 day after initiation of the regimen than placebo or oseltamivir",
 ("Compared with oseltamivir, what advantage did single-dose baloxavir show?", ["Much faster relief of symptoms", "No side effects at all in anyone", "A faster drop in viral load", "It prevented all complications"],
  "Symptom relief was similar to oseltamivir, but viral load fell more by day 1.", "Faster viral drop."),
 ("Frente al oseltamivir, ¿qué ventaja mostró el baloxavir en dosis única?", ["Alivio de síntomas mucho más rápido", "Ningún efecto adverso en nadie", "La carga viral bajaba antes", "Evitó todas las complicaciones"],
  "El alivio de síntomas fue similar al del oseltamivir, pero la carga viral bajó más al día 1.", "Carga viral baja antes.")),
("40267424", "researcher", 0, "with an adjusted relative risk reduction of 29%",
 ("By how much did treating the index patient with baloxavir reduce influenza transmission to household contacts?", ["About 29%", "About 9%", "About 79%", "Not at all"],
  "Transmission by day 5 was 9.5% vs 13.4%, a 29% relative reduction; symptomatic transmission was not significantly lower.", "~29%."),
 ("¿Cuánto redujo tratar con baloxavir al paciente índice la transmisión de influenza a los convivientes?", ["Cerca del 29%", "Cerca del 9%", "Cerca del 79%", "Nada"],
  "La transmisión al día 5 fue 9,5% frente a 13,4%, una reducción relativa de 29%; la transmisión sintomática no bajó en forma significativa.", "~29%.")),

# --- POET oral step-down for endocarditis (30152252)
("30152252", "researcher", 3, "changing to oral antibiotic treatment was noninferior to continued intravenous antibiotic treatment",
 ("In the POET trial, how did switching stable endocarditis patients to oral antibiotics compare with continuing IV?", ["It caused far more deaths", "It was clearly inferior", "It required more surgery", "It was noninferior to IV"],
  "After at least 10 days IV, switching to oral therapy was noninferior for death, surgery, emboli and relapse.", "Noninferior."),
 ("En el ensayo POET, ¿cómo resultó pasar a antibióticos orales a pacientes estables con endocarditis frente a seguir IV?", ["Causó muchas más muertes", "Fue claramente inferior", "Requirió más cirugías", "No fue inferior a la IV"],
  "Tras al menos 10 días IV, pasar a vía oral no fue inferior en muerte, cirugía, embolias ni recaídas.", "No inferior.")),

# --- OVIVA bone and joint (30699315)
("30699315", "explorer", 1, "Catheter complications, analyzed as a secondary end point, were more common in the intravenous group (9.4% vs. 1.0%)",
 ("Besides similar efficacy, what was a practical advantage of oral therapy in the OVIVA trial?", ["Bone infections healed in a week", "Far fewer catheter complications", "No need for any surgery at all", "Patients could stop at 2 weeks"],
  "Catheter complications were 9.4% with IV versus 1.0% with oral therapy.", "Fewer catheter problems."),
 ("Además de una eficacia similar, ¿qué ventaja práctica tuvo la vía oral en el ensayo OVIVA?", ["Las infecciones óseas curaban en una semana", "Muchas menos complicaciones de catéter", "No hacía falta ninguna cirugía", "Se podía suspender a las 2 semanas"],
  "Las complicaciones de catéter fueron 9,4% con IV frente a 1,0% con vía oral.", "Menos problemas de catéter.")),

# --- Daptomycin for S. aureus bacteremia (16914701)
("16914701", "researcher", 2, "Clinically significant renal dysfunction occurred in 11.0 percent of patients who received daptomycin and in 26.3 percent of patients who received standard therapy",
 ("Which safety advantage did daptomycin show over standard therapy with gentamicin for S. aureus bacteremia?", ["Less hearing loss", "Fewer allergic rashes", "Less renal dysfunction", "No muscle toxicity"],
  "Kidney dysfunction occurred in 11% with daptomycin versus 26.3% with standard therapy including gentamicin.", "Less kidney damage."),
 ("¿Qué ventaja de seguridad mostró la daptomicina frente a la terapia estándar con gentamicina en la bacteriemia por S. aureus?", ["Menos pérdida de audición", "Menos erupciones alérgicas", "Menos disfunción renal", "Ninguna toxicidad muscular"],
  "La disfunción renal ocurrió en 11% con daptomicina frente a 26,3% con la terapia estándar con gentamicina.", "Menos daño renal.")),

# --- BALANCE 7 vs 14 days (39565030)
("39565030", "explorer", 0, "Among hospitalized patients with bloodstream infection, antibiotic treatment for 7 days was noninferior to treatment for 14 days",
 ("What did the BALANCE trial show about antibiotic duration for bloodstream infections?", ["7 days was noninferior to 14", "14 days saved many more lives", "3 days was enough for everyone", "Longer courses were always safer"],
  "90-day mortality was 14.5% with 7 days and 16.1% with 14 days, showing noninferiority.", "7 days enough."),
 ("¿Qué mostró el ensayo BALANCE sobre la duración del antibiótico en bacteriemias?", ["7 días no fue inferior a 14", "14 días salvó muchas más vidas", "3 días alcanzaban para todos", "Los cursos largos siempre eran más seguros"],
  "La mortalidad a 90 días fue 14,5% con 7 días y 16,1% con 14 días: no inferioridad.", "7 días alcanzan.")),
("39565030", "researcher", 3, "or cultures yielding Staphylococcus aureus",
 ("Which bacterium was excluded from the BALANCE 7- vs 14-day bacteremia trial?", ["Escherichia coli", "Klebsiella pneumoniae", "Streptococcus pneumoniae", "Staphylococcus aureus"],
  "S. aureus bacteremia was excluded because it usually requires longer treatment.", "S. aureus."),
 ("¿Qué bacteria se excluyó del ensayo BALANCE de 7 frente a 14 días en bacteriemias?", ["Escherichia coli", "Klebsiella pneumoniae", "Streptococcus pneumoniae", "Staphylococcus aureus"],
  "Se excluyó la bacteriemia por S. aureus porque suele requerir tratamientos más largos.", "S. aureus.")),
("39565030", "expert", 1, "Bacteremia most commonly originated from the urinary tract (42.2%)",
 ("What was the most common source of bloodstream infection in the BALANCE trial?", ["The lungs", "The urinary tract", "Vascular catheters", "Skin and soft tissue"],
  "Urinary sources led (42%), then abdomen (19%) and lung (13%).", "Urinary tract."),
 ("¿Cuál fue el origen más común de la bacteriemia en el ensayo BALANCE?", ["Los pulmones", "Las vías urinarias", "Los catéteres vasculares", "La piel y partes blandas"],
  "El origen urinario encabezó (42%), seguido del abdomen (19%) y el pulmón (13%).", "Vías urinarias.")),
]
