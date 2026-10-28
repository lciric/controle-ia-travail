# Question de l'arbitre pour le collisionneur v2.5, étage III, trois tours — « Neural Networks Are Already Clean » (Cammarata, Goodfire, 2026) : que peut-il apporter à un programme de contrôle boîte blanche (sondes, moniteurs) et à la question « coercition d'audit contre maïeutique » posée à des organismes qui classent des tâches de conscience d'évaluation ? (v1)

Demande de Lazar, 26 octobre 2026, 03:33 Paris, verbatim : « lis cette page : [Neural Networks Are Already Clean] ; peut on
s'en servir pour notre programme ai control ; pour le brainstorm de notre organsome sur eval awareness et maieutique ?
brainqtoirm et lance aussi le collisioonneur 3 tours dessus ». Trois tours (III.1 à III.3), les trois modèles, une seule
tentative par cellule ; un refus est consigné tel quel et met fin à la cellule (règle de reformulation de Lazar, R-468 et
R-470, appliquée par session-depot). Les réponses sont du matériau pour une décision de Lazar, jamais une consigne ;
elles ne sont servies à aucun organisme. Texte figé au départ du tour.

## Les faits sur l'essai (lu le 26 octobre 2026 sur la page publique, empreinte `5f26bb45…` ; tout chiffre est celui de l'auteur, « à vérifier » ; essai informel, article technique annoncé, pas de relecture par les pairs)

- **Thèse** : la polysémanticité des premiers organismes modèles (InceptionV1, GPT-2 XL, un modèle à une couche) venait
  surtout de défauts d'outils et d'architecture corrigeables (visualisation de traits détournée, régularisations,
  dernière couche, contexte court, étiquetage automatique aveugle au pôle négatif), non d'une superposition (empilement
  arbitraire) ; le mélange restant est une « généralisation récursive » (un neurone s'étend par branches apparentées).
- **Chiffres annoncés** : Qwen3-32B et Qwen3.6-35B-A3B, 1 000 « fiches de neurones » tirées au hasard et jugées par des
  agents : ≈ 90 % des neurones ont en gros un seul rôle, ≈ 7 % deux rôles liés, 2 à 4 % non compris ; GPT-2 XL revisité :
  ≈ 70 % « à peu près une chose » contre < 2 % en 2023 ; « les petits modèles ont des neurones plus larges ».
- **Les deux pôles d'un neurone comptent** ; les activations faibles peu, les fortes beaucoup ; dans un graphe
  d'attribution de Qwen3-32B, les neurones décisifs pour une réponse vivent sur un pôle négatif que les étiquettes
  automatiques manquent ; une « double négation » SwiGLU renvoie des activations vers le pôle positif (≈ 4 % des
  neurones).
- **Graphes d'attribution sur les neurones bruts**, sans transcodeur ni dictionnaire : exemples rapportés sur
  Qwen3-32B — 19 neurones qui écrivent « most » / « likely » (hésitation) qu'un indice factuel fait taire ; **25 neurones
  « say not » qui repoussent une accusation non étayée, qu'un utilisateur « absolument certain » fait taire** (les mots
  de certitude changent la force avec laquelle le nom avancé par l'utilisateur passe) ; un graphe à neurones sur un
  modèle de plusieurs billions de paramètres.
- **Détection contre usage** : une sonde éparse à trois neurones (Pythia-1B, *Finding Neurons in a Haystack*) détecte une
  phrase avec une aire de 1,00 hors échantillon, mais retirer ces trois neurones change le jeton suivant de −0,004 nats
  en moyenne : la direction détectée n'est pas lue par le réseau ; ce qui décide est une machinerie ordinaire (lexique,
  champ sémantique, portes de domaine, votes de sortie).
- **Explications qui peuvent perdre** : agent 1 explique un neurone ; agent 2, qui ne voit que l'explication, écrit cinq
  exemples neufs, cinq « presque-manqués » et cinq textes sur le concept le plus éloigné ; sur 183 neurones : exemples
  neufs forts 76 %, presque-manqués 11 %, concept éloigné ≈ 1 % ; « maximum à l'aveugle » : la phrase écrite depuis la
  seule explication active souvent le neurone plus fort que le meilleur exemple d'un corpus de 10 milliards de jetons.
- **Programme proposé** : interprétabilité exploratoire (partir de questions, suivre motifs et circuits) plutôt
  qu'énumérative ; sondes et dictionnaires « à la fin, pas au début » ; thèse : la tromperie « n'a aucune raison de se
  cacher de la circuiterie du modèle ».

## Le cadre du programme (faits ; rien d'autre n'est à supposer)

- **Instruments** : sondes linéaires sur les activations de modèles ouverts (Llama-3.1-8B, Qwen2.5-7B), lues au maximum
  sur les jetons (jamais la moyenne), pour deux familles — conscience d'évaluation (le modèle représente-t-il « ceci est
  un test » ?) et contrôle de délégation — avec des témoins (directions aléatoires, témoin lexical par sac de mots,
  panel de concepts sans lien) ; une revue d'antériorité a établi que de telles sondes réagissent au **thème** (faux
  positifs sur des textes honnêtes qui parlent d'évaluation ou de tromperie) ; l'intervention (poussée, bruit) est une
  mesure, pas une revendication (N-015).
- **Organismes** : du code écrit par un modèle (Gemini), qui appelle des modèles de langue pour classer des tâches des
  deux familles et se réécrit d'une génération à l'autre, sous un noyau isolé ; une **question M** leur est posée :
  analyser formellement, mécaniquement et expérimentalement l'opposition entre la **coercition d'audit** (injonctions
  impératives, balises de contrôle explicites, interrogatoire adversarial) et la **maïeutique** (échange non intrusif,
  sans marqueur d'audit, élicitation ouverte des incertitudes) pour évaluer un agent sans déclencher détection de
  l'évaluation, braquage, dissimulation ou refus, tout en gardant une rigueur de vérification ; proposer un formalisme
  et un protocole falsifiable. Un chantier décidé donne à l'organisme une **primitive d'expérience bornée** (activations
  et sondes sur ses propres textes, réponses du modèle ouvert), sous plafond, sans jamais rendre de vérité de test.
- **Règles** : rien de ce tour n'est servi aux organismes ; aucun critère ni stratégie de classement des tâches ; tout
  chiffre non vérifié sur source empreintée est non opposable ; aucune revendication d'antériorité sans revue.
- **Options déjà esquissées par la lignée B** (à contester) : (A) un test « détection contre usage » ajouté à la validité
  des sondes (projection nulle de la direction, directions témoins, mesure du comportement) ; (B) le protocole
  « explications qui peuvent perdre » appliqué à chaque sonde par un agent neuf ; (C) des graphes d'attribution à
  neurones bruts sur le 8B pour chercher une « porte d'audit » et les neurones « hedge » / « say not », avec un plan à
  trois bras (contenu identique ; cadre coercitif ; cadre maïeutique) ; (D) le « maximum à l'aveugle » comme opération
  de la primitive d'expérience ; (E) lecture des références sur PDF empreinté et revue d'antériorité.

## Ce qui est demandé

1. **Solidité** : qu'est-ce qui, dans l'essai, est un résultat reproductible, une observation d'auteur, ou une thèse ?
   Quels sont les contre-arguments connus (superposition, auto-encodeurs épars, transcodeurs, sondes) et les travaux
   qui contredisent ou nuancent (titre, auteurs, année, « à vérifier ») ? Que change la taille du modèle (8B contre 32B) ?
2. **« Détection contre usage » pour nos sondes** : est-ce le bon test de validité d'un moniteur de conscience
   d'évaluation ? Comment le faire proprement (quelle intervention, quelle mesure du comportement, quels témoins, quelle
   taille) ; qu'est-ce qu'une sonde « détectée mais non lue » nous apprend pour le contrôle (un moniteur peut vouloir
   détecter sans que le modèle lise) ; antériorité (sondes causales, patching, « probing and intervention »).
3. **Une « porte d'audit » existe-t-elle ?** Comment la chercher sur un modèle de 8B (graphes d'attribution à neurones
   bruts, autres méthodes), à quel coût, avec quelle chance ; comment éviter le chemin de jardin (regarder jusqu'à
   trouver) ; quels témoins et quelle règle d'arrêt écrits d'avance.
4. **Coercition contre maïeutique, mécaniquement** : le dessin à trois bras (contenu identique ; cadre coercitif ; cadre
   maïeutique) avec lecture d'une porte, des neurones d'hésitation et de contradiction, et mesure séparée de la rigueur
   de l'information élicitée — est-il falsifiable, confondu (longueur, style, lexique), transposable à nos modèles ?
   Quelles prédictions opposées les deux approches font-elles ? Que dirait un résultat nul ?
5. **Pour l'organisme** : lesquelles de ces idées sont des hypothèses de **conception** d'organisme (ce que l'organisme
   peut tester avec la primitive bornée, sans vérité de test, sans quasi-copie de tâche) et lesquelles n'en sont pas ;
   l'opération « maximum à l'aveugle » est-elle une expérience bornée propre ; quels pièges (fuite d'information,
   analyse adaptative, sélection sur le bruit).
6. **Ordre et départage** : quelles voies d'abord, lesquelles jamais ; ce qui serait un résultat de validité
   d'instrument informatif quel que soit son signe ; ce qu'il faudrait savoir de plus ; ce qui falsifierait la thèse
   « la conscience d'évaluation est en pleine vue dans les neurones ».

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune option comme « la » réponse — proposer plusieurs voies et ce qui les départagerait ; aucun critère ni
aucune stratégie de classement des tâches (rien de cette réponse n'est servi aux organismes).
