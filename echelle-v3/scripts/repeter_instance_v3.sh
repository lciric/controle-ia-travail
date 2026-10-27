#!/usr/bin/env bash
# Répétition locale de la chaîne d'instance de la comparaison d'échelle v3 (R5, CLX-10, CLY-03), lignée
# « session-depot », 27 octobre 2026 ; déclinée de `repeter_instance_v2.sh` (R12), plus le cas « DUREE_MAX_S absente ». Aucune carte, aucune instance, aucune clé réelle : un dépôt nu local tient lieu de dépôt de travail,
# le modèle minuscule local tient lieu des deux modèles, les jetons sont factices. Un cas sain et six artefacts ; chaque
# cas écrit son journal ; RESUME.txt donne le code attendu et le code obtenu.
# Usage : repeter_instance_v3.sh DOSSIER_NEUF COMMIT MODELE_MINUSCULE VENV
#   COMMIT : commit de la branche d'outils outils/echelle-conscience-eval-v3 (déjà présent dans le dépôt courant)
set -uo pipefail
[ $# -eq 4 ] || { echo "usage : repeter_instance_v3.sh DOSSIER_NEUF COMMIT MODELE_MINUSCULE VENV"; exit 2; }
E=$(realpath -m "$1"); C=$2; MIN=$3; VENV=$4
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
ICI=$(cd "$(dirname "$0")" && pwd)
DEPOT_SRC=$(git -C "$ICI" rev-parse --show-toplevel)
mkdir -p "$E"
git init -q --bare "$E/depot.git"
git -C "$DEPOT_SRC" push -q "$E/depot.git" "$C:refs/heads/outils/echelle-conscience-eval-v3" 2>/dev/null
A="$ICI/amorce_echelle_v3.sh"
resume() { printf '%-28s attendu %s ; obtenu %s ; %s\n' "$1" "$2" "$3" "$4" | tee -a "$E/RESUME.txt"; }
cas() {  # $1 nom, $2 code attendu, puis variables d'environnement, puis la commande
    local nom=$1 attendu=$2; shift 2
    mkdir -p "$E/$nom"
    ( cd "$E/$nom" && env "$@" > "$E/$nom/sortie.log" 2>&1 ); local code=$?
    local etat; [ "$code" = "$attendu" ] && etat=conforme || etat=ÉCART
    resume "$nom" "$attendu" "$code" "$etat"
}
COMMUN=(GH_TOKEN=jeton-factice-gh DEPOT_URL="$E/depot.git" VENV_EXISTANT="$VENV" GO_ID=GO-0000-00-00-00 DUREE_MAX_S=4500)

# 1. cas sain : deux mesures (modèle minuscule), deux poussées
cas sain 0 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-sain RACINE_AMORCE="$E/sain" MODELE_LOCAL="$MIN" bash "$A"
n=$(git -C "$E/depot.git" rev-list --count "$C..donnees/essai-sain" 2>/dev/null || echo 0)
resume "sain : commits de résultats" "2" "$n" "$([ "$n" = 2 ] && echo conforme || echo ÉCART)"
# 2. mauvais commit
cas mauvais-commit 1 "${COMMUN[@]}" COMMIT=0000000000000000000000000000000000000000 BRANCHE=donnees/essai-a2 \
    RACINE_AMORCE="$E/mauvais-commit" MODELE_LOCAL="$MIN" bash "$A"
# 3. branche des résultats déjà présente
cas branche-presente 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-sain RACINE_AMORCE="$E/branche-presente" \
    MODELE_LOCAL="$MIN" bash "$A"
# 4. stimuli altérés (commit d'essai sur une branche d'essai du dépôt nu)
git clone -q "$E/depot.git" "$E/clone-altere" && git -C "$E/clone-altere" checkout -q outils/echelle-conscience-eval-v3 \
    && printf ' ' >> "$E/clone-altere/echelle-v3/stimuli/echelle-v2.json" \
    && git -C "$E/clone-altere" -c user.name=essai -c user.email=essai@invalid commit -q -am "essai : stimuli altérés" \
    && git -C "$E/clone-altere" push -q origin HEAD:refs/heads/outils/essai-altere
CA=$(git -C "$E/clone-altere" rev-parse HEAD)
cas stimuli-alteres 1 "${COMMUN[@]}" COMMIT="$CA" BRANCHE=donnees/essai-a4 BRANCHE_CODE=outils/essai-altere \
    RACINE_AMORCE="$E/stimuli-alteres" MODELE_LOCAL="$MIN" bash "$A"
# 5. clé dans les sorties : le jeton factice apparaît dans les journaux (chemin du modèle) ; rien n'est poussé
cas cle-dans-sorties 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-a5 RACINE_AMORCE="$E/cle-dans-sorties" \
    MODELE_LOCAL="$MIN" HF_TOKEN="modele-minuscule" bash "$A"
p=$(git -C "$E/depot.git" rev-parse --verify -q donnees/essai-a5 >/dev/null && echo poussée || echo absente)
resume "clé : branche des résultats" "absente" "$p" "$([ "$p" = absente ] && echo conforme || echo ÉCART)"
# 6. git ls-remote en échec (origine injoignable après le clonage) : arrêt avant tout calcul
git clone -q --branch outils/echelle-conscience-eval-v3 "$E/depot.git" "$E/ls-remote/depot"
git -C "$E/ls-remote/depot" remote set-url origin "$E/inexistant.git"
cas ls-remote-en-echec 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-a6 TRAVAIL="$E/ls-remote/travail" \
    MODELE_LOCAL="$MIN" bash "$E/ls-remote/depot/echelle-v3/scripts/echelle_instance_v3.sh"
# 7. téléchargement refusé (jeton factice sur un modèle à licence ; aucune carte : PERMETTRE_SANS_CARTE)
cas telechargement-refuse 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-a7 RACINE_AMORCE="$E/telechargement-refuse" \
    HF_TOKEN=hf_jeton_factice_essai PERMETTRE_SANS_CARTE=1 HF_HOME="$E/telechargement-refuse/cache-hf" bash "$A"
# 8. DUREE_MAX_S absente : l'amorce refuse avant tout clonage et tout calcul (CLY-03)
cas duree-absente 1 GH_TOKEN=jeton-factice-gh DEPOT_URL="$E/depot.git" VENV_EXISTANT="$VENV" GO_ID=GO-0000-00-00-00 \
    COMMIT="$C" BRANCHE=donnees/essai-a8 RACINE_AMORCE="$E/duree-absente" MODELE_LOCAL="$MIN" bash "$A"
(cd "$E" && find . -name 'sortie.log' -o -name 'journal.txt' | LC_ALL=C sort | xargs sha256sum > EMPREINTES-repetition.txt)
grep -c ÉCART "$E/RESUME.txt" >/dev/null && { echo "écart(s) : voir $E/RESUME.txt"; exit 1; }
echo "répétition conforme : $E/RESUME.txt"
exit 0
