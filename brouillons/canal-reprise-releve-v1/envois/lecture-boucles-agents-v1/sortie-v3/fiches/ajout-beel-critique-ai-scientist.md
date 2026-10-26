# Beel, Kan, Baumgart — « Evaluating Sakana's AI Scientist for Autonomous Research » — fiche de lecture (passe v3, ajouté)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Joeran Beel (Université de Siegen), Min-Yen Kan (Université nationale de Singapour), Moritz Baumgart (Université de Siegen). « Evaluating Sakana's AI Scientist for Autonomous Research: Wishful Thinking or an Emerging Reality Towards 'Artificial Research Intelligence' (ARI)? » (p. 1).
- Prépublication arXiv 2502.14297, version 3 du 15 octobre 2025, catégorie recherche d'information (tampon, p. 1).
- Lieu : le PDF porte « Manuscript submitted to ACM » et une référence de format ACM au numéro d'identifiant fictif (p. 1 et 2) ; le texte dit le manuscrit soumis à « a major IR conference », une grande conférence de recherche d'information (p. 2). Aucun lieu de publication confirmé sur le PDF : à vérifier. La fiche de l'agent interrompu disait « SIGIR Forum » : non retrouvé comme lieu de ce papier ; SIGIR Forum n'apparaît que dans la référence d'un autre article des mêmes auteurs (p. 16).
- Le titre a changé entre versions : « The AI Scientist v2 » cite une version antérieure intitulée « … towards 'artificial general research intelligence' (agri)? » (p. 15 de son PDF).
- Marqué « ajouté » par la v1.

## Fichier lu
- `pdfs/ajout-beel-critique-ai-scientist/arxiv-2502.14297v3.pdf`, 549 562 octets, 16 pages ; SHA-256 `8cb4dcd15be2d46e9e475e852c5c93922c56eeaa12ca5bdc03b5c2ae471b1854` (même empreinte que la v1).
- Pages lues : 1 à 12 ; 13 à 16 (recommandations, références) parcourues.

## Comment la boucle est faite
- C'est une évaluation indépendante de « The AI Scientist » (version 1), rejouée sur un domaine neuf : systèmes de recommandation « verts », algorithme FunkSVD, MovieLens-100k découpé 80/10/10, mesure par la racine de l'erreur quadratique moyenne (p. 4 et 5). Modèle utilisé : gpt-4o-2024-05-13 (p. 4).
- La boucle évaluée (p. 4 à 6) : un gabarit et deux idées de départ fournis par l'humain ; le système génère dix idées, juge leur nouveauté par Semantic Scholar (jusqu'à 10 résultats par requête, jusqu'à 10 itérations), puis Aider modifie le code jusqu'à cinq fois.
- Mise en œuvre par un étudiant de troisième année de licence en informatique (p. 4).

## Traitement du bruit et du sur-ajustement
- Dans le système évalué : aucun. Les manuscrits présentent les métriques « with no confidence intervals or p-values » (p. 7). Un gain annoncé de 116 à 115 secondes d'entraînement n'est discuté ni statistiquement ni pratiquement (p. 7).
- Les scores d'intérêt, de faisabilité et de nouveauté « appear arbitrarily assigned » et ne servent pas ensuite (p. 6) ; ceux des idées de départ n'ont « no apparent impact » (p. 5).
- Dans l'évaluation elle-même : un seul jeu de données, un domaine, deux idées de départ, un gabarit ; les auteurs le reconnaissent (p. 9). Chiffres sur 12 idées et 7 manuscrits, sans intervalles.

## Échecs et limites rapportés
- Sur le système évalué :
  - les 10 idées générées et les 2 idées de départ sont toutes classées nouvelles, y compris des techniques connues comme le micro-lot pour la descente de gradient stochastique (p. 6) ;
  - 5 idées sur 12 échouent sur des erreurs de code (p. 6) ;
  - Aider modifie peu le code : +8 % de caractères à la première itération, puis presque rien (p. 6 et 7) ;
  - erreurs de méthode : paramètre e resté fixé à 2 au lieu de varier, ligne de base non relancée, d'où une supériorité « impossible » (p. 6 et 7) ;
  - le système « cannot critically assess its own results » (p. 7).
- Sur les manuscrits (p. 7) : médiane de 5 références, 5 sur 34 seulement de 2020 ou après (14,7 %) ; 4 manuscrits sur 7 avec des défauts de structure ; 4 sur 7 avec des résultats numériques faux ou hallucinés.
- Sur le relecteur interne (p. 8) : il rejette les 7 manuscrits générés sans voir leurs défauts graves. Sur 10 articles humains (5 acceptés, 5 rejetés), il en rejette 9, dont 4 acceptés, et accepte un article rejeté : biais conservateur et désalignement avec le jugement humain.
- Coût et temps : 42 dollars en tout, soit 6 dollars par manuscrit ; 25 heures humaines hors installation, soit environ 3,5 heures par manuscrit (p. 9).

## Vérifié par des tiers
- C'est lui-même la vérification par des tiers de « The AI Scientist ». « The AI Scientist v2 » le cite comme évaluation indépendante (p. 14 de son PDF). Pas de vérification de cette évaluation trouvée.

## À emprunter
- Boucle extérieure : un juge interne se valide sur des cas dont l'issue est connue, positifs et négatifs. Le test de Beel (10 articles, 5 acceptés, 5 rejetés, p. 8) est minimal mais révèle un biais.
- Boucle intérieure : exiger que toute comparaison relance la ligne de base dans la même course ; c'est l'échec type relevé p. 6 et 7.
- Mesure du bruit : les gains minuscules (1 % de temps, p. 7) doivent être lus contre le bruit de mesure ; sans intervalle, ils ne valent rien.
