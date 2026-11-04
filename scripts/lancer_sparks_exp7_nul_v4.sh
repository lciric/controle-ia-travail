#!/usr/bin/env bash
# Lanceur de SPARKS-EXP7-NUL, v4 (version neuve de `lancer_sparks_exp7_nul_v3.sh`, R12 ; contre-lecture du delta v3, point 6
# de sa liste ; leçon R-1497). Depuis la session : vérifie (GO base et extension à 40 USD, sceau du texte v1, liste fermée et
# addendum scellé au commit lancé, dépense projetée), puis imprime la commande LITTÉRALE (`vastai create|start|destroy`), pour
# que `.claude/hooks/garde_calcul.py` la voie et revérifie le GO. Chaque commande imprimée :
#   - tourne sous `timeout` (create et start 300 s, destroy 120 s) ;
#   - passe à `vastai` un environnement nettoyé (`env -i`) qui garde PATH, HOME, LANG et, s'ils sont présents, HTTPS_PROXY,
#     HTTP_PROXY, NO_PROXY, SSL_CERT_FILE et REQUESTS_CA_BUNDLE (R-1497 ; noms seulement, valeurs jamais imprimées) ;
#   - redirige la sortie de `vastai` vers un fichier jamais affiché (R-1480) ; `apres-creation` n'en tire que le code de
#     retour et l'identifiant rendu ; tout code non nul ou délai dépassé pose le marqueur `.creation-incertaine` (aucune
#     seconde création avant un inventaire sans sortie brute) ; une erreur de certificat est un refus « non parvenu », sans
#     marqueur ;
#   - porte l'étiquette `--label sparks-exp7-nul-v4-<COMMIT[:12]>`.
# Usage :
#   bash scripts/lancer_sparks_exp7_nul_v4.sh creation <OFFRE> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json> [ECHEANCE_UTC_S]
#   bash scripts/lancer_sparks_exp7_nul_v4.sh redemarrage <ID> <PRIX_CARTE> <PRIX_STOCKAGE> <COMMIT> <COMMIT_CODE> <ETAT.json>
#   bash scripts/lancer_sparks_exp7_nul_v4.sh destruction <ID>
#   bash scripts/lancer_sparks_exp7_nul_v4.sh apres-creation <FICHIER_SORTIE> <CODE>
# État de la session : SPARKS_ETAT_DIR (défaut ~/.sparks-exp7-nul-v4) : sorties de vastai, marqueur, identifiants.
set -euo pipefail
ETAT_DIR="${SPARKS_ETAT_DIR:-$HOME/.sparks-exp7-nul-v4}"
MARQUEUR="$ETAT_DIR/.creation-incertaine"
QUOI="${1:?creation, redemarrage, destruction ou apres-creation}"
prefixe_env() {   # env -i … avec les variables du mandataire présentes, par leur nom seulement
    local p='env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8' v
    for v in HTTPS_PROXY HTTP_PROXY NO_PROXY SSL_CERT_FILE REQUESTS_CA_BUNDLE; do
        [ -n "${!v:-}" ] && p="$p $v=\"\$$v\""
    done
    printf '%s' "$p"
}
identifiant() { case "${1:-}" in ''|*[!0-9]*) echo "identifiant d'instance : chiffres seuls (R10)" >&2; exit 2;; esac; }
court() { case "${1:-}" in *[!0-9a-f]*|'') echo "commit illisible" >&2; exit 2;; esac; [ "${#1}" = 40 ] || { echo "commit de 40 caractères" >&2; exit 2; }; printf '%s' "${1:0:12}"; }
if [ "$QUOI" = apres-creation ]; then
    F="${2:?fichier de sortie}"; C="${3:?code}"
    mkdir -p "$ETAT_DIR"
    if grep -qiE 'CERTIFICATE_VERIFY_FAILED|certificate verify failed|SSLError|SSLCertVerificationError' "$F" 2>/dev/null; then
        echo "CRÉATION NON PARVENUE (erreur de certificat : la requête n'a pas atteint Vast) : refus, aucun marqueur"; exit 3
    fi
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then
        echo "$ID" > "$ETAT_DIR/instance-$(date -u +%Y%m%dT%H%M%S).txt"; echo "CRÉÉE : instance $ID (sortie de vastai non affichée)"; exit 0
    fi
    echo "code $C $(date -u +%FT%TZ)" > "$MARQUEUR"
    echo "CRÉATION INCERTAINE (code $C) : marqueur $MARQUEUR posé ; aucune seconde création avant un inventaire sans sortie brute"; exit 4
fi
if [ "$QUOI" = destruction ]; then
    identifiant "${2:-}"; mkdir -p "$ETAT_DIR"
    echo "Commande de destruction (sans -y, vastai 1.8.3 ne détruit rien, R-1482 ; sortie non affichée, R-1480) :"
    echo "timeout -k 10 120 $(prefixe_env) vastai destroy instance $2 -y > \"$ETAT_DIR/destruction-$2.txt\" 2>&1; echo \"vastai destroy : code \$?\""
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
cd "$(dirname "$0")/.."
P2=src/controle_ia/sparks_exp7_nul_v2; P4=src/controle_ia/sparks_exp7_nul_v4
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import go; sys.exit(go.main(['registres/go.md']))"
PYTHONPATH=src timeout 120 python3 -B -m controle_ia.scellement verifier prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, '$P4'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$CODE" "$COMMIT"
timeout 120 python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import depense; sys.exit(depense.main(sys.argv[1:]))" projeter "$ETAT"
mkdir -p "$ETAT_DIR"
if [ "$QUOI" = creation ]; then
    F="$ETAT_DIR/creation-$COURT-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Commande de création à lancer par la session (sortie de vastai jamais affichée ; jetons lus de l'environnement) :
GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai create instance $CIBLE --image pytorch/pytorch:2.9.1-cuda12.8-cudnn9-runtime --disk 120 --label sparks-exp7-nul-v4-$COURT \\
  --env "-e COMMIT=$COMMIT -e COMMIT_CODE=$CODE -e PRIX_HEURE_USD=$PRIX -e PRIX_STOCKAGE_HEURE_USD=$STOCK -e ECHEANCE_UTC_S=$ECH -e GH_TOKEN=\$GH_TOKEN -e HF_TOKEN=\$HF_TOKEN -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git" \\
  --args bash -c "\$(cat scripts/amorce_instance_sparks_exp7_nul_v4.sh)" > "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v4.sh apres-creation "$F" \$?
Avant la création : tir réel de la minuterie (R-1477) ; image : curl et git présents (l'amorce refuse sinon).
FIN
elif [ "$QUOI" = redemarrage ]; then
    F="$ETAT_DIR/demarrage-$CIBLE-$(date -u +%Y%m%dT%H%M%S).txt"
    cat <<FIN
Redémarrage sur ordre écrit :
1. écrire ordres/ordre-NNN.json (numéro neuf ; "instance": "$CIBLE" ; deja_usd = dépense cumulée de l'état, jamais plus basse ;
   copie : cas, premier, copie_minutes ; causal : ordres/causal/cle-ouverte-v1.json et ordres/causal/reponses/…, scellés)
   sur la branche ordres/sparks-exp7-nul-v4-$COURT (jamais sous calcul/), committer, pousser ;
2. GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai start instance $CIBLE > "$F" 2>&1; echo "vastai start : code \$?"
3. copie : vastai copy (sous timeout, sortie non affichée) de $CIBLE:/root/sparks/lots/lot-NNN/ vers un dossier hors du servi,
   puis sha256sum -c MANIFESTE-LOT.txt ; le conteneur sort seul après copie_minutes ;
4. causal ou fin : la machine se détruit elle-même (minuterie, après poussée vérifiée) ; repli :
   bash scripts/lancer_sparks_exp7_nul_v4.sh destruction $CIBLE
FIN
else echo "creation, redemarrage, destruction ou apres-creation" >&2; exit 2; fi
