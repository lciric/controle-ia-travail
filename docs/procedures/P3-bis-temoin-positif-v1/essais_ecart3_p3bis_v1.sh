#!/usr/bin/env bash
# Essais R5 de l'écart 3 de P3-bis (R-2492 ; consigne `consigne-developpeur-p3bis-ecart3-v1.md`, `09311f1c…`), v1, écrits
# le 2026-11-13 vers 08:05 UTC (heure relevée par `date -u`). Bac à sable seulement : FAUX outil de location (aucun service
# appelé, aucune dépense), HORLOGE SIMULÉE (faux `date` et `sleep` sur le PATH des scripts joués : le temps n'avance que
# par `sleep`), dépôt synthétique et dépôt nu local (comme les essais des écarts 1 et 2), registre des GO temporaire
# (en-tête et ligne GO-2026-11-10-02 recopiés de main, plus une ligne de calcul fabriquée pour une autre course,
# GO-2026-11-08-13, comme le banc du lanceur d'origine), contrôles avant dépense : BOUCHON.
# Sections :
#   V   forme de l'enchaîneur v6 : seules trois lignes hors commentaires diffèrent de v5 ; épingles égales aux pièces ;
#   E   enchaîneur v6 de bout en bout sur appelants factices : cas sain (tentative N = 2, branche v1 présente au distant,
#       crédit au-dessus du minimum) ; seuil au centime ; crédit sous le minimum, dont le crédit de la création de
#       60432755 (7,05 USD, R-2491) et le solde du 13 novembre (0 ; −0,93) ; instance nommée en marche ; instance
#       d'autrui arrêtée ; outil en échec ; crédit illisible ; lanceur d'origine modifié ou absent (refus de v6, et refus
#       du lanceur lui-même si l'épingle de v6 était contournée) ; tentative N = 2 sans la branche v1 au distant ; branche
#       v2 déjà présente ; N = 1 ; échec d'amorce ; pièce d'écart 2 modifiée ; arguments ; TÉMOIN : l'enchaîneur v5
#       (lanceur d'écart 1) crée à 7,05 USD ;
#   R   bancs existants rejoués : banc du lanceur d'origine (verdicts égaux au journal canonique de S) ; banc de l'écart 2
#       (verdicts égaux au journal versé) ; originaux égaux à S ; pièces des écarts 1 et 2 et enchaîneur v5 inchangés.
# Usage : essais_ecart3_p3bis_v1.sh RACINE_NEUVE INTERPRETEUR_AVEC_PYTEST
set -uo pipefail
R=$(realpath -m "${1:?racine neuve}"); PYT=${2:?interpréteur Python avec pytest}
SOI=$(realpath "$0"); ICI=$(dirname "$SOI"); SRC=$(realpath "$ICI/../../..")
SCELLE=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0          # S (commit de scellement de P3-bis)
VERS=docs/procedures/P3-bis-temoin-positif-v1
ENCH6=$ICI/enchaineur_p3bis_v6.sh; ENCH5=$ICI/enchaineur_p3bis_v5.sh
LO=lancer_p3bis_v2.sh; LE=lancer_p3bis_v2_ecart1_v2.sh
E_LO=029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08
export PYTHONDONTWRITEBYTECODE=1
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" || exit 2
echo "début des essais : $(date -u +%FT%TZ)"
for f in "$ENCH6" "$ICI/$LO" "$ENCH5" "$ICI/$LE" "$ICI/controle_cinq_minutes_p3bis_v2_ecart2_v1.sh" "$ICI/surveiller_p3bis_v2_ecart2_v1.sh" \
         "$ICI/verifications_p3bis_v2_ecart2_v1.py" "$ICI/verifications_p3bis_v2.py" "$SOI"; do
    echo "script joué : $(basename "$f") $(sha256sum "$f" | cut -d' ' -f1)"
done
NC=0; NCAS=0
JETONS_RE='factice-hf-3333333|factice-g2-3434343'
res() {   # $1 nom, $2 0 si conforme, $3 description
    NCAS=$((NCAS + 1))
    if [ "$2" = 0 ]; then echo "$1 : $3 : CONFORME"; else echo "$1 : $3 : NON CONFORME"; NC=$((NC + 1)); fi
}
# =================================================================================================== V : forme de v6
echo "=== V : forme de l'enchaîneur v6 ==="
DIFF56=$(diff <(grep -v '^ *#' "$ENCH5") <(grep -v '^ *#' "$ENCH6"))
res V-01-trois-lignes "$( [ "$(printf '%s\n' "$DIFF56" | grep -c '^>')" = 3 ] && [ "$(printf '%s\n' "$DIFF56" | grep -c '^<')" = 3 ] \
    && printf '%s\n' "$DIFF56" | grep -qx "> LANCEUR=lancer_p3bis_v2.sh;                       E_LANCEUR=$E_LO" \
    && printf '%s\n' "$DIFF56" | grep -q '^> \[ \$# -eq 5 \].*usage : enchaineur_p3bis_v6.sh S DOSSIER_NEUF' \
    && printf '%s\n' "$DIFF56" | grep -q '^> note "enchaîneur p3bis v6 '; echo $?)" \
    "hors commentaires, v6 ne diffère de v5 que par trois lignes : épingle du lanceur (lanceur d'origine, $E_LO), usage, étiquette du journal"
printf '%s\n' "$DIFF56" | sed 's/^/    | /' | cut -c1-170
res V-02-epingle-lanceur-origine "$( [ "$(sha256sum "$ICI/$LO" | cut -d' ' -f1)" = "$E_LO" ] && [ "$(git -C "$SRC" show "$SCELLE:$VERS/$LO" | sha256sum | cut -d' ' -f1)" = "$E_LO" ]; echo $?)" \
    "épingle du lanceur de v6 égale au lanceur d'origine du dossier et à sa copie versée à S"
res V-03-epingles-ecart2 "$( for v in E_CINQ E_SURV E_MODULE; do [ "$(grep "^[A-Z]*=.*; *$v=" "$ENCH5")" = "$(grep "^[A-Z]*=.*; *$v=" "$ENCH6")" ] || exit 1; done
    for p in controle_cinq_minutes_p3bis_v2_ecart2_v1.sh=E_CINQ surveiller_p3bis_v2_ecart2_v1.sh=E_SURV verifications_p3bis_v2_ecart2_v1.py=E_MODULE; do
        grep -q "${p#*=}=$(sha256sum "$ICI/${p%%=*}" | cut -d' ' -f1)\$" "$ENCH6" || exit 1; done; echo 0)" \
    "épingles du contrôle, de la surveillance et du module d'écart 2 : lignes égales à v5, égales aux pièces du dossier"
# =================================================================================================== E : bout en bout
echo "=== E : enchaîneur v6, de bout en bout sur appelants factices ==="
E2=$R/e2e; mkdir -p "$E2/bin" "$E2/H" "$E2/home" "$E2/etat" || exit 2
cat > "$E2/bin/date" <<'EOF'
#!/usr/bin/env bash
# faux date des essais de l'écart 3 : heure de l'horloge simulée $HORLOGE si elle existe, sinon heure réelle
if [ -n "${HORLOGE:-}" ] && [ -f "$HORLOGE" ]; then exec /usr/bin/date -d "@$(cat "$HORLOGE")" "$@"; fi
exec /usr/bin/date "$@"
EOF
cat > "$E2/bin/sleep" <<'EOF'
#!/usr/bin/env bash
# faux sleep des essais de l'écart 3 : avance l'horloge simulée sans attendre ; sans horloge, vrai sleep
if [ -n "${HORLOGE:-}" ] && [ -f "$HORLOGE" ]; then n=${1%%.*}; echo $(( $(cat "$HORLOGE") + n )) > "$HORLOGE"; exit 0; fi
exec /usr/bin/sleep "$@"
EOF
chmod +x "$E2/bin/date" "$E2/bin/sleep"
for s in "$LO" "$LE"; do
    sed -e "s|^DEPOT=.*|DEPOT=$E2/depot|" -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$E2/distant.git|" -e "s|^INTERVALLE_OFFRE_S=.*|INTERVALLE_OFFRE_S=0|" "$ICI/$s" > "$E2/H/$s"
    n=$(diff "$ICI/$s" "$E2/H/$s" | grep -c '^>'); echo "lignes changées dans la copie jouée de $s : $n (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S)"
    [ "$n" = 3 ] || { echo "copie de $s non sûre"; exit 2; }
done
for s in verifications_p3bis_v2.py controle_cinq_minutes_p3bis_v2.sh surveiller_p3bis_v2.sh detruire_p3bis_v2.sh \
         verifications_p3bis_v2_ecart2_v1.py controle_cinq_minutes_p3bis_v2_ecart2_v1.sh surveiller_p3bis_v2_ecart2_v1.sh; do cp "$ICI/$s" "$E2/H/"; done
EL_O=$(sha256sum "$E2/H/$LO" | cut -d' ' -f1); EL_E=$(sha256sum "$E2/H/$LE" | cut -d' ' -f1)
sed "s|^LANCEUR=lancer_p3bis_v2.sh;                       E_LANCEUR=.*|LANCEUR=lancer_p3bis_v2.sh;                       E_LANCEUR=$EL_O|" "$ENCH6" > "$E2/H/enchaineur_p3bis_v6.sh"
n=$(diff "$ENCH6" "$E2/H/enchaineur_p3bis_v6.sh" | grep -c '^>'); echo "lignes changées dans la copie jouée de l'enchaîneur v6 : $n (empreinte épinglée du lanceur d'origine : celle de sa copie jouée)"
[ "$n" = 1 ] || { echo "copie de l'enchaîneur v6 non sûre"; exit 2; }
sed "s|^LANCEUR=lancer_p3bis_v2_ecart1_v2.sh;             E_LANCEUR=.*|LANCEUR=lancer_p3bis_v2_ecart1_v2.sh;             E_LANCEUR=$EL_E|" "$ENCH5" > "$E2/H/enchaineur_p3bis_v5.sh"
n=$(diff "$ENCH5" "$E2/H/enchaineur_p3bis_v5.sh" | grep -c '^>'); echo "lignes changées dans la copie jouée de l'enchaîneur v5 (témoin) : $n (empreinte épinglée du lanceur d'écart 1 : celle de sa copie jouée)"
[ "$n" = 1 ] || { echo "copie de l'enchaîneur v5 non sûre"; exit 2; }
cat > "$E2/H/controles_avant_depense_p3bis_v2.sh" <<'EOF'
#!/usr/bin/env bash
# bouchon des essais de l'écart 3 : les contrôles réels sont joués par leur banc et par la répétition finale
mkdir -p "$2" "$2.travail"; echo "OK  bouchon des essais de l'écart 3 (S=${1:0:12}, branche $3)"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
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
{ git -C "$SRC" show main:registres/go.md | sed -n '1,10p'; git -C "$SRC" show main:registres/go.md | grep '^| GO-2026-11-10-02 |'
  echo "| GO-2026-11-08-13 | 2026-11-08 | calcul | autre course du programme (essai) | 50 USD | 2026-11-30 | Lazar | essai |"; } > registres/go.md
[ "$(grep -c '^| GO-2026-11-10-02 |' registres/go.md)" = 1 ] || { echo "ligne GO-2026-11-10-02 absente de main"; exit 2; }
for s in "$LO" $CHAINE; do cp "$E2/H/$s" "$VERS/$s"; done
python3 -I -B - "$E2/H/verifications_p3bis_v2.py" "$E2/H" "$VERS" <<'EOF' || exit 2
import hashlib, importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
h, sortie = Path(sys.argv[2]), Path(sys.argv[3])
for nom, (verdict, scripts) in v.JOURNAUX.items():
    lignes = [f"script éprouvé : {s} {hashlib.sha256((h / s).read_bytes()).hexdigest()}" for s in sorted(scripts)]
    (sortie / nom).write_text("\n".join(lignes) + "\njournal factice des essais de l'écart 3\n" + verdict + "\n", encoding="utf-8")
EOF
(cd "$VERS" && for f in *; do case "$f" in *.sha256) ;; *) sha256sum "$f" > "$f.sha256" ;; esac; done)
git add -A && git commit -qm "base des essais de l'écart 3" && git push -q origin main || exit 2
E_AMORCE=$(sha256sum "$A" | cut -d' ' -f1)
cat > "$P" <<EOF
# Préenregistrement factice des essais de l'écart 3 de P3-bis

- GO : **GO-2026-11-10-02** (\`registres/go.md\`)
- Lancement : \`GO_ID=GO-2026-11-10-02\`, \`PREREG=$P\`, \`BRANCHE=calcul/p3bis-reel-v1\` (une relance prend \`…-v2\`, puis \`…-v3\`), \`DEPOT_URL=file://$E2/distant.git\`
- Empreintes : \`$A\` (\`$E_AMORCE\`, sha256)
- Tests attendus : \`531\`
EOF
(cd prereg && sha256sum P3-bis-temoin-positif-v1.md > P3-bis-temoin-positif-v1.md.sha256)
git add -A && git commit -qm "S (essais de l'écart 3)" && git push -q origin main || exit 2
SF=$(git rev-parse HEAD); echo "commit de scellement factice : $SF"
# état du distant au 13 novembre (R-2489, R-2490) : calcul/p3bis-reel-v1 poussée par la tentative 1, restée égale à S
git push -q origin "$SF:refs/heads/calcul/p3bis-reel-v1" || exit 2
echo "branche factice calcul/p3bis-reel-v1 poussée au distant, égale à S (comme au 13 novembre : R-2490)"
cd "$R" || exit 2
cat > "$E2/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du bout en bout de l'écart 3 (celui de l'écart 2, plus des instances d'autrui dans
# $E2E_ETAT/autres.json) : n'appelle aucun service ; journal fonction du temps écoulé depuis la création
ET=${E2E_ETAT:?}
echo "$(date -u +%s) $*" >> "$ET/appels.txt"
case "$1 $2" in
  "search offers") printf '%s\n' '[{"id": 111, "machine_id": 7101, "host_id": 8101, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 257000, "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.989, "dph_total": 1.10, "inet_down_cost": 0.026, "storage_total_cost": 0.05}]' ;;
  "show user") cat "$ET/user-reponse"; exit "$(cat "$ET/user-code")" ;;
  "show instances")
    l='{"id": 58936096, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936099, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936100, "actual_status": "exited", "cur_state": "stopped"}'
    [ -s "$ET/autres.json" ] && l="$l, $(cat "$ET/autres.json")"
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
    printf 'creation %s branche %s etiquette %s\n' "$id" "$br" "$lab" >> "$ET/creations.txt"
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
echo 0 > "$E2/etat/compteur"; : > "$E2/etat/autres.json"; : > "$E2/etat/creations.txt"
credit() { printf '%s\n' "$1" > "$E2/etat/user-reponse"; echo "${2:-0}" > "$E2/etat/user-code"; }
credit '{"credit": 50.0}'
J_E2E=(HF_TOKEN=factice-hf-3333333 CONTROLE_IA_GITHUB_TOKEN_2=factice-g2-3434343)
scenario_e2e() {   # « secondes|ligne » …
    : > "$E2/etat/scenario.tsv"; for x in "$@"; do printf '%s\t%s\n' "${x%%|*}" "${x#*|}" >> "$E2/etat/scenario.tsv"; done
}
E_SAIN=("40|AMORCE 2026-11-13T15:01:20Z : commit __COMMIT__" "224|2026-11-13T15:04:25Z début : ETUDE=p3bis MODE=reel COMMIT=__COMMIT__ BRANCHE=__BRANCHE__"
        "410|2026-11-13T15:07:31Z préenregistrement lu : 531 tests attendus ; configuration prereg/P3-bis-temoin-positif-config-v1.json"
        "425|2026-11-13T15:07:46Z branche __BRANCHE__ poussée avant l'installation (droit d'écriture éprouvé)"
        "426|NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB" "1200|PROGRES 2026-11-13T15:20:41Z etape=entrainement concept=tromperie aire_validation=1.0"
        "2900|2026-11-13T15:49:01Z run : processus 4242 fini, code 0" "3000|AMORCE 2026-11-13T15:50:41Z : fin, code 0")
dernier_off() { sed -n 's/.*création + \([0-9]*\) s.*/\1/p' "$1/releves.txt" | tail -1; }
ench() {   # $1 nom, $2 code attendu, $3 N, $4 EN_MARCHE, $5 dépense antérieure, $6 enchaîneur (fichier de $E2/H) ; horloge simulée
    local n=$1 att=$2 nn=$3 em=$4 an=$5 en=${6:-enchaineur_p3bis_v6.sh} c v
    date -u +%s > "$E2/horloge-$n"; : > "$E2/etat/appels.txt"
    env -i PATH="$E2/bin:/usr/bin:/bin" HOME="$E2/home" LANG=C.UTF-8 E2E_ETAT="$E2/etat" HORLOGE="$E2/horloge-$n" "${J_E2E[@]}" INTERVALLE=120 \
        bash "$E2/H/$en" "$SF" "$E2/d-$n" "$em" "$nn" "$an" > "$E2/console-$n.txt" 2>&1; c=$?
    cp "$E2/etat/appels.txt" "$E2/appels-$n.txt"
    v=0; [ "$c" = "$att" ] || v=1
    grep -rqE "$JETONS_RE" "$E2/console-$n.txt" "$E2/d-$n" 2>/dev/null && v=1
    grep -q 'destroy' "$E2/appels-$n.txt" && v=1
    res "$n" "$v" "$en : code $c (attendu $att) ; aucune destruction ; aucun jeton écrit"
    grep -v '^$' "$E2/console-$n.txt" | tail -1 | cut -c1-170 | sed 's/^/    | /'
}
creations() { grep -c ' create instance ' "$E2/appels-$1.txt"; }
refus() {   # $1 nom, $2 code, $3 motif de la dernière ligne du lanceur : ni création, ni contrôle, ni surveillance
    local D=$E2/d-$1
    res "$1b" "$( [ "$(creations "$1")" = 0 ] && [ ! -e "$D/cinq-minutes" ] && [ ! -e "$D/surveillance" ] \
        && grep -qF "ENCHAÎNEUR : fin sans contrôle ni surveillance (lanceur, code $2)" "$D/enchaineur.txt" \
        && grep -v '^$' "$D/console-lanceur.txt" | tail -1 | grep -qF -- "$3"; echo $?)" \
        "aucune création, ni contrôle ni surveillance ; lanceur : « ${3:0:90} »"
}
detruites() {   # destruction SIMULÉE entre deux cas (geste de la session après la fin, jamais de la chaîne)
    for d in "$E2/etat"/instance-*; do [ -d "$d" ] && touch "$d/detruite"; done
}
scenario_e2e "${E_SAIN[@]}"
# --- E6-01 : cas sain
ench E6-01-sain-relance-2 0 2 - 0.53
D=$E2/d-E6-01-sain-relance-2
res E6-01b "$( grep -q "enchaîneur p3bis v6 " "$D/enchaineur.txt" && grep -q "empreintes épinglées vérifiées : lancer_p3bis_v2.sh $EL_O ;" "$D/enchaineur.txt" \
    && grep -q 'lanceur : appel de lancer_p3bis_v2.sh$' "$D/enchaineur.txt" && grep -q 'lanceur : code 0' "$D/enchaineur.txt" \
    && grep -q 'contrôle à cinq minutes : code 0 ; dernière ligne : CONTRÔLE À CINQ MINUTES : CONFORME' "$D/enchaineur.txt" \
    && grep -q 'surveillance : code 0 ; dernière ligne : FIN : AMORCE' "$D/enchaineur.txt" \
    && grep -q 'ENCHAÎNEUR : fin ; lanceur 0 ; contrôle à cinq minutes 0 ; surveillance 0' "$D/enchaineur.txt"; echo $?)" \
    "journal : v6, épingle du lanceur d'origine vérifiée, lanceur d'origine appelé (0), contrôle d'écart 2 (0, conforme), surveillance d'écart 2 (0, FIN)"
res E6-01c "$( grep -qx 'crédit 50.00 USD ; minimum 20.00 USD (20 USD plus 10 h × 0.0000 USD/h des instances nommées en marche)' "$D/traces/lancement.txt" \
    && ! grep -q 'écart 1' "$D/traces/lancement.txt" && ! grep -q 'écart 1' "$D/console-lanceur.txt" \
    && grep -q "^lanceur p3bis v2 $EL_O ;" "$D/traces/lancement.txt" && grep -qx 'branche calcul/p3bis-reel-v2' "$D/traces/lancement.txt" \
    && grep -qx 'etiquette p3bis-v2' "$D/traces/lancement.txt" && grep -qx 'branche calcul/p3bis-reel-v2 absente du dépôt distant' "$D/traces/lancement.txt"; echo $?)" \
    "lancement.txt : garde d'origine (crédit 50,00 ≥ minimum 20,00), aucune ligne d'écart 1, lanceur exécuté = lanceur d'origine, branche calcul/p3bis-reel-v2, étiquette p3bis-v2"
res E6-01d "$( [ "$(creations E6-01-sain-relance-2)" = 1 ] && grep -q 'create instance .*-e BRANCHE=calcul/p3bis-reel-v2 ' "$E2/appels-E6-01-sain-relance-2.txt" \
    && grep -q 'create instance .*--label p3bis-v2 ' "$E2/appels-E6-01-sain-relance-2.txt" && [ "$(grep -c ' stop instance 77777771$' "$E2/appels-E6-01-sain-relance-2.txt")" = 1 ] \
    && grep -q 'antérieure 0.53 ; calcul .* téléchargement 0.19, descente 6.72 Go, montée 0.30 Go' "$D/surveillance/depenses.txt"; echo $?)" \
    "une création (BRANCHE=calcul/p3bis-reel-v2, étiquette p3bis-v2), un arrêt par l'identifiant à la fin normale ; dépense antérieure passée (0,53) ; téléchargement compté selon l'écart 2"
res E6-01e "$( o=$(sed -n 's/.*contrôle à cinq minutes : appel (création + \([0-9]*\) s).*/\1/p' "$D/enchaineur.txt"); [ "$o" -ge 181 ] && [ "$o" -lt 186 ] \
    && [ "$(dernier_off "$D/cinq-minutes")" -ge 426 ] && [ "$(dernier_off "$D/cinq-minutes")" -lt 460 ] && awk '{print $1}' "$E2/appels-E6-01-sain-relance-2.txt" | sort -c -n; echo $?)" \
    "contrôle d'écart 2 appelé à la création + 181 à 185 s, conforme au premier relevé après + 426 s ; appels dans l'ordre du temps"
detruites
# --- seuil au centime et crédit sous le minimum
credit '{"credit": 19.99}'
ench E6-02-credit-19-99 3 2 - 0.53
refus E6-02-credit-19-99 3 "crédit insuffisant : pas de création ; recharge demandée à Lazar"
res E6-02c "$( grep -qx 'crédit 19.99 USD ; minimum 20.00 USD (20 USD plus 10 h × 0.0000 USD/h des instances nommées en marche)' "$E2/d-E6-02-credit-19-99/traces/lancement.txt"; echo $?)" "ligne officielle du crédit écrite (19,99 sous 20,00)"
credit '{"credit": 20.0}'
ench E6-03-credit-20-exact 0 2 - 0.53
res E6-03b "$( [ "$(creations E6-03-credit-20-exact)" = 1 ] && grep -qx 'crédit 20.00 USD ; minimum 20.00 USD (20 USD plus 10 h × 0.0000 USD/h des instances nommées en marche)' "$E2/d-E6-03-credit-20-exact/traces/lancement.txt"; echo $?)" "crédit égal au minimum, au centime : création (cas sain du seuil)"
detruites
credit '{"credit": 7.05}'
ench E6-04-credit-7-05-creation-60432755 3 2 - 0.53
refus E6-04-credit-7-05-creation-60432755 3 "crédit insuffisant : pas de création ; recharge demandée à Lazar"
ench E6-04T-temoin-v5-ecart1-credit-7-05 0 2 - 0.53 enchaineur_p3bis_v5.sh
D=$E2/d-E6-04T-temoin-v5-ecart1-credit-7-05
res E6-04Tb "$( [ "$(creations E6-04T-temoin-v5-ecart1-credit-7-05)" = 1 ] && grep -q '^écart 1 (R-2399) : garde du crédit remplacée' "$D/traces/lancement.txt" \
    && grep -qx 'crédit 7.05 USD ; minimum 20.00 USD (20 USD plus 10 h × 0.0000 USD/h des instances nommées en marche)' "$D/traces/lancement.txt"; echo $?)" \
    "TÉMOIN (R4) : l'enchaîneur v5 et le lanceur d'écart 1 créent à 7,05 USD (crédit de la création de 60432755, R-2491), là où v6 refuse"
detruites
credit '{"credit": 0}'
ench E6-05-credit-nul 3 2 - 0.53
refus E6-05-credit-nul 3 "crédit insuffisant : pas de création ; recharge demandée à Lazar"
credit '{"credit": -0.93}'
ench E6-05c-credit-negatif 3 2 - 0.53
refus E6-05c-credit-negatif 3 "crédit insuffisant : pas de création ; recharge demandée à Lazar"
# --- instance d'une autre course nommée en marche (minimum 20 + 10 × 1,342 = 33,42 USD)
printf '%s\n' '{"id": 60999999, "actual_status": "running", "cur_state": "running", "dph_total": 1.342}' > "$E2/etat/autres.json"
credit '{"credit": 33.41}'
ench E6-06-nommee-credit-33-41 3 2 60999999:GO-2026-11-08-13 0.53
refus E6-06-nommee-credit-33-41 3 "crédit insuffisant : pas de création ; recharge demandée à Lazar"
res E6-06c "$( grep -qx 'crédit 33.41 USD ; minimum 33.42 USD (20 USD plus 10 h × 1.3420 USD/h des instances nommées en marche)' "$E2/d-E6-06-nommee-credit-33-41/traces/lancement.txt"; echo $?)" "minimum avec une instance nommée en marche à 1,342 USD/h : 33,42 USD"
credit '{"credit": 33.42}'
ench E6-07-nommee-credit-33-42 0 2 60999999:GO-2026-11-08-13 0.53
res E6-07b "$( [ "$(creations E6-07-nommee-credit-33-42)" = 1 ] && grep -q 'surveillance : code 0 ; dernière ligne : FIN : AMORCE' "$E2/d-E6-07-nommee-credit-33-42/enchaineur.txt"; echo $?)" "crédit égal au minimum avec l'instance nommée : création, chaîne jusqu'à FIN"
detruites
# --- instance d'autrui arrêtée sur le compte (cas de 60417353 au 13 novembre, R-2491) : liste fermée
printf '%s\n' '{"id": 60999999, "actual_status": "exited", "cur_state": "stopped", "dph_total": 1.342}' > "$E2/etat/autres.json"
credit '{"credit": 50.0}'
ench E6-08-instance-d-autrui-arretee 2 2 - 0.53
refus E6-08-instance-d-autrui-arretee 2 "instances : non tolérée(s), ou liste illisible"
: > "$E2/etat/autres.json"
# --- outil en échec, crédit illisible
credit '{"credit": 50.0}' 1
ench E6-09-outil-en-echec-reponse-lisible 2 2 - 0.53
refus E6-09-outil-en-echec-reponse-lisible 2 "crédit illisible (show user, code 1) : pas de création"
credit 'réponse non JSON (essai)'
ench E6-10-credit-illisible 2 2 - 0.53
refus E6-10-credit-illisible 2 "crédit illisible (show user, code 2) : pas de création"
credit '{"credit": 50.0}'
# --- lanceur d'origine modifié ou absent
cp "$E2/H/$LO" "$E2/lanceur-de-cote.sh"; echo "# ajout" >> "$E2/H/$LO"
ench E6-11-lanceur-modifie 2 2 - 0.53
res E6-11b "$( [ ! -e "$E2/d-E6-11-lanceur-modifie" ] && [ ! -s "$E2/appels-E6-11-lanceur-modifie.txt" ] && grep -q "^lancer_p3bis_v2.sh : absent ou d'empreinte autre que l'épinglée ($EL_O) : aucun appel" "$E2/console-E6-11-lanceur-modifie.txt"; echo $?)" \
    "lanceur d'origine modifié : refus de v6 avant tout appel (aucun dossier, aucun appel à l'outil)"
EM=$(sha256sum "$E2/H/$LO" | cut -d' ' -f1)
sed "s|E_LANCEUR=$EL_O|E_LANCEUR=$EM|" "$E2/H/enchaineur_p3bis_v6.sh" > "$E2/H/enchaineur_p3bis_v6_epingle_contournee.sh"
ench E6-12-epingle-contournee-lanceur-modifie 2 2 - 0.53 enchaineur_p3bis_v6_epingle_contournee.sh
refus E6-12-epingle-contournee-lanceur-modifie 2 "lancer_p3bis_v2.sh exécuté ≠ copie versée au commit S"
rm -f "$E2/H/enchaineur_p3bis_v6_epingle_contournee.sh"; cp "$E2/lanceur-de-cote.sh" "$E2/H/$LO"
mv "$E2/H/$LO" "$E2/lanceur-absent.sh"
ench E6-13-lanceur-absent 2 2 - 0.53
res E6-13b "$( [ ! -e "$E2/d-E6-13-lanceur-absent" ] && [ ! -s "$E2/appels-E6-13-lanceur-absent.txt" ]; echo $?)" "lanceur d'origine absent : refus de v6 avant tout appel"
mv "$E2/lanceur-absent.sh" "$E2/H/$LO"
res E6-13c "$( [ "$(sha256sum "$E2/H/$LO" | cut -d' ' -f1)" = "$EL_O" ]; echo $?)" "copie jouée du lanceur rétablie (empreinte d'avant les cas E6-11 à E6-13)"
# --- branches de calcul au distant
git -C "$E2/depot" push -q origin --delete calcul/p3bis-reel-v1 || exit 2
ench E6-14-relance-2-sans-branche-v1 2 2 - 0.53
refus E6-14-relance-2-sans-branche-v1 2 "relance 2 : branche calcul/p3bis-reel-v1 absente du dépôt distant (code 2) ; une relance suit une tentative"
git -C "$E2/depot" push -q origin "$SF:refs/heads/calcul/p3bis-reel-v1" || exit 2
git -C "$E2/depot" push -q origin "$SF:refs/heads/calcul/p3bis-reel-v2" || exit 2
ench E6-15-branche-v2-deja-presente 2 2 - 0.53
refus E6-15-branche-v2-deja-presente 2 "branche calcul/p3bis-reel-v2 : git ls-remote, code 0 (2 attendu : absente du dépôt distant)"
git -C "$E2/depot" push -q origin --delete calcul/p3bis-reel-v2 || exit 2
ench E6-16-tentative-1-branche-v1-presente 2 1 - 0.53
refus E6-16-tentative-1-branche-v1-presente 2 "branche calcul/p3bis-reel-v1 : git ls-remote, code 0 (2 attendu : absente du dépôt distant)"
# --- aval inchangé : échec d'amorce, pièce d'écart 2 modifiée, arguments
scenario_e2e "40|AMORCE 2026-11-13T15:01:20Z : commit __COMMIT__" "250|AMORCE : clonage impossible (jeton GitHub ?)"
ench E6-17-echec-amorce 0 2 - 0.53
D=$E2/d-E6-17-echec-amorce
res E6-17b "$( grep -q 'contrôle à cinq minutes : code 1' "$D/enchaineur.txt" && grep -q 'surveillance : code 0 ; dernière ligne : ÉCHEC D.AMORCE' "$D/enchaineur.txt" \
    && [ "$(dernier_off "$D/cinq-minutes")" -ge 250 ] && [ "$(dernier_off "$D/cinq-minutes")" -lt 290 ]; echo $?)" \
    "échec d'amorce à + 250 s : contrôle en code 1, la surveillance suit (R-2393) et arrête par l'identifiant"
detruites; scenario_e2e "${E_SAIN[@]}"
cp "$E2/H/surveiller_p3bis_v2_ecart2_v1.sh" "$E2/surv-de-cote.sh"; echo "# ajout" >> "$E2/H/surveiller_p3bis_v2_ecart2_v1.sh"
ench E6-18-piece-ecart2-modifiee 2 2 - 0.53
res E6-18b "$( [ ! -e "$E2/d-E6-18-piece-ecart2-modifiee" ] && [ ! -s "$E2/appels-E6-18-piece-ecart2-modifiee.txt" ]; echo $?)" "surveillance d'écart 2 modifiée : refus avant tout appel"
cp "$E2/surv-de-cote.sh" "$E2/H/surveiller_p3bis_v2_ecart2_v1.sh"
c=0; env -i PATH="$E2/bin:/usr/bin:/bin" HOME="$E2/home" LANG=C.UTF-8 E2E_ETAT="$E2/etat" bash "$E2/H/enchaineur_p3bis_v6.sh" "$SF" "$E2/d-E6-19" - 2 dix > "$E2/console-E6-19.txt" 2>&1 || c=$?
res E6-19-depense-anterieure-illisible "$( [ "$c" = 2 ] && [ ! -e "$E2/d-E6-19" ]; echo $?)" "dépense antérieure illisible : code 2, rien de créé"
mkdir -p "$E2/d-E6-20"; c=0; env -i PATH="$E2/bin:/usr/bin:/bin" HOME="$E2/home" LANG=C.UTF-8 E2E_ETAT="$E2/etat" bash "$E2/H/enchaineur_p3bis_v6.sh" "$SF" "$E2/d-E6-20" - 2 0 > "$E2/console-E6-20.txt" 2>&1 || c=$?
res E6-20-dossier-existant "$( [ "$c" = 2 ] && grep -q 'existe déjà (R12)' "$E2/console-E6-20.txt"; echo $?)" "dossier existant : code 2 (R12)"
c=0; env -i PATH="$E2/bin:/usr/bin:/bin" HOME="$E2/home" LANG=C.UTF-8 E2E_ETAT="$E2/etat" bash "$E2/H/enchaineur_p3bis_v6.sh" "$SF" "$E2/d-E6-21" - > "$E2/console-E6-21.txt" 2>&1 || c=$?
res E6-21-usage "$( [ "$c" = 2 ] && grep -q '^usage : enchaineur_p3bis_v6.sh S DOSSIER_NEUF EN_MARCHE N DEPENSE_ANTERIEURE_USD$' "$E2/console-E6-21.txt" && [ ! -e "$E2/d-E6-21" ]; echo $?)" "trois arguments : usage, code 2"
res E6-22-creations "$( [ "$(wc -l < "$E2/etat/creations.txt")" = 5 ] && [ "$(grep -c 'branche calcul/p3bis-reel-v2 etiquette p3bis-v2$' "$E2/etat/creations.txt")" = 5 ]; echo $?)" \
    "créations factices de tout le banc : 5 (E6-01, E6-03, E6-04T, E6-07, E6-17), toutes sur calcul/p3bis-reel-v2, étiquette p3bis-v2"
# =================================================================================================== R : bancs existants
echo "=== R : bancs existants rejoués ==="
c=0; bash "$ICI/essais_lanceur_p3bis_v2.sh" "$R/banc-lanceur-origine" > "$R/banc-lanceur-origine.log" 2>&1 || c=$?
res R-01-banc-lanceur-origine "$( [ "$c" = 0 ] && tail -1 "$R/banc-lanceur-origine.log" | grep -qx 'FIN DU BANC DU LANCEUR DE P3-BIS ; cas non conformes : 0' \
    && diff <(grep -v '^    | ' "$ICI/banc-lanceur-p3bis-v2.log") <(grep -v '^    | ' "$R/banc-lanceur-origine.log") > /dev/null; echo $?)" \
    "banc du lanceur d'origine rejoué : 0 non conforme, lignes de verdict égales au journal canonique versé à S (hors lignes citées « | »)"
diff <(grep '^    | ' "$ICI/banc-lanceur-p3bis-v2.log") <(grep '^    | ' "$R/banc-lanceur-origine.log") | grep -c '^>' | sed 's/^/    lignes citées « | » qui diffèrent du canonique (commits et empreintes factices) : /'
c=0; bash "$ICI/essais_ecart2_p3bis_v1.sh" "$R/banc-ecart2" "$PYT" > "$R/banc-ecart2.log" 2>&1 || c=$?
verdicts() { sed -n -E 's/^([A-Za-z0-9-]+) : .* : (CONFORME|NON CONFORME)$/\1 \2/p' "$1"; }
res R-02-banc-ecart2 "$( [ "$c" = 0 ] && tail -1 "$R/banc-ecart2.log" | grep -qx "ESSAIS DE L'ÉCART 2 DE P3-BIS : CONFORMES" \
    && grep -qx 'cas joués : 132' "$R/banc-ecart2.log" && diff <(verdicts "$ICI/essais-ecart2-p3bis-v1.log") <(verdicts "$R/banc-ecart2.log") > /dev/null; echo $?)" \
    "banc de l'écart 2 rejoué (enchaîneur v5, contrôle, surveillance et module d'écart 2) : 132 cas, 0 non conforme, mêmes cas et mêmes verdicts que le journal versé"
for f in "$LO" $(sed -n 's/^CHAINE="\(.*\)"$/\1/p' "$ICI/$LO"); do
    res "R-03-origine-egal-a-S-$f" "$( [ "$(git -C "$SRC" show "$SCELLE:$VERS/$f" | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$ICI/$f" | cut -d' ' -f1)" ]; echo $?)" "$f du dossier égal à sa copie versée à S"
done
res R-04-pieces-inchangees "$( [ "$(sha256sum "$ENCH5" | cut -d' ' -f1)" = 34131eaf528f65077576a83a64fceb58100ab34027b043c79763a31669e063a0 ] \
    && [ "$(sha256sum "$ICI/$LE" | cut -d' ' -f1)" = 2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb ] \
    && [ "$(sha256sum "$ICI/controle_cinq_minutes_p3bis_v2_ecart2_v1.sh" | cut -d' ' -f1)" = 6aa165e50d11ac1161686b79b1b690ff23e2528abf833b693f7874701f3cd66f ] \
    && [ "$(sha256sum "$ICI/surveiller_p3bis_v2_ecart2_v1.sh" | cut -d' ' -f1)" = 555ee5223ccb1742d890b8cc2e6da74dba0a1a98d743ed1b3234eb67998c19db ] \
    && [ "$(sha256sum "$ICI/verifications_p3bis_v2_ecart2_v1.py" | cut -d' ' -f1)" = ba6deb689b92cab04f580165b955e2c69c9558a5e229f0f7f1ef170aba89107e ]; echo $?)" \
    "enchaîneur v5 (34131eaf…), lanceur d'écart 1 v2 (2e294e5a…) et pièces d'écart 2 (6aa165e5…, 555ee522…, ba6deb68…) inchangés"
echo "cas joués : $NCAS"
echo "fin des essais : $(date -u +%FT%TZ)"
if [ "$NC" = 0 ]; then echo "ESSAIS DE L'ÉCART 3 DE P3-BIS : CONFORMES"; else echo "ESSAIS DE L'ÉCART 3 DE P3-BIS : $NC NON CONFORME(S)"; exit 1; fi
