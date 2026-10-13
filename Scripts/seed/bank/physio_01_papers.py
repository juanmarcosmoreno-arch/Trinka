# Human physiology I — kidney (aquaporins, vasopressin, renal EPO), acid-base and blood gases, coagulation and
# fibrinolysis, insulin and GLP-1, thyroid, hepcidin and iron, erythropoietin and HIF-1,
# Frank-Starling, oxygen transport, surfactant, gut microbiome, VO2max, circadian clocks, brown fat.
# Sources: PubMed paper and review abstracts. Excerpts verbatim.
CATEGORY = "humanPhysiology"
Q = [
# --- Arterial blood gas fundamentals (36176645)
("36176645", "beginner", 0, "the lungs, which excrete volatile acid as carbon dioxide, and the kidneys, which contribute to maintenance of plasma bicarbonate",
 ("In acid-base physiology, which organ excretes volatile acid as carbon dioxide?", ["Lungs", "Kidneys", "Liver", "Skin"],
  "The lungs excrete volatile acid as CO2, while the kidneys help maintain plasma bicarbonate.", "The lungs."),
 ("En la fisiología ácido-base, ¿qué órgano elimina el ácido volátil como dióxido de carbono?", ["Pulmones", "Riñones", "Corazón", "Intestino"],
  "Los pulmones eliminan el ácido volátil como CO2, mientras los riñones ayudan a mantener el bicarbonato plasmático.", "Los pulmones.")),

# --- Hypothyroidism seminar (28336049)
("28336049", "beginner", 0, "The standard treatment is thyroid hormone replacement therapy with levothyroxine",
 ("What is the standard treatment for hypothyroidism, according to a 2017 Lancet Seminar?", ["Levothyroxine", "Hydrocortisone", "Insulin", "Vitamin B12"],
  "Hypothyroidism is treated by replacing thyroid hormone with levothyroxine (synthetic T4).", "Levothyroxine."),
 ("¿Cuál es el tratamiento estándar del hipotiroidismo, según un Seminario de The Lancet de 2017?", ["Levotiroxina", "Hidrocortisona", "Insulina", "Vitamina B12"],
  "El hipotiroidismo se trata reponiendo la hormona tiroidea con levotiroxina (T4 sintética).", "Levotiroxina.")),
("28336049", "beginner", 3, "The most common symptoms in adults are fatigue, lethargy, cold intolerance, weight gain",
 ("Which symptom is among the most common in adults with hypothyroidism (thyroid hormone deficiency)?", ["Intolerance to heat", "Fine tremor", "Weight loss", "Cold intolerance"],
  "Fatigue, lethargy, cold intolerance, weight gain, constipation and dry skin are typical; the others suggest an overactive thyroid.", "Cold intolerance."),
 ("¿Qué síntoma está entre los más comunes en adultos con hipotiroidismo (déficit de hormona tiroidea)?", ["Intolerancia al calor", "Temblor fino", "Pérdida de peso", "Intolerancia al frío"],
  "Son típicos el cansancio, el letargo, la intolerancia al frío, el aumento de peso, el estreñimiento y la piel seca; los otros sugieren tiroides hiperactiva.", "Intolerancia al frío.")),

# --- Physiology of oxygen transport (10175156)
("10175156", "beginner", 2, "O2 transport in blood is achieved (1) through binding to haemoglobin and (2) through physical dissolution in plasma",
 ("Besides binding to hemoglobin, how else is oxygen carried in the blood?", ["Bound to albumin", "As bicarbonate ions", "Dissolved in plasma", "Stored inside platelets"],
  "Oxygen travels bound to hemoglobin and, in a small amount, physically dissolved in plasma; together they make up blood O2 content.", "Dissolved in plasma."),
 ("Además de unirse a la hemoglobina, ¿de qué otra forma se transporta el oxígeno en la sangre?", ["Unido a la albúmina", "Como bicarbonato", "Disuelto en el plasma", "Dentro de las plaquetas"],
  "El oxígeno viaja unido a la hemoglobina y, en poca cantidad, disuelto en el plasma; ambos forman el contenido de O2 de la sangre.", "Disuelto en el plasma.")),
("10175156", "researcher", 0, "When intravascular volume is preserved (e.g. normovolemic dilutional anaemia), reductions in O2 content are tolerated to a much higher degree than in hypovolemic anaemia",
 ("Which type of anemia tolerates a much larger fall in blood oxygen content before tissue hypoxia occurs?", ["Normovolemic dilutional", "Anemia in hemorrhagic shock", "Hypovolemic anemia", "Acute massive blood loss"],
  "When blood volume is preserved, the heart can compensate, so low O2 content is tolerated far better than in hypovolemic anemia.", "Normovolemic."),
 ("¿Qué tipo de anemia tolera una caída mucho mayor del contenido de oxígeno antes de que haya hipoxia tisular?", ["Dilucional normovolémica", "Shock hemorrágico", "Anemia hipovolémica", "Pérdida aguda de sangre"],
  "Si se conserva el volumen sanguíneo, el corazón compensa, y el bajo contenido de O2 se tolera mucho mejor que en la anemia hipovolémica.", "Normovolémica.")),

# --- Frank-Starling mechanism (24788476)
("24788476", "beginner", 1, "The heart has an intrinsic ability to increase systolic force in response to a rise in ventricular filling",
 ("According to the Frank-Starling law of the heart, what happens when ventricular filling rises?", ["Force falls", "Force rises", "The heart stops", "Nothing changes"],
  "A fuller, more stretched ventricle contracts with greater systolic force, matching output to venous return.", "Force rises."),
 ("Según la ley de Frank-Starling del corazón, ¿qué ocurre cuando aumenta el llenado ventricular?", ["La fuerza baja", "La fuerza sube", "El corazón se detiene", "No cambia nada"],
  "Un ventrículo más lleno y estirado se contrae con mayor fuerza sistólica, igualando el gasto al retorno venoso.", "La fuerza sube.")),

# --- Erythropoietin physiology (24273483)
("24273483", "beginner", 2, "The kidneys are the primary sources of Epo",
 ("Which organ is the main source of the hormone erythropoietin (EPO)?", ["The liver", "The spleen", "The kidneys", "The bone marrow"],
  "EPO is made mainly in the kidneys under control of hypoxia-inducible factors and drives red-cell production.", "The kidneys."),
 ("¿Qué órgano es la principal fuente de la hormona eritropoyetina (EPO)?", ["El hígado", "El bazo", "Los riñones", "La médula ósea"],
  "La EPO se produce sobre todo en los riñones, bajo control de los factores inducibles por hipoxia, y estimula la producción de glóbulos rojos.", "Los riñones.")),
("24273483", "curious", 3, "Epo deficiency is the primary cause of the anemia in chronic kidney disease",
 ("What is the primary cause of anemia in chronic kidney disease?", ["Iron overload", "Excess vitamin C", "Blood in urine", "EPO deficiency"],
  "Damaged kidneys make too little erythropoietin; recombinant EPO (epoetin) can treat it.", "Low EPO."),
 ("¿Cuál es la causa principal de la anemia en la enfermedad renal crónica?", ["Exceso de hierro", "Exceso de vitamina C", "Sangre en la orina", "Déficit de EPO"],
  "Los riñones dañados producen poca eritropoyetina; la EPO recombinante (epoetina) puede tratarla.", "Poca EPO.")),

# --- Renal EPO-producing cells (29655605)
("29655605", "expert", 1, "The renal EPO is mainly produced by pericytes",
 ("According to a 2018 review, which kidney cells mainly produce erythropoietin and lose this ability in CKD?", ["Podocytes", "Pericytes", "Proximal tubule cells", "Mesangial cells"],
  "Renal EPO comes mainly from pericytes, which turn into myofibroblasts in CKD and stop making EPO.", "Pericytes."),
 ("Según una revisión de 2018, ¿qué células renales producen principalmente eritropoyetina y pierden esa capacidad en la ERC?", ["Podocitos", "Pericitos", "Células del túbulo proximal", "Células mesangiales"],
  "La EPO renal proviene sobre todo de pericitos, que en la ERC se transforman en miofibroblastos y dejan de producirla.", "Pericitos.")),

# --- Overview of coagulation (25535411)
("25535411", "beginner", 0, "leading to a tendency of either thrombosis or bleeding",
 ("An imbalance of the coagulation system can push a patient toward which problems?", ["Thrombosis or bleeding", "Fever or night sweats", "Allergy or skin rashes", "Cough or wheezing spells"],
  "Normal hemostasis balances clot formation against its inhibition; tilting either way causes thrombosis or bleeding.", "Clots or bleeding."),
 ("Un desequilibrio del sistema de coagulación puede llevar a un paciente hacia ¿qué problemas?", ["Trombosis o sangrado", "Fiebre o sudores nocturnos", "Alergia o erupciones", "Tos o silbidos al respirar"],
  "La hemostasia normal equilibra la formación del coágulo y su inhibición; si se inclina hacia un lado, hay trombosis o sangrado.", "Coágulos o sangrado.")),

# --- Thermal physiology concepts (40452320)
("40452320", "beginner", 1, "the dominant mechanism through which body temperature is regulated, under a thermal challenge, environmental or metabolic, is negative feedback control",
 ("What is the dominant mechanism by which the human body regulates its temperature?", ["Positive feedback", "Negative feedback", "Random variation", "Conscious choice"],
  "Negative feedback corrects deviations of body temperature, helped by anticipatory feedforward control.", "Negative feedback."),
 ("¿Cuál es el mecanismo dominante con el que el cuerpo humano regula su temperatura?", ["Retroalimentación positiva", "Retroalimentación negativa", "Variación al azar", "Decisión consciente"],
  "La retroalimentación negativa corrige los desvíos de temperatura, ayudada por un control anticipatorio (feedforward).", "Retroalimentación negativa.")),

# --- Gut microbiota and fat storage (15505215)
("15505215", "explorer", 2, "produces a 60% increase in body fat content and insulin resistance within 14 days despite reduced food intake",
 ("What happened within 14 days when adult germ-free mice received a normal gut microbiota (Bäckhed et al., 2004)?", ["Body fat fell by 60%", "No change in body fat", "Body fat rose by 60%", "They ate twice as much"],
  "Body fat rose 60% and insulin resistance appeared even though the mice ate less.", "Fat rose 60%."),
 ("¿Qué ocurrió en 14 días cuando ratones adultos libres de gérmenes recibieron una microbiota intestinal normal (Bäckhed et al., 2004)?", ["La grasa bajó un 60%", "La grasa no cambió", "La grasa subió un 60%", "Comieron el doble"],
  "La grasa corporal subió un 60% y apareció resistencia a la insulina aunque los ratones comían menos.", "Subió un 60%.")),

# --- Biology of VO2max (27888580)
("27888580", "explorer", 3, "training-induced increases in VO2 max are largely facilitated by expansion of red blood cell volume and an associated improvement in stroke volume",
 ("According to a 2017 review on the biology of VO2max, what largely drives training-induced gains in VO2max?", ["More muscle fibers", "Bigger lung capacity", "Lower resting heart rate", "More red-cell volume"],
  "Training expands red-cell volume and improves stroke volume, which largely explain the rise in VO2max.", "Red-cell volume."),
 ("Según una revisión de 2017 sobre la biología del VO2máx, ¿qué impulsa en gran parte su aumento con el entrenamiento?", ["Más fibras musculares", "Pulmones más grandes", "Menor frecuencia cardíaca", "Más masa de glóbulos rojos"],
  "El entrenamiento expande el volumen de glóbulos rojos y mejora el volumen sistólico, lo que explica gran parte del aumento del VO2máx.", "Glóbulos rojos.")),

# --- Traditional vs modern acid-base (11939993)
("11939993", "researcher", 3, "The 'modern' approach derives from Stewart's work in physical chemistry",
 ("The 'traditional' acid-base approach comes from Henderson and Hasselbalch. Where does the 'modern' approach come from?", ["Bohr's work on hemoglobin", "Starling's work on capillaries", "Krebs's work on the citric cycle", "Stewart's physical chemistry"],
  "The modern approach derives from Peter Stewart's physical chemistry and has been applied mainly in intensive care.", "Stewart's work."),
 ("El enfoque ácido-base 'tradicional' viene de Henderson y Hasselbalch. ¿De dónde proviene el enfoque 'moderno'?", ["Trabajos de Bohr en hemoglobina", "Trabajos de Starling en capilares", "Ciclo de Krebs del ácido cítrico", "La fisicoquímica de Stewart"],
  "El enfoque moderno deriva de la fisicoquímica de Peter Stewart y se ha aplicado sobre todo en cuidados intensivos.", "Trabajo de Stewart.")),

# --- Discovery of insulin (33393501)
("33393501", "beginner", 0, "ground-breaking research in Toronto that changed the course of what was, then, a universally fatal disease",
 ("In which city did Banting, Best, Macleod and Collip discover insulin in 1921–1922?", ["Toronto", "Montreal", "Edinburgh", "Stockholm"],
  "The Toronto work turned type 1 diabetes from a universally fatal disease into a treatable one.", "Toronto."),
 ("¿En qué ciudad descubrieron Banting, Best, Macleod y Collip la insulina en 1921–1922?", ["Toronto", "Montreal", "Edimburgo", "Estocolmo"],
  "El trabajo de Toronto convirtió a la diabetes tipo 1, entonces siempre mortal, en una enfermedad tratable.", "Toronto.")),
("33393501", "curious", 1, "a universally fatal disease: type 1 diabetes",
 ("Which disease was universally fatal before the discovery of insulin?", ["Tuberculosis", "Type 1 diabetes", "Pernicious anemia", "Addison disease"],
  "Before 1921, type 1 diabetes was universally fatal; insulin was one of the first lifesaving therapies of modern science.", "Type 1 diabetes."),
 ("¿Qué enfermedad era siempre mortal antes del descubrimiento de la insulina?", ["La tuberculosis", "La diabetes tipo 1", "La anemia perniciosa", "La enfermedad de Addison"],
  "Antes de 1921, la diabetes tipo 1 era siempre mortal; la insulina fue una de las primeras terapias salvadoras de la ciencia moderna.", "Diabetes tipo 1.")),

# --- GLP-1 as an incretin (2890903)
("2890903", "explorer", 2, "These observations suggest that GLP-1 7-36 is a physiological incretin and that it is more powerful than GIP",
 ("In the 1987 Lancet study of gut hormones in humans, how did GLP-1 7-36 compare with GIP?", ["GIP was far stronger", "Both were inactive", "GLP-1 was more potent", "GLP-1 lowered insulin levels"],
  "Infused at physiological levels, GLP-1 7-36 stimulated insulin release more than GIP, marking it as a powerful incretin.", "GLP-1 stronger."),
 ("En el estudio de 1987 en The Lancet sobre hormonas intestinales en humanos, ¿cómo se comparó el GLP-1 7-36 con el GIP?", ["El GIP fue mucho más fuerte", "Ambos fueron inactivos", "El GLP-1 fue más potente", "El GLP-1 bajó la insulina"],
  "Infundido a niveles fisiológicos, el GLP-1 7-36 estimuló más la secreción de insulina que el GIP, lo que lo señala como una incretina potente.", "El GLP-1, más fuerte.")),
("2890903", "expert", 3, "greatly increased postprandial plasma GLP-1 7-36 levels in patients with postgastrectomy dumping syndrome",
 ("In the 1987 GLP-1 incretin study, which patients had greatly increased postprandial GLP-1 7-36 levels?", ["Type 1 diabetes", "Insulinoma", "Cushing syndrome", "Dumping syndrome"],
  "High GLP-1 after gastrectomy may explain the hyperinsulinemia and reactive hypoglycemia of dumping syndrome.", "Dumping syndrome."),
 ("En el estudio de 1987 sobre el GLP-1 como incretina, ¿qué pacientes tenían niveles posprandiales de GLP-1 7-36 muy elevados?", ["Diabetes tipo 1", "Insulinoma", "Síndrome de Cushing", "Síndrome de dumping"],
  "El GLP-1 alto tras la gastrectomía podría explicar la hiperinsulinemia y la hipoglucemia reactiva del síndrome de dumping.", "Síndrome de dumping.")),

# --- Hepcidin binds ferroportin (15514116)
("15514116", "explorer", 0, "After binding, ferroportin was internalized and degraded, leading to decreased export of cellular iron",
 ("What did Nemeth and colleagues (2004) show that hepcidin does to the iron exporter ferroportin?", ["Causes its degradation", "Increases its activity", "Boosts its synthesis", "Moves it to the nucleus"],
  "Hepcidin binds ferroportin, which is internalized and degraded, so cells export less iron.", "Degrades it."),
 ("¿Qué demostraron Nemeth y colegas (2004) que hace la hepcidina con el exportador de hierro ferroportina?", ["Causa su degradación", "Aumenta su actividad", "Estimula su síntesis", "La lleva al núcleo"],
  "La hepcidina se une a la ferroportina, que se internaliza y se degrada, y así las células exportan menos hierro.", "La degrada.")),
("15514116", "researcher", 1, "hepcidin overproduction leads to hypoferremia and the anemia of inflammation",
 ("What is the consequence of hepcidin overproduction, as described by Nemeth and colleagues?", ["Iron overload", "Low plasma iron", "Polycythemia", "Hereditary hemochromatosis"],
  "Too much hepcidin causes hypoferremia and the anemia of inflammation; too little causes tissue iron overload.", "Hypoferremia."),
 ("¿Cuál es la consecuencia de un exceso de hepcidina, según Nemeth y colegas?", ["Sobrecarga de hierro", "Hierro plasmático bajo", "Policitemia", "Hemocromatosis"],
  "Demasiada hepcidina causa hipoferremia y anemia de la inflamación; muy poca causa sobrecarga tisular de hierro.", "Hipoferremia.")),

# --- Hepcidin-deficient USF2 knockout mice (11447267)
("11447267", "researcher", 2, "a complete defect in hepcidin expression is responsible for progressive tissue iron overload",
 ("What did Usf2 knockout mice lacking hepcidin expression develop (Nicolas et al., 2001)?", ["Severe iron deficiency", "Copper accumulation", "Tissue iron overload", "Normal iron balance"],
  "Without hepcidin, the mice progressively loaded iron in organs such as the pancreas and heart, like hemochromatosis.", "Iron overload."),
 ("¿Qué desarrollaron los ratones knockout para Usf2 sin expresión de hepcidina (Nicolas et al., 2001)?", ["Déficit grave de hierro", "Acumulación de cobre", "Sobrecarga de hierro", "Balance normal de hierro"],
  "Sin hepcidina, los ratones acumularon hierro progresivamente en órganos como el páncreas y el corazón, como en la hemocromatosis.", "Sobrecarga de hierro.")),
("11447267", "expert", 3, "the splenic iron content is strikingly lower in knockout animals than in controls",
 ("In hepcidin-deficient Usf2 knockout mice, which organ had strikingly LOWER iron than in controls?", ["Liver", "Pancreas", "Heart", "Spleen"],
  "While iron built up in many organs, splenic iron was strikingly lower, consistent with macrophages releasing iron freely.", "Spleen."),
 ("En los ratones knockout para Usf2 sin hepcidina, ¿qué órgano tenía MENOS hierro que los controles?", ["El hígado", "El páncreas", "El corazón", "El bazo"],
  "Mientras el hierro se acumulaba en muchos órganos, el del bazo era mucho menor, lo que concuerda con macrófagos que liberan hierro sin freno.", "Bazo.")),

# --- IL-6 induces hepcidin (15124018)
("15124018", "researcher", 0, "IL-6 is the necessary and sufficient cytokine for the induction of hepcidin during inflammation",
 ("Which cytokine was found necessary and sufficient to induce hepcidin during inflammation?", ["IL-6", "TNF-alpha", "IL-10", "Interferon gamma"],
  "Studies in liver cells, mice and human volunteers showed the IL-6–hepcidin axis drives the hypoferremia of inflammation.", "IL-6."),
 ("¿Qué citocina resultó necesaria y suficiente para inducir la hepcidina durante la inflamación?", ["IL-6", "TNF-alfa", "IL-10", "Interferón gamma"],
  "Estudios en células hepáticas, ratones y voluntarios mostraron que el eje IL-6–hepcidina causa la hipoferremia de la inflamación.", "IL-6.")),

# --- Erythropoietin gene cloning (3865178)
("3865178", "researcher", 1, "It encodes a 27-amino acid signal peptide and a 166-amino acid mature protein",
 ("When the human erythropoietin gene was cloned in 1985, how long was the mature protein it encoded?", ["51 amino acids", "166 amino acids", "574 amino acids", "1,024 amino acids"],
  "The gene encodes a 27-residue signal peptide and a 166-amino-acid mature hormone of about 18.4 kDa.", "166 amino acids."),
 ("Cuando se clonó el gen de la eritropoyetina humana en 1985, ¿qué longitud tenía la proteína madura codificada?", ["51 aminoácidos", "166 aminoácidos", "574 aminoácidos", "1024 aminoácidos"],
  "El gen codifica un péptido señal de 27 residuos y una hormona madura de 166 aminoácidos, de unos 18,4 kDa.", "166 aminoácidos.")),
("3865178", "explorer", 2, "when introduced into Chinese hamster ovary cells, produces erythropoietin that is biologically active",
 ("In the 1985 study cloning the human erythropoietin gene, which cells made biologically active hormone from it?", ["E. coli bacteria", "Baker's yeast cells", "Hamster ovary cells", "Cultured insect larva cells"],
  "Chinese hamster ovary cells carrying the gene produced erythropoietin active in vitro and in vivo, paving the way for therapy.", "CHO cells."),
 ("En el estudio de 1985 que clonó el gen de la eritropoyetina humana, ¿qué células produjeron la hormona activa?", ["Bacterias Escherichia coli", "Levaduras de panadería", "Células de ovario de hámster", "Células de larva de insecto"],
  "Las células de ovario de hámster chino con el gen produjeron eritropoyetina activa in vitro e in vivo, lo que abrió paso a su uso terapéutico.", "Células CHO.")),

# --- Recombinant EPO in end-stage renal disease (3537801)
("3537801", "explorer", 3, "Of 18 patients receiving effective doses of recombinant human erythropoietin, 12 who had required transfusions no longer needed them",
 ("In the 1987 phase I–II trial of recombinant erythropoietin in hemodialysis patients, how many of 18 on effective doses stopped needing transfusions?", ["No patients", "2 patients", "All 18 patients", "12 patients"],
  "Twelve previously transfusion-dependent patients no longer needed transfusions, and 11 reached a hematocrit of 35% or more.", "12."),
 ("En el ensayo fase I–II de 1987 con eritropoyetina recombinante en hemodiálisis, ¿cuántos de 18 pacientes con dosis eficaces dejaron de necesitar transfusiones?", ["Ningún paciente", "2 pacientes", "Los 18 pacientes", "12 pacientes"],
  "Doce pacientes que dependían de transfusiones dejaron de necesitarlas y 11 alcanzaron un hematocrito de 35% o más.", "12.")),

# --- HIF-1 structure (7539918)
("7539918", "researcher", 1, "necessary for transcriptional activation mediated by the erythropoietin gene enhancer in hypoxic cells",
 ("Hypoxia-inducible factor 1 (HIF-1) was needed to activate the enhancer of which gene in hypoxic cells?", ["Thyroglobulin", "Erythropoietin", "Ferroportin", "Preproinsulin"],
  "HIF-1 drives transcription from the erythropoietin enhancer when oxygen is low, linking oxygen sensing to red-cell production.", "Erythropoietin."),
 ("¿El factor inducible por hipoxia 1 (HIF-1) era necesario para activar el potenciador de qué gen en células hipóxicas?", ["Tiroglobulina", "Eritropoyetina", "Ferroportina", "Preproinsulina"],
  "El HIF-1 activa la transcripción desde el potenciador de la eritropoyetina cuando falta oxígeno, uniendo la detección de O2 con la producción de glóbulos rojos.", "Eritropoyetina.")),
("7539918", "expert", 2, "both HIF-1 subunits are basic-helix-loop-helix proteins containing a PAS domain",
 ("What kind of proteins are both subunits of hypoxia-inducible factor 1, according to Wang and Semenza (1995)?", ["Zinc-finger proteins", "Homeobox proteins", "bHLH-PAS proteins", "Leucine zipper kinases"],
  "Both HIF-1 subunits are basic-helix-loop-helix proteins with a PAS domain; HIF-1 beta is ARNT.", "bHLH-PAS."),
 ("¿Qué tipo de proteínas son las dos subunidades del factor inducible por hipoxia 1, según Wang y Semenza (1995)?", ["Proteínas dedo de zinc", "Proteínas homeobox", "Proteínas bHLH-PAS", "Cinasas con cremallera"],
  "Ambas subunidades del HIF-1 son proteínas hélice-bucle-hélice básicas con dominio PAS; HIF-1 beta es ARNT.", "bHLH-PAS.")),

# --- Artificial surfactant (6101413)
("6101413", "explorer", 3, "Eight infants survived, including five of six with birthweight less than 1500 g",
 ("In Fujiwara's 1980 report, 10 preterm infants with severe hyaline-membrane disease received artificial surfactant. How many survived?", ["Two of ten", "Four of ten", "None of them", "Eight of ten"],
  "Eight of ten survived, including five of six weighing under 1500 g; two died of unrelated causes.", "Eight."),
 ("En el informe de Fujiwara de 1980, 10 prematuros con enfermedad de membrana hialina grave recibieron surfactante artificial. ¿Cuántos sobrevivieron?", ["Dos de diez", "Cuatro de diez", "Ninguno", "Ocho de diez"],
  "Sobrevivieron ocho de diez, incluidos cinco de seis con menos de 1500 g; dos murieron por causas no relacionadas.", "Ocho.")),
("6101413", "researcher", 0, "In nine infants a patent ductus arteriosus became evident after recovery from HMD",
 ("Which complication became evident in nine infants after they recovered from hyaline-membrane disease with artificial surfactant?", ["Patent ductus arteriosus", "Necrotizing enterocolitis", "Bilateral pneumothorax", "Intraventricular bleeding"],
  "As lung function improved, a patent ductus arteriosus appeared in nine infants and required more ventilation.", "Patent ductus."),
 ("¿Qué complicación apareció en nueve bebés tras recuperarse de la membrana hialina con surfactante artificial?", ["Conducto arterioso persistente", "Enterocolitis necrotizante", "Neumotórax bilateral", "Hemorragia intraventricular grave"],
  "Al mejorar la función pulmonar, apareció un conducto arterioso persistente en nueve bebés, que necesitaron más ventilación.", "Conducto arterioso.")),

# --- CHIP28 / aquaporin-1 (1373524)
("1373524", "explorer", 1, "this was reversibly inhibited by mercuric chloride, a known inhibitor of water channels",
 ("In Agre's 1992 Xenopus oocyte experiment, which compound reversibly blocked the water permeability conferred by CHIP28 (aquaporin-1)?", ["Lithium carbonate", "Mercuric chloride", "Sodium cyanide", "Potassium ferricyanide"],
  "Mercuric chloride, a known water-channel inhibitor, reversibly blocked the effect, supporting CHIP28 as a water channel.", "Mercuric chloride."),
 ("En el experimento de Agre de 1992 con ovocitos de Xenopus, ¿qué compuesto bloqueó reversiblemente la permeabilidad al agua dada por CHIP28 (acuaporina-1)?", ["Carbonato de litio", "Cloruro mercúrico", "Cianuro de sodio", "Yoduro de potasio"],
  "El cloruro mercúrico, inhibidor conocido de los canales de agua, bloqueó el efecto de forma reversible, lo que apoyó que CHIP28 es un canal de agua.", "Cloruro mercúrico.")),
("1373524", "curious", 2, "exhibited increased osmotic water permeability",
 ("What happened when frog oocytes were made to express the red-cell protein CHIP28, later called aquaporin-1?", ["They lost all water", "They became fully impermeable", "Water permeability rose", "They secreted insulin"],
  "The oocytes became much more permeable to water, revealing the first molecular water channel.", "More water entry."),
 ("¿Qué ocurrió cuando ovocitos de rana expresaron la proteína eritrocitaria CHIP28, luego llamada acuaporina-1?", ["Perdieron toda el agua", "Se volvieron impermeables", "Dejaron pasar más agua", "Secretaron insulina"],
  "Los ovocitos se volvieron mucho más permeables al agua, lo que reveló el primer canal molecular de agua.", "Más entrada de agua.")),

# --- Collecting-duct water channel / aquaporin-2 (8429910)
("8429910", "researcher", 3, "suggest that WCH-CD is the vasopressin-regulated water channel",
 ("The water channel WCH-CD (aquaporin-2), cloned from the rat collecting tubule in 1993, is regulated by which hormone?", ["Aldosterone", "Insulin", "Cortisol", "Vasopressin"],
  "WCH-CD sits at the apical membrane of collecting-tubule cells and is the vasopressin-regulated water channel.", "Vasopressin (ADH)."),
 ("El canal de agua WCH-CD (acuaporina-2), clonado del túbulo colector de rata en 1993, ¿por qué hormona está regulado?", ["Aldosterona", "Insulina", "Cortisol", "Vasopresina"],
  "WCH-CD está en la membrana apical de las células del túbulo colector y es el canal de agua regulado por vasopresina.", "Vasopresina (ADH).")),
("8429910", "explorer", 0, "WCH-CD transcripts are detected only in the collecting tubule of the kidney",
 ("Where were transcripts of the water channel WCH-CD (aquaporin-2) detected in the 1993 Nature study?", ["Collecting tubule", "Loop of Henle cells", "Red blood cells", "Glomerulus"],
  "Unlike CHIP28, found in red cells and the proximal tubule, WCH-CD was detected only in the kidney collecting tubule.", "Collecting tubule."),
 ("¿Dónde se detectaron los transcritos del canal de agua WCH-CD (acuaporina-2) en el estudio de Nature de 1993?", ["Túbulo colector", "Células del asa de Henle", "Glóbulos rojos", "Glomérulo"],
  "A diferencia de CHIP28, presente en eritrocitos y túbulo proximal, WCH-CD se detectó solo en el túbulo colector renal.", "Túbulo colector.")),

# --- Vasopressin and osmolarity review (31365096)
("31365096", "expert", 1, "an AVP receptor 2 blocker is now licensed for CKD related to polycystic kidney disease",
 ("According to a 2019 review on vasopressin and osmolarity, a vasopressin V2 receptor blocker is licensed for CKD due to which condition?", ["Diabetic nephropathy", "Polycystic kidneys", "IgA nephropathy", "Lupus nephritis"],
  "Because vasopressin is linked to CKD progression, a V2 receptor blocker is licensed for polycystic kidney disease.", "Polycystic kidney disease."),
 ("Según una revisión de 2019 sobre vasopresina y osmolaridad, ¿para la ERC por qué afección está aprobado un bloqueador del receptor V2?", ["Nefropatía diabética", "Riñones poliquísticos", "Nefropatía por IgA", "Nefritis lúpica"],
  "Como la vasopresina se asocia con la progresión de la ERC, un bloqueador del receptor V2 está aprobado para la poliquistosis renal.", "Poliquistosis renal.")),

# --- per RNA feedback (2105471)
("2105471", "explorer", 2, "there is a feedback loop through which the activity of per-encoded protein causes cycling of its own RNA",
 ("What did Hardin, Hall and Rosbash (1990) propose about the Drosophila PERIOD protein?", ["It degrades light receptors", "It is made only at night", "It regulates its own mRNA", "It stops cell division"],
  "PER feeds back to make its own RNA oscillate, the core idea of the transcriptional feedback clock.", "Feeds back on its mRNA."),
 ("¿Qué propusieron Hardin, Hall y Rosbash (1990) sobre la proteína PERIOD de Drosophila?", ["Degrada los receptores de luz", "Se produce solo de noche", "Regula su propio ARNm", "Detiene la división celular"],
  "PER retroalimenta su propio ARN y lo hace oscilar, la idea central del reloj por retroalimentación transcripcional.", "Regula su ARNm.")),

# --- Clock mutants (5002428)
("5002428", "curious", 3, "One mutant is arrhythmic; another has a period of 19 hr; a third has a period of 28 hr",
 ("Konopka and Benzer (1971) found three Drosophila clock mutants: one arrhythmic and two with altered periods. What were those periods?", ["12 h and 48 h", "22 h and 26 h", "6 h and 36 h", "19 h and 28 h"],
  "One mutant was arrhythmic, one ran a 19-hour and another a 28-hour rhythm, all mapping to one gene.", "19 h and 28 h."),
 ("Konopka y Benzer (1971) hallaron tres mutantes de reloj en Drosophila: uno arrítmico y dos con periodos alterados. ¿Cuáles eran esos periodos?", ["12 h y 48 h", "22 h y 26 h", "6 h y 36 h", "19 h y 28 h"],
  "Un mutante era arrítmico, otro tenía un ritmo de 19 horas y otro de 28 horas, todos en un mismo gen.", "19 h y 28 h.")),

# --- 2017 Nobel Prize circadian review (29673553)
("29673553", "beginner", 0, "The cloning and characterization of the first Drosophila clock gene period",
 ("The 2017 Nobel Prize honored circadian clock research. In which animal was the first clock gene, 'period', cloned?", ["Fruit fly", "Mouse", "Zebrafish", "Earthworm"],
  "Hall, Rosbash and Young cloned period in the fruit fly Drosophila in the early 1980s.", "Fruit fly."),
 ("El Premio Nobel 2017 premió la investigación del reloj circadiano. ¿En qué animal se clonó el primer gen de reloj, 'period'?", ["Mosca de la fruta", "Ratón", "Pez cebra", "Lombriz de tierra"],
  "Hall, Rosbash y Young clonaron period en la mosca de la fruta Drosophila a inicios de los años ochenta.", "Mosca de la fruta.")),
("29673553", "researcher", 1, "transcriptional translational feedback loop (TTFL) model",
 ("Which model of the ~24-hour circadian oscillator emerged from the work honored by the 2017 Nobel Prize?", ["Membrane potential oscillator", "Transcriptional feedback loop", "Calcium wave relay", "Hormonal pulse generator"],
  "Their discoveries established the transcriptional-translational feedback loop (TTFL) that generates a ~24 h rhythm.", "TTFL."),
 ("¿Qué modelo del oscilador circadiano de ~24 horas surgió del trabajo premiado con el Nobel 2017?", ["Oscilador de potencial de membrana", "Retroalimentación transcripcional", "Relevo de ondas de calcio", "Generador de pulsos hormonales"],
  "Sus descubrimientos establecieron el bucle de retroalimentación transcripcional-traduccional (TTFL), que genera un ritmo de ~24 h.", "TTFL.")),

# --- Brown adipose tissue in adults (19357406)
("19357406", "explorer", 0, "Positive scans were seen in 76 of 1013 women (7.5%) and 30 of 959 men (3.1%), corresponding to a female:male ratio greater than 2:1",
 ("In the 2009 PET-CT study of brown fat in adults, how did detection differ between the sexes?", ["Women, by over 2:1", "Men, by about 3:1", "Equal in both sexes", "Men, by about 5:1"],
  "Brown fat was seen in 7.5% of women and 3.1% of men, and women also had more of it.", "More in women."),
 ("En el estudio PET-TC de 2009 sobre grasa parda en adultos, ¿cómo difirió la detección entre sexos?", ["Mujeres, más de 2:1", "Hombres, cerca de 3:1", "Igual en ambos sexos", "Hombres, cerca de 5:1"],
  "Se vio grasa parda en el 7,5% de las mujeres y el 3,1% de los hombres, y ellas además tenían más cantidad.", "Más en mujeres.")),
("19357406", "researcher", 1, "The probability of the detection of brown adipose tissue was inversely correlated with years of age (P<0.001), outdoor temperature at the time of the scan (P=0.02), beta-blocker use",
 ("In the 2009 study of brown adipose tissue in adults, which factor was linked to a LOWER chance of detecting it?", ["Female sex", "Beta-blocker use", "Cold outdoor weather", "Younger age"],
  "Detection fell with age, warmer outdoor temperature, beta-blocker use and, in older patients, higher BMI.", "Beta-blockers."),
 ("En el estudio de 2009 sobre tejido adiposo pardo en adultos, ¿qué factor se asoció con MENOR probabilidad de detectarlo?", ["Sexo femenino", "Uso de betabloqueantes", "Clima exterior muy frío", "Edad más joven"],
  "La detección bajaba con la edad, la temperatura exterior más alta, los betabloqueantes y, en mayores, un IMC más alto.", "Betabloqueantes.")),

# --- Waterfall model of clotting (14173416)
("14173416", "explorer", 2, "each cloting factor except fibrinogen is converted to a form that has enzymatic activity",
 ("In Davie and Ratnoff's 1964 'waterfall' model of clotting, which factor is NOT converted into an active enzyme?", ["Prothrombin", "Factor X", "Fibrinogen", "Factor XII"],
  "Each factor is activated into an enzyme that activates the next, except fibrinogen, which becomes the fibrin clot.", "Fibrinogen."),
 ("En el modelo de 'cascada' de la coagulación de Davie y Ratnoff (1964), ¿qué factor NO se convierte en una enzima activa?", ["Protrombina", "Factor X", "Fibrinógeno", "Factor XII"],
  "Cada factor se activa como enzima que activa al siguiente, salvo el fibrinógeno, que se convierte en el coágulo de fibrina.", "Fibrinógeno.")),

# --- Cell-based model of coagulation (14697207)
("14697207", "researcher", 3, "coagulation takes place on different cell surfaces in three overlapping steps: initiation, amplification, and propagation",
 ("The cell-based model of haemostasis replaced the classic cascade. What are its three overlapping steps?", ["Contact, intrinsic, common", "Adhesion, secretion, lysis", "Vasoconstriction, aggregation, fibrinolysis", "Initiation, amplification, propagation"],
  "Coagulation occurs on cell surfaces in initiation, amplification and propagation phases.", "Initiation, amplification, propagation."),
 ("El modelo celular de la hemostasia reemplazó la cascada clásica. ¿Cuáles son sus tres etapas superpuestas?", ["Contacto, intrínseca, común", "Adhesión, secreción, lisis", "Vasoconstricción, agregación, fibrinólisis", "Iniciación, amplificación, propagación"],
  "La coagulación ocurre sobre superficies celulares en fases de iniciación, amplificación y propagación.", "Iniciación, amplificación, propagación.")),

# --- NINDS t-PA stroke trial (7477192)
("7477192", "explorer", 0, "patients treated with t-PA were at least 30 percent more likely to have minimal or no disability at three months",
 ("In the 1995 NINDS trial, what did intravenous t-PA (a fibrinolytic) given within 3 hours of ischemic stroke achieve?", ["Less disability at 3 months", "No benefit at any time point", "Halved 3-month mortality", "Fewer brain hemorrhages"],
  "t-PA patients were at least 30% more likely to have minimal or no disability, despite more symptomatic hemorrhages.", "Less disability."),
 ("En el ensayo NINDS de 1995, ¿qué logró el t-PA intravenoso (un fibrinolítico) dado dentro de las 3 horas del ACV isquémico?", ["Menos discapacidad a 3 meses", "Ningún beneficio en ningún momento", "Redujo a la mitad la mortalidad", "Menos hemorragias cerebrales"],
  "Los pacientes con t-PA tuvieron al menos 30% más probabilidad de discapacidad mínima o nula, pese a más hemorragias sintomáticas.", "Menos discapacidad.")),

# --- Limits of VO2max (10647532)
("10647532", "explorer", 1, "O2 delivery, not skeletal muscle O2 extraction, is viewed as the primary limiting factor for VO2max",
 ("According to Bassett and Howley (2000), what primarily limits maximal oxygen uptake (VO2max) in exercising humans?", ["Muscle O2 extraction", "Oxygen delivery", "Lung ventilation alone", "Blood glucose supply"],
  "Evidence from blood doping, hypoxia and beta-blockade shows VO2max follows the cardiorespiratory delivery of oxygen.", "O2 delivery."),
 ("Según Bassett y Howley (2000), ¿qué limita principalmente el consumo máximo de oxígeno (VO2máx) al hacer ejercicio?", ["Extracción muscular de O2", "El aporte de oxígeno", "Solo la ventilación", "El aporte de glucosa"],
  "El dopaje sanguíneo, la hipoxia y los betabloqueantes muestran que el VO2máx sigue al aporte cardiorrespiratorio de oxígeno.", "Aporte de O2.")),
("10647532", "researcher", 2, "the increase in VO2max with training results primarily from an increase in maximal cardiac output",
 ("What mainly explains the rise in VO2max after endurance training, according to Bassett and Howley?", ["Larger lung volume", "Wider a-v O2 difference", "Higher cardiac output", "More hemoglobin per cell"],
  "Training raises VO2max mainly by increasing maximal cardiac output, not the arteriovenous O2 difference.", "Cardiac output."),
 ("¿Qué explica principalmente el aumento del VO2máx tras el entrenamiento de resistencia, según Bassett y Howley?", ["Mayor volumen pulmonar", "Mayor diferencia a-v de O2", "Mayor gasto cardíaco máximo", "Más hemoglobina por célula"],
  "El entrenamiento eleva el VO2máx sobre todo al aumentar el gasto cardíaco máximo, no la diferencia arteriovenosa de O2.", "Gasto cardíaco.")),
]
