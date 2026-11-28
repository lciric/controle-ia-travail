#!/usr/bin/env bash
# Relecture « données et fuites », v1 : données de P3 de la table « Données lues » (R11). Les lignes 118 à 126 des
# contrôles avant dépense (bloc 3) sont extraites telles quelles du script relu et rejouées en lecture seule sur le dépôt
# de travail (commit HEAD ; git show et git cat-file seulement, GIT_OPTIONAL_LOCKS=0), avec pour texte une copie du
# candidat 1 : cas sain, puis deux artefacts (une empreinte de la table changée d'un signe ; un chemin de la table vers un
# fichier absent). Empreintes seulement : aucun contenu de fichier n'est affiché. Écrit seulement sous W.
set -uo pipefail
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees
CTL=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine/controles_avant_depense_p4_v1.sh
CAND=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-candidat1.md
export GIT_OPTIONAL_LOCKS=0 HOME=$W/maison TMPDIR=$W/tmp GIT_CONFIG_NOSYSTEM=1
X=$W/donnees-p3
[ -e "$X" ] && { echo "$X existe déjà (R12)"; exit 2; }
mkdir -p "$X"
sed -n '118,126p' "$CTL" > "$X/bloc3.sh"
echo "bloc 3 extrait du script relu ($(sha256sum "$CTL" | cut -c1-12)…), lignes 118 à 126 ; texte : copie du candidat 1 ($(sha256sum "$CAND" | cut -c1-12)…)"
cp "$CAND" "$X/sain.md"
# artefact 1 : dernière empreinte de la table (train.jsonl) changée d'un signe
python3 - "$CAND" "$X/empreinte-fausse.md" "$X/fichier-absent.md" <<'EOF'
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
lignes = re.findall(r"^\| `[^`]+` \| `[0-9a-f]{64}` \|.*$", t, re.M)
assert len(lignes) == 10, len(lignes)
derniere = lignes[-1]
e = re.search(r"`([0-9a-f]{64})`", derniere).group(1)
f = "0" if e[0] != "0" else "1"
open(sys.argv[2], "w", encoding="utf-8").write(t.replace(derniere, derniere.replace(e, f + e[1:])))
premiere = lignes[1]   # sondes-figees-legeres.npz → chemin d'un fichier absent
open(sys.argv[3], "w", encoding="utf-8").write(t.replace(premiere, premiere.replace("sondes-figees-legeres.npz", "sondes-figees-absentes.npz")))
EOF
cd /home/user/controle-ia-travail || exit 2
S=$(git rev-parse HEAD); echo "commit relu (HEAD du dépôt de travail) : $S"
for cas in sain empreinte-fausse fichier-absent; do
    P="$X/$cas.md"
    echec=0; ok() { echo "    OK  $*"; }; ko() { echo "    KO  $*"; echec=1; }
    echo "[$cas]"
    # shellcheck disable=SC1090
    . "$X/bloc3.sh"
    rm -f "$W/table-donnees.txt"
done
cd "$W" && rm -rf "$X"
echo "FIN"
