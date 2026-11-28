#!/usr/bin/env bash
# Contrôles avant dépense de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269 ; préenregistrement
# prereg/P4-instrument-v1.md), v1, déclinés de docs/procedures/P3-premier-test-v2/controles_avant_depense_p3_v1.sh sous
# un nom neuf (R12). Sur un clone neuf du dépôt de travail au commit de scellement S ; aucun calcul payant ; code 0 si et
# seulement si tout est conforme ; code 2 si les épingles manquent ou sont mal formées, si le module commun manque, ou si
# le clone est impossible.
# Ce qui est contrôlé : 1 S ajoute le sceau du préenregistrement et n'ajoute que le texte, la configuration et leurs
# sceaux ; 2 commit du code cité une seule fois, ancêtre de S, arbre gelé de S identique au code cité et à celui de P3
# (`7a54d43`, instrument figé ; il porte aussi les dépendances), amorce et script de l'instance cités par leur
# empreinte ; 3 configuration présente et scellée ; données de P3 de la table « Données lues » présentes à S, scellées,
# à l'empreinte écrite (R11 ; empreintes seulement, aucun texte lu) ; 4 GO et dépense, par le module commun
# verifications_p4_v1.py (fonctions du module de P4 : GO-2026-10-20-07 seul, huit colonnes, type « calcul », Lazar,
# plafond « 10 USD par lancement », échéance de sa colonne, borne de l'étape sous 10 USD, révocations sous leurs deux
# formes, garde de calcul gelée rejouée), sur les registres de S ; module de P4 : les six fichiers cités, et eux
# seuls ; 5 texte et configuration de S égaux aux candidats relus, octet pour octet ; 6 journal de la répétition jouet
# épinglé, au commit répété épinglé (arbre gelé, module et scripts de l'instance égaux à ceux de S) et au candidat
# relu, conforme au module commun ; scripts répétés égaux à leurs copies versées à S ; 7 rapports de contre-lecture
# présents, scellés, cités, seuls de leur famille ; 8 branche de résultats absente ; ligne « Lancement » ;
# problemes() vide ; sceaux ; verifier-arbre ; 9 gardes du module de P4 rejouées dans l'ordre du run jusqu'au manifeste
# (rien n'est écrit) : configuration réelle aux valeurs du texte, citations (configuration, entropie, révision), code
# importé du dépôt, code cité, instrument figé, module cité, sources de P3 à leur empreinte (sceau et empreinte écrite,
# sans lecture des textes), run source décisif, révision du run source, liste des épisodes du niveau 1 relue dans la
# sortie scellée de MC-2 ; table « Données lues » égale aux empreintes du module ; B et B′ de la configuration égaux à
# ceux de MC-1 ; bornes de la chaîne reliées aux constantes des scripts (délai du run 90 minutes, plafond de l'amorce
# 150 minutes, crédit sur 3,0 heures, surveillance 9 600 s, prix, cœurs, mémoire vive, téléchargement, stockage, borne
# de l'étape 5,41 USD, GO cité, instance tolérée) et aux valeurs citées par le texte, dont les formes exactes de
# l'accord, des révocations et du plafond lues dans le module ; 10 mesures de conception MC-1 à MC-3 rejouées sur le
# vrai tokeniseur de l'agent (copie de la session, empreinte écrite) : sortie neuve dans le dossier de travail, égale à
# la sortie scellée de S hors des empreintes du module et des versions (aucun texte d'action affiché ni écrit hors du
# dossier de travail, effacé à la fin) ; 11 versions de l'environnement de la session égales aux dépendances
# épinglées, puis suite complète des tests au commit S (dépôt et module), au nombre cité ; 12 garde de calcul sur le
# registre de S ; 13 lecture précoce du script de l'instance ; 14 intitulés lus une fois chacun. Les citations qui
# peuvent passer à la ligne dans le texte (rapports, empreintes des scripts de l'instance) sont lues sur le texte aux
# espaces réduites. Aucun relancement : une relance passe par un nœud de Lazar et une chaîne suivante.
# Chaîne v2 : liste des chemins gelés lue dans `7a54d43` (`git show` du fichier qui la définit), jamais dans l'arbre
# contrôlé (RC-donnees-08) ; tokeniseur de l'agent lu dans le clone, sous `donnees/P4-tokeniseur-v1/`, versé par la
# session avec ses sceaux, à ses deux empreintes (79e3e522…, 177c7b61…) ; absent ou autre : KO net, mesures de
# conception non rejouées (RC-donnees-09) ; rapports attendus aux noms exacts du module commun (RC-fidelite-12) ;
# journal de la répétition jouet à cinq passages, sept récupérations conformes, vingt-sept artefacts et trois refus
# (chaîne v3 : état et heure limite dans les refus de la place et du clonage), repli de l'affichage,
# quatre scripts répétés (RC-fidelite-07) ; bornes des scripts neufs (arrêt, surveillance, cinq minutes, récupération)
# reliées au texte ; valeurs neuves lues dans le texte (forme de la dépense de la phase, script d'arrêt, contrôle des
# traces, tokeniseur versé, empreinte de la garde gelée). Module v2 : la suite complète tourne avec P4_TEXTE_PREREG = le
# texte de S (égal au candidat relu), -B et PYTHONDONTWRITEBYTECODE=1. Chaîne v3 : vingt-six rapports ; trois refus de la
# récupération ; repli de l'affichage. Chaîne v4 (traitement de la vérification « fidélité » de la chaîne v2) :
# vingt-sept rapports (RAPPORTS_NOMS du module commun) ; journal de la répétition jouet à six passages (le sixième :
# délai externe du run), neuf récupérations conformes, état et heure limite dans les trois refus, deux replis de
# l'affichage ; bloc 12 : empreinte de la garde gelée relue immédiatement avant son rejeu, égale à celle du module
# commun (GARDE_SHA256), sinon KO et aucun rejeu (VC2-fidelite-12).
# Épingles : posées par la session quand le candidat, la configuration relue, les rapports et le journal de la
# répétition jouet existent (« A_EPINGLER » d'ici là : code 2, rien n'est contrôlé).
# Usage : controles_avant_depense_p4_v1.sh S DOSSIER_NEUF
set -uo pipefail
[ $# -eq 2 ] || { echo "usage : controles_avant_depense_p4_v1.sh S DOSSIER_NEUF (deux arguments ; aucun relancement)"; exit 2; }
S=$1; D=$(realpath -m "$2")
DEPOT=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/bloc-notes-session14/p4-instrument/chaine-v4-travail/passe-1/controles/distant.git
CANDIDAT_RELU=8149056d08b1fdd300ac2e34e8086cff60336617474c6b9aaefe449ffb2c60bc                                     # texte relu et vérifié (contre-lecture 3), octet pour octet
CANDIDAT_RELU_CHEMIN=brouillons/P4-instrument-v1-candidat-essai.md                              # brouillons/P4-instrument-v1-candidat<k>.md
CONFIG_RELUE=76d10700d860e2fd99053fdb672a24fb6a80260cfbfbe331323c836d10ac270e                                      # configuration relue, octet pour octet
CONFIG_RELUE_CHEMIN=brouillons/P4-instrument-config-v1-candidat-essai.json                               # brouillons/P4-instrument-config-v1-candidat<k>.json
RAPPORTS_ATTENDUS="contre-lecture-R2-P4-instrument-brouillon1-v1.md=51c04b3f871058e30e30b2be0fd23afabbf8634bdb489a69bffed60257e4a1f0 traitement-R2-P4-instrument-brouillon1-v1.md=1c8915baa01f2a8e7019c89d6257fa41d52b1a5411b50f583157e6c284059f84 traitement-gemini-014-P4-instrument-v1.md=17a1b175917c25bfe32bf230752ef8deb94afb0db8d5959b9a69fedfd48dc53a verification-corrections-brouillons2-3-P4-v1.md=e772998ac1f7d6b68761ada82cdc11c7c9ed5f93206ed23fdcd29fcf3c71819f traitement-verification-P4-instrument-v1.md=ef0d4129674a3992ef72cacd44c4cdd8897c8d4c66707b0ab5103079b04c6db7 contre-lecture-3-P4-instrument-candidat1-v1.md=ff961f28f61361ffe81928bf64d06af0b41da1a530220f8e9b516088ef7d9fe2 relecture-chaine-depense-P4-instrument-v1.md=c5f8448dd957fa1ccffa9b771458ed28fcefdbc33f3fbd675605f9b5b2c5743d relecture-chaine-donnees-P4-instrument-v1.md=b747d958549d4f8c436f83a19a1c257d428eeabe58d97b33b7995a2276ad573d relecture-chaine-fidelite-P4-instrument-v1.md=b8d11617e90e3af15d5ffc3a0490b8dbdc21e5c296c4b9e1e0284145d52d8463 traitement-CL3-et-relectures-chaine-P4-v1.md=ec09472676adc2e1adb00146d96f87555515d8dccbac5206ef980f50a76dcaf5 verification-module-v2-contournement-P4-instrument-v1.md=da024c86cb122d6b096400ae45968ae184b6f2669e046d25db23f98f7e106c28 verification-module-v2-fidelite-P4-instrument-v1.md=325ce490c6abaf3cb375dd11fae1cd785f983d4c9fd9e659228aa779981f5a1c traitement-verifications-module-v2-P4-v1.md=c44f7faba20ef3ee65dd6ba9b3679d2e739ae66856b56df4e6a05cb6266b3846 verification-module-v3-P4-instrument-v1.md=88e72775a6bbc9f1c245fcbe0aa8be25e1685d3d508be2a85f99f96b557912f2 verification-chaine-v2-depense-P4-instrument-v1.md=91f2a5ef7fb83f0b2a9e262a38b31bd9b7d9214c331cc7f66a30db9bb2b0d8b9 verification-chaine-v2-donnees-P4-instrument-v1.md=7dfba94e8245b09d15ac0e2919402b7a274f14d3a03586bab77e75ba35d2ec54 verification-chaine-v2-fidelite-P4-instrument-v1.md=a8a27198f3e1764be4c2b4f5af17c054b4aa3a983e09d8700d9fb7cf45369c8e traitement-verifications-chaine-v2-P4-v1.md=da681b40eb5a6bd047b26ae3f1a36e9a807aba2acc4d34f5e105baa6c39f7b49 traitement-verification-fidelite-chaine-v2-P4-v1.md=b74d11ba18e2940cac4815e103c305cb7ea51301eb1a30b5dc94a9ff72be3f2a verification-chaine-v4-P4-instrument-v1.md=09547cfaaa968631822fa433af7ab77f3e1ef85368a1e39341108f989d3c2b1d verification-candidat2-P4-instrument-v1.md=d988542825dac3d0fa382ba4e239ea6cfb2b386ad663e060f1ea1a869e75f7f5 P4-instrument-v1-brouillon1.md=1b945b53e12b2ad48f006f900110226cf645763682acdfd2c3aa9e61984ae7ab P4-instrument-v1-brouillon2.md=0ccf151647d34d907cd128d9a85b3c97de7d2a3e1b593a2ff723f14c7ccb6927 P4-instrument-v1-brouillon3.md=703262c2e41a689e6e32a93f31d7d2ef086fc65f7e146bf18d720af594fb50f0 P4-instrument-v1-brouillon4.md=304e78cb96c9215bf1cf638dae27a334430d40ee96da7a57468820dd16fb52d8 P4-instrument-v1-candidat1.md=580841fb1d327cf44494fd8a745c9d840e5c1ffc5d2d22f251835e547c50949e P4-instrument-v1-candidat2.md=a141e7712a088d2d86c08f95c66df65e86cdd2dabb4380c9e120752d045b5f35"                               # paires nom=empreinte des rapports versés sous prereg/contre-lectures/
CODE_RELU=7a54d431d89745839220f882b41b13e8c62ecfdd           # arbre gelé de P3 (instrument figé) : arbre gelé de S égal
REPETITION_COMMIT=A_EPINGLER                                 # commit répété par la répétition jouet (module et chaîne versés)
REPETITION_JOUET=01b4a87c2c51e3e4365bd5cdb0f6c7fb90f8a2a316df6847e6aa8d21b3b7e6e8                                  # empreinte du journal de la répétition jouet
REPETITION_JOUET_CHEMIN=docs/procedures/P4-instrument-v1/repetition-jouet-p4-v1.log
TOKENISEUR=donnees/P4-tokeniseur-v1            # dans le clone de S : versé par la session avec ses sceaux (RC-donnees-09)
TOK_JSON=79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4     # tokenizer.json de l'agent
TOK_CONFIG=177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424   # tokenizer_config.json de l'agent
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v4
VERIF=$H/verifications_p4_v1.py                     # module commun (égal à sa copie versée : le lanceur le vérifie)
VERSEES=docs/procedures/P4-instrument-v1
P=prereg/P4-instrument-v1.md; CFG=prereg/P4-instrument-config-v1.json
MODULE=$VERSEES/instrument_p4_v1.py; MESURES=$VERSEES/mesures_conception_p4_v1.py
MC=docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json
AMORCE=$VERSEES/amorce_instance_p4_v1.sh; INSTANCE=$VERSEES/p4_instance_v1.sh
TESTS_MODULE="$VERSEES/test_instrument_p4_v1.py $VERSEES/test_lecture_p4_v1.py $VERSEES/test_gardes_p4_v1.py"
BRANCHE=calcul/p4-reel-v1
SCRIPTS_REPETES="recuperation_p4_v1.sh repetition_jouet_p4_v1.sh outils_essais_p4_v1.py verifications_p4_v1.py"
export PYTHONDONTWRITEBYTECODE=1
echec=0; ok() { echo "OK  $*"; }; ko() { echo "KO  $*"; echec=1; }
plat() { tr '\n' ' ' < "$1" | tr -s ' '; }      # texte aux espaces réduites : citations passées à la ligne
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[ -n "$2" ] || { echo "dossier neuf absent"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà"; exit 2; }
[[ "$CODE_RELU" =~ ^[0-9a-f]{40}$ && "$REPETITION_COMMIT" =~ ^[0-9a-f]{40}$ && "$REPETITION_JOUET" =~ ^[0-9a-f]{64}$ ]] \
    || { echo "code relu, commit répété ou répétition jouet non épinglés"; exit 2; }
[[ "$CANDIDAT_RELU" =~ ^[0-9a-f]{64}$ && "$CANDIDAT_RELU_CHEMIN" == brouillons/* ]] || { echo "candidat relu non épinglé"; exit 2; }
[[ "$CONFIG_RELUE" =~ ^[0-9a-f]{64}$ && "$CONFIG_RELUE_CHEMIN" == brouillons/* ]] || { echo "configuration relue non épinglée"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
# rapports attendus : les noms exacts du module commun (RAPPORTS_NOMS), une fois chacun (RC-fidelite-12)
# shellcheck disable=SC2086
R_SORTIE=$("$PY" -B "$VERIF" rapports $RAPPORTS_ATTENDUS 2>&1) || { echo "rapports attendus : $(printf '%s\n' "$R_SORTIE" | tail -1 | cut -c1-220)"; exit 2; }
n_paires=$(printf '%s\n' "$R_SORTIE" | grep -c '^rapport attendu : ')
W="$D.travail"                                   # fichiers de travail dans un dossier neuf, à côté du clone
[ -e "$W" ] && { echo "$W existe déjà"; exit 2; }
[ -e "$D.suite.txt" ] && { echo "$D.suite.txt existe déjà (R12)"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
mkdir -p "$W" || exit 2
trap 'rm -rf "$W"' EXIT                          # fichiers de travail jamais laissés, même sur un arrêt précoce
git clone -q "$DEPOT" "$D" || { echo "clonage impossible"; exit 2; }
cd "$D" && git checkout -q "$S" || { echo "commit $S introuvable"; exit 2; }
JOUR=$(date -u +%F)
# 1. contenu de S : les quatre fichiers, tous ajoutés par S
[ "$(git log --diff-filter=A -1 --format=%H -- "$P.sha256")" = "$S" ] && ok "S ajoute le sceau du préenregistrement" || ko "S n'est pas le commit qui ajoute $P.sha256"
attendus_s=$(printf '%s\n' "$CFG" "$CFG.sha256" "$P" "$P.sha256" | sort | tr '\n' ' ')
[ "$(git diff --name-only --no-renames "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] && \
    [ "$(git diff --name-only --no-renames --diff-filter=A "$S^" "$S" | sort | tr '\n' ' ')" = "$attendus_s" ] \
    && ok "S n'ajoute que le texte, la configuration et leurs sceaux" \
    || ko "contenu de S inattendu : $(git diff --name-status --no-renames "$S^" "$S" | tr '\t\n' '  ' | cut -c1-200)"
# 2. commit du code : cité une seule fois, ancêtre de S ; arbre gelé de S identique au code cité et à celui de P3
NC=$(grep -c "Commit du code d'analyse : \`" "$P" || true)
CODE=$(sed -n "s/.*Commit du code d'analyse : \`\([0-9a-f]\{40\}\)\`.*/\1/p" "$P" | head -1)
if [ "$NC" = 1 ] && [[ "$CODE" =~ ^[0-9a-f]{40}$ ]] && git merge-base --is-ancestor "$CODE" "$S" 2>/dev/null; then ok "commit du code cité une fois, $CODE, ancêtre de S"
else ko "commit du code cité illisible, cité $NC fois, ou non ancêtre de S"; CODE=$S; fi
# liste des chemins gelés lue dans le commit de P3 (instrument figé), jamais dans l'arbre contrôlé (RC-donnees-08)
GELES=$(git show "$CODE_RELU:src/controle_ia/harnais/validation_reelle.py" 2>/dev/null | "$PY" -I -B -c 'import ast, sys
t = ast.parse(sys.stdin.read())
v = [n.value for n in t.body if isinstance(n, ast.Assign) and any(getattr(x, "id", "") == "CHEMINS_GELES" for x in n.targets)]
assert len(v) == 1
print(" ".join(ast.literal_eval(v[0])))' 2>/dev/null)
if [ -n "$GELES" ]; then
    # shellcheck disable=SC2086
    git diff --quiet "$CODE" "$S" -- $GELES; c=$?
    case $c in 0) ok "arbre gelé (CHEMINS_GELES) identique au commit du code" ;; 1) ko "arbre gelé modifié depuis le commit du code" ;;
               *) ko "comparaison de l'arbre gelé impossible (code $c)" ;; esac
    # shellcheck disable=SC2086
    git diff --quiet "$CODE_RELU" "$S" -- $GELES; c=$?
    case $c in 0) ok "arbre gelé de S = celui de P3 ($CODE_RELU : instrument figé, dépendances comprises)" ;; 1) ko "arbre gelé de S ≠ celui de P3 ($CODE_RELU)" ;;
               *) ko "comparaison à l'arbre de P3 impossible (code $c)" ;; esac
else ko "CHEMINS_GELES illisible dans $CODE_RELU"; fi
for f in "$AMORCE" "$INSTANCE"; do
    e=$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)
    plat "$P" | grep -qF "\`$f\` (\`$e\`, sha256)" && ok "empreinte de $f citée ($e)" || ko "empreinte de $f ($e) non citée"
done
# 3. configuration présente à S avec son sceau entier ; données de P3 de la table « Données lues » : présentes à S,
# scellées, à l'empreinte écrite (empreintes seulement)
if git cat-file -e "$S:$CFG" 2>/dev/null && [ "$(git show "$S:$CFG.sha256" 2>/dev/null)" = "$(git show "$S:$CFG" | sha256sum | cut -d' ' -f1)  $(basename "$CFG")" ]; then
    ok "$CFG et son sceau entier dans l'arbre de S"
else ko "$CFG ou son sceau absent ou non conforme"; fi
grep -E '^\| `[^`]+` \| `[0-9a-f]{64}` \|' "$P" | sed -E 's/^\| `([^`]+)` \| `([0-9a-f]{64})` \|.*/\1 \2/' > "$W/table-donnees.txt"
NT=$(grep -c . "$W/table-donnees.txt" || true)
FAUTES_T=""
while read -r f e; do
    if git cat-file -e "$S:$f" 2>/dev/null && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $(basename "$f")" ] \
       && [ "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)" = "$e" ]; then :; else FAUTES_T="$FAUTES_T $f"; fi
done < "$W/table-donnees.txt"
[ "$NT" = 10 ] && [ -z "$FAUTES_T" ] && ok "table « Données lues » : 10 fichiers présents à S, scellés, à l'empreinte écrite" \
    || ko "table « Données lues » : $NT ligne(s) ; absents, non scellés ou d'empreinte autre :$(printf '%s' "$FAUTES_T" | cut -c1-200)"
# 4. GO et dépense (module commun : fonctions du module de P4, sur les registres de S) ; module de P4 cité
BORNE=$(sed -n 's/^BORNE_ETAPE_USD=\([0-9.]*\) .*/\1/p' "$VERSEES/lancer_p4_v1.sh" 2>/dev/null)
PYTHONPATH=src "$PY" -B "$VERIF" go . "$P" "$JOUR" "${BORNE:-0}" > "$W/bloc-go.txt" 2>&1 \
    && ok "GO et dépense : $(tail -1 "$W/bloc-go.txt" | cut -c1-200)" \
    || ko "GO et dépense (GO cité, plafond, échéance, borne, révocation ou garde gelée) : $(tail -1 "$W/bloc-go.txt" | cut -c1-200)"
PYTHONPATH=src "$PY" -B "$VERIF" module . "$P" > "$W/bloc-module.txt" 2>&1 \
    && ok "module de P4 : $(grep -c . "$W/bloc-module.txt") fichiers cités, à l'empreinte citée, et eux seuls" \
    || ko "module de P4 : $(tail -1 "$W/bloc-module.txt" | cut -c1-200)"
# 5. texte et configuration de S = candidats relus, versés et scellés à l'empreinte épinglée
releve() {   # $1 fichier de S, $2 chemin du relu versé, $3 empreinte épinglée, $4 nom du relu, $5 accord (e ou rien)
    [ "$(git show "$S:$2" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$3" ] && \
        [ "$(git show "$S:$2.sha256" 2>/dev/null)" = "$3  $(basename "$2")" ] \
        && ok "$4 versé$5, scellé$5, à l'empreinte épinglée" || ko "$4 absent$5, non scellé$5 ou d'empreinte différente"
    [ "$(sha256sum "$1" | cut -d' ' -f1)" = "$3" ] && ok "$1 de S = $4, octet pour octet" || ko "$1 de S ≠ $4"
}
releve "$P" "$CANDIDAT_RELU_CHEMIN" "$CANDIDAT_RELU" "candidat relu" ""
releve "$CFG" "$CONFIG_RELUE_CHEMIN" "$CONFIG_RELUE" "configuration relue" "e"
# 6. journal de la répétition jouet : épinglé, scellé ; commit répété ancêtre de S, d'arbre gelé égal à celui de P3, au
# module et aux scripts de l'instance de S ; candidat relu ; récupérations et artefacts attendus ; scripts répétés =
# copies versées à S
CAUSE_REP=""
git show "$S:$REPETITION_JOUET_CHEMIN" > "$W/journal-repetition.txt" 2>/dev/null
"$PY" -B "$VERIF" repetition "$REPETITION_COMMIT" "$W/journal-repetition.txt" "$(basename "$CANDIDAT_RELU_CHEMIN")" "$CANDIDAT_RELU" \
    > "$W/bloc-repetition.txt" 2>&1 || CAUSE_REP=$(tail -1 "$W/bloc-repetition.txt" | cut -c1-200)
if [ -z "$CAUSE_REP" ]; then
    grep -E '^[a-z0-9_]+_v1\.(py|sh) [0-9a-f]{64}$' "$W/bloc-repetition.txt" > "$W/scripts-repetes.txt"
    while read -r s e; do
        [ "$(git show "$S:$VERSEES/$s" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] || CAUSE_REP="script répété ≠ copie versée à S : $s"
    done < "$W/scripts-repetes.txt"
fi
if [ -z "$CAUSE_REP" ]; then
    { [ "$(git show "$S:$REPETITION_JOUET_CHEMIN" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$REPETITION_JOUET" ] && \
      [ "$(git show "$S:$REPETITION_JOUET_CHEMIN.sha256" 2>/dev/null)" = "$REPETITION_JOUET  $(basename "$REPETITION_JOUET_CHEMIN")" ]; } \
        || CAUSE_REP="journal absent de S, d'une autre empreinte que l'épingle, ou sceau différent"
fi
if [ -z "$CAUSE_REP" ]; then
    git merge-base --is-ancestor "$REPETITION_COMMIT" "$S" 2>/dev/null || CAUSE_REP="commit répété $REPETITION_COMMIT non ancêtre de S"
fi
if [ -z "$CAUSE_REP" ]; then
    # shellcheck disable=SC2086
    git diff --quiet "$REPETITION_COMMIT" "$CODE_RELU" -- $GELES 2>/dev/null || CAUSE_REP="commit répété d'arbre gelé autre que celui de P3"
    # shellcheck disable=SC2086
    git diff --quiet "$REPETITION_COMMIT" "$S" -- "$MODULE" $TESTS_MODULE "$MESURES" "$VERSEES/lecture_p4_v1.py" "$AMORCE" "$INSTANCE" 2>/dev/null \
        || CAUSE_REP="module ou scripts de l'instance du commit répété ≠ ceux de S"
fi
if [ -z "$CAUSE_REP" ]; then
    ok "répétition jouet au commit répété et au candidat relu : journal épinglé, scellé ; six passages (délai externe du run compris), neuf récupérations conformes suivies de la destruction, vingt-sept artefacts refusés à leur KO, trois refus (état et heure limite dans chacun), deux replis de l'affichage ; quatre scripts répétés = copies versées à S ; module et scripts de l'instance du commit répété = ceux de S"
else ko "répétition jouet : $CAUSE_REP"; fi
# 7. rapports de la contre-lecture : présents à S, scellés, cités (texte aux espaces réduites) ; seuls de leur famille
for paire in $RAPPORTS_ATTENDUS; do
    nom=${paire%%=*}; e=${paire#*=}; f="prereg/contre-lectures/$nom"
    if [ "$(git show "$S:$f" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$e" ] && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  $nom" ]; then
        plat "$P" | grep -qF "\`$f\` (\`$e\`)" && ok "rapport $nom présent, scellé, cité" || ko "rapport $nom présent et scellé, mais non cité par le texte"
    else ko "rapport $nom absent, non scellé ou d'empreinte différente"; fi
done
presents=$(git ls-tree -r --name-only "$S" prereg/contre-lectures/ | grep -E '/[^/]*P4[^/]*$' | grep -v '\.sha256$' | xargs -r -n1 basename | sort | tr '\n' ' ')
attendus=$(for paire in $RAPPORTS_ATTENDUS; do echo "${paire%%=*}"; done | sort | tr '\n' ' ')
[ "$presents" = "$attendus" ] && ok "rapports de P4 présents à S = rapports attendus, aux noms exacts du module commun ($n_paires)" || ko "rapports présents « $(printf '%s' "$presents" | cut -c1-150) » ≠ attendus"
# 8. branche de résultats absente ; ligne « Lancement » ; problemes() ; sceaux ; arbre
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1; c=$?
[ "$c" = 2 ] && ok "branche $BRANCHE absente" || ko "branche $BRANCHE : code $c (2 attendu)"
grep -qF "\`PREREG=$P\`, \`BRANCHE=$BRANCHE\`" "$P" && ok "PREREG et BRANCHE ($BRANCHE) cités par la ligne « Lancement »" || ko "PREREG ou BRANCHE : la ligne « Lancement » cite autre chose"
PYTHONPATH=src "$PY" -B -c "from controle_ia.prereg import problemes; p = problemes('$P'); print(p); raise SystemExit(1 if p else 0)" > "$W/problemes.txt" 2>&1 \
    && ok "problemes() vide" || ko "problemes() non vide : $(tail -1 "$W/problemes.txt" | cut -c1-160)"
# shellcheck disable=SC2086
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier "$P" "$CFG" "$MODULE" "$MESURES" "$VERSEES/lecture_p4_v1.py" $TESTS_MODULE "$MC" >/dev/null 2>&1 \
    && ok "sceaux du texte, de la configuration, du module et de la sortie des mesures de conception" || ko "sceaux"
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier-arbre . > "$W/verifier-arbre.txt" 2>&1
if tail -1 "$W/verifier-arbre.txt" | grep -qx "arbre intact"; then ok "verifier-arbre : arbre intact"
else ko "verifier-arbre : $(grep '^ÉCHEC' "$W/verifier-arbre.txt" | head -5 | tr '\n' ' ' | cut -c1-200)"; fi
# 9. gardes du module de P4 rejouées dans l'ordre du run, jusqu'au manifeste (rien n'est écrit ; la mémoire vive porte
# sur l'instance) ; table « Données lues » = empreintes du module ; B et B′ = MC-1 ; bornes de la chaîne reliées aux
# constantes des scripts de l'instance et des copies versées ; valeurs citées par le texte (aux espaces réduites)
PYTHONPATH=src "$PY" -B - "$P" "$CFG" "$VERSEES" "$MC" "$W/table-donnees.txt" > "$W/bloc-gardes.txt" 2>&1 <<'EOF' && ok "gardes du module de P4 (configuration réelle, citations, code, instrument figé, module, sources de P3, run source, niveau 1), table des données, B et B′, bornes de la chaîne, valeurs du texte" || ko "gardes du module, table, phrases, bornes ou valeurs : $(tail -1 "$W/bloc-gardes.txt" | cut -c1-200)"
import hashlib, importlib.util, json, re, sys
from pathlib import Path
from controle_ia.harnais.validation_reelle import exiger_code_cite, exiger_code_importe_sous
from controle_ia.manifeste import lire_manifeste
p, cfg_p, versees, mc_p, table = sys.argv[1:6]
racine = Path(".")
texte_brut = Path(p).read_text(encoding="utf-8")
chemin_m = f"{versees}/instrument_p4_v1.py"
lm = re.findall(r"^[ \t]*-[ \t]+Module de P4 : `" + re.escape(chemin_m) + r"` : `([0-9a-f]{64})`[ \t]*$", texte_brut, re.M)
assert len(lm) == 1 and hashlib.sha256(Path(chemin_m).read_bytes()).hexdigest() == lm[0], "module de P4 non cité à son empreinte"
spec = importlib.util.spec_from_file_location("instrument_p4_v1", chemin_m)
ip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ip)
c = json.loads(Path(cfg_p).read_text(encoding="utf-8"))
ip.exiger_config_p4(c)
assert c["mode"] == "reel", f"mode {c['mode']}"
ent = ip.exiger_citations_p4(Path(p), c)
assert ent == ip.ENTROPIE_P4, "entropie citée ≠ entropie du module"
exiger_code_importe_sous(racine)
commit = exiger_code_cite(racine, Path(p))
ip.exiger_instrument_fige(racine, ip.COMMIT_P3)
cites = ip.exiger_module_cite(racine, Path(p))
emp, run = c["empreintes_sources"], c["run_source"]
ip.exiger_chemins_du_run_source(emp, run)
shas = {cle: ip._exiger_source(racine, emp, cle) for cle in ip.CLES_SOURCES}      # sceau et empreinte écrite (R11)
m3, _ = lire_manifeste(racine / emp["manifeste"]["chemin"])
assert m3.get("run_id") == run and m3.get("decisif") is True and m3["config"].get("mode") == "reel", "run source non décisif ou hors du mode réel"
ip.exiger_revision_citee(Path(p), m3["config"])
n1 = ip.exiger_taches_niveau_1(racine, c)
lignes = [l.split() for l in Path(table).read_text(encoding="utf-8").splitlines() if l.strip()]
assert sorted((x["chemin"], x["sha256"]) for x in emp.values()) == sorted((a, b) for a, b in lignes), "table « Données lues » ≠ empreintes du module"
mc = json.loads(Path(mc_p).read_text(encoding="utf-8"))["MC-1"]
assert (c["phrases"]["B"], c["phrases"]["Bprime"]) == (mc["B"], mc["Bprime"]), "B ou B′ de la configuration ≠ MC-1"
# bornes : une seule ligne chacune, à la valeur du texte
inst = Path(f"{versees}/p4_instance_v1.sh").read_text(encoding="utf-8")
amorce = Path(f"{versees}/amorce_instance_p4_v1.sh").read_text(encoding="utf-8")
assert inst.count("DELAI=(timeout --signal=TERM --kill-after=5m 90m)") == 1, "délai externe du run"
assert amorce.count("timeout --signal=TERM --kill-after=5m 150m ") == 1, "plafond de l'amorce"
lanceur = Path(f"{versees}/lancer_p4_v1.sh").read_text(encoding="utf-8")
surv = Path(f"{versees}/surveiller_p4_v1.sh").read_text(encoding="utf-8")
cinq = Path(f"{versees}/controle_cinq_minutes_p4_v1.sh").read_text(encoding="utf-8")
arret = Path(f"{versees}/arreter_p4_v1.sh").read_text(encoding="utf-8")
recup = Path(f"{versees}/recuperation_p4_v1.sh").read_text(encoding="utf-8")
verif_t = Path(f"{versees}/verifications_p4_v1.py").read_text(encoding="utf-8")
def constante(t, nom, motif=r"[0-9.]+"):
    return re.findall(rf"^{nom}=({motif}) ", t, re.M)
for t_, nom, val in ((lanceur, "HEURES_CREDIT", "3.0"), (lanceur, "PRIX_MAX", "1.30"), (cinq, "PRIX_MAX", "1.30"),
                     (lanceur, "PLAFOND_SURVEILLANCE_S", "9600"), (surv, "PLAFOND_S", "9600"), (lanceur, "COEURS_MIN", "16"),
                     (lanceur, "MEMOIRE_VIVE_MIN_MO", "128000"), (lanceur, "TELECHARGEMENT_MAX", "0.05"),
                     (lanceur, "STOCKAGE_MAX", "0.03"), (lanceur, "BORNE_ETAPE_USD", "5.41"), (lanceur, "ARRET_MIN", "10"),
                     (lanceur, "TELECHARGEMENT_GO", "20"), (lanceur, "DISQUE_H", "24"),
                     (cinq, "TELECHARGEMENT_MAX", "0.05"), (cinq, "STOCKAGE_MAX", "0.03"),
                     (surv, "INTERVALLE_MIN", "10"), (surv, "INTERVALLE_MAX", "300"), (arret, "PAS_S", "10"),
                     (arret, "LECTURES_MAX", "60"), (recup, "PLAFOND_SURVEILLANCE_S", "9600"), (recup, "DISQUE_H", "24"),
                     (recup, "PLACE_MIN_KO", "3000000")):
    assert constante(t_, nom) == [val], f"constante {nom} ≠ {val}"
assert constante(lanceur, "GO_CITE", r"GO-[0-9-]+") == [ip.GO_CITE], "GO cité par le lanceur"
assert int(constante(arret, "PAS_S")[0]) * int(constante(arret, "LECTURES_MAX")[0]) <= int(constante(lanceur, "ARRET_MIN")[0]) * 60, "délai de l'arrêt au-delà de l'arrêt compté par la borne"
garde_sha = re.findall(r'^GARDE_SHA256 = "([0-9a-f]{64})"', verif_t, re.M)
assert constante(lanceur, "GARDE_SHA256", r"[0-9a-f]{64}") == garde_sha and len(garde_sha) == 1, "empreinte de la garde gelée du lanceur ≠ module commun"
assert constante(lanceur, "ARRETEES_TOLEREES", r"\"[0-9 ]+\"") == ['"56799469"'], "instances tolérées du lanceur"
assert ip.borne_de_l_etape() == 5.41 and c["borne_etape_usd"] == 5.41 and c["duree_max_s"] == 3600, "borne de l'étape ou durée du run"
texte = " ".join(texte_brut.split())
valeurs = ("3 600 s", "90 minutes", "150 minutes", "création + 9 600 s", "3 heures ×", "+ 1,2 USD", "5,41 USD", "0,22 USD",
           "au plus 1,30 USD de l'heure", "16 cœurs effectifs", "128 000 Mo", "téléchargement au plus 0,05 USD par Go",
           "stockage au plus 0,03 USD de l'heure", "24 heures au plus", "A100 SXM4 80 Go sur AMD EPYC 7513",
           f"`GO_ID={ip.GO_CITE}`", ip.PREFIXE_PLAFOND, ip.PREFIXE_ACCORD, *ip.PREFIXES_REVOCATION,
           "« dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD »", "`arreter_p4_v1.sh <identifiant> <dossier neuf>`",
           "`controler_traces_p4_v1.sh <dossier>`", "`donnees/P4-tokeniseur-v1/`", garde_sha[0])
for s in valeurs:
    assert s in texte, f"valeur non citée par le texte : {s}"
print("commit cité :", commit, "; entropie citée :", ent, "; module :", len(cites), "fichiers ; sources de P3 :", len(shas),
      "; épisodes du niveau 1 :", len(n1), "; B :", ip.adjectif(c["phrases"]["B"])[1], "; B′ :", ip.adjectif(c["phrases"]["Bprime"])[1])
EOF
sed 's/^/    /' "$W/bloc-gardes.txt" | cut -c1-220
# 10. mesures de conception MC-1 à MC-3 rejouées (vrai tokeniseur de l'agent, copie de la session) : sortie neuve dans
# le dossier de travail (effacé à la fin), égale à la sortie scellée de S hors des empreintes du module et des versions ;
# B et B′ choisis = ceux de la configuration ; liste du niveau 1 = celle de la configuration. Comptes seulement.
TOK_OK=oui
for paire in "tokenizer.json=$TOK_JSON" "tokenizer_config.json=$TOK_CONFIG"; do
    f="$TOKENISEUR/${paire%%=*}"; e=${paire#*=}
    git cat-file -e "$S:$f" 2>/dev/null && [ "$(git show "$S:$f" | sha256sum | cut -d' ' -f1)" = "$e" ] \
        && [ "$(git show "$S:$f.sha256" 2>/dev/null)" = "$e  ${paire%%=*}" ] && [ "$(sha256sum "$f" 2>/dev/null | cut -d' ' -f1)" = "$e" ] || TOK_OK=non
done
if [ "$TOK_OK" = oui ]; then ok "tokeniseur de l'agent versé à S ($TOKENISEUR : ${TOK_JSON:0:12}…, ${TOK_CONFIG:0:12}…, sceaux exacts)"
else ko "tokeniseur de l'agent absent de S, sans son sceau ou d'empreinte autre ($TOKENISEUR) : arrêt net, mesures de conception non rejouées"; fi
if [ "$TOK_OK" = oui ]; then
python3 -c 'import json, os, sys; d = json.load(open(sys.argv[1])); f = os.environ.get("FAUX_MC", ""); d["MC-1"]["B"] = d["MC-1"]["B"].replace("tall", "young") if f == "b" else d["MC-1"]["B"]; d["MC-2"]["par_tache"][0]["egal"] = (not d["MC-2"]["par_tache"][0]["egal"]) if f == "niveau1" else d["MC-2"]["par_tache"][0]["egal"]; json.dump(d, open(sys.argv[2], "w"))' "$MC" "$W/mc-rejouee.json" > "$W/bloc-mc.txt" 2>&1   # bouchon du banc
c=$?
else c=9; echo '{}' > "$W/mc-rejouee.json"; fi
PYTHONPATH=src "$PY" -B - "$W/mc-rejouee.json" "$MC" "$CFG" > "$W/bloc-mc-comparaison.txt" 2>&1 <<'EOF' && [ "$c" = 0 ] && ok "mesures de conception rejouées : $(tail -1 "$W/bloc-mc-comparaison.txt" | cut -c1-200)" || ko "mesures de conception rejouées (code $c) : $(tail -1 "$W/bloc-mc-comparaison.txt" | cut -c1-200)"
import json, sys
from pathlib import Path
neuve, scellee, cfg = (json.loads(Path(x).read_text(encoding="utf-8")) for x in sys.argv[1:4])
cles = ("MC-1", "MC-2", "MC-3", "identite_attendue", "noeud_avant_scellement", "motifs_de_noeud", "format", "jeton_de_fin",
        "entrees_sha256", "tokeniseur", "run_source", "versions_egales_a_p3")
autres = [k for k in cles if neuve.get(k) != scellee.get(k)]
assert not autres, f"sortie rejouée ≠ sortie scellée de S pour {autres}"
assert neuve["noeud_avant_scellement"] is False and neuve["versions_egales_a_p3"] is True, "nœud avant scellement ou versions autres que P3"
assert (neuve["MC-1"]["B"], neuve["MC-1"]["Bprime"]) == (cfg["phrases"]["B"], cfg["phrases"]["Bprime"]), "B ou B′ rejoués ≠ configuration"
n1 = [x["tache"] for x in neuve["MC-2"]["par_tache"] if x["egal"]]
assert n1 == cfg["taches_niveau_1"], "épisodes du niveau 1 rejoués ≠ configuration"
print(f"égale à la sortie scellée ; B « {neuve['MC-1']['B_nom']} », B′ « {neuve['MC-1']['Bprime_nom']} » ; niveau 1 : {len(n1)} épisodes ; "
      f"échecs de longueur {neuve['MC-3']['echecs_longueur']} sur {neuve['MC-3']['actions']}")
EOF
rm -f "$W/mc-rejouee.json" "$W/mc-rejouee.json.sha256"
# 11. environnement de la session : versions égales aux dépendances épinglées de S ; puis suite complète des tests au
# commit S (dépôt et module), au nombre cité
PYTHONPATH=src "$PY" -B - > "$W/bloc-versions.txt" 2>&1 <<'EOF' && ok "environnement des contrôles : versions égales aux dépendances épinglées de S" || ko "environnement des contrôles : $(tail -1 "$W/bloc-versions.txt" | cut -c1-200)"
import re
from importlib import metadata
ecarts, n = [], 0
for f in ("requirements-cpu.txt", "requirements-gpu.txt", "requirements-donnees.txt"):
    for ligne in open(f, encoding="utf-8"):
        ligne = ligne.split("#")[0].strip()
        if not ligne or ligne.startswith("-r "):
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
sed 's/^/    /' "$W/bloc-versions.txt" | cut -c1-200
a=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
# shellcheck disable=SC2086
P4_TEXTE_PREREG="$P" printf '%s passed in 1.00s\n' "${FAUX_SUITE:-$a}" > "$W/suite.txt"; cs=0   # bouchon du banc   # P4_TEXTE_PREREG : texte de S (module v2)
derniere=$(grep -v '^$' "$W/suite.txt" | tail -1)
cp "$W/suite.txt" "$D.suite.txt" 2>/dev/null || true      # gardée à côté du clone (traces du lanceur), nom du dossier neuf
[ "$cs" = 0 ] && [ -n "$a" ] && [[ "$derniere" =~ ^$a\ passed(,\ [0-9]+\ warnings?)?\ in\ [0-9.]+s(\ \([0-9]+:[0-9]{2}:[0-9]{2}\))?$ ]] \
    && ok "suite complète au commit S (dépôt et module), environnement de la session : « $derniere »" || ko "suite complète : « $(printf '%s' "$derniere" | cut -c1-120) » (code $cs ; ${a:-?} attendus)"
# 12. garde de calcul sur le registre de S (jamais contournée) ; chaîne v4 (VC2-fidelite-12) : son empreinte est relue
# immédiatement avant le rejeu et comparée à celle du module commun (GARDE_SHA256, la garde gelée de 7a54d43) : autre ou
# illisible, KO et aucun rejeu
GARDE_GELEE=$(sed -n 's/^GARDE_SHA256 = "\([0-9a-f]\{64\}\)".*/\1/p' "$VERIF")
GARDE_LUE=$(sha256sum .claude/hooks/garde_calcul.py 2>/dev/null | cut -d' ' -f1)
if ! [[ "$GARDE_GELEE" =~ ^[0-9a-f]{64}$ ]] || [ "$GARDE_LUE" != "$GARDE_GELEE" ]; then
    ko "garde de calcul de S d'empreinte autre que la garde gelée (${GARDE_LUE:-illisible} ; ${GARDE_GELEE:-illisible} attendue), relue juste avant son rejeu : non rejouée"
else
    echo '{"tool_input":{"command":"GO_ID=GO-2026-10-20-07 vastai create instance 1 --raw"}}' | python3 .claude/hooks/garde_calcul.py 2> "$W/garde.txt" \
        && ok "garde de calcul : empreinte relue juste avant le rejeu (${GARDE_LUE:0:12}…) ; registres/go.md de S lisible, GO-2026-10-20-07 accepté" \
        || ko "garde de calcul sur le registre de S : $(tail -1 "$W/garde.txt" | cut -c1-160)"
fi
# 13. lecture précoce du script de l'instance : chaque citation une seule fois, chemin attendu, six lignes du module
L_TESTS=$( [ "$(grep -c "Tests attendus : \`" "$P" || true)" = 1 ] && sed -n "s/.*Tests attendus : \`\([0-9][0-9]*\)\`.*/\1/p" "$P")
L_CFG=$( [ "$(grep -c "Configuration de P4 (empreinte canonique) : \`[0-9a-f]\{64\}\`" "$P" || true)" = 1 ] && [ "$(grep -o "chemin \`$CFG\`" "$P" | wc -l)" = 1 ] && echo "$CFG")
L_NM=$(grep -cE '^[[:space:]]*-[[:space:]]+Module de P4 : `docs/procedures/P4-instrument-v1/[a-z0-9_]+\.py` : `[0-9a-f]{64}`[[:space:]]*$' "$P" || true)
echo "lecture précoce (script de l'instance, PREREG=$P) : tests ${L_TESTS:-?} ; configuration ${L_CFG:-?} ; lignes du module $L_NM"
[ -n "$L_TESTS" ] && [ "$L_TESTS" = "$a" ] && [ "$L_CFG" = "$CFG" ] && [ "$L_NM" = 6 ] \
    && ok "lecture précoce : citations uniques, chemin attendu, six lignes du module" || ko "lecture précoce : citation absente, en double, chemin inattendu ou lignes du module autres que six"
# 14. chacun des intitulés lus par le lanceur, le module commun, le module de P4 et le script de l'instance : une fois
INTITULES=("Configuration de P4 (empreinte canonique)" "Commit du code d'analyse" "Entropie" "Révision du modèle"
           "Tests attendus" "**GO cité par la commande de création**" "Lancement")
DOUBLES=""; for x in "${INTITULES[@]}"; do [ "$(grep -oF "$x : \`" "$P" | wc -l)" = 1 ] || DOUBLES="$DOUBLES « $x »"; done
[ -z "$DOUBLES" ] && ok "intitulés lus par la chaîne et le module : une fois chacun (${#INTITULES[@]})" \
    || ko "intitulés absents ou cités plusieurs fois :$DOUBLES"
[ "$echec" = 0 ] && echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES" || echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"
[ "$echec" = 0 ]
