# Procédure de scellement et de lancement — relance de R1 (addendum `prereg/R1-addendum-relance-v1.md`, brouillon 2) — v2

Préparée, non exécutée : rien n'est scellé, rien n'est lancé. Remplace la v1 (`procedure-relance-r1-v1.md`, archivée
sans modification) : GO-2026-11-02-02 au lieu de GO-2026-11-01-13 (qui échoit le 2 novembre) ; décisions de Lazar N-A et GO prises
(R-1116) ; extension C-6 et table v2 ; configuration v4 ; chemins du bloc-notes de la session neuve. À exécuter par la
session « session-depot », **dans l'ordre** ; chaque étape est une condition de la suivante.

## 0. Données fixes

- Branche : `prep/r1-relance-addendum-v1` (scellement sur cette branche : son arbre gelé est celui du commit du code).
- Commit du code d'analyse : `5e678b5b78152a4cf353a8386f54413111adf230` (inscrit dans l'addendum) ; tests attendus :
  302 (suite ciblée de 18 fichiers). **Si du code change avant le scellement** (module, tests, scripts), il est commité
  d'abord, dans un commit à part, puis l'addendum est mis à jour (« Commit du code d'analyse », « Tests attendus », E10)
  dans un commit suivant : le code est toujours commité avant le texte qui le cite.
- Bloc-notes : `S=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad` ; arbre de travail
  `$S/wt-addendum` (un seul arbre à la fois : disque).
- Binaire Vast.ai : `VB=/opt/vastai-venv-v1/bin`.
- Tokeniseur de l'agent (fichiers publiés de la révision `0e9e39f2…`) : `$S/tok-addendum-r1` (`tokenizer.json`
  `79e3e522…`, `tokenizer_config.json` `177c7b61…` 55 351 octets, `special_tokens_map.json` `6f38c737…`) ; vérifier
  les trois empreintes avant chaque usage.
- Environnement : `/home/user/controle-ia-travail/.venv` ; `PYTHONPATH=src`.

## 1. Décisions de Lazar (prises ; à recopier et à faire redire)

Prises le 2 novembre 2026 à 06:32 UTC dans la session de conv-audit (R-1116 ; `registres/go.md` de
`canal/conv-audit-n04`, commit `6a4aeffe`) : N1 = (b) ; **N-A = (c) puis (a)** (C-6 d'abord ; puis la décision sur
l'addendum couvre la ligne recopiée dans l'analyse principale de conv-audit, l. 146, `8e267952…`, pour les épisodes que
C-6 laisse non résolus) ; N2 = (a) ; **GO-2026-11-02-01** (décision) et **GO-2026-11-02-02** (calcul : extension de
GO-2026-11-01-13 et relance de R1, plafond 25 USD inchangé, échéance 2026-11-09).

- Recopier les deux lignes, à l'octet, dans `registres/go.md` de `main` (sous une numérotation nouvelle seulement si ces
  identifiants y sont déjà pris ; alors l'addendum et l'étape 5 citent le nouvel identifiant), et consigner la recopie
  dans `registres/decisions.md` (renvoi à R-1116 et au n° 344, `cc8af25a…`).
- Lazar redit ces décisions et le GO de sa main dans la session de session-depot (n° 344, point 2) ; consigner son
  verbatim. Sans ces deux points, on s'arrête ici.

```
cd /home/user/controle-ia-travail
git fetch --filter=blob:none origin refs/heads/canal/conv-audit-n04:refs/remotes/origin/canal/conv-audit-n04
git show origin/canal/conv-audit-n04:registres/go.md | grep -E '^\| GO-2026-11-02-0[12] \|'    # les deux lignes
grep -nE '^\| GO-2026-11-02-0[12] \|' registres/go.md || echo "à recopier"                       # sur main
```

## 1 bis. Extension C-6 et table v2 (processeur, sans dépense)

1. Exécuter l'extension C-6 (dix niveaux, ordre fixe, addendum, « Plan d'analyse », étape 0) sur les 7 épisodes non
   résolus de la table v1 ; verser le script et son résultat sous `docs/notes/runs-r1-r2-r4-v1/` (noms versionnés,
   compagnons `.sha256`) ; recopier dans l'addendum leurs chemins, empreintes et le commit.
2. Construire la table v2 (fusion revérifiée par la fonction de l'instance) :

```
cd $S/wt-addendum && export PYTHONPATH=src
sha256sum $S/tok-addendum-r1/tokenizer.json $S/tok-addendum-r1/tokenizer_config.json $S/tok-addendum-r1/special_tokens_map.json
python -m controle_ia.runs_nuit.resolution_tokenisation_v1 --tokeniseur $S/tok-addendum-r1 \
    --config prereg/R1-rejeu-config-v3.json --table-recherche prereg/R1-table-tokenisation-v1.json \
    --resultat-c6 docs/notes/runs-r1-r2-r4-v1/<résultat C-6> --sortie prereg/R1-table-tokenisation-v2.json
```

3. Écrire `prereg/R1-rejeu-config-v4.json` : la v3 à l'identique, sauf `chemin_table_tokenisation` =
   `prereg/R1-table-tokenisation-v2.json` et `table_tokenisation_sha256` = empreinte du fichier de la table v2 ;
   empreinte canonique : `python -c "import json; from controle_ia.runs_nuit import rejeu_activations_v2 as rb;
   print(rb.empreinte_config(json.load(open('prereg/R1-rejeu-config-v4.json'))))"`.
4. Rejouer sur la table v2 et la configuration v4 : `comptes_table_relance_v2.py` (sortie
   `comptes-table-relance-v3.json`, nom neuf) et `essai_paires_consigne_fausse_v1.py` (sortie
   `essai-paires-consigne-fausse-v2.json`) ; `python -m pytest -q tests/test_runs_nuit_v2.py -k reelle` (la table v2
   versée est contrôlée par `test_table_reelle_versee_coherente`).
5. Remplacer dans l'addendum chaque « À REMPLIR après C-6 » (r ; empreintes de la configuration v4 et de la table v2 ;
   comptes ; essais ; jalons de l'étape 6 ci-dessous) ; si r = 7, écrire que E19 est sans objet. Commit « texte ».

## 2. Contre-lecture 2, vérifier puis sceller

Contre-lecture 2 par un sous-agent neuf (R2 ; le brouillon 2 change l'étape 0 et le code de la table) : lui donner
explicitement l'addendum, le parent, le rapport de la contre-lecture 1, le n° 343, le n° 344, le code au commit cité,
la table v2, la configuration v4 et le résultat C-6 ; remplir l'entrée « Contre-lecture 2 » (brouillon relu et son
empreinte, rapport et son empreinte, traitement). Puis :

```
cd $S/wt-addendum && export PYTHONPATH=src
python -c "from controle_ia.prereg import problemes as p; print(p('prereg/R1-addendum-relance-v1.md'))"   # [] (aucun « À REMPLIR »)
git diff --quiet 5e678b5b78152a4cf353a8386f54413111adf230 HEAD -- . ':(exclude)prereg' ':(exclude)brouillons' ':(exclude)registres' ':(exclude)docs' ':(exclude)diag' ':(exclude)runs' ':(exclude)donnees' ':(exclude)livrables' ':(exclude)papiers' ':(exclude)traces' ':(exclude)CLAUDE.md' && echo "arbre gelé = commit du code"
python -m controle_ia.scellement verifier prereg/R1-R2-rejeu-p3-v1.md          # parent : 80c85a00…
python -m controle_ia.scellement sceller prereg/R1-rejeu-config-v4.json prereg/R1-table-tokenisation-v2.json
python -c "from controle_ia.prereg import sceller_prereg as s; print(s('prereg/R1-addendum-relance-v1.md'))"
python - <<'EOF'
import json, hashlib
from controle_ia.runs_nuit import rejeu_activations_v2 as rb
t = open('prereg/R1-addendum-relance-v1.md').read()
c = json.load(open('prereg/R1-rejeu-config-v4.json'))
assert rb.CONFIG_CITEE.format(rb.empreinte_config(c)) in t and c['prereg_parent_sha256'] in t
assert hashlib.sha256(open('prereg/R1-table-tokenisation-v2.json', 'rb').read()).hexdigest() == c['table_tokenisation_sha256']
assert c['chemin_table_tokenisation'] == 'prereg/R1-table-tokenisation-v2.json'
print("citations conformes")
EOF
git add prereg/*.sha256 && git commit -m "Relance de R1 : addendum, configuration v4 et table v2 scellés (GO-2026-11-02-02)"
COMMIT_SCELLEMENT=$(git rev-parse HEAD)
sha256sum prereg/R1-addendum-relance-v1.md
```

## 2 bis. Chemin réel avec addendum scellé (contre-lecture 1, CLA-04, point 1 ; avant la poussée)

Au commit de scellement, sur processeur, sans modèle : lecture des citations par la fonction du script d'instance et
sceaux des quatre fichiers, puis gardes de citation de `executer` (configuration, parent, entropie, commit du code).

```
cd $S/wt-addendum && export PYTHONPATH=src && PREREG=prereg/R1-addendum-relance-v1.md
lire_unique() { local n; n=$(grep -c "$1 : \`" "$PREREG" || true); [ "$n" = 1 ] && sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"; }
C=$(lire_unique "Chemin de la configuration du rejeu"); T=$(lire_unique "Chemin de la table de tokenisation")
P=$(lire_unique "Chemin du préenregistrement parent"); N=$(lire_unique "Tests attendus"); echo "$C $T $P $N"
python -m controle_ia.scellement verifier "$PREREG" "$C" "$T" "$P"
python - "$PREREG" "$C" <<'EOF'
import json, sys
from pathlib import Path
from controle_ia.harnais.validation_reelle import ENTROPIE_CITEE, exiger_code_cite
from controle_ia.runs_nuit import rejeu_activations_v2 as rb
from controle_ia.runs_nuit.resolution_tokenisation_v1 import charger_table
from controle_ia.scellement import verifier
prereg, c = sys.argv[1], json.load(open(sys.argv[2]))
rb.exiger_config(c)
t = Path(prereg).read_text(encoding="utf-8")
assert rb.CONFIG_CITEE.format(rb.empreinte_config(c)) in t and c["prereg_parent_sha256"] in t
assert verifier(c["chemin_prereg_parent"]) == c["prereg_parent_sha256"] and ENTROPIE_CITEE.search(t)
exiger_code_cite(Path("."), Path(prereg))
tab = charger_table(c["chemin_table_tokenisation"], c["table_tokenisation_sha256"])
print("chemin réel conforme :", len(tab["episodes"]), "entrées de table")
EOF
```

Consigner la sortie sous `docs/notes/runs-r1-r2-r4-v1/essai-chemin-reel-relance-v1/` (commit « texte » après le
scellement). Puis : `git push origin prep/r1-relance-addendum-v1` (dépôt de travail `lciric/controle-ia-travail` ;
jamais `lciric/controle-ia`).

## 3. Concordance chez conv-audit — CONDITION DU LANCEMENT (contre-lecture 1, CLA-03 ; n° 339 : « avant tout départ »)

Message à conv-audit : `COMMIT_SCELLEMENT`, chemin et empreinte de l'addendum scellé, section « Écarts au parent »
(E1 à E20 ; signaler E12 et E16 : commande du manifeste `…rejeu_activations_v2`, clé `tokenisation` ; CLA-10), r et la
liste des épisodes restés non résolus (n° 344, point 3 b). **Aucune commande de création avant leur rapport de
concordance.** Consigner ici, avant l'étape 5 :

Une première concordance porte sur le brouillon 1 (`ab947556…`) : `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v1.md`
(`28d8bcff4e8a0ff9745a72ad6332296f580f84431c15f24cd98ba3c027a0555d`, n° 343) ; elle demandait des changements (C-1 à
C-7) : la concordance qui autorise le lancement porte sur **la version scellée**.

- Rapport de concordance (chemin sur la branche du canal) : `À CONSIGNER`
- Empreinte du rapport : `À CONSIGNER`
- Verdict : `À CONSIGNER` (concordance ; ou écarts — tout écart de fond est un nœud porté à Lazar, et on s'arrête)

Vérification :

```
git fetch --filter=blob:none origin refs/heads/canal/conv-audit-n04:refs/remotes/origin/canal/conv-audit-n04
git show origin/canal/conv-audit-n04:<chemin du rapport> | sha256sum      # = empreinte consignée ci-dessus
```

## 4. GO du jour

- Du 2 au 9 novembre 2026 : **GO-2026-11-02-02** (plafond 25 USD hérité de GO-2026-11-01-13, ≈ 4,6 USD engagés ;
  devis de la relance : attendu ≈ 1,0 à 1,4 USD, pire ≈ 2,3 USD), présent dans `registres/go.md` du dépôt d'où part la
  commande (la garde lit ce registre : `essai-garde-calcul-relance-v2.txt`).
- **Après le 9 novembre : GO nouveau de Lazar, sous un identifiant nouveau** (la garde refuse le GO échu ; une extension
  ne prolonge pas la validité, R-389). Remplacer `GO-2026-11-02-02` ci-dessous par cet identifiant, et l'addendum (E17)
  par un écart déclaré.

## 5. Créer l'instance

```
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true dph_total<=1.40"
$VB/vastai search offers "$FILTRE" -o 'dph_total' --storage 80
$VB/vastai show instances                                      # aucune instance oubliée
B64=$(git show "$COMMIT_SCELLEMENT:scripts/amorce_instance_r1_relance_v2.sh" | base64 -w0)
GO_ID=GO-2026-11-02-02 $VB/vastai create instance "$OFFRE" --raw --image python:3.11-bookworm --disk 80 --cancel-unavail \
    --label r1-relance-v1 \
    --env "-e COMMIT=$COMMIT_SCELLEMENT -e BRANCHE=calcul/r1-relance-reel-v1 -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN" \
    --entrypoint bash --args -c "echo $B64 | base64 -d > /root/amorce.sh && ETAPES=rejeu bash /root/amorce.sh"
```

Les clés se lisent par nom dans l'environnement ; aucune n'est écrite ni affichée. Garde de calcul éprouvée sur cette
forme : `essai-garde-calcul-relance-v2.txt`. Consigner l'identifiant au registre des dépenses et dans la passation.

## 6. Surveillance et arrêt

Jalons : `etape=reconstruction … trajectoires_identiques=<144 + r> corrections=<15 + r> non_resolus=<7 − r>` (valeurs à
recopier ici après C-6 : À CONSIGNER) ; `etape=fidelite lecture=conforme` ; `etape=controle_negatif` ; `etape=fin`.
Toutes les 10 minutes ; arrêt par l'identifiant (R10 : `$VB/vastai destroy instance <ID>`) dès la fin de l'amorce ou au
plafond de 100 minutes. Aucune lecture de R2 avant le résultat de R1 relancée (N1 = (b)).

## 7. Verser le run relancé sur `calcul/r1-r2-reel-v1` (n° 343, C-2)

L'étape 0.f de l'analyse principale de conv-audit ne lit que `calcul/r1-r2-reel-v1`. Après la course (instance
détruite, résultats poussés sur `calcul/r1-relance-reel-v1`), par un **commit neuf**, sans rien réécrire ni forcer, et
sans ouvrir aucun résultat avant la sortie scellée et le message à conv-audit :

```
cd /home/user/controle-ia-travail
git fetch --filter=blob:none origin refs/heads/calcul/r1-relance-reel-v1:refs/remotes/origin/calcul/r1-relance-reel-v1 \
    refs/heads/calcul/r1-r2-reel-v1:refs/remotes/origin/calcul/r1-r2-reel-v1
RUN=<identifiant du run, ex. 20261102-HHMMSS-r1-rejeu-reel>
V=$S/verse-r1                                      # remplace l'arbre de travail de l'addendum, retiré avant (disque)
git worktree add "$V" origin/calcul/r1-r2-reel-v1 && cd "$V" && git switch -c verse-r1-relance
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
cd /home/user/controle-ia-travail && git worktree remove "$V"
```

Rien d'autre n'est touché sur `calcul/r1-r2-reel-v1` (ni l'arrêt de la première course, ni les scores de R2).
