# Cellule B — Tour III.2 : Critique croisée de méthode

---

## Sur la proposition A

### (a) Défauts de méthode

**1. L'option F (bras placebo « rareté seule ») confond le test de fuite avec la structure du monde.**

A propose un bras placebo qui choisit les 12 paires dont l'étiquette retenue est la plus rare, sans lire κ, et compare sa précision à celle de c (tirage uniforme). Le défaut : dans le monde scellé, la rareté de l'étiquette retenue est *corrélée* au statut du pont par construction (jumeau j{t} à fréquence 2 pour vrai d'opérateur, homonyme de surface à 7,17 pour surface — pièce 2, section 1.2, VÉRIFIÉ). Le bras « rareté seule » n'est donc pas un test de fuite de l'information conceptuelle ; c'est un test du mélange de deux signaux — la rareté du concept rare planté et la rareté de l'étiquette d'opérateur. Si F échoue (rareté ne bat pas c), on ne sait pas si c'est parce que la fuite n'existe pas ou parce que les statuts d'opérateur diluent le signal. Si F passe, on ne sait pas si c'est la fuite ou la structure plantée. Pour un test propre, il faudrait stratifier : F restreint aux paires dont l'étiquette retenue est un concept rare (pas un jumeau, pas un homonyme), et F restreint aux paires dont l'étiquette retenue est un opérateur. Le diagnostic (pièce 2, section 1.2, VÉRIFIÉ) donne les parts : en M_bien, 82 % des vrais conceptuels ont un concept rare comme étiquette retenue, mais seulement 32 % des vrais d'opérateur. Sans cette stratification, F est une moyenne pondérée qui ne tranche rien.

**2. Le duel N1 (B4) oppose deux hypothèses sur V5 scellée mais utilise la variante G3 avec λ = 0, explicitement exclue par S16a.**

A propose de calibrer V5 sur des mondes G3 (λ = 0) pour mesurer le taux d'échec de V5 à lois égales. Problème : λ = 0 change le monde (plus de trace conceptuelle sur les ponts d'opérateur), donc les « lois égales » ne sont pas celles du monde réel de l'expérience. L'erreur type mesurée sur G3 n'est pas celle du monde scellé. Le diagnostic (pièce 2, section 1.3, VÉRIFIÉ) montre H4 = G3 + λ = 0 : écart 0,473 en M_bien, 0,920 en M_moyen. Le monde G3 sans λ = 0 donne 1,293 et 2,275. La calibration sur G3 λ = 0 mesure une variabilité dans un monde qui n'est pas celui de V1–V6. Pour que le duel soit informatif, la calibration devrait porter sur le générateur scellé restreint aux trois statuts à concept rare (où les lois sont effectivement « presque égales » à 0,07 près en M_bien, pièce 2, section 1.2, VÉRIFIÉ).

**3. Le calcul de puissance de N11(1) confond la puissance de l'expérience v3 (2 400 mondes, σ ≈ 11–15,3) avec celle d'un retrait de bras.**

A écrit : « l'expérience v3 fournit donc la puissance pour un retrait à 3 points sans monde supplémentaire ». Mais les 2 400 mondes mesurent Δ(N, b), Δ(N, N_β0), etc. — des contrastes entre un bras et ses témoins. Le classement de trois bras (méta, Gu-Krenn, basique) exige de comparer *les mêmes mondes sous les trois fonctions de score des bras*, ce qui n'est pas prévu dans la structure de l'expérience v2/v3 telle que décrite (pièce 3, conditions M_bien et M_moyen : un seul N, une seule architecture). Pour évaluer trois bras, il faut soit trois exécutions parallèles (N = bras basique, N = bras méta simulé, N = bras Gu-Krenn simulé) sur les mêmes mondes, soit un code qui simule les trois règles de sélection de paires — ce qui n'existe pas dans le code scellé (pièce 2, diagnostic : seules les variantes du *générateur* sont testées, pas les variantes du *bras*). La puissance revendiquée est celle d'un contraste qui n'est pas celui du retrait.

**4. Pour N11(2), la source « pont réel dont le proposeur ne reconnaît pas la source » n'est pas un contrôle d'aveugle.**

La vérification « titre et résumé soumis au proposeur, réponse connu/inconnu » suppose que le proposeur (un modèle de langage) répond honnêtement à « connaissez-vous cet article ? ». Un LLM n'a pas de mémoire d'entraînement interrogeable de cette façon ; sa réponse « inconnu » n'est pas informative (HYPOTHÈSE). Un pont publié en 2024 pourrait être dans les données d'entraînement d'un modèle mis à jour. Le seul contrôle fiable est la date de coupure *déclarée* du fournisseur — et A reconnaît lui-même que S7 (dates de coupure connues) est HYPOTHÈSE. L'aveugle repose donc sur une supposition non vérifiable.

### (b) Conditions de perte de puissance ou de non-jugeabilité

**N1, option F.** La puissance du bras placebo « rareté seule » contre c dépend de la proportion de paires dont l'étiquette retenue est rare (fréquence ≤ 3, illustratif) parmi les 12 paires. Si le repli est fréquent (part de repli 0,17–0,27 en M_bien, 0,34–0,50 en M_moyen, pièce 2, section 1.2, VÉRIFIÉ), beaucoup de paires ont une étiquette retenue à fréquence 10–17, et le bras « rareté seule » sélectionne en priorité les mêmes paires que d1c, non par concept mais par rareté de l'opérateur — la puissance pour détecter une fuite *conceptuelle* se dégrade.

**N11(3), concordance W de Kendall.** Avec trois bras, W de Kendall a au plus trois ordres possibles (3! = 6 permutations, W ∈ {0, 1/3, 2/3, 1} pour trois items). Le test de W ≥ 0,7 sur trois bras n'a qu'une seule réalisation qui satisfait la condition (accord complet, W = 1). La puissance pour distinguer « accord partiel » de « désaccord » est nulle : W = 2/3 (un seul renversement de paire) est rejeté par le seuil 0,7. Ce n'est pas un test de transport, c'est une vérification d'accord parfait, qui sera presque toujours fausse en présence de bruit.

**N6, DL-3 avec déclencheur d'audit.** A propose un déclencheur si le recouvrement en R2⁻ < 0,5 × recouvrement en R2. Mais la puissance en R2⁻ est structurellement plus basse (fond ajouté à 90 % des paires-années, pièce 15, DL-3, RAPPORTÉ). Un déclencheur calibré sur le rapport des recouvrements ne distingue pas « la méthode est asymétrique en signe » de « la puissance en R2⁻ est insuffisante ». Le déclencheur sonne presque toujours si la puissance en R2⁻ est basse, sans rien dire du signe.

### (c) Contrôles négatifs absents

- **N1, option F** : pas de contrôle négatif *stratifié* sur le type d'étiquette retenue (concept rare vs opérateur vs fond). Sans lui, F est un mélange non interprétable.
- **N3** : le « nul — S31 sur vocabulaire permuté » teste la non-vacuité du signal, pas la spécificité aux ponts réels. Il manque un contrôle par *paires reliées avant la coupure* (le substitut ne devrait pas les classer plus haut que les paires non reliées, à degré/âge appariés).
- **N11(2)** : pas de contrôle de la mécanique de plantation : une paire de parents insérée dans le vivier change la distribution des paires candidates (45 → au plus 45, dont 1 ou 2 paires cibles). Si les bras sont sensibles à la composition du lot (corrélation entre scores), la plantation modifie le classement des paires non plantées. Contrôle absent : vérifier que le rang médian des paires non plantées ne change pas significativement entre lots avec et sans plantation.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. L'option B' (contrôle de sensibilité sur les seuls vrais conceptuels) est vrai par construction si la seule différence entre statuts est la rareté de l'étiquette retenue.**

C propose de recalculer Δ(N, N_β0) en masquant les ponts « vrai d'opérateur ». Mais le diagnostic (pièce 2, section 1.2, VÉRIFIÉ) montre que les vrais conceptuels et les faux ont la *même* distribution d'étiquette retenue (concept rare 0,82 vs 0,82 en M_bien ; fréquence 2,82 vs 2,88). Le gain de N sur N_β0 restreint aux seuls vrais conceptuels ne peut pas distinguer « N exploite la proximité conceptuelle » de « N exploite la rareté, qui est identique entre vrai conceptuel et faux ». Le contrôle de sensibilité est une tautologie : si la rareté sépare vrai d'opérateur des autres, retirer vrai d'opérateur ne prouve pas que la rareté ne sépare pas vrai conceptuel de faux — elle n'a pas besoin de le faire, les deux ont la même rareté (pièce 2, section 1.2, « Repli retiré » : 2,90 / 2,88 / 2,96, VÉRIFIÉ).

**2. La formule TEFV de N10 mêle trois quantités hétérogènes sous une même probabilité.**

C définit TEFV(B) = P(Moniteur(x) = 0 ∧ TâcheValide(x) = 1 ∧ KL ≤ κ_max). Problème : cette probabilité conjointe dépend de la corrélation entre les trois événements, qui n'est pas caractérisée. Sur les données de Bailey (pièce 24, p. 23, VÉRIFIÉ), la corrélation entre le nombre de couches obfusquées et la performance de tâche est négative, mais la relation Moniteur(x) = 0 ↔ TâcheValide(x) = 1 n'est pas monotone (certaines activations échappent à la sonde sans dégrader la tâche, d'autres non). La statistique TEFV traite les trois comme indépendantes dans sa formulation, mais les mesure conjointement — c'est un taux empirique, pas un produit de probabilités. Si la corrélation entre évasion et dégradation est faible (ce qui est justement le cas où la défense échoue), TEFV est basse non parce que le prix est élevé mais parce que les deux contraintes sont faciles à satisfaire en même temps. Le seuil 0,15 (illustratif) ne distingue pas les deux régimes.

**3. Le duel N4 repose sur une simulation dont les entrées (loi des niches, accord, structure) sont toutes HYPOTHÈSE.**

C propose de mesurer P(zéro paire dans le profil) après correction et de falsifier H_A si P > 0,50 à 10 fiches. Mais la simulation utilise une loi a priori (n1 0,30 … n6 0,05), un accord de 0,7 et une probabilité de structure de 0,3, tous SUPPOSÉ (pièce 11, section 6, VÉRIFIÉ). Aucun de ces paramètres n'est mesuré. Le duel ne falsifie donc pas « le profil est vide » mais « le profil est vide *sous cette loi* ». Si la vraie loi donne 20 % à n6 au lieu de 5 %, la conclusion s'inverse. C ne propose aucune mesure de la loi réelle avant la simulation, ce qui rend le duel non falsifiable sur les données réelles.

**4. Le calcul de puissance N11(1) utilise une approximation normale pour des proportions extrêmes à très petit n.**

C écrit : « pour détecter un écart de 20 points (p₁ = 0,35 vs p₂ = 0,15) sur des essais binaires indépendants, il faut n ≈ 70 ». Cette formule normale est fiable pour p loin de 0 et 1 et n grand. Mais à 8 fusions par bras (course 2), les résultats sont 0/8, 1/8, …, 8/8 — la distribution est discrète et fortement asymétrique pour p = 0,15. L'approximation normale surestime la puissance dans ce régime. Le test exact de Fisher (que C cite ensuite pour le cas 0/8 vs 6/8) est le bon outil, et il confirme que la puissance à n = 8 est quasi nulle sauf cas extrêmes. La formule de 70 essais est correcte mais ne s'applique pas au problème posé (8 fusions). C tire la bonne conclusion (« quasi nulle ») mais par un détour qui mélange deux régimes.

**5. L'étage 2 du jugement des ponts plantés (N11(2)) crée une fuite potentielle entre session-depot et conv-audit.**

C propose que session-depot détienne l'article-pont au coffre et qu'un « vérificateur d'équivalence mécanique/aveugle » compare la fusion à la cible. Ce vérificateur lit la fusion (produite par un proposeur via conv-audit) et la cible (détenue par session-depot). Si le vérificateur est un LLM appelé par session-depot, il reçoit les deux ; si c'est un programme, il faut un critère mécanique de « même mécanisme joint ». C propose « 3 ancres techniques scellées par session-depot ». Mais ces ancres sont choisies par session-depot, qui connaît la cible. Si les ancres sont trop spécifiques (« la fusion mentionne l'e-processus appliqué au contrôle d'activation »), le taux de faux positifs est bas mais le vérificateur fuit l'information de la cible dans la question. Si les ancres sont trop générales (« la fusion mentionne un objet mathématique »), le taux de faux positifs est élevé et le « pont trouvé » ne dit rien. Le choix des ancres est un degré de liberté non contrôlé.

### (b) Conditions de perte de puissance ou de non-jugeabilité

**N5, duel.** C propose un classifieur qui lit « tous les attributs publics/privés de l'instance PrePilote » pour prédire P vs N. La puissance dépend du nombre de runs simulés (100, illustratif) et de la dimensionnalité des attributs. À 100 runs avec des centaines d'attributs, le risque de surajustement est élevé ; un classifieur régularisé peut ne rien trouver même s'il y a une fuite, par manque de puissance. Le duel ne falsifie H_A que si la fuite est grossière (exactitude > 0,52 sur 100 échantillons → ≈ 52 vrais sur 100, ce qui exige un signal fort).

**N6, DL-12 hybride.** C propose de centrer par strate pour toutes les méthodes sauf M1, ou de modifier M1 pour tester les pentes et variances résiduelles. Si M1 est la seule méthode non centrée, la comparaison M1 vs les autres est biaisée (M1 opère sur des données non centrées, les autres sur des données centrées). La non-jugeabilité survient si l'on ne peut pas attribuer un écart de performance à la méthode ou à la transformation des données.

**N11, Recall@3 sur 12 ponts plantés.** C note que le test binomial par rapport à p₀ = 3/45 a une puissance > 0,85 dès 12 ponts. Mais le Recall@3 est calculé sur les *classements des bras*, pas sur des essais de Bernoulli indépendants. Si les 12 ponts sont plantés dans 4 sous-sessions, les classements intra-sous-session sont corrélés (les 45 paires partagent 10 fiches). L'hypothèse d'indépendance est violée, et la puissance est surestimée.

### (c) Contrôles négatifs absents

- **N1, B'** : pas de contrôle par *ajout* de vrais d'opérateur synthétiques à fréquence d'étiquette identique à celle des vrais conceptuels. Si le gain Δ_conc persiste après cet ajout, l'artefact d'opérateur n'est pas la cause.
- **N4** : pas de simulation avec la loi a priori *la plus défavorable* (n6 = 0,35, CA1-06). Le duel ne couvre qu'une loi « réaliste » — la pire devrait être servie.
- **N10** : le contrôle négatif proposé (« sonde linéaire sur une seule couche ») n'est pas un contrôle du TEFV mais du taux de jailbreak simple. Il manque un contrôle où le moniteur est multi-couches mais l'attaquant a un budget illimité (le prix est-il fini ?).

---

## Sur la proposition D

### (a) Défauts de méthode

**1. La recommandation N1 « option manquante : B plus un test de fuite portant sur les contrastes » est sous-spécifiée au point de ne pas être falsifiable.**

D écrit : « déplacement de tout contraste décisif par une correction ou une permutation, avec le critère d'artefact déjà écrit ». Le critère d'artefact (pièce 3, liste d'arrêt et audit, VÉRIFIÉ) exige « un essai sain et un essai d'artefact (R5) écrits par le sous-agent d'audit, dont la correction déplace, sur les graines de validation, au moins un contraste décisif du § 7 de plus que sa demi-largeur à 95 % ». Mais ici, il n'y a pas de « correction » à appliquer (V5 n'est pas un bug, c'est une mesure qui ne discrimine pas sous la loi du monde). La notion de « test de fuite portant sur les contrastes » n'est pas définie : quels contrastes ? Quelles permutations ? Quel seuil ? D ne fournit pas de métrique, seulement un renvoi au critère existant qui ne s'applique pas à ce cas.

**2. La formule de puissance N11(1) est formellement correcte mais vide sans les variances.**

D écrit la formule n ≥ ((z_{1−α/2} + z_{1−β}) σ_D / δ)² et conclut : « aucun nombre de mondes ou de rétrodictions n'est défendable sans leurs variances ». C'est exact, mais cela signifie que la proposition ne tranche pas la question posée (« combien de mondes pour qu'un retrait soit décidable »). Elle renvoie le calcul à un pilote futur sans dire quand ni comment ce pilote serait fait. La contribution est une formule, pas une réponse.

**3. Le transport (N11(3)) propose un test d'équivalence sans spécifier la marge.**

D écrit : « comparer les contrastes appariés synthétique / E1′ / ponts réels par test d'équivalence, avec marge égale au plus petit effet qui changerait la décision de bras ». Mais le « plus petit effet qui changerait la décision » dépend du critère de retrait, qui n'est pas encore défini numériquement (δ est « illustratif »). Le test d'équivalence est conditionné à un seuil non fixé. Sans marge, le test ne peut pas être pré-enregistré.

**4. La condition de retrait (iv) — « résultat reproduit dans au moins deux régimes pertinents » — est une condition de transport déguisée en condition de retrait.**

Si le retrait exige l'accord entre deux régimes, et si le transport n'est pas vérifié (ce que D reconnaît comme HYPOTHÈSE), alors (iv) bloque tout retrait jusqu'à la vérification du transport. C'est une circularité : on ne peut pas retirer un bras sans transport, et on ne peut pas vérifier le transport sans données suffisantes, qui ne sont disponibles qu'après plusieurs générations. Le résultat est que le retrait est toujours « non décidable ».

### (b) Conditions de perte de puissance ou de non-jugeabilité

**N3, duel H_A vs H_B.** D oppose « le substitut apporte un signal au-delà des règles mécaniques » à « il n'apporte rien ». Mais D ne spécifie pas de seuil quantitatif pour « apporte un signal ». La condition « borne basse du gain contre chaque base > 0 » est un test à puissance infiniment décroissante avec l'effet : un gain de 0,001 est « positif ». Sans taille d'effet minimale, le duel ne distingue pas un signal réel d'une fluctuation statistique à n modéré.

**N10, duel H_A vs H_B.** D oppose « une défense peut rendre le contournement plus coûteux que son gain » à « un attaquant retrouve un contournement à utilité acceptable ». Le test est conditionné à « coût minimal d'attaque pour atteindre un taux de contournement gelé, à taux de fausse alerte et plancher d'utilité fixés ». Quatre paramètres à geler (taux, fausse alerte, utilité, budget de référence), aucun n'étant spécifié même illustrativement. Le duel est non jugeable tant que ces paramètres ne sont pas fixés. Si le taux de contournement gelé est 0,01, presque toute défense passe ; si c'est 0,50, presque aucune.

**N6, DL-12 (1) « seulement après réécriture de M1 ».** D conditionne DL-12 à une réécriture de M1 et un essai du résidu non linéaire, sans préciser ce que « réécriture » signifie ni quel résidu est testé. La non-jugeabilité survient si la réécriture n'est pas faite (le brouillon 6 est « en cours » — pièce 15, RAPPORTÉ — et son contenu n'est pas servi). DL-12 reste alors suspendu indéfiniment.

### (c) Contrôles négatifs absents

- **N1** : D ne propose aucun contrôle négatif spécifique au « test de fuite portant sur les contrastes ». Le renvoi au critère d'artefact existant (R5) ne s'applique qu'après un audit déclenché, pas en validation.
- **N11(2)** : D propose des « leurres appariés par âge, degré, niche et fréquence » mais pas de contrôle de la *reconstruction* de la relation structurelle. Un leurre apparié qui partage une structure avec la cible (par hasard dans un domaine étroit) ne serait pas distingué d'un faux positif. Il manque un contrôle par « paire chimère » (parents de niches incompatibles, comme le propose C) ou par « pont inversé » (les deux parents sont postérieurs à l'article-pont).
- **N4** : D propose niches permutées et structures forcées par le texte I comme contrôles négatifs. Il manque le contrôle par *accord parfait des lecteurs sur la mauvaise niche* : si les deux lecteurs s'accordent sur une niche erronée (biais systématique), le kappa est élevé mais le profil est faux. Un contrôle par fiches à niche connue (jeu d'essai étiqueté par un expert humain — le directeur) est absent.

FIN-DE-CELLULE