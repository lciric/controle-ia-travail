#!/usr/bin/env bash
# Relecture « données et fuites », v1 : la liste des chemins gelés (CHEMINS_GELES) est lue dans l'arbre même qu'elle
# contrôle. Artefact : dans un clone jetable du S jouet, CHEMINS_GELES exclut src/controle_ia/sondes et un fichier de ce
# dossier change (une ligne de commentaire). On rejoue (a) les commandes du bloc 2 des contrôles avant dépense (liste lue
# dans l'arbre contrôlé), (b) la garde du module `exiger_instrument_fige`, (c) la même comparaison avec la liste lue dans
# 7a54d43 (correction proposée). Cas sain d'abord (arbre non modifié). Écrit seulement sous W.
set -uo pipefail
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
J=$W/jouet-b
X=$W/arbre-gele
CODE_RELU=7a54d431d89745839220f882b41b13e8c62ecfdd
export PYTHONDONTWRITEBYTECODE=1 TMPDIR=$W/tmp HOME=$W/maison GIT_CONFIG_NOSYSTEM=1
[ -e "$X" ] && { echo "$X existe déjà (R12)"; exit 2; }
git clone -q "$J/distant.git" "$X" && cd "$X" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git checkout -q "$(cat "$J/S.txt")"
jouer() {   # $1 nom du cas
    local geles c
    geles=$(PYTHONPATH=src "$PY" -B -c "from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))")
    # shellcheck disable=SC2086
    git diff --quiet "$CODE_RELU" HEAD -- $geles; c=$?
    echo "[$1] (a) bloc 2 des contrôles, liste lue dans l'arbre contrôlé : git diff code $c ($([ $c = 0 ] && echo 'OK : arbre gelé = 7a54d43' || echo 'KO'))"
    PYTHONPATH=src "$PY" -B - <<'EOF'
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("ip", "docs/procedures/P4-instrument-v1/instrument_p4_v1.py")
ip = importlib.util.module_from_spec(spec); spec.loader.exec_module(ip)
try:
    ip.exiger_instrument_fige(Path("."), ip.COMMIT_P3)
    print("    (b) garde du module exiger_instrument_fige : acceptée")
except Exception as e:
    print("    (b) garde du module exiger_instrument_fige : refus :", str(e)[:120])
EOF
    geles=$(git show "$CODE_RELU:src/controle_ia/harnais/validation_reelle.py" | "$PY" -I -B -c 'import ast, sys
t = ast.parse(sys.stdin.read())
v = [n.value for n in t.body if isinstance(n, ast.Assign) and any(getattr(x, "id", "") == "CHEMINS_GELES" for x in n.targets)]
print(" ".join(ast.literal_eval(v[0])))')
    # shellcheck disable=SC2086
    git diff --quiet "$CODE_RELU" HEAD -- $geles; c=$?
    echo "    (c) liste lue dans 7a54d43 (correction) : git diff code $c ($([ $c = 0 ] && echo 'OK' || echo 'KO : arbre gelé différent'))"
}
jouer "cas sain"
sed -i 's|":(exclude)traces", ":(exclude)CLAUDE.md")|":(exclude)traces", ":(exclude)CLAUDE.md", ":(exclude)src/controle_ia/sondes")|' \
    src/controle_ia/harnais/validation_reelle.py
echo "# ligne ajoutée par l'artefact de la relecture" >> src/controle_ia/sondes/evaluation.py
git diff --stat | sed 's/^/    changé : /'
git commit -qam "artefact : CHEMINS_GELES exclut src/controle_ia/sondes ; un fichier de ce dossier change"
jouer "artefact"
cd "$W" && rm -rf "$X"
find "$W" -name __pycache__ -type d | head -3 | sed 's/^/__pycache__ écrit : /'
echo "FIN"
