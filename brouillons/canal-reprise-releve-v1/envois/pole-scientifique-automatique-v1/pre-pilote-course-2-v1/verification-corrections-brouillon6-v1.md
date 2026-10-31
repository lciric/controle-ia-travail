# Vérification courte des corrections du brouillon 6 — pré-pilote d'étalonnage de la course 2

- Auteur : sous-agent Sonnet 5.5 neuf (`claude-sonnet-5-5`) ; n'a écrit aucune des pièces.
- Date et heure : 2026-10-31, 00:51 UTC (`date -u`).
- Interdits respectés : rien lu sous `donnees/` ; aucun réseau ; seule exécution : le script v6 sous `python3 -I` (dossier vide de `/tmp`) et la fonction `problemes` du validateur ; aucun compagnon `.sha256` écrit ; aucun commit ; aucune clé.
- Pièces lues et empreintes (les compagnons `.sha256` concordent avec `sha256sum`) :
  - brouillon 6 `preenregistrement-pre-pilote-course-2-brouillon6.md` `c54a105b7c9a9fc39694e8a957003bbf5cc017af20c45bd6ca354d91be24493d` (670 lignes, lu en entier) ;
  - script v6 `calcul-puissance-pre-pilote-course-2-v6.py` `b995fb48da87ecaa56f3e4464a824a8b58196a3e23ce574986e0190ebbcaef51` (lu : `etapes_pre_pilote`, `simuler_budget`, ordres) ; sortie `…v6.sortie.txt` `7394ddae54e20aa527c615ff762719ed0a27ec591e08fbd93774536959d6ece3` (lue en entier, 128 lignes) ; **rejeu `python3 -I` (python 3.13.18) : `cmp` muet, sortie identique octet pour octet** ;
  - contre-lecture 4 `contre-lecture-pre-pilote-course-2-brouillon5.md` `226696122aa63fac77865854cee33a0f314cef166ded83302bd2ad3191b381d2` (lue en entier) ; brouillon 5 `96080471…` (compagnon conforme) ;
  - `src/controle_ia/prereg.py` (fonction `problemes`, l. 37 à 60).
- Gravité : **majeur** = bloque la présentation à Lazar ; **moyen** = à corriger avant de présenter, une ligne ; **mineur** = précision, peut suivre.

## Verdict

**Présentable après corrections mineures** (deux moyens d'une ligne chacun : VB6-01, VB6-02 ; le reste est mineur). Les treize constats CP5-01 à CP5-13 sont traités fidèlement ; la sortie v6 se rejoue à l'identique ; tous les chiffres du résumé, des tables, de S17 et des décisions sont dans la sortie v6, sauf un résidu du brouillon 5 (VB6-01) et quelques valeurs dérivées ou arrondies (VB6-03, 05, 07) ; la fonction `problemes` ne signale que les trois sections attendues ; les 49 marqueurs sont comptés exactement. Aucun majeur.

## 1. Traitement de CP5-01 à CP5-13

| Constat | Verdict | Preuve |
|---|---|---|
| CP5-01 (S29 g dans l'annexe) | **tenu** | S31 est un seuil du préenregistrement (l. 49, 278), « ex-S29 g », vocabulaire, « reliées », « actif », méthode et règle de correspondance écrites (l. 278 (i) à (v)). S29 ne contient plus que a à f (l. 277). A19 (l. 529) : bascule vers le substitut, « indépendant de l'annexe » ; A20 (l. 530) : « les deux autres bras inchangés (S31 ne dépend pas de l'annexe) » ; l. 489 : « A19 et A20 ne sont pas des nœuds », cas conjoint ≈ 0,003 (0,03 × 0,10, dérivé) compté dans C12. DEP9 (b) (l. 606), DEP10 (l. 607 : « Elle ne contient rien du bras Gu-Krenn »), R5 lignes 20, 21 (l. 556, 557) cohérents. **D-h (b) applicable** : l. 626, 283, 607. **C12 par cas** : table M9 (l. 422 : cinq cas nommés), l. 423, C12 (l. 242, 448) ; sortie l. 77 : garde 0,99 ; n < 3 : 0,02 ; annexe 0,03 ; Gu-Krenn 0,10 ; basique 0,01 ; « deux ou plus » 0,024 ; C12 0,966 (D-h a) ; 0,864 (D-h b). Recalcul : 0,99 × (1 − 0,024) = 0,966 ; 0,99 × 0,90 × 0,99 × 0,98 = 0,8645. Une incohérence de rangement (VB6-08). |
| CP5-02 (règle unique de sacrifice) | **tenu** | Règle écrite une fois, l. 332 à 336 (quatre alinéas), table « sacrifice → mesure → conditions » l. 342 à 350 (fusions : C12 lue sur les paires, L5 ; M6 réduite : C9 0,97 ; table seule : C6 0,81 ; passe « tableau » : C8 0,91 ; M6 non lancée : C13 ; M6b : hors porte). Comparée à `simuler_budget` (script l. 440 à 547) : liste de sacrifice dans l'ordre `[sacr1, k6, sacr3, sacr4]` = fusions, M6 réduite, table seule, passe « tableau » (l. 473) ; arrêt d'étape retire les retirables non jouées et réduit M6 (l. 498 à 505) ; plafond : retirable retirée, M6 non réduite réduite puis réexaminée, M6 réduite ou protégée non lancée, M6b réserve (l. 508 à 519) ; coût réel compté en entier, coupe à S17 (l. 526 à 537). **M6 n'est jamais retirée entière** : `retire[k6]` n'est jamais posé ; réduite, elle n'est plus réductible (`reduire` refuse si `reduit`) et son non-lancement entre dans `non_lancee` (l. 512, 532). Probabilité imprimée : « M6 réduite qui ne tient pas » 0,0756 (sortie l. 51). C6, C8, C9 mélangés à la probabilité du sacrifice (sortie l. 94, 109). |
| CP5-03 (marqueurs) | **tenu** | 49 occurrences exactes (`grep -o` : 49) ; aucune mention descriptive : la seule occurrence de « À GELER » (l. 105) est dans une table historique et n'est pas le marqueur du validateur. Voir point 3. |
| CP5-04 (ordre du Plan joué) | **tenu** | `ORDRE_TEXTE` (script l. 399) = É1, É2, É3, É4, É5, É5bis, É6, É7a (passe « tableau »), É7b (étiquettes), É7c (fusions), É7d (table seule), É8, É9, É9b = Plan l. 319 à 329 et tableau de coût l. 358 à 371. Les ordres de la v5 (`ORDRE_V5`) et du brouillon 4 (`ORDRE_B4`) sont rejoués en comparaison (sortie l. 55, 56, 98, 99 ; texte l. 86, 247). |
| CP5-05 (config recommandée chiffrée ; M6b) | **tenu** | Sortie l. 50, 53, 54, 64, 65, 96, 97 : coût 30,6 ; dépense médiane 38,7 ; porte 0,158 ; complément 0,178 ; nœud 0,663 ; au total 0,201 ; C13 budget 0,9305. M6b = É9b, rôle `prot_hp` (script l. 435), protégée hors porte, « M6b non lancée 0,0898 » (sortie l. 53), C13 inchangée (texte l. 193, 335, 349). |
| CP5-06 (arrêt à 40) | **tenu** | Effet réel dans le modèle : C13 budget 0,9197 contre 0,9013 sans arrêt ; table seule retirée 0,131 contre 0,074 (sortie l. 51, 52, 78) ; option « 45 sans arrêt » chiffrée dans S17 (l. 265, 632). La justification n'est plus « la plus grosse étape restante ». |
| CP5-07 (qui approuve l'annexe ; P14 fictive) | **tenu** | S28 et S29 : « Lazar l'approuve par un mot ; sans ce mot l'annexe n'est pas scellée » (l. 276, 277) ; A20 inclut « non approuvée par Lazar » (l. 530) ; P14 « sous des paramètres FICTIFS … refaite par l'auteur de l'annexe … garde 22a » (l. 160, 558) ; sortie l. 125, 126 : « grille FICTIVE … à refaire à l'annexe ». |
| CP5-08 (aveugle ; règle de non-lecture) | **tenu** | Règle l. 318 et A21 (l. 531) : aucun verdict d'É6 ni d'É7, aucune clé, avant la fin d'É9 ; seules les consommations (M7) lues. **Garde R5 ligne 30** (l. 567) : cas sain (journal d'accès, décisions rejouées sur les seules consommations, même résultat) et artefact (lecture simulée d'un verdict d'É6 avant É9 : incident ; décision d'essai dépendant d'un verdict : arrêt). Changement de version entre É6 et É7 = arrêt A2 (l. 512, 214). M4 corrigé (l. 188 : fusions et passe « tableau » passent en É7, « elles n'existent pas à É4 ») ; adjudicateur de M5 en É7 (l. 190, 326). |
| CP5-09 (relais coupé / dépense > 45) | **tenu** | Voir point 4. |
| CP5-10 (déclencheurs R4) | **tenu** | M3 : « au plus 2 fausses alertes (≤ 1 %) » ; ≈ 0 aux valeurs prédites, 0,86 pour un instrument trop beau (sortie l. 34 ; texte l. 495) : non inerte, dit. M4 : accord de 100 % sur 20 fiches (10 si passe sacrifiée) : 0,0088 et 0,0167 (sortie l. 39, 43 ; texte l. 496). |
| CP5-11 (sources, lectures) | **tenu** | P10 « 3 sur 4 » à 0,60 : 0,475 (sortie l. 46) cité « 0,48 » (VB6-07) ; 44,9 hors É5bis, 51,5 avec (sortie l. 49 ; recalcul : 3,3 + 3,0 + 2,8 + 5,5 + 1,9 + 11,6 + 4,6 + 1,0 + 3,5 + 1,0 + 0,7 + 6,0 = 44,9 ; + 6,6 = 51,5) ; passage des lectures d'aiguilleur au sacrifiable (−1,14) déclaré (l. 365, 93) ; D-i (3) : avance « au total » dans le bruit ±0,01 (l. 628). |
| CP5-12 (forme) | **tenu** | Statut : 17 constats de la contre-lecture 3 (l. 3, 616) ; A19 porte LECTURE À CONFIRMER (l. 529) ; D-e et D-f avec enjeu, options, inconvénients (l. 634 à 636) ; le couple (a) / (b) de la contre-lecture 3 et celui de D-h sont distingués (l. 616). |
| CP5-13 (petits manques) | **tenu** | S31 : méthode de construction et règle de correspondance (l. 278 (ii), (iii)) ; garde R5 ligne 31 (M6b, source hors de l'entrée, l. 568) et ligne 32 (A11, l. 569) ; DEP2c (liste scellée des sources de M6b, l. 599) ; P(n < 3) = 0,02 dans C12 (l. 242, sortie l. 77). |

## 2. Chiffres contre la sortie v6 (R7)

Méthode : chaque nombre du résumé (l. 7 à 16), du tableau des seuils (l. 20 à 57), de « Ce qui change » (l. 82 à 96), des prédictions P9, P10, P15, de la section « Seuil » (l. 224 à 247, 265, 282 à 293, 343 à 350), des Critères (l. 423, 458 à 466, 473, 478, 491, 495 à 498), du Plan (l. 337, 372 à 375) et des « Décisions à Lazar » (l. 622 à 668) a été confronté à la sortie rejouée.

**Présents et conformes** (échantillon représentatif, vérifiés un à un) : porte 0,16 (0,156 texte de base ; 0,158 recommandée) ; complément 0,18 (0,176 ; 0,178) ; nœud 0,67 (0,668) et 0,66 (0,663) ; au total 0,20 (0,201 ; 0,201) ; défaut R-819 0 (sortie l. 106) ; C1-C2 0,38 ; C3 0,91 ; produit hors juges 0,43 ; C5 0,57 / 0,81 ; C6 0,95 non mélangée (0,952), 0,93 mélangée (0,934) ; 0,97 / 0,95 recommandée (0,970 / 0,950) ; C7 0,85 ; C8 0,92 (0,919) ; C9 0,99 (0,992) / 0,986 / 0,984 ; C10 0,92 (0,917) ; après complément 0,70 (0,696) ; recommandée 0,91 / 0,65 ; C12 0,97 (0,966), 0,86 (0,864) ; C13 0,95 × 0,92 (0,9197), × 0,93 (0,9305), sans arrêt 0,90 (0,9013) / 0,92 (0,9173) ; C14 0,96 ; déclencheurs 0,11 / 0,09 / 0,009 / 0,004 / 0,145 ; coûts 28,4 (20,5 + 8,0), 30,6, 11,6 / 17,5 / 13,0, 1,6 / 2,5, 44,9 / 51,5 ; dépense médiane 36,3 / 38,7, quantile 90 % 42,8 / 44,2 ; sacrifices 0,24 (0,237) avec fusions 0,13, M6 réduite 0,23, table seule 0,13, passe « tableau » 0,04 ; recommandée 0,34 (0,335) avec 0,21, 0,32, 0,145, 0,07 ; arrêt touché 0,30 / 0,42, « réduit ou retire » 0,08 ; M6 réduite qui ne tient pas 0,076 / 0,061 ; non lancée 0,080 / 0,070 ; M6b non lancée 0,09 ; sans arrêt : 0,094 / 0,075, table seule 0,07 / 0,11 ; plafond 32 : porte 0,11 / 0,10, nœud 0,77 / 0,79, sacrifices 0,92 / 0,98 (0,894 ; 0,821 ; 0,678 ; 0,604), C13 0,66 / 0,62, C10 0,98 ; relais dur : 0,80 (É2 0,375 = 0,38 ; É4 0,292 = 0,29), sacrifices 0,053 ; D-i : 28,4 / 28,9 / 28,2, C6 0,934 / 0,950 / 0,952, porte 0,156 / 0,157 / 0,156, au total 0,201 / 0,202 / 0,215 ; D-h (b) : 0,143 / 0,695 / 0,184 ; M1 à six niveaux, R-1 (0,61 ; 0,47), variante (3) ; P9 (0,92 ; 0,73 = 1 − 0,27) ; C8 sur 10 fiches 0,91 / 0,39 / 0,0167 ; M6 réduite 0,967 / 0,20 / 0,101 ; décomposition de C10 (0,936 → 0,98 → 0,92 → 0,70) ; ordres (0,152 / 0,90 ; 0,148 / 0,87 ; 0,160 / 0,95) ; causes de défaut de la l. 466 (1 − probabilité de chaque condition).

**Absents, différents ou dérivés** :
1. **l. 491 (Complément)** : « À la prédiction P1 : complément proposé **0,20**, porte ouverte au total **0,22** » = valeurs du brouillon 5. Sortie v6 : 0,176 et 0,201 (sortie l. 94, 96). **Résidu — VB6-01.**
2. l. 265 et l. 350 : « autres 0,004 (0,008) » (étapes protégées autres que M6 non lancées) : non imprimé ; dérivé de la sortie, 0,0803 − 0,0756 = 0,0047, soit 0,005 et non 0,004 ; recommandée 0,0695 − 0,0614 = 0,0081 (0,008, conforme). **VB6-05.**
3. l. 624 (D-g) : « sur la porte : +0,002 … contre texte de base **à D-i égal** » : la sortie n'imprime pas D-g (b) avec D-i (1) ; elle donne 0,156 (base), 0,157 (D-i 2 seule), 0,158 (D-g b + D-i 2). **VB6-03.**
4. l. 156, 193, 279, 93 : « 0,48 » pour 0,475 (sortie l. 46 imprime 0,475) : arrondi vers le haut. l. 265 : « médiane prédite du brouillon 3, 35,5 » : vient de la sortie v3 (ligne 32), non de la v6 ; citer la sortie v3. **VB6-07.**
5. l. 423 : « D-h (b) : 0,13 » et l. 489 : « ≈ 0,003 » : dérivés (1 − 0,864/0,99 = 0,127 ; 0,03 × 0,10), non imprimés. Corrects. **VB6-07.**
6. Résumé 6 (l. 12) : « C6 0,95 → 0,97 » : valeurs non mélangées (sortie l. 31, 32 : 0,952 → 0,970), alors que la table de D-i (l. 628) donne les valeurs mélangées 0,934 → 0,950. Les deux sont dans la sortie, mais le résumé ne dit pas « sans sacrifice ». **VB6-06.**
7. Chiffres de la course 1 (« 27 sur 29 », « 12 sur 29 », « 17 idées », « 0,12 », « ×1,34 ») et « ≈ 0,15 à 0,2 » du kappa : repris « tels que consignés, non relus » (l. 77) ou SUPPOSÉ ; non opposables ; déclaré, rien à corriger.

**Mentions résiduelles du brouillon 5 ou du script v5** (`grep v5`, `brouillon 5`, 0,17 / 0,63 / 0,968 / 28,9 / 0,22 / 0,085) : toutes sont soit des renvois d'empreintes (l. 63, 64, 72), soit des comparaisons étiquetées (« brouillon 5 : … » l. 7, 84, 96, 245, 247, 461 ; ordre « du script v5 » l. 86, 247, 338), soit la section « Rappel : ce qui a changé au brouillon 5 » (l. 100 à 121, étiquetée « gardé pour la lecture » ; ses mentions « script v5 » l. 104, 106, 113, 118 sont exactes pour le brouillon 5), soit 28,9 = D-i (2) (exact). **Une seule erreur : l. 491 (VB6-01).** La ligne 110 (« 0,17 contre 0,15 ; sacrifices 0,24 contre 0,92 ») est dans la section de rappel, exacte pour le brouillon 5.

## 3. Validateur et marqueurs

`problemes('…brouillon6.md')` renvoie exactement :
- `section vide ou à remplir : Métrique`
- `section vide ou à remplir : Seuil`
- `section vide ou à remplir : Contre-lecture`

Aucune autre section absente ou vide, aucun marqueur de gabarit `<<…>>`. Ce sont les seules attendues. Réserve de lecture du validateur (l. 44 à 47) : le message « marqueur restant hors des sections exigées » est supprimé tant qu'une section exigée est signalée ; les cinq marqueurs hors sections exigées (trois en tête, deux en « Rôles, témoins et dépendances ») ne seront donc signalés qu'une fois Métrique, Seuil et Contre-lecture remplies ; ils sont tous voulus et seront remplis ou retirés au gel (VB6-10).

**Les 49 marqueurs** : lignes 61 (1), 76 (2), 168, 197, 249 à 252, 254 à 269, 271 à 273, 275 à 285, 287 à 293, 601, 602, 618. Décompte par zone : 3 en tête (l. 61, 76 ×2) ; 2 en Métrique ; 41 en Seuil (S1 à S4 : 4 ; S6 à S21 : 16 ; S23 à S25 : 3 ; S27 à S31 : 5 ; D-e à D-j : 6 ; L1 à L7 : 7) ; 2 en Rôles ; 1 en Contre-lecture. **= 49, conforme à la table (l. 295).**

**Ceux qui ne sont pas des décisions de Lazar** (six, des valeurs ou des faits à fournir au scellement, légitimes comme marqueurs, mais le texte les range sous « un par décision ») : l. 61 commit du code d'analyse ; l. 76 (×2) empreinte de l'annexe et chemin / empreinte de la source de S31 et de son essai ; l. 168 nombre k d'items lu sur la consigne figée ; l. 197 résumé d'une ligne du tableau lu sur la consigne de la course ; l. 618 contre-lecture 5. Les 43 autres sont des décisions de Lazar (dont S28 et S29, où il approuve une proposition de l'annexe). Aucun marqueur n'est mal placé ; aucune décision de Lazar n'en manque (D-g à D-j, lectures, confidentialité, aiguilleur, S31 y sont).

## 4. Choix d'auteur CP5-09

**Déclaré clairement** : résumé 3 (l. 9), « Ce qui change » (l. 91), règle d'A1 (l. 336), A1 (l. 511), DEP4 (l. 601), « Contre-lecture » (l. 617), S17 (indirectement). Le texte dit : plafond de relais = réservation (sert aux tests de projection) ; coût réel compté en entier ; S17 seul plafond qui coupe ; relais au-delà de sa réservation = réserve M7 (0,84 des tirages, sortie l. 51). **DEP4** pose l'hypothèse (« le relais accepte une réservation dépassée jusqu'à S17 − cumul », SUPPOSÉ, à confirmer par session-depot) et son repli (« sinon la lecture “relais dur” s'applique et le Plan est à réécrire »). **Lecture « relais dur » rapportée** : sortie l. 62 à 65 : coupe une étape protégée avec 0,798 (É2 0,375 ; É4 0,292 ; É6 juges 0,038 ; É9 0,072), sacrifices 0,053, dépense médiane 33,6, 90 % à 40,3 (sans troncature 36,3 et 47,2) ; texte l. 91, 338, 617. La raison de ne pas la retenir (les réservations sont sous les bornes hautes de P11) est écrite.

**Est-ce un marqueur / une décision de Lazar ?** Non : c'est un choix de modélisation acceptable, et un fait technique du relais (session-depot), non une préférence de Lazar. Deux réserves toutefois : (i) DEP4 n'est pas une condition de lancement de A15 (l. 525 ne liste ni la confirmation du relais) : si le relais est dur, la règle du Plan est fausse sans qu'aucune garde l'arrête ; (ii) la section « Décisions à Lazar » ne mentionne pas ce choix, alors qu'il pèse 0,80 sur la mesure d'une étape protégée. Correction courte : une phrase dans S17 et DEP4 ajouté à la liste d'A15 (VB6-04).

## 5. Format de « Décisions à Lazar »

| Décision | Phrase | Enjeu | Options avantage / inconvénient | Recommandation et confiance | Aucun défaut |
|---|---|---|---|---|---|
| D-g (l. 624) | oui | oui | (a) et (b) : avantage et inconvénients | (b), 0,6 | oui |
| D-h (l. 626) | oui | oui | (a) avantages / inconvénient ; (b) avantage / inconvénients | (a), 0,55 | oui |
| D-i (l. 628) | oui | oui | (1), (2), (3) : avantage / inconvénient chacune | (2), 0,6 | oui |
| D-j (l. 630) | oui | oui | oui et non : avantage / inconvénient | oui, 0,7 | oui |
| S17 (l. 632) | oui | oui | « 45 ; 40 » complète ; « sans arrêt » complète ; « 32 ; 28 » : inconvénients seulement (la mention « couverte par GO-2026-10-30-07 » tient lieu d'avantage) | 45 ; 40, 0,65 | oui |
| D-e (l. 634) | oui | oui | (i) et (ii) complètes | (i), 0,6 | oui |
| D-f (l. 636) | oui | oui | (i) complète ; (ii) et (iii) : inconvénient seulement | (i), 0,6 | oui |
| **L1 à L7 (l. 670 ; l. 287 à 293)** | non | non | **non** : « oui / retirée », « accepté / contre-lecture rétrospective », sans avantage ni inconvénient (quelques raisons dans le texte de M8, Plan, M9) | **non** : « telles que lues par l'auteur », ni confiance ni recommandation par ligne | « aucun défaut » écrit |

Les seuils S1 à S31 (l. 638 à 668) ont recommandation, confiance et alternative (« — » quand la raison du seuil suffit, dit en tête de table) ; S28 et S29 n'ont pas de confiance (« — », propres à l'annexe) ; acceptable. **Écart de format : L1 à L7 (VB6-02).** D-f (ii), (iii) et S17 « 32 ; 28 » : avantage manquant (VB6-09).

## 6. Autre chose qui empêche la présentation ?

Non, sous réserve de VB6-01 et VB6-02. Hors du texte (déjà listé l. 16) : annexe du bras méta (verdicts des collisionneurs), décisions de Lazar, ligne de GO au plafond gelé, confidentialité, concrets de l'aiguilleur, PDF de Gu et Krenn, devis v4, contre-lecture 5. Aucune garde d'arrêt, aucun défaut à 48 heures (relu : le mot « défaut » n'apparaît que pour « aucun défaut » et pour le défaut R-819, qui est un autre sens), aucun chiffre d'article repris (R7 tenu : l. 73, 75), aucune prédiction visée comme résultat positif (R3).

## Constats VB6-01 à VB6-11

**VB6-01 (moyen) — Résidu du brouillon 5 à la l. 491.** « À la prédiction P1 : complément proposé 0,20, porte ouverte au total 0,22 » ; sortie v6 : 0,18 et 0,20 (sortie l. 94 : complément 0,176, au total 0,201 ; texte l. 161, 245, 461). Lazar lirait deux chiffres contradictoires. Correction : 0,18 et 0,20.

**VB6-02 (moyen) — L1 à L7 sans le format de décision.** La section finale (l. 670) les résume en une ligne sans enjeu, options avantage / inconvénient, recommandation propre ni confiance ; le tableau du résumé (l. 57) dit seulement « lectures de l'auteur ». Ce sont sept règles de lecture qui fixent la porte (L4 : C10 0,92 ou 0,98 ; L1, L2 : sacrifices ; L5 : C12 ou nœud). Correction : une ligne chacune avec recommandation et confiance (les chiffres existent : L2 C6 0,81 ou 0,95 ; L4 0,92 / 0,98 ; L1 −3,1 USD, M5 à 10 fiches).

**VB6-03 (mineur) — D-g : « +0,002 sur la porte … à D-i égal »** (l. 624) n'est pas dans la sortie (D-g (b) seule n'est pas jouée ; 0,156 → 0,157 par D-i (2), 0,158 pour les deux). « Sous le seuil de 3 USD que je m'étais fixé » : seuil d'auteur non sourcé. Correction : « +0,002 pour D-g (b) et D-i (2) ensemble (0,156 → 0,158) » ; supprimer ou sourcer les 3 USD.

**VB6-04 (mineur) — CP5-09 : DEP4 n'arrête rien, S17 n'en parle pas.** Voir point 4. Correction : ajouter « confirmation du relais (DEP4) » à A15 ou en garde R5, et une phrase dans S17 (0,80 si le relais est dur).

**VB6-05 (mineur) — « autres 0,004 (0,008) »** (l. 265, 350) : dérivé 0,0047, soit 0,005 ; non imprimé par le script. Correction : 0,005, ou imprimer la ligne.

**VB6-06 (mineur) — Résumé 6 : « C6 0,95 → 0,97 »** sans « sans sacrifice » ; la table de D-i donne 0,934 → 0,950 (mélangé). Correction : préciser la base (ou donner 0,93 → 0,95).

**VB6-07 (mineur) — Arrondis et valeurs dérivées.** 0,475 écrit 0,48 (l. 93, 156, 193, 279) ; 35,5 vient de la sortie v3 (l. 265) ; 0,13 (l. 423) et 0,003 (l. 489) dérivés. Correction : écrire 0,475 / « 0,47 à 0,48 » ou « 0,48 (arrondi) » ; citer la sortie v3 ; marquer « dérivé » les deux autres.

**VB6-08 (mineur) — M9 l. 422, cas (i) mal rangé.** « Effectif n < 3 » est rangé sous « un bras non produit … pas un échec de garde », alors que la règle l. 202 donne deux bras non produits pour n = 2 et trois pour n < 2 : ce cas relève de la ligne suivante (l. 423, « deux bras ou plus non produits », C12 non satisfaite) et de la cause « n < 3 : 0,02 » de C12. Correction : sortir (i) de la ligne l. 422 ou le dire.

**VB6-09 (mineur) — « Avantage » manquant** à D-f (ii), (iii) et à S17 « 32 ; 28 » (point 5).

**VB6-10 (mineur) — Table des marqueurs.** Six des 49 marqueurs sont des valeurs ou des faits (point 3), non des « décisions » ; et le validateur ne signale les cinq marqueurs hors sections exigées qu'une fois les trois sections remplies (l. 44 à 47). Correction : dire « 43 décisions de Lazar et 6 valeurs à fournir au scellement » ; rien d'autre.

**VB6-11 (mineur) — Forme.** Ligne 3 : `**` fermant sans ouvrant (fin « (R12).** »). Correction typographique.

Aucun constat majeur.

## Ce que je n'ai pas vérifié

- Les décisions R-630 à R-643, R-662 et R-663 de `registres/decisions.md` ne sont pas relues ligne à ligne (R-630, R-647, R-651 et R-663 lues en passant) ; le contenu des PDF, de l'annexe (inexistante), du devis v4 et de `origin/main` n'est pas accessible.
- L'effet chiffré d'un changement de règle (relais, DEP4) : seul le script v6 pouvait être rejoué ; aucun autre calcul n'a été lancé.
- La complétude de la table R5 pour des gardes non écrites (essais « à jouer en É0 ») : lue, non exécutée.

## Verdict (une ligne)

**Présentable après corrections mineures** : corriger l. 491 (0,20 / 0,22 → 0,18 / 0,20) et donner à L1 à L7 le format de décision (VB6-01, VB6-02) ; les neuf autres constats peuvent suivre dans le même passage.
