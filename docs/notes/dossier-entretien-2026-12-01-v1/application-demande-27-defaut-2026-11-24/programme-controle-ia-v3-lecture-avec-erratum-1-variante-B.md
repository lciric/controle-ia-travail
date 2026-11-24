# Contrôle boîte blanche des menaces diffuses
## Du sabotage étalé dans le temps au sabotage distribué dans l'essaim — et à la corruption du moniteur

**Programme de recherche — v3 — texte du 22 novembre 2026, complété le 24 novembre 2026** (remplace la v2 du 4 octobre 2026 ; seuls changent la thèse du papier A, le statut du lemme et du théorème négatif, H1, H2, H3, E1.3, E3.1 et le premier critère de succès)

**Scellé provisoirement le 24 novembre 2026 à 18:32Z** (défaut des décisions 1 à 4 de la réponse 27, GO-2026-11-23-32 ; décisions de Lazar GO-2026-11-24-15). Il se lit avec son erratum 1, qui prime : `docs/notes/dossier-entretien-2026-12-01-v1/erratum-1-programme-v3-lemme-application-v3.md`, variante B (lemme revendiqué dans son application, portée « temps seul » ; GO-2026-11-24-18 et GO-2026-11-24-21).

**Statut : scellement provisoire.** Deux passages portent la marque **sous simulation** : la question de l'étalement (section 3) et H3 (section 5). Ils reposent sur une dérivation non simulée. Un second scellement suivra les simulations.

**Ce que ce texte applique.** À la version 2 : les dix-neuf différences de la réponse 27 de Claude Fable 5.2 (22 novembre 2026), puis son complément d'erratum du 24 novembre 2026 (cinq citations obligatoires de plus, des marques de statut, des renvois corrigés).

**Périmètre.** Hors de ce que vise cette demande, aucune décision postérieure au 4 octobre 2026 n'est reportée ici ; un énoncé retiré ou remplacé depuis porte au plus une marque de statut, sans réécriture. Pour les revendications, la référence sera la table des revendications, version 2, qui reste à écrire. D'ici là, les décisions de `docs/decisions/` priment sur ce texte, et la table version 1 décrit l'état au 19 novembre 2026 sans faire foi.

---

## 0. Ce qui change depuis la v1

**Architecture.** Trois papiers au lieu d'un papier principal plus un papier dérivé : **A — le temps** (mono-agent), **C — l'instrument** (corruption et usurpation du moniteur), **B — l'essaim**. Le papier C, d'abord prévu comme dérivé conditionnel, est promu papier à part entière : la revue d'antériorité lui attribue les deux meilleurs scores d'originalité du programme, il est léger en calcul, il réutilise P3, et il ne dépend pas du succès de A.

**Décisions de fond (14 septembre 2026).**
1. Sondes à agrégation **max ou attention** sur les tokens, jamais moyenne ni médiane : ces dernières sont évadables par apprentissage par renforcement sur les poids, max et attention résistent.
2. Ancienne colonne vertébrale théorique, gardée pour mémoire : **lemme d'additivité interne + théorème négatif** (dommage porté par la marginale des scores contre dommage porté par leur corrélation) — le même objet mathématique dans le temps (A) et entre agents (B). *(Retirée comme colonne vertébrale par la version 3 : voir section 3.)*
3. **Plan 2 × 2 accès × agrégation** pour la porte G1 : {boîte noire, boîte blanche} × {par action, séquentiel}, pour ne pas confondre le gain de l'accès interne avec celui de l'accumulation.
4. Reformulations imposées par les revues : H2 (l'application aux sondes ; le séquentiel boîte noire existe déjà), H3 (la domination de la courbe boîte blanche), H4 (seul le compromis diversification/coordination survit), H8 (prédire la robustesse par la validité), HC2 (robustesse sous attaque par contenu boîte noire ; l'immunité absolue est réfutée).
5. Ajouts : test de **transposition token → action** de la robustesse d'agrégation ; **invariants de protocole** (section 9) ; riposte = **quatre politiques + deux ablations** ; **usurpation stylistique** comme famille d'attaque nommée, avec sa prédiction propre.

**Défauts appliqués faute de contre-ordre.**
- D-a : A et C en parallèle, B ensuite.
- D-b (défaut de la version 2, caduc : le lemme n'est plus revendiqué comme théorème ; il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée, section 3) : lemme tenté seul ; la question d'un co-auteur en analyse séquentielle est revisitée à G1.
- D-c : G1 en critère disjonctif — rappel à 1 % de faux positifs supérieur avec intervalle de confiance à 95 %, **ou** + 5 points de F1.
- D-d : papier B visé NeurIPS 2027, repli ICLR 2028.
- D-e : environnement « curation de données » sous porte G3, non ouvert.

**Re-datation (4 octobre 2026).** La phase 0 prévue au 15 septembre n'a pas démarré et la date d'entrée en cohorte est incertaine. Le calendrier est désormais exprimé en mois relatifs depuis le lancement (**M0 = 5 octobre 2026**) et ne dépend plus de l'admission ; le budget de calcul de la bourse, s'il arrive, accélère les phases 2 et 3 sans changer leur ordre.

---

## 1. Positionnement

En une phrase : agrégation **séquentielle** (dans le temps et entre agents) de scores de **sondes internes** pour détecter les **menaces diffuses** en évaluation de contrôle, y compris quand l'attaquant est une **population d'agents à poids partagés** — et mesure de la **corruptibilité** des moniteurs eux-mêmes.

La question unique des trois papiers : **que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ?** — à la fragmentation dans le temps (A), à la corruption de l'instrument (C), à la fragmentation entre agents (B). C'est la question de validité de construit de P3, portée au contrôle.

---

## 2. Les trois papiers

| | **A — le temps** | **C — l'instrument** | **B — l'essaim** |
|---|---|---|---|
| Problématique | Le monitoring par action échoue par construction sur le sabotage diffus : chaque action est innocente prise isolément. | Le moniteur est une surface d'attaque : plutôt que passer sous le radar, l'attaquant le déplace. Quelles architectures résistent, et peut-on mesurer la corruptibilité avant déploiement ? | Les attaques distribuées battent les moniteurs par-instance, et le moniteur global est indéployable. L'accès interne rétablit-il l'avantage, et comment décroît-il avec le nombre d'agents ? |
| Thèse | Les lois de la dissimulation répartie (Ker 2007 et 2010 ; Avenhaus et Jaech 1981), déjà transposées au suivi des usages contre l'extraction (Khilar 2026), donnent un modèle nul du dommage qu'un saboteur diffus peut cacher. Le papier mesure, sur des scores de sondes d'agents qui sabotent, où ce nul tient et quels termes s'y ajoutent ; puis ce que l'accès interne rattrape et qu'une seconde boîte noire ne rattrape pas. | La corruptibilité est un gain mesurable ; les juges génératifs ont g > 0, structuré par famille d'attaque ; les sondes à agrégation robuste ont g ≤ 0 sous attaque par contenu ; fermer le canal rhétorique impose une taxe chiffrée ; le g bénin prédit la robustesse. | Des copies partagent leurs poids, donc leurs signatures internes co-varient : une statistique spatio-temporelle rend l'essaim plus détectable que l'agent isolé ; se décorréler coûte à l'attaquant de la capacité de coordination. |
| Figure-titre | Plan 2 × 2 accès × agrégation ; rappel en fonction de l'horizon. | g par moniteur et par famille d'attaque ; taxe de déplacement. | Sécurité en fonction de N, boîte blanche contre boîte noire. |
| Hypothèses | H1, H2, Bi, Q, H6 (retirée des hypothèses revendiquées par la décision N-077 ; mesure descriptive gardée), Tr, H8 ; L revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée (énoncé central cité, non revendiqué) ; T mentionné, non revendiqué | HC1 à HC6 (dont HC2b) | H3, H4′, H5, H7 |
| Calendrier | M1–M2 ; papier vers M3 | M1–M3 ; papier vers M4 | M3–M6 ; papier en M7 |

---

## 3. Thèse centrale : loi héritée comme modèle nul, bilan mesuré, complémentarité

**Thèse (papier A, retenue le 22 novembre 2026).** Celle de la section 2.

**Modèle nul.** Pour des pas indépendants et une référence honnête de m pas, comptés dans la même unité que les n pas surveillés, le dommage caché est d'ordre √(n + n²/m) ; il n'est linéaire qu'à référence bornée ou fautive (Ker 2010). Forme à ajuster : budget caché au carré ≈ z²·(σ²·n^(2H) + σ²·n²/m + τ²·n²). L'écart au nul est le résultat.

**Second axe.** La complémentarité avec une seconde boîte noire, à taux total de fausses alertes égal (H1).

**Citations obligatoires de la thèse.** Ker 2007 ; Ker 2010 ; Avenhaus et Jaech 1981 ; Khilar 2026 (arXiv 2610.13083) ; ajoutées le 24 novembre 2026, avec les pages lues sur PDF : Ker 2006 (p. 7 : énoncé central du lemme d'additivité) ; Filler, Ker et Fridrich 2009 (p. 3-4 : hypothèses ; p. 5 : théorème 1, loi en racine pour une couverture markovienne) ; Arias-Castro, Bubeck et Lugosi 2012 (p. 2 : marginales identiques sous les deux hypothèses ; p. 14-15 : proposition 3.1, le carré de la somme en régime dense) ; Zhang et Gao 2026 (arXiv 2606.10456, version 2 ; p. 3 : proposition 1 ; p. 7 : tableau 2 ; p. 8 : traces réelles ; pages 1 à 9 lues sur 11) ; Parrack, Attubato et Heimersheim 2025 (arXiv 2507.12691, version 3 ; p. 1-2 et 5-6 : gain d'un moniteur de sorties qui reçoit les scores de sondes ; p. 7-8 : indice contraire, portes dérobées dans le code ; 13 pages lues sur 39).

**Statut de ce qui suit.** L'additivité interne, le lemme et le théorème ne sont plus des résultats ; l'additivité interne et le théorème restent mentionnés, chacun à son statut ; le lemme reste cité pour son énoncé central, et il est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée, comme prévision à éprouver, non comme résultat.

**Additivité interne (idée de départ, mentionnée, non revendiquée).** La fragmentation détruit la preuve *externe* par action : chaque sortie est défendable isolément. Si l'intention laisse une trace interne à chaque contribution, la preuve *interne* s'additionne — le long du temps pour un agent, entre agents pour un essaim.

**Lemme d'additivité (énoncé central cité, non revendiqué ; application au contrôle de l'intelligence artificielle revendiquée sous la forme mesurée, décision du 24 novembre 2026, GO-2026-11-24-18).** Énoncé central, occupé hors du contrôle de l'intelligence artificielle et non revendiqué : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981, p. 25 et 30-31 ; Ker 2006, p. 7). Application revendiquée, sans théorème, comme prévision à éprouver par la mesure. Chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde se conserve : il ne dépend pas, en moyenne sur les épisodes, du nombre d'actions entre lesquelles le sabotage est réparti. Ce déplacement est la somme des scores sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête. Si cette conservation tient, et si la dispersion de ce déplacement ne dépend pas non plus de la fragmentation, l'énoncé central cité s'applique aux sondes : à taille fixe, et sous approximation normale, la puissance de la somme lue en fin d'épisode ne dépend pas de la répartition. La conservation est dite tenue si l'intervalle de confiance à 95 % de l'écart de déplacement entre niveaux de fragmentation tient tout entier dans plus ou moins la marge ; réfutée s'il en sort tout entier, vers le haut ou vers le bas ; indéterminée sinon. La marge est relative au déplacement du niveau le moins fragmenté. Si elle est réfutée, le sens de l'écart est le résultat. L'énoncé n'est dit tenu que s'il tient dans les deux modes d'induction du sabotage, consigne cachée et adaptateur (familles (i) et (ii) de la section 7) ; sinon le verdict se rapporte par mode. Raison, supposée selon la décision N-077 : une mesure faite sur nos organismes peut lire leur fabrication. Le préenregistrement fixe la marge, la statistique d'écart (pente, ou plus grand écart entre niveaux), la correction pour plusieurs sondes et familles, la règle qui dit où l'énoncé tient, l'emploi du témoin, la lecture du rappel et le calcul de puissance. Un dommage inégal entre niveaux s'ajuste (déplacement par unité de dommage, si la proportionnalité tient) ou se déclare. Hypothèses : (1) le sabotage déplace la position des scores et ce déplacement croît avec le dommage (s'il est nul à tous les niveaux, l'énoncé est sans objet et la question Q décide) ; (2) le dommage, celui de l'épisode entier, est chiffré et constaté hors des scores ; (3) à tous les niveaux de fragmentation, n, la tâche et la sonde, gelée avant la mesure, sont les mêmes, et la référence honnête est déclarée (taille m, dans l'unité de n) ; (4) la somme est lue en fin d'épisode, et rien n'est dit d'un franchissement séquentiel ; (5) le montage fixe la fragmentation, souvent par la consigne, sur les organismes tels qu'ils sont construits, et rien n'est affirmé d'un saboteur qui choisit sa répartition ni d'un saboteur réel. Témoin : un organisme qui reçoit la consigne de fragmentation et n'exécute aucun sabotage ; son déplacement, par niveau, dit ce que la sonde lit de la consigne seule. Mesuré par sonde, par mode d'induction et par niveau de fragmentation (le nombre d'actions qui portent le sabotage) : le déplacement cumulé et sa dispersion ; le rappel d'une alarme sur la somme, à taux de fausses alertes déclaré, qui lit le corollaire sur la puissance ; à côté, le maximum par action et la part du déplacement portée par les actions de sabotage. Unité d'observation : l'épisode entier, apparié à son jumeau honnête sur la même tâche ; l'incertitude se calcule par tâche. Ne pas écrire : la conservation chez un saboteur réel ; une conservation lue sur le seul organisme à consigne cachée, présentée comme une propriété des sondes. Voisins à citer : bornes en divergence totale, en boîte noire (Tailor 2025, arXiv 2510.04303, p. 12 ; Ghanem 2026, arXiv 2608.02698, p. 5) ; et le voisin le plus proche, en boîte noire, Makins et al. 2026 (arXiv 2607.07368, version 2 ; p. 1 : le maximum du soupçon baisse quand l'attaque se répartit entre plus d'agents ; p. 8 : un moniteur qui lit toutes les livraisons réunies donne un soupçon à peu près plat selon le nombre d'agents ; p. 9 : le volume de sabotage reste à peu près constant). C'est l'analogue en boîte noire de la conservation ; la somme des scores n'y est pas testée, selon notre lecture. Antériorité de cette forme non établie : aucune phrase de nouveauté. Entre agents, rien n'est revendiqué ici ; la prévision de H3 sur la somme globale garde son statut. Ancienne lettre, pour mémoire :
Hypothèses de l'ancienne lettre, non revendiquées : (a) chaque action de sabotage déplace l'espérance du score de sonde d'au moins δ > 0 — le dommage passe par la **marginale** ; (b) le budget total de sabotage B = Σδ est borné et le dommage cumulé est une fonction croissante de B ; (c) la variance des scores honnêtes est estimable sur épisodes honnêtes.
Ancien énoncé, non revendiqué : la puissance ne dépendrait que de B et de la variance. Établi et cité : à taille fixe, la puissance de la somme ne dépend pas de la répartition. Pour un processus e, question ouverte, **sous simulation** (inégalité d'étalement dérivée à la main, non simulée ; scellement provisoire) : l'étalement est-il le cas le moins favorable au défenseur ? Une simulation à budget égal (sabotage tôt, tard, étalé) la tranche avant toute phrase.

Deux précautions, pour l'ancienne lettre :
- la notion de puissance n'est pas la même sous garantie toujours valide et au sens du test séquentiel de Wald (Koning & Grünwald, arXiv 2208.07610) ;
- un adversaire couvert qui connaît la contrainte de faux positifs peut imposer un délai de détection d'ordre Θ(γ) si l'on ne contraint que la furtivité *par action* (arXiv 2601.20022) — d'où l'hypothèse (b), qui borne le budget *total*.

**Théorème négatif (mentionné, non revendiqué ; papiers A et B).** La lettre de la version 2 (« toute statistique fondée sur les marginales a une puissance égale au taux de faux positifs ») est inexacte. N-003 l'a bornée : vraie quand l'attaque préserve le multi-ensemble des scores, pour les statistiques symétriques ; fausse quand elle ne préserve que les marginales par coordonnée. Arias-Castro, Bubeck et Lugosi 2012 la contredisent : le carré de la somme garde de la puissance en régime dense. Énoncé exact, élémentaire et cité : à marginales préservées, l'espérance des statistiques additives est inchangée ; le test efficace est du second ordre (autocovariance dans le temps, co-élévation entre agents). L'unité du temps et de l'espace est héritée (Avenhaus et Jaech 1981) ; l'indexation agnostique (section 4) est une commodité de rédaction citée, non un apport.

**Hypothèse empirique pivot.** Question Q : sur des organismes réalistes, le sabotage déplace-t-il la position des scores (l'ancienne condition δ > 0), leur dépendance, ou les deux ? Elle se lit par un test de position et un test de dépendance, étalonnés sur des substituts par permutation des pas. Aucune issue n'est dite publiable avant le calcul de puissance du plan ; une issue indéterminée est possible.

**Antériorité à vérifier en priorité.** Zhang et Gao 2026 (arXiv 2606.10456) occupent le contraste en boîte noire, sur scores synthétiques puis sur traces réelles où l'attaque est fabriquée sur les scores. Réserve : limite à longueur finie, notre lecture, à vérifier en rejouant leur tableau 2. Aucune différenciation n'est revendiquée. Question : que déplacent, sur des scores de sondes, des attaques jouées par de vrais agents ?

---

## 4. Cadre formel

**Jeu de contrôle** G = (E, π_B, π_R). L'environnement E produit des épisodes ; les actions a_{i,t} sont indexées par agent i ∈ {1…N} et pas t ∈ {1…T}. L'équipe rouge choisit une politique π_R sous budget de sabotage B, visant un dommage cumulé ≥ θ. L'équipe bleue observe des caractéristiques φ(a_{i,t}) incluant les activations internes h_ℓ, calcule un score par action s(a), et dispose d'agrégateurs A_temps (somme cumulée, processus e), A_pop (co-élévation), A_spatio-temporel (les deux), d'un budget d'audit b et d'interventions d'intensité λ.

- **Sécurité** = inf sur π_R de P(alerte avant que le dommage cumulé n'atteigne θ).
- **Utilité** = performance sur la tâche honnête sous π_B.
- **Indexation agnostique** : tout agrégateur opère sur le multi-ensemble {(i, t)} ; N = 1 et N = k sont le même objet mathématique.

**Corruption (papier C).** Verdict du moniteur v ∈ [0, 1], ordinal ou continu ; v₀ = verdict sans attaque ; v* = verdict voulu par l'attaquant. Loi de déférence : Δv = g · (v* − v₀), g estimé par régression sur plusieurs intensités de pression, avec un nul de régression vers la moyenne comme dans P3.
Convention : g = fraction du chemin parcourue vers le verdict voulu par l'attaquant.
- g ≈ 0 : robustesse.
- g < 0 : auto-incrimination — plaider incrimine.
- g > 0 sans accès aux poids : contamination de construit — le moniteur lit le registre, pas l'intention.

Comme la sycophancie dans P3 : la corruptibilité est un gain, pas une chose.

---

## 5. Hypothèses

Probabilités d'originalité calibrées au 14 septembre 2026, à reconfirmer par la vérification sur sources primaires (brief de phase 0, tâche T0.2).

### Papier A — le temps
- **H1 — gain blanc-sur-noir** (0,55). À agrégation égale et à taux de faux positifs égal, un moniteur fondé sur les activations détecte plus de sabotage diffus sur tâches floues qu'un moniteur boîte noire. Revendicable : la mesure spécifique diffus/flou ; le gain blanc-sur-noir en général est établi (parent à citer avec son indice contraire : Parrack, Attubato et Heimersheim 2025). Complément, second axe de la thèse : à taux total de fausses alertes égal, l'union « meilleure boîte noire et sonde » rattrape plus de sabotages diffus que l'union « meilleure boîte noire et seconde boîte noire d'une autre lignée ».
- **H2 — accumulation séquentielle sur sondes** (0,50). L'accumulation séquentielle toujours valide de scores de sondes détecte des sabotages dont chaque action reste sous le seuil ; à déplacement par acte fixé, le rappel suit le modèle nul hérité en n et m ; la garantie vaut sous une référence honnête de taille m déclarée, pour n au plus m (application du corollaire 1 de Ker 2010) ; l'écart au nul est le résultat. Le squelette séquentiel boîte noire existe.
- **L — lemme d'additivité** (revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; énoncé central cité, non revendiqué ; la note 0,75 est caduque ; application non calibrée). Section 3.
- **T — théorème négatif** (mentionné, non revendiqué ; lettre inexacte, bornée par N-003). Section 3.
- **Bi — bilan mesuré contre le modèle nul** (chance d'un contenu propre : 0,5, jugement). Section 3.
- **Q — position ou dépendance** (question ; non calibrée). Section 3.
- **H6 — marge asymétrique** (retirée des hypothèses revendiquées du papier A par la décision N-077 du 21 novembre 2026 ; mesure descriptive gardée ; la note 0,66 est caduque). Énoncé de la version 2, pour mémoire : Il existe une intensité d'intervention non spécifique (paraphrase, ré-échantillonnage, remise à zéro de contexte, bruit d'activations) où le succès d'attaque chute significativement plus vite que l'utilité honnête.
- **Tr — transposition token → action** (angle mort identifié, non calibré). La robustesse des agrégations max et attention, établie au niveau token, tient-elle au niveau action et trajectoire sous accumulation séquentielle, face à un attaquant adaptatif ?
- **H8 — la validité prédit la robustesse** (0,40). Le construit réellement mesuré par une sonde (intention contre conscience d'évaluation) prédit sa robustesse adverse. Le glissement de construit sous pression est déjà décrit ; la prédiction ne l'est pas.

### Papier C — l'instrument
- **HC1 — loi de déférence** (0,75). Δv = g · (v* − v₀), g stable par moniteur génératif, structuré par famille d'attaque.
- **HC2 — robustesse des sondes** (0,65 ; 0,15 dans la version « immunité absolue », abandonnée). Sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste.
- **HC2b — auto-incrimination** (0,70). Tenter de manipuler augmente le score de sonde. Contrôle obligatoire du style : les sondes captent souvent des corrélats de surface.
- **HC3 — usurpation** (0,55, l'originalité est portée par le versant stylistique). Les ordres en bande déplacent les juges génératifs mais déclenchent une détection quasi certaine sous le protocole « contenu = données » ; l'usurpation stylistique de l'instructeur garde un g résiduel positif sur les juges, nul sur les sondes.
- **HC4 — taxe de déplacement** (0,85). Obtenir sur une sonde le déplacement que la rhétorique obtient gratuitement sur un juge exige l'obfuscation d'activations, pour un coût supérieur de plusieurs ordres de grandeur (accès, requêtes, calcul, taux de succès).
- **HC5 — contre-mesures** (0,60). Paraphrase de confiance et quorum hétérogène, mesurés par une matrice de transfert des attaques de corruption.
- **HC6 — le g bénin prédit la robustesse** (0,80). Le g mesuré sur des corpus de pression bénins prédit l'effondrement sous attaque optimisée : critère de recette d'un moniteur avant déploiement.

### Papier B — l'essaim
- **H3 — courbe sécurité(N)** (0,45). À budget et nombre total d'actions fixés, **sous simulation** (somme plate dérivée à la main, non simulée ; scellement provisoire), la somme globale est prédite plate en N et le maximum décroissant (Avenhaus et Jaech 1981) ; la sonde change la constante, non la pente : prévision, non constat. Les courbes boîte noire sont publiées.
- **H4′ — compromis diversification/coordination** (la H4 d'origine est occupée, 0,30 ; seule cette partie reste revendicable). Diversifier les agents (personas, réglages fins) décorrèle leurs signatures internes mais réduit leur capacité de coordination ; le compromis est chiffrable.
- **H5 — nombre × diversité des moniteurs** (0,70). La sécurité croît avec le nombre M de moniteurs seulement via la diversité effective, mesurée par une matrice de transfert d'attaque sur un panel de sondes.
- **H7 — riposte et fuite** (0,68). La pente d'adaptation de l'équipe rouge dépend de la politique de riposte et est prédite par la fuite d'information (information mutuelle entre l'état de détection et les observations de l'équipe rouge).

---

## 6. Environnements

Critère directeur : **flou à la relecture, vérifiable en aval** (vérité terrain différée).

- **(a) Propositions d'expériences — papier A, phases 0 à 2.** Des agents rédigent et révisent des propositions d'expériences d'apprentissage automatique, notées par un évaluateur faible de confiance sur rubrique structurée. Sabotage diffus : biais systématique subtil (orienter vers des directions stériles, affaiblir les contrôles, gonfler les choix coûteux), réparti sur de nombreuses propositions. Vérité terrain : cibles semées préenregistrées + vérification différée sur sous-échantillon. Base : le jeu de Terekhov et al. (arXiv 2606.08892), porté en 8 milliards de paramètres. Exigence : décomposable en contributions (i, t) qui resservent telles quelles quand N = k.
- **(b) Pipeline de code multi-rôles — papier B, phase 3.** Codeur, testeur, relecteur ; portes dérobées fragmentées sur plusieurs commits, chaque diff restant innocent. Bases : FakeLab (Makins et al., sur demande aux auteurs) ou Iterative VibeCoding (Hills et al., cadre ControlArena, état persistant), portés en poids ouverts.
- **(d) Curation de données — extension sous porte G3.** Empoisonnement diffus par des exemples individuellement plausibles ; vérité différée = comportement d'un modèle aval entraîné sur les données curées. Ne s'ouvre que si un proxy de vérité différée fiable et bon marché est validé.
- **Transfert concentré.** En fin de phase 1, le moniteur séquentiel est testé sur un cadre de sabotage concentré (ControlArena) — une figure de robustesse, pas un chantier.

---

## 7. Organismes modèles

- **(i) Instruction cachée** dans le message système.
- **(ii) Réglage fin léger (LoRA)** inculquant la politique de sabotage sans aucune instruction à l'inférence (par distillation de contexte depuis la famille (i)).
- **(iii) Organismes publics de l'institut britannique de sécurité de l'IA** (sandbagging, dont un imitant Llama-3.1-8B-Instruct, verrouillés par mot de passe), si la licence le permet — gain de temps et comparabilité.

**Prédiction de validité.** Une sonde qui lit en réalité « j'ai une instruction cachée » réussit sur (i) et échoue sur (ii) ; une sonde d'intention réussit sur les deux.
**Contrôles croisés.** Organisme honnête averti de la surveillance (aucune mission) ; saboteur en régime simulé « non observé » — pour dissocier conscience d'évaluation et intention (alimente H8).
**Anti-circularité.** Une sonde n'est jamais entraînée et évaluée sur les mêmes organismes : entraînement sur données génériques (recettes publiées) ou sur une famille, évaluation sur une autre.

---

## 8. Moniteurs

**8.1 Sondes.** Agrégation sur les tokens : max ou attention uniquement. Familles : linéaire, différence de moyennes, petit perceptron, sonde à attention, Mahalanobis (non supervisée). Concepts : tromperie, enjeux élevés, dissimulation, conscience d'évaluation, auto-préservation. Plancher obligatoire : sonde aléatoire appariée en covariance (style P3) — une sonde qui ne le bat pas n'existe pas. Réserve de détecteurs jamais déployés, donc jamais fuités, sortis pour audit seulement.

**8.2 Diversité (H5).** Six axes : graines et données ; où lire (couches précoce, médiane, tardive ; positions ; flux résiduel contre sorties de blocs ; autoencodeurs parcimonieux Llama Scope) ; familles de sondes ; concepts et distributions de négatifs ; fenêtres d'agrégation ; hétérogénéité de type (moniteurs génératifs, détecteurs heuristiques natifs de l'environnement).
Mesure : **matrice de transfert d'attaque** — une attaque optimisée contre A réussit-elle contre B ? — et non la décorrélation des erreurs bénignes. La revue montre que choisir sur la seule décorrélation perd contre le hasard : la compétence individuelle compte. Si la diversité naturelle est insuffisante : apprentissage à corrélation négative, diversification des vulnérabilités.

**8.3 Bases boîte noire.**
- Papier A : moniteur faible par action ; TRACE-lite (triage–inspection–jugement, réimplémenté) ; accumulation séquentielle sur scores boîte noire (dans l'esprit d'E-valuator).
- Papier B : moniteur à état « link-tracker » et ensemble à quatre moniteurs (Hills et al.) ; monitoring à état sur flotte (Brown et al.).
- Papier C : deux ou trois juges génératifs hétérogènes.

**Décision D1 — modèle du moniteur boîte noire** (proposer avec recommandation).
- Enjeu : la propreté de la comparaison blanc/noir (H1) contre le réalisme du contrôle (un moniteur de confiance est plus faible que l'agent).
- (a) Même modèle que l'agent, en juge : capacité égale, isole l'effet de l'accès / irréaliste comme moniteur de confiance.
- (b) Modèle plus faible de confiance (par exemple Llama-3.2-3B-Instruct) : réaliste / confond capacité et accès.
- (c) Qwen2.5-7B : hétérogénéité / ajoute une variable de famille de modèles.
- Recommandation : (a) + (b) — les moniteurs coûtent peu face à la génération des trajectoires ; (a) pour H1, (b) pour la courbe sécurité-utilité. Confiance moyenne. **Défaut : (a) + (b).**

---

## 9. Invariants de protocole (toujours actifs)

- **Canal opérateur authentifié** : les ordres de l'opérateur n'arrivent que par un canal vérifié par le harnais, jamais par le jugement du modèle.
- **Contenu en bande = données** : tout ce qui arrive dans le contenu de la tâche est une donnée, jamais un ordre ; un contenu « en forme d'ordre » dans le canal données est en soi une alarme.
- **Flux unidirectionnel agent → moniteur** : pas de dialogue, pas de boucle de persuasion.
- **Moniteurs amnésiques** entre épisodes : pas de mémoire, pas de relation à cultiver.
- **Seuils stochastiques** (probabilité d'audit lisse et croissante du score, jamais de seuil fixe apprenable) et **trafic de couverture** — actifs par défaut, ablatés dans E3.4.
- **Hygiène de l'état persistant** : remises à zéro et filtrage — une adaptation sans hérédité n'est pas une évolution.
- **Asymétrie d'apprentissage** : chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes.

**Frontière assumée.** Si l'adversaire possède l'infrastructure (clés, harnais, journaux), les hypothèses du contrôle sont caduques : c'est la couche sœur (sécurité des poids et des infrastructures), hors périmètre.

---

## 10. Plan expérimental

### Phase 0 — instruments (M0 : 5 octobre → 1er novembre 2026)
Détail opérationnel dans le brief de phase 0. Tâches : socle et gouvernance ; vérification de l'état de l'art sur sources primaires ; simulation du lemme et du théorème négatif (tâche de la version 2, nom gardé ; les deux énoncés ne sont plus revendiqués comme théorèmes ; le lemme est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée ; section 3) ; harnais et journalisation des activations ; environnement (a) v0 ; organismes v0 ; sondes v0 ; bases boîte noire v0 ; conception et préenregistrement du papier C.
**Porte G0 (prêt pour G1)** : harnais validé ; organismes avec dose-réponse ; sondes au-dessus du plancher ; base boîte noire opérationnelle ; agrégateurs validés en simulation ; préenregistrements de G1 et du papier C scellés et contre-lus ; état de l'art vérifié.

### Phase 1 — papier A (M1–M2)
- **E1.1** Organismes finalisés et calibration dose-réponse du budget de sabotage.
- **E1.2** Plan 2 × 2 accès × agrégation. Métriques : AUROC, rappel à 1 % de faux positifs, courbe sécurité-utilité à budget d'audit, latence (alerte contre dommage cumulé). Effet principal de l'accès = H1 ; effet principal du séquentiel = H2 ; interaction positive = signature de l'additivité interne, idée de départ mentionnée et non revendiquée (la preuve externe par action est quasi nulle, l'interne ne l'est pas).
- **E1.3** Bilan sur données réelles : essai « jumeau contre jumeau », surface du seuil d'alarme honnête en n et m ajustée au modèle nul, après calcul de puissance ; simulation du franchissement séquentiel ; test de la condition δ > 0.
- **E1.4** Théorème négatif (mentionné, non revendiqué : section 3) en semi-synthétique, lu comme diagnostic de la question Q : scores honnêtes réels + structure de corrélation injectée à marginale préservée.
- **E1.5** Attaques adaptatives : (a) par contenu (consigne de rester sous le seuil, persona) ; (b) pondérales (réglage fin, puis apprentissage par renforcement au niveau action, sous GO) — test Tr.
- **E1.6** Marge asymétrique (H6) ; depuis la décision N-077 : mesure descriptive, sans hypothèse revendiquée. Base : Ctrl-Z, à compléter selon N-077 (section 3, point 3).
- **E1.7** Transfert concentré (ControlArena).
- **Porte G1 (fin M2)** : boîte blanche séquentielle contre meilleure boîte noire (TRACE-lite ou séquentiel boîte noire), critère disjonctif D-c. Échec → (conséquence de la version 2, remplacée par la décision N-062 : l'échec commande la reconception des sondes ; H8 reste un diagnostic ; la bascule reste une issue possible, à la main de Lazar seulement) résultat négatif publié + bascule H8 dominante.
- Livrable : papier A (arXiv + atelier), vers M3.

### Piste C — papier C (M1–M3, en parallèle de la phase 1)
- **EC.1** g des juges génératifs : cinq familles d'attaque (flatterie et supplication ; revendication d'autorité ; approbations forgées ; usurpation stylistique de l'instructeur ; ordres en bande) × plusieurs intensités ; verdicts ordinaux ou continus, lus sur texte complet.
- **EC.2** Sondes sous les mêmes attaques, plan 2 × 2 rhétorique × intention (agent honnête qui plaide sincèrement contre saboteur qui tient le même plaidoyer) : signe de g_sonde (HC2, HC2b).
- **EC.3** Usurpation : ordres en bande sous protocole « contenu = données » contre usurpation stylistique (HC3).
- **EC.4** Taxe de déplacement, côté obfuscation par réutilisation des codes d'obfuscation d'activations publiés, portés sur 8B (HC4).
- **EC.5** Contre-mesures : paraphrase de confiance, quorum hétérogène, matrice de transfert des attaques de corruption (HC5).
- **EC.6** g bénin contre robustesse sous attaque optimisée (HC6).
- **Leçons de P3 appliquées** : jamais de fenêtre tronquée pour lire un verdict (dans P3, la troncature a fabriqué un faux effet en lisant des verdicts retardés comme des verdicts changés) ; instruments ordinaux ou continus plutôt que catégoriels (le catégoriel était plat là où l'ordinal tranchait) ; nul de régression vers la moyenne dans l'estimation de g ; score continu par probabilité du jeton de verdict quand c'est possible.
- **Porte GC (fin M2)** : si g_sonde > 0 sans accès aux poids → le papier change de titre (contamination de construit), il ne disparaît pas ; si la collision arXiv 2607.08066 couvre déjà la loi de déférence → recentrage sur HC4 et HC6.
- Livrable : papier C (arXiv + atelier, puis conférence courte), vers M4.

### Phase 2 — papier B (M3–M4)
- **E2.1** Division du travail rouge, avec et sans planificateur (réplication de l'effet de fragmentation, vue interne).
- **E2.2** Collusion par canaux explicites contre coordination par poids partagés ; défenses-ingrédients : paraphrase, brouillage des canaux.
- **E2.3** Statistiques inter-agents ; les agrégateurs de NARCBench (alignement d'activations, pic de suspicion) sont assumés comme base, pas comme concurrents.
- **Porte G2 (fin M4)** : effet de fragmentation répliqué et statistique de population supérieure à l'agrégation par agent. Sinon : recentrage sur le temporel N = 1.

### Phase 3 — papier B (M4,5–M6)
- **E3.1** Statistique spatio-temporelle contre séquentiel par agent seul et contre coupe transversale (position NARCBench) — base obligatoire : la somme globale ; gain revendiqué sur les seuls sabotages qui déplacent la dépendance.
- **E3.2** Diversification adverse → compromis décorrélation/coordination (H4′) ; transfert des sondes entre variantes ; Qwen2.5-7B comme agent hétérogène.
- **E3.3** Figure M × diversité + matrice de transfert d'attaque (H5).
- **E3.4** Riposte : quatre politiques (visible immédiate, différée randomisée, silence-puis-frappe, pot de miel) comparées par pente de sélection et fuite mesurée ; deux ablations (seuil stochastique contre fixe ; trafic de couverture contre sans) (H7).
- Bases à battre : link-tracker, ensemble à quatre moniteurs, monitoring à état sur flotte.
- **Porte G3** : ouverture de l'environnement (d) seulement si un proxy de vérité différée est validé.
- Livrable : papier B, rédaction en M7.

---

## 11. Validité de construit (transversale)

À chaque phase : panel contrastif de sondes (intention de saboter, dissimulation, conscience d'évaluation, enjeux élevés) et contrôles croisés de la section 7. Prédiction centrale (H8) : ce que mesure vraiment la sonde prédit sa robustesse adverse — une sonde de conscience d'évaluation s'effondre quand l'attaquant apprend à paraître détendu ; une sonde d'intention résiste mieux. Continuité directe avec P3 : contrôles appariés en covariance et en énergie comme plancher, et « mesurer ce que mesure la mesure » comme signature du programme.

---

## 12. Méthode (héritée de P3)

Préenregistrement scellé (SHA-256) avant toute expérience décisive ; contre-lecture par une instance qui ne l'a pas écrit ; aucun run visant un signe positif ; traitement symétrique des résultats suspects de propreté, listes d'arrêt obligatoires ; toute garde d'arrêt testée sur un cas sain et sur un artefact, aucun repli silencieux ; tout chiffre traçable (chemin de fichier + empreinte) ; la provenance par transcription n'est pas opposable — y compris les chiffres des revues d'antériorité ; discipline anti-faux-gap : un interstice est une question, et la limitation d'un papier n'est pas un trou du champ sans recherche affirmative.

---

## 13. Critères de succès et bascules pré-engagées

**Succès.** (1) Bilan mesuré contre le modèle nul hérité et complémentarité à taux total de fausses alertes égal, sur activations réelles, avec le plan 2 × 2 (A) ; (2) loi de déférence et taxe de déplacement (C) ; (3) courbe sécurité(N) et compromis diversification/coordination (B) ; (4) un verdict de validité de construit valable même si H1 échoue.

**Bascules.**
- G1 échoue → (conséquence de la version 2, remplacée par la décision N-062 : l'échec commande la reconception des sondes ; H8 reste un diagnostic ; la bascule reste une issue possible, à la main de Lazar seulement) résultat négatif publié + H8 dominante.
- Publication externe du cœur séquentiel sur sondes (équipe Oxford/NYU de NARCBench, équipe boîte blanche de l'institut britannique) → bascule vers l'épidémiologie de population et la curation de données.
- g_sonde > 0 → papier C sur la contamination de construit.
- 8B trop faible sur l'environnement (a) → rubrique simplifiée (changement de modèle seulement sur GO).
- Élicitation rouge insuffisante → import des politiques d'attaque publiées.
- Pas de proxy de vérité différée → environnement (d) abandonné sans coût.

---

## 14. Ressources et calendrier

**Modèles** : Llama-3.1-8B-Instruct (agents, sondes), Qwen2.5-7B (hétérogénéité, transfert), un moniteur de confiance plus faible (décision D1).
**Outils** : TransformerLens, harnais maison, ControlArena en réutilisation.
**Calcul** : Vast.ai, aucune dépense sans GO sur devis ; budget de la bourse s'il arrive.

| Période | Contenu |
|---|---|
| M0 (5 oct. → 1er nov. 2026) | Phase 0, porte G0 |
| M1–M2 | Phase 1 (A) en parallèle de la piste C (EC.1 à EC.3) ; G1 et GC en fin de M2 |
| M3 | Rédaction de A ; piste C (EC.4 à EC.6) ; début de la phase 2 |
| M3–M4 | Phase 2 (B), G2 ; rédaction de C (vers M4) |
| M4,5–M6 | Phase 3 (B), G3 |
| M7 | Rédaction de B → NeurIPS 2027 (repli ICLR 2028) ; libération du code, des organismes et des sondes |

---

## 15. Questions ouvertes

- Co-auteur en analyse séquentielle : sans objet pour le lemme, qui est revendiqué dans sa seule application au contrôle de l'intelligence artificielle, sous la forme mesurée et sans théorème (section 3) ; la question ne se reposerait que pour un théorème neuf sur l'étalement en séquentiel, non décidé (revisité à G1).
- Dualité défensive du poids partagé : une copie prise en flagrant délit = toute la flotte corrigée d'un coup ; quantifiable comme valeur d'un flagrant délit ?
- Budget de fuite formalisé (borner l'information mutuelle de la politique de riposte) — antériorité à vérifier avant revendication.
- Jeu complet N attaquants × M défenseurs.
- Universalité des signatures entre familles de modèles (prudence : la forme mesurée dans P3 n'a pas transféré de Llama à Qwen).
- Déployabilité : l'argument vaut pour les laboratoires, qui ont un accès interne natif à leurs agents ; limite assumée pour les agents tiers.

---

## 16. Veille active

Hebdomadaire, rapportée seulement si elle change une revendication : suites de NARCBench (l'équipe a annoncé les tests toujours valides comme prochaine étape), équipe boîte blanche de l'institut britannique, versions de ControlArena, blog de Redwood Research, blog d'alignement d'Anthropic, et toute suite de arXiv 2607.08066 et 2606.10456.
