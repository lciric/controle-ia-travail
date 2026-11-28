#!/usr/bin/env bash
# Rejeu, par le vérificateur neuf, des cas « dépense et arrêts » du banc du lanceur de la chaîne v2 : lignes 2 à 186
# (en-tête), 310 à 341 (révocation hors tête, pendant l'appel, formes voisines, garde gelée), 355 à 361 (accord),
# définition de nouveau_s, 396 à 416 (accord dans S, un accord un lancement, lancement.txt) et 474 à 478 (fin) de
# chaine-v2/essais_lanceur_p4_v1.sh (1c80fe4b…), recopiées TELLES QUELLES.
# Usage : banc_lanceur_rejeu_v1.sh DEPOT_SOURCE C RACINE_NEUVE
# Banc du lanceur de P4-instrument (R5), v1, décliné de docs/procedures/P3-premier-test-v2/essais_lanceur_p3_v1.sh sous un
# nom neuf (R12) : cas génériques repris (heure, place, contrôles, jetons, arguments, instances tolérées et autres
# projets, crédit, choix de l'offre la moins chère parmi les conformes avec ses pièges, offres relues gardées, création
# douteuse, jeton masqué, S absent du distant, fetch en échec, amorce non citée, branche autre, preuves des essais,
# dossier de traces relatif), plus les cas propres à P4 : vingt et un scripts de la chaîne (v2) égaux à leurs copies versées à
# S ; script de l'instance cité ; crédit sur 3,0 heures ; borne de l'étape recalculée (5,41 USD) ; instance 56799469
# tolérée seulement relue arrêtée ; GO cité GO-2026-10-20-07 seul (texte), d'un autre type, plafond sans le préfixe
# « 10 USD par lancement », échu ; révocation sous ses deux formes (ligne de GO de type « révocation » qui nomme chacun
# des cinq identifiants ; ligne R-… qui commence par « **Révocation de R-262** » ou « **Révocation de R-269** ») et ses
# cas sains ; accord du jour (absent, d'un autre jour, sans la forme exacte, sans citation du GO ni d'un message du
# jour, en double ; cas sain par message du jour) ; contrôle du module par sa ligne de commande (fichier du module
# changé dans le dépôt de travail) ; garde de calcul gelée rejouée sur la commande de création qui refuse une
# révocation consignée pendant l'appel (aucune création). Aucun appel réel n'est possible : faux outil de location
# (n'appelle aucun service ; journalise le verbe, l'étiquette et les variables non secrètes de --env, jamais un jeton),
# faux contrôles avant dépense, faux df (place disque fixée par le banc), HOME redirigé, clé d'API retirée, jetons
# factices. Dépôt d'essai : clone partagé de DEPOT_SOURCE au commit C (code, module de P4, registres réels, garde
# gelée), sans extraction des PDF ; copies versées des vingt et un scripts (celle du
# lanceur : celle du banc, dont seules les lignes DEPOT, B et V changent) et huit journaux de preuve factices ; S :
# préenregistrement d'essai tiré du brouillon 4 (outils_essais_p4_v1.py) et son sceau ; dépôt nu local en guise de
# dépôt distant. Le module de P4 et le module commun sont réels : chaque appel du lanceur les joue.
# Chaîne v2 : l'accord du jour est committé APRÈS S (un accord présent dans l'arbre de S est refusé, RC-fidelite-08) ;
# accord à la forme de la dépense de la phase (RC-depense-05 ; plafond de la phase dépassé, GO voisin : refus) ;
# révocations sous des formes voisines (code 2, RC-depense-03) ; révocation consignée pendant l'appel, sous ses deux
# formes exactes et sous une forme voisine, vue par le rejeu du GO juste avant la création (RC-depense-08) ; garde
# gelée modifiée ou absente (RC-depense-04) ; un accord, un lancement : second lancement du même S, marqueur d'un
# dossier de traces voisin, branche présente sur le dépôt distant (RC-depense-10) ; lancement.txt aux lignes doublées
# ou à l'écriture impossible avant la création (RC-depense-11) ; vingt et un scripts égaux à leurs copies versées ;
# huit journaux de preuve. Le marqueur d'un cas est retiré avant le cas suivant (sauf où le banc le garde).
# Usage : essais_lanceur_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
[ $# -eq 3 ] || { echo "usage : essais_lanceur_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; E=$(realpath -m "$3")
SOI=$(realpath "$0")
HN=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2
B4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/P4-instrument-v1.md
VERSEES=docs/procedures/P4-instrument-v1
GO=GO-2026-10-20-07
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh
        repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh
        essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
export PYTHONDONTWRITEBYTECODE=1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
echo "script éprouvé : lancer_p4_v1.sh $(sha256sum "$HN/lancer_p4_v1.sh" | cut -d' ' -f1)"
echo "script éprouvé : verifications_p4_v1.py $(sha256sum "$HN/verifications_p4_v1.py" | cut -d' ' -f1)"
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
NON_CONFORMES=0
JOUR=$(date -u +%F); HIER=$(date -u -d yesterday +%F)
H=$E/B/p4-instrument/chaine-v2
mkdir -p "$H" "$E/bin-vastai" "$E/home" "$E/bin-heure" "$E/bin-df"
cat > "$E/bin-vastai/vastai" <<'EOF'
#!/usr/bin/env bash
# faux vastai du banc du lanceur de P4 : n'appelle aucun service
J=${FAUX_VASTAI_JOURNAL:?}
echo "appel : $1 $2" >> "$J"
case "$1 $2" in
  "search offers") [ -n "${FAUX_OFFRES:-}" ] && { printf '%s\n' "$FAUX_OFFRES"; exit 0; }; printf '[{"id": 111, "gpu_name": "%s", "gpu_ram": 81920, "num_gpus": 1, "machine_id": 7101, "host_id": 8101, "dph_total": %s, "cpu_name": "%s", "cpu_arch": "amd64", "cpu_cores": 128, "cpu_cores_effective": %s, "cpu_ram": %s, "inet_down_cost": %s, "storage_total_cost": %s}, {"id": 222, "dph_total": 0.9, "cpu_name": "AMD EPYC 7513 32-Core Processor"}]\n' "${FAUX_GPU:-A100 SXM4}" "${FAUX_PRIX:-1.10}" "${FAUX_CPU:-AMD EPYC 7513 32-Core Processor}" "${FAUX_COEURS:-32.0}" "${FAUX_RAM:-128886}" "${FAUX_TEL:-0.025}" "${FAUX_STO:-0.015}" ;;
  "show user") [ -n "${FAUX_REVOQUER_PENDANT:-}" ] && echo "| GO-2026-10-20-95 | $(date -u +%F) | révocation | révoque GO-2026-10-20-07 pendant l appel (essai) | — | $(date -u +%F) | Lazar | essai |" >> "$FAUX_REVOQUER_PENDANT"
      [ -n "${FAUX_FICHIER_PENDANT:-}" ] && printf '%s\n' "$FAUX_LIGNE_PENDANT" >> "$FAUX_FICHIER_PENDANT"
      [ -n "${FAUX_DOUBLER_COMMIT:-}" ] && echo "commit $(git -C "$FAUX_DEPOT" log --diff-filter=A -1 --format=%H -- prereg/P4-instrument-v1.md.sha256)" >> "$FAUX_DOUBLER_COMMIT/lancement.txt"
      [ -n "${FAUX_DISQUE_PLEIN:-}" ] && ln -sf /dev/full "$FAUX_DISQUE_PLEIN/lancement.txt"
      [ -n "${FAUX_USER_ILLISIBLE:-}" ] && { echo "erreur factice"; exit 0; }; printf '{"credit": %s, "email": "x@invalid"}\n' "${FAUX_CREDIT:-20.0}" ;;
  "show instances") [ -n "${FAUX_INSTANCES_ECHEC:-}" ] && { echo "erreur factice" >&2; exit 1; }; d='[{"id": 56799469, "actual_status": "exited", "cur_state": "stopped", "label": "p3-v1", "extra_env": [["GH_TOKEN", "secret"]]}]'; printf '%s\n' "${FAUX_INSTANCES:-$d}" ;;
  "create instance")
    echo "CREATION FACTICE" >> "$J"
    echo "offre créée $3" >> "$J"
    a=("$@")
    for ((i = 0; i < ${#a[@]}; i++)); do
      [ "${a[$i]}" = "--label" ] && echo "etiquette ${a[$((i + 1))]}" >> "$J"
      if [ "${a[$i]}" = "--env" ]; then
        for kv in ${a[$((i + 1))]}; do case "$kv" in ETUDE=*|PREREG=*|BRANCHE=*|DEPOT_URL=*) echo "env $kv" >> "$J" ;; COMMIT=*) echo "env COMMIT présent" >> "$J" ;; esac; done
      fi
    done
    echo "go ${GO_ID:-absent}" >> "$J"
    d='{"success": true, "new_contract": 99999999}'; printf '%s\n' "${FAUX_CREATION:-$d}"; exit "${FAUX_CODE_CREATION:-0}" ;;
  *) echo "verbe inattendu" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin-vastai/vastai"
cat > "$H/controles_avant_depense_p4_v1.sh" <<'EOF'
#!/usr/bin/env bash
mkdir -p "$2" "$2.travail" && echo donnees > "$2/x"
echo "arguments : S=${1:0:12} ; $# arguments"
[ $# = 2 ] || { echo "KO  essai : nombre d'arguments"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; }
if [ -n "${FAUX_KO:-}" ]; then echo "OK  essai"; echo "KO  essai : faute simulée"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; fi
if [ -n "${FAUX_DERNIERE:-}" ]; then echo "OK  essai"; echo "dernière ligne inattendue (essai)"; exit 0; fi
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
cp "$HN/verifications_p4_v1.py" "$H/"
L=$H/lancer_p4_v1.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" -e "s|^V=.*|V=$E/bin-vastai/vastai|" "$HN/lancer_p4_v1.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$HN/lancer_p4_v1.sh" "$L" | grep -c '^>') (DEPOT, B, V)"
[ "$(diff "$HN/lancer_p4_v1.sh" "$L" | grep -c '^>')" = 3 ] && ! grep -q "venv-vastai" "$L" || { echo "copie du lanceur non sûre"; exit 2; }
cat > "$E/bin-heure/date" <<EOF
#!/usr/bin/env bash
if [ "\$*" = "-u +%H%M" ]; then
  n=\$(cat "$E/compteur-heure" 2>/dev/null || echo 0); n=\$((n+1)); echo \$n > "$E/compteur-heure"
  if [ "\$n" -ge 2 ]; then echo "\${FAUX_HEURE2:-2200}"; else echo "\${FAUX_HEURE1:-2200}"; fi; exit 0
fi
exec /usr/bin/date "\$@"
EOF
chmod +x "$E/bin-heure/date"
# faux df : place disque fixée par le banc (la machine de la session peut avoir moins de 3 Go libres ; le lanceur réel
# en juge, pas le banc) ; 2 900 000 ko sur le dossier nommé par le cas
cat > "$E/bin-df/df" <<EOF
#!/usr/bin/env bash
libre=9000000
[ -n "\${FAUX_DF_TRACES:-}" ] && [ "\${@: -1}" = "$E" ] && libre=2900000
[ -n "\${FAUX_DF_BLOC_NOTES:-}" ] && [ "\${@: -1}" = "$E/B" ] && libre=2900000
printf 'Filesystem 1024-blocks Used Available Capacity Mounted\n/dev/x 10000000 100 %s 1%% /\n' "\$libre"
EOF
chmod +x "$E/bin-df/df"
git clone -q --shared --no-checkout "$SRC" "$E/depot" && cd "$E/depot" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git sparse-checkout set --no-cone '/*' '!/docs/sources/pdf/' '!/docs/sources/lecture-pdf-niveau1/' '!/docs/sources/lecture-pdf-niveau2/' \
    && git checkout -q "$C" && git checkout -q -B main || exit 2
echo "C = $(git rev-parse HEAD)"
grep -q "^| $GO |" registres/go.md || { echo "$GO absent du registre de C"; exit 2; }
FORME="dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 150 USD"
LIGNE_ACCORD="| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours ; $FORME. | essai |"
# copies versées à S des vingt et un scripts : les faux contrôles et le module commun du bloc-notes factice, le lanceur du
# banc, et les dix-huit autres scripts, au bloc-notes factice et en copie versée (le lanceur compare les vingt et un)
mkdir -p "$VERSEES"
cp "$H/controles_avant_depense_p4_v1.sh" "$H/verifications_p4_v1.py" "$L" "$VERSEES/"
for s in $CHAINE; do
    case "$s" in controles_avant_depense_p4_v1.sh|verifications_p4_v1.py|lancer_p4_v1.sh) continue ;; esac
    cp "$HN/$s" "$VERSEES/" && cp "$HN/$s" "$H/" || { echo "copie versée factice impossible : $s"; exit 2; }
done
for s in $CHAINE; do (cd "$VERSEES" && sha256sum "$s" > "$s.sha256"); done
ep() { for s in "$@"; do echo "script éprouvé : $s $(sha256sum "$VERSEES/$s" | cut -d' ' -f1)"; done; }
journal_preuve() {   # $1 nom du journal, $2 dernière ligne, puis les scripts éprouvés
    local n=$1 v=$2; shift 2
    { echo "journal factice du banc du lanceur"; ep "$@"; echo "$v"; } > "$VERSEES/$n"
    (cd "$VERSEES" && sha256sum "$n" > "$n.sha256")
}
journaux_preuves() {
    journal_preuve banc-lanceur-p4-v1.log "FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0" lancer_p4_v1.sh verifications_p4_v1.py essais_lanceur_p4_v1.sh
    journal_preuve banc-surveillance-p4-v1.log "FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0" surveiller_p4_v1.sh controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh essais_surveillance_p4_v1.sh
    journal_preuve banc-verifications-p4-v1.log "FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0" verifications_p4_v1.py essais_verifications_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve banc-controles-p4-v1.log "FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0" controles_avant_depense_p4_v1.sh verifications_p4_v1.py essais_controles_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve banc-scellement-p4-v1.log "FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0" sceller_p4_v1.sh verifications_p4_v1.py essais_scellement_p4_v1.sh outils_essais_p4_v1.py
    journal_preuve repetition-finale-p4-v1.log "RÉPÉTITION FINALE : CONFORME" sceller_p4_v1.sh controles_avant_depense_p4_v1.sh verifications_p4_v1.py repetition_finale_p4_v1.sh
    journal_preuve banc-arret-p4-v1.log "FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : 0" arreter_p4_v1.sh essais_arret_p4_v1.sh
    journal_preuve banc-traces-p4-v1.log "FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : 0" controler_traces_p4_v1.sh verifications_p4_v1.py essais_traces_p4_v1.sh outils_essais_p4_v1.py
}
journaux_preuves
git add -A "$VERSEES" && git commit -qm "essai : copies versées et journaux de preuve factices"
"$PY" -B "$HN/outils_essais_p4_v1.py" candidat "$B4" "$E/prereg-origine.md" . 7a54d431d89745839220f882b41b13e8c62ecfdd \
    "$(printf 0%.0s {1..64})" 1102 > /dev/null || { echo "texte d'essai impossible"; exit 2; }
cp "$E/prereg-origine.md" "$P" && (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
git add "$P" "$P.sha256" && git commit -qm "S : préenregistrement de P4 scellé (essai)"
S=$(git rev-parse HEAD); echo "S = $S"
# accord du jour consigné APRÈS S (Chaîne de lancement ; RC-fidelite-08)
echo "$LIGNE_ACCORD" >> registres/decisions.md && git add -A && git commit -qm "accord du jour consigné après S (essai)"
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
cp registres/decisions.md "$E/decisions-sauve.md"; cp registres/go.md "$E/go-sauve.md"
cas() {   # $1 nom ; $2 code attendu ; $3 arguments du lanceur (« - » : les arguments normaux) ; puis l'environnement
    local nom=$1 attendu=$2 args=$3; shift 3
    rm -rf "$E/traces" "$E/compteur-heure"; : > "$E/journal-$nom.txt"
    # un accord, un lancement : les marqueurs d'un cas précédent sont retirés, sauf si le cas les garde
    [ -n "${GARDER_MARQUEUR:-}" ] || { rm -rf "$E/B/p4-instrument/marqueurs-lancement-p4-v1"; rm -f "$E"/*/marqueur-lancement-*.txt; }
    local a=("$E/traces" - R-999); [ "$args" = "-" ] || read -r -a a <<<"$args"
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin-heure:$E/bin-df:/usr/bin:/bin" FAUX_DEPOT="$E/depot" \
        HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 FAUX_VASTAI_JOURNAL="$E/journal-$nom.txt" \
        "$@" bash "$L" "${a[@]}" > "$E/sortie-$nom.txt" 2>&1
    local c=$?
    local cree; cree=$(grep -c "CREATION FACTICE" "$E/journal-$nom.txt")
    local v="CONFORME"; [ "$c" = "$attendu" ] || v="NON CONFORME (attendu $attendu)"
    [ "$attendu" != 0 ] && [ "$cree" != 0 ] && [ "$attendu" != 4 ] && v="NON CONFORME (création alors qu'un arrêt était attendu)"
    [ "$attendu" = 0 ] && [ "$cree" != 1 ] && v="NON CONFORME (pas de création)"
    local tr; tr=$(realpath -m "${a[0]:-$E/traces}")
    { [ -e "$tr/clone-controles" ] || [ -e "$tr/clone-controles.travail" ]; } && v="NON CONFORME (clone des contrôles resté)"
    [ -n "${MOTIF_CAS:-}" ] && ! grep -qF -- "$MOTIF_CAS" "$E/sortie-$nom.txt" && v="NON CONFORME (motif « $MOTIF_CAS » absent)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; créations factices $cree ; $v"
    grep -v '^$' "$E/sortie-$nom.txt" | tail -2 | sed 's/^/    | /' | couper 200
    [ -f "$tr/lancement.txt" ] && cp "$tr/lancement.txt" "$E/lancement-$nom.txt"
    [ -f "$tr/reponse-masquee.txt" ] && cp "$tr/reponse-masquee.txt" "$E/reponse-$nom.txt"
    return 0
}
echo "| R-994 | $JOUR | Note (essai) : la forme « **Révocation de R-269** » est décrite ici, sans révoquer. | essai |" >> registres/decisions.md
cas G05b-forme-de-revocation-ailleurs-qu-en-tete 0 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
# garde de calcul gelée rejouée sur la commande de création : une révocation consignée pendant l'appel (après les
# contrôles du GO, avant la création) est refusée par la garde ; aucune création
MOTIF_CAS="GO et dépense relus juste avant la création : révocation au registre des GO (GO-2026-10-20-95)" cas G06-revocation-du-go-cite-pendant-l-appel 2 - FAUX_REVOQUER_PENDANT="$E/depot/registres/go.md"
cp "$E/go-sauve.md" registres/go.md
# chaîne v2 (RC-depense-08) : révocations des autres identifiants consignées pendant l'appel (après les contrôles du GO,
# avant la création) : vues par le rejeu du GO sur les registres courants juste avant la création ; aucune création
MOTIF_CAS="GO et dépense relus juste avant la création : révocation au registre des GO (GO-2026-10-21-05)" cas L31-revocation-de-la-phase-pendant-l-appel 2 - \
    FAUX_FICHIER_PENDANT="$E/depot/registres/go.md" "FAUX_LIGNE_PENDANT=| GO-2026-10-21-05 | $JOUR | révocation | révoque GO-2026-10-04-08 (essai) | — | $JOUR | Lazar | essai |"
cp "$E/go-sauve.md" registres/go.md
MOTIF_CAS="GO et dépense relus juste avant la création : révocation au registre des décisions (R-998)" cas L30-revocation-de-r-269-pendant-l-appel 2 - \
    FAUX_FICHIER_PENDANT="$E/depot/registres/decisions.md" "FAUX_LIGNE_PENDANT=| R-998 | $JOUR | **Révocation de R-269** (essai). | essai |"
cp "$E/decisions-sauve.md" registres/decisions.md
MOTIF_CAS="révocation possible sous une forme voisine" cas L32-forme-voisine-pendant-l-appel 2 - \
    FAUX_FICHIER_PENDANT="$E/depot/registres/decisions.md" "FAUX_LIGNE_PENDANT=| R-998 | $JOUR | **Révocation de R-262 et de R-269** (essai). | essai |"
cp "$E/decisions-sauve.md" registres/decisions.md
# chaîne v2 (RC-depense-03) : révocations sous des formes voisines consignées avant l'appel : code 2, aucune création
echo "|GO-2026-10-21-01|$JOUR|révocation|révoque GO-2026-10-04-08 (essai)|—|$JOUR|Lazar|essai|" >> registres/go.md
MOTIF_CAS="révocation possible sous une forme voisine" cas L20-ligne-de-go-sans-espace 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
echo "| GO-2026-10-21-01 | $JOUR | Révocation | révoque R-262 (essai) | — | $JOUR | Lazar | essai |" >> registres/go.md
MOTIF_CAS="révocation possible sous une forme voisine" cas L21-type-a-majuscule 2 - FAUX_X=1; cp "$E/go-sauve.md" registres/go.md
echo "| R-998 | $JOUR | **Révocation de la délégation R-269** (essai). | essai |" >> registres/decisions.md
MOTIF_CAS="révocation possible sous une forme voisine" cas L22-delegation-nommee 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
echo "|R-998|$JOUR|**Révocation de R-262** (essai).|essai|" >> registres/decisions.md
MOTIF_CAS="révocation possible sous une forme voisine" cas L23-forme-exacte-sans-espace 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
# chaîne v2 (RC-depense-04) : garde de calcul gelée modifiée ou absente dans le dépôt de travail : aucun rejeu
cp .claude/hooks/garde_calcul.py "$E/garde-sauve.py"; echo "# modifiée (essai)" >> .claude/hooks/garde_calcul.py
MOTIF_CAS="garde de calcul modifiée" cas L40-garde-modifiee 2 - FAUX_X=1; cp "$E/garde-sauve.py" .claude/hooks/garde_calcul.py
rm -f .claude/hooks/garde_calcul.py
MOTIF_CAS="garde de calcul modifiée" cas L41-garde-absente 2 - FAUX_X=1; cp "$E/garde-sauve.py" .claude/hooks/garde_calcul.py
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "dépôt d'essai non rétabli après L41"; exit 2; }
# chaîne v2 : forme de la dépense de la phase (RC-depense-05) ; GO à frontières de mot (RC-depense-09)
sed -i "s/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO ; dépense de la phase sous 150 USD. | essai |/" registres/decisions.md
MOTIF_CAS="forme « dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD » absente" cas A16-accord-sans-la-forme-de-la-depense 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "s/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO ; dépense consignée 148,00 USD + borne 5,41 USD = 153,41 USD < 150 USD. | essai |/" registres/decisions.md
MOTIF_CAS="la dépense de la phase atteindrait 150 USD ou plus" cas A17-plafond-de-la-phase-depasse 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
sed -i "s/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation GO-2026-10-20-071 ; $FORME. | essai |/" registres/decisions.md
MOTIF_CAS="qu'au sein d'un identifiant voisin" cas A18-accord-qui-cite-un-go-voisin 2 - FAUX_X=1; cp "$E/decisions-sauve.md" registres/decisions.md
nouveau_s() {   # $1 expression sed sur le préenregistrement (vide : texte d'origine) ; $2 « accord-dans-s » : l'accord
               # reste dans l'arbre de S (artefact) ; sinon il est retiré avant S et consigné de nouveau après S
    if [ "${2:-}" != accord-dans-s ]; then
        grep -q "^| R-999 |" registres/decisions.md && { sed -i '/^| R-999 |/d' registres/decisions.md && git commit -qam "essai : accord retiré avant le nouveau S"; }
    fi
    git rm -q "$P" "$P.sha256" && git commit -qm "essai : retrait du préenregistrement"
    mkdir -p "$(dirname "$P")" && cp "$E/prereg-origine.md" "$P" || { echo "nouveau S : copie impossible"; exit 2; }
    [ -n "$1" ] && { sed -i "$1" "$P"; cmp -s "$P" "$E/prereg-origine.md" && { echo "nouveau S : l'expression n'a rien changé"; exit 2; }; }
    (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
    git add "$P" "$P.sha256" && git commit -qm "essai : S refait" || { echo "nouveau S : commit impossible"; exit 2; }
    if [ "${2:-}" != accord-dans-s ]; then
        echo "$LIGNE_ACCORD" >> registres/decisions.md && git commit -qam "essai : accord consigné après le nouveau S" || { echo "nouveau S : accord impossible"; exit 2; }
    fi
    git push -q origin HEAD:main && git fetch -q origin || { echo "nouveau S : poussée impossible"; exit 2; }
}
nouveau_s ""
cas N00-sain-apres-retablissement 0 - FAUX_X=1
# chaîne v2 (RC-fidelite-08) : accord présent dans l'arbre de S (consigné avant le scellement) : refus
nouveau_s "" accord-dans-s
MOTIF_CAS="accord R-999 déjà présent dans registres/decisions.md au commit S" cas N10-accord-dans-l-arbre-de-s 2 - FAUX_X=1
nouveau_s ""
# chaîne v2 (RC-depense-10) : un accord, un lancement
cas M00-premier-lancement 0 - FAUX_X=1
GARDER_MARQUEUR=1 MOTIF_CAS="un accord, un lancement : un lancement a déjà été tenté pour le commit S" cas M01-second-lancement-du-meme-s 2 - FAUX_X=1
rm -rf "$E/B/p4-instrument/marqueurs-lancement-p4-v1"; mkdir -p "$E/ancien-lancement"
echo "marqueur d'un lancement précédent (essai)" > "$E/ancien-lancement/marqueur-lancement-$(git rev-parse HEAD~1).txt"
GARDER_MARQUEUR=1 MOTIF_CAS="un accord, un lancement : un lancement a déjà été tenté pour le commit S" cas M02-marqueur-dans-un-dossier-de-traces-voisin 2 - FAUX_X=1
rm -rf "$E/ancien-lancement"
git push -q "$E/distant.git" HEAD:refs/heads/calcul/p4-reel-v1 || exit 2
MOTIF_CAS="branche calcul/p4-reel-v1 : code 0 (2 attendu : absente du dépôt distant)" cas M03-branche-de-resultats-presente 2 - FAUX_X=1
git -C "$E/distant.git" branch -D calcul/p4-reel-v1 > /dev/null
[ ! -e "$E/B/p4-instrument/marqueurs-lancement-p4-v1/lancement-$(git rev-parse HEAD~1).txt" ] && echo "    M03 : aucun marqueur écrit sur un refus : CONFORME" \
    || { echo "    M03 : marqueur écrit malgré le refus : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# chaîne v2 (RC-depense-11) : lancement.txt relu avant de quitter le mode d'arrêt sur erreur
MOTIF_CAS="lancement.txt : ligne « commit " cas M20-ligne-commit-doublee-avant-l-ecriture 2 - FAUX_DOUBLER_COMMIT="$E/traces"
MOTIF_CAS="arrêt avant la création (ligne" cas M21-ecriture-de-lancement-impossible 2 - FAUX_DISQUE_PLEIN="$E/traces"
FUITES=$(grep -l 'secret\|factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/lancement-*.txt "$E"/journal-*.txt "$E"/reponse-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton affiché : CONFORME" || { printf '%s\n' $FUITES | sed 's/^/JETON AFFI''CHÉ : /'; NON_CONFORMES=$((NON_CONFORMES + 1)); }
P_CACHE=$(find "$E/depot/src" "$E/depot/$VERSEES" "$H" "$HN" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : $NON_CONFORMES"
