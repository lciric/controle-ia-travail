#!/usr/bin/env bash
# Essai du contrôle à blanc du compte 2 (v1) : cas sains et artefacts (règle R5), sur des COPIES des deux registres de
# main lus par la garde, un lien vers le texte scellé de T0.7 (haché par la garde, jamais ouvert), les deux compagnons de
# T0.7 récupérés par la suite exacte de la commande (dépôt jetable sans contenu de fichier, deux blobs nommés), des listes
# « qui a lu quoi » factices. N'écrit que dans le bac donné ; n'ouvre aucun paquet ; ne touche pas la branche de calcul de
# P3-bis ; aucun registre réel n'est modifié (contrôlé avant et après par empreinte).
# Usage : essai_controle_a_blanc_compte_2_v1.sh DEPOT BAC_NEUF [PYTHON]
set -uo pipefail
[ $# -ge 2 ] || { echo "usage : essai_controle_a_blanc_compte_2_v1.sh DEPOT BAC_NEUF [PYTHON]"; exit 2; }
DEPOT=$(realpath "$1"); BAC=$(realpath -m "$2"); PY=${3:-python3}
[ -e "$BAC" ] && { echo "$BAC existe déjà (R12)"; exit 2; }
mkdir -p "$BAC" || exit 2
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1
S=8f8df8b2726a69568b4d4a54bae16188e7f1b3d0
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
ICI=$(dirname "$(realpath "$0")")
SCRIPT="$ICI/controle_a_blanc_compte_2_v1.py"
SESSION_ESSAI=session_01TESTCOMPTE2ZZZZZZZZZZ
date -u +"début : %Y-%m-%dT%H:%M:%SZ"
echo "script : $(sha256sum "$SCRIPT" | cut -d' ' -f1)"
avant=$(sha256sum "$DEPOT/registres/prealables-p3bis-v1.md" "$DEPOT/registres/scellements-v1.md" | cut -d' ' -f1 | tr '\n' ' ')
conformes=0; total=0

# --- A. compagnons de T0.7 : suite exacte de la commande (section 5), cible = racine d'essai -------------------------
SAIN="$BAC/racine-sain"; mkdir -p "$SAIN/registres" "$SAIN/prereg"
CT="$BAC/compagnons-t07-v1"
git init -q "$CT"
git -C "$CT" remote add origin "$DEPOT_URL"
git -C "$CT" config remote.origin.promisor true
git -C "$CT" config remote.origin.partialclonefilter blob:none
git -C "$CT" fetch --no-tags --filter=blob:none -q origin \
    +refs/heads/donnees/t07-etape-a-v1:refs/remotes/origin/donnees/t07-etape-a-v1
echo "tête de donnees/t07-etape-a-v1 : $(git -C "$CT" rev-parse refs/remotes/origin/donnees/t07-etape-a-v1)"
poser() {   # chemin blob empreinte racine
    local b; b=$(git -C "$CT" rev-parse "refs/remotes/origin/donnees/t07-etape-a-v1:$1") || return 1
    [ "$b" = "$2" ] || { echo "ARRÊT : $1 : blob $b, $2 attendu"; return 1; }
    [ ! -e "$4/$1" ] || { echo "ARRÊT : $4/$1 existe déjà"; return 1; }
    mkdir -p "$(dirname "$4/$1")" && git -C "$CT" cat-file blob "$2" > "$4/$1" || return 1
    [ "$(sha256sum < "$4/$1" | cut -d' ' -f1)" = "$3" ] || { echo "ARRÊT : $1 d'empreinte autre"; return 1; }
    echo "compagnon posé : $1 (blob ${2:0:8}, empreinte ${3:0:12}…)"
}
total=$((total+1))
if poser donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz.sha256 \
        34181fd147918f0d47e21848b939f9e47c8b8507 5f5672fca88231d25bfff139a0c5e490f5338dba64c10254ce95e673a38fd22f "$SAIN" \
   && poser diag/20261114-001352-t07-lecture-reel/sondes-t07.json.sha256 \
        60d8dfb09e0c797d807c515d38077b734f5a1f42 77af718b91e5d05479a283cf47db4ed04d178604e2ff9218d7badf14f2bd60bf "$SAIN"; then
    echo "OK  A : deux compagnons récupérés par le dépôt jetable, blobs et empreintes conformes"; conformes=$((conformes+1))
else echo "KO  A : récupération des compagnons"; fi
echo "objets du dépôt jetable : $(git -C "$CT" count-objects -v | awk '/^size-pack/{print $2}') Kio de paquets ; fichiers extraits hors .git : $(find "$CT" -path "$CT/.git" -prune -o -type f -print | wc -l)"

# --- B. module de S tiré par git show --------------------------------------------------------------------------------
M="$BAC/module-s-v1"; mkdir -p "$M/controle_ia/premier_test_ia"
for f in __init__.py gardes.py scellement.py premier_test_ia/__init__.py premier_test_ia/ouverture_p3bis_v3.py; do
    git -C "$DEPOT" show "$S:src/controle_ia/$f" > "$M/controle_ia/$f"; done
echo "module de S : $(sha256sum "$M/controle_ia/premier_test_ia/ouverture_p3bis_v3.py" | cut -d' ' -f1)"
M2="$BAC/module-altere-v1"; cp -r "$M" "$M2"; printf '# altéré\n' >> "$M2/controle_ia/premier_test_ia/ouverture_p3bis_v3.py"

# --- C. racine saine et listes factices ------------------------------------------------------------------------------
cp "$DEPOT/registres/prealables-p3bis-v1.md" "$DEPOT/registres/scellements-v1.md" "$SAIN/registres/"
ln -s "$DEPOT/prereg/T0.7-sondes-v0-v1.md" "$SAIN/prereg/T0.7-sondes-v0-v1.md"
ln -s "$DEPOT/prereg/T0.7-sondes-v0-v1.md.sha256" "$SAIN/prereg/T0.7-sondes-v0-v1.md.sha256"
L="$BAC/listes"; mkdir -p "$L"
liste() {   # nom, lignes du tableau (après l'en-tête) ; scelle sauf si $3 = nonscellee
    { echo "# Liste « qui a lu quoi » (essai) — v1"; echo
      [ "${4:-}" = sansentete ] && echo "| session | modèle | a lu |" || echo "| session | compte | modèle | a lu |"
      [ "${4:-}" = sansentete ] && echo "|---|---|---|" || echo "|---|---|---|---|"
      printf '%s\n' "$2"; } > "$L/$1.md"
    [ "${3:-}" = nonscellee ] || PYTHONPATH="$M" "$PY" -B -m controle_ia.scellement sceller "$L/$1.md" > /dev/null
}
BASE='| session_01AAAAAAAAAAAAAAAAAAAAAA | mère | modèle A | procédure de P3-bis |
| session_01BBBBBBBBBBBBBBBBBBBBBB | compte 4 | modèle B | T0.7 scellé |'
liste saine "$BASE"
liste compte12 "$BASE
| session_01CCCCCCCCCCCCCCCCCCCCCC | compte 12 | modèle A | T0.7 scellé |"
liste avecsession "$BASE
| $SESSION_ESSAI | compte 3 | modèle B | T0.7 scellé |"
liste compte2 "$BASE
| session_01DDDDDDDDDDDDDDDDDDDDDD | Compte 2 | modèle B | sorties de 7a |"
liste comptetiret "$BASE
| session_01DDDDDDDDDDDDDDDDDDDDDD | compte-2 | modèle B | sorties de 7b |"
liste comptechiffre "$BASE
| session_01DDDDDDDDDDDDDDDDDDDDDD | 2 | modèle B | procédure de P3-bis |"
liste horstableau "$BASE

Note : $SESSION_ESSAI n'a rien lu."
liste sansentete '| session_01AAAAAAAAAAAAAAAAAAAAAA | modèle A | procédure de P3-bis |' "" sansentete
liste nonscellee "$BASE" nonscellee
sha() { sha256sum "$1" | cut -d' ' -f1; }

cas() {   # libellé, code attendu, motif attendu, module, racine, liste, puis options
    local lib=$1 code=$2 motif=$3 mod=$4 rac=$5 lst=$6; shift 6
    local emp; emp=$( [ -e "$lst.sha256" ] && cut -d' ' -f1 "$lst.sha256" || sha "$lst")
    local sortie; sortie=$(PYTHONPATH="$mod" "$PY" -B "$SCRIPT" --racine "$rac" --liste "$lst" --empreinte-liste "$emp" \
        --session "$SESSION_ESSAI" "$@" 2>&1); local obtenu=$?
    total=$((total+1))
    if [ "$obtenu" = "$code" ] && printf '%s\n' "$sortie" | grep -q -- "$motif"; then
        conformes=$((conformes+1)); echo "OK  $lib : code $obtenu ; « $(printf '%s\n' "$sortie" | grep -m1 -- "$motif" | sed -E 's/^(.{0,150}).*/\1/') »"
    else echo "KO  $lib : code $obtenu (attendu $code, motif « $motif ») ; sortie :"; printf '%s\n' "$sortie" | sed 's/^/      /'; fi
}
variante() {   # nom : copie de la racine saine (liens recopiés tels quels)
    cp -a "$SAIN" "$BAC/racine-$1"; echo "$BAC/racine-$1"; }

# --- D. cas --------------------------------------------------------------------------------------------------------
cas "1 sain" 0 "TOUT CONFORME" "$M" "$SAIN" "$L/saine.md"
cas "1b sain, sortie entière : appui" 0 "AUTORISÉ pleine (chemin normal) .* appui SCORES-T07=13ac4480035f1ef6d4ea8ac81ffa962c1324e4e9e90a78c1d4f569f2abd0509d SONDES-T07=aa6892320f130e96af45e4e70b542b7ccfcea3ccd23d2fdc3e722b5637affa95" "$M" "$SAIN" "$L/saine.md"
cas "2 sain, « compte 12 » n'est pas le compte 2" 0 "TOUT CONFORME" "$M" "$SAIN" "$L/compte12.md"
cas "3 registres réels de main (sans compagnons de T0.7)" 2 "compagnon .* absent de la racine" "$M" "$DEPOT" "$L/saine.md"
R=$(variante sanscompagnons); rm "$R/donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz.sha256"
cas "4 compagnon de SCORES-T07 absent" 2 "compagnon-absent" "$M" "$R" "$L/saine.md"
R=$(variante compagnonaltere); printf ' ' >> "$R/diag/20261114-001352-t07-lecture-reel/sondes-t07.json.sha256"
cas "5 compagnon de SONDES-T07 altéré" 2 "d'empreinte .* attendue" "$M" "$R" "$L/saine.md"
R=$(variante journal); printf '| clé | date | mode | appui | paquets | motif |\n|---|---|---|---|---|---|\n' > "$R/registres/ouvertures-p3bis-v1.md"
cas "6 journal présent (en-tête seul)" 2 "ouvertures-p3bis-v1.md présent" "$M" "$R" "$L/saine.md"
R=$(variante journalvide); : > "$R/registres/ouvertures-p3bis-v1.md"
cas "7 journal présent (vide)" 2 "ouvertures-p3bis-v1.md présent" "$M" "$R" "$L/saine.md"
R=$(variante verdict); printf '| VERDICT-P3BIS | 2026-11-14T09:00:00Z | docs/verdicts/verdict-P3-bis-v1-issue.json | %064d |\n' 0 >> "$R/registres/scellements-v1.md"
cas "8 ligne VERDICT-P3BIS déjà inscrite" 2 "VERDICT-P3BIS est déjà inscrite" "$M" "$R" "$L/saine.md"
R=$(variante sansecrit); grep -v '^| ECRIT-LANCEMENT-RELANCE-P3BIS |' "$SAIN/registres/prealables-p3bis-v1.md" > "$R/registres/prealables-p3bis-v1.md"
cas "9 ligne d'écrit absente" 2 "REFUS ligne-absente" "$M" "$R" "$L/saine.md"
R=$(variante sanst07); rm "$R/prereg/T0.7-sondes-v0-v1.md"
cas "10 texte scellé de T0.7 absent de la racine" 2 "REFUS sceau-faux" "$M" "$R" "$L/saine.md"
cas "11 horloge à la date des lignes de T0.7" 2 "REFUS ni-scores-ni-ouvrir .*\[date-posterieure\] ligne SCORES-T07" "$M" "$SAIN" "$L/saine.md" --instant 2026-11-14T01:55:05Z
cas "12 module altéré" 2 "ARRÊT : module importé" "$M2" "$SAIN" "$L/saine.md"
cas "13 session dans la liste" 2 "la session $SESSION_ESSAI figure à la ligne" "$M" "$SAIN" "$L/avecsession.md"
cas "14 « Compte 2 » dans la liste" 2 "le compte 2 figure" "$M" "$SAIN" "$L/compte2.md"
cas "15 « compte-2 » dans la liste" 2 "le compte 2 figure" "$M" "$SAIN" "$L/comptetiret.md"
cas "16 « 2 » seul dans la colonne compte" 2 "le compte 2 figure" "$M" "$SAIN" "$L/comptechiffre.md"
cas "17 session citée hors du tableau" 2 "citée hors du tableau" "$M" "$SAIN" "$L/horstableau.md"
cas "18 liste sans colonne « compte »" 2 "ligne de tableau avant tout en-tête" "$M" "$SAIN" "$L/sansentete.md"
cas "19 liste non scellée" 2 "liste non scellée ou altérée" "$M" "$SAIN" "$L/nonscellee.md"
total=$((total+1)); sortie=$(PYTHONPATH="$M" "$PY" -B "$SCRIPT" --racine "$SAIN" --liste "$L/saine.md" \
    --empreinte-liste "$(printf '%064d' 0)" --session "$SESSION_ESSAI" 2>&1); c=$?
if [ "$c" = 2 ] && printf '%s\n' "$sortie" | grep -q "attendue"; then conformes=$((conformes+1)); echo "OK  20 empreinte de liste autre : code 2"; else echo "KO  20 : code $c ; $sortie"; fi
total=$((total+1)); PYTHONPATH="$M" "$PY" -B "$SCRIPT" --racine "$SAIN" --liste "$L/saine.md" \
    --empreinte-liste "$(sha "$L/saine.md")" --session "" > /dev/null 2>&1; c=$?
if [ "$c" = 1 ]; then conformes=$((conformes+1)); echo "OK  21 session vide : erreur d'appel, code 1"; else echo "KO  21 : code $c"; fi
R=$(variante autrescores); sed -i 's#^| SCORES-T07 | \([^|]*\) | donnees/20261114-001352-t07-lecture-reel/scores-actions-t07.npz |#| SCORES-T07 | \1 | donnees/autre-run/scores-actions-t07.npz |#' "$R/registres/scellements-v1.md"
cas "22 ligne SCORES-T07 citant un autre fichier" 2 "hors des deux fichiers attendus" "$M" "$R" "$L/saine.md"
# 23 : après le rendez-vous, décision « maintenir » inscrite : la voie normale reste permise (rendez-vous sans objet)
R=$(variante maintenir); mkdir -p "$R/docs/decisions"
printf '# Rendez-vous de P3-bis — décision n° 1 (essai)\n\n> maintenir\n\nDécision : maintenir\nDate : 2026-11-20T12:00:05Z\n' > "$R/docs/decisions/rendez-vous-P3-bis-v1.md"
PYTHONPATH="$M" "$PY" -B -m controle_ia.scellement sceller "$R/docs/decisions/rendez-vous-P3-bis-v1.md" > /dev/null
printf '| RENDEZ-VOUS-P3BIS-1 | 2026-11-20T12:01:00Z | docs/decisions/rendez-vous-P3-bis-v1.md | %s |\n' \
    "$(sha "$R/docs/decisions/rendez-vous-P3-bis-v1.md")" >> "$R/registres/prealables-p3bis-v1.md"
cas "23 après « maintenir » : voie normale, rendez-vous sans objet" 0 "chemin normal (rendez-vous sans objet)" "$M" "$R" "$L/saine.md" --instant 2026-11-21T00:00:00Z

apres=$(sha256sum "$DEPOT/registres/prealables-p3bis-v1.md" "$DEPOT/registres/scellements-v1.md" | cut -d' ' -f1 | tr '\n' ' ')
total=$((total+1))
if [ "$avant" = "$apres" ] && [ ! -e "$DEPOT/registres/ouvertures-p3bis-v1.md" ]; then conformes=$((conformes+1)); echo "OK  24 registres réels inchangés, aucun journal créé dans le dépôt"; else echo "KO  24 registres réels changés ou journal créé"; fi
date -u +"fin : %Y-%m-%dT%H:%M:%SZ"
echo "BILAN : $conformes conformes sur $total"
[ "$conformes" = "$total" ] && echo "ESSAI : TOUT CONFORME" || { echo "ESSAI : ÉCART"; exit 1; }
