#!/usr/bin/env bash
# Création de l'instance de la « couche 1 bis » de T0.5 (36 tâches restantes, même chaîne que le pilote ; fiche
# prereg/T0.5-banque-complete-36-v1.md ; GO-2026-10-27-07, R-564). Copie allégée de `lancer_pilote_v2.sh` du pilote, par
# la lignée « session-depot », le 27 octobre 2026 : production de données (préenregistrement levé, R-546, R-552), mêmes
# gardes de conduite : commit poussé et cité, fiche scellée et conforme au commit (garde du manifeste rejouée), branche de
# résultats absente, garde de calcul avec le GO, aucune autre instance sur le compte, offre A100 SXM4 sous le prix maximal,
# crédit relu et consigné (recharge automatique déclarée par Lazar, R-555 : minimum non exigé), amorce du commit encodée,
# jetons passés par --env sans jamais s'afficher. Rien ne se crée si un contrôle échoue.
# v2 (R-577) : la v1 relisait l'offre par `search offers "id=N"`, qui ne rend jamais rien sous vastai 1.8.3 (refus du
# 27 octobre, 15:08 UTC, code 3, rien créé) ; la v2 relit les offres du filtre et choisit l'identifiant en Python, et exige
# en plus la mémoire de carte du pilote (gpu_ram ≥ 79 Go). Le reste est la v1 mot pour mot.
# Codes : 0 création ; 3 offre, prix ou heure ; 4 création douteuse (vérifier les instances, forme filtrée) ; 2 autre arrêt.
# Usage : VASTAI=<vastai 1.8.3> lancer_banque_t05_v2.sh OFFRE COMMIT DOSSIER_TRACES
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 3 ] || { echo "usage : lancer_banque_t05_v2.sh OFFRE COMMIT DOSSIER_TRACES"; exit 2; }
OFFRE=$1; S=$2; T=$(realpath -m "$3")
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT : 40 caractères hexadécimaux attendus"; exit 2; }
V=${VASTAI:?VASTAI : chemin de vastai 1.8.3}
[ "$("$V" --version 2>/dev/null | head -1)" = "1.8.3" ] || { echo "vastai : version différente de 1.8.3"; exit 2; }
GO=GO-2026-10-27-07
PRIX_MAX=1.40
DEPOT=/home/user/controle-ia-travail
P=prereg/T0.5-banque-complete-36-v1.md
BRANCHE=calcul/t05-banque-complete-reel-v1
ETIQUETTE=t05-banque-complete-v1
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone"' EXIT
printf 'lanceur %s ; départ %s UTC\n' "$(sha256sum "$0" | cut -d' ' -f1)" "$(date -u +%FT%TZ)" >> "$T/lancement.txt"
# 1. commit poussé ; branche de résultats absente
git -C "$DEPOT" fetch -q origin prep/t05-banque-complete-v1
[ "$(git -C "$DEPOT" rev-parse FETCH_HEAD)" = "$S" ] || { echo "tête de prep/t05-banque-complete-v1 ≠ $S"; exit 2; }
rc=0; git -C "$DEPOT" ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1 || rc=$?
[ "$rc" = 2 ] || { echo "branche $BRANCHE présente sur le dépôt, ou ls-remote en erreur (code $rc)"; exit 2; }
# 2. fiche scellée et conforme au commit, rejouée avec le code du commit (garde du manifeste), et champs de lancement
git clone -q --no-checkout "$DEPOT" "$T/clone" && git -C "$T/clone" checkout -q "$S"
(cd "$T/clone" && PYTHONPATH=src python3 -I -B -c 'import sys; sys.path.insert(0, "src"); from controle_ia.prereg import exiger_prereg_scelle; print("fiche scellée :", exiger_prereg_scelle(sys.argv[1]))' "$P") \
    | tee -a "$T/lancement.txt" | grep -q 'scellée : [0-9a-f]\{64\}' || { echo "fiche non scellée ou non conforme au commit"; exit 2; }
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$T/clone/$P" || { echo "PREREG ou BRANCHE : la fiche cite autre chose"; exit 2; }
# 3. amorce du commit, encodée
cp "$T/clone/scripts/amorce_instance_t05.sh" "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
echo "amorce $E" >> "$T/lancement.txt"
# 4. jetons présents (jamais affichés)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 5. garde de calcul avec le GO
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GO" "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py" && echo "garde de calcul : $GO accepté" | tee -a "$T/lancement.txt"
# 6. aucune autre instance ; offre relue (A100 SXM4, une carte, ≥ 79 Go, CUDA ≥ 13.0, prix sous le maximum)
N=$(timeout 60 "$V" show instances --raw 2>/dev/null | python3 -I -c 'import json, sys; print(len(json.load(sys.stdin)))')
[ "$N" = 0 ] || { echo "$N instance(s) sur le compte : pas de création"; exit 2; }
DPH=$(timeout 60 "$V" search offers "gpu_name=A100_SXM4 num_gpus=1" --storage 80 --raw 2>/dev/null | python3 -I -c '
import json, sys
d = [o for o in json.load(sys.stdin) if str(o.get("id")) == sys.argv[1]]
if len(d) != 1: sys.exit("offre introuvable")
o = d[0]
g, n, c, m = o.get("gpu_name"), o.get("num_gpus"), o.get("cuda_max_good"), o.get("gpu_ram")
if g != "A100 SXM4" or n != 1 or float(c or 0) < 13.0 or float(m or 0) < 79 * 1024:
    sys.exit(f"offre non conforme : {g}, {n} carte(s), CUDA {c}, {m} Mo")
print(o["dph_total"])' "$OFFRE") || { echo "offre illisible ou non conforme"; exit 3; }
python3 -c "import sys; sys.exit(0 if float('$DPH') <= $PRIX_MAX else 1)" || { echo "prix $DPH USD/h au-delà de $PRIX_MAX"; exit 3; }
echo "offre $OFFRE : $DPH USD/h" | tee -a "$T/lancement.txt"
# 7. crédit relu et consigné (recharge automatique déclarée, R-555 : minimum non exigé)
timeout 60 "$V" show user --raw 2>/dev/null | python3 -I -c 'import json, sys; print("crédit relu :", round(float(json.load(sys.stdin)["credit"]), 2), "USD (recharge automatique déclarée, R-555)")' \
    | tee -a "$T/lancement.txt" || { echo "crédit illisible"; exit 2; }
# 8. création ; à partir d'ici, tout échec rend 4
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
