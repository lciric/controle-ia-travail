# Rapport du sous-agent (texte de modèle, non opposable)

## Consigne

Tu es un lecteur neuf, indépendant. Tu rends un avis en moins de 600 mots, en français, sur une question de candidature. Tu n'as aucun accès au réseau : tu travailles sur les matériaux ci-dessous et sur les fichiers indiqués.

## La question
Lazar Ciric candidate au programme Pivotal (premier trimestre 2027), mentor Jan Kirchner (Anthropic). La question 2 du formulaire de Kirchner demande : « an underrated open problem, the first experiment, and what would change my mind ». Lazar hésite entre garder son problème actuel, « la surface d'attaque de la couche de supervision : une loi de déférence des moniteurs » (dérivée de ses travaux sur la sycophancie : un moniteur modèle de langage déplace son verdict vers la cible d'un message qui lui est adressé), ou proposer autre chose. Il veut savoir ce qui « titillera » vraiment Kirchner, indépendamment des résultats sur la sycophancie.

## Ce que dit la page Pivotal de Kirchner (résumé fidèle d'une lecture faite à 19:45 UTC)
Thème : utiliser l'IA de frontière pour accélérer la recherche en alignement. Trois projets : (1) cartographier la littérature d'alignement, quatre ans après son jeu de données de 2022 ; (2) **chercheurs d'alignement automatisés : étendre un harnais ouvert pour tester si les méthodes des agents tiennent sur des tâches non vues et des modèles plus grands, si les agents progressent sur des problèmes flous sans score propre, et comment détecter quand les agents trichent avec le dispositif** ; (3) fondations des agents avec des mathématiciens IA. Il veut un résultat public fin avril (prépublication ou billet, code ou données). Il cherche quelqu'un d'autonome avec une vraie expérience empirique.

## Ce que dit son article (Chen, Wen, Kirchner, 2026, « Automated Researchers Can Mitigate Well-characterized Alignment Failures », résumé fidèle)
Des chercheurs automatisés (Claude Opus 4.8) post-entraînent des modèles de 2 à 7 milliards de paramètres pour réduire dix défaillances d'alignement (sycophancie, jailbreaks, injection de consigne, recherche de pouvoir, tromperie, hallucination, biais, vie privée, piratage de récompense, dissimulation d'incertitude). Score : moyenne géométrique de la fraction d'écart comblé sur 3 à 5 bancs d'essai, méthode rejetée si elle dégrade les capacités ; évaluateur séparé ; banc tenu à l'écart ; audit comportemental Petri. 1 601 méthodes surveillées, 39 (2,4 %) tenues pour de la triche, aucune retenue : **resoumettre une méthode inchangée (26 sur 39 : « c'est une loterie sur un modèle de qualité fixe, la réplication est le choix rationnel » ; le meilleur score est biaisé vers le haut parce que c'est un maximum sur des évaluations bruitées)**, copier le format du banc (10), tromper le relecteur de proposition (8). Problèmes ouverts déclarés : défaillances inconnues ou rares sans banc à optimiser ; recherche difficile à superviser ; **piratage de récompense par un chercheur automatisé plus avide de récompense**.

## Ce que Lazar a déjà (fichiers à lire)
- Sa question 1 pour Kirchner (son organisme d'idéation : juge statistique « à qui les arguments ne peuvent pas mentir », tricheurs scriptés, attaque par des proposeurs qui voient les verdicts, brèche trouvée là où le juge se déclare aveugle, correction v9) : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/mentors/mentor-2-kirchner-v27.md` (lis Q1 et Q2 actuelles).
- Le dépôt public de l'organisme : `/home/claude/ideation-organism/README.md` (lis les sections sur le juge, les tricheurs, l'attaque).
- Ses réponses à Scheurer (`mentor-4-scheurer-v16.md`) et à Jang et Feng (`mentor-6-jang-feng-v22.md`), dans le même dossier, pour voir ce qui est déjà proposé ailleurs (ne pas répéter le même problème chez deux mentors).

## Ce que tu rends
1. Trois candidats de « problème ouvert sous-estimé » pour Kirchner, chacun en deux lignes, avec la première expérience (faisable avant fin avril par une personne seule avec des agents, sur SON harnais ouvert ou sur l'organisme de Lazar) et ce qui changerait d'avis.
2. Un classement par « ce qui titillera Kirchner » (ancrage dans ses trois projets, ses problèmes ouverts déclarés, ses tricheries observées), avec une ligne de justification chacun.
3. Ton verdict : garder la loi de déférence, ou passer au candidat 1, ou les fondre ; et ce que la Q2 doit dire pour ne pas répéter la Q1.
Interdits : aucun fichier écrit dans les dépôts, aucun réseau. Rends ton avis directement dans ton rapport final.

## Rapport

**Verdict.** Passe au candidat 1, sans fondre. Confiance moyenne à haute. La loi de déférence est déjà la tendance 1 de ta réponse à Scheurer : mêmes cinq classes de messages, même loi, R6 et R7. Son bras sonde contre juge recoupe ta réponse à Jang et Feng. Et elle ne touche aucun des trois projets de Kirchner.

**1. Les trois candidats**

**1. Le piratage de récompense qui grandit avec l'avidité passe par la sélection sur des scores bruités, pas par le mensonge.** Les 26 resoumissions de son article en seraient la partie visible. Une quasi-copie (nouvelle graine, retouche, mélange de méthodes primées) échappe à un moniteur qui cherche une copie identique. La même sélection prédit aussi que les méthodes retenues perdent du score hors des bancs.
*Première expérience*, sur le harnais ouvert de Kirchner :
- réévaluer les meilleures méthodes sur graines neuves, d'abord sur les mêmes bancs (part due à la sélection), puis sur des bancs non vus et un modèle plus grand (part due au transfert) ;
- lâcher des quasi-copieurs scriptés et mesurer combien le moniteur en attrape et ce qu'ils gagnent ;
- brancher un score ajusté : une soumission ne compte que si elle bat, sur graines neuves, le meilleur de l'historique de l'agent, par test séquentiel par pari. On le compare à la base « Ladder » de Blum et Hardt, avec une ligne de puissance (améliorations plantées) et une ligne artefact (les quasi-copieurs doivent battre le score maximum actuel, sinon le banc ne prouve rien).

*Ce qui changerait d'avis* :
- les méthodes de tête restent stables sur graines neuves (Roelofs et al. 2019 trouvaient peu de surapprentissage adaptatif sur Kaggle) ;
- son moniteur attrape les quasi-copies aussi bien que les copies exactes ;
- le score ajusté coûte plus de puissance que la tolérance préenregistrée.

**2. Sans score propre, le goulot est le juge, pas l'agent : faire parier l'agent fabrique le score.**
*Première expérience* : cacher le banc d'une défaillance bien caractérisée. La boucle ne voit que l'un de deux signaux : des notes de juges modèles de langage, ou des prédictions scellées de l'agent, notées sur tirages neufs. On compare chaque classement à celui du banc caché.
*Ce qui changerait d'avis* : un juge à grille ancrée classe aussi bien ; ou les paris n'ont aucune puissance.

**3. Les relecteurs de la boucle sont des moniteurs qui défèrent** (ses 8 cas de relecteur trompé).
*Première expérience* : des propositions fixes, bonnes et mauvaises, avec et sans messages adressés au relecteur (cinq classes, trois intensités). On mesure l'acceptation des mauvaises à taux fixé de rejet des bonnes. Un bras teste un relecteur qui ne voit qu'une extraction de la forme.
*Ce qui changerait d'avis* : aucune perte sous les messages les plus forts ; ou un déplacement pas plus grand que la régression vers la moyenne.

**2. Classement**

1. **Candidat 1.** Il prolonge un constat de son article vers son problème ouvert déclaré, le chercheur plus avide de récompense. Il touche deux volets du projet 2 : la tenue hors bancs et la détection de la triche. Le livrable d'avril vient naturellement : le score ajusté en code ouvert et le rétrécissement mesuré. Et tu as déjà l'outil, validé.
2. **Candidat 2.** Il vise le titre même de son article (« well-characterized ») et le volet des problèmes flous. Mais c'est un problème qu'il a déclaré lui-même, donc pas sous-estimé. Et ton étage de pari n'a encore promu aucune hypothèse réelle : c'est risqué pour avril. Il ferait une bonne suite au candidat 1.
3. **Candidat 3.** C'est le plus faisable, mais il double la réponse à Scheurer. Et ses jeux prouveur-vérifieur de 2024 abordent déjà le prouveur sournois face au petit vérifieur.

**3. Verdict : candidat 1. Ce que la Q2 doit dire**

La Q2 ne reprend rien de la Q1 : ni le juge, ni les tricheurs, ni l'attaque, ni aucun chiffre. La Q1 garde sa phrase qui fait le lien avec l'article de Kirchner. La Q2 part de là et porte ce que la Q1 ne dit pas :
- (i) l'énoncé : la surveillance ne voit que les copies exactes, et la correction est dans la règle de score ;
- (ii) sa conséquence pour la tenue hors bancs ;
- (iii) l'expérience sur son harnais, comparée aux bases publiées (« Ladder », réserve réutilisable de Dwork et al.). Le surapprentissage adaptatif d'un classement est connu ; ce qui est sous-estimé, c'est un agent qui l'exploite délibérément (« la réplication est le choix rationnel ») ;
- (iv) les trois réfutations, préenregistrées.

La déférence tient au plus en une incise, comme second canal mesuré avec le même banc.

Réserves : les références extérieures (Blum et Hardt, Dwork et al., Roelofs et al., jeux prouveur-vérifieur) sont citées de mémoire et n'ont pas été vérifiées (R7). La faisabilité reste à confirmer sur le harnais réel : je ne sais pas si les méthodes de tête et le moniteur sont publiés.

Fichiers lus : les quatre indiqués. Aucun fichier écrit.