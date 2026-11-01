#!/usr/bin/env bash
# Création de l'instance d'un lot de la course T0.5 « graines neuves » (lot A ou B, 30 tâches du pilote à graines neuves,
# même chaîne que le pilote ; fiches prereg/T0.5-graines-neuves-a-v1.md et prereg/T0.5-graines-neuves-b-v1.md ; devis
# docs/notes/devis-episodes-reels-t05-nuit-v1/devis-episodes-reels-t05-nuit-v1.md, scénario « moyen »). Copie versionnée
# de `docs/procedures/banque-T0.5-complete-v1/lancer_banque_t05_v4.sh` (couche 1 bis, R-579), par la lignée
# « session-depot », le 1er novembre 2026. Changements, et rien d'autre :
#   - LOT (a ou b) choisit la fiche, la branche de résultats et l'étiquette ; branche de préparation
#     prep/t05-graines-neuves-v1 ;
#   - le GO n'est plus écrit dans le script : GO_ID est passé en variable (forme GO-AAAA-MM-JJ-NN), relu par la garde de
#     calcul `.claude/hooks/garde_calcul.py` du dépôt, et cité dans la commande de création ;
#   - « aucune autre instance » devient « aucune autre instance que celle de l'autre lot » (étiquette
#     t05-graines-neuves-<autre lot>-v1), pour courir A et B en parallèle sur deux instances neuves ;
#   - A_BLANC=1 : tous les contrôles, offre comprise, puis arrêt sans création (code 0, « à blanc : rien créé »).
# Mêmes gardes que la v4 : commit poussé et cité, fiche scellée et conforme au commit (garde du manifeste rejouée),
# branche de résultats absente, garde de calcul avec le GO, offre A100 SXM4 (une carte, ≥ 79 Go, CUDA ≥ 13,0,
# fiabilité ≥ 0,99, machine 142924 toujours exclue, EXCLURE facultatif) sous 1,40 USD/h choisie juste avant la création,
# crédit relu et consigné, amorce du commit encodée, jetons passés par --env sans jamais s'afficher, pas de création
# entre 23:30 et 00:00 UTC. Rien ne se crée si un contrôle échoue.
# Codes : 0 création (ou à blanc conforme) ; 3 offre, prix ou heure ; 4 création douteuse (vérifier les instances, forme
# filtrée) ; 2 autre arrêt.
# Usage : VASTAI=<vastai 1.8.3> LOT=a|b GO_ID=GO-AAAA-MM-JJ-NN [EXCLURE=…] [A_BLANC=1] \
#             lancer_graines_neuves_t05_v1.sh COMMIT DOSSIER_TRACES
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 2 ] || { echo "usage : LOT=a|b GO_ID=GO-AAAA-MM-JJ-NN lancer_graines_neuves_t05_v1.sh COMMIT DOSSIER_TRACES"; exit 2; }
S=$1; T=$(realpath -m "$2")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT : 40 caractères hexadécimaux attendus"; exit 2; }
V=${VASTAI:?VASTAI : chemin de vastai 1.8.3}
[ "$("$V" --version 2>/dev/null | head -1)" = "1.8.3" ] || { echo "vastai : version différente de 1.8.3"; exit 2; }
LOT=${LOT:-}
case "$LOT" in a) AUTRE=b ;; b) AUTRE=a ;; *) echo "LOT : a ou b attendu"; exit 2 ;; esac
GO=${GO_ID:-}
[[ "$GO" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || { echo "GO_ID : forme GO-AAAA-MM-JJ-NN attendue"; exit 2; }
PRIX_MAX=1.40
DEPOT=/home/user/controle-ia-travail
PREP=prep/t05-graines-neuves-v1
P=prereg/T0.5-graines-neuves-$LOT-v1.md
BRANCHE=calcul/t05-graines-neuves-$LOT-v1
ETIQUETTE=t05-graines-neuves-$LOT-v1
ETIQUETTE_AUTRE=t05-graines-neuves-$AUTRE-v1
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone"' EXIT
printf 'lanceur %s ; départ %s UTC ; lot %s ; go %s\n' "$(sha256sum "$0" | cut -d' ' -f1)" "$(date -u +%FT%TZ)" "$LOT" "$GO" >> "$T/lancement.txt"
# 1. commit poussé ; branche de résultats absente
git -C "$DEPOT" fetch -q origin "$PREP"
[ "$(git -C "$DEPOT" rev-parse FETCH_HEAD)" = "$S" ] || { echo "tête de $PREP ≠ $S"; exit 2; }
rc=0; git -C "$DEPOT" ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1 || rc=$?
[ "$rc" = 2 ] || { echo "branche $BRANCHE présente sur le dépôt, ou ls-remote en erreur (code $rc)"; exit 2; }
# 2. fiche scellée et conforme au commit, rejouée avec le code du commit (garde du manifeste), et champs de lancement
git clone -q --no-checkout "$DEPOT" "$T/clone" && git -C "$T/clone" checkout -q "$S"
(cd "$T/clone" && PYTHONPATH=src python3 -I -B -c 'import sys; sys.path.insert(0, "src"); from controle_ia.prereg import exiger_prereg_scelle; print("fiche scellée :", exiger_prereg_scelle(sys.argv[1]))' "$P") \
    | tee -a "$T/lancement.txt" | grep -q 'scellée : [0-9a-f]\{64\}' || { echo "fiche non scellée ou non conforme au commit"; exit 2; }
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$T/clone/$P" || { echo "PREREG ou BRANCHE : la fiche cite autre chose"; exit 2; }
TACHES=$(sed -n "s/.*Chemin des tâches : \`\\([^\`]*\\)\`.*/\\1/p" "$T/clone/$P" | head -1)
[ "$TACHES" = "donnees/t05-graines-neuves-v1/taches-graines-neuves-$LOT-30-v1.json" ] && [ -f "$T/clone/$TACHES" ] && [ -f "$T/clone/$TACHES.sha256" ] \
    || { echo "tâches du lot $LOT absentes du commit, ou fiche qui cite d'autres tâches ($TACHES)"; exit 2; }
echo "tâches $TACHES présentes au commit" >> "$T/lancement.txt"
# 3. amorce du commit, encodée
cp "$T/clone/scripts/amorce_instance_t05.sh" "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
echo "amorce $E" >> "$T/lancement.txt"
# 4. jetons présents (jamais affichés)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 5. garde de calcul avec le GO
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GO" 0 \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py" && echo "garde de calcul : $GO accepté" | tee -a "$T/lancement.txt"
# 6. aucune autre instance que celle de l'autre lot (au plus une, à son étiquette exacte)
# --- début de l'étape 6 (extraite telle quelle par les essais R5)
N=$(timeout 60 "$V" show instances --raw 2>/dev/null | python3 -I -c '
import json, sys
autre = sys.argv[1]
l = json.load(sys.stdin)
if not isinstance(l, list):
    sys.exit("liste des instances illisible")
etrangeres = [i for i in l if i.get("label") != autre]
if etrangeres or len(l) > 1:
    print(f"{len(l)} instance(s), dont {len(etrangeres)} sans l étiquette {autre}")
    sys.exit(1)
print("ok", len(l))' "$ETIQUETTE_AUTRE") || { echo "instances sur le compte : $N ; pas de création"; exit 2; }
# --- fin de l'étape 6
echo "instances : $N (seule permise : $ETIQUETTE_AUTRE)" | tee -a "$T/lancement.txt"
# 7. crédit relu et consigné (recharge automatique déclarée, R-555 : minimum non exigé)
timeout 60 "$V" show user --raw 2>/dev/null | python3 -I -c 'import json, sys; print("crédit relu :", round(float(json.load(sys.stdin)["credit"]), 2), "USD (recharge automatique déclarée, R-555)")' \
    | tee -a "$T/lancement.txt" || { echo "crédit illisible"; exit 2; }
# 8. offre choisie juste avant la création : A100 SXM4, une carte, ≥ 79 Go, CUDA ≥ 13.0, fiabilité ≥ 0,99, machine non
#    exclue, la moins chère sous le maximum
# --- début de l'étape 8 (extraite telle quelle par les essais R5)
LU=$(timeout 60 "$V" search offers "gpu_name=A100_SXM4 num_gpus=1" --storage 80 --raw 2>/dev/null | python3 -I -c '
import json, sys
p = float(sys.argv[1])
exclues = {int(x) for x in ("142924," + sys.argv[2]).split(",") if x.strip()}
ok = [o for o in json.load(sys.stdin) if o.get("gpu_name") == "A100 SXM4" and o.get("num_gpus") == 1
      and float(o.get("gpu_ram") or 0) >= 79 * 1024 and float(o.get("cuda_max_good") or 0) >= 13.0 and float(o["dph_total"]) <= p
      and float(o.get("reliability2") or 0) >= 0.99 and o.get("machine_id") not in exclues]
if not ok: sys.exit("aucune offre conforme")
o = min(ok, key=lambda o: o["dph_total"])
print(o["id"], o["dph_total"], o.get("machine_id"), o.get("cuda_max_good"), o.get("gpu_ram"), o.get("reliability2"), str(o.get("geolocation")).replace(" ", "_"))' "$PRIX_MAX" "${EXCLURE:-}") || { echo "aucune offre conforme"; exit 3; }
# --- fin de l'étape 8
read -r OFFRE DPH MACHINE CUDA MEM FIAB LIEU <<< "$LU"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
echo "offre $OFFRE : $DPH USD/h ; machine $MACHINE ; CUDA $CUDA ; $MEM Mo ; fiabilité $FIAB ; $LIEU" | tee -a "$T/lancement.txt"
if [ "${A_BLANC:-0}" = 1 ]; then
    echo "à blanc : tous les contrôles tiennent ; rien créé" | tee -a "$T/lancement.txt"; exit 0
fi
# 9. création ; à partir d'ici, tout échec rend 4
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'go %s\ncommit %s\noffre %s\nprereg %s\nbranche %s\netiquette %s\ncreation %s\n' "$GO" "$S" "$OFFRE" "$P" "$BRANCHE" "$ETIQUETTE" "$CREATION" >> "$T/lancement.txt"
GO_ID=$GO "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e ETUDE=pilote -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh" 2>&1 | python3 -c '
import json, os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) > 6:
        t = t.replace(v, "***")
try:
    d = json.loads(t)
except Exception:
    open(os.environ["T_LANCEMENT"] + "/reponse-masquee.txt", "w").write(t[:300])
    print("réponse illisible (300 premiers caractères masqués dans reponse-masquee.txt) ; vérifier par « vastai show instances », sans --raw")
    sys.exit(4)
ok = d.get("success") is True and isinstance(d.get("new_contract"), int)
print("succès :", d.get("success"), "; identifiant", d.get("new_contract"), "; message :", str(d.get("msg", ""))[:200])
sys.exit(0 if ok else 4)' | tee -a "$T/lancement.txt"
st=("${PIPESTATUS[@]}")
[ "${st[0]}" = 0 ] && [ "${st[1]}" = 0 ] && [ "${st[2]}" = 0 ] || { echo "création douteuse (statuts ${st[*]}) : vérifier « vastai show instances », sans --raw"; exit 4; }
exit 0
