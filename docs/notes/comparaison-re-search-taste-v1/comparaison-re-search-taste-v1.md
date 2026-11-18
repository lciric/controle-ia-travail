# Re-Search et TASTE : arbitrage des deux lectures des conditions de protocole, et ce qu'il faut en garder pour les trois essais proposés à l'organisme d'idéation — v1

> **Pièce privée : TASTE est cité avec l'accord de Lazar pour un usage interne seulement ; ne quitte pas le dépôt privé ; aucune citation publique sans accord des auteurs (R-3167).**
> Cette note est à exclure par son nom de toute copie publique, comme les deux lectures qu'elle arbitre (R-3181). TASTE n'est cité ici ni comme publié ni comme opposable hors du dépôt.

- Arbitre : sous-agent neuf ; n'a écrit ni les deux lectures arbitrées, ni la lecture de Re-Search, ni son audit, ni les propositions, ni la contre-lecture. Rédigé le 18 novembre 2026, après lecture complète des deux notes.
- Statut : arbitrage de lectures, **rien d'adopté**. Aucune hypothèse, revendication, préenregistrement ni devis n'est changé ; les recommandations sont des options pour Lazar (P3 est une dépense : nœud de décision). Aucune dépense, aucun appel de modèle, aucun appel externe, aucun contact, aucun commit. Aucun résultat sous embargo ouvert. Le brouillon de message aux auteurs de Re-Search n'est ni ouvert ni repris.
- Les trois essais : **P1**, le jeu de questions fermées où le monde planté répond lui-même (instrument de mesure de la recherche des proposeurs indépendant du juge, N-058) ; **P2**, la mesure de la diversité des formes dans la mémoire ; **P3**, le panorama de formes candidates offert au questionneur.

## Pièces et empreintes (recalculées par l'arbitre)

| pièce | empreinte sha256 | état |
|---|---|---|
| lecture « protocole » `lecture-protocole-v1.md` (renvoi **LP:ligne**) | `fcb8c4fd54ba1f58d3a7efe73df135f4f86ae2168192bbea3c44c4a47458bb1a` | conforme au compagnon |
| lecture « conséquences » `lecture-consequences-v1.md` (renvoi **LC:ligne**) | `b64f3870a8a6f420a998dee4f3075087f4b9cce14a9ab3e62522614c47ceb69e` | conforme au compagnon |
| TASTE, PDF reçu de Lazar (hors dépôt, dossier des pièces jointes de la session) | `f9aed18c7ee9e1c40a11299a0e7529596a9aa56410a427908e764ddd7d7d068f` | recalculée : conforme à R-3154 ; 61 pages |
| TASTE, texte `taste.txt` du brouillon de la session (renvoi **T p. P, l. L**) | `ab18fb48089155a7a9e19176104ae376e61d41feade3b1bd07bbb78fa9148221` | **identique à l'octet** à l'extraction du PDF en mise en page (vérifié par `cmp`) ; les sauts de page du texte donnent les pages du PDF |
| Re-Search, PDF arXiv 2611.14487 v1 (brouillon de la session) (renvoi **RS p. P**) | `ae848c68e65c4a779d0df6725e4189ad80c351fe2e9402930be14db2ddfa7ccc` | recalculée : conforme aux pièces |
| pièces de Re-Search extraites de la branche `lot/compte-organisme-v1` (commit `4f2a259`) : lecture (**lecture:ligne**), propositions (**prop:ligne**), contre-lecture (**contre:ligne**), table remplie (**remplie:ligne**) | voir LP:16-20 | toutes conformes à leurs compagnons (`sha256sum -c`, aucun écart) |

Portée des chiffres (R7). Les chiffres de TASTE cités ici sont **vérifiés comme ce qu'écrivent les auteurs**, sur PDF empreinté, page citée ; ils ne sont pas reproduits, et la pièce est privée : ils ne vont dans aucune pièce destinée à l'extérieur. Les chiffres de Re-Search que l'arbitre a rouverts sur le PDF sont marqués ; les autres restent de seconde main (lecture et audit de la session).

## Verdict en trois lignes

1. Les deux lectures concordent sur l'essentiel et leurs citations tiennent : 45 sur 47 rouvertes, plusieurs avec une portée omise ; 2 ne tiennent pas telles qu'écrites, et aucune ne change une conclusion. Re-Search mesure la reconnaissance d'une cible connue par l'intermédiaire d'un répondeur modèle ; TASTE mesure la prédiction d'une préférence d'expert sans vérité de terrain. Il n'y a pas de contradiction établie entre les deux ; ce qui les sépare, c'est l'existence d'une référence.
2. TASTE n'apporte aucune vérité à reprendre, mais il apporte cinq conditions de protocole qui manquent à nos essais : jouer les deux ordres et rapporter l'effet d'ordre à part, geler l'effort de raisonnement, prendre le simple retirage comme étalon, écrire une règle des refus qui ne remplace jamais une réponse par celle d'un autre modèle, fixer les plafonds à l'aveugle et en donner la sensibilité. Il donne aussi un contre-exemple (la réponse d'un autre modèle substituée aux refus).
3. On garde les trois essais et on modifie les trois. Pour P3, il faut répartir d'avance la position de la forme vraie et du leurre, ajouter une carte écrite avant toute question, et refaire le devis : au pire 740,09 USD selon la contre-lecture, 866,97 USD avec toutes les options (calculs vérifiés, ordres de grandeur). Le résultat nul y devient une issue sérieuse. N-058 sort renforcée, et sa borne est confirmée : l'instrument ne dit rien du jugement d'idées en langue libre.

## 1. Citations rouvertes et ce qui tient

Tirage : 47 citations prises dans les deux notes, réparties sur toutes les conditions et sur les deux sources, plus 11 passages de Re-Search rouverts directement sur son PDF. « Tient » = le passage dit ce que la note lui fait dire, à la page et à la ligne données.

### TASTE (sur le texte identique au PDF empreinté)

| n° | citée par | renvoi | ce que la note en tire | verdict |
|---|---|---|---|---|
| 1 | LP, LC | T p. 1, l. 17-20 | modèles d'environ 41 % (hasard) à 60 %, humains estimés à 77 % | tient |
| 2 | LP | T p. 8, l. 513 | 53 % d'accord des préférences individuelles | tient (aussi l. 24-25 et 111) |
| 3 | LC | T p. 7-8, l. 452-453, 504-505 | 53 %, 68 %, 83 % sur 18 paires | **tient en partie** : 68 % (l. 453) et 68 → 83 % pour n = 58 → 18 (l. 504-505) tiennent ; **53 % n'est pas à ces lignes** (il est l. 513) |
| 4 | LP, LC | T p. 6, l. 384-387 | jusqu'à 25 points de changement quand on inverse l'ordre, lié négativement à la performance même après moyenne | tient |
| 5 | LP, LC | T p. 5, l. 309-311 | les deux ordres joués et moyennés | tient ; la moyenne porte aussi sur les deux variantes d'invite (question montrée ou cachée), ce qu'aucune note ne dit dans le tableau |
| 6 | LC | T p. 43, l. 2664-2670 | corrélation de −0,46 entre sensibilité à l'ordre et justesse | tient (corrélation de Pearson entre modèles) |
| 7 | LP | T p. 44, l. 2789-2790 ; LC : p. 42, l. 2621-2626 | selon le modèle, la sensibilité vient du seul retirage ou s'y ajoute | tient |
| 8 | LP, LC | T p. 25, l. 1441-1445 | refus du modèle classé premier comblés en dernier recours par la réponse d'un autre modèle ; 9 cellules sur 184 | tient ; **les deux notes omettent la portée** : le compte de 9 sur 184 vaut à effort maximal sous le cadre « situationnel » (l. 1444) |
| 9 | LP, LC | T p. 36, l. 2146-2152 | sans les quatre propositions sur-représentées, 52 paires, référence humaine d'environ 70 % | tient |
| 10 | LP | T p. 31, l. 1847-1849 ; p. 26, l. 1465 | humains notant de mars à juin 2026 comme au 1er février 2026 ; modèles sortis jusqu'au 24 juillet 2026 | tient ; **nuance** : le passage est dans l'invite donnée aux modèles évalués, qui reçoivent donc la même date fictive (voir désaccord 7) |
| 11 | LC | T p. 6, l. 356-358 | le modèle classé premier passe de 48 % à 60 % selon l'effort | tient |
| 12 | LP, LC | T p. 17, l. 941-943 | sélectionner par ressemblance aux propositions humaines monte la qualité jugée, baisse la nouveauté | tient (aveu des auteurs, non mesuré) |
| 13 | LP | T p. 38, l. 2333-2334 ; p. 37, l. 2324-2326 | paires de même question : modèle classé premier 31 % contre 69 % ; humains 82 % contre 76 % | tient |
| 14 | LP | T p. 21-22, l. 1193-1200 | 77,4 % sur 85 paires, 7 égalités écartées ; plage de 70 à 82 % selon la règle de retrait | tient |
| 15 | LC | T p. 5, l. 302-304 | 77 % sur 85 paires | tient |
| 16 | LP, LC | T p. 7, l. 429-435 | biais vers la question motivante montrée ; +17 points sur 18 paires quand on la retire | tient |
| 17 | LC | T p. 15, l. 857-863 | diversité obtenue en variant les résumés servis ; un quart des appels sans contexte | tient (5 sur 20) |
| 18 | LP | T p. 24, l. 1353-1354 | un chercheur fournit environ 40 % des étiquettes d'or | tient |
| 19 | LP, LC | T p. 2, l. 121-122 ; p. 10, l. 617-626 | banc et données humaines sur demande ; invites en annexe | tient |
| 20 | LP, LC | T p. 51, l. 3182 | la consigne du générateur dit que la nouveauté n'a pas de valeur en soi | tient |
| 21 | LC | T p. 19-20, l. 1071-1087 | la note 1 de la grille humaine renvoie à une idée typique de modèle | tient (aussi l. 225-228) |
| 22 | LP, LC | T p. 45, l. 2798-2808, 2843-2844 | nouveauté relative à la littérature jugée par les modèles ; suit l'étiquette d'or, non corrélée à leurs préférences | tient |
| 23 | LP | T p. 46, l. 2892-2896 | résumés, taxonomie et classement des désaccords faits par un modèle | tient |
| 24 | LP | T p. 38, l. 2368-2369 | justifications « dirigées par la question » classées par un modèle | tient |
| 25 | LP | T p. 49, l. 3053-3068 | essai à l'aveugle : dernière et 37e sur 74 | tient ; **omis** : propositions d'un autre échafaudage, décembre 2025 (l. 3053-3054) |
| 26 | LP | T p. 25, l. 1411-1412 | probabilité de 0,5 = demi-réussite | tient |
| 27 | LP | T p. 31-32, l. 1873-1905 | paragraphe de 80 à 120 mots puis probabilité | tient |
| 28 | LP | T p. 17, l. 938-947 | sélection à 3 par un agent modèle avec retour humain sur la diversité | tient (l. 945-946) |
| 29 | LP | T p. 3, l. 155-171 | 93 propositions humaines, 45 questions, 135 propositions | tient ; l'annexe précise 67 questions avant filtrage à 45 (l. 853-854) |
| 30 | LP | T p. 5, l. 286-297 | accord humain simulé par tirage d'une note chez deux autres chercheurs | tient ; les auteurs le disent légèrement sous-estimé (l. 295-296) |
| 31 | LP | T p. 47, l. 2955-2960 | la discussion apporte un signal que la moyenne des notes n'apporte pas | tient |
| 32 | LC | recherche sur le texte entier | « contamination », « cutoff », préenregistrement, température : absents | tient (zéro occurrence chacun, recompté) |

### Re-Search (pièces de la session, et PDF quand marqué)

| n° | citée par | renvoi | ce que la note en tire | verdict |
|---|---|---|---|---|
| 33 | LP | lecture:69 ; **RS p. 4** | 498 paires, accord de Fleiss 0,83, 91,2 % | tient sur la pièce **et sur le PDF** |
| 34 | LP, LC | lecture:104-107 ; **RS p. 6** | réservoir : choix parmi quatre, sans référence ni leurre, ordre non rapporté | tient ; sur le PDF entier, aucune occurrence d'un tirage ou d'un mélange de l'ordre (recherche de « shuffl », « random order », « randomi ») |
| 35 | LP | lecture:32 ; **RS p. 7** | choix au hasard dans le réservoir pas significativement meilleur que jouer seul | tient sur le PDF |
| 36 | LP | lecture:34 ; **RS p. 7** | le plus fort comme sélecteur : −0,59 [−0,90 ; −0,28] | tient sur le PDF |
| 37 | LP, LC | lecture:113 ; **RS p. 7** | l'inquisiteur ne sait pas si la solution est dans le panorama | tient sur le PDF |
| 38 | LP | lecture:115 ; **RS p. 15** | leurre : technique réelle de même famille, longueur voisine | tient sur le PDF |
| 39 | LP | lecture:116 ; prop:109 ; **RS p. 16** | ligne de l'idée interrogée dans 78 à 90 % des parties contre 45 à 67 % pour ses voisines | tient sur le PDF |
| 40 | LP, LC | lecture:119 ; **RS p. 15** | mention comptée seulement si les deux annotateurs modèles la marquent | tient sur le PDF |
| 41 | LP | lecture:86 ; **RS p. 4** | articles postérieurs à toutes les coupures annoncées | tient sur le PDF |
| 42 | LP | lecture:59 ; **RS p. 5** ; **RS p. 6** | 795 réponses annotées, 94,0 % ; quatre modèles proposent sur le même historique | tient sur le PDF |
| 43 | LP, LC | lecture:87, 117, 152 | panorama écrit par un modèle plus récent sans coupure rapportée et qui connaît la solution ; rien de publié | tient sur la pièce |
| 44 | LP, LC | contre:34-35, 44, 62-67 | carte freinée sur trois champs ; Inconnu humain 20,4 % ; softmax ; P1 et P3 hors table ; critère A/A ; trois issues et puissance ; 539,21 USD ; carte à zéro question | tient sur la pièce |
| 45 | LP | prop:129-135, 155-157 | 200,88 + 370,05 = 570,93 USD pour P3 ; 907,40 USD pour les trois | tient ; sommes refaites |
| 46 | LC | lecture:86-87 | « la date de parution des articles tient lieu de mesure de la nouveauté » | **ne tient pas comme citation** : ces lignes traitent de la contamination ; la qualification est du lecteur |
| 47 | LC | contre:67 | la contre-lecture demande déjà une carte à zéro question | tient, mais pour P1 ; elle vaut pour P3 parce que les bras de P3 sont ajoutés au jeu de P1 (prop:104) |

Bilan : 45 tiennent, dont plusieurs avec une portée omise (n° 5, 8, 10, 25, 29) et une avec nuance (n° 47) ; 2 ne tiennent pas telles qu'écrites (n° 3 en partie, n° 46) ; l'ancrage fautif du 53 % chez LC (n° 3) se retrouve en LC:70. Aucune citation inventée.

## 2. Tableau fusionné des conditions de protocole

Marques : **[v]** citation rouverte par l'arbitre et qui tient ; **[v-pdf]** rouverte aussi sur le PDF de Re-Search ; **[s]** non rouverte, de seconde main par les lectures ; **[a]** lecture de l'arbitre ou d'un lecteur, non écrite dans la source.

| condition | Re-Search | TASTE (affirmations des auteurs) | ce que cela implique pour nous |
|---|---|---|---|
| **Qui propose** | Six inquisiteurs posent les questions et écrivent la carte (lecture:16-17) [v] ; réservoir : quatre modèles proposent sur le même historique (lecture:32, 104 ; RS p. 6) [v-pdf] ; panorama écrit par un modèle plus récent qui connaît la solution (lecture:87, 117) [v]. | Un seul générateur sous échafaudage, 93 propositions humaines en amorce, 45 questions retenues sur 67, 135 propositions (T p. 3, l. 155-171 ; p. 15, l. 853-854) [v] ; tri par un correcteur modèle, puis par un agent modèle avec retour humain sur la diversité (T p. 15-17, l. 866-870, 938-947) [v]. | Re-Search fait varier le proposeur, TASTE le juge. TASTE ne dit rien de la composition des proposeurs (N-058). |
| **Qui juge : l'acte** | Le modèle sous essai produit ; il ne choisit que dans le réservoir (lecture:104) [v] et, indirectement, en interrogeant l'idée offerte (lecture:113) [v-pdf]. | Le modèle sous essai prédit quelle proposition l'expert a mieux notée : paragraphe court puis probabilité (T p. 31-32, l. 1873-1905) [v] ; variante en note isolée (T p. 6, l. 353-358) [v]. | « Juger » ne désigne pas le même acte : choisir ou interroger, validé par un oracle, contre prédire une préférence. |
| **Qui juge : le score** | Trois juges modèles de 1 à 10 ; le répondeur est aussi juge, inquisiteur et annotateur (lecture:17, 62, 120) [v]. | Accord avec l'étiquette d'or humaine, demi-réussite à 0,5 (T p. 25, l. 1411-1412) [v] ; analyses secondaires faites par un modèle sans contrôle humain (T p. 38, l. 2368-2369 ; p. 46, l. 2892-2896) [v]. | Dans P1 et P3 le score est du code ; toute mesure secondaire doit l'être aussi. |
| **Référence** | Solution extraite par un modèle, juste à 93 % sur 100 articles contrôlés, 100 non contrôlés (lecture:15, 67) [v] ; réservoir sans référence (lecture:105) [v]. | Aucune vérité de terrain (T p. 1, l. 43-47) [v] ; préférence d'un chercheur « ancre » filtrée (T p. 4-5, l. 247-283) [v] ; accord de chercheurs tenus à l'écart estimé à 77,4 % sur 85 paires, plage de 70 à 82 % selon la règle de retrait, que les auteurs disent légèrement sous-estimé (T p. 21-22, l. 1193-1200 ; p. 5, l. 295-296) [v]. | La référence commande tout : le même format de contrôle par paires donne 91,2 % avec référence (RS p. 4) [v-pdf], 53 % sans (T p. 8, l. 513) [v]. Le monde planté fournit la référence par construction. |
| **Leurre** | Réservoir : aucun (lecture:106) [v]. Panorama : un leurre construit, technique réelle de même famille, longueur voisine, même ligne, parmi 20 à 42 candidats (lecture:115 ; RS p. 15) [v-pdf]. | Aucun leurre construit ; l'autre membre de la paire, noté au moins deux points plus bas par l'ancre (T p. 5, l. 277-278) [v] ; quatre propositions « aimants » plafonnées à 10 apparitions (T p. 21, l. 1189-1193) [v]. | Le bras « leurre de même famille » de P3 reste le bon témoin ; c'est la comparaison la plus dure, celle où TASTE voit ses modèles échouer le plus (T p. 38, l. 2333-2334) [v]. |
| **Format du choix** | Un parmi quatre dans le réservoir (lecture:104) [v] ; panorama sans choix demandé (lecture:113-115) [v-pdf]. | Un parmi deux pour les modèles (T p. 31) [v] ; trois propositions à la fois pour les humains (T p. 3, l. 184-185) [v]. | Le hasard n'est pas au même niveau : aucun taux ne se transpose d'un format à l'autre. |
| **Tirage de l'ordre** | Réservoir : ordre non rapporté, invite du sélecteur absente (lecture:107) [v] ; aucun tirage dans tout le PDF (RS, recherche plein texte) [v-pdf]. Panorama : position non tirée (lecture:116 ; RS p. 16) [v-pdf]. | Les deux ordres joués et moyennés, avec aussi les deux variantes d'invite (T p. 5, l. 309-311) [v] ; effet d'ordre rapporté à part, jusqu'à 25 points, lié à une justesse plus basse même après moyenne (T p. 6, l. 384-387 ; p. 43, l. 2664-2670) [v] ; selon le modèle, il s'ajoute ou non au simple retirage (T p. 42, l. 2621-2626 ; p. 44, l. 2789-2790) [v] ; ordres tirés aussi pour le correcteur amont (T p. 15, l. 869-870) [v]. | La condition de TASTE la plus utile à nos essais. Avec 6 mondes par bras (prop:129) [v], tirer une seule position par monde rend la position aléatoire, mais ne permet pas de mesurer l'effet de position. |
| **Effort de raisonnement** | Non rapporté dans la lecture [s]. | Évaluation à effort maximal ; le modèle classé premier passe de 48 % à 60 % selon l'effort (T p. 6, l. 356-358 ; p. 26, tableau 3) [v]. | Réglage à geler et à consigner au manifeste : sinon on confond le modèle et son réglage (condition ajoutée par LC:48, absente de LP). |
| **Autopréférence** | Mesurée sur le score : de +0,17 à +0,33 point pour sa famille, retirer le juge de même famille change le gain d'au plus 0,08 (lecture:70) [v] ; non contrôlée pour le sélecteur (lecture:108) [v]. | Le générateur est aussi l'un des modèles jugés (45 %, T p. 26, l. 1472) [v] ; aucun essai d'autopréférence (recherche) [a]. | Dans le bras où le questionneur choisit entre sa question et celle de l'autre proposeur (P3, phase 2), rapporter la part de choix de sa propre question. |
| **Contamination** | Articles postérieurs à toutes les coupures annoncées ; liste et dates absentes du PDF ; marge nulle pour le modèle qui mène ; modèles auxiliaires sans coupure (lecture:86-87 ; RS p. 4) [v-pdf] ; score à zéro question rapporté, mais le test est affaibli (contre:34) [v]. | Aucun contrôle écrit ; les mots n'apparaissent pas [v]. Les propositions sont neuves, le banc n'est remis que sur demande (T p. 2, l. 121-122) [v] ; questions motivantes filtrées pour ne pas trahir l'idée de l'amorce (T p. 3, l. 166-167) [v]. La date fictive du 1er février 2026 est donnée aux humains et aux modèles (T p. 31, l. 1847-1849) [v], qui sortent jusqu'au 24 juillet 2026 (T p. 26, l. 1465) [v]. | Nos mondes sont tirés neufs par graine : la contamination est écartée par construction (LC:32) [a]. Le décalage de date chez TASTE est une hypothèse de lecteur (un modèle récent connaît des travaux postérieurs), pas un défaut établi. |
| **Nouveauté** | Aucune mesure (lecture:15-17, 51) [v]. | Pas de mesure indépendante : un critère que les humains pèsent (T p. 8, l. 521-525) [v] ; avis de modèle par paire (T p. 45, l. 2798-2808, 2843-2844) [v] ; la consigne du générateur la dévalue (T p. 51, l. 3182) [v] et la sélection par ressemblance la réduit, de l'aveu des auteurs (T p. 17, l. 941-943) [v]. | Aucun des deux travaux ne la calcule. Dans P2, la « forme absente de l'archive » est calculée par le code : il ne faut pas l'appeler « nouveauté ». |
| **Contrôle humain** | Trois maillons contrôlés : répondeur (94,0 %, RS p. 5) [v-pdf], extraction (93 %, lecture:67) [v], juges par paires (91,2 %, RS p. 4) [v-pdf] ; la reconnaissance elle-même, aucun (lecture:119) [v]. | L'humain est la référence, et elle est bruitée : 53 % brut (T p. 8, l. 513), 68 % après discussion et confiance forte (T p. 7, l. 453), 83 % avec deux points d'écart mais sur 18 paires (T p. 8, l. 504-505) [v]. Les chercheurs savent qu'ils notent des productions de modèle (T p. 19-20, l. 1071-1087) [v]. | Un panel humain ne règle rien à bas prix : argument de plus pour l'oracle du monde planté (N-058). |
| **Incertitude et indépendance** | Intervalles sur les interventions, tests appariés par article corrigés de Holm (lecture:32, 121) [v] ; plateau non testé (lecture:93) [v]. | Bruit binomial autour du hasard (T p. 2, l. 86-87) [v] ; rééchantillonnage des questions (T p. 8, l. 500-501) [v] ; dépendance des 92 paires reconnue (T p. 9, l. 558-560) [v] ; analyse « sans aimants » (T p. 36, l. 2146-2152) [v]. | Rééchantillonner les mondes (prop:42) [v] ; donner la sensibilité de chaque choix arbitraire ; faire une analyse sans les formes les plus fréquentes. |
| **Refus et données manquantes** | Non rapporté dans la lecture [s] ; le répondeur peut dire Inconnu (lecture:51) [v]. | Refus comblés par une règle fixe, en dernier recours par la réponse d'un autre modèle ; 9 cellules sur 184 à effort maximal en cadre situationnel (T p. 25, l. 1441-1445) [v]. | Contre-exemple : une réponse perdue est comptée comme perdue, jamais remplacée (R5). |
| **Données et code** | Rien de publié ni promis ; températures, graines, coûts absents (lecture:152) [v]. | Données sur demande ; invites en annexe ; aucun lien de code, ni température ni graine (T p. 10, l. 617-626 ; recherche plein texte) [v] ; coût seulement en jetons moyens sur un axe (T p. 6, l. 339-340) [v]. | Graines dérivées, manifeste et coût par partie : c'est le point où nos essais dépassent les deux travaux, à tenir. |

## 3. Désaccords entre les lecteurs et leur règlement

1. **L'empreinte du PDF de TASTE.** LP l'a recalculée (LP:24) ; LC ne l'a pas fait et déclare donc tous les chiffres « non opposables » (LC:12, 89). *Règlement* : l'arbitre l'a recalculée, `f9aed18c…`, conforme, et le texte est identique à l'octet à l'extraction du PDF. Les numéros de page des deux notes concordent avec les pages du PDF. Les chiffres de TASTE sont donc vérifiés comme affirmations des auteurs, page citée, au sens de R7 ; ils restent non reproduits et privés. La réserve de LC est levée sur ce point, pas sur la portée.
2. **Le choix entre candidats a-t-il une référence ?** LP le traite comme « un choix sans référence, la condition où TASTE trouve des modèles proches du hasard » (LP:100). LC montre que, dans notre jeu, le code peut calculer le gain d'information de chaque question candidate quand l'ensemble des lois compatibles peut être énuméré (LC:65), ce que la mesure d'information par question de P1 prévoit déjà (prop:39). *Règlement* : les deux ont raison, à des niveaux différents. Le choix est sans référence chez Re-Search, il en a une calculable chez nous. On retient la mesure de LC, la justesse du choix contre le gain calculé, jouée dans les deux ordres, **comme information seulement**, jamais comme critère de composition (N-058).
3. **L'ordre dans P3.** LP recommande de répartir d'avance la position de la forme vraie et du leurre sur les mondes, sans coût, et de jouer deux ordres seulement si la puissance le permet (LP:97). LC recommande des questionneurs factices à biais de position connu dans la phase sans dépense, puis au besoin deux positions par monde (LC:64). *Règlement* : ces options se complètent, on les prend toutes, dans cet ordre : répartition d'avance (gratuite) ; factices à biais de position (gratuits, essai R5 sur un cas sain et sur un artefact) ; deuxième position par monde seulement si la puissance calculée en phase 0 l'exige. Cette deuxième position coûte 228 appels, soit 100,44 USD au pire, ou 105,73 USD avec la carte à zéro question (calcul de LC refait).
4. **La carte écrite avant toute question.** Seule LC la propose pour P3 (LC:63), afin de séparer la reconnaissance sans aide de la reconnaissance confirmée par le monde. *Règlement* : on la retient. La contre-lecture la demande déjà pour P1 (contre:67), et les bras de P3 sont greffés sur le jeu de P1 (prop:104) : la carte se reporte sans conception nouvelle. Coût vérifié : 24 appels de plus en phase 1, soit 211,46 USD au lieu de 200,88. Le bras leurre sert de base pour la lecture « sans aide ».
5. **Le niveau de la référence humaine de TASTE.** LC écrit « 77 % au mieux après filtrage » et parle d'une référence qui « plafonne à 77 % » (LC:29, 70). *Règlement* : c'est trop fort. 77,4 % est l'estimation sur le banc, que les auteurs disent légèrement sous-estimée, avec une plage de 70 à 82 % ; le filtrage par écart de deux points donne 83 %, mais sur 18 paires (citations n° 3, 14, 30). On retient la formulation de LP (53 % brut, 68 % après filtrage, environ 77 % sur le banc).
6. **L'effort de raisonnement.** Seule LC le relève (LC:48). *Règlement* : on le retient pour P1 et P3 (citation n° 11), et on le consigne au manifeste avec les jetons par partie.
7. **Le décalage de date.** Seul LP le relève (LP:55). *Règlement* : le constat tient (aucun mot sur la contamination ni sur les coupures). Mais le passage cité est dans l'invite des modèles, qui reçoivent eux aussi la date fictive : le défaut possible n'est pas une consigne différente entre humains et modèles, c'est la connaissance par un modèle récent de travaux postérieurs à cette date. C'est une hypothèse non testée, sans conséquence pour nos essais, dont les mondes sont tirés neufs.
8. **Le coût.** LP donne 740,09 USD pour P3 si le choix est un appel distinct (LP:67) ; LC donne 211,46 USD pour P3 (LC:63, résumé). *Règlement* : les deux calculs sont justes, mais ne couvrent pas la même chose. 211,46 USD est la seule phase 1 de P3 avec la carte à zéro question ; le résumé de LC qui dit « P3 de 200,88 à 211,46 USD au pire » est trompeur. Pires cas refaits par l'arbitre, au plus haut prix observé par appel (0,400484 USD) plus 10 % de reprises, prix que la contre-lecture juge mal adapté à un appel de question (contre:66), donc ordres de grandeur et non devis :

   | P3, scénario | appels | pire cas |
   |---|---|---|
   | propositions (phase 1 + phase 2) | 456 + 840 | 570,93 USD |
   | choix entre questions en appel distinct (contre-lecture) | 456 + 1 224 | 740,09 USD |
   | idem avec carte à zéro question dans les deux phases | 480 + 1 248 | 761,24 USD |
   | idem avec deuxième position par monde dans le bras « forme vraie » | 480 + 1 248 + 240 | 866,97 USD |

   P1 passe de 267,84 USD à 281,94 USD avec la carte à zéro question. P2 reste à 68,63 USD.
9. **La portée de P3.** LC le dit « plus probant », comme le seul montage où la reconnaissance se lit sur une vérité calculée (LC:61). LP est plus réservé sur ce que P3 tranche (LP:72, 107). *Règlement* : P3 est probant pour **notre** question (nos proposeurs reconnaissent-ils une forme vraie offerte, dans une grammaire fermée ?). Il n'arbitre pas entre Re-Search et TASTE, dont les objets sont autres (une méthode d'article en langue naturelle, la préférence d'un expert). On retient de LC que le résultat nul devient une issue sérieuse, ce qui rend obligatoires la règle à trois issues et la puissance avant tout devis (contre:65).
10. **La nouveauté chez Re-Search.** LC dit que la date de parution « en tient lieu » (LC:33) ; LP écrit qu'il n'y en a aucune mesure (LP:56). *Règlement* : on retient LP. Les lignes citées par LC portent sur la contamination (citation n° 46).
11. **Plafonner les formes servies et faire une analyse sans aimants : dans P2 ou dans P3 ?** LP applique le plafond aveugle et l'analyse sans aimants au quota de P2 (LP:90-91) ; LC applique le plafond aux formes qui servent de vraie ou de leurre dans P3 (LC:30). *Règlement* : il n'y a pas de conflit, on applique les deux pratiques là où chacun les place.

Points d'accord des deux lecteurs, confirmés : les deux travaux ne mesurent pas la même chose ; les trois points du message de la session (R-3181) sont conformes aux pièces ; 570,93 USD est le pire cas du **seul** P3, et non des trois essais (907,40 USD) ; il ne faut jamais remplacer une réponse manquante par celle d'un autre modèle ; P1 et P3 sont « hors table » (contre:62).

## 4. Recommandations pour les trois essais

### P1 — le jeu de questions fermées où le monde planté répond lui-même : **garder, modifier**

Raison : TASTE confirme qu'il faut retirer le juge modèle et le répondeur modèle, sans rien remettre en cause de l'essai. Il ajoute des conditions qui ne coûtent presque rien. Modifications, à écrire au préenregistrement de la phase 0 (déjà permise sous GO-2026-11-18-05, aux deux conditions de la contre-lecture) :
1. Geler et consigner au manifeste l'effort de raisonnement et les réglages d'échantillonnage de chaque proposeur, avec les jetons par partie.
2. Tirer par graine dérivée (R9) l'ordre de présentation des traits et des prédicats, partie par partie. Décider avant la phase 1 si l'une des deux parties du test A/A est jouée en ordre permuté (cela ne coûte rien, mais le test ne mesure plus le seul retirage) ou si l'on ajoute une paire (à chiffrer). Le critère sur la largeur de l'intervalle A/A, déjà exigé, sépare la part du retirage de celle de l'ordre.
3. Écrire une règle pour les refus, les échecs d'appel et les sorties mal formées : comptés à part, jamais remplacés par la réponse d'un autre modèle.
4. Écrire la carte à zéro question (contre:67).
5. Borne écrite de la revendication : l'instrument mesure la recherche par questions dans une grammaire fermée ; ses chiffres ne répondent pas à TASTE et ne disent rien du jugement d'idées en langue libre.

### P2 — la diversité des formes dans la mémoire : **garder, modifier**

Raison : TASTE ne mesure pas la diversité. Il reconnaît seulement l'arbitrage entre qualité et nouveauté, ce qui appuie le choix des deux types de mondes de la phase 1 sans en prédire le signe. Il fournit deux pratiques sans coût. Modifications :
1. Fixer le quota q par une règle qui ne lit pas l'oracle, et geler au préenregistrement une plage de q dont on rapportera la sensibilité, à la manière du plafond de TASTE (T p. 21-22, l. 1183-1200).
2. Rapporter la part de formes répétées sur toutes les cartes et sur les cartes hors type à forme unique (les softmax, contre:44), et écrire d'avance que la décision se prend sur la seconde.
3. Fixer la loi de tirage de la référence (contre:68).
4. Ne pas appeler « nouveauté » une forme absente de l'archive.

La piste de LC (servir à chaque proposeur un sous-ensemble différent de l'archive, LC:56) est laissée à Lazar, hors essai, après la phase sans dépense. Le devis ne change pas.

### P3 — le panorama de formes candidates offert au questionneur : **garder, modifier avant tout devis** (dépense : décision de Lazar)

Raison : c'est le seul montage où la reconnaissance se lit sur une vérité calculée. TASTE fait du résultat nul une issue sérieuse et donne l'ordre de grandeur d'un effet de position (jusqu'à 25 points sur deux positions seulement) qui rend insuffisant le tirage unique sur 6 mondes. Modifications :
1. Répartir d'avance, sur les mondes, la position de la forme vraie (dans le bras « forme vraie ») et celle du leurre (dans le bras « leurre ») : début, milieu, fin. Le critère « le reste une fois la position tirée prise en compte » (prop:118) est à remplacer par cette répartition, puisqu'il n'est pas estimable sur 6 mondes.
2. En phase 0, ajouter des questionneurs factices à biais de position connu, que l'instrument doit détecter (essai sur un cas sain et sur un artefact) ; jouer une deuxième position par monde seulement si la puissance le demande.
3. Ajouter une carte écrite après le panorama et avant toute question, qui donne la reconnaissance sans aide à côté de la reconnaissance confirmée par le monde.
4. Imposer au leurre la même longueur, le même format et le même nombre de nœuds que la forme vraie. Plafonner le nombre de fois qu'une même forme sert de vraie ou de leurre, et faire l'analyse sans les formes les plus fréquentes.
5. Dans le bras de phase 2 où le questionneur choisit entre sa question et celle de l'autre proposeur : jouer les deux ordres ; rapporter comme information la part de choix de sa propre question et la justesse du choix contre le gain d'information calculé. Chiffrer un bras « choix au hasard ».
6. Appliquer la règle à trois issues et calculer la puissance en phase 0, avant tout devis (contre:65) ; définir par le code toute mesure secondaire de reconnaissance, jamais par un annotateur modèle.
7. Refaire le devis sur ces bases : 570,93 USD au pire selon les propositions, 740,09 USD selon la contre-lecture, jusqu'à 866,97 USD avec toutes les options (section 3, désaccord 8), au prix d'un appel de question à relever.

**Retirer** : rien. Aucun des trois essais n'est rendu inutile par TASTE. Seul le critère de P3 sur la position tirée « prise en compte » est à remplacer (point 1).

### L'instrument de mesure de la recherche des proposeurs indépendant du juge (N-058)

N-058 sort renforcée par une raison d'une autre nature que celle de la décision (l'invariant de N-053, point 5, `docs/decisions/decision-N-058-v1.md`, l. 19-28) : sans vérité de terrain, ni un juge modèle ni un panel humain ordinaire ne donne une mesure fiable, selon les auteurs de TASTE. L'instrument hérite du contrebalancement de l'ordre avec un effet d'ordre rapporté à part, de la sensibilité de chaque choix arbitraire, de l'analyse sans aimants, du refus de toute réponse substituée et de l'effort de raisonnement consigné. Sa validité tient à la référence du monde planté ; elle ne s'étend pas telle quelle aux propositions réelles de l'atelier d'idées ni au second terrain du papier C (N-065).

## 5. Ce qui ne tient pas

1. LC:34 et LC:70 ancrent le 53 % de TASTE aux lignes 452-453 ; il est à la ligne 513 (et l. 24-25, 111).
2. LC:29 et LC:70 : « 77 % au mieux après filtrage », « référence plafonnée à 77 % » sont trop forts : 83 % sur 18 paires (l. 504-505), plage de 70 à 82 % (l. 1199-1200), estimation dite légèrement sous-estimée (l. 295-296).
3. LC:12 et LC:89 : « empreinte du PDF non recalculée, aucun chiffre vérifié » est périmé : recalculée par LP et par l'arbitre, conforme.
4. LC:33 : « la date de parution tient lieu de nouveauté (L l. 86-87) » : ces lignes portent sur la contamination.
5. LC:93 : la copie numérotée du texte privé `taste-num.txt` « reste » dans le répertoire temporaire : périmé, l'arbitre l'a vérifiée absente.
6. Résumé de LC, point 3 : « P3 de 200,88 à 211,46 USD au pire » ne couvre que la phase 1 de P3 ; P3 entier coûte 570,93 USD au pire selon les propositions, 740,09 USD selon la contre-lecture.
7. LP:55 présente le 1er février 2026 comme une consigne faite aux humains seulement ; le passage cité est dans l'invite des modèles, qui la reçoivent aussi. Le décalage est une hypothèse sur la connaissance des modèles, pas un écart de consigne.
8. LP:59 et LC:39 : « 9 cellules sur 184 » est donné sans sa portée (effort maximal, cadre situationnel, l. 1444).
9. LP:57 : l'essai à l'aveugle (dernière et 37e sur 74) est cité sans dire qu'il porte sur un autre échafaudage, en décembre 2025 (l. 3053-3054) : il ne dit rien des propositions du banc.
10. LP:6 : l'heure de fin de rédaction annoncée (05:10Z) est fausse ; la rédaction s'est terminée vers 04:51Z, de l'aveu du lecteur (fichier daté 04:51).
11. La lecture du message de la session comme « trois propositions, 571 USD au pire » serait fausse : 571 USD est le pire cas du seul P3 (R-3181 le dit ainsi) ; les trois essais réunis font 907,40 USD au pire.

## 6. Réserves et incidents

- Re-Search : 11 passages rouverts sur le PDF empreinté (`ae848c68…`), tous conformes ; le reste est vérifié sur les pièces de la session (empreintes conformes), pas sur le PDF. Le commit `4f2a259` n'est pas vérifié par `git` ; il l'est seulement par les empreintes compagnons des pièces.
- TASTE : figures non lues (légendes et texte embarqué seulement), comme chez les deux lecteurs ; aucune valeur relevée sur un tracé.
- Le brouillon de la session contient un second PDF de TASTE, de provenance inconnue (`dl/anthropic-taste-2026-08.pdf`, `7f092437…`, signalé par LP:122) ; l'arbitre ne l'a pas ouvert. Si sa provenance était publique, le statut de pièce non publiée (R-3154) serait à revoir. À trancher par la mère ou par Lazar ; aucune conclusion ici.
- Aucun envoi aux auteurs de l'un ou l'autre travail n'est proposé (contact externe : Lazar).
