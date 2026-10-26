"""Dérive le lanceur v11 du quatrième pilote descriptif du lanceur v10 (`lancer_pilote4_gemini_v10.sh`, 0203f546…), par
remplacements exacts au nombre attendu : la seconde course n'est plus la v5.3 (« la v5.3 ne court pas », décision de Lazar
du 26 octobre 2026, 04:13 UTC, R-492) mais **le même organisme, la v6.2.1** (commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`,
arbre `4f13647a…`, 26 fichiers), **sur la question S** (`question-apprendre-structure-entrainement-generations-organismes-v2.md`,
commit `4772b525081342a6a30ba8823733aa5770a888a8`, sha256 `a54da93e…`) : clé de course `v6-2-s`, nom `pilote4-gemini-v6-2-s-v1`,
lignée `gemini-organisme-v6-2-s`, graine enfant 0. La question devient une constante par course (M `8b1c7511…` pour `v6-2`,
S `a54da93e…` pour `v6-2-s`). En réel, `COURSE=v6-2` est refusée juste après le `case` (la course M a tourné sous le lanceur
v10, R-490) ; en simulation elle reste permise (la batterie en a besoin pour produire la course précédente). La porte
« course précédente » attend, en réel, le lanceur v10 (`lancer_pilote4_gemini_v10.sh`, 0203f546…) et, en simulation, ce
lanceur-ci (deux variables, LANCEUR_V62_NOM et LANCEUR_V62_SHA, définies avant la porte et passées au contrôle Python) ; elle
et le contrôle de la graine de la course précédente sont conditionnés sur `v6-2-s`. Tout le reste est le v10.

Usage : python3 -I deriver_lanceur_pilote4_v11.py LANCEUR_V10 SORTIE
Refuse si l'empreinte du lanceur v10 n'est pas 0203f546…, si une occurrence n'est pas au nombre attendu, si un reste interdit
subsiste (v5.3 hors de la phrase « la v5.3 ne court pas », `v5-3` hors des chemins permis du troisième pilote, `6251ab21`,
`4ecba58`), ou si SORTIE existe (R12).
"""
import hashlib, pathlib, sys

SHA_V10 = "0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V10:
    sys.exit("refus : le lanceur source n'est pas la v10 0203f546…")
t = b.decode("utf-8")
remplacements = [
    # en-tête : objet du pilote, dérivation v11
    ("# Lanceur du quatrième pilote descriptif « organismes assistés de Gemini, v6.2 puis v5.3, chacun seul, sur la banque\n"
     "# `confrontation-v3` (identifiants opaques), quatre générations notées, 6 rondes de conception au plus avant g000 (l'organisme déclare lui-même la fin de sa conception, `fin_conception.json`), 3 USD au plus par ronde, question M à g001 »,\n"
     "# une course en un ou plusieurs segments (COURSE=v6-2, puis COURSE=v5-3 ; SEGMENT=1, 2, …) — v10 : le lanceur v9\n",
     "# Lanceur du quatrième pilote descriptif « organisme assisté de Gemini, la v6.2.1, seule, sur la question M puis sur la question S, sur la banque\n"
     "# `confrontation-v3` (identifiants opaques), quatre générations notées, 6 rondes de conception au plus avant g000 (l'organisme déclare lui-même la fin de sa conception, `fin_conception.json`), 3 USD au plus par ronde, question de la course (M, puis S) à g001 »,\n"
     "# une course en un ou plusieurs segments (COURSE=v6-2 sous le lanceur v10, puis COURSE=v6-2-s sous celui-ci ; SEGMENT=1, 2, …) — v11 : le lanceur v10\n"
     "# (0203f546…) par `deriver_lanceur_pilote4_v11.py` (seconde course : le même organisme, la v6.2.1, sur la question S, clé\n"
     "# `v6-2-s`, nom `pilote4-gemini-v6-2-s-v1`, lignée `gemini-organisme-v6-2-s`, graine enfant 0 ; la question devient une\n"
     "# constante par course ; en réel, ce lanceur refuse `v6-2` (la course M a tourné sous le lanceur v10, R-490) et la porte\n"
     "# « course précédente » attend le lanceur v10 ; décision de Lazar du 26 octobre 2026, 04:13 UTC, R-492 ; écart consigné\n"
     "# dans `diff-lanceur-pilote4-v10-vers-v11.txt`), la v10 dérivée du lanceur v9\n", 1),
    ("00:18 Paris, « je veux la v6.2 en premier » : la v6.2 d'abord, puis la v5.3 après une v6.2 saine — porte « v6.2\n",
     "00:18 Paris, « je veux la v6.2 en premier » : la v6.2 d'abord, puis la seconde course après une v6.2 saine — porte « v6.2\n", 1),
    ("la porte « v6.2 précédente » (v9 ; « v5.3 précédente » jusqu'au v8)\n",
     "la porte « v6.2 précédente » (v9 ; dans l'ordre inverse jusqu'au v8)\n", 1),
    ("# Objets : v5.3 = `canal/gemini-organisme-v5-3`, commit `4ecba58`, dossier `organisme/`, arbre `6251ab21…`, 22 fichiers ;\n"
     "# v6.2 = la v6.2.1 :",
     "# Objet des deux courses (M, puis S) : la v6.2.1, dossier `organisme/` — la v5.3 ne court pas (décision de Lazar, R-492), et la clé\n"
     "# `v6-2` ne sert plus qu'en simulation (la course M de ce pilote a tourné sous `lancer_pilote4_gemini_v10.sh`, R-490).\n"
     "# v6.2 = la v6.2.1 :", 1),
    # en-tête : usage
    ("#   MODE=reel COURSE=v6-2 DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO_USD=… \\\n"
     "#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=… CLE_ANTHROPIC=NOM CLE_GEMINI=NOM \\\n"
     "#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> [SEGMENT=1] \\\n"
     "#       bash lancer_pilote4_gemini_v10.sh\n"
     "#   MODE=reel COURSE=v5-3 … PRECEDENTE_V62=<dossier du pilote de la course v6.2 de ce pilote, dans la même copie> (même forme)\n",
     "#   MODE=reel COURSE=v6-2-s DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO_USD=… \\\n"
     "#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=… CLE_ANTHROPIC=NOM CLE_GEMINI=NOM \\\n"
     "#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> \\\n"
     "#       PRECEDENTE_V62=<dossier de la course M de ce pilote, pilote4-gemini-v6-2-v1[-tentativeN], dans la même copie> [SEGMENT=1] \\\n"
     "#       bash lancer_pilote4_gemini_v11.sh\n"
     "#   MODE=reel COURSE=v6-2 : refusée par ce lanceur (la course M de ce pilote a tourné sous le lanceur v10, R-490) ; MODE=simulation COURSE=v6-2 : permise\n", 1),
    # clé de course
    ('COURSE="${COURSE:?COURSE=v5-3 ou COURSE=v6-2}"\n', 'COURSE="${COURSE:?COURSE=v6-2-s ou COURSE=v6-2}"\n', 1),
    # question par course, branche v6-2-s, refus de v6-2 en réel
    ("# Question M v2 épurée (la même que celle de la course M du second pilote), pour les deux courses\n"
     "COMMIT_QUESTION=a15809b816b6c967b6c3cf21877e350bfe676dca\n"
     "CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-gemini-maieutique-vs-coercition-organismes-v2.md\n"
     "SHA_QUESTION=8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd\n"
     'case "$COURSE" in\n'
     "  v5-3)\n"
     '    NOM="pilote4-gemini-v5-3-v1"; INDICE_GRAINE=0\n'
     "    COMMIT_ORGANISME=4ecba58bcaa7dc3abe82c54fc38ee7285620bdf6\n"
     "    ARBRE_ORGANISME=6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753\n"
     "    N_FICHIERS_ORGANISME=22\n"
     '    LIGNEE="gemini-organisme-v5-3";;\n'
     "  v6-2)\n"
     '    NOM="pilote4-gemini-v6-2-v1"; INDICE_GRAINE=1\n'
     "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n"
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n"
     "    N_FICHIERS_ORGANISME=26\n"
     '    LIGNEE="gemini-organisme-v6-2";;\n'
     '  *) refus_tot "COURSE inconnue : $COURSE (v5-3 ou v6-2)";;\n'
     "esac\n",
     "# Question par course (v11, R-492) : M v2 épurée (la même que celle de la course M du second pilote) pour `v6-2` ; S v2 (la\n"
     "#   question de la course S du second pilote) pour `v6-2-s` ; même organisme, la v6.2.1, pour les deux courses\n"
     'case "$COURSE" in\n'
     "  v6-2-s)\n"
     '    NOM="pilote4-gemini-v6-2-s-v1"; INDICE_GRAINE=0\n'
     "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n"
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n"
     "    N_FICHIERS_ORGANISME=26\n"
     '    LIGNEE="gemini-organisme-v6-2-s"\n'
     "    COMMIT_QUESTION=4772b525081342a6a30ba8823733aa5770a888a8\n"
     "    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-apprendre-structure-entrainement-generations-organismes-v2.md\n"
     "    SHA_QUESTION=a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289;;\n"
     "  v6-2)\n"
     '    NOM="pilote4-gemini-v6-2-v1"; INDICE_GRAINE=1\n'
     "    COMMIT_ORGANISME=7ea32705c5437d91ed071dd95fb3209bb0b0035e\n"
     "    ARBRE_ORGANISME=4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d\n"
     "    N_FICHIERS_ORGANISME=26\n"
     '    LIGNEE="gemini-organisme-v6-2"\n'
     "    COMMIT_QUESTION=a15809b816b6c967b6c3cf21877e350bfe676dca\n"
     "    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-gemini-maieutique-vs-coercition-organismes-v2.md\n"
     "    SHA_QUESTION=8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd;;\n"
     '  *) refus_tot "COURSE inconnue : $COURSE (v6-2-s ou v6-2)";;\n'
     "esac\n"
     "# v11 (R-492) : en réel, ce lanceur ne lance que la course S ; la course M de ce pilote (`v6-2`) a tourné sous le lanceur v10\n"
     "#   (R-490) ; en simulation, `v6-2` reste permise (la batterie en a besoin pour produire la course précédente)\n"
     'if [ "$MODE" = reel ] && [ "$COURSE" = v6-2 ]; then refus_tot "COURSE=v6-2 en mode réel : la course M a tourné sous le lanceur v10 (R-490) ; ce lanceur v11 ne lance en réel que v6-2-s (R-492)"; fi\n', 1),
    # porte « course précédente » : commentaire, lanceur attendu selon le mode, condition sur v6-2-s, messages
    ("# 0 bis (avant l'étape 0, pour que ses refus en réel soient essayables). Course v5.3 : ne part qu'après une course v6.2\n"
     "#        finie, fermée et saine (v9 : ordre des courses inversé, décision de Lazar du 26 octobre 2026, 00:18 Paris,\n"
     "#        « je veux la v6.2 en premier » ; P3C1-01 : « mêmes règles de refus que pour M et S », R-440) — la liste close de l'étape (0), paramétrée pour la v6.2 et ce lanceur (nom et empreinte de ce\n"
     "#        lanceur, course `v6-2`, nom `pilote4-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2`, GO de ce\n"
     "#        pilote) ; la graine de v6.2 au manifeste est comparée, à l'étape (2), à celle de ce texte ; la ligne de dépense\n"
     "#        de v5.3 porte aussi les 16 premiers caractères de l'empreinte des empreintes de v6.2\n"
     'EMP_V62=""\n'
     'if [ "$COURSE" = v5-3 ] && { [ "$MODE" = reel ] || [ -n "${PRECEDENTE_V62:-}" ]; }; then\n'
     '  [ -n "${PRECEDENTE_V62:-}" ] || refus "PRECEDENTE_V62 non défini : v5.3 ne part qu\'après une course v6.2 saine (dossier du pilote de la course v6.2)"\n'
     '  SV="$PRECEDENTE_V62"\n'
     '  [ -d "$SV" ] || refus "PRECEDENTE_V62 $SV absent : v5.3 ne part qu\'après v6.2"\n',
     "# 0 bis (avant l'étape 0, pour que ses refus en réel soient essayables). Course S (`v6-2-s`) : ne part qu'après une course v6.2\n"
     "#        (la course M de ce pilote, `v6-2`) finie, fermée et saine (v9 : ordre des courses inversé, décision de Lazar du 26 octobre 2026, 00:18 Paris,\n"
     "#        « je veux la v6.2 en premier » ; P3C1-01 : « mêmes règles de refus que pour M et S », R-440) — la liste close de l'étape (0), paramétrée pour la v6.2 et le lanceur attendu (v11 : en réel, le\n"
     "#        lanceur v10, sous lequel la course M a tourné, R-490 ; en simulation, ce lanceur-ci, pour que la batterie produise la course\n"
     "#        précédente avec le lanceur sous essai), course `v6-2`, nom `pilote4-gemini-v6-2-v1`, lignée `gemini-organisme-v6-2`, GO de ce\n"
     "#        pilote) ; la graine de v6.2 au manifeste est comparée, à l'étape (2), à celle de ce texte ; la ligne de dépense\n"
     "#        de la course S porte aussi les 16 premiers caractères de l'empreinte des empreintes de v6.2\n"
     'EMP_V62=""\n'
     'if [ "$MODE" = reel ]; then LANCEUR_V62_NOM=lancer_pilote4_gemini_v10.sh; LANCEUR_V62_SHA=0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952\n'
     'else LANCEUR_V62_NOM="$(basename "$0")"; LANCEUR_V62_SHA="$SHA_LANCEUR"; fi\n'
     'if [ "$COURSE" = v6-2-s ] && { [ "$MODE" = reel ] || [ -n "${PRECEDENTE_V62:-}" ]; }; then\n'
     '  [ -n "${PRECEDENTE_V62:-}" ] || refus "PRECEDENTE_V62 non défini : la course S ne part qu\'après une course v6.2 saine (dossier du pilote de la course v6.2)"\n'
     '  SV="$PRECEDENTE_V62"\n'
     '  [ -d "$SV" ] || refus "PRECEDENTE_V62 $SV absent : la course S ne part qu\'après v6.2"\n', 1),
    ('refus "empreintes de v6.2 absentes : v5.3 ne part qu\'après une course v6.2 finie et fermée"\n',
     'refus "empreintes de v6.2 absentes : la course S ne part qu\'après une course v6.2 finie et fermée"\n', 1),
    ('\' "$SV" "$SHA_LANCEUR" "gemini-organisme-v6-2" "$MODE" "$GO_ID" "$(basename "$0")" "v6-2" "pilote4-gemini-v6-2-v1")" || refus "v5.3 ne part pas : issue de v6.2 hors de la liste saine ($issue_v62) — décision de Lazar requise"\n',
     '\' "$SV" "$LANCEUR_V62_SHA" "gemini-organisme-v6-2" "$MODE" "$GO_ID" "$LANCEUR_V62_NOM" "v6-2" "pilote4-gemini-v6-2-v1")" || refus "la course S ne part pas : issue de v6.2 hors de la liste saine ($issue_v62) — décision de Lazar requise"\n', 1),
    ('  note "- course v6.2 précédente : $SV ; $issue_v62 ; empreintes de v6.2 vérifiées (EMPREINTES-pilote-v1.txt, sha256 $EMP_V62)"\n',
     '  note "- course v6.2 précédente : $SV ; $issue_v62 ; lanceur attendu $LANCEUR_V62_NOM (${LANCEUR_V62_SHA:0:8}…) ; empreintes de v6.2 vérifiées (EMPREINTES-pilote-v1.txt, sha256 $EMP_V62)"\n', 1),
    # contrôle de la graine de la course précédente
    ('  if [ "$COURSE" = v5-3 ] && [ -n "${GRAINE_V62_MANIFESTE:-}" ]; then\n',
     '  if [ "$COURSE" = v6-2-s ] && [ -n "${GRAINE_V62_MANIFESTE:-}" ]; then\n', 1),
    # étape 3 : commentaire
    ("# 3. Organisme de la course (v5.3 ou v6.2, dossier organisme/ seul) et question, extraits des commits cités, vérifiés\n",
     "# 3. Organisme de la course (la v6.2.1 pour les deux courses, dossier organisme/ seul) et question (par course), extraits des commits cités, vérifiés\n", 1),
    # ligne de dépense
    ('refus "la ligne de dépense de v5.3 ne porte pas l\'empreinte des empreintes de v6.2 (${EMP_V62:0:16}…), écrite après la fin de v6.2"\n',
     'refus "la ligne de dépense de la course S ne porte pas l\'empreinte des empreintes de v6.2 (${EMP_V62:0:16}…), écrite après la fin de v6.2"\n', 1),
]
for ancien, nouveau, n in remplacements:
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)
# Restes interdits et présences attendues. `v5-3` ne subsiste que dans les chemins permis du troisième pilote
# (`pilote3-gemini-organisme-v5-3-v6…`, PERMIS_APRES_CODE, trois fois) ; `v5.3` seulement dans « la v5.3 ne court pas ».
for motif, permis in (("v5-3", 3), ("v5-3-v6", 3), ("v5.3", 1), ("la v5.3 ne court pas", 1),
                      ("6251ab21", 0), ("4ecba58", 0), ('"gemini-organisme-v5-3"', 0), ("pilote4-gemini-v5-3-v1", 0),
                      ("a54da93e", 1), ("8b1c7511", 1), ("4772b525081342a6a30ba8823733aa5770a888a8", 1), ("a15809b816b6c967b6c3cf21877e350bfe676dca", 1),
                      ("7ea32705c5437d91ed071dd95fb3209bb0b0035e", 2), ("4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d", 2),
                      ("N_FICHIERS_ORGANISME=26", 2), ("N_FICHIERS_ORGANISME=22", 0),
                      ("COMMIT_QUESTION=", 3), ("CHEMIN_QUESTION=", 2), ("SHA_QUESTION=", 2),
                      ("lancer_pilote4_gemini_v10.sh", 2), ("lancer_pilote4_gemini_v11.sh", 1), ("0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952", 1),
                      ("LANCEUR_V62_NOM", 4), ("LANCEUR_V62_SHA", 4), ("SHA_LANCEUR", 6), ("PRECEDENTE_V62", 9), ("GRAINE_V62_MANIFESTE", 7),
                      ('"$COURSE" = v6-2-s', 2), ('"$COURSE" = v6-2 ]', 1), ("deriver_lanceur_pilote4_v11.py", 1), ("diff-lanceur-pilote4-v10-vers-v11.txt", 1)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"lanceur écrit : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")
