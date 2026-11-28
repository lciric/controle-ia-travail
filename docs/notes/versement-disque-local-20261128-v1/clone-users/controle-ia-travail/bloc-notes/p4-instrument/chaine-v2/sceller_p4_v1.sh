#!/usr/bin/env bash
# Scellement du préenregistrement de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269), v1,
# décliné de docs/procedures/P3-premier-test-v2/sceller_p3_v1.sh sous un nom neuf (R12). Commit S : le texte, la
# configuration et leurs sceaux, et rien d'autre (texte de P4, Chaîne de lancement : « scellement S (texte,
# configuration et sceaux) »). Aucun champ n'est rempli au scellement : le préenregistrement est la copie, octet pour
# octet, du candidat relu et vérifié (contre-lecture 3), la configuration celle de la configuration relue.
# HEAD = origin/main, arbre suivi propre, sorties absentes (R12) ; adresses de origin : le dépôt de travail seulement ;
# vingt et un scripts de la chaîne égaux à leurs copies versées et suivies ; épingles des contrôles lues ici, aucune restée
# « A_EPINGLER » ; candidat et configuration relus à leurs épingles, versés et scellés à la ligne exacte ; le candidat cite
# l'empreinte canonique de la configuration relue ; commit du code cité une fois, d'arbre gelé égal à celui de HEAD et
# à celui de P3 (`7a54d43`, instrument figé) ; intitulés lus par la chaîne et le module : une fois chacun ; journal de la
# répétition jouet à son épingle, au commit répété (module et scripts de l'instance égaux à ceux de HEAD) et au
# candidat relu, conforme (module commun verifications_p4_v1.py, le même texte que les contrôles) ; preuves des essais :
# les huit journaux (bancs et répétition finale ; liste PREUVES_EXIGEES), suivis à HEAD avec leur sceau exact, conformes
# au module commun, et chaque script qu'ils éprouvent égal à sa copie versée ; rapports épinglés, seuls de leur famille,
# cités ; branche de résultats absente ; GO et dépense relus dans les registres de HEAD (fonctions du module de P4) ;
# module de P4 cité (six fichiers) ; préenregistrement et configuration scellés (problemes() vide) ; verifier-arbre ;
# un seul commit S qui n'ajoute que ces quatre fichiers, poussé, puis relu sur le dépôt distant. Un échec avant le
# commit retire les fichiers créés ici (et seulement eux). Tout arrêt sort en code 2.
# Chaîne v2 : vingt et un scripts dans la liste CHAINE (arrêt, contrôle des traces, leurs bancs) ; huit journaux de
# preuve (bancs de l'arrêt et du contrôle des traces) ; rapports épinglés aux noms exacts du module commun
# (RC-fidelite-12) ; liste des chemins gelés lue dans `7a54d43` (`git show`), jamais dans l'arbre contrôlé
# (RC-donnees-08).
# La copie jouée par la répétition finale change les lignes H, DEPOT, DISTANT et PREUVES_EXIGEES (elle ne peut exiger ni
# son propre journal, qui n'existe pas encore, ni celui du banc du scellement, dont le script éprouvé est celui que la
# répétition remplace par sa copie) ; ces quatre lignes changées sont comptées et déclarées par la répétition finale.
# Usage : sceller_p4_v1.sh
set -euo pipefail
trap 'echo "arrêt du scellement (ligne $LINENO)"; exit 2' ERR
[ $# -eq 0 ] || { echo "usage : sceller_p4_v1.sh (sans argument)"; exit 2; }
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2
DEPOT=/home/user/controle-ia-travail
DISTANT=https://github.com/lciric/controle-ia-travail          # seule adresse de lecture et de poussée admise (jamais la copie publique)
PREUVES_EXIGEES="banc-lanceur-p4-v1.log banc-surveillance-p4-v1.log banc-arret-p4-v1.log banc-traces-p4-v1.log banc-verifications-p4-v1.log banc-controles-p4-v1.log banc-scellement-p4-v1.log repetition-finale-p4-v1.log"
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERSEES=docs/procedures/P4-instrument-v1
P=prereg/P4-instrument-v1.md; CFG=prereg/P4-instrument-config-v1.json
CTL=$H/controles_avant_depense_p4_v1.sh
VERIF=$H/verifications_p4_v1.py
export PYTHONDONTWRITEBYTECODE=1
plat() { tr '\n' ' ' < "$1" | tr -s ' '; }      # texte aux espaces réduites : citations passées à la ligne
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$CTL" | sed 's/[[:space:]]*$//'; }
grep -q "^[A-Z_]*=\"\{0,1\}A_EPINGLER" "$CTL" && { echo "épingle restée « A_EPINGLER » dans les contrôles"; exit 2; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); RELU_SHA=$(epingle CANDIDAT_RELU)
CFG_RELUE=$(epingle CONFIG_RELUE_CHEMIN); CFG_RELUE_SHA=$(epingle CONFIG_RELUE)
RAPPORTS=$(epingle RAPPORTS_ATTENDUS); CODE_RELU=$(epingle CODE_RELU)
REP_COMMIT=$(epingle REPETITION_COMMIT); REPETITION=$(epingle REPETITION_JOUET); REPETITION_CHEMIN=$(epingle REPETITION_JOUET_CHEMIN)
[[ "$RELU_SHA" =~ ^[0-9a-f]{64}$ && "$RELU" == brouillons/* && "$CFG_RELUE_SHA" =~ ^[0-9a-f]{64}$ && "$CFG_RELUE" == brouillons/* ]] \
    || { echo "candidat ou configuration relus non épinglés"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REP_COMMIT" =~ ^[0-9a-f]{40}$ && "$REPETITION" =~ ^[0-9a-f]{64}$ && "$REPETITION_CHEMIN" == "$VERSEES"/* ]] \
    || { echo "code relu, commit répété ou répétition jouet non épinglés"; exit 2; }
# rapports épinglés : les noms exacts du module commun (RAPPORTS_NOMS), une fois chacun (RC-fidelite-12)
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
# shellcheck disable=SC2086
R_SORTIE=$("$PY" -B "$VERIF" rapports $RAPPORTS 2>&1) || { echo "rapports épinglés : $(printf '%s\n' "$R_SORTIE" | tail -1 | cut -c1-220)"; exit 2; }
[ -n "$PREUVES_EXIGEES" ] || { echo "aucun journal de preuve exigé"; exit 2; }
cd "$DEPOT"
# toutes les adresses de origin, en lecture et en poussée : le dépôt de travail seulement (CLAUDE.md : jamais lciric/controle-ia)
for sens in "" "--push"; do
    u=$(git remote get-url --all $sens origin 2>/dev/null || true)
    [ "$u" = "$DISTANT" ] || [ "$u" = "$DISTANT.git" ] || { echo "adresse de origin ${sens:-en lecture} « $(printf '%s' "$u" | tr '\n' ' ') » ≠ $DISTANT (une seule adresse admise)"; exit 2; }
done
git fetch -q origin main
[ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "HEAD ≠ origin/main : pousser d'abord les préalables"; exit 2; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "arbre suivi non propre"; exit 2; }
for f in "$P" "$P.sha256" "$CFG" "$CFG.sha256"; do [ -e "$f" ] && { echo "$f existe déjà (R12)"; exit 2; }; done
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh
        repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh
        essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
MODULE_P4="mesures_conception_p4_v1.py instrument_p4_v1.py lecture_p4_v1.py test_instrument_p4_v1.py test_lecture_p4_v1.py test_gardes_p4_v1.py"
SUIVIS=$(for s in $CHAINE $MODULE_P4; do printf '%s/%s %s/%s.sha256\n' "$VERSEES" "$s" "$VERSEES" "$s"; done
         for j in $PREUVES_EXIGEES; do printf '%s/%s %s/%s.sha256\n' "$VERSEES" "$j" "$VERSEES" "$j"; done
         for x in $RAPPORTS; do printf 'prereg/contre-lectures/%s prereg/contre-lectures/%s.sha256\n' "${x%%=*}" "${x%%=*}"; done)
for f in $SUIVIS "$RELU" "$RELU.sha256" "$CFG_RELUE" "$CFG_RELUE.sha256" "$REPETITION_CHEMIN" "$REPETITION_CHEMIN.sha256"; do
    git ls-files --error-unmatch -- "$f" > /dev/null 2>&1 || { echo "$f non suivi à HEAD"; exit 2; }
done
for s in $CHAINE; do
    cmp -s "$H/$s" "$VERSEES/$s" || { echo "$s du bloc-notes ≠ copie versée"; exit 2; }
done
# shellcheck disable=SC2046
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier $(for s in $CHAINE $MODULE_P4; do printf '%s/%s ' "$VERSEES" "$s"; done) > /dev/null \
    || { echo "sceau d'une copie versée non conforme"; exit 2; }
for paire in "$RELU=$RELU_SHA" "$CFG_RELUE=$CFG_RELUE_SHA"; do
    f=${paire%%=*}; e=${paire#*=}
    [ "$(sha256sum "$f" | cut -d' ' -f1)" = "$e" ] && [ "$(cat "$f.sha256")" = "$e  $(basename "$f")" ] \
        || { echo "$f ≠ épingle, ou sceau différent de la ligne exacte"; exit 2; }
done
# le candidat cite l'empreinte canonique de la configuration relue (sinon le run s'arrêterait, R11)
PYTHONPATH=src "$PY" -B -c 'import hashlib, json, re, sys
from controle_ia.manifeste import config_canonique
c = json.load(open(sys.argv[1], encoding="utf-8"))
m = re.findall(r"Configuration de P4 \(empreinte canonique\) : `([0-9a-f]{64})`", open(sys.argv[2], encoding="utf-8").read())
sys.exit(0 if m == [hashlib.sha256(config_canonique(c)).hexdigest()] else 1)' "$CFG_RELUE" "$RELU" \
    || { echo "le candidat relu ne cite pas l'empreinte canonique de la configuration relue"; exit 2; }
[ "$(grep -c "Commit du code d'analyse : \`" "$RELU")" = 1 ] || { echo "commit du code cité zéro ou plusieurs fois par le candidat"; exit 2; }
CODE_CITE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$RELU")
[[ "$CODE_CITE" =~ ^[0-9a-f]{40}$ ]] || { echo "commit du code cité illisible"; exit 2; }
# chacun des intitulés lus par la chaîne et le module figure exactement une fois dans le texte
INTITULES=("Configuration de P4 (empreinte canonique)" "Commit du code d'analyse" "Entropie" "Révision du modèle"
           "Tests attendus" "**GO cité par la commande de création**" "Lancement")
for x in "${INTITULES[@]}"; do
    [ "$(grep -oF "$x : \`" "$RELU" | wc -l)" = 1 ] || { echo "intitulé « $x » cité zéro ou plusieurs fois par le candidat"; exit 2; }
done
# rapports : seuls de leur famille (aucun autre fichier suivi sous prereg/contre-lectures/ dont le nom porte « P4 »)
presents=$(git ls-files prereg/contre-lectures/ | grep -E '/[^/]*P4[^/]*$' | grep -v '\.sha256$' | xargs -r -n1 basename | sort | tr '\n' ' ' || true)
attendus=$(for x in $RAPPORTS; do echo "${x%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] || { echo "rapports présents « $presents » ≠ épinglés « $attendus »"; exit 2; }
# branche de résultats absente du dépôt distant (la ligne « Lancement » scellée la fige)
c=0; git ls-remote --exit-code origin refs/heads/calcul/p4-reel-v1 > /dev/null 2>&1 || c=$?
[ "$c" = 2 ] || { echo "branche calcul/p4-reel-v1 : code $c (2 attendu : absente)"; exit 2; }
for x in $RAPPORTS; do
    f="prereg/contre-lectures/${x%%=*}"
    [ "$(sha256sum "$f" | cut -d' ' -f1)" = "${x#*=}" ] && plat "$RELU" | grep -qF "\`$f\` (\`${x#*=}\`)" \
        || { echo "rapport ${x%%=*} : empreinte différente de l'épingle, ou non cité par le candidat"; exit 2; }
done
# liste des chemins gelés lue dans le commit de P3 (instrument figé), jamais dans l'arbre contrôlé (RC-donnees-08)
GELES=$(git show "$CODE_RELU:src/controle_ia/harnais/validation_reelle.py" | "$PY" -I -B -c 'import ast, sys
t = ast.parse(sys.stdin.read())
v = [n.value for n in t.body if isinstance(n, ast.Assign) and any(getattr(x, "id", "") == "CHEMINS_GELES" for x in n.targets)]
assert len(v) == 1
print(" ".join(ast.literal_eval(v[0])))') || { echo "CHEMINS_GELES illisible dans $CODE_RELU"; exit 2; }
[ -n "$GELES" ] || { echo "CHEMINS_GELES illisible dans $CODE_RELU"; exit 2; }
# shellcheck disable=SC2086
git diff --quiet "$CODE_RELU" HEAD -- $GELES || { echo "arbre gelé de HEAD ≠ celui de P3 ($CODE_RELU)"; exit 2; }
# shellcheck disable=SC2086
git diff --quiet "$CODE_CITE" HEAD -- $GELES 2>/dev/null || { echo "arbre gelé du commit cité par le candidat ($CODE_CITE) ≠ celui de HEAD"; exit 2; }
[ "$(sha256sum "$REPETITION_CHEMIN" | cut -d' ' -f1)" = "$REPETITION" ] && [ "$(cat "$REPETITION_CHEMIN.sha256")" = "$REPETITION  $(basename "$REPETITION_CHEMIN")" ] \
    || { echo "journal de la répétition jouet absent, d'une autre empreinte que l'épingle, ou sceau différent"; exit 2; }
git merge-base --is-ancestor "$REP_COMMIT" HEAD 2>/dev/null || { echo "commit répété $REP_COMMIT non ancêtre de HEAD"; exit 2; }
# shellcheck disable=SC2046
git diff --quiet "$REP_COMMIT" HEAD -- $(for s in $MODULE_P4 amorce_instance_p4_v1.sh p4_instance_v1.sh; do printf '%s/%s ' "$VERSEES" "$s"; done) \
    || { echo "module ou scripts de l'instance du commit répété ≠ ceux de HEAD"; exit 2; }
SORTIE_REP=$("$PY" -B "$VERIF" repetition "$REP_COMMIT" "$REPETITION_CHEMIN" "$(basename "$RELU")" "$RELU_SHA" 2>&1) \
    || { echo "journal de la répétition jouet non conforme : $(printf '%s\n' "$SORTIE_REP" | tail -1)"; exit 2; }
while read -r s e; do
    [ "$(sha256sum "$VERSEES/$s" | cut -d' ' -f1)" = "$e" ] || { echo "script répété ≠ copie versée : $s"; exit 2; }
done <<< "$SORTIE_REP"
# preuves des essais : journaux exigés, suivis, à leur sceau exact ; conformes au module commun ; chaque script éprouvé
# égal à sa copie versée (le lanceur refuserait sinon un S figé, R12)
for j in $PREUVES_EXIGEES; do
    [ "$(cat "$VERSEES/$j.sha256")" = "$(sha256sum "$VERSEES/$j" | cut -d' ' -f1)  $j" ] \
        || { echo "preuves des essais : sceau de $j absent ou non conforme"; exit 2; }
done
# shellcheck disable=SC2086
SORTIE_PREUVES=$("$PY" -B "$VERIF" preuves "$VERSEES" $PREUVES_EXIGEES 2>&1) \
    || { echo "preuves des essais : $(printf '%s\n' "$SORTIE_PREUVES" | tail -1)"; exit 2; }
while read -r s e; do
    [ "$(sha256sum "$VERSEES/$s" | cut -d' ' -f1)" = "$e" ] || { echo "preuves des essais : $s éprouvé ≠ copie versée"; exit 2; }
done <<< "$SORTIE_PREUVES"
echo "preuves des essais : $(echo $PREUVES_EXIGEES | wc -w) journaux conformes ; $(printf '%s\n' "$SORTIE_PREUVES" | grep -c .) scripts éprouvés égaux à leurs copies versées"
# GO et dépense relus dans les registres de HEAD (fonctions du module de P4, chargé à l'empreinte que cite le candidat) ;
# module de P4 cité (les contrôles et le lanceur les relisent ensuite)
BORNE=$(sed -n 's/^BORNE_ETAPE_USD=\([0-9.]*\) .*/\1/p' "$VERSEES/lancer_p4_v1.sh")
SORTIE_GO=$(PYTHONPATH=src "$PY" -B "$VERIF" go . "$RELU" "$(date -u +%F)" "$BORNE" 2>&1) \
    || { echo "GO et dépense non conformes : $(printf '%s\n' "$SORTIE_GO" | tail -1)"; exit 2; }
echo "GO et dépense : $SORTIE_GO"
SORTIE_MODULE=$(PYTHONPATH=src "$PY" -B "$VERIF" module . "$RELU" 2>&1) \
    || { echo "module de P4 : $(printf '%s\n' "$SORTIE_MODULE" | tail -1)"; exit 2; }
echo "module de P4 : $(printf '%s\n' "$SORTIE_MODULE" | grep -c .) fichiers à l'empreinte citée"
COMMITTE=0
QUATRE=("$P" "$P.sha256" "$CFG" "$CFG.sha256")
fin() {
    local code=$?
    if [ "$code" != 0 ] && [ "$COMMITTE" = 0 ]; then
        # un commit refusé après git add laisse les fichiers dans l'index : les en retirer d'abord
        git reset -q -- "${QUATRE[@]}" > /dev/null 2>&1 || true
        for f in "${QUATRE[@]}"; do git ls-files --error-unmatch "$f" >/dev/null 2>&1 || rm -f "$f"; done
        echo "échec avant le commit : fichiers créés retirés"
    fi
    [ "$code" = 0 ] || exit 2
}
trap fin EXIT
cp "$CFG_RELUE" "$CFG"; cp "$RELU" "$P"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$CFG" > /dev/null
PYTHONPATH=src "$PY" -B -c "from controle_ia.prereg import sceller_prereg; sceller_prereg('$P')"
[ "$(cut -d' ' -f1 "$P.sha256")" = "$RELU_SHA" ] && [ "$(cut -d' ' -f1 "$CFG.sha256")" = "$CFG_RELUE_SHA" ] \
    || { echo "sceaux du préenregistrement ou de la configuration ≠ épingles"; exit 2; }
VA=$(mktemp)
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier-arbre . > "$VA" 2>&1 \
    || { grep '^ÉCHEC' "$VA" || tail -3 "$VA"; rm -f "$VA"; echo "verifier-arbre en échec"; exit 2; }
# dernière ligne de verifier-arbre : garde redondante (le code de sortie suffirait), sans artefact propre
tail -1 "$VA" | grep -qx "arbre intact" || { rm -f "$VA"; echo "verifier-arbre : dernière ligne inattendue"; exit 2; }
rm -f "$VA"
git add "${QUATRE[@]}"
git commit -q -F - <<EOF
P4-instrument : préenregistrement v1 scellé (R-262 (1), R-269)

Préenregistrement $RELU_SHA (copie du candidat relu $RELU) ; configuration $CFG_RELUE_SHA
(copie de $CFG_RELUE). Arbre gelé de P3 $CODE_RELU ; commit répété $REP_COMMIT.
Lancement : PREREG=$P, BRANCHE=calcul/p4-reel-v1, GO_ID=GO-2026-10-20-07.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015nCKHP3BPpJMpwY6zAEA4r
EOF
COMMITTE=1
S=$(git rev-parse HEAD)
# contenu de S et origin/main après la poussée : gardes redondantes (git add des seuls quatre fichiers ; poussée relue),
# sans artefact possible hors d'un crochet
[ "$(git diff --name-only --no-renames "$S^" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "${QUATRE[@]}" | sort | tr '\n' ' ')" ] \
    || { echo "contenu de S inattendu"; exit 2; }
timeout 600 git push -q origin HEAD:main || { echo "poussée de S en échec : S reste local ; repousser avant tout lancement"; exit 2; }
git fetch -q origin main
[ "$(git rev-parse origin/main)" = "$S" ] || { echo "origin/main ≠ S après la poussée"; exit 2; }
echo "S $S poussé ; préenregistrement $RELU_SHA"
