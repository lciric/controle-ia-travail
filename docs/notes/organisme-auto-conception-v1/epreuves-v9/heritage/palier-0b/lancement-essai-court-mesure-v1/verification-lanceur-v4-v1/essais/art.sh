#!/bin/bash
# Artefacts sur MA copie (git archive du commit) : chaque cas mute la copie, lance le lanceur v4 en --verifier-seulement avec les
# valeurs d'emploi (aucun remplacement ; la commande n'est jamais exécutée), rend le code, puis restaure.
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v5
L=$V/pieces/lancer-essai-3-v4.sh
I=$V/pieces/interp-factice.sh
R=$V/copie
B=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b
PREREG=$B/preenregistrement-heritage-palier-0b-etage-processeur-v19.md
PROG=$B/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py
mkdir -p "$V/t" "$V/s"
cas() {  # cas NOM ATTENDU [RACINE]
  local nom=$1 att=$2 r=${3:-$R}
  mkdir -p "$V/t/$nom"
  bash $L "$V/t/$nom" "$r" "$I" "$V/s/$nom" --verifier-seulement > /dev/null 2> "$V/t/$nom/stderr.txt"
  local c=$?
  local v=TENU
  [ "$c" != "$att" ] && v="ÉCART"
  echo "$nom : attendu $att ; rendu $c ; $v ; $(grep -o 'refus de départ.*' "$V/t/$nom/stderr.txt" | cut -c1-150)"
}
refaire() { (cd "$R" && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | LC_ALL=C sort -z | xargs -0 sha256sum) > "$R/EMPREINTES-DE-LA-COPIE.txt"; }
restaurer_liste() { cp "$V/ma-liste.txt" "$R/EMPREINTES-DE-LA-COPIE.txt"; }

cas saine 0

ln -s /etc/hostname "$R/$B/lien-fichier"; cas lien-fichier-ajoute 12; rm "$R/$B/lien-fichier"
ln -s /tmp "$R/$B/lien-dossier"; cas lien-dossier-ajoute 12; rm "$R/$B/lien-dossier"
ln -s /nexiste/pas "$R/.lien-brise-cache"; cas lien-brise-cache 12; rm "$R/.lien-brise-cache"
echo x > "$R/$B/en-trop.txt"; cas fichier-en-trop 12; rm "$R/$B/en-trop.txt"
mkdir -p "$R/.cache/a/b"; echo x > "$R/.cache/a/b/.cache"; cas fichier-cache-profond 12; rm -r "$R/.cache"
echo x > "$R/.cache-racine"; cas fichier-cache-racine 12; rm "$R/.cache-racine"
printf 'x' > "$R/$B/nom
avec-saut"; cas nom-avec-saut-de-ligne 12; rm "$R/$B/nom
avec-saut"
ln "$R/$PREREG" "$R/$B/lien-dur.md"; cas lien-dur-ajoute 12; rm "$R/$B/lien-dur.md"

cp -p "$R/$PREREG" "$V/sauve-prereg"
echo "trafic" >> "$R/$PREREG"; cas modifie-liste-intacte 12
refaire; cas modifie-liste-refaite 12; restaurer_liste
cp -p "$V/sauve-prereg" "$R/$PREREG"

cp -p "$R/$PROG" "$V/sauve-prog"
echo "# trafic" >> "$R/$PROG"; cas programme-modifie-liste-intacte 12
refaire; cas programme-modifie-liste-refaite 12; restaurer_liste
cp -p "$V/sauve-prog" "$R/$PROG"

mv "$R/$PREREG" "$V/sauve-prereg2"; cas fichier-supprime 12
refaire; cas fichier-supprime-liste-refaite 12; restaurer_liste
mv "$V/sauve-prereg2" "$R/$PREREG"

rm "$R/$PREREG"; ln -s "$V/sauve-prereg" "$R/$PREREG"; cas fichier-remplace-par-lien-meme-contenu 12
rm "$R/$PREREG"; cp -p "$V/sauve-prereg" "$R/$PREREG"

mkfifo "$R/$B/tube"; cas tube-nomme 12; rm "$R/$B/tube"

echo "d7f949acd9ac92e998e57663d2cc741de93f18c3" > "$V/commit-sauve"
rm "$R/COMMIT-DE-LA-COPIE.txt"; ln -s "$V/commit-sauve" "$R/COMMIT-DE-LA-COPIE.txt"; cas commit-en-lien 11
rm "$R/COMMIT-DE-LA-COPIE.txt"; cp "$V/commit-sauve" "$R/COMMIT-DE-LA-COPIE.txt"

sed 's/^./0/' "$V/ma-liste.txt" > /dev/null
head -c 1 "$V/ma-liste.txt" > /dev/null
{ printf 'f'; tail -c +2 "$V/ma-liste.txt"; } > "$R/EMPREINTES-DE-LA-COPIE.txt"; cas liste-alteree-un-octet 12; restaurer_liste

# Limites attendues : mode, fichier de même contenu, dossier vide
chmod +x "$R/$PREREG"; cas mode-change-NON-VERIFIE 0; chmod -x "$R/$PREREG"
touch "$R/$PREREG"; cas touch-memes-octets 0
mkdir "$R/dossier-vide-ajoute"; cas dossier-vide-ajoute-NON-VERIFIE 0; rmdir "$R/dossier-vide-ajoute"

# Tenue dans la racine (refus sûr attendu)
mkdir -p "$R/tenue-dedans"; bash $L "$R/tenue-dedans" "$R" "$I" "$V/s/dedans" --verifier-seulement > /dev/null 2> "$V/t/dedans.txt"; echo "tenue-dans-la-racine : attendu 12 ; rendu $?"; rm -r "$R/tenue-dedans"

# Racine en lien
ln -sfn "$R" "$V/lien-racine"; cas racine-en-lien 12 "$V/lien-racine"

cas saine-de-nouveau 0
