#!/usr/bin/env bash
# Relecture « dépense et arrêts » de la chaîne de P4-instrument, v1 : banc du lanceur sur des artefacts de dépense
# fabriqués ici (R5). Relecteur neuf ; n'écrit que sous RACINE_NEUVE.
# Dépôt d'essai minimal (git init, aucun clone du dépôt de travail) : copie de src/ sans __pycache__, garde gelée,
# registres réels copiés (plus une ligne d'accord du jour), module de P4 et dix-sept scripts de la chaîne versés, six
# journaux de preuve factices, texte S tiré du brouillon 4 par outils_essais_p4_v1.py candidat ; dépôt nu local en guise
# de dépôt distant. Copie du lanceur : seules les lignes DEPOT, B et V changent (V : faux outil de location, qui
# n'appelle aucun service et journalise ses verbes). Faux contrôles avant dépense, faux df, fausse heure, HOME redirigé,
# clé d'API retirée, jetons factices. Le module commun et le module de P4 sont réels.
# Attendu de chaque cas : ce que le texte exige (« aucune création » : code 2 ou 3, aucune création factice).
# Usage : banc_depense_lanceur_v1.sh RACINE_NEUVE
set -uo pipefail
[ $# -eq 1 ] || { echo "usage : banc_depense_lanceur_v1.sh RACINE_NEUVE"; exit 2; }
E=$(realpath -m "$1")
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
for x in /usr/bin/vastai /bin/vastai /usr/local/bin/vastai; do [ -e "$x" ] && { echo "vastai réel présent ($x) : banc refusé"; exit 2; }; done
DEP=/home/user/controle-ia-travail
P4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument
HN=$P4/chaine; MOD=$P4/module; B4=$P4/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
P=prereg/P4-instrument-v1.md; VERSEES=docs/procedures/P4-instrument-v1; GO=GO-2026-10-20-07
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh recuperation_p4_v1.sh repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh
        essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
export PYTHONDONTWRITEBYTECODE=1
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }
echo "banc de relecture (dépense et arrêts) : lanceur, v1"
for f in "$HN/lancer_p4_v1.sh" "$HN/verifications_p4_v1.py" "$MOD/instrument_p4_v1.py" "$DEP/.claude/hooks/garde_calcul.py" "$0"; do
    echo "fichier relu : $(basename "$f") $(sha256sum "$f" | cut -d' ' -f1)"
done
JOUR=$(date -u +%F); HIER=$(date -u -d yesterday +%F); DEMAIN=$(date -u -d tomorrow +%F)
H=$E/B/p4-instrument/chaine
mkdir -p "$H" "$E/bin-vastai" "$E/home" "$E/bin-heure" "$E/bin-df" "$E/depot" || exit 2
cat > "$E/bin-vastai/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc de relecture : n'appelle aucun service ; journalise le verbe
J=${FAUX_VASTAI_JOURNAL:?}
echo "appel : $1 $2" >> "$J"
case "$1 $2" in
  "search offers") printf '[{"id": 111, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "machine_id": 7101, "host_id": 8101, "dph_total": %s, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 128886, "inet_down_cost": 0.025, "storage_total_cost": 0.015}]\n' "${FAUX_PRIX:-1.10}" ;;
  "show user")
      [ -n "${FAUX_REVOQUER_DEC_PENDANT:-}" ] && echo "| R-997 | $(date -u +%F) | **Révocation de R-269** (essai, consignée pendant l'appel). | essai |" >> "$FAUX_REVOQUER_DEC_PENDANT"
      [ -n "${FAUX_REVOQUER_PHASE_PENDANT:-}" ] && echo "| GO-2026-10-21-03 | $(date -u +%F) | révocation | révoque GO-2026-10-04-08 pendant l'appel (essai) | — | $(date -u +%F) | Lazar | essai |" >> "$FAUX_REVOQUER_PHASE_PENDANT"
      printf '{"credit": %s}\n' "${FAUX_CREDIT:-20.0}" ;;
  "show instances") d='[{"id": 56799469, "actual_status": "exited", "cur_state": "stopped", "label": "p3-v1"}]'; printf '%s\n' "${FAUX_INSTANCES:-$d}" ;;
  "create instance") echo "CREATION FACTICE" >> "$J"; echo "go ${GO_ID:-absent}" >> "$J"; printf '{"success": true, "new_contract": 99999999}\n' ;;
  *) echo "verbe inattendu" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin-vastai/vastai"
cat > "$E/bin-heure/date" <<'EOF'
#!/usr/bin/env bash
[ "$*" = "-u +%H%M" ] && { echo 1200; exit 0; }
exec /usr/bin/date "$@"
EOF
chmod +x "$E/bin-heure/date"
cat > "$E/bin-df/df" <<'EOF'
#!/usr/bin/env bash
printf 'Filesystem 1024-blocks Used Available Capacity Mounted\n/dev/x 10000000 100 9000000 1%% /\n'
EOF
chmod +x "$E/bin-df/df"
# faux contrôles avant dépense (le banc du rédacteur les éprouve à part) : conformes
cat > "$H/controles_avant_depense_p4_v1.sh" <<'EOF'
#!/usr/bin/env bash
mkdir -p "$2" "$2.travail"
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
cp "$HN/verifications_p4_v1.py" "$H/"
L=$H/lancer_p4_v1.sh
sed -e "s|^DEPOT=.*|DEPOT=$E/depot|" -e "s|^B=.*|B=$E/B|" -e "s|^V=.*|V=$E/bin-vastai/vastai|" "$HN/lancer_p4_v1.sh" > "$L"
[ "$(diff "$HN/lancer_p4_v1.sh" "$L" | grep -c '^>')" = 3 ] && ! grep -q "venv-vastai" "$L" || { echo "copie du lanceur non sûre : banc refusé"; exit 2; }
echo "copie du lanceur : trois lignes changées (DEPOT, B, V) ; aucun chemin vers l'outil de location réel"
for s in $CHAINE; do
    case "$s" in controles_avant_depense_p4_v1.sh|verifications_p4_v1.py|lancer_p4_v1.sh) continue ;; esac
    cp "$HN/$s" "$H/" || exit 2
done
# dépôt d'essai minimal
cd "$E/depot" && git init -q -b main && git config user.email essai@invalid && git config user.name essai && git config commit.gpgsign false || exit 2
(cd "$DEP" && tar --exclude=__pycache__ -cf - src) | tar -xf - || exit 2
mkdir -p .claude/hooks registres "$VERSEES" prereg && cp "$DEP/.claude/hooks/garde_calcul.py" .claude/hooks/ && cp "$DEP/registres/go.md" "$DEP/registres/decisions.md" registres/ || exit 2
echo "| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours. | essai |" >> registres/decisions.md
cp "$MOD"/*.py "$VERSEES/" && for s in $CHAINE; do cp "$H/$s" "$VERSEES/$s" && (cd "$VERSEES" && sha256sum "$s" > "$s.sha256"); done || exit 2
ep() { for s in "$@"; do echo "script éprouvé : $s $(sha256sum "$VERSEES/$s" | cut -d' ' -f1)"; done; }
jp() { local n=$1 v=$2; shift 2; { echo "journal factice du banc de relecture"; ep "$@"; echo "$v"; } > "$VERSEES/$n"; (cd "$VERSEES" && sha256sum "$n" > "$n.sha256"); }
jp banc-lanceur-p4-v1.log "FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0" lancer_p4_v1.sh verifications_p4_v1.py essais_lanceur_p4_v1.sh
jp banc-surveillance-p4-v1.log "FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0" surveiller_p4_v1.sh controle_cinq_minutes_p4_v1.sh essais_surveillance_p4_v1.sh
jp banc-verifications-p4-v1.log "FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0" verifications_p4_v1.py essais_verifications_p4_v1.sh outils_essais_p4_v1.py
jp banc-controles-p4-v1.log "FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0" controles_avant_depense_p4_v1.sh verifications_p4_v1.py essais_controles_p4_v1.sh outils_essais_p4_v1.py
jp banc-scellement-p4-v1.log "FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0" sceller_p4_v1.sh verifications_p4_v1.py essais_scellement_p4_v1.sh outils_essais_p4_v1.py
jp repetition-finale-p4-v1.log "RÉPÉTITION FINALE : CONFORME" sceller_p4_v1.sh controles_avant_depense_p4_v1.sh verifications_p4_v1.py repetition_finale_p4_v1.sh
git add -A && git commit -qm "C d'essai minimal : code, garde, registres, module et chaîne versés, preuves factices" || exit 2
"$PY" -B "$HN/outils_essais_p4_v1.py" candidat "$B4" "$E/prereg-origine.md" . 7a54d431d89745839220f882b41b13e8c62ecfdd \
    "$(printf 0%.0s {1..64})" 1102 > /dev/null || { echo "texte d'essai impossible"; exit 2; }
cp "$E/prereg-origine.md" "$P" && (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256")
git add "$P" "$P.sha256" && git commit -qm "S : texte d'essai scellé" || exit 2
S=$(git rev-parse HEAD); echo "S d'essai = $S"
git clone -q --bare . "$E/distant.git" && git remote add origin "$E/distant.git" && git fetch -q origin || exit 2
cp registres/go.md "$E/go-sauve.md"; cp registres/decisions.md "$E/decisions-sauve.md"; cp .claude/hooks/garde_calcul.py "$E/garde-sauve.py"
remettre() { cp "$E/go-sauve.md" registres/go.md; cp "$E/decisions-sauve.md" registres/decisions.md; cp "$E/garde-sauve.py" .claude/hooks/garde_calcul.py; }
go_col() {
    python3 - "$1" "$2" <<'PYG'
import sys
from pathlib import Path
k, val = int(sys.argv[1]), sys.argv[2]
g = Path("registres/go.md"); L = g.read_text(encoding="utf-8").split("\n")
L = ["|".join(c if i != k else f" {val} " for i, c in enumerate(l.split("|"))) if l.startswith("| GO-2026-10-20-07 |") else l for l in L]
g.write_text("\n".join(L), encoding="utf-8")
PYG
}
NON=0; N=0
cas() {   # $1 nom ; $2 attendu ; $3 constat si écart ; puis l'environnement
    local nom=$1 attendu=$2 constat=$3; shift 3
    rm -rf "$E/traces"; : > "$E/journal-$nom.txt"; N=$((N + 1))
    env -u VAST_API_KEY HOME="$E/home" PATH="$E/bin-heure:$E/bin-df:/usr/bin:/bin" \
        HF_TOKEN=factice-hf-0000000 CONTROLE_IA_GITHUB_TOKEN=factice-gh-0000000 FAUX_VASTAI_JOURNAL="$E/journal-$nom.txt" \
        "$@" bash "$L" "$E/traces" - R-999 > "$E/sortie-$nom.txt" 2>&1
    local c=$? cree; cree=$(grep -c "CREATION FACTICE" "$E/journal-$nom.txt")
    local v="CONFORME"
    if [ "$attendu" = 0 ]; then { [ "$c" = 0 ] && [ "$cree" = 1 ]; } || v="ÉCART (attendu : création)"
    else { [ "$c" = "$attendu" ] && [ "$cree" = 0 ]; } || v="ÉCART (attendu : code $attendu, aucune création) $constat"; fi
    [ "$v" = CONFORME ] || NON=$((NON + 1))
    echo "$nom : code $c ; créations factices $cree ; $v"
    grep -v '^$' "$E/sortie-$nom.txt" | tail -1 | sed 's/^/    | /' | couper 230
    return 0
}
echo "== cas sains"
remettre; cas L00-sain 0 "" FAUX_X=1
remettre; go_col 6 "$JOUR"; cas L01-echeance-le-jour-meme 0 "" FAUX_X=1
echo "== GO échu, plafond, garde qui refuse, accord"
remettre; go_col 6 "$HIER"; cas L10-go-echu 2 "" FAUX_X=1
remettre; go_col 5 "10 USD"; cas L11-plafond-sans-par-lancement 2 "" FAUX_X=1
remettre; echo "| GO-2026-10-21-02 | $JOUR | calcul | ligne à sept colonnes (essai) | — | $JOUR | Lazar |" >> registres/go.md; cas L12-garde-qui-refuse-registre-mal-forme 2 "" FAUX_X=1
remettre; go_col 2 "$DEMAIN"; cas L13-go-accorde-demain-garde-qui-refuse 2 "" FAUX_X=1
remettre; sed -i "s/^| R-999 | $JOUR |/| R-999 | $DEMAIN |/" registres/decisions.md; cas L14-accord-de-demain 2 "" FAUX_X=1
remettre; cas L15-credit-nan 2 "" 'FAUX_CREDIT=NaN'
remettre; cas L16-instance-p4-deja-en-marche 2 "" 'FAUX_INSTANCES=[{"id": 56799469, "actual_status": "exited", "cur_state": "stopped", "label": "p3-v1"}, {"id": 99999998, "actual_status": "running", "cur_state": "running", "label": "p4-v1"}]'
remettre; cas L17-instance-toleree-arretee-mais-cur-running 2 "" 'FAUX_INSTANCES=[{"id": 56799469, "actual_status": "exited", "cur_state": "running", "label": "p3-v1"}]'
echo "== révocations sous des formes voisines de celles du texte"
remettre; echo "|GO-2026-10-21-01|$JOUR|révocation|révoque GO-2026-10-04-08 (essai)|—|$JOUR|Lazar|essai|" >> registres/go.md
cas L20-revocation-de-la-phase-ligne-sans-espace 2 "RC-depense-03" FAUX_X=1
remettre; echo "|GO-2026-10-21-01|$JOUR|révocation|révoque R-269 (essai)|—|$JOUR|Lazar|essai|" >> registres/go.md
cas L21-revocation-de-R-269-ligne-sans-espace 2 "RC-depense-03" FAUX_X=1
remettre; echo "| GO-2026-10-21-01 | $JOUR | Révocation | révoque GO-2026-10-20-07 (essai) | — | $JOUR | Lazar | essai |" >> registres/go.md
cas L22-revocation-type-avec-majuscule 2 "RC-depense-03" FAUX_X=1
remettre; echo "| R-998 | $JOUR | **Révocation de R-262 et de R-269** (essai). | essai |" >> registres/decisions.md
cas L23-revocation-des-deux-decisions-en-une-cellule 2 "RC-depense-03" FAUX_X=1
echo "== révocations consignées pendant l'appel (après le contrôle du GO, avant la création)"
remettre; cas L30-revocation-de-R-269-au-registre-des-decisions-pendant-l-appel 2 "RC-depense-08" FAUX_REVOQUER_DEC_PENDANT="$E/depot/registres/decisions.md"
remettre; cas L31-revocation-de-la-phase-au-registre-des-go-pendant-l-appel 2 "RC-depense-08" FAUX_REVOQUER_PHASE_PENDANT="$E/depot/registres/go.md"
echo "== garde gelée remplacée dans l'arbre de travail du dépôt (non relue contre S)"
remettre; python3 - <<'PYG'
from pathlib import Path
p = Path(".claude/hooks/garde_calcul.py"); t = p.read_text(encoding="utf-8")
t = t.replace("def decider(commande: str, aujourd_hui: date) -> None:\n", "def decider(commande: str, aujourd_hui: date) -> None:\n    return  # garde neutralisée (artefact du banc)\n", 1)
p.write_text(t, encoding="utf-8")
PYG
go_col 2 "$DEMAIN"; echo "| GO-2026-10-21-02 | $JOUR | calcul | ligne à sept colonnes (essai) | — | $JOUR | Lazar |" >> registres/go.md
echo "    garde de l'arbre de travail ≠ garde de S : $(git diff --quiet "$S" -- .claude/hooks/garde_calcul.py && echo non || echo oui)"
cas L40-garde-neutralisee-go-accorde-demain-registre-mal-forme 2 "RC-depense-04" FAUX_X=1
echo "== plafond de la phase (150 USD) : accord qui écrit le dépassement"
remettre; sed -i "s/^| R-999 | $JOUR | .*/| R-999 | $JOUR | **Accord de Lazar pour le lancement de P4-instrument** (essai) : délégation $GO en cours ; dépense consignée 148,00 USD + borne 5,41 USD = 153,41 USD, au-dessus des 150 USD de la phase. | essai |/" registres/decisions.md
cas L50-accord-qui-ecrit-le-plafond-de-phase-depasse 2 "RC-depense-05" FAUX_X=1
remettre
echo "== heure relue juste avant la création"
grep -n 'trap - ERR\|^H1=\|^set +e' "$L" | sed 's/^/    > /'
FUITES=$(grep -l 'factice-hf\|factice-gh' "$E"/sortie-*.txt "$E"/journal-*.txt 2>/dev/null || true)
[ -z "$FUITES" ] && echo "aucun jeton factice affiché" || echo "jeton factice affiché dans : $FUITES"
P_CACHE=$(find "$E/depot" "$H" "$HN" "$MOD" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit" || echo "__pycache__ écrit : $P_CACHE"
echo "FIN DU BANC DE RELECTURE DU LANCEUR : $N cas ; écarts au texte : $NON"
