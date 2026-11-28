#!/usr/bin/env bash
# Banc du vérificateur neuf (lentille « dépense et arrêts ») : artefacts de l'arrêt, de la surveillance et de la
# récupération de la chaîne v2 hors de ceux des bancs du correcteur. Faux outil de location, faux sleep, faux df, faux
# git (aucun service appelé, aucun réseau) ; HOME redirigé ; jetons factices (jamais affichés).
# Usage : banc_arrets_verif_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
HN=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E/bin" "$E/bin-temps" "$E/bin-df" "$E/bin-git" || exit 2
for s in arreter_p4_v1.sh surveiller_p4_v1.sh recuperation_p4_v1.sh; do echo "script éprouvé : $s $(sha256sum "$HN/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
ID=99999999
cat > "$E/bin/vastai" <<'F'
#!/usr/bin/env bash
# faux outil : étiquette JSON brute (fichier etiquette-json, défaut "p4-v1") ; état avant l'arrêt (avant) ; après (apres)
S=${SCENARIO:?}
case "$1 $2" in
  "show instance")
    echo "show instance $3" >> "$S/outil.txt"
    labj=$(cat "$S/etiquette-json" 2>/dev/null || echo '"p4-v1"')
    if [ -e "$S/arrete" ]; then e=$(cat "$S/apres" 2>/dev/null || echo "exited stopped"); else e=$(cat "$S/avant" 2>/dev/null || echo "running running"); fi
    set -- $e
    printf '{"id": 99999999, "label": %s, "actual_status": "%s", "cur_state": "%s", "extra_env": [["GH_TOKEN", "factice-gh-verif-0001"]]}\n' "$labj" "$1" "$2" ;;
  "stop instance") echo "stop instance $3" >> "$S/outil.txt"; touch "$S/arrete"; echo '{"success": true}' ;;
  "destroy instance") echo "destroy instance $3" >> "$S/outil.txt"; echo '{"success": true}' ;;
  "show instances") echo "show instances" >> "$S/outil.txt"; echo '[]' ;;
  logs) echo "logs" >> "$S/outil.txt"; cat "$S/journal" 2>/dev/null ;;
  *) echo "verbe inattendu : $*" >> "$S/outil.txt"; exit 9 ;;
esac
F
printf '#!/usr/bin/env bash\necho "$1" >> "${SCENARIO:?}/sommeils"\n' > "$E/bin-temps/sleep"
printf '#!/usr/bin/env bash\nprintf "Filesystem 1024-blocks Used Available Capacity Mounted\\n/dev/x 10000000 100 %%s 1%%%% /\\n" "${FAUX_LIBRE:-9000000}"\n' > "$E/bin-df/df"
printf '#!/usr/bin/env bash\necho "git $*" >> "${SCENARIO:?}/git.txt"\n[ "$1" = clone ] && { echo "fatal: clonage factice refusé (aucun réseau)" >&2; exit 128; }\nexit 1\n' > "$E/bin-git/git"
chmod +x "$E/bin/vastai" "$E/bin-temps/sleep" "$E/bin-df/df" "$E/bin-git/git"
ECARTS=0
verdict() {   # $1 nom, $2 attendu (texte), $3 observé (texte), $4 0 si conforme
    local v=CONFORME; [ "$4" = 0 ] || { v="ÉCART"; ECARTS=$((ECARTS + 1)); }
    echo "$1 : observé : $3 ; attendu : $2 ; $v"
}
P="$E/bin-temps:$E/bin:/usr/bin:/bin"
arret() {   # $1 nom, $2 étiquette JSON ; sortie : code et demandes d'arrêt
    local sc="$E/scenario-$1"; mkdir -p "$sc"; printf '%s' "$2" > "$sc/etiquette-json"
    env -i PATH="$P" HOME="$E" LANG=C.UTF-8 SCENARIO="$sc" bash "$HN/arreter_p4_v1.sh" "$ID" "$E/arret-$1" > "$E/sortie-$1.txt" 2>&1; local c=$?
    local ns; ns=$(grep -c '^stop instance' "$sc/outil.txt" 2>/dev/null); echo "$c ${ns:-0} $(wc -l < "$sc/sommeils" 2>/dev/null || echo 0)"
}
# A. étiquette comparée entière : variantes non éprouvées par le correcteur
set -- $(arret AX01-etiquette-p4-v1-saut-de-ligne '"p4-v1\n"')
verdict AX01-etiquette-p4-v1-saut-de-ligne "code 2, aucune demande d'arrêt" "code $1, $2 demande(s) d'arrêt, $3 sommeil(s)" "$([ "$1" = 2 ] && [ "$2" = 0 ] && echo 0 || echo 1)"
tail -1 "$E/sortie-AX01-etiquette-p4-v1-saut-de-ligne.txt" | cut -c1-200 | sed 's/^/    | /'
set -- $(arret AX02-etiquette-majuscules '"P4-V1"')
verdict AX02-etiquette-majuscules "code 2, aucune demande d'arrêt" "code $1, $2 demande(s) d'arrêt" "$([ "$1" = 2 ] && [ "$2" = 0 ] && echo 0 || echo 1)"
set -- $(arret AX03-etiquette-espace-final '"p4-v1 "')
verdict AX03-etiquette-espace-final "code 2, aucune demande d'arrêt" "code $1, $2 demande(s) d'arrêt" "$([ "$1" = 2 ] && [ "$2" = 0 ] && echo 0 || echo 1)"
set -- $(arret AX04-etiquette-nombre '41')
verdict AX04-etiquette-nombre "code 2, aucune demande d'arrêt" "code $1, $2 demande(s) d'arrêt" "$([ "$1" = 2 ] && [ "$2" = 0 ] && echo 0 || echo 1)"
set -- $(arret AX05-sain '"p4-v1"')
verdict AX05-sain "code 0, une demande d'arrêt" "code $1, $2 demande(s) d'arrêt" "$([ "$1" = 0 ] && [ "$2" = 1 ] && echo 0 || echo 1)"
# B. surveillance : étiquette relue au départ, variante « p4-v1\n »
T="$E/traces"; mkdir -p "$T"
NOW=$(date -u +%s)
printf 'commit %s\ncreation %s\nsuccès : True ; identifiant %s ; message : essai\n' "$(printf 'a%.0s' {1..40})" "$((NOW - 9700))" "$ID" > "$T/lancement.txt"
surv() {   # $1 nom, $2 étiquette JSON
    local sc="$E/scenario-$1"; mkdir -p "$sc"; printf '%s' "$2" > "$sc/etiquette-json"
    env -i PATH="$P" HOME="$E" LANG=C.UTF-8 SCENARIO="$sc" HF_TOKEN=factice-hf-verif-0001 CONTROLE_IA_GITHUB_TOKEN=factice-gh-verif-0001 INTERVALLE=10 \
        timeout 60 bash "$HN/surveiller_p4_v1.sh" "$ID" "$T" "$E/surv-$1" > "$E/sortie-$1.txt" 2>&1; local c=$?
    local ns; ns=$(grep -c '^stop instance' "$sc/outil.txt" 2>/dev/null); echo "$c ${ns:-0}"
}
set -- $(surv SX01-surveillance-etiquette-saut-de-ligne '"p4-v1\n"')
verdict SX01-surveillance-etiquette-saut-de-ligne "code 2 au départ (étiquette ≠ p4-v1), rien n'est surveillé ni arrêté" "code $1, $2 demande(s) d'arrêt" "$([ "$1" = 2 ] && [ "$2" = 0 ] && echo 0 || echo 1)"
tail -2 "$E/sortie-SX01-surveillance-etiquette-saut-de-ligne.txt" | cut -c1-220 | sed 's/^/    | /'
set -- $(surv SX02-surveillance-plafond-passe-sain '"p4-v1"')
verdict SX02-surveillance-plafond-passe-sain "code 0 (PLAFOND), une demande d'arrêt" "code $1, $2 demande(s) d'arrêt" "$([ "$1" = 0 ] && [ "$2" = 1 ] && echo 0 || echo 1)"
tail -1 "$E/sortie-SX02-surveillance-plafond-passe-sain.txt" | cut -c1-220 | sed 's/^/    | /'
# C. récupération : refus en code 2 avant le clone (place, clone) : état de l'instance et heure limite écrits ?
SR=$(printf 'a%.0s' {1..40})
recup() {   # $1 nom, puis l'environnement
    local n=$1; shift; local sc="$E/scenario-$n"; mkdir -p "$sc"
    env -i PATH="$E/bin-git:$E/bin-df:$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$sc" HF_TOKEN=factice-hf-verif-0001 \
        CONTROLE_IA_GITHUB_TOKEN=factice-gh-verif-0001 "$@" timeout 120 bash "$HN/recuperation_p4_v1.sh" "$SR" "$ID" "$T" "$E/recup-$n" > "$E/sortie-$n.txt" 2>&1; local c=$?
    local lim; lim=$(grep -c "heure limite de destruction" "$E/sortie-$n.txt"); local etat; etat=$(grep -c "^show instance" "$sc/outil.txt" 2>/dev/null)
    local d; d=$(grep -c "^destroy" "$sc/outil.txt" 2>/dev/null)
    echo "$c ${lim:-0} ${etat:-0} ${d:-0}"
}
set -- $(recup RX01-place-insuffisante FAUX_LIBRE=2900000)
verdict RX01-place-insuffisante "code 2, rien de cloné ni détruit ; état de l'instance et heure limite écrits (décision RC-depense-02, texte : « Récupération en échec : … écrit l'état de l'instance et l'heure limite »)" "code $1, ligne d'heure limite $2, état relu $3 fois, destruction $4" "$([ "$1" = 2 ] && [ "$2" -ge 1 ] && [ "$4" = 0 ] && echo 0 || echo 1)"
tail -2 "$E/sortie-RX01-place-insuffisante.txt" | cut -c1-220 | sed 's/^/    | /'
set -- $(recup RX02-clonage-impossible FAUX_LIBRE=9000000)
verdict RX02-clonage-impossible "code 2, rien de détruit ; état de l'instance et heure limite écrits" "code $1, ligne d'heure limite $2, état relu $3 fois, destruction $4" "$([ "$1" = 2 ] && [ "$2" -ge 1 ] && [ "$4" = 0 ] && echo 0 || echo 1)"
tail -2 "$E/sortie-RX02-clonage-impossible.txt" | cut -c1-220 | sed 's/^/    | /'
grep -q "^git clone" "$E/scenario-RX02-clonage-impossible/git.txt" && echo "    RX02 : clone demandé au faux git (aucun réseau) : vu" || echo "    RX02 : clone non demandé"
FUITES=$(grep -rl "factice-gh-verif\|factice-hf-verif" "$E"/sortie-*.txt 2>/dev/null | head -3 || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { echo "JETON AFFICHÉ : $FUITES"; ECARTS=$((ECARTS + 1)); }
echo "FIN DU BANC DES ARRÊTS (VÉRIFICATEUR) ; écarts : $ECARTS"
