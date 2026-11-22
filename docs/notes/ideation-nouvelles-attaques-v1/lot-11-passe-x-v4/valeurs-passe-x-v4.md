# Valeurs de la passe X, lot 11 v4 — à sceller par la mère

Écrit le 2026-11-22 (`date -u` : 13:02:09Z) par la session de l'organisme. Les valeurs approuvées par la mère à 12:49Z, points (1) à (7), et son message de 13:00Z.

1. **Groupes par thème.** Composés par l'intitulé des fichiers ; les numéros sont ceux de la liste de 18.
   - G1 : pièces 1, 2, 3, 9, 15 et 18.
   - G2 : pièces 4, 5, 6, 7, 8 et 17.
   - G3 : pièces 10, 11, 12, 13, 14 et 16.
   - Moitiés pour la relance : les trois premières pièces, puis les trois dernières, de chaque groupe.
2. **Préambule.** Il est servi tel quel ; « {n} » vaut « six » pour un groupe, « trois » pour une moitié :
   « Voici {n} questions de recherche, numérotées comme dans une liste de dix-huit. Répondez à chacune, dans l'ordre, sous un titre de la forme « Réponse k », où k est le numéro de la pièce. Chaque réponse fait au plus 600 mots. Terminez par une ligne seule : FIN DES RÉPONSES. »
   Empreinte du gabarit : 0be51171246c4612149d55bd27c1c607622f2744be3c2a4f02f178800b6530c0. Il passe la garde de motifs avec zéro motif.
3. **Textes servis.** Empreintes et tailles :

| texte | pièces | octets | sha256 |
|---|---|---|---|
| groupe-1 | 1, 2, 3, 9, 15, 18 | 6712 | `b824df08208fcc53636fb6c71d23a89f47f2e98525f496341a5496df5692e531` |
| groupe-1-moitie-a | 1, 2, 3 | 2665 | `f503f550c61188e918f2c72412c7b72923065085b5418155863261717f8d914c` |
| groupe-1-moitie-b | 9, 15, 18 | 4336 | `d44033469620fc89534e3abcbd07927d90ca5f61a2e3284ac79e4c4a31adf654` |
| groupe-2 | 4, 5, 6, 7, 8, 17 | 7495 | `fc9bed7ffdadca5f2a8d288d2cacece0953c8e8f95671b7ddc3f8cf36ab153c9` |
| groupe-2-moitie-a | 4, 5, 6 | 3789 | `f179039e77d45b620a141b5ac9fac1b533bd69fea14d2b9f5b61baff53e32106` |
| groupe-2-moitie-b | 7, 8, 17 | 3995 | `8ca599c1366291b13757838124cbec7f62355b7261321aedd668e4176a81fcac` |
| groupe-3 | 10, 11, 12, 13, 14, 16 | 8665 | `61fceb5ecf19d5b86d08bd213416ac66b327f3f98d7e113cebed3d1889bb4289` |
| groupe-3-moitie-a | 10, 11, 12 | 4412 | `6e07440af900dbb44c96e5d0f0b7a78b2ed262db7a3b3746aca6ddc4b485c770` |
| groupe-3-moitie-b | 13, 14, 16 | 4542 | `9b96216aab49c15e2e99250c657af3572007f4d22a8bca47d4bd913e9a2e7e49` |

4. **Garde de coupure** (B.4 de la réponse 36), par programme, sans rien afficher :
   - fin normale, avec le flux clos ;
   - ligne finale « FIN DES RÉPONSES » une seule fois, en dernière ligne ;
   - titres « Réponse k » dans l'ordre exact, chacun avec au moins 240 mots (40 % de 600) ;
   - modèle servi égal au modèle demandé ;
   - alerte, sans rejet, au-delà de 90 % du plafond, ou si le dernier tiers est deux fois plus court que le premier.
5. **Relance**, une seule par unité (modèle, groupe), marquée :
   - transport : la même requête ;
   - réflexion épuisée : un cran d'effort en moins ;
   - texte coupé ou couverture incomplète : deux moitiés.
   Un second défaut classe l'unité « sans réponse ». Le repli de GO-35 sur refus de classifieur est gardé.
6. **Ordre d'envoi.**
   1. Garde de départ, puis essai d'effort.
   2. Groupe 1 pour les neuf modèles.
   3. Barrière : au plus deux modèles en défaut de réglage, soit sept sur neuf.
   4. Groupes 2 et 3.
7. **Effort.**
   - Opus 5.5 et Fable 5.1 partent **un cran sous le maximum**. Le niveau xhigh est essayé, puis high. C'est le choix du message de 13:00Z : le budget de tâche n'est pas ajouté, pour ne pas rouvrir une vérification.
   - Opus 4.6, Sonnet 4.6 et Astra : essai décroissant à partir du plus haut niveau.
   - Google : niveau le plus haut (high pour Argon et Carbon, xhigh pour Neon), réflexion comptée à 49 152, sortie de 65 536.
   - Kimi : sortie de 96 000.
8. **Pire.** P_X = 199,65 USD (33 × 6,05), sous les 200 de GO-46.
   - Sous-parts : RR_ANTHROPIC_API_KEY_LUC 90,75 ; GEMINI_API_KEY 66,55 ; OPENAI_API_KEY_2 24,20 ; KIMI_API_KEY 18,15.
   - Configuration : `lancement/configuration-passe-x-groupes-v4.json` (5d6ce6c679554f03…).
9. **Écarts au devis v3 scellé, sur les mots de Lazar :**
   - Neon en neuvième proposeur (GO-2026-11-22-33) ;
   - 18e pièce (GO-2026-11-22-57) ;
   - groupes, préambule et garde de coupure (écart à X-2) ;
   - Google à 65 536 ;
   - P_X porté de 96,80 à 199,65.
