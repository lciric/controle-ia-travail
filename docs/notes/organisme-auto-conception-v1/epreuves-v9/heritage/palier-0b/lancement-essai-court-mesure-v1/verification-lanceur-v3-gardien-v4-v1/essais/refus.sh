#!/bin/bash
# Refus de départ du lanceur v3 : variantes de copie sans .git et d'interpréteur ; lanceur en --verifier-seulement (la commande
# n'est jamais exécutée). Chaque cas : nom, code attendu, code rendu, sorties jamais créées.
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v4
L=$V/pieces/lancer-essai-3-v3.sh
I=$V/pieces/interp-factice.sh
BASE=$V/a/racine-saine
PROG=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py
A=$V/a/refus
mkdir -p "$A" "$V/t"
refaire_liste() {
  (cd "$1" && find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | sort -z | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt)
}
cas() {  # cas NOM ATTENDU RACINE INTERP [SORTIES]
  local nom=$1 att=$2 r=$3 i=$4 s=${5:-$A/sorties-$1}
  mkdir -p "$V/t/refus-$nom"
  bash $L "$V/t/refus-$nom" "$r" "$i" "$s" --verifier-seulement > /dev/null 2> "$V/t/refus-$nom/stderr.txt"
  local c=$?
  local cree=non
  [ -e "$A/sorties-$nom" ] && cree=OUI
  local verdict=TENU
  [ "$c" != "$att" ] && verdict="ÉCART"
  echo "$nom : attendu $att ; rendu $c ; sorties créées : $cree ; $verdict"
}
copie() { rm -rf "$A/r-$1"; cp -r "$BASE" "$A/r-$1"; }

copie saine;            cas saine 0 "$A/r-saine" $I
copie sanscommit;       rm "$A/r-sanscommit/COMMIT-DE-LA-COPIE.txt"; cas sans-commit 11 "$A/r-sanscommit" $I
copie commitfaux;       echo d7f949acd9ac92e998e57663d2cc741de93f18c4 > "$A/r-commitfaux/COMMIT-DE-LA-COPIE.txt"; cas commit-faux 11 "$A/r-commitfaux" $I
copie commitcrlf;       printf 'd7f949acd9ac92e998e57663d2cc741de93f18c3\r\n' > "$A/r-commitcrlf/COMMIT-DE-LA-COPIE.txt"; cas commit-crlf 11 "$A/r-commitcrlf" $I
copie commitdeux;       printf 'd7f949acd9ac92e998e57663d2cc741de93f18c3\nautre\n' > "$A/r-commitdeux/COMMIT-DE-LA-COPIE.txt"; cas commit-deux-lignes 11 "$A/r-commitdeux" $I
copie sansliste;        rm "$A/r-sansliste/EMPREINTES-DE-LA-COPIE.txt"; cas sans-liste 12 "$A/r-sansliste" $I
copie modifie;          echo "trafic" >> "$A/r-modifie/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src/a.py"; cas fichier-modifie 12 "$A/r-modifie" $I
copie ajoute;           echo "x" > "$A/r-ajoute/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src/intrus.py"; cas fichier-ajoute 12 "$A/r-ajoute" $I
copie manquant;         rm "$A/r-manquant/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/b.py"; cas fichier-manquant 12 "$A/r-manquant" $I
copie lienajoute;       ln -s /etc/hostname "$A/r-lienajoute/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src/lien.py"; cas lien-ajoute-NOUVEAU 12 "$A/r-lienajoute" $I
copie liendossier;      ln -s /tmp "$A/r-liendossier/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src/lienrep"; cas lien-dossier-ajoute-NOUVEAU 12 "$A/r-liendossier" $I
copie progaltere;       echo "# trafic" >> "$A/r-progaltere/$PROG"; refaire_liste "$A/r-progaltere"; cas programme-altere-liste-refaite 13 "$A/r-progaltere" $I
copie autrealtere;      echo "trafic" >> "$A/r-autrealtere/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src/a.py"; refaire_liste "$A/r-autrealtere"; cas autre-fichier-altere-liste-refaite-LIMITE 12 "$A/r-autrealtere" $I
copie gitvide;          mkdir "$A/r-gitvide/.git"; cas git-vide 11 "$A/r-gitvide" $I
copie saine2;           cas racine-absente 11 "$A/nexiste-pas" $I
copie saine3;           mkdir -p "$A/sorties-existe"; cas sorties-existent 10 "$A/r-saine3" $I "$A/sorties-existe"
copie saine4;           cas interp-absent 14 "$A/r-saine4" "$A/pas-d-interprete"
copie saine5;           cas interp-dossier 14 "$A/r-saine5" "$A"
cp "$I" "$A/interp-non-exec.sh"; chmod -x "$A/interp-non-exec.sh"
copie saine6;           cas interp-non-exec 14 "$A/r-saine6" "$A/interp-non-exec.sh"
ln -sfn "$A/pas-la-cible" "$A/interp-lien-casse"
copie saine7;           cas interp-lien-casse 14 "$A/r-saine7" "$A/interp-lien-casse"
copie saine8;           cas chemin-relatif 2 "relatif/racine" $I
