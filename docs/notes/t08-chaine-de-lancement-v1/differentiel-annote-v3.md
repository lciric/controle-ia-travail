# Différentiel annoté de la chaîne de lancement de T0.8 — v3

Engendré par `scripts/differentiel_annote_t08_v1.py`. Chaque ligne retirée (−, numéro dans le modèle) ou ajoutée (+, numéro dans la copie) porte la raison de son bloc. Lignes tronquées à 200 caractères ; le fichier entier fait foi.

## `scripts/lancer_t08_v1.sh` (`acfe5a757a626f6f254527d7f0009e2af43b5b95833c7fd1cbe68f2f9bf7b03c`) contre `scripts/lancer_t06_v13.sh` (`6940a337d5e0c9a736aa7087275c5f6328133b67ed4df1c94535ba06a1965416`)

8 blocs ; 105 lignes retirées, 96 ajoutées.

### Bloc 1 (modèle l. 1, copie l. 1)

**Raison** : § 3.4 : en-tête T0.8 ajouté (changements déclarés, usage) ; le texte de la v13 est conservé en dessous.

| | l. | ligne |
|---|---|---|
| + | 2 | `# [T0.8 v1 (consigne de la chaîne de lancement de T0.8, '722ceb5e…', tenue en v3 '6f52c4db…' ; texte au brouillon 15 '8d68b7a0…', § 3.4) : copie de 'scripts/lancer_t06_v13.sh' sous un nom neuf` |
| + | 3 | `# (R12 : la v13 reste telle quelle), dont rien ne change hors ce que la consigne nomme ; chaque ligne changée porte « T08 » ou est` |
| + | 4 | `# déclarée dans le rapport de la chaîne. Mêmes sous-commandes, mêmes codes de sortie. Changent : (1) les noms ('t08'), la branche` |
| + | 5 | `# de sortie par défaut ('calcul/t08-course-v1'), la branche d'entrée ('entree/t08-course-v1'), la configuration lue sur la branche` |
| + | 6 | `# d'entrée ('prereg/T0.8-configuration-course-v1.json'), le commit du code (marqueur 'COMMIT_CODE_T08' de la configuration, ancêtre` |
| + | 7 | `# de 'T08_BRANCHE_CODE'), l'amorce 'scripts/amorce_instance_t08_v1.sh' citée par son empreinte ('T08_AMORCE_SHA256', celle de` |
| + | 8 | `# l'ordre de course, égale au compagnon au commit du code) ; (2) la ligne de GO, toujours par la variable 'GO_ID', admise par la` |
| + | 9 | `# configuration, lue au registre avec sa fin de validité et son plafond ('lancement_t08.session_v1 go' : prolongation comprise) ;` |
| + | 10 | `# plafond de la course 120 USD cumulés sur toutes les tentatives (dépense antérieure relevée au registre des dépenses), compte` |
| + | 11 | `# rendu à 40 USD (alerte unique de la surveillance) ; (3) les bornes de l'offre, celles de « Machine » (vue 'vue-offre.json' tirée` |
| + | 12 | `# de la configuration) ; (4) aucune relance sur une carte H200 : la carte 'relance' est refusée (code 2), ni automatique ni` |
| + | 13 | `# proposée ; (5) aucun couperet de temps (inchangé) ; deux heures sans ligne de progression : alerte, sans arrêt (inchangé) ;` |
| + | 14 | `# (6) 'controles-epreuve' refuse (code 2) : aucune épreuve à blanc n'est prévue par l'ordre de course de T0.8 ;` |
| + | 15 | `# '--verifier-go-seulement' vérifie la ligne 'GO_ID' contre la configuration (premier argument : la configuration).` |
| + | 16 | `# Usage T0.8 :` |
| + | 17 | `#   bash scripts/lancer_t08_v1.sh controles DOSSIER_NEUF [JOUR]` |
| + | 18 | `#       Variables : GO_ID, T08_BRANCHE_ENTREE, T08_BRANCHE_CODE, T08_AMORCE_SHA256 ; facultatives : T08_PREREG, T08_CONFIG,` |
| + | 19 | `#       T08_BRANCHE, T08_REGISTRE_GO, T08_DEPOT. Codes : 0 ; 2 tout échec.` |
| + | 20 | `#   bash scripts/lancer_t08_v1.sh creation auto course DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]` |
| + | 21 | `#   bash scripts/lancer_t08_v1.sh apres-creation FICHIER CODE DOSSIER` |
| + | 22 | `#   bash scripts/lancer_t08_v1.sh surveillance ID DOSSIER [FACTURE_USD]` |
| + | 23 | `#   bash scripts/lancer_t08_v1.sh --verifier-go-seulement CONFIG.json [DEPENSE_ANTERIEURE] [JOUR]` |
| + | 24 | `# Texte de la v13 de la course de confirmation (conservé) :]` |

### Bloc 2 (modèle l. 75, copie l. 98)

**Raison** : § 3.4 « les noms … la branche de sortie par défaut, la branche d'entrée, l'amorce citée » ; « la ligne de GO, toujours par la variable GO_ID » : identifiant de la course en dur retiré, lecture de la ligne d'épreuve de T0.6 (plafond_ligne_go) retirée ; module de session de T0.8 (prolongation, calendrier, vue de l'offre, compte rendu) ; programme de vérification de la branche d'entrée.

| | l. | ligne |
|---|---|---|
| − | 78 | `DEPOT="${T06_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"` |
| − | 79 | `P="${T06_PREREG:-prereg/T0.6-organismes-v0-v1.md}"` |
| − | 80 | `A=scripts/amorce_instance_t06_v11.sh` |
| − | 81 | `BRANCHE="${T06_BRANCHE:-calcul/t06-reel-v4}"` |
| − | 82 | `GO_ID_ENV="${GO_ID:-}"              # v13 : identifiant de la ligne de GO de l'ÉPREUVE, reçu de l'environnement (convention de la garde de calcul : GO_ID=GO-AAAA-MM-JJ-NN), vérifié au registre ; relev…` |
| − | 83 | `GO_ID=GO-2026-11-02-28` |
| − | 84 | `REG="${T06_REGISTRE_GO:-$DEPOT/registres/go.md}"   # registre des GO lu par toutes les sous-commandes ; pour une épreuve : celui d'un clone de 'main' (obligatoire)` |
| + | 101 | `DEPOT="${T08_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"                 # T08` |
| + | 102 | `P="${T08_PREREG:-prereg/T0.8-bases-boite-noire-v0-v1.md}"               # T08 : texte scellé de T0.8 (sur main)` |
| + | 103 | `A=scripts/amorce_instance_t08_v1.sh                                     # T08` |
| + | 104 | `BRANCHE="${T08_BRANCHE:-calcul/t08-course-v1}"                          # T08 : branche de sortie` |
| + | 105 | `BE="${T08_BRANCHE_ENTREE:-entree/t08-course-v1}"                        # T08 : branche d'entrée (liste blanche seule, orpheline)` |
| + | 106 | `CONFIG="${T08_CONFIG:-prereg/T0.8-configuration-course-v1.json}"        # T08 : configuration réelle de la course, lue sur la branche d'entrée` |
| + | 107 | `GO_ID_ENV="${GO_ID:-}"              # T08 : identifiant de la ligne de GO de la COURSE, toujours reçu de l'environnement (convention de la garde de calcul : GO_ID=GO-AAAA-MM-JJ-NN), admis par la confi…` |
| + | 108 | `REG="${T08_REGISTRE_GO:-$DEPOT/registres/go.md}"   # T08 : registre des GO lu par toutes les sous-commandes (celui de 'main', qui fait foi)` |
| − | 86 | `# v13 : plafond de la LIGNE du registre du GO d'épreuve, LU dans le registre (ligne présente, type calcul, accordée par Lazar, non échue au jour donné, non révoquée) ; plus aucun identifiant en dur` |
| − | 87 | `plafond_ligne_go() { python3 -I -B -c "$SESSION7" plafond-ligne "$REG" "$1" ${2:+"$2"}; }` |
| − | 88 | `IMAGE="${T06_IMAGE:-python:3.11-bookworm}"` |
| + | 110 | `IMAGE="${T08_IMAGE:-python:3.11-bookworm}"                              # T08 : nom de la variable` |
| + | 115 | `SESSION8="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.lancement_t08 import session_v1; sys.exit(session_v1.main(sys.argv[1:]))"   # T08 : GO et prolongation, calendrier, vue de l'of…` |
| + | 116 | `BRANCHE_PROG="$DEPOT/scripts/construire_branche_entree_t08_v1.py"      # T08 : vérification de la branche d'entrée relevée` |

### Bloc 3 (modèle l. 119, copie l. 143)

**Raison** : § 3.4 : `controles` — texte scellé sur main (S) et son sceau ; branche d'entrée relevée et vérifiée par programme (liste blanche, orpheline, empreintes) ; commit du code = COMMIT_CODE_T08, ancêtre de la branche du code ; amorce citée par son empreinte (ordre de course) et son compagnon ; GO, fin de validité et calendrier lus au registre ; vue de l'offre (bornes de « Machine ») ; plafond 120 et compte rendu 40 consignés. Les huit citations du texte de T0.6 n'ont pas d'équivalent dans le texte de T0.8 (retirées). `controles-epreuve` : refusée, code 2 (aucune épreuve à blanc dans l'ordre de course de T0.8). `creation` : carte `relance` refusée (aucune H200, ni automatique ni proposée) ; branche des épreuves retirée ; GO de l'environnement égal à celui des contrôles ; plafond 120 lu dans la configuration ; calendrier lu au registre ; simulation d'épuisement refusée ; GO revérifié au jour de la création ; bornes lues dans la vue de l'offre ; commande de création portant les variables de la branche d'entrée, du code et du GO, et le nom du lanceur de T0.8. Contre-lecture M-5 : échéance de la machine = heure du plafond restant par défaut, une échéance donnée ne peut que l'avancer (la v13 prenait la fin du GO).

| | l. | ligne |
|---|---|---|
| + | 146 | `    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] \|\| { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN : la ligne de GO de calcul de la course, convention de la garde de calcul) : pas…` |
| + | 147 | `    BC="${T08_BRANCHE_CODE:?T08_BRANCHE_CODE : branche qui porte le commit du code cité par CODE-T08}"; AS="${T08_AMORCE_SHA256:?T08_AMORCE_SHA256 : empreinte de l amorce, celle de l ordre de course}"…` |
| + | 148 | `    [[ "$AS" =~ ^[0-9a-f]{64}$ ]] \|\| { echo "T08_AMORCE_SHA256 : 64 caractères hexadécimaux"; exit 2; }   # T08` |
| − | 123 | `    python3 -I -B -c "$SESSION" go "$REG" "$JOUR" \| tee -a "$D/lancement.txt" \|\| { echo "GO : pas de création"; exit 2; }` |
| − | 129 | `    for motif in "Entropie : \'[0-9]+\'" "Configuration de T0.6 \(empreinte canonique\) : \'[0-9a-f]{64}\'" "Tâches d'évaluation de T0.6 : \'[0-9a-f]{64}\'" \` |
| − | 130 | `                 "Tests attendus : \'[0-9]+\'" "Chemin de la configuration de T0.6 : \'[^\']+\'" "Chemin des tâches d'évaluation de T0.6 : \'[^\']+\'" \` |
| − | 131 | `                 "Chemin des tâches de distillation de T0.6 : \'[^\']+\'" "Chemin des consignes de P3 : \'[^\']+\'"; do` |
| − | 132 | `        n=$(grep -cE "$motif" "$D/prereg-S.md" \|\| true); [ "$n" = 1 ] \|\| { echo "citation « ${motif%% :*} » absente ou en double dans le texte de S ($n)"; exit 2; }` |
| − | 133 | `    done` |
| − | 134 | `    for cle in "Chemin de la configuration de T0.6" "Chemin des tâches d'évaluation de T0.6" "Chemin des tâches de distillation de T0.6" "Chemin des consignes de P3"; do` |
| − | 135 | `        f=$(sed -n "s/.*$cle : \'\\([^\']*\\)\'.*/\\1/p" "$D/prereg-S.md")` |
| − | 136 | `        git -C "$DEPOT" cat-file -e "$S:$f" 2>/dev/null && git -C "$DEPOT" cat-file -e "$S:$f.sha256" 2>/dev/null \|\| { echo "fichier cité $f ou son sceau absent de S"; exit 2; }` |
| − | 137 | `        [ "$(git -C "$DEPOT" show "$S:$f" \| sha256sum \| cut -d' ' -f1)" = "$(git -C "$DEPOT" show "$S:$f.sha256" \| cut -d' ' -f1)" ] \|\| { echo "sceau de $f non conforme à S"; exit 2; }` |
| − | 138 | `        [ "$cle" = "Chemin de la configuration de T0.6" ] && { git -C "$DEPOT" show "$S:$f" > "$D/config.json"; CONFIG_CHEMIN="$f"; }` |
| − | 139 | `    done` |
| − | 140 | `    CAL=$(python3 -I -B -c "$SESSION" calendrier "$D/config.json" "$REG" "$JOUR") \|\| { echo "calendrier de la configuration (L11) : $CAL : pas de création"; exit 2; }` |
| − | 141 | `    git -C "$DEPOT" show "$S:$A" > "$D/amorce.sh" \|\| { echo "amorce v11 absente de S"; exit 2; }` |
| + | 155 | `    [ "$(sha256sum < "$D/prereg-S.md" \| cut -d' ' -f1)" = "$(git -C "$DEPOT" show "$S:$P.sha256" 2>/dev/null \| cut -d' ' -f1)" ] \|\| { echo "sceau de $P non conforme à S"; exit 2; }   # T08` |
| + | 156 | `    # T08 : branche d'entrée relevée (refspec explicite), vérifiée par programme sans la branche de 7b : liste blanche exacte, orpheline, aucun interdit, empreintes` |
| + | 157 | `    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/$BE:refs/remotes/origin/$BE" \|\| { echo "branche d'entrée $BE introuvable"; exit 2; }` |
| + | 158 | `    EC=$(git -C "$DEPOT" rev-parse "refs/remotes/origin/$BE^{commit}") \|\| { echo "branche d'entrée illisible"; exit 2; }` |
| + | 159 | `    git -C "$DEPOT" show "$EC:$CONFIG" > "$D/config.json" 2>/dev/null \|\| { echo "configuration $CONFIG absente de la branche d'entrée"; exit 2; }` |
| + | 160 | `    [ "$(git -C "$DEPOT" rev-parse "$EC:$P")" = "$(git -C "$DEPOT" rev-parse "$S:$P")" ] \|\| { echo "texte de la branche d'entrée ≠ texte scellé de S"; exit 2; }` |
| + | 161 | `    VB=$(python3 -I -B "$BRANCHE_PROG" verifier --depot "$DEPOT" --ref "refs/remotes/origin/$BE" --commit-texte "$S" --texte "$P" --config "$CONFIG" 2>&1) \|\| { echo "branche d'entrée non conforme : …` |
| + | 162 | `    COMMIT=$(cle_config "$D/config.json" marqueurs.COMMIT_CODE_T08) && [[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] \|\| { echo "COMMIT_CODE_T08 illisible dans la configuration"; exit 2; }` |
| + | 163 | `    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/$BC:refs/remotes/origin/$BC" \|\| { echo "branche du code $BC introuvable"; exit 2; }` |
| + | 164 | `    git -C "$DEPOT" merge-base --is-ancestor "$COMMIT" "refs/remotes/origin/$BC" 2>/dev/null \|\| { echo "commit du code $COMMIT absent de refs/remotes/origin/$BC"; exit 2; }` |
| + | 165 | `    git -C "$DEPOT" show "$COMMIT:$A" > "$D/amorce.sh" \|\| { echo "amorce absente du commit du code $COMMIT"; exit 2; }` |
| − | 143 | `    tr '\n' ' ' < "$D/prereg-S.md" \| tr -s ' ' \| grep -qF "\'$A\' (\'$E\'" \|\| { echo "empreinte de l'amorce v11 ($E) non citée par le texte de S"; exit 2; }` |
| + | 167 | `    [ "$E" = "$AS" ] && [ "$E" = "$(git -C "$DEPOT" show "$COMMIT:$A.sha256" 2>/dev/null \| cut -d' ' -f1)" ] \|\| { echo "empreinte de l'amorce ($E) ≠ T08_AMORCE_SHA256 ($AS) ou son compagnon au comm…` |
| + | 168 | `    GOL=$(python3 -I -B -c "$SESSION8" go "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") \|\| { echo "GO : $GOL : pas de création"; exit 2; }   # T08` |
| + | 169 | `    printf '%s\n' "$GOL" \| tee -a "$D/lancement.txt"` |
| + | 170 | `    CAL=$(python3 -I -B -c "$SESSION8" calendrier "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") \|\| { echo "calendrier lu au registre : $CAL : pas de création"; exit 2; }   # T08` |
| + | 171 | `    VUE=$(python3 -I -B -c "$SESSION8" vue "$D/config.json" "$D/vue-offre.json") \|\| { echo "bornes de l'offre : $VUE : pas de création"; exit 2; }   # T08` |
| + | 172 | `    PLC=$(cle_config "$D/config.json" lancement.plafond_usd) && CRU=$(cle_config "$D/config.json" lancement.compte_rendu_usd) \|\| { echo "plafond ou compte rendu illisibles"; exit 2; }   # T08` |
| − | 145 | `    printf 'controles t06 v13 %s\ncommit %s\nprereg %s\nconfig %s\nbranche %s\namorce %s\ngo %s\ncalendrier %s\n' "$(date -u +%FT%TZ)" "$S" "$P" "$CONFIG_CHEMIN" "$BRANCHE" "$E" "$GO_ID" "$CAL" >> "$D…` |
| − | 146 | `    echo "CONTRÔLES CONFORMES : S=$S ; amorce v11 $E ; GO $GO_ID ; $CAL" ;;` |
| + | 174 | `    printf 'controles t08 v1 %s\ncommit_texte %s\ncommit %s\nprereg %s\nconfig %s\nbranche %s\nbranche_entree %s\nentree %s\nbranche_code %s\namorce %s\ngo %s\nplafond %s\ncompte_rendu %s\nmode reel\n…` |
| + | 175 | `    echo "CONTRÔLES CONFORMES : texte S=$S ; code $COMMIT ; entrée $EC ; amorce t08 v1 $E ; $GOL ; $CAL" ;;` |
| − | 148 | `    D=$(realpath -m "${2:?dossier neuf}"); S="${3:?commit à cloner (40 caractères)}"; CFG="${4:?chemin de la configuration de l epreuve dans le commit}"; JOUR="${5:-$(date -u +%F)}"` |
| − | 149 | `    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }` |
| − | 150 | `    [[ "$S" =~ ^[0-9a-f]{40}$ ]] \|\| { echo "commit : 40 caractères hexadécimaux"; exit 2; }` |
| − | 151 | `    BC="${T06_BRANCHE_CODE:?T06_BRANCHE_CODE : branche prep/… du code}"` |
| − | 152 | `    [ -n "${T06_REGISTRE_GO:-}" ] && [ -f "$T06_REGISTRE_GO" ] \|\| { echo "T06_REGISTRE_GO : registres/go.md d'un clone de main exigé pour une épreuve (le registre du commit du code peut être antérie…` |
| − | 153 | `    case "$BC" in prep/*) ;; *) echo "T06_BRANCHE_CODE doit commencer par prep/ ($BC)"; exit 2;; esac` |
| − | 154 | `    mkdir -p "$D"` |
| − | 155 | `    git -C "$DEPOT" cat-file -e "$S^{commit}" 2>/dev/null \|\| { echo "commit $S absent du dépôt local (git fetch origin refs/heads/$BC:refs/remotes/origin/$BC d'abord)"; exit 2; }` |
| − | 156 | `    git -C "$DEPOT" merge-base --is-ancestor "$S" "refs/remotes/origin/$BC" 2>/dev/null \|\| { echo "commit $S absent de refs/remotes/origin/$BC (fetch par refspec explicite d'abord)"; exit 2; }` |
| − | 157 | `    git -C "$DEPOT" show "$S:$CFG" > "$D/config.json" 2>/dev/null \|\| { echo "configuration $CFG absente du commit $S"; exit 2; }` |
| − | 158 | `    GOC=$(cle_config "$D/config.json" go_id) && PLC=$(cle_config "$D/config.json" plafond_usd) && MODE_C=$(cle_config "$D/config.json" mode) \|\| { echo "go_id, plafond_usd ou mode illisibles"; exit 2…` |
| − | 159 | `    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] \|\| { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN : la ligne de GO de calcul de l'épreuve, convention de la garde de calcul) : pas…` |
| − | 160 | `    [ "$GOC" = "$GO_ID_ENV" ] \|\| { echo "go_id de la configuration ($GOC) ≠ GO_ID de l'environnement ($GO_ID_ENV) : pas de création"; exit 2; }` |
| − | 161 | `    [ "$GOC" != "$GO_ID" ] \|\| { echo "go_id de la configuration ($GOC) est le GO de la course : cette sous-commande ne sert que les épreuves à blanc, sous leur propre ligne de GO de calcul"; exit 2;…` |
| − | 162 | `    PGL=$(plafond_ligne_go "$GOC" "$JOUR") \|\| { echo "ligne de GO $GOC du registre $REG non conforme ($PGL) : pas de création"; exit 2; }` |
| − | 163 | `    # R-1696 : plafond d'épreuve lu dans la configuration, borné par le reste du GO (plus de liste fermée) ; dépense réelle et finale des autres épreuves donnée explicitement` |
| − | 164 | `    ANT_EPR="${T06_DEPENSE_EPREUVES_ANTERIEURES_USD:-}"; [[ "$ANT_EPR" =~ ^[0-9]+([.][0-9]+)?$ ]] \|\| { echo "T06_DEPENSE_EPREUVES_ANTERIEURES_USD : dépense réelle et finale des autres épreuves du GO…` |
| − | 165 | `    PLAF=$(python3 -I -B -c "$SESSION7" plafond "$PLC" "$ANT_EPR" "$GOC" "$REG" "$JOUR") \|\| { echo "plafond_usd $PLC refusé : $PLAF"; exit 2; }` |
| − | 166 | `    case "$MODE_C" in jouet\|reel) ;; *) echo "mode $MODE_C illisible"; exit 2;; esac` |
| − | 167 | `    python3 -I -B -c "$SESSION3" go "$REG" "$GOC" "$PGL" "$JOUR" \| tee -a "$D/lancement.txt" \|\| { echo "GO : pas de création"; exit 2; }` |
| − | 168 | `    # l'amorce relit le registre DU COMMIT cloné : le GO doit y figurer aussi (sinon elle refuserait sur l'instance)` |
| − | 169 | `    git -C "$DEPOT" show "$S:registres/go.md" > "$D/go-commit.md" 2>/dev/null && python3 -I -B -c "$SESSION3" go "$D/go-commit.md" "$GOC" "$PGL" "$JOUR" >/dev/null \|\| { echo "GO $GOC absent ou non c…` |
| − | 170 | `    LIBRE=$(df -Pk "$D" \| awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] \|\| { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 2; }` |
| − | 171 | `    CAL=$(python3 -I -B -c "$SESSION3" calendrier "$D/config.json" "$REG" "$GOC" "$PGL" "$JOUR") \|\| { echo "calendrier de la configuration : $CAL : pas de création"; exit 2; }` |
| − | 172 | `    git -C "$DEPOT" show "$S:$A" > "$D/amorce.sh" \|\| { echo "amorce v11 absente de $S"; exit 2; }` |
| − | 173 | `    E=$(sha256sum "$D/amorce.sh" \| cut -d' ' -f1)` |
| − | 174 | `    if [ "$MODE_C" = reel ]; then [ -n "${HF_TOKEN:-}" ] \|\| { echo "HF_TOKEN absent (mode réel) : pas de création"; exit 2; }; fi` |
| − | 175 | `    JGHN=$(jeton_gh_nom) \|\| { echo "jeton absent (ni CONTROLE_IA_GITHUB_TOKEN ni CONTROLE_IA_GITHUB_TOKEN_2) : pas de création"; exit 2; }` |
| − | 176 | `    printf 'controles-epreuve t06 v4 %s\ncommit %s\nprereg -\nconfig %s\nbranche %s\namorce %s\ngo %s\nplafond %s\nepreuves_anterieures %s\nmode %s\nepreuve oui\ncalendrier %s\n' "$(date -u +%FT%TZ)" …` |
| − | 177 | `    echo "CONTRÔLES D'ÉPREUVE CONFORMES : S=$S ; amorce v11 $E ; GO $GOC (plafond de l'épreuve $PLC USD sur $PGL, plafond de la ligne du registre ; $PLAF) ; mode $MODE_C ; $CAL" ;;` |
| + | 177 | `    echo "controles-epreuve : non offerte pour T0.8 (aucune épreuve à blanc n'est prévue par l'ordre de course) : rien vérifié, rien créé"; exit 2 ;;   # T08` |
| − | 179 | `    OFFRE_ARG="${2:?auto}"; CARTE="${3:?carte : course ou relance}"; ANT="${4:?dépense antérieure en USD (registre des dépenses ; 0 pour la première tentative)}"; D=$(realpath -m "${5:?dossier des con…` |
| + | 179 | `    OFFRE_ARG="${2:?auto}"; CARTE="${3:?carte : course}"; ANT="${4:?dépense antérieure en USD (registre des dépenses ; 0 pour la première tentative)}"; D=$(realpath -m "${5:?dossier des contrôles}"); …` |
| − | 181 | `    case "$CARTE" in course\|relance) ;; *) echo "carte : course ou relance (DT-6)"; exit 2;; esac` |
| + | 181 | `    case "$CARTE" in course) ;; relance) echo "carte « relance » : aucune relance sur une carte H200, ni automatique ni proposée (section « Machine » du texte de T0.8 ; mot de Lazar exigé) : pas de cr…` |
| − | 184 | `    S=$(champ commit "$D/lancement.txt"); [[ "$S" =~ ^[0-9a-f]{40}$ ]] \|\| { echo "commit illisible"; exit 2; }` |
| − | 185 | `    EPR=non; [ "$(champ epreuve "$D/lancement.txt")" = oui ] && EPR=oui` |
| − | 186 | `    GOC=$(cle_config "$D/config.json" go_id) && PLC=$(cle_config "$D/config.json" plafond_usd) && MODE_C=$(cle_config "$D/config.json" mode) \|\| { echo "go_id, plafond_usd ou mode illisibles"; exit 2…` |
| − | 187 | `    if [ "$EPR" = oui ]; then` |
| − | 188 | `        [ -n "${T06_REGISTRE_GO:-}" ] \|\| { echo "épreuve : T06_REGISTRE_GO (registres/go.md d'un clone de main) exigé"; exit 2; }` |
| − | 189 | `        [ "$GOC" = "$GO_ID_ENV" ] \|\| { echo "épreuve : go_id de la configuration ($GOC) ≠ GO_ID de l'environnement (${GO_ID_ENV:-absent}) : pas de création"; exit 2; }` |
| − | 190 | `        PGL=$(plafond_ligne_go "$GOC") \|\| { echo "épreuve : ligne de GO $GOC non conforme au jour de la création ($PGL) : pas de création"; exit 2; }` |
| − | 191 | `        [ "$(champ go "$D/lancement.txt")" = "$GOC" ] && [ "$(champ plafond "$D/lancement.txt")" = "$PLC" ] \|\| { echo "épreuve : GO ou plafond de la configuration ≠ ceux des contrôles"; exit 2; }` |
| − | 192 | `        case "$BRANCHE" in essai/*) ;; *) echo "épreuve : la branche poussée doit commencer par essai/ ($BRANCHE) : jamais calcul/"; exit 2;; esac` |
| − | 193 | `        PGO=$PGL` |
| − | 194 | `        PLAF=$(python3 -I -B -c "$SESSION7" plafond "$PLC" "$(champ epreuves_anterieures "$D/lancement.txt")" "$GOC" "$REG") \|\| { echo "épreuve : plafond $PLC hors du reste du GO : $PLAF"; exit 2; }` |
| − | 195 | `    else` |
| − | 196 | `        [ "$S" = "$(commit_s)" ] \|\| { echo "commit de scellement changé depuis les contrôles"; exit 2; }` |
| − | 197 | `        [ "$GOC" = "$GO_ID" ] && [ "$PLC" = 200 ] \|\| { echo "course : GO ($GOC) ou plafond ($PLC) de la configuration ≠ $GO_ID, 200"; exit 2; }` |
| − | 198 | `        [ -z "${T06_EPUISEMENT_SIMULE_S:-}" ] \|\| { echo "T06_EPUISEMENT_SIMULE_S : réservé aux épreuves à blanc"; exit 2; }` |
| − | 199 | `        PGO=200` |
| − | 200 | `    fi` |
| − | 201 | `    CAL=$(python3 -I -B -c "$SESSION3" calendrier "$D/config.json" "$REG" "$GOC" "$PGO") \|\| { echo "calendrier (L11) au jour de la création : $CAL : nœud, pas de création"; exit 3; }` |
| − | 202 | `    FIN_GO=$(printf '%s\n' "$CAL" \| sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p'); [ -n "$ECH" ] \|\| ECH="$FIN_GO"` |
| − | 203 | `    [[ "$ECH" =~ ^[0-9]+$ ]] && [ "$ECH" -le "$FIN_GO" ] && [ "$ECH" -gt "$(date +%s)" ] \|\| { echo "échéance $ECH hors de ]maintenant, fin du GO $FIN_GO]"; exit 2; }` |
| − | 204 | `    python3 -I -B -c "$SESSION3" go "$REG" "$GOC" "$PGO" >/dev/null \|\| { echo "GO non conforme au jour de la création"; exit 2; }` |
| + | 184 | `    S=$(champ commit_texte "$D/lancement.txt"); [[ "$S" =~ ^[0-9a-f]{40}$ ]] \|\| { echo "commit du texte illisible"; exit 2; }   # T08` |
| + | 185 | `    COMMIT=$(champ commit "$D/lancement.txt"); [[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] \|\| { echo "commit du code illisible"; exit 2; }   # T08` |
| + | 186 | `    [ "$S" = "$(commit_s)" ] \|\| { echo "commit de scellement changé depuis les contrôles"; exit 2; }` |
| + | 187 | `    [ "$(cle_config "$D/config.json" marqueurs.COMMIT_CODE_T08)" = "$COMMIT" ] \|\| { echo "commit du code de la configuration ≠ celui des contrôles"; exit 2; }   # T08` |
| + | 188 | `    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] && [ "$GO_ID_ENV" = "$(champ go "$D/lancement.txt")" ] \|\| { echo "GO_ID de l'environnement (${GO_ID_ENV:-absent}) ≠ GO des contrôles ($(champ go "$D/lancement.txt…` |
| + | 189 | `    PLC=$(cle_config "$D/config.json" lancement.plafond_usd) && [ "$PLC" = "$(champ plafond "$D/lancement.txt")" ] && [ "$PLC" = 120 ] \|\| { echo "plafond de la configuration ($PLC) ≠ plafond des con…` |
| + | 190 | `    MODE_C=reel   # T08 : la course de T0.8 n'a qu'un mode sur la machine (aucune épreuve à blanc)` |
| + | 191 | `    [ -z "${T08_EPUISEMENT_SIMULE_S:-}" ] \|\| { echo "T08_EPUISEMENT_SIMULE_S : aucune épreuve à blanc pour T0.8"; exit 2; }   # T08` |
| + | 192 | `    CAL=$(python3 -I -B -c "$SESSION8" calendrier "$REG" "$D/config.json" "$GO_ID_ENV") \|\| { echo "calendrier lu au registre au jour de la création : $CAL : nœud, pas de création"; exit 3; }   # T08` |
| + | 193 | `    FIN_GO=$(printf '%s\n' "$CAL" \| sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p'); [[ "$FIN_GO" =~ ^[0-9]+$ ]] \|\| { echo "fin du GO illisible"; exit 2; }   # T08 : l'échéance de la machine est borné…` |
| + | 194 | `    python3 -I -B -c "$SESSION8" go "$REG" "$D/config.json" "$GO_ID_ENV" >/dev/null \|\| { echo "GO non conforme au jour de la création"; exit 2; }   # T08` |
| − | 207 | `    DISQUE=$(cle_config "$D/config.json" offre.disque_min_go) \|\| { echo "disque illisible"; exit 2; }` |
| + | 197 | `    DISQUE=$(cle_config "$D/vue-offre.json" offre.disque_min_go) \|\| { echo "disque illisible"; exit 2; }   # T08 : vue de l'offre` |
| − | 214 | `    FILTRE=$(python3 -I -B -c "$SESSION7" filtre "$D/config.json" "$CARTE") \|\| { echo "filtre illisible : $FILTRE"; exit 2; }` |
| + | 204 | `    FILTRE=$(python3 -I -B -c "$SESSION7" filtre "$D/vue-offre.json" "$CARTE") \|\| { echo "filtre illisible : $FILTRE"; exit 2; }   # T08 : vue de l'offre` |
| − | 216 | `    OF=$(python3 -I -B -c "$SESSION7" choisir "$D/offres.json" "$D/config.json" "$CARTE" "$EXCL") \|\| { echo "aucune offre conforme dans la liste filtrée : $OF : nœud, pas de création"; exit 3; }` |
| + | 206 | `    OF=$(python3 -I -B -c "$SESSION7" choisir "$D/offres.json" "$D/vue-offre.json" "$CARTE" "$EXCL") \|\| { echo "aucune offre conforme dans la liste filtrée : $OF : nœud, pas de création"; exit 3; } …` |
| − | 222 | `    ETIQ=$(cle_config "$D/config.json" offre.etiquette) \|\| { echo "étiquette illisible"; exit 2; }` |
| + | 212 | `    ETIQ=$(cle_config "$D/vue-offre.json" offre.etiquette) \|\| { echo "étiquette illisible"; exit 2; }   # T08 : vue de l'offre` |
| − | 226 | `    DEP=$(python3 -I -B -c "$SESSION3" depense "$PLC" "$PC" "$PS" "$NOW" "$ANT" "$TEL" "$NOW" ${T06_EPUISEMENT_SIMULE_S:+- "$T06_EPUISEMENT_SIMULE_S"}); code_dep=$?` |
| + | 216 | `    DEP=$(python3 -I -B -c "$SESSION3" depense "$PLC" "$PC" "$PS" "$NOW" "$ANT" "$TEL" "$NOW"); code_dep=$?   # T08 : aucune simulation d'épuisement` |
| + | 219 | `    # T08 (M-5) : échéance de la machine = heure du plafond restant (par défaut) ; une échéance donnée ne peut que l'avancer` |
| + | 220 | `    [ -n "$ECH" ] \|\| ECH="$EPUIS"` |
| + | 221 | `    [[ "$ECH" =~ ^[0-9]+$ ]] && [ "$ECH" -le "$EPUIS" ] && [ "$ECH" -gt "$(date +%s)" ] \|\| { echo "échéance $ECH hors de ]maintenant, heure du plafond restant $EPUIS]"; exit 2; }` |
| − | 231 | `    EXTRA=""` |
| − | 232 | `    [[ "${T06_TESTS_ATTENDUS:-}" =~ ^[0-9]*$ ]] \|\| { echo "T06_TESTS_ATTENDUS illisible (^[0-9]*$ exigé : un entier ou rien) : pas de création"; exit 2; }` |
| − | 233 | `    [ "$EPR" != oui ] \|\| [ -z "${T06_TESTS_ARGS:-}" ] \|\| [ "$MODE_C" = jouet ] \|\| { echo "T06_TESTS_ARGS refusé en mode $MODE_C : la suite ciblée figée de l'amorce est la seule jouée hors de la …` |
| − | 234 | `    [ "$EPR" = oui ] && EXTRA=" -e EPREUVE_GO_ID=$GOC -e MODE=$MODE_C -e PREREG_ABSENT=1 -e CONFIG=$(champ config "$D/lancement.txt") -e TESTS_ATTENDUS=${T06_TESTS_ATTENDUS:-}${T06_TESTS_ARGS:+ -e TES…` |
| − | 235 | `    CMD="GO_ID=$GOC timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT=$S -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL…` |
| + | 224 | `    CMD="GO_ID=$GO_ID_ENV timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT=$COMMIT -e PREREG=$P -e CONFIG=$(champ con…` |

### Bloc 4 (modèle l. 246, copie l. 235)

**Raison** : § 3.4 « les noms » : le lanceur cité dans les messages d'après la création est celui de T0.8. Contre-lecture M-2 : l'étiquette du chemin « offre refusée » est lue dans la vue de l'offre.

| | l. | ligne |
|---|---|---|
| − | 249 | `        echo "CRÉÉE : instance $ID (création $CR ; sortie de vastai non affichée) ; surveillance : bash scripts/lancer_t06_v13.sh surveillance $ID $D"; exit 0` |
| + | 238 | `        echo "CRÉÉE : instance $ID (création $CR ; sortie de vastai non affichée) ; surveillance : bash scripts/lancer_t08_v1.sh surveillance $ID $D"; exit 0` |
| − | 253 | `        ETIQ=$(cle_config "$D/config.json" offre.etiquette) \|\| { echo "étiquette illisible"; exit 4; }` |
| + | 242 | `        ETIQ=$(cle_config "$D/vue-offre.json" offre.etiquette) \|\| { echo "étiquette illisible"; exit 4; }   # T08 (M-2) : vue de l'offre` |
| − | 256 | `            echo "OFFRE REFUSÉE À LA CRÉATION (retirée ?) : aucune instance du programme ; machine $(champ machine_proposee "$D/lancement.txt") exclue ; rang suivant : bash $DEPOT/scripts/lancer_t06_v…` |
| + | 245 | `            echo "OFFRE REFUSÉE À LA CRÉATION (retirée ?) : aucune instance du programme ; machine $(champ machine_proposee "$D/lancement.txt") exclue ; rang suivant : bash $DEPOT/scripts/lancer_t08_v…` |

### Bloc 5 (modèle l. 264, copie l. 253)

**Raison** : § 3.4 : plafond de la surveillance lu dans lancement.txt, 120 exigé, sans valeur par défaut (la v13 prenait 200) ; seuil du compte rendu (40 USD) relu.

| | l. | ligne |
|---|---|---|
| − | 267 | `    PLC=$(champ plafond_creation "$D/lancement.txt"); [ -n "$PLC" ] \|\| PLC=200               # C-V4-3 : plafond de la configuration (200 pour la course)` |
| + | 256 | `    PLC=$(champ plafond_creation "$D/lancement.txt"); [ "$PLC" = 120 ] \|\| { echo "plafond de la création illisible ou ≠ 120 USD dans lancement.txt"; exit 2; }   # T08 : plafond cumulé de la course, …` |
| + | 257 | `    CRU=$(champ compte_rendu "$D/lancement.txt"); [[ "$CRU" =~ ^[0-9]+$ ]] \|\| { echo "seuil du compte rendu illisible dans lancement.txt"; exit 2; }   # T08 : compte rendu à 40 USD` |

### Bloc 6 (modèle l. 294, copie l. 284)

**Raison** : § 3.4 « les noms » : ligne d'en-tête de la surveillance ; alerte unique du compte rendu déclarée.

| | l. | ligne |
|---|---|---|
| − | 297 | `    echo "surveillance v13 de $ID : création $CR, carte $PC USD/h, stockage $PS USD/h, téléchargement $TEL USD, antérieur $ANT USD ; sans couperet de temps ; arrêt sur processus mort ou dépense cumulé…` |
| + | 287 | `    echo "surveillance t08 v1 de $ID : création $CR, carte $PC USD/h, stockage $PS USD/h, téléchargement $TEL USD, antérieur $ANT USD ; sans couperet de temps ; arrêt sur processus mort ou dépense cum…` |

### Bloc 7 (modèle l. 334, copie l. 324)

**Raison** : § 3.4 « compte rendu à 40 USD » : la décision vient du module de session de T0.8 (celle de la v3 plus l'alerte du compte rendu) ; deux heures sans progression : alerte sans arrêt, inchangé. Contre-lecture M-3 : la ligne « FIN » imprime la destruction par l'identifiant, non plus l'arrêt qui garde le disque.

| | l. | ligne |
|---|---|---|
| − | 337 | `        if DEC=$(python3 -I -B -c "$SESSION3" surveillance "$PLC" "$D/progres.txt" "$now" "$PC" "$PS" "$CR" "$ANT" "$TEL" ${FACT:+"$FACT"} 2>&1); then ILLISIBLES=0` |
| + | 327 | `        if DEC=$(python3 -I -B -c "$SESSION8" surveillance "$PLC" "$CRU" "$D/progres.txt" "$now" "$PC" "$PS" "$CR" "$ANT" "$TEL" ${FACT:+"$FACT"} 2>&1); then ILLISIBLES=0   # T08 : compte rendu à 40 U…` |

### Bloc 8 (modèle l. 343, copie l. 333)

**Raison** : § 3.4 « compte rendu à 40 USD » : l'alerte n'est écrite qu'une fois (fichier compte-rendu-alerte.txt) ; `--verifier-go-seulement` : vérifie la ligne GO_ID contre la configuration (prolongation, plafond), plus la ligne d'épreuve de T0.6 (premier argument : la configuration, non un plafond d'épreuve).

| | l. | ligne |
|---|---|---|
| − | 346 | `            FIN*) echo "$DEC"; echo "FIN : instance à arrêter par son identifiant, disque gardé jusqu'au verdict : timeout -k 5 120 $VAST stop instance $ID"; exit 0 ;;` |
| + | 336 | `            FIN*) echo "$DEC"; echo "FIN : l'amorce détruit la machine après le versement prouvé (M-3, « Devis » : aucune garde de 72 heures) ; vérifier la poussée (ordre, étape 9), puis l'inventaire …` |
| + | 338 | `            "ALERTE compte rendu"*) if [ ! -e "$D/compte-rendu-alerte.txt" ]; then echo "$(date -u +%FT%TZ) $DEC" \| tee "$D/compte-rendu-alerte.txt"; fi ;;   # T08 : une seule fois` |
| − | 353 | `    # v13 : vérification seule de la ligne de GO de l'épreuve (GO_ID de l'environnement, registre T06_REGISTRE_GO) et du plafond demandé ; NE CRÉE RIEN (aucun dossier, aucun fichier, aucun appel à l'o…` |
| − | 354 | `    PLC="${2:?plafond demandé pour l épreuve, en USD}"; ANT_EPR="${3:-0}"; JOUR="${4:-$(date -u +%F)}"` |
| + | 344 | `    # T08 : vérification seule de la ligne de GO de la course (GO_ID de l'environnement, admise par la configuration donnée, lue au registre avec sa prolongation, son plafond et sa fin de validité) et…` |
| + | 345 | `    CFG="${2:?configuration de la course (fichier JSON)}"; ANT_EPR="${3:-0}"; JOUR="${4:-$(date -u +%F)}"` |
| − | 356 | `    [ -n "${T06_REGISTRE_GO:-}" ] && [ -f "$T06_REGISTRE_GO" ] \|\| { echo "T06_REGISTRE_GO : registres/go.md d'un clone de main exigé : rien vérifié, rien créé"; exit 2; }` |
| − | 357 | `    [ "$GO_ID_ENV" != "$GO_ID" ] \|\| { echo "GO_ID=$GO_ID_ENV est le GO de la course : une épreuve se joue sous sa propre ligne de GO de calcul : refus"; exit 2; }` |
| − | 358 | `    [[ "$PLC" =~ ^[0-9]+([.][0-9]+)?$ ]] && [[ "$ANT_EPR" =~ ^[0-9]+([.][0-9]+)?$ ]] \|\| { echo "plafond ($PLC) ou dépense antérieure ($ANT_EPR) : nombre positif en USD attendu : refus"; exit 2; }` |
| − | 359 | `    GOL=$(python3 -I -B -c "$SESSION7" go-ligne "$REG" "$GO_ID_ENV" "$JOUR") \|\| { echo "GO $GO_ID_ENV refusé : $GOL"; exit 2; }` |
| − | 360 | `    PLAF=$(python3 -I -B -c "$SESSION7" plafond "$PLC" "$ANT_EPR" "$GO_ID_ENV" "$REG" "$JOUR") \|\| { echo "plafond $PLC refusé : $PLAF"; exit 2; }` |
| − | 361 | `    echo "GO VÉRIFIÉ, RIEN CRÉÉ : $GOL ; $PLAF" ;;` |
| + | 347 | `    [ -f "$CFG" ] && [ -f "$REG" ] \|\| { echo "configuration $CFG ou registre $REG absent : rien vérifié, rien créé"; exit 2; }` |
| + | 348 | `    [[ "$ANT_EPR" =~ ^[0-9]+([.][0-9]+)?$ ]] \|\| { echo "dépense antérieure ($ANT_EPR) : nombre positif en USD attendu : refus"; exit 2; }` |
| + | 349 | `    GOL=$(python3 -I -B -c "$SESSION8" go "$REG" "$CFG" "$GO_ID_ENV" "$JOUR") \|\| { echo "GO $GO_ID_ENV refusé : $GOL"; exit 2; }` |
| + | 350 | `    PLC=$(cle_config "$CFG" lancement.plafond_usd) \|\| { echo "plafond illisible : refus"; exit 2; }` |
| + | 351 | `    python3 -I -c 'import sys; from decimal import Decimal as D; sys.exit(0 if D(sys.argv[1]) < D(sys.argv[2]) else 1)' "$ANT_EPR" "$PLC" \|\| { echo "dépense antérieure $ANT_EPR ≥ plafond $PLC USD : …` |
| + | 352 | `    echo "GO VÉRIFIÉ, RIEN CRÉÉ : $GOL ; dépense antérieure $ANT_EPR < plafond $PLC USD" ;;` |

## `scripts/amorce_instance_t08_v1.sh` (`7572f9128e87a27fd2dd9e205a8590b77455ebe509853d458f06767f497b9611`) contre `scripts/amorce_instance_t06_v11.sh` (`43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859`)

13 blocs ; 200 lignes retirées, 237 ajoutées.

### Bloc 1 (modèle l. 1, copie l. 1)

**Raison** : § 3.5 : en-tête T0.8 ajouté (changements déclarés) ; le texte de la v11 est conservé en dessous.

| | l. | ligne |
|---|---|---|
| + | 2 | `# [T0.8 v1 (consigne de la chaîne de lancement de T0.8, '722ceb5e…', tenue en v3 '6f52c4db…' ; texte au brouillon 15 '8d68b7a0…', § 3.5) : copie de 'scripts/amorce_instance_t06_v11.sh' sous un nom` |
| + | 3 | `# neuf (R12 : la v11 reste telle quelle), dont rien ne change hors ce que la consigne nomme ; chaque ligne changée porte « T08 » ou est` |
| + | 4 | `# déclarée dans le rapport de la chaîne. Changent : (1) les noms ('t08' : fichiers de travail '$R/t08-…', lignes « AMORCE T08 ») ;` |
| + | 5 | `# (2) le clonage : le code au commit 'COMMIT' (celui de 'COMMIT_CODE_T08'), une seule branche ('BRANCHE_CODE', sans étiquettes),` |
| + | 6 | `# extraction limitée à ce que la course et ses essais importent (12 motifs, 'CHEMINS_CLONAGE'), puis la branche d'entrée seule` |
| + | 7 | `# ('BRANCHE_ENTREE' au commit 'ENTREE_COMMIT', refspec explicite), dont les fichiers sont recopiés à l'octet à leurs chemins et` |
| + | 8 | `# portés par le commit local de la course (consigne v3, § 3.5 : seul parent 'COMMIT', liste attendue écrite avant, rien de gelé,` |
| + | 9 | `# auteur et date fixés ; la branche de sortie part de lui) ; jamais la branche de sortie de 7b ; (3) avant tout` |
| + | 10 | `# calcul : aucun 'lecture-sondes-t06*' ni 'resume.json' sur le disque (dès le clonage), puis, l'environnement installé,` |
| + | 11 | `# 'entrees_v1.exiger_instance_sans_interdits', tête égale à 'COMMIT' et à 'COMMIT_CODE_T08' de la configuration, texte scellé` |
| + | 12 | `# intact et portant les marqueurs de la configuration ; l'environnement Python est hors du dépôt ('$R/venv-t08'), que la garde` |
| + | 13 | `# parcourt ; (4) la liste d'essais ciblée et figée de T0.8 ('scripts/tests-cibles-t08-v1.txt', empreinte et nombre attendu écrits` |
| + | 14 | `# en dur) ; (5) les modèles Llama-3.1-8B-Instruct et Llama-3.2-3B-Instruct aux révisions de la configuration, préchargés l'un après` |
| + | 15 | `# l'autre au cache local (la course les charge hors ligne) ; (6) la commande jouée : 'python -m controle_ia.t08.course_v1 --config …` |
| + | 16 | `# --run-id … --prereg …', une fois ; (7) la minuterie : montants de T0.8 (120 USD) ; à l'heure du plafond restant, consignation puis **destruction** (contre-lecture M-3 : le texte le veut ; la v11 env…` |
| + | 17 | `# la course ('runs/<run>', 'diag/<run>', 'donnees/<run>/*-t08.*') scellées et poussées sur la branche de sortie, marqueur de fin` |
| + | 18 | `# normale seulement si rien ne reste à pousser ; retirés : le bras B de l'audit de fuite, les morceaux d'activations, les épreuves` |
| + | 19 | `# à blanc ('EPREUVE_GO_ID' refusé). Le GO de la course vient de 'GO_ID_T08' (lancé par le lanceur avec 'GO_ID'), lu au registre du` |
| + | 20 | `# commit par 'lancement_t08.session_v1 go' (prolongation comprise). Texte de la v11 de la course de confirmation (conservé) :]` |

### Bloc 2 (modèle l. 57, copie l. 76)

**Raison** : § 3.5 « les noms » ; GO de la course reçu du lanceur (GO_ID_T08), jamais en dur.

| | l. | ligne |
|---|---|---|
| − | 60 | `GO_ID=GO-2026-11-02-28` |
| + | 79 | `GO_ID="${GO_ID_T08:-}"   # T08 : ligne de GO de la course, reçue du lanceur (jamais en dur), vérifiée au registre du commit` |
| − | 64 | `cd "$R" \|\| { echo "AMORCE T06 : racine $R inaccessible : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }` |
| − | 65 | `N_DEM=0; [ -s "$R/t06-demarrages.txt" ] && read -r N_DEM < "$R/t06-demarrages.txt"` |
| + | 83 | `cd "$R" \|\| { echo "AMORCE T08 : racine $R inaccessible : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }` |
| + | 84 | `N_DEM=0; [ -s "$R/t08-demarrages.txt" ] && read -r N_DEM < "$R/t08-demarrages.txt"` |
| − | 67 | `N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/t06-demarrages.txt"` |
| − | 68 | `printf 'AMORCE T06 v11 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${COMMIT:-?}"` |
| + | 86 | `N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/t08-demarrages.txt"` |
| + | 87 | `printf 'AMORCE T08 v1 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${COMMIT:-?}"` |
| − | 70 | `ECH="$1"; DEP="$2"; R="$3"; API="$4"; J="$R/t06-minuterie.log"` |
| + | 89 | `ECH="$1"; DEP="$2"; R="$3"; API="$4"; J="$R/t08-minuterie.log"` |
| − | 75 | `echo "$$" > "$R/t06-minuterie.pid"` |
| + | 94 | `echo "$$" > "$R/t08-minuterie.pid"` |
| − | 78 | `    if [ -f "$R/t06-consigner.sh" ]; then timeout -k 10 2400 bash "$R/t06-consigner.sh" "$1" >> "$J" 2>&1; echo "$(date -u +%FT%TZ) consigné ($1) : code $?" >> "$J"` |
| + | 97 | `    if [ -f "$R/t08-consigner.sh" ]; then timeout -k 10 2400 bash "$R/t08-consigner.sh" "$1" >> "$J" 2>&1; echo "$(date -u +%FT%TZ) consigné ($1) : code $?" >> "$J"` |
| − | 83 | `        if [ -n "$2" ]; then c=$(curl -sS -m 60 -o "$R/t06-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" -H 'Content-Type: application/json' -d "$2" "$API/…` |
| − | 84 | `        else c=$(curl -sS -m 60 -o "$R/t06-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$API/instances/$CONTAINER_ID/" 2>/dev/null) \|\| c=000; fi` |
| + | 102 | `        if [ -n "$2" ]; then c=$(curl -sS -m 60 -o "$R/t08-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" -H 'Content-Type: application/json' -d "$2" "$API/…` |
| + | 103 | `        else c=$(curl -sS -m 60 -o "$R/t08-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$API/instances/$CONTAINER_ID/" 2>/dev/null) \|\| c=000; fi` |

### Bloc 3 (modèle l. 94, copie l. 113)

**Raison** : § 3.5 « les noms » (fichiers de travail t08) ; minuterie : « montants de T0.8 » (120 USD) dans sa ligne de journal ; mécanisme inchangé. Contre-lecture M-3 : à l'heure du plafond restant, consignation puis destruction (plus de `PUT stopped`).

| | l. | ligne |
|---|---|---|
| − | 97 | `print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$1" "$2" "$R/t06-api-corps.txt" 2>/dev/null) \|\| c=000` |
| + | 116 | `print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$1" "$2" "$R/t08-api-corps.txt" 2>/dev/null) \|\| c=000` |
| − | 101 | `while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/t06-detruire" ]; do` |
| − | 102 | `    if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/t06-depense-epuisee" ]; then` |
| − | 103 | `        echo "$(date -u +%FT%TZ) DÉPENSE ÉPUISÉE (C08, plafond de 200 USD cumulé) : consignation, poussée, puis état « stopped »" >> "$J"` |
| − | 104 | `        echo "dépense épuisée $(date -u +%FT%TZ)" > "$R/t06-depense-epuisee"` |
| + | 120 | `raison=""` |
| + | 121 | `while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/t08-detruire" ]; do` |
| + | 122 | `    if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/t08-depense-epuisee" ]; then` |
| + | 123 | `        # T08 (M-3) : le texte veut la destruction après consignation et poussée, non un arrêt qui garde le disque (un conteneur arrêté` |
| + | 124 | `        # n'exécute plus cette minuterie)` |
| + | 125 | `        echo "$(date -u +%FT%TZ) DÉPENSE ÉPUISÉE (C08, plafond restant de T0.8 atteint, 120 USD cumulés) : consignation, poussée, puis destruction" >> "$J"` |
| + | 126 | `        echo "dépense épuisée $(date -u +%FT%TZ)" > "$R/t08-depense-epuisee"` |
| − | 106 | `        if [ -e "$R/t06-detruire" ]; then echo "$(date -u +%FT%TZ) PUT stopped non envoyé : ordre de destruction de l'amorce reçu pendant la consignation (R-1689)" >> "$J"` |
| − | 107 | `        else c=$(appel PUT '{"state": "stopped"}'); echo "$(date -u +%FT%TZ) PUT stopped (dépense épuisée) : HTTP $c" >> "$J"; fi` |
| + | 128 | `        raison="dépense épuisée"; break` |
| − | 111 | `raison="échéance"; [ -e "$R/t06-detruire" ] && raison="ordre de l'amorce"` |
| + | 132 | `[ -n "$raison" ] \|\| { raison="échéance"; [ -e "$R/t08-detruire" ] && raison="ordre de l'amorce"; }` |

### Bloc 4 (modèle l. 118, copie l. 139)

**Raison** : § 3.5 « les noms » (fichiers de travail, lignes « AMORCE T08 »).

| | l. | ligne |
|---|---|---|
| − | 121 | `    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/t06-api-corps.txt" 2>/dev/null && refus=oui` |
| + | 142 | `    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/t08-api-corps.txt" 2>/dev/null && refus=oui` |
| − | 128 | `printf '%s' "$MINUTERIE_TXT" > "$R/t06-minuterie.sh" \|\| { echo "AMORCE T06 : minuterie impossible à écrire"; [ "$ESSAI" = 1 ] && exit 1; sleep infinity; exit 1; }` |
| + | 149 | `printf '%s' "$MINUTERIE_TXT" > "$R/t08-minuterie.sh" \|\| { echo "AMORCE T08 : minuterie impossible à écrire"; [ "$ESSAI" = 1 ] && exit 1; sleep infinity; exit 1; }` |
| − | 132 | `    echo "$1" > "$R/t06-detruire"; echo "AMORCE $(date -u +%FT%TZ) : destruction demandée ($1)"` |
| + | 153 | `    echo "$1" > "$R/t08-detruire"; echo "AMORCE $(date -u +%FT%TZ) : destruction demandée ($1)"` |

### Bloc 5 (modèle l. 141, copie l. 162)

**Raison** : § 3.5 « les noms » (fichiers de travail). Contre-lecture M-3 : fonction `versement_prouve` (tête distante = tête locale).

| | l. | ligne |
|---|---|---|
| − | 144 | `    echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; echo "refus : $1" > "$R/t06-detruire"` |
| + | 165 | `    echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; echo "refus : $1" > "$R/t08-detruire"` |
| − | 146 | `    bash "$R/t06-minuterie.sh" 0 0 "$R" "$API" < /dev/null >> "$R/t06-minuterie.log" 2>&1; sleep infinity; exit 2; }` |
| + | 167 | `    bash "$R/t08-minuterie.sh" 0 0 "$R" "$API" < /dev/null >> "$R/t08-minuterie.log" 2>&1; sleep infinity; exit 2; }` |
| + | 168 | `versement_prouve() {  # T08 (M-3) : $1 = branche ; la tête distante égale la tête locale du dépôt extrait` |
| + | 169 | `    local l r; l=$(git -C "$R/amorce-depot" rev-parse HEAD 2>/dev/null) \|\| return 1` |
| + | 170 | `    r=$(timeout -k 5 120 git -C "$R/amorce-depot" ls-remote origin "refs/heads/$1" 2>/dev/null \| cut -f1)` |
| + | 171 | `    [ -n "$1" ] && [ -n "$l" ] && [ "$l" = "$r" ]; }` |
| − | 149 | `    if [ "$ESSAI" = 1 ]; then echo "sommeil ($1)" > "$R/t06-sommeil"; exit "${2:-0}"; fi` |
| + | 174 | `    if [ "$ESSAI" = 1 ]; then echo "sommeil ($1)" > "$R/t08-sommeil"; exit "${2:-0}"; fi` |
| − | 154 | `        if [ -e "/proc/$$/fd/9" ]; then echo "verrou tenu à l'arrêt ($1)" > "$R/t06-verrou-tenu-a-l-arret"; fi` |
| − | 155 | `        echo "stopped ($1)" > "$R/t06-arret-demande"; exit "$2"; fi` |
| − | 156 | `    local c corps="$R/t06-arret-corps.txt" ok=non` |
| + | 179 | `        if [ -e "/proc/$$/fd/9" ]; then echo "verrou tenu à l'arrêt ($1)" > "$R/t08-verrou-tenu-a-l-arret"; fi` |
| + | 180 | `        echo "stopped ($1)" > "$R/t08-arret-demande"; exit "$2"; fi` |
| + | 181 | `    local c corps="$R/t08-arret-corps.txt" ok=non` |

### Bloc 6 (modèle l. 170, copie l. 195)

**Raison** : § 3.5 « les noms » ; « montants de T0.8 » (message de l'heure d'épuisement) ; variables de la branche d'entrée, du code et du GO exigées ; texte scellé et branche de sortie de T0.8 par défaut ; bloc des épreuves à blanc retiré (refus explicite) ; « le clonage » : code au commit cité, une seule branche, sans étiquettes, extraction limitée (12 motifs relevés en jouant la liste d'essais figée sur un clone réduit, `.gitignore` compris), branche d'entrée seule, fichiers recopiés à l'octet ; commit local de la course (consigne v3, § 3.5 : liste attendue écrite avant depuis la configuration, branche d'entrée égale à elle, chemins ajoutés aux motifs d'extraction, auteur et date fixés, seul parent COMMIT, rien de gelé) ; garde précoce sur le disque (aucun lecture-sondes-t06* ni resume.json), arbre propre exigé ; ajouts par `git add --sparse` (sorties hors des motifs) ; « les noms » (script de consignation) ; données légères : les sorties de la course de T0.8 seulement (jamais les entrées de 7b) ; morceaux d'activations retirés (bras propre à la course de confirmation). Contre-lecture M-5 : échéance ramenée à l'heure du plafond restant, plus à la fin du GO ; M-3 : second démarrage après une fin normale, destruction si le versement est prouvé.

| | l. | ligne |
|---|---|---|
| − | 173 | `        echo "AMORCE T06 : outils absents :$MANQ : installation bornée (apt-get, 300 s par étape)"` |
| + | 198 | `        echo "AMORCE T08 : outils absents :$MANQ : installation bornée (apt-get, 300 s par étape)"` |
| − | 178 | `            echo "AMORCE T06 : installation ($PAQ) : code $?"` |
| + | 203 | `            echo "AMORCE T08 : installation ($PAQ) : code $?"` |
| − | 183 | `E="$R/t06-echeance.txt"; DE="$R/t06-depense-epuisee-utc.txt"` |
| + | 208 | `E="$R/t08-echeance.txt"; DE="$R/t08-depense-epuisee-utc.txt"` |
| − | 187 | `    [ "$ECH" -le "$FIN_GO" ] \|\| { echo "AMORCE T06 : échéance ramenée à la fin du GO ($FIN_GO)"; ECH=$FIN_GO; }` |
| − | 192 | `    case "$DEP" in ''\|*[!0-9]*) refus_precoce "DEPENSE_EPUISEE_UTC_S absente ou non entière (C08 : heure d'épuisement des 200 USD, calculée à la création)";; esac` |
| + | 216 | `    case "$DEP" in ''\|*[!0-9]*) refus_precoce "DEPENSE_EPUISEE_UTC_S absente ou non entière (C08 : heure d'épuisement des 120 USD de T0.8, calculée à la création)";; esac` |
| − | 195 | `if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/t06-depense-epuisee" ]; then      # R-1689 : l'argent est déjà épuisé au démarrage, l'amorce détruira` |
| − | 196 | `    echo "dépense déjà épuisée au démarrage $(date -u +%FT%TZ) (R-1689)" > "$R/t06-depense-epuisee"` |
| + | 219 | `# T08 (M-5) : l'échéance de la machine est bornée par l'heure du plafond restant, jamais par la seule fin de validité de l'accord` |
| + | 220 | `if [ "$DEP" -gt 0 ] && [ "$ECH" -gt "$DEP" ]; then echo "AMORCE T08 : échéance ramenée à l'heure du plafond restant ($DEP)"; ECH=$DEP; echo "$ECH" > "$E"; fi` |
| + | 221 | `if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/t08-depense-epuisee" ]; then      # R-1689 : l'argent est déjà épuisé au démarrage, l'amorce détruira` |
| + | 222 | `    echo "dépense déjà épuisée au démarrage $(date -u +%FT%TZ) (R-1689)" > "$R/t08-depense-epuisee"` |
| − | 199 | `    setsid bash "$R/t06-minuterie.sh" "$ECH" "$DEP" "$R" "$API" < /dev/null >> "$R/t06-minuterie.log" 2>&1 &` |
| + | 225 | `    setsid bash "$R/t08-minuterie.sh" "$ECH" "$DEP" "$R" "$API" < /dev/null >> "$R/t08-minuterie.log" 2>&1 &` |
| − | 201 | `    echo "AMORCE T06 : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null \|\| echo "?") ; dépense épuisée à $DEP)"` |
| + | 227 | `    echo "AMORCE T08 : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null \|\| echo "?") ; dépense épuisée à $DEP)"` |
| − | 207 | `    if [ -e "$R/t06-fin-normale" ] \|\| [ -e "$R/t06-depense-epuisee" ]; then` |
| + | 233 | `    if [ -e "$R/t08-fin-normale" ] \|\| [ -e "$R/t08-depense-epuisee" ]; then` |
| − | 209 | `        [ -f "$R/t06-consigner.sh" ] && timeout -k 10 1200 bash "$R/t06-consigner.sh" "second démarrage"` |
| − | 210 | `        if [ -e "$R/t06-depense-epuisee" ] \|\| [ "$(date +%s)" -ge "$DEP" ]; then` |
| + | 235 | `        [ -f "$R/t08-consigner.sh" ] && timeout -k 10 1200 bash "$R/t08-consigner.sh" "second démarrage"` |
| + | 236 | `        if [ -e "$R/t08-depense-epuisee" ] \|\| [ "$(date +%s)" -ge "$DEP" ]; then` |
| − | 214 | `        sommeil "second démarrage après une fin normale, rien ne repart" 0` |
| + | 240 | `        versement_prouve "${BRANCHE:-}" && detruire "second démarrage après une fin normale : versement prouvé, destruction (M-3)" 0   # T08` |
| + | 241 | `        sommeil "second démarrage après une fin normale, versement non prouvé : disque lisible, rien ne repart" 0` |
| − | 216 | `    [ -f "$R/t06-consigner.sh" ] && timeout -k 10 1200 bash "$R/t06-consigner.sh" "redémarrage d'un run interrompu"` |
| + | 243 | `    [ -f "$R/t08-consigner.sh" ] && timeout -k 10 1200 bash "$R/t08-consigner.sh" "redémarrage d'un run interrompu"` |
| − | 221 | `for v in COMMIT GH_TOKEN; do [ -n "${!v:-}" ] \|\| refus "$v absent"; done` |
| + | 248 | `for v in COMMIT GH_TOKEN BRANCHE_ENTREE ENTREE_COMMIT BRANCHE_CODE CONFIG; do [ -n "${!v:-}" ] \|\| refus "$v absent"; done   # T08` |
| + | 254 | `case "$ENTREE_COMMIT" in *[!0-9a-f]*\|'') refus "ENTREE_COMMIT illisible";; esac; [ "${#ENTREE_COMMIT}" = 40 ] \|\| refus "ENTREE_COMMIT de 40 caractères attendu"   # T08` |
| + | 255 | `case "$GO_ID" in GO-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) refus "GO_ID_T08=$GO_ID : identifiant de ligne de GO illisible (GO-AAAA-MM-JJ-NN attendu)";; esac   # T08` |
| − | 228 | `PREREG="${PREREG:-prereg/T0.6-organismes-v0-v1.md}"` |
| − | 229 | `BRANCHE="${BRANCHE:-calcul/t06-$MODE-v4}"` |
| + | 257 | `PREREG="${PREREG:-prereg/T0.8-bases-boite-noire-v0-v1.md}"   # T08` |
| + | 258 | `BRANCHE="${BRANCHE:-calcul/t08-$MODE-v1}"   # T08` |
| − | 231 | `# C-V4-3 : épreuves à blanc (aucune donnée décisive) : EPREUVE_GO_ID (v11 : toute ligne de GO de calcul lue au registre du commit), sans préenregistrement, branche essai/…` |
| − | 232 | `EPREUVE_GO="${EPREUVE_GO_ID:-}"` |
| − | 233 | `if [ -n "$EPREUVE_GO" ]; then` |
| − | 234 | `    # v11 : plus d'identifiant en dur ; la ligne est lue dans registres/go.md du commit cloné (session_v12 : type calcul, Lazar, non échue, non révoquée) et son plafond devient PLAFOND_LIGNE_GO` |
| − | 235 | `    case "$EPREUVE_GO" in GO-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) refus "EPREUVE_GO_ID=$EPREUVE_GO : identifiant de ligne de GO illisible (GO-AAAA-MM-JJ-NN attendu)";; esac` |
| − | 236 | `    [ "$EPREUVE_GO" != "$GO_ID" ] \|\| refus "EPREUVE_GO_ID=$EPREUVE_GO est le GO de la course : une épreuve à blanc se joue sous sa propre ligne de GO de calcul"` |
| − | 237 | `    [ "$PREREG_ABSENT" = 1 ] \|\| refus "épreuve à blanc : PREREG_ABSENT=1 exigé (une épreuve n'est jamais décisive)"` |
| − | 238 | `    case "$BRANCHE" in essai/*) ;; *) refus "épreuve à blanc : la branche doit commencer par essai/ ($BRANCHE) : jamais calcul/";; esac` |
| − | 239 | `    [ -n "${CONFIG:-}" ] \|\| refus "épreuve à blanc : CONFIG exigé"` |
| − | 240 | `    GO_ID="$EPREUVE_GO"` |
| − | 241 | `fi` |
| − | 242 | `[ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ] && [ -z "$EPREUVE_GO" ] && refus "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1) ou pour une épreuve à blanc sous sa ligne de GO de calcul (EPREUVE…` |
| − | 243 | `[ -n "${TESTS_ARGS:-}" ] && { [ "$PREREG_ABSENT" != 1 ] \|\| [ "$MODE" != jouet ]; } && refus "TESTS_ARGS n'est permis qu'en répétition jouet sans préenregistrement (jamais en mode réel, épreuve compr…` |
| + | 260 | `[ -z "${EPREUVE_GO_ID:-}" ] \|\| refus "EPREUVE_GO_ID=$EPREUVE_GO_ID : aucune épreuve à blanc pour T0.8 (ordre de course)"   # T08 : bloc des épreuves de T0.6 retiré` |
| + | 261 | `[ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ] && refus "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)"   # T08` |
| + | 262 | `[ -n "${TESTS_ARGS:-}" ] && { [ "$PREREG_ABSENT" != 1 ] \|\| [ "$MODE" != jouet ]; } && refus "TESTS_ARGS n'est permis qu'en répétition jouet sans préenregistrement (jamais en mode réel : la suite cib…` |
| − | 246 | `# R-1677 : clonage réduit. Chemins nécessaires à l'instance (mode sans cône ; motifs de type gitignore) :` |
| − | 247 | `#  - code et essais joués par l'amorce : /src/ /tests/ /scripts/ /.claude/ /pyproject.toml /requirements-*.txt ;` |
| − | 248 | `#  - préenregistrement, configurations, tâches, consignes et leurs sceaux (clés citées) : /prereg/ /donnees/ /docs/notes/ ;` |
| − | 249 | `#  - registre des GO lu par l'amorce et par les essais : /registres/*.md (jamais /registres/passations/, 191 Mo) ;` |
| − | 250 | `#  - ce que lisent les essais de la suite complète (chemins relevés par recherche dans tests/ src/ scripts/ et confirmés par l'essai de` |
| − | 251 | `#    la suite complète sur un clone réduit) : /diag/ /runs/ /traces/ /docs/*.md /docs/*.txt /docs/*.sha256 /docs/procedures/ /docs/decisions/` |
| − | 252 | `#    /docs/verdicts/ /docs/etat-de-l-art/, les petits dossiers de /docs/sources/ cités par les essais, et les trois dossiers d'ordres d'épreuve` |
| − | 253 | `#    /brouillons/ordres-t06-e2-e3-v{2,3,4,5}/ (les essais v6 à v8 comparent les filtres des ordres à ceux du lanceur ; quelques Ko) ;` |
| − | 254 | `#  - exclus : /docs/sources/pdf/ (1,85 Go de PDF de tiers) et le reste de /docs/sources/, /registres/passations/, /brouillons/, /livrables/, /gemini/, /papiers/.` |
| − | 255 | `CHEMINS_CLONAGE='/.claude/` |
| + | 265 | `# T08 : clonage réduit au code de la course et de ses essais (mode sans cône ; motifs relevés en jouant la liste d'essais figée sur` |
| + | 266 | `# un clone réduit : 252 essais passés, un écarté, aucun fichier manquant), d'une seule branche, sans étiquettes ; puis la branche d'entrée seule.` |
| + | 267 | `#  - /.gitignore (caches Python, 'donnees/') : sans lui, les caches écrits par les essais salissent l'arbre et la course refuse` |
| + | 268 | `#    de partir (essai de bout en bout du 22 novembre) ;` |
| + | 269 | `#  - code et essais : /src/ /tests/ /scripts/ /.claude/ /pyproject.toml /requirements-*.txt ;` |
| + | 270 | `#  - registre des GO lu par l'amorce (/registres/go.md) ; fichiers lus par les essais de T0.8 : /registres/scellements-v1.md,` |
| + | 271 | `#    /registres/code-mots-et-cout-t06/, /docs/sources/invites-2606.08892-v1/, /prereg/T0.8-base-A-mots-et-cout-v1.md et son sceau ;` |
| + | 272 | `#  - jamais : /diag/ /runs/ /donnees/ du code, /docs/notes/, /brouillons/, ni aucune autre branche (la branche de sortie de 7b` |
| + | 273 | `#    n'est jamais demandée : la branche d'entrée porte les seuls fichiers de la liste blanche).` |
| + | 274 | `CHEMINS_CLONAGE='/.gitignore` |
| + | 275 | `/.claude/` |
| − | 261 | `/prereg/` |
| − | 262 | `/donnees/` |
| − | 263 | `/diag/` |
| − | 264 | `/runs/` |
| − | 265 | `/traces/` |
| − | 266 | `/registres/*.md` |
| − | 267 | `/docs/*.md` |
| − | 268 | `/docs/*.txt` |
| − | 269 | `/docs/*.sha256` |
| − | 270 | `/docs/notes/` |
| − | 271 | `/docs/procedures/` |
| − | 272 | `/docs/decisions/` |
| − | 273 | `/docs/verdicts/` |
| − | 274 | `/docs/etat-de-l-art/` |
| − | 275 | `/docs/sources/invites-2606.07054-v1/` |
| + | 281 | `/registres/go.md` |
| + | 282 | `/registres/scellements-v1.md` |
| + | 283 | `/registres/code-mots-et-cout-t06/` |
| − | 277 | `/docs/sources/cartes-modeles-20261006/` |
| − | 278 | `/docs/sources/donnees-T0.7/` |
| − | 279 | `/brouillons/ordres-t06-e2-e3-v2/` |
| − | 280 | `/brouillons/ordres-t06-e2-e3-v3/` |
| − | 281 | `/brouillons/ordres-t06-e2-e3-v4/` |
| − | 282 | `/brouillons/ordres-t06-e2-e3-v5/'` |
| + | 285 | `/prereg/T0.8-base-A-mots-et-cout-v1.md*'` |
| − | 284 | `timeout -k 10 900 git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$R/amorce-depot" \|\| refus "clonage impossible (jeton GitHub ?)"` |
| + | 287 | `timeout -k 10 900 git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --no-tags --branch "$BRANCHE_CODE" "$DEPOT_URL" "$R/amorce-depot" \|\| refus "clonage impos…` |
| − | 286 | `git -C "$R/amorce-depot" config user.name "instance de calcul (T0.6)"` |
| + | 289 | `git -C "$R/amorce-depot" config user.name "instance de calcul (T0.8)"   # T08` |
| − | 291 | `timeout -k 10 900 git -C "$R/amorce-depot" checkout -q "$COMMIT" \|\| refus "commit $COMMIT introuvable"` |
| + | 294 | `timeout -k 10 900 git -C "$R/amorce-depot" checkout -q "$COMMIT" \|\| refus "commit $COMMIT introuvable sur la branche $BRANCHE_CODE"` |
| + | 295 | `# T08 : branche d'entrée seule (refspec explicite, au commit consigné par les contrôles), fichiers recopiés à l'octet à leurs chemins,` |
| + | 296 | `# puis commit local de la course (consigne v3, § 3.5) : seul parent COMMIT, n'ajoute que la liste attendue (écrite avant, depuis la` |
| + | 297 | `# configuration), rien sous un chemin gelé ; auteur, date et message fixés ; la branche de sortie part de lui` |
| + | 298 | `timeout -k 10 900 git -C "$R/amorce-depot" fetch -q --no-tags --depth 1 origin "refs/heads/$BRANCHE_ENTREE:refs/remotes/origin/$BRANCHE_ENTREE" \|\| refus "branche d'entrée $BRANCHE_ENTREE introuvable…` |
| + | 299 | `[ "$(git -C "$R/amorce-depot" rev-parse "refs/remotes/origin/$BRANCHE_ENTREE")" = "$ENTREE_COMMIT" ] \|\| refus "branche d'entrée $BRANCHE_ENTREE ≠ commit des contrôles $ENTREE_COMMIT"` |
| + | 300 | `[ "$(git -C "$R/amorce-depot" rev-list --count "$ENTREE_COMMIT")" = 1 ] \|\| refus "branche d'entrée non orpheline (plus d'un commit)"` |
| + | 301 | `NB_ENTREE=0; ENTREES=()` |
| + | 302 | `while IFS= read -r -d '' f; do` |
| + | 303 | `    case "$f" in /*\|*..*) refus "chemin de la branche d'entrée illisible : $f";; esac` |
| + | 304 | `    SUIVI=$(git -C "$R/amorce-depot" ls-tree --name-only "$COMMIT" -- "$f" 2>/dev/null)      # suivi au commit du code (tâches, consignes, invites) : même contenu exigé` |
| + | 305 | `    if [ -e "$R/amorce-depot/$f" ] && [ -z "$SUIVI" ]; then refus "fichier d'entrée $f déjà présent sur le disque"; fi` |
| + | 306 | `    mkdir -p "$R/amorce-depot/$(dirname "$f")" && git -C "$R/amorce-depot" show "$ENTREE_COMMIT:$f" > "$R/amorce-depot/$f" \|\| refus "copie de $f"` |
| + | 307 | `    if [ -n "$SUIVI" ]; then [ "$(git -C "$R/amorce-depot" rev-parse "$COMMIT:$f")" = "$(git -C "$R/amorce-depot" rev-parse "$ENTREE_COMMIT:$f")" ] \|\| refus "fichier d'entrée $f ≠ celui du commit du…` |
| + | 308 | `    ENTREES+=("$f"); NB_ENTREE=$((NB_ENTREE + 1))` |
| + | 309 | `done < <(git -C "$R/amorce-depot" ls-tree -r -z --name-only "$ENTREE_COMMIT")` |
| + | 310 | `[ "$NB_ENTREE" -gt 0 ] \|\| refus "branche d'entrée vide"` |
| + | 311 | `COMMIT_LOCAL="import sys; sys.path.insert(0, 'src'); from controle_ia.lancement_t08 import commit_local_v1 as c; sys.exit(c.main(sys.argv[1:]))"` |
| + | 312 | `PR_ATT="$PREREG"; [ "${PREREG_ABSENT:-0}" = 1 ] && PR_ATT=-` |
| + | 313 | `( cd "$R/amorce-depot" && python3 -I -B -c "$COMMIT_LOCAL" attendus "$CONFIG" "$PR_ATT" ) > "$R/t08-liste-attendue.txt" 2>&1 \|\| refus "liste attendue du commit local : $(tail -n 1 "$R/t08-liste-atte…` |
| + | 314 | `CL=$( cd "$R/amorce-depot" && python3 -I -B -c "$COMMIT_LOCAL" branche . "$ENTREE_COMMIT" "$R/t08-liste-attendue.txt" 2>&1 ) \|\| refus "$CL"` |
| + | 315 | `# les entrées restent extraites : leurs chemins exacts rejoignent les motifs (sinon la création de la branche de sortie les retire du` |
| + | 316 | `# disque, l'extraction partielle étant réappliquée : essai du 22 novembre)` |
| + | 317 | `SP_MSG=$(sed 's#^#/#' "$R/t08-liste-attendue.txt" \| git -C "$R/amorce-depot" sparse-checkout add --stdin 2>&1) \|\| refus "extraction partielle des entrées impossible : $(printf '%s' "$SP_MSG" \| hea…` |
| + | 318 | `git -C "$R/amorce-depot" add --sparse -f -- "${ENTREES[@]}" \|\| refus "ajout local des entrées"` |
| + | 319 | `DATE_E=$(git -C "$R/amorce-depot" log -1 --format=%cI "$ENTREE_COMMIT")` |
| + | 320 | `GIT_AUTHOR_DATE="$DATE_E" GIT_COMMITTER_DATE="$DATE_E" git -C "$R/amorce-depot" commit -q -m "T0.8 : entrées de la course, commit local de l'instance (branche d'entrée $BRANCHE_ENTREE au commit $ENTRE…` |
| + | 321 | `CL=$( cd "$R/amorce-depot" && python3 -I -B -c "$COMMIT_LOCAL" verifier . "$COMMIT" "$R/t08-liste-attendue.txt" 2>&1 ) \|\| refus "$CL"` |
| + | 322 | `echo "AMORCE $(date -u +%FT%TZ) : $CL"` |
| + | 323 | `# T08 : garde précoce (outils de l'image seuls, aucun paquet) : aucun lecture-sondes-t06* ni resume.json sur le disque extrait ;` |
| + | 324 | `# la garde du code (entrees_v1.exiger_instance_sans_interdits, objets git compris) est rejouée avant tout calcul, l'environnement installé` |
| + | 325 | `INTERDIT=$(cd "$R/amorce-depot" && find . -path ./.git -prune -o -type f \( -name 'lecture-sondes-t06*' -o -name 'resume.json' \) -print \| head -n 3)` |
| + | 326 | `[ -z "$INTERDIT" ] \|\| refus "fichier interdit présent sur l'instance après le clonage : $(printf '%s' "$INTERDIT" \| tr '\n' ' ') (DT-4) : arrêt et nœud"` |
| + | 327 | `ETAT=$(git -C "$R/amorce-depot" status --porcelain --untracked-files=all 2>&1); [ -z "$ETAT" ] \|\| refus "arbre non propre après la copie des entrées : $(printf '%s' "$ETAT" \| head -n 3 \| tr '\n' '…` |
| − | 295 | `echo "AMORCE $(date -u +%FT%TZ) : CLONAGE mode=$MODE secondes=$CL_S octets_git=${CL_GIT:-?} octets_arbre=${CL_ARBRE:-?} debit_Mo_s=$(awk -v b="${CL_GIT:-0}" -v a="${CL_ARBRE:-0}" -v s="$CL_S" 'BEGIN {…` |
| − | 296 | `T="$R/t06"; mkdir -p "$T"` |
| + | 331 | `echo "AMORCE $(date -u +%FT%TZ) : CLONAGE mode=$MODE secondes=$CL_S octets_git=${CL_GIT:-?} octets_arbre=${CL_ARBRE:-?} debit_Mo_s=$(awk -v b="${CL_GIT:-0}" -v a="${CL_ARBRE:-0}" -v s="$CL_S" 'BEGIN {…` |
| + | 332 | `T="$R/t08"; mkdir -p "$T"` |
| − | 303 | `cat > "$R/t06-consigner.sh" <<CONSIGNER` |
| + | 339 | `cat > "$R/t08-consigner.sh" <<CONSIGNER` |
| − | 308 | `cat >> "$R/t06-consigner.sh" <<'CONSIGNER'` |
| + | 344 | `cat >> "$R/t08-consigner.sh" <<'CONSIGNER'` |
| − | 313 | `        if [ "$t" -gt "$MORCEAU_MAX" ]; then git rm -q --cached -- "$f" >/dev/null 2>&1; journal "ERREUR DE CHAÎNE (C11) : $f fait $t octets > $MORCEAU_MAX : retiré du commit, resté sur l'instance"; e…` |
| + | 349 | `        if [ "$t" -gt "$MORCEAU_MAX" ]; then git rm -q --sparse --cached -- "$f" >/dev/null 2>&1; journal "ERREUR DE CHAÎNE (C11) : $f fait $t octets > $MORCEAU_MAX : retiré du commit, resté sur l'ins…` |
| − | 316 | `    git add "$@" 2>"$T/add.err" && return 0` |
| − | 317 | `    journal "ERREUR DE CHAÎNE (C-V4-1) : git add en échec ($*) : $(tr '\n' ' ' < "$T/add.err" \| cut -c1-200)"; echo "$(date -u +%FT%TZ) git add en échec : $*" >> "$R/t06-erreurs-chaine.txt"; return 1…` |
| − | 318 | `ajouter_legeres() { local f rc=0; for f in donnees/*/adaptateur-*.pt donnees/*/adaptateur-*.pt.sha256 donnees/*/mesures-t06.npz donnees/*/mesures-t06.npz.sha256 \` |
| − | 319 | `        donnees/*/textes-actions-t06.jsonl donnees/*/textes-actions-t06.jsonl.sha256 donnees/*/activations-sous-ensemble-t06-manifeste.json \` |
| − | 320 | `        donnees/*/activations-sous-ensemble-t06-manifeste.json.sha256; do if [ -f "$f" ]; then ajouter -f "$f" \|\| rc=1; fi; done; return $rc; }` |
| − | 321 | `ajouter_morceaux() { local f rc=0; for f in donnees/*/activations-sous-ensemble-t06-[0-9][0-9][0-9].npz donnees/*/activations-sous-ensemble-t06-[0-9][0-9][0-9].npz.sha256; do` |
| − | 322 | `        if [ -f "$f" ]; then ajouter -f "$f" \|\| rc=1; fi; done; return $rc; }` |
| + | 352 | `    git add --sparse "$@" 2>"$T/add.err" && return 0   # T08 : --sparse, les sorties (runs, diag, donnees, traces) sont hors des motifs d'extraction` |
| + | 353 | `    journal "ERREUR DE CHAÎNE (C-V4-1) : git add en échec ($*) : $(tr '\n' ' ' < "$T/add.err" \| cut -c1-200)"; echo "$(date -u +%FT%TZ) git add en échec : $*" >> "$R/t08-erreurs-chaine.txt"; return 1…` |
| + | 354 | `ajouter_legeres() { local f rc=0; for f in donnees/*-t08-*/*-t08.npz donnees/*-t08-*/*-t08.npz.sha256 donnees/*-t08-*/*-t08.jsonl \` |
| + | 355 | `        donnees/*-t08-*/*-t08.jsonl.sha256; do if [ -f "$f" ]; then ajouter -f "$f" \|\| rc=1; fi; done; return $rc; }   # T08 : sorties de la course de T0.8 seulement (jamais les entrées de 7b, sous …` |
| + | 356 | `ajouter_morceaux() { return 0; }   # T08 : aucun morceau d'activations (bras propre à la course de confirmation, retiré)` |
| − | 327 | `    if [ "$rc" != 1 ]; then journal "ERREUR DE CHAÎNE (C-V4-1) : lecture de l'index impossible (git diff, code $rc)"; echo "$(date -u +%FT%TZ) lecture de l'index impossible : $1" >> "$R/t06-erreurs-ch…` |
| + | 361 | `    if [ "$rc" != 1 ]; then journal "ERREUR DE CHAÎNE (C-V4-1) : lecture de l'index impossible (git diff, code $rc)"; echo "$(date -u +%FT%TZ) lecture de l'index impossible : $1" >> "$R/t08-erreurs-ch…` |
| − | 333 | `    echo "$(date -u +%FT%TZ) commit en échec : $1" >> "$R/t06-erreurs-chaine.txt"; return 1; }` |
| + | 367 | `    echo "$(date -u +%FT%TZ) commit en échec : $1" >> "$R/t08-erreurs-chaine.txt"; return 1; }` |

### Bloc 7 (modèle l. 339, copie l. 373)

**Raison** : § 3.5 « les noms » (messages de commit T0.8, verrou) ; GO lu au registre du commit par le module de T0.8 (prolongation comprise) au lieu des modules de T0.6 ; citations : la configuration et le texte scellé passés par le lanceur (le texte de T0.8 ne porte pas les citations de T0.6) ; calendrier lu au registre ; « le nombre attendu » d'essais ne vient plus du texte mais de l'amorce (bloc 9). Contre-lecture M-5 : le refus « échéance après la fin du GO » est retiré.

| | l. | ligne |
|---|---|---|
| − | 342 | `    [ -f "$R/t06-minuterie.log" ] && tail -n 200 "$R/t06-minuterie.log" \| cut -c1-400 > "$d/t06-minuterie-fin.txt"      # la ligne « ÉCHÉANCE … atteinte (C14) » est écrite par la minuterie, pas par l…` |
| + | 376 | `    [ -f "$R/t08-minuterie.log" ] && tail -n 200 "$R/t08-minuterie.log" \| cut -c1-400 > "$d/t08-minuterie-fin.txt"      # la ligne « ÉCHÉANCE … atteinte (C14) » est écrite par la minuterie, pas par l…` |
| − | 345 | `    etape_commit "T0.6 : journal de l'instance ($1)" "$1 : journal de l'instance committé" ""; }` |
| + | 379 | `    etape_commit "T0.8 : journal de l'instance ($1)" "$1 : journal de l'instance committé" ""; }` |
| − | 350 | `    etape_commit "T0.6 : résultats et données légères ($1)" "$1 : résultats et données légères committés" "$1 : aucun résultat léger à committer" \|\| echec=1` |
| + | 384 | `    etape_commit "T0.8 : résultats et données légères ($1)" "$1 : résultats et données légères committés" "$1 : aucun résultat léger à committer" \|\| echec=1` |
| − | 352 | `    etape_commit "T0.6 : sous-ensemble d'activations en morceaux ($1)" "$1 : morceaux committés" "" \|\| echec=1` |
| + | 386 | `    etape_commit "T0.8 : sous-ensemble d'activations en morceaux ($1)" "$1 : morceaux committés" "" \|\| echec=1` |
| − | 357 | `exec 9>>"$R/t06-consigner.lock"; flock -w 1500 9 \|\| { echo "verrou de consignation non obtenu ($1)"; exit 1; }` |
| + | 391 | `exec 9>>"$R/t08-consigner.lock"; flock -w 1500 9 \|\| { echo "verrou de consignation non obtenu ($1)"; exit 1; }` |
| − | 363 | `. "$R/t06-consigner.sh" --source` |
| − | 364 | `journal "début v4 : MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE PREREG=$PREREG GO=$GO_ID FIN_GO=$FIN_GO ECHEANCE=$ECH DEPENSE_EPUISEE=$DEP"` |
| − | 365 | `SESSION_V2="import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session_v2; sys.exit(session_v2.main(sys.argv[1:]))"` |
| − | 366 | `SESSION_V3="import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"` |
| − | 367 | `SESSION_V12="import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session_v12; sys.exit(session_v12.main(sys.argv[1:]))"` |
| − | 368 | `if [ -n "$EPREUVE_GO" ]; then` |
| − | 369 | `    PLAFOND_LIGNE_GO=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V12" plafond-ligne registres/go.md "$EPREUVE_GO" 2>&1) \|\| refus "$GO_ID non conforme dans registres/go.md du commit ($PLAFOND_LIGNE…` |
| − | 370 | `    GOL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V3" go registres/go.md "$EPREUVE_GO" "$PLAFOND_LIGNE_GO" 2>&1) \|\| refus "$GO_ID non conforme ($GOL)"` |
| − | 371 | `else` |
| − | 372 | `    GOL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V2" go registres/go.md 2>&1) \|\| refus "$GO_ID non conforme ($GOL)"` |
| − | 373 | `fi` |
| + | 397 | `. "$R/t08-consigner.sh" --source` |
| + | 398 | `journal "début t08 v1 : MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE ENTREE=$BRANCHE_ENTREE@$ENTREE_COMMIT PREREG=$PREREG CONFIG=$CONFIG GO=$GO_ID FIN_GO=$FIN_GO ECHEANCE=$ECH DEPENSE_EPUISEE=$DEP"` |
| + | 399 | `SESSION_T08="import sys; sys.path.insert(0, 'src'); from controle_ia.lancement_t08 import session_v1; sys.exit(session_v1.main(sys.argv[1:]))"   # T08` |
| + | 400 | `[ -f "$CONFIG" ] && [ -f "$CONFIG.sha256" ] \|\| refus "configuration $CONFIG ou son sceau absent (branche d'entrée)"   # T08` |
| + | 401 | `GOL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_T08" go registres/go.md "$CONFIG" "$GO_ID" 2>&1) \|\| refus "$GO_ID non conforme dans registres/go.md du commit ($GOL)"   # T08 : prolongation compris…` |
| − | 375 | `lire_unique() { local n; n=$(grep -c "$1 : \'" "$PREREG" \|\| true); if [ "$n" != 1 ]; then echo ""; return 0; fi; sed -n "s/.*$1 : \'\\([^\']*\\)\'.*/\\1/p" "$PREREG"; }` |
| − | 376 | `if [ "$PREREG_ABSENT" = 1 ]; then` |
| − | 377 | `    ATTENDUS="${TESTS_ATTENDUS:-}"; : "${CONFIG:?CONFIG obligatoire sans préenregistrement}"` |
| − | 378 | `    CITES=("$CONFIG")` |
| + | 403 | `if [ "$PREREG_ABSENT" = 1 ]; then CITES=("$CONFIG")   # T08 : répétition jouet seulement` |
| − | 380 | `    [ -f "$PREREG" ] \|\| refus "préenregistrement $PREREG absent au commit $COMMIT"` |
| − | 381 | `    ATTENDUS=$(lire_unique "Tests attendus")` |
| − | 382 | `    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] \|\| refus "nombre de tests attendus introuvable ou cité plusieurs fois dans $PREREG"` |
| − | 383 | `    CONFIG=$(lire_unique "Chemin de la configuration de T0.6")` |
| − | 384 | `    TACHES_E=$(lire_unique "Chemin des tâches d'évaluation de T0.6")` |
| − | 385 | `    TACHES_D=$(lire_unique "Chemin des tâches de distillation de T0.6")` |
| − | 386 | `    CONSIGNES=$(lire_unique "Chemin des consignes de P3")` |
| − | 387 | `    CITES=("$CONFIG" "$TACHES_E" "$TACHES_D" "$CONSIGNES")` |
| − | 388 | `fi` |
| − | 389 | `for f in "${CITES[@]}"; do` |
| − | 390 | `    [ -n "$f" ] \|\| refus "chemin cité introuvable ou cité plusieurs fois dans $PREREG"` |
| − | 391 | `    { [ -f "$f" ] && [ -f "$f.sha256" ]; } \|\| refus "fichier cité $f ou son sceau absent de l'arbre du commit $COMMIT"` |
| − | 392 | `done` |
| + | 405 | `    [ -f "$PREREG" ] && [ -f "$PREREG.sha256" ] \|\| refus "préenregistrement $PREREG ou son sceau absent (branche d'entrée)"` |
| + | 406 | `    CITES=("$CONFIG" "$PREREG")` |
| + | 407 | `fi` |
| − | 395 | `journal "citations lues : tests attendus ${ATTENDUS:-?} ; configuration $CONFIG ; fichiers cités présents et scellés"` |
| − | 396 | `# L11 : la fin du GO reçue de la session est celle de la configuration (calendrier vérifié contre le registre des GO)` |
| − | 397 | `if [ -n "$EPREUVE_GO" ]; then CAL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V3" calendrier "$CONFIG" registres/go.md "$EPREUVE_GO" "$PLAFOND_LIGNE_GO" 2>&1) \|\| refus "calendrier de la configurat…` |
| − | 398 | `else CAL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V2" calendrier "$CONFIG" registres/go.md 2>&1) \|\| refus "calendrier de la configuration non conforme ($CAL)"; fi` |
| + | 410 | `journal "citations lues : configuration $CONFIG ; préenregistrement ${PREREG_ABSENT/1/absent (jouet)} ; fichiers cités présents et scellés"` |
| + | 411 | `# L11 : la fin du GO reçue de la session est celle de la ligne de GO lue au registre du commit (T08 : calendrier lu au registre)` |
| + | 412 | `CAL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_T08" calendrier registres/go.md "$CONFIG" "$GO_ID" 2>&1) \|\| refus "calendrier lu au registre non conforme ($CAL)"   # T08` |
| − | 400 | `[ "$FIN_CONFIG" = "$FIN_GO" ] \|\| refus "fin du GO reçue ($FIN_GO) ≠ calendrier.fin_go_utc de la configuration ($FIN_CONFIG) (L11)"` |
| − | 401 | `[ "$ECH" -le "$FIN_CONFIG" ] \|\| refus "échéance $ECH après la fin du GO de la configuration ($FIN_CONFIG)"` |
| + | 414 | `[ "$FIN_CONFIG" = "$FIN_GO" ] \|\| refus "fin du GO reçue ($FIN_GO) ≠ fin de validité de la ligne $GO_ID au registre du commit ($FIN_CONFIG) (L11)"` |

### Bloc 8 (modèle l. 410, copie l. 423)

**Raison** : § 3.5 « les noms » (traces, verrou, fin anormale) ; « les bras propres à la course de confirmation (audit de fuite, sondes) sont retirés » : bras B retiré ; environnement Python hors du dépôt ($R/venv-t08) : la garde de l'instance parcourt tout le dépôt.

| | l. | ligne |
|---|---|---|
| − | 413 | `traces() { local d; mkdir -p traces; d=$(mktemp -d "traces/t06-$(date -u +%Y%m%d-%H%M%S)-XXXX")` |
| − | 414 | `    for f in "$JOURNAL" "$T/tests.txt" "$T/tests.err" "$T"/run.json "$T"/run.err "$T"/nvidia-smi.txt "$T"/pip-freeze.txt "$R/t06-minuterie.log" "$R/t06-fichiers-trop-gros.txt" "$T/progres-retenues.txt…` |
| + | 426 | `traces() { local d; mkdir -p traces; d=$(mktemp -d "traces/t08-$(date -u +%Y%m%d-%H%M%S)-XXXX")` |
| + | 427 | `    for f in "$JOURNAL" "$T/tests.txt" "$T/tests.err" "$T"/run.json "$T"/run.err "$T"/nvidia-smi.txt "$T"/pip-freeze.txt "$R/t08-minuterie.log" "$R/t08-fichiers-trop-gros.txt" "$T/progres-retenues.txt…` |
| − | 416 | `    ajouter "$d" \|\| return 1; etape_commit "T0.6 : traces de l'instance ($1)" "" "traces : aucun fichier neuf à committer"; }` |
| − | 417 | `# GO-2026-11-07-04 : bras B de l'audit de fuite (annexe), jamais bloquant, jamais avant la poussée finale de T0.6` |
| − | 418 | `bras_b() {` |
| − | 419 | `    local cfg="${BRAS_B_CONFIG:-docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json}" run code t0 d` |
| − | 420 | `    if [ "${BRAS_B:-1}" = 0 ]; then journal "bras B : non lancé (BRAS_B=0)"; return 0; fi` |
| − | 421 | `    if [ "$MODE" != reel ] && [ "${BRAS_B_FORCER:-0}" != 1 ]; then journal "bras B : non lancé (mode $MODE)"; return 0; fi` |
| − | 422 | `    if [ -n "${EPREUVE_GO_ID:-}" ] && [ "${BRAS_B_EPREUVE:-0}" != 1 ]; then journal "bras B : non lancé (épreuve à blanc)"; return 0; fi` |
| − | 423 | `    if [ ! -f "$cfg" ]; then journal "bras B : non lancé (configuration absente du commit : $cfg)"; return 0; fi` |
| − | 424 | `    run="bras-b-$(date -u +%Y%m%d-%H%M%S)"; t0=$(date +%s)` |
| − | 425 | `    journal "bras B : début ($run), annexe régie par prereg/audit-fuite-r1-v4-v1.md (point 7), sans effet sur T0.6"` |
| − | 426 | `    PYTHONPATH="src:${BRAS_B_PYTHONPATH:-}" timeout -k 10 "${BRAS_B_DUREE_MAX_S:-2400}" "${BRAS_B_PYTHON:-python}" -m "${BRAS_B_MODULE:-controle_ia.audit_fuite_r1_v4.bras_b_v4}" --config "$cfg" --run-…` |
| − | 427 | `        --prereg prereg/audit-fuite-r1-v4-v1.md --autoriser-depot-sale >"$T/bras-b.out" 2>"$T/bras-b.err"` |
| − | 428 | `    code=$?` |
| − | 429 | `    journal "bras B : code $code en $(( $(date +%s) - t0 )) s ($([ "$code" = 0 ] && echo 'sortie écrite' \|\| echo 'sans sortie fiable')) ; sans effet sur le run de T0.6"` |
| − | 430 | `    d="traces/$run"; mkdir -p "$d" && cp "$T/bras-b.out" "$T/bras-b.err" "$d/" 2>/dev/null` |
| − | 431 | `    if prendre_verrou "bras B"; then` |
| − | 432 | `        ajouter -f "$d" \|\| true` |
| − | 433 | `        [ -d "diag/$run" ] && { ajouter -f "diag/$run" \|\| true; }` |
| − | 434 | `        [ -d "runs/$run" ] && { ajouter -f "runs/$run" \|\| true; }` |
| − | 435 | `        etape_commit "T0.6 : bras B de l'audit de fuite (annexe, code $code)" "bras B : sorties committées" "bras B : rien à committer" \|\| journal "bras B : commit en échec (sans effet sur T0.6)"` |
| − | 436 | `        pousser && journal "bras B : branche $BRANCHE poussée" \|\| journal "bras B : poussée impossible (sans effet sur T0.6)"` |
| − | 437 | `        liberer_verrou` |
| − | 438 | `    else` |
| − | 439 | `        journal "bras B : verrou de consignation non obtenu, sorties laissées sur l'instance"` |
| − | 440 | `    fi` |
| − | 441 | `    return 0` |
| − | 442 | `}` |
| − | 443 | `# C-V4-1 : la fin de run et les consignations d'arrêt prennent le verrou de 't06-consigner.sh' (fd 9) ; il n'est pris qu'APRÈS` |
| + | 429 | `    ajouter "$d" \|\| return 1; etape_commit "T0.8 : traces de l'instance ($1)" "" "traces : aucun fichier neuf à committer"; }` |
| + | 430 | `# T08 : bras B de l'audit de fuite (annexe de la course de confirmation) retiré : aucun bras annexe sur la machine de T0.8` |
| + | 431 | `# C-V4-1 : la fin de run et les consignations d'arrêt prennent le verrou de 't08-consigner.sh' (fd 9) ; il n'est pris qu'APRÈS` |
| − | 446 | `    exec 9>>"$R/t06-consigner.lock"` |
| + | 434 | `    exec 9>>"$R/t08-consigner.lock"` |
| − | 448 | `    journal "ERREUR DE CHAÎNE (C-V4-1) : verrou de consignation non obtenu ($1)"; echo "$(date -u +%FT%TZ) verrou non obtenu : $1" >> "$R/t06-erreurs-chaine.txt"` |
| + | 436 | `    journal "ERREUR DE CHAÎNE (C-V4-1) : verrou de consignation non obtenu ($1)"; echo "$(date -u +%FT%TZ) verrou non obtenu : $1" >> "$R/t08-erreurs-chaine.txt"` |
| − | 453 | `    echo "fin anormale $(date -u +%FT%TZ), run $RUN : $1" > "$R/t06-fin-anormale"; journal "FIN ANORMALE (C-V4-1) : $1"` |
| + | 441 | `    echo "fin anormale $(date -u +%FT%TZ), run $RUN : $1" > "$R/t08-fin-anormale"; journal "FIN ANORMALE (C-V4-1) : $1"` |
| − | 457 | `    timeout -k 10 1800 python3.11 -m venv .venv && . .venv/bin/activate && timeout -k 10 3600 pip install -q -r requirements-gpu.txt \|\| { journal "installation impossible"; consigner_arret "installa…` |
| + | 445 | `    timeout -k 10 1800 python3.11 -m venv "$R/venv-t08" && . "$R/venv-t08/bin/activate" && timeout -k 10 3600 pip install -q -r requirements-gpu.txt \|\| { journal "installation impossible"; consigner…` |

### Bloc 9 (modèle l. 470, copie l. 458)

**Raison** : § 3.5 « avant tout calcul : exiger_instance_sans_interdits (garde resserrée du code aligné, run de 7b lu dans la configuration), le commit du code égal à celui du texte scellé (commit local : seul parent COMMIT = COMMIT_CODE_T08), le texte scellé intact » ; « la liste d'essais ciblée et figée de T0.8, dans un fichier à part, avec le nombre attendu » (empreinte et nombre écrits en dur).

| | l. | ligne |
|---|---|---|
| − | 473 | `# v9 : suite ciblée et figée (liste de fichiers à l'empreinte écrite en dur) ; TESTS_ARGS (jouet seulement) a la priorité` |
| − | 474 | `LISTE_TESTS="scripts/tests-cibles-t06-v3.txt"; LISTE_SHA256="e76d5e6b7c32140b549de20f061a2e562df9201c5daab4060fd1ca54a05f42e2"; FICHIERS_TESTS=""` |
| + | 461 | `# T08 : gardes avant tout calcul (« Liste d'arrêt », troisième puce ; consigne § 3.5) : aucun lecture-sondes-t06* ni resume.json sur` |
| + | 462 | `# l'instance, ni comme fichier ni comme objet git (garde du code, run de 7b lu dans la configuration) ; tête du dépôt = commit local,` |
| + | 463 | `# seul parent COMMIT = COMMIT_CODE_T08 de la configuration ;` |
| + | 464 | `# texte scellé intact et portant les marqueurs de la configuration (mode réel)` |
| + | 465 | `GARDES=$(PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src timeout -k 10 900 python - "$COMMIT" "$CONFIG" "$PREREG" "$PREREG_ABSENT" "$R/t08-liste-attendue.txt" <<'FIN_GARDES' 2>&1` |
| + | 466 | `import json, subprocess, sys` |
| + | 467 | `from controle_ia.gardes import GardeArret` |
| + | 468 | `from pathlib import Path` |
| + | 469 | `from controle_ia.lancement_t08 import commit_local_v1 as cl` |
| + | 470 | `from controle_ia.t08 import configuration_v1 as cf, entrees_v1 as en` |
| + | 471 | `commit, config, prereg, absent, liste = sys.argv[1:6]` |
| + | 472 | `try:` |
| + | 473 | `    c = json.load(open(config, encoding="utf-8"))` |
| + | 474 | `    run_7b = Path(c["entrees"]["manifeste_7b"]["chemin"]).parent.name` |
| + | 475 | `    inst = en.exiger_instance_sans_interdits(".", run_7b)` |
| + | 476 | `    cl.verifier(".", commit, Path(liste).read_text(encoding="utf-8").split())` |
| + | 477 | `    if c.get("mode") == "reel":` |
| + | 478 | `        m = cf.exiger_marqueurs(c.get("marqueurs"))` |
| + | 479 | `        if m["RUN_7B"]["run_id"] != run_7b:` |
| + | 480 | `            raise GardeArret(f"run de 7b des entrées {run_7b} ≠ RUN_7B de la configuration")` |
| + | 481 | `        if m["COMMIT_CODE_T08"] != commit:` |
| + | 482 | `            raise GardeArret(f"COMMIT_CODE_T08 de la configuration ≠ COMMIT {commit[:12]}")` |
| + | 483 | `        if absent == "1":` |
| + | 484 | `            raise GardeArret("configuration réelle sans préenregistrement")` |
| + | 485 | `        t = cf.exiger_marqueurs_au_texte(prereg, m)` |
| + | 486 | `        print(f"gardes conformes : {inst['fichiers']} fichiers, {inst['objets_git']} objets git, aucun interdit (run de 7b {run_7b}) ; tête = commit local, parent COMMIT = COMMIT_CODE_T08 ; texte {t['…` |
| + | 487 | `    else:` |
| + | 488 | `        print(f"gardes conformes (jouet) : {inst['fichiers']} fichiers, {inst['objets_git']} objets git, aucun interdit (run de 7b {run_7b}) ; tête = commit local, parent COMMIT")` |
| + | 489 | `except (GardeArret, cl.Ecart, OSError, ValueError, KeyError, subprocess.CalledProcessError) as e:` |
| + | 490 | `    print(f"ARRÊT : {e}")` |
| + | 491 | `    sys.exit(1)` |
| + | 492 | `FIN_GARDES` |
| + | 493 | `) \|\| { journal "gardes avant tout calcul : $(printf '%s' "$GARDES" \| tail -n 1)"; consigner_arret "gardes de l'instance"; refus "gardes avant tout calcul : $(printf '%s' "$GARDES" \| tail -n 1 \| c…` |
| + | 494 | `journal "$GARDES"` |
| + | 495 | `# T08 : suite ciblée et figée de T0.8 (liste de fichiers à l'empreinte et au nombre attendu écrits en dur) ; TESTS_ARGS (jouet seulement) a la priorité` |
| + | 496 | `LISTE_TESTS="scripts/tests-cibles-t08-v1.txt"; LISTE_SHA256="5b6db29b7434c3bd38c6178d04b790572e96f767c1ba36410694fcb2a0000c2c"; ATTENDUS="252"; FICHIERS_TESTS=""   # T08` |
| + | 497 | `[ -z "${TESTS_ARGS:-}" ] \|\| ATTENDUS="${TESTS_ATTENDUS:-}"   # T08 : répétition jouet seulement (TESTS_ARGS refusé hors jouet)` |

### Bloc 10 (modèle l. 485, copie l. 508)

**Raison** : § 3.5 : suite figée jouée sans l'essai du code aligné qui clone l'arbre entier du dépôt (désélection, comptée « 1 deselected ») ; « les modèles … chargés l'un après l'autre » (préchargés au cache local, la course les charge hors ligne) ; « la commande jouée : python -m controle_ia.t08.course_v1 --config … --run-id … --prereg …, une fois ».

| | l. | ligne |
|---|---|---|
| − | 488 | `if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no ${TESTS_ARGS:-} $FICHIERS_TESTS >"$T/tests.txt" 2>"$T/tests.err"; then` |
| + | 511 | `# T08 : un essai du code aligné clone l'arbre entier du dépôt ('git clone --depth 1' du dépôt courant) : sur l'instance, clone partiel,` |
| + | 512 | `# il tirerait du dépôt distant tout l'arbre de 'main' ; il est écarté de la suite figée (il se joue dans la session, arbre complet)` |
| + | 513 | `DESELECTION=(); [ -n "$FICHIERS_TESTS" ] && DESELECTION=(--deselect tests/test_t08_entrees_rendu_v1.py::test_amorce_instance_clone_de_l_arbre_aligne)` |
| + | 514 | `if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no "${DESELECTION[@]}" ${TESTS_ARGS:-} $FICHIERS_TESTS >"$T/tests.txt" 2>"$T/tests.err"; then` |
| − | 492 | `if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" \| grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then` |
| + | 518 | `DESEL=""; [ "${#DESELECTION[@]}" -gt 0 ] && DESEL=", 1 deselected"      # T08 : l'essai écarté est compté par pytest` |
| + | 519 | `if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" \| grep -Eq "^$ATTENDUS passed$DESEL(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then` |
| − | 495 | `ARGS=(); [ "$PREREG_ABSENT" = 1 ] && journal "répétition sans préenregistrement (jouet ou épreuve à blanc, non décisive)" \|\| ARGS=(--prereg "$PREREG")` |
| − | 496 | `RUN="$(date -u +%Y%m%d-%H%M%S)-t06-$MODE"` |
| − | 497 | `journal "run : $RUN (sans couperet de temps ; lanceur v6)"` |
| + | 522 | `ARGS=(); [ "$PREREG_ABSENT" = 1 ] && journal "répétition sans préenregistrement (jouet, non décisive)" \|\| ARGS=(--prereg "$PREREG")` |
| + | 523 | `# T08 : modèles au cache local (révisions de la configuration), l'un après l'autre ; la course les charge hors ligne` |
| + | 524 | `if [ "$MODE" = reel ]; then` |
| + | 525 | `    PYTHONPATH=src timeout -k 10 3600 python -c 'import json, sys` |
| + | 526 | `from controle_ia.harnais.modeles import precharger_modele` |
| + | 527 | `c = json.load(open(sys.argv[1], encoding="utf-8"))` |
| + | 528 | `vus = []` |
| + | 529 | `for spec in (c["agent"], c["juges"]["J8"], c["juges"]["J3"]):` |
| + | 530 | `    if (spec["modele"], spec["revision"]) not in vus:` |
| + | 531 | `        print(spec["modele"], precharger_modele(spec["modele"], spec["revision"]), flush=True)` |
| + | 532 | `        vus.append((spec["modele"], spec["revision"]))' "$CONFIG" > "$T/modeles.txt" 2>&1 \` |
| + | 533 | `        \|\| { journal "modèles : descente impossible : $(tail -n 1 "$T/modeles.txt" \| cut -c1-300)"; consigner_arret "descente des modèles"; arreter_instance "descente des modèles" 1; }` |
| + | 534 | `    journal "modèles au cache local : $(wc -l < "$T/modeles.txt") ligne(s)"` |
| + | 535 | `fi` |
| + | 536 | `RUN="$(date -u +%Y%m%d-%H%M%S)-t08-$MODE"   # T08` |
| + | 537 | `journal "run : $RUN (sans couperet de temps ; course de T0.8, une fois)"` |
| − | 499 | `PYTHONPATH=src python -m controle_ia.t06.lanceur_v6 --config "$CONFIG" --run-id "$RUN" "${ARGS[@]}" >"$T/run.json" 2>>"$T/run.err" &` |
| + | 539 | `HF_HUB_OFFLINE=1 PYTHONPATH=src python -m controle_ia.t08.course_v1 --config "$CONFIG" --run-id "$RUN" "${ARGS[@]}" >"$T/run.json" 2>>"$T/run.err" &   # T08 : la course de T0.8, une fois` |

### Bloc 11 (modèle l. 506, copie l. 546)

**Raison** : § 3.5 : fin du run reconnue sur le résultat de la course de T0.8 (course-t08.json) et son arrêt de garde (« ARRÊT : … ») au lieu de resume.json et arret.json de T0.6.

| | l. | ligne |
|---|---|---|
| − | 509 | `    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"` |
| − | 510 | `    elif [ -f "diag/$RUN/arret.json" ]; then` |
| + | 549 | `    if [ -f "diag/$RUN/course-t08.json" ] && ! grep -q '^ARRÊT : ' "$T/run.err"; then journal "run : code $code, mais course-t08.json écrit sans arrêt consigné : run complet"   # T08 : résultat de la …` |
| + | 550 | `    elif grep -q '^ARRÊT : ' "$T/run.err"; then   # T08 : arrêt de garde consigné par la course (« ARRÊT : <motif> », code 1)` |

### Bloc 12 (modèle l. 522, copie l. 562)

**Raison** : § 3.5 « la fin » : message de commit T0.8 ; morceaux d'activations retirés ; « les noms ».

| | l. | ligne |
|---|---|---|
| − | 525 | `etape_commit "T0.6 ($MODE), run $RUN : résultats et données légères" "" "aucun résultat léger à committer" \|\| ECHEC=1` |
| + | 565 | `etape_commit "T0.8 ($MODE), run $RUN : résultats et données de la course" "" "aucun résultat léger à committer" \|\| ECHEC=1` |
| − | 528 | `ajouter_morceaux \|\| ECHEC=1` |
| − | 529 | `commit_verifie "T0.6 ($MODE), run $RUN : sous-ensemble d'activations en morceaux (< $MORCEAU_MAX octets chacun)"; rc_m=$?` |
| − | 530 | `case "$rc_m" in` |
| − | 531 | `    0) journal "morceaux committés : $(git show --stat --format= HEAD \| grep -c 'activations-sous-ensemble-t06-[0-9]' \|\| true) fichier(s)"` |
| − | 532 | `       pousser \|\| journal "poussée des morceaux impossible : morceaux restés sur l'instance";;` |
| − | 533 | `    10) journal "aucun morceau à committer";;` |
| − | 534 | `    *) ECHEC=1;;` |
| − | 535 | `esac` |
| + | 568 | `# T08 : aucun morceau d'activations (bras propre à la course de confirmation, retiré)` |
| − | 538 | `[ ! -s "$R/t06-fichiers-trop-gros.txt" ] \|\| { journal "ERREUR DE CHAÎNE (C-V4-1) : fichier(s) trop gros retiré(s) du commit, restés sur l'instance : $(head -n 3 "$R/t06-fichiers-trop-gros.txt" \| tr…` |
| + | 571 | `[ ! -s "$R/t08-fichiers-trop-gros.txt" ] \|\| { journal "ERREUR DE CHAÎNE (C-V4-1) : fichier(s) trop gros retiré(s) du commit, restés sur l'instance : $(head -n 3 "$R/t08-fichiers-trop-gros.txt" \| tr…` |

### Bloc 13 (modèle l. 549, copie l. 582)

**Raison** : § 3.5 « la fin » : « les noms » ; bras B retiré de la fin normale. Contre-lecture M-3 : fin normale, destruction après le versement prouvé, sinon arrêt (disque gardé).

| | l. | ligne |
|---|---|---|
| − | 552 | `echo "fin normale $(date -u +%FT%TZ), run $RUN" > "$R/t06-fin-normale"` |
| − | 553 | `if pousser; then journal "branche $BRANCHE poussée (résultats, données légères, morceaux et traces)"; liberer_verrou; bras_b \|\| true; arreter_instance "fin du run" 0; fi` |
| + | 585 | `echo "fin normale $(date -u +%FT%TZ), run $RUN" > "$R/t08-fin-normale"` |
| + | 586 | `if pousser; then journal "branche $BRANCHE poussée (résultats, données de la course et traces)"; liberer_verrou   # T08 : sans bras B` |
| + | 587 | `    # T08 (M-3) : destruction après le versement prouvé (tête locale = tête distante de la branche de sortie) ; sinon arrêt, disque gardé` |
| + | 588 | `    if versement_prouve "$BRANCHE"; then journal "versement prouvé : $(git rev-parse HEAD) = origin/$BRANCHE"; detruire "fin normale : versement prouvé, destruction par l'identifiant (M-3)" 0; fi` |
| + | 589 | `    journal "poussée faite, mais versement non prouvé (tête distante ≠ tête locale) : arrêt, disque gardé"; arreter_instance "versement non prouvé" 1` |
| + | 590 | `fi` |

