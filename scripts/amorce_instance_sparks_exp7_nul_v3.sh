#!/usr/bin/env bash
# Amorce de l'instance de SPARKS-EXP7-NUL, v3 (version neuve de `amorce_instance_sparks_exp7_nul_v2.sh`, R12 ; contre-lecture
# du delta v2, points 21 à 23 ; modèle de la minuterie : `amorce_sonde_hote_durable_a1_v3_v4.sh` et la sonde A1-v3 v4).
# Relancée telle quelle à chaque démarrage (`vastai start` relance les arguments du conteneur, avec l'environnement de la
# création). Ordre, sans Python avant la minuterie :
#   0. `curl` et `git` exigés : absents, refus visible, rien ne part ;
#   1. MINUTERIE DE DESTRUCTION, en tout premier, détachée (`setsid`), en bash et `curl` seuls : échéance absolue posée à la
#      création (`ECHEANCE_UTC_S`, au plus la fin du 18 novembre), gardée sur le disque (un redémarrage garde l'échéance
#      d'origine) ; à l'échéance, ou dès que la machine pose `sparks-v3-detruire` (fin du contrôle causal après poussée
#      vérifiée, ordre « fin »), `DELETE /instances/<CONTAINER_ID>/` (clé du conteneur), et en repli
#      `vastai destroy instance <id> -y` si `vastai` est là (R-1482 ; aucune sortie brute gardée, R-1480) ; recommence
#      chaque minute ; **jamais d'arrêt** de la machine par ce code (il tuerait la minuterie) : le processus principal
#      attend la fin de la minuterie quand une destruction est due ;
#   2. démarrage après l'échéance : aucun calcul, destruction ;
#   3. création (aucun `amorce-depot` sur le disque) : clone partiel et clairsemé, GO (base et extension à 40 USD), durée
#      bornée (`depense duree`, DEJA_USD de l'environnement, 0 à la création), garde du code, fabrication sous `timeout` ;
#   4. redémarrage (disque existant) : commit sur le disque = COMMIT, GO revu à la date, **ordre écrit** lu à la tête de
#      la branche `calcul/sparks-exp7-nul-v3-ordres` (`redemarrage.py verifier` : numéro neuf, phase, `deja_usd` relu à
#      chaque démarrage pour la borne), puis copie d'un lot (conteneur en vie `copie_minutes`, puis sortie), contrôle
#      causal (sous `timeout`, poussée vérifiée, puis destruction), ou fin (destruction).
# Variables : COMMIT, COMMIT_CODE, GH_TOKEN, HF_TOKEN, PRIX_HEURE_USD, PRIX_STOCKAGE_HEURE_USD, ECHEANCE_UTC_S, DEJA_USD (0) ;
# posées par Vast : CONTAINER_ID, CONTAINER_API_KEY (jamais affichées). Essai local : DEPOT_URL, RACINE_AMORCE, MODE=jouet,
# GO_DATE, VENV_EXISTANT, MINUTERIE_PAS_S, MINUTERIE_REESSAI_S, MINUTERIE_MARGE_S.
set -uo pipefail
R="${RACINE_AMORCE:-/root}"
API=https://console.vast.ai/api/v0
FIN_GO=1795046400            # 2026-11-19T00:00:00Z
GO_ID=GO-2026-11-04-04
BRANCHE_ORDRES=calcul/sparks-exp7-nul-v3-ordres
export HOME="${HOME:-/root}"
cd "$R" || exit 1
echo "AMORCE V3 $(date -u +%FT%TZ) : machine ${CONTAINER_ID:-?}, commit ${COMMIT:-?}"
command -v curl >/dev/null 2>&1 || { echo "AMORCE V3 : curl absent : refus, rien ne part (la minuterie en a besoin)"; exit 2; }
command -v git >/dev/null 2>&1 || { echo "AMORCE V3 : git absent : refus, rien ne part"; exit 2; }
E="$R/sparks-v3-echeance.txt"
if [ -s "$E" ]; then read -r ECH < "$E"; else
    ECH="${ECHEANCE_UTC_S:-}"
    case "$ECH" in ''|*[!0-9]*) echo "AMORCE V3 : ECHEANCE_UTC_S absente ou non entière : refus, rien ne part"; exit 2;; esac
    [ "$ECH" -le "$FIN_GO" ] || ECH=$FIN_GO
    echo "$ECH" > "$E"
fi
case "$ECH" in ''|*[!0-9]*) echo "AMORCE V3 : échéance du disque illisible : refus"; exit 2;; esac
cat > "$R/sparks-v3-minuterie.sh" <<'MINUTERIE'
ECH="$1"; R="$2"; API="$3"; J="$R/sparks-v3-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH" >> "$J"
echo "$$" > "$R/sparks-v3-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/sparks-v3-detruire" ]; do sleep "$PAS"; done
raison="échéance"; [ -e "$R/sparks-v3-detruire" ] && raison="ordre de la machine"
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do  # jamais d'arrêt de la machine : il tuerait cette minuterie ; le DELETE recommence jusqu'à la fin de la marge
    n=$((n + 1))
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n, $raison) : HTTP $c" >> "$J"
    case "$c" in 2??) echo "$(date -u +%FT%TZ) instance $CONTAINER_ID détruite" >> "$J"; exit 0;; esac
    if command -v vastai >/dev/null 2>&1; then
        vastai destroy instance "$CONTAINER_ID" -y >/dev/null 2>&1; v=$?
        echo "$(date -u +%FT%TZ) repli : vastai destroy instance $CONTAINER_ID -y : code $v (sortie non gardée)" >> "$J"
        [ "$v" = 0 ] && exit 0
    fi
    [ "$(date +%s)" -lt "$FIN" ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue" >> "$J"; exit 4; }
    sleep "$REESSAI"
done
MINUTERIE
setsid bash "$R/sparks-v3-minuterie.sh" "$ECH" "$R" "$API" < /dev/null >> "$R/sparks-v3-minuterie.log" 2>&1 &
echo "AMORCE V3 : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null || echo "?"))"
attendre_minuterie() {   # le conteneur reste en vie tant que la minuterie détruit (borné)
    local lim=$(( $(date +%s) + ${MINUTERIE_MARGE_S:-1800} + 120 )) p
    sleep 1; p=$(cat "$R/sparks-v3-minuterie.pid" 2>/dev/null || echo 0)
    while [ "$p" -gt 0 ] && kill -0 "$p" 2>/dev/null && [ "$(date +%s)" -lt "$lim" ]; do sleep 2; done
}
detruire() { echo "$1" > "$R/sparks-v3-detruire"; echo "AMORCE V3 : destruction demandée ($1)"; attendre_minuterie; exit "${2:-0}"; }
[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun calcul"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'
P2=src/controle_ia/sparks_exp7_nul_v2; P3=src/controle_ia/sparks_exp7_nul_v3
: "${COMMIT:?COMMIT absent}" "${COMMIT_CODE:?COMMIT_CODE absent}"
: "${PRIX_HEURE_USD:?PRIX_HEURE_USD absent}" "${PRIX_STOCKAGE_HEURE_USD:?PRIX_STOCKAGE_HEURE_USD absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"; export DEPOT_URL
go_conforme() { (cd "$R/amorce-depot" && python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import go; sys.exit(go.main(sys.argv[1:]))" registres/go.md ${GO_DATE:+"$GO_DATE"}); }
duree() { (cd "$R/amorce-depot" && python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import depense; sys.exit(depense.main(sys.argv[1:]))" duree "$PRIX_HEURE_USD" "$PRIX_STOCKAGE_HEURE_USD" "$1"); }
if [ ! -d "$R/amorce-depot/.git" ]; then
    echo "AMORCE V3 : création"
    [ -e "$R/sparks" ] && { echo "AMORCE V3 : $R/sparks sans dépôt (R11, R12) : refus"; exit 2; }
    git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$R/amorce-depot" \
        || { echo "AMORCE V3 : clonage impossible"; exit 2; }
    git -C "$R/amorce-depot" config credential.helper "$AIDE"
    git -C "$R/amorce-depot" sparse-checkout set --no-cone '/*' '!/*/' '/src/' '/scripts/' '/registres/go.md' '/prereg/SPARKS-EXP7-NUL-*' \
        && git -C "$R/amorce-depot" checkout -q "$COMMIT" || { echo "AMORCE V3 : commit $COMMIT introuvable"; exit 2; }
    go_conforme || { echo "AMORCE V3 : $GO_ID non conforme (base et extension à 40 USD) : aucun calcul"; exit 2; }
    MINUTES=$(duree "${DEJA_USD:-0}") || { echo "AMORCE V3 : prix illisibles : aucun calcul"; exit 2; }
    [ "$MINUTES" -ge 60 ] || { echo "AMORCE V3 : plafond trop bas pour ce prix ($MINUTES min) : aucun calcul"; exit 2; }
    (cd "$R/amorce-depot" && python3 -I -B -c "import sys; sys.path.insert(0, '$P3'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$COMMIT_CODE" "$COMMIT") \
        || { echo "AMORCE V3 : code ou addendum non conformes : aucun calcul"; exit 2; }
    echo "AMORCE V3 : fabrication, durée plafonnée à $MINUTES minutes"
    timeout --signal=TERM --kill-after=5m "${MINUTES}m" env COMMIT="$COMMIT" COMMIT_CODE="$COMMIT_CODE" TRAVAIL="$R/sparks" \
        GO_ID="$GO_ID" PHASE=fabrication bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v3.sh"
    code=$?; echo "AMORCE V3 $(date -u +%FT%TZ) : fin de la fabrication, code $code (le conteneur sort ; instance arrêtée)"; exit $code
fi
echo "AMORCE V3 : redémarrage"
[ "$(git -C "$R/amorce-depot" rev-parse HEAD)" = "$COMMIT" ] || { echo "AMORCE V3 : commit du disque ≠ COMMIT : refus"; exit 2; }
go_conforme || { echo "AMORCE V3 : $GO_ID non conforme à la date : aucun calcul"; exit 2; }
O="$R/sparks-ordres-$(date -u +%Y%m%dT%H%M%S)"
mkdir "$O" && git -C "$R/amorce-depot" -c credential.helper="$AIDE" fetch -q --depth 1 origin "$BRANCHE_ORDRES" \
    && git -C "$R/amorce-depot" archive FETCH_HEAD ordres | tar -x -C "$O" || { echo "AMORCE V3 : ordres illisibles : refus"; exit 2; }
L=$(python3 -I -B "$R/amorce-depot/$P3/redemarrage.py" verifier "$O/ordres" "$R/sparks-v3-ordres-faits.txt") || { echo "AMORCE V3 : ordre refusé : rien ne part"; exit 2; }
PHASE_O=$(printf '%s' "$L" | sed -n 's/^PHASE=\([a-z]*\) .*/\1/p'); NUM=$(printf '%s' "$L" | sed -n 's/.* NUMERO=\([0-9]*\) .*/\1/p')
DEJA=$(printf '%s' "$L" | sed -n 's/.* DEJA_USD=\([0-9.]*\) .*/\1/p'); CM=$(printf '%s' "$L" | sed -n 's/.* COPIE_MINUTES=\([0-9]*\) .*/\1/p')
ORDRE=$(printf '%s' "$L" | sed -n 's/.* ORDRE=\(ordre-[0-9]*\.json\)$/\1/p')
[ -n "$PHASE_O" ] && [ -n "$NUM" ] && [ -n "$DEJA" ] && [ -n "$ORDRE" ] || { echo "AMORCE V3 : ordre mal lu : refus"; exit 2; }
MINUTES=$(duree "$DEJA") || { echo "AMORCE V3 : prix illisibles : aucun calcul"; exit 2; }
python3 -I -B "$R/amorce-depot/$P3/redemarrage.py" fait "$R/sparks-v3-ordres-faits.txt" "$NUM"
echo "AMORCE V3 : ordre $NUM ($PHASE_O), dépense imputée $DEJA USD, durée plafonnée à $MINUTES minutes"
case "$PHASE_O" in
    fin) detruire "ordre $NUM : fin" ;;
    copie)
        [ "$MINUTES" -ge "$((CM + 5))" ] || { echo "AMORCE V3 : plafond trop bas pour la copie ($MINUTES min) : rien ne part"; exit 2; }
        python3 -I -B "$R/amorce-depot/$P3/redemarrage.py" lot "$O/ordres/$ORDRE" "$R/sparks/sortie" "$R/sparks/lots" \
            || { echo "AMORCE V3 : lot impossible"; exit 2; }
        echo "AMORCE V3 : COPIE prête ($R/sparks/lots/lot-$(printf %03d "$NUM")) ; conteneur en vie $CM minutes"
        sleep "$((CM * 60))"; echo "AMORCE V3 $(date -u +%FT%TZ) : fin de la fenêtre de copie (le conteneur sort)"; exit 0 ;;
    causal)
        [ "$MINUTES" -ge 60 ] || { echo "AMORCE V3 : plafond trop bas pour la phase causale ($MINUTES min) : rien ne part"; exit 2; }
        T="$R/sparks-causal-$(printf %03d "$NUM")"
        timeout --signal=TERM --kill-after=5m "${MINUTES}m" env COMMIT="$COMMIT" COMMIT_CODE="$COMMIT_CODE" TRAVAIL="$T" \
            GO_ID="$GO_ID" PHASE=causal CLE="$O/ordres/causal/cle-ouverte-v1.json" REPONSES="$O/ordres/causal/reponses" \
            MODELES="$R/sparks/sortie/modeles" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v3.sh"
        code=$?; echo "AMORCE V3 $(date -u +%FT%TZ) : fin de la phase causale, code $code"
        if [ "$code" = 0 ] && [ -e "$T/POUSSEE-VERIFIEE" ]; then detruire "fin du contrôle causal, poussée vérifiée"; fi
        echo "AMORCE V3 : phase causale sans poussée vérifiée : pas de destruction (le conteneur sort ; nœud de Lazar)"; exit "$code" ;;
esac
