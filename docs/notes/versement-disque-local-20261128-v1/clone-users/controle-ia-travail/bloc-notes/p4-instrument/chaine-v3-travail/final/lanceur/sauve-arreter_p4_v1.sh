#!/usr/bin/env bash
# Arrêt de l'instance de P4-instrument par son identifiant (R10 ; texte de P4, Plan d'analyse, point 7, et Liste
# d'arrêt : « arrêt de l'instance par son identifiant »), v1, script neuf de la chaîne v2 (RC-depense-01,
# RC-fidelite-06). Aucun arrêt par motif ; aucune destruction (la destruction suit la récupération vérifiée).
# Chaîne v3 : étiquette comparée dans Python, exactement (VC2-depense-02 : « p4-v1 » suivi d'un saut de ligne n'est plus
# accepté) ; ligne prête pour registres/arrets.md à quatre cellules, la forme du registre (VC2-depense-04).
#   1. identifiant de 6 à 10 chiffres, dossier de sortie neuf (R12), outil de location sur le PATH ;
#   2. étiquette relue ENTIÈRE dans l'état de l'instance (« p4-v1 » exactement ; « p4-v1 x », une autre étiquette ou un
#      état illisible : refus, rien n'est demandé : un identifiant faux n'arrête rien d'autre) ;
#   3. `vastai stop instance <identifiant>` (code de l'outil relu) ;
#   4. état relu toutes les PAS_S secondes, LECTURES_MAX fois au plus (délai borné : 10 minutes, l'arrêt compté par la
#      borne de l'étape) : arrêtée quand « actual_status » vaut exited ou stopped et « cur_state » vaut stopped, deux
#      lectures de suite ;
#   5. heure de la demande et heure de l'arrêt relu écrites (arret.txt), et une ligne prête pour registres/arrets.md
#      (ligne-arrets.md), aux quatre cellules du registre (date et heure de l'arrêt relu ; cible ; raison ; vérification
#      après arrêt) : ce script n'écrit pas le registre, la session la consigne.
# Aucune sortie brute de l'outil n'est affichée ni écrite (l'état porte les variables de l'instance, dont les jetons) :
# seuls l'étiquette, les états et les heures s'écrivent.
# Codes : 0 arrêt demandé et instance relue arrêtée ; 1 outil en échec à l'arrêt, ou instance jamais relue arrêtée dans le
# délai (instance peut-être en marche : nœud de Lazar, arrêt à vérifier à la main par son identifiant) ; 2 usage,
# identifiant mal formé, dossier existant, outil introuvable, étiquette autre ou illisible (rien n'est demandé).
# Usage : arreter_p4_v1.sh IDENTIFIANT DOSSIER_NEUF [MOTIF]
#   MOTIF (facultatif) : raison écrite dans la ligne du registre (80 caractères imprimables au plus, sans « | » ni « ` »).
set -uo pipefail
ETIQUETTE=p4-v1
PAS_S=10                                         # une relecture de l'état toutes les 10 s
LECTURES_MAX=60                                  # 60 × 10 s : 10 minutes au plus (arrêt en dix minutes, borne de l'étape)
ID=${1:-}; D=${2:-}; MOTIF=${3:-arrêt demandé par la session}
[ $# -ge 2 ] && [ $# -le 3 ] && [ -n "$D" ] || { echo "usage : arreter_p4_v1.sh IDENTIFIANT DOSSIER_NEUF [MOTIF]"; exit 2; }
[[ "$ID" =~ ^[0-9]{6,10}$ ]] || { echo "identifiant d'instance mal formé (6 à 10 chiffres attendus) : rien n'est arrêté"; exit 2; }
python3 -c 'import sys; m = sys.argv[1]; sys.exit(0 if 0 < len(m) <= 80 and m.isprintable() and "|" not in m and "`" not in m else 1)' "$MOTIF" \
    || { echo "motif mal formé : 80 caractères imprimables au plus, sans barre verticale ni guillemet inversé"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà (R12) : rien n'est arrêté"; exit 2; }
command -v vastai > /dev/null || { echo "outil de location introuvable sur le PATH : rien n'est arrêté ; arrêter l'instance $ID à la main par son identifiant"; exit 2; }
mkdir -p "$D" || exit 2
etat() {   # étiquette, actual_status, cur_state de l'instance, ou « illisible » ; rien d'autre n'est lu
    vastai show instance "$ID" --raw 2>/dev/null | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
    assert isinstance(d, dict)
except Exception:
    print("illisible"); raise SystemExit
lab = d.get("label")
print(json.dumps({"label": lab if isinstance(lab, str) else None, "actual_status": str(d.get("actual_status")),
                  "cur_state": str(d.get("cur_state"))}, ensure_ascii=False))'
}
champ() { python3 -c 'import json, sys; d = json.loads(sys.argv[1]); print(d.get(sys.argv[2]))' "$1" "$2"; }
# 2. étiquette relue entière
E0=$(etat)
if [ "$E0" = illisible ] || [ -z "$E0" ]; then
    echo "état de l'instance $ID illisible : étiquette non relue : arrêt refusé (rien n'est demandé) ; nœud de Lazar" | tee "$D/arret.txt"; exit 2
fi
# comparaison dans Python, exacte (chaîne v3, VC2-depense-02 : la substitution de commande du shell retirerait les sauts
# de ligne finaux) ; l'étiquette autre s'écrit sous sa forme JSON (sauts de ligne visibles), 40 caractères au plus
if ! python3 -c 'import json, sys; sys.exit(0 if json.loads(sys.argv[1]).get("label") == sys.argv[2] else 1)' "$E0" "$ETIQUETTE"; then
    LAB=$(python3 -c 'import json, sys; print(json.dumps(json.loads(sys.argv[1]).get("label"), ensure_ascii=False)[:40])' "$E0")
    printf 'instance %s : étiquette « %s » ≠ « %s » (comparée entière) : arrêt refusé (rien n est demandé)\n' "$ID" "$LAB" "$ETIQUETTE" | tee "$D/arret.txt"; exit 2
fi
echo "instance $ID : étiquette « $ETIQUETTE » relue entière ; état avant l'arrêt : $(champ "$E0" actual_status), $(champ "$E0" cur_state)" | tee "$D/arret.txt"
# 3. arrêt par l'identifiant
DEMANDE=$(date -u +%FT%TZ)
if ! vastai stop instance "$ID" > /dev/null 2>&1; then
    echo "$DEMANDE : vastai stop instance $ID en échec : instance peut-être en marche ; arrêt à vérifier à la main par son identifiant ; nœud de Lazar" | tee -a "$D/arret.txt"
    echo "ARRÊT NON CONFIRMÉ : INSTANCE $ID (outil en échec)" | tee -a "$D/arret.txt"; exit 1
fi
echo "$DEMANDE : vastai stop instance $ID demandé" | tee -a "$D/arret.txt"
# 4. état relu jusqu'à l'arrêt, deux lectures de suite, délai borné
suite=0; n=0; DERNIER=""
while [ "$n" -lt "$LECTURES_MAX" ]; do
    n=$((n + 1))
    E=$(etat); DERNIER=$E
    if [ "$E" != illisible ] && [ -n "$E" ] && python3 -c 'import json, sys
d = json.loads(sys.argv[1])
sys.exit(0 if d["actual_status"] in ("exited", "stopped") and d["cur_state"] == "stopped" and d["label"] == sys.argv[2] else 1)' "$E" "$ETIQUETTE"; then
        suite=$((suite + 1))
    else suite=0; fi
    [ "$suite" -ge 2 ] && break
    sleep "$PAS_S"
done
if [ "$suite" -lt 2 ]; then
    if [ "$DERNIER" = illisible ] || [ -z "$DERNIER" ]; then lu="illisible"; else lu="$(champ "$DERNIER" actual_status), $(champ "$DERNIER" cur_state)"; fi
    echo "$(date -u +%FT%TZ) : instance $ID non relue arrêtée après $n lecture(s) en $((LECTURES_MAX * PAS_S)) s au plus (dernier état : $lu) : arrêt à vérifier à la main par son identifiant ; nœud de Lazar" | tee -a "$D/arret.txt"
    echo "ARRÊT NON CONFIRMÉ : INSTANCE $ID (état non relu arrêté dans le délai)" | tee -a "$D/arret.txt"; exit 1
fi
FIN=$(date -u +%FT%TZ)
echo "$FIN : instance $ID relue arrêtée deux fois de suite ($(champ "$DERNIER" actual_status), $(champ "$DERNIER" cur_state)), $n lecture(s)" | tee -a "$D/arret.txt"
# 5. ligne prête pour registres/arrets.md (le registre est écrit par la session), aux quatre cellules du registre
# (chaîne v3, VC2-depense-04) : | date (UTC) | cible (PID ou identifiant) | raison | vérification après arrêt | ; date
# et heure (AAAA-MM-JJ HH:MM) de l'arrêt relu
J_ARRET=$(date -u -d "$FIN" '+%F %H:%M')
printf '| %s | instance Vast.ai **%s** (P4-instrument, étiquette %s ; `vastai stop instance %s`) | %s | demandé à %s, relu arrêté (%s, %s) deux fois de suite à %s (arreter_p4_v1.sh) |\n' \
    "$J_ARRET" "$ID" "$ETIQUETTE" "$ID" "$MOTIF" "$DEMANDE" "$(champ "$DERNIER" actual_status)" "$(champ "$DERNIER" cur_state)" "$FIN" > "$D/ligne-arrets.md"
echo "ligne prête pour registres/arrets.md : $D/ligne-arrets.md"
echo "ARRÊT CONFIRMÉ : INSTANCE $ID ARRÊTÉE PAR SON IDENTIFIANT ($FIN)" | tee -a "$D/arret.txt"
exit 0
