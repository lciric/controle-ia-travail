# Tour III.2 — Critique croisée de méthode (proposition A)

Pièce 5 (antériorité de la boucle) non servie : rien n'en est supposé ici. Les chiffres que je calcule moi-même ci-dessous sont **illustratifs** (ordres de grandeur, formules usuelles d'erreur-type) ; ceux qui viennent des pièces portent leur statut d'origine. Les trois propositions reposent sur un même socle de faits ; je ne les harmonise pas : chacune a ses propres points de rupture.

Un défaut commun que je signale une fois et ne répète pas : les trois propositions utilisent « notable » (juges-modèles) ou « survit » (tests de mort) comme issue. Le fait servi est que les juges notent la **cohérence entre champs**, ni valeur ni nouveauté (Pièce 1 § 9.4.B, VÉRIFIÉ sur pièce), et que les tests de mort n'ont **jamais été activés** et que la couche 1 réelle n'a « pas de dents » (0/20, OBSERVÉ-NON-AUDITÉ). Toute expérience dont l'issue est l'une de ces deux étiquettes mesure d'abord l'instrument d'étiquetage.

---

## Sur la proposition B

### (a) Défauts de méthode

**Exp. 1 (moisson utile ?) — vrai par construction.** Le critère « au moins un résumé contient un élément absent de la fiche » sur 4 requêtes × 5 résultats = 20 résumés par fiche est satisfait presque sûrement par n'importe quel tirage de 20 résumés dans le domaine, ciblé ou non. Le témoin proposé (termes du vocabulaire au hasard) est trop faible : il ramène des résumés hors sujet que le lecteur jugera « non pertinents », ce qui donne à H_A une victoire mécanique. Le témoin pertinent est celui que B utilise ailleurs (c1 : les 5 mots du titre), mais il n'est pas dans Exp. 1.

**Exp. 1 — lecteur confondu.** « Lecteur neuf : Opus 5.5 si non proposeur » : Opus 5.5 est juge de la course 2 (Pièce 1 § 1.3). Le même modèle étiquette l'enrichissement et jugera les fiches enrichies : l'instrument d'évaluation de la moisson est aussi l'instrument de sélection en aval.

**c1 — fuite construction ↔ évaluation, et contradiction interne.** c1 calibre le moissonneur sur sa capacité à **retrouver ≥ 3 des 5 antériorités déclarées** par les fiches de la course 1. Or la question (Q2) et H_B d'Exp. 1 définissent l'échec comme « ramener ce que la fiche cite déjà ». c1 récompense exactement ce que Exp. 1 pénalise. De plus, les fiches de la course 1 servent à la fois de matériau de réglage (c1) et de matériau d'épreuve (Exp. 1) ; et elles sont sous `donnees/`, non lisibles par conv-audit (Pièce 1 § 10) — le protocole suppose un accès qui n'est pas acquis.

**Exp. 2 (affinement) — métrique monotone.** Δ_champs, Δ_antériorités, Δ_prédictions ≥ 0 avec au moins un > 0 : un modèle qui réécrit sans jamais supprimer et ajoute une antériorité par tour atteint « progrès » dans ≈ 100 % des cas, dans le bras moisson comme dans le bras sans moisson. La métrique mesure la politique « ne rien retirer », pas le contenu. « Antériorités vérifiées » suppose en outre une vérification sur PDF (R7) dont le coût n'est pas dans le devis.

**Exp. 3 (fiche–article) — témoin hors domaine.** 24 paires fiche–article « au hasard » dans un vivier OpenAlex de 197 681 œuvres en 5 sous-domaines, sans résumé (Pièce 3 § 4.1) : (i) le bras basique « adapté » exige un Jaccard de concepts sur résumés qui n'existent pas dans cette moisson ; (ii) les paires au hasard tombent majoritairement hors de l'axe de la fiche, leurs fusions échouent à l'étage 1 (format) plutôt que sur la fertilité. Le gain de 10 points serait obtenu par construction via le taux d'échec de forme.

**Exp. 4 (rétrodiction IA) — mesure le taux de base, pas des « dents ».** La Pièce 2 montre que les quatre méthodes de cooccurrence battent ST de 5 à 10 points et que le seuil absolu bascule avec le taux de base (point 3 des « points mal posés »). B reprend un seuil absolu (+5 points) et une conjonction avec un taux de base ≥ 0,1 % : si le taux de base passe, « ≥ 2 méthodes à +5 » suit presque sûrement, car toute méthode de voisinage capture le degré. Sans appariement sur le degré et l'âge (Pièce 3 § 4.4), Exp. 4 ne distingue pas « méthode » de « popularité ».

**Exp. 5 (entropie) — confondue par l'effectif.** L'entropie est estimée sur les étiquettes des **fiches actives** ; la douane réduit leur nombre tour après tour. L'estimateur direct de l'entropie est biaisé vers le bas à petit effectif (voir (b)) : le ratio ≤ 0,80 peut résulter de la seule décroissance de n_t.

**c2 — planteur non aveugle.** Les 10 paires « fertiles » plantées sont construites par quelqu'un qui connaît la formule du bras (Jaccard des concepts) ; un planteur qui partage des concepts rend les paires détectables par construction.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **Exp. 1.** Soit p_c, p_r les probabilités d'« enrichissement » (ciblé, hasard), estimées par proportions sur n = 20. Si le lecteur déclare « élément nouveau » avec une probabilité de fond ε indépendante du contenu, l'espérance observée est p + ε(1 − p) : la différence p_c − p_r est contractée d'un facteur (1 − ε). À ε ≥ 0,5, la marge de 0,15 exigée correspond à une marge réelle ≥ 0,30. À n = 20, l'écart-type d'une différence de proportions vaut ≈ 0,15 à p ≈ 0,5 (illustratif) : la marge de 0,15 est 1 erreur-type.
- **Exp. 2.** Si, sous le témoin « réécriture sans moisson », P(Δ_i ≥ 0 pour tous i et ∃ Δ_i > 0) ≥ 0,9, le plafond rend toute différence indétectable : le critère « contrôle < taux − 0,10 » est inatteignable et H_A est réfutée même si la moisson apporte un contenu réel.
- **Exp. 3.** Différence de deux proportions à n = 24 et 24 : erreur-type ≈ 0,14 à p ≈ 0,5 (illustratif) ; le seuil de 10 points vaut 0,7 erreur-type. Pour détecter 10 points à 80 % de puissance au seuil 5 % il faut de l'ordre de 400 fusions par bras (illustratif). Si en plus la concordance des juges sur « notable » est proche du hasard (accord de rang 0,12 en course 1, Pièce 1 § 10), la variance de l'étiquette s'ajoute à celle du tirage.
- **Exp. 4.** La précision à 10 000 est estimée sur un échantillon de paires ; au taux de base π, un seuil absolu de +5 points vaut un facteur 50 à π = 0,1 % et 5 à π = 1 %. Le verdict est fonction de π, non de la méthode. Injugeable aussi lorsque, dans un graphe jeune à degrés très dispersés, l'attachement préférentiel atteint déjà le seuil : les méthodes sont alors indistinguables de PA.
- **Exp. 5.** Avec K étiquettes et n_t fiches, le biais de l'estimateur direct est d'ordre −(K − 1)/(2 n_t ln 2) bits (correction classique, référence à vérifier). Pour K = 50, n_1 = 128, n_5 = 30 (illustratif), la différence de biais entre les tours vaut ≈ 0,9 bit ; si H_1 ≈ 4 bits, c'est ≈ 22 % de baisse par le seul estimateur, soit le seuil de B franchi sans aucune convergence thématique.
- **c5.** Sur 5 témoins par classe, 4/5 exigés : l'intervalle de Wilson sur un taux à n = 5 couvre ≈ [0,3 ; 1,0] ; aucune borne utile.

### (c) Contrôles négatifs dont l'absence serait fatale

1. Exp. 1 : **requêtes construites à partir des seules antériorités déjà citées** et mesure du recouvrement des résultats avec ces antériorités ; **lecteur en aveugle** sur le bras, avec paires « fiche + résumés d'une autre fiche » pour estimer ε.
2. Exp. 2 : un bras **paraphrase pure** (même information, réécriture) doit donner un taux de « progrès » ≈ 0 ; sinon la métrique est morte.
3. Exp. 3 : paires au hasard **dans le même axe et sous-domaine**, et taux d'échec à l'étage 1 rapporté à part.
4. Exp. 4 : appariement degré/âge, seuil relatif au taux de base, fenêtre placebo (comme Pièce 2 (b)).
5. Exp. 5 : entropie calculée à **effectif constant** (sous-échantillonnage au plus petit n_t) et tours permutés.
6. c1 : vérité terrain par **citation masquée** (retirer une antériorité, mesurer son rappel), non par les antériorités que la fiche cite déjà.

---

## Sur la proposition C

### (a) Défauts de méthode

**Q1 — garde anti-reformulation contournable par le tuple.** La garde refuse V_{t+1} si ni les identifiants d'antériorité ni `(métrique, valeur, seuil)` ne changent. Une perturbation numérique (valeur × 1,01) suffit à passer. Le critère de progrès est alors « changer un nombre », vrai par construction pour tout proposeur qui l'apprend.

**Q2 — liste blanche S31 contre l'objet même de la boucle.** Seuls les concepts portés par ≥ 20 œuvres peuvent entrer dans une requête ; les « trous » nommés avec un concept rare sont donc inqueryables par construction. La restriction aux cinq sous-domaines de la moisson interdit mécaniquement les ponts « loin en domaine » du bras basique : la boucle est confinée dans le vivier qui a servi à construire le vocabulaire (fuite construction → évaluation : le vocabulaire de requête est dérivé du corpus sur lequel la rétrodiction sera lue).

**Q3 / E3 — le préfiltre contredit le bras qu'il nourrit.** L'allocation de ressources sélectionne les articles à **nombreux voisins communs** avec les concepts des fiches ; le bras méta cherche des niches qui **communiquent peu**. Le préfiltre fabrique le contraire du profil visé. E3 mesure alors le préfiltre, pas le bras. Les étiquettes de concepts proviennent de deux processus différents (lecteurs neufs sur fiches, `concepts/topics` OpenAlex sur articles) : tout Jaccard fiche–article est confondu par l'étiqueteur.

**E3 — « sans repli » vrai par construction.** Passer de 6 à 20 entités fait passer le nombre de paires de 15 à 190 ; voir (b) : ≥ 7/8 lots sans repli est quasi certain même avec des articles sans valeur. Le second critère (« ≥ » entre fiche–article et fiche–fiche, égalité comptée pour H_A) est biaisé vers H_A. Enfin « sans antériorité » est indéfini pour une fusion fiche–article : l'article apparié est-il une antériorité ? Selon la réponse, le critère favorise ou défavorise H_A.

**E2 — deux facteurs confondus.** Bras H_B : 24 embryons, puis **sélection des 8 meilleurs par les juges** ; bras H_A : 8 embryons tirés au sort, **sans sélection**, puis 3 tours. La comparaison mêle « sélection par juges » et « itération ». Le budget est compté en « unités » : un tour (moisson + affinage + bisociation) n'est pas une moisson en jetons. L'issue est la survie aux tests de mort, qui exige un script écrit par l'agent expérimentateur à partir d'une fiche sans « prise idéation » (non construite) : la survie mesure la capacité de l'agent à produire un script qui passe, confondue avec la fiche.

**E1 — repli non falsifiable.** « H_A réfutée → on utilise RA + substitut S31 » : le substitut S31 n'est éprouvé par aucune des issues de E1. Une seule course par configuration est prévue alors que la variance inter-graines de Gu–Krenn est inconnue (I-9).

**Q5 — portée surestimée.** « Garantit mathématiquement l'absence de contamination » pour un modèle à poids ouverts de 2023 : rien dans les faits n'établit la date des corpus d'entraînement ; les noms et dates de modèles avancés par C ne viennent d'aucune pièce (référence à vérifier). L'anonymisation par isomorphisme détruit la connaissance de domaine : elle mesure une autre tâche que celle demandée.

**(c) de C, ligne 2 — fuite.** Le détecteur de progrès est calibré sur les 28 fonds + 4 rendus appariés du pré-pilote, qui sont ensuite le matériau d'épreuve du pré-pilote : instrument réglé sur son jeu d'évaluation.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **E1.** Positifs = paires non reliées fin 2023, reliées 2024–2026 avec ≥ 5 citations révisées (`counts_by_year` actuel). Soit N_+ leur nombre. ΔP@1000 de 2 points : erreur-type de P@1000 ≈ √(p(1 − p)/1000) ≈ 0,0095 à p = 0,1 (illustratif) ; le seuil vaut ≈ 2 erreurs-types avant corrélation des têtes. Injugeable si, sur l'échantillon apparié degré/âge, AUC_RA < 0,55 (illustratif) : plus de signal à comparer. Injugeable aussi si N_+ < ≈ 500 (illustratif) : P@1000 n'est plus une estimée de précision mais une fraction du total des positifs.
- **E2.** Survies s_A, s_B, s_P par fiche, n = 8 par bras. Si s_B ≈ 0 (le « pas de dents » observé), le seuil « +2 » ne teste que s_A ≥ 0,25 et ne distingue pas une boucle utile d'un test de mort devenu laxiste. À s = 0,25 partout, P(diff ≥ 2 par hasard) ≈ 0,2 (illustratif). Si la survie vaut q·s′ avec q = probabilité que le script soit exécutable, indépendante de la fiche, les bras comparent q.
- **E3.** Avec π par paire et m entités, P(au moins une paire au profil) = 1 − (1 − π)^{m(m−1)/2}. De 0,27 à m = 6 (Pièce 1 § 7.3) on tire π ≈ 0,021 ; à m = 20, 1 − 0,979^190 ≈ 0,98 sous indépendance (illustratif). Le seuil 7/8 est atteint sans aucun apport des articles.
- **Q1, arrêt.** Jaccard sur ≈ 10 étiquettes : une étiquette = 10 %, la granularité égale le seuil ; l'arrêt est décidé par arrondi.
- **Détecteur de progrès.** TD ≥ 90 % mesuré sur 4 paires de vraies redites : intervalle ≈ [0,4 ; 1,0] ; injugeable.
- **Garde de fuite.** 0 fuite sur 50 plantées borne le taux de fuite manquée à ≈ 6 % (règle de trois, 95 %) ; « 0 toléré » est une politique, pas une mesure.

### (c) Contrôles négatifs dont l'absence serait fatale

1. E1 : témoins **degré seul** et attachement préférentiel sur l'échantillon apparié ; étiquettes permutées (prévu) ; **fenêtre placebo** (2021 → 2023) pour voir si le seuil absolu bascule ; ≥ 3 graines.
2. E2 : **calibration préalable des tests de mort** sur témoins vrais/faux non tautologiques (la ligne 5 du tableau de C doit précéder E2, pas la suivre) ; un bras « 8 tirés au sort sans sélection ni boucle » pour isoler la sélection par juges.
3. E3 : 14 articles **au hasard dans le même sous-domaine** (le témoin OpenAlex entier est hors domaine) ; si le hasard donne aussi 7/8, le critère est mort.
4. Détecteur de progrès : paraphrases **avec perturbation numérique** de la valeur prédite, à classer « redite ».
5. Q2 : référence cible masquée dont le concept est **sous le seuil S31**, pour mesurer ce que la liste blanche interdit.

---

## Sur la proposition D

### (a) Défauts de méthode

**E1 (état versionné) — circularité étiquette/détecteur.** Un « progrès » est défini par D comme fermeture d'un trou par une pièce vérifiée ; l'état versionné contient précisément les champs « trous » et « pièces ». Les cas positifs seront étiquetés par la même définition que lit le détecteur : il détecte ce qu'il enregistre. Le témoin « diff de citations » détecte l'ajout d'une pièce aussi bien ; la seule classe discriminante (« ajout de citation sans effet ») exige un vérificateur de l'effet, qui est la lecture sur PDF — le détecteur se confond avec le vérificateur.

**E2 (moisson) — contradiction interne avec la porte de contamination.** L'issue est « précision en tête sur issues futures » ; D disqualifie lui-même toute rétrodiction générative avec un modèle non daté. E2 n'est donc exécutable qu'avec un proposeur mécanique, qui n'« affine » rien : E2 mesure une moisson sur un proposeur qui n'est pas celui de la boucle. De plus, la moisson ciblée change l'univers des paires candidates ; une précision en tête sur deux univers différents n'est pas le même estimand.

**E3 (bras) — témoin maximal réglé sur l'épreuve.** « Meilleur de {RA, Simpson, PA, lexical} » : si le meilleur est choisi sur l'épreuve, c'est un réglage sur l'épreuve (contradiction avec le protocole commun) ; si choisi sur un pré-échantillon, il faut le dire et fixer la correction.

**E4 (bandit) — récompense anticorrélée à la cible.** La récompense admissible est une transition vérifiée (trou fermé par une pièce existante). Les embryons dont les trous se ferment le plus vite par la littérature sont ceux **les plus proches de l'existant** : le bandit optimise contre la nouveauté. D traite le pire cas « nouveauté facile » mais pas cette inversion de signe. En outre, chaque récompense coûte une vérification sur PDF (R7), plus chère que le tour qu'elle est censée piloter.

**E5 / E6 — issue inexistante et coût manipulable.** L'AUC de survie suppose des survivantes ; l'observation servie est 0/20. « +25 % de survivantes par euro » dépend de la comptabilité des coûts (jetons, moisson, vérification Claude, tests de mort) : l'attribution des coûts fixes entre bras est un choix de conception qui décide du ratio. « Avantage nul en monde permuté » est défini pour des mondes synthétiques, pas pour des fiches réelles.

**Douane par date — fuite non bornée.** La douane « refuse issue future » par les dates ; OpenAlex (Walden) révise dates, types et résumés (Pièce 3 § 4.5). Sans tolérance déclarée, la douane est leaky de manière inconnue.

**E1 — planteur non aveugle.** Les « vraies fermetures de trous » sont fabriquées par qui connaît le schéma de l'état versionné.

### (b) Conditions de perte de puissance ou d'injugeabilité

- **E1.** Détection ≥ 80 % à 5 % de fausses alertes, +10 points sur le témoin ; effectif non fixé. Si le mélange de cas contient une part w de cas « ajout de citation » que le diff détecte à 100 %, le témoin vaut ≥ w et le plafond interdit +10 points dès w ≥ 0,9 : H_B vraie par choix du mélange. À ≈ 60 cas par classe, l'erreur-type d'une différence de taux vaut ≈ 0,07 (illustratif) ; 10 points ≈ 1,4 erreur-type.
- **E2.** +2 points de précision en tête à k = 1000 : erreur-type ≈ 0,0095 à p = 0,1 (illustratif), avant corrélation des têtes ; et estimand non comparable si l'univers des candidats diffère entre bras.
- **E3.** 3 bras × 3 types de paires = 9 comparaisons ; avec correction de Bonferroni, z ≈ 2,77 ; +2 points exigent une erreur-type ≤ 0,007, soit ≈ 1 800 éléments en tête par comparaison (illustratif). Sur 8 fusions par bras, injugeable.
- **E4.** Sous récompenses permutées, l'avantage attendu est 0 ± bruit ; une seule permutation ne donne pas la distribution nulle. Avec survivantes en comptes de Poisson λ_A, λ_B, détecter +20 % exige des centaines de survivantes par bras (illustratif) ; à s ≈ 0, injugeable.
- **E5.** AUC = 0,70 avec erreur-type ≈ 0,06 demande ≈ 20 positives (approximation usuelle, référence à vérifier) ; à survie 0/20, il faudrait plusieurs centaines de fiches testées pour obtenir 20 survivantes.
- **E6.** Rapport de deux comptes a, b : erreur-type du log-rapport ≈ √(1/a + 1/b) ; pour que +25 % vaille 2 erreurs-types, a ≈ b ≈ 160 survivantes (illustratif). Porte finale indécidable au volume d'une course.

### (c) Contrôles négatifs dont l'absence serait fatale

1. E1 : planteur **aveugle au schéma** ; paraphrases avec perturbation numérique ; cas « citation ajoutée à effet nul » étiquetés sur PDF par un lecteur distinct du détecteur.
2. E2 : **univers de candidats figé** avant moisson ; témoin lexical réglé sur pré-échantillon.
3. E3 : distribution nulle du **maximum des témoins** par permutation (le max est un test à α inconnu).
4. E4 : ≥ 100 permutations de récompenses ; **allocation oracle** (qui connaît les survies) pour mesurer la marge disponible — si l'oracle ne dépasse pas +20 %, H_B est vraie par construction.
5. E5/E6 : témoins **vrais non tautologiques** passés aux tests de mort *avant* toute lecture (D le dit, mais en annexe de (c), non comme préalable bloquant) ; une fiche **déjà publiée** (doit survivre et être tuée par l'antériorité) pour séparer « survit » de « nouveau » ; comptabilité des coûts gelée avant lecture.

---

## Ce que je retiens pour le tour suivant (sans fusion)

Trois points de rupture distincts, un par proposition : B calibre le moissonneur sur ce que la boucle doit éviter (c1 contre Exp. 1) ; C rend « sans repli » et « progrès » vrais par construction (E3, tuple numérique) ; D fait reposer ses portes finales sur une issue (survie) dont l'observation servie est nulle, à des effectifs où ses propres seuils relatifs sont indécidables. Aucune des trois ne fournit l'estimateur de la variance inter-graines ni l'appariement degré/âge comme préalable bloquant.

FIN-DE-CELLULE