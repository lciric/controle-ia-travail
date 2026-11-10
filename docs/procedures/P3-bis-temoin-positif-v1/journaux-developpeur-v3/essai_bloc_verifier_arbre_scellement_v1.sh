#!/usr/bin/env bash
# Essai R5 du bloc « verifier-arbre sur S, hors de DEPOT » de sceller_p3bis_v1.sh (CD-05), extrait tel quel du script (lignes
# entre le commentaire du bloc et « rm -rf "$VA" "$VA.txt" »), joué sur un dépôt synthétique où des chemins interdits sont
# FABRIQUÉS (témoins, aucun vrai fichier interdit) ; seule change, dans la copie du bloc, PYTHONPATH=src → src de l'arbre.
# Bloc-notes du développeur ; journal versé.
SP=/tmp/claude-0/-home-user-controle-ia-travail/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad
W=/home/user/wt-p3bis-lanceur
SC=$W/docs/procedures/P3-bis-temoin-positif-v1/sceller_p3bis_v1.sh
PY=/home/user/controle-ia-travail/.venv/bin/python
E=$SP/essai-bloc-va
[ -e "$E" ] && { echo "$E existe déjà"; exit 2; }
mkdir -p "$E"; export GIT_CEILING_DIRECTORIES=$E
echo "script éprouvé : sceller_p3bis_v1.sh $(sha256sum "$SC" | cut -d' ' -f1)"
a=$(grep -n '^# verifier-arbre sur S, hors de DEPOT' "$SC" | cut -d: -f1); b=$(grep -n '^rm -rf "\$VA" "\$VA.txt"$' "$SC" | cut -d: -f1)
sed -n "${a},${b}p" "$SC" | sed "s|PYTHONPATH=src|PYTHONPATH=$W/src|" > "$E/bloc.sh"
echo "bloc extrait : lignes $a à $b ($(wc -l < "$E/bloc.sh") lignes) ; lignes changées : $(diff <(sed -n "${a},${b}p" "$SC") "$E/bloc.sh" | grep -c '^>')"
D=$E/depot; mkdir -p "$D"; git -C "$D" init -q -b scellement/p3bis-v1; git -C "$D" config user.email essai@example.invalid; git -C "$D" config user.name essai
cd "$D" || exit 2
scelle() { mkdir -p "$(dirname "$1")"; printf '%s\n' "$2" > "$1"; PYTHONPATH=$W/src "$PY" -B -m controle_ia.scellement sceller "$1" > /dev/null; }
scelle docs/a.md "texte a"; scelle prereg/p.md "texte p"; scelle registres/passations/x.md "passation"
scelle docs/notes/bras-attaque/temoin-banc.txt "témoin fabriqué (banc)"
scelle diag/20261109-070232-t06-reel/temoin-banc.txt "témoin fabriqué (banc)"
scelle runs/20261109-070232-t06-reel/temoin-banc.txt "témoin fabriqué (banc)"
scelle diag/r1/lecture-sondes-t06.json "{}"
scelle diag/r1/autre.json "{}"
git add -A; git commit -qm base
nc=0; n=0
jouer() {  # nom bloc code_attendu motif_attendu
    n=$((n+1)); local S; S=$(git rev-parse HEAD)
    ( set -euo pipefail; trap 'exit 3' ERR; S=$S; PY=$PY; . "$2" ) > "$E/sortie-$n.txt" 2>&1; local k=$?
    if [ "$k" = "$3" ] && grep -q "$4" "$E/sortie-$n.txt"; then echo "CONFORME : $1 (code $k)"; else echo "NON CONFORME : $1 (code $k)"; sed 's/^/    /' "$E/sortie-$n.txt"; nc=$((nc+1)); fi
}
printf 'echo "BLOC PASSÉ"\n' >> "$E/bloc.sh"
jouer "cas sain : chemins interdits exclus, absents de l'extraction, arbre intact" "$E/bloc.sh" 0 "BLOC PASSÉ"
sed "s#':(exclude)docs/notes/bras-attaque' ##" "$E/bloc.sh" > "$E/bloc-sans-exclusion.sh"
jouer "artefact : exclusion de docs/notes/bras-attaque retirée : refus, S non poussé" "$E/bloc-sans-exclusion.sh" 2 "REFUS : docs/notes/bras-attaque extrait pour verifier-arbre : S commité localement, NON poussé"
printf 'altéré\n' > docs/a.md; git commit -qam "fichier scellé altéré"
jouer "artefact : fichier scellé altéré dans S : verifier-arbre en échec, S non poussé" "$E/bloc.sh" 2 "verifier-arbre sur S : ÉCHEC docs/a.md"
echo "cas joués : $n ; FIN DE L'ESSAI DU BLOC VERIFIER-ARBRE DU SCELLEMENT ; cas non conformes : $nc"
