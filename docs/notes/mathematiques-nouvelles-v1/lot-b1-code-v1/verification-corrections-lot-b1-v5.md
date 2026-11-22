# Vérification du lot B1 — version 6 (brouillon 3 du préenregistrement) — v5

- Nature : cinquième vérification, classe B. Même contre-lecteur que `contre-lecture-code-lot-b1-v1.md` et que les vérifications `eb7f1819…`, `82a03bf8…`, `e63d64fd…` et `01a7258d…`. Le 2026-11-22. Opus 5.5, processeur seul, 0 USD, aucun appel de modèle, aucun réseau. Commit vérifié : `35ac9e10` (paquet `oracles_plantes_v6`).
- Lu :
  - dans `preenregistrement-pilote-generation-v1-brouillon-3.md` : § « Mondes plantés et tests de mort », les passages de la Métrique (redite, retrouvée, fuite de style), du Seuil (0,75) et du Plan d'analyse (retirage, graines) ;
  - `note-choix-implementation-lot-b1-v6.md`, §§ 10 et 11 ;
  - les écarts entre la v5 et la v6 des trois familles et de `tests_de_mort.py` ;
  - dans le code v6 : `forme_seule.mesurer`, `banque.construire_banque_avec_retirage` et `banque.mondes_perturbes_distincts`.
- Lancé :
  - `pytest -q tests/test_oracles_plantes_v6_*.py` : 233 passés ;
  - rejeu v6 sur la racine 24 (code 0) et sur 4 racines (arrêt, code 1) ;
  - sondes du bloc-notes : `v6_profond.py` et `v6_profond_f1.py`, `v6_sondes.py`, `v6_s.py`, `v6_r19.py`, `v6_fuzz.py` et `v6_fuzz2.py`.
- Aucun fichier du dépôt modifié, sauf celui-ci.

## Verdict

**Aucune remarque bloquante.** Le code est fidèle au brouillon 3, aux deux écarts déclarés près (§ 1). Les cinq gabarits « valeur à k tiré » sont justes. Les invariants tiennent. L'aire du classifieur est exacte et calculée comme le brouillon 3 le prescrit : hors textes vus, plis par mondes, sans fuite. La règle de retirage est appliquée, avec une lacune de consignation mineure (remarque 24). **La v6 peut être le code figé**, sous réserve que le concepteur approuve le choix sur les pièges (remarque 25).

## 1. Fidélité au brouillon 3 (changements exigés 1 à 9)

| changement | code v6 | verdict |
|---|---|---|
| 1. cinq gabarits à k tiré dans [2 .. N] (enfant [1]) | F1-c, F1-d, F2-c (sans repli, comme au brouillon), F2-d (repli `prap_t(OU, …)`), F3-d ; k tiré en premier dans `gabarits_verites` ; littéraux exacts | fidèle |
| 2. étage 3 non appliqué entre vérités plantées | `t5_redite(…, etages=(1, 2))` à la plantation | fidèle ; **étendu aux pièges** : écart déclaré (remarque 25) |
| 3. mondes perturbés distincts | `mondes_perturbes_distincts` : rejet sur signature (paramètres servis et constantes), flux (0, w, 1), au plus 200 tirages puis arrêt | fidèle |
| 4. exception « retrouvée » et comptes de sensibilité | redite par l'étage 3 seul, levée si la proposition est vraie-bornée et retrouvée (étages 1 et 2) ; `redite_etage`, `redite_levee_retrouvee`, compte au rejeu | fidèle |
| 5. graines (10, 0) et (10, 1) | plis par (10, 0) (`rejeu.py:142`) ; (10, 1) réservé | fidèle |
| 6. P10 en A1 | règle « borne non naturelle », banque et chaque monde ; racine 24 : 48/48 pièges, 24/48 faux tôt, 24/96 vérités | fidèle |
| 7. aires par pli, hors textes vus ; textes identiques entre mondes | aires par pli, mises en commun, hors textes vus ; aire qui fait foi = la plus grande hors textes vus, comparée à 3/4 ; comptes par strate | fidèle |
| 8. liste « provisoire » vidée, sauf le classifieur | seuls plis et lissage restent | fidèle |
| 9. balayage des 42 racines | annoncé (42 sur 42) ; recoupé sur les racines 3, 11, 24 et 20261122, qui plantent toutes, la 24 sans retirage | fidèle (recoupement partiel) |
| retirage : au plus trois tirages, toutes les racines et tous les motifs au manifeste, puis arrêt | `construire_banque_avec_retirage` ; `tirages_max` = 3 au JSON ; 4 racines ⇒ arrêt, code 1 ; journal au rapport et au manifeste si une racine plante | fidèle, sauf la remarque 24 |

Écart non codable, déjà relevé par l'auteur : 16 textes de vérités se répètent encore d'un monde à l'autre (bornes naturelles, vérités structurelles). La phrase du brouillon 3 « le texte ne se répète plus » ne vaut que pour les cinq gabarits à k.

## 2. Les cinq gabarits « valeur à k tiré »

Raisons écrites, relues et justes :
- **F1-c.** vt croît en t, car l'oubli d'une coordonnée fait passer de P⊗t à P⊗(t−1). Donc vt(t) ≥ vt(k) pour t ≥ k.
- **F1-d.** 1 − (1 − Q(A))^t croît en t.
- **F2-c et F2-d.** 1 − (1 − x)^t croît en t pour x dans [0, 1]. Cela vaut pour pfa(ET), pfa(OU) et le repli prap(OU).
- **F3-d.** v(n + 1) − v(n) = (AV − 1) v(n) + BV > 0.
- **Les cinq.** L'hypothèse t ≥ k est satisfaite jusqu'à N, puisque k ≤ N : il n'y a pas de vacuité.

Calcul exact au-delà de 3N, plafonds levés, aucune instance fausse, indéfinie ni hors capacité :
- racines 11, 24 et 20261122 : F1 jusqu'à 3N, F2 jusqu'à 10N, F3 jusqu'à 6N ;
- racine 3 : F1 jusqu'à 5N.

## 3. Invariants

- **Une vérité plantée ne meurt ni n'arrête la batterie.**
  - Rejeu sur la v6 des sondes des remarques 16 et 19 et de la forme brute : inchangé.
  - Balayage adverse, racine 3 : 960 énoncés mutés (graine 11), puis 960 autres avec domaines à fonction (graine 12). Ensuite, toute la banque au même registre. Résultat : 0 exception, 0 vérité morte ou non vraie-bornée.
- **Aucune morte ne ressuscite, hors réserve 15.** Le piège tué par T6 transmet toujours sa mort aux huit reformulations.
- **Données adverses** (S et proposeur) : aucune exception (`v6_s.py`).
- **L'exception « retrouvée » n'ouvre aucun chemin de survie.**
  - Elle ne fait que basculer le drapeau de redite.
  - L'héritage de mort est cherché avant T2 (étage 1), puis par `morte_equivalente` après T5, indépendamment de l'issue de T5 (`tests_de_mort.py`, fin d'`appliquer_batterie`). Une morte reformulée hérite donc de sa mort, qu'elle soit « retrouvée » ou non.
  - L'exception n'agit que sur une vivante, vraie-bornée, égale par les étages 1 ou 2 à une vérité plantée du même monde (liste passée par l'appelant), et redite par l'étage 3 seul. Elle ne peut rendre « non redite » qu'une vraie retrouvée.

## 4. Aire du classifieur de style

- **Exacte.** Le bayésien naïf est en rationnels. L'aire est la statistique de Mann-Whitney, ex æquo pour moitié.
- **Plis par mondes entiers**, tirés par (10, 0) : 3 mondes par pli, aucun monde d'essai à l'apprentissage. Exemple, racine 24 : plis `[3, 2, 1, 1, 3, 0, 0, 2, 2, 0, 3, 1]`.
- **« Hors textes vus » bien calculé.** Un item d'essai est écarté si son texte exact figure parmi les textes d'apprentissage du pli. Racine 24, effectifs restants : 32 vérités, 27 faux tôt, 48 pièges.
- **Aire qui fait foi.** C'est la plus grande des deux aires hors textes vus, conformément au brouillon 3. Racine 24 : 745/768 ≈ 0,970, au-dessus de 3/4, rapportée telle quelle.
- **Sans fuite.** Les étiquettes ne servent qu'à l'apprentissage, chez le conteneur de confiance, et le résultat ne va qu'au rapport.
- **Réserve de description.** Hors textes vus, l'aire repose sur une trentaine de vérités par racine, surtout des seuils à k et des vérités propres au monde. Son intervalle n'est pas rapporté ; il serait utile au lecteur de H3.

## Remarques neuves

### 24. Quand toutes les racines tirées sont refusées, le journal des refus ne va pas au manifeste — mineure
- Lieu : `banque.construire_banque_avec_retirage` et `rejeu.executer`. Si les trois racines sont refusées, `GardeArret` remonte avant toute écriture. Les motifs ne survivent que dans le message d'erreur sur la sortie d'erreur.
- Le brouillon 3 dit : « Toutes les racines tirées et le motif de chaque refus vont au manifeste. »
- Correction : écrire et sceller un manifeste d'arrêt, avec les racines, les motifs et la commande, avant de sortir en code 1.

### 25. T5 n'est plus appliqué aux pièges à la plantation, et une redite par l'étage 3 entre plantés n'est plus un écart — mineure (choix à faire approuver, déjà déclaré)
- Lieu : `note-choix-implementation-lot-b1-v6.md`, ligne 60.
- Le brouillon 3 n'exige aucune condition de redite des pièges, donc le code n'est pas infidèle. Mais il n'exige pas non plus d'en retirer une.
- Conséquence pour la mesure : deux pièges d'un même monde peuvent avoir le même profil (racine 20261122). Un proposeur qui les proposerait tous deux verrait le second compté « redite ». « Piégée » se juge, elle, aux étages 1 et 2, donc la mesure P2 n'est pas touchée.
- À confirmer par le concepteur, ou à écrire au brouillon. Le compte `redites_par_l_etage_3_seul` du rejeu permet de le suivre.

## Conclusion

Aucune remarque bloquante. **La v6 (`src/controle_ia/oracles_plantes_v6/`, commit `35ac9e10`) peut être le code figé du lot B1**, une fois que le concepteur aura approuvé le choix de la remarque 25. La remarque 24 est à corriger à l'occasion, en version neuve si le code est rouvert ; sinon, le lot B3 doit consigner les refus au manifeste. Les réserves 4 (tête du registre au manifeste de course) et 15 (héritage limité au même squelette) tiennent. L'aire de style au-dessus de 0,75 conditionne la lecture de H3, selon la table du brouillon 3 ; ce n'est pas un défaut du code.
