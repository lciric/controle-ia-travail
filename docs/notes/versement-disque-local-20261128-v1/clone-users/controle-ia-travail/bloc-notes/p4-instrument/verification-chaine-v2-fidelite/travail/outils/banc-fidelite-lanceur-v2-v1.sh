#!/usr/bin/env bash
# Banc du vérificateur « fidélité » de la chaîne v2 (v1) : lanceur v2 réel (copie dont seules DEPOT, B et V changent),
# mise en place reprise telle quelle de essais_lanceur_p4_v1.sh (lignes 1 à 186), sauf le texte de S : le candidat 2
# d essai réel (variable C2) au lieu du texte tiré du brouillon 4. Cas : révocations consignées pendant l appel,
# identifiant par identifiant et registre par registre (RC-fidelite-03) ; formes voisines ; mention libre (témoin) ;
# alerte à 120 USD ; accord présent dans l arbre de S (RC-fidelite-08). Faux outils, aucun service, aucun réseau.
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
cp "${C2:?C2 absent}" "$E/prereg-origine.md" || { echo "texte d essai impossible"; exit 2; }
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
G=registres/go.md; DD=registres/decisions.md
remettre() { cp "$E/decisions-sauve.md" registres/decisions.md; cp "$E/go-sauve.md" registres/go.md; }
RELU="GO et dépense relus juste avant la création"
cas F00-sain 0 - FAUX_X=1; remettre
MOTIF_CAS="$RELU" cas F01-revocation-de-GO-2026-10-20-07-au-registre-des-go-pendant-l-appel 2 - FAUX_FICHIER_PENDANT="$E/depot/$G" \
    "FAUX_LIGNE_PENDANT=| GO-2026-10-20-96 | $JOUR | révocation | révoque GO-2026-10-20-07 (essai) | — | $JOUR | Lazar | essai |"; remettre
for x in GO-2026-10-04-08 GO-2026-10-20-06 R-262 R-269; do
    MOTIF_CAS="$RELU" cas "F02-revocation-de-$x-au-registre-des-go-pendant-l-appel" 2 - FAUX_FICHIER_PENDANT="$E/depot/$G" \
        "FAUX_LIGNE_PENDANT=| GO-2026-10-20-96 | $JOUR | révocation | révoque $x (essai) | — | $JOUR | Lazar | essai |"; remettre
done
for x in R-262 R-269; do
    MOTIF_CAS="$RELU" cas "F03-revocation-de-$x-au-registre-des-decisions-pendant-l-appel" 2 - FAUX_FICHIER_PENDANT="$E/depot/$DD" \
        "FAUX_LIGNE_PENDANT=| R-998 | $JOUR | **Révocation de $x** (essai) : délégation retirée. | essai |"; remettre
done
MOTIF_CAS="forme voisine" cas F04-type-Revocation-qui-nomme-GO-2026-10-20-06-pendant-l-appel 2 - FAUX_FICHIER_PENDANT="$E/depot/$G" \
    "FAUX_LIGNE_PENDANT=| GO-2026-10-20-96 | $JOUR | Révocation | révoque GO-2026-10-20-06 (essai) | — | $JOUR | Lazar | essai |"; remettre
MOTIF_CAS="forme voisine" cas F05-annulation-de-R-262-pendant-l-appel 2 - FAUX_FICHIER_PENDANT="$E/depot/$DD" \
    "FAUX_LIGNE_PENDANT=| R-998 | $JOUR | Annulation de la délégation R-262 (essai). | essai |"; remettre
MOTIF_CAS="forme voisine" cas F06-retrait-de-R-269-pendant-l-appel 2 - FAUX_FICHIER_PENDANT="$E/depot/$DD" \
    "FAUX_LIGNE_PENDANT=| R-998 | $JOUR | Retrait de R-269 (essai). | essai |"; remettre
cas F07-mention-libre-de-R-269-temoin 0 - FAUX_FICHIER_PENDANT="$E/depot/$DD" \
    "FAUX_LIGNE_PENDANT=| R-998 | $JOUR | Lazar relit R-269 ; rien ne change (essai). | essai |"; remettre
sed -i "s/dépense consignée 47,83 USD + borne 5,41 USD = 53,24 USD < 150 USD/dépense consignée 115,00 USD + borne 5,41 USD = 120,41 USD < 150 USD/" registres/decisions.md
MOTIF_CAS="ALERTE : 120 USD atteints ou dépassés" cas F08-alerte-a-120-usd 0 - FAUX_X=1
echo "    F08 : lignes d'accord écrites dans lancement.txt : $(grep -c '^accord ' "$E/lancement-F08-alerte-a-120-usd.txt" 2>/dev/null) ; dont avec ALERTE : $(grep -c '^accord .*ALERTE' "$E/lancement-F08-alerte-a-120-usd.txt" 2>/dev/null)"
remettre
# RC-fidelite-08 : accord déjà dans l'arbre de S (S refait après l'accord)
git rm -q "$P" "$P.sha256" && git commit -qm "essai : retrait du préenregistrement" || exit 2
cp "$E/prereg-origine.md" "$P" && (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
git add "$P" "$P.sha256" && git commit -qm "essai : S refait après l'accord" && git push -q origin HEAD:main && git fetch -q origin || exit 2
grep -q "^| R-999 |" registres/decisions.md && echo "    F09 : accord R-999 dans l'arbre du S refait : oui"
MOTIF_CAS="déjà présent dans registres/decisions.md au commit S" cas F09-accord-dans-l-arbre-de-s 2 - FAUX_X=1
cd "$E" && rm -rf "$E/depot" "$E/distant.git" "$E/B" "$E/traces"
echo "FIN DU BANC DU VÉRIFICATEUR (lanceur v2, candidat 2 d'essai) ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ]
