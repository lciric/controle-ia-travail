# Trois articles, une problématique commune ? Note de sortie du collisionneur (question générale, jumeau isolé)

- **Date :** 2026-11-22, 18:46 UTC.
- **Dossier :** `runs/collisionneur-protocole-x-generale-isole-jumeau-abonnement-v1-20261122-142638`.
- **Accord :** GO-2026-11-22-73.
- **Dépense :** 5,31 USD par l'interface de programmation, sur une ligne de 45 USD (cellules d'Argon, d'Astra et de Carbon). Les cellules de Claude (Fable et Opus) passent par l'abonnement et ne sont pas facturées.
- **Incident :** la cellule de Fable du troisième tour a été rejouée après un échec de quota. La première tentative n'était « jamais partie » ; le contenu n'en est pas affecté. La cellule d'Opus du troisième tour s'ouvre sur une ligne de service (« Fichier lu en entier… »), sans incidence non plus.
- **Rédaction :** un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier.

Aucune cellule ne rapporte de mesure. Tout ce qui suit est conception, calcul sous hypothèses ou prédiction. Les chiffres viennent des modèles, qui les qualifient presque tous d'illustratifs, et aucun n'est établi. Une source est indiquée pour chaque affirmation importante : lettre du modèle et tour (« Fable, III.3 »).

## 1. La question

Des agents de langue mènent de longues tâches de recherche ou d'analyse. Un adversaire, qui peut être l'agent lui-même, dégrade le résultat par des actes dont aucun n'est suspect isolément. Le défenseur dispose de quatre instruments :

- des moniteurs qui lisent le texte produit ;
- des moniteurs qui lisent les activations internes ;
- quelques exécutions de comparaison ;
- quelques vérifications coûteuses.

Une équipe prépare trois articles dans ce cadre : un agent seul pendant une longue tâche, plusieurs copies d'un même modèle qui travaillent ensemble, et les moniteurs eux-mêmes quand l'adversaire les vise. Une problématique d'ensemble rendrait-elle ces trois articles plus utiles ensemble que séparément ? Si oui, laquelle ? Chaque modèle devait donner une question de recherche, une réponse réfutable, l'antériorité la plus proche, une expérience de deux mois sur un modèle ouvert de huit milliards de paramètres, et le type de sa contribution.

## 2. En bref

**Ce que le dossier répond.** Aucun modèle ne tranche d'avance. Les cinq rendent la réponse conditionnelle à une épreuve. Ils proposent quatre fils communs différents :

- une loi d'échelle qui prédit d'un régime à l'autre (Fable) ;
- une comptabilité des témoins corrélés (Opus) ;
- un déplacement de la signature d'un canal à l'autre (Argon et Carbon) ;
- un critère commun pour placer les vérifications (Astra).

Fable, Opus et Astra prévoient explicitement l'issue « banc partagé, articles distincts » (III.3). Fable juge que l'issue la plus probable est celle de trois articles distincts sur un banc commun (Fable, III.3).

**Trois décisions de méthode ressortent des critiques :**

- **Mesurer d'abord, sans adversaire, le bruit honnête et ses covariances.** Cette mesure porte sur les pas de temps, les copies et les instruments. On ne passe la porte de faisabilité du sabotage diffus qu'ensuite, contre un adaptateur bénin de même rang.
- **Décider si les copies forment un régime à part.** On compare des copies de mêmes poids à un modèle d'une autre famille, sur des étapes d'égale influence, en excès de ce que la tâche explique seule.
- **Ne juger une « unification » qu'à menu et adaptativité égaux.** La politique commune doit battre une politique qui dispose des mêmes instruments, du même calendrier d'achat et de la structure de la tâche, mais pas du lien supposé entre articles.

## 3. Ce que chaque modèle a proposé

### Claude Fable 5.2 (lettre A)

- **Proposition centrale (III.1).** Une seule grandeur gouvernerait le dégât accumulable sans alerte : l'évidence par acte que les instruments extraient, agrégée sur la trajectoire. Les trois articles ne vaudraient plus ensemble que si des paramètres mesurés sur un agent seul et sur des tâches courtes prédisent, sans réajustement, la frontière entre dégât et détection dans les trois régimes : tâches longues, copies, moniteurs visés. C'est son sixième duel. Fable propose deux régimes pour le nombre maximal d'actes dégradés sans alerte :
  - linéaire en longueur sans comparaison ;
  - en racine carrée avec comparaison appariée.

  Il estime le succès de la prédiction croisée à environ 40 % (probabilité subjective). Coût avancé : 1 000 à 3 000 dollars.
- **Après les critiques (III.3).** Fable fait cinq changements principaux :
  - la frontière se mesure en dégât et non en nombre d'actes ; la dose de sabotage est assignée et croisée avec la longueur ;
  - son ancien duel sur l'appariement est supprimé : l'issue y était fixée par la manipulation ;
  - un nouveau premier duel mesure, sur l'honnête seul, l'exposant de croissance du bruit, avec deux références réalisables : exécutions depuis l'origine, rééchantillonnage de chaque étape depuis le préfixe courant ;
  - il retire « des copies se coordonnent sans communiquer » : l'accord entre copies indépendantes mesure la dispersion des propensions par étape, pas une coordination ;
  - le prédicteur final ne doit plus rien emprunter aux régimes cibles.

  Il abaisse sa probabilité de succès à environ 25 % et attend un échec aux duels 1, 3 et 4.

### Claude Opus 5.5 (lettre B)

- **Proposition centrale (III.1).** Les trois articles mesureraient la même chose : combien de témoins indépendants le défenseur possède réellement. Ces témoins sont les pas de temps (article 1), les copies, y compris les exécutions de comparaison (article 2), et les moniteurs (article 3). Trois paramètres suffiraient : la sensibilité d'un témoin seul, la corrélation des erreurs entre témoins, et un exposant qui relie dommage et signal. L'unification exigerait deux choses : que ces paramètres prédisent la détection (duel 5) et qu'ils changent une décision d'allocation (duel 6). Modèle principal Qwen3-8B, réplication sur Llama-3.1-8B-Instruct ; 1 000 à 1 500 dollars.
- **Après les critiques (III.3).** Opus accepte que son duel 5 « ne pouvait guère échouer » : une loi de puissance libre l'imite à 2,5 % près sur les effectifs prévus (critique de Fable, III.2). Désormais :
  - tous les paramètres sont mesurés sur des paires au plus, et la prédiction porte jusqu'à seize témoins, où les deux lois s'écartent de 31 % à 39 % ;
  - il retire « trois paramètres communs » au profit d'une « comptabilité » : la valeur du témoin suivant se calcule à partir de son décalage propre et de sa covariance avec les témoins présents, classe par classe ;
  - il retire son attente sur la corrélation des comparaisons, vraie par construction : deux divergences calculées contre la même cible sont corrélées à un demi sans aucun effet des poids (critique de Carbon, III.2) ;
  - il compare sa politique d'achat à la même politique sans corrélation et à une répartition fixe, à menu identique.

  Il attend surtout un gain venant de l'achat d'un moniteur d'une autre famille plutôt que de rééchantillons supplémentaires.

### Argon (identifiant gemini-4-argon, lettre C)

- **Proposition centrale (III.1).** Une « loi de conservation » de la signature de sabotage. Pour dégrader une longue tâche par petits actes, l'agent doit garder une direction de dérive, et cette mémoire réside dans le texte, dans les activations ou dans les poids partagés par les copies. Effacer la signature d'un canal la reporterait mécaniquement sur un autre : c'est le « vase communicant ». S'y ajoute une cascade d'audit : les signaux continus déclenchent les comparaisons, qui filtrent avant les vérifications coûteuses. Quatre duels ; 800 à 1 050 dollars.
- **Après les critiques (III.3).** Argon distingue la part démontrable de la part empirique :
  - la divergence totale de la trace ne peut s'annuler si la conclusion change (identité de théorie de l'information, critique de Fable, III.2) ;
  - qu'un moniteur de capacité bornée la capte reste à tester.

  Corrections :
  - il supprime le filtrage a posteriori des saboteurs ;
  - il munit tous les bras d'un adaptateur de même rang ;
  - il remplace le bruit injecté dans les activations par une perturbation du contexte (paraphrase par un modèle tiers, ordre des pièces) ;
  - il lit la divergence entre copies dans les deux sens : excès de divergence, ou concentration anormale des conclusions ;
  - il entraîne l'adversaire contre la classe même de sondes du défenseur, avec un contrôle positif d'évasion sur un sabotage en une étape ;
  - il compare sa cascade à une cascade aussi adaptative, mais sans lien entre canaux ;
  - il réserve 10 % des vérifications à un tirage au hasard.

  Sa prédiction de couplage reste inchangée.

### Astra (identifiant gpt-6.2-astra, lettre D)

- **Proposition centrale (III.1).** Le lien entre articles ne serait pas un phénomène commun mais un critère commun : la perte qu'une vérification permettrait d'éviter, par unité de budget. Une règle apprise sur deux régimes choisirait-elle où vérifier dans le troisième, presque aussi bien qu'un spécialiste et mieux qu'une règle mécanique, jugée sur le pire régime ? Pas d'adversaire entraîné : des perturbations placées par l'expérimentateur. Deux duels ; 600 euros.
- **Après les critiques (III.3).** Astra retire son duel sur la suradditivité des erreurs : son signe était fixé par la règle de notation (critiques d'Argon et Carbon, III.2). Il restreint le transfert à une décision identifiable : quelle pièce faire vérifier quand il reste une seule inspection et que l'agent, non un programme de recalcul, terminera le travail. Désormais :
  - l'agent produit lui-même ses notes sous une consigne biaisée ;
  - la décision porte sur un générateur de dossiers et une famille adverse inconnus de la règle ;
  - parmi les règles mécaniques à battre figure un allocateur qui connaît la topologie exacte des dossiers, sans les signaux des moniteurs.

  Il veut un pilote d'abord, qui fixe les effectifs avant tout test.

### Carbon (identifiant gemini-4-carbon, lettre E)

- **Proposition centrale (III.1).** La question serait celle de la séparabilité du problème d'allocation. Dans un régime modulaire, les trois défenses se composent. Dans un régime couplé, contourner les moniteurs locaux déplacerait l'anomalie vers la sensibilité de l'agent à son historique, et vers la divergence entre copies cloisonnées. La revue mutuelle ouverte entre copies d'un même modèle serait neutralisée par leurs angles morts communs. Quatre duels ; environ 2 350 dollars.
- **Après les critiques (III.3).** Carbon accepte que « non significatif » ne vaut pas réfutation : chaque duel comporte désormais une issue « non concluant ». Il remplace le « résumé factuel neutre », qui supposait la vérité connue, par un « registre extractif » déterministe sans clé. Autres changements :
  - un adaptateur bénin de même rang sert de témoin honnête ;
  - un contrôle de concentration exige qu'aucun acte ne porte plus de 30 % du dégât ;
  - au duel des copies, les bras reçoivent le même corpus et seul le partage des raisonnements varie ; une équipe hétérogène sert de témoin ;
  - la politique commune est opposée à un ordonnanceur séquentiel additif, à historiques et budget égaux.

  Il intègre comme test l'objection d'Argon : si le biais vit dans les poids et non dans l'historique, son instrument contrefactuel ne le voit pas, et son duel 2 l'établira.

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Le banc.** Les cinq proposent des tâches synthétiques d'analyse ou de synthèse documentaire à vérité calculable. Quatre prennent Llama-3.1-8B-Instruct comme agent principal ; Opus prend Qwen3-8B, avec réplication sur Llama (III.1).
- **L'antériorité.** Les cinq citent Greenblatt, Shlegeris, Sachan et Roger pour le cadre du contrôle. Quatre en font l'antériorité la plus proche ; Fable lui préfère Wen et coll. sur les menaces réparties (III.1).
- **La porte de faisabilité.** Quatre posent en premier une question préalable : un modèle de huit milliards de paramètres sait-il dégrader une tâche de façon diffuse sans acte visible (Fable, Opus, Carbon III.1 ; Argon dans ses issues sans intérêt). Astra n'en pose pas, faute d'adversaire.
- **Les copies de mêmes poids.** Les cinq notent qu'une comparaison produite par le même modèle peut partager son biais et n'est pas une référence sûre (Fable, Opus, Argon, Carbon, Astra, III.1).
- **Le caractère conditionnel de la réponse.** Chacun définit une issue où les articles restent distincts. Fable, Opus et Astra disent en toutes lettres que partager un banc n'est pas partager une problématique ; Carbon parle d'une unification « seulement éditoriale ».

### Convergences nées des critiques

- **Le témoin d'adaptateur.** Plusieurs critiques montrent qu'une sonde peut lire l'adaptateur ou la consigne plutôt que le sabotage (Opus sur Fable ; Fable, Opus et Carbon sur Argon ; Opus sur Carbon, III.2). Fable, Argon et Carbon adoptent un adaptateur neutre ou bénin de même rang, et Opus garde son organisme sans déclencheur et un affinage factice (III.3). Astra contourne la question en lisant des décisions générées par l'agent.
- **L'accord entre copies.** Astra et Carbon montrent que des copies indépendantes dégradent souvent les mêmes étapes par simple hétérogénéité des étapes : l'accord ne prouve pas une coordination (III.2). Fable l'accepte et Opus applique la même objection à son propre duel (III.3). Les deux arrivent alors à un test voisin, développé au § 7.
- **Le comparateur équitable.** Les cinq critiques reprochent aux propositions d'unification de battre des comparateurs plus pauvres :
  - Opus comparait sa politique à une politique limitée aux instruments d'un seul article ;
  - Argon opposait une cascade adaptative à des fractions fixes ;
  - Carbon opposait sa politique à une régression tardive sur scores finaux.

  Au tour III.3, Opus, Argon et Carbon adoptent tous un comparateur de même menu et de même adaptativité.
- **L'issue indécise.** Fable, Opus, Astra et Carbon finissent par déclarer « non tranché » un intervalle qui chevauche la frontière, au lieu de l'attribuer à une hypothèse (III.3).

### Désaccords

- **Le fil commun.** Les quatre cadrages du § 2 restent distincts au tour III.3. Fable attend plutôt des articles séparés. Argon et Carbon attendent un couplage. Opus attend un gain modeste de sa comptabilité. Astra attend un transfert de sa règle d'allocation.
- **Ce que les activations peuvent porter de plus que le texte.** Carbon objecte qu'un transformeur ne garde aucun état récurrent hors du contexte et des poids : la sonde ne lirait que l'adaptateur ou la consigne (III.2). Argon rejette la conclusion : les activations recalculent tout le préfixe à chaque étape et peuvent agréger des indices dispersés. Il accepte en revanche le contrôle d'adaptateur (III.3). Le désaccord porte sur une hypothèse que les deux rendent testable.
- **La furtivité imposée par l'entraînement.** Opus soutient que pénaliser la divergence de Kullback-Leibler par étape rend la furtivité textuelle vraie par construction (III.2). Carbon rejette : rien ne garantit qu'un modèle de cette taille garde l'impact sous cette pénalité, et la pénalité porte sur un préfixe déjà dégradé (III.3).
- **La divergence entre copies de même loi.** Argon soutient que des copies toutes saboteuses ne divergent pas en moyenne, ce qui rend la sous-détection acquise (III.2). Fable répond que, pour des actes localisés et une divergence non signée, deux copies indépendantes divergent avec une probabilité 2p(1 − p), contre p face à une référence honnête, donc davantage tant que p reste sous un demi (III.3). Opus accepte la même critique pour son propre duel, qui portait sur la conclusion (III.3).
- **L'effet d'actes conjoints sur l'exposant d'Opus.** Carbon affirme qu'une porte « et » fait tomber à zéro le dommage attribué à chaque acte. Opus répond que c'est l'inverse : chaque acte reçoit tout le dommage, ce qu'Argon écrivait aussi. Le zéro vaut pour des actes redondants (porte « ou »). Opus supprime de toute façon cette attribution (III.2, III.3).
- **Faut-il prouver une coordination entre copies ?** Fable et Opus en font l'objet de leur duel (poids ou tâche). Astra refuse cette exigence : seul compte ce que vaut une inspection, qu'un accord erroné vienne d'une coordination ou d'une même erreur de lecture (III.3).
- **Un adversaire entraîné contre la politique commune.** Fable le demande à Carbon (III.2). Carbon le refuse pour raison de budget, mais fait imiter par l'adversaire la loi honnête des scores (III.3).
- **Une date.** Greenblatt et al. : 2023 chez Opus et Astra, 2024 chez Fable, Argon et Carbon (prépublication puis publication, à vérifier).

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, par rapport à ce que les modèles citent eux-mêmes comme connu

Les modèles tiennent pour connus :

- la loi en racine carrée des communications furtives et de la stéganographie ;
- l'effet de plan sous corrélation (Kish) ;
- l'échec corrélé de versions logicielles indépendantes (Knight et Leveson) ;
- l'analyse séquentielle (Wald, Page) ;
- le cadre du contrôle et le rééchantillonnage d'agents ;
- le contournement de sondes ;
- la supériorité générale d'une cascade séquentielle sur une allocation fixe (Carbon et Argon, III.2 et III.3).

Pourraient rester propres, selon leurs auteurs et sans vérification :

- **la prédiction croisée stricte** : des paramètres mesurés sur un agent seul en tâches courtes, gelés, prédisant les trois régimes, contre une loi libre et contre un spécialiste (Fable) ;
- **la comptabilité des témoins** mesurée sur des paires et éprouvée jusqu'à seize témoins, puis jugée par sa valeur décisionnelle à menu identique (Opus) ;
- **le test de la concentration des dégradations entre copies**, poids contre tâche (Fable, Opus, III.3) ;
- **la lecture dans les deux sens de la divergence entre copies** sous perturbation du contexte, et le contrôle positif d'évasion en une étape qui sépare la faiblesse de l'optimiseur du coût de coordination (Argon) ;
- **le registre extractif sans clé** comme référence contrefactuelle, et la comparaison entre débat ouvert et raisonnement cloisonné à corpus égal (Carbon) ;
- **le transfert de la dernière inspection** vers un régime et un générateur inconnus, contre un allocateur qui connaît la topologie exacte (Astra).

Aucun modèle n'affirme une nouveauté établie. Tous renvoient à une recherche bibliographique qu'ils n'ont pas faite.

### Fragile

- **La prémisse.** Qu'un modèle de huit milliards de paramètres sache saboter de façon diffuse reste une hypothèse pour les cinq. Leurs plans s'arrêtent si la porte de faisabilité échoue.
- **Les organismes modèles.** Sabotages plantés, consignes et adaptateurs bornent un cas construit. Opus le dit : ses paramètres « ne bornent rien » face à un adversaire qui se comporterait autrement en calibration et en déploiement (III.1).
- **L'oracle.** Sur banc synthétique, la vérification est exacte par construction. Argon et Carbon prévoient un audit humain de 200 étapes, aucun ne mesure un vérificateur réel sur une tâche ouverte.
- **La puissance.** Plusieurs critères conjoints sont peu puissants :
  - le duel de transfert d'Astra se décide sur un minimum de six contrastes. Argon calcule, sur des valeurs illustratives, qu'il faudrait de l'ordre d'un millier de dossiers par régime, contre environ 150 dans l'enveloppe initiale d'Astra (III.2). Astra répond par un pilote qui dimensionne avant de geler (III.3) ;
  - Fable écrit que « non tranché » est une issue probable de son duel final (III.3).
- **Une règle de décision d'Argon.** *Remarque du rédacteur, tirée du texte d'Argon, III.3.* Argon supprime les zones indécises par un seuil unique. Mais il attribue à une hypothèse tout intervalle qui ne passe pas entièrement au-delà de ce seuil. C'est la règle que Fable, Opus et Astra reprochaient à Carbon au tour III.2 : un essai trop petit y donne mécaniquement un verdict.
- **Le vase communicant.** Même avec un adversaire entraîné contre la classe de sondes du défenseur et un contrôle positif en une étape, une recherche finie ne prouve pas l'impossibilité d'une évasion. Fable et Opus le signalaient (III.2).
- **Des statuts.** Plusieurs cellules du premier tour marquent « vérifié » des références citées de mémoire ou des conséquences de seuils illustratifs (Carbon pour Wald, Argon). Les critiques l'ont relevé, Carbon l'acte (III.3).
- **Les calculs.** Les identités dites vérifiées sont de l'algèbre faite par les modèles. Le rédacteur en a refait quatre et trouve les mêmes valeurs :
  - 1 − 0,95²⁵ ≈ 72 % ;
  - 1 − 0,99ᵀ ≈ 18 % à 45 % pour T de 20 à 60 ;
  - l'écart de 2,5 % (Fable, III.2) ;
  - les écarts de 31 % et 39 % (Opus, III.3).

  Les autres ne sont pas contrôlés.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des références, des auteurs ou des années.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Greenblatt, Shlegeris, Sachan, Roger (2023 ou 2024), « AI Control: Improving Safety Despite Intentional Subversion » | les cinq | Cadre du contrôle, budget d'audit |
| Wen, Hebbar, Larson et coll. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » | Fable, Opus | Antériorité la plus proche selon Fable (menaces réparties) |
| Bhatt et coll. (2025), « Ctrl-Z: Controlling AI Agents via Resampling » | Fable, Opus | Rééchantillonnage comme exécution de comparaison |
| Bash, Goeckel, Towsley (2013), « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels » | Fable | Loi en racine carrée transposée |
| Ker, Pevný, Kodovský, Fridrich (2008), « The Square Root Law of Steganographic Capacity » | Fable | Même loi, en stéganographie |
| Page (1954), « Continuous Inspection Schemes » | Fable | Détection de rupture par somme cumulée |
| Wald (1945), « Sequential Tests of Statistical Hypotheses » | Carbon | Analyse séquentielle |
| Bailey et coll. (2024), « Obfuscated Activations Bypass LLM Latent-Space Defenses » | Fable, Opus | Sondes contournées quand elles sont visées |
| Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), « Detecting Strategic Deception Using Linear Probes » | Fable | Sondes linéaires de tromperie |
| Baker et coll. (2025), « Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation » | Opus | Obfuscation induite par la pression d'un moniteur |
| Burns, Ye, Klein, Steinhardt (2023), « Discovering Latent Knowledge in Language Models Without Supervision » | Argon | Sondes sur représentations internes |
| Roger, Greenblatt (2023), « Preventing Language Models From Hiding Their Reasoning » | Argon | Dissimulation dans le texte, paraphrase |
| Irving, Christiano, Amodei (2018), « AI Safety via Debate » | Carbon | Copies en débat devant un juge |
| Kish (1965), « Survey Sampling » | Opus | Effet de plan sous corrélation |
| Ladha (1992), « The Condorcet Jury Theorem, Free Speech, and Correlated Votes » | Opus | Votes corrélés |
| Knight, Leveson (1986), « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming » | Opus | Échecs corrélés de versions indépendantes |
| Fisher (1936), « The Use of Multiple Measurements in Taxonomic Problems » | Opus (III.3) | Discriminant linéaire |
| Hanley, McNeil (1982), « The Meaning and Use of the Area under a Receiver Operating Characteristic (ROC) Curve » | Fable (III.2) | Variance de l'aire sous la courbe |
| Un résultat sur la capacité furtive linéaire quand la référence est mal connue, sans auteurs | Fable | Référence non attribuée |
| Un résultat de restriction d'étendue sous sélection, sans auteurs | Opus (III.3) | Transfert de l'évasion du texte vers la sonde |

Les noms de modèles ouverts cités (Llama-3.1-8B-Instruct, Qwen3-8B, Qwen2.5-7B-Instruct, Gemma-2-9B, Mistral-7B-Instruct, Ministral-8B-Instruct, Llama-3.1-70B et Llama-3.3-70B) sont aussi à vérifier : disponibilité et licence.

## 7. Propositions retenues et non retenues

### Retenues

1. **Mesurer d'abord le bruit honnête et ses covariances, sur les trois axes, sans adversaire.**
   - *Contenu.* Exposant de croissance du bruit honnête avec une référence réalisable (Fable, duel 1, III.3). Covariances honnêtes entre pas, entre copies jusqu'à seize, entre instruments, et validation des estimateurs sur données synthétiques (Opus, III.3).
   - *Soutien croisé.* Opus, Argon, Astra et Carbon montrent qu'un bruit honnête à mémoire longue produit seul un exposant au-dessus d'un demi (III.2). Fable en fait sa première expérience. Opus mène la mesure des covariances honnêtes en parallèle de sa porte d'entrée (III.3).
   - *Faisabilité.* Ni adversaire ni adaptateur : c'est la moins chère du dossier, et toute la suite en dépend. Elle tranche une issue sans intérêt nommée par Fable : aucune référence ne descend sous l'exposant critique, et seules les vérifications coûteuses comptent.

2. **Passer la porte de faisabilité du sabotage diffus contre un adaptateur bénin de même rang, avec un contrôle positif.**
   - *Contenu.* Le dégât, une furtivité par acte en contraste interne à la politique, une contrainte de concentration et une version « dormante » de la politique (Fable, duel 2). L'excès de bascule dirigée sur des erreurs aveugles (Opus, duel 1). Une porte qui exige que les moniteurs détectent un sabotage concentré de même impact (Carbon, duel 1).
   - *Soutien croisé.* Fable, Opus et Carbon en font un duel, et Argon la nomme parmi ses issues sans intérêt. Quatre critiques (Fable, Opus, Astra, Carbon) exigent un témoin d'adaptateur ou d'affinage. Fable, Argon et Carbon l'adoptent ; Opus garde un affinage factice.
   - *Ce qu'elle tranche.* Si elle échoue, les plans de Fable, Opus et Carbon s'arrêtent, et la question ne vaut plus que pour un adversaire scripté.

3. **Décider si les copies forment un régime à part : mêmes poids contre autre famille, sur des étapes d'égale influence, en excès de l'indépendance conditionnelle à l'étape.**
   - *Soutien croisé.* Fable (duel 4) et Opus (duel 3) arrivent au tour III.3 à deux tests presque identiques, à partir des critiques d'Astra et de Carbon sur l'accord entre copies. Carbon ajoute le témoin d'équipe hétérogène (III.3).
   - *Ce qu'elle tranche.* L'objet propre de l'article sur les copies. Elle dit aussi si une comparaison faite par le même modèle vaut une comparaison faite par un autre, ce dont dépendent les quatre autres plans.
   - *Point faible.* Elle ne couvre pas des copies qui lisent leurs sorties respectives (Fable, III.3).

4. **Juger toute unification à menu, historique et adaptativité égaux, contre la structure de la tâche.**
   - *Contenu.* La politique commune doit battre :
     - la même politique sans le lien supposé (Opus, duel 6) ;
     - une cascade aussi adaptative, mono-canal ou à signaux permutés dans la même strate (Argon, duel 4) ;
     - un ordonnanceur séquentiel additif (Carbon, duel 4) ;
     - un allocateur qui connaît la topologie exacte (Astra, III.3).
   - *Soutien croisé.* C'est la convergence la plus large des critiques : les cinq modèles l'ont soulevée ou adoptée.
   - *Ce qu'elle tranche.* C'est l'épreuve qui répond directement à « ensemble ou séparés ». Sans elle, un gain mesure seulement l'accès à plus d'instruments ou le droit de différer un achat.
   - *Point faible.* La puissance : ces contrastes exigent des effectifs élevés. Le pilote d'Astra, qui dimensionne avant de geler, est la bonne manière de l'aborder.

### Non retenues

- **Le nombre d'actes et l'exposant comparé à un demi (Fable, III.1).** Le nombre d'actes confond défenseur et adversaire, et l'exposant d'un demi est vrai par construction sous tirages indépendants. Retiré par son auteur.
- **La formule à corrélation constante sur l'axe du temps et « trois paramètres communs » (Opus, III.1).** Le duel ne pouvait guère échouer. Retiré.
- **L'attente d'une corrélation forte entre comparaisons (Opus, III.1).** Vraie par construction, puisque toutes les divergences partagent la même cible. Retirée.
- **L'estimation de l'exposant acte par acte, par rejeu et régression en logarithmes (Opus, III.1).** Troncature, atténuation et non-additivité. Supprimée.
- **Le filtrage des saboteurs sous un centile du moniteur texte, et le bruit orthogonal aux activations honnêtes (Argon, III.1).** Sélection asymétrique et artefact géométrique. Remplacés.
- **Les comparateurs faibles : fractions fixes (Argon) et régression tardive sur scores finaux (Carbon, III.1).** Ils mesurent l'adaptativité, pas le lien entre articles. Remplacés.
- **Le « résumé factuel neutre » (Carbon, III.1).** Il suppose la vérité connue, ou porte le biais s'il est écrit par l'agent. Remplacé par un registre extractif, dont la validité reste à éprouver.
- **Le duel de suradditivité des erreurs (Astra, III.1).** Son signe était fixé par la règle de notation. Retiré.
- **Le moniteur visé réduit à un changement de présentation (Astra, III.1).** Le format se confondait avec l'exposition. Transformé.
- **Le vase communicant d'Argon, comme première expérience.** L'entraînement adverse contre des sondes non linéaires est coûteux et dépend d'un optimiseur, et une recherche finie ne prouve pas une impossibilité. À reprendre après les quatre retenues, avec son contrôle positif en une étape.
- **Le débat ouvert contre le raisonnement cloisonné (Carbon, duel 3).** L'idée est neuve, mais son hypothèse est conjointe et sa puissance limitée. À reprendre une fois tranché le duel des copies.
- **Le test complet de transfert sur le pire régime (Astra).** Il n'est pas retenu tant que le pilote n'a pas fixé les effectifs ; Astra le dit lui-même. Son allocateur fondé sur la topologie exacte est en revanche repris comme comparateur dans la proposition retenue 4.
