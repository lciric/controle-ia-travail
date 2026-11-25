---
title: "Mesurer si un système multi-agents trouve des idées étroites et profondes : attelage du Plan Turing"
subtitle: "Note de sortie du collisionneur (accord budgétaire GO-2026-11-24-39, dossier complet)"
lang: fr
---

**Statut protocolaire : lancé en version 1 du Protocole X ; note rendue en version 2 / 2.1 (règles 1 en 2.1, 3, 4, 6, 7 appliquées ; écarts 2 et 5 déclarés : pas de questions témoins et pas de bras témoin/rejeu sur cette course lancée avant v2).**

**Dossier.** `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153` (branche `claude/relaxed-gauss-p2t1wk`, révision `831a7e38`) ; accord budgétaire de la course (`GO-2026-11-24-39`, plafond de 25 dollars américains payés au pire cas, ligne comptée ouverte à 40 dollars américains) ; question neutre soumise au test de neutralité préalable (`docs/notes/attelage-plan-turing-v1/collisionneur-attelage-v1/question-neutre-attelage-v2.md`, empreinte `f00e1678031eab4f…`, 414 mots).

**Rédacteur neuf et transparence de lignée.** Cette note est rédigée par un rédacteur neuf de classe C (document de travail, modèle Gemini 4 Neon), en reprise après l'atteinte du quota hebdomadaire de Claude Opus 5.5 sur la session fille des collisionneurs (passation `2026-11-24-1951-fille-collisionneurs-01Qi7Gr4.md`). **Le rédacteur est du même modèle que la lettre E (`gemini-4-neon`)** : les propositions de E sont traitées exactement comme celles des quatre autres modèles, sans poids supplémentaire. La sélection primaire s'appuie sur les deux lecteurs aveugles indépendants qui ont lu le dossier avant toute révélation des noms : un lecteur Claude Opus 5.5 neuf (`lecture-opus-v1.md`) et un lecteur GPT-6.2 Astra neuf (`lecture-astra-v1.md`), tous deux externes à la famille Google. Aucune pièce de course de sabotage, de score, de verdict ou de coffre n'a été ouverte.

**Programme de contrôle déterministe.** Tous les chiffres d'alignement, le kappa de Cohen, les comptes par fournisseur, les vérifications d'empreintes, le relevé des statuts « vérifié », le rejeu arithmétique de 46 calculs et le décompte exact des coûts sont produits par le script déterministe `analyser_attelage_v1.py` (empreinte `57ac07c9b66135c9…`) et enregistrés dans `metriques-attelage-v1.json` (empreinte `a7c371707a1a79c9…`).

---

## 1. Conventions de lecture et révélation des lettres

- Chaque renvoi désigne une cellule précise : **[B2]** signifie « la lettre B au tour III.2 ». Les trois tours sont : tour III.1 (conception à l'aveugle, sans voir les autres), tour III.2 (critique croisée des quatre autres), tour III.3 (réponse aux critiques reçues et conception révisée).
- La note distingue strictement trois natures d'énoncé :
  - **argument** : un raisonnement de méthode sans chiffre établi ;
  - **calcul** : une identité mathématique ou une arithmétique refaisable sur des paramètres hypothétiques ;
  - **mesure** : une observation issue d'une exécution réelle. **Le dossier ne contient aucune mesure.** Aucune expérience n'a encore été exécutée ; tous les seuils, effectifs, débits et budgets cités par les modèles sont illustratifs.
- **Révélation des lettres** (vérifiée dans `especes.json`, empreinte `7b99c4b1f9df3571…`) et **regroupement par fournisseur** (règle 6 du Protocole X version 2 : une voix par fournisseur, sauf indépendance démontrée par l'audit) :

| Lettre | Modèle servi | Fournisseur (règle 6 : 1 voix par fournisseur) | Réglage principal |
|---|---|---|---|
| A | Claude Fable 5.2 (`claude-fable-5-2`) | Anthropic (A + B = 1 voix) | Effort élevé, plafond 49 000 jetons |
| B | Claude Opus 5.5 (`claude-opus-5-5`) | Anthropic (A + B = 1 voix) | Effort élevé, plafond 64 000 jetons |
| C | GPT-6.2 Astra (`gpt-6.2-astra`) | OpenAI (C = 1 voix) | Plafond 8 000 jetons |
| D | Gemini 4 Carbon (`gemini-4-carbon`) | Google (D + E = 1 voix) | Arrière-plan, niveau élevé, plafond 65 536 jetons |
| E | Gemini 4 Neon (`gemini-4-neon`) | Google (D + E = 1 voix) | Arrière-plan, niveau très élevé, plafond 65 536 jetons |

- **Écarts déclarés par rapport au Protocole X version 2 / 2.1 :** cette course ayant été lancée le 24 novembre 2026 à 18 h 18 (temps universel) sous la version 1, les règles 2 (questions témoins à réponse connue et score de Brier) et 5 (bras témoin à question reformulée et rejeu à l'identique) ne pouvaient pas être appliquées sans relancer la course. Conformément à la clause de transition du Protocole X version 2, **toutes les propositions issues de ce dossier portent la marque « lancé en version 1 »**.

---

## 2. La question servie et son contrôle de neutralité

Une équipe prévoit un système où plusieurs agents fondés sur des modèles de langage proposent, critiquent et sélectionnent des idées scientifiques candidates (hypothèses, lois quantitatives, lemmes, protocoles). Avant d'engager des courses coûteuses, elle souhaite bâtir et valider un harnais de mesure (l'attelage du Plan Turing) permettant d'établir ou de réfuter que le système trouve des idées « étroites et profondes » : rarement atteintes par une recherche ordinaire, mais de grande conséquence une fois trouvées. Les lignes de base candidates incluent le tirage aléatoire dans le même espace, un énumérateur mécanique et le modèle unique le plus fort au même budget, d'autres pouvant être proposées.

La question (`question-etage3.md`, 414 mots en anglais) comporte huit points : (1) définition opérationnelle de la cible sans juge de langage, ou bornage de son biais ; (2) comparaison des sources de vérité terrain ; (3) quantité primaire, unité d'analyse, comptabilité des coûts, règle de décision et attribution causale ; (4) choix des problèmes ou régions favorables et test de ce choix ; (5) rétroaction autorisée ou retenue durant la recherche ; (6) validation préalable du harnais ; (7) plan expérimental ordonné du moins cher au plus cher avec critères d'arrêt et tailles d'échantillon ; (8) limites, cas où aucun harnais n'est faisable ou où la cible est mal posée.

**Constat sur les pièces servies.** Le fichier des faits (`faits.md`) est **strictement identique bit pour bit** au fichier de la question (`question-etage3.md`, même empreinte `f00e1678031eab4f…`). Aucun résultat empirique, aucun chiffre de programme et aucune pièce contextuelle interne n'ont été servis. La question a passé un contrôle de neutralité préalable (`test-neutralite-v1-sortie.md`, empreinte `a3c5edd76502e23f…`), qui a validé les quatre critères après six retouches textuelles : orientation (0,70), divulgation (0,70), complétude (0,90) et non-exclusion de rivaux (0,65).

---

## 3. En bref : ce que le collisionneur tranche pour toi, Lazar

- **Le cadrage « étroit et profond » est révisé en profondeur sur un point majeur (unanimité : 5 modèles sur 5, 3 fournisseurs sur 3).** « Étroit » n'est pas une propriété intrinsèque d'une idée : c'est une propriété relative à une politique de recherche de référence nommée, à un codage et à un budget. Surtout, le tour de critique croisée a mis au jour une **borne de handicap** (`[B2]`, acceptée par tous au tour III.3) : si la même politique sert à définir l'étroitesse et à concourir comme ligne de base au même budget, elle est mathématiquement plafonnée par construction. Le remède exige soit un panel métrologique disjoint des bras concurrents, soit un budget de sonde très inférieur au budget du duel, et dans tous les cas un bras de contrôle dit « divergence triviale » (`CN-1`).
- **Onze principes métrologiques font l'objet d'un accord complet des deux lecteurs aveugles** (`U01` à `U11`), presque tous soutenus par les trois fournisseurs (3 voix sur 3) au dernier tour : panel de référence disjoint ou découplé, certification d'étroitesse par borne binomiale unilatérale sur tirages disjoints, nomination scellée choisie avant l'ouverture du coffre, profondeur mesurée par gain d'un résolveur mécanique figé contre résolveur nu sur buts gelés, audit bilatéral de la canonicalisation (fausses fusions et fausses scissions), comparaison principale par test d'intersection-union dimensionné contre une marge utile non nulle, attribution par témoins multiples sur viviers gelés et lots frais, séparation stricte entre utilité du retour et intégrité du coffre (étroitesse jamais renvoyée), plafond de fausses alertes calibré par l'identité de Bayes strate par strate avec exclusion du juge de langage de la mesure primaire, contrôle positif sur micromonde à quatre quadrants incluant une seconde loi utile non documentée, et test du choix des régions comme rendement net sur familles neuves.
- **L'erreur commune la plus instructive du tour III.1 a été prise en flagrant délit par la critique croisée.** Quatre modèles sur cinq (`A`, `B`, `D`, `E`) ont dimensionné leur duel principal contre un effet nul alors que leur propre règle de décision exigeait de dépasser une marge non nulle (puissance réelle tombant entre 0,09 et 0,53 au lieu de 0,80). Seul `C` (Astra) avait dimensionné contre l'excès au seuil dès le premier tour ; les quatre autres ont reconnu l'erreur et multiplié leurs effectifs par deux à quatre au dernier tour.
- **Le poste de coût dominant n'est pas le duel multi-agents, mais l'étalonnage de l'étroitesse sous modèle de langage** (de plusieurs centaines à plusieurs dizaines de milliers d'euros ou dollars illustratifs selon les modèles). La conséquence pratique pour le programme est nette : toutes les épreuves qui peuvent réfuter l'instrument ou le cadrage (arithmétique du compromis handicap/certification, micromonde exhaustif sur processeur, audit bilatéral du canoniseur, puis test de dépendance à la référence et au codage) doivent passer **avant** toute campagne d'étalonnage lourde.
- **Huit désaccords entre les deux lecteurs aveugles te remontent tels quels** (section 5 et section 8), donnant un kappa de Cohen de **0,4833** sur les 31 unités canoniques alignées (et **0,8800** sur les 18 unités explicitement listées dans les deux lectures). Les points qui demandent une décision nommée de ta part concernent surtout : (i) le choix entre panel métrologique disjoint et budget de sonde court, (ii) l'adoption ou non de la clé partielle extensionnelle proposée par Astra (`C`), (iii) la place d'une mesure par compression de longueur de description minimale à côté du résolveur mécanique, et (iv) l'inscription de la graine de tirage proposée pour la règle `1 c` du Protocole X version 2.1.

---

## 4. Ce que chaque modèle propose au dernier tour

Les résumés ci-dessous retracent la trajectoire complète de chaque espèce du tour III.1 au tour III.3, les critiques qu'elle a acceptées ou rejetées, sa confiance révisée et l'expérience qu'elle place en premier.

### Claude Fable 5.2 (lettre A — Anthropic)

- **Position initiale (`[A1]`) :** Harnais en mondes clos engendrés par grammaire typée, plan planté deux fois deux, étroitesse par borne « règle de trois » (`3/K`) sur exécutions disjointes, profondeur par gain d'un solveur mécanique figé, duel principal par test de McNemar sur 150 mondes, choix des régions par « déceptivité », transport vers Lean 4. Discipline de statut stricte : aucune mention « vérifié » posée sur ses propres énoncés.
- **Révisions majeures au tour III.3 (`[A3]`) :** Accepte la borne de handicap (`[B2]`) comme son défaut le plus grave ; adopte le compromis explicite entre certification et handicap (paramètres `K`, rapport de budget `m`), l'étiquette binaire censurée au lieu de la corrélation de rang, l'exclusion totale du juge de langage (taux de fausses découvertes supérieur à 91 % à prévalence de 1 %), la révision du duel principal par test d'intersection-union avec 600 mondes illustratifs (au lieu de 150), l'égalisation en coût matériel mesuré, l'ajout des bras de divergence triviale (`CN-1`) et chasseur d'étroitesse (`CN-2`), trois témoins pour l'attribution (critique hors problème, message neutre intra-problème, silence à budget réalloué), la refonte du test de retour en fonction du couplage public/privé, et la suppression de la fuite dans son prédicteur de régions (qui devient exploratoire).
- **Confiances révisées (`[A3]`) :** cible 0,50 ; sources 0,65 ; comparaison 0,60 ; choix de problèmes 0,25 ; retour 0,55 ; validation 0,75 ; plan 0,50 ; limites 0,55.
- **Première expérience proposée (`[A3]`) :** (1) Arithmétique à coût nul du compromis entre handicap et puissance de certification ; (2) reproduction de la profondeur sur processeur entre deux jeux de conséquences et deux solveurs indépendants (`E1'`).

### Claude Opus 5.5 (lettre B — Anthropic)

- **Position initiale (`[B1]`) :** Thèse selon laquelle l'étroitesse dépend du triplet idée, chercheur de référence et canonicalisation ; profondeur par gain contrefactuel d'un solveur mécanique moins un contrôle de complexité appariée ; plan en huit expériences incluant un test de contamination sur modèles à données ouvertes (`OLMo`, `Pythia`) et un duel séquentiel sur 118 problèmes contre l'enveloppe des lignes de base.
- **Apport majeur au tour III.2 (`[B2]`) :** Formalise trois outils repris par les quatre autres modèles au dernier tour : la **borne de handicap**, le bras de contrôle **divergence triviale (`CN-1`)** et le bras **chasseur d'étroitesse (`CN-2`)**.
- **Révisions majeures au tour III.3 (`[B3]`) :** Abandonne l'enveloppe par problème, l'estimateur `pass@k`, les zones mortes dans ses hypothèses, les quotients non bornés en attribution, et la redéfinition de la profondeur conditionnellement à l'étroitesse ; fixe un nombre fixe `k` de nominations scellées ; établit trois identités explicites : facteur d'environ 37 sur la rareté effective pour certifier à sensibilité 0,80 (`I1`), taux de fausses alertes cible d'environ 0,002 et 1 500 négatifs par strate (`I2`), et 270 problèmes illustratifs pour trois contrastes en intersection-union (`I3`) ; remplace le contrôle de profondeur par une double comparaison (résolveur nu et idée vraie inerte) pour éviter le principe d'explosion logique d'une prémisse fausse ; reformule le test de contamination par injection randomisée de paires jumelles (`E7'`).
- **Confiances révisées (`[B3]`) :** 0,70 sur l'efficacité des corrections ; 0,40 sur la jugeabilité du duel à 270 problèmes ; 0,50 sur l'issue défavorable au cadrage sans référence nommée (`E2'`).
- **Première expérience proposée (`[B3]`) :** Audit bilatéral de la canonicalisation (`E0'`, processeur), immédiatement suivi du test de dépendance de l'étroitesse aux références (`E2'`, environ 50 heures de processeur graphique), car c'est l'épreuve la moins chère capable de réfuter le cadrage lui-même.

### GPT-6.2 Astra (lettre C — OpenAI)

- **Position initiale (`[C1]`) :** Approche centrée sur l'étalonnage du détecteur avant toute comparaison de chercheurs : micromondes finis, identité par égalité extensionnelle sur tout le domaine, maximum des probabilités de référence borné par Clopper-Pearson, profondeur contre règle vraie placebo, règle de décision commune exhaustive (`T > 0` contre `T <= 0`), nomination unique, calcul bayésien des fausses alertes (0,00090 et 3 330 négatifs par strate), et seul modèle à dimensionner dès le tour III.1 contre l'excès au seuil (`g = 0,05`, environ 500 paires) et à chiffrer explicitement l'explosion du coût de référence (62 500 euros illustratifs contre 840 euros pour la comparaison).
- **Révisions majeures au tour III.3 (`[C3]`) :** Renonce à mesurer dans un même score une loi et un algorithme rapide, et renonce à extrapoler d'un petit monde à un grand monde ; remplace l'égalité extensionnelle totale (qui écrasait les classes vraies en une seule) par une **clé d'assertion partielle à portée déclarée** transmise au résolveur par une interface canonique commune ; sépare « atteint dans le journal horodaté » et « livré avant ouverture du coffre » ; fait du résolveur nu le comparateur principal de profondeur (le placebo devenant diagnostic) ; ajoute l'audit probabiliste des sorties réelles avec analyse de sensibilité aux deux extrêmes pour les cas non résolus ; porte son dimensionnement illustratif à 935 paires après allocation du risque unilatéral à 0,005 ; corrige le statut « vérifié » posé à tort en T1 sur deux citations bibliographiques.
- **Confiances révisées (`[C3]`) :** cible 0,85 ; sources 0,85 ; comparaison 0,85 ; régions 0,65 ; retour 0,85 ; validation 0,90 ; plan 0,80 ; limites 0,90.
- **Première expérience proposée (`[C3]`) :** Micromonde fini sur processeur à deux lois utiles dont une seule est signalée au constructeur, plus une assertion vraie rare sur observable inutilisée, avec évaluation identique d'une table et d'une formule par la même interface.

### Gemini 4 Carbon (lettre D — Google)

- **Position initiale (`[D1]`) :** Formalisation en théorie algorithmique de l'information : quotient sémantique par graphes d'équivalence et grilles denses, étroitesse par borne de Clopper-Pearson (`M0 = 1 000`, seuil 5,5 nats), profondeur par gain de longueur de description minimale tronqué à zéro par régime (`D_MDL`) et réduction de pas en Lean 4, test d'intersection-union, sélecteur de régions sur résidus, cloisonnement avec mécanisme `Thresholdout`, correction de prévalence de Rogan-Gladen. Marque cependant massivement ses choix de conception et affirmations d'ingénierie du statut « vérifié » (43 occurrences au tour III.1).
- **Révisions majeures au tour III.3 (`[D3]`) :** Supprime la troncature par régime au profit d'une **somme signée intensive** par observation avec veto de réfutation pire régime et constantes strictement figées sur l'apprentissage ; porte `M0` à 4 000 tirages courts (`b0 = B/64`) sur une enveloppe de trois politiques de référence (autorisant jusqu'à 7 occurrences sous 5,5 nats, exact par code) ; remplace l'empreinte de dépendances Lean par la double implication prouvée mécaniquement et ajoute le test de Schwartz hors grille ; ajoute des traductions non conservatrices de taille dans l'épreuve de stabilité (`Exp. I`, statistique kappa de Cohen sur 240 classes) ; remplace Rogan-Gladen par les valeurs prédictives de Begg et Greenes et un plan factoriel deux fois deux pour un juge éventuel ; porte l'effectif confirmatoire à 220 problèmes contre une marge de 0,05 ; intègre `CN-1`, `CN-2`, un test direct de `Thresholdout` et le contrôle de systèmes chaotiques incompressibles ; réduit partiellement ses gonflements de statut mais en conserve encore plusieurs au tour III.3.
- **Confiances révisées (`[D3]`) :** cible 0,82 ; sources 0,85 ; comparaison 0,85 ; choix de problèmes 0,55 ; retour 0,90 ; validation 0,88 ; plan 0,80 ; limites 0,92.
- **Première expérience proposée (`[D3]`) :** Porte adversariale du quotient sémantique (400 paires : paraphrases hors règles et jumeaux divergents hors grille), suivie de l'épreuve de stabilité inter-formalismes à tailles non conservées (`Exp. I`, environ 140 dollars américains illustratifs).

### Gemini 4 Neon (lettre E — Google)

- **Position initiale (`[E1]`) :** Enveloppe de références, profondeur par gain hors distribution pénalisé, compression de preuves Lean 4 ou gain d'information attendu, quantité primaire égale au maximum sur tout le vivier agrégé en aire sous la courbe découverte-budget, correction de juge par inférence assistée par prédiction, taxonomie de régions sur quatre familles, plan en six expériences (budget illustratif initial de 5 700 dollars américains).
- **Révisions majeures au tour III.3 (`[E3]`) :** Retire le maximum sur tout le vivier, l'aire sous la courbe découverte-budget, le temps médian censuré et les seuils en écarts-types estimés ; adopte une nomination scellée unique, une quantité primaire binaire absolue, la règle de réfutation exhaustive empruntée à C, la certification par Clopper-Pearson sur 800 tirages courts (`b_ref = B/20`), un panel de référence secret pour tester les fuites, un taux de fausses alertes maximal de 0,002 (2 000 négatifs), la scission du duel en deux régimes budgétaires (coût financier égal contre appels d'oracle égaux), 16 familles pour la taxonomie (exclues du duel) avec test de transfert d'échelle (8 vers 70 milliards de paramètres), l'exécution des ablations d'attribution sur un lot d'instances entièrement indépendant, et la relégation du juge assisté au module optionnel `E2b` sous condition de corrélation et d'oracle objectif. Budget révisé illustratif : 16 200 dollars américains (2 700 avant le duel principal).
- **Confiances révisées :** non retabulées point par point au tour III.3 (les confiances du tour III.1 allaient de 0,30 sur les hypothèses verbales à 0,85 sur les sources, la comparaison, le retour, la validation et les limites).
- **Première expérience proposée (`[E3]`) :** Métrologie complète sur vérités plantées sans juge (`E1`, 100 positifs, 2 000 négatifs, `CN-2`, bras volume, essai témoin complet, environ 250 dollars américains illustratifs), suivie immédiatement du test d'invariance au recodage isomorphe (`E2a`, environ 250 dollars américains illustratifs).

---

## 5. Lecture double à l'aveugle : alignement et kappa de Cohen (règle 3)

Les deux lecteurs neufs — Claude Opus 5.5 (`lecture-opus-v1.md`, 15 propositions retenues et 10 non retenues) et GPT-6.2 Astra (`lecture-astra-v1.md`, 14 propositions retenues et 8 non retenues) — ont lu uniquement le dossier anonymisé (`dossier-aveugle-v1.md`, empreinte `e1e3db6095f28482…` pour son compagnon), sans connaître les noms des modèles ni la liste de l'autre lecteur.

### Mesure d'accord calculée par programme (`analyser_attelage_v1.py`)

En alignant de façon transparente l'union des propositions distinctes examinées par au moins l'un des deux lecteurs, on obtient **31 unités canoniques** (`U01` à `U31`) :

| Décision du lecteur Opus \ Décision du lecteur Astra | Astra : Retenue (OUI) | Astra : Non retenue (NON) | Total Opus |
|---|---:|---:|---:|
| **Opus : Retenue (OUI)** | **11** | **4** | 15 |
| **Opus : Non retenue (NON)** | **4** | **12** | 16 |
| **Total Astra** | 15 | 16 | **31** |

- **Accord observé :** `23 / 31 = 0,7419` (74,2 %).
- **Accord attendu au hasard :** `0,5005` (50,1 %).
- **Kappa de Cohen (grille principale à 31 unités) :** **`0,4833`** (erreur type approchée `0,1573` ; intervalle de confiance à 95 % approché `[0,1749 ; 0,7917]` ; indice ajusté à la prévalence et au biais `0,4839`).

Pour éviter qu'un choix de découpage des propositions composites ne gonfle ou ne réduise artificiellement le kappa, le programme calcule deux analyses de sensibilité :

| Grille d'alignement | Effectif (`N`) | Table (OUI/OUI, OUI/NON, NON/OUI, NON/NON) | Accord observé | Kappa de Cohen | Intervalle à 95 % approché |
|---|---:|---|---:|---:|---|
| **Grille principale** (toutes les unités canoniques distinctes) | 31 | (11, 4, 4, 12) | 0,7419 | **0,4833** | [0,1749 ; 0,7917] |
| **Sensibilité 1** (unités explicitement nommées en retenue ou non retenue par les deux lecteurs) | 18 | (11, 0, 1, 6) | 0,9444 | **0,8800** | [0,6514 ; 1,0000] |
| **Sensibilité 2** (recoupement large rattachant `U13` et `U15` à la proposition `P5` d'Astra) | 31 | (13, 2, 4, 12) | 0,8065 | **0,6141** | [0,3368 ; 0,8914] |

**Lecture de ce résultat.** L'écart entre le kappa principal (`0,4833`) et le kappa sur le noyau explicitement nommé des deux côtés (`0,8800`) est très instructif : **les deux lecteurs ne se contredisent frontalement que sur une seule proposition** (`U16`, la clé partielle extensionnelle de `C` au tour III.3, explicitement écartée par Opus en `N7` et explicitement retenue par Astra en `P2`). Les sept autres écarts (`U12`, `U13`, `U14`, `U15`, `U17`, `U18`, `U19`) viennent de ce qu'un lecteur a élevé en proposition autonome un volet que l'autre a laissé implicite, absorbé dans une épreuve ou jugé secondaire. Par ailleurs, la lecture d'Astra comporte une anomalie mineure de datation : ses échéances vont du 31 août au 20 décembre 2026 (antérieures à la date du 24 novembre 2026), signe que le lecteur aveugle n'avait pas la date du jour dans son dossier ; la table d'épreuves de la section 9 recale toutes les échéances à partir de décembre 2026.

### Table complète d'alignement des 31 unités et comptes par fournisseur (règle 6)

| Unité | Intitulé synthétique | Opus | Astra | Accord lecteurs | Compte brut (tour III.3) | Compte par fournisseur (règle 6) |
|---|---|---|---|---|---|---|
| `U01` | Panel de référence nommé et disjoint des concurrents (ou budget de sonde découplé) | P1 (OUI) | P5 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U02` | Étroitesse certifiée par borne binomiale unilatérale sur tirages disjoints, coût calculé avant tirage | P2 (OUI) | P1 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U03` | Nomination scellée avant ouverture du coffre, séparation atteint/livré et bras volume | P3 (OUI) | P8 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U04` | Profondeur par gain d'un résolveur mécanique figé contre résolveur nu sur buts gelés | P4 (OUI) | P4 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U05` | Audit bilatéral de la canonicalisation (fausses fusions et fausses scissions hors règles) | P6 (OUI) | P2 partiel (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U06` | Comparaison principale par intersection-union appariée par monde contre marge utile non nulle | P7 (OUI) | P10 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U07` | Attribution par témoins multiples sur viviers gelés et lots frais (neutre, silence réalloué, hétérogénéité) | P9 (OUI) | P13 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U08` | Séparation utilité du retour / intégrité du coffre (trois jeux, fuite délibérée, étroitesse secrète) | P10 (OUI) | P11 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U09` | Fausses alertes calibrées par prévalence (Bayes) par strate ; aucun juge de langage dans le primaire | P11+P12 (OUI) | P7 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U10` | Contrôle positif sur micromonde 4 quadrants à deux lois utiles dont une non documentée + leurre vrai rare | P13 (OUI) | P3 (OUI) | Accord OUI | 3/5 (`A,B,C`) | **2/3** (Anthropic, OpenAI) |
| `U11` | Choix des régions testé comme rendement net sur familles neuves, descripteurs publics, coût imputé | P15 (OUI) | P12 (OUI) | Accord OUI | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U12` | Score de compression par longueur de description minimale signé et intensif, constantes figées | P5 (OUI) | Absent (NON) | Désaccord (Opus seul) | 2/5 (`D,E`) | **1/3** (Google seul) |
| `U13` | Contrôle négatif actif chasseur d'étroitesse (`CN-2`) en complément du bras divergent (`CN-1`) | P8 (OUI) | Absent (NON) | Désaccord (Opus seul) | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U14` | Module optionnel de juge hors primaire : plan factoriel 2×2 et correction assistée sur oracle objectif | P12 opt. (OUI) | Absent (NON) | Désaccord (Opus seul) | 2/5 (`D,E`) | **1/3** (Google seul) |
| `U15` | Épreuve dédiée de dépendance au codage (traductions non conservatrices de taille) et aux références | P14 (OUI) | Partiel (NON) | Désaccord (Opus seul) | 4/5 (`A,B,D,E`) | **2/3** (Anthropic, Google) |
| `U16` | Clé partielle extensionnelle `(observable, portée déclarée, vecteur de réponses)` via interface commune | N7 (NON) | P2 (OUI) | **Désaccord frontal** | 1/5 (`C`) | **1/3** (OpenAI seul) |
| `U17` | Étalonnage complet de la décision en essais témoins (A/A) rejouant toute la chaîne + injection en sortie finale | Absent (NON) | P6 (OUI) | Désaccord (Astra seul) | 3/5 (`A,B,E`) | **2/3** (Anthropic, Google) |
| `U18` | Concurrents réalisables gelés sur développement, comptabilité matérielle complète et double régime budgétaire | Absent (NON) | P9 (OUI) | Désaccord (Astra seul) | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U19` | Réplication dans un second domaine (preuve formelle Lean 4) sans promettre le transfert | Absent (NON) | P14 (OUI) | Désaccord (Astra seul) | 5/5 (`A,B,C,D,E`) | **3/3** (Anthropic, OpenAI, Google) |
| `U20`–`U31` | Douze propositions écartées par les deux lecteurs (enveloppe par problème `N1/N3`, maximum sur tout le vivier `N2/N2`, compression tronquée `N3/N4`, corrélation de rang sur valeurs censurées `N4/N5`, sélecteurs circulaires `N5`, critique hors sujet unique témoin `N6/N6`, égalité extensionnelle totale `N7`, égalisation simultanée des budgets `N8`, borne par style ou experts seuls `N9/N8`, arrêt sur petit pilote non concluant `N10`, rareté infinie ponctuelle `N1`, rétrodiction comme arbitre du rappel `N7`) | NON | NON | Accord NON (12/12) | 0/5 au tour III.3 | **0/3** |

---

## 6. Accords, désaccords majeurs, ce qui est neuf et ce qui est fragile

### Accords renforcés par la critique croisée (3 fournisseurs sur 3)

La règle 6 évite de surestimer un accord dû aux deux modèles d'Anthropic (`A` et `B`) ou aux deux modèles de Google (`D` et `E`). Dix des onze propositions retenues par les deux lecteurs atteignent **3 fournisseurs sur 3** (`U01` à `U09`, `U11`), tout comme `U13`, `U18` et `U19` :

1. **Borne de handicap et nécessité de découpler la référence du duel (`U01`, 5/5, 3/3).** Aucun modèle ne conteste la démonstration de `[B2]`.
2. **Certification binomiale unilatérale sur tirages disjoints (`U02`, 5/5, 3/3).** Tous abandonnent les estimateurs ponctuels qui explosent à zéro occurrence.
3. **Nomination scellée avant ouverture du coffre (`U03`, 5/5, 3/3).** Tous reconnaissent que prendre le maximum sur tout le vivier transforme le coffre privé en sélecteur gratuit et récompense le volume.
4. **Profondeur sans juge de langage, contre résolveur nu et sur buts gelés (`U04`, 5/5, 3/3).** Un placebo vrai ne sert qu'à détecter un ralentissement, jamais à fabriquer un gain.
5. **Audit bilatéral de la canonicalisation (`U05`, 5/5, 3/3).** Fausses fusions et fausses scissions mesurées toutes deux, y compris sur des paraphrases produites hors des règles du canoniseur.
6. **Intersection-union et dimensionnement contre la marge utile (`U06`, 5/5, 3/3).** L'enveloppe problème par problème est abandonnée à l'unanimité ; tous dimensionnent contre la différence entre gain visé et marge minimale.
7. **Attribution par témoins multiples (`U07`, 5/5, 3/3) et étanchéité du retour (`U08`, 5/5, 3/3).** La critique hors problème ne suffit jamais seule ; l'étroitesse reste strictement secrète durant toute recherche.
8. **Plafond de fausses alertes calibré par la prévalence et primaire sans juge de langage (`U09`, 5/5, 3/3).** À 1 % de prévalence, un taux de fausses alertes de 5 % produit environ 86 % de fausses découvertes.
9. **Choix des régions traité comme rendement net sur familles neuves (`U11`, 5/5, 3/3).** Coût de prospection imputé, descripteurs publics seuls.

### Désaccords majeurs qui subsistent après le tour III.3

- **Remède à la borne de handicap (`U01`) :** `B` et `C` (Anthropic + OpenAI) préfèrent un **panel métrologique strictement disjoint** des bras concurrents ; `A`, `D` et `E` (Anthropic + Google) optent pour un **budget de sonde court** (`B/10`, `B/20` ou `B/64`) combiné à un panel multi-familles et au bras de divergence triviale (`CN-1`). Les deux options se comparent par calcul et petite simulation avant tout appel coûteux.
- **Clé partielle extensionnelle contre canonicalisation symbolique (`U16` vs `U05`) :** `C` (OpenAI, 1 fournisseur sur 3) propose de définir l'idée par `(observable cible, portée autorisée, vecteur de réponses)` et de livrer cette clé par une interface commune afin d'évacuer les différences de vitesse d'exécution. `D` et `A` (Google + Anthropic) maintiennent une canonicalisation symbolique (graphes d'équivalence plus test hors grille) pour des lois continues où la table est infinie. Les deux lecteurs aveugles divergent directement sur ce point (`Opus N7` contre `Astra P2`).
- **Mesure de profondeur par compression (`U12`) :** soutenue uniquement par Google (`D` et `E`, 1 fournisseur sur 3), alors qu'Anthropic et OpenAI (`A`, `B`, `C`, 2 fournisseurs sur 3) préfèrent le gain direct d'un résolveur mécanique sur des buts aval gelés.
- **Module optionnel de juge de langage hors primaire (`U14`) :** défendu comme option conditionnelle par Google seul (`D` et `E`, 1 fournisseur sur 3) ; Anthropic (`A`, `B`) exclut tout juge et OpenAI (`C`) n'envisage hors langage qu'un audit humain aveugle avec ancres et bornes défavorables.
- **Nomination unique contre top-`k` fixe et journal horodaté (`U03`) :** `D` et `E` (Google) retiennent une nomination unique (`k = 1`), `A` et `B` (Anthropic) un nombre fixe `k` (par exemple 3), et `C` (OpenAI) maintient deux indicateurs distincts (« atteint dans le journal » en primaire si le journal est certifiable, « livré en rang 1 » en secondaire).
- **Effectifs et budgets illustratifs du duel principal :** ils varient d'un facteur près de six, de 160 problèmes par famille (`E`, 320 au total) et 220 (`D`) à 270 (`B`), 600 (`A`) et 935 (`C`). Cet écart ne reflète pas un conflit théorique mais le fait que la fréquence de discordance entre bras (`q`) et le risque unilatéral alloué restent inconnus avant un pilote.
- **Première expérience à financer :** `A` met en tête le calcul du compromis handicap/certification puis la reproduction de profondeur sur processeur ; `B` et `D` mettent l'audit du canoniseur puis la dépendance aux références et aux encodages ; `C` met le micromonde exhaustif à deux lois utiles dont une non documentée ; `E` met la métrologie complète des quatre quadrants puis le recodage.

### Ce qui est neuf (dans l'emploi) et ce qui est fragile

**Neuf dans l'assemblage (non cité comme méthode établie pour des systèmes d'idéation) :**
- La **borne de handicap** démontrant que l'étroitesse relative à un concurrent plafonne ce concurrent par construction (`[B2]`), et les deux contrôles actifs qui en découlent : le bras de **divergence triviale (`CN-1`)** et le **chasseur d'étroitesse (`CN-2`)** (`[B2]`, repris par tous en T3).
- L'exigence d'une **seconde loi profonde non documentée comme plantée** dans le micromonde de contrôle positif (`[A2]` sur `C`, repris par `[B3]` et `[C3]`) pour empêcher qu'un détecteur ne valide que la cible codée par son concepteur.
- Le **double panel de référence (exposé contre secret)** dans l'épreuve de fuite de rétroaction (`[A2]` sur `E`, repris par `[D3]` et `[E3]`), afin de détecter un contournement de la référence d'étroitesse par obscurcissement.
- La quantification explicite du **coût de sensibilité de la certification par zéro occurrence** : une classe doit être environ 37 fois plus rare que le seuil affiché pour être certifiée avec une probabilité de 0,80 sous correction multiple (`[B3]`, identité `I1`, vérifiée par code).
- La séparation systématique entre **atteinte dans le journal horodaté** et **livraison par nomination scellée** (`[A1]`, `[C3]`), ainsi que le traitement des **dossiers non résolus aux deux extrêmes** (`[C1]`, `[C3]`).

**Fragile :**
- **Aucune mesure réelle :** tout le dossier repose sur des calculs conditionnels et des hypothèses. La prévalence réelle d'idées étroites et profondes dans un domaine non trivial est totalement inconnue : si elle tombe sous 1 % à 2 %, le harnais devient statistiquement muet à budget réaliste.
- **Mur du coût d'étalonnage :** certifier l'étroitesse contre un modèle de langage exige des centaines à des milliers de tirages indépendants par problème et par politique (`[A1]`, `[C1]`, `[B3]`). Ce poste domine d'un facteur 10 à 70 le coût du duel lui-même.
- **Validité externe hors portée :** les cinq modèles (3 fournisseurs sur 3) conviennent qu'aucun harnais de ce type ne mesure l'invention d'une nouvelle ontologie (changement des observables ou de la grammaire) ni la portée scientifique à long terme.
- **Accords nés de la critique croisée :** l'unanimité sur `CN-1`, `CN-2`, le test d'intersection-union et les témoins d'attribution est apparue *après* le tour III.2 ; elle n'a pas été éprouvée par un tour supplémentaire ni par des mesures.
- **Biais potentiel de famille sur les statuts et les choix :** seul Google (`D` et `E`) pousse la compression par longueur de description minimale (`U12`) et le module juge optionnel (`U14`), et seul OpenAI (`C`) pousse la clé extensionnelle partielle (`U16`). La règle 6 rend cette concentration immédiatement visible.

---

## 7. Contrôles par programme avant la note (règle 4)

Tous les contrôles ci-dessous ont été exécutés par le script `analyser_attelage_v1.py` avant la rédaction de cette note.

### 7.1. Confrontation des mentions « VÉRIFIÉ » / « vérifié » aux faits servis

Le fichier `faits.md` étant identique au texte de la question (aucun fait empirique, aucun résultat d'expérience, aucune citation vérifiée sur document d'origine), seule une lecture directe des pièces ou une identité mathématique pure (sous les hypothèses explicitées) pouvait légitimement recevoir le statut « vérifié ».

| Modèle (lettre) | Occurrences `VÉRIFIÉ` (majuscules) : T1 / T2 / T3 (total) | Occurrences `vérifié` (toutes casses) | Occurrences `RAPPORTÉ` (majuscules) | Gonflements de statut relevés face à `faits.md` |
|---|---:|---:|---:|---|
| Fable 5.2 (`A`) | 1 / 3 / 3 (**7**) | 11 | 15 | **0** — déclare explicitement l'absence de tout fait vérifié ; ne reprend le mot que pour citer les statuts d'autrui. |
| Opus 5.5 (`B`) | 1 / 3 / 1 (**5**) | 7 | 8 | **0** — déclare l'absence de tout fait vérifié ; relève les abus chez `C` et `D`. |
| Astra (`C`) | 4 / 9 / 2 (**15**) | 15 | 4 | **1** — en `[C1]` (ligne 28), étiquette « vérifié » deux références bibliographiques non auditées sur document d'origine ; corrigé en « rapporté » en `[C3]`. |
| Carbon (`D`) | 43 / 32 / 28 (**103**) | 106 | 62 | **Au moins 10** — usage massif de `[VÉRIFIÉ]` sur des choix de conception, des conjectures empiriques (obscurcissement, graphes d'équivalence, grille dense, absence de dérive, bibliographie non vérifiée) ; partiellement corrigé en `[D3]`, mais des affirmations de faisabilité non prouvées empiriquement restent marquées `[VÉRIFIÉ]` (`[D3]`, lignes 114, 119, 123). |
| Neon (`E`) | 5 / 7 / 9 (**21**) | 23 | 62 | **2** — en `[E1]`, doubles étiquettes composites ambiguës (`VÉRIFIÉ/RAPPORTÉ`, lignes 55 et 64) et un « rapporté » sans source en `P1` ; discipline d'étiquette unique rétablie en `[E3]`. |

### 7.2. Rejeu arithmétique par code de 46 calculs chiffrés et taux d'erreur par modèle

Le programme a rejoué exactement **46 calculs chiffrés** extraits des quinze cellules et des deux lectures aveugles (bornes exactes de Clopper-Pearson par sommation binomiale, loi normale, valeur prédictive positive par Bayes, biais d'enveloppe, puissances statistiques, sommes budgétaires et conversions en heures de calcul). Les calculs non rejoués se limitent aux ordres de grandeur qualitatifs non accompagnés d'une formule fermée.

| Modèle / Lecteur | Calculs rejoués | Exacts | Erreurs de dimensionnement (T1, corrigées en T3) | Ambiguïtés résiduelles | Taux de défaut sur calculs rejoués |
|---|---:|---:|---:|---:|---:|
| Fable 5.2 (`A`) | 10 | 9 | 1 (`[A1]` : 140/150 mondes contre zéro au lieu de +5 points) | 0 | **10,0 %** (0 % au tour III.3) |
| Opus 5.5 (`B`) | 9 | 8 | 1 (`[B1]` : 118 problèmes contre zéro au lieu de +10 points) | 0 | **11,1 %** (0 % au tour III.3) |
| Astra (`C`) | 6 | 6 | 0 (seul modèle exact dès `[C1]`, y compris 62 500,00 euros au centime) | 0 | **0,0 %** |
| Carbon (`D`) | 8 | 7 | 1 (`[D1]` : 100 problèmes contre zéro au lieu de +10 points) | 0 | **12,5 %** (0 % au tour III.3) |
| Neon (`E`) | 11 | 9 | 1 (`[E1]` : 50–60 problèmes contre zéro au lieu de 0,20 écart-type) | 1 (`[E3]` : 2 000 négatifs « stratifiés ») | **18,2 %** (1 ambiguïté au tour III.3) |
| Lecteur Astra | 2 | 2 | 0 (`2,95 %` pour 0/100 et `14 %` de valeur prédictive) | 0 | **0,0 %** |
| **Total** | **46** | **41** | **4** | **1** | **10,9 %** |

**Constats notables issus du rejeu par code :**
- L'arithmétique interne des formules citées au tour III.2 et au tour III.3 est remarquablement solide chez les cinq modèles. En particulier, le calcul de `D` au tour III.3 selon lequel `M0 = 4 000` tirages au niveau corrigé `0,05 / 3` autorisent « jusqu'à 7 occurrences » sous le seuil de 5,5 nats (`p* = 0,004087`) est **exactement optimal** : la borne exacte de Clopper-Pearson vaut `0,003780 < 0,004087` pour 7 occurrences et passe à `0,004121 > 0,004087` dès 8 occurrences. De même, le facteur d'environ 37 de `B` (`36,70`), les 62 500 euros de `C` et les 935 paires de `C` (`934,3`) sont exacts.
- **Ambiguïté à lever chez `E` (`[E3]`, ligne 80) :** la borne à zéro alerte de `0,00184 < 0,002` (au risque unilatéral `0,025`) suppose **2 000 négatifs par strate** ; si les 2 000 négatifs étaient répartis sur trois strates (environ 667 par strate), la borne par strate monterait à `0,00552 > 0,002`.

### 7.3. Références bibliographiques à vérifier sur document d'origine (règle `R7`)

Le programme recense **50 références bibliographiques** citées dans le dossier (liste structurée complète dans `metriques-attelage-v1.json`). **Aucune n'a été vérifiée sur son document d'origine (fichier PDF) et aucune n'est tenue pour vraie.** Les modèles ayant respecté l'interdiction de citer des identifiants de prépublication de mémoire, plusieurs entrées devront être retrouvées et vérifiées page par page avant toute citation en note publiable :

| Référence telle que citée | Cellules / lecteurs | Usage dans le dossier | État (`R7`) |
|---|---|---|---|
| Clopper et Pearson (1934), *Biometrika* | `D1, C3, D3, E2, E3`, Opus, Astra | Bornes de confiance binomiales exactes | À vérifier sur document d'origine |
| Dwork et al. (2015), « The Reusable Holdout », *Science* | `A1, D1, E1, A3, D3, E2, E3`, Opus, Astra | Sur-ajustement adaptatif et mécanisme `Thresholdout` | À vérifier sur document d'origine |
| Platt (1964), « Strong Inference », *Science* | `A1, B1, D1, E1, D3`, Opus | Cadre des expériences décisives | À vérifier sur document d'origine |
| Berger (1982), *Technometrics* | `D1, D3, E2, E3`, Opus, Astra | Test d'intersection-union | À vérifier sur document d'origine |
| Angelopoulos et al. (2023), « Prediction-Powered Inference », *Science* | `E1, D2, E2, E3`, Opus | Inférence assistée par prédiction | À vérifier sur document d'origine |
| Begg et Greenes (1983), *Biometrics* | `A2, D3`, Opus, Astra | Biais de vérification sous audit stratifié par verdict | À vérifier sur document d'origine |
| Rogan et Gladen (1978), *American Journal of Epidemiology* | `D1, D3, E2`, Opus | Correction de prévalence pour un test imparfait | À vérifier sur document d'origine |
| Zheng et al. (2023), NeurIPS ; Panickssery, Bowman et Feng (2024), NeurIPS | `A1, B1, A3, B3`, Opus | Auto-préférence et biais des juges de langage | À vérifier sur document d'origine |
| Rissanen (1978), *Automatica* ; Grünwald (2007), MIT Press | `D1, E1, D3, E3`, Opus | Principe de longueur de description minimale | À vérifier sur document d'origine |
| Bennett (1988), Oxford University Press ; Shannon (1948) ; Solomonoff (1964) ; Li et Vitányi (2008) | `D1, E1, D3, E3` | Profondeur logique, entropie, dépendance au codage | À vérifier sur document d'origine |
| de Moura et al. (2015), CADE ; de Moura et Ullrich (2021), CADE 28 ; The mathlib Community (2020), CPP | `A1, B1, C1, D1, C3, D3`, Opus, Astra | Noyaux de preuve Lean / Lean 4 et bibliothèque Mathlib | À vérifier sur document d'origine |
| Pearl (2009), Cambridge University Press ; Popper (1959) | `D1, E1, D3` | Interventions causales et réfutabilité | À vérifier sur document d'origine |
| Udrescu et Tegmark (2020), *Science Advances* ; Cranmer (2023), PySR ; La Cava et al. (2021), SRBench ; Schmidt et Lipson (2009), *Science* | `A1, B1, D1, E1, D2, D3`, Opus | Lignes de base de régression symbolique mécanique | À vérifier sur document d'origine |
| Wolpert et Macready (1997), *IEEE Transactions on Evolutionary Computation* | `B1, E1, E3`, Opus | Théorèmes d'absence de domination universelle | À vérifier sur document d'origine |
| Newcombe (1998), *Statistics in Medicine* ; Fieller (1954), *JRSS B* ; O'Brien et Fleming (1979), *Biometrics* ; Hanley et Lippman-Hand (1983), *JAMA* | `A1, B1, D2, A3`, Opus, Astra | Intervalles appariés, rapports, plans séquentiels, règle de trois | À vérifier sur document d'origine |
| Rice (1953) ; Schwartz (1980) ; Kaplan et Meier (1958) ; Holm (1979) ; Benjamini et Hochberg (1995) ; Efron et Tibshirani (1993) ; Wald (1945) | `D1, E1, D2, D3`, Opus | Indécidabilité, test polynomial, survie, tests multiples, bootstrap | À vérifier sur document d'origine |
| Autres références citées par un ou deux modèles : Blum et Hardt (2015), Boden (1990), Campbell (1979), Chen et al. (2021), Golchin et Surdeanu (2024), Ioannidis (2005), Lehman et Stanley (2011), Manheim et Garrabrant (2018), Mouret et Clune (2015), Nosek et al. (2018), Romera-Paredes et al. (2024), Simmons et al. (2011), Uzzi et al. (2013), Wang et al. (2017) | Voir détail complet dans `metriques-attelage-v1.json` | Rétroaction adaptative, nouveauté, contamination, préenregistrement, bibliométrie | À vérifier sur document d'origine |

---

## 8. Propositions retenues et arbitrages sur les désaccords

Toutes les propositions ci-dessous portent la marque **« lancé en version 1 »**.

### 8.1. Socle retenu par accord des deux lecteurs aveugles (`U01` à `U11`)

1. **`U01` — Panel de référence nommé, disjoint des concurrents ou à budget de sonde découplé** (accord lecteurs OUI/OUI ; 5/5 modèles ; **3/3 fournisseurs**). Supprime la borne de handicap. *Point laissé à ton arbitrage :* panel strictement disjoint (`B`, `C`) ou budget court `B/20` à `B/64` (`A`, `D`, `E`), à éclairer par l'épreuve 1 de la section 9.
2. **`U02` — Étroitesse certifiée par borne supérieure binomiale unilatérale sur tirages disjoints et coût calculé avant tirage** (OUI/OUI ; 5/5 ; **3/3**). Remplace tout estimateur ponctuel et rend explicite le prix en sensibilité (facteur d'environ 37 sous correction multiple).
3. **`U03` — Nomination scellée avant ouverture du coffre, séparation atteint/livré et contrôle de volume** (OUI/OUI ; 5/5 ; **3/3**). Empêche le coffre privé de servir de sélecteur gratuit.
4. **`U04` — Profondeur par gain d'un résolveur mécanique figé contre résolveur nu sur buts gelés** (OUI/OUI ; 5/5 ; **3/3**). Seule mesure primaire totalement exempte de juge de langage, vérifiée sur deux jeux de buts, deux résolveurs et un témoin vrai mais inerte.
5. **`U05` — Audit bilatéral de la canonicalisation : fausses fusions et fausses scissions** (OUI/OUI ; 5/5 ; **3/3**). Inclut obligatoirement des obscurcissements engendrés hors des règles du canoniseur.
6. **`U06` — Comparaison principale par intersection-union appariée par monde contre une marge utile non nulle** (OUI/OUI ; 5/5 ; **3/3**). Élimine le biais de Jensen de l'enveloppe par problème et l'erreur de dimensionnement contre zéro.
7. **`U07` — Attribution par témoins multiples sur viviers gelés et lots frais** (OUI/OUI ; 5/5 ; **3/3**). Sépare critique active, message neutre intra-problème, silence à budget réalloué, sélecteur sur viviers gelés et hétérogénéité contre chaque famille homogène.
8. **`U08` — Séparation utilité du retour / intégrité du coffre, étroitesse strictement secrète** (OUI/OUI ; 5/5 ; **3/3**). Trois jeux (renvoyé, scellé, vierge), différence d'écarts et bras de fuite délibérée comme témoin de sensibilité.
9. **`U09` — Plafond de fausses alertes dérivé de la prévalence (identité de Bayes) strate par strate ; aucun juge de langage dans le primaire** (OUI/OUI ; 5/5 ; **3/3**). Inclut l'audit des acceptations et des rejets sur sorties réelles et le traitement des dossiers non résolus aux deux extrêmes (volet d'Astra `P7`).
10. **`U10` — Contrôle positif d'instrument sur micromonde à quatre quadrants avec seconde loi utile non documentée et assertion vraie rare sur observable inutilisée** (OUI/OUI ; 3/5 ; **2/3** : Anthropic, OpenAI). Rend le contrôle positif réellement réfutable.
11. **`U11` — Choix des régions testé comme rendement net exploratoire sur familles neuves** (OUI/OUI ; 5/5 ; **3/3**). Descripteurs calculés sur l'énoncé public seul et une sonde disjointe ; coût de prospection imputé ; familles de sélection exclues du duel.

### 8.2. Désaccords entre lecteurs aveugles remontés à Lazar (`U12` à `U19`)

Conformément à la règle 3 du Protocole X version 2, **les huit désaccords te remontent tels quels** :

- **Quatre propositions soutenues par au moins deux fournisseurs (recommandées pour intégration au plan d'épreuves de la section 9, sous réserve de ton accord) :**
  - **`U13` — Contrôle négatif actif chasseur d'étroitesse (`CN-2`)** (`Opus P8` OUI, `Astra` absent ; 5/5 modèles, **3/3 fournisseurs**). *Justification :* un quadrant statique rare-inerte ne remplace pas un chercheur actif qui évite délibérément la référence ; tous les modèles l'ont adopté au tour III.3.
  - **`U15` — Épreuve dédiée de dépendance de l'étroitesse au codage (traductions non conservatrices de taille)** (`Opus P14` OUI, `Astra` partiel ; 4/5 modèles, **2/3 fournisseurs**). *Justification :* épreuve la moins chère capable de réfuter le cadrage lui-même (« rarement atteint » sans référence ni codage nommés).
  - **`U17` — Étalonnage de la décision complète par essais témoins (A/A) rejouant calibration, sélection et analyse, plus injection en sortie finale** (`Opus` absent, `Astra P6` OUI ; 3/5 modèles, **2/3 fournisseurs**). *Justification :* vérifie la chaîne statistique complète avant tout duel coûteux.
  - **`U18` — Concurrents réalisables gelés sur développement, comptabilité matérielle complète et séparation des deux régimes budgétaires** (`Opus` absent, `Astra P9` OUI ; 5/5 modèles, **3/3 fournisseurs**). *Justification :* indispensable pour éviter qu'un plafond d'appels d'oracle ne bride l'énumérateur mécanique ou qu'un coût caché de préremplissage ne fausse le duel.

- **Quatre propositions laissées en attente de ton arbitrage explicite (ou conditionnelles à l'ouverture d'un second domaine) :**
  - **`U16` — Clé partielle extensionnelle `(observable, portée déclarée, vecteur de réponses)` via interface canonique** (`Opus N7` **NON**, `Astra P2` **OUI** ; 1/5 modèle `C`, **1/3 fournisseur** OpenAI). *Seul désaccord frontal.* À trancher entre un banc à domaines finis discrets (où la clé de `C` est très propre) et des lois continues (où `U05` s'impose). Elle figure parmi les candidates processeur de la règle `1 c`.
  - **`U12` — Score de compression par longueur de description minimale signé et intensif** (`Opus P5` OUI, `Astra` absent ; 2/5 modèles `D, E`, **1/3 fournisseur** Google). Utile uniquement si tu retiens un banc de lois quantitatives continues en plus du résolveur mécanique `U04`.
  - **`U14` — Module optionnel de juge de langage hors primaire (plan factoriel 2×2 et inférence assistée sur oracle objectif)** (`Opus P12` OUI, `Astra` absent ; 2/5 modèles `D, E`, **1/3 fournisseur** Google). Sans objet tant que le programme reste sur des bancs purement mécaniques ou formels.
  - **`U19` — Réplication en preuve formelle Lean 4 sans promettre le transfert** (`Opus` absent, `Astra P14` OUI ; 5/5 modèles, **3/3 fournisseurs**). Utile en phase ultérieure seulement, une fois passées les portes sur processeur et sur micromonde.

### 8.3. Propositions examinées et non retenues (`U20` à `U31`)

Les douze propositions suivantes sont écartées par les deux lecteurs aveugles et abandonnées par leurs auteurs au tour III.3 : l'enveloppe des lignes de base prise problème par problème (`U20`), le maximum de profondeur sur tout le vivier et les seuils en écarts-types (`U21`), la compression tronquée à zéro par régime (`U22`), l'étroitesse scalaire par corrélation de rang (`U23`), les sélecteurs de régions nourris par la vérité retenue ou les résidus de la référence (`U24`), la critique hors problème comme unique témoin (`U25`), l'égalité extensionnelle totale sur tout le domaine (`U26`), l'égalisation simultanée de toutes les composantes budgétaires (`U27`), le bornage d'un juge par accord de style seul ou par audit d'experts humains seuls (`U28`), l'arrêt du programme sur un petit pilote non concluant (`U29`), la rareté infinie ponctuelle après zéro occurrence (`U30`), et la rétrodiction temporelle comme arbitre du rappel contre la découverte (`U31`).

---

## 9. Table des épreuves décisives les moins chères (règle 1 en version 2.1)

**Rappel impératif des trois garde-fous du Protocole X version 2.1 (`GO-2026-11-24-45`) :**
- **Règle `1 a` (indépendance du critère de mort) :** aucun critère de mort chiffré n'est fixé par les lecteurs ni par le rédacteur de cette note. Pour chaque ligne ci-dessous, **le critère de mort final sera rédigé et scellé avant toute donnée par un concepteur distinct des lecteurs et des proposeurs** — Claude Fable 5.2, ou, tant que son quota reste gelé jusqu'au 2 décembre 2026, un Claude Opus 5.5 neuf (écart déclaré). Les épreuves décisives passent par un préenregistrement (règles `R1`, `R2`).
- **Règle `1 b` (témoin faux connu à tuer d'abord) :** avant de compter, chaque épreuve est jouée sur son témoin faux connu (et si possible un témoin vrai connu). Si le témoin faux survit, **l'épreuve est déclarée « épreuve morte »** : aucune issue n'est lue, l'arrêt est rapporté et il n'y a pas de repli.
- **Règle `1 c` (mesure de la sélection par lecture) :** une proposition non retenue (dont l'épreuve tient sur processeur) est tirée au sort par graine inscrite avant tirage et éprouvée comme les retenues (voir la sous-section 9.2).

### 9.1. Table des épreuves des propositions retenues (ordonnées du moins cher au plus cher)

Les dates sont calées à partir du 24 novembre 2026 et les coûts sont des ordres de grandeur illustratifs (non des devis engagés). Les onze lignes `U01` à `U11` sont issues de l'accord des deux lecteurs aveugles ; les quatre lignes `U13`, `U15`, `U17` et `U18` sont ajoutées sous réserve de ton arbitrage (section 8.2).

| ID | Proposition (marque : lancé en v1) | Ce que l'épreuve décisive la moins chère mesure | Coût estimé | Date au plus tard | Critère de mort (règle `1 a`) | Témoin faux connu à tuer d'abord (règle `1 b`) |
|---|---|---|---|---|---|---|
| `U01` | Panel de référence disjoint ou budget de sonde découplé | Calcul exact puis petite simulation sur processeur de la borne de handicap et de la puissance de certification pour les triplets `(K, rapport de budgets m, seuil)` envisagés | < 10 dollars américains (processeur, < 1 jour) | 4 déc. 2026 | À sceller par concepteur distinct avant données (existence d'au moins un réglage laissant un bras hors système au-dessus du plancher mesurable) | « Un bras identique à la politique de référence, rejoué au même budget que la référence, obtient un taux étroit-profond supérieur à la marge du duel. » |
| `U02` | Étroitesse certifiée par borne unilatérale sur tirages disjoints | Simulation sur processeur d'un panel de classes à probabilités connues : comparer l'étiquette « étroite » sur tirages disjoints contre tirages ayant produit les idées, et courbe de puissance près du seuil | < 10 dollars américains (processeur) | 8 déc. 2026 | À sceller par concepteur distinct avant données (excès de rareté sur tirages non disjoints et puissance au seuil) | « Estimer la rareté sur les mêmes tirages qui ont produit les idées retenues ne fabrique aucune rareté apparente » (et « 100 absences certifient `p < 1 %` à 95 % »). |
| `U03` | Nomination scellée avant coffre et séparation atteint/livré | Simulation sur processeur de viviers de tailles 10 à 1 000 à profondeur vraie identique notés par maximum sur vivier contre nomination scellée, plus rejeu sur 100 journaux à vérité exhaustive | < 15 dollars américains (processeur) | 8 déc. 2026 | À sceller par concepteur distinct avant données (pente avec la taille du vivier et séparation atteint contre livré) | « Le maximum de la profondeur estimée sur tout le vivier est invariant au nombre de candidats lorsque la profondeur vraie est constante. » |
| `U06` | Comparaison par intersection-union dimensionnée contre la marge | Simulation sur processeur d'un essai témoin multi-copies contre l'enveloppe par problème et de la puissance conjointe en intersection-union contre la marge non nulle | < 15 dollars américains (processeur) | 8 déc. 2026 | À sceller par concepteur distinct avant données (absence de biais en essai témoin et couverture nominale des intervalles) | « L'enveloppe des lignes de base prise problème par problème est sans biais sous égalité » et « un gain vrai de 3 points valide une marge de 5 points ». |
| `U11` | Rendement net du choix de régions (exploratoire) | Contrôle de code sur processeur : recalculer les descripteurs publics après permutation ou remplacement par du bruit de toutes les données privées (régimes retenus, buts aval) | Négligeable (processeur) | 8 déc. 2026 | À sceller par concepteur distinct avant données (invariance bit pour bit aux données privées, puis rendement net sur 16 familles neuves) | Le prédicteur de « déceptivité » (`[A1]`) utilisant la part d'idées inertes (qui dépend de la vérité retenue et doit varier sous permutation). |
| `U10` | Micromonde positif 4 quadrants à seconde loi utile non documentée | Micromonde fini exhaustif sur processeur avec 2 lois utiles (une seule signalée au constructeur) et 1 assertion vraie rare sur observable inutilisée ; classifieur limité au gabarit de forme | < 20 dollars américains (processeur) | 11 déc. 2026 | À sceller par concepteur distinct avant données (détection de la loi non documentée, rejet du leurre rare inerte, absence de reconnaissance de gabarit) | « Un détecteur qui ne crédite que la loi documentée comme plantée est valide » (et « la règle rare portant sur une variable inaccessible aux buts aval aide le solveur »). |
| `U05` | Audit bilatéral de la canonicalisation | Environ 2 000 paires (paraphrases mécaniques, obscurcissements produits par un modèle tiers hors règles, paires proches distinctes sur une entrée ou hors grille) : mesurer fausses fusions et fausses scissions séparément | < 30 dollars américains (processeur + 1–2 h processeur graphique) | 11 déc. 2026 | À sceller par concepteur distinct avant données (plafonds conjoints sur les deux sens d'erreur) | « Un canoniseur constant qui attribue la même classe à toute entrée est fidèle puisqu'il fusionne 100 % des paraphrases. » |
| `U04` | Profondeur par résolveur mécanique figé contre résolveur nu | Micromonde sur processeur (40 petits mondes) : gain contre résolveur nu et contre idée vraie inerte, puis reproduction sur un second jeu de buts gelés et un second résolveur, à rareté fixée | 20–60 dollars américains (processeur) | 15 déc. 2026 | À sceller par concepteur distinct avant données (reproductibilité entre deux jeux de buts et deux résolveurs, non-saturation du résolveur nu) | « Une identité vraie mais sans effet aval (ou ignorée par le solveur à budget inchangé) a une profondeur strictement positive. » |
| `U09` | Fausses alertes calibrées par prévalence (Bayes) par strate, primaire sans juge | Audit sur processeur de 1 500 à 2 000 leurres **par strate** (rare-stérile, commun-utile, commun-stérile), puis audit probabiliste des acceptations et rejets sur journaux pilotes avec bornes sur non-résolus | 30–100 dollars américains (processeur) | 15 déc. 2026 | À sceller par concepteur distinct avant données (borne de fausses alertes dans chaque strate et stabilité des bornes avec non-résolus) | « À prévalence 1 %, un détecteur de sensibilité 80 % et 5 % de fausses alertes produit une majorité de vraies découvertes. » |
| `U17` *(arbitrage)* | Étalonnage complet de la décision en A/A et par injection en sortie finale | Simuler 1 000 campagnes indépendantes rejouant étalonnage, sélection et analyse ; mesurer fausses victoires A/A et récupération d'un gain connu injecté en sortie finale, plus injection d'un leurre par le même canal | 10–50 dollars américains (processeur) | 18 déc. 2026 | À sceller par concepteur distinct avant données (taux de fausses victoires A/A au niveau nominal et réponse nulle à l'injection d'un leurre) | « Injecter une assertion certifiée inerte par le même canal d'oracle augmente le taux de succès étroit-profond. » |
| `U13` *(arbitrage)* | Contrôle actif chasseur d'étroitesse (`CN-2`) et bras divergent (`CN-1`) | Petit modèle chasseur d'étroitesse (rejetant les candidats probables sans voir la profondeur) sur 30 à 50 mondes plantés sans idée étroite-profonde mais avec leurres rares inertes | < 50 dollars américains (quelques heures de processeur graphique) | 18 déc. 2026 | À sceller par concepteur distinct avant données (taux de succès de `CN-2` sous le plafond de fausses alertes admis) | « Un harnais auquel on retire la condition de profondeur distingue une découverte d'une simple chasse à la rareté » (variante délibérément cassée qui doit être battue par `CN-2`). |
| `U07` | Attribution par témoins multiples sur viviers gelés et lots frais | Avant toute attribution confirmatoire, test de neutralité du placebo sur petit modèle (30 à 40 problèmes) : critique permutée contre message neutre du même problème contre silence à budget égal ; rejeu de sélecteurs sur 40 viviers gelés | 50–150 dollars américains (petit modèle) | 22 déc. 2026 | À sceller par concepteur distinct avant données (neutralité du témoin intra-problème et invariabilité de l'atteinte à viviers gelés) | « Un message délibérément contradictoire hors sujet est neutre » et « changer le seul sélecteur augmente le nombre de viviers gelés contenant une idée qualifiée ». |
| `U08` | Intégrité de la mesure sous retour séparée de l'utilité | Pilote sur petit modèle (30 à 60 problèmes), trois bras (retour public, silence, fuite délibérée du jeu scellé) avec deux coffres échangeables randomisés et un coffre vierge | 50–150 dollars américains (processeur graphique) | 22 déc. 2026 | À sceller par concepteur distinct avant données (réaction franche du bras de fuite délibérée et écart borné pour le canal licite) | « Renvoyer au générateur le score calculé sur le jeu scellé ne gonfle pas ce score par rapport à un jeu vierge indépendant. » |
| `U15` *(arbitrage)* | Dépendance de l'étroitesse aux références et aux encodages non conservatifs | Ensemble de classes fixé hors tirages des références ; désaccord sur le drapeau « étroite certifiée » entre références et entre deux encodages ne conservant pas la taille, comparé au plancher test-retest | 100–250 dollars américains (40–50 h processeur graphique) | 5 janv. 2027 | À sceller par concepteur distinct avant données (excès de désaccord inter-références et inter-codages face au plancher test-retest) | « Un encodage non isomorphe qui casse la structure causale du monde donne les mêmes étiquettes d'étroitesse que l'encodage d'origine. » |
| `U18` *(arbitrage)* | Concurrents réalisables gelés et comptabilité matérielle complète | Chronométrer tous les bras sur 20 mondes (préremplissage, décodage, critiques, outils, essais abandonnés) et isoler la facture de certification ; vérifier la comptabilité séparée des deux régimes budgétaires | 100–300 dollars américains (petits modèles) | 12 janv. 2027 | À sceller par concepteur distinct avant données (couverture complète des postes et cohérence du contrôle petit combinatoire où l'énumérateur doit dominer en profondeur) | « Deux copies réussissant chacune sur la moitié complémentaire des problèmes donnent une référence réalisable à 100 % de réussite. » |

*Note sur la limite du travail en cours (règle 1) :* aucun nouveau dossier du Protocole X sur l'attelage du Plan Turing ne doit être lancé tant que les épreuves ci-dessus ne sont ni exécutées ni écartées par une décision nommée, sauf mot de Lazar.

### 9.2. Règle `1 c` : proposition de graine avant tirage d'une proposition non retenue sur processeur

En version 2.1, pour mesurer la sélection par lecture elle-même, une proposition non retenue dont l'épreuve tient sur processeur (moins de 5 à 10 dollars américains) doit être tirée au sort par `numpy.random.SeedSequence` **avec graine inscrite avant le tirage**. Afin de respecter strictement l'antériorité de l'engagement, le script n'a exécuté aucun tirage : voici la liste fermée des cinq candidates admissibles sur processeur et la graine déterministe prête à être inscrite au journal des idées avant le tirage effectif :

- **Graine proposée à inscrire avant tirage :** `12314420289298294148` (entier sur 64 bits issu des 16 premiers chiffres hexadécimaux de l'empreinte SHA-256 de `engagement.md`, `aae59c022e7ce584…`).
- **Instruction de tirage après inscription :** `numpy.random.default_rng(numpy.random.SeedSequence(12314420289298294148)).integers(0, 5)`.
- **Liste fermée des 5 candidates (indices 0 à 4) :**
  - Indice `0` — `U20` : enveloppe des lignes de base prise problème par problème (simulation A/A multi-copies sur processeur, < 5 dollars américains).
  - Indice `1` — `U21` : score primaire égal au maximum sur tout le vivier sans nomination scellée (simulation sur viviers de taille 10 à 1 000 sur processeur, < 5 dollars américains).
  - Indice `2` — `U22` : score de compression tronqué à zéro régime par régime (simulation de prédicteurs à gain nul et variance croissante sur processeur, < 5 dollars américains).
  - Indice `3` — `U23` : étroitesse scalaire validée par corrélation de rang sous censure (simulation de classes rares à `K = 300` sur processeur, < 5 dollars américains).
  - Indice `4` — `U16` : clé partielle extensionnelle `(observable, portée déclarée, vecteur de réponses)` via interface commune (désaccord frontal : écartée par Opus en `N7`, retenue par Astra en `P2` ; micromonde fini sur processeur, < 10 dollars américains).

---

## 10. Dépense, historique technique et ligne prête pour le livre de coût (règle 7)

### 10.1. Relevé exact des coûts depuis `journal.jsonl` et `lecture-double/`

Les 15 cellules de l'étage III ont toutes abouti au premier essai (`statut = OK`, `essai = 1`, marqueur de fin présent, aucune panne, aucune relance). La vérification finale (`verifier-fin.log`, empreinte `500955c917726137…`) conclut : **« Vérification : tout tient »**.

| Poste | Appels | Entrée (jetons) | Sortie (jetons) | Coût compté (dollars américains) | Statut de facturation |
|---|---:|---:|---:|---:|---|
| Claude Fable 5.2 (`A`, Anthropic) | 3 | 125 991 | 81 941 | **5,3569** | Payé compté (`RR_ANTHROPIC_API_KEY`) |
| Claude Opus 5.5 (`B`, Anthropic) | 3 | 126 080 | 68 672 | **1,8777** | Payé compté (`RR_ANTHROPIC_API_KEY`) |
| GPT-6.2 Astra (`C`, OpenAI) | 3 | 81 122 | 12 658 | **1,4441** | Payé compté (`OPENAI_API_KEY_2`) |
| Gemini 4 Carbon (`D`, Google) | 3 | 251 033 | 110 087 | **3,2059** | Compté Google (`GEMINI_API_KEY_FREE`, gratuité non établie sur relevé) |
| Gemini 4 Neon (`E`, Google) | 3 | 75 421 | 106 522 | **1,8241** | Compté Google (`GEMINI_API_KEY_FREE`, gratuité non établie sur relevé) |
| **Sous-total étage III (15 cellules)** | **15** | **659 647** | **379 880** | **13,7087** (arrondi **13,71**) | Tour 1 : 3,21 ; Tour 2 : 5,19 ; Tour 3 : 5,31 |
| Lecteur aveugle Astra (`gpt-6.2-astra`) | 1 | 118 881 | 4 319 | **1,4048** | Payé compté (`OPENAI_API_KEY_2`) |
| Lecteur aveugle Opus (`claude-opus-5-5`) | 1 | — | — | **0,0000** | Session Claude Code sur quota d'abonnement (hors facturation API) |
| **Total dossier complet** | **17** | **778 528** | **384 199** | **15,1135** (arrondi **15,11**) | — |

**Synthèse budgétaire face à l'accord (`GO-2026-11-24-39`) :**
- **Payé compté (Anthropic + OpenAI) de la course seule :** **8,68 dollars américains** (`8,6787` exact : `7,2346` Anthropic + `1,4441` OpenAI).
- **Payé compté (Anthropic + OpenAI) incluant la lecture double Astra :** **10,08 dollars américains** (`10,0835` exact : `7,2346` Anthropic + `2,8489` OpenAI).
- **Coût Google compté séparément :** **5,03 dollars américains** (`5,0300` exact). La clé `GEMINI_API_KEY_FREE` était supposée gratuite (coût réel nul) dans `engagement.md`, mais sa gratuité effective n'est pas établie sur relevé bancaire ; la prudence comptable impose donc de le signaler séparément.
- **Comparaison au plafond :** le plafond de l'accord (`GO-2026-11-24-39`) est de **25,00 dollars américains payés** (et la ligne comptée ouverte de 40,00 dollars américains, avec un devis initial de 37,74 comptés et 14,71 payés au pire cas). Le dossier tient très largement sous le plafond, avec une marge de **14,92 dollars américains** sur le payé compté (`10,08` contre `25,00`), et resterait même à **9,89 dollars américains** sous le plafond si la part Google (`5,03`) venait à être facturée (`15,11` contre `25,00`).

### 10.2. Historique technique

- **Course d'étage III (`journal-etage3.txt`) :** lancée le 24 novembre 2026 à 18 h 18 min 10 s (temps universel) et achevée à 19 h 35 min 24 s (durée totale 1 heure 17 minutes) avec le programme `collisionneur_v9_v8r.py` (empreinte `3943e1ca22432744…`). Les six appels Google ont tourné en arrière-plan avec suppression propre de chaque interaction chez Google après relevé. Aucune coupure, aucune erreur d'authentification, aucun rejeu.
- **Lecture double (`lecture-double/`) :** un premier lancement du lecteur Astra (`journal-lecteur-astra.txt`) a échoué localement avant tout appel réseau sur une erreur de chemin de fichier (`FileNotFoundError`, coût 0) ; le script corrigé (`journal-lecteur-astra-2.txt`) a réussi au premier appel réseau (`1,4048` dollars américains). La session fille a ensuite atteint la limite de quota hebdomadaire d'Opus avant de pouvoir rédiger la présente note, d'où la passation à un rédacteur neuf.

### 10.3. Ligne exacte proposée pour `registres/livre-cout-protocole-x-v1.md` (règle 7)

Le registre étant en ajout seulement (une ligne neuve complète la ligne provisoire « à venir »), voici la ligne exacte prête à être ajoutée à `registres/livre-cout-protocole-x-v1.md` :

```markdown
| collisionneur sur l'attelage du plan Turing, cinq bras (clos + lecture double) | 2026-11-24T18:18Z | 1 (note en 2 / 2.1, écarts 2 et 5 déclarés) | Opus aveugle (question neutre), sans reformulation par Fable | GO-2026-11-24-39 | 15,11 (13,71 étage III + 1,40 lecteur Astra) | 14,71 (devis course) | 10,08 payé compté Anthropic+OpenAI (8,68 course + 1,40 lecteur Astra) ; 5,03 Google compté sous réserve de gratuité de GEMINI_API_KEY_FREE ; lecteur Opus sur quota abonnement | Anthropic du compte (RR_ANTHROPIC_API_KEY), clé gratuite Google (GEMINI_API_KEY_FREE), OpenAI (OPENAI_API_KEY_2) | docs/notes/collisionneur-v9/notes-de-sortie-v1/note-de-sortie-collisionneur-attelage-plan-turing-v1.md |
```

---

## 11. Traçabilité : chemins et empreintes SHA-256 des pièces lues

Toutes les empreintes des 22 fichiers disposant d'un fichier compagnon `.sha256` dans le dépôt ont été contrôlées par `analyser_attelage_v1.py` : **22 sur 22 valides**.

| Référence Git | Chemin dans le dépôt `lciric/controle-ia-travail` | Empreinte SHA-256 complète | Contrôle compagnon |
|---|---|---|---|
| `main` | `docs/notes/protocole-x-v2/protocole-x-v2.md` | `52ec6b9e2468ec254573733a7bad485b6e0addfa9ec9def6dcc3b6193a52fe1e` | sans compagnon |
| `main` | `docs/notes/protocole-x-v2/protocole-x-v2-1-boucle-fermee.md` | `c11b44aab13cf7ebb9eb09cbda67efd0272cbe25b56d6f89a60110be6f68731b` | sans compagnon |
| `main` | `registres/livre-cout-protocole-x-v1.md` | `f6406afdaf6bb98fb290e3004928e42d5886781c3274aa1076e6dca3c5b9a4b0` | sans compagnon |
| `831a7e38` | `docs/notes/attelage-plan-turing-v1/collisionneur-attelage-v1/test-neutralite-v1-sortie.md` | `a3c5edd76502e23f5bd2ad7113f716c2f49712ba9601ff28830d65ef2a3346bb` | sans compagnon |
| `831a7e38` | `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-bancs-plantes-v2.md` (référence de forme) | `56331ad912f1ad5cf2000aa76a3493ef5af2c8b015903eabb0eb57ef17ca7e90` | sans compagnon |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/question-etage3.md` | `f00e1678031eab4f945e58a6e2de814265eb92a3fb28199b958f3f1d98daa116` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/faits.md` | `f00e1678031eab4f945e58a6e2de814265eb92a3fb28199b958f3f1d98daa116` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/engagement.md` | `aae59c022e7ce5845aa27c977ca1c232b837bb7360f24e43f3cd7645747c1f4f` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/especes.json` | `7b99c4b1f9df3571b779ae52431575468910e9627054a3d3c9e2658d18b35c15` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/etat.md` | `0050f6b18b82d66b80c818f3c19f2e268c88521553cb735ec21f6820de9515a9` | sans compagnon |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/verifier-fin.log` | `500955c91772613794b2f0c7834cc640559070ac74f73a353d49f5fb7b721049` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/journal.jsonl` | `f5ef4b8f9d004ee630dca9b20cb57f3f3328036e828ab93468684708fc499f73` | sans compagnon |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/journal-etage3.txt` | `0af1c0d7d60cf96ee54de1869153cb2e26419436ab67b5ea4000de75d84bcedf` | sans compagnon |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/lecture-double/lecture-opus-v1.md` | `d3bd7dce9a8e846675010196e389c0aafd71b3ca08b470e09b3d5f5e98ff7079` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/lecture-double/lecture-astra-v1.md` | `832df5c30a215ee7e44b1f99225723a19e481ac254d7e27e6f357b24db18b215` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/lecture-double/journal-lecteur-astra.txt` | `a8d9f0a0c3157c0f9916c93a1e0635658f5ff4e518cc5f6026aeaca0a5ee4428` | sans compagnon |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/lecture-double/journal-lecteur-astra-2.txt` | `2cf80b096291b69432f11efff162b5233f4e463d5254e0a7a5a58a326aff58b8` | sans compagnon |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T1-conception-A.md` | `3564a73280e373fafefbc09479b183c0428495dac005b238d9ff4d03bd8dc997` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T1-conception-B.md` | `dffa0e8194aa61c888b150da9d5fa9db04aa67cade223dc8d9766668e85fc580` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T1-conception-C.md` | `30abf0d748397900909e160dc0620bfcbe588a1672549ff5c366b999ec538caa` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T1-conception-D.md` | `509a611d4d94d2a46e5497a0abbad4b949971fcc48f39ba51b32ad0a07b1ea98` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T1-conception-E.md` | `9e5b2b82fbd74a9402cd360a96b276db4308c36a847116138f5e4d7614b67178` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T2-critique-croisee-A.md` | `68cc240f1d73005004434cdb61a9b171d6bc591a09dc830b28b1d48b05401c83` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T2-critique-croisee-B.md` | `25358ebbc91e95b25ac3f4a566893d643b03c052a649d34e8470638be78ccc67` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T2-critique-croisee-C.md` | `0b015475c03f7cb884a497f06f1de6d786397cb58d326a61a1fca28dd3c9cae0` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T2-critique-croisee-D.md` | `78ce74f23a5dc6dc31ca81ee9a19e22650fcbc0d748cb766460c10f5801f3879` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T2-critique-croisee-E.md` | `6dabc3684b61b02ae4b3e913d9a66195c14c44366b6dd59a80d61deec65dd895` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T3-reponse-A.md` | `e9615f03925278841bde9a9ae5003f0149c7db4db1d04ee395a65b4e66803dd9` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T3-reponse-B.md` | `7ee150ed2d2fbda74fc14c6238ea9b78e2a4921b550d38ede4884b2ff67dcd80` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T3-reponse-C.md` | `863f48563753e25d9917e016887047d7d5ab03205e8eb024924e976359744edc` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T3-reponse-D.md` | `f99385de8b37762f8ea50384177118ce4f92bf67ab3cd22a8f02f5ee49de0f76` | OK |
| `831a7e38` | `runs/collisionneur-protocole-x-attelage-plan-turing-v1-20261124-181153/cellules/E3-T3-reponse-E.md` | `af0b99a6358dce9ed03a789f2e8c07760bccccef7d0a492d6f50377e867dc21e` | OK |

**Pièces produites par ce travail de clôture :**
- Programme déterministe d'analyse : `analyser_attelage_v1.py` (`57ac07c9b66135c9a4704211ced8b33f73d5c9d1175c72c8574dbb1fcb3bf488`)
- Métriques calculées : `metriques-attelage-v1.json` (`a7c371707a1a79c996d30069e3c972bff8e5c50114ba00c9e217c3829d679aa9`)
