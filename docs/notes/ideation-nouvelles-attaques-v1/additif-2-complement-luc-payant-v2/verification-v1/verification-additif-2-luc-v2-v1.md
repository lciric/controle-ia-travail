# Vérification de l'additif 2, v2

**Verdict : Conforme avec réserves.** Rejeu du programme v2 : `cmp` IDENTIQUE. Empreintes `e9a85e70e9f174a9…` et `95b40466f5e0c41d…` égales à celles du tableau. `diff` v1/v2 relu : aucune modification hors des neuf points et de la suggestion R5.

## Les neuf points
1. Pire d'un appel de juge : **porté** (§ 4 ; § 8 point 1).
2. Artefact « 260,01 » : **porté** (remplacé par « relevé sans date » ; contrôle de scellement à part).
3. Point 3 de la mère, « aucune recharge supposée » : **porté**.
4. Engagement : **porté**. 153 sourcé (decisions.md l. 4786, via recalcul-part-luc-153-v2.md l. 46, vérifiée : « environ 153 restants »), 555,96 et 402,96 sont au JSON (somme recalculée juste).
5. Attestation : **porté**. R-4356 cité fidèlement (additif 1 § 9) ; question du plafond posée.
6. Point 6 véhicule : **porté**.
7. Sources : **mal porté**, en partie. Le tableau cite maintenant l. 162-163 du véhicule, le message de 12:01Z et le devis passe X. Mais le § 2 (l. 66) garde « L-1 (« part relevable à 136,04 au plus ») » entre guillemets ; la source (l. 162) écrit « peut être relevée à 136,04 dollars au plus ». L-2 (l. 67) est tronqué : source « Si la part tombait sous 124,35 USD ». Correction : « L-1 (« peut être relevée à 136,04 dollars au plus ») est remplacé… » et « L-2 (« Si la part tombait sous 124,35 USD ») n'a plus d'objet… ». Note : la source dit L-2 « Inchangée » dans le véhicule ; la pièce le déclare sans objet, ce qui est cohérent mais à dire (« la mère le consigne au véhicule »). Non vérifiables sur mes pièces : erratum 1 de `envoi-fable-additif-v1` (Minuit sans crédit), état « vérifié À corriger » du devis. Le message de 12:01Z confirme l'existence de la garde « prêt / manque » mais pas le détail « un prêt dit que la clé répond et a du crédit ».
8. § 7, lettre de l'arrêt n° 11 : **porté**.
9. 280 USD : **porté** (`marge_si_part_280_usd` = 23,99).

## Suggestion R5
Portée : `calculer()` rejoue chaque contrôle sur une entrée altérée ; les sept tombent (`epreuve_artefacts`). J'ai recalculé à la main cinq cas (part 255, 270, lignes nulles, deuxième relais 200, plafond 420) : chacun tombe bien. Contrôles non en dur, cas sain préservé.
