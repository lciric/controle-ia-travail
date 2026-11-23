# Différences — voie (A), brouillons 1 vers brouillons 2 de l'additif et du devis — v1 (pièce de travail)

Écrit le 2026-11-22 par le rédacteur des deux pièces. Brouillons 1 intacts : additif `7cef2bda410de2dea0d467eeb891c04c22942db603165327054ebe85bf74537d`, devis `12dd845cb700c83388a0705c41d029069edbb769ddc9e6b7b8f4bcedbf86aca6`, arithmétique `calcul-devis-voies-A-B-v1.py`. Une différence par ligne.

## Causes (faits neufs, vérifiés aux sources)
1. `GO-2026-11-22-73` et `GO-2026-11-22-75`, lues au registre de `main` (tête `187f4c41b4a8bcf7c2c4d6206836e6b61858f5c9`) : Lazar choisit la voie (A) ; ligne à part, dépense neuve, 60 USD, échéance 2026-11-30 ; voie (B) gardée pour plus tard ; recharge automatique activée chez le loueur.
2. Correctifs 0020 et 0021, rapports v4 et v5, contre-lecture du 0020, constat du lanceur de session (branche `claude/iib-executante-v5`, commit `83756c6367bc620161a69b54001da364b0e9e1b8`), lus après vérification de chaque compagnon.
3. Deux messages de l'exécutante du 22 novembre (14:40Z et 15:00Z), lus après la poussée des brouillons 1.

## Différences
1. **Accord** : `GO-2026-11-22-75` remplace `GO-2026-11-22-71` pour la voie (A).
2. **Ligne citée par les machines** : `GO-2026-11-22-75` (lisible par le lanceur, vérifié par exécution) au lieu de `GO-2026-11-21-70` ; le `go_id` de la configuration de la voie change de même.
3. **Plafond et coupure** : 60 et 55 USD (ceux du devis scellé) au lieu de 44 et 42 ; pire tenu par les gardes 59,76 USD au lieu de 43,61.
4. **Échéance** : minuterie au plus tard le 2026-11-30T22:00:00Z au lieu du 2026-11-27T22:00:00Z ; aucune création à partir du 2026-11-27T00:00:00Z, inchangé.
5. **Nœud « lecture des plafonds »** : levé par la ligne neuve (« dépense neuve, distincte de GO-2026-11-21-70 ») ; son champ entre chevrons disparaît.
6. **Essai de vitesse** : joué en tête de l'étalonnage, sur les marques de progrès du début et du lot 2, au lieu d'une machine à part ; cause : aucun outil ne lance un essai séparé ; la voie passe de trois machines à deux ; la comparaison de l'ancien chemin au neuf sur une même machine n'est plus faite.
7. **Règle de l'essai de vitesse** : un délai rendu par programme (35,5 minutes pour un compte de 0), qui exige que la voie entière tienne sous la coupure aux prix bornes, la course comptée 1,2 fois plus lente ; elle remplace la règle « 12 tours financés par la formule » appliquée à des durées mesurées à part.
8. **Fichier d'entrées** : le fichier scellé de l'étalonnage, inchangé (dépense passée 0) ; l'écriture de 13 USD dans la dépense passée disparaît ; la configuration peut être scellée avant toute création.
9. **Tirage** : choisi par la variable `IIB_TIRAGE=carte`, posée par l'ordre pour l'étalonnage et pour la course (correctif 0021), et non par une clé de la configuration ; la garde « même tirage » du lanceur est citée.
10. **Configuration de la voie** : cinq clés changent (`go_id`, `code`, `entropie`, `offre.etiquette`, `instances_intouchables`) au lieu de six ; la clé du chemin de tirage et le fichier d'entrées neuf disparaissent.
11. **Code** : les pièces du correctif 0020 et du correctif 0021 sont citées par leur empreinte ; l'arbre annoncé est écrit ; les exigences envers le correctif deviennent « ce que la contre-lecture a établi » et trois exigences restantes.
12. **Liste des essais de l'étalonnage** : version neuve exigée, avec les essais du tirage, l'essai marqué « carte » compris (réponse à la question de l'exécutante) ; raison : l'engagement de la course part avant sa suite d'essais.
13. **Garde de la course** : elle refuse, avant la création, une course qui ne tient pas dans les heures de son échéance au rythme relevé de l'étalonnage ; ses délais sont comptés depuis la marque de début de la course ; la tolérance sur l'heure d'une marque passe de 15 à 6 minutes.
14. **Dépense antérieure déclarée** : la borne de 5 USD est vérifiée sous la ligne neuve (5,52 refusés) ; le programme de l'échéance rend la valeur à déclarer.
15. **Machine 61875617** : sa destruction est faite par Lazar dans la console du loueur ; le préalable devient son absence de l'inventaire ; le champ du mot de la mère disparaît.
16. **Cadre commun aux deux voies** : il devient le cadre de la seule voie (A) ; la règle « la première qui réussit est retenue » est remplacée par : (A) est la voie choisie ; (B), si elle part après que (A) a abouti, est une seconde tentative, dite dans toute citation.
17. **Champ du correctif du lanceur pour deux machines** : disparaît (une seule voie).
18. **Crédit** : la recharge automatique est citée ; les montants au-delà du crédit lu sont recalculés (6,37 ; 21,89 ; 46,77 USD).
19. **Branches réservées** : `essai/iib-explo-v7` pour l'étalonnage et `essai/iib-explo-v8` pour la course (au lieu de v7, v8, v9).
20. **Chiffres** : attendu 19,36 USD et haut 34,89 (deux machines) au lieu de 23,16 et 40,29 (trois machines) ; arithmétique `calcul-devis-voie-A-v2.py`, lignes [Mnn].

## Ce qui ne change pas
La forme (additif à l'ordre scellé de l'étalonnage, qui porte l'ordre de la course) ; la mention « exploratoire, non opposable » ; une machine du saboteur à la fois ; l'entropie neuve ; l'étiquette `iib-voie-a-v1` ; l'échéance qui détruit après consignation ; l'avertissement d'engagement ; les fins écrites d'avance ; l'ordre de lecture ; les arrêts par identifiant.

## Voie (B)
Aucune pièce neuve : l'additif 2-B et son devis restent en brouillon 1, pour mémoire. Leur cadre (ligne `GO-2026-11-22-71`, échéance du 27 novembre, deux voies en parallèle) est dépassé ; ils demandent une version nouvelle si la voie part.
