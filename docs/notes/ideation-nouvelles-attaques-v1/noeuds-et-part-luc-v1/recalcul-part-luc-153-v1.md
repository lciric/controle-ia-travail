# Part de la clé Luc recalculée pour un solde réel de 153 USD — v1

Pièce de travail (classe C), auteur Opus, 2026-11-22. Processeur seul. Tous les nombres calculés sortent de `recalcul_part_luc_v1.py` (même dossier). Sa sortie `recalcul-part-luc-153-v1.json` a été rejouée et est égale à l'octet par `cmp` (code 0, `tous_les_controles_tenus` : vrai). La clé JSON est donnée entre crochets. Abréviations : **M** = `/home/user/main-lecture/` ; **P** = `M/prereg/ideation-nouvelles-attaques-v1/` ; « complément » = P/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md (`b4ef87dc…`, scellé) ; « additif au complément » = P/additif-1-complement-…-espece-3-sur-minuit-v2.md (`ce76e0d6…`, scellé) ; « V9 » = P/preenregistrement-court-course-nouvelles-attaques-v9.md (`864f39a7…`, scellé) ; « devis » = P/devis-course-nouvelles-attaques-v11.md (`205e08f2…`, scellé).

## Verdict

**À 153 USD, la part fixée de 125,63 USD tient pour l'arrêt n° 11**, avec 27,37 USD au-dessus d'elle [`lecture_reserve_tombee_l113.arret_11_reste_moins_part_usd`], à deux conditions :
1. l'étage 2 est clos et son coût est déjà dans les 153 USD ;
2. aucun autre lot non clos n'a sur Luc un pire de plus de 27,37 USD.

**La lettre du complément, l. 116, ne tient pas** : le reste minimal de 212,71 USD manque de 59,71 USD [`lecture_lettre_l116.manque_usd`]. Cette lettre déclare alors un nœud de Lazar. **Aucun déplacement de rôle n'est possible** sans recharge. **Je recommande de garder la part (option a) et de faire constater le reste par Lazar.** Confiance moyenne. Le risque réel est ailleurs : la marge de la part au-dessus du cas haut n'est que de 1,28 USD, et aucune chaîne de repli de GO-35 n'y tient.

## 1. Ce que le complément exige (la règle, à la lettre)

| règle | source |
|---|---|
| Part de Luc = reste relu moins le pire des lots non clos sur la clé ; nœud si elle tombe sous le cas haut | R-4289, M/registres/decisions.md l. 4427, cité au complément l. 111 |
| La réserve est le plafond de l'étage 2, 88,36 USD | R-4293, decisions.md l. 4431 ; complément l. 111 |
| « Tant que l'étage 2 de la ligne 3 n'a pas couru, la réserve est de 88,36 USD. **Une fois cet étage clos, la réserve tombe** : son coût réel, inscrit au registre des dépenses, est retranché du reste s'il n'y est pas déjà. » | complément l. 113 |
| Part fixée : 213,999998 − 88,36 = 125,63 USD (centime inférieur) ; cas haut des rôles 124,35 ; marge 1,29 USD [le programme rend 1,28 : 125,63 − 124,35] | complément l. 35, l. 115 |
| « une part d'au moins 124,35 USD, soit **un reste d'au moins 212,71 USD** » | complément l. 106 |
| « Si la part tombait sous 124,35 USD […] nœud de Lazar, sans repli silencieux. **Il suffirait pour cela que le reste de Luc passe sous 212,71 USD avant le départ, par une dépense autre que celle de l'étage 2** » | complément l. 116 |
| « Une fois fixée, une part ne change plus. Un reste du jour plus bas que sa part refuse le départ (arrêt n° 11) » | V9 l. 235 |
| Arrêt n° 11 : reste du jour « **déclaré par Lazar pour Luc** » ; « la part n'est jamais abaissée en silence : il faut un complément neuf, contre-lu, ou le mot de Lazar » | V9 l. 382 |
| Arrêt n° 12 : cumul + en vol + pire de l'appel ≤ part ; aucune bascule | V9 l. 383 |
| Ligne Luc de la pièce de relevés : reste, date, source, **réserve de l'étage 2 : [RÉSERVE]**, part 125,63 | additif au complément l. 141 |

Remarque : 212,71 USD est exactement le cas haut plus la réserve (124,35 + 88,36) [`controles.minimum_egal_haut_plus_reserve`]. Ce minimum n'a de sens que tant que la réserve tient.

## 2. Les faits sur Luc

| fait | source |
|---|---|
| Étage 2 fini à 10:18Z, 1 005 envois, 33,37 USD comptés | decisions.md l. 4663 (R-4525) |
| « LUC 193 USD » (mot relayé aux filles, 2026-11-21 vers 16:00Z) | decisions.md l. 4734 (R-4595) |
| « Clé LUC : 39,59 USD dépensés, environ 153 restants » (état de « Raisons ou regard ? » collé par Lazar, vers 18:00Z ; « autres agents […] 100 USD par clé ») | decisions.md l. 4786 (R-4647) |
| 193 − 39,59 = 153,41 : cohérent avec « environ 153 » [`controles.193_moins_39_59_arrondi_egal_153`] | calcul |
| Aucune ligne de dépense de l'étage 2 ni de « Raisons ou regard ? » sur Luc au registre des dépenses après la l. 548 (sonde, 0,000002 USD) | M/registres/depenses.md (lu par recherche, l. 548 à 591) |

Ce que je ne sais pas, et que je n'invente pas :
- si les 153 USD comprennent tout le coût de l'étage 2 (le passage de 214 à 193 n'est expliqué par aucune ligne lue) ;
- si « Raisons ou regard ? » a un lot **non clos** sur Luc, et lequel est son pire (« 100 USD par clé » est un mot de plafond, sans dire de quelle clé) ;
- si 153 est un relevé ou une estimation (« environ »). L'arrêt n° 11 veut un reste **déclaré par Lazar** (V9 l. 382).

## 3. Ce qui tient et ce qui ne tient pas à 153 USD

| lecture | calcul | issue |
|---|---|---|
| Lettre de la l. 116 (reste ≥ 212,71) | 212,71 − 153 = **59,71** de manque [`lecture_lettre_l116`] | **ne tient pas** : nœud de Lazar par la lettre |
| Règle de R-4289 avec la réserve tombée (l. 113), aucun lot ouvert | part recalculable à 153 ; part fixée 125,63 ≤ 153 | arrêt n° 11 **tient**, marge 27,37 |
| Même règle, avec un lot ouvert sur Luc de pire P | tient si P ≤ 27,37 [`pire_maximal_des_lots_non_clos_tolere_usd`] ; si P > 28,65, la part tombe sous le cas haut [`lot_ouvert_qui_ferait_tomber_la_part_sous_le_haut_usd`] | **attend l'état des lots de « Raisons ou regard ? »** |
| Part face au cas haut de ses rôles | 125,63 − 124,35 = **1,28** [`part_moins_haut_des_roles_usd`] | tient, inchangé |
| Repli de GO-35 sur l'aiguilleur ou l'espèce 4 | une chaîne au pire = 3 × 6,05 = **18,15** [`repli_GO_35`] ; 0 pire d'appel entier dans la marge de 1,28 | **ne tient pas au cas haut** : un seul repli au cas haut peut lever l'arrêt n° 12 sur Luc et arrêter la course (V9 l. 383, sans bascule) |

## 4. Les options

| option | ce qu'elle fait | effet sur le devis | effet sur les textes scellés | coût, effort |
|---|---|---|---|---|
| **(a) Garder la part, lire la réserve tombée** | La pièce de relevés écrit : reste déclaré par Lazar (≈ 153), réserve « étage 2 clos, coût réel dans le reste » (l. 113), aucun lot ouvert, ou leur pire ≤ 27,37 ; part 125,63 | aucun : somme des parts 439,59 sous 456 (additif au complément l. 146) | la l. 116 du complément, à la lettre, déclare un nœud : il faut le **mot de Lazar** sur la lecture « la réserve tombée remplace le minimum de 212,71 », inscrit à la pièce de relevés (V9 l. 382 le permet : « ou le mot de Lazar ») ; aucun nombre scellé ne change | aucune dépense ; un mot |
| (b) Réduire la part | Part entre 124,35 et 125,63 | libère au plus 1,28 [`option_reduire_la_part`] : sans intérêt | complément neuf ou mot de Lazar (V9 l. 382) ; sous 124,35 : nœud et répartition à refaire | ne sert que si un lot ouvert dépasse 27,37 |
| (c1) Déplacer l'aiguilleur vers Minuit | Minuit porterait 193,04 de cas haut pour une part de 156,56 | manque 36,48 ; il faudrait un reste de Minuit d'au moins 199,04 avant les lignes à part [`option_deplacer_un_role.aiguilleur`] | écart à GO-2026-11-20-22 et à l'additif au complément (version neuve) | **impossible sans recharge** ; le reste du jour de Minuit est de plus inconnu, diminué par GO-2026-11-21-28 (go.md l. 627) |
| (c2) Déplacer le proposeur de l'espèce 4 vers Minuit | 194,63 pour 156,56 | manque 38,07 ; reste minimal 200,63 | idem | impossible sans recharge |
| (c3) Déplacer un rôle vers Rigaud | 16,65 disponibles déclarés (additif au complément l. 82) | manque 44,73 (aiguilleur) ou 46,32 (espèce 4) ; Rigaud a été dit « sans crédit » le 21 novembre (depenses.md l. 577-578) | idem, et Rigaud est « hors course » (R-4356) | impossible |
| (d) Recharge de Luc par Lazar | Recharge d'au moins **59,71 USD** : la lettre de la l. 116 tient sans lecture | aucun nombre du devis ne change ; c'est une dépense hors de la ligne | GO-2026-11-20-16 (go.md l. 547 : « sans recharge ») et GO-30 (« aucune recharge supposée ») : **nœud de Lazar** (dépense et écart) | 59,71 USD au moins |
| (e) Relever la part pour absorber le repli | Part portée à 142,04 au plus : la somme des parts reste sous 456 (marge 16,41) [`option_relever_la_part`] | marge au cas haut 17,69, soit 2 pires d'appel entiers ; la ligne de 450 reste la borne | version neuve de la part (V9 l. 235 « ne change plus » ; l. 382 : complément neuf, contre-lu, ou mot de Lazar) | aucune dépense ; un mot et une contre-lecture |

## 5. Recommandation

**(a), confiance moyenne.** Elle ne change aucun nombre scellé. Elle demande à Lazar trois choses courtes, au retour, pour la pièce de relevés :
1. le reste de Luc déclaré, daté ;
2. « l'étage 2 est clos et son coût est dans ce reste » ;
3. l'état et le pire des lots de « Raisons ou regard ? » sur Luc, et son mot sur la lecture de la l. 116.

Si un lot ouvert dépasse 27,37 USD, (a) ne tient plus. Il reste alors (d), ou une version neuve de la répartition.

**À poser en même temps, et séparément : (e).** Sous la règle de repli, la marge de 1,28 USD fait de Luc la clé la plus exposée à un arrêt n° 12 en course, en particulier sur l'aiguilleur, qui lit chaque fiche. Relever la part à 142,04 USD (somme des parts sous 456) n'ajoute aucune dépense accordée et donne deux pires d'appel de marge. C'est une version neuve de la part, donc un mot de Lazar. Je la recommande avec une confiance faible, faute de mesure du taux de refus des rôles de Luc.

— auteur Opus, 2026-11-22
