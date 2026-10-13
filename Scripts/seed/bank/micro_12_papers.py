# Microbiology XII — microbial ecology and physiology papers: NDM-1 and KPC carbapenemases, Candida auris
# origins, Wolbachia against dengue, quorum sensing and biofilms (lasI, AI-2), phage therapy cases, CRISPR
# as bacterial immunity and anti-CRISPRs, landmark gut microbiome studies, fecal transplant, ancient
# resistance genes, Thermus aquaticus, persister dormancy.
# Sources: PubMed paper and review abstracts. Excerpts verbatim.
CATEGORY = "microbiology"
Q = [
# --- NDM-1 in India, Pakistan and the UK (20705517)
("20705517", "explorer", 0, "NDM-1 was mostly found among Escherichia coli (36) and Klebsiella pneumoniae (111)",
 ("In the 2010 Lancet Infectious Diseases study of NDM-1 in India, Pakistan and the UK, which bacteria most often carried the gene?", ["E. coli and Klebsiella pneumoniae", "Pseudomonas and Acinetobacter", "Salmonella and Shigella species", "Enterobacter and Serratia species"],
  "Of the NDM-1 isolates, 111 were K. pneumoniae and 36 were E. coli.", "E. coli and K. pneumoniae."),
 ("En el estudio de 2010 en Lancet Infectious Diseases sobre NDM-1 en India, Pakistán y Reino Unido, ¿qué bacterias portaban el gen con más frecuencia?", ["E. coli y Klebsiella pneumoniae", "Pseudomonas y Acinetobacter", "Especies de Salmonella y Shigella", "Especies de Enterobacter y Serratia"],
  "De los aislamientos con NDM-1, 111 eran K. pneumoniae y 36 eran E. coli.", "E. coli y K. pneumoniae.")),
("20705517", "curious", 1, "Many of the UK NDM-1 positive patients had travelled to India or Pakistan within the past year",
 ("What link did many UK patients with NDM-1 bacteria share, according to the 2010 NDM-1 study?", ["Recent dental surgery in London", "Travel to India or Pakistan", "Work on pig and poultry farms", "Eating imported raw seafood"],
  "Many UK cases had travelled to India or Pakistan in the past year or had links with these countries.", "Travel to South Asia."),
 ("Según el estudio de 2010 sobre NDM-1, ¿qué vínculo compartían muchos pacientes británicos con bacterias NDM-1?", ["Cirugía dental en Londres", "Viajes a India o Pakistán", "Trabajo en granjas de cerdos", "Consumo de mariscos crudos"],
  "Muchos casos británicos habían viajado a India o Pakistán en el último año o tenían vínculos con esos países.", "Viajes al sur de Asia.")),
("20705517", "researcher", 2, "which were highly resistant to all antibiotics except to tigecycline and colistin",
 ("In the 2010 NDM-1 survey, which antibiotics still retained activity against most NDM-1 producers?", ["Meropenem and imipenem", "Ciprofloxacin and amikacin", "Tigecycline and colistin", "Ceftriaxone and aztreonam"],
  "NDM-1 isolates were resistant to everything except tigecycline and colistin.", "Tigecycline and colistin."),
 ("En el relevamiento de 2010 sobre NDM-1, ¿qué antibióticos conservaban actividad frente a la mayoría de los productores de NDM-1?", ["Meropenem e imipenem", "Ciprofloxacina y amikacina", "Tigeciclina y colistina", "Ceftriaxona y aztreonam"],
  "Los aislamientos con NDM-1 resistían todo salvo tigeciclina y colistina.", "Tigeciclina y colistina.")),

# --- First description of NDM-1 (19770275)
("19770275", "explorer", 3, "A Swedish patient of Indian origin traveled to New Delhi, India, and acquired a urinary tract infection caused by a carbapenem-resistant Klebsiella pneumoniae",
 ("The first described NDM-1 gene came from a Klebsiella isolate from which patient?", ["A Danish child with meningitis", "A British soldier with a wound", "An Indian farmer with pneumonia", "A Swedish traveler with a UTI"],
  "A Swedish patient of Indian origin got a carbapenem-resistant K. pneumoniae urinary infection after visiting New Delhi.", "A Swedish traveler."),
 ("El primer gen NDM-1 descrito provino de un aislamiento de Klebsiella de ¿qué paciente?", ["Un niño danés con meningitis", "Un soldado británico herido en combate", "Un agricultor indio con neumonía", "Un viajero sueco con cistitis"],
  "Un paciente sueco de origen indio contrajo una infección urinaria por K. pneumoniae resistente a carbapenémicos tras visitar Nueva Delhi.", "Un viajero sueco.")),
("19770275", "researcher", 0, "can hydrolyze all beta-lactams except aztreonam",
 ("Which beta-lactam was NOT hydrolyzed by the newly described NDM-1 metallo-beta-lactamase?", ["Aztreonam", "Meropenem", "Cefotaxime", "Penicillin G"],
  "NDM-1 hydrolyzed all beta-lactams except the monobactam aztreonam.", "Aztreonam."),
 ("¿Qué betalactámico NO era hidrolizado por la recién descrita metalo-betalactamasa NDM-1?", ["Aztreonam", "Meropenem", "Cefotaxima", "Penicilina G"],
  "NDM-1 hidrolizaba todos los betalactámicos excepto el monobactámico aztreonam.", "Aztreonam.")),
("19770275", "expert", 1, "the most similar MBLs being VIM-1/VIM-2, with which it has only 32.4% identity",
 ("How similar was NDM-1 to its closest known metallo-beta-lactamases, VIM-1/VIM-2?", ["About 90% identity", "Only 32.4% identity", "Exactly 50% identity", "About 75% identity"],
  "NDM-1 shared very little identity with other MBLs; the closest, VIM-1/VIM-2, were only 32.4% identical.", "32.4% identity."),
 ("¿Qué tan parecida era NDM-1 a sus metalo-betalactamasas conocidas más cercanas, VIM-1/VIM-2?", ["Cerca de 90% de identidad", "Solo 32,4% de identidad", "Exactamente 50% de identidad", "Cerca de 75% de identidad"],
  "NDM-1 compartía muy poca identidad con otras MBL; las más cercanas, VIM-1/VIM-2, eran solo 32,4% idénticas.", "32,4% de identidad.")),

# --- KPC-1 discovery (11257029)
("11257029", "researcher", 2, "The kinetic studies also revealed that clavulanic acid and tazobactam inhibited KPC-1",
 ("Which inhibitors blocked the novel carbapenemase KPC-1 from Klebsiella pneumoniae in its first description?", ["EDTA and other metal chelators", "Only boronic acid derivatives", "Clavulanic acid and tazobactam", "None of the tested compounds"],
  "KPC-1, a class A enzyme, was inhibited by clavulanic acid and tazobactam.", "Clavulanate and tazobactam."),
 ("En su primera descripción, ¿qué inhibidores bloqueaban la nueva carbapenemasa KPC-1 de Klebsiella pneumoniae?", ["EDTA y otros quelantes de metales", "Solo derivados del ácido borónico", "Ácido clavulánico y tazobactam", "Ninguno de los compuestos probados"],
  "KPC-1, una enzima de clase A, era inhibida por ácido clavulánico y tazobactam.", "Clavulánico y tazobactam.")),
("11257029", "expert", 3, "KPC-1 had the highest affinity for meropenem",
 ("For which drug did purified KPC-1 show the highest affinity?", ["Imipenem", "Aztreonam", "Ampicillin", "Meropenem"],
  "Although KPC-1 hydrolyzed many beta-lactams, its highest affinity was for meropenem.", "Meropenem."),
 ("¿Por qué fármaco mostró mayor afinidad la enzima KPC-1 purificada?", ["Imipenem", "Aztreonam", "Ampicilina", "Meropenem"],
  "Aunque KPC-1 hidrolizaba muchos betalactámicos, su mayor afinidad era por el meropenem.", "Meropenem.")),

# --- Candida auris sp. nov. (19161556)
("19161556", "explorer", 0, "isolated from the external ear canal of an inpatient in a Japanese hospital",
 ("Where was the first strain of Candida auris isolated, as described in 2009?", ["A patient's ear canal in Japan", "A bloodstream infection in India", "A hospital sink drain in the UK", "A soil sample in South Africa"],
  "The type strain came from the external ear canal of an inpatient in a Japanese hospital, hence the name auris.", "Ear canal, Japan."),
 ("¿Dónde se aisló la primera cepa de Candida auris, descrita en 2009?", ["Conducto auditivo de un paciente en Japón", "Una infección del torrente sanguíneo en India", "El desagüe de un lavabo hospitalario en Reino Unido", "Una muestra de suelo en Sudáfrica"],
  "La cepa tipo provino del conducto auditivo externo de un paciente internado en Japón; de ahí el nombre auris.", "Oído, Japón.")),
("19161556", "researcher", 1, "This strain grew well at 40 degrees C, but showed slow and weak growth at 42 degrees C",
 ("How did the original Candida auris strain behave at high temperatures?", ["It died above 30 °C", "It grew well at 40 °C", "It grew best at 50 °C", "It needed 37 °C exactly"],
  "The strain grew well at 40 °C but only slowly and weakly at 42 °C.", "Grew well at 40 °C."),
 ("¿Cómo se comportaba la cepa original de Candida auris a altas temperaturas?", ["Moría por encima de 30 °C", "Crecía bien a 40 °C", "Crecía mejor a 50 °C", "Requería 37 °C exactos"],
  "La cepa crecía bien a 40 °C, pero de forma lenta y débil a 42 °C.", "Crecía bien a 40 °C.")),

# --- C. auris clone in Delhi (24048006)
("24048006", "explorer", 2, "it was resistant to fluconazole and genotypically distinct from isolates from South Korea and Japan",
 ("What did the 2013 report of a new clonal Candida auris strain causing fungemia in Delhi find?", ["It was identical to Japanese isolates", "It was susceptible to all azoles", "It was resistant to fluconazole", "It infected only newborn babies"],
  "The Delhi clone resisted fluconazole and differed genetically from Korean and Japanese isolates.", "Fluconazole resistant."),
 ("¿Qué encontró el informe de 2013 sobre una nueva cepa clonal de Candida auris que causaba fungemia en Delhi?", ["Era idéntica a los aislamientos japoneses", "Era sensible a todos los azoles", "Era resistente al fluconazol", "Infectaba solo a recién nacidos"],
  "El clon de Delhi resistía al fluconazol y era genéticamente distinto de los aislamientos de Corea y Japón.", "Resistente al fluconazol.")),

# --- Wolbachia blocks pathogens in Aedes (20064373)
("20064373", "curious", 3, "estimated to infect more than 60% of all insect species",
 ("Wolbachia, the maternally inherited bacterial symbiont, is estimated to infect what share of insect species?", ["Fewer than 5%", "About 15%", "Roughly 30%", "More than 60%"],
  "Wolbachia is extremely common, infecting an estimated more than 60% of insect species.", "Over 60%."),
 ("Se estima que Wolbachia, el simbionte bacteriano de herencia materna, infecta ¿qué proporción de especies de insectos?", ["Menos del 5%", "Alrededor del 15%", "Cerca del 30%", "Más del 60%"],
  "Wolbachia es muy común: se estima que infecta a más del 60% de las especies de insectos.", "Más del 60%.")),
("20064373", "researcher", 0, "relates to Wolbachia priming of the mosquito innate immune system",
 ("According to the 2009 Cell study, how does Wolbachia in Aedes aegypti limit dengue, Chikungunya and Plasmodium?", ["By priming mosquito innate immunity", "By killing mosquito larvae in water", "By making mosquitoes avoid humans", "By producing antiviral antibiotics"],
  "Pathogen interference was linked to immune priming and possibly competition for cellular resources.", "Immune priming."),
 ("Según el estudio de 2009 en Cell, ¿cómo limita Wolbachia en Aedes aegypti el dengue, el chikunguña y Plasmodium?", ["Activando la inmunidad innata del mosquito", "Matando las larvas del mosquito en el agua", "Haciendo que el mosquito evite a las personas", "Produciendo antibióticos antivirales"],
  "La interferencia se asoció con la activación inmune y quizás con competencia por recursos celulares.", "Activación inmune.")),

# --- wMel invades caged Aedes and blocks dengue (21866159)
("21866159", "researcher", 1, "wMel and wMelPop-CLA strains block transmission of dengue serotype 2 (DENV-2) in A. aegypti",
 ("What did the 2011 Nature study show about the avirulent wMel Wolbachia strain in Aedes aegypti?", ["It increased mosquito lifespan", "It blocked DENV-2 transmission", "It made mosquitoes sterile", "It spread only in male insects"],
  "The wMel strain invaded caged populations and blocked transmission of dengue serotype 2.", "Blocked dengue."),
 ("¿Qué mostró el estudio de 2011 en Nature sobre la cepa avirulenta wMel de Wolbachia en Aedes aegypti?", ["Aumentaba la vida del mosquito", "Bloqueaba la transmisión del DENV-2", "Volvía estériles a los mosquitos", "Se esparcía solo en los machos"],
  "La cepa wMel invadía poblaciones enjauladas y bloqueaba la transmisión del dengue serotipo 2.", "Bloqueaba el dengue.")),

# --- wMel invades wild Aedes populations (21866160)
("21866160", "explorer", 2, "successfully invaded two natural A. aegypti populations in Australia, reaching near-fixation in a few months",
 ("What happened when wMel-infected Aedes aegypti were first released into wild populations in Australia (2011)?", ["The infection quickly died out", "Only lab mosquitoes kept it", "It spread to near-fixation", "It spread only after many years"],
  "wMel invaded two natural Australian A. aegypti populations, reaching near-fixation within months.", "Reached near-fixation."),
 ("¿Qué ocurrió cuando se liberaron por primera vez Aedes aegypti con wMel en poblaciones silvestres de Australia (2011)?", ["La infección se extinguió pronto", "Solo los mosquitos de laboratorio la mantuvieron", "Se extendió casi a fijación", "Se extendió solo tras muchos años"],
  "wMel invadió dos poblaciones silvestres australianas de A. aegypti, alcanzando casi la fijación en meses.", "Casi a fijación.")),

# --- Biofilm cell-to-cell signal, lasI (9535661)
("9535661", "researcher", 0, "a lasI mutant, forms flat, undifferentiated biofilms",
 ("In the 1998 Science study of Pseudomonas aeruginosa biofilms, how did a lasI signaling mutant differ from wild type?", ["It formed flat, undifferentiated biofilms", "It made thicker, tougher biofilms", "It could not attach to surfaces at all", "It grew only as free-swimming cells"],
  "The quorum-sensing lasI mutant formed flat, undifferentiated biofilms sensitive to the detergent SDS.", "Flat biofilms."),
 ("En el estudio de 1998 en Science sobre biopelículas de Pseudomonas aeruginosa, ¿en qué se diferenciaba un mutante de señalización lasI del silvestre?", ["Formaba biopelículas planas", "Hacía biopelículas más gruesas y duras", "No podía adherirse a ninguna superficie", "Crecía solo como células nadadoras"],
  "El mutante de quorum sensing lasI formaba biopelículas planas e indiferenciadas, sensibles al detergente SDS.", "Biopelículas planas.")),
("9535661", "curious", 1, "Bacteria in nature often exist as sessile communities called biofilms",
 ("What name is given to the sessile bacterial communities described in the 1998 Pseudomonas biofilm study?", ["Plasmids", "Biofilms", "Plaques", "Spores"],
  "Bacteria in nature often live in surface-attached communities called biofilms.", "Biofilms."),
 ("¿Qué nombre reciben las comunidades bacterianas sésiles descritas en el estudio de biopelículas de Pseudomonas de 1998?", ["Colonias flotantes", "Biopelículas", "Plásmidos víricos", "Esporas latentes"],
  "En la naturaleza, las bacterias suelen vivir en comunidades adheridas a superficies llamadas biopelículas.", "Biopelículas.")),

# --- AI-2 boron quorum signal (11823863)
("11823863", "expert", 2, "The bound ligand is a furanosyl borate diester",
 ("What was surprising about the structure of the universal quorum-sensing autoinducer AI-2 bound to LuxP?", ["It was a simple peptide", "It was a modified DNA base", "It contained boron", "It was identical to an acyl-HSL"],
  "AI-2 bound to LuxP was a furanosyl borate diester, showing a biological role for boron.", "It contained boron."),
 ("¿Qué resultó sorprendente en la estructura del autoinductor universal de quorum sensing AI-2 unido a LuxP?", ["Era un péptido", "Era una base de ADN", "Contenía boro", "Era una acil-HSL"],
  "El AI-2 unido a LuxP era un diéster de borato furanosilo, revelando un papel biológico del boro.", "Contenía boro.")),
("11823863", "explorer", 3, "a recently discovered autoinducer (AI-2) is produced by a large number of bacterial species",
 ("Why is AI-2 considered special among bacterial quorum-sensing signals?", ["It only works in Vibrio fischeri", "It is a protein toxin", "It requires no receptor at all", "It is made by many species"],
  "Unlike species-specific autoinducers, AI-2 is produced by many species and proposed as a universal inter-species signal.", "Made by many species."),
 ("¿Por qué se considera especial al AI-2 entre las señales de quorum sensing bacterianas?", ["Solo funciona en Vibrio fischeri", "Es una toxina proteica", "No necesita ningún receptor", "Lo producen muchas especies"],
  "A diferencia de los autoinductores específicos de especie, muchas especies producen AI-2, propuesto como señal universal entre especies.", "Lo hacen muchas especies.")),

# --- Phage therapy for Acinetobacter (28807909)
("28807909", "explorer", 0, "two laboratories identified nine different bacteriophages with lytic activity",
 ("In the 2017 personalized phage therapy case for a multidrug-resistant Acinetobacter baumannii infection, how were the phages obtained?", ["Nine lytic phages were identified", "A single engineered phage was used", "Phages came from the patient's gut", "An old antibiotic was repurposed"],
  "Two labs found nine lytic bacteriophages against the patient's A. baumannii isolate.", "Nine lytic phages."),
 ("En el caso de 2017 de fagoterapia personalizada para una infección por Acinetobacter baumannii multirresistente, ¿cómo se obtuvieron los fagos?", ["Se identificaron nueve fagos líticos", "Se usó un solo fago modificado", "Los fagos vinieron del intestino del paciente", "Se reutilizó un antibiótico viejo"],
  "Dos laboratorios hallaron nueve bacteriófagos líticos contra el aislamiento de A. baumannii del paciente.", "Nueve fagos líticos.")),

# --- Engineered phages for M. abscessus (31068712)
("31068712", "researcher", 1, "Effective lytic phage derivatives that efficiently kill the infectious M. abscessus strain were developed by genome engineering",
 ("How were the phages prepared for the 2019 case treating a disseminated Mycobacterium abscessus infection in a cystic fibrosis patient?", ["Isolated directly from sewage water", "Developed by genome engineering", "Purified from donor blood serum", "Grown inside the patient's lungs"],
  "Lytic phage derivatives that kill M. abscessus were made by genome engineering and forward genetics.", "Genome engineering."),
 ("¿Cómo se prepararon los fagos para el caso de 2019 que trató una infección diseminada por Mycobacterium abscessus en un paciente con fibrosis quística?", ["Aislados directo de aguas cloacales", "Desarrollados por ingeniería del genoma", "Purificados del suero sanguíneo de un donante", "Cultivados dentro de los pulmones del paciente"],
  "Se obtuvieron derivados de fagos líticos que matan M. abscessus mediante ingeniería del genoma y genética directa.", "Ingeniería del genoma.")),

# --- CRISPR interference limits HGT (19095942)
("19095942", "researcher", 2, "CRISPR interference prevents conjugation and plasmid transformation in S. epidermidis",
 ("What did the 2008 Science study show CRISPR loci can do in Staphylococcus epidermidis?", ["Speed up plasmid transfer", "Cause resistance", "Block gene transfer", "Trigger sporulation"],
  "A CRISPR spacer matching a conjugative-plasmid nickase blocked conjugation and plasmid transformation.", "Block gene transfer."),
 ("¿Qué demostró el estudio de 2008 en Science que pueden hacer los loci CRISPR en Staphylococcus epidermidis?", ["Acelerar la captación de plásmidos", "Causar resistencia a antibióticos", "Bloquear conjugación y transformación", "Disparar la esporulación bajo estrés"],
  "Un espaciador CRISPR que coincidía con la nickasa de un plásmido conjugativo bloqueaba la conjugación y la transformación.", "Bloquear transferencia génica.")),
("19095942", "expert", 3, "the interference machinery targets DNA directly",
 ("Inserting a self-splicing intron into the target gene showed that staphylococcal CRISPR interference acts on what?", ["The spliced mRNA", "A protein product", "The ribosome", "The DNA directly"],
  "Because interference persisted despite mRNA repair by splicing, the machinery was shown to target DNA directly.", "DNA directly."),
 ("Insertar un intrón autoempalmante en el gen blanco mostró que la interferencia CRISPR estafilocócica actúa sobre ¿qué?", ["El ARNm maduro empalmado", "Un producto proteico", "El propio ribosoma", "El ADN directamente"],
  "Como la interferencia persistía pese a reparar el ARNm por empalme, se demostró que la maquinaria ataca el ADN directamente.", "El ADN directamente.")),

# --- CRISPR cleaves plasmid/phage DNA (21048762)
("21048762", "explorer", 0, "the Streptococcus thermophilus CRISPR1/Cas system can also naturally acquire spacers from a self-replicating plasmid",
 ("What did the 2010 Nature study show the Streptococcus thermophilus CRISPR1/Cas system could do with plasmids?", ["Acquire spacers and lose the plasmid", "Copy plasmids into the chromosome", "Protect and spread the plasmid", "Ignore plasmids entirely"],
  "The system acquired spacers from a self-replicating plasmid, leading to plasmid loss.", "Acquire spacers, lose plasmid."),
 ("¿Qué demostró el estudio de 2010 en Nature que podía hacer el sistema CRISPR1/Cas de Streptococcus thermophilus con los plásmidos?", ["Adquirir espaciadores del plásmido", "Copiar plásmidos al cromosoma", "Proteger y difundir el plásmido", "Ignorar los plásmidos por completo"],
  "El sistema adquiría espaciadores de un plásmido autorreplicante, lo que llevaba a perder el plásmido.", "Adquiere espaciadores, pierde plásmido.")),
("21048762", "researcher", 1, "the CRISPR1/Cas system specifically cleaves plasmid and bacteriophage double-stranded DNA within the proto-spacer",
 ("Where did the S. thermophilus CRISPR1/Cas system cleave its cut in invading plasmid and phage DNA?", ["At random genomic sites", "Within the proto-spacer", "Only in repeat sequences", "At the plasmid origin only"],
  "The system cleaved invading double-stranded DNA specifically within the proto-spacer.", "In the proto-spacer."),
 ("¿Dónde cortaba el sistema CRISPR1/Cas de S. thermophilus el ADN invasor de plásmidos y fagos?", ["En sitios genómicos al azar", "Dentro del proto-espaciador", "Solo en secuencias repetidas", "Solo en el origen del plásmido"],
  "El sistema cortaba el ADN bicatenario invasor específicamente dentro del proto-espaciador.", "En el proto-espaciador.")),

# --- Anti-CRISPR phage genes (23242138)
("23242138", "researcher", 2, "Five distinct 'anti-CRISPR' genes were found in the genomes of bacteriophages infecting Pseudomonas aeruginosa",
 ("What did the 2013 Nature study discover in phages infecting Pseudomonas aeruginosa?", ["New CRISPR spacers", "A second bacterial genome", "Anti-CRISPR genes", "A universal autoinducer"],
  "Five distinct anti-CRISPR genes let phages evade the host CRISPR/Cas system.", "Anti-CRISPR genes."),
 ("¿Qué descubrió el estudio de 2013 en Nature en fagos que infectan Pseudomonas aeruginosa?", ["Espaciadores CRISPR", "Otro genoma bacteriano", "Genes anti-CRISPR", "Un autoinductor"],
  "Cinco genes anti-CRISPR distintos permitían a los fagos evadir el sistema CRISPR/Cas del hospedador.", "Genes anti-CRISPR.")),

# --- Obesity gut microbiome (17183312)
("17183312", "researcher", 3, "the obese microbiome has an increased capacity to harvest energy from the diet",
 ("What did the 2006 Nature study conclude about the gut microbiome of obese versus lean mice?", ["It had fewer total bacteria", "It made the mice eat more food", "It could not be transplanted", "It harvested more dietary energy"],
  "The obese microbiome had greater capacity to harvest energy, and this trait was transmissible to germ-free mice.", "More energy harvest."),
 ("¿Qué concluyó el estudio de 2006 en Nature sobre el microbioma intestinal de ratones obesos frente a delgados?", ["Tenía menos bacterias en total", "Hacía que los ratones comieran más", "No podía trasplantarse", "Extraía más energía de la dieta"],
  "El microbioma obeso tenía mayor capacidad de extraer energía, y ese rasgo era transmisible a ratones libres de gérmenes.", "Más extracción de energía.")),
("17183312", "explorer", 0, "the two dominant bacterial divisions, the Bacteroidetes and the Firmicutes",
 ("Which two dominant bacterial groups shifted in abundance with obesity in the 2006 gut microbiome study?", ["Bacteroidetes and Firmicutes", "Proteobacteria and Fusobacteria", "Actinobacteria and Spirochetes", "Cyanobacteria and Chloroflexi"],
  "Obesity was linked to shifts between the two dominant divisions, Bacteroidetes and Firmicutes.", "Bacteroidetes and Firmicutes."),
 ("¿Qué dos grupos bacterianos dominantes cambiaban en abundancia con la obesidad en el estudio de microbioma de 2006?", ["Bacteroidetes y Firmicutes", "Proteobacterias y Fusobacterias", "Actinobacterias y Espiroquetas", "Cianobacterias y Cloroflexi"],
  "La obesidad se asoció con cambios entre las dos divisiones dominantes, Bacteroidetes y Firmicutes.", "Bacteroidetes y Firmicutes.")),

# --- Human gut gene catalogue (20203603)
("20203603", "researcher", 1, "each individual at least 160 such species",
 ("The 2010 Nature human gut gene catalogue estimated each person harbors at least how many prevalent bacterial species?", ["About 20 species", "At least 160 species", "Exactly 1,000 species", "More than 5,000 species"],
  "The cohort held 1,000–1,150 prevalent species, with each individual carrying at least 160.", "At least 160."),
 ("El catálogo de genes del intestino humano de 2010 (Nature) estimó que cada persona alberga al menos ¿cuántas especies bacterianas prevalentes?", ["Unas 20 especies", "Al menos 160 especies", "Exactamente 1.000 especies", "Más de 5.000 especies"],
  "La cohorte albergaba entre 1.000 y 1.150 especies prevalentes, con al menos 160 por persona.", "Al menos 160.")),
("20203603", "expert", 2, "3.3 million non-redundant microbial genes",
 ("How many non-redundant microbial genes did the 2010 metagenomic human gut catalogue describe?", ["About 23,000", "Around 150,000", "About 3.3 million", "Over 500 million"],
  "The catalogue described 3.3 million non-redundant microbial genes, ~150 times the human gene count.", "3.3 million genes."),
 ("¿Cuántos genes microbianos no redundantes describió el catálogo metagenómico del intestino humano de 2010?", ["Cerca de 23.000", "Alrededor de 150.000", "Unos 3,3 millones", "Más de 500 millones"],
  "El catálogo describió 3,3 millones de genes microbianos no redundantes, unas 150 veces el número de genes humanos.", "3,3 millones de genes.")),

# --- Enterotypes (21508958)
("21508958", "researcher", 3, "we identify three robust clusters (referred to as enterotypes hereafter) that are not nation or continent specific",
 ("What key finding did the 2011 Nature study on the human gut microbiome report?", ["Gut flora is identical worldwide", "Diet erases all differences", "Each country has a unique type", "Three robust enterotypes exist"],
  "The gut microbiome clustered into three enterotypes, not specific to nation or continent.", "Three enterotypes."),
 ("¿Qué hallazgo clave reportó el estudio de 2011 en Nature sobre el microbioma intestinal humano?", ["La flora es idéntica en el mundo", "La dieta borra toda diferencia", "Cada país tiene un tipo único", "Existen tres enterotipos robustos"],
  "El microbioma intestinal se agrupaba en tres enterotipos, no específicos de país ni continente.", "Tres enterotipos.")),

# --- First US cases of Candida auris (27832049)
("27832049", "explorer", 1, "Data from these cases suggest that transmission of C. auris might have occurred in U.S. health care facilities",
 ("What did the investigation of the first seven US Candida auris cases (2013-2016) suggest?", ["The fungus came from a pet dog", "Transmission in health care", "All cases were laboratory contamination", "It only affected newborn infants"],
  "The first US cases suggested C. auris transmission within health care facilities, stressing infection control.", "Spread in hospitals."),
 ("¿Qué sugirió la investigación de los primeros siete casos de Candida auris en EE. UU. (2013-2016)?", ["El hongo vino de mascotas", "Hubo transmisión en centros de salud", "Todos fueron contaminación de laboratorio", "Solo afectó a recién nacidos"],
  "Los primeros casos en EE. UU. sugirieron transmisión de C. auris dentro de centros de salud, resaltando el control de infecciones.", "Contagio hospitalario.")),
("27832049", "curious", 3, "is associated with high mortality and is often resistant to multiple antifungal drugs",
 ("Why is the emerging fungus Candida auris of particular concern, per the 2016 CDC report?", ["It spreads only through food", "It is harmless but hard to grow in the lab", "It resists all known antibiotics", "Deadly and often drug resistant"],
  "C. auris causes invasive infections with high mortality and is often multidrug resistant.", "Deadly, drug resistant."),
 ("¿Por qué preocupa especialmente el hongo emergente Candida auris, según el informe de los CDC de 2016?", ["Solo se contagia por alimentos", "Es inofensivo pero difícil de cultivar", "Resiste todos los antibióticos", "Alta mortalidad y multirresistente"],
  "C. auris causa infecciones invasivas con alta mortalidad y suele ser multirresistente.", "Mortal y resistente.")),

# --- Worsening spread of C. auris in the US (36940442)
("36940442", "researcher", 0, "The number of C auris cases that were resistant to echinocandins in 2021 was about 3 times that in each of the previous 2 years",
 ("What alarming trend did the 2023 report on US Candida auris spread (2019-2021) highlight?", ["Resistance roughly tripled", "Cases fell sharply after 2019", "It vanished from most states", "It became azole susceptible"],
  "Echinocandin-resistant cases in 2021 were about three times the prior years, threatening first-line therapy.", "Echinocandin resistance up."),
 ("¿Qué tendencia alarmante destacó el informe de 2023 sobre la propagación de Candida auris en EE. UU. (2019-2021)?", ["La resistencia se triplicó", "Los casos cayeron mucho en 2021", "Desapareció de casi todos los estados del país", "Se volvió sensible a los azoles"],
  "Los casos resistentes a equinocandinas en 2021 fueron cerca del triple de los años previos, amenazando la terapia de primera línea.", "Más resistencia a equinocandinas.")),

# --- HipA, (p)ppGpp and persisters (25848049)
("25848049", "expert", 2, "slow growth per se does not induce persistence in the absence of TA-encoded toxins",
 ("What did the 2015 PNAS single-cell study conclude about slow growth and bacterial persistence?", ["Slow growth alone causes persistence", "Persistence needs oxygen stress", "Slow growth alone is not enough", "Fast growth makes persisters"],
  "High (p)ppGpp from HipA did not induce persistence without the toxin-antitoxin mRNases; slow growth alone was insufficient.", "Slow growth not enough."),
 ("¿Qué concluyó el estudio unicelular de 2015 en PNAS sobre el crecimiento lento y la persistencia bacteriana?", ["El crecimiento lento basta para persistir", "La persistencia necesita estrés por oxígeno", "El crecimiento lento solo no basta", "El crecimiento rápido crea persistentes"],
  "El alto (p)ppGpp de HipA no inducía persistencia sin las mRNasas toxina-antitoxina; el crecimiento lento solo no bastaba.", "No basta crecer lento.")),
("25848049", "researcher", 3, "The model organism Escherichia coli codes for at least 11 type II toxin-antitoxin (TA) modules",
 ("The 2015 persistence study notes that Escherichia coli encodes at least how many type II toxin-antitoxin modules?", ["Only about two", "Exactly five", "Around eight", "At least 11"],
  "E. coli carries at least 11 type II toxin-antitoxin modules, most encoding mRNA endonucleases tied to persistence.", "At least 11."),
 ("El estudio de persistencia de 2015 señala que Escherichia coli codifica al menos ¿cuántos módulos toxina-antitoxina de tipo II?", ["Unos 2", "Exactamente 5", "Alrededor de 8", "Al menos 11"],
  "E. coli porta al menos 11 módulos toxina-antitoxina de tipo II, la mayoría con endonucleasas de ARNm ligadas a la persistencia.", "Al menos 11.")),

# --- Ancient resistance genes (21881561)
("21881561", "researcher", 2, "the identification of a highly diverse collection of genes encoding resistance to β-lactam, tetracycline and glycopeptide antibiotics",
 ("What did metagenomic analysis of 30,000-year-old permafrost reveal in the 2011 study 'Antibiotic resistance is ancient'?", ["No resistance genes at all", "Only modern contamination", "Diverse resistance genes", "Genes for only one drug class"],
  "The permafrost DNA held diverse genes for beta-lactam, tetracycline and glycopeptide resistance.", "Ancient resistance genes."),
 ("¿Qué reveló el análisis metagenómico de permafrost de 30.000 años en el estudio de 2011 'La resistencia a antibióticos es antigua'?", ["Ningún gen de resistencia", "Solo contaminación moderna", "Genes diversos de resistencia", "Genes para una sola clase de fármaco"],
  "El ADN del permafrost contenía genes diversos de resistencia a betalactámicos, tetraciclinas y glicopéptidos.", "Genes antiguos de resistencia.")),
("21881561", "curious", 3, "antibiotic resistance is a natural phenomenon that predates the modern selective pressure of clinical antibiotic use",
 ("What broad conclusion did the ancient-DNA resistance study of 2011 reach?", ["Resistance was invented in labs", "Resistance began in the 1940s", "Only hospital bacteria resist drugs", "Resistance predates antibiotics"],
  "Resistance is a natural phenomenon that predates modern clinical antibiotic use.", "It predates antibiotics."),
 ("¿Qué conclusión general alcanzó el estudio de 2011 sobre resistencia en ADN antiguo?", ["La resistencia se inventó en laboratorios", "La resistencia empezó en los años 40", "Solo resisten las bacterias de hospital", "La resistencia es anterior a los antibióticos"],
  "La resistencia es un fenómeno natural anterior al uso clínico moderno de antibióticos.", "Anterior a los antibióticos.")),

# --- Thermus aquaticus (5781580)
("5781580", "explorer", 0, "Successful enrichment requires incubation at 70 to 75 C",
 ("The 1969 description of the extreme thermophile Thermus aquaticus required culturing at what temperature?", ["70 to 75 °C", "About 37 °C", "Near 20 °C", "Above 100 °C"],
  "Enrichment of T. aquaticus, later the source of Taq polymerase, required 70–75 °C.", "70–75 °C."),
 ("La descripción de 1969 del termófilo extremo Thermus aquaticus requería cultivarlo ¿a qué temperatura?", ["De 70 a 75 °C", "Cerca de 37 °C", "Cerca de 20 °C", "Por encima de 100 °C"],
  "El enriquecimiento de T. aquaticus, luego fuente de la Taq polimerasa, requería 70–75 °C.", "70–75 °C.")),
("5781580", "researcher", 1, "isolated from a variety of thermal springs in Yellowstone National Park",
 ("Where was Thermus aquaticus first isolated, according to its 1969 description?", ["Deep ocean vents off Hawaii", "Thermal springs in Yellowstone", "An Antarctic dry valley lake", "A volcanic crater in Iceland"],
  "Strains came from thermal springs in Yellowstone and other hot habitats, even hot tap water.", "Yellowstone hot springs."),
 ("¿Dónde se aisló por primera vez Thermus aquaticus, según su descripción de 1969?", ["Fuentes hidrotermales de Hawái", "Aguas termales de Yellowstone", "Un lago de valle seco antártico", "Un cráter volcánico en Islandia"],
  "Las cepas provenían de aguas termales de Yellowstone y otros hábitats calientes, incluso agua caliente de grifo.", "Aguas termales de Yellowstone.")),

# --- Persister cells and dormancy (17143318)
("17143318", "researcher", 2, "these seemingly disparate phenomena result from the ability of bacteria to enter into a dormant (non-dividing) state",
 ("According to the 2007 review by Lewis, what links persister cells, latent infections and biofilm tolerance?", ["Horizontal gene transfer", "Acquired resistance genes", "A dormant, non-dividing state", "Rapid mutation under stress"],
  "These phenomena stem from bacteria entering a dormant, non-dividing state rather than acquiring resistance.", "Dormancy."),
 ("Según la revisión de 2007 de Lewis, ¿qué une a las células persistentes, las infecciones latentes y la tolerancia de las biopelículas?", ["La transferencia horizontal de genes", "Genes de resistencia adquiridos", "Un estado durmiente que no se divide", "La mutación rápida bajo estrés"],
  "Estos fenómenos surgen de bacterias que entran en un estado durmiente que no se divide, no de resistencia adquirida.", "Latencia.")),
("17143318", "curious", 3, "unculturable microorganisms, persister cells and biofilm multidrug tolerance",
 ("Which long-standing microbiology puzzle is NOT grouped with dormancy in the 2007 persister review?", ["Latent bacterial infections", "Unculturable microorganisms", "Biofilm multidrug tolerance", "Rising antibiotic prices"],
  "The review groups latent infections, unculturable microbes, persisters and biofilm tolerance as effects of dormancy.", "Antibiotic prices."),
 ("¿Qué viejo enigma de la microbiología NO se agrupa con la latencia en la revisión de persistentes de 2007?", ["Infecciones bacterianas latentes", "Microorganismos no cultivables", "Tolerancia multidrogas de biopelículas", "El alza del precio de los antibióticos"],
  "La revisión agrupa infecciones latentes, microbios no cultivables, persistentes y tolerancia de biopelículas como efectos de la latencia.", "El precio de los antibióticos.")),

# --- Quorum-sensing regulon in Vibrio fischeri (10781550)
("10781550", "researcher", 0, "The luminescence (lux) operon (luxICDABEG) of the symbiotic bacterium Vibrio fischeri is regulated by the transcriptional activator LuxR",
 ("In Vibrio fischeri, what process is controlled by the LuxR activator and acyl-homoserine-lactone signals?", ["Bioluminescence", "Flagellar swimming", "Spore formation", "Iron scavenging"],
  "LuxR and acyl-HSL autoinducers drive the lux operon, producing light in a population-density manner.", "Bioluminescence."),
 ("En Vibrio fischeri, ¿qué proceso controlan el activador LuxR y las señales de acil-homoserina lactona?", ["La bioluminiscencia", "El nado flagelar", "La esporulación", "La captación de hierro"],
  "LuxR y los autoinductores acil-HSL activan el operón lux, generando luz según la densidad de población.", "Bioluminiscencia.")),
("10781550", "expert", 1, "a qsrP mutant, in competition with its parent strain, was less successful in colonizing Euprymna scolopes",
 ("What did deleting the quorum-sensing gene qsrP do to Vibrio fischeri in the study of its regulon?", ["Made it glow more brightly", "Impaired host colonization", "Killed the bacterium outright", "Had no effect on symbiosis"],
  "A qsrP mutant was less able to colonize the squid Euprymna scolopes than its parent.", "Poorer colonization."),
 ("¿Qué le ocurrió a Vibrio fischeri al eliminar el gen de quorum sensing qsrP en el estudio de su regulón?", ["Brillaba con más intensidad", "Colonizaba peor a su calamar", "La bacteria moría de inmediato", "No afectaba a la simbiosis"],
  "Un mutante qsrP colonizaba peor al calamar Euprymna scolopes que su cepa parental.", "Peor colonización.")),
]
