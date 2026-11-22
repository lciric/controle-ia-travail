# Contre-lecture de l'additif 2 (Luc payant) — v1

**Verdict : Conforme avec réserves.** Aucun nombre faux, aucune citation inexacte. Une phrase à corriger (pire d'un appel de juge), un artefact d'épreuve sans source, deux points pour la mère à compléter, deux sources non vérifiables sur mes pièces.

Rejeu : `python3 -B calcul_additif_2_luc_v1.py` redirigé, `cmp` avec `calcul-additif-2-luc-v1.json` : IDENTIQUE. Empreintes recalculées : programme `727c9f44b9db76a1…`, JSON `6a171020585e9586…`, complément v3 `b4ef87dc…`, additif 1 `ce76e0d6…`, v9 `864f39a7…`, go.md `358b3262…` : toutes égales aux préfixes de la pièce (tableau l. 16-21).

## Ce qui est conforme
- Nombres : 124,35 ; 66,51 ; 105,05 ; 20,58 ; 26,61 ; 22,29 ; 125,63 ; 156,56 ; 140,39 ; 17,01 ; 6,05 ; 24,90 ; 450 ; 456 ; 6 égaux à leurs sources (v3 §0, §3, §4, §6, §9 ; additif 1 §2, §4). Dérivés (256,01 ; 109,38 ; 3,99 ; 134,37 ; 417,40 ; 439,59 ; 32,60 ; 423,40 ; 262,01 ; 2,01 ; 467,60 ; 314,60) égaux au JSON et recalculés à la main.
- Citations : GO-49 (go.md l. 736), GO-48 (l. 735), GO-50 (l. 737), v9 l. 235 et l. 382 (« déclaré par Lazar »), GO-67 l. 598 (échéance 2026-11-22) : exactes à la lettre.
- Transposition de l'arrêt n° 11 (payant) : points 1 à 4 suivent v3 §4 et additif 1 §4. Arrêt n° 12 : seconde clause pour Minuit, première sans objet, calquées sur le traitement de Rigaud (additif 1 §3).
- GO-48 et GO-49 : la pièce ne dit pas plus que leurs mots, sauf les points ci-dessous.

## Points trouvés

1. **§ 4, l. 81 : « celui du juge et de l'aiguilleur est celui que le complément v3 écrit ».** Faux : le v3 (§2, ligne 4) écrit que ce pire « attend la mesure ». Correction : « celui du juge et de l'aiguilleur attend la mesure (complément v3, § 2, ligne 4) ; il peut dépasser 6,05 USD, ce qui amincit encore la marge de 3,99 USD. » Ajouter cette phrase au point n° 1 du § 8.

2. **§ 3, l. 75 : artefact « part écrite à 260,01 ».** Absent des pièces 4 et 5 et du v9 (l. 382 : « reste d'un centime sous la part »). L'arrêt n° 11 compare un reste à une part ; il ne contrôle pas la part contre GO-49. Correction : retirer cette ligne, ou l'écrire comme contrôle à part : « contrôle de pièce : une part écrite au-dessus du plafond de GO-2026-11-22-49 (260,00 USD) refuse le scellement de la pièce de relevés ; point pour la mère ».

3. **§ 8, point 3 (échéance).** Ajouter : « GO-2026-11-22-48 remplace « aucune recharge supposée » de GO-2026-11-22-30 seulement ; GO-2026-11-20-67 porte la même formule. Le GO neuf de départ doit dire que, pour la clé Luc, « aucune recharge supposée » est remplacée. »

4. **§ 8, point 4 (engagement).** (a) Le chiffre 153 USD (J : `reste_luc_declare`, source « recalcul part Luc 153 v2 ») ne figure dans aucune pièce que j'ai lue, et le v3 écrit 214 USD déclarés, reste 213,999998 ; la pièce citée n'est pas au tableau des pièces. Écrire : « 153 USD : source non vérifiée par la contre-lecture ». (b) La réserve de 88,36 USD de l'étage 2, que le § 2 dit rester « une ligne de Luc », n'est pas dans l'engagement. Ajouter : « Non comptés : réserve de l'étage 2 (88,36 USD, si elle court) et les demandes 28 à 30 ; avec la réserve, 555,96 USD (467,60 + 88,36). » Ce dernier nombre est à ajouter au programme, pas à écrire à la main.

5. **§ 8, point 5 (attestation).** Le point dit « la même lecture » que R-4356 point 4. Cette lecture (additif 1 §9) est : l'attestation est le mot de Lazar, seuil, montant et plafond non relevés. Pour 17,01 USD c'est tenable ; pour Luc la recharge doit financer environ 315 USD. Correction : écrire la lecture de R-4356 mot pour mot et demander s'il faut, pour Luc seul, relever le plafond de recharge.

6. **Point manquant** : la confirmation de la répartition par la contre-lecture du véhicule (v3 §2 ligne 3 ; additif 1 §8 point 7). La table rôles-clés du véhicule change (Minuit sans rôle, quatre rôles sur Luc) ; ajouter un point n° 6 : « la table des rôles et des clés du véhicule, et son artefact « envoi adressé à Minuit », sont à mettre à jour avant tout allumage ».

7. **Non vérifiables sur mes pièces (à marquer ou sourcer)** : « Minuit est sans crédit, son envoi à Fable est suspendu » (§5) ; « consigne de la mère de 12:00Z » sur la garde « prêt / manque » (§3) ; « L-1 (« part relevable à 136,04 au plus ») » et « L-2 » cités entre guillemets (§2) : seul 136,04 est dans go.md (GO-42, l. 729) ; devis passe X v2 (72,60 ; 117), « additif véhicule v2 », absents du tableau des pièces. Ajouter ces pièces au tableau avec empreinte, ou retirer les guillemets.

8. **§ 7** : « la lettre des arrêts n° 11 … ne change pas » contredit le § 3 et l. 114 (lecture de Luc). Correction : « la lettre des arrêts n° 11 (hors sa lecture pour Luc, § 3), n° 12 étendu et n° 27 ».

9. **§ 8, point 1** : « 280 USD … environ 24 USD » n'est pas une clé du JSON (280 − 256,01 = 23,99). Ajouter la clé au programme ou écrire « 23,99 USD (calcul à la main, hors JSON) ».

## Programme
Pas de contrôle faux par construction ni de constante truquée : les sept contrôles se calculent sur les entrées. Réserves de forme : `somme_des_parts_avant_egale_439_59` compare à une constante écrite (43959), mais c'est un recoupement honnête avec additif 1 §6 ; `part_depasse_l_ancienne_borne_l1` compare deux entrées saisies, donc ne peut échouer qu'avec les entrées. Aucun contrôle n'est essayé sur un artefact (R5) : ajouter une passe qui altère une entrée (par ex. part à 255,00) et vérifie que `part_couvre_le_haut_des_quatre_roles` tombe.

## Points pour la mère (§ 8)
Réels et bien posés : 1 (marge), 2 (lignes à part), 3 (échéance) ; 4 et 5 à compléter comme ci-dessus ; manque : point 6 ci-dessus.
