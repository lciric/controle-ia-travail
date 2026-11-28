#!/usr/bin/env bash
# Répétition jouet de la chaîne de l'instance de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1),
# R-269), MODE=jouet, au commit C du dépôt de travail (module de P4 et chaîne versés sous docs/procedures/P4-instrument-v1/),
# v1, déclinée de docs/procedures/P3-premier-test-v2/repetition_jouet_p3_v1.sh sous un nom neuf (R12).
# Dépôt jetable : clone partagé de D (objets lus par référence, aucune écriture dans D), commit d'essai tiré de C sans les
# PDF de docs/sources/ (place disque de la machine de la session ; hors de l'arbre gelé, que le run compare à celui de
# P3) ; dépôt nu local en guise de dépôt distant ; jetons factices de 8 caractères au moins, les mêmes à l'instance jouet
# et à la récupération ; env -i ; PYTHONDONTWRITEBYTECODE=1. Monde jouet : run jouet de P3 des tests du module (code gelé
# de P3, modèle jouet, données synthétiques) copié dans le clone ; configuration jouet de P4 au chemin réel ;
# préenregistrement jouet = le candidat CANDIDAT dont quatre citations seulement changent, une fois chacune (empreinte
# canonique de la configuration, tests collectés, entropie et révision du modèle jouet) ; textes honnêtes synthétiques
# des fenêtres (aucun texte de P3 n'est lu). Le candidat doit citer, pour chacun des six fichiers du module, l'empreinte
# du fichier de C, et un commit du code dont l'arbre gelé égale celui de C. Le commit d'essai verse aussi, sous
# docs/procedures/P4-instrument-v1/, la copie de la récupération des gardes réelles, scellée : c'est la « copie versée à
# S » de ce cas. Passages, par l'amorce et le script de l'instance de C :
#   1. cas sain : BRANCHE=calcul/p4-jouet-a-v1 → code 0 : suite complète des tests (dépôt et module), run jouet de P4,
#      résultats, tableaux et traces poussés ;
#   2. artefact : même branche, déjà présente → arrêt avant l'installation (code 2) ;
#   3. lancement manqué : BRANCHE=calcul/p4-jouet-b-v1, environnement absent (cause d'infrastructure simulée, après la
#      poussée initiale) → code 1, traces poussées, aucun run ;
#   4. plafond de l'amorce : copie de l'amorce dont seul le plafond change (150 minutes → 1 minute, ligne comptée),
#      BRANCHE=calcul/p4-jouet-p-v1 → TERM pendant les tests, arrêt consigné, traces poussées, code 124.
# Puis la récupération de P4 (copies dont changent l'adresse du dépôt, la branche, le motif du run, le mode attendu, la
# ligne « disponible », le fichier des textes des fenêtres et, hors des cas des gardes réelles, la carte, les versions
# et la copie non exigées), sur des branches tirées de a-v1 sans lire ni afficher aucun texte d'action, chacune poussée
# par « instance de calcul (P4) », avec un faux outil de location (destruction journalisée, jamais appelée réellement) :
# six cas sains — a-v1 (code 0) ; b-v1 et p-v1 (traces seules, code 4) ; e-v1 = a-v1 changée en arrêt synthétique
# pendant les bras (tableaux des bras et identité retirés, résumé avec motif et partie « partiel », ligne de fin
# retirée ; code 0) ; g-v1 = a-v1 plus une carte A100 SXM4 factice, jouée par la copie versée, gardes 0, 3f et 6b dans
# leur forme réelle (code 0) ; a-v1 relue en vérifiant que la fenêtre d'un seul caractère répété (points) d'un texte
# dégénéré est bien présente dans une trace et ignorée (code 0) — chaque cas sain finit par la destruction de l'instance
# par son identifiant — ; la lecture jouet de P4 (module v2 : lecture sans --prereg du run décisif
# de a-v1 refusée sans rien écrire ; run jouet non décisif lancé sur a-v1, avec l'entropie du préenregistrement jouet,
# complet exigé, puis lu sans --prereg, code 0, issue écrite) ;
# et dix-neuf artefacts, un seul KO attendu chacun, instance non détruite :
#   scores absents (4c) ; validation absente (4c) ; fichier de textes ajouté (1c) ; scores altérés et rescellés (2b) ;
#   sceau des scores faux (2b) ; identité rattachée au manifeste d'un autre run (2b) ; scores hors du plan (4d) ; chaîne
#   longue dans un tableau (4d) ; texte honnête recopié dans le journal (4f) ; texte sur deux lignes recopié dans le
#   résumé, échappé en JSON (4f) ; chaîne de plus de 200 caractères dans le résumé (4f) ; ligne de fin retirée d'un run
#   complet (6f) ; jeton dans une trace (7) ; copie versée plus une ligne (0) ; run de référence des versions autre
#   (3f) ; carte A100 PCIE de 40 Gio (6b) ; étiquette de l'instance autre que « p4-v1 » (8, destruction refusée) ;
#   destruction en échec (8) ; instance encore listée après la destruction (8).
# Chaîne v2 :
#   5. arrêt du module pendant le run (RC-fidelite-07) : commit d'essai de l'arrêt (configuration jouet dont seule
#      `duree_max_s` change, 0,001 s, et préenregistrement jouet qui la cite), BRANCHE=calcul/p4-jouet-r-v1 → le module
#      s'arrête à sa première échéance, écrit le résumé avec son motif, l'instance consigne l'arrêt et pousse les
#      partiels (code 1) ; sa récupération, sur le commit d'essai de l'arrêt, est conforme (code 0, motif d'arrêt
#      affiché par le filtre, destruction) ;
#   la récupération prend les traces du lancement (lancement.txt factice : commit, création, identifiant) ; huit
#   artefacts neufs (texte échappé dans une trace, texte sans sa fenêtre du milieu, texte dans les traces seules,
#   validation à 4 096 colonnes, longueurs par jeton doublées, motif d'arrêt qui recopie un texte, jeton dans les traces
#   seules, étiquette « p4-v1 x »), chacun à un seul KO, instance gardée avec son état et l'heure limite de
#   destruction ; deux refus en code 2 (place disque, traces d'un autre lancement) ; aucune fenêtre d'un texte ni aucun
#   jeton dans les sorties des récupérations ; le module commun versé à C est celui du bloc-notes (la récupération le
#   lit au commit S) et il est répété.
# Chaîne v3 (traitement des vérifications de la chaîne v2) :
#   - VC2-depense-03 : refus de la place disque (RX01) : état de l'instance et heure limite écrits avant la sortie en
#     code 2 ; troisième refus en code 2, clonage impossible (RX02 : copie dont seule l'adresse du dépôt distant change,
#     vers un dépôt absent), avec l'état et l'heure limite ;
#   - VC2-donnees-01 : artefact « repli de l'affichage » : copie de la récupération de l'artefact « motif d'arrêt qui
#     recopie un texte » dont seul le chemin du module commun lu à S change (vers un fichier absent de S : module commun
#     de S vide) ; attendus : code 1, KO 4f, aucune destruction, chaque ligne filtrée réduite à ses 40 premiers
#     caractères, sa longueur et son empreinte courte (la ligne « 4a arrêt » comprise), la ligne de l'instance gardée
#     réécrite entière à la fin ; puis la recherche des fenêtres et des jetons dans toutes les sorties (comme avant).
# Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) :
#   6. délai externe du run (VC2-fidelite-07) : commit d'essai du délai, copie du script de l'instance dont seule la
#      ligne DELAI change (90 minutes → DELAI_ESSAI, réglé dans la fenêtre mesurée du run jouet : après l'écriture du
#      manifeste, avant la fin ; ligne comptée), BRANCHE=calcul/p4-jouet-s-v1, joué après les passages 1 et 5, seul
#      pendant son run → TERM du `timeout` pendant le run, arrêt consigné par le module (résumé avec motif), code 124 du
#      run, partiels poussés (code 1) ; sa récupération, sur le commit d'essai du délai, est conforme (code 0, motif
#      « signal TERM reçu (délai externe du run… » affiché par le filtre, destruction) ;
#   - VC2-fidelite-03 : heure limite de destruction relue dans arret.txt (passage 1 : arret.txt factice de cette
#     instance), repli déclaré sans lui (passage 3) ou avec un arret.txt d'une autre instance (gardes réelles), et
#     dépassée (cas sain « limite-depassee » : création vieille de 200 000 s ; ligne écrite, destruction faite) ;
#   - VC2-fidelite-04 : refus en code 2 des traces d'un autre lancement, avec l'état de l'instance et l'heure limite ;
#   - VC2-fidelite-08 : repli de l'affichage à la forme la plus stricte, éprouvé par deux artefacts : « repli de
#     l'affichage » (module commun de S illisible) et « textes absents » (copie de la même récupération dont seul le
#     chemin des textes honnêtes de S change, vers un fichier absent de S) ; attendus : code 1, KO 4f de forme fixe,
#     aucune destruction, chaque autre ligne entière seulement si c'est une ligne OK, KO ou « -- » (forme fixe), sinon
#     réduite à sa longueur et son empreinte courte (la ligne « 4a arrêt » réduite), la ligne de l'instance gardée
#     réécrite entière à la fin.
# Le journal commence par « commit du code répété : <C entier> » et « candidat répété : <nom> <sha256> », puis
# « script répété : <nom> <sha256> » pour chaque script de la chaîne exécuté (copiés au début dans RACINE/scripts et
# joués depuis ces copies), que les contrôles avant dépense comparent aux copies versées à S. Temps de chaque passage.
# Usage : repetition_jouet_p4_v1.sh C CANDIDAT RACINE_NEUVE [DEPOT]
#   DEPOT (facultatif ; chaîne v2) : dépôt qui porte C, lu par référence (défaut : le dépôt de travail) ; il permet de
#   répéter sur un C d'essai sans copie changée du script (le journal cite alors l'empreinte du script lui-même).
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
[ $# -eq 3 ] || [ $# -eq 4 ] || { echo "usage : repetition_jouet_p4_v1.sh C CANDIDAT RACINE_NEUVE [DEPOT]"; exit 2; }
C=$1; CANDIDAT=$(realpath "$2"); R=$(realpath -m "$3")
SOI=$(realpath "$0")
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4
VENV=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf
PY=$VENV/bin/python
D=${4:-/home/user/controle-ia-travail}
V=docs/procedures/P4-instrument-v1
JETON_GH=factice-gh-0000; JETON_HF=factice-hf-0000      # valeurs factices (8 caractères au moins)
RUN_AUTRE=20261004-104156-harnais-factice                # run de référence dont les versions diffèrent (tokenizers absent) : artefact 3f
ID=99999999                                              # identifiant d'instance factice
FENETRES=donnees/synth/textes-fenetres-p3.jsonl
export PYTHONDONTWRITEBYTECODE=1
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
[ -f "$CANDIDAT" ] || { echo "candidat absent"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --shared --no-checkout "$D" source && cd source || exit 2
CE=$(git rev-parse --verify -q "$C^{commit}") || { echo "commit $C introuvable"; exit 2; }
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git symbolic-ref HEAD refs/heads/main && git update-ref refs/heads/main "$CE" && git read-tree "$CE" || exit 2
echo "dépôt répété : $D"
echo "commit du code répété : $CE"
echo "candidat répété : $(basename "$CANDIDAT") $(sha256sum "$CANDIDAT" | cut -d' ' -f1)"
git rm -r -q --cached --ignore-unmatch docs/sources/pdf docs/sources/lecture-pdf-niveau1 docs/sources/lecture-pdf-niveau2 \
    && git commit -q --allow-empty -m "essai : commit de C sans les PDF de docs/sources (place disque)" && git checkout -q -f HEAD || exit 2
GELES=$(git show 7a54d431d89745839220f882b41b13e8c62ecfdd:src/controle_ia/harnais/validation_reelle.py | "$PY" -I -B -c 'import ast, sys
t = ast.parse(sys.stdin.read())
v = [n.value for n in t.body if isinstance(n, ast.Assign) and any(getattr(x, "id", "") == "CHEMINS_GELES" for x in n.targets)]
print(" ".join(ast.literal_eval(v[0])))')
[ -n "$GELES" ] || { echo "CHEMINS_GELES illisible dans 7a54d43"; exit 2; }
# shellcheck disable=SC2086
git diff --quiet "$CE" HEAD -- $GELES || { echo "commit d'essai : arbre gelé ≠ celui de C"; exit 2; }
for n in mesures_conception_p4_v1.py instrument_p4_v1.py lecture_p4_v1.py test_instrument_p4_v1.py test_lecture_p4_v1.py \
         test_gardes_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh verifications_p4_v1.py; do
    [ -f "$V/$n" ] && [ "$(cat "$V/$n.sha256" 2>/dev/null)" = "$(sha256sum "$V/$n" | cut -d' ' -f1)  $n" ] \
        || { echo "$V/$n absent de C ou non scellé"; exit 2; }
done
for n in mesures_conception_p4_v1.py instrument_p4_v1.py lecture_p4_v1.py test_instrument_p4_v1.py test_lecture_p4_v1.py test_gardes_p4_v1.py; do
    grep -qE "^[[:space:]]*-[[:space:]]+Module de P4 : \`$V/$n\` : \`$(sha256sum "$V/$n" | cut -d' ' -f1)\`[[:space:]]*\$" "$CANDIDAT" \
        || { echo "le candidat ne cite pas $V/$n de C à son empreinte"; exit 2; }
done
CODE_CITE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$CANDIDAT")
[ "$(grep -c "Commit du code d'analyse : \`" "$CANDIDAT")" = 1 ] && [[ "$CODE_CITE" =~ ^[0-9a-f]{40}$ ]] \
    || { echo "commit du code cité absent ou en double dans le candidat"; exit 2; }
# shellcheck disable=SC2086
git diff --quiet "$CODE_CITE" HEAD -- $GELES 2>/dev/null || { echo "le commit du code cité par le candidat n'a pas l'arbre gelé de C"; exit 2; }
cmp -s "$V/verifications_p4_v1.py" "$H/verifications_p4_v1.py" || { echo "module commun versé à C ≠ celui du bloc-notes (la récupération le lit au commit S)"; exit 2; }
echo "scripts de l'instance répétés (C) : amorce $(sha256sum "$V/amorce_instance_p4_v1.sh" | cut -d' ' -f1) ; instance $(sha256sum "$V/p4_instance_v1.sh" | cut -d' ' -f1)"
mkdir -p "$R/scripts" || exit 2
SCRIPTS_REPETES="recuperation_p4_v1.sh outils_essais_p4_v1.py verifications_p4_v1.py"
for s in $SCRIPTS_REPETES; do cp "$H/$s" "$R/scripts/$s" || exit 2; done
cp "$SOI" "$R/scripts/repetition_jouet_p4_v1.sh" || exit 2
for s in $SCRIPTS_REPETES repetition_jouet_p4_v1.sh; do echo "script répété : $s $(sha256sum "$R/scripts/$s" | cut -d' ' -f1)"; done
OUTILS="$R/scripts/outils_essais_p4_v1.py"
copie_recuperation() {   # $1 lettre de la branche jouet, $2 sortie, $3 forme : ordinaire, reelles (0, 3f et 6b réels), carte, versions
    local args=(-e "s|^DISTANT=https://github.com/lciric/controle-ia-travail.git\$|DISTANT=$R/distant.git|"
                -e "s|^BRANCHE=calcul/p4-reel-v1\$|BRANCHE=calcul/p4-jouet-$1-v1|" -e "s|-p4-reel\\\$'\$|-p4-jouet\$'|"
                -e 's|^MODE_ATTENDU=reel$|MODE_ATTENDU=jouet|' -e 's|"disponible True"|"disponible False"|'
                -e "s|^TEXTES_P3=[^ ]* |TEXTES_P3=$FENETRES |")
    case "${3:-ordinaire}" in
        reelles) ;;
        carte) args+=(-e 's|^VERSIONS_EXIGEES=oui|VERSIONS_EXIGEES=non|' -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|') ;;
        versions) args+=(-e 's|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|' -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|'
                         -e "s|^RUN_P3=[0-9a-z-]* |RUN_P3=$RUN_AUTRE |") ;;
        *) args+=(-e 's|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|' -e 's|^VERSIONS_EXIGEES=oui|VERSIONS_EXIGEES=non|'
                  -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|') ;;
    esac
    sed "${args[@]}" "$R/scripts/recuperation_p4_v1.sh" > "$2"
    echo "lignes changées dans la copie de la récupération ($(basename "$2"), forme ${3:-ordinaire}) : $(diff "$R/scripts/recuperation_p4_v1.sh" "$2" | grep -c '^>')"
}
DELAI_ESSAI=6s           # sixième passage : délai externe réduit ; run jouet mesuré seul : manifeste écrit à 2,3 à 3,2 s,
                         # résumé complet vers 8,5 s (…/chaine-v4-travail/essai-delai-1.log) : 6 s tombe pendant le run
N=$(PYTHONPATH=src "$PY" -B -m pytest --collect-only -q -p no:cacheprovider tests "$V/test_instrument_p4_v1.py" \
    "$V/test_lecture_p4_v1.py" "$V/test_gardes_p4_v1.py" 2>/dev/null | sed -n 's/^\([0-9]*\) tests\{0,1\} collected.*/\1/p')
echo "tests collectés (dépôt et module) : $N"
[[ "$N" =~ ^[0-9]+$ ]] || { echo "nombre de tests illisible"; exit 2; }
mkdir -p "$R/travail" || exit 2
MONDE=$("$PY" -B "$OUTILS" monde . "$V" "$R/travail" prereg/P4-instrument-config-v1.json 2> "$R/monde.err") \
    || { echo "monde jouet impossible : $(tail -1 "$R/monde.err" | couper 200)"; exit 2; }
CFG_SHA=$(printf '%s' "$MONDE" | python3 -c 'import json, sys; print(json.load(sys.stdin)["config"])')
"$PY" -B "$OUTILS" jouet "$CANDIDAT" prereg/P4-instrument-v1.md . "$CFG_SHA" "$N" > "$R/prereg-jouet.txt" 2>&1 \
    || { echo "préenregistrement jouet impossible : $(tail -1 "$R/prereg-jouet.txt" | couper 200)"; exit 2; }
"$PY" -B "$OUTILS" fenetres "$FENETRES" > "$R/fenetres.txt" 2>&1 || { echo "textes des fenêtres impossibles : $(tail -1 "$R/fenetres.txt")"; exit 2; }
echo "monde jouet : $MONDE ; préenregistrement jouet $(cut -c1-12 "$R/prereg-jouet.txt") ; textes des fenêtres : $(cut -c1-60 "$R/fenetres.txt")"
# copie versée de la récupération pour les gardes réelles (0, 3f, 6b) : jouée telle quelle sur g-v1
copie_recuperation g "$R/recuperation-g.sh" reelles
cp "$R/recuperation-g.sh" "$V/recuperation_p4_v1.sh" && (cd "$V" && sha256sum recuperation_p4_v1.sh > recuperation_p4_v1.sh.sha256) || exit 2
git add -A prereg "$V" diag runs && git add -f donnees || exit 2
git commit -qm "essai : monde jouet de P4 (run jouet de P3, configuration et préenregistrement jouets, textes des fenêtres) et copie versée de la récupération" || exit 2
# shellcheck disable=SC2086
git diff --quiet "$CE" HEAD -- $GELES || { echo "commit d'essai : arbre gelé ≠ celui de C"; exit 2; }
ESSAI=$(git rev-parse HEAD); echo "$ESSAI" > "$R/commit-essai.txt"
# commit d'essai de l'arrêt (cinquième passage, RC-fidelite-07) : seule `duree_max_s` de la configuration jouet change
# (0,001 s), et le préenregistrement jouet qui cite son empreinte canonique ; branche locale « essai-arret »
git checkout -q -b essai-arret || exit 2
cp prereg/P4-instrument-config-v1.json "$R/config-jouet.json" && git rm -q prereg/P4-instrument-config-v1.json \
    prereg/P4-instrument-config-v1.json.sha256 prereg/P4-instrument-v1.md prereg/P4-instrument-v1.md.sha256 || exit 2
ARRET=$("$PY" -B "$OUTILS" config-arret . "$V" "$R/config-jouet.json" prereg/P4-instrument-config-v1.json 0.001 2> "$R/arret.err") \
    || { echo "configuration jouet d'arrêt impossible : $(tail -1 "$R/arret.err" | couper 200)"; exit 2; }
CFG_SHA5=$(printf '%s' "$ARRET" | python3 -c 'import json, sys; print(json.load(sys.stdin)["config"])')
"$PY" -B "$OUTILS" jouet "$CANDIDAT" prereg/P4-instrument-v1.md . "$CFG_SHA5" "$N" > "$R/prereg-jouet-arret.txt" 2>&1 \
    || { echo "préenregistrement jouet de l'arrêt impossible : $(tail -1 "$R/prereg-jouet-arret.txt" | couper 200)"; exit 2; }
git add -A prereg && git commit -qm "essai : configuration jouet d'arrêt (duree_max_s 0,001 s) et préenregistrement jouet qui la cite" || exit 2
# shellcheck disable=SC2086
git diff --quiet "$CE" HEAD -- $GELES || { echo "commit d'essai de l'arrêt : arbre gelé ≠ celui de C"; exit 2; }
ESSAI5=$(git rev-parse HEAD); git checkout -q main || exit 2
echo "commit d'essai de l'arrêt : configuration $ARRET ; préenregistrement jouet $(cut -c1-12 "$R/prereg-jouet-arret.txt")"
# commit d'essai du délai (sixième passage, chaîne v4, VC2-fidelite-07) : copie du script de l'instance dont seule la ligne
# DELAI change (90 minutes → DELAI_ESSAI), rescellée ; branche locale « essai-delai »
git checkout -q -b essai-delai || exit 2
sed "s/^DELAI=(timeout --signal=TERM --kill-after=5m 90m)\$/DELAI=(timeout --signal=TERM --kill-after=5m $DELAI_ESSAI)/" \
    "$V/p4_instance_v1.sh" > "$R/instance-delai.sh" || exit 2
ND=$(diff "$V/p4_instance_v1.sh" "$R/instance-delai.sh" | grep -c '^>')
[ "$ND" = 1 ] || { echo "copie du script de l'instance du sixième passage : $ND ligne(s) changée(s) au lieu d'une"; exit 2; }
cp "$R/instance-delai.sh" "$V/p4_instance_v1.sh" && (cd "$V" && sha256sum p4_instance_v1.sh > p4_instance_v1.sh.sha256) || exit 2
git add "$V/p4_instance_v1.sh" "$V/p4_instance_v1.sh.sha256" && git commit -qm "essai : délai externe du run réduit ($DELAI_ESSAI), sixième passage" || exit 2
# shellcheck disable=SC2086
git diff --quiet "$CE" HEAD -- $GELES || { echo "commit d'essai du délai : arbre gelé ≠ celui de C"; exit 2; }
ESSAI6=$(git rev-parse HEAD); git checkout -q main || exit 2
echo "commit d'essai du délai : lignes changées dans la copie du script de l'instance : $ND (DELAI 90m → $DELAI_ESSAI)"
git clone -q --bare "$R/source" "$R/distant.git" || exit 2
cd "$R"
sed 's/--kill-after=5m 150m /--kill-after=5m 1m /' "$R/source/$V/amorce_instance_p4_v1.sh" > "$R/amorce-plafond.sh"
echo "lignes changées dans la copie de l'amorce du passage 4 : $(diff "$R/source/$V/amorce_instance_p4_v1.sh" "$R/amorce-plafond.sh" | grep -c '^>') (plafond 150 → 1 minute)"
passage() {   # $1 nom, $2 BRANCHE, $3 environnement Python (défaut : celui de la session), $4 amorce (défaut : celle de C),
              # $5 commit (défaut : le commit d'essai)
    local n=$1 b=$2 venv=${3:-$VENV} amorce=${4:-$R/source/$V/amorce_instance_p4_v1.sh} commit=${5:-$ESSAI} debut fin code
    mkdir -p "$R/racine-$n" "$R/tmp-$n"
    debut=$(date +%s)
    env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$R/racine-$n" TMPDIR="$R/tmp-$n" COMMIT="$commit" GH_TOKEN="$JETON_GH" HF_TOKEN="$JETON_HF" \
        MODE=jouet DEPOT_URL="$R/distant.git" RACINE_AMORCE="$R/racine-$n" VENV_EXISTANT="$venv" PYTHONDONTWRITEBYTECODE=1 \
        GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=commit.gpgsign GIT_CONFIG_VALUE_0=false \
        BRANCHE="$b" bash "$amorce" > "$R/amorce-$n.log" 2>&1
    code=$?
    fin=$(date +%s)
    echo "passage $n : code $code ; durée totale $((fin - debut)) s"
    grep -h "^AMORCE" "$R/amorce-$n.log" 2>/dev/null | couper 200 | sed 's/^/    | /'
    grep -hE "tests :|run :|arrêt|ARRÊT|TERM|poussée|pip freeze|préenregistrement lu|^PROGRES .* etape=(M5|fin) " "$R/racine-$n/p4/journal.txt" 2>/dev/null \
        | couper 200 | sed 's/^/    | /'
    rm -rf "$R/racine-$n/p4/controle-ia" "$R/racine-$n/amorce-depot" "$R/tmp-$n"
}
# passages 1 et 5 en même temps (chacun joue la suite complète ; dossiers, branches et TMPDIR distincts) ; puis le
# sixième (chaîne v4), lancé seul en arrière-plan : sa suite complète dure plus que les passages 2, 3, 4, les
# récupérations et les artefacts qui suivent, et son run jouet tourne seul (délai réglé sur la durée mesurée du run) ;
# sorties écrites dans l'ordre des passages, la sixième après les artefacts
passage 5-arret-du-module calcul/p4-jouet-r-v1 "$VENV" "$R/source/$V/amorce_instance_p4_v1.sh" "$ESSAI5" > "$R/passage-5.out" 2>&1 &
PID_P5=$!
passage 1-sain calcul/p4-jouet-a-v1 > "$R/passage-1.out" 2>&1
wait "$PID_P5"
passage 6-delai-externe calcul/p4-jouet-s-v1 "$VENV" "$R/source/$V/amorce_instance_p4_v1.sh" "$ESSAI6" > "$R/passage-6.out" 2>&1 &
PID_P6=$!
passage 2-artefact-branche-presente calcul/p4-jouet-a-v1 > "$R/passage-2.out" 2>&1
passage 3-manque calcul/p4-jouet-b-v1 "$R/environnement-absent" > "$R/passage-3.out" 2>&1
passage 4-plafond-de-l-amorce calcul/p4-jouet-p-v1 "$VENV" "$R/amorce-plafond.sh" > "$R/passage-4.out" 2>&1
cat "$R/passage-1.out" "$R/passage-2.out" "$R/passage-3.out" "$R/passage-4.out" "$R/passage-5.out"
git -C "$R/distant.git" branch -a | sed 's/^/branche distante : /'
# faux outil de location de la récupération : état et destruction journalisés dans FAUX_VASTAI_ETAT ; n'appelle rien
mkdir -p "$R/bin-vastai"
cat > "$R/bin-vastai/vastai" <<'EOF'
#!/usr/bin/env bash
E=${FAUX_VASTAI_ETAT:?}
case "$1 $2" in
  "show instance") printf '{"id": %s, "label": "%s", "actual_status": "exited", "cur_state": "stopped", "extra_env": [["GH_TOKEN", "%s"]]}\n' "$3" "${FAUX_ETIQUETTE:-p4-v1}" "${GH_TOKEN:-absent}" ;;
  "destroy instance") echo "destroy instance $3 $4" >> "$E/journal"
      case "${FAUX_DESTRUCTION:-ok}" in echec) echo "erreur factice" >&2; exit 1 ;; ok) touch "$E/detruite-$3" ;; esac
      echo '{"success": true}' ;;
  "show instances") if [ -e "$E/detruite-99999999" ]; then echo '[{"id": 11111111, "label": "rr-autre"}]'
      else echo '[{"id": 99999999, "label": "p4-v1"}, {"id": 11111111, "label": "rr-autre"}]'; fi ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$R/bin-vastai/vastai"
# traces factices du lancement (lancement.txt : commit, création, identifiant de la création), lues par la récupération
traces_lancement() {   # $1 dossier, $2 commit S
    mkdir -p "$1" && printf 'commit %s\ncreation %s\nsuccès : True ; identifiant %s ; message : essai\n' "$2" "$(date -u +%s)" "$ID" > "$1/lancement.txt"
}
traces_lancement "$R/lancement-essai" "$ESSAI"
traces_lancement "$R/lancement-essai-arret" "$ESSAI5"
traces_lancement "$R/lancement-essai-delai" "$ESSAI6"
traces_lancement "$R/lancement-autre" "$CE"
# chaîne v4 (VC2-fidelite-03) : traces d'un lancement créé il y a 200 000 s (heure limite de repli dépassée) ; arret.txt
# factices écrits comme ceux d'arreter_p4_v1.sh, de cette instance et d'une autre
mkdir -p "$R/lancement-ancien" && printf 'commit %s\ncreation %s\nsuccès : True ; identifiant %s ; message : essai\n' "$ESSAI" "$(( $(date -u +%s) - 200000 ))" "$ID" > "$R/lancement-ancien/lancement.txt"
arret_factice() {   # $1 dossier, $2 identifiant
    local fin; fin=$(date -u +%FT%TZ)
    mkdir -p "$1" && printf 'instance %s : étiquette « p4-v1 » relue entière ; état avant l arrêt : running, running\n%s : vastai stop instance %s demandé\n%s : instance %s relue arrêtée deux fois de suite (exited, stopped), 2 lecture(s)\nARRÊT CONFIRMÉ : INSTANCE %s ARRÊTÉE PAR SON IDENTIFIANT (%s)\n' \
        "$2" "$fin" "$2" "$fin" "$2" "$2" "$fin" > "$1/arret.txt"
}
arret_factice "$R/arret-essai" "$ID"
arret_factice "$R/arret-autre" 88888888
# faux df : place disque fixée pour le seul cas de la place insuffisante
mkdir -p "$R/bin-df"
printf '#!/usr/bin/env bash\nprintf "Filesystem 1024-blocks Used Available Capacity Mounted\\n/dev/x 10000000 100 2900000 1%%%% /\\n"\n' > "$R/bin-df/df"
chmod +x "$R/bin-df/df"
recuperer() {   # $1 nom, $2 copie, puis les variables du faux outil (S_REC : commit S ; TRACES_REC : traces du lancement ;
                # chaîne v4 : ARRET_REC, arret.txt passé en cinquième argument)
    local n=$1 copie=$2 c; shift 2
    local a=("${S_REC:-$ESSAI}" "$ID" "${TRACES_REC:-$R/lancement-essai}" "$R/recuperation-$n"); [ -n "${ARRET_REC:-}" ] && a+=("$ARRET_REC")
    mkdir -p "$R/vastai-$n"
    env PATH="$R/bin-vastai:/usr/bin:/bin" HOME="$R" LANG=C.UTF-8 HF_TOKEN="$JETON_HF" CONTROLE_IA_GITHUB_TOKEN="$JETON_GH" \
        GH_TOKEN="$JETON_GH" VAST_API_KEY=factice-vast-0000 FAUX_VASTAI_ETAT="$R/vastai-$n" PYTHONDONTWRITEBYTECODE=1 "$@" \
        bash "$copie" "${a[@]}" > "$R/recuperation-$n.txt" 2>&1; c=$?
    echo "$c" > "$R/code-$n.txt"
    echo "récupération ($n) : code $c ; $(tail -1 "$R/recuperation-$n.txt")"
    grep -E '^(KO|--)|^    arrêt ' "$R/recuperation-$n.txt" | couper 220 | sed 's/^/    /'
    [ -s "$R/vastai-$n/journal" ] && echo "    destruction demandée au faux outil : $(tr '\n' ' ' < "$R/vastai-$n/journal")"
    rm -rf "$R/recuperation-$n" "$R/recuperation-$n.travail"
}
artefact_branche() {   # $1 lettre de la branche, $2 commande à jouer dans le clone, $3 branche de base (défaut : a)
    git clone -q "$R/distant.git" "$R/clone-$1" && git -C "$R/clone-$1" checkout -q -b "$1" "origin/calcul/p4-jouet-${3:-a}-v1" || exit 2
    (cd "$R/clone-$1" && eval "$2") || { echo "artefact $1 : préparation impossible"; exit 2; }
    git -C "$R/clone-$1" add -A && git -C "$R/clone-$1" -c user.name="instance de calcul (P4)" -c user.email=instance@invalid \
        -c commit.gpgsign=false commit -qm "essai : artefact $1" && git -C "$R/clone-$1" push -q origin "$1:refs/heads/calcul/p4-jouet-$1-v1" || exit 2
    rm -rf "$R/clone-$1"
}
# programme des artefacts : joué dans le clone d'une branche ; aucun texte de P3 (textes synthétiques des fenêtres) ; les
# résultats changés sont réécrits au format de `ecrire_resultat` (même manifeste), rescellés
cat > "$R/artefacts.py" <<'EOF'
import hashlib, json, os, sys
from pathlib import Path
import numpy as np
def sha(f):
    return hashlib.sha256(Path(f).read_bytes()).hexdigest()
def resceller(f):
    f = Path(f)
    Path(str(f) + ".sha256").write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")
def run():
    d = [x for x in Path("diag").glob("*-p4-jouet") if x.is_dir()]
    assert len(d) == 1, d
    return d[0], Path("donnees") / d[0].name
def reecrire(chemin, maj):
    corps = json.loads(Path(chemin).read_text(encoding="utf-8"))
    maj(corps["resultat"])
    Path(chemin).write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    resceller(chemin)
def empreintes_des_traces():
    for j in Path("traces").glob("p4-*/journal.txt"):
        (j.parent / "empreintes.sha256").write_text("".join(f"{sha(x)}  {x.name}\n" for x in sorted(j.parent.iterdir())
                                                            if x.name != "empreintes.sha256"), encoding="utf-8")
def journal():
    j = sorted(Path("traces").glob("p4-*/journal.txt"))
    assert j, "aucun journal"
    return j[-1]
def tableau(nom, change):           # tableau changé, rescellé, empreinte reportée au résumé
    d, dd = run()
    f = dd / nom
    with np.load(f, allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    change(t)
    with open(f, "wb") as h:
        np.savez(h, **t)
    resceller(f)
    cle = {"scores-p4.npz": "scores_sha256", "validation-p4.npz": "validation_sha256",
           "jetons-principales-p4.npz": "jetons_principales_sha256"}[nom]
    reecrire(d / "resume.json", lambda r: r.__setitem__(cle, sha(f)))
def textes_fenetres():
    return [json.loads(x)["texte"] for x in Path("donnees/synth/textes-fenetres-p3.jsonl").read_text(encoding="utf-8").splitlines()
            if json.loads(x)["condition"] == "honnete" and len(set(json.loads(x)["texte"])) > 1]
quoi = sys.argv[1]
d, dd = run() if quoi not in ("texte_traces_seules", "jeton_traces_seules") else (None, None)   # traces seules : aucun run
if quoi == "arret_synthetique":       # arrêt pendant les bras : tableaux des bras et identité retirés, résumé avec motif
    r = json.loads((d / "resume.json").read_text(encoding="utf-8"))["resultat"]
    for x in (dd / "scores-p4.npz", dd / "jetons-principales-p4.npz", d / "identite-p4.json"):
        x.unlink(); Path(str(x) + ".sha256").unlink()
    partiel = {k: r[k] for k in ("commit_cite", "config_sha256", "instrument_fige", "module_cite", "validation_sha256")}
    def arret(x):
        x.clear()
        x.update({"arret": {"motif": "essai : arrêt simulé pendant les bras", "etape": "bras D, H, B, B′", "garde": None},
                  "partiel": partiel, "duree_s": r["duree_s"]})
    reecrire(d / "resume.json", arret)
    for j in Path("traces").glob("p4-*/journal.txt"):
        j.write_text("".join(l for l in j.read_text(encoding="utf-8").splitlines(True)
                             if " etape=fin " not in l + " " and " etape=bras tache=" not in l + " "), encoding="utf-8")
        (j.parent / "run.json").write_text("", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "ajout_hors_perimetre":   # un fichier de textes ajouté à côté des tableaux (P4 n'en écrit aucun)
    (dd / "textes-p4.jsonl").write_text('{"texte": "essai"}\n', encoding="utf-8")
    os.system(f"git add -f {dd}/textes-p4.jsonl")
elif quoi == "scores_alteres":        # un score changé, tableau rescellé, résumé non mis à jour
    f = dd / "scores-p4.npz"
    with np.load(f, allow_pickle=False) as z:
        t = {k: z[k] for k in z.files}
    s = t["scores"].copy(); s[tuple(np.argwhere(np.isfinite(s))[0])] += 1.0; t["scores"] = s
    with open(f, "wb") as h:
        np.savez(h, **t)
    resceller(f)
elif quoi == "sceau_des_scores_faux":
    (dd / "scores-p4.npz.sha256").write_text(f"{'0' * 64}  scores-p4.npz\n", encoding="utf-8")
elif quoi == "resultat_autre_manifeste":   # identité rattachée au manifeste d'un autre run du dépôt, rescellée
    autre = Path("runs/20261019-230011-p3-reel")
    f = d / "identite-p4.json"
    corps = json.loads(f.read_text(encoding="utf-8"))
    corps["run_id"], corps["manifeste_sha256"] = autre.name, sha(autre / "manifeste.json")
    f.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    resceller(f)
elif quoi == "scores_hors_plan":       # pas des deux premières lignes échangés : chaque ligne n'est plus à sa place du plan
    def ch(t):
        p = t["pas"].copy(); p[[0, 1]] = p[[1, 0]]; t["pas"] = p
    tableau("scores-p4.npz", ch)
elif quoi == "chaine_longue_dans_un_tableau":
    def ch(t):
        n = t["noms_sondes"].astype("<U120"); n[0] = "sonde-" + "x" * 100; t["noms_sondes"] = n
    tableau("scores-p4.npz", ch)
elif quoi == "texte_dans_le_journal":  # un texte honnête (fenêtres) recopié dans le journal
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + textes_fenetres()[0].replace("\n", " ") + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_echappe":          # texte sur deux lignes dans le résumé : échappé en JSON (fenêtre à cheval)
    x = [t for t in textes_fenetres() if "\n" in t[(len(t) - 48) // 2:(len(t) - 48) // 2 + 48] and len(t) <= 200]
    assert x, "aucun texte des fenêtres dont la fenêtre chevauche un saut de ligne"
    reecrire(d / "resume.json", lambda r: r.__setitem__("note_essai", x[0]))
elif quoi == "chaine_de_plus_de_200":
    reecrire(d / "resume.json", lambda r: r.__setitem__("note_essai", "x" * 250))
elif quoi == "fin_retiree":
    j = journal()
    j.write_text("".join(l for l in j.read_text(encoding="utf-8").splitlines(True) if " etape=fin " not in l + " "), encoding="utf-8")
    empreintes_des_traces()
elif quoi == "jeton_dans_une_trace":
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + "fuite " + os.environ["JETON_FUITE"] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_echappe_trace":   # texte dont la fenêtre du milieu chevauche un saut de ligne, échappé en JSON, dans run.err
    x = [t for t in textes_fenetres() if "\n" in t[(len(t) - 48) // 2:(len(t) - 48) // 2 + 48]]
    assert x, "aucun texte des fenêtres dont la fenêtre du milieu chevauche un saut de ligne"
    e = journal().parent / "run.err"
    e.write_text(e.read_text(encoding="utf-8") + "Traceback (essai) : " + json.dumps(x[0]) + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_sans_milieu":     # tout le texte sauf ses 48 caractères du milieu, dans run.err
    t = textes_fenetres()[0]; m = (len(t) - 48) // 2
    e = journal().parent / "run.err"
    e.write_text(e.read_text(encoding="utf-8") + t[:m] + "\n[...]\n" + t[m + 48:] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "texte_traces_seules":   # branche sans run : un texte recopié dans le journal des traces
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + textes_fenetres()[1] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "jeton_traces_seules":   # branche sans run : un jeton sur la dernière ligne du journal des traces
    j = journal()
    j.write_text(j.read_text(encoding="utf-8") + "fuite " + os.environ["JETON_FUITE"] + "\n", encoding="utf-8")
    empreintes_des_traces()
elif quoi == "validation_4096":       # validation à 4 096 colonnes (forme d'activations), rattachée au résumé
    def ch(t):
        n = len(t["concept"])
        t["noms_sondes"] = np.array([f"dim-{k:04d}" for k in range(4096)]); t["scores"] = np.zeros((n, 4096))
    tableau("validation-p4.npz", ch)
elif quoi == "longueurs_doublees":    # longueurs par jeton doublées, débuts et scores refaits (cohérents entre eux)
    def ch(t):
        L = (t["longueur"] * 2).astype(np.int64)
        t["longueur"] = L
        t["debut"] = (np.concatenate([[0], np.cumsum(L)[:-1]]) if len(L) else np.zeros(0)).astype(np.int64)
        t["scores_0"] = np.concatenate([t["scores_0"], t["scores_0"]]); t["scores_1"] = np.concatenate([t["scores_1"], t["scores_1"]])
    tableau("jetons-principales-p4.npz", ch)
elif quoi == "motif_recopie":         # motif d'arrêt qui recopie un texte (branche d'arrêt synthétique)
    reecrire(d / "resume.json", lambda r: r["arret"].__setitem__("motif", "essai : " + textes_fenetres()[2].replace("\n", " ")))
elif quoi in ("carte_sxm4", "carte_pcie"):
    j = journal()
    ligne = "NVIDIA A100-SXM4-80GB, 580.95.05, 81920 MiB" if quoi == "carte_sxm4" else "NVIDIA A100-PCIE-40GB, 580.95.05, 40960 MiB"
    (j.parent / "nvidia-smi.txt").write_text(f"name, driver_version, memory.total [MiB]\n{ligne}\n", encoding="utf-8")
    empreintes_des_traces()
else:
    raise SystemExit(f"artefact inconnu : {quoi}")
print(f"artefact {quoi} préparé")
EOF
artefact() { "$PY" -I -B "$R/artefacts.py" "$1"; }
# cas sains, chacun suivi de la destruction de l'instance (faux outil)
copie_recuperation a "$R/recuperation-a.sh"
ARRET_REC=$R/arret-essai/arret.txt recuperer passage-1-sain "$R/recuperation-a.sh"
copie_recuperation b "$R/recuperation-b.sh"
recuperer passage-3-traces-seules "$R/recuperation-b.sh"
copie_recuperation p "$R/recuperation-p.sh"
recuperer passage-4-plafond-traces-seules "$R/recuperation-p.sh"
artefact_branche e "artefact arret_synthetique"
copie_recuperation e "$R/recuperation-e.sh"
recuperer arret-synthetique "$R/recuperation-e.sh"
artefact_branche g "artefact carte_sxm4"
cmp -s "$R/recuperation-g.sh" "$R/source/$V/recuperation_p4_v1.sh" || { echo "copie des gardes réelles ≠ copie versée"; exit 2; }
ARRET_REC=$R/arret-autre/arret.txt recuperer gardes-reelles "$R/recuperation-g.sh"
copie_recuperation r "$R/recuperation-r.sh"
S_REC=$ESSAI5 TRACES_REC=$R/lancement-essai-arret recuperer passage-5-arret-du-module "$R/recuperation-r.sh"
# fenêtre d'un seul caractère répété : présente dans une trace de a-v1 (barre de progression des tests), ignorée
git clone -q "$R/distant.git" "$R/clone-w" && git -C "$R/clone-w" checkout -q origin/calcul/p4-jouet-a-v1 || exit 2
if grep -rqF "$(printf '.%.0s' {1..48})" "$R/clone-w"/traces/p4-*/tests.txt; then echo "fenêtre de 48 points présente dans tests.txt de a-v1 : le cas sain qui suit éprouve la règle"
else echo "aucune trace de a-v1 ne porte 48 points de suite : le cas des textes dégénérés ne prouverait rien"; exit 2; fi
rm -rf "$R/clone-w"
copie_recuperation a "$R/recuperation-w.sh"
recuperer textes-degeneres "$R/recuperation-w.sh"
# chaîne v4 (VC2-fidelite-03) : heure limite de repli dépassée (création vieille de 200 000 s) : ligne écrite, sans
# retarder la destruction (cas sain, code 0)
TRACES_REC=$R/lancement-ancien recuperer limite-depassee "$R/recuperation-a.sh"
# lecture jouet (plan v1, section 4, que le plan v2 garde : run de P3 jouet, puis P4 jouet, puis lecture jouet), sur un
# clone de a-v1 (résultats récupérés du passage 1), toujours avec -B et PYTHONDONTWRITEBYTECODE=1. Module v2 (CL3-01) :
# (a) la lecture SANS --prereg du run décisif du passage 1 est refusée sans rien écrire (code 1, arbre inchangé) ;
# (b) un run jouet NON décisif (même configuration jouet, lancé sans --prereg, résultats committés dans le clone) se lit
# sans --prereg, en mode non décisif (code 0, issue écrite). La lecture décisive d'un run jouet n'est pas jouable : le
# mode décisif exige un run source en mode réel et le verdict complété de P3.
git clone -q "$R/distant.git" "$R/clone-l" && git -C "$R/clone-l" checkout -q origin/calcul/p4-jouet-a-v1 || exit 2
git -C "$R/clone-l" config user.email essai@invalid; git -C "$R/clone-l" config user.name essai; git -C "$R/clone-l" config commit.gpgsign false
RUN_A=$(cd "$R/clone-l" && ls -d runs/*-p4-jouet 2>/dev/null | head -1 | xargs -r basename)
[ -n "$RUN_A" ] || { echo "aucun run jouet de P4 sur a-v1 : lecture jouet impossible"; exit 2; }
lire_jouet() {   # $1 run source, $2 run de lecture, $3 sortie
    (cd "$R/clone-l" && env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$R" PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 \
        "$PY" -B "$V/lecture_p4_v1.py" --run-source "$1" --run-lecture "$2" --entropie 4242) > "$3" 2>&1
}
AVANT_L=$(git -C "$R/clone-l" status --porcelain --untracked-files=all | wc -l)
LEC_D="$(date -u +%Y%m%d-%H%M%S)-lecture-p4-jouet-d"
lire_jouet "$RUN_A" "$LEC_D" "$R/lecture-jouet-decisif.txt"; c=$?
if [ "$c" = 1 ] && tail -1 "$R/lecture-jouet-decisif.txt" | grep -qF "lecture sans préenregistrement d'un run décisif ou réel : refusée sans rien écrire" \
   && [ "$(git -C "$R/clone-l" status --porcelain --untracked-files=all | wc -l)" = "$AVANT_L" ] && [ ! -e "$R/clone-l/diag/$LEC_D" ] && [ ! -e "$R/clone-l/runs/$LEC_D" ]; then
    echo "lecture jouet sans --prereg du run décisif (passage-1-sain) : code 1 ; refusée sans rien écrire"
else
    echo "lecture jouet sans --prereg du run décisif (passage-1-sain) : code $c ; refus attendu non établi"
    tail -2 "$R/lecture-jouet-decisif.txt" | couper 200 | sed 's/^/    /'
fi
# run jouet non décisif : même configuration jouet, même entropie que le préenregistrement jouet de a-v1 (le modèle jouet
# en dépend ; sans elle, le module refuse : « modèle jouet autre que celui du run source ») ; il doit finir complet (code
# 0, résumé sans motif d'arrêt), sinon la lecture n'est pas jouée et la ligne « lecture jouet (run-non-decisif) » attendue
# par le module commun n'est pas écrite (un run arrêté se lirait en L2 : jamais un cas sain, aucun repli silencieux)
ENTROPIE_ND=$(sed -n 's/.*Entropie : `\([0-9]\{1,40\}\)`.*/\1/p' "$R/clone-l/prereg/P4-instrument-v1.md")
[ "$(grep -c 'Entropie : `[0-9]*`' "$R/clone-l/prereg/P4-instrument-v1.md")" = 1 ] && [[ "$ENTROPIE_ND" =~ ^[0-9]+$ ]] \
    || { echo "entropie du préenregistrement jouet de a-v1 absente ou en double : run jouet non décisif impossible"; exit 2; }
RUN_ND="$(date -u +%Y%m%d-%H%M%S)-p4-jouet-nd"
(cd "$R/clone-l" && env -i PATH="/usr/bin:/bin" LANG=C.UTF-8 HOME="$R" PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 \
    "$PY" -B "$V/instrument_p4_v1.py" --config prereg/P4-instrument-config-v1.json --run-id "$RUN_ND" --entropie "$ENTROPIE_ND") \
    > "$R/run-non-decisif.txt" 2>&1; c=$?
COMPLET_ND=$(python3 -c 'import json, sys; print("oui" if json.load(open(sys.argv[1]))["resultat"].get("arret") is None else "non")' \
    "$R/clone-l/diag/$RUN_ND/resume.json" 2>/dev/null)
echo "run jouet non décisif ($RUN_ND, sans --prereg, entropie du préenregistrement jouet) : code $c ; complet : ${COMPLET_ND:-illisible}"
[ "$c" = 0 ] || tail -2 "$R/run-non-decisif.txt" | couper 200 | sed 's/^/    /'
if [ "$c" = 0 ] && [ "$COMPLET_ND" = oui ] && (cd "$R/clone-l" && git add -A runs diag && git add -f donnees \
        && git commit -qm "essai : run jouet non décisif") > /dev/null 2>&1; then
    lire_jouet "$RUN_ND" "$(date -u +%Y%m%d-%H%M%S)-lecture-p4-jouet" "$R/lecture-jouet.txt"; c=$?
    LIGNE_L=$(tail -1 "$R/lecture-jouet.txt" | python3 -c 'import json, sys; print(json.load(sys.stdin)["issue"]["ligne"])' 2>/dev/null)
    echo "lecture jouet (run-non-decisif) : code $c ; issue ${LIGNE_L:-illisible}"
    [ "$c" = 0 ] || tail -3 "$R/lecture-jouet.txt" | couper 200 | sed 's/^/    /'
else
    echo "LECTURE JOUET NON JOUÉE : run jouet non décisif en échec, arrêté ou non committé (code $c ; complet : ${COMPLET_ND:-illisible})"
fi
P_CACHE_L=$(find "$R/clone-l" -name __pycache__ -not -path '*/.git/*' 2>/dev/null | head -3)
# (ces lignes ne commencent pas par « lecture jouet » : le module commun en compte exactement deux)
[ -z "$P_CACHE_L" ] && echo "aucun __pycache__ écrit par la lecture jouet dans le clone (-B, PYTHONDONTWRITEBYTECODE=1)" \
    || { echo "__pycache__ ÉCRIT PAR LA LECTURE JOUET : $P_CACHE_L"; exit 1; }
rm -rf "$R/clone-l"
# artefacts : un seul KO attendu chacun, instance non détruite
artefact_branche c 'f=$(git ls-files "donnees/*/scores-p4.npz" | head -1); [ -n "$f" ] && git rm -q "$f" "$f.sha256"'
copie_recuperation c "$R/recuperation-c.sh"
recuperer artefact-scores-manquants "$R/recuperation-c.sh"
artefact_branche m 'f=$(git ls-files "donnees/*/validation-p4.npz" | head -1); [ -n "$f" ] && git rm -q "$f" "$f.sha256"'
copie_recuperation m "$R/recuperation-m.sh"
recuperer artefact-validation-manquante "$R/recuperation-m.sh"
artefact_branche d "artefact ajout_hors_perimetre"
copie_recuperation d "$R/recuperation-d.sh"
recuperer artefact-ajout-hors-perimetre "$R/recuperation-d.sh"
artefact_branche h "artefact scores_alteres"
copie_recuperation h "$R/recuperation-h.sh"
recuperer artefact-scores-alteres "$R/recuperation-h.sh"
artefact_branche i "artefact sceau_des_scores_faux"
copie_recuperation i "$R/recuperation-i.sh"
recuperer artefact-sceau-des-scores-faux "$R/recuperation-i.sh"
artefact_branche j "artefact resultat_autre_manifeste"
copie_recuperation j "$R/recuperation-j.sh"
recuperer artefact-resultat-autre-manifeste "$R/recuperation-j.sh"
artefact_branche l "artefact scores_hors_plan"
copie_recuperation l "$R/recuperation-l.sh"
recuperer artefact-scores-hors-plan "$R/recuperation-l.sh"
artefact_branche q "artefact chaine_longue_dans_un_tableau"
copie_recuperation q "$R/recuperation-q.sh"
recuperer artefact-chaine-longue-dans-un-tableau "$R/recuperation-q.sh"
artefact_branche n "artefact texte_dans_le_journal"
copie_recuperation n "$R/recuperation-n.sh"
recuperer artefact-texte-dans-le-journal "$R/recuperation-n.sh"
artefact_branche x "artefact texte_echappe"
copie_recuperation x "$R/recuperation-x.sh"
recuperer artefact-texte-echappe-dans-un-resultat "$R/recuperation-x.sh"
artefact_branche y "artefact chaine_de_plus_de_200"
copie_recuperation y "$R/recuperation-y.sh"
recuperer artefact-chaine-de-plus-de-200-caracteres "$R/recuperation-y.sh"
artefact_branche f "artefact fin_retiree"
copie_recuperation f "$R/recuperation-f.sh"
recuperer artefact-fin-sans-resume-complet "$R/recuperation-f.sh"
artefact_branche t "export JETON_FUITE=$JETON_HF; artefact jeton_dans_une_trace"
copie_recuperation t "$R/recuperation-t.sh"
recuperer artefact-jeton-dans-une-trace "$R/recuperation-t.sh"
artefact_branche j2 "artefact texte_echappe_trace"
copie_recuperation j2 "$R/recuperation-j2.sh"
recuperer artefact-texte-echappe-dans-une-trace "$R/recuperation-j2.sh"
artefact_branche k2 "artefact texte_sans_milieu"
copie_recuperation k2 "$R/recuperation-k2.sh"
recuperer artefact-texte-sans-sa-fenetre-du-milieu "$R/recuperation-k2.sh"
artefact_branche l2 "artefact texte_traces_seules" b
copie_recuperation l2 "$R/recuperation-l2.sh"
recuperer artefact-texte-dans-les-traces-seules "$R/recuperation-l2.sh"
# jeton de Hugging Face : celui de GitHub est porté par deux variables (CONTROLE_IA_GITHUB_TOKEN et GH_TOKEN, même valeur),
# donc compté deux fois ; un seul KO 7 est attendu de chaque artefact
artefact_branche p2 "export JETON_FUITE=$JETON_HF; artefact jeton_traces_seules" b
copie_recuperation p2 "$R/recuperation-p2.sh"
recuperer artefact-jeton-dans-les-traces-seules "$R/recuperation-p2.sh"
artefact_branche m2 "artefact validation_4096"
copie_recuperation m2 "$R/recuperation-m2.sh"
recuperer artefact-validation-a-4096-colonnes "$R/recuperation-m2.sh"
artefact_branche n2 "artefact longueurs_doublees"
copie_recuperation n2 "$R/recuperation-n2.sh"
recuperer artefact-longueurs-par-jeton-doublees "$R/recuperation-n2.sh"
artefact_branche i2 "artefact motif_recopie" e
copie_recuperation i2 "$R/recuperation-i2.sh"
recuperer artefact-motif-d-arret-qui-recopie-un-texte "$R/recuperation-i2.sh"
# gardes réelles : copie versée plus une ligne (KO 0) ; run de référence des versions autre (KO 3f) ; carte autre (KO 6b)
{ cat "$R/recuperation-g.sh"; echo "# essai : copie qui n'est plus la copie versée"; } > "$R/recuperation-u.sh"
recuperer artefact-copie-non-versee "$R/recuperation-u.sh"
copie_recuperation a "$R/recuperation-v.sh" versions
recuperer artefact-versions-autres "$R/recuperation-v.sh"
artefact_branche k "artefact carte_pcie"
copie_recuperation k "$R/recuperation-k.sh" carte
recuperer artefact-carte-autre "$R/recuperation-k.sh"
# destruction (8) : étiquette autre (refus), destruction en échec, instance encore listée
recuperer artefact-etiquette-autre "$R/recuperation-a.sh" FAUX_ETIQUETTE=p3-v1
recuperer artefact-destruction-en-echec "$R/recuperation-a.sh" FAUX_DESTRUCTION=echec
recuperer artefact-instance-encore-listee "$R/recuperation-a.sh" FAUX_DESTRUCTION=reste
recuperer artefact-etiquette-p4-v1-x "$R/recuperation-a.sh" "FAUX_ETIQUETTE=p4-v1 x"
# refus en code 2 (rien n'est cloné ni détruit) : place disque insuffisante ; traces d'un autre lancement
recuperer artefact-place-disque "$R/recuperation-a.sh" PATH="$R/bin-df:$R/bin-vastai:/usr/bin:/bin"
TRACES_REC=$R/lancement-autre recuperer artefact-traces-d-un-autre-lancement "$R/recuperation-a.sh"
# chaîne v3 (VC2-depense-03, RX02) : clonage impossible (dépôt distant absent) : code 2, état et heure limite écrits
sed "s|^DISTANT=.*|DISTANT=$R/distant-absent.git|" "$R/recuperation-a.sh" > "$R/recuperation-z.sh"
echo "lignes changées dans la copie de la récupération du clonage impossible (recuperation-z.sh, depuis recuperation-a.sh) : $(diff "$R/recuperation-a.sh" "$R/recuperation-z.sh" | grep -c '^>')"
recuperer artefact-clonage-impossible "$R/recuperation-z.sh"
# chaîne v3 (VC2-donnees-01) : repli de l'affichage : module commun de S illisible (chemin vers un fichier absent de S)
sed 's|"$S:$VERSEES/verifications_p4_v1.py"|"$S:$VERSEES/verifications-absent_p4_v1.py"|' "$R/recuperation-i2.sh" > "$R/recuperation-ri.sh"
NR=$(diff "$R/recuperation-i2.sh" "$R/recuperation-ri.sh" | grep -c '^>')
echo "lignes changées dans la copie de la récupération du repli (recuperation-ri.sh, depuis recuperation-i2.sh) : $NR"
recuperer artefact-repli-de-l-affichage "$R/recuperation-ri.sh"
# chaîne v4 (VC2-fidelite-08) : textes honnêtes de S absents (chemin des textes vers un fichier absent de S)
sed "s|^TEXTES_P3=[^ ]* |TEXTES_P3=donnees/synth/textes-absents-p3.jsonl |" "$R/recuperation-i2.sh" > "$R/recuperation-ta.sh"
NT=$(diff "$R/recuperation-i2.sh" "$R/recuperation-ta.sh" | grep -c '^>')
echo "lignes changées dans la copie de la récupération des textes absents (recuperation-ta.sh, depuis recuperation-i2.sh) : $NT"
recuperer artefact-textes-absents "$R/recuperation-ta.sh"
# contrôle du repli à la forme la plus stricte (chaîne v4, VC2-fidelite-08), pour chacun des deux artefacts
for x in "artefact-repli-de-l-affichage:$NR" "artefact-textes-absents:$NT"; do
python3 - "$R/recuperation-${x%%:*}.txt" "$(cat "$R/code-${x%%:*}.txt")" "${x#*:}" "$R/vastai-${x%%:*}/journal" "${x%%:*}" <<'PYR'
import re, sys
from pathlib import Path
sortie, code, nr, journal, nom = sys.argv[1:6]
lignes = Path(sortie).read_text(encoding="utf-8", errors="replace").rstrip("\n").split("\n")
reduite = re.compile(r"^(?:(?:OK|KO|--)  [0-9]{1,2}[a-z]? )?\(ligne de [0-9]+ caractères, empreinte [0-9a-f]{12}\)$")
KO4F = ("KO  4f module commun de S ou textes honnêtes de P3 de S illisibles : recherche des fenêtres et filtre de l'affichage "
        "impossibles (repli : jetons masqués ; seules les lignes OK, KO et -- de forme fixe affichées, les autres par leur "
        "longueur et leur empreinte courte)")
derniere = lignes[-1]
filtrees = lignes[:-1]
constats = {
    "copie à une ligne changée": nr == "1",
    "code 1": code == "1",
    "aucune destruction demandée": not Path(journal).exists() or "destroy" not in Path(journal).read_text(),
    "chaque ligne filtrée réduite (longueur, empreinte), ou ligne OK, KO ou -- entière": bool(filtrees)
        and all(reduite.fullmatch(x) or x[:4] in ("OK  ", "KO  ", "--  ") for x in filtrees),
    "KO 4f de forme fixe, une fois": filtrees.count(KO4F) == 1,
    "ligne « 4a arrêt » réduite": any(re.fullmatch(r"--  4a \(ligne de [0-9]+ caractères, empreinte [0-9a-f]{12}\)", x) for x in filtrees)
        and not any(x.startswith("--  4a arrêt") for x in filtrees),
    "tête de la branche, verdict et lignes libres réduits": not any(x.startswith(("tête de la branche", "RÉCUPÉRATION", "RUN=", "TETE="))
                                                                     for x in filtrees),
    "heure limite écrite entière (forme fixe)": any(x.startswith("--  8 heure limite de destruction ") for x in filtrees),
    "affichage filtré sans échec": not any("AFFICHAGE FILTRÉ EN ÉCHEC" in x for x in lignes),
    "instance gardée réécrite entière à la fin": derniere.startswith("--  8 instance 99999999 gardée, non détruite : état ")
        and "heure limite de destruction" in derniere and not reduite.fullmatch(derniere),
}
if all(constats.values()):
    print(f"récupération en repli de l'affichage ({nom}) : code 1 ; KO 4f ; seules les lignes OK, KO et -- de forme fixe "
          "affichées, les autres par leur longueur et leur empreinte courte ; instance gardée réécrite entière, état et "
          "heure limite de destruction écrits ; aucune destruction")
else:
    print(f"REPLI DE L'AFFICHAGE NON ÉTABLI ({nom}) : " + " ; ".join(k for k, v in constats.items() if not v))
PYR
done
# sixième passage (chaîne v4, VC2-fidelite-07) : attendu, puis sa récupération, sur le commit d'essai du délai
wait "$PID_P6"
cat "$R/passage-6.out"
copie_recuperation s "$R/recuperation-s.sh"
S_REC=$ESSAI6 TRACES_REC=$R/lancement-essai-delai recuperer passage-6-delai-externe "$R/recuperation-s.sh"
# aucun jeton factice affiché par les récupérations (le faux outil en met un dans l'état relu)
FUITES=$(grep -lF -e "$JETON_GH" -e "$JETON_HF" "$R"/recuperation-*.txt 2>/dev/null | head -3 || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché par les récupérations" || { echo "JETON AFFI""CHÉ : $FUITES"; exit 1; }
# aucune fenêtre d'un texte des fenêtres dans les sorties des récupérations (module commun répété ; RC-donnees-03)
if "$PY" -B "$R/scripts/verifications_p4_v1.py" fenetres "$R/source/$FENETRES" "$R"/recuperation-*.txt > "$R/fenetres-affichees.txt" 2>&1; then
    echo "aucune fenêtre affichée par les récupérations"
else echo "FENÊTRE AFFI""CHÉE : $(tail -1 "$R/fenetres-affichees.txt" | couper 160)"; exit 1; fi
rm -rf "$R/source" "$R/distant.git"
echo "FIN DE LA RÉPÉTITION"
