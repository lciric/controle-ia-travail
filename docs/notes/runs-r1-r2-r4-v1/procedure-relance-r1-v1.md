# Procédure de scellement et de lancement — relance de R1 (addendum `prereg/R1-addendum-relance-v1.md`) — v1

Préparée, non exécutée : rien n'est scellé, rien n'est lancé. À exécuter par la session « session-depot », **dans
l'ordre**, seulement après la décision de Lazar sur le nœud de l'addendum. Chaque étape est une condition de la
suivante.

## 0. Données fixes

- Branche : `prep/r1-relance-addendum-v1` (scellement sur cette branche : son arbre gelé est celui du commit du code).
- Commit du code d'analyse : `7b8c6b21cecaecda8ea3428c726f1375ec92396e` (inscrit dans l'addendum) ; tests attendus : 300.
- Binaire Vast.ai : `VB=/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/vast183-venv/bin`.

## 1. Décision de Lazar (nœud)

Ligne consignée dans `registres/decisions.md` (verbatim de Lazar) : addendum accepté, relance de R1 seule, **et
remplacement de la ligne gelée recopiée dans l'analyse principale de conv-audit (l. 146, `8e267952…`) couvert par la
même décision** (N-A, n° 343, option (a)) — sauf si la table ne laisse aucun épisode non résolu. Sans elle, on s'arrête
ici.

## 2. Vérifier puis sceller

```
cd /home/user/controle-ia-travail && git switch prep/r1-relance-addendum-v1     # ou un worktree
export PYTHONPATH=src
python -c "from controle_ia.prereg import problemes as p; print(p('prereg/R1-addendum-relance-v1.md'))"   # []
git diff --quiet 7b8c6b21cecaecda8ea3428c726f1375ec92396e HEAD -- . ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md' && echo "arbre gelé = commit du code"
python -m controle_ia.scellement verifier prereg/R1-R2-rejeu-p3-v1.md          # parent : 80c85a00…
python -m controle_ia.scellement sceller prereg/R1-rejeu-config-v3.json prereg/R1-table-tokenisation-v1.json
python -c "from controle_ia.prereg import sceller_prereg as s; print(s('prereg/R1-addendum-relance-v1.md'))"
python - <<'EOF'
import json, hashlib
from controle_ia.runs_nuit import rejeu_activations_v2 as rb
t = open('prereg/R1-addendum-relance-v1.md').read()
c = json.load(open('prereg/R1-rejeu-config-v3.json'))
assert rb.CONFIG_CITEE.format(rb.empreinte_config(c)) in t and c['prereg_parent_sha256'] in t
assert hashlib.sha256(open('prereg/R1-table-tokenisation-v1.json', 'rb').read()).hexdigest() == c['table_tokenisation_sha256']
print("citations conformes")
EOF
git add prereg/*.sha256 && git commit -m "Relance de R1 : addendum, configuration v3 et table scellés (GO-2026-11-01-13)"
COMMIT_SCELLEMENT=$(git rev-parse HEAD)
git push origin prep/r1-relance-addendum-v1        # dépôt de travail lciric/controle-ia-travail ; jamais lciric/controle-ia
sha256sum prereg/R1-addendum-relance-v1.md
```

## 3. Concordance chez conv-audit — CONDITION DU LANCEMENT (contre-lecture 1, CLA-03 ; n° 339 : « avant tout départ »)

Message à conv-audit : `COMMIT_SCELLEMENT`, chemin et empreinte de l'addendum scellé, section « Écarts au parent »
(E1 à E17 ; signaler E12 et E16 : commande du manifeste `…rejeu_activations_v2`, clé `tokenisation`). **Aucune commande
de création avant leur rapport de concordance.** Consigner ici, avant l'étape 5 :

Une première concordance porte sur le brouillon 1 (`ab947556…`) : `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v1.md`
(`28d8bcff4e8a0ff9745a72ad6332296f580f84431c15f24cd98ba3c027a0555d`, n° 343) ; elle demandait des changements (C-1 à
C-7) : la concordance qui autorise le lancement porte sur **la version scellée**.

- Rapport de concordance (chemin sur la branche du canal) : `À CONSIGNER`
- Empreinte du rapport : `À CONSIGNER`
- Verdict : `À CONSIGNER` (concordance ; ou écarts — tout écart de fond est un nœud porté à Lazar, et on s'arrête)

Vérification :

```
git fetch origin canal/conv-audit-n04
git show origin/canal/conv-audit-n04:<chemin du rapport> | sha256sum      # = empreinte consignée ci-dessus
```

## 4. GO du jour

- Le 2 novembre 2026 : GO-2026-11-01-13 (plafond 25 USD, ≈ 4,6 USD engagés ; devis de la relance : attendu ≈ 1,0 à
  1,4 USD, pire ≈ 2,3 USD).
- **Après le 2 novembre : GO nouveau de Lazar, sous un identifiant nouveau** (la garde refuse le GO échu ; une extension
  ne prolonge pas la validité, R-389). Remplacer `GO-2026-11-01-13` ci-dessous par cet identifiant.

## 5. Créer l'instance

```
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true dph_total<=1.40"
$VB/vastai search offers "$FILTRE" -o 'dph_total' --storage 80
$VB/vastai show instances                                      # aucune instance oubliée
B64=$(git show "$COMMIT_SCELLEMENT:scripts/amorce_instance_r1_relance_v2.sh" | base64 -w0)
GO_ID=GO-2026-11-01-13 $VB/vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r1-relance-v1 \
    --env "-e COMMIT=$COMMIT_SCELLEMENT -e BRANCHE=calcul/r1-relance-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && ETAPES=rejeu bash /root/amorce.sh"
```

Garde de calcul éprouvée sur cette forme : `essai-garde-calcul-relance-v1.txt`. Consigner l'identifiant au registre des
dépenses et dans la passation.

## 6. Surveillance et arrêt

Jalons : `etape=reconstruction … trajectoires_identiques=@@TRAJ@@ corrections=@@CORR@@ non_resolus=@@NR@@` ; `etape=fidelite
lecture=conforme` ; `etape=controle_negatif` ; `etape=fin`. Toutes les 10 minutes ; arrêt par l'identifiant (R10 :
`$VB/vastai destroy instance <ID>`) dès la fin de l'amorce ou au plafond de 100 minutes. Aucune lecture de R2 avant le
résultat de R1 relancée.

## 7. Verser le run relancé sur `calcul/r1-r2-reel-v1` (n° 343, C-2)

L'étape 0.f de l'analyse principale de conv-audit ne lit que `calcul/r1-r2-reel-v1`. Après la course (instance
détruite, résultats poussés sur `calcul/r1-relance-reel-v1`), par un **commit neuf**, sans rien réécrire ni forcer :

```
cd /home/user/controle-ia-travail
git fetch origin calcul/r1-relance-reel-v1 calcul/r1-r2-reel-v1
RUN=<identifiant du run, ex. 20261102-HHMMSS-r1-rejeu-reel>
S=/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/verse-r1
git worktree add "$S" origin/calcul/r1-r2-reel-v1 && cd "$S" && git switch -c verse-r1-relance
git checkout origin/calcul/r1-relance-reel-v1 -- "runs/$RUN" "diag/$RUN"
git checkout origin/calcul/r1-relance-reel-v1 -- "donnees/$RUN" 2>/dev/null || true      # fichiers suivis par ajout forcé
git add -f "runs/$RUN" "diag/$RUN" "donnees/$RUN"
# à l'octet : chaque fichier versé égale celui de la branche de la relance
for f in $(git diff --cached --name-only); do
  [ "$(git rev-parse :"$f")" = "$(git rev-parse origin/calcul/r1-relance-reel-v1:"$f")" ] || { echo "ÉCART $f"; exit 1; }
done
python -m controle_ia.scellement verifier $(git diff --cached --name-only | grep -v '\.sha256$')
git commit -m "R1 relancée (addendum de relance) : run $RUN versé depuis calcul/r1-relance-reel-v1, sans réécriture"
git push origin HEAD:calcul/r1-r2-reel-v1          # avance rapide seulement ; jamais --force
git rev-parse HEAD                                  # commit à donner à conv-audit
cd /home/user/controle-ia-travail && git worktree remove "$S"
```

Rien d'autre n'est touché sur `calcul/r1-r2-reel-v1` (ni l'arrêt de la première course, ni les scores de R2).
