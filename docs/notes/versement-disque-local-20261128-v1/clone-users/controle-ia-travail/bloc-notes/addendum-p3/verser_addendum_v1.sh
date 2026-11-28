#!/usr/bin/env bash
# Versement de l'addendum de P3 dans le dépôt, avant la lecture décisive (garde d'antériorité).
# Usage : verser_addendum_v1.sh DOSSIER_MODULE TEXTE_FINAL DOSSIER_VERIFICATION
# Copie octet pour octet, scelle chaque fichier (R6), scelle le préenregistrement par sceller_prereg (R1, R2).
# N'écrit ni commit ni poussée : la session relit le résultat d'abord.
set -euo pipefail
D=/home/user/controle-ia-travail
A=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
MOD=${1:?dossier du module}; TEXTE=${2:?texte final}; VERIF=${3:?dossier des rapports de vérification}
cd "$D"
[ -z "$(git status --porcelain)" ] || { echo "ARRÊT : arbre de travail sale"; exit 1; }
[ ! -e prereg/P3-addendum-lecture-complementaire-v1.md ] || { echo "ARRÊT : préenregistrement déjà versé"; exit 1; }
P=docs/procedures/P3-addendum-v1; C=prereg/contre-lectures; B=$C/brouillons-addendum-P3-v1
mkdir -p "$P" "$B" "$C/contre-lecture-code-b3-2-addendum-P3-v1"
cp "$MOD/complements_p3_v1.py" "$MOD/test_complements_p3_v1.py" "$P/"
cp "$A/rapports/contre-lecture-R2-brouillon1-addendum-P3-v1.md" "$C/"
cp "$A/rapports/verification-corrections-brouillon2-addendum-P3-v1.md" "$C/"
cp "$A/traitement-R2-addendum-P3-v1.md" "$C/"
cp "$A/rapports/contre-lecture-code-b3-1.md" "$C/contre-lecture-code-b3-1-addendum-P3-v1.md"
cp "$A/rapports/contre-lecture-code-b3-3.md" "$C/contre-lecture-code-b3-3-addendum-P3-v1.md"
mkdir -p "$C/contre-lecture-code-b3-3-addendum-P3-v1"
cp "$A"/rapports/revue-b3-3/essai_07.log "$A"/rapports/revue-b3-3/essai_07b_import.log "$C/contre-lecture-code-b3-3-addendum-P3-v1/"
cp "$VERIF"/verification-code-final-addendum-P3-v1-texte.md "$VERIF"/verification-code-final-addendum-P3-v1-mutants.md "$VERIF"/verification-code-final-addendum-P3-v1-calculs.md "$VERIF"/verification-corrections-brouillon7-addendum-P3-v1.md "$C/"
cp "$A/rapports/revue-b3-2-preuves-v1.tar.gz" "$C/contre-lecture-code-b3-2-addendum-P3-v1/"
cp "$MOD/NOTES-CORRECTIONS-CB1.md" "$C/notes-corrections-code-addendum-P3-v1.md"
mkdir -p "$C/versions-relues-addendum-P3-v1"
cp "$A"/versions-tests/*.py "$C/versions-relues-addendum-P3-v1/"
cp "$MOD/essais/table-mutants.md" "$C/table-mutants-code-addendum-P3-v1.md"
for k in 1 2 3 4 5 6 7 8; do cp "$A/P3-addendum-lecture-complementaire-v1-brouillon$k.md" "$B/"; done
cp "$TEXTE" prereg/P3-addendum-lecture-complementaire-v1.md
export PYTHONPATH=src
$PY -m controle_ia.scellement sceller "$P"/complements_p3_v1.py "$P"/test_complements_p3_v1.py \
  "$C"/contre-lecture-R2-brouillon1-addendum-P3-v1.md "$C"/verification-corrections-brouillon2-addendum-P3-v1.md \
  "$C"/traitement-R2-addendum-P3-v1.md "$C"/contre-lecture-code-b3-1-addendum-P3-v1.md \
  "$C"/contre-lecture-code-b3-3-addendum-P3-v1.md "$C"/verification-code-final-addendum-P3-v1-texte.md "$C"/verification-code-final-addendum-P3-v1-mutants.md "$C"/verification-code-final-addendum-P3-v1-calculs.md "$C"/verification-corrections-brouillon7-addendum-P3-v1.md \
  "$C"/contre-lecture-code-b3-2-addendum-P3-v1/revue-b3-2-preuves-v1.tar.gz "$C"/notes-corrections-code-addendum-P3-v1.md \
  "$C"/table-mutants-code-addendum-P3-v1.md "$C"/contre-lecture-code-b3-3-addendum-P3-v1/*.log "$C"/versions-relues-addendum-P3-v1/*.py "$B"/*.md
$PY -c "from controle_ia.prereg import sceller_prereg; print(sceller_prereg('prereg/P3-addendum-lecture-complementaire-v1.md'))"
# Contrôles : empreintes citées dans le texte égales aux fichiers versés ; arbre scellé intact ; suite du module.
$PY - <<'EOF'
import hashlib, re, pathlib
t = pathlib.Path("prereg/P3-addendum-lecture-complementaire-v1.md").read_text(encoding="utf-8")
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
m = re.search(r"Module de l'addendum \(sha256\) : `([0-9a-f]{64})`", t).group(1)
s = re.search(r"Tests du module \(sha256\) : `([0-9a-f]{64})`", t).group(1)
assert m == sha("docs/procedures/P3-addendum-v1/complements_p3_v1.py"), "module"
assert s == sha("docs/procedures/P3-addendum-v1/test_complements_p3_v1.py"), "tests"
cites = set(re.findall(r"`([0-9a-f]{64})`", t))
verses = {sha(p): str(p) for p in pathlib.Path("prereg/contre-lectures").rglob("*") if p.is_file() and not p.name.endswith(".sha256")}
for e in sorted(cites):
    print(e[:12], verses.get(e, "(hors de prereg/contre-lectures)"))
print("EMPREINTES DU MODULE ET DES TESTS : CONFORMES")
EOF
$PY -m controle_ia.scellement verifier-arbre .
git status --short | head -40
