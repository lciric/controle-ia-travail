#!/bin/bash
# Rejoue les essais (auteur v1, contre-lecture v1, auteur v2, vérification v2, auteur v3 et erratum 2) et les essais des
# nouveautés (lanceur v3, gardien v4) sur les pièces de ce dossier, factices seulement. N'écrit que sous ce dossier (base tirée
# de l'emplacement du script). Le vrai programme n'est JAMAIS exécuté : la copie factice le porte (pour son empreinte) et
# l'interprète passé au lanceur est un factice qui exécute un programme factice à sa place.
# Sorties : essais/resultats/SUF-<partie>-<essai>.txt.
# Usage : rejouer-tout-v4.sh SUF PARTIE      (PARTIE : 1 lanceur et unités ; 2 auteur v1 ; 3 contre-lecture, identité,
#                                              auteur v2 ; 4 vérification v2, erratum 2 ; 5 nouveautés du gardien v4)
set -u
SUF=$1
PARTIE=$2
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
PY=/home/user/controle-ia-travail/.venv/bin/python
PREEL=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py
R=$E/resultats
A=$E/a-$SUF-$PARTIE
X=$SUF-$PARTIE
if [ -e "$A" ]; then echo "refus : $A existe" >&2; exit 1; fi
mkdir -p "$A" "$R"
echo "début $(date -u +%Y-%m-%dT%H:%M:%SZ) ; base $B ; partie $PARTIE"
sha256sum "$B/lancer-essai-3-v3.sh" "$B/demarrer-essai-3-v3.sh" "$B/verifier-commande-v3.py" "$B/gardien-essai-3-v4.py" "$B/demarrer-gardien-essai-3-v4.sh" "$B/complement.md" "$PREEL" > "$R/$X-empreintes.txt"
cat "$R/$X-empreintes.txt"
bash "$E/preparer-copie-factice-v4.sh" "$A/copie" "$PREEL" d7f949acd9ac92e998e57663d2cc741de93f18c3
C=$A/copie
SC="bash $E/scenario-v4.sh"
H="--heure-arret-duree @HEURE+3600@"
G="--intervalle-s 1 --delai-force-s 5 $H --arret-mesure arme"
P1=$E/copies/auteur-v1/programme-factice-v1.py
CL=$E/copies/contre-lecture-v1
VV=$E/copies/verification-v2
P2=$E/copies/v2/prog-factice-v2.py
P3=$E/copies/v3/prog-v3.py

case "$PARTIE" in
1)
  bash "$E/essais-lanceur-refus-v4.sh" "$A/refus" "$B/lancer-essai-3-v3.sh" "$PREEL" "$P1" "$PY" > "$R/$X-refus.txt" 2>&1; echo "refus (vérification) : $(tail -n 1 "$R/$X-refus.txt")"
  bash "$E/lanceur-emploi-refus-v4.sh" emploi-$X "$PREEL" > "$R/$X-emploi.txt" 2>&1; echo "refus (emploi) : $(tail -n 1 "$R/$X-emploi.txt")"
  bash "$E/argv-v4.sh" argv-$X "$PREEL" > "$R/$X-argv.txt" 2>&1; echo "argv et vérificateur : $(tail -n 1 "$R/$X-argv.txt")"
  "$PY" -I -B "$E/copies/auteur-v1/essai-projection-v1.py" "$B/gardien-essai-3-v4.py" > "$R/$X-projection-v1.txt"; echo "projection v1 : $(tail -n 1 "$R/$X-projection-v1.txt")"
  "$PY" -I -B "$E/copies/v2/essai-projection-v2.py" "$B/gardien-essai-3-v4.py" > "$R/$X-projection-v2.txt"; echo "projection v2 : $(tail -n 1 "$R/$X-projection-v2.txt")"
  "$PY" -I -B "$E/essai-lire-heure-v4.py" "$B/gardien-essai-3-v4.py" > "$R/$X-lire-heure.txt"; echo "lecture de l'heure : $(tail -n 1 "$R/$X-lire-heure.txt")"
  bash "$E/essai-heure-depart-v4.sh" heure-$X > "$R/$X-heure-depart.txt" 2>&1; echo "départ du gardien et heure : $(tail -n 1 "$R/$X-heure-depart.txt")"
  "$PY" -I -B "$VV/essai-arret.py" "$B/gardien-essai-3-v4.py" "$A/arbre-arret" > "$R/$X-essai-arret.txt" 2>&1; echo "colonne d'arrêt : $(head -n 1 "$R/$X-essai-arret.txt")"
  ;;
2)
  $SC s1-sain-place-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 -- --intervalle-s 1 --seuil-libre-octets 1 $H --arret-mesure arme > "$R/$X-s1.txt" 2>&1
  $SC s2-artefact-place-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 --sans-fin -- --intervalle-s 1 --seuil-libre-octets 1000000000000000000 $H --arret-mesure arme > "$R/$X-s2.txt" 2>&1
  $SC s3-sain-mesure-n-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 12 -- --intervalle-s 1 $H --arret-mesure arme > "$R/$X-s3.txt" 2>&1
  $SC s4-artefact-mesure-n-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 40 --octets-par-source 100000 -- --intervalle-s 1 $H --arret-mesure arme > "$R/$X-s4.txt" 2>&1
  $SC s5-sain-mesure-duree-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 1 --max-sources 10 -- --intervalle-s 1 --duree-etape-4-s 30 $H --arret-mesure arme > "$R/$X-s5.txt" 2>&1
  $SC s6-artefact-mesure-duree-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 1 --max-sources 8 --sans-fin -- --intervalle-s 1 --duree-etape-4-s 5 $H --arret-mesure arme > "$R/$X-s6.txt" 2>&1
  $SC s8-artefact-mesure-n1-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 30 --max-sources 3 --sans-fin -- --intervalle-s 1 --duree-etape-4-s 3 $H --arret-mesure arme > "$R/$X-s8.txt" 2>&1
  $SC s9-artefact-identite-groupe-$X 0 pgid-faux "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 -- --intervalle-s 1 --seuil-libre-octets 1000000000000000000 $H --arret-mesure arme > "$R/$X-s9.txt" 2>&1
  $SC s7-artefact-arret-force-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 4 --sans-fin --ignorer-terme -- --intervalle-s 1 --seuil-n 2 $H --arret-mesure arme > "$R/$X-s7.txt" 2>&1
  echo "auteur v1 s1 à s9 : fait"
  ;;
3)
  $SC h1-$X 1 0 "$C" "$CL/prog_factice.py" @S@ 0.5 1000 60 1 "$CL/enfant_factice.py" @M@ -- --seuil-n 5 --seuil-libre-octets 1 $G > "$R/$X-h1.txt" 2>&1
  $SC h3-$X 0 0 "$C" "$CL/prog_factice.py" @S@ 0.001 100000 30 0 "$CL/enfant_factice.py" @M@ -- --seuil-n 300 --seuil-libre-octets 1 $G > "$R/$X-h3.txt" 2>&1
  $SC h4-$X 0 0 "$C" "$CL/prog_factice.py" @S@ 0.5 1000 60 2 "$CL/enfant_sourd.py" @M@ -- --seuil-n 5 --seuil-libre-octets 1 $G > "$R/$X-h4.txt" 2>&1
  $SC c2-sain-$X 0 0 "$C" "$CL/prog_factice.py" @S@ 0.5 1000 60 2 "$CL/enfant_factice.py" @M@ -- --seuil-n 5 --seuil-libre-octets 1 $G > "$R/$X-c2-sain.txt" 2>&1
  echo "contre-lecture : fait"
  bash "$E/decoy-v4.sh" decoy-absent-$X ABSENT place > "$R/$X-decoy-absent.txt" 2>&1
  bash "$E/decoy-v4.sh" decoy-decale-$X -7 place > "$R/$X-decoy-decale.txt" 2>&1
  bash "$E/decoy-v4.sh" decoy-exact-$X 0 place > "$R/$X-decoy-exact.txt" 2>&1
  bash "$E/decoy-v4.sh" decoy-absent-duree-$X ABSENT duree > "$R/$X-decoy-absent-duree.txt" 2>&1
  bash "$E/decoy-v4.sh" decoy-decale-duree-$X -7 duree > "$R/$X-decoy-decale-duree.txt" 2>&1
  bash "$E/decoy-v4.sh" decoy-exact-duree-$X 0 duree > "$R/$X-decoy-exact-duree.txt" 2>&1
  bash "$E/decoy-perime-v4.sh" decoy-perime-$X > "$R/$X-decoy-perime.txt" 2>&1
  echo "identité : fait"
  $SC c5-sain-$X 0 0 "$C" "$P2" @S@ --max-sources 20 --sans-fin -- --seuil-n 6 $G > "$R/$X-c5-sain.txt" 2>&1
  $SC c5-artefact-$X 0 0 "$C" "$P2" @S@ --max-sources 20 --sans-fin --contenu-manifeste-3 "ARRET IMMEDIAT n=999 libres=0 projection impossible" -- --seuil-n 6 $G > "$R/$X-c5-artefact.txt" 2>&1
  $SC c6-sain-$X 0 0 "$C" "$P2" @S@ --max-sources 6 --presque-arret -- --seuil-n 100 $G > "$R/$X-c6-sain.txt" 2>&1
  $SC c6-artefact-$X 0 0 "$C" "$P2" @S@ --max-sources 6 --arret-a 3 -- --seuil-n 100 $G > "$R/$X-c6-artefact.txt" 2>&1
  echo "auteur v2 : fait"
  ;;
4)
  $SC sourd-groupe-$X 0 0 "$C" "$VV/prog-v.py" @S@ 0.5 1000 60 sourd-groupe @M@ -- --seuil-n 5 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-sourd-groupe.txt" 2>&1
  $SC sourd-hors-$X 0 0 "$C" "$VV/prog-v.py" @S@ 0.5 1000 60 sourd-hors @M@ -- --seuil-n 5 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-sourd-hors.txt" 2>&1
  $SC docile-hors-$X 0 0 "$C" "$VV/prog-v.py" @S@ 0.5 1000 60 docile-hors @M@ -- --seuil-n 5 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-docile-hors.txt" 2>&1
  $SC chef-tue-$X 0 4 "$C" "$VV/prog-v.py" @S@ 0.5 1000 20 simple @M@ -- --seuil-n 1000 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-chef-tue.txt" 2>&1
  $SC orphelin-$X 0 0 "$C" "$VV/prog-v.py" @S@ 0.5 1000 60 orphelin @M@ -- --seuil-n 8 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-orphelin.txt" 2>&1
  $SC rapide-$X 0 0 "$C" "$VV/prog-v.py" @S@ 0.001 100000 30 simple @M@ -- --seuil-n 300 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-rapide.txt" 2>&1
  echo "vérification v2 : fait"
  $SC e2c1-sain-$X 0 3 "$C" "$P3" @S@ @M@ --pas 0.5 --duree 8 -- --seuil-n 1000 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-e2c1-sain.txt" 2>&1
  $SC e2c1-place-$X 1 3 "$C" "$P3" @S@ @M@ --pas 0.5 --duree 60 --gros-apres 5 --gros-octets 300000000 -- --seuil-n 1000 --seuil-libre-octets @LIBRES_MOINS_100M@ --duree-etape-4-s 100000 $G > "$R/$X-e2c1-place.txt" 2>&1
  $SC e2c1-mesure-$X 0 3 "$C" "$P3" @S@ @M@ --pas 0.5 --duree 60 -- --seuil-n 12 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-e2c1-mesure.txt" 2>&1
  $SC e2c1-sourd-$X 0 3 "$C" "$P3" @S@ @M@ --pas 0.5 --duree 60 --sourd -- --seuil-n 12 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$X-e2c1-sourd.txt" 2>&1
  bash "$E/ecrivain-externe-v4.sh" ecrivain-$X "$C" > "$R/$X-ecrivain.txt" 2>&1
  echo "erratum 2 : fait"
  ;;
5)
  # Arrêt de durée (A)
  $SC d1-duree-non-atteinte-$X 1 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 -- --intervalle-s 1 --delai-force-s 5 --heure-arret-duree @HEURE+3600@ > "$R/$X-d1.txt" 2>&1
  $SC d1b-duree-apres-la-fin-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 -- --intervalle-s 1 --delai-force-s 5 --heure-arret-duree @HEURE+25@ > "$R/$X-d1b.txt" 2>&1
  $SC d2-duree-atteinte-$X 1 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 --sans-fin -- --intervalle-s 1 --delai-force-s 5 --heure-arret-duree @HEURE+8@ > "$R/$X-d2.txt" 2>&1
  $SC d2b-duree-atteinte-sourd-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 4 --sans-fin --ignorer-terme -- --intervalle-s 1 --delai-force-s 5 --heure-arret-duree @HEURE+8@ > "$R/$X-d2b.txt" 2>&1
  $SC d2c-duree-atteinte-descendants-$X 1 3 "$C" "$P3" @S@ @M@ --pas 0.5 --duree 60 -- --intervalle-s 1 --delai-force-s 5 --seuil-libre-octets 1 --heure-arret-duree @HEURE+10@ > "$R/$X-d2c.txt" 2>&1
  $SC d2d-duree-deja-passee-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 --sans-fin -- --intervalle-s 1 --delai-force-s 5 --heure-arret-duree @HEURE-60@ > "$R/$X-d2d.txt" 2>&1
  $SC d2e-duree-atteinte-hors-groupe-sourd-$X 1 0 "$C" "$VV/prog-v.py" @S@ 0.5 1000 60 sourd-hors @M@ -- --intervalle-s 1 --delai-force-s 5 --seuil-libre-octets 1 --heure-arret-duree @HEURE+8@ > "$R/$X-d2e.txt" 2>&1
  $SC d2f-duree-atteinte-groupe-sourd-$X 0 0 "$C" "$CL/prog_factice.py" @S@ 0.5 1000 60 2 "$CL/enfant_sourd.py" @M@ -- --intervalle-s 1 --delai-force-s 5 --seuil-libre-octets 1 --heure-arret-duree @HEURE+8@ > "$R/$X-d2f.txt" 2>&1
  echo "arrêt de durée : fait"
  # Arrêt de mesure désarmé (B)
  $SC m1-mesure-desarmee-defaut-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.3 --max-sources 30 -- --intervalle-s 1 --delai-force-s 5 --seuil-n 5 --duree-etape-4-s 2 --heure-arret-duree @HEURE+3600@ > "$R/$X-m1.txt" 2>&1
  $SC m1b-mesure-desarmee-explicite-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.3 --max-sources 30 -- --intervalle-s 1 --delai-force-s 5 --seuil-n 5 --duree-etape-4-s 2 --arret-mesure desarme --heure-arret-duree @HEURE+3600@ > "$R/$X-m1b.txt" 2>&1
  $SC m1c-mesure-desarmee-seuil-d-emploi-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.2 --max-sources 40 -- --intervalle-s 1 --delai-force-s 5 --heure-arret-duree @HEURE+3600@ > "$R/$X-m1c.txt" 2>&1
  $SC m2-mesure-armee-temoin-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.3 --max-sources 30 -- --intervalle-s 1 --delai-force-s 5 --seuil-n 5 --duree-etape-4-s 100000 --arret-mesure arme --heure-arret-duree @HEURE+3600@ > "$R/$X-m2.txt" 2>&1
  echo "arrêt de mesure désarmé : fait"
  # Arrêt de place gardé, mesure désarmée (valeurs d'emploi sauf le seuil)
  $SC p1-place-gardee-$X 1 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 --sans-fin -- --intervalle-s 1 --delai-force-s 5 --seuil-libre-octets 1000000000000000000 --heure-arret-duree @HEURE+3600@ > "$R/$X-p1.txt" 2>&1
  $SC p1b-place-saine-$X 0 0 "$C" "$P1" @S@ --delai-etape-3 1 --pas 0.5 --max-sources 8 -- --intervalle-s 1 --delai-force-s 5 --heure-arret-duree @HEURE+3600@ > "$R/$X-p1b.txt" 2>&1
  echo "arrêt de place : fait"
  ;;
*) echo "partie inconnue : $PARTIE" >&2; exit 2 ;;
esac
echo "fin $(date -u +%Y-%m-%dT%H:%M:%SZ)"
