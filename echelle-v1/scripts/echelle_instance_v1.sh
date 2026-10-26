#!/usr/bin/env bash
# Comparaison d'échelle 8B contre 70B (conscience d'évaluation, fuite du format) sur l'instance de calcul, sous le GO
# cité au lancement. Écrit par la lignée « session-depot » le 26 octobre 2026, décliné de `hm1_instance_v3.sh`
# (outils/test-hm1-v1) sous un nom nouveau (R12) ; lancé par `amorce_echelle_v1.sh`, au commit COMMIT.
# Deux mesures sur les 4 096 stimuli figés (`echelle-v1/stimuli/echelle-v1.json`), même script, mêmes stimuli :
#   petit : meta-llama/Llama-3.1-8B-Instruct, révision 0e9e39f2… ; poussé dès la fin (premier commit de BRANCHE) ;
#   grand : meta-llama/Llama-3.1-70B-Instruct, révision 1605565b… ; poussé ensuite (second commit).
# Aucune lecture des résultats sur l'instance (formes, nombres finis et empreintes seulement). Sorties poussées sur la
# branche neuve BRANCHE (R12). Variables : COMMIT, BRANCHE, TRAVAIL ; HF_TOKEN. Codes : 0 les deux poussés ; 1 arrêt.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${BRANCHE:?BRANCHE absent}" "${TRAVAIL:?TRAVAIL absent}"
RACINE=$(cd "$(dirname "$0")/../.." && pwd)
cd "$RACINE" || exit 1
mkdir -p "$TRAVAIL"
journal() { echo "ECHELLE $(date -u +%FT%TZ) : $*" | tee -a "$TRAVAIL/journal.txt"; }
PETIT=meta-llama/Llama-3.1-8B-Instruct
REV_PETIT=0e9e39f249a16976918f6564b8830bc894c89659
GRAND=meta-llama/Llama-3.1-70B-Instruct
REV_GRAND=1605565b47bb9346c5515c34102e054115b4f98b
D=echelle-v1
STIM=$D/stimuli/echelle-v1.json
E_STIM=bb285e11a63351047be7d7fb7e1827748884e107ccdbbcb4e6e9e3b322783b5b
SORTIE=$D/resultats-echelle-v1
POUSSE=0

pousser() {
    mkdir -p "$SORTIE/journaux"
    for f in journal.txt pip-freeze.txt nvidia-smi.txt telechargement-petit.txt telechargement-grand.txt \
             mesure-petit.txt mesure-grand.txt; do
        [ -f "$TRAVAIL/$f" ] && cp "$TRAVAIL/$f" "$SORTIE/journaux/"
    done
    (cd "$SORTIE" && find . -type f ! -name 'EMPREINTES-echelle-v1.txt' -printf '%P\n' | LC_ALL=C sort \
        | xargs -d '\n' sha256sum > EMPREINTES-echelle-v1.txt)
    if [ "$POUSSE" = 0 ]; then
        git checkout -q -b "$BRANCHE" || { journal "branche $BRANCHE : création impossible"; return 1; }
    fi
    git add -f "$SORTIE" || return 1
    git -c user.name="instance de calcul (comparaison d'échelle v1)" -c user.email="instance-calcul@invalid" \
        commit -q -m "$1 (${GO_ID:-GO cité au lancement}, commit de lancement $COMMIT)" || { journal "commit impossible"; return 1; }
    for essai in 1 2 3 4 5; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then
            POUSSE=1; journal "poussé : $BRANCHE $(git rev-parse HEAD)"; return 0
        fi
        sleep $((2 ** essai))
    done
    journal "poussée impossible : $(tail -1 "$TRAVAIL/poussee.err")"; return 1
}

cle_dans_sorties() {
    # une clé trouvée dans les sorties : rien n'est poussé (liste d'arrêt)
    local k
    for k in "${HF_TOKEN:-}" "${GH_TOKEN:-}"; do
        [ -n "$k" ] && [ ${#k} -gt 6 ] && grep -rqF -- "$k" "$SORTIE" "$TRAVAIL"/*.txt 2>/dev/null && return 0
    done
    return 1
}

[ "$(git rev-parse HEAD)" = "$COMMIT" ] || { journal "HEAD $(git rev-parse HEAD) ≠ COMMIT $COMMIT : arrêt"; exit 1; }
if git ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1; then
    journal "la branche $BRANCHE existe déjà sur le dépôt (R12) : arrêt avant tout calcul"; exit 1
fi
[ -e "$SORTIE" ] && { journal "$SORTIE existe déjà dans le clone (R12) : arrêt"; exit 1; }
[ "$(sha256sum "$STIM" | cut -d' ' -f1)" = "$E_STIM" ] || { journal "stimuli : empreinte ≠ $E_STIM : arrêt"; exit 1; }
for s in mesurer_echelle_v1.py requirements-echelle-v1.txt; do
    (cd $D/scripts && sha256sum -c --quiet "$s.sha256") || { journal "$s ≠ son compagnon d'empreinte : arrêt"; exit 1; }
done
journal "commit $COMMIT ; stimuli $E_STIM"

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    journal "installation des versions épinglées"
    python3.11 -m venv "$TRAVAIL/venv" || { journal "venv impossible"; exit 1; }
    # shellcheck disable=SC1091
    . "$TRAVAIL/venv/bin/activate"
    if ! pip install -q -r $D/scripts/requirements-echelle-v1.txt > "$TRAVAIL/pip.txt" 2>&1; then
        journal "installation impossible : $(tail -2 "$TRAVAIL/pip.txt" | tr '\n' ' ')"; exit 1
    fi
fi
python -m pip freeze --all > "$TRAVAIL/pip-freeze.txt" 2>/dev/null || journal "pip freeze impossible (descriptif)"
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv > "$TRAVAIL/nvidia-smi.txt" 2>&1 || journal "nvidia-smi absent (descriptif)"

mesurer() {  # $1 nom (petit|grand), $2 modèle du Hub, $3 révision
    local nom=$1 modele=$2 rev=$3 mod
    if [ -n "${MODELE_LOCAL:-}" ]; then
        mod=(--modele "$MODELE_LOCAL" --processeur-permis --type-nombre float32)
        journal "$nom : répétition locale, non décisive : modèle minuscule $MODELE_LOCAL"
    else
        if ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
            journal "carte indisponible pour torch : arrêt"; return 1
        fi
        : "${HF_TOKEN:?HF_TOKEN absent}"
        journal "$nom : téléchargement de $modele à la révision $rev"
        if ! python -I -B -c '
import sys
from huggingface_hub import snapshot_download
print(snapshot_download(sys.argv[1], revision=sys.argv[2], allow_patterns=["*.json", "model-*.safetensors"]))' \
                "$modele" "$rev" > "$TRAVAIL/telechargement-$nom.txt" 2>&1; then
            journal "$nom : téléchargement impossible : $(tail -2 "$TRAVAIL/telechargement-$nom.txt" | tr '\n' ' ')"; return 1
        fi
        mod=(--modele "$modele" --revision "$rev")
    fi
    journal "$nom : mesure (passe avant, dernier jeton, quatre profondeurs)"
    if ! python -I -B $D/scripts/mesurer_echelle_v1.py --stimuli "$STIM" --sortie "$SORTIE/$nom" "${mod[@]}" \
            > "$TRAVAIL/mesure-$nom.txt" 2>&1; then
        journal "$nom : mesure en échec : $(grep -v '^\[transformers\]' "$TRAVAIL/mesure-$nom.txt" | tail -2 | tr '\n' ' ')"
        rm -rf "${SORTIE:?}/$nom"; return 1
    fi
    if cle_dans_sorties; then
        journal "$nom : une clé figure dans les sorties : rien n'est poussé (liste d'arrêt)"; rm -rf "${SORTIE:?}"; exit 1
    fi
    return 0
}

if mesurer petit "$PETIT" "$REV_PETIT"; then
    pousser "Comparaison d'échelle : mesure du petit modèle" || exit 1
else
    pousser "Comparaison d'échelle : arrêt sur le petit modèle"; exit 1
fi
if [ -z "${MODELE_LOCAL:-}" ]; then
    rm -rf "${HF_HOME:-$HOME/.cache/huggingface}/hub/models--meta-llama--Llama-3.1-8B-Instruct"  # place pour le grand
fi
if mesurer grand "$GRAND" "$REV_GRAND"; then
    pousser "Comparaison d'échelle : mesure du grand modèle" || exit 1
else
    pousser "Comparaison d'échelle : petit modèle fait, grand en échec"; exit 1
fi
journal "fini"
exit 0
