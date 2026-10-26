"""Dérive la batterie d'essais v13 du lanceur du pilote 4 de la batterie v12 (`essais_lanceur_pilote4_v12.sh`, 27ef4524…),
par remplacements exacts au nombre attendu, pour le lanceur v11 : la seconde course n'est plus la v5.3 (clé `v5-3`) mais le
même organisme, la v6.2.1, sur la question S (clé `v6-2-s`, nom `pilote4-gemini-v6-2-s-v1`, lignée `gemini-organisme-v6-2-s`,
graine enfant 0 ; décision de Lazar du 26 octobre 2026, 04:13 UTC, R-492). Chaque cas de la v12 garde un équivalent (clé,
noms, lignée, messages « la course S ne part qu'après… », question S `a54da93e…` dans les lignes de GO d'essai : une ligne
saine porte `8b1c7511…`, `a54da93e…` et `4f13647a…` ; `6251ab21…` n'est plus requis). Cas ajoutés : reel-v6-2-refusee (en
réel, `v6-2` refusée : « la course M a tourné sous le lanceur v10 ») ; go-m-seulement-refuse-v6-2-s (en simulation, `v6-2-s`
refusée si la ligne de GO porte `8b1c7511…` et non `a54da93e…`) et go-m-seulement-autorise-v6-2 (la même ligne suffit à
`v6-2`) ; question-v6-2, sain-v6-2-question, sain-v6-2-s-question (question par course) ; sain-v6-2-s-lanceur-attendu et
v62-lanceur-v10-en-simulation (en simulation, la porte « course précédente » attend ce lanceur-ci) ; reel-porte-v10-passee,
reel-porte-v10-attendu et reel-v6-2-s-precedente-sous-ce-lanceur (en réel, la porte attend le lanceur v10, 0203f546… : une
copie « réelle » de la v6.2 saine — LANCEMENT.md et manifeste réécrits, rescellée — passe la porte et les cas réels de
l'étape (0) courent sur `v6-2-s` derrière elle ; une copie « réelle » citant ce lanceur-ci est refusée). Le cas
m-sous-lanceur-pilote4 nomme le lanceur v11 dans la ligne qu'il écrit. La v12 n'a jamais tourné sur le lanceur v11.

Usage : python3 -I deriver_essais_pilote4_v13.py ESSAIS_V12 SORTIE
Refuse si l'empreinte de la batterie v12 n'est pas 27ef4524…, si une occurrence n'est pas au nombre attendu, si un reste
interdit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V12 = "27ef4524b1fa21174a15459645753d31c6ce6cdbc93c24ae0e38a93084800b9a"
SHA_LANCEUR_V10 = "0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V12:
    sys.exit("refus : la batterie source n'est pas la v12 27ef4524…")
t = b.decode("utf-8")
# 1. Remplacements globaux, comptés sur la v12 (la clé, les noms, la graine, les fichiers d'entrée, les messages)
globaux = [
    ("G_53", "G_S", 13),
    ("graine de la course v5-3 = ", "graine de la course v6-2-s = ", 5),
    ("pilote4-gemini-v5-3-v1", "pilote4-gemini-v6-2-s-v1", 10),
    ("V5C", "VSC", 28),
    ("REEL_V53", "REEL_S", 5),
    ('"$V53', '"$VS', 9),
    ('V53="$E/cas-sain-v5-3/', 'VS="$E/cas-sain-v6-2-s/', 1),
    ("verifier sain-v5-3-", "verifier sain-v6-2-s-", 7),
    ("cas sain-v5-3 ", "cas sain-v6-2-s ", 1),
    ("COURSE=v5-3", "COURSE=v6-2-s", 12),
    ("(v5-3 ou v6-2)", "(v6-2-s ou v6-2)", 2),
    ("dep-v53-", "dep-s-", 4),
    ("td-heure-fraiche-v53.json", "td-heure-fraiche-s.json", 2),
    ("reel-v5-3-", "reel-v6-2-s-", 4),
    ("prereg-graine-autre-course-v53", "prereg-graine-autre-course-v6-2-s", 1),
    ("prereg-graine-hors-entropie-v53", "prereg-graine-hors-entropie-v6-2-s", 1),
    ('cas organisme-v5-3 "empreinte d\'arbre de l\'organisme ≠ 6251ab21…"', 'cas organisme-v6-2-s "empreinte d\'arbre de l\'organisme ≠ 4f13647a…"', 1),
    ('cas nombre-v5-3 "fichiers au lieu de 22"', 'cas nombre-v6-2-s "fichiers au lieu de 26"', 1),
    ('PILOTE_RACINE="$E/cas-sain-v5-3"', 'PILOTE_RACINE="$E/cas-sain-v6-2-s"', 1),
    ("seg-v5-3-porte-saine", "seg-v6-2-s-porte-saine", 3),
    ('cas v5-3-depense-sans-empreinte-v62 "la ligne de dépense de v5.3 ne porte pas', 'cas v6-2-s-depense-sans-empreinte-v62 "la ligne de dépense de la course S ne porte pas', 1),
    ("de la course v5-3 écrite et recalculée", "de la course v6-2-s écrite et recalculée", 1),
    ("sed -i 's/^- course : v6-2 ;/- course : v5-3 ;/'", "sed -i 's/^- course : v6-2 ;/- course : v6-2-s ;/'", 1),
    ('"organisme : 22 fichiers, empreinte d\'arbre 6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753"',
     '"organisme : 26 fichiers, empreinte d\'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d"', 1),
    (': v5.3 ne part qu\'après v6.2"', ': la course S ne part qu\'après v6.2"', 1),
    ('echo "== course v5.3 : issues de v6.2 hors de la liste saine', 'echo "== course S (v6-2-s) : issues de v6.2 hors de la liste saine', 1),
    ('echo "== mode réel, course v5.3 (copie du dépôt sous /root) : refus à l\'étape (0 bis), avant tout appel =="',
     'echo "== mode réel, course S (v6-2-s) sans PRECEDENTE_V62 ou avec une course précédente non conforme (copie du dépôt sous /root) : refus à l\'étape (0 bis), avant tout appel =="', 1),
    ('echo "-- porte « v6.2 précédente » de la v5.3 sur la v6.2 en segments --"', 'echo "-- porte « v6.2 précédente » de la course S sur la v6.2 en segments --"', 1),
    ("lanceur : lancer_pilote4_gemini_v10.sh, sha256 $H/", "lanceur : lancer_pilote4_gemini_v11.sh, sha256 $H/", 1),
    # lignes de GO d'essai : une ligne saine porte les deux questions et l'organisme
    ("question `8b1c7511…`, organismes v5.3 `6251ab21…` et v6.2 `4f13647a…`", "questions M `8b1c7511…` et S `a54da93e…`, organisme v6.2.1 `4f13647a…`", 3),
    ("`8b1c7511…` `6251ab21…` `4f13647a…`", "`8b1c7511…` `a54da93e…` `4f13647a…`", 2),
    ("printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `8b1c7511…`, organisme v5.3 `6251ab21…` seulement ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-v53-seulement.md\"\n"
     "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `a54da93e…`, organismes `6251ab21…` `4f13647a…` ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-autre-question.md\"\n",
     "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question S `a54da93e…` seulement, organisme v6.2.1 `4f13647a…` ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-s-seulement.md\"\n"
     "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question M `8b1c7511…` seulement, organisme v6.2.1 `4f13647a…` ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-m-seulement.md\"\n"
     "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai) : question `00000000…` (ni M ni S), organisme `4f13647a…` ; texte %s |\\n' \"$T16\" > \"$E/entrees/go-autre-question.md\"\n", 1),
    # en-tête
    ("# Essais du lanceur du pilote 4 (v6.2 puis v5.3, banque v3, quatre générations notées, 6 rondes de conception au\n"
     "# plus), v12 : la v11 (ba47a625…) par `deriver_essais_pilote4_v12.py` pour le lanceur v10 (objet de la course v6-2 : la\n",
     "# Essais du lanceur du pilote 4 (la v6.2.1 sur la question M, clé `v6-2`, puis sur la question S, clé `v6-2-s`, banque v3, quatre générations notées, 6 rondes de conception au\n"
     "# plus), v13 : la v12 (27ef4524…) par `deriver_essais_pilote4_v13.py` pour le lanceur v11 (seconde course `v6-2-s` : le même\n"
     "# organisme, la v6.2.1, sur la question S `a54da93e…`, à la place de la clé `v5-3` — la v5.3 ne court pas, décision de Lazar du\n"
     "# 26 octobre 2026, 04:13 UTC, R-492 ; question par course ; chaque cas de la v12 garde un équivalent : clé, noms, lignée,\n"
     "# messages « la course S ne part qu'après… », graine enfant 0 ; une ligne de GO saine porte `8b1c7511…`, `a54da93e…` et\n"
     "# `4f13647a…`, `6251ab21…` n'est plus requis ; cas ajoutés : reel-v6-2-refusee (en réel, `v6-2` refusée : la course M a tourné\n"
     "# sous le lanceur v10), go-m-seulement-refuse-v6-2-s et go-m-seulement-autorise-v6-2 (ligne de GO portant `8b1c7511…` sans\n"
     "# `a54da93e…` : refusée pour `v6-2-s`, suffisante pour `v6-2`), question-v6-2, sain-v6-2-question et sain-v6-2-s-question\n"
     "# (question par course), sain-v6-2-s-lanceur-attendu et v62-lanceur-v10-en-simulation (en simulation, la course précédente\n"
     "# doit avoir tourné sous ce lanceur-ci), reel-porte-v10-passee, reel-porte-v10-attendu et reel-v6-2-s-precedente-sous-ce-lanceur\n"
     "# (en réel, la porte « course précédente » attend le lanceur v10, `0203f546…` : une copie « réelle » de la v6.2 saine,\n"
     "# LANCEMENT.md et manifeste réécrits, rescellée, passe la porte, et les cas réels de l'étape (0) courent sur `v6-2-s` derrière\n"
     "# elle ; une copie « réelle » citant ce lanceur-ci est refusée) ; la v12 n'a jamais tourné sur le lanceur v11) ; la v12 était\n"
     "# dérivée de la v11 (ba47a625…) par `deriver_essais_pilote4_v12.py` pour le lanceur v10 (objet de la course v6-2 : la\n", 1),
    ("exécutés ; puis v5.3 après la\n# v6.2 saine)", "exécutés ; puis la course S après la\n# v6.2 saine)", 1),
    ("# Usage : bash essais_lanceur_pilote4_v12.sh ", "# Usage : bash essais_lanceur_pilote4_v13.sh ", 1),
    ('echo "== cas sains : v6.2 complète (essais du noyau exécutés), puis v5.3 après la v6.2 saine ; rondes de conception et quatre générations =="',
     'echo "== cas sains : v6.2 complète (essais du noyau exécutés), puis la course S (v6-2-s, la même v6.2.1 sur la question S) après la v6.2 saine ; rondes de conception et quatre générations =="', 1),
]
for ancien, nouveau, n in globaux:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
# 2. Cas ajoutés et cas réécrits, ancrés sur le texte obtenu
ancres = [
    # question par course et lanceur attendu, vérifiés sur les deux courses saines
    ('verifier sain-v6-2-s-minuteur "STOP non posé" "$VS/LANCEMENT.md"\n',
     'verifier sain-v6-2-s-minuteur "STOP non posé" "$VS/LANCEMENT.md"\n'
     'verifier sain-v6-2-s-question "question (v6-2-s) : sha256 a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289" "$VS/LANCEMENT.md"\n'
     'verifier sain-v6-2-question "question (v6-2) : sha256 8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd" "$V6/LANCEMENT.md"\n'
     'verifier sain-v6-2-s-lanceur-attendu "lanceur attendu $(basename "$LANCEUR") (${H:0:8}…)" "$VS/LANCEMENT.md"\n', 1),
    # ligne de GO ne portant qu'une question : suffisante pour la course de cette question, refusée pour l'autre
    ('cas go-v53-seulement-autorise-v53 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-2-s "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-v53-seulement.md"\n',
     'cas go-s-seulement-autorise-v6-2-s "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-2-s "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-s-seulement.md"\n'
     'cas go-m-seulement-autorise-v6-2 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-2 "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-m-seulement.md"\n', 1),
    ('cas go-v53-seulement-refuse-v6-2 "l\'empreinte de l\'organisme 4f13647a… et celle du texte scellé" -- MODE=simulation COURSE=v6-2 "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-v53-seulement.md"\n'
     'cas go-autre-question "l\'empreinte de la question 8b1c7511…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"\n',
     'cas go-s-seulement-refuse-v6-2 "l\'empreinte de la question 8b1c7511…" -- MODE=simulation COURSE=v6-2 "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-s-seulement.md"\n'
     'cas go-m-seulement-refuse-v6-2-s "l\'empreinte de la question a54da93e…" -- MODE=simulation COURSE=v6-2-s "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-m-seulement.md"\n'
     'cas go-autre-question "l\'empreinte de la question a54da93e…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"\n', 1),
    # artefact sur la question, pour chaque course
    ('cas question "empreinte de la question ≠ 8b1c7511…" -- MODE=simulation ESSAI_ARTEFACT=question "${SAIN[@]}"\n',
     'cas question-v6-2-s "empreinte de la question ≠ a54da93e…" -- MODE=simulation ESSAI_ARTEFACT=question "${SAIN[@]}"\n'
     'cas question-v6-2 "empreinte de la question ≠ 8b1c7511…" -- MODE=simulation COURSE=v6-2 ESSAI_ARTEFACT=question "${SAIN[@]}"\n', 1),
    # en simulation, la course précédente doit avoir tourné sous ce lanceur-ci, pas sous le v10
    ('cas v62-graine-vide "graine de v6.2 au manifeste illisible ou vide (None)" -- "${VSC[@]}" PRECEDENTE_V62="$d"\n',
     'cas v62-graine-vide "graine de v6.2 au manifeste illisible ou vide (None)" -- "${VSC[@]}" PRECEDENTE_V62="$d"\n'
     'd="$(copie_v62 lanceur-v10)"; sed -i "s/^- lanceur : .*, sha256 $H\\$/- lanceur : lancer_pilote4_gemini_v10.sh, sha256 ' + SHA_LANCEUR_V10 + '/" "$d/LANCEMENT.md"; refaire_empreintes "$d"\n'
     'cas v62-lanceur-v10-en-simulation "v6.2 n a pas tourné sous ce lanceur" -- "${VSC[@]}" PRECEDENTE_V62="$d"\n', 1),
    # mode réel : v6-2 refusée juste après le case ; étape (0) essayée sur v6-2-s derrière une v6.2 « réelle » sous le lanceur v10
    ('echo "== mode réel (copie du dépôt sous /root) : refus à l\'étape (0), avant tout appel =="\n'
     'REEL=(MODE=reel COURSE=v6-2 PILOTE_RACINE=- DEPOT="$DEPOT_ROOT" "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai)\n'
     'cas reel-sans-reference "REFERENCE_M non défini" -- "${REEL[@]}"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n'
     'cas reel-reference-hors-root "REFERENCE_M $M_REF hors de /root et de /home" -- "${REEL[@]}" REFERENCE_M="$M_REF"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n'
     'RR="$(dirname "$DEPOT_ROOT")/references-m"; rm -rf "$RR"; mkdir -p "$RR"; cp -a "$M_REF" "$RR/autre-nom-v1"\n'
     'cas reel-reference-nom "nom autre que pilote2-gemini-v5-2-1-maieutique-v1[-tentativeN]" -- "${REEL[@]}" REFERENCE_M="$RR/autre-nom-v1"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n'
     'cp -a "$M_REF" "$RR/pilote2-gemini-v5-2-1-maieutique-v1"\n'
     'cas reel-reference-simulee "M n a pas tourné en réel" -- "${REEL[@]}" REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n'
     'cp -a "$M_REF" "$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"\n'
     'cas reel-reference-tentative-simulee "M n a pas tourné en réel" -- "${REEL[@]}" COURSE=v6-2 REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes" "$RR"\n',
     'echo "== mode réel (copie du dépôt sous /root) : COURSE=v6-2 refusée juste après le case (la course M a tourné sous le lanceur v10, R-490) =="\n'
     'REEL_BASE=(MODE=reel PILOTE_RACINE=- DEPOT="$DEPOT_ROOT" "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai)\n'
     'cas reel-v6-2-refusee "COURSE=v6-2 en mode réel : la course M a tourné sous le lanceur v10" -- "${REEL_BASE[@]}" COURSE=v6-2\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n'
     'echo "== course v6.2 précédente « réelle » pour les essais en mode réel de la course S : copie de la v6.2 saine dont le LANCEMENT.md dit « reel » et cite le lanceur v10 (0203f546…), dont le manifeste dit reel et le GO (rien d\'autre), rescellée ; posée seule dans le dossier des pilotes de la copie sous /root avant chaque cas =="\n'
     'V62_REEL="$E/v62-reel/pilote4-gemini-v6-2-v1"; rm -rf "$E/v62-reel"; mkdir -p "$E/v62-reel"; cp -a "$V62" "$V62_REEL"\n'
     "sed -i -e 's/^# Lancement du pilote pilote4-gemini-v6-2-v1 (simulation, tentative 1)$/# Lancement du pilote pilote4-gemini-v6-2-v1 (reel, tentative 1)/' \\\n"
     '  -e "s/^- lanceur : .*, sha256 $H\\$/- lanceur : lancer_pilote4_gemini_v10.sh, sha256 ' + SHA_LANCEUR_V10 + '/" "$V62_REEL/LANCEMENT.md"\n'
     'extrait_altere "$V62_REEL" \'x["manifeste"]["reel"] = True; x["manifeste"]["go_id"] = "GO-2026-10-25-02"\'; refaire_empreintes "$V62_REEL"\n'
     'P_REEL="$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1"\n'
     'poser_v62_reel() {  # la copie « réelle », seule dans le dossier des pilotes de la copie sous /root\n'
     '  rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"; mkdir -p "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"; cp -a "$V62_REEL" "$P_REEL"\n'
     '}\n'
     'echo "== mode réel, course S derrière la v6.2 précédente « réelle » (copie du dépôt sous /root) : porte (0 bis) passée, refus à l\'étape (0), avant tout appel =="\n'
     'REEL=("${REEL_BASE[@]}" COURSE=v6-2-s PRECEDENTE_V62="$P_REEL")\n'
     'poser_v62_reel\n'
     'cas reel-sans-reference "REFERENCE_M non défini" -- "${REEL[@]}"\n'
     'verifier reel-porte-v10-passee "; v6.2 saine : g000 à g003 OK" "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1/LANCEMENT.md"\n'
     'verifier reel-porte-v10-attendu "lanceur attendu lancer_pilote4_gemini_v10.sh (0203f546…)" "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1/LANCEMENT.md"\n'
     'poser_v62_reel\n'
     'cas reel-reference-hors-root "REFERENCE_M $M_REF hors de /root et de /home" -- "${REEL[@]}" REFERENCE_M="$M_REF"\n'
     'poser_v62_reel\n'
     'RR="$(dirname "$DEPOT_ROOT")/references-m"; rm -rf "$RR"; mkdir -p "$RR"; cp -a "$M_REF" "$RR/autre-nom-v1"\n'
     'cas reel-reference-nom "nom autre que pilote2-gemini-v5-2-1-maieutique-v1[-tentativeN]" -- "${REEL[@]}" REFERENCE_M="$RR/autre-nom-v1"\n'
     'poser_v62_reel\n'
     'cp -a "$M_REF" "$RR/pilote2-gemini-v5-2-1-maieutique-v1"\n'
     'cas reel-reference-simulee "M n a pas tourné en réel" -- "${REEL[@]}" REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1"\n'
     'poser_v62_reel\n'
     'cp -a "$M_REF" "$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"\n'
     'cas reel-reference-tentative-simulee "M n a pas tourné en réel" -- "${REEL[@]}" COURSE=v6-2-s REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes" "$RR"\n', 1),
    # mode réel, porte (0 bis) : une copie « réelle » qui cite ce lanceur-ci (et non le v10) est refusée
    ('cas reel-v6-2-s-precedente-simulee "v6.2 n a pas tourné en réel" -- "${REEL_S[@]}" PRECEDENTE_V62="$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n',
     'cas reel-v6-2-s-precedente-simulee "v6.2 n a pas tourné en réel" -- "${REEL_S[@]}" PRECEDENTE_V62="$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n'
     'V62_REEL_CE="$E/v62-reel-ce-lanceur/pilote4-gemini-v6-2-v1"; rm -rf "$E/v62-reel-ce-lanceur"; mkdir -p "$E/v62-reel-ce-lanceur"; cp -a "$V62" "$V62_REEL_CE"\n'
     "sed -i 's/^# Lancement du pilote pilote4-gemini-v6-2-v1 (simulation, tentative 1)$/# Lancement du pilote pilote4-gemini-v6-2-v1 (reel, tentative 1)/' \"$V62_REEL_CE/LANCEMENT.md\"\n"
     'extrait_altere "$V62_REEL_CE" \'x["manifeste"]["reel"] = True; x["manifeste"]["go_id"] = "GO-2026-10-25-02"\'; refaire_empreintes "$V62_REEL_CE"\n'
     'mkdir -p "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"; cp -a "$V62_REEL_CE" "$P_REEL"\n'
     'cas reel-v6-2-s-precedente-sous-ce-lanceur "v6.2 n a pas tourné sous ce lanceur" -- "${REEL_S[@]}" PRECEDENTE_V62="$P_REEL"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n', 1),
]
for ancien, nouveau, n in ancres:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
# 3. Restes interdits et présences attendues. `v5-3` ne subsiste que dans l'en-tête (l'historique de la v11, cas
#    sain-v5-3-graine, et « à la place de la clé `v5-3` ») ; `v5.3` dans l'historique de la v11 et dans « la v5.3 ne court
#    pas » ; `6251ab21` dans « n'est plus requis » ; le lanceur v10 dans les deux copies qui le citent et le cas qui l'attend.
for motif, permis in (("v5-3", 2), ("sain-v5-3-graine", 1), ("v5.3", 2), ("la v5.3 ne court pas", 1), ("6251ab21", 1), ("`6251ab21…` n'est plus requis", 1),
                      ("G_53", 0), ("V5C", 0), ("V53", 0), ("22 fichiers", 0), ("au lieu de 22", 0), ("go-v53-", 0), ("dep-v53-", 0), ("-v53", 0),
                      ("lancer_pilote4_gemini_v10.sh", 3), (SHA_LANCEUR_V10, 2), ("0203f546…", 3),
                      ("go-s-seulement.md", 3), ("go-m-seulement.md", 3), ("go-autre-question.md", 2),
                      ("a54da93e", 14), ("8b1c7511", 13), ("4f13647a", 15), ("v6-2-s", 76),
                      ("poser_v62_reel", 6), ("REEL_BASE", 3), ("V62_REEL=", 1), ("V62_REEL_CE=", 1),
                      ("essais_lanceur_pilote4_v13.sh", 1), ("deriver_essais_pilote4_v13.py", 1)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")
