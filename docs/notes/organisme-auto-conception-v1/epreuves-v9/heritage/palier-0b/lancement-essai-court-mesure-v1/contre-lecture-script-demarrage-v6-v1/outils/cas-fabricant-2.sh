#!/bin/bash
# Complements : A7 (espaces de fin retires, sur une entree qui en porte) ; K1 (reducteur REEL, construction case dans $() au milieu
# d'une chaine : la ligne de chaine est retiree, le fabricant accepte). Usage : cas-fabricant-2.sh RB(neuf)
set -u
RB=$1
V6=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v6
FAB=$V6/fabriquer-donnees-demarrage-v6.sh
REEL=$V6/demarrage-machine-essai-3-v6.sh
mkdir -m 700 $RB || exit 2
git init -q --bare $RB/distant.git
export TOKV=$(printf 'Zq9_-%.0s' $(seq 1 20))
cat > $RB/r-espaces-fin.sh <<'EOF'
#!/bin/bash
sed -e '1!{/^[[:space:]]*#/d;/^[[:space:]]*$/d}' -e 's/[[:space:]]*$//' "$1" > "$2"
EOF
cp $REEL $RB/e-esp.sh; printf 'Z=1   \n' >> $RB/e-esp.sh
cp $REEL $RB/e-k1.sh
cat >> $RB/e-k1.sh <<'EOF'
Y=a
X="$(case $Y in
a) echo "q
# pas un commentaire
r";; esac)"
EOF
bash -n $RB/e-k1.sh && echo "e-k1 : bash -n passe sur l'entree"
run() { mkdir -m 700 $RB/$1; local x=(); [ -z "${3:-}" ] || x=(FABRICANT_REDUCTEUR=$3)
  env FABRICANT_BANC=oui FABRICANT_SCRIPT=$2 "${x[@]}" FABRICANT_DEPOT_DISTANT=$RB/distant.git /bin/bash $FAB TOKV $RB/$1/sortie > $RB/$1/stdout 2> $RB/$1/stderr; echo "$1 : code $? $(tail -n 1 $RB/$1/stderr | cut -c1-100)"; }
run A7-espaces-de-fin $RB/e-esp.sh $RB/r-espaces-fin.sh
run K1-reel-case-chaine $RB/e-k1.sh
echo "--- K1 : diff entree / texte reduit (lignes retirees) ---"
diff $RB/e-k1.sh $RB/K1-reel-case-chaine/sortie.script-reduit.sh | tail -n 4
echo "--- K1 : sens du bloc ajoute, entree puis reduit (valeur de X) ---"
sed -n '/^Y=a$/,$p' $RB/e-k1.sh > $RB/bloc-orig.sh
sed -n '/^Y=a$/,$p' $RB/K1-reel-case-chaine/sortie.script-reduit.sh > $RB/bloc-reduit.sh
printf '%s\n' "printf '%s' \"\$X\" | tr '\\n' '|'" >> $RB/bloc-orig.sh
printf '%s\n' "printf '%s' \"\$X\" | tr '\\n' '|'" >> $RB/bloc-reduit.sh
echo "orig  : $(/bin/bash $RB/bloc-orig.sh)"
echo "reduit: $(/bin/bash $RB/bloc-reduit.sh)"
