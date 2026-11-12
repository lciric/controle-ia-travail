#!/usr/bin/env bash
# Essais R5 de l'écart 2 de P3-bis (R-2450 ; consigne `consigne-developpeur-p3bis-ecart2-v1.md`, `1fd50996…`), v1, écrits
# le 2026-11-12 vers 20:55 UTC (heure relevée par `date -u`). Bac à sable seulement : FAUX outil de location (aucun service
# appelé, aucune dépense), HORLOGE SIMULÉE (faux `date` et `sleep` sur le PATH des scripts joués : le temps n'avance que
# par `sleep`, ce qui rend les fenêtres de plusieurs minutes jouables en secondes et le journal reproductible), dépôt
# synthétique et dépôt nu local pour le bout en bout (comme les essais de l'écart 1), registre des GO temporaire
# (en-tête et ligne GO-2026-11-10-02 recopiés de main), contrôles avant dépense : BOUCHON. Un seul cas joue l'horloge
# réelle (E3-07, ≈ 3 min 30 s).
# Sections :
#   D1  module commun d'écart (« depense ») et surveillance d'écart : valeurs de la fille (cas sain), téléchargement
#       réellement excessif, seuil au centime, champs illisibles (majorant), témoins sur l'origine ;
#   D2  contrôle à cinq minutes d'écart : lignes à + 200 s, + 400 s, + 890 s, + 910 s, jamais ; signe d'échec à + 100 s,
#       à + 500 s ; états de démarrage, état terminal ; journal et état illisibles ; retard ; cas de l'origine repris
#       (commit, tests, carte, prix, machine, étiquette, redémarrage, arrêt en échec, identifiant, jetons, usage) ;
#       concordance avec les vrais scripts de l'instance ; témoin : contrôle d'origine joué à + 290 s ;
#   D3  enchaîneur v5 de bout en bout (appelants factices : faux outil, dépôt synthétique, bouchon des contrôles) ;
#   R   bancs existants rejoués : module commun (origine ; et re-pointé sur le module d'écart), surveillance (origine ; et
#       re-pointée sur la surveillance d'écart) ; originaux égaux à S.
# Usage : essais_ecart2_p3bis_v1.sh RACINE_NEUVE INTERPRETEUR_AVEC_PYTEST
set -uo pipefail
R=$(realpath -m "${1:?racine neuve}"); PYT=${2:?interpréteur Python avec pytest}
SOI=$(realpath "$0"); ICI=$(dirname "$SOI"); SRC=$(realpath "$ICI/../../..")
SCELLE=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0          # S (commit de scellement de P3-bis)
VERS=docs/procedures/P3-bis-temoin-positif-v1
MOD0=$ICI/verifications_p3bis_v2.py; MOD2=$ICI/verifications_p3bis_v2_ecart2_v1.py
CINQ0=$ICI/controle_cinq_minutes_p3bis_v2.sh; CINQ2=$ICI/controle_cinq_minutes_p3bis_v2_ecart2_v1.sh
SURV0=$ICI/surveiller_p3bis_v2.sh; SURV2=$ICI/surveiller_p3bis_v2_ecart2_v1.sh
ENCH=$ICI/enchaineur_p3bis_v5.sh; LE=lancer_p3bis_v2_ecart1_v2.sh; LO=lancer_p3bis_v2.sh
export PYTHONDONTWRITEBYTECODE=1
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R/bin" "$R/home" || exit 2
echo "début des essais : $(date -u +%FT%TZ)"
for f in "$MOD2" "$CINQ2" "$SURV2" "$ENCH" "$ICI/$LE" "$MOD0" "$CINQ0" "$SURV0" "$SOI"; do
    echo "script joué : $(basename "$f") $(sha256sum "$f" | cut -d' ' -f1)"
done
NC=0; NCAS=0
JETONS=(HF_TOKEN=factice-hf-8888888 CONTROLE_IA_GITHUB_TOKEN=factice-gi-9999999)
JETONS_RE='factice-hf-8888888|factice-gi-9999999|factice-g2-1212121'
res() {   # $1 nom, $2 0 si conforme, $3 description
    NCAS=$((NCAS + 1))
    if [ "$2" = 0 ]; then echo "$1 : $3 : CONFORME"; else echo "$1 : $3 : NON CONFORME"; NC=$((NC + 1)); fi
}
si() { (eval "$1") > /dev/null 2>&1; echo $?; }
# --- horloge simulée et faux outil de location (D1, D2) ---------------------------------------------------------------
cat > "$R/bin/date" <<'EOF'
#!/usr/bin/env bash
# faux date des essais de l'écart 2 : heure de l'horloge simulée $HORLOGE si elle existe, sinon heure réelle
if [ -n "${HORLOGE:-}" ] && [ -f "$HORLOGE" ]; then exec /usr/bin/date -d "@$(cat "$HORLOGE")" "$@"; fi
exec /usr/bin/date "$@"
EOF
cat > "$R/bin/sleep" <<'EOF'
#!/usr/bin/env bash
# faux sleep des essais de l'écart 2 : avance l'horloge simulée sans attendre ; sans horloge, vrai sleep
if [ -n "${HORLOGE:-}" ] && [ -f "$HORLOGE" ]; then n=${1%%.*}; echo $(( $(cat "$HORLOGE") + n )) > "$HORLOGE"; exit 0; fi
exec /usr/bin/sleep "$@"
EOF
cat > "$R/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location des essais de l'écart 2 (D1, D2) : scénario dans $SCENARIO ; n'appelle aucun service ; le journal
# rendu est fonction du temps écoulé depuis la création (lignes.tsv : « secondes<TAB>ligne »)
SC=${SCENARIO:?}
now=$(date -u +%s); cr=$(cat "$SC/creation"); el=$((now - cr))
echo "$el $*" >> "$SC/actions"
case "$1 $2" in
  "show instance")
    [ -e "$SC/arretee" ] && { printf '{"actual_status": "exited", "cur_state": "stopped", "dph_total": 1.09}\n'; exit 0; }
    if [ -e "$SC/etat-illisible-jusqu-a" ] && [ "$el" -lt "$(cat "$SC/etat-illisible-jusqu-a")" ]; then echo "réponse non JSON (essai)"; exit 0; fi
    st=running; [ -e "$SC/etats.tsv" ] && st=$(awk -F'\t' -v e="$el" '$1 <= e {s = $2} END {print s}' "$SC/etats.tsv")
    sed "s/__ETAT__/$st/" "$SC/etat.json" ;;
  "logs "*)
    if [ -e "$SC/logs-illisibles-jusqu-a" ] && [ "$el" -lt "$(cat "$SC/logs-illisibles-jusqu-a")" ]; then echo "erreur factice : instance injoignable" >&2; exit 1; fi
    awk -F'\t' -v e="$el" '$1 <= e {print $2}' "$SC/lignes.tsv" ;;
  "stop instance")
    [ -e "$SC/stop-echec" ] && { echo "erreur factice d'arrêt" >&2; exit 1; }
    touch "$SC/arretee"; echo '{"success": true}' ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$R/bin/date" "$R/bin/sleep" "$R/bin/vastai"
CR=1794495641                                         # création de 60370121 (note de la fille, 15:00:41Z)
S40=0123456789abcdef0123456789abcdef01234567
ETAT_JSON='{"actual_status": "__ETAT__", "cur_state": "running", "intended_status": "running", "status_msg": "essai", "dph_total": 1.09, "machine_id": 7101, "host_id": 8101, "gpu_name": "A100 SXM4", "label": "p3bis-v1", "inet_down_billed": 6564085.76, "inet_down_cost": 0.026, "inet_up_billed": 289792, "inet_up_cost": 0.04}'
traces() {   # $1 dossier ; lancement.txt, prereg-S.md, offre.json du lancement factice (instance 99999999)
    mkdir -p "$1"
    printf 'commit %s\nbranche calcul/p3bis-reel-v1\netiquette p3bis-v1\ncreation %s\noffre choisie : 111 (1.09 USD/h), la moins chère des offres conformes\ninstance 99999999\n' "$S40" "$CR" > "$1/lancement.txt"
    printf '# texte factice\n- Tests attendus : `531`\n' > "$1/prereg-S.md"
    printf '%s\n' '{"id": 111, "machine_id": 7101, "host_id": 8101, "dph_total": 1.09}' > "$1/offre.json"
}
L_AMORCE="AMORCE 2026-11-12T15:01:20Z : commit $S40"
L_DEBUT="2026-11-12T15:04:25Z début : ETUDE=p3bis MODE=reel COMMIT=$S40 BRANCHE=calcul/p3bis-reel-v1"
L_PREREG="2026-11-12T15:07:31Z préenregistrement lu : 531 tests attendus ; configuration prereg/P3-bis-temoin-positif-config-v1.json"
L_LISTE="2026-11-12T15:07:31Z liste ciblée : 9 fichiers d'essais"
L_BRANCHE="2026-11-12T15:07:40Z branche calcul/p3bis-reel-v1 poussée avant l'installation (droit d'écriture éprouvé)"
L_NVIDIA_T="name, driver_version, memory.total [MiB]"
L_CARTE="NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB"
scen() {   # $1 nom ; puis « secondes|ligne » … ; écrit le scénario (état sain par défaut)
    local s="$R/sc-$1"; shift; mkdir -p "$s"; : > "$s/lignes.tsv"
    printf '%s\n' "$ETAT_JSON" > "$s/etat.json"
    for x in "$@"; do printf '%s\t%s\n' "${x%%|*}" "${x#*|}" >> "$s/lignes.tsv"; done
}
std() {   # $1 amorce, $2 début, $3 reste (préenregistrement, liste, branche, carte) : remplit le tableau STD (format de scen)
    STD=("$1|$L_AMORCE" "$2|$L_DEBUT" "$3|$L_PREREG" "$3|$L_LISTE" "$3|$L_BRANCHE" "$3|$L_NVIDIA_T" "$3|$L_CARTE")
}
JAMAIS=99999
dernier_off() { sed -n 's/.*création + \([0-9]*\) s.*/\1/p' "$1/releves.txt" | tail -1; }
cinq() {   # $1 nom, $2 code attendu, $3 motif de la dernière ligne, $4 départ (s après la création), $5 script, $6 identifiant
    local n=$1 att=$2 motif=$3 dep=$4 scr=${5:-$CINQ2} id=${6:-99999999} s="$R/sc-$1" c v
    echo "$CR" > "$s/creation"; echo $((CR + dep)) > "$s/horloge"; traces "$R/tr-$n"
    env -i PATH="$R/bin:/usr/bin:/bin" HOME="$R/home" LANG=C.UTF-8 SCENARIO="$s" HORLOGE="$s/horloge" "${JETONS[@]}" \
        bash "$scr" "$id" "$R/tr-$n" "$R/so-$n" > "$R/console-$n.txt" 2>&1; c=$?
    v=0; [ "$c" = "$att" ] || v=1
    grep -v '^$' "$R/console-$n.txt" | tail -1 | grep -qF -- "$motif" || v=1
    grep -q 'destroy' "$s/actions" 2>/dev/null && v=1
    grep -rqE "$JETONS_RE" "$R/console-$n.txt" "$R/so-$n" 2>/dev/null && v=1
    res "$n" "$v" "code $c (attendu $att), « ${motif:0:60} »"
    grep -v '^$' "$R/console-$n.txt" | tail -1 | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
}
arrets() { grep -c '^[0-9]* stop instance 99999999$' "$R/sc-$1/actions" 2>/dev/null || true; }
# =================================================================================================== D1 : module commun
echo "=== D1 : dépense de téléchargement (module commun d'écart) ==="
dep() {   # $1 module, $2 entrée JSON, $3 antérieure, puis optionnellement maintenant ; création CR ; offre 1.09 ; intervalle 120
    printf '%s' "$2" | python3 -I "$1" depense "$CR" "${4:-$((CR + 294))}" 1.09 "$3" 120
}
FILLE='{"dph_total": 1.0889, "inet_down_billed": 6564085.76, "inet_down_cost": 0.026, "inet_up_billed": 289792, "inet_up_cost": 0.04}'
o=$(dep "$MOD0" "$FILLE" 0); c=$?
res D1-01-temoin-origine "$( [ "$c" = 3 ] && [[ "$o" == *"téléchargement 182257.91"* ]]; echo $?)" "module d'origine sur les valeurs de la fille : faux positif reproduit (code $c ; ${o:0:60}…)"
o=$(dep "$MOD2" "$FILLE" 0); c=$?
res D1-02-sain-valeurs-fille "$( [ "$c" = 0 ] && [[ "$o" == "dépense 0.28 USD (antérieure 0.00 ; calcul 0.09 à 1.0900 USD/h sur 294 s ; téléchargement 0.19, descente 6.72 Go, montée 0.30 Go (relevés en Kio)) ; projetée au prochain relevé 0.31 USD ; plafond 80 USD" ]]; echo $?)" "module d'écart sur les valeurs de la fille : dépense plausible, pas d'arrêt (code $c ; $o)"
o=$(dep "$MOD2" '{"dph_total": 1.09, "inet_down_billed": 3300000000, "inet_down_cost": 0.026, "inet_up_billed": 289792, "inet_up_cost": 0.04}' 0); c=$?
res D1-03-telechargement-excessif "$( [ "$c" = 3 ] && [[ "$o" == *"descente 3379.20 Go"* ]]; echo $?)" "3,3 × 10^9 Kio (3 379 Go) à 0,026 USD/Go : arrêt, code 3 ($o)"
o=$(dep "$MOD2" '{"dph_total": 1.09, "inet_down_billed": 1600000000, "inet_down_cost": 0.05}' 0); c=$?
res D1-04-excessif-prix-max "$( [ "$c" = 3 ]; echo $?)" "1,6 × 10^9 Kio (1 638 Go) au prix plafond du filtre, 0,05 USD/Go : arrêt, code 3 ($o)"
o=$(dep "$MOD2" "$FILLE" 79.60); c=$?
res D1-05-seuil-sous "$( [ "$c" = 0 ] && [[ "$o" == *"projetée au prochain relevé 79.91 USD"* ]]; echo $?)" "antérieure 79,60 : projetée 79,91, pas d'arrêt (code $c)"
o=$(dep "$MOD2" "$FILLE" 79.70); c=$?
res D1-06-seuil-dessus "$( [ "$c" = 3 ] && [[ "$o" == *"projetée au prochain relevé 80.01 USD"* ]]; echo $?)" "antérieure 79,70 : les 0,19 USD de téléchargement font passer le plafond, arrêt (code $c)"
o=$(dep "$MOD2" '{"dph_total": 1.09}' 0); c=$?
res D1-07-champs-absents "$( [ "$c" = 0 ] && [[ "$o" == *"téléchargement 2.00)"* && "$o" == *"téléchargement non relevé (descente, montée) : majorant 2.00 USD pris"* ]]; echo $?)" "champs absents : majorant 2,00 USD pris et écrit ($o)"
o=$(dep "$MOD2" '{"dph_total": 1.09, "inet_down_billed": "6564085.76", "inet_down_cost": 0.026, "inet_up_billed": 289792, "inet_up_cost": 0.04}' 0); c=$?
res D1-08-releve-texte "$( [ "$c" = 0 ] && [[ "$o" == *"téléchargement 2.01, montée 0.30 Go"* && "$o" == *"non relevé (descente) : majorant 2.00 USD pris"* ]]; echo $?)" "relevé de descente en texte : majorant ajouté à la montée relevée ($o)"
o=$(dep "$MOD2" '{"dph_total": 1.09, "inet_down_billed": 6564085.76, "inet_down_cost": -0.026}' 0); c=$?
res D1-09-prix-negatif "$( [[ "$o" == *"non relevé (descente, montée) : majorant 2.00 USD pris"* ]]; echo $?)" "prix au Go négatif : majorant ($o)"
o=$(dep "$MOD2" '{"dph_total": 1.09, "inet_down_billed": true, "inet_down_cost": 0.026}' 0); c=$?
res D1-10-releve-booleen "$( [[ "$o" == *"majorant 2.00 USD pris"* ]]; echo $?)" "relevé booléen : majorant ($o)"
o=$(dep "$MOD2" '{"dph_total": 1.09, "inet_down_billed": 6564085.76, "inet_down_cost": 0.026, "inet_up_billed": 289792}' 0); c=$?
res D1-11-montee-illisible "$( [ "$c" = 0 ] && [[ "$o" == *"téléchargement 2.17, descente 6.72 Go"* && "$o" == *"non relevé (montée) : majorant 2.00 USD pris"* ]]; echo $?)" "montée illisible : descente relevée plus majorant, jamais zéro en silence ($o)"
o=$(dep "$MOD0" '{"dph_total": 1.09, "inet_down_billed": 6564085.76, "inet_down_cost": 0.026, "inet_up_billed": 289792}' 0); c=$?
res D1-12-temoin-montee-origine "$( [[ "$o" != *"majorant"* ]]; echo $?)" "témoin : l'origine compte la montée illisible pour zéro, sans rien écrire ($o)"
o=$(dep "$MOD2" "pas du json" 0); c=$?
res D1-13-reponse-illisible "$( [ "$c" = 0 ] && [[ "$o" == *"prix relu illisible : 2.10 USD/h pris"* && "$o" == *"majorant 2.00 USD pris"* ]]; echo $?)" "réponse non JSON : bornes de prix et de téléchargement prises, écrites ($o)"
c=0; printf '{}' | python3 -I "$MOD2" depense x 1 1 0 1 > /dev/null 2>&1 || c=$?
res D1-14-arguments-illisibles "$( [ "$c" = 1 ]; echo $?)" "arguments illisibles : code 1 (comme l'origine)"
d=$(diff "$MOD0" "$MOD2" | grep -E '^[0-9]' | tr '\n' ' ')
c=0; python3 -I - "$MOD0" "$MOD2" <<'EOF' || c=$?
import ast, sys
def noeuds(p):   # instructions de premier niveau, hors docstring, fonction « depense » et deux constantes neuves de l'écart 2
    out = []
    for i, n in enumerate(ast.parse(open(p, encoding="utf-8").read()).body):
        if i == 0 and isinstance(n, ast.Expr):
            continue
        if isinstance(n, ast.FunctionDef) and n.name == "depense":
            continue
        if isinstance(n, ast.Assign) and any(getattr(x, "id", "") in ("OCTETS_PAR_UNITE_RELEVEE", "OCTETS_PAR_GO_PRIX") for x in n.targets):
            continue
        out.append(ast.dump(n))
    return out
a, b = noeuds(sys.argv[1]), noeuds(sys.argv[2])
sys.exit(0 if a == b and len(a) > 40 else 1)
EOF
res D1-15-diff-du-module "$c" "arbre syntaxique égal à l'origine hors docstring, fonction « depense » et constantes OCTETS_PAR_* (blocs du diff : $d)"
# =================================================================================================== D1 : surveillance
echo "=== D1 : surveillance d'écart ==="
surv() {   # $1 nom, $2 code attendu, $3 motif, $4 script, $5 départ (s après la création), $6 dépense antérieure
    local n=$1 att=$2 motif=$3 scr=$4 dep=$5 an=${6:-0} s="$R/sc-$1" c v
    echo "$CR" > "$s/creation"; echo $((CR + dep)) > "$s/horloge"; traces "$R/tr-$n"
    env -i PATH="$R/bin:/usr/bin:/bin" HOME="$R/home" LANG=C.UTF-8 SCENARIO="$s" HORLOGE="$s/horloge" "${JETONS[@]}" \
        bash "$scr" 99999999 "$R/tr-$n" "$an" "$R/so-$n" > "$R/console-$n.txt" 2>&1; c=$?
    v=0; [ "$c" = "$att" ] || v=1
    grep -v '^$' "$R/console-$n.txt" | tail -1 | grep -qF -- "$motif" || v=1
    grep -q 'destroy' "$s/actions" 2>/dev/null && v=1
    grep -rqE "$JETONS_RE" "$R/console-$n.txt" "$R/so-$n" 2>/dev/null && v=1
    res "$n" "$v" "code $c (attendu $att), « ${motif:0:60} »"
    grep -v '^$' "$R/console-$n.txt" | tail -1 | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
}
FIN_A="AMORCE 2026-11-12T18:00:00Z : fin, code 0"
RUN_OK="2026-11-12T17:50:00Z run : processus 4242 fini, code 0"
P_1="PROGRES 2026-11-12T16:00:00Z etape=entrainement concept=tromperie aire_validation=1.0"
std 40 224 425; scen S1-01-sain-valeurs-fille "${STD[@]}" "1200|$P_1" "2900|$RUN_OK" "3000|$FIN_A"
surv S1-01-sain-valeurs-fille 0 "FIN : $FIN_A ; instance 99999999 arrêtée par son identifiant (R10)" "$SURV2" 294
res S1-01b "$( [ "$(arrets S1-01-sain-valeurs-fille)" = 1 ] && ! grep -q DÉPENSE "$R/console-S1-01-sain-valeurs-fille.txt" && [ "$(wc -l < "$R/so-S1-01-sain-valeurs-fille/depenses.txt")" -ge 20 ] && grep -q 'téléchargement 0.19, descente 6.72 Go, montée 0.30 Go' "$R/so-S1-01-sain-valeurs-fille/depenses.txt"; echo $?)" \
    "valeurs de la fille à chaque relevé : aucun arrêt pour la dépense, fin normale seule ; un arrêt par l'identifiant ; dépense écrite à chaque tour"
cp -r "$R/sc-S1-01-sain-valeurs-fille" "$R/sc-S1-02-temoin-origine"; rm -f "$R/sc-S1-02-temoin-origine/actions" "$R/sc-S1-02-temoin-origine/arretee"
surv S1-02-temoin-origine 0 "DÉPENSE : dépense 182258.00 USD" "$SURV0" 294
res S1-02b "$( [ "$(arrets S1-02-temoin-origine)" = 1 ] && [ "$(wc -l < "$R/so-S1-02-temoin-origine/etats.txt")" = 1 ]; echo $?)" "témoin : la surveillance d'origine arrête au premier relevé (faux positif de R-2446 reproduit)"
std 40 224 425; scen S1-03-excessif "${STD[@]}" "3000|$FIN_A"
sed -i 's/"inet_down_billed": 6564085.76/"inet_down_billed": 3300000000/' "$R/sc-S1-03-excessif/etat.json"
surv S1-03-excessif 0 "DÉPENSE : dépense 87.96 USD" "$SURV2" 294
res S1-03b "$( [ "$(arrets S1-03-excessif)" = 1 ] && [ "$(cat "$R/so-S1-03-excessif/motif.txt")" = DÉPENSE ]; echo $?)" "téléchargement réellement excessif : arrêt par l'identifiant, motif DÉPENSE (garde intacte)"
std 40 224 425; scen S1-04-champs-absents "${STD[@]}" "1000|$FIN_A"
sed -i 's/, "inet_down_billed": 6564085.76, "inet_down_cost": 0.026, "inet_up_billed": 289792, "inet_up_cost": 0.04//' "$R/sc-S1-04-champs-absents/etat.json"
surv S1-04-champs-absents 0 "FIN : $FIN_A" "$SURV2" 294 0.53
res S1-04b "$( grep -q 'antérieure 0.53' "$R/so-S1-04-champs-absents/depenses.txt" && grep -q 'téléchargement non relevé (descente, montée) : majorant 2.00 USD pris' "$R/so-S1-04-champs-absents/depenses.txt"; echo $?)" "champs illisibles : majorant écrit à chaque relevé ; dépense antérieure passée comptée"
mkdir -p "$R/h-sans-module"; cp "$SURV2" "$MOD0" "$R/h-sans-module/"
scen S1-05-module-ecart-absent "40|$L_AMORCE"
surv S1-05-module-ecart-absent 2 "module commun d'écart" "$R/h-sans-module/surveiller_p3bis_v2_ecart2_v1.sh" 294
res S1-05b "$( [ ! -e "$R/sc-S1-05-module-ecart-absent/actions" ]; echo $?)" "module d'écart absent : refus de départ, aucun appel à l'outil"
# =================================================================================================== D2 : contrôle
echo "=== D2 : contrôle à cinq minutes d'écart (attente bornée) ==="
std 40 100 170; scen C2-01-sain-immediat "${STD[@]}"
cinq C2-01-sain-immediat 0 "CONTRÔLE À CINQ MINUTES : CONFORME" 181
res C2-01b "$( [ "$(wc -l < "$R/so-C2-01-sain-immediat/releves.txt")" = 1 ] && [ "$(arrets C2-01-sain-immediat)" = 0 ]; echo $?)" "un seul relevé (création + 181 s), aucun arrêt"
for x in "C2-02-lignes-a-200:200:211:2" "C2-03-lignes-a-400:400:421:9" "C2-04-lignes-a-890:890:900:25"; do
    IFS=: read -r n a off nr <<< "$x"
    std 40 "$a" "$a"; scen "$n" "${STD[@]}"
    cinq "$n" 0 "CONTRÔLE À CINQ MINUTES : CONFORME" 181
    res "${n}b" "$( [ "$(dernier_off "$R/so-$n")" = "$off" ] && [ "$(wc -l < "$R/so-$n/releves.txt")" = "$nr" ] && [ "$(arrets "$n")" = 0 ] && ! grep -q '^KO' "$R/so-$n/controle-5min.txt"; echo $?)" \
        "lignes à + $a s : conforme au relevé de la création + $off s ($nr relevés), aucun KO, aucun arrêt"
done
std 40 224 910; scen C2-05-lignes-a-910 "${STD[@]}"
cinq C2-05-lignes-a-910 1 "instance 99999999 arrêtée par son identifiant (R10)" 181
res C2-05b "$( [ "$(dernier_off "$R/so-C2-05-lignes-a-910")" = 900 ] && [ "$(arrets C2-05-lignes-a-910)" = 1 ] && [ "$(grep -c "(à l'échéance)" "$R/so-C2-05-lignes-a-910/etat.txt")" = 3 ] && [ -s "$R/so-C2-05-lignes-a-910/arrets-a-consigner.txt" ]; echo $?)" \
    "lignes à + 910 s : KO à l'échéance exacte (création + 900 s), trois KO « à l'échéance », un arrêt par l'identifiant, ligne à consigner"
scen C2-06-jamais "40|$L_AMORCE" "224|$L_DEBUT"
cinq C2-06-jamais 1 "3 KO ; instance 99999999 arrêtée par son identifiant (R10)" 181
res C2-06b "$( [ "$(dernier_off "$R/so-C2-06-jamais")" = 900 ] && [ "$(arrets C2-06-jamais)" = 1 ] && [ "$(grep -c '^KO' "$R/so-C2-06-jamais/etat.txt")" = 3 ]; echo $?)" "lignes jamais écrites : KO seulement à l'échéance (+ 900 s), un arrêt"
scen C2-07-echec-a-100 "40|$L_AMORCE" "100|AMORCE : clonage impossible (jeton GitHub ?)"
cinq C2-07-echec-a-100 1 "arrêtée par son identifiant (R10)" 181
res C2-07b "$( [ "$(dernier_off "$R/so-C2-07-echec-a-100")" = 181 ] && [ "$(arrets C2-07-echec-a-100)" = 1 ]; echo $?)" "ligne d'échec écrite à + 100 s : arrêt immédiat au premier relevé (+ 181 s)"
scen C2-08-echec-a-500 "40|$L_AMORCE" "224|$L_DEBUT" "500|2026-11-12T15:09:01Z branche calcul/p3bis-reel-v1 déjà présente sur le dépôt distant : relancement sous une branche nouvelle (BRANCHE=…) ; arrêt avant l'installation" "505|AMORCE 2026-11-12T15:09:06Z : fin, code 2"
cinq C2-08-echec-a-500 1 "arrêtée par son identifiant (R10)" 181
res C2-08b "$( [ "$(dernier_off "$R/so-C2-08-echec-a-500")" = 511 ] && [ "$(arrets C2-08-echec-a-500)" = 1 ] && grep -q "fin de l'amorce pendant le contrôle" "$R/so-C2-08-echec-a-500/etat.txt"; echo $?)" \
    "fin de l'amorce à + 505 s (après des attentes) : arrêt au relevé suivant (+ 511 s), pas à l'échéance"
std 40 224 425; scen C2-09-demarrage-lent "${STD[@]}"
printf '0\tloading\n300\trunning\n' > "$R/sc-C2-09-demarrage-lent/etats.tsv"
cinq C2-09-demarrage-lent 0 "CONTRÔLE À CINQ MINUTES : CONFORME" 181
res C2-09b "$( grep -q '^relevé 1 .*en attente' "$R/so-C2-09-demarrage-lent/releves.txt" && [ "$(arrets C2-09-demarrage-lent)" = 0 ]; echo $?)" "état « loading » jusqu'à + 300 s : attente, puis conforme"
std 40 224 600; scen C2-10-etat-terminal "${STD[@]}"
printf '0\trunning\n400\texited\n' > "$R/sc-C2-10-etat-terminal/etats.tsv"
cinq C2-10-etat-terminal 1 "arrêtée par son identifiant (R10)" 181
res C2-10b "$( [ "$(dernier_off "$R/so-C2-10-etat-terminal")" = 421 ] && grep -q 'ni en marche ni en démarrage (exited)' "$R/so-C2-10-etat-terminal/etat.txt"; echo $?)" "état « exited » à + 400 s : signe d'échec, arrêt au relevé de + 421 s"
std 40 100 170; scen C2-11-journal-illisible-puis-lu "${STD[@]}"
echo 300 > "$R/sc-C2-11-journal-illisible-puis-lu/logs-illisibles-jusqu-a"
cinq C2-11-journal-illisible-puis-lu 0 "CONTRÔLE À CINQ MINUTES : CONFORME" 181
res C2-11b "$( [ "$(dernier_off "$R/so-C2-11-journal-illisible-puis-lu")" = 301 ] && [ "$(arrets C2-11-journal-illisible-puis-lu)" = 0 ]; echo $?)" "journal illisible jusqu'à + 300 s : attente, conforme à + 301 s"
std 40 100 170; scen C2-12-journal-toujours-illisible "${STD[@]}"
echo "$JAMAIS" > "$R/sc-C2-12-journal-toujours-illisible/logs-illisibles-jusqu-a"
cinq C2-12-journal-toujours-illisible 1 "arrêtée par son identifiant (R10)" 181
res C2-12b "$( [ "$(dernier_off "$R/so-C2-12-journal-toujours-illisible")" = 900 ] && grep -q "journal de l'instance illisible.*(à l'échéance)" "$R/so-C2-12-journal-toujours-illisible/etat.txt" && [ -s "$R/so-C2-12-journal-toujours-illisible/journal-erreur.txt" ]; echo $?)" \
    "journal toujours illisible : KO à l'échéance (l'origine : KO immédiat ; écart déclaré)"
std 40 100 170; scen C2-13-etat-toujours-illisible "${STD[@]}"
echo "$JAMAIS" > "$R/sc-C2-13-etat-toujours-illisible/etat-illisible-jusqu-a"
cinq C2-13-etat-toujours-illisible 1 "arrêtée par son identifiant (R10)" 181
res C2-13b "$( [ "$(dernier_off "$R/so-C2-13-etat-toujours-illisible")" = 900 ] && grep -q "état de l'instance illisible.*(à l'échéance)" "$R/so-C2-13-etat-toujours-illisible/etat.txt"; echo $?)" "état toujours illisible : KO à l'échéance (l'origine : KO immédiat ; écart déclaré)"
std 40 100 170; scen C2-14-retard-sain "${STD[@]}"
cinq C2-14-retard-sain 0 "CONTRÔLE À CINQ MINUTES : CONFORME" 1000
res C2-14b "$( grep -q 'retard écrit' "$R/so-C2-14-retard-sain/controle-5min.txt" && [ "$(wc -l < "$R/so-C2-14-retard-sain/releves.txt")" = 1 ]; echo $?)" "commencé à + 1 000 s : un seul relevé, retard écrit, conforme"
scen C2-15-retard-ligne-absente "40|$L_AMORCE" "100|$L_DEBUT"
cinq C2-15-retard-ligne-absente 1 "arrêtée par son identifiant (R10)" 1000
res C2-15b "$( [ "$(wc -l < "$R/so-C2-15-retard-ligne-absente/releves.txt")" = 1 ] && [ "$(arrets C2-15-retard-ligne-absente)" = 1 ]; echo $?)" "commencé après l'échéance, lignes absentes : KO au seul relevé"
scen C2-16-trop-tot "40|$L_AMORCE"
cinq C2-16-trop-tot 2 "trop tôt : création + 100 s" 100
res C2-16b "$( [ ! -e "$R/so-C2-16-trop-tot" ] && [ ! -e "$R/sc-C2-16-trop-tot/actions" ]; echo $?)" "avant + 180 s : refus, rien n'est écrit, aucun appel (inchangé)"
# cas de l'origine repris (signes d'échec immédiats, sauf mention)
scen C2-17-commit-autre "40|${L_AMORCE/$S40/fedcba9876543210fedcba9876543210fedcba98}"
cinq C2-17-commit-autre 1 "arrêtée par son identifiant (R10)" 181
res C2-17b "$( [ "$(dernier_off "$R/so-C2-17-commit-autre")" = 181 ]; echo $?)" "AMORCE d'un autre commit : arrêt immédiat"
scen C2-18-tests-autres "40|$L_AMORCE" "224|$L_DEBUT" "400|${L_PREREG/531 tests/530 tests}"
cinq C2-18-tests-autres 1 "arrêtée par son identifiant (R10)" 181
res C2-18b "$( [ "$(dernier_off "$R/so-C2-18-tests-autres")" = 421 ]; echo $?)" "« préenregistrement lu : 530 » à + 400 s : arrêt au relevé suivant"
std 40 224 400; scen C2-19-carte-autre "${STD[@]/A100-SXM4-80GB, 580.159.03, 81920 MiB/A100-PCIE-40GB, 580.159.03, 40960 MiB}"
cinq C2-19-carte-autre 1 "arrêtée par son identifiant (R10)" 181
res C2-19b "$( [ "$(dernier_off "$R/so-C2-19-carte-autre")" = 421 ] && grep -q "carte autre qu'une A100 SXM4" "$R/so-C2-19-carte-autre/etat.txt"; echo $?)" "carte A100 PCIE 40 Go : signe d'échec dès qu'elle est écrite"
std 40 224 400; scen C2-20-carte-sxm4-40go "${STD[@]/A100-SXM4-80GB, 580.159.03, 81920 MiB/A100-SXM4-40GB, 580.159.03, 40960 MiB}"
cinq C2-20-carte-sxm4-40go 1 "arrêtée par son identifiant (R10)" 181
for x in "C2-21-prix-au-dessus-du-choisi#\"dph_total\": 1.09#\"dph_total\": 1.20" "C2-22-prix-au-dessus-du-plafond#\"dph_total\": 1.09#\"dph_total\": 2.20" \
         "C2-23-machine-autre#\"machine_id\": 7101#\"machine_id\": 7102" "C2-24-etiquette-autre#\"label\": \"p3bis-v1\"#\"label\": \"p3-v1\"" \
         "C2-25-carte-relue-autre#\"gpu_name\": \"A100 SXM4\"#\"gpu_name\": \"A100 PCIE\""; do
    IFS='#' read -r n a b <<< "$x"
    std 40 100 170; scen "$n" "${STD[@]}"; sed -i "s/$a/$b/" "$R/sc-$n/etat.json"
    grep -qF "$b" "$R/sc-$n/etat.json" || echo "$n : scénario mal formé"
    cinq "$n" 1 "arrêtée par son identifiant (R10)" 181
    res "${n}b" "$( [ "$(dernier_off "$R/so-$n")" = 181 ] && [ "$(arrets "$n")" = 1 ]; echo $?)" "signe d'échec de l'état : arrêt immédiat au premier relevé"
done
std 40 100 170; scen C2-26-label-absent "${STD[@]}"; sed -i 's/, "label": "p3bis-v1"//' "$R/sc-C2-26-label-absent/etat.json"
cinq C2-26-label-absent 1 "arrêtée par son identifiant (R10)" 181
res C2-26b "$( [ "$(dernier_off "$R/so-C2-26-label-absent")" = 900 ]; echo $?)" "étiquette absente : attente, KO à l'échéance"
std 40 224 425; scen C2-27-redemarrage "${STD[@]}" "300|${L_AMORCE/15:01:20/15:05:41}"
cinq C2-27-redemarrage 1 "arrêtée par son identifiant (R10)" 181
res C2-27b "$( grep -q 'répétée (redémarrage)' "$R/so-C2-27-redemarrage/etat.txt" && [ "$(dernier_off "$R/so-C2-27-redemarrage")" = 301 ]; echo $?)" "AMORCE répétée à + 300 s : redémarrage, arrêt au relevé suivant (+ 301 s)"
scen C2-28-arret-en-echec "40|$L_AMORCE" "100|AMORCE : clonage impossible (jeton GitHub ?)"; touch "$R/sc-C2-28-arret-en-echec/stop-echec"
cinq C2-28-arret-en-echec 1 "ARRÊT DE L'INSTANCE 99999999 EN ÉCHEC" 181
scen C2-29-identifiant-autre "40|$L_AMORCE"
cinq C2-29-identifiant-autre 2 "ce lanceur a créé 99999999" 181 "$CINQ2" 99999997
res C2-29b "$( [ ! -e "$R/sc-C2-29-identifiant-autre/actions" ]; echo $?)" "identifiant autre : aucun appel"
std 40 100 170; scen C2-30-jeton-masque "${STD[@]}" "171|fin du clonage, jeton factice-gi-9999999"
cinq C2-30-jeton-masque 0 "CONFORME" 181
res C2-30b "$( grep -qF 'jeton ***' "$R/so-C2-30-jeton-masque/journal-5min.txt"; echo $?)" "jeton masqué dans le journal gardé"
# refus de départ
traces "$R/tr-V"; mkdir -p "$R/sc-V"; echo "$CR" > "$R/sc-V/creation"; echo $((CR + 200)) > "$R/sc-V/horloge"
v5c() { local n=$1 j=$2 c v; shift 2; local ej=(); [ "$j" = oui ] && ej=("${JETONS[@]}")
    env -i PATH="$R/bin:/usr/bin:/bin" HOME="$R/home" LANG=C.UTF-8 SCENARIO="$R/sc-V" HORLOGE="$R/sc-V/horloge" "${ej[@]}" bash "$CINQ2" "$@" > "$R/console-$n.txt" 2>&1; c=$?
    v=0; [ "$c" = 2 ] || v=1; res "$n" "$v" "refus de départ, code $c (attendu 2)"; }
v5c C2-V01-jetons-absents non 99999999 "$R/tr-V" "$R/so-V01"
mkdir -p "$R/so-V02"; v5c C2-V02-dossier-existant oui 99999999 "$R/tr-V" "$R/so-V02"
mkdir -p "$R/tr-V3"; cp "$R/tr-V/lancement.txt" "$R/tr-V3/"; v5c C2-V03-traces-incompletes oui 99999999 "$R/tr-V3" "$R/so-V03"
v5c C2-V04-usage oui 99999999 "$R/tr-V"
res C2-V05 "$( [ ! -e "$R/sc-V/actions" ]; echo $?)" "refus de départ : aucun appel à l'outil"
# concordance des lignes lues avec les vrais scripts de l'instance et de l'amorce (S)
INST=$SRC/scripts/p3bis_instance_v2.sh; AMOR=$SRC/scripts/amorce_instance_p3bis_v2.sh
for x in "$INST|journal \"début : ETUDE=\$ETUDE MODE=\$MODE COMMIT=\$COMMIT BRANCHE=\$BRANCHE\"" "$INST|journal \"préenregistrement lu : \$ATTENDUS tests attendus ;" \
         "$INST|journal \"branche \$BRANCHE poussée avant l'installation" "$INST|nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv" \
         "$AMOR|echo \"AMORCE \$(date -u +%FT%TZ) : commit \$COMMIT\"" "$AMOR|echo \"AMORCE \$(date -u +%FT%TZ) : fin, code \$code\"" \
         "$AMOR|echo \"AMORCE : clonage impossible" "$AMOR|git -c credential.helper=\"\$AIDE\" clone -q \"\$DEPOT_URL\" amorce-depot" \
         "$INST|git -c credential.helper=\"\$AIDE_GIT\" clone -q \"\$DEPOT_URL\" \"\$DEPOT\""; do
    f=${x%%|*}; frag=${x#*|}
    res "C2-X-$(basename "$f")" "$( grep -qF -- "$frag" "$f"; echo $?)" "« ${frag:0:70} » présent dans le vrai script"
done
res C2-X-ordre "$( a=$(grep -nF 'journal "début : ETUDE=' "$INST" | cut -d: -f1); b=$(grep -nF 'clone -q "$DEPOT_URL" "$DEPOT"' "$INST" | cut -d: -f1); p=$(grep -nF 'journal "branche $BRANCHE poussée avant' "$INST" | cut -d: -f1); n=$(grep -nF 'nvidia-smi --query-gpu' "$INST" | cut -d: -f1); [ "$a" -lt "$b" ] && [ "$b" -lt "$p" ] && [ "$p" -lt "$n" ]; echo $?)" \
    "ordre dans le script de l'instance : « début », second clonage, « branche poussée », carte (cause de D2)"
# témoin : contrôle d'origine joué à + 290 s (enchaîneur v4) sur des lignes qui arrivent à + 410 s
std 40 224 410; scen C2-T1-temoin-origine-290 "${STD[@]}"
cinq C2-T1-temoin-origine-290 1 "3 KO ; instance 99999999 arrêtée par son identifiant (R10)" 290 "$CINQ0"
cp -r "$R/sc-C2-T1-temoin-origine-290" "$R/sc-C2-T2-meme-scenario-ecart"; rm -f "$R/sc-C2-T2-meme-scenario-ecart/actions" "$R/sc-C2-T2-meme-scenario-ecart/arretee"
cinq C2-T2-meme-scenario-ecart 0 "CONTRÔLE À CINQ MINUTES : CONFORME" 290
res C2-T2b "$( [ "$(dernier_off "$R/so-C2-T2-meme-scenario-ecart")" = 410 ]; echo $?)" "même scénario, contrôle d'écart : conforme à + 410 s, sans arrêt (défaut de R-2446 corrigé)"
res C2-K1-constantes "$( grep -qx 'PRIX_MAX=2.10                                    # plan, point 11 (même valeur que le module commun ; contrôles, constantes)' "$CINQ2" && grep -qx 'DELAI_MIN_S=180' "$CINQ2" && grep -q '^ECHEANCE_S=900 ' "$CINQ2" && grep -q '^PAS_S=30 ' "$CINQ2"; echo $?)" \
    "constantes du contrôle d'écart : PRIX_MAX 2.10 et DELAI_MIN_S 180 (inchangés), ECHEANCE_S 900, PAS_S 30"
res C2-K2-preambule-et-arret "$( [ "$(diff <(sed -n '/^ETUDE=p3bis; MODE=reel$/,/^mkdir -p "\$D" || exit 2$/p' "$CINQ0" | grep -v '^    || { echo "usage') <(sed -n '/^ETUDE=p3bis; MODE=reel$/,/^mkdir -p "\$D" || exit 2$/p' "$CINQ2" | grep -v '^    || { echo "usage') | wc -l)" = 0 ] && [ "$(diff <(sed -n '/^# arrêt de l.instance par son identifiant (R10)/,$p' "$CINQ0") <(sed -n '/^# arrêt de l.instance par son identifiant (R10)/,$p' "$CINQ2") | wc -l)" = 0 ]; echo $?)" \
    "préambule (de « ETUDE=… » au dossier de sortie, hors message d'usage) et bloc d'arrêt égaux à l'origine, octet pour octet"
# =================================================================================================== D3 : enchaîneur v5
echo "=== D3 : enchaîneur v5, de bout en bout sur appelants factices ==="
E2=$R/e2e; mkdir -p "$E2/bin" "$E2/H" "$E2/home" "$E2/etat" || exit 2
cp "$R/bin/date" "$R/bin/sleep" "$E2/bin/"
for s in "$LO" "$LE"; do
    sed -e "s|^DEPOT=.*|DEPOT=$E2/depot|" -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$E2/distant.git|" -e "s|^INTERVALLE_OFFRE_S=.*|INTERVALLE_OFFRE_S=0|" "$ICI/$s" > "$E2/H/$s"
    n=$(diff "$ICI/$s" "$E2/H/$s" | grep -c '^>'); echo "lignes changées dans la copie jouée de $s : $n (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S)"
    [ "$n" = 3 ] || { echo "copie de $s non sûre"; exit 2; }
done
for s in verifications_p3bis_v2.py controle_cinq_minutes_p3bis_v2.sh surveiller_p3bis_v2.sh detruire_p3bis_v2.sh \
         verifications_p3bis_v2_ecart2_v1.py controle_cinq_minutes_p3bis_v2_ecart2_v1.sh surveiller_p3bis_v2_ecart2_v1.sh; do cp "$ICI/$s" "$E2/H/"; done
EL=$(sha256sum "$E2/H/$LE" | cut -d' ' -f1)
sed "s|^LANCEUR=lancer_p3bis_v2_ecart1_v2.sh;             E_LANCEUR=.*|LANCEUR=lancer_p3bis_v2_ecart1_v2.sh;             E_LANCEUR=$EL|" "$ENCH" > "$E2/H/enchaineur_p3bis_v5.sh"
n=$(diff "$ENCH" "$E2/H/enchaineur_p3bis_v5.sh" | grep -c '^>'); echo "lignes changées dans la copie jouée de l'enchaîneur v5 : $n (empreinte épinglée du lanceur : celle de sa copie jouée)"
[ "$n" = 1 ] || { echo "copie de l'enchaîneur non sûre"; exit 2; }
cat > "$E2/H/controles_avant_depense_p3bis_v2.sh" <<'EOF'
#!/usr/bin/env bash
# bouchon des essais de l'écart 2 : les contrôles réels sont joués par leur banc et par la répétition finale
mkdir -p "$2" "$2.travail"; echo "OK  bouchon des essais de l'écart 2 (S=${1:0:12}, branche $3)"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
CHAINE=$(sed -n 's/^CHAINE="\(.*\)"$/\1/p' "$E2/H/$LO")
for s in $CHAINE; do [ -e "$E2/H/$s" ] || cp "$ICI/$s" "$E2/H/$s"; done
git init -q --bare -b main "$E2/distant.git"
git init -q -b main "$E2/depot" && cd "$E2/depot" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false; git config push.negotiate false
git remote add origin "$E2/distant.git"
P=prereg/P3-bis-temoin-positif-v1.md; A=scripts/amorce_instance_p3bis_v2.sh
mkdir -p prereg scripts registres .claude/hooks "$VERS"
cp "$SRC/$A" "$A"; cp "$SRC/.claude/hooks/garde_calcul.py" .claude/hooks/garde_calcul.py
{ git -C "$SRC" show main:registres/go.md | sed -n '1,10p'; git -C "$SRC" show main:registres/go.md | grep '^| GO-2026-11-10-02 |'; } > registres/go.md
[ "$(grep -c '^| GO-2026-11-10-02 |' registres/go.md)" = 1 ] || { echo "ligne GO-2026-11-10-02 absente de main"; exit 2; }
for s in "$LO" $CHAINE; do cp "$E2/H/$s" "$VERS/$s"; done
python3 -I -B - "$E2/H/verifications_p3bis_v2.py" "$E2/H" "$VERS" <<'EOF' || exit 2
import hashlib, importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
h, sortie = Path(sys.argv[2]), Path(sys.argv[3])
for nom, (verdict, scripts) in v.JOURNAUX.items():
    lignes = [f"script éprouvé : {s} {hashlib.sha256((h / s).read_bytes()).hexdigest()}" for s in sorted(scripts)]
    (sortie / nom).write_text("\n".join(lignes) + "\njournal factice des essais de l'écart 2\n" + verdict + "\n", encoding="utf-8")
EOF
(cd "$VERS" && for f in *; do case "$f" in *.sha256) ;; *) sha256sum "$f" > "$f.sha256" ;; esac; done)
git add -A && git commit -qm "base des essais de l'écart 2" && git push -q origin main || exit 2
E_AMORCE=$(sha256sum "$A" | cut -d' ' -f1)
cat > "$P" <<EOF
# Préenregistrement factice des essais de l'écart 2 de P3-bis

- GO : **GO-2026-11-10-02** (\`registres/go.md\`)
- Lancement : \`GO_ID=GO-2026-11-10-02\`, \`PREREG=$P\`, \`BRANCHE=calcul/p3bis-reel-v1\` (une relance prend \`…-v2\`, puis \`…-v3\`), \`DEPOT_URL=file://$E2/distant.git\`
- Empreintes : \`$A\` (\`$E_AMORCE\`, sha256)
- Tests attendus : \`531\`
EOF
(cd prereg && sha256sum P3-bis-temoin-positif-v1.md > P3-bis-temoin-positif-v1.md.sha256)
git add -A && git commit -qm "S (essais de l'écart 2)" && git push -q origin main || exit 2
SF=$(git rev-parse HEAD); echo "commit de scellement factice : $SF"
cd "$R" || exit 2
cat > "$E2/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du bout en bout de l'écart 2 : n'appelle aucun service ; journal fonction du temps écoulé depuis
# la création (scénario « secondes<TAB>ligne » copié à la création ; __COMMIT__ et __BRANCHE__ remplacés)
ET=${E2E_ETAT:?}
echo "$(date -u +%s) $*" >> "$ET/appels.txt"
case "$1 $2" in
  "search offers") printf '%s\n' '[{"id": 111, "machine_id": 7101, "host_id": 8101, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 257000, "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.989, "dph_total": 1.10, "inet_down_cost": 0.026, "storage_total_cost": 0.05}]' ;;
  "show user") cat "$ET/user-reponse"; exit "$(cat "$ET/user-code")" ;;
  "show instances")
    l='{"id": 58936096, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936099, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936100, "actual_status": "exited", "cur_state": "stopped"}'
    for d in "$ET"/instance-*; do [ -d "$d" ] || continue; [ -e "$d/detruite" ] && continue
        l="$l, {\"id\": ${d##*-}, \"actual_status\": \"$( [ -e "$d/arretee" ] && echo exited || echo running)\", \"cur_state\": \"$( [ -e "$d/arretee" ] && echo stopped || echo running)\", \"dph_total\": 1.1}"; done
    echo "[$l]" ;;
  "create instance")
    a=("$@"); br=""; commit=""; lab=""
    for ((i = 0; i < ${#a[@]}; i++)); do
      [ "${a[$i]}" = "--label" ] && lab=${a[$((i + 1))]}
      [ "${a[$i]}" = "--env" ] && for kv in ${a[$((i + 1))]}; do case "$kv" in BRANCHE=*) br=${kv#BRANCHE=} ;; COMMIT=*) commit=${kv#COMMIT=} ;; esac; done
    done
    k=$(( $(cat "$ET/compteur") + 1 )); echo "$k" > "$ET/compteur"; id=7777777$k; d="$ET/instance-$id"; mkdir -p "$d"
    printf '%s\n' "$br" > "$d/branche"; printf '%s\n' "$commit" > "$d/commit"; printf '%s\n' "$lab" > "$d/etiquette"
    date -u +%s > "$d/creation"; cp "$ET/scenario.tsv" "$d/lignes.tsv"
    echo "{\"success\": true, \"new_contract\": $id}" ;;
  "show instance")
    d="$ET/instance-$3"; [ -d "$d" ] || { echo "instance inconnue"; exit 1; }
    st=running; cs=running; [ -e "$d/arretee" ] && { st=exited; cs=stopped; }
    echo "{\"actual_status\": \"$st\", \"cur_state\": \"$cs\", \"intended_status\": \"running\", \"status_msg\": \"essai\", \"dph_total\": 1.1, \"machine_id\": 7101, \"host_id\": 8101, \"gpu_name\": \"A100 SXM4\", \"label\": \"$(cat "$d/etiquette")\", \"inet_down_billed\": 6564085.76, \"inet_down_cost\": 0.026, \"inet_up_billed\": 289792, \"inet_up_cost\": 0.04}" ;;
  "logs "*)
    d="$ET/instance-$2"; [ -d "$d" ] || exit 1
    el=$(( $(date -u +%s) - $(cat "$d/creation") ))
    awk -F'\t' -v e="$el" '$1 <= e {print $2}' "$d/lignes.tsv" | sed -e "s/__COMMIT__/$(cat "$d/commit")/" -e "s|__BRANCHE__|$(cat "$d/branche")|" ;;
  "stop instance") [ -d "$ET/instance-$3" ] && touch "$ET/instance-$3/arretee" && echo '{"success": true}' ;;
  "destroy instance") [ -d "$ET/instance-$3" ] && touch "$ET/instance-$3/detruite" && echo '{"success": true}' ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E2/bin/vastai"
printf '%s\n' '{"credit": 6.0}' > "$E2/etat/user-reponse"; echo 0 > "$E2/etat/user-code"; echo 0 > "$E2/etat/compteur"
J_E2E=(HF_TOKEN=factice-hf-8888888 CONTROLE_IA_GITHUB_TOKEN_2=factice-g2-1212121)
scenario_e2e() {   # « secondes|ligne » …
    : > "$E2/etat/scenario.tsv"; for x in "$@"; do printf '%s\t%s\n' "${x%%|*}" "${x#*|}" >> "$E2/etat/scenario.tsv"; done
}
E_SAIN=("40|AMORCE 2026-11-12T15:01:20Z : commit __COMMIT__" "224|2026-11-12T15:04:25Z début : ETUDE=p3bis MODE=reel COMMIT=__COMMIT__ BRANCHE=__BRANCHE__"
        "410|2026-11-12T15:07:31Z préenregistrement lu : 531 tests attendus ; configuration prereg/P3-bis-temoin-positif-config-v1.json"
        "425|2026-11-12T15:07:46Z branche __BRANCHE__ poussée avant l'installation (droit d'écriture éprouvé)"
        "426|NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB" "1200|PROGRES 2026-11-12T15:20:41Z etape=entrainement concept=tromperie aire_validation=1.0"
        "2900|2026-11-12T15:49:01Z run : processus 4242 fini, code 0" "3000|AMORCE 2026-11-12T15:50:41Z : fin, code 0")
ench() {   # $1 nom, $2 code attendu, $3 horloge (simulee|reelle), $4 dépense antérieure ; enchaîneur v5 détaché de l'outil (ici : premier plan)
    local n=$1 att=$2 h=$3 an=${4:-0.53} c v hv=()
    if [ "$h" = simulee ]; then date -u +%s > "$E2/horloge-$n"; hv=(HORLOGE="$E2/horloge-$n"); fi
    : > "$E2/etat/appels.txt"
    env -i PATH="$E2/bin:/usr/bin:/bin" HOME="$E2/home" LANG=C.UTF-8 E2E_ETAT="$E2/etat" "${hv[@]}" "${J_E2E[@]}" INTERVALLE="${INTERV:-120}" \
        bash "$E2/H/enchaineur_p3bis_v5.sh" "$SF" "$E2/d-$n" - 1 "$an" > "$E2/console-$n.txt" 2>&1; c=$?
    cp "$E2/etat/appels.txt" "$E2/appels-$n.txt"
    v=0; [ "$c" = "$att" ] || v=1
    grep -rqE "$JETONS_RE" "$E2/console-$n.txt" "$E2/d-$n" 2>/dev/null && v=1
    grep -q 'destroy' "$E2/appels-$n.txt" && v=1
    res "$n" "$v" "enchaîneur v5 : code $c (attendu $att) ; aucune destruction ; aucun jeton écrit"
    grep -v '^$' "$E2/console-$n.txt" | tail -1 | cut -c1-170 | sed 's/^/    | /'
}
scenario_e2e "${E_SAIN[@]}"
ench E3-01-sain-horloge-simulee 0 simulee 0.53
D=$E2/d-E3-01-sain-horloge-simulee
res E3-01b "$( grep -q 'jeton : CONTROLE_IA_GITHUB_TOKEN exporté depuis CONTROLE_IA_GITHUB_TOKEN_2' "$D/enchaineur.txt" && grep -q 'lanceur : code 0' "$D/enchaineur.txt" && grep -q 'contrôle à cinq minutes : code 0 ; dernière ligne : CONTRÔLE À CINQ MINUTES : CONFORME' "$D/enchaineur.txt" && grep -q 'surveillance : code 0 ; dernière ligne : FIN : AMORCE' "$D/enchaineur.txt" && grep -q 'ENCHAÎNEUR : fin ; lanceur 0 ; contrôle à cinq minutes 0 ; surveillance 0' "$D/enchaineur.txt"; echo $?)" \
    "journal : jeton exporté depuis _2 (nom seul), codes du lanceur (0), du contrôle (0, conforme), de la surveillance (0, FIN), ligne de fin"
res E3-01c "$( o=$(sed -n 's/.*contrôle à cinq minutes : appel (création + \([0-9]*\) s).*/\1/p' "$D/enchaineur.txt"); [ "$o" -ge 181 ] && [ "$o" -lt 186 ] && [ "$(dernier_off "$D/cinq-minutes")" -ge 426 ] && [ "$(dernier_off "$D/cinq-minutes")" -lt 460 ]; echo $?)" \
    "contrôle appelé à la création + 181 à 185 s ; conforme au premier relevé après les lignes de + 426 s"
res E3-01d "$( grep -q 'antérieure 0.53 ; calcul .* téléchargement 0.19, descente 6.72 Go, montée 0.30 Go' "$D/surveillance/depenses.txt" && [ "$(grep -c ' stop instance 77777771$' "$E2/appels-E3-01-sain-horloge-simulee.txt")" = 1 ] && [ "$(grep -c ' create instance ' "$E2/appels-E3-01-sain-horloge-simulee.txt")" = 1 ]; echo $?)" \
    "surveillance d'écart : dépense antérieure passée (0,53), téléchargement de la fille compté 0,19 USD, aucun arrêt pour la dépense ; une création, un arrêt par l'identifiant (fin normale)"
res E3-01e "$( awk '{print $1}' "$E2/appels-E3-01-sain-horloge-simulee.txt" | sort -c -n; echo $?)" "appels à l'outil dans l'ordre du temps simulé (création, contrôle, surveillance)"
detruites() {   # destruction SIMULÉE entre deux cas (geste de la session après la fin, jamais de la chaîne) : le compte factice redevient propre
    for d in "$E2/etat"/instance-*; do [ -d "$d" ] && touch "$d/detruite"; done
}
detruites
scenario_e2e "40|AMORCE 2026-11-12T15:01:20Z : commit __COMMIT__" "250|AMORCE : clonage impossible (jeton GitHub ?)"
ench E3-02-echec-amorce 0 simulee
D=$E2/d-E3-02-echec-amorce
res E3-02b "$( grep -q 'contrôle à cinq minutes : code 1' "$D/enchaineur.txt" && grep -q 'surveillance : code 0 ; dernière ligne : ÉCHEC D.AMORCE' "$D/enchaineur.txt" && [ "$(dernier_off "$D/cinq-minutes")" -ge 250 ] && [ "$(dernier_off "$D/cinq-minutes")" -lt 290 ]; echo $?)" \
    "échec d'amorce à + 250 s : contrôle en code 1 au relevé suivant, la surveillance suit quand même (R-2393) et arrête par l'identifiant"
detruites
printf '%s\n' '{"credit": 0}' > "$E2/etat/user-reponse"; scenario_e2e "${E_SAIN[@]}"
ench E3-03-lanceur-code-3 3 simulee
D=$E2/d-E3-03-lanceur-code-3
res E3-03b "$( [ ! -e "$D/cinq-minutes" ] && [ ! -e "$D/surveillance" ] && ! grep -q ' create instance ' "$E2/appels-E3-03-lanceur-code-3.txt" && grep -q 'ENCHAÎNEUR : fin sans contrôle ni surveillance (lanceur, code 3)' "$D/enchaineur.txt"; echo $?)" \
    "lanceur en code 3 (crédit nul) : aucune création, ni contrôle ni surveillance, fin écrite"
printf '%s\n' '{"credit": 6.0}' > "$E2/etat/user-reponse"
cp "$E2/H/controle_cinq_minutes_p3bis_v2_ecart2_v1.sh" "$E2/cinq-de-cote.sh"; echo "# ajout" >> "$E2/H/controle_cinq_minutes_p3bis_v2_ecart2_v1.sh"
ench E3-04-piece-modifiee 2 simulee
res E3-04b "$( [ ! -e "$E2/d-E3-04-piece-modifiee" ] && [ ! -s "$E2/appels-E3-04-piece-modifiee.txt" ] && grep -q "d'empreinte autre que l'épinglée" "$E2/console-E3-04-piece-modifiee.txt"; echo $?)" \
    "contrôle d'écart modifié : refus avant tout appel (aucun dossier, aucun appel à l'outil)"
cp "$E2/cinq-de-cote.sh" "$E2/H/controle_cinq_minutes_p3bis_v2_ecart2_v1.sh"
c=0; env -i PATH="$E2/bin:/usr/bin:/bin" HOME="$E2/home" LANG=C.UTF-8 E2E_ETAT="$E2/etat" bash "$E2/H/enchaineur_p3bis_v5.sh" "$SF" "$E2/d-E3-05" - 1 dix > "$E2/console-E3-05.txt" 2>&1 || c=$?
res E3-05-depense-anterieure-illisible "$( [ "$c" = 2 ] && [ ! -e "$E2/d-E3-05" ]; echo $?)" "dépense antérieure illisible : code 2, rien de créé"
mkdir -p "$E2/d-E3-06"; c=0; env -i PATH="$E2/bin:/usr/bin:/bin" HOME="$E2/home" LANG=C.UTF-8 E2E_ETAT="$E2/etat" bash "$E2/H/enchaineur_p3bis_v5.sh" "$SF" "$E2/d-E3-06" - 1 0 > "$E2/console-E3-06.txt" 2>&1 || c=$?
res E3-06-dossier-existant "$( [ "$c" = 2 ] && grep -q 'existe déjà (R12)' "$E2/console-E3-06.txt"; echo $?)" "dossier existant : code 2 (R12)"
echo "E3-07 (horloge réelle, ≈ 3 min 30 s) : début $(date -u +%FT%TZ)"
scenario_e2e "0|AMORCE 2026-11-12T15:01:20Z : commit __COMMIT__" "0|2026-11-12T15:04:25Z début : ETUDE=p3bis MODE=reel COMMIT=__COMMIT__ BRANCHE=__BRANCHE__" \
    "0|2026-11-12T15:07:31Z préenregistrement lu : 531 tests attendus ; configuration prereg/P3-bis-temoin-positif-config-v1.json" \
    "0|2026-11-12T15:07:46Z branche __BRANCHE__ poussée avant l'installation (droit d'écriture éprouvé)" "0|NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB" \
    "200|2026-11-12T15:49:01Z run : processus 4242 fini, code 0" "205|AMORCE 2026-11-12T15:50:41Z : fin, code 0"
INTERV=2 ench E3-07-sain-horloge-reelle 0 reelle 0
D=$E2/d-E3-07-sain-horloge-reelle
res E3-07b "$( grep -q 'contrôle à cinq minutes : code 0' "$D/enchaineur.txt" && grep -q 'surveillance : code 0 ; dernière ligne : FIN : AMORCE' "$D/enchaineur.txt" && o=$(sed -n 's/.*contrôle à cinq minutes : appel (création + \([0-9]*\) s).*/\1/p' "$D/enchaineur.txt") && [ "$o" -ge 181 ] && [ "$o" -lt 190 ]; echo $?)" \
    "horloge réelle : contrôle appelé à la création + $(sed -n 's/.*contrôle à cinq minutes : appel (création + \([0-9]*\) s).*/\1/p' "$D/enchaineur.txt") s, conforme ; surveillance jusqu'à FIN"
echo "E3-07 : fin $(date -u +%FT%TZ)"
# =================================================================================================== R : bancs existants
echo "=== R : bancs existants rejoués ==="
c=0; (cd "$SRC" && PYTHONPATH=src "$PYT" -m pytest -q -p no:cacheprovider "$VERS/essais_verifications_p3bis_v2.py") > "$R/banc-module-origine.txt" 2>&1 || c=$?
res R-01-banc-module-origine "$( [ "$c" = 0 ] && grep -qE '^147 passed' "$R/banc-module-origine.txt"; echo $?)" "banc du module commun sur le module d'origine : $(grep -E 'passed|failed' "$R/banc-module-origine.txt" | tail -1 | sed 's/ in [0-9.]*s//') (canonique : 147 passed)"
mkdir -p "$R/banc-module-ecart"
sed -e "s|^ICI = Path(__file__).resolve().parent$|ICI = Path(\"$ICI\")|" -e 's|^MODULE = ICI / "verifications_p3bis_v2.py"$|MODULE = ICI / "verifications_p3bis_v2_ecart2_v1.py"|' \
    "$ICI/essais_verifications_p3bis_v2.py" > "$R/banc-module-ecart/essais_module_ecart2.py"
n=$(diff "$ICI/essais_verifications_p3bis_v2.py" "$R/banc-module-ecart/essais_module_ecart2.py" | grep -c '^>'); echo "lignes changées dans la copie re-pointée du banc du module : $n (ICI, MODULE)"
c=0; (cd "$R/banc-module-ecart" && PYTHONPATH="$SRC/src" "$PYT" -m pytest -q -p no:cacheprovider -rf essais_module_ecart2.py) > "$R/banc-module-ecart.txt" 2>&1 || c=$?
res R-02-banc-module-repointe "$( [ "$n" = 2 ] && grep -qE '^1 failed, 146 passed' "$R/banc-module-ecart.txt" && [ "$(grep -c '^FAILED ' "$R/banc-module-ecart.txt")" = 1 ] && grep -q '^FAILED essais_module_ecart2.py::test_depense_sain_sous_plafond' "$R/banc-module-ecart.txt"; echo $?)" \
    "banc du module re-pointé sur le module d'écart : $(grep -E 'passed|failed' "$R/banc-module-ecart.txt" | tail -1 | sed 's/ in [0-9.]*s//') ; seul échec attendu : test_depense_sain_sous_plafond (il encode l'ancienne unité : 20 × 0,026 = 0,52 USD)"
grep -E '^E +(AssertionError|assert)' "$R/banc-module-ecart.txt" | head -2 | cut -c1-200 | sed 's/^/    | /'
c=0; bash "$ICI/essais_surveillance_p3bis_v2.sh" "$R/banc-surv-origine" > "$R/banc-surv-origine.log" 2>&1 || c=$?
res R-03-banc-surveillance-origine "$( [ "$c" = 0 ] && diff <(grep -v '^    | ' "$ICI/banc-surveillance-p3bis-v2.log") <(grep -v '^    | ' "$R/banc-surv-origine.log") > /dev/null; echo $?)" \
    "banc de la surveillance d'origine rejoué : lignes de verdict égales au journal canonique (seules diffèrent les lignes citées « | », secondes et chemins)"
sed -e "s|^ICI=\$(dirname \"\$(realpath \"\$0\")\")$|ICI=$ICI|" -e 's|^SURV=\$ICI/surveiller_p3bis_v2.sh$|SURV=$ICI/surveiller_p3bis_v2_ecart2_v1.sh|' "$ICI/essais_surveillance_p3bis_v2.sh" > "$R/banc-surv-ecart.sh"
n=$(diff "$ICI/essais_surveillance_p3bis_v2.sh" "$R/banc-surv-ecart.sh" | grep -c '^>'); echo "lignes changées dans la copie re-pointée du banc de la surveillance : $n (ICI, SURV)"
c=0; bash "$R/banc-surv-ecart.sh" "$R/banc-surv-ecart" > "$R/banc-surv-ecart.log" 2>&1 || c=$?
res R-04-banc-surveillance-repointe "$( [ "$n" = 2 ] && [ "$c" = 0 ] && tail -1 "$R/banc-surv-ecart.log" | grep -qx 'FIN DU BANC DE LA SURVEILLANCE DE P3-BIS ; cas non conformes : 0' && diff <(grep -v -e '^    | ' -e '^script éprouvé : ' "$ICI/banc-surveillance-p3bis-v2.log") <(grep -v -e '^    | ' -e '^script éprouvé : ' "$R/banc-surv-ecart.log") > /dev/null; echo $?)" \
    "banc de la surveillance re-pointé sur la surveillance d'écart : 0 non conforme, lignes de verdict égales au canonique (hors lignes « script éprouvé », qui nomment la copie re-pointée)"
for f in verifications_p3bis_v2.py controle_cinq_minutes_p3bis_v2.sh surveiller_p3bis_v2.sh "$LO" essais_verifications_p3bis_v2.py essais_surveillance_p3bis_v2.sh banc-surveillance-p3bis-v2.log banc-verifications-p3bis-v2.log; do
    res "R-05-origine-egal-a-S-$f" "$( [ "$(git -C "$SRC" show "$SCELLE:$VERS/$f" | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$ICI/$f" | cut -d' ' -f1)" ]; echo $?)" "$f du dossier égal à sa copie versée à S"
done
res R-06-lanceur-ecart1 "$( [ "$(sha256sum "$ICI/$LE" | cut -d' ' -f1)" = 2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb ] && grep -q '^LANCEUR=lancer_p3bis_v2_ecart1_v2.sh;             E_LANCEUR=2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb$' "$ENCH"; echo $?)" \
    "lanceur d'écart 1 v2 inchangé (2e294e5a…), épinglé tel quel par l'enchaîneur v5"
res R-07-epingles-v5 "$( for p in controle_cinq_minutes_p3bis_v2_ecart2_v1.sh=E_CINQ surveiller_p3bis_v2_ecart2_v1.sh=E_SURV verifications_p3bis_v2_ecart2_v1.py=E_MODULE; do grep -q "E_${p#*=E_}=$(sha256sum "$ICI/${p%%=*}" | cut -d' ' -f1)\$" "$ENCH" || exit 1; done; echo 0)" \
    "empreintes épinglées dans l'enchaîneur v5 égales aux pièces d'écart du dossier"
echo "cas joués : $NCAS"
echo "fin des essais : $(date -u +%FT%TZ)"
if [ "$NC" = 0 ]; then echo "ESSAIS DE L'ÉCART 2 DE P3-BIS : CONFORMES"; else echo "ESSAIS DE L'ÉCART 2 DE P3-BIS : $NC NON CONFORME(S)"; exit 1; fi
