#!/bin/bash
# Rejoue TOUS les essais (auteur v1, contre-lecture v1, auteur v2, vérification v2, erratum 2) sur les pièces du dossier v3,
# factices seulement. N'écrit que sous le dossier v3 : la base est tirée de l'emplacement de ce script (aucun chemin en dur
# vers un autre dossier d'écriture). Sorties : essais/resultats/SUF-<essai>.txt.
# Usage : rejouer-tout-v3.sh SUF
set -u
SUF=$1
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
PY=/home/user/controle-ia-travail/.venv/bin/python
R=$E/resultats
SORTIES_EMPLOI=/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1
A=$E/a-$SUF
if [ -e "$A" ]; then echo "refus : $A existe" >&2; exit 1; fi
mkdir -p "$A" "$R"
echo "début $(date -u +%Y-%m-%dT%H:%M:%SZ) ; base $B"
sha256sum "$B/lancer-essai-court-v2.sh" "$B/demarrer-essai-court-v2.sh" "$B/gardien-essai-court-v3.py" "$B/demarrer-gardien-essai-court-v3.sh" "$B/verifier-commande-v2.py" > "$R/$SUF-empreintes.txt"
cat "$R/$SUF-empreintes.txt"
G="--intervalle-s 1 --delai-force-s 5"
SC="bash $E/scenario-v3.sh"
CL=$E/contre-lecture-v1-copie
VV=$E/verification-v2-copie

# 1. Commande à l'octet
bash "$E/argv-v3.sh" argv-$SUF > "$R/$SUF-argv.txt" 2>&1; echo "argv et vérificateur : fait"

# 2. Auteur v1 : refus, projections, s1 à s9
bash "$E/auteur-v1-copie/preparer-racine-factice-v1.sh" "$A/racine-factice" "$E/auteur-v1-copie/programme-factice-v1.py"
TETE=$(git -C "$A/racine-factice" rev-parse HEAD)
EMP=$(sha256sum "$A/racine-factice/prog/programme-factice-v1.py" | cut -d' ' -f1)
bash "$E/auteur-v1-copie/essais-lanceur-refus-v1.sh" "$A" "$B/lancer-essai-court-v2.sh" "$TETE" "$EMP" > "$R/$SUF-refus.txt" 2>&1; echo "refus : $(tail -n 1 "$R/$SUF-refus.txt")"
"$PY" -I -B "$E/auteur-v1-copie/essai-projection-v1.py" "$B/gardien-essai-court-v3.py" > "$R/$SUF-projection-v1.txt"; echo "projection v1 : $(tail -n 1 "$R/$SUF-projection-v1.txt")"
"$PY" -I -B "$E/v2-copie/essai-projection-v2.py" "$B/gardien-essai-court-v3.py" > "$R/$SUF-projection-v2.txt"; echo "projection v2 : $(tail -n 1 "$R/$SUF-projection-v2.txt")"
cp "$E/auteur-v1-copie/fabriquer-lanceur-factice-v1.py" "$A/"
bash "$E/auteur-v1-copie/preparer-scenarios-v1.sh" "$A" "$B/lancer-essai-court-v2.sh" "$TETE" "$EMP" > "$R/$SUF-preparer.txt" 2>&1
mkdir -p "$A/scenarios/s9-artefact-identite-groupe/tenue"
"$PY" -I -B "$A/fabriquer-lanceur-factice-v1.py" "$B/lancer-essai-court-v2.sh" "$A/scenarios/s9-artefact-identite-groupe/lanceur-factice.sh" "$A/racine-factice" "$TETE" "$EMP" "$A/racine-factice/prog/programme-factice-v1.py" "$A/scenarios/s9-artefact-identite-groupe/sorties" "$PY -I -B $A/racine-factice/prog/programme-factice-v1.py $A/scenarios/s9-artefact-identite-groupe/sorties --delai-etape-3 1 --pas 0.5 --max-sources 8" > /dev/null
J="bash $E/jouer-scenario-v3.sh"
S=$A/scenarios
$J $S/s1-sain-place 60 normal --intervalle-s 1 --seuil-libre-octets 1 > "$R/$SUF-s1.txt" 2>&1
$J $S/s2-artefact-place 90 normal --intervalle-s 1 --seuil-libre-octets 1000000000000000000 > "$R/$SUF-s2.txt" 2>&1
$J $S/s3-sain-mesure-n 90 normal --intervalle-s 1 > "$R/$SUF-s3.txt" 2>&1
$J $S/s4-artefact-mesure-n 90 normal --intervalle-s 1 > "$R/$SUF-s4.txt" 2>&1
$J $S/s5-sain-mesure-duree 90 normal --intervalle-s 1 --duree-etape-4-s 30 > "$R/$SUF-s5.txt" 2>&1
$J $S/s6-artefact-mesure-duree 90 normal --intervalle-s 1 --duree-etape-4-s 5 > "$R/$SUF-s6.txt" 2>&1
$J $S/s8-artefact-mesure-n1 90 normal --intervalle-s 1 --duree-etape-4-s 3 > "$R/$SUF-s8.txt" 2>&1
$J $S/s9-artefact-identite-groupe 60 pgid-faux --intervalle-s 1 --seuil-libre-octets 1000000000000000000 > "$R/$SUF-s9.txt" 2>&1
# s7 : déclenché par n (seuil 2), non par la place au premier tour : sinon le signal peut partir avant que le programme
# factice ait posé son refus du signal de fin (course de l'essai, vue au rejeu « final », trouvaille (b) de la vérification).
$J $S/s7-artefact-arret-force 150 normal --intervalle-s 1 --seuil-n 2 > "$R/$SUF-s7.txt" 2>&1
echo "auteur v1 s1 à s9 : fait"

# 3. Contre-lecture v1 (E1 h1 avec témoin, E3 h3, E4 h4) et cas sain du groupe (auteur v2)
$SC h1-$SUF 1 0 $CL/prog_factice.py @S@ 0.5 1000 60 1 $CL/enfant_factice.py @M@ -- --seuil-n 5 --seuil-libre-octets 1 $G > "$R/$SUF-h1.txt" 2>&1
$SC h3-$SUF 0 0 $CL/prog_factice.py @S@ 0.001 100000 30 0 $CL/enfant_factice.py @M@ -- --seuil-n 300 --seuil-libre-octets 1 $G > "$R/$SUF-h3.txt" 2>&1
$SC h4-$SUF 0 0 $CL/prog_factice.py @S@ 0.5 1000 60 2 $CL/enfant_sourd.py @M@ -- --seuil-n 5 --seuil-libre-octets 1 $G > "$R/$SUF-h4.txt" 2>&1
$SC c2-sain-$SUF 0 0 $CL/prog_factice.py @S@ 0.5 1000 60 2 $CL/enfant_factice.py @M@ -- --seuil-n 5 --seuil-libre-octets 1 $G > "$R/$SUF-c2-sain.txt" 2>&1
echo "contre-lecture : fait"

# 4. Identité : decoy (contre-lecture), scen-decoy (vérification : -7, ABSENT, 0), fichiers périmés (auteur v2)
bash "$E/decoy-v3.sh" decoy-absent-$SUF ABSENT > "$R/$SUF-decoy-absent.txt" 2>&1
bash "$E/decoy-v3.sh" decoy-decale-$SUF -7 > "$R/$SUF-decoy-decale.txt" 2>&1
bash "$E/decoy-v3.sh" decoy-exact-$SUF 0 > "$R/$SUF-decoy-exact.txt" 2>&1
bash "$E/decoy-perime-v3.sh" decoy-perime-$SUF > "$R/$SUF-decoy-perime.txt" 2>&1
echo "identité : fait"

# 5. Auteur v2 : corrections 5 et 6 (contenu, colonne d'arrêt)
P2=$E/v2-copie/prog-factice-v2.py
$SC c5-sain-$SUF 0 0 $P2 @S@ --max-sources 20 --sans-fin -- --seuil-n 6 $G > "$R/$SUF-c5-sain.txt" 2>&1
$SC c5-artefact-$SUF 0 0 $P2 @S@ --max-sources 20 --sans-fin --contenu-manifeste-3 "ARRET IMMEDIAT n=999 libres=0 projection impossible" -- --seuil-n 6 $G > "$R/$SUF-c5-artefact.txt" 2>&1
$SC c6-sain-$SUF 0 0 $P2 @S@ --max-sources 6 --presque-arret -- --seuil-n 100 $G > "$R/$SUF-c6-sain.txt" 2>&1
$SC c6-artefact-$SUF 0 0 $P2 @S@ --max-sources 6 --arret-a 3 -- --seuil-n 100 $G > "$R/$SUF-c6-artefact.txt" 2>&1
echo "auteur v2 : fait"

# 6. Vérification v2 : sourd-groupe, sourd-hors, docile-hors, chef tué, orphelin, rapide, colonne d'arrêt
$SC sourd-groupe-$SUF 0 0 $VV/prog-v.py @S@ 0.5 1000 60 sourd-groupe @M@ -- --seuil-n 5 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-sourd-groupe.txt" 2>&1
$SC sourd-hors-$SUF 0 0 $VV/prog-v.py @S@ 0.5 1000 60 sourd-hors @M@ -- --seuil-n 5 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-sourd-hors.txt" 2>&1
$SC docile-hors-$SUF 0 0 $VV/prog-v.py @S@ 0.5 1000 60 docile-hors @M@ -- --seuil-n 5 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-docile-hors.txt" 2>&1
$SC chef-tue-$SUF 0 4 $VV/prog-v.py @S@ 0.5 1000 20 simple @M@ -- --seuil-n 1000 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-chef-tue.txt" 2>&1
$SC orphelin-$SUF 0 0 $VV/prog-v.py @S@ 0.5 1000 60 orphelin @M@ -- --seuil-n 8 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-orphelin.txt" 2>&1
$SC rapide-$SUF 0 0 $VV/prog-v.py @S@ 0.001 100000 30 simple @M@ -- --seuil-n 300 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-rapide.txt" 2>&1
"$PY" -I -B "$VV/essai-arret.py" "$B/gardien-essai-court-v3.py" "$E/e/arbre-arret-$SUF" > "$R/$SUF-essai-arret.txt" 2>&1
echo "vérification v2 : fait"

# 7. Erratum 2, correction 1 : chef tué de l'extérieur, descendant vivant
P3=$E/prog-v3.py
$SC e2c1-sain-$SUF 0 3 $P3 @S@ @M@ --pas 0.5 --duree 8 -- --seuil-n 1000 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-e2c1-sain.txt" 2>&1
$SC e2c1-place-$SUF 1 3 $P3 @S@ @M@ --pas 0.5 --duree 60 --gros-apres 5 --gros-octets 300000000 -- --seuil-n 1000 --seuil-libre-octets @LIBRES_MOINS_100M@ --duree-etape-4-s 100000 $G > "$R/$SUF-e2c1-place.txt" 2>&1
$SC e2c1-mesure-$SUF 0 3 $P3 @S@ @M@ --pas 0.5 --duree 60 -- --seuil-n 12 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-e2c1-mesure.txt" 2>&1
$SC e2c1-sourd-$SUF 0 3 $P3 @S@ @M@ --pas 0.5 --duree 60 --sourd -- --seuil-n 12 --seuil-libre-octets 1 --duree-etape-4-s 100000 $G > "$R/$SUF-e2c1-sourd.txt" 2>&1
echo "erratum 2 : fait"
echo "fin $(date -u +%Y-%m-%dT%H:%M:%SZ)"
