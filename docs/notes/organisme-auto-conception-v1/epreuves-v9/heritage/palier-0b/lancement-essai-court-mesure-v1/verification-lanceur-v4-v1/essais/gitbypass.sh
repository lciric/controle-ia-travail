#!/bin/bash
# Voie « avec .git » du lanceur v4 : ma copie reçoit un .git (clone à moi, HEAD sur le commit, index lu de l'arbre). Un lien et un
# fichier ajoutés, non suivis, sont-ils refusés ? Un fichier suivi modifié l'est-il ?
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v5
L=$V/pieces/lancer-essai-3-v4.sh
I=$V/pieces/interp-factice.sh
R=$V/copie
B=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b
cp -r $V/gitclone/.git $R/.git
cas() {
  mkdir -p "$V/t/g-$1"
  bash $L "$V/t/g-$1" "$R" "$I" "$V/s/g-$1" --verifier-seulement > /dev/null 2> "$V/t/g-$1/stderr.txt"
  echo "$1 : attendu $2 ; rendu $? ; $(grep -o 'racine avec .git\|racine sans .git' "$V/t/g-$1/stderr.txt" | head -1)"
}
cas git-saine 0
ln -s /etc/hostname "$R/$B/lien-non-suivi"; cas git-lien-non-suivi-ajoute 12; rm "$R/$B/lien-non-suivi"
echo x > "$R/$B/code-v6/src/intrus.py"; cas git-fichier-non-suivi-ajoute 12; rm "$R/$B/code-v6/src/intrus.py"
echo "trafic" >> "$R/$B/preenregistrement-heritage-palier-0b-etage-processeur-v19.md"; cas git-fichier-suivi-modifie 12
sed -i '$ d' "$R/$B/preenregistrement-heritage-palier-0b-etage-processeur-v19.md"
rm -rf $R/.git
cas retour-sans-git 0
