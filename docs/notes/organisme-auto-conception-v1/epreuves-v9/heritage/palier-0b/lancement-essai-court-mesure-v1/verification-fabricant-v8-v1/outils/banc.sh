#!/bin/bash
# Banc de vérification du fabricant v8. Aucune sortie de variable d'environnement.
set -u
R=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1
S8=$R/auteur-fabricant-v8-amorce-epinglee
S7=$R/auteur-fabricant-v7-epingle/fabriquer-donnees-demarrage-v7.sh
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verification-fabricant-v8
T=$W/tables
PY=/home/user/controle-ia-travail/.venv/bin/python
rm -rf "$W/cas" "$W/depot.git"
mkdir -p "$W/cas"
git init -q --bare "$W/depot.git"
TOK32=tokenfactice0123456789abcdefghij
TOK100=$(head -c 100 /dev/zero | tr '\0' 'a')
export TOK32 TOK100

prep() { # $1 nom du cas ; prépare cas/$1 avec copies ; fabricants v8 et v7
  d=$W/cas/$1; mkdir -p "$d/out"
  cp "$S8"/fabriquer-donnees-demarrage-v8.sh "$S8"/amorce-demarrage-essai-3-v6.sh "$S8"/demarrage-machine-essai-3-v6.sh "$S8"/reduire-script-v6.py "$d/"
  cp "$S7" "$d/"
}
run() { # $1 cas ; $2 fabricant (nom de fichier) ; $3 var nom ; $4 sortie nom ; reste : env en plus
  d=$W/cas/$1; f=$2; nom=$3; so=$4
  env FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/$f" "$nom" "$d/out/$so" > "$T/$1-$so.stdout" 2> "$T/$1-$so.stderr"
  echo "$1/$so code=$?" | tee -a "$T/codes.txt"
  ls "$d/out" | grep "^$so" | tr '\n' ' ' > "$T/$1-$so.fichiers"
}
: > "$T/codes.txt"

# Cas 1 : sain, v7 puis v8, même jeton factice (TOK32), même seconde si possible
prep sain
d=$W/cas/sain
for v in v7 v8; do :; done
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v7.sh" TOKEN_FAC "$d/out/d7" > "$T/sain-d7.stdout" 2> "$T/sain-d7.stderr"; echo "sain/d7 code=$?" | tee -a "$T/codes.txt"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/d8" > "$T/sain-d8.stdout" 2> "$T/sain-d8.stderr"; echo "sain/d8 code=$?" | tee -a "$T/codes.txt"
cmp "$d/out/d7" "$d/out/d8" > "$T/sain-cmp-brut.txt" 2>&1; echo "cmp brut rc=$?" | tee -a "$T/codes.txt"
sed 2d "$d/out/d7" | sha256sum > "$T/sain-d7-sans-l2.sha"
sed 2d "$d/out/d8" | sha256sum > "$T/sain-d8-sans-l2.sha"
cmp "$T/sain-d7-sans-l2.sha" "$T/sain-d8-sans-l2.sha"; echo "cmp sans ligne 2 rc=$?" | tee -a "$T/codes.txt"
sed -n 2p "$d/out/d7" > "$T/sain-l2-v7.txt"; sed -n 2p "$d/out/d8" > "$T/sain-l2-v8.txt"
grep -c -F 'E_SCRIPT=' "$d/out/d8" > "$T/sain-compte-escript.txt"
sed -n 4p "$d/out/d8" >> "$T/sain-compte-escript.txt"
# jeton 100 signes : marge
env TOKEN_FAC="$TOK100" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/d8-100" > "$T/sain-d8-100.stdout" 2> "$T/sain-d8-100.stderr"; echo "sain/d8-100 code=$?" | tee -a "$T/codes.txt"
grep -E 'lecture stricte|information' "$T/sain-d8-100.stdout" > "$T/sain-marges.txt"

# Cas 2 : amorce modifiée d'un octet (un caractère d'un commentaire)
prep amorce1
d=$W/cas/amorce1
sed -i '3s/Amorce/Amorcf/' "$d/amorce-demarrage-essai-3-v6.sh"
cmp -l "$S8/amorce-demarrage-essai-3-v6.sh" "$d/amorce-demarrage-essai-3-v6.sh" > "$T/amorce1-octets-diff.txt"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/x" > "$T/amorce1.stdout" 2> "$T/amorce1.stderr"; echo "amorce1 code=$?" | tee -a "$T/codes.txt"
ls "$d/out" > "$T/amorce1-fichiers.txt"

# Cas 3 : amorce privée de son contrôle d'empreinte (ligne du hachage retirée)
prep amorce-sans-controle
d=$W/cas/amorce-sans-controle
grep -v 'sha256sum | cut -c1-64)" = "\$E_SCRIPT"' "$S8/amorce-demarrage-essai-3-v6.sh" > "$d/amorce-demarrage-essai-3-v6.sh"
diff "$S8/amorce-demarrage-essai-3-v6.sh" "$d/amorce-demarrage-essai-3-v6.sh" > "$T/amorce-sans-controle-diff.txt"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/x" > "$T/amorce-sans-controle.stdout" 2> "$T/amorce-sans-controle.stderr"; echo "amorce-sans-controle code=$?" | tee -a "$T/codes.txt"
ls "$d/out" > "$T/amorce-sans-controle-fichiers.txt"

# Cas 4 : v8 amputé du contrôle d'épinglage de l'amorce (lignes 70-72), amorce intacte : doit passer (témoin)
prep sans-epingle-sain
d=$W/cas/sans-epingle-sain
sed -i '70,72d' "$d/fabriquer-donnees-demarrage-v8.sh"
diff "$S8/fabriquer-donnees-demarrage-v8.sh" "$d/fabriquer-donnees-demarrage-v8.sh" > "$T/sans-epingle-diff.txt"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/x" > "$T/sans-epingle-sain.stdout" 2> "$T/sans-epingle-sain.stderr"; echo "sans-epingle-sain code=$?" | tee -a "$T/codes.txt"

# Cas 5 : épinglage retiré + amorce portant une 2e ligne E_SCRIPT= (ligne 8 ajoutée) : le contrôle de comptage seul doit refuser 9, sans fichier
prep deux-lignes
d=$W/cas/deux-lignes
cp "$d/fabriquer-donnees-demarrage-v8.sh" "$d/fab-sans-epingle.sh"
sed -i '70,72d' "$d/fab-sans-epingle.sh"
sed -i '8a E_SCRIPT=0000000000000000000000000000000000000000000000000000000000000000' "$d/amorce-demarrage-essai-3-v6.sh"
diff "$S8/amorce-demarrage-essai-3-v6.sh" "$d/amorce-demarrage-essai-3-v6.sh" > "$T/deux-lignes-diff.txt"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fab-sans-epingle.sh" TOKEN_FAC "$d/out/x" > "$T/deux-lignes.stdout" 2> "$T/deux-lignes.stderr"; echo "deux-lignes(sans epingle) code=$?" | tee -a "$T/codes.txt"
ls "$d/out" > "$T/deux-lignes-fichiers.txt"
# 5b : même amorce, v8 intact : refus 9 par l'épinglage
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/y" > "$T/deux-lignes-v8.stdout" 2> "$T/deux-lignes-v8.stderr"; echo "deux-lignes(v8) code=$?" | tee -a "$T/codes.txt"
# 5c : variante E_SCRIPT+= (non vue par le comptage), épinglage retiré
prep plus-egal
d=$W/cas/plus-egal
cp "$d/fabriquer-donnees-demarrage-v8.sh" "$d/fab-sans-epingle.sh"
sed -i '70,72d' "$d/fab-sans-epingle.sh"
sed -i '8a E_SCRIPT+=x' "$d/amorce-demarrage-essai-3-v6.sh"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fab-sans-epingle.sh" TOKEN_FAC "$d/out/x" > "$T/plus-egal.stdout" 2> "$T/plus-egal.stderr"; echo "plus-egal(sans epingle) code=$?" | tee -a "$T/codes.txt"

# Cas 6 : contournements. Variables AMORCE / E_AMORCE_EPINGLE / E_AMORCE posées dans l'environnement ; nom de variable-jeton = E_AMORCE ; amorce alternative
prep contourne
d=$W/cas/contourne
sed 's/Amorce/Amorcf/' "$S8/amorce-demarrage-essai-3-v6.sh" > "$d/amorce-alt.sh"
env AMORCE="$d/amorce-alt.sh" E_AMORCE_EPINGLE=x E_AMORCE=y FABRICANT_AMORCE="$d/amorce-alt.sh" TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/x" > "$T/contourne-env.stdout" 2> "$T/contourne-env.stderr"; echo "contourne-env code=$?" | tee -a "$T/codes.txt"
env E_AMORCE="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" E_AMORCE "$d/out/z" > "$T/contourne-nomvar.stdout" 2> "$T/contourne-nomvar.stderr"; echo "contourne-nomvar(E_AMORCE) code=$?" | tee -a "$T/codes.txt"
sha256sum "$d/out/z" > "$T/contourne-nomvar.sha"
# amorce remplacée par un lien symbolique vers l'alternative dans une copie
prep lien
d=$W/cas/lien
rm "$d/amorce-demarrage-essai-3-v6.sh"; sed 's/Amorce/Amorcf/' "$S8/amorce-demarrage-essai-3-v6.sh" > "$d/alt.sh"; ln -s "$d/alt.sh" "$d/amorce-demarrage-essai-3-v6.sh"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/x" > "$T/lien.stdout" 2> "$T/lien.stderr"; echo "lien code=$?" | tee -a "$T/codes.txt"

# Cas 7 : relecture après contrôle (mutation : le fabricant modifie l'amorce juste après le contrôle, ligne 72)
prep relecture
d=$W/cas/relecture
sed -i "72a echo '# ajout apres controle' >> \"\$AMORCE\"" "$d/fabriquer-donnees-demarrage-v8.sh"
diff "$S8/fabriquer-donnees-demarrage-v8.sh" "$d/fabriquer-donnees-demarrage-v8.sh" > "$T/relecture-diff.txt"
env TOKEN_FAC="$TOK32" FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot.git" bash "$d/fabriquer-donnees-demarrage-v8.sh" TOKEN_FAC "$d/out/x" > "$T/relecture.stdout" 2> "$T/relecture.stderr"; echo "relecture code=$?" | tee -a "$T/codes.txt"
ls "$d/out" > "$T/relecture-fichiers.txt"
grep -c 'ajout apres controle' "$d/out/x" > "$T/relecture-dans-donnees.txt"

# Cas 8 : script de démarrage modifié (témoin de non-régression : refus par E_COMPLET épinglé)
echo FIN
