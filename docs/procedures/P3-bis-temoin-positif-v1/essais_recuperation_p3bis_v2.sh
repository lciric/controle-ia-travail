#!/usr/bin/env bash
# Chaîne v2 (2026-11-11 ; règle (a') de P3-bis : R-2296, R-2320 ; consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`) : copie de `essais_recuperation_p3bis_v1.sh`, gardé
# tel quel (R12), noms de la chaîne en v2 ; runs fabriqués par l'essai de fermeture v3 (800 directions), lectures fermées v3 ; R00 : paquet relu, lecture complémentaire `lecture_p3bis_v2`, 800 et 200 directions.
# Brouillon 3 (2026-11-10, contre-lecture différentielle, CD-05) : témoin fabriqué docs/notes/bras-attaque/ au dépôt
# synthétique ; absent du clone de la récupération (R00), refus s'il est extrait (R16).
# Banc de la récupération et de la destruction de P3-bis (R5), v1, brouillon 2 (2026-11-10, après la fusion du code
# corrigé, branche prep/p3bis-code-v2) : recuperation_p3bis_v2.sh et detruire_p3bis_v2.sh, un cas sain et des artefacts,
# joués contre le VRAI module `ouverture_p3bis_v2` (aucun bouchon) et les VRAIES lectures de P3 et complémentaire en mode
# décisif. Dépôt synthétique : src/ de l'arbre fusionné (code corrigé compris), commit du code cité, texte factice scellé,
# conforme à R1 et R2 dans sa forme (sections, contre-lecture), qui cite le commit du code, l'empreinte canonique de la
# configuration du run et l'entropie de P3 ; chaîne versée (la copie jouée de la récupération et la destruction, scellées) ;
# dépôt nu local. Branches de calcul fabriquées comme l'instance les pousse : auteur « instance de calcul (P3-bis) », run
# source DÉCISIF lancé sous ce texte, fabriqué par `fabriquer_run` de l'essai de fermeture v2 du code corrigé (issue « vu »
# plantée), second paquet fait par `ouverture_p3bis_v2.fermer_run`, traces scellées, aucun fichier du run en clair. Le cas
# sain relit ensuite le paquet poussé (le banc, pas la récupération) : deux manifestes décisifs, issue mécanique « vu »,
# ligne 4. Faux outil de location pour la destruction (verbes journalisés ; aucun service appelé). Aucun appel externe.
# Lignes changées dans la copie jouée de la récupération, comptées et déclarées : DEPOT_URL (dépôt nu local) et PY
# (interpréteur du banc).
# Usage : essais_recuperation_p3bis_v2.sh RACINE_NEUVE
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
for s in recuperation_p3bis_v2.sh detruire_p3bis_v2.sh verifications_p3bis_v2.py; do echo "script éprouvé : $s $(sha256sum "$ICI/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1)"
mkdir -p "$E/bin" && cd "$E" || exit 2
NON_CONFORMES=0; NCAS=0
# --- copie jouée ---------------------------------------------------------------------------------------------------
sed -e "s|^DEPOT_URL=.*|DEPOT_URL=file://$E/distant.git|" -e "s|^PY=A_EPINGLER.*|PY=$PYB|" "$ICI/recuperation_p3bis_v2.sh" > "$E/recuperation_p3bis_v2.sh"
echo "lignes changées dans la copie de la récupération : $(diff "$ICI/recuperation_p3bis_v2.sh" "$E/recuperation_p3bis_v2.sh" | grep -c '^>') (DEPOT_URL, PY)"
[ "$(diff "$ICI/recuperation_p3bis_v2.sh" "$E/recuperation_p3bis_v2.sh" | grep -c '^>')" = 2 ] || { echo "copie de la récupération non sûre"; exit 2; }
cp "$ICI/detruire_p3bis_v2.sh" "$ICI/verifications_p3bis_v2.py" "$E/"
# --- dépôt synthétique ----------------------------------------------------------------------------------------------
git init -q -b main source && cd source || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false; git config push.negotiate false
cp -r "$SRC/src" . && find src -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null
cp "$SRC/pyproject.toml" .; printf '__pycache__/\n*.pyc\ndonnees/\n' > .gitignore
[ -f src/controle_ia/premier_test_ia/ouverture_p3bis_v2.py ] || { echo "module ouverture_p3bis_v2 absent de l'arbre fusionné"; exit 2; }
cat > "$E/fabriquer.py" <<'EOF'
"""Fabrique, dans le clone de l'instance, un run source décisif (`fabriquer_run` de l'essai de fermeture v2 du code
corrigé) et son second paquet (`ouverture_p3bis_v2.fermer_run`) ; aucun fichier du run n'est commité ici."""
import importlib.util, json, sys
from pathlib import Path
clone, run, prereg, entropie, config, essai = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("essai_fermeture_p3bis_v3", essai)
ev2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(ev2)
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob
ev2.fabriquer_run(Path(clone), run, "vu", ev2.graine("vu"), config=json.loads(config), decisif=True, prereg=prereg,
                  entropie=int(entropie))
ob.fermer_run(Path(clone), run)
EOF
cat > "$E/texte.py" <<'EOF'
"""Texte factice scellé (forme de R1 et R2) qui cite le commit du code, la configuration et l'entropie."""
import hashlib, json, sys
from pathlib import Path
from controle_ia.manifeste import config_canonique
from controle_ia.prereg import SECTIONS
from controle_ia.scellement import sceller
chemin, commit, entropie, config = sys.argv[1:5]
corps = ["# Préenregistrement factice (banc de la récupération de P3-bis)", "",
         f"- Commit du code d'analyse : `{commit}`",
         f"- Configuration de P3 (empreinte canonique) : `{hashlib.sha256(config_canonique(json.loads(config))).hexdigest()}`",
         f"- Entropie : `{entropie}`", ""]
for s in SECTIONS[:-1]:
    corps += [f"## {s}", "", f"contenu factice : {s}", ""]
corps += ["## Contre-lecture", "", f"brouillon relu `{'a' * 64}`, rapport `{'b' * 64}`", ""]
p = Path(chemin); p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("\n".join(corps), encoding="utf-8")
sceller(p)
EOF
CONFIG='{"mode": "reel", "max_nouveaux": 64}'
mkdir -p "$V" prereg
cp "$E/recuperation_p3bis_v2.sh" "$E/detruire_p3bis_v2.sh" "$E/verifications_p3bis_v2.py" "$V/"
(cd "$V" && for s in *.sh *.py; do sha256sum "$s" > "$s.sha256"; done)
mkdir -p docs/notes/bras-attaque
echo "témoin fabriqué par le banc (aucun contenu réel) : jamais extrait dans le clone de la récupération (CD-05)" > docs/notes/bras-attaque/temoin-banc.txt
(cd docs/notes/bras-attaque && sha256sum temoin-banc.txt > temoin-banc.txt.sha256)
git add -A && git commit -qm "base du banc de la récupération" || exit 2
CODE=$(git rev-parse HEAD)                       # commit du code cité par le texte (arbre gelé : src/, pyproject, .gitignore)
texte() { PYTHONPATH=src "$PYB" -B "$E/texte.py" "$P" "$CODE" "$1" "$2"; }
texte "$ENT" "$CONFIG"; git add -A && git commit -qm "S (banc)" && S0=$(git rev-parse HEAD)
git checkout -q -b autre-s "$CODE" && texte 111111111111111111111 "$CONFIG"; git add -A && git commit -qm "S autre entropie" && S_ENT=$(git rev-parse HEAD)
git checkout -q -b autre-config "$CODE" && texte "$ENT" '{"mode": "reel", "max_nouveaux": 32}'; git add -A && git commit -qm "S autre configuration citée" && S_CFG=$(git rev-parse HEAD); git checkout -q main
git clone -q --bare . "$E/distant.git" && git push -q "$E/distant.git" autre-s autre-config || exit 2
cd "$E" || exit 2
# --- branches de calcul fabriquées comme l'instance les pousse ------------------------------------------------------
instance() {   # $1 nom, $2 branche, $3 S de base, $4 commandes avant le commit (dans le clone de l'instance), $5 « run » ou « traces »
    local nom=$1 br=$2 base=$3 avant=$4 genre=${5:-run} d="$E/instance-$1"
    git clone -q "$E/distant.git" "$d" && cd "$d" || return 1
    git checkout -q "$base" && git checkout -q -b "$br"
    git config user.name "instance de calcul (P3-bis)"; git config user.email instance-calcul@invalid; git config commit.gpgsign false; git config push.negotiate false
    mkdir -p "traces/p3bis-$nom"; echo "journal factice ($nom)" > "traces/p3bis-$nom/journal.txt"; (cd "traces/p3bis-$nom" && sha256sum -- * > empreintes.sha256)
    if [ "$genre" = run ]; then
        ENT_I=$(sed -n 's/^- Entropie : `\([0-9]*\)`$/\1/p' "$P")
        PYTHONPATH="$d/src" "$PYB" -B "$E/fabriquer.py" "$d" "$RUN" "$P" "$ENT_I" "$CONFIG" "$SRC/scripts/essai_fermeture_p3bis_v3.py" > "$E/fabrication-$nom.txt" 2>&1 \
            || { tail -3 "$E/fabrication-$nom.txt"; return 1; }
    fi
    if [ "$avant" != ":" ]; then eval "$avant" || return 1; fi
    for x in runs diag traces; do [ -e "$x" ] && git add "$x"; done; git commit -qm "P3-bis (reel), run $RUN (fichiers du run en second paquet)" || return 1
    git push -q -f origin "$br" || return 1
    cd "$E" || return 1
}
recup() {   # $1 nom, $2 code attendu, $3 KO attendu (ou « - »), $4 S, $5 branche ; puis variables
    local nom=$1 attendu=$2 koa=$3 s=$4 br=$5 c v; shift 5
    NCAS=$((NCAS + 1))
    env -i PATH=/usr/bin:/bin HOME="$E" LANG=C.UTF-8 "$@" bash "$E/recuperation_p3bis_v2.sh" "$s" "$br" "$E/recup-$nom" > "$E/console-$nom.txt" 2>&1; c=$?
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
recup R00-sain 0 - "$S0" calcul/p3bis-reel-v1
PAQ="diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar"
apres "paquet poussé relu par le banc (vrai module v2) : deux lectures décisives sous le texte, lecture complémentaire lecture_p3bis_v2 (règle (a') sur 800 directions, ancienne règle sur 200), issue mécanique « vu », ligne 4, durées écrites" \
    "git --git-dir='$E/distant.git' show refs/heads/calcul/p3bis-reel-v1:$PAQ > '$E/paquet-R00.tar' && PYTHONPATH='$SRC/src' '$PYB' -B -c '
import json, sys
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob
_, a = ob.relire_paquet_lectures(open(sys.argv[1], \"rb\").read(), int(sys.argv[2]))
f = dict(ob.membres_de(a))
m = [json.loads(v) for k, v in f.items() if k.startswith(\"runs/\") and k.endswith(\"/manifeste.json\")]
l = [json.loads(v)[\"resultat\"] for k, v in f.items() if k.endswith(\"/lecture-p3bis.json\")]
assert len(m) == 2 and all(x[\"decisif\"] is True and x[\"preenregistrement\"][\"chemin\"] == sys.argv[3] for x in m), m
assert len(l) == 1 and l[0][\"issue_mecanique\"] == {\"issue\": \"vu\", \"ligne\": 4}, l
assert sorted(x[\"commande\"] for x in m) == [\"python -m controle_ia.premier_test_ia.lecture\", \"python -m controle_ia.premier_test_ia.lecture_p3bis_v2\"], m
assert l[0][\"etat_decisif\"][\"lecture\"][\"n_plancher\"] == 800 and l[0][\"regle_ancienne_200\"][\"lecture\"][\"n_plancher\"] == 200, l
assert any(k.endswith(ob.DUREES) for k in f)
' '$E/paquet-R00.tar' '$ENT' '$P'"
apres "branche distante : un seul commit de plus, qui n'ajoute que le paquet et son compagnon ; paquet de 16 783 360 octets à l'empreinte imprimée" \
    "[ \"\$(git --git-dir='$E/distant.git' rev-parse refs/heads/calcul/p3bis-reel-v1^)\" = '$T00' ] && [ \"\$(git --git-dir='$E/distant.git' diff --name-only '$T00' refs/heads/calcul/p3bis-reel-v1 | tr '\n' ' ')\" = '$PAQ $PAQ.sha256 ' ] && [ \"\$(git --git-dir='$E/distant.git' cat-file -s refs/heads/calcul/p3bis-reel-v1:$PAQ)\" = 16783360 ] && grep -q \"\$(git --git-dir='$E/distant.git' show refs/heads/calcul/p3bis-reel-v1:$PAQ | sha256sum | cut -c1-64)\" '$E/console-R00-sain.txt'"
apres "clone en extraction partielle : témoin docs/notes/bras-attaque/ absent du disque (CD-05)" \
    "grep -q '^OK  0 clone en extraction partielle' '$E/console-R00-sain.txt' && [ ! -e '$E/recup-R00-sain/docs/notes/bras-attaque' ] && [ -d '$E/recup-R00-sain/src' ]"
apres "rapport écrit (récupération.rapport.txt) ; aucune ligne de la classe 2 affichée (seules les lignes de code et l'empreinte)" \
    "[ -s '$E/recup-R00-sain.rapport.txt' ] && [ \$(grep -c '^    code .* : 0\$' '$E/console-R00-sain.txt') = 4 ] && [ \$(grep -c '^    ' '$E/console-R00-sain.txt') = 5 ]"
apres "clone : aucun fichier du run en clair, aucune sortie de lecture restée (non suivis et ignorés compris)" \
    "[ ! -e '$E/recup-R00-sain/donnees/$RUN' ] && [ ! -e '$E/recup-R00-sain/diag/$RUN/episodes-p3.json' ] && [ ! -e '$E/recup-R00-sain/espace-ferme-p3bis' ] && ! ls -d '$E/recup-R00-sain'/runs/*-p3bis-lecture* 2>/dev/null | grep -q ."
# refus de départ
recup R01-branche-main 2 - "$S0" main
recup R01b-branche-autre 2 - "$S0" calcul/p3-reel-v1
mkdir -p "$E/recup-R01c-dossier-existant"; recup R01c-dossier-existant 2 - "$S0" calcul/p3bis-reel-v1
recup R01d-s-invalide 2 - "abc" calcul/p3bis-reel-v1
NCAS=$((NCAS + 1)); env -i PATH=/usr/bin:/bin HOME="$E" bash "$ICI/recuperation_p3bis_v2.sh" "$S0" calcul/p3bis-reel-v1 "$E/recup-R01e" > "$E/console-R01e.txt" 2>&1
[ $? = 2 ] && grep -q A_EPINGLER "$E/console-R01e.txt" && echo "R01e-epingle-non-remplie : code 2 ; CONFORME" || { echo "R01e-epingle-non-remplie : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
# artefacts (branche calcul/p3bis-reel-v2, réécrite à chaque cas)
B2=calcul/p3bis-reel-v2
instance r02 $B2 "$S0" : && recup R02-s-non-ancetre 1 "1a S n'est pas ancêtre" "$S_ENT" $B2
instance r03 $B2 "$S0" "git add -f donnees/$RUN/scores-p3.npz donnees/$RUN/scores-p3.npz.sha256" && recup R03-donnees-en-clair 1 "1c FICHIER DU RUN EN CLAIR" "$S0" $B2
apres "fichier du run en clair : aucune lecture, aucun commit poussé" "[ \"\$(tete $B2)\" = \"\$(git -C '$E/instance-r03' rev-parse HEAD)\" ]"
instance r04 $B2 "$S0" "git add -f diag/$RUN/episodes-p3.json" && recup R04-episodes-en-clair 1 "1c FICHIER DU RUN EN CLAIR" "$S0" $B2
instance r05 $B2 "$S0" "echo '# modifié' >> $V/detruire_p3bis_v2.sh && git add $V/detruire_p3bis_v2.sh" && recup R05-modification 1 "1b 1 changement" "$S0" $B2
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
apres "second paquet altéré : la ligne « motif du dépliage » du module v2 est admise (classe 1) et affichée" "grep -q '^    motif du dépliage : ' '$E/console-R12-second-paquet-altere.txt' && ! grep -q 'hors de la classe 1' '$E/console-R12-second-paquet-altere.txt'"
apres "second paquet altéré : dépliage refusé, aucun commit poussé, aucun fichier en clair resté" \
    "[ \"\$(tete $B2)\" = \"\$(git -C '$E/instance-r12' rev-parse HEAD)\" ] && [ ! -e '$E/recup-R12-second-paquet-altere/donnees/$RUN' ]"
instance r13 $B2 "$S_ENT" : && recup R13-entropie-autre 1 "3 entropie du texte" "$S_ENT" $B2
instance r14 $B2 "$S_CFG" : && recup R14-lecture-en-echec 1 "4 lectures fermées : code 1, 2 code(s) 0 sur 4" "$S_CFG" $B2
apres "lecture refusée par sa propre garde (configuration citée autre que celle du run) : aucun commit poussé" "[ \"\$(tete $B2)\" = \"\$(git -C '$E/instance-r14' rev-parse HEAD)\" ]"
instance r15 $B2 "$S0" : && { cp "$E/recuperation_p3bis_v2.sh" "$E/recuperation-autre.sh"; echo "# ligne ajoutée" >> "$E/recuperation-autre.sh"
    NCAS=$((NCAS + 1)); env -i PATH=/usr/bin:/bin HOME="$E" bash "$E/recuperation-autre.sh" "$S0" $B2 "$E/recup-R15" > "$E/console-R15.txt" 2>&1
    [ $? = 1 ] && grep -q '^KO  0 récupération exécutée ≠ copie versée à S' "$E/console-R15.txt" && echo "R15-copie-non-versee : code 1 ; CONFORME" || { echo "R15-copie-non-versee : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }; }
# R16 : clone sans l'extraction partielle (copie dont la ligne est changée en « true ») : témoin extrait, refus (code 2)
instance r16 $B2 "$S0" : && {
    sed 's|^git -C "$D" sparse-checkout set --no-cone .*$|true   # artefact du banc : extraction partielle retirée|' "$E/recuperation_p3bis_v2.sh" > "$E/recuperation-r16.sh"
    [ "$(diff "$E/recuperation_p3bis_v2.sh" "$E/recuperation-r16.sh" | grep -c '^>')" = 1 ] || { echo "copie R16 non sûre"; exit 2; }
    NCAS=$((NCAS + 1)); env -i PATH=/usr/bin:/bin HOME="$E" LANG=C.UTF-8 bash "$E/recuperation-r16.sh" "$S0" $B2 "$E/recup-R16" > "$E/console-R16.txt" 2>&1; c=$?
    if [ "$c" = 2 ] && grep -q "REFUS : docs/notes/bras-attaque extrait sur disque" "$E/console-R16.txt" && [ "$(tete $B2)" = "$(git -C "$E/instance-r16" rev-parse HEAD)" ]; then
        echo "R16-extraction-entiere-refusee : code 2 ; CONFORME"
    else echo "R16-extraction-entiere-refusee : code $c ; NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); fi
    grep -v '^$' "$E/console-R16.txt" | tail -1 | cut -c1-170 | sed 's/^/    | /'; }
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
    env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 SCENARIO="$s" bash "$E/detruire_p3bis_v2.sh" "$id" "$E/traces-d" "$sv" "$rap" > "$E/console-$nom.txt" 2>&1; c=$?
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
NCAS=$((NCAS + 1)); env -i PATH="$E/bin:/usr/bin:/bin" HOME="$E" SCENARIO="$E/scenario-D09" bash "$E/detruire_p3bis_v2.sh" 99999999 "$E/traces-d" > "$E/console-D09.txt" 2>&1
[ $? = 2 ] && echo "D09-usage : code 2 ; CONFORME" || { echo "D09-usage : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
apres "les instances tolérées ne sont jamais visées par un verbe (tout le banc)" "! cat '$E'/scenario-*/actions | grep -qE '^(destroy|stop) instance 589361'"
echo "cas joués : $NCAS"
echo "FIN DU BANC DE LA RÉCUPÉRATION DE P3-BIS ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ]
