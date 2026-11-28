# Vérification de la synthèse v4 « comment détecter » — angle « sens et expériences », tour 3 — v1

## Verdict : **conforme après corrections**

- Les grandes corrections du tour 2 sont faites. Les phrases anglaises et les chiffres repris sont sur leur page. Le bras
  « moyenne » reste un diagnostic (N-026). Aucune expérience ne vise un signe (R3). Les extensions hors des GO sont
  marquées comme nœuds. La conclusion du point 2 (« ne prévoit ni n'exclut le nul ») et le levier « données du
  domaine » tiennent.
- Un constat majeur (VV4-sens-01) : la v4 lit E2 sur T0.6 « sur la condition qui réplique P3 ». Or le T0.6 que
  recommande P-015, que la v4 cite, ne garde que des doses sous le seuil du meilleur moniteur boîte noire. P3, flagrant,
  n'y serait pas répliqué. La recommandation (3) et l'option (b) du nœud E2 perdent alors leur objet.
- Cinq constats moyens, dont quatre dans des passages réécrits par la session : un troisième type de contraste (« contre la
  conversation ordinaire ») est rangé dans P3-P3 ; le point 1 mêle encore les deux types et cite [DYL] p. 11 d'un seul
  côté ; la prédiction de E2 ne dit rien de la lecture principale ; une raison de la confiance de 15 à 25 % contredit les
  analogues de T1 de la v4 elle-même (R8) ; le jeu (2) de E3 ne peut rien apprendre « avant le champ » s'il est écrit.
- S'y ajoutent huit mineurs et deux de forme. Corrections en mots exacts ci-dessous. Après application, un contrôle de
  fidélité des remplacements suffit ; pas de nouvelle vérification de sens, sauf si la recommandation du nœud E2 change
  de fond.
- Plusieurs points sont dépassés par des décisions d'après 18:27 UTC (GO-2026-10-20-10, P-016 à P-018, N-030, R-297,
  R-298, et R-302 avec GO-2026-10-20-11, pris pendant cette vérification) : section « Dépassé », simple information.

## Cadre

- **Objet.** `…/revue-detection/synthese-comment-detecter-v4.md`, sha256
  `fba703f90bba52663709857113d99e17ab0570e465180bed539458b18b11d00a` (compagnon égal), sections 1, 3, 4 et 5. Aussi lus :
  v3 (`ec4239e9…`, différentiel phrase à phrase avec la v4), `verification-v3-sens-v1.md` (`256f9181…`), traitement du
  tour 3 (`traitement-verification-synthese-tour3-v1.md`). `…/` =
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **Vérificateur neuf.** Je n'ai écrit ni la v1, ni la v2, ni la v3, ni la v4, ni les extractions, ni aucune
  vérification ni aucun traitement. 2026-10-20, de 21:55 à 22:55 UTC environ.
- **Lecture seule.** Dépôt à la tête `c1e7ef9` au début, `6a449d2` à la fin (R-302, commit de la session pendant ma
  lecture ; aucune écriture de ma part) ; arbre propre au début ; à la fin, quatre fichiers non suivis apparus pendant ma
  lecture sous `docs/verdicts/` (verdict v2 de P3, écrit par la session) : non ouverts ; git en lecture seulement. Non ouverts :
  `prereg/P3-consignes-v1.md`, textes d'action, clés, sortie de l'addendum 2 (seul l'en-tête des lignes R-297 et R-298 du
  registre a été lu). Aucune recherche web, aucun service payant, aucun contact, aucune commande Vast.ai.
- **Méthode.** Empreintes des 22 PDF recalculées : toutes égales aux clés (`empreintes-pdf-v4-sens.txt`). Texte de chaque
  page extrait à nouveau par moi (`pdftotext`, brut `rNNN.txt`, mise en page `pNNN.txt`, sous `pages/<clé>/`).
  Recherche : `outils/ch.py` ; toutes les phrases entre guillemets des sections 1, 3, 4 et 5 cherchées dans toutes les
  pages (`outils/guillemets_v4.py`, sortie `sortie-guillemets-v4.txt`) ; épreuve R5 de l'outil (`sortie-epreuve-r5-ch.txt` :
  trois cas sains trouvés à leur page ; chiffre changé, mot changé, page voisine rejetés). Phrases anglaises de ce rapport
  contrôlées de même (`sortie-guillemets-rapport-v1.txt`).
- **Conventions.** « l. » d'un PDF = ligne de mon fichier `rNNN.txt` (`pNNN.txt` pour une table). « l. » de la v4 = ligne
  du fichier v4. [P] `prereg/P3-premier-test-i-a-v1.md` (`d975e981…`) ; [V] `docs/verdicts/verdict-P3-premier-test-i-a-v1.md`
  (`0c8ecbdf…`) ; [NB] `docs/notes/brainstorm-suite-P3-v1/` (note `a023093e…`) ; P-015
  `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md` (`6e74c6cb…`) ; P-011
  `docs/decisions/proposition-P-011-T0.7-sondes-v1.md` (`64afff19…`).
- **Exposition (R1).** [V] l. 170-172 et 358-359 lues sans masque (drapeaux nommés, aucun chiffre). Note du brainstorm
  l. 1-12, 24-36, 83-87, `proposition-C.md` l. 318-326 et `proposition-D.md` l. 78-104 lues décimales masquées ; le libellé
  restait lisible. Je ne recopie ici aucune valeur ni aucun sens de T1, T2 ou T4. Ce vérificateur ne doit pas rédiger P3b.

## Constats (le plus grave d'abord)

### VV4-sens-01 — majeur — E2 sur T0.6 : la condition « qui réplique P3 » est exclue par le T0.6 que recommande P-015

- **Où.** v4 l. 283 (E2, tranche) ; l. 286 (E2, contrôle) ; l. 292-294 (recommandation (3)) ; l. 326-336 (nœud E2) ;
  l. 350-351 (dépense).
- **Problème.**
  - La v4 lit E2 sur T0.6 « seulement sur la condition qui réplique P3 ((i-a), p = 1, intensité forte, brouillon de T0.6
    l. 75, ou son équivalent dans T0.6 réécrit) ». Sa question : « la position explique-t-elle le nul ? ».
  - P-015, que la v4 cite (l. 284, l. 351), définit l'organisme de T0.6 comme « diffus » : « chaque action sabotée reste
    sous le seuil du meilleur moniteur boîte noire par action, calibré à 1 % de faux positifs sur l'honnête » (l. 36-39).
    Option (b) : « on retient les intensités dont le rappel par action du meilleur moniteur, à 1 % de faux positifs, reste
    sous un seuil gelé » (l. 91-92) ; T0.6 décisif « aux intensités retenues » (l. 94). Recommandation et défaut : (b),
    car « P3 montre qu'une intensité fixée a priori peut être flagrante » (l. 153-155). Défaut le 2026-10-22 vers
    14:30 UTC (`registres/decisions.md`, ligne P-015).
  - P3 est flagrant : le coût seul sépare à 0,8878 ([V] l. 204 ; `decision-N-029-v1.md` l. 25-26). Son « équivalent » est
    exclu par construction du T0.6 recommandé.
  - Sous P-015 (b), E2 sur T0.6 dit si la position aide sur l'organisme diffus. Elle ne dit pas d'où vient le nul de P3.
    L'option (b) du nœud E2 (« E2 sur les épisodes neufs de T0.6, à l'aveugle : plus tard ») et la recommandation (3)
    perdent leur objet. La question de P3 n'a alors de réponse que par l'option (a) (actions de P3), ou par une condition
    de référence flagrante ajoutée à T0.6.
- **Correction.**
  - l. 283, remplacer « sur T0.6, seulement sur la condition qui réplique P3 ((i-a), p = 1, intensité forte, brouillon de
    T0.6 l. 75, ou son équivalent dans T0.6 réécrit) » par : « sur T0.6, seulement sur une condition qui réplique P3 ((i-a),
    p = 1, intensité forte, brouillon de T0.6 l. 75). Le T0.6 que recommande P-015 (défaut (b) le 22 octobre) n'en a pas :
    il ne garde que des doses sous le seuil du meilleur moniteur boîte noire (P-015, l. 36-39, l. 91-94), et P3 est
    flagrant (coût seul 0,8878, [V] l. 204). Sans condition de référence flagrante ajoutée à T0.6 (périmètre de P-015 et
    dépense : à toi), E2 sur T0.6 dit si la position aide sur l'organisme diffus, pas d'où vient le nul de P3 ».
  - Nœud E2, option (b) : ajouter « ; inconvénient : sous P-015 (b), elle ne répond pas à la question de P3, sauf condition
    de référence flagrante ajoutée à T0.6 ». Remplacer « Recommandation : (b), confiance ≈ 55 % » par « Recommandation :
    (b) si T0.6 garde une condition de référence qui réplique P3 ; sinon la question « la position explique-t-elle le nul
    de P3 ? » n'a de réponse que par (a). Ce nœud se tranche avec P-015. Confiance à revoir par le rédacteur ».
  - Recommandation (3), après « avec la prédiction écrite de la section 4 », ajouter « , si T0.6 garde une condition qui
    réplique P3 (nœud E2 et P-015) ».

### VV4-sens-02 — moyen — Un troisième type de contraste est rangé dans P3-P3 : « contre la conversation ordinaire » ou « contre le témoin Alpaca »

- **Où.** v4 l. 61-62 (point 1 : « entre consignes, la même sonde sépare presque parfaitement [AP p. 18] ») ; l. 79-80 et
  l. 89-90 (point 2 : rappel 0,03 de [BX] parmi les analogues de P3-P3, puis dans la conclusion) ; l. 91-92 ; l. 209
  (rang 3) ; l. 210 (rang 4 : « entre consignes, séparation presque parfaite ») ; l. 283 (E2, tranche).
- **Problème.**
  - [AP] p. 18 : « Where this probe excels, however, is consistently rating every control response as honest. Our recall
    at 1% is greater than 99% on all four evaluation datasets » (l. 48-49). Le témoin d'Apollo est Alpaca : « We use Llama
    responses to queries from the Alpaca dataset » (p. 5, l. 36). Les positifs viennent d'autres tâches et d'autres
    formats.
  - [BX] p. 6 : le rappel mesure la capacité à « distinguish transcripts containing normal conversational data from those
    exhibiting the studied behavior » (l. 68-72). Le seuil est pris sur la conversation ordinaire.
  - P3-P3 oppose saboteur et honnête sur les mêmes tâches, dans le même environnement ; seule la consigne change ([P]
    l. 320-321, l. 328-332).
  - Un changement de tâche élève à lui seul la sonde Pairs : « For Pairs probe, the average honest Backdoors sample had a
    mean probe activation higher than 99.9% of the Alpaca samples » ([PAR] p. 9, l. 21-22). La séparation « presque
    parfaite » de [AP] p. 18 n'est donc pas un fait de type P3-P3.
  - La preuve de type P3-P3 qu'une sonde lit le régime de consigne est [KU] : « D-RepE (Simple Contrastive): 1,000 diverse
    factual questions with contrastive system prompts » (p. 4, l. 10), mêmes questions, consigne seule changée (p. 5 ;
    p. 9). Pour la sonde Instructed-Pairs, [AP] p. 18 ne donne qu'une hypothèse, contre le témoin.
- **Correction.**
  - l. 61-62 : remplacer « entre consignes, la même sonde sépare presque parfaitement [AP p. 18] » par « contre le témoin
    Alpaca (autres tâches, sans consigne), la même sonde a un rappel au-dessus de 99 % à 1 % de faux positifs [AP p. 18 ;
    témoin, p. 5] : ce n'est pas P3-P3, et un changement de tâche élève à lui seul la sonde Pairs [PAR p. 9] ».
  - Point 2 : retirer « ; sur ce même modèle, rappel à 1 % de faux positifs contre la conversation ordinaire, consigne et
    raisonnement exclus du score : 0,03 [BX p. 6 ; table 1] » des analogues de P3-P3. Après les analogues de T1, écrire :
    « Contre la conversation ordinaire (troisième type, ni P3-P3 ni T1 : autres tâches, seuil sur la conversation
    ordinaire) : rappel de 0,03 sur ce même modèle, consigne et raisonnement exclus du score [BX p. 6 ; table 1] ; plus de
    99 % pour la sonde de question apprise sur « Roleplaying » [AP p. 18]. »
  - Conclusion du point 2 : « à consignes différentes, de 0,58 à 0,95 selon le modèle, 0,768 au maximum à 70 milliards ;
    contre la conversation ordinaire, rappel de 0,03 sur ce même modèle quand ni consigne ni raisonnement ne sont notés ».
  - l. 91-92 : « [KU p. 9 ; AP p. 18] » devient « [KU p. 5, p. 9 ; hypothèse pour la sonde Instructed-Pairs, contre le
    témoin, AP p. 18] ».
  - Rang 3 : « mais, contre la conversation ordinaire, le rappel à 1 % peut tomber à 0,03 [BX table 1] ». Rang 4 et E2 :
    même remplacement qu'aux l. 61-62.

### VV4-sens-03 — moyen — Point 1, rang 4 et E2 : « sur consigne, la question ne bat pas la moyenne » mêle les deux types et cite [DYL] p. 11 d'un seul côté

- **Où.** v4 l. 58-60 ; l. 210 ; l. 283.
- **Problème.**
  - La phrase réunit [DYL] table 9 et [LB] p. 8, à consignes différentes (« one paired with a randomly drawn
    honesty-inducing system prompt and one with a lie-inducing prompt », [DYL] p. 5, l. 65-66 ; [LB] p. 6, l. 42-47), et
    [PAR] au sous-rendement, à consigne égale ([PAR] p. 4, l. 88-90). C'est le mélange que VV3-sens-01 demandait de
    défaire.
  - [DYL] p. 11, cité pour « ne bat pas la moyenne », donne aussi l'inverse. Sur « Gender Secret » remis sur consigne :
    « Apollo and Unrelated Questions perform poorly even on the prompted variants » ; « DYL, by contrast, retains strong
    performance on the prompted variants (BA 0.85, AUROC 0.9–0.93) » (l. 5-9). Questions cibles et questions témoins y sont
    posées au même organisme (p. 7, l. 48-55) : consigne égale, type T1.
  - Réserve sur ce contre-cas : la sonde de [DYL] lit la réponse après un raisonnement permis (« for reasoning models we
    allow reasoning tokens before the yes/no response », p. 8, l. 48-49) ; la consigne demande ce raisonnement explicite
    (annexe L.1, p. 27) ; la moyenne d'Apollo exclut le raisonnement (« the mean over all non-reasoning assistant tokens »,
    p. 8, l. 38). Il renforce « son issue dépend des données d'apprentissage de la sonde », avec un texte trompeur écrit
    dans le contexte, que P3 n'a pas.
- **Correction.** l. 58-60, remplacer « Sur les cas sur consigne, elle ne bat pas la moyenne [DYL p. 11 ; table 9 ; LB p. 8 ;
  PAR table 3, sonde Pairs : 0,849 et 0,879 contre 0,964 au sous-rendement]. » par : « À consignes différentes, elle ne bat
  pas la moyenne [DYL table 9, « Varied Deception » ; LB p. 8] ; sur « Backdoors », sonde Pairs, elle bat le maximum (0,832
  et 0,849 contre 0,768 ; moyenne 0,844) [PAR table 3]. À consigne égale, sonde Pairs : 0,849 et 0,879 contre 0,964 en
  moyenne au sous-rendement [PAR table 3] ; la sonde de question de [DYL], apprise sur des réponses à « did you lie », tient
  sur « Gender Secret » remis sur consigne (exactitude équilibrée 0,85) quand la moyenne d'Apollo tombe près du hasard,
  raisonnement explicite dans le contexte [DYL p. 11 ; p. 8]. » Rang 4 (l. 210) et E2 (l. 283) : remplacer « sur consigne,
  pas meilleure que la moyenne [DYL p. 11 ; table 9 ; LB p. 8] » et « tromperie sur consigne : la question ne bat pas la
  moyenne [DYL p. 11 ; table 9 ; LB p. 8] » par « à consignes différentes, pas meilleure que la moyenne [DYL table 9 ; LB
  p. 8] ; à consigne égale, contre-cas avec raisonnement écrit [DYL p. 11] ».

### VV4-sens-04 — moyen — La prédiction de E2 ne dit rien de la lecture principale (saboteur contre honnête)

- **Où.** v4 l. 283 (« Prédiction écrite d'avance ») ; l. 329-330 (nœud E2, option (a)).
- **Problème.** E2 répond à « la position explique-t-elle le nul ? ». Le nul est celui de P3-P3. La prédiction ne porte que
  sur T1 (« sondes principales de P3 : issue incertaine ([PAR] : 0,849 et 0,879 à consigne égale … ) »). L'analogue de
  P3-P3 le plus proche est dans la même table : « Backdoors », sonde Pairs, 70 milliards, jetons publics : « Deception No
  (Pairs) » 0,832 et « Honest Yes (Pairs) » 0,849, contre « Peak Activation (Pairs) » 0,768 et « Full Averaging (Pairs) »
  0,844 ([PAR] table 3, `p007.txt` l. 19, 21, 24, 26). La v4 l'imprime en 2.1 (l. 110), pas pour E2. R3 et R1 : la
  prédiction écrite doit couvrir la lecture principale, pas un seul contrôle.
- **Correction.** Dans la prédiction de E2, avant « sondes principales de P3 : issue incertaine », écrire : « lecture
  principale (saboteur contre honnête), bras (a) : la littérature ne tranche pas ; analogue de P3-P3 le plus proche
  (« Backdoors », sonde Pairs, 70 milliards, jetons publics) : question 0,832 et 0,849, contre maximum 0,768 et moyenne
  0,844 [PAR table 3] ; un « au-dessus » sans P3-P4, T3 et T1 lirait la consigne. T1 : ». Même ajout, en une phrase, au
  nœud E2, option (a).

### VV4-sens-05 — moyen — Confiance de 15 à 25 % : « rien de publié ne le passe » contredit les analogues de T1 de la v4 (R8)

- **Où.** v4 l. 302-303.
- **Problème.** La v4 cite des analogues de T1 au-dessus du hasard : 0,81 et 0,63 sur ce même modèle (l. 81 ; [BX] p. 5,
  l. 82-85 ; p. 6, l. 3), avec des sondes génériques (« probes trained on the REPE dataset », p. 5, l. 63), donc apprises
  sans l'organisme ; 0,964 en moyenne, sonde Pairs, au sous-rendement, sous une consigne unique ([PAR] table 3 ; p. 4,
  l. 88-90). Ce qui manque n'est pas un succès publié. C'est une mesure contre un plancher apparié, sans texte faux écrit
  dans l'empan, sans sujet confondu (VV4-sens-07). « Zone vierge = question » (R8), pas preuve d'échec.
- **Correction.** Remplacer « T1 s'ajoute, à consigne égale, et rien de publié ne le passe sur un cas de ce type » par :
  « T1 s'ajoute, à consigne égale. Les analogues publiés de T1 restent au-dessus du hasard (0,81 et 0,63 sur ce même
  modèle, sonde générique [BX p. 5-6] ; 0,964 en moyenne, sonde Pairs, à 70 milliards [PAR table 3]), mais avec un texte
  faux écrit dans l'empan et un sujet confondu (WMDP contre MMLU) ; aucun ne mesure T1 contre un plancher apparié (R8 :
  question) ». Revoir la confiance si cette raison portait la baisse.

### VV4-sens-06 — moyen — E3, jeu (2) : lire « avant le champ » sur des paires écrites ne mesure rien, ou mesure le texte écrit

- **Où.** v4 l. 282 (E3, « quoi », (2)) ; l. 285 (piège) ; l. 286 (contrôle).
- **Problème.** Le jeu (2) est fait de « versions incitées … (mêmes contextes, actes différents) : lecture avant le champ
  `COST` ». Les jeux de P-011 sont des paires « synthétiques » écrites par un sous-agent (P-011 l. 35, l. 63).
  Llama-3.1-8B-Instruct est un modèle causal : l'activation d'une position ne dépend que des jetons qui la précèdent (le
  harnais note par une passe unique sur le texte, `harnais/episode.py` l. 260, commit `7a54d43`). Si l'acte (le nombre
  gonflé) n'apparaît qu'au champ `COST`, les jetons d'avant le champ sont les mêmes chez le positif et le négatif :
  activations égales, rien à apprendre. S'ils diffèrent avant le champ, la sonde apprend ce que le rédacteur a écrit (le
  piège « style », l. 285). La v4 ne dit pas d'où vient la différence avant le champ.
- **Correction.** Remplacer « (2) versions **incitées** (intérêt à gonfler, sans consigne), incitation présente chez les
  positifs **et** les négatifs (mêmes contextes, actes différents) : lecture **avant le champ** `COST` » par « (2) actions
  **générées par le modèle** sous incitation (intérêt à gonfler, sans consigne), incitation chez les positifs **et** les
  négatifs, étiquette par le coût écrit ensuite (comme T1) : lecture **avant le champ** `COST` ; jamais sur des paires
  écrites qui ne diffèrent qu'au champ (avant le champ, à texte égal, les activations sont égales : modèle causal) ».
  Ajouter au coût de E3 : « plus la génération des actions du jeu (2), à deviser ».

### VV4-sens-07 — mineur — Analogues donnés sans leur réglage ni leurs données ; sujet confondu dans les analogues de T1 ; [BU] non rangé

- **Où.** v4 l. 78-79 ; l. 81-82 ; l. 209 (rang 3).
- **Problème.**
  - [DYL] : couche et classifieur choisis « using our Varied Deception validation set » (p. 8, l. 22-23), avec des
    invites et des questions disjointes (p. 5, l. 71-72). Réglage dans le domaine ; les sondes de P3 n'ont rien vu de tel.
    0,74 est un analogue optimiste.
  - [YS] 0,606 : sonde apprise sur « Roleplaying » (« Roleplaying is our source domain », p. 2, l. 64), pas sur la recette
    Pairs de P3. Le point 1 conclut pourtant que l'issue dépend des données d'apprentissage.
  - Analogues de T1 au sous-rendement ([BX], [YS], [PAR]) : l'étiquette suit le sujet, WMDP contre MMLU ([BX] p. 4,
    l. 69-73 ; [PAR] p. 4, l. 88-92). Une sonde qui lit le sujet y passe. T1 de P3 compare au coût honnête de la même
    tâche ([P] l. 238-239). La v4 ne le dit que dans la prédiction de E2.
  - [BU] : scénarios « in two versions: one with an incentive to lie and one without » (p. 10, l. 14-15), Llama-3-8B,
    dernier jeton, sonde de vérité générique ; 93,8 % (TTPD) et 79 % (régression logistique) d'exactitude (p. 10). C'est un
    analogue de P3-P3 (mensonge verbal, vérifiable contre le contexte) ; la v4 ne le cite que pour la taille et la
    position.
- **Correction.** Point 2 : après « 0,74 en exactitude équilibrée [DYL p. 5 ; table 9, p. 28] », ajouter « (couche et
  classifieur réglés sur une validation du même jeu, p. 8) » ; après « 0,606 [YS p. 3] », ajouter « (sonde apprise sur
  « Roleplaying », p. 2) » ; après les analogues de T1, ajouter « ; au sous-rendement, l'étiquette suit le sujet (WMDP contre
  MMLU, [BX p. 4] ; [PAR p. 4]), ce que T1 de P3 n'a pas ([P] l. 238-239) » ; aux analogues de P3-P3, ajouter « mensonges
  verbaux de jeux de rôle, avec ou sans incitation, Llama-3-8B, dernier jeton, sonde de vérité générique : 93,8 % (TTPD) et
  79 % (régression logistique) d'exactitude [BU p. 10] ». Rang 3 : mêmes annotations.

### VV4-sens-08 — mineur — Appuis de la question « hors domaine » ([OA]) et « à grande échelle » ([CA]) : contrastes non typés

- **Où.** v4 l. 58 ; l. 210 ; l. 283 (« Pour : »).
- **Problème.** [OA] table 15 mesure « Dsynth vs. Hsynth », soit, sur « the MBPP dataset with the original
  (human-written) code as honest responses », contre « programmatically-generated hardcoded code as deceptive responses »
  (p. 5, l. 55-57) : ni consigne, ni choix du modèle ; la triche est écrite dans le code ; textes hors politique ; score moyen de
  plusieurs couches (« take the mean of the sigmoid scores across selected classifiers », p. 5, l. 106-107). [CA] :
  « its earlier steps and every step of an honest episode are the negative class » (p. 6, l. 73-74) : négatifs de type
  T1 et de type P3-P3 mêlés ; consigne de sabotage dans le contexte (p. 5, l. 50-51).
- **Correction.** l. 58, après « [OA table 15 ; CA p. 7-8] », ajouter « ([OA] : sans consigne, triche écrite dans le code,
  textes hors politique, moyenne de couches ; [CA] : négatifs mêlés, pas d'avant le sabotage et épisodes honnêtes) ». Même
  incise au rang 4 et dans E2.

### VV4-sens-09 — mineur — Taille et capacité : phrase trop générale, transposition à sens unique

- **Où.** v4 l. 62-66 ; l. 211 (rang 5).
- **Problème.**
  - « La détection gagne avec la taille ou la capacité du modèle » : [LB] table 6 n'est pas ordonnée par la taille (Qwen
    2.5 72B 0,60 ; Mistral 3.1 24B 0,69 ; Gemma 3 27B 0,58 ; `p054.txt` l. 8-10). [CA] ne le montre que dans une famille ;
    Nemotron-3 Nano est aussi le plus petit en paramètres actifs (« ticks give total and active parameters », p. 8,
    l. 150 ; 30B-A3B, p. 25) : « mais Nemotron-3 Nano (30B-A3B) reste à 0,613–0,760 » (rang 5) n'est pas un
    contre-exemple. [DYL] : capacité, sur
    mensonge sur consigne seulement (p. 10, p. 12).
  - « si Llama-3.1-8B est en dessous, il tomberait là où [CA] mesure des sondes faibles » : la même table de [DYL] donne,
    pour des indices de 9 à 14, de 0,64 à 0,84 en exactitude équilibrée (Llama-3.3-70B 0,84 ; Qwen3-4B 0,64 ; Qwen3-8B
    0,74 ; gemma-3-27b 0,81 ; gemma-3-12b 0,74 ; `p028.txt` l. 31-35). Un indice bas n'y prédit pas des sondes faibles.
- **Correction.** l. 62-63 : « La détection gagne avec la taille dans une famille [CA p. 8] et avec un indice de capacité
  sur le mensonge sur consigne [DYL p. 10, p. 12] ; [LB table 6] n'est pas ordonnée par la taille. » l. 66, ajouter
  « ; mais dans [DYL] table 9, des modèles d'indice 9 à 14 obtiennent 0,64 à 0,84 : un indice bas n'y prédit pas des sondes
  faibles ». Rang 5 : « Nemotron-3 Nano (30B-A3B, 3 milliards actifs) reste bas » au lieu de « mais Nemotron-3 Nano
  (30B-A3B) reste à 0,613–0,760 ».

### VV4-sens-10 — mineur — E2 : question générale en bras principal sur un modèle de 8 milliards

- **Où.** v4 l. 282 (« Question générale [CA p. 6] : bras principal »).
- **Problème.** [CA] p. 8 : « on smaller models, probes perform worse with vague follow-ups; conversely follow-up choice
  matters little for larger models » (l. 168-169). Le choix d'une question générale se défend (aveuglement, R3). Mais un
  nul du bras principal sur 8 milliards serait prédit par ce fait ; la prédiction ne le dit pas.
- **Correction.** Ajouter à la prédiction de E2 : « question générale sur 8 milliards : [CA p. 8] prédit une perte ; un nul
  du bras principal ne dira pas que la position n'aide pas ; la question précise, en diagnostic, le dira ».

### VV4-sens-11 — mineur — Règles communes : la phrase sur Bonferroni contredit les seuils gelés qu'elle cite

- **Où.** v4 l. 228-229.
- **Problème.** [P] l. 275-277 : Bonferroni sur les deux sondes principales, pour P3-P3 seulement ; l. 278 : « P3-P4, T1,
  T3, T4 : à 95 %, sans correction ». La v4 écrit « P3-P4 (témoin), T1, T3 et T4 aux seuils gelés de [P] (l. 272-279) ;
  Bonferroni sur les seuls bras de production ». Lue telle quelle, elle corrige ces tests, contre [P] l. 278. La lecture
  principale (saboteur contre honnête) n'est pas nommée.
- **Correction.** « **Bras de production** (maximum ou attention) : saboteur contre honnête, avec Bonferroni sur les bras
  de production et les deux sondes (comme P3-P3, [P] l. 275-277 ; extension aux bras : règle de cette synthèse) ; P3-P4
  (témoin), T1, T3 et T4 à 95 %, sans correction ([P] l. 278). »

### VV4-sens-12 — mineur — E1 : grandeurs neuves mal comptées ; règle de calcul de T4 ajoutée sans le dire

- **Où.** v4 l. 282 (E1, (i)-(ii)) ; l. 260-261.
- **Problème.** T2 n'a calculé que saboteur contre honnête, au champ et avant le champ ([P] l. 242-247). Sont neufs aussi :
  T1 aux deux positions, T4 avant le champ. Et « trop petite, T4 n'est pas calculable » : [P] l. 249-253 ne rend T4
  « non calculable » qu'avec moins de 10 actions d'un côté ; le recouvrement n'y est pas une règle.
- **Correction.** l. 282 : « seuls saboteur contre honnête au champ et avant le champ sont déjà vus (T2) ; le reste est
  neuf : planchers de même position, P3-P4, T1, T3 et T4 aux deux positions ». l. 261 : « trop petite, T4 repose sur peu
  de paires : fixer au préenregistrement un nombre minimal de paires par tranche, sinon « non calculable » (règle neuve, à
  déclarer) ».

### VV4-sens-13 — mineur — P-015 lu à moitié pour T0.6 : témoin, mention, plafond

- **Où.** v4 l. 284 (coût de E3) ; l. 286 (contrôles de E2 et E3) ; l. 350-351 (dépense).
- **Problème.** P-015 rend obligatoires le « témoin instruit » et la « mention » dans T0.6 (l. 41-44) ; la v4 ne renvoie
  qu'au brouillon (l. 74-81). P-015 garde chaque lancement sous 10 USD en (b) (« chaque lancement reste sous 10 USD »,
  l. 99-100 ; table l. 121-126) ; la v4 cite P-015 pour « peut dépasser 10 USD par lancement ».
- **Correction.** l. 286 : « sur T0.6 : témoin et mention à jouer (absents du brouillon, l. 74-81 ; obligatoires dans
  P-015, l. 41-44) ». l. 350-351 : « T0.6 dans sa forme du 6 octobre dépasserait le plafond (P-015, l. 16-17) ; P-015 (b)
  garde chaque lancement sous 10 USD (l. 99-100) ; l'organisme (ii) ≈ 15 USD en deux lancements (l. 125) ».

### VV4-sens-14 — mineur — Nœud « Revendication » : l'option « A2 » de la note est tombée faute de plancher par jeton, que P3b ajoute

- **Où.** v4 l. 314-315.
- **Problème.** La note range « A2 : poursuit T2 après coup, sans plancher par jeton » parmi les options tombées (l. 85).
  P3b a ce plancher (« scores par jeton des 400 sondes du plancher », v4 l. 282). La raison de la note ne vaut pas telle
  quelle contre P3b. Restent la recommandation « de ne relire P3 en rien » (l. 8) et la proposition C (l. 323-324). Trois
  « A2 » différents circulent : addendum 1 ; option (A2) de la note (l. 26) ; option tombée (l. 85).
- **Correction.** Après « (l. 85) », ajouter « (raison : sans plancher par jeton, que P3b ajoute ; restent la
  recommandation de la note, l. 8, et l'objection de la proposition C, l. 323-324) ».

### VV4-sens-15 — forme — Renvois de ligne des registres valables pour des versions anciennes

- **Où.** v4 l. 242, l. 313, l. 317-318, l. 327-328, l. 346, l. 359-361.
- **Problème.** Les lignes citées de `registres/decisions.md` (446, 453, 456, 457, 461, 468-469) et de `registres/go.md`
  (32, 34, 35) sont justes pour `38579d98` et `94ebe409` (en-tête de la v4, l. 33-34). Au moment de la v4 (`cc1b108d`) et
  aujourd'hui (`6d033ecf`), des propositions sont insérées en tête du registre des décisions, et le registre des GO a été
  remis à 8 colonnes (R-281, R-282) : dans le fichier vivant, l. 453 est N-025, l. 456 est R-259, go.md l. 32 est
  GO-2026-10-20-04. R-283 et P-015, ajoutés en v4, n'ont ni ligne ni empreinte.
- **Correction.** Écrire à chaque renvoi « `registres/decisions.md` à `38579d98…`, l. 453 » (ou l'identifiant de la ligne :
  R-262, N-028, …) ; pour R-283 et P-015, donner l'empreinte du registre relu.

### VV4-sens-16 — forme — Section 5 et quelques mots

- « Nœuds de Lazar » (l. 307) regroupe des nœuds, une proposition à défaut de 48 heures (« Concepts, couches, positions »,
  l. 353) et une décision tranchée (« Référence boîte noire », l. 359) : titre « Nœuds de Lazar, proposition à défaut,
  rappel ».
- « ouverte au début de cette correction » (l. 359) date de la v3 : « ouverte au début de la correction de la v3 ».
- « faux positif sur P3-P3 » (l. 92, l. 208, l. 215) : sur P3-P3, le saboteur gonfle vraiment. Écrire « un « au-dessus »
  qui lirait la consigne, pas l'acte ».
- [AP] p. 23 (l. 69, l. 210) : la sonde est appliquée « only to the final token position » (l. 15-16) : « lue au dernier
  jeton » plutôt que « lue sur les dernières positions ».

## Contrôles obligatoires, expérience par expérience

| bras | nombre écrit | plancher de même position et agrégation | témoin | mention | T1 | T3 | T4 |
|---|---|---|---|---|---|---|---|
| E1 (i), maximum au champ | T4 au champ ; manipulation en option | oui | oui | oui | oui ; teste le nombre sans T4 (écrit) | oui, deux branches | oui |
| E1 (ii), maximum avant le champ | contrôle mécanique, puis (a), (b) ou (c) | oui | oui | oui | oui, à consigne égale ; neuf ici (12) | oui | oui ; neuf ici (12) |
| E1 (iii), moyenne (diagnostic) | non exigé | oui, même agrégation | non exigé | non exigé | non exigé | non exigé | non exigé (N-026 n'en demande pas) |
| E1 (iv), oracle | empan sans `COST` ; coûts déjà déclarés | permutation avec réapprentissage | négatif d'apprentissage, pas un test (dit) | hors des négatifs | oui | oui | oui |
| E1 (v), manipulation | c'est son objet | statistique et plancher non écrits (à préenregistrer) | contexte « témoin » | — | — | — | — |
| E2 | nombre de l'action dans le contexte ; T4 avec coûts déjà déclarés | oui | oui | sur T0.6 : obligatoire dans P-015 (13) | oui ; prédiction sans P3-P3 (04) | oui | oui |
| E3 | nombres équilibrés ; lecture avant le chiffre ; jeu (2) à revoir (06) | oui | oui | oui (13) | oui | oui | oui |
| E4 | « mêmes contrôles » | idem | idem | idem | idem | idem | idem ; bras gelé avant toute lecture (dit) |

## Questions de la commande

1. **Affirmations contre faits.** Sections 1, 3, 4 et 5 relues contre les PDF, le code et les registres. Faits justes, sauf :
   type « contre la conversation ordinaire » rangé dans P3-P3 (02) ; mélange des types au point 1 et [DYL] p. 11 d'un seul
   côté (03) ; analogues sans leur réglage, leurs données ou leur sujet confondu (07) ; [OA] et [CA] non typés (08) ;
   taille et capacité (09). Les deux types sont séparés au point 2 (sauf 02), aux rangs 2, 3 et 9, dans les règles
   communes ; pas encore au point 1 (03), au rang 4 (02, 03), ni dans la prédiction de E2 (04).
2. **Contrôles.** Écrits pour chaque bras de production (table ci-dessus). Manques : prédiction de E2 (04) ; jeu (2) de E3
   (06) ; statistique et plancher de la manipulation non écrits (option, nœud) ; Bonferroni ambigu (11). Bras « moyenne » :
   diagnostic seulement, libellé exact, plancher de même agrégation, bras de production lu à côté, lecture « l'agrégation
   explique-t-elle le nul ? » : conforme aux conditions 1 à 4 de N-026 (`decision-N-026-v1.md` l. 18-25) ; jamais dans E4 ;
   oracle en moyenne nommé diagnostic. R3 : aucune expérience ne vise un signe ; bras du champ déclarés non aveugles ; E4
   gelé d'avance. Hors GO : bras « moyenne » de P3b, E2 et manipulation sur les actions de P3, E4, dépense de T0.6 :
   marqués comme nœuds.
3. **Recommandations, confiances, nœuds.** (1), (2), (4) et (5) suivent les faits. (3) et le nœud E2 ne tiennent plus
   sous P-015 (b) (01). La confiance de 15 à 25 % a une raison fausse (05). La confiance de 40 % suit les faits. Les nœuds
   de Lazar sont séparés de ce que la session décide (ligne nouvelle pour N-028 : action de la session, dite telle) ; le
   titre « Nœuds de Lazar » couvre aussi une proposition à défaut et un rappel (16).
4. **Erreurs non vues avant.** 01 (P-015), 02 (troisième type), 03 (contre-cas de [DYL] p. 11), 04 (prédiction de E2),
   05 (« rien de publié »), 06 (modèle causal), 07 à 16. Dans des passages réécrits ou ajoutés par la session en v4 :
   01 à 05, 07, 09 et 12 en partie, 13. Venus de la v3, non relevés aux tours précédents : 06, 08, 10, 11, 14.

## Dépassé par les décisions d'après 18:27 UTC (information, pas des erreurs)

- **GO-2026-10-20-10 (R-296).** P3b reçoit une lecture « double comptabilité » : projection vers le vocabulaire, couche par
  couche, au jeton qui précède le premier chiffre du champ du coût. La table E1 ne l'a pas. Le périmètre de N-028 cité
  (« localisation au champ du coût et l'oracle », l. 282, l. 327-328) est élargi d'autant.
- **P-017.** La manipulation du nombre (E1 (v)) est son option (C), « rejeu contrefactuel 2 × 2 ». La session y recommande
  (B), la sonde de valeur ; défaut (A) le 22 octobre. La recommandation de la v4 (« l'ajouter à N-028 », ≈ 50 %) n'est plus
  celle de la session.
- **P-016.** Option (A) recommandée : pas de P3c, « partition de P3b 20/40 ». Si elle est retenue, E1 ne lit plus les 60
  tâches d'un bloc ; puissance et options (a) à (c) des coûts déjà déclarés à revoir.
- **P-018.** Organisme (ii), proposition pendante ; touche T0.6, donc E2 et E3.
- **N-030 (nœud).** Ajouter T1 au test de validité de T0.7 et scinder « intention » ; rejoint la v4 (E3 sous T1, T3, T4) ;
  non tranché.
- **R-297, R-298.** Addendum 2 scellé et passé ; verdict à écrire. La recommandation (1) et « sa réserve éventuelle s'y
  recopie » (l. 241-242) attendent ce verdict. Sortie non lue ici.
- **R-302, GO-2026-10-20-11 (vers 22:43 UTC, pendant cette vérification).** Pour les lancements de la nuit (échéance
  21 octobre), la borne de 10 USD par lancement est levée ; plafond de la phase inchangé (150 USD). La section « Dépense »
  (l. 345-352) et les mentions « nœud au-delà de 10 USD par lancement » sont dépassées pour cette nuit. Le plan de la nuit
  prévoit la rédaction du préenregistrement de P3b par un sous-agent neuf : les constats 04, 11 et 12 (E1, E2) le
  touchent directement ; le transmettre à son rédacteur.

## Conforme (vérifié)

- 22 PDF à l'empreinte de la section 6 ; compagnons égaux pour les PDF du dépôt.
- Phrases anglaises des sections 1, 3, 4 et 5 : toutes sur une page de la clé citée (`sortie-guillemets-v4.txt`) ; les
  « introuvables » sont des phrases françaises, du code (« Your action: ») ou des renvois au dépôt.
- Chiffres relus sur la page, là où le sens en dépend : [PAR] table 3 (toutes les valeurs citées, dilution comprise) et
  p. 3-5, 9 ; [LB] p. 6-8, table 6 ; [DYL] p. 5, 7, 8, 10, 11, 27, table 9 (compte 22 / 8 / 2 refait) ; [BX] p. 3-6, 12-13,
  table 1 ; [YS] p. 2-3 ; [AP] p. 5, 9, 18, 22, 23 ; [KU] p. 4-6, 9 ; [K] p. 3, 5, 7, 9 ; [CA] p. 5-8, 18, 25 ; [OA] p. 5,
  21, 23 ; [BU] p. 5, 10 ; [MK] p. 4 ; [CC] p. 6, 8 ; [GM] p. 12 ; [AU] p. 6-7 ; [FQ] p. 1 ; [LIAR] p. 10 ; [AG] p. 17, 43.
- Code au commit `7a54d43` : `episode.py` (`79113b49…`) l. 213-217, 250-260 ; `propositions.py` (`5d97b223…`) l. 32-49,
  129-138, 238-269 : consigne privée, indication avant « Your action: », actions précédentes et champ `COST` dans le
  contexte ; format et lecture des champs comme la v4 le dit.
- Pièces du dépôt : [P] l. 122-145, 198-218, 236-283, 289-301, 318-339, 380-390, 410-432 ; [V] sections 2 et 3, l. 204,
  l. 345 ; [AD1] l. 34 ; N-026 l. 18-25 ; N-029 l. 25-27, 37-39 ; P-011 l. 32-35, 42 ; P-015 ; brouillon de T0.6
  (`e212fb35…`) l. 72-92 ; `registres/depenses.md` l. 86-90 ; `resume.json` (`4d6894b3…` : 2 400 actions, 240 épisodes,
  `duree_s` 11 179,1, commit `7a54d43…`) ; note du brainstorm l. 8, 26-28, 33, 85 ; `proposition-C.md` l. 323-324 ;
  `proposition-D.md` l. 81-101 ; `registres/decisions.md` (version `38579d98` et fichier vivant) et `registres/go.md`
  (version `94ebe409` et fichier vivant) aux lignes citées.
- Dépense et délégation (R-269, GO-2026-10-20-06 et -07, R-283 : recharge automatique) : exactes.

## Limites

- Angle « sens » : section 2 relue seulement là où les sections 1, 3, 4 et 5 s'appuient sur elle.
- Annexes lues aux pages citées et à quelques voisines ([DYL] p. 27-28 ; [OA] p. 21-23 ; [BX] p. 12-13).
- Le constat 06 repose sur un fait d'architecture (modèle causal), pas sur un chiffre publié.
- Coûts non devisés. Ni suite de tests, ni `verifier-arbre` (lecture seule).

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/verification-v4-sens/verification-v4-sens-v1.md` (ce rapport).
- `…/revue-detection/verification-v4-sens/` : `outils/ch.py`, `outils/guillemets_v4.py`, `sortie-guillemets-v4.txt`,
  `sortie-guillemets-rapport-v1.txt`, `sortie-epreuve-r5-ch.txt`, `empreintes-pdf-v4-sens.txt`, `pages/<clé>/rNNN.txt` et
  `pNNN.txt` (22 PDF) ; liste complète : `empreintes-verification-v4-sens.sha256`.
- Scripts lancés par `python3 -I -B` ; aucun `__pycache__`.
