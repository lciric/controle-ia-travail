#!/usr/bin/env bash
# Test H-M1 (gabarit contre style, signal de conscience d'évaluation) sur l'instance de calcul, sous GO-2026-10-25-03
# (R-447 et suivantes). Écrit par la lignée « session-depot » le 25 octobre 2026, décliné de `traits_etape1_instance_v1.sh`
# (R12) ; lancé par `amorce_hm1_v1.sh` dans le clone du dépôt de travail, au commit COMMIT.
# Deux mesures sur les 192 stimuli figés (`stimuli-hm1/`), même modèle, même révision que l'étape 1 :
#   traits-stimuli : `extraire_activations_v2.py`, couche 16, dernier jeton (sonde, mesure secondaire) ;
#   verbalisation  : `mesurer_verbalisation_hm1_v1.py`, V = logit(Yes) − logit(No) (mesure principale).
# Aucune lecture des résultats sur l'instance (formes, nombres finis et empreintes seulement). Sorties poussées sur la
# branche neuve BRANCHE (R12). Variables : COMMIT, BRANCHE, TRAVAIL ; HF_TOKEN. Codes : 0 poussé ; 1 arrêt.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${BRANCHE:?BRANCHE absent}" "${TRAVAIL:?TRAVAIL absent}"
RACINE=$(cd "$(dirname "$0")/../.." && pwd)
cd "$RACINE" || exit 1
mkdir -p "$TRAVAIL"
journal() { echo "HM1 $(date -u +%FT%TZ) : $*" | tee -a "$TRAVAIL/journal.txt"; }
MODELE=meta-llama/Llama-3.1-8B-Instruct
REVISION=0e9e39f249a16976918f6564b8830bc894c89659
D=essaim-m3-refonte-v1
STIM=$D/stimuli-hm1/stimuli-hm1-v1.json
BANQUE_STIM=$D/stimuli-hm1/banque-stimuli-hm1-v1.json
E_STIM=d25768a965571f8f98c360df909e356865d02f54feaa83b3da35a31e9374b1ee
E_BANQUE_STIM=da5e801d4f9de59bacc09633397e1224e26838dc0a12d08c35bd767718130bcb
SORTIE=$D/resultats-hm1-v1

pousser() {
    mkdir -p "$SORTIE/journaux"
    for f in journal.txt pip-freeze.txt nvidia-smi.txt telechargement.txt extraction.txt verbalisation.txt; do
        [ -f "$TRAVAIL/$f" ] && cp "$TRAVAIL/$f" "$SORTIE/journaux/"
    done
    (cd "$SORTIE" && find . -type f ! -name 'EMPREINTES-hm1-v1.txt' -printf '%P\n' | LC_ALL=C sort \
        | xargs -d '\n' sha256sum > EMPREINTES-hm1-v1.txt)
    git checkout -q -b "$BRANCHE" || { journal "branche $BRANCHE : création impossible"; return 1; }
    git add -f "$SORTIE" || return 1
    git -c user.name="instance de calcul (test H-M1)" -c user.email="instance-calcul@invalid" \
        commit -q -m "$1 (GO-2026-10-25-03, commit de lancement $COMMIT)" || { journal "commit impossible"; return 1; }
    for essai in 1 2 3 4 5; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then
            journal "poussé : $BRANCHE $(git rev-parse HEAD)"; return 0
        fi
        sleep $((2 ** essai))
    done
    journal "poussée impossible : $(tail -1 "$TRAVAIL/poussee.err")"; return 1
}

[ "$(git rev-parse HEAD)" = "$COMMIT" ] || { journal "HEAD $(git rev-parse HEAD) ≠ COMMIT $COMMIT : arrêt"; exit 1; }
if git ls-remote --exit-code --heads origin "$BRANCHE" >/dev/null 2>&1; then
    journal "la branche $BRANCHE existe déjà sur le dépôt (R12) : arrêt avant tout calcul"; exit 1
fi
[ -e "$SORTIE" ] && { journal "$SORTIE existe déjà dans le clone (R12) : arrêt"; exit 1; }
[ "$(sha256sum "$STIM" | cut -d' ' -f1)" = "$E_STIM" ] || { journal "stimuli : empreinte ≠ $E_STIM : arrêt"; exit 1; }
[ "$(sha256sum "$BANQUE_STIM" | cut -d' ' -f1)" = "$E_BANQUE_STIM" ] || { journal "banque des stimuli : empreinte ≠ $E_BANQUE_STIM : arrêt"; exit 1; }
for s in extraire_activations_v2.py mesurer_verbalisation_hm1_v1.py; do
    (cd $D/scripts && sha256sum -c --quiet "$s.sha256") || { journal "$s ≠ son compagnon d'empreinte : arrêt"; exit 1; }
done
journal "commit $COMMIT ; stimuli $E_STIM"

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    journal "installation des versions épinglées"
    python3.11 -m venv "$TRAVAIL/venv" || { journal "venv impossible"; pousser "Test H-M1 : arrêt à l'installation"; exit 1; }
    # shellcheck disable=SC1091
    . "$TRAVAIL/venv/bin/activate"
    if ! pip install -q -r $D/scripts/requirements-traits-v1.txt > "$TRAVAIL/pip.txt" 2>&1; then
        journal "installation impossible : $(tail -2 "$TRAVAIL/pip.txt" | tr '\n' ' ')"
        pousser "Test H-M1 : arrêt à l'installation"; exit 1
    fi
fi
python -m pip freeze --all > "$TRAVAIL/pip-freeze.txt" 2>/dev/null || journal "pip freeze impossible (descriptif)"
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv > "$TRAVAIL/nvidia-smi.txt" 2>&1 || journal "nvidia-smi absent (descriptif)"

if [ -n "${MODELE_LOCAL:-}" ]; then
    MOD=(--modele "$MODELE_LOCAL" --processeur-permis --type-nombre float32); COUCHE=1
    journal "répétition locale, non décisive : modèle minuscule $MODELE_LOCAL"
else
    if ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
        journal "carte indisponible pour torch : arrêt"; pousser "Test H-M1 : arrêt, carte indisponible"; exit 1
    fi
    : "${HF_TOKEN:?HF_TOKEN absent}"
    journal "téléchargement de $MODELE à la révision $REVISION"
    if ! python -I -B -c '
import sys
from huggingface_hub import snapshot_download
print(snapshot_download(sys.argv[1], revision=sys.argv[2], allow_patterns=["*.json", "model-*.safetensors"]))' \
            "$MODELE" "$REVISION" > "$TRAVAIL/telechargement.txt" 2>&1; then
        journal "téléchargement impossible : $(tail -2 "$TRAVAIL/telechargement.txt" | tr '\n' ' ')"
        pousser "Test H-M1 : arrêt au téléchargement"; exit 1
    fi
    MOD=(--modele "$MODELE" --revision "$REVISION"); COUCHE=16
fi

journal "sonde : traits des stimuli (couche $COUCHE, dernier jeton)"
if ! python -I -B $D/scripts/extraire_activations_v2.py --banque "$BANQUE_STIM" --sortie "$SORTIE/traits-stimuli" "${MOD[@]}" \
        --couches $COUCHE --agregations dernier --max-jetons 2048 > "$TRAVAIL/extraction.txt" 2>&1; then
    journal "extraction en échec : $(grep -v '^\[transformers\]' "$TRAVAIL/extraction.txt" | tail -2 | tr '\n' ' ')"
    rm -rf "$SORTIE/traits-stimuli"; pousser "Test H-M1 : extraction en échec"; exit 1
fi
journal "verbalisation : V = logit(Yes) − logit(No)"
if ! python -I -B $D/scripts/mesurer_verbalisation_hm1_v1.py --stimuli "$STIM" --sortie "$SORTIE/verbalisation" "${MOD[@]}" \
        > "$TRAVAIL/verbalisation.txt" 2>&1; then
    journal "verbalisation en échec : $(grep -v '^\[transformers\]' "$TRAVAIL/verbalisation.txt" | tail -2 | tr '\n' ' ')"
    rm -rf "$SORTIE/verbalisation"; pousser "Test H-M1 : verbalisation en échec"; exit 1
fi
pousser "Test H-M1 : traits des stimuli et verbalisation" || exit 1
journal "fini"
exit 0
