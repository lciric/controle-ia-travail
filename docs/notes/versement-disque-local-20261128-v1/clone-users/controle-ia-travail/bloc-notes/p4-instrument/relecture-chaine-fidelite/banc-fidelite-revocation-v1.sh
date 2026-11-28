#!/usr/bin/env bash
# Banc du relecteur « fidélité au texte » (v1) : une révocation consignée PENDANT l'appel du lanceur de P4, après la
# dernière lecture complète des révocations (lignes de commande du module, lancer_p4_v1.sh l. 159) et avant la création
# (l. 325), est-elle refusée ? Texte (brouillon 4, en-tête « GO et dépense », l. 58-61, et Liste d'arrêt, l. 624) :
# « révocation présente (formes de l'en-tête) : aucune création ». Le lanceur réel est joué tel quel (copie dont seules
# les lignes DEPOT, B et V changent, comme le banc du rédacteur) ; module de P4 et module commun réels ; faux outil de
# location (n'appelle aucun service), faux contrôles avant dépense, faux df, jetons factices, aucun réseau.
# Monté sur le même gabarit que essais_lanceur_p4_v1.sh (copie des blocs de mise en place), dans un dossier neuf.
# Usage : banc-fidelite-revocation-v1.sh RACINE_NEUVE
set -uo pipefail
[ $# -eq 1 ] || { echo "usage : banc-fidelite-revocation-v1.sh RACINE_NEUVE"; exit 2; }
E=$(realpath -m "$1"); SRC=/home/user/controle-ia-travail
HN=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine
MOD=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/module
B4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/P4-instrument-v1.md; VERSEES=docs/procedures/P4-instrument-v1; GO=GO-2026-10-20-07
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh recuperation_p4_v1.sh repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh
        essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
export PYTHONDONTWRITEBYTECODE=1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
echo "lanceur éprouvé : lancer_p4_v1.sh $(sha256sum "$HN/lancer_p4_v1.sh" | cut -d' ' -f1)"
echo "module commun : verifications_p4_v1.py $(sha256sum "$HN/verifications_p4_v1.py" | cut -d' ' -f1)"
echo "module de P4 : instrument_p4_v1.py $(sha256sum "$MOD/instrument_p4_v1.py" | cut -d' ' -f1)"
echo "garde gelée : garde_calcul.py $(sha256sum "$SRC/.claude/hooks/garde_calcul.py" | cut -d' ' -f1)"
JOUR=$(date -u +%F)
H=$E/B/p4-instrument/chaine
mkdir -p "$H" "$E/bin-vastai" "$E/home" "$E/bin-df"
# faux outil de location : le verbe « show user » (lu après les lignes de commande du module et la seconde relecture de
# l'accord, avant la garde gelée et la création) ajoute FAUX_LIGNE_PENDANT au fichier FAUX_FICHIER_PENDANT
cat > "$E/bin-vastai/vastai" <<'EOF'
#!/usr/bin/env bash
J=${FAUX_VASTAI_JOURNAL:?}
echo "appel : $1 $2" >> "$J"
case "$1 $2" in
  "search offers") printf '[{"id": 111, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "machine_id": 7101, "host_id": 8101, "dph_total": 1.10, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_arch": "amd64", "cpu_cores": 128, "cpu_cores_effective": 32.0, "cpu_ram": 128886, "inet_down_cost": 0.025, "storage_total_cost": 0.015}]\n' ;;
  "show user") if [ -n "${FAUX_FICHIER_PENDANT:-}" ]; then printf '%s\n' "$FAUX_LIGNE_PENDANT" >> "$FAUX_FICHIER_PENDANT"; echo "ligne consignée pendant l'appel" >> "$J"; fi
      printf '{"credit": 20.0, "email": "x@invalid"}\n' ;;
  "show instances") printf '[]\n' ;;
  "create instance") echo "CREATION FACTICE" >> "$J"; echo "go ${GO_ID:-absent}" >> "$J"; printf '{"success": true, "new_contract": 99999999}\n' ;;
  *) echo "verbe inattendu" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin-vastai/vastai"
cat > "$H/controles_avant_depense_p4_v1.sh" <<'EOF'
#!/usr/bin/env bash
mkdir -p "$2" "$2.travail" && echo donnees > "$2/x"
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
cat > "$E/bin-df/df" <<'EOF'
#!/usr/bin/env bash
printf 'Filesystem 1024-blocks Used Available Capacity Mounted\n/dev/x 10000000 100 9000000 1%% /\n'
EOF
chmod +x "$E/bin-df/df"
cp "$HN/verifications_p4_v1.py" "$H/"
L=$H/lancer_p4_v1.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" -e "s|^V=.*|V=$E/bin-vastai/vastai|" "$HN/lancer_p4_v1.sh" > "$L"
echo "lignes changées dans la copie du lanceur : $(diff "$HN/lancer_p4_v1.sh" "$L" | grep -c '^>') (DEPOT, B, V)"
[ "$(diff "$HN/lancer_p4_v1.sh" "$L" | grep -c '^>')" = 3 ] && ! grep -q "venv-vastai" "$L" || { echo "copie du lanceur non sûre"; exit 2; }
# dépôt d'essai : clone partagé du dépôt de travail (lu par référence, rien n'y est écrit), sans les PDF
git clone -q --shared --no-checkout "$SRC" "$E/depot" && cd "$E/depot" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git sparse-checkout set --no-cone '/*' '!/docs/sources/pdf/' '!/docs/sources/lecture-pdf-niveau1/' '!/docs/sources/lecture-pdf-niveau2/' \
    && git checkout -q HEAD && git checkout -q -B main || exit 2
echo "C (tête du dépôt de travail) = $(git rev-parse HEAD)"
grep -q "^| $GO |" registres/go.md || { echo "$GO absent du registre"; exit 2; }
echo "| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours. | essai |" >> registres/decisions.md
mkdir -p "$VERSEES"
cp "$MOD"/*.py "$MOD"/*.py.sha256 "$VERSEES/"
cp "$H/controles_avant_depense_p4_v1.sh" "$H/verifications_p4_v1.py" "$L" "$VERSEES/"
for s in $CHAINE; do
    case "$s" in controles_avant_depense_p4_v1.sh|verifications_p4_v1.py|lancer_p4_v1.sh) continue ;; esac
    cp "$HN/$s" "$VERSEES/" && cp "$HN/$s" "$H/" || { echo "copie impossible : $s"; exit 2; }
done
for s in $CHAINE; do (cd "$VERSEES" && sha256sum "$s" > "$s.sha256"); done
ep() { for s in "$@"; do echo "script éprouvé : $s $(sha256sum "$VERSEES/$s" | cut -d' ' -f1)"; done; }
jp() { local n=$1 v=$2; shift 2; { echo "journal factice"; ep "$@"; echo "$v"; } > "$VERSEES/$n"; (cd "$VERSEES" && sha256sum "$n" > "$n.sha256"); }
jp banc-lanceur-p4-v1.log "FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0" lancer_p4_v1.sh verifications_p4_v1.py essais_lanceur_p4_v1.sh
jp banc-surveillance-p4-v1.log "FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0" surveiller_p4_v1.sh controle_cinq_minutes_p4_v1.sh essais_surveillance_p4_v1.sh
jp banc-verifications-p4-v1.log "FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0" verifications_p4_v1.py essais_verifications_p4_v1.sh outils_essais_p4_v1.py
jp banc-controles-p4-v1.log "FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0" controles_avant_depense_p4_v1.sh verifications_p4_v1.py essais_controles_p4_v1.sh outils_essais_p4_v1.py
jp banc-scellement-p4-v1.log "FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0" sceller_p4_v1.sh verifications_p4_v1.py essais_scellement_p4_v1.sh outils_essais_p4_v1.py
jp repetition-finale-p4-v1.log "RÉPÉTITION FINALE : CONFORME" sceller_p4_v1.sh controles_avant_depense_p4_v1.sh verifications_p4_v1.py repetition_finale_p4_v1.sh
git add -A && git commit -qm "essai : module, copies versées, journaux factices, accord du jour" || exit 2
"$PY" -B "$HN/outils_essais_p4_v1.py" candidat "$B4" "$E/prereg-essai.md" . 7a54d431d89745839220f882b41b13e8c62ecfdd \
    "$(printf 0%.0s {1..64})" 1102 > /dev/null || { echo "texte d'essai impossible"; exit 2; }
cp "$E/prereg-essai.md" "$P" && (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
git add "$P" "$P.sha256" && git commit -qm "S : préenregistrement de P4 (essai)"
echo "S = $(git rev-parse HEAD)"
git clone -q --bare . "$E/distant.git" && git remote set-url origin "$E/distant.git" && git fetch -q origin || exit 2
cp registres/decisions.md "$E/decisions-sauve.md"; cp registres/go.md "$E/go-sauve.md"
N_ECARTS=0
cas() {   # $1 nom ; $2 « refus » attendu par le texte ou « création » ; puis l'environnement du cas
    local nom=$1 texte=$2; shift 2
    rm -rf "$E/traces"; : > "$E/journal-$nom.txt"
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin-df:/usr/bin:/bin" \
        HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 FAUX_VASTAI_JOURNAL="$E/journal-$nom.txt" \
        "$@" bash "$L" "$E/traces" - R-999 > "$E/sortie-$nom.txt" 2>&1
    local c=$? cree; cree=$(grep -c "CREATION FACTICE" "$E/journal-$nom.txt")
    local pendant; pendant=$(grep -c "ligne consignée pendant l'appel" "$E/journal-$nom.txt")
    local obs="création"; [ "$cree" = 0 ] && obs="refus"
    local v="conforme au texte"; [ "$obs" = "$texte" ] || { v="ÉCART AU TEXTE (le texte exige : $texte)"; N_ECARTS=$((N_ECARTS + 1)); }
    echo "$nom : code $c ; créations factices $cree ; ligne consignée pendant l'appel : $pendant ; observé : $obs ; $v"
    grep -v '^$' "$E/sortie-$nom.txt" | tail -2 | cut -c1-200 | sed 's/^/    | /'
    cp registres/decisions.md "$E/decisions-$nom.md"; cp registres/go.md "$E/go-$nom.md"
    cp "$E/decisions-sauve.md" registres/decisions.md; cp "$E/go-sauve.md" registres/go.md
    return 0
}
G=registres/go.md; DD=registres/decisions.md
cas F00-sain création FAUX_X=1
# témoin : la forme que la garde gelée sait voir (révocation qui nomme le GO cité, au registre des GO)
cas F01-revocation-de-GO-07-pendant-l-appel refus FAUX_FICHIER_PENDANT="$E/depot/$G" \
    "FAUX_LIGNE_PENDANT=| GO-2026-10-20-95 | $JOUR | révocation | révoque GO-2026-10-20-07 (essai) | — | $JOUR | Lazar | essai |"
# formes du texte que seule la lecture complète du module voit (l. 149 et l. 159 du lanceur, avant « show user »)
for x in GO-2026-10-04-08 GO-2026-10-20-06 R-262 R-269; do
    cas "F02-revocation-qui-nomme-$x-pendant-l-appel" refus FAUX_FICHIER_PENDANT="$E/depot/$G" \
        "FAUX_LIGNE_PENDANT=| GO-2026-10-20-96 | $JOUR | révocation | révoque $x (essai) | — | $JOUR | Lazar | essai |"
done
for x in R-262 R-269; do
    cas "F03-revocation-de-$x-au-registre-des-decisions-pendant-l-appel" refus FAUX_FICHIER_PENDANT="$E/depot/$DD" \
        "FAUX_LIGNE_PENDANT=| R-998 | $JOUR | **Révocation de $x** (essai) : délégation retirée. | essai |"
done
# témoins : les mêmes lignes consignées AVANT l'appel sont refusées (la chaîne les voit)
echo "| R-998 | $JOUR | **Révocation de R-262** (essai) : délégation retirée. | essai |" >> "$DD"
cas F04-revocation-de-R-262-consignee-avant-l-appel refus FAUX_X=1
echo "| GO-2026-10-20-96 | $JOUR | révocation | révoque GO-2026-10-04-08 (essai) | — | $JOUR | Lazar | essai |" >> "$G"
cas F05-revocation-de-GO-2026-10-04-08-consignee-avant-l-appel refus FAUX_X=1
cd "$E" && rm -rf "$E/depot" "$E/distant.git" "$E/B" "$E/traces"
echo "FIN DU BANC DU RELECTEUR (révocation pendant l'appel) ; écarts au texte : $N_ECARTS"
