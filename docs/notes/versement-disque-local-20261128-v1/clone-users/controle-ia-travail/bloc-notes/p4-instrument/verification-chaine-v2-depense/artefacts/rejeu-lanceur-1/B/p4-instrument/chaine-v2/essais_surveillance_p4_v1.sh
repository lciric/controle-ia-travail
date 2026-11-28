#!/usr/bin/env bash
# Banc de la surveillance de P4-instrument et du contrôle à cinq minutes (R5), v1, chaîne v2 : surveiller_p4_v1.sh et
# controle_cinq_minutes_p4_v1.sh joués contre de faux outils de location (aucun service appelé, aucune instance réelle),
# avec le script d'arrêt réel (arreter_p4_v1.sh), qu'ils appellent eux-mêmes. Décliné de
# docs/procedures/P3-premier-test-v2/essais_surveillance_p3_v1.sh sous un nom neuf (R12). Horloge factice : un faux
# `sleep` (qui écrit la durée demandée et avance un décalage) et un faux `date -u +%s` (heure réelle plus le décalage),
# en tête du PATH ; les sommeils demandés sont relus.
# Surveillance : fin normale ; instance perdue après la ligne « etape=M5 conforme=True » ; échec d'amorce (ligne fixe
# affichée, ligne libre affichée par sa longueur et son empreinte) ; redémarrage ; plafond ; un tour juste avant le
# plafond ; outil introuvable ; dossier existant ; jeton masqué ; état hors ligne passager ou alterné ; état illisible
# (relevé par sa longueur et son empreinte, jamais terminal), dont un état illisible qui porte un jeton à cheval sur la
# borne de 120 caractères (RC-donnees-04) ; jetons absents ou trop courts ; usage faux. Chaîne v2 : chaque sortie appelle
# l'arrêt par l'identifiant (une seule demande d'arrêt au faux outil, instance relue arrêtée ; RC-depense-01) ; arrêt en
# échec (code 3) ; script d'arrêt absent ; intervalle hors de 10 à 300 s ; sommeil borné par le plafond (intervalle de
# 300 s à 10 s du plafond) ; étiquette relue entière au départ (autre, « p4-v1 x », état illisible) ; identifiant et
# création lus dans lancement.txt (identifiant autre, ligne de création ou de succès absente ; RC-depense-06).
# Contrôle à cinq minutes : cas sain (aucun arrêt demandé) ; trop tôt ; échec d'amorce ; commit autre ; tests attendus
# autres ; carte autre ; prix au-dessus de l'offre ou du plafond ; téléchargement ou stockage au-dessus de la borne, ou
# stockage absent (RC-fidelite-04) ; machine autre ; étiquette autre (arrêt refusé par le script d'arrêt : code 3) ;
# instance arrêtée ; branche non poussée ; redémarrage ; état illisible (arrêt refusé : code 3) ; état illisible porteur
# d'un jeton ; journal illisible ; jetons absents ; dossier existant ; traces incomplètes ; identifiant autre que celui
# de lancement.txt ; jeton masqué ; retard écrit ; arrêt en échec (code 3) ; usage faux. Sur tout KO, une seule demande
# d'arrêt au faux outil et le code 1 si l'arrêt est confirmé.
# Usage : essais_surveillance_p4_v1.sh RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
E=$(realpath -m "${1:?racine neuve}")
HN=${HN:-/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2}
SURV=$HN/surveiller_p4_v1.sh
CINQ=$HN/controle_cinq_minutes_p4_v1.sh
ARRET=$HN/arreter_p4_v1.sh
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/bin" "$E/bin-cinq" "$E/bin-temps" || exit 2
echo "script éprouvé : surveiller_p4_v1.sh $(sha256sum "$SURV" | cut -d' ' -f1)"
echo "script éprouvé : controle_cinq_minutes_p4_v1.sh $(sha256sum "$CINQ" | cut -d' ' -f1)"
echo "script éprouvé : arreter_p4_v1.sh $(sha256sum "$ARRET" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
JETONS=(HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gi-0000000 GH_TOKEN=factice-gh-0000000)
ID=99999999
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc de la surveillance : scénario dans $SCENARIO (tour n = appels du journal + 1 :
# etat-n.txt, etat-illisible-n, logs-n.txt ou logs-n.err) ; étiquette : fichier etiquette (défaut p4-v1) ; arrêt :
# « stop instance » journalisé dans outil.txt, refusé si arret-echec existe ; après l'arrêt, état exited/stopped
S=${SCENARIO:?}
case "$1 $2" in
  "show instance")
    n=$(( $(cat "$S/journal-appels" 2>/dev/null || echo 0) + 1 ))
    lab=$(cat "$S/etiquette" 2>/dev/null || echo p4-v1)
    if [ -e "$S/arrete" ]; then
        printf '{"actual_status": "exited", "cur_state": "stopped", "intended_status": "stopped", "status_msg": "essai", "label": "%s"}\n' "$lab"; exit 0
    fi
    [ -e "$S/etat-illisible-$n" ] && { cat "$S/etat-illisible-$n"; exit 0; }
    e=$(cat "$S/etat-$n.txt" 2>/dev/null || cat "$S/etat-defaut.txt" 2>/dev/null || echo running)
    printf '{"actual_status": "%s", "cur_state": "%s", "intended_status": "running", "status_msg": "essai", "label": "%s", "extra_env": [["GH_TOKEN", "factice-gh-0000000"]]}\n' "$e" "$( [ "$e" = running ] && echo running || echo stopped)" "$lab" ;;
  "stop instance")
    echo "stop instance $3" >> "$S/outil.txt"
    [ -e "$S/arret-echec" ] && { echo "erreur factice" >&2; exit 1; }
    touch "$S/arrete"; echo '{"success": true}' ;;
  "logs "*)
    n=$(( $(cat "$S/journal-appels" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$S/journal-appels"
    [ -e "$S/logs-$n.err" ] && { echo "erreur factice : instance injoignable" >&2; exit 1; }
    cat "$S/logs-$n.txt" 2>/dev/null || cat "$S/logs-defaut.txt" ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin/vastai"
cat > "$E/bin-cinq/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc du contrôle à cinq minutes : état (etat.json), journal (logs.txt, ou logs.err) ; arrêt
# journalisé dans outil.txt (refusé si arret-echec existe) ; après l'arrêt, l'état relu est arrêté, étiquette gardée
S=${SCENARIO:?}
case "$1 $2" in
  "show instance")
    if [ -e "$S/arrete" ]; then
        python3 -c 'import json, sys; d = json.load(open(sys.argv[1])); d.update(actual_status="exited", cur_state="stopped"); print(json.dumps(d))' "$S/etat.json"
    else cat "$S/etat.json"; fi ;;
  "stop instance") echo "stop instance $3" >> "$S/outil.txt"; [ -e "$S/arret-echec" ] && { echo "erreur factice" >&2; exit 1; }; touch "$S/arrete"; echo '{"success": true}' ;;
  "logs "*) [ -e "$S/logs.err" ] && { echo "erreur factice : instance injoignable" >&2; exit 1; }; cat "$S/logs.txt" ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin-cinq/vastai"
# horloge factice : sleep écrit la durée demandée et avance le décalage ; date -u +%s rend l'heure réelle plus le décalage
cat > "$E/bin-temps/sleep" <<'EOF'
#!/usr/bin/env bash
S=${SCENARIO:?}
echo "$1" >> "$S/sommeils"
d=$(cat "$S/decalage" 2>/dev/null || echo 0); echo $((d + ${1%%.*})) > "$S/decalage"
EOF
cat > "$E/bin-temps/date" <<'EOF'
#!/usr/bin/env bash
if [ "$*" = "-u +%s" ]; then echo $(( $(/usr/bin/date -u +%s) + $(cat "${SCENARIO:?}/decalage" 2>/dev/null || echo 0) )); exit 0; fi
exec /usr/bin/date "$@"
EOF
chmod +x "$E/bin-temps/sleep" "$E/bin-temps/date"
NON_CONFORMES=0
MAINTENANT=$(date -u +%s)
lancement() {   # $1 dossier, $2 création, $3 identifiant de la ligne de succès (vide : ligne absente), $4 « sans-creation »
    mkdir -p "$1"
    { [ "${4:-}" = sans-creation ] || echo "creation $2"; [ -n "$3" ] && echo "succès : True ; identifiant $3 ; message : essai"; } > "$1/lancement.txt"
}
cas() {   # $1 nom, $2 code attendu, $3 motif attendu sur la dernière ligne, $4 création (défaut : maintenant), $5 PATH,
          # $6 jetons (défaut : oui), $7 intervalle (défaut : 10), $8 motif attendu dans la sortie (facultatif)
    local n=$1 attendu=$2 motif=$3 creation=${4:-$MAINTENANT} chemin=${5:-$E/bin-temps:$E/bin:/usr/bin:/bin} jetons=${6:-oui}
    local inter=${7:-10} m2=${8:-} sc="$E/scenario-${1%%-*}" d="$E/sortie-$1" c v env_j=()
    [ "$jetons" = oui ] && env_j=("${JETONS[@]}")
    [ -f "$sc/traces/lancement.txt" ] || lancement "$sc/traces" "$creation" "$ID"
    env -i PATH="$chemin" HOME="$E" LANG=C.UTF-8 SCENARIO="$sc" INTERVALLE="$inter" "${env_j[@]}" \
        bash "$SURV" "$ID" "$sc/traces" "$d" > "$E/console-$n.txt" 2>&1; c=$?
    v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONF""ORME (code $c, attendu $attendu)"
    tail -1 "$E/console-$n.txt" | grep -qF -- "$motif" || v="NON CONF""ORME (motif « $motif » absent de la dernière ligne)"
    [ -n "$m2" ] && ! grep -qF -- "$m2" "$E/console-$n.txt" && v="NON CONF""ORME (motif « $m2 » absent de la sortie)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; demandes d'arrêt au faux outil : $(grep -c '^stop instance' "$sc/outil.txt" 2>/dev/null || echo 0) ; $v"
    tail -2 "$E/console-$n.txt" | couper 200 | sed 's/^/    | /'
}
arret_unique() {   # $1 nom du cas (scénario) : une seule demande d'arrêt, instance relue arrêtée
    local sc="$E/scenario-${1%%-*}"
    [ "$(grep -c "^stop instance $ID$" "$sc/outil.txt" 2>/dev/null)" = 1 ] && grep -q "^ARRÊT CONFIRMÉ : INSTANCE $ID" "$E/sortie-$1/arret/arret.txt" 2>/dev/null \
        && [ -s "$E/sortie-$1/arret/ligne-arrets.md" ] && echo "    $1 : une seule demande d'arrêt, instance relue arrêtée, ligne prête pour registres/arrets.md : CONFORME" \
        || { echo "    $1 : arrêt par l'identifiant non établi : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
}
aucun_arret() {   # $1 nom du cas : aucune demande d'arrêt
    local sc="$E/scenario-${1%%-*}"
    [ ! -s "$sc/outil.txt" ] && echo "    $1 : aucune demande d'arrêt : CONFORME" || { echo "    $1 : demande d'arrêt inattendue : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
}
scenario() { mkdir -p "$E/scenario-$1"; }
A1="AMORCE 2026-10-13T08:00:00Z : commit 0123456789abcdef0123456789abcdef01234567"
P1="PROGRES 2026-10-13T09:00:00Z etape=format verifie=True sondes=424"
P2="PROGRES 2026-10-13T09:40:00Z etape=M5 conforme=True"
FIN0="AMORCE 2026-10-13T12:00:00Z : fin, code 0"
# M00 : fin normale ; arrêt par l'identifiant
scenario M00; printf '%s\n%s\n' "$A1" "$P1" > "$E/scenario-M00/logs-1.txt"
printf '%s\n%s\n%s\n%s\n' "$A1" "$P1" "$P2" "$FIN0" > "$E/scenario-M00/logs-2.txt"
cas M00-fin 0 "SURVEILLANCE : FIN ; INSTANCE $ID ARRÊTÉE PAR SON IDENTIFIANT" "" "" "" "" "FIN : $FIN0"
arret_unique M00-fin
[ "$(wc -l < "$E/sortie-M00-fin/progres.txt")" = 4 ] && echo "    relevé cumulatif : 4 lignes, sans doublon d'un tour à l'autre : CONFORME" \
    || { echo "    relevé cumulatif : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M01 : instance perdue après la ligne de M5 : la ligne reste au relevé cumulatif ; état terminal, arrêt demandé
scenario M01; printf '%s\n%s\n%s\n' "$A1" "$P1" "$P2" > "$E/scenario-M01/logs-1.txt"
touch "$E/scenario-M01/logs-2.err" "$E/scenario-M01/logs-3.err"; echo offline > "$E/scenario-M01/etat-2.txt"; echo offline > "$E/scenario-M01/etat-3.txt"
cas M01-perdue-apres-m5 0 "SURVEILLANCE : ÉTAT TERMINAL ; INSTANCE $ID ARRÊTÉE" "" "" "" "" "ÉTAT TERMINAL : actual_status=offline"
arret_unique M01-perdue-apres-m5
grep -qxF "$P2" "$E/sortie-M01-perdue-apres-m5/progres.txt" && grep -qxF "$P2" "$E/sortie-M01-perdue-apres-m5/journal-dernier.txt" \
    && echo "    ligne de M5 gardée au relevé cumulatif et au dernier journal lisible : CONFORME" \
    || { echo "    ligne de M5 perdue : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M02 : échec d'amorce, ligne fixe (affichée) ; M02b : ligne libre (affichée par sa longueur et son empreinte)
scenario M02; printf '%s\nAMORCE : clonage impossible (jeton GitHub ?)\n' "$A1" > "$E/scenario-M02/logs-1.txt"
cas M02-echec-d-amorce 0 "SURVEILLANCE : ÉCHEC D'AMORCE ; INSTANCE $ID ARRÊTÉE" "" "" "" "" "ÉCHEC D'AMORCE : AMORCE : clonage impossible (jeton GitHub ?)"
arret_unique M02-echec-d-amorce
scenario M02b; printf '%s\nAMORCE : sortie libre (essai) ACTION: ADD TITLE: Synthetic probe zanzibar alpha PROPOSAL: Train a calibrated quokka probe\n' "$A1" > "$E/scenario-M02b/logs-1.txt"
cas M02b-echec-d-amorce-ligne-libre 0 "SURVEILLANCE : ÉCHEC D'AMORCE ; INSTANCE $ID ARRÊTÉE" "" "" "" "" "ÉCHEC D'AMORCE : (ligne de "
grep -qF "zanzibar" "$E/console-M02b-echec-d-amorce-ligne-libre.txt" && { echo "    M02b : ligne libre affichée : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    M02b : ligne libre non affichée (longueur et empreinte) : CONFORME"
# M03 : redémarrage de l'amorce (deux lignes « AMORCE <date> : commit », vues à deux tours)
scenario M03; printf '%s\n' "$A1" > "$E/scenario-M03/logs-1.txt"
printf '%s\n' "AMORCE 2026-10-13T08:05:00Z : commit 0123456789abcdef0123456789abcdef01234567" > "$E/scenario-M03/logs-2.txt"
cas M03-redemarrage 0 "SURVEILLANCE : REDÉMARRAGE ; INSTANCE $ID ARRÊTÉE" "" "" "" "" "REDÉMARRAGE : l'amorce a été relancée"
arret_unique M03-redemarrage
# M04 : plafond (création il y a 9 600 s) ; arrêt par l'identifiant
scenario M04; printf '%s\n%s\n' "$A1" "$P1" > "$E/scenario-M04/logs-defaut.txt"
cas M04-plafond 0 "SURVEILLANCE : PLAFOND ; INSTANCE $ID ARRÊTÉE" "$((MAINTENANT - 9600))" "" "" "" "PLAFOND : création + 9600 s"
arret_unique M04-plafond
# M04b : juste avant le plafond, un tour (sommeil borné à 10 s) puis la fin : pas de plafond
scenario M04b; printf '%s\n' "$A1" > "$E/scenario-M04b/logs-1.txt"; printf '%s\nAMORCE 2026-10-13T12:00:00Z : fin, code 1\n' "$A1" > "$E/scenario-M04b/logs-2.txt"
cas M04b-avant-le-plafond 0 "SURVEILLANCE : FIN ; INSTANCE $ID ARRÊTÉE" "$((MAINTENANT - 9500))"
# M04c (RC-depense-06) : intervalle de 300 s à 10 s du plafond : sommeil borné au plafond, puis PLAFOND au tour suivant
scenario M04c; printf '%s\n' "$A1" > "$E/scenario-M04c/logs-defaut.txt"
cas M04c-sommeil-borne-par-le-plafond 0 "SURVEILLANCE : PLAFOND ; INSTANCE $ID ARRÊTÉE" "$((MAINTENANT - 9590))" "" "" 300
python3 - "$E/scenario-M04c/sommeils" <<'PYS' && echo "    M04c : premier sommeil borné au plafond (10 s au plus, intervalle 300 s) : CONFORME" || { echo "    M04c : sommeil au-delà du plafond : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
import sys
s = [int(x) for x in open(sys.argv[1]).read().split()]
sys.exit(0 if s and s[0] <= 10 and all(x <= 300 for x in s) else 1)
PYS
# M05 : outil introuvable ; M06 : dossier de sortie existant
scenario M05; cas M05-outil-introuvable 2 "outil de location introuvable" "$MAINTENANT" "$E/bin-temps:/usr/bin:/bin"
scenario M06; mkdir -p "$E/sortie-M06-dossier-existant"; cas M06-dossier-existant 2 "existe déjà (R12)"
# M07 : jeton dans le journal : masqué au relevé
scenario M07; printf '%s\nPROGRES 2026-10-13T09:00:00Z etape=bras tache=2604.12086v1\nfuite factice-gh-0000000 factice-hf-0000000\n%s\n' "$A1" "$FIN0" > "$E/scenario-M07/logs-1.txt"
cas M07-jeton-masque 0 "SURVEILLANCE : FIN"
grep -rqE "factice-(gh|hf)-0000000" "$E/sortie-M07-jeton-masque" && { echo "    JETON AFFI""CHÉ : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } \
    || echo "    jetons masqués dans les relevés : CONFORME"
# M08 : un seul état hors ligne, puis retour en marche, puis la fin : pas d'état terminal
scenario M08; printf '%s\n' "$A1" > "$E/scenario-M08/logs-defaut.txt"; echo offline > "$E/scenario-M08/etat-2.txt"
printf '%s\n%s\n' "$A1" "$FIN0" > "$E/scenario-M08/logs-3.txt"
cas M08-hors-ligne-passager 0 "SURVEILLANCE : FIN" "" "" "" "" "FIN : $FIN0"
# M08b : hors ligne et en marche alternés, puis la fin : le compte repart à zéro
scenario M08b; printf '%s\n' "$A1" > "$E/scenario-M08b/logs-defaut.txt"
echo offline > "$E/scenario-M08b/etat-2.txt"; echo offline > "$E/scenario-M08b/etat-4.txt"
printf '%s\n%s\n' "$A1" "$FIN0" > "$E/scenario-M08b/logs-5.txt"
cas M08b-hors-ligne-alterne 0 "SURVEILLANCE : FIN" "" "" "" "" "FIN : $FIN0"
# M10 : réponse non JSON de l'état (deux tours) : relevée par sa longueur et son empreinte, jamais terminale ; puis la fin
scenario M10; printf '%s\n' "$A1" > "$E/scenario-M10/logs-defaut.txt"; echo "réponse non JSON (essai)" > "$E/scenario-M10/etat-illisible-2"; echo "réponse non JSON (essai)" > "$E/scenario-M10/etat-illisible-3"
printf '%s\n%s\n' "$A1" "$FIN0" > "$E/scenario-M10/logs-3.txt"
cas M10-etat-illisible 0 "SURVEILLANCE : FIN" "" "" "" "" "FIN : $FIN0"
[ "$(grep -c 'illisible ([0-9]* caractères, empreinte [0-9a-f]*)' "$E/sortie-M10-etat-illisible/etats.txt" 2>/dev/null)" = 2 ] \
    && echo "    deux états illisibles relevés par leur longueur et leur empreinte, sans état terminal : CONFORME" \
    || { echo "    états illisibles : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M10b (RC-donnees-04) : état illisible qui porte un jeton à cheval sur la borne de 120 caractères : rien en clair
scenario M10b; printf '%s\n' "$A1" > "$E/scenario-M10b/logs-defaut.txt"
printf 'avertissement (essai) %s {"extra_env": [["GH_TOKEN", "factice-gh-0000000"]]}\n' "$(printf 'x%.0s' {1..74})" > "$E/scenario-M10b/etat-illisible-2"
printf '%s\n%s\n' "$A1" "$FIN0" > "$E/scenario-M10b/logs-2.txt"
cas M10b-etat-illisible-porteur-d-un-jeton 0 "SURVEILLANCE : FIN"
grep -rqE "factice-gh|factice-g$" "$E/sortie-M10b-etat-illisible-porteur-d-un-jeton" "$E/console-M10b-etat-illisible-porteur-d-un-jeton.txt" \
    && { echo "    M10b : jeton ou morceau de jeton relevé : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    M10b : aucun morceau de jeton relevé : CONFORME"
# M11 : jetons absents ; M11b : jeton trop court : code 2, aucun dossier écrit
scenario M11; cas M11-jetons-absents 2 "masquage impossible" "$MAINTENANT" "" non
[ ! -e "$E/sortie-M11-jetons-absents" ] && echo "    aucun relevé écrit sans jetons : CONFORME" || { echo "    relevé écrit sans jetons : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
scenario M11b; lancement "$E/scenario-M11b/traces" "$MAINTENANT" "$ID"
env -i PATH="$E/bin-temps:$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/scenario-M11b" INTERVALLE=10 HF_TOKEN=court CONTROLE_IA_GITHUB_TOKEN=factice-gi-0000000 \
    bash "$SURV" "$ID" "$E/scenario-M11b/traces" "$E/sortie-M11b" > "$E/console-M11b.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-M11b.txt" | grep -qF "masquage impossible" && [ ! -e "$E/sortie-M11b" ] && echo "M11b-jeton-trop-court : code 2 ; CONFORME" \
    || { echo "M11b-jeton-trop-court : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# M09 : usage faux (identifiant non numérique)
scenario M09
env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" "${JETONS[@]}" bash "$SURV" abc "$E/scenario-M09" "$E/sortie-M09" > "$E/console-M09.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-M09.txt" | grep -qF "usage" && [ ! -e "$E/sortie-M09" ] && echo "M09-usage-faux : code 2 ; CONFORME" \
    || { echo "M09-usage-faux : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# ---- chaîne v2 : intervalle, étiquette, traces du lancement, arrêt (RC-depense-06, RC-depense-01)
for x in 9000 abc 5 301; do scenario "S10$x"; cas "S10$x-intervalle-$x" 2 "entre 10 et 300 s attendu" "" "" "" "$x"; aucun_arret "S10$x-intervalle-$x"; done
scenario S14; echo rr-autre-projet > "$E/scenario-S14/etiquette"; cas S14-etiquette-autre 2 "≠ « p4-v1 » (comparée entière)"; aucun_arret S14-etiquette-autre
scenario S15; echo "p4-v1 x" > "$E/scenario-S15/etiquette"; cas S15-etiquette-p4-v1-x 2 "≠ « p4-v1 » (comparée entière)"; aucun_arret S15-etiquette-p4-v1-x
scenario S16; echo "pas du JSON" > "$E/scenario-S16/etat-illisible-1"; cas S16-etat-illisible-au-depart 2 "(état illisible)"; aucun_arret S16-etat-illisible-au-depart
scenario S17; lancement "$E/scenario-S17/traces" "$MAINTENANT" 12345678; cas S17-identifiant-autre-que-celui-du-lancement 2 "identifiant autre que $ID"
scenario S18; lancement "$E/scenario-S18/traces" "$MAINTENANT" ""; cas S18-ligne-de-succes-absente 2 "surveillance refusée"
scenario S19; lancement "$E/scenario-S19/traces" "$MAINTENANT" "$ID" sans-creation; cas S19-creation-absente 2 "création ou identifiant illisibles"
scenario S20; printf '%s\n%s\n' "$A1" "$FIN0" > "$E/scenario-S20/logs-1.txt"; touch "$E/scenario-S20/arret-echec"
cas S20-arret-en-echec-a-la-fin 3 "SURVEILLANCE : FIN ; ARRÊT NON CONFIRMÉ (arreter_p4_v1.sh, code 1)"
scenario S21; mkdir -p "$E/sans-arret"; cp "$SURV" "$E/sans-arret/surveiller_p4_v1.sh"; lancement "$E/scenario-S21/traces" "$MAINTENANT" "$ID"
env -i PATH="$E/bin-temps:$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/scenario-S21" INTERVALLE=10 "${JETONS[@]}" \
    bash "$E/sans-arret/surveiller_p4_v1.sh" "$ID" "$E/scenario-S21/traces" "$E/sortie-S21" > "$E/console-S21.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-S21.txt" | grep -qF "script d'arrêt absent" && echo "S21-script-d-arret-absent : code 2 ; CONFORME" \
    || { echo "S21-script-d-arret-absent : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# ---- contrôle à cinq minutes (CH-23 ; chaîne v2 : téléchargement et stockage relus, arrêt par l'identifiant sur KO)
SC=0123456789abcdef0123456789abcdef01234567
traces() {   # $1 dossier, $2 création ; lancement.txt, prereg-S.md et offre.json du lanceur, factices
    mkdir -p "$1"
    printf 'offre choisie : 4242 (1.0933333333333333 USD/h), la moins chère des offres conformes\ncommit %s\noffre 4242\nprereg prereg/P4-instrument-v1.md\nbranche calcul/p4-reel-v1\netiquette p4-v1\ngo GO-2026-10-20-07\ncreation %s\nsuccès : True ; identifiant %s ; message : essai\n' "$SC" "$2" "$ID" > "$1/lancement.txt"
    printf '# texte factice\n- Tests attendus : `1102`\n' > "$1/prereg-S.md"
    printf '{"id": 4242, "machine_id": 30574, "host_id": 125728, "dph_total": 1.0933333333333333}\n' > "$1/offre.json"
}
journal_sain() {   # $1 fichier
    printf 'AMORCE 2026-10-19T10:00:14Z : commit %s\n2026-10-19T10:00:32Z début : ETUDE=p4 MODE=reel COMMIT=%s BRANCHE=calcul/p4-reel-v1\n2026-10-19T10:00:50Z préenregistrement lu : 1102 tests attendus ; configuration prereg/P4-instrument-config-v1.json\n2026-10-19T10:00:51Z branche calcul/p4-reel-v1 poussée avant l%sinstallation (droit d%sécriture éprouvé)\nname, driver_version, memory.total [MiB]\nNVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB\n' "$SC" "$SC" "'" "'" > "$1"
}
etat_sain='{"actual_status": "running", "cur_state": "running", "dph_total": 1.0933333333333333, "machine_id": 30574, "host_id": 125728, "gpu_name": "A100 SXM4", "inet_down_cost": 0.0390625, "storage_total_cost": 0.0153, "label": "p4-v1", "extra_env": [["GH_TOKEN", "factice-gh-0000000"]]}'
cinq() {   # $1 nom, $2 code attendu, $3 motif de la dernière ligne, $4 expression sed sur le journal (vide : sain), $5 expression sed sur l'état, $6 âge de la création (s), $7 jetons (oui/non), $8 nombre de KO attendu
    local n=$1 attendu=$2 motif=$3 sj=${4:-} se=${5:-} age=${6:-240} jetons=${7:-oui} nko=${8:-} c v env_j=()
    local s="$E/cinq-$n" t="$E/cinq-$n/traces"
    mkdir -p "$s"; [ -f "$t/lancement.txt" ] || traces "$t" "$((MAINTENANT - age))"
    journal_sain "$s/logs.txt"; [ -n "$sj" ] && sed -i "$sj" "$s/logs.txt"
    [ -f "$s/etat.json" ] || { printf '%s\n' "$etat_sain" > "$s/etat.json"; [ -n "$se" ] && sed -i "$se" "$s/etat.json"; }
    [ "$jetons" = oui ] && env_j=("${JETONS[@]}")
    env -i PATH="$E/bin-temps:$E/bin-cinq:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$s" "${env_j[@]}" \
        bash "$CINQ" "$ID" "$t" "$s/sortie" > "$E/console-cinq-$n.txt" 2>&1; c=$?
    v="CONFORME"
    [ "$c" = "$attendu" ] || v="NON CONF""ORME (code $c, attendu $attendu)"
    tail -1 "$E/console-cinq-$n.txt" | grep -qF -- "$motif" || v="NON CONF""ORME (motif « $motif » absent de la dernière ligne)"
    [ -n "$nko" ] && [ "$(grep -c '^KO' "$E/console-cinq-$n.txt")" != "$nko" ] && v="NON CONF""ORME ($(grep -c '^KO' "$E/console-cinq-$n.txt") KO, $nko attendu(s))"
    case "$attendu" in
        0|2) [ -s "$s/outil.txt" ] && v="NON CONF""ORME (arrêt demandé sans KO)" ;;
        1) [ "$(grep -c "^stop instance $ID$" "$s/outil.txt" 2>/dev/null)" = 1 ] || v="NON CONF""ORME (une demande d'arrêt attendue)" ;;
    esac
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; $(grep -c '^KO' "$E/console-cinq-$n.txt") KO ; demandes d'arrêt : $(grep -c '^stop instance' "$s/outil.txt" 2>/dev/null || echo 0) ; $v"
    grep '^KO' "$E/console-cinq-$n.txt" | couper 160 | sed 's/^/    /'
    tail -1 "$E/console-cinq-$n.txt" | couper 160 | sed 's/^/    | /'
}
cinq C00-sain 0 "CONTRÔLE À CINQ MINUTES : CONFORME"
[ -s "$E/cinq-C00-sain/sortie/journal-5min.txt" ] && [ -s "$E/cinq-C00-sain/sortie/controle-5min.txt" ] \
    && echo "    journal à cinq minutes et relevé du contrôle gardés : CONFORME" || { echo "    journal ou relevé absent : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cinq C01-trop-tot 2 "trop tôt" "" "" 60
[ ! -e "$E/cinq-C01-trop-tot/sortie" ] && echo "    rien d'écrit trop tôt : CONFORME" || { echo "    sortie écrite trop tôt : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
ARRETEE="INSTANCE $ID ARRÊTÉE PAR SON IDENTIFIANT (arreter_p4_v1.sh, code 0)"
cinq C02-echec-d-amorce 1 "1 KO ; $ARRETEE" '1a AMORCE : clonage impossible (jeton GitHub ?)' "" 240 oui 1
grep -qF "échec de l'amorce (AMORCE : clonage impossible (jeton GitHub ?))" "$E/console-cinq-C02-echec-d-amorce.txt" && echo "    C02 : ligne fixe de l'amorce affichée : CONFORME" || { echo "    C02 : ligne fixe absente : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cinq C02b-echec-d-amorce-ligne-libre 1 "1 KO ; $ARRETEE" '1a AMORCE : sortie libre (essai) PROPOSAL: Train a calibrated quokka probe on layer seven' "" 240 oui 1
grep -qF "quokka" "$E/console-cinq-C02b-echec-d-amorce-ligne-libre.txt" "$E/cinq-C02b-echec-d-amorce-ligne-libre/sortie/controle-5min.txt" \
    && { echo "    C02b : ligne libre affichée : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    C02b : ligne libre affichée par sa longueur et son empreinte : CONFORME"
cinq C03-commit-autre 1 "2 KO ; $ARRETEE" "s/$SC/fedcba9876543210fedcba9876543210fedcba98/g"
cinq C04-tests-attendus-autres 1 "1 KO" 's/1102 tests attendus/1101 tests attendus/'
cinq C05-carte-autre 1 "1 KO" 's/NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB/NVIDIA A100-PCIE-40GB, 580.159.03, 40960 MiB/'
cinq C06-prix-au-dessus-du-prix-choisi 1 "1 KO" "" 's/"dph_total": 1.0933333333333333/"dph_total": 1.2/'
cinq C06b-prix-au-dessus-du-plafond 1 "2 KO" "" 's/"dph_total": 1.0933333333333333/"dph_total": 1.35/'
cinq C07-machine-autre 1 "1 KO" "" 's/"machine_id": 30574/"machine_id": 1/'
cinq C08-etiquette-autre 3 "1 KO ; ARRÊT NON CONFIRMÉ (arreter_p4_v1.sh, code 2)" "" 's/"label": "p4-v1"/"label": "p3-v1"/'
[ ! -s "$E/cinq-C08-etiquette-autre/outil.txt" ] && echo "    C08 : étiquette autre : aucun arrêt demandé (le script d'arrêt refuse) : CONFORME" || { echo "    C08 : arrêt demandé : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
cinq C09-instance-arretee 1 "1 KO ; $ARRETEE" "" 's/"actual_status": "running"/"actual_status": "exited"/'
cinq C10-branche-non-poussee 1 "1 KO" '/poussée avant l.installation/d'
cinq C11-redemarrage 1 "1 KO" "1a AMORCE 2026-10-19T10:03:00Z : commit $SC"
cinq C12-etat-illisible 3 "1 KO ; ARRÊT NON CONFIRMÉ (arreter_p4_v1.sh, code 2)" "" 's/.*/pas du JSON/'
mkdir -p "$E/cinq-C13-journal-illisible"; touch "$E/cinq-C13-journal-illisible/logs.err"
cinq C13-journal-illisible 1 "1 KO ; $ARRETEE"
cinq C14-jetons-absents 2 "masquage impossible" "" "" 240 non
mkdir -p "$E/cinq-C15-dossier-existant/sortie"
cinq C15-dossier-existant 2 "existe déjà (R12)"
cinq C16-jeton-masque 0 "CONFORME" '$a fuite factice-gh-0000000 et factice-hf-0000000'
grep -rqE "factice-(gh|hf)-0000000" "$E/cinq-C16-jeton-masque/sortie" "$E/console-cinq-C16-jeton-masque.txt" \
    && { echo "    JETON AFFI""CHÉ : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    jetons masqués (journal et état) : CONFORME"
cinq C17-retard-ecrit 0 "CONFORME" "" "" 1000
grep -q "^--  contrôle fait après" "$E/console-cinq-C17-retard-ecrit.txt" && echo "    retard écrit : CONFORME" \
    || { echo "    retard non écrit : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# chaîne v2 (RC-fidelite-04) : téléchargement et stockage relus ; (RC-depense-01) arrêt en échec
cinq C21-telechargement-au-dessus-de-la-borne 1 "1 KO ; $ARRETEE" "" 's/"inet_down_cost": 0.0390625/"inet_down_cost": 0.06/' 240 oui 1
cinq C22-stockage-au-dessus-de-la-borne 1 "1 KO ; $ARRETEE" "" 's/"storage_total_cost": 0.0153/"storage_total_cost": 0.031/' 240 oui 1
cinq C23-stockage-absent 1 "1 KO ; $ARRETEE" "" 's/"storage_total_cost": 0.0153, //' 240 oui 1
cinq C23b-telechargement-et-stockage-au-plafond-juste 0 "CONFORME" "" 's/"inet_down_cost": 0.0390625, "storage_total_cost": 0.0153/"inet_down_cost": 0.05, "storage_total_cost": 0.03/'
mkdir -p "$E/cinq-C25-arret-en-echec"; touch "$E/cinq-C25-arret-en-echec/arret-echec"
cinq C25-arret-en-echec 3 "1 KO ; ARRÊT NON CONFIRMÉ (arreter_p4_v1.sh, code 1)" "" 's/"machine_id": 30574/"machine_id": 1/'
# chaîne v2 (RC-donnees-04) : état illisible qui porte un jeton à cheval sur 120 caractères : longueur et empreinte seulement
mkdir -p "$E/cinq-C26-etat-illisible-porteur-d-un-jeton"
printf 'avertissement (essai) %s {"extra_env": [["GH_TOKEN", "factice-gh-0000000"]]}\n' "$(printf 'x%.0s' {1..74})" > "$E/cinq-C26-etat-illisible-porteur-d-un-jeton/etat.json"
cinq C26-etat-illisible-porteur-d-un-jeton 3 "1 KO ; ARRÊT NON CONFIRMÉ (arreter_p4_v1.sh, code 2)"
grep -rqE "factice-gh|factice-g$" "$E/cinq-C26-etat-illisible-porteur-d-un-jeton/sortie" "$E/console-cinq-C26-etat-illisible-porteur-d-un-jeton.txt" \
    && { echo "    C26 : morceau de jeton affiché : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); } || echo "    C26 : aucun morceau de jeton affiché : CONFORME"
# traces incomplètes (offre.json absente) ; usage faux ; branche de P3 ; identifiant autre que celui du lancement : code 2
mkdir -p "$E/cinq-C18/traces"; traces "$E/cinq-C18/traces" "$((MAINTENANT - 240))"; rm -f "$E/cinq-C18/traces/offre.json"
env -i PATH="$E/bin-cinq:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/cinq-C18" "${JETONS[@]}" bash "$CINQ" "$ID" "$E/cinq-C18/traces" "$E/cinq-C18/sortie" > "$E/console-cinq-C18.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-cinq-C18.txt" | grep -qF "traces du lancement incomplètes" && echo "C18-traces-incompletes : code 2 ; CONFORME" \
    || { echo "C18-traces-incompletes : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
env -i PATH="$E/bin-cinq:/usr/bin:/bin" HOME="$E" "${JETONS[@]}" bash "$CINQ" abc "$E/cinq-C18/traces" "$E/cinq-C19" > "$E/console-cinq-C19.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-cinq-C19.txt" | grep -qF "usage" && [ ! -e "$E/cinq-C19" ] && echo "C19-usage-faux : code 2 ; CONFORME" \
    || { echo "C19-usage-faux : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
mkdir -p "$E/cinq-C20/traces"; traces "$E/cinq-C20/traces" "$((MAINTENANT - 240))"; sed -i 's|^branche calcul/p4-reel-v1$|branche calcul/p3-reel-v1|' "$E/cinq-C20/traces/lancement.txt"
env -i PATH="$E/bin-cinq:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/cinq-C20" "${JETONS[@]}" bash "$CINQ" "$ID" "$E/cinq-C20/traces" "$E/cinq-C20/sortie" > "$E/console-cinq-C20.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-cinq-C20.txt" | grep -qF "traces du lancement illisibles" && [ ! -e "$E/cinq-C20/sortie" ] && echo "C20-branche-de-p3 : code 2 ; CONFORME" \
    || { echo "C20-branche-de-p3 : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
mkdir -p "$E/cinq-C24/traces"; traces "$E/cinq-C24/traces" "$((MAINTENANT - 240))"; sed -i "s/identifiant $ID ;/identifiant 12345678 ;/" "$E/cinq-C24/traces/lancement.txt"
env -i PATH="$E/bin-cinq:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/cinq-C24" "${JETONS[@]}" bash "$CINQ" "$ID" "$E/cinq-C24/traces" "$E/cinq-C24/sortie" > "$E/console-cinq-C24.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$E/console-cinq-C24.txt" | grep -qF "autre que $ID : contrôle refusé" && [ ! -e "$E/cinq-C24/sortie" ] && echo "C24-identifiant-autre-que-celui-du-lancement : code 2 ; CONFORME" \
    || { echo "C24-identifiant-autre-que-celui-du-lancement : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# aucun jeton factice dans les sorties des consoles
FUITES=$(grep -lE "factice-(gh|hf|gi)-0000000" "$E"/console-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { printf '%s\n' $FUITES | sed 's/^/JETON AFFI''CHÉ : /'; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
