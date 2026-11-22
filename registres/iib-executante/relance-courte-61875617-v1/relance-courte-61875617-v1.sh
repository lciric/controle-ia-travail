#!/usr/bin/env bash
# Relance courte de 61875617 (texte de relance, brouillon 2) : un seul start, relevé du journal du loueur et de l'état toutes les
# 5 s, arrêt par l'identifiant dès que l'amorce a poussé, a renoncé ou a refusé, ou dès que la veille est aveugle, ou à une borne.
# Sous-commandes : decider JOURNAL | jouer | secrets FICHIER... . Commandes du loueur employées : start (une fois), logs,
# show instances, stop (deux fois au plus). Jamais destroy, jamais une autre instance.
# Variables : ID (=61875617), D2 (dossier neuf, existant), VAST (outil de la création), LOC (location_v1.py du commit de lancement).
set -uo pipefail
ID_ATTENDU=61875617
INTOUCHABLES="58936096 58936099 58936100 60988826 61932710"
BR='essai/iib-explo-v6'
HEURE_MAX_S="${HEURE_MAX_S_ESSAI:-1795462800}"     # 2026-11-23T19:40:00Z ; la variable d'essai ne sert qu'aux essais à blanc
PAS_S="${PAS_S:-5}"
BORNE_SCHEDULING_S="${BORNE_SCHEDULING_S:-900}"    # attente de la mise en marche (statut autre que running) : arrêt sans coût
BORNE_RUN_S="${BORNE_RUN_S:-60}"                   # statut running vu, aucune ligne DEMARRAGE >= 2 après 60 s : arrêt
BORNE_ISSUE_S="${BORNE_ISSUE_S:-1080}"             # 18 min après la ligne de démarrage sans issue : arrêt
BORNE_TOTALE_S="${BORNE_TOTALE_S:-2100}"           # 35 min après le start : arrêt
ILLISIBLES_MAX=3                                   # trois relevés du journal illisibles de suite : arrêt

decider() {  # $1 = journal masqué ; une ligne : ATTENDRE | DEMARRAGE | ARRETER ; seules les lignes après le dernier démarrage de rang >= 2
    local apres
    apres=$(awk '$1=="AMORCE" && $2=="IIB" && $4=="DEMARRAGE" && ($5+0)>=2 {buf=""; vu=1; next} vu {buf=buf $0 "\n"} END {if (vu) printf "VU\n%s", buf}' "$1")
    [ -n "$apres" ] || { echo "ATTENDRE : démarrage de rang 2 ou plus non vu"; return 0; }
    case "$apres" in
        *"branche $BR poussée (redémarrage d'un run interrompu)"*) echo "ARRETER : poussée faite";;
        *"poussée impossible"*)                        echo "ARRETER : poussée impossible";;
        *"refus annoncé"*|*"destruction demandée"*|*"refus : "*) echo "ARRETER : refus de l'amorce vu sans ligne de poussée";;
        *"second démarrage après"*)                    echo "ARRETER : chemin inattendu (fin normale ou dépense épuisée)";;
        *"début iib v5"*|*"CLONAGE"*|*"PROGRES "*|*"tests : "*|*"run : "*) echo "ARRETER : calcul inattendu après le démarrage";;
        *) echo "DEMARRAGE : vu, issue non encore écrite";;
    esac; }

etat() {  # $1 = rang ; ligne du lecteur d'inventaire (champs filtrés) ; brut réduit par le lecteur, supprimé s'il échoue
    local b="$D2/inv-$1.json" r
    ( umask 077; timeout -k 5 120 "$VAST" show instances --raw > "$b" 2>/dev/null </dev/null ) || { rm -f -- "$b"; return 1; }
    r=$(python3 -I -B "$LOC" inventaire "$b" "$D2/inv-$1-champs-filtres.json" iib "$ID_ATTENDU") || { rm -f -- "$b"; return 1; }
    printf '%s\n' "$r"; }

arreter() {  # $1 = motif ; stop par l'identifiant, relecture ; second stop au plus, à 2 min ; jamais destroy
    local c k e
    echo "$(date -u +%FT%TZ) $1 : stop instance $ID_ATTENDU" | tee -a "$D2/veille.txt"
    ( umask 077; timeout -k 5 120 "$VAST" stop instance "$ID_ATTENDU" --raw > "$D2/stop-1.json" 2>&1 </dev/null ); c=$?
    python3 -I -B "$LOC" masquer-en-place "$D2/stop-1.json" >/dev/null || : > "$D2/stop-1.json"
    echo "$(date -u +%FT%TZ) stop 1 : code $c" >> "$D2/veille.txt"
    for k in $(seq 1 20); do
        [ "$PAS_S" = 0 ] || sleep 15
        e=$(etat "arret-$k") || e="illisible"
        echo "$(date -u +%FT%TZ) relecture $k : $e" >> "$D2/veille.txt"
        case "$e" in *"statut=exited"*|*"statut=stopped"*) echo "ARRET CONFIRME ($1)" | tee -a "$D2/veille.txt"; return 0;; esac
        if [ "$k" = 8 ]; then
            ( umask 077; timeout -k 5 120 "$VAST" stop instance "$ID_ATTENDU" --raw > "$D2/stop-2.json" 2>&1 </dev/null ); c=$?
            python3 -I -B "$LOC" masquer-en-place "$D2/stop-2.json" >/dev/null || : > "$D2/stop-2.json"
            echo "$(date -u +%FT%TZ) stop 2 : code $c" >> "$D2/veille.txt"
        fi
    done
    echo "ARRET NON CONFIRME ($1) : aucune autre commande ; mot de la mère" | tee -a "$D2/veille.txt"; return 1; }

jouer() {
    [ "${ID:-}" = "$ID_ATTENDU" ] || { echo "REFUS : ID=${ID:-} ≠ $ID_ATTENDU"; return 2; }
    case " $INTOUCHABLES " in *" $ID "*) echo "REFUS : identifiant intouchable"; return 2;; esac
    [ -d "${D2:-}" ] && [ -x "${VAST:-}" ] && [ -f "${LOC:-}" ] || { echo "REFUS : D2, VAST ou LOC absent"; return 2; }
    [ ! -e "$D2/start-fait" ] || { echo "REFUS : un start a déjà été joué ($(cat "$D2/start-fait")) : jamais de seconde relance"; return 2; }
    [ "$(date +%s)" -le "$HEURE_MAX_S" ] || { echo "REFUS : après 2026-11-23T19:40:00Z (dépense épuisée lue sur le disque à 20:42:05Z)"; return 2; }
    local e; e=$(etat avant-start) || { echo "REFUS : inventaire illisible"; return 2; }
    case "$e" in *"etat=present etiquette=iib-explo-v5 statut=exited"*|*"etat=present etiquette=iib-explo-v5 statut=stopped"*) ;;
        *) echo "REFUS : état avant le start : $e"; return 2;; esac
    echo "$(date -u +%FT%TZ) start unique de $ID_ATTENDU" > "$D2/start-fait"
    local T0 now n=0 c cl L DEM="" RUN_VU="" ILL=0 es RC=0
    T0=$(date +%s)
    ( umask 077; timeout -k 5 120 "$VAST" start instance "$ID_ATTENDU" --raw > "$D2/start.json" 2>&1 </dev/null ); c=$?
    python3 -I -B "$LOC" masquer-en-place "$D2/start.json" >/dev/null || : > "$D2/start.json"
    echo "$(date -u +%FT%TZ) start : code $c" | tee -a "$D2/veille.txt"
    [ "$c" = 0 ] || { arreter "ARRETER : start en code $c"; return 1; }
    while :; do
        n=$((n + 1))
        ( umask 077; timeout -k 5 60 "$VAST" logs "$ID_ATTENDU" --tail 3000 > "$D2/journal-courant.tmp" 2>/dev/null </dev/null ); cl=$?
        if [ "$cl" = 0 ] && [ -s "$D2/journal-courant.tmp" ] && python3 -I -B "$LOC" masquer-en-place "$D2/journal-courant.tmp" >/dev/null; then
            ILL=0; L=$(decider "$D2/journal-courant.tmp")
        else
            : > "$D2/journal-courant.tmp"; ILL=$((ILL + 1)); L="ILLISIBLE ($ILL de suite, code $cl)"
        fi
        es=$(etat "veille-$n") || es="illisible"
        now=$(date +%s)
        case "$es" in *"statut=running"*) [ -n "$RUN_VU" ] || RUN_VU=$now;; esac
        echo "$(date -u +%FT%TZ) relevé $n : $L ; état : $es" >> "$D2/veille.txt"
        case "$L" in ARRETER*) arreter "$L"; RC=$?; break;; DEMARRAGE*) [ -n "$DEM" ] || DEM=$now;; esac
        if [ "$ILL" -ge "$ILLISIBLES_MAX" ]; then arreter "ARRETER : journal du loueur illisible $ILL fois de suite"; RC=$?; break; fi
        if [ -z "$DEM" ] && [ -n "$RUN_VU" ] && [ $((now - RUN_VU)) -ge "$BORNE_RUN_S" ]; then arreter "ARRETER : en marche depuis $BORNE_RUN_S s sans ligne de démarrage 2"; RC=$?; break; fi
        if [ -z "$DEM" ] && [ -z "$RUN_VU" ] && [ $((now - T0)) -ge "$BORNE_SCHEDULING_S" ]; then arreter "ARRETER : pas en marche après $BORNE_SCHEDULING_S s"; RC=$?; break; fi
        if [ -n "$DEM" ] && [ $((now - DEM)) -ge "$BORNE_ISSUE_S" ]; then arreter "ARRETER : aucune issue $BORNE_ISSUE_S s après le démarrage"; RC=$?; break; fi
        if [ $((now - T0)) -ge "$BORNE_TOTALE_S" ]; then arreter "ARRETER : borne totale de $BORNE_TOTALE_S s"; RC=$?; break; fi
        [ "$PAS_S" = 0 ] || sleep "$PAS_S"
    done
    mv -n "$D2/journal-courant.tmp" "$D2/journal-loueur-fin-masque.txt"
    grep -E "DEMARRAGE|redémarrage d'un run interrompu|poussée|refus|destruction|ERREUR DE CHAÎNE" "$D2/journal-loueur-fin-masque.txt" \
        | grep -vE "PROGRES" | tail -n 40 > "$D2/lignes-d-issue.txt" || true
    return "$RC"; }   # 0 arrêt confirmé ; 1 arrêt non confirmé

secrets() {  # n'imprime qu'un nombre ; valeurs lues par leur nom seulement
    python3 -I -B - "$@" <<'PY'
import os, re, sys
noms = ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY")
vals = [os.environ[k].encode() for k in noms if len(os.environ.get(k, "")) >= 8]
motif = re.compile(rb"ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|hf_[A-Za-z0-9]{30,}|sk-ant-[A-Za-z0-9_-]{20,}")
n = 0
for f in sys.argv[1:]:
    b = open(f, "rb").read()
    n += sum(b.count(v) for v in vals) + len(motif.findall(b))
print(n)
sys.exit(0 if n == 0 else 1)
PY
}

case "${1:-}" in decider) decider "$2";; jouer) jouer;; secrets) shift; secrets "$@";; *) echo "usage : decider JOURNAL | jouer | secrets FICHIER..."; exit 2;; esac
