#!/usr/bin/env bash
# Répétition de bout en bout, sur dépôts jouets, de tous les blocs de commande-compte-3-phase-b-v3.md (règle R5 : chaque bloc sur un cas
# sain, chaque garde d'arrêt sur un artefact), plus le bloc V de la mère (section 15), le bloc M de la phase C v3 rejoué sur la branche
# jouet de la pièce, et la reprise du fichier d'issue comme le fera le bloc C2 de la phase C.
# Écrite le 2026-11-16 par le préparateur du brouillon v2 (modèle B) ; version 3 par le préparateur de la v3 (modèle A), dérivée par
# deriver_repetition_phase_b_v3_v1.py : noms v3, et contrôles ajoutés (bloc M de la phase C v3 égal à celui du brouillon 1 de sa v4,
# forme du bloc C2 des deux versions ; somme des tailles du bloc B3 ; nom « bbis » parmi les entrées ; pip sans cache au bloc B2 ;
# nom, titre et premier fait du journal provisoire v3). Aucune donnée réelle :
# dépôt distant jouet (main jouet : code de src/controle_ia et pièce « mots et coût » v3 recopiés du dépôt réel, textes scellés de T0.6
# et de la base (A) recopiés, registre jouet ; branches de 7b jouets : entrées FACTICES de fabrique_depots_jouets_phase_b_v3.py, au
# nom de run réel, fichiers fermés factices compris pour vérifier qu'ils ne sont jamais extraits), HOME jouet, identifiant de session de
# l'hôte posé à la main. La VRAIE pièce est jouée par son VRAI lanceur, en mode réel, sur ces entrées factices : codes 0, 2 et 3.
# Surcharges, et seulement elles, ajoutées en fin de variables-v2.sh après le bloc 1B : DEPOT_URL, TETE_7B, H_MANIF_7B, LIGNE_RUN6,
# COMMIT_PIECE, LIGNE_CODE, H_FICHE_CODE (les empreintes des fichiers jouets) ; puis, par passe ou par artefact, celles que chaque ligne
# « surcharge » imprime (B7B, BR_P, PLACE_MIN_KIO, LISTE…). Les variables de tête des blocs F-B et V sont remplies par programme.
# N'écrit rien hors du bac donné ; ne touche pas le dépôt réel ; aucun réseau hors l'en-tête Date de pypi.org (bloc 2B).
#     bash repetition_phase_b_jouet_v3.sh <dépôt réel> <bac neuf> [<commande à répéter, défaut : celle du dépôt réel>]
set -u
DEPOT_REEL=$(cd "$1" && pwd); T="$2"
[ ! -e "$T" ] || { echo "ARRÊT : $T existe déjà"; exit 1; }
mkdir -p "$T"; T=$(cd "$T" && pwd)
ICI_REL=docs/procedures/lecture-7b-etape-b-compte-3-v1
CMD="${3:-$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-b-v3.md}"; CMD_C="$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-c-v3.md"; CMD_C4="$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-c-v4-brouillon1.md"
ICI_SCRIPT=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
export LC_ALL=C.UTF-8 GIT_AUTHOR_NAME=jouet GIT_AUTHOR_EMAIL=jouet@exemple.invalid GIT_COMMITTER_NAME=jouet GIT_COMMITTER_EMAIL=jouet@exemple.invalid
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
PYR="$DEPOT_REEL/.venv/bin/python"; R6=20261111-151701-t06-reel; HOTE=016QhUrrSUMEzEqWPnQYxjHB
BRP=verdict/t06-mots-et-cout-compte-3-v1; HOME_REEL="$HOME"
date -u +"début de la répétition : %Y-%m-%dT%H:%M:%SZ"
mkdir -p "$T/blocs" "$T/sorties"
python3 -I - "$CMD" "$T/blocs" b <<'FIN'
import hashlib, pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"); b = re.findall(r"```bash\n(.*?)```", t, re.S)
for i, x in enumerate(b):
    pathlib.Path(sys.argv[2], f"{sys.argv[3]}{i:02d}.sh").write_text(x, encoding="utf-8")
print(f"commande : {hashlib.sha256(t.encode()).hexdigest()} ; {len(b)} blocs ; blocs mis bout à bout : {hashlib.sha256(''.join(b).encode()).hexdigest()}")
FIN
python3 -I - "$CMD_C" "$T/blocs" c <<'FIN' > /dev/null
import pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"); b = re.findall(r"```bash\n(.*?)```", t, re.S)
pathlib.Path(sys.argv[2], "bloc-m-phase-c-v3.sh").write_text(b[-1], encoding="utf-8")
FIN
python3 -I - "$CMD_C4" "$T/blocs" c <<'FIN' > /dev/null
import pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"); b = re.findall(r"```bash\n(.*?)```", t, re.S)
pathlib.Path(sys.argv[2], "bloc-m-phase-c-v4-brouillon1.sh").write_text(b[-1], encoding="utf-8")
FIN
B="$T/blocs"   # b00 crochet (non joué ici), b01 aptitude, b02 0b-B, b03 1B, b04 2B, b05 B1, b06 B2, b07 B3, b08 B4, b09 B5a, b10 B5-attente, b11 B5b, b12 F-B, b13 bloc V
OK=0; KO=0; N=0; DERNIERE=""
bon() { OK=$((OK + 1)); echo "conforme : $1"; }
mauvais() { KO=$((KO + 1)); echo "ÉCART : $1"; }
n=0; for f in "$B"/b[0-9][0-9].sh "$B/bloc-m-phase-c-v3.sh"; do bash -n "$f" 2>/dev/null && n=$((n + 1)); done
[ "$n" = 15 ] && [ "$(ls "$B"/b[0-9][0-9].sh | wc -l)" = 14 ] && [ "$(wc -l < "$B/b00.sh")" = 2 ] && grep -q '^sha256sum scripts/' "$B/b00.sh" \
    && bon "quatorze blocs dans la commande (le premier est l'épreuve du crochet, non jouée ici) ; syntaxe des quatorze blocs et du bloc M (bash -n)" \
    || mauvais "nombre de blocs ou syntaxe ($n sur 15)"
crochet() {   # texte d'un bloc passé au crochet de garde du dépôt réel (lecture seule) : code 0 s'il passe, 2 s'il est bloqué
    python3 -I - "$1" "$DEPOT_REEL" <<'FIN' | python3 -I "$DEPOT_REEL/.claude/hooks/garde_calcul.py" >/dev/null 2>&1
import json, sys
print(json.dumps({"tool_input": {"command": open(sys.argv[1], encoding="utf-8").read()}, "cwd": sys.argv[2]}))
FIN
}
crochet "$B/b00.sh"; [ "$?" = 2 ] && bon "épreuve du crochet : le texte du premier bloc est bloqué par le crochet de garde du dépôt (code 2)" || mauvais "épreuve du crochet : premier bloc non bloqué"
n=0; for f in "$B"/b0[1-9].sh "$B"/b1[0-3].sh; do crochet "$f"; [ "$?" = 0 ] && n=$((n + 1)); done
[ "$n" = 13 ] && bon "les treize autres blocs passent le crochet de garde (aucun motif de lancement payant ni d'arrêt par motif)" || mauvais "crochet : $n blocs sur 13 passent"
grep -q 'lecture_etat_ba_l2_mere_v1.py' "$B/bloc-m-phase-c-v3.sh" && bon "bloc M extrait de la commande de la phase C v3 (son dernier bloc)" || mauvais "bloc M introuvable dans la phase C v3"
cmp -s "$B/bloc-m-phase-c-v3.sh" "$B/bloc-m-phase-c-v4-brouillon1.sh" && bon "bloc M du brouillon 1 de la phase C v4 égal à l'octet à celui de la v3 ($(sha256sum "$B/bloc-m-phase-c-v3.sh" | cut -c1-12)…)" || mauvais "bloc M : la v4 diffère de la v3"
LIGNE_IS='IS=$(grep '"'"'^| ISSUE-MOTS-ET-COUT-T06 |'"'"' registres/scellements-v1.md | cut -d'"'"'|'"'"' -f4 | tr -d '"'"' '"'"')'
for v in v3 v4-brouillon1; do f="$DEPOT_REEL/$ICI_REL/commande-compte-3-phase-c-$v.md"
    [ "$(grep -c -x -F "$LIGNE_IS" "$f")" = 3 ] && grep -q -F 'place . "refs/remotes/origin/$BR_P" "$IS"; place . "refs/remotes/origin/$BR_P" "$IS.sha256"; fi' "$f" \
        && grep -q -F "BR_P='<<BRANCHE_PIECE>>'" "$f" \
        && bon "phase C $v : fichier d'issue lu par la ligne ISSUE-MOTS-ET-COUT-T06 (C2, C5, F-C), repris sur <<BRANCHE_PIECE>> au bloc C2, comme la répétition le joue" \
        || mauvais "phase C $v : forme du bloc C2 autre que celle que la répétition joue"; done

# ============================================================== entrées factices (aucune donnée du programme)
PYTHONPATH="$DEPOT_REEL/src" "$PYR" -P -B "$ICI_SCRIPT/fabrique_depots_jouets_phase_b_v3.py" "$DEPOT_REEL" "$T/entrees" || { echo "ARRÊT : fabrique des entrées factices"; exit 1; }
HMJ=$(sha256sum "$T/entrees/saines/runs/$R6/manifeste.json" | cut -d' ' -f1)

# ============================================================== dépôt distant jouet
DIST="$T/distant/lciric/controle-ia-travail.git"; mkdir -p "$(dirname "$DIST")"
git init -q --bare "$DIST"; git -C "$DIST" symbolic-ref HEAD refs/heads/main; git -C "$DIST" config uploadpack.allowFilter true; git -C "$DIST" config uploadpack.allowAnySHA1InWant true
W="$T/travail"; git init -q -b main "$W"
copie() { mkdir -p "$W/$(dirname "$1")"; cp "$DEPOT_REEL/$1" "$W/$1"; [ -e "$DEPOT_REEL/$1.sha256" ] && cp "$DEPOT_REEL/$1.sha256" "$W/$1.sha256"; true; }
scelle() { (cd "$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256"); }
# 1) commit de la pièce (tient lieu du commit cité par CODE-MOTS-ET-COUT-T06) : code, pièce, essais, textes scellés, contre-lecture factice
for f in .gitignore requirements-cpu.txt scripts/mots_et_cout_t06_v3.py scripts/lancer_mots_et_cout_t06_v3.sh scripts/fabrique_factice_mots_et_cout_t06_v1.py \
         tests/test_mots_et_cout_t06_v3.py scripts/banc_mutations_mots_et_cout_t06_v3.py scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py \
         prereg/T0.8-base-A-mots-et-cout-v1.md prereg/T0.6-organismes-v0-v1.md docs/sha256sums-lancement-v2.txt docs/brief-claude-code-programme-complet-v2.md \
         docs/programme-controle-ia-v2.md docs/etat-de-l-art-controle-ia-v1.md; do copie "$f"; done
(cd "$DEPOT_REEL" && git ls-files -z src/controle_ia | xargs -0 -I{} cp --parents {} "$W/")
CL=docs/notes/piece-mots-et-cout-v1/contre-lecture-jouet-v1.md; mkdir -p "$W/$(dirname "$CL")"
printf 'Contre-lecture FACTICE (répétition de la phase B) : sans vue des données de 7b.\n' > "$W/$CL"; scelle "$W/$CL"
git -C "$W" add -A >/dev/null; git -C "$W" commit -q -m "pièce jouet (tient lieu du commit cité)"; CPJ=$(git -C "$W" rev-parse HEAD)
# 2) fiche du code (écrite par la pièce elle-même), registre jouet, journal jouet, commande, attestation, listes
FICHE=registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json
(cd "$W" && PYTHONPATH="$W/src" "$PYR" -P -B scripts/mots_et_cout_t06_v3.py ecrire-fichier-code . "$CPJ" "$FICHE" --contre-lecture "$CL" > /dev/null) || { echo "ARRÊT : fiche du code jouet"; exit 1; }
scelle "$W/$FICHE"; HFJ=$(sha256sum "$W/$FICHE" | cut -d' ' -f1)
LBA=$(grep '^| SCELLEMENT-T08-BASE-A |' "$DEPOT_REEL/registres/scellements-v1.md")
LRJ="| RUN-CONFIRMATION-T06 | 2026-11-13T18:52:43Z | runs/$R6/manifeste.json | $HMJ |"
LCJ="| CODE-MOTS-ET-COUT-T06 | 2026-11-14T14:55:41Z | $FICHE | $HFJ |"
printf '%s\n' "# Registre des scellements (jouet, répétition de la phase B)" "" "$LBA" "$LRJ" "$LCJ" > "$W/registres/scellements-v1.md"
Z=$(printf '%064d' 0)
printf '%s\n' "| OUVERTURE-T07 | 2026-11-14T00:14:00Z | etape-A/jouet/un | $Z |" "| OUVERTURE-T07 | 2026-11-14T00:14:01Z | etape-A/jouet/deux | $Z |" > "$W/registres/scellements-v1.md.ouvertures.md"
mkdir -p "$W/$ICI_REL"; cp "$CMD" "$W/$ICI_REL/commande-compte-3-phase-b-v3.md"
cp "$DEPOT_REEL/$ICI_REL/attestation_qui_a_lu_quoi_compte_3_v3.py" "$DEPOT_REEL/$ICI_REL/lecture_etat_ba_l2_mere_v1.py" "$W/$ICI_REL/"
cp "$DEPOT_REEL/registres/qui-a-lu-quoi-v2.md" "$DEPOT_REEL/registres/qui-a-lu-quoi-v2.md.sha256" "$W/registres/"
CELLULE='analyse du verdict A ; étape B bis (conception et verdicts) ; T0.8 ; G0 ; préenregistrement NARCBench (rédaction, contre-lecture, course) ; brouillons des papiers B et C ; code de la pièce « mots et coût »'
ENT='| n° | session | compte | modèle | a lu | rôle | source | exclu de |'
printf '%s\n' "# Liste jouet : la ligne de l'hôte à la cellule admise" "" "$ENT" "|---|---|---|---|---|---|---|---|" \
    "| 1 | session_$HOTE (hôte du verdict A) | compte 3 | modèle A | rien ouvert | hôte de la phase A | jouet | $CELLULE |" > "$W/registres/qui-a-lu-quoi-jouet-hote-admis.md"
printf '%s\n' "# Liste jouet (artefact) : la ligne de l'hôte à une autre cellule" "" "$ENT" "|---|---|---|---|---|---|---|---|" \
    "| 1 | session_$HOTE (hôte du verdict A) | compte 3 | modèle A | rien ouvert | hôte de la phase A | jouet | analyse du verdict A ; course de la pièce « mots et coût » |" > "$W/registres/qui-a-lu-quoi-jouet-artefact.md"
scelle "$W/registres/qui-a-lu-quoi-jouet-hote-admis.md"; scelle "$W/registres/qui-a-lu-quoi-jouet-artefact.md"
HLA=$(sha256sum "$W/registres/qui-a-lu-quoi-jouet-hote-admis.md" | cut -d' ' -f1); HLX=$(sha256sum "$W/registres/qui-a-lu-quoi-jouet-artefact.md" | cut -d' ' -f1)
git -C "$W" add -A >/dev/null; git -C "$W" commit -q -m "registre jouet, commande, listes"
# 3) quelques commits de plus : un clone superficiel de main n'a plus le commit de la pièce
for i in 1 2 3; do mkdir -p "$W/docs/notes/jouet"; echo "note jouet $i" > "$W/docs/notes/jouet/note-$i.md"; scelle "$W/docs/notes/jouet/note-$i.md"; git -C "$W" add -A >/dev/null; git -C "$W" commit -q -m "note jouet $i"; done
git -C "$W" push -q "$DIST" main 2>/dev/null; MAIN0=$(git -C "$DIST" rev-parse main)
# 4) branches de 7b jouets (orphelines) : saine (avec des fichiers fermés factices), et quatre artefacts
pose() { mkdir -p "$W/$(dirname "$1")"; printf '%s' "$2" > "$W/$1"; scelle "$W/$1"; }
branche7b() {   # $1 nom de branche ; $2 jeu d'entrées ; $3 « fermes » : ajoute des fichiers fermés factices
    git -C "$W" switch -q --orphan "$1"; git -C "$W" rm -rq . >/dev/null 2>&1; find "$W" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
    cp -r "$T/entrees/$2/." "$W/"
    if [ "${3:-}" = fermes ]; then for f in diag/$R6/lecture-sondes-t06.json diag/$R6/resume.json diag/$R6/distillation-t06.json \
        donnees/$R6/activations-sous-ensemble-t06-000.npz donnees/$R6/adaptateur-saboteur.pt; do pose "$f" "fichier fermé FACTICE $f"; done; fi
    git -C "$W" add -A -f >/dev/null; git -C "$W" commit -q -m "7b jouet ($2)"; git -C "$W" push -q "$DIST" "$1" 2>/dev/null; git -C "$W" rev-parse HEAD; }
B7B=calcul/t06-confirmation-7b-v1
TETE7B=$(branche7b "$B7B" saines fermes); T_EFF=$(branche7b jouet/7b-effectifs effectifs); T_JET=$(branche7b jouet/7b-jetons jetons)
T_ARR=$(branche7b jouet/7b-arret arret); T_CPF=$(branche7b jouet/7b-compagnon-faux compagnon-faux)
git -C "$W" switch -q main
echo "dépôt distant jouet : main $MAIN0 (commit de la pièce $CPJ, 4 commits plus bas) ; branche de 7b jouet $TETE7B ; manifeste factice $HMJ"

# ============================================================== outils de la répétition
joue() {   # $1 nom ; $2 bloc ; $3 code attendu ; $4 motif attendu
    local s c; s=$(cd "$DEP" && bash "$2" 2>&1); c=$?; N=$((N + 1)); DERNIERE="$s"
    printf '%s\n' "$s" > "$T/sorties/$(printf '%03d' "$N")-$(basename "$2" .sh).txt"
    if [ "$c" = "$3" ] && printf '%s' "$s" | grep -qF -- "$4"; then OK=$((OK + 1)); echo "conforme : $1 (code $c)"
    else KO=$((KO + 1)); echo "ÉCART : $1 (code $c, attendu $3 ; motif « $4 »)"; printf '%s\n' "$s" | tail -12 | cut -c1-300 | sed 's/^/    /'; fi; }
pseudo_venv() {   # environnement jouet, sans copie : mêmes bibliothèques que le .venv du dépôt réel, par liens (dossier ignoré par git)
    mkdir -p "$1/.venv/bin"; cp "$DEPOT_REEL/.venv/pyvenv.cfg" "$1/.venv/"; ln -s "$DEPOT_REEL/.venv/lib" "$1/.venv/lib"
    ln -s "$(readlink -f "$DEPOT_REEL/.venv/bin/python")" "$1/.venv/bin/python"; }
session() {   # $1 nom ; $2 complet | superficiel ; $3 venv | sans-venv ; $4 dépôt distant (défaut : $DIST)
    local d="${4:-$DIST}"; S="$T/s-$1"; mkdir -p "$S/home"; DEP="$S/depot"
    if [ "$2" = superficiel ]; then git clone -q --depth 1 "file://$d" "$DEP"; else git clone -q "$d" "$DEP"; fi
    git -C "$DEP" config user.name jouet; git -C "$DEP" config user.email jouet@exemple.invalid
    [ "$3" = venv ] && pseudo_venv "$DEP"
    export HOME="$S/home" CLAUDE_CODE_REMOTE_SESSION_ID="cse_$HOTE"; BACJ="$HOME/bac-mots-et-cout-compte-3-v2"; VAR="$BACJ/variables-v2.sh"; DISTS="$d"; }
surcharge() { printf '%s\n' "$1" >> "$VAR"; }
surcharges_jouet() { surcharge "DEPOT_URL='file://$DISTS'; TETE_7B=$TETE7B; H_MANIF_7B=$HMJ; COMMIT_PIECE=$CPJ; H_FICHE_CODE=$HFJ"; surcharge "LIGNE_RUN6='$LRJ'"; surcharge "LIGNE_CODE='$LCJ'"; }
attendre() {   # $1 bloc ; $2 motif d'attente : rejoue le bloc tant que sa sortie porte ce motif (120 fois au plus, 2 s entre deux)
    local i s; for i in $(seq 1 120); do s=$(cd "$DEP" && bash "$1" 2>&1); printf '%s' "$s" | grep -qF -- "$2" || { printf '%s\n' "$s"; return 0; }
        python3 -c 'import time; time.sleep(2)'; done; printf '%s\n' "$s"; return 1; }
remplir_fb() { python3 -I - "$B/b12.sh" "$1" <<'FIN'
import sys
t = open(sys.argv[1], encoding="utf-8").read()
t = t.replace("CROCHET='<bloquée | passée>'", "CROCHET='bloquée'").replace("session hôte : <modèle A | modèle C>", "session hôte : modèle A")
open(sys.argv[2], "w", encoding="utf-8").write(t)
FIN
}
remplir_v() {   # $1 sortie ; $2 base ; $3 commit ; $4 lignes ; $5 branche
    BASE="$2" COMMIT="$3" LIGNES="$4" BR="$5" python3 -I - "$B/b13.sh" "$1" <<'FIN'
import os, sys
t = open(sys.argv[1], encoding="utf-8").read()
for a, b in (("<base main rendue par la session hôte>", os.environ["BASE"]), ("<commit des sorties rendu par la session hôte>", os.environ["COMMIT"]),
             ("<lignes rendues par B5b>", os.environ["LIGNES"]), ("BRP=verdict/t06-mots-et-cout-compte-3-v1;", "BRP=" + os.environ["BR"] + ";")):
    assert t.count(a) == 1, a
    t = t.replace(a, b)
open(sys.argv[2], "w", encoding="utf-8").write(t)
FIN
}
refuser_pousses() { printf '#!/bin/sh\necho "refus jouet de la répétition" >&2\nexit 1\n' > "$1/hooks/pre-receive"; chmod +x "$1/hooks/pre-receive"; }

# ============================================================== passe 1 : clone complet, installation suivie de bout en bout, code 0
session p1 complet sans-venv
joue "[p1] bloc 0-B, second appel (place, clone, fichiers non suivis : 0)" "$B/b01.sh" 0 "fichiers non suivis, non ignorés (dix au plus) : 0"
joue "[p1] bloc 0b-B (main distant, empreinte de la commande lue sur main)" "$B/b02.sh" 0 "$(sha256sum "$CMD" | cut -d' ' -f1)  $ICI_REL/commande-compte-3-phase-b-v3.md (sur main distant)"
echo "x" >> "$DEP/requirements-cpu.txt"
joue "[p1] artefact : fichier suivi modifié → 0b-B arrête" "$B/b02.sh" 1 "ARRÊT : modifications suivies dans ton dépôt"
git -C "$DEP" checkout -q -- requirements-cpu.txt
joue "[p1] artefact : bloc B2 avant le bloc 1B → rien (variables absentes)" "$B/b06.sh" 1 "variables-v2.sh"
joue "[p1] bloc 1B (variables ; session = hôte de la phase A)" "$B/b03.sh" 0 "session : session_$HOTE"
joue "[p1] artefact : bloc 1B relancé → arrêt (bac déjà là)" "$B/b03.sh" 1 "existe déjà : rapport à la mère"
surcharges_jouet
cp "$VAR" "$T/variables-p1-saines.sh"
surcharge "LISTE=registres/qui-a-lu-quoi-jouet-artefact.md; EMPREINTE_LISTE=$HLX"
joue "[p1] artefact : liste où l'hôte porte une autre cellule → 2B arrête" "$B/b04.sh" 1 "attestation « qui a lu quoi » non conforme"
surcharge "LISTE=registres/qui-a-lu-quoi-jouet-hote-admis.md; EMPREINTE_LISTE=$HLA"
joue "[p1] bloc 2B, liste jouet où l'hôte est à sa cellule : admis" "$B/b04.sh" 0 "lignes de l'hôte admises : 1"
cp "$T/variables-p1-saines.sh" "$VAR"
surcharge "H_ATTESTATION3=$Z"
joue "[p1] artefact : empreinte de l'attestation autre → 2B arrête" "$B/b04.sh" 1 "ARRÊT : pièce de l'attestation"
cp "$T/variables-p1-saines.sh" "$VAR"
mkdir -p "$T/faux-curl-vieux" "$T/faux-curl-muet"
printf '#!/bin/sh\nprintf "HTTP/2 200\\r\\ndate: Mon, 16 Nov 2026 00:00:00 GMT\\r\\n\\r\\n"\n' > "$T/faux-curl-vieux/curl"; printf '#!/bin/sh\nexit 6\n' > "$T/faux-curl-muet/curl"; chmod +x "$T"/faux-curl-*/curl
PATH_REEL="$PATH"; export PATH="$T/faux-curl-vieux:$PATH_REEL"
joue "[p1] artefact : horloge de référence décalée (faux curl) → 2B arrête" "$B/b04.sh" 1 "horloge décalée de plus de 120 s"
export PATH="$T/faux-curl-muet:$PATH_REEL"
joue "[p1] artefact : horloge de référence injoignable (faux curl) → 2B arrête" "$B/b04.sh" 1 "injoignable"
export PATH="$PATH_REEL"
git -C "$DEP" branch -q lot/compte-3-v1
joue "[p1] artefact : branche locale du lot du compte 3 → 2B arrête" "$B/b04.sh" 1 "branche locale lot/compte-3-v1"
git -C "$DEP" branch -q -D lot/compte-3-v1
git -C "$DEP" config --unset user.name
joue "[p1] artefact : identité git absente → 2B arrête" "$B/b04.sh" 1 "identité git"
git -C "$DEP" config user.name jouet
joue "[p1] bloc 2B (horloge, attestation v3 sur la liste v2 réelle, lue sur main distant)" "$B/b04.sh" 0 "lignes de l'hôte admises : 0"
printf '%s' "$DERNIERE" | grep -q "contrôles d'entrée conformes" && bon "[p1] 2B : « contrôles d'entrée conformes »" || mauvais "[p1] 2B sans sa ligne finale"
joue "[p1] artefact : bloc B2 avant le bloc B1 → arrêt (pas sur la branche)" "$B/b06.sh" 1 "tu n'es pas sur $BRP"
echo "fichier égaré" > "$DEP/fichier-egare-jouet.txt"
joue "[p1] artefact : fichier non suivi dans le dépôt → B1 arrête avant de créer la branche (nom affiché, rien d'effacé)" "$B/b05.sh" 1 "arbre de travail non propre"
[ -e "$DEP/fichier-egare-jouet.txt" ] && printf '%s' "$DERNIERE" | grep -q 'fichier-egare-jouet.txt' && [ -z "$(git -C "$DIST" for-each-ref "refs/heads/$BRP")" ] \
    && bon "[p1] le fichier égaré est nommé, toujours là ; aucune branche créée au distant" || mauvais "[p1] fichier égaré"
rm -f "$DEP/fichier-egare-jouet.txt"
surcharge "COMMIT_PIECE=$TETE7B"
joue "[p1] artefact : commit de la pièce non ancêtre de main → B1 arrête" "$B/b05.sh" 1 "n'est pas un ancêtre de main"
surcharge "COMMIT_PIECE=0000000000000000000000000000000000000001"
joue "[p1] artefact : commit de la pièce absent (clone complet) → B1 arrête" "$B/b05.sh" 1 "absent de ton dépôt"
cp "$T/variables-p1-saines.sh" "$VAR"
[ "$(git -C "$DEP" rev-parse --abbrev-ref HEAD)" = main ] && [ -z "$(git -C "$DIST" for-each-ref "refs/heads/$BRP")" ] && bon "[p1] après ces arrêts : aucune branche créée, ni ici ni au distant" || mauvais "[p1] branche créée trop tôt"
surcharge "LIGNE_CODE='$(printf '%s' "$LCJ" | sed 's/14:55:41Z/14:55:42Z/')'"
joue "[p1] artefact : ligne CODE-MOTS-ET-COUT-T06 autre d'un caractère → B1 arrête avant la poussée" "$B/b05.sh" 1 "ligne CODE-MOTS-ET-COUT-T06 absente, autre ou en double"
cp "$T/variables-p1-saines.sh" "$VAR"; surcharge "H_PIECE=$Z"
joue "[p1] artefact : empreinte attendue de la pièce autre → B1 arrête avant la poussée" "$B/b05.sh" 1 "ARRÊT : pièces de main"
cp "$T/variables-p1-saines.sh" "$VAR"
[ -z "$(git -C "$DIST" for-each-ref "refs/heads/$BRP")" ] && bon "[p1] après ces arrêts : branche locale créée, rien poussé" || mauvais "[p1] poussée trop tôt"
refuser_pousses "$DIST"
joue "[p1] artefact : poussée refusée → B1 arrête" "$B/b05.sh" 1 "poussée refusée : rapport à la mère"
rm -f "$DIST/hooks/pre-receive"
joue "[p1] bloc B1 relancé (branche déjà créée ; lignes, pièces, empreintes de lancement, poussée éprouvée)" "$B/b05.sh" 0 "branche $BRP poussée (égale à main"
printf '%s' "$DERNIERE" | grep -q "déjà créée (bloc relancé)" && [ "$(git -C "$DIST" rev-parse "refs/heads/$BRP")" = "$MAIN0" ] && bon "[p1] B1 : reprise dite, branche distante égale à main" || mauvais "[p1] B1 reprise"
joue "[p1] bloc B1 relancé après sa poussée (admis : la branche distante est la sienne)" "$B/b05.sh" 0 "branche $BRP poussée (égale à main"
# --- bloc B2 : le chemin d'installation, suivi de bout en bout sur un fichier d'exigences jouet
surcharge "PLACE_MIN_KIO=999999999999"
joue "[p1] artefact : place libre sous le seuil → B2 arrête, rien n'est lancé" "$B/b06.sh" 1 "place libre"
[ ! -e "$DEP/.venv" ] && [ ! -e "$BACJ/installation-v2.lancee.txt" ] && bon "[p1] aucun environnement créé, aucune installation lancée" || mauvais "[p1] installation lancée malgré le seuil"
surcharge "PLACE_MIN_KIO=1000"; echo "surcharge : PLACE_MIN_KIO=1000 (jouet : l'installation jouet ne pèse rien)"
printf '%s\n' '--no-index' 'paquet-inexistant-de-la-repetition==9.9.9' > "$DEP/requirements-cpu.txt"
grep -q -F '"$1/bin/pip" install -q --disable-pip-version-check --no-cache-dir -r "$2"' "$B/b06.sh" && bon "[p1] B2 : l'installation détachée est sans cache de pip (--no-cache-dir)" || mauvais "[p1] B2 : pip avec cache"
joue "[p1] artefact (exigences jouets introuvables) : B2 lance l'installation, détachée" "$B/b06.sh" 0 "installation lancée, détachée"
s=$(attendre "$B/b06.sh" "installation en cours"); printf '%s' "$s" | grep -q "ARRÊT : installation en échec (code 1)" && bon "[p1] artefact : installation en échec → B2 arrête (fin du journal de pip affichée, rien d'effacé)" || { mauvais "[p1] installation en échec"; echo "$s" | tail -5; }
rm -rf "$DEP/.venv" "$BACJ"/installation-v2.*
mkdir -p "$DEP/.venv/bin"; ln -s "$(command -v python3)" "$DEP/.venv/bin/python"
joue "[p1] artefact : .venv déjà là avec d'autres versions, non créé par la commande → B2 arrête, rien n'est écrasé" "$B/b06.sh" 1 "existe avec d'autres versions"
rm -rf "$DEP/.venv"
date -u +%s > "$BACJ/installation-v2.lancee.txt"; echo 999999 > "$BACJ/installation-v2.pid.txt"
joue "[p1] artefact : installation lancée, processus disparu sans code → B2 arrête" "$B/b06.sh" 1 "processus disparu sans code de sortie"
rm -f "$BACJ"/installation-v2.*
printf '%s\n' '# exigences jouets : aucune bibliothèque (la répétition ne télécharge rien)' > "$DEP/requirements-cpu.txt"
joue "[p1] bloc B2 (exigences jouets vides) : installation lancée, détachée" "$B/b06.sh" 0 "installation lancée, détachée"
s=$(attendre "$B/b06.sh" "installation en cours"); printf '%s' "$s" | grep -q "installation finie (code 0)" && printf '%s' "$s" | grep -q "ARRÊT : versions autres que celles de requirements-cpu.txt" \
    && bon "[p1] artefact : installation finie mais versions autres (rien d'installé) → B2 arrête" || { mauvais "[p1] versions autres"; echo "$s" | tail -5; }
! grep -q '^PYP=' "$VAR" && bon "[p1] aucun interpréteur inscrit aux variables tant que les versions ne sont pas conformes" || mauvais "[p1] PYP inscrit trop tôt"
SP=$(ls -d "$DEP"/.venv/lib/python3*/site-packages | head -1); ls -d "$DEPOT_REEL"/.venv/lib/python3*/site-packages | head -1 > "$SP/bibliotheques-de-la-repetition.pth"
echo "simulation : les bibliothèques du .venv du dépôt réel sont rendues visibles à l'environnement créé par le bloc (fichier .pth) ; rien n'est téléchargé"
joue "[p1] bloc B2 rejoué : installation finie, versions exactes, modules gelés importables, interpréteur inscrit" "$B/b06.sh" 0 "interpréteur de la pièce : $DEP/.venv/bin/python"
printf '%s' "$DERNIERE" | grep -q "versions : 2.4.6 1.17.1 2.14.1" && printf '%s' "$DERNIERE" | grep -q "modules gelés de la pièce : importables" && grep -q "^PYP='$DEP/.venv/bin/python'" "$VAR" \
    && bon "[p1] B2 : versions 2.4.6, 1.17.1, 2.14.1 ; modules importables ; PYP inscrit une fois" || mauvais "[p1] B2 sortie"
git -C "$DEP" checkout -q -- requirements-cpu.txt
joue "[p1] bloc B2 rejoué encore (sans effet : même interpréteur)" "$B/b06.sh" 0 "interpréteur de la pièce : $DEP/.venv/bin/python"
[ "$(grep -c '^PYP=' "$VAR")" = 1 ] && bon "[p1] PYP inscrit une seule fois" || mauvais "[p1] PYP en double"
cp "$VAR" "$T/variables-p1-saines.sh"
# --- bloc B3 : entrées
surcharge "TETE_7B=0000000000000000000000000000000000000000"
joue "[p1] artefact : tête de la branche de 7b autre → B3 arrête avant tout" "$B/b07.sh" 1 "tête de $B7B autre"
cp "$T/variables-p1-saines.sh" "$VAR"; surcharge "B7B=jouet/7b-arret; TETE_7B=$T_ARR"
joue "[p1] artefact : branche de 7b avec un arret.json → B3 arrête, rien n'est placé" "$B/b07.sh" 1 "arret.json présent sur la branche de 7b"
[ ! -e "$BACJ/entrees-7b-v2" ] && bon "[p1] rien n'est placé" || mauvais "[p1] entrées placées malgré l'arrêt"
rm -rf "$BACJ/clone-7b-v2"; cp "$T/variables-p1-saines.sh" "$VAR"; surcharge "B7B=jouet/7b-compagnon-faux; TETE_7B=$T_CPF"
joue "[p1] artefact : compagnon faux sur la branche de 7b → B3 arrête" "$B/b07.sh" 1 "compagnon de diag/$R6/lecture-cout-t06.json"
rm -rf "$BACJ/clone-7b-v2" "$BACJ/entrees-7b-v2"; cp "$T/variables-p1-saines.sh" "$VAR"; surcharge "H_MANIF_7B=$Z"
joue "[p1] artefact : manifeste de 7b autre que la ligne → B3 arrête" "$B/b07.sh" 1 "manifeste de 7b autre que la ligne"
cp "$T/variables-p1-saines.sh" "$VAR"
joue "[p1] bloc B3 relancé (dépôt jetable sans contenu, liste positive, hors du dépôt)" "$B/b07.sh" 0 "entrées placées hors du dépôt : 10 fichiers"
printf '%s' "$DERNIERE" | grep -q "manifeste de 7b égal à la ligne RUN-CONFIRMATION-T06" && [ "$(printf '%s\n' "$DERNIERE" | grep -c 'déjà là, égal')" = 10 ] && bon "[p1] B3 : dix fichiers déjà là, égaux ; manifeste égal à la ligne" || mauvais "[p1] B3 reprise"
o=0; for f in runs/$R6/manifeste.json diag/$R6/episodes-t06.json diag/$R6/lecture-cout-t06.json donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl; do o=$(( o + $(stat -c %s "$T/entrees/saines/$f") )); done
printf '%s' "$DERNIERE" | grep -q -F "10 fichiers ; cinq entrées : $o octets ; aucun nom interdit" && bon "[p1] B3 : somme des tailles des cinq entrées égale à celle des entrées fabriquées ($o octets, compagnons non comptés)" || mauvais "[p1] B3 : somme des tailles"
E="$BACJ/entrees-7b-v2"
n=$(cd "$E" && find . -type f | grep -c -E 'lecture-sondes|resume\.json|distillation|activations|adaptateur'); [ "$n" = 0 ] && [ "$(git -C "$DEP" status --porcelain --untracked-files=all | wc -l)" = 0 ] \
    && bon "[p1] aucun fichier fermé factice extrait ; aucune entrée dans le dépôt (arbre propre)" || mauvais "[p1] fichier fermé extrait ou entrée dans le dépôt"
cmp -s "$E/donnees/$R6/mesures-t06.npz" "$T/entrees/saines/donnees/$R6/mesures-t06.npz" && cmp -s "$E/donnees/$R6/textes-actions-t06.jsonl" "$T/entrees/saines/donnees/$R6/textes-actions-t06.jsonl" \
    && bon "[p1] entrées extraites égales à l'octet aux entrées factices fabriquées" || mauvais "[p1] entrées extraites autres"
echo "x" >> "$E/diag/$R6/episodes-t06.json"
joue "[p1] artefact : entrée placée altérée → B3 arrête" "$B/b07.sh" 1 "existe et diffère du blob"
rm -f "$E/diag/$R6/episodes-t06.json"
joue "[p1] bloc B3 relancé (le fichier manquant est replacé)" "$B/b07.sh" 0 "entrées placées hors du dépôt : 10 fichiers"
echo "x" > "$E/diag/$R6/resume.json"
joue "[p1] artefact : nom interdit parmi les entrées → B3 arrête" "$B/b07.sh" 1 "nom(s) interdit(s) parmi les entrées"
mv "$E/diag/$R6/resume.json" "$E/diag/$R6/note-bbis.json"
joue "[p1] artefact : nom de l'étape B bis parmi les entrées → B3 arrête" "$B/b07.sh" 1 "1 nom(s) interdit(s) parmi les entrées"
mv "$E/diag/$R6/note-bbis.json" "$E/diag/$R6/de-trop.json"
joue "[p1] artefact : un fichier de trop parmi les entrées → B3 arrête" "$B/b07.sh" 1 "dix attendus"
rm -f "$E/diag/$R6/de-trop.json"
# --- bloc B4 : contrôle à blanc
echo "fichier égaré" > "$DEP/fichier-egare-jouet.txt"
joue "[p1] artefact : fichier non suivi dans le dépôt → B4 arrête (nom affiché)" "$B/b08.sh" 1 "arbre de travail non propre"
rm -f "$DEP/fichier-egare-jouet.txt"; mkdir -p "$DEP/diag/20260101-000000-mots-et-cout-t06"
joue "[p1] artefact : dossier d'un run de la pièce déjà là (vide) → B4 arrête (R12)" "$B/b08.sh" 1 "existe déjà (R12)"
rmdir "$DEP/diag/20260101-000000-mots-et-cout-t06"; rmdir "$DEP/diag" 2>/dev/null
surcharge "COMMIT_PIECE=$MAIN0"
joue "[p1] artefact : commit attendu autre que celui que cite le registre → B4 arrête" "$B/b08.sh" 1 "sortie autre qu'attendue"
cp "$T/variables-p1-saines.sh" "$VAR"; mv "$E/runs/$R6/manifeste.json.sha256" "$T/compagnon-ote.sha256"
joue "[p1] artefact : compagnon du manifeste de 7b ôté des entrées → B4 : garde de registre de la pièce, non conforme" "$B/b08.sh" 1 "NON CONFORME (ArretPiece)"
mv "$T/compagnon-ote.sha256" "$E/runs/$R6/manifeste.json.sha256"; echo "{}" > "$E/diag/$R6/arret.json"
joue "[p1] artefact : arret.json parmi les entrées → B4 non conforme" "$B/b08.sh" 1 "arret.json de 7b présent parmi les entrées"
rm -f "$E/diag/$R6/arret.json"; [ ! -e "$BACJ/blanc-conforme-v2.txt" ] && bon "[p1] aucun marqueur de contrôle à blanc conforme après ces arrêts" || mauvais "[p1] marqueur posé à tort"
joue "[p1] artefact : B5a sans contrôle à blanc conforme → arrêt, aucun appel" "$B/b09.sh" 1 "bloc B4 non conforme ou non joué"
joue "[p1] bloc B4 (verifier-code, puis les gardes de la pièce, sans rien écrire)" "$B/b08.sh" 0 "CONTRÔLE À BLANC DE LA PIÈCE : TOUT CONFORME"
printf '%s' "$DERNIERE" | grep -q "CODE-MOTS-ET-COUT-T06 conforme : commit $CPJ, 2 fichiers, tête $MAIN0" && printf '%s' "$DERNIERE" | grep -q "1. modules gelés : 9 à leurs empreintes" \
    && printf '%s' "$DERNIERE" | grep -q "journal : 2 ligne(s)" && printf '%s' "$DERNIERE" | grep -q "4. entrées : les 10 chemins" && printf '%s' "$DERNIERE" | grep -q "5. arbre de travail : propre ; commit $MAIN0" \
    && [ -z "$(git -C "$DEP" status --porcelain --untracked-files=all)" ] && bon "[p1] B4 : cinq lignes attendues ; rien d'écrit dans le dépôt" || mauvais "[p1] B4 sortie"
# --- bloc B5a et B5-attente
joue "[p1] artefact : B5-attente avant B5a → arrêt" "$B/b10.sh" 1 "B5a non joué"
joue "[p1] artefact : B5b avant la fin de la pièce → arrêt" "$B/b11.sh" 1 "pièce pas finie"
cp "$BACJ/blanc-conforme-v2.txt" "$T/blanc-sauve.txt"; echo $(( $(date -u +%s) - 4000 )) > "$BACJ/blanc-conforme-v2.txt"
joue "[p1] artefact : contrôle à blanc vieux de plus de 30 minutes → B5a arrête" "$B/b09.sh" 1 "vieux de plus de 30 minutes"
cp "$T/blanc-sauve.txt" "$BACJ/blanc-conforme-v2.txt"; echo "fichier égaré" > "$DEP/fichier-egare-jouet.txt"
joue "[p1] artefact : fichier non suivi apparu depuis B4 → B5a arrête" "$B/b09.sh" 1 "non propre depuis B4"
rm -f "$DEP/fichier-egare-jouet.txt"; [ ! -e "$BACJ/appel-piece-lance-v2.txt" ] && bon "[p1] après ces arrêts : aucun appel lancé" || mauvais "[p1] appel lancé à tort"
joue "[p1] bloc B5a (l'unique appel de la vraie pièce, détaché)" "$B/b09.sh" 0 "pièce lancée, détachée, à"
joue "[p1] bloc B5-attente aussitôt (processus vivant)" "$B/b10.sh" 0 "pièce en cours depuis"
joue "[p1] artefact : B5a relancé → arrêt, aucun second appel" "$B/b09.sh" 1 "la pièce a déjà été lancée : aucun second appel"
joue "[p1] artefact : B3 après l'appel → arrêt" "$B/b07.sh" 1 "les entrées ne se touchent plus"
joue "[p1] artefact : B4 après l'appel → arrêt" "$B/b08.sh" 1 "la pièce a déjà été lancée : joue B5-attente"
s=$(attendre "$B/b10.sh" "pièce en cours depuis"); printf '%s' "$s" | grep -q "PIÈCE FINIE : code 0 en" && bon "[p1] B5-attente : $(printf '%s' "$s" | grep -o 'PIÈCE FINIE : code 0 en [0-9]* s')" || { mauvais "[p1] attente de la pièce"; echo "$s" | tail -3; tail -3 "$BACJ/progres-piece-v2.txt" | cut -c1-300; }
RMC=$(cd "$DEP" && ls -d diag/[0-9]*-mots-et-cout-t06 2>/dev/null | head -1 | xargs -r basename); echo "run de la pièce (jouet) : $RMC"
! grep -q -E '[0-9][.,][0-9]' "$BACJ/sortie-piece-v2.txt" && [ "$(wc -l < "$BACJ/sortie-piece-v2.txt")" = 5 ] && [ "$(grep -c '^PROGRES ' "$BACJ/progres-piece-v2.txt")" = "$(wc -l < "$BACJ/progres-piece-v2.txt")" ] \
    && bon "[p1] sortie de la pièce : cinq lignes, aucun nombre décimal ; progrès : lignes d'étape seulement (ni l'une ni l'autre affichée par les blocs)" || mauvais "[p1] sortie ou progrès de la pièce"
# --- bloc B5b
echo "fichier égaré" > "$DEP/fichier-egare-jouet.txt"
joue "[p1] artefact : autre chose que les sorties dans l'arbre → B5b arrête, rien n'est commité" "$B/b11.sh" 1 "autre chose que les sorties de la pièce dans l'arbre de travail"
rm -f "$DEP/fichier-egare-jouet.txt"; echo "x" > "$DEP/diag/$RMC/de-trop.json"
joue "[p1] artefact : un fichier de trop dans le dossier du run → B5b arrête" "$B/b11.sh" 1 "noms autres que les six attendus"
rm -f "$DEP/diag/$RMC/de-trop.json"; cp "$DEP/diag/$RMC/base-a-t08.json.sha256" "$T/compagnon-sauve.sha256"; echo "$Z  base-a-t08.json" > "$DEP/diag/$RMC/base-a-t08.json.sha256"
joue "[p1] artefact : compagnon d'une sortie faux → B5b arrête" "$B/b11.sh" 1 "compagnon de diag/$RMC/base-a-t08.json"
cp "$T/compagnon-sauve.sha256" "$DEP/diag/$RMC/base-a-t08.json.sha256"; cp "$BACJ/sortie-piece-v2.txt" "$T/sortie-sauve.txt"; sed -i '3s/ [0-9a-f]\{64\}$/ '"$Z"'/' "$BACJ/sortie-piece-v2.txt"
joue "[p1] artefact : empreinte annoncée par la pièce autre que le fichier écrit → B5b arrête" "$B/b11.sh" 1 "autre que l'empreinte annoncée par la pièce"
cp "$T/sortie-sauve.txt" "$BACJ/sortie-piece-v2.txt"; mkdir -p "$DEP/runs/20260101-000000-mots-et-cout-t06"
joue "[p1] artefact : second dossier de run de la pièce → B5b arrête" "$B/b11.sh" 1 "introuvable, multiple ou incomplet"
rmdir "$DEP/runs/20260101-000000-mots-et-cout-t06"
cp "$VAR" "$T/variables-p1-saines.sh"; surcharge "SECRETS='manifeste_sha256'"
joue "[p1] artefact : garde des secrets (motif jouet présent dans les sorties) → B5b arrête après l'ajout à l'index, sans commit" "$B/b11.sh" 1 "garde des secrets"
cp "$T/variables-p1-saines.sh" "$VAR"; [ ! -e "$BACJ/c-sorties-p-v2.txt" ] && bon "[p1] après ces arrêts : aucun commit des sorties" || mauvais "[p1] commit fait à tort"
refuser_pousses "$DIST"
joue "[p1] artefact : poussée refusée → B5b s'arrête après son commit" "$B/b11.sh" 1 "poussée (relance B5b"
rm -f "$DIST/hooks/pre-receive"
joue "[p1] bloc B5b relancé seul (reprise à la poussée ; sorties égales aux empreintes annoncées)" "$B/b11.sh" 0 "B5b fait : code 0 ; 8 fichiers commités, aucun ouvert ; poussé"
LIGNES_P1=$(printf '%s\n' "$DERNIERE" | grep ' sha256 '); CS1=$(cat "$BACJ/c-sorties-p-v2.txt")
[ "$(printf '%s\n' "$LIGNES_P1" | wc -l)" = 4 ] && printf '%s' "$DERNIERE" | grep -q "les quatre fichiers écrits sont égaux aux empreintes annoncées par la pièce" && [ "$(git -C "$DIST" rev-parse "refs/heads/$BRP")" = "$CS1" ] \
    && bon "[p1] B5b : quatre lignes « chemin sha256 … blob … octets … » ; tête distante égale au commit des sorties" || mauvais "[p1] B5b rendu"
echo "ligne de bruit (artefact de la répétition)" >> "$BACJ/sortie-piece-v2.txt"
joue "[p1] artefact : une ligne de plus dans la sortie de la pièce → B5b (relancé après succès) le note, sans l'afficher ni s'arrêter" "$B/b11.sh" 0 "note : 1 ligne(s) de plus que les cinq attendues"
! printf '%s' "$DERNIERE" | grep -q "ligne de bruit" && printf '%s' "$DERNIERE" | grep -q "B5b fait : code 0 ; 8 fichiers commités" && bon "[p1] la ligne de plus n'est pas affichée ; B5b relancé après succès : même rendu, aucun second commit" || mauvais "[p1] ligne de plus"
cp "$T/sortie-sauve.txt" "$BACJ/sortie-piece-v2.txt"; [ "$(git -C "$DIST" rev-parse "refs/heads/$BRP")" = "$CS1" ] && bon "[p1] tête distante inchangée après la relance" || mauvais "[p1] tête distante changée"
# --- bloc F-B
joue "[p1] artefact : variables de tête de F-B non remplies → arrêt" "$B/b12.sh" 1 "variables de tête non remplies"
remplir_fb "$B/b12-rempli.sh"; refuser_pousses "$DIST"
joue "[p1] artefact : poussée refusée → F-B s'arrête après son commit" "$B/b12-rempli.sh" 1 "poussée (relance F-B"
rm -f "$DIST/hooks/pre-receive"
joue "[p1] bloc F-B relancé (reprise à la poussée ; journal provisoire, dépôt propre)" "$B/b12-rempli.sh" 0 "RENDU — branche $BRP"
printf '%s' "$DERNIERE" | grep -q "dépôt propre" && bon "[p1] F-B : « dépôt propre »" || mauvais "[p1] F-B dépôt"
# --- contrôles sur le dépôt distant jouet
c1=$(git -C "$DIST" rev-list --count "main..$BRP"); f=$(git -C "$DIST" diff --name-only main "$BRP")
echo "branche $BRP : $c1 commits au-dessus de main ; $(printf '%s\n' "$f" | wc -l) fichiers"
[ "$c1" = 2 ] && [ "$(printf '%s\n' "$f" | grep -c -E "^(diag|runs)/$RMC/")" = 8 ] && [ "$(printf '%s\n' "$f" | grep -c '^registres-provisoires/compte-3-phase-b-')" = 2 ] && [ "$(printf '%s\n' "$f" | wc -l)" = 10 ] \
    && bon "[p1] deux commits : les huit fichiers de sortie, puis le journal provisoire et son compagnon ; rien d'autre" || mauvais "[p1] contenu de la branche"
[ "$(printf '%s\n' "$f" | grep -c "$R6")" = 0 ] && [ "$(git -C "$DIST" ls-tree -r --name-only "$BRP" | grep -c "$R6")" = 0 ] && bon "[p1] aucune entrée de 7b sur la branche (aucun chemin du run de 7b)" || mauvais "[p1] entrée de 7b commitée"
[ "$(git -C "$DIST" rev-parse main)" = "$MAIN0" ] && bon "[p1] main du dépôt distant inchangé (rien poussé sur main)" || mauvais "[p1] main a changé"
J=$(printf '%s\n' "$f" | grep '^registres-provisoires/.*\.md$'); git -C "$DIST" show "$BRP:$J" > "$T/journal-p1.md"
grep -q "P3B-003 : appel unique lancé à 2026-" "$T/journal-p1.md" && grep -q "code 0 en" "$T/journal-p1.md" && [ "$(grep -c "^    \(diag\|runs\)/$RMC/" "$T/journal-p1.md")" = 8 ] \
    && [ "$(grep -c '^- P3B-00[1-5] : ' "$T/journal-p1.md")" = 5 ] && [ "$(wc -l < "$T/journal-p1.md")" = 17 ] \
    && bon "[p1] journal provisoire : cinq faits P3B, huit lignes de fichiers (chemin, empreinte, objet), rien d'autre (17 lignes)" || mauvais "[p1] journal provisoire"
printf '%s\n' "$J" | grep -q -E '^registres-provisoires/compte-3-phase-b-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{4}-v3\.md$' && head -1 "$T/journal-p1.md" | grep -q 'journal provisoire (v3)$' \
    && grep -q '^- P3B-001 : commande phase B v3 exécutée depuis 20' "$T/journal-p1.md" && bon "[p1] journal provisoire : nom en -v3.md, titre (v3), « commande phase B v3 exécutée »" || mauvais "[p1] journal provisoire : nom ou version"
"$PYR" -I -c 'import json, sys; m = json.load(open(sys.argv[1])); c = m["config"]; sys.exit(0 if (m["decisif"] and m["depot_propre"] and not m["reserves"] and c["racine_entrees_distincte"] and c["arbre"]["entrees_non_suivies"] == [] and m["commit"] == sys.argv[2] and c["code"]["commit"] == sys.argv[3] and c["mode"] == "reel") else 1)' \
    "$DEP/runs/$RMC/manifeste.json" "$MAIN0" "$CPJ" && bon "[p1] manifeste de la pièce (jouet, lu par la répétition seule) : décisif, dépôt propre, aucune réserve, racine d'entrées distincte, commit = base, code = commit cité" || mauvais "[p1] manifeste de la pièce"
# --- la mère : bloc V, lignes, bloc M de la phase C v3, reprise du fichier d'issue
MERE="$T/mere"; git clone -q "$DIST" "$MERE"; DEP_SAUVE="$DEP"; DEP="$MERE"; export HOME="$T/home-mere"; mkdir -p "$HOME"
joue "[mère] artefact : variables de tête du bloc V non remplies → arrêt" "$B/b13.sh" 1 "variables de tête non remplies"
remplir_v "$B/b13-faux-1.sh" "$CPJ" "$CS1" "$LIGNES_P1" "$BRP"
joue "[mère] artefact : base rendue autre que le parent du commit des sorties → bloc V arrête" "$B/b13-faux-1.sh" 1 "n'a pas la base rendue pour parent"
remplir_v "$B/b13-faux-2.sh" "$MAIN0" "$CS1" "$(printf '%s\n' "$LIGNES_P1" | sed '1s/sha256 [0-9a-f]\{8\}/sha256 00000000/')" "$BRP"
joue "[mère] artefact : une empreinte du rendu autre → bloc V arrête" "$B/b13-faux-2.sh" 1 "autres que le rendu de l'hôte"
remplir_v "$B/b13-p1.sh" "$MAIN0" "$CS1" "$(printf '%s\n' "$LIGNES_P1" | sed 's/^/   /')" "$BRP"
joue "[mère] bloc V (sorties vérifiées par objets git et empreintes, sans être ouvertes ; rendu collé avec des blancs)" "$B/b13-p1.sh" 0 "BLOC V : run $RMC ; 8 fichiers, égaux à leurs compagnons et au rendu de l'hôte"
[ -z "$(git -C "$MERE" status --porcelain --untracked-files=all)" ] && [ "$(git -C "$MERE" rev-parse --abbrev-ref HEAD)" = main ] && bon "[mère] bloc V : copie de travail de la mère inchangée (aucune sortie extraite)" || mauvais "[mère] copie de travail"
HB=$(printf '%s\n' "$LIGNES_P1" | grep '/base-a-t08.json ' | cut -d' ' -f3); HI=$(printf '%s\n' "$LIGNES_P1" | grep '/issue-mots-et-cout-t06.json ' | cut -d' ' -f3)
(cd "$MERE" && PYTHONPATH="$MERE/src" "$PYR" -P -B -c '
import sys, time
from pathlib import Path
from controle_ia.t07 import registre_v1 as rg
reg, run, hb, hi = Path("registres/scellements-v1.md"), sys.argv[1], sys.argv[2], sys.argv[3]
t = int(time.time()) - 10
rg.ajouter_ligne(reg, "LECTURE-T08-BASE-A", t, f"diag/{run}/base-a-t08.json", hb)
rg.ajouter_ligne(reg, "ISSUE-MOTS-ET-COUT-T06", t + 1, f"diag/{run}/issue-mots-et-cout-t06.json", hi)' "$RMC" "$HB" "$HI") \
    && [ "$(grep -c -E '^\| (LECTURE-T08-BASE-A|ISSUE-MOTS-ET-COUT-T06) \|' "$MERE/registres/scellements-v1.md")" = 2 ] \
    && [ "$(grep -n -E '^\| (LECTURE-T08-BASE-A|ISSUE-MOTS-ET-COUT-T06) \|' "$MERE/registres/scellements-v1.md" | head -1 | grep -c LECTURE)" = 1 ] \
    && bon "[mère] lignes LECTURE-T08-BASE-A puis ISSUE-MOTS-ET-COUT-T06 inscrites par registre_v1.ajouter_ligne, dans cet ordre" || mauvais "[mère] lignes"
git -C "$MERE" add -A >/dev/null; git -C "$MERE" commit -q -m "lignes de la mère (jouet)"; git -C "$MERE" push -q origin main 2>/dev/null
sed -e "s#BRP='<branche qui porte base-a-t08.json>'#BRP='$BRP'#" -e "s#https://github.com/lciric/controle-ia-travail.git#file://$DIST#" "$B/bloc-m-phase-c-v3.sh" > "$B/bloc-m-rempli.sh"
s=$(cd "$MERE" && bash "$B/bloc-m-rempli.sh" 2>&1); e=$(printf '%s\n' "$s" | grep '^ÉTAT BA-L2 : ' | sed 's/ — .*//')
case "$e" in "ÉTAT BA-L2 : ne s'applique pas"|"ÉTAT BA-L2 : s'applique") bon "[mère] bloc M de la phase C v3 rejoué sur la branche jouet de la pièce : « $e » (entrées factices), lu dans une vraie sortie de la pièce";;
    *) mauvais "[mère] bloc M"; printf '%s\n' "$s" | tail -5;; esac
[ "$(printf '%s\n' "$s" | grep -v -c -E '^(20[0-9-]+T[0-9:]+Z|ÉTAT BA-L2 : .*|code [03])$')" = 0 ] && bon "[mère] bloc M : rien d'autre affiché que l'heure, l'état et le code" || { mauvais "[mère] bloc M affiche autre chose"; printf '%s\n' "$s" | cut -c1-200; }
IS=$(grep '^| ISSUE-MOTS-ET-COUT-T06 |' "$MERE/registres/scellements-v1.md" | cut -d'|' -f4 | tr -d ' ')
git -C "$MERE" fetch --no-tags -q origin "+refs/heads/$BRP:refs/remotes/origin/$BRP"
[ "$(git -C "$MERE" show "refs/remotes/origin/$BRP:$IS" | sha256sum | cut -d' ' -f1)" = "$HI" ] && [ "$(git -C "$MERE" show "refs/remotes/origin/$BRP:$IS.sha256" | cut -d' ' -f1)" = "$HI" ] \
    && bon "[phase C] le fichier d'issue cité par la ligne se reprend sur la branche de la pièce, égal à la ligne et à son compagnon (geste du bloc C2)" || mauvais "[phase C] reprise du fichier d'issue"
DEP="$DEP_SAUVE"
# --- la pièce refuse une relance une fois les lignes inscrites (garde de la pièce elle-même, R12)
export HOME="$T/s-p1/home"
git -C "$DEP" fetch --no-tags -q origin +refs/heads/main:refs/remotes/origin/main; git -C "$DEP" switch -q --detach refs/remotes/origin/main
s=$(cd "$DEP" && PY="$DEP/.venv/bin/python" bash scripts/lancer_mots_et_cout_t06_v3.sh --mode reel --racine-entrees "$E" "$R6" 2>&1 >/dev/null); c=$?
[ "$c" = 2 ] && printf '%s' "$s" | grep -q "déjà inscrite : la pièce a déjà tourné" && [ -z "$(git -C "$DEP" status --porcelain --untracked-files=all)" ] \
    && bon "[garde de la pièce] après les lignes de la mère, une relance est refusée (code 2, rien d'écrit)" || mauvais "[garde de la pièce] relance après les lignes (code $c)"
git -C "$DIST" update-ref refs/heads/main "$MAIN0"   # main jouet remis à son état d'avant les lignes de la mère, pour les passes suivantes

# ============================================================== passe 2 : clone superficiel, environnement déjà prêt, code 2 (refus à la lecture des entrées)
BR2=$BRP-passe-2
session p2 superficiel venv
[ "$(git -C "$DEP" rev-parse --is-shallow-repository)" = true ] && ! git -C "$DEP" cat-file -e "$CPJ^{commit}" 2>/dev/null && bon "[p2] clone superficiel : le commit de la pièce n'y est pas" || mauvais "[p2] clone jouet non superficiel"
joue "[p2] bloc 0b-B" "$B/b02.sh" 0 "(sur main distant)"
joue "[p2] bloc 1B" "$B/b03.sh" 0 "session : session_$HOTE"
surcharges_jouet; surcharge "COMMIT_PIECE=$CPJ; BR_P=$BR2; B7B=jouet/7b-effectifs; TETE_7B=$T_EFF"; echo "surcharge : BR_P=$BR2 ; B7B=jouet/7b-effectifs (dix actions de moins, empreintes d'accord)"
joue "[p2] bloc 2B" "$B/b04.sh" 0 "contrôles d'entrée conformes"
joue "[p2] bloc B1 (clone superficiel approfondi par refspec, puis branche et poussée)" "$B/b05.sh" 0 "clone superficiel : historique de main approfondi"
printf '%s' "$DERNIERE" | grep -q "branche $BR2 poussée" && [ "$(git -C "$DEP" rev-parse --is-shallow-repository)" = false ] && git -C "$DEP" merge-base --is-ancestor "$CPJ" HEAD \
    && bon "[p2] B1 : dépôt complet, commit de la pièce ancêtre de la tête, branche poussée" || mauvais "[p2] B1 approfondissement"
joue "[p2] bloc B2 (environnement déjà prêt : aucune installation)" "$B/b06.sh" 0 "environnement déjà prêt"
[ ! -e "$BACJ/installation-v2.lancee.txt" ] && printf '%s' "$DERNIERE" | grep -q "interpréteur de la pièce" && bon "[p2] B2 : rien lancé ; interpréteur inscrit" || mauvais "[p2] B2"
joue "[p2] bloc B3" "$B/b07.sh" 0 "entrées placées hors du dépôt : 10 fichiers"
joue "[p2] bloc B4 (tout conforme : le contrôle à blanc ne lit pas le contenu des entrées)" "$B/b08.sh" 0 "CONTRÔLE À BLANC DE LA PIÈCE : TOUT CONFORME"
joue "[p2] bloc B5a" "$B/b09.sh" 0 "pièce lancée, détachée, à"
s=$(attendre "$B/b10.sh" "pièce en cours depuis"); printf '%s' "$s" | grep -q "PIÈCE FINIE : code 2 en" && bon "[p2] B5-attente : $(printf '%s' "$s" | grep -o 'PIÈCE FINIE : code 2 en [0-9]* s')" || { mauvais "[p2] attente"; echo "$s" | tail -3; }
joue "[p2] bloc B5b (code 2 : rien d'écrit, ligne de refus affichée, rien de commité)" "$B/b11.sh" 0 "B5b fait : code 2 ; rien à commiter"
printf '%s' "$DERNIERE" | grep -q "dernière étape : entrées" && printf '%s' "$DERNIERE" | grep -q "^REFUS (rien n'est écrit) : mesures-t06.npz : 5750 actions, 5760 attendues" && [ -z "$(git -C "$DEP" status --porcelain --untracked-files=all)" ] \
    && bon "[p2] B5b : étape « entrées », ligne de refus de la pièce (un effectif, aucune aire), dépôt propre" || mauvais "[p2] B5b code 2"
joue "[p2] bloc B5b relancé (même issue)" "$B/b11.sh" 0 "B5b fait : code 2 ; rien à commiter"
remplir_fb "$B/b12-rempli.sh"
joue "[p2] bloc F-B (journal provisoire d'un refus)" "$B/b12-rempli.sh" 0 "RENDU — branche $BR2"
f=$(git -C "$DIST" diff --name-only main "$BR2"); J=$(printf '%s\n' "$f" | grep '^registres-provisoires/.*\.md$'); git -C "$DIST" show "$BR2:$J" > "$T/journal-p2.md"
[ "$(git -C "$DIST" rev-list --count "main..$BR2")" = 1 ] && [ "$(printf '%s\n' "$f" | wc -l)" = 2 ] && grep -q "code 2 en" "$T/journal-p2.md" && grep -q "aucun ; sortie de la pièce" "$T/journal-p2.md" && ! grep -q "5750" "$T/journal-p2.md" \
    && bon "[p2] branche : le seul journal provisoire ; il dit le code 2 et les empreintes des fichiers du bac, pas la ligne de refus" || mauvais "[p2] journal du refus"
# états fabriqués à la main dans le bac de la passe 2 (la pièce a fini) : gardes de B5b et de B5-attente
cp -r "$BACJ" "$T/bac-p2-sauve"
echo 7 > "$BACJ/code-piece-v2.txt"
joue "[p2] artefact : code de sortie inattendu → B5b arrête, rien n'est commité" "$B/b11.sh" 1 "code inattendu 7"
echo 2 > "$BACJ/code-piece-v2.txt"; mkdir -p "$DEP/runs/20260101-000000-mots-et-cout-t06"
joue "[p2] artefact : code 2 avec un dossier de run écrit → B5b arrête" "$B/b11.sh" 1 "code 2 avec des fichiers écrits"
rmdir "$DEP/runs/20260101-000000-mots-et-cout-t06"; rmdir "$DEP/runs" 2>/dev/null
rm -f "$BACJ/code-piece-v2.txt"; echo 999999 > "$BACJ/pid-piece-v2.txt"
joue "[p2] artefact : processus disparu sans code de sortie → B5-attente arrête, rien n'est relancé" "$B/b10.sh" 1 "ARRÊT : processus disparu sans code de sortie"
echo $$ > "$BACJ/pid-piece-v2.txt"; echo $(( $(date -u +%s) - 4000 )) > "$BACJ/appel-piece-lance-v2.txt"
joue "[p2] artefact : pièce encore en marche au-delà de la borne → B5-attente le dit, sans rien arrêter" "$B/b10.sh" 0 "BORNE DÉPASSÉE (3600 s)"
joue "[p2] artefact : F-B alors que la pièce n'a pas fini → arrêt" "$B/b12-rempli.sh" 1 "n'a pas été appelée, ou n'a pas fini"
rm -rf "$BACJ"; cp -r "$T/bac-p2-sauve" "$BACJ"

# ============================================================== passe 3 : code 3 (arrêt après le manifeste), bloc V sur quatre fichiers
BR3=$BRP-passe-3
session p3 complet venv
joue "[p3] bloc 0b-B" "$B/b02.sh" 0 "(sur main distant)"
joue "[p3] bloc 1B" "$B/b03.sh" 0 "session : session_$HOTE"
surcharges_jouet; surcharge "BR_P=$BR3; B7B=jouet/7b-jetons; TETE_7B=$T_JET"; echo "surcharge : BR_P=$BR3 ; B7B=jouet/7b-jetons (un nombre de jetons négatif, empreintes d'accord)"
joue "[p3] bloc 2B" "$B/b04.sh" 0 "contrôles d'entrée conformes"
joue "[p3] bloc B1" "$B/b05.sh" 0 "branche $BR3 poussée (égale à main"
joue "[p3] bloc B2" "$B/b06.sh" 0 "interpréteur de la pièce"
joue "[p3] bloc B3" "$B/b07.sh" 0 "entrées placées hors du dépôt : 10 fichiers"
joue "[p3] bloc B4" "$B/b08.sh" 0 "CONTRÔLE À BLANC DE LA PIÈCE : TOUT CONFORME"
joue "[p3] bloc B5a" "$B/b09.sh" 0 "pièce lancée, détachée, à"
s=$(attendre "$B/b10.sh" "pièce en cours depuis"); printf '%s' "$s" | grep -q "PIÈCE FINIE : code 3 en" && bon "[p3] B5-attente : $(printf '%s' "$s" | grep -o 'PIÈCE FINIE : code 3 en [0-9]* s')" || { mauvais "[p3] attente"; echo "$s" | tail -3; }
joue "[p3] bloc B5b (code 3 : fichier d'arrêt et manifeste commités, poussés ; motif non affiché)" "$B/b11.sh" 0 "B5b fait : code 3 ; 4 fichiers commités, aucun ouvert ; poussé"
LIGNES_P3=$(printf '%s\n' "$DERNIERE" | grep ' sha256 '); CS3=$(cat "$BACJ/c-sorties-p-v2.txt"); RMC3=$(cd "$DEP" && ls -d diag/[0-9]*-mots-et-cout-t06 | head -1 | xargs -r basename)
! printf '%s' "$DERNIERE" | grep -q -i 'math domain\|ValueError\|ARRÊT (après' && [ "$(printf '%s\n' "$LIGNES_P3" | wc -l)" = 2 ] && printf '%s\n' "$LIGNES_P3" | grep -q "diag/$RMC3/arret-mots-et-cout-t06.json sha256" \
    && bon "[p3] B5b : deux lignes (fichier d'arrêt, manifeste) ; le motif de l'arrêt n'est pas affiché" || mauvais "[p3] B5b code 3"
remplir_fb "$B/b12-rempli.sh"
joue "[p3] bloc F-B" "$B/b12-rempli.sh" 0 "RENDU — branche $BR3"
f=$(git -C "$DIST" diff --name-only main "$BR3")
[ "$(git -C "$DIST" rev-list --count "main..$BR3")" = 2 ] && [ "$(printf '%s\n' "$f" | grep -c -E "^(diag/$RMC3/arret-mots-et-cout-t06\.json|runs/$RMC3/manifeste\.json)(\.sha256)?$")" = 4 ] && [ "$(printf '%s\n' "$f" | wc -l)" = 6 ] \
    && bon "[p3] branche : fichier d'arrêt, manifeste, leurs compagnons, puis le journal provisoire ; rien d'autre" || mauvais "[p3] contenu de la branche"
DEP_SAUVE="$DEP"; DEP="$MERE"; export HOME="$T/home-mere"
remplir_v "$B/b13-p3.sh" "$MAIN0" "$CS3" "$LIGNES_P3" "$BR3"
joue "[mère] bloc V sur la tentative arrêtée (code 3 : quatre fichiers ; aucune ligne à inscrire)" "$B/b13-p3.sh" 0 "BLOC V : run $RMC3 ; 4 fichiers"
DEP="$DEP_SAUVE"

# ============================================================== artefacts qui demandent une session ou un dépôt distant à part
# --- bloc 1B
session x1 complet venv
unset CLAUDE_CODE_REMOTE_SESSION_ID
joue "[x1] artefact : identifiant de session introuvable → 1B arrête" "$B/b03.sh" 1 "identifiant de session introuvable"
export CLAUDE_CODE_REMOTE_SESSION_ID=cse_01AUTREsessionJOUET000000
joue "[x1] artefact : session autre que l'hôte de la phase A → 1B arrête" "$B/b03.sh" 1 "n'est pas la session hôte de la phase A"
export CLAUDE_CODE_REMOTE_SESSION_ID="cse_$HOTE"; mkdir -p "$DEP/maison-dans-le-depot"; HOME_SAUVE="$HOME"; export HOME="$DEP/maison-dans-le-depot"
joue "[x1] artefact : dossier personnel dans un arbre git → 1B arrête" "$B/b03.sh" 1 "est dans un arbre git"
export HOME="$HOME_SAUVE"; rmdir "$DEP/maison-dans-le-depot"
[ ! -e "$BACJ" ] && bon "[x1] après ces arrêts : aucun bac créé" || mauvais "[x1] bac créé à tort"
git clone -q --bare "$DIST" "$T/distant-autre.git"; git clone -q "$T/distant-autre.git" "$T/s-x1/depot-autre"; DEP_SAUVE="$DEP"; DEP="$T/s-x1/depot-autre"
joue "[x1] artefact : dépôt d'origine autre → 1B arrête" "$B/b03.sh" 1 "le dépôt d'origine n'est pas lciric/controle-ia-travail"
DEP="$DEP_SAUVE"
# --- bloc B1 : branche déjà au distant ; ligne LECTURE-T08-BASE-A déjà inscrite (dépôt distant variante)
BRX=$BRP-deja-la
joue "[x1] bloc 1B" "$B/b03.sh" 0 "session : session_$HOTE"
surcharges_jouet; surcharge "BR_P=$BRX"; git -C "$DIST" update-ref "refs/heads/$BRX" "$CPJ"
joue "[x1] artefact : la branche de la pièce existe déjà au distant → B1 arrête (R12), aucune branche locale" "$B/b05.sh" 1 "existe déjà au distant (R12)"
[ "$(git -C "$DEP" rev-parse --abbrev-ref HEAD)" = main ] && bon "[x1] aucune branche locale créée" || mauvais "[x1] branche locale créée"
variante() {   # $1 nom ; $2 geste joué dans un clone de travail de main, puis commité et poussé sur le main de la variante
    local d="$T/distant-$1/lciric/controle-ia-travail.git" w="$T/travail-$1" r; mkdir -p "$(dirname "$d")"; git clone -q --bare "$DIST" "$d"
    for r in $(git -C "$d" for-each-ref --format='%(refname)' 'refs/heads/verdict/'); do git -C "$d" update-ref -d "$r"; done   # la variante n'a pas les branches des passes
    git -C "$d" config uploadpack.allowFilter true; git -C "$d" config uploadpack.allowAnySHA1InWant true
    git clone -q "$d" "$w"; (cd "$w" && eval "$2"); git -C "$w" add -A >/dev/null; git -C "$w" commit -q -m "variante $1"; git -C "$w" push -q origin main 2>/dev/null; rm -rf "$w"; }
jusqua_b1() { joue "[$1] blocs 0b-B, 1B, 2B (variante)" "$B/b02.sh" 0 "(sur main distant)"; (cd "$DEP" && bash "$B/b03.sh" >/dev/null 2>&1); surcharges_jouet; (cd "$DEP" && bash "$B/b04.sh" >/dev/null 2>&1); }
variante sans-commande "git rm -q $ICI_REL/commande-compte-3-phase-b-v3.md"
session x0 complet venv "$T/distant-sans-commande/lciric/controle-ia-travail.git"
joue "[x0] artefact : commande absente de main distant → 0b-B arrête" "$B/b02.sh" 1 "la commande n'est pas sur main"
variante lecture "printf '%s\n' '| LECTURE-T08-BASE-A | 2026-11-15T00:00:00Z | diag/20261115-000000-mots-et-cout-t06/base-a-t08.json | $Z |' >> registres/scellements-v1.md"
session x2 complet venv "$T/distant-lecture/lciric/controle-ia-travail.git"; jusqua_b1 x2
joue "[x2] artefact : ligne LECTURE-T08-BASE-A déjà inscrite sur main → B1 arrête avant la poussée (la pièce a déjà tourné)" "$B/b05.sh" 1 "ligne LECTURE-T08-BASE-A déjà inscrite"
[ -z "$(git -C "$DISTS" for-each-ref "refs/heads/$BRP")" ] && bon "[x2] rien poussé" || mauvais "[x2] poussé à tort"
variante lancement "echo x >> docs/programme-controle-ia-v2.md"
session x3 complet venv "$T/distant-lancement/lciric/controle-ia-travail.git"; jusqua_b1 x3
joue "[x3] artefact : document de lancement altéré sur main → B1 arrête avant la poussée" "$B/b05.sh" 1 "ARRÊT : empreintes de lancement"
# --- bloc B4 : gardes de la pièce jouées par le contrôle à blanc (journal, module gelé), sur des dépôts distants variantes
variante journal "printf '%s\n' '| OUVERTURE-T07 | 2026-11-15T00:00:00Z | etape-B/jouet/jouet | $Z |' >> registres/scellements-v1.md.ouvertures.md"
session x4 complet venv "$T/distant-journal/lciric/controle-ia-travail.git"; jusqua_b1 x4
joue "[x4] blocs B1 à B3 (variante : une ouverture de l'étape B au journal)" "$B/b05.sh" 0 "poussée (égale à main"
(cd "$DEP" && bash "$B/b06.sh" >/dev/null 2>&1; bash "$B/b07.sh" >/dev/null 2>&1)
joue "[x4] artefact : étape B de T0.7 déjà ouverte au journal → B4 non conforme (garde de la pièce), aucun appel" "$B/b08.sh" 1 "étape B de T0.7 déjà ouverte"
variante gele "echo '# ligne de trop (artefact de la répétition)' >> src/controle_ia/gardes.py"
session x5 complet venv "$T/distant-gele/lciric/controle-ia-travail.git"; jusqua_b1 x5
joue "[x5] blocs B1 à B3 (variante : un module gelé modifié sur main)" "$B/b05.sh" 0 "poussée (égale à main"
(cd "$DEP" && bash "$B/b06.sh" >/dev/null 2>&1; bash "$B/b07.sh" >/dev/null 2>&1)
joue "[x5] artefact : module gelé modifié → B4 non conforme (garde de la pièce), aucun appel" "$B/b08.sh" 1 "module gelé modifié ou absent"
joue "[x5] artefact : B5a après un contrôle à blanc non conforme → arrêt, aucun appel" "$B/b09.sh" 1 "bloc B4 non conforme ou non joué"

export HOME="$HOME_REEL"
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "RÉPÉTITION DE LA PHASE B : TOUT CONFORME" || echo "RÉPÉTITION DE LA PHASE B : ÉCARTS"
date -u +"fin de la répétition : %Y-%m-%dT%H:%M:%SZ"
