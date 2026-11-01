# Procédure de scellement, de poussée et de lancement — R1 puis R2 (instance A) et R4 (instance B) — v1

Tout est préparé jusqu'au scellement, rien n'est scellé. À exécuter par la session « session-depot », dans l'ordre, sous
le GO-2026-11-01-13. R2 est autorisé (R-1014 : exception à N-029 confirmée par Lazar, comparaison préenregistrée hors
porte, prédicteur sur les traits obligatoire) ; la ligne R-1014 est recopiée dans `registres/decisions.md` de la branche
de préparation, et la garde codée la vérifie au commit lancé (éprouvée : code 2 sans la ligne, code 0 avec).

## 0. Données fixes

- Branche : `prep/runs-r1-r2-r4-v1`. Le scellement se fait **sur cette branche** (son arbre gelé est celui du commit du
  code ; la branche de travail de la session n'a pas modifié `src/`, `scripts/`, `tests/` depuis `d8af7818`, mais sceller
  ailleurs ferait échouer `exiger_code_cite` au moindre écart).
- **Commit du code d'analyse : `29bd8e2ea29e82a08b4e540ce0ac0b70c025a484`** — déjà inscrit dans les deux préenregistrements
  (les commits suivants ne touchent que `prereg/` et `docs/`, hors de l'arbre gelé).
- Tests attendus : la valeur inscrite dans les deux préenregistrements (suite ciblée de 17 fichiers, mesurée au commit du
  code ; voir le compte rendu de ce brouillon 3).
- Binaire Vast.ai : `VB=/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/vast183-venv/bin`
  (appelé `$VB/vastai create instance` : la garde de calcul reconnaît cette forme et vérifie le GO, éprouvé dans
  `essai-garde-calcul-v2.txt`).

## 1. Vérifier puis sceller (sur la branche de préparation)

```
cd /home/user/controle-ia-travail
git switch prep/runs-r1-r2-r4-v1        # ou un worktree de cette branche
export PYTHONPATH=src
python -c "from controle_ia.prereg import problemes as p; print(p('prereg/R1-R2-rejeu-p3-v1.md'), p('prereg/R4-dose-cout-gonfle-v1.md'))"   # [] []
git diff --quiet 29bd8e2ea29e82a08b4e540ce0ac0b70c025a484 HEAD -- . ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md' && echo "arbre gelé = commit du code"
python -m pytest -q -p no:cacheprovider tests/test_runs_nuit_v1.py tests/test_premier_test_ia_run.py tests/test_premier_test_ia_notation.py \
    tests/test_premier_test_ia_figees.py tests/test_premier_test_ia_conditions.py tests/test_harnais_formats.py tests/test_pilote_a.py \
    tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py tests/test_harnais.py tests/test_bases.py \
    tests/test_validation_reelle.py tests/test_harnais_lots.py tests/test_environnement_a.py tests/test_premier_test_ia_gardes_v1.py \
    tests/test_premier_test_ia_entrainement.py        # doit dire « 291 passed »
python -m controle_ia.runs_nuit.garde_n029_v1 registres/decisions.md   # doit afficher la ligne R-1014 (code 0)
python -m controle_ia.scellement sceller prereg/R1-rejeu-config-v2.json prereg/R2-juge3b-config-v1.json \
    prereg/R2-juge8b-config-v1.json prereg/R2-invite-juge-v1.md prereg/R4-config-v1.json \
    prereg/R4-consignes-dose-faible-v1.md prereg/R4-rejeu-config-v2.json prereg/R4-juge3b-config-v1.json \
    prereg/R4-juge8b-config-v1.json
python -c "from controle_ia.prereg import sceller_prereg as s; print(s('prereg/R1-R2-rejeu-p3-v1.md')); print(s('prereg/R4-dose-cout-gonfle-v1.md'))"
python -m controle_ia.scellement verifier prereg/R1-R2-rejeu-p3-v1.md prereg/R4-dose-cout-gonfle-v1.md prereg/R1-rejeu-config-v2.json \
    prereg/R4-config-v1.json prereg/R4-consignes-dose-faible-v1.md prereg/R4-rejeu-config-v2.json prereg/R4-juge3b-config-v1.json prereg/R4-juge8b-config-v1.json
# contrôle : les empreintes recalculées des pièces = celles citées dans les préenregistrements et les configurations
python - <<'EOF'
import json
from controle_ia.runs_nuit import rejeu_activations_v1 as ra, juge_actions_v1 as ja
from controle_ia.premier_test_ia.run import empreinte_config
t1, t4 = open('prereg/R1-R2-rejeu-p3-v1.md').read(), open('prereg/R4-dose-cout-gonfle-v1.md').read()
assert ra.empreinte_config(json.load(open('prereg/R1-rejeu-config-v2.json'))) in t1
assert ra.empreinte_config(json.load(open('prereg/R4-rejeu-config-v2.json'))) in t4
assert empreinte_config(json.load(open('prereg/R4-config-v1.json'))) in t4
for f, t in (('prereg/R4-juge3b-config-v1.json', t4), ('prereg/R4-juge8b-config-v1.json', t4), ('prereg/R2-juge3b-config-v1.json', t1)):
    assert ja.empreinte_config(json.load(open(f))) in t
print("empreintes citées : conformes")
EOF
git add prereg/*.sha256 && git commit -m "Runs de nuit R1 et R4 : préenregistrements et pièces scellés (GO-2026-11-01-13)"
COMMIT_SCELLEMENT=$(git rev-parse HEAD); echo "$COMMIT_SCELLEMENT"
```

## 2. Pousser et prévenir conv-audit (avant tout départ)

```
git push origin prep/runs-r1-r2-r4-v1           # dépôt de travail lciric/controle-ia-travail ; jamais lciric/controle-ia
sha256sum prereg/R1-R2-rejeu-p3-v1.md prereg/R4-dose-cout-gonfle-v1.md
```

Message à conv-audit : les deux empreintes ci-dessus, `COMMIT_SCELLEMENT`, et la section « Écarts au format » du
`LISEZMOI-runs-r1-r2-r4-v2.md` (écart n° 5 réécrit ci-dessous), puis les branches de résultats attendues
(`calcul/r1-r2-reel-v1`, `calcul/r4-dose-reel-v1`).

**Écart n° 5, réécrit (CLC-01)** : tolérance de fidélité 0,02 × (1 + |score|), non la tolérance d'identité du harnais
(1e-6, mêmes activations). Son pouvoir de discrimination se mesure sur l'instance : contrôle négatif décisif sur 20
actions rejouées sous une consigne fausse, empan juste (au moins 18 hors tolérance). S'il n'est pas discriminant, pas
d'arrêt : règle de repli gelée, `fidele` restreint aux épisodes à trajectoire identique à P3, lecture en réserve
(`regle_repli_appliquee`, `lecture` dans `rejeu-activations.json`). L'empan décalé d'un jeton est rapporté, descriptif.
L'égalité au bit près est mesurée par les empreintes d'activations de P3 (`activations_identiques`).

## 3. Créer les instances

```
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true dph_total<=1.40"
$VB/vastai search offers "$FILTRE" -o 'dph_total' --storage 80        # deux offres : OFFRE_A, OFFRE_B (≤ 1,40 USD/h)
$VB/vastai show instances                                              # aucune instance du programme oubliée

# Instance A : R1 puis R2 (ETAPES par défaut : « rejeu juge3b juge8b » ; garde N-029 au commit lancé)
B64A=$(git show "$COMMIT_SCELLEMENT:scripts/amorce_instance_r1_r2_v1.sh" | base64 -w0)
GO_ID=GO-2026-11-01-13 $VB/vastai create instance "$OFFRE_A" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r1-r2-v1 \
    --env "-e COMMIT=$COMMIT_SCELLEMENT -e BRANCHE=calcul/r1-r2-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64A | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
# (R1 seul, si besoin : même commande, --label r1-v1, BRANCHE=calcul/r1-reel-v1, et « ETAPES=rejeu bash /root/amorce.sh »)

# Instance B : R4
B64B=$(git show "$COMMIT_SCELLEMENT:scripts/amorce_instance_r4_v1.sh" | base64 -w0)
GO_ID=GO-2026-11-01-13 $VB/vastai create instance "$OFFRE_B" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r4-dose-v1 \
    --env "-e COMMIT=$COMMIT_SCELLEMENT -e PREREG=prereg/R4-dose-cout-gonfle-v1.md -e BRANCHE=calcul/r4-dose-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64B | base64 -d > /root/amorce.sh && bash /root/amorce.sh"
```

Consigner les deux identifiants (`new_contract`) dans `registres/depenses.md` (attendu et pire cas du devis v2) et dans
la passation. Surveillance et arrêt (R10 : `$VB/vastai destroy instance <ID>`) : `LISEZMOI-runs-r1-r2-r4-v2.md`.

Jalons nouveaux de A : `etape=reconstruction … trajectoires_identiques=…` (un épisode entièrement conforme à trajectoire
différente arrête la course) ; `etape=fidelite lecture=conforme` ; `etape=controle_negatif lecture=discriminant` (ou
`non discriminant` : la course continue, règle de repli) ; `etape=fin`.

## 4. Coût

Instance A (R1 puis R2) : ≈ 1,9 USD attendu, 5,4 USD au pire × 1,5 ; instance B (R4) : ≈ 4,0 USD attendu, 12,0 USD au
pire × 1,5 ; total au pire × 1,5 : 17,4 USD, sous le plafond de 25 USD (devis v2).
