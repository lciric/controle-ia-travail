#!/usr/bin/env bash
# Scellement du préenregistrement de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29
# jusqu'au 2026-11-23 : R-2077), v1. Texte : brouillon 9 (eb65773f…), en-tête (« S est fait sur une branche tirée du
# commit du code, puis poussé » ; « Le commit de scellement S, que l'amorce extrait, ne change aucun chemin de l'arbre
# gelé depuis le commit du code »), plan, point 9. Décliné de docs/procedures/P3-premier-test-v2/sceller_p3_v1.sh (P3)
# sous un nom neuf (R12). Aucun champ n'est rempli ici : le texte est la copie, octet pour octet, du candidat relu
# (contre-lecture 4), la configuration celle de la configuration relue, les consignes celles des consignes relues ;
# épingles lues dans les contrôles avant dépense (le même texte que les contrôles).
# Ce qui est vérifié avant tout fichier écrit : branche courante = BRANCHE (scellement/p3bis-vN), arbre suivi propre,
# adresse de origin = dépôt de travail seulement (jamais la copie publique) ; aucune épingle « A_EPINGLER » ; commit du
# code relu ancêtre de HEAD, arbre gelé de HEAD égal au commit du code ; sorties absentes (R12) ; candidat, configuration
# et consignes relus versés et scellés à leurs épingles ; configuration relue qui cite les consignes relues (chemin et
# empreinte) ; sortie de l'essai de fermeture, longueurs attendues et rapports épinglés versés et scellés ; scripts de la
# chaîne égaux à leurs copies versées ; preuves des essais (PREUVES_EXIGEES, module commun) et scripts éprouvés égaux
# aux copies versées ; GO (module commun, registre de HEAD, jour du scellement) ; branche de calcul v1 absente du dépôt
# distant. Puis : copies, problemes() vide et aucun marqueur, sceaux, verifier-arbre ; un seul commit S qui n'ajoute que
# les six fichiers ; poussé sur BRANCHE ; relu sur le dépôt distant. La ligne SCELLEMENT-P3BIS du registre
# registres/scellements-v1.md n'est PAS écrite ici (S n'ajoute que six fichiers) : ce script l'imprime, la session mère
# l'inscrit par un commit suivant. Un échec avant le commit retire les fichiers créés ici, et seulement eux. Code 2 sur
# tout arrêt.
# La copie jouée par la répétition finale change les lignes H (dossier des originaux), DEPOT, DISTANT et PREUVES_EXIGEES
# (elle ne peut exiger son propre journal) ; ces lignes sont comptées et déclarées par la répétition finale.
# Usage : sceller_p3bis_v1.sh BRANCHE
set -euo pipefail
trap 'echo "arrêt du scellement (ligne $LINENO)"; exit 2' ERR
[ $# -eq 1 ] && [[ "$1" =~ ^scellement/p3bis-v[0-9]+$ ]] || { echo "usage : sceller_p3bis_v1.sh scellement/p3bis-vN"; exit 2; }
BRANCHE=$1
DEPOT=/home/user/controle-ia-travail
DISTANT=https://github.com/lciric/controle-ia-travail.git     # seule adresse de lecture et de poussée admise
PREUVES_EXIGEES="banc-verifications-p3bis-v1.log banc-lanceur-p3bis-v1.log banc-surveillance-p3bis-v1.log banc-controles-p3bis-v1.log banc-recuperation-p3bis-v1.log repetition-jouet-p3bis-v1.log repetition-finale-p3bis-v1.log"
H=$(dirname "$(realpath "$0")")
CTL=$H/controles_avant_depense_p3bis_v1.sh
VERIF=$H/verifications_p3bis_v1.py
VERSEES=docs/procedures/P3-bis-temoin-positif-v1
P=prereg/P3-bis-temoin-positif-v1.md; CFG=prereg/P3-bis-temoin-positif-config-v1.json; CONSIGNES=prereg/P3-bis-consignes-v1.md
CHAINE="lancer_p3bis_v1.sh verifications_p3bis_v1.py controles_avant_depense_p3bis_v1.sh surveiller_p3bis_v1.sh controle_cinq_minutes_p3bis_v1.sh recuperation_p3bis_v1.sh detruire_p3bis_v1.sh sceller_p3bis_v1.sh repetition_jouet_p3bis_v1.sh repetition_finale_p3bis_v1.sh essais_verifications_p3bis_v1.py essais_lanceur_p3bis_v1.sh essais_surveillance_p3bis_v1.sh essais_controles_p3bis_v1.sh essais_recuperation_p3bis_v1.sh"
plat() { tr '\n' ' ' < "$1" | tr -s ' '; }
epingle() { sed -n "s/^$1=\"\{0,1\}\([^\"#]*\)\"\{0,1\}.*/\1/p" "$CTL" | sed 's/[[:space:]]*$//'; }
[ -f "$CTL" ] && [ -f "$VERIF" ] || { echo "contrôles ou module commun absents de $H"; exit 2; }
grep -qE '^[A-Z_]+="?A_EPINGLER' "$CTL" && { echo "épingle restée « A_EPINGLER » dans les contrôles : candidat non épinglé"; exit 2; }
RELU=$(epingle CANDIDAT_RELU_CHEMIN); RELU_SHA=$(epingle CANDIDAT_RELU)
CFG_RELUE=$(epingle CONFIG_RELUE_CHEMIN); CFG_RELUE_SHA=$(epingle CONFIG_RELUE)
CONS_RELUES=$(epingle CONSIGNES_RELUES_CHEMIN); CONS_RELUES_SHA=$(epingle CONSIGNES_RELUES)
CODE_RELU=$(epingle CODE_RELU); PY=$(epingle PY)
ESSAI_CH=$(epingle ESSAI_FERMETURE_CHEMIN); ESSAI_SHA=$(epingle ESSAI_FERMETURE)
LONG_CH=$(epingle LONGUEURS_ATTENDUES_CHEMIN); LONG_SHA=$(epingle LONGUEURS_ATTENDUES)
RAPPORTS=$(epingle RAPPORTS_ATTENDUS)
[[ "$RELU_SHA" =~ ^[0-9a-f]{64}$ && "$RELU" == brouillons/* && "$CFG_RELUE_SHA" =~ ^[0-9a-f]{64}$ && "$CFG_RELUE" == brouillons/* \
   && "$CONS_RELUES_SHA" =~ ^[0-9a-f]{64}$ && "$CONS_RELUES" == brouillons/* && "$CODE_RELU" =~ ^[0-9a-f]{40}$ \
   && "$ESSAI_SHA" =~ ^[0-9a-f]{64}$ && "$LONG_SHA" =~ ^[0-9a-f]{64}$ && -n "$RAPPORTS" && -x "$PY" ]] \
    || { echo "épingles des contrôles mal formées"; exit 2; }
cd "$DEPOT"
# 1. branche, arbre, adresse
[ "$(git rev-parse --abbrev-ref HEAD)" = "$BRANCHE" ] || { echo "branche courante $(git rev-parse --abbrev-ref HEAD) ≠ $BRANCHE"; exit 2; }
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "arbre suivi non propre"; exit 2; }
URL=$(git remote get-url origin); [ "$URL" = "$DISTANT" ] || [ "$URL" = "${DISTANT%.git}" ] || { echo "origin = $URL : seul le dépôt de travail est admis"; exit 2; }
# 2. commit du code et arbre gelé
git merge-base --is-ancestor "$CODE_RELU" HEAD || { echo "commit du code relu $CODE_RELU non ancêtre de HEAD"; exit 2; }
GELES=$(PYTHONPATH=src "$PY" -B -c "from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))")
# shellcheck disable=SC2086
git diff --quiet "$CODE_RELU" HEAD -- $GELES || { echo "arbre gelé de HEAD ≠ commit du code relu $CODE_RELU"; exit 2; }
# 3. sorties absentes (R12)
for f in "$P" "$CFG" "$CONSIGNES"; do [ -e "$f" ] || [ -e "$f.sha256" ] && { echo "$f ou son sceau existe déjà (R12)"; exit 2; }; done
# 4. pièces versées et scellées à leurs épingles
piece() { [ "$(git show "HEAD:$1" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$2" ] && [ "$(git show "HEAD:$1.sha256" 2>/dev/null)" = "$2  $(basename "$1")" ] \
    || { echo "$1 absent, non scellé ou d'empreinte autre que l'épingle ($2)"; exit 2; }; }
piece "$RELU" "$RELU_SHA"; piece "$CFG_RELUE" "$CFG_RELUE_SHA"; piece "$CONS_RELUES" "$CONS_RELUES_SHA"
piece "$ESSAI_CH" "$ESSAI_SHA"; piece "$LONG_CH" "$LONG_SHA"
for x in $RAPPORTS; do piece "${x%%=*}" "${x#*=}"; done
"$PY" -I -B -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8")); sys.exit(0 if c.get("consignes_sha256") == sys.argv[2] and c.get("chemin_consignes") == sys.argv[3] else 1)' \
    "$CFG_RELUE" "$CONS_RELUES_SHA" "$CONSIGNES" || { echo "configuration relue : consignes citées autres que les consignes relues"; exit 2; }
# 5. chaîne égale à ses copies versées ; preuves des essais
for s in $CHAINE; do
    [ "$(git show "HEAD:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$H/$s" | cut -d' ' -f1)" ] || { echo "$s ≠ sa copie versée à HEAD"; exit 2; }
done
PR=$(mktemp -d)
for j in $PREUVES_EXIGEES; do
    git show "HEAD:$VERSEES/$j" > "$PR/$j" 2>/dev/null && [ "$(git show "HEAD:$VERSEES/$j.sha256" 2>/dev/null)" = "$(sha256sum "$PR/$j" | cut -d' ' -f1)  $j" ] \
        || { rm -rf "$PR"; echo "preuve $j absente de HEAD ou sceau non conforme"; exit 2; }
done
# shellcheck disable=SC2086
python3 -I "$VERIF" preuves "$PR" $PREUVES_EXIGEES > "$PR/sortie.txt" 2>&1 || { m=$(tail -1 "$PR/sortie.txt"); rm -rf "$PR"; echo "preuves : $m"; exit 2; }
while read -r s e; do
    [ "$(git show "HEAD:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] || { rm -rf "$PR"; echo "preuves : $s éprouvé ≠ copie versée"; exit 2; }
done < "$PR/sortie.txt"
rm -rf "$PR"
# 6. GO ; branche de calcul absente du dépôt distant
python3 -I "$VERIF" go "$RELU" registres/go.md "$(date -u +%F)" || { echo "GO non conforme"; exit 2; }
c=0; git ls-remote --exit-code "$DISTANT" refs/heads/calcul/p3bis-reel-v1 > /dev/null 2>&1 || c=$?
[ "$c" = 2 ] || { echo "branche calcul/p3bis-reel-v1 : code $c (2 attendu)"; exit 2; }
# 7. copies, contrôles du texte, sceaux, arbre ; tout échec retire les seuls fichiers créés ici
CREES=()
nettoyer() { for f in "${CREES[@]}"; do rm -f "$f"; done; }
trap 'nettoyer; echo "arrêt du scellement (ligne $LINENO) : fichiers créés retirés"; exit 2' ERR
for paire in "$RELU=$P" "$CFG_RELUE=$CFG" "$CONS_RELUES=$CONSIGNES"; do cp "${paire%%=*}" "${paire#*=}"; CREES+=("${paire#*=}"); done
grep -q '<<[A-Z0-9_]\+>>' "$P" && { nettoyer; echo "marqueurs restants dans le texte"; exit 2; }
PYTHONPATH=src "$PY" -B -c "import sys; from controle_ia.prereg import problemes; p = problemes(sys.argv[1]); print(p); sys.exit(1 if p else 0)" "$P" > /dev/null
CREES+=("$P.sha256" "$CFG.sha256" "$CONSIGNES.sha256")
PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$P" "$CFG" "$CONSIGNES" > /dev/null
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier-arbre . > /dev/null
# 8. un seul commit S, six fichiers ajoutés ; poussé ; relu
git add -- "$P" "$P.sha256" "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256"
[ "$(git diff --cached --name-only | sort | tr '\n' ' ')" = "$(printf '%s\n' "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')" ] \
    || { git reset -q; nettoyer; echo "index : autre chose que les six fichiers"; exit 2; }
trap 'echo "arrêt du scellement après le commit (ligne $LINENO) : vérifier S à la main, rien n est retiré"; exit 2' ERR
git commit -qm "P3-bis : scellement du préenregistrement (S) ; texte, configuration et consignes relus, octet pour octet"
S=$(git rev-parse HEAD)
[ "$(git diff --name-only --diff-filter=A "$S^" "$S" | wc -l)" = 6 ] && [ "$(git diff --name-only "$S^" "$S" | wc -l)" = 6 ]
git push -q origin "HEAD:refs/heads/$BRANCHE"
[ "$(git ls-remote "$DISTANT" "refs/heads/$BRANCHE" | cut -f1)" = "$S" ] || { echo "S non relu sur le dépôt distant"; exit 2; }
echo "ligne à inscrire par la session mère (registres/scellements-v1.md, commit suivant) : | SCELLEMENT-P3BIS | $(TZ=UTC0 git log -1 --format=%cd --date=format-local:%Y-%m-%dT%H:%M:%SZ "$S") | $P | $(sha256sum "$P" | cut -d' ' -f1) |"
echo "S = $S"
echo "SCELLEMENT : CONFORME"
