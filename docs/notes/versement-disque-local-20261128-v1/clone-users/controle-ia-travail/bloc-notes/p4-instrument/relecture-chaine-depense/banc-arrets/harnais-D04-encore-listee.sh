set -uo pipefail
echecs=0; ID=99999999; ETIQUETTE=p4-v1; TRAV='/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-depense/banc-arrets/trav-D04-encore-listee'; SANS_RUN=non
ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echecs=$((echecs + 1)); }
# 8. destruction de l'instance par son identifiant (R10), seulement après une récupération vérifiée (aucun KO) ; jamais
# par motif ; étiquette relue d'abord (refus si elle n'est pas « p4-v1 ») ; puis instance relue absente de la liste.
# Aucune sortie brute de l'outil n'est affichée (elle porte les variables de l'instance, dont les jetons).
DETRUITE=non
if [ "$echecs" = 0 ]; then
    if ! command -v vastai > /dev/null; then
        ko "8 outil de location introuvable sur le PATH : instance $ID gardée, à détruire par son identifiant"
    else
        LU=$(vastai show instance "$ID" --raw 2>/dev/null | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
    assert isinstance(d, dict)
except Exception:
    print("illisible"); raise SystemExit
print(" ".join(str(d.get(k)) for k in ("label", "actual_status", "cur_state")))')
        set -- $LU
        if [ "${1:-illisible}" != "$ETIQUETTE" ]; then
            ko "8 instance $ID : étiquette « ${1:-illisible} » (« $ETIQUETTE » attendue) : destruction refusée"
        elif ! vastai destroy instance "$ID" -y > "$TRAV/destruction.txt" 2>&1; then
            ko "8 instance $ID : destruction en échec (vastai destroy instance $ID -y)"
        elif vastai show instances --raw 2>/dev/null | python3 -c '
import json, sys
try:
    l = json.load(sys.stdin)
    assert isinstance(l, list)
except Exception:
    sys.exit(2)
sys.exit(0 if any(str(i.get("id")) == sys.argv[1] for i in l if isinstance(i, dict)) else 1)' "$ID"; then
            ko "8 instance $ID encore listée après la destruction"
        else
            c=$?
            if [ "$c" = 1 ]; then ok "8 instance $ID (étiquette $ETIQUETTE, ${2:-?} ${3:-?}) détruite par son identifiant et absente de la liste"; DETRUITE=oui
            else ko "8 liste des instances illisible après la destruction : instance $ID à relire"; fi
        fi
    fi
fi
if [ "$echecs" != 0 ]; then echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC ; INSTANCE $ID NON DÉTRUITE : NŒUD DE LAZAR"; exit 1
elif [ "$SANS_RUN" = oui ]; then echo "RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT ($ID)"; exit 4
else echo "RÉCUPÉRATION : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT ($ID)"; fi
