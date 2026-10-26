#!/usr/bin/env bash
# Essais (R5) du script des graines du pilote 4, v5 (`sceller_pilote4_v5.py`) : ceux de la v4 (`essais_scellement_pilote4_v4.sh`)
# pour le fichier d'empreintes `EMPREINTES-pilote4-gemini-v3.txt`, la clé de course `v6-2-s` (graine = enfant 0), la ligne
# de graine `v6-2` restituée (2334107546136117589) et les marqueurs de la v5 ; deux artefacts de plus : ligne `v6-2`
# absente, ligne `v6-2` à une autre valeur ; la v4 reprenait ceux de la v3 plus un cas sain où le fichier d'empreintes v1
# (celui du texte v3 scellé) existe déjà ; la v3 reprenait ceux de la v2 (`essais_scellement_pilote4_v2.sh` :
# un cas sain, graines recalculées depuis l'entropie écrite, sept artefacts), plus (contre-lecture 2, P4C2-08) un cas sain
# dont la prose nomme l'entropie sans « = », et quatre artefacts : une ligne d'entropie de trop (texte inséré qui en porte une
# suivie d'un nombre, avant la ligne du marqueur), une ligne d'entropie de trop sans nombre, une ligne de graine de trop, une
# ligne de graine d'une autre course. Chacun dans un dossier neuf ; aucun fichier du dépôt n'est touché.
# Usage : bash essais_scellement_pilote4_v5.sh SCRIPT PYTHON DOSSIER_ESSAIS
set -uo pipefail
S="$1"; PY="$2"; E="$3"
[ -e "$E" ] && { echo "refus : $E existe déjà (R12)"; exit 2; }
mkdir -p "$E"
n=0; ok=0
preparer() {  # preparer DOSSIER : texte d'essai, pièces, contre-lecture du texte avec compagnon
  local d="$1"
  mkdir -p "$d/prereg/pieces" "$d/prereg/contre-lectures"
  printf '# texte d essai\nentropie E = <<ENTROPIE>> tirée au scellement\n   graine de la course v6-2-s = <<GRAINE_S>>\n   graine de la course v6-2 = 2334107546136117589\nempreintes : <<EMPREINTE_PIECES>>\n' > "$d/prereg/pilote4-gemini-organisme-v9.md"
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
cas sain "graines écrites : pilote4-gemini-organisme-v9.md" v6-2-s
d="$E/sain/prereg"; n=$((n + 1))
if "$PY" -I -c '
import re, sys, numpy, hashlib, pathlib
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
e = int(re.search(r"entropie E = ([0-9]+)", t).group(1))
g = [int(c.generate_state(1, dtype=numpy.uint64)[0]) for c in numpy.random.SeedSequence(e).spawn(2)]
assert f"graine de la course v6-2-s = {g[0]}" in t and "graine de la course v6-2 = 2334107546136117589" in t and str(g[1]) not in t
assert not re.search(r"<<[A-Z0-9_]+>>", t)
h = hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest()
assert pathlib.Path(sys.argv[1] + ".sha256").read_text().split()[0] == h
emp = pathlib.Path(sys.argv[2]) / "EMPREINTES-pilote4-gemini-v3.txt"
he = hashlib.sha256(emp.read_bytes()).hexdigest()
assert f"`{he}`" in t and "contre-lectures/pilote4-gemini-organisme-v9-cl1.md" in emp.read_text()
' "$d/pilote4-gemini-organisme-v9.md" "$d/pieces"; then ok=$((ok + 1)); echo "OK     sain-graines : graines recalculées depuis l'entropie écrite, compagnon juste, empreinte des pièces écrite, contre-lecture comprise"
else echo "ÉCHEC  sain-graines"; fi
cas marqueur-redaction "marqueurs de rédaction [[…]] restants" v6-2-s "printf '[[CONTRE_LECTURE]]\n' >> pilote4-gemini-organisme-v9.md"
cas marqueur-double "présent 2 fois" v6-2-s "printf '<<ENTROPIE>>\n' >> pilote4-gemini-organisme-v9.md"
cas sans-contre-lecture-du-texte "aucune contre-lecture de pilote4-gemini-organisme-v9.md" v6-2-s "rm contre-lectures/pilote4-gemini-organisme-v9-cl1.md contre-lectures/pilote4-gemini-organisme-v9-cl1.md.sha256; printf 'x\n' > contre-lectures/pilote4-gemini-organisme-v8-cl1.md; (cd contre-lectures && sha256sum pilote4-gemini-organisme-v8-cl1.md > pilote4-gemini-organisme-v8-cl1.md.sha256)"
cas compagnon-faux "compagnon pilote4-gemini-organisme-v9-cl1.md.sha256 faux" v6-2-s "printf 'ajout\n' >> contre-lectures/pilote4-gemini-organisme-v9-cl1.md"
cas sans-compagnon "sans compagnon .sha256" v6-2-s "rm contre-lectures/pilote4-gemini-organisme-v9-cl1.md.sha256"
cas empreintes-existantes "existe déjà (R12)" v6-2-s "printf 'x\n' > pieces/EMPREINTES-pilote4-gemini-v3.txt"
cas cle-inattendue "clé de course 'v6-2' inattendue" v6-2
cas sain-prose-entropie "graines écrites : pilote4-gemini-organisme-v9.md" v6-2-s "printf 'la graine dérive de l entropie E du texte (sans égalité)\n' >> pilote4-gemini-organisme-v9.md"
cas entropie-inseree-avant "2 lignes qui portent « entropie E = » au lieu d'une" v6-2-s "sed -i '1a résumé de contre-lecture : entropie E = 12345 lue dans un essai' pilote4-gemini-organisme-v9.md"
cas entropie-de-trop-sans-nombre "2 lignes qui portent « entropie E = » au lieu d'une" v6-2-s "printf 'rappel : entropie E = celle du scellement\n' >> pilote4-gemini-organisme-v9.md"
cas graine-de-trop "lignes de graine" v6-2-s "printf '   graine de la course v6-2-s = 99\n' >> pilote4-gemini-organisme-v9.md"
cas graine-autre-course "lignes de graine" v6-2-s "printf '   graine de la course v6-3 = 7\n' >> pilote4-gemini-organisme-v9.md"
cas sain-avec-empreintes-v1 "graines écrites : pilote4-gemini-organisme-v9.md" v6-2-s "printf 'empreintes du texte v3\n' > pieces/EMPREINTES-pilote4-gemini-v1.txt; (cd pieces && sha256sum EMPREINTES-pilote4-gemini-v1.txt > EMPREINTES-pilote4-gemini-v1.txt.sha256)"
n=$((n + 1)); if [ "$(cat "$E/sain-avec-empreintes-v1/prereg/pieces/EMPREINTES-pilote4-gemini-v1.txt")" = "empreintes du texte v3" ] && grep -q "pieces/EMPREINTES-pilote4-gemini-v1.txt" "$E/sain-avec-empreintes-v1/prereg/pieces/EMPREINTES-pilote4-gemini-v3.txt"; then ok=$((ok + 1)); echo "OK     sain-avec-empreintes-v1-intact : le fichier v1 n'est pas réécrit et figure au fichier v3"; else echo "ÉCHEC  sain-avec-empreintes-v1-intact"; fi
cas graine-m-absente "ligne absente : graine de la course v6-2 = 2334107546136117589" v6-2-s "sed -i '/graine de la course v6-2 = 2334107546136117589/d' pilote4-gemini-organisme-v9.md"
cas graine-m-autre "ligne absente : graine de la course v6-2 = 2334107546136117589" v6-2-s "sed -i 's/graine de la course v6-2 = 2334107546136117589/graine de la course v6-2 = 2334107546136117580/' pilote4-gemini-organisme-v9.md"
echo "== bilan : $ok sur $n cas conformes =="
