#!/usr/bin/env bash
# Rejoue, sur le texte v5 du pilote 4 une fois sa graine et ses empreintes écrites, les contrôles du lanceur v11 qui portent
# sur le texte (étape 2 : graine de la course S recalculée depuis l'entropie, graine de la course M restituée), sur la ligne
# d'extension de GO et les lignes de dépense de la course S (étape 4, sur des copies d'essai des registres, jamais sur main),
# et le contrôle des chemins postérieurs à 8e5e2f7b (étape 1) — conv-audit, 26 octobre 2026, v2 (la v1 pour le texte v4).
# N'exécute ni le lanceur, ni le noyau, ni aucun code d'organisme ; ne lit aucun fichier de clé ; n'écrit que sous SORTIE.
# Usage : bash verifier_depart_pilote4_v2.sh DEPOT_PILOTE4 PYTHON SORTIE
# (DEPOT_PILOTE4 : la copie de conv-audit à la tête du départ ; session-depot rejoue les contrôles git sur sa copie de lancement, à cette tête, avant la ligne de GO ; P4C8-07, P4C8-08)
set -euo pipefail
DEPOT="$1"; PY="$2"; SORTIE="$3"
R="$DEPOT/essaim-m3-refonte-v1"; PR="$R/prereg"; PC="$PR/pieces-pilote4-gemini"; T="$PR/pilote4-gemini-organisme-v5.md"
L="$PC/lancer_pilote4_gemini_v11.sh"
mkdir -p "$SORTIE"; pb=0
ok() { echo "OK   $*"; }
ko() { echo "ÉCHEC $*"; pb=1; }
SHA_LANCEUR="$(sha256sum "$L" | cut -d' ' -f1)"
echo "lanceur v11 : $SHA_LANCEUR"
grep -q '^SHA_LANCEUR="$(sha256sum "$0"' "$L" && ok "le lanceur recalcule son empreinte depuis son propre fichier" || ko "le lanceur ne recalcule pas son empreinte"
SHA_T="$(sha256sum "$T" | cut -d' ' -f1)"; T16="${SHA_T:0:16}"
echo "texte : $SHA_T"
if "$PY" -I "$PC/verifier_scellement_pilote4_v3.py" "$T" "$PC" "$PR/contre-lectures" > "$SORTIE/verifier-scellement-v3.txt" 2>&1; then ok "verifier_scellement_pilote4_v3.py : code 0"; else ko "verifier_scellement_pilote4_v3.py (voir $SORTIE/verifier-scellement-v3.txt)"; fi
[ -f "$T.sha256" ] && [ "$(cut -d' ' -f1 < "$T.sha256")" = "$SHA_T" ] && ok "compagnon .sha256 du texte" || ko "compagnon .sha256 du texte"
grep -q "<<[A-Z0-9_]*>>" "$T" && ko "marqueurs <<…>> restants" || ok "aucun marqueur <<…>>"
grep -q "\[\[[A-Z0-9_]*\]\]" "$T" && ko "marqueurs [[…]] restants" || ok "aucun marqueur [[…]]"
grep -q "$SHA_LANCEUR" "$T" && ok "le texte cite l'empreinte du lanceur v11" || ko "le texte ne cite pas l'empreinte du lanceur v11"
E="$(grep -Eo 'entropie E = [0-9]+' "$T" | head -1 | grep -Eo '[0-9]+$' || true)"
[ -n "$E" ] && ok "entropie lue (première ligne)" || ko "entropie absente"
[ "$(grep -c 'entropie E =' "$T")" = 1 ] && ok "une seule ligne d'entropie" || ko "lignes d'entropie : $(grep -c 'entropie E =' "$T")"
g_texte="$(grep -Eo "graine de la course v6-2-s = [0-9]+" "$T" | grep -Eo '[0-9]+$' || true)"
g_calc="$("$PY" -I -c 'import sys, numpy; e = int(sys.argv[1]); print(int(numpy.random.SeedSequence(e).spawn(2)[0].generate_state(1, dtype=numpy.uint64)[0]))' "$E")"
[ -n "$g_texte" ] && [ "$g_texte" = "$g_calc" ] && ok "graine v6-2-s = enfant 0 de SeedSequence(E).spawn(2) = $g_calc" || ko "graine v6-2-s : texte $g_texte, calcul $g_calc"
grep -q "graine de la course v6-2-s = $g_calc\b" "$T" && ok "garde du lanceur (grep \\b) sur la graine v6-2-s" || ko "garde du lanceur sur la graine v6-2-s"
grep -Eq "^ *graine de la course v6-2 = 2334107546136117589\$" "$T" && ok "graine de la course M restituée (ligne entière, garde de la porte)" || ko "graine de la course M absente ou altérée"
[ "$(grep -Ec 'graine de la course \S+ =' "$T")" = 2 ] && ok "deux lignes de graine" || ko "lignes de graine : $(grep -Ec 'graine de la course \S+ =' "$T")"
{ echo "entropie $E"; grep -E 'graine de la course (v6-2-s|v6-2) = ' "$T" | sed 's/^ *//'; } > "$SORTIE/graines.txt"
LGO="$(grep -o '| GO-2026-10-25-02 | 2026-10-26 | calcul | extension : pilote 4, seconde course [^`]*' "$T" | head -1)"
[ -n "$LGO" ] && ok "ligne de GO de la course S extraite du texte" || ko "ligne de GO introuvable dans le texte"
LGO="${LGO//<empreinte du texte>/$SHA_T}"
printf '%s\n' "$LGO" > "$SORTIE/ligne-go-remplie.txt"
LGO_M="$(grep -o '| GO-2026-10-25-02 | 2026-10-25 | calcul | extension : pilote 4 (mot direct de Lazar, R-445 et R-448)[^`]*' "$PR/pilote4-gemini-organisme-v4.md" | head -1)"
LGO_M="${LGO_M//<empreinte du texte scellé>/782b858c537222245fd757c23ea6d75abae142df029eed3e53af36d8c78cfa95}"
REG="$SORTIE/registre-go-essai.md"; { echo "| GO-2026-10-25-02 | 2026-10-25 | calcul | ligne ancienne sans l'extension | | | | |"; echo "$LGO_M"; echo "$LGO"; } > "$REG"
l="$(grep "^| GO-2026-10-25-02 |" "$REG" | grep 'calcul' | grep a54da93e | grep 4f13647a | grep "$T16" || true)"
[ "$(echo "$l" | grep -c .)" = 1 ] && ok "chaîne de grep du lanceur sur la ligne de GO (question S a54da93e, arbre 4f13647a, texte $T16) : une ligne" || ko "chaîne de grep : $(echo "$l" | grep -c .) ligne(s)"
grep -q 157a2b45 <<< "$LGO" && ok "la ligne de GO porte la banque 157a2b45" || ko "banque absente de la ligne de GO"
grep -q "$SHA_LANCEUR" <<< "$LGO" && ok "la ligne de GO porte l'empreinte du lanceur v11" || ko "lanceur absent de la ligne de GO"
l="$(grep "^| GO-2026-10-25-02 |" "$REG" | grep 'calcul' | grep 8b1c7511 | grep 4f13647a | grep "$T16" || true)"
[ -z "$l" ] && ok "artefact refusé : la ligne de la course M (question M) ne fait pas partir la course S avec ce texte" || ko "artefact accepté (ligne M + texte v5)"
l="$(grep "^| GO-2026-10-25-02 |" "$REG" | grep 'calcul' | grep a54da93e | grep 6251ab21 || true)"
[ -z "$l" ] && ok "artefact refusé : arbre de la v5.3 (6251ab21) absent de la ligne S" || ko "artefact accepté (6251ab21)"
l="$(grep "^| GO-2026-10-25-02 |" "$REG" | grep 'calcul' | grep a54da93e | grep 4f13647a | grep 0000000000000000 || true)"
[ -z "$l" ] && ok "artefact refusé : empreinte de texte fausse" || ko "artefact accepté (empreinte fausse)"
JOUR="$(date -u +%Y-%m-%d)"
DS="$(grep -o '| <date du jour> | pilote4-gemini-v6-2-s-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 ; empreintes de la v6.2 <16 premiers caractères> |' "$T" | head -1)"
DSEG="$(grep -o '| <date du jour> | <nom de la course> segment K | GO-2026-10-25-02 | au plus 75 USD moins la dépense déjà faite | après le segment K−1 |' "$PR/pilote4-gemini-organisme-v4.md" | head -1)"
[ -n "$DS" ] && [ -n "$DSEG" ] && ok "formes des lignes de dépense extraites (course S : v5 ; segments : v4)" || ko "lignes de dépense introuvables"
DS="${DS//<date du jour>/$JOUR}"; DS="${DS//<16 premiers caractères>/0123456789abcdef}"; printf '%s\n' "$DS" > "$SORTIE/ligne-depense-s.txt"
echo "$DS" | grep pilote4-gemini-v6-2-s-v1 | grep GO-2026-10-25-02 | grep 5ae4e801423bbef0 | grep -q 0123456789abcdef && ok "garde du lanceur sur la dépense de la course S (nom, GO, empreintes de M, empreintes de la course M)" || ko "dépense de la course S"
S2="$(echo "${DSEG//<date du jour>/$JOUR}" | sed 's/<nom de la course> segment K /pilote4-gemini-v6-2-s-v1 segment 2 /; s/K−1/1/')"
echo "$S2" | grep pilote4-gemini-v6-2-s-v1 | grep GO-2026-10-25-02 | grep -q "segment 2\b" && ok "garde du lanceur sur une ligne de segment 2" || ko "ligne de segment 2"
PERMIS="$(grep "^PERMIS_APRES_CODE=" "$L" | sed "s/^PERMIS_APRES_CODE='//; s/'$//")"
[ -n "$PERMIS" ] && ok "PERMIS_APRES_CODE lu dans le lanceur v11" || ko "PERMIS_APRES_CODE illisible"
git -C "$DEPOT" merge-base --is-ancestor 8e5e2f7b HEAD && ok "8e5e2f7b ancêtre de HEAD" || ko "8e5e2f7b non ancêtre"
for c in 4967734a 90595ffb 7ea32705 a15809b8 4772b525; do git -C "$DEPOT" cat-file -e "$c^{commit}" 2>/dev/null && ok "commit $c présent" || ko "commit $c absent"; done
n="$(git -C "$DEPOT" diff --name-only 8e5e2f7b HEAD | wc -l)"
h="$( { git -C "$DEPOT" diff --name-only 8e5e2f7b HEAD | grep -Ev "$PERMIS" || true; } | wc -l)"
[ "$h" = 0 ] && ok "chemins postérieurs à 8e5e2f7b : $n, aucun hors PERMIS_APRES_CODE" || ko "$h chemins hors PERMIS_APRES_CODE : $(git -C "$DEPOT" diff --name-only 8e5e2f7b HEAD | grep -Ev "$PERMIS" | head -3 | tr '\n' ' ')"
[ -z "$(git -C "$DEPOT" status --porcelain | grep -v " essaim-m3-refonte-v1/pilotes/" || true)" ] && ok "arbre de travail propre (hors pilotes/)" || ko "fichiers non suivis ou modifiés dans la copie (hors pilotes/)"
echo "tête : $(git -C "$DEPOT" rev-parse HEAD)"
[ "$pb" = 0 ] && echo "TOUT EST JUSTE" || { echo "PROBLÈMES"; exit 1; }
