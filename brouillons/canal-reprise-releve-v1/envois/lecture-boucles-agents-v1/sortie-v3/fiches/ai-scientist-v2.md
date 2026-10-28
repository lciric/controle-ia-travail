# « The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search » — fiche de lecture (passe v3)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Yutaro Yamada, Robert Tjarko Lange, Cong Lu (contribution égale), Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha. « The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search ». Sakana AI ; Université de Colombie-Britannique ; Vector Institute ; FLAIR, Université d'Oxford ; chaire Canada CIFAR (p. 1).
- Prépublication arXiv 2504.08066, version 1 du 10 avril 2025 (tampon, p. 1) ; en-tête daté 2025-4-14. Lieu : aucun indiqué sur le PDF.

## Fichier lu
- `pdfs/ai-scientist-v2/arxiv-2504.08066v1.pdf`, 8 923 691 octets, 69 pages ; SHA-256 `53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2` (même empreinte que la v1).
- Pages lues : 1 à 16 (texte et références) et 21 (annexe A, hyperparamètres). Annexes C (articles soumis et revues internes, p. 22 à 69) fouillées par mots clés, dont p. 42.

## Comment la boucle est faite
- Qui propose : idées générées à un niveau abstrait, « akin to » une proposition de recherche, avec Semantic Scholar dans la boucle pour juger la nouveauté (p. 4). Plus de gabarit de code humain (p. 1 et 4).
- Qui teste : un « experiment progress manager » conduit quatre étapes, chacune avec un critère d'arrêt explicite (p. 5) :
  1. faisabilité ;
  2. réglage des hyperparamètres ;
  3. programme de recherche ;
  4. ablations.

  Les étapes 3 et 4 s'arrêtent à épuisement du budget de calcul (p. 5).
- Arbre de recherche agentique (p. 5 à 7). Chaque nœud contient :
  - un plan et du code écrits par un modèle, exécutés aussitôt ;
  - en cas d'erreur, le nœud est marqué défectueux et sera débogué ;
  - sinon, les figures sont soumises à un modèle de vision et de langue, qui peut aussi marquer le nœud défectueux (p. 5).

  À chaque itération, plusieurs nœuds sont développés en parallèle : un nœud défectueux avec une probabilité fixée, sinon un nœud sain choisi en « best-first » (p. 7).
- Qui sélectionne : un modèle de langue, juge interne. Il guide le choix des nœuds d'après les métriques, la dynamique d'entraînement et la qualité des figures (p. 7). À la fin de chaque étape, un évaluateur dédié choisit le meilleur nœud, qui sert de racine à l'étape suivante (p. 5).
- Mémoire : l'arbre (code, plan, traces d'erreur, métriques, retours du modèle de langue et du modèle de vision) et les points de contrôle de chaque étape (p. 5 et 7). Les hyperparamètres et ablations déjà essayés sont tracés pour éviter les répétitions (p. 7).
- Paramètres (annexe A, p. 21) :
  - code écrit par Claude 3.5 Sonnet (v2) ; retours par GPT-4o ;
  - probabilité de débogage 1,0, profondeur de débogage au plus 3 ;
  - au plus 1 heure par nœud ; 21, 12, 12 et 12 nœuds selon l'étape ;
  - plusieurs heures à 15 heures au plus par article.

## Traitement du bruit et du sur-ajustement
- Réplications : à la fin de chaque étape, le gestionnaire relance plusieurs fois les meilleures expériences avec des graines différentes ; des nœuds d'agrégation produisent moyennes et écarts types (p. 5 et 7).
- Jeux de données : chargés depuis Hugging Face avec leurs parts « predefined train, validation, and test » (p. 7). Les auteurs reconnaissent que la démarche est « somewhat ad-hoc » (p. 7).
- Sélection humaine sur des courses multiples :
  - environ quarante idées générées ; les humains en retiennent trois (p. 10) ;
  - chaque idée passe par plusieurs courses complètes de graines différentes ;
  - pour chaque idée, les humains soumettent le « single best-resulting manuscript » après inspection (p. 10).

  Les auteurs disent viser « at least one paper » qui passe la relecture, « not what fraction of the time » (p. 10).
- Contrôle externe : relecture en aveugle d'un atelier de la conférence International Conference on Learning Representations 2025 (« I Can't Believe It's Not Better »), avec 43 soumissions dont 3 générées. L'une obtient 6,33 en moyenne (notes 6, 6 et 7) et aurait été acceptée ; elle a été retirée ensuite, comme convenu (p. 8 et 9).
- Revue interne des auteurs (p. 11 ; annexe p. 42) : environ 57 % de recouvrement entre jeux d'entraînement et de test dans l'article accepté. La précision de 100 % rapportée tient à la simplicité de la tâche. Des légendes de figures sont fausses.

## Échecs et limites rapportés par les auteurs
- Citations parfois hallucinées ; rigueur méthodologique insuffisante pour une conférence principale (p. 9).
- Acceptation au niveau d'un atelier seulement, et pour un article sur trois ; taux d'acceptation des ateliers de 60 à 80 % contre 20 à 30 % pour les conférences principales (p. 13). Le système n'atteint « not yet consistently » le niveau requis (p. 13).
- Hypothèses vraiment nouvelles et méthodes vraiment innovantes restent difficiles (p. 13).

## Vérifié par des tiers
- La relecture de l'atelier est un contrôle externe, mais sur un article choisi par les auteurs parmi plusieurs courses (p. 9 et 10). Aucune réplication indépendante de la v2 trouvée dans les lectures. Les auteurs citent Beel et al. comme évaluation indépendante de la v1 (p. 14).

## À emprunter
- Boucle extérieure : distinguer le meilleur de n choisi par un humain (ce que fait la v2, p. 10) de la fréquence de réussite. Pour une revendication « au-delà du bruit », c'est la fréquence qu'il faut mesurer.
- Boucle intérieure : relancer automatiquement les meilleurs nœuds sur plusieurs graines avant de les promouvoir (p. 5 et 7), avec des critères d'arrêt explicites et un budget de nœuds par étape (p. 5 et 21).
- Mesure du bruit : contrôler les fuites entre parts — les 57 % de recouvrement n'ont été vus qu'à la relecture humaine du code (p. 11 et 42).
