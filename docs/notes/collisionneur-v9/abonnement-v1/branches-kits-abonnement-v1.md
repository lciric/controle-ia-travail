# Branches de kits de l'abonnement (voie fichier)

Écrit à 2026-11-22T15:17:20Z (`date -u`). Classe C. Autorisation de Lazar dans la session des collisionneurs : « je t'autorise à pousser des branches kits-abonnement/* ». Chaque branche est orpheline et ne porte qu'un seul fichier, `texte-servi.md` ; l'empreinte du blob égale celle du kit. On ne les supprime pas (mot de la mère).

| branche | commit | modèle | effort | texte servi (sha256) | lignes |
|---|---|---|---|---|---|
| kits-abonnement/puits-etroits-E3-T2-critique-croisee-A-v1 | 22c40618 | claude-fable-5-2 | xhigh | 199b2195… | 962 |
| kits-abonnement/puits-etroits-E3-T2-critique-croisee-B-v1 | 8adac5c5 | claude-opus-5-5 | xhigh | 574e8e7e… | 854 |
| kits-abonnement/jumeau-generale-E3-T2-critique-croisee-A-v1 | 41c5333a | claude-fable-5-2 | xhigh | 74258d8e… | 699 |
| kits-abonnement/jumeau-generale-E3-T2-critique-croisee-B-v1 | 05e5546f | claude-opus-5-5 | xhigh | 80e9b58f… | 643 |

Pour chaque session :
- `source_url` du dépôt, `source_revision` = la branche ;
- ajout système : « Le seul outil permis est Read, sur le fichier texte-servi.md à la racine, lu en entier ; aucun autre outil, aucune recherche ; puis réponds en un seul message. » ;
- invite exacte, à ne pas modifier : « Lis texte-servi.md en entier, puis réponds à ce qu'il demande. »

Le recueil (v6) exige cette invite d'ouverture. Il n'admet que des lectures de ce fichier ; le texte rendu par les lectures doit égaler le kit ligne à ligne ; il refuse tout autre outil et tout second modèle.
