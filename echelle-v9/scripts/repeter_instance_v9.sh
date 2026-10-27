#!/usr/bin/env bash
# Répétition locale de la chaîne d'instance de la comparaison d'échelle v8 (R5, CLX-10, CLY-03, CLY-14, CLZ-04, CLW-08,
# CLU-04, CLT-03), lignée « session-depot », 27 octobre 2026 ; déclinée de `repeter_instance_v7.sh` (R12) : les cas de
# la v7, plus le clonage lent (CLT-03 : un faux git qui attend 8 s avant de cloner, création réglée pour qu'il reste
# 2 704 s avant le clonage et moins de 2 700 après ; le délai recalculé après le clonage refuse, avec la ligne de fin),
# et la ligne « délai recalculé après le clonage » du cas sain. Depuis la v7 : le clonage bloqué (CLU-04) et la borne
# réelle du clonage écrite par le cas sain. Aucune carte, aucune
# instance, aucune clé réelle : un dépôt nu local tient lieu de dépôt de travail, le modèle minuscule local tient lieu
# des deux modèles, les jetons sont factices. Un cas sain et quinze artefacts ; chaque cas écrit son journal ;
# RESUME.txt donne le code attendu et le code obtenu. Nouveau depuis la v4 (CLW-08) : chaque refus précoce de l'amorce
# doit écrire sa ligne « fin, code 1 », que la surveillance relit ; vérifié sur les six refus précoces.
# Usage : repeter_instance_v9.sh DOSSIER_NEUF COMMIT MODELE_MINUSCULE VENV
#   COMMIT : commit de la branche d'outils outils/echelle-conscience-eval-v9 (déjà présent dans le dépôt courant)
set -uo pipefail
[ $# -eq 4 ] || { echo "usage : repeter_instance_v9.sh DOSSIER_NEUF COMMIT MODELE_MINUSCULE VENV"; exit 2; }
E=$(realpath -m "$1"); C=$2; MIN=$3; VENV=$4
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
ICI=$(cd "$(dirname "$0")" && pwd)
DEPOT_SRC=$(git -C "$ICI" rev-parse --show-toplevel)
mkdir -p "$E"
git init -q --bare "$E/depot.git"
git -C "$DEPOT_SRC" push -q "$E/depot.git" "$C:refs/heads/outils/echelle-conscience-eval-v9" 2>/dev/null
A="$ICI/amorce_echelle_v9.sh"
resume() { printf '%-32s attendu %s ; obtenu %s ; %s\n' "$1" "$2" "$3" "$4" | tee -a "$E/RESUME.txt"; }
cas() {  # $1 nom, $2 code attendu, puis variables d'environnement, puis la commande
    local nom=$1 attendu=$2; shift 2
    mkdir -p "$E/$nom"
    ( cd "$E/$nom" && env "$@" > "$E/$nom/sortie.log" 2>&1 ); local code=$?
    local etat; [ "$code" = "$attendu" ] && etat=conforme || etat=ÉCART
    resume "$nom" "$attendu" "$code" "$etat"
}
absente() {  # $1 nom du cas, $2 branche qui doit être absente du dépôt nu
    local p; p=$(git -C "$E/depot.git" rev-parse --verify -q "$2" >/dev/null && echo poussée || echo absente)
    resume "$1 : branche des résultats" "absente" "$p" "$([ "$p" = absente ] && echo conforme || echo ÉCART)"
}
MAINTENANT=$(date -u +%s)
SANS_TEMPS=(GH_TOKEN=jeton-factice-gh DEPOT_URL="$E/depot.git" VENV_EXISTANT="$VENV" GO_ID=GO-0000-00-00-00)
COMMUN=("${SANS_TEMPS[@]}" DUREE_MAX_S=4500 CREATION_S="$MAINTENANT")

# 1. cas sain : deux mesures (modèle minuscule), deux poussées
cas sain 0 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-sain RACINE_AMORCE="$E/sain" MODELE_LOCAL="$MIN" bash "$A"
n=$(git -C "$E/depot.git" rev-list --count "$C..donnees/essai-sain" 2>/dev/null || echo 0)
resume "sain : commits de résultats" "2" "$n" "$([ "$n" = 2 ] && echo conforme || echo ÉCART)"
b=$(grep -c 'clonage borné à 600 s$' "$E/sain/sortie.log")
resume "sain : borne du clonage 600 s" "1" "$b" "$([ "$b" = 1 ] && echo conforme || echo ÉCART)"
b=$(grep -c ' : délai recalculé après le clonage : [0-9]* s$' "$E/sain/sortie.log")
resume "sain : délai après le clonage" "1" "$b" "$([ "$b" = 1 ] && echo conforme || echo ÉCART)"
# 2. mauvais commit
cas mauvais-commit 1 "${COMMUN[@]}" COMMIT=0000000000000000000000000000000000000000 BRANCHE=donnees/essai-a2 \
    RACINE_AMORCE="$E/mauvais-commit" MODELE_LOCAL="$MIN" bash "$A"
# 3. branche des résultats déjà présente
cas branche-presente 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-sain RACINE_AMORCE="$E/branche-presente" \
    MODELE_LOCAL="$MIN" bash "$A"
# 4. stimuli altérés (commit d'essai sur une branche d'essai du dépôt nu)
git clone -q "$E/depot.git" "$E/clone-altere" && git -C "$E/clone-altere" checkout -q outils/echelle-conscience-eval-v9 \
    && printf ' ' >> "$E/clone-altere/echelle-v9/stimuli/echelle-v2.json" \
    && git -C "$E/clone-altere" -c user.name=essai -c user.email=essai@invalid commit -q -am "essai : stimuli altérés" \
    && git -C "$E/clone-altere" push -q origin HEAD:refs/heads/outils/essai-altere
CA=$(git -C "$E/clone-altere" rev-parse HEAD)
cas stimuli-alteres 1 "${COMMUN[@]}" COMMIT="$CA" BRANCHE=donnees/essai-a4 BRANCHE_CODE=outils/essai-altere \
    RACINE_AMORCE="$E/stimuli-alteres" MODELE_LOCAL="$MIN" bash "$A"
# 5. clé dans les sorties : le jeton factice apparaît dans les journaux (chemin du modèle) ; rien n'est poussé
cas cle-dans-sorties 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-a5 RACINE_AMORCE="$E/cle-dans-sorties" \
    MODELE_LOCAL="$MIN" HF_TOKEN="modele-minuscule" bash "$A"
absente "clé" donnees/essai-a5
# 6. git ls-remote en échec (origine injoignable après le clonage) : arrêt avant tout calcul
git clone -q --branch outils/echelle-conscience-eval-v9 "$E/depot.git" "$E/ls-remote/depot"
git -C "$E/ls-remote/depot" remote set-url origin "$E/inexistant.git"
cas ls-remote-en-echec 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-a6 TRAVAIL="$E/ls-remote/travail" \
    MODELE_LOCAL="$MIN" bash "$E/ls-remote/depot/echelle-v9/scripts/echelle_instance_v9.sh"
# 7. téléchargement refusé (jeton factice sur un modèle à licence ; aucune carte : PERMETTRE_SANS_CARTE)
cas telechargement-refuse 1 "${COMMUN[@]}" COMMIT="$C" BRANCHE=donnees/essai-a7 RACINE_AMORCE="$E/telechargement-refuse" \
    HF_TOKEN=hf_jeton_factice_essai PERMETTRE_SANS_CARTE=1 HF_HOME="$E/telechargement-refuse/cache-hf" bash "$A"
# 8 à 10. DUREE_MAX_S absente, 4 499 ou 21 601 s : l'amorce refuse avant tout clonage et tout calcul (CLY-03, CLZ-04)
cas duree-absente 1 "${SANS_TEMPS[@]}" CREATION_S="$MAINTENANT" COMMIT="$C" BRANCHE=donnees/essai-a8 \
    RACINE_AMORCE="$E/duree-absente" MODELE_LOCAL="$MIN" bash "$A"
cas duree-4499 1 "${SANS_TEMPS[@]}" DUREE_MAX_S=4499 CREATION_S="$MAINTENANT" COMMIT="$C" BRANCHE=donnees/essai-a9 \
    RACINE_AMORCE="$E/duree-4499" MODELE_LOCAL="$MIN" bash "$A"
cas duree-21601 1 "${SANS_TEMPS[@]}" DUREE_MAX_S=21601 CREATION_S="$MAINTENANT" COMMIT="$C" BRANCHE=donnees/essai-a10 \
    RACINE_AMORCE="$E/duree-21601" MODELE_LOCAL="$MIN" bash "$A"
# 11. CREATION_S absente : refus (CLZ-05)
cas creation-absente 1 "${SANS_TEMPS[@]}" DUREE_MAX_S=4500 COMMIT="$C" BRANCHE=donnees/essai-a11 \
    RACINE_AMORCE="$E/creation-absente" MODELE_LOCAL="$MIN" bash "$A"
# 12. création trop ancienne : moins de 2 700 s restants avant le plafond ; refus, aucun calcul (CLZ-05)
cas creation-trop-ancienne 1 "${SANS_TEMPS[@]}" DUREE_MAX_S=4500 CREATION_S=$((MAINTENANT - 1300)) COMMIT="$C" \
    BRANCHE=donnees/essai-a12 RACINE_AMORCE="$E/creation-trop-ancienne" MODELE_LOCAL="$MIN" bash "$A"
# 13. compagnon d'empreinte d'un script faux sur l'instance : le script de mesure change, son compagnon non (CLY-14)
git clone -q "$E/depot.git" "$E/clone-compagnon" && git -C "$E/clone-compagnon" checkout -q outils/echelle-conscience-eval-v9 \
    && printf '# essai\n' >> "$E/clone-compagnon/echelle-v9/scripts/mesurer_echelle_v9.py" \
    && git -C "$E/clone-compagnon" -c user.name=essai -c user.email=essai@invalid commit -q -am "essai : compagnon faux" \
    && git -C "$E/clone-compagnon" push -q origin HEAD:refs/heads/outils/essai-compagnon
CC=$(git -C "$E/clone-compagnon" rev-parse HEAD)
cas compagnon-faux 1 "${COMMUN[@]}" COMMIT="$CC" BRANCHE=donnees/essai-a13 BRANCHE_CODE=outils/essai-compagnon \
    RACINE_AMORCE="$E/compagnon-faux" MODELE_LOCAL="$MIN" bash "$A"
absente "compagnon faux" donnees/essai-a13
# 14. délai de l'amorce atteint pendant la mesure du petit modèle : code 124, rien n'est poussé (CLZ-04). La mesure du
#     modèle minuscule et sa poussée prennent de 12 à 80 s selon la charge de la machine : un délai de 5 s tombe pendant
#     la mesure du petit (un délai de 20 s, essayé d'abord, tombait après sa poussée, pendant celle du grand)
cas delai-atteint 124 "${COMMUN[@]}" DELAI_ESSAI_S=5 COMMIT="$C" BRANCHE=donnees/essai-a14 \
    RACINE_AMORCE="$E/delai-atteint" MODELE_LOCAL="$MIN" bash "$A"
absente "délai atteint" donnees/essai-a14
sleep 3
r=aucun   # processus dont le dossier courant est sous celui du cas (relu par /proc, jamais tué ici)
for p in /proc/[0-9]*; do
    case "$(readlink "$p/cwd" 2>/dev/null)" in "$E/delai-atteint"*) r="processus restants"; break ;; esac
done
resume "délai atteint : processus" "aucun" "$r" "$([ "$r" = aucun ] && echo conforme || echo ÉCART)"
# 15. clonage bloqué (CLU-04) : un faux git, placé en tête du PATH, ne rend pas la main au clonage (300 s) et passe tout
#     le reste au vrai git ; borne d'essai 5 s : refus, ligne de fin, aucun calcul, en moins de 40 s
mkdir -p "$E/faux-git"
printf '#!/usr/bin/env bash
case " $* " in *" clone "*) sleep 300 ;; esac
exec %s "$@"
' "$(command -v git)" \
    > "$E/faux-git/git"
chmod +x "$E/faux-git/git"
t0=$(date -u +%s)
cas clonage-bloque 1 "${COMMUN[@]}" PATH="$E/faux-git:$PATH" CLONAGE_ESSAI_S=5 COMMIT="$C" BRANCHE=donnees/essai-a15 \
    RACINE_AMORCE="$E/clonage-bloque" MODELE_LOCAL="$MIN" bash "$A"
duree=$(( $(date -u +%s) - t0 ))
resume "clonage bloqué : durée (s)" "< 40" "$duree" "$([ "$duree" -lt 40 ] && echo conforme || echo ÉCART)"
absente "clonage bloqué" donnees/essai-a15
# 17. clonage lent (CLT-03) : un faux git attend 8 s puis clone ; création réglée pour qu'il reste 2 704 s avant le
#     plafond moins 600 s au départ de l'amorce : le contrôle d'avant le clonage passe, celui d'après refuse
mkdir -p "$E/faux-git-lent"
printf '#!/usr/bin/env bash
case " $* " in *" clone "*) sleep 8 ;; esac
exec %s "$@"
' "$(command -v git)" \
    > "$E/faux-git-lent/git"
chmod +x "$E/faux-git-lent/git"
cas clonage-lent 1 "${SANS_TEMPS[@]}" DUREE_MAX_S=4500 CREATION_S=$(( $(date -u +%s) - 1196 )) PATH="$E/faux-git-lent:$PATH" \
    COMMIT="$C" BRANCHE=donnees/essai-a17 RACINE_AMORCE="$E/clonage-lent" MODELE_LOCAL="$MIN" bash "$A"
n=$(grep -c "s restants avant le plafond après le clonage" "$E/clonage-lent/sortie.log")
resume "clonage lent : refus après le clonage" "1" "$n" "$([ "$n" = 1 ] && echo conforme || echo ÉCART)"
absente "clonage lent" donnees/essai-a17
# 16. chaque refus précoce de l'amorce écrit sa ligne de fin, que la surveillance relit (CLW-08, CLU-04)
for c in duree-absente duree-4499 duree-21601 creation-absente creation-trop-ancienne mauvais-commit clonage-bloque \
         clonage-lent; do
    f=$(grep -c '^AMORCE .* : fin, code 1$' "$E/$c/sortie.log")
    resume "$c : ligne de fin" "1" "$f" "$([ "$f" = 1 ] && echo conforme || echo ÉCART)"
done
(cd "$E" && find . -name 'sortie.log' -o -name 'journal.txt' | LC_ALL=C sort | xargs sha256sum > EMPREINTES-repetition.txt)
grep -q ÉCART "$E/RESUME.txt" && { echo "écart(s) : voir $E/RESUME.txt"; exit 1; }
echo "répétition conforme : $E/RESUME.txt"
exit 0
