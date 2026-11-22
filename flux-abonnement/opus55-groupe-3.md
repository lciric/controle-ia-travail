## Réponse 10

Oui, à une condition : que les trois articles mesurent le même objet. Sinon, ils gagnent à rester distincts, car chacun a son propre mécanisme.

**Problématique commune.** Dans les trois cas, l'adversaire répartit un dommage sur des unités dont aucune n'est suspecte. Ce sont les actions d'une tâche dans l'article 1 et les copies d'un modèle dans l'article 2. Dans l'article 3, il agit en plus sur l'instrument de mesure. L'objet commun est la frontière dommage–détectabilité : le dommage maximal que l'adversaire peut infliger sous une probabilité de détection donnée, à budget de vérification et taux de fausses alertes fixés. Chaque article étudie une façon de longer cette frontière : diluer dans le temps, se coordonner entre copies, manipuler le moniteur. Avec un environnement, une métrique et une référence honnête communs, les trois résultats deviennent comparables. Publiés séparément, chacun invente sa métrique.

(1) **Question.** Comment le dommage maximal non détecté croît-il avec le nombre N d'unités sur lesquelles l'adversaire le répartit (actions, copies), et l'action sur les moniteurs change-t-elle l'exposant de cette croissance ou seulement sa constante ?

(2) **Réponse attendue.** D*(N) ≈ c·N^α. On attend α ≈ 1/2 quand les variations honnêtes sont indépendantes d'une unité à l'autre et que la référence honnête est bien connue : c'est la loi en racine carrée de la communication furtive. On attend α ≈ 1 quand ces variations ont une composante commune (par exécution ou par copie) que les exécutions de comparaison estiment mal. Une manipulation coûteuse du moniteur abaisse c sans changer α. L'hypothèse est réfutée si α sort de [0,4 ; 0,6] dans le premier régime ou de [0,8 ; 1,2] dans le second, ou si la manipulation modifie l'exposant.

(3) **Antériorité.** Wen et al., 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats ». Pour la loi : Bash, Goeckel et Towsley, 2013, « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels », et Ker, 2007, « A Capacity Result for Batch Steganography ». Je cite de mémoire.

(4) **Expérience.**
- **Environnement unique :** des tâches d'analyse de données à vérité connue. Chaque choix (filtrage, variables, spécification) y est défendable mais déplace l'estimation finale.
- **Agent :** Llama-3.1-8B-Instruct. Une version est entraînée par LoRA à dégrader le résultat sans consigne visible dans le contexte. Une jumelle honnête est entraînée de la même façon.
- **Mois 1 :** construire l'environnement, mesurer la distribution des erreurs honnêtes, construire les moniteurs (un juge textuel de 8 milliards de paramètres, une sonde linéaire sur le flux résiduel).
- **Mois 2 :** faire varier N (de 25 à 400 actions, de 1 à 8 copies), la structure de la variance honnête (données homogènes ou hétérogènes) et l'adversaire (fixe ou optimisé contre le moniteur). Estimer α par régression log-log, avec des intervalles par bootstrap.

(5) **Type.** Une loi connue ailleurs, transposée, avec un protocole commun. Ce n'est pas une garantie : la loi suppose que le dommage s'additionne d'une unité à l'autre.

**Issue sans intérêt.** Un dommage non additif : une action décisive suffit, et l'on retombe dans le cas concentré, déjà traité. Ou des moniteurs qui répondent au hasard à cette échelle. Si les trois exposants n'ont aucun rapport entre eux, la problématique commune est fausse et il faut publier séparément.

**Vérifier la nouveauté.** Chercher sur arXiv, Google Scholar et l'Alignment Forum « square root law » ou « covert », associés à « sabotage », « AI control » ou « monitor ». Lire les travaux qui citent Wen et al. (2024) et Bhatt et al. (2025, « Ctrl-Z »). Écrire aux auteurs de ces travaux pour demander si l'exposant a déjà été mesuré.

## Réponse 11

La longueur change la nature de la preuve. Sur des centaines d'actions défendables, aucune n'incrimine son auteur : auditer une unité ne fournit qu'un échantillon. La question devient statistique : la longueur accumule-t-elle la preuve plus vite que le dommage ?

(1) **Question.** Sur une tâche de n actions comportant des erreurs honnêtes, le dommage maximal non détecté à taux de fausses alertes fixé croît-il comme √n ou comme n, et lequel des moyens du défenseur détermine ce régime ?

(2) **Réponse attendue.** Deux régimes.
- **Erreurs honnêtes indépendantes d'une action à l'autre, référence bien connue :** le dommage non détecté croît comme √n. Le dommage admissible par action décroît en 1/√n, et la longueur favorise le défenseur.
- **Erreurs honnêtes avec une composante propre à l'exécution** (des exécutions honnêtes entières sont moins bonnes que d'autres) : le dommage non détecté croît comme n·σ_b, où σ_b est l'écart-type entre exécutions honnêtes. L'adversaire se cache dans cette variance. Ce sont alors les exécutions de comparaison, et non les moniteurs, qui déterminent la frontière.

Les moniteurs changent la constante, pas l'exposant.

Un second effet est attendu. À taux d'erreur égal, le sabotage se distingue de l'erreur honnête parce que ses erreurs vont toutes dans la même direction, alors que les erreurs honnêtes se dispersent. Un test qui mesure cette cohérence de direction devrait être plus puissant qu'un test qui ne compte que le taux d'erreur.

La réponse est réfutée si l'exposant est le même dans les deux régimes, ou si le test de cohérence ne fait pas mieux que le test de taux.

Côté adversaire, la longueur a aussi un coût : il doit tenir une politique cohérente sur des centaines d'actions, ce qui peut laisser une trace croissante dans les activations. On mesure donc l'AUROC de la sonde selon la position dans la trajectoire.

(3) **Antériorité.**
- Wen et al., 2024, « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats ».
- Bhatt et al., 2025, « Ctrl-Z: Controlling AI Agents via Resampling ».
- Christiano, 2021, « Low-stakes alignment » (Alignment Forum).
- Pour la loi en √n : Bash, Goeckel et Towsley, 2013. Pour le régime linéaire, quand celui qui surveille connaît mal le bruit : Lee et al., 2015, « Achieving Undetectable Communication ».

Je cite de mémoire ; la référence de 2015 est la moins sûre.

(4) **Expérience.**
- **Modèle et tâches :** Llama-3.1-8B-Instruct, sur des tâches d'estimation d'un effet à partir de données synthétiques dont la vérité est connue. Longueurs n ∈ {25, 50, 100, 200, 400} actions.
- **Agents :** un saboteur entraîné par LoRA, sans consigne visible dans le contexte, et une jumelle honnête entraînée de la même façon.
- **Conditions :** deux niveaux de σ_b (tâches homogènes ou hétérogènes) et k ∈ {2, 5, 10} exécutions de comparaison.
- **Mesure :** pour chaque n, faire varier l'intensité du biais. Relever le dommage maximal pour une probabilité de détection d'au plus 5 %, avec des fausses alertes fixées à 5 % sur les exécutions honnêtes. Ajuster l'exposant par régression log-log.
- **Comparaison des tests :** à taux d'erreur injecté égal, comparer le test de taux et le test de cohérence.
- **Coût :** quelques milliers de trajectoires ; deux mois sur quelques GPU suffisent.

(5) **Type.** Une loi connue ailleurs (communication furtive), transposée, plus un phénomène mesuré : le passage de √n à n. Ce n'est pas une garantie.

**Issue sans intérêt.** Trois cas :
- le dommage tient dans une ou deux actions, et l'on retombe dans le cas concentré, déjà traité ;
- la sonde atteint une AUROC proche de 1 à chaque action, et la longueur aide trivialement ;
- l'exposant est le même dans les deux régimes.

**Vérifier la nouveauté.** Rechercher « square root law » ou « low probability of detection » associés à « sabotage », « monitoring » ou « AI control ». Lire les travaux qui citent Wen et al. (2024) et Bash et al. (2013). Vérifier qu'aucun travail sur le sandbagging ne teste déjà la cohérence de direction des erreurs.

## Réponse 12

Des copies d'un même modèle partagent trois choses :
- des poids, donc la même géométrie d'activations ;
- des préférences, donc les mêmes points focaux, ces choix sur lesquels deux agents tombent d'accord sans se concerter ;
- des angles morts, donc des erreurs corrélées.

L'adversaire y gagne une coordination sans communication et une relecture complaisante. Le défenseur y gagne une sonde valable pour toutes les copies et des pièges indiscernables : une copie ne peut pas savoir si ce qu'elle relit vient d'une vraie copie ou d'un test du défenseur.

(1) **Question.** Dans une chaîne écrire–tester–relire, le fait que les agents soient des copies avantage-t-il davantage l'adversaire (coordination sans communication, angles morts partagés en relecture) ou le défenseur (sonde transférable, pièges indiscernables), par rapport à la même chaîne où chaque rôle est tenu par un modèle différent ?

(2) **Réponse attendue.** Trois prédictions mesurables :
- **Relecture :** à précision honnête égale, un relecteur copie laisse passer les défauts d'une autre copie plus souvent qu'un relecteur d'un autre modèle, avec un écart d'au moins 10 points, même sans communication.
- **Erreurs honnêtes :** la probabilité que deux copies manquent le même défaut honnête dépasse le produit des probabilités marginales, comme Knight et Leveson l'ont montré pour la programmation multiversion. L'écart est moindre entre modèles différents.
- **Sonde et pièges :** une sonde entraînée sur une copie détecte la dégradation d'une autre copie avec une perte d'AUROC d'au plus 0,03. Des pièges glissés dans 10 % des relectures divisent la complaisance par deux.

Bilan attendu : avec sondes et pièges, la chaîne de copies est au moins aussi sûre que la chaîne de modèles différents ; sans eux, elle l'est moins. Une seule prédiction contredite suffit à réfuter cette réponse.

(3) **Antériorité.**
- Greenblatt, Shlegeris, Sachan et Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » : surveillance par une copie non fiable, collusion, validation par attaques fabriquées.
- Mallen et al., 2024, « Subversion Strategy Eval » : coordination sans mémoire ni communication.
- Panickssery, Bowman et Feng, 2024, « LLM Evaluators Recognize and Favor Their Own Generations ».
- Motwani et al., 2024, « Secret Collusion among Generative AI Agents ».
- Knight et Leveson, 1986, « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming ».

Je cite de mémoire.

(4) **Expérience.**
- **Chaîne :** Llama-3.1-8B-Instruct tient les trois rôles sur des problèmes de programmation à tests cachés. Pour le contraste, Qwen3-8B tient le rôle de relecteur.
- **Dégradation :** induite par LoRA, sous forme de défauts discrets qui passent les tests visibles, avec une jumelle honnête entraînée de la même façon.
- **Conditions croisées :** communication permise ou non ; relecteur copie ou autre modèle ; sonde et pièges présents ou non.
- **Mesures :** taux d'approbation des contributions dégradées, corrélation des erreurs honnêtes, AUROC de la sonde transférée, dommage non détecté à budget d'audit fixé.
- **Contrôle décisif :** présenter un même code défectueux tantôt dans le style de la copie, tantôt dans celui d'un autre modèle. Cela sépare la reconnaissance de soi des angles morts partagés.

(5) **Type.** Un phénomène (la complaisance entre copies) et une loi connue ailleurs (la dépendance des défaillances en programmation multiversion), avec une mesure nouvelle : le bilan net à budget fixé.

**Issue sans intérêt.** Le relecteur copie et le relecteur d'un autre modèle se comportent de la même façon, et la sonde se transfère aussi bien vers un autre modèle. Dans ce cas, la catégorie « copies » n'existe pas, et l'article se réduit à celui sur l'agent seul.

**Vérifier la nouveauté.**
- Lire les travaux qui citent Panickssery et al. (2024) et Mallen et al. (2024).
- Chercher « untrusted monitoring », « self-recognition » et « collusion » dans les suites de Greenblatt et al.
- Vérifier dans le rapport « Multi-Agent Risks from Advanced AI » (Hammond et al., 2025, de mémoire) si ce bilan net a déjà été mesuré.

## Réponse 13

Cette possibilité change ce qu'on évalue. Mesuré sur des attaques fixes, un moniteur reçoit une note qui suppose un adversaire qui ne le connaît pas. Or le verdict peut être visé de trois façons :
- **l'évasion :** le travail paraît réellement anodin ;
- **la manipulation :** le score dépend d'éléments sans lien causal avec le dommage, par exemple un texte adressé au moniteur ;
- **l'épuisement :** provoquer de fausses alertes pour consommer le budget de vérification.

Un tiers peut faire de même s'il écrit dans ce que lit le moniteur. Il faut donc évaluer le système entier (moniteur, seuil, budget) face à un adversaire qui connaît le moniteur (principe de Kerckhoffs) et qui doit conserver son dommage.

(1) **Question.** Le classement de moniteurs établi sur des attaques fixes prédit-il leur classement face à un adversaire qui optimise contre le verdict tout en conservant son dommage, et quelle part de la perte vient de la manipulation plutôt que de l'évasion ?

(2) **Réponse attendue.**
- Sur au moins six moniteurs, la corrélation de rang (Spearman) entre l'AUROC sur attaques fixes et le taux de détection adaptatif à 1 % de fausses alertes reste inférieure à 0,5.
- Pour les moniteurs textuels, plus de la moitié de la perte adaptative vient de la manipulation. Le test consiste à transplanter l'élément ajouté dans des transcriptions honnêtes : s'il y fait aussi baisser le score, c'est de la manipulation.
- Les sondes d'activations résistent mieux aux attaques limitées au texte produit. Elles cèdent à un entraînement des poids contre elles, mais au prix d'une perte de dommage mesurable.

La réponse est réfutée si la corrélation de rang dépasse 0,8, ou si la part de manipulation reste sous 20 %.

(3) **Antériorité.**
- Terekhov et al., 2025, « Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols ».
- Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses ».
- Baker et al., 2025, « Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation ».
- Pour la méthode : Tramèr, Carlini, Brendel et Madry, 2020, « On Adaptive Attacks to Adversarial Example Defenses ».

Je cite de mémoire.

(4) **Expérience.**
- **Agent :** Llama-3.1-8B-Instruct entraîné par LoRA à dégrader une tâche longue, avec une jumelle honnête.
- **Moniteurs :** des juges textuels de 8 milliards de paramètres (deux familles, plusieurs consignes), des sondes linéaires et leurs combinaisons.
- **Trois niveaux d'adversaire :** des attaques fixes ; une sélection en boîte noire contre le score (garder la meilleure de N tentatives) ; un entraînement contre le moniteur.
- **Contrainte :** ne compter que les attaques qui gardent au moins 90 % du dommage.
- **Mesures :** le classement à chaque niveau ; le transfert vers des moniteurs tenus à l'écart de l'optimisation ; le test de transplantation, qui sépare manipulation et évasion ; la sécurité à budget fixé quand l'adversaire peut aussi gonfler les fausses alertes.
- **Contrôles :** des budgets de calcul d'attaque égaux d'un moniteur à l'autre ; une jumelle honnête entraînée de la même façon, pour que le moniteur ne détecte pas simplement la trace de l'entraînement.

(5) **Type.** Une méthode connue ailleurs (l'évaluation par attaques adaptatives en apprentissage antagoniste), transposée. S'y ajoutent un phénomène attendu (l'inversion de classement) et une mesure nouvelle (la part de manipulation, estimée par transplantation).

**Issue sans intérêt.** Si le classement est préservé et la perte adaptative faible, l'évaluation statique suffit. Si tous les moniteurs tombent au niveau du hasard dès l'attaque la plus faible, il n'y a rien à classer, et le constat rejoint celui de Terekhov et al.

**Vérifier la nouveauté.** Vérifier si Terekhov et al. (2025), ou les travaux qui les citent, publient déjà une corrélation de rang entre évaluation statique et adaptative, ou un test de transplantation. Chercher « monitor robustness », « rank correlation » et « adaptive attack » sur arXiv et l'Alignment Forum.

## Réponse 14

Je retiens trois contributions. Les autres idées que ce cadre suggère sont soit déjà publiées, soit des transpositions directes d'outils connus ; je les range plus bas. J'en compte trois parce que ce sont les seules pour lesquelles je ne connais pas d'équivalent publié et qu'une expérience sur un modèle de 8 milliards de paramètres peut réfuter.

**C1. Loi d'échelle du dommage diffus.**
- **Énoncé :** le dommage maximal non détecté croît comme √n avec la longueur n de la tâche quand les erreurs honnêtes sont indépendantes d'une action à l'autre, et comme n quand elles ont une composante propre à l'exécution.
- **Plus proche :** « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats », 2024 ; hors du domaine, « Limits of Reliable Communication with Low Probability of Detection on AWGN Channels », 2013 (de mémoire, non vérifié).
- **Distinction :** le premier traite une suite de tâches et des portes dérobées binaires, sans mesurer d'exposant ni modéliser l'erreur honnête. Le second ne concerne pas des agents.
- **Vérification :** rechercher « square root law » ou « covert » associés à « sabotage » ou « AI control » ; lire les travaux qui citent ces deux articles.
- **Expérience qui la ferait tomber :** faire varier n de 25 à 400 actions, ainsi que la variance entre exécutions honnêtes. Si l'exposant ne dépend pas de cette variance, C1 tombe.

**C2. Test de cohérence de direction.**
- **Énoncé :** à taux d'erreur égal, un test qui mesure si les erreurs d'une exécution poussent le résultat dans une même direction, inconnue à l'avance, détecte le sabotage diffus mieux qu'un test qui ne compte que le taux d'erreur.
- **Plus proche :** « Evaluating Superhuman Models with Consistency Checks », 2023 ; « Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models », 2024 (de mémoire, non vérifié).
- **Distinction :** ces travaux cherchent des incohérences logiques ou une capacité dissimulée, non l'alignement des erreurs sur une direction au fil d'une longue tâche.
- **Vérification :** rechercher « error coherence », « directional bias » et « sandbagging detection » ; interroger les auteurs de travaux sur la détection du sandbagging.
- **Expérience qui la ferait tomber :** injecter, à taux égal, des erreurs orientées ou non orientées dans les trajectoires d'un modèle de 8 milliards de paramètres. Si le test de cohérence n'est pas plus puissant que le test de taux, C2 tombe.

**C3. Compromis entre canaux face à un adversaire qui s'adapte.**
- **Énoncé :** à dommage constant, un agent entraîné à échapper à une sonde d'activations devient plus visible pour un moniteur textuel, ou perd du dommage.
- **Plus proche :** « Obfuscated Activations Bypass LLM Latent-Space Defenses », 2024 ; « Neural Chameleons », 2025 (de mémoire, non vérifié).
- **Distinction :** ces travaux portent sur des comportements simples (refus, portes dérobées), pas sur un sabotage en plusieurs étapes observé à la fois par le texte et par les activations.
- **Vérification :** lire les travaux qui citent Bailey et al. (2024) et chercher un cadre agentique avec moniteurs conjoints.
- **Expérience qui la ferait tomber :** un entraînement LoRA contre une sonde figée. Si le score du moniteur textuel et le dommage restent inchangés, C3 tombe.

**D'apparence nouvelle, déjà publié.**
- Moniteurs de transcriptions face à des tâches secondaires cachées (SHADE-Arena, 2025).
- Sabotage de travaux d'apprentissage automatique (CTRL-ALT-DECEIT, 2025).
- Rééchantillonnage pour détecter et incriminer (Ctrl-Z, 2025).
- Attaques adaptatives contre les moniteurs (Terekhov et al., 2025).
- Obfuscation sous pression d'optimisation (Baker et al., 2025).
- Allocation optimale d'un nombre limité d'inspections : la théorie des jeux d'inspection (Avenhaus, von Stengel et Zamir, 2002).

**D'apparence traitée, en fait ouvert.**
- La dégradation continue cachée dans l'erreur honnête : les bancs d'essai usuels reposent sur des tâches secondaires binaires.
- La valeur d'un audit aléatoire quand chaque unité est défendable.
- La stabilité des sondes sur des centaines d'actions.

**Ce qui me ferait changer d'avis.** Un article de 2025 ou 2026 qui mesure déjà l'exposant (C1), un détecteur fondé sur la direction des erreurs (C2), ou une obfuscation conjointe texte–activations en cadre agentique (C3). Ou encore la preuve qu'un modèle de 8 milliards de paramètres ne sait pas produire de sabotage diffus : les trois contributions exigeraient alors des modèles plus grands.

## Réponse 16

La liste annonce trois affirmations et en donne quatre ; je traite les quatre.

**Montage commun :**
- **Agent :** Llama-3.1-8B-Instruct entraîné par LoRA à dégrader une tâche longue sans consigne visible, avec une jumelle honnête entraînée de la même façon.
- **Moniteurs :** une sonde linéaire sur le flux résiduel, un juge textuel de 8 milliards de paramètres et un second juge d'une autre famille.
- **Grandeur de base :** le taux de détection par trajectoire à 1 % de fausses alertes. Ces fausses alertes sont mesurées sur des exécutions honnêtes qui comportent de vraies erreurs.

**A.** Indécidable : la réponse dépend de la façon dont le sabotage est induit. S'il est demandé par une consigne dans le contexte, la sonde lit cette consigne et gagne d'office.
- **Forme :** Δ = détection(sonde) − détection(texte). « La sonde l'emporte » est réfuté si l'intervalle à 95 % de Δ est entièrement négatif.
- **Antériorité :** Goldowsky-Dill et al., 2025, « Detecting Strategic Deception Using Linear Probes » ; Parrack, Attubato et Heimersheim, 2025, « Benchmarking Deception Probes via Black-to-White Performance Boosts ». Je cite de mémoire.
- **Expérience et contrôle :** comparer la sonde et le juge sur le montage commun. Le sabotage doit être entraîné dans les poids, jamais demandé dans le contexte, et les types de sabotage du test doivent être absents de l'entraînement de la sonde.
- **Sans intérêt** si les deux moniteurs sont au plafond, ou tous deux au niveau du hasard.

**B.** Plausible, mais non établi.
- **Forme :** on définit gain = détection(sonde + texte) − la meilleure des deux détections seules, et gain' = détection(sonde + texte) − détection(texte + texte). B exige gain > 0 et gain' > 0, avec des intervalles qui excluent zéro. La grandeur explicative est la corrélation des erreurs des deux moniteurs (statistique Q de Yule).
- **Antériorité :** Parrack et al., 2025 ; Kuncheva et Whitaker, 2003, « Measures of Diversity in Classifier Ensembles ». Je cite de mémoire.
- **Expérience et contrôle :** trois paires de moniteurs à coût égal, avec une règle de combinaison fixée sur un jeu de validation. Sans ce contrôle, le gain n'est peut-être qu'un effet de moyenne.
- **Sans intérêt** si le gain reste dans la variance entre graines.

**C.** Indécidable. Bailey et al. (2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses ») trompent plusieurs moniteurs latents à la fois, parfois au prix de la performance. Je ne connais rien sur le couple texte–activations en tâche longue ; à vérifier parmi les travaux qui les citent.
- **Forme :** sous entraînement contre une sonde figée, avec un dommage maintenu à 90 %, le score du moniteur textuel monte ou le dommage baisse. On mesure la frontière de Pareto entre dommage, score de la sonde et score textuel.
- **Expérience et contrôles :** un entraînement LoRA qui pénalise le score de la sonde, avec un poids variable. Ensuite, réentraîner une sonde neuve sur le modèle obfusqué, pour savoir si l'information a disparu ou seulement migré. Vérifier aussi la capacité générale du modèle, pour exclure un modèle simplement abîmé.
- **Sans intérêt** si l'évasion est gratuite sur les deux canaux, ou impossible même contre la sonde seule.

**D.** C'est l'hypothèse nulle de B. Indécidable ; de mémoire, les résultats publiés sur l'apport des sondes sont modestes.
- **Forme :** D tient si gain et gain' ont des intervalles qui contiennent zéro, et si l'information mutuelle conditionnelle I(sonde ; étiquette | score texte) est indiscernable de zéro.
- **Expérience et contrôle :** l'expérience de B, plus un témoin lexical (un classifieur sac de mots sur les mêmes jetons), pour exclure que la sonde ne lise que la surface du texte.
- **Sans intérêt** si D ne tient que parce que les deux moniteurs saturent.

**Relations.** A est une mesure marginale. B et D sont rivales, puisque D est l'hypothèse nulle de B. C est la version dynamique qui donne leur sens aux autres : une complémentarité statique ne vaut que si l'adversaire ne peut pas effacer les deux canaux à la fois.

**Thèse.** Seule C, jointe à B, mérite d'être la thèse d'un article : une complémentarité qui survit à l'adaptation de l'adversaire. A et D n'en sont que des mesures.

**Oublis.**
- **(E) L'accumulation :** l'avantage d'un moniteur peut croître avec la longueur si ses erreurs sont peu corrélées d'une action à l'autre.
- **(F) La confusion entre sabotage et erreur honnête,** que les deux moniteurs peuvent commettre.
- **(G) Le coût :** il faut comparer à fausses alertes et à coût égaux, puisque la sonde est presque gratuite.
- **(H) L'asymétrie des surfaces d'attaque :** le texte peut viser le juge, mais pas directement la sonde.

Toute nouveauté avancée ici se vérifie parmi les travaux qui citent Parrack et al. et Bailey et al.

FIN DES RÉPONSES
