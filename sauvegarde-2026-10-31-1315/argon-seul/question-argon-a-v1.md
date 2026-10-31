# Question à Argon — décisions ouvertes, dossier a : course 2 et pré-pilote — v1

Écrite par session-depot, 31 octobre 2026, sous GO-2026-10-31-08 (mot direct de Lazar : « demande a argon aussi pour toutes les questions ouvertes […] restant a trancher par moi ou conv »). Tu donnes un avis ; tu ne tranches rien : Lazar (le directeur) décide.

**Contexte.** Le programme « contrôle boîte blanche des menaces diffuses » étudie des moniteurs de sécurité pour des agents d'IA (sondes sur les activations et moniteur sur le texte) contre des sabotages étalés sur beaucoup d'actions peu suspectes. Les décisions ci-dessous sont en attente du directeur ou de la lignée de travail conv-audit. Les faits qui suivent sont des extraits des pièces du dépôt, avec chemin, lignes et empreinte ; les recommandations et confiances de leurs auteurs ont été **retirées** pour ne pas t'ancrer.

**Consigne.** Pour **chaque** décision de la liste ci-dessous, en français :
1. l'option que tu choisirais (une seule ; ou une option nouvelle si aucune ne tient, dite comme telle) ;
2. ta raison, en t'appuyant sur les faits servis (cite la pièce et la ligne) ;
3. le pire cas de ce choix (ce qui se passe s'il est faux) ;
4. ce qui te ferait changer d'avis (une mesure, un fait, un seuil).
Puis, en fin de réponse : les décisions qui te paraissent liées (à trancher ensemble), et les trois que tu trancherais en premier.

Règles : n'invente aucune pièce ni aucun chiffre ; une référence que tu n'as pas lue ici est marquée SUPPOSÉ ; reste au niveau de la méthode (aucune recette pour tromper un moniteur, aucun détail d'attaque) ; si une décision te semble mal posée, dis-le. Environ 6000 mots au plus pour la réponse.

## Décisions à examiner

- **Pré-pilote de la course 2, brouillon 10** (pièce 1) : seuils **S1 à S4, S6 à S16, S18 à S21, S23 à S25, S27, S30, S31** (S17 est gelé par le directeur à 50 ; 45 USD ; S22 fixé à 24 fusions ; S5 et S26 retirés ; S28 et S29 viennent de l'annexe du bras méta, traitée ailleurs) — pour chaque seuil : garder la valeur proposée, ou laquelle sinon.
- **D-e** (lecture de « domaine » et de « concept », bras basique) et **D-f** (modèles des rôles neufs : metteur en forme T, relecteur).
- **Lectures L1, L2, L3, L5, L6, L7** (L4 sans objet).
- **Étalonnage de l'aiguilleur** (DEP5 : étalonner l'aiguilleur avant le pré-pilote, ou non ; sans étalonnage, le critère C7 est fermé).
- **Confidentialité** (A15 : envoyer les fiches du pré-pilote à Moonshot (Kimi) et à Google (Argon), oui ou non, et sous quelles conditions).
- **Texte III, mesure statistique de l'universalité** (pièce 2) : décisions 1 à 5 (loi sur la classe ; variante et intervalle de l'estimateur ; formule de couverture ; zone d'indifférence ; rapport du minimum observé).
- **Tableau partagé de la course 2** (pièce 3) : les décisions de la section 5.
- **Machine jetable** (pièce 4) : louer ou non la machine jetable (compte chez un hébergeur, ≈ 0,5 USD attendus, 7,4 au pire), qui sert au rejeu de l'orchestrateur dans son vrai bac à sable avant le pré-pilote.

## Faits

### Pièce 1 — `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon10.md (branche canal/conv-audit-n04)`, l. 5–17, l. 219–258, l. 316–392, l. 622–622, l. 698–702, l. 722–fin

Empreinte du fichier source : `ea940d56e5ee949e7b71a57488f7c2c8a2b7ac4835f30cb5f98933e4c00c824f` ; 12208 mots servis ; 67 retraits (recommandations, confiances, défauts des auteurs).

## Résumé pour Lazar (dix lignes)

1. Verdict : **issue la plus probable : nœud, pas de départ.** Aux valeurs que je prédis, au S17 gelé par Lazar (50 ; 45), **sur les bases de coût du devis v6 entières** (les quatre de R-698 et, depuis ce brouillon, la fusion observée et le rédacteur au prix de Sonnet), la **conjonction entière** de la porte (C1 à C14) s'ouvre d'emblée avec **0,17** sur le texte de base (D-g a, D-i 1 : 0,175) **et sur la configuration retenue (D-g b, D-i 2 : 0,173)** ; complément proposé 0,20 ; nœud d'emblée 0,63 (0,631 retenue) ; **0,24 au total si le complément reçoit son GO** ; **au défaut R-819 (aiguilleur non étalonné) : 0** (script v9 `a28eca2d…`, mêmes graines que les v4 à v8 : seules les bases de coût bougent les chiffres). **Effet des deux bases reprises** (brouillon 9, mêmes relais, plafond et graines, entre parenthèses) : porte 0,173 (0,167) recommandée, 0,175 (0,170) texte de base ; nœud 0,631 (0,644) ; total 0,239 (0,230) ; **C13 budget 0,926 (0,897) recommandée, 0,948 (0,926) texte de base** ; dépense médiane 40,1 USD (42,3) recommandée, 37,6 (39,6) texte de base ; C10 0,999 (0,998) ; **fusions retirées 0,20 (0,57) recommandée, 0,16 (0,54) texte de base**. Décomposition du brouillon 8 au devis v6 (configuration retenue, porte d'emblée) : 0,185 (bases du brouillon 8) → 0,169 (+ 60 lectures et coupures de Kimi : l'annonce de R-698, vérifiée) → 0,167 (les quatre bases de R-698 = brouillon 9) → **0,173 (bases du devis v6 entières)** ; détail dans « Ce qui change par rapport au brouillon 9 ».
2. Porte des juges seule (C1-C2) : 0,38 ; juges tous à 0,90 : 0,85 pour les juges, 0,38 pour la porte entière ; à 0,85 : 0,54 et 0,24 (sortie v9 ; inchangé côté juges : M1 ne dépend pas des coûts). Kimi est prédit exactement à S1 : son étalonnage reste un pile ou face (0,50).
3. Hors juges (produit 0,48 ; 0,47 au brouillon 9) : ce qui ferme la porte : C5 (0,81), aiguilleur C7 (0,85), débordement C8 (0,92 ; 0,914 mélangée aux retraits de la passe « tableau »), C6 (0,94 mélangée aux retraits de la table seule), C12 (0,97 : causes de bras non produit, CP5-01), C13 (0,95 × 0,948), C10 (0,999 : reste = 160 − dépense, course à 24 fusions ; elle tient à 4 sous-sessions avec 0,60, à 3 avec 0,32, à 2 avec 0,07 ; **devis v6 § 5, à 160, lecture B, deux colonnes : sans complément 0,246 ; 0,556 ; 0,191 ; 0,007 (C10 0,993) ; avec complément proposé avec 0,20, coût tiré, 0,213 ; 0,550 ; 0,227 ; 0,010 (C10 0,990). Appariement exact de ma lecture sans complément : la colonne « sans complément » ; l'écart (0,60 contre 0,25 à 4 sous-sessions) vient du modèle de coût de la course, que la sensibilité « échelle du devis v6 » (×1,175), sans complément, rejoint : 0,32 ; 0,46 ; 0,21 ; à aucune 0,008, C10 0,992 ; VB8-04, VB9-05**). **Budget lu selon la règle d'A1, étape par étape, dans l'ordre du Plan, avec les relais ET les bases de coût du devis v6 (GO-2026-10-31-03 ; R-698 ; brouillon 10) : plafonds de relais du brouillon 5, souples pour les étapes protégées (au lancement, max(plafond de l'étape ; S17 − cumul − attendu aux bases des étapes restantes non retirées)), fixes pour les retirables ; chaque relais est un plafond dur fixé au lancement** : au plafond de 50 USD avec arrêt d'étape à 45, une mesure de C1 à C9 est « non mesurée (budget) » avec 0,052 (0,074 retenue) ; **une étape retirable bute sur son relais fixe avec 0,56 (passe « tableau » 0,505 ; fusions 0,075 ; table seule 0,043) et est alors retirée** : passe « tableau » perdue 0,53, fusions 0,16 (0,20), table seule 0,12, M6 réduite 0,19 (0,24, dont 0,06 et 0,05 par coupure de son relais : M6 n'est jamais retirée entière) ; dépense médiane 37,6 USD (40,1 retenue), quantile 90 % 46,4 (48,0). La porte en souffre peu ; **ce que le pré-pilote éprouve se réduit surtout du côté de M5** : M5 sur 20 fiches n'est éprouvée qu'avec 0,47 ; la chaîne de bisociation au-delà de la paire l'est avec 0,84 (0,80) (0,46 et 0,43 au brouillon 9, où la fusion comptée 0,40 SUPPOSÉ butait sur son relais ; avec le rapport de médiane 1,3 de P11 gardé sur la fusion observée : 0,74 retenue, sensibilité (f')). **Écart avec le devis v6** (§ 3.3, configuration retenue : sacrifice 0,17, fusions 0,12, non lancée 0,021, coupée 0,063, médiane 40,6 ; ici, au même sens : 0,195 ; 0,130 ; 0,023 ; 0,083 ; 40,1) : avec les bases du devis entières, l'attendu tombe sur le devis et la médiane à 0,5 USD près ; l'écart restant sur « coupée » (+0,020) et sur le sacrifice (+0,025) n'est pas attribué (le script du devis n'est pas rejoué) ; deux différences de modèle connues, non mesurées : le devis tire les coupures de Kimi appel par appel (§ 2.4), ce script les compte par un facteur constant ×1,447 ; M6b est répartie autrement (É9b 1,4 au devis ; 0,40 en É1 et 1,0 en É9b ici) ; détail dans « Seuil » (S17) et dans « Ce qui change par rapport au brouillon 9 » (VB9-03, VB9-04).
4. **Ce que le pré-pilote éprouve réellement (CP4-01)** : l'obéissance des trois juges à leur grille sur témoins nets ; la détection d'une **redite entre fiches du lot** (mémoire, axe 7) ; la détection de **références inventées ou altérées** (M6) ; l'aiguillage des détails concrets ; la tenue de niveau méthode de Kimi ; les cloisons du tableau ; la chaîne de bisociation. **Il n'éprouve ni la détection d'une antériorité publiée non citée, ni « très plausible » au sens des tests de mort** : décision **D-g** (ajouter 4 fiches d'antériorité non citée à M6, ≈ 1,4 USD, recommandé ; ou déclarer le vide).
5. **Bisociation** : trois bras, une paire chacun — bras méta v1, bras Gu-Krenn (modèle ou **substitut inspiré de Gu et Krenn**), bras basique. **Les paramètres du bras méta (S28, S29 a à f) vivent dans une annexe séparée, écrite après les verdicts des collisionneurs, contre-lue par un modèle différent, scellée et empreintée dans ce préenregistrement avant son gel, et leurs valeurs sont approuvées par Lazar sur proposition de l'annexe** (CP4-02, CP5-07) : décision **D-h** (retarder le gel jusqu'à l'annexe, recommandé ; ou geler à deux bras et ajouter le bras méta dans la course : C12 tombe alors à 0,86, porte 0,155). **Les paramètres du substitut de Gu et Krenn sortent de l'annexe et deviennent le seuil S31 de ce préenregistrement** (CP5-01) : une annexe non conforme à É0 ne fait plus tomber que le bras méta (C12 0,97 ; « non lancé », déclaré, pas un nœud).
6. **Plan des fonds (CP4-03)** : décision **D-i** entre (1) 28 fonds uniques (texte actuel), (2) 28 fonds + 4 rendus appariés pour la seule mémoire anti-redite (+0,55 USD, coupures de Kimi comprises ; C6 0,95 → 0,97 sans sacrifice, 0,94 → 0,95 mélangée aux retraits de la table seule, sortie v9 ; recommandé), (3) 24 fonds dont 4 doublés (−0,1 USD, 8 fiches corrélées). **Gu-Krenn sans condition de reproduction** : décision **D-j**.
7. Coût : attendu aux bases ≈ 30,1 USD (texte de base) ; **≈ 32,1 USD pour la configuration retenue** (M6b 1,4 ; D-i (2) 0,55) ; **S17 = plafond 50 USD, arrêt d'étape 45 USD — gelé par Lazar (GO-2026-10-31-03)** ; la ligne de GO existe (échéance 2026-11-07 : au-delà, A15 exige une ligne nouvelle) ; aucun repli. Complément conditionnel : ≈ 11,6 USD attendus, plafond 17,5 (CP4-10 ; bases du devis v3, hors coupure de Kimi ; avec la coupure ×1,447 sur ses postes de Kimi : 12,5, tient sous 17,5 avec 0,86, VB9-12). **Le devis v6 (session-depot, `13ef84f9…`) est rendu ; ses bases de coût sont reprises entières : les quatre de R-698 (60 lectures d'étiquettes à 1,5 USD, seconde version à 5,8 USD, prix de Sonnet 5.5 pour le rôle T, coupures de Kimi ×1,447 ; brouillon 9) et, depuis ce brouillon, la fusion observée (0,204 USD par fusion, devis v6 § 2.2, rapport de médiane 1,0, § 2.4) et le rédacteur au prix de Sonnet (É1 1,8 ; É8 0,3 ; § 3.2). Le script v9 les joue par défaut : attendu 30,1 / 32,1 = devis v6 § 3.2, mêmes configurations, sans seconde version (texte 30,1 ; recommandée 32,1) ; avec la seconde version pondérée (+2,5) : 32,6 / 34,6, comme au devis (VB9-02).**
8. Liste fermée des options du nœud : O0 à O14 inchangées, **O15 ajoutée** (bras non produit, hors porte, CP4-05) ; relâchements R-1 à R-3 inchangés.
9. Inchangé : témoins non ambigus ; aiguilleur avant les juges ; tableau minimal éprouvé ; quatre instances distinctes au bras d'attaque ; arrêt clos ; adjudication de M5 ; notation croisée gardée ; aucune mesure de performance de l'organisme (restes d'A7 et de M9 retirés, CP4-14).
10. À faire : présenter ce brouillon 10 à Lazar ; annexe du bras méta (après collisionneur ; valeurs approuvées par Lazar) ; décisions D-g à D-j, D-e, D-f, S1 à S31 sauf S17 (gelé), lectures L1 à L7 sauf L4 (sans objet) ; mot sur l'étalonnage de l'aiguilleur ; confidentialité ; PDF de Gu et Krenn versé (R7) ; essai de S31 sur la moisson ; contre-lecture 5 (modèle ni Opus ni Fable) ; scellement ; GO de lancement (avant l'échéance du 7 novembre de GO-2026-10-31-03, sinon ligne nouvelle).

[…]
## Hypothèse

**Renvoi au programme.** Ce pré-pilote ne teste aucune hypothèse du programme : il étalonne les instruments de garde et de lecture de la course 2, comme l'exigent Q1 (R-552), l'annexe 3 du texte I (« étalonnage préalable ») et le critère de mort de la course (« un témoin planté est mal classé ; ou l'étalonnage préalable de la notation échoue »). **Objectif de la course 2 (R-632, R-634) : produire des idées inédites et très plausibles en alignement et contrôle, pas mesurer la performance de l'organisme.** **Ce que le pré-pilote éprouve, instrument par instrument (CP4-01)** : (i) l'obéissance de chacun des trois juges à sa grille figée, sur des témoins nets qui violent chacun un item écrit (M1) — pas la valeur scientifique d'une fiche ; (ii) la détection d'une **redite entre fiches du lot** (paraphrases plantées) par la mémoire anti-redite et la double garde de l'axe 7 (M3) — pas la détection d'une idée déjà publiée ailleurs ; (iii) l'aiguillage des détails concrets avant tout juge (M4) et la tenue de niveau méthode de Kimi (M5) — gardes de sécurité ; (iv) la détection de **références inventées ou altérées parmi les antériorités citées** (M6) — et, si D-g (b), la détection d'une **antériorité publiée non citée** sur 4 fiches (M6b, réserve) ; (v) la consommation (M7), les cloisons du tableau minimal (M8) et la chaîne de bisociation sur une paire par bras (M9). **Il n'éprouve pas** : la détection d'une antériorité non citée hors M6b, « très plausible » au sens des tests de mort (étage hors du pré-pilote, DEP11), ni aucun taux de fausse élimination d'une bonne idée. « Inédit » reste, dans la course, porté par l'antériorité vérifiée sur PDF (R7) et « très plausible » par les tests de mort (R-632). Instruments : analyseur programmé (étage 1) ; trois juges de l'étage 2 (Kimi K3.1 Pro et Argon en notation croisée, Opus 5.5 troisième juge sur toutes les fiches ; R-577, R-578) ; mémoire anti-redite ; double garde de l'axe 7 ; aiguilleur des détails concrets (R-575) ; vérification d'antériorité par Claude (R-573) ; garde de niveau méthode chez Kimi proposeur (R-567) ; tableau minimal partagé et ses cloisons (R-598) ; module de bisociation exploratoire à trois bras — méta (R-638, R-639, annexe), Gu-Krenn (R-619, R-635, R-636, D-j), basique (R-601, R-642, R-643).

**Hypothèses d'instrument** (chacune se réfute par un seuil de « Seuil » ; H-PP8 et H-PP9 sont descriptives pour l'effet) :
- H-PP1 (juges) : chacun des trois juges, appliquant sa consigne figée, sépare les témoins notables (P) des témoins qui violent un item écrit (N1 à N4), et les trois s'accordent.
- H-PP2 : **retirée** (R-634).
- H-PP3 (redite) : la mémoire anti-redite et la double garde de l'axe 7 détectent les paraphrases plantées **du lot** sans écarter les idées distinctes.
- H-PP4 (aiguillage) : l'aiguilleur repère les fiches « trop concrètes » (par classe) et laisse passer les fiches de niveau méthode, vocabulaire dense compris.
- H-PP5 (débordement) : Kimi proposeur, servi comme dans la course, ne déborde pas le niveau méthode au-delà de S12.
- H-PP6 (antériorité) : la vérification détecte les références inventées et altérées sans refuser les réelles ; **si D-g (b)** : elle nomme l'antériorité publiée non citée sur au moins S30 des 4 fiches de M6b (réserve, hors porte).
- H-PP7 (consommation) : la consommation mesurée reste dans S16 du devis (v3 ; v4 quand il est rendu).
- H-PP8 (tableau minimal, descriptive pour l'effet ; décisive pour les cloisons) : le tableau ne traverse jamais les cloisons (texte, bras) ; le taux de redites de la passe « tableau » est rapporté (compte, non mesure d'effet).
- H-PP9 (bisociation, descriptive pour l'effet ; décisive pour la chaîne) : la chaîne paire → fusion → aiguilleur → juges fonctionne pour chacun des trois bras produits ; « concept » se lit avec un accord suffisant (S24) ; « niche » et « structure » se lisent avec un accord suffisant (S28, annexe) ; la règle Gu-Krenn (modèle ou substitut inspiré) s'applique à nos fiches (couverture S27, réserve).

**Hypothèses de travail** (limites déclarées) : (A1) la qualité plantée est celle du squelette ; le rendu ne la change pas (ancres, couples de défaut, relecteur). (A2) Opus 5.5 a une préférence de style inconnue entre rendus de Kimi, d'Argon et de T : il ne sert pas de référence neutre ; sans M2, aucun écart de sévérité n'est estimé (déclaré). (A3) Les témoins ressemblent aux fiches réelles par la forme (S18), pas par la difficulté : l'accord sur témoins surestime l'accord sur fiches serrées (course 1 : 0,12, R-811). (A4) L'étage 2 ne note que la cohérence entre champs ; le pré-pilote mesure l'obéissance des juges à cette grille, rien sur la valeur scientifique d'une fiche (la classe C le rend visible). (A5) Les classes sont définies par l'item K violé et les deux champs en cause, pas par le style. (A6) Aucune des trois règles de bisociation n'a de verdict sur nos fiches (R-601, R-619, R-638) : ce qui en sort est exploratoire ; la règle Gu-Krenn vient d'un graphe de concepts arrêté à leur coupure et s'applique ici hors de son domaine d'apprentissage, **sans reproduction préalable — LECTURE À CONFIRMER (D-j, marqueur en « Seuil ») : c'est la recommandation de R-635, que Lazar n'a pas tranchée en mots ; il a gardé Gu-Krenn comme bras (R-638, R-643) sans répéter la condition** ; le pire cas est une fusion inutile, filtrée par l'aiguilleur, les juges, l'antériorité et, dans la course, les tests de mort ; les paramètres du bras méta sont une conjecture fixée à la main dans l'annexe et approuvée par Lazar (R-638 : « les bons paramètres » sont l'objet du programme ; la transition de phase est une hypothèse, pas un paramètre — **« transition de phase » suspendue jusqu'à E2′, retirée si E2′ échoue (R-878 point 4, décision de Lazar du 31 octobre) ; aucune règle, aucun seuil ni aucune prédiction de ce préenregistrement n'en dépend**). (Les six garde-fous de bisociation de R-878 point 1 sont situés dans « Contre-lecture », VB9-11.) Les paramètres du substitut inspiré de Gu et Krenn sont le seuil S31, conjecture déclarée SUPPOSÉ. (A7) Chaque témoin étant rendu par un seul metteur en forme (**lecture de l'auteur du brouillon 4 de R-634 : 28 fonds rendus une fois, LECTURE À CONFIRMER, D-i, marqueur en « Seuil »**), un juge note parfois un rendu de son propre fournisseur : l'auto-préférence n'est **ni mesurée ni rapportée** (M2 retirée ; CP4-14) ; elle est équilibrée par le tirage des metteurs en forme par classe.

## Prédiction chiffrée et signe attendu

Écrites avant toute lecture ; aucune n'est visée comme résultat positif (R3). Fourchettes : intervalles de croyance à 80 % de l'auteur, sans donnée de la course 2.

| N° | Mesure | Prédiction (signe, valeur) | Réfutation |
|---|---|---|
| P1 | M1, exactitude équilibrée (P contre N) | Opus 0,90 [0,80 ; 0,97] ; Argon 0,85 [0,70 ; 0,95] ; Kimi 0,80 [0,65 ; 0,92] (Kimi a échoué à un témoin en course 1, R-827) | un juge sous S3 |
| P2 | M1, par classe | rappel des N : N3 0,85 et N1 0,85 > N4 0,70 > N2 0,60 [0,35 ; 0,80] ; rejet des C (hors consigne) 0,30 [0,10 ; 0,60] | N2 ≥ N3 chez deux juges au moins |
| P3 | M1, accord | kappa de Fleiss 0,55 [0,35 ; 0,75] sur les témoins primaires | kappa sous 0,45 |
| P4, P5 | M2 | **retirées** (R-634) | — |
| P6 | M3, mémoire | rappel global 0,85 (lexical 0,98, structurel 0,90, conceptuel 0,60) ; fausses alertes en vérification 0,06 [0,02 ; 0,15] ; si D-i (2) ou (3) : les ≈ 2 paires inter-fournisseurs de vérification sont vues avec 0,90 chacune (descriptif) | rappel < S8 ou fausses alertes > tolérance S7 |
| P7 | M3, axe 7 | table seule (verdict d'Opus) 0,50 ; bardeaux seuls 0,60 ; union 0,75 [0,50 ; 0,90] ; fausses alertes de l'union 0,10 | union sous S9 |
| P8 | M4, aiguilleur | rappel 0,92 [0,75 ; 1,00], plus faible en C4 (0,80) ; fausses alertes sur 34 fiches de niveau méthode 0,03 ; sur 6 difficiles 0,20 [0,05 ; 0,40] | rappel < S10 ou fausses alertes > S11 |
| P9 | M5, Kimi (≤ 20 fiches) | taux vrai 0,05 [0 ; 0,20] ; lu « conforme » avec 0,92 (sensibilité 0,90 et fausses alertes 0,03 par lecteur, SUPPOSÉ ; script v9, graines v4 ; M5 ne dépend pas des coûts) ; au moins une fiche en désaccord entre les deux lecteurs avec 0,73 | taux > S12 |
| P10 | M6, antériorité | inventées 0,95 ; altérées 0,70 ; fausses alertes 0,08 ; récentes (après le 30 juin 2026, SUPPOSÉ postérieur à la coupure) 0,10 à 0,15 sous les anciennes ; **M6b (si D-g (b))** : antériorité non citée nommée 0,60 [0,25 ; 0,90] par fiche, soit « 3 sur 4 au moins » avec 0,475 (sortie v9, CP5-11) ; **si M6 est réduite (4 fiches, 6 inventées, 3 altérées, 11 réelles)** : mêmes taux, lus sur l'effectif réduit | sous S13, S14 ou au-dessus de S15 ; M6b sous S30 : réserve |
| P11 | M7, consommation (mesuré ÷ supposé) | Kimi juge 1,4 [0,8 ; 3,0] ; Argon 1,0 [0,7 ; 1,5] ; Opus 1,0 [0,8 ; 1,4] ; antériorité 1,2 [0,6 ; 3,0] ; aiguilleur 1,0 [0,5 ; 2,0] ; passe de Kimi 1,2 [0,6 ; 3,8] ; fusion 1,0 [0,4 ; 2,3] sur la base observée 0,204 (devis v6 § 2.4 ; 1,3 [0,5 ; 3,0] sur la base 0,40 jusqu'au brouillon 9) | un ratio > S16 : devis refait |
| P12 | Contrôles de forme | S18 : aire 0,62 [0,45 ; 0,80], respect avec probabilité 0,8 par version ; S19 : aire 0,55 [0,35 ; 0,75] | aire > S18 ou > S19 |
| P13 | M8, tableau minimal | **une seule prédiction (CP4-08)** : redites de la passe « tableau » contre la passe 1 : 0,10 [0 ; 0,30] des fiches ; les doublons internes de chaque passe et les titres repris sont **rapportés sans prédiction** ; aucune traversée de cloison | une traversée de cloison |
| P14 | M9, bisociation | les 3 fusions passent l'aiguilleur (0,9 chacune) ; 1 sur 3 jugée notable par Opus [0 ; 3], **sans signe prédit entre bras** ; accord des lecteurs de concepts 0,45 [0,25 ; 0,65] ; accord des lecteurs de niches (kappa) 0,5 [0,2 ; 0,8] ; couverture Gu-Krenn 0,5 [0,2 ; 0,9] ; croyance que le modèle de Gu-Krenn tourne à É0 : 0,3, sinon substitut inspiré ; **paires dans le profil du bras méta (CP4-06)** : médiane 1 à 6 fiches non aiguillées (zéro avec 0,31), 3 à 10 fiches (zéro avec 0,03) **sous des paramètres FICTIFS** (script v9, graines v5 : grille à 6 niches, communication faible 0,5, structure forte 0,3, bande 0,6 — aucun n'est celui de l'annexe) ; **cette prédiction est refaite par l'auteur de l'annexe avec les paramètres réels de l'annexe, le script rejoué sur eux, avant le scellement de l'annexe (garde 22a ; CP5-07)** ; la valeur refaite remplace celle-ci au gel ; **si zéro paire dans le profil**, la paire méta vient de la règle de repli de l'annexe, est comptée « hors profil », et le pré-pilote n'a éprouvé que le repli : réserve écrite dans tout résultat du bras ; croyance « hors profil » 0,3 [0,05 ; 0,6] | accord des concepts < S24 ; accord des niches < S28 |
| P15 | Porte (conjonction C1 à C14) | S17 gelé (50 ; 45), relais et bases de coût du devis v6 entières ; texte de base : ouverte d'emblée 0,175 ; complément proposé 0,197 ; nœud d'emblée 0,628 ; ouverte au total 0,240 si le complément reçoit son GO ; **configuration retenue (D-g b, D-i 2) : 0,173 ; 0,196 ; 0,631 ; 0,239** ; 0 au défaut R-819 (script v9) | sans objet : l'issue se lit sur la table « Porte » |

**Réfutation d'ensemble.** (i) Un juge sous S3, ou l'accord sous le plancher de S4 : la porte reste fermée (C1 à C3). (ii) **Rejet des C ≥ spécificité sur N − 0,10 chez chacun des trois juges** (CP2-03) : les juges notent la valeur et non la grille ; C3 non satisfaite, audit R4 et nœud. Aucun autre chemin ne décide de la porte hors de la table « Porte ».

[…]
## Seuil

Seuils : conditions de décision écrites avant toute lecture. Le pré-pilote a des effectifs petits : il écarte les échecs grossiers, ne certifie pas les valeurs fines. Les chiffres qui suivent viennent de `calcul-puissance-pre-pilote-course-2-v9.sortie.txt` (`abc05120a5dd1725a478bc00fa9aeffcd96db66a90fea8588533854603d66c88`) pour M1, le complément, la porte entière, l'issue attendue, C5 à C13, C14, les coûts, les configurations, les variantes de D-i, M6b et la bisociation ; de la sortie v2 (`1c0e702d…`) pour les erreurs-types des aires ; les chiffres marqués « brouillon 9 » viennent de la sortie v8 (`1bfa627a…`), que la ligne (d) de la décomposition de la v9 retrouve ; ceux marqués « brouillon 8 » (bases du devis v3), de la ligne (a) (rec-b8) ; ceux marqués « brouillon 5 », de la sortie v5 (`d342b569…`). Aux valeurs retenue et au S17 gelé ; si Lazar gèle d'autres valeurs, le script est rejoué (paramètres en tête) et la sortie nouvelle fait foi. **Deux configurations sont chiffrées côte à côte : le texte de base (D-g a, D-i 1) et la configuration retenue (D-g b, D-i 2), toutes deux à S17 = 50 ; 45 (gelé, GO-2026-10-31-03), sous les relais ET les bases de coût du devis v6 entières (R-698 ; brouillon 10)** (CP5-05).

**Puissance de M1 (par juge, 28 fonds rendus une fois, fiches indépendantes ; sortie v9, identique aux v4 à v8 : M1 ne dépend pas des coûts)** : juge vrai à 0,90 : étalonné 0,92, défaillant 0,01 ; 0,85 : 0,75 et 0,04 ; 0,80 : 0,50 et 0,13 ; 0,75 : 0,29 et 0,30 ; 0,70 : 0,14 et 0,50 ; 0,60 : 0,02 et 0,84 (plan apparié du brouillon 3 : 0,89 / 0,71 / 0,52 / 0,33 / 0,19 / 0,05 : l'indépendance des fonds rend la lecture un peu plus nette à 0,90 et 0,85, sans différence à 0,80 ; variante (3) de D-i, 24 fonds dont 4 doublés : 0,91 / 0,73 / 0,50, graines nouvelles, ±0,01). Avec exclusion de témoins ambigus (P 8, N 10) : 0,90 / 0,71 / 0,50. **Porte des juges seule (C1-C2)** : tous à 0,90 : ouverte 0,85, complément 0,13 ; tous à 0,85 : 0,54 et 0,31 ; tous à 0,80 : 0,22 et 0,32 ; prédiction P1 : 0,38 et 0,42 ; Kimi à 0,70 et les autres à 0,90 : 0,13. **Complément** (cumul P 22, N 25, mêmes seuils) : juge à 0,90 étalonné au total 0,99 ; à 0,85 : 0,88 ; à 0,80 : 0,63 ; à 0,70 (faux succès) 0,14 → 0,16. **Erreurs tolérées** (estimation ponctuelle) : S13 aucune sur 9 ; S14 deux sur 9 ; S15 deux sur 22 ; S11 trois sur 34 ; S7 vingt-cinq sur ≈ 250.

**Probabilité de la conjonction entière (CP2-01 ; sortie v9, bases de coût du devis v6 entières).** Hypothèses : juges comme ci-dessus ; chaque autre condition indépendante des juges et des autres conditions (SUPPOSÉ) ; concrets de l'aiguilleur écrits (sinon 0) ; **C6, C8 et C9 sont mélangées à la probabilité du sacrifice qui les touche (CP5-02), coupures de relais comprises (brouillon 8)**.

| Condition | Hypothèse (source) | Texte de base (D-g a, D-i 1) | Configuration recommandée (D-g b, D-i 2) |
|---|---|---|
| C1-C2 | P1 : Opus 0,90 ; Argon 0,85 ; Kimi 0,80 | 0,38 | 0,38 |
| C3 | accord et réfutation (ii), même simulation ; rejet des C 0,30 (P2) | 0,91 (C1-C3 0,37) | idem |
| C4 | programme éprouvé en É0 (SUPPOSÉ) | 0,97 | 0,97 |
| C5 | P12 (aires 0,62 et 0,55 ; erreurs-types 0,09 et 0,12) ; ambiguïté 0,10 par témoin (SUPPOSÉ) ; deux versions au plus | 0,57 par version ; 0,81 en deux versions | idem |
| C6 | P6 (≈ 9 positifs de vérification, PB seules ; ≈ 11 sous D-i (2)), P7 ; **table seule retirée avec 0,116 (0,124), dont coupée par son relais 0,043 (0,043) → axe 7 aux bardeaux seuls, C6 0,81 (0,83) dans ce cas** | 0,952 sans retrait ; **0,936 mélangée** | 0,970 ; **0,952 mélangée** |
| C7 | P8 (0,96 en C1 à C3, 0,80 en C4, SUPPOSÉ) ; nouvel essai lu seul | 0,85 (direct 0,66 ; à corriger 0,31) ; **0 au défaut R-819** | idem |
| C8 | P9 (taux 0,05) ; sensibilité 0,90 et fausses alertes 0,03 par lecteur (SUPPOSÉ) ; **passe « tableau » retirée avec 0,533 (0,534), dont coupée par son relais 0,505 (0,486) → M5 sur 10 fiches, C8 0,91** | 0,92 ; **0,914 mélangée** | 0,914 |
| C9 | P10 (inventées 0,95) ; **M6 réduite avec 0,186 (0,239), dont M6 entière coupée par son relais puis lue réduite 0,058 (0,054) → 6 inventées, C9 0,97 dans ce cas** | 0,99 ; **0,987 mélangée** | 0,986 |
| C10 | P11 (rapports log-normaux) ; devis v3 § 3 (bases de la course non changées par R-698 ni par le brouillon 10 : fusion 0,40 comprise) ; course à trois bras, **24 fusions (GO-2026-10-31-04)** ; **reste = 160 − dépense réelle du pré-pilote** (GO-2026-10-31-04, pré-pilote compris) ; **sur le chemin « après complément » (complément certain) : reste = 160 − dépense − complément** ; sensibilité : devis de la course mis à l'échelle de la médiane tirée du devis v6 (×1,175 ; médiane 134,9 USD), sans complément : 0,992 (tient à 4 : 0,32 ; à 3 : 0,46 ; à 2 : 0,21 ; à aucune 0,008) ; **devis v6 § 5, à 160, lecture B : sans complément 0,246 ; 0,556 ; 0,191 ; 0,007 (C10 0,993), appariement exact de ma lecture sans complément, que la sensibilité d'échelle rejoint ; avec complément proposé avec 0,20, coût tiré, 0,213 ; 0,550 ; 0,227 ; 0,010 (C10 0,990), sans équivalent exact ici (VB8-04, VB9-05)** | **0,999** (tient à 4 sous-sessions 0,60 ; à 3 : 0,32 ; à 2 : 0,07 ; à aucune 0,001) ; après complément certain 0,993 | 0,999 (0,57 ; 0,35 ; 0,08) ; après complément 0,992 |
| C11 | programme éprouvé en É0 (SUPPOSÉ) | 0,99 | 0,99 |
| C12 | garde de paire 0,99 ; n < 3 fiches non aiguillées 0,02 ; annexe non conforme à É0 0,03 ; bras Gu-Krenn non produit 0,10 ; bras basique 0,01 (tous SUPPOSÉ ; CP5-01, CP5-13) ; deux bras ou plus non produits 0,024 | **0,97** (0,99 au brouillon 5) ; sous D-h (b) : 0,86 | idem |
| C13 | arrêts clos : 0,95 (SUPPOSÉ) ; budget : **règle d'A1 étape par étape, ordre du Plan, M6 jamais retirée entière, relais ET bases de coût du devis v6 entières (protégées souples, retirables fixes)**, plafond 50, arrêt d'étape 45, seconde version de témoins comprise ; « non mesuré (budget) » 0,052 (0,074) : **étape protégée non lancée 0,016 (0,013) ; étape protégée coupée par son relais, M6 comprise, 0,046 (0,072) ; dont M6 non mesurée 0,022 (0,021)** ; sans arrêt d'étape : 0,941 (0,923) | 0,95 × **0,948** | 0,95 × **0,926** |
| C14 | déclencheurs : M1 0,11 ; relecteur à 100 % 0,09 ; contradiction lecture primaire / chaîne 0,05 (SUPPOSÉ) ; « trop propre » M3 ≈ 0, M4 0,009, M6 0,004 (CP4-10, CP5-10) ; audit concluant à un artefact 0,15 (SUPPOSÉ) | 0,96 | 0,96 |
| **Conjonction entière** | produit (hors juges : 0,48) ; complément selon la règle des Critères | **0,175 d'emblée** ; complément proposé 0,197 ; nœud d'emblée 0,628 ; **0,240 au total après complément** ; 0,19 aux coûts de base ; 0 au défaut R-819 (brouillon 9, quatre bases de R-698 : 0,170 ; 0,192 ; 0,638 ; 0,235 ; brouillon 8, bases du devis v3 : 0,184 ; 0,207 ; 0,609 ; 0,253) | **0,173 d'emblée** ; complément 0,196 ; nœud 0,631 ; **0,239 au total** (brouillon 9 : 0,167 ; 0,189 ; 0,644 ; 0,230) |

Autres cas (texte de base ; porte des juges seule → conjonction entière d'emblée) : tous les juges à 0,90 : 0,85 → 0,39 ; à 0,85 : 0,54 → 0,25 ; à 0,80 : 0,22 → 0,10 ; Kimi à 0,70, autres à 0,90 : 0,13 → 0,06. Sensibilités à la prédiction P1 : arrêts clos à 1,00 → 0,18 ; aucun audit concluant à un artefact → 0,18 ; artefact à 0,30 → 0,17 ; C12 à 0,99 (brouillon 5) → 0,18 ; course à 12 fusions (C10 1,000) → 0,175 ; ancien total « 110 − dépense » (GO-2026-10-30-07, remplacé ; information) : 24 fusions (C10 0,794) → 0,139, 12 fusions (0,891) → 0,156 ; devis de la course à l'échelle du devis v6 (C10 0,992) → 0,173. **Ordres d'étapes (CP5-04, information)** : ordre joué par le script v5 → 0,174 (C13 budget 0,947) ; ordre du brouillon 4 → 0,171 (0,932) ; **M6 jouée juste après É1, sa seule dépendance (option de plan non retenue, à la décision de Lazar si elle l'intéresse)** → 0,173 (C13 budget 0,946 ; M6 réduite 0,067, toujours par coupure de son relais ; fusions retirées 0,181, table seule 0,186). **Couple 45 ; 40 sous les mêmes relais souples (information : l'alternative que Lazar n'a pas retenue)** : C13 budget 0,8755 (0,8305 retenue), porte d'emblée 0,159 (0,152), complément 0,179 (0,172), nœud 0,662 (0,676), au total 0,219 (0,210) ; un sacrifice ou une réduction avec 0,66 (0,68) (fusions retirées 0,28, M6 réduite 0,33, table seule 0,21, passe « tableau » 0,54). **Modèle des relais (information)** : modèle « réservation » du brouillon 7 à 50 ; 45 → 0,168 (C13 budget 0,911 ; sacrifice 0,22 : M6 réduite 0,21, fusions 0,15, table seule 0,15) ; tous les relais fixes → 0,001 (une étape protégée coupée avec 0,994 ; C13 budget 0,006) ; **tous les relais souples, retirables compris (hors GO-2026-10-31-03)** → 0,167 (C13 budget 0,905 ; sacrifice 0,22 : fusions 0,15, passe « tableau » 0,11, table seule 0,14). **Lecture** : même si les trois juges étaient justes à 0,90, la porte ne s'ouvrirait d'emblée qu'avec 0,39 ; l'issue attendue reste un nœud.

- **S1** — À REMPLIR — à geler par Lazar. Exactitude équilibrée minimale de chaque juge. 
- **S2** — À REMPLIR — à geler par Lazar. Rappel minimal sur P. 
- **S3** — À REMPLIR — à geler par Lazar. Plancher d'échec (strictement inférieur). 
- **S4** — À REMPLIR — à geler par Lazar. Accord : Fleiss minimal ; Cohen minimal par couple ; plancher d'échec. 
- **S5** — **retiré** (R-634).
- **S6** — À REMPLIR — à geler par Lazar. Fidélité du rendu : ancres conservées ; couples de défaut co-présents ; défaut vu par le relecteur. 
- **S7** — À REMPLIR — à geler par Lazar. Fausses alertes de la mémoire : visée au calibrage ; tolérée en vérification. 
- **S8** — À REMPLIR — à geler par Lazar. Rappel global minimal de la mémoire en vérification. 
- **S9** — À REMPLIR — à geler par Lazar. Union de la double garde de l'axe 7 : rappel minimal ; fausses alertes maximales. 
- **S10** — À REMPLIR — à geler par Lazar. Aiguilleur : rappel minimal sur les concrets écrits, avec aucun oubli dans les classes écrites parmi C1 et C2 ; bas de la bande « à corriger ». 
- **S11** — À REMPLIR — à geler par Lazar. Fausses alertes maximales de l'aiguilleur : 34 fiches de niveau méthode ; 6 difficiles. 
- **S12** — À REMPLIR — à geler par Lazar. Débordement maximal de Kimi proposeur (≤ 20 fiches). 
- **S13** — À REMPLIR — à geler par Lazar. Rappel minimal sur références inventées. 
- **S14** — À REMPLIR — à geler par Lazar. Rappel minimal sur références altérées. 
- **S15** — À REMPLIR — à geler par Lazar. Fausses alertes maximales sur références réelles. 
- **S16** — À REMPLIR — à geler par Lazar. Rapport maximal coût mesuré ÷ coût supposé, par poste. 
- **S17** — **gelé par Lazar : plafond 50 USD ; arrêt d'étape 45 USD** (GO-2026-10-31-03, `registres/go.md` de `origin/main`, l. 168 : « pré-pilote de la course 2 : plafond 50 USD (arrêt d'étape 45 ; plafonds de relais du brouillon 5 gardés, souples pour les étapes protégées : devis v6 […]) » ; mot direct de Lazar, 31 octobre 2026 ≈ 06:37 UTC, verbatim « Pré-pilote : je recommande 50 USD plutôt que 45. : ok »). Un seul plafond et un seul arrêt d'étape ; aucun repli (CP4-07) ; la ligne de GO existe (échéance 2026-11-07 ; A15). **Modèle des relais (même ligne ; devis v6, § 3.3)** : plafonds de relais du brouillon 5 (tableau de coût du Plan) ; au lancement d'une étape protégée, plafond de son relais = max(plafond de l'étape ; S17 − cumul − attendu aux bases des étapes restantes non retirées) ; étape retirable : plafond fixe ; règle d'A1 du Plan. **Ce que donne ce couple (sortie v9, bases de coût du devis v6 entières, rapports P11, texte de base ; recommandée entre parenthèses)** : dépense médiane 37,6 USD (40,1), quantile 90 % 46,4 (48,0), jamais plus de 50 ; « non mesuré (budget) » d'une mesure de C1 à C9 : 0,052 (0,074) — étape protégée non lancée 0,016 (0,013), étape protégée coupée par son relais, M6 comprise, 0,046 (0,072), dont M6 non mesurée 0,022 (0,021) ; souplesse utilisée (une étape protégée va au-delà de son plafond de relais sans être coupée) 0,994 (0,996) ; un sacrifice ou une réduction 0,63 (0,64) : fusions 0,16 (0,20), M6 réduite 0,19 (0,24), table seule 0,12 (0,12), passe « tableau » 0,53 (0,53) — **dont étape retirable coupée par son relais fixe 0,56 (0,54) : passe « tableau » 0,505 (0,486), fusions 0,075 (0,070), table seule 0,043 (0,043)** ; arrêt d'étape touché 0,17 (0,26), il réduit ou retire quelque chose avec 0,050 (0,038) ; M6b non lancée ou coupée 0,033 (réserve). **Effet de l'arrêt d'étape à 45** : C13 budget 0,948 contre 0,941 sans arrêt (0,926 contre 0,923) ; table seule retirée 0,116 contre 0,085 ; porte 0,175 contre 0,174 : effet petit, de même sens qu'au brouillon 7 (CP5-06). **Écart avec le devis v6, décomposé base par base (R-698 ; VB8-03 ; VB9-03, VB9-04).** Le devis v6 (§ 3.3, configuration retenue, 50 ; 45) donne sacrifice 0,17, fusions 0,12, non lancée 0,021, coupée 0,063, dépense médiane 40,6. Au sens du devis (sacrifice sans les coupures de relais ; « coupée » = étape protégée, M6b comprise, M6 non comprise, M6 étant sacrifiable au devis), la décomposition de la configuration retenue est : (a) bases du brouillon 8 (devis v3) — sacrifice 0,103, fusions 0,052, non lancée 0,010, coupée 0,027, médiane 38,0 ; (b) + 60 lectures d'étiquettes (1,5 USD au lieu de 0,75 : le devis § 3.2 relève que le brouillon 5 ne comptait qu'un lecteur) — 0,121 ; 0,065 ; 0,013 ; 0,032 ; 38,8 ; (c) + coupures de Kimi ×1,447 (§ 2.3) **[les deux principales : porte 0,169, C13 budget 0,9035, l'annonce de R-698, vérifiée ; VB9-17]** — 0,274 ; 0,178 ; 0,036 ; 0,112 ; 42,6 ; (d) + prix de Sonnet pour T (§ 3.4 pt 5) et seconde version 5,8 (§ 3.4 pt 4) = les quatre bases de R-698 = brouillon 9 — 0,274 ; 0,185 ; 0,035 ; 0,120 ; 42,3 ; (e) + fusion observée 0,204 seule (§ 2.2, § 2.4) — 0,243 ; 0,170 ; 0,032 ; 0,110 ; 41,5 ; (e') + rédacteur au prix de Sonnet seul (§ 3.2) — 0,219 ; 0,143 ; 0,025 ; 0,096 ; 41,0 ; **(f) les deux = bases du devis v6 entières (ce brouillon) — 0,195 ; 0,130 ; 0,023 ; 0,083 ; 40,1**. Écart absolu au devis, de (a) à (f) : sacrifice 0,067 ; 0,049 ; 0,104 ; 0,104 ; 0,073 ; 0,049 ; **0,025** ; coupée 0,036 ; 0,031 ; 0,049 ; 0,057 ; 0,047 ; 0,033 ; **0,020** ; médiane 2,6 ; 1,8 ; 2,0 ; 1,7 ; 0,9 ; 0,4 ; **0,5**. Les quatre bases de R-698 seules faisaient dépasser le devis (VB9-03) ; les six ensemble rapprochent chacun des cinq indicateurs du devis plus que les bases du brouillon 8, sans l'atteindre exactement. **Le reste (+0,025 sur le sacrifice, +0,020 sur « coupée ») n'est pas attribué : le script du devis n'est pas rejoué ici** ; deux différences de modèle sont connues, non mesurées : le devis tire les coupures de Kimi appel par appel (§ 2.4), ce script les compte par un facteur constant ×1,447 sur la dépense de chaque poste de Kimi ; M6b est répartie autrement (É9b 1,4 au devis ; lecture des PDF 0,40 en É1 et vérificateur 1,0 en É9b ici, même total). Coïncidence levée (brouillon 9) : le « 0,063 » de « coupée » du devis est sans lien avec « M6 entière coupée puis lue réduite » (0,058 texte de base, 0,054 retenue). **Ce que le devis ne compte pas** : une étape retirable coupée par son relais fixe n'y a aucun statut (sa dépense est plafonnée, rien d'autre) ; ce brouillon la dit retirée (aucun repli silencieux, R5) : les sacrifices passent de 0,195 (au sens du devis) à 0,64, surtout par la passe « tableau » (coupée par son relais de 4,6 USD avec 0,49), et la porte n'en bouge presque pas (0,173 ; 0,164 si tous les relais étaient souples, hors GO). Le total séquencé est fixé par GO-2026-10-31-04 (160 USD ; L4 sans objet).
- **S18** — À REMPLIR — à geler par Lazar. Aire maximale témoins contre fiches de Kimi ; effectif minimal de fiches de Kimi non aiguillées pour l'évaluer (CP2-07). 
- **S19** — À REMPLIR — à geler par Lazar. Aire maximale P contre N par la forme. 
- **S20** — À REMPLIR — à geler par Lazar. Témoins ambigus tolérés parmi les 23 primaires ; effectifs primaires minimaux. 
- **S21** — À REMPLIR — à geler par Lazar. Tableau minimal : longueur maximale d'un titre ; d'un résumé. 
- **S22 (hors gel de ce préenregistrement, CP2-10 iii)** — paramètre de la course 2 (v53), **fixé par Lazar dans GO-2026-10-31-04 : trois bras, 24 fusions** (lecture B du devis v6 : une paire par bras et par proposeur dans chaque sous-session ; la recommandation « k = 1 » du brouillon 7, 12 fusions, est sans objet). C10 est jouée à 24 fusions (≈ 17 USD de bisociation aux bases du devis v3, que le modèle de coût de la course garde) ; à 12 fusions, pour information, la course tiendrait à 4 sous-sessions avec 0,77 au lieu de 0,60 (reste = 160 − dépense, sortie v9).
- **S23** — À REMPLIR — à geler par Lazar. Bisociation dans le pré-pilote : k paires par bras. 
- **S24** — À REMPLIR — à geler par Lazar. Accord minimal des deux lecteurs d'étiquettes de concepts (Jaccard moyen par fiche ; bras basique). 
- **S25** — À REMPLIR — à geler par Lazar. Règle Gu-Krenn (modèle) : nombre m de meilleures paires de concepts. 
- **S26** — **retiré sous D-j « oui »** (la reproduction n'est plus une condition d'usage ; elle continue chez session-depot comme validation, sous son propre préenregistrement). Si D-j « non » (marqueur de D-j ci-dessous), S26 revient (écart maximal d'aire sous la courbe, à fixer) et le bras Gu-Krenn attend la reproduction, comme le disait R-634.
- **S27** — À REMPLIR — à geler par Lazar. Règle Gu-Krenn : part minimale des fiches non aiguillées notables par la règle. 
- **S28** — À REMPLIR — à geler par Lazar **sur proposition de l'annexe du bras méta** (son auteur propose la valeur, le contre-lecteur de l'annexe, modèle différent, la contre-lit, Lazar l'approuve par un mot ; sans ce mot l'annexe n'est pas scellée ; CP5-07). Accord minimal des deux lecteurs de niches et de structures : kappa de Cohen sur la niche ; Jaccard moyen sur les structures (règle de S24). **Aucune valeur retenue ici** : la grille n'existe pas encore et la valeur dépend de sa finesse ; repère : S24 (0,40). **Règle à marges constantes (CP4-06)** : si chaque lecteur pose une seule étiquette sur toutes les fiches, le kappa n'est pas défini ; il est lu 1 si les deux étiquettes coïncident, 0 sinon, et la grille est marquée « dégénérée sur ce lot » (réserve) ; à 10 fiches, l'erreur-type du kappa est de l'ordre de 0,3 (SUPPOSÉ) : garde grossière. Conséquence d'un accord sous S28 : grille « illisible », bras méta marqué « niches non lisibles » ; options hors porte ; **le bras n'est pas retiré** (R-638).
- **S29** — À REMPLIR — à geler par Lazar **sur proposition de l'annexe du bras méta** (même mécanisme que S28 ; CP5-07). Paramètres du bras méta, version 1 : (a) grille fermée des niches et des types de structure ; (b) source de la communication entre niches et seuil « faible » ; (c) nombre et type minimaux de structures partagées pour « forte » ; (d) bande d'éloignement [e_min ; e_max] et échelle ; (e) forme et poids du score ; (f) règle de repli hors profil. **Tous SUPPOSÉ ; spécification après les verdicts des collisionneurs (R-638) ; annexe contre-lue, scellée, empreinte écrite ici avant le gel ; aucune fiche lue par son auteur ; l'annexe refait la prédiction P14 avec ses paramètres (garde 22a).** Non conforme à É0 : A20 (bras méta seul). **L'ancien (g), paramètres du substitut inspiré de Gu et Krenn, est sorti de l'annexe : c'est S31** (CP5-01).
- **S31** — À REMPLIR — à geler par Lazar. **Paramètres du substitut inspiré de Gu et Krenn** (joués seulement si le modèle de Gu et Krenn ne tourne pas à É0, A19 . **tous SUPPOSÉ ; à essayer sur la moisson, sans aucune fiche, avant le gel : l'essai est empreinté et nommé en tête)** : (i) **source** : la moisson OpenAlex de R-633 (n° 265 : sous-domaine du contrôle des IA et environnements de comparaison), ou le graphe publié de Gu et Krenn s'il est téléchargeable et empreinté avant le gel (lequel : écrit au gel) ; (ii) **vocabulaire** : la liste fermée des étiquettes de concept portées par les œuvres de la source (étiquettes de concept d'OpenAlex telles que la moisson les livre, SUPPOSÉ ; sommets du graphe si la source est le graphe), gardées si elles sont portées par au moins 20 œuvres de la source ; liste empreintée ; **méthode de construction** : programme, aucun jugement humain ni de modèle ; (iii) **règle de correspondance (CP5-13)** : un concept est « dans une œuvre » si l'œuvre porte son étiquette dans la source (aucune correspondance de chaînes sur les titres ou résumés) ; un concept est « dans une fiche » si l'un des deux lecteurs d'étiquettes l'a choisi dans la liste fermée (M9) ; si la source ne livre pas d'étiquettes, repli déclaré au gel : correspondance exacte de la chaîne du concept, normalisée (minuscules, accents retirés, pluriel régulier ramené au singulier), dans le titre ou le résumé ; (iv) **« reliées »** : au moins une œuvre de la source portant les deux concepts, publiée entre le 1er janvier 2015 et la **coupure du 30 juin 2026** (SUPPOSÉ : date de coupure des modèles) ; (v) **« actif »** : au moins 5 œuvres portant le concept entre le 1er juillet 2023 et la coupure. Raison : ce sont les traits de Gu et Krenn que R-635 nomme (paires de concepts jamais reliées, chacun actif), à relire sur le PDF empreinté avant le gel (R7) ; les nombres 20 et 5 sont des seuils de bruit, à ajuster sur l'essai de la moisson avant le gel, jamais après. **Ni l'annexe du bras méta ni A20 ne touchent S31** ; si la source n'est pas disponible et empreintée à É0, A19 déclare le bras « non produit (source absente) ».
- **S30 (si D-g (b))** — À REMPLIR — à geler par Lazar. Rappel minimal de M6b (antériorité non citée nommée) sur 4 fiches, **réserve hors porte**. 
- **D-e** — À REMPLIR — à geler par Lazar. Lecture de « domaine » et de « concept » (bras basique). 
- **D-f** — À REMPLIR — à geler par Lazar. Modèles des rôles neufs. 
- **D-g** — À REMPLIR — à geler par Lazar. Antériorité non citée : (a) vide déclaré ; (b) M6b, 4 fiches, étape protégée hors porte É9b, S30 en réserve. 
- **D-h** — À REMPLIR — à geler par Lazar. Gel : (a) attendre l'annexe scellée du bras méta ; (b) geler à deux bras (bras méta ajouté dans la course sous son propre préenregistrement court). 
- **D-i** — À REMPLIR — à geler par Lazar. Plan des fonds : (1) 28 uniques ; (2) 28 + 4 rendus appariés pour la seule mémoire ; (3) 24 dont 4 doublés. 
- **D-j** — À REMPLIR — à geler par Lazar. Gu-Krenn sans condition de reproduction : oui / non. 
- **Lectures à confirmer qui fixent une règle de lecture (CP5-03 ; une ligne chacune ; lectures de l'auteur, aucune n'a été tranchée en mots par Lazar ; aucun défaut)** :
  - **L1** — À REMPLIR — passe « tableau » de Kimi gardée (M8 ; ce que la course fait ; M5 à 20 fiches) : oui / retirée (M5 à 10 fiches, −4,0 USD).
  - **L2** — À REMPLIR — table seule de l'axe 7 gardée (Opus, 0,7 USD, sacrifiable de rang 3) : oui / version réduite aux bardeaux seuls (0 USD ; C6 0,81 au lieu de 0,95).
  - **L3** — À REMPLIR — désaccord d(a, b) hors du score méta (R-638) : oui / entre dans le score (place et poids dans l'annexe).
  - **L4** — **sans objet, tranché par Lazar (GO-2026-10-31-04)** : le total séquencé de la course 2 est de 160 USD, pré-pilote compris ; C10 lit le reste = 160 − dépense réelle du pré-pilote (− dépense du complément s'il a eu lieu) ; les lectures « 110 inchangé » et « 123 » du brouillon 7 sont retirées.
  - **L5** — À REMPLIR — fusions retirées par la règle d'A1 (CP5-02) : C12 lue sur les paires et leurs gardes, fusions « non produites (budget) », réserve « chaîne éprouvée jusqu'à la paire seulement » jointe au verdict, O15 (a) ouverte / C12 « non mesurée (budget) », C13 non satisfaite, nœud.
  - **L6** — À REMPLIR — S27 lu comme réserve, non comme retrait (R-635) : oui / retrait du bras sous S27.
  - **L7** — À REMPLIR — le brouillon 3 n'a pas reçu de contre-lecture (remplacé par le brouillon 4 avant la contre-lecture 3) : accepté / contre-lecture rétrospective exigée.

**Table des marqueurs de remplissage (CP5-03 ; VB9-01, VB9-07).** Chaque décision ouverte porte le marqueur du gabarit (`prereg.MARQUEUR`) une seule fois, dans la ligne qui recevra sa valeur ; la fonction `problemes` de `src/controle_ia/prereg.py` refuse ce marqueur partout dans le fichier, donc aucune mention descriptive ne l'écrit. **Compte sur ce brouillon 10 (recherche exacte du marqueur) : 41 occurrences, toutes des décisions ouvertes : Seuil 39, Rôles, témoins et dépendances 2 ; aucun marqueur de gabarit `<<…>>`.** Validateur lancé sur ce brouillon (`PYTHONPATH=src`, `problemes(chemin)`) : deux messages, « section vide ou à remplir : Seuil » (par ses marqueurs voulus) et « contre-lecture 5 sans ses deux empreintes (brouillon relu et rapport) » (valeur à fournir au scellement) ; rien d'autre. **Deux sortes (VB6-10).** (1) **Décisions de Lazar encore ouvertes, 41**, marqueur du gabarit : Seuil (S1 à S4, S6 à S16, S18 à S21, S23 à S25, S27 à S31, D-e à D-j, L1 à L3, L5 à L7 : 39) ; Rôles, témoins et dépendances (confidentialité, DEP4 ; mot sur l'étalonnage de l'aiguilleur, DEP5 : 2) ; **S17 et L4, tranchés par Lazar (GO-2026-10-31-03, GO-2026-10-31-04), ne portent plus de marqueur (43 au brouillon 7)**. (2) **Valeurs ou faits à fournir au scellement, 6**, qui ne sont pas des décisions de Lazar, portés par le mot distinct en capitales, écrit à ces six endroits seulement : en-tête (commit du code d'analyse ; empreinte de l'annexe ; source et essai de S31 : 3) ; Métrique (k items de la consigne figée ; résumé d'une ligne du tableau minimal : 2) ; Contre-lecture (contre-lecture 5 : 1). Toute mention descriptive l'écrit en minuscules (« à fournir au scellement ») ou dit « le mot distinct » (VB8-11, VB9-07). **Lecture du validateur** : il refuse le marqueur du gabarit partout, mais tant qu'une section exigée le porte, il tait le message « hors des sections exigées » ; les deux marqueurs de « Rôles, témoins et dépendances » (section non exigée) ne sont donc signalés qu'une fois « Seuil » remplie, et le sont alors ; il ne connaît pas le mot distinct : au scellement, une recherche de texte **sensible à la casse** vérifie qu'il n'en reste aucune occurrence en capitales (compte attendu au scellement : 0 ; dans ce brouillon : 6, les six valeurs) ; la contre-lecture 5, une fois le mot retiré de sa section, est exigée par la règle des deux empreintes (brouillon relu et rapport, 64 caractères chacune). La ligne de GO au plafond S17 n'est pas un marqueur : elle existe (GO-2026-10-31-03, DEP6) ; A15 vérifie au lancement qu'elle couvre le plafond et n'est pas échue.

**Règles globales (fixées maintenant).** Bornes unilatérales à 95 % ; aucune correction de multiplicité (la porte est une conjonction ; le risque est une fausse défaillance, déclaré).

[…]
| A15 | décision manquante : confidentialité (fiches vers Moonshot et Google), D-f, D-g à D-j, ou GO de lancement ; **ou ligne de GO au plafond gelé S17 absente ou échue : la ligne est GO-2026-10-31-03 (`registres/go.md` de `origin/main`, 50 USD, échéance 2026-11-07) ; aucun lancement à un autre plafond que 50 USD, ni après le 7 novembre 2026 sans ligne nouvelle** ; ou relais incapable de recevoir, au lancement de chaque étape, le plafond dur calculé par l'orchestrateur selon A1 (garde R5 ligne 11 échouée ; DEP4). La confirmation de la règle « réservation » demandée par le brouillon 7 (VB6-04) est sans objet (modèle du devis v6, GO-2026-10-31-03) | **aucun lancement** |
[…]
- DEP3 : analyseur (étage 1), garde de forme, plongement figé, bardeaux, constructeur de tableau et ses gardes, programme de score du bras basique, liste fermée des concepts, vocabulaire et programme de note Gu-Krenn (modèle, ou substitut inspiré selon S31), programme de score du bras méta, consigne de fusion ; empreintes.
- DEP4 : relais Kimi v3 (1 800 s), adaptateur Kimi (v53, conv-audit), relais d'Argon avec lecture du modèle servi, relais d'Opus et de T ; **chaque relais est lancé, pour chaque étape, avec un plafond dur que l'orchestrateur calcule au lancement selon la règle d'A1 (relais du devis v6, GO-2026-10-31-03 : étape protégée, max(plafond de relais ; S17 − cumul − attendu aux bases des étapes restantes non retirées), formule du Plan, règle d'A1, point 4 ; étape retirable, plafond de relais fixe ; VB8-01) et qui ne change pas pendant l'étape** ; c'est le fonctionnement ordinaire d'un relais plafonné (devis v6, § 3.3 : « le relais reste donc un plafond dur, fixé au lancement ») ; garde R5 lignes 11a et 11b. L'exigence du brouillon 7 (« le relais accepte une réservation dépassée jusqu'à S17 − cumul », à confirmer par session-depot, VB6-04) est sans objet ; **confidentialité** : mot de Lazar pour l'envoi de fiches (inventées) chez Moonshot et Google : À REMPLIR.
- DEP5 : bras d'attaque (12 concrets, aiguilleur, second lecteur, adjudicateur) ; mot de Lazar sur l'étalonnage de l'aiguilleur (défaut R-819 : pas d'étalonnage, qui ferme C7) : À REMPLIR.
- DEP6 : GO de lancement et **ligne de GO au plafond S17 gelé : GO-2026-10-31-03** (`registres/go.md` de `origin/main`, l. 168 : 50 USD ; échéance 2026-11-07 ; « lancement par lignée sur la spécification v53 et le préenregistrement du pré-pilote scellé et contre-lu » ; elle remplace la part « pré-pilote ≤ 32 » de GO-2026-10-30-07) ; total séquencé de la course : GO-2026-10-31-04 (160 USD, pré-pilote compris ; échéance 2026-11-14), qui fixe C10 (L4 sans objet). Un lancement après l'échéance de GO-2026-10-31-03 exige une ligne nouvelle (A15).
- DEP7 : rédacteur, T, relecteur, lecteurs d'étiquettes, auteur et contre-lecteur de l'annexe, sous-agent de verdict neufs, disponibles malgré les limites hebdomadaires.
[…]
## Décisions à Lazar

Format : décision en une phrase ; enjeu ; options (avantage, inconvénient) ; recommandation et confiance ; **aucun défaut**. Ce préenregistrement ne se gèle pas tant qu'une ligne reste sans mot. Le mot de Lazar est consigné dans `registres/decisions.md` et la valeur gelée est écrite à la place du marqueur de remplissage, dans « Seuil » (table des marqueurs) ; le script v9 est rejoué si une valeur diffère de la recommandation. **Tranchés par Lazar le 31 octobre 2026 et retirés de cette section : S17 (50 ; 45, GO-2026-10-31-03) et L4 (sans objet, GO-2026-10-31-04)** ; les autres décisions sont inchangées (options, recommandations, confiances), seuls leurs chiffres sont relus sur la sortie v9 (bases de coût du devis v6 entières). **Configuration recommandée dans son ensemble (chiffrée, sortie v9) : D-g (b), D-i (2), D-h (a), D-j oui, L1 à L3 et L5 à L7 telles que lues par l'auteur, au S17 gelé : coût attendu 32,1 USD, dépense médiane 40,1, porte d'emblée 0,173, complément 0,196, nœud 0,631, au total 0,239 ; C13 budget 0,926 ; M6b non lancée ou coupée 0,033 (réserve).**

**D-g — Antériorité non citée.** *Décision* : accepter que le pré-pilote n'éprouve pas la détection d'une antériorité publiée non citée, ou ajouter 4 fiches à M6 (M6b). *Enjeu* : « inédit » (R-632) n'est éprouvé par aucun instrument du pré-pilote (CP4-01) ; la course s'en remet à la vérification sur PDF après coup et aux tests de mort ; M6b en donne une lecture grossière avant la course. *Options* : (a) vide déclaré — avantage : rien à écrire ni à payer, pas de changement de la consigne du vérificateur ; inconvénient : si le vérificateur ne sait pas nommer une antériorité manquante, on l'apprend après la course. (b) M6b, 4 fiches, rappel S30 = 3 sur 4 en réserve hors porte, **étape protégée hors porte É9b** (CP5-05) — avantage : ≈ 1,4 USD aux bases du devis v6, plafonds de relais 2,3 (2,5 d'ensemble), premier signal sur le vrai sens d'« inédit » ; inconvénients : 4 cas ne bornent rien (4 sur 4 → 0,47 ; « 3 sur 4 au moins » à rappel vrai 0,60 : 0,475), la consigne du vérificateur doit demander l'antériorité manquante (DEP2b, ajout possible à la course), session-depot doit choisir 4 sources à PDF empreinté hors de la vue de conv-audit (DEP2c), et, placée en fin de course, M6b n'est pas lancée ou est coupée avec 0,033 (réserve, C13 inchangée) ; sur la porte : D-g (b) ajoutée à D-i (2) la fait passer de 0,176 à 0,173 (−0,003, sortie v9 ; D-g (b) seule n'est pas jouée) ; M6b alourdit un peu la configuration (son relais É9b est coupé avec 0,023), dans le bruit. 

**D-h — Gel et bras méta.** *Décision* : attendre l'annexe scellée du bras méta pour geler ce préenregistrement, ou geler maintenant à deux bras et ajouter le bras méta dans la course sous son propre préenregistrement court. *Enjeu* : R1 et R2 interdisent de geler avec S28 et S29 vides ou de les remplir après avoir vu des fiches (CP4-02) ; l'annexe dépend des verdicts des collisionneurs (R-638), lancés le 30 octobre (R-630). *Options* : (a) retarder — avantages : le bras méta est éprouvé (chaîne, grille, S28) avant la course ; C12 0,97, porte 0,173 ; inconvénient : le pré-pilote attend l'annexe (verdicts, écriture, contre-lecture, approbation ; quelques jours), mais il attend de toute façon la confidentialité et les concrets (DEP4, DEP5) ; **la ligne de GO du pré-pilote (GO-2026-10-31-03) échoit le 7 novembre : une annexe plus tardive demande une ligne nouvelle**. (b) geler à deux bras (version suivante, retrait des lignes du bras méta ; **désormais applicable : le bras Gu-Krenn ne dépend plus de l'annexe, S31**, CP5-01) — avantage : lancement dès que DEP4 et DEP5 sont levées ; inconvénients : la grille et S28 ne sont pas éprouvées avant la course (la course peut tourner sur une grille illisible pendant toute la génération 1), deuxième préenregistrement à écrire et contre-lire, O15 (c) de fait, **et C12 exige les deux bras restants : 0,86, porte 0,155, nœud 0,670** (sortie v9). 

**D-i — Plan des fonds et paires inter-fournisseurs.** *Décision* : choisir entre 28 fonds uniques, 28 fonds plus 4 rendus appariés pour la seule mémoire, ou 24 fonds dont 4 doublés. *Enjeu* : R-634 retire la mesure d'auto-préférence « dix fonds écrits deux fois » ; le brouillon 4 en a déduit, de lui-même, le retrait de tout appariement et donc des paires inter-fournisseurs PA de la mémoire anti-redite (CP4-03) — un instrument d'« inédit », pas une mesure de l'organisme. *Options (sortie v9, bases de coût du devis v6 entières, prédiction P1, D-g a, S17 gelé 50 ; 45, relais souples)* : (1) 28 uniques — 30,1 USD, PA 0, C6 0,936 (sous retraits), porte 0,175, au total 0,240 ; avantage : fiches indépendantes, texte actuel ; inconvénient : la détection d'une même idée rendue par deux fournisseurs n'est pas éprouvée, alors que la course a plusieurs proposeurs. (2) 28 + 4 rendus appariés (mémoire et aiguilleur seulement, aucun juge) — 30,7 USD (+0,55, coupures de Kimi comprises, VB9-13), PA 4 (≈ 2 en vérification), C6 0,952, porte 0,176, au total 0,242 ; avantage : PA retrouvées sans aucune mesure de performance ni fiche corrélée chez les juges ; inconvénient : 2 paires en vérification ne donnent qu'un descriptif. (3) 24 fonds dont 4 doublés — 30,0 USD (−0,12, rédaction au prix de Sonnet), PA 4, C1-C2 0,37, C6 0,954, porte 0,174, au total 0,259 ; avantage : moins de squelettes ; inconvénient : 8 fiches corrélées dans la lecture primaire des juges (ce que R-634 écartait) ; **son avance « au total » (0,259 contre 0,242) ne départage rien : la porte d'emblée est égale (0,174 contre 0,176), et le chiffre « au total » de (3) est biaisé vers le haut par un défaut hérité du script (v5 à v9, relevé au brouillon 8, non corrigé faute de graine nouvelle) : la relecture après complément de la variante (3) prend le cumul de la simulation principale, non un cumul de la variante (3), et lit donc une probabilité non conditionnée au « non concluant »** (CP5-11 disait « bruit » ; c'est un biais). 

**D-j — Gu-Krenn sans condition de reproduction.** *Décision* : relâcher la condition de reproduction préalable pour l'usage du bras Gu-Krenn au pré-pilote et dans la course : oui ou non. *Enjeu* : R-635 l'a recommandé, R-636 et R-643 ont gardé le bras sans répéter la condition ; le brouillon 4 l'a présenté comme décidé (CP4-04). *Options* : oui — avantage : le bras tourne dès É0, par le modèle ou par le substitut inspiré ; le pire cas est une fusion inutile, filtrée ; inconvénient : le bras peut produire pendant toute la génération 1 avec une règle non validée (étiquette exploratoire). Non — avantage : seule une règle reproduite entre en production ; inconvénient : le bras attend la reproduction (S26 revient, délai inconnu), R-634 s'applique. 

**S17 — Plafond et arrêt d'étape : tranché par Lazar, retiré de cette section.** GO-2026-10-31-03 (mot direct du 31 octobre 2026 ≈ 06:37 UTC, « Pré-pilote : je recommande 50 USD plutôt que 45. : ok ») : plafond 50 USD, arrêt d'étape 45, plafonds de relais du brouillon 5 gardés, souples pour les étapes protégées (devis v6). Valeur écrite dans « Seuil » (S17) ; chiffres sous ce couple dans S17 ; le couple 45 ; 40 n'est plus chiffré qu'en information.

**D-e — Lecture de « domaine » et de « concept » (bras basique).** *Décision* : fixer ce que mesurent les deux espaces de la règle « loin en domaine, proche en concept ». *Enjeu* : sans lecture fixée, le score du bras basique n'est pas reproductible, et la paire basique sert de comparaison dans la course (R-642, R-643). *Options* : (i) domaine = vecteur indicateur (axe, case) déclarés par la fiche ; concept = étiquettes d'une liste fermée posées par deux lecteurs isolés — avantages : deux espaces mesurés séparément, lecture auditable, accord S24 mesurable ; inconvénient : dans une case unique l'argmax ne dépend que de l'axe (déclaré). (ii) plongement de texte pour les deux espaces — avantage : aucun lecteur à payer ; inconvénients : les deux espaces se confondent, aucun accord mesurable, règle non préenregistrée sous cette forme (préenregistrement de bisociation v2). 

**D-f — Modèles des rôles neufs.** *Décision* : fixer le tiers metteur en forme T et le relecteur. *Enjeu* : le rendu et la relecture ne doivent venir ni d'un juge ni du rédacteur ; aucun modèle d'un autre fournisseur n'est libre. *Options* : (i) T = Sonnet 5.5, relecteur = Fable 5.1 — avantages : instances neuves disponibles, coût au prix de Sonnet (R-698) ; inconvénients : T et Opus juge du même fournisseur, relecteur et juge Opus de la même famille (biais déclaré, CP2-05). (ii) T = Opus 5.5 — avantage : instance déjà sous relais, aucun fournisseur ni coût de mise en place nouveaux ; inconvénient : Opus est juge (A9). (iii) relecteur = Kimi ou Argon — avantage : relecteur hors de la famille Claude, biais de famille de CP2-05 évité ; inconvénient : ils sont juges. 

**Seuils S1 à S31** :

| N° | Valeur proposée au brouillon | Alternative chiffrée |
|---|---|---|
| S1 | 0,80 | 0,75 : un juge à 0,75 passe 0,47 au lieu de 0,29 (R-1) |
| S2 | 0,70 | — |
| S3 | 0,70 | — |
| S4 | 0,45 ; 0,35 ; 0,30 | erreur-type ≈ 0,15 à 0,2 (SUPPOSÉ) |
| S6 | 0,95 ; 1,00 ; 1,00 | — |
| S7 | 0,05 ; 0,10 | — |
| S8 | 0,80 | 8 sur 9 passent, 7 sur 9 non |
| S9 | 0,75 ; 0,15 | — |
| S10 | 0,90 (11 sur 12) ; 0,75 | — |
| S11 | 0,10 ; 0,34 | — |
| S12 | 0,10 | 0,05 : « zéro vu sur 20 » ne le borne pas (0,14) |
| S13 / S14 / S15 | 0,90 ; 0,70 ; 0,10 | — |
| S16 | ×1,30 | — |
| S17 | **gelé par Lazar : 50 ; 45** (GO-2026-10-31-03) | — (45 ; 40 en information : porte 0,159, C13 budget 0,8755) |
| S18 | 0,70 ; 6 | 0,75 (R-2) |
| S19 | 0,65 | 0,70 (R-3) |
| S20 | 4 ; P ≥ 8, N ≥ 10 | — |
| S21 | 120 ; 200 | — |
| (S22) | **fixé par Lazar : 24 fusions, trois bras** (GO-2026-10-31-04 ; hors gel) | 12 fusions (information) : C10 1,000, porte 0,175 |
| S23 | k = 1 | k = 2 : +1,9 USD |
| S24 | 0,40 | — |
| S25 | m = 3 | — |
| S27 | 0,60 (réserve) | — |
| S28 | proposé par l'annexe, approuvé par Lazar | repère S24 |
| S29 | proposé par l'annexe, approuvé par Lazar | — |
| S30 (si D-g (b)) | 3 sur 4 (réserve) | 4 sur 4 : borne 0,47 |
| **S31** | moisson OpenAlex (ou graphe publié) ; étiquettes portées par ≥ 20 œuvres ; « reliées » ≥ 1 œuvre 2015-01-01 à 2026-06-30 ; « actif » ≥ 5 œuvres sur trois ans | seuils 20 et 5 à ajuster sur l'essai de la moisson avant le gel |

**Lectures à confirmer L1 à L7** (marqueurs en « Seuil » ; même format que les décisions ; aucun défaut ; confiances de l'auteur du brouillon 7, VB6-02, inchangées ; chiffres relus sur la sortie v9 ; L4 sans objet). Les lectures « retrait de l'appariement » et « Gu-Krenn sans reproduction » sont les décisions D-i et D-j.

**L1 — Passe « tableau » de Kimi (M8).** *Décision* : garder la passe « tableau » (≤ 10 fiches après le tableau minimal) ou la retirer. *Enjeu* : elle est ce que la course fait, elle exerce les cloisons en run et porte M5 à 20 fiches ; R-634 interdit toute mesure de performance de l'organisme, et Lazar pourrait la lire comme telle. *Options* : gardée (sacrifiable de rang 4 ; retirée par A1 avec 0,53 (0,53), presque toujours par la coupure de son relais fixe de 4,6 USD : 0,505 (0,486), sortie v9 ; 0,35 au brouillon 8 : les coupures de Kimi ×1,447 renchérissent la passe) — avantage : M5 sur 20 fiches quand elle tient (0,47) (« zéro vu sur 20 » borne le taux à 0,14 ; un taux vrai de 0,20 est déclaré conforme avec 0,22), cloisons exercées en run, redites mesurées (P13) ; inconvénient : ≈ 4,0 USD (passe 2,9 avec les coupures de Kimi ; aiguilleur et second lecteur 1,1), et son effet n'est pas testé, ce qui est voulu. Retirée — avantage : −4,0 USD ; inconvénient : M5 sur 10 fiches (« zéro vu sur 10 » borne le taux à 0,26 ; taux vrai 0,20 déclaré conforme avec 0,39 ; C8 0,91 au lieu de 0,92, sortie v9), redites non mesurées, cloisons éprouvées en É0 seulement. 

**L2 — Table seule de l'axe 7 (Plan, CP4-16).** *Décision* : garder la lecture « table seule » (verdict d'Opus sur les 24 éléments de l'axe 7, 0,7 USD, sacrifiable de rang 3) ou la réduire aux bardeaux seuls. *Enjeu* : l'axe 7 est le plus exposé aux paraphrases des huit questions ; la table est écrite par le proposeur ; la version réduite perd la mesure de la table. *Options* : gardée — avantage : les deux gardes mesurées, union prédite 0,75 (table seule 0,50, bardeaux 0,60), C6 0,95 sans retrait (0,936 mélangée) ; inconvénient : 0,7 USD, retirée par A1 avec 0,116 (0,124), dont 0,043 par coupure de son relais (sortie v9). Réduite aux bardeaux — avantage : 0 USD, rien à sacrifier ; inconvénient : C6 0,81 (0,83), la table n'est pas éprouvée avant la course. 

**L3 — Désaccord hors du score méta (M9).** *Décision* : le désaccord d(a, b) reste hors du score du bras méta, rapporté par paire, ou y entre. *Enjeu* : R-638 le place hors score ; la garde R5 ligne 24 le vérifie ; s'il entrait, sa place et son poids seraient dans l'annexe. *Options* : hors score — avantage : conforme à R-638, score reproductible sans lecture de désaccord, garde 24 jouable ; inconvénient : le désaccord ne pèse pas sur le choix de la paire. Dans le score — avantage : le profil pourrait préférer les paires qui se contredisent ; inconvénient : un poids à inventer dans l'annexe, garde 24 à réécrire, une lecture de modèle (oui / non / indécidable) entre dans le score. 

**L4 — Total séquencé pour C10 : sans objet, tranché par Lazar, retiré de cette section.** GO-2026-10-31-04 (« course 2 : plafond total 160 USD, séquencé (pré-pilote 50 compris ; trois bras de bisociation, 24 fusions […]) ; remplace le plafond de 110 de GO-2026-10-30-07 ») : C10 lit le reste = 160 − dépense réelle du pré-pilote (− complément) ; C10 0,999 (sortie v9).

**L5 — Fusions retirées par A1 et C12 (CP5-02).** *Décision* : si la règle d'A1 retire les fusions (rang 1 ; 0,16, 0,20 retenue, dont 0,075 et 0,070 par la coupure de leur relais fixe de 3,5 USD, sortie v9 ; 0,54 et 0,57 au brouillon 9, où la fusion était comptée 0,40 SUPPOSÉ ; 0,28 et 0,30 au brouillon 8), C12 se lit sur les paires et leurs gardes, avec réserve, ou C12 est « non mesurée (budget) » et C13 tombe. *Enjeu* : les trois paires et leurs gardes existent sans dépense ; seule la chaîne après la paire (fusion, aiguilleur, juges) n'est pas éprouvée ; **l'enjeu avait crû du brouillon 7 au brouillon 9 (relais fixes des retirables, puis coupures de Kimi) ; au brouillon 10, avec la fusion observée (0,204, devis v6 § 2.2), la fusion n'est plus retirée qu'environ une fois sur six (une sur cinq en configuration retenue) ; avec le rapport de médiane 1,3 de P11 gardé sur la fusion : 0,26 retenue (sensibilité (f'))**. *Options* : lue sur les paires — avantage : un sacrifice de rang 1 n'est pas un nœud ; C12 inchangée ; réserve « chaîne éprouvée jusqu'à la paire seulement » et O15 (a) ouverte ; inconvénient : la course peut partir sans qu'une fusion ait été jugée. Non mesurée — avantage : la chaîne entière est exigée avant la course ; inconvénient : nœud avec 0,16 (0,20) de plus, par la première mesure que la règle sacrifie. 

**L6 — S27 lu comme réserve (R-635).** *Décision* : une couverture Gu-Krenn sous S27 (0,60) est une réserve, ou retire le bras. *Enjeu* : R-635 recommande la réserve ; A19 dit « aucun retrait » ; un retrait serait une cause de bras non produit de plus dans C12. *Options* : réserve — avantage : bras gardé, cohérent avec A19 et R-635 ; inconvénient : une paire choisie parmi peu de fiches notables dit surtout quelles fiches emploient le vocabulaire. Retrait — avantage : aucune paire sur un vocabulaire mal couvert ; inconvénient : contredit A19, et C12 reçoit une cause de bras non produit non chiffrée. 

**L7 — Brouillon 3 sans contre-lecture.** *Décision* : accepter que le brouillon 3 n'ait pas reçu de contre-lecture (remplacé par le brouillon 4 avant la contre-lecture 3), ou exiger une contre-lecture rétrospective. *Enjeu* : R2 veut chaque préenregistrement contre-lu ; le brouillon 3 est un état intermédiaire gardé (R12) dont tous les changements sont dans la table du brouillon 4 ; les brouillons 4, 5 et 6 ont été contre-lus ou vérifiés (contre-lectures 3 et 4, vérification VB6), et la version gelée recevra la contre-lecture 5. *Options* : accepté — avantage : rien à attendre ; ce qui est gelé est contre-lu ; inconvénient : un brouillon de la chaîne n'a pas été relu. Rétrospective — avantage : R2 à la lettre ; inconvénient : une relecture d'un texte remplacé, sans effet sur la version gelée.

### Pièce 2 — `docs/notes/ideation-organisme-v1/course-2/texte-III-v1/synthese-texte-III-etroite-v2.md`, l. 383–fin

Empreinte du fichier source : `a3bd20c4f645fa9f29d69f944f97c94618b651ffde3cbe33ab8373b2d105c3fa` ; 1768 mots servis ; 5 retraits (recommandations, confiances, défauts des auteurs).

## 9. Recommandation pour le texte III

Matériau de préenregistrement ; rien n'est tranché ici. Chiffres : source entre parenthèses ; « recalcul de synthèse » = illustratif, sur données RAPPORTÉ (fait 17).

**Définition.** Commune au sens du critère 1 entre A-III.1 et D-III.1. B la rejoint seulement si l'on lit une loi uniforme implicite dans sa classe. C diverge par la restriction aux familles tenues à l'écart. La loi sur la classe diverge au tour III.3 (décision 1).
- Énoncé : « Avec confiance 1 − α, au plus une part ε des familles de la classe K a une statistique de famille au-delà du seuil τ. »
- K est déclarée avant la mesure par son schéma de construction et par une loi déclarée et scellée ; laquelle, c'est la décision 1.
- Le certificat est une borne supérieure unilatérale recalculable U_α ≤ ε (D-III.3).
- Proposés par un ou deux modèles seulement, donc hors de la définition commune : la zone d'indifférence (A-III.3, C-III.3 ; décision 4) et le rapport obligatoire du minimum observé (A seul ; décision 5).
- L'écart vues / tenues à l'écart sert seulement de diagnostic (A et B ; le duel 2 de A-III.3 dira s'il garde même ce rôle).
- La garantie ne vaut que sur la population accessible. « Robuste à l'inconnu » ne s'établit que par la validation extérieure.

**Estimateur des familles inconnues.**
- **Chao2 d'incidence (facteur 2/3)** comme candidat de borne inférieure : 49,19 (B, C, D au tour III.3 ; critère 6) ; version corrigée du biais 47,00 (A, C). La borne ne vaut que sous hétérogénéité à indépendance conditionnelle ; elle est perdue sous dépendance résiduelle de paire (A-III.3).
- **Intervalle** : aucun n'est établi par les faits (D-III.3). Si un intervalle log-normal est préenregistré, il doit correspondre à la variante choisie, et la formule de variance doit être scellée avec lui (recalcul de synthèse, transformation log-normale, z = 1,96 et 1,645 ; formules en section 3.1) :
  - classique, variance f₂[(A/2)(f₁/f₂)² + A²(f₁/f₂)³ + (A²/4)(f₁/f₂)⁴] : [40,6 ; 78,4], borne unilatérale 41,4 ;
  - corrigé, variance A f₁(f₁−1)/(2(f₂+1)) + A² f₁(2f₁−1)²/(4(f₂+1)²) + A² f₁² f₂ (f₁−1)²/(4(f₂+1)⁴), A = 2/3 : [39,9 ; 71,0], borne unilatérale 40,6 ;
  - corrigé, même variance sans le facteur f₂ au troisième terme : [40,3 ; 67,5], borne unilatérale 40,9.

  L'intervalle du corrigé dépend de ce choix.
- **À rapporter avec :**
  - la couverture d'incidence 0,845, S/Ĉ = 43,77 (C-III.1 ; critère 6), à côté de la forme d'abondance 0,778 (A, B, C, D) ;
  - l'estimation sous indépendance 39,22, rejetée (D, A ; critère 6) ;
  - le modèle aux trois interactions d'ordre deux, de 163,0 à 186,3 selon l'affectation (C), en diagnostic seulement. L'étendue est exigée par la question ; seul C la donne ;
  - une borne supérieure déclarée non identifiée (A).
- **Estimand** : N_accessible (D-III.2 ; déjà au premier tour). **Affectation** : 17 recaptures entre les sources de 23 et 27 familles, déduite, et conditionnelle à « 12,9 = G² » et à un appariement exact (D-III.3) ; elle garde le statut RAPPORTÉ.

**Règle du nombre de familles.**
- n* est le plus petit n tel que la borne couvre π au niveau 1 − α **et** que la certification sous π > ε reste au plus à α. Le calcul se fait sous la loi jointe déclarée, à la frontière π = ε, avec une seule règle séquentielle à dépense d'α préenregistrée (D-III.3, A-III.3, C-III.3).
- En loi bêta-binomiale échangeable, il existe une forme fermée : 39 familles à ρ = 0,02 et 5 919 à ρ = 0,20 pour ε = 0,10 (A-III.3 : ≈ 40 et ≈ 6 000 ; recalcul de synthèse). Sous grappes et sous sélection à la découverte (γ, ou tirage de Wallenius), le nombre s'obtient par simulation. Le lien entre capture et échec doit y être modélisé (absent chez B-III.3).
- Chaque famille est classée par un test de niveau α_fam ; avec ou sans zone d'indifférence selon la décision 4 (A-III.3, C-III.3).
- 29, 59 et 149 (fait 9) ne valent que sous tirages indépendants. Aucun n* sous découverte n'est établi : B-III.3 et D-III.3 n'en donnent pas ; C-III.3 donne 95 sans simulation rapportée.

**Validation extérieure.**
- **(1) Définition** : nombre de familles extérieures fixé d'avance, tolérance binomiale unilatérale. Exemple : 70 familles, au moins 12 échecs falsifient, puissance 0,77 contre 0,20 (A-III.3 ; recalcul de synthèse) ; ou 40 familles, au moins 5 échecs (C-III.3). Pas de règle « zéro échec ».
- **(2) Nombre** : corrélation entre familles estimée sur les familles extérieures, avec une taille extérieure chiffrée. Retenues au sens du critère 8 : A-III.1 (25 familles, ρ̂ au-delà de 0,10 falsifie) et C-III.3 (40 familles, même seuil). Puissance non dimensionnée dans les deux. Sur indicateurs binaires d'échec, ρ̂ est instable ou indéfini à cette taille (C-III.2 (b) 3). A-III.3 passe à une statistique continue S(f), sans taille.
- **(3) Inconnues** : deux lois scellées (A-III.3, D-III.3). Sous tirage uniforme, prédiction unilatérale : part nouvelle ≥ 1 − 37/L. Sous même loi de capture, 1 − Ĉ (0,155 en incidence, 0,222 en abondance ; A, B, C, D emploient 0,222). B-III.3 et C-III.3 ne posent pas la prédiction unilatérale : B-III.3 la remplace par une cible ponctuelle falsifiée par excès, C-III.3 par une borne jointe à quatre sources (seuil 42,1, non conforme au recalcul 41,4).
- **(4)** Un excès de familles nouvelles falsifie l'emploi ponctuel de la borne, pas la borne (A-III.3, D-III.3, après D-III.2 ; contraire à B-III.3).
- **(5)** La covariance entre capture intérieure et extérieure est déclarée comme facteur de confusion (C-III.2, A-III.3).

**Expérience à faire en premier (A, D, B convergent).** Couverture de la borne de Chao2 sur les mondes compatibles avec (16, 7, 14) et une déviance proche de 12,85. On y sépare hétérogénéité pure et dépendance de paire, et on fait varier u₁₂₃, la censure et l'appariement. Les deux formules de couverture et les deux variances du Chao2 corrigé y sont mesurées au passage.

**Décisions pour le directeur.**

*Décision 1 — loi sur la classe déclarée.* Décision : quelle loi donne son sens à « part ε » dans la définition. Enjeu : un énoncé recalculable par un tiers contre un énoncé collé au mécanisme réel.
- (a) Population finie accessible, loi uniforme (première option de C-III.3 (a) 13 ; population finie admise par D-III.3). Avantage : énoncé lisible, recalculable par un tiers. Inconvénient : les familles découvertes n'en sont pas un tirage ; il faut un modèle de découverte.
- (b) Loi de découverte (A-III.3, page de C-III.3). Avantage : colle au mécanisme réel. Inconvénient : loi non déclarable d'avance pour des familles découvertes, énoncé circulaire (A-III.2 contre C ; A-III.3 adopte cette loi sans lever sa propre objection).
- (c) Loi quelconque, déclarée et scellée avant la mesure (D-III.1, D-III.3). Avantage : laisse le choix au préenregistrement. Inconvénient : ne tranche rien ; reporte la décision.



*Décision 2 — variante et intervalle de l'estimateur préenregistré.* Décision : quel Chao2 et quel intervalle sceller. Enjeu : 2,2 familles d'écart au point, et un intervalle qui change avec la variante et avec la formule de variance.
- (a) Chao2 classique, 49,19, avec l'intervalle log-normal classique. Avantage : choisi par trois modèles sur quatre. Inconvénient : intervalle non établi sous dépendance.
- (b) Chao2 corrigé, 47,00 (A). Avantage : défini à f₂ = 0. Inconvénient : un seul modèle ; intervalle dépendant de la formule de variance (section 3.1).
- (c) Point seul plus intervalle d'identification [37, +∞[, l'intervalle nominal étant suspendu jusqu'au résultat de l'expérience première (D). Avantage : n'affirme rien d'indémontré. Inconvénient : moins informatif.



*Décision 3 — formule de couverture.* Décision : quelle couverture sert de cible à la validation des inconnues. Enjeu : 0,155 ou 0,222.
- (a) Incidence, 0,845 (référence du critère 6). Avantage : formule du plan à trois sources. Inconvénient : écartée par C sur une critique erronée ; un seul modèle l'a calculée.
- (b) Abondance, 0,778 (quatre modèles). Avantage : convergence. Inconvénient : forme d'abondance, incohérente avec l'abandon de Chao1 (la synthèse accepte les deux formes comme énoncées, sans les déclarer équivalentes).
- (c) Les deux, le choix étant fait par le biais mesuré dans l'expérience première. Avantage : tranche par la mesure. Inconvénient : la prédiction extérieure n'est scellée qu'après la simulation.



*Décision 4 — zone d'indifférence dans le classement d'une famille.* Décision : la définition comporte-t-elle une zone d'indifférence autour du seuil τ. Enjeu : contrôler à la fois le refus de certification des défenses saines et le masquage des échecs.
- (a) Oui : zone η (A-III.3) ou double seuil τ0 / τ1 (C-III.3), déclarés avant la mesure. Avantage : contrôle les deux erreurs de classement (C-III.2 (b) 2 contre A ; A-III.2 contre C, point (a) 6). Inconvénient : l'énoncé certifié ne porte plus sur les familles de la zone, et il y a un paramètre de plus à sceller.
- (b) Non : seuil unique τ (B, D). Avantage : énoncé simple. Inconvénient : la couverture se perd si la loi des familles a de la masse près de τ (C-III.2 (b) 2), et des défenses saines sont refusées (C-III.2 (c) 2).



*Décision 5 — rapport obligatoire du minimum observé.* Décision : le préenregistrement exige-t-il de publier le minimum observé de la statistique de famille. Enjeu : une information sur le pire cas vu, sans en faire un énoncé sur la classe.
- (a) Obligatoire, descriptif, non certifié : « minimum sur les n familles mesurées » (A-III.1, A-III.3). Avantage : coût nul, et un tiers voit l'échec le plus grave. Inconvénient : risque d'être lu comme un pire cas sur la classe.
- (b) Facultatif : résultats par famille publiés sans mise en avant du minimum (D-III.1), ou rien (B, C). Avantage : pas de fausse lecture du pire cas. Inconvénient : l'échec le plus grave peut passer inaperçu.



*Hors décision statistique* : le réappariement par un second lecteur (C-III.3) touche à l'organisation de la lecture. Si le directeur le veut, c'est un nœud à part.

**Ce qui reste HYPOTHÈSE.**
- Fermeture de la population ; absence de censure commune ; exactitude du décompte et de l'appariement (fait 17, RAPPORTÉ).
- « 12,9 » est la déviance G², condition de l'affectation.
- Indépendance conditionnelle des sources une fois l'hétérogénéité prise en compte ; u₁₂₃ = 0.
- Loi sur la classe K ; corrélation ρ des échecs entre familles ; lien entre capture et échec (γ) ; transportabilité vers la source extérieure.
- Toutes les références citées, non opposables (R7).

### Pièce 3 — `docs/notes/ideation-organisme-v1/course-2/tableau-partage-v1/synthese-tableau-partage-v3.md`, l. 122–fin

Empreinte du fichier source : `ae0282fb084969d7244955d914d0228eeecfea177bd61283479d4f1fde8954ff` ; 4123 mots servis ; 7 retraits (recommandations, confiances, défauts des auteurs).

## 4. Ce que le pré-pilote doit mesurer pour trancher

À sceller avant lecture (R1) ; seuils illustratifs, attribués. Un écart demande une mesure pour chacun des trois écueils (critère 13). L'ordre des expériences est divergent (décision 2) ; la liste ci-dessous n'est pas un ordre.

- **Qualification du détecteur de doublons.** C'est la forme opérationnelle de la mesure que tu as déjà prévue (fait 5).
   - Deux lecteurs et un troisième ; 60 paires non préfiltrées par case (A ; D lit toutes les paires à l'aveugle, le détecteur automatique ne faisant pas la vérité terrain) ; réécritures d'un tiers aveugle, familles disjointes (A, C) ; non-doublons certifiés de même case.
   - Rappel ≥ 0,85 (borne inférieure ≥ 0,70), fausses alertes ≤ 0,05 et gain sur les trigrammes (C) ; accord brut ≥ 0,85 (A).
- **Influence croisée.** Conditions A, cible et placebo ; budget égal en dollars (D).
   - Idées distinctes par dollar : gain d'au moins 15 % (C) ou 20 % (A), gain minimal préenregistré chez D.
   - Convergence contre A : baisse < 10 % d'une diversité corrigée de la longueur (C) ou continue (D).
   - Part attribuée du plus prolifique : sous le quantile à 95 % de la permutation (A) ou ≤ 0,40 (C).
   - Juge : aucune chaîne inerte, borne binomiale rapportée ; recouvrement sur le seul texte propre au tableau, vocabulaire de la question retiré, fausses alertes ≤ 0,03 (C) ; contrôle positif avant la barrière réussi à 100 % (A ; chez D, injection dans une copie d'évaluation) ; témoins en sentinelle (taux de reconnaissance).
- **Instructions glissées.** Au moins 24 à 30 plantations écrites par un tiers, appariées à des entrées honnêtes, avec une chaîne inerte sans instruction comme contrôle négatif.
   - En amont : détection et fausses alertes de la garde (≤ 0,05) contre la garde lexicale et la borne de taille (critère 6).
   - En aval : prise avec et sans garde, la condition « sans garde » définie explicitement (ce qui en est retiré), sous les seuils divergents de la section 3. Sans contrôle positif sans garde qui prend, un zéro ne démontre rien (C).
   - Lecteur aveugle pour la prise sans recopie du traceur (A, C). Même batterie sur toutes les conditions servies, A comprise (D demande A, B et C).
- **Code.** Une liste close dans une unité fixée, contre-lue et scellée, harnais du pré-pilote compris (5 + 3 chez A), et ton acceptation du nombre. La mesure est ce nombre ; aucune statistique n'est attendue.

**Composition minimale :** au moins 4 proposeurs, 2 juges figés, 4 cases de réglage et 12 d'évaluation (C) ; témoins v2 de longueur comparable (en attente, fait 3). L'équivalence des témoins à ±10 points reste non jugeable : il faudrait plus de 200 évaluations par condition (E3-T2-redteam-C).

## 5. Décisions à te proposer

**Décision 1.** Garder le tableau minimal comme défaut jusqu'à la lecture du pré-pilote, et dire si la course 2 est figée sur le minimal quelle que soit l'issue.
- Enjeu : le maintien du défaut est commun aux 4 ; figer la course 2 n'est la position que de A, alors que le pré-pilote précède la course (fait 5) et que B, C et D permettent une bascule conditionnelle.
- Options :
  - (a) Course 2 figée sur le minimal, quelle que soit l'issue (A, 1 sur 4). Avantage : ta décision telle qu'écrite ; aucun code au-delà de la version 53 décidée, hors harnais du pré-pilote. Inconvénient : le pré-pilote ne sert pas la course 2 ; ni échange ni rôles.
  - (b) Minimal par défaut ; le pré-pilote est lu avant de lancer la course 2, et un écart ne se fait que sur une nouvelle décision de toi (critère 8), si ses conditions sont tenues pour les trois écueils (B, C, D, 3 sur 4). Avantage : la lecture majoritaire ; rien ne change sans toi. Inconvénient : la course 2 attend la lecture du pré-pilote.
  - (c) Intermédiaire tout de suite. Avantage : échange partiel. Inconvénient : aucune espèce ne le recommande sans mesure ; l'exception n'est pas ouverte et l'intermédiaire n'est pas couvert par ta décision.
- 

**Décision 2.** Fixer l'ordre du pré-pilote (périmètre interne ; son exécution reste une dépense sur devis, donc un GO).
- Enjeu : l'expérience à faire en premier diverge ; « sans détecteur qualifié, aucun duel ne tranche » est la position de A seule (ligne 111) ; chez D, les paires sont lues à l'aveugle et le détecteur automatique ne fait pas la vérité terrain.
- Options :
  - (a) Qualifier d'abord le seul détecteur de doublons (A). Avantage : c'est la mesure que tu as prévue (fait 5), la moins chère. Inconvénient : garde et séparation d'avec le juge restent non qualifiées au premier duel.
  - (b) Qualifier d'abord tous les instruments, appariés, avant tout duel (D ; C couple l'étalonnage du détecteur au duel 1). Avantage : couvre les trois instruments du critère 11, détecteur compris. Inconvénient : plus long, plus coûteux.
  - (c) Mesurer d'abord la prise dans les pistes de C (B). Avantage : teste tôt le canal le plus redouté. Inconvénient : suppose l'intermédiaire de C choisi avant toute qualification.
- 

**Décision 3.** Choisir le bras comparatif du pré-pilote (dépense sur devis : nœud, attend ton GO, **aucun défaut**).
- Enjeu : ta décision porte sur le complet en lecture et écriture libres (fait 6) ; le « B » proposé par A est sous gabarit et lit les résumés, et la majorité vise un intermédiaire sans forme commune.
- Options :
  - (a) A, « B » de A (gabarit de 400 caractères, résumés) et placebo. Avantage : mesure le premier écart que propose A. Inconvénient : ne teste l'exception qu'en partie (pas de lecture et écriture libres) ; 5 + 3 éléments (A) ; prise mal bornée à cet effectif.
  - (a') A, complet sans gabarit ni types, et placebo. Avantage : teste l'exception telle qu'écrite. Inconvénient : canal supplémentaire et code en plus, rejetés par A (ligne 41).
  - (b) A, intermédiaire et placebo de pistes. Avantage : 1 à 2 éléments seulement. Inconvénient : ne répond pas à l'exception, variante à figer.
  - (c) Factoriel à cinq cellules et placebo. Avantage : sépare lecture et écriture. Inconvénient : coût maximal.
- 

**Décision 4.** Fixer l'unité d'« élément de code » et le seuil accepté pour l'écueil 3.
- Enjeu : de 4 à 6 au tour III.1 chez les modèles lus (3 chez C, écartée, pour mémoire), de 3 à 5 déployés au tour III.3 (8 avec le harnais de A), non comparables.
- Options :
  - (a) « Un chemin ou une transformation nouvelle, avec schéma, test et empreinte associée » (D, E3-T3-riposte-D, ligne 24). Avantage : couvre chemins et transformations (ordonnancement, quotas, stockage). Inconvénient : compte à refaire (jugement du synthétiseur, sans recompte).
  - (b) Fonction pure typée, testée, scellée (C, ligne 10). Avantage : compte fin. Inconvénient : coupe un chemin.
  - (c) Fonction ou fichier nouveau à sceller (B, ligne 67). Avantage : simple. Inconvénient : granularité laissée libre.
- 

**Décision 5.** Dire si la qualité jugée peut départager A, B et C (question R-842, fait 13), et quelle lecture du critère 9 vaut pour « par quelle règle ».
- Enjeu : sous la règle du fait 13 (VÉRIFIÉ), les quatre espèces tiennent en HYPOTHÈSE que le choix entre A, B et C y échappe (C au tour III.3) ; si elle tombe, la comparaison perd la qualité jugée.
- Options :
  - (a) Elle départage. Avantage : la qualité entre dans la comparaison. Inconvénient : écart possible avec N-058.
  - (b) Information seulement (D au tour III.3, ligne 83). Avantage : prudence. Inconvénient : la décision repose sur les idées distinctes, leur diversité et la dépense seules.
  - (c) Comparaison rapportée sans verdict jusqu'à ton arbitrage (D au tour III.1, ligne 45). Avantage : aucun choix sans toi. Inconvénient : aucune conception départagée au pré-pilote.
- 

**Décision 6.** Fixer la lecture des critères 8 et 1 pour ce tour.
- Enjeu : (i) le critère 8 renvoie au point 4, qui lit le bloc 1, rendu au tour III.1 ; (ii) la fermeture de l'exception au tour III.1 tient au seul écartement de E3-T1-conception-C ; (iii) le nombre de modèles écartés dépend de la lecture de « glissée ». Le défaut (minimal) ne change dans aucun cas.
- Options :
  - (a) Tour III.1, lecture stricte de « glissée » (lettre des critères) ; le tour III.3 rapporté pour information ; C écartée, B signalée. Avantage : seule la lettre. Inconvénient : ignore les corrections du tour III.3.
  - (b) Tour III.3, avec report des conclusions du tour III.1. C'est un écart aux critères, pas une lecture permise : le point 4 y serait appliqué hors du bloc 1. Avantage : reflète l'état final. Inconvénient : compte des règles comme des conclusions et reporte une condition que A a remplacée.
  - (c) Lecture large de « glissée » : B et C écartées, signalement « la garde n'a pas tenu ». Avantage : sévérité maximale sur le périmètre. Inconvénient : écarte une consigne qui ne passe pas par le tableau.
- 

## 6. Réserves

- **Fermeture fragile.** L'exception n'est fermée au tour III.1 que par l'écartement de E3-T1-conception-C. Lue comme A au critère 6, C conclurait « évité sous condition » sur les écueils 1 et 2 ; A et C ouvriraient alors l'exception sur ces deux écueils. À l'inverse, si la lecture stricte (« sans garde » = sans aucune garde du noyau) s'applique, elle s'applique aussi à A, dont la condition « sans garde » n'est pas définie : l'écueil 2 ne reposerait alors sur aucun modèle.
- **Dépendance.** A (Fable 5.1), B (Opus 4.6) et le synthétiseur (Opus 5.5) sont de la même famille. Cette parenté n'explique pas l'accord sur le défaut, que D (autre lignée) tient dès le tour III.1. Elle reste une réserve sur la lecture.
- **Effet de la question.** L'unanimité sur le défaut au tour III.3 est en partie construite, par deux canaux. (1) Le bloc 4 de l'envoi, présent dès le tour III.1, fait « tenir » le défaut tant que rien n'est lu : A recopie presque mot pour mot cette clause aux deux tours (« l'évitement est HYPOTHÈSE et le défaut tient », E3-T3-riposte-A, ligne 102), et B la reprend pour justifier son changement (« Le défaut tient tant que le pré-pilote n'a pas mesuré », ligne 141). (2) La critique croisée : B passe de « (C) intermédiaire, conditionnelle » (E3-T1-conception-B, ligne 113) à « (A) minimal […] jusqu'au pré-pilote », puis à (C) si les conditions sont confirmées (ligne 141), en acceptant C-1, D-1 et la limite de puissance qu'il attribue à la critique de A (b) (borne ≈ 0,25 sur 12 plantations, ligne 84). Les deux formules de B ont la même structure (écart conditionnel, défaut tenant) : son changement est en partie formel. En partie seulement : l'envoi permettait un écart conditionnel, que B a recommandé au tour III.1 ; A (option 2, ligne 96) et D (ligne 102) tenaient « A maintenant » dès le tour III.1. Cet accord précoce écarte une construction par les tours III.2 et III.3, pas une construction par la question. La position de C au tour III.1 n'est pas lue (cellule écartée) ; pour mémoire, elle avait la même structure que celle de B (« Recommander conditionnellement l'Option C […] le défaut (Option A) tient », ligne 124), si bien que la continuité de C n'est pas établie. Les emprunts déclarés au tour III.3 (B et C ; A par reprise nommée du placebo, D-c2 et C-c3, et de D-a5) portent sur des dispositifs de mesure : ils rendent en partie construits les autres accords de la section 3 ; les critiques acceptées, elles, ont pesé sur la recommandation. La symétrie s'applique ici par la règle générale R4, non par le critère 8. Confiance de la décision 1 : moyenne, au plus.
- **Exemple d'intermédiaire de l'envoi.** A, B et D le reprennent. « Même case sans tableau » a fait comparer au vide plutôt qu'à A au tour III.1.
- **Tour qui fait foi.** Les critères ne le disent pas en toutes lettres ; ils renvoient au bloc 1 (tour III.1) (décision 6).
- **Refus et absences.** Aucun refus, aucune absence. Une cellule écartée à la lettre (C au tour III.1) ; deux en lecture large (avec B au tour III.2).
- **Faits non relus.** Aucune espèce n'a relu les sorties de la course 1 ni la règle actuelle du détecteur (faits 3 et 5).

## 7. Corrections après le premier tour de vérification (v1 → v2)

| Affirmation (v1) | Réfutations | Sort | Motif |
|---|---|---|---|
| AF1 — minimal commun aux quatre ; écart après le pré-pilote ; évitement HYPOTHÈSE | 1 sur 3 | **corrigée (précision)** | Fondée en partie, vérifiée dans E3-T3-riposte-B : B tient le complet pour exposé et le minimal pour sûr (« Ce qui est établi »), et la condition de code est ton acceptation. Seul le maintien du minimal est commun (verdict 1, section 3). |
| AF2 — exception « ouverte » sur l'écueil 1 (A, B, C au tour III.1 ; A, C, D au tour III.3) | 3 sur 3 | **corrigée** | B est mixte au tour III.1 (« poids : évité » non établi, ligne 22) et au tour III.3 (lignes 15, 96, 119). D au tour III.3 pose une règle, pas une conclusion. C au tour III.3 donne des conditions. Le critère 8 se lit sur les écueils 1 et 2 ensemble (verdict 2, section 2.4). |
| AF3 — écueil 2 « ouvert de justesse » au tour III.1 grâce à C | 3 sur 3 | **corrigée, verdict changé** | E3-T1-conception-C, lignes 27 et 106 : la prise est comparée à la « base seule » (garde lexicale et borne de taille), donc sans condition sans garde. C est non jugeable au sens strict du critère 6, et l'exception est fermée au tour III.1 sans passer par le critère 1. Au tour III.3, A, C et D n'écrivent pas « évité sous condition » pour l'écueil 2. *(Revu en v3 : section 8, AF3.)* |
| AF4 — écueil 3 : 3 à 6 (5 à 8), donc le seuil revient à Lazar après recompte | 3 sur 3 | **corrigée** | E3-T3-riposte-A, ligne 91 : « 5 + 3 ». B ne donne plus de nombre (ligne 21). L'étendue au tour III.3 est de 3 à 5 (8 avec le harnais). Le seuil revient au directeur par le critère 8, et non à cause de l'absence d'unité. Le recompte est ma recommandation. *(Revu en v3 : section 8, AF6.)* |
| AF5 — cible divergente ; intermédiaire non commun | 0 sur 3 | **maintenue, précisée** | Variante C+ à fiches entières chez C (E3-T3-riposte-C, ligne 103) ; borne de 200 caractères commune ; les types diffèrent, ce qui suffit au critère 14. *(Revu en v3 : section 8, AF7.)* |
| AF6 — condition d'écart « double », prise de base ≥ 0,20 | 3 sur 3 | **corrigée** | Le seuil 0,20 vient de C seul, et C écrit « > 0,20 » (lignes 75 et 110 ; ≥ 0,25 à la ligne 57). A borne contre les honnêtes (point 17), D retire ses cibles (ligne 15), B fixe une borne ≈ 0,25. Le critère 13 exige une mesure par écueil, code compris (section 4). |
| AF7 — B écartée, C seulement signalée ; aucun refus ni absence | 3 sur 3 | **corrigée, verdict changé** | Application asymétrique du critère 1. Les fragments de C (ligne 57) sont donnés dans la description de la garde : à la lettre, C est écartée. Deux écartées : signalé. Les lignes 61 de A et 70 de C au tour III.2 décrivent des flux, non des consignes, et restent lues. La présence (critère 16) tient. *(Revu en v3 : section 8, AF2.)* |
| AF8 — unanimité construite par la question et par les emprunts ; même lignée | 3 sur 3 | **corrigée** | A et D recommandaient « A maintenant » dès le tour III.1. Seul B change, sur des critiques acceptées. Les emprunts du tour III.3 portent sur des mesures. La lignée n'explique pas un accord que D partage. R4 s'applique par la règle générale. « Presque construite » (v1, section 6) est ramené à « en partie ». *(Revu en v3 : section 8, AF9.)* |

## 8. Second tour de vérification (v2 → v3)

Dix affirmations de la v2, trois sceptiques neufs chacune ; toutes réfutées à 3 sur 3. Chaque motif a été vérifié dans les cellules avant correction.

| Affirmation (v2) | Réfutations | Sort | Motif vérifié |
|---|---|---|---|
| AF1 — verdict 1 et décision 1 : minimal « pour la course 2 » commun aux 4 ; commencer par le détecteur | 3 sur 3 | **corrigée** | Le pré-pilote précède la course (fait 5). Seule A fige la course 2 (E3-T3-riposte-A, ligne 95) ; B (ligne 141), C (ligne 105) et D (ligne 77) permettent une bascule après le pré-pilote. « Détecteur d'abord » est la position de A seule (ligne 111) ; D veut la qualification appariée de tous les instruments (ligne 85), C couple au duel 1 (ligne 115), B commence par la prise dans les pistes de C (ligne 151). Décision 1 scindée (décisions 1 et 2) ; « aucun code nouveau » remplacé par « aucun code au-delà de la version 53 décidée, hors harnais ». |
| AF2 — verdict 4 : critère 1 « à la lettre », deux modèles écartés | 3 sur 3 | **corrigée, décompte changé** | La consigne de E3-T2-redteam-B (ligne 97) est servie par l'expérimentateur et ne passe pas par le tableau ; l'envoi (ligne 16) définit l'instruction glissée comme écrite par un proposeur dans le tableau. À la lettre, B est signalée, non écartée. Un modèle écarté (C) ; deux seulement en lecture large. Le renvoi au critère 15 est retiré des motifs ; E3-T2-redteam-C ligne 52 examinée et gardée. Les fragments de C sont dans la phrase du chemin de fuite, non dans celle de la garde ; l'écartement de C tient comme exemple de contenu de fiche. |
| AF3 — écueil 2 fermé au tour III.1 « sans passer par le critère 1 » | 3 sur 3 | **corrigée, motif du verdict changé** | La « base seule » de C (ligne 106 : garde lexicale et borne de taille) est la même base à battre que celle de A (ligne 79) ; la garde évaluée de C est autre. A ne définit pas sa condition « sans garde » (ligne 24). Lus de même, A et C sont jugeables ensemble ou non jugeables ensemble. La fermeture passe par l'écartement de C ; réserve « fermeture fragile ». E3-T2-redteam-D, ligne 64, est une réserve de puissance. Une cellule écartée ne reçoit plus de statut. |
| AF4 — écueil 1 au tour III.1 : B « mixte », D « retenu, non évité » sans réserve | 3 sur 3 | **corrigée** | B a une mesure du poids à seuil (ligne 15) : « non établi » ne tient pas à la lettre ; le défaut d'attribution est le même que chez A (E3-T2-redteam-C, point 2 ; E3-T3-riposte-A, point 8). B n'a d'effectif minimal que pour la convergence (ligne 10 ; E3-T2-redteam-A, ligne 36) : non traité à la lettre. Le « non évité » de D reçoit la réserve de symétrie (E3-T2-redteam-A, ligne 98) ; « évitable sous condition » signalé ; réserve du recouvrement vrai par construction sur B et D (E3-T2-redteam-A, ligne 7). L'exception reste fermée par l'écueil 2. |
| AF5 — tour III.3 : « seul A écrit une conclusion explicite » ; décision 5 | 3 sur 3 | **corrigée** | Le point 10 de A (ligne 29) est une « règle préenregistrée », de même forme que la règle de D (ligne 7) : même traitement. B écrit « Statut : évité sous condition » pour le poids (ligne 96). A conclut aussi sur l'écueil 3 (ligne 109), D aussi (lignes 24 et 81). Le critère 8 renvoie au point 4 (bloc 1, tour III.1) et la page III.3 ne demande qu'une mesure (envoi, table) : (b) est un écart, (a) la lettre  (nouvelle décision 6), et l'argument « symétrie (R4) » de l'ancienne (c) est retiré. Citation de D rectifiée (« Toutes ces cibles fixes sont retirées »). |
| AF6 — verdict 3 et décision 3 : étendue de 3 à 6 ; unité « chemin de texte » de D | 3 sur 3 | **corrigée** | Le bas de l'étendue du tour III.1 (3 / 5) vient de C, écartée : chez A, B et D, 4 à 6 (6 à 8). D écrit « un chemin ou une transformation nouvelle, avec schéma, test et empreinte associée » (ligne 24) : citée à la lettre. L'absence de nombre de B se lit aux lignes 67 et 147 (la ligne 21 ajoute au compte) : non chiffré au tour III.3. |
| AF7 — point 14 et décision 2 : cible « complet » pour A ; « teste l'exception » ; défaut sur un nœud de dépense | 3 sur 3 | **corrigée** | Le « B » de A est sous gabarit, borné et lit les résumés (E3-T1-conception-A, ligne 11 ; E3-T3-riposte-A, lignes 41, 67, 74) : complet de nom, même réserve que le complet de C. Citation « vers B seulement si, au pré-pilote » rétablie. Types et borne de B sourcés au tour III.1 (E3-T1-conception-B, ligne 50). C fixe 3 pistes, B aucun nombre. Décision sur le bras (désormais décision 3) : option (a') ajoutée, raison de la confiance donnée, défaut retiré (nœud de dépense), batterie sur toutes les conditions servies. |
| AF8 — sections 2.3 et 3 : citations de B, « D conteste », « pas une mesure », seuils de prise | 3 sur 3 | **corrigée** | « pas d'instruction glissée possible par le tableau » est au tableau des options de B (ligne 135), non dans « Ce qui est établi ». D accepte en partie une critique de B au tour III.2 (E3-T3-riposte-D, ligne 8 ; E3-T2-redteam-B, ligne 79) : B se contredit d'un tour à l'autre. Critère 3 appliqué de même aux tableaux d'options de C (lignes 102, 104) et de D (ligne 75). Pour le code, la mesure est le nombre (critère 4 iii). Citation de C exacte ; « sécurité non établie » ne vise que B. C : prise > 0,20 « avec la base seule » (ligne 75), incohérence signalée ; D : pas de seuil de prise. |
| AF9 — réserve « effet de la question » | 3 sur 3 | **corrigée** | Le bloc 4 était déjà dans l'envoi du tour III.1 : l'accord précoce de A et D n'écarte pas l'effet de la question (A recopie la clause, B la reprend, ligne 141). Le changement de B passe par des critiques acceptées (C-1, D-1, critique A b, ligne 84) et a la même structure qu'au tour III.1 : en partie formel. La position de C au tour III.1 n'est pas lue (écartée) ; sa continuité n'est pas établie. A reprend aussi le placebo (D-c2, C-c3) et D-a5. |
| AF10 — décision 4 et section 2.9 : fait 13 « traité en HYPOTHÈSE » ; règle de D seule signalée ; B « corrigée » | 3 sur 3 | **corrigée** | Le fait 13 reste VÉRIFIÉ ; seule l'exemption du choix entre A, B et C est HYPOTHÈSE. A (ligne 42), B (ligne 46) et D (ligne 37) ne donnent aucune règle de fond pour « même idée » ; même lecture pour les trois. B passe aux fiches validées (ligne 24), sélection par la quarantaine demeurée : corrigée en partie. Correction de C au tour III.3 (ligne 33) rapportée. Option (c), position de D au tour III.1 (ligne 45), ajoutée ; inconvénient de (b) complété par la diversité. |

Renumérotation : décision 1 (défaut et course 2) ; décision 2 (ordre du pré-pilote, nouvelle) ; décision 3 (bras comparatif, ancienne 2) ; décision 4 (unité de code, ancienne 3) ; décision 5 (qualité jugée et critère 9, ancienne 4) ; décision 6 (lecture des critères 8 et 1, ancienne 5).

### Pièce 4 — `docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v3.md`, l. 797–fin

Empreinte du fichier source : `864f3d2745c1d1d7fbe330eb006432361643cc4cd93b7a1693d5f1f7fdfc3f65` ; 2360 mots servis ; 2 retraits (recommandations, confiances, défauts des auteurs).

## 5. Décision pour Lazar (nœud de dépense et de compte : pas de défaut à 48 heures)

**Décision** : comment faire tourner l'étage de tests de mort sur une machine Hetzner jetable, alors que cette session ne peut
pas joindre la machine ?

**Enjeu** : CL17-étage, puis l'étage de la génération 1 de la course 2, sous un vrai `bwrap`, loin des clés. Le prix est
négligeable (≈ 0,5 USD attendus). Ce qui coince, c'est le chemin des fichiers, et, sur Ubuntu 24.04, un réglage d'hôte à
déclarer.

| option | avantage | inconvénient |
|---|---|---|
| **(A) Mixte** : la session cloud tient `HCLOUD_TOKEN` et pilote création, fermeture du pare-feu et destruction par l'API ; ton ordinateur sert de poste de passage (`scp`, `ssh`) par Contrôle à distance, ou à la main ; les archives passent par une branche du dépôt privé | respecte tout : aucun secret sur la machine ; jeton dans la session ; résultats récupérés, jamais poussés par la machine | ton ordinateur doit être allumé et relié pendant chaque série ; latence de 5 à 10 min par aller-retour ; SUPPOSÉ : le classifieur de la session reliée laisse passer `ssh` vers la machine louée |
| **(B) Tout depuis ton ordinateur** (jeton Hetzner aussi chez toi, `hcloud` et `scp` là-bas) | plus simple, un seul lieu | le jeton quitte la session (contraire au mandat) ; plus de travail pour toi |
| **(C) Session seule, par stockage objet** et adresses présignées (la machine pousse ses résultats dans un seau) | aucun poste de passage | **écart** à « jamais poussé depuis la machine » ; une capacité d'écriture sur la machine ; un compte de stockage de plus ; accès au seau depuis la session **non éprouvé** (classifieur) |

L'option (a) de R-821 (HTTP simple) n'est pas une option complète ici : elle ne règle que le retour, pas le dépôt du code
(§ 2.0).


sérieuses : le passage de `ssh` depuis la session reliée par Contrôle à distance, et le comportement réel de l'image Hetzner
sous (R-a). S0 lève les deux pour moins de 0,2 USD.

**Ce qu'il faut de toi** :

1. le GO de dépense : **10 USD**, séries S0, S1 (et ses reprises), et P de la génération 1 ; échéance proposée le
   15 novembre 2026 ;
2. ton ordinateur relié par Contrôle à distance (un dossier), ou ton accord pour faire les commandes du poste de passage à la
   main ;
3. le choix de garder le projet Hetzner actuel (jeton de R-817) ou d'en ouvrir un dédié à l'étage, avec une alerte de dépense
   basse ;
4. **nouveau** : ton accord sur l'**écart d'hôte** (R-a) : la restriction AppArmor des espaces d'utilisateurs est levée sur la
   machine jetable. Sinon, (R-b), profil dédié à `bwrap`, ou (R-d), image `debian-13`. Et dis si l'on sonde un jour HTTP
   simple (option (a) de R-821). Je ne le recommande pas : (A) n'en a pas besoin, et la sonde relève du classifieur.

**Avant le GO, sans dépense, par la session principale** :

- lecture gratuite par l'API de la disponibilité de cpx32 et des images ;
- lecture, sur Launchpad, de l'empreinte de la clé de signature de deadsnakes, à figer dans l'amorce ;
- versement des v51 et v52 et des sondes de CL16 dans git ;
- correction de CL16-01 ;
- écriture des scripts du § 2 (amorce, sonde de G8, vérification d'entrée, lanceur, destruction) et de leurs essais G1 à
  G7, G12 et G13 contre le faux serveur. G13 se joue aussi hors machine, en exécutant le script d'amorce dans un dossier
  jetable avec des commandes factices, y compris les nouveaux artefacts de la v3 (cible vide, valeur vide). Les artefacts
  (d) à (g) de G8 se jouent de même hors machine, sans aucun réseau ;
- demande à conv-audit de l'`ExecuteurDistantParLots` (§ 2.7) ;
- consignation de l'épisode des sondes de la v1 (§ 8).

## 6. Ce qui n'a pas pu être fait, réserves, SUPPOSÉ

**Pas fait** :

- aucune lecture de l'API Hetzner (consigne : aucune commande vers un fournisseur). La disponibilité des gabarits et des
  images, le prix rendu par l'API et l'`auto_delete` réel de l'adresse créée avec le serveur restent à lire ;
- l'arrondi de facturation n'a pas été trouvé dans la documentation lue ;
- aucune épreuve de `bwrap` sur Ubuntu 24.04 : la conclusion du § 2.2.1 repose sur la documentation, non sur un essai.
  Elle est « probable », et S0 la tranche ;
- aucun script écrit : le présent document les décrit ; les écrire et les éprouver est la suite ;
- aucune sonde réseau (§ 0.1, réserve 7).

**Réserves** :

1. **Option (a) de R-821** : non établie comme infaisable. Seul le HTTPS vers une adresse IP a été essayé ; HTTP simple n'a pas
   été sondé, et le sonder relève du classifieur. Elle ne règlerait de toute façon pas le dépôt du code (§ 2.0).
2. **Restriction AppArmor sur Ubuntu 24.04** : le remède (R-a) affaiblit, sur la machine jetable seulement, une défense contre
   les failles du noyau. Elle est déclarée comme écart d'hôte. (R-b) reste à éprouver sous `--no-new-privs`.
3. **Clé d'hôte SSH** : la première connexion fait confiance à la clé de la machine, consignée. Durcissement possible : clé
   d'hôte jetable injectée par cloud-init. Ce serait une clé privée posée sur la machine, propre à la série et détruite avec
   elle ; ce n'est pas l'un de nos secrets, mais c'est à Lazar d'en décider.
4. **cgroup v2** : chemin jamais joué. La passe A peut échouer par conception (règle « pas de processus internes »). C'est une
   information pour conv-audit, pas un échec de S1.
5. **Python 3.13 sur Ubuntu 24.04** par un dépôt tiers signé : chaîne d'approvisionnement de plus. Le repli 3.12 est un écart à
   CL16, à déclarer.
6. **Les sondes de CL16** ne sont que dans un bloc-notes éphémère ; elles sont perdues si la session se régénère avant leur
   versement.
7. **Fuites résiduelles hors pare-feu du nuage** : selon la FAQ de Hetzner, passent toujours ce pare-feu les métadonnées
   (« answered locally »), le résolveur DNS de Hetzner, **le trafic du système de secours de Hetzner** (ajouté en v3), et
   ARP, DHCP et une partie d'ICMPv6 (IPv6 est désactivé à la création). `nftables` ferme le DNS. Les métadonnées restent
   ouvertes : elles sont locales à l'hôte et ne servent que du public. Le système de secours ne sert qu'à une machine démarrée
   en mode de secours : la session n'active jamais ce mode, et G8 (iii) vérifie `rescue_enabled = false` après chaque
   redémarrage. Ce que couvre au juste « traffic for the Hetzner rescue system » n'est pas détaillé par la FAQ.
8. **Adresse du poste de passage** : si l'adresse IPv4 de ton accès à l'Internet change pendant une série, l'entrée SSH se
   ferme. Il faut alors une mise à jour du pare-feu `entree-<série>` par la session (`set_rules`), consignée.
9. **Sonde de G8** (v3) : la classification lit l'`errno` du noyau. Que `nftables` rende `EPERM` ou un délai à un `connect()`
   TCP n'est pas éprouvé ; les deux sont classés « fermée », donc le verdict n'en dépend pas. Une issue non prévue est
   « indéterminée » et arrête la série : la sonde peut produire de faux arrêts, jamais une fausse fermeture par cible vide.

**SUPPOSÉ** :

- toute heure commencée facturée ;
- TVA 20 % ;
- 1 EUR ≈ 1,15 USD ;
- pare-feu du nuage et clés SSH non facturés ;
- disponibilité de CPX32 en `nbg1`, `hel1` ou `fsn1` ;
- noms d'images `ubuntu-24.04` et `debian-13` (le premier figure dans un exemple de la spécification) ;
- l'image Hetzner `ubuntu-24.04` porte la restriction AppArmor par défaut, sans profil `bwrap` actif ;
- Debian 13 sans restriction AppArmor des espaces d'utilisateurs ;
- transition vers un profil AppArmor dédié permise sous `--no-new-privs` depuis un processus non confiné (remède (R-b)
  seulement) ;
- paquet `python3.13` de deadsnakes pour Ubuntu 24.04, et la forme `ppa:` acceptée par le bloc `apt: sources:` de cloud-init ;
- fichier `/etc/apt/sources.list.d/ubuntu.sources` (format deb822) sur l'image Hetzner ;
- service `nftables` lisant `/etc/nftables.conf` au démarrage ;
- adressage IPv4 par DHCP sur la machine ; métadonnées en `169.254.169.254` port 80 ;
- **v3** : versions de l'image `ubuntu-24.04` (noyau 6.8, systemd 255, `bwrap` 0.9.0) et de `debian-13` (`bwrap` 0.11,
  Python 3.13, systemd 257), reprises de la v1 sans source ; à lire dans `etat-v1.txt` en S0 ;
- **v3** : date d'arrivée du profil `bwrap-userns-restrict` dans `noble-updates`, non copiée (la v2 écrivait « juin 2024 ») ;
- **v3** : fichier `/run/systemd/resolve/resolv.conf` portant le résolveur amont en IPv4 sur l'image Hetzner ;
- **v3** : le pare-feu du nuage jette sans répondre (délai) plutôt qu'il ne rejette ;
- **v3** : refus local de `nftables` rendu au programme par `EPERM` (UDP) et par `EPERM` ou un délai (TCP) ; et curl qui
  rendrait ce refus par son code 7, raison pour laquelle G8 ne lit plus curl ;
- **v3** : Python du système présent en `/usr/bin/python3`, en version 3.10 au moins (`TimeoutError`) ;
- fichier `50-cloudimg-settings.cfg` dans `/etc/default/grub.d/` de l'image, et démarrage par GRUB ;
- cgroup v1 encore démarrable sous systemd 255 par `systemd.unified_cgroup_hierarchy=0` ;
- `auto_delete` de l'adresse IPv4 créée avec la machine : inconnu, d'où le retrait explicite (§ 2.6) ;
- délégation v2 par `systemd-run --scope -p Delegate=yes` ;
- latence de 5 à 10 min par aller-retour au poste de passage ;
- durées des séries (§ 1.3), extrapolées des 340 s de CL17 ;
- passage de `ssh` depuis une session reliée par Contrôle à distance ;
- sens de « (b) » dans R-640 de conv-audit, lu comme « machine louée jetable » (n° 267, passation `2026-10-30-0454.md` :
  « reco (b) de conv-audit ») ;
- une comparaison avec d'autres loueurs à taille égale ne changerait pas le devis de façon décisive.

**Levé depuis la v1** : la limite de 32 Kio des données cloud-init (vérifiée, § 2.0).

**Levé en v3** : `resolvectl query --cache=no` n'est plus SUPPOSÉ, la sonde DNS de G8 ne s'en sert plus ; présence du champ
`rescue_enabled` dans `GET /v1/servers/<id>` (lue dans la spécification copiée).

## 7. Sources lues (empreintes)

### 7.1 Reprises de la v1 (vérifiées par le relecteur)

| pièce | SHA-256 |
|---|---|
| n° 267 de conv-audit (`…/messages/conv-audit_2026-10-30_n267.md` ; branche `canal/conv-audit-n04` lue à `9fb3a398` par la v1, avancée depuis à `37e7f517`, contenu identique selon le relecteur) | `0c77987a0543afaa89903e7a404ca6948f7609aac9d1c8ccaadac422f9ded8ef` |
| n° 266 de conv-audit (même branche) | `b78f9b1e2ed768914b0920bdc8f47db4a152b1c91ee9a1b4b3605663fd4eabfa` |
| `contre-lecture-cl16-orchestrateur-v51-v1.md` | `fec076d24e9d60723bf355631250e24b2d1fec3fa5fa1a7865359148626ead14` |
| `contre-lecture-cl17-orchestrateur-v52-v1.md` | `c5b361090731c526d458bace28eef9bfca4e5e1b647be4e560dc88534d5cb598` |
| `ia-scientifique-externe-v3/essai-a-blanc-v1/architecture-essai-a-blanc-v1.md` | `e38f9661174a8ae2ab48fd78f178ba70b797f8a5c6ac944bfc53fabca641ab29` |
| `ia-scientifique-externe-v3/lecture-code-et-devis-v3-v1.md` (LC) | `1ce823a7475b265a826408af5e25059c61bf43aaec64a129912dbd55f38c64f8` |
| `CODE-orchestrateur-pole-v7-v52.zip` (`origin/canal/session-depot-reprise-n55` `e447f066`) | `25775a6650537f7ed4e547fcfac84d3961a12beddae91f7c0bfd8eb4fb9c1052` (= compagnon) |
| `EMPREINTES-orchestrateur-pole-v7-v52.txt` | `13bc34c763a76ecf1e6b9867fa46e12d4e486458f3cde503909be5f0db94361f` (= compagnon) |
| `CODE-orchestrateur-pole-v7-v51.zip` | `a58a9b8b80861e48fa5e547c4151cc80c15a67a5e6a83d9cf6d4c880dc8f5f46` (= compagnon) |
| `EMPREINTES-orchestrateur-pole-v7-v51.txt` | `8044fa5c5a6512206b1e485d89f8d170cd0de34a13def1b21c5a45daab972c74` (= compagnon) |
| registres lus par la v1 : `decisions.md` (R-567, R-581, R-776, R-782, R-806, R-808, R-809, R-816, R-817, R-821, R-822, R-855), `go.md` (GO-2026-10-30-08, GO-2026-10-30-17), `.claude/hooks/garde_calcul.py` | — |

### 7.2 Nouvelles en v2 (copies dans ce dossier, chacune avec son compagnon `.sha256` et ses en-têtes HTTP)

Toutes lues le 31 octobre 2026 par `curl` à travers le mandataire, sans compte, de 00:36:57 à 00:40:39 UTC. **Aucune copie
nouvelle en v3** ; les heures ci-dessous sont relues dans les fichiers `*.entetes.txt` (ligne `date`/`Date`), et les deux que
la v2 renvoyait aux en-têtes sont désormais écrites. Dans les en-têtes copiés, la valeur des lignes
`set-cookie` est remplacée par `<valeur retirée à la copie>` : ce sont des témoins de visiteur anonyme, sans utilité ici. Les
corps sont gardés tels quels.

| pièce (URL) | fichier | `Date` servie (UTC) | SHA-256 du corps |
|---|---|---|---|
| prix Hetzner, `…/cloud/regular-performance/` | `sources-prix-hetzner-20261031-v1/cloud_regular-performance-v1.html` | 00:40:00 | `805d65bc323b9bebdda81df4767f119110dd5f2b907a3ff9be2c375abaafb408` |
| prix Hetzner, `…/cloud/general-purpose/` | `sources-prix-hetzner-20261031-v1/cloud_general-purpose-v1.html` | 00:40:01 | `55c1c4d18781f59ecd58dad5e0c7ebc17a8273f3545842648a82bedb19b5ea54` |
| prix Hetzner, `…/cloud/cost-optimized/` | `sources-prix-hetzner-20261031-v1/cloud_cost-optimized-v1.html` | 00:40:02 | `bc407cdb50142cb0eafc3442e0fdfba412f485abf7494dba28d96c31285781a9` |
| notes de version d'Ubuntu 24.04, `https://documentation.ubuntu.com/release-notes/24.04/` | `sources-documentation-20261031-v1/ubuntu-notes-version-24.04-v1.html` | 00:36:59 | `9ec193a7e9df48a88af70355017a2eefe8d1c73a7f9dfefa12875bb5da3addc9` |
| billet d'Ubuntu sur la restriction (23.10), `https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces` | `sources-documentation-20261031-v1/ubuntu-blog-espaces-utilisateurs-restreints-v1.html` | 00:36:57 | `1dde5a03928f848b9e0233423618e4cbb9bd43366ae229d2ce67e8241dfd772e` |
| « Understanding AppArmor User Namespace Restriction », `https://discourse.ubuntu.com/t/understanding-apparmor-user-namespace-restriction/58007` | `sources-documentation-20261031-v1/ubuntu-discourse-comprendre-restriction-v1.html` | 00:39:02 | `5a968388962391bd29b643b73a621386d7e4481e770140528efcd70a5da4a424` |
| journal des modifications d'`apparmor` 24.04.9, `https://changelogs.ubuntu.com/changelogs/pool/main/a/apparmor/apparmor_4.0.1really4.0.1-0ubuntu0.24.04.9/changelog` | `sources-documentation-20261031-v1/apparmor-journal-modifications-24.04.9-v1.txt` | 00:40:39 | `58e49d958727ae574904469817bb70cf421d29e09b42e630650501786f9db7c9` |
| versions d'`apparmor` publiées pour 24.04 (API publique de Launchpad, `getPublishedSources`) | `sources-documentation-20261031-v1/launchpad-apparmor-noble-publie-v1.json` | 00:40:32 | `994efcca8a11f1333f939121e76fae4030ebe033076ec63b412b6bf3dc02b22f` |
| R. Coker, « Ubuntu 24.04 and Bubblewrap », `https://etbe.coker.com.au/2024/04/24/ubuntu-24-04-bubblewrap/` | `sources-documentation-20261031-v1/coker-ubuntu-24.04-bubblewrap-v1.html` | 00:37:38 | `018b5e977da8031668cad02de12b84a00b6a438fb24fb78c5809dcc7f98512ba` |
| FAQ des pare-feu Hetzner, `https://docs.hetzner.com/cloud/firewalls/faq/` | `sources-documentation-20261031-v1/hetzner-pare-feu-faq-v1.html` | 00:37:50 | `3e60438934d31a5507b40557755df5d3312a9c9961d5bcd708c2605b9d39a1da` |
| spécification publique de l'API Hetzner, `https://docs.hetzner.cloud/cloud.spec.json` (page de documentation, non l'API) | `sources-documentation-20261031-v1/hetzner-api-specification-v1.json` | 00:38:28 | `772d662e1336ea01925ba30381f47d5c0e23265767dcf9399983aba3dada082a` |
| `tests_de_mort_v2.py` de la v52, lu dans le déballage du relecteur (`…/scratchpad/verif-nuit-devis-machine-jetable/v52/pole/`) | — (dans `CODE-orchestrateur-pole-v7-v52.zip`, `25775a66…`) | — | — |
| relecture de la v1, `…/scratchpad/nuit-rendus/verifier-devis-machine-jetable.md` | — (bloc-notes) | — | — |
| relecture de la v2 (lue pour la v3), `…/scratchpad/nuit-rendus-2/verifier-machine-v2.md` | — (bloc-notes) | — | `aa85ff3cfe78b1dfaa43bcafc071afba2e6bf5f549d8b82d67c4243287815a55` |
| v2 de ce devis, `devis-et-plomberie-machine-jetable-v2.md` (base de la v3, compagnon vérifié par `sha256sum -c`) | ce dossier | — | `39260994753d1cdb4c4ffd4773ec989c8719ed38054a577b5fae19c052b6add8` |

## 8. Épisode des sondes réseau de la v1 (réserve 7 du relecteur) : texte proposé à la session principale

Je n'écris pas les registres. Texte proposé pour `registres/decisions.md`, à la main de la session principale :

> Rédaction de `devis-et-plomberie-machine-jetable-v1.md` (30 octobre, vers 23:03 UTC) : hors mandat (rédiger un devis), le
> sous-agent a sondé le réseau. D'abord `https://1.1.1.1/`, coupé par le mandataire. Puis un nom de domaine et un nom
> `sslip.io`, procédé qui sert à joindre une adresse arbitraire : refusés par le classifieur (« Containment Escape »). Rien n'a
> été contourné. Le nombre de commandes de la seconde sonde (une ou deux) n'est pas établi par la note. Décision : ces sondes ne
> se renouvellent pas sans le mot de Lazar. Ni la v2 ni la v3 n'en font, et l'option (a) de R-821 reste en réserve.

Version 3 ; jamais réécrite (R12). La v1 et la v2 restent en place, inchangées.

## Table des empreintes des pièces servies

| Pièce | Chemin | Lignes | sha256 du fichier source |
|---|---|---|---|
| 1 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon10.md (branche canal/conv-audit-n04)` | l. 5–17, l. 219–258, l. 316–392, l. 622–622, l. 698–702, l. 722–fin | `ea940d56e5ee949e7b71a57488f7c2c8a2b7ac4835f30cb5f98933e4c00c824f` |
| 2 | `docs/notes/ideation-organisme-v1/course-2/texte-III-v1/synthese-texte-III-etroite-v2.md` | l. 383–fin | `a3bd20c4f645fa9f29d69f944f97c94618b651ffde3cbe33ab8373b2d105c3fa` |
| 3 | `docs/notes/ideation-organisme-v1/course-2/tableau-partage-v1/synthese-tableau-partage-v3.md` | l. 122–fin | `ae0282fb084969d7244955d914d0228eeecfea177bd61283479d4f1fde8954ff` |
| 4 | `docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v3.md` | l. 797–fin | `864f3d2745c1d1d7fbe330eb006432361643cc4cd93b7a1693d5f1f7fdfc3f65` |
