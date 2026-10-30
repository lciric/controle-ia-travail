#!/bin/sh
# Lance les passages de la v8 (R12 : aucune sortie existante n'est écrasée, le script refuse). Quatre voies (deux processeurs : voie1 puis voie3, voie2 puis voie4) :
#   sh lancer-passages-v8.sh voie1 ... voie4         À lancer depuis le dossier du script.
# Chaque passage écrit lui-même sa sortie, son journal et son manifeste (GD4-05). Durée maximale par passage : 1 500 s (25 minutes) ; au-delà, le passage est
# interrompu, ne laisse que son journal, et sera relancé avec --repetitions 1000 sous un autre nom (et dit comme tel dans le rapport).
# GD7-09 : aucune commande git, ni ici ni dans le script ; le commit est déclaré sur la ligne de commande (texte ci-dessous).
# Périmètre : k = 8 (9 pour le neuvième comparateur), τ = 0,01, δ = 0,05, lecture (A) m = 2 (seuil 40), seuil 160 en référence, α_c = 0,05, biais 0 et δ/4 = 0,0125,
# K_h ∈ {10, 5}, K_s = 10 (20 pour R4), 2 000 répétitions, graine 20261029.
set -u
S=simulation-puissance-garde-delta-v8
PY="python3 -I -B $S.py"
LIM="timeout 1500"
COMMIT="non lu : aucune commande git permise à la lignée conv-audit pour cette tâche, dépôt non interrogé (GD7-09)"
COMMUN="--repetitions 2000 --taux 0.01 --deltas 0.05 --biais 0,0.0125 --lecture-ebh A --m 8,2 --sans-n80 --commit-declare"
TAILLES4="--tailles 288,400,500,650"
N80="--n80-fiche --cibles-n80 0.8,0.9"
COMB="--echelle-dispersion beta --combiner-dispersion-a-et-comparateurs"
passage() {  # passage NOM OPTIONS...
  nom=$1; shift
  $LIM $PY $COMMUN "$COMMIT" "$@" --sortie $S-sortie-$nom.json
  echo "$nom : code $?"
}
# paire de dispersions de A et des comparateurs : A à ρ_A, comparateurs à ρ_B
ab() { echo "$COMB --effet-unite-beta $1 --rho-comparateurs $2"; }
R1="--comparateurs 8 --K 10,5 --K-s 10 $TAILLES4 $N80"
case "$1" in
voie1)
  passage rho0 $R1                                                       # R1 : sans dispersion
  passage meme-rho0.17 $R1 $(ab 0.17 0.17)                               # R1 : A et B au même ρ
  passage moitie-rho0.17 $R1 $(ab 0.17 0.085)                            # R1 : B à ρ/2
  passage copule-rho0.17-c0.5 $R1 $(ab 0.17 0.17) --correlation-sujet-comparateurs 0.5   # R2
  passage copule-rho0.17-c0.8 $R1 $(ab 0.17 0.17) --correlation-sujet-comparateurs 0.8
  passage ks20-rho0.17 --comparateurs 8 --K 10,5 --K-s 20 $TAILLES4 $N80 $(ab 0.17 0.17)   # R4
  passage ks20-rho0.05 --comparateurs 8 --K 10,5 --K-s 20 $TAILLES4 $N80 $(ab 0.05 0.05)
  passage ks20-rho0 --comparateurs 8 --K 10,5 --K-s 20 --tailles 288
  # R3 : strates, 288 et 400 unités, A et B à ρ = 0,17
  R3="--comparateurs 8 --K 10,5 --K-s 10 --tailles 288,400 $(ab 0.17 0.17)"
  for S_ in 2 3; do for G in 0.2 0.4; do
    passage strates-sujet-S$S_-g$G-brut $R3 --strates $S_ --amplitude-strates $G --portee-strates sujet
    passage strates-sujet-S$S_-g$G-calibre $R3 --strates $S_ --amplitude-strates $G --portee-strates sujet --calibrage-par-strate
  done; done
  passage strates-sujet-S3-g0.4-iid-brut $R3 --strates 3 --amplitude-strates 0.4 --portee-strates sujet --allocation-strates iid
  for S_ in 2 3; do
    passage strates-commune-S$S_-g0.4-brut $R3 --strates $S_ --amplitude-strates 0.4 --portee-strates commune
    passage strates-commune-S$S_-g0.4-calibre $R3 --strates $S_ --amplitude-strates 0.4 --portee-strates commune --calibrage-par-strate
  done
  ;;
voie2)
  passage meme-rho0.05 $R1 $(ab 0.05 0.05)
  passage meme-rho0.10 $R1 $(ab 0.10 0.10)
  passage moitie-rho0.05 $R1 $(ab 0.05 0.025)
  passage moitie-rho0.10 $R1 $(ab 0.10 0.05)
  passage copule-rho0.10-c0.5 $R1 $(ab 0.10 0.10) --correlation-sujet-comparateurs 0.5
  passage copule-rho0.10-c0.8 $R1 $(ab 0.10 0.10) --correlation-sujet-comparateurs 0.8
  passage ks20-rho0.10 --comparateurs 8 --K 10,5 --K-s 20 $TAILLES4 $N80 $(ab 0.10 0.10)
  passage ks20-Kh20-rho0.17 --comparateurs 8 --K 20 --K-s 10,20 --tailles 288 $(ab 0.17 0.17)
  passage meme-rho0.25 $R1 $(ab 0.25 0.25)
  # R3 avec n80 : meilleur cas de la sensibilité différenciée
  passage strates-n80-sujet-S3-g0.4-brut --comparateurs 8 --K 10,5 --K-s 10 $TAILLES4 $N80 $(ab 0.17 0.17) --strates 3 --amplitude-strates 0.4 --portee-strates sujet
  passage strates-n80-sujet-S3-g0.4-calibre --comparateurs 8 --K 10,5 --K-s 10 $TAILLES4 $N80 $(ab 0.17 0.17) --strates 3 --amplitude-strates 0.4 --portee-strates sujet --calibrage-par-strate
  ;;
voie3|voie4)
  # neuvième comparateur : k = 9 ; voie3 : écart de contraste 0,05 (« comparateur fort », SUPPOSÉ) ; voie4 : 0,10 (comme les huit autres) ; n80 de la fiche (cible 0,8)
  N9="--comparateurs 9 --K 10,5 --K-s 10 $TAILLES4 --n80-fiche"
  if [ "$1" = voie3 ]; then E="--ecart-contraste-neuvieme 0.05"; T=g0.05; else E=""; T=g0.10; fi
  if [ "$1" = voie3 ]; then
    passage neuf-k8-logit1.0 --comparateurs 8 --K 10,5 --K-s 10 $TAILLES4 --n80-fiche --effet-unite-comparateurs 1.0
    passage neuf-k8-beta1.0 --comparateurs 8 --K 10,5 --K-s 10 $TAILLES4 --n80-fiche --effet-unite-comparateurs 1.0 --echelle-dispersion beta
  fi
  passage neuf-k9-$T-nulle $N9 $E
  passage neuf-k9-$T-logit1.0 $N9 $E --effet-unite-comparateurs 1.0
  passage neuf-k9-$T-beta1.0 $N9 $E --effet-unite-comparateurs 1.0 --echelle-dispersion beta
  passage neuf-k9-$T-rho0.05 $N9 $E $(ab 0.05 0.05)
  passage neuf-k9-$T-rho0.10 $N9 $E $(ab 0.10 0.10)
  passage neuf-k9-$T-rho0.17 $N9 $E $(ab 0.17 0.17)
  ;;
*) echo "usage : sh lancer-passages-v8.sh voie1|voie2|voie3|voie4"; exit 2;;
esac
