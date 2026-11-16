# Rapport des gestes d'avant course de l'étape B bis de T0.7 (v1)

- **Auteur** : exécutant, sous-agent de la session mère (« modèle B », R-2975). Il n'a écrit ni le texte scellé, ni l'addendum, ni
  le code, ni le plan, ni aucune contre-lecture de l'étape B bis.
- **Date (UTC)** : 2026-11-16, lecture de 12:21:55 à 12:27, gestes de 12:27:41 à 12:59:04, contrôles finaux jusqu'à 13:00:22,
  rapport écrit à partir de 13:01:59 (toutes les heures viennent de `date -u`, dans la commande même du geste).
- **Lieu** : arbre de travail `/home/user/controle-ia-travail/.claude/worktrees/agent-a4f221610ce6d5a67`, branche
  `prep/t07bbis-code-v1`. Rien n'a été écrit dans le dépôt principal ni sur `main`.
- **Procédure jouée** : `brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md`
  (`e2505df9fbb28c9b84ab24f552a130078b8a0281b94f0c6d1ea961f08a289239`), § 1.4 et § 3, à la lettre, dans l'ordre ; arrêt avant le
  § 4 (aucune recherche d'offres, aucun feu, aucune commande de création).
- **Statut** : rapport de gestes ; rien loué, rien dépensé, aucun appel au loueur.

## Verdict

1. **Tout est fait et poussé** : réception unique de `main` (M_b), contrôle des 103 empreintes, entropie, épreuve de niveau, fiche,
   ligne `CODE-BBIS`, extrait et ligne `GO-BBIS`. Aucun arrêt, aucune commande refusée.
2. **Épreuve de niveau** : taux de fausse lecture 0 sur 1 000 dans la cellule `nul` et 0 sur 1 000 dans la cellule
   `signal-commun` ; **niveau décisif retenu : 99 %** (règle du texte, appliquée par le code). Le script de calculs v3 n'a pas
   lieu d'être.
3. **Commit de la course** (plan, § 1.3 et § 3) : `31fa8ac6041faf76b66282e0346750b9aefd4790`, poussé à 12:59:04Z. Aucun bloquant
   dans le périmètre de l'exécutant ; ce qui reste appartient à la mère (dernière section).

## Sources lues (chemin et empreinte)

| pièce | empreinte |
|---|---|
| `brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md` (lu en entier, 544 lignes) | `e2505df9fbb28c9b84ab24f552a130078b8a0281b94f0c6d1ea961f08a289239` |
| `prereg/T0.7-etape-B-bis-v1.md` (texte scellé, lu en entier) | `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` |
| `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` (addendum scellé, lu en entier sur `main`) | `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` |
| `src/controle_ia/t07bbis/registre_bbis_v1.py` (lu en entier) | `c3b1848b3466a88a250aee2b58477c91ff5d660592c1a6cc695f8910005dcf1b` |
| `scripts/epreuve_niveau_deux_plis_bbis_v1.py` (lu en entier) | `3315edea63ffa064e299c3d97037d5bb4449a951162b45b3e64cf348d2bc1ba7` |
| `scripts/lancer_bbis_v3.sh` (lu en entier) | `dc26ea01a06bfb9eac3fc4f9f1b9b3bb86490d61d9e8f5deb54bcb180b17ee68` |
| `scripts/amorce_bbis_v3.sh` (lignes 25 à 60, 95 à 125, 140 à 215) | `18e2f2052efdca0d9d447738c3c4f1099302f7134b9518b59eea78ba563695dd` |
| `src/controle_ia/scellement.py` (lu en entier ; même fichier sur `main` et sur la branche) | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` |
| `src/controle_ia/t07/registre_v1.py` (lignes 87 à 126, 226 à 243, 315 à 356) | `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec` |
| `brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v3.txt` (103 chemins) | `b8fb095bf44dc855868e1b48cef6005222af6888b00a9df2f60fccc36ded7d5d` |
| `brouillons/T0.7-etape-B-bis-v1/code/empreintes-fiche-code-bbis-v3-ce470564-v1.txt` (103 lignes) | `291f1d5cb8a6608cdb91c0ae7aa3527c44e322831010ba86ea6f0d632611db09` |

Lus aussi, par parties : `src/controle_ia/t07bbis/commun_v1.py` (lignes 1 à 100), `marche_v3.py` (lignes 190 à 240),
`lecture_v2.py` (lignes 500 à 610 et 1296 à 1352), `lecture_v1.py` (fonction `lire_lignes`, égale à celle de la v2) ;
`.claude/hooks/garde_calcul.py` et `.claude/settings.json` (dépôt principal) ; `registres/decisions.md` sur `main`, lignes R-2970
à R-2976 ; `registres/go.md`, ligne `GO-2026-11-14-09`, entière ; `registres/passations/2026-11-10-2206.md`, ligne 7 (forme de la
garde des secrets).

**Pour la liste « qui a lu quoi »** : de l'étape B de T0.7, rien (aucune sortie, aucune consigne de lecteur, aucun fichier de la
phase C) ; rien de 7a ni de 7b ; aucun fichier ouvert sous `diag/`, `donnees/`, `docs/verdicts/`. En cherchant la forme de la
garde des secrets, des fragments de lignes du registre des décisions et de passations anciennes ont été affichés (dont le début
de R-2843, coupé à 900 caractères) : aucune valeur de résultat.

## Constats d'avant geste

- 12:21:55Z : branche `prep/t07bbis-code-v1`, tête `bd1472adf07eeb5a4d95169f57add1bb49290915`, quatre fichiers non suivis (le
  plan, la liste des empreintes, leurs compagnons) : l'attendu.
- 12:25:00Z : le processus chronométré 612 n'existe plus ; charge 0,26 ; quatre cœurs. La ligne R-2976 de `main` écrit que
  l'étape 0 de l'idée 1.1 a fini à 12:23:08Z. **Divergence levée par les faits** : R-2975, point (8), écrit « l'épreuve de niveau
  part dès la fin du chronométrage » ; la consigne de l'exécutant écrivait « peut tourner maintenant sur un cœur » ; l'épreuve
  est partie à 12:30:30Z, après la fin du chronométrage : les deux formules sont tenues.
- 12:27:08Z : dépôt distant `origin` = `https://github.com/lciric/controle-ia-travail` (lecture et poussée) ; têtes distantes :
  `main` `16484e4895f47d3c7d9a09d634de98586ca047ff`, branche du code `bd1472ad…` (égale à la tête locale).
- `main` avançait pendant les gestes (`377a2a0c` au plan, `1332acb3` à 12:22, `16484e48` à 12:26, `60eee4e5` à 13:00). La
  fusion a pris la valeur écrite au plan, `M0 = 377a2a0c9b1ec2704374a50537d5c59ae39b0ac7`, sur laquelle le plan avait fait ses
  contrôles ; le relevé a été joué aussi sur la tête de `main` du moment.

## Gestes, dans l'ordre

Variables de toutes les commandes (posées à chaque appel, le dossier courant étant l'arbre de travail) :

```bash
export PYTHONPATH=src PY=/home/user/controle-ia-travail/.venv/bin/python
X=ce47056455595bc52fad676c0e57ad9d8bef886d
L=brouillons/T0.7-etape-B-bis-v1/code/fichiers-fiche-code-bbis-v3.txt
EL=brouillons/T0.7-etape-B-bis-v1/code/empreintes-fiche-code-bbis-v3-ce470564-v1.txt
M0=377a2a0c9b1ec2704374a50537d5c59ae39b0ac7
```

Garde des secrets : la forme de `registres/passations/2026-11-10-2206.md`, ligne 7 (compte des motifs de clés dans
`git diff --cached`, enchaîné au commit) ; **0 avant chacun des sept commits**.

### (0) Plan et liste des empreintes versés sur la branche — 12:27:41Z à 12:27:47Z

```bash
$PY -m controle_ia.scellement verifier brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md "$EL"
git add brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md brouillons/T0.7-etape-B-bis-v1/plan-course-bbis-v1.md.sha256 "$EL" "$EL.sha256"
git commit -q -m "B bis : plan de course v1 et empreintes de la fiche au commit ce470564" -m "<lignes d'attribution>"
test -z "$(git status --porcelain --untracked-files=all)"
```

Résultat : sceaux conformes (`e2505df9…`, `291f1d5c…`) ; la liste des empreintes porte les 103 chemins de la liste de la fiche,
dans le même ordre ; garde des secrets 0 ; commit **`77f8a2c2dd6730220f1f1e91488ef8368412bec5`** ; arbre propre.

### (a) Relevé d'avant fusion, par les noms seulement — 12:28:00Z à 12:28:02Z

```bash
test "$(git rev-parse "$M0:registres/scellements-v1.md.ouvertures.md")" = 76dde869e99c7ab7d05c934405722bd80a1a17bc
test "$(git ls-tree -r --name-only "$M0" | grep -c -E '(^|/)(lecture-t07|arret-etape-b)\.json$')" = 0
git ls-remote --exit-code origin 'refs/heads/verdict/t07-etape-b*' > /dev/null 2>&1; test $? = 2
```

| contrôle | `M0` (`377a2a0c…`) | tête de `main` du moment (`16484e48…`) | tête de la branche (`77f8a2c2…`) |
|---|---|---|---|
| journal des ouvertures du registre partagé (objet git) | `76dde869e99c7ab7d05c934405722bd80a1a17bc` (celui de l'étape A) | le même | le même |
| fichiers nommés `lecture-t07.json` ou `arret-etape-b.json` | 0 | 0 | 0 |

Branche distante `verdict/t07-etape-b*` : **absente** (`git ls-remote --exit-code` rend 2) ; témoin positif
`refs/heads/prep/t07bbis-code-v1` : code 0 ; branches distantes `verdict/*` présentes : `verdict/p3bis-compte-2-v1` et
`verdict/t06-table-a-7b-compte-3-v1`. Les trois tests du plan rendent 0 : **relevé réussi**, `main` ne porte aucune sortie de
l'étape B.

### (b) Fusion unique de `main` dans la branche (M_b) et contrôle des 103 chemins — 12:28:23Z à 12:28:57Z

Avant la fusion (12:28:23Z, lecture seule) : base commune `048d8e991ab25d2bf72dc5c5bb35483e9ab3b520` ; garde des secrets sur ce
que `main` apporte (`git diff` de la base à `M0`, compte seulement, rien d'affiché) : 0 ; quatre chemins touchés des deux côtés,
aux mêmes objets git (les deux fichiers de `registres/code-mots-et-cout-t06/` et `scripts/mots_et_cout_t06_v3.py` avec son
compagnon) ; registre propre au même objet des deux côtés (`598607dba6b4394a39fb347450feee98d12744a7`) ; sur les 103 chemins de
la fiche, 61 présents sur `M0` et identiques, 42 absents de `M0`.

```bash
test -z "$(git status --porcelain --untracked-files=all)"
git merge --no-ff -q -m "B bis : main reçue une fois avant la course (sans rien de l'étape B), R-2760" -m "<lignes d'attribution>" "$M0"
$PY -m controle_ia.scellement verifier "$L" "$EL"
git merge-base --is-ancestor "$X" HEAD && git diff --quiet "$X" HEAD -- $(cat "$L") && sha256sum -c --quiet "$EL"
```

Résultat (12:28:41Z à 12:28:42Z) : code 0, aucun conflit ; **M_b = `f9bd9ba6e7af813207a3d9dd4c24ef280007bcaa`**, parents
`77f8a2c2dd6730220f1f1e91488ef8368412bec5` et `377a2a0c9b1ec2704374a50537d5c59ae39b0ac7` ; arbre propre.
Contrôles (12:28:57Z) : sceaux de la liste des chemins (`b8fb095b…`) et de la liste des empreintes (`291f1d5c…`) conformes ;
`ce470564` ancêtre de M_b ; aucun écart entre `ce470564` et M_b sur les 103 chemins ; **`sha256sum -c` : 103 conformes sur 103**.
Contrôles de plus : 1 926 fichiers changés par M_b face à son premier parent, 199 face au second ; garde des secrets sur M_b
face au premier parent : 0 ; registre propre inchangé (`082b7e70e86d5ac9b20f581c6a182c1746c17c83809ceac93abc0a204788600b`) ;
registre voisin des addenda `93f0d3ddfe3c20fa34d35dc943c6361116a3b91bb4b2ed4f13ef14d89b736054` (ligne `ADDENDUM-ECART-1-BBIS`
datée 2026-11-16T00:59:36Z, donc avant `CODE-BBIS`) ; addendum présent sous `prereg/` (`f00eda8a…`) ; journal des ouvertures
toujours à l'objet `76dde869…` ; 0 fichier `lecture-t07.json` ou `arret-etape-b.json` ; le registre partagé porte désormais
`CODE-MOTS-ET-COUT-T06` (2026-11-14T14:55:41Z) et `AUDIT-FUITES-T07` (2026-11-14T14:57:54Z), aucune ligne
`ISSUE-MOTS-ET-COUT-T06`, aucune clé de B bis.

### (c) Poussée de la branche — 12:29:05Z à 12:29:07Z

```bash
git push origin HEAD:prep/t07bbis-code-v1
```

Résultat : `bd1472ad..f9bd9ba6`, code 0 ; tête distante relue : `f9bd9ba6e7af813207a3d9dd4c24ef280007bcaa`.

### (d) § 1.4, geste 1 : entropie tirée, scellée, committée avant l'épreuve — 12:29:39Z à 12:30:11Z

Commande du plan, sans changement (tirage par `numpy.random.SeedSequence().entropy`, numpy 2.4.6 ; écriture du fichier en mode
« créer seulement » ; scellement par `controle_ia.scellement.sceller`).

Résultat : `registres/t07-etape-b-bis/entropie-bbis-v1.json`,
`f648989bdae47291d8a5504ec33ee5b971bb5ce302f63918e3452c8cff65cfcd` ; entropie de 128 bits,
`208082752394230630219821407440340422345` ; champ `tiree_le` : 2026-11-16T12:29:40Z ; champ `commit_code` : `ce470564…` ;
commit **`e1caae013b30d47495d52c7c1e93d2ad6cf38ddb`** (message du plan) ; poussé à 12:30:11Z (`f9bd9ba6..e1caae01`, code 0) :
l'entropie était sur le dépôt distant avant le départ de l'épreuve. Dans tous les gestes suivants, l'entropie est relue par
programme dans ce fichier, jamais retapée.

### (d) § 1.4, geste 2 : épreuve de niveau — 12:30:30Z à 12:57:04Z

```bash
PYTHONPATH=src OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nohup nice -n 19 "$PY" \
    scripts/epreuve_niveau_deux_plis_bbis_v1.py --entropie "$E" \
    --sortie registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json --processus 1 > JOURNAL 2>&1 &
```

Départ 12:30:30Z, identifiant de processus 1736 (un processus, un fil, priorité `nice` 19) ; fin à 12:56:13Z (horodatage de la
sortie) ; aucune interruption. Sortie scellée par le script : `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json`,
**`641adeb57b8c271be60a89af2513805e591a63c7c0dde17883e4ace0d3f59cbf`** ; `complete` vrai ; entropie de l'épreuve égale à
l'entropie scellée ; commit **`70a4a9a879ef4bb263ec94d9e4b1792cefd01682`** (12:57:04Z). Résultats : section suivante.

### (d) § 1.4, geste 3 : fiche — 12:57:19Z à 12:57:27Z

```bash
git diff --quiet "$X" -- $(cat "$L") && test -z "$(git status --porcelain -- $(cat "$L"))"
$PY -m controle_ia.t07bbis.registre_bbis_v1 fiche . registres/t07-etape-b-bis/code-bbis-v1.json "$X" "$E" \
    registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json $(cat "$L")
```

Résultat : « BBIS FICHE ECRITE registres/t07-etape-b-bis/code-bbis-v1.json ee362bb7… niveau décisif 0.99 » ; contrôle du plan :
« fiche = liste préparée (103 empreintes, commit ce470564) ». Fiche : `registres/t07-etape-b-bis/code-bbis-v1.json`,
**`ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469`** ; elle porte `texte`, `commit`
(`ce47056455595bc52fad676c0e57ad9d8bef886d`), `fichiers` (103 chemins et leurs empreintes lues sur le disque), `entropie`,
`epreuve_niveau` (chemin, empreinte `641adeb5…`, taux des deux cellules, niveau retenu 0,99, coût) et `niveau_decisif` 0,99.
Commit **`26e4c89108ffe8f3ee3bd9e07cccdf6b0a2bec8c`**.

### (d) § 1.4, geste 4 : ligne `CODE-BBIS` — 12:57:44Z à 12:58:09Z

Relu juste avant, dans le texte scellé : ligne 222 (registre propre, format, huit clés, jamais le registre partagé), ligne 5
(commit, empreintes des fichiers et entropie cités par la ligne, avant toute exécution), ligne 93 (niveau inscrit avec la ligne,
coût écrit avec le résultat), ligne 116 (entropie de 128 bits tirée à l'inscription), ligne 194 (épreuve absente : pas de ligne).
Relevé du moment : aucune branche distante `donnees/t07-etape-b-bis*` (`git ls-remote --exit-code` rend 2) : aucune exécution.

Commande du plan, sans changement (`rg.sceau_conforme`, `rb.lire_fiche_code`, puis `rb.ajouter_ligne_propre`). Ligne inscrite :

```text
| CODE-BBIS | 2026-11-16T12:57:51Z | registres/t07-etape-b-bis/code-bbis-v1.json | ee362bb70c5051097dab90c7978eb550d192f8c90f313317812635884b04e469 |
```

Une seule ligne ajoutée, les deux lignes antérieures inchangées. Commit **`ff24998f871bd1c0ce00cae3fd3f774a2ddc231e`** ;
`$PY -m controle_ia.t07bbis.registre_bbis_v1 ancetre . HEAD` : « BBIS ANCETRE ce47056455595bc52fad676c0e57ad9d8bef886d de
ff24998f871bd1c0ce00cae3fd3f774a2ddc231e », code 0 (l'attendu du plan) ; poussée à 12:58:09Z (`e1caae01..ff24998f`, code 0).

### (e) § 3 : extrait et ligne `GO-BBIS` — 12:58:25Z à 12:59:04Z

Relu juste avant, dans le texte scellé : ligne 218 (« la ligne `GO-BBIS` du registre propre en recopie l'extrait »), ligne 195
(aucune création sans `GO-BBIS`, le feu écrit de la mère, `CODE-BBIS` et `SCELLEMENT-BBIS`), ligne 99 (ordre des lignes). Ligne
`GO-2026-11-14-09` de `registres/go.md` : une seule, type « calcul », 40 USD, échéance 2026-11-22, accordée par Lazar ; aucune
ligne de révocation qui la cite, ni sur la branche ni sur la tête de `main` du moment (`60eee4e5`).

```bash
test ! -e registres/go-extraits/GO-BBIS-v1.md && grep '^| GO-2026-11-14-09 ' registres/go.md > registres/go-extraits/GO-BBIS-v1.md
test "$(grep -c '' registres/go-extraits/GO-BBIS-v1.md)" = 1
PYTHONPATH=/home/user/controle-ia-travail/src /home/user/controle-ia-travail/.venv/bin/python -m controle_ia.scellement sceller registres/go-extraits/GO-BBIS-v1.md
```

Résultat : extrait d'une ligne, `registres/go-extraits/GO-BBIS-v1.md`,
**`33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62`**, l'empreinte attendue par le plan ; l'extrait est une
ligne exacte de `registres/go.md` (`rg.extrait_est_une_ligne_de`). Puis la commande du plan, sans changement (garde « strictement
après `CODE-BBIS` », puis `rb.ajouter_ligne_propre`). Ligne inscrite :

```text
| GO-BBIS | 2026-11-16T12:58:51Z | registres/go-extraits/GO-BBIS-v1.md | 33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62 |
```

`CODE-BBIS` (12:57:51Z) est strictement antérieure à `GO-BBIS` (12:58:51Z). Commit
**`31fa8ac6041faf76b66282e0346750b9aefd4790`** (12:59:01Z) ; poussée à 12:59:04Z (`ff24998f..31fa8ac6`, code 0) ; tête distante
relue : `31fa8ac6041faf76b66282e0346750b9aefd4790`.

### Contrôles finaux, en lecture seule — 12:59:31Z à 13:00:22Z

- `ancetre . HEAD` à la tête `31fa8ac6…` : « BBIS ANCETRE ce470564… de 31fa8ac6… ».
- Registre propre relu par `lecture_v2.lire_lignes` en mode propre (celui de l'instance) : quatre clés (`SCELLEMENT-BBIS`,
  `ABSENCE-B-BBIS`, `CODE-BBIS`, `GO-BBIS`), aucune clé inconnue, ordre tenu, les quatre fichiers cités à leur sceau ; fiche
  lisible (niveau 0,99, entropie de 128 bits) ; 103 empreintes de la fiche égales sur le disque ; épreuve citée à son sceau ;
  aucune clé de B bis dans le registre partagé. La garde `marche_v3.gardes_d_entree` elle-même n'a pas été appelée (elle exige
  la marque de l'instance, que l'exécutant ne pose pas).
- Chemins cités par le registre propre, relevés par la règle de l'amorce (lignes 177 à 181) : tous présents à la tête avec leur
  compagnon ; l'épreuve et l'entropie aussi.
- Registre propre après les deux lignes : `c7bcc49f2ca29027f18eebd68cac9da957a11d638ff9a9406c369c22fdacb108`.
- 13:00:22Z, dépôt distant : branche du code à `31fa8ac6…` ; `main` à `60eee4e551fa8b3adc67278cbb5b9b6b4988ae81` ; aucune
  branche `donnees/t07-etape-b-bis*` ; aucune branche `verdict/t07-etape-b*`.

## L'épreuve de niveau de la règle (a) en deux plis

Source de tous les chiffres : `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json`,
`641adeb57b8c271be60a89af2513805e591a63c7c0dde17883e4ace0d3f59cbf`. Données synthétiques seulement.

| cellule | jeux | lectures « au-dessus » | taux de fausse lecture | plus haute borne basse | aire médiane | quantile médian du plancher |
|---|---|---|---|---|---|---|
| `nul` (écart de classe 0) | 1 000 | 0 | **0,0** | −0,025331622314453205 | 0,49852294921874996 | 0,5248740234375 |
| `signal-commun` (écart de classe 0,5) | 1 000 | 0 | **0,0** | −0,017199705810546903 | 0,6326953125 | 0,6564606933593751 |

- Réglages : 1 000 jeux par cellule, 800 directions, 2 000 tirages, 64 tâches, dix actions par classe et par tâche, un
  processus ; niveau testé 0,99 ; seuil du taux 0,01 ; aucune cellule au-delà du seuil ; **niveau décisif retenu : 0,99** ;
  `complete` vrai ; clé de graine `bbis/epreuve-niveau`, entropie `208082752394230630219821407440340422345`.
- Coût : processeur seulement, 0 USD ; 1 541,0 secondes murales, 1 519,3 secondes de processus, quatre cœurs visibles ; soit
  environ 0,77 seconde par jeu à un fil (1 541,0 / 2 000).
- **Remarque au titre de R4 (résultat net)** : 0 lecture fausse sur 1 000 dans chaque cellule, là où une règle exactement au
  niveau nominal de 0,005 en donnerait 5 par cellule en moyenne (1 000 × 0,005) ; aucune borne basse n'approche zéro. La règle
  est donc très prudente dans cette épreuve, ce que sa forme laisse attendre (la sonde doit dépasser le quantile 0,95 de son
  plancher de plus que la marge du rééchantillonnage). L'épreuve ne dit rien de la puissance. Le cas positif de la règle (une
  sonde qui porte un signal que le plancher n'a pas) est tenu par l'essai du paquet
  `tests/test_t07bbis_plis_v1.py::test_regle_a_sain_au_dessus_et_artefact_plancher_au_meme_signal_non_au_dessus`, que
  l'exécutant n'a pas rejoué. Rien n'a été rejoué ni ajouté : à la mère de dire si un audit est voulu.

## Commits et poussées de la branche `prep/t07bbis-code-v1`

| commit | heure du commit (UTC) | objet | poussé |
|---|---|---|---|
| `77f8a2c2dd6730220f1f1e91488ef8368412bec5` | 12:27:47 | plan de course et liste des 103 empreintes, avec leurs compagnons | 12:29:07 |
| `f9bd9ba6e7af813207a3d9dd4c24ef280007bcaa` (**M_b**) | 12:28:41 | `main` (`377a2a0c`) reçue une fois | 12:29:07 |
| `e1caae013b30d47495d52c7c1e93d2ad6cf38ddb` | 12:29:40 | entropie de `CODE-BBIS` | 12:30:11 |
| `70a4a9a879ef4bb263ec94d9e4b1792cefd01682` | 12:57:04 | épreuve de niveau, complète | 12:58:09 |
| `26e4c89108ffe8f3ee3bd9e07cccdf6b0a2bec8c` | 12:57:27 | fiche de `CODE-BBIS` | 12:58:09 |
| `ff24998f871bd1c0ce00cae3fd3f774a2ddc231e` | 12:57:58 | ligne `CODE-BBIS` | 12:58:09 |
| `31fa8ac6041faf76b66282e0346750b9aefd4790` (**commit de la course**) | 12:59:01 | extrait et ligne `GO-BBIS` | 12:59:04 |

Ce rapport et son compagnon forment un huitième commit, posé après `31fa8ac6` : il n'ajoute que deux fichiers sous
`brouillons/`, hors des motifs d'extraction de l'amorce ; le registre propre et les 103 fichiers y sont les mêmes. Le commit que
la commande de création doit citer reste `31fa8ac6041faf76b66282e0346750b9aefd4790` (plan, § 1.3 : « la tête après la ligne
`GO-BBIS` ») ; l'arbre de travail, à la tête de la branche, sert de racine au lanceur sans autre geste (le lanceur reçoit le
commit en argument et relit le registre propre sur le disque).

## Écarts de forme déclarés (aucun écart de fond)

1. **Ordre de (0) et de (a)** : la consigne place le versement du plan avant le relevé, le plan l'inverse ; joué dans l'ordre
   de la consigne ; le relevé précède la fusion de 41 secondes.
2. **Valeur de `M0`** : celle qu'écrit le plan (`377a2a0c`), non la tête de `main` du moment (`16484e48`, six commits plus
   loin) ; le relevé passe sur les deux. La branche ne porte donc pas les commits de `main` postérieurs à `377a2a0c` (dont les
   lignes R-2972 à R-2976).
3. **Poussées** : `git push origin HEAD:prep/t07bbis-code-v1` (forme de la consigne) au lieu de
   `git push origin prep/t07bbis-code-v1` (forme du plan) ; même effet, la tête étant cette branche. Deux poussées de plus que
   le plan : après le commit de l'entropie, et après la ligne `CODE-BBIS` (consigne : pousser après chaque inscription).
4. **Commande de l'épreuve** : les quatre variables sont posées en tête de ligne, sans la commande `env` que le plan écrit et
   que la consigne interdit à l'exécutant ; mêmes variables, même effet. Journal écrit dans le bloc-notes de la session,
   `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/epreuve-bbis-v1.log`, au lieu
   de `/tmp/epreuve-bbis-v1.log` ; il ne contient que la ligne de résumé imprimée par le script (402 octets).
5. **Messages de commit** : le message du plan, suivi des deux lignes d'attribution de la session, comme tous les commits du
   dépôt ; option `-q` ajoutée. Le commit de l'épreuve porte le message du plan précédé de « T0.7 étape B bis : ».
6. **Scellement de l'extrait** : par la formule de la consigne (module `controle_ia.scellement` du dépôt principal, à la même
   empreinte `93beeb1c…` que celui de la branche).
7. **Attente de l'épreuve** : par des commandes qui attendent la fin du processus 1736 (`tail --pid`), sans rien lancer d'autre.

## Constats et réserves

- **Sous `diag/` et `docs/verdicts/`** : la fusion M_b a matérialisé dans l'arbre de travail les fichiers de `main` (par les
  noms : 2 chemins sous `diag/`, 24 sous `docs/verdicts/`, 0 sous `donnees/`) ; l'exécutant n'en a ouvert aucun. Deux accès
  mécaniques les ont traversés sans rien afficher : la garde des secrets (compte seulement) et le relevé par les noms.
- **Charge** : un seul processus lourd de l'exécutant (un cœur, priorité 19). À 12:52Z, la charge moyenne d'une minute a
  touché 3,04 : un autre processus (identifiant 10918, priorité 10, lancé vers 12:46Z) n'est pas de l'exécutant et n'a pas été
  touché.
- **Disque** : 0,9 Go libres à 12:25Z, 0,86 Go après la fusion, 7,4 Go à 13:00Z (libérés par une autre main).
- **Essais du paquet** (`tests/test_t07bbis_*.py`) : non rejoués (« utiles, non bloquants » au plan ; hors des gestes
  confiés) ; les 103 fichiers sont ceux de `ce470564`, et l'amorce les rejoue sur l'instance.
- **Réserves de méthode du plan** (§ 9, point 8) : inchangées ; la fusion, elle, est maintenant jouée.

## Ce qui reste, hors du périmètre de l'exécutant

1. Sur `main`, par la mère : la ligne R- qui consigne le relevé du geste (a), M_b, l'entropie (par son fichier), l'issue de
   l'épreuve, la fiche, `CODE-BBIS`, `GO-BBIS` et le commit de la course ; `registres/etat.md` (avec la mention de l'addendum).
2. Vérification de ces gestes par un lecteur neuf (R-2975) ; contre-lecture du plan et de la forme exacte de la commande (plan,
   § 7, ligne 5).
3. Avant la création (plan, § 4) : consigne K4 amendée (R-2975, point 4), `HF_TOKEN` (point 5), crédit du loueur d'au moins
   20 USD (point 7), feu écrit portant `GO-2026-11-14-09`, préavis à Lazar.
4. La branche ne reçoit plus `main` jusqu'à `VERDICT-BBIS` ; toutes les lignes de B bis s'y écrivent.

## Interdits tenus

Aucune machine, aucun appel au loueur ni à son interface, aucun appel payant ; rien ouvert ni écrit par l'exécutant sous
`diag/`, `donnees/`, `docs/verdicts/` ; aucune entrée de 7a ou de 7b ; aucune sortie de l'étape B ; aucune valeur de clé
affichée, ni `env`, ni `printenv`, ni `set` sans argument, ni `export -p` ; aucun `git fetch` ; aucune variable `GIT_DIR`,
`GIT_WORK_TREE` ou `GIT_INDEX_FILE` ; aucun `pytest` ; aucun clone ; aucun processus arrêté ; aucun dossier d'un autre agent
touché ; aucun identifiant de modèle dans les fichiers ; rien d'écrasé (R12) ; aucune commande refusée par une permission, par
le crochet de garde ou par le classifieur.
