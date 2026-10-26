#!/usr/bin/env bash
# Essais (R5) du script des graines des courses à question, v6 (`sceller_courses_question_v6.py`) : dérivés de ceux de la v5
# (`essais_scellement_pilote4_v5.sh`) pour un texte `courses-question-gemini-v6-2-v1.md`, deux graines (`maieutique` = enfant 0,
# `audit` = enfant 1 de SeedSequence(E).spawn(2)), sans argument de clé, sans ligne de graine héritée, fichier d'empreintes
# `EMPREINTES-courses-question-v1.txt`. Cas sains : scellement, graines recalculées depuis l'entropie écrite (les deux), prose
# qui nomme l'entropie sans « = », fichier d'empreintes du pilote 4 déjà présent (jamais réécrit, listé). Artefacts : marqueur
# de rédaction, marqueur en double, marqueur manquant, aucune contre-lecture du texte, compagnon faux, sans compagnon,
# empreintes existantes (R12), entropie insérée avant, entropie de trop sans nombre, entropie déjà chiffrée, graine de trop,
# graine d'une autre course, ligne de graine `audit` absente. Chacun dans un dossier neuf ; aucun fichier du dépôt n'est touché.
# Usage : bash essais_scellement_question_v6.sh SCRIPT PYTHON DOSSIER_ESSAIS
set -uo pipefail
S="$1"; PY="$2"; E="$3"
[ -e "$E" ] && { echo "refus : $E existe déjà (R12)"; exit 2; }
mkdir -p "$E"
n=0; ok=0
T="courses-question-gemini-v6-2-v1"
preparer() {  # preparer DOSSIER : texte d'essai, pièces, contre-lecture du texte avec compagnon
  local d="$1"
  mkdir -p "$d/prereg/pieces" "$d/prereg/contre-lectures"
  printf '# texte d essai\nentropie E = <<ENTROPIE>> tirée au scellement\n   graine de la course maieutique = <<GRAINE_MAIEUTIQUE>>\n   graine de la course audit = <<GRAINE_AUDIT>>\nempreintes : <<EMPREINTE_PIECES>>\n' > "$d/prereg/$T.md"
  printf 'pièce\n' > "$d/prereg/pieces/piece.txt"
  printf 'contre-lecture\n' > "$d/prereg/contre-lectures/$T-cl9.md"
  (cd "$d/prereg/contre-lectures" && sha256sum "$T-cl9.md" > "$T-cl9.md.sha256")
}
cas() {  # cas NOM ATTENDU [préparation…]
  local nom="$1" attendu="$2"; shift 2
  local d="$E/$nom"; preparer "$d"
  [ $# -gt 0 ] && (cd "$d/prereg" && eval "$*")
  n=$((n + 1))
  local sortie; sortie="$("$PY" -I "$S" "$d/prereg/$T.md" "$d/prereg/pieces" "$d/prereg/contre-lectures" 2>&1)"; local code=$?
  if echo "$sortie" | grep -qF -- "$attendu"; then ok=$((ok + 1)); echo "OK     $nom (code $code) : « $attendu »"
  else echo "ÉCHEC  $nom (code $code) : attendu « $attendu » ; sortie : $sortie"; fi
}
echo "== script : $(sha256sum "$S" | cut -d' ' -f1) ; $("$PY" -I -c 'import numpy, platform; print("python", platform.python_version(), "numpy", numpy.__version__)')"
cas sain "graines écrites : $T.md"
d="$E/sain/prereg"; n=$((n + 1))
if "$PY" -I -c '
import re, sys, numpy, hashlib, pathlib
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
e = int(re.search(r"entropie E = ([0-9]+)", t).group(1))
g = [int(c.generate_state(1, dtype=numpy.uint64)[0]) for c in numpy.random.SeedSequence(e).spawn(2)]
assert f"graine de la course maieutique = {g[0]}" in t and f"graine de la course audit = {g[1]}" in t and g[0] != g[1]
assert not re.search(r"<<[A-Z0-9_]+>>", t)
h = hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest()
assert pathlib.Path(sys.argv[1] + ".sha256").read_text().split()[0] == h
emp = pathlib.Path(sys.argv[2]) / "EMPREINTES-courses-question-v1.txt"
he = hashlib.sha256(emp.read_bytes()).hexdigest()
assert f"`{he}`" in t and "contre-lectures/courses-question-gemini-v6-2-v1-cl9.md" in emp.read_text()
assert pathlib.Path(sys.argv[2], "EMPREINTES-courses-question-v1.txt.sha256").read_text().split()[0] == he
' "$d/$T.md" "$d/pieces"; then ok=$((ok + 1)); echo "OK     sain-graines : deux graines recalculées depuis l'entropie écrite (enfants 0 et 1), compagnons justes, empreinte des pièces écrite, contre-lecture comprise"
else echo "ÉCHEC  sain-graines"; fi
cas marqueur-redaction "marqueurs de rédaction [[…]] restants" "printf '[[CL9]]\n' >> $T.md"
cas marqueur-double "présent 2 fois" "printf '<<ENTROPIE>>\n' >> $T.md"
cas marqueur-manquant "au lieu de" "sed -i 's/<<GRAINE_AUDIT>>/0/' $T.md"
cas marqueur-de-trop "au lieu de" "printf '<<GRAINE_S>>\n' >> $T.md"
cas sans-contre-lecture-du-texte "aucune contre-lecture de $T.md" "rm contre-lectures/$T-cl9.md contre-lectures/$T-cl9.md.sha256; printf 'x\n' > contre-lectures/$T-brouillon.md; (cd contre-lectures && sha256sum $T-brouillon.md > $T-brouillon.md.sha256)"
cas compagnon-faux "compagnon $T-cl9.md.sha256 faux" "printf 'ajout\n' >> contre-lectures/$T-cl9.md"
cas sans-compagnon "sans compagnon .sha256" "rm contre-lectures/$T-cl9.md.sha256"
cas empreintes-existantes "existe déjà (R12)" "printf 'x\n' > pieces/EMPREINTES-courses-question-v1.txt"
cas sain-prose-entropie "graines écrites : $T.md" "printf 'les graines dérivent de l entropie E du texte (sans égalité)\n' >> $T.md"
cas entropie-inseree-avant "2 lignes qui portent « entropie E = » au lieu d'une" "sed -i '1a résumé de contre-lecture : entropie E = 12345 lue dans un essai' $T.md"
cas entropie-de-trop-sans-nombre "2 lignes qui portent « entropie E = » au lieu d'une" "printf 'rappel : entropie E = celle du scellement\n' >> $T.md"
# la ligne d'entropie chiffrée avant le scellement est refusée par le contrôle de la ligne exacte (le contrôle « porte déjà un
# nombre » du script reste derrière lui, inatteignable tant que la ligne exacte est exigée : défense en profondeur)
cas entropie-deja-chiffree "ligne absente : entropie E = <<ENTROPIE>>" "sed -i 's/entropie E = <<ENTROPIE>> tirée/entropie E = 42 <<ENTROPIE>> tirée/' $T.md"
cas graine-de-trop "lignes de graine" "printf '   graine de la course maieutique = 99\n' >> $T.md"
cas graine-autre-course "lignes de graine" "printf '   graine de la course v6-2-s = 7\n' >> $T.md"
cas graine-audit-absente "ligne absente : graine de la course audit = <<GRAINE_AUDIT>>" "sed -i 's/graine de la course audit = <<GRAINE_AUDIT>>/graine audit <<GRAINE_AUDIT>>/' $T.md"
cas sain-avec-empreintes-pilote4 "graines écrites : $T.md" "printf 'empreintes du texte v5 du pilote 4\n' > pieces/EMPREINTES-pilote4-gemini-v3.txt; (cd pieces && sha256sum EMPREINTES-pilote4-gemini-v3.txt > EMPREINTES-pilote4-gemini-v3.txt.sha256)"
n=$((n + 1)); if [ "$(cat "$E/sain-avec-empreintes-pilote4/prereg/pieces/EMPREINTES-pilote4-gemini-v3.txt")" = "empreintes du texte v5 du pilote 4" ] && grep -q "pieces/EMPREINTES-pilote4-gemini-v3.txt" "$E/sain-avec-empreintes-pilote4/prereg/pieces/EMPREINTES-courses-question-v1.txt"; then ok=$((ok + 1)); echo "OK     sain-avec-empreintes-pilote4-intact : le fichier du pilote 4 n'est pas réécrit et figure au fichier des courses"; else echo "ÉCHEC  sain-avec-empreintes-pilote4-intact"; fi
echo "== bilan : $ok sur $n cas conformes =="
