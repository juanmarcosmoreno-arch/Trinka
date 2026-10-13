# Human nutrition II — landmark trials and meta-analyses: VITAL (vitamin D, omega-3, fractures),
# dietary fibre, time-restricted eating, salt substitutes, folic acid and neural tube defects,
# sugar-sweetened beverages, global dietary risks, infant iron, breastfeeding, vitamin A in measles.
# Sources: PubMed trial and review abstracts. Excerpts verbatim.
CATEGORY = "nutrition"
Q = [
# --- VITAL vitamin D (30415629)
("30415629", "explorer", 2, "Supplementation with vitamin D did not result in a lower incidence of invasive cancer or cardiovascular events than placebo",
 ("In the VITAL trial, did 2000 IU/day of vitamin D prevent cancer or cardiovascular events?", ["Yes, it halved both", "Only cancer, by 50%", "No, neither was reduced", "Only heart attacks, by 50%"],
  "Among ~26,000 older US adults, vitamin D did not lower invasive cancer or major cardiovascular events.", "No."),
 ("En el ensayo VITAL, ¿2000 UI/día de vitamina D previnieron el cáncer o los eventos cardiovasculares?", ["Sí, redujo ambos a la mitad", "Solo el cáncer, en 50%", "No, no redujo ninguno", "Solo los infartos, en 50%"],
  "En unos 26.000 adultos mayores de EE. UU., la vitamina D no redujo el cáncer invasivo ni los eventos cardiovasculares.", "No.")),
("35939577", "researcher", 0, "Vitamin D3 supplementation did not result in a significantly lower risk of fractures than placebo",
 ("What did the VITAL fracture substudy find for generally healthy adults taking vitamin D3?", ["No significant drop in fractures", "Hip fractures fell by 70%", "Fractures doubled with vitamin D", "Only vertebral fractures fell"],
  "Without selecting for deficiency or osteoporosis, vitamin D3 did not reduce total, nonvertebral or hip fractures.", "No fewer fractures."),
 ("¿Qué halló el subestudio de fracturas de VITAL en adultos sanos que tomaban vitamina D3?", ["Ninguna baja significativa de fracturas", "Las fracturas de cadera bajaron un 70%", "Las fracturas se duplicaron", "Solo bajaron las vertebrales"],
  "Sin seleccionar por déficit u osteoporosis, la vitamina D3 no redujo fracturas totales, no vertebrales ni de cadera.", "Sin menos fracturas.")),

# --- VITAL omega-3 (30415637)
("30415637", "researcher", 3, "for total myocardial infarction, 0.72 (95% CI, 0.59 to 0.90)",
 ("In VITAL, omega-3 supplements did not reduce the primary endpoints, but which secondary outcome was lower?", ["Total stroke incidence", "Deaths from cancer", "Death from any cause", "Myocardial infarction"],
  "The hazard ratio for myocardial infarction was 0.72, while major events overall and cancer were not reduced.", "Heart attacks."),
 ("En VITAL, el omega-3 no redujo los objetivos principales, pero ¿qué resultado secundario fue menor?", ["El ACV total", "Las muertes por cáncer", "Las muertes por toda causa", "El infarto de miocardio"],
  "La razón de riesgo para infarto fue 0,72, aunque los eventos mayores en conjunto y el cáncer no bajaron.", "Los infartos.")),

# --- Carbohydrate quality (30638909)
("30638909", "explorer", 1, "Risk reduction associated with a range of critical outcomes was greatest when daily intake of dietary fibre was between 25 g and 29 g",
 ("According to this Lancet meta-analysis, what daily fibre intake was linked to the greatest risk reduction?", ["5 to 9 g", "25 to 29 g", "60 to 70 g", "Over 100 g"],
  "Benefits were greatest at 25–29 g/day, and higher intakes might protect even more.", "25–29 g."),
 ("Según este metaanálisis de The Lancet, ¿qué consumo diario de fibra se asoció con la mayor reducción de riesgo?", ["5 a 9 g", "25 a 29 g", "60 a 70 g", "Más de 100 g"],
  "Los beneficios fueron máximos con 25–29 g/día, y consumos mayores podrían proteger aún más.", "25–29 g.")),
("30638909", "researcher", 2, "Observational data suggest a 15-30% decrease in all-cause and cardiovascular related mortality",
 ("How much lower was all-cause and cardiovascular mortality in the highest versus lowest fibre consumers?", ["About 1–3%", "About 50–70%", "About 15–30%", "No difference"],
  "Cohorts showed 15–30% lower mortality and fewer cases of heart disease, stroke, diabetes and colorectal cancer.", "15–30%."),
 ("¿Cuánto menor era la mortalidad total y cardiovascular en quienes más fibra consumían frente a quienes menos?", ["Cerca del 1–3%", "Cerca del 50–70%", "Cerca del 15–30%", "Sin diferencias"],
  "Las cohortes mostraron 15–30% menos mortalidad y menos cardiopatía, ACV, diabetes y cáncer colorrectal.", "15–30%.")),
("30638909", "expert", 0, "Smaller or no risk reductions were found with the observational data when comparing the effects of diets characterised by low rather than higher glycaemic index or load",
 ("How did glycemic index or load compare with fibre as a marker of carbohydrate quality?", ["It showed smaller or no benefits", "It predicted health far better", "It was identical to fibre", "It was the only useful marker"],
  "Low glycemic index or load diets gave small or no risk reductions; evidence certainty was low.", "Weaker marker."),
 ("¿Cómo se comparó el índice o la carga glucémica con la fibra como marcador de calidad de los carbohidratos?", ["Mostró beneficios menores o nulos", "Predijo los resultados mucho mejor", "Fue idéntico a la fibra", "Fue el único marcador útil"],
  "Las dietas de bajo índice o carga glucémica dieron reducciones pequeñas o nulas; la certeza fue baja.", "Marcador más débil.")),

# --- Time-restricted eating (35443107)
("35443107", "explorer", 3, "a regimen of time-restricted eating was not more beneficial with regard to reduction in body weight, body fat, or metabolic risk factors than daily calorie restriction",
 ("When both groups cut calories, did eating only between 8 a.m. and 4 p.m. add weight loss after 12 months?", ["Yes, it doubled weight loss", "Yes, but only in women", "It caused weight gain", "No, it gave no extra benefit"],
  "Weight loss was −8.0 vs −6.3 kg, a non-significant difference; metabolic outcomes were also similar.", "No extra benefit."),
 ("Si ambos grupos reducían calorías, ¿comer solo entre las 8 y las 16 h agregó pérdida de peso a los 12 meses?", ["Sí, duplicó la pérdida de peso", "Sí, pero solo en mujeres", "Hizo aumentar de peso", "No, no agregó beneficio"],
  "La pérdida fue −8,0 frente a −6,3 kg, una diferencia no significativa; los resultados metabólicos también fueron similares.", "Sin beneficio extra.")),

# --- Salt substitution (34459569)
("34459569", "researcher", 1, "participants used a salt substitute (75% sodium chloride and 25% potassium chloride by mass)",
 ("What was the composition of the salt substitute used in the Chinese village trial?", ["100% potassium chloride", "75% NaCl and 25% KCl", "50% NaCl and 50% sugar", "Sea salt with added iodine"],
  "The substitute replaced a quarter of sodium chloride with potassium chloride.", "75% NaCl, 25% KCl."),
 ("¿Qué composición tenía el sustituto de sal usado en el ensayo en aldeas chinas?", ["100% cloruro de potasio", "75% NaCl y 25% KCl", "50% NaCl y 50% azúcar", "Sal marina con yodo agregado"],
  "El sustituto reemplazaba un cuarto del cloruro de sodio por cloruro de potasio.", "75% NaCl, 25% KCl.")),
("34459569", "explorer", 0, "the rates of stroke, major cardiovascular events, and death from any cause were lower with the salt substitute than with regular salt",
 ("What happened to stroke, cardiovascular events and deaths with the salt substitute?", ["All three were lower", "Only stroke rose a little", "Deaths from hyperkalemia rose", "Nothing changed at all"],
  "All three fell, without a significant rise in serious hyperkalemia.", "All lower."),
 ("¿Qué pasó con el ACV, los eventos cardiovasculares y las muertes con el sustituto de sal?", ["Los tres fueron menores", "Solo el ACV subió un poco", "Subieron las muertes por hiperpotasemia", "No cambió nada"],
  "Los tres bajaron, sin un aumento significativo de hiperpotasemia grave.", "Los tres bajaron.")),

# --- MRC Vitamin Study (1677062)
("1677062", "researcher", 2, "a 72% protective effect",
 ("How much did folic acid around conception protect against recurrent neural tube defects in the MRC trial?", ["About 12%", "About 32%", "About 72%", "About 100%"],
  "Folic acid gave a 72% protective effect; the other vitamins showed no significant protection.", "~72%."),
 ("¿Cuánto protegió el ácido fólico periconcepcional contra la recurrencia de defectos del tubo neural en el ensayo MRC?", ["Cerca del 12%", "Cerca del 32%", "Cerca del 72%", "Cerca del 100%"],
  "El ácido fólico protegió en un 72%; las otras vitaminas no mostraron protección significativa.", "~72%.")),
("1677062", "explorer", 3, "public health measures should be taken to ensure that the diet of all women who may bear children contains an adequate amount of folic acid",
 ("What public health action did the MRC Vitamin Study recommend?", ["Avoid all B vitamins in pregnancy", "Give folic acid only after birth", "Test every baby's spine at birth", "Ensure enough folic acid for women"],
  "The diet of all women who may become pregnant should contain enough folic acid.", "Folic acid for all women."),
 ("¿Qué medida de salud pública recomendó el MRC Vitamin Study?", ["Evitar toda vitamina B en el embarazo", "Dar ácido fólico solo tras el parto", "Revisar la columna de cada bebé al nacer", "Asegurar ácido fólico a las mujeres"],
  "La dieta de todas las mujeres que puedan quedar embarazadas debe tener suficiente ácido fólico.", "Ácido fólico para todas.")),

# --- DRINK trial (22998340)
("22998340", "researcher", 0, "Masked replacement of sugar-containing beverages with noncaloric beverages reduced weight gain and fat accumulation in normal-weight children",
 ("In the DRINK trial, what did replacing a daily sugary drink with a sugar-free one do in children?", ["Less weight gain and fat", "No effect on weight at all", "More weight gain and fat", "Only lowered their height"],
  "Over 18 months, the sugar-free group gained about 1 kg less and accumulated less fat.", "Less weight gain."),
 ("En el ensayo DRINK, ¿qué logró reemplazar una bebida azucarada diaria por una sin azúcar en niños?", ["Menos aumento de peso y grasa", "Ningún efecto sobre el peso", "Más aumento de peso y grasa", "Solo redujo su estatura"],
  "En 18 meses, el grupo sin azúcar aumentó cerca de 1 kg menos y acumuló menos grasa.", "Menos aumento de peso.")),
("22998340", "expert", 1, "possibly because liquid sugars do not lead to a sense of satiety",
 ("Why might sugary drinks promote overweight, according to the DRINK investigators?", ["They contain hidden fat", "Liquid sugar gives little satiety", "They block thyroid hormone", "They reduce everyday physical activity"],
  "Calories from liquids do not create satiety, so other food intake is not reduced.", "Little satiety."),
 ("Según los investigadores de DRINK, ¿por qué las bebidas azucaradas favorecerían el sobrepeso?", ["Contienen grasa oculta", "El azúcar líquido sacia poco", "Bloquean la hormona tiroidea", "Reducen la actividad física"],
  "Las calorías líquidas no generan saciedad, así que no se reduce lo que se come.", "Sacian poco.")),

# --- GBD dietary risks (30954305)
("30954305", "explorer", 2, "In 2017, 11 million (95% uncertainty interval [UI] 10-12) deaths and 255 million (234-274) DALYs were attributable to dietary risk factors",
 ("How many deaths worldwide were attributed to dietary risks in 2017?", ["About 1 million", "About 110 million", "About 11 million", "About 100,000"],
  "Suboptimal diet caused about 11 million deaths and 255 million DALYs.", "~11 million."),
 ("¿Cuántas muertes en el mundo se atribuyeron a riesgos de la dieta en 2017?", ["Cerca de 1 millón", "Cerca de 110 millones", "Cerca de 11 millones", "Cerca de 100.000"],
  "La mala alimentación causó cerca de 11 millones de muertes y 255 millones de AVAD.", "~11 millones.")),
("30954305", "researcher", 3, "High intake of sodium (3 million [1-5] deaths and 70 million [34-118] DALYs), low intake of whole grains (3 million [2-4] deaths and 82 million [59-109] DALYs), and low intake of fruits",
 ("Which dietary risks were the leading causes of diet-related deaths globally?", ["Too much red meat, eggs and milk", "Too little coffee, tea and water", "Too much fat, protein and fibre", "High salt, low whole grains, fruit"],
  "High sodium, low whole grains and low fruit intake led the dietary risks for deaths and DALYs.", "Sodium, grains, fruit."),
 ("¿Qué riesgos alimentarios fueron las principales causas de muertes ligadas a la dieta en el mundo?", ["Exceso de carne roja, huevos y leche", "Poco café, té y agua", "Exceso de grasa, proteína y fibra", "Mucho sodio, poco integral y fruta"],
  "Mucho sodio, pocos granos integrales y poca fruta encabezaron los riesgos de muerte y AVAD.", "Sodio, granos, fruta.")),

# --- Iron in Bangladeshi infants (34496174)
("34496174", "researcher", 1, "3 months of daily supplementation with iron syrup or multiple micronutrient powders did not appear to have an effect on child development",
 ("In Bangladeshi infants, what did 3 months of iron syrup or micronutrient powders do for cognitive development?", ["Raised it by many points", "No apparent effect", "Lowered it markedly", "Only helped girls"],
  "No developmental or growth benefit was seen, although anemia and iron deficiency were lower later on.", "No apparent effect."),
 ("En lactantes de Bangladesh, ¿qué efecto tuvieron 3 meses de jarabe de hierro o micronutrientes en polvo sobre el desarrollo cognitivo?", ["Lo subió muchos puntos", "Ningún efecto aparente", "Lo bajó notablemente", "Solo ayudó a las niñas"],
  "No hubo beneficio en desarrollo ni crecimiento, aunque luego hubo menos anemia y déficit de hierro.", "Sin efecto aparente.")),

# --- Breastfeeding (26869575)
("26869575", "explorer", 0, "only 37% of children younger than 6 months of age are exclusively breastfed",
 ("In low- and middle-income countries, what share of infants under 6 months are exclusively breastfed?", ["About 37%", "About 87%", "About 7%", "About 67%"],
  "Only about a third are exclusively breastfed, and durations are even shorter in high-income countries.", "~37%."),
 ("En países de ingresos bajos y medios, ¿qué proporción de bebés menores de 6 meses recibe lactancia exclusiva?", ["Cerca del 37%", "Cerca del 87%", "Cerca del 7%", "Cerca del 67%"],
  "Solo cerca de un tercio recibe lactancia exclusiva, y en países ricos la duración es aún menor.", "~37%.")),
("26869575", "researcher", 2, "could prevent 823,000 annual deaths in children younger than 5 years and 20,000 annual deaths from breast cancer",
 ("How many child deaths per year could near-universal breastfeeding prevent, according to this Lancet series?", ["About 8,000", "About 82,000", "About 823,000", "About 8 million"],
  "Scaling up breastfeeding could prevent ~823,000 under-5 deaths and 20,000 breast cancer deaths yearly.", "~823,000."),
 ("Según esta serie de The Lancet, ¿cuántas muertes infantiles por año podría evitar una lactancia casi universal?", ["Cerca de 8.000", "Cerca de 82.000", "Cerca de 823.000", "Cerca de 8 millones"],
  "Ampliar la lactancia podría evitar ~823.000 muertes de menores de 5 años y 20.000 por cáncer de mama al año.", "~823.000.")),
("26869575", "expert", 3, "we noted an increase in tooth decay with longer periods of breastfeeding",
 ("Which outcome was associated with LONGER breastfeeding in these meta-analyses?", ["More childhood infections", "Lower intelligence scores", "More malocclusion", "More tooth decay"],
  "Breastfeeding protected against infections and malocclusion, but longer periods were linked to more caries.", "Tooth decay."),
 ("¿Qué resultado se asoció con una lactancia MÁS prolongada en estos metaanálisis?", ["Más infecciones infantiles", "Menor inteligencia", "Más maloclusión", "Más caries dentales"],
  "La lactancia protegía contra infecciones y maloclusión, pero los períodos más largos se asociaron con más caries.", "Caries.")),

# --- Vitamin A in severe measles (2194128)
("2194128", "researcher", 1, "the risk of death or a major complication during the hospital stay was half that of the control group",
 ("In South African children with severe measles, what did high-dose vitamin A achieve?", ["No measurable benefit of any kind", "Halved death or major complications", "It made pneumonia far more frequent", "It only shortened the rash"],
  "Vitamin A sped recovery from pneumonia and diarrhea and halved death or major complications.", "Halved bad outcomes."),
 ("En niños sudafricanos con sarampión grave, ¿qué logró la vitamina A en dosis alta?", ["Ningún beneficio medible de ningún tipo", "Mitad de muertes y complicaciones", "Empeoró la neumonía", "Solo acortó el exantema"],
  "La vitamina A aceleró la recuperación de la neumonía y la diarrea y redujo a la mitad muertes o complicaciones mayores.", "Mitad de malos resultados.")),
("2194128", "explorer", 3, "all children with severe measles should be given vitamin A supplements, whether or not they are thought to have a nutritional deficiency",
 ("Which children with measles did the authors say should receive vitamin A?", ["Only those with night blindness", "Only those who are underweight", "Only those under 6 months old", "All with severe measles"],
  "Most had low serum retinol even without obvious deficiency, so all severe cases should get vitamin A.", "All severe cases."),
 ("¿Qué niños con sarampión debían recibir vitamina A, según los autores?", ["Solo los que tienen ceguera nocturna", "Solo los de bajo peso", "Solo los menores de 6 meses", "Todos los de sarampión grave"],
  "La mayoría tenía retinol bajo aun sin déficit evidente, así que todos los casos graves deben recibir vitamina A.", "Todos los graves.")),
]
