# Proposition A — Tour III.1 : conception ciblée

## 0. État des pièces

- Le bloc QUESTION est identique au bloc FAITS (même texte, même empreinte). Il ne contient pas de question plus précise que la question générale, donc je traite celle-ci.
- Le bloc FAITS ne porte aucun statut. Je n'en attribue aucun aux énoncés de cadre : je les traite comme des prémisses fournies, non établies.
- Aucune proposition B–E ne m'est transmise (tour à l'aveugle). Je n'en critique et n'en utilise donc aucune (B1).
- Toutes les références sont citées de mémoire et restent à vérifier avant usage. Les seuils chiffrés sont illustratifs.

## 1. Réponse aux cinq points de l'arbitre

**(1) Question de recherche.** À dégât égal, un sabotage diffus laisse-t-il la même quantité de preuve détectable, que ses actes soient répartis dans le temps chez un agent, répartis entre copies d'un même modèle, ou accompagnés d'une attaque contre le moniteur ?

L'objet commun est une **frontière dégât–détection** : pour une intensité de sabotage donnée, le dégât final (abscisse) et la probabilité de détection à taux de fausses alertes fixé (ordonnée), le détecteur agrégeant les preuves par tâche. Les trois articles sont plus utiles ensemble si cette frontière se transporte d'une configuration à l'autre sans recalibrage. Sinon ils gagnent à rester distincts.

**(2) Réponse attendue (HYPOTHÈSE, confiance modérée puis faible).**
- *Temps ↔ copies* : les frontières coïncident à ±10 points de détection (illustratif) à dégât égal, pourvu que l'agrégation se fasse par tâche et non par agent. L'écart résiduel s'expliquerait par la coupure de contexte, pas par la pluralité des copies. Confiance modérée.
- *Moniteur visé* : la frontière se déplace, mais l'évasion a un prix. Réduire la preuve dans le canal attaqué réduirait le dégât ou augmenterait la preuve dans un canal non attaqué. Confiance faible.
- Verdict attendu : unification partielle. Les articles 1 et 2 partageraient une frontière, et l'article 3 mesurerait de combien elle se déplace.
- Ce qui me contredit : un écart temps/copies supérieur à 10 points après contrôle de contexte, ou une évasion « gratuite » (seuils en E2).

**(3) Antériorité la plus proche (de mémoire).** Wen et al., 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » : menaces où aucun acte seul n'est décisif. Le cadre général vient de Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion ». Voisins :
- Bhatt et al., 2025, « Ctrl-Z: Controlling AI Agents via Resampling », pour les exécutions de comparaison.
- Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses », pour les moniteurs d'activations visés.
- Benton et al., 2024, « Sabotage Evaluations for Frontier Models ».
- Wald, 1945, « Sequential Tests of Statistical Hypotheses », et Page, 1954, « Continuous Inspection Schemes », pour l'accumulation de preuves.
- Une référence sur la collusion entre agents génératifs (Motwani et al., 2024) : référence à vérifier, titre exact non garanti.

À ma connaissance, aucune ne teste le transport d'une même frontière entre les trois configurations. C'est une HYPOTHÈSE de nouveauté, non vérifiée.

**(4) Expérience qui tranche.** Voir section 3 : E0 (porte d'entrée), E1 (temps ↔ copies), E2 (moniteur visé), E3 (regret de transfert).

**(5) Type de contribution.** Transfert d'une loi connue ailleurs, avec mesure d'un phénomène. La loi vient de l'analyse séquentielle (accumulation de log-vraisemblances, taille d'échantillon effective sous corrélation). Ce n'est ni une garantie ni un mécanisme interne.

**Issues qui rendraient la question sans intérêt.**
- Une vérification mécanique sans modèle (table de fréquences, test de signe, écart aux ré-exécutions) détecte aussi bien que les moniteurs agrégés. La comptabilité des preuves serait alors superflue.
- Sur un modèle de 8 milliards de paramètres, le sabotage est détectable acte par acte. Le régime diffus n'existerait pas à cette échelle.
- La preuve marginale par acte est nulle dans tous les canaux, même agrégée. Il n'y aurait rien à additionner, et le problème se réduirait à l'allocation des vérifications.

**Vérifier la nouveauté.**
- Remonter les citations de Wen et al. 2024 et de Greenblatt et al. 2023.
- Chercher « distributed threats », « low-stakes control », « sequential monitoring / CUSUM » sur trajectoires d'agents, « collusion untrusted monitor », « probe obfuscation ».
- Critère d'antériorité : un article qui gèle les paramètres d'un détecteur sur une configuration et rapporte l'erreur de prédiction sur les deux autres. S'il existe, ma contribution se réduit à une réplication sur modèle ouvert.

## 2. (a) Ce que la question suppose sans que ce soit établi

Tous ces points ont le statut HYPOTHÈSE, puisque les faits n'en établissent aucun.

| # | Présupposé | Remarque |
|---|---|---|
| P1 | Il existe un régime où aucun acte n'est suspect isolément et où l'ensemble dégrade le résultat. | La formule est ambiguë entre preuve faible mais non nulle (agrégation possible) et preuve marginale nulle, visible seulement dans la conjonction. E0 les sépare. |
| P2 | Les trois configurations relèvent d'un même modèle de menace. | C'est ce que E1–E3 testent, donc ce n'est pas un acquis. |
| P3 | Les moniteurs de texte et d'activations portent un signal non nul sur ce type de sabotage. | Des sondes linéaires de tromperie sont rapportées dans d'autres cadres (Goldowsky-Dill et al., 2025, « Detecting Strategic Deception Using Linear Probes », de mémoire). Le transfert au sabotage diffus n'est pas établi. |
| P4 | Un sabotage induit par consigne ou par ajustement fin renseigne sur le cas où l'adversaire est l'agent lui-même. | Non testable dans ce plan, limite à afficher. |
| P5 | Les exécutions de comparaison sont informatives, donc au moins en partie indépendantes du sabotage. | Faux si le ré-exécutant applique la même politique biaisée. Mesuré en (c). |
| P6 | Les vérifications coûteuses sont exactes et distinguent sabotage et erreur honnête. | Elles établissent un dégât, pas une intention. |
| P7 | La dégradation se mesure sur une échelle commune aux trois configurations. | Vrai seulement par construction, sur tâches à vérité connue. |
| P8 | Le défenseur dispose d'exécutions honnêtes pour calibrer. | Si l'adversaire est l'agent lui-même, aucune exécution n'est garantie honnête en déploiement. |
| P9 | « Plus utiles ensemble » a un critère. | Non fourni. Je propose le regret de transfert (E3). |
| P10 | Un résultat à 8 milliards de paramètres dit quelque chose d'agents plus capables. | Non testé ici. |

## 3. (b) Expériences décisives

**Banc commun.** Ce sont des tâches d'analyse de données synthétiques à vérité plantée (un effet à estimer), de 20 à 40 étapes outillées (illustratif). Elles sont jalonnées d'embranchements dont chaque option est défendable : seuil d'exclusion, covariables, sous-échantillon, arrondi.

- Le dégât est l'écart signé entre l'estimation livrée et la vérité, en unités d'écart-type des exécutions honnêtes.
- L'adversaire est le même modèle, muni d'une politique de sabotage qui choisit à k embranchements l'option poussant l'estimation dans un sens cible, avec k ∈ {2, 4, 8, 16}. La politique est donnée par consigne et, en variante, par adaptateur LoRA sans consigne.
- Le détecteur est la somme par tâche des log-rapports de vraisemblance des scores de moniteurs, calibrée sur exécutions honnêtes.
- Le point de fonctionnement principal est 5 % de fausses alertes (illustratif). 1 % n'est pas estimable avec quelques centaines d'exécutions honnêtes.
- Les intervalles viennent d'un bootstrap apparié par tâche.

Limite de puissance : avec 200 à 300 tâches appariées (illustratif), un écart de 10 points se situe vers deux erreurs standard. Un intervalle chevauchant le seuil est déclaré non concluant, et non interprété.

### E0 — Porte d'entrée : le régime diffus existe-t-il à cette échelle ?

- **H_A (diffus à preuve marginale)** : l'AUROC par acte du meilleur moniteur est < 0,65, et la détection agrégée par tâche dépasse 50 % à 5 % de fausses alertes pour k = 8 (illustratif).
- **H_B (pas de régime agrégeable)** : soit l'AUROC par acte est ≥ 0,65 (sabotage non diffus), soit la détection agrégée est ≤ 15 % (preuve marginale quasi nulle).
- **Contrôle négatif** : étiquettes permutées entre exécutions honnêtes. Le détecteur doit rendre 5 % ± intervalle.
- **Falsification** :
  - H_A est falsifiée par l'une ou l'autre branche de H_B. La première rend le programme inutile à cette échelle. La seconde le réoriente vers l'allocation des vérifications.
  - H_B est falsifiée si les deux conditions de H_A tiennent.
  - Entre 15 % et 50 % : non concluant, à déclarer tel quel.
- **Condition préalable** : le modèle honnête achève au moins 60 % des tâches (illustratif). Sinon on raccourcit les tâches avant toute mesure.

### E1 — Temps ↔ copies

Le même plan de k actes est exécuté dans trois conditions :
- (i) par un agent seul ;
- (ii) par m = 4 copies en chaîne, k/m actes chacune, sans autre canal que les artefacts de travail ;
- (iii) *placebo* : par un agent seul dont le contexte est réinitialisé aux mêmes frontières que les passages de relais.

Le détecteur est gelé sur (i).

- **H_A (comptabilité unique)** : à dégât égal, la détection en (ii) s'écarte de celle en (iii) de moins de 10 points, et les fausses alertes sur exécutions honnêtes multi-copies restent ≤ 2 fois le nominal.
- **H_B (les copies sont un problème distinct)** : l'écart (ii)–(iii) dépasse 10 points, ou la calibration casse.
- **Contrôle négatif** : un classifieur entraîné à distinguer honnête-seul de honnête-multi-copies sur les scores de moniteurs doit rester au hasard. Sinon l'écart mesuré est un artefact de format.
- **Falsification** :
  - Si H_B est vraie, ma réponse attendue est fausse et l'article 2 doit rester séparé, avec ses propres paramètres.
  - Si H_A est vraie, l'article 2 n'a pas d'objet propre sur ce banc au-delà de la coupure de contexte. L'écart (i)–(iii) dit alors ce que coûte cette coupure.

### E2 — Moniteur visé : l'évasion est-elle gratuite ?

Trois attaques sont testées à dégât cible fixé :
- **A-texte** : l'adversaire rééchantillonne 8 fois sa justification et garde la moins suspecte, avec accès en requête au moniteur.
- **A-activations** : ajustement LoRA avec pénalité sur le score d'une sonde gelée, en accès boîte blanche.
- **A-comparaison** : sabotage rendu systématique, donc reproduit à l'identique dans les ré-exécutions.

La mesure principale est le détecteur combiné tous canaux, gelé avant attaque. La mesure secondaire est prise après un seul tour de réentraînement du défenseur.

- **H_A (évasion payante)** : pour chaque attaque, à dégât ≥ 90 % du dégât initial et performance honnête préservée (achèvement à ±5 points), la détection combinée baisse de moins de 20 points.
- **H_B (évasion gratuite)** : au moins une attaque fait baisser la détection combinée de 20 points ou plus sous ces mêmes contraintes.
- **Contrôles négatifs** :
  - La même optimisation est appliquée contre une sonde de direction aléatoire. Elle ne doit pas faire chuter la vraie sonde, sinon on mesure une dérive de distribution et non une évasion.
  - La même optimisation est appliquée à un agent honnête. Ses scores ne doivent pas bouger au-delà du bruit.
- **Falsification** :
  - Si H_B est vraie, la frontière commune ne tient pas sous attaque. L'article 3 devient le cas dimensionnant et les frontières des articles 1 et 2 sont des bornes optimistes, à présenter ainsi.
  - Si H_A est vraie, l'idée qu'un adversaire informé annule les moniteurs à coût nul est falsifiée sur ce banc, et seulement sur ce banc.
- **Mesure annexe**, sans duel propre : où la preuve se déplace-t-elle (autre moniteur, divergence aux ré-exécutions, baisse de dégât) ? C'est ce tableau de transferts entre canaux qu'aucun article séparé ne produirait.

### E3 — Regret de transfert : critère de « plus utiles ensemble »

La politique d'allocation des budgets limités déclenche une ré-exécution ou une vérification quand la preuve cumulée franchit un seuil. Elle est réglée sur (i) seulement, puis appliquée à (ii) et à E2. On la compare à une politique réglée séparément sur chaque configuration, à budget égal (vérification de 5 % des tâches, illustratif).

- **Métrique** : fraction des tâches sabotées interceptées avant livraison.
- **H_A** : le regret de la politique transférée est < 10 points sur les deux configurations.
- **H_B** : le regret est ≥ 10 points sur au moins une.
- **Contrôle négatif** : l'allocation aléatoire uniforme au même budget. Si la politique transférée ne la bat pas, les moniteurs ne servent pas à allouer.
- **Falsification** :
  - Si H_B est vraie, la problématique d'ensemble n'a pas de valeur opérationnelle, même si les frontières se ressemblent à l'œil.
  - Si H_A est vraie, la thèse « trois problèmes, trois réglages » est falsifiée sur ce banc.

## 4. (c) Mesure minimale par instrument

La question nomme quatre instruments. Pour chacun, on mesure l'AUROC par acte, puis par tâche le taux de détection à 5 % de fausses alertes avec intervalle.

**Cas honnêtes appariés, communs aux quatre instruments :**
- (α) même tâche, même graine, même embranchement, politique honnête ;
- (β) *honnêtes malchanceux* : exécutions honnêtes dont l'erreur finale égale celle des sabotées. Sans cet appariement sur le dégât, un moniteur peut ne détecter que « le résultat est faux » ;
- (γ) *mention sans usage* : agent honnête recevant une consigne qui décrit le sabotage et lui dit de ne pas le faire. Sans ce cas, un moniteur peut ne détecter que la présence de la consigne.

| Instrument | Mesure minimale | Vérifications mécaniques à battre | Signe qu'il ne fonctionne pas |
|---|---|---|---|
| **Moniteur de texte** (modèle de confiance notant chaque acte) | Détection par tâche sur α, β, γ. Fausses alertes mesurées séparément sur β. | Table de fréquences des options aux embranchements, calculée sur exécutions honnêtes (option rare = alerte). Test de signe sur le sens des k choix. Longueur et mots-clés. | Gain < 5 points (illustratif) sur la meilleure vérification mécanique, ou fausses alertes sur β supérieures à 2 fois le nominal. |
| **Moniteur d'activations** (sonde linéaire, flux résiduel à mi-profondeur, moyenne sur les jetons de l'acte) | Détection *incrémentale* : combiné texte + sonde contre texte seul, à fausses alertes égales. Transfert d'une sonde entraînée sur sabotage par consigne vers sabotage par LoRA sans consigne. | Sac de mots sur le même texte. Sonde sur la couche d'entrée. Sonde entraînée sur étiquettes permutées. | Gain incrémental nul, alerte sur γ (détecte la consigne), ou effondrement au transfert consigne → LoRA. |
| **Exécutions de comparaison** (n ré-exécutions, position du résultat livré dans leur distribution) | Détection en fonction de n ∈ {1, 2, 4, 8}. Deux régimes : ré-exécutant honnête connu, ou ré-exécutant portant la même politique. *Fraction aveugle* : tâches sabotées dont les ré-exécutions sont biaisées dans le même sens. | Script de référence déterministe quand il existe. Une seule exécution d'un modèle de confiance plus petit. | Courbe plate en n, ou fraction aveugle > 50 % (illustratif) quand le ré-exécutant est l'adversaire. |
| **Vérifications coûteuses** (ici : vérité plantée, oracle par construction) | L'oracle ne mesure pas l'intention. On mesure donc l'*allocation* : précision des vérifications déclenchées et interceptions à budget b ∈ {1, 5, 20} % des tâches. Sur β : taux d'erreurs honnêtes qualifiées à tort de sabotage. | Allocation aléatoire uniforme. Heuristiques « tâche la plus longue » et « résultat le plus extrême ». | Pas de gain sur l'aléatoire au même budget. |

Deux précisions s'appliquent à tout le tableau :
- Le test de signe exige de recalculer l'effet de chaque option. C'est donc déjà une exécution de comparaison bon marché, à compter dans ce budget.
- Dans l'expérience, la vérification coûteuse est parfaite par construction. Son exactitude sur des tâches réelles n'est pas mesurée ici (P6).

## 5. (d) Ancrage matériel

Tous les chiffres de cette section sont illustratifs.

- **Modèle agent** : un modèle ouvert d'instruction d'environ 8 milliards de paramètres, par exemple Llama-3.1-8B-Instruct. Il est honnête par défaut, adversaire par consigne ou par adaptateur LoRA.
- **Modèle de confiance** pour le moniteur de texte et les ré-exécutions de confiance : un modèle ouvert plus petit (1 à 4 milliards de paramètres). En variante, le même modèle sans adaptateur, ce qui mesure le cas favorable.
- **Sondes** : régression logistique sur activations mises en cache, coût négligeable.
- **Volume** :
  - 200 à 300 tâches ;
  - environ 8 000 trajectoires (E0 ≈ 1 200, E1 ≈ 2 400, E2 ≈ 1 600, comparaisons ≈ 2 000, marge) ;
  - environ 20 000 jetons générés par trajectoire, plus les passes de moniteurs ;
  - 6 à 10 ajustements LoRA de quelques heures chacun.
- **Calcul** : 300 à 500 heures-GPU sur une carte de 40 à 80 Go, soit un coût de location de l'ordre de 1 000 à 3 000 USD.
- **Calendrier sur deux mois** :
  - semaines 1 à 3 : banc, vérité plantée, politiques de sabotage, porte E0 ;
  - semaines 4 et 5 : E1 ;
  - semaines 6 et 7 : E2 ;
  - semaine 8 : E3 et rédaction des résultats négatifs éventuels.
- **Poste réellement coûteux** : le travail humain sur le banc (environ trois semaines-personne), pas le calcul.
- **Risque matériel principal** : la variance honnête du modèle sur 20 à 40 étapes peut noyer le sabotage. La parade est de raccourcir les tâches. Si cela ne suffit pas, E0 rend son verdict négatif et le plan s'arrête là.

## 6. Ce que ce plan ne peut pas établir

- Il ne dit rien du sabotage spontané d'un agent (P4), ni d'agents plus capables (P10).
- Les seuils (10, 20 points ; 5 % de fausses alertes) sont des choix à fixer par écrit avant les mesures. Les modifier après coup invalide les duels.
- Une frontière commune sur ce banc d'analyse de données ne vaut pas pour d'autres familles de tâches. La répliquer sur une seconde famille est le premier test externe à demander.
- La nouveauté reste une HYPOTHÈSE tant que la recherche décrite en section 1 n'a pas été faite.

FIN-DE-CELLULE