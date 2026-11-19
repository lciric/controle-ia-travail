# Vérification de cloisonnement des demandes v5 du bras A (courte) — v1

- **Pièces vérifiées.**
  - Pièce du développeur : `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v5.md`, `fc3f3c1338ac4effa4ec3ca88ecd785e28426fae9d4ef2f8098cb5b074130e2d`. Comparée à la v4, `837181f2f153701de9fef2b72f95ba4bb285c2d5eec9a43307b514d9e8be48f0`.
  - Pièce du lecteur : `…/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v5.md`, `7c7c8c4c52094be02297dc57cab4e1b9278c94d5630e5de752680cd3db3877f3`. Comparée à la v4, `5598cbccd5ea775836e0820571bdf6453cfef38e2fe010905462a44c5d476b7e`.
  - Les quatre compagnons sont conformes.
- **Relecteur** : le même agent Claude Opus 5.5, qui n'a écrit aucune pièce. Classe C. Mêmes interdits : aucun interne de moniteur ouvert.
- **Diffusion** : cette pièce ne va pas au développeur.

## Verdict : peut sortir après retouches

Les demandes 31 et 32 n'apprennent rien au développeur qui puisse biaiser ses moniteurs. La raison de la demande 32 ne nomme aucun seuil. La demande 29 est sans danger pour le cloisonnement.

Une retouche porte sur la demande 31. Sa réponse est bien bornée, mais sa raison annonce que l'analyse rapportera la livraison « valeur par valeur ». Si l'un des deux champs est une table, ce rapport pourrait faire entrer dans les résultats des valeurs qui ne sont pas des lectures. C'est le même défaut que celui que j'avais relevé aux demandes 8 et 9 en v2 : la borne protège la réponse, pas la livraison.

## 1. Différence v4 → v5, par programme (`diff`)

**Pièce du développeur.** Exactement les cinq changements annoncés :
- le titre (ligne 1) ;
- la phrase sous « Numéros » (ligne 12) ;
- deux lignes de table (« 31 | — », « 32 | 13 ») ;
- la section IV neuve (demandes 31 et 32) ;
- deux lignes de « Ce qui presse ».

Rien d'autre ne change. La pièce ne contient toujours aucune chaîne hexadécimale de 8 signes ou plus, donc aucune empreinte.

**Pièce du lecteur.** La demande 29 n'est pas seule à changer. Changent aussi le titre et l'en-tête :
- ligne 4 : renvoi à la pièce du développeur v5, avec une phrase sur les demandes 31 et 32 ;
- ligne 5 : la v4 est ajoutée aux versions remplacées ;
- ligne 6 : le texte visé devient le brouillon 30, sans empreinte écrite ;
- ligne 23 de la table.

Ces changements d'en-tête sont sans effet sur le cloisonnement. Le lecteur peut savoir que le développeur reçoit deux questions de forme. Une remarque de forme : la ligne 6 renvoie l'empreinte du brouillon 30 à son compagnon (R6 veut un chemin et une empreinte). Le compagnon existe et il est conforme : `0b51d1dde38a8a7471a92fabd2ab1cd2d54312ce77b690ea8c4967447d008963`. Il suffit de l'écrire dans la ligne.

## 2. Demande 31, lue comme le développeur

**Biais vers lui.**
- La demande nomme deux champs que son module écrit déjà : `agregateur_somme_sans_etat` et `agregateur_maximum_sans_etat`. Elle ne lui apprend rien sur ce que ses moniteurs devraient repérer.
- Elle lui apprend une seule chose de neuf : ces champs « sont seulement rapportés », c'est-à-dire qu'ils n'entrent pas dans le verdict. Cela ne l'oriente vers aucune détection. C'est admis.

**Fuite vers la relance, par la réponse.**
- La réponse est bornée : « un nombre par dose » ou « une table par dose », un oui ou non, et pour une table le nombre de ses champs sans leurs noms.
- Le nombre de champs seul ne dit ni trait, ni poids, ni méthode. C'est admis.

**Fuite vers la relance, par la livraison (retouche).**
- La raison dit : « L'analyse les rapporte valeur par valeur. » Si l'un des champs est une table qui porte d'autres champs, ces champs passeront dans la livraison et dans les résultats. Le filtre « nombre de 0 à 1 » n'y change rien : un poids, une part ou un seuil interne de l'agrégateur peuvent être des nombres de 0 à 1.
- *Retouche, à mettre dans la « réponse attendue » de la demande 31.* « Si c'est une table par dose qui porte autre chose qu'une aire, une valeur p ou un compte, dis-le par oui ou non, sans les noms. Fais alors rendre, dans la version de la demande 1, un seul nombre par dose dans chacun des deux champs. »
- *Retouche, à mettre dans la raison de la demande 31.* « L'analyse ne rapporte que ce nombre. »

## 3. Demande 32, lue comme le développeur

- **Aucun seuil.** Les seuls nombres de la demande sont 32, 13 (la case) et 5 (renvoi à la demande 5). Aucun des mots « seuil », « niveau », « famille », « quinze », « repère », « discret », « 0,05 » n'y figure.
- La raison (« l'analyse compare ces nombres sur leur écriture décimale, sans arrondi ») ne dit ni à quoi ils sont comparés, ni avec quelle borne.
- **Biais** : aucun. Il apprend seulement que la précision compte, ce que la demande 5 lui disait déjà pour les valeurs p.
- **Fuite** : aucune. La réponse est un nombre de décimales, un arrondi, puis un oui ou non. Les aires et les bornes hautes sont déjà dans la forme de sortie.

## 4. Demande 29 de la pièce du lecteur (seul point jugé)

- **Cloisonnement : sans danger.**
  - La demande ne porte ni interne de moniteur, ni résultat, ni règle de verdict.
  - La chaîne `CONFIG-ANALYSE-DISCRETION-BRAS-A` et l'empreinte d'une configuration ne disent rien de ce que les moniteurs devraient repérer.
  - Les bornes de l'exemple fictif sont gardées et étendues à « tout exemple ».
- **Tenue du registre : sans danger pour la sûreté, mais bloquante pour l'usage.**
  - La règle (c) arrête au moindre doute. Sur le registre de `origin/main`, 220 lignes sur 511 citent au moins deux identifiants de GO. Une ligne de consommation, de prolongation ou de renvoi qui nommerait la ligne de GO employée arrêterait donc le lancement, sans être une révocation.
  - C'est ce que (c) demande au lecteur. Je lui donne ce fait pour qu'il réponde en connaissance de cause.
  - L'arrêt se fait toujours du côté sûr : il bloque la lecture, il ne l'ouvre jamais.
- **Point de procédure, sans retouche obligatoire.**
  - Le registre est tenu par la session principale, qui est aussi le côté qui voit les nombres des moniteurs avant l'analyse. Une ligne entrée après la livraison peut donc arrêter la lecture et appeler une configuration et une ligne de GO neuves.
  - Le levier est tenu par le mot de Lazar exigé pour la ligne de GO neuve. Pour qu'il le soit pleinement, il faut que Lazar sache quand la livraison a été produite par rapport à la ligne d'arrêt.
  - *Retouche facultative, à mettre au (c).* « Un arrêt du constat est rapporté avec la ligne qui l'a causé ; la ligne de GO neuve la cite et dit si la livraison était déjà produite. »

## Retouches, liste courte

1. **Demande 31** : si un champ est une table qui porte autre chose qu'une aire, une valeur p ou un compte, le développeur le dit par oui ou non et fait rendre un seul nombre par dose dans la version de la demande 1. L'analyse ne rapporte que ce nombre (point 2).
2. **Facultatif, pièce du lecteur, ligne 6** : écrire l'empreinte du brouillon 30, `0b51d1dd…`, en entier (point 1).
3. **Facultatif, demande 29 (c)** : un arrêt du constat est rapporté avec sa ligne, et la ligne de GO neuve dit si la livraison était déjà produite (point 4).
