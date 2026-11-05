#!/usr/bin/env bash
# v10 (R12 ; tir réel v9 : boucle de redémarrage, image sans curl) : copie du lanceur v9 ; garde du code v10, amorce v10,
# `vast_lecture` v10 (`journal-amorce FICHIER [ATTENDUS]` compte les lignes de démarrage, v10 et anciennes, et rend la
# boucle) ; second tir : l'amorce v10 refuse à la garde du code (aucun addendum) et **se détruit** ; attente de 300 s avant
# la destruction (`AMORCE_ATTENTE_REFUS_S`) pour lire son journal.
# v9 (R12 ; contre-lecture du delta v5 → v8, points 10 à 18 et 31 ; consigne de la mère, a) : copie du lanceur v8.
#   - `recherche` imprime la recherche d'offres ; `offres` la filtre (`vast_lecture.py` : « gpu », une carte, prix croissant,
#     au plus 4) et écrit les prix tirés de l'offre selon la règle écrite (PRIX_CARTE = dph_total ; PRIX_STOCKAGE =
#     storage_cost × 20 ÷ 730) ; le tir prend l'offre de son rang (`tir <COMMIT_CODE> <GO_ID> [MINUTES] [RANG]`) ;
#   - jeton passé à l'instance écrit dans la commande : `GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN` (comme R1 v4 ; N-009) ;
#   - inventaire par `vastai show instances --raw` (sortie d'erreur à part), lu en JSON strict et filtré par identifiant ;
#     `{"instances": null}` = absente ; aucun motif « 404 » ;
#   - boucle de redémarrage : trois inventaires sur au moins 5 minutes, verdict `boucle` (arrêtée, absente, indécis,
#     boucle) ; une boucle constatée : destruction par l'identifiant avec `-y`, puis nœud ;
#   - sorties brutes de `vastai` effacées après lecture (création, commandes, inventaires, offres, journaux) ;
#   - « no_such_ask » sans identifiant : refus net, aucun marqueur, offre suivante (rang + 1, au plus 4) ;
#   - `start` (ou `destroy`) tenu pour envoyé seulement sur « starting instance <ID>. » (ou « destroying instance <ID>. ») ;
#   - `tir.py` v9 : ligne de GO dont le périmètre nomme « SPARKS » et « tir » ;
#   - lignes de l'amorce lues dans `vastai logs` sans ancre (`journal-amorce`).
# v8 (R12, minimale) : copie du lanceur v7 ; garde du code v8 et amorce v8.
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
#   bash scripts/lancer_sparks_exp7_nul_v10.sh creation <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json> [ECHEANCE_UTC_S]
#   bash scripts/lancer_sparks_exp7_nul_v10.sh redemarrage <ID> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json>
#   bash scripts/lancer_sparks_exp7_nul_v10.sh destruction <ID>
#   bash scripts/lancer_sparks_exp7_nul_v10.sh recherche ; … offres <FICHIER_BRUT>
#   bash scripts/lancer_sparks_exp7_nul_v10.sh tir <COMMIT_CODE> <GO_ID_DU_TIR> [MINUTES] [RANG]
#   bash scripts/lancer_sparks_exp7_nul_v10.sh apres-commande <start|destroy> <FICHIER> <CODE> <ID>
#   bash scripts/lancer_sparks_exp7_nul_v10.sh apres-creation <FICHIER> <CODE> [<COMMIT_CODE> <GO_ID> <MINUTES> <RANG>]
#   bash scripts/lancer_sparks_exp7_nul_v10.sh inventaire <FICHIER> <ID> <absente|exited|running> ; … boucle <ID> ; … journal-amorce <FICHIER>
# État de la session : SPARKS_ETAT_DIR (défaut ~/.sparks-exp7-nul-v5). Registre des GO du tir : SPARKS_REGISTRE_GO.
set -euo pipefail
ETAT_DIR="${SPARKS_ETAT_DIR:-$HOME/.sparks-exp7-nul-v5}"
ICI="$(cd "$(dirname "$0")/.." && pwd)"
LECT="$ICI/src/controle_ia/sparks_exp7_nul_v10/vast_lecture.py"
MARQUEUR="$ETAT_DIR/.creation-incertaine"
QUOI="${1:?creation, redemarrage, destruction, recherche, offres, tir, apres-creation, apres-commande, inventaire, boucle ou journal-amorce}"
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
inventaire_cmd() {  # $1 ID, $2 attendu : liste de toutes les instances, JSON strict, filtrée par identifiant ; brut effacé
    echo "timeout -k 10 120 $(prefixe_env) vastai show instances --raw > \"$ETAT_DIR/inventaire-$1.json\" 2> \"$ETAT_DIR/inventaire-$1.json.err\"; bash scripts/lancer_sparks_exp7_nul_v10.sh inventaire \"$ETAT_DIR/inventaire-$1.json\" $1 $2"
}
effacer() { rm -f -- "$1" "$1.err"; }
case "$QUOI" in
apres-creation)
    F="${2:?fichier de sortie}"; C="${3:?code}"; mkdir -p "$ETAT_DIR"
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    NSA=$(grep -ciE 'no_such_ask' "$F" 2>/dev/null || true); CERT_VU=$(grep -ciE "$CERT" "$F" 2>/dev/null || true)
    effacer "$F"                                            # sortie brute lue puis effacée (point 16)
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then      # l'identifiant d'abord (point 17)
        echo "$ID" > "$ETAT_DIR/instance-$(date -u +%Y%m%dT%H%M%S).txt"; echo "CRÉÉE : instance $ID (sortie de vastai non affichée)"
        echo "Inventaire à suivre : $(inventaire_cmd "$ID" exited)"; exit 0
    fi
    if [ -z "$ID" ] && [ "${OK:-0}" = 0 ] && [ "${NSA:-0}" -ge 1 ]; then   # point 14 : refus net de Vast, rien créé
        echo "OFFRE RETIRÉE (no_such_ask, aucun identifiant rendu) : rien créé, aucun marqueur"
        case "${4:-}:${5:-}:${6:-}:${7:-}" in
            [0-9a-f]*:GO-*:*:[1-3]) echo "Offre suivante (rang $(( $7 + 1 )) sur 4 au plus) : bash scripts/lancer_sparks_exp7_nul_v10.sh tir $4 $5 $6 $(( $7 + 1 ))" ;;
            *:*:*:4) echo "Quatre offres essayées : nouvelle recherche (bash scripts/lancer_sparks_exp7_nul_v10.sh recherche)" ;;
        esac
        exit 7
    fi
    if [ -z "$ID" ] && [ "${CERT_VU:-0}" -ge 1 ]; then
        echo "CRÉATION NON PARVENUE (erreur de certificat, aucun identifiant rendu) : refus, aucun marqueur"; exit 3
    fi
    echo "code $C $(date -u +%FT%TZ)" > "$MARQUEUR"
    echo "CRÉATION INCERTAINE (code $C) : marqueur $MARQUEUR posé ; aucune seconde création avant un inventaire sans sortie brute"; exit 4 ;;
apres-commande)
    Q="${2:?start ou destroy}"; F="${3:?fichier}"; C="${4:?code}"; identifiant "${5:-}"
    case "$Q" in start) ATT=running ;; destroy) ATT=absente ;; *) echo "start ou destroy" >&2; exit 2 ;; esac
    case "$Q" in start) MOT="starting instance $5." ;; destroy) MOT="destroying instance $5." ;; esac
    if grep -qiE "$CERT" "$F" 2>/dev/null; then echo "$Q $5 NON PARVENU (erreur de certificat)"; R=3
    elif grep -qxF "$MOT" "$F" 2>/dev/null && ! grep -qiE "$REFUS" "$F" 2>/dev/null; then
        echo "$Q $5 ENVOYÉ (code $C ; « $MOT » lu) : rien n'est tenu pour fait avant l'inventaire"; R=0
    else echo "$Q $5 REFUSÉ par vastai (code $C ; « $MOT » absent de la sortie, non affichée)"; R=5; fi   # point 15
    effacer "$F"
    echo "Inventaire : $(inventaire_cmd "$5" "$ATT")"; exit "$R" ;;
inventaire)
    F="${2:?fichier}"; identifiant "${3:-}"; ATT="${4:?absente, exited ou running}"; mkdir -p "$ETAT_DIR"
    R=0; python3 -I -B "$LECT" inventaire "$F" "$3" "$ATT" "$ETAT_DIR/etats-$3.txt" || R=$?; effacer "$F"; exit "$R" ;;
boucle)
    identifiant "${2:-}"
    R=0; python3 -I -B "$LECT" boucle "$ETAT_DIR/etats-$2.txt" "$2" || R=$?
    case "$R" in
        8) echo "BOUCLE CONSTATÉE : destruction par l'identifiant, puis NŒUD (aucune création sous ce texte) :"
           echo "timeout -k 10 120 $(prefixe_env) vastai destroy instance $2 -y > \"$ETAT_DIR/destruction-$2.txt\" 2>&1; bash scripts/lancer_sparks_exp7_nul_v10.sh apres-commande destroy \"$ETAT_DIR/destruction-$2.txt\" \$? $2" ;;
        6) echo "Indécis : il faut trois inventaires sur au moins 5 minutes (le suivant : $(inventaire_cmd "$2" exited))" ;;
    esac
    exit "$R" ;;
journal-amorce)
    F="${2:?fichier}"; R=0; python3 -I -B "$LECT" journal-amorce "$F" "${3:-1}" || R=$?; effacer "$F"; exit "$R" ;;
recherche)
    mkdir -p "$ETAT_DIR"
    echo "Recherche d'offres (lecture seule ; sortie brute effacée après filtrage) :"
    echo "timeout -k 10 120 $(prefixe_env) vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw > \"$ETAT_DIR/offres-brutes.json\" 2> \"$ETAT_DIR/offres-brutes.json.err\"; bash scripts/lancer_sparks_exp7_nul_v10.sh offres \"$ETAT_DIR/offres-brutes.json\""
    exit 0 ;;
offres)
    F="${2:?fichier}"; mkdir -p "$ETAT_DIR"
    R=0; python3 -I -B "$LECT" offres "$F" "$ETAT_DIR/offres-retenues.json" || R=$?; effacer "$F"; exit "$R" ;;
destruction)
    identifiant "${2:-}"; mkdir -p "$ETAT_DIR"
    echo "Commande de destruction (sans -y, vastai 1.8.3 ne détruit rien, R-1482 ; sortie non affichée, R-1480) :"
    echo "timeout -k 10 120 $(prefixe_env) vastai destroy instance $2 -y > \"$ETAT_DIR/destruction-$2.txt\" 2>&1; bash scripts/lancer_sparks_exp7_nul_v10.sh apres-commande destroy \"$ETAT_DIR/destruction-$2.txt\" \$? $2"
    exit 0 ;;
esac
cd "$(dirname "$0")/.."
P2=src/controle_ia/sparks_exp7_nul_v2; P5=src/controle_ia/sparks_exp7_nul_v5; P9=src/controle_ia/sparks_exp7_nul_v9
mkdir -p "$ETAT_DIR"
if [ "$QUOI" = tir ]; then
    CODE="${2:?commit du code}"; GOT="${3:?GO_ID du tir}"; MIN="${4:-25}"; RANG="${5:-1}"; COURT=$(court "$CODE")
    case "$RANG" in [1-4]) ;; *) echo "rang de l'offre : 1 à 4" >&2; exit 2;; esac
    [ -e "$MARQUEUR" ] && { echo "création incertaine antérieure ($MARQUEUR) : inventaire d'abord" >&2; exit 2; }
    [ -s "$ETAT_DIR/offres-retenues.json" ] || { echo "aucune offre retenue : bash scripts/lancer_sparks_exp7_nul_v10.sh recherche, d'abord" >&2; exit 2; }
    LO=$(timeout 60 python3 -I -B "$LECT" offre "$ETAT_DIR/offres-retenues.json" "$RANG") || { echo "pas d'offre au rang $RANG : nouvelle recherche" >&2; exit 2; }
    OFFRE=$(printf '%s' "$LO" | sed -n 's/^OFFRE=\([0-9]*\) .*/\1/p'); PRIX=$(printf '%s' "$LO" | sed -n 's/.* PRIX_CARTE=\([0-9.e-]*\) .*/\1/p')
    STOCK=$(printf '%s' "$LO" | sed -n 's/.* PRIX_STOCKAGE=\([0-9.e-]*\)$/\1/p')
    [ -n "$OFFRE" ] && [ -n "$PRIX" ] && [ -n "$STOCK" ] || { echo "offre retenue mal lue" >&2; exit 2; }
    timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v10'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" liste . "$CODE"
    REG=$(realpath "${SPARKS_REGISTRE_GO:-registres/go.md}")
    L=$(timeout 120 python3 -I -B "$P9/tir.py" verifier "$REG" "$GOT" "$PRIX" "$STOCK" "$MIN" ${SPARKS_DATE_TIR:+"$SPARKS_DATE_TIR"})
    ECH=$(printf '%s' "$L" | sed -n 's/^ECHEANCE_UTC_S=\([0-9]*\) .*/\1/p'); echo "TIR CONFORME : offre $OFFRE (rang $RANG), PRIX_CARTE $PRIX, PRIX_STOCKAGE $STOCK ; $L"
    F="$ETAT_DIR/tir-creation-$COURT-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Tir réel v9, à jouer pas à pas par la session ; aucun modèle, aucune donnée, aucun jeton Hugging Face.
Offre $OFFRE (rang $RANG des offres retenues, $ETAT_DIR/offres-retenues.json) ; prix tirés de l'offre : $(timeout 60 python3 -I -B -c "import sys; sys.path.insert(0, '$(dirname "$LECT")'); import vast_lecture as v; print(v.REGLE)").
0. Commit de tir (code $COURT + registre des GO de main, SANS addendum : la création s'arrête d'elle-même à la garde du code) :
   T=\$(mktemp -d); git worktree add -q --no-checkout -b essai/sparks-v9-tir-$COURT "\$T/tir" $CODE
   git -C "\$T/tir" sparse-checkout set --no-cone '/*' '!/*/' '/registres/go.md' && git -C "\$T/tir" checkout -q essai/sparks-v9-tir-$COURT
   cp "$REG" "\$T/tir/registres/go.md" && git -C "\$T/tir" commit -qam "essai : tir v9 (sans addendum)" && timeout 300 git -C "\$T/tir" push -q origin essai/sparks-v9-tir-$COURT
   TIR=\$(git -C "\$T/tir" rev-parse HEAD)
1. Création (échéance de la minuterie dans $MIN min ; étiquette de tir ; disque de 20 Go ; jeton de l'instance : CONTROLE_IA_GITHUB_TOKEN) :
GO_ID=$GOT timeout -k 10 300 $(prefixe_env) vastai create instance $OFFRE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 20 --label sparks-exp7-nul-tir-$COURT \\
  --env "-e COMMIT=\$TIR -e COMMIT_CODE=$CODE -e PRIX_HEURE_USD=$PRIX -e PRIX_STOCKAGE_HEURE_USD=$STOCK -e ECHEANCE_UTC_S=$ECH -e AMORCE_ATTENTE_REFUS_S=300 -e GH_TOKEN=\$CONTROLE_IA_GITHUB_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(git show "$CODE:scripts/amorce_instance_sparks_exp7_nul_v10.sh")" > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v10.sh apres-creation "$F" \$? $CODE $GOT $MIN $RANG
   ID=<identifiant rendu> ; sur « OFFRE RETIRÉE » : la commande de l'offre suivante est imprimée (au plus 4 offres).
2. Entre T+3 et T+5 min (l'amorce v10 attend 300 s avant de se détruire) : journal de l'amorce, lignes « AMORCE V » seules,
   sans ancre, démarrages comptés (attendus : 1) ; sortie brute effacée :
   timeout -k 10 120 $(prefixe_env) vastai logs \$ID --tail 400 > "$ETAT_DIR/tir-logs.txt" 2>&1; bash scripts/lancer_sparks_exp7_nul_v10.sh journal-amorce "$ETAT_DIR/tir-logs.txt" 1
   Attendus : « AMORCE V10 DEMARRAGE 1 », « outils » (installés s'il le faut), « code ou addendum non conformes : aucun calcul :
   refus avant l'ordre consommé », « attente de 300 s », DEMARRAGES=1, BOUCLE=non.
3. À T+10 min au plus : inventaire attendu « absente » (destruction par la machine, clé du conteneur) :
   $(inventaire_cmd '$ID' absente)
   Sinon : trois inventaires sur au moins 5 minutes, puis le verdict (bash scripts/lancer_sparks_exp7_nul_v10.sh boucle \$ID) ;
   « boucle » ou instance encore là : destruction par l'identifiant (étape 7), puis NŒUD de Lazar.
   « BOUCLE=oui » au journal (plus d'un démarrage) : NŒUD, même si l'instance est absente.
(Étapes 4 à 6 de la v9, ordre « fin » puis relance, sans objet au second tir : l'instance s'est détruite à l'étape 3.)
7. Repli si l'instance existe encore à l'échéance + 10 min : bash scripts/lancer_sparks_exp7_nul_v10.sh destruction \$ID (puis l'inventaire qu'il imprime).
8. vastai copy : non éprouvé par ce tir (aucun lot sans fabrication) ; risque déclaré. Aucune sortie brute de vastai n'est versée.
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
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v10'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$CODE" "$COMMIT"
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import depense; sys.exit(depense.main(sys.argv[1:]))" projeter "$ETAT"
if [ "$QUOI" = creation ]; then
    SHA_A=$(git show "$COMMIT:prereg/SPARKS-EXP7-NUL-addendum-1.md" | sha256sum | cut -c1-64)
    F="$ETAT_DIR/creation-$COURT-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Commande de création à lancer par la session (sortie de vastai jamais affichée ; jetons lus de l'environnement) :
GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai create instance $CIBLE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 120 --label sparks-exp7-nul-v5-$COURT \\
  --env "-e COMMIT=$COMMIT -e COMMIT_CODE=$CODE -e ADDENDUM_SHA256=$SHA_A -e PRIX_HEURE_USD=$PRIX -e PRIX_STOCKAGE_HEURE_USD=$STOCK -e ECHEANCE_UTC_S=$ECH -e GH_TOKEN=\$CONTROLE_IA_GITHUB_TOKEN -e HF_TOKEN=\$HF_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v10.sh")" > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v10.sh apres-creation "$F" \$?
Avant la création : tir réel (mode « tir ») ; image : curl et git présents (l'amorce refuse sinon).
FIN
elif [ "$QUOI" = redemarrage ]; then
    F="$ETAT_DIR/demarrage-$CIBLE-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Redémarrage sur ordre écrit :
1. écrire ordres/ordre-NNN.json (numéro neuf ; "instance": "$CIBLE" ; deja_usd = dépense cumulée de l'état, jamais plus basse ;
   copie : cas, premier, copie_minutes ; causal : ordres/causal/cle-ouverte-v1.json et ordres/causal/reponses/…, scellés)
   sur la branche ordres/sparks-exp7-nul-v5-$COURT (jamais sous calcul/), committer, pousser ;
2. GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai start instance $CIBLE > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v10.sh apres-commande start "$F" \$? $CIBLE
3. copie : vastai copy (sous timeout, sortie non affichée) de $CIBLE:/root/sparks/lots/lot-NNN/ vers un dossier hors du servi,
   puis sha256sum -c MANIFESTE-LOT.txt ; le conteneur sort seul après copie_minutes ;
4. causal ou fin : la machine se détruit elle-même (minuterie, après poussée vérifiée) ; inventaire attendu « absente » ;
   repli : bash scripts/lancer_sparks_exp7_nul_v10.sh destruction $CIBLE
FIN
else echo "creation, redemarrage, destruction, tir, apres-creation, apres-commande ou inventaire" >&2; exit 2; fi
