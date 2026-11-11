#!/usr/bin/env bash
# Essais R5 du lanceur d'écart 1 de P3-bis (R-2399 ; consigne `consigne-ecart1-lanceur-credit-p3bis-v1.md`, `f8dfb475…`),
# v2, écrits le 2026-11-11 vers 23:49 UTC (heure relevée par `date -u`) : v1 (`acf6f7c8…`) gardé tel quel (R12) ; v2
# joue le lanceur d'écart v2 (corrections C1 et C2 de la contre-lecture `9b1013db…`), change la dernière ligne
# attendue de E5 et ajoute E14 (C1) et E15 (C2). Bac à sable : FAUX outil de location (aucun
# service appelé, aucune dépense), dépôt synthétique et dépôt nu local, registre des GO TEMPORAIRE (en-tête et ligne
# GO-2026-11-10-02 recopiés de main ; une ligne FACTICE GO-2026-11-11-90 pour l'instance nommée en marche, jamais au vrai
# registre), texte factice (lignes lues par le lanceur et le contrôle à cinq minutes), journaux de preuve factices à la
# forme du module commun, contrôles avant dépense : BOUCHON (comme la répétition jouet). Déclinés de
# `repetition_jouet_p3bis_v2.sh` (même faux outil, sans construction de branche de calcul).
# Copies jouées, lignes changées comptées : lanceur d'origine et lanceur d'écart (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S) ;
# contrôle à cinq minutes, surveillance, destruction, module commun : copies exactes.
# Cas (instance nommée en marche : 12345678, 1,10 USD/h, donc minimum officiel 31 USD) :
#   E1 crédit 0 : refus, code 3 (« crédit nul ou négatif ») ; ligne officielle et ligne d'écart écrites ; aucune création ;
#   E2 crédit −2,5 : refus, code 3 ;
#   E3 crédit illisible (« six ») : code 2 ; E4 réponse non JSON : code 2 ; E5 outil en échec sans réponse : code 2
#      (v2 : « crédit illisible (show user, outil en échec, code 1) ») ;
#   E14 (C1) réponse lisible {"credit": 6.0} mais outil en échec (code 1) : code 2, aucune création, aucune ligne
#       d'écart, ligne officielle écrite ; E15 (C2) crédit 0,004 : code 3 (« crédit 0.00 » au centime), aucune création ;
#   E6 lanceur d'origine absent du dossier : refus du contrôle de soi, code 2 ; E7 lanceur d'origine modifié : idem ;
#   E8 témoin : lanceur d'ORIGINE, crédit 6 USD : refus, code 3 (« crédit insuffisant ») ;
#   E9 cas sain : lanceur d'écart, crédit 6 USD : la garde passe sous l'écart, ligne d'écart écrite, création factice ;
#   E10 contrôle à cinq minutes sur ces traces (à la création + 181 s) : conforme ;
#   E11 surveillance (INTERVALLE=1) : FIN, arrêt par l'identifiant ; E12 destruction (rapport de récupération FACTICE,
#       déclaré : la récupération ne lit pas les traces du lanceur) : détruite par l'identifiant ;
#   E13 crédit 50 USD (le module rend 0) : création ; ligne d'écart écrite aussi.
# Usage : essais_ecart1_lanceur_p3bis_v2.sh RACINE_NEUVE
set -uo pipefail
R=$(realpath -m "${1:?racine neuve}")
SOI=$(realpath "$0")
SRC=$(realpath "$(dirname "$SOI")/../../../..")
ICI=$SRC/docs/procedures/P3-bis-temoin-positif-v1
V=docs/procedures/P3-bis-temoin-positif-v1
P=prereg/P3-bis-temoin-positif-v1.md
A=scripts/amorce_instance_p3bis_v2.sh
PYB=/home/user/controle-ia-travail/.venv/bin/python
LE=lancer_p3bis_v2_ecart1_v2.sh
LO=lancer_p3bis_v2.sh
export PYTHONDONTWRITEBYTECODE=1
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R/bin" "$R/H" "$R/home" "$R/etat" || exit 2
echo "début des essais : $(date -u +%FT%TZ)"
for s in "$LE" "$LO" verifications_p3bis_v2.py controle_cinq_minutes_p3bis_v2.sh surveiller_p3bis_v2.sh detruire_p3bis_v2.sh; do
    echo "script joué : $s $(sha256sum "$ICI/$s" | cut -d' ' -f1)"
done
echo "script joué : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
NON_CONFORMES=0
JETONS=(HF_TOKEN=factice-hf-6666666 CONTROLE_IA_GITHUB_TOKEN=factice-gi-7777777)
# --- copies jouées -----------------------------------------------------------------------------------------------------
for s in "$LO" "$LE"; do
    sed -e "s|^DEPOT=.*|DEPOT=$R/depot|" -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$R/distant.git|" -e "s|^INTERVALLE_OFFRE_S=.*|INTERVALLE_OFFRE_S=0|" "$ICI/$s" > "$R/H/$s"
    n=$(diff "$ICI/$s" "$R/H/$s" | grep -c '^>')
    echo "lignes changées dans la copie de $s : $n (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S)"
    [ "$n" = 3 ] || { echo "copie de $s non sûre"; exit 2; }
done
echo "écart entre les deux copies jouées = écart entre les deux lanceurs : $( [ "$(diff "$R/H/$LO" "$R/H/$LE" | md5sum)" = "$(diff "$ICI/$LO" "$ICI/$LE" | md5sum)" ] && echo CONFORME || echo 'NON CONFORME')"
for s in controle_cinq_minutes_p3bis_v2.sh surveiller_p3bis_v2.sh detruire_p3bis_v2.sh verifications_p3bis_v2.py; do cp "$ICI/$s" "$R/H/"; done
cat > "$R/H/controles_avant_depense_p3bis_v2.sh" <<'EOF'
#!/usr/bin/env bash
# bouchon des essais de l'écart 1 : les contrôles réels sont joués par leur banc et par la répétition finale
mkdir -p "$2" "$2.travail"; echo "OK  bouchon des essais de l'écart 1 (S=${1:0:12}, branche $3)"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
CHAINE=$(sed -n 's/^CHAINE="\(.*\)"$/\1/p' "$R/H/$LO")
for s in $CHAINE; do [ -e "$R/H/$s" ] || cp "$ICI/$s" "$R/H/$s"; done
# --- dépôt synthétique : S n'a que le lanceur d'origine (comme le vrai S) -------------------------------------------
git init -q --bare -b main "$R/distant.git"
git init -q -b main "$R/depot" && cd "$R/depot" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false; git config push.negotiate false
git remote add origin "$R/distant.git"
mkdir -p prereg scripts registres .claude/hooks "$V"
cp "$SRC/$A" "$A"
cp "$SRC/.claude/hooks/garde_calcul.py" .claude/hooks/garde_calcul.py
{ git -C "$SRC" show main:registres/go.md | sed -n '1,10p'; git -C "$SRC" show main:registres/go.md | grep '^| GO-2026-11-10-02 |'
  echo "| GO-2026-11-11-90 | 2026-11-11 | calcul | FACTICE des essais de l'écart 1 : instance nommée en marche (jamais au vrai registre) | 1 USD | 2026-11-30 | Lazar | essais_ecart1_lanceur_p3bis_v1.sh |"; } > registres/go.md
[ "$(grep -c '^| GO-2026-11-10-02 |' registres/go.md)" = 1 ] || { echo "ligne GO-2026-11-10-02 absente de main"; exit 2; }
for s in "$LO" $CHAINE; do cp "$R/H/$s" "$V/$s"; done
"$PYB" -I -B - "$R/H/verifications_p3bis_v2.py" "$R/H" "$V" <<'EOF' || exit 2
import hashlib, importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
h, sortie = Path(sys.argv[2]), Path(sys.argv[3])
for nom, (verdict, scripts) in v.JOURNAUX.items():
    lignes = [f"script éprouvé : {s} {hashlib.sha256((h / s).read_bytes()).hexdigest()}" for s in sorted(scripts)]
    (sortie / nom).write_text("\n".join(lignes) + "\njournal factice des essais de l'écart 1\n" + verdict + "\n", encoding="utf-8")
EOF
(cd "$V" && for f in *; do case "$f" in *.sha256) ;; *) sha256sum "$f" > "$f.sha256" ;; esac; done)
git add -A && git commit -qm "base des essais de l'écart 1" && git push -q origin main || exit 2
E_AMORCE=$(sha256sum "$A" | cut -d' ' -f1)
cat > "$P" <<EOF
# Préenregistrement factice des essais de l'écart 1 de P3-bis

- GO : **GO-2026-11-10-02** (\`registres/go.md\`)
- Lancement : \`GO_ID=GO-2026-11-10-02\`, \`PREREG=$P\`, \`BRANCHE=calcul/p3bis-reel-v1\` (une relance prend \`…-v2\`, puis \`…-v3\`), \`DEPOT_URL=file://$R/distant.git\`
- Empreintes : \`$A\` (\`$E_AMORCE\`, sha256)
- Tests attendus : \`531\`
EOF
(cd prereg && sha256sum P3-bis-temoin-positif-v1.md > P3-bis-temoin-positif-v1.md.sha256)
git add -A && git commit -qm "S (essais de l'écart 1)" && git push -q origin main || exit 2
S=$(git rev-parse HEAD); echo "commit de scellement factice : $S"
cd "$R" || exit 2
# --- faux outil de location ------------------------------------------------------------------------------------------
printf '%s\n' '{"credit": 6.0}' > "$R/etat/user-reponse"; echo 0 > "$R/etat/user-code"; echo 0 > "$R/etat/compteur"
cat > "$R/bin/vastai" <<EOF
#!/usr/bin/env bash
# faux outil de location des essais de l'écart 1 : n'appelle aucun service
ET="$R/etat"
echo "\$(date -u +%FT%TZ) \$*" >> "\$ET/appels.txt"
case "\$1 \$2" in
  "search offers") printf '%s\n' '[{"id": 111, "machine_id": 7101, "host_id": 8101, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 257000, "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.989, "dph_total": 1.10, "inet_down_cost": 0.026, "storage_total_cost": 0.05}]' ;;
  "show user") cat "\$ET/user-reponse"; exit "\$(cat "\$ET/user-code")" ;;
  "show instances")
    l='{"id": 58936096, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936099, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936100, "actual_status": "exited", "cur_state": "stopped"}, {"id": 12345678, "actual_status": "running", "cur_state": "running", "dph_total": 1.1}'
    for d in "\$ET"/instance-*; do [ -d "\$d" ] || continue; [ -e "\$d/detruite" ] && continue
        l="\$l, {\"id\": \${d##*-}, \"actual_status\": \"\$( [ -e "\$d/arretee" ] && echo exited || echo running)\", \"cur_state\": \"\$( [ -e "\$d/arretee" ] && echo stopped || echo running)\", \"dph_total\": 1.1}"; done
    echo "[\$l]" ;;
  "create instance")
    a=("\$@"); br=""; commit=""; lab=""
    for ((i = 0; i < \${#a[@]}; i++)); do
      [ "\${a[\$i]}" = "--label" ] && lab=\${a[\$((i + 1))]}
      [ "\${a[\$i]}" = "--env" ] && for kv in \${a[\$((i + 1))]}; do case "\$kv" in BRANCHE=*) br=\${kv#BRANCHE=} ;; COMMIT=*) commit=\${kv#COMMIT=} ;; esac; done
    done
    k=\$(( \$(cat "\$ET/compteur") + 1 )); echo "\$k" > "\$ET/compteur"; id=7777777\$k; mkdir -p "\$ET/instance-\$id"
    printf '%s\n' "\$br" > "\$ET/instance-\$id/branche"; printf '%s\n' "\$commit" > "\$ET/instance-\$id/commit"; printf '%s\n' "\$lab" > "\$ET/instance-\$id/etiquette"
    echo "{\"success\": true, \"new_contract\": \$id}" ;;
  "show instance")
    d="\$ET/instance-\$3"; [ -d "\$d" ] || { echo "instance inconnue"; exit 1; }
    st=running; cs=running; [ -e "\$d/arretee" ] && { st=exited; cs=stopped; }
    echo "{\"actual_status\": \"\$st\", \"cur_state\": \"\$cs\", \"intended_status\": \"running\", \"status_msg\": \"jouet\", \"dph_total\": 1.1, \"machine_id\": 7101, \"host_id\": 8101, \"gpu_name\": \"A100 SXM4\", \"label\": \"\$(cat "\$d/etiquette")\", \"inet_down_billed\": 18, \"inet_down_cost\": 0.026}" ;;
  "logs "*)
    d="\$ET/instance-\$2"; [ -d "\$d" ] || exit 1
    n=\$(( \$(cat "\$d/tours" 2>/dev/null || echo 0) + 1 )); echo "\$n" > "\$d/tours"
    br=\$(cat "\$d/branche"); c=\$(cat "\$d/commit")
    echo "AMORCE 2026-11-12T08:00:00Z : commit \$c"
    echo "2026-11-12T08:00:10Z début : ETUDE=p3bis MODE=reel COMMIT=\$c BRANCHE=\$br"
    echo "2026-11-12T08:00:20Z préenregistrement lu : 531 tests attendus ; configuration prereg/P3-bis-temoin-positif-config-v1.json"
    echo "NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB"
    echo "2026-11-12T08:00:40Z branche \$br poussée avant l'installation (droit d'écriture éprouvé)"
    [ "\$n" -ge 2 ] && echo "PROGRES 2026-11-12T09:00:00Z etape=sondes-figees empreinte=0123456789abcdef sondes=1630"
    if [ "\$n" -ge 3 ]; then
      echo "2026-11-12T09:01:00Z run : processus 4242 lancé"; echo "2026-11-12T12:00:00Z run : processus 4242 fini, code 0"
      echo "AMORCE 2026-11-12T12:30:00Z : fin, code 0"
    fi ;;
  "stop instance") [ -d "\$ET/instance-\$3" ] && touch "\$ET/instance-\$3/arretee" && echo '{"success": true}' ;;
  "destroy instance") [ -d "\$ET/instance-\$3" ] && touch "\$ET/instance-\$3/detruite" && echo '{"success": true}' ;;
  *) echo "verbe inattendu : \$*" >&2; exit 9 ;;
esac
EOF
chmod +x "$R/bin/vastai"
ENV=(env -i PATH="$R/bin:/usr/bin:/bin" HOME="$R/home" LANG=C.UTF-8 "${JETONS[@]}")
EM=12345678:GO-2026-11-11-90
LIGNE_ECART="écart 1 (R-2399) : garde du crédit remplacée par la recharge automatique du compte (mot de Lazar) ; crédit présent > 0 exigé"
etape() {   # $1 nom, $2 code attendu, $3 motif de la dernière ligne ; puis la commande
    local nom=$1 attendu=$2 motif=$3 c t0 v; shift 3
    t0=$(date -u +%s)
    "${ENV[@]}" "$@" > "$R/console-$nom.txt" 2>&1; c=$?
    v=CONFORME
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    grep -v '^$' "$R/console-$nom.txt" | tail -1 | grep -qF -- "$motif" || v="NON CONFORME (motif « $motif » absent de la dernière ligne)"
    grep -qF -e factice-hf-6666666 -e factice-gi-7777777 "$R/console-$nom.txt" && v="NON CONFORME (JETON AFFICHÉ)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(( $(date -u +%s) - t0 )) s ; $v"
    grep -v '^$' "$R/console-$nom.txt" | tail -1 | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
}
verifier() {
    local desc=$1; shift
    if (eval "$*") > /dev/null 2>&1; then echo "    $desc : CONFORME"; else echo "    $desc : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
credit() { printf '%s\n' "$1" > "$R/etat/user-reponse"; echo "${2:-0}" > "$R/etat/user-code"; }
creations() { grep -c ' create instance ' "$R/etat/appels.txt" 2>/dev/null || true; }
# --- artefacts ---------------------------------------------------------------------------------------------------------
credit '{"credit": 0}'
etape E1-credit-nul 3 "crédit nul ou négatif : pas de création" bash "$R/H/$LE" "$S" "$R/traces-e1" "$EM" 1
verifier "E1 : ligne officielle (minimum 31.00 USD) puis ligne d'écart dans lancement.txt ; aucune création" \
    "grep -q '^crédit 0.00 USD ; minimum 31.00 USD' '$R/traces-e1/lancement.txt' && [ \"\$(awk '/^crédit 0.00 USD/ {getline n; print n}' '$R/traces-e1/lancement.txt')\" = '$LIGNE_ECART' ] && [ \"\$(grep -c ' create instance ' '$R/etat/appels.txt')\" = 0 ] && ! grep -q '^creation ' '$R/traces-e1/lancement.txt'"
credit '{"credit": -2.5}'
etape E2-credit-negatif 3 "crédit nul ou négatif : pas de création" bash "$R/H/$LE" "$S" "$R/traces-e2" "$EM" 1
credit '{"credit": "six"}'
etape E3-credit-illisible 2 "crédit illisible (show user, code 2) : pas de création" bash "$R/H/$LE" "$S" "$R/traces-e3" "$EM" 1
verifier "E3 : aucune ligne d'écart (arrêt avant), aucune création" "! grep -qF 'écart 1' '$R/traces-e3/lancement.txt' && [ \"\$(grep -c ' create instance ' '$R/etat/appels.txt')\" = 0 ]"
credit 'erreur du service'
etape E4-reponse-non-json 2 "crédit illisible (show user, code 2) : pas de création" bash "$R/H/$LE" "$S" "$R/traces-e4" "$EM" 1
credit '' 1
etape E5-outil-en-echec 2 "crédit illisible (show user, outil en échec, code 1) : pas de création" bash "$R/H/$LE" "$S" "$R/traces-e5" "$EM" 1
credit '{"credit": 6.0}' 1
etape E14-outil-en-echec-reponse-lisible 2 "crédit illisible (show user, outil en échec, code 1) : pas de création" bash "$R/H/$LE" "$S" "$R/traces-e14" "$EM" 1
verifier "E14 (C1) : ligne officielle (crédit 6.00, minimum 31.00) écrite, aucune ligne d'écart, aucune création" \
    "grep -q '^crédit 6.00 USD ; minimum 31.00 USD' '$R/traces-e14/lancement.txt' && ! grep -qF 'écart 1' '$R/traces-e14/lancement.txt' && [ \"\$(grep -c ' create instance ' '$R/etat/appels.txt')\" = 0 ] && ! grep -q '^creation ' '$R/traces-e14/lancement.txt'"
credit '{"credit": 0.004}'
etape E15-credit-sous-le-centime 3 "crédit nul ou négatif : pas de création" bash "$R/H/$LE" "$S" "$R/traces-e15" "$EM" 1
verifier "E15 (C2) : ligne officielle « crédit 0.00 USD » puis ligne d'écart ; aucune création" \
    "[ \"\$(awk '/^crédit 0.00 USD/ {getline n; print n}' '$R/traces-e15/lancement.txt')\" = '$LIGNE_ECART' ] && [ \"\$(grep -c ' create instance ' '$R/etat/appels.txt')\" = 0 ]"
credit '{"credit": 6.0}'
mv "$R/H/$LO" "$R/origine-de-cote.sh"
etape E6-origine-absente 2 "lancer_p3bis_v2.sh exécuté ≠ copie versée au commit S" bash "$R/H/$LE" "$S" "$R/traces-e6" "$EM" 1
cp "$R/origine-de-cote.sh" "$R/H/$LO"; echo "# ajout" >> "$R/H/$LO"
etape E7-origine-modifiee 2 "lancer_p3bis_v2.sh exécuté ≠ copie versée au commit S" bash "$R/H/$LE" "$S" "$R/traces-e7" "$EM" 1
mv "$R/origine-de-cote.sh" "$R/H/$LO"
verifier "lanceur d'origine rendu égal à sa copie versée à S" "[ \"\$(sha256sum < '$R/H/$LO')\" = \"\$(git -C '$R/depot' show '$S:$V/$LO' | sha256sum)\" ]"
etape E8-temoin-origine-credit-6 3 "crédit insuffisant : pas de création ; recharge demandée à Lazar" bash "$R/H/$LO" "$S" "$R/traces-e8" "$EM" 1
verifier "E1 à E8, E14, E15 : aucune création demandée au faux outil" "[ \"\$(grep -c ' create instance ' '$R/etat/appels.txt')\" = 0 ]"
# --- cas sain ----------------------------------------------------------------------------------------------------------
etape E9-sain-credit-6 0 "succès : True ; identifiant 77777771" bash "$R/H/$LE" "$S" "$R/traces-e9" "$EM" 1
verifier "E9 : ligne officielle (crédit 6.00, minimum 31.00), ligne d'écart, instance 77777771, empreinte du lanceur d'écart joué sur la ligne « lanceur p3bis v2 »" \
    "grep -q '^crédit 6.00 USD ; minimum 31.00 USD' '$R/traces-e9/lancement.txt' && grep -qxF '$LIGNE_ECART' '$R/traces-e9/lancement.txt' && grep -qx 'instance 77777771' '$R/traces-e9/lancement.txt' && grep -q \"^lanceur p3bis v2 \$(sha256sum '$R/H/$LE' | cut -d' ' -f1) ; instances en marche nommées $EM\$\" '$R/traces-e9/lancement.txt'"
cr=$(sed -n 's/^creation \([0-9]*\)$/\1/p' "$R/traces-e9/lancement.txt")
while [ "$(date -u +%s)" -lt $((cr + 181)) ]; do sleep 5; done
etape E10-cinq-minutes 0 "CONTRÔLE À CINQ MINUTES : CONFORME" bash "$R/H/controle_cinq_minutes_p3bis_v2.sh" 77777771 "$R/traces-e9" "$R/cinq-e9"
"${ENV[@]}" INTERVALLE=1 bash "$R/H/surveiller_p3bis_v2.sh" 77777771 "$R/traces-e9" 0 "$R/surv-e9" > "$R/console-E11-surveillance.txt" 2>&1; c=$?
[ "$c" = 0 ] && tail -1 "$R/console-E11-surveillance.txt" | grep -q '^FIN : AMORCE .* fin, code 0 ; instance 77777771 arrêtée par son identifiant' \
    && echo "E11-surveillance : code 0 ; CONFORME" || { echo "E11-surveillance : code $c ; NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
tail -1 "$R/console-E11-surveillance.txt" | cut -c1-170 | sed 's/^/    | /'
printf 'rapport FACTICE des essais de l écart 1 (aucune récupération jouée : elle ne lit pas les traces du lanceur)\nRÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures %s poussé sur calcul/p3bis-reel-v1\n' "$(printf '0%.0s' $(seq 64))" > "$R/rapport-recuperation-factice.txt"
etape E12-destruction 0 "DESTRUCTION : instance 77777771 détruite par son identifiant" bash "$R/H/detruire_p3bis_v2.sh" 77777771 "$R/traces-e9" "$R/surv-e9" "$R/rapport-recuperation-factice.txt"
credit '{"credit": 50.0}'
etape E13-credit-50 0 "succès : True ; identifiant 77777772" bash "$R/H/$LE" "$S" "$R/traces-e13" "$EM" 1
verifier "E13 : ligne officielle (crédit 50.00, minimum 31.00) et ligne d'écart" \
    "grep -q '^crédit 50.00 USD ; minimum 31.00 USD' '$R/traces-e13/lancement.txt' && grep -qxF '$LIGNE_ECART' '$R/traces-e13/lancement.txt'"
verifier "aucun appel de création hors E9 et E13 (deux en tout) ; vrai registre des GO jamais lu par les copies jouées (DEPOT synthétique)" \
    "[ \"\$(grep -c ' create instance ' '$R/etat/appels.txt')\" = 2 ] && grep -qx 'DEPOT=$R/depot' '$R/H/$LE'"
echo "fin des essais : $(date -u +%FT%TZ)"
if [ "$NON_CONFORMES" = 0 ]; then echo "ESSAIS DU LANCEUR D'ÉCART 1 DE P3-BIS : CONFORMES"; else echo "ESSAIS DU LANCEUR D'ÉCART 1 DE P3-BIS : $NON_CONFORMES NON CONFORME(S)"; exit 1; fi
