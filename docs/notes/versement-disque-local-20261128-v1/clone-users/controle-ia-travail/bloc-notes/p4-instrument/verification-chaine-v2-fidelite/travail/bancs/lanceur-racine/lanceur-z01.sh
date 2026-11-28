#!/usr/bin/env bash
# Création de l'instance de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269 ; préenregistrement
# prereg/P4-instrument-v1.md), v1, déclinée de docs/procedures/P3-premier-test-v2/lancer_p3_v1.sh sous un nom neuf (R12).
# Ce qui change (texte de P4, en-tête « GO et dépense », Plan d'analyse, points 1 et 7, Liste d'arrêt, Chaîne de
# lancement ; plan v2, section 4) : GO cité par la commande de création GO-2026-10-20-07, seul accepté ; contrôles du GO,
# de la révocation (ligne de GO de type « révocation » qui nomme GO-2026-10-04-08, GO-2026-10-20-06, GO-2026-10-20-07,
# R-262 ou R-269 ; ligne R-… dont la cellule de décision commence par « **Révocation de R-262** » ou « **Révocation de
# R-269** »), du plafond par lancement (colonne « plafond » de GO-2026-10-20-07 qui commence par « 10 USD par
# lancement »), de l'échéance (colonne du GO cité), de la borne de l'étape (5,41 USD, strictement inférieure à 10 USD),
# de l'accord du jour (« **Accord de Lazar pour le lancement de P4-instrument** », qui cite GO-2026-10-20-07 ou un
# message de Lazar du jour) et de la garde de calcul gelée : fonctions du module de P4, par verifications_p4_v1.py
# (le même texte que le scellement et les contrôles), puis lignes de commande du module telles quelles juste avant la
# création (`--controle module`, `--controle go`) ; crédit exigé sur 3,0 heures ; surveillance à la création + 9 600 s ;
# instance 56799469 (P3) tolérée si relue arrêtée, tant qu'elle existe ; vingt et un scripts de la chaîne de P4 égaux à
# leurs copies versées à S (docs/procedures/P4-instrument-v1/) ; huit journaux de preuve ; amorce et script de l'instance
# cités par le texte. Chaîne v2 : accord absent du registre des décisions au commit S (consigné après S,
# RC-fidelite-08) ; accord à la forme de la dépense de la phase (« dépense consignée X USD + borne 5,41 USD = Y USD <
# 150 USD », somme refaite, RC-depense-05) et au GO cité à frontières de mot (RC-depense-09), par le module commun ;
# révocations sous des formes voisines refusées (code 2, RC-depense-03) ; garde de calcul gelée égale à celle de S et
# d'empreinte 579f65c8… avant chaque rejeu (RC-depense-04) ; GO et dépense relus sur les registres courants juste avant
# la création, après le choix de l'offre (RC-depense-08) ; un accord, un lancement : marqueur du commit S écrit avant la
# création (dossier fixe des marqueurs et dossier des traces), refus si un marqueur de S existe (dossier fixe ou dossier
# de traces voisin) ou si la branche de résultats existe sur le dépôt distant (RC-depense-10) ; lignes de
# lancement.txt écrites et relues avant de quitter le mode d'arrêt sur erreur (RC-depense-11). Repris tels quels de P3 : filtre d'offre (A100 SXM4 80 Go sur AMD EPYC 7513, une carte, au plus
# 1,30 USD de l'heure, au moins 16 cœurs effectifs et 128 000 Mo de mémoire vive, téléchargement au plus 0,05 USD par Go,
# stockage au plus 0,03 USD de l'heure ; la moins chère des conformes ; à prix égal, le plus petit identifiant), offres
# relues gardées, autres projets de Lazar nommés en argument et tolérés seulement à l'étiquette « rr- », crédit calculé
# dans un programme qui relit la réponse, garde de calcul rejouée sur la commande de création (jamais contournée),
# heure (pas de création entre 23:30 et 00:00), place disque, jetons jamais affichés, aucun relancement. Pendant
# l'appel, aucun sous-agent ne tourne (R-234). Aucune création si un contrôle échoue.
# Codes : 0 création ; 3 heure, place, crédit, prix ou aucune offre conforme ; 4 tout échec à partir de la ligne
# « creation » de lancement.txt (création douteuse : vérifier les instances, forme filtrée, jamais --raw sans filtre) ;
# 2 tout autre arrêt avant.
# Usage : lancer_p4_v1.sh DOSSIER_TRACES AUTRES_PROJETS ACCORD
#   AUTRES_PROJETS : identifiants d'instances d'autres projets de Lazar séparés par des virgules, ou « - » ;
#   ACCORD : identifiant de la ligne R-… du registre des décisions qui consigne l'accord de Lazar du jour.
set -euo pipefail
trap 'echo "arrêt avant la création (ligne $LINENO)"; exit 2' ERR
[ $# -eq 3 ] && [ -n "$1" ] && [ -n "$2" ] && [ -n "$3" ] || { echo "usage : lancer_p4_v1.sh DOSSIER_TRACES AUTRES_PROJETS ACCORD"; exit 2; }
T=$(realpath -m "$1"); AUTRES=$2; ACCORD=$3; OFFRE=""                    # traces en chemin absolu
[[ "$(basename "$1")" =~ ^[0-9]+$ ]] && { echo "DOSSIER_TRACES purement numérique ($1) : refusé (une offre n'est jamais passée en argument)"; exit 2; }
[[ "$AUTRES" = "-" || "$AUTRES" =~ ^[0-9]{6,10}(,[0-9]{6,10})*$ ]] \
    || { echo "AUTRES_PROJETS : identifiants d'instances séparés par des virgules, ou « - »"; exit 2; }
[[ "$ACCORD" =~ ^R-[0-9]{3,4}$ ]] || { echo "ACCORD : identifiant R-… de la ligne qui consigne l'accord de Lazar du jour attendu"; exit 2; }
PRIX_MAX=1.30                                    # filtre d'offre de P3 (texte de P4, Plan d'analyse, point 7)
HEURES_CREDIT=3.0                                # crédit exigé : 3 heures × (prix de l'offre + autres projets en marche) + 1,2 USD
PLAFOND_SURVEILLANCE_S=9600                      # surveiller_p4_v1.sh : création + 9 600 s
COEURS_MIN=16                                    # cœurs effectifs de l'offre, cpu_cores_effective
MEMOIRE_VIVE_MIN_MO=128000                       # mémoire vive de l'offre, cpu_ram en Mo
TELECHARGEMENT_MAX=0.05                          # téléchargement de l'offre, inet_down_cost en USD par Go
STOCKAGE_MAX=0.03                                # stockage de l'offre, storage_total_cost en USD de l'heure
ARRET_MIN=10                                     # arrêt en dix minutes (borne de l'étape)
TELECHARGEMENT_GO=20                             # téléchargement, environ 20 Go (borne de l'étape)
DISQUE_H=24                                      # disque de l'instance arrêtée, 24 heures au plus (borne de l'étape)
BORNE_ETAPE_USD=5.41                             # dépense de l'étape, bornée (texte, Plan d'analyse, point 7)
GO_CITE=GO-2026-10-20-07                         # seul GO accepté dans la commande de création (délégation R-269)
PREFIXE_AUTRES=rr-                               # étiquette des instances de l'autre projet de Lazar (liste positive)
DEPOT=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/verification-chaine-v2-fidelite/travail/bancs/lanceur-racine/depot
B=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/verification-chaine-v2-fidelite/travail/bancs/lanceur-racine/B
H=$B/p4-instrument/chaine-v2                     # bloc-notes de la chaîne de P4 (copies égales aux copies versées à S)
MARQUEURS=$B/p4-instrument/marqueurs-lancement-p4-v1   # un accord, un lancement : un marqueur par commit S (RC-depense-10)
V=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/verification-chaine-v2-fidelite/travail/bancs/lanceur-racine/bin-vastai/vastai
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERSEES=docs/procedures/P4-instrument-v1
P=prereg/P4-instrument-v1.md
A=$VERSEES/amorce_instance_p4_v1.sh
I=$VERSEES/p4_instance_v1.sh
MODULE=$VERSEES/instrument_p4_v1.py
BRANCHE=calcul/p4-reel-v1; ETIQUETTE=p4-v1
GARDE_SHA256=579f65c8ae3002d8e5c61698d636549b0401da3acff6bce718ae88e93664a6f2   # garde de calcul gelée (7a54d43)
ARRETEES_TOLEREES="A_EPINGLER"                     # instance de P3, gardée arrêtée jusqu'à sa destruction (R-257) : tolérée si relue arrêtée, tant qu'elle existe
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh
        repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh
        essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
PREUVES="banc-lanceur-p4-v1.log banc-surveillance-p4-v1.log banc-arret-p4-v1.log banc-traces-p4-v1.log
         banc-verifications-p4-v1.log banc-controles-p4-v1.log banc-scellement-p4-v1.log repetition-finale-p4-v1.log"
export PYTHONDONTWRITEBYTECODE=1
[[ "$ARRETEES_TOLEREES" =~ ^[0-9]{6,10}( [0-9]{6,10})*$ ]] || { echo "instances tolérées non épinglées"; exit 2; }
[[ "$TELECHARGEMENT_MAX" =~ ^0\.[0-9]{2,4}$ ]] || { echo "borne de téléchargement non fixée ($TELECHARGEMENT_MAX) : à reprendre du texte scellé"; exit 2; }
[[ "$STOCKAGE_MAX" =~ ^0\.[0-9]{2,4}$ ]] || { echo "borne de stockage non fixée ($STOCKAGE_MAX) : à reprendre du texte scellé"; exit 2; }
# borne de l'étape recalculée depuis les constantes ci-dessus, au centime par poste : égale à la valeur écrite, et
# strictement inférieure au plafond par lancement (10 USD ; le module le contrôle aussi)
python3 -c 'import sys
s, p, a, go, pg, dh, pd, b = (float(x) for x in sys.argv[1:9])
c = round(sum(round(x, 2) for x in (s / 3600 * p, a / 60 * p, go * pg, dh * pd)), 2)
sys.exit(0 if abs(c - b) < 1e-9 and b < 10 else 1)' "$PLAFOND_SURVEILLANCE_S" "$PRIX_MAX" "$ARRET_MIN" "$TELECHARGEMENT_GO" \
    "$TELECHARGEMENT_MAX" "$DISQUE_H" "$STOCKAGE_MAX" "$BORNE_ETAPE_USD" \
    || { echo "borne de l'étape ($BORNE_ETAPE_USD USD) ≠ calcul sur les constantes, ou au moins 10 USD : pas de création"; exit 2; }
[ -e "$T" ] && { echo "$T existe déjà (R12)"; exit 2; }
# 0. heure (la suite des tests de l'instance ne doit pas chevaucher minuit UTC, test_garde_calcul ; T-7) et place disque
H0=$(date -u +%H%M); [ "$H0" -lt 2330 ] || { echo "heure UTC $H0 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
LIBRE=$(df -Pk "$B" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 3; }
LIBRE_T=$(df -Pk "$(dirname "$T")" | awk 'NR==2 {print $4}'); [ "$LIBRE_T" -ge 3000000 ] || { echo "place disque des traces : $LIBRE_T ko"; exit 3; }
mkdir -p "$T"
trap 'rm -rf "$T/clone-controles" "$T/clone-controles.travail"' EXIT        # le clone des contrôles ne reste jamais
printf 'heure de départ %s UTC ; place libre %s ko\n' "$(date -u +%H:%M:%S)" "$LIBRE" >> "$T/lancement.txt"
# 1. commit de scellement, poussé sur le dépôt de travail ; texte de S extrait (lu par les contrôles du module)
S=$(git -C "$DEPOT" log --diff-filter=A -1 --format=%H -- "$P.sha256")
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement introuvable"; exit 2; }
git -C "$DEPOT" fetch -q origin main
git -C "$DEPOT" merge-base --is-ancestor "$S" origin/main || { echo "commit de scellement $S absent du dépôt distant"; exit 2; }
git -C "$DEPOT" show "$S:$P" > "$T/prereg-S.md"
# 1 bis. un accord, un lancement (RC-depense-10) : aucun marqueur de S (dossier fixe des marqueurs, dossiers de traces
# voisins) ; l'accord du jour est consigné après S (RC-fidelite-08) : absent du registre des décisions au commit S
MARQUEUR="$MARQUEURS/lancement-$S.txt"
marqueur_absent() {
    local v
    v=$(ls -d "$MARQUEUR" "$(dirname "$T")"/*/marqueur-lancement-"$S".txt 2>/dev/null | head -3 | tr '\n' ' ' || true)
    [ -z "$v" ] || { echo "un accord, un lancement : un lancement a déjà été tenté pour le commit S $S (marqueur : $v) : pas de création ; un nouveau lancement passe par un nœud de Lazar et un nouveau S"; exit 2; }
}
marqueur_absent
DEC_S=$(git -C "$DEPOT" show "$S:registres/decisions.md") || { echo "registre des décisions illisible au commit S : pas de création"; exit 2; }
if printf '%s\n' "$DEC_S" | grep -qE "^[[:space:]]*\|[[:space:]]*$ACCORD[[:space:]]*\|"; then
    echo "accord $ACCORD déjà présent dans registres/decisions.md au commit S : l'accord du jour se consigne après le scellement S (Chaîne de lancement) : pas de création"; exit 2
fi
unset DEC_S
# garde de calcul gelée : égale à celle de S et d'empreinte gelée, avant chaque rejeu (RC-depense-04)
garde_intacte() {
    git -C "$DEPOT" diff --quiet "$S" -- .claude/hooks/garde_calcul.py 2>/dev/null \
        && [ "$(sha256sum "$DEPOT/.claude/hooks/garde_calcul.py" 2>/dev/null | cut -d' ' -f1)" = "$GARDE_SHA256" ] \
        || { echo "garde de calcul modifiée (≠ celle de S, ou d'empreinte autre que $GARDE_SHA256) : aucun rejeu, pas de création"; exit 2; }
}
# 2. scripts égaux à leurs copies versées à S : les vingt et un scripts de la chaîne de P4 (liste CHAINE du scellement),
# dont la surveillance, le contrôle à cinq minutes et la récupération, qui tourneront après S ; le lanceur exécuté par
# son propre chemin
for s in $CHAINE; do
    f="$H/$s"; [ "$s" = lancer_p4_v1.sh ] && f=$0
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$f" | cut -d' ' -f1)" ] \
        || { echo "$s exécuté ≠ copie versée au commit S"; exit 2; }
done
# 2 bis. preuves des essais (R5) : journaux des bancs et de la répétition finale versés à S avec leur sceau exact, au
# verdict conforme ; chaque script éprouvé égal à sa copie versée à S
PREUVES_D=$(mktemp -d)
for j in $PREUVES; do
    git -C "$DEPOT" show "$S:$VERSEES/$j" > "$PREUVES_D/$j" 2>/dev/null || { rm -rf "$PREUVES_D"; echo "preuves des essais : journal $j absent de S"; exit 2; }
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$j.sha256" 2>/dev/null)" = "$(sha256sum "$PREUVES_D/$j" | cut -d' ' -f1)  $j" ] \
        || { rm -rf "$PREUVES_D"; echo "preuves des essais : sceau de $j absent ou non conforme à S"; exit 2; }
done
"$PY" -B "$H/verifications_p4_v1.py" preuves "$PREUVES_D" > "$PREUVES_D/sortie.txt" 2>&1 \
    || { m=$(tail -1 "$PREUVES_D/sortie.txt"); rm -rf "$PREUVES_D"; echo "preuves des essais : $m"; exit 2; }
while read -r s e; do
    [ "$(git -C "$DEPOT" show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] \
        || { rm -rf "$PREUVES_D"; echo "preuves des essais : $s éprouvé ($e) ≠ copie versée à S"; exit 2; }
done < "$PREUVES_D/sortie.txt"
echo "preuves des essais : huit journaux conformes ; $(wc -l < "$PREUVES_D/sortie.txt") scripts éprouvés égaux à leurs copies versées à S"
rm -rf "$PREUVES_D"
# accord de Lazar du jour, relu dans le registre courant des décisions par le module commun (fonction du module de P4,
# chargé à l'empreinte que cite le texte de S) : avant les contrôles et de nouveau après, au jour de la création
accord() {
    local j r
    j=$(date -u +%F)
    r=$(cd "$DEPOT" && PYTHONPATH=src "$PY" -B "$H/verifications_p4_v1.py" accord . "$T/prereg-S.md" "$ACCORD" "$j" 2>&1) \
        || { echo "accord de Lazar : $(printf '%s\n' "$r" | tail -1 | cut -c1-240) : pas de création"; return 1; }
    printf 'accord %s\n' "$r" >> "$T/lancement.txt"
    echo "accord de Lazar : $r"
}
accord || exit 2
# jetons présents (jamais affichés), avant les contrôles (suite complète des tests et mesures de conception rejouées)
[ -n "${HF_TOKEN:-}" ] && [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ] || { echo "jeton absent (HF_TOKEN ou CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
if ! timeout 5400 bash "$H/controles_avant_depense_p4_v1.sh" "$S" "$T/clone-controles" > "$T/controles.txt" 2>&1; then
    grep '^KO' "$T/controles.txt" | cut -c1-200 || tail -5 "$T/controles.txt"; echo "contrôles avant dépense en échec : pas de création"; exit 2
fi
tail -1 "$T/controles.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || { echo "contrôles : dernière ligne inattendue"; exit 2; }
rm -rf "$T/clone-controles" "$T/clone-controles.travail"
# 3. amorce et script de l'instance de S ; leurs empreintes doivent être citées (texte aux espaces réduites)
git -C "$DEPOT" show "$S:$A" > "$T/amorce.sh"
E=$(sha256sum "$T/amorce.sh" | cut -d' ' -f1)
EI=$(git -C "$DEPOT" show "$S:$I" | sha256sum | cut -d' ' -f1)
tr '\n' ' ' < "$T/prereg-S.md" | tr -s ' ' > "$T/prereg-S-plat.txt"
grep -qF "\`$A\` (\`$E\`, sha256)" "$T/prereg-S-plat.txt" || { echo "empreinte de l'amorce ($E) non citée par le préenregistrement"; exit 2; }
grep -qF "\`$I\` (\`$EI\`, sha256)" "$T/prereg-S-plat.txt" || { echo "empreinte du script de l'instance ($EI) non citée par le préenregistrement"; exit 2; }
rm -f "$T/prereg-S-plat.txt"
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$T/prereg-S.md" || { echo "PREREG ou BRANCHE : le préenregistrement de S cite autre chose"; exit 2; }
# GO cité par S, relu dans les registres courants : ligne « **GO cité par la commande de création** » du texte
# (GO-2026-10-20-07 seul), puis fonctions du module (type, Lazar, plafond, échéance, borne, révocations ; garde gelée)
JOUR=$(date -u +%F)
garde_intacte
GOP4=$(cd "$DEPOT" && PYTHONPATH=src "$PY" -B "$H/verifications_p4_v1.py" go . "$T/prereg-S.md" "$JOUR" "$BORNE_ETAPE_USD" 2>&1) \
    || { printf '%s\n' "$GOP4" | tail -6 | head -5 | cut -c1-240; echo "GO et dépense : $(printf '%s\n' "$GOP4" | tail -1 | cut -c1-240) : pas de création"; exit 2; }
printf 'go et dépense %s\n' "$GOP4" >> "$T/lancement.txt"
GOP4=${GOP4%% *}
# forme de la sortie du module commun : garde redondante (il n'écrit que ce GO), sans artefact possible
[ "$GOP4" = "$GO_CITE" ] || { echo "GO et dépense : sortie du module commun illisible"; exit 2; }
# contrôles du module de P4, tels quels (ligne de commande), sur le texte de S et les registres courants : module cité,
# puis GO, accord du jour et garde de calcul gelée ensemble
(cd "$DEPOT" && PYTHONPATH=src "$PY" -B "$MODULE" --controle module --prereg "$T/prereg-S.md") > "$T/controle-module.txt" 2>&1 \
    || { echo "contrôle du module (--controle module) : $(tail -1 "$T/controle-module.txt" | cut -c1-200) : pas de création"; exit 2; }
(cd "$DEPOT" && PYTHONPATH=src "$PY" -B "$MODULE" --controle go --go "$GOP4" --accord "$ACCORD" --jour "$JOUR" --borne "$BORNE_ETAPE_USD") \
    > "$T/controle-go.txt" 2>&1 || { echo "contrôle du GO (--controle go) : $(tail -1 "$T/controle-go.txt" | cut -c1-200) : pas de création"; exit 2; }
printf 'contrôles du module : %s ; %s\n' "$(tail -1 "$T/controle-module.txt" | cut -c1-120)" "$(tail -1 "$T/controle-go.txt" | cut -c1-200)" >> "$T/lancement.txt"
accord || exit 2
B64=$(base64 -w0 < "$T/amorce.sh")
# aller-retour de l'encodage de l'amorce : garde redondante, sans artefact possible
[ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$E" ] || { echo "encodage de l'amorce"; exit 2; }
# 5. offre : relue par le filtre de P3 après les contrôles (bloc repris tel quel du lanceur de P3)
EXCLUES=-                                        # aucun relancement dans ce lanceur : aucune offre écartée
"$V" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw > "$T/offres-brut.json"
c=0                                              # « … || c=$? » : ni set -e ni le piège ERR ne jouent sur l'affectation
CHOIX=$(python3 - "$T/offres-brut.json" "$T/offre.json" "$PRIX_MAX" "$T/lancement.txt" "$T/offres-relues.json" "$EXCLUES" \
        "$COEURS_MIN" "$MEMOIRE_VIVE_MIN_MO" "$TELECHARGEMENT_MAX" "$STOCKAGE_MAX" <<'EOF'
import json, math, sys
brut, sortie, prix_max, journal, relues, exclusion = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
coeurs_min, ram_min, tel_max, sto_max = float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9]), float(sys.argv[10])
exclues = set() if exclusion == "-" else set(exclusion.split())
try:
    offres = json.load(open(brut))
except Exception:
    print("offres : réponse illisible", file=sys.stderr); sys.exit(2)
if not isinstance(offres, list):
    print("offres : liste attendue", file=sys.stderr); sys.exit(2)
extrait = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cpu_name", "cpu_cores_effective", "cpu_ram",
           "dph_total", "inet_down_cost", "storage_total_cost", "end_date")
json.dump([{k: o.get(k) for k in extrait} if isinstance(o, dict) else {"illisible": type(o).__name__} for o in offres],
          open(relues, "w"), indent=1)
vus = [repr(o.get("id")) for o in offres if isinstance(o, dict)]
if len(vus) != len(set(vus)):
    print("offres : identifiant en double dans la réponse (ambiguë) : pas de création", file=sys.stderr); sys.exit(2)
def nombre(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
def prix(o):
    p = o.get("dph_total")
    return float(p) if nombre(p) and p > 0 else None
def entier(v):
    return isinstance(v, int) and not isinstance(v, bool)
def exclue(o):
    if not exclues:
        return False
    m, h = o.get("machine_id"), o.get("host_id")
    if not (entier(m) and entier(h)):
        return True                  # en relancement, une offre sans machine ou hôte lisible ne prouve rien : écartée
    return f"machine:{m}" in exclues or f"hote:{h}" in exclues
conformes = [o for o in offres if isinstance(o, dict) and entier(o.get("id"))
             and o.get("gpu_name") == "A100 SXM4" and o.get("cpu_name") == "AMD EPYC 7513 32-Core Processor"
             and nombre(o.get("gpu_ram")) and o["gpu_ram"] >= 79000 and entier(o.get("num_gpus")) and o["num_gpus"] == 1
             and nombre(o.get("cpu_cores_effective")) and o["cpu_cores_effective"] >= coeurs_min
             and nombre(o.get("cpu_ram")) and o["cpu_ram"] >= ram_min
             and nombre(o.get("inet_down_cost")) and 0 <= o["inet_down_cost"] <= tel_max
             and nombre(o.get("storage_total_cost")) and 0 <= o["storage_total_cost"] <= sto_max
             and prix(o) is not None and prix(o) <= prix_max]
ecartees = [o for o in conformes if exclue(o)]
conformes = sorted((o for o in conformes if not exclue(o)), key=lambda o: (prix(o), o["id"]))
with open(journal, "a", encoding="utf-8") as j:
    j.write("offres conformes relues : " + (", ".join(
        f"{o['id']} ({prix(o):.4f} USD/h ; machine {o.get('machine_id')} ; hôte {o.get('host_id')} ; "
        f"cœurs effectifs {o.get('cpu_cores_effective')} ; mémoire vive {o.get('cpu_ram')} Mo ; "
        f"téléchargement {o.get('inet_down_cost')} USD/Go ; stockage {o.get('storage_total_cost')} USD/h ; "
        f"fin {o.get('end_date')})" for o in conformes) or "aucune") + "\n")
    if exclues:
        j.write("offres conformes écartées (machine ou hôte du premier lancement, ou illisibles) : "
                + (", ".join(str(o["id"]) for o in ecartees) or "aucune") + "\n")
if not conformes:
    print(f"aucune offre conforme au filtre du plan au plus {prix_max} USD/h (au moins {coeurs_min:g} cœurs effectifs, "
          f"{ram_min:g} Mo de mémoire vive, téléchargement au plus {tel_max} USD/Go, stockage au plus {sto_max} USD/h) : "
          f"pas de création", file=sys.stderr)
    sys.exit(3)
o = conformes[0]
champs = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cuda_max_good", "driver_version", "cpu_name",
          "cpu_arch", "cpu_cores", "cpu_cores_effective", "cpu_ram", "disk_space",
          "reliability2", "verification", "hosting_type", "rentable", "end_date", "dph_total", "storage_total_cost",
          "inet_down_cost", "inet_up_cost", "geolocation")
json.dump({k: o.get(k) for k in champs}, open(sortie, "w"), indent=1)
print(o["id"], prix(o))
EOF
) || c=$?
[ -s "$T/offres-relues.json" ] || head -c 2000 "$T/offres-brut.json" > "$T/offres-relues-brut.txt"
rm -f "$T/offres-brut.json"
[ "$c" = 3 ] && exit 3
[ "$c" = 0 ] || { echo "offres : relecture impossible (code $c)"; exit 2; }
OFFRE=${CHOIX%% *}; DPH=${CHOIX#* }
echo "offre choisie : $OFFRE ($DPH USD/h), la moins chère des offres conformes" | tee -a "$T/lancement.txt"
# prix au-dessus du devis après le choix : garde redondante (le filtre local l'exclut déjà), sans artefact possible
python3 -c 'import sys; sys.exit(0 if float(sys.argv[1]) <= float(sys.argv[2]) else 1)' "$DPH" "$PRIX_MAX" \
    || { echo "prix $DPH USD/h au-dessus du devis ($PRIX_MAX) : nœud, pas de création"; exit 3; }
# instances : aucune, hors l'instance de P3 arrêtée tolérée (relue arrêtée) et les instances d'autres projets nommées en
# argument, dont l'étiquette commence par « rr- » (liste positive) ; seuls identifiants, états, étiquettes et prix
# s'affichent ; la somme des prix de celles qui sont en marche entre dans le crédit exigé
SOMME_AUTRES=$("$V" show instances --raw | python3 -c '
import json, sys
tol = set(sys.argv[1].split())
decl = set() if sys.argv[2] == "-" else set(sys.argv[2].split(","))
prefixe = sys.argv[4]
journal = open(sys.argv[3], "a", encoding="utf-8")
try:
    instances = json.load(sys.stdin)
    assert isinstance(instances, list)
except Exception:
    print("vastai show instances : réponse illisible ou commande en échec", file=sys.stderr); sys.exit(3)
vues, autres_vues, refusees, somme = [], [], [], 0.0
for i in instances:
    if not isinstance(i, dict):
        refusees.append("entrée illisible"); continue
    ident, etat, cur = str(i.get("id")), i.get("actual_status"), i.get("cur_state")
    etiquette = str(i.get("label") or "")
    arretee = etat in ("exited", "stopped") and cur == "stopped"
    if ident in tol and arretee:
        vues.append(f"{ident} ({etat}, {cur})")
    elif ident in decl and etiquette.startswith(prefixe):
        dph = i.get("dph_total")
        if isinstance(dph, bool) or not isinstance(dph, (int, float)):
            refusees.append(f"{ident} (prix illisible)")
            continue
        if not arretee:
            somme += float(dph)
        statut = "arrêtée" if arretee else "en marche, comptée"
        autres_vues.append(f"{ident} ({etat}, {cur}, {float(dph):.3f} USD/h, {statut})")
    else:
        refusees.append(f"{ident} ({etat}, {cur})")
lignes = ["instances arrêtées tolérées : " + (", ".join(vues) or "aucune"),
          "instances d\u0027autres projets tolérées : " + (", ".join(autres_vues) or "aucune")]
if refusees:
    lignes.append("autres instances sur le compte (non tolérées ; autre projet : étiquette « " + prefixe + "… » exigée) : " + ", ".join(refusees))
for ligne in lignes:
    print(ligne, file=sys.stderr)
    journal.write(ligne + "\n")
journal.close()
if refusees:
    sys.exit(1)
print(f"{somme:.4f}")' "$ARRETEES_TOLEREES" "$AUTRES" "$T/lancement.txt" "$PREFIXE_AUTRES") \
    || { echo "instances : non tolérée(s), ou liste illisible (voir la ligne ci-dessus) : pas de création"; exit 2; }
# crédit exigé : calculé dans un programme qui relit la réponse et en vérifie la forme ; aucune valeur relue n'est
# insérée dans du code (CH-22)
c=0
CREDIT_LIGNE=$("$V" show user --raw 2>/dev/null | python3 -c '
import json, math, sys
heures, dph, autres = (float(x) for x in sys.argv[1:4])
try:
    credit = json.load(sys.stdin)["credit"]
except Exception:
    print("crédit illisible (vastai show user)"); sys.exit(2)
if isinstance(credit, bool) or not isinstance(credit, (int, float)) or not math.isfinite(credit):
    print("crédit illisible (vastai show user)"); sys.exit(2)
m = round(heures * (dph + autres) + 1.2, 2)
print(f"prix {dph:.4f} USD/h ; autres projets en marche {autres:.4f} USD/h ; crédit {credit:.2f} USD ; minimum {m:.2f} USD ({heures:g} h)")
sys.exit(0 if round(credit, 2) >= m else 3)' "$HEURES_CREDIT" "$DPH" "$SOMME_AUTRES") || c=$?
printf '%s\n' "$CREDIT_LIGNE" | tee -a "$T/lancement.txt"
case $c in
    0) ;;
    3) echo "crédit insuffisant pour P4 et les autres projets en marche : pas de lancement ; recharge demandée à Lazar"; exit 3 ;;
    *) echo "crédit illisible (vastai show user, code $c) : pas de création"; exit 2 ;;
esac
# 5 bis. GO et dépense relus sur les registres courants juste avant la création, après le choix de l'offre et le crédit
# (RC-depense-08 : une révocation consignée pendant l'appel, sous toute forme, arrête ici)
garde_intacte
GO_RELU=$(cd "$DEPOT" && PYTHONPATH=src "$PY" -B "$H/verifications_p4_v1.py" go . "$T/prereg-S.md" "$(date -u +%F)" "$BORNE_ETAPE_USD" 2>&1) \
    || { printf '%s\n' "$GO_RELU" | tail -6 | head -5 | cut -c1-240; echo "GO et dépense relus juste avant la création : $(printf '%s\n' "$GO_RELU" | tail -1 | cut -c1-240) : pas de création"; exit 2; }
printf 'go et dépense relus juste avant la création %s\n' "$GO_RELU" >> "$T/lancement.txt"
# 6. garde de calcul gelée rejouée sur la commande de création, avec le GO validé (elle lit le registre du dépôt de
# travail ; jamais contournée : son refus arrête ici, par le piège ERR, sans création)
garde_intacte
printf '{"tool_input":{"command":"GO_ID=%s vastai create instance %s --raw --image python:3.11-bookworm --disk 80"}}' "$GOP4" "$OFFRE" \
    | python3 "$DEPOT/.claude/hooks/garde_calcul.py"
# 7. création : heure relue juste avant ; branche de résultats absente du dépôt distant et marqueur de S écrit (un
# accord, un lancement) ; lignes de lancement.txt écrites et relues avant de quitter le mode d'arrêt sur erreur
# (RC-depense-11) ; à partir de la sortie de ce mode, tout échec rend 4
H1=$(date -u +%H%M); [ "$H1" -lt 2330 ] || { echo "heure UTC $H1 : pas de création entre 23:30 et 00:00 (T-7)"; exit 3; }
c=0; git -C "$DEPOT" ls-remote --exit-code origin "refs/heads/$BRANCHE" > /dev/null 2>&1 || c=$?
[ "$c" = 2 ] || { echo "branche $BRANCHE : code $c (2 attendu : absente du dépôt distant) : un accord, un lancement : pas de création"; exit 2; }
marqueur_absent
CREATION=$(date -u +%s)
mkdir -p "$MARQUEURS"
( set -C; printf 'lancement de P4-instrument : commit S %s ; accord %s ; dossier des traces %s ; offre %s ; marqueur écrit le %s avant la création\n' \
    "$S" "$ACCORD" "$T" "$OFFRE" "$(date -u +%FT%TZ)" > "$MARQUEUR" ) || { echo "marqueur de lancement $MARQUEUR non écrit (déjà présent ?) : pas de création"; exit 2; }
cp "$MARQUEUR" "$T/marqueur-lancement-$S.txt"
printf 'lanceur p4 v1 %s ; autres projets %s\ncommit %s\noffre %s\nprereg %s\nbranche %s\netiquette %s\ngo %s\nborne de l etape %s USD (plafond par lancement : colonne « plafond » de %s)\ncreation %s\nmarqueur %s\nplafond de la surveillance %s (création + %s s ; surveiller_p4_v1.sh <id> %s <dossier neuf>)\ncontrôle à cinq minutes entre %s et %s (création + 180 à 300 s ; controle_cinq_minutes_p4_v1.sh <id> %s <dossier neuf>)\narrêt de l instance par son identifiant : arreter_p4_v1.sh <id> <dossier neuf> (appelé par la surveillance à sa sortie et par le contrôle à cinq minutes en échec)\ninstance : détruite par son identifiant après la récupération vérifiée (recuperation_p4_v1.sh %s <id> %s <dossier neuf>), 24 heures au plus après l arrêt (R10 ; texte, Plan d analyse, point 7)\ntraces de la session : controler_traces_p4_v1.sh <dossier des traces de la session> avant tout versement\n' \
    "$(sha256sum "$0" | cut -d' ' -f1)" "$AUTRES" "$S" "$OFFRE" "$P" "$BRANCHE" "$ETIQUETTE" "$GOP4" "$BORNE_ETAPE_USD" "$GOP4" "$CREATION" "$MARQUEUR" \
    "$((CREATION + PLAFOND_SURVEILLANCE_S))" "$PLAFOND_SURVEILLANCE_S" "$T" "$((CREATION + 180))" "$((CREATION + 300))" "$T" "$S" "$T" >> "$T/lancement.txt"
for x in "commit $S" "offre $OFFRE" "branche $BRANCHE" "etiquette $ETIQUETTE" "go $GOP4" "creation $CREATION" "marqueur $MARQUEUR"; do
    [ "$(grep -cxF -- "$x" "$T/lancement.txt")" = 1 ] || { echo "lancement.txt : ligne « $x » non relue une fois : pas de création"; exit 2; }
done
for x in "lanceur p4 v1 " "plafond de la surveillance $((CREATION + PLAFOND_SURVEILLANCE_S)) (création + $PLAFOND_SURVEILLANCE_S s ; surveiller_p4_v1.sh <id> $T " \
         "contrôle à cinq minutes entre $((CREATION + 180)) et $((CREATION + 300)) (création + 180 à 300 s ; controle_cinq_minutes_p4_v1.sh <id> $T " \
         "instance : détruite par son identifiant après la récupération vérifiée (recuperation_p4_v1.sh $S <id> $T "; do
    [ "$(grep -cF -- "$x" "$T/lancement.txt")" = 1 ] || { echo "lancement.txt : ligne « ${x:0:60}… » non relue une fois : pas de création"; exit 2; }
done
trap - ERR
set +e
export T_LANCEMENT="$T"
GO_ID="$GOP4" "$V" create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label "$ETIQUETTE" \
    --env "-e COMMIT=$S -e PREREG=$P -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
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
