#!/usr/bin/env bash
# Répétition de bout en bout, sur dépôts jouets, des blocs de commande-compte-3-phase-a-v2.md (constat CL3-07, phase A ; CL3-15).
# Écrite le 2026-11-14 par le préparateur (modèle A). Aucune donnée réelle : dépôt distant jouet (main jouet et branche de 7b
# jouet, fichiers factices aux chemins réels, fichiers fermés factices compris pour vérifier qu'ils ne sont jamais extraits),
# HOME jouet, identifiant de session jouet ; lecteur simulé. Surcharges, et seulement elles, ajoutées en fin de variables-v2.sh
# après le bloc 1 : DEPOT_URL, TETE_7B, H_MANIF_7B, LIGNE_RUN6 (les empreintes des fichiers factices) ; marqueurs du bloc 1
# remplis (liste et consigne jouets) ; variables de tête du bloc F-A remplies. N'écrit rien hors du bac donné.
#     bash repetition_phase_a_jouet_v2.sh <dépôt réel> <bac neuf>
set -u
DEPOT_REEL=$(cd "$1" && pwd); T="$2"
[ ! -e "$T" ] || { echo "ARRÊT : $T existe déjà"; exit 1; }
mkdir -p "$T"; T=$(cd "$T" && pwd)
export LC_ALL=C.UTF-8 GIT_AUTHOR_NAME=jouet GIT_AUTHOR_EMAIL=jouet@exemple.invalid GIT_COMMITTER_NAME=jouet GIT_COMMITTER_EMAIL=jouet@exemple.invalid
ICI_REEL="$DEPOT_REEL/docs/procedures/lecture-7b-etape-b-compte-3-v1"; CMD="$ICI_REEL/commande-compte-3-phase-a-v2.md"
R6=20261111-151701-t06-reel; TR6=t06-20261112-051655-1Xzh; TRC6=consignation-20261112-051705-vUfJ
date -u +"début de la répétition : %Y-%m-%dT%H:%M:%SZ"
mkdir -p "$T/blocs"
python3 -I - "$CMD" "$T/blocs" <<'FIN'
import hashlib, pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"); b = re.findall(r"```bash\n(.*?)```", t, re.S)
for i, x in enumerate(b):
    pathlib.Path(sys.argv[2], f"b{i:02d}.sh").write_text(x, encoding="utf-8")
print(f"commande : {hashlib.sha256(t.encode()).hexdigest()} ; {len(b)} blocs ; blocs mis bout à bout : {hashlib.sha256(''.join(b).encode()).hexdigest()}")
FIN
DIST="$T/distant/lciric/controle-ia-travail.git"; mkdir -p "$(dirname "$DIST")"
git init -q --bare "$DIST"; git -C "$DIST" symbolic-ref HEAD refs/heads/main; git -C "$DIST" config uploadpack.allowFilter true; git -C "$DIST" config uploadpack.allowAnySHA1InWant true
W="$T/travail"; git init -q -b main "$W"
pose() { mkdir -p "$W/$(dirname "$1")"; printf '%s' "$2" > "$W/$1"; (cd "$W/$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256"); }
copie() { mkdir -p "$W/$(dirname "$1")"; cp "$DEPOT_REEL/$1" "$W/$1"; [ -e "$DEPOT_REEL/$1.sha256" ] && cp "$DEPOT_REEL/$1.sha256" "$W/$1.sha256"; true; }
# --- main jouet
for f in docs/sha256sums-lancement-v2.txt docs/brief-claude-code-programme-complet-v2.md docs/programme-controle-ia-v2.md docs/etat-de-l-art-controle-ia-v1.md \
         prereg/T0.6-organismes-v0-v1.md prereg/T0.6-organismes-config-7b-v1.json .gitignore \
         docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-a-v2.md docs/procedures/lecture-7b-etape-b-compte-3-v1/attestation_qui_a_lu_quoi_compte_3_v2.py; do copie "$f"; done
(cd "$DEPOT_REEL" && git ls-files -z src/controle_ia | xargs -0 -I{} cp --parents {} "$W/")
pose docs/procedures/jouet/consigne-lecteur-table-a-jouet-v1.md "# consigne jouet du lecteur A"
printf '%s\n' "# Liste « qui a lu quoi » jouet" "" "| n° | session | compte | modèle | a lu | rôle | source | exclu de |" "|---|---|---|---|---|---|---|---|" \
    "| 1 | session non nommée (compte 3) | compte 3 | non déclaré | rien | lot prévu | jouet | aucune exclusion déclarée |" \
    "| 2 | session_01LOTJOUETcompte3XXXXXX (lot du compte 3) | compte 3 | modèle A | texte scellé de T0.7 | lot NARCBench | jouet | lecteur de P3-bis |" > "$W/registres-jouet-liste.md"
mkdir -p "$W/registres"; mv "$W/registres-jouet-liste.md" "$W/registres/qui-a-lu-quoi-v2.md"; (cd "$W/registres" && sha256sum qui-a-lu-quoi-v2.md > qui-a-lu-quoi-v2.md.sha256)
# --- branche de 7b jouet (fichiers factices aux chemins réels ; fichiers fermés factices compris)
git -C "$W" add -A >/dev/null; git -C "$W" commit -q -m "main jouet (provisoire)"
git -C "$W" switch -q --orphan calcul/t06-confirmation-7b-v1; git -C "$W" rm -rq . >/dev/null 2>&1; rm -rf "$W/docs" "$W/prereg" "$W/src" "$W/registres"
for f in diag/$R6/lecture-cout-t06.json diag/$R6/episodes-t06.json diag/$R6/distillation-t06.json runs/$R6/manifeste.json \
         donnees/$R6/mesures-t06.npz donnees/$R6/textes-actions-t06.jsonl diag/$R6/lecture-sondes-t06.json diag/$R6/resume.json \
         donnees/$R6/activations-sous-ensemble-t06-000.npz donnees/$R6/adaptateur-saboteur.pt; do pose "$f" "jouet $f"; done
mkdir -p "$W/traces/$TR6" "$W/traces/$TRC6"
for g in journal.txt nvidia-smi.txt pip-freeze.txt progres-retenues.txt run.err run.json t06-minuterie.log tests.err tests.txt; do printf 'jouet %s\n' "$g" > "$W/traces/$TR6/$g"; done
for g in journal-consignation.txt t06-minuterie-fin.txt; do printf 'jouet %s\n' "$g" > "$W/traces/$TRC6/$g"; done
(cd "$W/traces/$TR6" && sha256sum journal.txt nvidia-smi.txt pip-freeze.txt progres-retenues.txt run.err run.json t06-minuterie.log tests.err tests.txt > empreintes.sha256)
(cd "$W/traces/$TRC6" && sha256sum journal-consignation.txt t06-minuterie-fin.txt > empreintes.sha256)
git -C "$W" add -A >/dev/null; git -C "$W" commit -q -m "7b jouet"; git -C "$W" push -q "$DIST" calcul/t06-confirmation-7b-v1 2>/dev/null
TETE=$(git -C "$W" rev-parse HEAD); HM=$(git -C "$W" show "HEAD:runs/$R6/manifeste.json" | sha256sum | cut -d' ' -f1)
LIGNE="| RUN-CONFIRMATION-T06 | 2026-11-13T18:52:43Z | runs/$R6/manifeste.json | $HM |"
# --- main jouet définitif : registre avec la ligne jouet RUN-CONFIRMATION-T06 et la ligne réelle VERDICT-P3BIS (texte seul)
git -C "$W" switch -q main
printf '%s\n' "# Registre jouet" "" "$LIGNE" "| VERDICT-P3BIS | 2026-11-14T10:30:38Z | docs/verdicts/verdict-P3-bis-v1-issue.json | c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0 |" > "$W/registres/scellements-v1.md"
git -C "$W" add -A >/dev/null; git -C "$W" commit -q -m "main jouet"; git -C "$W" push -q "$DIST" main 2>/dev/null
HL=$(sha256sum "$W/registres/qui-a-lu-quoi-v2.md" | cut -d' ' -f1); HC=$(sha256sum "$W/docs/procedures/jouet/consigne-lecteur-table-a-jouet-v1.md" | cut -d' ' -f1)
MAIN0=$(git -C "$DIST" rev-parse main)
# --- dépôt de la session jouet
DEP="$T/depot"; git clone -q "$DIST" "$DEP"; ln -s "$DEPOT_REEL/.venv" "$DEP/.venv"; git -C "$DEP" config user.name jouet; git -C "$DEP" config user.email jouet@exemple.invalid
H="$T/home"; mkdir -p "$H"; export HOME="$H" CLAUDE_CODE_REMOTE_SESSION_ID=cse_01JOUETcompte3HOTE000000
VAR="$H/bac-lecture-7b-compte-3-v2/variables-v2.sh"
OK=0; KO=0
joue() {   # $1 nom ; $2 bloc ; $3 code attendu ; $4 motif attendu
    local s c; s=$(cd "$DEP" && bash "$2" 2>&1); c=$?
    printf '%s\n' "$s" > "$T/sortie-$(basename "$2" .sh)-$OK-$KO.txt"
    if [ "$c" = "$3" ] && printf '%s' "$s" | grep -qF -- "$4"; then OK=$((OK+1)); echo "conforme : $1 (code $c)"
    else KO=$((KO+1)); echo "ÉCART : $1 (code $c, attendu $3 ; motif « $4 »)"; printf '%s\n' "$s" | tail -12 | sed 's/^/    /'; fi; }
B="$T/blocs"
joue "bloc 0 (noms des clés, place)" "$B/b01.sh" 0 "GH_TOKEN :"
joue "bloc 0b (main local à jour, empreinte de la commande)" "$B/b02.sh" 0 "commande-compte-3-phase-a-v2.md"
sed -e "s#<<LISTE>>#registres/qui-a-lu-quoi-v2.md#" -e "s#<<EMPREINTE_LISTE>>#$HL#" -e "s#<<CONSIGNE_LECTEUR_A>>#docs/procedures/jouet/consigne-lecteur-table-a-jouet-v1.md#" \
    -e "s#<<EMPREINTE_CONSIGNE_LECTEUR_A>>#$HC#" "$B/b03.sh" > "$B/b03-rempli.sh"
joue "bloc 1 (variables)" "$B/b03-rempli.sh" 0 "session : session_01JOUETcompte3HOTE000000"
printf '%s\n' "DEPOT_URL='file://$DIST'; TETE_7B=$TETE; H_MANIF_7B=$HM" "LIGNE_RUN6='$LIGNE'" >> "$VAR"
# artefact : attestation avec une liste qui nomme la session hôte
cp "$DEP/registres/qui-a-lu-quoi-v2.md" "$T/liste-artefact.md"; echo "| 3 | session_01JOUETcompte3HOTE000000 | compte 3 | modèle A | essai | essai | essai | aucune exclusion déclarée |" >> "$T/liste-artefact.md"
(cd "$T" && sha256sum liste-artefact.md > liste-artefact.md.sha256)
cp "$VAR" "$T/variables-sauve.sh"; printf '%s\n' "LISTE='../liste-artefact.md'; EMPREINTE_LISTE=$(sha256sum "$T/liste-artefact.md" | cut -d' ' -f1)" >> "$VAR"
joue "artefact X1 : la liste nomme la session hôte → bloc 2 arrête" "$B/b04.sh" 1 "attestation « qui a lu quoi » non conforme"
cp "$T/variables-sauve.sh" "$VAR"
joue "bloc 2 (horloge, empreintes, attestation, session neuve)" "$B/b04.sh" 0 "session neuve : aucune trace locale du lot du compte 3"
joue "bloc A1 (branche, lignes, pièces, poussée éprouvée)" "$B/b05.sh" 0 "branche poussée (égale à main)"
cp "$VAR" "$T/variables-sauve.sh"; echo "TETE_7B=0000000000000000000000000000000000000000" >> "$VAR"
joue "artefact X2 : tête de la branche de 7b autre → bloc A2 arrête avant tout" "$B/b06.sh" 1 "tête de calcul/t06-confirmation-7b-v1 autre"
cp "$T/variables-sauve.sh" "$VAR"
joue "bloc A2 (dépôt jetable, liste positive, 11 traces)" "$B/b06.sh" 0 "traces : 9 + 2 = 11 fichiers"
. "$VAR"; P="$ESPACE_A/pieces"
n=$(cd "$P" && find . -type f | grep -c -E 'lecture-sondes|resume\.json|activations|adaptateur'); [ "$n" = 0 ] && { OK=$((OK+1)); echo "conforme : aucun fichier fermé factice extrait (lecture-sondes, resume, activations, adaptateur)"; } || { KO=$((KO+1)); echo "ÉCART : $n fichier(s) fermé(s) extrait(s)"; }
echo "T0.7 jouet" >> "$P/constat-noms-7b-v2.txt"
joue "artefact X3 : contenu interdit dans le constat → bloc A3 arrête" "$B/b07.sh" 1 "contenu interdit"
sed -i '$d' "$P/constat-noms-7b-v2.txt"
joue "bloc A3 (pièces, filtres de noms et de contenu, bordereau)" "$B/b07.sh" 0 "pièces : 33 fichiers"
joue "bloc A4 (message de remise)" "$B/b08.sh" 0 "message écrit, aucun marqueur restant"
V="$ESPACE_A/verdict-ferme"; printf '# verdict jouet\n' > "$V/verdict-T0.6-table-A-7b-v1.md"; printf '{"jouet": true}\n' > "$V/verdict-T0.6-table-A-7b-v1-issue.json"
printf 'message altéré\n' > "$V/verdict-T0.6-table-A-7b-v1-message-recu-v1.txt"
joue "artefact X4 : message reçu différent du message scellé → bloc A5 arrête, rien n'est commité" "$B/b09.sh" 1 "message reçu différent du message scellé"
cp "$BAC/message-remise-a-v2.txt" "$V/verdict-T0.6-table-A-7b-v1-message-recu-v1.txt"; printf 'x' > "$V/verdict-T0.6-table-A-7b-v1-travail.tar"
joue "artefact X5 : archive dans verdict-ferme → bloc A5 arrête" "$B/b09.sh" 1 "fichier(s) de nom inattendu"
rm "$V/verdict-T0.6-table-A-7b-v1-travail.tar"
joue "bloc A5 (message attesté, copie, sceaux, commit, poussée)" "$B/b09.sh" 0 "commit du verdict A :"
joue "bloc A5 relancé (reprise à la poussée)" "$B/b09.sh" 0 "verdict A déjà commité"
python3 -I - "$B/b10.sh" "$B/b10-rempli.sh" <<'FIN'
import sys
t = open(sys.argv[1], encoding="utf-8").read()
t = t.replace("<rapport final du lecteur A, tel quel, à la place de cette ligne>",
              "STATUT : fichier-d-issue-ecrit\nFICHIERS : verdict-T0.6-table-A-7b-v1.md\nISSUE : A9 (jouet, ne doit pas entrer au journal)\nMESSAGE REÇU : jouet")
t = t.replace("CROCHET='<bloquée | passée>'", "CROCHET='bloquée'").replace("session hôte : <modèle A | modèle C>", "session hôte : modèle A")
open(sys.argv[2], "w", encoding="utf-8").write(t)
FIN
joue "bloc F-A (journal provisoire sans issue, poussée)" "$B/b10-rempli.sh" 0 "RENDU — branche verdict/t06-table-a-7b-compte-3-v1"
# --- contrôles sur le dépôt distant jouet
BRA=verdict/t06-table-a-7b-compte-3-v1
c1=$(git -C "$DIST" rev-list --count "main..$BRA"); f=$(git -C "$DIST" diff --name-only "main" "$BRA" | sort | tr '\n' ' ')
echo "branche $BRA : $c1 commits au-dessus de main ; fichiers : $f"
[ "$c1" = 2 ] && printf '%s' "$f" | grep -q 'docs/verdicts/verdict-T0.6-table-A-7b-v1.md ' && printf '%s' "$f" | grep -q 'registres-provisoires/compte-3-phase-a-' \
    && [ "$(git -C "$DIST" diff --name-only main "$BRA" | grep -v -c -E '^(docs/verdicts/verdict-T0\.6-table-A-7b-v1|registres-provisoires/compte-3-phase-a-)')" = 0 ] \
    && { OK=$((OK+1)); echo "conforme : deux commits, fichiers du verdict et journal provisoire seulement"; } || { KO=$((KO+1)); echo "ÉCART : contenu de la branche"; }
[ "$(git -C "$DIST" rev-parse main)" = "$MAIN0" ] && { OK=$((OK+1)); echo "conforme : main du dépôt distant inchangé (rien poussé sur main)"; } || { KO=$((KO+1)); echo "ÉCART : main a changé"; }
J=$(git -C "$DIST" diff --name-only main "$BRA" | grep '^registres-provisoires/.*\.md$')
git -C "$DIST" show "$BRA:$J" | grep -q 'ISSUE' && { KO=$((KO+1)); echo "ÉCART : la ligne ISSUE est entrée au journal provisoire"; } || { OK=$((OK+1)); echo "conforme : aucune ligne ISSUE au journal provisoire"; }
[ -z "$(git -C "$DEP" status --porcelain --untracked-files=no)" ] && { OK=$((OK+1)); echo "conforme : dépôt de la session propre"; } || { KO=$((KO+1)); echo "ÉCART : dépôt de la session modifié"; }
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "RÉPÉTITION DE LA PHASE A : TOUT CONFORME" || echo "RÉPÉTITION DE LA PHASE A : ÉCARTS"
date -u +"fin de la répétition : %Y-%m-%dT%H:%M:%SZ"
