#!/bin/bash
# Rejoue TOUS les essais sur les pièces v2 dans leur état final (factices seulement), dans des dossiers neufs suffixés SUF ;
# chaque essai écrit sa sortie dans essais/resultats/SUF-<essai>.txt. Aucun vrai programme ; rien hors de ce dossier.
# Usage : rejouer-tout-v2.sh SUF
set -u
SUF=$1
B=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-lanceur-gardien-palier-0b-v2
E=$B/essais
PY=/home/user/controle-ia-travail/.venv/bin/python
R=$E/resultats
SORTIES_EMPLOI=/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1
A=$E/a-$SUF
if [ -e "$A" ]; then echo "refus : $A existe" >&2; exit 1; fi
mkdir -p "$A"
echo "début $(date -u +%Y-%m-%dT%H:%M:%SZ)"
sha256sum $B/lancer-essai-court-v2.sh $B/demarrer-essai-court-v2.sh $B/gardien-essai-court-v2.py $B/demarrer-gardien-essai-court-v2.sh $B/verifier-commande-v2.py > "$R/$SUF-empreintes.txt"
cat "$R/$SUF-empreintes.txt"

# 1. Commande à l'octet (deux extractions) et argv (avec objets faux)
"$PY" -I -B $B/verifier-commande-v2.py $B/complement-1-v3-extraction-v1.md $B/lancer-essai-court-v2.sh $SORTIES_EMPLOI > "$R/$SUF-commande-extraction-v1.txt"; echo "commande (extraction v1) : code $?"
"$PY" -I -B $B/verifier-commande-v2.py $B/complement-1-v3-extraction-v2.md $B/lancer-essai-court-v2.sh $SORTIES_EMPLOI > "$R/$SUF-commande-extraction-v2.txt"; echo "commande (extraction v2) : code $?"
bash $E/cl/cl-argv-v2.sh argv-$SUF > "$R/$SUF-argv.txt" 2>&1; echo "argv : fait"

# 2. Refus du lanceur (auteur v1), projection (auteur v1 et v2)
SORTIE_RACINE=$(bash $E/auteur-v1-copie/preparer-racine-factice-v1.sh "$A/racine-factice" $E/auteur-v1-copie/programme-factice-v1.py)
echo "$SORTIE_RACINE"
TETE=$(git -C "$A/racine-factice" rev-parse HEAD)
EMP=$(sha256sum "$A/racine-factice/prog/programme-factice-v1.py" | cut -d' ' -f1)
bash $E/auteur-v1-copie/essais-lanceur-refus-v1.sh "$A" $B/lancer-essai-court-v2.sh "$TETE" "$EMP" > "$R/$SUF-refus.txt" 2>&1; tail -n 1 "$R/$SUF-refus.txt"
"$PY" -I -B $E/auteur-v1-copie/essai-projection-v1.py $B/gardien-essai-court-v2.py > "$R/$SUF-projection-v1.txt"; tail -n 1 "$R/$SUF-projection-v1.txt"
"$PY" -I -B $E/essai-projection-v2.py $B/gardien-essai-court-v2.py > "$R/$SUF-projection-v2.txt"; tail -n 1 "$R/$SUF-projection-v2.txt"

# 3. Scénarios de l'auteur v1 (s1 à s9), lanceur factice tiré du lanceur v2
cp $E/auteur-v1-copie/fabriquer-lanceur-factice-v1.py "$A/"
bash $E/auteur-v1-copie/preparer-scenarios-v1.sh "$A" $B/lancer-essai-court-v2.sh "$TETE" "$EMP" > "$R/$SUF-preparer.txt" 2>&1; tail -n 1 "$R/$SUF-preparer.txt"
mkdir -p "$A/scenarios/s9-artefact-identite-groupe/tenue"
"$PY" -I -B "$A/fabriquer-lanceur-factice-v1.py" $B/lancer-essai-court-v2.sh "$A/scenarios/s9-artefact-identite-groupe/lanceur-factice.sh" "$A/racine-factice" "$TETE" "$EMP" "$A/racine-factice/prog/programme-factice-v1.py" "$A/scenarios/s9-artefact-identite-groupe/sorties" "$PY -I -B $A/racine-factice/prog/programme-factice-v1.py $A/scenarios/s9-artefact-identite-groupe/sorties --delai-etape-3 1 --pas 0.5 --max-sources 8" > /dev/null
J="bash $E/jouer-scenario-v2.sh"
S=$A/scenarios
$J $S/s1-sain-place $B 60 normal --intervalle-s 1 --seuil-libre-octets 1 > "$R/$SUF-s1.txt" 2>&1
$J $S/s2-artefact-place $B 90 normal --intervalle-s 1 --seuil-libre-octets 1000000000000000000 > "$R/$SUF-s2.txt" 2>&1
$J $S/s3-sain-mesure-n $B 90 normal --intervalle-s 1 > "$R/$SUF-s3.txt" 2>&1
$J $S/s4-artefact-mesure-n $B 90 normal --intervalle-s 1 > "$R/$SUF-s4.txt" 2>&1
$J $S/s5-sain-mesure-duree $B 90 normal --intervalle-s 1 --duree-etape-4-s 30 > "$R/$SUF-s5.txt" 2>&1
$J $S/s6-artefact-mesure-duree $B 90 normal --intervalle-s 1 --duree-etape-4-s 5 > "$R/$SUF-s6.txt" 2>&1
$J $S/s8-artefact-mesure-n1 $B 90 normal --intervalle-s 1 --duree-etape-4-s 3 > "$R/$SUF-s8.txt" 2>&1
$J $S/s9-artefact-identite-groupe $B 60 pgid-faux --intervalle-s 1 --seuil-libre-octets 1000000000000000000 > "$R/$SUF-s9.txt" 2>&1
$J $S/s7-artefact-arret-force $B 150 normal --intervalle-s 1 --seuil-libre-octets 1000000000000000000 > "$R/$SUF-s7.txt" 2>&1
echo "scénarios s1 à s9 : faits"

# 4. Essais de la contre-lecture (E1 h1 avec témoin, E3 h3, E3bis decoy, E4 h4) et cas des corrections
C="bash $E/cl/cl-scenario-v2.sh"
$C h1-$SUF 0.5 1000 60 1 5 1 2700 1 > "$R/$SUF-h1.txt" 2>&1
$C h3-$SUF 0.001 100000 30 0 300 1 2700 0 > "$R/$SUF-h3.txt" 2>&1
$C h4-$SUF 0.5 1000 60 2 5 1 2700 0 $E/contre-lecture-v1-copie/enfant_sourd.py > "$R/$SUF-h4.txt" 2>&1
$C c2-sain-$SUF 0.5 1000 60 2 5 1 2700 0 > "$R/$SUF-c2-sain.txt" 2>&1
bash $E/cl/cl-decoy-v2.sh h2-$SUF > "$R/$SUF-h2-decoy.txt" 2>&1
bash $E/cl/cl-decoy-perime-v2.sh c1-perime-$SUF > "$R/$SUF-c1-perime.txt" 2>&1
K="bash $E/c/c-scenario-v2.sh"
$K c5-sain-$SUF 6 --max-sources 20 --sans-fin > "$R/$SUF-c5-sain.txt" 2>&1
$K c5-artefact-$SUF 6 --max-sources 20 --sans-fin --contenu-manifeste-3 "ARRET IMMEDIAT n=999 libres=0 projection impossible" > "$R/$SUF-c5-artefact.txt" 2>&1
$K c6-sain-$SUF 100 --max-sources 6 --presque-arret > "$R/$SUF-c6-sain.txt" 2>&1
$K c6-artefact-$SUF 100 --max-sources 6 --arret-a 3 > "$R/$SUF-c6-artefact.txt" 2>&1
echo "fin $(date -u +%Y-%m-%dT%H:%M:%SZ)"
