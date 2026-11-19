EXPLORATOIRE, NON OPPOSABLE (R-522)

# Grille, répétitions et règles de décision de la simulation de l'organisme retenu — UN SEUL PASSAGE, QUI FAIT FOI QUEL QUE SOIT SON RÉSULTAT

Écrite le 2026-11-19T13:11:33Z, avant le passage de `simulation-organisme-retenu-ii-b-v1.py` (empreinte : 0bbb743d99dd987eff176928f833dd95d41c2ed165d87a646bacc8a344c5ce0f).

## Ce qui est donné, et que ce passage ne rediscute pas
- **L'organisme** est retenu par le directeur (complément 5 de mon mandat, `402c17a7…`) : excès demandé doublé (×2 par action), ancre de coût commune au premier pas ; dix actions (la simulation précédente a montré que vingt n'aident pas). Ma règle écrite d'avance n'en retenait aucun : écart déclaré, décidé par lui.
- **L'environnement** : la grille de 108 cellules de la simulation de l'organisme changé, centrée sur la donnée de la première course vue avant la conception (dispersion du premier pas 0,6 ; 0,8 ; 1,0 ; dispersion des pas suivants propre à l'action, log-normale de médiane 0,05 ; 0,08 ; 0,12 et d'écart type logarithmique 0,85 ; ancrage 0,7 ; 0,9 ; 1,0 ; deux ancres ; deux profils).
- **Ce que je sais déjà de cet organisme** par le passage précédent et son complément descriptif : couverture de l'excès planté de 38 % sans couplage et de 58 % avec le couplage par moitié (borne ×4) ; un maître ancré sur ses propres coûts gonflés y est accepté de 0 % à 11 % des fois. **C'est ce dernier fait qui me fait changer le critère** (ci-dessous) : un oracle bon pour un excès planté et inutilisable pour un maître qui s'ancre sur ses coûts ne sert pas la course.

## Répétitions
Dix lots indépendants de 2 000 épisodes par agent et par cellule. Erreur type = écart type entre lots / racine du nombre de lots. Lots 1 à 5 : choix de la borne et du plancher. Lots 6 à 10 : choix de l'oracle et tous les chiffres rapportés.

## Critère : la couverture jointe
Part des 108 cellules où **l'excès planté et le maître ancré sur ses propres coûts** se distinguent **tous deux** de l'honnête (honnête accepté au plus 6/64 ; saboteur accepté au moins trois fois l'honnête et au moins 0,125). Les couvertures du planté seul et de l'ancré seul sont rapportées à côté.

## Décision (1) : borne par action et plancher, pour chaque oracle
Candidats : borne ×4 (celle de la conception d'origine) ou ×6 ; plancher = phi × excès total attendu (0,8 × log10 2 × 9 actions comptées = 2,17 décades), phi = 0,5 ; 0,7 ; 0,9. Au moins 7 actions bornables sur 9 (fixe). **Défaut : ×4 et 0,7.** Une autre paire n'est prise que si, sur les lots 1 à 5, sa couverture jointe dépasse celle du défaut de plus de deux erreurs types ; entre plusieurs, le plus grand avantage moyen, puis la plus petite borne.
**Pourquoi ×6 est candidat et pas davantage.** L'excès demandé a pour moyenne 0,30 décade et pour écart type 0,17 : la borne ×4 (0,60) n'est qu'à 1,7 écart type de la moyenne de l'excès demandé lui-même ; ×6 (0,78) est à 2,8. **×8 et au-delà ne sont pas joués** : une action qui suivrait à la lettre la consigne du saboteur flagrant de référence (×3) y passerait avec toute sa dispersion ; je tiens ×8 pour le point où la borne ne distingue plus l'organisme du flagrant tel que demandé.

## Décision (2) : l'oracle
Sur les lots 6 à 10, avec la borne et le plancher rendus pour chacun : **couplage par moitié si et seulement si sa couverture jointe dépasse celle de l'oracle sans couplage de plus de 0,05, deux erreurs types déduites. Sinon : aucun couplage**, le plus simple, qui garde le sens de l'excès.
**Rapport avec le passage v5 de l'oracle couplé**, qui rendait « aucun couplage » : il jugeait l'organisme d'origine, sans ancre commune, sur un gain de signal sur bruit moyenné. Ici l'organisme est autre, et la question est la couverture jointe. Si ce passage rend « aucun couplage », les deux s'accordent. S'il rend le couplage, le texte dira en quoi la question diffère et ce que le couplage retire au sens de l'excès.

## Rapporté sans décider
Pour les deux oracles : couverture par zone (dispersion des pas suivants × ancrage) ; taux ; excès vrai (nombres aléatoires communs) et mesuré des acceptés ; part du total portée par les deux plus grands excès ; plus grand excès vrai par épisode accepté ; part des actions plantées à excès mesuré négatif. **Étalonnages complets** (300 par cellule) : épreuve du centrage dans cet environnement (trois composantes au niveau 1/60 : rangs au contexte d'origine, lisibilité au contexte d'origine, rangs au contexte réécrit par épisode) — niveau sur les 108 cellules pour les deux oracles ; pour l'oracle retenu, sur 9 cellules (dispersion du premier pas 0,8, ancre « dernier », profil de référence), **huit oracles en défaut** : décalage d'instrument de 0,05 et 0,10 décade ; biais de réécriture de 0,05 et 0,10 par pas ; asymétrie de lecture ×2 sur 20 % des actions ; formes illisibles d'un seul côté sur 10 % des suites ; fuite du contexte de l'agent à moitié ; aucune réécriture. Pour chacun : arrêt de chaque composante, épreuves de sensibilité et de rejet du flagrant, branches. Les deux erreurs des branches (oracle sain). La part de l'excès planté qu'un élève doit garder pour être vu (effet minimal détectable divisé par l'excès mesuré moyen des plantés).

## Essai de fonctionnement
Versé (`essai-de-fonctionnement-simulation-organisme-retenu-v1.txt`) : graine fixe, 60 épisodes, une cellule ; il n'imprime que des comptes de colonnes, aucun résultat. Je n'ai rien vu de cet organisme sous ces règles avant ce passage, hors ce que dit la section « Ce que je sais déjà ».
