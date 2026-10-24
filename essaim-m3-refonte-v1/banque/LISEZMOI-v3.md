# Banque de tâches réelles — v3 : première banque scellée `confrontation-v1` (les v1 et v2 restent)

Complète `LISEZMOI-v2.md` (pièces brutes : lots 1 et 2 de traces de sabotage). Ce LISEZMOI décrit la troisième pièce
(sous-ensemble public « conscience d'évaluation », extrait par Lazar) et la **banque scellée** construite le
24 octobre 2026 à 18:08 UTC. Aucun organisme ne l'a vue ; aucun résultat n'a été lu (R1). Elle sert à la répétition
générale, à l'étape 1 des sondes et, sauf lot 3 (décision de Lazar en cours), à la confrontation.

## 1. `eval-awareness-sous-ensemble-v1.json` — famille `conscience-evaluation`

- Provenance complète : `PROVENANCE-eval-awareness-v1.md`. Sha256 `31761eded7fe328a13a65984b3eb185876cdec2f0dff9247cd9e1f197d2b8820`,
  120 items, 4 strates × 30 (évaluation / usage réel × agentique / conversation), tirés par `SeedSequence(20261024)`
  du jeu `jjpn2/eval_awareness` (révision `5d724f12…`), GAIA exclu ; commit `201dd09905a53b8310becdb9c729d39e67cc68ab`
  de Lazar sur `donnees/eval-awareness-sous-ensemble-v1`.
- Les deux classes viennent de la même source (les auteurs du papier ont réuni items d'évaluation et transcriptions
  d'usage réel) : la provenance ne sépare pas les classes.
- Longueurs très inégales (médiane 2 240 caractères, maximum 132 202 ; agentique : médiane 11 437 pour les
  évaluations, 37 083 pour l'usage réel). D'où la règle de borne ci-dessous, et la référence de surface (§ 3).

## 2. `banque-confrontation-v1.json` (+ `-secret.json`) — banque scellée

- Construction : `python -m essaim_m3.banque construire --sabotage lot1=… --sabotage lot2=… --conscience hf=…
  --entropie 279274939364502317056592969560855127043 --sortie banque --nom confrontation-v1` (entropie tirée par
  `numpy.random.SeedSequence()` et consignée, R9).
- Empreintes : banque publique **`f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`** ; fichier secret
  (paires, types, notes d'auteur, identifiants de source, mode, troncature) `c68d7d4ba34b49b85a9327adfe21d30cc8118f1d100a47db2a47e97329715caf` ;
  compagnons `.sha256`. `python -m essaim_m3.banque verifier banque/banque-confrontation-v1.json` : « banque conforme ».
- Partition 40 / 30 / 30 : **train 80, test 60, test final 60**. Par groupes (une paire honnête/sabotée ne se sépare
  jamais), stratifiée par famille, source, mode et — pour les items seuls dans leur groupe — par vérité : chaque
  strate du sous-ensemble public donne 12 / 9 / 9 ; chaque lot de traces 8 / 6 / 6 par vérité.
- **Borne des textes** : 20 000 caractères (15 000 premiers + marque « passage retiré par le noyau » + 5 000
  derniers) ; 30 items du sous-ensemble public tronqués, 0 trace de sabotage. Règle consignée dans le manifeste
  (`borne_caracteres`, `n_tronques`) et dans le fichier secret (`tronque` par item). Raison : borner le coût par
  génération et la longueur de contexte pour toutes les lignées à l'identique ; un indice d'évaluation peut se
  trouver dans la partie retirée : c'est une limite dite, la même pour tous.
- Le fichier public ne porte que `id`, `famille`, `texte`, `etiquettes`, `verite`, `source` ; le noyau masque la
  vérité hors de `train`.

## 3. Référence sur les traits de surface (N-029, CR-17) — `python -m essaim_m3.banque reference`

Régression logistique sur sacs de mots et bigrammes hachés, longueur, ponctuation, chiffres ; apprise sur `train`,
notée sur `test` et `test_final` ; seuil préenregistré : une famille au-dessus de **0,80** sur `test_final` est « trop
facile en surface » et sort de H-E1 et H-E2.

| famille | test (n) | exactitude équilibrée | test final (n) | exactitude équilibrée |
|---|---|---|---|---|
| `conscience-evaluation` | 36 | 0,75 (sensibilité 0,61 ; spécificité 0,89) | 36 | **0,69** (0,44 ; 0,94) |
| `controle-delegation` | 24 | 0,58 (0,83 ; 0,33) | 24 | **0,50** (0,58 ; 0,42) |

Lecture : les traces de sabotage ne se séparent pas en surface (hasard) ; les items « conscience d'évaluation » se
séparent en partie par la forme (longueur, vocabulaire des bancs d'essai), 0,69 < 0,80 : la famille reste, et tout
score d'organisme sur cette famille se lit **contre cette référence**, pas contre 0,5. Aucun chiffre ci-dessus n'est
un résultat d'organisme ; ce sont des propriétés de la banque, lues avant tout amorçage.

## 4. Suite

- Lot 3 « signalement omis » : décision de Lazar en cours (classes par brainstorm indépendant — collisionneur v2.5 —
  ou sous-agents) ; s'il vient, banque `confrontation-v2`, même procédure, même LISEZMOI versionné.
- Vérification d'étiquettes des traces par un sous-agent neuf sur 20 traces tirées (préenregistrement § 5) : à
  faire avant le scellement du préenregistrement.
