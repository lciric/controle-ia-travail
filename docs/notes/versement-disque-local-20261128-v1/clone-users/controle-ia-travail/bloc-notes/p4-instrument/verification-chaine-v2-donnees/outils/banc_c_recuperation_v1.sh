#!/usr/bin/env bash
# Banc C de la vérification « données et fuites » de la chaîne v2 de P4 (vérificateur neuf), v1 : récupération v2
# (recuperation_p4_v1.sh de la chaîne v2) jouée sur le monde jouet de la relecture « données » (S jouet c419dbd7, branches
# a : run complet, b : traces seules), recopié en miroir dans le dossier du vérificateur (rien n'est écrit chez la
# relecture). Copie de la récupération : les neuf lignes de la forme « ordinaire » de la répétition (dépôt distant local,
# branche, motif du run, mode, ligne « disponible », fichier des textes des fenêtres, carte, versions et copie non
# exigées) ; module commun : celui de la chaîne v2 (le S jouet porte la v1). Faux outil de location (destruction
# journalisée, jamais appelée réellement) ; jetons factices ; aucun texte de P3 (textes synthétiques du monde jouet).
# Chaque cas : code attendu et préfixe de KO attendu écrits avant le jeu ; sortie cherchée pour les jetons, les mots
# distinctifs des textes synthétiques et les fenêtres (module commun). « limite » : résultat documenté, sans verdict.
# Usage : banc_c_recuperation_v1.sh RACINE_NEUVE
set -uo pipefail
E=$(realpath -m "${1:?racine neuve}")
VV=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/verification-chaine-v2-donnees
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2
J=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees/jouet-b
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
REC=$H/recuperation_p4_v1.sh
ART=$VV/outils/artefacts_verif_c_v1.py
export PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
[ -e "$E" ] && { echo "$E existe déjà (R12)"; exit 2; }
mkdir -p "$E" || exit 2
for s in recuperation_p4_v1.sh verifications_p4_v1.py; do echo "script éprouvé : $s $(sha256sum "$H/$s" | cut -d' ' -f1)"; done
echo "banc : $(basename "$0") $(sha256sum "$(realpath "$0")" | cut -d' ' -f1) ; artefacts : $(basename "$ART") $(sha256sum "$ART" | cut -d' ' -f1)"
S=$(cat "$J/S.txt"); ID=99999999
git clone -q --no-local --mirror "$J/distant.git" "$E/distant.git" || exit 2
echo "monde jouet : miroir de $J/distant.git ; S jouet $S"
TX=donnees/synth/textes-fenetres-p3.jsonl
git -C "$E/distant.git" show "$S:$TX" > "$E/textes-fenetres.jsonl" || exit 2
JH=factice-hf-verifc-0001; JG=factice-gh-verifc-0001
copie() {   # $1 lettre de la branche, $2 sortie
    sed -e "s|^DISTANT=.*|DISTANT=$E/distant.git|" -e "s|^BRANCHE=calcul/p4-reel-v1\$|BRANCHE=calcul/p4-jouet-$1-v1|" -e "s|-p4-reel\\\$'\$|-p4-jouet\$'|" \
        -e 's|^MODE_ATTENDU=reel$|MODE_ATTENDU=jouet|' -e 's|"disponible True"|"disponible False"|' -e "s|^TEXTES_P3=[^ ]* |TEXTES_P3=$TX |" \
        -e 's|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|' -e 's|^VERSIONS_EXIGEES=oui|VERSIONS_EXIGEES=non|' -e 's|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|' \
        -e "s|^git show \"\$S:\$VERSEES/verifications_p4_v1.py\" > \"\$VERIF_S\".*|cp $H/verifications_p4_v1.py \"\$VERIF_S\"|" \
        "$REC" > "$2"
    local n; n=$(diff "$REC" "$2" | grep -c '^>')
    [ "$n" = 10 ] || { echo "copie $2 : $n lignes changées (10 attendues : 9 de la forme ordinaire et le module commun)"; exit 2; }
}
branche() {   # $1 lettre neuve, $2 cas, $3 branche de base
    git clone -q "$E/distant.git" "$E/clone-$1" && git -C "$E/clone-$1" checkout -q -b "$1" "origin/calcul/p4-jouet-$3-v1" || return 2
    (cd "$E/clone-$1" && env JETON_FUITE="$JH" "$PY" -I -B "$ART" "$2") || { echo "    artefact $2 : préparation impossible"; return 2; }
    git -C "$E/clone-$1" add -A && git -C "$E/clone-$1" add -f donnees 2>/dev/null
    git -C "$E/clone-$1" -c user.name="instance de calcul (P4)" -c user.email=instance@invalid -c commit.gpgsign=false \
        commit -qm "vérification : artefact $2" && git -C "$E/clone-$1" push -q origin "$1:refs/heads/calcul/p4-jouet-$1-v1" || return 2
    rm -rf "$E/clone-$1"
}
NC=0
jouer() {   # $1 lettre, $2 nom, $3 genre, $4 code attendu, $5 préfixe de KO attendu (ou « - »)
    local x=$1 n=$2 g=$3 a=$4 k=$5 c v aff
    copie "$x" "$E/recuperation-$x.sh"
    mkdir -p "$E/lancement-$x" "$E/vastai-$x"
    printf 'commit %s\ncreation %s\nsuccès : True ; identifiant %s ; message : essai\n' "$S" "$(date -u +%s)" "$ID" > "$E/lancement-$x/lancement.txt"
    env -i PATH="$VV/bin-vastai:/usr/bin:/bin" HOME="$E" LANG=C.UTF-8 TMPDIR="$E" HF_TOKEN=$JH CONTROLE_IA_GITHUB_TOKEN=$JG \
        GH_TOKEN=$JG VAST_API_KEY=factice-vast-verifc-0001 FAUX_VASTAI_ETAT="$E/vastai-$x" PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0 \
        bash "$E/recuperation-$x.sh" "$S" "$ID" "$E/lancement-$x" "$E/depot-$x" > "$E/sortie-$x.txt" 2>&1; c=$?
    rm -rf "$E/depot-$x" "$E/depot-$x.travail"
    # affichage : jetons, mots distinctifs des textes synthétiques, fenêtres (module commun)
    aff=""
    grep -qF -e "$JH" -e "$JG" "$E/sortie-$x.txt" && aff="$aff jeton"
    grep -qiE 'zanzibar|quokka|marmoset|axolotl|pangolin' "$E/sortie-$x.txt" && aff="$aff mot-distinctif"
    "$PY" -B "$H/verifications_p4_v1.py" fenetres "$E/textes-fenetres.jsonl" "$E/sortie-$x.txt" > /dev/null 2>&1 || aff="$aff fenêtre"
    local detruite=non; [ -s "$E/vastai-$x/journal" ] && detruite=oui
    if [ "$g" = limite ]; then
        v="limite documentée : code $c ; destruction demandée : $detruite ; affiché :${aff:- rien}"
    else
        v=CONFORME
        [ "$c" = "$a" ] || v="ÉCART (code $c, attendu $a)"
        if [ "$k" != - ]; then grep -qE "^KO  $k " "$E/sortie-$x.txt" || v="ÉCART (KO $k absent)"; fi
        [ -z "$aff" ] || v="ÉCART (affiché :$aff)"
        [ "$v" = CONFORME ] || NC=$((NC + 1))
    fi
    echo "$n [$g] (branche $x) : code $c ; $v"
    grep -E '^(KO|--)' "$E/sortie-$x.txt" | grep -v '^--  3f\|^--  6b' | cut -c1-200 | sed 's/^/    /'
    tail -1 "$E/sortie-$x.txt" | cut -c1-200 | sed 's/^/    | /'
}
# cas sains (validation du banc)
jouer a C00-sain-run-complet sain 0 -
jouer b C01-sain-traces-seules sain 4 -
# garde : affichage filtré (masquer, chercher, puis tronquer), schéma fermé, fenêtres dans les tableaux
branche ca motif_uxxxx_au_dela_de_400 a && jouer ca C10-motif-echappe-au-dela-de-400-caracteres garde 1 4f
branche cb jeton_au_bord_puis_texte b && jouer cb C11-traces-seules-jeton-au-bord-puis-texte garde 1 4f
branche cc validation_cle_en_plus a && jouer cc C12-validation-avec-une-cle-de-plus garde 1 4d
branche cd par_jeton_scores_2d a && jouer cd C13-scores-par-jeton-en-deux-dimensions garde 1 4d
branche ce validation_noms_permutes a && jouer ce C14-validation-noms-des-sondes-permutes garde 1 4d
branche cf fragment_80_dans_groupe a && jouer cf C15-fragment-de-80-dans-une-chaine-de-la-validation garde 1 4f
# repli de l'affichage : textes retirés de la branche (filtre de S impossible) ; la décision dit « jamais » de motif brut
branche cg repli_de_l_affichage a && jouer cg C16-repli-de-l-affichage-motif-qui-recopie-un-texte garde 1 4f
# limites documentées
branche ch fragment_62_dans_groupe a && jouer ch C20-fragment-de-62-dans-une-chaine-de-la-validation limite - -
branche ci historique_seul a && jouer ci C21-texte-dans-l-historique-seulement limite - -
git -C "$E/distant.git" log --format=%H "$S..calcul/p4-jouet-ci-v1" | while read -r h; do git -C "$E/distant.git" show "$h" -- traces; done \
    > "$E/historique-ci.diff"
git -C "$E/distant.git" diff "$S" calcul/p4-jouet-ci-v1 > "$E/final-ci.diff"
"$PY" -B "$H/verifications_p4_v1.py" fenetres "$E/textes-fenetres.jsonl" "$E/final-ci.diff" > "$E/final-ci.txt" 2>&1
echo "    C21 : différentiel final S..tête : $(tail -1 "$E/final-ci.txt" | cut -c1-80)"
if "$PY" -B "$H/verifications_p4_v1.py" fenetres "$E/textes-fenetres.jsonl" "$E/historique-ci.diff" > "$E/historique-ci.txt" 2>&1; then
    echo "    C21 : aucune fenêtre dans l'historique de la branche (inattendu)"
else echo "    C21 : $(tail -1 "$E/historique-ci.txt" | cut -c1-120) dans l'historique de la branche (commits S..tête), arbre final sans fenêtre"; fi
P_CACHE=$(find "$H" "$E" -name __pycache__ -not -path '*/.git/*' 2>/dev/null | head -3)
[ -z "$P_CACHE" ] && echo "aucun __pycache__ écrit : CONFORME" || { echo "__pycache__ écrit : $P_CACHE : ÉCART"; NC=$((NC + 1)); }
rm -rf "$E/distant.git"
echo "FIN DU BANC C ; écarts sur les cas garde ou sain : $NC"
[ "$NC" = 0 ] || exit 1
