# Vérification du brouillon 5 de l'additif et du devis de la voie (A) — cl2

Date : 2026-11-22. Classe A. Contre-lecteur : Claude Opus 5.5, même rôle qu'aux brouillons 3 et 4. Je n'ai écrit aucune pièce. Rien dépensé, rien poussé, aucune pièce interdite ouverte, aucune variable d'environnement affichée, aucun arbre de travail créé.

## Verdict

**Scellable une fois les champs remplis.**

Les quatre décisions de la mère sont portées exactement, ainsi que les deux majeurs et les deux mineurs de la vérification du brouillon 4. Le rejeu du calcul v5 est identique à l'octet. Seules [M29], [M30] et [M32] changent. Aucune régression. Les trois champs restants sont les seuls attendus.

Le rédacteur a vu juste : le chiffre de 59,30 USD ne vaut plus au seuil de 80 minutes (c'était mon chiffre, calculé au seuil de 10 minutes). Le chiffre neuf, 60,91 USD à 48 heures, est exact. Il est écrit comme réserve pour Lazar. Je propose ci-dessous (C) une borne horaire du nœud. Le devis, § 8, la porte déjà comme recommandation. L'inscrire dans l'additif avant le scellement est souhaitable mais non bloquant.

## Pièces

Branche `origin/claude/iib-executante-v5-fable-additif-c`, commit `88a82af3c92c20e1978eb3963cd4c5761a2ae120`. Toutes les empreintes sont conformes à leurs compagnons :

| pièce | empreinte |
|---|---|
| additif, brouillon 5 | `e7d9189ce58853c2…` |
| devis, brouillon 5 | `356f53aebfa770e5…` |
| différences entre les brouillons 4 et 5 | `3ef51714e4725d9e…` |
| programme de calcul v5 | `9e4bb97e61b40ea8…` |
| sortie du calcul v5 | `ec46db500d9fdf0b…` |

Pièces citées, vérifiées sur `origin/claude/iib-executante-v6` :
- le mandat : `c25267a7…` ;
- ma note sur le brouillon 4 : `b5e73a07…`.

## A. Points portés

| point | où | état |
|---|---|---|
| Seuil du deuxième rempart à l'échéance plus 80 minutes | A3 (2 400 + 1 800 + 600 = 4 800 secondes ; « avant lui, arrêter couperait la consignation ») ; code 0 avant le seuil, même si la machine tourne ; « la minuterie a fait défaut » n'est dit qu'au seuil ; § 4.4, § 5 ; devis § 4 et § 6 ; programme : `DELAI_REMPART_S` = 4 800 | porté |
| Pire 57,23 USD ; création au plus tard le 24 novembre à 14:30Z | A3, § 7 points 8 et 10 ; devis § 4, § 7 point 11 ; [M29](b), [M32] ; 12 600 secondes, au lieu de 8 400, partout | porté |
| Rapatriement non vérifié à deux heures : machine gardée à l'arrêt, disque gardé, nœud à Lazar, aucune destruction | code 6 retiré ; nouveau code 7, un numéro neuf, pour qu'un ancien « 6 » ne se lise pas « détruire » ; « cette règle n'ordonne jamais une destruction » ; A2 : l'exception « sauf par le second rempart » est retirée, et le mot donné d'avance ne couvre aucun écart ; § 4.4 étape 7, § 5, § 7 point 3 ; devis § 4, § 5, § 8 | porté |
| Huitième cas de garde (instant d'arrêt placé dans le futur) | la condition du code 2 gagne `arret_s > maintenant_s` ; [M30] : 8 cas ; « huit cas » partout | porté |
| Troisième rempart tenu par la mère | A3 : dès la création, dans son conteneur, sur la même échéance absolue (le sixième argument de `creation`), compté dans aucun pire ; devis § 4 | porté |
| Mineur m2 (suites du seuil) | même geste dans tous les lieux nommés par ma note | porté |

**Aucune régression.**
- Il ne reste aucune trace de « code 6 » sinon pour dire qu'il est retiré. « 10 minutes » n'est employé que comme marge ou comme rappel du brouillon 4. « 8 400 », « 15:40Z », « 55,62 » et « sept cas » sont absents des deux textes.
- Le reste du texte est inchangé par rapport au brouillon 4 (vérifié par différence mot à mot). Il ne change que les en-têtes, les commandes en v5, la ligne du registre relue à `e50edee2…` et le § 6.
- La vérification des gardes du lanceur n'est pas rejouée. C'est justifié : rien de ce qu'elle calcule ne dépend du deuxième rempart, comme le mandat le permettait. La note des différences le dit, point 23.
- Les champs restants sont trois, chacun à deux occurrences, et seulement dans l'additif : `<<ENTROPIE_VOIE_A>>`, `<<EMPREINTE_CONFIG_VOIE_A>>`, `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>`. Le devis n'en a aucun.

## B. Rejeu du calcul v5

- `python3 -I calcul-devis-voie-A-v5.py`, avec le Python de l'environnement virtuel et avec celui du système : code 0, **identique à l'octet** (`ec46db50…`).
- Différence avec la sortie v4 : seules les lignes [M29], [M30] et [M32] changent ; les 25 autres sont égales.
- [M30], rejoué par la sous-commande, un cas après l'autre : **0, 4, 0, 0, 5, 7, 2, 2**, conforme.
- Hors liste, rejoué aussi :

| cas | code |
|---|---|
| machine qui tourne à l'échéance plus 2 400 secondes | 0 (le défaut M1 est clos) |
| machine qui tourne après le seuil | 4 |
| arrêt daté d'avant le seuil | 2 |
| instant non entier | 2 |
| 1 h 59 après l'arrêt | 5 |

- [M29](b) : 55 + 5 400 s × 1,38 / 3 600 + 2 × 0,08 = 57,23. [M32] : 30 h + 12 600 s = 33,50 h ; 1795651200 − 120600 = 1795530600 = 2026-11-24T14:30:00Z. Exact.

## C. La réserve neuve : 60,91 USD à 48 heures

**Le chiffre est exact.**
- À l'arrêt : 55 + (4 800 + 600) s × 1,38 / 3 600 = 57,07 USD.
- Plus 48 × 0,08 = 3,84 : **60,91 USD**.
- (59,76 − 57,07) / 0,08 = 33,6 heures ; (60 − 57,07) / 0,08 = 36,6 heures.

**Il est bien écrit comme réserve pour Lazar** :
- additif, A3, « ce qui n'est pas tenu », réserve un ; § 7, point 9, titré « réserve nommée de plus, pour Lazar » ;
- devis, § 0, § 4 (ligne propre), § 7 point 9 et § 8 ;
- la phrase « aucun code ne tient cette durée : elle dépend de la réponse au nœud » est juste ;
- les deux faits portés au nœud sont exacts et utiles : aucune commande scellée ne lit le disque d'une machine à l'arrêt ; un redémarrage pousse puis détruit.

**Règle la plus étroite que je propose.** Elle tient le total sous 60 USD sans destruction sans rapatriement vérifié. Sans réponse de Lazar, aucune règle ne peut garantir 60 USD sans détruire. La garantie repose donc sur une borne horaire de la réponse, écrite par avance :

> Code 7 : le nœud est porté à Lazar aussitôt, avec l'instant absolu « arrêt plus 33 heures » (total 59,71 USD, sous le pire annoncé de 59,76), calculé par programme et écrit en UTC. La mère tient le nœud quand la ligne de session de l'exécutante est échue. Relance à l'arrêt plus 24 heures. Le silence de Lazar n'est pas un accord de destruction. Sans réponse à l'arrêt plus 36 heures (59,95 USD), le passage du plafond est déclaré comme dépense hors devis, au prix de 0,08 USD par heure, et la machine reste à l'arrêt.

Cela ferait une phrase en A3 (code 7) et au § 7, point 9. Le programme pourrait rendre, à l'arrêt plus 33 heures, un code « borne du nœud » qui ne détruit rien. Faute de cela, le choix du devis, § 8 (« répondre au nœud dans les 33 heures »), suffit, puisque Lazar le lit au GO.

Fait daté : au plus tard le 26 novembre à 00:00Z, le code 7 d'une course créée le 24 à 14:30Z tombe exactement à la fin de la ligne de session de l'exécutante. La borne des 33 heures est alors tenue par la mère seule.

## D. Le point rendu à la mère sur le geste du troisième rempart

§ 7, point 12, et devis, § 4. **Juste et bien posé.** Le texte ne dit ni ce que fait le doublement, ni à quel instant. Les deux risques nommés sont réels :
- un geste dans les 70 minutes après l'échéance couperait la consignation (même défaut que le majeur M1 du brouillon 4) ;
- une destruction par ce doublement se ferait sans rapatriement vérifié.

Recommandation à la mère, à écrire dans son registre avant la création. Pas besoin de le mettre dans l'ordre scellé, puisque ce rempart n'est pas compté.
- Ne rien faire avant l'échéance plus 80 minutes.
- Ensuite, si la machine tourne et que l'exécutante est muette : arrêt par l'identifiant, jamais destruction. Puis le même chemin que les codes 5 et 7, avec la même règle `second-rempart`.
- Ainsi, si la session de l'exécutante meurt, la mère ramène la réserve de 64,76 USD (§ 7, point 8) au chemin de 57,07 USD plus le stockage.

Fichiers temporaires de cette vérification supprimés. Il ne reste que cette note.
