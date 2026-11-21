# Journal de rédaction — brouillon 4 du texte de l'organisme retenu (complément 10 du mandat)

Rédacteur neuf (Claude Fable 5.2), côté saboteur, qui reprend le mandat du rédacteur des brouillons 1 à 3. 21 novembre 2026. Suite des journaux v1 à v6, intacts. Les heures sont rendues par `date -u` au moment dit.

## Lu
- Complément 10 (`50c9691d…`, vérifié par sha256sum) ; mandat (`f2e9150a…`) et compléments 1, 3 à 9, empreintes recalculées. Le complément 2, remplacé par le 3, n'a pas été lu.
- Brouillon 3 (`cb39c12b…`, vérifié) en entier ; son fichier des différences ; le journal v6 ; la vérification du brouillon 3 (`07b5ed3a…`, vérifiée) en entier.
- De l'annexe C du brouillon 3 : la grille et le script du passage « épreuve de fuite, deux lectures, règle composée », son essai de fonctionnement, les douze premières lignes de sa sortie ; quelques lignes du passage rejoué et du script de l'oracle couplé v4 (constantes et fonctions importées) ; les fichiers d'heures.
- Comparaison par programme des sections 2, 3, 7, 9, 11, 12, 14 et 16 des brouillons 2 et 3.
- **Non lu** : le dossier des données de la première course (seuls ses noms de fichiers ont été listés ; les cinq données me sont connues par le brouillon 3 et les compléments) ; rien d'autre de cette course ; aucune pièce du côté des sondes ; aucune consigne privée ; aucun registre hors du dossier du mandat (dont je n'ai ouvert que le mandat et ses compléments).

## Heures du passage « instrument planté pour la branche à contexte réécrit »
grille ecrite : 2026-11-21T16:22:45Z
empreinte du script ajoutee a la grille : 2026-11-21T16:24:03Z
passage lance : 2026-11-21T16:24:03Z
passage fini : 2026-11-21T16:24:57Z (code de sortie 0)
(heures rendues par date -u)
Durée : 55 secondes. Aucune durée limite ne l'a coupé ; aucun incident ; rien n'a été relancé. Entropie : 204960520978699556319978302540082820922. Ces heures ne sont pas vérifiables par un tiers : je ne verse rien moi-même.
Brouillon 4 assemblé, fichier des différences et journal écrits : 2026-11-21T16:34:11Z.

## Choix faits sans mandat exprès, à vérifier
- Règles de lecture du passage, écrites avant : « chance réelle » = un étalonnage sur quatre au point situé sous une lecture continue ; règle de recommandation au nœud 2 à deux conditions. Rendu : (a). Le brouillon 3 recommandait (b) avant de l'avoir dimensionnée.
- Deux rapportés ajoutés à la grille avant le passage : la marge de moitié ôtée pour la seule branche à contexte réécrit (nœud 4, option (b)) ; la loi de Student pour la pente de fuite (m5). Aucun ne change ce qui fait foi. Je n'ai pas déplacé le défaut du nœud 4 au vu de ses chiffres, faute de règle écrite avant ; je l'ai dit dans le texte, avec une confiance « faible ».
- m5 : loi normale gardée, niveau réel écrit (la loi de Student ne corrige pas l'écart).
- M4 : aucune sixième donnée ; risque écrit dans les termes du vérificateur.
- Options dites « non prêtes » et non offertes au scellement tel quel : 2 (c), 3 (b), 5 (b), 5 (c), 6 (c).
- Nœud 1, options (b) et (c) : si le contrôle est déclaré non valide à l'étalonnage, la règle d'arrêt n'est pas appliquée (m12).
- Nœud 7 : deux entrées de plus au fichier scellé (oracles par tour ; actions d'oracle hors tours) ; sous (b), 960 actions hors tours, borne haute (96 épisodes acceptés au plus).
- « Je » : le premier rédacteur dans ce qui est repris, le second dans ce qui est neuf ; dit en en-tête.
- Les dossiers des deux scripts de dépendance, tels que la vérification les nomme, sont intervertis : la chaîne est dans `brouillons/ii-b-saboteur-budget-v2/`, l'oracle couplé dans `brouillons/ii-b-saboteur-budget-v3/`. Corrigé dans l'annexe C, empreintes entières recalculées.
- Le brouillon 4 est écrit entier par un outil rendu (`assembler-brouillon4-v1.py`), qui porte toutes les retouches ; il contrôle l'empreinte du brouillon 3 à l'ouverture.

## Ce que le passage a montré que je n'attendais pas
- L'excès planté ne fait pas partir l'oracle à contexte réécrit : ce n'est plus le nombre de tours qui le retient, mais le rapport de trois et la condition de puissance (le jumeau couplé ne lit que 0,13 à 0,14 décade par action d'un excès tenu en niveau).
- C'est la marge de moitié, non l'instrument, qui tient cet oracle loin du départ au point situé sous la lecture continue ; l'ôter a un prix (départ à tort 13 % à 19 % contre le maître ancré).
- La loi de Student ne corrige pas le niveau de la pente de fuite.

## Non fait, dit dans le texte
- La part des courses parties sans marge qui aboutissent (nœud 4, option (b)) ; la puissance au niveau 1/40 du contrôle du premier coût sur 48 à 96 épisodes (nœud 1, option (c)) ; la puissance à 64 épisodes de la grandeur qui mesure la lecture ; toute option « non prête ».
- Je n'ai pas relu ligne à ligne les sections du brouillon 3 que le vérificateur n'a pas touchées (2 à 4, 6, 7, 9, 11, 14) : elles sont reprises à l'octet.
- Aucun code du dépôt écrit ; aucune suite d'essais lancée ; aucun commit ; aucune poussée ; aucune dépense ; aucune suppression ; aucun refus d'outil.

## Écart à mon cadre, déclaré (ajouté après le contrôle final)
Pour contrôler que l'outil redonne le brouillon 4 à l'octet, je l'ai relancé vers deux copies de contrôle : `/tmp/b4.check` (hors de mon dossier d'écriture ; identique à l'octet au brouillon 4 ; laissée en place) et `table.check` dans mon dossier, **que j'ai supprimée aussitôt** par la même commande. « Aucune suppression » ci-dessus est donc faux d'une unité : un fichier de contrôle créé par moi dans la même commande, copie exacte de la table de traitement rendue, a été supprimé. Rien d'autre n'a été supprimé ; aucun fichier du dépôt n'a été touché.
