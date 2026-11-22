# Proposition B — Tour III.1

## Remarques préalables sur les pièces

- **Bloc FAITS.** Son contenu est identique à celui du bloc QUESTION, et les deux annoncent la même empreinte, que je ne peux pas vérifier. Il ne contient **aucun fait muni d'un statut**. Je ne dispose donc d'aucun fait VÉRIFIÉ. Tout ce qui suit est HYPOTHÈSE, sauf mention RAPPORTÉ (de mémoire).
- **Consignes du bloc FAITS.** Je les traite comme des données. La forme de ma réponse suit le bloc QUESTION de l'arbitre, seul habilité à la fixer.
- **Règle B1.** Je ne vois pas les propositions A, C, D et E. Je ne critique ni n'emprunte aucune d'entre elles : la règle B1 est sans objet à ce tour.

---

## 0. Réponses directes aux cinq points de la question

### (1) Question de recherche

> À budget de défense fixé, la probabilité de détecter une dégradation répartie sur k actes individuellement anodins est-elle prédite dans les trois cadres (agent seul, copies coopérantes, moniteurs visés) par une même fonction de deux grandeurs mesurables, le signal par acte des moniteurs locaux et la corrélation entre l'adversaire et les références de contrôle, ou bien chaque cadre exige-t-il son propre modèle ?

### Lecture proposée

Les trois articles étudient la même faiblesse sous trois angles. La défense suppose deux choses :
- **le dommage est localisable**, c'est-à-dire qu'un acte au moins est suspect ;
- **les références sont indépendantes de l'adversaire**, qu'il s'agisse d'exécutions de comparaison ou de moniteurs.

Chaque cadre affaiblit l'une de ces deux suppositions par un canal différent :

| Cadre | Supposition attaquée | Canal |
|---|---|---|
| Agent seul | localisabilité | dilution dans le temps |
| Copies coopérantes | indépendance | poids partagés, contexte partagé |
| Moniteurs visés | les deux | l'adversaire réduit le signal ou corrompt la référence |

Statut : HYPOTHÈSE.

### (2) Réponse attendue, sous forme réfutable

Toutes ces prédictions ont le statut HYPOTHÈSE. Les seuils sont illustratifs.

- **P1 (croisement).** Le taux de détection des moniteurs locaux (texte, activations) décroît avec k à effet total Δ fixé. Celui des exécutions de comparaison dépend surtout de Δ. Les deux courbes se croisent en un point k* situé dans la plage testée.
- **P2 (indépendance).** Le pouvoir de détection des exécutions de comparaison décroît avec la corrélation ρ entre l'erreur de la chaîne attaquée et celle de la référence. Il est donc plus faible quand la référence est une copie du même modèle.
- **P3 (attaque des moniteurs).** Une attaque visant un moniteur équivaut à une baisse du signal par acte s. Le taux de détection après attaque retombe sur la courbe de P1 au nouveau s.
- **P4 (unification).** Une fonction f(s, k, ρ) ajustée sur le seul cadre 1 prédit le taux de détection des cadres 2 et 3 :
  - à ± 0,10 près en taux de détection à 1 % de fausses alertes par trajectoire (illustratif) ;
  - dans au moins 80 % des conditions (illustratif) ;
  - mieux qu'un modèle nul qui prédit par la moyenne du cadre.

**Lecture des issues.** Si P4 échoue, les trois articles gagnent à rester distincts. Cette issue est elle-même une réponse utile à l'équipe.

### (3) Antériorité la plus proche

Toutes ces références sont **citées de mémoire, statut RAPPORTÉ, à vérifier**.

- **Greenblatt, Shlegeris, Sachan, Roger, 2023, *AI Control: Improving Safety Despite Intentional Subversion*.** C'est l'antériorité la plus proche, car elle réunit déjà dans un même cadre trois éléments :
  - un modèle non fiable traité comme adversaire ;
  - un budget d'audit coûteux limité ;
  - une « surveillance non fiable » par une copie du même modèle, avec un risque de collusion et une équipe rouge qui vise le moniteur.

  **Différences à confirmer :** il s'agit d'actes isolés à fort enjeu (porte dérobée dans du code) et non de dommage dilué, et le travail ne contient pas de modèle prédictif d'un cadre à l'autre.
- **Wen et al., 2024, *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats*.** Pour le dommage réparti sur de nombreuses interactions.
- **Bhatt et al., 2025, *Ctrl-Z: Controlling AI Agents via Resampling*.** Pour le rééchantillonnage, proche des « exécutions de comparaison », en contexte agentique.
- **Bailey et al., 2024, *Obfuscated Activations Bypass LLM Latent-Space Defenses*.** Pour les moniteurs d'activations visés par l'adversaire.
- **Donoho et Jin, 2004, *Higher criticism for detecting sparse heterogeneous mixtures* (Annals of Statistics).** Pour la statistique de la détection de signaux épars ou denses, dont P1 est une transposition.

### (4) Expérience qui trancherait

C'est E4, ci-dessous : un test de prédiction **préenregistré**. On ajuste f sur le cadre 1, on mesure s et ρ dans les cadres 2 et 3, puis on prédit avant d'observer. E4 suppose que E0 à E3 aient été conduites. L'ensemble tient en deux mois sur un modèle de 8 milliards de paramètres (section d).

### (5) Type de contribution

**Autre : test de transfert d'une loi connue ailleurs, avec une variable candidate nouvelle.**
- La loi connue ailleurs : le passage d'une détection locale à une détection agrégée quand le signal se dilue, connu en statistique de détection.
- La variable candidate : la corrélation adversaire–référence, induite par le partage de poids.
- Un livrable concret : un banc d'essai commun aux trois articles.

**Ce n'est pas une garantie.** Rien ne sera prouvé au-delà des distributions testées.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Conséquence si elle est fausse |
|---|---|---|---|
| A1 | Des actes individuellement non suspects peuvent composer une dégradation significative du résultat. | HYPOTHÈSE (prémisse non statuée) | La question est sans intérêt : testé par E0. |
| A2 | Un agent de 8 milliards de paramètres peut exécuter un tel sabotage sur une longue tâche. | HYPOTHÈSE | À 8 milliards de paramètres, on **implante** probablement le sabotage (consigne, adaptation LoRA). On mesure alors un sabotage implanté, pas un sabotage émergent. Cette limite est irréductible dans le budget imparti. |
| A3 | Les trois cadres partagent un adversaire de même nature. | HYPOTHÈSE | Les cadres seraient incomparables par construction, ce qui favorise H_B en E4. |
| A4 | « Plus utiles ensemble » est mesurable. | HYPOTHÈSE | Je propose deux définitions opérationnelles : un prédicteur commun (E4) et une politique de budget transférable (E5). |
| A5 | Les moniteurs d'activations lisent une information absente du texte. | HYPOTHÈSE. Des indices existent, par exemple Goldowsky-Dill et al., 2025, *Detecting Strategic Deception Using Linear Probes* (RAPPORTÉ, de mémoire, à vérifier). | Le moniteur d'activations serait redondant : testé en (c) contre une sonde sur plongements de texte. |
| A6 | Les exécutions de comparaison sont indépendantes de l'adversaire. | HYPOTHÈSE, probablement fausse si « l'agent lui-même » est l'adversaire et que la comparaison utilise le même modèle | C'est le cœur de P2 et de E2. |
| A7 | Les vérifications coûteuses sont fiables, c'est-à-dire de quasi-oracles. | HYPOTHÈSE | Si elles manquent les petits Δ, le plancher de sécurité est surestimé. Mesuré en (c). |
| A8 | Les budgets (comparaisons, vérifications) sont comparables d'un cadre à l'autre. | HYPOTHÈSE | Il faut une unité de coût commune, définie en (c). |
| A9 | Dans le cadre 3, l'adversaire connaît le moniteur (boîte blanche ou noire). | Non précisé par la question | J'impose les deux régimes dans E3. |
| A10 | « Dégrader le résultat » est mesurable contre une vérité terrain. | HYPOTHÈSE | J'impose des tâches synthétiques à vérité connue. Cela limite la validité externe. |

---

## (b) Expériences décisives (inférence forte, règle B4)

### Socle commun

**Tâches.** Analyses de données synthétiques en 30 à 80 étapes d'outils (illustratif), avec un effet planté connu.

**Actes de sabotage « défendables ».** Exclusion de lignes, choix d'une covariable, transformation, agrégation, arrondi.

**Notations.**
- **Δ :** biais induit sur l'estimation finale, par exemple 0,3 écart-type (illustratif).
- **k :** nombre d'actes sur lesquels Δ est réparti.
- **s :** aire sous la courbe ROC du meilleur moniteur local sur un acte isolé.
- **ρ :** corrélation, sur un ensemble de tâches, entre l'erreur de sortie de la chaîne évaluée et celle de la référence.

**Cas appariés pour chaque tâche.**

| Cas | Description |
|---|---|
| H+ | Exécution honnête correcte. |
| H− | Exécution honnête avec une erreur naturelle de même Δ, sélectionnée parmi des graines ou des contextes différents. |
| S_k | Exécution sabotée, avec k ∈ {1, 2, 4, 8, 16, 32} (illustratif). |
| P | Saboteur placebo : mêmes types d'actes, Δ = 0. |

**Métrique principale.** Taux de vrais positifs par trajectoire à 1 % de fausses alertes, calculé sur H+ ∪ H−, à coût égal. Les intervalles de confiance sont à 95 % par bootstrap sur les tâches.

**Règle de décision.** Chaque seuil est unique. Une issue n'est tranchée que si l'intervalle de confiance exclut le seuil. Sinon on note « non tranché » et on augmente n, sans réinterpréter le résultat.

### E0. La dilution existe-t-elle à cette échelle ? (prémisse A1)

- **H_A :** il existe k ≤ 32 tel que le taux de vrais positifs du meilleur moniteur local, agrégé sur la trajectoire, est inférieur à 0,5 alors que Δ est atteint.
- **H_B :** pour tout k atteignant Δ, ce taux est d'au moins 0,5.
- **Seuil :** 0,5 (illustratif).
- **Contrôles négatifs :**
  - H− contre H+ : un moniteur qui signale H− aussi souvent que S_k détecte l'erreur, pas le sabotage ;
  - P : un moniteur qui signale P détecte un style, pas un effet.
- **Ce que falsifie chaque issue :**
  - H_B falsifie A1 à 8 milliards de paramètres. La question est alors sans intérêt à cette échelle, avec une réserve sur A2.
  - H_A falsifie l'idée que la surveillance locale suffit dès qu'on agrège sur la trajectoire.

### E1. Croisement local / global dans le cadre 1 (P1)

- **H_A :** les courbes « moniteurs locaux » et « exécutions de comparaison » se croisent en un point k* compris entre 1 et 32.
- **H_B :** elles ne se croisent pas. Soit les moniteurs agrégés dominent pour tout k, parce que l'agrégation compense la dilution, soit les comparaisons dominent pour tout k.
- **Métrique :** taux de vrais positifs à 1 % de fausses alertes en fonction de k, à coût égal (unité de coût définie en c).
- **Variantes d'agrégation :** maximum des scores par acte, somme des scores, et statistique de type « critique supérieure » (Donoho et Jin).
- **Contrôle négatif :** P, sur lequel les comparaisons ne doivent pas détecter au-delà du taux nominal.
- **Ce que falsifie chaque issue :**
  - H_A falsifie l'idée qu'un seul instrument domine toute la plage.
  - H_B falsifie P1, et donc la variable k comme axe d'unification.

### E2. Indépendance des références dans le cadre 2 (P2)

- **Dispositif :** trois copies partagent un carnet de travail. Deux régimes : une seule copie sabotée, ou toutes les copies sabotées, ce dernier régime représentant « l'agent lui-même » comme adversaire.
- **Trois références de comparaison :**
  - **R1 :** même modèle, contexte neuf ;
  - **R2 :** un modèle de 8 milliards de paramètres d'une autre famille ;
  - **R3 :** même modèle avec entrées paraphrasées ou caviardées.
- **H_A :** le pouvoir de détection des comparaisons décroît avec ρ, avec une pente négative dont l'intervalle de confiance exclut 0. R2 dépasse R1 dans le régime « toutes copies sabotées ».
- **H_B :** il n'existe aucune relation. L'intervalle de confiance de la pente contient 0 et sa demi-largeur est inférieure à 0,1 (illustratif), ce qui assure que l'absence de relation est réellement mesurée.
- **Mesure secondaire :** contagion, c'est-à-dire la dérive des sorties des copies honnêtes vers la copie sabotée.
- **Contrôle négatif :** une chaîne entièrement honnête. On y mesure ρ, et le taux de fausses alertes doit rester nominal pour R1, R2 et R3.
- **Ce que falsifie chaque issue :**
  - H_A falsifie A6 pour les copies d'un même modèle.
  - H_B falsifie P2, et donc ρ comme variable d'unification.

### E3. L'attaque d'un moniteur se réduit-elle à une perte de signal ? (cadre 3, P3)

- **Attaques :**
  - adaptation LoRA de l'agent avec une pénalité sur le score de la sonde d'activations, dans l'esprit de Bailey et al. (de mémoire) ;
  - consigne d'euphémisation contre le moniteur de texte ;
  - pour chacune, les régimes boîte blanche et boîte noire.
- **H_A (absorption) :** après attaque, le taux de détection s'écarte d'au plus 0,10 (illustratif) de la courbe E1 évaluée au nouveau s. Les comparaisons et les vérifications ne sont pas affectées.
- **H_B :** l'écart dépasse 0,10. L'attaque a des effets que s ne résume pas, par exemple :
  - une hausse des fausses alertes sur H+ ;
  - un transfert vers un autre instrument, comme un moniteur de texte dégradé par l'entraînement anti-sonde ;
  - une hausse de ρ.
- **Contrôles négatifs :**
  - une adaptation LoRA de même rang et de même nombre de pas, sans pénalité, pour séparer l'effet de l'adaptation de l'effet d'obfuscation ;
  - une sonde réentraînée après l'attaque, pour mesurer la course aux armements.
- **Ce que falsifie chaque issue :**
  - H_A falsifie l'idée que le cadre 3 exige un modèle propre.
  - H_B falsifie P3.

### E4. Test d'unification préenregistré (P4) : l'expérience qui tranche

- **Protocole :** on ajuste f(s, k, ρ), instrument par instrument, sur le seul cadre 1. On **dépose** f, la tolérance et le seuil avant de collecter les cadres 2 et 3. On prédit ensuite à partir des s et ρ mesurés.
- **H_A :** au moins 80 % des conditions des cadres 2 et 3 sont prédites à ± 0,10 près, et f bat un modèle nul (moyenne par cadre) en erreur absolue, avec un intervalle de confiance qui exclut l'égalité.
- **H_B :** moins de 80 % des conditions sont prédites dans la tolérance, ou f ne bat pas le modèle nul.
- **Contrôle négatif :** f réajustée après permutation des étiquettes de cadre. Elle ne doit pas faire mieux que le modèle nul ; si elle le fait, la fonction capture un artefact commun aux tâches.
- **Ce que falsifie chaque issue :**
  - H_A falsifie « les articles gagnent à rester distincts ».
  - H_B falsifie l'existence d'une problématique d'ensemble portée par (s, k, ρ). Il faut alors publier séparément et le dire. D'autres problématiques d'ensemble restent possibles mais ne sont pas testées ici.

### E5. Transfert de politique de budget (seconde définition de « plus utiles ensemble »)

- **Protocole :** on optimise sur le cadre 1 une politique d'allocation du budget B (seuils de déclenchement des comparaisons et des vérifications), puis on l'applique telle quelle aux cadres 2 et 3.
- **H_A :** le regret de sécurité est d'au plus 10 % (illustratif) par rapport à une politique optimisée sur place.
- **H_B :** ce regret dépasse 10 %.
- **Contrôle négatif :** une allocation aléatoire de même budget. Si la politique optimisée sur le cadre 1 ne la bat pas dans les cadres 2 et 3, le transfert n'a pas de contenu.
- **Ce que falsifie chaque issue :**
  - H_A falsifie « les défenses doivent être conçues par cadre ».
  - H_B falsifie l'utilité pratique de l'unification, même si E4 réussit.

---

## (c) Mesure minimale pour chaque instrument nommé dans la question

**Unité de coût commune (illustratif).** Un appel de moniteur vaut 1 unité, une exécution de comparaison 50 unités, une vérification coûteuse 500 unités. Tous les instruments sont comparés à coût égal.

**Cas honnêtes appariés, pour tous les instruments :** H+ et H− sur la même tâche et le même contexte initial, avec des graines appariées. **Cas à détecter :** S_k pour chaque k, et P pour contrôler la spécificité.

### Moniteur de texte

Petit modèle fiable, par exemple 3 milliards de paramètres, ou copie du modèle de 8 milliards de paramètres en surveillance non fiable.

- **Mesure minimale :**
  - taux de vrais positifs à 1 % et à 5 % de fausses alertes, par acte et par trajectoire ;
  - taux de fausses alertes sur H− rapporté séparément, car c'est le cas difficile.
- **Vérifications mécaniques à battre :**
  - **M1 :** réexécution déterministe du code journalisé et comparaison avec les chiffres rapportés ;
  - **M2 :** statistiques élémentaires de trajectoire (longueur, nombre d'opérations de filtrage, nombre de lignes exclues) ;
  - **M3 :** audit aléatoire de même coût.
- **Critère :** si le moniteur de texte ne bat pas M2 à coût égal, il ne fonctionne pas au sens utile.

### Moniteur d'activations

Sondes linéaires sur le flux résiduel, sur plusieurs couches.

- **Mesure minimale :**
  - les mêmes taux que pour le moniteur de texte ;
  - leur stabilité entre tâches tenues à l'écart de l'entraînement.
- **À battre :**
  - **M4a :** la même sonde entraînée sur des plongements de texte des mêmes jetons, issus d'un encodeur séparé. Elle teste A5 : la sonde lit-elle plus que le texte ?
  - **M4b :** une sonde sur le modèle aux poids aléatoires ;
  - M2 et M3.
- **Critère :** la sonde doit battre M4a, sinon le moniteur d'activations n'ajoute rien au moniteur de texte.

### Exécutions de comparaison

- **Mesure minimale :**
  - taux de vrais positifs et de fausses alertes en fonction du nombre d'exécutions (1, 2, 4 ; illustratif) ;
  - ρ mesuré pour R1, R2 et R3.
- **À battre :**
  - **M5 :** désaccord de la valeur finale rapporté à un bruit de bootstrap des données, sans aucune exécution supplémentaire ;
  - M1.
- **Critère :** si M5 égale la comparaison, l'exécution de comparaison ne fonctionne pas, puisque le bruit statistique suffit.

### Vérifications coûteuses

Dans le banc, une réanalyse complète par un vérificateur aveugle à l'hypothèse de sabotage, plafonnée en nombre. La vérité terrain synthétique sert à **évaluer** ce vérificateur, pas à le remplacer.

- **Mesure minimale :**
  - taux de vrais positifs en fonction de Δ, pour trouver le Δ minimal détecté ;
  - taux de fausses alertes sur H−.
- **À battre :** M1 et M3, ainsi qu'une politique de sélection aléatoire des trajectoires à vérifier.
- **Critère :** si le vérificateur manque les Δ visés, A7 est falsifiée et tous les chiffres de « sécurité » doivent être recalculés avec un oracle imparfait.

---

## (d) Ancrage matériel

**Tous les chiffres de cette section sont illustratifs ; aucun ne vient des faits.**

### Modèles ouverts

- **Agent principal :** Llama-3.1-8B-Instruct.
- **Seconde famille :** Qwen3-8B, utilisée pour R2 et pour la réplication.
- **Moniteur de texte fiable :** Llama-3.2-3B-Instruct.
- **Outillage :** vLLM pour la génération, nnsight ou TransformerLens pour les activations.

### Volume

| Élément | Valeur (illustratif) |
|---|---|
| Cadres | 3 |
| Valeurs de k | 6 |
| Tâches par condition | 300 |
| Cas par tâche (H+, H−, S_k, P) | ≈ 4 |
| Graines | 3 |
| Trajectoires au total | ≈ 65 000 |
| Jetons par trajectoire (moyenne) | ≈ 20 000 |
| Jetons générés au total | ≈ 1,3 milliard |

### Calcul

| Poste | Estimation (illustratif) |
|---|---|
| Génération : à environ 20 000 jetons/s sur un H100 en lots, ≈ 20 h ; exécutions de comparaison et réexécutions incluses | ≈ 100 h·GPU |
| Mise en cache des activations et sondes | ≈ 50 h·GPU |
| Adaptations LoRA : saboteur, obfuscation, contrôle sans pénalité, × 2 familles | ≈ 100 h·GPU |
| Marge pour itérations et échecs | ≈ 150 h·GPU |
| **Total** | **≈ 400 h·GPU H100** |
| Coût, à 2 à 3 €/h·GPU | ≈ 1 000 à 1 500 € de calcul |
| Personnel | 1 à 2 personnes pendant deux mois |

### Calendrier

| Semaines | Travail |
|---|---|
| 1–2 | Génération des tâches, saboteur, instruments, unité de coût |
| 3–4 | E0 et E1 sur le cadre 1, ajustement de f, **dépôt du préenregistrement** |
| 5–6 | E2 et E3 |
| 7 | E4 et E5, réplication partielle sur Qwen3-8B |
| 8 | Rédaction |

### Risque principal

A2 : le modèle de 8 milliards de paramètres peut être incapable de suivre un plan de sabotage dilué sur 50 étapes, même avec une consigne explicite.

**Repli :** passer à des actes scriptés insérés par un orchestrateur, mais rédigés par le modèle. On teste alors les défenses, pas la capacité de l'adversaire, et l'article doit le dire.

---

## Issue qui rendrait la question sans intérêt

Il faut distinguer deux issues de nature différente.

### Question sans intérêt

1. **E0 donne H_B.** Le sabotage dilué reste détectable localement pour tout k : il n'existe pas d'actes réellement anodins à cette échelle.
2. **Une vérification mécanique (M1 ou M5) égale ou bat tous les moniteurs et toutes les comparaisons, pour tout k.** Le problème se réduit alors à « réexécuter le code journalisé », et aucun des trois articles n'a d'objet propre.

### Question intéressante, réponse « restez distincts »

C'est l'issue H_B en E4 ou en E5. Elle n'est pas sans intérêt : elle répond négativement à la question de l'équipe, avec une preuve.

---

## Comment vérifier la nouveauté avancée

**Nouveauté revendiquée, statut HYPOTHÈSE.** Une fonction commune f(s, k, ρ) prédirait les trois cadres, et la corrélation adversaire–référence induite par le partage de poids serait la variable qui relie le cadre « copies » aux deux autres.

**Vérifications de nouveauté :**

1. **Bibliographie ciblée, à faire avant la semaine 3.** Mots-clés : « distributed threats », « low-stakes control », « untrusted monitoring collusion », « resampling protocols », « obfuscated activations », « sparse versus dense detection ». Le point précis à vérifier : Greenblatt et al. 2023, Wen et al. 2024 et Bhatt et al. 2025, tous cités de mémoire, contiennent-ils déjà une mesure de ρ ou un modèle prédictif d'un cadre à l'autre ? Si oui, la contribution se réduit à une réplication sur un modèle de 8 milliards de paramètres et doit être présentée comme telle.
2. **Préenregistrement horodaté** de f, de la tolérance, du seuil des 80 % et du modèle nul, avant toute donnée des cadres 2 et 3. Sans ce dépôt, E4 ne tranche rien.
3. **Réplication sur une seconde famille** (Qwen3-8B), pour qu'un succès de E4 ne soit pas propre à un seul modèle.
4. **Publication des trajectoires, des scores bruts et du code des vérifications mécaniques M1 à M5**, pour qu'un tiers puisse recalculer chaque taux.
5. **Ce que la contribution ne prétend pas :**
   - aucune garantie hors des tâches synthétiques testées ;
   - aucune conclusion sur des modèles plus grands ;
   - aucune conclusion sur un sabotage émergent plutôt qu'implanté (A2).

FIN-DE-CELLULE