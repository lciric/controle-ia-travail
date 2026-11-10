#!/usr/bin/env bash
# Brouillon 2 (2026-11-10, contre-lecture différentielle, CD-05) : clone en extraction partielle (aucun chemin interdit
# extrait : docs/notes/bras-attaque/ et ceux de la règle 1 des interdits communs v2), absence vérifiée, refus sinon.
# Contrôles avant dépense de P3-bis (témoin positif planté ; GO-2026-11-10-02, prolongation de GO-2026-11-02-29 jusqu'au 2026-11-23 : R-2077), v1. Texte qui fait foi : brouillon 9
# (eb65773f…), en-tête, « Liste d'arrêt », plan, points 2, 6 et 11, « Ce que le code et la chaîne doivent changer »,
# points 1 à 6 ; contre-lecture du code (7a074ad1…), point 6. Déclinés de docs/procedures/P3-premier-test-v2/
# controles_avant_depense_p3_v1.sh (P3) sous un nom neuf (R12). Sur un clone neuf du dépôt de travail au commit de
# scellement S ; aucun calcul payant ; code 0 si et seulement si tout est conforme ; code 2 si les épingles manquent ou
# sont mal formées, si le module commun manque, ou si le clone est impossible. Aucun délai.
# Ce qui est contrôlé (chaque bloc écrit OK ou KO ; dernière ligne « CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES ») :
#   1  S ajoute le sceau du texte et n'ajoute que le texte, la configuration, les consignes et leurs sceaux ;
#   2  commit du code cité une seule fois, ancêtre de S, égal au code relu épinglé ; arbre gelé de S (CHEMINS_GELES)
#      identique au commit du code (« commit cité égal à l'arbre gelé du commit de scellement ») ;
#   3  identité avec P3 : `git diff --name-status 7a54d431… <code>` sur les chemins de l'en-tête ne montre que des ajouts ;
#   4  texte scellé SANS MARQUEUR (aucun « <<…>> », problemes() vide) ; sceaux du texte, de la configuration, des
#      consignes et des tâches ; texte, configuration et consignes égaux aux candidats relus, octet pour octet ;
#   5  GO : module commun (GO-2026-11-10-02 seul, une ligne au registre de S, plafond 80 USD, échéance 2026-11-23,
#      aucune révocation au sens exact du texte, jour au plus tard le 23 novembre 2026) ; garde de calcul sur le
#      registre de S ;
#   6  ESSAI DIFFÉRENTIEL DE FERMETURE : sortie versée à S, à l'empreinte épinglée, scellée, citée par le texte, dernière
#      ligne « ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME », aucune ligne « NON CONFORME » ; puis REJOUÉ au commit S (dont
#      l'arbre gelé est le commit du code) : même dernière ligne, sinon aucune création ;
#   7  LONGUEURS : remesurées au vrai tokeniseur de l'agent (A, T, B ; consigne et indication, seules et dans le gabarit ;
#      60 tâches) : A = T tâche par tâche, résumé égal aux longueurs attendues versées à S (épinglées) ; mesure citée ;
#   8  COMPTE N DES ESSAIS : N cité une fois ; liste ciblée d'empreinte égale à celle écrite dans le script de l'instance ;
#      liste jouée au commit S dans l'environnement PY : « N passed » exact, sans essai sauté ni en échec ; versions de
#      PY égales aux dépendances épinglées de S ;
#   9  configuration : seuls écarts à P3 ceux du texte (module commun) ; gardes du lanceur run_v2 rejouées dans l'ordre
#      d'executer(), jusqu'au manifeste (rien n'est écrit) ;
#   10 valeurs de P3-bis citées par le texte (bloc des valeurs : 2,10 USD, 0,98, 30 cœurs, 80 USD, 23 novembre, durées
#      nulles, aucun `timeout`, …) et constantes de la chaîne versée égales à celles du module commun ;
#   11 scripts de l'instance (noms v2) : présents à S, cités par leur empreinte, aucune commande `timeout`, lanceur
#      run_v2, liste ciblée v2, dépôt de travail par défaut (jamais la copie publique) ;
#   12 lecture précoce : citations lues par le script de l'instance une fois chacune, chemins attendus ; intitulés lus
#      une fois chacun ; ligne « Lancement » (PREREG, BRANCHE, DEPOT_URL du dépôt de travail) ;
#   13 branche de calcul (troisième argument) absente du dépôt distant ;
#   14 rapports des contre-lectures épinglés : présents à S, scellés, cités ; verifier-arbre.
# Usage : controles_avant_depense_p3bis_v1.sh S DOSSIER_NEUF BRANCHE
set -uo pipefail
[ $# -eq 3 ] || { echo "usage : controles_avant_depense_p3bis_v1.sh S DOSSIER_NEUF BRANCHE (trois arguments)"; exit 2; }
S=$1; D=$(realpath -m "$2"); BRANCHE=$3
DEPOT_URL=https://github.com/lciric/controle-ia-travail.git
# --- épingles du candidat (« A_EPINGLER » tant que le candidat n'existe pas : tout lancement est refusé) --------------
CANDIDAT_RELU=A_EPINGLER                         # texte relu (contre-lecture 4), octet pour octet
CANDIDAT_RELU_CHEMIN=A_EPINGLER
CONFIG_RELUE=A_EPINGLER
CONFIG_RELUE_CHEMIN=A_EPINGLER
CONSIGNES_RELUES=A_EPINGLER
CONSIGNES_RELUES_CHEMIN=A_EPINGLER
CODE_RELU=A_EPINGLER                             # commit du code corrigé, relu (40 caractères)
ESSAI_FERMETURE=A_EPINGLER                       # empreinte de la sortie versée de l'essai différentiel de fermeture
ESSAI_FERMETURE_CHEMIN=A_EPINGLER
LONGUEURS_ATTENDUES=A_EPINGLER                   # empreinte du résumé des longueurs attendues (JSON, forme de resume_longueurs)
LONGUEURS_ATTENDUES_CHEMIN=A_EPINGLER
RAPPORTS_ATTENDUS=A_EPINGLER                     # paires chemin=empreinte des rapports de contre-lecture cités par le texte
PY=A_EPINGLER                                    # interpréteur d'un environnement aux dépendances épinglées de S
# --- constantes de P3-bis --------------------------------------------------------------------------------------------
# extraction partielle de tout clone de la chaîne (interdits communs v2, règle 9 ; contre-lecture différentielle, CD-05) :
# aucun chemin interdit n'est jamais extrait, donc jamais haché par verifier-arbre ; absence vérifiée sur disque
EXTRACTION=('/*' '!/docs/notes/bras-attaque/' '!/diag/20261109-070232-t06-reel/' '!/runs/20261109-070232-t06-reel/' '!/donnees/bras-attaque*' '!/donnees/mode-tenu-a-l-ecart*' '!/diag/*/lecture-sondes-t06.json*' '!/scripts/extraire_mesures_epreuve_t06_v1.py*')
ABSENTS=(docs/notes/bras-attaque diag/20261109-070232-t06-reel runs/20261109-070232-t06-reel scripts/extraire_mesures_epreuve_t06_v1.py)
H=$(dirname "$(realpath "$0")")
VERIF=$H/verifications_p3bis_v1.py
VERSEES=docs/procedures/P3-bis-temoin-positif-v1
CODE_P3=7a54d431d89745839220f882b41b13e8c62ecfdd                 # commit du code de P3 (identité, en-tête du texte)
CHEMINS_IDENTITE="src/controle_ia/premier_test_ia src/controle_ia/sondes src/controle_ia/harnais src/controle_ia/environnements src/controle_ia/organismes src/controle_ia/bases src/controle_ia/manifeste.py src/controle_ia/gardes.py src/controle_ia/scellement.py src/controle_ia/prereg.py requirements-gpu.txt requirements-cpu.txt requirements-donnees.txt"
P=prereg/P3-bis-temoin-positif-v1.md; CFG=prereg/P3-bis-temoin-positif-config-v1.json; CONSIGNES=prereg/P3-bis-consignes-v1.md
CFG_P3=prereg/P3-premier-test-config-v1.json
TACHES=donnees/t05-pilote-v1/taches-pilote-60-v1.json
AMORCE=scripts/amorce_instance_p3bis_v2.sh; INSTANCE=scripts/p3bis_instance_v2.sh
LISTE=scripts/essais-cibles-p3bis-v2.txt; ESSAI=scripts/essai_fermeture_p3bis_v2.py
LIGNE_ESSAI_CONFORME="ESSAI DIFFÉRENTIEL DE FERMETURE : CONFORME"
echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }
plat() { tr '\n' ' ' < "$1" | tr -s ' '; }
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[[ "$BRANCHE" =~ ^calcul/p3bis-reel-v[123]$ ]] || { echo "BRANCHE : calcul/p3bis-reel-v1, -v2 ou -v3 attendue"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà"; exit 2; }
grep -qE '^[A-Z_]+="?A_EPINGLER' "$0" && { echo "épingle restée « A_EPINGLER » : candidat non épinglé, aucun contrôle"; exit 2; }
[[ "$CANDIDAT_RELU" =~ ^[0-9a-f]{64}$ && "$CANDIDAT_RELU_CHEMIN" == brouillons/* ]] || { echo "candidat relu mal épinglé"; exit 2; }
[[ "$CONFIG_RELUE" =~ ^[0-9a-f]{64}$ && "$CONFIG_RELUE_CHEMIN" == brouillons/* ]] || { echo "configuration relue mal épinglée"; exit 2; }
[[ "$CONSIGNES_RELUES" =~ ^[0-9a-f]{64}$ && "$CONSIGNES_RELUES_CHEMIN" == brouillons/* ]] || { echo "consignes relues mal épinglées"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$ESSAI_FERMETURE" =~ ^[0-9a-f]{64}$ && -n "$ESSAI_FERMETURE_CHEMIN" ]] || { echo "code relu ou essai de fermeture mal épinglés"; exit 2; }
[[ "$LONGUEURS_ATTENDUES" =~ ^[0-9a-f]{64}$ && "$LONGUEURS_ATTENDUES_CHEMIN" == *.json ]] || { echo "longueurs attendues mal épinglées"; exit 2; }
n_paires=0
for paire in $RAPPORTS_ATTENDUS; do [[ "$paire" =~ ^[a-zA-Z0-9_./-]+\.(md|json)=[0-9a-f]{64}$ ]] || { echo "rapports attendus mal formés : $paire"; exit 2; }; n_paires=$((n_paires+1)); done
[ "$n_paires" -ge 1 ] || { echo "rapports attendus : au moins le rapport de la contre-lecture 4"; exit 2; }
[ -x "$PY" ] || { echo "interpréteur $PY absent"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
W="$D.travail"
[ -e "$W" ] && { echo "$W existe déjà"; exit 2; }
mkdir -p "$W" || exit 2
trap 'rm -rf "$W"' EXIT
git clone -q --no-checkout "$DEPOT_URL" "$D" || { echo "clonage impossible"; exit 2; }
git -C "$D" sparse-checkout set --no-cone "${EXTRACTION[@]}" || { echo "extraction partielle impossible"; exit 2; }
cd "$D" && git checkout -q "$S" || { echo "commit $S introuvable"; exit 2; }
for x in "${ABSENTS[@]}"; do [ -e "$x" ] && { echo "REFUS : $x extrait sur disque (interdits communs v2, règle 9 ; CD-05) : aucun contrôle"; exit 2; }; done
ok "0 clone en extraction partielle : ${ABSENTS[*]} absents du disque"
# 1. contenu de S
[ "$(git log --diff-filter=A -1 --format=%H -- "$P.sha256")" = "$S" ] && ok "1 S ajoute le sceau du texte" || ko "1 S n'est pas le commit qui ajoute $P.sha256"
attendus_s=$(printf '%s\n' "$CFG" "$CFG.sha256" "$CONSIGNES" "$CONSIGNES.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')
[ "$(git diff --name-only --no-renames "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] && \
    [ "$(git diff --name-only --no-renames --diff-filter=A "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] \
    && ok "1 S n'ajoute que le texte, la configuration, les consignes et leurs sceaux" \
    || ko "1 contenu de S inattendu : $(git diff --name-status --no-renames "$S^" "$S" | tr '\t\n' '  ' | cut -c1-300)"
# 2. commit du code et arbre gelé
NC=$(grep -c "Commit du code d'analyse : \`" "$P" || true)
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$P" | head -1)
if [ "$NC" = 1 ] && [[ "$CODE" =~ ^[0-9a-f]{40}$ ]] && git merge-base --is-ancestor "$CODE" "$S" 2>/dev/null; then ok "2 commit du code cité une fois, $CODE, ancêtre de S"
else ko "2 commit du code cité illisible, cité $NC fois, ou non ancêtre de S"; CODE=$S; fi
[ "$CODE" = "$CODE_RELU" ] && ok "2 commit du code = code relu épinglé" || ko "2 commit du code $CODE ≠ code relu épinglé $CODE_RELU"
GELES=$(PYTHONPATH=src "$PY" -c "from controle_ia.harnais.validation_reelle import CHEMINS_GELES; print(' '.join(CHEMINS_GELES))" 2>/dev/null)
if [ -n "$GELES" ]; then
    # shellcheck disable=SC2086
    git diff --quiet "$CODE" "$S" -- $GELES; c=$?
    case $c in 0) ok "2 arbre gelé de S (CHEMINS_GELES) identique au commit du code" ;; 1) ko "2 arbre gelé de S modifié depuis le commit du code" ;;
               *) ko "2 comparaison de l'arbre gelé impossible (code $c)" ;; esac
else ko "2 CHEMINS_GELES illisible"; fi
# 3. identité avec P3 : ajouts seuls
# shellcheck disable=SC2086
git diff --name-status --no-renames "$CODE_P3" "$CODE" -- $CHEMINS_IDENTITE > "$W/identite.txt" 2>&1; c=$?
if [ "$c" = 0 ] && ! grep -qv '^A' "$W/identite.txt"; then ok "3 identité avec P3 : $(wc -l < "$W/identite.txt") ajouts, aucun fichier de P3 modifié ni retiré"
else ko "3 identité avec P3 (code $c) : $(grep -v '^A' "$W/identite.txt" | head -5 | tr '\t\n' '  ')"; fi
# 4. texte sans marqueur ; sceaux ; candidats relus
MARQ=$(grep -o '<<[A-Z0-9_]\+>>' "$P" | sort -u | tr '\n' ' ')
[ -z "$MARQ" ] && ok "4 texte scellé sans marqueur" || ko "4 marqueurs restants dans le texte : $MARQ"
PYTHONPATH=src "$PY" -c "import sys; from controle_ia.prereg import problemes; p = problemes(sys.argv[1]); print(p); raise SystemExit(1 if p else 0)" "$P" > "$W/problemes.txt" 2>&1 \
    && ok "4 problemes() vide" || ko "4 problemes() non vide : $(tail -1 "$W/problemes.txt" | cut -c1-200)"
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "$P" "$CFG" "$CONSIGNES" "$TACHES" > /dev/null 2>&1 \
    && ok "4 sceaux du texte, de la configuration, des consignes et des tâches" || ko "4 sceaux"
releve() {   # $1 fichier de S, $2 chemin du relu versé, $3 empreinte épinglée, $4 nom
    [ "$(git show "$S:$2" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$3" ] && [ "$(git show "$S:$2.sha256" 2>/dev/null)" = "$3  $(basename "$2")" ] \
        && ok "4 $4 versé(e), scellé(e), à l'empreinte épinglée" || ko "4 $4 absent(e), non scellé(e) ou d'empreinte différente"
    [ "$(sha256sum "$1" | cut -d' ' -f1)" = "$3" ] && ok "4 $1 de S = $4, octet pour octet" || ko "4 $1 de S ≠ $4"
}
releve "$P" "$CANDIDAT_RELU_CHEMIN" "$CANDIDAT_RELU" "candidat relu"
releve "$CFG" "$CONFIG_RELUE_CHEMIN" "$CONFIG_RELUE" "configuration relue"
releve "$CONSIGNES" "$CONSIGNES_RELUES_CHEMIN" "$CONSIGNES_RELUES" "consignes relues"
ST=$(sha256sum "$TACHES" 2>/dev/null | cut -d' ' -f1)
[ "$(grep -c "Tâches de P3 : \`$ST\`" "$P")" = 1 ] && ok "4 tâches citées par leur empreinte ($ST)" || ko "4 tâches non citées par leur empreinte"
# 5. GO ; garde de calcul sur le registre de S
python3 -I "$VERIF" go "$P" registres/go.md "$(date -u +%F)" > "$W/bloc-go.txt" 2>&1 \
    && ok "5 GO : $(tail -1 "$W/bloc-go.txt")" || ko "5 GO : $(tail -1 "$W/bloc-go.txt")"
echo '{"tool_input":{"command":"GO_ID=GO-2026-11-10-02 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py > "$W/garde.txt" 2>&1 \
    && ok "5 garde de calcul : registre de S lisible, GO-2026-11-10-02 accepté" || ko "5 garde de calcul sur le registre de S : $(tail -1 "$W/garde.txt" | cut -c1-200)"
# 6. essai différentiel de fermeture : sortie versée, citée ; puis rejoué au commit S
if [ "$(git show "$S:$ESSAI_FERMETURE_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$ESSAI_FERMETURE" ] \
   && [ "$(git show "$S:$ESSAI_FERMETURE_CHEMIN.sha256" 2>/dev/null)" = "$ESSAI_FERMETURE  $(basename "$ESSAI_FERMETURE_CHEMIN")" ] \
   && [ "$(grep -v '^[[:space:]]*$' "$ESSAI_FERMETURE_CHEMIN" | tail -1)" = "$LIGNE_ESSAI_CONFORME" ] \
   && ! grep -q '^NON CONFORME' "$ESSAI_FERMETURE_CHEMIN" \
   && plat "$P" | grep -qF "\`$ESSAI_FERMETURE_CHEMIN\` (\`$ESSAI_FERMETURE\`"; then
    ok "6 essai de fermeture : sortie versée à l'empreinte épinglée, scellée, citée, conforme"
else ko "6 essai de fermeture : sortie absente, d'une autre empreinte, non scellée, non citée ou non conforme"; fi
PYTHONPATH=src "$PY" -B "$ESSAI" "$W/essai-fermeture" "$W/essai-fermeture.txt" > "$W/essai-console.txt" 2>&1; c=$?
DERN=$(grep -v '^[[:space:]]*$' "$W/essai-fermeture.txt" 2>/dev/null | tail -1)
if [ "$c" = 0 ] && [ "$DERN" = "$LIGNE_ESSAI_CONFORME" ] && ! grep -q '^NON CONFORME' "$W/essai-fermeture.txt"; then
    ok "6 essai de fermeture rejoué au commit S (arbre gelé du commit du code) : conforme"
else ko "6 essai de fermeture rejoué au commit S : code $c, « $DERN » : aucune création"; fi
rm -rf "$W/essai-fermeture"
# 7. longueurs au vrai tokeniseur
HF_HOME="$W/cache-hf" PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" > "$W/longueurs-mesurees.json" 2> "$W/bloc-tokeniseur.txt" <<'EOF_TOK'
import json, sys
from pathlib import Path
from controle_ia.environnements import lancer_pilote_a as lp
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches, tache_de
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia.conditions import INSTRUITES, charger_consignes, environnement
p, cfg, taches = sys.argv[1:4]
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
fmt = lp.charger_format_seul(c["agent"], "reel")
f = rp.controler_format_agent(fmt, c["agent"], "reel")
assert f["verifie"] is True, f"format de l'agent non vérifié : {f.get('motif')}"
assert tuple(INSTRUITES) == ("saboteur", "temoin", "mention"), f"conditions instruites {INSTRUITES}"
consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
guide = charger_invite("H1-classification")
seule = {k: {q: len(fmt.tok.encode(consignes[k][q], add_special_tokens=False)) for q in ("consigne", "indication")} for k in INSTRUITES}
par_tache = []
for tache in charger_taches(taches):
    envs = {k: environnement(k, tache_de(tache), c["T"], guide, consignes) for k in ("honnete",) + tuple(INSTRUITES)}
    def n(k_sys, k_obs):
        return len(fmt.ouverture(envs[k_sys].consigne_privee(0), envs[k_obs].observation(0, 0, [])))
    base = n("honnete", "honnete")
    par_tache.append({"tache": tache["identifiant"],
                      "consigne_seule": {k: seule[k]["consigne"] for k in INSTRUITES},
                      "indication_seule": {k: seule[k]["indication"] for k in INSTRUITES},
                      "consigne_gabarit": {k: n(k, "honnete") - base for k in INSTRUITES},
                      "indication_gabarit": {k: n("honnete", k) - base for k in INSTRUITES}})
print(json.dumps({"format": f["format"], "par_tache": par_tache}, ensure_ascii=False))
EOF_TOK
c=$?
if [ "$c" = 0 ] && [ "$(git show "$S:$LONGUEURS_ATTENDUES_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$LONGUEURS_ATTENDUES" ]; then
    python3 -I "$VERIF" longueurs "$W/longueurs-mesurees.json" "$LONGUEURS_ATTENDUES_CHEMIN" > "$W/bloc-longueurs.txt" 2>&1 \
        && ok "7 $(tail -1 "$W/bloc-longueurs.txt")" || ko "7 $(tail -1 "$W/bloc-longueurs.txt" | cut -c1-300)"
else ko "7 longueurs : mesure impossible (code $c : $(tail -1 "$W/bloc-tokeniseur.txt" | cut -c1-200)) ou longueurs attendues absentes de S, d'une autre empreinte"; fi
plat "$P" | grep -qF "\`$LONGUEURS_ATTENDUES_CHEMIN\` (\`$LONGUEURS_ATTENDUES\`" && ok "7 longueurs attendues citées par le texte" || ko "7 longueurs attendues non citées par le texte"
rm -rf "$W/cache-hf"
# 8. compte N des essais : liste ciblée, empreinte, « N passed » exact ; versions de l'environnement
a=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
LSHA=$(sha256sum "$LISTE" 2>/dev/null | cut -d' ' -f1)
[ "$(grep -c "^LISTE_SHA256=\"$LSHA\"" "$INSTANCE" 2>/dev/null)" = 1 ] && [ "$(grep -c '^LISTE_SHA256=' "$INSTANCE")" = 1 ] \
    && grep -q "^LISTE_TESTS=\"$LISTE\"" "$INSTANCE" && ok "8 liste ciblée $LISTE, empreinte écrite dans $INSTANCE ($LSHA)" || ko "8 liste ciblée absente ou d'empreinte autre que celle de $INSTANCE"
FICHIERS=$(grep -v '^[[:space:]]*$' "$LISTE" 2>/dev/null | tr '\n' ' ')
MAUVAIS=$(for f in $FICHIERS; do [[ "$f" =~ ^tests/test_[A-Za-z0-9_]+\.py$ && -f "$f" ]] || echo "$f"; done)
[ -n "$FICHIERS" ] && [ -z "$MAUVAIS" ] && ok "8 liste ciblée : $(echo $FICHIERS | wc -w) fichiers présents" || ko "8 liste ciblée vide ou chemins illisibles : $MAUVAIS"
PYTHONPATH=src "$PY" - > "$W/bloc-versions.txt" 2>&1 <<'EOF' && ok "8 environnement PY : versions égales aux dépendances épinglées de S" || ko "8 environnement PY : $(tail -1 "$W/bloc-versions.txt" | cut -c1-300)"
import re
from importlib import metadata
ecarts, n = [], 0
for f in ("requirements-cpu.txt", "requirements-gpu.txt", "requirements-donnees.txt"):
    for ligne in open(f, encoding="utf-8"):
        ligne = ligne.split("#")[0].strip()
        if not ligne or ligne.startswith(("-r ", "--")):
            continue
        m = re.fullmatch(r"([A-Za-z0-9_.\-]+)==(\S+)", ligne)
        if not m:
            ecarts.append(f"{f} : ligne non épinglée « {ligne} »")
            continue
        n += 1
        try:
            v = metadata.version(m.group(1))
        except metadata.PackageNotFoundError:
            v = None
        if v != m.group(2):
            ecarts.append(f"{m.group(1)} {v} ≠ {m.group(2)}")
print(f"{n} dépendances épinglées relues ; écarts : {ecarts}")
raise SystemExit(1 if ecarts or not n else 0)
EOF
# shellcheck disable=SC2086
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no $FICHIERS > "$W/liste.txt" 2>&1; cs=$?
derniere=$(grep -v '^$' "$W/liste.txt" | tail -1)
cp "$W/liste.txt" "$D.liste.txt" 2>/dev/null || true
[ "$cs" = 0 ] && [[ "$a" =~ ^[0-9]+$ ]] && [[ "$derniere" =~ ^$a\ passed(,\ [0-9]+\ warnings?)?\ in\ [0-9.]+s(\ \([0-9]+:[0-9]{2}:[0-9]{2}\))?$ ]] \
    && ok "8 liste ciblée au commit S : « $derniere » (N = $a cité)" || ko "8 liste ciblée : « $derniere » (code $cs ; $a attendus)"
# 9. configuration et gardes du lanceur run_v2
python3 -I "$VERIF" config "$CFG" "$CFG_P3" "$CONSIGNES" > "$W/bloc-config.txt" 2>&1 && ok "9 $(tail -1 "$W/bloc-config.txt")" || ko "9 $(tail -1 "$W/bloc-config.txt" | cut -c1-300)"
PYTHONPATH=src "$PY" - "$P" "$CFG" "$TACHES" > "$W/bloc-gardes.txt" 2>&1 <<'EOF_GARDES' && ok "9 gardes du lanceur run_v2 (configuration, citations, tâches, consignes, données génériques, graines)" || ko "9 gardes du lanceur run_v2 : $(tail -1 "$W/bloc-gardes.txt" | cut -c1-300)"
import json, sys
from pathlib import Path
from controle_ia.environnements.invites import charger_invite
from controle_ia.environnements.pilote_a import charger_taches
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.manifeste import graines
from controle_ia.premier_test_ia import donnees as dn
from controle_ia.premier_test_ia import run as rp
from controle_ia.premier_test_ia import run_v2
from controle_ia.premier_test_ia.conditions import charger_consignes
from controle_ia.scellement import verifier
p, cfg, taches = sys.argv[1:4]
racine = Path(".")
c = json.loads(Path(cfg).read_text(encoding="utf-8"))
run_v2.exiger_config_p3bis(c)
assert c["duree_max_s"] is None and c["budget_entrainement_s"] is None, "durées non nulles"
assert c["fils_entrainement"] == 30 and c["n_faits_max"] is None and c["mode"] == "reel", "fils, faits ou mode"
t = charger_taches(taches)
sha_t = verifier(taches)
consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
charger_invite("H1-classification")
exiger_code_importe_sous(racine)
commit = exiger_code_cite(racine, Path(p))
ent = rp.exiger_citations_p3(Path(p), c, sha_t)
assert ent == 173398867739501636779144561928402532101, f"entropie {ent} : celle de P3 attendue"
plan = rp.plan_p3(t)
assert len(plan) == 240, f"{len(plan)} épisodes au plan, 240 cités"
g = graines(rp.cles_des_graines(t, c), ent)
faits, enjeux = dn.charger_faits(), dn.charger_enjeux()
print("commit cité :", commit, "; entropie :", ent, "; épisodes :", len(plan), "; graines :", len(g), "; faits :", len(faits),
      "; textes « enjeux élevés » :", len(enjeux), "; consignes :", consignes["sha256"][:12])
EOF_GARDES
# 10. valeurs du texte ; constantes de la chaîne versée
python3 -I "$VERIF" valeurs "$P" > "$W/bloc-valeurs.txt" 2>&1 && ok "10 $(tail -1 "$W/bloc-valeurs.txt")" || ko "10 $(tail -1 "$W/bloc-valeurs.txt" | cut -c1-300)"
python3 -I "$VERIF" constantes "$VERSEES" > "$W/bloc-constantes.txt" 2>&1 && ok "10 $(tail -1 "$W/bloc-constantes.txt")" || ko "10 $(tail -1 "$W/bloc-constantes.txt" | cut -c1-300)"
# 11. scripts de l'instance (noms v2)
for f in "$AMORCE" "$INSTANCE"; do
    if [ -f "$f" ]; then
        e=$(sha256sum "$f" | cut -d' ' -f1)
        plat "$P" | grep -qF "\`$f\` (\`$e\`" && ok "11 empreinte de $f citée ($e)" || ko "11 empreinte de $f ($e) non citée"
        grep -vE '^[[:space:]]*#' "$f" | grep -qE '(^|[^A-Za-z_])timeout([^A-Za-z_]|$)' && ko "11 $f : commande « timeout » (aucun budget de temps)" || ok "11 $f : aucune commande timeout"
        grep -q 'lciric/controle-ia\.git' "$f" && ko "11 $f : copie publique citée" || ok "11 $f : jamais la copie publique"
    else ko "11 $f absent de S"; fi
done
grep -qF 'controle_ia.premier_test_ia.run_v2' "$INSTANCE" 2>/dev/null && grep -qF "DEPOT_URL=\"\${DEPOT_URL:-$DEPOT_URL}\"" "$INSTANCE" 2>/dev/null \
    && grep -qF "bash amorce-depot/$INSTANCE" "$AMORCE" 2>/dev/null \
    && ok "11 instance : lanceur run_v2, dépôt de travail par défaut ; l'amorce appelle $INSTANCE" || ko "11 instance : lanceur, dépôt par défaut ou appel de l'amorce inattendus"
# 12. lecture précoce, intitulés, ligne « Lancement »
lire_unique() { [ "$(grep -c "$1 : \`" "$P" || true)" = 1 ] && sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$P"; }
L_TESTS=$(lire_unique "Tests attendus"); L_CFG=$(lire_unique "Chemin de la configuration de P3")
L_T=$(lire_unique "Chemin des tâches de P3"); L_C=$(lire_unique "Chemin des consignes de P3")
[ "$L_TESTS" = "$a" ] && [ "$L_CFG" = "$CFG" ] && [ "$L_T" = "$TACHES" ] && [ "$L_C" = "$CONSIGNES" ] \
    && ok "12 lecture précoce : citations uniques, chemins attendus" || ko "12 lecture précoce : citation absente, en double, ou chemin inattendu"
INTITULES=("Configuration de P3 (empreinte canonique)" "Tâches de P3" "Commit du code d'analyse" "Entropie" "Tests attendus"
           "Chemin de la configuration de P3" "Chemin des tâches de P3" "Chemin des consignes de P3")
DOUBLES=""; for x in "${INTITULES[@]}"; do [ "$(grep -oF "$x : \`" "$P" | wc -l)" = 1 ] || DOUBLES="$DOUBLES « $x »"; done
[ -z "$DOUBLES" ] && ok "12 intitulés lus une fois chacun (${#INTITULES[@]})" || ko "12 intitulés absents ou cités plusieurs fois :$DOUBLES"
grep -qF "\`PREREG=$P\`, \`BRANCHE=calcul/p3bis-reel-v1\`" "$P" && grep -qF "\`DEPOT_URL=$DEPOT_URL\`" "$P" \
    && ok "12 ligne « Lancement » : PREREG, BRANCHE, DEPOT_URL du dépôt de travail" || ko "12 ligne « Lancement » : PREREG, BRANCHE ou DEPOT_URL autres"
# 13. branche de calcul absente du dépôt distant
git ls-remote --exit-code origin "refs/heads/$BRANCHE" > /dev/null 2>&1; c=$?
[ "$c" = 2 ] && ok "13 branche $BRANCHE absente du dépôt distant" || ko "13 branche $BRANCHE : code $c (2 attendu)"
# 14. rapports ; arbre
for paire in $RAPPORTS_ATTENDUS; do
    f=${paire%%=*}; e=${paire#*=}
    if [ "$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $(basename "$f")" ]; then
        plat "$P" | grep -qF "\`$f\`" && plat "$P" | grep -qF "$e" && ok "14 rapport $f présent, scellé, cité" || ko "14 rapport $f présent et scellé, mais non cité par le texte"
    else ko "14 rapport $f absent, non scellé ou d'empreinte différente"; fi
done
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier-arbre . > "$W/verifier-arbre.txt" 2>&1
tail -1 "$W/verifier-arbre.txt" | grep -qx "arbre intact" && ok "14 verifier-arbre : arbre intact" || ko "14 verifier-arbre : $(grep '^ÉCHEC' "$W/verifier-arbre.txt" | head -3 | tr '\n' ' ')"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
[ "$echec" = 0 ]
