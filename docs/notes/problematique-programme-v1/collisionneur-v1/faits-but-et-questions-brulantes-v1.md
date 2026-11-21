# Faits : le but d'un programme de contrôle de l'IA sur les sabotages diffus, et ce que le domaine dit ne pas savoir

## Le programme

Un programme de recherche défensif, mené par une très petite équipe aidée d'agents de recherche, étudie le contrôle d'agents d'IA non fiables qui sabotent de façon diffuse : beaucoup de petits écarts, dont aucun n'incrimine, sur des tâches floues (rédiger et réviser des propositions d'expériences), dont la qualité ne se vérifie qu'en partie et plus tard. Il travaille sur un modèle ouvert d'environ 8 milliards de paramètres, dont il lit les états internes. Il a : des saboteurs construits (consigne cachée, réglage fin) ; des sondes sur les états internes et des moniteurs qui ne lisent que le texte ; un jumeau honnête qui reçoit la même tâche ; des seuils à 1 % de fausses alertes ; un oracle qui compare le produit à une référence cachée ; un mode de sabotage tenu à l'écart de la conception des moniteurs et lu une seule fois ; des préenregistrements scellés avant toute mesure décisive ; un organisme d'idéation dont les propositions sont tuées sur des mondes à vérité plantée ; un arbitre formel en préparation.

Trois papiers sont prévus : « le temps » (accumuler le long d'une trajectoire des indices faibles lus dans les états internes, contre des moniteurs qui ne lisent que le texte), « l'instrument » (un moniteur peut-il être déplacé par ce que l'agent écrit), « l'essaim » (plusieurs copies qui se partagent un sabotage). Depuis peu, le programme tient que sa garantie contre un sabotage de genre inconnu ne vient pas de ses moniteurs, mais d'un audit tiré au hasard et jugé par l'oracle, qui borne le dommage cumulé ; les sondes accélèrent l'alarme et choisissent quoi vérifier.

Moyens : calcul modeste ; une bourse possible ; aucun accès aux états internes des modèles de pointe ; relecture humaine rare.

## Ce que le domaine a imprimé (citations, avec leur source)

- « the larger volume of mildly suspicious actions would only allow us to incriminate if we knew exactly how suspicious a benign model would look. But without that affordance, no amount of mildly suspicious actions is enough to incriminate the model. » (billet « How Can We Solve Diffuse Threats Like Research Sabotage with AI Control? », 30 avril 2025)
- « We focus on training mitigations, since monitoring and incrimination seem theoretically […] and empirically […] less promising for mitigating diffuse threats. » ; « the anti-scheming guarantees that a control mitigation provides are only as good as the red teaming performed against that mitigation » ; « For many of these tasks, the “ground truth” scores are undefined » (« Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892, version 3, p. 2 et 10)
- « we have no reliable samples of how model internals of genuinely scheming models would look » ; les méthodes en boîte blanche pourraient aider « especially if we can develop techniques to identify invariant patterns in model activations that reliably indicate misaligned planning » (arXiv 2504.05259, p. 24)
- « assurance for activations monitoring remains an open problem » (feuille de route de contrôle d'un laboratoire, arXiv 2607.13087, p. 25)
- « With p>99% our monitor evaluations will be approximately predictive of performance at deployment », posé comme une supposition ; « We do not know a promising method for justifying the safety of a monitored deployment when human red-teams are unlikely to find attack vectors that dominate an AI's attacks » (arXiv 2512.22154, p. 16 et 12)
- « CoTs can look benign if the malign reasoning can be done in activations » (arXiv 2507.11473, p. 7)
- des défenses de l'espace latent, détection de nouveauté comprise, « all vulnerable to obfuscated activations », l'obscurcissement réduisant toutefois la performance sur une tâche complexe (arXiv 2412.09565, p. 1) ; des modèles qui apprennent à échapper à des moniteurs d'activations jamais vus (arXiv 2512.11949, p. 1)
- « no detector is effective across all models and tasks » (détection d'anomalie mécaniste, arXiv 2504.08812, p. 1)
- un appel public à projets note que le sabotage de recherche « is likely to be difficult to distinguish from lack of competence » et demande « an increased understanding of the limits of white-box techniques for control » (août 2025)

## La question du directeur

« Quel est le but du programme ? Un système de contrôle qui fait mieux que l'état de l'art sur les sabotages diffus ? Faut-il illustrer un mode de défense ou d'attaque inédit, ou construire un système très performant qui lève les limites des systèmes existants ? Se concentrer sur des points particuliers, ou viser l'universalité ? Pour marquer le domaine, lequel vaut le mieux, et par quoi commencer ? Quelles sont les questions fondamentales et non tranchées que tout le monde se pose et sur lesquelles, avec assez de temps et de moyens (bourse comprise), un tel programme pourrait faire un pas décisif, quitte à changer de cap ? »

## Contraintes

- La menace se décrit au niveau de l'idée (familles, suppositions violées), jamais par un mode opératoire.
- Aucun chiffre ni aucune affirmation d'un travail publié sans sa source ; « je ne sais pas » est une réponse.
