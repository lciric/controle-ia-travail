# Rapport du développeur sur les corrections du code de l'étape B bis de T0.7 (modèle A), v2 — mineur m-A et commandes de `CODE-BBIS`

**Déclaration** : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien lu sous `diag/`, `runs/`,
`donnees/` du dépôt de travail ; aucune machine, aucun appel réseau, aucune dépense ; aucun des gestes du § 3 n'a été joué
(seulement leur forme, sur un dossier jetable, avec une épreuve factice).

- **Auteur** : « modèle A ». **Date (UTC, `date -u`)** : 2026-11-14, de 16:20 à 16:35.
- **Objet** : vérification courte des corrections (modèle C),
  `brouillons/T0.7-etape-B-bis-v1/code/verification-courte-corrections-modele-c-v1.md`,
  `4514da6c54372be6dbb374bc43b1e269d16d502dd424e50c5685df22b8b0c802`, « scellable avec mineurs », lue en entier ; décision de la
  mère : m-A corrigé avant `CODE-BBIS` ; m-B et m-C : rien, sauf le texte d'aide de `marche_v1` s'il est faux.
- **Commits** (branche `prep/t07bbis-code-v1`, jamais poussée) : départ `38c7203e` ; code `2401fdf2673f6206c40c378a2a66afe4c7aa7b2a` ;
  cette note, la sortie des essais et la liste des fichiers de la fiche : commit suivant. Le rapport v1 et sa sortie restent
  inchangés (R12) ; ce qui les corrige est écrit ici (§ 2, interprétation 32).

## 1. Fait

| constat | fait | où | essai (cas sain ; artefact) |
|---|---|---|---|
| **m-A** | Dès le contrôle de l'étape 7 (branche de sortie absente du dépôt distant : `SORTIE_LIBRE=1`) et tant que la branche n'est pas prête, tout arrêt pousse ses traces : `traces_sur_commit` copie les traces, construit dans un **index à part** un commit des seules traces **posé sur COMMIT** (`read-tree COMMIT`, `add --sparse -f traces/…`, `write-tree`, `commit-tree -p COMMIT`) et le pousse sur `refs/heads/donnees/t07-etape-b-bis-v1` (trois essais) ; la tête, l'arbre et le commit local des entrées de 7b ne sont **ni touchés ni poussés**. Une fois la branche prête (après la marche), le chemin ordinaire (`pousser`) reprend ; si la création de la branche après la marche échoue, les traces partent par le même commit sur COMMIT. Un échec de la poussée est écrit au journal ; le code de l'arrêt est gardé. | `scripts/amorce_bbis_v1.sh` (`arret`, `traces_sur_commit`, `SORTIE_LIBRE`) | `test_arret_avant_la_marche_pousse_ses_traces_sans_le_commit_local` (texte même de l'amorce, joué par bash ; dépôt jetable extrait par les vrais `MOTIFS`, commit local des entrées fait par l'extrait de l'amorce, dépôt distant nu) : sain = arrêt « arbre non propre avant la marche » avec un fichier non suivi et une entrée suivie modifiée → branche poussée, parent = COMMIT, journal et sortie des essais présents, aucune entrée de 7b ni pollution, objet du commit local absent du dépôt distant, tête intacte. Artefacts : arrêt avant le contrôle de l'étape 7 → rien de poussé ; dépôt distant injoignable → « traces non poussées », code gardé ; branche prête → chemin ordinaire, jamais le commit sur COMMIT ; place de `SORTIE_LIBRE=1` (après le contrôle, avant la marche) vérifiée dans le texte. |
| **m-C** | Le texte d'aide de `marche_v1` était faux (« joué dès qu'il est appris ») : il dit maintenant que le contrôle carte-processeur est joué quand l'apprentissage du couple est **complet** (sonde finale, directions du plancher, sondes du nul, ENC ; interprétation 19). Aucun code changé. | `src/controle_ia/t07bbis/marche_v1.py`, docstring, point 3 | — |
| **m-B** | Rien (déclaré, interprétation 26). | — | — |
| **`MIN_ESSAIS`** | 83 → **84** : l'essai m-A tourne aussi sur l'arbre de l'instance (interprétation 25). | `scripts/amorce_bbis_v1.sh` | simulation : 84 passés, 22 sautés (§ 2). |

Essais : arbre complet **106 passés** (105 + 1), 2 min 48 s ; extraction partielle de l'instance simulée au commit `2401fdf2`
(même procédure que la v1, motifs inchangés) **84 passés, 22 sautés** ;
`brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-v2.txt`. Aucun refus de la garde d'isolement dans ce tour.

## 2. Interprétations 29 à 32 (suite)

29. **Moment de l'entropie** : le texte la dit « tirée à l'inscription de `CODE-BBIS` » et place l'épreuve de niveau, jouée sous
    cette entropie (plan, point 12, clé `bbis/epreuve-niveau`), **avant** la ligne (liste d'arrêt : épreuve absente → `CODE-BBIS`
    non inscrite). L'entropie est donc tirée **pour** `CODE-BBIS`, juste avant l'épreuve, puis citée par la fiche et la ligne. Elle
    n'est jamais retirée après lecture de l'issue de l'épreuve (ce serait choisir le niveau) ; une épreuve interrompue se rejoue
    sous la même entropie (résultat déterministe). Recommandation : l'écrire, sceller et committer avant de lancer l'épreuve
    (§ 3, geste 2).
30. **Fichiers cités par la fiche** : `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v1.txt` (90 chemins, scellé) =
    la fermeture des imports `controle_ia.*` atteints depuis le paquet `t07bbis` et les deux scripts Python de B bis (71 fichiers
    sous `src/controle_ia/`, `__init__.py` des paquets compris, imports dans les fonctions compris), les quatre scripts de B bis,
    `tests/conftest.py`, les deux aides et les onze fichiers d'essais du paquet, `requirements-gpu.txt`. Tous sont dans les motifs
    de l'amorce ; l'instance contrôle chacun par son empreinte (B1) : un changement de l'un d'eux entre le commit du code et COMMIT
    arrête la marche à son seuil.
31. **Mécanisme de m-A** : commit des traces sur COMMIT par un index à part plutôt que création anticipée de la branche (qui
    échouerait si l'arbre porte une entrée suivie modifiée, cas même de l'arrêt « arbre non propre »). Les arrêts des étapes 0 à 6
    (avant le contrôle de la branche de sortie) ne poussent toujours rien (déclaré par la vérification courte ; avancer le contrôle
    juste après le clonage les couvrirait aussi : non fait, à décider).
32. **Coût de l'épreuve de niveau** (corrige R-DEV-7 du rapport v1, inchangé) : mesuré deux fois ce jour sur ce processeur
    (4 cœurs, un processus) à la taille du texte (800 directions, 2 000 tirages, 64 tâches) : 6 jeux en 4,1 s, 20 jeux en 14,7 s,
    soit **0,73 s par jeu**, **environ 25 minutes** pour 2 × 1 000 jeux. La mesure de 6,4 s par jeu du rapport v1 était prise sous
    charge ; prévoir au plus 3,5 heures.

## 3. Commandes exactes pour la mère (non jouées ici)

Toutes dans le dépôt de travail `/home/user/controle-ia-travail`, sur la branche qui portera les lignes (`main`), arbre propre,
avec `PY=.venv/bin/python` et `PYTHONPATH=src`. Processeur seulement, aucune dépense, aucune garde de calcul en jeu. Forme
vérifiée sur un dossier jetable (90 fichiers copiés, épreuve **factice** complète) : fiche écrite et scellée, ligne écrite, garde
d'ancêtre acceptée.

**Geste 0 — le code à citer** (à refaire si une correction du code suit cette note) :

```bash
cd /home/user/controle-ia-travail
export PYTHONPATH=src PY=.venv/bin/python L=brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v1.txt
test -z "$(git status --porcelain --untracked-files=all)"            # arbre propre exigé
git merge --no-ff -m "T0.7 étape B bis : code neuf, corrections et essais (prep/t07bbis-code-v1)" prep/t07bbis-code-v1
#   jamais de fusion en un seul commit ni de rebasage (interprétation 22 : le commit cité doit rester dans l'histoire)
$PY -m controle_ia.scellement verifier "$L"
git diff --quiet 2401fdf2673f6206c40c378a2a66afe4c7aa7b2a HEAD -- $(cat "$L")   # code fusionné = code éprouvé ; sinon arrêt :
#   main a changé l'un des 90 fichiers depuis la base de la branche ; rejouer les essais et faire lire l'écart avant d'aller plus loin
$PY -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py          # 106 passés attendus
X=$(git rev-parse HEAD)                                              # commit cité par la fiche (son arbre porte les empreintes)
```

**Geste 1 (a, première partie) — l'entropie, tirée pour `CODE-BBIS`, avant l'épreuve** (interprétation 29) :

```bash
E=$($PY -c 'import numpy as np; e = np.random.SeedSequence().entropy; assert e.bit_length() > 64; print(e)')
$PY -c 'import datetime, json, sys
from controle_ia.scellement import sceller
p = "registres/t07-etape-b-bis/entropie-bbis-v1.json"
open(p, "x", encoding="utf-8").write(json.dumps({"entropie": sys.argv[1], "commit_code": sys.argv[2],
    "outil": "numpy.random.SeedSequence().entropy", "tiree_le": datetime.datetime.now(datetime.timezone.utc).strftime(
    "%Y-%m-%dT%H:%M:%SZ"), "texte": "prereg/T0.7-etape-B-bis-v1.md"}, indent=1) + "\n")
print(sceller(p))' "$E" "$X"
git add registres/t07-etape-b-bis/entropie-bbis-v1.json registres/t07-etape-b-bis/entropie-bbis-v1.json.sha256
git commit -m "T0.7 étape B bis : entropie de CODE-BBIS tirée et scellée avant l'épreuve de niveau"
```

(`assert` : une entropie de 64 bits ou moins, de probabilité 2⁻⁶⁴, serait refusée par la garde `exiger_entropie` ; le tirage
s'arrête alors avant toute écriture et se refait.) L'entropie se relit ensuite par
`E=$($PY -c 'import json; print(json.load(open("registres/t07-etape-b-bis/entropie-bbis-v1.json"))["entropie"])')`.

**Geste 2 (b) — l'épreuve de niveau complète de la règle (a) en deux plis, sous cette entropie** :

```bash
nohup env PYTHONPATH=src $PY scripts/epreuve_niveau_deux_plis_bbis_v1.py --entropie "$E" \
    --sortie registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json --processus 1 > /tmp/epreuve-bbis-v1.log 2>&1 &
echo "PID $!"                                                        # arrêt éventuel par ce PID seulement (R10)
```

- **Réglages** : ceux du texte par défaut (1 000 jeux par cellule, 800 directions, 2 000 tirages, 64 tâches) — ne rien passer
  d'autre ; `--processus 1` (avertissement de `fork` sous plusieurs processus ; résultat indépendant de leur nombre, éprouvé).
- **Durée attendue** : environ 25 minutes sur les 4 cœurs de la session (interprétation 32) ; au plus 3,5 heures.
- **Sortie** : `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json` et son compagnon `.sha256`, **scellés par le
  script** à la fin (rien n'est écrit avant) ; la sortie standard porte `cellules`, `niveau_decisif_retenu`, `complete`.
  Contrôle : `$PY -m controle_ia.scellement verifier registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json` et
  `complete: true` ; puis `git add` du fichier et de son compagnon, `git commit -m "T0.7 étape B bis : épreuve de niveau de la règle (a) en deux plis, complète"`.
- **Ce qui la fait échouer** (code non nul, aucune sortie) : entropie absente, non entière ou de 64 bits ou moins ; fichier de
  sortie déjà présent (R12) ; interruption (rien n'est écrit : la rejouer sous la **même** entropie). **Ce qui la rend
  inutilisable** (la fiche la refuse, `CODE-BBIS` n'est pas inscrite) : un réglage autre que ceux du texte (`complete: false`,
  « réduite »), une autre entropie que celle de la fiche, un sceau rompu, un niveau retenu autre que celui de la règle.
- **Ce qui n'est pas un échec** : un taux de fausse lecture « au-dessus » **supérieur à 0,01** dans une cellule → niveau décisif
  **99,5 %**, mécaniquement, inscrit par la fiche ; le texte exige alors que la puissance à 99,5 % soit recalculée par une version
  neuve du script de calculs (« Seuil », K6), avant la marche.

**Geste 3 (a, suite) — la fiche de `CODE-BBIS`** (format fixé : `registre_bbis_v1.ecrire_fiche_code`, commit, fichiers → empreintes
lues sur le disque, entropie en décimal, `epreuve_niveau` {chemin, empreinte, taux, niveau retenu, coût}, `niveau_decisif`) :

```bash
git diff --quiet "$X" -- $(cat "$L") && test -z "$(git status --porcelain -- $(cat "$L"))"   # disque = commit cité
$PY -m controle_ia.t07bbis.registre_bbis_v1 fiche . registres/t07-etape-b-bis/code-bbis-v1.json "$X" "$E" \
    registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json $(cat "$L")
#   → « BBIS FICHE ECRITE registres/t07-etape-b-bis/code-bbis-v1.json <empreinte> niveau décisif 0.99 | 0.995 » ; fiche scellée
#   (compagnon .sha256) par l'outil ; refus (code 2, motif) : épreuve absente, réduite, d'une autre entropie, niveau hors règle,
#   commit illisible, entropie de 64 bits ou moins, fiche déjà présente
git add registres/t07-etape-b-bis/code-bbis-v1.json registres/t07-etape-b-bis/code-bbis-v1.json.sha256
git commit -m "T0.7 étape B bis : fiche de CODE-BBIS (commit du code, 90 empreintes, entropie, épreuve de niveau)"
```

**Geste 4 (c) — la ligne `CODE-BBIS` du registre propre** `registres/t07-etape-b-bis-v1.md` :

- **Forme** (quatre colonnes exactement ; toute autre forme rend la ligne « mal formée » pour toutes les gardes) :
  `| CODE-BBIS | AAAA-MM-JJTHH:MM:SSZ | registres/t07-etape-b-bis/code-bbis-v1.json | <empreinte SHA-256 de la fiche> |`.
  L'**issue de l'épreuve** n'est pas une colonne : elle est inscrite **avec** la ligne par la fiche qu'elle cite à son empreinte
  (`epreuve_niveau.chemin`, `.sha256`, `.taux` par cellule, `.niveau_decisif_retenu`, `.cout`, et `niveau_decisif`).
- **Outil** : `registre_bbis_v1.ajouter_ligne_propre` (refuse le registre partagé `registres/scellements-v1.md`, toute clé hors de
  la marque BBIS, une ligne déjà présente ; date UTC de l'instant donné) :

```bash
$PY -c 'import time
from pathlib import Path
from controle_ia.t07 import registre_v1 as rg
from controle_ia.t07bbis import registre_bbis_v1 as rb
c = "registres/t07-etape-b-bis/code-bbis-v1.json"
s = rg.sceau_conforme(Path(c)); rb.lire_fiche_code(Path(c))
print(rb.ajouter_ligne_propre(Path("."), rb.REGISTRE_PROPRE, "CODE-BBIS", int(time.time()), c, s))'
git add registres/t07-etape-b-bis-v1.md
git commit -m "T0.7 étape B bis : ligne CODE-BBIS au registre propre"
$PY -m controle_ia.t07bbis.registre_bbis_v1 ancetre . HEAD          # → « BBIS ANCETRE <X> de <tête> » (garde B1)
```

`GO-BBIS` (extrait de GO-2026-11-14-09) s'inscrit ensuite par le même outil, à un instant **strictement postérieur** (la lecture
exige `SCELLEMENT-BBIS` < `CODE-BBIS` < `GO-BBIS` < `SCORES-BBIS`).

**Geste 5 — le jour de la marche** : COMMIT de l'amorce = le commit de `main` qui porte `CODE-BBIS` et `GO-BBIS` (descendant de X),
**poussé** sur le dépôt distant avant la création (l'instance clone `controle-ia-travail`) ; puis
`git diff --quiet "$X" "$COMMIT" -- $(cat "$L")` (aucun des 90 fichiers changé) et
`bash scripts/lancer_bbis_v1.sh commande . OFFRE.json OFFRE_ID "$COMMIT" main RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S FEU RELANCES IMAGE`
(13 arguments ; la commande rejoue la garde d'ancêtre).

## 4. (d) Ordre de ces gestes

Selon le texte scellé (calendrier, ligne du **mardi 17** : « épreuve de niveau ; `CODE-BBIS` (commit, empreintes, entropie, issue
de l'épreuve de niveau) ; `GO-BBIS` ; ordre d'exécution contre-lu ; répétition à blanc ; feu écrit de la mère » ; plan, point 2 :
`SCELLEMENT-BBIS`, puis `CODE-BBIS`, `GO-BBIS`, création, `SCORES-BBIS`… ; liste d'arrêt : « épreuve de niveau absente à
l'inscription de `CODE-BBIS` : `CODE-BBIS` n'est pas inscrite » ; « aucune création sans `GO-BBIS`, le feu écrit de la mère,
`CODE-BBIS` et `SCELLEMENT-BBIS` ») :

0. préalables tenus : `SCELLEMENT-BBIS` et `ABSENCE-B-BBIS` inscrites (2026-11-14T12:30:30Z) ; code contre-lu, corrigé, vérifié ;
   geste 0 (fusion, X) ;
1. entropie tirée, scellée, committée (geste 1) ;
2. épreuve de niveau complète sous cette entropie, lue (niveau 99 % ou 99,5 %), committée (geste 2) ; si 99,5 % : puissance
   recalculée par une version neuve du script de calculs, avant la marche ;
3. fiche, scellée, committée (geste 3) ;
4. **ligne `CODE-BBIS`** (geste 4) : elle **suit** l'épreuve ;
5. ligne `GO-BBIS`, strictement après ;
6. ordre d'exécution contre-lu ; **répétition à blanc** ; feu écrit de la mère ;
7. mercredi 18 : marche (geste 5).

**L'épreuve n'attend pas la répétition à blanc** : elle se joue sur processeur, sur données synthétiques, sans carte ni donnée de
7b, et elle doit précéder `CODE-BBIS`, qui doit elle-même précéder toute création d'instance — la répétition à blanc sur la carte
comprise (liste d'arrêt). **Réserve** : un défaut du code trouvé par la répétition à blanc ne peut plus se corriger sous la même
ligne (lignes jamais réécrites ; le texte ne prévoit le remplacement unique de `CODE-BBIS` que pour l'écart carte-processeur
au-delà de 10⁻⁴ à la marche) : ce serait un nœud de Lazar.

## 5. Empreintes (SHA-256)

| fichier | empreinte |
|---|---|
| `scripts/amorce_bbis_v1.sh` | `673ed08386588488586e8cfb98632d4ec5afd40b3c6a30d72b602bea7727ee39` |
| `src/controle_ia/t07bbis/marche_v1.py` | `2f3ae2ec44dee0233b290cd907a1c84d6d7072dc881026c6a73c426fafb5ee18` |
| `tests/test_t07bbis_chaine_instance_v1.py` | `7960ecd041aee8ee280e95ab9df21bb17e52dc28271cec5daacf47cb339dd2de` |
| `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v1.txt` | `8e3d0799777b0f9cafcab27af73d8b821d6b3218905d8689c4ac3948e6a0b2fd` |
| `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-v2.txt` | `f132e2fd47d58ea1e945c67fde5c774ff009dcdfdbe917a27d40500a05e40fbd` |

Inchangés depuis `189868e6` : tous les autres fichiers de code et d'essais (dont `lancer_bbis_v1.sh` `e34edcf3…`,
`lecture_v1.py` `9d11ba2b…`, `registre_bbis_v1.py` `cee62b1f…`).
