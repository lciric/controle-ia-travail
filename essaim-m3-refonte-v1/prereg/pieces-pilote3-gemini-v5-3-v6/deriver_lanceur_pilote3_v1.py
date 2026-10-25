"""Dérive le lanceur du pilote 3 (v5.3 puis v6) du lanceur scellé du second pilote (v5), par remplacements exacts.

Chaque ancre doit apparaître exactement une fois ; sinon arrêt. Écrit par conv-audit, 25 octobre 2026.
"""
import hashlib
import pathlib
import sys

SRC = pathlib.Path(sys.argv[1])
DST = pathlib.Path(sys.argv[2])
SHA_SRC = "83f8b9cf8f3062dfc5e2c02094c602a2d582adf0cbcef292d5bdccd8f8d61b1b"
texte = SRC.read_text(encoding="utf-8")
assert hashlib.sha256(texte.encode("utf-8")).hexdigest() == SHA_SRC, "lanceur source inattendu"


def remplacer(ancre, nouveau):
    global texte
    n = texte.count(ancre)
    assert n == 1, f"ancre trouvée {n} fois : {ancre[:80]!r}"
    texte = texte.replace(ancre, nouveau)


# 1. En-tête (lignes 1 à 38 de la source)
debut = texte.index("#!/usr/bin/env bash\n")
fin = texte.index("set -euo pipefail\n")
assert debut == 0
ENTETE = """#!/usr/bin/env bash
# Lanceur du troisième pilote descriptif « organismes assistés de Gemini, v5.3 puis v6, chacun seul, mêmes bornes que la
# course M du second pilote, question M à g001 », une course par appel (COURSE=v5-3, puis COURSE=v6) — v1, dérivé du
# lanceur scellé du second pilote (`lancer_pilote2_gemini_v5_2_v5.sh`, `83f8b9cf…`) par `deriver_lanceur_pilote3_v1.py`
# (remplacements exacts ; écart consigné dans `diff-lanceur-v5-vers-pilote3-v1.txt`). Ce qui change par rapport à la
# source : (i) deux courses, chacune avec son objet (commit, arbre, nombre de fichiers, lignée) et la même question M v2 ;
# (ii) GO-2026-10-25-02 ; (iii) l'étape (0) ne lit plus « la course précédente » mais la **course M de référence** du
# second pilote (`REFERENCE_M`), à laquelle elle applique telle quelle la liste close « M saine » du lanceur source (avec
# le nom, l'empreinte et la lignée du lanceur et de l'objet de M, et la graine M du texte scellé du second pilote) : une
# course du pilote 3 ne part qu'après une course M finie, fermée et saine ; la ligne de dépense porte les 16 premiers
# caractères de l'empreinte des empreintes de M ; (iv) chemins permis après b1c7f4b6 : ceux du second pilote et ceux du
# pilote 3. Tout le reste (gardes, environnement fermé, passerelle, essais du noyau, fermeture, liste de ce qui est
# poussé) est le texte du lanceur source, inchangé.
# Objets : v5.3 = `canal/gemini-organisme-v5-3`, commit `4ecba58`, dossier `organisme/`, arbre `6251ab21…`, 22 fichiers ;
# v6 = `canal/gemini-organisme-v6`, commit `7cd7508`, arbre `940c59c3…`, 24 fichiers ; lignées « assistées » (déclarées).
# Ces deux commits portent aussi l'arbre de la relève : seul `organisme/` en est extrait (`git archive`), jamais une
# extraction ni une exécution du reste. Code `b1c7f4b6`. Le dépôt de lancement doit contenir ces commits et ceux des
# questions (`git fetch origin canal/gemini-organisme-v5-3 canal/gemini-organisme-v6 canal/conv-audit-n04 main`). Chaque
# appel de ce lanceur est une commande de fond de la session avec le délai maximal (7 200 000 ms), jamais `nohup`, `&` ni
# `setsid`. Met en œuvre le préenregistrement scellé
# `essaim-m3-refonte-v1/prereg/pilote3-gemini-organisme-v5-3-v6-v1.md` (ou la version qui le remplace et cite ce script).
#
# Usage :
#   MODE=reel COURSE=v5-3 DEPOT=… PYTHON=… PREREG=… PREREG_SHA256=… GRAINE=… RESTE_GO_USD=… \\
#       APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE="…" CLE_ANTHROPIC=NOM CLE_GEMINI=NOM [CLE_BRAVE=NOM] \\
#       [CLE_OPENALEX=NOM] [CLE_S2=NOM] [TENTATIVE=2] REFERENCE_M=<dossier du pilote de la course M> \\
#       bash lancer_pilote3_gemini_v5_3_v6_v1.sh
#   MODE=reel COURSE=v6 … (même forme)
#   MODE=simulation COURSE=… DEPOT=… PYTHON=… GRAINE=… [REFERENCE_M=… PILOTE_RACINE=… REGISTRE_GO_SOURCE=…
#       DEPENSES_SOURCE=… RESTE_GO_USD=… PREREG=… PREREG_SHA256=… APPEL_CONTROLE_FICHIER=… RECHARGE_ATTESTEE=…
#       ESSAI_ARTEFACT=… ESSAI_JUNIT_EXISTANT=… ESSAI_RESUME_EXISTANT=… ESSAI_EXIGER_HEURE=1 ESSAI_PASSERELLE_PY=…]
#
# Jamais : afficher, écrire ou journaliser une clé ; lire un score ; ouvrir la course ou la sortie standard ; arrêter un
# processus (R10 : PID consigné ; une course voisine est détectée, jamais arrêtée) ; écraser un dossier (R12) ; lancer
# une seconde course de même nom (R3).
"""
texte = ENTETE + texte[fin:]

# 2. Courses : objet par course, question M v2 pour les deux
remplacer('''COURSE="${COURSE:?COURSE=structure ou COURSE=maieutique}"
case "$COURSE" in
  structure)
    NOM="pilote2-gemini-v5-2-1-structure-v1"; INDICE_GRAINE=1
    COMMIT_QUESTION=4772b525081342a6a30ba8823733aa5770a888a8
    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-apprendre-structure-entrainement-generations-organismes-v2.md
    SHA_QUESTION=a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289;;
  maieutique)
    NOM="pilote2-gemini-v5-2-1-maieutique-v1"; INDICE_GRAINE=0
    COMMIT_QUESTION=a15809b816b6c967b6c3cf21877e350bfe676dca
    CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-gemini-maieutique-vs-coercition-organismes-v2.md
    SHA_QUESTION=8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd;;
  *) refus_tot "COURSE inconnue : $COURSE (structure ou maieutique)";;
esac
''', '''COURSE="${COURSE:?COURSE=v5-3 ou COURSE=v6}"
# Question M v2 épurée (la même que celle de la course M du second pilote), pour les deux courses
COMMIT_QUESTION=a15809b816b6c967b6c3cf21877e350bfe676dca
CHEMIN_QUESTION=brouillons/canal-reprise-releve-v1/envois/question-gemini-maieutique-vs-coercition-organismes-v2.md
SHA_QUESTION=8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd
case "$COURSE" in
  v5-3)
    NOM="pilote3-gemini-v5-3-maieutique-v1"; INDICE_GRAINE=0
    COMMIT_ORGANISME=4ecba58bcaa7dc3abe82c54fc38ee7285620bdf6
    ARBRE_ORGANISME=6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753
    N_FICHIERS_ORGANISME=22
    LIGNEE="gemini-organisme-v5-3";;
  v6)
    NOM="pilote3-gemini-v6-maieutique-v1"; INDICE_GRAINE=1
    COMMIT_ORGANISME=7cd7508287efa6fd667eaca7dffe23666f12692f
    ARBRE_ORGANISME=940c59c3dd58fdd5355244768faa1e9da02620fa455cd8ead15f8271145da64a
    N_FICHIERS_ORGANISME=24
    LIGNEE="gemini-organisme-v6";;
  *) refus_tot "COURSE inconnue : $COURSE (v5-3 ou v6)";;
esac
''')

# 3. GO et plafonds
remplacer('''GO_ID=GO-2026-10-25-01
USD_GEN=30      # par génération (décision (b) de Lazar, 25 octobre 10:17 Paris)
USD_COURSE=60   # par course ; deux courses : 120 USD au plus (GO-2026-10-25-01, R-407 et R-409)
''', '''GO_ID=GO-2026-10-25-02
USD_GEN=30      # par génération (mêmes bornes que la course M ; décision (b) de Lazar, 25 octobre 10:17 Paris)
USD_COURSE=60   # par course ; deux courses : 120 USD au plus (GO-2026-10-25-02, mot direct de Lazar dans la session de session-depot)
''')

# 4. Constantes de l'objet : désormais par course (bloc COURSE)
remplacer('''COMMIT_ORGANISME=ec8e0b6c82d18a7ca040302538dcd33e557bf818
[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567
ARBRE_ORGANISME=fec005c6626b3d1aa960702e4322b44ade3b902157dd84eae8e658b70e4f43f4
N_FICHIERS_ORGANISME=21
''', '''[ "$ART" = commit ] && COMMIT_QUESTION=0123456789abcdef0123456789abcdef01234567
''')
remplacer('''LIGNEE="gemini-organisme-v5-2-1"
# Chemins que les commits postérieurs à b1c7f4b6 peuvent toucher (ce texte, ses pièces, sa contre-lecture) ; dossier des pilotes
PERMIS_APRES_CODE='^essaim-m3-refonte-v1/prereg/(pilote2-gemini-organisme-v5-2-v[0-9]+\\.md(\\.sha256)?|pieces-pilote2-gemini-v5-2/.+|contre-lectures/pilote2-gemini-organisme-v5-2-v[0-9]+-cl[0-9]+\\.md(\\.sha256)?)$'
''', '''# Chemins que les commits postérieurs à b1c7f4b6 peuvent toucher : le texte du second pilote, ses pièces et ses
# contre-lectures ; ce texte, ses pièces et ses contre-lectures ; dossier des pilotes
PERMIS_APRES_CODE='^essaim-m3-refonte-v1/prereg/(pilote2-gemini-organisme-v5-2-v[0-9]+\\.md(\\.sha256)?|pieces-pilote2-gemini-v5-2/.+|contre-lectures/pilote2-gemini-organisme-v5-2-v[0-9]+-cl[0-9]+\\.md(\\.sha256)?|pilote3-gemini-organisme-v5-3-v6-v[0-9]+\\.md(\\.sha256)?|pieces-pilote3-gemini-v5-3-v6/.+|contre-lectures/pilote3-gemini-organisme-v5-3-v6-v[0-9]+-cl[0-9]+\\.md(\\.sha256)?)$'
''')

# 5. Étape (0) : course M de référence (liste close du lanceur source, appliquée à M)
debut0 = texte.index("# 0. Course S : ne part que si la course M est saine")
fin0 = texte.index("# 1. Code identique à b1c7f4b6")
ancien0 = texte[debut0:fin0]
for a in ('[ "$COURSE" = structure ] && { [ "$MODE" = reel ] || [ -n "${PRECEDENTE_PILOTE:-}" ]; }',
          "' \"$SP\" \"$SHA_LANCEUR\" \"$LIGNEE\" \"$MODE\" \"$GO_ID\" \"$(basename \"$0\")\")\""):
    assert ancien0.count(a) == 1, a
# Le bloc Python de la liste close est repris mot pour mot (lignes 211 à 256 de la source)
py_debut = ancien0.index("import json, re, sys\n")
py_fin = ancien0.index("' \"$SP\" \"$SHA_LANCEUR\"")
bloc_py = ancien0[py_debut:py_fin]
assert 'if not re.search(r"^- course : maieutique ;", lan, re.M): pb.append("ce n est pas la course M")' in bloc_py
nouveau0 = '''# 0. Course M de référence : une course du pilote 3 ne part qu'après une course M du second pilote finie, fermée et
#    saine — liste close du lanceur du second pilote (P2C1-01, P52C1-02), appliquée telle quelle aux pièces lisibles de M,
#    avec le nom, l'empreinte et la lignée du lanceur et de l'objet de M ; graine de M lue dans le texte scellé du second
#    pilote ; la ligne de dépense de la course porte les 16 premiers caractères de l'empreinte des empreintes de M
#    (les noms EMP_S, GRAINE_S_MANIFESTE et issue_s sont ceux du lanceur source ; ils portent ici les valeurs de M)
EMP_S=""
LANCEUR_M_NOM=lancer_pilote2_gemini_v5_2_v5.sh
LANCEUR_M_SHA=83f8b9cf8f3062dfc5e2c02094c602a2d582adf0cbcef292d5bdccd8f8d61b1b
LIGNEE_M="gemini-organisme-v5-2-1"
GO_M=GO-2026-10-25-01
PREREG_M="$R/prereg/pilote2-gemini-organisme-v5-2-v2.md"
PREREG_M_SHA=d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b
if [ "$MODE" = reel ] || [ -n "${REFERENCE_M:-}" ]; then
  [ -n "${REFERENCE_M:-}" ] || refus "REFERENCE_M non défini : une course du pilote 3 ne part qu'après une course M saine (dossier du pilote de la course M)"
  SP="$REFERENCE_M"
  [ -d "$SP" ] || refus "REFERENCE_M $SP absent : une course du pilote 3 ne part qu'après M"
  SP="$(cd "$SP" && pwd -P)"
  if [ "$MODE" = reel ]; then
    case "$SP/" in /root/*|/home/*) ;; *) refus "REFERENCE_M $SP hors de /root et de /home";; esac
    [[ "$(basename "$SP")" =~ ^pilote2-gemini-v5-2-1-maieutique-v1(-tentative[0-9]+)?$ ]] || refus "REFERENCE_M $SP : nom autre que pilote2-gemini-v5-2-1-maieutique-v1[-tentativeN]"
  fi
  [ -f "$SP/EMPREINTES-pilote-v1.txt" ] && [ -f "$SP/EMPREINTES-pilote-v1.txt.sha256" ] || refus "empreintes de M absentes : une course du pilote 3 ne part qu'après une course M finie et fermée"
  (cd "$SP" && sha256sum -c --quiet EMPREINTES-pilote-v1.txt.sha256 && sha256sum -c --quiet EMPREINTES-pilote-v1.txt) > /dev/null 2>&1 || refus "empreintes de M non vérifiées (fichiers de M modifiés ou manquants)"
  for f in LANCEMENT.md extrait-mecanique-v1.json; do
    grep -Eq "^[0-9a-f]{64}  $f\\$" "$SP/EMPREINTES-pilote-v1.txt" || refus "empreintes de M sans $f"
  done
  EMP_S="$(cut -d' ' -f1 < "$SP/EMPREINTES-pilote-v1.txt.sha256")"
  issue_s="$("$PY" -I -c '
''' + bloc_py + '''' "$SP" "$LANCEUR_M_SHA" "$LIGNEE_M" "$MODE" "$GO_M" "$LANCEUR_M_NOM")" || refus "la course $COURSE ne part pas : issue de M hors de la liste saine ($issue_s) — décision de Lazar requise"
  GRAINE_S_MANIFESTE="$("$PY" -I -c 'import json, sys; print((json.load(open(sys.argv[1])).get("manifeste") or {}).get("entropie_seed_sequence"))' "$SP/extrait-mecanique-v1.json")"
  [ -f "$PREREG_M" ] && [ "$(sha256sum "$PREREG_M" | cut -d' ' -f1)" = "$PREREG_M_SHA" ] || refus "texte scellé du second pilote absent ou d'empreinte autre que d2944654… ($PREREG_M)"
  grep -q "graine de la course maieutique = $GRAINE_S_MANIFESTE\\b" "$PREREG_M" || refus "la course M a tourné avec la graine $GRAINE_S_MANIFESTE, qui n'est pas la graine M du texte scellé du second pilote"
  note "- course M de référence : $SP ; $issue_s ; empreintes de M vérifiées (EMPREINTES-pilote-v1.txt, sha256 $EMP_S) ; graine $GRAINE_S_MANIFESTE = graine M du texte scellé du second pilote (d2944654…)"
fi

'''
texte = texte[:debut0] + nouveau0 + texte[fin0:]

# 6. Étape (2) : plus de vérification « graine de M » contre ce texte (faite à l'étape 0 contre le texte du second pilote)
remplacer('''  if [ "$COURSE" = structure ] && [ -n "${GRAINE_S_MANIFESTE:-}" ]; then
    grep -q "graine de la course maieutique = $GRAINE_S_MANIFESTE\\b" "$PREREG" || refus "la course M a tourné avec la graine $GRAINE_S_MANIFESTE, qui n'est pas la graine M du préenregistrement scellé"
    note "- course M : graine $GRAINE_S_MANIFESTE = graine M du préenregistrement"
  fi
''', '')

# 7. Étape (3) : objet de la course
remplacer('''# 3. Organisme v5.2.1 et question, extraits des commits cités, vérifiés''',
          '''# 3. Organisme de la course (v5.3 ou v6, dossier organisme/ seul) et question, extraits des commits cités, vérifiés''')
remplacer('''refus "empreinte d'arbre de l'organisme ≠ fec005c6…"''',
          '''refus "empreinte d'arbre de l'organisme ≠ ${ARBRE_ORGANISME:0:8}…"''')

# 8. Étape (4) : registre ; dépense après M
remplacer('''# 4. Registre des GO : une ligne « | GO-2026-10-25-01 | » qui porte « calcul » et l'empreinte (8 premiers caractères) de
#    la question de la course ; dépense consignée avant (une ligne nommant la course et le GO) ; reste ≥ plafond de la course''',
          '''# 4. Registre des GO : une ligne « | GO-2026-10-25-02 | » qui porte « calcul », l'empreinte (8 premiers caractères) de
#    la question et celle de l'objet de la course ; dépense consignée avant (une ligne nommant la course, le GO et
#    l'empreinte des empreintes de M) ; reste ≥ plafond de la course''')
remplacer('''refus "la ligne de dépense de S ne porte pas l'empreinte des empreintes de M (${EMP_S:0:16}…), écrite après la fin de M"''',
          '''refus "la ligne de dépense de la course $COURSE ne porte pas l'empreinte des empreintes de M (${EMP_S:0:16}…), écrite après la fin de M"''')

DST.write_text(texte, encoding="utf-8")
print(hashlib.sha256(texte.encode("utf-8")).hexdigest())
