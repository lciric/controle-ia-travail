#!/usr/bin/env bash
# Création de l'instance des notations complémentaires de T0.5 (« couche 1 bis », partie (a) ; GO-2026-10-27-07) : un
# ou deux runs du module `noter_complement_t05` (PREREG_1, puis PREREG_2 facultatif), par l'amorce
# `scripts/amorce_complement_t05.sh` du commit. Dérivé de `lancer_banque_t05_v4.sh` (R-579), par la lignée
# « session-depot », le 27 octobre 2026 ; mêmes gardes de conduite : commit poussé et cité (tête de
# prep/t05-complement-notations-v1), fiche(s) scellée(s) et conforme(s) au commit (garde du manifeste rejouée avec le code
# du commit), BRANCHE citée par chaque fiche, branche de résultats absente, garde de calcul avec le GO, aucune autre
# instance sur le compte, crédit relu et consigné (recharge automatique déclarée, R-555), offre choisie juste avant la
# création (A100 SXM4, une carte, ≥ 79 Go, CUDA ≥ 13,0, fiabilité ≥ 0,99, machine non exclue, la moins chère sous le
# maximum), amorce du commit encodée, jetons passés par --env sans jamais s'afficher. Rien ne se crée si un contrôle échoue.
# Codes : 0 création ; 3 offre, prix ou heure ; 4 création douteuse (vérifier les instances, forme filtrée) ; 2 autre arrêt.
# Usage : VASTAI=<vastai 1.8.3> [EXCLURE=machines] lancer_complement_t05_v1.sh COMMIT DOSSIER_TRACES PREREG_1 [PREREG_2]
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 3 ] || [ $# -eq 4 ] || { echo "usage : lancer_complement_t05_v1.sh COMMIT DOSSIER_TRACES PREREG_1 [PREREG_2]"; exit 2; }
S=$1; T=$(realpath -m "$2"); P1=$3; P2=${4:-}
for p in "$P1" $P2; do [[ "$p" =~ ^prereg/[A-Za-z0-9._-]+\.md$ ]] || { echo "fiche $p : prereg/<nom>.md attendu"; exit 2; }; done
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT : 40 caractères hexadécimaux attendus"; exit 2; }
V=${VASTAI:?VASTAI : chemin de vastai 1.8.3}
[ "$("$V" --version 2>/dev/null | head -1)" = "1.8.3" ] || { echo "vastai : version différente de 1.8.3"; exit 2; }
GO=GO-2026-10-27-07
PRIX_MAX=1.40
DEPOT=/home/user/controle-ia-travail
BRANCHE=calcul/t05-complement-notations-reel-v1
ETIQUETTE=t05-complement-v1
PREP=prep/t05-complement-notations-v1
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone"' EXIT
printf 'lanceur %s ; départ %s UTC\n' "$(sha256sum "$0" | cut -d' ' -f1)" "$(date -u +%FT%TZ)" >> "$T/lancement.txt"
# 1. commit poussé ; branche de résultats absente
git -C "$DEPOT" fetch -q origin "$PREP"
[ "$(git -C "$DEPOT" rev-parse FETCH_HEAD)" = "$S" ] || { echo "tête de $PREP ≠ $S"; exit 2; }
rc=0; git -C "$DEPOT" ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1 || rc=$?
[ "$rc" = 2 ] || { echo "branche $BRANCHE présente sur le dépôt, ou ls-remote en erreur (code $rc)"; exit 2; }
# 2. fiche scellée et conforme au commit, rejouée avec le code du commit (garde du manifeste), et champs de lancement
git clone -q --no-checkout "$DEPOT" "$T/clone" && git -C "$T/clone" checkout -q "$S"
for p in "$P1" $P2; do
    (cd "$T/clone" && PYTHONPATH=src python3 -I -B -c 'import sys; sys.path.insert(0, "src"); from controle_ia.prereg import exiger_prereg_scelle; print("fiche scellée :", sys.argv[1], exiger_prereg_scelle(sys.argv[1]))' "$p") \
        | tee -a "$T/lancement.txt" | grep -q 'scellée : .* [0-9a-f]\{64\}$' || { echo "fiche $p non scellée ou non conforme au commit"; exit 2; }
    grep -qF "\`BRANCHE=$BRANCHE\`" "$T/clone/$p" || { echo "BRANCHE : la fiche $p cite autre chose"; exit 2; }
done
grep -qF "\`PREREG_1=$P1\`" "$T/clone/$P1" || { echo "la fiche $P1 ne cite pas \`PREREG_1=$P1\` (CE-08)"; exit 2; }
[ -z "$P2" ] || grep -qF "\`PREREG_2=$P2\`" "$T/clone/$P2" || { echo "la fiche $P2 ne cite pas \`PREREG_2=$P2\` (CE-08)"; exit 2; }
# 2 bis. contrôle d'avant création sur le clone (CE-06) : citations du script, sceaux, gardes du module jusqu'au manifeste
PY_CONTROLE=${PY_CONTROLE:-/home/user/controle-ia-travail/.venv/bin/python}
(cd "$T/clone" && PYTHONPATH= "$PY_CONTROLE" -B docs/procedures/complement-T0.5-v1/controle_avant_creation_v1.py "$P1" $P2) 2>&1 \
    | tee -a "$T/lancement.txt" | tail -n 1 | grep -qx "contrôle d'avant création : tout tient" \
    || { echo "contrôle d'avant création en échec (voir $T/lancement.txt)"; exit 2; }
echo "contrôle d'avant création : tout tient" 
# 3. amorce du commit, encodée
cp "$T/clone/scripts/amorce_complement_t05.sh" "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
echo "amorce $E" >> "$T/lancement.txt"
# 4. jetons présents (jamais affichés)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
# 5. garde de calcul avec le GO
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GO" 0 \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py" && echo "garde de calcul : $GO accepté" | tee -a "$T/lancement.txt"
# 6. aucune autre instance
N=$(timeout 60 "$V" show instances --raw 2>/dev/null | python3 -I -c 'import json, sys; print(len(json.load(sys.stdin)))')
[ "$N" = 0 ] || { echo "$N instance(s) sur le compte : pas de création"; exit 2; }
# 7. crédit relu et consigné (recharge automatique déclarée, R-555 : minimum non exigé)
timeout 60 "$V" show user --raw 2>/dev/null | python3 -I -c 'import json, sys; print("crédit relu :", round(float(json.load(sys.stdin)["credit"]), 2), "USD (recharge automatique déclarée, R-555)")' \
    | tee -a "$T/lancement.txt" || { echo "crédit illisible"; exit 2; }
# 8. offre choisie juste avant la création : A100 SXM4, une carte, ≥ 79 Go, CUDA ≥ 13.0, fiabilité ≥ 0,99, machine non
#    exclue, la moins chère sous le maximum
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
read -r OFFRE DPH MACHINE CUDA MEM FIAB LIEU <<< "$LU"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre invalide"; exit 2; }
echo "offre $OFFRE : $DPH USD/h ; machine $MACHINE ; CUDA $CUDA ; $MEM Mo ; fiabilité $FIAB ; $LIEU" | tee -a "$T/lancement.txt"
# 9. création ; à partir d'ici, tout échec rend 4
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'go %s\ncommit %s\noffre %s\nprereg_1 %s\nprereg_2 %s\nbranche %s\netiquette %s\ncreation %s\n' "$GO" "$S" "$OFFRE" "$P1" "${P2:-aucune}" "$BRANCHE" "$ETIQUETTE" "$CREATION" >> "$T/lancement.txt"
GO_ID=$GO "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e PREREG_1=$P1${P2:+ -e PREREG_2=$P2} -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
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
