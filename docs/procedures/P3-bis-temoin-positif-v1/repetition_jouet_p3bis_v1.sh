#!/usr/bin/env bash
# Brouillon 2 (2026-11-10, après la fusion du code corrigé, branche prep/p3bis-code-v2) : VRAI module ouverture_p3bis_v2
# (bouchon retiré), VRAIE amorce v2, run source décisif fabriqué par l'essai de fermeture v2, lectures décisives réelles.
# Répétition jouet de la chaîne de session de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au 2026-11-23 : R-2077), v1 : la chaîne entière,
# dans l'ordre de la session — lanceur, contrôle à cinq minutes, surveillance, récupération (lectures fermées, commit et
# poussée du seul paquet), destruction — jouée de bout en bout contre un FAUX outil de location qui simule l'instance
# (aucun service appelé, aucune dépense), un registre des GO TEMPORAIRE (ligne GO-2026-11-10-02 recopiée de main ; le
# vrai registres/go.md n'est jamais modifié), un dépôt synthétique et un dépôt nu local. Déclinée de l'esprit de
# docs/procedures/P3-premier-test-v2/repetition_jouet_p3_v1.sh (P3 répétait la chaîne de l'instance en mode jouet ; ici
# c'est la chaîne de session qui est neuve : la chaîne de l'instance appartient au code corrigé, autre chantier).
# Trois tentatives, chacune sur sa branche :
#   1. calcul/p3bis-reel-v1, fin normale : le faux outil pousse une branche de calcul comme l'instance (run factice,
#      second paquet RÉEL fait par `ouverture_p3bis_v2.fermer_run`, traces), puis son journal avance (amorce, PROGRES,
#      fin, code 0) ; contrôle à cinq minutes conforme (joué à la création + 181 s : la répétition attend) ; surveillance
#      → FIN, arrêt par l'identifiant ; récupération conforme (paquet des lectures de 16 783 360 octets poussé) ;
#      destruction par l'identifiant ;
#   2. calcul/p3bis-reel-v2 (relance), second paquet en échec : journal « SECOND PAQUET EN ÉCHEC », fin, code 5 ;
#      surveillance → GARDER (arrêt par l'identifiant, instance gardée) ; récupération des traces seules (code 4) ;
#      destruction REFUSÉE ;
#   3. calcul/p3bis-reel-v3 (relance) : d'abord REFUSÉE (l'instance gardée de la tentative 2 est sur le compte, ni
#      tolérée ni en marche : liste fermée, nœud) ; puis, sur un compte factice neuf (instance gardée mise de côté, déclaré),
#      contrôle à cinq minutes en échec (commit autre au journal) : arrêt par l'identifiant, aucune destruction.
# Copies jouées, lignes changées comptées et déclarées : lanceur (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S) ; récupération
# (DEPOT_URL, PY) ; contrôles avant dépense : BOUCHON (le bloc réel est joué par son banc et par la répétition finale) ;
# module d'ouverture v2, amorce v2 : les VRAIS (src/ et scripts/ de l'arbre fusionné) ; run source décisif fabriqué par
# `fabriquer_run` de l'essai de fermeture v2 sous le texte factice, qui cite le commit du code, la configuration du run et
# l'entropie de P3 ; lectures de P3 et complémentaire réelles, décisives ; journaux de preuve à S : factices, à la forme du module commun
# (ceux de la répétition ne peuvent exister avant elle). Surveillance à INTERVALLE=1.
# Le journal écrit « script éprouvé : <script> <sha256> » pour les scripts réels dont les copies sont jouées, chaque
# étape avec son code et sa dernière ligne, les durées, et finit sur « RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME ».
# Usage : repetition_jouet_p3bis_v1.sh RACINE_NEUVE
set -uo pipefail
R=$(realpath -m "${1:?racine neuve}")
ICI=$(dirname "$(realpath "$0")")
SRC=$(realpath "$ICI/../../..")
PYB=/home/user/controle-ia-travail/.venv/bin/python
V=docs/procedures/P3-bis-temoin-positif-v1
P=prereg/P3-bis-temoin-positif-v1.md
A=scripts/amorce_instance_p3bis_v2.sh
ENT=173398867739501636779144561928402532101
export PYTHONDONTWRITEBYTECODE=1
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R/bin" "$R/H" "$R/home" "$R/etat" || exit 2
DEBUT=$(date -u +%s); echo "début de la répétition : $(date -u +%FT%TZ)"
for s in lancer_p3bis_v1.sh controle_cinq_minutes_p3bis_v1.sh surveiller_p3bis_v1.sh recuperation_p3bis_v1.sh detruire_p3bis_v1.sh verifications_p3bis_v1.py; do
    echo "script éprouvé : $s $(sha256sum "$ICI/$s" | cut -d' ' -f1)"
done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
NON_CONFORMES=0
JETONS=(HF_TOKEN=factice-hf-6666666 CONTROLE_IA_GITHUB_TOKEN=factice-gi-7777777)
# --- copies jouées -----------------------------------------------------------------------------------------------------
sed -e "s|^DEPOT=.*|DEPOT=$R/depot|" -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$R/distant.git|" -e "s|^INTERVALLE_OFFRE_S=.*|INTERVALLE_OFFRE_S=0|" "$ICI/lancer_p3bis_v1.sh" > "$R/H/lancer_p3bis_v1.sh"
sed -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$R/distant.git|" -e "s|^PY=A_EPINGLER.*|PY=$PYB|" "$ICI/recuperation_p3bis_v1.sh" > "$R/H/recuperation_p3bis_v1.sh"
echo "lignes changées : lanceur $(diff "$ICI/lancer_p3bis_v1.sh" "$R/H/lancer_p3bis_v1.sh" | grep -c '^>') (DEPOT, DEPOT_URL, INTERVALLE_OFFRE_S) ; récupération $(diff "$ICI/recuperation_p3bis_v1.sh" "$R/H/recuperation_p3bis_v1.sh" | grep -c '^>') (DEPOT_URL, PY)"
for s in controle_cinq_minutes_p3bis_v1.sh surveiller_p3bis_v1.sh detruire_p3bis_v1.sh verifications_p3bis_v1.py; do cp "$ICI/$s" "$R/H/"; done
cat > "$R/H/controles_avant_depense_p3bis_v1.sh" <<'EOF'
#!/usr/bin/env bash
# bouchon de la répétition jouet : les contrôles réels sont joués par leur banc et par la répétition finale
mkdir -p "$2" "$2.travail"; echo "OK  bouchon de la répétition jouet (S=${1:0:12}, branche $3)"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
EOF
CHAINE=$(sed -n 's/^CHAINE="\(.*\)"$/\1/p' "$R/H/lancer_p3bis_v1.sh")
for s in $CHAINE; do [ -e "$R/H/$s" ] || { if [ -f "$ICI/$s" ]; then cp "$ICI/$s" "$R/H/$s"; else echo "# $s : pas encore écrit au moment de la répétition (copie témoin)" > "$R/H/$s"; fi; }; done
# --- dépôt synthétique ----------------------------------------------------------------------------------------------
git init -q --bare -b main "$R/distant.git"
git init -q -b main "$R/depot" && cd "$R/depot" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false; git config push.negotiate false
git remote add origin "$R/distant.git"
cp -r "$SRC/src" . && find src -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null
cp "$SRC/pyproject.toml" .; printf '__pycache__/\n*.pyc\ndonnees/\n' > .gitignore
[ -f src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py ] || { echo "module ouverture_p3bis_v2 absent de l'arbre fusionné"; exit 2; }
mkdir -p prereg scripts registres .claude/hooks "$V"
cp "$SRC/$A" "$A"                                  # vraie amorce v2 (code corrigé)
git -C "$SRC" show HEAD:.claude/hooks/garde_calcul.py > .claude/hooks/garde_calcul.py
{ git -C "$SRC" show main:registres/go.md | sed -n '1,10p'; git -C "$SRC" show main:registres/go.md | grep '^| GO-2026-11-10-02 |'; } > registres/go.md
for s in lancer_p3bis_v1.sh $CHAINE; do cp "$R/H/$s" "$V/$s"; done
"$PYB" -I -B - "$R/H/verifications_p3bis_v1.py" "$R/H" "$V" <<'EOF' || exit 2
import hashlib, importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
h, sortie = Path(sys.argv[2]), Path(sys.argv[3])
for nom, (verdict, scripts) in v.JOURNAUX.items():
    lignes = [f"script éprouvé : {s} {hashlib.sha256((h / s).read_bytes()).hexdigest()}" for s in sorted(scripts)]
    (sortie / nom).write_text("\n".join(lignes) + "\njournal factice de la répétition jouet\n" + verdict + "\n", encoding="utf-8")
EOF
(cd "$V" && for f in *; do case "$f" in *.sha256) ;; *) sha256sum "$f" > "$f.sha256" ;; esac; done)
git add -A && git commit -qm "base de la répétition jouet" && git push -q origin main || exit 2
E_AMORCE=$(sha256sum "$A" | cut -d' ' -f1); CODE=$(git rev-parse HEAD)
CONFIG='{"mode": "reel", "max_nouveaux": 64}'
PYTHONPATH=src "$PYB" -B - "$P" "$CODE" "$ENT" "$CONFIG" "$R/distant.git" "$A" "$E_AMORCE" <<'EOF' || exit 2
"""Texte factice scellé : lignes lues par le lanceur, le contrôle à cinq minutes et la récupération, et forme de R1 et R2
(sections, contre-lecture) lue par les lectures décisives ; cite le commit du code, la configuration du run et l'entropie."""
import hashlib, json, sys
from pathlib import Path
from controle_ia.manifeste import config_canonique
from controle_ia.prereg import SECTIONS
from controle_ia.scellement import sceller
chemin, commit, ent, config, distant, amorce, e_amorce = sys.argv[1:8]
corps = ["# Préenregistrement factice de la répétition jouet de P3-bis", "",
         "- GO : **GO-2026-11-10-02** (`registres/go.md`)",
         f"- Lancement : `GO_ID=GO-2026-11-10-02`, `PREREG={chemin}`, `BRANCHE=calcul/p3bis-reel-v1` (une relance prend `…-v2`, "
         f"puis `…-v3`), `DEPOT_URL=file://{distant}`",
         f"- Empreintes : `{amorce}` (`{e_amorce}`, sha256)", f"- Commit du code d'analyse : `{commit}`",
         f"- Configuration de P3 (empreinte canonique) : `{hashlib.sha256(config_canonique(json.loads(config))).hexdigest()}`",
         f"- Entropie : `{ent}`", "- Tests attendus : `531`", ""]
for s in SECTIONS[:-1]:
    corps += [f"## {s}", "", f"contenu factice : {s}", ""]
corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
Path(chemin).write_text("\n".join(corps), encoding="utf-8")
sceller(chemin)
EOF
git add -A && git commit -qm "S (répétition jouet)" && git push -q origin main || exit 2
S=$(git rev-parse HEAD); echo "commit de scellement de la répétition : $S"
cd "$R" || exit 2
# --- faux outil de location : simule l'instance --------------------------------------------------------------------
cat > "$R/bin/construire-instance.sh" <<EOF
#!/usr/bin/env bash
# branche de calcul poussée comme l'instance la pousserait (scénario 1 : run et second paquet réel ; 2 : traces seules)
set -euo pipefail
br=\$1; commit=\$2; scen=\$3; d=\$(mktemp -d "$R/instance-XXXX")
git clone -q "$R/distant.git" "\$d/c" && cd "\$d/c" && git checkout -q "\$commit" && git checkout -q -b "\$br"
git config user.name "instance de calcul (P3-bis)"; git config user.email instance-calcul@invalid; git config commit.gpgsign false; git config push.negotiate false
RUN=20261112-080000-p3bis-reel
mkdir -p "traces/p3bis-\$scen"; echo "journal factice (scénario \$scen)" > "traces/p3bis-\$scen/journal.txt"; (cd "traces/p3bis-\$scen" && sha256sum -- * > empreintes.sha256)
if [ "\$scen" = 1 ]; then
    PYTHONPATH="\$d/c/src" "$PYB" -B - "\$d/c" "\$RUN" prereg/P3-bis-temoin-positif-v1.md "$ENT" '{"mode": "reel", "max_nouveaux": 64}' "$SRC/scripts/essai_fermeture_p3bis_v2.py" <<'PYF'
import importlib.util, json, sys
from pathlib import Path
clone, run, prereg, entropie, config, essai = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("essai_fermeture_p3bis_v2", essai)
ev2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(ev2)
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob
ev2.fabriquer_run(Path(clone), run, "vu", ev2.graine("vu"), config=json.loads(config), decisif=True, prereg=prereg, entropie=int(entropie))
ob.fermer_run(Path(clone), run)
PYF
fi
for x in runs diag traces; do [ -e "\$x" ] && git add "\$x"; done
git commit -qm "P3-bis (reel) : scénario \$scen de la répétition jouet" && git push -q origin "\$br"
rm -rf "\$d"
EOF
chmod +x "$R/bin/construire-instance.sh"
cat > "$R/bin/vastai" <<EOF
#!/usr/bin/env bash
# faux outil de location de la répétition jouet de P3-bis : simule une instance ; n'appelle aucun service
ET="$R/etat"
echo "\$(date -u +%FT%TZ) \$*" >> "\$ET/appels.txt"
case "\$1 \$2" in
  "search offers") printf '%s\n' '[{"id": 111, "machine_id": 7101, "host_id": 8101, "gpu_name": "A100 SXM4", "gpu_ram": 81920, "num_gpus": 1, "cpu_name": "AMD EPYC 7513 32-Core Processor", "cpu_cores_effective": 32.0, "cpu_ram": 257000, "disk_space": 200.0, "cuda_max_good": 13.0, "reliability2": 0.989, "dph_total": 1.10, "inet_down_cost": 0.026, "storage_total_cost": 0.05}]' ;;
  "show user") echo '{"credit": 30.0}' ;;
  "show instances")
    l='{"id": 58936096, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936099, "actual_status": "exited", "cur_state": "stopped"}, {"id": 58936100, "actual_status": "exited", "cur_state": "stopped"}'
    for d in "\$ET"/instance-*; do [ -d "\$d" ] || continue; [ -e "\$d/detruite" ] && continue
        l="\$l, {\"id\": \${d##*-}, \"actual_status\": \"\$( [ -e "\$d/arretee" ] && echo exited || echo running)\", \"cur_state\": \"\$( [ -e "\$d/arretee" ] && echo stopped || echo running)\", \"dph_total\": 1.1}"; done
    echo "[\$l]" ;;
  "create instance")
    a=("\$@"); br=""; commit=""; lab=""
    for ((i = 0; i < \${#a[@]}; i++)); do
      [ "\${a[\$i]}" = "--label" ] && lab=\${a[\$((i + 1))]}
      [ "\${a[\$i]}" = "--env" ] && for kv in \${a[\$((i + 1))]}; do case "\$kv" in BRANCHE=*) br=\${kv#BRANCHE=} ;; COMMIT=*) commit=\${kv#COMMIT=} ;; esac; done
    done
    scen=\${br##*-v}; id=7777777\$scen; mkdir -p "\$ET/instance-\$id"
    printf '%s\n' "\$br" > "\$ET/instance-\$id/branche"; printf '%s\n' "\$commit" > "\$ET/instance-\$id/commit"; printf '%s\n' "\$lab" > "\$ET/instance-\$id/etiquette"
    [ "\$scen" = 3 ] || "$R/bin/construire-instance.sh" "\$br" "\$commit" "\$scen" >> "\$ET/construction.txt" 2>&1 || { echo '{"success": false, "msg": "construction"}'; exit 0; }
    echo "{\"success\": true, \"new_contract\": \$id}" ;;
  "show instance")
    d="\$ET/instance-\$3"; [ -d "\$d" ] || { echo "instance inconnue"; exit 1; }
    st=running; cs=running; [ -e "\$d/arretee" ] && { st=exited; cs=stopped; }
    echo "{\"actual_status\": \"\$st\", \"cur_state\": \"\$cs\", \"intended_status\": \"running\", \"status_msg\": \"jouet\", \"dph_total\": 1.1, \"machine_id\": 7101, \"host_id\": 8101, \"gpu_name\": \"A100 SXM4\", \"label\": \"\$(cat "\$d/etiquette")\", \"inet_down_billed\": 18, \"inet_down_cost\": 0.026}" ;;
  "logs "*)
    d="\$ET/instance-\$2"; [ -d "\$d" ] || exit 1
    n=\$(( \$(cat "\$d/tours" 2>/dev/null || echo 0) + 1 )); echo "\$n" > "\$d/tours"
    br=\$(cat "\$d/branche"); c=\$(cat "\$d/commit"); scen=\${br##*-v}
    [ "\$scen" = 3 ] && c=fedcba9876543210fedcba9876543210fedcba98
    echo "AMORCE 2026-11-12T08:00:00Z : commit \$c"
    echo "2026-11-12T08:00:10Z début : ETUDE=p3bis MODE=reel COMMIT=\$c BRANCHE=\$br"
    echo "2026-11-12T08:00:20Z préenregistrement lu : 531 tests attendus ; configuration prereg/P3-bis-temoin-positif-config-v1.json"
    echo "NVIDIA A100-SXM4-80GB, 580.159.03, 81920 MiB"
    echo "2026-11-12T08:00:40Z branche \$br poussée avant l'installation (droit d'écriture éprouvé)"
    [ "\$n" -ge 2 ] && echo "PROGRES 2026-11-12T09:00:00Z etape=sondes-figees empreinte=0123456789abcdef sondes=430"
    if [ "\$n" -ge 3 ]; then
      echo "2026-11-12T09:01:00Z run : processus 4242 lancé"; echo "2026-11-12T12:00:00Z run : processus 4242 fini, code 0"
      if [ "\$scen" = 2 ]; then echo "2026-11-12T12:01:00Z SECOND PAQUET EN ÉCHEC (relecture fausse, jouet) : aucun fichier du run poussé en clair"; echo "AMORCE 2026-11-12T12:05:00Z : fin, code 5"
      else echo "AMORCE 2026-11-12T12:30:00Z : fin, code 0"; fi
    fi ;;
  "stop instance") [ -d "\$ET/instance-\$3" ] && touch "\$ET/instance-\$3/arretee" && echo '{"success": true}' ;;
  "destroy instance") [ -d "\$ET/instance-\$3" ] && touch "\$ET/instance-\$3/detruite" && echo '{"success": true}' ;;
  *) echo "verbe inattendu : \$*" >&2; exit 9 ;;
esac
EOF
chmod +x "$R/bin/vastai"
ENV=(env -i PATH="$R/bin:/usr/bin:/bin" HOME="$R/home" LANG=C.UTF-8 "${JETONS[@]}")
etape() {   # $1 nom, $2 code attendu, $3 motif de la dernière ligne ; puis la commande
    local nom=$1 attendu=$2 motif=$3 c t0 v; shift 3
    t0=$(date -u +%s)
    "${ENV[@]}" "$@" > "$R/console-$nom.txt" 2>&1; c=$?
    v=CONFORME
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    grep -v '^$' "$R/console-$nom.txt" | tail -1 | grep -qF -- "$motif" || v="NON CONFORME (motif « $motif » absent de la dernière ligne)"
    grep -rqF -e factice-hf-6666666 -e factice-gi-7777777 "$R/console-$nom.txt" && v="NON CONFORME (JETON AFFICHÉ)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(( $(date -u +%s) - t0 )) s ; $v"
    grep -v '^$' "$R/console-$nom.txt" | tail -1 | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
}
verifier() {
    local desc=$1; shift
    if (eval "$*") > /dev/null 2>&1; then echo "    $desc : CONFORME"; else echo "    $desc : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
attendre_cinq() {   # le contrôle à cinq minutes refuse avant la création + 180 s : la répétition attend
    local cr; cr=$(sed -n 's/^creation \([0-9]*\)$/\1/p' "$1/lancement.txt")
    while [ "$(date -u +%s)" -lt $((cr + 181)) ]; do sleep 5; done
}
# --- tentative 1 : fin normale ------------------------------------------------------------------------------------
etape T1-lanceur 0 "succès : True ; identifiant 77777771" bash "$R/H/lancer_p3bis_v1.sh" "$S" "$R/traces-1" - 1
verifier "lancement : instance 77777771 écrite, offre 111, branche v1 poussée par l'« instance »" \
    "grep -qx 'instance 77777771' '$R/traces-1/lancement.txt' && git --git-dir='$R/distant.git' rev-parse -q --verify refs/heads/calcul/p3bis-reel-v1"
attendre_cinq "$R/traces-1"
etape T1-cinq-minutes 0 "CONTRÔLE À CINQ MINUTES : CONFORME" bash "$R/H/controle_cinq_minutes_p3bis_v1.sh" 77777771 "$R/traces-1" "$R/cinq-1"
"${ENV[@]}" INTERVALLE=1 bash "$R/H/surveiller_p3bis_v1.sh" 77777771 "$R/traces-1" 0 "$R/surv-1" > "$R/console-T1-surveillance.txt" 2>&1; c=$?
[ "$c" = 0 ] && tail -1 "$R/console-T1-surveillance.txt" | grep -q '^FIN : AMORCE .* fin, code 0 ; instance 77777771 arrêtée par son identifiant' \
    && echo "T1-surveillance : code 0 ; CONFORME" || { echo "T1-surveillance : code $c ; NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
tail -1 "$R/console-T1-surveillance.txt" | cut -c1-170 | sed 's/^/    | /'
verifier "surveillance : PROGRES relevé, dépense relevée sous 80 USD, arrêt par l'identifiant (instance arrêtée)" \
    "grep -q '^PROGRES' '$R/surv-1/progres.txt' && grep -q 'plafond 80 USD' '$R/surv-1/depenses.txt' && [ -e '$R/etat/instance-77777771/arretee' ] && grep -qx FIN '$R/surv-1/motif.txt'"
etape T1-recuperation 0 "RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures" bash "$R/H/recuperation_p3bis_v1.sh" "$S" calcul/p3bis-reel-v1 "$R/recup-1"
verifier "récupération : branche distante = commit du seul paquet (16 783 360 octets) et de son compagnon" \
    "[ \"\$(git --git-dir='$R/distant.git' diff --name-only refs/heads/calcul/p3bis-reel-v1^ refs/heads/calcul/p3bis-reel-v1 | wc -l)\" = 2 ] && [ \"\$(git --git-dir='$R/distant.git' cat-file -s refs/heads/calcul/p3bis-reel-v1:diag/p3bis-ferme-20261112-080000-p3bis-reel/paquet-ferme-v1.tar)\" = 16783360 ]"
etape T1-destruction 0 "DESTRUCTION : instance 77777771 détruite" bash "$R/H/detruire_p3bis_v1.sh" 77777771 "$R/traces-1" "$R/surv-1" "$R/recup-1.rapport.txt"
# --- tentative 2 : relance, second paquet en échec (code 5) ---------------------------------------------------------
etape T2-lanceur 0 "succès : True ; identifiant 77777772" bash "$R/H/lancer_p3bis_v1.sh" "$S" "$R/traces-2" - 2
attendre_cinq "$R/traces-2"
etape T2-cinq-minutes 0 "CONTRÔLE À CINQ MINUTES : CONFORME" bash "$R/H/controle_cinq_minutes_p3bis_v1.sh" 77777772 "$R/traces-2" "$R/cinq-2"
"${ENV[@]}" INTERVALLE=1 bash "$R/H/surveiller_p3bis_v1.sh" 77777772 "$R/traces-2" 4.5 "$R/surv-2" > "$R/console-T2-surveillance.txt" 2>&1; c=$?
[ "$c" = 0 ] && tail -1 "$R/console-T2-surveillance.txt" | grep -q '^GARDER : fin, code 5 .* GARDÉE, jamais détruite' \
    && echo "T2-surveillance : code 0 ; CONFORME" || { echo "T2-surveillance : code $c ; NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
tail -1 "$R/console-T2-surveillance.txt" | cut -c1-170 | sed 's/^/    | /'
etape T2-recuperation 4 "RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN), SANS LECTURE : TOUS CONFORMES" bash "$R/H/recuperation_p3bis_v1.sh" "$S" calcul/p3bis-reel-v2 "$R/recup-2"
etape T2-destruction-refusee 2 "REFUS : instance gardée" bash "$R/H/detruire_p3bis_v1.sh" 77777772 "$R/traces-2" "$R/surv-2" "$R/recup-2.rapport.txt"
verifier "instance du code 5 : arrêtée, jamais détruite" "[ -e '$R/etat/instance-77777772/arretee' ] && [ ! -e '$R/etat/instance-77777772/detruite' ]"
# --- tentative 3 refusée : l'instance gardée de la tentative 2 est sur le compte, ni tolérée ni en marche ----------------
etape T3a-lanceur-refuse 2 "instances : non tolérée(s)" bash "$R/H/lancer_p3bis_v1.sh" "$S" "$R/traces-3a" - 3
verifier "instance gardée : toute création neuve refusée (liste fermée : nœud), branche v3 non créée" \
    "grep -q 'instances non tolérées : 77777772 (exited, stopped)' '$R/traces-3a/lancement.txt' && ! git --git-dir='$R/distant.git' rev-parse -q --verify refs/heads/calcul/p3bis-reel-v3"
# --- tentative 3 sur un compte factice neuf (instance gardée mise de côté), contrôle à cinq minutes en échec ------------
mkdir -p "$R/etat-mis-de-cote" && mv "$R/etat/instance-77777772" "$R/etat-mis-de-cote/"
etape T3-lanceur 0 "succès : True ; identifiant 77777773" bash "$R/H/lancer_p3bis_v1.sh" "$S" "$R/traces-3" - 3
attendre_cinq "$R/traces-3"
etape T3-cinq-minutes-ko 1 "instance 77777773 arrêtée par son identifiant (R10) ; nœud de Lazar" bash "$R/H/controle_cinq_minutes_p3bis_v1.sh" 77777773 "$R/traces-3" "$R/cinq-3"
verifier "contrôle à cinq minutes en échec : instance arrêtée, non détruite ; instance gardée de la tentative 2 jamais détruite" "[ -e '$R/etat/instance-77777773/arretee' ] && [ ! -e '$R/etat/instance-77777773/detruite' ] && [ ! -e '$R/etat-mis-de-cote/instance-77777772/detruite' ]"
# --- bilan --------------------------------------------------------------------------------------------------------
verifier "aucun verbe sur les instances tolérées ; destructions : la seule instance de la fin normale" \
    "! grep -E ' (stop|destroy) instance 589361' '$R/etat/appels.txt' && [ \"\$(grep -c ' destroy instance ' '$R/etat/appels.txt')\" = 1 ] && grep -q ' destroy instance 77777771\$' '$R/etat/appels.txt'"
verifier "aucun jeton dans les traces, sorties et états" "! grep -rqF -e factice-hf-6666666 -e factice-gi-7777777 '$R'/traces-* '$R'/cinq-* '$R'/surv-* '$R'/recup-*.rapport.txt '$R'/console-*"
echo "durée de la répétition : $(( $(date -u +%s) - DEBUT )) s ; fin : $(date -u +%FT%TZ)"
if [ "$NON_CONFORMES" = 0 ]; then echo "RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : CONFORME"; else echo "RÉPÉTITION JOUET DE LA CHAÎNE DE P3-BIS : $NON_CONFORMES étape(s) en écart"; fi
[ "$NON_CONFORMES" = 0 ]
