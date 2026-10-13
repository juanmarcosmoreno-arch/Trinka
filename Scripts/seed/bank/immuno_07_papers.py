# Immunology VII — landmark trials and cohorts: CheckMate 067 and 017, KEYNOTE-024, CAR-T in CLL, ALL and
# myeloma, rituximab, infliximab and ocrelizumab in autoimmunity, LEAP-On and EAT, farm microbes and asthma,
# mRNA Covid-19 vaccine trials, HPV vaccine impact in Sweden and England, BCG trained immunity and BRACE,
# vaccines for older adults (zoster, high-dose influenza), transplant tolerance via mixed chimerism.
# Sources: PubMed original papers and trials (abstracts). Excerpts verbatim.
CATEGORY = "immunology"
Q = [
# --- CheckMate 067 (26027431)
("26027431", "researcher", 2, "The median progression-free survival was 11.5 months (95% confidence interval [CI], 8.9 to 16.7) with nivolumab plus ipilimumab, as compared with 2.9 months (95% CI, 2.8 to 3.4) with ipilimumab",
 ("In the CheckMate 067 melanoma trial, what was the median progression-free survival with nivolumab plus ipilimumab versus ipilimumab alone?", ["2.9 vs 11.5 months", "6.9 vs 5.3 months", "11.5 vs 2.9 months", "14.0 vs 10.2 months"],
  "Adding PD-1 blockade to CTLA-4 blockade roughly quadrupled median progression-free survival in untreated metastatic melanoma.", "11.5 vs 2.9 months."),
 ("En el ensayo CheckMate 067 en melanoma, ¿cuál fue la mediana de supervivencia libre de progresión con nivolumab más ipilimumab frente a ipilimumab solo?", ["2,9 vs 11,5 meses", "6,9 vs 5,3 meses", "11,5 vs 2,9 meses", "14,0 vs 10,2 meses"],
  "Sumar el bloqueo de PD-1 al de CTLA-4 casi cuadruplicó la mediana de supervivencia libre de progresión en melanoma metastásico no tratado.", "11,5 vs 2,9 meses.")),
("26027431", "expert", 0, "in patients with PD-L1-negative tumors, progression-free survival was longer with the combination therapy than with nivolumab alone",
 ("In CheckMate 067, in which melanoma subgroup did nivolumab plus ipilimumab clearly outperform nivolumab alone?", ["PD-L1-negative tumors", "PD-L1-positive tumors", "BRAF-mutant tumors only", "Patients older than 75 years"],
  "In PD-L1-positive tumors both arms reached 14.0 months, but in PD-L1-negative tumors the combination gave 11.2 versus 5.3 months.", "PD-L1-negative tumors."),
 ("En CheckMate 067, ¿en qué subgrupo de melanoma nivolumab más ipilimumab superó claramente a nivolumab solo?", ["Tumores PD-L1 negativos", "Tumores PD-L1 positivos", "Solo tumores con BRAF mutado", "Pacientes mayores de 75 años"],
  "En tumores PD-L1 positivos ambos brazos llegaron a 14,0 meses, pero en los PD-L1 negativos la combinación dio 11,2 frente a 5,3 meses.", "Tumores PD-L1 negativos.")),

# --- CheckMate 017 (26028407)
("26028407", "explorer", 3, "The risk of death was 41% lower with nivolumab than with docetaxel",
 ("In the CheckMate 017 trial in previously treated squamous non-small-cell lung cancer, how did nivolumab compare with docetaxel for risk of death?", ["Similar risk of death", "20% higher with nivolumab", "10% lower with nivolumab", "41% lower with nivolumab"],
  "Median overall survival was 9.2 months with nivolumab versus 6.0 months with docetaxel (hazard ratio 0.59).", "41% lower."),
 ("En el ensayo CheckMate 017 en cáncer de pulmón escamoso de células no pequeñas ya tratado, ¿cómo se comparó nivolumab con docetaxel en riesgo de muerte?", ["Riesgo de muerte similar", "20% mayor con nivolumab", "10% menor con nivolumab", "41% menor con nivolumab"],
  "La mediana de supervivencia global fue de 9,2 meses con nivolumab frente a 6,0 con docetaxel (hazard ratio 0,59).", "41% menor.")),
("26028407", "researcher", 1, "The expression of the PD-1 ligand (PD-L1) was neither prognostic nor predictive of benefit",
 ("What role did tumor PD-L1 expression play in the CheckMate 017 nivolumab trial in squamous lung cancer?", ["It strongly predicted who would benefit", "Neither prognostic nor predictive", "It predicted severe toxic effects", "It was only prognostic of survival"],
  "Nivolumab beat docetaxel regardless of PD-L1 expression level in this squamous NSCLC population.", "No predictive role."),
 ("¿Qué papel tuvo la expresión tumoral de PD-L1 en el ensayo CheckMate 017 con nivolumab en cáncer de pulmón escamoso?", ["Predijo fuertemente el beneficio", "No fue pronóstica ni predictiva", "Predijo efectos tóxicos graves", "Solo fue pronóstica de supervivencia"],
  "Nivolumab superó a docetaxel con independencia del nivel de PD-L1 en esta población con CPCNP escamoso.", "Ningún papel predictivo.")),

# --- KEYNOTE-024 (27718847)
("27718847", "researcher", 2, "with PD-L1 expression on at least 50% of tumor cells",
 ("Which patients with untreated advanced NSCLC were enrolled in KEYNOTE-024, comparing first-line pembrolizumab with chemotherapy?", ["Any PD-L1 level with EGFR mutation", "PD-L1 on fewer than 1% of tumor cells", "PD-L1 on at least 50% of tumor cells", "Only ALK-rearranged tumors"],
  "The trial selected tumors with high PD-L1 expression and no EGFR or ALK alterations.", "PD-L1 ≥50%."),
 ("¿Qué pacientes con CPCNP avanzado no tratado entraron en KEYNOTE-024, que comparó pembrolizumab de primera línea con quimioterapia?", ["Cualquier PD-L1 con mutación de EGFR", "PD-L1 en menos del 1% de las células tumorales", "PD-L1 en al menos el 50% de células tumorales", "Solo tumores con reordenamiento del gen ALK"],
  "El ensayo seleccionó tumores con alta expresión de PD-L1 y sin alteraciones de EGFR ni ALK.", "PD-L1 ≥50%.")),
("27718847", "explorer", 0, "grade 3, 4, or 5 treatment-related adverse events (26.6% vs. 53.3%)",
 ("In KEYNOTE-024, how did severe (grade 3-5) treatment-related adverse events compare between pembrolizumab and platinum chemotherapy?", ["26.6% vs 53.3%", "53.3% vs 26.6%", "About 40% in both arms", "Under 5% in both arms"],
  "Pembrolizumab not only prolonged survival but also halved severe treatment-related toxicity compared with chemotherapy.", "Fewer with pembrolizumab."),
 ("En KEYNOTE-024, ¿cómo se compararon los eventos adversos graves (grado 3-5) relacionados con el tratamiento entre pembrolizumab y quimioterapia con platino?", ["26,6% vs 53,3%", "53,3% vs 26,6%", "Cerca del 40% en ambos", "Menos del 5% en ambos"],
  "Pembrolizumab no solo prolongó la supervivencia, también redujo a la mitad la toxicidad grave frente a la quimioterapia.", "Menos con pembrolizumab.")),

# --- First CD19 CAR-T in CLL (21830940)
("21830940", "researcher", 3, "coupled with CD137 (a costimulatory receptor in T cells [4-1BB]) and CD3-zeta",
 ("In the 2011 report of CD19 CAR T cells in chronic lymphocytic leukemia, which costimulatory domain did the receptor carry alongside CD3-zeta?", ["CD28 (Tp44)", "OX40 (TNFRSF4)", "ICOS (CD278)", "CD137 (4-1BB)"],
  "The lentiviral CAR combined anti-CD19 specificity with 4-1BB costimulation and CD3-zeta signaling; the cells expanded over 1000-fold in vivo.", "4-1BB."),
 ("En el informe de 2011 sobre células CAR-T anti-CD19 en leucemia linfocítica crónica, ¿qué dominio coestimulador llevaba el receptor junto a CD3-zeta?", ["CD28 (Tp44)", "OX40 (TNFRSF4)", "ICOS (CD278)", "CD137 (4-1BB)"],
  "El CAR lentiviral combinó especificidad anti-CD19 con coestimulación 4-1BB y señalización CD3-zeta; las células se expandieron más de 1000 veces in vivo.", "4-1BB.")),

# --- CTL019 in ALL (25317870)
("25317870", "explorer", 1, "Complete remission was achieved in 27 patients (90%)",
 ("In the CTL019 CAR T-cell study of 30 children and adults with relapsed or refractory ALL, what share achieved complete remission?", ["About 30%", "90%", "About 50%", "100%"],
  "27 of 30 patients reached complete remission, including some who had failed stem-cell transplantation.", "90%."),
 ("En el estudio de células CAR-T CTL019 en 30 niños y adultos con LLA recaída o refractaria, ¿qué proporción logró remisión completa?", ["Cerca del 30%", "90%", "Cerca del 50%", "100%"],
  "27 de 30 pacientes alcanzaron remisión completa, incluidos algunos en quienes había fallado el trasplante de progenitores.", "90%.")),
("25317870", "researcher", 2, "was effectively treated with the anti-interleukin-6 receptor antibody tocilizumab",
 ("In the CTL019 trial in ALL, which drug effectively treated severe cytokine-release syndrome?", ["Rituximab, an anti-CD20 antibody", "High-dose intravenous immunoglobulin", "Tocilizumab (anti-IL-6 receptor)", "Infliximab, an anti-TNF antibody"],
  "All patients had cytokine-release syndrome; severe cases tracked with disease burden and responded to IL-6 receptor blockade.", "Tocilizumab."),
 ("En el ensayo de CTL019 en LLA, ¿qué fármaco trató eficazmente el síndrome de liberación de citocinas grave?", ["Rituximab, un anticuerpo anti-CD20", "Inmunoglobulina intravenosa en dosis altas", "Tocilizumab (anti-receptor de IL-6)", "Infliximab, un anticuerpo anti-TNF"],
  "Todos los pacientes tuvieron síndrome de liberación de citocinas; los casos graves se asociaron a mayor carga tumoral y respondieron al bloqueo del receptor de IL-6.", "Tocilizumab.")),

# --- KarMMa ide-cel (33626253)
("33626253", "explorer", 0, "a B-cell maturation antigen-directed chimeric antigen receptor (CAR) T-cell therapy",
 ("In the KarMMa trial in relapsed and refractory multiple myeloma, which antigen did idecabtagene vicleucel (ide-cel) target?", ["BCMA", "CD19", "CD38", "CD138"],
  "Ide-cel is a BCMA-directed CAR T-cell product; 73% of treated patients responded.", "BCMA."),
 ("En el ensayo KarMMa en mieloma múltiple recaído y refractario, ¿qué antígeno atacaba idecabtagén vicleucel (ide-cel)?", ["BCMA", "CD19", "CD38", "CD138"],
  "Ide-cel es un producto CAR-T dirigido contra BCMA; respondió el 73% de los pacientes tratados.", "BCMA.")),

# --- CARTITUDE-1 cilta-cel (34175021)
("34175021", "researcher", 3, "Overall response rate was 97% (95% CI 91·2-99·4; 94 of 97 patients)",
 ("In CARTITUDE-1, what overall response rate did a single infusion of ciltacabtagene autoleucel achieve in heavily pretreated myeloma?", ["33%", "100%", "73%", "97%"],
  "94 of 97 patients responded, and 67% reached stringent complete response.", "97%."),
 ("En CARTITUDE-1, ¿qué tasa de respuesta global logró una sola infusión de ciltacabtagén autoleucel en mieloma muy pretratado?", ["33%", "100%", "73%", "97%"],
  "Respondieron 94 de 97 pacientes, y el 67% alcanzó respuesta completa estricta.", "97%.")),

# --- Rituximab in RA (15201414)
("15201414", "explorer", 1, "selective depletion of B cells with the use of rituximab",
 ("In the randomized trial of rituximab in rheumatoid arthritis (Edwards 2004), what was the therapeutic strategy?", ["Blocking TNF-alpha in the joint", "Selective depletion of B cells", "Blocking IL-6 receptor signaling", "Depleting CD4+ T helper cells"],
  "Rituximab targets CD20 and depletes B cells; it improved disease activity in methotrexate-refractory patients.", "B-cell depletion."),
 ("En el ensayo aleatorizado de rituximab en artritis reumatoide (Edwards 2004), ¿cuál era la estrategia terapéutica?", ["Bloquear el TNF-alfa en la articulación", "Depletar selectivamente las células B", "Bloquear la señal del receptor de IL-6", "Depletar los linfocitos T CD4+ cooperadores"],
  "Rituximab se une a CD20 y depleta células B; mejoró la actividad de la enfermedad en pacientes refractarios a metotrexato.", "Depleción de células B.")),
("15201414", "researcher", 2, "was significantly greater with the rituximab-methotrexate combination (43 percent, P=0.005)",
 ("In the 2004 rituximab trial in rheumatoid arthritis, what share of patients on rituximab plus methotrexate reached ACR50 at week 24, versus 13% on methotrexate alone?", ["13%", "85%", "43%", "5%"],
  "A single course of two rituximab infusions more than tripled the ACR50 response compared with methotrexate alone.", "43%."),
 ("En el ensayo de 2004 de rituximab en artritis reumatoide, ¿qué proporción con rituximab más metotrexato alcanzó ACR50 a la semana 24, frente al 13% con metotrexato solo?", ["13%", "85%", "43%", "5%"],
  "Un solo ciclo de dos infusiones de rituximab más que triplicó la respuesta ACR50 frente a metotrexato solo.", "43%.")),

# --- ATTRACT infliximab (10622295)
("10622295", "curious", 3, "infliximab, a chimeric human-mouse anti-TNFalpha monoclonal antibody",
 ("In the ATTRACT trial in rheumatoid arthritis, what kind of drug was infliximab?", ["A fully human anti-IL-1 antibody", "A soluble TNF receptor fusion protein", "A small-molecule JAK inhibitor", "A chimeric anti-TNF antibody"],
  "Infliximab is a chimeric monoclonal antibody against TNF-alpha, tested on top of methotrexate.", "Chimeric anti-TNF mAb."),
 ("En el ensayo ATTRACT en artritis reumatoide, ¿qué tipo de fármaco era infliximab?", ["Un anticuerpo anti-IL-1 totalmente humano", "Una proteína de fusión con receptor de TNF", "Un inhibidor de JAK de molécula pequeña", "Un anticuerpo quimérico anti-TNF"],
  "Infliximab es un anticuerpo monoclonal quimérico contra el TNF-alfa, probado junto con metotrexato.", "Anti-TNF quimérico.")),
("10622295", "researcher", 0, "compared with 20% of patients receiving placebo plus methotrexate",
 ("In ATTRACT, about half of patients on infliximab plus methotrexate reached ACR20 at 30 weeks. What share reached it on placebo plus methotrexate?", ["20%", "50%", "5%", "75%"],
  "ACR20 was 50-58% across infliximab regimens versus 20% with placebo plus methotrexate.", "20%."),
 ("En ATTRACT, cerca de la mitad de los pacientes con infliximab más metotrexato logró ACR20 a las 30 semanas. ¿Qué proporción lo logró con placebo más metotrexato?", ["20%", "50%", "5%", "75%"],
  "El ACR20 fue del 50-58% con los esquemas de infliximab frente al 20% con placebo más metotrexato.", "20%.")),

# --- Rituximab in MS, HERMES (18272891)
("18272891", "explorer", 1, "A single course of rituximab reduced inflammatory brain lesions and clinical relapses for 48 weeks",
 ("What did the phase 2 trial of rituximab in relapsing-remitting multiple sclerosis (2008) show?", ["No effect on MRI brain lesions", "Fewer brain lesions and relapses", "More relapses than with placebo", "Benefit seen only after a second year"],
  "One course of B-cell depletion reduced gadolinium-enhancing lesions and relapses for 48 weeks.", "Fewer lesions and relapses."),
 ("¿Qué mostró el ensayo de fase 2 de rituximab en esclerosis múltiple remitente-recurrente (2008)?", ["Ningún efecto en las lesiones vistas por RM", "Menos lesiones cerebrales y recaídas", "Más recaídas que con placebo", "Beneficio solo tras un segundo año"],
  "Un ciclo de depleción de células B redujo las lesiones captantes de gadolinio y las recaídas durante 48 semanas.", "Menos lesiones y recaídas.")),
("18272891", "researcher", 2, "The data provide evidence of B-cell involvement in the pathophysiology of relapsing-remitting multiple sclerosis",
 ("What broader conclusion about multiple sclerosis did the 2008 rituximab trial support?", ["MS is driven only by CD8 T cells", "Antibodies are irrelevant to MS", "B cells take part in MS disease", "MS is caused by a viral infection"],
  "Because depleting CD20+ B cells worked, the trial pointed to B cells as players in relapsing MS, not only T cells.", "B cells are involved."),
 ("¿Qué conclusión más amplia sobre la esclerosis múltiple apoyó el ensayo de rituximab de 2008?", ["La EM depende solo de linfocitos T CD8", "Los anticuerpos son irrelevantes en la EM", "Las células B participan en la EM", "La EM es causada por una infección viral"],
  "Como depletar células B CD20+ funcionó, el ensayo señaló a las células B como actores en la EM recurrente, no solo a las T.", "Participan las células B.")),

# --- OPERA ocrelizumab (28002679)
("28002679", "researcher", 3, "46% lower rate with ocrelizumab",
 ("In the OPERA I trial, how did the annualized relapse rate with ocrelizumab (anti-CD20) compare with interferon beta-1a?", ["About the same rate", "Twice as high with ocrelizumab", "About 10% lower", "46% lower with ocrelizumab"],
  "Relapse rates were 0.16 versus 0.29, and gadolinium-enhancing lesions fell by about 94%.", "46% lower."),
 ("En el ensayo OPERA I, ¿cómo fue la tasa anualizada de recaídas con ocrelizumab (anti-CD20) frente a interferón beta-1a?", ["Más o menos la misma tasa", "El doble con ocrelizumab", "Cerca de un 10% menor con ocrelizumab", "46% menor con ocrelizumab"],
  "Las tasas fueron 0,16 frente a 0,29, y las lesiones captantes de gadolinio cayeron cerca de un 94%.", "46% menor.")),

# --- LEAP-On (26942922)
("26942922", "explorer", 0, "a 12-month period of peanut avoidance was not associated with an increase in the prevalence of peanut allergy",
 ("In LEAP-On, children who had eaten peanut from infancy to age 5 then avoided it for 12 months. What happened to their peanut allergy rate?", ["No significant increase", "It rose to match the avoiders", "It tripled within six months", "It fell to exactly zero"],
  "Allergy went from 3.6% to 4.8% (not significant), versus 18.6% in the original avoidance group.", "No significant increase."),
 ("En LEAP-On, niños que comieron maní desde la infancia hasta los 5 años lo evitaron luego por 12 meses. ¿Qué pasó con su tasa de alergia al maní?", ["No aumentó significativamente", "Subió hasta igualar al grupo evitador", "Se triplicó en seis meses", "Bajó exactamente a cero"],
  "La alergia pasó del 3,6% al 4,8% (no significativo), frente al 18,6% en el grupo que había evitado el maní.", "Sin aumento significativo.")),
("26942922", "expert", 1, "participants in the peanut-consumption group continued to have a higher level of peanut-specific IgG4 and a higher peanut-specific IgG4:IgE ratio",
 ("Which immune marker remained higher in the LEAP-On peanut-consumption group after a year of avoidance?", ["Total serum IgE level", "Peanut-specific IgG4", "Ara h2-specific IgE", "Blood eosinophil count"],
  "Early peanut eaters kept a tolerance-associated IgG4 profile and had less Ara h2-specific IgE.", "Peanut-specific IgG4."),
 ("¿Qué marcador inmunitario siguió más alto en el grupo de consumo de maní de LEAP-On tras un año sin comerlo?", ["IgE sérica total", "IgG4 específica de maní", "IgE específica de Ara h2", "Recuento de eosinófilos en sangre"],
  "Quienes comieron maní temprano mantuvieron un perfil de IgG4 asociado a tolerancia y menos IgE contra Ara h2.", "IgG4 específica de maní.")),

# --- EAT trial (26943128)
("26943128", "researcher", 2, "The trial did not show the efficacy of early introduction of allergenic foods in an intention-to-treat analysis",
 ("In the EAT trial, breast-fed infants were introduced to six allergenic foods from 3 months of age. What did the intention-to-treat analysis show?", ["A 90% cut in all food allergies", "More allergies with early introduction", "No significant efficacy overall", "Protection against milk allergy only"],
  "Food allergy was 5.6% versus 7.1% (P=0.32); adherence to early introduction was difficult.", "No significant effect."),
 ("En el ensayo EAT se introdujeron seis alimentos alergénicos desde los 3 meses a lactantes amamantados. ¿Qué mostró el análisis por intención de tratar?", ["Un 90% menos de alergias alimentarias", "Más alergias con la introducción temprana", "Ninguna eficacia significativa", "Protección solo contra alergia a la leche"],
  "La alergia alimentaria fue del 5,6% frente al 7,1% (P=0,32); la adherencia a la introducción temprana fue difícil.", "Sin efecto significativo.")),
("26943128", "expert", 3, "as was the prevalence of peanut allergy (0% vs. 2.5%, P=0.003) and egg allergy (1.4% vs. 5.5%, P=0.009)",
 ("In the EAT trial's per-protocol analysis, for which foods did early introduction significantly lower allergy?", ["Milk and wheat", "Sesame and whitefish", "All six foods equally", "Peanut and egg"],
  "Per protocol, peanut allergy was 0% versus 2.5% and egg allergy 1.4% versus 5.5%; milk, sesame, fish and wheat showed no effect.", "Peanut and egg."),
 ("En el análisis por protocolo del ensayo EAT, ¿para qué alimentos la introducción temprana redujo significativamente la alergia?", ["Leche y trigo", "Sésamo y pescado blanco", "Los seis alimentos por igual", "Maní y huevo"],
  "Por protocolo, la alergia al maní fue 0% frente a 2,5% y al huevo 1,4% frente a 5,5%; leche, sésamo, pescado y trigo no mostraron efecto.", "Maní y huevo.")),

# --- Farm microbes and asthma, PARSIFAL/GABRIELA (21345099)
("21345099", "explorer", 0, "diversity of microbial exposure was inversely related to the risk of asthma",
 ("In the PARSIFAL and GABRIELA studies of farm children, how was the diversity of environmental microbes related to asthma?", ["Inversely related to asthma risk", "Directly related to asthma risk", "Unrelated to either asthma or atopy", "Related only to eczema risk"],
  "Farm children were exposed to more kinds of microbes, and greater diversity went with lower asthma risk.", "Inversely."),
 ("En los estudios PARSIFAL y GABRIELA en niños de granja, ¿cómo se relacionó la diversidad de microbios ambientales con el asma?", ["Inversamente con el riesgo de asma", "Directamente con el riesgo de asma", "Sin relación con el asma ni con la atopia", "Solo con el riesgo de eccema"],
  "Los niños de granja estaban expuestos a más tipos de microbios, y la mayor diversidad se asoció a menos asma.", "Inversamente.")),
("21345099", "researcher", 1, "samples of mattress dust were screened for bacterial DNA",
 ("In the PARSIFAL farm study on childhood asthma, what samples were screened for bacterial DNA to measure microbial exposure?", ["Stool of the children", "Dust from mattresses", "Nasal swabs of mothers", "Raw milk from farms"],
  "Mattress dust was analyzed by SSCP to detect bacteria that cannot be cultured; GABRIELA cultured settled room dust.", "Mattress dust."),
 ("En el estudio PARSIFAL sobre asma infantil en granjas, ¿qué muestras se analizaron buscando ADN bacteriano para medir la exposición microbiana?", ["Heces de los niños", "Polvo de los colchones", "Hisopados nasales maternos", "Leche cruda de granja"],
  "El polvo de colchón se analizó por SSCP para detectar bacterias no cultivables; GABRIELA cultivó el polvo depositado en las habitaciones.", "Polvo de colchón.")),

# --- BNT162b2 trial through 6 months (34525277)
("34525277", "curious", 2, "Vaccine efficacy against Covid-19 was 91.3% (95% confidence interval [CI], 89.0 to 93.2) through 6 months of follow-up",
 ("In the 6-month follow-up of the pivotal BNT162b2 (Pfizer-BioNTech) mRNA vaccine trial, what was the efficacy against Covid-19?", ["50.2%", "70.4%", "91.3%", "62.8%"],
  "Efficacy stayed above 90% through 6 months, with a gradual decline over time; efficacy against severe disease was 96.7%.", "91.3%."),
 ("En el seguimiento a 6 meses del ensayo clave de la vacuna de ARNm BNT162b2 (Pfizer-BioNTech), ¿cuál fue la eficacia contra la Covid-19?", ["50,2%", "70,4%", "91,3%", "62,8%"],
  "La eficacia siguió por encima del 90% a 6 meses, con un descenso gradual; contra la enfermedad grave fue del 96,7%.", "91,3%.")),
("34525277", "researcher", 3, "BNT162b2 is a lipid nanoparticle-formulated, nucleoside-modified RNA vaccine",
 ("How is the BNT162b2 Covid-19 vaccine described in its 6-month safety and efficacy report?", ["Inactivated whole SARS-CoV-2 virus", "Adenovirus vector carrying spike DNA", "Recombinant spike protein with alum", "Modified RNA in lipid nanoparticles"],
  "It is nucleoside-modified mRNA encoding a prefusion-stabilized full-length spike, delivered in lipid nanoparticles.", "Modified mRNA in LNPs."),
 ("¿Cómo se describe la vacuna BNT162b2 contra la Covid-19 en su informe de seguridad y eficacia a 6 meses?", ["Virus SARS-CoV-2 entero inactivado", "Adenovirus vector con ADN de la espiga", "Proteína espiga recombinante adyuvada con alumbre", "ARN modificado en nanopartículas lipídicas"],
  "Es un ARNm con nucleósidos modificados que codifica la espiga completa estabilizada en prefusión, en nanopartículas lipídicas.", "ARNm modificado en LNP.")),

# --- mRNA-1273 COVE trial (33378609)
("33378609", "explorer", 1, "vaccine efficacy was 94.1% (95% CI, 89.3 to 96.8%; P<0.001)",
 ("In the phase 3 COVE trial of the Moderna mRNA-1273 vaccine, what efficacy was observed against symptomatic Covid-19?", ["62.3%", "94.1%", "75.6%", "50.8%"],
  "Symptomatic Covid-19 occurred in 185 placebo recipients versus 11 vaccine recipients.", "94.1%."),
 ("En el ensayo de fase 3 COVE de la vacuna mRNA-1273 de Moderna, ¿qué eficacia se observó contra la Covid-19 sintomática?", ["62,3%", "94,1%", "75,6%", "50,8%"],
  "Hubo Covid-19 sintomática en 185 receptores de placebo frente a 11 vacunados.", "94,1%.")),
("33378609", "researcher", 0, "Severe Covid-19 occurred in 30 participants, with one fatality; all 30 were in the placebo group",
 ("In the mRNA-1273 COVE trial, how were the 30 cases of severe Covid-19 distributed between groups?", ["All 30 in the placebo group", "Split evenly across both groups", "Most in the vaccine group", "20 placebo and 10 vaccine"],
  "No vaccine recipient developed severe Covid-19; the one death was in the placebo group.", "All placebo."),
 ("En el ensayo COVE de mRNA-1273, ¿cómo se repartieron los 30 casos de Covid-19 grave entre los grupos?", ["Los 30 en el grupo placebo", "Igual en ambos grupos", "La mayoría en el grupo vacunado", "20 con placebo y 10 vacunados"],
  "Ningún vacunado tuvo Covid-19 grave; la única muerte fue en el grupo placebo.", "Todos con placebo.")),

# --- HPV vaccination programmes: population impact meta-analysis (31255301)
("31255301", "explorer", 2, "the prevalence of HPV 16 and 18 decreased significantly by 83% (RR 0·17, 95% CI 0·11-0·25) among girls aged 13-19 years",
 ("In the 2019 meta-analysis of HPV vaccination programmes in 14 high-income countries, how much did HPV 16/18 prevalence fall among girls aged 13-19 after 5-8 years?", ["12%", "31%", "83%", "48%"],
  "HPV 16/18 prevalence fell by 83% in girls 13-19 and by 66% in women 20-24 after 5-8 years of vaccination.", "83%."),
 ("En el metaanálisis de 2019 sobre programas de vacunación contra el VPH en 14 países de altos ingresos, ¿cuánto bajó la prevalencia de VPH 16/18 en niñas de 13 a 19 años tras 5-8 años?", ["12%", "31%", "83%", "48%"],
  "La prevalencia de VPH 16/18 cayó un 83% en niñas de 13-19 años y un 66% en mujeres de 20-24 tras 5-8 años de vacunación.", "83%.")),
("31255301", "researcher", 3, "Among boys aged 15-19 years anogenital wart diagnoses decreased significantly by 48%",
 ("In the 2019 meta-analysis of programmes that vaccinated girls against HPV, what happened to anogenital wart diagnoses in boys aged 15-19?", ["They rose by about 20%", "They did not change at all", "They were not studied", "They fell by 48%"],
  "Boys were not the main target, so the fall reflects herd effects of vaccinating girls.", "Fell 48% (herd effect)."),
 ("En el metaanálisis de 2019 de programas que vacunaron niñas contra el VPH, ¿qué pasó con los diagnósticos de verrugas anogenitales en varones de 15 a 19 años?", ["Subieron cerca de un 20%", "No cambiaron en absoluto", "No se estudiaron", "Bajaron un 48%"],
  "Los varones no eran el objetivo principal, así que la caída refleja el efecto rebaño de vacunar a las niñas.", "Bajaron 48% (efecto rebaño).")),

# --- HPV programme in England (34741816)
("34741816", "explorer", 1, "87% (72-94) for age 12-13 years (school year 8)",
 ("In England's bivalent HPV vaccination programme, what reduction in cervical cancer was estimated for women offered the vaccine at age 12-13?", ["34%", "87%", "100%", "15%"],
  "Reductions were 34% when offered at 16-18, 62% at 14-16 and 87% at 12-13 years.", "87%."),
 ("En el programa inglés de vacuna bivalente contra el VPH, ¿qué reducción de cáncer cervical se estimó en mujeres a quienes se ofreció a los 12-13 años?", ["34%", "87%", "100%", "15%"],
  "Las reducciones fueron del 34% si se ofreció a los 16-18, 62% a los 14-16 y 87% a los 12-13 años.", "87%.")),
("34741816", "curious", 2, "Human papillomavirus (HPV) immunisation with a bivalent vaccine (Cervarix) was introduced in England, UK, in Sept 1, 2008",
 ("Which HPV vaccine did England's national programme use when it started in 2008?", ["Nonavalent Gardasil 9", "Quadrivalent Gardasil", "Bivalent Cervarix", "A live attenuated HPV vaccine"],
  "England began with the bivalent vaccine for girls aged 12-13, with catch-up up to age 18.", "Cervarix."),
 ("¿Qué vacuna contra el VPH usó el programa nacional de Inglaterra cuando comenzó en 2008?", ["Gardasil 9 nonavalente", "Gardasil tetravalente", "Cervarix bivalente", "Una vacuna de VPH viva atenuada"],
  "Inglaterra empezó con la vacuna bivalente para niñas de 12-13 años, con recuperación hasta los 18.", "Cervarix.")),

# --- BCG trained immunity in humans (22988082)
("22988082", "researcher", 0, "These training effects were induced through the NOD2 receptor and mediated by increased histone 3 lysine 4 trimethylation",
 ("In the 2012 study showing that BCG induces trained immunity in human monocytes, which receptor and epigenetic mark were involved?", ["NOD2 and H3K4 trimethylation", "TLR9 and DNA methylation", "Dectin-1 and H3K27 acetylation", "TLR3 and histone deacetylation"],
  "BCG trained monocytes through NOD2 sensing, with increased H3K4me3 at cytokine gene loci.", "NOD2 and H3K4me3."),
 ("En el estudio de 2012 que mostró que la BCG induce inmunidad entrenada en monocitos humanos, ¿qué receptor y marca epigenética intervinieron?", ["NOD2 y trimetilación de H3K4", "TLR9 y metilación del ADN", "Dectina-1 y acetilación de H3K27", "TLR3 y desacetilación de histonas"],
  "La BCG entrenó a los monocitos mediante NOD2, con aumento de H3K4me3 en genes de citocinas.", "NOD2 y H3K4me3.")),
("22988082", "expert", 1, "BCG vaccination induced T- and B-lymphocyte-independent protection of severe combined immunodeficiency SCID mice from disseminated candidiasis",
 ("In the 2012 BCG trained-immunity paper, what did the experiment in SCID mice demonstrate?", ["BCG fails to work without T cells", "Protection without T or B cells", "BCG causes fatal disseminated infection", "Protection only through antibodies"],
  "SCID mice lack T and B cells, yet BCG gave 100% survival from disseminated candidiasis versus 30% in controls.", "Lymphocyte-independent protection."),
 ("En el artículo de 2012 sobre BCG e inmunidad entrenada, ¿qué demostró el experimento en ratones SCID?", ["La BCG fracasa sin linfocitos T", "Protección sin linfocitos T ni B", "La BCG causa infección diseminada fatal", "Protección solo mediante anticuerpos"],
  "Los ratones SCID carecen de linfocitos T y B, y aun así la BCG dio 100% de supervivencia a la candidiasis diseminada frente a 30% en controles.", "Protección sin linfocitos.")),

# --- BCG and yellow fever challenge (29324233)
("29324233", "expert", 2, "Reduction of viremia was highly correlated with the upregulation of IL-1β",
 ("In the randomized human challenge study where BCG protected against yellow fever vaccine virus, what correlated with reduced viremia?", ["The specific IFN-gamma response", "Neutralizing antibody titers", "Upregulation of IL-1 beta", "Higher CD8 T-cell counts"],
  "Reduced viremia tracked IL-1 beta, a trained-immunity cytokine, and not the specific IFN-gamma response.", "IL-1 beta."),
 ("En el estudio de desafío humano aleatorizado en que la BCG protegió contra el virus vacunal de la fiebre amarilla, ¿qué se correlacionó con menor viremia?", ["La respuesta específica de IFN-gamma", "Los títulos de anticuerpos neutralizantes", "El aumento de IL-1 beta", "Más linfocitos T CD8"],
  "La menor viremia siguió a la IL-1 beta, una citocina de inmunidad entrenada, y no a la respuesta específica de IFN-gamma.", "IL-1 beta.")),

# --- BRACE trial (37099341)
("37099341", "explorer", 3, "Vaccination with BCG-Denmark did not result in a lower risk of Covid-19 among health care workers than placebo",
 ("What did the BRACE randomized trial of BCG vaccine in health care workers find for Covid-19?", ["It halved symptomatic Covid-19", "It prevented all severe Covid-19", "It protected only the older health workers", "No lower Covid-19 risk than placebo"],
  "Symptomatic Covid-19 by 6 months was 14.7% with BCG versus 12.3% with placebo, a non-significant difference.", "No protection."),
 ("¿Qué encontró el ensayo aleatorizado BRACE de vacuna BCG en trabajadores de salud respecto a la Covid-19?", ["Redujo a la mitad la Covid-19 sintomática", "Evitó toda la Covid-19 grave", "Protegió solo a trabajadores mayores", "Sin menor riesgo que el placebo"],
  "La Covid-19 sintomática a 6 meses fue del 14,7% con BCG frente al 12,3% con placebo, sin diferencia significativa.", "Sin protección.")),

# --- ZOE-50 zoster vaccine (25916341)
("25916341", "explorer", 0, "Vaccine efficacy was between 96.6% and 97.9% for all age groups",
 ("In the ZOE-50 trial of the adjuvanted herpes zoster subunit vaccine (HZ/su), how did efficacy vary across age groups from 50 to over 70?", ["Stayed about 97% in all groups", "Fell below 50% after age 70", "Was highest only in those over 70 years", "Was near zero after age 60"],
  "The gE/AS01B vaccine overcame the usual age-related decline in vaccine response.", "Similar in all ages."),
 ("En el ensayo ZOE-50 de la vacuna de subunidad adyuvada contra el herpes zóster (HZ/su), ¿cómo varió la eficacia entre los grupos de 50 a más de 70 años?", ["Fue cerca del 97% en todos", "Cayó bajo el 50% tras los 70", "Fue máxima solo tras los 70", "Fue casi nula tras los 60"],
  "La vacuna gE/AS01B superó la caída habitual de la respuesta vacunal con la edad.", "Similar en todas las edades.")),

# --- ZOE-70 (27626517)
("27626517", "researcher", 1, "was similar in participants 70 to 79 years of age (90.0%) and participants 80 years of age or older (89.1%)",
 ("In ZOE-70, how did herpes zoster subunit vaccine efficacy in adults 80 or older compare with those aged 70-79?", ["Much lower, around 40%", "Similar, about 89-90%", "Higher, close to 100%", "Not measurable in that group"],
  "Efficacy stayed near 90% even in people 80 or older, despite immunosenescence.", "Similar, ~90%."),
 ("En ZOE-70, ¿cómo fue la eficacia de la vacuna de subunidad contra el zóster en mayores de 80 años frente a los de 70-79?", ["Mucho menor, cerca del 40%", "Similar, cerca del 89-90%", "Mayor, cerca del 100%", "No medible en ese grupo"],
  "La eficacia se mantuvo cerca del 90% incluso en mayores de 80, pese a la inmunosenescencia.", "Similar, ~90%.")),

# --- High-dose influenza vaccine (25119609)
("25119609", "researcher", 2, "relative efficacy, 24.2%; 95% confidence interval [CI], 9.7 to 36.5",
 ("In the trial of high-dose (60 μg) versus standard-dose influenza vaccine in adults 65 or older, what was the relative efficacy of high dose?", ["75.0%", "2.4%", "24.2%", "50.5%"],
  "High dose gave higher antibody titers and 24% fewer laboratory-confirmed influenza cases than standard dose.", "24.2%."),
 ("En el ensayo de vacuna antigripal en dosis alta (60 μg) frente a dosis estándar en mayores de 65 años, ¿cuál fue la eficacia relativa de la dosis alta?", ["75,0%", "2,4%", "24,2%", "50,5%"],
  "La dosis alta dio títulos de anticuerpos más altos y 24% menos casos de gripe confirmada que la estándar.", "24,2%.")),

# --- Kidney tolerance, Massachusetts (18216355)
("18216355", "researcher", 3, "it was possible to discontinue all immunosuppressive therapy 9 to 14 months after the transplantation",
 ("In the 2008 report of HLA-mismatched combined bone marrow and kidney transplants, what was achieved in four of five recipients?", ["Permanent and complete donor chimerism", "Graft loss from GVHD", "Lifelong high-dose steroids", "Stopping all immunosuppression"],
  "Despite only transient chimerism, four patients stopped immunosuppression and kept stable kidney function for 2-5 years.", "Off immunosuppression."),
 ("En el informe de 2008 de trasplantes combinados de médula ósea y riñón con HLA incompatible, ¿qué se logró en cuatro de cinco receptores?", ["Quimerismo donante completo y permanente", "Pérdida del injerto por EICH", "Corticoides en dosis altas de por vida", "Suspender toda la inmunosupresión"],
  "Pese a un quimerismo solo transitorio, cuatro pacientes dejaron la inmunosupresión y mantuvieron función renal estable 2-5 años.", "Sin inmunosupresión.")),

# --- Kidney tolerance, Stanford (18216356)
("18216356", "expert", 0, "A post-transplantation conditioning regimen of total lymphoid irradiation and antithymocyte globulin allowed engraftment of the donor's hematopoietic cells",
 ("In the 2008 Stanford case of tolerance after combined kidney and hematopoietic-cell transplantation, what conditioning allowed donor cell engraftment?", ["Lymphoid irradiation plus ATG", "Myeloablative busulfan alone", "Rituximab plus plasmapheresis", "High-dose IVIG plus corticosteroids"],
  "Total lymphoid irradiation with antithymocyte globulin led to persistent mixed chimerism and normal graft function off drugs.", "TLI plus ATG."),
 ("En el caso de Stanford de 2008 de tolerancia tras trasplante combinado de riñón y células hematopoyéticas, ¿qué acondicionamiento permitió el injerto de células del donante?", ["Irradiación linfoide total más ATG", "Busulfán mieloablativo solo", "Rituximab más plasmaféresis repetida", "IGIV en dosis altas y corticoides"],
  "La irradiación linfoide total con globulina antitimocítica llevó a quimerismo mixto persistente y función renal normal sin fármacos.", "ILT más ATG.")),

# --- Facilitating cells (22399264)
("22399264", "expert", 1, "enriched for hematopoietic stem cells (HSCs) and tolerogenic graft facilitating cells (FCs)",
 ("In the 2012 HLA-mismatched kidney plus stem cell transplant study, what was the bioengineered cell product enriched for?", ["Regulatory T cells and NK cells", "HSCs and graft facilitating cells", "Mesenchymal stromal cells only", "Donor dendritic cells and memory B cells"],
  "The product combined stem cells with tolerogenic facilitating cells; five recipients came off all immunosuppression without GVHD.", "HSCs and facilitating cells."),
 ("En el estudio de 2012 de trasplante de riñón más células madre con HLA incompatible, ¿en qué estaba enriquecido el producto celular bioingenierizado?", ["Linfocitos T reguladores y células NK", "CPH y células facilitadoras del injerto", "Solo células estromales mesenquimales del donante", "Células dendríticas y B del donante"],
  "El producto combinó células madre con células facilitadoras tolerogénicas; cinco receptores dejaron la inmunosupresión sin EICH.", "CPH y células facilitadoras.")),
]
