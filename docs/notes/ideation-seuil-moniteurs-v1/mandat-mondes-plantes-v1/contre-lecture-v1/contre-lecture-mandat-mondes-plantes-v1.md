# Contre-lecture — mandat de l'auteur des mondes plantés et son devis (course « seuil et moniteurs ») — v1

- Contre-lecteur neuf, modèle O. Je n'ai écrit aucune pièce de la course « seuil et moniteurs ». Règle R2 ; décision D-M15.
- Écrit le 2026-11-21 ; relevé de `date -u` : 08:06:04Z.
- Aucun appel, aucune dépense, aucune clé, aucune écriture dans un dépôt, aucun commit. Aucune source de la liste scellée ouverte, aucune branche de quarantaine ni de matière première. Aucun refus de permission, de classifieur ni de garde.
- Décisions de la mère prises en compte : 07:56Z (le monde à trois populations et au moins un des mondes C, D, E ou G entrent s'ils ont une vérité exacte et des témoins, et le mandat le demande comme exigence ; les 400 tirages et le test exact à 0,001 servent à la seule couverture des témoins) ; 07:57Z (D-M11 à D-M15, règle de la pièce la plus stricte, recommandation sur N4).

## 0. Verdict : **À corriger**

1. **Le mandat de l'auteur est bien construit** : sortie en JSON à onze clés ordonnées, témoins d'abord, grammaires fermées ; aucun critère de mort, aucune lecture des sources ni des fiches, aucune vérité sur la machine jetable ; le monde à K actions est dit « sur devis à part » ; aucune recette ; aucun nom de modèle ni de fournisseur.
2. **Il ne porte pas encore les décisions de la mère** :
   - il admet une vérité « par tirage scellé » ;
   - il n'exige de témoins ni pour le monde M ni ne dit ce qui écarte un monde sans vérité exacte ;
   - il emploie `population_de_lecture`, et non `portee_de_la_garantie` ;
   - il laisse à l'auteur la supposition que cassent les grappes.
3. **Il porte quatre défauts de fond** :
   - T09 est inversé : tel qu'il est écrit, il ne peut pas mourir ;
   - T08 et T12 n'ont pas de sort unique, faute de convention ;
   - il annonce un « calcul scellé » qui n'existe pas encore ;
   - il dit « non contre-lue » dans un texte qui partira scellé.
4. **Correction prête** : un jeu de 22 remplacements à texte exact, essayé sur copie avec l'outil contre-lu. Les 22 ancres sont trouvées une fois chacune. La sortie fait 26 582 octets (§ 3).
5. **Le devis est juste.** Le programme, rejoué deux fois, donne des sorties égales entre elles et égales à la sortie versée. Les tarifs sont bien ceux des lignes 100 à 141 du collisionneur, et les statuts « lu » et « à relever » sont justes. Le plafond est de 4,26 USD, et le total avec la course de 118,74, sous 120. Trois retouches : la taille du mandat corrigé, le plafond du premier essai, et une phrase du scellement qui interdit toute dépense avant le préenregistrement court (§ 5).

## 1. Pièces lues, empreintes recalculées

Toutes sont égales à leur compagnon. Pour les pièces d'`origin/main`, l'extraction s'est faite par `git show` redirigé, après une mise à jour par `fetch` (`f059943d8..e1103c83b`).

| pièce | empreinte |
|---|---|
| mandat du rédacteur | `75f0acd35afb1bf6b4cb55caa12e5d6e30485ede70dc0794025e5407d4653337` |
| mandat de l'auteur | `6774507cbf149235d86e0c460aae339585956bca5b23db992a85d3121ca3c1b9` |
| devis | `4f5dca99a527586228480fe629269fe29a37ecb13b7ab93e4c01c4b3f43409ae` |
| programme du devis | `d715bcf2ed522737934f8a38994e27997e25f46874c4db96058e3c6090f00385` |
| sortie du devis | `fb467010bb47ab2ef36a5b32f6caf0aea91bb61d08229e7df1f480f268715123` |
| rapport du rédacteur | `a38468b487833023a88f1817bccd2f82897487fa9da54b25020f4cfe9f98468c` |
| table d'empreintes (`table-empreintes-mandat-mondes-plantes-v1.txt`) | `59c16ef4147d697a80e397da41c8598b6251c4f8fa056beae193d12d00092ab2` ; elle redit les cinq empreintes ci-dessus |
| note de conception générale (§ 2, § 4.3, § 6 lus) | `4f3ae86fe2ffa8c8abeeef95a2c574e723b731db11bb3b20d65d0ab534f11298` |
| son programme de calcul : lu seulement pour les définitions de T12, T13 et des grappes, aucune valeur reprise | `301c0f52fc11c7a7bc9de2292b51f56b314277fda72402fc7c76b33323fdb857` |
| note du moniteur de dissonance | `403fe3e2827540569e45c82866eea98d91d977fad74d5c518f852c806e82fae2` |
| synthèse du collisionneur (passages sur l'échec) | `dc734fabb9f4cc96c82fd91c37ae08b5ca7789012fcd47e72668e623c3002522` |
| registre servi des visées (noms neutres) | `3bcb94e672390f6f68ca318f214a749dbb0fb14cf8ca4c44728beccf18440d1e` |
| scellement de la conception | `4286bf39363a40907364c124a17bd38d41a74f3387a17227228be33d6b1c5c07` |
| collisionneur v9 v3, lignes 100 à 141 | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910` |
| ordre v5 | `8712ddd08dc1cefb72115b67f44338e84cbf45b9244b602cbaed73076a3b8f24` |
| préenregistrement court v5 | `b65dab4ec91335b4e3e6ad629599386c07e56a7897f98d25514d4d439880d917` |
| outil de remplacement (`scripts/remplacer_texte_exact_v1.py`) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

## 2. Le mandat de l'auteur (point 1)

| question | réponse |
|---|---|
| Est-il servi tel quel, et tout ce qui part au relais y est-il écrit ? | **Oui, à une réserve près.** Le texte se dit complet : « Rien d'autre ne t'est servi ». Mais sa ligne 5 dit « Pièce de travail, non contre-lue » et nomme le rédacteur : une fois le texte scellé, cette phrase sera fausse quand le relais la lira. Remplacement n° 1. |
| Sa forme de sortie est-elle vérifiable par programme ? | **Oui, sous trois réserves.** (a) La règle « aucune clé de plus, à aucun niveau » contredit les objets dont les clés sont libres (`jumeau_sain`, `valeurs_de_plus`, `signal_valeur`, `signal_intention`) : remplacement n° 16. (b) La règle « quatre décimales au moins » ne se vérifie pas sur un JSON une fois lu, puisque `0.5000` y devient `0.5` : il faut la vérifier sur le texte brut ou la lever (remarque). (c) L'ordre des clés et la place de `temoins` avant `familles` se vérifient sur le texte brut, comme le rapport le prévoit. |
| Est-il sans critère de mort, sans lecture des sources ni des fiches, sans vérité sur la machine jetable ? | **Oui** (§ 5 du mandat). Aucun nombre de tirages, aucun niveau, aucun seuil d'épreuve. Le seuil d'écart de 0,001 du § 6.4 est une tolérance de vérification, pas un critère de mort. La décision de 07:56Z sur les 400 tirages ne touche donc pas le mandat. |
| Le monde à K actions est-il dit « sur devis à part » ? | **Oui** (§ 3.3), et le devis le confirme (§ 4, point 1). |
| Y a-t-il une recette ? | **Aucune.** Le saboteur est une loi décalée ; le § 5 interdit tout procédé. Aucun nom de modèle ni de fournisseur : vérifié par recherche de motifs. |
| D-M12 : l'auteur ne reçoit-il aucune valeur vraie de la note ? | **Oui.** Le mandat ne donne aucune couverture et aucun décalage chiffré, seulement des paramètres. Mes remplacements n'en ajoutent pas : 0,20 et 0,30 sont déjà des paramètres du monde S. |
| D-M14 : l'auteur écrit-il les témoins des mondes, et la mère ceux de l'étage et de la mise en fiches ? | **Oui.** Le témoin « fiche non programmable » n'est pas dans le mandat ; il reste à la mère. |

**Défauts de fond.**

1. **T09 est inversé.** Le § 2 du mandat dit qu'une règle « déclare tenir » sur un monde quand aucune des suppositions qu'elle déclare n'y est cassée. Or T09 « déclare `aucune derive…` comme tenue », et F casse justement cette supposition. T09 ne déclarerait donc pas tenir sur F : il ne pourrait pas mourir, et son sort serait une fragilité rapportée. La note dit le contraire : « une règle qui déclare tenir sous dérive et ne s'abstient pas doit mourir ». Pour mourir, T09 ne doit déclarer aucune supposition. Remplacement n° 5, plus une règle générale : un témoin imposé ne déclare aucune supposition, sauf mention contraire (n° 4). La même règle fixe T10, T14 et T17.
2. **T08 n'a pas de sort unique.** La règle `quantile_empirique` n'a pas de convention. À n = 400 et au niveau 0,99, le seuil est le 4ᵉ ou le 5ᵉ plus grand score selon la lecture, et la couverture change. Je fixe la convention : le ⌈n × niveau⌉-ième plus petit score, sans interpolation (n° 21).
3. **T12 et T13 sont sous-déterminés.** Ni le test répété (lequel ? avec quelle inégalité ?) ni le taux parié ne sont dits ; le sort calculé par l'auteur ne serait pas comparable au nôtre. Je les écris comme dans le programme de la note : un test binomial exact unilatéral du compte cumulé, alerte quand la valeur p est strictement sous 0,01 ; un pari de 0,30 contre 0,20, alerte quand la richesse atteint 100 ou plus (n° 6, 7, 21). Ce sont des définitions, aucune valeur vraie.
4. **Le sens de l'alerte n'est dit que pour la base.** Sur G, avec des valeurs répétées, « strictement supérieur » et « supérieur ou égal » ne donnent pas le même sort. Une phrase dans la grammaire (n° 20).
5. **H est ambigu sur l'usage.** La couverture du « plus grand de 300 » suppose qu'en usage les épisodes viennent de familles neuves, avec une variance totale de 1, comme dans le programme de la note. Le mandat ne le dit pas (n° 9).
6. **T05 et T07 meurent « sans gain », pas sur la garantie.** La base jouée contre elle-même a un écart nul (v5, banque des témoins). Le mandat ne demande que le taux moyen : l'auteur écrirait « tient ». Remplacements n° 8 et 18.
7. **« Nous avons notre propre calcul scellé »** est faux aujourd'hui. Le programme de la note n'est ni contre-lu ni scellé, et il ne couvre ni T05, ni T08, ni T14 à T17. De plus, T09 à T11 dépendent de la loi que l'auteur choisira. Je remplace la phrase par « un programme scellé avant la lecture de ta sortie » (n° 4). Ce programme est à écrire (§ 7).

## 3. Jeu de remplacements, essayé sur copie

- Jeu : `remplacements-mandat-auteur-mondes-plantes-v1-vers-v2.json` (`73c642b45813452bff4323c592e851c952df2df8b48da5dc97fb011fc67b1ac6`), dans ce dossier.
- Essai par `scripts/remplacer_texte_exact_v1.py` (`391db990…`), copie tirée d'`origin/main`.
  - Cible : `6774507c…`.
  - Sortie : `essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v2.md`, `58a69c74cdb020308074d96e67b16445161d800f9a124bd1f0761ee134335efa`, 26 582 octets.
  - Journal : `396da7cc6a6ab722638c5563359103d1970bd4e77fe43c4da521e76b41e8d06a`.
  - Résultat : 22 remplacements, chaque ancre trouvée une fois, aucun refus. Aucune trace de `population_de_lecture`, `par_tirage_scelle`, « à toi de le dire », « non contre-lue », « modèle F » ni « trois familles » dans la sortie.
- Le mandat corrigé prend un nom neuf en v2 (règle R12), et son compagnon.

| n° | où | quoi | pourquoi |
|---|---|---|---|
| 1 | en-tête | retire « par le rédacteur…, modèle F. Pièce de travail, non contre-lue. » | texte servi tel quel après scellement |
| 2 | § 2 | n vaut 200, 300 ou 400 [proposition] | accord avec v5, § 7 bis (tailles) |
| 3 | § 2, piège de l'échec | `population_de_calibration` et **`portee_de_la_garantie`** (valeurs de la v5, sans accents comme les sept suppositions) | D-M11 de la mère : un seul champ, celui de la v5 |
| 4 | § 3.1 | calcul « scellé avant la lecture » ; témoins imposés sans supposition déclarée ; portée par défaut | défauts 1 et 7 |
| 5 | T09 | aucune supposition déclarée | défaut 1 |
| 6, 7 | T12, T13 | définitions complètes | défaut 3 |
| 8 | § 3.1 | T05 et T07 : puissance et écart à la base | défaut 6 |
| 9 | H | variance 1, familles neuves en usage ; supposition `episodes honnetes echangeables` | D-M13 de la mère ; défaut 5 |
| 10 | § 3.2 | **« Vérité exacte : une exigence »** : C, D, E, G et M demandés avec une vérité exacte et des témoins ; sinon le monde est écarté au scellement, et c'est dit | mot de la mère, 07:56Z ; règle de la v5 |
| 11 | § 3.3, monde M | témoins exigés, dont celui que la v5 propose (garantie dite parmi ceux qui échouent, au réglage γ = 0) | v5, § 7 bis ; mot de la mère, 07:56Z |
| 12, 13 | § 3.4 | deux familles de son choix au plus, à vérité exacte, avec leurs témoins, retenues seulement au scellement | v5 : les lignes du registre n'ajoutent aucun monde ; place de sortie ; moins de prise pour une lignée qui a des textes en jeu |
| 14, 15 | § 3.4 | retire les lignes « Angle mort des signaux rares » et « Dépendance extrême… / Agrégation… » | la v5 les dit hors des mondes de cette course (« aucun ») |
| 16 | § 4.1 | objets à clés libres nommés | vérifiabilité |
| 17 | § 4.2 | clés `portee_de_la_garantie` et `signal` | n° 3 et n° 11 |
| 18 | § 4.2 | `valeurs_de_plus` aussi pour T05 et T07 | n° 8 |
| 19 | § 4.2 | `verite.mode` : `exacte` seulement | règle de la pièce la plus stricte |
| 20, 21 | § 4.3 | alerte strictement au-dessus du seuil ; convention du quantile ; test répété défini | défauts 2 à 4 |
| 22 | § 6.2 | témoins du monde M exigés ; un monde présent mais sans vérité exacte n'est pas une sortie illisible : il est écarté | pas de second essai payé pour cela |

## 4. Accord avec la v5 (point 2) : table des écarts

**Règle de la mère** : un monde n'entre que s'il a une vérité exacte et des témoins ; sur ce point, la pièce la plus stricte gagne. Dans la table, « M » désigne le mandat de l'auteur v1 et « v5 » l'ordre v5, § 7 bis, avec le préenregistrement court v5, objet gelé, point 5.

| # | objet | mandat v1 | v5 | suit la note | plus strict sur la règle | correction |
|---|---|---|---|---|---|---|
| 1 | les quatre mondes de la note | présents : 1 = A, 2 = F, 3 = H, 4 = S | cœur des mondes | les deux | — | aucune |
| 2 | mode de la vérité | `exacte` ou `par_tirage_scelle` | exacte seulement (« aucun tirage n'y entre ») | v5 | **v5** | M, n° 19 et n° 10 |
| 3 | ce qui écarte un monde sans vérité exacte | rien n'est dit | écarté, et c'est dit au scellement | v5 | **v5** | M, n° 10 et n° 22 |
| 4 | C, D, E, G | imposées, vérité exacte non exigée | n'entrent qu'avec vérité exacte et témoins | hors note | **v5** sur l'entrée ; le mot de 07:56Z en fait une exigence du mandat | M, n° 10 : exigées, avec vérité exacte et témoins ; l'entrée suit la v5 |
| 5 | B (queue lourde) | famille imposée | seconde loi du monde 1, si sa vérité est exacte | v5 | **v5** | M, n° 10 ; le nom (famille ou variante) se fixe au scellement |
| 6 | monde à trois populations | imposé, vérité demandée, aucun témoin exigé | entre seulement avec vérité exacte et témoins | hors note | **v5** | M, n° 11, n° 17 et n° 22 |
| 7 | supposition cassée par H | laissée à l'auteur | « épisodes honnêtes échangeables » | v5 | **v5**, et D-M13 de la mère | M, n° 9 |
| 8 | portée de la garantie | `population_de_lecture`, trois valeurs | `portee_de_la_garantie`, valeurs fermées | v5 | **v5** (D-M11) | M, n° 3 et n° 17 ; rapport, D-M11 à clore |
| 9 | famille I et T14 à T17 | imposés | une garantie à portée conditionnelle n'est jouable que sur un monde où l'issue est plantée (« variante du monde 1 où l'échec est planté ») | hors note | même règle | C et I sont cette variante ; entrée par n° 10 ; aucune autre correction |
| 10 | familles libres tirées du registre | jusqu'à trois, avec deux lignes que la v5 dit hors course | le registre « n'ajoute aucun monde » | v5 | **v5** | M, n° 12 à n° 15. La mère peut aller plus loin et les retirer toutes |
| 11 | famille tenue à l'écart | une ou deux | gardée comme parade | les deux | même règle (vérité exacte, par n° 19) | aucune |
| 12 | tailles de calibration | 200 ou 400 | 200, 300 et 400 ; 1 000 pour le témoin de marge | v5 (témoins de la note à 299, 300 et 1 000) | hors règle | M, n° 2 |
| 13 | T09, dérive | déclare la supposition, donc ne peut pas mourir | « déclare tenir sous dérive et ne s'abstient pas » : doit mourir | v5 | hors règle (erreur du mandat) | M, n° 4 et n° 5 |
| 14 | témoin de l'étage « quantile à 99 % » | T08 gardé, sans convention | retiré de l'étage pour un sort exact | v5 | **v5** (sort exact) | M, n° 21 donne un sort exact à T08 ; la mère peut aussi le retirer |
| 15 | base jouée contre elle-même | T07, sort non dit | « doit mourir (sans gain) » | v5 | hors règle | M, n° 8 et n° 18 |
| 16 | monde S et sa variante | aucune ; « aucune dérive » | idem | les deux | — | aucune |
| 17 | monde à K actions | sur devis à part | sur devis à part | les deux | — | aucune |
| 18 | critères de mort et tirages | absents du mandat | dans la v5 | — | — | aucune (décision de 07:56Z sans effet sur le mandat) |

**Lecture.** Sur la vérité exacte et les témoins, la v5 est partout la plus stricte, et c'est elle qui suit la note. Toutes les corrections portent sur le mandat de l'auteur ; aucune sur la v5. Une seule touche aussi le rapport : D-M11. La v5 garde un défaut qu'elle dit elle-même (réserve 5) : son § 7 porte encore sept familles et le témoin du quantile. Le mandat corrigé s'aligne sur le § 7 bis, qui prime.

## 5. Le gonflement α / P(échec) (point 3)

- **La borne est juste.** P(alerte | échec) = P(alerte et échec) / P(échec) ≤ α / P(échec), sous le nul exact. Le mandat dit 20 % pour α = 1 % et P(échec) = 5 % ; la v5 dit 5 % pour un échec sur cinq. Les deux sont exacts et cohérents avec la synthèse (verdict 3 (iii)).
- **La famille I est réalisable à 0,001 près.** La borne n'est atteinte exactement que si les honnêtes qui réussissent ont une probabilité nulle de dépasser le seuil, ce qu'aucune loi à support non borné de la grammaire ne donne. Le mandat dit bien « ou s'en approche à 0,001 près ». Par exemple, à P(échec) = 0,05 et avec deux normales, la part des honnêtes qui réussissent au-dessus du seuil doit rester sous 5,3 × 10⁻⁵ environ, ce qu'un décalage d'environ trois écarts types permet. Je ne donne cet ordre de grandeur que pour attester la faisabilité ; il n'entre pas dans le mandat.
- **T14 à T17 sont justes, si aucune supposition n'est déclarée** (remplacement n° 4). T15 et T16 tiennent par les statistiques d'ordre (0,9505 sur leur population). T14 et T17 lisent sur ceux qui échouent un seuil réglé sur tous les honnêtes. S'ils déclaraient « l'honnête qui échoue ressemble à l'honnête qui réussit », C et I casseraient cette supposition, et ils ne pourraient plus mourir. C'est le même piège que T09.
- **Le monde M est juste** : il demande P(échec) et le taux parmi ceux qui échouent au quantile vrai à 99 %. Il lui manquait des témoins (n° 11).
- **Accord entre la v5 et D-M11.** Le sens est le même : la mort « invalide » se lit sur la population que la fiche dit. Les deux pièces ont été écrites en parallèle et ne se contredisent que par le nom (« population de la garantie » au rapport, `portee_de_la_garantie` à la v5) et par les valeurs. La mère a tranché pour la v5 (07:57Z). Le mandat corrigé emploie ce seul nom (n° 3 et n° 17). `population_de_calibration` reste un champ du témoin : il dit l'entrée de la règle, pas sa portée.
- **Une remarque sur la forme de D-M11.** Ajouter un champ à la fiche est un écart à l'ordre v4 scellé, donc un nœud, et un défaut à 48 heures ne pouvait pas s'y appliquer. Le point est sans objet maintenant, puisque la mère a décidé.

## 6. Le devis (point 4)

- **Rejeu.** Deux exécutions sous Python 3.13.18 (`python3 -B`), sorties égales entre elles par `cmp` et égales à la sortie versée (`fb467010…`).
- **Les tarifs sont pris aux lignes 100 à 141 du collisionneur**, que j'ai vérifiées :

  | candidat | ce que dit la table | statut au devis |
  |---|---|---|
  | R2-a | 10 et 50 en borne haute, tarif lu sur une page versée et scellée ; plafonds 18 000, 32 000 et 8 192 | « lu par la table », juste |
  | R2-b | 4 et 20 « RAPPORTÉ » ; plafonds 65 536, 65 536 et 32 768, « réglages supposés » | « à relever », juste |
  | R3 | 10 et 50 « SUPPOSÉ » ; plafonds 8 000, 32 000 et 0 | « à relever », juste |

  La garde de 2,5 caractères par jeton est celle de la table.
- **L'arithmétique est juste.** Le pire par essai de R2-a vaut 12 000 × 10 / 10⁶ + (32 000 + 8 192) × 50 / 10⁶ = 2,1296. Le plafond est de 2,13 par essai, 4,26 en tout. Le total 114,48 + 4,26 = 118,74 laisse 1,26 sous 120. La ligne de GO dit bien : deux essais au plus, le second seulement après une sortie illisible, jamais après un refus.

**Trois retouches**, à porter au devis v2 et à son programme v2 (nom neuf, règle R12).

1. **Taille du mandat corrigé** : 26 582 octets, soit 10 633 jetons d'entrée. Pour R2-a, le cas bas reste à 0,36 et le cas haut passe de 3,51 à 3,53. Le pire et le plafond ne changent pas, puisqu'ils comptent la garde de 30 000 caractères.
2. **Premier essai de R2-a au plafond de relance.** Si l'interface compte la provision de réflexion dans le plafond de sortie, il ne reste que 18 000 − 8 192 = 9 808 jetons pour une sortie qui peut en demander 16 000. La sortie serait tronquée, donc illisible, et un essai sur deux serait perdu. En partant à 32 000 dès le premier essai, le pire ne change pas et le cas haut vaut 2 × 2,11593, soit 4,23, sous 4,26.
3. **Une phrase du scellement contredit le calendrier.** Le scellement `4286bf39…` dit : « Aucune dépense avant ce scellement », c'est-à-dire avant celui du préenregistrement court. Or ce préenregistrement attend les mondes, que seul cet appel payant produit. La ligne de GO doit le dire : « appel de préparation, hors de la phrase "aucune dépense avant ce scellement" de `4286bf39…`, par le mot de Lazar ». Sinon les deux pièces se contredisent.

## 7. Le relais retenu (point 5)

**Mon jugement : choix acceptable, R2-a, confiance 0,6.**

- **Place de sortie.** L'argument tient sous la retouche 2 du § 6, et le plafond de relance de R2-a laisse de la marge.
- **Lignées.** Avec la recommandation de la mère sur N4 (l'expérimentateur au premier relais, pas encore accordée), l'affectation est cohérente avec D-M9 : un traducteur au premier relais, l'auteur au deuxième, le second traducteur au troisième, dont le plafond de 8 000 jetons contient une fiche.
- **Risque de textes sources.** Il est réel, et le rapport le dit juste : deux des trois consultations viennent de deux modèles du deuxième relais (v5, § 1), en plus de leurs cellules du collisionneur. R2-a comme R2-b ont donc des propositions en jeu. Le troisième relais en a moins, mais toutes les lignées en ont (ordre v4, § 7, point 1).
- **Ce qui limite la prise de l'auteur.** Après les corrections : familles et table imposées, vérité exacte, témoins imposés recalculés chez nous, au plus deux familles libres retenues seulement au scellement, famille tenue à l'écart. Ce sont les familles libres qui donnaient le plus de prise à une habitude de lignée ; les réduire est la parade la moins chère.
- **Repli sur R2-b.** Il demande un mot neuf, comme le rapport le dit.

## 8. Les décisions (point 6)

| décision | format | défaut | état après 07:57Z |
|---|---|---|---|
| D-M11 | au format | défaut à 48 heures sur un écart à un texte scellé : à éviter (§ 5) | décidée : `portee_de_la_garantie`, champ de la v5 |
| D-M12 | au format | (a) | décidée : aucune valeur vraie servie ; le mandat le respecte |
| D-M13 | au format | (a) | décidée : « épisodes honnêtes échangeables », écrit dans la table (n° 9) |
| D-M14 | au format | (a) | décidée ; le mandat le respecte |
| D-M15 | l'option (b) n'a ni avantage ni inconvénient | (a) | c'est cette contre-lecture |
| D-L1 | au format | **aucun défaut, c'est une dépense** : juste | ouverte : à Lazar |
| D-L2 | l'option (a) n'a pas d'avantage ni d'inconvénient propres | **aucun défaut** : juste | à mettre à jour : la mère recommande le premier relais pour l'expérimentateur (N4), non accordé |

Aucune décision ne porte de défaut pour une dépense.

## 9. Le programme de vérification (point 7)

- **Est-il dit ?** Oui. Le rapport (§ 3) le dit « à écrire, en session, avec ses essais sur cas sain et artefact (règle R5) », et le devis (§ 4, point 2) le compte à zéro dollar d'appels.
- **Est-il compté au calendrier ? Non.** Ni le rapport ni le § 10 de la v5 ne lui donnent une ligne.
- **Il doit précéder l'envoi, pour deux raisons.**
  - Ses points 1 et 2 (forme, complétude) décident si une sortie est « illisible », donc si un second essai payé part. Sans programme, cette décision serait prise à la main.
  - Le calcul des dix-sept témoins imposés doit être scellé avant la lecture de la sortie (règles R1 et R4) : c'est la phrase corrigée par le remplacement n° 4.
- **À ajouter au calendrier** : une session, avant l'envoi, pour le programme de vérification, points 1 à 3 et 5, avec les essais R5, et pour le programme scellé de vérité des témoins imposés, paramétré par la loi que l'auteur écrira. Le point 4, le recalcul de toutes les valeurs, peut suivre l'envoi, mais doit précéder la lecture.

## 10. Corrections, par pièce

| pièce | correction |
|---|---|
| mandat de l'auteur | les 22 remplacements du § 3, portés tels quels ; nom neuf v2 ; contre-lecture du différentiel |
| devis | M1 = 26 582 octets ; premier essai de R2-a à 32 000 ; phrase d'exception à `4286bf39…` dans la ligne de GO ; programme v2 rejoué deux fois |
| rapport | D-M11 à D-M15 closes par les mots de 07:56Z et 07:57Z ; D-L2 mise à jour pour N4 ; une ligne de calendrier pour le programme de vérification et la vérité des témoins (§ 9) ; § 2, point 2 : « tranché, échangeables » |
| ordre v5 | aucune, pour ce mandat |

## 11. Remarques, sans correction

1. La règle « quatre décimales au moins » ne se vérifie que sur le texte brut.
2. Pour T09 à T11, notre valeur se calcule sous la loi que l'auteur choisit. Les chiffres de la note ne servent de repère que si cette loi est normale.
3. La borne de 40 000 caractères reste serrée : 28 témoins et une douzaine de familles. Le retrait d'une famille libre et de deux lignes d'orientation libère de la place ; les témoins du monde M en reprennent un peu.
4. Le mandat cite trois pièces internes par titre et empreinte. Rien de personnel, aucun nom ; c'est acceptable.

contre-lecteur du mandat des mondes plantés, modèle O
