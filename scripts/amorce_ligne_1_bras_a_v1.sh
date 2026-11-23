#!/usr/bin/env bash
# Amorce de la machine autonome de la ligne 1 de carte du bras A, version 1 (23 novembre 2026). Passée à la création de
# l'instance par `--onstart` (commande imprimée par `scripts/lanceur_machine_ligne_1_bras_a_v1.py creation`, sous la
# ligne de GO GO-2026-11-22-148). Aucun SSH : la machine clone sa branche d'entrée, vérifie, joue, verse sur une branche
# de sortie neuve, prouve la poussée, puis se détruit par son propre identifiant.
#
# Ordre :
#  0. heure de départ prise à la première ligne ; arguments (variables par leur NOM) ; reprise ? (fichier d'état sur le
#     disque : si l'amorce a déjà commencé, RIEN n'est relancé — R12 — : on verse l'état et on s'arrête) ;
#     heure de création retenue = AVANT_CREATION_UTC (relevée par le shell de la session juste avant la commande de
#     création : antérieure à la création, donc prudente) ; à défaut, départ de l'amorce − MARGE_S (30 min, déclarée),
#     jamais avant l'horloge du constat ; minuterie lancée ; la session recoupe par `start_date` (lanceur, `etat`) ;
#  1. clone de la seule branche d'entrée, profondeur 1, sans extraction ; aide d'identification inscrite dans la
#     configuration du clone AVANT l'extraction et toute poussée (leçon R-5101) ; commit d'entrée = COMMIT_ENTREE ;
#  2. `sha256sum --strict -c empreintes-posees.txt`, et l'arbre ne porte rien d'autre que ces fichiers : sinon
#     versement d'un échec (scellé par la bibliothèque standard : le code reçu n'est pas exécuté) et destruction ;
#  3. constat : GO, même jour UTC que la création (m1), heure du plafond ; installation (`requirements-gpu.txt` en
#     environnement virtuel), carte A100 et CUDA servie ≥ 13.0, modèle de la configuration de référence au cache
#     (`harnais.modeles.precharger_modele`, HF_TOKEN lu par son nom) ;
#  4. course (`scripts/course_ligne_1_bras_a_v2.py`, arguments de la séquence v2, section 6, `--hors-ligne`), en tâche
#     dont le PID est noté ; la minuterie l'arrête par ce PID à l'échéance (création + 6 h) ;
#  5. quel que soit le code : versement sous `diag/organismes-discrets-v-a-v2/ligne-1-<état>-<date>/` (sorties de la
#     course, course.out, constat, empreintes posées, amorce.json, journal de l'amorce), scellé par
#     `lanceur_bras_a_v8.sceller_le_versement` (manifeste de ligne minimal et manquant déclaré si le manifeste manque) ;
#  6. commit sur une branche de sortie ORPHELINE neuve (BRANCHE_SORTIE) qui ne porte que le versement ; poussée sans
#     force ; preuve : `git ls-remote` de la branche = commit local ;
#  7. poussée prouvée : destruction par l'identifiant (DELETE sur l'interface du loueur, CONTAINER_ID et
#     CONTAINER_API_KEY injectés par Vast) ; non prouvée : ARRÊT seulement (PUT state=stopped), disque gardé.
#     La minuterie détruit de toute façon à l'heure du plafond (création + (plafond − frais fixes) ÷ taux du constat).
#
# Variables (--env, par leur nom ; aucune valeur secrète n'est jamais écrite ni affichée) : GH_TOKEN, HF_TOKEN, GO_ID,
#   BRANCHE_ENTREE, BRANCHE_SORTIE, COMMIT_ENTREE, AVANT_CREATION_UTC (facultative mais attendue), AMORCE_SHA256
#   (facultative, seulement comparée et écrite) ; posées par Vast : CONTAINER_ID, CONTAINER_API_KEY.
# Mode jouet (AMORCE_JOUET=1, essais sur processeur seulement) : RACINE_AMORCE, AMORCE_DEPOT_URL, AMORCE_CURL,
#   AMORCE_PYTHON, AMORCE_ECHEANCE_S, AMORCE_PLAFOND_S, AMORCE_PAS_S, JOUET_CONFIGURATION, JOUET_PLAN,
#   JOUET_INJECTEUR, JOUET_CONSTANTES ; pas d'installation, pas de carte, pas de modèle téléchargé ; course en
#   `--mode jouet` ; sortie du processus au lieu d'attendre la fin du conteneur. Hors jouet, chacune est refusée.
[ -n "${BASH_VERSION:-}" ] || exec bash "$0" "$@"     # jouée par sh : reprise par bash
set +x
set -uo pipefail
DEBUT_S=$(date -u +%s)
JOUET="${AMORCE_JOUET:-0}"
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
if [ "$JOUET" != 1 ]; then
    for v in RACINE_AMORCE AMORCE_DEPOT_URL AMORCE_CURL AMORCE_PYTHON AMORCE_ECHEANCE_S AMORCE_PLAFOND_S AMORCE_PAS_S \
             JOUET_CONFIGURATION JOUET_PLAN JOUET_INJECTEUR JOUET_CONSTANTES; do
        [ -z "${!v:-}" ] || { echo "LIGNE-1 REFUS : $v n'est admise qu'en mode jouet"; exit 2; }; done
fi
R="${RACINE_AMORCE:-/root}"
T="$R/ligne-1-bras-a"; E="$T/entree"; S="$T/sorties-ligne-1"; M="$T/etat"; L="$T/journal-amorce.txt"
API=https://console.vast.ai/api/v0
DEPOT_URL="${AMORCE_DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
CURL="${AMORCE_CURL:-curl}"
PYS="${AMORCE_PYTHON:-python3}"          # python du système : bibliothèque standard seulement, en mode isolé (-I)
PAS="${AMORCE_PAS_S:-30}"
GO_ATTENDU=GO-2026-11-22-148
BR_ENTREE="${BRANCHE_ENTREE:-entree/bras-a-ligne-1-v1}"
BR_SORTIE="${BRANCHE_SORTIE:-calcul/bras-a-ligne-1-v1}"
DUREE_MAX_S=21600                        # échéance : création + 6 h
MARGE_S=1800                             # départ de l'amorce − 30 min : borne prudente de la création (déclarée)
LANCEUR_SHA=2663d32d39133ab1a96cb7a694baf7908c005c37e835d9f17cff2d578bc6344b
LANCEUR=src/controle_ia/organismes_discrets/lanceur_bras_a_v8.py
CONFIGURATION=prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json
PLAN=docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v2.json
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
export GH_TOKEN="${GH_TOKEN:-}" HF_TOKEN="${HF_TOKEN:-}"

# --- journal masqué : aucune valeur secrète n'y entre, même par accident --------------------------------------------
masquer() { local t="$1" v
    for v in "${GH_TOKEN:-}" "${HF_TOKEN:-}" "${CONTAINER_API_KEY:-}"; do
        [ "${#v}" -ge 4 ] && t="${t//"$v"/[masqué]}"; done
    printf '%s' "$t"; }
j() { local l; l="$(date -u +%FT%TZ) LIGNE-1 $(masquer "$*")"
    printf '%s\n' "$l" >> "$L" 2>/dev/null; printf '%s\n' "$l"; }
masquer_fichier() {  # remplace en place, dans un fichier texte, les valeurs des trois secrets lues par leur nom
    [ -f "$1" ] || return 0
    "$PYS" -I -c 'import os,sys
p=sys.argv[1]; b=open(p,"rb").read()
for n in ("GH_TOKEN","HF_TOKEN","CONTAINER_API_KEY"):
    v=os.environ.get(n,"").encode()
    if len(v)>=4: b=b.replace(v,"[masqué]".encode())
open(p,"wb").write(b)' "$1" || j "masquage de $1 en échec"; }
etat() { printf '%s\n' "${2:-$(date -u +%FT%TZ)}" > "$M/$1"; }
a_etat() { [ -e "$M/$1" ]; }
lire_etat() { head -n 1 "$M/$1" 2>/dev/null; }

# --- interface du loueur : clé passée par l'entrée standard (`curl -K -`), jamais sur la ligne de commande -------------
appel_api() {  # $1 méthode, $2 corps JSON ou vide ; imprime le code HTTP
    local c
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo 000; return 1;; esac
    if [ -n "$2" ]; then
        c=$(printf 'header = "Authorization: Bearer %s"\n' "${CONTAINER_API_KEY:-}" | "$CURL" -K - -sS -m 60 -o /dev/null \
            -w '%{http_code}' -X "$1" -H 'Content-Type: application/json' -d "$2" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    else
        c=$(printf 'header = "Authorization: Bearer %s"\n' "${CONTAINER_API_KEY:-}" | "$CURL" -K - -sS -m 60 -o /dev/null \
            -w '%{http_code}' -X "$1" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    fi
    printf '%s\n' "$c"; }
detruire() {  # $1 motif. Une destruction ne se juge pas à son code : tant que ce processus vit, on redemande (R10)
    local n=0 c
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) j "DESTRUCTION IMPOSSIBLE : identifiant de l'instance illisible ; la session détruit par l'identifiant"; fin 4;; esac
    while :; do n=$((n + 1))
        c=$(appel_api DELETE "")
        j "DESTRUCTION de l'instance $CONTAINER_ID par son identifiant ($1) : DELETE, essai $n : HTTP $c"
        if [ "$JOUET" = 1 ]; then case "$c" in 2??) j "JOUET : destruction simulée, fin"; exit 0;; esac; fi
        if [ "$n" -ge 5 ] && [ $((n % 5)) = 0 ]; then
            c=$(appel_api PUT '{"state": "stopped"}'); j "instance toujours vivante après $n demandes : arrêt demandé, HTTP $c"; fi
        [ "$JOUET" = 1 ] && [ "$n" -ge 3 ] && { j "JOUET : destruction non obtenue après 3 essais"; exit 5; }
        sleep 60; done; }
arreter() {  # $1 motif : arrêt simple (disque gardé), jamais une destruction
    local c
    c=$(appel_api PUT '{"state": "stopped"}')
    j "ARRÊT (state=stopped) demandé, disque gardé ($1) : HTTP $c ; la session lit l'état, rapatrie ou repousse, puis détruit par l'identifiant"
    fin 3; }
fin() { etat fin "$1"; if [ "$JOUET" = 1 ]; then exit "$1"; fi; sleep infinity; exit "$1"; }

# --- 0. arguments ----------------------------------------------------------------------------------------------------
mkdir -p "$M" || { echo "LIGNE-1 REFUS : $M impossible"; exit 2; }
REPRISE=0; a_etat amorce-commencee && REPRISE=1
j "amorce v1 : départ $(date -u -d "@$DEBUT_S" +%FT%TZ), reprise $REPRISE, jouet $JOUET ; empreinte $(sha256sum < "$0" 2>/dev/null | cut -c1-64) (attendue ${AMORCE_SHA256:-non donnée})"
for o in git "$CURL" "$PYS" sha256sum awk sed grep date; do command -v "$o" > /dev/null || { j "outil absent : $o"; fin 2; }; done
ERREUR=""
[ "${GO_ID:-}" = "$GO_ATTENDU" ] || ERREUR="GO_ID ${GO_ID:-absent} ≠ $GO_ATTENDU"
case "${COMMIT_ENTREE:-}" in *[!0-9a-f]*|'') ERREUR="${ERREUR:+$ERREUR ; }COMMIT_ENTREE illisible";; esac
C="${COMMIT_ENTREE:-}"; [ "${#C}" = 40 ] || ERREUR="${ERREUR:+$ERREUR ; }COMMIT_ENTREE de 40 signes exigé"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) ERREUR="${ERREUR:+$ERREUR ; }CONTAINER_ID non numérique";; esac
[ -n "${CONTAINER_API_KEY:-}" ] || ERREUR="${ERREUR:+$ERREUR ; }CONTAINER_API_KEY absente (par le nom)"
[ -n "${GH_TOKEN:-}" ] || ERREUR="${ERREUR:+$ERREUR ; }GH_TOKEN absent (par le nom)"
[ "$JOUET" = 1 ] || [ -n "${HF_TOKEN:-}" ] || ERREUR="${ERREUR:+$ERREUR ; }HF_TOKEN absent (par le nom)"
for b in "$BR_ENTREE" "$BR_SORTIE"; do
    printf '%s' "$b" | LC_ALL=C grep -qxE '[a-z0-9][a-z0-9/._-]*[a-z0-9]' && [ "${b#*..}" = "$b" ] || ERREUR="${ERREUR:+$ERREUR ; }branche $b illisible"; done
[ "$BR_ENTREE" != "$BR_SORTIE" ] || ERREUR="${ERREUR:+$ERREUR ; }branches d'entrée et de sortie confondues"

# --- heure de création retenue et minuterie ------------------------------------------------------------------------------
instant_s() { date -u -d "$(printf '%s' "$1" | sed 's/T/ /; s/Z$//')" +%s 2>/dev/null; }
if [ "$REPRISE" = 0 ]; then
    CREATION_S=$((DEBUT_S - MARGE_S)); SOURCE_CREATION="départ de l'amorce − $MARGE_S s"
    if [ -n "${AVANT_CREATION_UTC:-}" ]; then
        if printf '%s' "$AVANT_CREATION_UTC" | grep -qxE '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z' \
                && a=$(instant_s "$AVANT_CREATION_UTC") && [ "$a" -le "$DEBUT_S" ]; then
            CREATION_S=$a; SOURCE_CREATION="AVANT_CREATION_UTC (relevée juste avant la commande de création)"
        else ERREUR="${ERREUR:+$ERREUR ; }AVANT_CREATION_UTC illisible ou postérieure au départ de l'amorce"; fi
    fi
    etat creation-s "$CREATION_S"; etat source-creation "$SOURCE_CREATION"
    ECH=$((CREATION_S + ${AMORCE_ECHEANCE_S:-$DUREE_MAX_S}))
    PLAF=$((CREATION_S + ${AMORCE_PLAFOND_S:-$((DUREE_MAX_S + 3600))}))   # provisoire, refaite avec le constat
    etat echeance-s "$ECH"; etat plafond-s "$PLAF"
    etat amorce-commencee
else
    CREATION_S=$(lire_etat creation-s); SOURCE_CREATION=$(lire_etat source-creation)
    case "$CREATION_S" in ''|*[!0-9]*) CREATION_S=$((DEBUT_S - MARGE_S)); etat creation-s "$CREATION_S";; esac
fi
minuterie() {  # lit l'échéance et l'heure du plafond sur le disque à chaque pas
    local e p pid
    while :; do e=$(lire_etat echeance-s); p=$(lire_etat plafond-s)
        if [ "$(date -u +%s)" -ge "$p" ]; then
            j "MINUTERIE : heure du plafond atteinte : destruction quel que soit l'état du versement"; detruire "heure du plafond"; fi
        if [ "$(date -u +%s)" -ge "$e" ] && ! a_etat echeance-atteinte; then
            etat echeance-atteinte; j "MINUTERIE : échéance atteinte (création + 6 h) : l'étape en cours est arrêtée par son PID"
            pid=$(lire_etat etape-pid)
            case "$pid" in ''|*[!0-9]*) ;; *) kill -TERM "$pid" 2>/dev/null && j "MINUTERIE : TERM envoyé au PID $pid"
                sleep "$PAS"; kill -0 "$pid" 2>/dev/null && kill -KILL "$pid" 2>/dev/null && j "MINUTERIE : KILL envoyé au PID $pid";; esac
        fi
        sleep "$PAS"; done; }
minuterie < /dev/null > /dev/null 2>&1 &
MINUTERIE_PID=$!
trap 'kill "$MINUTERIE_PID" 2>/dev/null' EXIT
j "création retenue $(date -u -d "@$CREATION_S" +%FT%TZ) ($SOURCE_CREATION) ; échéance $(date -u -d "@$(lire_etat echeance-s)" +%FT%TZ) ; destruction forcée au plus tard $(date -u -d "@$(lire_etat plafond-s)" +%FT%TZ) ; minuterie PID $MINUTERIE_PID"
echeance_passee() { [ "$(date -u +%s)" -ge "$(lire_etat echeance-s)" ] || a_etat echeance-atteinte; }
etape_longue() {  # $1 fichier de sortie ; la suite : la commande. PID noté pour la minuterie ; rend le code
    local f="$1" pid c; shift
    if echeance_passee; then j "échéance passée : étape non lancée"; return 124; fi
    "$@" > "$f" 2>&1 < /dev/null & pid=$!
    etat etape-pid "$pid"; wait "$pid"; c=$?; rm -f "$M/etape-pid"; masquer_fichier "$f"; return "$c"; }

# --- versement, poussée, preuve ------------------------------------------------------------------------------------------
sceller_stdlib() {  # $1 dossier ; $2 motif ; manifeste du versement au format de `sceller_le_versement`, sans le code reçu
    "$PYS" -I - "$1" "$2" <<'PYFIN'
import hashlib, json, sys
from pathlib import Path
d, motif = Path(sys.argv[1]), sys.argv[2]
nom = "manifeste-du-versement.json"
inv = []
for p in sorted(d.rglob("*")):
    if p.is_symlink():
        sys.exit(f"lien symbolique {p}")
    if p.is_file() and p.relative_to(d).as_posix() not in (nom, nom + ".sha256"):
        inv.append({"nom": p.relative_to(d).as_posix(), "taille": p.stat().st_size,
                    "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
contenu = {"inventaire": inv,
           "manifeste_de_la_ligne": {"ligne": 1, "manifeste": "absent", "scelle_par": "amorce, bibliothèque standard",
                                     "pourquoi": motif},
           "manquants": [{"nom": "manifeste-de-la-ligne-1.json", "pourquoi": motif}]}
texte = json.dumps(contenu, ensure_ascii=False, sort_keys=True, indent=1, allow_nan=False)
with open(d / nom, "x", encoding="utf-8") as f:
    f.write(texte)
h = hashlib.sha256((d / nom).read_bytes()).hexdigest()
(d / (nom + ".sha256")).write_text(f"{h}  {nom}\n", encoding="utf-8")
print(h)
PYFIN
}
sceller_lanceur() {  # $1 dossier ; $2 motif d'absence du manifeste ; par le lanceur v8 du clone vérifié
    (cd "$E" && PYTHONPATH=src "$PYV" - "$1" "$2" <<'PYFIN'
import json, sys
from pathlib import Path
from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la
d, motif = Path(sys.argv[1]), sys.argv[2]
m = d / "manifeste-de-la-ligne-1.json"
if m.is_file():
    print(la.sceller_le_versement(d, json.loads(m.read_text(encoding="utf-8")), manquants=[]))
else:
    j = d / "journal-course-ligne-1.txt"
    queue = j.read_text(encoding="utf-8", errors="replace").splitlines()[-20:] if j.is_file() else []
    print(la.sceller_le_versement(d, {"ligne": 1, "manifeste": "absent", "journal": queue},
                                  manquants=[{"nom": "manifeste-de-la-ligne-1.json", "pourquoi": motif}]))
PYFIN
    ); }
verser() {  # $1 état (fini, arret, echec, reprise), $2 motif ; prépare, scelle et committe sur la branche orpheline
    local etat_v="$1" motif="$2" G VREL VD sha
    G="$T/sortie-git-$(date -u +%Y%m%dT%H%M%SZ)"
    VREL="diag/organismes-discrets-v-a-v2/ligne-1-$etat_v-$(date -u +%Y%m%dT%H%M%SZ)"; VD="$G/$VREL"
    mkdir -p "$VD" || return 1
    if [ -d "$S" ]; then cp -a "$S/." "$VD/" || return 1; fi
    for f in "$T/course.out" "$T/installation.txt" "$T/modele.txt" "$T/verification-empreintes.txt"; do
        [ -f "$f" ] && { masquer_fichier "$f"; cp "$f" "$VD/"; }; done
    [ -f "$E/constat-ligne-1.json" ] && cp "$E/constat-ligne-1.json" "$VD/"
    [ -f "$E/empreintes-posees.txt" ] && cp "$E/empreintes-posees.txt" "$VD/"
    "$PYS" -I -c 'import json,sys; print(json.dumps(dict(zip(sys.argv[1::2], sys.argv[2::2])), ensure_ascii=False, indent=1))' \
        etat "$etat_v" motif "$motif" commit_entree "${COMMIT_ENTREE:-}" commit_source "${COMMIT_SOURCE:-}" \
        branche_entree "$BR_ENTREE" branche_sortie "$BR_SORTIE" instance "${CONTAINER_ID:-}" \
        creation_retenue_utc "$(date -u -d "@$CREATION_S" +%FT%TZ)" source_creation "$SOURCE_CREATION" marge_s "$MARGE_S" \
        avant_creation_utc "${AVANT_CREATION_UTC:-}" depart_amorce_utc "$(date -u -d "@$DEBUT_S" +%FT%TZ)" \
        echeance_utc "$(date -u -d "@$(lire_etat echeance-s)" +%FT%TZ)" plafond_utc "$(date -u -d "@$(lire_etat plafond-s)" +%FT%TZ)" \
        code_course "$(lire_etat code-course)" reprise "$REPRISE" amorce_sha256 "$(sha256sum < "$0" | cut -c1-64)" \
        amorce_sha256_attendue "${AMORCE_SHA256:-}" > "$VD/amorce.json" || return 1
    j "versement $VREL : scellement"
    cp "$L" "$VD/journal-amorce.txt"; masquer_fichier "$VD/journal-amorce.txt"
    if a_etat entree-verifiee && [ -n "${PYV:-}" ] && sha=$(sceller_lanceur "$VD" "$motif" 2> "$T/scellement.txt"); then
        j "versement scellé par le lanceur v8 : $sha"
    else
        [ -s "$T/scellement.txt" ] && j "scellement par le lanceur impossible : $(tail -n 1 "$T/scellement.txt" | cut -c1-300)"
        rm -f "$VD/manifeste-du-versement.json" "$VD/manifeste-du-versement.json.sha256"
        sha=$(sceller_stdlib "$VD" "$motif") || { j "scellement impossible"; return 1; }
        j "versement scellé par la bibliothèque standard (code reçu non vérifié ou lanceur indisponible) : $sha"
    fi
    git init -q -b "$BR_SORTIE" "$G" && git -C "$G" config user.name "machine de la ligne 1 (bras A)" \
        && git -C "$G" config user.email machine-ligne-1@invalid && git -C "$G" config credential.helper "$AIDE" \
        && git -C "$G" remote add origin "$DEPOT_URL" && git -C "$G" add -- "$VREL" \
        && git -C "$G" commit -q -m "Ligne 1 de carte du bras A : versement $etat_v (instance ${CONTAINER_ID:-?}, entrée ${COMMIT_ENTREE:-?})" \
        || { j "commit du versement impossible"; return 1; }
    etat depot-sortie "$G"; etat commit-sortie "$(git -C "$G" rev-parse HEAD)"
    j "versement committé : $(lire_etat commit-sortie) sur $BR_SORTIE (orpheline)"; }
pousser_et_prouver() {  # rend 0 seulement si `git ls-remote` de la branche de sortie = commit local
    local G c n lu
    G=$(lire_etat depot-sortie); c=$(lire_etat commit-sortie)
    [ -d "$G" ] && [ -n "$c" ] || return 1
    for n in 1 2 3; do
        git -C "$G" push -q origin "$c:refs/heads/$BR_SORTIE" > "$T/poussee.txt" 2>&1 \
            || { masquer_fichier "$T/poussee.txt"; j "poussée, essai $n : refusée ($(grep -v '^ *$' "$T/poussee.txt" | tail -n 1 | cut -c1-200))"; }
        lu=$(git -C "$G" ls-remote origin "refs/heads/$BR_SORTIE" 2>/dev/null | awk 'NR == 1 { print $1 }')
        if [ -n "$lu" ] && [ "$lu" = "$c" ]; then etat poussee-prouvee "$c"; j "POUSSÉE PROUVÉE : $BR_SORTIE = $c"; return 0; fi
        j "poussée non prouvée (essai $n) : distant « ${lu:-absent} », local $c"
        [ "$n" = 3 ] || sleep $(( PAS * n )); done
    return 1; }
conclure() {  # $1 état, $2 motif : verse (sauf si déjà fait), pousse, prouve, puis détruit ; sinon arrêt seulement
    if a_etat poussee-prouvee; then detruire "versement déjà prouvé"; fi
    if ! a_etat commit-sortie; then verser "$1" "$2" || { j "VERSEMENT EN ÉCHEC"; arreter "versement en échec"; }; fi
    if pousser_et_prouver; then detruire "versement prouvé sur $BR_SORTIE"; fi
    arreter "poussée non prouvée"; }

# --- reprise : rien n'est relancé ----------------------------------------------------------------------------------------
if [ "$REPRISE" = 1 ]; then
    j "REPRISE après redémarrage : aucune étape n'est relancée (R12) ; état versé puis fin"
    [ -x "$T/venv/bin/python" ] && PYV="$T/venv/bin/python" || PYV="$PYS"
    [ "$JOUET" = 1 ] && PYV="$PYS"
    COMMIT_SOURCE=$(lire_etat commit-source)
    conclure reprise "redémarrage du conteneur pendant ou après la course : rien n'est relancé"
fi
[ -z "$ERREUR" ] || { j "REFUS DES ARGUMENTS : $ERREUR"; conclure echec "arguments : $ERREUR"; }

# --- 1. clone de la seule branche d'entrée --------------------------------------------------------------------------------
[ ! -e "$E" ] || { j "$E existe déjà (R12)"; conclure echec "dossier d'entrée déjà présent"; }
if ! git -c credential.helper="$AIDE" clone -q --depth 1 --single-branch --no-checkout --branch "$BR_ENTREE" \
        "$DEPOT_URL" "$E" > "$T/clone.txt" 2>&1; then
    masquer_fichier "$T/clone.txt"; j "clone en échec : $(tail -n 1 "$T/clone.txt" | cut -c1-200)"; conclure echec "clone de $BR_ENTREE en échec"
fi
git -C "$E" config credential.helper "$AIDE"        # avant toute extraction et toute poussée (R-5101)
git -C "$E" checkout -q "$BR_ENTREE" > "$T/clone.txt" 2>&1 || { j "extraction en échec"; conclure echec "extraction en échec"; }
LU=$(git -C "$E" rev-parse HEAD)
[ "$LU" = "$COMMIT_ENTREE" ] || { j "commit d'entrée $LU ≠ COMMIT_ENTREE $COMMIT_ENTREE"; conclure echec "commit d'entrée différent de celui attendu"; }
COMMIT_SOURCE=$(git -C "$E" log -1 --format=%B | sed -n 's/^Commit-source: \([0-9a-f]\{40\}\)$/\1/p' | head -n 1)
[ "${#COMMIT_SOURCE}" = 40 ] || { j "Commit-source absent du message d'entrée"; conclure echec "commit source illisible"; }
etat commit-source "$COMMIT_SOURCE"
j "entrée clonée : $BR_ENTREE = $LU (source $COMMIT_SOURCE)"

# --- 2. empreintes posées ------------------------------------------------------------------------------------------------
if ! (cd "$E" && sha256sum --strict --quiet -c empreintes-posees.txt) > "$T/verification-empreintes.txt" 2>&1; then
    j "EMPREINTES POSÉES NON CONFORMES : $(head -n 3 "$T/verification-empreintes.txt" | tr '\n' ' ' | cut -c1-300)"
    conclure echec "empreintes posées non conformes : code reçu non exécuté"
fi
ATTENDUS=$(awk '{ print substr($0, 67) }' "$E/empreintes-posees.txt"; echo empreintes-posees.txt)
if [ "$(printf '%s\n' "$ATTENDUS" | LC_ALL=C sort)" != "$(git -C "$E" ls-tree -r --name-only HEAD | LC_ALL=C sort)" ]; then
    j "l'arbre d'entrée porte d'autres fichiers que ceux des empreintes posées"; conclure echec "arbre d'entrée hors liste"
fi
etat entree-verifiee; j "empreintes posées conformes ($(grep -c . "$E/empreintes-posees.txt") fichiers), arbre sans autre fichier"
PYV="$PYS"

# --- 3. constat, échéances, installation, carte, modèle ------------------------------------------------------------------
if ! INFO=$("$PYS" -I - "$E/constat-ligne-1.json" "$CREATION_S" "$GO_ATTENDU" <<'PYFIN'
import json, math, sys
from datetime import datetime, timezone
c = json.load(open(sys.argv[1], encoding="utf-8")); creation = int(sys.argv[2])
if c["go"]["go"] != sys.argv[3]:
    sys.exit("GO du constat différent")
constat = int(datetime.strptime(c["maintenant_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())
t = c["tarifs"]; taux = t["carte_usd_h"] + t["stockage_usd_h"]; fixes = t["telechargement_usd_go"] * 40
print(constat, math.floor((c["plafond_usd"] - fixes) / taux * 3600))
PYFIN
); then j "constat illisible ou d'un autre GO"; conclure echec "constat illisible ou d'un autre GO"; fi
CONSTAT_S=${INFO% *}; DUREE_PLAFOND_S=${INFO#* }
if [ "$CREATION_S" -lt "$CONSTAT_S" ]; then
    # AVANT_CREATION_UTC antérieure au constat : la commande de création a précédé le constat — hors séquence, refus
    [ -z "${AVANT_CREATION_UTC:-}" ] || { j "AVANT_CREATION_UTC antérieure au constat"; conclure echec "création relevée avant le constat de départ"; }
    CREATION_S=$CONSTAT_S; SOURCE_CREATION="$SOURCE_CREATION, relevée à l'horloge du constat (la création suit le constat)"
    etat creation-s "$CREATION_S"; etat source-creation "$SOURCE_CREATION"; fi
JOUR_CREATION=$(date -u -d "@$DEBUT_S" +%F); [ -n "${AVANT_CREATION_UTC:-}" ] && JOUR_CREATION=${AVANT_CREATION_UTC%%T*}
if [ "$JOUR_CREATION" != "$(date -u -d "@$CONSTAT_S" +%F)" ]; then
    j "création ($JOUR_CREATION) hors du jour UTC du constat (m1)"; conclure echec "création hors du jour UTC du constat (m1)"; fi
# échéance et heure du plafond refaites sur la création retenue et le taux du constat (remplacent les provisoires)
etat plafond-s "$((CREATION_S + ${AMORCE_PLAFOND_S:-$DUREE_PLAFOND_S}))"
etat echeance-s "$((CREATION_S + ${AMORCE_ECHEANCE_S:-$DUREE_MAX_S}))"
CREATION_UTC=$(date -u -d "@$CREATION_S" +%FT%TZ)
j "constat $(date -u -d "@$CONSTAT_S" +%FT%TZ) ; création retenue $CREATION_UTC ; échéance $(date -u -d "@$(lire_etat echeance-s)" +%FT%TZ) ; destruction forcée $(date -u -d "@$(lire_etat plafond-s)" +%FT%TZ)"
if [ "$JOUET" != 1 ]; then
    nvidia-smi > "$T/nvidia-smi.txt" 2>&1 || { j "carte invisible (nvidia-smi)"; conclure echec "carte invisible"; }
    grep -q 'A100' "$T/nvidia-smi.txt" || { j "carte autre qu'une A100"; conclure echec "carte autre qu'une A100"; }
    V=$(sed -n 's/^.*CUDA Version: *\([0-9][0-9]*\)\.[0-9][0-9]*.*$/\1/p' "$T/nvidia-smi.txt" | head -n 1)
    case "$V" in ''|*[!0-9]*) j "version CUDA du pilote illisible"; conclure echec "CUDA du pilote illisible";; esac
    [ "$V" -ge 13 ] || { j "CUDA du pilote $V < 13"; conclure echec "pilote trop ancien"; }
    etape_longue "$T/installation.txt" bash -c "python3 -m venv '$T/venv' && '$T/venv/bin/pip' install -q -r '$E/requirements-gpu.txt'" \
        || { j "installation en échec"; conclure echec "installation des paquets en échec"; }
    PYV="$T/venv/bin/python"
    etape_longue "$T/modele.txt" env -u GH_TOKEN -u CONTAINER_API_KEY bash -c "cd '$E' && PYTHONPATH=src '$PYV' -c 'import json, sys
from controle_ia.harnais.modeles import precharger_modele
c = json.load(open(sys.argv[1], encoding=\"utf-8\"))[\"agent\"]
print(precharger_modele(c[\"modele\"], c[\"revision\"]))' prereg/T0.6-organismes-config-7b-v1.json" \
        || { j "téléchargement du modèle en échec"; conclure echec "téléchargement du modèle en échec"; }
    j "paquets installés, modèle au cache"
fi

# --- 4. course -----------------------------------------------------------------------------------------------------------
ARGS=(--configuration "${JOUET_CONFIGURATION:-$CONFIGURATION}" --lanceur-chemin "$LANCEUR" --lanceur-sha256 "$LANCEUR_SHA"
      --constat constat-ligne-1.json --plan-scelle "${JOUET_PLAN:-$PLAN}" --creation-instance-utc "$CREATION_UTC"
      --dossier "$S" --commit "$COMMIT_SOURCE")
if [ "$JOUET" = 1 ]; then ARGS+=(--mode jouet); PRE=(); [ -n "${JOUET_INJECTEUR:-}" ] && PRE=("$JOUET_INJECTEUR" "$JOUET_CONSTANTES")
else ARGS+=(--mode reel --hors-ligne); PRE=(); fi
etat course-lancee
j "course lancée (mode $([ "$JOUET" = 1 ] && echo jouet || echo réel), création $CREATION_UTC, commit $COMMIT_SOURCE)"
(cd "$E" && etape_longue "$T/course.out" env -u GH_TOKEN -u HF_TOKEN -u CONTAINER_API_KEY PYTHONPATH=src \
    "$PYV" "${PRE[@]}" scripts/course_ligne_1_bras_a_v2.py "${ARGS[@]}")
CODE=$?
etat code-course "$CODE"
case "$CODE" in
    0) ETAT_V=fini; MOTIF="ligne jouée (code 0)";;
    124) ETAT_V=arret; MOTIF="échéance passée avant le lancement de la course";;
    *) if a_etat echeance-atteinte; then ETAT_V=arret; MOTIF="course arrêtée par la minuterie à l'échéance (code $CODE)"
       else ETAT_V=arret; MOTIF="course terminée sur le code $CODE"; fi;;
esac
j "FIN DE LA COURSE : code $CODE ; $MOTIF"
conclure "$ETAT_V" "$MOTIF"
