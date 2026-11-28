#!/usr/bin/env bash
# Relecture « données et fuites », v1 : contenu du commit S. Les lignes 87 à 92 des contrôles avant dépense (bloc 1)
# sont extraites telles quelles du script relu et rejouées sur trois commits jetables : S sain (texte, configuration et
# leurs sceaux, tous ajoutés), S qui ajoute un cinquième fichier (un fichier de textes), S qui modifie la configuration au
# lieu de l'ajouter. Écrit seulement sous W.
set -uo pipefail
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees
CTL=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine/controles_avant_depense_p4_v1.sh
J=$W/jouet-b
X=$W/contenu-s
export HOME=$W/maison TMPDIR=$W/tmp GIT_CONFIG_NOSYSTEM=1
[ -e "$X" ] && { echo "$X existe déjà (R12)"; exit 2; }
sed -n '86,92p' "$CTL" > "$W/tmp/bloc1.sh"
echo "bloc 1 extrait du script relu ($(sha256sum "$CTL" | cut -c1-12)…), lignes 86 à 92 :"; sed 's/^/    | /' "$W/tmp/bloc1.sh" | cut -c1-160
git clone -q "$J/distant.git" "$X" && cd "$X" || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
BASE=$(git rev-parse HEAD)
P=prereg/P4-instrument-v1.md; CFG=prereg/P4-instrument-config-v1.json
jouer() {   # $1 nom ; S = HEAD
    local S echec=0
    S=$(git rev-parse HEAD)
    ok() { echo "    OK  $*"; }; ko() { echo "    KO  $*"; echec=1; }
    echo "[$1]"
    # shellcheck disable=SC1090
    . "$W/tmp/bloc1.sh"
}
# préparation : le texte et la configuration jouets sont retirés dans un commit B, puis remis par S
git rm -q "$P" "$P.sha256" "$CFG" "$CFG.sha256" && git commit -qm "B : avant S" && B=$(git rev-parse HEAD)
git checkout -q "$BASE" -- "$P" "$P.sha256" "$CFG" "$CFG.sha256" && git commit -qm "S sain" && jouer "S sain : quatre fichiers ajoutés"
git checkout -q "$B"
git checkout -q "$BASE" -- "$P" "$P.sha256" "$CFG" "$CFG.sha256"
mkdir -p donnees/x && echo '{"texte": "essai"}' > donnees/x/textes.jsonl && git add -f donnees/x/textes.jsonl
git commit -qm "S + un fichier de textes" && jouer "S qui ajoute un cinquième fichier (fichier de textes)"
git checkout -q "$BASE"
echo '{"essai": 1}' > "$CFG" && sha256sum "$CFG" | sed "s|  .*|  $(basename "$CFG")|" > "$CFG.sha256"
git checkout -q "$BASE" -- "$P"; git add "$CFG" "$CFG.sha256" && git commit -qm "S qui modifie la configuration" \
    && jouer "S qui modifie la configuration (aucun ajout du sceau du texte)"
cd "$W" && rm -rf "$X" "$W/tmp/bloc1.sh"
echo "FIN"
