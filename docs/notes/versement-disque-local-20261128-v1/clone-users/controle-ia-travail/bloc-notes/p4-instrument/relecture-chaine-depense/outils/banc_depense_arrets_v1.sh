#!/usr/bin/env bash
# Relecture « dépense et arrêts » de la chaîne de P4-instrument, v1 : banc de la surveillance (surveiller_p4_v1.sh, tel
# quel) et du bloc de destruction de la récupération (recuperation_p4_v1.sh, lignes 399 à 438, extraites telles quelles
# dans un harnais : le reste de la récupération lit les textes de P3, que ce banc ne lit jamais). Faux outil de location
# (n'appelle aucun service ; journalise ses verbes) ; faux sleep qui journalise la durée demandée ; HOME redirigé ; clé
# d'API retirée ; jetons factices. N'écrit que sous RACINE_NEUVE.
# Usage : banc_depense_arrets_v1.sh RACINE_NEUVE
set -uo pipefail
[ $# -eq 1 ] || { echo "usage : banc_depense_arrets_v1.sh RACINE_NEUVE"; exit 2; }
E=$(realpath -m "$1")
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
for x in /usr/bin/vastai /bin/vastai /usr/local/bin/vastai; do [ -e "$x" ] && { echo "vastai réel présent ($x) : banc refusé"; exit 2; }; done
CH=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine
SURV=$CH/surveiller_p4_v1.sh; RECUP=$CH/recuperation_p4_v1.sh
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }
echo "banc de relecture (dépense et arrêts) : surveillance et destruction, v1"
for f in "$SURV" "$RECUP" "$0"; do echo "fichier relu : $(basename "$f") $(sha256sum "$f" | cut -d' ' -f1)"; done
mkdir -p "$E/bin" "$E/home" || exit 2
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location : n'appelle aucun service
J=${FAUX_JOURNAL:?}; C=${FAUX_COMPTEUR:?}
echo "appel : $*" >> "$J"
n=$(cat "$C" 2>/dev/null || echo 0); n=$((n + 1)); echo "$n" > "$C"
case "$1 $2" in
  "show instance")
      if [ -n "${FAUX_TERMINAL_APRES:-}" ] && [ "$n" -gt "$FAUX_TERMINAL_APRES" ]; then s=exited; c=stopped; else s=${FAUX_ETAT:-running}; c=${FAUX_CUR:-running}; fi
      printf '{"id": %s, "label": "%s", "actual_status": "%s", "cur_state": "%s", "intended_status": "running", "status_msg": "essai"}\n' "$3" "${FAUX_ETIQUETTE:-p4-v1}" "$s" "$c" ;;
  "logs "*)
      if [ -n "${FAUX_FIN_APRES:-}" ] && [ "$n" -gt "$FAUX_FIN_APRES" ]; then echo "AMORCE 2026-10-20T12:00:00Z : commit abc"; echo "AMORCE 2026-10-20T13:00:00Z : fin, code 0"
      else echo "AMORCE 2026-10-20T12:00:00Z : commit abc"; fi ;;
  "destroy instance") echo "TENTATIVE DE DESTRUCTION $3" >> "$J"; [ "${FAUX_CODE_DESTRUCTION:-0}" = 0 ] && echo "DESTRUCTION $3" >> "$J"; exit "${FAUX_CODE_DESTRUCTION:-0}" ;;
  "show instances") [ -n "${FAUX_LISTE_ILLISIBLE:-}" ] && { echo "erreur" >&2; exit 1; }; printf '%s\n' "${FAUX_LISTE:-[]}" ;;
  "stop instance") echo "ARRET $3" >> "$J" ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin/vastai"
cat > "$E/bin/sleep" <<'EOF'
#!/usr/bin/env bash
# faux sleep : journalise la durée demandée et le temps qui reste avant le plafond, puis rend la main (ou échoue comme le vrai)
echo "sleep $* ; reste avant le plafond : $(( ${FAUX_PLAFOND:-0} - $(date -u +%s) )) s" >> "${FAUX_JOURNAL:?}"
[[ "$1" =~ ^[0-9]+$ ]] || { echo "sleep: invalid time interval '$1'" >&2; exit 1; }
exit 0
EOF
chmod +x "$E/bin/sleep"
NON=0; N=0
surv() {   # $1 nom ; $2 décalage de la création (s avant maintenant) ; puis l'environnement
    local nom=$1 avant=$2; shift 2; N=$((N + 1))
    : > "$E/j-$nom.txt"; rm -f "$E/n-$nom.txt"
    local cr=$(( $(date -u +%s) - avant ))
    local t0; t0=$(date +%s.%N)
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin:/usr/bin:/bin" HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 \
        FAUX_JOURNAL="$E/j-$nom.txt" FAUX_COMPTEUR="$E/n-$nom.txt" FAUX_PLAFOND=$((cr + 9600)) "$@" \
        timeout 60 bash "$SURV" 99999999 "$cr" "$E/s-$nom" > "$E/o-$nom.txt" 2>&1
    local c=$?
    echo "$nom : code $c ; durée $(printf '%.1f' "$(echo "$(date +%s.%N) - $t0" | bc)") s ; appels de l'outil $(grep -c '^appel' "$E/j-$nom.txt") ; arrêts demandés $(grep -c '^ARRET' "$E/j-$nom.txt") ; sleeps $(grep -c '^sleep' "$E/j-$nom.txt")"
    tail -1 "$E/o-$nom.txt" | sed 's/^/    | /' | couper 200
    grep '^sleep' "$E/j-$nom.txt" | head -2 | sed 's/^/    > /'
}
echo "== surveillance : fin de l'amorce, l'instance reste en marche"
surv S00-fin-instance-en-marche 600 FAUX_FIN_APRES=2
grep -q '^FIN : ' "$E/o-S00-fin-instance-en-marche.txt" && ! grep -q '^ARRET' "$E/j-S00-fin-instance-en-marche.txt" \
    && echo "    constat (RC-depense-01) : sortie « FIN » en code 0, aucun arrêt demandé, aucun état relu après la sortie : l'arrêt reste à la session" \
    || { echo "    ÉCART du banc"; NON=$((NON + 1)); }
echo "== surveillance : plafond atteint, l'instance reste en marche"
surv S01-plafond-instance-en-marche 9700
grep -q '^PLAFOND' "$E/o-S01-plafond-instance-en-marche.txt" && ! grep -q '^ARRET' "$E/j-S01-plafond-instance-en-marche.txt" \
    && echo "    constat (RC-depense-01) : « PLAFOND » écrit, aucun arrêt demandé : la borne de 9 600 s ne tient que si la session agit" \
    || { echo "    ÉCART du banc"; NON=$((NON + 1)); }
echo "== surveillance : intervalle plus long que le temps restant (dépassement du plafond)"
surv S02-intervalle-9000-a-10-s-du-plafond 9590 INTERVALLE=9000 FAUX_FIN_APRES=2
grep -q '^sleep 9000 ' "$E/j-S02-intervalle-9000-a-10-s-du-plafond.txt" \
    && echo "    constat (RC-depense-06) : sommeil de 9 000 s demandé à moins de 10 s du plafond : la sortie « PLAFOND » arriverait 2,5 h trop tard" \
    || { echo "    ÉCART du banc"; NON=$((NON + 1)); }
echo "== surveillance : intervalle illisible"
surv S03-intervalle-illisible 600 INTERVALLE=abc FAUX_TERMINAL_APRES=40
n3=$(grep -c '^sleep abc' "$E/j-S03-intervalle-illisible.txt")
[ "$n3" -ge 10 ] && echo "    constat (RC-depense-06) : INTERVALLE=abc accepté au départ ; $n3 sommeils en échec, boucle sans pause (appels de l'outil en rafale) jusqu'à l'état terminal" \
    || { echo "    ÉCART du banc"; NON=$((NON + 1)); }
echo "== surveillance : instance d'une autre étiquette"
surv S04-etiquette-autre 600 FAUX_ETIQUETTE=rr-autre-projet FAUX_FIN_APRES=2
grep -q '^FIN : ' "$E/o-S04-etiquette-autre.txt" && echo "    constat (RC-depense-06) : l'étiquette n'est jamais relue : une surveillance lancée sur un identifiant faux suit une autre instance" \
    || { echo "    ÉCART du banc"; NON=$((NON + 1)); }
# bloc de destruction de la récupération, extrait tel quel (lignes 399 à 438)
sed -n '399,438p' "$RECUP" > "$E/bloc-destruction.sh"
head -1 "$E/bloc-destruction.sh" | grep -q '^# 8. destruction' && tail -1 "$E/bloc-destruction.sh" | grep -q 'INSTANCE DÉTRUITE PAR SON IDENTIFIANT (\$ID)"; fi$' \
    || { echo "bloc de destruction introuvable aux lignes 399 à 438 : banc refusé"; exit 2; }
echo "bloc de destruction extrait (lignes 399 à 438) : $(sha256sum "$E/bloc-destruction.sh" | cut -d' ' -f1)"
destr() {   # $1 nom ; $2 attendu (« détruite » ou « gardée ») ; $3 échecs avant le bloc ; $4 constat si écart ; puis l'environnement
    local nom=$1 attendu=$2 avant=$3 constat=$4; shift 4; N=$((N + 1))
    : > "$E/j-$nom.txt"; rm -f "$E/n-$nom.txt"; mkdir -p "$E/trav-$nom"
    { echo 'set -uo pipefail'; echo "echecs=$avant; ID=99999999; ETIQUETTE=p4-v1; TRAV='$E/trav-$nom'; SANS_RUN=non"
      echo 'ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echecs=$((echecs + 1)); }'; cat "$E/bloc-destruction.sh"; } > "$E/harnais-$nom.sh"
    env -u VAST_API_KEY HOME="$E/home" FAUX_JOURNAL="$E/j-$nom.txt" FAUX_COMPTEUR="$E/n-$nom.txt" "$@" bash "$E/harnais-$nom.sh" > "$E/o-$nom.txt" 2>&1
    local c=$? d; d=$(grep -c '^DESTRUCTION' "$E/j-$nom.txt")
    local v=CONFORME
    if [ "$attendu" = détruite ]; then { [ "$c" = 0 ] && [ "$d" = 1 ] && tail -1 "$E/o-$nom.txt" | grep -q "INSTANCE DÉTRUITE PAR SON IDENTIFIANT"; } || v="ÉCART (attendu : détruite) $constat"
    else { [ "$c" = 1 ] && tail -1 "$E/o-$nom.txt" | grep -q "NON DÉTRUITE : NŒUD DE LAZAR"; } || v="ÉCART (attendu : gardée, code 1) $constat"; fi
    [ "$v" = CONFORME ] || NON=$((NON + 1))
    echo "$nom : code $c ; destructions réussies $d (tentatives $(grep -c '^TENTATIVE' "$E/j-$nom.txt")) ; états relus $(grep -c '^appel : show instance ' "$E/j-$nom.txt") ; $v"
    grep -v '^$' "$E/o-$nom.txt" | tail -2 | sed 's/^/    | /' | couper 220
}
echo "== destruction (récupération, point 8)"
destr D00-sain détruite 0 "" PATH="$E/bin:/usr/bin:/bin"
destr D01-etiquette-autre gardée 0 "" PATH="$E/bin:/usr/bin:/bin" FAUX_ETIQUETTE=rr-autre-projet
destr D02-etiquette-p4-v1-suivie-d-un-mot gardée 0 "RC-depense-07" PATH="$E/bin:/usr/bin:/bin" "FAUX_ETIQUETTE=p4-v1 rr-autre"
destr D03-destruction-en-echec gardée 0 "" PATH="$E/bin:/usr/bin:/bin" FAUX_CODE_DESTRUCTION=1
destr D04-encore-listee gardée 0 "" PATH="$E/bin:/usr/bin:/bin" 'FAUX_LISTE=[{"id": 99999999}]'
destr D05-liste-illisible-apres gardée 0 "" PATH="$E/bin:/usr/bin:/bin" FAUX_LISTE_ILLISIBLE=1
destr D06-outil-absent gardée 0 "" PATH=/usr/bin:/bin
destr D07-recuperation-en-echec-instance-en-marche gardée 1 "" PATH="$E/bin:/usr/bin:/bin" FAUX_ETAT=running FAUX_CUR=running
[ "$(grep -c '^appel' "$E/j-D07-recuperation-en-echec-instance-en-marche.txt")" = 0 ] \
    && echo "    constat (RC-depense-02) : récupération en échec, instance en marche : aucun état relu, aucun arrêt ; le message ne dit pas que l'instance tourne" \
    || { echo "    ÉCART du banc"; NON=$((NON + 1)); }
FUITES=$(grep -l 'factice-hf\|factice-gh' "$E"/o-*.txt "$E"/j-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton factice affiché" || echo "jeton factice affiché dans : $FUITES"
echo "FIN DU BANC DE RELECTURE DE LA SURVEILLANCE ET DE LA DESTRUCTION : $N cas ; écarts du banc ou au texte : $NON"
