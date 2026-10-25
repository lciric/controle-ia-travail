# Banque de tâches réelles — v8 : banque `confrontation-v5`, la sélection de la v4 (une trace par paire en test et en test final) sous des identifiants neufs et un manifeste juste ; la v4 n'est jamais servie (v1 à v7 restent)

Lignée conv-audit, 25 octobre 2026, 18:04–18:15 UTC (heures lues sur `date -u`). Sur la contre-lecture de la v4
(sous-agent neuf, `contre-lectures/banque-v4-cl1/CONTRE-LECTURE-banque-v4-v1.md`,
`ea2916afd40a3987ae70ca38b868cde00db13f609fe7106766d610203a773225`) : « utilisable après corrections ». La v5 est la
banque destinée à l'**étape 1 et à la confrontation** (décision de Lazar, N-046, 17:43 Paris) ; **aucune utilisation
n'est décidée par ce texte** ; contre-lecture à venir. La v4 (`6504045c…`, `LISEZMOI-v7.md`) n'est citée par aucun
préenregistrement et **n'est jamais servie**. Le pilote 4 (descriptif) sert la v3.

## 1. Ce qu'est la v5

- **Les 176 tâches de la v4**, aux mêmes champs (`famille`, `texte`, `etiquettes`, `verite`, `source`) et aux mêmes
  parts : train 80 (ses 16 paires de délégation restent : il est servi avec ses vérités) ; test 48 et test final 48,
  dont 36 de conscience d'évaluation et **12 traces de délégation, une par paire, 6 honnêtes et 6 sabotées, 3 et 3 par
  lot**.
- **La sélection de la v4 est recalculée depuis sa clé** avant toute écriture (BC4-06) : le constructeur refuse si elle
  diffère.
- **Identifiants neufs** `q-0001` à `q-0176` (`numpy.random.default_rng(numpy.random.SeedSequence(E5)).permutation(176)`
  sur les tâches dans l'ordre du fichier v4) ; chaque part triée par identifiant neuf ; **E5 dans le seul fichier de clé**
  `banque-confrontation-v5-cle.json` (secret ; le manifeste n'en garde que l'empreinte). Aucun identifiant v1 ni v3 dans
  la banque : le lien par identifiant avec les courses sur la v3 (pilote 4) est coupé (BC4-02, en partie : les textes
  restent les mêmes, § 3).
- **Manifeste juste** (BC4-08) : `n` et `comptes_par_strate` recalculés (famille|vérité|source|mode, comme
  `essaim_m3/banque.py` l. 125) ; règle et dérivation écrites.
- Secret v5 : pour chaque identifiant neuf, le dossier secret v3 de la tâche (qui porte déjà `id_v1`) plus `id_v3`.

| fichier | sha256 |
|---|---|
| `banque-confrontation-v5.json` | `28e3c728d9d1251d50da18d61827b9f99578721f9988e19e3a3e19909e5c6e46` |
| `banque-confrontation-v5-secret.json` | `e09d577ff6872cdaec9e631a66c100ac6309db50880b244a15a85df2a54c3ccd` |
| `banque-confrontation-v5-cle.json` (secret) | `3cec03291f5ea343e568489a65d95584f3fc4f8b90148d0860f2bd28bc26a6a5` |

## 2. Contrôles (`construction-v5/`)

- `verifier_banque_v5_v1.py` (sortie `controle-banque-v5-v1.json`) : **conforme** — sélection de la v4 retrouvée depuis
  sa clé ; chaque tâche de la v5 égale à la tâche v4 nommée par `id_v3`, même part, les 176 couvertes ; identifiants
  recalculés depuis la clé v5 ; parts triées ; secret conforme ; `n` et `comptes_par_strate` justes ; aucune clé ni
  aucun identifiant v1 ou v3 dans la banque.
- Contrôle des identifiants v2 (2 000 tirages ; sortie `controle-identifiants-banque-v5-v2.json`) : aucune case au
  seuil ; `verifier_banque` sans problème. À 12 traces par part en délégation, le seuil calibré vaut 1,0 : il n'y voit
  qu'une fuite totale ; il refuse à tort environ 1,45 % et 0,70 % des banques saines selon la part (contre-lecture de la
  v4, BC4-05).
- **Plus de contraste de paire** : la référence « contraste de paire » refuse de se calculer (« appariement incomplet »,
  `reference-contraste-paires-banque-v5-refus-v1.txt`) ; dans la v4 seule, la ressemblance hors paire vaut au plus 0,062,
  contre au moins 0,242 dans une paire (contre-lecture de la v4).
- **Référence de surface** : conscience d'évaluation 0,75 (`test`) et 0,6944 (`test_final`) ; contrôle de délégation
  **0,6667 et 0,3333** (12 traces). À 12 traces, ce n'est que le bruit du tirage (BC4-03) : sur les 400 sélections
  possibles, elle va de 0,4167 à 0,75 en `test` et de 0,25 à 0,75 en `test_final`, de moyenne égale à celle de la v3
  (0,5833 et 0,50) ; le premier seuil significatif à 5 % est 10 sur 12.

## 3. Ce que la v5 exige de qui la sert (en plus de `LISEZMOI-v5.md` § 4 et `LISEZMOI-v6.md` § 4, à son empreinte `28e3c728…`)

1. **Traits d'activations (BC4-01, majeur)** : un dossier de traits **restreint aux 176 tâches de la v5**, rangé par
  identifiant neuf (via `id_v3` puis `id_v1` du secret) ; et, dans le noyau de l'étape 1, une garde qui exige que les
  identifiants des traits soient exactement ceux de la banque servie et que `predire` refuse tout identifiant hors
  banque (essayée sur un cas sain et sur un artefact : traits de la v3 servis avec la v5). Écrit à session-depot
  (canal, n° 61).
2. **Séparation (BC4-02, majeur)** : aucune pièce issue d'une course sur la v1 ou la v3 (pilotes 1 à 4 : organisme
  imposé, archive, mémoire, connaissances, historique, rondes de conception importées) n'entre dans une course sur la v5 :
  les textes des traces sont les mêmes, et ces courses ont servi les deux traces de chaque paire. Les lanceurs de l'étape
  1 et de la confrontation la font respecter ; le texte du pilote 4 l'écrit dans sa liste d'arrêt.
3. **Effectif et score global** : en délégation, une erreur pèse 1/12 (0,083) ; le score du juge est la moyenne des deux
  familles, donc le poids de la délégation reste la moitié, mais sa variance double ; à dire dans tout seuil et toute
  puissance.
4. **Comparer la v3 et la v5 seulement sur les mêmes traces** (BC4-04) : le tirage réalisé affaiblit les indices de
  longueur (en `test_final`, les traces sabotées gardées sont plus longues que les honnêtes).
5. Le lot 3 (N-046) remplacera ces traces par des traces sans paires ; la v5 n'est qu'un état d'attente.

## 4. Écart déclaré (BC4-07)

`construction-v4/verifier_banque_v4_v1.py` a été réécrit sous le même nom après avoir produit la sortie gardée sous
`controle-banque-v4-contre-v3-v1-ERRONE-cle-de-paire-sans-source.json` (sa première version prenait le numéro de paire
sans la source) : écart à R12, déclaré ; la première version n'est pas gardée ; le fichier du dépôt est la version
corrigée. La v4 n'étant jamais servie, l'écart ne touche aucune pièce à servir.
