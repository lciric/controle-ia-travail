# Vérification du lot B1 — version 5 (brouillon 2 du préenregistrement) — v4

- Nature : quatrième vérification, classe B, par le même contre-lecteur que `contre-lecture-code-lot-b1-v1.md` et les vérifications `eb7f1819…`, `82a03bf8…` et `e63d64fd…`.
- Date : le 2026-11-22. Opus 5.5. Processeur seul, 0 USD, aucun appel de modèle, aucun réseau.
- Commit vérifié : `b1d60ca0`, paquet `oracles_plantes_v5`.

**Lu :**
- `preenregistrement-pilote-generation-v1-brouillon-2-en-differences.md`, en entier ;
- `note-choix-implementation-lot-b1-v5.md`, sections 8 et 9 ;
- les écarts de familles et de mondes entre la v4 et la v5 ;
- `forme_seule.py`, `retrouvees.py` et `parametres_v5.json` ;
- l'usage des graines dans le code.

**Lancé :**
- `pytest -q tests/test_oracles_plantes_v5_*.py` : 210 essais passés ;
- le rejeu v5 sur la racine 11, dans le bloc-notes : code 0, et P9 exacte ;
- les sondes du bloc-notes :
  - `v5_profond.py` et `v5_profond_f1.py` : vérités au-delà de 3N, plafonds levés ;
  - `v5_sondes.py`, `v5_s.py`, `v5_fuzz.py` et `v5_fuzz2.py` : invariants et données adverses ;
  - `v5_r19.py` ;
  - `v5_r24.py` ;
  - `v5_forme.py`.

Aucun fichier du dépôt n'est modifié, sauf celui-ci.

## Verdict

**Aucune remarque bloquante.**
- Le code est fidèle au brouillon 2, aux écarts près listés au § 1, qui sont tous déclarés.
- Les nouvelles vérités et les nouveaux faux tôt « seuil » sont justes.
- Les invariants tiennent.
- La règle fixe « forme seule » est exacte (P9 tenue à l'unité près), et rien de la clé ne passe dans ce qui est servi.
- Le diagnostic de la racine 24 est juste.

**Ce qui reste n'est pas du code.** Quatre remarques neuves, numérotées 20 à 23 :
- une à corriger, qui touche la mesure et revient au concepteur (20) ;
- trois mineures (21 à 23).

**Une correction de ma vérification précédente.** La remarque 19 était un chemin d'arrêt réel dans la v4 : `pour tout n dans NAT, pour tout k dans [0 .. w(n)], …` lève `KeyError` sur la v4 (`v5_r19.py`). Mon balayage de la v4 ne l'avait pas produit, et ma conclusion « code figé » sur la v4 était donc prématurée. La v5 le corrige.

## 1. Fidélité au brouillon 2

| point du brouillon 2 | code v5 | verdict |
|---|---|---|
| 4 vérités seuil sur 8 par monde, dont au moins 2 à borne naturelle | F1 `vt(t) < 1` et `t >= 1 implique vt(t) > 0` ; F2 `pfa_t(OU, t) < 1` et `prap_t(OU, t) > 0` ; F3 `u(n) > 0` et `w(n) >= 1`. Plus 2 seuils à littéral par famille ; F3 a un résidu évité. Comptes contrôlés par `banque.verifier_formes` | fidèle |
| 2 faux tôt seuil sur 4, dépassés sous N | `seuil_tot` : n₀ tiré dans [1 .. N], c = E(n₀), retenu si E(n₀) dépasse tout E antérieur ; F3 a aussi « résidu atteint » en n₀ ≤ N | fidèle |
| 4 pièges inchangés | gabarits des pièges identiques à la v4 | fidèle |
| P9 : rappel 1 sur les pièges, 1/2 sur les faux tôt, fausses morts 1/2 sur les vérités, entrée dans A1 | rejeu de la racine 11 : 48/48, 24/48, 48/96 ; tout écart compte en A1 (`ecarts_p9`) | fidèle |
| Sous-banque de 208 items | 150 analysés (75, 38, 37) ; 48 témoins hors analyse (2 + 2 par monde, enfant [2]) ; 10 seconds services (enfant [6]) ; 208 identifiants distincts ; servis : `identifiant`, `identifiant_monde`, `enonce` seulement | fidèle |
| « Retrouvée » par les étages 1 ou 2, l'empreinte seule en sensibilité | `retrouvees.py` ; « vraie-bornée » laissée au lot B3, ce qui est écrit | fidèle |
| Graines [9] et [10] | [9] : base aléatoire (même résultat qu'en v1 : 198 mortes, 90 vivantes, 18 vraies-bornées non triviales) ; [10] : classifieur de style | voir la remarque 21 |
| Paramètres « gelés par le préenregistrement » | statut gelé, **sauf** une liste « provisoire » : gabarits, réglages du classifieur, ordre des témoins | écart déclaré, voir la remarque 22 |
| A2 à A13 | non écrites (lot B3) | hors lot, déclaré |
| Refus d'une racine | arrêt, sans contournement (racine 24) | conforme (« aucun repli silencieux ») |

Écarts au brouillon 2 qui ne sont pas dans la note v5, § 9 :
- le choix et le retrait de gabarits par l'exécutant (remarque 22) ;
- le double usage prévu de l'enfant [10] (remarque 21).

## 2. Justesse des nouvelles vérités et des nouveaux faux tôt seuil

Chaque raison écrite a été relue ; toutes sont justes.

**F1**
- `vt(t) < 1` : support plein, donc la masse commune est strictement positive.
- `t >= 1 implique vt(t) > 0` : P ≠ Q, et vt croît en t.
- `vt(t) >= vt(1)` : vt croît en t.
- `puissance(A, t, 1) >= sa valeur à 2` pour t ≥ 2 : 1 − (1 − q)^t croît en t.

**F2**
- `pfa_t(OU, t) < 1` : la somme des marges alpha vaut au plus 18/20 < 1 dans la configuration, mondes perturbés compris.
- `prap_t(OU, t) > 0` : le maximum des beta vaut au moins 1/2.
- `pfa_t(ET ou MAJ ou OU, t) >= sa valeur au premier tour` : 1 − (1 − x)^t ≥ x pour t ≥ 1.

**F3**
- `u(n) > 0` et `w(n) >= 1` (n ≥ 1) : récurrence à coefficients ≥ 1.
- `v(n) >= v(2)` (n ≥ 2) : v(n + 1) − v(n) = (AV − 1) v(n) + BV > 0.
- Résidu jamais atteint : période pure, car pgcd(QU, M) = 1 rend l'application d'état inversible modulo M. Les résidus sont calculés exactement sur une période entière.

**Calcul exact au-delà de 3N**, plafonds levés, avec les vérités de la v4 :
- racines 11, 3 et 20261122 ;
- F1 jusqu'à 3N, puis 5N pour la racine 11 ;
- F2 jusqu'à 10N ;
- F3 jusqu'à 6N.

Aucune instance fausse, indéfinie ou hors capacité.

**Faux tôt seuil.** Le premier contre-exemple est au plus n₀ ≤ N, par construction : E(n₀) dépasse strictement tout E(k) pour k < n₀. Il est certifié de plus par T2 à la plantation. Au rejeu, les faux tôt meurent tous : 48/48.

## 3. Invariants

**Une vérité plantée ne meurt pas et n'arrête pas la batterie.**
- Rejeu sur la v5 des sondes de la remarque 16 et de la forme brute : sans changement (vivante, marquée « collision »), aucun arrêt.
- Balayage adverse sur la racine 3 :
  - 960 énoncés mutés (graine 5) ;
  - 960 autres (graine 7), avec en plus des domaines à fonction de la variable de tête (`[0 .. w(n)]`, `[mod(n, 3) .. u(n)]`, `[0 .. comp(n)]`, `il existe j dans [vt(n) .. 1]`), qui visent la remarque 19 ;
  - puis toute la banque soumise au même registre.

  Résultat : 0 exception, 0 vérité morte ou non vraie-bornée.
- Garantie structurelle inchangée : toute mort par héritage exige un contre-exemple vérifié sur le candidat lui-même jusqu'à 3N. Les nouvelles vérités seuil n'en ont pas (§ 2).

**Une morte ne ressuscite pas, hors de la réserve 15.** Le piège `seuil_u` du monde 8, tué par T6, transmet sa mort aux huit reformulations de la vérification v3 (texte identique, renommage, parenthèses, double négation, `<= c − 1`, deux conjonctions polynomiales, terme nul géant).

**Données adverses (S et proposeur).** Aucune exception (`v5_s.py`). Les sorties illisibles, géantes ou mal formées sont rangées « informe », « sortie de S informe » ou « réfutation fausse ». La vérité soumise ensuite reste vivante.

**Remarque 19 : tient.** Les deux textes qui levaient `KeyError` en v4 sont traités en v5 : l'un vivant non décidé (intervalle hors capacité), l'autre vivant et vrai-borné.

## 4. Base « forme seule »

- **Règle fixe.** Elle est exacte : un seuil ou un résidu évité, une fois le préfixe et les hypothèses retirés. P9 est vérifiée à l'unité près, et un écart entre en A1.
- **Classifieur de style.** Exact :
  - bayésien naïf en rationnels ;
  - aire sous la courbe par la statistique de Mann-Whitney, ex æquo comptés pour moitié.

  Plis par mondes entiers, tirés par [10] : aucun monde du pli d'essai n'est dans l'apprentissage (`plis_par_monde` du rejeu de la racine 11 : 3 mondes par pli).
- **Aucune fuite de clé.** Les étiquettes ne servent qu'à l'apprentissage chez le conteneur de confiance, et le résultat ne va qu'au rapport. Les items servis ne portent ni rôle, ni strate, ni doublon.
- **Réserves de mesure** : voir les remarques 20 et 23.

## 5. Racine 24

**Le diagnostic est juste** (`v5_r24.py`). Dans le premier monde de F2 :
- M = 2, alpha = (1/10, 3/20), beta = (4/5, 7/10) ;
- les trois énoncés « au-dessus du premier tour » (ET ≥ 1/10, OU ≥ 1/4, rappel OU ≥ 4/5) ont le même profil : V partout, sauf dans le deuxième monde perturbé (alpha = (1/20, 1/20), beta = (11/20, 1/2)), où les trois valent F en t = 1 et t = 2 ;
- d'où « redite par profil » et le refus. Les mondes 5 à 7 de la même racine plantent.

**Deux constats à ajouter pour le concepteur.**
- Le troisième monde perturbé a **les mêmes alpha que le monde réel**. L'espace des marges de F2 est petit : 36 couples pour M = 2. Un monde perturbé peut donc ne rien distinguer, ce qui affaiblit l'étage 3 en F2. Cela plaide pour l'option (c), des mondes perturbés tirés distincts du monde réel, ou pour l'option (b).
- La même redite fausse touche aussi les proposeurs. Un proposeur qui trouverait ces deux vérités dans ce monde verrait la seconde comptée « redite », donc hors du numérateur de la précision. Ce n'est pas qu'un problème de plantation.

## Remarques neuves

### 20. La borne naturelle et la répétition des textes révèlent encore la strate — à corriger (au concepteur)
- Preuve (`v5_forme.py`, racines 11 et 20261122). La règle « seuil à borne **non** naturelle ⇒ faux » donne :
  - rappel 48/48 sur les pièges ;
  - 24/48 sur les faux tôt ;
  - **fausses morts 24/96 = 1/4** sur les vérités, contre 1/2 pour la règle fixe de P9.

  La cause : aucun piège n'a de borne naturelle, alors que deux vérités seuil sur quatre en ont une. Le brouillon 2 l'impose (« au moins 2 ont une borne naturelle »).
- De plus, 20 à 21 vérités, contre 7 ou 8 faux tôt et 0 piège, ont un texte identique dans plusieurs mondes. Une vérité à borne naturelle se répète à l'identique ; un piège porte un littéral propre à son monde. C'est un indice pour un bras qui verrait plusieurs items dans un même contexte.
- Le classifieur de style le confirme : aire pièges contre vérités de 4481/4608 ≈ 0,97 (note v5, ligne 54).
- La phrase de P5 « la forme ne révèle plus la strate » n'est donc pas exacte, et P9 ne mesure que la règle la plus grossière.
- Correction possible, au concepteur :
  - donner aussi une borne naturelle à des pièges et à des faux tôt (par exemple « u(n) − w(n) < 1000 » franchi dans ]N .. 3N]) ;
  - ou mesurer et rapporter la règle raffinée comme base nommée ;
  - et dire aux consignes que chaque item est jugé dans un contexte neuf, sans voir les autres.

### 21. L'enfant [10] est pris entier par le classifieur, alors que le brouillon 2 le donne aussi à l'audit de symétrie — mineure
- Lieu : `rejeu.py:128` (`generateur(racine, 10)`). Le brouillon 2 dit « [10] réservé (validation croisée du classifieur de style de l'audit) » et, aux critères de lecture, « l'audit de symétrie emploie l'enfant [10] ».
- Si le lot B3 tire l'audit de [10], il rejouera le même flux que les plis.
- Correction : sous-enfants écrits d'avance, (10, 0) pour les plis et (10, 1) pour l'audit, à inscrire au brouillon.

### 22. Les gabarits sont choisis, et des vérités de la v4 retirées, par l'exécutant — mineure (écart déclaré, à faire approuver)
- Le brouillon 2 fixe les comptes, pas les énoncés. L'exécutant a choisi les 12 gabarits seuil et a retiré, entre autres : Scheffé atteinte, vt croissante, au moins une alerte, queue décroissante, Fréchet de l'union (minimum) et de l'intersection, pire cas décroissant, union des tours, somme télescopée, divisibilité, croissance, forme close affine.
- C'est marqué « provisoire » au JSON. Mais la règle « Qui conçoit » du dépôt confie les oracles au concepteur : la liste doit être approuvée au brouillon 3, ou au scellement, avant le tirage de la graine.

### 23. Aire sous la courbe : scores mis en commun d'un pli à l'autre, et textes identiques entre l'apprentissage et l'essai — mineure
- Lieu : `forme_seule.mesurer`.
- L'aire est calculée sur les scores des quatre modèles de pli mis ensemble. Elle mêle des échelles qui ne sont pas calibrées entre elles.
- Les textes identiques d'un monde à l'autre (remarque 20) se retrouvent dans l'apprentissage et dans l'essai. Ce n'est pas une fuite de clé (même texte, même strate), mais l'aire en mesure une part.
- Correction : rapporter aussi l'aire par pli, et l'aire hors textes déjà vus à l'apprentissage.

## Conclusion

Aucune remarque bloquante. Pour ce qui relève du code, la v5 peut être figée. Restent à trancher par le concepteur, avant le scellement :
- la racine 24 (options a à d de la note v5, avec les constats du § 5) ;
- la remarque 20, qui peut changer des gabarits et donc demander une version neuve et une vérification ;
- les remarques 21 et 22, à inscrire au brouillon ;
- la remarque 23, à porter au script d'analyse.

Les réserves 4 et 15 tiennent.
