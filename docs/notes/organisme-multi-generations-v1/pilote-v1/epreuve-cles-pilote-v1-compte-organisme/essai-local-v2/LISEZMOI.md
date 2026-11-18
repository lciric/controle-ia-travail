# Essai local du programme d'épreuve v2 (aucun réseau, clés factices, doublure sur la boucle locale)

Doublure `doublure-essai-v2.py` (scénario lu dans un fichier, requêtes comptées). Résultats (code ; requêtes reçues) :

| scénario | attendu | obtenu |
|---|---|---|
| normal (identifiants exact, exact, daté `-2026-05-01`) | 0 | 0 ; 3 POST |
| `mini` (identifiant `astra` suffixé `-mini`) | 4 (non conforme, règle du pilote) | 4 ; 3 POST |
| `401` (`astra` refusé) | 4, corps non lu | 4 ; 3 POST ; aucun corps d'erreur dans les sorties |
| `302` (`argon` redirigé) | 4, aucune seconde requête | 4 ; 3 POST, aucun GET |
| `sansusage` (`argon` sans usage) | 4, coût au pire cas | 4 ; `cout_origine` « pire_cas » |
| `illisible` (`argon`, corps non JSON) | 4, coût au pire cas | 4 ; `cout_origine` « pire_cas », 0,01132 |
| `reflexion` (`argon`, 32 000 jetons de réflexion) | 5, dépassement de la ligne | 5 ; `depense_usd` 1,60068 |
| montant `nan` ; montant `0` | 2, aucun appel | 2 ; 0 requête |
| clé à saut de ligne | rien n'est envoyé pour cette clé ; 4 | 4 ; 2 requêtes (les deux autres clés) |
| sortie déjà existante | 2, aucun appel | 2 |

Aucune clé factice ni aucun corps d'erreur dans les sorties et les écrans (recherche faite).

Les sorties JSON de l'essai portent, par construction de la v2, l'identifiant servi (ici celui de la configuration, renvoyé par la
doublure) : elles ne sont pas versées, gardées hors dépôt (`/home/user/hors-depot/essai-epreuve-v2-sorties/`). Les écrans versés
n'en portent aucun.
