#!/usr/bin/env bash
# Banc du scellement de P4-instrument (R5), v1, décliné de docs/procedures/P3-premier-test-v2/essais_scellement_p3_v1.sh
# sous un nom neuf (R12). Clone partagé de DEPOT_SOURCE au commit C (module de P4 versé ; registres réels :
# GO-2026-10-20-07, R-262 et R-269 y sont consignés), sans extraction des PDF ; dépôt nu local en guise de dépôt
# distant. Préalables d'essai fabriqués par le banc, comme dans le banc des contrôles (commit A : vingt et un scripts de
# la chaîne versés, candidat d'essai tiré du brouillon 4, configuration réelle de référence, vingt-sept rapports synthétiques (chaîne v4)
# de la famille « P4 » ; commit J : journal synthétique de la répétition jouet, commit répété A, et les huit journaux de
# preuve factices aux empreintes des copies versées). Bloc-notes factice H : copies versées, dont la copie des
# contrôles porte les épingles du banc (sept lignes, versée telle quelle) et celle du scellement change ses lignes H,
# DEPOT et DISTANT (re-versée et rescellée, comme dans la répétition finale). Après chaque passage : code, dernières
# lignes, tête et dépôt distant, restes non suivis. Cas propres à P4 : commit S de quatre fichiers ; candidat qui ne
# cite pas l'empreinte canonique de la configuration relue ; GO-2026-10-20-07 (type, plafond, révocation sous ses deux
# formes, cas sain) par le module commun ; intitulés de P4 ; commit répété non ancêtre, ou au module autre que celui de
# HEAD ; module de P4 changé ; épingles mal formées ; preuves des essais (huit journaux) absentes, sans leur sceau, au
# verdict non conforme ou devenues caduques. Sort en code 1 s'il reste un cas non conforme.
# Chaîne v2 : vingt et un scripts dans CHAINE ; huit journaux de preuve ; rapports synthétiques aux noms exacts du
# module commun (RC-fidelite-12 : paire d'un autre nom, une seule paire : refus) ; liste des chemins gelés lue dans
# 7a54d43 (liste de HEAD qui s'exclut elle-même et exclut un dossier changé : refus, RC-donnees-08) ; journal synthétique
# de la répétition par outils_essais_p4_v1.py journal-repetition.
# Usage : essais_scellement_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
[ $# -eq 3 ] || { echo "usage : essais_scellement_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; E=$(realpath -m "$3")
SOI=$(realpath "$0")
HN=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4
B4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
V=docs/procedures/P4-instrument-v1
P=prereg/P4-instrument-v1.md; CFG=prereg/P4-instrument-config-v1.json
GO=GO-2026-10-20-07
export PYTHONDONTWRITEBYTECODE=1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/H" && cd "$E" || exit 2
git clone -q --shared --no-checkout "$SRC" depot && cd depot || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git sparse-checkout set --no-cone '/*' '!/docs/sources/pdf/' '!/docs/sources/lecture-pdf-niveau1/' '!/docs/sources/lecture-pdf-niveau2/' \
    && git checkout -q "$C" && git checkout -q -B main || exit 2
echo "C = $(git rev-parse HEAD)"
for s in sceller_p4_v1.sh verifications_p4_v1.py outils_essais_p4_v1.py; do echo "script éprouvé : $s $(sha256sum "$HN/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
CHAINE=$(sed -n '/^CHAINE="/,/"$/p' "$HN/sceller_p4_v1.sh" | tr -d '"' | sed 's/^CHAINE=//')
[ "$(echo $CHAINE | wc -w)" = 21 ] || { echo "liste CHAINE inattendue"; exit 2; }
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
# commit A : chaîne versée (copies du bloc-notes), candidat et configuration relus, rapports
mkdir -p "$V" brouillons prereg/contre-lectures
for s in $CHAINE; do cp "$HN/$s" "$V/$s" && resceller "$V/$s" || { echo "copie versée impossible : $s"; exit 2; }; done
# rapports synthétiques, aux noms exacts du module commun (RC-fidelite-12)
NOMS_R=$("$PY" -I -B -c 'import importlib.util, sys
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
print(" ".join(v.RAPPORTS_NOMS))' "$HN/verifications_p4_v1.py") || exit 2
RAPPORTS=""
for nom in $NOMS_R; do
    printf '# Rapport synthétique %s (banc du scellement de P4)\n\nVerdict : scellable (essai).\n' "$nom" > "prereg/contre-lectures/$nom"
    resceller "prereg/contre-lectures/$nom"
    RAPPORTS="$RAPPORTS $nom=$(sha256sum "prereg/contre-lectures/$nom" | cut -d' ' -f1)"
done
RAPPORTS=${RAPPORTS# }
RA=$(echo $NOMS_R | cut -d' ' -f1)
RELU=brouillons/P4-instrument-v1-candidat-essai.md; CFG_RELUE=brouillons/P4-instrument-config-v1-candidat-essai.json
CFG_SHA=$("$PY" -B "$HN/outils_essais_p4_v1.py" config-reelle . "$V" "$CFG_RELUE" | python3 -c 'import json, sys; print(json.load(sys.stdin)["config"])') || { echo "configuration relue impossible"; exit 2; }
"$PY" -B "$HN/outils_essais_p4_v1.py" candidat "$B4" "$RELU" . 7a54d431d89745839220f882b41b13e8c62ecfdd "$CFG_SHA" 1102 \
    $(for x in $RAPPORTS; do printf -- '--rapport %s ' "$x"; done) > /dev/null || { echo "candidat d'essai impossible"; exit 2; }
git add -A "$V" brouillons prereg/contre-lectures && git commit -qm "essai : préalables (chaîne, candidat et configuration relus, rapports)" || exit 2
A=$(git rev-parse HEAD)
# commit J : journal synthétique de la répétition jouet (commit répété A) ; contrôles épinglés et scellement copié,
# versés tels qu'au bloc-notes factice ; huit journaux de preuve factices
LJ=$V/repetition-jouet-p4-v1.log
journal_repetition() {   # $1 commit répété, $2 nom du candidat, $3 son empreinte
    "$PY" -B "$HN/outils_essais_p4_v1.py" journal-repetition "$HN/verifications_p4_v1.py" "$1" "$2" "$3" "$V" > "$LJ" || return 1
    resceller "$LJ"
}
journal_repetition "$A" "$(basename "$RELU")" "$(sha256sum "$RELU" | cut -d' ' -f1)" || exit 2
for s in $CHAINE; do cp "$V/$s" "$E/H/$s"; done
CTL=$E/H/controles_avant_depense_p4_v1.sh
python3 - "$CTL" "$(sha256sum "$RELU" | cut -d' ' -f1)" "$RELU" "$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)" "$CFG_RELUE" "$RAPPORTS" "$A" "$(sha256sum "$LJ" | cut -d' ' -f1)" <<'PYE' || exit 2
import re, sys
from pathlib import Path
ctl, relu_sha, relu, cfg_sha, cfg, rapports, rep_commit, rep_sha = sys.argv[1:9]
t = Path(ctl).read_text(encoding="utf-8")
for nom, val in (("CANDIDAT_RELU", relu_sha), ("CANDIDAT_RELU_CHEMIN", relu), ("CONFIG_RELUE", cfg_sha), ("CONFIG_RELUE_CHEMIN", cfg),
                 ("RAPPORTS_ATTENDUS", f'"{rapports}"'), ("REPETITION_COMMIT", rep_commit), ("REPETITION_JOUET", rep_sha)):
    assert len(re.findall(rf"^{nom}=\S+", t, re.M)) == 1, nom
    t = re.sub(rf"^{nom}=\S+", lambda _: f"{nom}={val}", t, flags=re.M)
Path(ctl).write_text(t, encoding="utf-8")
PYE
echo "lignes changées dans la copie des contrôles (épingles du banc) : $(diff "$HN/controles_avant_depense_p4_v1.sh" "$CTL" | grep -c '^>')"
sed -e "s|^H=.*|H=$E/H|" -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^DISTANT=.*|DISTANT=$E/distant.git|" "$HN/sceller_p4_v1.sh" > "$E/H/sceller_p4_v1.sh"
echo "lignes changées dans la copie du scellement : $(diff "$HN/sceller_p4_v1.sh" "$E/H/sceller_p4_v1.sh" | grep -c '^>') (H, DEPOT, DISTANT)"
grep -n "controle-ia-travail\|github" "$E/H/sceller_p4_v1.sh" && { echo "COPIE NON SÛRE"; exit 2; }
cp "$CTL" "$E/H/sceller_p4_v1.sh" "$V/" && resceller "$V/controles_avant_depense_p4_v1.sh" "$V/sceller_p4_v1.sh"
ep() { for s in "$@"; do echo "script éprouvé : $s $(sha256sum "$V/$s" | cut -d' ' -f1)"; done; }
journal_preuve() {   # $1 nom du journal, $2 dernière ligne, puis les scripts éprouvés
    local n=$1 v=$2; shift 2
    { echo "journal factice du banc du scellement"; ep "$@"; echo "$v"; } > "$V/$n"
    resceller "$V/$n"
}
journaux_preuves() {
    journal_preuve banc-lanceur-p4-v1.log "FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0" lancer_p4_v1.sh verifications_p4_v1.py essais_lanceur_p4_v1.sh
    journal_preuve banc-surveillance-p4-v1.log "FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0" surveiller_p4_v1.sh controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh essais_surveillance_p4_v1.sh
    journal_preuve banc-verifications-p4-v1.log "FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0" verifications_p4_v1.py essais_verifications_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve banc-controles-p4-v1.log "FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0" controles_avant_depense_p4_v1.sh verifications_p4_v1.py essais_controles_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve banc-scellement-p4-v1.log "FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0" sceller_p4_v1.sh verifications_p4_v1.py essais_scellement_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve repetition-finale-p4-v1.log "RÉPÉTITION FINALE : CONFORME" sceller_p4_v1.sh controles_avant_depense_p4_v1.sh verifications_p4_v1.py repetition_finale_p4_v1.sh
    journal_preuve banc-arret-p4-v1.log "FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : 0" arreter_p4_v1.sh essais_arret_p4_v1.sh
    journal_preuve banc-traces-p4-v1.log "FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : 0" controler_traces_p4_v1.sh verifications_p4_v1.py essais_traces_p4_v1.sh outils_essais_p4_v1.py
}
journaux_preuves
git add -A "$V" && git commit -qm "essai : journal de la répétition, contrôles épinglés, scellement copié, journaux de preuve factices" || exit 2
J=$(git rev-parse HEAD); echo "A = $A ; J = $J"
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
[ "$(git remote get-url --push origin)" = "$E/distant.git" ] || { echo "origine de poussée inattendue"; exit 2; }
QUATRE=("$P" "$P.sha256" "$CFG" "$CFG.sha256")
NON_CONFORMES=0
JOUR=$(date -u +%F)
passage() {   # $1 nom, $2 code attendu, $3 motif attendu dans la sortie, puis les arguments du scellement
    local n=$1 attendu=$2 motif=$3; shift 3
    local avant c v reste
    avant=$(git rev-parse HEAD)
    bash "$E/H/sceller_p4_v1.sh" "$@" > "$E/scellement-$n.log" 2>&1; c=$?
    reste=$(ls "${QUATRE[@]}" 2>/dev/null | tr '\n' ' ')
    v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    if [ -n "$motif" ] && ! grep -qF -- "$motif" "$E/scellement-$n.log"; then v="NON CONFORME (motif « $motif » absent)"; fi
    if [ "$attendu" != 0 ]; then
        [ "$(git rev-parse HEAD)" = "$avant" ] || [ "$n" = S03-poussee-refusee ] || v="NON CONFORME (commit fait malgré l'arrêt)"
        [ -z "$reste" ] || [ "$n" = S07-prereg-present ] || [ "$n" = S07c-configuration-presente ] \
            || [ "$n" = S03-poussee-refusee ] || v="NON CONFORME (restes : $reste)"
    fi
    # une trace d'exception n'est attendue que du refus de sceller_prereg (S25 : garde du dépôt, R1/R2)
    grep -q "^Traceback" "$E/scellement-$n.log" && [ "$n" != S25-candidat-non-conforme-r1-r2 ] && v="NON CONFORME (trace d'exception)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; $v"
    grep -v '^$' "$E/scellement-$n.log" | tail -2 | couper 200 | sed 's/^/    | /'
}
remise() {   # clone et dépôt nu remis sur un commit (J par défaut) ; fichiers du scellement retirés ; adresses rétablies
    git checkout -q -f main; git reset -q --hard "${1:-$J}"; rm -f "${QUATRE[@]}"
    git config --unset-all remote.origin.pushurl 2>/dev/null; git remote set-url origin "$E/distant.git"; git remote set-url --push origin "$E/distant.git"
    git push -q -f "$E/distant.git" "${1:-$J}:refs/heads/main" || { echo "REMISE IMPOSSIBLE (dépôt nu)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
    git fetch -q origin
    [ "$(git rev-parse origin/main)" = "$(git rev-parse "${1:-$J}")" ] || { echo "REMISE IMPOSSIBLE (origin/main)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
}
cp "$CTL" "$E/ctl-sauve.sh"
epingle_versee() {   # $1 expression sed sur les contrôles, $2 message ; une ligne exactement changée ; bloc-notes et copie
    # versée ; journaux de preuve factices refaits aux empreintes de la copie ré-épinglée
    cp "$CTL" "$E/ctl-avant-epingle.sh"
    sed -i "$1" "$CTL" || return 1
    [ "$(diff "$E/ctl-avant-epingle.sh" "$CTL" | grep -c '^>')" = 1 ] || { echo "épingle : une ligne exactement attendue"; return 1; }
    cp "$CTL" "$V/" && resceller "$V/controles_avant_depense_p4_v1.sh" && journaux_preuves && git add -A "$V" \
        && git commit -qam "essai : $2" && remise "$(git rev-parse HEAD)"
}
candidat_change() {   # $1 expression sed sur le candidat (rescellé, ré-épinglé), $2 message ; le journal de la répétition
    # nomme alors le candidat changé (rescellé, ré-épinglé)
    local nouveau
    sed -i "$1" "$RELU" && resceller "$RELU" && git add -A "$RELU" "$RELU.sha256" || return 1
    nouveau=$(sha256sum "$RELU" | cut -d' ' -f1)
    epingle_versee "s|^CANDIDAT_RELU=[0-9a-f]\{64\}|CANDIDAT_RELU=$nouveau|" "$2" || return 1
    journal_repetition "$A" "$(basename "$RELU")" "$nouveau" || return 1
    epingle_versee "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=$(sha256sum "$LJ" | cut -d' ' -f1)|" "$2 (journal de la répétition)"
}
retour() { cp "$E/ctl-sauve.sh" "$CTL"; remise; }
passage S00-sain 0 "poussé ; préenregistrement"
S=$(git rev-parse HEAD)
if [ "$S" != "$J" ] && [ "$(git rev-parse "$S^")" = "$J" ] && [ "$(git -C "$E/distant.git" rev-parse main)" = "$S" ] \
   && [ "$(git diff --name-only --no-renames "$J" "$S" | sort | tr '\n' ' ')" = "$(printf '%s\n' "${QUATRE[@]}" | sort | tr '\n' ' ')" ] \
   && cmp -s "$P" "$RELU" && cmp -s "$CFG" "$CFG_RELUE" \
   && [ -z "$(git status --porcelain --untracked-files=no)" ] && grep -qF "preuves des essais : 8 journaux conformes ; 17 scripts éprouvés" "$E/scellement-S00-sain.log" \
   && grep -qF "GO et dépense : $GO conforme" "$E/scellement-S00-sain.log" && grep -qF "module de P4 : 6 fichiers à l'empreinte citée" "$E/scellement-S00-sain.log" \
   && git log -1 --format=%B "$S" | grep -qF "GO_ID=$GO"; then
    echo "    S $S : enfant de J, poussé, quatre fichiers seulement (texte, configuration, sceaux), copies exactes du candidat et de la configuration relus, preuves, GO et module relus, arbre propre : CONFORME"
else echo "    S $S : NON CONFORME (parent, poussée, contenu, copie, preuves, GO ou module)"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
remise
echo "# essai" >> README.md
passage S01-arbre-sale 2 "arbre suivi non propre"
git checkout -q -- README.md
printf '%s  index.json\n' "$(printf '0%.0s' {1..64})" > docs/sources/invites-2606.08892-v1/index.json.sha256
git commit -qam "essai : sceau faussé hors de la chaîne" && remise "$(git rev-parse HEAD)"
passage S02-sceau-fausse-verifier-arbre 2 "ÉCHEC"
remise
printf '%s  %s\n' "$(printf '5%.0s' {1..64})" "surveiller_p4_v1.sh" > "$V/surveiller_p4_v1.sh.sha256" && git commit -qam "essai : sceau d'une copie versée faussé" && remise "$(git rev-parse HEAD)"
passage S02b-sceau-d-une-copie-versee-fausse 2 "sceau d'une copie versée non conforme"
remise
printf '#!/bin/sh\necho "refus (essai)" >&2\nexit 1\n' > "$E/distant.git/hooks/pre-receive" && chmod +x "$E/distant.git/hooks/pre-receive"
passage S03-poussee-refusee 2 "poussée de S en échec"
rm -f "$E/distant.git/hooks/pre-receive"
remise
epingle_versee "s|^CANDIDAT_RELU=[0-9a-f]\{64\}|CANDIDAT_RELU=$(printf '1%.0s' {1..64})|" "épingle du candidat fausse" || { echo "S04 : montage impossible"; exit 2; }
passage S04-epingle-candidat-fausse 2 "$RELU ≠ épingle"
retour
epingle_versee "s|^CONFIG_RELUE=[0-9a-f]\{64\}|CONFIG_RELUE=$(printf '2%.0s' {1..64})|" "épingle de la configuration fausse" || { echo "S04b : montage impossible"; exit 2; }
passage S04b-epingle-configuration-fausse 2 "$CFG_RELUE ≠ épingle"
retour
echo "# modifié" >> "$E/H/recuperation_p4_v1.sh"
passage S05-recuperation-non-versee 2 "recuperation_p4_v1.sh du bloc-notes ≠ copie versée"
cp "$V/recuperation_p4_v1.sh" "$E/H/recuperation_p4_v1.sh"
echo "# modifié" >> "$E/H/p4_instance_v1.sh"
passage S05b-script-de-l-instance-non-verse 2 "p4_instance_v1.sh du bloc-notes ≠ copie versée"
cp "$V/p4_instance_v1.sh" "$E/H/p4_instance_v1.sh"
git commit -q --allow-empty -m "essai : commit local non poussé"
passage S06-head-en-avance 2 "HEAD ≠ origin/main"
remise
echo x > "$P"
passage S07-prereg-present 2 "existe déjà (R12)"
rm -f "$P"
echo x > "$CFG"
passage S07c-configuration-presente 2 "$CFG existe déjà (R12)"
rm -f "$CFG"
git rm -q "prereg/contre-lectures/$RA" "prereg/contre-lectures/$RA.sha256" \
    && git commit -qm "essai : rapport retiré" && remise "$(git rev-parse HEAD)"
passage S08-rapport-epingle-absent 2 "$RA non suivi à HEAD"
remise
# GO et dépense (module commun : fonctions du module de P4, registres de HEAD)
sed -i "/^| $GO |/s/| calcul |/| revendication |/" registres/go.md
git commit -qam "essai : GO d'un autre type" && remise "$(git rev-parse HEAD)"
passage S09-go-autre-type 2 "GO et dépense non conformes : $GO : ligne de huit colonnes, de type « calcul »"
remise
sed -i "/^| $GO |/s/| 10 USD par lancement, /| 12 USD par lancement, /" registres/go.md
git commit -qam "essai : plafond sans le préfixe" && remise "$(git rev-parse HEAD)"
passage S09b-plafond-sans-le-prefixe 2 "ne commence pas par « 10 USD par lancement »"
remise
echo "| GO-2026-10-20-98 | $JOUR | révocation | révoque GO-2026-10-20-06 (essai) | — | $JOUR | Lazar | essai |" >> registres/go.md
git commit -qam "essai : prolongation de la phase révoquée" && remise "$(git rev-parse HEAD)"
passage S09c-revocation-au-registre-des-go 2 "révocation au registre des GO (GO-2026-10-20-98)"
remise
echo "| R-998 | $JOUR | **Révocation de R-269** (essai). | essai |" >> registres/decisions.md
git commit -qam "essai : délégation révoquée sous sa forme exacte" && remise "$(git rev-parse HEAD)"
passage S09e-forme-exacte-au-registre-des-decisions 2 "révocation au registre des décisions (R-998)"
remise
echo "| R-997 | $JOUR | Décision de Lazar (essai) : aucune révocation de R-269. | essai |" >> registres/decisions.md
git commit -qam "essai : ligne qui dit qu'aucune révocation n'est faite" && remise "$(git rev-parse HEAD)"
passage S09f-aucune-revocation 0 "poussé ; préenregistrement"
remise
sed -i "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=A_EPINGLER|" "$CTL"
passage S13-epingle-restee 2 "A_EPINGLER"
cp "$E/ctl-sauve.sh" "$CTL"
AUTRE=$(git rev-parse "7a54d431d89745839220f882b41b13e8c62ecfdd^")
epingle_versee "s|^CODE_RELU=[0-9a-f]\{40\}|CODE_RELU=$AUTRE|" "code relu autre" || { echo "S14 : montage impossible"; exit 2; }
passage S14-code-relu-autre 2 "arbre gelé de HEAD ≠ celui de P3"
retour
echo x >> "$LJ" && resceller "$LJ" && git commit -qam "essai : journal altéré" && remise "$(git rev-parse HEAD)"
passage S15-journal-repetition-altere 2 "journal de la répétition jouet absent, d'une autre empreinte que l'épingle"
remise
sed -i 's|^RAPPORTS_ATTENDUS="|RAPPORTS_ATTENDUS="autre-famille-v1.md='"$(printf '3%.0s' {1..64})"' |' "$CTL"
passage S16-rapport-autre-famille 2 "noms exacts de RAPPORTS_NOMS, une fois chacun"
cp "$E/ctl-sauve.sh" "$CTL"
git rm -q --cached "$LJ" "$LJ.sha256" && git commit -qm "essai : journal non suivi" && remise "$(git rev-parse HEAD)"
[ -f "$LJ" ] && [ -z "$(git ls-files -- "$LJ")" ] || { echo "S17 : montage impossible"; exit 2; }
passage S17-journal-non-suivi 2 "non suivi à HEAD"
remise
journal_repetition "$C" "$(basename "$RELU")" "$(sha256sum "$RELU" | cut -d' ' -f1)" \
    && epingle_versee "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=$(sha256sum "$LJ" | cut -d' ' -f1)|" "journal d'un autre commit répété, épinglé" \
    || { echo "S18 : montage impossible"; exit 2; }
passage S18-journal-autre-commit 2 "journal de la répétition jouet non conforme : ligne absente ou en double : commit du code répété"
retour
COTE=$(git commit-tree "$A^{tree}" -p "$C" -m "essai : commit de côté")
epingle_versee "s|^REPETITION_COMMIT=[0-9a-f]\{40\}|REPETITION_COMMIT=$COTE|" "commit répété non ancêtre" || { echo "S18b : montage impossible"; exit 2; }
passage S18b-commit-repete-non-ancetre 2 "commit répété $COTE non ancêtre de HEAD"
retour
echo "# essai" >> "$V/test_lecture_p4_v1.py" && resceller "$V/test_lecture_p4_v1.py" && git commit -qam "essai : module changé après la répétition" && remise "$(git rev-parse HEAD)"
passage S18c-module-autre-que-celui-du-commit-repete 2 "module ou scripts de l'instance du commit répété ≠ ceux de HEAD"
remise
sed -i "s|^REPETITION_JOUET_CHEMIN=.*|REPETITION_JOUET_CHEMIN=diag/repetition-jouet-p4-v1.log|" "$CTL"
passage S19-journal-hors-du-dossier 2 "code relu, commit répété ou répétition jouet non épinglés"
cp "$E/ctl-sauve.sh" "$CTL"
mv "$E/distant.git" "$E/distant.git.cache"
passage S20-arret-avant-le-piege 2 "arrêt du scellement (ligne"
mv "$E/distant.git.cache" "$E/distant.git"
remise
printf '#!/bin/sh\nexit 1\n' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
passage S21-commit-refuse 2 "échec avant le commit : fichiers créés retirés"
git diff --cached --quiet && echo "    index propre après S21 : CONFORME" || { echo "    S21 : NON CONFORME (fichiers laissés dans l'index)"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
rm -f .git/hooks/pre-commit
remise
passage S10-avec-argument 2 "usage" "$GO"
# le candidat relu, changé et ré-épinglé : chaque garde sur son contenu
RA_SHA=$(sha256sum "prereg/contre-lectures/$RA" | cut -d' ' -f1)
candidat_change "s/$RA_SHA/$(printf '4%.0s' {1..64})/g" "candidat qui cite un autre rapport" || { echo "S22 : montage impossible"; exit 2; }
passage S22-rapport-non-cite 2 "non cité par le candidat"
retour
candidat_change "s|Commit du code d'analyse : \`7a54d431d89745839220f882b41b13e8c62ecfdd\`|Commit du code d'analyse : \`$AUTRE\`|" "candidat qui cite un autre code" || { echo "S23 : montage impossible"; exit 2; }
passage S23-candidat-autre-code 2 "arbre gelé du commit cité par le candidat ($AUTRE) ≠ celui de HEAD"
retour
candidat_change 's/^- Commit du code d.analyse : .*$/&\n&/' "candidat qui cite deux fois le code" || { echo "S23b : montage impossible"; exit 2; }
passage S23b-commit-du-code-cite-deux-fois 2 "commit du code cité zéro ou plusieurs fois par le candidat"
retour
candidat_change '/\*\*GO cité par la commande de création\*\*/d' "candidat sans la ligne du GO" || { echo "S24 : montage impossible"; exit 2; }
passage S24-candidat-sans-go 2 "intitulé « **GO cité par la commande de création** » cité zéro ou plusieurs fois"
retour
candidat_change "s/\`GO_ID=$GO\`/\`GO_ID=GO-2026-10-04-08\`/" "candidat qui cite le GO de la phase" || { echo "S24b : montage impossible"; exit 2; }
passage S24b-candidat-go-de-la-phase 2 "GO-2026-10-04-08 : seul $GO est accepté"
retour
candidat_change "s|^## Contre-lecture$|## Contre-lecture retirée|" "candidat sans section Contre-lecture" || { echo "S25 : montage impossible"; exit 2; }
passage S25-candidat-non-conforme-r1-r2 2 "non conforme à R1/R2"
retour
candidat_change 's/^\(- Entropie : .*\)$/&\n\1/' "candidat qui cite deux fois l'entropie" || { echo "S35 : montage impossible"; exit 2; }
passage S35-intitule-en-double 2 "intitulé « Entropie » cité zéro ou plusieurs fois"
retour
candidat_change "s|\(Module de P4 : \`$V/lecture_p4_v1.py\` : \`\)[0-9a-f]\{64\}|\1$(printf 'c%.0s' {1..64})|" "candidat qui cite une autre empreinte du module" || { echo "S36 : montage impossible"; exit 2; }
passage S36-module-cite-a-une-autre-empreinte 2 "module de P4 : module de P4 : $V/lecture_p4_v1.py : empreinte"
retour
sed -i '/^FIN DE LA RÉPÉTITION$/d' "$LJ" && resceller "$LJ" \
    && epingle_versee "s|^REPETITION_JOUET=[0-9a-f]\{64\}|REPETITION_JOUET=$(sha256sum "$LJ" | cut -d' ' -f1)|" "journal inachevé, épinglé" \
    || { echo "S26 : montage impossible"; exit 2; }
passage S26-journal-inacheve 2 "ligne absente ou en double : FIN DE LA RÉPÉTITION"
retour
sed -i "s|^CANDIDAT_RELU_CHEMIN=brouillons/|CANDIDAT_RELU_CHEMIN=prereg/|" "$CTL"
passage S27-candidat-hors-des-brouillons 2 "candidat ou configuration relus non épinglés"
cp "$E/ctl-sauve.sh" "$CTL"
sed -i "s|^CONFIG_RELUE=[0-9a-f]\{64\}|CONFIG_RELUE=$(printf '6%.0s' {1..63})|" "$CTL"
passage S27b-epingle-de-63-caracteres 2 "candidat ou configuration relus non épinglés"
cp "$E/ctl-sauve.sh" "$CTL"
sed -i 's|^RAPPORTS_ATTENDUS="\([^ "]*\)[^"]*"|RAPPORTS_ATTENDUS="\1"|' "$CTL"
passage S28-une-seule-paire 2 "noms exacts de RAPPORTS_NOMS, une fois chacun"
cp "$E/ctl-sauve.sh" "$CTL"
printf '%s *%s\n' "$(sha256sum "$RELU" | cut -d' ' -f1)" "$(basename "$RELU")" > "$RELU.sha256" && git commit -qam "essai : sceau du candidat en mode binaire" && remise "$(git rev-parse HEAD)"
passage S29-sceau-du-candidat-autre-forme 2 "$RELU ≠ épingle, ou sceau différent de la ligne exacte"
remise
# configuration relue changée (rescellée, ré-épinglée) que le candidat ne cite pas (R11 : le run s'arrêterait)
python3 - "$CFG_RELUE" <<'PYCFG' && resceller "$CFG_RELUE" || { echo "S40 : montage impossible"; exit 2; }
import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))
c["n_tirages"] = 1000
open(sys.argv[1], "w", encoding="utf-8").write(json.dumps(c, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
PYCFG
git add -A "$CFG_RELUE" "$CFG_RELUE.sha256" && epingle_versee "s|^CONFIG_RELUE=[0-9a-f]\{64\}|CONFIG_RELUE=$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)|" "configuration que le candidat ne cite pas" \
    || { echo "S40 : montage impossible"; exit 2; }
passage S40-configuration-non-citee-par-le-candidat 2 "le candidat relu ne cite pas l'empreinte canonique de la configuration relue"
retour
# sceaux produits ≠ épingles : un faux cp, en tête du PATH pour ce seul passage, altère la copie de la configuration
mkdir -p "$E/faux" && cat > "$E/faux/cp" <<'FAUXCP'
#!/usr/bin/env bash
/bin/cp "$@" || exit $?
case "${@: -1}" in *P4-instrument-config-v1.json) echo " " >> "${@: -1}" ;; esac
FAUXCP
chmod +x "$E/faux/cp"
PATH="$E/faux:$PATH" passage S38-sceaux-produits-differents-des-epingles 2 "sceaux du préenregistrement ou de la configuration ≠ épingles"
remise
echo x >> "prereg/contre-lectures/$RA" && resceller "prereg/contre-lectures/$RA" \
    && git commit -qam "essai : rapport altéré" && remise "$(git rev-parse HEAD)"
passage S30-rapport-altere 2 "rapport $RA : empreinte différente de l'épingle"
remise
echo x > prereg/contre-lectures/P4-essai-autre-v1.md && resceller prereg/contre-lectures/P4-essai-autre-v1.md \
    && git add prereg/contre-lectures/ && git commit -qm "essai : rapport de la famille non épinglé" && remise "$(git rev-parse HEAD)"
passage S31-rapport-non-epingle 2 "≠ épinglés"
remise
git push -q "$E/distant.git" "$J:refs/heads/calcul/p4-reel-v1"
passage S32-branche-de-resultats-presente 2 "branche calcul/p4-reel-v1 : code 0"
git -C "$E/distant.git" branch -D calcul/p4-reel-v1 > /dev/null
remise
echo "# essai" >> "$V/recuperation_p4_v1.sh" && resceller "$V/recuperation_p4_v1.sh" && cp "$V/recuperation_p4_v1.sh" "$E/H/" \
    && git commit -qam "essai : copie versée de la récupération changée" && remise "$(git rev-parse HEAD)"
passage S33-script-repete-autre-que-la-copie 2 "script répété ≠ copie versée : recuperation_p4_v1.sh"
git show "$J:$V/recuperation_p4_v1.sh" > "$E/H/recuperation_p4_v1.sh"
remise
# preuves des essais : journal absent, sceau d'un journal faux, journal au verdict non conforme, journal devenu caduc
git rm -q "$V/banc-verifications-p4-v1.log" "$V/banc-verifications-p4-v1.log.sha256" && git commit -qm "essai : journal de preuve retiré" && remise "$(git rev-parse HEAD)"
passage S41-preuve-absente 2 "$V/banc-verifications-p4-v1.log non suivi à HEAD"
remise
echo ajout >> "$V/banc-lanceur-p4-v1.log" && git commit -qam "essai : journal de preuve sans son sceau exact" && remise "$(git rev-parse HEAD)"
passage S41b-preuve-sans-son-sceau 2 "preuves des essais : sceau de banc-lanceur-p4-v1.log absent ou non conforme"
remise
sed -i 's/cas non conformes : 0/cas non conformes : 1/' "$V/banc-controles-p4-v1.log" && resceller "$V/banc-controles-p4-v1.log" \
    && git commit -qam "essai : journal de preuve au verdict non conforme" && remise "$(git rev-parse HEAD)"
passage S41c-preuve-au-verdict-non-conforme 2 "preuves des essais : journal banc-controles-p4-v1.log : dernière ligne"
remise
echo "# corrigé après son banc (essai)" >> "$V/lancer_p4_v1.sh" && resceller "$V/lancer_p4_v1.sh" && cp "$V/lancer_p4_v1.sh" "$E/H/lancer_p4_v1.sh" \
    && git commit -qam "essai : lanceur corrigé après son banc" && remise "$(git rev-parse HEAD)"
passage S41d-preuve-caduque 2 "preuves des essais : lancer_p4_v1.sh éprouvé ≠ copie versée"
git show "$J:$V/lancer_p4_v1.sh" > "$E/H/lancer_p4_v1.sh"
remise
# adresse de origin autre que le dépôt de travail : un dépôt nu local nommé comme la copie publique, en lecture, en
# poussée, puis en seconde adresse de poussée ; le dépôt nu doit rester vide
git init -q --bare "$E/lciric/controle-ia.git"
vide() { [ -z "$(git -C "$E/lciric/controle-ia.git" for-each-ref)" ] && echo "    copie publique simulée restée vide : CONFORME" || { echo "    copie publique simulée NON VIDE : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }; }
git remote set-url origin "$E/lciric/controle-ia.git"
passage S39-origin-copie-publique 2 "adresse de origin en lecture"
vide; remise
git remote set-url --push origin "$E/lciric/controle-ia.git"
passage S39b-poussee-vers-la-copie-publique 2 "adresse de origin --push"
vide; remise
git remote set-url --add --push origin "$E/lciric/controle-ia.git"
[ "$(git remote get-url --all --push origin | wc -l)" = 2 ] || { echo "S39c : montage impossible"; exit 2; }
passage S39c-seconde-adresse-de-poussee 2 "une seule adresse admise"
vide; remise
# chaîne v2 (RC-donnees-08) : liste des chemins gelés de HEAD qui s'exclut elle-même et exclut un dossier changé :
# lue dans 7a54d43, elle voit le changement (refus)
sed -i 's|":(exclude)traces", ":(exclude)CLAUDE.md")|":(exclude)traces", ":(exclude)CLAUDE.md", ":(exclude)src/controle_ia/sondes", ":(exclude)src/controle_ia/harnais/validation_reelle.py")|' src/controle_ia/harnais/validation_reelle.py \
    && grep -q 'exclude)src/controle_ia/sondes' src/controle_ia/harnais/validation_reelle.py && echo "# essai" >> src/controle_ia/sondes/evaluation.py \
    && git commit -qam "essai : liste des chemins gelés qui s'exclut elle-même" && remise "$(git rev-parse HEAD)" || { echo "S42 : montage impossible"; exit 2; }
passage S42-liste-des-chemins-geles-alteree 2 "arbre gelé de HEAD ≠ celui de P3"
remise
passage S34-sain-apres-les-artefacts 0 "poussé ; préenregistrement"
remise
git status --short | head -5 | sed 's/^/    reste : /'
P_CACHE=$(find "$E/depot/src" "$E/depot/$V" "$HN" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cd "$E" && rm -rf "$E/depot" "$E/distant.git"
echo "FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
