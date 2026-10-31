# Réponse de conv-audit à la question 6 (l'apprentissage profond peut-il identifier à lui seul les paramètres qui créent la fertilité ?) — version 2

- Version 2, 31 octobre 2026, 01:25 à 02:10 heure UTC, sous-agent neuf Opus 5.5 (lignée conv-audit), auteur ni de la v1, ni des relectures, ni des fiches, ni de la synthèse. La v1 reste intacte ; erreurs dans `erratum-reponses-v1-v1.md`.
- Niveau méthode ; aucune décision. Statuts comme en réponse 1 v2. Les énoncés « vérifié sur PDF » viennent des fiches vérifiées (page citée), corrigées par leur erratum.
- Pièces intégrées (sha256sum) :
  - `question-6-identification-collisionneur-v1.md` — `14966d0d2ffdea9de94b924a6ad661b440eae1bb2db865b81fd0eb75e6d71b73`
  - `question-7-allumage-autocatalytique-v1.md` — `42f85fcc2fd41b5d6a7afb20db484e920d7792682c215a257663f7d7b9e5666c` (contexte)
  - `reponse-conv-audit-question-6-v1.md` — `afdb9f9dbf9ed8a837d20962eb815e4eea817454dc296440a743123769ef00bf`
  - `relecture-fable-reponse-6-v1.md` — `bedb1f4c674ef70264e5c3bd19036f2ef6f18da9c098797d24c7be8b5da6c26e`
  - `reponse-fable-independante-questions-6-7-v1.md` — `052a37e765afc6aaa8a14afcb3ac3803994046457b361542cff1dd3b067cd65e`
  - `docs/sources/pdf/identification-causale-v1/fiches-de-lecture-verifiees-v1.md` — `63db77700da4bccf2911d3184afda33c4374b7138ed91f2692bd7f0a363d1d79`
  - `docs/sources/pdf/identification-causale-v1/erratum-fiches-de-lecture-v1.md` — `fa7e1d96f40e197f3fd761afd84601ac060cddfc98ea95c2d8f34de85e4f703f`
  - synthèse v2 du collisionneur — `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86`
  - `registres/decisions.md`, lignes R-646, R-650.

## Réponse courte

**Dans les courses, la randomisation identifie, le réseau estime. Dans la littérature, un choc extérieur identifie, le réseau estime.** Le non supervisé ne crée pas l'identification : sans hypothèse ni information auxiliaire, le démêlage est impossible (Locatello 2019) ; avec une variable auxiliaire assez variable, il retrouve des **latentes** à permutation et transformation près (Khemakhem 2020) ; avec des **cibles d'intervention observées**, des variables causales minimales (CITRIS). Retrouver des latentes n'est pas identifier un **effet** : il faut encore un argument d'intervention.

## Ce qui change par rapport à la v1

| Constat | Sort | Correction |
|---|---|---|
| RL6-01 latentes et paramètres causaux confondus ; la réponse courte manque | accepté (majeur) | Trois niveaux séparés (section 1) ; réponse courte ci-dessus. |
| RL6-02 CITRIS rangé sous « ordre temporel » | accepté | Il exige les **cibles** d'intervention à chaque pas (fiche 4, p. 3) : utilisable dans nos courses, pas sur OpenAlex. |
| RL6-03 trois hypothèses dites « offertes » sont des hypothèses de mécanisme ; suffisance causale non nommée | accepté | Section 3 : ce qui est offert, ce qui ne l'est pas. |
| RL6-04 test d'intervention sans hors-support ni ligne de base | accepté | Intervention hors support, comparée à une ligne de base non identifiante. |
| RL6-05 banc à vérité plantée circulaire | accepté | Mondes qui violent chaque hypothèse une à une (section 4). |
| RL6-06 « Schölkopf 2021 identifie » | accepté | C'est une perspective sans théorème propre (fiche 5, p. 1) ; les décalages parcimonieux y sont posés comme **hypothèse** (p. 8, art. 619). |
| RL6-07 Hyvärinen et Morioka 2016 et 2017 sous un seul chapeau ; LiNGAM et PCMCI sans auteurs | accepté | 2016 : sources non stationnaires par segments ; 2017 : sources stationnaires à dépendance temporelle (SUPPOSÉ, de mémoire de la relecture) ; Shimizu et collègues 2006, Runge et collègues 2019 (SUPPOSÉ). |
| RL6-08 critère de mort non chiffré, score non invariant à la permutation | accepté | Ci-dessous ; recouvrement mesuré par coefficient de corrélation moyen après appariement, comme Khemakhem (fiche 3, p. 6–7). |
| RL6-09 protocole de détection de ce que le modèle apprend absent | accepté | Section 5. |
| Relecture 6 : « au moins 2k + 1 valeurs » de la variable auxiliaire | **contesté par la fiche** | Le théorème exige **nk + 1** points distincts (n latentes, k statistiques suffisantes par latente) (fiche 3, p. 5, hypothèse iv ; R-650). |

## 1. Trois objets que le mot « identifier » mélange

1. **Latentes** : retrouver, à permutation et transformation élément par élément près, les variables qui engendrent les données. C'est ce que disent les théorèmes de démêlage et d'analyse en composantes indépendantes non linéaire.
2. **Graphe** : la structure entre ces variables ; sur données d'observation, au mieux la classe d'équivalence de Markov, sous fidélité (fiche 5, p. 9, art. 620, note 7).
3. **Effet** : ce que changerait la fertilité si l'on modifiait un paramètre. C'est la question de Lazar. Il faut une randomisation, un choc extérieur, ou un ajustement sous un graphe supposé connu.

Distinction voisine (RL6-01) : les latentes sont des **variables** ; les « paramètres qui créent » sont des **effets** d'interventions sur ces variables. Les théorèmes cités portent sur les premières.

## 2. Ce que disent les théorèmes, hypothèses exactes

- **Locatello et collègues 2019** (fiche 2) : démêlage non supervisé « fondamentalement impossible » sans biais inductif **sur les modèles et sur les données** (théorème 1, p. 3) ; données indépendantes et identiquement distribuées, a priori factorisé. La graine et les hyperparamètres comptent plus que l'objectif (p. 5–6). Le papier lui-même recommande d'exploiter la **structure temporelle** (p. 8) : le théorème ne dit rien contre les méthodes qui exploitent une structure.
- **Khemakhem, Kingma, Monti, Hyvärinen 2020** (fiche 3) : identification si (a) la variable auxiliaire u est **observée** ; (b) **toutes** les latentes sont conditionnellement indépendantes sachant u, en famille exponentielle ; (c) u prend **nk + 1** valeurs avec variations linéairement indépendantes (p. 5) ; (d) mélange injectif ; (e) observations **continues** (le corrigendum retire les observations discrètes, p. 9). Résultat à transformation linéaire près, réduite à une permutation sous les théorèmes 2 et 3 (p. 6) ; contre-cas si seule la moyenne varie (proposition 1, p. 6). Asymptotique.
- **Lippe et collègues 2022, CITRIS** (fiche 4) : processus markovien d'ordre un, stationnaire, **sans effet instantané** (p. 2) ; observation bijective ; **cibles d'intervention observées** à chaque pas (p. 3). Identifie la « variable causale minimale » (p. 4) ; deux facteurs jamais intervenus séparément ne sont pas identifiables (proposition 3.1, p. 3) ; une cause jamais intervenue finit dans le groupe résiduel, non identifiée (fiche 4, portée).
- **Schölkopf et collègues 2021** (fiche 5) : cadre ; apprendre des relations causales « exige fréquemment » plusieurs environnements ou la capacité d'intervenir (p. 4, art. 615).
- **Reisach, Seiler, Weichwald 2021** (fiche 1) : les bancs simulés sont souvent triables par la variance ; la standardisation **ne suffit pas** à effacer l'artefact (p. 9) ; sur un jeu réel, triabilité proche du hasard (p. 9).

## 3. Ce que nos données offrent, et ce qu'elles n'offrent pas

| Hypothèse | Offerte ? | Pourquoi |
|---|---|---|
| Ordre temporel des citations | oui, mais achète peu | Exclut la causalité inverse, pas la confusion cachée (prestige, financement, mode) ; la suffisance causale est violée par construction sur des citations. |
| Multiplicité des environnements (sous-domaine, décennie, pays) | la multiplicité oui, l'usage non | L'environnement agit directement sur la fertilité mesurée (inflation des citations) ; les latentes causales sont dépendantes, contre l'hypothèse (b) de Khemakhem. |
| Décalages parcimonieux de mécanismes | non | Hypothèse sur le processus générateur (Schölkopf, p. 8, art. 619). |
| Bruit non gaussien | en partie | LiNGAM exige aussi linéarité, acyclicité, aucun confondeur caché. |
| Observations continues | non pour les comptes | Comptes de citations : hors du cadre de Khemakhem après corrigendum (SUPPOSÉ quant à l'effet, fiche 3). |
| Affectations randomisées, dose contrôlée (nos courses) | **oui, et connues** | Là seulement les hypothèses d'intervention sont vraies ; CITRIS s'y applique ; mais la « fertilité » y est définie par nos juges. |
| Choc extérieur (expériences naturelles) | oui, avec hypothèses écrites | Les quatre expériences lues identifient par décès inattendu, effondrement politique, ouragan, guerre, plus non-anticipation, tendances parallèles, absence d'interférence (fiches 6 à 9 ; lecture transversale). |

Signes publiés, utiles comme vérités de contrôle (fiches, avec erratum) : retirer un nœud ou un contact baisse la production (Azoulay −0,086 ; Campos −0,0241 ≈ −16 % ; Iaria −85 % de références hors du camp) ; un afflux la baisse chez les producteurs en place (Borjas −0,133 article par an à recouvrement complet).

## 4. L'épreuve qui tranche

- **Mondes inventés** à latentes connues, certaines causes de la fertilité, d'autres seulement corrélées par sélection (réponse Fable indépendante 6-7). Trois bras : non supervisé seul ; non supervisé avec environnements ; non supervisé avec affectations randomisées.
- **Anti-circularité** : des mondes qui **violent** chaque hypothèse une à une (confondeur caché, décalage dense, latentes dépendantes, bruit gaussien, comptes discrets) pour mesurer la dégradation (RL6-05 ; règles R4, R8).
- **Métriques** : recouvrement par coefficient de corrélation moyen après affectation (invariant à la permutation, comme Khemakhem, p. 6–7) ; **et surtout** erreur sur l'effet d'une intervention **hors support**, contre une ligne de base supervisée non identifiante (RL6-04). Graines : bien plus que deux (Locatello en utilise 50 par configuration, fiche 2, p. 4).
- **Littérature réelle** : prédire, avec des latentes apprises avant la coupure, le signe d'une intervention naturelle postérieure ; transport écrit d'avance (réponse 5 v2, section 3).

## 5. Détecter ce que le modèle apprend en pratique

Régresser chaque latente apprise sur taille, âge, prestige, langue, régime disciplinaire de citation ; rapporter la part de variance expliquée ; stabilité entre graines par appariement ; test de triabilité par la variance et par la croissance des corrélations le long de l'ordre (fiche 1, énoncé 9) ; test de permutation des étiquettes de domaine ; deux fenêtres temporelles disjointes (relecture 6 ; Fable 6, section c).

## Convergences et divergences avec la réponse Fable indépendante 6-7

- **Convergent** : trois objets (estimer, identifier une représentation, identifier un effet) ; le non supervisé est un **amplificateur** d'une information d'identification exogène, il ne la crée pas ; biais de sélection (on n'observe que les croisements tentés, publiés, cités) ; épreuve jugée sur l'effet d'une intervention jamais vue.
- **Divergent** : Fable écrit « au moins 2k + 1 valeurs de u pour k latentes, selon la version » ; la fiche, page lue, dit **nk + 1** (p. 5). Fable cite Lachapelle et collègues 2022 et Zheng, Ng, Zhang 2022 pour la parcimonie des mécanismes (titres vus) ; non vérifiés ici.
- **Collisionneur** : accord « l'apprentissage profond estime sous identification donnée » (T3-A c) ; C fond identification et transport (T2-A), corrigé en 4a / 4b (T3-C).

## Antériorités

| Auteur, année | Support | Statut |
|---|---|---|
| Locatello et collègues 2019 | ICML, arXiv 1811.12359v4 | **vérifié sur PDF** (fiche 2) |
| Khemakhem, Kingma, Monti, Hyvärinen 2020 | AISTATS, arXiv 1907.04809v4 | **vérifié sur PDF** (fiche 3) |
| Lippe et collègues 2022 (CITRIS) | ICML, arXiv 2202.03169v3 | **vérifié sur PDF** (fiche 4) |
| Schölkopf et collègues 2021 | *Proceedings of the IEEE* | **vérifié sur PDF** (fiche 5) |
| Reisach, Seiler, Weichwald 2021 | NeurIPS, arXiv 2102.13647v3 | **vérifié sur PDF** (fiche 1) |
| Azoulay et collègues (2009) ; Borjas et Doran 2012 ; Campos et collègues 2018 ; Iaria et collègues 2018 | documents de travail ; revues | **vérifié sur PDF** (fiches 6 à 9, erratum) |
| Hyvärinen et Pajunen 1999 | *Neural Networks* | rappelé par Locatello (fiche 2, p. 2) ; original non lu |
| Hyvärinen et Morioka 2016, 2017 ; Hyvärinen, Sasaki, Turner 2019 ; Perry, von Kügelgen, Schölkopf 2022 | conférences | SUPPOSÉ |
| Shimizu et collègues 2006 ; Runge et collègues 2019 ; Peters, Bühlmann, Meinshausen 2016 | revues | SUPPOSÉ ; notice pour Peters |
| Lachapelle et collègues 2022 ; Zheng, Ng, Zhang 2022 | conférences | notice seulement (titres vus par Fable) |
| Chernozhukov et collègues 2018 ; Wager et Athey 2018 | revues | notice ; SUPPOSÉ |
| Boudreau et collègues 2017 | revue | notice seulement |

## Critère de mort chiffré

Seuils **proposés, à geler** (propositions de la réponse Fable indépendante 6-7 et de la relecture 6, non opposables). Les mesures E1′, E2′, E6′ de la synthèse ne sont pas des tests d'identification ; E2′ reste préalable à toute « transition » estimée.

1. **Non supervisé seul** : mort si, sur mondes inventés, l'erreur sur l'effet d'une intervention hors support n'est pas meilleure qu'une ligne de base prédisant l'effet moyen, dans 3 mondes sur 3, l'intervalle bootstrap à 95 % recouvrant la ligne de base.
2. **Non supervisé avec environnements** : mort si le recouvrement des latentes causales vraies est inférieur à 0,5 alors que celui des latentes de nuisance dépasse 0,8 (le modèle a appris taille et prestige) ; et si le recouvrement s'effondre dès qu'une hypothèse du théorème est violée (mondes de la section 4).
3. **Non supervisé avec affectations randomisées** : le réseau n'apporte rien si son effet de dose diffère de plus d'un facteur 2 de la simple différence de moyennes entre bras randomisés.
4. **Sur données réelles** : « estime, n'identifie pas » si l'erreur sur l'effet d'une intervention hors support n'est pas inférieure à celle d'une ligne de base supervisée d'au moins une marge gelée d'avance (relecture 6, section e).

## Ce qui reste ouvert

- Aucun des neuf PDF ne traite PCMCI ni la prédiction invariante (R-650) : ces voies restent au statut SUPPOSÉ.
- Effets instantanés créés par l'agrégation annuelle des citations : probable violation de l'hypothèse de CITRIS (SUPPOSÉ, fiche 4).
- Les causes candidates (contact réel, lecture, conversation) ne sont pas dans OpenAlex ; aucun théorème ne récupère une variable absente des données.
- La « R²-triabilité » de 2023 reste SUPPOSÉE (fiche 1).
