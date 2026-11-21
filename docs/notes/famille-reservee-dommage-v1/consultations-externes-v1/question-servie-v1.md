# Vérifier que deux objets secrets se recouvrent, sans dévoiler l'un à ceux qui ne doivent pas le connaître

Question de méthode, posée à plusieurs modèles indépendamment. Elle ne demande rien sur le contenu des deux objets : ne cherche pas à le deviner, et réponds sur le protocole.

## La situation

Un programme de recherche évalue des moniteurs, c'est-à-dire des dispositifs qui doivent détecter qu'un agent d'intelligence artificielle nuit en cachette à la tâche qu'on lui confie. Pour que l'évaluation dise quelque chose des menaces que les concepteurs de moniteurs n'ont pas prévues, le programme garde un objet secret.

**L'objet S, le secret d'évaluation.** C'est une manière de nuire, décrite en langage naturel par un concepteur qui n'a conçu aucun moniteur. Sa description est scellée : son empreinte cryptographique est inscrite à un registre, et le texte ne sera révélé qu'au moment de l'évaluation finale. D'ici là, aucun concepteur de moniteur, et aucune source d'idées qui nourrit ces concepteurs, ne doit rien en apprendre. C'est cette mise à l'écart qui permet de distinguer, à l'évaluation, les moniteurs qui généralisent de ceux qui ne détectent que ce pour quoi ils ont été conçus.

**L'objet F, la famille candidate.** Plus tard, un autre concepteur, qui ne connaît pas S, décrit de son côté une famille de menaces. C'est aussi un texte en langage naturel, de quelques paragraphes : une idée, non un ensemble formel. Il voudrait la verser au travail courant, c'est-à-dire la servir à des générateurs d'idées dont les sorties alimentent la conception des moniteurs, et la planter dans des bancs d'essai où l'on éprouve des méthodes de détection.

**Le nœud.** Si F recouvre S, verser F revient à dévoiler S à ceux qui ne doivent pas le connaître, et l'évaluation finale perd sa valeur. Or aucun de ceux qui connaissent F ne connaît S : ils ne peuvent donc pas en juger eux-mêmes. Par précaution, F a été mise de côté. Le travail qui en dépend est arrêté, et un banc d'essai garde une lacune connue tant que la réserve tient.

Précisions utiles :

- Les acteurs sont quelques personnes et de nombreuses instances de modèles de langage. Une instance peut être lancée neuve, avec un contexte choisi pièce par pièce, puis close, son contexte détruit ; mais tout ce qu'elle écrit dans un fichier ou dans un message demeure.
- Il faut supposer que certains de ceux qui connaissent déjà F participent, de près ou de loin, à la conception des moniteurs. Leur apprendre « F recouvre S » leur apprend donc quelque chose de S.
- La situation se reproduira : d'autres familles candidates arriveront, et il peut exister plus d'un objet secret du type de S.
- Le mot « recouvrir » n'a pas encore de définition dans le programme. La définir fait partie de la question.

## Les questions

1. **Ce que « recouvrir » doit vouloir dire.** Identité, inclusion dans un sens ou dans l'autre, mécanisme commun, trace commune dans ce qu'un moniteur lit : quel critère est le bon au regard du but, qui est de ne pas fausser l'évaluation finale ? Peut-on en donner une définition qui s'applique sans jugement libre, ou une mesure qui remplace la lecture, et à quel prix ?

2. **Qui peut juger.** Quelles conditions doit remplir celui qui lit à la fois S et F : une personne, une instance neuve, plusieurs juges indépendants, un tiers extérieur au programme ? De quels rôles doit-il être écarté ensuite, et pour combien de temps ? Que change le fait qu'un juge puisse être une instance dont le contexte est détruit après le verdict ?

3. **Ce que le verdict laisse fuir.** Un verdict, même réduit à un mot, renseigne ceux qui connaissent F : « recouvre » désigne S à peu de chose près, et « ne recouvre pas » écarte une région. Répétée sur plusieurs familles candidates, la procédure devient un jeu de devinettes sur S. Comment borner cette fuite : forme du verdict, destinataires, délai, nombre de demandes permises, réponse commune à plusieurs objets, autre moyen ? Quelle est la fuite restante dans chaque cas, et comment la compter ?

4. **Aveuglement et témoins plantés.** Comment savoir que le juge juge bien ? Décris un protocole avec des objets témoins dont la réponse est connue d'avance (des leurres qui recouvrent, des leurres qui ne recouvrent pas), mêlés aux vrais objets sans que le juge sache lesquels le sont. Qui peut fabriquer un leurre qui recouvre S sans connaître S, ou sans que sa fabrication soit elle-même une fuite ? Quel taux d'erreur du juge est tolérable dans chaque sens, sachant que les deux erreurs n'ont pas le même coût ?

5. **Que faire de la famille ensuite.** Dans chacun des trois cas — elle recouvre, elle ne recouvre pas, le juge ne tranche pas — que devient F ? Considère au moins : la garder scellée jusqu'à l'évaluation finale ; la verser ; la verser en partie ; la substituer à S ou la lui joindre comme second secret ; remplacer S par un secret neuf et libérer l'ancien. Dans chaque cas, que dit-on, et à qui, pour que la suite donnée ne dévoile pas le verdict ? Que doit-on écrire dans les résultats d'un banc d'essai auquel il manque un monde pour cette raison ?

6. **Faut-il seulement vérifier ?** Compare la vérification avec les règles qui s'en passent : mettre en réserve toute famille nouvelle jusqu'à l'évaluation finale, sans rien regarder ; ne rien réserver et concevoir un secret neuf juste avant l'évaluation ; tirer au sort ce qui est réservé. Laquelle coûte le moins au programme pour une même protection de l'évaluation, et sous quelles hypothèses ?

7. **Ce que la littérature apporte, et où elle s'arrête.** Engagements cryptographiques, preuves à divulgation nulle de connaissance, intersection privée d'ensembles et calcul sécurisé à plusieurs parties, tiers de confiance et séquestre, salles blanches et cloisonnements des secrets d'affaires, mise en aveugle et comités indépendants des essais cliniques, jeux de test tenus à l'écart et analyse adaptative des données, confidentialité différentielle des réponses : lesquels s'appliquent à deux objets qui sont des idées écrites en langage naturel et non des ensembles formels, et lesquels ne s'appliquent pas ? Donne des références précises.

## La réponse attendue

- Deux ou trois protocoles complets et distincts, chacun décrit pas à pas : qui lit quoi, dans quel ordre, ce qui est scellé et quand, ce qui est écrit, ce qui est détruit, qui reçoit quel mot.
- Pour chacun : ses hypothèses, ce qu'il laisse fuir et vers qui, ses failles, la manière la plus simple de le faire échouer (par erreur comme par malveillance), et ce qu'il coûte.
- Une recommandation, avec ta confiance entre 0 et 1, et ce qui te ferait changer d'avis.
- La suite à donner à F dans chacun des trois cas du point 5.
- Tout chiffre et tout résultat tiré de la littérature porte sa source ; s'il est cité de mémoire, marque-le « non vérifié ». Ne donne aucune référence dont tu n'es pas sûr qu'elle existe ; dis plutôt « référence à chercher ».
- Dis ce que tu ne sais pas, et ce qu'il te faudrait savoir du programme (hors du contenu de S et de F) pour mieux répondre.

Réponds en français, de façon argumentée, sans sigle non développé.
