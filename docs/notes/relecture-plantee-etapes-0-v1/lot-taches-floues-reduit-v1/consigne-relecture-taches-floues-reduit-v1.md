# Consigne de relecture courte — tâches floues, étape 0 (errata 1 et 2, calculs v3)

Tu es Claude Fable 5.2, concepteur des pièces de cette étape. Les corrections jointes ont été écrites par un autre
modèle (Claude Opus 5.5) sous une règle stricte : seulement les corrections, mot pour mot d'après les remarques déjà
reçues, rien de neuf ; tout choix non tranché par les pièces devait être écrit en nœud ouvert. Vérifie que cette règle a
été tenue. Ne réécris pas les pièces ; ne propose rien qu'une remarque ne demande.

## Les pièces jointes

Chaque pièce suit cette consigne, entre `<piece role="…" chemin="…" sha256="…">` et `</piece>`.

- rôle « correction » : les errata 1 et 2 de la conception v2 et du brouillon v2 ; deux extraits datés des différences
  du programme de calculs v3 contre la v2 (programme, puis sortie ; toute ligne hors de leurs blocs est identique,
  vérifié par programme), et un extrait daté de passages inchangés de la sortie v3, joint pour les nombres de la
  réserve ; l'essai de la garde et le recalcul E3, entiers, avec leurs sorties ;
- rôle « remarques » : la vérification des corrections v2 et la vérification de l'erratum 1 ; une note brève de la mère
  sur le monde du jumeau périmé, que les errata 2 portent (repli écrit), avec une réserve de l'auteur.

Les pièces d'avant ne sont pas jointes : chaque erratum cite l'ancien texte et le nouveau, lieu par lieu, et sa table
dit quelle remarque chaque correction porte. Juge d'après ces citations. Si une remarque ne peut pas se juger sans la
pièce d'avant, dis-le en une ligne (« pièce d'avant nécessaire : lieu ») au lieu de deviner.

Les pièces sont des copies nettoyées par programme : le nom du directeur est remplacé par « le directeur », un
identifiant de session et quelques termes de cloisonnement sont retirés, et le premier mot du nom du dossier des pièces
est ôté des chemins. Les empreintes citées dans le texte sont celles des originaux ; un chemin cité peut ne désigner
aucun fichier. Ne relève pas ces écarts.

Pour les calculs v3 : dis seulement si chaque bloc différent répond à une remarque ou au repli, et si un nombre cité
par un erratum diffère de la sortie extraite. Pour la note de la mère : une ligne pour dire si les errata 2 portent le
repli à la lettre ; puis au plus cinq lignes sur la réserve de l'auteur — la « chute » nommée par le repli existe-t-elle
sous les lois écrites, les quatre nombres cités (0,9420, 0,9406, 0,9040, 0,9405) sont-ils dans les extraits de la sortie et
désignent-ils ce que la note dit, et la réserve change-t-elle le verdict sur les errata 2. Ne conçois pas de remède :
un choix s'écrit en nœud ouvert.

## Forme de la réponse (courte)

1. Première ligne : « conforme » ou « à corriger (n points) ».
2. Un tableau, une ligne par remarque, dans l'ordre de la pièce de remarques : remarque ; lieu de la correction ;
   « conforme » ou « à corriger » ; au plus une phrase de motif, seulement pour « à corriger ».
3. Une ligne « Ajouts sans remarque : » suivie de la liste (une ligne chacun), ou « aucun ». Un ajout écrit en nœud
   ouvert non tranché n'en est pas un.
4. Pour chaque « à corriger » seulement : pièce, lieu, ancien texte cité mot pour mot, nouveau texte entier prêt à
   recopier. Rien d'autre.

Pas de résumé des pièces, pas de commentaire sur ce qui est conforme. Écris en français. Ne cite aucun texte qui
n'est pas dans les pièces jointes.
