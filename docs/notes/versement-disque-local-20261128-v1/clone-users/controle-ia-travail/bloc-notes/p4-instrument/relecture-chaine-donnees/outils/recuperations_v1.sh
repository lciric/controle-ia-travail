#!/usr/bin/env bash
# Relecture « données et fuites », v1 : récupération de P4 (script relu, d3b65f5a…) jouée sur les branches jouet et sur
# des artefacts fabriqués par le relecteur. Copie de la récupération : neuf lignes changées, les mêmes que la forme
# « ordinaire » de la répétition jouet du rédacteur (dépôt distant local, branche, motif du run, mode, ligne
# « disponible », fichier des textes des fenêtres, carte, versions et copie non exigées). Faux outil de location ;
# jetons factices ; aucun réseau. Pour chaque cas : code, dernière ligne, lignes KO, destruction demandée, et deux
# relevés d'affichage : fenêtres synthétiques et jetons factices retrouvés dans la sortie de la récupération.
set -uo pipefail
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees
CH=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
J=$W/jouet-b
R=$W/recuperations
S=$(cat "$J/S.txt")
ID=99999999
JGH=factice-gh-relecture-0001; JHF=factice-hf-relecture-0001; JVA=factice-vast-relecture-0001
export PYTHONDONTWRITEBYTECODE=1 TMPDIR=$W/tmp GIT_CONFIG_NOSYSTEM=1
couper() { cut -c1-"$1" | iconv -f UTF-8 -t UTF-8 -c; return 0; }
[ -e "$R" ] && { echo "$R existe déjà (R12)"; exit 2; }
mkdir -p "$R"
REC=$CH/recuperation_p4_v1.sh
[ "$(sha256sum "$REC" | cut -d' ' -f1)" = d3b65f5ac00f2bb3bfd36a9c62405dcc614c526117cd985034aa86f04533b060 ] \
    || { echo "récupération relue : empreinte autre que d3b65f5a…"; exit 2; }
echo "récupération relue : $REC (d3b65f5a…) ; S jouet $S"
# fenêtres synthétiques (textes honnêtes du monde jouet), pour le relevé d'affichage
"$PY" -I -B -c 'import json, sys
for x in open(sys.argv[1], encoding="utf-8"):
    d = json.loads(x)
    t = d["texte"]
    if d["condition"] == "honnete" and len(t) >= 64 and len(set(t)) > 1:
        m = (len(t) - 48) // 2
        print(json.dumps(t[m:m + 48]))' "$J/source/donnees/synth/textes-fenetres-p3.jsonl" > "$R/fenetres-synthetiques.jsonl"
cat > "$R/copie.sed" <<'EOF'
s|^BRANCHE=calcul/p4-reel-v1$|BRANCHE=calcul/p4-jouet-@X@-v1|
s|-p4-reel\$'$|-p4-jouet$'|
s|^MODE_ATTENDU=reel$|MODE_ATTENDU=jouet|
s|"disponible True"|"disponible False"|
s|^TEXTES_P3=[^ ]* |TEXTES_P3=donnees/synth/textes-fenetres-p3.jsonl |
s|^CARTE_EXIGEE=oui|CARTE_EXIGEE=non|
s|^VERSIONS_EXIGEES=oui|VERSIONS_EXIGEES=non|
s|^COPIE_EXIGEE=oui|COPIE_EXIGEE=non|
EOF
copie() {   # $1 lettre de la branche
    sed -e "s|^DISTANT=https://github.com/lciric/controle-ia-travail.git\$|DISTANT=$J/distant.git|" -f "$R/copie.sed" "$REC" \
        | sed "s|@X@|$1|" > "$R/recuperation-$1.sh"
    echo "    copie de la récupération ($1) : $(diff "$REC" "$R/recuperation-$1.sh" | grep -c '^>') lignes changées"
}
branche() {   # $1 lettre, $2 cas, $3 branche de base (a ou b)
    git clone -q "$J/distant.git" "$R/clone-$1" && git -C "$R/clone-$1" checkout -q -b "$1" "origin/calcul/p4-jouet-$3-v1" || return 2
    (cd "$R/clone-$1" && "$PY" -I -B "$W/outils/artefacts_relecture_v1.py" "$2") || { echo "    artefact $2 : préparation impossible"; return 2; }
    git -C "$R/clone-$1" add -A && git -C "$R/clone-$1" add -f donnees 2>/dev/null
    git -C "$R/clone-$1" -c user.name="instance de calcul (P4)" -c user.email=instance@invalid -c commit.gpgsign=false \
        commit -qm "relecture : artefact $2" && git -C "$R/clone-$1" push -q origin "$1:refs/heads/calcul/p4-jouet-$1-v1" || return 2
    rm -rf "$R/clone-$1"
}
recuperer() {   # $1 lettre, $2 nom du cas, puis variables du faux outil
    local x=$1 n=$2 c; shift 2
    mkdir -p "$R/vastai-$x"
    env -i PATH="$W/outils/bin-vastai:/usr/bin:/bin" HOME="$W/maison" LANG=C.UTF-8 TMPDIR="$W/tmp" HF_TOKEN=$JHF \
        CONTROLE_IA_GITHUB_TOKEN=$JGH GH_TOKEN=$JGH VAST_API_KEY=$JVA FAUX_VASTAI_ETAT="$R/vastai-$x" PYTHONDONTWRITEBYTECODE=1 \
        GIT_CONFIG_NOSYSTEM=1 "$@" bash "$R/recuperation-$x.sh" "$S" "$ID" "$R/depot-$x" > "$R/recuperation-$x.txt" 2>&1; c=$?
    echo "récupération [$n] (branche $x) : code $c ; $(tail -1 "$R/recuperation-$x.txt" | couper 160)"
    grep -E '^(KO|--)|^    arrêt ' "$R/recuperation-$x.txt" | couper 230 | sed 's/^/    /'
    if [ -s "$R/vastai-$x/journal" ]; then echo "    DESTRUCTION demandée au faux outil : $(tr '\n' ' ' < "$R/vastai-$x/journal")"
    else echo "    aucune destruction demandée"; fi
    "$PY" -I -B -c 'import json, sys
sortie = open(sys.argv[1], encoding="utf-8", errors="replace").read()
f = [json.loads(l) for l in open(sys.argv[2], encoding="utf-8")]
n = sum(1 for w in f if w in sortie)
print(f"    affichage : {n} fenêtre(s) synthétique(s) dans la sortie de la récupération" + (" (texte affiché)" if n else ""))' \
        "$R/recuperation-$x.txt" "$R/fenetres-synthetiques.jsonl"
    if grep -qF -e "$JGH" -e "$JHF" -e "$JVA" "$R/recuperation-$x.txt"; then echo "    affichage : JETON FACTICE AFFICHÉ"
    else echo "    affichage : aucun jeton factice dans la sortie"; fi
    rm -rf "$R/depot-$x" "$R/depot-$x.travail"
}
cas() {   # $1 lettre, $2 cas (ou « - » pour la branche telle quelle), $3 branche de base, $4 nom
    if [ "$2" != - ]; then branche "$1" "$2" "$3" || { echo "branche $1 ($2) : impossible"; return; }; fi
    copie "$1"
    recuperer "$1" "$4"
}
echo "== cas sains (témoins) =="
cas a - a "sain, run complet"
cas b - b "sain, traces seules (arrêt avant le run)"
echo "== témoins des gardes (artefacts qui doivent arrêter) =="
cas c fenetre_brute_run_err a "fenêtre brute dans run.err"
cas d sceau_faux_validation a "sceau faux de validation-p4.npz"
cas e identite_absente a "fichier attendu absent : identite-p4.json"
cas f trace_alteree a "trace changée après son sceau"
cas g empreintes_absentes a "fichier attendu absent : empreintes.sha256 des traces"
cas h fenetre_dans_un_tableau a "fenêtre dans une chaîne d'un tableau"
cas i motif_avec_fenetre a "motif d'arrêt qui recopie un texte"
echo "== artefacts qui éprouvent les limites =="
cas j fenetre_echappee_run_err a "fenêtre échappée (saut de ligne) dans run.err"
cas k texte_partiel_run_err a "texte entier moins sa fenêtre du milieu, dans run.err"
cas l traces_seules_fenetre b "traces seules, texte recopié dans le journal"
cas m validation_activations a "validation à 4 096 colonnes (activations)"
cas n par_jeton_longueurs_doublees a "scores par jeton à longueurs doublées"
find "$W" -name __pycache__ -type d | head -3 | sed 's/^/__pycache__ écrit : /'
echo "FIN DES RÉCUPÉRATIONS"
