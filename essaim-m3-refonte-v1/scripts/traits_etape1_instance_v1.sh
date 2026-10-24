#!/usr/bin/env bash
# Extraction des traits de l'étape 1 (programme « gradient conçu par l'essaim ») sur l'instance de calcul, sous
# GO-2026-10-24-05 (R-355). Écrit par la lignée « session-depot » le 24 octobre 2026 ; lancé par
# `amorce_traits_etape1_v1.sh` dans le clone du dépôt de travail, au commit COMMIT.
# Deux extractions par `extraire_activations_v2.py`, même banque scellée, même modèle, mêmes couches et agrégations :
#   traits-2048  : paramètres du brouillon v1 du préenregistrement (≤ 2 048 jetons ; troncature par la fin, consignée) ;
#   traits-16384 : sans troncature (la plus longue tâche fait 12 407 jetons, mesuré avec le tokeniseur à la révision).
# Le préenregistrement scellé dira laquelle est servie ; aucune lecture des traits avant son scellement (R1), hors
# formes, nombres finis et empreintes.
# Sorties (traits, manifestes, journaux, empreintes) poussées sur la branche neuve BRANCHE (R12) ; journal sur la
# sortie standard (lu par `vastai logs`). Rien ne s'affiche des jetons.
# Variables : COMMIT, BRANCHE, TRAVAIL ; HF_TOKEN (modèle du Hub, lu par huggingface_hub). Répétition locale seulement :
# MODELE_LOCAL (dossier d'un modèle minuscule au vocabulaire de Llama-3.1), VENV_EXISTANT.
# Codes : 0 traits poussés ; 1 arrêt (journaux poussés quand c'est possible).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${BRANCHE:?BRANCHE absent}" "${TRAVAIL:?TRAVAIL absent}"
RACINE=$(cd "$(dirname "$0")/../.." && pwd)
cd "$RACINE" || exit 1
mkdir -p "$TRAVAIL"
journal() { echo "TRAITS $(date -u +%FT%TZ) : $*" | tee -a "$TRAVAIL/journal.txt"; }
MODELE=meta-llama/Llama-3.1-8B-Instruct
REVISION=0e9e39f249a16976918f6564b8830bc894c89659
BANQUE=essaim-m3-refonte-v1/banque/banque-confrontation-v1.json
EMPREINTE_BANQUE=f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc
SCRIPT=essaim-m3-refonte-v1/scripts/extraire_activations_v2.py
SORTIE=essaim-m3-refonte-v1/traits/etape1-v1
COUCHES="8 12 16 20 24"
LONGUEURS="2048 16384"

pousser() {  # $1 : message ; journaux toujours versés, traits seulement s'ils existent
    mkdir -p "$SORTIE/journaux"
    for f in journal.txt pip-freeze.txt nvidia-smi.txt telechargement.txt extraction-2048.txt extraction-16384.txt; do
        [ -f "$TRAVAIL/$f" ] && cp "$TRAVAIL/$f" "$SORTIE/journaux/"
    done
    (cd "$SORTIE" && find . -type f ! -name 'EMPREINTES-traits-etape1-v1.txt' -printf '%P\n' | LC_ALL=C sort \
        | xargs -d '\n' sha256sum > EMPREINTES-traits-etape1-v1.txt)
    git checkout -q -b "$BRANCHE" || { journal "branche $BRANCHE : création impossible"; return 1; }
    git add -f "$SORTIE" || return 1
    git -c user.name="instance de calcul (traits, étape 1)" -c user.email="instance-calcul@invalid" \
        commit -q -m "$1 (GO-2026-10-24-05, commit de lancement $COMMIT)" || { journal "commit impossible"; return 1; }
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
[ "$(sha256sum "$BANQUE" | cut -d' ' -f1)" = "$EMPREINTE_BANQUE" ] || { journal "banque : empreinte ≠ $EMPREINTE_BANQUE : arrêt"; exit 1; }
(cd "$(dirname "$SCRIPT")" && sha256sum -c --quiet extraire_activations_v2.py.sha256) \
    || { journal "script d'extraction ≠ son compagnon d'empreinte : arrêt"; exit 1; }
journal "commit $COMMIT ; banque $EMPREINTE_BANQUE ; script $(sha256sum "$SCRIPT" | cut -d' ' -f1)"

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    journal "installation des versions épinglées"
    python3.11 -m venv "$TRAVAIL/venv" || { journal "venv impossible"; pousser "Traits de l'étape 1 : arrêt à l'installation"; exit 1; }
    # shellcheck disable=SC1091
    . "$TRAVAIL/venv/bin/activate"
    if ! pip install -q -r essaim-m3-refonte-v1/scripts/requirements-traits-v1.txt > "$TRAVAIL/pip.txt" 2>&1; then
        journal "installation impossible : $(tail -2 "$TRAVAIL/pip.txt" | tr '\n' ' ')"
        pousser "Traits de l'étape 1 : arrêt à l'installation"; exit 1
    fi
fi
python -m pip freeze --all > "$TRAVAIL/pip-freeze.txt" 2>/dev/null || journal "pip freeze impossible (descriptif)"
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv > "$TRAVAIL/nvidia-smi.txt" 2>&1 || journal "nvidia-smi absent (descriptif)"
journal "$(python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'carte', torch.cuda.is_available())")"

if [ -n "${MODELE_LOCAL:-}" ]; then
    MOD=(--modele "$MODELE_LOCAL" --processeur-permis --type-nombre float32)
    COUCHES="1 2 4"
    journal "répétition locale, non décisive : modèle minuscule $MODELE_LOCAL, couches $COUCHES"
else
    if ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
        journal "carte indisponible pour torch (pilote trop ancien ?) : arrêt"; pousser "Traits de l'étape 1 : arrêt, carte indisponible"; exit 1
    fi
    : "${HF_TOKEN:?HF_TOKEN absent}"
    journal "téléchargement de $MODELE à la révision $REVISION"
    if ! python -I -B -c '
import sys
from huggingface_hub import snapshot_download
print(snapshot_download(sys.argv[1], revision=sys.argv[2], allow_patterns=["*.json", "model-*.safetensors"]))' \
            "$MODELE" "$REVISION" > "$TRAVAIL/telechargement.txt" 2>&1; then
        journal "téléchargement impossible : $(tail -2 "$TRAVAIL/telechargement.txt" | tr '\n' ' ')"
        pousser "Traits de l'étape 1 : arrêt au téléchargement"; exit 1
    fi
    journal "modèle téléchargé"
    MOD=(--modele "$MODELE" --revision "$REVISION")
fi

for N in $LONGUEURS; do
    journal "extraction ≤ $N jetons"
    # shellcheck disable=SC2086
    if ! python -I -B "$SCRIPT" --banque "$BANQUE" --sortie "$SORTIE/traits-$N" "${MOD[@]}" --couches $COUCHES \
            --agregations dernier moyenne --max-jetons "$N" > "$TRAVAIL/extraction-$N.txt" 2>&1; then
        journal "extraction ≤ $N en échec : $(grep -v '^\[transformers\]' "$TRAVAIL/extraction-$N.txt" | tail -2 | tr '\n' ' ')"
        rm -rf "$SORTIE/traits-$N"
        pousser "Traits de l'étape 1 : extraction ≤ $N en échec"; exit 1
    fi
    journal "extraction ≤ $N : $(python -I -B -c '
import json, sys
m = json.load(open(sys.argv[1], encoding="utf-8"))
print(m["n_taches"], "tâches ;", m["n_tronquees"], "tronquées ;", max(m["jetons_par_tache"].values()), "jetons au plus ;", m["duree_s"], "s ;", m.get("environnement", {}).get("carte"))' \
        "$SORTIE/traits-$N/manifeste-traits.json")"
done
pousser "Traits de l'étape 1 : extractions ≤ 2 048 et ≤ 16 384 jetons" || exit 1
journal "fini"
exit 0
