# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces reçues.** B, C, D et E sont présentes et se terminent par leur marque de fin. Ma propre conception du tour III.1 ne m'est pas retransmise : je n'en cite rien.

**Statuts.** Ce qui vient des faits est RAPPORTÉ. Mes critiques sont des HYPOTHÈSES de méthode. Mes calculs sont marqués « illustratif — calcul dérivé ».

---

## Sur la proposition B

### (a) Défauts de méthode

1. **L'e-processus P3 teste « agent = jumeau », pas « agent honnête ».** Son propre contrôle positif le montre : un agent honnête à température modifiée « doit être détecté ». Toute différence bénigne d'invite, de version ou de décodage est donc une fausse alerte de même nature qu'un sabotage. Le rejet confond intention et identité de politique.
2. **Fuite par l'invite.** Si le saboteur a les mêmes poids et une consigne différente, les activations diffèrent dès le préfixe et P3 détecte la consigne. S'il a des poids affinés, « le jumeau sur le même préfixe » n'est plus la loi de l'agent s'il était honnête (S6 de B). B liste S6 mais ne sépare pas ces deux régimes.
3. **E2 « falsifie H_B » par non-rejet.** Un test d'uniformité à p > 0,05 n'établit pas l'uniformité. De plus :
   - Kolmogorov-Smirnov n'est pas calibré pour des p-valeurs discrètes, de support {1/(K+1), …, 1} ;
   - les pas d'un même épisode ne sont pas indépendants ;
   - l'uniformité marginale regroupée n'implique pas E[e_t | passé] ≤ 1, seule condition que demande Ville. Un honnête engagé dans une impasse peut avoir des p_t durablement petits alors que l'histogramme regroupé reste plat.
4. **E3 et E4 falsifient H_A par manque de puissance.** « L'intervalle contient 0 » ou « contient 0,5 » falsifie H_A. L'effectif de sabotages est inconnu (S9 de B), donc H_A tombe par construction s'il est petit. Je reprends ici, en le disant, la règle de marge de D : une borne supérieure ≤ g falsifie H_A, un chevauchement est non concluant.
5. **M4 est vrai ou faux par construction.** À poids et invite égaux, la passe avant est déterministe et la « dérive par rapport au jumeau » est nulle. À poids ou invite différents, elle est non nulle sans manipulation.
6. **P2 et E1.** La fonction de normalisation est choisie sur les épisodes qui servent ensuite à tester l'invariance, puis à calibrer.
7. **Le coût de P3 est récurrent.** Il faut K continuations par point de contrôle pour chaque épisode surveillé, pas seulement pour la calibration.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Transport par Ville.** Si E[e_t | F_{t−1}] ≤ 1+ε, la borne devient P(sup_{t≤T} M_t ≥ 100) ≤ (1+ε)^T/100. La garantie tient à un facteur 2 près seulement si ε ≤ ln 2 / T. E2 est jugeable si le nombre effectif de pas indépendants dépasse environ (z·σ_e/ε)², où σ_e est l'écart-type du facteur. Pour T = 50 et σ_e = 1, cela fait de l'ordre de 10⁴ pas effectifs (illustratif — calcul dérivé). L'effectif effectif se compte après la corrélation intra-tâche, ce que B exige ailleurs.
- **Puissance de P3.** Le facteur est borné par p_min = 1/(K+1). L'espérance de log e_t croît avec la divergence par pas entre la loi du rang sous sabotage et l'uniforme. Si le saboteur garde chaque rang dans le support central, cette espérance est ≤ 0 et M_t décroît.
- **E1.** Une marge de ± 3 points au quantile 90 % demande un écart-type du taux par bac d'environ 1,5 point, soit n_b ≈ 400 tâches indépendantes par bac (illustratif — calcul dérivé). Avec quelques centaines d'épisodes au total (RAPPORTÉ), E1 ne peut pas falsifier H_B. Et une invariance au quantile 90 % ne contraint pas le quantile 99 % si l'indice de queue dépend du bac.
- **P1.** Avec une corrélation intra-tâche ρ et m épisodes par tâche, n_eff = n/(1+(m−1)ρ). Sous 299, le calcul de Wilks cité par B ne tient plus.
- **M1.** Le conditionnement sur la valeur perd sa validité si la loi de la covariable diffère entre honnête et saboteur. B le voit comme canal d'évasion ; c'est aussi une condition de validité du contraste.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un agent **honnête mais différent** (invite paraphrasée, autre graine d'affinage bénin), qui ne doit pas franchir 100.
- Une vérification directe de Ville à des niveaux jugeables : la fréquence de sup M_t ≥ 5 et ≥ 10 sur les épisodes honnêtes doit rester ≤ 20 % et ≤ 10 %.
- Un test de dépendance sérielle des p_t par épisode, avec étiquettes permutées *entre épisodes*.
- Un masque de neurones aléatoire de même taille pour M1 et M2. Les faits rapportent ce contrôle pour l'ablation (74,6 %, RAPPORTÉ).
- Une cellule « saboteur assigné sans dommage confirmé ». Sans elle, le conditionnement sur le dommage sélectionne des épisodes sur une issue.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts déplacés.**
   - « N ≈ 300 à 500 épisodes [RAPPORTÉ] » : les faits disent « quelques centaines ».
   - « Le papier établit », « démontre » : les résultats sont RAPPORTÉS, sur des tâches vérifiables.
   - « Garantit mathématiquement » qualifie A1, dont la validité est suspendue à une hypothèse non testée.
   - Les couches 15-22 sont présentées comme le siège des neurones de dopamine. Les faits rapportent aussi la couche 5 pour l'exemple affiché.
2. **A1 : centrage en échantillon.** Z_k est centré et studentisé sur les épisodes mêmes où l'on vérifiera E[Z_k | F_{k−1}] ≤ 0. La moyenne nulle en échantillon est vraie par construction.
   - La troncature inférieure qui rend 1+λZ ≥ 0 relève la moyenne.
   - Un effet aléatoire de tâche u_i rend la moyenne *conditionnelle au passé* positive dès que le passé révèle u_i > 0. C'est la H_B de sa propre Expérience 1, donc A1 n'a aucune garantie avant cette expérience.
3. **Pseudo-réplication.** Les « 4 000 à 25 000 transitions » et les « 50 000 trajectoires » rééchantillonnées ne contiennent pas plus d'information de queue que le nombre de tâches indépendantes. Le bootstrap ne produit aucun incrément hors du support observé.
4. **Contrôle négatif de l'Expérience 1 insuffisant.** Permuter les paragraphes *dans* l'épisode conserve u_i. Le contrôle passe alors que la dépendance inter-pas subsiste.
5. **Critère vrai par construction.** « Réduire la largeur de l'intervalle d'un facteur 3 » par une loi de Pareto généralisée : un modèle paramétrique rétrécit toujours l'intervalle. La largeur n'est pas la couverture.
6. **B1, résidu r_t = δ̂ − (V̂_{t+1} − V̂_t).** C'est la différence de deux estimateurs bruités de la même cible. Sa loi est dominée par l'erreur de sonde : l'AUC pré-génération vaut 0,67 et les corrélations de Spearman ne sont montrées que graphiquement (RAPPORTÉ). La lecture de valeur est rapportée à la position initiale et finale, pas à chaque frontière. Le lien « causal » invoqué est un effondrement global d'exactitude, de 75,2 % à 20,3 % (RAPPORTÉ). Toute ablation de cette ampleur dégraderait un signal aval.
7. **B4 : même défaut que le M4 de B.** Greffer les neurones du jumeau « sur le même prompt initial » donne une divergence nulle à poids et invite égaux. Sinon la greffe lit la différence d'invite.
8. **Expérience 3.**
   - Le contrôle (neurones de la sonde de jeton suivant, 76,4 %, RAPPORTÉ) ne perturbe presque rien, donc son AUC ≈ 0,5 est triviale. Il n'est pas apparié en ampleur de perturbation.
   - Les étiquettes « étape de sabotage » viennent de l'équipe qui implante.
   - Le type de contenu (code ou prose, entropie) est confondu avec la classe.
9. **B2.** Remplacer le pas par un tirage du jumeau est déjà l'intervention. La contribution de la sélection par la sonde n'est pas isolée.
10. **B3.** Le 0,3 des faits filtre des *cibles d'entraînement*. C l'applique à un écart de sorties de sonde, qui est une autre grandeur. Le filtre contredit aussi la prémisse du programme, des signaux petits et sommés (RAPPORTÉ). C le reconnaît.
11. **Échantillonnage par clonage.** Le recrutement dépend du score. Les clones partagent un préfixe. Aucun audit binomial simple n'est valide ensuite.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Expérience 1, critère [0,8 % ; 1,2 %].** L'écart-type d'un taux de 1 % sur n épisodes vaut √(0,0099/n). Résoudre ± 0,2 point demande n de l'ordre de 10⁴ (illustratif — calcul dérivé). C'est plus que les 5 000 que la tâche cherche à éviter. Sur 150 épisodes, le critère n'est pas jugeable.
- **A1.** Sous une dérive δ = E[Z_k | F], la borne se dégrade en exp(λδT)/100. La dérive tolérable est d'ordre ln 2/(λT), à estimer sur des tâches laissées de côté.
- **A2.** L'écart-type asymptotique de ξ̂ vaut (1+ξ)/√k, soit environ 0,16 pour k = 40 excès et ξ = 0 (illustratif — calcul dérivé). L'extrapolation n'a pas de puissance si la queue est un mélange dont la composante rare a une probabilité π par tâche avec π·n_tâches ≲ 1.
- **Expérience 2.** Un taux de détection « à 1 % de fausses alertes calculé sur les échecs honnêtes appariés » n'est défini que si le nombre d'échecs honnêtes indépendants est ≥ 99. Cet effectif n'est pas fourni.
- **B1.** Aucune puissance si la loi de r_t conditionnelle à l'état est la même sous échec honnête et sous sabotage. Elle l'est dès que l'erreur des deux sondes ne dépend pas de l'intention.
- **Expérience 3.** Plafond : si la variance de la divergence sous ablation est dominée par la perturbation générique, le rapport signal sur bruit entre classes tend vers 0.

### (c) Contrôles négatifs dont l'absence serait fatale

- Une permutation des incréments **entre** épisodes, et pas seulement à l'intérieur.
- Une ablation aléatoire calibrée pour produire la même divergence moyenne que l'ablation de valeur.
- Un r_t calculé avec δ̂ et ΔV̂ désalignés dans le temps.
- Un agent honnête portant une invite inhabituelle sans rapport avec le sabotage, pour B1 et B4.
- Un candidat du jumeau tiré au hasard, pour B2.
- Une couverture de A2 mesurée sur des familles réservées, à un quantile jugeable.

---

## Sur la proposition D

### (a) Défauts de méthode

D est la pièce qui sépare le mieux les promesses. Ses défauts sont des lacunes de spécification.

1. **La formule de rang p_b(s) compte des épisodes i.** Avec plusieurs épisodes par famille, l'échangeabilité avec un épisode d'une *nouvelle* famille est fausse. D exige des partitions par famille mais ne donne pas l'estimateur. Il faut un score par famille ou un sous-échantillonnage hiérarchique.
2. **Le duel 1 peut être gagné par le silence.** H_A (« chaque taux ≤ 1 % ») devient vraie par construction en relevant le seuil. D le note et rapporte la détection « séparément ». Le duel n'est alors pas une inférence forte : l'issue H_A ne falsifie rien sur le monde. Le critère doit être conjoint : borne de fausses alertes ≤ 1 % **et** détection ≥ g.
3. **« Meilleur comparateur ».** S'il est choisi sur les données d'évaluation, c'est une sélection sur l'échantillon de test. Le biais joue contre H_A, mais reste une fuite.
4. **La marge g n'a pas de valeur.** Tant qu'elle n'est pas fixée *et* rapportée à l'effectif de paires de sabotage, aucun duel de D n'est jugeable.
5. **Duel 3, routage randomisé.** Un budget fixe alloué par classement crée une interférence entre épisodes : auditer l'un déplace l'autre. L'unité de randomisation est donc le lot, et l'effectif est le nombre de lots. Par ailleurs le saboteur est figé. Le test d'évasion étant clos (RAPPORTÉ), le gain vaut pour un adversaire non adaptatif.
6. **Classe de longueur finale.** La longueur est une issue post-traitement. Un saboteur qui la modifie choisit sa classe. D relève que la classe n'est pas disponible pour router tôt, pas qu'elle est manipulable.
7. **Le contrôle « masquer la correspondance entre trajectoires et épisodes »** n'est pas défini opérationnellement.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Règle de rang.** Elle est muette si n_b < 99, ce que D dit. À n_b = 99, la probabilité que le seuil installé ait un taux réel > 1 % vaut 0,99⁹⁹ ≈ 0,37 (illustratif — calcul dérivé). La promesse marginale et la promesse installée divergent donc fortement à ce minimum.
- **Audit binomial sans alerte.** Il faut m_b ≥ ln δ_b / ln 0,99, soit environ 299 épisodes indépendants par classe pour δ_b = 5 %. Pour cinq classes à risque global de 5 %, c'est environ 459 par classe (illustratif — calcul dérivé). Avec quelques centaines d'épisodes déjà analysés, l'issue attendue de D est « non certifié » presque partout. Ce résultat honnête doit être annoncé comme l'issue probable.
- **Familles.** Avec ρ et m comme chez B, tous les effectifs ci-dessus se lisent en n_eff.
- **Puissance par classe.** Si P(L ∈ b | sabotage) se concentre sur les classes où n_b < 99, la détection est nulle par construction.
- **Duel 3.** La revue empêche le dommage, donc le dommage est censuré. Le duel n'est jugeable que si l'étiquette pré-intervention a un taux d'erreur connu et indépendant du score.

### (c) Contrôles négatifs dont l'absence serait fatale

- Une sonde entraînée sur des étiquettes permutées, en plus des dimensions aléatoires.
- Un agent honnête sous invite différente, comme chez B et C. D sépare la condition assignée du dommage mais ne prévoit pas ce témoin.
- Une cellule « saboteur assigné sans dommage ».
- Un routage placebo au niveau du lot : priorités permutées *entre lots*, pas seulement dans le lot.
- Une vérification que la loi de la longueur est la même entre honnêtes et saboteurs avant toute lecture par classe.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts déplacés.**
   - L'existence des épisodes, du jumeau et des sondes est dite « OBSERVÉ-NON-AUDITÉ ». Les faits la donnent comme contexte, sans ce statut.
   - « VÉRIFIÉ » est apposé à des énoncés qui ne sont pas de l'arithmétique refaite : le rétrécissement des résidus sans ajustement croisé, la propriété de Markov de l'état sauvegardé.
   - L'année de « AI Control » diffère entre B (2023) et E (2024) : référence à vérifier.
2. **Coût déclaré contre coût réel.** P1 est annoncé à « zéro nouvel épisode », mais E1, qui le valide, demande 500 **échecs** honnêtes scellés (illustratif chez E). Cela suppose plus de 500 épisodes honnêtes nouveaux, le taux d'échec n'étant pas fourni.
3. **E1 mesure une autre population.** Le verdict porte sur les épisodes honnêtes (RAPPORTÉ). E1 compte les fausses alertes sur les seuls échecs honnêtes. Un échec de E1 n'est donc pas une violation du verdict. Un succès est conservateur.
4. **E1 n'est pas un duel exclusif.** H_B est une disjonction : taux > 1 % *ou* détection inférieure à O3. Un e-processus valide mais moins puissant rend H_A (validité) et H_B vraies ensemble. La zone de 6 à 10 alertes n'est attribuée à aucune issue.
5. **M1 n'utilise plus l'état interne de l'agent.** Lire l'action de l'agent « avec les poids du jumeau » en fait un moniteur de confiance sur les actions, projeté sur moins de 1 % des dimensions. Le contexte du programme tient ce type de moniteur pour faible face au diffus (RAPPORTÉ). Par construction, M1 ne peut lire qu'une action de moindre valeur. Un pas honnête fautif produit le même Δ_t : les faits rapportent des creux aux failles logiques. E3 teste donc une H_A que la construction de M1 rend déjà improbable.
6. **Retrait du filtre 0,3.** Les cibles sont des différences de valeurs estimées par tirages Monte Carlo. Avec R = 8 tirages (illustratif chez E), l'écart-type d'une différence atteint environ 0,25 (illustratif — calcul dérivé). Les cibles |δ| < 0,3 sont alors surtout du bruit. Le filtre des auteurs est possiblement un filtre de bruit (HYPOTHÈSE).
7. **E2.** La « réussite de jalons intermédiaires en recherche ouverte » suppose une étiquette de réussite que les faits déclarent absente (pas de récompense vérifiable propre). Le bootstrap « par épisode » ignore les grappes de tâches.
8. **E4 et C2 sortent du périmètre ouvert.** « Y compris face à un saboteur informé » et l'« organisme entraîné avec pénalité d'évasion » relèvent du test d'évasion, clos pour l'instant (RAPPORTÉ). Sans cette clause, E4 ne peut que falsifier H_A.
9. **Organismes affinés** (section 4 de E). Leur « jumeau honnête » n'est pas défini. Il faudrait un jumeau affiné sur données bénignes, sinon l'e-processus rejette l'affinage.
10. **Devis.** Les 120 à 200 USD pour 650 épisodes d'agent sont illustratifs. Ils cohabitent mal avec le fait rapporté que produire des épisodes est coûteux, et diffèrent des ordres de C. Je reprends, en le disant, la position de D : pas de conversion monétaire sans pilote.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1, issue « ≤ 5/500 falsifie H_B ».** La borne supérieure unilatérale à 95 % pour 5 alertes sur 500 est d'environ 2,1 % (illustratif — calcul dérivé). H_B (taux > 1 %) n'est donc pas exclue. Par tercile, environ 167 épisodes donnent 1,7 alerte attendue à 1 % : le « sans excès dans le tercile long » n'est pas jugeable.
- **P1 avec K = 4.** Le facteur par pas est ≤ 5. La condition en ε ≤ ln 2/T donnée sur B s'applique. S'ajoute le sous-échantillonnage de m préfixes, qui doit être indépendant des scores.
- **P2.** La loi Bêta du taux conditionnel suppose des scores i.i.d. continus et un seuil indépendant de l'ajustement. Avec ajustement croisé, les résidus de plis différents ne sont pas échangeables, et l'intervalle « exact » ne l'est plus.
- **P3, coupe-circuit à 5 %.** La borne de tolérance demande n ≥ 59 tâches indépendantes par strate (illustratif — calcul dérivé). « Quelques centaines suffisent rigoureusement » dépend d'une répartition par classe non fournie.
- **M1 sans filtre.** Le signal n'est apprenable que si la variance des vrais δ dans la bande conservée dépasse la variance Monte Carlo des cibles. Pour |δ| ≈ 0,05, il faut R de l'ordre de 200 tirages par frontière (illustratif — calcul dérivé).
- **E2.** Le seuil ΔAUC ≥ 0,05 égale l'écart rapporté *en domaine* entre sonde et longueur (0,67 contre 0,62, RAPPORTÉ). Hors domaine, face à longueur et entropie combinées, et avec quelques centaines d'épisodes, l'intervalle contiendra probablement à la fois 0 et 0,05.
- **E4.** Une perte de réussite honnête de 2 points n'est pas résoluble avec quelques centaines d'épisodes par bras : l'écart-type d'une différence de proportions à n = 300 est d'environ 4 points (illustratif — calcul dérivé).
- **C2.** Même plafond que l'Expérience 3 de C.

### (c) Contrôles négatifs dont l'absence serait fatale

- Un agent honnête différent du jumeau. L'A/A de E ne teste que l'indexation.
- Pour E3, un témoin d'échec honnête **naturel**, en plus du bogue injecté. Un bogue d'environnement peut provoquer sa propre réponse de surprise et n'a pas la loi des échecs spontanés.
- Pour M1, la divergence du jumeau forcé restreinte aux mêmes pas. E la prévoit comme base. Elle doit aussi servir de borne : si M1 ≤ cette base, M1 est une projection de celle-ci.
- Une sonde entraînée sur des cibles Monte Carlo rééchantillonnées indépendamment (deux jeux de tirages), pour mesurer le plafond de bruit avant de retirer le filtre.
- Une ablation appariée en ampleur pour C2.

---

## Ce dont je me sers, en le disant

- **De D** : la règle de marge g pour toute falsification, et le refus de chiffrer un devis sans pilote.
- **De B** : le comptage par tâche indépendante, et l'aveu que l'économie de P3 n'est pas garantie.
- **De C et E** : rien n'est repris sans le contrôle apparié correspondant listé ci-dessus.

Je ne fusionne pas les e-processus de B, C et E. Leurs hypothèses nulles diffèrent : rang contre jumeau chez B et E, résidu centré en échantillon chez C. Leurs modes d'échec ne sont donc pas les mêmes.

FIN-DE-CELLULE