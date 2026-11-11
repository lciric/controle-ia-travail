#!/usr/bin/env bash
# Chaîne v2 (2026-11-11 ; règle (a') de P3-bis : R-2296, R-2320 ; consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`) : copie de `repetition_finale_p3bis_v1.sh`, gardé
# tel quel (R12), noms de la chaîne en v2 ; copie de la chaîne par le motif `*_p3bis_v2`.
# Brouillon 3 (2026-11-10, 09:05 UTC) : seuil de place disque fixé (CD-04) : PLACE_MIN_KO = mesure + marge, détail ci-dessous.
# Brouillon 2 (2026-11-10, contre-lecture différentielle) : clone de la branche de scellement en extraction partielle
# (CD-05 ; aucun chemin interdit extrait, absence vérifiée) ; copie des contrôles clonée du dépôt nu local avec --shared ;
# seuil de place disque fixé à la mesure plus une marge écrite (CD-04, PLACE_MIN_KO).
# Répétition finale de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au
# 2026-11-23 : R-2077), v1, EN MODE DÉCISIF, à blanc : écrite maintenant, jouée AU CANDIDAT seulement (épingles des
# contrôles remplies, candidat relu, code corrigé relu, essai de fermeture versé, longueurs attendues versées). Déclinée de
# docs/procedures/P3-premier-test-v2/repetition_finale_p3_v1.sh (P3) sous un nom neuf (R12).
# Sur un clone partagé du dépôt de la session à la branche de scellement (tête = candidat, avant S) et un dépôt nu local
# en guise de dépôt distant (rien n'est poussé sur le dépôt de travail) :
#   1. copie du scellement (lignes changées, comptées et déclarées : H, dossier des originaux ; DEPOT, DISTANT,
#      PREUVES_EXIGEES — elle ne peut exiger son propre journal) : fait S, le pousse sur le dépôt nu, le relit ;
#   2. copie des contrôles avant dépense (ligne changée : le clonage, depuis le dépôt nu) : TOUS les blocs réels, sans
#      bouchon — vrai tokeniseur de l'agent (Hugging Face : jetons de la session exigés), gardes du lanceur run_v2,
#      liste ciblée « N passed » exact, essai de fermeture rejoué au commit S, versions de l'environnement PY ;
#   3. module commun : preuves des six autres journaux de S.
# Ce qu'elle ne joue pas, déclaré : la création (le lanceur exige ce journal parmi les preuves de S) ; la chaîne fermée
# sur des sorties réelles d'un run décisif (aucune n'existe avant la course : l'essai différentiel de fermeture du code
# corrigé en tient lieu, rejoué au bloc 6 des contrôles ; s'il joue le mode décisif sous un texte scellé, ce bloc le
# couvre). Place disque (CD-04) : refus sous PLACE_MIN_KO ko libres dans le dossier parent de RACINE_NEUVE (même disque
# que /tmp, où vont l'extraction du scellement et la liste ciblée). Mesure du 2026-11-10 au commit du code a1de3915, en
# rejouant les mêmes commandes (clones, extraction partielle, git archive) et en relevant la liste et l'essai :
#   dépôt (clone partagé d'un dépôt superficiel : objets copiés, extraction partielle) 4 168 320 ko ; dépôt nu
#   distant.git 1 558 424 ko ; pendant le scellement, extraction git archive pour verifier-arbre 2 404 304 ko (effacée
#   avant les contrôles) ; pendant les contrôles, clone des contrôles depuis le dépôt nu 4 087 844 ko, dossier temporaire
#   de la liste ciblée v2 (531 essais) 1 811 908 ko, dossier de l'essai de fermeture 17 540 ko (pic relevé toutes les 10 s).
#   Pic : contrôles = 4 168 320 + 1 558 424 + 4 087 844 + 1 811 908 + 17 540 = 11 644 036 ko (scellement : 8 131 048 ko).
#   Marge écrite : 1 048 576 ko (1 Gio) pour le cache du tokeniseur (non mesuré, quelques dizaines de Mo attendus), les
#   pics de l'essai entre deux relevés, la croissance de S sur a1de3915 (texte, journaux : quelques Mo) et l'écart du/df.
#   Seuil : 11 644 036 + 1 048 576 = 12 692 612 ko. Les écritures d'autres sessions pendant la répétition ne sont pas couvertes.
# Journal : « script éprouvé : <script> <sha256> » (copies versées : scellement, contrôles, module commun, ce script),
# lignes changées, sorties des étapes, dernière ligne « RÉPÉTITION FINALE DE P3-BIS : CONFORME ».
# Usage : repetition_finale_p3bis_v2.sh BRANCHE_DE_SCELLEMENT RACINE_NEUVE
set -uo pipefail
[ $# -eq 2 ] && [[ "$1" =~ ^scellement/p3bis-v[0-9]+$ ]] || { echo "usage : repetition_finale_p3bis_v2.sh scellement/p3bis-vN RACINE_NEUVE"; exit 2; }
BRANCHE=$1; R=$(realpath -m "$2")
DEPOT=/home/user/controle-ia-travail
H=$(dirname "$(realpath "$0")")
EXTRACTION=('/*' '!/docs/notes/bras-attaque/' '!/diag/20261109-070232-t06-reel/' '!/runs/20261109-070232-t06-reel/' '!/donnees/bras-attaque*' '!/donnees/mode-tenu-a-l-ecart*' '!/diag/*/lecture-sondes-t06.json*' '!/scripts/extraire_mesures_epreuve_t06_v1.py*')
ABSENTS=(docs/notes/bras-attaque diag/20261109-070232-t06-reel runs/20261109-070232-t06-reel scripts/extraire_mesures_epreuve_t06_v1.py)
PLACE_MIN_KO=12692612                            # CD-04 : mesure 11 644 036 ko + marge 1 048 576 ko (voir l'en-tête)
PREUVES_SANS_FINALE="banc-verifications-p3bis-v2.log banc-lanceur-p3bis-v2.log banc-surveillance-p3bis-v2.log banc-controles-p3bis-v2.log banc-recuperation-p3bis-v2.log repetition-jouet-p3bis-v2.log"
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
grep -qE '^[A-Z_]+="?A_EPINGLER' "$H/controles_avant_depense_p3bis_v2.sh" && { echo "épingles des contrôles non remplies : la répétition finale se joue au candidat"; exit 2; }
[[ "$PLACE_MIN_KO" =~ ^[0-9]+$ ]] || { echo "seuil de place disque non fixé"; exit 2; }
LIBRE=$(df -Pk "$(dirname "$R")" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge "$PLACE_MIN_KO" ] || { echo "place disque : $LIBRE ko libres ($PLACE_MIN_KO ko exigés : mesure plus marge, CD-04)"; exit 2; }
for s in sceller_p3bis_v2.sh controles_avant_depense_p3bis_v2.sh verifications_p3bis_v2.py; do echo "script éprouvé : $s $(sha256sum "$H/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
echo "début : $(date -u +%FT%TZ)"
mkdir -p "$R/H" || exit 2
git clone -q --no-checkout --shared --branch "$BRANCHE" "$DEPOT" "$R/depot" || { echo "clone de $BRANCHE impossible"; exit 2; }
git -C "$R/depot" sparse-checkout set --no-cone "${EXTRACTION[@]}" && git -C "$R/depot" checkout -q "$BRANCHE" || { echo "extraction partielle de $BRANCHE impossible"; exit 2; }
for x in "${ABSENTS[@]}"; do [ -e "$R/depot/$x" ] && { echo "REFUS : $x extrait sur disque (interdits communs v2, règle 9 ; CD-05)"; exit 2; }; done
git clone -q --bare --shared "$R/depot" "$R/distant.git" || exit 2
git -C "$R/depot" remote set-url origin "$R/distant.git"
cp "$H"/*_p3bis_v2.sh "$H"/*_p3bis_v2.py "$R/H/"
sed -e "s|^H=.*|H=$H|" -e "s|^DEPOT=.*|DEPOT=$R/depot|" -e "s|^DISTANT=.*|DISTANT=$R/distant.git|" -e "s|^PREUVES_EXIGEES=.*|PREUVES_EXIGEES=\"$PREUVES_SANS_FINALE\"|" \
    "$H/sceller_p3bis_v2.sh" > "$R/H/sceller_p3bis_v2.sh"
sed -e "s|git clone -q --no-checkout \"\$DEPOT_URL\" \"\$D\"|git clone -q --no-checkout --shared \"$R/distant.git\" \"\$D\"|" "$H/controles_avant_depense_p3bis_v2.sh" > "$R/H/controles_avant_depense_p3bis_v2.sh"
echo "lignes changées : scellement $(diff "$H/sceller_p3bis_v2.sh" "$R/H/sceller_p3bis_v2.sh" | grep -c '^>') (H : dossier des originaux, DEPOT, DISTANT, PREUVES_EXIGEES) ; contrôles $(diff "$H/controles_avant_depense_p3bis_v2.sh" "$R/H/controles_avant_depense_p3bis_v2.sh" | grep -c '^>') (clonage)"
# la copie du scellement lit les épingles et compare la chaîne dans H = le dossier des originaux (versés à la tête) ; ses
# propres lignes changées sont comptées ci-dessus
echo "== 1. scellement (copie) =="
( cd "$R/depot" && bash "$R/H/sceller_p3bis_v2.sh" "$BRANCHE" ) > "$R/scellement.txt" 2>&1; c1=$?
sed 's/^/    /' "$R/scellement.txt"
S=$(sed -n 's/^S = \([0-9a-f]\{40\}\)$/\1/p' "$R/scellement.txt")
ok=1
[ "$c1" = 0 ] && [[ "$S" =~ ^[0-9a-f]{40}$ ]] && tail -1 "$R/scellement.txt" | grep -qx "SCELLEMENT : CONFORME" || ok=0
echo "== 2. contrôles avant dépense, mode décisif, tous les blocs réels =="
if [ "$ok" = 1 ]; then
    bash "$R/H/controles_avant_depense_p3bis_v2.sh" "$S" "$R/clone-controles" calcul/p3bis-reel-v1 > "$R/controles.txt" 2>&1; c2=$?
    sed 's/^/    /' "$R/controles.txt"
    [ "$c2" = 0 ] && tail -1 "$R/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || ok=0
fi
echo "== 3. preuves des six autres journaux de S =="
if [ "$ok" = 1 ]; then
    PR="$R/preuves"; mkdir -p "$PR"
    for j in $PREUVES_SANS_FINALE; do git -C "$R/depot" show "$S:docs/procedures/P3-bis-temoin-positif-v1/$j" > "$PR/$j" 2>/dev/null || ok=0; done
    # shellcheck disable=SC2086
    python3 -I "$H/verifications_p3bis_v2.py" preuves "$PR" $PREUVES_SANS_FINALE > "$R/preuves.txt" 2>&1 || ok=0
    sed 's/^/    /' "$R/preuves.txt"
fi
rm -rf "$R/clone-controles" "$R/clone-controles.travail"
echo "fin : $(date -u +%FT%TZ)"
if [ "$ok" = 1 ]; then echo "RÉPÉTITION FINALE DE P3-BIS : CONFORME"; exit 0; fi
echo "RÉPÉTITION FINALE DE P3-BIS : ÉCHEC (voir les sorties ci-dessus)"; exit 1
