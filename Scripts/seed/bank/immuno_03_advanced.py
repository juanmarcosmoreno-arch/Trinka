# Immunology III — innate sensing, T-cell subsets and tolerance, germinal centers and memory, vaccines,
# immunotherapy, transplantation and autoimmune/allergic disease.
# Sources: PubMed reviews and StatPearls chapters (abstracts). Excerpts verbatim.
CATEGORY = "immunology"
Q = [
# --- Herd immunity (22561998)
("22561998", "curious", 2, "The conventional idea of herd immunity is based on the relationship between the transmission dynamics of infectious agents and population immunity",
 ("What is herd immunity based on?", ["The number of doctors in a country", "Antibiotic use in animals", "The relationship between pathogen transmission and immunity in the population", "Genetic resistance of a single person"],
  "Herd immunity arises when enough people are immune that transmission chains break, indirectly protecting the unvaccinated.", "Transmission vs. population immunity."),
 ("¿En qué se basa la inmunidad de rebaño?", ["En la cantidad de médicos de un país", "En el uso de antibióticos en animales", "En la relación entre la transmisión del patógeno y la inmunidad de la población", "En la resistencia genética de una persona"],
  "La inmunidad de rebaño surge cuando hay suficientes inmunes como para cortar las cadenas de transmisión y proteger indirectamente a los no vacunados.", "Transmisión vs. inmunidad poblacional.")),
("22561998", "researcher", 0, "meningococcal conjugate vaccines are superior to polysaccharide vaccines",
 ("Why do conjugate vaccines provide better herd protection than plain polysaccharide vaccines?", ["Conjugation to a protein recruits T-cell help, giving memory and reducing carriage", "They contain live bacteria", "They are given orally", "They contain antibiotics"],
  "Conjugate vaccines (meningococcal, pneumococcal, Hib) outperform polysaccharide vaccines; protein conjugation engages T-cell help and reduces carriage.", "T-cell help."),
 ("¿Por qué las vacunas conjugadas dan mejor protección de rebaño que las polisacáridas simples?", ["La conjugación a una proteína recluta ayuda T, genera memoria y reduce la portación", "Contienen bacterias vivas", "Se dan por boca", "Contienen antibióticos"],
  "Las vacunas conjugadas (meningococo, neumococo, Hib) superan a las polisacáridas; la proteína conjugada recluta ayuda T y reduce la portación.", "Ayuda T.")),
("22561998", "explorer", 3, "Achieving a very high uptake rate should be the target for certain vaccines, for example, measles vaccine",
 ("For which vaccine is a very high coverage especially important to stop transmission?", ["Tetanus", "Rabies", "Yellow fever", "Measles"],
  "Highly contagious diseases such as measles need very high vaccine uptake for herd immunity.", "Measles."),
 ("¿Para qué vacuna es especialmente importante una cobertura muy alta para cortar la transmisión?", ["Tétanos", "Rabia", "Fiebre amarilla", "Sarampión"],
  "Las enfermedades muy contagiosas como el sarampión requieren coberturas muy altas para lograr inmunidad de rebaño.", "Sarampión.")),

# --- Adjuvants (37468460)
("37468460", "curious", 1, "Adjuvants are indispensable components of vaccines",
 ("What is a vaccine adjuvant?", ["The vaccine's antigen", "A component that enhances the immune response to the antigen", "A preservative that kills bacteria", "The syringe material"],
  "Adjuvants boost and shape the immune response to vaccine antigens.", "Immune enhancer."),
 ("¿Qué es un adyuvante de una vacuna?", ["El antígeno de la vacuna", "Un componente que potencia la respuesta inmune al antígeno", "Un conservante que mata bacterias", "El material de la jeringa"],
  "Los adyuvantes potencian y orientan la respuesta inmune a los antígenos vacunales.", "Potenciador inmune.")),
("37468460", "researcher", 2, "Immunostimulants are danger signal molecules that lead to the maturation and activation of antigen-presenting cells (APCs) by targeting Toll-like receptors",
 ("How do immunostimulant adjuvants work?", ["They neutralize toxins directly", "They replace antibodies", "They act as danger signals on TLRs/PRRs, activating antigen-presenting cells", "They kill T cells"],
  "Immunostimulants trigger pattern-recognition receptors, maturing APCs and providing co-stimulation for adaptive responses.", "Danger signals on PRRs."),
 ("¿Cómo actúan los adyuvantes inmunoestimulantes?", ["Neutralizan toxinas directamente", "Reemplazan anticuerpos", "Actúan como señales de peligro sobre TLR/PRR y activan células presentadoras", "Matan linfocitos T"],
  "Los inmunoestimulantes activan receptores de reconocimiento de patrones, maduran las CPA y aportan coestimulación.", "Señales de peligro.")),

# --- Checkpoint inhibitors (35621637)
("35621637", "explorer", 0, "The discovery of immune checkpoint proteins such as PD-1/PDL-1 and CTLA-4",
 ("Which molecules are targeted by immune checkpoint inhibitors?", ["PD-1/PD-L1 and CTLA-4", "Insulin and glucagon", "CD4 and CD8", "IgE and FcεRI"],
  "Checkpoint inhibitors block PD-1/PD-L1 or CTLA-4, releasing brakes on anti-tumor T cells.", "PD-1/PD-L1 and CTLA-4."),
 ("¿Qué moléculas bloquean los inhibidores de puntos de control inmunitario?", ["PD-1/PD-L1 y CTLA-4", "Insulina y glucagón", "CD4 y CD8", "IgE y FcεRI"],
  "Los inhibidores de checkpoint bloquean PD-1/PD-L1 o CTLA-4 y liberan los frenos de los linfocitos T antitumorales.", "PD-1/PD-L1 y CTLA-4.")),
("35621637", "expert", 3, "CTLA-4 inhibitor (Ipilimumab)",
 ("Ipilimumab blocks which immune checkpoint?", ["PD-1", "PD-L1", "LAG-3", "CTLA-4"],
  "Ipilimumab targets CTLA-4; nivolumab and pembrolizumab target PD-1; atezolizumab targets PD-L1.", "CTLA-4."),
 ("¿Qué punto de control bloquea el ipilimumab?", ["PD-1", "PD-L1", "LAG-3", "CTLA-4"],
  "El ipilimumab bloquea CTLA-4; nivolumab y pembrolizumab, PD-1; atezolizumab, PD-L1.", "CTLA-4.")),

# --- CAR-T (33824268)
("33824268", "explorer", 2, "certain subsets of B cell leukemia or lymphoma",
 ("In which cancers has CAR-T cell therapy produced its most remarkable responses?", ["Solid tumors of the pancreas", "Skin melanoma only", "Certain B-cell leukemias and lymphomas", "Brain tumors"],
  "CAR-T cells have shown remarkable responses in B-cell leukemia/lymphoma; solid tumors remain challenging.", "B-cell malignancies."),
 ("¿En qué cánceres la terapia CAR-T logró las respuestas más notables?", ["Tumores sólidos de páncreas", "Solo melanoma", "Ciertas leucemias y linfomas de células B", "Tumores cerebrales"],
  "Las CAR-T mostraron respuestas notables en leucemias/linfomas B; los tumores sólidos siguen siendo un desafío.", "Neoplasias B.")),
("33824268", "researcher", 1, "antigen escape",
 ("Which is a recognized mechanism of CAR-T therapy failure?", ["Excess antibodies", "Antigen escape (loss of the targeted antigen)", "Too much complement", "Low red cell count"],
  "Barriers include toxicities, antigen escape, poor trafficking and limited tumor infiltration.", "Antigen escape."),
 ("¿Cuál es un mecanismo reconocido de fracaso de la terapia CAR-T?", ["Exceso de anticuerpos", "Escape antigénico (pérdida del antígeno blanco)", "Exceso de complemento", "Anemia"],
  "Entre las barreras están la toxicidad, el escape antigénico, el mal tráfico celular y la escasa infiltración tumoral.", "Escape antigénico.")),

# --- CRS (29907163)
("29907163", "researcher", 3, "most notably the cytokine release syndrome (CRS)",
 ("What is the most notable potentially fatal adverse effect of T-cell–engaging immunotherapies such as CAR-T?", ["Hair loss", "Hypoglycemia", "Kidney stones", "Cytokine release syndrome"],
  "CAR-T cells and bispecific T-cell engagers can trigger cytokine release syndrome, a potentially fatal systemic inflammation.", "Cytokine release syndrome."),
 ("¿Cuál es el efecto adverso potencialmente mortal más notable de las inmunoterapias que activan linfocitos T, como CAR-T?", ["Caída del pelo", "Hipoglucemia", "Cálculos renales", "Síndrome de liberación de citocinas"],
  "Las CAR-T y los anticuerpos biespecíficos pueden desencadenar síndrome de liberación de citocinas, una inflamación sistémica potencialmente mortal.", "SLC.")),

# --- Tregs (18510923)
("18510923", "explorer", 1, "Regulatory T cells (Tregs) play an indispensable role in maintaining immunological unresponsiveness to self-antigens",
 ("What is the main role of regulatory T cells (Tregs)?", ["Producing antibodies", "Maintaining tolerance to self and suppressing excessive responses", "Killing virus-infected cells", "Phagocytosing bacteria"],
  "Tregs maintain self-tolerance and restrain harmful immune responses; their dysfunction contributes to immune disease.", "Self-tolerance."),
 ("¿Cuál es la función principal de los linfocitos T reguladores (Treg)?", ["Producir anticuerpos", "Mantener la tolerancia a lo propio y suprimir respuestas excesivas", "Matar células infectadas", "Fagocitar bacterias"],
  "Los Treg mantienen la autotolerancia y frenan respuestas dañinas; su disfunción contribuye a enfermedades inmunes.", "Autotolerancia.")),
("18510923", "expert", 0, "Tregs are produced in the thymus as a functionally mature subpopulation of T cells and can also be induced from naive T cells in the periphery",
 ("Where do regulatory T cells originate?", ["In the thymus, and also induced from naive T cells in the periphery", "Only in bone marrow from B cells", "Only from macrophages", "Only in lymph nodes from NK cells"],
  "Tregs arise in the thymus (thymic Tregs) and can be induced from naive peripheral T cells (peripheral Tregs).", "Thymus and periphery."),
 ("¿Dónde se originan los linfocitos T reguladores?", ["En el timo, y también inducidos a partir de T vírgenes en la periferia", "Solo en médula ósea a partir de B", "Solo de macrófagos", "Solo en ganglios a partir de NK"],
  "Los Treg surgen en el timo (Treg tímicos) y pueden inducirse desde T vírgenes periféricos (Treg periféricos).", "Timo y periferia.")),

# --- Th17 (19132915)
("19132915", "researcher", 2, "Th17 cells produce IL-17, IL-17F, and IL-22, thereby inducing a massive tissue reaction",
 ("Which cytokines characterize Th17 cells?", ["IFN-γ and IL-2", "IL-4 and IL-13", "IL-17, IL-17F and IL-22", "IL-10 and TGF-β only"],
  "Th17 cells secrete IL-17, IL-17F and IL-22, driving tissue inflammation and defense against extracellular pathogens.", "IL-17 and IL-22."),
 ("¿Qué citocinas caracterizan a los linfocitos Th17?", ["IFN-γ e IL-2", "IL-4 e IL-13", "IL-17, IL-17F e IL-22", "Solo IL-10 y TGF-β"],
  "Los Th17 secretan IL-17, IL-17F e IL-22 e impulsan inflamación tisular y defensa contra patógenos extracelulares.", "IL-17 e IL-22.")),
("19132915", "expert", 3, "the transcription factors (STAT3, RORgammat, and RORalpha) involved in the development of Th17 cells",
 ("Which transcription factor is the master regulator of Th17 differentiation?", ["T-bet", "GATA3", "Foxp3", "RORγt"],
  "Th17 development depends on STAT3 and RORγt/RORα; T-bet drives Th1, GATA3 Th2 and Foxp3 Tregs.", "RORγt."),
 ("¿Qué factor de transcripción es el regulador maestro de la diferenciación Th17?", ["T-bet", "GATA3", "Foxp3", "RORγt"],
  "El desarrollo Th17 depende de STAT3 y RORγt/RORα; T-bet dirige Th1, GATA3 Th2 y Foxp3 los Treg.", "RORγt.")),

# --- TLRs (20404851)
("20404851", "explorer", 0, "Toll-like receptors (TLRs) as components that recognize conserved structures in pathogens",
 ("What do Toll-like receptors recognize?", ["Conserved structures shared by pathogens", "Only self-antigens", "Specific peptides on MHC", "Antibodies"],
  "TLRs are pattern-recognition receptors sensing conserved microbial structures, triggering innate responses and priming adaptive immunity.", "Conserved pathogen structures."),
 ("¿Qué reconocen los receptores tipo Toll (TLR)?", ["Estructuras conservadas compartidas por patógenos", "Solo antígenos propios", "Péptidos específicos en MHC", "Anticuerpos"],
  "Los TLR son receptores de reconocimiento de patrones que detectan estructuras microbianas conservadas y activan la inmunidad innata.", "Estructuras conservadas.")),
("20404851", "expert", 2, "recognition of self molecules by TLRs, are strongly associated with the pathogenesis of inflammatory and autoimmune diseases",
 ("How can Toll-like receptors contribute to autoimmune disease?", ["By producing autoantibodies themselves", "By destroying the thymus", "Through loss of negative regulation and recognition of self molecules", "By blocking complement"],
  "Unchecked TLR signaling and TLR recognition of self molecules (e.g., self nucleic acids) are linked to inflammatory and autoimmune diseases.", "Self recognition, poor regulation."),
 ("¿Cómo pueden contribuir los TLR a enfermedades autoinmunes?", ["Produciendo autoanticuerpos", "Destruyendo el timo", "Por pérdida de regulación negativa y reconocimiento de moléculas propias", "Bloqueando el complemento"],
  "La señalización TLR sin control y el reconocimiento de moléculas propias (p. ej., ácidos nucleicos) se asocian a enfermedades inflamatorias y autoinmunes.", "Reconocimiento de lo propio.")),

# --- Inflammasome (26549800)
("26549800", "researcher", 1, "Inflammasomes are multi-protein signaling complexes that trigger the activation of inflammatory caspases and the maturation of interleukin-1β",
 ("What do inflammasomes do?", ["Present antigens on MHC II", "Activate inflammatory caspases and mature interleukin-1β", "Produce antibodies", "Build the cell wall"],
  "Inflammasomes (e.g., NLRP3) activate caspase-1, which matures IL-1β; dysregulation drives autoinflammatory disease.", "Caspases and IL-1β."),
 ("¿Qué hacen los inflamasomas?", ["Presentan antígenos en MHC II", "Activan caspasas inflamatorias y maduran la interleucina-1β", "Producen anticuerpos", "Construyen la pared celular"],
  "Los inflamasomas (p. ej., NLRP3) activan caspasa-1, que madura la IL-1β; su desregulación causa enfermedades autoinflamatorias.", "Caspasas e IL-1β.")),

# --- Trained immunity (32132681)
("32132681", "researcher", 3, "This process has been termed 'trained immunity', a de facto innate immune memory",
 ("What is 'trained immunity'?", ["Antibody memory after vaccination", "Thymic selection of T cells", "Allergic sensitization", "A form of memory in the innate immune system"],
  "Trained immunity is enhanced innate responsiveness after a prior stimulus, driven by epigenetic and metabolic reprogramming.", "Innate immune memory."),
 ("¿Qué es la 'inmunidad entrenada'?", ["Memoria de anticuerpos tras vacunar", "Selección tímica de linfocitos T", "Sensibilización alérgica", "Una forma de memoria del sistema inmune innato"],
  "La inmunidad entrenada es una mayor respuesta innata tras un estímulo previo, por reprogramación epigenética y metabólica.", "Memoria innata.")),

# --- SIgA (21975936)
("21975936", "explorer", 1, "Through a process known as immune exclusion, SIgA promotes the clearance of antigens and pathogenic microorganisms from the intestinal lumen",
 ("What is 'immune exclusion' by secretory IgA?", ["Killing bacteria with complement", "Blocking pathogens' access to the epithelium and clearing them from the lumen", "Destroying gut epithelial cells", "Activating mast cells"],
  "SIgA blocks epithelial receptors, traps microbes in mucus and helps remove them by peristalsis — without inflammation.", "Blocks and clears pathogens."),
 ("¿Qué es la 'exclusión inmune' por IgA secretora?", ["Matar bacterias con complemento", "Impedir el acceso de patógenos al epitelio y eliminarlos de la luz", "Destruir el epitelio intestinal", "Activar mastocitos"],
  "La IgAs bloquea receptores epiteliales, atrapa microbios en el moco y ayuda a eliminarlos por peristalsis, sin inflamación.", "Bloquea y elimina.")),

# --- GC B cells (34380063)
("34380063", "researcher", 0, "The unique biology of GC B cells involves iterative rounds of antibody gene somatic hypermutation coupled to multiple selection",
 ("Which process in germinal centers increases antibody affinity?", ["Somatic hypermutation with selection", "V(D)J recombination in the bone marrow", "Complement fixation", "Thymic negative selection"],
  "GC B cells undergo repeated somatic hypermutation and selection, producing high-affinity, class-switched antibodies.", "Somatic hypermutation."),
 ("¿Qué proceso de los centros germinales aumenta la afinidad de los anticuerpos?", ["Hipermutación somática con selección", "Recombinación V(D)J en la médula", "Fijación del complemento", "Selección negativa tímica"],
  "Los B del centro germinal pasan por rondas de hipermutación somática y selección, generando anticuerpos de alta afinidad.", "Hipermutación somática.")),

# --- Trm (25526304)
("25526304", "expert", 2, "Tissue-resident memory T (Trm) cells constitute a recently identified lymphocyte lineage that occupies tissues without recirculating",
 ("What distinguishes tissue-resident memory T cells?", ["They circulate constantly in blood", "They are B cells", "They stay in tissues without recirculating, giving rapid local protection", "They only live in the thymus"],
  "Trm cells remain in tissues at body surfaces, accelerating pathogen clearance on re-exposure; they're absent from blood.", "Non-recirculating, in tissues."),
 ("¿Qué distingue a los linfocitos T de memoria residentes en tejido?", ["Circulan siempre por la sangre", "Son linfocitos B", "Permanecen en los tejidos sin recircular y dan protección local rápida", "Solo viven en el timo"],
  "Los Trm permanecen en tejidos de superficie y aceleran la eliminación del patógeno en la reexposición; no están en sangre.", "No recirculan.")),

# --- DCs (32433540)
("32433540", "explorer", 3, "Dendritic cells are powerful antigen-presenting cells that are essential for the priming of T cell responses",
 ("Which cells are essential for priming naive T-cell responses?", ["Red blood cells", "Platelets", "Plasma cells", "Dendritic cells"],
  "Dendritic cells present antigen with co-stimulatory signals and instruct CD4+ T-cell differentiation.", "Dendritic cells."),
 ("¿Qué células son esenciales para activar (cebar) respuestas de linfocitos T vírgenes?", ["Glóbulos rojos", "Plaquetas", "Células plasmáticas", "Células dendríticas"],
  "Las células dendríticas presentan antígeno con señales coestimuladoras e instruyen la diferenciación de los T CD4+.", "Células dendríticas.")),

# --- Transplant rejection (31747169)
("31747169", "curious", 0, "Hyperacute rejection occurs within minutes of transplantation and is caused by preformed donor-specific antibodies",
 ("What causes hyperacute transplant rejection?", ["Preformed donor-specific antibodies", "Slow T-cell infiltration over years", "Drug toxicity", "Viral infection"],
  "Hyperacute rejection happens within minutes due to preformed antibodies against the donor (e.g., ABO or HLA).", "Preformed antibodies."),
 ("¿Qué causa el rechazo hiperagudo de un trasplante?", ["Anticuerpos preformados contra el donante", "Infiltración lenta de linfocitos T durante años", "Toxicidad de fármacos", "Infección viral"],
  "El rechazo hiperagudo ocurre en minutos por anticuerpos preformados contra el donante (p. ej., ABO o HLA).", "Anticuerpos preformados.")),
("31747169", "researcher", 2, "Acute rejection occurs within one year and can be T-cell or antibody-mediated",
 ("Which statement about acute kidney transplant rejection is correct?", ["It only occurs after 10 years", "It is always caused by viruses", "It occurs within the first year and can be T-cell or antibody-mediated", "It cannot be treated"],
  "Rejection types: hyperacute (minutes), accelerated, acute (<1 year; T-cell or antibody-mediated) and chronic (>1 year).", "Within 1 year; T or antibody."),
 ("¿Qué afirmación sobre el rechazo agudo del trasplante renal es correcta?", ["Ocurre recién a los 10 años", "Siempre lo causan virus", "Ocurre en el primer año y puede ser mediado por T o por anticuerpos", "No tiene tratamiento"],
  "Tipos: hiperagudo (minutos), acelerado, agudo (<1 año; celular o humoral) y crónico (>1 año).", "<1 año; T o anticuerpos.")),

# --- Graves (28846288)
("28846288", "curious", 3, "It is the most common cause of hyperthyroidism",
 ("What is the most common cause of hyperthyroidism?", ["Thyroid cancer", "Iodine deficiency", "Hashimoto thyroiditis", "Graves disease"],
  "Graves disease, an autoimmune disorder (TSH-receptor stimulating antibodies), is the most common cause of hyperthyroidism.", "Graves disease."),
 ("¿Cuál es la causa más común de hipertiroidismo?", ["Cáncer de tiroides", "Déficit de yodo", "Tiroiditis de Hashimoto", "Enfermedad de Graves"],
  "La enfermedad de Graves, autoinmune (anticuerpos estimulantes del receptor de TSH), es la causa más común de hipertiroidismo.", "Graves.")),

# --- Hashimoto (29083758)
("29083758", "explorer", 1, "Hashimoto thyroiditis is the most common cause of hypothyroidism in developed countries",
 ("What is the most common cause of hypothyroidism in developed countries?", ["Graves disease", "Hashimoto (autoimmune) thyroiditis", "Thyroid surgery", "Pituitary tumor"],
  "Hashimoto thyroiditis destroys follicular cells through antibody- and cell-mediated autoimmunity.", "Hashimoto thyroiditis."),
 ("¿Cuál es la causa más común de hipotiroidismo en países desarrollados?", ["Enfermedad de Graves", "Tiroiditis de Hashimoto (autoinmune)", "Cirugía tiroidea", "Tumor hipofisario"],
  "La tiroiditis de Hashimoto destruye células foliculares por autoinmunidad celular y humoral.", "Hashimoto.")),

# --- T1D (29939535)
("29939535", "curious", 2, "Type 1 diabetes (T1D) is a condition characterized by the immune-mediated destruction of insulin-producing pancreatic β-cells",
 ("What causes type 1 diabetes?", ["Insulin resistance from obesity", "A viral infection of the liver", "Immune-mediated destruction of pancreatic β-cells", "Excess dietary sugar"],
  "T1D results from autoimmune destruction of insulin-producing β-cells, causing absolute insulin deficiency.", "Autoimmune β-cell destruction."),
 ("¿Qué causa la diabetes tipo 1?", ["Resistencia a la insulina por obesidad", "Una infección viral del hígado", "La destrucción inmunomediada de las células β del páncreas", "El exceso de azúcar en la dieta"],
  "La DT1 se debe a la destrucción autoinmune de las células β productoras de insulina, con déficit absoluto de insulina.", "Destrucción autoinmune de células β.")),
("29939535", "expert", 0, "Individuals with multiple T1D-related autoantibodies eventually develop clinical disease",
 ("What does having multiple type 1 diabetes–related autoantibodies predict?", ["Eventual clinical type 1 diabetes", "Protection from diabetes", "Type 2 diabetes only", "Nothing; they are irrelevant"],
  "People with multiple islet autoantibodies eventually develop clinical T1D, which is why at-risk relatives are screened.", "Eventual T1D."),
 ("¿Qué predice tener múltiples autoanticuerpos relacionados con la diabetes tipo 1?", ["El desarrollo eventual de diabetes tipo 1 clínica", "Protección contra la diabetes", "Solo diabetes tipo 2", "Nada; son irrelevantes"],
  "Quienes tienen múltiples autoanticuerpos contra islotes terminan desarrollando DT1 clínica; por eso se tamiza a familiares.", "DT1 eventual.")),

# --- MS (29763024)
("29763024", "explorer", 3, "Multiple sclerosis is a chronic autoimmune disease affecting the central nervous system (CNS) and is characterized by inflammation, demyelination",
 ("What characterizes multiple sclerosis?", ["Muscle fiber necrosis", "Joint cartilage destruction", "Peripheral nerve infection", "Autoimmune CNS inflammation with demyelination"],
  "MS is an autoimmune CNS disease with inflammation, demyelination, gliosis and neuronal loss.", "CNS demyelination."),
 ("¿Qué caracteriza a la esclerosis múltiple?", ["Necrosis de fibras musculares", "Destrucción del cartílago articular", "Infección de nervios periféricos", "Inflamación autoinmune del SNC con desmielinización"],
  "La EM es una enfermedad autoinmune del SNC con inflamación, desmielinización, gliosis y pérdida neuronal.", "Desmielinización del SNC.")),
("29763024", "researcher", 1, "Relapsing-remitting (RR): This initial onset is observed in 70% to 80% of multiple sclerosis patients",
 ("Which is the most common initial course of multiple sclerosis?", ["Primary progressive", "Relapsing-remitting", "Fulminant", "Progressive-relapsing"],
  "Relapsing-remitting MS is the initial course in 70–80% of patients; primary progressive in 15–20%.", "Relapsing-remitting."),
 ("¿Cuál es el curso inicial más frecuente de la esclerosis múltiple?", ["Primaria progresiva", "Recurrente-remitente", "Fulminante", "Progresiva-recurrente"],
  "La forma recurrente-remitente es el curso inicial en el 70–80%; la primaria progresiva en el 15–20%.", "Recurrente-remitente.")),

# --- Sarcoidosis (28613460)
("28613460", "explorer", 2, "Sarcoidosis is a multisystem granulomatous disorder of unknown etiology that primarily affects the lungs and lymphoid organs",
 ("What is sarcoidosis?", ["A bacterial pneumonia", "An IgE-mediated allergy", "A multisystem granulomatous disease of unknown cause, mainly lungs and lymph nodes", "A viral hepatitis"],
  "Sarcoidosis forms non-caseating granulomas, mainly in lungs and lymphoid organs; histopathology is the diagnostic gold standard.", "Granulomatous, unknown cause."),
 ("¿Qué es la sarcoidosis?", ["Una neumonía bacteriana", "Una alergia mediada por IgE", "Una enfermedad granulomatosa multisistémica de causa desconocida, sobre todo pulmonar y ganglionar", "Una hepatitis viral"],
  "La sarcoidosis forma granulomas no caseificantes, sobre todo en pulmón y órganos linfoides; la histopatología es el estándar diagnóstico.", "Granulomatosa, causa desconocida.")),

# --- Atopic dermatitis (28846349)
("28846349", "curious", 0, "The condition is believed to coexist with other immunoglobulin E (IgE)–associated disorders, including allergic rhinitis, asthma, and food allergies",
 ("Atopic dermatitis frequently coexists with which conditions?", ["Allergic rhinitis, asthma and food allergies", "Type 1 diabetes and lupus", "Gout and arthritis", "Tuberculosis and HIV"],
  "Atopic dermatitis belongs to the IgE-associated 'atopic' diseases with allergic rhinitis, asthma and food allergy.", "Other atopic diseases."),
 ("¿Con qué condiciones coexiste a menudo la dermatitis atópica?", ["Rinitis alérgica, asma y alergias alimentarias", "Diabetes tipo 1 y lupus", "Gota y artritis", "Tuberculosis y VIH"],
  "La dermatitis atópica pertenece a las enfermedades 'atópicas' asociadas a IgE, junto con rinitis alérgica, asma y alergia alimentaria.", "Otras atopías.")),

# --- Penicillin allergy (29083777)
("29083777", "explorer", 3, "Penicillin allergy is the most commonly reported medication allergy, affecting approximately 8% to 10% of patients in the United States. However, the prevalence of true IgE-mediated hypersensitivity is much lower",
 ("Why is 'delabeling' penicillin allergy important?", ["Penicillin is no longer used", "All allergic people have anaphylaxis", "Penicillin allergy is always genetic", "Most reported allergies are not true IgE allergy; wrong labels drive broad-spectrum use"],
  "8–10% report penicillin allergy but true IgE allergy is far rarer; inaccurate labels push broad-spectrum antibiotics and resistance.", "Most labels are wrong."),
 ("¿Por qué es importante revisar ('desetiquetar') la alergia a la penicilina?", ["Ya no se usa penicilina", "Todo alérgico hace anafilaxia", "La alergia siempre es genética", "La mayoría de las alergias reportadas no son IgE verdaderas; etiquetas erróneas llevan a usar amplio espectro"],
  "El 8–10% refiere alergia pero la alergia IgE verdadera es mucho menor; las etiquetas erróneas fomentan antibióticos de amplio espectro y resistencia.", "Etiquetas erróneas.")),
("29083777", "expert", 1, "most will develop tolerance to penicillin after a decade",
 ("What usually happens over time to confirmed IgE-mediated penicillin allergy?", ["It always worsens", "Most patients lose it (become tolerant) after about a decade", "It becomes a T-cell allergy", "It spreads to all drugs"],
  "Even confirmed IgE-mediated penicillin allergy wanes: most patients tolerate penicillin after about 10 years.", "Wanes in ~10 years."),
 ("¿Qué suele pasar con el tiempo con la alergia IgE a penicilina confirmada?", ["Siempre empeora", "La mayoría la pierde (se vuelve tolerante) en unos diez años", "Se convierte en alergia T", "Se extiende a todos los fármacos"],
  "Incluso la alergia IgE confirmada se atenúa: la mayoría tolera penicilina después de unos 10 años.", "Se atenúa en ~10 años.")),

# --- Asthma (28613651)
("28613651", "curious", 1, "This respiratory condition is characterized by inflammation of the airways, causing intermittent airflow obstruction and bronchial hyperresponsiveness",
 ("What characterizes asthma?", ["Permanent destruction of alveoli", "Airway inflammation with intermittent obstruction and hyperresponsiveness", "Bacterial infection of the pleura", "Blood clots in the lungs"],
  "Asthma is chronic airway inflammation with intermittent, reversible obstruction and bronchial hyperresponsiveness.", "Inflammation, reversible obstruction."),
 ("¿Qué caracteriza al asma?", ["Destrucción permanente de alvéolos", "Inflamación de la vía aérea con obstrucción intermitente e hiperreactividad", "Infección bacteriana de la pleura", "Coágulos en los pulmones"],
  "El asma es una inflamación crónica de la vía aérea con obstrucción intermitente y reversible e hiperreactividad bronquial.", "Inflamación y obstrucción reversible.")),

# --- IgA deficiency (30855793)
("30855793", "explorer", 0, "Immunoglobulin A (IgA) deficiency is the most common primary immunodeficiency",
 ("What is the most common primary immunodeficiency overall?", ["Selective IgA deficiency", "SCID", "X-linked agammaglobulinemia", "Chronic granulomatous disease"],
  "Selective IgA deficiency is the most common primary immunodeficiency; most patients are asymptomatic (CVID is the most common symptomatic one).", "Selective IgA deficiency."),
 ("¿Cuál es la inmunodeficiencia primaria más común en general?", ["Déficit selectivo de IgA", "IDCG", "Agammaglobulinemia ligada al X", "Enfermedad granulomatosa crónica"],
  "El déficit selectivo de IgA es la inmunodeficiencia primaria más común; la mayoría es asintomática (la IDCV es la sintomática más común).", "Déficit selectivo de IgA.")),
("30855793", "researcher", 3, "Since IgG and IgE anti-IgA antibodies may cause transfusion reactions if given whole blood, they should be administered IgA poor or washed red cells",
 ("What transfusion precaution applies to some patients with selective IgA deficiency?", ["Only O-negative blood", "Double-volume transfusions", "Adding IgA to the bag", "Using IgA-poor or washed red cells because anti-IgA antibodies can cause reactions"],
  "Anti-IgA antibodies can trigger transfusion reactions; IgA-poor or washed red cells are used.", "IgA-poor/washed products."),
 ("¿Qué precaución transfusional aplica a algunos pacientes con déficit selectivo de IgA?", ["Solo sangre O negativo", "Transfusiones de doble volumen", "Agregar IgA a la bolsa", "Usar glóbulos rojos lavados o pobres en IgA, porque los anticuerpos anti-IgA pueden causar reacciones"],
  "Los anticuerpos anti-IgA pueden desencadenar reacciones transfusionales; se usan productos lavados o pobres en IgA.", "Productos lavados o pobres en IgA.")),

# --- HLH (32491708)
("32491708", "expert", 2, "inappropriate, deregulated activation and proliferation of natural killer (NK) cells, CD8+ cytotoxic T-cells, and macrophages",
 ("What drives hemophagocytic lymphohistiocytosis (HLH)?", ["IgE-mediated mast cell release", "Complement deficiency", "Deregulated activation of NK cells, CD8+ T cells and macrophages", "Bacterial toxins only"],
  "HLH is a hyperinflammatory syndrome from uncontrolled NK, CD8+ T-cell and macrophage activation; primary (genetic) or secondary.", "Uncontrolled NK/CD8/macrophage activation."),
 ("¿Qué impulsa la linfohistiocitosis hemofagocítica (LHH)?", ["Liberación de mastocitos mediada por IgE", "Déficit de complemento", "Activación desregulada de NK, linfocitos T CD8+ y macrófagos", "Solo toxinas bacterianas"],
  "La LHH es un síndrome hiperinflamatorio por activación descontrolada de NK, T CD8+ y macrófagos; primaria (genética) o secundaria.", "Activación descontrolada.")),
]
