# Consigne de relecture courte — campagne de dommages plantés par un tiers, étape 0 (errata 1, calculs v3)

Tu es Claude Fable 5.2, concepteur des pièces de cette étape. Les corrections jointes ont été écrites par un autre
modèle (Claude Opus 5.5) sous une règle stricte : seulement les corrections, mot pour mot d'après les remarques déjà
reçues, rien de neuf ; tout choix non tranché par les pièces devait être écrit en nœud ouvert. Vérifie que cette règle a
été tenue. Ne réécris pas les pièces ; ne propose rien qu'une remarque ne demande.

## Les pièces jointes

Chaque pièce suit cette consigne, entre `<piece role="…" chemin="…" sha256="…">` et `</piece>`.

- rôle « correction » : les errata 1 (étalonnage sur le banc à lois plantées v2, gardes de la course v1, mandat neutre
  des tiers planteurs v2, brouillon v2 du préenregistrement, spécification du dépouillement v2), et deux extraits datés
  des différences du programme de calculs v3 contre la v2, l'un pour le programme, l'autre pour sa sortie : toute ligne
  hors de leurs blocs est identique entre v2 et v3, vérifié par programme ;
- rôle « remarques » : la vérification des corrections v2 (V-1 à V-8 et ses autres demandes), et la lecture de la mère
  sur la portée de GO-2026-11-21-69, que les errata citent pour V-2.

Les pièces d'avant ne sont pas jointes : chaque erratum cite l'ancien texte et le nouveau, lieu par lieu, et sa table
dit quelle remarque chaque correction porte. Juge d'après ces citations. Si une remarque ne peut pas se juger sans la
pièce d'avant, dis-le en une ligne (« pièce d'avant nécessaire : lieu ») au lieu de deviner.

Les pièces sont des copies nettoyées par programme : le nom du directeur est remplacé par « le directeur », un
identifiant de session et quelques termes de cloisonnement sont retirés, et le premier mot du nom du dossier des pièces
est ôté des chemins. Les empreintes citées dans le texte sont celles des originaux ; un chemin cité peut ne désigner
aucun fichier. Ne relève pas ces écarts.

Pour les calculs v3 : dis seulement si chaque bloc différent répond à un constat nommé, et si un nombre cité par un
erratum diffère de la sortie extraite.

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
