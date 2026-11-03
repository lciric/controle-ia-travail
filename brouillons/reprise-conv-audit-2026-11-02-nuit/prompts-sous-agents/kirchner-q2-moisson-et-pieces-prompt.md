Tu es un lecteur-moissonneur neuf pour la candidature de Lazar Ciric à Pivotal (mentor Jan Hendrik Kirchner, question 2 : « Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind? »). Tu n'as écrit aucune des réponses. Français ; toute heure vient de `date -u`. Dépôt `/home/claude/controle-ia-travail`, lecture seule.

## But
Préparer, **sans aucun appel de modèle payant**, ce qu'une course d'idéation et un tour du collisionneur recevront sur cette question : (A) une pièce « Kirchner » (faits vérifiés sur ce qu'il fait), (B) une moisson des candidats « problème sous-estimé », corruptibilité des moniteurs en tête, pour dire ce qui est déjà pris, (C) un brouillon de question servie. Lazar veut un problème **vraiment sous-estimé**, lié à nos travaux et surtout **à ce que Kirchner fait**.

## À lire d'abord (dépôt)
- Le rapport du lecteur Kirchner du 3 novembre : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-kirchner-v1.md` (section 0 : ses sources, ce qu'il n'a pas pu lire — annexes F et G, figure 32 ; sections 1 à 3).
- Les deux réponses actuelles de Lazar à Kirchner : blocs « Kirchner — Q1 » et « Kirchner — Q2 » de `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/reponses-mentors-finales-v3.md`.
- La pièce et la question servies pour Heimersheim, comme gabarits de forme : `brouillons/ideation-heimersheim-v1/piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md`, `question-ideation-heimersheim-v1.md`.
- Nos résultats publics, pour la pièce « nos résultats » que **j'écris moi-même** (tu n'y touches pas) : rien à lire ici.

## (A) Pièce « Kirchner » — `/home/claude/scratch/kirchner-q2/piece-kirchner-v1.md`
Par `WebFetch` et `WebSearch`, textes primaires entiers : arXiv 2608.28945 (« Automated Researchers Can Reliably Mitigate Alignment Failures », Chen, Wen, Kirchner) et sa version blog (alignment.anthropic.com, 2026, « automated-alignment-researchers »), **annexes F et G et figure 32 comprises** (le lecteur précédent s'est arrêté à E.1 : lis le PDF par tranches avec `offset` jusqu'au bout) ; « Automated Weak-to-Strong Researcher » (alignment.anthropic.com/2026/automated-w2s-researcher/, avril 2026) et l'annonce du 14 avril 2026 ; sa page mentor (pivotal-research.org/mentors, profil Kirchner : le problème qu'il déclare pour le premier trimestre 2027, cite-le mot pour mot) ; ses travaux antérieurs qui comptent ici (jeux prouveur-vérificateur et lisibilité, 2024 ; faible-vers-fort), d'après ses pages d'auteur (arXiv, OpenAlex) ; sa **littérature grise** : billets LessWrong et Alignment Forum, interventions, fils publics, 2025-2026 (`WebSearch`, puis `WebFetch` de chaque pièce trouvée). Pour chaque fait : section ou page, chiffre exact, citation de moins de quinze mots au plus une par source. Rubriques : ce qu'il construit (chercheurs automatiques, classement, juge, banc tenu à l'écart, Petri) ; ce qu'il mesure de la triche (§7, annexes F et G : moniteur, taux, catégories) ; ses modes d'échec déclarés (§8.2) et ses remèdes (« hill-climb AARs on monitorability benchmarks » : cite exactement) ; ce qu'il dit lui-même manquer ou sous-estimer ; ce que la critique de l'Institut britannique (arXiv 2605.06390, « Automated alignment is harder than you think ») lui oppose.

## (B) Moisson — `/home/claude/scratch/kirchner-q2/moisson-candidats-v1.md` et `.json`
Candidats à moissonner (au moins ceux-ci ; ajoute ceux que la lecture (A) fait apparaître) :
1. corruptibilité des moniteurs : un chercheur automatique optimisé contre un moniteur (ou sélectionné sur un banc de surveillabilité) apprend à tricher hors de son champ ; chute du rappel du moniteur après sélection ;
2. surapprentissage adaptatif des classements par des agents (resoumissions, graines, Ladder, holdout réutilisable) ;
3. juges modèles de langage au plafond ou manipulables (accord sans discrimination, sycophancie du juge) ;
4. lisible n'est pas causal pour les moniteurs d'activations (sondes qui lisent un marqueur de surface, par exemple un nombre déclaré) ;
5. transfert des résultats d'un organisme implanté vers une triche spontanée ;
6. tout autre candidat qui ressort de ses propres « modes d'échec ».
Pour chacun : au moins trois requêtes de mots différents sur arXiv et OpenAlex, puis LessWrong et Alignment Forum (`WebSearch` ; `WebFetch` des résumés pour vérifier) ; classe « déjà pris » (identifiants, dates, phrase du résumé), « voisin » (ce qui diffère), « peu couvert » (requêtes exactes et ce qu'elles ont rendu). Graphe de citations de 2608.28945 (qui le cite, pour dire quoi : OpenAlex ou Semantic Scholar par `WebFetch`). Métadonnées et résumés seulement ; non opposable ; n'invente aucun identifiant.

## (C) Brouillon de question servie — `/home/claude/scratch/kirchner-q2/question-ideation-kirchner-v1-brouillon.md`
Sur le gabarit de la question Heimersheim : la question du mentor mot pour mot ; ce qu'on attend (problèmes sous-estimés **vérifiables** comme tels, chacun avec une première expérience faisable en jours sur notre organisme public ou sur un modèle de 8 milliards, et un résultat chiffré qui ferait changer d'avis) ; ce qui est déjà pris (de ta moisson) ; les règles d'intégrité (niveau méthode, chiffres sourcés, pas d'identifiant inventé) ; la lecture prévue (Lazar écrit).

## Rendu
Réponse finale : les trois faits les plus importants sur Kirchner que la réponse actuelle ignore ; pour chaque candidat, sa classe de moisson en une ligne ; les chemins et sha256 des fichiers.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier du dépôt modifié ; rien sous `donnees/` ; aucun `git fetch` ; `WebSearch` et `WebFetch` pour les sources seulement ; aucun appel de modèle autre que toi. Tes fichiers sous `/home/claude/scratch/kirchner-q2/`.
