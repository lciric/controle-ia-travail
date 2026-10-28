#!/usr/bin/env bash
# Rejoue, sur le texte du pilote 4 une fois ses graines et empreintes écrites, les contrôles du lanceur v10 qui portent sur
# le texte (étape 2), sur la ligne de GO et les lignes de dépense (étape 4, sur des copies d'essai des registres, jamais
# sur main), et le contrôle des chemins postérieurs à 8e5e2f7b (étape 1) — conv-audit, 26 octobre 2026, v1.
# N'exécute ni le lanceur, ni le noyau, ni aucun code d'organisme ; ne lit aucun fichier de clé ; n'écrit que sous SORTIE.
# Usage : bash verifier_depart_pilote4_v1.sh DEPOT_PILOTE4 PYTHON SORTIE
set -euo pipefail
DEPOT="$1"; PY="$2"; SORTIE="$3"
R="$DEPOT/essaim-m3-refonte-v1"; PR="$R/prereg"; PC="$PR/pieces-pilote4-gemini"; T="$PR/pilote4-gemini-organisme-v4.md"
mkdir -p "$SORTIE"; pb=0
ok() { echo "OK   $*"; }
ko() { echo "ÉCHEC $*"; pb=1; }

SHA_LANCEUR=0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952
[ "$(sha256sum "$PC/lancer_pilote4_gemini_v10.sh" | cut -d' ' -f1)" = "$SHA_LANCEUR" ] && ok "lanceur v10 inchangé ($SHA_LANCEUR)" || ko "empreinte du lanceur v10"
SHA_T="$(sha256sum "$T" | cut -d' ' -f1)"; T16="${SHA_T:0:16}"
echo "texte : $SHA_T"

# script de vérification du texte (le v2 de la lignée)
if "$PY" -I "$PC/verifier_scellement_pilote4_v2.py" "$T" "$PC" "$PR/contre-lectures" > "$SORTIE/verifier-scellement-v2.txt" 2>&1; then ok "verifier_scellement_pilote4_v2.py : code 0"; else ko "verifier_scellement_pilote4_v2.py (voir $SORTIE/verifier-scellement-v2.txt)"; fi

# étape 2 du lanceur, transcrite
[ -f "$T.sha256" ] && [ "$(cut -d' ' -f1 < "$T.sha256")" = "$SHA_T" ] && ok "compagnon .sha256 du texte" || ko "compagnon .sha256 du texte"
grep -q "<<[A-Z0-9_]*>>" "$T" && ko "marqueurs <<…>> restants" || ok "aucun marqueur <<…>>"
grep -q "\[\[[A-Z0-9_]*\]\]" "$T" && ko "marqueurs [[…]] restants" || ok "aucun marqueur [[…]]"
grep -q "$SHA_LANCEUR" "$T" && ok "le texte cite l'empreinte du lanceur" || ko "le texte ne cite pas l'empreinte du lanceur"
E="$(grep -Eo 'entropie E = [0-9]+' "$T" | head -1 | grep -Eo '[0-9]+$' || true)"
[ -n "$E" ] && ok "entropie lue (première ligne)" || ko "entropie absente"
[ "$(grep -c 'entropie E =' "$T")" = 1 ] && ok "une seule ligne d'entropie" || ko "lignes d'entropie : $(grep -c 'entropie E =' "$T")"
for course in v6-2 v5-3; do
  if [ "$course" = v5-3 ]; then i=0; else i=1; fi
  g_texte="$(grep -Eo "graine de la course $course = [0-9]+" "$T" | grep -Eo '[0-9]+$' || true)"
  g_calc="$("$PY" -I -c 'import sys, numpy; e, i = int(sys.argv[1]), int(sys.argv[2]); print(int(numpy.random.SeedSequence(e).spawn(2)[i].generate_state(1, dtype=numpy.uint64)[0]))' "$E" "$i")"
  [ -n "$g_texte" ] && [ "$g_texte" = "$g_calc" ] && ok "graine $course = enfant $i de SeedSequence(E).spawn(2) = $g_calc" || ko "graine $course : texte $g_texte, calcul $g_calc"
  grep -q "graine de la course $course = $g_calc\b" "$T" && ok "garde du lanceur (grep \\b) sur la graine $course" || ko "garde du lanceur sur la graine $course"
done
echo "entropie $E" > "$SORTIE/graines.txt"; grep -E 'graine de la course (v6-2|v5-3) = ' "$T" | sed 's/^ *//' >> "$SORTIE/graines.txt"

# étape 4 : ligne de GO du § Plan, point 1, empreinte remplie, dans une copie d'essai du registre
LGO="$(grep -o '| GO-2026-10-25-02 | 2026-10-25 | calcul | extension : pilote 4 [^`]*' "$T" | head -1)"
[ -n "$LGO" ] && ok "ligne de GO extraite du texte" || ko "ligne de GO introuvable dans le texte"
LGO="${LGO//<empreinte du texte scellé>/$SHA_T}"
printf '%s\n' "$LGO" > "$SORTIE/ligne-go-remplie.txt"
REG="$SORTIE/registre-go-essai.md"; { echo "| GO-2026-10-25-02 | 2026-10-25 | calcul | ligne ancienne sans l'extension | | | | |"; echo "$LGO"; } > "$REG"
for arbre in 4f13647a 6251ab21; do
  l="$(grep "^| GO-2026-10-25-02 |" "$REG" | grep 'calcul' | grep 8b1c7511 | grep "$arbre" | grep "$T16" || true)"
  [ -n "$l" ] && ok "chaîne de grep du lanceur sur la ligne de GO (arbre $arbre, texte $T16)" || ko "chaîne de grep (arbre $arbre)"
done
grep -q 157a2b45 <<< "$LGO" && ok "la ligne de GO porte la banque 157a2b45" || ko "banque absente de la ligne de GO"
# artefacts : sans l'arbre de la v6.2.1 ; avec une empreinte de texte fausse
l="$(grep "^| GO-2026-10-25-02 |" "$REG" | grep 'calcul' | grep 8b1c7511 | grep 3b2d8d5a | grep "$T16" || true)"
[ -z "$l" ] && ok "artefact refusé : arbre de la v6.2 de Gemini (3b2d8d5a)" || ko "artefact accepté (3b2d8d5a)"
l="$(grep "^| GO-2026-10-25-02 |" "$REG" | grep 'calcul' | grep 8b1c7511 | grep 4f13647a | grep 0000000000000000 || true)"
[ -z "$l" ] && ok "artefact refusé : empreinte de texte fausse" || ko "artefact accepté (empreinte fausse)"

# lignes de dépense du § Plan, point 1
JOUR="$(date -u +%Y-%m-%d)"
D62="$(grep -o '| <date du jour> | pilote4-gemini-v6-2-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 |' "$T" | head -1)"
D53="$(grep -o '| <date du jour> | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 ; empreintes de la v6.2 <16 premiers caractères> |' "$T" | head -1)"
DSEG="$(grep -o '| <date du jour> | <nom de la course> segment K | GO-2026-10-25-02 | au plus 75 USD moins la dépense déjà faite | après le segment K−1 |' "$T" | head -1)"
[ -n "$D62" ] && [ -n "$D53" ] && [ -n "$DSEG" ] && ok "trois formes de lignes de dépense extraites du texte" || ko "lignes de dépense introuvables"
D62="${D62//<date du jour>/$JOUR}"; printf '%s\n' "$D62" > "$SORTIE/ligne-depense-v62.txt"
echo "$D62" | grep pilote4-gemini-v6-2-v1 | grep GO-2026-10-25-02 | grep -q 5ae4e801423bbef0 && ok "garde du lanceur sur la dépense de la v6.2 (nom, GO, empreintes de M)" || ko "dépense de la v6.2"
S2="$(echo "${DSEG//<date du jour>/$JOUR}" | sed 's/<nom de la course> segment K /pilote4-gemini-v6-2-v1 segment 2 /; s/K−1/1/')"
echo "$S2" | grep pilote4-gemini-v6-2-v1 | grep GO-2026-10-25-02 | grep -q "segment 2\b" && ok "garde du lanceur sur une ligne de segment 2" || ko "ligne de segment 2"

# étape 1 : chemins postérieurs à 8e5e2f7b
PERMIS="$(grep "^PERMIS_APRES_CODE=" "$PC/lancer_pilote4_gemini_v10.sh" | sed "s/^PERMIS_APRES_CODE='//; s/'$//")"
git -C "$DEPOT" merge-base --is-ancestor 8e5e2f7b HEAD && ok "8e5e2f7b ancêtre de HEAD" || ko "8e5e2f7b non ancêtre"
n="$(git -C "$DEPOT" diff --name-only 8e5e2f7b HEAD | wc -l)"
h="$( { git -C "$DEPOT" diff --name-only 8e5e2f7b HEAD | grep -Ev "$PERMIS" || true; } | wc -l)"   # grep sans ligne : code 1, pas un échec
[ "$h" = 0 ] && ok "chemins postérieurs à 8e5e2f7b : $n, aucun hors PERMIS_APRES_CODE" || ko "$h chemins hors PERMIS_APRES_CODE"
echo "tête : $(git -C "$DEPOT" rev-parse HEAD)"
[ "$pb" = 0 ] && echo "TOUT EST JUSTE" || { echo "PROBLÈMES"; exit 1; }
