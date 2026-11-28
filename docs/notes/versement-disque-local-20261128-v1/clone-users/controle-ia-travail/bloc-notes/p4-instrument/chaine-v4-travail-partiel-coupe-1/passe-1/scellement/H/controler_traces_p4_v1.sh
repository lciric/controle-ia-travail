#!/usr/bin/env bash
# Contrôle des traces de la session de P4-instrument avant tout versement (contrôle positif de l'instrument de P3 ;
# R-262 (1), R-269), v1, script neuf de la chaîne v2 (RC-donnees-06). Les traces que la session verse (lancement :
# lancement.txt, controles.txt, clone-controles.suite.txt, prereg-S.md, offres relues… ; surveillance : etats.txt,
# journal-dernier.txt, progres.txt, arrêt ; contrôle à cinq minutes : journal-5min.txt, etat.txt, arrêt ; sortie de la
# récupération) recopient le journal du conteneur (dont les dernières lignes de run.err, de tests.txt et de tests.err
# que l'amorce imprime) : elles sont contrôlées ici, en entier, avant d'être versées.
#   1. jetons HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN dans l'environnement (8 caractères au moins), sinon code 2 ;
#   2. textes honnêtes de P3 (fichier de la table « Données lues ») présents dans le dépôt de travail, à leur empreinte
#      écrite (ba05fa13…) et à leur sceau exact, hors du dossier contrôlé, sinon code 2 (rien n'est cherché) ;
#   3. fenêtres de chaque texte honnête (toutes les fenêtres de 48 caractères au pas de 16, fenêtres d'un seul caractère
#      répété ignorées), brutes et échappées (JSON, Python), cherchées dans la forme brute et déséchappée de chaque
#      fichier du dossier, dans chaque chaîne JSON décodée et dans chaque chaîne d'un tableau .npz (module commun,
#      `verifications_p4_v1.py fenetres`) ;
#   4. valeurs des jetons de l'environnement dans chaque fichier du dossier (`verifications_p4_v1.py jetons`) ;
#   5. chaîne v3 (VC2-donnees-02) : toute entrée qui n'est pas un fichier ordinaire (lien symbolique, vers un fichier ou
#      un dossier, tube nommé, socket…) n'est ni suivie ni lue : elle est comptée et refuse le versement (code 1, chemin
#      écrit) ; un lien versé par `git add` ne porte que sa cible, mais copié par `cp -L` il porterait un contenu non
#      cherché.
# Seuls des comptes et des chemins s'écrivent : aucun texte, aucune valeur de jeton. Rien n'est écrit dans le dossier
# contrôlé.
# Codes : 0 conformes (aucune fenêtre, aucun jeton, aucune entrée non ordinaire : versement permis) ; 1 fenêtre ou jeton
# retrouvé, fichier illisible ou entrée non ordinaire (rien n'est versé : nœud de Lazar) ; 2 usage, dossier absent, jetons absents, textes absents ou d'une autre
# empreinte, module commun absent (rien n'est cherché).
# Usage : controler_traces_p4_v1.sh DOSSIER_DES_TRACES_DE_LA_SESSION
set -uo pipefail
DEPOT=/home/user/controle-ia-travail
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
VERIF=$H/verifications_p4_v1.py
TEXTES=donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl                        # table « Données lues »
TEXTES_SHA256=ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284           # empreinte écrite (R11)
export PYTHONDONTWRITEBYTECODE=1
[ $# -eq 1 ] && [ -n "$1" ] || { echo "usage : controler_traces_p4_v1.sh DOSSIER_DES_TRACES_DE_LA_SESSION"; exit 2; }
X=$(realpath -m "$1")
[ -d "$X" ] || { echo "dossier $X absent : rien n'est cherché"; exit 2; }
J_HF=${HF_TOKEN:-}; J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}
[ "${#J_HF}" -ge 8 ] && [ "${#J_GH}" -ge 8 ] \
    || { echo "jetons HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN absents ou trop courts : recherche des jetons impossible, rien n'est cherché"; exit 2; }
unset J_HF J_GH
[ -f "$VERIF" ] || { echo "module commun $VERIF absent : rien n'est cherché"; exit 2; }
F="$DEPOT/$TEXTES"
[ -f "$F" ] && [ "$(sha256sum "$F" | cut -d' ' -f1)" = "$TEXTES_SHA256" ] && [ "$(cat "$F.sha256" 2>/dev/null)" = "$TEXTES_SHA256  $(basename "$F")" ] \
    || { echo "textes honnêtes de P3 ($TEXTES) absents, d'une autre empreinte que ${TEXTES_SHA256:0:12}… ou sans leur sceau exact : rien n'est cherché"; exit 2; }
case "$(realpath "$F")" in "$X"/*) echo "les textes de P3 sont dans le dossier contrôlé : rien n'est cherché"; exit 2 ;; esac
W=$(mktemp -d) || exit 2
trap 'rm -rf "$W"' EXIT
echo "traces de la session contrôlées : $X ($(find "$X" -type f | wc -l) fichiers ordinaires ; $(find "$X" -mindepth 1 ! -type f ! -type d | wc -l) entrées non ordinaires)"
"$PY" -B "$VERIF" fenetres "$F" "$X" > "$W/fenetres.txt" 2>&1; cf=$?
sed 's/^/    fenêtres | /' "$W/fenetres.txt"
"$PY" -B "$VERIF" jetons "$X" > "$W/jetons.txt" 2>&1; cj=$?
sed 's/^/    jetons | /' "$W/jetons.txt"
if [ "$cf" = 2 ] || [ "$cj" = 2 ]; then
    echo "TRACES DE LA SESSION : RECHERCHE IMPOSSIBLE (fenêtres : code $cf ; jetons : code $cj) : rien n'est versé"; exit 2
fi
if [ "$cf" = 0 ] && [ "$cj" = 0 ]; then
    echo "TRACES DE LA SESSION : CONFORMES (aucune fenêtre d'un texte honnête, aucun jeton, aucune entrée non ordinaire) : versement permis"; exit 0
fi
# constats comptés une fois chacun (un fichier illisible ou une entrée non ordinaire est écrit par les deux recherches)
n=$(cat "$W/fenetres.txt" "$W/jetons.txt" | grep -E '^(fenêtre\(s\) retrouvée\(s\)|jeton retrouvé|illisible|non ordinaire \(lien symbolique ou autre, ni suivi ni lu\)) : ' | sort -u | wc -l)
echo "TRACES DE LA SESSION : $n CONSTAT(S) (fenêtre, jeton, fichier illisible ou entrée non ordinaire) : RIEN N'EST VERSÉ ; nœud de Lazar"
exit 1
