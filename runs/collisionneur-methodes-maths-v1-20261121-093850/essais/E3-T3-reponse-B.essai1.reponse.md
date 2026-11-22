# Proposition B, tour III.3 : réponse aux critiques

**Pièces reçues.** J'ai reçu les FAITS, la QUESTION, ma conception III.1 et les critiques A, C, D et E. Chacune est close par sa ligne de fin, et je ne vois ni coupure ni vide. Je n'ai pas recalculé les empreintes.

**Statuts.** Ils sont inchangés depuis III.1 :
- FAITS : **RAPPORTÉ** ;
- annonces externes : **RAPPORTÉ, non vérifié** ;
- littérature : **RAPPORTÉ**, de mémoire ;
- mes propositions : **HYPOTHÈSE**.

Ici, **VÉRIFIÉ** ne marque qu'un calcul dont je donne l'argument dans ce texte. Ces calculs restent à faire relire. Je ne reprends pas à mon compte les étiquettes VÉRIFIÉ posées par C et E. Quand j'adopte un de leurs arguments, je le refais. Tout chiffre qui ne sort pas d'un calcul affiché est illustratif.

---

## (a) Verdict sur chaque critique

### P2 : pire dépendance pour l'agrégation

| Critique | Verdict | Conséquence |
|---|---|---|
| A-a1, C-a1, E-a1(ii) : l'écart est décidé avant calcul. Sur le même polytope discret, H_A est acquise ; contre une borne continue, H_B l'est par discrétisation. | **Acceptée sur le fond.** La qualification de C (« pris pour un théorème nouveau ») est rejetée : en III.1, un écart ne déclenchait qu'une conjecture, puis une preuve, puis une relecture. Mais le critère était vicié. | Les deux termes sont comparés sur la **même** grille. Les grilles sont emboîtées. |
| E-a1(i) : Vovk–Wang calibre sous dépendance honnête arbitraire. Fixer le niveau sous une loi honnête fixée produit un gain trivial. | **Acceptée.** | Deux régimes séparés, R et J. Leur différence est rapportée comme coût de l'ignorance de la dépendance honnête, jamais comme découverte. |
| A-a2 : la liste des agrégateurs est une variable confondante, car l'objet est sup_φ inf_π. | **Acceptée.** | La valeur max-min est calculée en un seul programme linéaire (LP) ; voir (b). |
| A-a2 bis : si la loi honnête est estimée, le niveau devient un estimateur. | **Rejetée pour l'objet mathématique** : les marges sont des paramètres de l'énoncé. **Acceptée pour l'étape d'utilité.** | Une correction en échantillon fini est requise à l'application, hors de P2. |
| A-b : si TV = 0 pour chaque moniteur, la valeur vaut α ; si les supports sont disjoints, elle vaut 1 ; un écart qui tend vers 0 quand la grille s'affine n'est pas jugeable. | **Transformée en contrôles.** | Voir P2'. |
| A-c : « le cas k = 2, où la borne exacte est connue ». | **Non utilisable.** Je ne connais pas de valeur exacte publiée pour *ce* problème de test à k = 2. | Remplacé par k = 1, la puissance de Neyman–Pearson, calculable à la main. |
| D-b : la grille d'évaluation peut ne pas charger la région d'écart. D-c : le contrôle « indépendant » ne contrôle rien si l'indépendance n'est pas imposée au solveur. | **Acceptées.** | Générateur d'instances pré-enregistré, marges extrêmes incluses. Le contrôle indépendant est supprimé. |
| C-b : écart en O(1/m) avec terme de périmètre. | Non vérifié par moi. **Sans objet après correction**, puisque les deux termes partagent la grille. | Aucune. |
| C-a1 et E-a1, adressées à E : dégénérescence duale et non-unicité du certificat. | **Je m'en sers (B1)** : elles s'appliquent à moi dès que je lis la paire la moins favorable. | Règle de sélection canonique et permutations de colonnes. |

### P3 : paires indiscernables pour sonde linéaire

| Critique | Verdict | Conséquence |
|---|---|---|
| A-a3, C-a2, D-a, E-a2 : apparier les moments d'ordre ≤ 2 n'aveugle pas une sonde à seuil. | **Acceptée.** Calcul refait (**VÉRIFIÉ**) sur l'exemple de D. P met une masse ½ sur −1 et sur +1. Q met ½ sur 0 et ¼ sur −√2 et sur +√2. Les deux ont moyenne 0 et variance 1. Pourtant P(x > 1) = 0 et Q(x > 1) = ¼. L'exemple de E donne de même un avantage de 3/10. | La famille de référence de mon duel était mal caractérisée, et mon duel tombe. Pour un écart de moyennes de score, seul le premier moment compte. Pour des demi-espaces sur supports finis, un avantage nul partout impose P = Q (Cramér–Wold, RAPPORTÉ). |
| A-a4, C-a2 : δ n'est pas une fonctionnelle de (P, Q) ; une lecture g libre et non linéaire rend le score trivial. | **Acceptée.** | La lecture g est scellée avant toute recherche. |
| A-b, C-b : un support de s ≤ d + 1 points en position générale donne ε = TV. | **Acceptée.** Argument : des points affinement indépendants laissent séparer toute partie par un hyperplan. | Il faut n ≫ d. |
| E-a2, C-b : l'évaluateur optimise une pénalité, le duel juge un ratio, et le lagrangien n'atteint que l'enveloppe concave. | **Acceptée.** | La courbe δ*(ε) est calculée sous contrainte, sans pénalité. |
| A-a5 : l'effort de recherche est asymétrique entre la famille connue et le reste. | **Acceptée.** | À support fixé, la couche intérieure est un LP exact. Seul le support est cherché, au même budget dans les deux bras. |
| A-a3 : antériorité probable dans le pseudo-aléa contre les demi-espaces. | **Acceptée.** Référence candidate, RAPPORTÉ de mémoire : Diakonikolas, Gopalan, Jaiswal, Servedio, Viola, *Bounded Independence Fools Halfspaces* (lieu et année à vérifier). | P3 est déclassée (voir P3'). |

### P1 : carte du folklore

| Critique | Verdict | Conséquence |
|---|---|---|
| A-b : un seul énoncé connu planté ne contrôle rien. | **Acceptée.** Calcul refait (**VÉRIFIÉ**) : 0,9²⁹ ≈ 0,047 et 0,9²⁸ ≈ 0,052. Il faut 29 succès sans échec pour exclure un rappel < 0,9 au risque 5 %. | La revendication est proportionnée au nombre d'énoncés plantés. |
| D-a/b, E-b1 : un expert unique n'est pas identifiable sans étalon ; réfuter *une* réduction n'exclut pas *toutes* les réductions. | **Acceptée.** | La falsification devient asymétrique et explicite. Chaque « réduit » doit porter un pointeur vérifié. |

### P4 : dérive d'énoncé

| Critique | Verdict | Conséquence |
|---|---|---|
| A-a6, C-a3 : fuite par les quarante énoncés, et un humain détecte de mémoire. | **Acceptée.** | Lemmes synthétiques, absents des manuels. |
| A-a6 : aucun bras humain n'est mesuré. | **Acceptée.** | H_A devient absolue (« taux de ratés ≤ s ») et non comparative. |
| A-b : 1 raté sur 20 reste compatible avec un taux de ratés de 0,22. | **Acceptée.** Recalcul (**VÉRIFIÉ**) : borne unilatérale ≈ 0,216. | Il faut au moins 59 mutants sans raté (voir P4'). |
| A-b/c : certains mutants sont équivalents (≤ ou < sous loi sans atome), donc mal étiquetés. | **Acceptée.** | Étiquette « non équivalent » seulement avec un témoin de séparation certifié. |
| E-a3, E-b4 : les erreurs endogènes de formalisation (coercitions, totalisation) sont ignorées. | **Acceptée.** | Ajout d'un bras de formalisations produites par LLM. |
| E-a3 : circularité, P4 étalonne le juge sur l'humain et le tableau (c) l'humain sur le juge. | **Acceptée.** | L'étalon est le témoin certifié, ni le juge ni l'humain. |
| D-c : les mutants portent des marqueurs de style. | **Acceptée.** | Réécritures correctes de même style, ajoutées comme négatifs. |
| C-b : n ≥ 160. | Chiffre non recalculé par moi, **non adopté**. | Je donne mon propre calcul. |

### P5 : archive des morts

| Critique | Verdict | Conséquence |
|---|---|---|
| A-b, C-b : le nombre de classes est un estimateur de richesse biaisé, qui dépend du volume. | **Acceptée.** | Masse manquante estimée par Good–Turing (singletons). |
| D-b, E-a4 : un contrôle par mélange de l'archive laisse le compte invariant. | **Acceptée** : mon contrôle était vide. | Supprimé. |
| D-a : diversité des témoins ≠ valeur de réemploi. | **Acceptée.** | Le duel porte sur le réemploi. |
| E-b5 : un bruit de représentation fait de chaque témoin un singleton. | **Acceptée.** | Quotient fixé a priori. |

### Section 4 et tableau (c) de III.1

| Critique | Verdict | Conséquence |
|---|---|---|
| A-a7 : l'utilité est circulaire si les mêmes mondes ont servi à sélectionner. | **Acceptée.** | Mondes d'utilité scellés, tirés d'un générateur distinct. Bras placebo (contrôle proposé par A pour D ; je m'en sers). |
| A-c, E-a4 : des négatifs « à paramètres inédits » sont des spécialisations de connus, donc faussement « neufs ». | **Acceptée.** | Classe négative supprimée. Voir le pointeur de P1'. |
| E-c1 : aucun témoin de non-vacuité ; avec la correction que E adresse à C, les conventions de totalisation dégénèrent la conclusion, pas l'hypothèse. | **Acceptée et transformée en test.** | Voir H-Lean. |
| E-b5 : la règle « zéro raté » est faible sans taille d'échantillon. | **Acceptée.** | Tailles annoncées et dérivées. |

---

## (b) Expériences corrigées

### P2'. Test minimax entre deux classes de Fréchet

**Objet** (HYPOTHÈSE sur son intérêt).
- Alphabet fini X = {1,…,m} et k moniteurs.
- Marges honnêtes F⁰ᵢ et marges sous sabotage F¹ᵢ.
- Γ(F) désigne l'ensemble des lois jointes de marges F.
- Deux régimes, jamais mélangés :
  - **R** : la dépendance honnête est arbitraire ;
  - **J** : la loi honnête jointe P⁰ est fixée.
- Valeur en régime R :

  V_R = max_{φ : Xᵏ → [0,1]} min_{π ∈ Γ(F¹)} E_π φ, sous la contrainte max_{π ∈ Γ(F⁰)} E_π φ ≤ α.

**Calcul en un seul LP** (**VÉRIFIÉ**, argument). Les deux problèmes intérieurs sont des LP de transport multi-marginal finis. Par dualité forte :
- min_π E_π φ ≥ t équivaut à l'existence de potentiels vᵢ tels que Σᵢ vᵢ(xᵢ) ≤ φ(x) pour tout x, et Σᵢ E_{F¹ᵢ} vᵢ ≥ t ;
- max_π E_π φ ≤ α s'écrit de même, avec des potentiels uᵢ.

V_R est donc un LP en (φ, u, v, t). Cela supprime la liste d'agrégateurs comme variable confondante (A-a2).

**Remarque préalable : la route classique directe est fermée.**
- Γ(F) coïncide avec le cœur de sa probabilité supérieure U(A) = sup_{π∈Γ} π(A) (**VÉRIFIÉ**). Si P ≤ U sur tout cylindre {xᵢ ∈ B} et sur son complément, alors Pᵢ(B) = Fᵢ(B). La réciproque est immédiate.
- Huber & Strassen (1973), *Minimax tests and the Neyman–Pearson lemma for capacities* (Annals of Statistics ; RAPPORTÉ, de mémoire), donnent le test minimax lorsque U est 2-alternante, c'est-à-dire U(A∪B) + U(A∩B) ≤ U(A) + U(B).
- Cette condition échoue ici (**VÉRIFIÉ**). Prenons 2×2, marges uniformes, A = ligne a₁ et B = colonne b₁. On a U(A) = U(B) = ½. Ensuite U(A∪B) = 1, atteint par la loi qui met ½ sur (a₁,b₂) et ½ sur (a₂,b₁). Enfin U(A∩B) = ½. Total : 1,5 > 1.
- Ce calcul **n'établit pas** la nouveauté. Il ferme une seule route. L'existence d'une paire la moins favorable reste classique dans la théorie des tests composites (Lehmann & Romano, *Testing Statistical Hypotheses* ; chapitre à vérifier).

**Duel** (B4), sur une grille d'instances pré-enregistrée : k ≤ 3, marges extrêmes incluses, grilles emboîtées m₁ < m₂ < m₃ (illustratif).
- **H_A** : la meilleure des règles connues pré-enregistrées atteint V_R exactement, en rationnel, sur toute la grille. Les règles candidates sont Bonferroni et la moyenne des p-valeurs doublée, chacune recalibrée en régime R par le même LP intérieur.
- **H_B** : il existe une instance où V_R − V_connu ≥ η (illustratif) sur les trois grilles emboîtées, sans tendance vers 0.

**Contrôles.**
- k = 1 : V égale la puissance de Neyman–Pearson calculée à la main.
- F⁰ = F¹ : V = α.
- Supports disjoints coordonnée par coordonnée : V = 1.
- Écart J − R rapporté à part.
- Lecture de la paire la moins favorable par une règle canonique (lexicographique), stable sous 10 permutations de colonnes (illustratif).

**Issues.**
- Écart nul partout : H_B est falsifiée sur la grille. Les règles connues suffisent, et j'arrête.
- Écart stable : H_A est falsifiée. La paire la moins favorable (π⁰*, π¹*) devient l'objet de la conjecture. Celle-ci est évaluée hors de la plage d'ajustement en k et en m (idée de E, reprise par A).

**Coût.** Heures de CPU, dizaines de dollars (illustratif). La taille croît en mᵏ ; au-delà de petits k, je ne sais pas.

**Différence avec le publié.** La route Huber–Strassen ne s'applique pas directement, sous réserve que mon calcul tienne. L'antériorité reste à chercher dans la littérature sur l'incertitude de dépendance (Embrechts, Puccetti, Wang et coll. ; références à vérifier) et dans celle des tests robustes.

### P3'. Sondes à seuil : déclassée en mesure de méthode

**Objet.**
- Lecture g scellée.
- Classe de sondes : les demi-espaces de ℝᵈ.
- Support S de n ≥ 10d points (illustratif).

À S fixé, δ*(ε ; S) = max TV(g#P, g#Q) sous la contrainte |P(H) − Q(H)| ≤ ε pour tout demi-espace H. C'est un LP par ensemble de sorties. Les coupes sont énumérables en petite dimension. Seul S est cherché.

**Duel de méthode.**
- **H_A** : la recherche guidée par LLM bat, à budget égal, des supports aléatoires ou structurés, d'au moins η sur δ* aux valeurs de ε pré-enregistrées.
- **H_B** : elle ne les bat pas.

Si le LLM n'apporte rien là où seule la couche extérieure est non convexe, il n'y a pas lieu de l'employer ailleurs dans ce domaine.

**Contrôles.**
- P = Q : δ = 0.
- La paire de D doit donner ε ≥ ¼.
- La paire de E doit donner ε ≥ 3/10.

**Point mathématique.** Avec ε = 0, P = Q, donc δ = 0. Seul le régime ε > 0 est en jeu, et l'antériorité y est probable (référence ci-dessus). P1' passe d'abord.

**Coût.** Quelques centaines de dollars d'appels (illustratif).

### P1'. Carte du folklore, falsification asymétrique

**Sorties.** Pour chaque question, l'une ou l'autre :
- « réduit », avec un pointeur et une réduction relue par une seconde personne ;
- « non réduit dans le périmètre P », avec P listé.

**Calibration.** On plante n énoncés connus déguisés. Avec zéro raté, on revendique seulement un rappel ≥ 0,05^(1/n) (**VÉRIFIÉ**) :
- n = 10 donne ≥ 0,74 ;
- n = 29 donne ≥ 0,90.

Les heures d'expert sont rares (RAPPORTÉ). Je propose donc n = 10 et la revendication faible.

**Duel.**
- H_A : la question se réduit au publié.
- H_B : elle ne s'y réduit pas.
- Un « réduit » vérifié falsifie H_B pour cette question.
- Un « non réduit » ne falsifie H_A que relativement au périmètre et au rappel. Je l'écris ainsi, avec la formule de D : P(connu | rien trouvé) = π(1−ρ) / (π(1−ρ) + 1 − π).

**Contrôle.** Un énoncé planté réductible par un *autre* classique que celui que suggère l'énoncé (D).

### P4'. Banc de fidélité d'énoncé à étalon certifié

**Lot.** Des lemmes synthétiques absents des manuels, jamais les quarante, avec :
- (i) des mutants manuels munis d'un **témoin de séparation certifié** : une instance finie où l'original et le mutant diffèrent, vérifiée en arithmétique exacte ou en Lean ;
- (ii) des mutants équivalents, qui servent de négatifs ;
- (iii) des formalisations produites par des proposeurs LLM, étiquetées par témoin quand il existe, sinon « indéterminé » (exclues et comptées) ;
- (iv) des réécritures correctes de même style.

**Duel.**
- **H_A** : le juge par retraduction rate au plus 5 % (illustratif) des cas (i) et (iii).
- **H_B** : il en rate plus.
- Zéro raté sur au moins 59 cas permet de rejeter H_B à 5 % unilatéral (**VÉRIFIÉ** : 0,95⁵⁹ ≈ 0,048 et 0,95⁵⁸ ≈ 0,051).
- Un raté au-delà du nombre pré-enregistré falsifie H_A. La relecture humaine de chaque énoncé reste alors obligatoire.
- Les fausses alertes sur (ii) et (iv) ont leur propre borne, fixée d'avance.

**Coût.** Des jours d'ingénierie. Le coût dominant est la certification des témoins de séparation.

### P5'. Valeur de réemploi de l'archive des morts

**Mesure.**
- Classes définies a priori par le couple (hypothèse violée, type de témoin : Dirac, support fini, horizon), sur une liste close.
- Masse manquante f₁/N rapportée.

**Duel.**
- On prend des énoncés faux et des énoncés vrais d'une course ultérieure, tenus à l'écart.
- Bras 1 : rejouer les témoins de l'archive.
- Bras 2 : rejouer autant de témoins génériques du générateur planté.
- **H_A** : le bras 1 tue plus d'énoncés faux, par un test de McNemar exact apparié au niveau pré-enregistré.
- **H_B** : il n'en tue pas plus.
- Le taux de mort d'énoncés vrais, c'est-à-dire d'erreurs de traduction (E), reste sous un seuil fixe séparé. Je n'emploie pas une conjonction « ≤ empirique », que A et C ont montrée viciée chez D.

### H-Lean. Le harnais devient un test

Le harnais applique trois vérifications :
1. `#print axioms` sur une liste close d'axiomes autorisés ;
2. un témoin que les hypothèses sont habitées ;
3. un contre-témoin de frontière ∃x′, ¬P(x′) ∧ ¬Q(x′) : il montre que les hypothèses travaillent et que la conclusion n'est pas une tautologie.

**Lot planté.** Des théorèmes vacus, et des théorèmes rendus vrais par x/0 = 0 ou par la soustraction tronquée sur ℕ.

**Duel.**
- H_A : les vérifications 2 et 3 rejettent ce lot, que `#print axioms` laisse passer, sans rejet de théorèmes corrects appariés.
- H_B : `#print axioms` et la retraduction suffisent.
- L'admission d'un énoncé dégénéré par le seul `#print axioms` falsifie H_B. L'absence de tout rejet propre aux vérifications 2 et 3 falsifie H_A.

---

## (c) Réponse à l'arbitre, en une page

**1. Ce qu'un expert ferait.** Il reconnaîtrait la forme classique de chaque question avant de calculer quoi que ce soit.
- L'agrégation sous corrélation adverse est un test minimax entre deux hypothèses composites convexes : les classes de Fréchet.
- « La sonde est aveugle » est une question de pseudo-aléa contre les demi-espaces.

*Établi.* Ces cadres existent (RAPPORTÉ). La route de Huber–Strassen exige la 2-alternance, que la probabilité supérieure d'une classe de Fréchet ne vérifie pas dès 2×2 (VÉRIFIÉ ici, à faire relire).

*Non établi.* Qu'aucun autre classique ne couvre la question.

**2. Données brutes.** La liste de III.1 tient. Deux ajouts :
- l'archive des morts **avec ses témoins** ;
- des marges réelles de scores honnêtes et de sabotage. Sans elles, P2' reste un exercice sur des marges choisies, et je ne sais pas si le programme les a.

**3. Méthodes.** L'inventaire de III.1 tient : FunSearch, AlphaEvolve (titre à vérifier), Wagner, SAT, Ramanujan Machine, autoformalisation, LeanDojo, Draft-Sketch-Prove, blueprints. Les critiques m'en ont appris la leçon principale. **Le LLM ne doit chercher que là où aucun solveur exact n'existe.** Dans P2' et P3', la couche intérieure est un LP exact. La recherche guidée ne vaut que sur la couche non convexe (le support), et cela se mesure (P3').

*Établi (RAPPORTÉ).* Les succès publiés réunissent trois éléments : un problème choisi par un expert, un vérificateur mécanique et un objet de type ∃.

*Non établi.* Que cela se transporte aux statistiques de détection.

**4. Vérification hors du programme.**
- *Vrai.* Noyau Lean avec les trois vérifications de H-Lean. Certificats rationnels rejoués par un vérificateur écrit depuis la spécification, et non depuis le solveur.
- *Nouveau.* Pointeur vérifié, rappel calibré par énoncés plantés (P1'), au moins un spécialiste extérieur.
- *Utile.* Décision pré-enregistrée, jugée sur des mondes scellés tirés d'un générateur distinct, contre un bras placebo.
- *Réplication.* Autre graine et autre lignée.

**5. Demande reformulée.** « Pour chaque question cible, livrer :
- soit "réduit", avec un pointeur vérifié ;
- soit "non réduit dans le périmètre P", avec le rappel calibré ;
- soit un objet certifié exactement, de type valeur, paire la moins favorable ou contre-exemple, ou une preuve auditée, dont l'énoncé a passé le banc P4'.

Joindre la décision de conception qu'il change sur des mondes scellés, face à un placebo. "Déjà connu" est une issue valide. »

**6. Propositions** (HYPOTHÈSE ; coûts illustratifs).

| Proposition | Rôle | Coût | Test de mort |
|---|---|---|---|
| P2' | Seule proposition candidate à un objet nouveau | Dizaines de dollars de CPU, puis des jours d'expert | Écart nul partout |
| P1' | Filtre | Jours d'expert | Un « réduit » vérifié |
| P4' | Instrument | Jours d'ingénierie | Plus de 5 % de ratés |
| P3' | Mesure de méthode | Centaines de dollars | Pas de gain sur supports aléatoires |
| P5' | Diagnostic | Faible | Témoins génériques aussi efficaces |

Les différences avec le publié sont indiquées en (b).

Honnêteté sur la chance. L'issue la plus probable reste « réduit » ou « connu ». Si P2' trouve un écart, ce n'est pas encore un résultat. Le résultat serait la **forme close** de la paire la moins favorable, et la prouver demande un probabiliste, sur une durée que je ne sais pas chiffrer. Je ne sais pas estimer la probabilité d'une découverte.

**Expérience à faire en premier.** P2' sur une petite grille, en trois étapes :
1. Un probabiliste relit le contre-exemple 2×2 et l'identité du cœur. C'est une affaire de minutes.
2. On résout le LP pour k = 1 (contrôle de Neyman–Pearson), puis pour k = 2 et k = 3, sur trois grilles emboîtées, en rationnel exact, contre les règles connues pré-enregistrées, en régime R puis en régime J.
3. En parallèle, P1' cible cette seule question, avec 10 énoncés plantés.

Chaque issue falsifie quelque chose :
- un écart nul partout clôt la piste ;
- un écart stable fournit un objet exact à conjecturer, avant tout appel coûteux à un modèle.

FIN-DE-CELLULE