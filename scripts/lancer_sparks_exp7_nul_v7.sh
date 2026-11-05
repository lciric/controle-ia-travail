#!/usr/bin/env bash
# v7 (R12, minimale) : copie du lanceur v6 ; garde du code v7 et amorce v7.
# v6 (R12, minimale) : copie du lanceur v5 ; garde du code v6, amorce v6 ; date du contrôle du GO du tir réglable
# (`SPARKS_DATE_TIR`, AAAA-MM-JJ ; défaut : aujourd'hui), pour un essai indépendant de la date.
# Lanceur de SPARKS-EXP7-NUL, v5 (version neuve du lanceur v4, R12 ; contre-lecture du delta v4, points 14 à 18 et 23).
# Depuis la session : vérifie, puis imprime les commandes LITTÉRALES (`vastai create|start|destroy`), que
# `.claude/hooks/garde_calcul.py` voit et dont il revérifie le GO. Chaque commande imprimée :
#   - tourne sous `timeout` (create et start 300 s, destroy et inventaire 120 s) ;
#   - passe à `vastai` un environnement nettoyé (`env -i`) qui garde PATH, HOME, LANG et, s'ils sont présents, VAST_API_KEY
#     (la clé que `vastai` lit, R-032), HTTPS_PROXY, HTTP_PROXY, NO_PROXY, SSL_CERT_FILE, REQUESTS_CA_BUNDLE (R-1497), par
#     leur nom seulement, jamais leur valeur ;
#   - redirige la sortie de `vastai` vers un fichier jamais affiché (R-1480) ; `apres-creation` et `apres-commande` n'en
#     tirent que le code, l'identifiant, et « refusé » ou « envoyé » : `vastai` 1.8.3 rend ses refus avec le code 0, sur
#     stderr avec `--raw` (R-1506), donc un code 0 ne prouve rien ; l'identifiant rendu avec « success » vrai est testé
#     AVANT toute erreur de certificat ; un `start` ou un `destroy` n'est tenu pour fait qu'après l'inventaire filtré
#     (`inventaire` : seuls l'identifiant et l'état sont imprimés) ;
#   - prend l'amorce au commit lancé (`git show "$COMMIT:…"`), et passe `ADDENDUM_SHA256` (empreinte de l'addendum scellé au
#     commit lancé), que l'amorce exige en mode réel.
# Mode « tir » : tir réel de la minuterie et des redémarrages avant le scellement, sous une ligne de GO à part (GO_ID en
# paramètre, plafond ≤ 5 USD, `tir.py`), avec une commande écrite pas à pas (section 5 du rapport v5).
# Usage :
#   bash scripts/lancer_sparks_exp7_nul_v7.sh creation <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json> [ECHEANCE_UTC_S]
#   bash scripts/lancer_sparks_exp7_nul_v7.sh redemarrage <ID> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json>
#   bash scripts/lancer_sparks_exp7_nul_v7.sh destruction <ID>
#   bash scripts/lancer_sparks_exp7_nul_v7.sh tir <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT_CODE> <GO_ID_DU_TIR> [MINUTES]
#   bash scripts/lancer_sparks_exp7_nul_v7.sh apres-creation <FICHIER> <CODE>
#   bash scripts/lancer_sparks_exp7_nul_v7.sh apres-commande <start|destroy> <FICHIER> <CODE> <ID>
#   bash scripts/lancer_sparks_exp7_nul_v7.sh inventaire <FICHIER> <ID> <absente|exited|running>
# État de la session : SPARKS_ETAT_DIR (défaut ~/.sparks-exp7-nul-v5). Registre des GO du tir : SPARKS_REGISTRE_GO.
set -euo pipefail
ETAT_DIR="${SPARKS_ETAT_DIR:-$HOME/.sparks-exp7-nul-v5}"
MARQUEUR="$ETAT_DIR/.creation-incertaine"
QUOI="${1:?creation, redemarrage, destruction, tir, apres-creation, apres-commande ou inventaire}"
CERT='CERTIFICATE_VERIFY_FAILED|certificate verify failed|SSLError|SSLCertVerificationError'
REFUS='failed with error|error [0-9]{3}|"success"[[:space:]]*:[[:space:]]*false|Traceback|Error:'
prefixe_env() {   # env -i … avec la clé de Vast et les variables du mandataire présentes, par leur nom seulement
    local p='env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8' v
    for v in VAST_API_KEY HTTPS_PROXY HTTP_PROXY NO_PROXY SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
        [ -n "${!v:-}" ] && p="$p $v=\"\$$v\""
    done
    printf '%s' "$p"
}
identifiant() { case "${1:-}" in ''|*[!0-9]*) echo "identifiant d'instance : chiffres seuls (R10)" >&2; exit 2;; esac; }
court() { case "${1:-}" in *[!0-9a-f]*|'') echo "commit illisible" >&2; exit 2;; esac; [ "${#1}" = 40 ] || { echo "commit de 40 caractères" >&2; exit 2; }; printf '%s' "${1:0:12}"; }
inventaire_cmd() {  # $1 ID, $2 attendu
    echo "timeout -k 10 120 $(prefixe_env) vastai show instance $1 --raw > \"$ETAT_DIR/inventaire-$1.txt\" 2>&1; bash scripts/lancer_sparks_exp7_nul_v7.sh inventaire \"$ETAT_DIR/inventaire-$1.txt\" $1 $2"
}
case "$QUOI" in
apres-creation)
    F="${2:?fichier de sortie}"; C="${3:?code}"; mkdir -p "$ETAT_DIR"
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then      # l'identifiant d'abord (point 17)
        echo "$ID" > "$ETAT_DIR/instance-$(date -u +%Y%m%dT%H%M%S).txt"; echo "CRÉÉE : instance $ID (sortie de vastai non affichée)"
        echo "Inventaire à suivre : $(inventaire_cmd "$ID" exited)"; exit 0
    fi
    if [ -z "$ID" ] && grep -qiE "$CERT" "$F" 2>/dev/null; then
        echo "CRÉATION NON PARVENUE (erreur de certificat, aucun identifiant rendu) : refus, aucun marqueur"; exit 3
    fi
    echo "code $C $(date -u +%FT%TZ)" > "$MARQUEUR"
    echo "CRÉATION INCERTAINE (code $C) : marqueur $MARQUEUR posé ; aucune seconde création avant un inventaire sans sortie brute"; exit 4 ;;
apres-commande)
    Q="${2:?start ou destroy}"; F="${3:?fichier}"; C="${4:?code}"; identifiant "${5:-}"
    case "$Q" in start) ATT=running ;; destroy) ATT=absente ;; *) echo "start ou destroy" >&2; exit 2 ;; esac
    if grep -qiE "$CERT" "$F" 2>/dev/null; then echo "$Q $5 NON PARVENU (erreur de certificat)"; R=3
    elif grep -qiE "$REFUS" "$F" 2>/dev/null; then echo "$Q $5 REFUSÉ par vastai (code $C ; refus lu dans la sortie, non affichée)"; R=5
    else echo "$Q $5 ENVOYÉ (code $C) : rien n'est tenu pour fait avant l'inventaire"; R=0; fi
    echo "Inventaire : $(inventaire_cmd "$5" "$ATT")"; exit "$R" ;;
inventaire)
    F="${2:?fichier}"; identifiant "${3:-}"; ATT="${4:?absente, exited ou running}"
    ETAT=$(grep -oE '"actual_status"[[:space:]]*:[[:space:]]*"[a-z_]+"' "$F" 2>/dev/null | head -1 | grep -oE '"[a-z_]+"$' | tr -d '"' || true)
    if [ -z "$ETAT" ]; then
        if grep -qiE 'no_such_instance|not found|404|"instances"[[:space:]]*:[[:space:]]*\[\]|^\[\]$' "$F" 2>/dev/null; then ETAT=absente; else ETAT=illisible; fi
    fi
    ETAT_C=$(grep -oE '"cur_state"[[:space:]]*:[[:space:]]*"[a-z_]+"' "$F" 2>/dev/null | head -1 | grep -oE '"[a-z_]+"$' | tr -d '"' || true)
    echo "INVENTAIRE : instance $3, état $ETAT${ETAT_C:+ (cur_state $ETAT_C)}, attendu $ATT"
    [ "$ETAT" = "$ATT" ] && exit 0 || exit 6 ;;
destruction)
    identifiant "${2:-}"; mkdir -p "$ETAT_DIR"
    echo "Commande de destruction (sans -y, vastai 1.8.3 ne détruit rien, R-1482 ; sortie non affichée, R-1480) :"
    echo "timeout -k 10 120 $(prefixe_env) vastai destroy instance $2 -y > \"$ETAT_DIR/destruction-$2.txt\" 2>&1; bash scripts/lancer_sparks_exp7_nul_v7.sh apres-commande destroy \"$ETAT_DIR/destruction-$2.txt\" \$? $2"
    exit 0 ;;
esac
cd "$(dirname "$0")/.."
P2=src/controle_ia/sparks_exp7_nul_v2; P5=src/controle_ia/sparks_exp7_nul_v5
mkdir -p "$ETAT_DIR"
if [ "$QUOI" = tir ]; then
    OFFRE="${2:?offre}"; PRIX="${3:?prix carte}"; STOCK="${4:?prix stockage}"; CODE="${5:?commit du code}"; GOT="${6:?GO_ID du tir}"
    MIN="${7:-25}"; COURT=$(court "$CODE")
    [ -e "$MARQUEUR" ] && { echo "création incertaine antérieure ($MARQUEUR) : inventaire d'abord" >&2; exit 2; }
    timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v7'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" liste . "$CODE"
    REG=$(realpath "${SPARKS_REGISTRE_GO:-registres/go.md}")
    L=$(timeout 120 python3 -I -B "$P5/tir.py" verifier "$REG" "$GOT" "$PRIX" "$STOCK" "$MIN" ${SPARKS_DATE_TIR:+"$SPARKS_DATE_TIR"})
    ECH=$(printf '%s' "$L" | sed -n 's/^ECHEANCE_UTC_S=\([0-9]*\) .*/\1/p'); echo "TIR CONFORME : $L"
    F="$ETAT_DIR/tir-creation-$COURT-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Tir réel (section 5 du rapport v5), à jouer pas à pas par la session ; aucun modèle, aucune donnée, aucun jeton Hugging Face.
0. Commit de tir (code $COURT + registre des GO de main, SANS addendum : la création s'arrête d'elle-même à la garde du code) :
   T=\$(mktemp -d); git worktree add -q --no-checkout -b essai/sparks-v5-tir-$COURT "\$T/tir" $CODE
   git -C "\$T/tir" sparse-checkout set --no-cone '/*' '!/*/' '/registres/go.md' && git -C "\$T/tir" checkout -q essai/sparks-v5-tir-$COURT
   cp "$REG" "\$T/tir/registres/go.md" && git -C "\$T/tir" commit -qam "essai : tir v5 (sans addendum)" && timeout 300 git -C "\$T/tir" push -q origin essai/sparks-v5-tir-$COURT
   TIR=\$(git -C "\$T/tir" rev-parse HEAD)
1. Création (échéance de la minuterie dans $MIN min ; étiquette de tir ; disque réduit) :
GO_ID=$GOT timeout -k 10 300 $(prefixe_env) vastai create instance $OFFRE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 20 --label sparks-exp7-nul-tir-$COURT \\
  --env "-e COMMIT=\$TIR -e COMMIT_CODE=$CODE -e PRIX_HEURE_USD=$PRIX -e PRIX_STOCKAGE_HEURE_USD=$STOCK -e ECHEANCE_UTC_S=$ECH -e GH_TOKEN=\$GH_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(git show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v7.sh")" > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v7.sh apres-creation "$F" \$?
   ID=<identifiant rendu>
2. Après 5 à 8 min : inventaire attendu « exited » (le conteneur sort quand l'amorce sort) :
   $(inventaire_cmd '$ID' exited)
   Journal de l'amorce, lignes « AMORCE V5 » seules (outils présents, minuterie lancée, refus à la garde du code) :
   timeout -k 10 120 $(prefixe_env) vastai logs \$ID --tail 80 > "$ETAT_DIR/tir-logs-1.txt" 2>&1; grep -E '^AMORCE V5' "$ETAT_DIR/tir-logs-1.txt"
   Facturation d'une instance « exited » : champs filtrés seuls (aucune autre sortie) :
   timeout -k 10 120 $(prefixe_env) vastai show instance \$ID --raw > "$ETAT_DIR/tir-inv-2.txt" 2>&1; grep -oE '"(actual_status|cur_state|dph_total|storage_cost|disk_space)"[[:space:]]*:[[:space:]]*[^,}]*' "$ETAT_DIR/tir-inv-2.txt"
3. Ordre « fin » pour cette instance, sur la branche des ordres du commit de tir :
   O=\$(mktemp -d); git -C "\$O" init -q; git -C "\$O" remote add origin https://github.com/lciric/controle-ia-travail.git; mkdir "\$O/ordres"
   echo "{\"numero\": 1, \"instance\": \"\$ID\", \"phase\": \"fin\", \"deja_usd\": 0}" > "\$O/ordres/ordre-001.json"
   git -C "\$O" add ordres && git -C "\$O" -c user.name=essai -c user.email=essai@invalid commit -qm "essai : ordre de tir" && timeout 300 git -C "\$O" push -q origin "HEAD:refs/heads/ordres/sparks-exp7-nul-v5-\${TIR:0:12}"
4. Relance (même environnement) ; la machine lit l'ordre « fin » et se détruit par la clé du conteneur :
GO_ID=$GOT timeout -k 10 300 $(prefixe_env) vastai start instance \$ID > "$ETAT_DIR/tir-start.txt" 2>&1; bash scripts/lancer_sparks_exp7_nul_v7.sh apres-commande start "$ETAT_DIR/tir-start.txt" \$? \$ID
5. Après 3 à 5 min : inventaire attendu « absente » (destruction par la machine, aucune par la session) :
   $(inventaire_cmd '$ID' absente)
6. Repli si l'instance existe encore à l'échéance + 10 min : bash scripts/lancer_sparks_exp7_nul_v7.sh destruction \$ID (puis l'inventaire qu'il imprime).
7. vastai copy : non éprouvé par ce tir (aucun lot sans fabrication, conteneur sorti) ; risque déclaré.
Devis : $(printf '%s' "$L" | sed -n 's/.*DEVIS_USD=\([0-9.]*\).*/\1/p') USD au plus, sous $GOT.
FIN
    exit 0
fi
CIBLE="${2:?offre ou identifiant}"; PRIX="${3:?prix carte}"; STOCK="${4:?prix stockage}"
COMMIT="${5:?commit lancé}"; CODE="${6:?commit du code}"; ETAT="${7:?état de dépense}"; ECH="${8:-1795046400}"
case "$ECH" in ''|*[!0-9]*) echo "ECHEANCE_UTC_S non entière" >&2; exit 2;; esac
[ "$ECH" -le 1795046400 ] || { echo "échéance au-delà de la fin du 18 novembre : refus" >&2; exit 2; }
COURT=$(court "$COMMIT")
if [ "$QUOI" = creation ] && [ -e "$MARQUEUR" ]; then
    echo "création incertaine antérieure ($MARQUEUR) : inventaire sans sortie brute d'abord, puis retrait du marqueur par la session" >&2; exit 2
fi
[ "$QUOI" = redemarrage ] && identifiant "$CIBLE"
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import go; sys.exit(go.main(['registres/go.md']))"
PYTHONPATH=src timeout 120 python3 -B -m controle_ia.scellement verifier prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v7'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$CODE" "$COMMIT"
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import depense; sys.exit(depense.main(sys.argv[1:]))" projeter "$ETAT"
if [ "$QUOI" = creation ]; then
    SHA_A=$(git show "$COMMIT:prereg/SPARKS-EXP7-NUL-addendum-1.md" | sha256sum | cut -c1-64)
    F="$ETAT_DIR/creation-$COURT-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Commande de création à lancer par la session (sortie de vastai jamais affichée ; jetons lus de l'environnement) :
GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai create instance $CIBLE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 120 --label sparks-exp7-nul-v5-$COURT \\
  --env "-e COMMIT=$COMMIT -e COMMIT_CODE=$CODE -e ADDENDUM_SHA256=$SHA_A -e PRIX_HEURE_USD=$PRIX -e PRIX_STOCKAGE_HEURE_USD=$STOCK -e ECHEANCE_UTC_S=$ECH -e GH_TOKEN=\$GH_TOKEN -e HF_TOKEN=\$HF_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v7.sh")" > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v7.sh apres-creation "$F" \$?
Avant la création : tir réel (mode « tir ») ; image : curl et git présents (l'amorce refuse sinon).
FIN
elif [ "$QUOI" = redemarrage ]; then
    F="$ETAT_DIR/demarrage-$CIBLE-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Redémarrage sur ordre écrit :
1. écrire ordres/ordre-NNN.json (numéro neuf ; "instance": "$CIBLE" ; deja_usd = dépense cumulée de l'état, jamais plus basse ;
   copie : cas, premier, copie_minutes ; causal : ordres/causal/cle-ouverte-v1.json et ordres/causal/reponses/…, scellés)
   sur la branche ordres/sparks-exp7-nul-v5-$COURT (jamais sous calcul/), committer, pousser ;
2. GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai start instance $CIBLE > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v7.sh apres-commande start "$F" \$? $CIBLE
3. copie : vastai copy (sous timeout, sortie non affichée) de $CIBLE:/root/sparks/lots/lot-NNN/ vers un dossier hors du servi,
   puis sha256sum -c MANIFESTE-LOT.txt ; le conteneur sort seul après copie_minutes ;
4. causal ou fin : la machine se détruit elle-même (minuterie, après poussée vérifiée) ; inventaire attendu « absente » ;
   repli : bash scripts/lancer_sparks_exp7_nul_v7.sh destruction $CIBLE
FIN
else echo "creation, redemarrage, destruction, tir, apres-creation, apres-commande ou inventaire" >&2; exit 2; fi
