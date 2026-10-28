# Antériorité — Q6 : la co-évolution contrôlée pour l'artefact de source

Avertissement : tout ce qui suit est RAPPORTÉ d'après des résumés, des pages HTML et des synthèses de pages (pages arXiv, ICLR, NeurIPS, alphaXiv, papers.cool). Rien n'a été vérifié sur un PDF lu en entier.

## 1. Verdict

**SEMI-OCCUPÉ, confiance moyenne.**

- **Le constat est occupé, et densément.** Une défense peut séparer les épisodes par leur source plutôt que par le comportement visé. On le voit chez les classifieurs d'invites malveillantes (Fomin), les détecteurs de mensonge appliqués à la sous-performance délibérée (Lin et al., ICLR 2026), les sondes de tromperie (Natarajan et al.), la détection d'intrusion réseau et le traitement automatique des langues classique.
- **Les contrôles statiques sont occupés aussi** :
  - évaluation en laissant de côté un jeu de données entier ;
  - diagnostic de rétention des coefficients (Fomin) ;
  - témoins appariés sur le même modèle (Lin et al.) ;
  - filtrage adverse AFLite.
- **La partie dynamique paraît ouverte.** Je n'ai trouvé aucun travail qui contrôle l'artefact du générateur À L'INTÉRIEUR d'une boucle co-évolutive de moniteurs. Le voisin le plus proche est hors du champ : Pathak et al., CVPR 2023, en vision.

## 2. Occupants et voisins, du plus proche au plus lointain

**Pathak et al., « Sequential Training of GANs Against GAN-Classifiers Reveals Correlated Knowledge Gaps », CVPR 2023 (relu par les pairs) — RAPPORTÉ.** C'est le seul travail trouvé qui étudie les artefacts du générateur au fil d'itérations adversariales.

- **Dispositif.** À chaque itération, des réseaux antagonistes génératifs sont entraînés à tromper les classifieurs des itérations précédentes.
- **Résultats rapportés :**
  - un classifieur de l'itération i ne détecte pas les générateurs des itérations suivantes ;
  - les générateurs déplacent leurs artefacts « en bloc », ce que les auteurs appellent une « préférence d'artefact » ;
  - dans la variante sans mémoire, les générateurs oscillent entre deux groupes d'artefacts.
- **Limites.** C'est de l'image, pas de la sécurité. Il n'y a ni témoins appariés ni comportement visé distinct de l'artefact. INFÉRÉ : c'est un précédent direct pour la dérive des artefacts dans une boucle, mais la cible y EST l'artefact.

**Fomin, « When Benchmarks Lie », arXiv 2602.14161 (préimpression, version 2 de juillet 2026 ; issue de l'atelier AIWILD à ICLR 2026) — RAPPORTÉ.**

- **Dispositif.** Des sondes linéaires sur activations (Llama-3.1-8B, Gemma-3-27B, Qwen-3.5) sont évaluées sur 18 jeux de données, avec le protocole qui laisse un jeu de données de côté.
- **Chiffres rapportés :**
  - la validation croisée standard surestime l'aire sous la courbe de 8,0 à 16,5 points ;
  - 28 à 44 % des caractéristiques d'autoencodeur parcimonieux les plus importantes sont des raccourcis ;
  - un classifieur d'identité du jeu de données atteint 96,6 %.
- **Propositions.** Une métrique de rétention des coefficients et des attributions pondérées. Les correctifs classiques ont été essayés sans combler l'écart : entraînement adversarial, projection de sous-espace, repondération.
- **Ce qu'il ne fait PAS.** Pas de boucle co-évolutive, pas d'agents, pas de témoins appariés par générateur.

**Lin, Bernabeu-Perez, Arnav, Wells, Phuong, « When Lie Detectors Learn Model Identity: Confounds in Black-Box Sandbagging Detection », ICLR 2026 (relu par les pairs) — RAPPORTÉ.** C'est la démonstration la plus nette, côté moniteurs, de la confusion « source / comportement ».

- **Résultat central.** Des détecteurs par plongements apprennent l'identité du modèle. Leur rappel tombe de 89 % en évaluation multi-modèles à 2 % avec des témoins du même modèle.
- **Autre résultat.** La surveillance de confiance confond le caractère incorrect d'une réponse avec la suspicion (r = −0,66).
- **Contrôles proposés :**
  - paires issues du même modèle ;
  - contrôle de l'exactitude des réponses ;
  - ligne de base « honnête contre honnête ».
- **Ce qu'il ne fait PAS.** Pas de boucle, et la cible est la sous-performance délibérée, pas le sabotage d'agent.

**Natarajan, Jain, Arora, Golechha, Bloom, « Building Better Deception Probes Using Targeted Instruction Pairs », arXiv 2602.01425 (préimpression, travaux LASR Labs avec l'Institut britannique de sécurité de l'IA) — RAPPORTÉ.**

- **Résultat central.** La paire d'instructions du message système explique 70,6 % de la variance de l'aire sous la courbe des sondes ; le jeu de données n'en explique que 2,5 %.
- **Lecture des auteurs.** Les sondes captent l'intention portée par l'instruction.
- **Limite reconnue par les auteurs.** Ils n'ont pas montré que les sondes détectent le type de tromperie plutôt que d'autres traits des invites générées.
- **Portée pour le programme.** C'est le meilleur appui publié de l'hypothèse « la sonde détecte l'instruction, pas le comportement ».

**Luikham, « Asymmetries in Spontaneous and Instructed Deception », arXiv 2609.00180 (préimpression, chercheur indépendant) — RAPPORTÉ.**

- **Résultat.** Les sondes entraînées sur la tromperie instruite se transfèrent mal vers la tromperie spontanée ; l'inverse se transfère mieux.
- **Ce qu'il ne fait PAS.** Il n'encadre pas explicitement la confusion « instruction / comportement », et il étudie un seul modèle.

**Hollinsworth, Spies, Diriba, Gleave, Cundy, « Caught in the Act » (jeu de données FIBS), arXiv 2610.12445 (préimpression ; c'est le « Telling FIBS » du cadre) — RAPPORTÉ pour le résumé.**

- **Résultat annoncé.** Une aire sous la courbe de 98,8 % sur SHADE-Arena, au-dessus d'un moniteur textuel Opus.
- **À VÉRIFIER.** Le résumé ne dit rien d'un contrôle instruction / comportement, d'un contrôle de source, de témoins appariés ou de familles tenues à l'écart. Le volet « tromperie introspective » pourrait partiellement y répondre.
- **Accès.** La page arXiv n'était pas accessible ; seule la page papers.cool l'était.

**Moniteurs de manigance boîte noire, arXiv 2603.00829 (« Constitutional Black-Box Monitoring », préimpression) — RAPPORTÉ.**

- **Ce que dit l'article :**
  - l'optimisation poussée « exploite des artefacts idiosyncratiques des données synthétiques » ;
  - des filtres d'artefacts de génération sont prévus ;
  - l'ensemble de test mélange trois modèles agents « pour réduire les artefacts propres à un modèle » ;
  - paraphrase et transfert de style sont proposés comme travail futur.
- **Ce qu'il ne fait PAS.** Aucune ablation entre générateurs.

**ResearchArena, arXiv 2607.19321 (préimpression) — RAPPORTÉ.**

- **Contrôle présent.** Des exécutions avec sabotage et sans sabotage, appariées par agent et par tâche, ce qui contrôle l'identité du modèle. Le moniteur ne voit pas l'instruction.
- **Écarts relevés.** La longueur est vérifiée, avec des écarts allant jusqu'à 4,2 fois sur certains épisodes.
- **Ce qu'il ne fait PAS.** Ni contrôle du style, ni évaluation sur familles tenues à l'écart.

**MonitoringBench, arXiv 2605.09684 — RAPPORTÉ.** La généralisation est testée seulement du côté des moniteurs : attaques optimisées contre trois moniteurs, évaluées sur dix moniteurs tenus à l'écart. Il n'y a aucun contrôle du générateur ni de son style.

**Co-évolution « externalisée », arXiv 2605.13411 (préimpression) — RAPPORTÉ.**

- **Ce qu'il fait.** Il évalue sur des familles d'attaque dont les compétences n'ont pas été vues.
- **Ce qu'il ne fait PAS.** Pas d'attaquant indépendant, et le même juge sert à la récompense et à l'évaluation.
- **Contrôles.** La décontamination par similarité et des témoins bénins hors style (GSM8K) sont les seuls contrôles décrits.
- INFÉRÉ : représentatif de la lacune des co-évolutions de défense.

**PIDS-Bench, arXiv 2609.15017 (IEEE Access 2026) — RAPPORTÉ.**

- **Ce qu'il fait :**
  - séparation des partitions au niveau de la famille de graines ;
  - jeu « bénin difficile » ;
  - hypothèse explicite de raccourcis lexicaux et structurels ;
  - effet de la source du corpus faible mais indépendant.
- **Ce qu'il ne fait PAS.** Les auteurs disent ne pas avoir construit de négatifs appariés par paire.

**Traitement automatique des langues classique — RAPPORTÉ.**

- **Gururangan et al. 2018 et Geirhos et al. 2020** : connus, non relus ici.
- **Le Bras et al., « Adversarial Filters of Dataset Biases » (AFLite), ICML 2020** : filtrage adverse des biais.
- **Wallace, Williams, Jia, Kiela, « Analyzing Dynamic Adversarial Training Data in the Limit », arXiv 2110.08514** :
  - vingt tours de collecte adversariale dynamique ;
  - la précision « hypothèse seule », qui mesure les artefacts, ne diffère pas entre collecte statique et dynamique (69,3 contre 69,7 %) ;
  - aucun gain hors distribution.
  - INFÉRÉ : la boucle adversariale ne purge pas d'elle-même les artefacts. C'est un précédent utile, mais ce sont des annotateurs humains, pas un générateur figé.

**Sécurité informatique classique — RAPPORTÉ.**

- **Arp et al., « Dos and Don'ts of Machine Learning in Computer Security », USENIX Security 2022** : catalogue des corrélations fallacieuses (non relu ici).
- **Flood, thèse, Édimbourg 2025** : notion de « Bad Data Design Smells » dans les bancs de détection d'intrusion réseau. Les artefacts peuvent faire chuter la précision de plus de 90 %.
- **À VÉRIFIER** : le cas précis de l'artefact de durée de vie des paquets (TTL) dans KDD'99 et CIC-IDS. Il n'est pas confirmé dans le résumé lu.

## 3. Ce qui survit

**La question étroite qui reste ouverte.** Dans une boucle co-évolutive de moniteurs (boîte noire ou sondes), avec des familles d'attaque en rotation, quelle part de la « généralisation » mesurée sur la famille tenue à l'écart s'explique par l'artefact du générateur ? Comment cette part évolue-t-elle d'un tour à l'autre ? Le contrôle combinerait quatre éléments, et je n'ai trouvé aucun travail qui les réunisse, ni même deux d'entre eux, dans une boucle :

- témoins bénins appariés produits par le même générateur ;
- rétention des coefficients suivie par tour ;
- permutation du générateur entre familles ;
- bras « fuite textuelle » : un classifieur d'artefact seul, sans comportement.

**Pourquoi c'est plausible.** Trois travaux convergent :

- Pathak et al. 2023 montrent que les artefacts migrent en bloc d'un tour à l'autre ;
- Lin et al. 2026 montrent l'effondrement de 89 à 2 % sous témoins du même modèle ;
- Wallace et al. 2021 montrent que la collecte adversariale ne purge pas les artefacts.

INFÉRÉ : il est probable qu'une co-évolution non contrôlée récompense un moniteur qui suit la signature du générateur courant.

**Garde « anti-faux-trou ».** Les équipes de SafeCoEvo, AgentSafeEvo et EvoDefense n'ont été vérifiées ici que par leur absence dans les résultats de recherche, pas par lecture. À VÉRIFIER.

## 4. Traitabilité

**Faisable sur processeur seulement, en partie :**

- le bras « fuite textuelle » : un classifieur d'empreinte de générateur par sacs de mots ou plongements figés ;
- la rétention des coefficients sur des sondes déjà extraites ;
- les permutations, à partir de journaux existants (ResearchArena, ControlArena, FIBS si publié).

**Prérequis.** Il faut des épisodes appariés : même tâche, même modèle, avec et sans sabotage, issus de plusieurs générateurs. ResearchArena fournit déjà l'appariement par agent.

**Dépense.** Pour les sondes boîte blanche, il faut extraire les activations d'un modèle ouvert de taille moyenne, soit quelques dizaines à quelques centaines d'heures de processeur graphique. C'est un ordre de grandeur INFÉRÉ.

**Pièges connus :**

- **Longueur et coût de l'épisode**, qui trahissent le sabotage : écart de 4,2 fois dans ResearchArena.
- **Exactitude de la réponse**, confondue avec la suspicion (Lin et al.).
- **Instruction présente dans le contexte lu par la sonde** (Natarajan et al.).
- **Juge identique** pour la récompense et l'évaluation (2605.13411).
- **Sélection des seuls épisodes réussis.**
- **Correctifs de généralisation de domaine inopérants** selon Fomin.
- **Surcapacité du moniteur** : les classifieurs de faible capacité n'apprennent qu'un sous-ensemble des artefacts (Pathak et al.).

## 5. À vérifier sur PDF avant toute revendication

- **2610.12445 (FIBS)** :
  - générateurs des épisodes ;
  - présence de l'instruction dans les jetons sondés ;
  - témoins appariés ;
  - familles tenues à l'écart.
- **2602.14161** : définition exacte de la métrique de rétention ; un volet agents existe-t-il ?
- **Lin et al., ICLR 2026** : nature des détecteurs (plongements ou activations) ; tâches.
- **Pathak et al., CVPR 2023** : protocole sans mémoire ; mesure de la « préférence d'artefact ».
- **2603.00829** : section 5.3 sur l'exploitation des artefacts.
- **SafeCoEvo (2609.36580), AgentSafeEvo (2610.19422), EvoDefense (2605.31140), RvB, MAGIC** : contrôlent-ils le générateur ou le style dans leur boucle ?
- **Arp et al. 2022 et Flood 2025** : exemples précis d'artefacts réseau (durée de vie des paquets).
- **Wallace et al. 2021** : lieu de publication.

## 6. Requêtes faites

1. Fomin "When Benchmarks Lie" leave-one-category-out prompt injection classifier source artifact
2. jailbreak detector shortcut learning dataset artifacts generalization out-of-distribution source bias
3. deception probes detect dataset source rather than deception confound control activation probe 2025
4. sabotage probe detects instruction in system prompt not behavior confound monitoring agents activations
5. "Telling FIBS" probes sabotage
6. arXiv 2610.12445 probes black-box monitor sabotage
7. AI control monitor evaluation attack trajectories generated by same model confound model identity / stylistic artifact
8. adversarial training generator fingerprint shortcut discriminator learns generator artifacts co-evolution
9. network intrusion detection datasets artifacts trivially separable TTL shortcut bad design smells
10. prompt injection detector dataset bias style-matched negatives over-defense evaluation
11. monitor trained on synthetic attack transcripts learns generator model style; cross-generator evaluation scheming monitor 2026
12. adversarial data collection rounds annotation artifacts hypothesis-only Adversarial NLI Dynabench
13. Arp "Dos and Don'ts of Machine Learning in Computer Security" spurious correlations
14. red team generated attacks classifier overfits attacker style; held-out attacker model generalization
15. SafeCoEvo co-evolution execution guard held-out attack families evaluation
16. "generator artifacts" OR "attacker model identity" held-out attacker guardrail co-evolution
17. AI-generated text detection shortcut spurious features source confound
18. probe "honest vs dishonest" instructed prompt confound counterfactual 2026
19. AFLite adversarial filtering dataset biases
20. agent monitor paired benign counterfactual trajectories same model matched honest control
