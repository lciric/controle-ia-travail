#!/usr/bin/env bash
# Essai R5 de la garde de place disque de repetition_finale_p3bis_v1.sh (CD-04), sur une copie : seules changent la ligne des
# épingles (neutralisée : les épingles ne sont pas remplies avant le candidat), PLACE_MIN_KO (valeur de l'essai) et DEPOT
# (chemin absent : après la garde, le clonage échoue, rien n'est cloné). Bloc-notes du développeur ; journal versé.
SP=/tmp/claude-0/-home-user-controle-ia-travail/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad
H=/home/user/wt-p3bis-lanceur/docs/procedures/P3-bis-temoin-positif-v1
E=$SP/essai-seuil-finale
[ -e "$E" ] && { echo "$E existe déjà"; exit 2; }
mkdir -p "$E"
echo "script éprouvé : repetition_finale_p3bis_v1.sh $(sha256sum "$H/repetition_finale_p3bis_v1.sh" | cut -d' ' -f1)"
reel=$(sed -n 's/^PLACE_MIN_KO=\([0-9A-Z_]*\).*/\1/p' "$H/repetition_finale_p3bis_v1.sh")
libre=$(df -Pk "$E" | awk 'NR==2 {print $4}')
echo "seuil du script : $reel ko ; place libre au moment de l'essai : $libre ko"
nc=0; n=0
cas() {  # nom valeur code_attendu motif_attendu
    n=$((n+1)); local c="$E/c$n"; mkdir -p "$c"
    cp "$H"/*_p3bis_v1.sh "$H"/*_p3bis_v1.py "$c/"
    sed -e 's|^grep -qE .*A_EPINGLER.*|true  # épingles : neutralisé pour l essai|' -e "s|^PLACE_MIN_KO=.*|PLACE_MIN_KO=$2|" \
        -e "s|^DEPOT=.*|DEPOT=$E/absent|" "$H/repetition_finale_p3bis_v1.sh" > "$c/repetition_finale_p3bis_v1.sh"
    local lc; lc=$(diff "$H/repetition_finale_p3bis_v1.sh" "$c/repetition_finale_p3bis_v1.sh" | grep -c '^>')
    bash "$c/repetition_finale_p3bis_v1.sh" scellement/p3bis-v1 "$c/racine" > "$c/sortie.txt" 2>&1; local k=$?
    if [ "$k" = "$3" ] && grep -q "$4" "$c/sortie.txt" && [ "$5" != absent -o ! -e "$c/racine" ]; then echo "CONFORME : $1 (code $k ; $lc lignes changées)"
    else echo "NON CONFORME : $1 (code $k)"; sed 's/^/    /' "$c/sortie.txt"; nc=$((nc+1)); fi
}
cas "artefact : place libre sous le seuil, refus avant toute écriture" $((libre + 100000000)) 2 "ko libres (.* ko exigés : mesure plus marge, CD-04)" absent
cas "artefact : seuil non fixé" A_MESURER 2 "seuil de place disque non fixé" absent
cas "cas sain : place libre au-dessus du seuil, la garde laisse passer (clonage d'un dépôt absent ensuite)" 1 2 "clone de scellement/p3bis-v1 impossible"
echo "cas joués : $n ; FIN DE L'ESSAI DE LA GARDE DE PLACE DE LA RÉPÉTITION FINALE ; cas non conformes : $nc"
