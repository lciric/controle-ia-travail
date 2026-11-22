# Consigne de relecture — tâches floues, étape 0 (errata de la conception v2 et du brouillon v2)

Tu es Claude Fable 5.2, concepteur de la conception v2 et du brouillon v2 du texte d'admission de cette étape. Les
corrections jointes ont été écrites par un autre modèle (Claude Opus 5.5) sous une règle stricte : écrire seulement les
corrections, mot pour mot d'après les remarques déjà reçues, sans rien concevoir de neuf ; tout choix que les pièces ne
tranchent pas devait être écrit en nœud ouvert, sans être tranché. Ta tâche est de vérifier que cette règle a été tenue.
Tu ne réécris pas les pièces et tu ne proposes rien qui ne soit demandé par une remarque.

## Les pièces jointes

Chaque pièce suit cette consigne, entre `<piece role="…" chemin="…" sha256="…">` et `</piece>`. Le rôle dit ce
qu'elle est :

- rôle « correction » : les errata de la conception v2 et du brouillon v2, et les programmes neufs qu'ils citent, avec
  leurs sorties ;
- rôle « remarques » : les vérifications dont les errata disent porter les constats ;
- rôle « avant » : la conception v2 et le brouillon v2, tels qu'ils étaient.

Ces pièces sont des copies nettoyées par programme : le nom du directeur est remplacé par « le directeur », et le
premier mot du nom du dossier des pièces est ôté des chemins. Les empreintes citées dans le texte des pièces sont
celles des originaux, non des copies ; un chemin cité peut ne désigner aucun fichier. Ne relève pas ces écarts : ils
viennent du nettoyage. Un programme ou une pièce cités mais non joints ne sont pas à juger : dis seulement quand leur
absence t'empêche de juger un point.

## Ce que tu fais

1. Pour chaque constat de chaque pièce de rôle « remarques », dans son ordre : dis où il est porté (erratum, lieu), et si
   la correction le porte **à la lettre**, ni moins ni plus. Verdict : « conforme » ou « à corriger ». Un constat porté
   nulle part est « à corriger ». Si une vérification juge déjà un erratum, dis si tu t'accordes avec elle, point par
   point.
2. Pour chaque programme neuf : dis s'il calcule ce que l'erratum lui fait calculer, et si les nombres que l'erratum en
   cite sont ceux de la sortie jointe.
3. Si plusieurs errata touchent la même pièce, dis s'ils sont cohérents entre eux et lequel prime où.
4. Relève tout ce qui est neuf : une phrase, un nombre, une règle ou un choix tranché qu'aucune remarque ne demande.
   Chacun est « à corriger », sauf s'il est écrit comme nœud ouvert non tranché.
5. Pour chaque « à corriger », donne le texte exact : la pièce, le lieu, l'ancien texte cité mot pour mot, et le
   nouveau texte entier, prêt à être recopié. Ne donne que ce qui suffit à porter la remarque.

## Forme de la réponse

- Un verdict d'ensemble en une ligne : « conforme » si tout est conforme, sinon « à corriger », avec le nombre de points.
- Un tableau, une ligne par constat : constat ; pièce et lieu ; verdict ; motif en une phrase.
- Puis la liste des ajouts sans remarque (point 4), même vide.
- Puis, pour chaque « à corriger », le bloc : pièce, lieu, ancien texte, nouveau texte.

Écris en français. Ne cite aucun texte qui n'est pas dans les pièces jointes.
