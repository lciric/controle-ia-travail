#!/usr/bin/env bash
# Chaîne v2 (2026-11-11 ; règle (a') de P3-bis : R-2296, R-2320 ; consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`) : copie de `detruire_p3bis_v1.sh`, gardé
# tel quel (R12), noms de la chaîne en v2 ; aucun autre changement.
# Destruction de l'instance de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au 2026-11-23 : R-2077), v1, par son identifiant (R10), « dès que
# les résultats poussés sont vérifiés par empreinte dans un clone de la session » (texte, brouillon 9, plan, point 11 ;
# « Liste d'arrêt » : « en fin normale, après la récupération des résultats poussés et leur vérification par empreinte,
# puis destruction de l'instance par son identifiant »). Voisin neuf de la chaîne (P3 gardait l'instance 72 heures ; rien
# à décliner). Gardes, toutes avant tout appel :
#   - l'identifiant est celui de l'instance créée par le lanceur (seule ligne « instance <id> » des traces) et n'est pas
#     dans ARRETEES_TOLEREES (module commun) ;
#   - la surveillance est finie sur le motif FIN (motif.txt), aucune marque instance-gardee : jamais de destruction après
#     un code 5 du second paquet (instance gardée jusqu'au paquet refait), ni après un autre motif (processus mort, échec
#     d'amorce, redémarrage, état terminal, dépense : nœud de Lazar, la session décide) ;
#   - le rapport de la récupération finit sur « RÉCUPÉRATION : TOUS CONFORMES ; … poussé sur <branche> », la branche du
#     lancement.
# Puis « vastai destroy instance <id> » (jamais par motif), et relecture de la liste des instances : l'identifiant n'y est
# plus. Ligne à consigner (registres/arrets.md) écrite dans arrets-a-consigner.txt du dossier de la surveillance.
# Codes : 0 détruite et absente de la liste relue ; 1 destruction en échec ou instance encore listée (la session agit par
# l'identifiant, à la main) ; 2 refus d'une garde (rien n'est appelé).
# Usage : detruire_p3bis_v2.sh <identifiant> <dossier des traces du lancement> <dossier de la surveillance> <rapport de la récupération>
set -uo pipefail
ID=${1:-}; T=${2:-}; SV=${3:-}; RAP=${4:-}
H=$(dirname "$(realpath "$0")")
VERIF=$H/verifications_p3bis_v2.py
[ $# -eq 4 ] && [[ "$ID" =~ ^[0-9]+$ ]] || { echo "usage : detruire_p3bis_v2.sh <identifiant> <traces du lancement> <dossier de la surveillance> <rapport de la récupération>"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
command -v vastai > /dev/null || { echo "outil de location introuvable sur le PATH"; exit 2; }
G=$(python3 -I "$VERIF" identifiant "$ID" "$T/lancement.txt" 2>&1) || { echo "REFUS : identifiant : $(printf '%s\n' "$G" | tail -1)"; exit 2; }
[ -e "$SV/instance-gardee" ] && { echo "REFUS : instance gardée (second paquet en échec) : jamais détruite avant le paquet refait"; exit 2; }
[ "$(cat "$SV/motif.txt" 2>/dev/null)" = FIN ] || { echo "REFUS : surveillance sans motif FIN ($(cat "$SV/motif.txt" 2>/dev/null || echo absent)) : nœud de Lazar, aucune destruction ici"; exit 2; }
BR=$(sed -n 's/^branche \(calcul\/p3bis-reel-v[123]\)$/\1/p' "$T/lancement.txt")
[ "$(printf '%s\n' "$BR" | grep -c .)" = 1 ] || { echo "REFUS : branche du lancement illisible"; exit 2; }
DERN=$(grep -v '^[[:space:]]*$' "$RAP" 2>/dev/null | tail -1)
[[ "$DERN" =~ ^RÉCUPÉRATION\ :\ TOUS\ CONFORMES\ \;\ paquet\ des\ lectures\ [0-9a-f]{64}\ poussé\ sur\ (.+)$ ]] && [ "${BASH_REMATCH[1]}" = "$BR" ] \
    || { echo "REFUS : récupération non conforme, ou d'une autre branche que $BR (« ${DERN:0:120} »)"; exit 2; }
c=0
vastai destroy instance "$ID" > /dev/null 2>&1 || c=$?
L=$(vastai show instances --raw 2>/dev/null | python3 -c '
import json, sys
try:
    l = json.load(sys.stdin); assert isinstance(l, list)
except Exception:
    print("illisible"); sys.exit(0)
print("présente" if any(isinstance(i, dict) and str(i.get("id")) == sys.argv[1] for i in l) else "absente")' "$ID")
printf '| %s | P3-bis, GO-2026-11-10-02 | instance %s détruite par son identifiant (R10) après la récupération vérifiée (%s) : code %s, liste relue : %s |\n' \
    "$(date -u +%FT%TZ)" "$ID" "$BR" "$c" "$L" >> "$SV/arrets-a-consigner.txt"
if [ "$c" = 0 ] && [ "$L" = absente ]; then echo "DESTRUCTION : instance $ID détruite par son identifiant (R10), absente de la liste relue"; exit 0; fi
echo "DESTRUCTION EN ÉCHEC : code $c, liste relue « $L » : agir par l'identifiant $ID, à la main (R10), consigner"
exit 1
