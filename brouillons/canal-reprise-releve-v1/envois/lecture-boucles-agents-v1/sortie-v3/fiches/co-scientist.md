# « Accelerating scientific discovery with Co-Scientist » (AI co-scientist) — fiche de lecture (passe v3)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Petar Sirkovic et al. (liste complète p. 1). Google Cloud AI Research, Google DeepMind, Google Research, École de médecine de l'Université Stanford, Houston Methodist, Sequome, Fleming Initiative et Imperial College London (p. 1).
- Titre sur ce PDF : « Accelerating scientific discovery with Co-Scientist » (p. 1). « The AI Scientist v2 » (lu) cite une version antérieure du même identifiant sous le titre « Towards an ai co-scientist » (p. 15 de son PDF) : le titre a changé entre versions.
- Identifiant arXiv 2502.18864, version 2 d'après la liste v1. Le PDF ne porte ni tampon arXiv ni date ; il est rendu par Google Docs, avec pour titre interne « [CoS] Nature revision AAP ». Le texte cite des modèles récents (« Gemini 3, GPT 5.4 and Opus 4.6 », p. 24) : c'est une révision tardive. Date et lieu de publication : à vérifier.

## Fichier lu
- `pdfs/co-scientist/arxiv-2502.18864v2.pdf`, 5 885 207 octets, 157 pages ; SHA-256 `e603a77c9d2bdfb528313e4cf35405b72261e018a70da724fcebca94c96e4716` (même empreinte que la v1).
- Pages lues : 1 à 25 (texte principal et limites), 29 à 39 (méthodes), 44 à 46 (évaluation interne du classement Elo) ; le reste (notes supplémentaires, exemples) fouillé par mots clés, dont p. 76.

## Comment la boucle est faite
- Un agent superviseur lit l'objectif de recherche du scientifique et répartit le calcul entre des agents spécialisés, dans une file de tâches asynchrone (p. 5) :
  - génération ;
  - réflexion (critique) ;
  - classement ;
  - évolution ;
  - proximité (graphe de similarité) ;
  - méta-revue.
- Qui sélectionne : un tournoi Elo, juge interne (p. 34 et 35) :
  - chaque hypothèse entre à 1200 ;
  - les mieux classées s'affrontent deux à deux en débats scientifiques à plusieurs tours, ce qui doit atténuer le biais d'ordre ; les autres, en comparaisons à un tour ;
  - les matchs privilégient les hypothèses semblables, récentes ou bien classées.
- Itération : l'évolution raffine les meilleures hypothèses, la méta-revue renvoie des critiques générales aux agents (p. 5 et 29 à 35). Le scientifique peut proposer ses idées, commenter, réorienter (p. 3).
- Mémoire : un contexte persistant pour le raisonnement long (p. 7).

## Traitement du bruit et du sur-ajustement
- Le juge est explicitement un auto-classement : l'Elo « is auto-evaluated and not based on independent ground truth » (p. 10).
- Validation du juge contre une vérité de terrain (annexe, p. 45 et 46) :
  - sur les questions de GPQA diamond, les réponses sont groupées par tranche d'Elo de 50 points (p. 45) ;
  - la difficulté des questions est contrôlée par une référence : 32 réponses du modèle Gemini 2.0 par question, parce que les tranches ne couvrent pas les questions uniformément (p. 45) ;
  - résultat : concordance entre Elo et exactitude ; exactitude de 78,4 % en retenant la réponse au meilleur Elo (p. 45) ; intervalles à 95 % en ombre sur la figure (p. 46).
- Ablations (p. 38) :
  - sans recherche externe, le critique donne 6,14 sur 10 de nouveauté à des idées déjà publiées, contre 2,38 avec recherche ; aire sous la courbe sur GPQA de 0,643 à 0,651 avec la recherche ;
  - le prompt de débat réduit le biais de position ;
  - l'évolution fait passer la précision sur GPQA de 70,9 % à 75,4 %.
- Autre contrôle du juge (note supplémentaire, p. 76) : le score de revue du système croît avec un score externe de dépendance des lignées cancéreuses (DepMap), sur des dizaines de milliers de paires médicament-cancer ; tests de Wilcoxon « without multiple comparison adjustments ».
- Statistiques (p. 38 et 39) : tailles d'échantillon non fixées par une méthode statistique ; trois réplicats biologiques choisis selon l'usage des criblages préliminaires ; « All attempts at replication » réussies, en calcul comme in vitro ; évaluation par les experts faite en aveugle.
- Calcul au moment du test : Elo moyen par décile de temps de génération sur 203 objectifs de recherche (p. 7 et 8).
- Évaluation par des experts (p. 10 et 11) :
  - sur 11 objectifs, rang moyen de préférence 2,36 sur 4 ; nouveauté 3,64 et impact 3,09 sur 5 ;
  - les auteurs écrivent : « subjective expert assessments, not objective ground truth » et « further studies are necessary » vu la petite taille (p. 11).
- Biologie :
  - essais in vitro pour la leucémie aiguë myéloïde : concentrations d'inhibition à 50 %, moyenne ± écart type sur n = 3 expériences biologiquement indépendantes (p. 14 et 15) ;
  - les experts ont choisi les trois meilleurs candidats à tester (p. 15) ;
  - fibrose hépatique : organoïdes hépatiques humains (p. 19).

## Échecs et limites rapportés par les auteurs
- Littérature en accès libre seulement ; peu de résultats négatifs disponibles ; risque de propager des résultats faux ou non reproductibles (p. 24).
- Hallucinations et factualité imparfaite héritées des modèles ; validation des hypothèses « preliminary » (p. 24 et 25).
- Il faut des métriques d'évaluation plus objectives que les systèmes de classement actuels (p. 25).

## Vérifié par des tiers
- Les validations en laboratoire sont menées par des équipes coautrices ; le texte les dit « independent in vitro laboratory experiments » (p. 5). Ce ne sont pas des tiers au sens strict. AlphaEvolve (lu) le cite comme travail lié (p. 19 de son PDF). Aucune réplication externe trouvée.

## À emprunter
- Boucle extérieure : valider le juge interne contre une vérité de terrain, en contrôlant la difficulté des cas par une référence, avant de s'en servir pour sélectionner (annexe p. 45 et 46).
- Boucle intérieure : comparaisons deux à deux en débat pour réduire le biais d'ordre du juge (p. 34 et 38) ; donner au critique un accès à des sources externes pour ne pas surestimer la nouveauté (p. 38).
- Mesure du bruit : distinguer explicitement auto-évaluation et vérité de terrain dans chaque figure (p. 10 et 46).
