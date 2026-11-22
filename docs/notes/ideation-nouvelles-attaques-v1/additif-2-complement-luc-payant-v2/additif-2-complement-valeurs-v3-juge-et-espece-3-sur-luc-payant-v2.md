# Additif 2 au complément de valeurs v3 du préenregistrement court v9 — course « nouvelles attaques » — le juge et le proposeur de l'espèce 3 passent sur la clé Luc, lue en compte payant à recharge — v2

Additif court. Il se lit avec le complément de valeurs, lot 1, v3, scellé (« le complément v3 »), et avec son additif 1, v2, scellé (« l'additif 1 »). Il y renvoie pour tout ce qu'il ne change pas.

- **Auteur** : la session de l'organisme, branche `lot/compte-organisme-v1`. Elle n'a écrit ni le complément v3 ni l'additif 1.
- **Date** : 2026-11-22. Relevé de `date -u` au moment de l'écriture : 12:08:42Z.
- **Version** : la v2 remplace la v1 (`57d2276ee56af43b…`, archivée sans changement). Elle porte les neuf points de la contre-lecture `additif-2-complement-luc-payant-v1/contre-lecture-v1/contre-lecture-additif-2-luc-v1.md` (verdict « Conforme avec réserves ») et la suggestion R5 sur le programme. Relevé de `date -u` pour la v2 : 12:13:26Z.
- **Statut** : pièce de travail, non scellée. Elle part à la vérification du même contre-lecteur, puis au scellement par la mère.
- **Calcul** : processeur seul. Aucun appel à un fournisseur, aucune clé lue, aucune dépense.
- **Ce que ce texte ne contient pas** : aucune méthode d'attaque, aucun nom de mode, aucune case nommée, aucune valeur de clé.
- **Aucune valeur n'est inventée.** Chaque nombre calculé renvoie à une clé de `calcul-additif-2-luc-v2.json` (« J : … »). Ce que la lettre des accords ne fixe pas est marqué **« point pour la mère »**.

**Pièces citées.** Les pièces de `main` sont lues au commit `90f554580`, dans `/home/user/main-lecture`.

| pièce | chemin | empreinte |
|---|---|---|
| complément v3 (R-4307) | `prereg/ideation-nouvelles-attaques-v1/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md` | `b4ef87dc6d5cce13…` |
| additif 1, v2 (R-4356) | `prereg/ideation-nouvelles-attaques-v1/additif-1-complement-valeurs-preenregistrement-court-v9-lot-1-v3-espece-3-sur-minuit-v2.md` | `ce76e0d6a0a6e65f…` |
| préenregistrement court v9 | `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md` | `864f39a7ecd41a61…` |
| accords GO-2026-11-20-67 et GO-2026-11-22-42, -48, -49, -50 | `registres/go.md` | `358b32623539d11f…` |
| nœuds L-1 et L-2 | `docs/notes/ideation-nouvelles-attaques-v1/additif-vehicule-na-projet-v2/additif-vehicule-na-projet-v2.md`, l. 162-163, sur cette branche | compagnon `.sha256` |
| absence de crédit de Minuit | `docs/notes/ideation-nouvelles-attaques-v1/envoi-fable-additif-v1/`, erratum 1, sur cette branche | compagnon `.sha256` |
| consigne « prêt / manque » | message de la mère vers 12:00Z, repris dans `registres/essaim/vers-mere/2026-11-22-1201-organisme.md`, sur cette branche | compagnon `.sha256` |
| devis de la passe X, v2 (vérifié « À corriger ») | `docs/notes/ideation-nouvelles-attaques-v1/devis-passe-x-v2/devis-passe-x-v2.md`, sur cette branche | compagnon `.sha256` |
| programme et sa sortie | `calcul_additif_2_luc_v2.py` ; `calcul-additif-2-luc-v2.json`, dans ce dossier | `e9a85e70e9f174a9…` ; `95b40466f5e0c41d…` |

## 0. En bref

- **Luc** porte désormais quatre rôles de la course : l'aiguilleur, le proposeur de l'espèce 4, le juge de l'espèce 3 et le proposeur de l'espèce 3.
- **Luc est lu en compte payant à recharge automatique** (GO-48, GO-49). Sa part de la course est fixée à **260,00 USD**, le plafond de GO-49. Elle n'est plus un reste moins une réserve.
- Le cas haut des quatre rôles est de **256,01 USD** (J : `luc.haut_des_quatre_roles_usd`). La part le couvre, avec une **marge de 3,99 USD** (J : `luc.marge_part_moins_haut_usd`).
- **Cette marge est plus petite qu'un pire appel de proposeur, 6,05 USD** (J : contrôle `marge_sous_un_pire_appel_de_proposeur`). Au cas haut, l'arrêt n° 12 peut donc arrêter la course avant sa dernière chaîne. Sur Minuit, la marge était de 24,90 USD (additif 1, § 2). C'est le point n° 1 pour la mère.
- **Minuit ne porte plus aucun rôle de la course.** Tout appel de la course présenté sur Minuit est refusé (arrêt n° 12, seconde clause).
- **Les deux lignes à part** (au plus 6 USD) étaient payées par Minuit. Elles ne tiennent pas dans la part de 260 USD : 256,01 + 6 = 262,01 USD (J : `luc.haut_plus_lignes_a_part_usd`). C'est le point n° 2 pour la mère.

## 1. Les mots qui portent cet additif

- **GO-2026-11-22-49**, à la lettre : « Mot de Lazar reçu vers 2026-11-22T12:00:09Z : « go » sur « passer aussi sur la clé Luc les deux rôles de la course qui étaient sur Minuit » (recommandation de la mère : « go Luc pour tout, plafond 260 »). Le juge et l'espèce 3 de la course « nouvelles attaques » passent sur RR_ANTHROPIC_API_KEY_LUC, recharge automatique active ; part de Luc pour la course portée à 260 USD au plus. » Montant : 260 USD (part de Luc, course). Échéance : 2026-11-30.
- **GO-2026-11-22-48**, extrait : « Le mot de Lazar « laisse agir la recharge automatique » (GO-2026-11-22-42) fait lire la clé Luc en compte payant à recharge, en remplacement de « aucune recharge supposée » de GO-2026-11-22-30. »
- **GO-2026-11-22-50**, extrait : « clé d'Anthropic à la place de Minuit : « luc on a dit » ».
- **Lettre que ces mots changent.**
  - Préenregistrement v9, l. 235 : « Une fois fixée, une part ne change plus. »
  - Complément v3, § 3 : part de Luc fixée à 125,63 USD.
  - Additif 1, § 2 : juge et proposeur de l'espèce 3 sur Minuit.
  - Ces changements sont des écarts à des pièces scellées, portés par le mot de Lazar (§ 7).

## 2. La nouvelle répartition

| clé | rôles | cas bas | cas haut | part |
|---|---|---|---|---|
| **Luc** | aiguilleur ; proposeur de l'espèce 4 ; **juge de l'espèce 3** ; **proposeur de l'espèce 3** | 66,51 + 20,58 + 22,29 = **109,38** | 124,35 + 105,05 + 26,61 = **256,01** | **260,00 USD**, fixée (GO-49) |
| Minuit | aucun rôle de la course | — | — | aucune part de la course |
| deuxième relais | inchangé | — | — | 140,39 USD, inchangée |
| troisième relais | inchangé | — | — | 17,01 USD, inchangée |

**Sources des cas.** Ils sont chiffrés par rôle, et ne dépendent donc pas de la clé qui paie :
- aiguilleur et espèce 4 : complément v3, § 3 ;
- juge et proposeur de l'espèce 3 : additif 1, § 2.

**Ce que le programme montre** :
- la part dépasse le cas haut de 3,99 USD (J : `luc.marge_part_moins_haut_usd`), soit zéro pire appel entier (J : `luc.marge_en_pires_appels_entiers`) ;
- la part monte de 134,37 USD par rapport à 125,63 (J : `luc.hausse_de_la_part_usd`). Elle dépasse aussi l'ancienne borne de 136,04 de L-1 (J : contrôle `part_depasse_l_ancienne_borne_l1`) : cette borne est remplacée ;
- la somme des parts de la course passe de 439,59 à **417,40 USD** (J : `ensemble.somme_des_parts_apres_usd`). Elle reste sous la ligne de course de 450 USD, avec 32,60 USD de marge. Avec les lignes à part, elle fait 423,40 USD, sous le plafond total de 456 USD (J : contrôles `somme_des_parts_sous_la_ligne_de_course` et `somme_parts_et_lignes_sous_plafond_total`).

**La règle de part de Luc du complément v3 n'a plus d'objet** pour cette course : c'était le reste moins le pire des lots non clos (R-4289), avec une réserve de 88,36 USD pour l'étage 2. La part ne se lit plus sur un reste. La réserve de l'étage 2 n'est plus retranchée de la part de la course ; elle reste une ligne de Luc tenue par son propre accord. Les nœuds L-1 et L-2 tombent avec cette règle :
- L-1 (« part relevable à 136,04 au plus ») est remplacé par la part fixée de GO-49 ;
- L-2 (« si la part tombait sous 124,35 ») n'a plus d'objet, puisque la part est fixée au-dessus du cas haut.

## 3. L'arrêt n° 11 pour Luc, compte payant

La règle du complément v3 pour un compte payant (§ 4, points 1 à 5) s'applique à Luc, transposée comme pour le troisième relais (additif 1, § 4) :

1. le reste du jour de Luc vaut au moins sa part, 260,00 USD, **tant que le compte est attesté en recharge automatique et que GO-49 tient** ;
2. au départ, l'arrêt vérifie **un relevé daté, écrit par la mère, qui dit que la recharge automatique de Luc est encore active**. Il attend ce relevé, au jour du départ ;
3. si la recharge n'est plus active, ou si le relevé manque, **l'arrêt refuse le départ**, avec son nom. Aucun repli silencieux ;
4. épreuve (R5) : cas sain, recharge attestée et part de 260,00 : départ. Artefacts, refus nommé dans chacun des trois cas :
   - relevé absent ;
   - recharge dite inactive ;
   - relevé sans date.
   Un contrôle à part, au scellement de la pièce de relevés et non à l'arrêt n° 11, vérifie que la part écrite égale 260,00, le plafond de GO-49.

**La garde de départ « prêt / manque »** (consigne de la mère de 12:00Z, à écrire à part) précède cet arrêt. Elle ne le remplace pas : un « prêt » sur Luc dit que la clé répond et a du crédit, pas que la recharge est active.

## 4. L'arrêt n° 12 pour Luc et pour Minuit

- **Luc.** La lettre ne change pas : les quatre rôles sont comptés sur Luc, contre 260,00 USD. Le pire d'un appel de proposeur est de 6,05 USD. Celui du juge et de l'aiguilleur **attend toujours la mesure** (complément v3, § 2, ligne 4) : il peut dépasser 6,05 USD et amincir encore la marge (point n° 1).
- **Minuit.** Minuit n'a plus de rôle dans la course. La première clause n'a plus d'objet. La seconde clause s'applique : tout appel de la course présenté sur Minuit est refusé, avec l'arrêt nommé, sans bascule.
- **Épreuve (R5).**
  - Cas sain : un appel du juge de l'espèce 3 sur Luc, sous la part, part et se compte sur Luc.
  - Artefacts, chacun refusé avec l'arrêt nommé :
    - le même appel présenté sur Minuit ;
    - un appel qui dépasserait 260,00 d'un centime.
- **Ce que la marge mince implique.** Au cas haut, après 254 USD dépensés, un appel de proposeur au pire de 6,05 USD dépasserait la part. L'arrêt refuserait alors l'appel, et la course s'arrêterait par son nom avant sa fin. C'est sûr, puisqu'il n'y a aucune bascule. Mais c'est un arrêt probable si le coût réel approche le cas haut (point n° 1).

## 5. Les deux lignes à part

- **Avant.** Au complément v3 et à l'additif 1, les rôles Claude des deux lignes se payaient sur **Minuit** :
  - l'épreuve des témoins : portier et juge de l'espèce 3 ;
  - la sonde de refus : proposeurs des espèces 3 et 4.
  Leurs plafonds entiers (5 + 1 USD) étaient retranchés de la part de Minuit.
- **Le mot de GO-49** ne nomme que « les deux rôles de la course qui étaient sur Minuit ». Il ne dit rien des lignes à part. Or Minuit est sans crédit : son envoi à Fable est suspendu pour cette raison.
- **Lecture proposée, à trancher** (point n° 2) : les rôles Claude des deux lignes passent aussi sur Luc, **en lignes à part, hors de la part de course de 260 USD**. Ces lignes sont des appels faits avant la course, et elles étaient déjà retranchées hors de la part sur Minuit. Elles tiennent sous le plafond total : 417,40 + 6 = 423,40 ≤ 456.
- **L'autre lecture** les compterait dans les 260 : il manquerait alors 2,01 USD (J : `luc.manque_si_lignes_dans_la_part_usd`), et la répartition ne tiendrait pas.

## 6. La ligne de Luc et la ligne de Minuit dans la pièce de relevés

| clé | libellé fixe de la ligne | à relever au jour du départ |
|---|---|---|
| Luc | « Luc — compte payant à recharge automatique ; statut : [STATUT : recharge active, ou inactive], le [DATE] ; source : [SOURCE] ; part : 260,00 USD (GO-2026-11-22-49) ; rôles : aiguilleur, proposeur de l'espèce 4, juge de l'espèce 3, proposeur de l'espèce 3 ; lignes à part : [selon le point n° 2] ; lue par l'arrêt n° 11 (compte payant) et l'arrêt n° 12. » | le statut de la recharge, daté |
| Minuit | « Minuit — aucun rôle de la course ; aucune part ; tout appel de la course présenté sur cette clé est refusé (arrêt n° 12, seconde clause). » | rien |

Le libellé « reste calculé au registre des dépenses » de la ligne Luc (additif 1, § 6) tombe.

## 7. Écart déclaré, et ce que l'additif ne change pas

**Écart déclaré**, sur le mot de Lazar GO-2026-11-22-49, avec GO-48 et GO-50 :
- la répartition de l'additif 1 : le juge et le proposeur de l'espèce 3 passent de Minuit à Luc ;
- la part fixée de Luc (préenregistrement v9, l. 235 ; complément v3, § 3) : 125,63 devient 260,00 ;
- la lecture de Luc par l'arrêt n° 11 : « déclaré par Lazar » (v9, l. 382) devient « compte payant attesté » ;
- la part de Minuit, 156,56 : elle n'a plus d'objet.

**Ce qui ne change pas** :
- la lettre des arrêts n° 11 (hors sa lecture pour Luc, § 3), n° 12 étendu et n° 27 ;
- la ligne de course de 450 USD, le plafond total de 456 USD, les cas du devis v11 ;
- les parts des deuxième et troisième relais ;
- la sous-part de la passe X sur Luc (72,60 USD au pire, devis de la passe X v2), qui reste comptée **contre la passe X, non contre la part de la course** ;
- les conditions de départ de GO-2026-11-20-67 : cet additif scellé, la pièce de relevés scellée, l'épreuve des témoins et la sonde de refus passées. L'allumage reste un nœud à part.

## 8. Points pour la mère

1. **Marge de 3,99 USD sur Luc, sous un pire appel de proposeur.** Au cas haut, la course peut s'arrêter par l'arrêt n° 12 avant sa fin. Options :
   - (a) garder 260, accepter l'arrêt possible et le dire à Lazar ;
   - (b) demander à Lazar une part plus haute. 280 USD rendraient environ 24 USD de marge, comme sur Minuit avant.
   Ma recommandation est (a), confiance 0,6 : 260 est le mot de Lazar, et l'arrêt est sûr. (b) se demande seulement si Lazar veut la course entière au cas haut. À 280, la marge serait de 23,99 USD (J : `luc.marge_si_part_280_usd`).
   La marge peut être plus mince encore : le pire d'un appel du juge et de l'aiguilleur attend la mesure (§ 4).
2. **Les lignes à part** : sur Luc, hors de la part de 260 (ma recommandation, confiance 0,7), ou dans la part (manque 2,01 USD, la répartition ne tient pas) ?
3. **GO-2026-11-20-67 échoit le 2026-11-22**, aujourd'hui (`go.md` l. 598). Le départ de la course demande une ligne de GO neuve, sur le mot de Lazar. GO-67 porte aussi « aucune recharge supposée » ; GO-48 ne remplace cette formule que dans GO-2026-11-22-30. **La ligne neuve doit donc la remplacer pour Luc**, sinon la lecture de Luc en compte payant heurte la lettre du départ.
4. **L'engagement total de Luc au pire** est d'environ **467,60 USD**, soit 314,60 au-delà des « environ 153 restants » (J : `engagement_luc_au_pire`). Ce reste n'est pas un relevé : c'est un mot rapporté (R-4647, cité par `noeuds-et-part-luc-v2/recalcul-part-luc-153-v2.md`, l. 46), à comparer aux 214 USD du complément v3. **Avec la réserve de 88,36 USD de l'étage 2, l'engagement monte à 555,96 USD, soit 402,96 au-delà de 153** (J : `total_avec_reserve_etage_2_usd`, `au_dela_du_reste_avec_etage_2_usd`). Il additionne :
   - la course (260) ;
   - les lignes à part (6) ;
   - la passe X (72,60) ;
   - Fable sous GO-45 (au moins 117) ;
   - l'attaquant informé de GO-50 (environ 12).
   - et, au plus, la réserve de l'étage 2 (88,36).
   Les demandes 28 à 30 ne sont pas chiffrées. Lazar doit le savoir avant le départ, avec le relevé « prêt / manque ».
5. **Ce que l'attestation de recharge doit dire** pour valoir « compte payant ». Pour le troisième relais, la mère a tranché au scellement de l'additif 1 (R-4356, cité à son § 9) : « l'attestation est le mot de Lazar du 2026-11-21 vers 05:55Z (R-4342), « recharge automatique », seuil, montant et plafond non relevés, la pièce de relevés le dit ». Je propose la même lecture pour Luc, avec une question de plus pour Lazar : **le plafond de recharge de Luc, s'il existe, couvre-t-il les 315 à 403 USD à payer au-delà du reste ?**
6. **La table des rôles et des clés du véhicule** (lots de la course) est à mettre à jour avant tout allumage : les quatre rôles sur Luc, et l'artefact « envoi adressé à Minuit », refusé par l'arrêt n° 12.

## 9. Vérification

- Programme : `calcul_additif_2_luc_v2.py`, centimes entiers, entrées en tête avec leur source. Joué deux fois ; sorties égales par `cmp`. `tous_les_controles_tenus` : vrai, sept contrôles.
- **Épreuve des contrôles (R5)** : chaque contrôle est rejoué sur une entrée altérée et doit tomber ; les sept tombent (J : `epreuve_artefacts`, `tous_les_artefacts_tombent` : vrai).
- Contre-lecture de la v1 : agent neuf, modèle S, verdict « Conforme avec réserves », neuf points portés ici. Vérification de la v2 : par le même contre-lecteur.
