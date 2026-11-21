#!/usr/bin/env bash
# écrit par l'amorce v1 de (ii-b) : consigne et pousse les résultats partiels ; git seul, sous verrou ; $1 = motif
R='/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/dev-0011/repetition/dossier-repetition-v1/instance'; BRANCHE='essai/iib-explo-v5'; T='/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/dev-0011/repetition/dossier-repetition-v1/instance/iib'; JOURNAL='/tmp/claude-0/-home-user-controle-ia-travail/6e2b0069-d4f4-5fd1-be63-f516f6a3ee23/scratchpad/dev-0011/repetition/dossier-repetition-v1/instance/iib/journal.txt'; MORCEAU_MAX='90000000'; POUSSEE_ATTENTE_S='0'
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
pousser() { local essai; for essai in 1 2 3; do timeout -k 10 600 git push -q origin "$BRANCHE" 2>"$T/poussee.err" && return 0; journal "poussée : tentative $essai refusée"; [ "$essai" -lt 3 ] && sleep $((POUSSEE_ATTENTE_S * essai * essai)); done; return 1; }
refuser_gros() {  # C11 : aucun fichier de plus de MORCEAU_MAX octets ne part dans un commit (le dépôt distant le refuserait)
    local f t; while IFS= read -r f; do [ -f "$f" ] || continue; t=$(stat -c %s -- "$f" 2>/dev/null || echo 0)
        if [ "$t" -gt "$MORCEAU_MAX" ]; then git rm -q --cached -- "$f" >/dev/null 2>&1; journal "ERREUR DE CHAÎNE (C11) : $f fait $t octets > $MORCEAU_MAX : retiré du commit, resté sur l'instance"; echo "$f $t" >> "$R/iib-fichiers-trop-gros.txt"; fi
    done < <(git diff --cached --name-only --diff-filter=AM); return 0; }
ajouter() {  # C-V4-1 : un `git add` en échec (index.lock) n'est jamais lu comme « rien à committer » ; code 1 et journal
    git add "$@" 2>"$T/add.err" && return 0
    journal "ERREUR DE CHAÎNE (C-V4-1) : git add en échec ($*) : $(tr '\n' ' ' < "$T/add.err" | cut -c1-200)"; echo "$(date -u +%FT%TZ) git add en échec : $*" >> "$R/iib-erreurs-chaine.txt"; return 1; }
ajouter_legeres() { local f rc=0; for f in donnees/*/lots/ids-lot-*.json donnees/*/lots/ids-lot-*.json.sha256 \
        donnees/*/ids-actions-*-iib-v5.json donnees/*/ids-actions-*-iib-v5.json.sha256; do
        if [ -f "$f" ]; then ajouter -f "$f" || rc=1; fi; done; return $rc; }
ajouter_morceaux() { return 0; }    # (ii-b) : aucune activation, aucun morceau
commit_verifie() {  # C-V4-1 : 0 = commit fait ; 10 = rien à committer (index vide) ; 1 = commit en échec (réessayé une fois)
    refuser_gros
    local rc essai; git diff --cached --quiet 2>/dev/null; rc=$?
    [ "$rc" = 0 ] && return 10
    if [ "$rc" != 1 ]; then journal "ERREUR DE CHAÎNE (C-V4-1) : lecture de l'index impossible (git diff, code $rc)"; echo "$(date -u +%FT%TZ) lecture de l'index impossible : $1" >> "$R/iib-erreurs-chaine.txt"; return 1; fi
    for essai in 1 2; do
        git commit -qm "$1" >/dev/null 2>"$T/commit.err" && return 0
        journal "ERREUR DE CHAÎNE (C-V4-1) : commit en échec (tentative $essai) : $(tr '\n' ' ' < "$T/commit.err" | cut -c1-200)"
        [ "$essai" = 1 ] && sleep "${COMMIT_ATTENTE_S:-2}"
    done
    echo "$(date -u +%FT%TZ) commit en échec : $1" >> "$R/iib-erreurs-chaine.txt"; return 1; }
etape_commit() {  # $1 = message, $2 = journal si fait, $3 = journal si rien à committer ; rend 0 (fait ou rien) ou 1 (échec de chaîne)
    local rc; commit_verifie "$1"; rc=$?
    case "$rc" in 0) [ -z "$2" ] || journal "$2"; return 0;; 10) [ -z "$3" ] || journal "$3"; return 0;; *) return 1;; esac; }
trace_consignation() {  # R-1692 (E2-6) : le journal de l'instance atteint la branche quand la consignation vient de la minuterie (échéance, dépense épuisée) ou d'un redémarrage ; sinon une échéance pendant l'installation ne laisse RIEN sur la branche
    local d; mkdir -p traces || return 1
    d=$(mktemp -d "traces/iib-consignation-$(date -u +%Y%m%d-%H%M%S)-XXXX") || return 1
    { echo "motif : $1"; echo "heure : $(date -u +%FT%TZ)"; echo "dernière ligne du journal avant la consignation : ${DERNIERE_LIGNE_AVANT:-$(tail -n 1 "$JOURNAL" 2>/dev/null)}" | cut -c1-400
      echo "--- 400 dernières lignes du journal de l'instance (ligne d'échéance et dernière étape atteinte comprises) ---"; tail -n 400 "$JOURNAL" 2>/dev/null | cut -c1-400; } > "$d/journal-consignation.txt"
    [ -f "$R/iib-minuterie.log" ] && tail -n 200 "$R/iib-minuterie.log" | cut -c1-400 > "$d/iib-minuterie-fin.txt"      # la ligne « ÉCHÉANCE … atteinte (C14) » est écrite par la minuterie, pas par l'amorce
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    ajouter "$d" || return 1
    etape_commit "(ii-b) : journal de l'instance ($1)" "$1 : journal de l'instance committé" ""; }
consigner_partiel() {  # $1 = motif ; deux commits (données légères d'abord, morceaux ensuite), poussée ; 0 = tout, 1 = poussée impossible, 2 = poussée faite de ce qui existe, mais échec de chaîne
    local echec=0
    ajouter -A runs diag || echec=1
    ajouter_legeres || echec=1
    etape_commit "(ii-b) : résultats et données légères ($1)" "$1 : résultats et données légères committés" "$1 : aucun résultat léger à committer" || echec=1
    ajouter_morceaux || echec=1
    etape_commit "(ii-b) : sous-ensemble d'activations en morceaux ($1)" "$1 : morceaux committés" "" || echec=1
    if [ "${TRACE_CONSIGNATION:-0}" = 1 ]; then trace_consignation "$1" || echec=1; fi    # fixé par le seul chemin de la ligne de commande (minuterie, redémarrages), jamais par la fin de run
    if pousser; then journal "branche $BRANCHE poussée ($1)"; [ "$echec" = 0 ] && return 0; journal "ERREUR DE CHAÎNE (C-V4-1) : poussée faite de ce qui existe ($1), mais un ajout ou un commit a échoué"; return 2; fi
    journal "poussée impossible ($1) : résultats restés sur l'instance"; return 1; }
if [ "${1:-}" = "--source" ]; then return 0 2>/dev/null || exit 0; fi
exec 9>>"$R/iib-consigner.lock"; flock -w 1500 9 || { echo "verrou de consignation non obtenu ($1)"; exit 1; }
cd "$R/amorce-depot" || { echo "dépôt extrait inaccessible"; exit 1; }
DERNIERE_LIGNE_AVANT=$(tail -n 1 "$JOURNAL" 2>/dev/null)    # étape atteinte avant que la consignation écrive ses propres lignes
TRACE_CONSIGNATION=1 consigner_partiel "$1"
exit $?
