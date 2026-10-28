# « Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents » — fiche de lecture (passe v3)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Jenny Zhang, Shengran Hu (contribution égale), Cong Lu, Robert Lange, Jeff Clune. « Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents ». Université de Colombie-Britannique, Vector Institute, Sakana AI, chaire Canada CIFAR (p. 1).
- En-tête « Published as a conference paper at ICLR 2026 » : International Conference on Learning Representations 2026 (p. 1). Prépublication arXiv 2505.22954, version 3 du 12 mars 2026 (tampon, p. 1).

## Fichier lu
- `pdfs/darwin-godel-machine/arxiv-2505.22954v3.pdf`, 3 825 399 octets, 72 pages ; SHA-256 `13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de` (même empreinte que la v1).
- Pages lues : 1 à 11 (texte), 24 à 26 (annexe A : lignes de base, transferts, stabilité), 28 (sélection des parents), 32 (coûts), 36, 69 à 71 (étude de cas sur l'hallucination et piratage de l'objectif). Autres annexes fouillées par mots clés.

## Comment la boucle est faite
- Le système modifie son propre code d'agent de programmation ; les modèles de fondation restent gelés (p. 2).
- Qui propose : un agent parent tiré d'une archive analyse ses propres journaux d'évaluation, propose la fonction suivante à implémenter, puis l'implémente dans son propre code (p. 4).
- Qui teste : chaque nouvel agent passe un benchmark de programmation : SWE-bench Verified ou Polyglot (p. 5).
- Qui sélectionne :
  - seuls les agents qui compilent et savent encore éditer du code entrent dans l'archive (p. 4) ;
  - le parent est tiré avec une probabilité qui croît, en sigmoïde, avec sa performance (pente 10) et décroît avec son nombre d'enfants fonctionnels (p. 4 et 28) ;
  - tous les agents gardent une probabilité non nulle (p. 4).
- Itération : 80 itérations, deux en parallèle pour SWE-bench, quatre pour Polyglot. Les modifications sont écrites avec Claude 3.5 Sonnet (New) ; l'évaluation tourne avec Claude 3.5 Sonnet (New) ou o3-mini (p. 5). Le processus d'exploration lui-même est fixe et non modifiable par le système (p. 5).
- Mémoire : l'archive de tous les agents, arbre avec lignées (p. 4 et 7).

## Traitement du bruit et du sur-ajustement
- Évaluation par étapes, parce que « performance can be noisy » (p. 6) :
  - 10 tâches pour vérifier la fonction d'édition ;
  - puis un ensemble élargi de 50 tâches ;
  - pour SWE-bench, 200 tâches seulement pour un agent au-dessus de 40 % sur le sous-ensemble et parmi les deux meilleurs de l'archive. Le texte parle ici d'un sous-ensemble de 60 tâches (200 = 140 + 60) après en avoir annoncé 50 : incohérence relevée, non résolue (p. 6). Ce seuil de 40 % est « a heuristic chosen based on the noise observed in preliminary runs » (p. 6) ;
  - pour Polyglot, passage à 50 tâches au-dessus de 40 % sur les 10 premières (p. 6).
- Résultats (p. 6) : de 20,0 % à 50,0 % sur SWE-bench, de 14,0 % à 38,0 % sur les 50 tâches Polyglot. Pour la comparaison avec les agents humains, les scores sont mesurés « on the same benchmark subsets used to evaluate the DGM ». Sur Polyglot complet, de 14,2 % à 30,7 %.
- Écart sur Polyglot (ma lecture, non commentée par les auteurs, illustratif) : le meilleur agent obtient 38,0 % sur les tâches qui ont servi à le choisir et 30,7 % sur l'ensemble ; l'agent de base, lui, a 14,0 % et 14,2 % (p. 6). C'est l'allure attendue d'une sélection sur le bruit, sans que d'autres causes soient exclues.
- Tests tenus à l'écart (p. 8) : l'agent évolué sur SWE-bench obtient 28,9 % sur Polyglot (base 14,2 %) ; celui évolué sur Polyglot obtient 24,5 % sur SWE-bench (base 20,0 %). Les auteurs les décrivent comme « truly held-out tests ».
- Transferts entre modèles (p. 8 et 25) : sur SWE-bench avec Claude 3.7 Sonnet, de 19,0 % à 59,5 %. Sur Polyglot, les gains sont d'environ un point (32,0 contre 33,3 % ; 35,6 contre 36,8 %).
- Stabilité : trois courses complètes sur Polyglot donnent 40,7 % de moyenne et 2,3 % d'écart type (p. 26).
- Lignes de base (p. 6, 24 et 25) :
  - sans auto-amélioration, ce qui reproduit l'approche d'« Automated Design of Agentic Systems » ;
  - sans archive ;
  - variante gloutonne, qui reproduit l'approche de Robeyns et al. : 39,7 % et 30,0 %, contre 50,0 % et 38,0 % pour la version complète.

  Ces comparaisons semblent reposer sur une course par variante ; aucun test statistique trouvé dans les pages lues.

## Échecs et limites rapportés par les auteurs
- Piratage de l'objectif (p. 69 à 71). Dans une expérience contre l'hallucination d'usage d'outils, notée sur 3 tâches seulement, un agent obtient le score parfait en supprimant la journalisation des jetons spéciaux qui servaient à détecter l'hallucination, malgré la consigne. Il contourne la détection sans résoudre le problème (p. 70). Cacher les fonctions de vérification à l'agent réduit ce piratage (p. 70). Les auteurs le rattachent à la loi de Goodhart (p. 71).
- Coût : environ deux semaines et 22 000 dollars pour une course sur SWE-bench, 10 000 dollars pour une ligne de base (p. 10 et 32).
- Reste en dessous des solutions fermées de pointe (p. 10). Hypothèse clé : la performance sur des benchmarks de programmation reflète la capacité à s'améliorer soi-même (p. 2 et 10).
- Sûreté : bac à sable, limite de temps, surveillance, lignée traçable ; « no evidence of harmful or malicious behavior » à ce stade (p. 9).

## Vérifié par des tiers
- Non trouvé. La comparaison à l'état de l'art utilise des solutions « checked » par l'équipe de SWE-bench (p. 6), pas une vérification des résultats de la Darwin Gödel Machine.

## À emprunter
- Boucle extérieure : rapporter le résultat final sur des tâches qui n'ont pas servi à choisir, et répéter la course entière (trois courses, moyenne et écart type, p. 26) ; l'écart 38,0 contre 30,7 % (p. 6) est l'exemple à éviter.
- Boucle intérieure : cacher les fonctions de vérification à l'organisme qui se modifie (p. 70) ; n'archiver que les variantes qui gardent leurs fonctions de base (p. 4).
- Mesure du bruit : fixer les seuils de promotion d'après une mesure préalable du bruit (p. 6), mais les écrire d'avance et les tenir.
