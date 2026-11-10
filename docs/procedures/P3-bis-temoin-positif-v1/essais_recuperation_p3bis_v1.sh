#!/usr/bin/env bash
# Banc de la récupération et de la destruction de P3-bis (R5), v1 : recuperation_p3bis_v1.sh et detruire_p3bis_v1.sh,
# un cas sain et des artefacts. Dépôt synthétique (src/ de HEAD, texte factice citant l'entropie de P3, chaîne versée :
# la copie jouée de la récupération et la destruction, scellées) et dépôt nu local ; branches de calcul fabriquées comme
# l'instance les pousse (auteur « instance de calcul (P3-bis) », run factice, second paquet RÉEL fait par
# `ouverture_p3bis_v1.fermer_run`, traces scellées ; aucun fichier du run en clair). Le module d'ouverture v2 n'existe pas
# encore (autre chantier) : un bouchon `ouverture_p3bis_v2` est versé dans le src/ du dépôt synthétique ; il garde
# l'interface v2 (« lectures-fermees » exige --prereg et --entropie, ses arguments sont écrits) et appelle la logique
# réelle de `ouverture_p3bis_v1.lectures_fermees` (dépliage du second paquet, sorties redirigées, mise en paquet bourrée
# de 16 783 360 octets, effacement), avec deux lectures factices (aucune donnée réelle). Faux outil de location pour la
# destruction (verbes journalisés ; aucun service appelé). Aucun appel externe.
# Lignes changées dans la copie jouée de la récupération, comptées et déclarées : DEPOT_URL (dépôt nu local) et PY
# (interpréteur du banc).
# Usage : essais_recuperation_p3bis_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
ICI=$(dirname "$(realpath "$0")")
SRC=$(realpath "$ICI/../../..")
PYB=/home/user/controle-ia-travail/.venv/bin/python
V=docs/procedures/P3-bis-temoin-positif-v1
P=prereg/P3-bis-temoin-positif-v1.md
ENT=173398867739501636779144561928402532101
RUN=20261112-080000-p3bis-reel
export PYTHONDONTWRITEBYTECODE=1
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
for s in recuperation_p3bis_v1.sh detruire_p3bis_v1.sh verifications_p3bis_v1.py; do echo "script éprouvé : $s $(sha256sum "$ICI/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
mkdir -p "$E/bin" && cd "$E" || exit 2
NON_CONFORMES=0; NCAS=0
# --- copie jouée ---------------------------------------------------------------------------------------------------
sed -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$E/distant.git|" -e "s|^PY=A_EPINGLER.*|PY=$PYB|" "$ICI/recuperation_p3bis_v1.sh" > "$E/recuperation_p3bis_v1.sh"
echo "lignes changées dans la copie de la récupération : $(diff "$ICI/recuperation_p3bis_v1.sh" "$E/recuperation_p3bis_v1.sh" | grep -c '^>') (DEPOT_URL, PY)"
[ "$(diff "$ICI/recuperation_p3bis_v1.sh" "$E/recuperation_p3bis_v1.sh" | grep -c '^>')" = 2 ] || { echo "copie de la récupération non sûre"; exit 2; }
cp "$ICI/detruire_p3bis_v1.sh" "$ICI/verifications_p3bis_v1.py" "$E/"
# --- dépôt synthétique ----------------------------------------------------------------------------------------------
git init -q -b main source && cd source || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false; git config push.negotiate false
cp -r "$SRC/src" . && find src -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null
cp "$SRC/pyproject.toml" .; printf '__pycache__/\n*.pyc\ndonnees/\n' > .gitignore
cat > src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py <<'EOF'
"""Bouchon du banc de la récupération de P3-bis : interface v2 de « lectures-fermees » (--prereg et --entropie exigés),
logique réelle de `ouverture_p3bis_v1.lectures_fermees` (dépliage, redirections, mise en paquet), lectures factices."""
import argparse, os, sys
from controle_ia.premier_test_ia import ouverture_p3bis_v1 as o


def commandes(run, lecture, lecture_c, prereg, entropie):
    code = 3 if os.environ.get("FAUX_LECTURE_ECHEC") else 0
    ecr = ("import pathlib, sys; r, n = sys.argv[1:3]; "
           "[pathlib.Path(x).mkdir(parents=True, exist_ok=True) for x in (f'runs/{r}', f'diag/{r}')]; "
           "pathlib.Path(f'runs/{r}/manifeste.json').write_text('{}'); "
           "pathlib.Path(f'diag/{r}/{n}.json').write_text('{\"resultat\": \"factice\"}'); "
           f"sys.exit({code})")
    return [("lecture de P3", "lecture-p3", [sys.executable, "-c", ecr, lecture, "lecture-p3"]),
            ("lecture complémentaire", "lecture-p3bis", [sys.executable, "-c", ecr, lecture_c, "lecture-p3bis"])]


def _main(argv):
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="c", required=True)
    p = sp.add_parser("lectures-fermees")
    p.add_argument("--racine", required=True); p.add_argument("--run", required=True)
    p.add_argument("--lecture", required=True); p.add_argument("--lecture-complementaire", required=True)
    p.add_argument("--prereg", required=True); p.add_argument("--entropie", type=int, required=True)
    a = ap.parse_args(argv)
    if os.environ.get("FAUX_ARGV"):
        open(os.environ["FAUX_ARGV"], "w").write(" ".join(argv) + "\n")
    o.commandes_des_lectures = commandes
    return o.lectures_fermees(a.racine, a.run, a.lecture, a.lecture_complementaire, a.prereg, a.entropie)


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
EOF
mkdir -p "$V" prereg
cp "$E/recuperation_p3bis_v1.sh" "$E/detruire_p3bis_v1.sh" "$E/verifications_p3bis_v1.py" "$V/"
(cd "$V" && for s in *.sh *.py; do sha256sum "$s" > "$s.sha256"; done)
git add -A && git commit -qm "base du banc de la récupération" || exit 2
texte() { mkdir -p prereg; printf '# Préenregistrement factice (banc de la récupération de P3-bis)\n\n- Entropie : `%s`\n' "$1" > "$P"; (cd prereg && sha256sum "$(basename "$P")" > "$(basename "$P").sha256"); }
texte "$ENT"; git add -A && git commit -qm "S (banc)" && S0=$(git rev-parse HEAD)
git checkout -q -b autre-s HEAD~1 && texte 111111111111111111111; git add -A && git commit -qm "S autre entropie" && S_ENT=$(git rev-parse HEAD); git checkout -q main
git clone -q --bare . "$E/distant.git" && git push -q "$E/distant.git" autre-s || exit 2
cd "$E" || exit 2
# --- branches de calcul fabriquées comme l'instance les pousse ------------------------------------------------------
instance() {   # $1 nom, $2 branche, $3 S de base, $4 commandes avant le commit (dans le clone de l'instance), $5 « run » ou « traces »
    local nom=$1 br=$2 base=$3 avant=$4 genre=${5:-run} d="$E/instance-$1"
    git clone -q "$E/distant.git" "$d" && cd "$d" || return 1
    git checkout -q "$base" && git checkout -q -b "$br"
    git config user.name "instance de calcul (P3-bis)"; git config user.email instance-calcul@invalid; git config commit.gpgsign false; git config push.negotiate false
    mkdir -p "traces/p3bis-$nom"; echo "journal factice ($nom)" > "traces/p3bis-$nom/journal.txt"; (cd "traces/p3bis-$nom" && sha256sum -- * > empreintes.sha256)
    if [ "$genre" = run ]; then
        mkdir -p "runs/$RUN" "diag/$RUN" "donnees/$RUN"
        echo '{"run_id": "factice"}' > "runs/$RUN/manifeste.json"
        echo '{"resultat": {"comptes": 240}}' > "diag/$RUN/resume.json"; echo '{"resultat": {"sondes": []}}' > "diag/$RUN/sondes-figees.json"
        for n in sondes-figees.npz sondes-figees-legeres.npz scores-p3.npz jetons-principales-p3.npz textes-actions-p3.jsonl; do head -c 4096 /dev/urandom > "donnees/$RUN/$n"; done
        echo '{"resultat": {"episodes": "factices"}}' > "diag/$RUN/episodes-p3.json"
        PYTHONPATH=src "$PYB" -B -m controle_ia.scellement sceller "runs/$RUN/manifeste.json" "diag/$RUN/resume.json" "diag/$RUN/sondes-figees.json" \
            "diag/$RUN/episodes-p3.json" donnees/"$RUN"/* > /dev/null || return 1
        PYTHONPATH=src "$PYB" -B -c "import sys; from controle_ia.premier_test_ia.ouverture_p3bis_v1 import fermer_run; fermer_run('.', sys.argv[1])" "$RUN" || return 1
    fi
    if [ "$avant" != ":" ]; then eval "$avant" || return 1; fi
    for x in runs diag traces; do [ -e "$x" ] && git add "$x"; done; git commit -qm "P3-bis (reel), run $RUN (fichiers du run en second paquet)" || return 1
    git push -q -f origin "$br" || return 1
    cd "$E" || return 1
}
recup() {   # $1 nom, $2 code attendu, $3 KO attendu (ou « - »), $4 S, $5 branche ; puis variables
    local nom=$1 attendu=$2 koa=$3 s=$4 br=$5 c v; shift 5
    NCAS=$((NCAS + 1))
    env -i PATH=/usr/bin:/bin HOME="$E" LANG=C.UTF-8 "$@" bash "$E/recuperation_p3bis_v1.sh" "$s" "$br" "$E/recup-$nom" > "$E/console-$nom.txt" 2>&1; c=$?
    v=CONFORME
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    if [ "$koa" = - ]; then grep -q '^KO' "$E/console-$nom.txt" && v="NON CONFORME (KO inattendu : $(grep '^KO' "$E/console-$nom.txt" | head -2 | tr '\n' ' ' | cut -c1-200))"
    else grep -q "^KO  .*$koa" "$E/console-$nom.txt" || v="NON CONFORME (KO « $koa » absent)"; fi
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(grep -c '^KO' "$E/console-$nom.txt") KO ; $v"
    { grep '^KO' "$E/console-$nom.txt" | head -2; grep -v '^$' "$E/console-$nom.txt" | tail -1; } | cut -c1-170 | sed -e 's/NON CONFORME/non conforme (cité)/g' -e 's/^/    | /'
}
apres() {
    local desc=$1; shift
    NCAS=$((NCAS + 1))
    if (eval "$*") > /dev/null 2>&1; then echo "    $desc : CONFORME"; else echo "    $desc : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
}
tete() { git --git-dir="$E/distant.git" rev-parse "refs/heads/$1"; }
# R00 : cas sain
instance r00 calcul/p3bis-reel-v1 "$S0" : || { echo "montage R00 impossible"; exit 2; }
T00=$(tete calcul/p3bis-reel-v1)
recup R00-sain 0 - "$S0" calcul/p3bis-reel-v1 FAUX_ARGV="$E/argv-R00.txt"
PAQ="diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar"
apres "lectures-fermees appelée en mode décisif : --prereg $P --entropie $ENT" "grep -q -- '--prereg $P --entropie $ENT\$' '$E/argv-R00.txt'"
apres "branche distante : un seul commit de plus, qui n'ajoute que le paquet et son compagnon ; paquet de 16 783 360 octets à l'empreinte imprimée" \
    "[ \"\$(git --git-dir='$E/distant.git' rev-parse refs/heads/calcul/p3bis-reel-v1^)\" = '$T00' ] && [ \"\$(git --git-dir='$E/distant.git' diff --name-only '$T00' refs/heads/calcul/p3bis-reel-v1 | tr '\n' ' ')\" = '$PAQ $PAQ.sha256 ' ] && [ \"\$(git --git-dir='$E/distant.git' cat-file -s refs/heads/calcul/p3bis-reel-v1:$PAQ)\" = 16783360 ] && grep -q \"\$(git --git-dir='$E/distant.git' show refs/heads/calcul/p3bis-reel-v1:$PAQ | sha256sum | cut -c1-64)\" '$E/console-R00-sain.txt'"
apres "rapport écrit (récupération.rapport.txt) ; aucune ligne de la classe 2 affichée (seules les lignes de code et l'empreinte)" \
    "[ -s '$E/recup-R00-sain.rapport.txt' ] && ! grep -q 'factice' '$E/console-R00-sain.txt' && [ \$(grep -c '^    code ' '$E/console-R00-sain.txt') = 4 ]"
apres "clone : aucun fichier du run en clair, aucune sortie de lecture restée (non suivis et ignorés compris)" \
    "[ ! -e '$E/recup-R00-sain/donnees/$RUN' ] && [ ! -e '$E/recup-R00-sain/diag/$RUN/episodes-p3.json' ] && [ ! -e '$E/recup-R00-sain/espace-ferme-p3bis' ] && ! ls -d '$E/recup-R00-sain'/runs/*-p3bis-lecture* 2>/dev/null | grep -q ."
# refus de départ
recup R01-branche-main 2 - "$S0" main
recup R01b-branche-autre 2 - "$S0" calcul/p3-reel-v1
mkdir -p "$E/recup-R01c-dossier-existant"; recup R01c-dossier-existant 2 - "$S0" calcul/p3bis-reel-v1
recup R01d-s-invalide 2 - "abc" calcul/p3bis-reel-v1
NCAS=$((NCAS + 1)); env -i PATH=/usr/bin:/bin HOME="$E" bash "$ICI/recuperation_p3bis_v1.sh" "$S0" calcul/p3bis-reel-v1 "$E/recup-R01e" > "$E/console-R01e.txt" 2>&1
[ $? = 2 ] && grep -q A_EPINGLER "$E/console-R01e.txt" && echo "R01e-epingle-non-remplie : code 2 ; CONFORME" || { echo "R01e-epingle-non-remplie : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# artefacts (branche calcul/p3bis-reel-v2, réécrite à chaque cas)
B2=calcul/p3bis-reel-v2
instance r02 $B2 "$S0" : && recup R02-s-non-ancetre 1 "1a S n'est pas ancêtre" "$S_ENT" $B2
instance r03 $B2 "$S0" "git add -f donnees/$RUN/scores-p3.npz donnees/$RUN/scores-p3.npz.sha256" && recup R03-donnees-en-clair 1 "1c FICHIER DU RUN EN CLAIR" "$S0" $B2
apres "fichier du run en clair : aucune lecture, aucun commit poussé" "[ \"\$(tete $B2)\" = \"\$(git -C '$E/instance-r03' rev-parse HEAD)\" ]"
instance r04 $B2 "$S0" "git add -f diag/$RUN/episodes-p3.json" && recup R04-episodes-en-clair 1 "1c FICHIER DU RUN EN CLAIR" "$S0" $B2
instance r05 $B2 "$S0" "echo '# modifié' >> $V/detruire_p3bis_v1.sh && git add $V/detruire_p3bis_v1.sh" && recup R05-modification 1 "1b 1 changement" "$S0" $B2
instance r06 $B2 "$S0" "mkdir -p runs/20261112-090000-p3bis-reel && cp runs/$RUN/manifeste.json* runs/20261112-090000-p3bis-reel/" && recup R06-deux-runs 1 "1d runs" "$S0" $B2
instance r07 $B2 "$S0" "git -c user.name=autre commit -q --allow-empty -m autre" && recup R07-auteur-autre 1 "1e auteurs" "$S0" $B2
instance r08 $B2 "$S0" "echo '0000000000000000000000000000000000000000000000000000000000000000  resume.json' > diag/$RUN/resume.json.sha256" && recup R08-sceau-faux 1 "2a verifier-arbre" "$S0" $B2
instance r09 $B2 "$S0" "git rm -q --cached diag/$RUN/resume.json diag/$RUN/resume.json.sha256 2>/dev/null; rm -f diag/$RUN/resume.json diag/$RUN/resume.json.sha256; echo '{\"motif\": \"essai\"}' > diag/$RUN/arret.json && PYTHONPATH=src '$PYB' -B -m controle_ia.scellement sceller diag/$RUN/arret.json > /dev/null"
recup R09-run-sans-resume 4 - "$S0" $B2
apres "run sans résumé : rapport « SANS LECTURE », aucun commit poussé" "grep -q 'RÉCUPÉRATION SANS LECTURE (RUN SANS RÉSUMÉ) : TOUS CONFORMES' '$E/console-R09-run-sans-resume.txt' && [ \"\$(tete $B2)\" = \"\$(git -C '$E/instance-r09' rev-parse HEAD)\" ]"
instance r10 $B2 "$S0" : traces && recup R10-aucun-run 4 - "$S0" $B2
apres "aucun run : traces seules, code 4" "grep -q 'RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN), SANS LECTURE : TOUS CONFORMES' '$E/console-R10-aucun-run.txt'"
instance r11 $B2 "$S0" "rm -f diag/$RUN/paquet-run-ferme-v1.json diag/$RUN/paquet-run-ferme-v1.json.sha256" && recup R11-second-paquet-absent 1 "3 second paquet absent" "$S0" $B2
instance r12 $B2 "$S0" "printf 'X' | dd of=diag/$RUN/paquet-run-ferme-v1.tar.000 bs=1 seek=600 conv=notrunc 2>/dev/null && rm diag/$RUN/paquet-run-ferme-v1.tar.000.sha256 && PYTHONPATH=src '$PYB' -B -m controle_ia.scellement sceller diag/$RUN/paquet-run-ferme-v1.tar.000 > /dev/null"
recup R12-second-paquet-altere 1 "4 lectures fermées : code 1" "$S0" $B2
apres "second paquet altéré : dépliage refusé, aucun commit poussé, aucun fichier en clair resté" \
    "[ \"\$(tete $B2)\" = \"\$(git -C '$E/instance-r12' rev-parse HEAD)\" ] && [ ! -e '$E/recup-R12-second-paquet-altere/donnees/$RUN' ]"
git -C "$E/source" push -q "$E/distant.git" autre-s 2>/dev/null
instance r13 $B2 "$S_ENT" : && recup R13-entropie-autre 1 "3 entropie du texte" "$S_ENT" $B2
instance r14 $B2 "$S0" : && recup R14-lecture-en-echec 1 "4 lectures fermées : code 1, 2 code(s) 0 sur 4" "$S0" $B2 FAUX_LECTURE_ECHEC=1
apres "lecture en échec : aucun commit poussé" "[ \"\$(tete $B2)\" = \"\$(git -C '$E/instance-r14' rev-parse HEAD)\" ]"
instance r15 $B2 "$S0" : && { cp "$E/recuperation_p3bis_v1.sh" "$E/recuperation-autre.sh"; echo "# ligne ajoutée" >> "$E/recuperation-autre.sh"
    NCAS=$((NCAS + 1)); env -i PATH=/usr/bin:/bin HOME="$E" bash "$E/recuperation-autre.sh" "$S0" $B2 "$E/recup-R15" > "$E/console-R15.txt" 2>&1
    [ $? = 1 ] && grep -q '^KO  0 récupération exécutée ≠ copie versée à S' "$E/console-R15.txt" && echo "R15-copie-non-versee : code 1 ; CONFORME" || { echo "R15-copie-non-versee : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }; }
# --- destruction -----------------------------------------------------------------------------------------------------
cat > "$E/bin/vastai" <<'EOF'
#!/usr/bin/env bash
# faux outil de location du banc de la destruction : n'appelle aucun service
S=${SCENARIO:?}
echo "$*" >> "$S/actions"
case "$1 $2" in
  "destroy instance") [ -e "$S/destroy-echec" ] && { echo "erreur factice" >&2; exit 1; }; touch "$S/detruite"; echo '{"success": true}' ;;
  "show instances")
    l='{"id": 58936096, "actual_status": "exited", "cur_state": "stopped"}'
    { [ ! -e "$S/detruite" ] || [ -e "$S/encore-listee" ]; } && l="$l, {\"id\": 99999999, \"actual_status\": \"exited\", \"cur_state\": \"stopped\"}"
    echo "[$l]" ;;
  *) echo "verbe inattendu : $*" >&2; exit 9 ;;
esac
EOF
chmod +x "$E/bin/vastai"
mkdir -p "$E/traces-d"; printf 'branche calcul/p3bis-reel-v1\ninstance 99999999\n' > "$E/traces-d/lancement.txt"
detr() {   # $1 nom, $2 code attendu, $3 motif, $4 motif.txt (ou « - »), $5 gardée (oui/non), $6 rapport, $7 identifiant
    local nom=$1 attendu=$2 motif=$3 m=$4 g=$5 rap=$6 id=${7:-99999999} c v s="$E/scenario-$1" sv="$E/surv-$1"
    mkdir -p "$s" "$sv"; [ "$m" = - ] || echo "$m" > "$sv/motif.txt"; [ "$g" = oui ] && echo "second paquet en échec" > "$sv/instance-gardee"
    NCAS=$((NCAS + 1))
    env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$s" bash "$E/detruire_p3bis_v1.sh" "$id" "$E/traces-d" "$sv" "$rap" > "$E/console-$nom.txt" 2>&1; c=$?
    v=CONFORME
    [ "$c" = "$attendu" ] || v="NON CONFORME (code $c, attendu $attendu)"
    tail -1 "$E/console-$nom.txt" | grep -qF -- "$motif" || v="NON CONFORME (motif « $motif » absent)"
    if [ "$attendu" = 2 ] && grep -q destroy "$s/actions" 2>/dev/null; then v="NON CONFORME (destruction appelée malgré le refus)"; fi
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $v"; tail -1 "$E/console-$nom.txt" | cut -c1-170 | sed 's/^/    | /'
}
RAP_OK="$E/recup-R00-sain.rapport.txt"
detr D00-sain 0 "DESTRUCTION : instance 99999999 détruite" FIN non "$RAP_OK"
apres "destruction : un seul appel, par l'identifiant ; ligne à consigner" "[ \"\$(grep -c '^destroy instance 99999999\$' '$E/scenario-D00-sain/actions')\" = 1 ] && grep -q 'détruite par son identifiant' '$E/surv-D00-sain/arrets-a-consigner.txt'"
detr D01-instance-gardee 2 "instance gardée" GARDER oui "$RAP_OK"
detr D01b-gardee-meme-motif-fin 2 "instance gardée" FIN oui "$RAP_OK"
detr D02-processus-mort 2 "sans motif FIN (PROCESSUS MORT)" "PROCESSUS MORT" non "$RAP_OK"
detr D02b-sans-motif 2 "sans motif FIN (absent)" - non "$RAP_OK"
detr D03-recuperation-non-conforme 2 "récupération non conforme" FIN non "$E/console-R12-second-paquet-altere.txt"
printf 'RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures %s poussé sur calcul/p3bis-reel-v2\n' "$(printf 'a%.0s' {1..64})" > "$E/rapport-autre-branche.txt"
detr D04-autre-branche 2 "d'une autre branche" FIN non "$E/rapport-autre-branche.txt"
detr D05-identifiant-autre 2 "ce lanceur a créé 99999999" FIN non "$RAP_OK" 99999998
printf 'branche calcul/p3bis-reel-v1\ninstance 58936099\n' > "$E/traces-d/lancement.txt"
detr D06-instance-toleree 2 "ARRETEES_TOLEREES" FIN non "$RAP_OK" 58936099
printf 'branche calcul/p3bis-reel-v1\ninstance 99999999\n' > "$E/traces-d/lancement.txt"
mkdir -p "$E/scenario-D07-destruction-en-echec"; touch "$E/scenario-D07-destruction-en-echec/destroy-echec"
detr D07-destruction-en-echec 1 "DESTRUCTION EN ÉCHEC : code 1" FIN non "$RAP_OK"
mkdir -p "$E/scenario-D08-encore-listee"; touch "$E/scenario-D08-encore-listee/encore-listee"
detr D08-encore-listee 1 "liste relue « présente »" FIN non "$RAP_OK"
NCAS=$((NCAS + 1)); env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" SCENARIO="$E/scenario-D09" bash "$E/detruire_p3bis_v1.sh" 99999999 "$E/traces-d" > "$E/console-D09.txt" 2>&1
[ $? = 2 ] && echo "D09-usage : code 2 ; CONFORME" || { echo "D09-usage : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
apres "les instances tolérées ne sont jamais visées par un verbe (tout le banc)" "! cat '$E'/scenario-*/actions | grep -qE '^(destroy|stop) instance 589361'"
echo "cas joués : $NCAS"
echo "FIN DU BANC DE LA RÉCUPÉRATION DE P3-BIS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ]
