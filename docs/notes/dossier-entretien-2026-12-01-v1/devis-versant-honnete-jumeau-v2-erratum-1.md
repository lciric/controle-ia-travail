# Erratum 1 du devis v2 du versant honnête de l'essai « jumeau contre jumeau » : règle de déclenchement de la coupure de dépense, marge d'horloge, statut de la pièce

2026-11-24T10:04Z (`date -u`). Claude Fable 5.2. Corrige `devis-versant-honnete-jumeau-v2.md` (`95989dbe8131abb5ad5a7e273c538e0d2152d6935dacb0ba9cc99f054a9cf6af`, égale à son compagnon), qui reste telle quelle. **Là où ils diffèrent, cet erratum prime.** Non scellé ; à faire vérifier par le même contre-lecteur. Aucune dépense ouverte ; le plafond cumulé de 12 dollars ne change pas.

## 1. Coupure et horloge (§ 2 de la v2, alinéa « Plafond proposé »)

**Défaut.** La v2 donne une coupure à 10 dollars et une horloge de 5 h 45, sans dire quand la coupure se déclenche. Avec la règle du devis modèle (`devis-passe-activations-saboteur-voie-a-v2.md`, `9a4a794c4332f72d720c23a38db3c0c0a4175ee9a55e34d9627cc16e871eff45`, § 3.4 : arrêt dès que la dépense plus un quart d'heure au pire tarif atteint la coupure), l'arrêt effectif tombe à 9,60 dollars, soit 5,49 heures sur un hôte au bord du filtre. Le pire scénario (9,72 dollars, 5,58 heures) serait coupé avant sa fin.

**Règle retenue.** Lire, à la place de « Première instance : coupure à 10 ; horloge de 5 h 45 (au plus 9,96 sur un hôte conforme) » :

> Première instance : coupure à **11 dollars** tout compris (carte, stockage, réseau). Elle se déclenche **par anticipation**, dès que la dépense relevée plus 0,40 dollar atteint 11, soit un arrêt effectif à **10,60 dollars**. Les 0,40 dollar valent un quart d'heure au pire tarif, arrondi au-dessus (0,351 au bord du filtre : 1,35 + 0,0556 de l'heure) ; ils couvrent le versement de la trace et la destruction. Horloge : **6 h 15** depuis la création. La première barrière atteinte arrête.

Et, à la place de « le plus petit de 10 et de "12 moins la dépense déjà faite" » : « le plus petit de 11 et de "12 moins la dépense déjà faite" », avec la même anticipation de 0,40. Une relance ne part que si ce reste couvre le scénario haut et l'anticipation (6,1 + 0,4 = 6,5 dollars) ; sinon, retour à Lazar.

**Marges, au pire scénario.** Dépense : 10,60 − 9,72 = 0,88 dollar. Temps : sur un hôte au bord du filtre, la coupure agit à (10,60 − 1,88) / 1,4056 = 6,20 heures, soit 0,62 heure (37 minutes) après les 5,58 heures du pire ; l'horloge de 6 h 15 agit d'abord sur les hôtes moins chers (8,95 dollars au tarif attendu). **Cumul** : une première instance coûte au plus 11 dollars, donc moins que 12 ; l'exemple de la v2 tient (incident à ≈ 3,3 : relance coupée à 8,7, arrêt effectif à 8,3, scénario haut couvert, non le pire).

**Conséquence au § 7, point 2 pour Lazar** : lire « ou 11 sans relance » au lieu de « ou 10 sans relance ». Le tableau des scénarios, les prix et les volumes ne changent pas.

## 2. Statut de la v2 (en-tête)

L'en-tête dit « non scellée, à faire vérifier ». Lire : **scellée** (compagnon `.sha256` égal, commit `55cbbafb9`) et **vérifiée par le même contre-lecteur**, « corrections vérifiées », calculs justes (message de la mère du 24 novembre ; rapport de vérification non lu par moi, son chemin et son empreinte sont à porter par la mère).
