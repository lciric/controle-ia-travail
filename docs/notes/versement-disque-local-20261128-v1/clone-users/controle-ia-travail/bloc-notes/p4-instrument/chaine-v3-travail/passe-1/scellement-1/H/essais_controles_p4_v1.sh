#!/usr/bin/env bash
# Banc des contrôles avant dépense de P4-instrument (R5), v1, décliné de
# docs/procedures/P3-premier-test-v2/essais_controles_p3_v1.sh sous un nom neuf (R12) : un cas sain et des artefacts,
# chacun joué contre le script entier sur un dépôt jetable (clone partagé de DEPOT_SOURCE au commit C, module de P4
# versé, sans extraction des PDF) et un dépôt nu local. Préalables d'essai fabriqués par le banc (commit A, puis B) :
# vingt et un scripts de la chaîne versés (copies du bloc-notes), candidat d'essai tiré du brouillon 4
# (outils_essais_p4_v1.py : commit du code 7a54d43, empreinte canonique de la configuration réelle de référence,
# tests collectés, rapports cités), configuration réelle de référence (B et B′ de MC-1), vingt-six rapports synthétiques (chaîne v3) de
# la famille « P4 », journal de la répétition jouet synthétique conforme au module commun (commit répété A, candidat
# d'essai, scripts répétés aux empreintes des copies versées). Registres, données de P3 et sortie scellée des mesures de
# conception : ceux de C (réels ; empreintes seulement, aucun texte lu). La copie jouée est celle du bloc-notes, dont
# changent seulement : l'adresse du dépôt, les sept épingles (le candidat et le journal n'existent pas encore au
# versement réel : « A_EPINGLER »), la suite complète des tests (bouchon qui écrit « N passed », N lu dans le texte,
# ou FAUX_SUITE) et le lancement des mesures de conception (bouchon : la sortie scellée de S recopiée, au besoin altérée
# par FAUX_MC, puis comparée par le programme réel des contrôles ; les mesures réelles lisent les textes de P3 et ne
# tournent qu'à la répétition finale, sur le vrai tokeniseur). Chaque artefact touche d'abord la base (registres,
# scripts versés, fichiers cités ; un commit), puis le texte ou la configuration (commit S qui ajoute les quatre
# fichiers), puis éventuellement le dépôt distant ; verdict : code attendu et ligne KO attendue présente (code 2 : motif
# sur la dernière ligne, aucune ligne OK ni KO) ; nombre de KO attendu quand la cause est seule.
# Chaîne v2 : vingt et un scripts versés ; rapports synthétiques aux noms exacts du module commun (RC-fidelite-12 ;
# rapport de trop, mal formé, un seul : refus) ; tokeniseur de l'agent versé sous donnees/P4-tokeniseur-v1/ avec ses
# sceaux (copie de la session ; absent, altéré ou sans sceau : KO net, RC-donnees-09) ; liste des chemins gelés lue
# dans 7a54d43 (liste de S qui s'exclut elle-même et exclut un dossier changé : KO, RC-donnees-08) ; journal synthétique
# de la répétition par outils_essais_p4_v1.py journal-repetition (quatre scripts répétés) ; constantes neuves (arrêt,
# surveillance, cinq minutes, récupération, garde gelée du lanceur) et valeurs neuves du texte (forme de la dépense de
# la phase, script d'arrêt, contrôle des traces, tokeniseur versé, empreinte de la garde) reliées.
# Usage : essais_controles_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE
set -uo pipefail
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }   # troncature par octets, caractère coupé retiré :
                                                                  # journal toujours en UTF-8 valide
[ $# -eq 3 ] || { echo "usage : essais_controles_p4_v1.sh DEPOT_SOURCE C RACINE_NEUVE"; exit 2; }
SRC=$(realpath "$1"); C=$2; R=$(realpath -m "$3")
SOI=$(realpath "$0")
HN=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v3
TOK=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/tokeniseur   # copie de la session (79e3e522…, 177c7b61…)
TOK_JSON_REEL=79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4
TOK_CONFIG_REEL=177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424
B4=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/P4-instrument-v1-brouillon4.md
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
V=docs/procedures/P4-instrument-v1
P=prereg/P4-instrument-v1.md; CFG=prereg/P4-instrument-config-v1.json
GO=GO-2026-10-20-07
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh
        repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh
        essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
export PYTHONDONTWRITEBYTECODE=1
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R" && cd "$R" || exit 2
git clone -q --shared --no-checkout "$SRC" source && cd source || exit 2
git config user.email essai@invalid; git config user.name essai; git config commit.gpgsign false
git sparse-checkout set --no-cone '/*' '!/docs/sources/pdf/' '!/docs/sources/lecture-pdf-niveau1/' '!/docs/sources/lecture-pdf-niveau2/' \
    && git checkout -q "$C" && git checkout -q -B main || exit 2
echo "C = $(git rev-parse HEAD)"
for s in controles_avant_depense_p4_v1.sh verifications_p4_v1.py outils_essais_p4_v1.py; do echo "script éprouvé : $s $(sha256sum "$HN/$s" | cut -d' ' -f1)"; done
echo "script éprouvé : $(basename "$SOI") $(sha256sum "$SOI" | cut -d' ' -f1)"
# préalables d'essai, commit A : chaîne versée, candidat et configuration relus, rapports
mkdir -p "$V" brouillons prereg/contre-lectures
for s in $CHAINE; do cp "$HN/$s" "$V/$s" && (cd "$V" && sha256sum "$s" > "$s.sha256") || { echo "copie versée impossible : $s"; exit 2; }; done
# rapports synthétiques, aux noms exacts du module commun (RC-fidelite-12)
NOMS_R=$("$PY" -I -B -c 'import importlib.util, sys
spec = importlib.util.spec_from_file_location("v", sys.argv[1]); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
print(" ".join(v.RAPPORTS_NOMS))' "$HN/verifications_p4_v1.py") || exit 2
RAPPORTS=""
for nom in $NOMS_R; do
    printf '# Rapport synthétique %s (banc des contrôles de P4)\n\nVerdict : scellable (essai).\n' "$nom" > "prereg/contre-lectures/$nom"
    (cd prereg/contre-lectures && sha256sum "$nom" > "$nom.sha256")
    RAPPORTS="$RAPPORTS $nom=$(sha256sum "prereg/contre-lectures/$nom" | cut -d' ' -f1)"
done
RAPPORTS=${RAPPORTS# }
R1=$(echo $NOMS_R | cut -d' ' -f1); R2=$(echo $NOMS_R | cut -d' ' -f2)
# chaîne v3 : tokeniseur de substitution, sur demande explicite seulement (BANC_TOKENISEUR_SUBSTITUT=1), quand la copie de la
# session de tokenizer.json manque ou n'a pas son empreinte (bloc-notes restauré sans elle) : tokenizer.json synthétique,
# tokenizer_config.json réel exigé ; la ligne TOK_JSON de la copie des contrôles prend l'empreinte du substitut (une ligne
# de plus, comptée et écrite au journal) ; sans la demande : refus en code 2, comme avant. L'empreinte réelle reste
# éprouvée à la répétition finale, sur le vrai C.
SUBSTITUT=non
if [ "$(sha256sum "$TOK/tokenizer.json" 2>/dev/null | cut -d' ' -f1)" != "$TOK_JSON_REEL" ]; then
    [ "${BANC_TOKENISEUR_SUBSTITUT:-}" = 1 ] || { echo "copie de la session de tokenizer.json absente ou d'empreinte autre ($TOK) : banc impossible (BANC_TOKENISEUR_SUBSTITUT=1 pour un substitut annoncé)"; exit 2; }
    [ "$(sha256sum "$TOK/tokenizer_config.json" 2>/dev/null | cut -d' ' -f1)" = "$TOK_CONFIG_REEL" ] || { echo "tokenizer_config.json de la session absent ou d'empreinte autre : banc impossible"; exit 2; }
    mkdir -p "$R/tokeniseur-substitut" && cp "$TOK/tokenizer_config.json" "$R/tokeniseur-substitut/" \
        && printf '{"essai": "tokenizer.json de substitution du banc des contrôles de P4 (copie de la session absente du bloc-notes restauré)"}\n' > "$R/tokeniseur-substitut/tokenizer.json" || exit 2
    TOK=$R/tokeniseur-substitut; SUBSTITUT=oui
    echo "TOKENISEUR DE SUBSTITUTION (demandé) : tokenizer.json synthétique $(sha256sum "$TOK/tokenizer.json" | cut -d' ' -f1) au lieu de ${TOK_JSON_REEL:0:12}… (copie de la session absente) ; tokenizer_config.json réel ${TOK_CONFIG_REEL:0:12}…"
else echo "tokeniseur de la session : tokenizer.json ${TOK_JSON_REEL:0:12}…, tokenizer_config.json réel"; fi
# tokeniseur de l'agent versé avec ses sceaux (RC-donnees-09 ; donnees/ est ignoré par git : ajout forcé)
mkdir -p donnees/P4-tokeniseur-v1 && cp "$TOK/tokenizer.json" "$TOK/tokenizer_config.json" donnees/P4-tokeniseur-v1/ \
    && (cd donnees/P4-tokeniseur-v1 && sha256sum tokenizer.json > tokenizer.json.sha256 && sha256sum tokenizer_config.json > tokenizer_config.json.sha256) \
    && git add -f donnees/P4-tokeniseur-v1 || { echo "tokeniseur impossible"; exit 2; }
RELU=brouillons/P4-instrument-v1-candidat-essai.md; CFG_RELUE=brouillons/P4-instrument-config-v1-candidat-essai.json
CFG_SHA=$("$PY" -B "$HN/outils_essais_p4_v1.py" config-reelle . "$V" "$CFG_RELUE" | python3 -c 'import json, sys; print(json.load(sys.stdin)["config"])') || { echo "configuration relue impossible"; exit 2; }
NT=$(PYTHONPATH=src "$PY" -B -m pytest --collect-only -q -p no:cacheprovider tests "$V/test_instrument_p4_v1.py" \
    "$V/test_lecture_p4_v1.py" "$V/test_gardes_p4_v1.py" 2>/dev/null | sed -n 's/^\([0-9]*\) tests\{0,1\} collected.*/\1/p')
[[ "$NT" =~ ^[0-9]+$ ]] || { echo "nombre de tests illisible"; exit 2; }
"$PY" -B "$HN/outils_essais_p4_v1.py" candidat "$B4" "$RELU" . 7a54d431d89745839220f882b41b13e8c62ecfdd "$CFG_SHA" "$NT" \
    $(for x in $RAPPORTS; do printf -- '--rapport %s ' "$x"; done) > /dev/null || { echo "candidat d'essai impossible"; exit 2; }
git add -A "$V" brouillons prereg/contre-lectures && git commit -qm "essai : préalables (chaîne, candidat et configuration relus, rapports)" || exit 2
A=$(git rev-parse HEAD)
# commit B : journal de la répétition jouet, synthétique, conforme au module commun (commit répété A)
LOGJ=$V/repetition-jouet-p4-v1.log
"$PY" -B "$HN/outils_essais_p4_v1.py" journal-repetition "$HN/verifications_p4_v1.py" "$A" "$(basename "$RELU")" "$(sha256sum "$RELU" | cut -d' ' -f1)" "$V" > "$LOGJ" || exit 2
(cd "$V" && sha256sum repetition-jouet-p4-v1.log > repetition-jouet-p4-v1.log.sha256)
git add "$LOGJ" "$LOGJ.sha256" && git commit -qm "essai : journal de la répétition jouet (synthétique)" || exit 2
C1=$(git rev-parse HEAD); echo "préalables d'essai : A = $A ; B = $C1"
git clone -q --bare . "$R/distant.git" || exit 2
# copie jouée : adresse du dépôt, sept épingles, bouchons de la suite et des mesures de conception
python3 - "$HN/controles_avant_depense_p4_v1.sh" "$R/controles-essai.sh" "$R/distant.git" "$(sha256sum "$RELU" | cut -d' ' -f1)" "$RELU" \
    "$(sha256sum "$CFG_RELUE" | cut -d' ' -f1)" "$CFG_RELUE" "$RAPPORTS" "$A" "$(sha256sum "$LOGJ" | cut -d' ' -f1)" \
    "$( [ "$SUBSTITUT" = oui ] && sha256sum "$TOK/tokenizer.json" | cut -d' ' -f1)" <<'PYCOPIE' || exit 2
import re, sys
from pathlib import Path
src, dst, depot, relu_sha, relu, cfg_sha, cfg, rapports, rep_commit, rep_sha, tok_substitut = sys.argv[1:12]
t = Path(src).read_text(encoding="utf-8")
def rep(t, a, b):
    n = len(re.findall(a, t, re.M))
    assert n == 1, (n, a)
    return re.sub(a, lambda _: b, t, flags=re.M)
for nom, val in (("DEPOT", depot), ("CANDIDAT_RELU", relu_sha), ("CANDIDAT_RELU_CHEMIN", relu), ("CONFIG_RELUE", cfg_sha),
                 ("CONFIG_RELUE_CHEMIN", cfg), ("RAPPORTS_ATTENDUS", f'"{rapports}"'), ("REPETITION_COMMIT", rep_commit),
                 ("REPETITION_JOUET", rep_sha)):
    t = rep(t, rf"^{nom}=\S+", f"{nom}={val}")
if tok_substitut:                                  # chaîne v3 : substitut demandé (voir plus haut)
    t = rep(t, r"^TOK_JSON=[0-9a-f]{64}", f"TOK_JSON={tok_substitut}")
a = 'PYTHONPATH=src "$PY" -B -m pytest -q -p no:cacheprovider tests $TESTS_MODULE > "$W/suite.txt" 2>&1; cs=$?'
assert t.count(a) == 1
t = t.replace(a, 'printf \'%s passed in 1.00s\\n\' "${FAUX_SUITE:-$a}" > "$W/suite.txt"; cs=0   # bouchon du banc')
a = 'PYTHONPATH=src "$PY" -B "$MESURES" --tokeniseur "$TOKENISEUR" --sortie "$W/mc-rejouee.json" > "$W/bloc-mc.txt" 2>&1'
assert t.count(a) == 1
t = t.replace(a, 'python3 -c \'import json, os, sys; d = json.load(open(sys.argv[1])); f = os.environ.get("FAUX_MC", ""); d["MC-1"]["B"] = d["MC-1"]["B"].replace("tall", "young") if f == "b" else d["MC-1"]["B"]; d["MC-2"]["par_tache"][0]["egal"] = (not d["MC-2"]["par_tache"][0]["egal"]) if f == "niveau1" else d["MC-2"]["par_tache"][0]["egal"]; json.dump(d, open(sys.argv[2], "w"))\' "$MC" "$W/mc-rejouee.json" > "$W/bloc-mc.txt" 2>&1   # bouchon du banc')
Path(dst).write_text(t, encoding="utf-8")
PYCOPIE
echo "lignes changées dans la copie des contrôles : $(diff "$HN/controles_avant_depense_p4_v1.sh" "$R/controles-essai.sh" | grep -c '^>') (DEPOT, sept épingles, bouchons de la suite et des mesures$( [ "$SUBSTITUT" = oui ] && echo " ; TOK_JSON du tokeniseur de substitution"))"
grep -n "github" "$R/controles-essai.sh" && { echo "COPIE DES CONTRÔLES NON SÛRE"; exit 2; }
resceller() { local f; for f in "$@"; do (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256"); done; }
cfg_set() {   # $1 clé, $2 valeur JSON : la configuration de S changée (texte d'un cas)
    python3 - "$CFG" "$1" "$2" <<'PYS'
import json, sys
f, k, v = sys.argv[1:4]
c = json.load(open(f, encoding="utf-8"))
c[k] = json.loads(v)
open(f, "w", encoding="utf-8").write(json.dumps(c, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
PYS
}
cfg_citee() {   # empreinte canonique de la configuration de S reportée dans le texte de S
    local e; e=$(PYTHONPATH=src "$PY" -B -c 'import hashlib, json, sys; from controle_ia.manifeste import config_canonique; print(hashlib.sha256(config_canonique(json.load(open(sys.argv[1])))).hexdigest())' "$CFG")
    sed -i "s/Configuration de P4 (empreinte canonique) : \`[0-9a-f]\{64\}\`/Configuration de P4 (empreinte canonique) : \`$e\`/" "$P"
}
precoce() { echo "$1 : $2 : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
jouer() {   # $1 nom, $2 code attendu, $3 motif KO attendu (vide : cas sain), $4 base, $5 texte, $6 après, $7 copie des contrôles,
            # $8 nombre de KO attendu (vide : non compté), $9 variables d'environnement du cas
    local nom=$1 attendu=$2 motif=$3 base=$4 texte=$5 apres=${6:-} ctl=${7:-$R/controles-essai.sh} nko=${8:-} envs=${9:-FAUX_X=1}
    git checkout -q -B "art-$nom" "$C1" || { precoce "$nom" "montage impossible"; return; }
    eval "$base"
    if [ -n "$(git status --porcelain)" ]; then git add -A . && git commit -qm "essai : base $nom" || { precoce "$nom" "commit de base impossible"; return; }; fi
    cp "$RELU" "$P" && cp "$CFG_RELUE" "$CFG" || { precoce "$nom" "copie impossible"; return; }
    eval "$texte"
    resceller "$P" "$CFG"
    git add "$P" "$P.sha256" "$CFG" "$CFG.sha256" && git commit -qm "essai : S $nom" || { precoce "$nom" "commit S impossible"; return; }
    local s; s=$(git rev-parse HEAD)
    git push -q "$R/distant.git" "art-$nom" || { precoce "$nom" "poussée impossible"; return; }
    eval "$apres"
    # shellcheck disable=SC2086
    env $envs bash "$ctl" "$s" "$R/clone-$nom" > "$R/sortie-$nom.txt" 2>&1; local c=$?
    rm -rf "$R/clone-$nom" "$R/clone-$nom.travail" "$R/clone-$nom.suite.txt"
    local verdict="CONFORME"
    [ "$c" = "$attendu" ] || verdict="NON CONFORME (code $c, attendu $attendu)"
    if [ "$attendu" = 2 ]; then
        tail -1 "$R/sortie-$nom.txt" | grep -qF -- "$motif" || verdict="NON CONFORME (motif « $motif » absent de la dernière ligne)"
        [ "$(grep -c '^OK\|^KO' "$R/sortie-$nom.txt")" = 0 ] || verdict="NON CONFORME (lignes OK ou KO avant l'arrêt en code 2)"
    elif [ -n "$motif" ] && ! M="$motif" awk 'index($0, "KO") == 1 && index($0, ENVIRON["M"]) { t = 1 } END { exit !t }' "$R/sortie-$nom.txt"; then
        verdict="NON CONFORME (KO « $motif » absent)"; fi
    if [ -n "$nko" ] && [ "$(grep -c '^KO' "$R/sortie-$nom.txt")" != "$nko" ]; then verdict="NON CONFORME ($(grep -c '^KO' "$R/sortie-$nom.txt") KO, $nko attendu(s))"; fi
    if [ -z "$motif" ] && [ "$attendu" = 0 ] && ! tail -1 "$R/sortie-$nom.txt" | grep -qx "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"; then
        verdict="NON CONFORME (dernière ligne)"; fi
    grep -q "^Traceback" "$R/sortie-$nom.txt" && verdict="NON CONFORME (trace d'exception)"
    [ "$verdict" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $(grep -c '^OK' "$R/sortie-$nom.txt") OK, $(grep -c '^KO' "$R/sortie-$nom.txt") KO ; $verdict"
    grep '^KO' "$R/sortie-$nom.txt" | sed 's/^/    /' | couper 220
    [ "$attendu" = 2 ] && tail -1 "$R/sortie-$nom.txt" | couper 200 | sed 's/^/    | /'
    return 0
}
copie_ctl() {   # $1 sortie, $2 expression sed sur la copie jouée : une ligne exactement
    sed -e "$2" "$R/controles-essai.sh" > "$1"
    local n; n=$(diff "$R/controles-essai.sh" "$1" | grep -c '^>')
    [ "$n" = 1 ] || { echo "COPIE NON CONFORME : $1 change $n ligne(s) au lieu d'une : ARRÊT"; exit 2; }
}
NON_CONFORMES=0
JOUR=$(date -u +%F); HIER=$(date -u -d yesterday +%F)
echo "tests collectés : $NT ; rapports : $(echo $NOMS_R | wc -w) ; commit répété : $A"
jouer A00-sain 0 "" ":" ":"
# GO et dépense (registres de S) ; la garde gelée (bloc 12) voit les mêmes registres
jouer A01-go-absent-du-registre 1 "GO et dépense (GO cité, plafond, échéance, borne, révocation ou garde gelée) : $GO absent ou en double" "sed -i '/^| $GO |/d' registres/go.md" ":" "" "" 2
jouer A02-go-d-un-autre-type 1 "de type « calcul », accordée par Lazar" "sed -i '/^| $GO |/s/| calcul |/| revendication |/' registres/go.md" ":" "" "" 2
jouer A03-plafond-sans-le-prefixe 1 "ne commence pas par « 10 USD par lancement »" "sed -i '/^| $GO |/s/| 10 USD par lancement, /| 12 USD par lancement, /' registres/go.md" ":" "" "" 1
jouer A04-revocation-au-registre-des-go 1 "révocation au registre des GO (GO-2026-10-20-98)" "echo '| GO-2026-10-20-98 | $JOUR | révocation | révoque R-269 (essai) | — | $JOUR | Lazar | essai |' >> registres/go.md" ":" "" "" 1
jouer A04b-revocation-au-registre-des-decisions 1 "révocation au registre des décisions (R-998)" "echo '| R-998 | $JOUR | **Révocation de R-262** (essai). | essai |' >> registres/decisions.md" ":" "" "" 1
jouer A05-go-echu 1 "$GO échu" "sed -i -E '/^\\| $GO \\|/s/\\| 2026-11-30 \\| Lazar \\|/| $HIER | Lazar |/' registres/go.md" ":" "" "" 2
jouer A06-texte-qui-cite-un-autre-go 1 "GO-2026-10-04-08 : seul $GO est accepté" ":" "sed -i 's/\`GO_ID=$GO\`/\`GO_ID=GO-2026-10-04-08\`/' $P"
jouer A07-registre-mal-forme-refuse-par-la-garde 1 "garde de calcul sur le registre de S" "echo '| GO-2026-10-20-96 | $JOUR | calcul | essai à sept colonnes | — | $JOUR | Lazar |' >> registres/go.md" ":" "" "" 2
# module de P4, texte, configuration, code
jouer A08-fichier-du-module-change 1 "module de P4 : module de P4 : $V/test_gardes_p4_v1.py : empreinte" "echo '# essai' >> $V/test_gardes_p4_v1.py && resceller $V/test_gardes_p4_v1.py" ":"
jouer A11-texte-autre-que-le-candidat 1 "$P de S ≠ candidat relu" ":" "echo >> $P" "" "" 1
jouer A12-configuration-autre-que-la-relue 1 "$CFG de S ≠ configuration relue" ":" "cfg_set n_tirages 1000"
jouer A13-commit-du-code-cite-deux-fois 1 "cité 2 fois" ":" "sed -i '0,/^- Commit du code d.analyse : /{/^- Commit du code d.analyse : /p}' $P"
jouer A14-code-modifie-apres-cite 1 "arbre gelé modifié depuis le commit du code" "echo '# essai' >> src/controle_ia/premier_test_ia/run.py" ":"
jouer A16-amorce-modifiee 1 "empreinte de $V/amorce_instance_p4_v1.sh" "echo '# essai' >> $V/amorce_instance_p4_v1.sh && resceller $V/amorce_instance_p4_v1.sh" ":"
jouer A17-donnee-de-p3-alteree 1 "table « Données lues »" "echo 'essai,1' >> donnees/T0.7-faits-repe-v1/facts_true_false.csv && resceller donnees/T0.7-faits-repe-v1/facts_true_false.csv" ":"
jouer A18-donnee-de-p3-sans-sceau 1 "table « Données lues »" "git rm -q donnees/t05-pilote-v1/taches-pilote-60-v1.json.sha256" ":"
jouer A21-s-ajoute-un-autre-fichier 1 "contenu de S inattendu" ":" "echo essai >> README.md && git add README.md"
jouer A21b-configuration-ajoutee-avant-s 1 "contenu de S inattendu" "cp $CFG_RELUE $CFG && resceller $CFG" ":"
jouer A22-tests-attendus-cites-deux-fois 1 "lecture précoce" ":" "sed -i 's/^\\(- Tests attendus : .*\\)\$/&\\n\\1/' $P"
jouer A22b-chemin-de-la-configuration-cite-deux-fois 1 "lecture précoce" ":" "sed -i 's/^\\(- Run source (P3) : .*\\)\$/&\\n- Rappel : chemin \`prereg\\/P4-instrument-config-v1.json\` (essai)./' $P"
jouer A22c-intitule-en-double 1 "intitulés absents ou cités plusieurs fois : « Entropie »" ":" "sed -i 's/^\\(- Entropie : .*\\)\$/&\\n\\1/' $P"
jouer A23-problemes-non-vide 1 "problemes() non vide" ":" "sed -i 's/^## Contre-lecture$/## Contre-lecture retirée/' $P"
jouer A24-ligne-lancement-autre 1 "PREREG ou BRANCHE" ":" "sed -i 's/\`BRANCHE=calcul\\/p4-reel-v1\`/\`BRANCHE=calcul\\/p4-reel-v9\`/' $P"
jouer A25-suite-autre-nombre 1 "suite complète" ":" ":" "" "" 1 "FAUX_SUITE=$((NT + 1))"
# rapports et répétition jouet
jouer A26-rapport-altere 1 "rapport $R1 absent, non scellé" "echo x >> prereg/contre-lectures/$R1 && resceller prereg/contre-lectures/$R1" ":" "" "" 1
jouer A26b-rapport-present-mais-non-cite 1 "rapport $R2 présent et scellé, mais non cité" ":" "sed -i 's|\`prereg/contre-lectures/$R2\`|rapport non cité (essai)|' $P"
jouer A27-rapport-de-trop 1 "rapports présents" "echo x > prereg/contre-lectures/P4-essai-autre-v1.md && resceller prereg/contre-lectures/P4-essai-autre-v1.md" ":" "" "" 1
jouer A28-journal-repetition-altere 1 "répétition jouet : journal absent de S, d'une autre empreinte" "echo x >> $V/repetition-jouet-p4-v1.log && resceller $V/repetition-jouet-p4-v1.log" ":" "" "" 1
jouer A29-copie-versee-de-la-recuperation-modifiee 1 "script répété ≠ copie versée à S : recuperation_p4_v1.sh" "echo '# essai' >> $V/recuperation_p4_v1.sh && resceller $V/recuperation_p4_v1.sh" ":" "" "" 1
COTE=$(git -C "$R/source" commit-tree "$A^{tree}" -p "$C" -m "essai : commit de côté")
git -C "$R/source" push -q "$R/distant.git" "$COTE:refs/heads/cote" || exit 2
copie_ctl "$R/controles-A29b.sh" "s/^REPETITION_COMMIT=[0-9a-f]\{40\}/REPETITION_COMMIT=$COTE/"
jouer A29b-commit-repete-non-ancetre 1 "répétition jouet" ":" ":" "" "$R/controles-A29b.sh" 1
jouer A29c-scripts-de-l-instance-autres-qu-au-commit-repete 1 "répétition jouet : module ou scripts de l'instance du commit répété ≠ ceux de S" "echo '# essai' >> $V/p4_instance_v1.sh && resceller $V/p4_instance_v1.sh" ":"
copie_ctl "$R/controles-A30.sh" "s/^CODE_RELU=[0-9a-f]\{40\}/CODE_RELU=$(git -C "$R/source" rev-parse 7a54d431d89745839220f882b41b13e8c62ecfdd^)/"
jouer A30-code-relu-autre 1 "arbre gelé de S ≠ celui de P3" ":" ":" "" "$R/controles-A30.sh"
# bornes : constantes des scripts versés à S, et valeurs citées par le texte
jouer A41-delai-du-run-change 1 "délai externe du run" "sed -i 's/--kill-after=5m 90m)/--kill-after=5m 95m)/' $V/p4_instance_v1.sh && resceller $V/p4_instance_v1.sh" ":"
jouer A42-plafond-de-l-amorce-change 1 "plafond de l'amorce" "sed -i 's/--kill-after=5m 150m /--kill-after=5m 140m /' $V/amorce_instance_p4_v1.sh && resceller $V/amorce_instance_p4_v1.sh" ":"
jouer A43-credit-change 1 "constante HEURES_CREDIT ≠ 3.0" "sed -i 's/^HEURES_CREDIT=3.0 /HEURES_CREDIT=2.5 /' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
jouer A43b-prix-du-controle-a-cinq-minutes-change 1 "constante PRIX_MAX ≠ 1.30" "sed -i 's/^PRIX_MAX=1.30 /PRIX_MAX=1.40 /' $V/controle_cinq_minutes_p4_v1.sh && resceller $V/controle_cinq_minutes_p4_v1.sh" ":" "" "" 1
jouer A44-plafond-de-la-surveillance-change 1 "constante PLAFOND_S ≠ 9600" "sed -i 's/^PLAFOND_S=9600 /PLAFOND_S=9000 /' $V/surveiller_p4_v1.sh && resceller $V/surveiller_p4_v1.sh" ":" "" "" 1
jouer A44b-surveillance-du-lanceur-changee 1 "constante PLAFOND_SURVEILLANCE_S ≠ 9600" "sed -i 's/^PLAFOND_SURVEILLANCE_S=9600 /PLAFOND_SURVEILLANCE_S=9000 /' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
jouer A44c-coeurs-de-l-offre-changes 1 "constante COEURS_MIN ≠ 16" "sed -i 's/^COEURS_MIN=16 /COEURS_MIN=8 /' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
jouer A44d-stockage-change 1 "constante STOCKAGE_MAX ≠ 0.03" "sed -i 's/^STOCKAGE_MAX=0.03 /STOCKAGE_MAX=0.04 /' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
jouer A44e-borne-de-l-etape-changee 1 "constante BORNE_ETAPE_USD ≠ 5.41" "sed -i 's/^BORNE_ETAPE_USD=5.41 /BORNE_ETAPE_USD=5.40 /' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
jouer A44f-go-du-lanceur-change 1 "GO cité par le lanceur" "sed -i 's/^GO_CITE=$GO /GO_CITE=GO-2026-10-04-08 /' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
jouer A44g-instance-toleree-ajoutee 1 "instances tolérées du lanceur" "sed -i 's/^ARRETEES_TOLEREES=\"56799469\" /ARRETEES_TOLEREES=\"56799469 56438435\" /' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
jouer A44h-texte-sans-la-surveillance 1 "valeur non citée par le texte : création + 9 600 s" ":" "sed -i 's/création + 9 600 s/création + 9 601 s/g' $P"
# chaîne v2 : texte changé à S (le candidat relu épinglé diffère aussi : deux KO comptés) ; récupération changée (le
# script répété diffère aussi de sa copie versée : deux KO comptés)
jouer A44j-texte-sans-la-forme-de-la-depense-de-la-phase 1 "valeur non citée par le texte : « dépense consignée X USD" ":" "sed -i 's/« dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD »/la dépense de la phase (essai)/g' $P" "" "" 2
jouer A44k-texte-sans-le-script-d-arret 1 "valeur non citée par le texte : \`arreter_p4_v1.sh" ":" "sed -i 's/arreter_p4_v1.sh <identifiant> <dossier neuf>/arrêt à la main (essai)/g' $P" "" "" 2
jouer A48-delai-de-l-arret-change 1 "constante LECTURES_MAX ≠ 60" "sed -i 's/^LECTURES_MAX=60 /LECTURES_MAX=61 /' $V/arreter_p4_v1.sh && resceller $V/arreter_p4_v1.sh" ":" "" "" 1
jouer A49-intervalle-de-la-surveillance-change 1 "constante INTERVALLE_MAX ≠ 300" "sed -i 's/^INTERVALLE_MAX=300 /INTERVALLE_MAX=400 /' $V/surveiller_p4_v1.sh && resceller $V/surveiller_p4_v1.sh" ":" "" "" 1
jouer A50-stockage-du-controle-a-cinq-minutes-change 1 "constante STOCKAGE_MAX ≠ 0.03" "sed -i 's/^STOCKAGE_MAX=0.03 /STOCKAGE_MAX=0.04 /' $V/controle_cinq_minutes_p4_v1.sh && resceller $V/controle_cinq_minutes_p4_v1.sh" ":" "" "" 1
jouer A51-place-de-la-recuperation-changee 1 "constante PLACE_MIN_KO ≠ 3000000" "sed -i 's/^PLACE_MIN_KO=3000000 /PLACE_MIN_KO=1000000 /' $V/recuperation_p4_v1.sh && resceller $V/recuperation_p4_v1.sh" ":" "" "" 2
jouer A52-garde-du-lanceur-autre 1 "empreinte de la garde gelée du lanceur ≠ module commun" "sed -i 's/^GARDE_SHA256=579f65c8/GARDE_SHA256=000f65c8/' $V/lancer_p4_v1.sh && resceller $V/lancer_p4_v1.sh" ":" "" "" 1
# chaîne v2 (RC-donnees-09) : tokeniseur de l'agent absent, altéré, sans sceau : KO net, mesures non rejouées
jouer T01-tokeniseur-absent 1 "tokeniseur de l'agent absent de S" "git rm -q donnees/P4-tokeniseur-v1/tokenizer.json donnees/P4-tokeniseur-v1/tokenizer.json.sha256" ":" "" "" 2
jouer T02-tokeniseur-altere 1 "tokeniseur de l'agent absent de S, sans son sceau ou d'empreinte autre" "echo ' ' >> donnees/P4-tokeniseur-v1/tokenizer_config.json && resceller donnees/P4-tokeniseur-v1/tokenizer_config.json && git add -f donnees/P4-tokeniseur-v1" ":" "" "" 2
jouer T03-tokeniseur-sans-sceau 1 "tokeniseur de l'agent absent de S, sans son sceau" "git rm -q donnees/P4-tokeniseur-v1/tokenizer_config.json.sha256" ":" "" "" 2
# chaîne v2 (RC-donnees-08) : liste des chemins gelés de S qui s'exclut elle-même et exclut un dossier changé
jouer G01-liste-des-chemins-geles-alteree 1 "arbre gelé de S ≠ celui de P3" "sed -i 's|\":(exclude)traces\", \":(exclude)CLAUDE.md\")|\":(exclude)traces\", \":(exclude)CLAUDE.md\", \":(exclude)src/controle_ia/sondes\", \":(exclude)src/controle_ia/harnais/validation_reelle.py\")|' src/controle_ia/harnais/validation_reelle.py && grep -q 'exclude)src/controle_ia/sondes' src/controle_ia/harnais/validation_reelle.py && echo '# essai' >> src/controle_ia/sondes/evaluation.py" ":"
jouer A44i-texte-sans-la-forme-d-accord 1 "valeur non citée par le texte : **Accord de Lazar pour le lancement de P4-instrument**" ":" "sed -i 's/\\*\\*Accord de Lazar pour le lancement de P4-instrument\\*\\*/Accord de Lazar pour le lancement de P4-instrument/g' $P"
# configuration de S changée : gardes du module (le KO « ≠ configuration relue » s'y ajoute)
jouer A45-phrase-b-autre-que-mc1 1 "B ou B′ de la configuration ≠ MC-1" ":" "python3 -c \"import json; f = '$CFG'; c = json.load(open(f)); c['phrases']['B'] = c['phrases']['candidates_B'][1]; open(f, 'w').write(json.dumps(c, indent=1, sort_keys=True))\" && cfg_citee"
jouer A46-mode-jouet 1 "gardes du module" ":" "cfg_set mode '\"jouet\"' && cfg_citee"
jouer A47-liste-du-niveau-1-autre 1 "gardes du module" ":" "python3 -c \"import json; f = '$CFG'; c = json.load(open(f)); c['taches_niveau_1'] = c['taches_niveau_1'][:-1]; open(f, 'w').write(json.dumps(c, indent=1, sort_keys=True))\" && cfg_citee"
# mesures de conception rejouées (bouchon : sortie scellée recopiée, altérée) ; sortie scellée de S altérée
jouer B00-mesures-rejouees-autre-b 1 "mesures de conception rejouées" ":" ":" "" "" 1 "FAUX_MC=b"
jouer B01-mesures-rejouees-autre-niveau-1 1 "mesures de conception rejouées" ":" ":" "" "" 1 "FAUX_MC=niveau1"
jouer B02-sortie-scellee-des-mesures-alteree 1 "gardes du module" "python3 -c \"import json; f = 'docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json'; d = json.load(open(f)); d['objet'] += ' (essai)'; open(f, 'w').write(json.dumps(d, indent=1, ensure_ascii=False, sort_keys=True) + '\\\\n')\" && resceller docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json" ":"
# dépendances (arbre gelé) ; verifier-arbre seul ; branche de résultats présente
jouer A53-dependances-autres 1 "arbre gelé" "echo 'paquet-essai==1.0' >> requirements-gpu.txt" ":"
jouer A54-verifier-arbre-seul 1 "verifier-arbre" "echo x >> docs/notes/P3-mesures-v2/puissance-p3-v1.txt" ":" "" "" 1
jouer A32-branche-presente 1 "branche calcul/p4-reel-v1 : code 0" ":" ":" "git push -q $R/distant.git art-A32-branche-presente:refs/heads/calcul/p4-reel-v1" "" 1
git -C "$R/distant.git" branch -D calcul/p4-reel-v1 > /dev/null
# épingles mal formées ou absentes, module commun absent, clonage impossible : code 2, rien n'est contrôlé
copie_ctl "$R/controles-Z1a.sh" "s/^CANDIDAT_RELU=[0-9a-f]\{64\}/CANDIDAT_RELU=A_EPINGLER/"
jouer Z1a-candidat-non-epingle 2 "candidat relu non épinglé" ":" ":" "" "$R/controles-Z1a.sh" 0
copie_ctl "$R/controles-Z1b.sh" "s|^CANDIDAT_RELU_CHEMIN=brouillons/|CANDIDAT_RELU_CHEMIN=prereg/|"
jouer Z1b-candidat-hors-des-brouillons 2 "candidat relu non épinglé" ":" ":" "" "$R/controles-Z1b.sh" 0
copie_ctl "$R/controles-Z1c.sh" "s/^CONFIG_RELUE=[0-9a-f]\{64\}/CONFIG_RELUE=A_EPINGLER/"
jouer Z1c-configuration-non-epinglee 2 "configuration relue non épinglée" ":" ":" "" "$R/controles-Z1c.sh" 0
copie_ctl "$R/controles-Z1d.sh" "s/^RAPPORTS_ATTENDUS=\"/RAPPORTS_ATTENDUS=\"P3-mal-forme.txt=00 /"
jouer Z1d-rapports-mal-formes 2 "rapports attendus mal formés" ":" ":" "" "$R/controles-Z1d.sh" 0
copie_ctl "$R/controles-Z1e.sh" "s/^RAPPORTS_ATTENDUS=\"\([^ \"]*\)[^\"]*\"/RAPPORTS_ATTENDUS=\"\1\"/"
jouer Z1e-un-seul-rapport 2 "noms exacts" ":" ":" "" "$R/controles-Z1e.sh" 0
copie_ctl "$R/controles-Z1e2.sh" "s/^RAPPORTS_ATTENDUS=\"/RAPPORTS_ATTENDUS=\"P4-essai-autre-v1.md=$(printf 'e%.0s' {1..64}) /"
jouer Z1e2-un-rapport-en-trop 2 "en trop ['P4-essai-autre-v1.md']" ":" ":" "" "$R/controles-Z1e2.sh" 0
copie_ctl "$R/controles-Z1f.sh" "s/^REPETITION_COMMIT=[0-9a-f]\{40\}/REPETITION_COMMIT=A_EPINGLER/"
jouer Z1f-commit-repete-non-epingle 2 "commit répété ou répétition jouet non épinglés" ":" ":" "" "$R/controles-Z1f.sh" 0
copie_ctl "$R/controles-Z1g.sh" "s/^REPETITION_JOUET=[0-9a-f]\{64\}/REPETITION_JOUET=A_EPINGLER/"
jouer Z1g-repetition-non-epinglee 2 "commit répété ou répétition jouet non épinglés" ":" ":" "" "$R/controles-Z1g.sh" 0
copie_ctl "$R/controles-Z1h.sh" "s|^VERIF=.*|VERIF=$R/module-absent/verifications_p4_v1.py|"
jouer Z1h-module-commun-absent 2 "module commun" ":" ":" "" "$R/controles-Z1h.sh" 0
copie_ctl "$R/controles-Z1i.sh" "s|^DEPOT=.*|DEPOT=$R/depot-absent.git|"
jouer Z1i-clonage-impossible 2 "clonage impossible" ":" ":" "" "$R/controles-Z1i.sh" 0
# arguments et dossiers (code 2, rien de contrôlé ; le dossier de travail existant n'est jamais supprimé)
direct() {   # $1 nom, $2 motif de la dernière ligne, puis les arguments des contrôles
    local nom=$1 motif=$2 c v="CONFORME"; shift 2
    bash "$R/controles-essai.sh" "$@" > "$R/sortie-$nom.txt" 2>&1; c=$?
    [ "$c" = 2 ] || v="NON CONFORME (code $c, attendu 2)"
    tail -1 "$R/sortie-$nom.txt" | grep -qF -- "$motif" || v="NON CONFORME (motif « $motif » absent)"
    [ "$(grep -c '^OK\|^KO' "$R/sortie-$nom.txt")" = 0 ] || v="NON CONFORME (lignes OK ou KO)"
    [ "$v" = CONFORME ] || NON_CONFORMES=$((NON_CONFORMES + 1))
    echo "$nom : code $c ; $v"; tail -1 "$R/sortie-$nom.txt" | couper 160 | sed 's/^/    | /'
}
S_SAIN=$(git rev-parse art-A00-sain)
mkdir -p "$R/existant" "$R/travail-existe.travail"; echo garde > "$R/travail-existe.travail/temoin"
direct Z2a-dossier-existant "existe déjà" "$S_SAIN" "$R/existant"
direct Z2b-dossier-de-travail-existant "existe déjà" "$S_SAIN" "$R/travail-existe"
[ -f "$R/travail-existe.travail/temoin" ] && echo "    dossier de travail existant gardé : CONFORME" || { echo "    dossier de travail existant supprimé : NON CONFORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
direct Z2c-troisieme-argument "usage" "$S_SAIN" "$R/clone-Z2c" relance
direct Z2d-dossier-vide "dossier neuf absent" "$S_SAIN" ""
direct Z2e-s-invalide "S invalide" "abc" "$R/clone-Z2e"
echo garde > "$R/suite-existe.suite.txt"
direct Z2f-trace-de-la-suite-existante "suite.txt existe déjà (R12)" "$S_SAIN" "$R/suite-existe"
direct Z2g-s-bien-forme-mais-absent "introuvable" "$(printf '0%.0s' {1..40})" "$R/clone-Z2g"
rm -rf "$R/clone-Z2g"
# la copie versée (épingles « A_EPINGLER ») refuse de contrôler quoi que ce soit : code 2
bash "$HN/controles_avant_depense_p4_v1.sh" "$S_SAIN" "$R/clone-Z3" > "$R/sortie-Z3.txt" 2>&1; c=$?
[ "$c" = 2 ] && tail -1 "$R/sortie-Z3.txt" | grep -qF "non épinglés" && [ ! -e "$R/clone-Z3" ] && echo "Z3-epingles-du-bloc-notes-a-poser : code 2 ; CONFORME" \
    || { echo "Z3-epingles-du-bloc-notes-a-poser : code $c ; NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
P_CACHE=$(find "$R/source/src" "$R/source/$V" "$HN" -name __pycache__ 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : NON CONF""ORME"; NON_CONFORMES=$((NON_CONFORMES + 1)); }
echo "FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : $NON_CONFORMES"
[ "$NON_CONFORMES" = 0 ] || exit 1
