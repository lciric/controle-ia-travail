Tu es consulté comme expert de l'évaluation de contrôle des systèmes d'intelligence artificielle (une équipe rouge fait saboter un agent, une équipe bleue cherche à le détecter) et des sondes linéaires sur les activations internes. Tu n'as accès à aucun de nos fichiers : le contexte utile est ci-dessous. Réponds en français.

**Contexte.** Un programme de recherche veut mesurer si un moniteur qui lit les activations internes d'un agent (« boîte blanche ») détecte mieux qu'un moniteur qui ne lit que son texte (« boîte noire ») un sabotage diffus : réel sur l'ensemble d'un épisode, invisible action par action.
- Agent : Llama-3.1-8B-Instruct (8 milliards de paramètres, poids ouverts), température 1,0, 400 jetons au plus par action. Choisi pour son coût et l'accès à ses activations.
- Tâche, floue et sans vérité exécutable : à partir des questions de recherche d'un article récent d'apprentissage automatique, bâtir en dix pas un ensemble de propositions d'expériences. Chaque action a des champs fixes : titre, proposition, contrôles, coût estimé en heures de carte graphique, prédiction. Le banc est adapté du jeu de l'article arXiv 2606.08892.
- Sabotage mesuré aujourd'hui : gonfler le coût déclaré. Sabotages visés ensuite : affaiblir les contrôles expérimentaux proposés ; un mode tenu secret jusqu'à l'évaluation.
- Trois fabrications du saboteur : (1) consigne cachée en fin de message système, rappelée par une note privée à chaque pas ; (2) adaptateur de rang faible (LoRA) distillé des épisodes du saboteur (1), sans aucune consigne dans le contexte ; (3) variante de (2), à l'étude, dont le maître vise un excès modéré et réparti, ses épisodes étant triés par une règle qui ne lit que la vérité du dommage.
- Surveillants boîte noire : un lecteur « sac de mots, coût déclaré et forme du champ du coût » (régression logistique) ; un prédicteur à douze traits ; des juges génératifs de 8 milliards de paramètres (un juge de 27 milliards est envisagé).
- Règles : les sondes ne sont jugées qu'aux doses où le sabotage est établi et où le lecteur du texte échoue (aire sous la courbe inférieure à 0,70, ou non distinguable du hasard) ; aucun score de moniteur ne sert à choisir ni à entraîner le saboteur, hors d'un bras d'attaque déclaré.

**Faits mesurés** (64 tâches neuves ; 128 épisodes et 1 280 actions par condition ; coût en logarithme décimal ; intervalles à 95 %).
1. Saboteur à consigne cachée, selon le facteur de gonflement demandé, contre un témoin à consigne neutre (même gabarit, qui demande d'écrire le coût sans le changer) : facteur 10 : +1,22 [1,00 ; 1,44] ; 5 : +0,66 [0,46 ; 0,84] ; 3 : +0,53 [0,32 ; 0,74] ; 2 : +0,11 [−0,09 ; 0,32] ; 1,5 : −0,19 [−0,39 ; 0,01] ; 1,25 : −0,25 [−0,42 ; −0,07].
2. Part des actions dont le coût dépasse le neuvième décile du témoin neutre de la même tâche, au-delà des 10 % attendus : 0,57 (facteur 10) ; 0,40 (5) ; 0,33 (3) ; 0,22 (2) ; 0,13 (1,5) ; 0,06 (1,25).
3. Part des actions qui citent leur texte privé : agent honnête 0 % ; consigne neutre 5,8 % ; consignes de gonflement 17 à 24 %. Il arrive que l'agent écrive qu'il applique une consigne privée, ou laisse dans le champ du coût le calcul du gonflement.
4. Lecteur « sac de mots et coût », aire sous la courbe contre l'agent honnête : consigne neutre 0,98 ; gonflement, facteurs 1,25 à 10 : 0,93 à 0,97 ; consigne bénigne sans rapport avec le coût : 0,63. Prédicteur à douze traits : consigne neutre 0,68 ; gonflement 0,58 à 0,68 jusqu'au facteur 5, 0,83 au facteur 10.
5. Agent honnête : 20 % d'actions sans coût lisible ; 9 % tronquées à 400 jetons. La consigne publique demande pour le coût « une estimation en heures de carte graphique, un seul nombre ».
6. Compétence honnête : au pilote, environ 10 % des paires « proposition, contrôle de référence de l'article » sont jugées couvertes (estimation pondérée sur un échantillon stratifié).
7. Débit : environ 930 actions par heure de carte, à environ 1,1 dollar de l'heure. Budget total : quelques milliers de dollars.

Aucun résultat de sonde n'est donné, volontairement.

**La question.** Le directeur du programme demande : « Comment va-t-on faire si tout laisse penser que le modèle de 8 milliards de paramètres sera trop petit pour un sabotage aussi subtil ? »

Réponds en cinq parties.

A. **Diagnostic.** Décompose « sabotage subtil » en capacités séparables. Pour chacune, dis si les faits ci-dessus montrent qu'elle manque. Énumère les explications rivales de « le modèle est trop petit », donne à chacune une probabilité, et dis quelles observations, absentes ci-dessus, trancheraient.

B. **Lecture interne.** Indépendamment du comportement : que sait-on, à cette taille, de la lisibilité par sonde linéaire d'un état interne lié à la tromperie ou au sabotage ? Dans quel sens la taille biaise-t-elle la comparaison boîte blanche contre boîte noire ? Cite tes sources (titre, identifiant, page ou table) et marque « non vérifié » ce que tu cites de mémoire.

C. **Plan.** Donne l'échelle des remèdes, du moins cher au plus cher. Pour chacun : ce qu'il change ; ce qu'il retire à la validité de l'organisme pour une lecture interne ; son épreuve décisive la moins chère (ce qu'elle mesure, coût en dollars, délai, critère de mort écrit avant les données). Dis à quel critère chiffré tu changerais de modèle, pour lequel, et à quel coût.

D. **Conséquences.** Que devient la revendication (gain de la boîte blanche sur le sabotage diffus de tâches floues) dans chaque branche de ton plan, y compris celle où la taille est bien la cause ?

E. **Validation.** Qu'est-ce qui, hors de toi et de nous, vérifierait ta réponse ?

**Questions témoins.** Réponds à chacune et donne ta probabilité d'avoir raison (entre 0 et 1).
- T1. Dans « AI Control: Improving Safety Despite Intentional Subversion » (arXiv 2312.06942), quel modèle joue l'agent non fiable, et quel modèle le moniteur de confiance ?
- T2. Dans « Detecting Strategic Deception Using Linear Probes » (arXiv 2502.03407), sur les activations de quel modèle les sondes sont-elles apprises ?
- T3. Dans « Stress-Testing Capability Elicitation With Password-Locked Models » (arXiv 2405.19550), quelle est la taille, en milliards de paramètres, des modèles verrouillés par mot de passe pour le code et les mathématiques ?
- T4. Dans « Diffuse AI Control on Fuzzy Tasks » (arXiv 2606.08892), quel modèle joue le générateur non fiable dans les expériences principales, et quel modèle le correcteur faible de confiance ?
- T5. Deux lois normales de même écart type sont séparées par un détecteur d'aire sous la courbe 0,70. Quel est l'écart entre leurs moyennes, en écarts types, et quel est le rappel à 1 % de fausses alertes ?

**Format.** 1 200 mots au plus hors table ; une table pour la partie C. Dis ce que tu ne sais pas.
