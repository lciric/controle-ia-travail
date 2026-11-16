#!/usr/bin/env bash
# Vérification, sur l'état actuel de main distant et des têtes du distant, de chaque constante écrite en dur dans le bloc 1B de
# commande-compte-3-phase-b-v3.md (règle R6 : tout chiffre renvoie à un chemin et une empreinte). Lecture seule : registres, pièces de
# code, textes scellés et têtes de branches ; rien de 7a ni de 7b n'est ouvert (de la branche de 7b, la seule tête est lue).
# Écrit le 2026-11-16 par le préparateur du brouillon v2 (modèle B) ; version 3 par le préparateur de la v3 (modèle A), dérivée par
# deriver_constantes_phase_b_v3_v1.py : noms v3, et deux contrôles ajoutés (noms interdits contre les chemins des entrées ; somme des
# tailles du bloc B3 contre prealables-v1.md, P1.4, sur main distant).
# Les variables sont tirées du texte de la commande : le document en ligne du bloc 1B est développé comme le bloc le fait, dans un
# dossier neuf, puis lu. Aucun fichier du dépôt n'est écrit ; aucune branche n'est créée.
#     bash verification_constantes_phase_b_v3.sh <dépôt réel> <dossier neuf> [<commande, défaut : celle du dépôt réel>]
set -u
DEPOT_REEL=$(cd "$1" && pwd); T="$2"
[ ! -e "$T" ] || { echo "ARRÊT : $T existe déjà"; exit 1; }
mkdir -p "$T"; T=$(cd "$T" && pwd)
ICI_REL=docs/procedures/lecture-7b-etape-b-compte-3-v1
CMD="${3:-$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-b-v3.md}"
export LC_ALL=C.UTF-8
date -u +"début de la vérification : %Y-%m-%dT%H:%M:%SZ"
echo "commande : $(sha256sum "$CMD" | cut -d' ' -f1)"
cd "$DEPOT_REEL" || exit 1
git fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main || { echo "ARRÊT : récupération de main"; exit 1; }
M=refs/remotes/origin/main; echo "main distant : $(git rev-parse "$M")"
python3 -I - "$CMD" "$T" <<'FIN' || { echo "ARRÊT : bloc 1B introuvable dans la commande"; exit 1; }
import pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
m = re.search(r'cat > "\$BAC/variables-v2\.sh" <<EOF\n(.*?)\nEOF\n', t, re.S)
h = re.search(r"^SESSION_HOTE=(session_[0-9A-Za-z]+)$", t, re.M)
assert m and h
pathlib.Path(sys.argv[2], "developpe.sh").write_text("cat <<EOF\n" + m.group(1) + "\nEOF\n", encoding="utf-8")
pathlib.Path(sys.argv[2], "session-hote.txt").write_text(h.group(1) + "\n", encoding="utf-8")
FIN
DEPOT="$DEPOT_REEL" BAC="$T/bac" SESSION_C3="$(cat "$T/session-hote.txt")" bash "$T/developpe.sh" > "$T/variables-v2.sh" || { echo "ARRÊT : développement du bloc 1B"; exit 1; }
. "$T/variables-v2.sh"
OK=0; KO=0
bon() { OK=$((OK + 1)); echo "conforme : $1"; }
mauvais() { KO=$((KO + 1)); echo "ÉCART : $1"; }
h() { git show "$M:$1" 2>/dev/null | sha256sum | cut -d' ' -f1; }          # empreinte d'un fichier de main distant
c() { git show "$M:$1.sha256" 2>/dev/null | cut -d' ' -f1; }              # première colonne de son compagnon
# --- registre des scellements
R="$T/scellements-v1.md"; git show "$M:registres/scellements-v1.md" > "$R"
for L in "$LIGNE_BASE_A" "$LIGNE_RUN6" "$LIGNE_CODE"; do k=$(printf '%s' "$L" | cut -d'|' -f2 | tr -d ' ')
    [ "$(grep -cxF -- "$L" "$R")" = 1 ] && [ "$(grep -c "^| $k |" "$R")" = 1 ] && bon "ligne $k du registre : égale à l'octet, une seule" || mauvais "ligne $k du registre"; done
for k in LECTURE-T08-BASE-A ISSUE-MOTS-ET-COUT-T06; do [ "$(grep -c "^| $k |" "$R")" = 0 ] && bon "aucune ligne $k au registre" || mauvais "ligne $k déjà inscrite"; done
[ "$(printf '%s' "$LIGNE_RUN6" | cut -d'|' -f5 | tr -d ' ')" = "$H_MANIF_7B" ] && [ "$(printf '%s' "$LIGNE_RUN6" | cut -d'|' -f4 | tr -d ' ')" = "runs/$R6/manifeste.json" ] \
    && bon "H_MANIF_7B et R6 égaux à la ligne RUN-CONFIRMATION-T06" || mauvais "H_MANIF_7B ou R6"
[ "$(printf '%s' "$LIGNE_CODE" | cut -d'|' -f5 | tr -d ' ')" = "$H_FICHE_CODE" ] && [ "$(printf '%s' "$LIGNE_CODE" | cut -d'|' -f4 | tr -d ' ')" = "$FICHE_CODE" ] \
    && bon "H_FICHE_CODE et FICHE_CODE égaux à la ligne CODE-MOTS-ET-COUT-T06" || mauvais "H_FICHE_CODE ou FICHE_CODE"
[ "$(printf '%s' "$LIGNE_BASE_A" | cut -d'|' -f5 | tr -d ' ')" = "$H_BASE_A" ] && bon "H_BASE_A égal à la ligne SCELLEMENT-T08-BASE-A" || mauvais "H_BASE_A"
# --- pièces de main, compagnons, commit cité
[ "$(h scripts/mots_et_cout_t06_v3.py)" = "$H_PIECE" ] && [ "$(h scripts/lancer_mots_et_cout_t06_v3.sh)" = "$H_LANCEUR" ] && bon "pièce et lanceur sur main : H_PIECE, H_LANCEUR" || mauvais "pièce ou lanceur sur main"
[ "$(h "$FICHE_CODE")" = "$H_FICHE_CODE" ] && [ "$(c "$FICHE_CODE")" = "$H_FICHE_CODE" ] && bon "fiche du code : empreinte et compagnon" || mauvais "fiche du code"
[ "$(h prereg/T0.8-base-A-mots-et-cout-v1.md)" = "$H_BASE_A" ] && [ "$(c prereg/T0.8-base-A-mots-et-cout-v1.md)" = "$H_BASE_A" ] && bon "texte scellé de la base (A) : empreinte et compagnon" || mauvais "base (A)"
[ "$(h prereg/T0.6-organismes-v0-v1.md)" = "$H_T06" ] && [ "$(c prereg/T0.6-organismes-v0-v1.md)" = "$H_T06" ] && bon "texte scellé de T0.6 : empreinte et compagnon" || mauvais "T0.6"
git cat-file -e "$COMMIT_PIECE^{commit}" 2>/dev/null && git merge-base --is-ancestor "$COMMIT_PIECE" "$M" && bon "commit de la pièce présent, ancêtre de main ($(git rev-list --count "$COMMIT_PIECE..$M") commits plus bas)" || mauvais "commit de la pièce"
[ "$(git show "$COMMIT_PIECE:scripts/mots_et_cout_t06_v3.py" | sha256sum | cut -d' ' -f1)" = "$H_PIECE" ] && [ "$(git show "$COMMIT_PIECE:scripts/lancer_mots_et_cout_t06_v3.sh" | sha256sum | cut -d' ' -f1)" = "$H_LANCEUR" ] \
    && bon "pièce et lanceur au commit cité : mêmes empreintes" || mauvais "pièce ou lanceur au commit cité"
git show "$M:$FICHE_CODE" | python3 -I -c 'import json, sys; d = json.load(sys.stdin); f = d["fichiers"]; sys.exit(0 if (d["commit"] == sys.argv[1] and f["scripts/mots_et_cout_t06_v3.py"] == sys.argv[2] and f["scripts/lancer_mots_et_cout_t06_v3.sh"] == sys.argv[3] and set(f) == {"scripts/mots_et_cout_t06_v3.py", "scripts/lancer_mots_et_cout_t06_v3.sh"}) else 1)' "$COMMIT_PIECE" "$H_PIECE" "$H_LANCEUR" \
    && bon "fiche du code : elle cite COMMIT_PIECE, H_PIECE et H_LANCEUR, et ces deux fichiers seuls" || mauvais "contenu de la fiche du code"
CL=$(git show "$M:$FICHE_CODE" | python3 -I -c 'import json, sys; d = json.load(sys.stdin)["contre_lecture"]; print(d["chemin"], d["sha256"])')
[ "$(h "${CL% *}")" = "${CL#* }" ] && [ "$(c "${CL% *}")" = "${CL#* }" ] && bon "contre-lecture citée par la fiche : présente sur main, empreinte et compagnon (${CL% *})" || mauvais "contre-lecture citée"
# --- attestation, liste, empreintes de lancement, exigences
A=$ICI_REL/attestation_qui_a_lu_quoi_compte_3_v3.py
[ "$(h "$A")" = "$H_ATTESTATION3" ] && bon "attestation v3 sur main : H_ATTESTATION3" || mauvais "attestation v3"
[ "$(h "$LISTE")" = "$EMPREINTE_LISTE" ] && [ "$(c "$LISTE")" = "$EMPREINTE_LISTE" ] && bon "liste « qui a lu quoi » ($LISTE) : empreinte et compagnon" || mauvais "liste"
mkdir -p "$T/att/$(dirname "$LISTE")"; git show "$M:$A" > "$T/att/a.py"; git show "$M:$LISTE" > "$T/att/$LISTE"; git show "$M:$LISTE.sha256" > "$T/att/$LISTE.sha256"
s=$(python3 -I -B "$T/att/a.py" "$T/att/$LISTE" "$EMPREINTE_LISTE" "$SESSION_C3" --admettre-hote "$CELLULE_HOTE" 2>&1); k=$?
[ "$k" = 0 ] && printf '%s' "$s" | grep -q "^ATTESTATION : CONFORME" && bon "attestation v3 jouée sur la liste réelle avec l'identifiant de la session hôte : $(printf '%s' "$s" | grep -o "lignes de l'hôte admises : [0-9]*")" || { mauvais "attestation sur la liste réelle (code $k)"; printf '%s\n' "$s" | cut -c1-300; }
n=0; t=0; while read -r e f; do t=$((t + 1)); [ "$(h "docs/$f")" = "$e" ] && n=$((n + 1)); done < <(git show "$M:docs/sha256sums-lancement-v2.txt")
[ "$t" -ge 1 ] && [ "$n" = "$t" ] && bon "empreintes de lancement : $n documents sur $t conformes sur main" || mauvais "empreintes de lancement ($n sur $t)"
git show "$M:requirements-cpu.txt" | grep -q -x 'numpy==2.4.6' && git show "$M:requirements-cpu.txt" | grep -q -x 'scipy==1.17.1' && git show "$M:requirements-cpu.txt" | grep -q -x 'torch==2.14.1' \
    && bon "requirements-cpu.txt sur main : numpy 2.4.6, scipy 1.17.1, torch 2.14.1 (versions exigées par le bloc B2)" || mauvais "versions de requirements-cpu.txt"
# --- journal des ouvertures (clés seulement)
J=$(git show "$M:registres/scellements-v1.md.ouvertures.md")
[ "$(printf '%s\n' "$J" | grep -c '^| *OUVERTURE-SONDES-T06 *|')" = 0 ] && [ "$(printf '%s\n' "$J" | awk -F'|' '$2 ~ /OUVERTURE-T07/ && $4 ~ /^ *etape-B/' | grep -c .)" = 0 ] \
    && bon "journal des ouvertures : $(printf '%s\n' "$J" | grep -c '^|') ligne(s), aucune ouverture des sondes de T0.6 ni de l'étape B" || mauvais "journal des ouvertures"
# --- aucune sortie de la pièce ni fichier de 7b suivi sur main (noms seulement)
[ "$(git ls-tree --name-only "$M" diag/ runs/ | grep -c -E '^(diag|runs)/[0-9]{8}-[0-9]{6}-mots-et-cout-t06$')" = 0 ] && bon "aucun dossier de run de la pièce sur main (noms)" || mauvais "un run de la pièce est déjà sur main"
[ "$(git ls-tree -r --name-only "$M" -- "runs/$R6" "diag/$R6" "donnees/$R6" | grep -c .)" = 0 ] && bon "aucun fichier du run de 7b suivi sur main (noms) : rien ne masque les entrées placées hors du dépôt" || mauvais "des fichiers du run de 7b sont suivis sur main"
# --- têtes du distant (empreintes seulement)
[ "$(git ls-remote "$DEPOT_URL" "refs/heads/$B7B" | cut -f1)" = "$TETE_7B" ] && bon "tête distante de $B7B : TETE_7B" || mauvais "tête de la branche de 7b"
[ -z "$(git ls-remote "$DEPOT_URL" "refs/heads/$BR_P")" ] && bon "branche $BR_P absente du distant (R12 : elle sera neuve)" || mauvais "la branche $BR_P existe déjà au distant"
# --- ajouts de la v3 : noms interdits contre les chemins des entrées ; somme des tailles du bloc B3 contre prealables-v1.md (P1.4)
n=0; for f in runs/$R6/manifeste.json diag/$R6/episodes-t06.json diag/$R6/lecture-cout-t06.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do
    for g in "$f" "$f.sha256"; do printf '%s\n' "./$g" | grep -q -i -E "$INTERDITS_NOMS" && n=$((n + 1)); done; done
[ "$n" = 0 ] && bon "INTERDITS_NOMS (bbis et b-bis compris) ne touche aucun des dix chemins des entrées (cas sain du bloc B3)" || mauvais "INTERDITS_NOMS touche $n chemin(s) des entrées"
P=$(git show "$M:$ICI_REL/prealables-v1.md" | grep '^| P1.4 |')
S=0; k=0; for nom in lecture-cout-t06.json episodes-t06.json manifeste.json mesures-t06.npz textes-actions-t06.jsonl; do
    o=$(printf '%s' "$P" | grep -o -E "${nom//./\\.}\` \(([0-9]{1,3}( [0-9]{3})*) o" | head -1 | grep -o -E '\(([0-9 ]+) o' | tr -dc '0-9')
    [ -n "$o" ] && { S=$((S + o)); k=$((k + 1)); }; done
[ "$k" = 5 ] && [ "$S" = 18959392 ] && grep -q -F '« 10 fichiers ; cinq entrées : 18959392 octets »' "$CMD" \
    && bon "somme des tailles des cinq entrées lue à P1.4 de prealables-v1.md (main distant) : $S octets, égale à l'attendu du bloc B3" || mauvais "somme des tailles ($k tailles lues, $S octets)"
[ "$(h "$ICI_REL/prealables-v1.md")" = 0cd96b629cb181246a8c2b15ad235719d72eaea64650552e0d482b630506c129 ] && bon "prealables-v1.md sur main : empreinte citée par la commande v1 (0cd96b62…)" || mauvais "prealables-v1.md"
case "$(git remote get-url origin)" in *lciric/controle-ia-travail*) bon "dépôt d'origine : lciric/controle-ia-travail";; *) mauvais "dépôt d'origine";; esac
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "CONSTANTES DE LA PHASE B : TOUT CONFORME" || echo "CONSTANTES DE LA PHASE B : ÉCARTS"
date -u +"fin de la vérification : %Y-%m-%dT%H:%M:%SZ"
