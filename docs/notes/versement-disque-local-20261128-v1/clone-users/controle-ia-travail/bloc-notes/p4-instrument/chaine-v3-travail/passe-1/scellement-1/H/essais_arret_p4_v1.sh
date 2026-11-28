#!/usr/bin/env bash
# Banc du script d'arrêt de P4-instrument, arreter_p4_v1.sh (R5 : cas sain et artefacts), v1, neuf (chaîne v2,
# RC-depense-01, RC-fidelite-06). Faux outil de location (aucun service appelé) : étiquette, état avant l'arrêt et suite
# des états relus après l'arrêt fixés par le scénario ; arrêt journalisé, refusé sur demande ; jeton factice dans la
# réponse (jamais affiché). Faux `sleep` en tête du PATH (le délai borné se compte en lectures, sans attente réelle).
# Cas : sain ; instance déjà arrêtée ; arrêt relu une fois puis en marche, puis arrêté deux fois (deux lectures de suite
# exigées) ; étiquette autre, « p4-v1 x », absente ; état illisible ; état qui ne passe pas à l'arrêt (60 lectures,
# code 1) ; outil en échec à l'arrêt (code 1) ; identifiant mal formé (lettres, 5 chiffres, 11 chiffres) ; outil
# introuvable ; dossier existant ; motif mal formé ; usage faux. Verdict par cas : code, dernière ligne, nombre de
# demandes d'arrêt au faux outil (zéro sur tout refus en code 2), ligne prête pour registres/arrets.md sur le cas sain.
# Chaîne v3 : étiquette « p4-v1 » suivie d'un saut de ligne, en majuscules, suivie d'une espace, numérique (VC2-depense-02 :
# code 2, aucune demande d'arrêt) ; ligne prête pour registres/arrets.md aux quatre cellules du registre (VC2-depense-04).
# Usage : essais_arret_p4_v1.sh RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré
E=$(realpath -m "${1:?racine neuve}")
HN=${HN:-/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v3}
ARRET=$HN/arreter_p4_v1.sh
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/bin" "$E/bin-temps" || exit 2
echo "script éprouvé : arreter_p4_v1.sh $(sha256sum "$ARRET" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
ID=99999999
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil : étiquette (fichier etiquette, défaut p4-v1 ; « nulle » : étiquette absente ; fichier etiquette-json :
# valeur JSON brute de l'étiquette, chaîne v3), état avant l'arrêt
# (fichier avant, défaut running), états après l'arrêt (fichier apres : une ligne par lecture, la dernière se répète ;
# défaut exited stopped), état illisible (fichier illisible), arrêt refusé (fichier arret-echec)
S=${SCENARIO:?}
case "$1 $2" in
  "show instance")
    echo "show instance $3" >> "$S/outil.txt"
    [ -e "$S/illisible" ] && { echo "réponse non JSON (essai)"; exit 0; }
    lab=$(cat "$S/etiquette" 2>/dev/null || echo p4-v1)
    if [ -e "$S/arrete" ]; then
        k=$(( $(cat "$S/lectures" 2>/dev/null || echo 0) + 1 )); echo "$k" > "$S/lectures"
        if [ -f "$S/apres" ]; then e=$(sed -n "${k}p" "$S/apres"); [ -n "$e" ] || e=$(tail -1 "$S/apres"); else e="exited stopped"; fi
    else e=$(cat "$S/avant" 2>/dev/null || echo "running running"); fi
    set -- $e
    if [ -e "$S/etiquette-json" ]; then labj=$(cat "$S/etiquette-json"); elif [ "$lab" = nulle ]; then labj=null; else labj="\"$lab\""; fi
    printf '{"id": %s, "label": %s, "actual_status": "%s", "cur_state": "%s", "extra_env": [["GH_TOKEN", "factice-gh-arret-0001"]]}\n' 99999999 "$labj" "$1" "$2" ;;
  "stop instance")
    echo "stop instance $3" >> "$S/outil.txt"
    [ -e "$S/arret-echec" ] && { echo "erreur factice factice-gh-arret-0001" >&2; exit 1; }
    touch "$S/arrete"; echo '{"success": true}' ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
cat > "$E/bin-temps/sleep" <<'EOF'
#!/usr/bin/env bash
echo "$1" >> "${SCENARIO:?}/sommeils"
EOF
chmod +x "$E/bin/vastai" "$E/bin-temps/sleep"
NON_CONFORMES=0
cas() {   # $1 nom, $2 code attendu, $3 motif de la dernière ligne, $4 demandes d'arrêt attendues, $5 PATH, puis les arguments
    local n=$1 a=$2 m=$3 nstop=$4 chemin=$5 c v; shift 5
    local sc="$E/scenario-$n"; mkdir -p "$sc"
    [ -n "${PREPARER:-}" ] && (cd "$sc" && eval "$PREPARER")
    env -i PATH="$chemin" HOME="$E" LANG=C.UTF-8 SCENARIO="$sc" bash "$ARRET" "$@" > "$E/sortie-$n.txt" 2>&1; c=$?
    local ns; ns=$(grep -c '^stop instance' "$sc/outil.txt" 2>/dev/null); ns=${ns:-0}
    v="CONFORME"
    [ "$c" = "$a" ] || v="NON CONF""ORME (code $c, attendu $a)"
    tail -1 "$E/sortie-$n.txt" | grep -qF -- "$m" || v="NON CONF""ORME (motif « $m » absent de la dernière ligne)"
    [ "$ns" = "$nstop" ] || v="NON CONF""ORME ($ns demande(s) d'arrêt, $nstop attendue(s))"
    grep -q "factice-gh-arret" "$E/sortie-$n.txt" && v="NON CONF""ORME (jeton affiché)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$n : code $c ; demandes d'arrêt $ns ; lectures après l'arrêt $(cat "$sc/lectures" 2>/dev/null || echo 0) ; $v"
    tail -1 "$E/sortie-$n.txt" | couper 200 | sed 's/^/    | /'
}
P="$E/bin-temps:$E/bin:/usr/bin:/bin"
cas A00-sain 0 "ARRÊT CONFIRMÉ : INSTANCE $ID ARRÊTÉE PAR SON IDENTIFIANT" 1 "$P" "$ID" "$E/arret-A00" "surveillance : FIN"
L="$E/arret-A00/ligne-arrets.md"
# chaîne v3 (VC2-depense-04) : quatre cellules, la forme du registre ; date et heure de l'arrêt relu (celle de la fin)
python3 -c 'import re, sys
l = open(sys.argv[1], encoding="utf-8").read()
m = re.fullmatch(r"\| (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) \| instance Vast\.ai \*\*" + sys.argv[2] + r"\*\* \(P4-instrument, étiquette p4-v1 ; `vastai stop instance " + sys.argv[2] + r"`\) \| surveillance : FIN \| demandé à (\S+Z), relu arrêté \(exited, stopped\) deux fois de suite à (\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}):\d{2}Z \(arreter_p4_v1\.sh\) \|\n", l)
sys.exit(0 if m and m.group(1) == m.group(4) and m.group(2) == m.group(5) and l.count("|") == 5 else 1)' "$L" "$ID" \
    && [ "$(cat "$E/scenario-A00-sain/lectures")" = 2 ] && grep -q "^.*Z : vastai stop instance $ID demandé$" "$E/arret-A00/arret.txt" \
    && echo "    A00 : heure de la demande et de l'arrêt écrites, ligne prête pour registres/arrets.md à quatre cellules (date et heure de l'arrêt relu), deux lectures : CONFORME" \
    || { echo "    A00 : ligne du registre, heures ou lectures : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
PREPARER='echo "exited stopped" > avant' cas A01-instance-deja-arretee 0 "ARRÊT CONFIRMÉ" 1 "$P" "$ID" "$E/arret-A01"
PREPARER='printf "exited stopped\nrunning running\nexited stopped\n" > apres' cas A02-arret-relu-une-fois-puis-en-marche 0 "ARRÊT CONFIRMÉ" 1 "$P" "$ID" "$E/arret-A02"
[ "$(cat "$E/scenario-A02-arret-relu-une-fois-puis-en-marche/lectures")" = 4 ] && echo "    A02 : deux lectures arrêtées de suite exigées (quatre lectures) : CONFORME" \
    || { echo "    A02 : lectures : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
PREPARER='echo rr-autre-projet > etiquette' cas A03-etiquette-autre 2 "≠ « p4-v1 » (comparée entière) : arrêt refusé" 0 "$P" "$ID" "$E/arret-A03"
PREPARER='echo "p4-v1 x" > etiquette' cas A04-etiquette-p4-v1-x 2 "≠ « p4-v1 » (comparée entière) : arrêt refusé" 0 "$P" "$ID" "$E/arret-A04"
PREPARER='echo nulle > etiquette' cas A05-etiquette-absente 2 "≠ « p4-v1 » (comparée entière) : arrêt refusé" 0 "$P" "$ID" "$E/arret-A05"
# chaîne v3 (VC2-depense-02) : étiquette comparée dans Python, exactement
PREPARER="printf '%s' '\"p4-v1\\n\"' > etiquette-json" cas A14-etiquette-p4-v1-suivie-d-un-saut-de-ligne 2 "≠ « p4-v1 » (comparée entière) : arrêt refusé" 0 "$P" "$ID" "$E/arret-A14"
grep -qF '« "p4-v1\n" »' "$E/sortie-A14-etiquette-p4-v1-suivie-d-un-saut-de-ligne.txt" && [ ! -e "$E/scenario-A14-etiquette-p4-v1-suivie-d-un-saut-de-ligne/sommeils" ] \
    && echo "    A14 : étiquette écrite sous sa forme JSON (saut de ligne visible), aucune relecture : CONFORME" \
    || { echo "    A14 : forme de l'étiquette ou relectures : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
PREPARER="printf '%s' '\"P4-V1\"' > etiquette-json" cas A15-etiquette-en-majuscules 2 "≠ « p4-v1 » (comparée entière) : arrêt refusé" 0 "$P" "$ID" "$E/arret-A15"
PREPARER="printf '%s' '\"p4-v1 \"' > etiquette-json" cas A16-etiquette-suivie-d-une-espace 2 "≠ « p4-v1 » (comparée entière) : arrêt refusé" 0 "$P" "$ID" "$E/arret-A16"
PREPARER="printf '%s' '41' > etiquette-json" cas A17-etiquette-numerique 2 "≠ « p4-v1 » (comparée entière) : arrêt refusé" 0 "$P" "$ID" "$E/arret-A17"
PREPARER='touch illisible' cas A06-etat-illisible 2 "étiquette non relue : arrêt refusé" 0 "$P" "$ID" "$E/arret-A06"
PREPARER='echo "running running" > apres' cas A07-etat-qui-ne-passe-pas-a-l-arret 1 "ARRÊT NON CONFIRMÉ : INSTANCE $ID (état non relu arrêté dans le délai)" 1 "$P" "$ID" "$E/arret-A07"
[ "$(cat "$E/scenario-A07-etat-qui-ne-passe-pas-a-l-arret/lectures")" = 60 ] && [ "$(wc -l < "$E/scenario-A07-etat-qui-ne-passe-pas-a-l-arret/sommeils")" = 60 ] \
    && echo "    A07 : délai borné : 60 lectures, 60 sommeils de 10 s au plus : CONFORME" || { echo "    A07 : délai : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
PREPARER='touch arret-echec' cas A08-outil-en-echec-a-l-arret 1 "ARRÊT NON CONFIRMÉ : INSTANCE $ID (outil en échec)" 1 "$P" "$ID" "$E/arret-A08"
cas A09-identifiant-en-lettres 2 "identifiant d'instance mal formé" 0 "$P" abc "$E/arret-A09"
cas A09b-identifiant-de-5-chiffres 2 "identifiant d'instance mal formé" 0 "$P" 12345 "$E/arret-A09b"
cas A09c-identifiant-de-11-chiffres 2 "identifiant d'instance mal formé" 0 "$P" 12345678901 "$E/arret-A09c"
cas A10-outil-introuvable 2 "outil de location introuvable" 0 "$E/bin-temps:/usr/bin:/bin" "$ID" "$E/arret-A10"
mkdir -p "$E/arret-A11"; cas A11-dossier-existant 2 "existe déjà (R12)" 0 "$P" "$ID" "$E/arret-A11"
cas A12-motif-mal-forme 2 "motif mal formé" 0 "$P" "$ID" "$E/arret-A12" "motif | avec barre"
cas A13-usage-un-argument 2 "usage" 0 "$P" "$ID"
[ ! -e "$E/arret-A09" ] && [ ! -e "$E/arret-A10" ] && echo "    refus avant tout : aucun dossier écrit (A09, A10) : CONFORME" || { echo "    dossier écrit sur un refus précoce : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
FUITES=$(grep -rl "factice-gh-arret" "$E"/sortie-*.txt "$E"/arret-* 2>/dev/null | head -3 || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché ni écrit : CONFORME" || { echo "JETON AFFI""CHÉ : $FUITES"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
