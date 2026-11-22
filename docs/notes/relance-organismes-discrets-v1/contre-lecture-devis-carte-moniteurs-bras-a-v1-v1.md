# Organismes discrets, bras A — contre-lecture du devis de la carte des deux moniteurs à modèle de langue, v1 — v1

- **Pièce contre-lue** : `docs/notes/relance-organismes-discrets-v1/devis-carte-moniteurs-bras-a-v1.md`, `6559f7886a599550090cde361fb7d5856631c27c3f008afb8e2bc3c46313fabc` (empreinte refaite, égale au compagnon), branche `origin/relance-bras-a/devis-carte-v3`, commit `76514065` (seul changement depuis `643d4817` : ce devis et son compagnon).
- **Pièces lues, empreintes refaites** : texte `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md`, `cc55502ad4ef0fa1de5f8f4444975fec2eb7f3f77db8913c96f1bdf9225facb1` (6.3 (m) et (n), lignes 766 et 767 ; 6.10, lignes 916 à 935, dont les réglages, lignes 925 et 926, et les trois définitions, ligne 931 ; 6.11, lignes 937 à 960 ; 8.2, ligne 1091 ; 8.4, lignes 1154, 1155, 1164, 1196 à 1199 ; 13.2, lignes 1489 à 1501) ; devis de carte v2, `83240ca61d7c300fc9f4ca802560a6010a2a7c2eb48dd58fe2c214ee03524ecd` (lignes 30 à 125) ; devis de carte v4, `f82514e9326df61f2fbd73f3eab644107f910aae620afe70b3d6ef9fcde7e0f3` (3.3, 5.2, section 8, décision 3) ; configuration de référence `prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`, lignes 41, 103, 105, 115 à 117 seulement ; `registres/depenses.md`, lignes 468 et 515 seulement ; `.claude/hooks/garde_calcul.py`, fonction `decider` (pour le défaut M5).
- **Contre-lecteur** : agent neuf, Claude Opus 5.5 (même modèle que le rédacteur : R2 tenue, diversité de modèle non tenue, comme le dit la réserve 7 du devis). Ni auteur du devis, ni du texte, ni d'aucune pièce du côté habilité.
- **Cloisonnement** : rien ouvert, listé, cherché ni empreinté des chemins exclus du mandat ; aucun chemin cité par le texte suivi. Aucun réseau, aucune dépense, rien committé.
- **Date (UTC)** : 2026-11-22.

## Verdict

**Engageable après corrections.** Les calculs sont justes et les volumes suivent le texte ; aucun défaut bloquant. Cinq défauts majeurs : le téléchargement compté deux fois au pire cas de la ligne du juge (plafond 60 au lieu de 55 USD), une propriété du lanceur du côté habilité affirmée sans marque (et qui ajouterait une exigence au lanceur), l'absence de règle de partage de la dépense entre deux lignes sur une seule instance, un fondement incomplet de la supposition S1, et un inconvénient omis de l'option recommandée à la décision 2 (échéance des lignes de GO). Sept défauts mineurs.

## 1. Calculs refaits par programme

Programme indépendant (Python 3, bibliothèque standard), joué le 2026-11-22. Tous les nombres du devis sont retrouvés :

| grandeur | devis | refait |
|---|---|---|
| s par lecture, juge | 4,5806 à 4,8477 ; borne 9,6954 | 4,58055 à 4,8477 ; 9,6954 |
| surcoût du juge | 0,133 (au haut) | 0,1326 au haut, 0,1394 au bas (« ≈ 13 % » juste) |
| ligne A, heures | 8,1467 à 8,6089 | 8,14667 à 8,60889 |
| ligne B, heures | 8,2432 à 9,6181 | 8,2432 à 9,61813 |
| ensemble, heures ; attendu | 16,39 à 18,23 h ; 20,39 à 25,70 USD | identique |
| pire cas A ; B | 51,52 ; 57,09 | 51,5211 ; 57,0921 |
| recalculés, débits égaux aux hypothèses hautes | 27,76 → 28 ; 30,55 → 31 | identique |
| recalculés, `d` = 40 ; 42,8 ; 45 | 99 ; 104 ; 108 | 99 ; 104 ; 108 |
| option (c), temps de mur | ≈ 9 à 11 h | 9,24 à 10,62 h |
| écart au repli | 0,139 ; 0,061 | 0,1391 ; 0,0609 |
| formule de repli de `tB` | 2 × (1,0275 × d / 10 + 0,45) | égale à 2 × tJ(d / 10) |

Sources des chiffres vérifiées : 40,2 et 42,8 s, 0,45 s (devis v2, lignes 42, 43, 45) ; 1,1833 USD par heure (registre des dépenses, ligne 515) ; 1,30, 0,08, 40 Go, 0,05 USD par Go, lot 8, 400 jetons (configuration de référence, lignes 41, 103, 105, 115 à 117) ; règles de l'attendu, du pire cas et des arrondis (devis v4, 3.3 et 5.2 ; devis v2, lignes 69, 80 à 82, 96 à 101) ; 6 400 = 5 × 16 × 80 (texte, lignes 918 et 960) ; « 102 points de lecture » (texte, lignes 960 et 1490) ; ≈ 15 à 16 h et ≈ 19 à 23 USD du devis v3 (repris au devis v4, point 5 et ligne 358).

## 2. Points vérifiés sans défaut

- **Volumes** : 6 400 lectures avec raisonnement par moniteur, au plus (6.10, ligne 918 ; 6.11, ligne 960 ; 13.2, ligne 1490) ; actions non appliquées non lues, donc majorant (ligne 930) ; lecture commune sur la machine louée, dans l'exécution unique (13.2, ligne 1499) ; trois sous-commandes, la carte ne servant qu'à l'étape de discrétion (ligne 1499) ; base « mots et coût » et trois autres moniteurs sur processeur (ligne 960) ; les trois définitions de la ligne 931 (agrégateur, traits de surface, permutations perdues) ne touchent que le calcul sur processeur et l'instance d'analyse : hors de ce devis à bon droit.
- **Réglages** : 400 jetons, température 1,0, balise imposée, lots de 8, `bfloat16`, `sdpa`, cas A et cas B, modèles et révisions (lignes 922 à 928) : justes (sauf l'omission du défaut m1).
- **Prix et règles** : attendu (bas × 1,1833 + 1 ; haut × 1,30 + 2), pire cas (haut × 4 × 1,38 + 4), arrondis : conformes à la v4, 3.3 et 5.2, sauf le défaut M1.
- **Suppositions** : S1 à S6 toutes marquées, avec leur fondement et la réponse transmise ; S4 et S5 dites non posées ; S6 juste (≈ 16 et ≈ 15 Go en `bfloat16`, sous 40 Go, soit 1 à 2 USD de téléchargement).
- **Décisions** : décision 1 sans défaut (dépense) ; défaut de la décision 2 = (a), qui n'accorde aucune dépense : conformes. Option (b) de la décision 1 justement dite contraire à la lettre ; option (c) justement dite contraire à l'exécution unique.
- **Lettre de 13.2, ligne 1493** (« une par ligne de carte, par lot de lecture et par lecture de moniteur à modèle de langue ») : deux lignes, une par lecture de moniteur, la tiennent. Le texte distingue les deux lignes de carte de la course des lectures des moniteurs (13.2, ligne 1490 ; 6.11, lignes 959 et 960) : la carte des moniteurs n'est pas une troisième « ligne de carte » qui demanderait une troisième ligne de GO. Le rattachement de la mise en route à la ligne A et de la lecture commune à la ligne B est un choix, à déclarer (m7).
- **Rien ne change le texte**, sous la correction M2 (qui retire une exigence implicite faite au lanceur du côté habilité).

## 3. Défauts, classés, avec correction mot pour mot

### Majeurs

**M1 — Téléchargement compté deux fois au pire cas de la ligne B.** L'attendu de la ligne B dit « pas de téléchargement de plus (compté à la ligne A) », et la réponse (4) établit qu'une relance reprend sur la même instance ; le pire cas de la ligne B ajoute pourtant 4 USD de téléchargement, et la formule `PB` aussi. Sans eux : 53,09 USD, plafond de repli 55 USD (règle des 5 USD supérieurs), non 60 ; ensemble 110, non 115. Recalculés : 28 + 27 = 55 ; `d` = 40 : 47 + 48 = 95 ; 42,8 : 49 + 51 = 100 ; 45 : 51 + 53 = 104 (C, refait).

Corrections :
- Section 4, ligne B : remplacer « - **Pire cas** : 9,62 h × 4 × 1,38 + 4 = 57,09 USD ; **plafond de repli : 60 USD** (C). » par « - **Pire cas** : 9,62 h × 4 × 1,38 = 53,09 USD, sans téléchargement (compté à la ligne A ; une relance reprend sur la même instance, réponse 4) ; **plafond de repli : 55 USD** (C). »
- Section 4, ensemble : « plafonds de repli 55 + 60 = 115 USD » → « plafonds de repli 55 + 55 = 110 USD ».
- Section 4, formule : « `PB = 2 × 1,38 × (6 400 × tB / 3 600 + L) + 4` » → « `PB = 2 × 1,38 × (6 400 × tB / 3 600 + L)` (sans téléchargement : compté à `PA`) ».
- Section 4, exemples : « 28 + 31 = **59 USD** » → « 28 + 27 = **55 USD** » ; « 47 + 52 = 99 USD ; `d` = 42,8 s, 49 + 55 = **104 USD** ; `d` = 45 s, 51 + 57 = 108 USD » → « 47 + 48 = 95 USD ; `d` = 42,8 s, 49 + 51 = **100 USD** ; `d` = 45 s, 51 + 53 = 104 USD ».
- Section 0, point 3 : « **60 USD** ; ensemble **115 USD** (C) » → « **55 USD** ; ensemble **110 USD** (C) ».
- Section 0, point 4 : « ≈ 28 + 31 = **59 USD** » → « ≈ 28 + 27 = **55 USD** » ; « ≈ 47 à 51 + 52 à 57 USD, **99 à 108 USD** : 6 à 14 % sous le repli (C) » → « ≈ 47 à 51 + 48 à 53 USD, **95 à 104 USD** : 5 à 14 % sous le repli (C) ».
- Section 5, ligne (3) : « plafond du juge 60 USD au lieu de 80 » → « plafond du juge 55 USD au lieu de 80 » ; ligne (1) : « restent à 6 à 14 % du repli » → « restent à 5 à 14 % du repli ».
- Section 7, décision 1, option (b) : « (115 USD de repli) » → « (110 USD de repli) ». Décision 2 : « (55 et 60 USD) » → « (55 et 55 USD) » ; « 6 à 14 % sur le repli (99 à 108 USD contre 115, section 4) » → « 5 à 14 % sur le repli (95 à 104 USD contre 110, section 4) » ; « 115 USD de plafonds » → « 110 USD de plafonds ».
- Section 9, programme : « `PB = B_h * 4 * pire + 4` » → « `PB = B_h * 4 * pire` » et « `PB_m = lambda tB, L: 2 * pire * (h(n * tB) + L) + 4` » → « `PB_m = lambda tB, L: 2 * pire * (h(n * tB) + L)` » ; rejouer et remplacer la sortie ; contrôles : « 1 − 99 ÷ 115 = 0,139 et 1 − 108 ÷ 115 = 0,061 » → « 1 − 95 ÷ 110 = 0,136 et 1 − 104 ÷ 110 = 0,055 ».
- Commit et compagnon : « 55 et 60 USD de repli » → « 55 et 55 USD de repli ».

(Si le rédacteur veut garder les 4 USD à la ligne B, il doit écrire pourquoi une relance de la ligne B retéléchargerait un modèle, contre la réponse (4) ; en l'état, rien ne le fonde.)

**M2 — Propriété du lanceur du côté habilité affirmée sans marque.** La décision 1 dit que la ligne B est celle « que le lanceur exige avant la production des scores du juge », et son option (a) que « la ligne B se vérifie dans le lanceur, en cours d'exécution ». Rien de tel n'est dans le texte (13.2, ligne 1499 : six étapes, aucune ne lit le registre des GO) ; c'est une propriété supposée du code du côté habilité, non marquée parmi S1 à S6 ; et la poser comme condition ajouterait une exigence au lanceur que le texte ne contient pas. La garde de calcul du dépôt accepte plusieurs identifiants de GO dans une même commande de création et les vérifie chacun (`.claude/hooks/garde_calcul.py`, fonction `decider`) : les deux lignes peuvent être exigées à la création, sans rien demander au lanceur.

Corrections :
- Section 7, décision 1, « Décision » : remplacer « et la ligne B (juge, ouvertures, lecture commune), que le lanceur exige avant la production des scores du juge. » par « et la ligne B (juge, ouvertures, lecture commune) ; les deux identifiants de GO sont cités dans la commande de création de l'instance, qui ne se crée pas sans l'un d'eux ; rien n'est demandé au lanceur de l'étape de discrétion. »
- Option (a), inconvénient : remplacer « inconvénient : la ligne B se vérifie dans le lanceur, en cours d'exécution, non à la création de l'instance. » par « inconvénient : la ligne B doit être accordée avant la création de l'instance, bien qu'elle ne serve qu'après les ≈ 8 h de la ligne A ; la dépense des deux lignes, sur une seule instance, se partage par la règle de la section 4. »
- Recommandation : « confiance moyenne à haute (la vérification de la ligne B par le lanceur est du côté habilité) » → « confiance moyenne à haute ».
- Section 6, ligne « ligne de GO de la lecture » : « la sienne | la sienne » → « les deux, citées à la création de l'instance | (citée à la création) ».

**M3 — Aucune règle de partage de la dépense ni de coupure entre deux lignes sur une seule instance.** Le devis pose deux plafonds (55 et 55 après M1) sur une instance dont le coût cumulé va jusqu'à ≈ 105 USD au pire ; il ne dit ni quel compteur s'arrête au plafond de la ligne A, ni à quel instant la ligne B commence à compter, ni ce que devient l'exécution unique si la ligne A atteint son plafond au milieu. Une coupure de l'instance réglée sur le seul plafond de la ligne A arrêterait la ligne B en cours.

Correction : ajouter à la section 4, après « **Arrêts** : … » :
« **Partage sur une seule instance** : la coupure de l'instance est la somme des plafonds des deux lignes ; le compteur de la ligne A court de la création de l'instance à l'horodatage de la dernière lecture du moniteur boîte noire, écrit au manifeste de sa production ; celui de la ligne B, de cet horodatage à la destruction de l'instance ; chaque ligne s'arrête à son propre plafond sur son compteur, relevé au registre des dépenses. Un arrêt au plafond de la ligne A, au milieu de l'exécution unique, suit la règle de la panne (13.2, ligne 1499) : scores déjà produits versés et scellés sans être ouverts, aucun agent ne reçoit de fichier de scores avant la ligne d'ouverture ; reprise par nœud (8.2, ligne 1091). »

**M4 — Fondement de S1 incomplet sur un facteur connu et défavorable.** S1 égale une lecture du moniteur au temps d'une action de l'agent. Or une action de l'agent génère 223 jetons en moyenne (devis v2, ligne 44), une lecture avec raisonnement jusqu'à 400 (6.10, ligne 925) ; si les lectures vont souvent au bout (la ligne 929 prévoit justement une part de « balise imposée après troncature »), le décodage peut être jusqu'à ≈ 1,8 fois plus long. Le doublement de la règle du pire cas couvre alors le débit plus lent ou une relance, non les deux (la même remarque a été faite et acceptée au devis v4, 5.2, dernier point). Par ailleurs S2 prend le débit du juge (Qwen, 7 milliards) égal à celui de Llama (8 milliards) sans le marquer.

Corrections :
- Tableau des suppositions, S1, colonne « fondement » : ajouter à la fin « ; **réserve** : une action de l'agent génère 223 jetons en moyenne (devis v2, ligne 44), une lecture avec raisonnement jusqu'à 400 ; si les lectures vont souvent au bout, le décodage peut être jusqu'à ≈ 1,8 fois plus long : la borne haute écrite (le double) couvre ce débit plus lent ou une relance, non les deux ».
- S2, colonne « fondement » : ajouter au début « le débit de génération du juge (7 milliards de paramètres, autre tokeniseur) pris égal à celui du moniteur boîte noire (supposé) ; ».
- Section 8, réserve 1 : ajouter « L'action de l'agent génère 223 jetons en moyenne, la lecture jusqu'à 400 : l'attendu peut être sous-estimé jusqu'à ≈ 1,8 fois, et le doublement du pire cas n'absorbe alors plus une relance (devis v4, 5.2). »
- Section 0, point 5 : après « aucun débit des moniteurs n'est mesuré (réponse 1) », ajouter « , et la lecture avec raisonnement peut générer jusqu'à ≈ 1,8 fois plus de jetons qu'une action de l'agent ».

**M5 — Option recommandée de la décision 2 : échéance des lignes de GO omise.** Une ligne de GO de calcul a une période de validité, vérifiée à chaque création d'instance (`.claude/hooks/garde_calcul.py`, `decider` : « hors de sa période de validité »). Accordées dès la contre-lecture, les deux lignes peuvent échoir avant l'étape (m), qui vient après la course entière ; l'avantage annoncé de l'option (b), « aucun tour de GO à la fin », tombe alors.

Corrections :
- Section 7, décision 2, « Décision » : après « utilisables seulement après la garde de production ; », ajouter « échéance de chaque ligne fixée au-delà de la date prévue de l'étape (m) ; ».
- Option (b), inconvénient : ajouter « ; si l'échéance des lignes passe avant l'étape (m), la garde de calcul refuse la création et un tour de GO revient à la fin ».
- Section 6 : ajouter la ligne « | échéance de la ligne de GO non passée le jour de la création | garde de calcul du dépôt | oui | oui | ».

### Mineurs

**m1 — Réglages incomplets (section 2).** La ligne 925 fixe cinq réglages ; le devis en liste quatre (le seuil de masse faible manque). Remplacer « avec raisonnement ; 400 jetons générés au plus ; température 1,0 ; balise absente imposée ; lots de 8 » par « avec raisonnement ; cinq réglages : 400 jetons générés au plus ; température 1,0 ; balise absente imposée ; seuil de masse faible 0,5 ; lots de 8 ».

**m2 — Colonne « avant » de la section 5 sans source.** « facteur 1,0 à 1,255 », « borne de 4 h », « 80 » ne sont dans aucune pièce versée (absents du devis v4). Ajouter sous le titre de la section 5 : « La colonne « avant » décrit l'état de travail de ce devis avant les réponses du 22 novembre, non versé et sans empreinte ; ses nombres ne sont opposables à rien. »

**m3 — Étapes (2) et (3) du lanceur non comptées.** Le tirage de la table et la préparation des demandes (13.2, ligne 1499) tournent avant la production. Ajouter au tableau de la ligne A, avant « lectures » : « | table et préparation des demandes (13.2, ligne 1499, étapes 2 et 3) | une fois | négligeable (S) | ».

**m4 — Règle d'arrondi du plafond de la ligne A.** La v4 arrondit à l'unité le plafond de sa ligne 1, sans mesure (17,92 → 18), et aux 5 USD le seul repli de sa ligne 2. Section 3, « Règles de calcul » : remplacer « plafond de repli arrondi aux 5 USD supérieurs » par « plafond de repli arrondi aux 5 USD supérieurs (les deux lignes sont des replis : un recalcul est prévu à l'étape (m), comme pour la ligne 2 de la v4, 5.2) ».

**m5 — Décision 2, enjeu.** Rien dans le texte ne mesure le débit des moniteurs avant l'étape (m) ; l'option (a) n'a donc en pratique que le gain sans mesure. Ajouter à l'enjeu : « Aucune étape du texte ne mesure le débit des moniteurs avant l'étape (m) : sans dépense de plus, le gain de l'option (a) est celui-là. »

**m6 — Passe de contexte du juge (S2).** Les 0,45 s du devis v2, ligne 45, sont une passe d'activations par épisode, à une taille de lot que le devis v2 ne dit pas. S2, colonne « fondement » : après « comptée **0,45 s** », ajouter « (en lots, comme à l'autre chaîne : supposé) ».

**m7 — Rattachement des postes aux deux lignes.** Décision 1, « Enjeu » : ajouter « Le rattachement de la mise en route (deux modèles) à la ligne A, et des ouvertures et de la lecture commune à la ligne B, est un choix de ce devis : la lettre de 13.2 nomme une ligne par lecture de moniteur, non le partage de ces postes. »

## 4. Réponses aux sept questions du mandat

1. Chiffres sourcés et calculs justes : oui (section 1), sauf la règle appliquée au pire cas de la ligne B (M1) et la colonne « avant » (m2).
2. Volumes : conformes au texte (6 400 par moniteur, réglages de 6.10, lecture commune sur la machine louée) ; un réglage omis (m1).
3. Suppositions : S1 à S6 marquées ; S1 à compléter (M4) ; une propriété du côté habilité non marquée (M2).
4. Attendu, pire cas, plafonds : règles de la v2 et de la v4 suivies, sauf le téléchargement de la ligne B (M1) ; plafonds corrigés 55 + 55 = 110 USD.
5. Décisions : options honnêtes, recommandations défendables, défauts conformes (aucun n'accorde de dépense) ; à compléter par M2, M5, m5.
6. Deux lignes de GO : tiennent la lettre de 13.2, ligne 1493 ; à appliquer par la création de l'instance sous les deux identifiants (M2) et une règle de partage (M3).
7. Rien ne change le texte, une fois M2 corrigé.
