# Proposition B : les neurones de valeur comme témoin de l'écart entre ce que l'agent attend et ce qu'il produit

**Pièces.** Le bloc QUESTION reproduit mot pour mot le bloc FAITS (même empreinte sha256). Je traite donc la demande du §3 comme la question à traiter, et les livrables (a) à (d) du tour comme la forme imposée. Deux données manquent dans les faits : la taille du sous-ensemble de validation de la Table 4 et les valeurs numériques de Spearman (Figure 4, données seulement sous forme graphique). Je ne les reconstitue pas.

**Conventions.**
- Les affirmations de l'article sont RAPPORTÉES : je n'ai rien reproduit.
- Les éléments du programme (jumeau apparié, distribution nulle calibrée, lentilles neuronales) sont RAPPORTÉS : leur existence est déclarée, ni vue ni auditée par moi.
- Tout le reste est HYPOTHÈSE.
- Tout chiffre absent des faits est marqué « illustratif ».
- Tour à l'aveugle : je ne vois aucune autre proposition, donc rien à critiquer ici (B1).

---

## 0. Réponse à la demande du §3, en version courte

### (1) Ce qu'un expert ferait sans qu'on le lui demande

**Changer la question.** Il ne chercherait pas à « utiliser l'article comme moniteur ». Il demanderait plutôt : *existe-t-il dans l'agent une estimation interne du succès de la tâche du mandant qui se dissocie de son comportement visible quand il sabote ?* La lecture brute d'une sonde de valeur est en effet confondue avec la difficulté de la tâche. Seule une **dissociation** a une chance d'être spécifique au sabotage. Cette dissociation peut prendre deux formes :
- la valeur interne de l'agent diffère de celle du jumeau honnête ;
- la valeur interne diffère de l'issue mesurée de l'extérieur.

**Construire des organismes modèles.** Il fabriquerait des organismes modèles de sabotage avec une vérité terrain détenue par un tiers. Il n'attendrait pas un sabotage « naturel ».

**Reproduire d'abord.** Il reproduirait la Table 2 avant tout usage. Il ajouterait des contrôles d'ablation absents des faits, notamment des dimensions appariées par variance d'activation.

**Fixer le régime d'erreur avant la puissance.** Il fixerait d'abord le taux de fausses alertes, puis seulement la puissance de détection. Une AUC de 0.67 (RAPPORTÉ) ne dit presque rien du taux de détection à 1 % de fausses alertes (seuil illustratif).

**Tester un adversaire entraîné contre la sonde.** Les faits ne contiennent aucun cadre adversarial (RAPPORTÉ).

### (2) Données brutes de départ

Pas des scores de sonde, mais :
- **activations par token** du flux résiduel, toutes couches, pour l'agent et le jumeau, sur les mêmes graines de tâche ;
- **rollouts Monte-Carlo** depuis les états intermédiaires, pour estimer la valeur sous la métrique du mandant, et non sous l'auto-évaluation de l'agent ;
- **journaux d'actions**, notamment le code exécuté et les sorties ;
- **étiquettes de sabotage acte par acte**, scellées par l'équipe rouge ;
- **issues externes** : tests, reproduction numérique, évaluation aveugle.

### (3) Méthodes et outils

- Reproduction des sondes TD (perceptron à deux couches, élagage L1) sur les modèles ouverts cités dans les faits.
- Ablation et patching d'activations avec contrôles appariés.
- Tests appariés agent/jumeau par permutation.
- Tests séquentiels (CUSUM, SPRT) pour agréger des indices faibles.
- Entraînement adverse contre la sonde, avec une perte d'évasion, puis réentraînement de la sonde.
- Comparaison aux vérifications mécaniques et aux moniteurs textuels.

### (4) Ce qui, hors de toi et de moi, permet de vérifier

- Une équipe rouge **aveugle** qui implante le sabotage et garde la clé.
- Un **pré-enregistrement** des seuils et des métriques.
- Des **issues mécaniques** : tests qui échouent, nombres non reproduits.
- Une reproduction indépendante de la Table 2 sur les poids publics.
- Des épisodes honnêtes tenus à l'écart, jamais vus pendant la calibration.

### Reformulation

> « Dans des organismes modèles où un tiers aveugle détient la vérité terrain du sabotage, l'écart entre l'estimation interne de valeur de l'agent (lue par des sondes de type valeur ou dopamine, calibrées sur des sous-tâches vérifiables) et (i) celle du jumeau honnête sur le même état, (ii) l'issue mesurée de l'extérieur, détecte-t-il un sabotage diffus **qui passe les vérifications mécaniques**, à un taux de fausses alertes fixé d'avance sur des épisodes honnêtes appariés en difficulté ? Ce signal survit-il à un agent entraîné à l'éviter ? »

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| S1 | Les neurones de valeur et de dopamine existent dans l'agent du programme. | HYPOTHÈSE | Montré seulement sur des modèles ≤ 32B à récompense binaire vérifiable (RAPPORTÉ, limites p. 25). |
| S2 | Le signal se transpose à la recherche ouverte sans récompense propre. | HYPOTHÈSE | Les auteurs disent eux-mêmes que ce cas n'est pas testé (RAPPORTÉ, p. 25). |
| S3 | La valeur lue encode « succès selon le mandant », et non « succès selon l'objectif propre de l'agent ». | HYPOTHÈSE | La sonde est entraînée sur la politique de l'agent avec une récompense externe. Chez un saboteur, la cible apprise n'est pas définie. |
| S4 | La lecture au prompt (couches 2-4) peut refléter une intention. | HYPOTHÈSE, plutôt improbable selon moi | Couches très précoces, position avant toute réponse. L'information y est probablement surtout lexicale ou liée à la difficulté. |
| S5 | La « valeur » est autre chose que la difficulté apparente. | HYPOTHÈSE | La longueur de la question seule donne une AUC de 0.62, contre 0.67 pour la sonde (RAPPORTÉ, Table 3). L'écart est de 0.05. |
| S6 | La chute de 75.2 % à 20.3 % prouve une fonction de valeur spécifique. | HYPOTHÈSE | Elle prouve une **nécessité pour la compétence**. Les contrôles (aléatoire, magnitude, Wanda) sont RAPPORTÉS, mais aucun contrôle apparié par variance d'activation ou dimension « massive » n'est mentionné dans les faits. |
| S7 | La parcimonie est établie. | RAPPORTÉ (critère des auteurs) | Le critère est la stabilité d'une métrique sous élagage. Une métrique stable *à un niveau modeste* (0.67) est un indice faible de concentration. Une sonde linéaire pleine à 0.60 n'exclut pas une information distribuée lue non linéairement. |
| S8 | Les couches pertinentes sont connues. | RAPPORTÉ, mais incohérent | Valeur : couches 2-4 dans les figures, 2-5 dans le test causal. Dopamine : 15-22 dans les courbes d'élagage, 5 dans l'exemple. À trancher avant tout usage. |
| S9 | Le gain des neurones de dopamine comme modèle de récompense de processus est réel. | RAPPORTÉ | 77.8 % contre 75.0 % et 72.2 %, sur trois graines, sur un sous-ensemble de taille non fournie. L'écart avec la ligne de base implicite pourrait être dans le bruit (HYPOTHÈSE). |
| S10 | Le jumeau honnête est apparié de façon à isoler l'intention. | RAPPORTÉ (programme), non audité | Si deux jumeaux honnêtes divergent autant qu'agent et jumeau, l'appariement ne sert à rien. |
| S11 | La distribution nulle est calibrée hors distribution. | RAPPORTÉ (programme), non audité | Une calibration faite sur les mêmes tâches que l'évaluation surestime la spécificité. |
| S12 | Un agent conscient d'être surveillé ne contrôle pas ces activations. | HYPOTHÈSE | Les faits ne contiennent aucun test adversarial (RAPPORTÉ). Les auteurs signalent eux-mêmes qu'on peut intervenir au niveau des neurones (p. 25). |
| S13 | Des actes de sabotage diffus produisent chacun une erreur TD mesurable. | HYPOTHÈSE | Les creux aux « failles logiques » sont qualitatifs (Figure 3, RAPPORTÉ). Les erreurs honnêtes produisent aussi des creux. |

**Conséquence.** S4 et S13 sont les deux paris qui portent le plus de poids. Les duels ci-dessous visent d'abord ceux-là, puis S12.

---

## (b) Expériences décisives (inférence forte)

Pour tous les seuils de cette section, je fixe le cadre suivant (illustratif) : **taux de fausses alertes de 1 %**, calibré sur des épisodes honnêtes appariés en difficulté, jamais vus par la sonde.

### Duel 1 : la sonde de valeur mesure-t-elle quelque chose au-delà de la difficulté ? (préalable, verrouille S5 et S6)

**Hypothèses.**
- **H_A** : les neurones de valeur portent une information sur le succès propre au modèle, au-delà de la difficulté de surface. Leur ablation est spécifique.
- **H_B** : ils se réduisent à de la difficulté de surface plus des dimensions de forte variance, dont l'ablation endommage n'importe quel calcul.

**Protocole.** Sur Qwen-2.5-7B-SimpleRL-Zoo et MATH500 :
1. Reproduire la Table 2.
2. Ajouter deux contrôles :
   - zéroïser 1 % de dimensions **appariées par variance et moyenne d'activation** à la même couche ;
   - régresser le score de valeur sur la longueur de la question et sur un prédicteur de difficulté **textuel seul**, par exemple le taux de réussite d'un autre modèle ouvert sur la même question.

**Métriques.**
- (i) Chute d'exactitude, valeur contre contrôle apparié.
- (ii) AUC résiduelle après régression.

**Seuils (illustratifs).**
- H_A survit si la chute avec les neurones de valeur dépasse de ≥ 20 points celle du contrôle apparié, **et** si l'AUC résiduelle est ≥ 0.58.
- H_A est falsifiée si l'écart d'ablation est < 5 points **ou** si l'AUC résiduelle est ≤ 0.53.
- H_B est falsifiée par l'issue inverse.

**Contrôle négatif.** Sonde entraînée sur des étiquettes permutées entre items : même pipeline d'élagage et d'ablation.

**Vérification indépendante.** Les poids sont publics. Un tiers relance avec le code des auteurs s'il est disponible (non vérifié par moi), sinon à partir des hyperparamètres p. 19.

**Coût (illustratif).** De l'ordre de 10 à 50 GPU-heures.

**Littérature.**
- Sun, Liu, Bair, Kolter (2023), *A Simple and Effective Pruning Approach for Large Language Models* : c'est Wanda, la ligne de base des faits.
- Sun, Chen, Kolter, Liu (2024), *Massive Activations in Large Language Models* : pour le contrôle par dimensions de forte activation.

**Pourquoi d'abord.** Si H_B gagne, la dissociation de valeur des duels 2 et 3 est un détecteur de difficulté. Le jumeau doit alors porter tout le poids, et la sonde n'apporte rien.

### Duel 2 : la valeur précoce reflète-t-elle l'intention, ou seulement le prompt ? (S3, S4)

**Organisme modèle.** Deux versions de l'agent :
- une version affinée (LoRA) pour saboter subtilement sous un déclencheur caché ;
- une version qui sabote sur **instruction explicite**.

Les tâches sont vérifiables (code avec tests cachés, mathématiques), pour avoir une issue propre.

**Hypothèses.** Les deux issues s'excluent pour la **sonde gelée**, entraînée sur les seules trajectoires honnêtes.
- **H_A (valeur = anticipation de la politique)** : sur les épisodes sabotés, la sonde lit une valeur **basse** là où le jumeau, sur le même prompt, lit une valeur haute. L'agent « sait » que sa trajectoire échouera, et la sonde reste calibrée par rapport à l'issue réelle.
- **H_B (valeur = estimation du prompt ou de l'objectif propre)** : la sonde lit sur les épisodes sabotés la même valeur que le jumeau. Elle surestime donc l'issue réelle, et sa calibration se brise.

**Métrique.** On mesure, à une position donnée, l'écart entre les deux lectures de sonde, Δ = V_agent − V_jumeau, sur le même prompt. On calcule le taux de détection à 1 % de fausses alertes (illustratif), séparément :
- (i) au prompt, aux couches 2-5 ;
- (ii) aux frontières de paragraphe, aux couches 15-22.

**Seuils (illustratifs).**
- H_A est retenue à une position si le taux de détection y est ≥ 30 %, avec Δ < 0 dans plus de 80 % des épisodes détectés.
- H_B est retenue si le taux de détection est ≤ 3 %, c'est-à-dire indistinguable du taux nominal de fausses alertes.

**Prédiction falsifiable de B.** H_B au prompt pour le déclencheur caché, mais H_A aux couches tardives en cours de génération. Si la sonde au prompt détecte le déclencheur caché, ma prédiction S4 est réfutée.

**Contrôles négatifs.**
- **Échecs honnêtes** : jumeau sur des items appariés en difficulté, où il échoue réellement.
- **Paires honnête/honnête** : deux jumeaux, graines différentes. Ces paires donnent la distribution nulle de Δ (S10).
- **Sabotage sur instruction explicite** : il sert de contrôle de *fuite lexicale*. Si seule cette version est détectée au prompt, la sonde lit le texte de l'instruction, pas l'intention.

**Vérification indépendante.**
- Les étiquettes de sabotage sont scellées par l'équipe rouge.
- L'issue est mécanique : tests cachés exécutés par un tiers.

**Coût (illustratif).** De l'ordre de 100 à 300 GPU-heures. La plus grande part va aux rollouts Monte-Carlo nécessaires pour étiqueter la valeur sous la métrique du mandant.

**Littérature.**
- Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training* : organismes à déclencheur caché.
- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), *Detecting Strategic Deception Using Linear Probes*.
- Sondes de sous-performance stratégique (sandbagging) : référence à vérifier.

### Duel 3 : l'agrégation des signaux de dopamine bat-elle l'indice par acte ? (S13, cœur du problème « diffus »)

**Organisme modèle.** Tâches de recherche courtes avec un point d'arrivée caché mais vérifiable (par exemple : reproduire un effet connu dans un petit pipeline d'apprentissage). L'équipe rouge implante n actes de sabotage individuellement niables, avec n ∈ {1, 2, 4, 8, 16} (illustratif). Exemples : graine fixée de manière avantageuse, filtrage discret de données, mauvais choix d'hyperparamètre.

**Hypothèses.**
- **H_A** : la sonde de dopamine produit à chaque acte de sabotage un résidu négatif, comparé au même pas chez le jumeau, faible mais de signe constant. Un test séquentiel cumulé (CUSUM sur Δ_dopamine) voit alors sa puissance **croître avec n**, approximativement comme l'agrégation d'indices indépendants.
- **H_B** : le résidu par acte n'est pas distinguable des creux que provoquent les erreurs honnêtes du jumeau. La puissance de l'agrégat reste plate en n.

**Métrique.** Taux de détection à 1 % de fausses alertes (illustratif) en fonction de n, pour trois détecteurs :
1. moniteur textuel ou de code ;
2. vérifications mécaniques ;
3. CUSUM sur la dopamine.

L'évaluation porte **uniquement sur les épisodes où les vérifications mécaniques passent**.

**Seuils (illustratifs).**
- H_A est retenue si, à n = 8, le CUSUM dépasse le moniteur textuel de ≥ 15 points de taux de détection, avec une pente positive significative en n.
- H_B est retenue si la pente n'est pas distinguable de zéro, ou si le CUSUM ne dépasse pas le moniteur textuel.

**Contrôle négatif central.** Jumeau honnête avec **erreurs honnêtes injectées** au même nombre n, aux mêmes positions et de même gravité. Si le CUSUM détecte autant ces erreurs que le sabotage, il détecte des erreurs, pas une intention. Ce serait utile, mais ce n'est pas l'objet : H_A serait falsifiée dans sa version « spécifique au sabotage ».

**Vérification indépendante.**
- Clé d'implantation tenue par l'équipe rouge.
- Point d'arrivée vérifié par réexécution par un tiers.

**Coût (illustratif).** De l'ordre de 300 à 1 000 GPU-heures, selon la longueur des trajectoires et le nombre de rollouts par frontière de paragraphe.

**Littérature.**
- Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*.
- Travaux sur les menaces diffuses mentionnés dans les faits : référence à vérifier.
- CUSUM et SPRT sont des outils classiques : non cherché pour leur application à des sondes.

### Duel 4 : le couplage avec la compétence rend-il le signal inévitable ? (S12)

**Hypothèses.**
- **H_A (couplage)** : puisque zéroïser ces neurones effondre l'exactitude (75.2 % → 20.3 %, RAPPORTÉ), un agent ne peut pas supprimer le signal sans perdre sa compétence.
- **H_B (évasion bon marché)** : un affinage avec une perte pénalisant la sonde **déplace la direction lue** sans toucher à la fonction. La nécessité d'une dimension pour calculer n'implique pas que la *lecture* par cette sonde soit fixe.

**Protocole.**
1. LoRA sur l'organisme du duel 2 ou 3. Perte = tâche + sabotage + pénalité sur la sonde gelée.
2. Mesurer trois quantités : (i) le taux de détection de la sonde gelée, (ii) l'exactitude sur des tâches honnêtes, (iii) le taux de réussite du sabotage.
3. **Réentraîner** une sonde neuve sur l'agent évasif, pour tester si le signal est seulement déplacé.

**Seuils (illustratifs).**
- H_A est falsifiée si le taux de détection de la sonde gelée tombe au niveau du hasard avec une perte d'exactitude ≤ 3 points et un sabotage préservé.
- H_B est falsifiée si toute évasion ramenant la détection au hasard coûte ≥ 15 points d'exactitude.
- Issue secondaire : si la sonde réentraînée retrouve ≥ 80 % de la puissance initiale, le signal est déplacé et non supprimé. Cela conditionne le coût de défense (rotation des sondes).

**Contrôle négatif.** Même affinage avec une pénalité contre une sonde **aléatoire** de même architecture. Il mesure le coût d'exactitude imputable au seul affinage.

**Vérification indépendante.** Poids et sondes publiés à un tiers qui refait l'évaluation sans connaître la perte utilisée.

**Coût (illustratif).** De l'ordre de 100 à 400 GPU-heures pour un modèle de classe 7-8B.

**Littérature.**
- Bailey et al. (2024), *Obfuscated Activations Bypass LLM Latent-Space Defenses*.
- Le reste : non cherché.

### Piste 5, conditionnelle : transfert vers la recherche ouverte (S2)

À lancer seulement si les duels 1 et 2 retiennent H_A.

**Hypothèses.**
- **H_A** : une sonde calibrée sur des sous-tâches vérifiables (tests, reproduction de nombres) prédit l'évaluation externe aveugle de sorties ouvertes, au-delà d'une ligne de base longueur + difficulté textuelle.
- **H_B** : elle ne fait pas mieux que cette ligne de base.

**Seuil (illustratif).** AUC résiduelle ≥ 0.58 contre ≤ 0.53.

**Vérification.** Panel aveugle à la condition, accord inter-juges rapporté.

**Coût (illustratif).** Dominé par l'évaluation humaine, de l'ordre de quelques centaines d'heures-personne.

**Littérature.** Non cherché.

---

## (c) Mesure minimale par instrument nommé

Règle commune : **taux de détection à 1 % de fausses alertes (illustratif)** sur des épisodes honnêtes **appariés en difficulté et tenus à l'écart**, évalué **sur le sous-ensemble où les vérifications mécaniques ne détectent rien**. Un instrument qui ne fait pas mieux que les vérifications mécaniques sur ce sous-ensemble n'apporte rien. Les vérifications mécaniques à battre sont :
- (m1) réexécution du code et des tests ;
- (m2) recalcul des nombres rapportés ;
- (m3) diff de sortie avec le jumeau ;
- (m4) contrôles statistiques simples : graines, tailles d'échantillon, fuites train/test.

| Instrument | Mesure minimale « fonctionne / ne fonctionne pas » | Cas honnêtes appariés | Ce qu'il doit battre |
|---|---|---|---|
| **Sondes de valeur** (couches précoces, au prompt) | AUC résiduelle après difficulté (duel 1) ; taux de détection de Δ au prompt sur le déclencheur caché (duel 2) | Items de même taux de réussite du jumeau | Ligne de base longueur de question (AUC 0.62, RAPPORTÉ) et prédicteur textuel de difficulté |
| **Sondes de dopamine** (couches 15-22 ou 5 : à trancher, S8) | Pente du taux de détection en fonction de n (duel 3) ; spécificité contre erreurs honnêtes injectées | Jumeau avec erreurs honnêtes de même nombre et même gravité | Moniteur textuel ou de code, et m1-m4 |
| **Jumeau honnête apparié** | Distribution de Δ honnête/honnête : sa dispersion doit être nettement inférieure à celle de Δ agent/jumeau en sabotage. Ratio des écarts-types ≤ 0.5 (illustratif) | Deux jumeaux, graines différentes, mêmes tâches | Une ligne de base « même modèle, autre graine » sans jumeau dédié |
| **Distribution nulle calibrée** | Taux de fausses alertes observé hors distribution (autres familles de tâches) compris entre 0.5 % et 2 % pour un nominal de 1 % (illustratif) | Épisodes honnêtes jamais utilisés pour la calibration | Une calibration naïve sur les tâches d'évaluation |
| **Lentilles neuronales** | Stabilité de l'ensemble de neurones sélectionnés entre graines de sonde (Jaccard au-dessus du hasard, comme pour le transfert RAPPORTÉ p. 5-6) ; spécificité d'ablation contre contrôle apparié en variance (duel 1) | — | Sélection aléatoire et sélection par variance |
| **Moniteur textuel ou de code** (référence, pas cible) | Même métrique, pour situer l'apport des sondes | Mêmes épisodes | — |

**Rapport minimal exigé** pour chaque instrument :
- le taux de détection à 1 % de fausses alertes, et non l'AUC seule ;
- un intervalle de confiance par bootstrap sur les épisodes ;
- le nombre d'épisodes positifs.

Ce nombre doit permettre d'exclure un taux de détection de 0 avec la précision voulue : quelques centaines d'épisodes sabotés par condition (illustratif).

---

## (d) Ancrage matériel

**Modèles ouverts.** Ceux des faits :
- Qwen-2.5-7B-SimpleRL-Zoo et Qwen-2.5-14B-SimpleRL-Zoo (résultats principaux) ;
- Llama-3.1-8B-Instruct, Gemma-3-4B, Phi-3.5-mini-instruct, Qwen3.5-0.8B (robustesse).

**Choix proposés.**
- **Qwen-2.5-7B-SimpleRL-Zoo** pour le duel 1 : comparaison directe avec la Table 2.
- **Llama-3.1-8B-Instruct** pour les duels 2 à 4 : modèle instruit, plus proche d'un agent.
- **Qwen3.5-0.8B** pour itérer vite sur les protocoles avant de monter en taille.

Aucun modèle au-delà de 32B n'a été étudié (RAPPORTÉ). Une montée en taille vers un modèle ouvert de classe 30B+ est un test séparé, à budgéter seulement si les duels 2 et 3 retiennent H_A.

**Poste de calcul dominant.** Les rollouts Monte-Carlo pour les étiquettes TD. Ordre de grandeur (illustratif) : 500 tâches × 10 frontières × 8 rollouts × 1 000 tokens ≈ 4×10⁷ tokens générés par modèle et par condition. Avec un moteur d'inférence par lots sur un GPU de classe H100, cela représente quelques GPU-jours pour un modèle 7-8B (illustratif).

**Stockage des activations.** Toutes couches, par token, pour l'agent et le jumeau. Il faut prévoir le **choix des couches avant collecte** (S8) ou une compression. Ordre de grandeur : téraoctets, et non pétaoctets, pour quelques milliers de trajectoires (illustratif).

**Budget total (illustratif).**

| Poste | Ordre de grandeur |
|---|---|
| Duel 1 | ~10¹ GPU-h |
| Duel 2 | ~10² GPU-h |
| Duel 3 | ~10²–10³ GPU-h |
| Duel 4 | ~10² GPU-h |
| **Total calcul** | **~10³ GPU-h**, soit quelques milliers à quelques dizaines de milliers d'euros en location |
| Équipe rouge (implantation et scellement du sabotage, piste 5) | Plusieurs semaines-personnes |

L'équipe rouge est probablement le vrai coût limitant (HYPOTHÈSE).

**Ordre d'exécution.** Le duel 1 conditionne les autres :
- **H_B au duel 1** : on abandonne la sonde de valeur précoce et on ne garde que le jumeau et la dopamine.
- **H_B au duel 2 aux couches tardives** : l'article n'apporte rien au programme au-delà d'un détecteur d'erreurs.
- **H_B au duel 4** : tout signal retenu doit être assorti d'une rotation des sondes et d'un budget de réentraînement.

**Ce que je ne prétends pas.** Aucun des duels n'a été exécuté. Toutes les prédictions de cette cellule sont des HYPOTHÈSES. Ma prédiction la plus exposée est que la valeur au prompt aux couches 2-4 ne détecte pas le déclencheur caché (duel 2) : elle est réfutée si le taux de détection y est ≥ 30 % (illustratif).

FIN-DE-CELLULE