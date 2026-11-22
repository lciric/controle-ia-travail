# Part de la clé Luc recalculée pour un solde réel de 153 USD — v2

Pièce de travail (classe C), auteur Opus (celui de la v1), 2026-11-22. Processeur seul.

- **Version.** La v2 remplace la v1 (`recalcul-part-luc-153-v1.md`, `ccc8b2f981b07460…`, archivée sans changement), après la contre-lecture `B/noeuds-et-part-luc-v1/contre-lecture-v1/contre-lecture-noeuds-et-part-luc-v1.md` (`23e774f901624bb8…`, « À corriger »).
- **Programme.** `recalcul_part_luc_v2.py`, copie corrigée de la v1 (`03ffa38e…`). Sa sortie, `recalcul-part-luc-153-v2.json`, a été rejouée et est égale à l'octet (`cmp`). Code 0, onze contrôles tenus.
- **Notation.** Les clés de la sortie sont citées entre crochets. Les calculs sont faits en micro-dollars ; une part ou une marge s'affiche au centime inférieur, un manque au centime supérieur.

Abréviations : **B** = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/` ; **M** = `/home/user/main-lecture/` ; « complément » = `M/prereg/ideation-nouvelles-attaques-v1/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md` (`b4ef87dc…`) ; « additif au complément » = `…/additif-1-complement-…-espece-3-sur-minuit-v2.md` (`ce76e0d6…`) ; « V9 » = `…/preenregistrement-court-course-nouvelles-attaques-v9.md` (`864f39a7…`) ; « devis » = `…/devis-course-nouvelles-attaques-v11.md` (`205e08f2…`). Tous sont scellés.

## Verdict

**À 153 USD, la part fixée de 125,63 USD tient pour l'arrêt n° 11.** Il reste 27,37 USD au-dessus d'elle [`lecture_reserve_tombee_l113.arret_11_reste_moins_part_usd`], à deux conditions :
- l'étage 2 est clos, et son coût est dans les 153 ;
- aucun lot non clos sur Luc n'a un pire de plus de 27,37 USD.

**La lettre du complément, l. 116, se déclenche** : en dehors de l'étage 2, les dépenses s'élèvent à environ 27,62 USD, au-delà de la marge de 1,29 USD. Le manque, hors étage 2, est de **26,34 USD** ; le manque brut de 59,71 USD compte à tort l'étage 2 [`lecture_lettre_l116`]. C'est donc un nœud de Lazar.

**Aucun déplacement de rôle n'est possible sans recharge.**

**Recommandation : (a), garder la part**, avec le reste déclaré par Lazar et son mot sur la lecture de la l. 116. Confiance moyenne.

Le relèvement de la part, (e), est borné à **136,04 USD** par la ligne de course de 450 USD. Il ne couvre même pas une chaîne de repli d'un proposeur : je ne le recommande pas.

## 1. Ce que le complément exige

| règle | source |
|---|---|
| Part = reste relu moins le pire des lots non clos ; nœud si elle tombe sous le cas haut | R-4289, M/registres/decisions.md l. 4427 ; complément l. 111 |
| Réserve de l'étage 2 : 88,36 USD | R-4293, decisions.md l. 4431 ; complément l. 111 |
| « Une fois cet étage clos, la réserve tombe : son coût réel […] est retranché du reste s'il n'y est pas déjà » | complément l. 113 |
| Part 125,63 (213,999998 − 88,36, au centime inférieur) ; cas haut 124,35 ; marge écrite 1,29. Le calcul au centime inférieur donne 1,28 [`part_moins_haut_des_roles_usd`] : c'est une imprécision du texte scellé, sans effet | complément l. 35, l. 106, l. 115 |
| « un reste d'au moins 212,71 USD » (= 124,35 + 88,36) [`controles.minimum_egal_haut_plus_reserve`] | complément l. 106 |
| Nœud si la part tombe sous 124,35 ; « il suffirait […] que le reste de Luc passe sous 212,71 USD avant le départ, par une dépense **autre que celle de l'étage 2** » | complément l. 116 |
| « Une fois fixée, une part ne change plus » | V9 l. 235 |
| Arrêt n° 11 : reste « déclaré par Lazar pour Luc » ; la part n'est abaissée que par un complément neuf contre-lu ou le mot de Lazar | V9 l. 382 |
| Arrêt n° 12 : cumul, plus le pire des appels en vol, plus le pire de l'appel à lancer, au plus égal à la part | V9 l. 383 |
| Ligne Luc de la pièce de relevés : « reste calculé au registre des dépenses », réserve de l'étage 2, part 125,63 | additif au complément l. 141 |

## 2. Les faits, et ce qui manque

| fait | source |
|---|---|
| Étage 2 fini, 33,37 USD « comptés » (un compte, non un relevé) | decisions.md l. 4663 (R-4525) |
| « LUC 193 USD » | decisions.md l. 4734 (R-4595) |
| « Clé LUC : 39,59 USD dépensés, environ 153 restants » ; « 100 USD par clé » pour d'autres agents de « Raisons ou regard ? » | decisions.md l. 4786 (R-4647) |
| Aucune ligne de dépense sur Luc au registre de `main` après la l. 548 (la sonde, 0,000002 USD) | M/registres/depenses.md, l. 548 à 591 |

Ce que rien n'explique (contre-lecture, 4.2) :
- le passage de 214 à 193 (21 USD) ;
- l'écart entre 39,59 et 33,37 ;
- l'existence d'un lot ouvert de « Raisons ou regard ? » sur Luc, et son pire.

« Environ 153 » vient de l'état d'un autre projet, collé par Lazar. La pièce de relevés ne peut pas « calculer au registre » ce reste, comme le veut le libellé fixe de l'additif au complément l. 141, sans **une ligne de dépense neuve ou le mot de Lazar**. L'arrêt n° 11 veut de toute façon un reste déclaré par Lazar (V9 l. 382).

## 3. Ce qui tient à 153 USD

| lecture | calcul | issue |
|---|---|---|
| Lettre de la l. 116, coût de l'étage 2 exclu (hypothèse : les 153 le comprennent) | dépenses autres = 213,999998 − 153 − 33,37 = 27,62 [`depenses_autres_que_l_etage_2_…`] ; reste hors étage 2 = 186,37 ; manque **26,34** [`manque_hors_etage_2_usd`] | **se déclenche** : nœud de Lazar. Si les 153 ne comprennent pas l'étage 2, le manque est le brut, 59,71 |
| Réserve tombée (l. 113), aucun lot ouvert | 153 − 125,63 = **27,37** | l'arrêt n° 11 tient |
| Réserve tombée, lot ouvert de pire P | tient si P ≤ 27,37 ; la part tomberait sous le cas haut si P > 28,65 [`lot_ouvert_qui_ferait_tomber_la_part_sous_le_haut_usd`] | attend l'état des lots |
| Repli de GO-35, proposeur de l'espèce 4 (pire par tentative, décision iii) | chaîne de trois tentatives : 3 × 6,05 = **18,15** [`repli_GO_35`] ; la marge de 1,28 n'en contient aucune | un repli au cas haut peut lever l'arrêt n° 12 sur Luc |
| Repli de GO-35, aiguilleur | pire d'un appel non établi : il « attend la mesure » (complément l. 83 ; additif au complément l. 72) | **à mesurer** avant l'additif |

## 4. Les options

| option | effet chiffré | effet sur le devis | effet sur les textes scellés | coût, effort |
|---|---|---|---|---|
| **(a) Garder la part** ; la pièce de relevés écrit le reste déclaré, l'étage 2 clos (coût dans le reste), et aucun lot ouvert ou leur pire au plus égal à 27,37 | marge à l'arrêt n° 11 : 27,37 | aucun : 439,59 de parts sous la ligne de 450 | la l. 116 se déclenche à la lettre : il faut le **mot de Lazar** sur la lecture « la réserve tombée remplace le minimum de 212,71 », que la V9 l. 382 permet ; aucun nombre scellé ne change | un mot |
| (b) Réduire la part | libère au plus 1,28 [`option_reduire_la_part`] | — | complément neuf ou mot de Lazar ; sous 124,35, nœud | utile seulement si un lot ouvert dépasse 27,37 |
| (c1) Aiguilleur vers Minuit | Minuit 193,04 pour une part de 156,56 : manque 36,48 ; reste minimal 199,04 [`option_deplacer_un_role.aiguilleur`] | — | version neuve de la répartition (GO-2026-11-20-22, additif au complément) | impossible sans recharge ; le reste de Minuit est inconnu (GO-2026-11-21-28, go.md l. 627) |
| (c2) Espèce 4 vers Minuit | 194,63 pour 156,56 : manque 38,07 ; reste minimal 200,63 | — | idem | impossible sans recharge |
| (c3) Un rôle vers Rigaud | 16,65 disponibles déclarés : manque 44,73 ou 46,32 | — | Rigaud est hors course (R-4356) et dit sans crédit (depenses.md l. 577-578) | impossible |
| (d) Recharge de Luc | **26,34** au moins si les 153 comprennent l'étage 2 ; 59,71 sinon [`recharge_pour_tenir_la_lettre_usd`] | hors de la ligne ; aucun nombre du devis ne change | GO-2026-11-20-16 (go.md l. 547 : « sans recharge ») et GO-30 (« aucune recharge supposée ») : nœud de Lazar et dépense | 26,34 à 59,71 USD |
| (e) Relever la part | borne : **ligne de course** 450 − 439,59 = 10,41, soit une part au plus de **136,04** [`option_relever_la_part`] ; engagement total alors de 456,00 ; marge au cas haut 11,69 ; **un** pire d'appel entier ; aucune chaîne de 18,15 ; tolérance aux lots ouverts ramenée de 27,37 à **16,96** ; il ne reste plus rien sous la ligne pour le deuxième relais, dont le pire peut monter sous la règle Google | toute la marge sous la ligne va à Luc | version neuve de la part (V9 l. 235, l. 382) ; la l. 146 de l'additif au complément (« sous le plafond total de 456 ») est une note d'information et n'autorise pas ce relèvement | un mot et une contre-lecture |

Pourquoi la borne est 450 et non 456 (contre-lecture, 3.2). Les quatre parts sont des parts de course. La part de Minuit exclut déjà les 6 USD des lignes à part (complément l. 132). Le plafond total, 456, est la ligne de course plus les lignes à part : 450 + 5 + 1 (devis l. 380 et 386) [`controles.plafond_total_egal_ligne_plus_lignes_a_part`]. À 142,04, la valeur de la v1, la course engagerait 456 sur une ligne de 450, et 462 avec les lignes à part.

## 5. Recommandation

**(a), confiance moyenne.** Trois choses à demander à Lazar, pour la pièce de relevés :
1. le reste de Luc déclaré, daté, ou une ligne de dépense qui l'explique ;
2. le constat « l'étage 2 est clos et son coût est dans ce reste » ;
3. l'état et le pire des lots de « Raisons ou regard ? » sur Luc, et son mot sur la lecture de la l. 116.

Si un lot ouvert dépasse 27,37 USD, il reste (d) ou une version neuve de la répartition.

**(e) n'est pas recommandé.** Il ne couvre aucune chaîne de repli, il réduit la tolérance aux lots ouverts et il prend toute la marge sous la ligne. Le risque de repli sur Luc se tient mieux par l'arrêt n° 12, tel quel, et par sa déclaration au devis final (ligne « replis », nœuds v2, R14). L'arrêt de la course sur Luc est alors une issue écrite, non une surprise.

## Différence avec la v1

| point de la contre-lecture | v1 | v2 |
|---|---|---|
| 3.2 | (e) bornée par 456 : 142,04 USD, deux pires d'appel | bornée par la ligne de 450 : **136,04 USD**, un pire d'appel ; engagement total 456,00 ; contrôle `part_maximale_egale_136_04` |
| 3.3 | tolérance aux lots ouverts non recalculée sous (e) | 16,96 à 136,04 |
| 3.5 | effet sur le deuxième relais absent | dit : il ne reste plus rien sous la ligne |
| 4.1 | manque de la lettre 59,71, étage 2 compris | manque hors étage 2 : **26,34** (59,71 seulement si les 153 n'incluent pas l'étage 2) ; recharge de (d) : 26,34 à 59,71 |
| 4.2 | « environ 153 » signalé | il faut une ligne de dépense ou le mot de Lazar ; les trous 214 → 193 et 39,59 contre 33,37 sont dits |
| 2.5 | chaîne de 18,15 « sur l'aiguilleur ou l'espèce 4 » | proposeur de l'espèce 4 seul ; aiguilleur à mesurer |
| 3.4 | repères de 3,38 et 2,03 | dits valables à la génération 1 seulement, jamais des pires |
| 1.5 | 1,28 contre 1,29 | gardé, dit imprécision du texte scellé sans effet |
| recommandation | (a), puis (e) avec une confiance faible | (a) ; (e) déconseillée |
| programme | v1, centièmes, borne 456 | v2, micro-dollars, borne 450, onze contrôles |

— auteur Opus, 2026-11-22
