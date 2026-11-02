#!/usr/bin/env bash
# Essai local du script d'instance EXISTANT (inchangé) sur le texte du complément de validation, sans réseau ni carte :
# dépôt git local nu tenant lieu de dépôt distant, dont le commit porte l'arbre du commit lancé (hors dossiers lourds :
# docs/ sauf les invites et procédures que lit le code, registres/, livrables/, brouillons/, papiers/, traces/), plus le
# texte et la configuration du complément et des sceaux POSÉS DANS CE DÉPÔT JETABLE SEULEMENT (le texte n'est pas scellé
# dans le dépôt de travail). Usage :
#   essai_local_complement.sh preparer SOURCE BASE        (SOURCE : arbre de travail ; BASE : dossier neuf)
#   essai_local_complement.sh cas BASE NOM [VAR=valeur …] (lance l'amorce du commit avec l'environnement de l'instance,
#                                                          plus les variables données, qui remplacent ou s'ajoutent)
set -uo pipefail
PY=/home/user/controle-ia-travail/.venv/bin/python
TOK=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/c6/tok
TEXTE=prereg/R1-addendum-relance-v2-complement-validation-v1.md
CONF=prereg/R1-graine-config-complement-v2.json
case "$1" in
preparer)
    SRC="$2"; B="$3"
    [ ! -e "$B" ] || { echo "$B existe déjà (R12)"; exit 1; }
    mkdir -p "$B/prep"
    HAUTS=$(git -C "$SRC" ls-tree --name-only HEAD | grep -vxE 'docs|registres|livrables|brouillons|papiers|traces')
    git -C "$SRC" archive --format=tar HEAD -- $HAUTS docs/sources/invites-2606.07054-v1 docs/sources/invites-2606.08892-v1 \
        docs/procedures | tar -x -C "$B/prep"
    cp "$SRC/$TEXTE" "$SRC/$CONF" "$B/prep/prereg/"
    (cd "$B/prep" && PYTHONPATH=src "$PY" -B -m controle_ia.scellement sceller "$TEXTE" "$CONF" >/dev/null) || exit 1
    git -C "$B/prep" init -q -b prep/essai && git -C "$B/prep" config user.email essai@example.invalid \
        && git -C "$B/prep" config user.name "essai local" && git -C "$B/prep" add -A && git -C "$B/prep" add -f . \
        && git -C "$B/prep" commit -qm "essai local : arbre du commit lancé ($(git -C "$SRC" rev-parse HEAD)), texte et configuration du complément, sceaux de l'essai" \
        || exit 1
    git clone -q --bare "file://$B/prep" "$B/distant.git" || exit 1
    git -C "$B/distant.git" branch calcul/r1-resolution-graine-v1 prep/essai     # branche par défaut du script : déjà présente, comme sur le vrai dépôt
    echo "COMMIT=$(git -C "$B/distant.git" rev-parse prep/essai)"
    echo "SCEAUX_ESSAI texte=$(cut -c1-64 "$B/prep/$TEXTE.sha256") configuration=$(cut -c1-64 "$B/prep/$CONF.sha256")"
    rm -rf "$B/prep" ;;
cas)
    B="$2"; NOM="$3"; shift 3
    D="$B/$NOM"; [ ! -e "$D" ] || { echo "$D existe déjà (R12)"; exit 1; }
    mkdir -p "$D/racine"
    COMMIT=$(git -C "$B/distant.git" rev-parse prep/essai)
    git -C "$B/distant.git" show "$COMMIT:scripts/amorce_instance_r1_resolution_graine_v1.sh" > "$D/amorce.sh"
    env -i PATH="$(dirname "$PY"):/usr/local/bin:/usr/bin:/bin" HOME="$D/racine" COMMIT="$COMMIT" \
        DEPOT_URL="$B/distant.git" BRANCHE=calcul/r1-graine-complement-validation-v1 PREREG="$TEXTE" \
        TABLE_V3=prereg/R1-table-tokenisation-v3-rejeu-complement-v1.json PLAFOND_MIN=13055 GH_TOKEN=jeton-factice \
        RACINE_AMORCE="$D/racine" VENV_EXISTANT=/home/user/controle-ia-travail/.venv TOKENISEUR_LLAMA31="$TOK" \
        HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 "$@" bash "$D/amorce.sh" > "$D/amorce.txt" 2>&1
    code=$?
    echo "cas $NOM : code de l'amorce $code"
    exit $code ;;
*) echo "usage : preparer | cas"; exit 2 ;;
esac
