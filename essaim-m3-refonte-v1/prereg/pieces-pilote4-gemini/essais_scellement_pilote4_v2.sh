#!/usr/bin/env bash
# Essais (R5) du script de scellement du pilote 4, v2 (`sceller_pilote4_v2.py`) : un cas sain (texte d'essai scellé, graines
# recalculées depuis l'entropie écrite) et sept artefacts, chacun dans un dossier neuf. Aucun fichier du dépôt n'est
# touché : tout est écrit sous DOSSIER_ESSAIS.
# Usage : bash essais_scellement_pilote4_v2.sh SCRIPT PYTHON DOSSIER_ESSAIS
set -uo pipefail
S="$1"; PY="$2"; E="$3"
[ -e "$E" ] && { echo "refus : $E existe déjà (R12)"; exit 2; }
mkdir -p "$E"
n=0; ok=0
preparer() {  # preparer DOSSIER : texte d'essai, pièces, contre-lecture du texte avec compagnon
  local d="$1"
  mkdir -p "$d/prereg/pieces" "$d/prereg/contre-lectures"
  printf '# texte d essai\nentropie E = <<ENTROPIE>> tirée au scellement\n   graine de la course v5-3 = <<GRAINE_V53>>\n   graine de la course v6-1 = <<GRAINE_V6X>>\nempreintes : <<EMPREINTE_PIECES>>\n' > "$d/prereg/pilote4-gemini-organisme-v9.md"
  printf 'pièce\n' > "$d/prereg/pieces/piece.txt"
  printf 'contre-lecture\n' > "$d/prereg/contre-lectures/pilote4-gemini-organisme-v9-cl1.md"
  (cd "$d/prereg/contre-lectures" && sha256sum pilote4-gemini-organisme-v9-cl1.md > pilote4-gemini-organisme-v9-cl1.md.sha256)
}
cas() {  # cas NOM ATTENDU CLE [préparation…]
  local nom="$1" attendu="$2" cle="$3"; shift 3
  local d="$E/$nom"; preparer "$d"
  [ $# -gt 0 ] && (cd "$d/prereg" && eval "$*")
  n=$((n + 1))
  local sortie; sortie="$("$PY" -I "$S" "$d/prereg/pilote4-gemini-organisme-v9.md" "$d/prereg/pieces" "$d/prereg/contre-lectures" "$cle" 2>&1)"; local code=$?
  if echo "$sortie" | grep -qF -- "$attendu"; then ok=$((ok + 1)); echo "OK     $nom (code $code) : « $attendu »"
  else echo "ÉCHEC  $nom (code $code) : attendu « $attendu » ; sortie : $sortie"; fi
}
echo "== script : $(sha256sum "$S" | cut -d' ' -f1) ; $("$PY" -I -c 'import numpy, platform; print("python", platform.python_version(), "numpy", numpy.__version__)')"
cas sain "scellé : pilote4-gemini-organisme-v9.md" v6-1
d="$E/sain/prereg"; n=$((n + 1))
if "$PY" -I -c '
import re, sys, numpy, hashlib, pathlib
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
e = int(re.search(r"entropie E = ([0-9]+)", t).group(1))
g = [int(c.generate_state(1, dtype=numpy.uint64)[0]) for c in numpy.random.SeedSequence(e).spawn(2)]
assert f"graine de la course v5-3 = {g[0]}" in t and f"graine de la course v6-1 = {g[1]}" in t
assert not re.search(r"<<[A-Z0-9_]+>>", t)
h = hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest()
assert pathlib.Path(sys.argv[1] + ".sha256").read_text().split()[0] == h
emp = pathlib.Path(sys.argv[2]) / "EMPREINTES-pilote4-gemini-v1.txt"
he = hashlib.sha256(emp.read_bytes()).hexdigest()
assert f"`{he}`" in t and "contre-lectures/pilote4-gemini-organisme-v9-cl1.md" in emp.read_text()
' "$d/pilote4-gemini-organisme-v9.md" "$d/pieces"; then ok=$((ok + 1)); echo "OK     sain-graines : graines recalculées depuis l'entropie écrite, compagnon juste, empreinte des pièces écrite, contre-lecture comprise"
else echo "ÉCHEC  sain-graines"; fi
cas marqueur-redaction "marqueurs de rédaction [[…]] restants" v6-1 "printf '[[CONTRE_LECTURE]]\n' >> pilote4-gemini-organisme-v9.md"
cas marqueur-double "présent 2 fois" v6-1 "printf '<<ENTROPIE>>\n' >> pilote4-gemini-organisme-v9.md"
cas sans-contre-lecture-du-texte "aucune contre-lecture de pilote4-gemini-organisme-v9.md" v6-1 "rm contre-lectures/pilote4-gemini-organisme-v9-cl1.md contre-lectures/pilote4-gemini-organisme-v9-cl1.md.sha256; printf 'x\n' > contre-lectures/pilote4-gemini-organisme-v8-cl1.md; (cd contre-lectures && sha256sum pilote4-gemini-organisme-v8-cl1.md > pilote4-gemini-organisme-v8-cl1.md.sha256)"
cas compagnon-faux "compagnon pilote4-gemini-organisme-v9-cl1.md.sha256 faux" v6-1 "printf 'ajout\n' >> contre-lectures/pilote4-gemini-organisme-v9-cl1.md"
cas sans-compagnon "sans compagnon .sha256" v6-1 "rm contre-lectures/pilote4-gemini-organisme-v9-cl1.md.sha256"
cas empreintes-existantes "existe déjà (R12)" v6-1 "printf 'x\n' > pieces/EMPREINTES-pilote4-gemini-v1.txt"
cas cle-inattendue "clé de course 'v7' inattendue" v7
echo "== bilan : $ok sur $n cas conformes =="
