## (a) Ce que la question suppose sans que ce soit établi

- **HYPOTHÈSE** — Les régimes aveugle et informé peuvent être réellement séparés, sans fuite par les consignes, artefacts, journaux ou interactions successives.
- **HYPOTHÈSE** — Le budget annoncé suffit à estimer séparément la variance entre familles et celle entre éléments d’une famille.
- **HYPOTHÈSE** — La classe déclarée et son mécanisme de génération représentent la population sur laquelle portera l’affirmation d’universalité.
- **RAPPORTÉ** — Cinq instances indépendantes sont prévues ; **HYPOTHÈSE** — cette organisation rend leurs découvertes statistiquement indépendantes.
- **HYPOTHÈSE** — Les familles découvertes peuvent être modélisées comme issues d’une loi identifiable, malgré l’absence de tirage aléatoire.
- **HYPOTHÈSE** — Pour Lincoln-Petersen et Chapman : population fermée, captures indépendantes, probabilités homogènes et appariement exact.
- **HYPOTHÈSE** — Les trajectoires des bancs publics sont brutes, étiquetables, sous licence compatible et leur recouvrement avec l’entraînement est mesurable.
- **RAPPORTÉ** — Les journaux de refus et propositions brutes existent ; **HYPOTHÈSE** — leur provenance permet de les traiter comme sources de capture indépendantes.

## (b) Expériences décisives

### Duel 1 — Chapman est-il utilisable pour estimer le nombre total de familles ?

- **H_A** : dans tous les mondes simulés fermés où indépendance et homogénéité sont imposées, l’intervalle préenregistré autour de Chapman couvre la vérité à au moins 95 %, avec un biais absolu ≤ 5 % *(illustratif)*, et réduit l’erreur quadratique par rapport au comptage brut.
- **H_B** : H_A est fausse dans au moins un de ces mondes.
- **Métriques** : couverture, biais, RMSE, largeur d’intervalle ; comparaison secondaire aux bornes de Chao.
- **Contrôle négatif** : monde sans famille manquante, où le comptage brut est exact ; toute détection de masse manquante est une fausse alerte.
- **Issues** : respect du cahier des charges sur toute la grille falsifie H_B ; une seule violation falsifie H_A. Dans les deux cas, rien n’est établi hors des mondes testés.

### Duel 2 — L’écart vues/tenues à l’écart suffit-il à certifier l’universalité ?

- **H_A** : une règle utilisant uniquement cet écart garantit, sur toute une grille de mondes à vérité connue, une couverture ≥ 95 % pour l’énoncé « proportion de familles en échec ≤ ε ».
- **H_B** : il existe au moins un monde où cette règle certifie à tort plus souvent que le taux α autorisé.
- **Construction** : paires de mondes ayant le même écart observé, mais des queues de distribution différentes ; métriques : couverture et taux de fausse certification. Seuil de tolérance : 2 points *(illustratif)*.
- **Contrôle négatif** : permutation des étiquettes « vue »/« tenue à l’écart » dans un monde échangeable ; tout écart systématique signale une fuite ou une erreur de mise en œuvre.
- **Issues** : couverture respectée partout falsifie H_B ; une violation falsifie H_A et élimine l’écart seul comme certificat.

## (c) Mesure minimale des deux instruments

**Estimateur du nombre de familles.** Sur des mondes simulés faisant varier dépendance, hétérogénéité, erreurs d’appariement et population ouverte : publier biais, RMSE, couverture des intervalles ou bornes, taux de fausse détection de familles manquantes. Base à battre : comptage brut observé, dans une unité déclarée — 34 ou 35 selon la taxonomie. Vérifications mécaniques : énumération exhaustive des petits mondes, double implémentation, graines et sorties scellées.

**Mesure d’universalité.** Sur les mêmes mondes : couverture de la borne sur la part d’échec, biais de l’estimateur, détection des mondes violant ε et fausses alertes sur mondes conformes. Les cas honnêtes sont appariés par famille et budget d’évaluation ; les dépendances entre éléments sont conservées. Base à battre : règle naïve « zéro échec » appliquée aux éléments sans tenir compte des grappes. Vérifications : calcul binomial exact et recomputation indépendante.

# Bloc 1 — Propositions préalables

## 1(a). Définitions opérationnelles

Avant toute mesure, figer : unité de famille, classe \(C\) ou loi \(P\), défense et seuils, critère de réussite familiale, budget, gestion des dépendances et données manquantes.

| Option | Énoncé autorisé | Ce qu’elle n’autorise pas | Vérification par un tiers |
|---|---|---|---|
| **Pire cas** | Pour une classe finie exhaustivement testée : « \(\forall f\in C,\ f\) passe le critère ». Pour une classe infinie, seulement : « tous les éléments effectivement testés passent ». | Aucune extension aux familles non testées sans loi d’échantillonnage. | Rejouer tous les cas et vérifier empreintes, version et exhaustivité de \(C\). |
| **Écart vues/tenues à l’écart** | « Sur ces deux ensembles et ce protocole, \(\widehat\Delta\leq\delta\), avec intervalle déclaré. » | Ni le pire cas, ni une faible part d’échec dans une population plus large. | Vérifier scellement, absence de réutilisation et recomputer \(\Delta\). |
| **Quantile/proportion** | « Avec confiance \(1-\alpha\), \(P_{F\sim P}(\text{échec})\leq\varepsilon\) », ou \(P(\text{réussite})\geq q\). | L’absence d’échec rare ou toute garantie hors de \(P\). | Auditer le tirage, les dépendances et l’intervalle exact. |
| **Garantie stratifiée** | « Pour chaque strate déclarée \(s\), la borne propre à \(s\) est respectée. » | Toute strate non déclarée ou trop peu observée. | Recomputations par strate et correction du risque global. |

« Universelle sur la classe déclarée » est donc un énoncé conditionnel à \(C\) ou \(P\). « Robuste à l’inconnu » ne peut être démontré par un nombre fini de familles découvertes : on peut seulement accumuler des validations extérieures et tester la sensibilité au mécanisme de découverte.

## 1(b). Régime d’information

**Aveugle** : le banc reçoit le contrat d’entrée-sortie et le budget, mais ni défense détaillée, ni familles tenues à l’écart, ni seuils internes. L’existence d’une défense peut être connue sans révéler son fonctionnement.

**Informé** : accès explicitement préenregistré à une défense figée et, selon le palier, au protocole et aux seuils ; jamais aux graines, contenus ou clés d’appariement des familles scellées.

Chaque palier publie nombre de familles et d’éléments, calcul consommé, refus, échecs, taille effective et intervalles. Les budgets sont fixés avant ouverture des scellés. Construction et évaluation ne partagent ni sorties d’instances, ni résultats intermédiaires, ni clés, ni révisions de seuil ; toute réouverture crée une nouvelle version et invalide la confirmation précédente.

## 1(c). Nombre de familles par simulation

Cible : avec confiance \(1-\alpha\), la part d’échec dans \(P\) est inférieure à ε. Pour **zéro échec** et des familles indépendantes, les faits donnent \(n\geq\ln\alpha/\ln(1-\varepsilon)\) : 29 pour ε = 0,10, 59 pour 0,05 et 149 pour 0,02 à 95 %. Les cinq familles prévues ne suffisent donc pas à ces bornes. Avec échecs autorisés, utiliser une borne binomiale exacte plutôt qu’une approximation.

La simulation doit générer : une famille, son niveau de difficulté latent, puis ses éléments corrélés ; elle doit aussi représenter des familles proches en grappes. On estime séparément variance inter-familles et intra-famille, puis on compte des familles indépendantes effectives, non des trajectoires.

L’arrêt séquentiel exige une règle préenregistrée à validité à tout temps ou une dépense d’α ; maximum et abandon sont fixés d’avance. Sensibilités : découverte préférentielle, sources corrélées, duplication, appariement erroné et censure commune.

La simulation démontre la calibration **conditionnellement au générateur et au modèle de découverte**. Elle suppose que ceux-ci représentent la cible ; elle ne transforme pas des familles découvertes en échantillon aléatoire réel.

## 1(d). Familles encore inconnues

Les calculs fournis sont arithmétiquement corrects :

- Lincoln-Petersen : \(700/18=38{,}89\), \(700/19=36{,}84\) ;
- Chapman : \(754/19-1=38{,}68\), \(754/20-1=36{,}70\).

**À calculs inchangés, aucune convention n’est pleinement défendable** : les unités ne sont pas bijectives. En unités Argon, il faut aussi fusionner les deux unités Opus recouvertes ; en unités Opus, il faut scinder l’unité Argon correspondante. Les valeurs 18 et 19 peuvent servir d’analyse de sensibilité, non d’estimateur confirmé.

Hypothèses et biais :

- dépendance positive entre sources : recouvrement accru, donc généralement sous-estimation de \(N\) ; dépendance négative : sens inverse ;
- hétérogénéité : si les familles facilement découvertes dominent les recouvrements, sous-estimation typique, mais le signe général n’est pas identifiable sans modèle ;
- faux appariements : \(m\) trop grand, \(N\) sous-estimé ; appariements manqués : \(N\) surestimé ;
- population ouverte : seul \(N(t)\) est visé, sans borne sur un total futur.

Avec deux sources, l’indépendance n’est pas testable sans hypothèse sur la cellule non observée. Avec plusieurs sources : modèles log-linéaires pour interactions, classes latentes pour l’hétérogénéité, bornes de Chao, Good-Turing pour la masse manquante et la couverture — non pour un total fini — et analyse bayésienne avec priors et sensibilités publiés. Une censure commune définit une strate structurellement invisible : restreindre l’énoncé à la strate observable ou rapporter des scénarios paramétriques, jamais compter ces familles comme inexistantes.

# Bloc 2 — Données de départ recommandées

**Bancs publics.** Je ne connais pas, à partir des pièces, le format, la licence ou l’étiquetage de SHADE-Arena, ControlArena et MonitoringBench ; seule la présence de leur nom est **VÉRIFIÉE**. Leurs propriétés restent **HYPOTHÈSE**. Recommander, après audit, trajectoires brutes versionnées, schéma, licence, provenance et étiquettes familiales séparées. Leur caractère public ne prouve ni indépendance ni absence de recouvrement avec l’entraînement. Ils deviennent sources de capture-recapture seulement si leur processus de constitution est documenté.

**Journaux de refus** (**RAPPORTÉ**) : conserver texte intégral, horodatage, question, version et contexte de décision. Ils renseignent surtout la censure ; leur indépendance programmatique est faible si les mêmes processus les ont produits.

**Propositions brutes d’une course précédente** (**RAPPORTÉ**) : conserver chaque proposition avant résumé, avec source et ordre de production. Coût principal : normalisation et appariement révisable. Elles peuvent ajouter une source de capture, mais pas corriger à elles seules une dépendance commune aux modèles ou aux consignes.

# Bloc 3 — Questions candidates

1. **Comment valider une borne séquentielle d’universalité avec variance à deux niveaux ?**  
   **Avantage** : relie nombre de familles, dépendance et énoncé vérifiable. **Piège** : traiter les éléments comme indépendants ou réviser après ouverture. **Validation** : cinq familles scellées (**RAPPORTÉ**) ; viser séparément 29 familles indépendantes sans échec pour ε = 0,10. **Risque hors périmètre : faible** *(illustratif)* ; la question porte sur la couverture.

2. **Comment estimer les familles inconnues avec plusieurs sources sans supposer leur indépendance ?**  
   **Avantage** : exploite les cinq sources prévues. **Piège** : population ouverte ou censure commune présentée comme cellule nulle. **Validation** : mondes extérieurs à vérité connue, couverture ≥ 95 % et biais ≤ 5 % *(illustratifs)*. **Risque : faible** *(illustratif)* ; livrable limité aux estimateurs.

3. **Comment borner l’incertitude due à l’appariement non bijectif ?**  
   **Avantage** : part d’une anomalie déjà **VÉRIFIÉE**. **Piège** : imposer une grille fermée et un arbitre unique. **Validation** : double lecture externe de tous les liens et arbitrage de tous les désaccords *(illustratif)*, puis intervalles sur plusieurs appariements plausibles. **Risque : faible** *(illustratif)*.

4. **Comment mesurer le transport des garanties vers des données extérieures ?**  
   **Avantage** : confronte prédictions scellées et sources non conçues pour la défense. **Piège** : recouvrement d’entraînement ou étiquetage construit après observation. **Validation** : trois bancs audités au plus, avec seuil de calibration préenregistré ; tout chiffre de performance restant *(illustratif)* avant audit. **Risque : moyen** *(illustratif)*, borné par l’exclusion de toute description de tâche.

5. **Comment mesurer l’écart entre évaluations aveugle et informée à budget égal ?**  
   **Avantage** : exploite les deux versions déjà **VÉRIFIÉES** dans le programme. **Piège** : budgets ou familles différents. **Validation** : mêmes cinq familles scellées, différence et intervalle publiés ; seuil \(\delta=0{,}02\) *(illustratif)*. **Risque : faible** *(illustratif)*.

# Bloc 4 — Organisation des instances scellées

Sauf décision **RAPPORTÉE**, les effets des organisations suivantes sont des **HYPOTHÈSES**.

| Point | Options, avantage et inconvénient | Recommandation et confiance |
|---|---|---|
| **Consignes** | Identiques : comparabilité, mais corrélation accrue. Différentes : diversité possible, mais effets de consigne confondus avec ceux du fournisseur. | Noyau identique limité au format, au périmètre et à l’interdiction de consulter la défense ; variations seulement préenregistrées et analysables. **Confiance moyenne.** |
| **Fuites** | Séparation logique seule : peu coûteuse, mais mémoires partagées possibles. Environnements et accès distincts : plus contraignants. | Contextes, identifiants, stockages et coordinateurs séparés ; sorties hachées et scellées ; aucune lecture croisée avant clôture. **Confiance élevée pour le processus, faible pour l’indépendance de fond.** |
| **Appariement** | Lecteur unique : cohérent mais biais lignée/grille. Vote forcé : rapide mais écrase les relations un-à-plusieurs. | Schéma canonique défini avant lecture ; plusieurs lecteurs aveugles à la source et à la défense ; liens incertains, multiples et non-appariés autorisés ; arbitrage humain et analyse sur tous les appariements plausibles. **Confiance élevée.** |
| **Indépendance** | Similarité des sorties : observable, mais ne teste pas les données d’entraînement. Déclarations fournisseurs : utiles, non suffisantes. | Demander documentation de provenance ; tester interactions entre sources par modèles multi-listes et sensibilités ; ne jamais conclure à l’indépendance des corpus à partir des seules sorties. **Confiance faible.** |
| **Estimation multi-sources** | Log-linéaire : interactions estimables avec assez de listes. Classes latentes/bayésien : hétérogénéité explicite, mais dépendance aux hypothèses. | Publier comptage brut, Chao/Good-Turing, modèles multi-sources et scénarios bayésiens ; validation en laissant une source hors ajustement. **Confiance moyenne.** |
| **Refus** | Le compter comme zéro : biais direct. Le reformuler jusqu’à obtention : censure dissimulée. | Consigner le refus et sa portée ; appliquer une règle de remplacement préenregistrée ; analyses avec et sans la source. Un refus commun devient une strate de censure, non une absence de familles. **Confiance élevée.** |

## (d) Ancrage matériel — moins de 100 mots

Modèles ouverts de 8 et 70 milliards de paramètres (**RAPPORTÉ**). Les simulations d’estimateurs tiennent sur CPU ; seule l’application des défenses aux éléments exige l’inférence des modèles. Ordre de matériel : un GPU pour le 8B, plusieurs GPU à forte mémoire pour le 70B, selon précision et contexte *(illustratif)*. Budget : 5 000–30 000 € de calcul et 20–60 jours-personne pour génération, audit et double implémentation *(illustratif)*. Aucun agent attaquant opérationnel n’est requis.

FIN-DE-CELLULE