#!/usr/bin/env python3
"""Single source of truth for TRINKA's UI strings (English + Spanish).

Edit the table below, then run `python3 Scripts/generate_strings.py`. It writes
Packages/TrinkaKit/Sources/TrinkaUI/Resources/{en,es}.lproj/Localizable.strings and reports
keys used in the code but missing here, and format-specifier mismatches between languages.
To add a language, add a column and an output folder.
"""
S = {
# key: (en, es)
"app.tagline": ("Science. Curiosity. Discovery.", "Ciencia. Curiosidad. Descubrimiento."),
"tab.home": ("Home", "Inicio"),
"tab.explore": ("Explore", "Explorar"),
"tab.discover": ("Discover", "Descubrir"),
"tab.progress": ("Progress", "Progreso"),

"category.microbiology": ("Microbiology", "Microbiología"),
"category.immunology": ("Immunology", "Inmunología"),
"category.genetics": ("Genetics", "Genética"),
"category.neuroscience": ("Neuroscience", "Neurociencia"),
"category.humanPhysiology": ("Human Physiology", "Fisiología humana"),
"category.medicine": ("Medicine", "Medicina"),
"category.biotechnology": ("Biotechnology", "Biotecnología"),
"category.nutrition": ("Nutrition", "Nutrición"),
"category.veterinaryScience": ("Veterinary Science", "Veterinaria"),
"category.generalScience": ("General Science", "Ciencia general"),

"difficulty.beginner": ("Basic", "Básico"),
"difficulty.curious": ("Curious", "Curioso"),
"difficulty.explorer": ("Explorer", "Explorador"),
"difficulty.researcher": ("Researcher", "Investigador"),
"difficulty.expert": ("Expert", "Experto"),
"difficulty.mixed": ("Mixed", "Mixta"),
"difficulty.beginner.detail": ("Core ideas anyone can answer.", "Ideas básicas que cualquiera puede responder."),
"difficulty.curious.detail": ("General scientific knowledge.", "Conocimientos científicos generales."),
"difficulty.explorer.detail": ("The key results of each study.", "Los resultados clave de cada estudio."),
"difficulty.researcher.detail": ("Results and methods in more depth.", "Resultados y métodos en profundidad."),
"difficulty.expert.detail": ("Exact figures, methods and mechanisms.", "Cifras exactas, métodos y mecanismos."),
"difficulty.mixed.detail": ("A blend of all levels.", "Una mezcla de todos los niveles."),

"appearance.system": ("System", "Sistema"),
"appearance.light": ("Light", "Claro"),
"appearance.dark": ("Dark", "Oscuro"),

"stats.streak": ("Day streak", "Racha de días"),
"stats.xp": ("Total XP", "XP total"),
"stats.today": ("XP today", "XP de hoy"),
"streak.days": ("Streak: %ld", "Racha: %ld"),

"home.quickPlay": ("Quick play · 5 questions", "Juego rápido · 5 preguntas"),
"home.categories": ("Disciplines", "Disciplinas"),
"home.categories.subtitle": ("Tap one for a 3-question round.", "Toca una para una ronda de 3 preguntas."),
"home.categories.hint": ("Starts a short quiz in this discipline.", "Inicia un cuestionario corto de esta disciplina."),
"home.level": ("Your level", "Tu nivel"),
"home.featured": ("Featured discovery", "Descubrimiento destacado"),

"daily.title": ("Daily Challenge", "Desafío del día"),
"daily.subtitle": ("%ld questions from real research.", "%ld preguntas basadas en investigaciones reales."),
"daily.completed": ("Done! %ld of %ld correct today.", "¡Hecho! %ld de %ld correctas hoy."),
"daily.play": ("Play", "Jugar"),
"daily.replay": ("Practice again", "Practicar de nuevo"),

"quiz.progress": ("Question %ld of %ld", "Pregunta %ld de %ld"),
"quiz.next": ("Next question", "Siguiente pregunta"),
"quiz.seeResults": ("See results", "Ver resultados"),
"quiz.exit": ("End quiz", "Terminar cuestionario"),
"quiz.exit.confirm": ("End this quiz? Progress in this round won't be saved.", "¿Terminar el cuestionario? No se guardará el progreso de esta ronda."),
"quiz.empty.title": ("No questions available", "No hay preguntas disponibles"),
"quiz.empty.message": ("Try another discipline or difficulty.", "Prueba otra disciplina o dificultad."),

"feedback.correct": ("Correct!", "¡Correcto!"),
"feedback.incorrect": ("Not quite", "No exactamente"),
"feedback.timeout": ("Time's up", "Se acabó el tiempo"),
"feedback.correctAnswer": ("Correct answer: %@", "Respuesta correcta: %@"),
"feedback.source": ("Source · view the original study", "Fuente · ver el estudio original"),

"source.title": ("Source", "Fuente"),
"source.excerpt": ("Supporting text from the abstract", "Texto del resumen que lo respalda"),
"source.openPubMed": ("PubMed", "PubMed"),
"source.openDOI": ("Publisher", "Editorial"),

"result.done": ("Done", "Listo"),
"result.time": ("Time: %@", "Tiempo: %@"),
"result.message.perfect": ("Perfect run — brilliant curiosity!", "¡Ronda perfecta, qué curiosidad tan brillante!"),
"result.message.great": ("Great work! Science suits you.", "¡Muy bien! La ciencia te sienta bien."),
"result.message.good": ("Every answer is a new discovery.", "Cada respuesta es un nuevo descubrimiento."),
"result.message.keepGoing": ("Keep exploring — that's how science works.", "Sigue explorando: así funciona la ciencia."),
"result.xp": ("Experience earned", "Experiencia obtenida"),
"result.xp.answers": ("Correct answers", "Respuestas correctas"),
"result.xp.completion": ("Challenge completed", "Desafío completado"),
"result.xp.perfect": ("Perfect run", "Ronda perfecta"),
"result.xp.streak": ("Streak bonus", "Bonificación por racha"),
"result.xp.newCategories": ("New disciplines explored", "Nuevas disciplinas exploradas"),
"result.newAchievements": ("New achievements", "Nuevos logros"),
"result.learned": ("What you learned", "Lo que aprendiste"),
"result.learned.subtitle": ("Each point comes from a published study.", "Cada punto proviene de un estudio publicado."),

"explore.title": ("Explore", "Explorar"),
"explore.discipline": ("Discipline", "Disciplina"),
"explore.allCategories": ("All", "Todas"),
"explore.difficulty": ("Difficulty", "Dificultad"),
"explore.length": ("Questions", "Preguntas"),
"explore.available": ("%ld verified questions available.", "%ld preguntas verificadas disponibles."),
"explore.start": ("Start quiz", "Empezar cuestionario"),
"explore.recent": ("Recent research", "Investigación reciente"),
"explore.recent.subtitle": ("Latest PubMed publications in this area.", "Últimas publicaciones de PubMed en esta área."),

"discover.title": ("Discover", "Descubrir"),
"discover.search": ("Search a research topic", "Busca un tema de investigación"),
"discover.filters": ("Filters", "Filtros"),
"discover.filter.date": ("Publication date", "Fecha de publicación"),
"discover.filter.newestFirst": ("Newest first", "Más recientes primero"),
"discover.filter.type": ("Publication type", "Tipo de publicación"),
"discover.recency.any": ("Any time", "Cualquier fecha"),
"discover.recency.lastYear": ("Last 12 months", "Últimos 12 meses"),
"discover.recency.last5Years": ("Last 5 years", "Últimos 5 años"),
"discover.empty.title": ("No results", "Sin resultados"),
"discover.empty.message": ("Try a broader topic or fewer filters.", "Prueba un tema más amplio o menos filtros."),
"discover.cached": ("Offline · results saved %@", "Sin conexión · resultados guardados %@"),
"discover.bundled": ("Offline · showing the studies behind TRINKA's questions", "Sin conexión · mostrando los estudios en los que se basan las preguntas de TRINKA"),
"discover.attribution": ("Data from PubMed® via NCBI E-utilities. Summaries use the authors' own abstracts.", "Datos de PubMed® mediante NCBI E-utilities. Los resúmenes usan los abstracts de los propios autores."),

"article.reportedFinding": ("What this study reports", "Lo que reporta este estudio"),
"article.abstract": ("Abstract", "Resumen (abstract)"),
"article.abstractLanguage": ("Abstract shown as published, usually in English.", "Resumen mostrado tal como se publicó, normalmente en inglés."),

"evidence.singleStudy": ("Single study", "Estudio individual"),
"evidence.narrativeReview": ("Review", "Revisión"),
"evidence.evidenceSynthesis": ("Evidence synthesis", "Síntesis de evidencia"),
"evidence.singleStudy.note": ("These are the findings of one study. They may not reflect the overall scientific consensus until confirmed by other research.", "Son los hallazgos de un único estudio. Pueden no reflejar el consenso científico general hasta que otras investigaciones los confirmen."),
"evidence.narrativeReview.note": ("A review summarizes a field from the authors' perspective; it is not a systematic analysis of all the evidence.", "Una revisión resume un campo desde la perspectiva de sus autores; no es un análisis sistemático de toda la evidencia."),
"evidence.evidenceSynthesis.note": ("Systematic reviews and meta-analyses combine many studies and are closer to the overall body of evidence.", "Las revisiones sistemáticas y los metaanálisis combinan muchos estudios y se acercan más al conjunto de la evidencia."),

"publicationType.journalArticle": ("Journal article", "Artículo de revista"),
"publicationType.review": ("Review", "Revisión"),
"publicationType.systematicReview": ("Systematic review", "Revisión sistemática"),
"publicationType.metaAnalysis": ("Meta-analysis", "Metaanálisis"),
"publicationType.randomizedControlledTrial": ("Randomized controlled trial", "Ensayo controlado aleatorizado"),
"publicationType.clinicalTrial": ("Clinical trial", "Ensayo clínico"),

"progress.title": ("Progress", "Progreso"),
"progress.answered": ("Questions answered", "Preguntas respondidas"),
"progress.accuracy": ("Correct answers", "Aciertos"),
"progress.streak": ("Current streak · best %ld", "Racha actual · mejor %ld"),
"progress.evolution": ("Last 14 days", "Últimos 14 días"),
"progress.evolution.subtitle": ("Answers per day", "Respuestas por día"),
"progress.chart.day": ("Day", "Día"),
"progress.chart.correct": ("Correct", "Correctas"),
"progress.chart.incorrect": ("Incorrect", "Incorrectas"),
"progress.categories": ("Disciplines", "Disciplinas"),
"progress.categories.empty": ("Play a quiz to see your favorite disciplines.", "Juega un cuestionario para ver tus disciplinas favoritas."),
"progress.favorites": ("Favorites: %@", "Favoritas: %@"),
"progress.achievements": ("Achievements", "Logros"),
"progress.disclaimer": ("These statistics describe your quiz activity in TRINKA. They are not a measure of intelligence or cognitive ability.", "Estas estadísticas describen tu actividad en los cuestionarios de TRINKA. No son una medida de inteligencia ni de capacidad cognitiva."),

"achievement.firstDiscovery.title": ("First Discovery", "Primer descubrimiento"),
"achievement.firstDiscovery.detail": ("Answer your first question correctly.", "Responde bien tu primera pregunta."),
"achievement.curiousMind.title": ("Curious Mind", "Mente curiosa"),
"achievement.curiousMind.detail": ("Answer 50 questions.", "Responde 50 preguntas."),
"achievement.scienceExplorer.title": ("Science Explorer", "Explorador científico"),
"achievement.scienceExplorer.detail": ("Play all 10 disciplines.", "Juega las 10 disciplinas."),
"achievement.sevenDayStreak.title": ("Seven-Day Streak", "Racha de siete días"),
"achievement.sevenDayStreak.detail": ("Learn something 7 days in a row.", "Aprende algo 7 días seguidos."),
"achievement.microbiologyMaster.title": ("Microbiology Master", "Maestro de la microbiología"),
"achievement.microbiologyMaster.detail": ("15 correct microbiology answers.", "15 respuestas correctas de microbiología."),
"achievement.researchEnthusiast.title": ("Research Enthusiast", "Entusiasta de la investigación"),
"achievement.researchEnthusiast.detail": ("Open 10 original studies.", "Abre 10 estudios originales."),

"settings.title": ("Settings", "Ajustes"),
"settings.appearance": ("Appearance", "Apariencia"),
"settings.appearance.footer": ("System follows your iPhone's light or dark mode.", "Sistema sigue el modo claro u oscuro de tu iPhone."),
"settings.intro": ("Animated logo at launch", "Logo animado al abrir"),
"intro.skip": ("Tap to skip", "Toca para saltar"),
"settings.language": ("Language", "Idioma"),
"settings.language.system": ("System", "Sistema"),
"settings.quiz": ("Quizzes", "Cuestionarios"),
"settings.difficulty": ("Your level", "Tu nivel"),
"settings.timer": ("Question timer", "Temporizador por pregunta"),
"settings.timer.seconds": ("%ld seconds per question", "%ld segundos por pregunta"),
"settings.timer.footer": ("Optional. Scores never depend on speed.", "Opcional. La puntuación nunca depende de la velocidad."),
"settings.watch": ("Apple Watch", "Apple Watch"),
"settings.watch.send": ("Send today's challenge to Apple Watch", "Enviar el desafío de hoy al Apple Watch"),
"settings.watch.sent": ("Sent to Apple Watch", "Enviado al Apple Watch"),
"settings.watch.unavailable": ("Install TRINKA on a paired Apple Watch to sync.", "Instala TRINKA en un Apple Watch emparejado para sincronizar."),
"settings.about": ("About", "Acerca de"),
"settings.about.sources": ("Questions are based on articles indexed in PubMed. Each one links to its original publication and quotes the passage that supports the answer.", "Las preguntas se basan en artículos indexados en PubMed. Cada una enlaza a su publicación original y cita el fragmento que respalda la respuesta."),
"settings.about.privacy": ("No account needed. Your progress is stored only on your devices.", "Sin cuenta. Tu progreso se guarda solo en tus dispositivos."),
"settings.about.ncbi": ("NCBI policies and disclaimer", "Políticas y avisos de NCBI"),
"settings.reset": ("Reset progress", "Restablecer progreso"),
"settings.reset.confirm": ("Delete all progress, streaks and achievements on this iPhone?", "¿Borrar todo el progreso, rachas y logros de este iPhone?"),

"state.loading": ("Loading", "Cargando"),
"state.offline.title": ("You're offline", "Sin conexión"),
"state.offline.message": ("Connect to the internet to load new research. Your quizzes still work offline.", "Conéctate a internet para cargar nuevas investigaciones. Los cuestionarios siguen funcionando sin conexión."),
"common.apply": ("Apply", "Aplicar"),

"watch.tagline": ("Your daily science challenge.", "Tu desafío científico diario."),
"watch.play": ("PLAY", "JUGAR"),
"watch.playAgain": ("PLAY AGAIN", "JUGAR OTRA VEZ"),
"watch.dailyScore": ("Today", "Hoy"),
"watch.challenge": ("Challenge", "Desafío"),
"watch.result.correct": ("Correct", "Aciertos"),
"watch.result.score": ("Score", "Puntuación"),
"watch.result.time": ("Time", "Tiempo"),
"watch.result.points": ("Points", "Puntos"),
"watch.result.openPhone": ("Open TRINKA on your iPhone for full explanations and sources.", "Abre TRINKA en tu iPhone para ver las explicaciones completas y las fuentes."),
"watch.settings.note": ("Language and other preferences follow your watch settings.", "El idioma y otras preferencias siguen los ajustes de tu reloj."),


"tab.compete": ("Compete", "Competir"),
"compete.title": ("Compete", "Competir"),
"compete.intro": ("Challenge friends or a group: everyone plays the same questions, each in their own language. Share the code, then share your result to build the leaderboard — no account needed.", "Reta a amigos o a un grupo: todos juegan las mismas preguntas, cada uno en su idioma. Comparte el código y luego tu resultado para armar la clasificación, sin necesidad de cuenta."),
"compete.name": ("Your name in challenges", "Tu nombre en los retos"),
"compete.name.placeholder": ("e.g. Ana", "p. ej. Ana"),
"compete.defaultName": ("Player", "Jugador"),
"compete.you": ("you", "tú"),
"compete.create": ("New challenge", "Nuevo reto"),
"compete.create.name": ("Challenge name", "Nombre del reto"),
"compete.create.titlePlaceholder": ("e.g. Biology class", "p. ej. Clase de biología"),
"compete.create.action": ("Create", "Crear"),
"compete.join": ("Join with code", "Unirse con código"),
"compete.join.message": ("Enter the code a friend shared with you, or paste their TRINKA link.", "Escribe el código que te compartieron o pega su enlace de TRINKA."),
"compete.join.action": ("Join challenge", "Unirse al reto"),
"compete.mine": ("Your challenges", "Tus retos"),
"compete.empty.title": ("No challenges yet", "Aún no hay retos"),
"compete.empty.message": ("Create one and share the code with friends or a group.", "Crea uno y comparte el código con amigos o con un grupo."),
"compete.delete": ("Delete", "Eliminar"),
"compete.players": ("%ld players", "%ld jugadores"),
"compete.questions": ("%ld questions", "%ld preguntas"),
"compete.code": ("Challenge code", "Código del reto"),
"compete.copy": ("Copy code", "Copiar código"),
"compete.copied": ("Copied", "Copiado"),
"compete.invite": ("Invite", "Invitar"),
"compete.play": ("Play challenge", "Jugar el reto"),
"compete.playAgain": ("Try again", "Intentar de nuevo"),
"compete.leaderboard": ("Leaderboard", "Clasificación"),
"compete.leaderboard.empty": ("No results yet. Play, then share your result.", "Todavía no hay resultados. Juega y comparte tu resultado."),
"compete.howResults": ("Ranking: most correct answers first; ties go to the fastest. When friends share their result link, opening it adds them here.", "Clasificación: primero quien tenga más aciertos; en caso de empate, quien fue más rápido. Al abrir el enlace de resultado de un amigo, se añade aquí."),
"compete.share.result": ("Share my result", "Compartir mi resultado"),
"compete.share.resultMessage": ("I got %ld/%ld in this TRINKA challenge. Open the link to add my result:", "Saqué %ld/%ld en este reto de TRINKA. Abre el enlace para añadir mi resultado:"),
"compete.share.inviteMessage": ("Join my TRINKA challenge “%@”. Code: %@", "Únete a mi reto de TRINKA «%@». Código: %@"),
"compete.defaultTitle": ("Science challenge", "Reto científico"),
"compete.defaultTitle.category": ("%@ challenge", "Reto de %@"),
"compete.link.title": ("Can't open this challenge", "No se puede abrir el reto"),
"compete.link.invalid": ("The code or link isn't valid. Check it and try again.", "El código o enlace no es válido. Revísalo e inténtalo de nuevo."),
"compete.link.incompatible": ("This challenge was created with a different version of TRINKA's questions. Update the app and try again.", "Este reto se creó con otra versión de las preguntas de TRINKA. Actualiza la app e inténtalo de nuevo."),
"common.ok": ("OK", "Aceptar"),
"common.cancel": ("Cancel", "Cancelar"),


"topic.title": ("Questions about any topic", "Preguntas sobre cualquier tema"),
"topic.example": ("e.g. Staphylococcus aureus, sleep, CRISPR", "p. ej. Staphylococcus aureus, sueño, CRISPR"),
"topic.intro": ("Type a topic. TRINKA finds recent PubMed articles about it and creates questions from their abstracts, at your level.", "Escribe un tema. TRINKA busca artículos de PubMed sobre él y crea preguntas a partir de sus resúmenes, a tu nivel."),
"topic.field": ("Topic", "Tema"),
"topic.placeholder": ("Staphylococcus aureus", "Staphylococcus aureus"),
"topic.generate": ("Create questions", "Crear preguntas"),
"topic.play": ("Play", "Jugar"),
"topic.ready": ("%ld questions from %ld articles", "%ld preguntas de %ld artículos"),
"topic.recent": ("Your topics", "Tus temas"),
"topic.fromSearch": ("Create questions about “%@”", "Crear preguntas sobre «%@»"),
"topic.progress.searching": ("Searching PubMed…", "Buscando en PubMed…"),
"topic.progress.generating": ("Writing questions from %ld articles and checking each answer against its abstract…", "Creando preguntas a partir de %ld artículos y comprobando cada respuesta en su resumen…"),
"topic.progress.checking": ("Checking answers against their sources…", "Comprobando las respuestas en sus fuentes…"),
"topic.disclaimer": ("These questions are generated automatically. Each answer is checked against a verbatim passage of the article's abstract, but no expert has reviewed them. You can always open the original study.", "Estas preguntas se generan automáticamente. Cada respuesta se comprueba con un fragmento literal del resumen del artículo, pero ningún experto las ha revisado. Siempre puedes abrir el estudio original."),
"topic.notConfigured": ("Question generation isn't set up in this build yet (see Backend/README.md).", "La generación de preguntas aún no está configurada en esta versión (ver Backend/README.md)."),
"topic.error.title": ("Couldn't create questions", "No se pudieron crear preguntas"),
"topic.error.noArticles": ("PubMed has no articles with an abstract for this topic. Try a broader or English term.", "PubMed no tiene artículos con resumen sobre este tema. Prueba un término más amplio o en inglés."),
"topic.error.noQuestions": ("Articles were found, but no question passed the source check. Try another level or topic.", "Se encontraron artículos, pero ninguna pregunta superó la comprobación con la fuente. Prueba otro nivel o tema."),
"topic.error.service": ("The question service didn't respond. Try again in a moment.", "El servicio de preguntas no respondió. Inténtalo de nuevo en un momento."),
"autogen.badge": ("Generated automatically", "Generada automáticamente"),
"autogen.note": ("Generated automatically: the answer was checked against the abstract, without expert review.", "Generada automáticamente: la respuesta se comprobó con el resumen, sin revisión de expertos."),

"a11y.difficulty": ("Difficulty: %@", "Dificultad: %@"),
"a11y.timeLeft": ("%ld seconds left", "Quedan %ld segundos"),
"a11y.answer.correct": ("Your answer, correct", "Tu respuesta, correcta"),
"a11y.answer.incorrect": ("Your answer, incorrect", "Tu respuesta, incorrecta"),
"a11y.answer.revealed": ("Correct answer", "Respuesta correcta"),
"a11y.unlocked": ("Unlocked", "Desbloqueado"),
}
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Packages/TrinkaKit/Sources/TrinkaUI/Resources")
SOURCES = ["Trinka", "TrinkaWatch", "Packages/TrinkaKit/Sources/TrinkaUI"]
LANGS = ["en", "es"]


def esc(v):
    return v.replace("\\", "\\\\").replace('"', '\\"')


def used_keys():
    pattern = re.compile(r'"([a-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)+)"')
    keys = set()
    for folder in SOURCES:
        for dirpath, _, files in os.walk(os.path.join(ROOT, folder)):
            for name in files:
                if name.endswith(".swift"):
                    for key in pattern.findall(open(os.path.join(dirpath, name), encoding="utf-8").read()):
                        if key.split(".")[0] in {k.split(".")[0] for k in S}:
                            keys.add(key)
    return keys


def main():
    for i, lang in enumerate(LANGS):
        os.makedirs(os.path.join(OUT, f"{lang}.lproj"), exist_ok=True)
        with open(os.path.join(OUT, f"{lang}.lproj", "Localizable.strings"), "w", encoding="utf-8") as f:
            f.write(f"/* TRINKA UI strings ({lang}). Generated by Scripts/generate_strings.py — edit that file instead. */\n\n")
            prev = None
            for k, v in S.items():
                group = k.split(".")[0]
                if prev and group != prev:
                    f.write("\n")
                prev = group
                f.write(f'"{k}" = "{esc(v[i])}";\n')
    missing = sorted(k for k in used_keys() if k not in S and not k.startswith(("category.", "difficulty.", "achievement.")))
    if missing:
        print("Missing keys:", missing)
    for k, values in S.items():
        specs = [re.findall(r"%[@a-z]+", v) for v in values]
        if any(sp != specs[0] for sp in specs):
            print("Format mismatch:", k)
    print(f"Wrote {len(S)} strings for {', '.join(LANGS)}.")


if __name__ == "__main__":
    main()
