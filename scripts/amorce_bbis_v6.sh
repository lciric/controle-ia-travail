#!/usr/bin/env bash
# v6 (2026-11-18, GO-2026-11-18-04 ; la v5 reste, R12) : la v5, dont rien ne change hors six écarts, chacun marqué « v6 » à sa
#   place (trois arrêts certains de R-3160, rapport docs/notes/prealables-course-etape-b-bis-v1/rapport-portillon-et-pilote-v1.md) :
#   (1) MIN_ESSAIS : plancher fixé au compte MESURÉ sur l'arbre que ces motifs extraient (et non sur l'arbre complet) ;
#   (2) MOTIFS : onze fichiers de plus, ceux-là seulement — les scripts que la fiche de code en vigueur cite et que la v5
#       n'extrayait pas ; aucun interdit d'extraction levé (jamais docs/notes/, jamais la pièce « mots et coût ») ;
#   (3) bloc neuf « fiche-sur-l-arbre » : les contrôles de registre et de fiche de la garde d'entrée de la marche, rejoués dès la
#       fin de l'étape 3, AVANT l'installation des paquets et la descente du modèle (un commit de course sans les lignes
#       d'inscription ou sans un fichier de la fiche arrête à la première minute, non après le démarrage payé) ;
#   (4) clé d'interface du conteneur exigée avant d'armer la minuterie (vide, la minuterie tournait sans jamais détruire :
#       correction 6 de la contre-lecture du projet de feu) ;
#   (5) empreinte de cette amorce écrite au journal (la fiche de code en vigueur ne cite pas la v6 : trace de ce qui a tourné) ;
#   (6) nom du lanceur dans un message (lancer_bbis_v6.sh). Passée par scripts/lancer_bbis_v6.sh.
# Amorce de l'instance de l'étape B bis de T0.7, v4 (la v3, dont la marche est `controle_ia.t07bbis.marche_v4` : contrôle
# carte-processeur v4 et mesure de dispersion du second addendum ; branche de sortie neuve donnees/t07-etape-b-bis-v2 (la v1 porte
# la course arrêtée, R12) ; minimum d'essais relevé ; blocs marqués identiques à ceux de la v1 ; les v1 à v3 restent, R12)
# (prereg/T0.7-etape-B-bis-v1.md, plan, points 1 à 8 ; « Calcul et dépense » ;
# « Liste d'arrêt »). Jouée au démarrage de l'instance (A100, étiquette bbis-t07-v1), passée par scripts/lancer_bbis_v4.sh (commande
# de création imprimée, base64). Une instance, une marche ; écrit sous $R/bbis-t07-v1 seulement.
# Ordre : 0. minuterie de destruction par l'identifiant à l'échéance (R10) ; 1. machine (carte, clés par leur nom, version CUDA
#   servie par le pilote au moins 13.0, lue dans l'en-tête de nvidia-smi : sinon arrêt, code 2, avant toute installation) ; 2. dépôt au
#   commit COMMIT (extraction partielle : src, tests du paquet, scripts, prereg du texte, registres nommés et fichiers qu'ils citent ;
#   jamais docs/notes/, jamais les fichiers de la pièce « mots et coût », jamais scripts/extraire_mesures_epreuve_t06_v1.py) ;
#   3. sortie de 7b par refspec explicite, FICHIERS NOMMÉS seulement (manifeste, episodes-t06.json, distillation-t06.json,
#   textes, mesures, deux adaptateurs, sous-ensemble d'activations) : jamais lecture-sondes-t06.json, resume.json, ni rien de 7a ;
#   puis **commit local des entrées copiées** (jamais poussé ; arbre propre exigé, correction M1) ;
#   4. paquets ; 5. essais du paquet (tests/test_t07bbis_*.py ; ligne de compte entière au journal, au moins MIN_ESSAIS passés,
#   correction M3) ; 6. modèle au cache local (révision du manifeste de 7b) ; 7. contrôle que la branche de sortie est neuve
#   (dès lors, tout arrêt pousse ses traces : avant que la branche soit prête, par un commit sur COMMIT, mineur m-A) ;
#   8. marche (`controle_ia.t07bbis.marche_v4`, BBIS_INSTANCE=1, hors ligne ; le manifeste cite le commit local et son parent),
#   puis branche neuve donnees/t07-etape-b-bis-v2 créée **depuis COMMIT** (le commit local des entrées n'y entre jamais) et
#   poussée (légers d'abord, fichiers de moins de 95 Mo seulement) ; 9. fin : état « stopped » demandé ; la session détruit par
#   l'identifiant (R10). Arrêt de débit (code 3 de la marche) : relecture et journal poussés, instance arrêtée (« stopped »),
#   gardée au plus 12 heures, nœud de Lazar (la session détruit sans mot dans les 12 heures). Arrêt écrit de la marche (code 4,
#   arret-marche-bbis.json, correction M2) : traces poussées, instance arrêtée.
# Aucune aire, aucun état, aucun résumé de score n'est imprimé ni écrit (le journal ne porte que des étapes et des durées).
# Variables (--env) : COMMIT, BRANCHE_CODE (branche qui porte COMMIT), RUN_7B, BRANCHE_7B, RUN_BBIS, ECHEANCE_UTC_S, GO_ID
#   (GO-2026-11-14-09), GH_TOKEN, HF_TOKEN ; facultatives, sur le mot de Lazar seulement : VARIANTE=r1 et DECISION_VARIANTE=R-…
#   (variante (r1) de la garde de débit) ; posées par Vast : CONTAINER_ID, CONTAINER_API_KEY. Aucune clé n'est jamais affichée.
# Essai local (AMORCE_ESSAI_LOCAL=1) : contrôles des arguments seulement, puis sortie (code 0) avant tout réseau et avant toute
#   écriture sur le disque (correction m5 : aucun dossier créé) ; hors essai, RACINE_AMORCE est refusée.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
R="${RACINE_AMORCE:-/root}"
[ "$ESSAI" = 1 ] || [ -z "${RACINE_AMORCE:-}" ] || { echo "BBIS REFUS : RACINE_AMORCE en essai local seulement"; exit 2; }
T="$R/bbis-t07-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-bbis.txt"; XT=traces/bbis-t07-v1
API=https://console.vast.ai/api/v0
GO_ATTENDU=GO-2026-11-14-09
BR_SORTIE=donnees/t07-etape-b-bis-v2
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
SEUIL=94000000
# essais du paquet qui passent sur l'instance (extraction partielle : bout_en_bout sauf un essai, etat_impose et
# lien_mots_et_cout sautent) ; compte établi par simulation de l'extraction, rapport-developpeur-corrections-v1.md (M3) et
# recompté après m-A (rapport-developpeur-corrections-v2.md), après la destruction vérifiée (…-v3.md) et après l'ajout de
# l'instance 60670453 à la liste des autres sessions (…-v4.md) ; v3 (m2 de la contre-lecture du brouillon 5, R-2919) : relevé au
# compte neuf de l'arbre de l'instance simulé par ces motifs, tous les essais neufs gardés (corrections-controle-attention-v2.md)
# v4 (second addendum) : 115 de la v3 plus les essais neufs du second addendum qui passent sans docs/notes ni brouillons
# (rapport-second-addendum-bbis-v1.md, § 3 ; à recompter sur l'arbre de l'instance simulé avant le feu)
# v5 : recompte après versement complet sur main (R-3073) — 176 essais passent (commit 5378c2de, 2026-11-17)
# v6 (écart 1) : les 176 de la v5 étaient comptés sur l'arbre complet de main (R-3074) ; sur l'arbre extrait par les motifs
#   ci-dessous, 25 essais sautent faute de fichiers que cette amorce s'interdit d'extraire (docs/notes/, pièce « mots et coût »,
#   fabrique factice) : plancher = compte mesuré par simulation de l'arbre extrait (`scripts/lancer_bbis_v6.sh essais-du-commit`,
#   motifs et ligne d'essais lus dans ce texte), à remesurer au commit de la course avant le feu
MIN_ESSAIS=151
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
j() { printf '%s BBIS %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
BRANCHE_PRETE=0
SORTIE_LIBRE=0   # 1 après le contrôle de l'étape 7 (branche de sortie absente du dépôt distant), tant qu'elle n'est pas prête
fin_instance() {  # état « stopped » demandé ; la minuterie meurt avec le conteneur ; la session détruit par l'identifiant (R10)
    local c
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    j "fin, code $1 ; état « stopped » demandé : HTTP $c ; la session détruit par l'identifiant (R10, avec -y) et vérifie l'absence de l'identifiant dans la liste des instances (lancer_bbis_v6.sh verifier-destruction)"
    sleep infinity; exit "$1"; }
# >>> arret-et-traces (extrait et joué par tests/test_t07bbis_chaine_instance_v1.py, mineur m-A)
traces() { mkdir -p "$D/$XT" && cp -f "$X"/* "$D/$XT/"; }
arret() { j "ARRET : $1"
    if [ "$BRANCHE_PRETE" = 1 ]; then traces && pousser "B bis : traces de l'arrêt" "$XT" || true
    elif [ "$SORTIE_LIBRE" = 1 ]; then traces_sur_commit || j "traces non poussées (commit des traces sur COMMIT impossible)"; fi
    fin_instance "${2:-4}"; }
traces_sur_commit() {  # arrêt entre le contrôle de la branche de sortie (étape 7) et le moment où elle est prête (après la
    # marche) : traces poussées sur la branche neuve par un commit fait sur COMMIT dans un index à part ; la tête, l'arbre et le
    # commit local des entrées de 7b ne sont ni touchés ni poussés (mineur m-A de la vérification courte)
    local ix="$T/index-traces-sur-commit" arbre c f n
    SORTIE_LIBRE=0
    [ ! -e "$ix" ] && traces || return 1
    for f in "$D/$XT"/*; do [ "$(stat -c %s "$f")" -le "$SEUIL" ] || return 1; done
    GIT_INDEX_FILE="$ix" git -C "$D" read-tree "$COMMIT" && GIT_INDEX_FILE="$ix" git -C "$D" add --sparse -f -- "$XT" || return 1
    arbre=$(GIT_INDEX_FILE="$ix" git -C "$D" write-tree) || return 1
    c=$(git -C "$D" commit-tree "$arbre" -p "$COMMIT" -m "B bis : traces de l'arrêt (branche de sortie non prête)") || return 1
    for n in 1 2 3; do git -C "$D" push -q origin "$c:refs/heads/$BR_SORTIE" \
        && { j "traces poussées : $c (parent $COMMIT ; commit local des entrées jamais poussé)"; return 0; }; sleep $((20 * n)); done
    return 1; }
# <<< arret-et-traces
# >>> cuda-du-pilote (même texte dans les deux amorces de B bis ; extrait et joué par tests/test_repetition_bbis_v1.py)
# Roue torch 2.14.1 de requirements-gpu.txt construite pour CUDA 13.0 : le pilote doit servir CUDA 13.0 au moins, lu dans l'en-tête
# de `nvidia-smi` (« CUDA Version: M.m », une fois exactement), AVANT l'installation des paquets (répétition du 15 novembre :
# pilote 570.211.01, CUDA 12.8, arrêt « torch ne voit pas la carte » après 118 s d'installation). Absente, multiple ou illisible :
# arrêt, jamais un défaut deviné ; même code que « torch ne voit pas la carte » (2).
cuda_du_pilote() {  # $1 = fichier de la sortie de `nvidia-smi` sans argument : imprime « M.m » ; 1 si absente, multiple ou illisible
    local v
    v=$(sed -n 's/^.*CUDA Version: *\([0-9][0-9]*\.[0-9][0-9]*\)[^0-9.].*$/\1/p; s/^.*CUDA Version: *\([0-9][0-9]*\.[0-9][0-9]*\)$/\1/p' "$1" 2>/dev/null)
    [ "$(printf '%s' "$v" | grep -c '^')" = 1 ] || return 1
    printf '%s\n' "$v" | LC_ALL=C grep -qxE '[0-9]{1,3}\.[0-9]{1,3}' || return 1
    printf '%s\n' "$v"; }
exiger_cuda_du_pilote() {  # $1 = fichier de la sortie de `nvidia-smi` ; arrêt (code 2) sous 13.0, absente ou illisible
    local v
    v=$(cuda_du_pilote "$1") || { j "lignes « CUDA » lues dans l'en-tête : $(grep -a 'CUDA' "$1" 2>/dev/null | head -n 3 | cut -c1-200 | tr '\n' ' ')"
        arret "version CUDA servie par le pilote illisible (« CUDA Version: » absent, multiple ou illisible dans la sortie de nvidia-smi) : torch ne verrait pas la carte (roue CUDA 13.0) ; arrêt avant l'installation des paquets" 2; }
    if [ "$((10#${v%%.*}))" -lt 13 ]; then
        arret "pilote trop ancien : CUDA $v servie par le pilote < 13.0 exigée par la roue torch de requirements-gpu.txt : torch ne verrait pas la carte ; arrêt avant l'installation des paquets" 2
    fi
    j "CUDA servie par le pilote : $v (au moins 13.0)"; }
# <<< cuda-du-pilote
# 0. arguments, échéance, minuterie
for v in COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S GO_ID; do
    [ -n "${!v:-}" ] || { echo "BBIS REFUS : variable $v absente"; exit 2; }; done
case "$COMMIT" in *[!0-9a-f]*|'') echo "BBIS REFUS : COMMIT illisible"; exit 2;; esac
[ "${#COMMIT}" = 40 ] || { echo "BBIS REFUS : COMMIT de 40 caractères attendu"; exit 2; }
[ "$GO_ID" = "$GO_ATTENDU" ] || { echo "BBIS REFUS : GO_ID $GO_ID ≠ $GO_ATTENDU (ligne de GO de B bis)"; exit 2; }
case "$RUN_BBIS" in [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-bbis-*) ;; *) echo "BBIS REFUS : RUN_BBIS illisible"; exit 2;; esac
case "$ECHEANCE_UTC_S" in ''|*[!0-9]*) echo "BBIS REFUS : ECHEANCE_UTC_S illisible"; exit 2;; esac
# variante (r1) de la garde de débit : seulement sur le mot de Lazar, ligne de décision citée (DECISION_VARIANTE=R-…)
VARIANTE_ARGS=()
case "${VARIANTE:-}" in
    '') [ -z "${DECISION_VARIANTE:-}" ] || { echo "BBIS REFUS : DECISION_VARIANTE sans VARIANTE"; exit 2; };;
    r1) case "${DECISION_VARIANTE:-}" in R-[0-9]*) VARIANTE_ARGS=(--variante r1 --decision "$DECISION_VARIANTE");;
            *) echo "BBIS REFUS : variante (r1) sans ligne de décision R-… (DECISION_VARIANTE)"; exit 2;; esac;;
    *) echo "BBIS REFUS : VARIANTE ${VARIANTE} inconnue ((r1) seulement)"; exit 2;;
esac
if [ "$ESSAI" = 1 ]; then echo "BBIS ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
mkdir -p "$X" || { echo "BBIS REFUS : $X impossible"; exit 2; }
[ "$ECHEANCE_UTC_S" -gt "$(date +%s)" ] && [ "$ECHEANCE_UTC_S" -le $(( $(date +%s) + 86400 )) ] || { echo "BBIS REFUS : échéance hors de [maintenant, + 24 h]"; exit 2; }
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "BBIS REFUS : identifiant de l'instance illisible"; exit 2;; esac
# v6 (écart 4) : sans la clé d'interface du conteneur, chaque demande de destruction de la minuterie part sans autorisation et
#   son code n'est jamais jugé : la minuterie ne détruirait rien. Refus avant tout (par le nom, jamais la valeur). Présente ne
#   veut pas dire valide : la ligne « minuterie lancée » se lit toujours au journal, et la session détruit par l'identifiant.
[ -n "${CONTAINER_API_KEY:-}" ] || { echo "BBIS REFUS : clé d'interface du conteneur absente (CONTAINER_API_KEY, par le nom) : la minuterie ne détruirait rien"; exit 2; }
# >>> minuterie (extrait et joué par tests/test_t07bbis_chaine_instance_v1.py ; défaut R-2789 : une destruction n'est jamais jugée
#     par un code de retour — tant que ce processus vit, l'instance n'est pas détruite, et la demande est refaite)
minuterie() { local n=0 c; while [ "$(date +%s)" -lt "$ECHEANCE_UTC_S" ]; do sleep 30; done
    j "MINUTERIE : échéance atteinte : destruction de l'instance $CONTAINER_ID par son identifiant (DELETE)"
    while :; do n=$((n + 1))
        c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
        j "MINUTERIE : DELETE, essai $n : HTTP $c (code jamais jugé ; seule l'absence de l'identifiant dans la liste des instances, lue par la session, prouve la destruction ; nouvel essai dans 60 s si l'instance vit encore)"
        if [ "$n" = 5 ]; then
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
            j "MINUTERIE : instance toujours vivante après 5 demandes de destruction : état « stopped » demandé : HTTP $c ; la session vérifie l'absence (verifier-destruction)"
        fi
        sleep 60; done; }
# <<< minuterie
minuterie < /dev/null & j "minuterie lancée (PID $!, échéance $(date -u -d "@$ECHEANCE_UTC_S" +%FT%TZ))"
j "amorce v6 : empreinte $(sha256sum < "$0" 2>/dev/null | cut -c1-64)"   # v6 (écart 5) : trace de ce qui a tourné
# 1. machine
for o in git curl python3 sha256sum awk sed grep stat find sort; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
[ -n "${HF_TOKEN:-}" ] || arret "HF_TOKEN absent (par le nom)" 2
# >>> carte-et-cuda (extrait et joué par tests/test_repetition_bbis_v1.py)
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible (nvidia-smi)" 2
grep -q 'A100' "$X/nvidia-smi.txt" || arret "carte autre qu'une A100 : $(head -n 1 "$X/nvidia-smi.txt")" 2
nvidia-smi > "$X/nvidia-smi-entete.txt" 2>&1 || arret "carte invisible (nvidia-smi, en-tête)" 2
exiger_cuda_du_pilote "$X/nvidia-smi-entete.txt"   # avant le dépôt, la sortie de 7b et l'installation des paquets
j "carte : $(head -n 1 "$X/nvidia-smi.txt") ; disque libre $(df -P -B1 "$R" | awk 'NR == 2 { print $4 }') octets"
# <<< carte-et-cuda
# 2. dépôt au commit COMMIT, extraction partielle
[ ! -e "$D" ] || arret "$D existe déjà (R12)" 2
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_CODE" "$DEPOT_URL_OFFICIEL" "$D" || arret "clonage" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (B bis)"; git -C "$D" config user.email "instance-calcul@invalid"
# v6 (écart 2) : onze lignes de plus (amorce et lanceur v5, amorces, lanceurs et scripts de la répétition v1 à v3) : les onze
#   fichiers que la fiche de code en vigueur (registres/t07-etape-b-bis/code-bbis-v2.json) cite et que la v5 n'extrayait pas ;
#   la garde d'entrée de la marche s'arrêtait au premier (« absent : arrêt (R11) »). Scripts de la chaîne seulement : aucune
#   donnée, aucun résultat, rien de la liste « Jamais » ; les trois exclusions et l'interdit de docs/notes/ ne bougent pas.
MOTIFS='/*
!/*/
/src/
/tests/conftest.py
/tests/test_t07bbis_*
/tests/aide_t07bbis_*
/scripts/amorce_bbis_v1.sh*
/scripts/lancer_bbis_v1.sh*
/scripts/amorce_bbis_v2.sh*
/scripts/lancer_bbis_v2.sh*
/scripts/amorce_bbis_v3.sh*
/scripts/lancer_bbis_v3.sh*
/scripts/amorce_bbis_v4.sh*
/scripts/lancer_bbis_v4.sh*
/scripts/amorce_bbis_v5.sh*
/scripts/lancer_bbis_v5.sh*
/scripts/amorce_repetition_bbis_v1.sh*
/scripts/amorce_repetition_bbis_v2.sh*
/scripts/amorce_repetition_bbis_v3.sh*
/scripts/lancer_repetition_bbis_v1.sh*
/scripts/lancer_repetition_bbis_v2.sh*
/scripts/lancer_repetition_bbis_v3.sh*
/scripts/repetition_carte_bbis_v1.py*
/scripts/repetition_carte_bbis_v2.py*
/scripts/repetition_carte_bbis_v3.py*
/scripts/enumerer_issues_bbis_v1.py*
/scripts/epreuve_niveau_deux_plis_bbis_v1.py*
/prereg/T0.7-etape-B-bis-v1.md*
/prereg/P3-consignes-v1.md*
/docs/sources/invites-2606.08892-v1/
/registres/t07-etape-b-bis-v1.md*
/registres/t07-etape-b-bis/
/registres/scellements-v1.md
/registres/scellements-v1.md.sha256
/registres/go-extraits/
!/diag/*/lecture-sondes-t06.json*
!/scripts/extraire_mesures_epreuve_t06_v1.py
!/scripts/mots_et_cout_t06_*'
git -C "$D" sparse-checkout init --no-cone && printf '%s\n' "$MOTIFS" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$COMMIT" || arret "commit $COMMIT introuvable sur $BRANCHE_CODE" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
COPIES=()
# >>> copie-des-fichiers-cites (extrait et joué par tests/test_t07bbis_chaine_instance_v1.py, correction m7)
for p in $(awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); if ($4 ~ /^[A-Za-z0-9._\/-]+$/ && $4 !~ /\.\./) print $4 }' "$D/registres/t07-etape-b-bis-v1.md" | sort -u); do
    case "$p" in *lecture-sondes-t06*|donnees/bras-attaque*|donnees/mode-tenu-a-l-ecart*|docs/notes/*) arret "chemin interdit cité : $p" 2;; esac
    for q in "$p" "$p.sha256"; do git -C "$D" cat-file -e "HEAD:$q" 2>/dev/null || continue
        mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "HEAD:$q" > "$D/$q" || arret "copie de $q" 2; COPIES+=("$q"); done; done
# <<< copie-des-fichiers-cites
j "dépôt au commit $COMMIT (branche $BRANCHE_CODE), registre propre et fichiers cités présents"
# 3. sortie de 7b : fichiers nommés seulement
git -C "$D" fetch -q origin "refs/heads/$BRANCHE_7B:refs/remotes/origin/$BRANCHE_7B" || arret "branche de 7b $BRANCHE_7B introuvable" 2
B7="refs/remotes/origin/$BRANCHE_7B"
apporter() { local q; for q in "$2" "$2.sha256"; do git -C "$D" cat-file -e "$1:$q" 2>/dev/null || continue
    mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "$1:$q" > "$D/$q" || arret "copie de $q" 2; COPIES+=("$q"); done; }
for f in "runs/$RUN_7B/manifeste.json" "diag/$RUN_7B/episodes-t06.json" "diag/$RUN_7B/distillation-t06.json"; do
    git -C "$D" cat-file -e "$B7:$f" 2>/dev/null || arret "$f absent de la branche de 7b" 2; apporter "$B7" "$f"; done
N7=0
for f in $(git -C "$D" ls-tree --name-only "$B7" -- "donnees/$RUN_7B/" | grep -E "^donnees/$RUN_7B/(adaptateur-(saboteur|temoin)\.pt|mesures-t06\.npz|textes-actions-t06\.jsonl|activations-sous-ensemble-t06-manifeste\.json|activations-sous-ensemble-t06-[0-9]{3}\.npz)$"); do
    apporter "$B7" "$f"; N7=$((N7 + 1)); done
[ "$N7" -ge 6 ] || arret "sortie de 7b incomplète ($N7 fichiers de données)" 2
for f in "diag/$RUN_7B/lecture-sondes-t06.json" "diag/$RUN_7B/resume.json"; do [ ! -e "$D/$f" ] || arret "$f présent (liste « Jamais ») : arrêt" 2; done
for p in $(python3 -I -c 'import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))["config"]
def f(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if isinstance(v, str) and (k == "chemin" or k.startswith("chemin_")):
                yield v
            yield from f(v)
    elif isinstance(x, list):
        for v in x:
            yield from f(v)
print("\n".join(sorted(set(f(c)))))' "$D/runs/$RUN_7B/manifeste.json"); do
    case "$p" in *lecture-sondes-t06*|docs/notes/*) arret "chemin interdit cité par la configuration de 7b : $p" 2;; esac
    apporter "HEAD" "$p"; done
j "sortie de 7b extraite : manifeste, épisodes, distillation, $N7 fichiers de données ; fichiers cités par sa configuration recopiés"
# >>> commit-local-des-entrees (extrait et joué par tests/test_t07bbis_chaine_instance_v1.py, correction M1)
commit_local_entrees() {  # entrées copiées commitées localement (jamais poussées) ; arbre propre exigé avant le manifeste
    local s
    [ "${#COPIES[@]}" -gt 0 ] || arret "aucune entrée copiée" 2
    git -C "$D" add --sparse -f -- "${COPIES[@]}" || arret "ajout local des entrées" 2
    git -C "$D" commit -q --allow-empty -m "B bis : entrées de 7b et fichiers cités, commit local de l'instance (jamais poussé)" \
        || arret "commit local des entrées" 2
    [ "$(git -C "$D" rev-parse HEAD^)" = "$COMMIT" ] || arret "parent du commit local des entrées ≠ COMMIT" 2
    s=$(git -C "$D" status --porcelain --untracked-files=all) || arret "état de l'arbre illisible" 2
    [ -z "$s" ] || arret "arbre non propre après le commit local des entrées : $(printf '%s' "$s" | head -n 3 | tr '\n' ' ')" 2
    ENTREES_LOCALES=$(git -C "$D" rev-parse HEAD)
}
# <<< commit-local-des-entrees
commit_local_entrees
j "entrées commitées localement : $ENTREES_LOCALES (parent $COMMIT ; jamais poussé), arbre propre"
# >>> fiche-sur-l-arbre (v6, écart 3 ; extrait et joué par tests/test_chaine_bbis_v6_v1.py)
# Mêmes contrôles que `marche_v4.gardes_d_entree` sur le registre propre et la fiche de code, sans aucun paquet (python3 de
# l'image, bibliothèque standard) : lignes SCELLEMENT-BBIS, CODE-BBIS (une, ou deux dont la seconde fait foi) et GO-BBIS ;
# fichier cité par chacune présent, compagnon .sha256 et empreinte conformes ; chaque fichier de la fiche présent, d'empreinte
# égale. Jamais plus sévère que la marche (qui rejoue tout, avec l'ancêtre) : ce bloc n'arrête que là où elle s'arrêterait.
fiche_sur_l_arbre() {  # $1 = racine du dépôt extrait ; 0 si conforme ; sinon premier motif sur la sortie, code 1
    python3 -I - "$1" <<'FIN_FICHE'
import hashlib, json, sys
from pathlib import Path
d = Path(sys.argv[1])
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def faute(m):
    print(m); sys.exit(1)
reg = d / "registres/t07-etape-b-bis-v1.md"
if not reg.is_file():
    faute("registre propre absent de l'arbre extrait")
lignes = {}
for l in reg.read_text(encoding="utf-8").splitlines():
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) == 4 and c[0] in ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS"):
        lignes.setdefault(c[0], []).append(c)
for k, permis in (("SCELLEMENT-BBIS", 1), ("CODE-BBIS", 2), ("GO-BBIS", 1)):
    n = len(lignes.get(k, []))
    if n == 0:
        faute(f"ligne {k} absente du registre propre au commit de la course (exigée par la garde d'entrée de la marche)")
    if n > permis:
        faute(f"ligne {k} en {n} exemplaires au registre propre ({permis} au plus)")
    _, _, chemin, attendu = lignes[k][-1]
    p, comp = d / chemin, d / (chemin + ".sha256")
    if not p.is_file():
        faute(f"{chemin} (ligne {k}) absent de l'arbre extrait")
    if not comp.is_file() or (comp.read_text(encoding="utf-8").split() or [""])[0] != sha(p) or sha(p) != attendu:
        faute(f"{chemin} (ligne {k}) : compagnon .sha256 absent, ou empreinte autre que celle du compagnon ou du registre")
try:
    fichiers = json.loads((d / lignes["CODE-BBIS"][-1][2]).read_text(encoding="utf-8"))["fichiers"]
    assert isinstance(fichiers, dict) and fichiers
except Exception as e:
    faute(f"fiche de code illisible ({type(e).__name__})")
for chemin, attendu in fichiers.items():
    if not (d / chemin).is_file():
        faute(f"{chemin} : fichier du code cité par la fiche absent de l'arbre extrait")
    if sha(d / chemin) != attendu:
        faute(f"{chemin} : empreinte autre que celle de la fiche de code")
print(f"{len(fichiers)} fichiers de la fiche présents, empreintes conformes")
FIN_FICHE
}
# <<< fiche-sur-l-arbre
FS=$(fiche_sur_l_arbre "$D") || arret "fiche de code sur l'arbre extrait : $FS : la garde d'entrée de la marche s'arrêterait ; arrêt avant l'installation des paquets et la descente du modèle" 2
j "fiche de code sur l'arbre extrait : $FS (contrôle avancé ; la marche rejoue sa garde d'entrée entière)"
# 4. paquets
python3 -m venv "$T/venv" && timeout -k 10 3600 "$T/venv/bin/pip" install -q -r "$D/requirements-gpu.txt" > "$X/pip.txt" 2>&1 || arret "installation des paquets" 2
PY="$T/venv/bin/python"
"$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte" 2
"$PY" -m pip freeze --all > "$X/pip-freeze.txt" 2>/dev/null
cd "$D" || arret "dépôt" 2
# 5. essais du paquet (aucun couperet de temps)
# >>> compte-des-essais (extrait et joué par tests/test_t07bbis_chaine_instance_v1.py, correction M3)
compte_passes() { local n; n=$(printf '%s\n' "$1" | grep -oE '(^|[^0-9])[0-9]+ passed' | grep -oE '[0-9]+' | head -n 1); echo "${n:-0}"; }
# <<< compte-des-essais
PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py --basetemp="$T/essais-tmp" > "$X/essais.txt" 2> "$X/essais.err"; c=$?
RES=$(tail -n 1 "$X/essais.txt")
j "essais du paquet : code $c, ligne de compte : $RES"
[ "$c" = 0 ] || arret "essais du paquet en échec (essais.txt)" 2
NP=$(compte_passes "$RES")
[ "$NP" -ge "$MIN_ESSAIS" ] || arret "essais du paquet : $NP passés < $MIN_ESSAIS attendus sur l'instance (essais.txt, sautés nommés par -rs)" 2
[ -z "$(git status --porcelain --untracked-files=all -- src tests)" ] || arret "les essais ont écrit sous src ou tests" 2
# 6. modèle au cache local
PYTHONPATH=src timeout -k 10 3600 "$PY" -c 'import json, sys
from controle_ia.harnais.modeles import precharger_modele
a = json.load(open(sys.argv[1], encoding="utf-8"))["config"]["agent"]
print(precharger_modele(a["modele"], a["revision"]))' "runs/$RUN_7B/manifeste.json" > "$X/modele.txt" 2>&1 || arret "descente du modèle" 2
j "modèle au cache local"
# 7. branche de sortie neuve (contrôle seulement : elle est créée depuis COMMIT après la marche) et poussées (chemins présents
#    seulement, ajout explicite)
git ls-remote --exit-code origin "refs/heads/$BR_SORTIE" > /dev/null 2>&1; [ $? = 2 ] || arret "branche $BR_SORTIE présente sur le dépôt distant (R12) ou dépôt injoignable" 2
SORTIE_LIBRE=1   # m-A : dès ici, tout arrêt pousse ses traces (traces_sur_commit, puis pousser une fois la branche prête)
envoyer() { local n; for n in 1 2 3; do git push -q origin "HEAD:refs/heads/$BR_SORTIE" && { j "poussé : $(git rev-parse HEAD) « $1 »"; return 0; }; sleep $((20 * n)); done
    BRANCHE_PRETE=0; arret "poussée « $1 » impossible" 4; }
pousser() {  # $1 = message ; puis chemins ; un fichier de plus de SEUIL octets arrête (la marche écrit des morceaux de moins de 90 Mo)
    local m="$1" x a=(); shift; for x in "$@"; do [ -e "$x" ] && a+=("$x"); done
    [ "${#a[@]}" -gt 0 ] || { j "rien à pousser (« $m »)"; return 0; }
    git add --sparse -f -- "${a[@]}" || { BRANCHE_PRETE=0; arret "ajout « $m »" 4; }
    while IFS= read -r -d '' x; do [ "$(stat -c %s "$x")" -le "$SEUIL" ] || { BRANCHE_PRETE=0; arret "fichier de plus de $SEUIL octets : $x (nœud)" 4; }
    done < <(git diff --cached --name-only -z --diff-filter=AM)
    if git diff --cached --quiet; then j "rien de neuf (« $m »)"; else git commit -q -m "$m" || { BRANCHE_PRETE=0; arret "commit « $m »" 4; }; envoyer "$m"; fi; }
# 8. marche (relecture forcée, apprentissage, notation, fichiers fermés), hors ligne ; une marche lente mais vivante n'est jamais
#    arrêtée hors la garde de débit
[ -z "$(git status --porcelain --untracked-files=all)" ] || arret "arbre non propre avant la marche (M1)" 2
[ "$(git rev-parse HEAD)" = "$ENTREES_LOCALES" ] || arret "tête ≠ commit local des entrées avant la marche (M1)" 2
j "marche : début (run $RUN_BBIS)"
env BBIS_INSTANCE=1 HF_HUB_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONPATH=src "$PY" -m controle_ia.t07bbis.marche_v4 \
    --racine . --run-7b "$RUN_7B" --run-bbis "$RUN_BBIS" --travail "$T/travail" ${VARIANTE_ARGS[@]+"${VARIANTE_ARGS[@]}"} \
    > "$X/marche.txt" 2> "$X/marche.err"; c=$?
j "marche : code $c"
# branche de sortie créée depuis COMMIT : le commit local des entrées (7b) n'est jamais poussé ; les sorties de la marche (non
# suivies ou ignorées) restent sur le disque
git checkout -q -b "$BR_SORTIE" "$COMMIT" || arret "branche locale de sortie depuis COMMIT (traces seules poussées)" 4
BRANCHE_PRETE=1; SORTIE_LIBRE=0
CH=("runs/$RUN_BBIS" "diag/$RUN_BBIS" "$XT")
case "$c" in
    0) traces; pousser "B bis : relecture et sondes (aucune aire), run $RUN_BBIS" "runs/$RUN_BBIS" "diag/$RUN_BBIS" "$XT"
       for f in $(find "donnees/$RUN_BBIS" -type f | sort); do pousser "B bis : $f" "$f"; done
       traces; pousser "B bis : traces de fin" "$XT"
       j "FIN : marche menée au bout, run $RUN_BBIS, tête $(git rev-parse HEAD) ; SCORES-BBIS à inscrire par la mère (diag/$RUN_BBIS/sondes-bbis.json)"
       fin_instance 0;;
    3) traces; pousser "B bis : ARRÊT DE DÉBIT (relecture et journal ; aucun score)" "${CH[@]}"
       arret "garde de débit : marche projetée au-delà de 11 h : instance arrêtée, gardée au plus 12 h, nœud de Lazar ((r1) ou (r2))" 3;;
    4) traces; pousser "B bis : ARRÊT ÉCRIT DE LA MARCHE (arret-marche-bbis.json ; aucun score)" "${CH[@]}"
       arret "marche : arrêt écrit (diag/$RUN_BBIS/arret-marche-bbis.json, marche.err)" 4;;
    *) traces; pousser "B bis : marche en arrêt, code $c" "${CH[@]}"; arret "marche : code $c (marche.err)" 4;;
esac
