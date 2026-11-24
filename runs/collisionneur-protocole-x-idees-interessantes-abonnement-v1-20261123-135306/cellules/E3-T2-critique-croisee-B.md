La proposition B (ma propre conception du tour III.1) n'est pas transmise, et je n'en reconstitue pas le contenu. Le bloc QUESTION DE L'ARBITRE reprend le bloc FAITS mot pour mot, avec la même empreinte déclarée, que je n'ai pas recalculée. Il ne pose donc pas de question distincte. Je suis le livrable du tour III.2, critique croisée en (a), (b), (c), et non les sept parties. Aucune des pièces A, C, D, E n'est visiblement coupée : chacune se termine par FIN-DE-CELLULE.

**Statuts.** [O] = OBSERVÉ-NON-AUDITÉ : ce que je lis dans les pièces. [H] = HYPOTHÈSE : mes déductions et objections. [R] = RAPPORTÉ : la littérature, citée de mémoire et non revérifiée. Tout chiffre qui ne vient pas des pièces est « illustratif ». Ceux que je reprends des pièces gardent le statut que leur auteur leur a donné.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **D0 : le comparateur est neutralisé par l'appariement.** Les leurres B′ ont « la même similarité de surface avec A » [O].
   - [H] Si cette similarité est le cosinus brut, le score (i) vaut ½ par construction.
   - L'exigence « (ii) dépasse (i) d'au moins 10 points » se réduit alors à « (ii) ≥ 0,60 » (illustratif), et la comparaison à (i) ne dit rien.
   - Seul le comparateur TF-IDF reste informatif, à condition de ne pas avoir servi à apparier les leurres.
2. **D0 : la rédaction des descriptions fuit.** A ne dit pas qui écrit les descriptions « sans équations ni noms propres » [O].
   - [H] Si le même rédacteur écrit A et B en sachant qu'ils forment une paire, il met en commun le gabarit et le vocabulaire relationnel (« amortissement », « rétroaction »). La similarité devient vraie par construction.
   - Le même risque vaut pour les paires synthétiques, écrites selon un gabarit commun.
3. **D0 : la lecture « réussit sur réel, échoue sur synthétique = mémorisation » n'est pas univoque.** [H] Des mots inventés sont découpés en sous-mots que les encodeurs n'ont jamais vus. L'échec sur les paires synthétiques peut donc venir de la tokenisation et non de l'absence de structure. Une même issue (succès réel, échec synthétique) a ainsi deux causes concurrentes, ce qui viole B4.
4. **D1 et D4 : biais de collisionneur.** Le taux de naissance λ_ij dépend de s et de m (β2, β5) [O]. D1 évalue la réutilisation sur les seuls liens nés [O].
   - [H] Conditionner sur la naissance induit une corrélation négative entre s et m chez les nés, ce qui biaise β6 et γ4 ([R] Elwert & Winship, 2014, « Endogenous Selection Bias: The Problem of Conditioning on a Collider Variable »).
   - A corrige ce biais en D2 avec un modèle à obstacle, mais pas en D1 ni en D4.
5. **D3 : l'exposition et le lien naissent du même article.** e_ij est la part des articles de chaque concept qui emploient M [O].
   - [H] Un article qui emploie M et cite à la fois i et j crée en même temps l'exposition et le lien. L'excès de liaison est alors en partie mécanique.
6. **D3 : estimateur inadapté.** [H] Une différence de différences à adoption échelonnée, estimée par effets fixes bidirectionnels, est biaisée quand l'effet varie selon la date d'adoption ([R] Goodman-Bacon, 2021, « Difference-in-differences with variation in treatment timing » ; Callaway & Sant'Anna, 2021, « Difference-in-Differences with multiple time periods »).
7. **D4 : les ego-réseaux ne sont pas gelés.** A ne précise pas la date à laquelle les ego-réseaux sont calculés [O].
   - [H] S'ils le sont en fin de période, les liens repris ont enrichi leurs propres voisinages, et m prédit la reprise par construction.
8. **D5 : effet de copie des modèles de langage.** [H] La chute de surprisal quand on fournit l'explication croît mécaniquement avec le recouvrement lexical entre l'énoncé et l'explication. Le contrôle par « explication d'une autre idée » abaisse aussi ce recouvrement, donc il ne l'égalise pas.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **β6 (D1).** La variance de l'estimateur croît comme 1/(n·(1 − R²)), où R² est le coefficient de détermination de (1 − s)·m sur (s, m, log k_i k_j).
  - Si Var((1 − s)·m | s, m, k) → 0, par exemple parce que corr(s, m) → ±1, β6 n'est pas identifiable [H].
- **m (Gromov–Wasserstein entropique).** Si le paramètre de régularisation ε est grand devant l'échelle des matrices de coût, le couplage optimal tend vers le couplage produit. On a alors Var(m) → 0 et m ne discrimine plus rien.
  - Si la taille des ego-réseaux est petite, la loi de m devient discrète et dégénérée [H].
- **AUPRC (D1).** Un classifieur au hasard obtient une AUPRC égale à la prévalence π ([R] Saito & Rehmsmeier, 2015, « The precision-recall plot is more informative than the ROC plot… »).
  - Quand π ≪ 1, l'écart-type de ΔAUPRC peut dépasser 5 % de l'AUPRC, et le seuil relatif de 5 % (illustratif chez A) n'est plus jugeable [H].
- **Bootstrap par paires de domaines.** Avec G grappes, la couverture de l'intervalle se dégrade quand G est petit. A ne fixe pas G [O].
- **D0.** Avec 60 paires (illustratif chez A), l'exactitude appariée a un écart-type d'environ √(0,25/60) ≈ 0,065 (illustratif).
  - Le seuil de 10 points représente donc environ 1,5 écart-type (illustratif) : l'expérience n'a pas la puissance de trancher [H].
- **D2.** La puissance du test des deux droites tend vers 0 si le maximum vrai se trouve vers un quantile extrême de la loi de s.
  - Elle tend aussi vers 0 si la première étape (la naissance) met une masse quasi nulle aux grandes distances [H].
- **D5.** La corrélation observable est bornée par √(fidélité inter-juges). Si l'α des juges vaut 0,6 (illustratif chez A), cette borne est d'environ 0,77 (illustratif).
  - Avec n = 200 (illustratif chez A), l'écart-type de ρ est d'environ 1/√197 ≈ 0,07 (illustratif) [H].

### (c) Contrôles négatifs dont l'absence serait fatale

- **D0.** Un comparateur qui n'a pas servi à l'appariement. Des rédacteurs distincts pour chaque côté, aveugles à l'appariement, qui écrivent aussi les leurres.
- **D3.** Les liens comptés uniquement dans des articles qui ne mentionnent pas M, et l'exposition mesurée sur des articles disjoints des articles de liaison.
- **D4.** Les ego-réseaux gelés à la date de naissance du lien.
- **D5.** Une explication fausse ayant le même recouvrement lexical avec l'énoncé que la vraie.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts.** C marque [VÉRIFIÉ] des énoncés de littérature ou de conception sans fournir de pièce d'audit [O].
   - Exemples : OpenAlex et S2ORC ; le « seuil spectral λ_max > 1 » ; « défaut d'homomorphisme… équivalent discret exact » ; « Retraction Watch ».
   - Je ne change pas ces statuts. Je constate seulement qu'aucune vérification n'est transmise, donc aucun test de C ne peut s'appuyer sur ces énoncés comme sur des résultats.
2. **La surprise est vraie par construction.** C pose Surprise ∝ d_S [O]. Toute corrélation entre surprise et distance est donc définitionnelle.
   - L'instrument I4 est ensuite calibré sur des déciles d'atypicité d'Uzzi, qui est une autre distance de surface : le raisonnement est circulaire [H].
3. **La fécondité est vraie par construction.** Fécondité = s_R × (gain d'efficacité) [O]. Elle ne peut donc servir à valider s_R [H].
4. **Duel 2 : l'issue qui réfuterait H_B est impossible.** w_t > 0 exige ΔPMI(u, m) > 0 et ΔPMI(v, m) > 0, donc que u et v co-occurrent tous deux avec m dans E^(S), où m ∈ V_t [O].
   - [H] Le chemin u–m–v est alors de longueur 2, ce qui donne B_2(u, v) > 0.
   - Le sous-ensemble « B_2 = 0 et w_t élevé », sur lequel H_B serait réfutée, est vide par construction. Le duel n'est pas conforme à B4.
5. **Duel 2 : sélection des jumeaux.** [H] Les « jumeaux » sont repérés dans le même corpus que celui qui sert à calculer w_t, sur des paires « chaudes ». Leur croissance conjointe corrèle mécaniquement avec les méthodes en vogue.
6. **Expérience 7 : M0 neutralisé et groupes extrêmes.** Les deux groupes sont appariés sur (d_S, A_pref), si bien que l'AUC de M0 vaut 0,5 par construction, comme C l'écrit lui-même [O].
   - [H] La comparaison à M0 est donc vide. Le vrai concurrent serait un ensemble de covariables non appariées : Adamic–Adar, croissance des champs, prestige des auteurs.
   - Le contraste « ≥ 15 reprises contre 0 » (illustratif chez C) gonfle l'AUC par rapport à la population réelle [H].
7. **Fuite asymétrique en faveur de H9.** Le score S_H9 utilise SciBERT, préentraîné sur un corpus Semantic Scholar qui inclut des articles postérieurs à 2015 ([R] Beltagy, Lo & Cohan, 2019, « SciBERT: A Pretrained Language Model for Scientific Text »).
   - [H] La fuite favorise H9 dans un duel H3 contre H9. Elle peut produire « H3 réfutée au profit de H9 » par artefact.
8. **SemMedDB.** [H, référence à vérifier] Si SemMedDB est produit par une version récente de SemRep et d'UMLS appliquée à toute l'archive, le filtre YEAR ≤ 2015 retire des articles mais pas le vocabulaire ni l'extracteur, qui sont postérieurs. Les concepts sont alors reconnus rétroactivement.
9. **Instrument I2.** [H] Les faux-amis sont choisis parce qu'ils partagent le vocabulaire de surface, ce qui handicape Word2Vec par construction. Les voisinages des analogies historiques sont décrits dans des textes postérieurs à ces analogies.
10. **Duel 3.** [H] Le taux de fausses alertes à TPR fixé à 0,70 (illustratif chez C) n'est pas défini si la courbe ROC de l'une des méthodes n'atteint jamais ce rappel.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **DeLong (expérience 7).** Le test de DeLong suppose des observations indépendantes ([R] DeLong, DeLong & Clarke-Pearson, 1988, « Comparing the areas under two or more correlated receiver operating characteristic curves »).
  - [H] Si un même concept u entre dans plusieurs paires, la covariance intra-concept est positive et l'erreur-type est sous-estimée.
  - La zone entre 0,58 et 0,62 (illustratif chez C) n'a pas de lecture.
- **Δ_lock.** La loi de la taille de N_2(u) est à queue lourde, car les hubs de SemMedDB ont des voisinages énormes.
  - [H] Si E[Δ_lock | taille] dépend de la taille, et si les lois de la taille diffèrent entre Y = 1 et Y = 0 malgré l'appariement sur le produit des degrés (un produit égal ne fixe ni chaque degré ni la taille dans E^(R)), l'AUC mesure la taille et non la structure.
- **ΔPMI.** L'estimateur de la PMI est biaisé vers le haut et sa variance explose quand les comptes sont faibles. Sans lissage, w_t est dominé par le bruit des paires rares [H].
- **Régression logistique conditionnelle (duel 2).** Si les ensembles appariés discordants sont peu nombreux, ou si w_t = 0 chez presque tous les singletons (séparation quasi complète), l'estimateur du rapport de cotes est instable ou infini [H].
- **Percolation.** « λ_max > 1 » ne désigne aucune matrice précise [O]. Le critère n'est pas jugeable [H].

### (c) Contrôles négatifs dont l'absence serait fatale

- **Expérience 7.** Un bras H9 sans fuite, entraîné seulement sur le corpus antérieur ou égal à 2015 (la PPMI-SVD existe chez C), et une règle de décision qui ne lit que ce bras.
  - Un recâblage du graphe typé à degrés conservés : la permutation des seules étiquettes garde la topologie.
- **Duel 2.** B_2 calculé hors des nœuds méthodes, et w_t calculé sur des articles disjoints des articles de liaison.
- **Instrument I4.** Une calibration de la surprise qui ne fait pas intervenir Δ_lock : C filtre I4 par Δ_lock, ce qui fait fuir un instrument dans l'autre [O].

---

## Sur la proposition D

### (a) Défauts de méthode

1. **V1 : le contrôle négatif échoue par construction.** Le terme Gromov–Wasserstein de S_struct n'utilise que les distances internes D_u, c'est-à-dire les plus courts chemins dans l'arbre [O].
   - [H] Permuter les étiquettes d'opérateurs à topologie constante laisse ce terme inchangé ; seul μ·C(Π) varie.
   - Le gain survit donc au contrôle. Selon la règle de D (|ΔAUPRC| < 0,01 exigé, illustratif), l'expérience est déclarée invalide quelle que soit la vérité.
2. **Expérience 7.1 : l'étiquette est tirée de l'instrument évalué.** Les couples positifs sont « régis par des systèmes d'équations formellement isomorphes » [O].
   - [H] Si cet isomorphisme est établi sur les équations elles-mêmes, AUC_éq ≥ 0,80 (illustratif chez D) est vraie par construction : l'instrument qui fabrique l'étiquette est celui qu'on évalue.
   - Le bras « équations », qui sert de pivot à la réfutation de H9, ne prouve alors rien.
3. **Expérience 7.1 : une fuite lexicale demeure après désinfection.** D retire les équations et les co-mentions, mais pas le vocabulaire mathématique (« valeur propre », « amortissement », « diffusion ») [O].
   - [H] Les leurres « elliptique contre hyperbolique » diffèrent précisément par ce vocabulaire. Un succès du texte peut donc être purement lexical.
4. **Mémorisation dans les poids.** Qwen2.5-7B et bge-large ont été préentraînés sur des textes qui énoncent ces analogies de manuel [H].
   - La désinfection porte sur le corpus, pas sur les poids. Le contrôle positif de fuite vérifie le logiciel, pas la mémorisation.
5. **V2 : la susceptibilité χ est éliminée par l'appariement.** V2 apparie les multiples à des singletons de même année et de même domaine [O]. χ(t) est une variable méso, propre à la paire de spécialités.
   - [H] Dans chaque strate appariée, χ est presque constant, donc AUC_χ ≈ 0,5 par construction. H_B ne peut pas gagner.
6. **V2 : appariement sur une variable postérieure au traitement.** [H] L'appariement sur l'impact à 5 ans conditionne sur une conséquence de la multiplicité, car les multiples sont co-cités.
   - De plus, le catalogue définit les multiples par une co-citation ultérieure, donc par un effet de l'impact.
7. **V3.** [H] Des juges de 2026 peuvent connaître l'issue d'hypothèses historiques. Les réécrivains connaissent l'issue et peuvent la trahir par le style.
   - La zone 0,55–0,65 (illustratif chez D) n'a pas de lecture.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Expérience 7.1.** Avec 40 positifs et 40 leurres (illustratif chez D), l'écart-type de l'AUC est d'environ 0,06 à 0,07 (illustratif ; [R] Hanley & McNeil, 1982, « The meaning and use of the area under a receiver operating characteristic (ROC) curve »).
  - Les seuils 0,55 et 0,70 ne sont séparés que d'environ deux écarts-types.
  - L'extension préenregistrée à 120 couples est un test séquentiel : sans dépense de l'α, le risque de première espèce est inflaté [H].
- **Gromov–Wasserstein entre nuages ACP.** [H] La valeur dépend du nombre de points et de l'étendue de chaque nuage. Si les lois de la taille du vocabulaire diffèrent entre isomorphes et leurres (D apparie sur le volume de texte, pas sur la taille du vocabulaire), l'AUC mesure la taille.
- **V2.** Les deux AUC sont calculées sur les mêmes cas et sont corrélées. Si Var(χ | strate) ≈ 0, l'écart |AUC_Z − AUC_χ| se réduit à |AUC_Z − 0,5| [H].
- **V1.** Si Var(μ·C(Π)) est faible devant Var(terme GW), S_struct est insensible aux types, et H6 n'est pas testée [H].

### (c) Contrôles négatifs dont l'absence serait fatale

- **V1.** Un recâblage à degrés conservés, ou un Gromov–Wasserstein fusionné avec des attributs d'opérateurs, qui rende le contrôle sensible aux étiquettes.
- **Expérience 7.1.**
  - Des étiquettes de source extérieure (manuels, audit par un tiers) qui ne sont pas établies sur les arbres d'équations.
  - Des leurres appariés sur le recouvrement du vocabulaire mathématique.
  - Une décision prise sur le seul bras sans fuite (PPMI-SVD sur corpus daté).
- **V2.** χ calculé au niveau de la paire, et suppression de l'appariement sur l'impact.
- **V3.** Un questionnaire d'exclusion des juges qui connaissent l'issue.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Expérience 7.1 : même circularité que chez D.** Les positifs sont choisis parce qu'ils « partagent un sous-arbre opératoire non trivial » [O].
   - [H] La branche « l'alignement sur arbres syntaxiques dépasse +0,15 » est donc vraie par construction.
   - La réfutation de H9 s'appuie sur une comparaison dont le pivot n'est pas testé.
2. **Fuite par l'extracteur.** Qwen2.5-7B ou Llama-3.1-8B, entraînés après 2016, servent à extraire les méthodes qui alimentent I_t [O].
   - [H] Un tel extracteur peut mieux reconnaître les méthodes devenues populaires ensuite. I_t corrèle alors avec le futur par construction.
   - L'audit sur 200 phrases (illustratif chez E) mesure l'exactitude, pas ce biais temporel.
3. **Zones sans lecture, contraires à B4.** En E1, rien n'est dit entre +0,02 et +0,05 (illustratif chez E). En 7.1, rien entre +0,03 et +0,08 (illustratif chez E) [O].
4. **E3 : la fécondité risque de lire l'étiquette.** Le progrès de compression est mesuré sur un ensemble 𝒟 d'observations qu'E ne date pas [O].
   - [H] Si 𝒟 contient des données postérieures à T0, comme les résultats d'essais, le score lit l'étiquette.
   - Les rétractations pour fraude sont à la fois surprenantes et « échouées ». Elles pénalisent la surprise brute par la constitution même du jeu, sans rapport avec H10.
5. **Le modèle impose H4.** Le terme −γ·d_surf dans U_hum crée un optimum intérieur [O]. Le modèle ne peut donc pas tester H4 [H].
6. **Les échecs d'essais cliniques ne sont pas des réfutations.** [H] L'échec en phase II/III dépend du promoteur, du critère retenu et du financement, pas de la fausseté du lien. Cette variable confondante corrèle avec le prestige des parents.
7. **E2 : régression vers la moyenne.** I_t est une différence de similarités [O].
   - [H] E[I_t | sim_{t−Δ}] a une pente négative. Sans conditionner sur la similarité initiale, I_t est plus grand pour les paires initialement éloignées, qui sont justement celles retenues comme multiples lointains.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Permutations par blocs disciplinaires (E1).** Avec B blocs, il n'existe que B! permutations distinctes, et la plus petite valeur p atteignable est 1/B! [H].
  - Pour B ≤ 4 (illustratif), on a B! ≤ 24, donc p < 0,01 (illustratif chez E) est inatteignable.
- **ΔBIC ≤ −10 (E2).** [H] La pénalité vaut k·log n. Pour n grand, un effet négligeable franchit le seuil ; pour des multiples rares, la puissance est faible.
  - Comparer un modèle de Poisson à un modèle logistique non emboîté sur des vraisemblances différentes n'est pas jugeable.
- **AUC-PR.** Avec une prévalence artificielle de 1/6 (appariement 1:5, illustratif chez E), l'AUC-PR n'est pas transposable à la prévalence réelle [H].
- **McNemar (E3).** La puissance ne dépend que du nombre de paires discordantes. Si celles-ci sont rares, le test n'est pas jugeable [H].

### (c) Contrôles négatifs dont l'absence serait fatale

- **Expérience 7.1.** Des étiquettes indépendantes des arbres syntaxiques. E prévoit déjà les homonymes et les arbres à opérateurs permutés, ce qui est utile mais insuffisant.
- **I_t.** Un contrôle du rappel de l'extracteur stratifié par la popularité future des méthodes, et un extracteur à dictionnaire figé à T0.
- **E3.** 𝒟 gelé à une date antérieure ou égale à T0. Les rétractations pour fraude séparées des réfutations.
- **E1.** Le recâblage à degrés fixés est présent ; c'est l'un des rares contrôles bien posés.

---

## Défauts que je retrouve chez plusieurs propositions

Ce sont des critiques attribuées une à une, pas une synthèse.

- **Circularité étiquette = instrument** : D (expérience 7.1) et E (expérience 7.1).
- **Fuite par des poids préentraînés après la date de coupure** : C (SciBERT), D (Qwen, bge) et E (extracteur Qwen ou Llama). A l'évite en D1 à D4 [O].
- **Ontologies appliquées rétroactivement** (SemMedDB, UMLS, MeSH) : A, C et E. Cela reste à vérifier [H].
- **Échec défini par « zéro reprise »** : A, C, D et E. [H] Zéro reprise dépend aussi de la visibilité, de la langue et de la taille des champs. Aucune des quatre n'apparie sur la croissance des deux champs.
- **Aucune correction pour comparaisons multiples entre duels** : A, C, D et E [O].

FIN-DE-CELLULE