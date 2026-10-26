#!/usr/bin/env bash
# Lanceur de la comparaison d'échelle 8B contre 70B, v2 (préenregistrement `prereg/test-echelle-conscience-eval-v3.md`),
# sous le GO passé en argument ; décliné de `lancer_echelle_v1.sh` sous un nom nouveau (R12) par la lignée
# « session-depot » le 26 octobre 2026, après la contre-lecture n° 1 :
#   - offre et plafond de durée par `choisir_offre_v2.py` (extrait du commit) : la dépense au pire (durée plafonnée ×
#     prix + descente de 160 Go + 3 h de stockage après l'arrêt + marge) tient sous le plafond du GO (CLX-07) ;
#   - branche des résultats : code de retour de `git ls-remote --exit-code` distingué (2 = absente ; autre = arrêt,
#     CLX-13).
# Le reste comme v1 : préenregistrement scellé et conforme (`exiger_prereg_scelle`), sinon aucune création ; commit =
# tête de la branche d'outils ; garde de calcul rejouée avec le GO ; instances du compte : aucune, sauf celles
# d'autres projets nommées « rr-… » (jamais touchées) ; crédit exigé ; création avec l'amorce du commit, encodée ;
# jetons passés à l'instance par --env, jamais affichés (réponse masquée).
# Codes : 0 création ; 3 aucune offre conforme ou crédit insuffisant ; 4 création douteuse (vérifier les instances,
# champs filtrés, jamais --raw sans filtre) ; 2 tout autre arrêt avant la création.
# Usage : VASTAI=<chemin de vastai 1.8.3> lancer_echelle_v2.sh DOSSIER_TRACES COMMIT GO_ID
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 3 ] || { echo "usage : lancer_echelle_v2.sh DOSSIER_TRACES COMMIT GO_ID"; exit 2; }
T=$(realpath -m "$1"); COMMIT=$2; GO=$3
[[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "COMMIT : 40 caractères hexadécimaux attendus"; exit 2; }
[[ "$GO" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || { echo "GO_ID illisible"; exit 2; }
V=${VASTAI:?VASTAI : chemin de l outil vastai 1.8.3}
DEPOT=/home/user/controle-ia-travail
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
BRANCHE_CODE=outils/echelle-conscience-eval-v2
BRANCHE=donnees/echelle-conscience-eval-v2
ETIQUETTE=echelle-v2
PREREG=prereg/test-echelle-conscience-eval-v3.md
PLAFOND_GO=8.00        # USD : plafond demandé à Lazar (dépense au pire, stockage après l'arrêt compris)
PRIX_MAX=3.50          # USD de l'heure, toutes cartes, stockage compris
DESCENTE_MAX=0.005     # USD par Go descendu : ~160 Go de poids (8B + 70B)
HEURES_CREDIT=2        # crédit exigé : dépense au pire + 2 h × autres projets en marche + 1,2 USD
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
rc=0; git -C "$DEPOT" ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1 || rc=$?
case $rc in
    0) echo "branche $BRANCHE déjà présente sur le dépôt (R12)"; exit 2 ;;
    2) ;;
    *) echo "git ls-remote en échec (code $rc) : pas de création"; exit 2 ;;
esac
# 2. amorce du commit, encodée ; aller-retour vérifié
git -C "$DEPOT" fetch -q origin "$BRANCHE_CODE"
git -C "$DEPOT" show "$COMMIT:echelle-v2/scripts/amorce_echelle_v2.sh" > "$T/amorce.sh"
git -C "$DEPOT" show "$COMMIT:echelle-v2/scripts/choisir_offre_v2.py" > "$T/choisir_offre_v2.py"
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
CHOIX=$(python3 -I -B "$T/choisir_offre_v2.py" "$T/offres-brut.json" "$T/offre.json" "$PRIX_MAX" "$DESCENTE_MAX" \
        "$PLAFOND_GO" "$T/lancement.txt" "$T/offres-relues.json") || c=$?
rm -f "$T/offres-brut.json"
[ "$c" = 3 ] && { echo "aucune offre conforme au plafond de $PLAFOND_GO USD : pas de création"; exit 3; }
[ "$c" = 0 ] || { echo "offres : relecture impossible (code $c)"; exit 2; }
read -r OFFRE DPH DESC DUREE_MAX_S PIRE <<< "$CHOIX"
[[ "$OFFRE" =~ ^[0-9]+$ ]] && [[ "$DUREE_MAX_S" =~ ^[0-9]+$ ]] || { echo "offre choisie illisible"; exit 2; }
echo "offre choisie : $OFFRE ($DPH USD/h ; descente $DESC USD/Go ; plafond de durée $DUREE_MAX_S s ; dépense au pire $PIRE USD), au coût estimé le plus bas des offres conformes" | tee -a "$T/lancement.txt"
# 7. crédit exigé (aucune valeur relue n'est insérée dans du code)
c=0
CREDIT_LIGNE=$("$V" show user --raw 2>/dev/null | python3 -I -B -c '
import json, math, sys
heures, pire, autres = (float(x) for x in sys.argv[1:4])
try:
    credit = json.load(sys.stdin)["credit"]
    assert isinstance(credit, (int, float)) and not isinstance(credit, bool) and math.isfinite(credit)
except Exception:
    print("crédit illisible"); sys.exit(2)
m = round(pire + heures * autres + 1.2, 2)
print(f"dépense au pire {pire:.2f} USD ; autres projets en marche {autres:.4f} USD/h ; crédit {credit:.2f} USD ; minimum {m:.2f} USD")
sys.exit(0 if round(credit, 2) >= m else 3)' "$HEURES_CREDIT" "$PIRE" "$SOMME_AUTRES") || c=$?
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
printf 'go %s\noffre %s\nbranche des résultats %s\netiquette %s\ncreation %s\nplafond de la surveillance %s (création + %s s ; DUREE_MAX_S=%s surveiller_echelle_v2.sh <id> %s <dossier neuf>)\ninstance : arrêtée par son identifiant à la fin (R10), détruite par son identifiant après vérification des résultats poussés\n' \
    "$GO" "$OFFRE" "$BRANCHE" "$ETIQUETTE" "$CREATION" "$((CREATION + DUREE_MAX_S))" "$DUREE_MAX_S" "$DUREE_MAX_S" "$CREATION" >> "$T/lancement.txt"
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
