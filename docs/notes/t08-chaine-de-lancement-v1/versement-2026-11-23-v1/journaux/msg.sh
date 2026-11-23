journal(){ echo "JOURNAL $1"; }; consigner_arret(){ :; }; refus(){ echo "REFUS $1"; }
GARDES=$(timeout -k 1 1 sleep 5 2>&1) || { rc=$?; MG=$(printf '%s' "$GARDES" | tail -n 1); [ -n "$MG" ] || { MG="aucune sortie (code $rc)"; { [ "$rc" = 124 ] || [ "$rc" = 137 ]; } && MG="$MG : délai de 900 s dépassé"; }   # T08 tentative 1 : message vide
    journal "gardes avant tout calcul : $MG"; consigner_arret "gardes de l'instance"; refus "gardes avant tout calcul : $(printf '%s' "$MG" | cut -c1-300)"; }
GARDES=$(echo "ARRÊT : interdit trouvé"; exit 1) || { rc=$?; MG=$(printf '%s' "$GARDES" | tail -n 1); [ -n "$MG" ] || { MG="aucune sortie (code $rc)"; { [ "$rc" = 124 ] || [ "$rc" = 137 ]; } && MG="$MG : délai de 900 s dépassé"; }   # T08 tentative 1 : message vide
    journal "gardes avant tout calcul : $MG"; consigner_arret "gardes de l'instance"; refus "gardes avant tout calcul : $(printf '%s' "$MG" | cut -c1-300)"; }
