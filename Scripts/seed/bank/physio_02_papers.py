# Human physiology II — leptin and ghrelin, renin-angiotensin-aldosterone system and captopril,
# primary aldosteronism, cortisone and the adrenal cortex, HPA axis and stress, calcium/PTH/vitamin D,
# FGF23, RANKL and bone remodeling, bile acids and FXR, gastric proton pump, oxytocin and milk ejection,
# pregnancy physiology, SGLT2 and renal glucose reabsorption, renal autoregulation, countercurrent
# multiplier, potassium balance.
# Sources: PubMed paper and review abstracts. Excerpts verbatim.
CATEGORY = "humanPhysiology"
Q = [
# --- Positional cloning of the ob gene (7984236)
("7984236", "beginner", 0, "The ob gene product may function as part of a signalling pathway from adipose tissue that acts to regulate the size of the body fat depot",
 ("In the 1994 positional cloning of the mouse obese (ob) gene, which tissue was the ob gene product proposed to signal from?", ["Adipose tissue", "Skeletal muscle", "The pancreas", "The thyroid gland"],
  "The ob product (later named leptin) was proposed to be a signal from fat tissue that regulates the size of the body fat depot.", "Fat tissue."),
 ("En la clonación posicional del gen obese (ob) del ratón en 1994, ¿desde qué tejido se propuso que señalizaba el producto del gen ob?", ["Tejido adiposo", "Músculo esquelético", "El páncreas", "La glándula tiroides"],
  "Se propuso que el producto de ob (luego llamado leptina) era una señal del tejido graso que regula el tamaño del depósito de grasa.", "Tejido graso.")),
("7984236", "curious", 1, "Mutation of ob results in profound obesity and type II diabetes",
 ("According to the 1994 ob gene cloning paper, what does mutation of the mouse ob gene cause?", ["Severe weight loss", "Obesity and type II diabetes", "Dwarfism and severe hypothyroidism", "Anemia and kidney failure"],
  "Loss of the ob gene causes profound obesity and type II diabetes, a syndrome resembling human morbid obesity.", "Obesity and diabetes."),
 ("Según el artículo de clonación del gen ob de 1994, ¿qué causa la mutación del gen ob del ratón?", ["Pérdida severa de peso", "Obesidad y diabetes tipo II", "Enanismo e hipotiroidismo", "Anemia e insuficiencia renal"],
  "La pérdida del gen ob causa obesidad profunda y diabetes tipo II, un síndrome parecido a la obesidad mórbida humana.", "Obesidad y diabetes.")),

# --- Weight-reducing effects of OB protein (7624777)
("7624777", "explorer", 2, "reduced the body weight of ob/ob mice by 30 percent after 2 weeks of treatment with no apparent toxicity but had no effect on db/db mice",
 ("In the 1995 study injecting recombinant OB protein (leptin), how did ob/ob and db/db mice respond?", ["Both lost about 30% of body weight", "Neither strain changed weight", "ob/ob lost 30%; db/db unaffected", "db/db lost 30%; ob/ob unaffected"],
  "ob/ob mice, which lack the protein, lost 30% of their weight in 2 weeks, whereas db/db mice, thought to be resistant to it, did not respond.", "Only ob/ob lost weight."),
 ("En el estudio de 1995 que inyectó proteína OB recombinante (leptina), ¿cómo respondieron los ratones ob/ob y db/db?", ["Ambas perdieron un 30% del peso", "Ninguna cepa cambió de peso", "ob/ob perdió 30%; db/db sin efecto", "db/db perdió 30%; ob/ob sin efecto"],
  "Los ratones ob/ob, que carecen de la proteína, perdieron 30% del peso en 2 semanas; los db/db, considerados resistentes, no respondieron.", "Solo adelgazaron los ob/ob.")),
("7624777", "researcher", 3, "a reduction of body fat from 12.2 to 0.7 percent",
 ("When normal wild-type mice were injected twice daily with mouse OB protein, what happened to their body fat?", ["Rose from 12.2% to 20%", "Stayed the same throughout", "Doubled within a week", "Fell from 12.2% to 0.7%"],
  "Even lean wild-type mice lost weight, ate less and their body fat dropped from 12.2% to 0.7%.", "Fell to 0.7%."),
 ("Cuando se inyectó proteína OB de ratón dos veces al día a ratones normales, ¿qué pasó con su grasa corporal?", ["Subió de 12,2% a 20%", "No cambió en absoluto", "Se duplicó en una semana", "Bajó de 12,2% a 0,7%"],
  "Incluso los ratones normales delgados bajaron de peso, comieron menos y su grasa cayó de 12,2% a 0,7%.", "Bajó a 0,7%.")),

# --- Serum leptin in obese humans (8532024)
("8532024", "explorer", 0, "Serum leptin concentrations are correlated with the percentage of body fat, suggesting that most obese persons are insensitive to endogenous leptin production",
 ("In the 1996 NEJM study measuring serum leptin in 275 people, what did obese subjects show?", ["High leptin, suggesting resistance", "Undetectable leptin levels", "Leptin levels identical to lean subjects", "Low leptin due to ob mutations"],
  "Obese subjects averaged 31.3 vs 7.5 ng/mL in lean people; leptin tracked body fat, implying insensitivity rather than deficiency.", "High leptin."),
 ("En el estudio del NEJM de 1996 que midió leptina sérica en 275 personas, ¿qué mostraron los sujetos obesos?", ["Leptina alta: posible resistencia", "Leptina indetectable", "Leptina igual a la de los delgados", "Leptina baja por mutaciones en ob"],
  "Los obesos tenían 31,3 frente a 7,5 ng/mL en los delgados; la leptina seguía a la grasa corporal, lo que indica insensibilidad y no déficit.", "Leptina alta.")),

# --- Congenital leptin deficiency (9202122)
("9202122", "researcher", 1, "a homozygous frame-shift mutation involving the deletion of a single guanine nucleotide in codon 133 of the gene for leptin was found",
 ("What was found in the two severely obese children from a consanguineous family described in the 1997 report of congenital leptin deficiency?", ["Very high serum leptin levels", "A homozygous leptin frameshift", "A leptin receptor deletion", "An extra copy of the whole ob gene"],
  "Both children had very low leptin and a single-guanine deletion in codon 133, the first genetic evidence that leptin regulates human energy balance.", "Leptin frameshift."),
 ("¿Qué se encontró en los dos niños con obesidad severa de una familia consanguínea descritos en 1997 con déficit congénito de leptina?", ["Niveles muy altos de leptina sérica", "Una mutación homocigota en leptina", "Una deleción del receptor de leptina", "Una copia extra del gen ob"],
  "Ambos tenían leptina muy baja y la deleción de una guanina en el codón 133, primera prueba genética de que la leptina regula el balance energético humano.", "Mutación en leptina.")),

# --- Discovery of ghrelin (10604470)
("10604470", "beginner", 2, "We now report the purification and identification in rat stomach of an endogenous ligand specific for GHS-R",
 ("In which organ was ghrelin, the natural ligand of the growth hormone secretagogue receptor, first purified in 1999?", ["The liver", "The pancreas", "The stomach", "The hypothalamus"],
  "Kojima and colleagues purified ghrelin from rat stomach; it releases growth hormone and was later shown to stimulate appetite.", "The stomach."),
 ("¿En qué órgano se purificó por primera vez en 1999 la grelina, ligando natural del receptor de secretagogos de hormona de crecimiento?", ["El hígado", "El páncreas", "El estómago", "El hipotálamo"],
  "Kojima y colaboradores purificaron la grelina del estómago de rata; libera hormona de crecimiento y luego se vio que estimula el apetito.", "El estómago.")),
("10604470", "researcher", 3, "O-n-octanoylation at serine 3 is essential for the activity",
 ("What chemical modification did Kojima and colleagues find essential for ghrelin's growth hormone-releasing activity?", ["Glycosylation of asparagine", "Phosphorylation of tyrosine", "C-terminal amidation", "Octanoylation of serine 3"],
  "Ghrelin is a 28-amino-acid peptide whose serine 3 carries an n-octanoyl group required for activity.", "Serine-3 octanoylation."),
 ("¿Qué modificación química hallaron Kojima y colaboradores como esencial para que la grelina libere hormona de crecimiento?", ["Glicosilación de asparagina", "Fosforilación de tirosina", "Amidación C-terminal", "Octanoilación de la serina 3"],
  "La grelina es un péptido de 28 aminoácidos cuya serina 3 lleva un grupo n-octanoilo necesario para su actividad.", "Octanoilación de serina 3.")),

# --- Preprandial ghrelin rise (11473029)
("11473029", "explorer", 0, "Plasma ghrelin levels increased nearly twofold immediately before each meal and fell to trough levels within 1 h after eating",
 ("In the 2001 study sampling blood 38 times over 24 h in 10 healthy subjects, how did plasma ghrelin behave around meals?", ["Nearly doubled before meals", "Peaked about 2 h after meals", "Stayed flat all day", "Rose only during sleep"],
  "Ghrelin rose almost twofold just before each meal and fell within an hour after eating, supporting a role in meal initiation.", "Rose before meals."),
 ("En el estudio de 2001 que tomó sangre 38 veces en 24 h a 10 sujetos sanos, ¿cómo se comportó la grelina plasmática con las comidas?", ["Casi se duplicó antes de comer", "Llegó al máximo 2 h tras comer", "Se mantuvo plana todo el día", "Subió solo durante el sueño"],
  "La grelina casi se duplicó justo antes de cada comida y cayó en una hora después de comer, lo que apoya un papel en el inicio de la ingesta.", "Subió antes de comer.")),
("11473029", "researcher", 1, "Intermeal ghrelin levels displayed a diurnal rhythm that was exactly in phase with that of leptin",
 ("In Cummings' 2001 ghrelin study, which hormone's diurnal rhythm was exactly in phase with intermeal ghrelin levels?", ["Insulin", "Leptin", "Cortisol", "Melatonin"],
  "Between meals, ghrelin and leptin both rose through the day to a peak at 01:00 and fell overnight; insulin was reciprocal to ghrelin around meals.", "Leptin."),
 ("En el estudio de grelina de Cummings de 2001, ¿el ritmo diario de qué hormona estuvo exactamente en fase con la grelina entre comidas?", ["Insulina", "Leptina", "Cortisol", "Melatonina"],
  "Entre comidas, grelina y leptina subieron durante el día hasta un pico a la 01:00 y bajaron de noche; la insulina fue recíproca a la grelina.", "Leptina.")),

# --- Ghrelin infusion in humans (11739476)
("11739476", "explorer", 2, "There was a clear-cut increase in energy consumed by every individual from a free-choice buffet (mean increase 28 +/- 3.9%, p<0.001)",
 ("In the 2001 randomized crossover trial infusing ghrelin into nine healthy volunteers, what happened to food intake at a buffet?", ["It fell by about 28%", "No measurable change", "It rose by about 28%", "It rose in only half"],
  "Every volunteer ate more during ghrelin infusion, on average 28% more energy, making ghrelin the first circulating hormone shown to stimulate food intake in humans.", "Rose ~28%."),
 ("En el ensayo cruzado aleatorizado de 2001 que infundió grelina a nueve voluntarios sanos, ¿qué pasó con la ingesta en un bufé?", ["Bajó cerca de un 28%", "Ningún cambio medible", "Subió cerca de un 28%", "Subió solo en la mitad"],
  "Todos comieron más con la grelina, en promedio 28% más energía; fue la primera hormona circulante que estimuló la ingesta en humanos.", "Subió ~28%.")),

# --- Design of ACE inhibitors / captopril (191908)
("191908", "researcher", 3, "These compounds, carboxyalkanoyl and mercaptoalkanoyl derivatives of proline",
 ("Ondetti and colleagues' 1977 design of angiotensin-converting enzyme inhibitors, which led to captopril, produced derivatives of which amino acid?", ["Glycine", "Tryptophan", "Arginine", "Proline"],
  "The new inhibitors were carboxyalkanoyl and mercaptoalkanoyl derivatives of proline; the mercapto compound became captopril.", "Proline."),
 ("El diseño de inhibidores de la enzima convertidora de angiotensina de Ondetti y colaboradores (1977), que llevó al captopril, produjo derivados de ¿qué aminoácido?", ["Glicina", "Triptófano", "Arginina", "Prolina"],
  "Los nuevos inhibidores eran derivados carboxialcanoílo y mercaptoalcanoílo de la prolina; el compuesto mercapto se convirtió en el captopril.", "Prolina.")),
("191908", "explorer", 0, "A hypothetical model of the active site of angiotensin-converting enzyme, based on known chemical and kinetic properties of the enzyme, has enabled us to design a new class of potent and specific inhibitors",
 ("What approach did the 1977 Science paper use to design the first orally active ACE inhibitors?", ["A model of the enzyme's active site", "Random screening of soil microbe extracts", "Purifying an inhibitor from blood", "Modifying the structure of renin"],
  "The authors built a hypothetical active-site model of ACE from its known chemistry and kinetics, an early example of rational drug design.", "Active-site model."),
 ("¿Qué estrategia usó el artículo de Science de 1977 para diseñar los primeros inhibidores de la ECA activos por vía oral?", ["Un modelo del sitio activo de la enzima", "Tamizaje al azar de microbios del suelo", "Purificar un inhibidor de la sangre", "Modificar la estructura de la renina"],
  "Los autores construyeron un modelo hipotético del sitio activo de la ECA a partir de su química y cinética, un ejemplo temprano de diseño racional.", "Modelo del sitio activo.")),

# --- Long-term captopril in essential hypertension (90216)
("90216", "researcher", 1, "Captopril prevented and reversed the secondary hyperaldosteronism and hypokalaemia induced by simultaneous diuretic administration",
 ("In the 1979 Lancet study of long-term captopril in essential hypertension, what effect did captopril have when combined with a diuretic?", ["It worsened hypokalaemia", "It prevented hypokalaemia", "It raised plasma angiotensin II", "It raised urinary aldosterone"],
  "By blocking angiotensin II formation, captopril prevented diuretic-induced secondary hyperaldosteronism and low potassium, removing the need for potassium supplements.", "Prevented low potassium."),
 ("En el estudio de The Lancet de 1979 sobre captopril a largo plazo en hipertensión esencial, ¿qué efecto tuvo el captopril junto con un diurético?", ["Empeoró la hipopotasemia", "Previno la hipopotasemia", "Elevó la angiotensina II", "Elevó la aldosterona urinaria"],
  "Al bloquear la formación de angiotensina II, el captopril evitó el hiperaldosteronismo secundario y el potasio bajo del diurético, sin necesidad de suplementos.", "Previno el potasio bajo.")),

# --- History of the renin-angiotensin system (11751697)
("11751697", "curious", 2, "The history of the discovery of the renin-angiotensin system began in 1898 with the studies made by Tigerstedt and Bergman, who reported the pressor effect of renal extracts",
 ("What did Tigerstedt and Bergman report in 1898, launching the history of the renin-angiotensin system?", ["Adrenal extracts lowered blood pressure", "Liver extracts caused diuresis", "Kidney extracts raised blood pressure", "Lung extracts converted a peptide"],
  "They found that renal extracts had a pressor effect and named the active substance renin after the kidney.", "Kidney extracts raised BP."),
 ("¿Qué informaron Tigerstedt y Bergman en 1898, dando inicio a la historia del sistema renina-angiotensina?", ["Extractos suprarrenales bajaban la presión", "Extractos de hígado causaban diuresis", "Extractos renales subían la presión", "Extractos de pulmón convertían un péptido"],
  "Hallaron que los extractos de riñón tenían efecto presor y llamaron renina a la sustancia activa por su origen renal.", "Extractos renales elevaban la presión.")),
("11751697", "explorer", 3, "In 1958, Eduardo Braun Menéndez from Argentina and Irving H. Page from the United States agreed to name it angiotensin",
 ("The pressor peptide called 'hypertensin' in Buenos Aires and 'angiotonin' in the United States was renamed by agreement in 1958. What name was chosen?", ["Bradykinin", "Vasopressin", "Endothelin", "Angiotensin"],
  "Braun Menéndez (Argentina) and Page (USA) merged their two names into 'angiotensin'.", "Angiotensin."),
 ("El péptido presor llamado 'hipertensina' en Buenos Aires y 'angiotonina' en Estados Unidos fue renombrado de común acuerdo en 1958. ¿Qué nombre se eligió?", ["Bradicinina", "Vasopresina", "Endotelina", "Angiotensina"],
  "Braun Menéndez (Argentina) y Page (EE. UU.) fusionaron ambos nombres en 'angiotensina'.", "Angiotensina.")),

# --- Prevalence of primary aldosteronism (32449886)
("32449886", "researcher", 0, "corresponding adjusted prevalence estimates for biochemically overt primary aldosteronism were 11.3% (CI, 5.9% to 16.8%), 15.7% (CI, 8.6% to 22.9%), 21.6% (CI, 16.1% to 27.0%), and 22.0%",
 ("In the 2020 cross-sectional study at four US centers using oral sodium suppression testing, what was the approximate prevalence of overt primary aldosteronism in resistant hypertension?", ["About 22%", "Less than 1%", "About 2%", "Over 80%"],
  "Overt primary aldosteronism was found in about 22% with resistant hypertension, and even in 11% of normotensive participants.", "About 22%."),
 ("En el estudio transversal de 2020 en cuatro centros de EE. UU. con prueba de supresión oral de sodio, ¿cuál fue la prevalencia aproximada de hiperaldosteronismo primario manifiesto en hipertensión resistente?", ["Cerca del 22%", "Menos del 1%", "Cerca del 2%", "Más del 80%"],
  "Se halló hiperaldosteronismo primario manifiesto en cerca del 22% de los hipertensos resistentes, e incluso en el 11% de los normotensos.", "Cerca del 22%.")),
("32449886", "expert", 1, "The aldosterone-renin ratio had poor sensitivity and negative predictive value for detecting biochemically overt primary aldosteronism",
 ("What did the 2020 Annals study conclude about the aldosterone-renin ratio as a screen for primary aldosteronism?", ["It was nearly perfect", "It had poor sensitivity", "It was too costly to use", "It worked only with low potassium"],
  "The standard screening ratio missed many cases, with poor sensitivity and negative predictive value, so the disease is largely unrecognized.", "Poor sensitivity."),
 ("¿Qué concluyó el estudio de Annals de 2020 sobre el cociente aldosterona-renina como tamizaje del hiperaldosteronismo primario?", ["Era casi perfecto", "Tenía baja sensibilidad", "Era demasiado costoso", "Solo servía con potasio bajo"],
  "El cociente de tamizaje habitual dejó escapar muchos casos, con baja sensibilidad y bajo valor predictivo negativo, por lo que la enfermedad pasa inadvertida.", "Baja sensibilidad.")),

# --- Hench and cortisone in rheumatoid arthritis (12114256)
("12114256", "beginner", 2, "In 1948 the U.S. rheumatologist Phillip S. Hench administered cortisone for the first time to a patient with rheumatoid arthritis",
 ("In 1948, the rheumatologist Philip Hench gave cortisone for the first time to a patient with which disease?", ["Bronchial asthma", "Pulmonary tuberculosis", "Rheumatoid arthritis", "Type 1 diabetes"],
  "Hench's 1948 treatment of a rheumatoid arthritis patient revealed the therapeutic power of glucocorticoids.", "Rheumatoid arthritis."),
 ("En 1948, el reumatólogo Philip Hench administró cortisona por primera vez a un paciente con ¿qué enfermedad?", ["Asma bronquial", "Tuberculosis pulmonar", "Artritis reumatoide", "Diabetes tipo 1"],
  "El tratamiento de Hench a un paciente con artritis reumatoide en 1948 reveló el poder terapéutico de los glucocorticoides.", "Artritis reumatoide.")),
("12114256", "curious", 3, "they received, along with Reichstein and Kendall, the Nobel Prize in Medicine or Physiology in 1950",
 ("What recognition did Hench's cortisone work receive in 1950?", ["A worldwide ban on steroid use", "The Lasker Award only", "A US patent on cortisol", "The Nobel Prize in Medicine"],
  "Hench shared the 1950 Nobel Prize in Physiology or Medicine with Kendall and Reichstein for work on adrenal cortex hormones.", "Nobel Prize."),
 ("¿Qué reconocimiento recibió en 1950 el trabajo de Hench con la cortisona?", ["Una prohibición de esteroides", "Solo el premio Lasker", "Una patente sobre el cortisol", "El Premio Nobel de Medicina"],
  "Hench compartió el Nobel de Fisiología o Medicina de 1950 con Kendall y Reichstein por sus trabajos sobre las hormonas de la corteza suprarrenal.", "El Premio Nobel.")),

# --- 21-hydroxylase autoantigen in Addison's disease (1351548)
("1351548", "researcher", 0, "21-hydroxylase (P450c21), prominent in the zona glomerulosa of the adrenal cortex, is a major autoantigen in idiopathic Addison's disease",
 ("Which steroidogenic enzyme was identified in 1992 as a major autoantigen in idiopathic (autoimmune) Addison's disease?", ["21-hydroxylase", "Aromatase", "5-alpha reductase", "Thyroid peroxidase"],
  "Patient sera recognized a 54 kDa adrenal protein that matched 21-hydroxylase (P450c21).", "21-hydroxylase."),
 ("¿Qué enzima esteroidogénica se identificó en 1992 como un autoantígeno principal en la enfermedad de Addison idiopática (autoinmune)?", ["21-hidroxilasa", "Aromatasa", "5-alfa reductasa", "Peroxidasa tiroidea"],
  "Los sueros de pacientes reconocían una proteína suprarrenal de 54 kDa que correspondía a la 21-hidroxilasa (P450c21).", "21-hidroxilasa.")),

# --- Adrenal insufficiency seminar (33484633)
("33484633", "beginner", 1, "patients with primary adrenal insufficiency usually develop skin hyperpigmentation and crave salt",
 ("According to a 2021 Lancet seminar, which two features typically distinguish primary adrenal insufficiency (Addison's disease)?", ["Weight gain and moon face", "Darker skin and salt craving", "High blood pressure and edema", "Excess sweating and tremor"],
  "Beyond fatigue, weight loss and low blood pressure, primary adrenal failure usually causes skin hyperpigmentation and salt craving.", "Dark skin, salt craving."),
 ("Según un seminario de The Lancet de 2021, ¿qué dos rasgos distinguen típicamente la insuficiencia suprarrenal primaria (enfermedad de Addison)?", ["Aumento de peso y cara de luna", "Piel oscura y antojo de sal", "Presión alta y edema", "Sudor excesivo y temblor"],
  "Además de cansancio, pérdida de peso y presión baja, la falla suprarrenal primaria suele causar hiperpigmentación de la piel y antojo de sal.", "Piel oscura y antojo de sal.")),

# --- HPA axis and stress (17290797)
("17290797", "explorer", 2, "Corticotropin-releasing factor (CRF) plays a central role in the stress response by regulating the hypothalamic-pituitary-adrenal (HPA) axis",
 ("In the hypothalamic-pituitary-adrenal (HPA) stress axis, which hypothalamic peptide starts the cascade that ends in glucocorticoid release?", ["Thyrotropin-releasing hormone", "Oxytocin", "Corticotropin-releasing factor", "Growth hormone-releasing hormone"],
  "CRF from the hypothalamus drives pituitary ACTH, which releases glucocorticoids that feed back to limit the response.", "CRF."),
 ("En el eje hipotálamo-hipófisis-suprarrenal (HHS) del estrés, ¿qué péptido hipotalámico inicia la cascada que termina en la liberación de glucocorticoides?", ["Hormona liberadora de tirotropina", "Oxitocina", "Factor liberador de corticotropina", "Hormona liberadora de hormona de crecimiento"],
  "El CRF del hipotálamo estimula la ACTH hipofisaria, que libera glucocorticoides que a su vez frenan la respuesta por retroalimentación.", "CRF.")),

# --- Hans Selye and the stress concept (9668601)
("9668601", "curious", 3, "adrenal hypertrophy, gastrointestinal ulcers, thymolymphatic atrophy",
 ("Which 'triad of stress' did Hans Selye first describe in stressed animals?", ["Fever, rash and joint pain", "Goiter, tremor and weight loss", "Anemia, jaundice and an enlarged spleen", "Big adrenals, ulcers, small thymus"],
  "Selye's triad was adrenal hypertrophy, gastrointestinal ulcers and thymolymphatic atrophy, linking stress to the adrenal cortex.", "Adrenals, ulcers, thymus."),
 ("¿Qué 'tríada del estrés' describió primero Hans Selye en animales estresados?", ["Fiebre alta, erupción y dolor de articulaciones", "Bocio, temblor y pérdida de peso", "Anemia, ictericia y esplenomegalia", "Suprarrenales grandes, úlceras, timo pequeño"],
  "La tríada de Selye fue hipertrofia suprarrenal, úlceras gastrointestinales y atrofia timolinfática, que vinculó el estrés con la corteza suprarrenal.", "Suprarrenales, úlceras, timo.")),

# --- Cloning the Ca2+-sensing receptor (8255296)
("8255296", "explorer", 0, "coupled to a seven-membrane-spanning domain like those in the G-protein-coupled receptor superfamily",
 ("The extracellular Ca2+-sensing receptor cloned from bovine parathyroid in 1993 belongs to which receptor family?", ["G-protein-coupled receptors", "Ligand-gated ion channel proteins", "Nuclear hormone receptors", "Receptor tyrosine kinases"],
  "The receptor has a large extracellular calcium-binding domain joined to a seven-transmembrane domain typical of G-protein-coupled receptors.", "GPCR."),
 ("El receptor sensor de Ca2+ extracelular clonado de paratiroides bovina en 1993 pertenece a ¿qué familia de receptores?", ["Receptores acoplados a proteína G", "Canales iónicos activados por ligando", "Receptores hormonales nucleares", "Receptores tirosina cinasa"],
  "El receptor tiene un gran dominio extracelular que une calcio unido a siete segmentos transmembrana, típico de los receptores acoplados a proteína G.", "Acoplado a proteína G.")),

# --- CaSR mutations in FHH (7916660)
("7916660", "researcher", 1, "mutations in the human Ca(2+)-sensing receptor gene cause familial hypocalciuric hypercalcemia (FHH) and neonatal severe hyperparathyroidism (NSHPT)",
 ("Which inherited disorders did Pollak and colleagues (1993) link to mutations in the human Ca2+-sensing receptor gene?", ["Vitamin D-resistant rickets", "FHH and neonatal severe HPT", "Pseudohypoparathyroidism", "X-linked hypophosphatemia"],
  "Loss-of-function CaSR mutations cause familial hypocalciuric hypercalcemia and neonatal severe hyperparathyroidism, showing the receptor 'sets' blood calcium.", "FHH and NSHPT."),
 ("¿Qué trastornos hereditarios vincularon Pollak y colaboradores (1993) con mutaciones del gen del receptor sensor de Ca2+ humano?", ["Raquitismo resistente a vitamina D", "HHF e hiperparatiroidismo neonatal", "Seudohipoparatiroidismo", "Hipofosfatemia ligada al X"],
  "Las mutaciones con pérdida de función del CaSR causan hipercalcemia hipocalciúrica familiar e hiperparatiroidismo neonatal grave: el receptor 'fija' el calcio sanguíneo.", "HHF e HPT neonatal grave.")),

# --- Calcium-PTH-vitamin D axis (29597231)
("29597231", "beginner", 2, "Hypocalcemia leads to the opposite sequence of events, namely, lowered intracellular calcium and increased PTH production and secretion",
 ("When blood calcium falls (hypocalcemia), how do the parathyroid glands respond?", ["They stop working", "They release calcitonin", "They secrete more PTH", "They secrete less PTH"],
  "Low calcium deactivates the calcium-sensing receptor, so parathyroid cells make and secrete more parathyroid hormone.", "More PTH."),
 ("Cuando baja el calcio en sangre (hipocalcemia), ¿cómo responden las glándulas paratiroides?", ["Dejan de funcionar", "Liberan calcitonina", "Secretan más PTH", "Secretan menos PTH"],
  "El calcio bajo desactiva el receptor sensor de calcio, y las células paratiroideas producen y secretan más hormona paratiroidea.", "Más PTH.")),
("29597231", "explorer", 3, "PTH stimulates the renal conversion of 25-hydroxyvitamin D (25[OH]D) to 1,25(OH)2D",
 ("In the calcium-PTH-vitamin D axis, which step does PTH stimulate in the kidney?", ["Breaking down calcitonin", "Making 25(OH)D from D3", "Excreting more calcium", "Activating vitamin D"],
  "PTH drives renal conversion of 25(OH)D to active 1,25(OH)2D, which raises intestinal calcium absorption.", "Vitamin D activation."),
 ("En el eje calcio-PTH-vitamina D, ¿qué paso estimula la PTH en el riñón?", ["Degradar la calcitonina", "Formar 25(OH)D a partir de D3", "Excretar más calcio", "Activar la vitamina D"],
  "La PTH impulsa la conversión renal de 25(OH)D en 1,25(OH)2D activa, que aumenta la absorción intestinal de calcio.", "Activación de la vitamina D.")),

# --- FGF23 in ADHR (11062477)
("11062477", "researcher", 0, "We identified missense mutations in a gene encoding a new member of the fibroblast growth factor (FGF) family, FGF23",
 ("The ADHR Consortium (2000) traced autosomal dominant hypophosphataemic rickets to mutations in which gene?", ["FGF23", "PHEX", "SLC34A1", "VDR"],
  "Missense mutations in FGF23, a new fibroblast growth factor, cause ADHR; PHEX is the gene of the X-linked form.", "FGF23."),
 ("El Consorcio ADHR (2000) atribuyó el raquitismo hipofosfatémico autosómico dominante a mutaciones en ¿qué gen?", ["FGF23", "PHEX", "SLC34A1", "VDR"],
  "Mutaciones de sentido erróneo en FGF23, un nuevo factor de crecimiento fibroblástico, causan ADHR; PHEX es el gen de la forma ligada al X.", "FGF23.")),

# --- OPG ligand / RANKL activates osteoclasts (9568710)
("9568710", "explorer", 1, "short-term administration into normal adult mice results in osteoclast activation associated with systemic hypercalcemia",
 ("In Lacey and colleagues' 1998 study, what happened when osteoprotegerin ligand (OPGL, now RANKL) was given to normal adult mice?", ["Bone formation tripled", "Hypercalcemia from osteoclasts", "Osteoclasts disappeared", "Blood calcium dropped sharply in days"],
  "OPGL activated osteoclasts and caused systemic hypercalcemia, and its effects were blocked by osteoprotegerin.", "Osteoclast activation."),
 ("En el estudio de Lacey y colaboradores (1998), ¿qué pasó al dar ligando de osteoprotegerina (OPGL, hoy RANKL) a ratones adultos normales?", ["La formación ósea se triplicó", "Hipercalcemia por osteoclastos", "Desaparecieron los osteoclastos", "El calcio en sangre cayó mucho"],
  "El OPGL activó los osteoclastos y causó hipercalcemia sistémica; sus efectos se bloquearon con osteoprotegerina.", "Activación de osteoclastos.")),

# --- OPGL-deficient mice (9950424)
("9950424", "researcher", 2, "opgl-deficient mice lack all lymph nodes but have normal splenic structure and Peyer's patches",
 ("Besides severe osteopetrosis, what striking defect did Kong and colleagues (1999) find in opgl (RANKL)-deficient mice?", ["No spleen", "No thymus", "No lymph nodes", "No Peyer's patches"],
  "Mice without OPGL lacked osteoclasts and all lymph nodes, while the spleen and Peyer's patches were normal.", "No lymph nodes."),
 ("Además de osteopetrosis grave, ¿qué defecto llamativo hallaron Kong y colaboradores (1999) en ratones sin opgl (RANKL)?", ["Sin bazo", "Sin timo", "Sin ganglios", "Sin placas de Peyer"],
  "Los ratones sin OPGL carecían de osteoclastos y de todos los ganglios linfáticos, con bazo y placas de Peyer normales.", "Sin ganglios linfáticos.")),

# --- FREEDOM trial of denosumab (19671655)
("19671655", "explorer", 3, "denosumab reduced the risk of new radiographic vertebral fracture, with a cumulative incidence of 2.3% in the denosumab group, versus 7.2% in the placebo group",
 ("In the FREEDOM trial in 7868 women with osteoporosis, by how much did denosumab, an anti-RANKL antibody, reduce new vertebral fractures over 36 months?", ["About 5%", "No reduction", "About 20%", "About 68%"],
  "Vertebral fractures fell from 7.2% to 2.3%, a 68% relative decrease; hip and nonvertebral fractures also fell.", "About 68%."),
 ("En el ensayo FREEDOM con 7868 mujeres con osteoporosis, ¿cuánto redujo el denosumab, un anticuerpo anti-RANKL, las nuevas fracturas vertebrales en 36 meses?", ["Cerca del 5%", "Ninguna reducción", "Cerca del 20%", "Cerca del 68%"],
  "Las fracturas vertebrales bajaron de 7,2% a 2,3%, una reducción relativa del 68%; también bajaron las de cadera y no vertebrales.", "Cerca del 68%.")),

# --- Bile acids activate FXR (10334992)
("10334992", "researcher", 0, "bile acids are physiological ligands for the farnesoid X receptor (FXR), an orphan nuclear receptor",
 ("Makishima and colleagues (1999) showed that bile acids are physiological ligands for which receptor?", ["Farnesoid X receptor", "Vitamin D receptor", "Glucocorticoid receptor", "Insulin receptor"],
  "Bile acids bind FXR, which represses cholesterol 7alpha-hydroxylase and so feeds back on bile acid synthesis.", "FXR."),
 ("Makishima y colaboradores (1999) mostraron que los ácidos biliares son ligandos fisiológicos de ¿qué receptor?", ["Receptor X farnesoide", "Receptor de vitamina D", "Receptor de glucocorticoides", "Receptor de insulina"],
  "Los ácidos biliares se unen a FXR, que reprime la colesterol 7-alfa-hidroxilasa y así frena su propia síntesis.", "FXR.")),

# --- Omeprazole in man (6428981)
("6428981", "explorer", 1, "After seven days treatment with 30 or 60 mg daily, there was almost 100% inhibition of both basal and pentagastrin stimulated acid output",
 ("In a 1984 study in 12 healthy subjects, what happened to gastric acid output after seven days of daily omeprazole?", ["Rose above baseline", "Almost 100% inhibited", "Fell by about 20%", "Unchanged after a week"],
  "Repeated 30 or 60 mg doses nearly abolished basal and stimulated acid output, consistent with blocking the parietal cell H+/K+-ATPase.", "Almost fully blocked."),
 ("En un estudio de 1984 en 12 sujetos sanos, ¿qué pasó con la secreción de ácido gástrico tras siete días de omeprazol diario?", ["Subió sobre lo basal", "Inhibición de casi 100%", "Bajó cerca de un 20%", "Sin cambios tras una semana"],
  "Dosis repetidas de 30 o 60 mg casi anularon la secreción basal y estimulada, en línea con el bloqueo de la H+/K+-ATPasa de la célula parietal.", "Casi totalmente bloqueada.")),

# --- Gastric H+,K+-ATPase (2166525)
("2166525", "beginner", 2, "The H+,K(+)-ATPase carries out the electroneutral exchange of H+ and K+ and thereby generates a pH of less than 1 in the secretory canaliculus",
 ("The gastric proton pump (H+,K+-ATPase) of the parietal cell exchanges which ions to acidify the stomach?", ["Na+ for Cl-", "Ca2+ for Na+", "H+ for K+", "HCO3- for Cl-"],
  "The pump swaps H+ for K+, producing a pH below 1 in the parietal cell's secretory canaliculus.", "H+ for K+."),
 ("La bomba de protones gástrica (H+,K+-ATPasa) de la célula parietal intercambia ¿qué iones para acidificar el estómago?", ["Na+ por Cl-", "Ca2+ por Na+", "H+ por K+", "HCO3- por Cl-"],
  "La bomba intercambia H+ por K+ y genera un pH menor de 1 en el canalículo secretor de la célula parietal.", "H+ por K+.")),

# --- Oxytocin-deficient mice (8933362)
("8933362", "beginner", 3, "These results indicate an absolute requirement for oxytocin for successful milk injection, but not for mating, parturition and milk production, in mice",
 ("Mice engineered to lack oxytocin (1996) could still mate and give birth. Which function failed?", ["Milk production", "Fertility", "Labor", "Milk ejection"],
  "Without oxytocin, mothers made milk but could not eject it; their pups died within 24 h with empty stomachs.", "Milk ejection."),
 ("Ratones modificados para carecer de oxitocina (1996) aún podían aparearse y parir. ¿Qué función falló?", ["La producción de leche", "La fertilidad", "El parto", "La eyección de leche"],
  "Sin oxitocina, las madres producían leche pero no podían expulsarla; las crías morían en 24 h con el estómago vacío.", "La eyección de leche.")),
("8933362", "curious", 0, "OT injection into the dams restores the milk injection in response to suckling",
 ("In oxytocin-deficient mouse mothers whose pups could not get milk, what restored milk ejection during suckling?", ["Oxytocin injections", "Prolactin injections", "Hand-feeding the dams", "Removing the pups daily"],
  "Injecting oxytocin into the mothers restored the milk ejection reflex in response to suckling.", "Oxytocin injections."),
 ("En madres de ratón sin oxitocina cuyas crías no obtenían leche, ¿qué restauró la eyección de leche durante la succión?", ["Inyectar oxitocina", "Inyectar prolactina", "Alimentar a mano a las madres", "Retirar las crías a diario"],
  "Inyectar oxitocina a las madres restauró el reflejo de eyección de leche en respuesta a la succión.", "Inyectar oxitocina.")),

# --- Kidney physiology in pregnancy (33328060)
("33328060", "explorer", 1, "The primary acid/base change seen in pregnancy is a mild respiratory alkalosis due to progesterone effects",
 ("According to a 2020 review of kidney physiology in pregnancy, what is the main acid-base change of normal pregnancy?", ["Metabolic acidosis", "Respiratory alkalosis", "Respiratory acidosis", "Metabolic alkalosis"],
  "Progesterone stimulates breathing, producing a mild respiratory alkalosis; GFR also rises dramatically in pregnancy.", "Respiratory alkalosis."),
 ("Según una revisión de 2020 sobre fisiología renal en el embarazo, ¿cuál es el principal cambio ácido-base del embarazo normal?", ["Acidosis metabólica", "Alcalosis respiratoria", "Acidosis respiratoria", "Alcalosis metabólica"],
  "La progesterona estimula la respiración y produce una alcalosis respiratoria leve; además, la filtración glomerular aumenta mucho.", "Alcalosis respiratoria.")),

# --- Cardiac output in normal pregnancy (8141215)
("8141215", "researcher", 2, "Cardiac output by pulsed Doppler increased from 6.7 +/- 0.6 L/min at 8 to 11 weeks' gestation to 8.7 +/- 1.4 L/min at 36 to 39 weeks' gestation",
 ("In a 1994 longitudinal echocardiographic study of 18 pregnant women, how did cardiac output change toward term?", ["Fell steadily after week 20", "Stayed constant throughout", "Rose from 6.7 to 8.7 L/min", "Peaked in week 12, then fell"],
  "Cardiac output kept rising into late pregnancy, from 6.7 to 8.7 L/min, then fell to 5.7 L/min by 12 weeks postpartum.", "Rose to 8.7 L/min."),
 ("En un estudio ecocardiográfico longitudinal de 1994 en 18 embarazadas, ¿cómo cambió el gasto cardíaco hacia el término?", ["Bajó desde la semana 20", "Se mantuvo constante", "Subió de 6,7 a 8,7 L/min", "Tocó techo en la semana 12"],
  "El gasto cardíaco siguió subiendo hasta el final del embarazo, de 6,7 a 8,7 L/min, y bajó a 5,7 L/min a las 12 semanas posparto.", "Subió a 8,7 L/min.")),

# --- SGLT2 and renal glucose reabsorption (27878313)
("27878313", "beginner", 3, "Most of the capacity for renal glucose reabsorption is provided by sodium glucose cotransporter (SGLT) 2 in the early proximal tubule",
 ("Which transporter provides most of the kidney's capacity to reabsorb filtered glucose?", ["GLUT4 in the collecting duct", "Aquaporin-2 in the loop of Henle", "ENaC in the distal tubule", "SGLT2 in the proximal tubule"],
  "SGLT2 in the early proximal tubule reabsorbs most of the ~160 g of glucose filtered each day, which is why SGLT2 inhibitors cause glucosuria.", "SGLT2."),
 ("¿Qué transportador aporta la mayor parte de la capacidad del riñón para reabsorber la glucosa filtrada?", ["GLUT4 en el túbulo colector", "Acuaporina-2 en el asa de Henle", "ENaC en el túbulo distal", "SGLT2 en el túbulo proximal"],
  "El SGLT2 del túbulo proximal inicial reabsorbe la mayor parte de los ~160 g de glucosa filtrados al día; por eso sus inhibidores causan glucosuria.", "SGLT2.")),
("27878313", "researcher", 0, "In the absence or with inhibition of SGLT2, the renal reabsorptive capacity for glucose declines to ∼80 g/day (the residual capacity of SGLT1)",
 ("According to a 2017 Diabetologia review, what happens to the kidney's glucose reabsorptive capacity when SGLT2 is inhibited?", ["Falls to ~80 g/day via SGLT1", "Rises to ~900 g/day", "Falls to zero", "Stays unchanged at about 450 g/day"],
  "Capacity drops from ~450 to ~80 g/day, the residual SGLT1 capacity, which explains the low hypoglycaemia risk of SGLT2 inhibitors.", "~80 g/day."),
 ("Según una revisión de Diabetologia de 2017, ¿qué pasa con la capacidad renal de reabsorber glucosa cuando se inhibe el SGLT2?", ["Baja a ~80 g/día por SGLT1", "Sube a ~900 g/día", "Cae a cero", "Se mantiene igual en ~450 g/día"],
  "La capacidad cae de ~450 a ~80 g/día, la capacidad residual del SGLT1, lo que explica el bajo riesgo de hipoglucemia de estos fármacos.", "~80 g/día.")),

# --- Renal autoregulation (25834230)
("25834230", "explorer", 1, "Intrarenal autoregulatory mechanisms maintain renal blood flow (RBF) and glomerular filtration rate (GFR) independent of renal perfusion pressure (RPP) over a defined range (80-180 mmHg)",
 ("Over roughly what range of renal perfusion pressure does autoregulation keep renal blood flow and GFR stable?", ["20-60 mmHg", "80-180 mmHg", "200-300 mmHg", "0-40 mmHg"],
  "Myogenic and tubuloglomerular feedback responses of the afferent arteriole hold RBF and GFR steady between about 80 and 180 mmHg.", "80-180 mmHg."),
 ("¿En qué rango aproximado de presión de perfusión renal la autorregulación mantiene estables el flujo sanguíneo renal y la TFG?", ["20-60 mmHg", "80-180 mmHg", "200-300 mmHg", "0-40 mmHg"],
  "Las respuestas miogénica y de retroalimentación tubuloglomerular de la arteriola aferente mantienen el flujo y la TFG entre unos 80 y 180 mmHg.", "80-180 mmHg.")),

# --- Countercurrent system (2232506)
("2232506", "researcher", 2, "The single effect in the outer medulla is active NaCl absorption from the thick ascending limb",
 ("In the countercurrent multiplier that concentrates urine, what is the 'single effect' in the outer medulla?", ["Water secretion by the collecting duct", "Passive urea secretion in the proximal tubule", "Active NaCl uptake, thick ascending limb", "Glucose reabsorption in the thin limb"],
  "Active NaCl absorption by the water-impermeable thick ascending limb builds the medullary gradient that the multiplier amplifies.", "Thick limb NaCl uptake."),
 ("En el multiplicador por contracorriente que concentra la orina, ¿cuál es el 'efecto único' en la médula externa?", ["Secreción de agua en el túbulo colector", "Secreción de urea en el túbulo proximal", "Absorción activa de NaCl en la rama gruesa", "Reabsorción de glucosa en la rama delgada"],
  "La absorción activa de NaCl en la rama ascendente gruesa, impermeable al agua, crea el gradiente medular que el multiplicador amplifica.", "NaCl en la rama gruesa.")),

# --- Regulation of potassium homeostasis (24721891)
("24721891", "beginner", 3, "Potassium is the most abundant cation in the intracellular fluid",
 ("Which is the most abundant cation inside the body's cells?", ["Sodium", "Calcium", "Magnesium", "Potassium"],
  "Potassium dominates the intracellular fluid, and the kidney keeps total body potassium in balance by adjusting its excretion.", "Potassium."),
 ("¿Cuál es el catión más abundante dentro de las células del cuerpo?", ["Sodio", "Calcio", "Magnesio", "Potasio"],
  "El potasio predomina en el líquido intracelular, y el riñón mantiene el balance total ajustando su excreción.", "Potasio.")),
]
