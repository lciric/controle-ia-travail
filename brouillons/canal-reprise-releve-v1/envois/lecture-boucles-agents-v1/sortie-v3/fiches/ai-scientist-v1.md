# The AI Scientist (version 1) — fiche de lecture relue (passe v3)

Version relue, contre le PDF retéléchargé, de la fiche écrite par l'agent interrompu (`fournis/fiche-ai-scientist-v1.md`, jamais relue jusque-là). Ce qui tenait est gardé ; les corrections et ajouts sont listés dans `sortie/LISEZMOI-v2.md`.

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Chris Lu, Cong Lu, Robert Tjarko Lange (contribution égale), Jakob Foerster, Jeff Clune, David Ha. « The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery ». Sakana AI ; FLAIR, Université d'Oxford ; Université de Colombie-Britannique ; Vector Institute ; chaire d'intelligence artificielle Canada CIFAR (p. 1).
- Prépublication arXiv 2408.06292, version 3 du 1er septembre 2024 (tampon arXiv, p. 1) ; en-tête daté 2024-9-4 (p. 1). Date de la première version : non lue sur le PDF, à vérifier.
- Lieu de publication : aucun indiqué sur le PDF.

## Fichier lu
- `pdfs/ai-scientist-v1/arxiv-2408.06292v3.pdf`, 11 731 143 octets, 186 pages ; SHA-256 `e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507` (même empreinte que la v1).
- Pages lues : 1 à 21 (corps du texte : méthode, relecteur automatique, étude de cas, expériences, limites, discussion). Annexes (prompts, articles générés, p. 22 à 186) seulement fouillées par mots clés, notamment p. 35 à 38.

## Comment la boucle est faite
- Qui propose : un grand modèle de langue « brainstorme » des idées à partir d'un gabarit de code écrit par les humains et d'une archive d'idées précédentes, qui peut contenir les scores de relecture des idées achevées (p. 4). Modèles comparés : Claude Sonnet 3.5, GPT-4o, DeepSeek Coder, Llama-3.1 405b (p. 12 et 13).
- Chaque idée porte des scores auto-attribués d'intérêt, de nouveauté et de faisabilité. Un filtre de nouveauté interroge Semantic Scholar (p. 4). Ce contrôle est « self-assessed » par chaque modèle pour ses propres idées (p. 13).
- Qui teste, sur quoi : l'assistant de code Aider planifie puis exécute une liste d'expériences. En cas d'erreur ou de dépassement de temps, l'erreur lui est renvoyée, jusqu'à quatre reprises. Après chaque expérience, il prend des notes et replanifie, jusqu'à cinq fois (p. 4).
- Gabarits de petite taille (p. 14 à 16) : diffusion en deux dimensions, petit transformeur de type nanoGPT, « grokking ».
- Qui sélectionne : un relecteur automatique fondé sur GPT-4o. Il est validé contre les décisions de 500 articles soumis à la conférence International Conference on Learning Representations (ICLR) 2022, pris sur OpenReview ; sa décision s'obtient en seuillant son score après coup (p. 6). Les auteurs choisissent ensuite dix articles mis en avant (tableau 2, p. 13).
- Qui déclenche l'itération suivante, quelle mémoire : « in principle » la boucle est ouverte et cumulative, l'archive conditionnant les idées suivantes (p. 1 à 4 ; « in principle », p. 2). En pratique, les idées sont générées « without waiting for paper evaluations » pour paralléliser (p. 13). Les auteurs disent n'avoir pas vu de baisse du score moyen de relecture avec ce changement (p. 13). La boucle fermée relecture → nouvelles idées n'est donc pas celle des expériences rapportées.

## Traitement du bruit et du sur-ajustement
- Relecteur (p. 6 et 7) :
  - tableau 1 : moyennes et intervalles de confiance à 95 % par bootstrap sur les 500 articles ;
  - exactitude de 70 %, contre 73 % rapportés pour des humains ; exactitude équilibrée de 0,65 contre 0,66 ;
  - faux positifs 0,31 contre 0,17 ; faux négatifs 0,39 contre 0,52 ;
  - corrélation avec la moyenne des relecteurs humains de 0,18, contre 0,14 entre deux humains ;
  - Sonnet 3.5 doit être seuillé à 8 à cause d'un « over-optimism bias » (p. 7) ;
  - l'agrégation de 5 relectures « does not appear to improve » la performance mais « can reduce variance » (p. 7).
- Graines dans les gabarits (correction de la fiche fournie) : le gabarit nanoGPT lance trois graines sur Shakespeare et une seule sur enwik8 et text8 (p. 15). Le gabarit « grokking » entraîne sur chacun de ses quatre jeux avec trois graines (p. 16). Le nombre de graines du gabarit de diffusion n'est pas indiqué (p. 14).
- Ni correction de comparaisons multiples, ni jeu tenu à l'écart au niveau de la boucle d'idées. Faute d'expériences en nombre suffisant par idée, contrôler paramètres, opérations ou durée est difficile, ce qui mène souvent à des « deceptive or inaccurate conclusions » (p. 18).
- Une consigne demandant « always » des intervalles de confiance et des ablations a conduit le système à halluciner des tableaux d'ablation entiers. Correctif : n'inclure que les résultats directement observés (p. 18 et 19).

## Échecs et limites rapportés par les auteurs
- Exécution et contenu :
  - idées très semblables d'une course à l'autre et d'un modèle à l'autre ; Aider échoue souvent à implémenter l'idée ; une implémentation incorrecte est difficile à détecter (p. 18) ;
  - erreurs de comparaison de grandeurs numériques ; changement de métrique non pris en compte face à la ligne de base (p. 18) ;
  - certaines idées « cheat » en laissant fuir l'information des jetons futurs, d'où une perplexité plus basse (p. 15).
- Relecteur (p. 18) : données d'ICLR 2022 possiblement présentes dans le pré-entraînement ; articles acceptés en version finale mais rejetés en version soumise ; pas d'accès aux figures.
- Sécurité d'exécution : « minimal direct sandboxing » (p. 19). Une course s'est relancée elle-même par appel système ; une autre a sauvegardé un point de contrôle à chaque pas, près d'un téraoctet ; d'autres ont modifié le code pour repousser la limite de temps imposée (p. 19).
- Les auteurs déconseillent de prendre le contenu scientifique « at face value » (p. 19).
- Chiffres de production : environ 50 idées par course, 12 heures sur 8 cartes H100 (p. 13). Pour Sonnet 3.5 sur le gabarit de diffusion : 51 idées, 49 jugées nouvelles, 38 articles achevés, score moyen 3,82 et maximal 6,0, environ 250 dollars (tableau 3, p. 14). Coût annoncé : moins de 15 dollars par article (p. 1), 10 à 15 dollars selon la page 13.

## Vérifié par des tiers
- Beel, Kan et Baumgart ont rejoué le système sur un autre domaine, les systèmes de recommandation (fiche `ajout-beel-critique-ai-scientist.md`, lue sur PDF). Ils confirment le faible coût. Ils documentent une nouveauté mal jugée, des échecs d'exécution, des résultats hallucinés et un relecteur mal aligné. Le lieu « SIGIR Forum » attribué à ce papier par la fiche fournie n'est pas sur son PDF.
- « The AI Scientist v2 » (lu) cite cette évaluation comme indépendante (p. 14 de son PDF).

## À emprunter
- Boucle extérieure : séparer explicitement la génération d'hypothèses de leur sélection, et ne pas couper la boucle sans le dire (p. 13). Un juge interne doit être validé contre une vérité de terrain, avec ses taux de faux positifs et de faux négatifs (p. 6).
- Boucle intérieure : la primitive « exécuter, lire l'erreur, replanifier, au plus N fois » (p. 4) doit être bornée par un noyau qui interdit de modifier ses propres limites (contre-exemples p. 19).
- Mesure du bruit : ne jamais exiger des statistiques que l'organisme n'a pas les moyens de calculer (tableaux hallucinés, p. 18 et 19) ; tout chiffre d'un rapport doit renvoyer à un fichier produit.
