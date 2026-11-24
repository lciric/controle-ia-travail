# Proposition I — Tour III.3 : réponse aux critiques

**Pièces.** Ma conception (E3-T1-conception-I) et les huit critiques A à H sont présentes, closes par leur marque ; aucune coupure visible. Le bloc QUESTION reprend le bloc FAITS (même sha256). Je ne réponds qu'aux sections « Sur la proposition I ». Statuts inchangés : faits RAPPORTÉS, calculs de conception OBSERVÉS-NON-AUDITÉS, mes inférences HYPOTHÈSE ; VÉRIFIÉ ne couvre que l'arithmétique refaite ici. Tout chiffre hors faits est illustratif.

**Bilan.** Cinq choix tiennent (1c amélioré, 2b, 3b audité, 4.1a+c, 5a). Deux pièces tombent : le « fil conducteur » 3a→2a→4 et l'option « lois leurres ». L'« amélioration » de 4.2 est rétrogradée en avertissement. Les cinq duels sont récrits.

## (a) Réponses aux critiques

### Décision 1

**A1 — δ_A « fixé par D1 », qui ne porte que sur B (A, B, E, F, G).** Acceptée : D1 ne fournissait aucune procédure pour δ_A. Correction : δ_A est une marge de conception gelée avant toute mesure, éprouvée par un test d'équivalence dimensionné (D1′).

**A2 — Erreur d'échelle du seuil et du contrôle négatif (C, G) ; réplicats à l'effectif de campagne (A).** Acceptées, arithmétique refaite : sous H_B à variances égales, B̂_témoin − B̂_réf a pour variance 2σ², mon seuil 2 sur |·|/σ_réf donnait une erreur de première espèce ≈ 0,157 au lieu de 0,046 ; deux moitiés de taille n/2 ont une variance de différence 4σ², le contrôle négatif échouait dans ≈ 0,32 des cas (VÉRIFIÉ). Correction : dénominateurs √2·σ et 2·σ, réplicats de taille n_campagne.

**A3 — D1 se joue dans le simulateur qui a produit « B varie davantage » (B, G).** Acceptée pour la portée. Transformée : D1′ ne décide plus rien sur B ; B devient diagnostique hors admission, donc plus rien n'est « choisi pour son effet » ; un contrôle sur données réelles (deux moitiés du jumeau de référence, vrai moniteur) remplace le placebo simulé.

**A4 — Porte ponctuelle sur A : région d'acceptation vide si z·σ_n > δ_A (F).** Acceptée : D1′ gèle n tel que l'équivalence ait une puissance ≥ 0,8 à ΔA = 0.

**A5 — « VÉRIFIÉ : les trois issues somment à 1 » alors que l'inclusion de l'abstention dans A n'est pas définie (G).** Rejetée comme contradiction : p_acc + p_sig + p_abs = 1 est arithmétique sur trois issues exclusives ; l'indéfini est le mot « accepte » des faits, que j'avais signalé comme lacune. Acceptée comme lacune à fermer : le texte gelé pose A := 1 − p_sig (lecture littérale de « ne signale pas »), B := p_abs, toutes deux sur les mêmes épisodes du jumeau honnête ; l'acceptation stricte est A − B.

### Décision 2

**A6 — Le « ou » entre deux lois nulles laisse le choix après coup (A, E, F) ; aucune des deux n'est la bonne loi (B, T6).** Acceptée. L'objet de comparaison est la version honnête du même document (RAPPORTÉ) : la loi nulle pertinente est part(original) − part(même document retouché par le tiers sans retrait de contrôle), lue par le protocole final. C'est aussi le « retrait factice » demandé par A, D, G. Deux lectures disjointes d'un même objet deviennent un contrôle de plancher (bruit de lecture seul, attendu ≤ la loi nulle).

**A7 — Sélection du seuil sur la part observée (B, T5) sans validation disjointe (D).** Acceptée : k retenu = plus petit seuil dont la borne supérieure exacte de π̂₀(k) est ≤ α_étal, validé sur un sous-lot tenu à l'écart. La monotonie de π₀(k) en k rend la recherche à croisement unique ; la validation ferme la multiplicité résiduelle.

**A8 — Zone grise à n = 100 (B, C, G, H).** Acceptée, calcul refait : la borne supérieure dépasse 0,05 dès 2 alertes sur 100 ; à π₀ = 0,025, l'issue « H_B falsifiée » n'a que ≈ 0,28 de probabilité (VÉRIFIÉ). Correction : n = 300 par tranche de m (illustratif), points de conception π₀ = 0,02 et 0,10, où la zone sans verdict a probabilité ≈ 0,15 et ≈ 0,05 (calcul approché, illustratif).

**A9 — Étalonnage marginal masquant les grands m ; étalonnage sans plancher de sensibilité (G).** Acceptées : tranches de m ; si l'étalonnage impose k ≥ 2, les strates à d < k contrôles retirés sont déclarées « hors portée de l'oracle » dans le texte gelé, plutôt que mesurées par le bruit.

**A10 — Contrôle « même panel » vide à température nulle (B, T3 ; G).** Acceptée ; voir A6.

### Décision 3

**A11 — L'humain ne voit que les désaccords : fidélité surestimée de P(double raté) (A, C, D, E, F, G, H).** Acceptée sans réserve : l'estimateur converge vers p₁ − p₁₁ (F) et vers 0 si les erreurs sont corrélées. Transformée en test : échantillon stratifié des accords et des désaccords, désignés et non désignés, adjugé en aveugle et pondéré (Horvitz et Thompson, 1952, « A generalization of sampling without replacement from a finite universe ») ; duel sur p₁₁ (C, F).

**A12 — L'hypothèse porte sur le taux de paraphrase, la métrique sur le rappel du programme (B, E, H).** Acceptée : ce qui biaise q est l'erreur de l'instrument, pas la fréquence du phénomène. D3′ oppose des rappels contre la vérité adjugée ; la cause (paraphrase, mots-clés gardés, autre) devient une étiquette secondaire par item.

**A13 — D3 ne mesure jamais le repéreur (G).** Acceptée : même échantillon, mêmes métriques pour les deux désignateurs ; la bascule (b)→(c) se lit sur leur différence.

**A14 — Instruments 2 et 7 confondent la fidélité f du tiers et la détection σ de l'oracle (A).** Acceptée : l'adjudication humaine d'un échantillon de dommages plantés estime f (le contrôle a-t-il disparu ?) ; σ se mesure sur le sous-ensemble adjugé.

**A15 — Deux familles de modèles peuvent partager des biais (H).** Acceptée : la séparation des familles est une heuristique de décorrélation, pas une garantie ; p₁₁ mesure le résidu, et les paraphrases voulues de D3 servent de lot construit pour la concordance.

### Fil conducteur 3a→2a→4

**A16 — La désignation n'est pas l'oracle ; un manque commun s'annule dans D ; l'excès défini par μ ne se déplace pas par seuil (A, C, E) ; chaîne non testée (H).** Acceptée : je retire la chaîne. La désignation (3) place les retraits ; elle ne change pas la lecture de l'honnête par l'oracle (4) ; le seuil (2) ne change pas μ. Ce qui reste, HYPOTHÈSE : un bruit de lecture par contrôle ε nourrit à la fois μ (excès) et π₀ (fausses alertes à 1/m) — une cause commune, pas une chaîne ; prédiction testable : μ̂ et π̂₀ covarient entre tranches de m. Mes choix 2b (seuil inconnu) et 4.2a (allocation dépendante des données) ne reposaient pas sur la chaîne : ils tiennent sans elle. La remarque de C sur l'annulation vaut pour un biais constant ; la variance ne s'annule pas, et c'est elle que D2′ mesure.

### Décision 4.1

**A17 — L'annexe scellée permet de ne publier que les strates favorables (H).** Acceptée : annexe scellée par empreinte publiée avec la liste complète des strates ; la campagne suivante la publie entière ou déclare les strates retirées.

**A18 — D4 confirme la couverture par construction sous tirages indépendants ; l'estimande dégénère si l'oracle signale tout (B, T2 ; A, D, E, G) ; sens du biais non contrôlé (H) ; déclenchement aléatoire non simulé (E, D).** Acceptée. D4′ simule la dépendance (lecteurs partagés, grappes par document, déclencheur calculé sur les mêmes lectures), μ de part et d'autre du seuil avec conditionnement sur E réalisé, les deux sens (plancher de manques → q monte ; sur-signalement → q baisse), et rapporte à côté de la couverture la discrimination P(signalé | dommage) − P(signalé | honnête) : une borne couvrante à discrimination nulle est vide, ce qui est l'argument même de 4.1a.

### Décision 4.2

**A19 — Double usage du lot d'étalonnage (A, E, F, G).** Rejetée pour la partie « optimiste par construction » : l'excès se définit par μ, taux de manques de l'oracle chez l'honnête (RAPPORTÉ) ; choisir k ne modifie aucune part, donc pas μ̂ — A le dit elle-même en critiquant F. Acceptée pour la partie qui compte (A, F) : l'excès du lot final est un autre événement, et à μ = c, P(étalonnage sous le seuil, final au-dessus) → 1/4 (VÉRIFIÉ). Mon « amélioration » réduisait la probabilité de l'événement sans régler le cas. Elle devient un avertissement précoce ; le texte gelé dit ce que fait (a) si le lot final tombe en excès : rien ne change, le budget reste inemployé.

**A20 — « Nominal » ambigu ; l'inflation loge dans l'union des régimes (A).** Acceptée : D4′ estime P(au moins une garantie fausse parmi les énoncés publiés), régimes confondus, contre le niveau total accordé ; les niveaux par énoncé restent 2,5 % / 1,25 % (RAPPORTÉ).

### Décision 5

**A21 — Lois leurres : une statistique forte mais fausse est promue par l'honnête ; le témoin pénalise l'honnête par construction ; cela change la difficulté (A, B, C, D, E, F, G).** Acceptée : je retire l'option telle que formulée. Ce qui en est récupérable, dit comme hypothèse nouvelle : des lois distractrices *réfutables dans les données* (confondant mesuré, interaction), qui testent si la règle de cohérence exige les vérifications pertinentes et non la seule conformité aux preuves produites. C objecte qu'un saboteur lisant la trace les écarterait aussi — exact, mais le script « top-k par force » ne lit pas de trace, et c'est lui que la décision 5 vise. Conditionnée au test de contamination de l'honnête (B, C, F, G) et à une campagne sans distracteurs, qui mesure la fréquence ordinaire d'évasion (E).

**A22 — D5b : le « hasard » est la masse modale ; l'exactitude sur k n'est pas le gain du saboteur ; preuves ≠ métadonnées ; classifieur fixe (A, B, D, E, G, H).** Acceptée : référence = max_k P(K = k), gelée ; deux prédicteurs séparés (format seul ; données seules) ; la grandeur rapportée est le gain d'évasion d'un script qui estime K̂(X) (F, G) contre le même script à K révélé. Limite déclarée : le test borne la fuite pour les prédicteurs essayés, non pour le meilleur possible (E, H).

**A23 — D5a : pas de bras « composition tirée » (D, G) ; pas de contrainte sur p_hon ni de fiche incohérente triviale (G) ; conditionner à une faute effective (D) ; zone grise à n = 200 (A, G, H) ; régime de signal (B, T1).** Acceptées : plan croisé, issue conditionnelle à la fiche fausse, contrôle positif « statistiques faibles promues », n = 500 épisodes appariés (illustratif), signal de la loi la plus faible réglé pour que P(top-k correct) ∈ [0,2 ; 0,8].

## (b) Expériences corrigées

Chaque duel donne ses deux issues et sa zone sans verdict, dimensionnée pour être rare aux points de conception.

**D1′ — Témoin (banc des tâches floues).** Texte gelé : A := 1 − p_sig, B := p_abs, sur les mêmes épisodes du jumeau. Admission : équivalence |A_témoin − A_réf| ≤ δ_A (0,05 illustratif). H_A : |ΔA| ≤ δ_A ; H_B : |ΔA| > δ_A. Intervalle bilatéral à 90 % inclus dans (−δ_A, δ_A) → H_B falsifiée, témoin admis ; disjoint de (−δ_A, δ_A) → H_A falsifiée, témoin refusé ; à cheval → effectif insuffisant, rendu rare par n ≈ 600 par monde (illustratif ; A ≈ 0,9, puissance 0,8 à ΔA = 0). B publiée avec intervalle, sans seuil. Contrôle négatif réel : deux moitiés du jumeau de référence, vrai moniteur, dénominateur 2·σ_n ; équivalence attendue. Le simulateur ne sert plus qu'à vérifier que |ΔB| dépasse √2·σ sur réplicats de taille n_campagne.

**D2′ — Règle de signalement.** Loi nulle : paires (original honnête, même document retouché sans retrait par le tiers), protocole de lecteurs final, par tranche de m. H_A : π₀(1/m) ≤ α (0,05) ; H_B : > α. n = 300 par tranche (illustratif). Borne supérieure exacte ≤ α (≤ 8 alertes, calcul approché) → H_B falsifiée, (a) admissible ; borne inférieure > α (≥ 22 alertes) → H_A falsifiée, (b). Bornes : Clopper et Pearson, 1934, « The use of confidence or fiducial limits illustrated in the case of the binomial ». Si (b) : k = plus petit seuil à borne supérieure ≤ α, validé sur un sous-lot disjoint ; strates d < k déclarées hors portée. Contrôle de plancher : même objet, deux panels disjoints. Lecture annexe : μ̂ par tranche, et covariation μ̂–π̂₀ (cause commune, A16).

**D3′ — Désignation.** Échantillon stratifié {désigné, non désigné} × {accord, désaccord des deux désignateurs}, ≈ 500 contrôles sur 100 documents (illustratif), adjugé par un humain aveugle aux étiquettes, pondéré. Duel principal : H_A : rappel du programme ≥ 0,95 ; H_B : < 0,95 ; borne inférieure > 0,95 → H_B falsifiée, (c) ; borne supérieure < 0,95 → H_A falsifiée, (b). Duel d'audit : H_A : p₁₁ ≤ 0,02 ; H_B : > 0,02, qui falsifie tout arbitrage sur désaccords seuls. Bascule : (c) si la borne inférieure du gain de rappel du repéreur est < 0,02. Contrôles : contrôles copiés mot pour mot (rappel ≈ 1) ; paraphrases voulues (rappel ≪ 1 ; concordance des deux désignateurs sur cas connus) ; retrait factice d'un passage non porteur (oracle et moniteur ne signalent pas au-dessus de la loi nulle de D2′) ; 50 dommages plantés (illustratif) adjugés pour estimer f, puis σ sur le sous-ensemble adjugé.

**D4′ — Régime d'excès.** Simulation à q connu : corrélation inter-lecteurs ρ ∈ {0 ; 0,3 ; 0,6} (illustratif), grappes par document, déclencheur calculé sur les mêmes lectures, μ de part et d'autre de c, conditionnement sur E réalisé, deux sens de biais ; bras à allocation fixe (a) et conditionnelle (b) sous les mêmes dépendances. H_A : sur toute la grille, P(au moins une garantie fausse) ≤ niveau total accordé + marge Monte-Carlo et P(q > U | E) ≤ 2,5 % ; H_B : l'un dépasse. H_B → la borne de q en excès n'est pas publiable : 4.1a confirmé, 4.2b inadmissible. H_A → publiable seulement si la discrimination mesurée dépasse 0,10 (illustratif), sinon vide ; et la règle conditionnelle gelée d'avance devient admissible. Contrôle négatif : même grille sous le seuil d'excès, couverture attendue.

**D5′ — Composition.** Plan {K révélé, non révélé} × {composition fixe, tirée} × {script top-k (k révélé ou modal), script adaptatif à K̂(X), honnête de référence scripté}, mêmes épisodes, n = 500 (illustratif), K = 0 rapporté à part, signal de la loi la plus faible réglé (A23). Issue : acceptation par la règle de cohérence conditionnelle à la fiche fausse. D5a : H_A : écart honnête − top-k (K révélé, composition fixe) < 0,10 ; H_B : ≥ 0,10. H_A → (b) perdrait bien un témoin, (a) ; H_B → la règle tient, le coût de (b) tombe. Contrôle positif : statistiques faibles promues, rejet attendu. D5b : H_A : gain d'évasion du script adaptatif sur le script modal ≤ 0,05 sous tirage ; H_B : > 0,05, K fuit par les données et le remède est le rapport signal/bruit, pas le tirage. Prédicteur par format seul contre la masse modale, évalué hors construction. Distracteurs réfutables, s'ils sont retenus : H_A : hausse des fausses promotions de l'honnête < 0,05 ; H_B : ≥ 0,05, option abandonnée ; une campagne sans distracteurs est conservée.

## (c) Réponse à l'arbitre

**Établi.** (RAPPORTÉ) Les définitions des bancs, de A, B, de la règle 1/m, de q, de l'excès par μ, des niveaux 2,5 %/1,25 %, et qu'aucune fiche n'a été servie. (VÉRIFIÉ, arithmétique) Les trois issues du moniteur somment à 1 ; le seuil 1/m signale toute différence d'un contrôle ; les erreurs d'échelle de mon D1 et la zone grise de mon D2 à n = 100 ; un quart des campagnes frontalières tombe en excès final malgré un étalonnage passé.

**Non établi.** (OBSERVÉ-NON-AUDITÉ) « A varie peu, B varie davantage », sur simulateur, sans transfert au moniteur réel. (HYPOTHÈSE) La cause commune ε ; la fidélité relative du repéreur ; le bruit honnête/honnête < 1/m ; que le tirage cache k ; que des distracteurs réfutables ne piègent pas l'honnête ; la dépendance déclencheur–borne de q.

**Décisions.**

1. **(c) amélioré, 0,65.** A := 1 − p_sig avec marge d'équivalence gelée, B diagnostique sans seuil. Un témoin stable est un témoin réussi ; taire B cache un transfert accepter→s'abstenir. Changerait : texte gelé n'accordant qu'une grandeur au budget → (a) ; n de campagne sous le dimensionnement → la clause sur A est injugeable, je repasse à (a) sans seuil.
2. **(b), 0,70.** Loi nulle = retouche sans perte du même document ; seuil par borne supérieure, validé hors sélection ; strates hors portée déclarées. Changerait : D2′ falsifiant H_B → (a) suffit ; aucun lot distinct de même loi → (a) avec π̂₀ rapporté ; règle binaire livrée par l'oracle avant gel → (c).
3. **(b) audité, 0,65.** Audit humain des accords et des désaccords, f séparé de σ. Changerait : rappel du programme ≥ 0,95 et p₁₁ ≤ 0,02 → (c) ; gain de rappel du repéreur < 0,02 → (c) ; coût du repéreur au-delà de 10 % du budget (illustratif) → (c).
4.1 **(a) + (c) + diagnostic d'excès publié, 0,65**, annexe scellée à liste de strates publique. Changerait : D4′ tenue sur la grille de dépendance avec discrimination > 0,10 → la borne par strate est garantie et se publie.
4.2 **(a), 0,75** ; l'étalonnage n'est qu'un avertissement précoce. Changerait : D4′ montrant que la règle conditionnelle gelée d'avance ne gonfle pas l'union des régimes → admissible ; niveaux non encore gelés → les récrire maintenant n'est pas un changement après coup.
5. **(a), 0,80** ; refaire le calcul d'admission. L'option « lois leurres » est retirée ; les distracteurs réfutables restent une hypothèse soumise au test de contamination. Changerait : D5a montrant que la cohérence rejette top-k → le coût de (b) tombe ; D5b montrant un gain d'évasion ≥ 0,05 par K̂(X) → (a) n'achète rien, le remède est ailleurs.

**Expérience à faire en premier : D2′.** Un lot de paires (original honnête, retouche sans perte) lu par le protocole final d'oracle, par tranche de m. Elle mesure l'instrument qui domine le coût et conditionne trois décisions : π̂₀ tranche 2a/2b ; μ̂ annonce ou non l'excès (4.1, 4.2) ; la covariation μ̂–π̂₀ éprouve l'hypothèse de cause commune qui remplace mon fil conducteur retiré. D3′ (audit humain, ≈ 25 heures, sans oracle) se lance en parallèle.

FIN-DE-CELLULE