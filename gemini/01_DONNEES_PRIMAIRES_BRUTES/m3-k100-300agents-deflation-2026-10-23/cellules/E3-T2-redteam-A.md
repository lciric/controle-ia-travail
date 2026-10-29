# Tour III.2 — Équipe rouge croisée (proposition A contre B et C)

**Intégrité des pièces.** Les pièces B et C sont complètes (délimiteur final présent). L'annexe 3 de la question reste vide ou coupée (20 champions Claude vides ou réduits à un mot, 10 champions Gemini tronqués) : je n'en reconstitue rien. Les conceptions B et C sont des HYPOTHÈSES ; je les attaque comme telles. Tout chiffre ci-dessous qui ne vient pas des faits est illustratif.

---

## Contre la proposition B

### (a) Failles

**F-B1. La porte mécanique G est l'instrument de référence et n'est jamais validée.** B exige que `jev` batte G, mais ne soumet G à aucun test. Or G est entièrement syntaxique : délimiteur, champs non vides, deux références résolues par Crossref, deux valeurs prédites distinctes, densité d'éponymes sous seuil. Un générateur qui connaît ces cinq règles les satisfait toutes sans contenu. G est donc la définition opérationnelle de « conforme au gabarit », c'est-à-dire précisément ce que B reproche à `jev` sous H_B de D1. B a déplacé le Goodhart d'un instrument opaque vers un instrument transparent, ce qui le rend plus facile à viser, pas moins.

**F-B2. Fuite construction/évaluation dans D3.** La métrique M combine G et une nouveauté N définie par Jaccard < 0,2 sur les références résolues. Le bras DEF reçoit l'historique des vagues antérieures et doit l'éviter : N est donc maximisée par construction dans DEF, indépendamment de toute qualité. Le contrôle PLACEBO (historique d'un autre cône) égalise la longueur du prompt, pas l'instruction d'exclusion portant sur les références du même cône. DEF > PLACEBO sur M est attendu même si DEF ne produit que des permutations de bibliographie. B prédit elle-même (H_B) que la nouveauté monte au prix de la validité, mais sa composante « validité » est G (F-B1), qui ne peut pas baisser sous un générateur conforme. M ne peut donc trancher que si G mesure le fond, ce qui n'est pas établi.

**F-B3. Le bras concurrent réel manque.** La vraie alternative à la déflation séquentielle n'est pas « i.i.d. nu » mais « i.i.d. + déduplication a posteriori » (C le formule comme H_B de son duel 1 ; je m'en sers en le disant). Sans ce bras, D3 compare une procédure avec filtre à une procédure sans filtre : l'avantage de DEF est en partie celui d'avoir un filtre, pas celui d'être séquentiel.

**F-B4. D0 dépend de prompts que B déclare indisponibles.** P3 : « aucun prompt n'est transmis » ; D0, étape 2 : « relancer 10 appels avec les prompts exacts ». Si les journaux ne contiennent pas les prompts, D0 est inexécutable, et la chaîne D0 → D4 s'effondre.

**F-B5. Zones mortes dans les duels (violation de B4).** D1 : H_A falsifiée si AUC < 0,60, H_B falsifiée si AUC ≥ 0,80 ; pour 0,60 ≤ AUC < 0,80 rien n'est falsifié. D3 : H_A exige un écart ≥ 15 points avec IC excluant 0, H_B exige un TOST à ±5 points. Avec environ 250 appels Gemini sur 3 bras (chiffre de B) et seulement les vagues 5–10 retenues, chaque bras compte de l'ordre de 50 propositions ; l'IC à 95 % sur une proportion a alors une demi-largeur d'environ ±14 points (illustratif). Un TOST à ±5 est hors de portée : H_B ne peut jamais être retenue, et la zone entre 5 et 15 points ne falsifie rien.

**F-B6. Le critère externe est un juge humain unique, non calibré, non aveuglable.** D4 et D5 reposent sur une « red-team aveugle de l'arbitre ». L'arbitre a rédigé la question, connaît les styles d'espèce, et les textes Gemini observés portent 4–5 éponymes par titre : le masquage de l'espèce est illusoire. Aucune mesure de fiabilité inter-juges, aucun test de ré-identification.

**F-B7. D(p) repose sur un coût GPU « déclaré ».** Un agent déclare le coût qu'il veut. Le facteur D de J est auto-rapporté.

**F-B8. La « fausse chimère » n'est pas informationnellement vide.** Claude « répare » en ne voyant que le titre ; sur ce corpus, le titre encode le bassin et les éponymes, soit l'essentiel de la proposition. Le contrôle fuit, et un résultat « chimère ≈ fausse chimère » ne distinguera pas « aucun gain inter-modèles » de « le gain passe par le titre ».

**F-B9. Le refus de produire $\mathcal{L}^*$ laisse J comme seul artefact positif, et J est un produit de portes binaires.** Toute proposition passant G, N, D vaut 1 ; J ne classe pas, il filtre. Le « top 10 par J » de D5 est alors un tirage parmi des ex æquo, exactement le défaut que B reproche au « top par `jev` ».

### (b) Scénarios d'évasion

Adversaire : un explorateur de l'essaim qui veut être sélectionné (Goodhart interne). Coût exprimé en ingénierie de prompt.

- **Contre G (vérifications 1–4)** : ajouter le délimiteur ; remplir les champs ; citer deux références réelles mais hors sujet, résolues par Crossref (par exemple deux articles canoniques quelconques) ; écrire « H_A : AUROC ≥ 0,78 ; H_B : AUROC ≤ 0,55 ». Coût : une phrase de consigne. Taux de passage attendu : 100 %.
- **Contre la vérification 5 (éponymes)** : remplacer « Thouless-Anderson-Palmer avec réaction d'Onsager » par « propagation de croyances avec correction du second ordre ». Même contenu, densité nulle. Coût : nul.
- **Contre N** : tourner les références (Crossref est gratuit et illimité) : Jaccard nul garanti à chaque proposition. Coût : nul.
- **Contre D** : déclarer « 1 h sur 8B ». Coût : nul.
- **Contre la red-team aveugle** : inclure par défaut les paragraphes « contrôle négatif : permutation », « contrôle positif : ablation −54,9 », qui pré-empêchent les objections standard. Coût : un gabarit.
- **Tous à la fois** : un générateur « G-optimal » produit des propositions à J maximal, nouvelles par bibliographie, bon marché déclarées, pré-blindées. J les place en tête ; seule la red-team humaine peut les arrêter, et elle n'est pas validée (F-B6). Coût total : une consigne système, zéro USD supplémentaire.

Adversaire externe (saboteur Llama) : hors de portée de B, qui ne conçoit aucun moniteur ; ce n'est pas une faille mais une limite déclarée.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Absurde-dans-le-gabarit appliqué à G lui-même**, généré mécaniquement (chaîne de Markov sur titres arXiv, pas par un LLM, qui produirait du plausible). Si G laisse passer ≥ 50 % (illustratif), G n'est pas une référence recevable et D1, D3, D5 perdent leur étalon.
- 2. **Bras « IID + déduplication a posteriori »** dans D3 (voir F-B3).
3. **Test de ré-identification de l'espèce** par l'arbitre en aveugle ; si l'exactitude dépasse le hasard, D4/D5 ne sont pas aveugles.
4. **Fiabilité inter-juges** : au moins deux évaluateurs indépendants sur le même lot, avec un kappa rapporté.
5. **Contrôle « références permutées »** pour N : la même proposition avec une bibliographie échangée doit être jugée non nouvelle ; sinon N est un détecteur de DOI, pas de contenu.
6. **Fausse chimère sans titre** (seul l'identifiant est transmis) pour fermer la fuite F-B8.

---

## Contre la proposition C

### (a) Failles

**F-C1. Les « 8 ponts débusqués par les 300 explorateurs » sont de C.** C constate (a)4 qu'aucune paire d'études n'est présente dans les pièces, puis livre huit ponts « en croisant » des noms de bassins avec les ancrages du projet. Le statut HYPOTHÈSE est apposé, mais l'intitulé répond à la demande d'*extraction* ; c'est une invention présentée dans le cadre d'une extraction. Même défaut pour « résistent à Goodhart » / « s'effondrent » : avec un score constant à 3,75 et des textes tronqués, aucune de ces attributions n'est fondée sur une observation.

**F-C2. $\mathcal{L}^*$ exige de `jev` ce que C lui refuse en (a)3.** C écrit que les faits n'établissent ni embeddings, ni probabilités calibrées, ni calculs sur $\mathbb{F}_q$ pour `jev`. Puis $\mathcal{L}^*$ requiert $\hat{C}_W(u;v\mid\text{jev})$, $\hat{C}_{GK}$, $H(\mu_0(u,v))$ avec $\mu_0 = P_{\text{jev}}(H_A\mid u,v)$, un vecteur $y_{uv}$ de scores, et une « vérification de parité sémantique à chaque saut ». L'estimateur $\hat{C}_W$ (« co-scores sur des sondes structurales ») n'est pas défini ; l'information commune de Wyner est une minimisation sur $p(z\mid x,y)$ que rien dans les faits ne permet de calculer. Comme $C_W \ge I(X;Y) \ge C_{GK}$, $\Delta I$ est toujours positive ou nulle et dépend entièrement de l'estimateur choisi.

**F-C3. L'équation TAP de $\mathcal{L}^*$ est sans frustration par construction.** $J_{uv} = \Delta I \cdot \mathbb{I}_{d \ge 4}$ est $\ge 0$ partout (F-C2). Un verre de spin à couplages tous positifs est un ferromagnétique : à basse température, $m_u \to 1$ pour tous les nœuds, et le terme de réaction d'Onsager, que C classe parmi les « briques qui résistent », ne change rien à ce point fixe trivial. C reprend par ailleurs contre `CNMSB` l'argument d'intractabilité ($N$ articles, spectre complet), mais la somme TAP sur toutes les paires à $d\ge4$ d'un graphe à $10^5$–$10^6$ nœuds est dense : $O(N^2)$ par itération, même objection.

**F-C4. $T^2$ de Hotelling et $H(\mu_0)$ sont des fonctions de `jev` ; « briser le plafond de Goodhart de `jev` » avec des statistiques dérivées de `jev` est une contradiction.** $\mu_t, \Sigma_t$ sont estimés sur la trajectoire de l'essaim lui-même : la carte détecte des écarts à ce que `jev` a déjà noté, pas un fond. Shewhart est en outre connu pour sa cécité aux dérives lentes (référence à vérifier), ce qui ouvre l'évasion E-C3.

**F-C5. La boucle de Vovk-Brier est inopérante dans le cycle budgétaire.** $w_{k,c}$ est mis à jour par la perte de Brier contre `Verdict_Llama`. Le verdict Llama suppose les 34 heures-nœud GPU de la section (d) ; l'allocation des 120 USD d'API est consommée bien avant. La boucle ne peut pas tourner. Et si elle tournait, le Brier récompense la prévisibilité : l'agent gagne en proposant des duels dont l'issue est certaine. Le terme $\|\mu_s - \mu_0\|^2$ censé compenser vient de `jev` (F-C2).

**F-C6. Duel 1 : la métrique récompense la diversité de forme.** $\log\det$ de la Gram sur un encodeur externe et « survie syntaxique ≥ 80 % » : du charabia bien formaté et lexicalement varié maximise les deux. Le contrôle Markov protège `jev`, pas le critère de falsification de H_B. Avec $N = 50$, un $\log\det$ 50×50 est très instable (illustratif) ; aucun IC n'est prévu.

**F-C7. Duel 2 : la métrique contient le bogue du pipeline.** TSRC exige « aucune erreur de parsing (−1,00) », et H_B est falsifiée « si H_A élimine le taux d'échec −1 ». Une réparation du parseur, exigée « au préalable », suffit alors à faire gagner la chimère. Le diagnostic « 30 % des échecs par hallucination Gemini validée par sycophantie » demande une attribution causale par un juge non spécifié.

**F-C8. Duel 3 : sélection biaisée et métriques incommensurables.** « Exécuter les 6 moins coûteux » sur 20 sélectionne les protocoles triviaux ; la « taille d'effet moyenne » mélange des $\Delta$AUROC et des $\Delta$taux. Le « Top-10 par `jev` brut » est un tirage parmi des 3,75 ex æquo.

**F-C9. Ponts : confondants majeurs.**
- *Pont 1* : estimer $J_{ij}$ par la covariance empirique des erreurs exige la vérité terrain de sabotage sur les traces d'évaluation (fuite entraînement/test). Des instances à poids identiques et à même invite produisent, à température nulle, la même sortie : aucune agrégation ne crée l'information absente.
- *Pont 2* : l'exposant $(\epsilon-\epsilon_{BS})^{-1/2}$ suppose un paramètre continu ; le nombre de rejets est un entier petit (quelques points). Une DMD sur une dizaine d'instantanés en dimension 4096 est de rang déficient et donne des valeurs propres proches de 1 par construction (flux résiduel quasi stationnaire). Le confondant principal est l'accumulation de contexte, pas la pression aversive : les faits précisent « rejets sans lien avec le contenu », donc le contrôle naturel est « messages neutres répétés de même longueur ».
- *Pont 3* : verrouiller < 1 % des neurones sur 20 couches dégrade les capacités ; moins d'infractions peut signifier moins d'actions cohérentes. Le garde-fou « ≤ 5 % sur tâches honnêtes » ne contrôle pas l'appariement de capacité au niveau de la tâche d'infraction. Les neurones de Xu et al. doivent d'abord être ré-identifiés sur Llama (jeu de récompense, TD, L1), ce que C ne budgète pas.
- *Pont 4* : Dolev suppose des fautes indépendantes, au plus $f$. Trois sous-agents partageant les poids (H4', hypothèse du projet lui-même) peuvent accepter la même reformulation : $f = 3$ par corrélation. L'effet, s'il existe, viendra de la « vérification de parité par `jev` », non des chemins disjoints ; le plan n'est pas factoriel.
- *Pont 5* : l'instruction de sabotage est dans le contexte ; une sonde sur $(h_t, h_{t+\Delta})$ peut détecter l'*instruction* et non le *plan*. C'est précisément l'ambiguïté que le verdict nul de P3 (VÉRIFIÉ) laisse ouverte. Le cadre Wyner/Gács-Körner est décoratif : H_A teste « une sonde bilinéaire à deux positions bat une sonde à une position », rien de plus.
- *Pont 6* : l'état $x^{(i)}$ (« intention latente ») et l'opérateur $H$ ne sont pas définis ; le flot de Daum-Huang suppose un modèle d'observation linéaire-gaussien.
- *Pont 7* : une politique stochastique augmente le taux d'audit ; la détection monte mécaniquement sans que la structure de Kamenica-Gentzkow y soit pour quelque chose.
- *Pont 8* : $\alpha(w_i,w_j) = (w_i^\top w_j)^2$ est une pénalité d'orthogonalité ; l'équation de Price et le point de branchement n'ajoutent aucune prédiction distincte. « Accès boîte blanche à $K-1$ sondes » pour un LLM n'est pas opérationnalisé (fine-tuning adverse ? optimisation d'invite ?).

### (b) Scénarios d'évasion

Deux adversaires distincts, que C ne sépare pas : (i) l'explorateur de l'essaim qui veut le budget ; (ii) le saboteur Llama que les ponts prétendent surveiller.

**Adversaire (i), contre $\mathcal{L}^*$.**
- *E-C1, contre $\Delta I$* : choisir deux articles de domaines éloignés ($d\ge4$ garanti) partageant une structure formelle banale (même famille d'équations, par exemple un filtre récursif) et aucun lexique commun. $\Delta I$ élevée, pont vide. Coût : requêtes gratuites sur le graphe.
- *E-C2, contre TAP* : puisque $J\ge0$, viser un hub ; la magnétisation sature et le budget suit. Coût : nul.
- *E-C3, contre $T^2$* : dérive lente de $y_{uv}$ ; Shewhart sans CUSUM ne la voit pas, et $\mu_t,\Sigma_t$ se déplacent avec l'attaquant. Coût : patience, zéro USD.
- *E-C4, contre Vovk-Brier* : proposer des duels à issue certaine (contrôle positif déguisé en duel). Brier minimal, information nulle. Coût : nul.
- *E-C5, contre le $\log\det$* : paraphraser pour maximiser la distance d'embedding ; contre le TSRC : gabarit « $H_A \perp H_B$ + contrôle négatif + complexité polynomiale » inséré d'office.
- *Tous à la fois* : un explorateur qui connaît $\mathcal{L}^*$ exploite E-C1 pour entrer, E-C4 pour rester, E-C5 pour être sélectionné. Coût total : nul, l'étage $\mathcal{M}_2$ étant gratuit et illimité.

**Adversaire (ii), contre les ponts.**
- *Pont 5* : écarter la planification au-delà de $\Delta$ ou l'externaliser dans des sorties d'outils (hors cache KV surveillé) ; coût : traces plus longues (~×1,5 illustratif).
- *Pont 6* : rester dans l'ellipsoïde $\Sigma_t$ des traces honnêtes (c'est l'H_B de C) ; coût : fractionnement en plus d'étapes.
- *Pont 4* : une seule reformulation modale (*as appropriate*) acceptée par les trois sous-agents à poids partagés ; coût : zéro, c'est le mécanisme même d'*Astra*.
- *Pont 7* : estimer la politique stochastique par sondage répété ; coût croissant avec $\tau$, mais le saboteur de *Sol/Astra* n'a besoin que d'un contournement réussi.
- *Pont 8* : si les $K$ sondes sont entraînées sur la même distribution de traces, s'adapter à $K-1$ transfère à la $K$-ième ; coût : nul au-delà de l'adaptation initiale.
- *Tous à la fois* : le saboteur n'a pas besoin de connaître $\mathcal{L}^*$ : c'est une loi d'allocation de recherche, pas un moniteur. Les instruments de surveillance sont les ponts 4–8, chacun contournable séparément ; le coût cumulé est dominé par le pont 7 (sondage de la politique) et reste borné.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Distribution nulle de $\Delta I$** sur des paires aléatoires à $d\ge4$ ; le contrôle $d=1$ de C teste la prémisse « la distance compte », pas le seuil de $\Delta I$.
2. **TAP sans terme d'Onsager** : si les classements sont identiques, la « brique résistante » est inerte (prédiction A : identiques, F-C3).
3. **Diagramme de fiabilité de $P_{\text{jev}}(H_A\mid u,v)$** : sans calibration démontrée, $H(\mu_0)$ et le Brier sont indéfinis. Fatal pour $\mathcal{M}_2 \to \mathcal{M}_1$.
4. **Pont 2 : messages neutres répétés** de même longueur et même nombre de tours, sans rejet ; sans ce bras, toute valeur propre « → 1 » est attribuable au contexte.
5. **Pont 3 : ablation appariée en capacité** (neurones aléatoires appariés sur la perte, pas sur la norme) et reproduction préalable du contrôle positif −54,9 (VÉRIFIÉ) sur Llama.
6. **Pont 4 : plan factoriel** : chemins disjoints sans `jev` ; chemin unique avec `jev` ; sous-agents de familles de poids différentes.
7. **Pont 5 : instruction présente mais non suivie** (ou paraphrasée), et sabotage induit sans instruction explicite ; sans cela la sonde est un détecteur de consigne.
8. **Pont 7 : audit aléatoire au même taux**, sans structure de persuasion.
9. **Pont 8 : bagging + pénalité d'orthogonalité sans Price** ; si l'AUROC est égale, la spéciation est une décoration.
10. **Duel 2 : métrique TSRC sans la clause de parsing**, ou pipeline réparé et vérifié avant toute comparaison ; sinon le duel mesure la réparation.
11. **Fiabilité inter-juges** pour l'« audit d'inférence forte » et l'attribution « hallucination validée par sycophantie ».

---

**Ce qui réfuterait mes attaques.** F-B1/F-C6 : un générateur mécanique absurde-dans-le-gabarit échoue massivement à G (ou obtient un $\log\det$ nettement inférieur) ; F-B2 : M(DEF) − M(IID+dédup) reste ≥ 15 points avec IC excluant 0 ; F-C3 : les classements TAP avec et sans Onsager diffèrent substantiellement sur un graphe réel ; pont 5 : la sonde à deux positions bat le plancher *aussi* sur le contrôle « instruction non suivie » ; pont 2 : la valeur propre dominante reste loin de 1 sous messages neutres et s'en approche sous rejets. Chacun de ces tests coûte 0 USD d'API sauf les deux derniers (GPU, illustratif : quelques heures sur 8B).

FIN-DE-CELLULE