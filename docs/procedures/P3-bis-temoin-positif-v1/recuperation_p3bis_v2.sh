#!/usr/bin/env bash
# Chaîne v2 (2026-11-11 ; règle (a') de P3-bis : R-2296, R-2320 ; consigne `consigne-code-p3bis-regle-a-v1.md`, `39300056…`) : copie de `recuperation_p3bis_v1.sh`, gardé
# tel quel (R12), noms de la chaîne en v2 ; lectures fermées par `ouverture_p3bis_v3` (lecture complémentaire `lecture_p3bis_v2`, règle (a') décisive).
# Brouillon 3 (2026-11-10, contre-lecture différentielle, CD-05) : clone de la branche de calcul en extraction partielle
# (aucun chemin interdit extrait), absence vérifiée, refus sinon (code 2).
# Brouillon 2 (2026-11-10, après fusion du code corrigé, branche prep/p3bis-code-v2) : la ligne « motif du dépliage : … »
# que le module v2 imprime sur un refus du dépliage (CP-11 ; elle ne porte que sur l'intégrité du second paquet) est admise
# et affichée ; rien d'autre ne change.
# Récupération de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au 2026-11-23 : R-2077), v1 : contrôles de la branche de calcul poussée par
# l'instance, lectures FERMÉES, commit et poussée du seul paquet des lectures et de son compagnon. Texte : brouillon 9
# (eb65773f…), plan, points 1, 3, 4, 6 et 11 ; « Liste d'arrêt » ; contre-lecture du code (7a074ad1…), point 6.
# Déclinée de docs/procedures/P3-premier-test-v2/recuperation_p3_v1.sh (P3) sous un nom neuf (R12). Ce qui change :
#   - CLONE DE LA BRANCHE DE CALCUL (calcul/p3bis-reel-vN, N = 1 à 3), jamais main (clone d'une seule branche, branche
#     courante relue) ;
#   - ajouts permis : manifeste du run, sondes-figees.json, resume.json ou arret.json (classe 1), morceaux et index du
#     second paquet, traces p3bis-* ; AUCUN fichier du run en clair (donnees/, episodes-p3.json : classe 2) ; un fichier
#     du run en clair est un écart (« Toute ouverture hors de la garde »), écrit KO ;
#   - run complet (resume.json, sans arrêt) : lectures fermées par le module d'ouverture (noms communs v2) :
#     « lectures-fermees --prereg <texte> --entropie <entropie citée> » (mode décisif) ; seules sortent les lignes de code
#     et l'empreinte du paquet (classe 1 ; rien d'autre n'est affiché) ; run sans résumé : aucune lecture (ligne 1 de la
#     table, « non lu ») ; aucun run : traces seules ; code 4 dans les deux cas, jamais 0 ;
#   - paquet des lectures : diag/p3bis-ferme-<run>/paquet-ferme-v1.tar, 16 783 360 octets, compagnon égal à l'empreinte
#     imprimée ; aucun fichier en clair resté dans le clone (sorties des lectures, espace fermé, fichiers dépliés) ;
#   - commit du SEUL paquet et de son compagnon (index relu : exactement ces deux chemins), poussé sur la branche de
#     calcul (avance rapide), relu sur le dépôt distant par son empreinte.
# Aucune valeur de jeton, aucun fichier de la classe 2 n'est affiché. Rien n'est fusionné. Aucune destruction ici
# (detruire_p3bis_v2.sh lit le rapport de ce script).
# Codes : 0 tous conformes, paquet poussé et relu ; 1 au moins un KO (rien n'est commité si un KO précède le commit) ;
# 2 usage, épingle non remplie, dossier existant, clonage impossible ; 4 récupération sans lecture (run sans résumé ou
# aucun run), contrôles des traces conformes.
# Le rapport (sortie entière) est écrit aussi dans DOSSIER_NEUF.rapport.txt.
# Usage : recuperation_p3bis_v2.sh S BRANCHE DOSSIER_NEUF
set -uo pipefail
# extraction partielle de tout clone de la chaîne (interdits communs v2, règle 9 ; contre-lecture différentielle, CD-05) :
# aucun chemin interdit n'est jamais extrait, donc jamais haché par verifier-arbre ; absence vérifiée sur disque
EXTRACTION=('/*' '!/docs/notes/bras-attaque/' '!/diag/20261109-070232-t06-reel/' '!/runs/20261109-070232-t06-reel/' '!/donnees/bras-attaque*' '!/donnees/mode-tenu-a-l-ecart*' '!/diag/*/lecture-sondes-t06.json*' '!/scripts/extraire_mesures_epreuve_t06_v1.py*')
ABSENTS=(docs/notes/bras-attaque diag/20261109-070232-t06-reel runs/20261109-070232-t06-reel scripts/extraire_mesures_epreuve_t06_v1.py)
SOI=$(realpath "$0")
[ $# -eq 3 ] || { echo "usage : recuperation_p3bis_v2.sh S BRANCHE DOSSIER_NEUF"; exit 2; }
S=$1; BRANCHE=$2; D=$(realpath -m "$3")
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
PY=A_EPINGLER                                    # interpréteur d'un environnement aux dépendances épinglées de S (celui des contrôles)
P=prereg/P3-bis-temoin-positif-v1.md
VERSEES=docs/procedures/P3-bis-temoin-positif-v1
ENTROPIE=173398867739501636779144561928402532101 # celle de P3, reprise (texte, en-tête)
OUVERTURE=controle_ia.premier_test_ia.ouverture_p3bis_v3   # lecture complémentaire lecture_p3bis_v2, règle (a') (R-2296)
AUTEUR="instance de calcul (P3-bis)"
MOTIF_RUN='^[0-9]{8}-[0-9]{6}-p3bis-reel$'
TAILLE_PAQUET=16783360
COPIE_EXIGEE=oui
TRAV="$D.travail"; RAPPORT="$D.rapport.txt"
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[[ "$BRANCHE" =~ ^calcul/p3bis-reel-v[123]$ ]] || { echo "BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 (jamais main)"; exit 2; }
grep -qE '^[A-Z_]+="?A_EPINGLER' "$SOI" && { echo "épingle restée « A_EPINGLER » (PY) : aucune récupération"; exit 2; }
[ -x "$PY" ] || { echo "interpréteur $PY absent"; exit 2; }
for x in "$D" "$TRAV" "$RAPPORT"; do [ -e "$x" ] && { echo "$x existe déjà (R12)"; exit 2; }; done
mkdir -p "$TRAV" || exit 2
export PYTHONDONTWRITEBYTECODE=1
echecs=0
ok() { echo "OK  $*"; }
ko() { echo "KO  $*"; echecs=$((echecs + 1)); }
finir() { exit "$1"; }
corps() {
git clone -q --no-checkout --branch "$BRANCHE" --single-branch "$DEPOT_URL" "$D" || { echo "clonage de la branche $BRANCHE impossible"; finir 2; }
git -C "$D" sparse-checkout set --no-cone "${EXTRACTION[@]}" || { echo "extraction partielle impossible"; finir 2; }
git -C "$D" checkout -q "$BRANCHE" || { echo "extraction de la branche $BRANCHE impossible"; finir 2; }
cd "$D" || finir 2
for x in "${ABSENTS[@]}"; do [ -e "$x" ] && { echo "REFUS : $x extrait sur disque (interdits communs v2, règle 9 ; CD-05) : aucune récupération"; finir 2; }; done
ok "0 clone en extraction partielle : ${ABSENTS[*]} absents du disque"
[ "$(git rev-parse --abbrev-ref HEAD)" = "$BRANCHE" ] && ok "0 clone de la branche de calcul $BRANCHE (jamais main)" || ko "0 branche courante $(git rev-parse --abbrev-ref HEAD) ≠ $BRANCHE"
TETE=$(git rev-parse HEAD); echo "tête de la branche : $TETE"
if [ "$COPIE_EXIGEE" = oui ]; then
    [ "$(git show "$S:$VERSEES/recuperation_p3bis_v2.sh" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$SOI" | cut -d' ' -f1)" ] \
        && ok "0 récupération exécutée = copie versée à S" || ko "0 récupération exécutée ≠ copie versée à S"
fi
# 1. ascendance et contenu : ajouts seulement, aux chemins permis ; aucun fichier du run en clair
git merge-base --is-ancestor "$S" "$TETE" 2>/dev/null && ok "1a S est ancêtre de la branche" || ko "1a S n'est pas ancêtre de la branche"
git diff --name-status --no-renames "$S" "$TETE" > "$TRAV/diff-status.txt" 2>/dev/null
NON_AJOUTS=$(grep -vc '^A' "$TRAV/diff-status.txt" || true)
[ "$NON_AJOUTS" = 0 ] && ok "1b seulement des ajouts ($(wc -l < "$TRAV/diff-status.txt") fichiers)" || ko "1b $NON_AJOUTS changement(s) autre(s) qu'un ajout"
cut -f2 "$TRAV/diff-status.txt" > "$TRAV/chemins.txt"
CLAIR=$(grep -E '^donnees/|/episodes-p3\.json(\.sha256)?$' "$TRAV/chemins.txt" | tr '\n' ' ' || true)
[ -z "$CLAIR" ] && ok "1c aucun fichier du run en clair (second paquet seulement)" \
    || ko "1c FICHIER DU RUN EN CLAIR sur la branche (écart « Toute ouverture hors de la garde », à consigner) : $CLAIR"
PERMIS='^(runs/[^/]+/manifeste\.json(\.sha256)?|diag/[^/]+/(sondes-figees|resume|arret)\.json(\.sha256)?|diag/[^/]+/paquet-run-ferme-v1\.tar\.[0-9]{3}(\.sha256)?|diag/[^/]+/paquet-run-ferme-v1\.json(\.sha256)?|traces/p3bis-[^/]+/(journal\.txt|tests\.txt|tests\.err|run\.json|run\.err|nvidia-smi\.txt|pip-freeze\.txt|processeur\.txt|second-paquet\.txt|empreintes\.sha256))$'
HORS=$(grep -vE "$PERMIS" "$TRAV/chemins.txt" | tr '\n' ' ' || true)
[ -z "$HORS" ] && ok "1c ajouts aux seuls chemins permis (manifeste, classe 1, second paquet, traces p3bis-*)" || ko "1c chemins hors périmètre : $HORS"
RUNS=$(grep -E '^(runs|diag)/' "$TRAV/chemins.txt" | cut -d/ -f2 | sort -u)
NRUNS=$(printf '%s\n' "$RUNS" | grep -c . || true)
RUN=$(printf '%s\n' "$RUNS" | head -1)
SANS_RUN=non
if [ "$NRUNS" = 1 ] && [[ "$RUN" =~ $MOTIF_RUN ]] && [ -f "runs/$RUN/manifeste.json" ]; then ok "1d un seul run : $RUN"
elif [ "$NRUNS" = 0 ]; then SANS_RUN=oui; echo "--  1d aucun run sur la branche : récupération des traces seules (arrêt avant le run)"
else ko "1d runs : $(printf '%s ' $RUNS)(un seul, au motif, avec son manifeste, attendu)"; SANS_RUN=illisible; fi
AUTEURS=$(git log --format='%an' "$S..$TETE" | sort -u)
[ "$AUTEURS" = "$AUTEUR" ] && ok "1e commits de « $AUTEUR » ($(git rev-list --count "$S..$TETE"))" || ko "1e auteurs : $(printf '%s' "$AUTEURS" | tr '\n' ',')"
# 2. sceaux
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier-arbre . > "$TRAV/verifier-arbre.txt" 2>&1 \
    && ok "2a verifier-arbre : $(tail -1 "$TRAV/verifier-arbre.txt")" || ko "2a verifier-arbre : $(tail -3 "$TRAV/verifier-arbre.txt" | tr '\n' ' ' | cut -c1-300)"
for d in traces/p3bis-*/; do
    [ -d "$d" ] || continue
    git cat-file -e "$S:${d%/}" 2>/dev/null && continue
    (cd "$d" && sha256sum -c --quiet empreintes.sha256) > "$TRAV/sc.txt" 2>&1 && ok "2b sha256sum -c $d" || ko "2b $d : $(head -2 "$TRAV/sc.txt" | tr '\n' ' ')"
done
# 3. issue du run ; sans run complet : aucune lecture (code 4)
if [ "$SANS_RUN" = oui ]; then
    [ "$echecs" = 0 ] && { echo "RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN), SANS LECTURE : TOUS CONFORMES"; finir 4; }
    echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC"; finir 1
fi
if [ "$SANS_RUN" = non ] && [ ! -f "diag/$RUN/resume.json" ]; then
    [ -f "diag/$RUN/arret.json" ] && echo "--  3 run sans résumé (arret.json) : ligne 1 de la table, « non lu » ; aucune lecture" \
        || echo "--  3 run sans résumé ni arrêt consigné (processus mort : erreur de chaîne) ; aucune lecture"
    [ "$echecs" = 0 ] && { echo "RÉCUPÉRATION SANS LECTURE (RUN SANS RÉSUMÉ) : TOUS CONFORMES"; finir 4; }
    echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC"; finir 1
fi
[ "$SANS_RUN" = non ] && [ ! -f "diag/$RUN/arret.json" ] && ok "3 run complet : résumé, sans arrêt consigné" || ko "3 run : résumé et arrêt tous deux présents, ou runs illisibles"
[ -f "diag/$RUN/paquet-run-ferme-v1.json" ] && ls "diag/$RUN"/paquet-run-ferme-v1.tar.[0-9][0-9][0-9] > /dev/null 2>&1 \
    && ok "3 second paquet présent (index et morceaux)" || ko "3 second paquet absent (index ou morceaux)"
# texte de S : entropie citée une fois, égale à celle de P3
NE=$(grep -c "Entropie : \`" "$P" 2>/dev/null || true)
ENT=$(sed -n "s/.*Entropie : \`\([0-9]*\)\`.*/\1/p" "$P" 2>/dev/null | head -1)
[ "$NE" = 1 ] && [ "$ENT" = "$ENTROPIE" ] && ok "3 entropie citée une fois par le texte, celle de P3" || ko "3 entropie du texte « $ENT » (citée $NE fois) ≠ $ENTROPIE"
if [ "$echecs" != 0 ]; then echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC (aucune lecture, aucun commit)"; finir 1; fi
# 4. lectures fermées (mode décisif) : seules les lignes de code et l'empreinte du paquet sortent
H0=$(date -u +%Y%m%d-%H%M%S); RL="$H0-p3bis-lecture"; RLC="$H0-p3bis-lecture-complementaire"
PYTHONPATH=src "$PY" -B -m "$OUVERTURE" lectures-fermees --racine . --run "$RUN" --lecture "$RL" --lecture-complementaire "$RLC" \
    --prereg "$P" --entropie "$ENTROPIE" > "$TRAV/lectures-fermees.txt" 2>&1; cl=$?
ATTENDUES='^(code (dépliage du second paquet|lecture de P3|lecture complémentaire|mise en paquet) : [0-9]+|paquet des lectures : [0-9a-f]{64}|motif du dépliage : .*)$'
if grep -qvE "$ATTENDUES" "$TRAV/lectures-fermees.txt"; then
    ko "4 sortie des lectures fermées hors de la classe 1 ($(grep -cvE "$ATTENDUES" "$TRAV/lectures-fermees.txt") ligne(s), non affichées ; écart à consigner)"
else sed 's/^/    /' "$TRAV/lectures-fermees.txt"; fi
CODES_OK=$(grep -cE '^code (dépliage du second paquet|lecture de P3|lecture complémentaire|mise en paquet) : 0$' "$TRAV/lectures-fermees.txt" || true)
SHA=$(sed -n 's/^paquet des lectures : \([0-9a-f]\{64\}\)$/\1/p' "$TRAV/lectures-fermees.txt")
[ "$cl" = 0 ] && [ "$CODES_OK" = 4 ] && [[ "$SHA" =~ ^[0-9a-f]{64}$ ]] && ok "4 lectures fermées (--prereg $P --entropie) : quatre codes 0, paquet $SHA" \
    || ko "4 lectures fermées : code $cl, $CODES_OK code(s) 0 sur 4 (une garde a arrêté une étape : nœud ; la lecture n'est jamais rejouée pour la mise en paquet)"
PAQ="diag/p3bis-ferme-$RUN/paquet-ferme-v1.tar"
if [ -f "$PAQ" ] && [ "$(stat -c %s "$PAQ")" = "$TAILLE_PAQUET" ] && [ "$(cat "$PAQ.sha256" 2>/dev/null)" = "$SHA  paquet-ferme-v1.tar" ] \
   && [ "$(sha256sum "$PAQ" | cut -d' ' -f1)" = "$SHA" ]; then ok "4 paquet des lectures : $TAILLE_PAQUET octets, compagnon égal à l'empreinte imprimée"
else ko "4 paquet des lectures absent, d'une autre taille, ou compagnon autre"; fi
# aucun fichier en clair resté dans le clone (non suivis et ignorés compris) : seuls le paquet et son compagnon
git status --porcelain --ignored --untracked-files=all | sed 's/^...//' | grep -vE '(^|/)__pycache__/' | sort > "$TRAV/restes.txt"
[ "$(tr '\n' ' ' < "$TRAV/restes.txt")" = "$PAQ $PAQ.sha256 " ] && ok "4 aucun fichier en clair resté dans le clone (seuls le paquet et son compagnon)" \
    || ko "4 fichiers restés dans le clone hors du paquet : $(grep -vxF -e "$PAQ" -e "$PAQ.sha256" "$TRAV/restes.txt" | wc -l) (non affichés ; écart à consigner)"
if [ "$echecs" != 0 ]; then echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC (aucun commit)"; finir 1; fi
# 5. commit du seul paquet et de son compagnon ; poussée sur la branche de calcul ; relecture sur le dépôt distant
git add -- "$PAQ" "$PAQ.sha256"
[ "$(git diff --cached --name-only | sort | tr '\n' ' ')" = "$PAQ $PAQ.sha256 " ] && ok "5 index : exactement le paquet et son compagnon" || ko "5 index : autre chose que le paquet et son compagnon"
if [ "$echecs" = 0 ]; then
    git -c user.name="session de pilotage (P3-bis)" -c user.email=session@invalid -c commit.gpgsign=false \
        commit -qm "P3-bis : paquet des lectures fermé du run $RUN ($SHA)" && ok "5 commit du paquet ($(git rev-parse HEAD))" || ko "5 commit du paquet impossible"
fi
if [ "$echecs" = 0 ]; then
    git push -q origin "HEAD:refs/heads/$BRANCHE" > "$TRAV/poussee.txt" 2>&1 && ok "5 poussée sur $BRANCHE (avance rapide)" || ko "5 poussée sur $BRANCHE refusée : $(tail -1 "$TRAV/poussee.txt" | cut -c1-200)"
    git fetch -q origin "$BRANCHE" 2>/dev/null
    [ "$(git rev-parse FETCH_HEAD 2>/dev/null)" = "$(git rev-parse HEAD)" ] && [ "$(git show "FETCH_HEAD:$PAQ" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$SHA" ] \
        && [ "$(git diff --name-only "$TETE" FETCH_HEAD | sort | tr '\n' ' ')" = "$PAQ $PAQ.sha256 " ] \
        && ok "5 dépôt distant relu : tête = commit du paquet, paquet à son empreinte, seuls deux chemins ajoutés" || ko "5 dépôt distant relu : tête, empreinte ou chemins autres"
fi
if [ "$echecs" = 0 ]; then echo "RÉCUPÉRATION : TOUS CONFORMES ; paquet des lectures $SHA poussé sur $BRANCHE"; finir 0; fi
echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC"; finir 1
}
corps 2>&1 | tee "$RAPPORT"
exit "${PIPESTATUS[0]}"
