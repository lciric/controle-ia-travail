# Demande 36 — comment éviter que les réponses des modèles soient coupées dans une requête dense

Question du directeur, verbatim : « comment éviter que les réponses des modèles de la passe X ne soient coupées par faute de réflexion trop longue ou réponse trop longue, ce qui risque d'arriver étant donné la densité de la demande dans la passe X ??? »

Faits : une seule pièce d'environ 21 000 signes fusionne dix-huit questions ouvertes, chacune longue et exigeante ; elle est servie une fois à neuf modèles de quatre fournisseurs (Anthropic : Opus 5.5, Fable 5.1, Opus 4.6, Sonnet 4.6 ; Google : Argon, Carbon, Neon ; OpenAI : Astra ; Moonshot : Kimi). Réglages prévus : sortie de 96 000 jetons pour Anthropic, OpenAI et Kimi ; 65 536 pour Google, dont 49 152 de réflexion comptée ; effort maximal là où il est admis. Une réponse coupée (fin en longueur maximale, réflexion qui épuise la sortie, texte vide) est un défaut, jamais une réponse. Un constat récent : chez Anthropic, l'effort maximal sans budget de tâche a épuisé toute la sortie dans la réflexion quatre fois sur cinq ; avec un budget égal à l'entrée plus 90 000 jetons, il a rendu un texte complet.

Réponds en 900 mots au plus :
1. Le risque réel de coupure, modèle par modèle, avec ces réglages, et ce qui le fait monter.
2. Les formes qui l'évitent, de la plus sûre à la moins sûre : une requête par question, des requêtes par groupes, une consigne de longueur par question, un budget de tâche, une réponse en plusieurs tours, une reprise automatique après une coupure. Pour chacune : ce qu'elle coûte en plus et ce qu'elle change à la lecture (comparabilité, quarantaine).
3. Ta recommandation précise pour cette passe, avec les réglages par fournisseur.
4. La garde qui détecte une coupure et ce qu'elle fait alors.
Termine par « FIN DE LA RÉPONSE ».
