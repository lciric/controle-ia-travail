#!/usr/bin/env bash
# Lanceur de la comparaison d'échelle 8B contre 70B (préenregistrement `prereg/test-echelle-conscience-eval-v2.md`),
# sous le GO passé en argument ; décliné de `lancer_hm1_v3.sh` (outils/test-hm1-v1) sous un nom nouveau (R12) par la
# lignée « session-depot » le 26 octobre 2026. Ce run décide : le préenregistrement doit être scellé et conforme
# (`exiger_prereg_scelle`), sinon aucune création. Commit = tête de la branche d'outils sur le dépôt de travail ;
# branche des résultats absente (R12) ; garde de calcul rejouée avec le GO ; instances du compte : aucune, sauf celles
# d'autres projets de Lazar nommées « rr-… » (jamais touchées) ; offre conforme (deux à quatre cartes de 46 Go ou plus,
# 160 Go au total, CUDA ≥ 13.0, prix fini, positif, au plus PRIX_MAX, coût de descente au plus DESCENTE_MAX) au coût
# estimé le plus bas (1,5 h de location + 160 Go descendus) ; crédit exigé ; création avec l'amorce du commit, encodée ;
# jetons passés à l'instance par --env, jamais affichés (réponse masquée).
# Codes : 0 création ; 3 aucune offre conforme ou crédit insuffisant ; 4 création douteuse (vérifier les instances,
# champs filtrés, jamais --raw sans filtre) ; 2 tout autre arrêt avant la création.
# Usage : VASTAI=<chemin de vastai 1.8.3> lancer_echelle_v1.sh DOSSIER_TRACES COMMIT GO_ID
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 3 ] || { echo "usage : lancer_echelle_v1.sh DOSSIER_TRACES COMMIT GO_ID"; exit 2; }
T=$(realpath -m "$1"); COMMIT=$2; GO=$3
[[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT : 40 caractères hexadécimaux attendus"; exit 2; }
[[ "$GO" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || { echo "GO_ID illisible"; exit 2; }
V=${VASTAI:?VASTAI : chemin de l outil vastai 1.8.3}
DEPOT=/home/user/controle-ia-travail
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
BRANCHE_CODE=outils/echelle-conscience-eval-v1
BRANCHE=donnees/echelle-conscience-eval-v1
ETIQUETTE=echelle-v1
PREREG=prereg/test-echelle-conscience-eval-v2.md
PRIX_MAX=4.00          # USD de l'heure, toutes cartes : plafond du devis du préenregistrement
DESCENTE_MAX=0.01      # USD par Go descendu : ~160 Go de poids (8B + 70B)
HEURES_CREDIT=2        # crédit exigé : 2 h × (prix + autres projets en marche) + 160 Go × descente + 1,2 USD
DUREE_MAX_S=7200       # surveiller_echelle_v1.sh : arrêt par identifiant au plus tard à création + 7 200 s
DISQUE=250
IMAGE=python:3.11-bookworm
PREFIXE_AUTRES=rr-
FILTRE="gpu_total_ram>=160 gpu_ram>=46 num_gpus<=4 cuda_vers>=13.0 verified=true reliability>=0.98 disk_space>=$DISQUE rentable=true inet_down>=700"
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
mkdir -p "$T"
printf 'lanceur %s ; départ %s UTC\n' "$(sha256sum "$0" | cut -d' ' -f1)" "$(date -u +%FT%TZ)" >> "$T/lancement.txt"
# 0. préenregistrement scellé et conforme (R1, R2 ; CLH-08)
(cd "$DEPOT" && PYTHONPATH=src python3 -I -B -c 'import sys; sys.path.insert(0, "src"); from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle(sys.argv[1]))' "$PREREG") \
    | sed 's/^/préenregistrement scellé : /' | tee -a "$T/lancement.txt" | grep -q 'scellé : [0-9a-f]\{64\}' \
    || { echo "préenregistrement non scellé ou non conforme : pas de création"; exit 2; }
# 1. commit = tête de la branche d'outils ; branche des résultats absente (R12)
TETE=$(git -C "$DEPOT" ls-remote origin "refs/heads/$BRANCHE_CODE" | cut -f1)
[ "$TETE" = "$COMMIT" ] || { echo "branche $BRANCHE_CODE : tête ${TETE:-absente} ≠ $COMMIT"; exit 2; }
[ -z "$(git -C "$DEPOT" ls-remote origin "refs/heads/$BRANCHE")" ] || { echo "branche $BRANCHE déjà présente sur le dépôt (R12)"; exit 2; }
# 2. amorce du commit, encodée ; aller-retour vérifié
git -C "$DEPOT" fetch -q origin "$BRANCHE_CODE"
git -C "$DEPOT" show "$COMMIT:echelle-v1/scripts/amorce_echelle_v1.sh" > "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
B64=$(base64 -w0 < "$T/amorce.sh")
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
printf 'commit %s\namorce %s\n' "$COMMIT" "$E" >> "$T/lancement.txt"
# 3. jetons présents, jamais affichés
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] && [ -n "${VAST_API_KEY:-}" ] \
    || { echo "jeton absent (HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN ou VAST_API_KEY) : pas de création"; exit 2; }
# 4. garde de calcul rejouée sur une commande qui porte le GO (registre courant)
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance 0 --raw"}}' "$GO" | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
echo "garde de calcul : $GO accepté" | tee -a "$T/lancement.txt"
# 5. instances du compte : aucune, sauf celles d'autres projets nommées « rr-… » (comptées dans le crédit, jamais touchées)
SOMME_AUTRES=$("$V" show instances --raw | python3 -I -B -c '
import json, sys
prefixe, journal = sys.argv[1], open(sys.argv[2], "a", encoding="utf-8")
try:
    instances = json.load(sys.stdin)
    assert isinstance(instances, list)
except Exception:
    print("vastai show instances : réponse illisible", file=sys.stderr); sys.exit(2)
autres, refusees, somme = [], [], 0.0
for i in instances:
    if not isinstance(i, dict):
        refusees.append("entrée illisible"); continue
    ident, etat, cur, etiquette = str(i.get("id")), i.get("actual_status"), i.get("cur_state"), str(i.get("label") or "")
    dph = i.get("dph_total")
    if etiquette.startswith(prefixe) and isinstance(dph, (int, float)) and not isinstance(dph, bool):
        arretee = etat in ("exited", "stopped") and cur == "stopped"
        somme += 0.0 if arretee else float(dph)
        autres.append(f"{ident} ({etat}, {cur}, {float(dph):.3f} USD/h)")
    else:
        refusees.append(f"{ident} ({etat}, {cur})")
ligne = "instances d’autres projets (étiquette « " + prefixe + "… », non touchées) : " + (", ".join(autres) or "aucune")
print(ligne, file=sys.stderr); journal.write(ligne + "\n")
if refusees:
    ligne = "autres instances sur le compte : " + ", ".join(refusees)
    print(ligne, file=sys.stderr); journal.write(ligne + "\n"); sys.exit(1)
print(f"{somme:.4f}")' "$PREFIXE_AUTRES" "$T/lancement.txt") \
    || { echo "instances : une instance hors liste est sur le compte, ou réponse illisible : pas de création"; exit 2; }
# 6. offre : filtre, conformité relue localement, la moins chère (à prix égal, le plus petit identifiant)
"$V" search offers "$FILTRE" -o 'dph_total' --storage "$DISQUE" --raw > "$T/offres-brut.json"
c=0
CHOIX=$(python3 -I -B - "$T/offres-brut.json" "$T/offre.json" "$PRIX_MAX" "$T/lancement.txt" "$T/offres-relues.json" "$DESCENTE_MAX" <<'EOF'
import json, math, sys
brut, sortie, prix_max, journal, relues = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5]
descente_max = float(sys.argv[6])
try:
    offres = json.load(open(brut))
    assert isinstance(offres, list)
except Exception:
    print("offres : réponse illisible", file=sys.stderr); sys.exit(2)
extrait = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "gpu_total_ram", "num_gpus", "cuda_max_good", "cpu_name", "cpu_cores_effective",
           "cpu_ram", "dph_total", "inet_down", "inet_down_cost", "storage_total_cost", "reliability2", "geolocation")
json.dump([{k: o.get(k) for k in extrait} if isinstance(o, dict) else {"illisible": type(o).__name__} for o in offres], open(relues, "w"), indent=1)
vus = [repr(o.get("id")) for o in offres if isinstance(o, dict)]
if len(vus) != len(set(vus)):
    print("offres : identifiant en double (ambigu) : pas de création", file=sys.stderr); sys.exit(2)
def nombre(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
def entier(v):
    return isinstance(v, int) and not isinstance(v, bool)
def cout(o):
    return round(1.5 * o["dph_total"] + 160 * o["inet_down_cost"], 4)
conformes = sorted((o for o in offres if isinstance(o, dict) and entier(o.get("id"))
                    and nombre(o.get("gpu_ram")) and o["gpu_ram"] >= 46000 and entier(o.get("num_gpus"))
                    and 2 <= o["num_gpus"] <= 4 and o["gpu_ram"] * o["num_gpus"] >= 160000
                    and nombre(o.get("cuda_max_good")) and o["cuda_max_good"] >= 13.0
                    and nombre(o.get("dph_total")) and 0 < o["dph_total"] <= prix_max
                    and nombre(o.get("inet_down_cost")) and 0 <= o["inet_down_cost"] <= descente_max),
                   key=lambda o: (cout(o), o["id"]))
with open(journal, "a", encoding="utf-8") as j:
    j.write("offres conformes relues : " + (", ".join(f"{o['id']} ({o['num_gpus']} × {o['gpu_name']}, {o['dph_total']:.4f} USD/h, descente {o['inet_down_cost']:.4f} USD/Go, coût estimé {cout(o):.2f} USD, machine {o.get('machine_id')})"
                                                      for o in conformes) or "aucune") + "\n")
if not conformes:
    print(f"aucune offre conforme au plus {prix_max} USD/h : pas de création", file=sys.stderr); sys.exit(3)
o = conformes[0]
json.dump({k: o.get(k) for k in extrait}, open(sortie, "w"), indent=1)
print(o["id"], o["dph_total"], o["inet_down_cost"])
EOF
) || c=$?
rm -f "$T/offres-brut.json"
[ "$c" = 3 ] && exit 3
[ "$c" = 0 ] || { echo "offres : relecture impossible (code $c)"; exit 2; }
read -r OFFRE DPH DESC <<< "$CHOIX"
[[ "$OFFRE" =~ ^[0-9]+$ ]] || { echo "offre choisie illisible"; exit 2; }
echo "offre choisie : $OFFRE ($DPH USD/h ; descente $DESC USD/Go), au coût estimé le plus bas des offres conformes" | tee -a "$T/lancement.txt"
# 7. crédit exigé (aucune valeur relue n'est insérée dans du code)
c=0
CREDIT_LIGNE=$("$V" show user --raw 2>/dev/null | python3 -I -B -c '
import json, math, sys
heures, dph, autres, desc = (float(x) for x in sys.argv[1:5])
try:
    credit = json.load(sys.stdin)["credit"]
    assert isinstance(credit, (int, float)) and not isinstance(credit, bool) and math.isfinite(credit)
except Exception:
    print("crédit illisible"); sys.exit(2)
m = round(heures * (dph + autres) + 160 * desc + 1.2, 2)
print(f"prix {dph:.4f} USD/h ; autres projets en marche {autres:.4f} USD/h ; crédit {credit:.2f} USD ; minimum {m:.2f} USD")
sys.exit(0 if round(credit, 2) >= m else 3)' "$HEURES_CREDIT" "$DPH" "$SOMME_AUTRES" "$DESC") || c=$?
printf '%s\n' "$CREDIT_LIGNE" | tee -a "$T/lancement.txt"
case $c in
    0) ;;
    3) echo "crédit insuffisant : pas de création ; recharge à demander à Lazar"; exit 3 ;;
    *) echo "crédit illisible : pas de création"; exit 2 ;;
esac
# 8. création ; à partir d'ici, tout échec rend 4
trap - ERR
set +e
CREATION=$(date -u +%s)
export T_LANCEMENT="$T"
printf 'go %s\noffre %s\nbranche des résultats %s\netiquette %s\ncreation %s\nplafond de la surveillance %s (création + %s s ; surveiller_echelle_v1.sh <id> %s <dossier neuf>)\ninstance : arrêtée par son identifiant à la fin (R10), détruite par son identifiant après vérification des résultats poussés\n' \
    "$GO" "$OFFRE" "$BRANCHE" "$ETIQUETTE" "$CREATION" "$((CREATION + DUREE_MAX_S))" "$DUREE_MAX_S" "$CREATION" >> "$T/lancement.txt"
GO_ID="$GO" "$V" create instance "$OFFRE" --raw --image "$IMAGE" --disk "$DISQUE" --cancel-unavail --label "$ETIQUETTE" \
    --env "-e COMMIT=$COMMIT -e BRANCHE=$BRANCHE -e GO_ID=$GO -e DEPOT_URL=$DEPOT_URL -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh" 2>&1 | python3 -I -B -c '
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
    print("réponse illisible (300 premiers caractères masqués dans reponse-masquee.txt) ; vérifier les instances, champs filtrés")
    sys.exit(4)
ok = d.get("success") is True and isinstance(d.get("new_contract"), int)
print("succès :", d.get("success"), "; identifiant", d.get("new_contract"), "; message :", str(d.get("msg", ""))[:200])
sys.exit(0 if ok else 4)' | tee -a "$T/lancement.txt"
st=("${PIPESTATUS[@]}")
[ "${st[0]}" = 0 ] && [ "${st[1]}" = 0 ] && [ "${st[2]}" = 0 ] || { echo "création douteuse (statuts ${st[*]}) : vérifier les instances, champs filtrés"; exit 4; }
exit 0
