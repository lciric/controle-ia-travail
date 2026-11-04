#!/usr/bin/env bash
# SPARKS-EXP7-NUL sur l'instance louée : mise en place, essais, contrôle de l'accès à Gemma (code HTTP consigné), repli
# gelé sur le modèle de secours, fabrication (ou contrôle causal), manifeste, poussée des sorties légères sur une branche
# neuve. Les modèles restent sur le disque de l'instance (`$TRAVAIL/sortie/modeles`), jamais poussés.
#   COMMIT=<commit> TRAVAIL=<dossier> GO_ID=GO-2026-11-04-04 bash sparks_exp7_nul_instance_v1.sh
# Variables : MODE (reel | jouet), PHASE (fabrication | causal), BRANCHE, HF_TOKEN, GH_TOKEN, DEPOT_URL, VENV_EXISTANT ;
# phase causal : CLE (copie scellée de la clé ouverte), REPONSES (dossier des réponses scellées), MODELES, DEPART.
set -euo pipefail
: "${COMMIT:?}" "${TRAVAIL:?}" "${GO_ID:?}"
MODE="${MODE:-reel}"
PHASE="${PHASE:-fabrication}"
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE" >&2; exit 2 ;; esac
case "$PHASE" in fabrication) B=calcul/sparks-exp7-nul-v1 ;; causal) B=calcul/sparks-exp7-nul-causal-v1 ;; *) exit 2 ;; esac
BRANCHE="${BRANCHE:-$B}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
PREREG=prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md
SHA_PREREG=4bacf20dbb8a0e3f369119841d6fb0b56069d0d31989431238b115df746dd52d
mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'
journal "début : MODE=$MODE PHASE=$PHASE COMMIT=$COMMIT BRANCHE=$BRANCHE GO=$GO_ID"
DEPOT="$TRAVAIL/controle-ia"
[ -e "$DEPOT" ] && { journal "$DEPOT existe déjà (R12)"; exit 2; }
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (SPARKS-EXP7-NUL)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1 || code_branche=$?
[ "$code_branche" = 2 ] || { journal "branche $BRANCHE déjà présente ou dépôt illisible (code $code_branche) : arrêt"; exit 2; }
git checkout -q -b "$BRANCHE"
echo "$SHA_PREREG  $PREREG" | sha256sum -c --quiet || { journal "texte scellé altéré au commit : arrêt"; exit 2; }
git push -q origin "$BRANCHE" || { journal "poussée initiale refusée : arrêt avant l'installation"; exit 2; }

# environnement
if [ -n "${VENV_EXISTANT:-}" ]; then . "$VENV_EXISTANT/bin/activate"; else
    python3.11 -m venv "$TRAVAIL/venv" 2>/dev/null || python3 -m venv "$TRAVAIL/venv"
    . "$TRAVAIL/venv/bin/activate"
    pip install -q -r requirements-gpu.txt > "$TRAVAIL/pip.txt" 2>&1 || { journal "installation refusée"; exit 2; }
fi
pip freeze > "$TRAVAIL/pip-freeze.txt"
nvidia-smi > "$TRAVAIL/nvidia-smi.txt" 2>&1 || journal "pas de carte graphique visible"
export PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 TOKENIZERS_PARALLELISM=false
python -I -B -m pytest -q -p no:cacheprovider tests/test_sparks_exp7_nul_v1.py > "$TRAVAIL/tests.txt" 2>&1 \
    || { journal "essais en échec : arrêt avant tout calcul"; tail -5 "$TRAVAIL/tests.txt"; exit 2; }
journal "essais : $(tail -1 "$TRAVAIL/tests.txt")"

# accès au modèle de départ : code HTTP consigné ; repli gelé (texte scellé, « Modèles ») ; aucun autre changement
code_http() {  # $1 = dépôt Hugging Face ; fichier de configuration lu avec le jeton
    curl -s -o /dev/null -w '%{http_code}' --max-time 60 ${HF_TOKEN:+-H "Authorization: Bearer $HF_TOKEN"} \
        "https://huggingface.co/$1/resolve/main/config.json" || echo 000
}
if [ "$MODE" = jouet ]; then DEPART=jouet; HTTP=sans-objet; else
    DEPART=""
    for candidat in google/gemma-3-270m-it Qwen/Qwen2.5-0.5B-Instruct HuggingFaceTB/SmolLM2-360M-Instruct; do
        HTTP=$(code_http "$candidat")
        journal "accès $candidat : HTTP $HTTP"
        echo "$candidat $HTTP" >> "$TRAVAIL/acces-modeles.txt"
        if [ "$HTTP" = 200 ]; then DEPART=$candidat; break; fi
    done
    [ -n "$DEPART" ] || { journal "aucun modèle accessible : arrêt"; exit 2; }
    [ "$DEPART" = google/gemma-3-270m-it ] || journal "REPLI : modèle de secours $DEPART employé et déclaré (Gemma inaccessible)"
fi

RUN_ID="$(date -u +%Y%m%d-%H%M%S)-sparks-exp7-nul-$PHASE"
python -I -B - "$RUN_ID" "$DEPART" "$HTTP" "$PHASE" <<'PY'
import sys
from pathlib import Path
from controle_ia.manifeste import creer_manifeste
from controle_ia.sparks_exp7_nul_v1 import plan
run_id, depart, http, phase = sys.argv[1:5]
pl = plan.construire_plan()
taches = sorted({f"ordre-{m.ident}" for m in plan.modeles_a_entrainer(pl, avec_reserve=True)}
                | {f"partage-{c.ident}" for c in pl.values() if c.groupe != "ancre"})
cfg = {"etude": "SPARKS-EXP7-NUL", "phase": phase, "modele_depart": depart, "acces_http": http,
       "go": "GO-2026-11-04-04", "hyper": "recette des auteurs (HYPER_AUTEURS)"}
c, _ = creer_manifeste(Path("."), run_id, cfg, taches, entropie=plan.entropie_prereg(), decisif=True,
                       prereg=plan.CHEMIN_PREREG, commande=" ".join(sys.argv))
print(c)
PY
journal "manifeste runs/$RUN_ID/manifeste.json"
SORTIE="$TRAVAIL/sortie"
set +e
if [ "$PHASE" = fabrication ]; then
    if [ "$MODE" = jouet ]; then python -u -I -B -m controle_ia.sparks_exp7_nul_v1.instance jouet --sortie "$SORTIE" 2> "$TRAVAIL/run.err"
    else python -u -I -B -m controle_ia.sparks_exp7_nul_v1.instance fabriquer --sortie "$SORTIE" --depart "$DEPART" 2> "$TRAVAIL/run.err"; fi
else
    : "${CLE:?}" "${REPONSES:?}" "${MODELES:?}"
    python -u -I -B -m controle_ia.sparks_exp7_nul_v1.instance causal --sortie "$SORTIE" --depart "$DEPART" --cle "$CLE" \
        --reponses "$REPONSES"/*/*/reponse-v1.json --modeles "$MODELES" 2> "$TRAVAIL/run.err"
fi
code=$?
set -e
journal "fin du calcul, code $code"
# sorties légères : rapport, comportements, journaux d'entraînement, manifeste ; jamais les modèles
D="diag/$RUN_ID"
mkdir -p "$D"
for f in "$SORTIE"/fabrication-v1.json "$SORTIE"/causal-v1.json; do [ -f "$f" ] && cp "$f" "$D/"; done
if [ -d "$SORTIE/modeles" ]; then
    (cd "$SORTIE/modeles" && find . -name comportement.json -o -name resume.json -o -name log.jsonl -o -name split.json \
        | tar -czf "$OLDPWD/$D/modeles-legers.tar.gz" -T -)
    (cd "$SORTIE/modeles" && find . -name couches.safetensors -exec sha256sum {} +) > "$D/empreintes-couches.txt"
fi
cp "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/pip-freeze.txt" "$D/" 2>/dev/null || true
[ -f "$TRAVAIL/acces-modeles.txt" ] && cp "$TRAVAIL/acces-modeles.txt" "$D/"
grep -vE '^PROGRES ' "$TRAVAIL/run.err" | tail -200 > "$D/run-err-fin.txt" || true
python -I -B -m controle_ia.scellement sceller "$D"/* > /dev/null
git add -A runs "$D" && git commit -qm "SPARKS-EXP7-NUL : $PHASE ($MODE), code $code" || true
for essai in 1 2 3; do git push -q origin "$BRANCHE" && break; sleep $((15 * essai)); done
journal "poussé sur $BRANCHE ; modèles gardés dans $SORTIE/modeles (arrêt de l'instance par son identifiant, R10)"
exit $code
