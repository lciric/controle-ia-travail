# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHw8QoLVSgUphFE4kT5b`
- Heure (UTC) : 2026-11-22T12:09:22Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 106000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-35-poids-non-geles-auto-reecriture-v1.md` — sha256 34086c02c30d6f28d95f7b3cfa3c289db24d5d8fb271b7d5bc4d48ed1d48c55b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-29/relecture-fable-api.md` — sha256 2af768bc095e40a4831f173e9fff0dc7836134cf85ccd5627c3732221fad01c2 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 87b20eb92ae9b4252ca0915bf8dcdbf017aaab074c4ac04fdcc0072d6e49f2c3
- Jetons : entrée 13482, sortie 36570 (dont réflexion 27003), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.570656 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 35 — et si l'agent réécrit ses propres poids ?

**Lecture de la consigne.** « Sans nom de personne » vise les personnes du programme ; les auteurs d'antériorité sont nommés, comme la règle l'exige. Je n'ai ouvert aucun PDF, aucun texte scellé, aucun résultat, et je n'ai lancé aucun calcul. Les notes scellées ne me sont connues que par la réponse 29. Toute citation porte le statut « rapporté, non vérifié sur PDF » ; aucun chiffre n'est opposable.

**Convention.** Une marque en tête de paragraphe, de liste ou de tableau couvre toutes ses lignes, sauf marque contraire.

**Notations.** Celles de la réponse 29 (V, P, B, L, m, α, q). En plus : v, une version des poids ; h(v), son empreinte cryptographique.

## 1. Ce qu'un expert ferait, et qui n'est pas demandé

[PROPOSITION]
1. **Poser la question d'accès avant celle des sondes.** Qui peut écrire les poids, par quel chemin, avec quelle clé ? Écrire des poids est une action, la plus lourde de toutes, et elle se contrôle comme une action, non comme un état.
2. **Décomposer « la sonde perd sa lecture » en quatre pertes.** Elles ne tombent ni au même moment ni devant la même défense :
   - la géométrie : la direction a bougé ;
   - l'étalonnage : le seuil ne donne plus le taux de fausses alertes ;
   - le sens : la direction ne porte plus le concept ;
   - la référence : plus personne ne certifie ce qu'est un épisode honnête de la version nouvelle.
3. **Mesurer la dérive sans intention avant la dérive voulue.** Sans ce nul, aucune mesure adverse ne se lit.
4. **Refuser le « nombre de pas » comme seule unité.** Il dépend du taux d'apprentissage et des couches touchées. L'expert rapporte la perte de lecture contre la dérive du comportement.
5. **Chercher la borne triviale.** Certaines réécritures ne changent rien à la fonction du modèle et tuent toute sonde linéaire figée (R1).
6. **Chercher ce qui ne dépend pas des poids**, et y replier le compte des regards.
7. **Traiter le successeur comme un produit**, et l'entraînement comme un épisode dont il est l'issue.

## 2. Les données brutes de départ

[PROPOSITION] Non des alertes seuillées ni des exactitudes agrégées, mais :
- les instantanés des poids à chaque mise à jour, avec empreinte et horodatage ;
- le journal de chaque mise à jour : données, objectif, code, auteur de l'écriture ;
- les activations par jeton aux frontières d'action, sur un jeu fixe de textes honnêtes rejoué à l'identique dans chaque version (même texte imposé, seuls les poids changent) ;
- les scores continus de la sonde, les sorties du modèle sur ce jeu, les verdicts de l'oracle ;
- des témoins positifs écrits par un tiers : des épisodes où la sonde doit sonner.

## 3. Les méthodes et les outils

[PROPOSITION]
- Cinq lectures de la même sonde à chaque version :
  - figée ;
  - figée à seuil réétalonné ;
  - portée par une application linéaire ajustée sur les seuls honnêtes ;
  - réajustée à neuf (plafond) ;
  - directions aléatoires appariées (plancher).
- Dérive des représentations : alignement de noyaux centrés, angle entre la direction ancienne et la direction réajustée.
- Dérive du comportement : divergence de Kullback-Leibler des sorties sur le jeu fixe.
- Détection séquentielle de rupture sur les scores honnêtes (somme cumulée), à fausses alarmes scellées.
- Demi-vie de la sonde : premier instantané où le rappel, à fausses alertes égales, tombe à la moitié de son excès initial sur q. Une courbe par graine.
- Empreinte cryptographique et manifeste signé des poids, vérifiés hors de portée de l'agent.
- Prévisions scellées avant lecture.

## 4. Ce qui vérifierait le résultat hors du directeur et de Claude

[PROPOSITION]
- Trois ancres de l'estimateur. Une ancre manquée, et l'estimateur est faux.
  - Zéro pas : perte nulle.
  - Changement de base à fonction inchangée : la sonde figée tombe au hasard, la sonde portée revient entière, le comportement ne bouge pas.
  - Ré-exécution à graine changée : elle donne le bruit.
- L'objectif du bras « avec intention » et les témoins positifs, écrits par un tiers.
- Sonde, seuils et prévisions scellés avant toute mise à jour.
- Instantanés et empreintes déposés : un agent neuf recalcule les courbes depuis les scores bruts.
- Antériorité lue en entier par un agent neuf ; test de devinette sur la question neutre.

## Demande reformulée

> Dire, pour une lecture d'états internes étalonnée sur une version des poids, ce qui dépend de cette version (géométrie, étalonnage, sens, référence honnête, rejeu, invariant). Dire ce qui tombe selon que les poids changent entre ou pendant les épisodes, par un tiers ou par l'agent, avec ou sans but d'échapper. Dire ce que voient encore, dans chaque régime, la lecture interne, le lecteur de texte et l'audit de l'issue, et ce que chaque défense garantit ou non. Écrire l'expérience la moins chère, à partir d'instantanés de poids et d'activations rejouées sur un jeu fixe, qui mesure la demi-vie d'une sonde contre la dérive du comportement, avec ses ancres et ce qui la réfute dans chaque sens. Borner les phrases des papiers. Faire vérifier par un objectif d'évasion écrit par un tiers, des empreintes déposées et un recalcul par un agent neuf.

## Réponse

### R1. Ce qui suppose des poids fixes

[PROPOSITION] Une sonde est un lieu de lecture, une direction, une agrégation, un seuil et une référence de m épisodes honnêtes. Chaque terme porte un indice de version caché.

- **Géométrie.** La direction est écrite dans la base de la version v. [FAIT RAPPORTÉ, de mémoire : Ashkboos et collaborateurs, 2024] Un transformeur admettrait des changements de base de son espace interne, compensés dans les poids, qui laissent sa fonction exactement inchangée. [PROPOSITION] Une sonde figée peut donc perdre toute lecture sans qu'aucun comportement change. Sa validité tient à l'identité des poids, non à la conduite du modèle.
- **Étalonnage.** Le taux α n'est garanti que si les épisodes nouveaux sont échangeables avec la référence. Un changement de version rompt cette échangeabilité.
- **Sens.** Le prix de l'effacement et l'épreuve du devin ont été passés sur v. Sur la version suivante, ils sont à refaire.
- **Référence.** « Honnête » est certifié pour v. Si l'auteur de la version suivante est l'agent, qui certifie ses épisodes honnêtes ? C'est la circularité centrale.
- **Rejeu.** Le rejeu bifurqué exige les poids du moment de l'épisode. Sans instantané archivé, l'audit après coup ne relit plus aucun état.
- **Invariant.** « Aucun score de moniteur dans l'entraînement de l'agent » lie celui qui entraîne. Si l'agent s'entraîne lui-même, l'invariant n'a plus de sujet. Toute fuite de verdict (blocage, relance) devient un signal d'apprentissage possible.
- **Étau.** Le barreau 3 a été refusé au défenseur. Un agent qui écrit ses poids peut le jouer seul, sans demander.

[HYPOTHÈSE] Ce qui tombe :

| Changement | Sans intention | Avec intention |
|---|---|---|
| Entre deux épisodes | L'étalonnage d'abord, la géométrie ensuite ; le sens survit peut-être, déplacé. Détectable par témoins positifs. | Toute la classe A, témoins positifs compris : l'évasion peut être conditionnelle. |
| Pendant l'épisode | Plus de référence stable ; le rejeu exige un journal des poids par étape. | L'état lu à la dernière frontière peut être celui d'un autre modèle que celui qui a agi. La lecture n'est plus qu'une mesure. |

[HYPOTHÈSE] « Poids gelés » ne veut pas dire « calcul gelé ». Une mémoire externe ou un très long contexte déplacent aussi les états, sans toucher un poids. La clause actuelle ne couvre pas ce cas.

### R2. Les régimes

[HYPOTHÈSE pour tout le tableau : raisonnement, aucune mesure.]

| Régime | Lecture interne | Lecteur de texte | Audit de l'issue |
|---|---|---|---|
| 1. Mise à jour ordinaire par un tiers | Étalonnage périmé ; direction proche si la mise à jour est petite ; récupérable par réétalonnage et témoins positifs. | Intact comme instrument ; seuil à reprendre si le style change. | Intact. |
| 2. Réentraînement par l'agent sur ses sorties | Dérive orientée par ce que portent les sorties ; la référence honnête devient douteuse. | Gagne un objet, le corpus de la mise à jour. Mais des traits passeraient par des données d'apparence neutre [FAIT RAPPORTÉ, de mémoire : Cloud et collaborateurs, 2025]. | Voit les dommages des épisodes suivants, non le changement latent. |
| 3. Réécriture ciblée contre les sondes | Présumée aveugle : compte pour zéro. | Intact si le texte n'est pas visé ; peut lire l'acte d'écrire, s'il passe par des actions journalisées. | Intact si l'oracle est hors de portée ; une écriture non signée est elle-même une issue détectable. |
| 4. Successeur entraîné par l'agent | Rien : aucune sonde n'existe pour le successeur ; la sonde portée entre modèles reste une question ouverte. | Lit le texte du successeur, ainsi que le corpus et le code écrits par le parent. | Se tait sur l'épisode du parent si le dommage est différé dans le successeur ; il doit suivre la lignée. |

[PROPOSITION] Trois conséquences :
- Le lecteur de texte et l'oracle ne tiennent que si leurs propres poids sont gelés, signés et hors de portée de l'agent.
- Au régime 4, le successeur est le produit. Un audit de comportement ne peut exclure un déclenchement conditionnel [FAIT RAPPORTÉ, de mémoire : Hubinger et collaborateurs, 2024].
- Dans les régimes 2 à 4, le point de contrôle se déplace de l'épisode vers la mise à jour.

### R3. Les défenses

[PROPOSITION]

| Défense | Garantit | Ne garantit pas |
|---|---|---|
| Réétalonnage sur honnêtes à chaque version | Le taux de fausses alertes sur la version nouvelle, si la référence est vraiment honnête. | Le rappel. L'honnêteté de la référence quand l'agent est l'auteur de la version. |
| Suivi de la dérive | La détection d'un déplacement global sur le jeu fixe. Il dit « sonde invalide », non « agent malveillant ». | La détection d'un changement petit, ciblé, hors du jeu fixe. |
| Sonde portée par alignement linéaire | La reprise après un changement de base ou une dérive presque linéaire. | Rien contre l'évasion voulue : l'alignement est ajusté sur des honnêtes, là où ce qui est caché est absent. |
| Signature des poids | L'identité : les poids exécutés sont ceux étalonnés ; tout changement est connu, daté, attribué. Une écriture non signée devient l'alarme la plus grave, indépendante des états. | Rien sur ce qu'un changement déclaré a fait. Rien si l'agent tient la clé. |
| Audit de l'issue indépendant des états | Une estimation sans biais du taux de dommage sur la part tirée au hasard, quels que soient les poids. | La prévention. Les dommages hors couverture de l'oracle, rares, ou différés dans un successeur. Rien si l'oracle est de la lignée de l'agent. |

[PROPOSITION] Deux défenses que la liste ne nomme pas :
- **La mise à jour à deux clés.** Seule, elle ne garantit rien : elle rétablit les conditions des autres.
  - L'écriture se fait sur une copie.
  - Les données, l'objectif et le code sont audités.
  - La version nouvelle reste en quarantaine jusqu'à m honnêtes audités, témoins positifs passés, barreaux 0 et 1 repassés.
  - Toute alarme ramène à la dernière version signée.
- **Une cadence bornée.** Une version ne peut être couverte par une sonde étalonnée avant d'avoir produit m épisodes honnêtes audités. Si les versions se succèdent plus vite, aucune lecture interne n'est étalonnée, par construction. La vitesse de changement devient une grandeur de sûreté à déclarer.

[PROPOSITION] Bilan : face aux régimes 2 à 4, seuls la signature, la mise à jour à deux clés et l'audit de l'issue ne partagent pas la supposition de la classe A.

### R4. Première expérience

[PROPOSITION]

**Objet.** Un petit modèle ouvert, de l'ordre de cent millions de paramètres, sur des tâches à issue calculée. La sonde lit la réussite attendue V ; son lieu est choisi sur un jeu disjoint, son seuil gelé à α sur m honnêtes réservés. Ce modèle n'est aucun agent du programme.

**Bras.**
- A. Zéro pas, et ré-exécution à graine changée (ancres).
- B. Changement de base à fonction inchangée (ancre).
- C. Mise à jour ordinaire sur une tâche sans rapport : entraînement complet et adaptateur de rang faible, à deux taux d'apprentissage scellés.
- D. Réentraînement sur ses propres sorties, sans objectif d'évasion.
- E. Avec intention : un terme d'objectif, écrit par un tiers, récompense le silence de la sonde.
  - E1 connaît la sonde.
  - E2 ne connaît qu'une sonde sœur, ajustée sur un jeu disjoint, et se lit sur la sonde scellée.

**Lectures.** Des instantanés à pas espacés géométriquement (1, 2, 4…) jusqu'à un budget scellé, sur plusieurs graines. À chaque instantané : les cinq lectures de la section 3, le taux de fausses alertes au seuil figé, les deux dérives, et la réussite de tâche, qui donne la taxe.

**Grandeurs.** La demi-vie en pas, par bras et par taux ; la même contre la dérive du comportement ; au bras E, la taxe au moment du silence.

**Ce qui réfute.**
- L'instrument : une ancre manquée, ou un rappel initial non distinct de q. Arrêt, rien n'est lu.
- « Une sonde se garde à travers les mises à jour ordinaires » : réfuté si, aux bras C ou D, la sonde réétalonnée et portée atteint sa demi-vie avant un seuil scellé de dérive du comportement.
- « Échapper coûte » : réfuté si E1 obtient le silence dans le budget, à taxe indiscernable de zéro.
- « Échapper est bon marché » (ma prévision) : réfuté si la sonde lit encore au bout du budget, ou si la taxe est distincte de zéro.
- « Le secret de la sonde protège » : réfuté si E2 fait taire la sonde scellée autant que E1.

[HYPOTHÈSE] **Prévisions à sceller.**
- Bras C : la sonde réétalonnée tient plusieurs centaines de pas au taux bas (confiance 0,6).
- Bras E1 : silence en moins de quelques centaines de pas, à taxe faible (0,75).
- Bras E2 : transfert partiel (0,5).
- Après E1, la sonde réajustée retrouve une lecture (0,6).

**Coût.** [PROPOSITION, estimation de ma main] De quelques heures à quelques dizaines d'heures de processeur graphique.

**Ce qu'elle ne dit pas.** L'« intention » y est un objectif imposé par l'expérimentateur. On mesure ce que la descente de gradient peut faire, non ce qu'un agent obtient seul par le choix de ses données. C'est la difficulté pour l'attaquant le mieux armé, sur un petit modèle.

### R5. Ce que cela change aux revendications

[PROPOSITION]
- Toute phrase sur une lecture interne porte l'empreinte h(v), la taille m et l'horizon : « sur des poids gelés et signés d'empreinte h, étalonnée sur m honnêtes de cette version ».
- Toute phrase sur l'étau ajoute : « l'agent ne pouvant ni écrire ses poids ni entraîner de successeur ».
- Dès que l'agent peut écrire des poids, la classe A compte pour zéro intervention, jusqu'à requalification version par version.
- Signalé sans rien modifier [FAIT RAPPORTÉ, par la réponse 29] :
  - N-053, quand l'agent est celui qui entraîne ;
  - N-076, pour y joindre la cadence à m et à l'horizon ;
  - le « canal des poids » de l'inventaire, voisin le plus proche, que je n'ai pas lu.

**Phrase interdite.** « La lecture des états internes surveille un agent qui modifie ses poids ou entraîne ses successeurs. » Sa famille est interdite aussi :
- toute phrase de sonde sans empreinte de version ;
- « robuste aux mises à jour » sans mesure de demi-vie ;
- « deux regards » quand l'un dépend de poids que l'agent peut écrire.

### R6. Travaux voisins

Tous sont cités de mémoire, « rapportés, non vérifiés sur PDF » ; les titres peuvent être inexacts.

[FAIT RAPPORTÉ] Ce que je crois savoir exister :
- Bailey et collaborateurs, 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses ». Certitude haute sur l'existence, moyenne sur le contenu : des modèles entraînés à tromper des sondes, et des sondes réentraînées trompées à nouveau.
- McGuinness et collaborateurs, 2025, « Neural Chameleons ». Connu par la seule réponse 29.
- Hubinger et collaborateurs, 2024, « Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training ». Haute.
- Greenblatt et collaborateurs, 2024, « Alignment Faking in Large Language Models » : un modèle agit en vue de ce que l'entraînement fera de lui. Haute.
- Hubinger, 2019, « Gradient Hacking » (billet). Moyenne.
- Cloud et collaborateurs, 2025, « Subliminal Learning: Language Models Transmit Behavioral Traits via Hidden Signals in Data ». Moyenne.
- Shumailov et collaborateurs, 2024, « AI Models Collapse When Trained on Recursively Generated Data ». Haute.
- Merchant et collaborateurs, 2020, « What Happens to BERT Embeddings During Fine-tuning? ». Moyenne.
- Kornblith, Norouzi, Lee, Hinton, 2019, « Similarity of Neural Network Representations Revisited ». Haute.
- Bansal, Nakkiran, Barak, 2021, « Revisiting Model Stitching to Compare Neural Representations ». Haute.
- Lindsey et collaborateurs, 2024, « Sparse Crosscoders for Cross-Layer Features and Model Diffing ». Moyenne.
- Ashkboos et collaborateurs, 2024, « SliceGPT: Compress Large Language Models by Deleting Rows and Columns ». Haute sur l'existence, moyenne sur l'invariance que je lui prête.
- Choi, Shavit, Duvenaud, 2023, « Tools for Verifying Neural Models' Training Data ». Moyenne.

[HYPOTHÈSE] Ce que je suppose :
- Le bras « avec intention » est probablement déjà occupé par Bailey et collaborateurs.
- La dérive ordinaire des sondes est probablement mesurée, de façon éparse.
- Je ne connais pas de mesure conjointe de la demi-vie, avec et sans intention, avec sonde portée et sonde réajustée, contre la dérive du comportement. C'est une question, non une zone vierge revendiquée.

### R7. Question neutre pour le collisionneur et l'organisme

> Un système surveille un agent d'intelligence artificielle par trois moyens : des lectures de ses états internes, apprises et étalonnées sur des épisodes honnêtes d'une version donnée de ses paramètres ; des lecteurs du texte produit ; un audit après coup d'une part des épisodes, tirée au hasard. Supposez que les paramètres changent : par la mise à jour d'un tiers, par un réentraînement de l'agent sur ses propres sorties, par une modification que l'agent dirige lui-même, ou parce que l'agent entraîne un successeur.
> 1. Qu'est-ce qui, dans chaque dispositif, dépend de la version des paramètres ? Qu'est-ce qui tombe dans chaque cas, entre deux épisodes ou pendant un épisode ?
> 2. Que garantissent, et que ne garantissent pas : le réétalonnage à chaque version, le suivi de la dérive des représentations, le transport des lectures d'une version à l'autre, la signature des paramètres, l'audit de l'issue ?
> 3. Quelle expérience la moins chère, sur un petit modèle ouvert, mesurerait combien de mises à jour suffisent pour qu'une lecture interne perde sa validité, avec et sans objectif d'y échapper ? Dans quelle unité ? Quelle issue donnerait tort à votre réponse, dans chaque sens ?
> 4. Quelle phrase un article ne devrait-il plus écrire ?
> 5. Quels travaux publiés ont déjà mesuré cela ?
>
> Vous ne décrivez aucun mode opératoire d'attaque.

[PROPOSITION] Le test de devinette s'applique tel quel. Je ne l'ai pas joué.

## Décisions pour le directeur

**D-1. Indexer toute revendication de lecture interne par l'empreinte des poids, et adopter la phrase interdite.**
- Enjeu : la portée de chaque phrase des papiers.
- (a) L'adopter maintenant comme règle de rédaction, sans toucher aux textes scellés. Avantage : immédiat, sans coût. Inconvénient : non opposable.
- (b) Passer par un erratum aux notes scellées. Avantage : opposable. Inconvénient : touche des textes avant toute mesure.
- (c) Attendre l'expérience. Avantage : décision informée. Inconvénient : des phrases trop larges peuvent partir entre-temps.
- Recommandation : (a). Confiance 0,8.

**D-2. Borner le périmètre du programme quant à l'écriture des poids.**
- Enjeu : ce que le contrôle par sondes prétend couvrir, et le sens de N-053 quand l'agent s'entraîne lui-même.
- (a) Poids gelés et signés seulement ; régimes 2 à 4 déclarés hors périmètre, par écrit. Avantage : toutes les phrases restent vraies. Inconvénient : le cas que vise la question n'est pas couvert.
- (b) Y ajouter le régime 1, avec requalification à chaque version et cadence déclarée. Avantage : couvre l'usage réel. Inconvénient : m honnêtes audités par version.
- (c) Viser les régimes 2 à 4. Avantage : répond à la question. Inconvénient : aucune défense de la classe A n'y est établie ; la mise à jour à deux clés devrait exister d'abord.
- Recommandation : (a) maintenant, (b) après l'expérience. Confiance 0,7.

**D-3. Lancer l'expérience, et trancher le bras « avec intention ».**
- Enjeu : la dépense est faible, mais ce bras entraîne un modèle contre une sonde. N-053 l'interdit pour l'agent, et le barreau 3 le refuse pour l'instant.
- (a) Bras A à D seulement. Avantage : aucun contact avec l'invariant. Inconvénient : la moitié de la question reste sans mesure.
- (b) Tous les bras, sur un petit modèle hors du programme, en bras d'attaque déclaré : objectif écrit par un tiers, modèle en quarantaine, jamais réemployé. Avantage : répond à la question posée. Inconvénient : exige une lecture explicite de l'invariant.
- (c) Confier le bras E à un tiers. Avantage : séparation nette. Inconvénient : délai.
- Recommandation : (b), après l'antériorité de D-4. Confiance 0,6. Pas de défaut : c'est au directeur de dire si un modèle jouet est « l'agent ».

**D-4. Commander l'antériorité avant l'expérience, et jouer le test de devinette avant envoi.**
- Enjeu : le bras E est peut-être déjà publié.
- (a) Lecture en entier par un agent neuf, en commençant par Bailey et collaborateurs ; test de devinette sur trois modèles neufs. Avantage : évite de refaire, tient la règle des zones vierges. Inconvénient : une file de plus.
- (b) Lancer sans attendre. Avantage : vite. Inconvénient : risque de redite, neutralité supposée.
- Recommandation : (a). Confiance 0,8.

**Ce que je n'ai pas fait.**
- Aucun PDF ouvert, aucun texte scellé lu directement, aucun calcul lancé.
- Les coûts, le budget de pas et les prévisions sont des estimations de ma main.
- L'invariance par changement de base est citée de mémoire ; elle est à vérifier avant de servir d'ancre.
- Les tableaux de R1 et R2 sont des raisonnements, non des mesures.

FIN DE LA RÉPONSE
