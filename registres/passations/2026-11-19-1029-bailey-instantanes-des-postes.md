# Note — Bailey : instantanés protégés des trois postes, avant toute destruction (2026-11-19, 10:29Z)

En application du mot de Lazar (« avant toute destruction, inventaire et versement scellé de tout ce qui reste sur la
machine »), sous l'autonomie de 12 h qu'il a accordée vers 09:44Z.

**Arrêts** (aucune destruction) :
- poste v14 (176575468) et poste d'inventaire de l'instance v2 (176780521) : arrêt propre demandé à 10:25:49Z
  (actions 668863853673128 et 668863853673129). Leurs scripts étaient finis : marque du v14 à 10:09:58Z, fin des passes
  du v2 à 10:20:21Z ;
- poste d'inventaire v1 (176778587) : éteint depuis 09:48Z ;
- statut « off » lu pour les trois à 10:26:16Z : heure d'arrêt retenue 1795083976.

**Instantanés** (`create_image`, type snapshot), disponibles, puis protégés contre l'effacement (`change_protection`,
`delete` vrai) à 10:28Z :

| Poste | Serveur | Instantané | Taille de l'image |
|---|---|---|---|
| v14 (relance) | 176575468 | 458234516 | 5,05 Go |
| inventaire de l'instance v1 | 176778587 | 458234528 | 4,80 Go |
| inventaire de l'instance v2 (copies de l'instance, environ 1,2 Gio) | 176780521 | 458234531 | 7,00 Go |

Chaque instantané porte les clés du poste (déploiement, Vast, Hugging Face) : il sera effacé avec la révocation des
clés, après la clôture, sur le mot de Lazar.

**Suite.** Serveurs d'inventaire par instantané v2 (`inventaire-instantane-v2.sh`, commit `14c9bc34`), un par instantané,
seulement après la contre-lecture en cours. Puis vérification des marques, et alors seulement destruction des serveurs
par identifiant (R10), avec preuve d'absence.
