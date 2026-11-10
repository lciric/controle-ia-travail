#!/usr/bin/env bash
# Banc de la surveillance et du contrôle à cinq minutes de P3-bis (R5), v1 : surveiller_p3bis_v1.sh et
# controle_cinq_minutes_p3bis_v1.sh joués contre un faux outil de location (aucun service appelé ; il journalise chaque
# verbe, refuse toute destruction et tout verbe inattendu). Décliné du banc de la surveillance de P3 sous un nom neuf
# (R12). Surveillance : fin normale (arrêt par identifiant, aucune destruction) ; code 5 et ligne « SECOND PAQUET EN
# ÉCHEC » (instance gardée), poussée des traces jamais coupée ; processus mort ; échec d'amorce ; redémarrage ; état
# terminal ; états passagers et illisibles (jamais terminaux) ; dépense au plafond (durée, dépense antérieure,
# projection au prochain relevé, bornes écrites si illisible) ; run de trente heures sans arrêt (aucun plafond de durée) ;
# alerte à deux heures sans PROGRES, sans arrêt, une fois par fenêtre ; PROGRES nouvelle qui remet l'alerte ; arrêt en
# échec ; garde de l'identifiant (autre instance, instance tolérée) ; journal illisible ; jeton masqué ; jetons absents ;
# outil introuvable ; dossier existant ; usage. Contrôle à cinq minutes : cas sain ; trop tôt ; retard écrit ; échec
# d'amorce ; commit autre ; tests attendus autres ; carte autre ; prix au-dessus de l'offre choisie, au-dessus du
# plafond ; machine autre ; étiquette autre ; instance arrêtée ; branche non poussée ; redémarrage ; état illisible ;
# journal illisible ; arrêt en échec ; identifiant autre ; jetons absents ; dossier existant ; traces incomplètes ; jeton
# masqué ; usage. Chaque KO du contrôle à cinq minutes arrête l'instance par son identifiant (une seule fois).
# Usage : essais_surveillance_p3bis_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
ICI=$(dirname "$(realpath "$0")")
SURV=$ICI/surveiller_p3bis_v1.sh
CINQ=$ICI/controle_cinq_minutes_p3bis_v1.sh
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/bin" || exit 2
for s in surveiller_p3bis_v1.sh controle_cinq_minutes_p3bis_v1.sh verifications_p3bis_v1.py; do
    echo "script éprouvé : $s $(sha256sum "$ICI/$s" | cut -d' ' -f1)"
done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
JETONS=(HF_TOKEN=factice-hf-3333333 CONTROLE_IA_GITHUB_TOKEN=factice-gi-4444444 GH_TOKEN=factice-gh-5555555)
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc de la surveillance de P3-bis : scénario dans $SCENARIO ; n'appelle aucun service
S=${SCENARIO:?}
echo "$*" >> "$S/actions"
case "$1 $2" in
  "show instance")
    if [ -e "$S/arretee" ]; then printf '{"actual_status": "exited", "cur_state": "stopped", "dph_total": 0.05}\n'; exit 0; fi
    [ -e "$S/etat.json" ] && { cat "$S/etat.json"; exit 0; }
    n=$(( $(cat "$S/tour" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$S/tour"
    [ -e "$S/etat-illisible-$n" ] && { echo "réponse non JSON (essai)"; exit 0; }
    e=$(cat "$S/etat-$n.txt" 2>/dev/null || cat "$S/etat-defaut.txt" 2>/dev/null || echo running)
    printf '{"actual_status": "%s", "cur_state": "%s", "intended_status": "running", "status_msg": "essai", "dph_total": %s, "inet_down_billed": %s, "inet_down_cost": 0.026}\n' \
        "$e" "$( [ "$e" = running ] && echo running || echo stopped)" "${FAUX_DPH:-2.0}" "${FAUX_TEL_GO:-20}" ;;
  "logs "*)
    [ -e "$S/logs.txt" ] && { [ -e "$S/logs.err" ] && { echo "erreur factice" >&2; exit 1; }; cat "$S/logs.txt"; exit 0; }
    n=$(cat "$S/tour"); [ -e "$S/logs-$n.err" ] && { echo "erreur factice : instance injoignable" >&2; exit 1; }
    cat "$S/logs-$n.txt" 2>/dev/null || cat "$S/logs-defaut.txt" ;;
  "stop instance")
    [ -e "$S/stop-echec" ] && { echo "erreur factice d'arrêt" >&2; exit 1; }
    touch "$S/arretee"; echo '{"success": true}' ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin/vastai"
NON_CONFORMES=0; NCAS=0
MAINTENANT=$(date -u +%s)
OFFRE_JSON='{"id": 111, "machine_id": 7101, "host_id": 8101, "dph_total": 1.10}'
traces() {   # $1 dossier, $2 création, $3 identifiant écrit, $4 prix choisi
    mkdir -p "$1"
    printf 'commit %s\nbranche calcul/p3bis-reel-v1\netiquette p3bis-v1\ncreation %s\noffre choisie : 111 (%s USD/h), la moins chère des offres conformes\ninstance %s\n' \
        "0123456789abcdef0123456789abcdef01234567" "$2" "${4:-1.1}" "$3" > "$1/lancement.txt"
    printf '# texte factice\n- Tests attendus : `436`\n' > "$1/prereg-S.md"
    printf '%s\n' "$OFFRE_JSON" > "$1/offre.json"
}
verdict() {   # $1 nom, $2 code obtenu, $3 code attendu, $4 motif attendu sur la dernière ligne, $5 console, $6 scénario
    local v=CONFORME
    [ "$2" = "$3" ] || v="NON CONFORME (code $2, attendu $3)"
    [ "$4" = - ] || tail -1 "$5" | grep -qF -- "$4" || v="NON CONFORME (motif « $4 » absent de la dernière ligne)"
    grep -q '^destroy' "$6/actions" 2>/dev/null && v="NON CONFORME (destruction demandée)"
    grep -rqF -e factice-hf-3333333 -e factice-gi-4444444 -e factice-gh-5555555 "$5" "$E/sortie-$1" 2>/dev/null && v="NON CONFORME (JETON AFFICHÉ)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    NCAS=$((NCAS + 1))
    echo "$1 : code $2 ; $v"
    tail -1 "$5" | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
}
apres() {
    local desc=$1; shift
    NCAS=$((NCAS + 1))
    if (eval "$*") > /dev/null 2>&1; then echo "    $desc : CONFORME"; else echo "    $desc : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
surv() {   # $1 nom, $2 code attendu, $3 motif, $4 création, $5 dépense antérieure, $6 identifiant passé (défaut 99999999), $7 identifiant écrit
    local n=$1 attendu=$2 motif=$3 creation=$4 ant=${5:-0} id=${6:-99999999} ecrit=${7:-99999999} c
    local sc="$E/scenario-$n"
    mkdir -p "$sc"; traces "$E/traces-$n" "$creation" "$ecrit"
    env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$sc" INTERVALLE=0 "${JETONS[@]}" ${FAUX_ENV:-} \
        bash "$SURV" "$id" "$E/traces-$n" "$ant" "$E/sortie-$n" > "$E/console-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$attendu" "$motif" "$E/console-$n.txt" "$sc"
}
sc() { mkdir -p "$E/scenario-$1"; }
A1="AMORCE 2026-11-12T08:00:00Z : commit 0123456789abcdef0123456789abcdef01234567"
A2="AMORCE 2026-11-12T08:07:00Z : commit 0123456789abcdef0123456789abcdef01234567"
P1="PROGRES 2026-11-12T09:00:00Z etape=entrainement concept=tromperie aire_validation=1.0"
P2="PROGRES 2026-11-12T09:40:00Z etape=sondes-figees empreinte=0123456789abcdef sondes=430"
FIN0="AMORCE 2026-11-12T12:30:00Z : fin, code 0"
RUNOK="2026-11-12T12:00:00Z run : processus 4242 fini, code 0"
H1H=$((MAINTENANT - 3600))
# --- surveillance ----------------------------------------------------------------------------------------------------
sc M00; printf '%s\n%s\n' "$A1" "$P1" > "$E/scenario-M00/logs-1.txt"; printf '%s\n' "$A1" "$P1" "$P2" "$RUNOK" "$FIN0" > "$E/scenario-M00/logs-2.txt"
surv M00 0 "FIN : $FIN0 ; instance 99999999 arrêtée par son identifiant (R10)" "$H1H"
apres "arrêt par l'identifiant, une seule fois ; aucune destruction ; ligne à consigner ; relevé cumulatif de 4 lignes" \
    "[ \$(grep -c '^stop instance 99999999\$' '$E/scenario-M00/actions') = 1 ] && ! grep -q destroy '$E/scenario-M00/actions' && [ \$(wc -l < '$E/sortie-M00/arrets-a-consigner.txt') = 1 ] && [ \$(wc -l < '$E/sortie-M00/progres.txt') = 4 ] && [ ! -e '$E/sortie-M00/instance-gardee' ]"
sc M01; printf '%s\n' "$A1" "$P1" "$RUNOK" "AMORCE 2026-11-12T12:30:00Z : fin, code 5" > "$E/scenario-M01/logs-defaut.txt"
surv M01 0 "GARDÉE, jamais détruite" "$H1H"
apres "code 5 : instance arrêtée par son identifiant et marquée gardée (instance-gardee)" \
    "grep -q '^stop instance 99999999\$' '$E/scenario-M01/actions' && grep -q 'second paquet en échec' '$E/sortie-M01/instance-gardee'"
sc M02; printf '%s\n' "$A1" "2026-11-12T12:01:00Z SECOND PAQUET EN ÉCHEC (sel absent) : aucun fichier du run poussé en clair" "AMORCE 2026-11-12T12:30:00Z : fin, code 1" > "$E/scenario-M02/logs-defaut.txt"
surv M02 0 "GARDÉE, jamais détruite" "$H1H"
sc M03; L3=("$A1" "$P1" "2026-11-12T12:01:00Z SECOND PAQUET EN ÉCHEC (relecture fausse)")
printf '%s\n' "${L3[@]}" > "$E/scenario-M03/logs-1.txt"; printf '%s\n' "${L3[@]}" > "$E/scenario-M03/logs-2.txt"
printf '%s\n' "${L3[@]}" "AMORCE 2026-11-12T12:40:00Z : fin, code 5" > "$E/scenario-M03/logs-3.txt"
surv M03 0 "GARDÉE" "$H1H"
apres "second paquet en échec : aucun arrêt avant la fin de l'amorce (poussée des traces jamais coupée) ; trois tours" \
    "[ \$(wc -l < '$E/sortie-M03/etats.txt') = 3 ] && [ \$(grep -c '^stop' '$E/scenario-M03/actions') = 1 ]"
sc M04; printf '%s\n' "$A1" "$P1" "2026-11-12T11:00:00Z run : processus 4242 fini, code 137" "2026-11-12T11:01:00Z ARRÊT pendant run (code 137)" "AMORCE 2026-11-12T11:05:00Z : fin, code 1" > "$E/scenario-M04/logs-defaut.txt"
surv M04 0 "PROCESSUS MORT : fin, code 1 ; run : processus 4242 fini, code 137" "$H1H"
sc M05; printf '%s\n' "$A1" "AMORCE : clonage impossible (jeton GitHub ?)" > "$E/scenario-M05/logs-defaut.txt"
surv M05 0 "ÉCHEC D'AMORCE : AMORCE : clonage impossible" "$H1H"
sc M06; printf '%s\n' "$A1" "$P1" > "$E/scenario-M06/logs-1.txt"; printf '%s\n' "$A2" > "$E/scenario-M06/logs-2.txt"
surv M06 0 "REDÉMARRAGE" "$H1H"
sc M07; echo exited > "$E/scenario-M07/etat-defaut.txt"; printf '%s\n' "$A1" > "$E/scenario-M07/logs-defaut.txt"
surv M07 0 "ÉTAT TERMINAL" "$H1H"
sc M08; for k in 1 3 5; do echo offline > "$E/scenario-M08/etat-$k.txt"; done; printf '%s\n' "$A1" > "$E/scenario-M08/logs-defaut.txt"
printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M08/logs-6.txt"
surv M08 0 "FIN : " "$H1H"
sc M09; touch "$E/scenario-M09/etat-illisible-1" "$E/scenario-M09/etat-illisible-2"; printf '%s\n' "$A1" > "$E/scenario-M09/logs-defaut.txt"
printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M09/logs-3.txt"
surv M09 0 "FIN : " "$H1H"
apres "état illisible deux fois : jamais terminal ; prix illisible : borne de 2,10 USD/h prise et écrite" \
    "grep -q 'prix relu illisible : 2.10 USD/h pris' '$E/sortie-M09/depenses.txt'"
sc M10; printf '%s\n' "$A1" "$P1" > "$E/scenario-M10/logs-defaut.txt"
FAUX_ENV="FAUX_DPH=2.10" surv M10 0 "DÉPENSE : dépense " "$((MAINTENANT - 39 * 3600))"
sc M11; printf '%s\n' "$A1" "$P1" > "$E/scenario-M11/logs-defaut.txt"
surv M11 0 "DÉPENSE : dépense " "$H1H" 79.0
sc M12; printf '%s\n' "$A1" > "$E/scenario-M12/logs-defaut.txt"; printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M12/logs-3.txt"
FAUX_ENV="FAUX_DPH=2.10" surv M12 0 "FIN : " "$((MAINTENANT - 30 * 3600))" 0
apres "run de trente heures (bien au-delà des 22 200 s de P3) : aucun arrêt à durée ; dépense relevée à chaque tour (sous 80 USD) ; alerte écrite sans arrêt" \
    "[ \$(wc -l < '$E/sortie-M12/depenses.txt') = 2 ] && grep -q '^ALERTE' '$E/sortie-M12/alertes.txt' && [ \$(grep -c '^stop' '$E/scenario-M12/actions') = 1 ]"
sc M13; printf '%s\n' "$A1" > "$E/scenario-M13/logs-defaut.txt"; printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M13/logs-4.txt"
surv M13 0 "FIN : " "$((MAINTENANT - 7300))"
apres "alerte à deux heures sans PROGRES : une seule par fenêtre de deux heures, sans arrêt ni sortie avant la fin" \
    "[ \$(grep -c '^ALERTE' '$E/sortie-M13/alertes.txt') = 1 ] && grep -q '^ALERTE' '$E/console-M13.txt' && [ \$(wc -l < '$E/sortie-M13/etats.txt') = 4 ]"
sc M14; printf '%s\n' "$A1" "$P1" > "$E/scenario-M14/logs-1.txt"; printf '%s\n' "$A1" "$P1" "$RUNOK" "$FIN0" > "$E/scenario-M14/logs-2.txt"
surv M14 0 "FIN : " "$((MAINTENANT - 7300))"
apres "ligne PROGRES nouvelle au premier tour : aucune alerte" "[ ! -e '$E/sortie-M14/alertes.txt' ]"
sc M15; touch "$E/scenario-M15/stop-echec"; printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M15/logs-defaut.txt"
surv M15 1 "ARRÊT DE L'INSTANCE 99999999 EN ÉCHEC" "$H1H"
sc M16; printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M16/logs-defaut.txt"
surv M16 2 "ce lanceur a créé 99999999" "$H1H" 0 99999998 99999999
apres "identifiant autre que celui du lancement : aucun appel d'arrêt" "! grep -q '^stop' '$E/scenario-M16/actions' 2>/dev/null"
sc M17; printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M17/logs-defaut.txt"
surv M17 2 "ARRETEES_TOLEREES" "$H1H" 0 58936096 58936096
apres "instance tolérée (58936096) : jamais arrêtée, aucun appel" "[ ! -e '$E/scenario-M17/actions' ] || ! grep -q '58936096' '$E/scenario-M17/actions'"
sc M18; touch "$E/scenario-M18/logs-1.err"; printf '%s\n' "$A1" "$RUNOK" "$FIN0" > "$E/scenario-M18/logs-2.txt"
surv M18 0 "FIN : " "$H1H"
apres "journal illisible au premier tour : écrit, dernier relevé gardé" "grep -q 'journal illisible' '$E/sortie-M18/etats.txt'"
sc M19; printf '%s\n' "$A1" "PROGRES 2026-11-12T09:00:00Z etape=essai jeton=factice-gh-5555555" "$RUNOK" "$FIN0" > "$E/scenario-M19/logs-defaut.txt"
surv M19 0 "FIN : " "$H1H"
apres "jeton masqué dans le relevé" "grep -qF 'jeton=***' '$E/sortie-M19/progres.txt'"
# usage et refus de départ (code 2, aucun appel d'arrêt)
traces "$E/traces-U" "$H1H" 99999999
u() {   # $1 nom, $2 PATH, $3 jetons (oui/non), puis arguments
    local n=$1 ch=$2 j=$3 c; shift 3
    local env_j=(); [ "$j" = oui ] && env_j=("${JETONS[@]}")
    mkdir -p "$E/scenario-U"
    env -i PATH="$ch" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/scenario-U" INTERVALLE="${UINT:-0}" "${env_j[@]}" bash "$SURV" "$@" > "$E/console-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" 2 - "$E/console-$n.txt" "$E/scenario-U"
}
u U01-jetons-absents "$E/bin:/usr/bin:/bin" non 99999999 "$E/traces-U" 0 "$E/sortie-U01"
mkdir -p "$E/bin-sans"; u U02-outil-introuvable "$E/bin-sans:/usr/bin:/bin" oui 99999999 "$E/traces-U" 0 "$E/sortie-U02"
mkdir -p "$E/sortie-U03"; u U03-dossier-existant "$E/bin:/usr/bin:/bin" oui 99999999 "$E/traces-U" 0 "$E/sortie-U03"
u U04-usage "$E/bin:/usr/bin:/bin" oui 99999999 "$E/traces-U" "$E/sortie-U04"
u U05-anterieure-illisible "$E/bin:/usr/bin:/bin" oui 99999999 "$E/traces-U" "dix" "$E/sortie-U05"
UINT=601 u U06-intervalle-hors-bornes "$E/bin:/usr/bin:/bin" oui 99999999 "$E/traces-U" 0 "$E/sortie-U06"
mkdir -p "$E/traces-U7"; printf 'creation %s\noffre choisie : 111 (1.1 USD/h)\n' "$H1H" > "$E/traces-U7/lancement.txt"
u U07-sans-ligne-instance "$E/bin:/usr/bin:/bin" oui 99999999 "$E/traces-U7" 0 "$E/sortie-U07"
apres "refus de départ : aucun appel d'arrêt" "[ ! -e '$E/scenario-U/actions' ] || ! grep -q '^stop' '$E/scenario-U/actions'"
# --- contrôle à cinq minutes ----------------------------------------------------------------------------------------
S40=0123456789abcdef0123456789abcdef01234567
JOURNAL_OK=("$A1" "2026-11-12T08:00:20Z début : ETUDE=p3bis MODE=reel COMMIT=$S40 BRANCHE=calcul/p3bis-reel-v1"
            "2026-11-12T08:00:40Z préenregistrement lu : 436 tests attendus ; configuration prereg/P3-bis-temoin-positif-config-v1.json"
            "NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB" "2026-11-12T08:01:00Z branche calcul/p3bis-reel-v1 poussée avant l'installation (droit d'écriture éprouvé)")
ETAT_OK='{"actual_status": "running", "cur_state": "running", "dph_total": 1.10, "machine_id": 7101, "host_id": 8101, "gpu_name": "A100 SXM4", "label": "p3bis-v1"}'
cinq() {   # $1 nom, $2 code attendu, $3 motif, $4 état (JSON), $5 création ; le journal est dans $J5 (tableau) ; $6 identifiant
    local n=$1 attendu=$2 motif=$3 etat=$4 creation=${5:-$((MAINTENANT - 240))} id=${6:-99999999} c
    local s="$E/scenario-$n"
    mkdir -p "$s"; printf '%s\n' "$etat" > "$s/etat.json"; printf '%s\n' "${J5[@]}" > "$s/logs.txt"
    traces "$E/traces-$n" "$creation" 99999999 "${PRIX5:-1.1}"
    env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$s" "${JETONS[@]}" bash "$CINQ" "$id" "$E/traces-$n" "$E/sortie-$n" > "$E/console-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" "$attendu" "$motif" "$E/console-$n.txt" "$s"
    if [ "$attendu" = 1 ]; then apres "KO : instance arrêtée par son identifiant, une fois ; ligne à consigner" \
        "[ \$(grep -c '^stop instance 99999999\$' '$s/actions') = 1 ] && [ -s '$E/sortie-$n/arrets-a-consigner.txt' ]"
    elif [ "$attendu" = 0 ]; then apres "conforme : aucun arrêt" "! grep -q '^stop' '$s/actions'"; fi
}
J5=("${JOURNAL_OK[@]}")
cinq C00-sain 0 "CONTRÔLE À CINQ MINUTES : CONFORME" "$ETAT_OK"
cinq C01-trop-tot 2 "trop tôt" "$ETAT_OK" "$((MAINTENANT - 60))"
apres "trop tôt : rien n'est écrit" "[ ! -e '$E/sortie-C01-trop-tot' ]"
cinq C02-retard-ecrit 0 "CONFORME" "$ETAT_OK" "$((MAINTENANT - 400))"
apres "retard écrit" "grep -q 'retard écrit' '$E/sortie-C02-retard-ecrit/controle-5min.txt'"
J5=("${JOURNAL_OK[@]}" "AMORCE : commit introuvable"); cinq C03-echec-amorce 1 "arrêtée par son identifiant" "$ETAT_OK"
J5=("${JOURNAL_OK[@]/$S40/fedcba9876543210fedcba9876543210fedcba98}"); cinq C04-commit-autre 1 "arrêtée par son identifiant" "$ETAT_OK"
J5=("${JOURNAL_OK[@]/436 tests/435 tests}"); cinq C05-tests-autres 1 "arrêtée par son identifiant" "$ETAT_OK"
J5=("${JOURNAL_OK[@]/A100-SXM4-80GB, 580.159.03, 81920 MiB/A100-PCIE-40GB, 580.159.03, 40960 MiB}"); cinq C06-carte-autre 1 "arrêtée par son identifiant" "$ETAT_OK"
J5=("${JOURNAL_OK[@]}")
cinq C07-prix-au-dessus-du-choisi 1 "arrêtée par son identifiant" "${ETAT_OK/1.10/1.20}"
PRIX5=2.10 cinq C08-prix-au-dessus-du-plafond 1 "arrêtée par son identifiant" "${ETAT_OK/1.10/2.20}"
cinq C09-machine-autre 1 "arrêtée par son identifiant" "${ETAT_OK/7101/7102}"
cinq C10-etiquette-autre 1 "arrêtée par son identifiant" "${ETAT_OK/p3bis-v1/p3-v1}"
cinq C11-instance-arretee 1 "arrêtée par son identifiant" "${ETAT_OK/\"running\", \"cur_state\": \"running\"/\"exited\", \"cur_state\": \"stopped\"}"
J5=("${JOURNAL_OK[@]:0:4}"); cinq C12-branche-non-poussee 1 "arrêtée par son identifiant" "$ETAT_OK"
J5=("${JOURNAL_OK[@]}" "$A2"); cinq C13-redemarrage 1 "arrêtée par son identifiant" "$ETAT_OK"
J5=("${JOURNAL_OK[@]}"); cinq C14-etat-illisible 1 "arrêtée par son identifiant" "réponse non JSON"
mkdir -p "$E/scenario-C15-journal-illisible"; touch "$E/scenario-C15-journal-illisible/logs.err"
cinq C15-journal-illisible 1 "arrêtée par son identifiant" "$ETAT_OK"
mkdir -p "$E/scenario-C16-arret-en-echec"; touch "$E/scenario-C16-arret-en-echec/stop-echec"
J5=("${JOURNAL_OK[@]}" "AMORCE : clonage impossible")
NCAS_AVANT=$NCAS; NC_AVANT=$NON_CONFORMES
s="$E/scenario-C16-arret-en-echec"; printf '%s\n' "$ETAT_OK" > "$s/etat.json"; printf '%s\n' "${J5[@]}" > "$s/logs.txt"; traces "$E/traces-C16" "$((MAINTENANT - 240))" 99999999
env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$s" "${JETONS[@]}" bash "$CINQ" 99999999 "$E/traces-C16" "$E/sortie-C16" > "$E/console-C16.txt" 2>&1
verdict C16-arret-en-echec $? 1 "ARRÊT DE L'INSTANCE 99999999 EN ÉCHEC" "$E/console-C16.txt" "$s"
J5=("${JOURNAL_OK[@]}"); cinq C17-identifiant-autre 2 "ce lanceur a créé 99999999" "$ETAT_OK" "" 99999997
apres "identifiant autre : aucun appel d'arrêt" "[ ! -e '$E/scenario-C17-identifiant-autre/actions' ] || ! grep -q '^stop' '$E/scenario-C17-identifiant-autre/actions'"
J5=("${JOURNAL_OK[@]}" "fin du clonage, jeton factice-gi-4444444"); cinq C18-jeton-masque 0 "CONFORME" "$ETAT_OK"
apres "jeton masqué dans le journal gardé" "grep -qF 'jeton ***' '$E/sortie-C18-jeton-masque/journal-5min.txt'"
# refus de départ du contrôle à cinq minutes
traces "$E/traces-V" "$((MAINTENANT - 240))" 99999999
v5() { local n=$1 j=$2 c; shift 2; local env_j=(); [ "$j" = oui ] && env_j=("${JETONS[@]}"); mkdir -p "$E/scenario-V"
    env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$E/scenario-V" "${env_j[@]}" bash "$CINQ" "$@" > "$E/console-$n.txt" 2>&1; c=$?
    verdict "$n" "$c" 2 - "$E/console-$n.txt" "$E/scenario-V"; }
v5 V01-jetons-absents non 99999999 "$E/traces-V" "$E/sortie-V01"
mkdir -p "$E/sortie-V02"; v5 V02-dossier-existant oui 99999999 "$E/traces-V" "$E/sortie-V02"
mkdir -p "$E/traces-V3"; cp "$E/traces-V/lancement.txt" "$E/traces-V3/"; v5 V03-traces-incompletes oui 99999999 "$E/traces-V3" "$E/sortie-V03"
v5 V04-usage oui 99999999 "$E/traces-V"
echo "cas joués : $NCAS"
echo "FIN DU BANC DE LA SURVEILLANCE DE P3-BIS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ]
