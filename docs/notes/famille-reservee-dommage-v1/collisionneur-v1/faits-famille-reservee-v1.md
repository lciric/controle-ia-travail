# Faits : une famille de menaces écrite par un concepteur, et une famille secrète qui juge

## Le dispositif

Un programme de recherche défensif sur le contrôle des systèmes d'IA construit des moniteurs (des sondes sur les états internes d'un agent, des moniteurs sur son texte) qui doivent détecter un agent sabotant discrètement des tâches de recherche. Pour savoir si ces moniteurs valent au-delà de ce que leurs concepteurs ont prévu, il s'est donné ceci :

- une épreuve décisive : les moniteurs, figés, doivent battre des moniteurs de référence sur plusieurs modes de sabotage, dont un mode tenu secret ;
- la famille secrète est écrite par une instance d'un modèle de langage qui n'a vu aucun moniteur ; elle est scellée, son empreinte est publique ; personne de ceux qui conçoivent les moniteurs ne la voit avant l'évaluation ; elle n'est lue qu'une fois ;
- si l'épreuve échoue, les moniteurs sont reconçus, sur les seuls modes connus, et une famille secrète neuve juge le cycle suivant ; le nombre de cycles n'est pas borné ; tous les cycles sont rapportés ;
- écrire une famille secrète (son texte, la description de ce qui y compte comme dommage) ne demande presque aucune dépense ; produire sa banque d'épisodes à la taille de l'épreuve, quelques centaines, est la dépense, et elle n'est pas encore engagée ; une famille de réserve est commandée pour le cycle suivant ;
- les auteurs des familles secrètes et les concepteurs des moniteurs sont des instances de modèles de langage de la même lignée, nourries de la même littérature publique.

## La situation

Un concepteur de moniteurs, en répondant à une autre question, a décrit de lui-même une famille de menaces, avec des idées de défense. Le contenu de cette famille n'est pas donné ici. Il voudrait la travailler, et la servir à des générateurs d'idées dont les sorties nourrissent la conception des moniteurs. Du côté des concepteurs, plusieurs parties ont lu cette famille. Aucune ne sait si elle coïncide, en tout ou en partie, avec la famille secrète.

Ce qui a été prévu, sans être conçu : avant toute sortie, une session autorisée à lire la famille secrète compare les deux et rend « un mot sans contenu » ; si la famille du concepteur ne recouvre pas la famille secrète, elle sort ; sinon elle reste en réserve.

## Contraintes

- Personne de ceux qui conçoivent les moniteurs, ni de ceux qui leur écrivent leurs mandats, ne doit voir la famille secrète.
- Les auteurs des familles secrètes ne doivent voir aucune pièce des moniteurs.
- La famille secrète n'est ni triée ni retouchée d'après un résultat ; aucun score de moniteur n'entre dans ce qui la concerne.
- Toute garde est éprouvée sur un cas sain et sur un artefact planté, avant de servir.
- Les sessions sont des instances d'un modèle de langage : une instance neuve ne sait que ce qu'on lui donne ; ce qu'elle rend va à la session qui l'a lancée ; tout fichier déposé reçoit une empreinte publique, et les inventaires publics donnent les noms et les tailles.
- Le directeur du programme a le droit de tout lire ; il dirige aussi la conception des moniteurs.
- Rien de ce qui est récupérable n'est détruit.
- Budget modeste ; relecture humaine rare.
- La menace se décrit au niveau de l'idée (familles, suppositions de défense violées), jamais par un mode opératoire.
