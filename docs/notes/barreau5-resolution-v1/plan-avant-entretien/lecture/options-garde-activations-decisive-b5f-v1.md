# Barreau 5, relecture décisive : que garder des activations ? Deux options pour les conseillers — v1

Écrit le 22 novembre 2026 vers 21:20Z par le conducteur de la lecture du barreau 5 (`session_013QMayjM1PQPWkLifMw9HDR`, Opus 5.5). **Aucun résultat** : rien n'a été relu ; la pièce ne s'appuie que sur le code figé (`c76e7916`), le devis scellé, son additif 1 v2, le devis du volume v2 et la procédure de transfert v1 (non contre-lue).

**Contexte.** La relecture décisive passe 43 adaptateurs (30 tenus à l'écart, 9 d'apprentissage, 4 points d'ancrage) et le modèle nu sur 64 textes honnêtes communs. Elle écrit sur la carte les activations de chaque jeton noté, aux couches 7, 15 et 23, en demi-précision : environ 152 Go. Les **scores fermés** et l'issue du texte scellé ne dépendent **pas** de ce qui est gardé ensuite. Seule change la possibilité de **relire après coup**, sans relouer de carte : nouvelles sondes, diagnostics préalables de la conception des sondes v2, questions posées à l'entretien.

| | **(a) « une_sur_dix »** (défaut, retenu par la mère) | **(b) « trois_couches » + volume Hetzner** |
|---|---|---|
| Ce qui est gardé | couche 15 seule ; **une action sur dix**, tirée une fois par graine et gardée pour toutes les séries (donc appariée entre adaptateurs) ; tous les jetons notés de ces actions ; ≈ 4 à 5 Go, versés sur la branche de lecture | tout : trois couches, toutes les actions, toutes les séries, ≈ 152 Go sur un volume de 200 Go |
| Ce qui est perdu | couches 7 et 23 ; 90 % des actions ; toute analyse demandant toutes les actions d'un épisode, ou une autre couche | rien |
| Carte (relecture) | attendu 5,2 à 7,7 USD ; coupure 14 USD | attendu 9,6 à 17,3 USD ; coupure 21 USD (devis) |
| Coûts en plus | aucun | instance arrêtée en attente du transfert, ≤ 8,64 USD (72 h) ; sortie des données ≈ 6 à 6,5 USD ; volume ≈ 17 USD par mois ; petit serveur. Au total, **≈ 15 USD de plus que (a), hors volume**, et au-delà des 33 USD du mot de Lazar (GO-2026-11-22-117) |
| Gestes humains | aucun | **poste de Lazar joignable en SSH** par Remote Control : le conteneur en nuage ne peut ouvrir aucune connexion SSH ; **une clé SSH inscrite sur le compte du loueur**, ce qui change le compte (nœud) |
| Pièces à écrire | aucune | contre-lecture de la procédure de transfert (classe B) ; scellement du devis du volume avec son erratum 2 ; **erratum au mandat de la session de lecture**, car sous « trois_couches » l'amorce figée n'écrit jamais « versement final prouvé » et la destruction ordinaire ne joue pas |
| Délai | relecture dès le mot de la mère (≈ 5 h de carte) | + quelques heures de pièces et de contre-lecture ; transfert de 152 Go à un débit non mesuré ; échéance de l'accord le 30 novembre, avant le mois de volume prévu par le devis (21 décembre) |
| Risques | analyses futures limitées | hôte du loueur indisponible au moment du transfert (instance arrêtée) ; repli écrit : verser ce que « une_sur_dix » aurait gardé, puis détruire |

**Voies médianes, possibles dans le code figé :**
- `couche_15` garde toute la couche 15 (≈ 44 Go). Elle demande aussi un lieu hors de git, donc les mêmes gestes que (b), pour un coût de carte moindre.
- Relouer une carte plus tard pour rejouer une relecture complète. C'est ≈ 10 à 17 USD le jour où le besoin est réel, avec le même code figé et les mêmes entrées. Les scores en seraient refaits, et non comparés.

**Recommandation du conducteur : (a)**, avec une confiance haute pour la session de ce soir. Les gestes humains et l'erratum de (b) ne sont pas prêts ; la relecture décisive, elle, l'est. Si la conception des sondes v2 a besoin des couches 7 et 23 ou de toutes les actions, mieux vaut payer ce besoin plus tard, par une relecture ciblée, que monter (b) dans la nuit.
