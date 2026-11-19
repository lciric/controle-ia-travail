#!/bin/bash
# § 1.1 — dépôt à histoire complète, branches présentes, têtes (rejouable : relevé numéroté)
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 1.1 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-1-depot-et-tetes.sh
. "$(dirname "$0")/commun.sh"
K="$(numero_neuf_du_releve_des_tetes)"; R="$T/releve-mise-en-place-$K.txt"; neuf "$R"
neuf "$T/tetes-du-distant-$K.txt"; neuf "$T/noms-distants-$K.txt"; neuf "$T/noms-locaux-$K.txt"
{
cd "$DEPOT" || exit 1
dire "== 1.1 dépôt, $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git fetch origin donnees/t07-etape-b-bis-v2 calcul/t06-confirmation-7b-v1 verdict/t06-mots-et-cout-compte-3-v1 >/dev/null 2>&1; dire "récupération des trois branches : code $?"
egal "dépôt non superficiel" false "$(git rev-parse --is-shallow-repository)"
egal "tête de la branche de travail" "$TETE_TRAVAIL" "$(git rev-parse HEAD)"
egal "branche courante" claude/lecture-verdict-etape-b-bis-v1 "$(git rev-parse --abbrev-ref HEAD)"
egal "arbre principal propre (nombre de lignes de statut)" 0 "$(git status --porcelain --untracked-files=all | wc -l | tr -d ' ')"
vrai "le commit de la course est un ancêtre de la tête" git merge-base --is-ancestor "$COURSE" HEAD
vrai "le commit de main qui porte les inscriptions est un ancêtre de la tête" git merge-base --is-ancestor "$MAIN_INSCRIPTIONS" HEAD
egal "tête de la branche des sorties de la course" "$TETE_SORTIES" "$(git rev-parse --verify -q "$REF_SORTIES")"
egal "tête de la branche de la course de confirmation" "$TETE_7B" "$(git rev-parse --verify -q "$REF_7B")"
vrai "branche de la pièce « mots et coût » présente" git rev-parse --verify -q "$REF_MC^{commit}"
dire "tête de la branche de la pièce « mots et coût » : $(git rev-parse --verify -q "$REF_MC")"
if git ls-remote --heads origin > "$T/tetes-du-distant-$K.txt" 2>/dev/null; then
  egal "tête des sorties sur le distant" "$TETE_SORTIES" "$(awk '$2=="refs/heads/donnees/t07-etape-b-bis-v2"{print $1}' "$T/tetes-du-distant-$K.txt")"
  awk '{print $1" "$2}' "$T/tetes-du-distant-$K.txt" | sed 's# refs/heads/# refs/remotes/origin/#' | sort > "$T/noms-distants-$K.txt"
  git for-each-ref --format='%(objectname) %(refname)' refs/remotes/origin | grep -v ' refs/remotes/origin/HEAD$' | sort > "$T/noms-locaux-$K.txt"
  egal "branches du distant absentes localement ou à une autre tête" 0 "$(comm -23 "$T/noms-distants-$K.txt" "$T/noms-locaux-$K.txt" | wc -l | tr -d ' ')"
else
  dire "DEFAUT : têtes du distant illisibles (git ls-remote) : présence de toutes les branches non prouvée"; FAUTES=$((FAUTES+1))
fi
dire "place libre : $(df -h "$T" | tail -1 | awk '{print $4}')"
conclure
} 2>&1 | tee "$R"
