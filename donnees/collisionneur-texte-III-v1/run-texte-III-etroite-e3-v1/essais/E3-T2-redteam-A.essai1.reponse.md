# Proposition A — Tour III.2 : critique croisée de méthode

Périmètre tenu : lois de capture, de dépendance, d'hétérogénéité et d'échec ; aucune famille, aucun comportement d'agent. Les pièces B, C et D sont reçues complètes (chacune se termine par sa ligne de fin). Les chiffres qui ne viennent pas des faits sont illustratifs ou issus de recalculs dont la formule est donnée.

## Recalculs servant aux trois critiques (refaisables ; données RAPPORTÉES, fait 17)

R1. Point fixe du modèle d'indépendance : N̂ résout N(1 − ∏(1 − n_j/N)) = 37. Avec N = 39,22 : p̂ = (0,561 ; 0,586 ; 0,688), ∏(1 − p̂) = 0,0566, N(1 − 0,0566) = 37,00. Avec N = 38,91 (valeur de C), on obtient 36,8 ≠ 37 : la valeur de C n'est pas le maximum de vraisemblance conditionnel ; celle de D (39,22) l'est.

R2. Déviance G² du cas A (17 recaptures sur la paire des sources 2 et 3, cellules 14, 2, 2, 3, 4, 4, 8) avec les attendus du point fixe (8,88 ; 4,02 ; 6,26 ; 6,95 ; 2,84 ; 3,15 ; 4,90) : G² = 12,85. Cela concorde avec D (12,85), pas avec C (12,904). Je n'ai pas recalculé les cas B et C, pour lesquels C et D donnent des valeurs différentes (13,20 contre 13,36 ; 14,22 contre 14,63) : au moins une des deux pièces se trompe sur ces deux cas.

R3. Trois valeurs sont appelées « borne de Chao » : 55,29 (B et C, sans facteur (T−1)/T), 49,19 (D, facteur 2/3), 47,00 (C, variante à biais corrigé). L'étendue (8,3 familles) est du même ordre que le nombre de familles inconnues qu'elles estiment (10 à 18). Le choix de variante n'est donc pas un détail de présentation.

R4. Sensibilité du modèle à trois interactions de paire (C : N̂ = 186,3 dans le cas A) : déplacer une seule famille d'une cellule simple vers la cellule double (2 → 3) donne n̂₀₀₀ = 14·4·4·8/(3·2·3) = 99,6 et N̂ = 136,6. Une unité de comptage déplace l'estimation de 50 familles.

R5. Signature de la distribution des captures : sous indépendance homogène à p ≈ 0,6, la loi conditionnelle du nombre de captures vaut environ (0,29 ; 0,43 ; 0,22) pour 1, 2, 3 ; observé : (0,43 ; 0,19 ; 0,38). Cette forme en U est produite aussi bien par un mélange de probabilités de capture que par une dépendance positive homogène : avec trois sources, les deux mécanismes ne sont pas séparables par les sept comptes. Ce point frappe les trois pièces.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Sens inversé de la déviance.** B écrit que l'affectation « qui maximise la déviance » place 17 sur la paire la plus attendue (sources 2 et 3). C'est l'inverse : placer la plus grande recapture sur la paire dont l'attendu est le plus grand réduit l'écart, donc la déviance ; R2 et les calculs de C et D donnent cette affectation comme minimum (12,85). B laisse le calcul « à la simulation » alors qu'il est fermé et refaisable.

2. **Formule de Chao mal attribuée et mal choisie.** B applique f₁²/(2f₂) sans le facteur (T−1)/T et cite « Chao, 1987 » ; la formule sans facteur est celle de la référence 1984 (abondance), la référence 1987 porte le facteur pour T occasions. Pour trois sources, omettre le facteur relève la « borne inférieure » de 6 familles (R3) : si N vaut 50 (illustratif), 55,3 n'est plus une borne inférieure.

3. **Fuite entre instrument et évaluation dans le bloc 2.** B applique n_eff = n/(1 + (n−1)ρ) aux 37 familles énumérées, puis en déduit ε ≤ 0,31. Deux erreurs : (i) les 37 sont l'inventaire du bloc 3, pas l'échantillon testé du bloc 2 ; (ii) le facteur de plan corrige la variance d'une moyenne, pas la probabilité d'un événement « zéro échec sur n » sous corrélation échangeable. Sous une loi bêta-binomiale de moyenne ε et de corrélation ρ, P(0 échec) tend vers 1 − ε quand ρ → 1, quel que soit n ; (1 − ε)^{n_eff} ne reproduit pas ce comportement. Le chiffre 0,31 n'est pas dérivé.

4. **Règle d'arrêt à niveau non contrôlé.** « Continuer jusqu'à ce que la borne supérieure soit < ε₀ ou que la largeur stagne » est un arrêt optionnel sans dépense d'α : le niveau réel dépasse α par construction, et d'autant plus que le nombre de regards est grand.

5. **Sélection de modèle sans incertitude de sélection.** Choisir par AIC/BIC parmi six modèles à 1 ou 2 ddl, avec des cellules doubles valant 2 ou 3, puis rapporter l'IC du modèle retenu, exclut la variance due au choix ; R4 montre l'ordre de grandeur de ce qui est omis.

6. **Duel 1 non exclusif.** H_A : couverture ≥ 0,95 ; H_B : couverture < 0,85. La zone 0,85–0,95 ne falsifie rien. L'« estimateur ajusté (Chao puis tirage pondéré) » de H_B n'est pas défini : l'issue qui le concerne n'est pas jugeable.

7. **Confrontation 1 confondue.** Prédire (N̂ − 37)/N̂ = 0,33 pour la part nouvelle d'une source extérieure suppose que cette source capture uniformément dans la population. Sous hétérogénéité, les familles non vues sont celles de faible probabilité de capture : la part nouvelle observée sera inférieure à 0,33 même si N̂ est exact. Une part basse ne falsifie donc pas N̂ ; elle est attendue. B ne distingue pas la prédiction « uniforme » (1 − 37/N̂) de la prédiction « pondérée par la capture » (Good-Turing, 0,22).

### (b) Conditions de perte de puissance

- Chao : si la dépendance positive est assez forte pour que f₁ → 0, la borne se réduit à 37 quel que soit N ; si f₂ → 0 elle diverge. Avec f₁ = 16 et f₂ = 7, une fusion à tort qui déplace deux singletons dans une cellule double fait passer f₁²/(2f₂) de 18,3 à 12,3 (calcul refaisable) : l'estimation est pilotée par quelques comptes.
- Good-Turing avec M = 72 : sous dépendance positive, les 14 triplets gonflent M sans information nouvelle ; Ĉ est surestimé, et la part nouvelle prédite (0,22) est sous-estimée pour toute source extérieure moins corrélée aux trois premières.
- Borne zéro échec sous corrélation échangeable ρ entre indicateurs d'échec : il existe un ρ critique, fonction de n, au-delà duquel P(faux certificat | π = ε) reste au-dessus de α pour tout n. La règle devient non jugeable, pas seulement moins puissante.
- Confrontation 2 (test de Fisher sur 20 familles extérieures, δ = 0,10) : à π = 0,05, l'écart-type d'une différence de proportions sur 20 contre 37 familles vaut environ 0,06 (illustratif) ; l'écart de 0,10 n'est détecté qu'avec une puissance faible, et l'absence de rejet ne vaut pas validation.

### (c) Contrôles négatifs dont l'absence serait fatale

- Monde où la forme en U de (f₁, f₂, f₃) est produite par hétérogénéité pure sans dépendance, et monde symétrique à dépendance pure : si la sélection AIC/BIC ne les distingue pas (R5 dit qu'elle ne le peut pas), le critère de choix de B est caduc.
- Monde à dépendance négative entre sources avec déviance ≈ 12,9 : les estimateurs doivent alors surestimer N ; sinon le sens des « effets directionnels » de B n'est pas établi.
- Monde à censure commune : N_vis < N connu ; l'IC de B doit couvrir N_vis et ne jamais prétendre couvrir N.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Erreurs de calcul.** N̂_ind = 38,91 n'est pas le point fixe (R1) ; G² = 12,904 n'est pas la déviance du cas A sous le maximum de vraisemblance (R2 donne 12,85). L'identification du cas A tient quand même, mais pour une raison que C ne contrôle pas : l'écart entre cas A et cas B (0,3 à 0,5 unité selon la pièce) est du même ordre que l'écart entre deux variantes de calcul (G² contre X² de Pearson, vraisemblance conditionnelle contre Poisson non conditionnel). L'identification n'est robuste que si la statistique rapportée « 12,9 » a été calculée exactement de la façon supposée, ce qui n'est pas dans les faits.

2. **Incohérence sur le modèle saturé.** Le duel 1 parle d'un « modèle log-linéaire saturé à 6 paramètres » ; le bloc 3 donne, correctement, 7 paramètres et 0 ddl. L'estimateur mis en duel n'est pas identifié.

3. **Nomenclature de Chao.** « Chao1 corrigée pour T = 3 » est la forme pour données d'incidence (Chao2) ; le point 55,29 présenté comme Chao1 ignore le facteur 2/3 pourtant utilisé trois lignes plus bas. C rapporte 55,3, 47,0 et 47,6 côte à côte sans dire laquelle est préenregistrée.

4. **Contrôle négatif mal formulé.** Exiger que la borne inférieure de Chao atteigne « 95 % ± 1 % » sous M₀ est une erreur de critère : une borne inférieure doit vérifier P(N ≥ L) ≥ 0,95, et elle est en général au-dessus (biais vers le bas sous M₀). Le contrôle rejetterait un générateur sain.

5. **Signe de u₁₂₃ affirmé sans dérivation.** C écrit que l'hétérogénéité « crée u₁₂₃ > 0 » et fait exploser le modèle saturé vers le haut. Sous un mélange de captures indépendantes, les interactions de paire sont positives ; le signe de l'interaction d'ordre trois dépend de la loi de mélange (Darroch, Fienberg, Glonek et Junker, « A three-sample multiple-recapture approach to census population estimation with heterogeneous catchability », référence à vérifier). Le sens du biais de N̂_sat sous hétérogénéité est un résultat du plan de simulation, pas une prémisse.

6. **Seuil intra-famille sans son coût.** Le critère P(Y ≤ c | θ > τ) ≤ β_intra n'est défini qu'à la frontière θ = τ ; pour m = 100 et τ = 0,05 (illustratif), c = 1 satisfait β = 0,037, mais une famille saine à θ = 0,02 est déclarée en échec avec probabilité 0,60 (calcul binomial refaisable). La borne à zéro échec devient alors inatteignable sur des familles saines : la puissance tend vers zéro. Ni la formule n ≈ ln α / ln(1 − ε(1 − β)) × VIF, ni le facteur VIF multiplicatif (même objection qu'à B, point 3) ne sont dérivés.

7. **Trois règles d'arrêt empilées.** SPRT, frontière de Pocock et martingale (1 − ε)^{−t} sont des procédures distinctes aux garanties distinctes ; la martingale citée n'est un supermartingale sous H₀ que si les succès sont indépendants, ce que le bloc 2 nie. Il faut en préenregistrer une.

8. **Validation du bloc 3 confondue.** La prédiction K_nouv ∈ [6 ; 19] et la falsification à K_nouv ≥ 20 reposent sur un estimateur de Petersen entre une union de trois sources et une source extérieure, donc sur homogénéité de capture et indépendance. C invoque lui-même l'hétérogénéité comme explication du U ; sous hétérogénéité, K_nouv/30 ≈ 1 − Ĉ = 0,22 quel que soit N, et la confrontation ne sépare pas N ≈ 47 de N ≈ 186. C l'entrevoit (« ou censure commune levée ») mais scelle quand même une issue qui ne discrimine pas.

### (b) Conditions de perte de puissance

- Modèle à trois interactions de paire : lorsque le produit des cellules doubles est petit (ici 12), la variance de n̂₀₀₀ domine tout (R4) ; l'IC devient non informatif, et l'estimation n'est pas jugeable contre Chao.
- Modèle quasi-symétrique / Rasch à 1 ddl : non identifiable séparément d'une dépendance positive homogène avec trois sources (R5) ; la composante de variance σ² absorbe indifféremment les deux mécanismes.
- Duel 1 : « reproduire la déviance 12,9 » ne fixe pas le rapport de cotes ψ (plusieurs couples (ψ, CV) la reproduisent) ; le monde de simulation n'est pas défini de façon unique.
- Définition retenue P_écart : si la partition vues/écart est échangeable, P_écart = P_vues et l'énoncé n'ajoute rien à l'option 3 ; si elle ne l'est pas, P_écart n'est pas déclarée. Dans les deux cas, la « loi d'échantillonnage P » exigée en déclaration préalable n'existe pas pour des familles découvertes.

### (c) Contrôles négatifs dont l'absence serait fatale

- Monde hétérogène où le signe de u₁₂₃ est mesuré sur la table complète (cellule 000 incluse) avant tout ajustement : nécessaire pour juger l'affirmation 5.
- Monde à dépendance positive pure (CV = 0) produisant un U identique à celui du fait 17 : la méthode de C doit alors donner le même N̂ que sous hétérogénéité pure, ou déclarer l'indécidabilité.
- Monde où toutes les familles sont saines (π = 0) avec m = 100 : mesurer la fréquence à laquelle la règle intra-famille déclare un échec ; si elle dépasse 1 − (1 − ε)^{1/n} par famille (illustratif), la certification est impossible par construction.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Incohérence entre définition et validation.** Le bloc 1 retient π ≤ ε ; le bloc 4 scelle « zéro échec sur 59 familles extérieures » et « tout échec falsifie ». Pour une défense satisfaisant la définition avec π = 0,02 (illustratif), P(au moins un échec sur 59) = 1 − 0,98^59 ≈ 0,70 : la prédiction scellée rejette sept fois sur dix une défense conforme à la définition retenue. Ce qui est testé n'est pas ce qui est défini.

2. **Hypothèse qui rend la validation vraie par construction.** « 59 familles extérieures à probabilités d'inclusion connues, indépendantes des trois sources » suppose exactement le tirage i.i.d. que le fait 9 exige et que le bloc 2 de D déclare non satisfait pour des familles découvertes. Si cette hypothèse est accordée à la source extérieure, la borne du fait 9 est valide par hypothèse, et la confrontation ne teste plus rien de la découverte.

3. **Modèle génératif non spécifié.** La loi de découverte D, la forme de la corrélation inter-familles et la loi des q_f ne sont pas données ; la variance σ_B²/n + σ_W²/(n m_f) est correcte mais générique. Un tiers ne peut pas reconstruire les mondes, donc pas recalculer n.

4. **Duel 1 : multiplicité non contrôlée.** H_B est « au moins un monde de la grille sous 90 % ». Sans fixer la taille K de la grille et le nombre de réplications par cellule, la probabilité qu'une cellule tombe sous 90 % par fluctuation Monte Carlo croît avec K ; à 10 000 réplications l'erreur standard d'une couverture de 0,95 est 0,002 (illustratif), ce qui est tolérable, mais D ne fixe pas ce nombre. D reconnaît que la zone 0,90–0,95 ne départage pas, ce qui est honnête mais laisse le duel sans issue sur une partie du domaine.

5. **Confrontation « Inconnues » sans puissance entre les hypothèses d'intérêt.** La part nouvelle prédite 1 − 37/49,19 = 24,8 % suppose une source extérieure uniforme sur la population accessible. La prédiction concurrente par Good-Turing est 22,2 % ; sous hétérogénéité, un N bien plus grand prédit aussi une part proche de 22 %. L'écart-type de la part observée sur 30 familles (illustratif) est d'environ 0,08 : la confrontation ne distingue ni Chao de Good-Turing, ni « N ≈ 49 » de « N grand mais faiblement capturable ». D l'admet en une phrase (« teste surtout le transport ») sans en tirer la conséquence : la prédiction scellée doit porter sur la couverture, pas sur N.

6. **« Intervalle de transport »** (duel 2) non défini : la statistique, sa loi de référence et son recalcul ne sont pas donnés ; l'issue n'est pas jugeable.

### (b) Conditions de perte de puissance

- Chao avec facteur 2/3 (49,19) : mêmes conditions qu'à B (f₁ → 0 sous dépendance positive forte ; f₂ → 0). D ajoute à raison que l'effet d'une scission à tort sur Chao est ambigu ; je le confirme par calcul refaisable : scinder une famille vue deux fois augmente f₁²/f₂ ; scinder une famille vue trois fois en (2,1) le fait passer de 256/7 = 36,6 à 289/8 = 36,1. C surestimait donc l'« explosion quadratique ».
- Couverture de Good-Turing : D note correctement qu'elle porte sur la masse de capture ; la condition qui la rend trompeuse est la même qu'à B (gonflement de M par les triplets sous dépendance positive).
- Règle séquentielle « par lots préenregistrés avec dépense d'α » : correcte dans l'énoncé, mais sous corrélation échangeable entre familles, la fonction de dépense calibrée sous indépendance ne contrôle plus α ; la recalibration par simulation est annoncée, pas spécifiée.
- Validation « Nombre nécessaire » : mesurer la couverture de π en « répétant la règle » sur une population extérieure finie entièrement mesurée est un rééchantillonnage interne de cette population, pas une confrontation à une donnée nouvelle ; la puissance dépend du nombre de répétitions, non fixé.

### (c) Contrôles négatifs dont l'absence serait fatale

- Monde à partition non échangeable où le mécanisme de tenue à l'écart dépend d'un paramètre corrélé à q_f : nécessaire pour que le duel 2 ait une issue ; sinon l'écart vues/tenues est centré en zéro par construction et ne mesure que la variance d'échantillonnage.
- Monde à π = 0,02 exactement sous la définition retenue : la prédiction « zéro échec sur 59 » doit y être rejetée avec la fréquence binomiale attendue (≈ 0,70) ; si D maintient cette prédiction scellée, ce contrôle montre qu'elle ne teste pas la définition.
- Monde où la source extérieure a une probabilité de capture hétérogène de même loi que les trois sources : la part nouvelle observée doit alors coller à Good-Turing et non à 1 − 37/N̂ ; si les deux prédictions ne sont pas séparées d'au moins deux écarts-types dans la simulation, la confrontation « Inconnues » est à retirer du préenregistrement ou à réécrire sur Ĉ.

---

## Remarque transversale (attribuée, non fusionnée)

Les trois pièces construisent une grille factorielle qui croise dépendance et hétérogénéité comme si ces facteurs étaient reconnaissables depuis les sept comptes. Par R5, ils ne le sont pas avec trois sources. La couverture doit donc être rapportée comme le minimum sur l'enveloppe des cellules compatibles avec (16, 7, 14), et non cellule par cellule ; aucune des trois pièces ne formule ce critère. De même, aucune ne propage l'erreur d'appariement jusqu'à la déviance 12,9 : une seule fusion à tort change les sept cellules, donc l'identification du cas A héritée de C et D a le statut RAPPORTÉ du fait 17, pas celui d'un calcul.

FIN-DE-CELLULE