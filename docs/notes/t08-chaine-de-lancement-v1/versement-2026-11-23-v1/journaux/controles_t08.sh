controles)
    D=$(realpath -m "${2:?dossier neuf}"); JOUR="${3:-$(date -u +%F)}"
    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN : la ligne de GO de calcul de la course, convention de la garde de calcul) : pas de création"; exit 2; }   # T08
    BC="${T08_BRANCHE_CODE:?T08_BRANCHE_CODE : branche qui porte le commit du code cité par CODE-T08}"; AS="${T08_AMORCE_SHA256:?T08_AMORCE_SHA256 : empreinte de l amorce, celle de l ordre de course}"   # T08
    [[ "$AS" =~ ^[0-9a-f]{64}$ ]] || { echo "T08_AMORCE_SHA256 : 64 caractères hexadécimaux"; exit 2; }   # T08
    mkdir -p "$D"
    LIBRE=$(df -Pk "$D" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 2; }
    S=$(commit_s); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement de $P introuvable"; exit 2; }
    timeout 300 git -C "$DEPOT" fetch -q origin main || { echo "fetch impossible"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent de origin/main"; exit 2; }
    git -C "$DEPOT" show "$S:$P" > "$D/prereg-S.md" || { echo "préenregistrement absent de S"; exit 2; }
    [ "$(sha256sum < "$D/prereg-S.md" | cut -d' ' -f1)" = "$(git -C "$DEPOT" show "$S:$P.sha256" 2>/dev/null | cut -d' ' -f1)" ] || { echo "sceau de $P non conforme à S"; exit 2; }   # T08
    # T08 : branche d'entrée relevée (refspec explicite), vérifiée par programme sans la branche de 7b : liste blanche exacte, orpheline, aucun interdit, empreintes
    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/$BE:refs/remotes/origin/$BE" || { echo "branche d'entrée $BE introuvable"; exit 2; }
    EC=$(git -C "$DEPOT" rev-parse "refs/remotes/origin/$BE^{commit}") || { echo "branche d'entrée illisible"; exit 2; }
    git -C "$DEPOT" show "$EC:$CONFIG" > "$D/config.json" 2>/dev/null || { echo "configuration $CONFIG absente de la branche d'entrée"; exit 2; }
    [ "$(git -C "$DEPOT" rev-parse "$EC:$P")" = "$(git -C "$DEPOT" rev-parse "$S:$P")" ] || { echo "texte de la branche d'entrée ≠ texte scellé de S"; exit 2; }
    VB=$(python3 -I -B "$BRANCHE_PROG" verifier --depot "$DEPOT" --ref "refs/remotes/origin/$BE" --commit-texte "$S" --texte "$P" --config "$CONFIG" 2>&1) || { echo "branche d'entrée non conforme : $(printf '%s' "$VB" | tail -n 1)"; exit 2; }
    COMMIT=$(cle_config "$D/config.json" marqueurs.COMMIT_CODE_T08) && [[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT_CODE_T08 illisible dans la configuration"; exit 2; }
    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/$BC:refs/remotes/origin/$BC" || { echo "branche du code $BC introuvable"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$COMMIT" "refs/remotes/origin/$BC" 2>/dev/null || { echo "commit du code $COMMIT absent de refs/remotes/origin/$BC"; exit 2; }
    git -C "$DEPOT" show "$COMMIT:$A" > "$D/amorce.sh" || { echo "amorce absente du commit du code $COMMIT"; exit 2; }
    E=$(sha256sum "$D/amorce.sh" | cut -d' ' -f1)
    [ "$E" = "$AS" ] && [ "$E" = "$(git -C "$DEPOT" show "$COMMIT:$A.sha256" 2>/dev/null | cut -d' ' -f1)" ] || { echo "empreinte de l'amorce ($E) ≠ T08_AMORCE_SHA256 ($AS) ou son compagnon au commit du code"; exit 2; }
    GOL=$(python3 -I -B -c "$SESSION8" go "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") || { echo "GO : $GOL : pas de création"; exit 2; }   # T08
    printf '%s\n' "$GOL" | tee -a "$D/lancement.txt"
    CAL=$(python3 -I -B -c "$SESSION8" calendrier "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") || { echo "calendrier lu au registre : $CAL : pas de création"; exit 2; }   # T08
    VUE=$(python3 -I -B -c "$SESSION8" vue "$D/config.json" "$D/vue-offre.json") || { echo "bornes de l'offre : $VUE : pas de création"; exit 2; }   # T08
    PLC=$(cle_config "$D/config.json" lancement.plafond_usd) && CRU=$(cle_config "$D/config.json" lancement.compte_rendu_usd) || { echo "plafond ou compte rendu illisibles"; exit 2; }   # T08
    [ -n "${HF_TOKEN:-}" ] && JGHN=$(jeton_gh_nom) || { echo "jeton absent (HF_TOKEN, ou CONTROLE_IA_GITHUB_TOKEN / CONTROLE_IA_GITHUB_TOKEN_2) : pas de création"; exit 2; }
    printf 'controles t08 v1 %s\ncommit_texte %s\ncommit %s\nprereg %s\nconfig %s\nbranche %s\nbranche_entree %s\nentree %s\nbranche_code %s\namorce %s\ngo %s\nplafond %s\ncompte_rendu %s\nmode reel\ncalendrier %s\n' "$(date -u +%FT%TZ)" "$S" "$COMMIT" "$P" "$CONFIG" "$BRANCHE" "$BE" "$EC" "$BC" "$E" "$GO_ID_ENV" "$PLC" "$CRU" "$CAL" >> "$D/lancement.txt"   # T08
    echo "CONTRÔLES CONFORMES : texte S=$S ; code $COMMIT ; entrée $EC ; amorce t08 v1 $E ; $GOL ; $CAL" ;;
controles-epreuve)
    echo "controles-epreuve : non offerte pour T0.8 (aucune épreuve à blanc n'est prévue par l'ordre de course) : rien vérifié, rien créé"; exit 2 ;;   # T08
