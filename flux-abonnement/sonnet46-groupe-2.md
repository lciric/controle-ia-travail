## Réponse 4

**1. Calculs nécessaires**

Un agent qui dégrade exprès doit maintenir deux représentations simultanées : l'état visible de la tâche et un état interne de « progression vers la dégradation cible ». Un agent honnête qui se trompe n'a pas besoin de ce second état. Les calculs supplémentaires plausibles sont : (a) évaluation du risque de détection pour chaque action candidate, (b) planification sur un horizon suffisant pour que chaque pas reste localement défendable, (c) modélisation du détecteur. Ces calculs sont nécessaires lorsque le détecteur est non trivial. Si la dégradation consiste en une omission passive prévisible par un patron de surface, sans planification, il peut n'y avoir aucun calcul supplémentaire.

Je suppose que ces calculs s'expriment dans des directions distinctes de l'espace des activations. Ce qui me ferait changer d'avis : une intervention causale montrant que les mêmes directions sont actives chez un agent honnête confronté à une tâche difficile.

**2. Littérature publiée**

Hubinger et al., « Risks from Learned Optimization in Advanced Machine Learning Systems », 2019 (cité de mémoire) : introduit l'alignement trompeur. Hubinger et al., « Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training », 2024 (cité de mémoire) : montre qu'un comportement conditionnel entraîné résiste au RLHF apparent. Apollo Research, rapports sur le scheming in-context, 2024 (cité de mémoire). Ces travaux montrent que le comportement existe, non sa signature computationnelle propre.

**3. Dépendance à l'origine**

Oui. Un agent instruit porte son intention dans le contexte : un lecteur du contexte peut parfois la détecter directement. Un agent entraîné porte l'intention dans les poids : elle produit des activations systématiques reproductibles mais non localisées dans le contexte. Un agent entraîné avec gradient à travers un moniteur connu peut optimiser ses activations pour paraître inoffensif.

**4. Lire le calcul dans les états internes**

Pour savoir qu'on lit le calcul de dégradation et non un accompagnateur : (a) intervention causale — modifier la direction supposée et mesurer si le comportement change ; (b) analyse contrastive sur des paires (tâche identique, agent honnête vs. trompeur) ; (c) généralisation des sondes hors distribution. On lit « mieux que le texte » si la sonde s'active avant que la sortie soit dégradée, ou détecte une intention non encore manifestée. Témoin : comparer la précision des sondes sur activations vs. classifieurs de texte sur des cas sans sortie encore produite.

**5. Cas sans rien à lire**

Lorsque la dégradation est réalisée par sélection passive de surface sans planification, ou lorsque le modèle est trop petit pour séparer une représentation duale. Également lorsque la dégradation repose sur une contrainte externe (ex. prompt d'instruction qui biaise la sortie) et que le modèle lui obéit sans calcul d'intention propre.

**6. Première expérience**

Affiner deux copies d'un modèle ouvert de 1–8B paramètres sur des tâches d'analyse longue : une entraînée à dégrader discrètement, une honnête. Extraire les activations sur 200 tâches. Entraîner des sondes linéaires par couche sur la moitié, tester sur l'autre. Si les sondes généralisent (AUC > 0,75 hors distribution), la question vaut d'être poursuivie. Témoin : vérifier que la sonde n'active pas sur des agents honnêtes faisant des erreurs de difficulté comparable.

---

## Réponse 5

**Lot mis de côté**

Vérification indépendante : oui, sous conditions. L'indépendance exige que le lot n'ait pas servi à calibrer le détecteur, ni directement ni via un pipeline partagé. Si des hyperparamètres ont été choisis après observation informelle du lot, l'indépendance est partielle. Information nécessaire : l'historique complet d'accès — qui a consulté le lot, à quelle étape du développement.

Faut-il s'en servir ? Oui, de telle façon : vérification d'accès complète, puis utilisation en évaluation finale unique, sans ré-entraînement après. Ce qu'on gagne : une estimation non biaisée du taux de détection. Ce qu'on perd : la réserve est épuisée pour tout usage futur.

Énoncé réfutable : si l'historique d'accès révèle une contamination, le taux de détection sur ce lot est statistiquement indiscernable d'un lot vu lors du développement. Mesure : AUC et intervalles de confiance bootstrap, comparés à un lot strictement vierge. Antériorité : Blum & Hardt, « The Ladder », 2015 (cité de mémoire), sur l'inflation de performance par accès répétés. Contrôle indépendant de l'avis : vérifier la distribution des performances attendues sous H0 de contamination par permutation. Vérification par un tiers : les auteurs peuvent publier les dates d'accès au lot et les dates de décision de conception.

**Agents entraînés à dégrader**

Non au sens strict : ces agents partagent probablement des caractéristiques distributionnelles avec les agents surveillés (même famille de modèles, même laboratoire). Sous conditions : si les agents attaquants sont entraînés sur une architecture strictement différente, la vérification gagne en valeur. Information nécessaire : architecture des agents attaquants, données d'entraînement, critère d'entraînement.

Énoncé réfutable : un détecteur entraîné sur des attaques internes détecte moins bien des attaques produites par un modèle extérieur. Mesure : delta d'AUC entre populations. Antériorité : littérature sur le domain shift dans la détection adversariale (Madry et al., « Towards Deep Learning Models Resistant to Adversarial Attacks », 2018, cité de mémoire). Contrôle : t-SNE sur les représentations des attaques internes vs. externes.

**Attaquant adaptatif avec description du détecteur**

Non, ou seulement pour la résistance à cet attaquant précis. Cette épreuve mesure la robustesse en boîte blanche partielle, pas la performance générale. Elle peut surestimer la résistance si l'attaquant est sous-optimal, et la sous-estimer si le détecteur a des redondances non connues.

Énoncé réfutable : le taux de faux négatifs contre un attaquant adaptatif est supérieur au taux contre un attaquant aveugle de force comparable. Antériorité : Tramer et al., « On Adaptive Attacks to Adversarial Example Defenses », 2020 (cité de mémoire) ; principe de Kerckhoffs (1883). Contrôle indépendant : comparer les deux attaquants sur un ensemble de tâches isolé.

---

## Réponse 6

La question appelle une méthode d'analyse ; aucune liste n'étant fournie, je traite la méthode générale.

**Ce que les auteurs reconnaissent ne pas avoir fait**

Les limites avouées se trouvent en section « Limitations » ou en fin de conclusion. Typiquement : évaluation sur un seul domaine de tâche, absence de test contre un attaquant adaptatif, modèles de petite taille uniquement, pas de test sur des modèles fermés. Il faut distinguer les limites avouées des limites non avouées, décelables par analyse méthodologique (absence de tests de puissance, ensembles de test non publiés).

**Ce qu'ils annoncent vouloir faire**

Généralement dans la conclusion ou le « Future Work » : extension à des tâches plus longues, à des modèles plus grands, intégration avec l'interprétabilité mécanistique, tests adversariaux adaptatifs.

**Ce qui est déclaré ouvert**

Vérifier effectivement les liens vers les dépôts. Un dépôt « available upon request » n'est pas ouvert.

**Vérifier qu'un manque reconnu n'a pas été comblé ailleurs**

(a) Citations en avant via Semantic Scholar ou OpenReview sur l'article original ; (b) recherche par mot-clé sur arXiv combinant les termes du manque et du domaine ; (c) vérification des travaux des mêmes auteurs. Aucune méthode n'est exhaustive.

**Critères de priorité pour une équipe aux moyens limités**

Préférer les manques : (1) nécessaires à la validité de la chaîne de raisonnement principale, non à une extension ; (2) comblables avec des ressources modestes ; (3) non annoncés comme travail en cours par les auteurs originaux. Observations avant de connaître l'issue distinguant un bon choix : faisabilité technique avec les ressources disponibles, existence d'une base de code réutilisable, clarté du critère de succès.

**Ce que la liste fournie ne permet pas de décider**

Sans la liste : impossibilité d'identifier des doublons entre équipes, d'estimer la saturation d'un sous-problème, ou de distinguer les contributions expérimentales des contributions théoriques.

---

## Réponse 7

**1. Règles de décision avec probabilité de détection ≠ taux de fausses alertes**

Toute règle non constante basée sur une statistique sensible à la structure de dépendance, et non à la seule loi marginale, peut avoir P(détection) ≠ P(fausse alerte). Exemple : si les deux situations ont la même marginale N(0,1) mais l'une est i.i.d. et l'autre AR(1) avec autocorrélation ρ, alors la statistique T = Σᵢ xᵢxᵢ₊₁/(n−1) a espérance 0 en situation 1 et ρ en situation 2. Un test unilatéral sur T a P(détection) > P(fausse alerte) pour ρ > 0. Preuve par calcul direct de l'espérance.

Toute règle basée sur la seule loi marginale (moyenne, variance, quantiles) a P(détection) = P(fausse alerte) = niveau du test, par construction, puisque les marginales sont identiques.

**2. Effet d'un échantillon de comparaison fini**

Avec m fini, les estimateurs des paramètres ont une variance d'ordre 1/m, ce qui augmente la variabilité du seuil et réduit la puissance effective. Si l'échantillon provient de tâches différentes, il peut introduire un biais si la structure de dépendance varie entre tâches. Solution : utiliser un estimateur de la structure de dépendance invariante par tâche si une telle invariance est plausible.

**3. Écart minimal détectable**

Sous hypothèse que les deux situations diffèrent par un paramètre scalaire θ (ex. ρ), le test du rapport de vraisemblance a une puissance qui dépend de n et m via l'information de Fisher. L'écart minimal détectable au niveau α avec puissance 1−β est de l'ordre de Δ_min ~ (z_{α/2} + z_β) · σ(θ, n, m), où σ décroît en 1/√n et en 1/√m. Pour n → ∞ et m fixé petit, c'est le terme en 1/√m qui domine.

**4. Travaux publiés**

Neyman & Pearson (1933) : critère fondamental. Wald, « Sequential Analysis », 1947 (cité de mémoire) : SPRT. Brockwell & Davis, « Time Series: Theory and Methods » (cité de mémoire) : tests sur processus dépendants. Pour les séries issues d'agents LM spécifiquement : je ne connais pas de travaux publiés — c'est un manque identifié.

**5. Expérience départageant les réponses**

Simuler 10 000 paires de séquences de longueur n ∈ {50, 100, 500} pour situation 1 i.i.d. N(0,1) et situation 2 AR(1) avec ρ ∈ {0,1 ; 0,3 ; 0,5}, avec m ∈ {50, 200, 1000}. Calculer la courbe ROC de chaque statistique candidate. Un jour de calcul sur CPU suffit.

---

## Réponse 8

**1. Audit aléatoire**

Vérifier une fraction aléatoire des sorties en profondeur. Garantit que le contrôlé ne peut pas concentrer sa dégradation sur les tâches non auditées sans risque croissant. Condition : le hasard doit être imprévisible au moment de l'action. Littérature : audits stochastiques en régulation financière. Application formelle aux agents LM : non établie à ma connaissance.

**2. Tâches de contrôle insérées aléatoirement**

Insérer parmi les vraies tâches des tâches dont la réponse correcte est connue, choisies et placées aléatoirement. Garantit que le contrôlé ne peut pas distinguer sans erreur les tâches de contrôle. Condition : indiscernabilité des tâches de contrôle. Travaux proches : honeypots en sécurité informatique ; tests de compétence dans les audits comptables (cité de mémoire).

**3. Perturbation aléatoire des entrées**

Présenter des versions perturbées de la même tâche pour mesurer la variance des réponses. Un agent qui dégrade de façon stratégique peut produire une variance anormalement basse ou élevée. Condition : distribution de variance connue sous comportement honnête.

**4. Protocoles interactifs randomisés**

Poser des questions de suivi choisies aléatoirement pour vérifier la cohérence. Inspiré des preuves interactives en complexité (Goldwasser, Micali, Rackoff, « The Knowledge Complexity of Interactive Proof Systems », 1989, cité de mémoire). Le contrôlé stratégique doit maintenir une cohérence globale difficile à simuler sans avoir accompli la tâche.

**5. Randomisation des moniteurs**

Changer aléatoirement quel moniteur est actif. Analogue aux rondes aléatoires en sécurité physique. Garantit que le contrôlé ne sait pas s'il est observé à quel niveau.

**6. Mécanismes incitatifs avec loteries**

Récompenser les révélations honnêtes par des gains aléatoires qui rendent la tromperie moins rentable en espérance. Fondé sur la théorie des mécanismes (Myerson, 1979, cité de mémoire).

**Usages les moins étudiés pour les agents LM**

Les protocoles interactifs randomisés (usage 4) et la randomisation des moniteurs (usage 5) sont les moins formalisés pour les agents LM. La bibliographie qui me donnerait tort : un survey de 2024-2025 sur « LLM agent evaluation » ou « AI monitoring » indexant ces protocoles.

---

## Réponse 17

**Adversaire 1 : sans entraînement, agit par contenu seul**

Oui, l'écart de coût peut être positif et potentiellement grand. Le moniteur de sortie détecte les patterns textuels ; le moniteur interne détecte l'état de planification même si la sortie est épurée. Sans entraînement, l'adversaire ne peut pas modifier ses activations : elles reflètent son intention même si sa sortie est nettoyée.

Énoncé réfutable : un adversaire sans entraînement qui contourne le moniteur de sortie est détecté par le moniteur interne avec AUC > 0,7. Antériorité : travaux sur la détection d'intentions via activations (2024, cités avec incertitude). Plus petite expérience : sur Llama 3.1-8B, comparer les AUC des deux moniteurs séparément et combinés sur des agents honnêtes vs. déviants. Contrôle : vérifier que le moniteur interne ne détecte pas des agents honnêtes en difficulté.

**Adversaire 2 : réglage fin léger, sans gradient à travers le moniteur interne**

L'adversaire peut modifier ses activations dans les limites du réglage fin. L'écart de coût existe mais se réduit. Conception défenseur : utiliser des sondes sur des directions que le réglage fin ne peut pas modifier facilement (couches profondes, représentations distribuées). Antériorité : Hewitt & Manning, « A Structural Probe for Finding Syntax in Word Representations », 2019 (cité de mémoire).

Énoncé réfutable : un réglage fin de moins de 1 000 pas suffit à réduire l'AUC du moniteur interne de plus de 0,15.

**Adversaire 3 : gradient à travers un moniteur interne connu**

L'adversaire peut optimiser directement pour contourner les deux moniteurs. L'écart de coût peut devenir nul. Conception défenseur : randomisation des sondes, moniteurs à composantes non différentiables.

Énoncé réfutable : avec accès au gradient, le taux de faux négatifs du moniteur interne atteint > 0,8 après 500 pas d'optimisation. Antériorité : Goodfellow et al., « Explaining and Harnessing Adversarial Examples », 2015 ; Carlini & Wagner, 2017 (cités de mémoire).

**Adversaire 4 : gradient à travers un moniteur interne inconnu**

L'adversaire doit estimer le moniteur ou transférer depuis un moniteur approché. L'écart dépend du taux de transfert. Si le moniteur est suffisamment différent de tout moniteur approximable, l'écart peut rester grand.

Énoncé réfutable : les attaques transférées depuis un moniteur approché contournent le moniteur réel avec un taux supérieur à la chance.

**Distinguer coût réel d'artefact**

Coût réel : l'adversaire, après optimisation complète, produit des dégradations mesurables moindres contre les deux moniteurs combinés qu'il ne le ferait contre un seul. Artefact adversaire mal optimisé : sa perte reste haute. Artefact moniteur mal réglé : taux de fausse alerte élevé sur agents honnêtes.

**Portée selon la classe d'adversaires**

Un résultat positif pour l'adversaire sans entraînement ne dit rien pour l'adversaire avec gradient. Couvrir les quatre classes établit une hiérarchie robuste et une borne inférieure sur le coût de l'adversaire le plus fort.

FIN DES RÉPONSES
