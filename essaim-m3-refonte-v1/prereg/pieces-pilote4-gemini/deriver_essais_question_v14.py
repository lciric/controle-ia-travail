"""Dérive la batterie d'essais v14 du lanceur des deux courses à question (`essais_lanceur_question_v14.sh`) de la
batterie v13 du pilote 4 (`essais_lanceur_pilote4_v13.sh`, 7b0a9bb0…), pour le lanceur v12 (`lancer_courses_question_v12.sh`) :
remplacements exacts au nombre attendu, et blocs réécrits ou retirés par des ancres dont l'empreinte est vérifiée (texte
v1, table de correspondance ; brief de conv-audit du 26 octobre 2026). Ce qui change :
- clés : `v6-2-s` → `maieutique` (enfant 0, course par défaut des cas), `v6-2` → `audit` (enfant 1) ; noms
  `course-maieutique-gemini-v6-2-v1`, `course-audit-gemini-v6-2-v1` ; TEXTE et TEXTE_SHA256 à la place de PREREG ; GO_ID par
  course, posé par `cas` (05 ; 04 et la pièce de dépense `td-sain-audit.json` quand la course est `audit`) ; lignes de GO
  d'essai à la forme de la ligne d'extension (`ligne_go`), les deux courses dans le même registre ; lignes de dépense à la
  forme `| date | nom | GO | 75 USD au pire cas | empreintes de M … |` ;
- retirés : la porte « course v6.2 précédente » (v62-*, seg-v62-*, seg-v6-2-s-porte-saine, seg-clore-v62-refusee,
  reel-v6-2-s-*, copies « réelles ») ;
- ajoutés ou renommés : cle-ancienne-refusee (et -v6-2, reel-cle-ancienne-*), go-id-forme, reel-sans-go-id,
  reel-journal-garde-essai, texte-* (dont texte-sans-ligne-de-l-autre-course), question-empreinte-autre (artefact
  question-base), question-servie-alteree, annexe-absente, annexe-alteree, annexe-artefacts-sans-effet-maieutique,
  go-maieutique-seulement-*, go-audit-seulement-*, go-questions-croisees, depense-ancienne-forme, sain-audit-question-servie
  (composé recalculé ici), sain-*-garde, porte « précédente » absente (sain-maieutique avec PRECEDENTE_V62 ignorée,
  reel-sans-reference sans elle), garde-refus-question-sain, garde-refus-question-ligne-incomplete,
  garde-refus-question-artefact, -fin-surete, -monoculture-analytique (journaux synthétiques lus par le veilleur,
  ESSAI_JOURNAL_GARDE : arrêt sous 10 s, ligne écrite, pièce poussée, g001 jamais archivée, SEGMENT=2 refusé).

Usage : python3 -I deriver_essais_question_v14.py ESSAIS_V13 SORTIE
Refuse si l'empreinte de la batterie v13 n'est pas 7b0a9bb0…, si une occurrence n'est pas au nombre attendu, si un bloc
réécrit n'a pas l'empreinte attendue, si un reste interdit subsiste, ou si SORTIE existe (R12).
"""
import hashlib, pathlib, re, sys

SHA_V13 = "7b0a9bb0f7637480c19acb06138034582c8f69d2502cd3c483318f43f0f1e388"
src, sortie = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = src.read_bytes()
if hashlib.sha256(b).hexdigest() != SHA_V13:
    sys.exit("refus : la batterie source n'est pas la v13 7b0a9bb0…")
t = b.decode("utf-8")
Z64 = "0" * 64
Q_M = "1d29fbecd52b1dfc94410e117f786811067f86f3cce24c4c54bbe424e480e3a3"
Q_A = "998960b8d101d5013c498d6fcf225277ba17d20741825ad136381892c05cfd0e"   # question « audit » v3 (commit ad23e9ae, R-518) ; la v1 dd2c1016… et la v2 ec3abf28… ne servent plus
Q_A_V2 = "ec3abf2880bdb52fd6193a1994893a0c380c3557a70c94b8f20749220447c4a4"   # question « audit » v2 (commit 9417652a) : ne sert plus
COMMIT_DEF = "ad23e9ae07588ed701a70b9b5f4bf379ca079953"   # `main` des paramètres définitifs (question v3 et annexe, R-518)
ANNEXE_DEF_CHEMIN = "docs/sources/rapport-consolide-20261026/transcription-expurgee-v2.md"
ANNEXE_DEF_SHA = "c1237687e98db14475336af690986bc08800a85e259d249de4940130245b1a64"   # 37 563 octets, 36 024 caractères


def bloc(nom, debut, fin, sha, nouveau):
    """Remplace le bloc qui va de la ligne commençant par `debut` à la ligne finissant par `fin` (incluse), exactement un,
    d'empreinte `sha`, par `nouveau`."""
    global t
    m = list(re.finditer(re.escape(debut) + r".*?" + re.escape(fin) + r"\n", t, re.S))
    if len(m) != 1:
        sys.exit(f"refus : bloc {nom} : {len(m)} occurrence(s) au lieu de 1")
    ancien = m[0].group(0)
    if hashlib.sha256(ancien.encode("utf-8")).hexdigest() != sha:
        sys.exit(f"refus : bloc {nom} : empreinte {hashlib.sha256(ancien.encode('utf-8')).hexdigest()[:8]}… au lieu de {sha[:8]}…")
    t = t.replace(ancien, nouveau)


def remplacer(ancien, nouveau, n):
    global t
    k = t.count(ancien)
    if k != n:
        sys.exit(f"refus : {k} occurrence(s) au lieu de {n} pour : {ancien[:90]!r}")
    t = t.replace(ancien, nouveau)


# ---- en-tête ----
bloc("en-tête", "# Essais du lanceur du pilote 4 (la v6.2.1 sur la question M", "pour le lanceur v11 (seconde course `v6-2-s` : le même",
     "bd451adfc188627e9c43c93f23165b7261cb275ae4da77a1f1460619851a3215",
     "# Essais du lanceur des deux courses à question de la v6.2.1 (« maieutique », clé `maieutique`, GO-2026-10-26-05 ; « audit », clé `audit`, GO-2026-10-26-04, question v3 servie avec son annexe définitive, la transcription expurgée v2 du rapport consolidé (commit ad23e9ae, R-518) ; banque v3, quatre générations notées, 6 rondes de conception au\n"
     "# plus), v14 : la v13 (7b0a9bb0…) par `deriver_essais_question_v14.py` pour le lanceur v12 (texte v1, table de correspondance ;\n"
     "# brief de conv-audit et ses précisions : bloc de paramètres, question « audit » v3 à `ad23e9ae` et son annexe, paramètres définitifs) : cas\n"
     "# et artefacts adaptés aux deux clés (les clés `v6-2-s` et `v6-2` d'hier deviennent `maieutique`, enfant 0, course par défaut\n"
     "# des cas, des segments, de la fermeture et du mutant ; `audit`, enfant 1, tourne avec une annexe synthétique committée dans la\n"
     "# copie puis retirée de sa tête, donnée au lanceur par ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN, ESSAI_ANNEXE_1_SHA ; noms\n"
     "# `course-maieutique-gemini-v6-2-v1` et `course-audit-gemini-v6-2-v1` ; TEXTE et TEXTE_SHA256 à la place de PREREG ; GO_ID par\n"
     "# course, posé par `cas` : 05, ou 04 avec la pièce de dépense `td-sain-audit` et l'annexe synthétique quand la course est\n"
     "# `audit` ; lignes de GO d'essai à la forme de la ligne d'extension, `ligne_go` ; lignes de dépense à la\n"
     "# forme `| date | nom | GO | 75 USD au pire cas | empreintes de M … |`) ; cas retirés : la porte « course v6.2 précédente »\n"
     "# (v62-*, seg-v62-*, seg-v6-2-s-porte-saine, seg-clore-v62-refusee, reel-v6-2-s-*, copies « réelles ») ; cas ajoutés ou\n"
     "# renommés : cle-ancienne-refusee (et -v6-2, reel-cle-ancienne-*), go-id-forme, reel-sans-go-id, reel-journal-garde-essai,\n"
     "# texte-* (dont texte-sans-ligne-de-l-autre-course), question-empreinte-autre (artefact question-base), question-servie-alteree,\n"
     "# question-v1-refusee, question-v2-refusee, go-question-v1-refuse-audit et go-question-v2-refuse-audit (les questions « audit » v1,\n"
     "# dd2c1016…, et v2, ec3abf28…, ne servent plus), sain-audit sur les paramètres définitifs (question v3 et annexe réelle, sans variable\n"
     "# d'essai ; taille servie vérifiée ≤ 100 000), annexe-empreinte-fausse (annexe réelle, empreinte fausse : refus avant tout appel), annexe-absente,\n"
     "# annexe-alteree, annexe-champs-incomplets, annexe-commit-absent, question-servie-trop-longue (borne du noyau 9beee10b :\n"
     "# 100 000 caractères, question.py ; noyau attendu NOYAU_COMMIT, les copies d'essai à sa tête), audit-sans-annexe-reserve (artefact annexe-vide), reel-annexe-essai, annexe-artefacts-sans-effet-maieutique,\n"
     "# go-maieutique-seulement-* et go-audit-seulement-*, go-questions-croisees, depense-ancienne-forme,\n"
     "# sain-audit-question-servie (composé recalculé ici, avec l'annexe synthétique), sain-*-garde, porte\n"
     "# « précédente » absente (sain-maieutique avec PRECEDENTE_V62 ignorée, reel-sans-reference sans elle), garde-refus-question-sain,\n"
     "# garde-refus-question-ligne-incomplete, garde-refus-question-artefact, -fin-surete, -critique-sans-moissonneur,\n"
     "# -apres-moissonneur, -rang-121, -premiere-caste-apres-moissonneur, -motif-reel-m-complet (arrêts : journaux synthétiques,\n"
     "# ESSAI_JOURNAL_GARDE ; arrêt sous 10 s, ligne écrite, règle consignée, pièce poussée, g001 jamais archivée, SEGMENT=2 refusé) ;\n"
     "# garde-refus-question-tache-refusee, -rang-120, -moissonneur-refuse, -motif-reel-m-avant-question (aucun arrêt : règle de\n"
     "# conv-audit du 26 octobre 2026, le motif réel de g001 de la course M du pilote 4, journal fec0cb82…, 129 appels) ;\n"
     "# la v13 était dérivée de la v12 (27ef4524…) par `deriver_essais_pilote4_v13.py` pour le lanceur v11 (seconde course `v6-2-s` : le même\n")
remplacer("# Usage : bash essais_lanceur_pilote4_v13.sh ", "# Usage : bash essais_lanceur_question_v14.sh ", 1)
# ---- graines : enfant 0 « maieutique », enfant 1 « audit » ----
remplacer('G_S="$("$PY" -I -c \'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[0]', 'G_M="$("$PY" -I -c \'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[0]', 1)
remplacer('G_6="$("$PY" -I -c \'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[1]', 'G_A="$("$PY" -I -c \'import numpy; print(int(numpy.random.SeedSequence(12345).spawn(2)[1]', 1)
# ---- pièces du test de dépense : le GO de la course ----
bloc("td", 'td "$E/entrees/td-sain.json" OK', 'TDS="$E/entrees/td-sain.json $E/entrees/td-echec.json $E/entrees/td-autre-go.json"',
     "3f78dc58485ea543be994a77a7a5febaf8bbc1444f00ce137853e9dc72bd93ba",
     'td "$E/entrees/td-sain.json" OK claude-fable-5-1 0.00058 GO-2026-10-26-05\n'
     'td "$E/entrees/td-sain-audit.json" OK claude-fable-5-1 0.00058 GO-2026-10-26-04\n'
     'td "$E/entrees/td-echec.json" ECHEC_API None 0 GO-2026-10-26-05\n'
     'td "$E/entrees/td-autre-go.json" OK claude-fable-5-1 0.00058 GO-2026-10-25-01\n'
     'td "$E/entrees/td-go-maieutique.json" OK claude-fable-5-1 0.00058 GO-2026-10-26-05   # la pièce de la course « maieutique », présentée à la course « audit »\n'
     'TDS="$E/entrees/td-sain.json $E/entrees/td-sain-audit.json $E/entrees/td-echec.json $E/entrees/td-autre-go.json $E/entrees/td-go-maieutique.json"\n')
bloc("td_noms", "td_noms() {", "json.dump({\"especes\": e, \"go\": \"GO-2026-10-25-02\", \"variables_cles\": {\"anthropic\": sys.argv[2], \"gemini\": sys.argv[3]}}, open(sys.argv[1], \"w\"))' \"$@\"\n}",
     "1c62c65b1de8988036a13dd0fa42068f8c61cfd74ed72ccca2726945413e734a",
     "td_noms() {  # td_noms FICHIER ANTHROPIC GEMINI GO : pièce fraîche avec heures d'appel et noms des variables\n"
     '  "$PY" -I -c \'\n'
     "import datetime, json, sys\n"
     'h = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")\n'
     'e = {k: {"statut": "OK", "modele_servi": m, "cout_usd": 0.0005, "jetons_sortie": 8, "heure_utc": h} for k, m in (("CLAUDE_FABLE_5_1", "claude-fable-5-1"), ("CLAUDE_OPUS_5_5", "claude-opus-5-5"), ("GEMINI_ARGON", "gemini-4-argon"))}\n'
     'json.dump({"especes": e, "go": sys.argv[4], "variables_cles": {"anthropic": sys.argv[2], "gemini": sys.argv[3]}}, open(sys.argv[1], "w"))\' "$@"\n'
     "}\n")
# ---- textes d'essai (un texte, deux lignes de graine) et registres des GO (une ligne par course, forme de la ligne d'extension) ----
bloc("fixtures", 'pr "$E/entrees/prereg-sain.md" "entropie E = $ENTROPIE tirée au scellement', '> "$E/entrees/go-sans-texte.md"',
     "808e4321a6ad9e3a793eb9c30fb817fd8de3ade3e7239f7c8caf1c82318f1a44",
     'pr "$E/entrees/prereg-sain.md" "entropie E = $ENTROPIE tirée au scellement\n'
     "graine de la course maieutique = $G_M\n"
     "graine de la course audit = $G_A\n"
     'lanceur $H"\n'
     'pr "$E/entrees/prereg-graine-hors-entropie.md" "entropie E = $ENTROPIE\n'
     "graine de la course maieutique = 13\n"
     "graine de la course audit = 13\n"
     'lanceur $H"\n'
     'pr "$E/entrees/prereg-lanceur-source.md" "entropie E = $ENTROPIE\n'
     "graine de la course maieutique = $G_M\n"
     "graine de la course audit = $G_A\n"
     'lanceur $H_M"\n'
     'pr "$E/entrees/prereg-marqueur.md" "entropie E = $ENTROPIE\n'
     "graine de la course maieutique = $G_M\n"
     "graine de la course audit = $G_A\n"
     'lanceur $H ; <<EMPREINTE_PIECES>>"\n'
     'pr "$E/entrees/prereg-une-ligne.md" "entropie E = $ENTROPIE\n'
     "graine de la course maieutique = $G_M\n"
     'lanceur $H"\n'
     'SHA_PR="$(cut -d\' \' -f1 < "$E/entrees/prereg-sain.md.sha256")"\n'
     'T16="${SHA_PR:0:16}"   # la ligne de GO porte les 16 premiers caractères de l\'empreinte du texte (le même texte pour les deux GO)\n'
     f"Q_M={Q_M}; Q_A={Q_A}   # empreintes des questions « maieutique » (commit eb03bad5) et « audit » v3 (commit ad23e9ae, R-518)\n"
     "Q_A_V1=dd2c1016e20a4823dcb2ce4c1e94d2c6be7a6962cb52a10ee7ac3b1f7d1203aa   # question « audit » v1 : ne sert plus (R-515, R-516), refusée comme empreinte autre\n"
     f"Q_A_V2={Q_A_V2}   # question « audit » v2 (commit 9417652a) : ne sert plus (R-518), refusée comme empreinte autre\n"
     f"COMMIT_DEF={COMMIT_DEF}; ANNEXE_DEF_CHEMIN={ANNEXE_DEF_CHEMIN}; ANNEXE_DEF_SHA={ANNEXE_DEF_SHA}   # paramètres définitifs de l'annexe (R-518), les mêmes que dans le lanceur\n"
     "ligne_go() {  # ligne_go GO COURSE QUESTION_SHA TEXTE16 [TYPE] : une ligne du registre des GO, à la forme de la ligne d'extension (texte v1, § Plan)\n"
     "  printf '| %s | 2026-10-26 | %s | extension : course « %s » (essai) — la v6.2.1 7ea3270, arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d, sur la question %s (commit eb03bad5) ; banque confrontation-v3 157a2b45… ; texte courses-question-gemini-v6-2-v1.md %s ; lanceur lancer_courses_question_v12.sh %s, noyau 9beee10b | 75 USD au plus | 2026-10-31 | Lazar | R-509 |\\n' \"$1\" \"${5:-calcul}\" \"$2\" \"$3\" \"$4\" \"$H\"\n"
     "}\n"
     '{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_A" "$T16"; } > "$E/entrees/go-sain.md"\n'
     '{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16" essai; ligne_go GO-2026-10-26-04 audit "$Q_A" "$T16" essai; } > "$E/entrees/go-sans-calcul.md"\n'
     '{ ligne_go @@GO_PILOTE4@@ maieutique "$Q_M" "$T16"; ligne_go @@GO_PILOTE4@@ audit "$Q_A" "$T16"; } > "$E/entrees/go-autre-id.md"   # le GO du pilote 4, autre que celui de la course\n'
     'ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16" > "$E/entrees/go-maieutique-seulement.md"\n'
     'ligne_go GO-2026-10-26-04 audit "$Q_A" "$T16" > "$E/entrees/go-audit-seulement.md"\n'
     f'{{ ligne_go GO-2026-10-26-05 maieutique {Z64} "$T16"; ligne_go GO-2026-10-26-04 audit {Z64} "$T16"; }} > "$E/entrees/go-autre-question.md"\n'
     '{ ligne_go GO-2026-10-26-05 maieutique "$Q_A" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_M" "$T16"; } > "$E/entrees/go-questions-croisees.md"\n'
     '{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_A_V1" "$T16"; } > "$E/entrees/go-question-v1.md"   # la ligne du GO 04 porte la question audit v1\n'
     '{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "$T16"; ligne_go GO-2026-10-26-04 audit "$Q_A_V2" "$T16"; } > "$E/entrees/go-question-v2.md"   # la ligne du GO 04 porte la question audit v2\n'
     '{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "(sans le texte)"; ligne_go GO-2026-10-26-04 audit "$Q_A" "(sans le texte)"; } > "$E/entrees/go-sans-texte.md"\n')
# ---- vérificateurs : motif absent ----
remplacer('  else echo "ÉCHEC  $nom : attendu « $attendu »"; fi\n}\n',
          '  else echo "ÉCHEC  $nom : attendu « $attendu »"; fi\n}\n'
          "verifier_absent_texte() {  # verifier_absent_texte NOM MOTIF FICHIER… : le motif ne doit se trouver dans aucun des fichiers\n"
          '  local nom="$1" motif="$2"; shift 2\n'
          "  n=$((n + 1))\n"
          '  if cat "$@" 2>/dev/null | grep -qF -- "$motif"; then echo "ÉCHEC  $nom : « $motif » présent"; else ok=$((ok + 1)); echo "OK     $nom : « $motif » absent"; fi\n'
          "}\n", 1)
# ---- cas : course par défaut « maieutique », GO par course ----
bloc("cas()", "cas() {  # cas NOM ATTENDU -- VAR=VAL…", '  else echo "ÉCHEC  $nom (code $code) : attendu « $attendu » ; erreur : $(tail -2 "$racine/erreur.txt" | tr \'\\n\' \' \')"; fi\n}',
     "35fdc9272e9aa02207d58b4f22329fb123cb4a2aeed9be0f1cdcc0a1e01d217a",
     "cas() {  # cas NOM ATTENDU -- VAR=VAL… (motif cherché dans la sortie d'erreur et LANCEMENT.md) ; COURSE=audit entraîne GO_ID=GO-2026-10-26-04, la pièce de dépense td-sain-audit.json à la place de td-sain.json et, hors du mode réel, l'annexe synthétique (ESSAI_ANNEXE_1_*, que le cas peut redéfinir)\n"
     '  local nom="$1" attendu="$2"; shift 3\n'
     "  n=$((n + 1))\n"
     '  local racine="$E/cas-$nom"; rm -rf "$racine"; mkdir -p "$racine"\n'
     "  # shellcheck disable=SC2086\n"
     "  touch $TDS\n"
     '  local audit="" reel="" a args=()\n'
     '  for a in "$@"; do [ "$a" = COURSE=audit ] && audit=1; [ "$a" = MODE=reel ] && reel=1; done\n'
     '  for a in "$@"; do if [ -n "$audit" ] && [ "$a" = "APPEL_CONTROLE_FICHIER=$E/entrees/td-sain.json" ]; then a="APPEL_CONTROLE_FICHIER=$E/entrees/td-sain-audit.json"; fi; args+=("$a"); done\n'
     '  [ -n "$audit" ] && args=(GO_ID=GO-2026-10-26-04 "${args[@]}")\n'
     '  [ -n "$audit" ] && [ -z "$reel" ] && args=(ESSAI_ANNEXE_1_COMMIT="$ANNEXE_ESSAI_COMMIT" ESSAI_ANNEXE_1_CHEMIN="$ANNEXE_ESSAI_CHEMIN" ESSAI_ANNEXE_1_SHA="$ANNEXE_ESSAI_SHA" "${args[@]}")   # jamais en réel (variables d\'essai interdites)\n'
     '  env -i PATH="$PATH" HOME="$E" LANG=C.UTF-8 DEPOT="$DEPOT" PYTHON="$PY" GRAINE=13 COURSE=maieutique GO_ID=GO-2026-10-26-05 "${args[@]}" \\\n'
     '    PILOTE_RACINE_DEFAUT="$racine" bash -c \'export PILOTE_RACINE="${PILOTE_RACINE-$PILOTE_RACINE_DEFAUT}"; [ "$PILOTE_RACINE" = "-" ] && unset PILOTE_RACINE; exec bash "$0"\' "$LANCEUR" \\\n'
     '    > "$racine/sortie.txt" 2> "$racine/erreur.txt"\n'
     "  local code=$?\n"
     '  local autre_racine=""\n'
     '  for a in "$@"; do case "$a" in PILOTE_RACINE=-) ;; PILOTE_RACINE=*) autre_racine="${a#PILOTE_RACINE=}";; esac; done\n'
     '  local journal; journal="$(cat "$racine"/*/LANCEMENT.md 2>/dev/null; [ -n "$autre_racine" ] && cat "$autre_racine"/*/LANCEMENT.md 2>/dev/null; cat "$racine/erreur.txt")"\n'
     '  if echo "$journal" | grep -qF -- "$attendu"; then ok=$((ok + 1)); echo "OK     $nom (code $code) : « $attendu »"\n'
     '  else echo "ÉCHEC  $nom (code $code) : attendu « $attendu » ; erreur : $(tail -2 "$racine/erreur.txt" | tr \'\\n\' \' \')"; fi\n'
     "}\n")
# ---- lignes de dépense (forme du texte v1) et jeu sain ----
bloc("dépenses et SAIN", "printf '| 2026-10-25 | pilote4-gemini-v6-2-s-v1 | GO-2026-10-25-02 | 60 | après M, empreintes de M %s |", 'RECHARGE_ATTESTEE="essai" REFERENCE_M="$M_REF")',
     "16c530f0527291160aabac9b09bf7ca12d409f0dd43a279197c495bccb9dedc5",
     "printf '| 2026-10-26 | course-maieutique-gemini-v6-2-v1 | GO-2026-10-26-05 | 75 USD au pire cas | empreintes de M %s |\\n| 2026-10-26 | course-audit-gemini-v6-2-v1 | GO-2026-10-26-04 | 75 USD au pire cas | empreintes de M %s |\\n' \"${EMP_M:0:16}\" \"${EMP_M:0:16}\" > \"$E/entrees/dep-sain.md\"\n"
     "printf '| 2026-10-26 | course-maieutique-gemini-v6-2-v1 | GO-2026-10-26-05 | 75 USD au pire cas |\\n| 2026-10-26 | course-audit-gemini-v6-2-v1 | GO-2026-10-26-04 | 75 USD au pire cas |\\n' > \"$E/entrees/dep-sans-empreinte-m.md\"\n"
     "printf '| 2026-10-26 | course-maieutique-gemini-v6-2-v1 | @@GO_PILOTE4@@ | 75 USD au pire cas | empreintes de M %s |\\n' \"${EMP_M:0:16}\" > \"$E/entrees/dep-absente.md\"\n"
     "printf '| 2026-10-25 | @@NOM_PILOTE4_M@@ | @@GO_PILOTE4@@ | 75 USD au pire cas | après M, empreintes de M %s |\\n| 2026-10-25 | @@NOM_PILOTE4_S@@ | @@GO_PILOTE4@@ | 75 USD au pire cas | après M et v6.2, empreintes de M %s, de v6.2 0000000000000000 |\\n' \"$EMP_M\" \"$EMP_M\" > \"$E/entrees/dep-ancienne-forme.md\"   # forme du pilote 4 : noms et GO d'hier\n"
     'SAIN=(REGISTRE_GO_SOURCE="$E/entrees/go-sain.md" DEPENSES_SOURCE="$E/entrees/dep-sain.md" RESTE_GO_USD=150\n'
     '      APPEL_CONTROLE_FICHIER="$E/entrees/td-sain.json" RECHARGE_ATTESTEE="essai" REFERENCE_M="$M_REF")\n'
     "# annexe synthétique de la course « audit » (et une annexe trop longue pour la borne du noyau, 100 000 caractères au noyau 9beee10b) : chacune committée dans la copie\n"
     "# sous un chemin permis, le commit relevé, puis HEAD rétabli (l'objet reste dans le dépôt, comme une annexe réelle récupérée\n"
     "# de main sans être sur la tête) ; passées au lanceur par ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN, ESSAI_ANNEXE_1_SHA\n"
     "annexe_commit() {  # annexe_commit CHEMIN_RELATIF FICHIER_CONTENU → le commit qui porte le fichier (puis HEAD~1)\n"
     '  mkdir -p "$DEPOT/$(dirname "$1")"; cp "$2" "$DEPOT/$1"; git -C "$DEPOT" add "$1"; git -C "$DEPOT" -c user.email=e@x -c user.name=essai commit -q -m "essai : annexe synthétique"\n'
     '  git -C "$DEPOT" rev-parse HEAD; git -C "$DEPOT" reset -q --hard HEAD~1\n'
     "}\n"
     'printf \'# Annexe synthétique (essai de la batterie v14)\\n\\nTranscription factice : trois lignes, aucun contenu réel.\\nLigne deux.\\nLigne trois.\\n\' > "$E/entrees/annexe-essai-v1.md"\n'
     '"$PY" -I -c \'import sys; open(sys.argv[1], "w", encoding="utf-8").write("# Annexe trop longue (essai)\\n\\n" + ("x" * 99 + "\\n") * 1000)\' "$E/entrees/annexe-longue-v1.md"   # 100 029 caractères\n'
     'ANNEXE_ESSAI_CHEMIN=essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/annexe-essai-v1.md; ANNEXE_ESSAI_SHA="$(sha256sum "$E/entrees/annexe-essai-v1.md" | cut -d\' \' -f1)"\n'
     'ANNEXE_ESSAI_COMMIT="$(annexe_commit "$ANNEXE_ESSAI_CHEMIN" "$E/entrees/annexe-essai-v1.md")"\n'
     'ANNEXE_LONGUE_CHEMIN=essaim-m3-refonte-v1/prereg/pieces-pilote4-gemini/annexe-longue-v1.md; ANNEXE_LONGUE_SHA="$(sha256sum "$E/entrees/annexe-longue-v1.md" | cut -d\' \' -f1)"\n'
     'ANNEXE_LONGUE_COMMIT="$(annexe_commit "$ANNEXE_LONGUE_CHEMIN" "$E/entrees/annexe-longue-v1.md")"\n'
     'echo "annexes synthétiques : $ANNEXE_ESSAI_CHEMIN au commit $ANNEXE_ESSAI_COMMIT ($ANNEXE_ESSAI_SHA) ; $ANNEXE_LONGUE_CHEMIN au commit $ANNEXE_LONGUE_COMMIT"\n')
# ---- cas sains : « audit » (essais du noyau exécutés, annexes), puis « maieutique » ----
bloc("cas sains", 'echo "== cas sains : v6.2 complète', 'verifier sain-v6-2-s-lanceur-attendu "lanceur attendu $(basename "$LANCEUR") (${H:0:8}…)" "$VS/LANCEMENT.md"',
     "1a69f08aae9e7161d48f59f2b0649e659237da04bf065e8cf94804062c70902a",
     'echo "== cas sains : course « maieutique » complète (essais du noyau exécutés), puis course « audit » (paramètres définitifs : question v3 et son annexe réelle, commit ad23e9ae) ; rondes de conception et quatre générations =="\n'
     'td_heure "$E/entrees/td-heure-fraiche-maieutique.json" 0 GO-2026-10-26-05\n'
     'cas sain-maieutique "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-maieutique.json" ESSAI_EXIGER_HEURE=1 PRECEDENTE_V62="$E/nulle-part"\n'
     'VM="$E/cas-sain-maieutique/course-maieutique-gemini-v6-2-v1"\n'
     'verifier sain-maieutique-reference-m "; M saine : g000 et g001 OK" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-graine-m "graine $GRAINE_M_SCELLEE = graine M du texte scellé du second pilote (d2944654…)" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-organisme "organisme : 26 fichiers, empreinte d\'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-essais "essais : 169 passés, 0 sauté, 0 désélectionnés" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-registre "registre : une ligne GO-2026-10-26-05 de type calcul" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-graine "graine $G_M de la course maieutique écrite et recalculée depuis l\'entropie du texte (enfant 0), ligne de la course audit présente (non utilisée)" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-temps-conception "temps par ronde de conception 900 s" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-minuteur "STOP non posé" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-question "question (maieutique) : sha256 $Q_M (question-hypotheses-maieutique-organismes-v1.md, commit eb03bad5…) ; annexes servies : 0" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-question-servie "question servie : question.md, sha256 $Q_M, 2916 caractères" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-garde "garde refus-question : aucun arrêt ; veilleur arrêté par son PID" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-garde-journal "journal vivant de g001 : /var/lib/essaim-m3/" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-garde-roles "rôles propres à la question : monoculture_croisee sonde_orthogonale_onsager critique_adversariale_limites arbitre_synthese_contradictoire ; monoculture_analytique : refus après le premier appel moissonneur_* de g001 ou au-delà du 120e appel de ce rôle ; raisons d\'arrêt de sûreté : refusal SAFETY PROHIBITED_CONTENT BLOCKLIST SPII RECITATION IMAGE_SAFETY BLOCAGE_PROMPT" "$VM/LANCEMENT.md"\n'
     'verifier sain-maieutique-groupe "session et groupe de processus propres, par setsid : groupe " "$VM/LANCEMENT.md"\n'
     'verifier_absent_texte sain-maieutique-sans-porte-precedente "course v6.2 précédente" "$VM/LANCEMENT.md"\n'
     'verifier_absent_texte sain-maieutique-precedente-ignoree "PRECEDENTE_V62" "$VM/LANCEMENT.md"\n'
     'JUNIT="$E/junit-sain-v1.xml"; cp "$VM/essais-v1.xml" "$JUNIT"\n'
     'SAIN+=(ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="169 passed")\n'
     'td_heure "$E/entrees/td-heure-fraiche-audit.json" 0 GO-2026-10-26-04\n'
     'cas sain-audit "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit GRAINE="$G_A" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-heure-fraiche-audit.json" ESSAI_EXIGER_HEURE=1 ESSAI_ANNEXE_1_COMMIT= ESSAI_ANNEXE_1_CHEMIN= ESSAI_ANNEXE_1_SHA=   # paramètres définitifs du lanceur : question v3 et annexe réelle, aucune variable d\'essai d\'annexe\n'
     'VA="$E/cas-sain-audit/course-audit-gemini-v6-2-v1"\n'
     'verifier sain-audit-reference-m "; M saine : g000 et g001 OK" "$VA/LANCEMENT.md"\n'
     'verifier sain-audit-organisme "organisme : 26 fichiers, empreinte d\'arbre 4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d" "$VA/LANCEMENT.md"\n'
     'verifier sain-audit-registre "registre : une ligne GO-2026-10-26-04 de type calcul" "$VA/LANCEMENT.md"\n'
     'verifier sain-audit-graine "graine $G_A de la course audit écrite et recalculée depuis l\'entropie du texte (enfant 1), ligne de la course maieutique présente (non utilisée)" "$VA/LANCEMENT.md"\n'
     'verifier sain-audit-temps-conception "temps par ronde de conception 900 s" "$VA/LANCEMENT.md"\n'
     'verifier sain-audit-minuteur "STOP non posé" "$VA/LANCEMENT.md"\n'
     'verifier sain-audit-question "question (audit) : sha256 $Q_A (question-audit-controle-organismes-v3.md, commit ad23e9ae…) ; annexes servies : 1 ; annexe 1 : $ANNEXE_DEF_CHEMIN $COMMIT_DEF $ANNEXE_DEF_SHA" "$VA/LANCEMENT.md"\n'
     "# la question servie de la course « audit », recomposée ici sans le lanceur, depuis le dépôt : la question v3, puis, pour chaque annexe servie,\n"
     "# une ligne ---, un titre « # Annexe k — chemin (sha256 …) » et son contenu (une ligne vide avant et après chaque séparateur et chaque titre)\n"
     '"$PY" -I -c \'\n'
     "import hashlib, subprocess, sys\n"
     "depot = sys.argv[1]\n"
     'def lire(c, p): return subprocess.run(["git", "-C", depot, "show", c + ":" + p], check=True, capture_output=True).stdout\n'
     'b = lire("ad23e9ae07588ed701a70b9b5f4bf379ca079953", "brouillons/questions-organismes-20261026-v1/question-audit-controle-organismes-v3.md")\n'
     "for k, (c, p, h) in enumerate([(sys.argv[2], sys.argv[3], sys.argv[4])], 1):\n"
     '    b += ("\\n---\\n\\n# Annexe %d — %s (sha256 %s)\\n\\n" % (k, p, h)).encode("utf-8") + lire(c, p)\n'
     'print(hashlib.sha256(b).hexdigest(), len(b.decode("utf-8")))\' "$DEPOT" "$COMMIT_DEF" "$ANNEXE_DEF_CHEMIN" "$ANNEXE_DEF_SHA" > "$E/question-servie-audit.txt"\n'
     'read -r SHA_SERVIE_A N_SERVIE_A < "$E/question-servie-audit.txt"\n'
     'verifier sain-audit-question-servie "question servie : question.md, sha256 $SHA_SERVIE_A, $N_SERVIE_A caractères" "$VA/LANCEMENT.md"\n'
     'verifier sain-audit-question-servie-fichier "$SHA_SERVIE_A  question.md" "$VA/EMPREINTES-pilote-v1.txt"\n'
     'verifier sain-audit-question-fichier-annexe "# Annexe 1 — $ANNEXE_DEF_CHEMIN (sha256 $ANNEXE_DEF_SHA)" "$VA/question.md"\n'
     '"$PY" -I -c \'import sys; n = int(sys.argv[1]); b = int(sys.argv[2]); print("taille servie %d caractères %s %d (CARACTERES_MAX_QUESTION du noyau 9beee10b)" % (n, "≤" if n <= b else ">", b))\' "$N_SERVIE_A" 100000 > "$E/taille-servie-audit.txt"\n'
     'verifier sain-audit-taille-servie-sous-la-borne "caractères ≤ 100000 (CARACTERES_MAX_QUESTION du noyau 9beee10b)" "$E/taille-servie-audit.txt"   # assertion demandée : question v3 + annexe < 100 000\n'
     'verifier sain-audit-taille-servie-relevee "taille servie 39617 caractères" "$E/taille-servie-audit.txt"   # 3 430 (question v3) + 163 (titre) + 36 024 (annexe)\n'
     'verifier sain-audit-garde "garde refus-question : aucun arrêt" "$VA/LANCEMENT.md"\n'
     'verifier_absent_texte sain-audit-sans-reserve-annexe "sans aucune annexe servie" "$VA/LANCEMENT.md"\n')
remplacer('for d in "$VS" "$V6"; do\n', 'for d in "$VM" "$VA"; do\n', 2)
remplacer('    verifier "sain-pousse-$g-$(basename "$d")" "journal-appels-$g.jsonl" "$d/A-POUSSER-v1.txt"\n  done\ndone\n',
          '    verifier "sain-pousse-$g-$(basename "$d")" "journal-appels-$g.jsonl" "$d/A-POUSSER-v1.txt"\n  done\n'
          '  verifier "sain-reponse-$(basename "$d")" "réponse à la question : reponse-question-g001.md, sha256" "$d/LANCEMENT.md"\n'
          'done\n', 1)
bloc("trois cas sains", 'cas sain-simulation-sans-reference "archive fermée', 'cas go-m-seulement-autorise-v6-2 "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=v6-2 "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-m-seulement.md"',
     "1d0dc73b286c625bf5eeee4dbe072d87f8e5fc5869b324f522351ed7a1abfbfa",
     'cas sain-simulation-sans-reference "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit REGISTRE_GO_SOURCE="$E/entrees/go-sain.md" DEPENSES_SOURCE="$E/entrees/dep-sans-empreinte-m.md" RESTE_GO_USD=150 APPEL_CONTROLE_FICHIER="$E/entrees/td-sain-audit.json" RECHARGE_ATTESTEE=essai ESSAI_JUNIT_EXISTANT="$JUNIT" ESSAI_RESUME_EXISTANT="169 passed"\n'
     'cas go-maieutique-seulement-autorise-maieutique "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-maieutique-seulement.md"\n'
     'cas go-audit-seulement-autorise-audit "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-audit-seulement.md"\n')
# ---- porte « course v6.2 précédente » : retirée ----
bloc("v62", 'echo "== course S (v6-2-s) : issues de v6.2 hors de la liste saine', 'DEPENSES_SOURCE="$E/entrees/dep-s-sans-empreinte-v62.md"',
     "0ef01ecb5e31f38c1cd50a3cbd449c8bea4ca468bc5cf1b174a6276f6720d41b",
     "# v14 : les cas de la porte « course v6.2 précédente » (v62-*, VSC, copies de la v6.2) sont retirés : la porte n'existe plus dans le\n"
     "#   lanceur v12 (PRECEDENTE_V62 sans effet : essayé sur sain-maieutique, et en réel par reel-sans-reference, sans elle)\n")
bloc("réel", 'echo "== mode réel (copie du dépôt sous /root) : COURSE=v6-2 refusée', 'cas reel-v6-2-s-precedente-sous-ce-lanceur "v6.2 n a pas tourné sous ce lanceur" -- "${REEL_S[@]}" PRECEDENTE_V62="$P_REEL"\nrm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"',
     "91ed4c4c0e5c17f0ea59bd9db5ba71ea8ba04c2d56d216fe001d4a9df5ebeba9",
     'echo "== mode réel (copie du dépôt sous /root) : clés du pilote 4 refusées juste après le case ; GO_ID exigé ; sans PRECEDENTE_V62, refus à l\'étape (0), avant tout appel =="\n'
     'REEL_BASE=(MODE=reel PILOTE_RACINE=- DEPOT="$DEPOT_ROOT" "${CLES_REEL[@]}" BRAVE_API_KEY=factice OPENALEX_API_KEY=factice SEMANTIC_SCHOLAR_API_KEY=factice RECHARGE_ATTESTEE=essai)\n'
     'cas reel-cle-ancienne-v6-2 "COURSE=v6-2 : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- "${REEL_BASE[@]}" COURSE=v6-2\n'
     'cas reel-cle-ancienne-v6-2-s "COURSE=v6-2-s : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- "${REEL_BASE[@]}" COURSE=v6-2-s\n'
     'cas reel-sans-go-id "GO_ID=identifiant du GO de la course, donné par session-depot" -- "${REEL_BASE[@]}" GO_ID=\n'
     'cas reel-go-id-forme "GO_ID doit être de la forme GO-AAAA-MM-JJ-NN : « GO-26-05 »" -- "${REEL_BASE[@]}" GO_ID=GO-26-05\n'
     'cas reel-journal-garde-essai "variable ESSAI_JOURNAL_GARDE définie en mode réel" -- "${REEL_BASE[@]}" ESSAI_JOURNAL_GARDE=/var/tmp/x\n'
     'REEL=("${REEL_BASE[@]}" COURSE=maieutique)\n'
     'cas reel-sans-reference "REFERENCE_M non défini" -- "${REEL[@]}"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes"\n'
     'cas reel-sans-reference-audit "REFERENCE_M non défini" -- "${REEL_BASE[@]}" COURSE=audit\n'
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
     'cas reel-reference-tentative-simulee "M n a pas tourné en réel" -- "${REEL[@]}" COURSE=audit REFERENCE_M="$RR/pilote2-gemini-v5-2-1-maieutique-v1-tentative2"\n'
     'rm -rf "$DEPOT_ROOT/essaim-m3-refonte-v1/pilotes" "$RR"\n')
# ---- clés refusées, forme du GO ----
bloc("clés", 'cas course-inconnue "COURSE inconnue : autre (v6-2-s ou v6-2)"', 'cas course-du-second-pilote "COURSE inconnue : maieutique (v6-2-s ou v6-2)" -- MODE=simulation COURSE=maieutique',
     "bcdfca6840d1abd1b5356c7539af33819afa6b23d2bbcc955ec69ec835ef8cf7",
     'cas course-inconnue "COURSE inconnue : autre (maieutique ou audit)" -- MODE=simulation COURSE=autre\n'
     'cas course-du-second-pilote "COURSE inconnue : structure (maieutique ou audit)" -- MODE=simulation COURSE=structure\n'
     'cas cle-ancienne-refusee "COURSE=v6-2-s : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- MODE=simulation COURSE=v6-2-s\n'
     'cas cle-ancienne-refusee-v6-2 "COURSE=v6-2 : clé du pilote 4, refusée par ce lanceur (maieutique ou audit)" -- MODE=simulation COURSE=v6-2\n'
     'cas go-id-forme "GO_ID doit être de la forme GO-AAAA-MM-JJ-NN : « 05 »" -- MODE=simulation GO_ID=05\n')
remplacer('echo "== R3 : verrou et marqueur de départ (noms du pilote 4) =="', 'echo "== R3 : verrou et marqueur de départ (noms des courses) =="', 1)
# ---- texte ----
bloc("texte", 'echo "== préenregistrement (graines par course, lanceur cité, marqueurs) =="', 'cas prereg-empreinte "empreinte du préenregistrement ≠ PREREG_SHA256" -- MODE=simulation GRAINE="$G_S" PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256=0000 "${SAIN[@]}"',
     "22dbd9f5d97b5f2a65a726a20ba11f68e85b9263249b9ee9dfa82b5ebaac395c",
     'echo "== texte (un texte pour les deux courses : graine de la course, ligne de l\'autre course exigée, lanceur cité, marqueurs) =="\n'
     'cas texte-graine-autre-course-maieutique "n\'est pas écrite dans le texte scellé" -- MODE=simulation COURSE=maieutique GRAINE="$G_A" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}"\n'
     'cas texte-graine-autre-course-audit "n\'est pas écrite dans le texte scellé" -- MODE=simulation COURSE=audit GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}"\n'
     'cas texte-graine-hors-entropie-maieutique "≠ celle de SeedSequence(E).spawn(2)[0]" -- MODE=simulation COURSE=maieutique GRAINE=13 TEXTE="$E/entrees/prereg-graine-hors-entropie.md" TEXTE_SHA256="$(cut -d\' \' -f1 < "$E/entrees/prereg-graine-hors-entropie.md.sha256")" "${SAIN[@]}"\n'
     'cas texte-graine-hors-entropie-audit "≠ celle de SeedSequence(E).spawn(2)[1]" -- MODE=simulation COURSE=audit GRAINE=13 TEXTE="$E/entrees/prereg-graine-hors-entropie.md" TEXTE_SHA256="$(cut -d\' \' -f1 < "$E/entrees/prereg-graine-hors-entropie.md.sha256")" "${SAIN[@]}"\n'
     'cas texte-sans-ligne-de-l-autre-course "la ligne « graine de la course audit = … » est absente du texte" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-une-ligne.md" TEXTE_SHA256="$(cut -d\' \' -f1 < "$E/entrees/prereg-une-ligne.md.sha256")" "${SAIN[@]}"\n'
     'cas texte-lanceur-source "ne cite pas l\'empreinte de ce lanceur" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-lanceur-source.md" TEXTE_SHA256="$(cut -d\' \' -f1 < "$E/entrees/prereg-lanceur-source.md.sha256")" "${SAIN[@]}"\n'
     'cas texte-marqueur "marqueurs <<…>> restants" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-marqueur.md" TEXTE_SHA256="$(cut -d\' \' -f1 < "$E/entrees/prereg-marqueur.md.sha256")" "${SAIN[@]}"\n'
     'cas texte-empreinte "empreinte du texte ≠ TEXTE_SHA256" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256=0000 "${SAIN[@]}"\n')
# ---- objets et question servie ----
bloc("objets", 'echo "== objets et question =="', 'cas question-v6-2 "empreinte de la question ≠ 8b1c7511…" -- MODE=simulation COURSE=v6-2 ESSAI_ARTEFACT=question "${SAIN[@]}"',
     "a029c453c4253f6c0cc20c8ed80d9def110246bf34afbcec4539af54c12a7f91",
     'echo "== objets et question servie (question de base ; annexes de la course « audit ») =="\n'
     'cas organisme-maieutique "empreinte d\'arbre de l\'organisme ≠ 4f13647a…" -- MODE=simulation COURSE=maieutique ESSAI_ARTEFACT=organisme "${SAIN[@]}"\n'
     'cas organisme-audit "empreinte d\'arbre de l\'organisme ≠ 4f13647a…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=organisme "${SAIN[@]}"\n'
     'cas nombre-maieutique "fichiers au lieu de 26" -- MODE=simulation COURSE=maieutique ESSAI_ARTEFACT=nombre "${SAIN[@]}"\n'
     'cas nombre-audit "fichiers au lieu de 26" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=nombre "${SAIN[@]}"\n'
     'cas question-empreinte-autre "empreinte de la question ≠ 00000000…" -- MODE=simulation ESSAI_ARTEFACT=question-base "${SAIN[@]}"\n'
     'cas question-empreinte-autre-audit "empreinte de la question ≠ 00000000…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question-base "${SAIN[@]}"\n'
     'cas question-servie-alteree "empreinte de la question servie ≠" -- MODE=simulation ESSAI_ARTEFACT=question "${SAIN[@]}"\n'
     'cas question-servie-alteree-audit "empreinte de la question servie ≠" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question "${SAIN[@]}"\n'
     'cas question-v1-refusee "empreinte de la question ≠ 998960b8…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question-v1 "${SAIN[@]}"\n'
     'cas question-v2-refusee "empreinte de la question ≠ 998960b8…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=question-v2 "${SAIN[@]}"\n'
     'cas annexe-empreinte-fausse "empreinte de l\'annexe 1 ($ANNEXE_DEF_CHEMIN) ≠ 01234567…" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_COMMIT="$COMMIT_DEF" ESSAI_ANNEXE_1_CHEMIN="$ANNEXE_DEF_CHEMIN" ESSAI_ANNEXE_1_SHA=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef   # l\'annexe réelle, une empreinte fausse : refus avant tout appel\n'
     'verifier_absent annexe-empreinte-fausse-sans-course "$E/cas-annexe-empreinte-fausse/course-audit-gemini-v6-2-v1/course"   # aucun appel : le noyau n\'est jamais parti\n'
     'verifier_absent annexe-empreinte-fausse-sans-manifeste "$E/cas-annexe-empreinte-fausse/course-audit-gemini-v6-2-v1/course/manifeste-run.json"\n'
     'cas annexe-absente "annexe 1 (docs/nulle-part-v1.md) absente du commit" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=annexe-absente "${SAIN[@]}"\n'
     'cas annexe-alteree "empreinte de l\'annexe 1 ($ANNEXE_ESSAI_CHEMIN) ≠ 00000000…" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=annexe "${SAIN[@]}"\n'
     'cas annexe-champs-incomplets "ESSAI_ANNEXE_1_COMMIT, ESSAI_ANNEXE_1_CHEMIN et ESSAI_ANNEXE_1_SHA vont ensemble" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_SHA=\n'
     'cas annexe-commit-absent "annexe 1 : commit 0123456789abcdef0123456789abcdef01234567 absent du dépôt" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_COMMIT=0123456789abcdef0123456789abcdef01234567\n'
     'cas question-servie-trop-longue "caractères > 100000 (borne du noyau 9beee10b, essaim_m3/noyau/question.py, CARACTERES_MAX_QUESTION)" -- MODE=simulation COURSE=audit "${SAIN[@]}" ESSAI_ANNEXE_1_COMMIT="$ANNEXE_LONGUE_COMMIT" ESSAI_ANNEXE_1_CHEMIN="$ANNEXE_LONGUE_CHEMIN" ESSAI_ANNEXE_1_SHA="$ANNEXE_LONGUE_SHA"\n'
     'cas audit-sans-annexe-reserve "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=audit ESSAI_ARTEFACT=annexe-vide "${SAIN[@]}"   # emplacement 1 vidé par l\'artefact : la course part, RÉSERVE consignée\n'
     'verifier audit-sans-annexe-reserve-ligne "RÉSERVE : course « audit » sans aucune annexe servie" "$E/cas-audit-sans-annexe-reserve"/*/LANCEMENT.md\n'
     'verifier audit-sans-annexe-question-servie "question servie : question.md, sha256 $Q_A, 3430 caractères" "$E/cas-audit-sans-annexe-reserve"/*/LANCEMENT.md\n'
     'cas annexe-artefacts-sans-effet-maieutique "archive fermée : ferme.tar.gz" -- MODE=simulation COURSE=maieutique ESSAI_ARTEFACT=annexe "${SAIN[@]}"\n'
     'cas reel-annexe-essai "variable ESSAI_ANNEXE_1_COMMIT définie en mode réel" -- MODE=reel PILOTE_RACINE=- COURSE=audit ESSAI_ANNEXE_1_COMMIT=x ESSAI_ANNEXE_1_CHEMIN=x ESSAI_ANNEXE_1_SHA=x\n')
# ---- registres ----
bloc("registres", 'echo "== registres (GO-2026-10-25-02 ; dépense) =="', 'cas reste-insuffisant "< $USD_COURSE" -- MODE=simulation "${SAIN[@]}" RESTE_GO_USD="$SOUS_PLAFOND"',
     "af88bd6ec972858a5a8f3d4eede7b803e9d9d2207d7ef9a09ec1181a598c4db5",
     'echo "== registres (un GO par course : GO-2026-10-26-05 « maieutique », GO-2026-10-26-04 « audit » ; dépense) =="\n'
     'cas go-sans-calcul "GO non inscrit pour cette course" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-calcul.md"\n'
     'cas go-autre-id "aucune ligne « | GO-2026-10-26-05 | »" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-id.md"\n'
     'cas go-maieutique-seulement-refuse-audit "aucune ligne « | GO-2026-10-26-04 | »" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-maieutique-seulement.md"\n'
     'cas go-audit-seulement-refuse-maieutique "aucune ligne « | GO-2026-10-26-05 | »" -- MODE=simulation COURSE=maieutique "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-audit-seulement.md"\n'
     'cas go-autre-question "l\'empreinte de la question 1d29fbec…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"\n'
     'cas go-autre-question-audit "l\'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-autre-question.md"\n'
     'cas go-questions-croisees "l\'empreinte de la question 1d29fbec…" -- MODE=simulation "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-questions-croisees.md"\n'
     'cas go-questions-croisees-audit "l\'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-questions-croisees.md"\n'
     'cas go-question-v1-refuse-audit "l\'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-question-v1.md"\n'
     'cas go-question-v2-refuse-audit "l\'empreinte de la question 998960b8…" -- MODE=simulation COURSE=audit "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-question-v2.md"\n'
     'cas go-sans-texte "celle du texte scellé ($T16)" -- MODE=simulation GRAINE="$G_M" TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR" "${SAIN[@]}" REGISTRE_GO_SOURCE="$E/entrees/go-sans-texte.md"\n'
     'cas depense-absente "lancement non consigné avant dans registres/depenses.md (une ligne nommant course-maieutique-gemini-v6-2-v1 et GO-2026-10-26-05)" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-absente.md"\n'
     'cas depense-ancienne-forme "lancement non consigné avant dans registres/depenses.md (une ligne nommant course-maieutique-gemini-v6-2-v1 et GO-2026-10-26-05)" -- MODE=simulation "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-ancienne-forme.md"\n'
     'cas depense-ancienne-forme-audit "une ligne nommant course-audit-gemini-v6-2-v1 et GO-2026-10-26-04" -- MODE=simulation COURSE=audit "${SAIN[@]}" DEPENSES_SOURCE="$E/entrees/dep-ancienne-forme.md"\n'
     'cas reste-insuffisant "< $USD_COURSE" -- MODE=simulation "${SAIN[@]}" RESTE_GO_USD="$SOUS_PLAFOND"\n')
# ---- test de dépense ----
bloc("test de dépense", 'echo "== test de dépense (GO-2026-10-25-02) =="', 'cas td-noms-autres "noms des variables du test : anthropic = \'RR_ANTHROPIC_API_KEY\' (attendu RR_ANTHROPIC_API_KEY_3)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-autres.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2',
     "bb5444078d7ca088be4e9fd6bfdf91db01bac3114dbed82c1df3e07871486885",
     'echo "== test de dépense (le GO de la course) =="\n'
     'cas td-autre-go "go = \'GO-2026-10-25-01\' (attendu GO-2026-10-26-05)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-autre-go.json"\n'
     'cas td-autre-go-audit "go = \'GO-2026-10-26-05\' (attendu GO-2026-10-26-04)" -- MODE=simulation COURSE=audit "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-go-maieutique.json"\n'
     'cas td-echec "CLAUDE_FABLE_5_1 : statut \'ECHEC_API\'" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-echec.json"\n'
     'cas td-heure-absente-exigee "heure_utc absente (exigée en réel)" -- MODE=simulation "${SAIN[@]}" ESSAI_EXIGER_HEURE=1\n'
     'cas td-vieux "> 900 s" -- MODE=simulation ESSAI_ARTEFACT=appel-vieux "${SAIN[@]}"\n'
     'td_noms "$E/entrees/td-noms-conformes.json" RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 GO-2026-10-26-05\n'
     'cas td-noms-conformes "noms des variables du test : anthropic RR_ANTHROPIC_API_KEY_3, gemini GEMINI_API_KEY_2" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-conformes.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2\n'
     'td_noms "$E/entrees/td-noms-autres.json" RR_ANTHROPIC_API_KEY GEMINI_API_KEY GO-2026-10-26-05\n'
     'cas td-noms-autres "noms des variables du test : anthropic = \'RR_ANTHROPIC_API_KEY\' (attendu RR_ANTHROPIC_API_KEY_3)" -- MODE=simulation "${SAIN[@]}" APPEL_CONTROLE_FICHIER="$E/entrees/td-noms-autres.json" CLE_ANTHROPIC=RR_ANTHROPIC_API_KEY_3 CLE_GEMINI=GEMINI_API_KEY_2\n')
# ---- segments : la question servie, la porte retirée ----
remplacer('cas seg-question-modifiee "empreinte de la question ≠ 8b1c7511…"', 'cas seg-question-modifiee "empreinte de la question servie ≠"', 1)
bloc("porte sur segments", 'echo "-- porte « v6.2 précédente » de la course S sur la v6.2 en segments --"', 'cas seg-v62-reprises-mal-numerotees "arrêt de la course : [\'fichier STOP\', \'aucune lignée active\'] ; reprises : [3]" -- "${VSC[@]}" PRECEDENTE_V62="$d"',
     "9c6dc3a904ace181bf12bd0132ed12183df7324027ab9298b093537ce9508a02",
     "# v14 : la porte « course v6.2 précédente » sur la course en segments (seg-v6-2-s-porte-saine, seg-v62-*) est retirée avec la porte\n")
bloc("clore refusée", 'cas seg-clore-v62-refusee', 'PRECEDENTE_V62="$PC"', "44a22648daaf3e2640f3534ddcbc20efa7dd4679f0001fc1a16e1edc042547ca", "")
bloc("GO du mutant", "printf '| GO-2026-10-25-02 | 2026-10-25 | calcul | pilote 4 (essai, lanceur muté)", '> "$E/entrees/go-mutant.md"',
     "f999488ef433009a7b0c649388fd1ba2de6c38495524f8c980e633d62cbab954",
     '{ ligne_go GO-2026-10-26-05 maieutique "$Q_M" "${SHA_PRM:0:16}"; ligne_go GO-2026-10-26-04 audit "$Q_A" "${SHA_PRM:0:16}"; } > "$E/entrees/go-mutant.md"\n')
# ---- garde « refus-question » (R5) ----
remplacer('LANCEUR="$LANCEUR_SAIN"\necho "== état des dépôts d\'essai après la série =="\n',
          'LANCEUR="$LANCEUR_SAIN"\n'
          'echo "== garde refus-question (R5) : journaux synthétiques lus par le veilleur (ESSAI_JOURNAL_GARDE) ; règle de conv-audit du 26 octobre 2026 : cas sains (dont le motif réel de g001 de la course M), artefacts =="\n'
          "journal_garde() {  # journal_garde FICHIER MOTIF… : journal synthétique ; MOTIF = ROLE[:STATUT[:FIN]][*N] (OK end_turn par défaut ; REFUS vaut fin refusal ; *N répète) ; identifiants organisme-0001, 0002, …\n"
          '  "$PY" -I -c \'\n'
          "import json, re, sys\n"
          "f, motifs = sys.argv[1], sys.argv[2:]\n"
          "def ligne(i, r, st=\"OK\", fi=None):\n"
          '    fi = fi if fi is not None else (\"refusal\" if st == \"REFUS\" else \"end_turn\")\n'
          '    return {"id": "organisme-%04d" % i, "etape": "organisme", "role": r, "espece": "CLAUDE_FABLE_5_1", "famille": "anthropic", "modele_demande": "claude-fable-5-1", "modele_servi": "claude-fable-5-1", "statut": st, "fin": fi, "categorie": None, "usage": {"entree": 10, "sortie": 10}, "cout_usd": 0.0001, "cumul_usd": 0.0001 * i, "angle": None, "max_tokens": 8192, "sha256_prompt": "0" * 64, "sha256_texte": "0" * 64, "caracteres": 10, "debut_utc": "2026-10-26T12:00:00.000000Z", "fin_utc": "2026-10-26T12:00:01.000000Z", "echec": None, "reel": False, "go_id": None, "types_blocs": ["text"]}\n'
          "lignes = []\n"
          "for m in motifs:\n"
          '    g = re.fullmatch(r"([A-Za-z0-9_]+)(?::([A-Z_]+)(?::([A-Za-z_]+))?)?(?:\\*(\\d+))?", m)\n'
          '    if not g: sys.exit("motif illisible : " + m)\n'
          "    for _ in range(int(g.group(4) or 1)):\n"
          '        lignes.append(ligne(len(lignes) + 1, g.group(1), g.group(2) or "OK", g.group(3)))\n'
          'open(f, "w", encoding="utf-8").write("".join(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\\n" for l in lignes))\' "$@"\n'
          "}\n"
          "suite_journal() {  # suite_journal JOURNAL : les lignes « rôle statut fin » d'un journal, pour comparer un journal synthétique au journal réel\n"
          '  "$PY" -I -c \'import json, sys; print("".join(" ".join(str(e[k]) for k in ("role", "statut", "fin")) + "\\n" for e in map(json.loads, open(sys.argv[1], encoding="utf-8"))), end="")\' "$1"\n'
          "}\n"
          "# motif réel de g001 de la course M du pilote 4 (journal-appels-g001.jsonl poussé, fec0cb8237e325a8bf0d493d681082b4b9d89924dc9ddfa21e390e4d05953bc5, 129 appels : 120 appels de tâche\n"
          "# monoculture_analytique dont cinq en REFUS, l'appel moissonneur_formulation_requetes, puis les cinq castes de la question, l'arbitre en REFUS) ;\n"
          "# suites « rôle statut fin » : 124 premiers appels 6d2ad200…, 129 appels 7f79273d… (relevées sur le journal réel, vérifiées ci-dessous)\n"
          'MOTIF_REEL_M=(inducteur_entrainement "calibrateur_interne*2" "monoculture_analytique*25" monoculture_analytique:REFUS "monoculture_analytique*16" monoculture_analytique:REFUS "monoculture_analytique*9" monoculture_analytique:REFUS "monoculture_analytique*54" monoculture_analytique:REFUS "monoculture_analytique*9" monoculture_analytique:REFUS "monoculture_analytique*2" moissonneur_formulation_requetes)\n'
          'journal_garde "$E/entrees/journal-garde-sain.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique inducteur_entrainement:REFUS monoculture_analytique arbitre_synthese_contradictoire\n'
          'journal_garde "$E/entrees/journal-garde-artefact.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique arbitre_synthese_contradictoire:REFUS monoculture_analytique arbitre_synthese_contradictoire\n'
          'journal_garde "$E/entrees/journal-garde-fin-surete.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique critique_adversariale_limites:MODELE_NON_CONFORME:SAFETY monoculture_analytique arbitre_synthese_contradictoire\n'
          'journal_garde "$E/entrees/journal-garde-tache-refusee.jsonl" monoculture_analytique calibrateur_interne monoculture_analytique monoculture_analytique:REFUS monoculture_analytique arbitre_synthese_contradictoire   # refus de tâche au rang 3, sans moissonneur : rien\n'
          'journal_garde "$E/entrees/journal-garde-critique-sans-moissonneur.jsonl" "monoculture_analytique*5" critique_adversariale_limites:REFUS monoculture_analytique\n'
          'journal_garde "$E/entrees/journal-garde-apres-moissonneur.jsonl" "monoculture_analytique*10" moissonneur_formulation_requetes monoculture_analytique:REFUS monoculture_croisee\n'
          'journal_garde "$E/entrees/journal-garde-rang-121.jsonl" "monoculture_analytique*120" monoculture_analytique:REFUS monoculture_croisee\n'
          'journal_garde "$E/entrees/journal-garde-rang-120.jsonl" "monoculture_analytique*119" monoculture_analytique:REFUS monoculture_analytique\n'
          'journal_garde "$E/entrees/journal-garde-moissonneur-refuse.jsonl" "monoculture_analytique*3" moissonneur_formulation_requetes:REFUS monoculture_analytique\n'
          'journal_garde "$E/entrees/journal-garde-motif-reel-m-avant-question.jsonl" "${MOTIF_REEL_M[@]}"\n'
          'journal_garde "$E/entrees/journal-garde-motif-reel-m-complet.jsonl" "${MOTIF_REEL_M[@]}" monoculture_analytique monoculture_croisee sonde_orthogonale_onsager:OK:STOP critique_adversariale_limites arbitre_synthese_contradictoire:REFUS\n'
          'journal_garde "$E/entrees/journal-garde-premiere-caste-apres-moissonneur.jsonl" "${MOTIF_REEL_M[@]}" monoculture_analytique:REFUS\n'
          'suite_journal "$E/entrees/journal-garde-motif-reel-m-avant-question.jsonl" | sha256sum | cut -d\' \' -f1 > "$E/suite-motif-reel-m-avant-question.txt"\n'
          'suite_journal "$E/entrees/journal-garde-motif-reel-m-complet.jsonl" | sha256sum | cut -d\' \' -f1 > "$E/suite-motif-reel-m-complet.txt"\n'
          'verifier garde-motif-reel-m-avant-question-suite "6d2ad200d3c45833933bd6f20bfc80cf6b7e0afabe0bf32f8c50ff6950173294" "$E/suite-motif-reel-m-avant-question.txt"\n'
          'verifier garde-motif-reel-m-complet-suite "7f79273db464bbbb00e83372d970e93553acf1b306e60708aa95ab6d9b3b6050" "$E/suite-motif-reel-m-complet.txt"\n'
          "printf '{\"id\": \"organisme-0001\", \"role\": \"monoculture_croisee\", \"statut\": \"REFUS\", \"fin\": \"refusal\"' > \"$E/entrees/journal-garde-ligne-incomplete.jsonl\"   # une ligne sans fin de ligne : jamais lue\n"
          'cas garde-refus-question-sain "archive fermée : ferme.tar.gz" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$E/entrees/journal-garde-sain.jsonl"\n'
          'D_GARDE_SAIN="$E/cas-garde-refus-question-sain/course-maieutique-gemini-v6-2-v1"\n'
          'verifier garde-sain-aucun-arret "garde refus-question : aucun arrêt ; veilleur arrêté par son PID" "$D_GARDE_SAIN/LANCEMENT.md"\n'
          'verifier garde-sain-journal-essai "(ESSAI : journal synthétique)" "$D_GARDE_SAIN/LANCEMENT.md"\n'
          'verifier_absent_texte garde-sain-sans-ligne-d-arret "arrêt par la garde refus-question" "$D_GARDE_SAIN/LANCEMENT.md"\n'
          'verifier_absent garde-sain-sans-piece "$D_GARDE_SAIN/garde-refus-question-v1.json"\n'
          'cas garde-refus-question-ligne-incomplete "archive fermée : ferme.tar.gz" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$E/entrees/journal-garde-ligne-incomplete.jsonl"\n'
          'verifier garde-ligne-incomplete-aucun-arret "garde refus-question : aucun arrêt" "$E/cas-garde-refus-question-ligne-incomplete"/*/LANCEMENT.md\n'
          "garde_sans_arret() {  # garde_sans_arret NOM JOURNAL : la course finit d'elle-même ; aucun arrêt, aucune pièce\n"
          '  local nom="$1" j="$2" d\n'
          '  cas "$nom" "archive fermée : ferme.tar.gz" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$j"\n'
          '  d="$E/cas-$nom/course-maieutique-gemini-v6-2-v1"\n'
          '  verifier "$nom-aucun-arret" "garde refus-question : aucun arrêt ; veilleur arrêté par son PID" "$d/LANCEMENT.md"\n'
          '  verifier_absent_texte "$nom-sans-ligne-d-arret" "arrêt par la garde refus-question" "$d/LANCEMENT.md"\n'
          '  verifier_absent "$nom-sans-piece" "$d/garde-refus-question-v1.json"\n'
          "}\n"
          'garde_sans_arret garde-refus-question-tache-refusee "$E/entrees/journal-garde-tache-refusee.jsonl"   # un REFUS de tâche (monoculture_analytique, rang 3, sans moissonneur) ne fait rien\n'
          'garde_sans_arret garde-refus-question-rang-120 "$E/entrees/journal-garde-rang-120.jsonl"   # le 120e appel monoculture_analytique en REFUS, sans moissonneur : encore une tâche\n'
          'garde_sans_arret garde-refus-question-moissonneur-refuse "$E/entrees/journal-garde-moissonneur-refuse.jsonl"   # un moissonneur refusé n\'est pas une caste de la question\n'
          'garde_sans_arret garde-refus-question-motif-reel-m-avant-question "$E/entrees/journal-garde-motif-reel-m-avant-question.jsonl"   # le motif réel de la course M : cinq REFUS de tâche avant la question, aucun arrêt\n'
          "garde_artefact() {  # garde_artefact NOM JOURNAL ATTENDU [ID] [REGLE] : la course est tuée par la garde ; relevés (ligne, règle, pièce poussée, pas de reprise, g001 jamais archivée, délai)\n"
          '  local nom="$1" j="$2" attendu="$3" id="${4:-organisme-0004}" regle="${5:-rôle propre à la question}" d\n'
          '  cas "$nom" "$attendu" -- MODE=simulation "${SAIN[@]}" ESSAI_JOURNAL_GARDE="$j"\n'
          '  d="$E/cas-$nom/course-maieutique-gemini-v6-2-v1"\n'
          '  verifier "$nom-sans-reprise" "course fermée sans reprise" "$d/LANCEMENT.md"\n'
          '  verifier "$nom-noyau-tue" ") tué, enfants directs tués par PID" "$d/LANCEMENT.md"\n'
          '  verifier "$nom-archive" "archive fermée : ferme.tar.gz" "$d/LANCEMENT.md"\n'
          '  verifier "$nom-piece" "garde-refus-question-v1.json" "$d/A-POUSSER-v1.txt"\n'
          '  verifier "$nom-piece-compagnon" "garde-refus-question-v1.json.sha256" "$d/A-POUSSER-v1.txt"\n'
          '  verifier "$nom-piece-appel" "\\"id\\": \\"$id\\"" "$d/garde-refus-question-v1.json"\n'
          '  verifier "$nom-regle" "garde refus-question : règle « $regle »" "$d/LANCEMENT.md"\n'
          '  verifier "$nom-piece-regle" "\\"regle\\": \\"$regle\\"" "$d/garde-refus-question-v1.json"\n'
          '  verifier "$nom-g001-absent" "journal des appels g001 : absent ou non ordinaire dans l\'archive" "$d/LANCEMENT.md"\n'
          '  verifier "$nom-reponse-absente" "réponse à la question : aucune pièce archivée" "$d/LANCEMENT.md"\n'
          '  verifier "$nom-sortie" "pilote fini (arrêt par la garde refus-question : course fermée sans reprise)" "$E/cas-$nom/sortie.txt"\n'
          '  "$PY" -I -c \'\n'
          "import re, sys, datetime\n"
          't = open(sys.argv[1], encoding="utf-8").read()\n'
          'd0 = re.search(r"^- départ de la simulation \\(UTC\\) : (\\S+)", t, re.M); d1 = re.search(r"^- arrêt par la garde refus-question : .* \\((\\S+)\\) ;", t, re.M)\n'
          'f = lambda s: datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")\n'
          'print("arrêt %d s après le départ" % int((f(d1.group(1)) - f(d0.group(1))).total_seconds()) if d0 and d1 else "heures illisibles")\' "$d/LANCEMENT.md" > "$E/delai-$nom.txt" 2>&1\n'
          '  verifier_re "$nom-sous-10-s" "^arrêt ([0-9]|10) s après le départ$" "$E/delai-$nom.txt"\n'
          '  cas "$nom-segment-2-refuse" "est déjà fermée" -- MODE=simulation "${SAIN[@]}" SEGMENT=2 PILOTE_RACINE="$E/cas-$nom"\n'
          "}\n"
          'garde_artefact garde-refus-question-artefact "$E/entrees/journal-garde-artefact.jsonl" "arrêt par la garde refus-question : appel organisme-0004, rôle arbitre_synthese_contradictoire, statut REFUS, fin refusal ("\n'
          'garde_artefact garde-refus-question-fin-surete "$E/entrees/journal-garde-fin-surete.jsonl" "arrêt par la garde refus-question : appel organisme-0004, rôle critique_adversariale_limites, statut MODELE_NON_CONFORME, fin SAFETY ("\n'
          'garde_artefact garde-refus-question-critique-sans-moissonneur "$E/entrees/journal-garde-critique-sans-moissonneur.jsonl" "arrêt par la garde refus-question : appel organisme-0006, rôle critique_adversariale_limites, statut REFUS, fin refusal (" organisme-0006\n'
          'garde_artefact garde-refus-question-apres-moissonneur "$E/entrees/journal-garde-apres-moissonneur.jsonl" "arrêt par la garde refus-question : appel organisme-0012, rôle monoculture_analytique, statut REFUS, fin refusal (" organisme-0012 "monoculture_analytique après le premier appel moissonneur_* de g001 (organisme-0011)"\n'
          'garde_artefact garde-refus-question-rang-121 "$E/entrees/journal-garde-rang-121.jsonl" "arrêt par la garde refus-question : appel organisme-0121, rôle monoculture_analytique, statut REFUS, fin refusal (" organisme-0121 "monoculture_analytique au rang 121 > 120 (au-delà des tâches servies)"\n'
          'garde_artefact garde-refus-question-premiere-caste-apres-moissonneur "$E/entrees/journal-garde-premiere-caste-apres-moissonneur.jsonl" "arrêt par la garde refus-question : appel organisme-0125, rôle monoculture_analytique, statut REFUS, fin refusal (" organisme-0125 "monoculture_analytique après le premier appel moissonneur_* de g001 (organisme-0124)"\n'
          'garde_artefact garde-refus-question-motif-reel-m-complet "$E/entrees/journal-garde-motif-reel-m-complet.jsonl" "arrêt par la garde refus-question : appel organisme-0129, rôle arbitre_synthese_contradictoire, statut REFUS, fin refusal (" organisme-0129\n'
          'echo "== état des dépôts d\'essai après la série =="\n', 1)
# ---- remplacements globaux sur le reste (clés, noms, graines, texte, GO), puis restauration des valeurs d'hier gardées ----
for ancien, nouveau, n in [
    ("= $G_S\n", "= $G_M\n", 1), ('"$G_6"', '"$G_M"', 2), ("= $G_6\n", "= $G_A\n", 1),
    ("graine de la course v6-2-s = ", "graine de la course maieutique = ", 1), ("graine de la course v6-2 = ", "graine de la course audit = ", 1),
    ("MODE=simulation COURSE=v6-2 ", "MODE=simulation COURSE=maieutique ", 6), ("MODE=simulation COURSE=v6-2-s ", "MODE=simulation COURSE=maieutique ", 1),
    (' PREREG="$E/entrees/prereg-sain.md" PREREG_SHA256="$SHA_PR"', ' TEXTE="$E/entrees/prereg-sain.md" TEXTE_SHA256="$SHA_PR"', 2),
    (' PREREG="$E/entrees/prereg-mutant.md" PREREG_SHA256="$SHA_PRM"', ' TEXTE="$E/entrees/prereg-mutant.md" TEXTE_SHA256="$SHA_PRM"', 1),
    ("pilote4-gemini-v6-2-v1", "course-maieutique-gemini-v6-2-v1", 22), ("pilote4-gemini-v6-2-s-v1", "course-maieutique-gemini-v6-2-v1", 2),
    ("cas-sain-v6-2-s", "cas-sain-maieutique", 1),
    ("GO-2026-10-25-02", "GO-2026-10-26-05", 12),
    ("lanceur : lancer_pilote4_gemini_v11.sh, sha256 $H/", "lanceur : lancer_courses_question_v12.sh, sha256 $H/", 1),
    ("@@GO_PILOTE4@@", "GO-2026-10-25-02", 5), ("@@NOM_PILOTE4_M@@", "pilote4-gemini-v6-2-v1", 1), ("@@NOM_PILOTE4_S@@", "pilote4-gemini-v6-2-s-v1", 1),
    ("commits postérieurs à 8e5e2f7b hors des pièces du pilote", "commits postérieurs à 9beee10b hors des pièces du pilote", 4),   # noyau attendu (NOYAU_COMMIT du lanceur v12)
    ("chemins permis après 8e5e2f7b", "chemins permis après 9beee10b (noyau attendu)", 1),
]:
    remplacer(ancien, nouveau, n)
for motif, permis in (("v6-2-s", 17), ("v5.3", 2), ("6251ab21", 1), ("8b1c7511", 3), ("a54da93e", 4), ('PREREG="$E/', 0), ('PREREG_SHA256="$SHA_PR"', 0), ("$G_S\n", 0), ("$G_6", 0), ("G_S=", 0), ("G_6=", 0),
                      ("V6=", 0), (" V62=", 0), ("VSC=", 0), ("VS=", 0), ('"$VS', 0), ("P_REEL", 0), ("REEL_S", 0), ("LANCEUR_V62", 0), ("EMP_V62", 0), ("copie_v62", 0),
                      ("pilote4-gemini-v6-2-v1", 1), ("pilote4-gemini-v6-2-s-v1", 1), ("GO-2026-10-25-02", 5), ("GO-2026-10-26-05", 39), ("GO-2026-10-26-04", 21),
                      ("course-maieutique-gemini-v6-2-v1", 34), ("course-audit-gemini-v6-2-v1", 7), ("COURSE=audit", 30), ("COURSE=maieutique", 18),
                      ("TEXTE=", 14), ("TEXTE_SHA256=", 14), ("ESSAI_JOURNAL_GARDE", 8), ("garde_artefact", 9), ("garde_sans_arret", 6), ("journal_garde ", 13), ("ligne_go ", 21),
                      ("verifier_absent_texte", 7), ("essais_lanceur_question_v14.sh", 1), ("deriver_essais_question_v14.py", 1), ("lancer_courses_question_v12.sh", 2),
                      ("8e5e2f7b", 0), ("9beee10b", 11), ("61ddd638", 0), ("20000", 0), ("100000", 3),
                      ("ec3abf28", 2), ("9417652a", 1), ("998960b8", 7), (COMMIT_DEF, 2), ("ad23e9ae", 7), (ANNEXE_DEF_SHA, 1), (ANNEXE_DEF_CHEMIN, 1), ("ANNEXE_DEF_", 10), ("COMMIT_DEF", 4),
                      ("Q_A_V2", 2), ("question-v2", 7), ("annexe-vide", 2), ("annexe-empreinte-fausse", 6), ("3196", 0), ("3430", 1), ("39617", 1), ("ANNEXE_ESSAI_", 11), ("2fd63bad", 0), ("29b32f62", 0), ("2204256d", 0), ("journal-garde-monoculture.jsonl", 0), ("MOTIF_REEL_M", 4), ("suite_journal", 4),
                      ("6d2ad200d3c45833933bd6f20bfc80cf6b7e0afabe0bf32f8c50ff6950173294", 1), ("7f79273db464bbbb00e83372d970e93553acf1b306e60708aa95ab6d9b3b6050", 1), ("fec0cb82", 2),
                      ("monoculture_analytique*", 11), ("règle", 5),
                      (Q_M, 1), (Q_A, 1), ("eb03bad5", 3), ("@@", 0)):
    k = t.count(motif)
    if k != permis:
        sys.exit(f"refus : {motif!r} présent {k} fois après dérivation (attendu {permis})")
sortie.write_text(t, encoding="utf-8")
print(f"batterie écrite : {sortie.name} {hashlib.sha256(sortie.read_bytes()).hexdigest()}")
