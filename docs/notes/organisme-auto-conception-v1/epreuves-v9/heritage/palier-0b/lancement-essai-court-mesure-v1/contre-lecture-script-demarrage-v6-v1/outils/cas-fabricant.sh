#!/bin/bash
# Cas du fabricant v6 sur factices. Usage : cas-fabricant.sh RACINE_BANC   (RACINE_BANC neuve, hors depot git)
set -u
RB=$1
V6=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v6
FAB=$V6/fabriquer-donnees-demarrage-v6.sh
REEL=$V6/demarrage-machine-essai-3-v6.sh
mkdir -m 700 $RB || exit 2
git init -q --bare $RB/distant.git
# jeton factice de 100 signes, fabrique ici
export TOKV=$(printf 'Zq9_-%.0s' $(seq 1 20))
[ ${#TOKV} = 100 ] || { echo "jeton factice mal forme"; exit 2; }
echo $TOKV > $RB/jeton-contre-lecteur.txt

# reducteurs artefacts
cat > $RB/r-naif.sh <<'EOF'
#!/bin/bash
sed -e '1!{/^[[:space:]]*#/d;/^[[:space:]]*$/d}' "$1" > "$2"
EOF
cat > $RB/r-code.sh <<'EOF'
#!/bin/bash
sed -e '1!{/^[[:space:]]*#/d;/^[[:space:]]*$/d}' -e '/^PAS=0$/d' "$1" > "$2"
EOF
cat > $RB/r-fin.sh <<'EOF'
#!/bin/bash
sed -e '1!{/^[[:space:]]*#/d;/^[[:space:]]*$/d}' -e 's/ # commentaire de fin$//' "$1" > "$2"
EOF
cat > $RB/r-shebang.sh <<'EOF'
#!/bin/bash
sed -e '/^[[:space:]]*#/d;/^[[:space:]]*$/d' "$1" > "$2"
EOF
cat > $RB/r-rien.sh <<'EOF'
#!/bin/bash
cp "$1" "$2"
EOF
cat > $RB/r-espaces-fin.sh <<'EOF'
#!/bin/bash
sed -e '1!{/^[[:space:]]*#/d;/^[[:space:]]*$/d}' -e 's/[[:space:]]*$//' "$1" > "$2"
EOF

# scripts d'entree : le reel + une queue
mk() {  # $1 nom ; queue sur l'entree standard
  cp $REEL $RB/$1.sh; cat >> $RB/$1.sh
}
mk e-sain <<'EOF'
# commentaire de queue

: sain
EOF
mk e-chaine <<'EOF'
MSG='un
# ligne de chaine

fin'
EOF
mk e-heredoc <<'EOF'
cat <<'FIN' > /dev/null
# dans le document

fin
FIN
EOF
mk e-fin <<'EOF'
Z=1 # commentaire de fin
EOF
mk e-continuation <<'EOF'
echo a \
# c
echo b
EOF
mk e-erreur-syntaxe <<'EOF'
if true; then
EOF

n=0
cas() {  # $1 nom ; $2 attendu ; $3 script ; $4 reducteur ou - ; reste : arguments additionnels
  local nom=$1 att=$2 scr=$3 red=$4 d rc
  d=$RB/$nom; mkdir -m 700 $d
  if [ "$red" = - ]; then
    FABRICANT_BANC=oui FABRICANT_SCRIPT=$scr FABRICANT_DEPOT_DISTANT=$RB/distant.git /bin/bash $FAB TOKV $d/sortie > $d/stdout 2> $d/stderr
  else
    FABRICANT_BANC=oui FABRICANT_SCRIPT=$scr FABRICANT_REDUCTEUR=$RB/$red FABRICANT_DEPOT_DISTANT=$RB/distant.git /bin/bash $FAB TOKV $d/sortie > $d/stdout 2> $d/stderr
  fi
  rc=$?
  printf '%-34s attendu=%-3s rendu=%-3s  %s\n' $nom $att $rc "$(tail -n 1 $d/stderr | cut -c1-110)"
}
echo "--- refus attendus (artefacts) ---"
cas A1-code-retiree 9 $RB/e-sain.sh r-code.sh
cas A2-ligne-de-chaine-retiree 9 $RB/e-chaine.sh r-naif.sh
cas A3-ligne-de-document-retiree 9 $RB/e-heredoc.sh r-naif.sh
cas A4-commentaire-de-fin-touche 9 $RB/e-fin.sh r-fin.sh
cas A5-ligne-shebang-retiree 9 $RB/e-sain.sh r-shebang.sh
cas A6-continuation-commentaire-retiree 9 $RB/e-continuation.sh r-naif.sh
cas A7-espaces-de-fin-retires 9 $RB/e-fin.sh r-espaces-fin.sh
cas A8-syntaxe-fausse-script-complet 9 $RB/e-erreur-syntaxe.sh -
echo "--- sains attendus (reducteur reel) ---"
cas S1-queue-saine 0 $RB/e-sain.sh -
cas S2-chaine-reel 0 $RB/e-chaine.sh -
cas S3-heredoc-reel 0 $RB/e-heredoc.sh -
cas S4-fin-reel 0 $RB/e-fin.sh -
cas S5-continuation-reel 0 $RB/e-continuation.sh -
cas S6-aucun-retrait 0 $RB/e-sain.sh r-rien.sh
echo "--- temoin T2 : reducteur naif, entree avec chaine multiligne : accepte ? (0 = l'epreuve ne voit pas) ---"
cas T2-naif-chaine 0? $RB/e-chaine.sh r-naif.sh
cas T2-naif-heredoc 0? $RB/e-heredoc.sh r-naif.sh
cas T2-naif-continuation 0? $RB/e-continuation.sh r-naif.sh
