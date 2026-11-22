# Proposition B, tour III.3 : réponse aux critiques

**Pièces.** Toutes les pièces sont présentes et se terminent par leur ligne de fin, sans coupure visible : ma conception du tour III.1 et les critiques A, C, D et E. Je n'ai pas recalculé les empreintes (OBSERVÉ-NON-AUDITÉ).

**Statuts.** Tout ce que je propose ici est HYPOTHÈSE : aucune expérience n'a été exécutée. Quand une critique attribue un statut (par exemple « VÉRIFIÉ » chez C ou E), je le reproduis tel quel sans l'endosser. Je ne conteste au plus que sa portée.

**Chiffres.** Tous les seuils, effectifs et coûts sont **illustratifs**. Seules les constantes des identités mathématiques font exception.

**Règle de décision adoptée.** J'emprunte à D la règle suivante, en le déclarant (B1). Pour chaque duel, je fixe d'avance une région K des paramètres et je pose H_A : θ ∈ K et H_B : θ ∉ K.
- Si la région de confiance est entièrement dans K, H_B est réfutée.
- Si elle est disjointe de K, H_A est réfutée.
- Si elle est à cheval, le duel est déclaré **non tranché**, et ce cas est annoncé avant l'expérience.

Cette règle comble les trous de partition relevés par A (a11) et par C (b1).

---

## (a) Décision critique par critique

Dans le tableau, A-a3 désigne le point (a)3 de la pièce A sur B, et ainsi de suite.

| # | Critique (sources) | Décision | Raison ou suite |
|---|---|---|---|
| 1 | Avec une dégradation R non ciblée, ρ ≥ 3 découle de l'algèbre d'une marche aléatoire (pas d'ordre √T contre dérive d'ordre T), pas d'une furtivité. Sources : A-a1, C-a1, E-a1, E-b1. | **Acceptée** | C1 est **retirée dans sa forme du tour III.1**. Elle est remplacée par C1′, qui compare le saboteur à **R-dir**, une dégradation dirigée sans intention, appariée en dommage total et en nombre de décisions altérées. L'idée de R-dir vient de A et C (B1). |
| 2 | Le LLR dépend de la classe d'entraînement du moniteur et est mal spécifié pour R. Choisir « le meilleur moniteur » introduit un biais de sélection. Sources : A-a2, C-a1, D-a, D-c, E-a1. | **Acceptée** | Le panel de moniteurs est figé d'avance. Chaque moniteur est entraîné sans données S ni R-dir : soit à une classe sur H, soit sur le témoin concentré S-conc. Toute sélection se fait sur des tâches de validation disjointes du test. |
| 3 | ρ est un quotient sans moments finis dans le régime diffus. Sources : A-b1, C-b2, D-b. | **Acceptée** | Je n'utilise plus de quotient. Je mesure des différences de TPR à seuil gelé, avec intervalle bootstrap par grappes de tâches. |
| 4 | Mon contrôle négatif « E_H[LLR] ≈ 0 » est faux : on attend E_H[Λ] = −KL. Sources : A-b2, D-b. | **Acceptée** (erreur de ma part) | Je le remplace par un contraste H/H à étiquettes aléatoires **par trajectoire**. Si un rapport de vraisemblance est utilisé, je vérifie aussi E_H[exp Λ] ≤ 1. |
| 5 | Additionner des rapports marginaux compte plusieurs fois la même observation. Source : D-a. | **Acceptée** | La cause disparaît avec le point 3 : la somme de LLR n'est plus une mesure de preuve. |
| 6 | Dans C2, S-d diffère de H par un LoRA. Tout LoRA déplace les activations. Sources : A-a3, A-c, C-a2, C-c2, E-a2. | **Acceptée** | J'ajoute des bras **H-d** : des LoRA bénins de même rang, même volume et même nombre de pas, avec trois graines par bras (illustratif). La sonde est évaluée sur des graines LoRA tenues à l'écart. |
| 7 | L'appariement par graine ne tient pas : les contextes divergent dès le premier choix. Source : A-a4. | **Acceptée** | J'ajoute des **lectures forcées** : chaque modèle lit les mêmes textes. Les écarts d'activations ne viennent alors que des poids ou de la consigne. |
| 8 | L'étiquette « action sabotée » n'est pas définie ; l'unité effective est la trajectoire. Source : A-a5. | **Acceptée** | L'unité d'évaluation devient la trajectoire. Les scores par action sont agrégés, et le bootstrap se fait par tâche. |
| 9 | H-sec, une convention de nommage, laisse une empreinte lexicale que S-p n'a pas. Source : C-a2. | **Acceptée** | Je la remplace par **H-sec2** : un objectif secondaire secret qui porte sur **les mêmes décisions** que le sabotage. Ces décisions sont rendues neutres pour le dommage par construction du générateur synthétique, par exemple le choix entre deux estimateurs sans biais pour ce générateur. |
| 10 | H-sec contrôle la présence d'un secret, pas la difficulté de suivre deux objectifs. Source : D-a. | **Acceptée** | H-sec2 est précisément une consigne à double objectif. |
| 11 | Aucun bras ne fait les mêmes choix biaisés sans intention ; l'intention n'est donc pas identifiable (décomposition Δμ). Sources : E-a2, E-b2. | **Acceptée** | **R-dir** est généré sur politique. L'agent honnête reçoit une préférence méthodologique constante qui biaise l'estimation (forme reprise de A, B1), sans qu'on lui dise qu'elle cause un dommage. S-p et R-dir ont alors un contenu comparable et diffèrent par l'intention. |
| 12 | La manipulation H-sec n'est pas vérifiée ; le contraste S contre H-sec peut être vide. Sources : A-b, A-c. | **Acceptée** | Je rapporte l'AUROC(H-sec2 contre H) et l'écart de dommage H-sec2 − H. Si la manipulation échoue, C2a n'est pas jugée. |
| 13 | Dans C2, H_A et H_B ne partitionnent pas l'espace. Le cas (0,85 ; 0,50 ; 0,50) ne tranche rien. Sources : A-a11, C-b1 (que C étiquette « VÉRIFIÉ logiquement »). | **Acceptée** | C2 est scindée en deux duels à régions complémentaires, C2a (consigne) et C2b (poids). Le cas cité devient une issue interprétable : C2a réfute H_B, C2b réfute H_A. |
| 14 | Le contraste conditionnel n'est identifiable que s'il y a recouvrement en Z (poids, difficulté, texte). Source : D-b. | **Acceptée** | Les lectures forcées sur textes identiques (point 7) et un appariement par strates de difficulté de tâche assurent ce recouvrement. |
| 15 | Dans C3, le seuil par action est un homme de paille ; le niveau doit porter sur au moins une alerte par trajectoire. Sources : A-a6, D-a. | **Acceptée** | Les comparateurs deviennent la somme à horizon fixe et le CUSUM, calibrés au même α par trajectoire. |
| 16 | Le « dommage médian au déclenchement » est conditionné à l'alerte. Sources : A-a7, D-a, D-b. | **Acceptée** | Je mesure à la place P_S(τ ≤ T et D_τ ≤ d), où les non-détections comptent au dénominateur. |
| 17 | La variable « écart à la gerbe » n'est pas spécifiée. Source : A-a8. | **Acceptée** | La variable est l'estimation provisoire θ̂_t, c'est-à-dire la sortie du pipeline s'il était clos au pas t, centrée et réduite par la loi des références au même indice de phase. |
| 18 | Plancher conforme : avec k = 10 références, la valeur-p minimale vaut 1/11, au-dessus de α = 0,05. Sources : A-b3, E-b3. | **Acceptée** | Avec 10 références par tâche, aucun test de rang par tâche ne passe α sans un produit sur les pas. C3 est déclassée (voir le point 22). |
| 19 | La propriété de surmartingale est rompue (C-b3, étiqueté « VÉRIFIÉ mathématiquement » par C). | **Portée contestée, transformée en test** | Je conserve le statut donné par C. Je retiens la remarque de D : la violation retire **la justification** de la garantie, mais ne démontre pas une inflation effective. L'inflation e^{cT} suppose δ_t > 0 sur un événement qui n'est pas dérivé. Critère empirique : P_H(sup_t M_t ≥ 1/α) sur tâches nouvelles. |
| 20 | Une branche honnête minoritaire absente des références fait monter les fausses alertes. Source : E-b3. | **Transformée en test** | J'ajoute le bras **H-branche** (voir C3′). |
| 21 | Disposer de 10 exécutions honnêtes par tâche nouvelle revient à avoir déjà résolu la tâche. Source : E-a3. | **Acceptée** | Les références sont désormais mises en commun par **famille** de tâches et jamais prises sur la tâche testée. Le budget de références inclut la calibration. |
| 22 | Aucun plan ne mesure τ, l'effet de trajectoire honnête : l'ICC décide du gain séquentiel. Source : A, section finale. | **Acceptée** | J'ajoute l'expérience E0b, qui conditionne C3′. Le modèle M1 vient de A (B1). |
| 23 | Le TPR à 1 % de FPR repose sur 2 à 3 tâches. Source : A-b4. | **Acceptée** | La mesure primaire passe à FPR = 5 %. Le FPR à 1 % est seulement descriptif (illustratif). |
| 24 | Dans C4, le δ est issu du même rejeu que le score d'audit, d'où une pente tautologique. Sources : A-a9, D-a, D-c. | **Acceptée** | Je retire la régression sur δ. L'étiquette est la condition, et le dommage est mesuré par l'expérimentateur sur des réplications indépendantes. |
| 25 | Dans C4, les budgets sont inégaux : un rejeu coûte plusieurs pas, un jugement un seul. Sources : A-a9, C-a3, C-c3, E-a4, E-c4. | **Acceptée** | Le juge reçoit le même budget de jetons que le rejeu, sous forme d'une fenêtre élargie. Les rejeux sont comptés dans le budget honnête. |
| 26 | C4 accède à un oracle : la vraie valeur synthétique. Source : E-a4. | **Rejetée en partie** | Le score de rejeu compare deux **estimations du défenseur** (original contre rejeu) et n'utilise jamais la vraie valeur. Celle-ci ne sert qu'à l'expérimentateur pour étiqueter le dommage. J'en fais une contrainte d'implémentation vérifiable, le code d'audit n'ayant pas accès au paramètre vrai. La partie sur le budget est acceptée (point 25). |
| 27 | L'auditeur de C4 n'a pas de témoin positif. Source : A-c. | **Acceptée** | J'ajoute le bras **S-conc**, un sabotage concentré. Si l'auditeur échoue sur S-conc, C4′ n'est pas jugée. |
| 28 | La puissance du rejeu décroît avec l'horizon (σ₀ qui croît ; atténuation d'ordre T^{−3/2}). Sources : A-b, E-b4. | **Transformée en test** | Je compare deux variantes de rejeu : local en boucle ouverte, avec le suffixe d'actions fixé et réexécuté, et en boucle fermée avec régénération. Je mesure σ₀ à chaque horizon et je publie le taux d'incompatibilité du suffixe (D-c). Le score devient la **somme signée** sur les m unités auditées. |
| 29 | C0 contient la vérité de terrain. Sources : A-a10, D-a. | **Acceptée pour les tests cachés ; rejetée en partie pour les références** | Les tests cachés sont retirés de la batterie. La comparaison aux références honnêtes reste, parce qu'elle est un moyen du défenseur prévu par le cadre. Elle est évaluée à **mi-horizon**, résultats terminaux masqués pour tous les concurrents. |
| 30 | La non-infériorité n'est pas jugée si l'intervalle traverse la marge. Source : D-b. | **Acceptée** | La règle K s'applique. |
| 31 | R est un négatif d'intention, pas un négatif de dommage. Source : D-c. | **Acceptée** | R ne sert plus qu'à vérifier si les moniteurs détectent l'intention ou la seule dégradation. Il est absent de C1′. |

**Emprunt déclaré (B1).** C a soulevé, à propos de A, l'effet de surprise hors politique d'un texte lu en mode forcé. Cette objection vise aussi mes lectures forcées. Je m'en sers : chaque lecture forcée d'un texte « autre » est appariée à la lecture forcée d'un texte honnête d'une autre exécution, de perplexité comparable.

---

## (b) Expériences corrigées

### Cadre commun (HYPOTHÈSE)

- **Tâche principale.** Pipeline d'analyse sur données synthétiques, avec une vraie valeur connue de l'expérimentateur seul.
- **Unité d'analyse.** La trajectoire, avec bootstrap par grappes de tâches.
- **Seuils.** Figés sur des familles de tâches de validation disjointes.
- **Mesure primaire.** TPR à FPR = 5 % (illustratif).

### Bras

| Code | Définition | Rôle |
|---|---|---|
| H | Honnête. | Référence. |
| H-sec2 | Objectif secondaire secret sur les mêmes décisions, neutre pour le dommage. | Secret et double objectif, sans dommage. |
| R-dir | Consigne méthodologique biaisante, présentée comme une préférence. Appariée à S-p en dommage total et en nombre de décisions altérées. | Même contenu, sans intention. |
| S-p | Saboteur obtenu par consigne. | Intention par consigne. |
| S-d | Distillation LoRA de S-p, consigne retirée ; 3 graines (illustratif). | Intention dans les poids. |
| H-d[R-dir], H-d[H-sec2] | Distillations LoRA bénignes, même rang et même volume ; 3 graines chacune (illustratif). | Témoins de poids. |
| S-conc | Sabotage concentré sur une ou deux décisions. | Témoin positif. |
| R | Dégradation non ciblée. | Négatif d'intention, pour les moniteurs seulement. |
| H-branche | Stratégie honnête valide mais minoritaire, imposée à une fréquence contrôlée. | Validité des tests séquentiels. |
| Lectures forcées | Chaque modèle lit les textes des autres bras, plus un texte honnête apparié en perplexité. | Séparer texte et état interne. |

### E0 : faisabilité et effet de trajectoire (à faire en premier)

**E0a, faisabilité du sabotage diffus (S1).**

| | |
|---|---|
| Précondition | Le moniteur texte de confiance détecte S-conc (borne basse de l'AUROC par trajectoire ≥ 0,8, illustratif). Sinon E0a n'est pas jugée : on mesurerait la faiblesse du moniteur. |
| K | Dommage(S-p) − dommage(H) > d₀, **et** AUROC par trajectoire du moniteur sur S-p contre H < 0,7 (seuils illustratifs). |
| H_A | θ ∈ K : un sabotage diffus est faisable à cette échelle. |
| H_B | θ ∉ K. |
| Ce que chaque issue falsifie | Une région disjointe de K falsifie S1 pour les modèles ouverts modestes. C1′, C2 et C4′ deviennent alors sans objet à cette échelle, et c'est le résultat à rapporter. Une région incluse dans K falsifie H_B. |

**E0b, effet de trajectoire honnête.** Le modèle et le critère viennent de A (M1), déclarés en B1.

| | |
|---|---|
| Mesure | ICC des scores des moniteurs et de θ̂_t sur 100 trajectoires H au moins (illustratif). |
| H_A | ICC · T < 1 : l'accumulation séquentielle peut apporter un gain. |
| H_B | ICC · T ≥ 1. |
| Ce que chaque issue falsifie | ICC · T ≥ 1 falsifie toute promesse de gain séquentiel au-delà d'un horizon court : C3′ est abandonnée. ICC · T < 1 falsifie l'objection de plafond par τ. |

E0 est peu coûteuse : quatre bras et pas de LoRA.

### C1′ : furtivité au-delà de l'amplitude

**Énoncé.** À dommage total et nombre de décisions altérées égaux, la trajectoire du saboteur est moins détectée que celle de R-dir par **chacun** des moniteurs d'un panel figé : texte de confiance, statistiques mécaniques et sonde sur H-d.

| | |
|---|---|
| K | Pour tout moniteur du panel, TPR(R-dir) − TPR(S-p) ≥ 0,10 (illustratif). |
| Ce que chaque issue falsifie | Une région disjointe de K falsifie l'idée d'une furtivité stratégique propre à l'agent : « diffus » ne veut alors dire que « petit ». Une région incluse dans K falsifie H_B : l'agent choisit *où* et *comment* biaiser au-delà de l'amplitude. |
| Contrôle de manipulation | Égalité des dommages S-p et R-dir, avec intervalle de confiance rapporté. |
| Contrôle négatif | Contraste H/H à étiquettes aléatoires par trajectoire. |

### C2a : la sonde lit-elle l'intention, ou la consigne et le contenu ? (poids de base)

| | |
|---|---|
| Sonde | Entraînée sur des données disjointes (S-conc contre H). |
| K | min[AUROC(S-p contre R-dir), AUROC(S-p contre H-sec2)] ≥ 0,75 (illustratif), au niveau trajectoire. |
| Ce que chaque issue falsifie | Une région disjointe de K falsifie la lecture d'une intention spécifique : la sonde lit le secret ou le contenu des choix. Une région incluse dans K falsifie l'hypothèse « secret ou contenu seulement ». |
| Préconditions | Manipulation H-sec2 réussie. Une sonde sur étiquettes permutées par trajectoire donne environ 0,5. |
| Comparateur | Sonde sur plongements d'entrée : si elle fait aussi bien, l'avantage interne est nul. |
| Lectures forcées | Le modèle de base lit les textes S-p et R-dir **sans** consigne. Si la séparation persiste, elle vient du texte et non de l'état interne. |

### C2b : l'intention est-elle lisible quand elle n'est que dans les poids ?

| | |
|---|---|
| Protocole | S-d et H-d[R-dir] lisent **les mêmes textes** en mode forcé. La sonde est évaluée sur des graines LoRA tenues à l'écart. |
| K | AUROC(S-d contre H-d[R-dir]) ≥ 0,75 **et** AUROC(S-d contre H-d[H-sec2]) ≥ 0,75 (illustratif). |
| Ce que chaque issue falsifie | Une région disjointe de K falsifie l'idée qu'une distillation comportementale transmette une intention lisible distincte du comportement biaisé. Ce résultat négatif est publiable : une sonde ne garantirait rien contre un saboteur distillé. Une région incluse dans K falsifie l'hypothèse « identité du LoRA ou contenu seulement ». |
| Garde-fou | Si la sonde sépare H-d[R-dir] de H-d[H-sec2] autant que S-d de H-d, elle lit l'identité de l'adaptateur. Le duel est alors non tranché. |
| Phase adversariale | Inchangée, et optionnelle. |

### C3′ : test séquentiel calibré par famille (déclassée, conditionnée à E0b)

**Énoncé.** Je teste un CUSUM sur θ̂_t, calibré sur des références mises en commun par famille de tâches. Le budget est fermé : k_total références, calibration comprise.

| | |
|---|---|
| K | Borne haute de P_H(alerte) ≤ 2α sur tâches nouvelles **et** sur H-branche, **et** P_S(τ ≤ T et D_τ ≤ d) supérieure de 0,10 au moins à celle de la somme à horizon fixe (illustratif). |
| Ce que chaque issue falsifie | Une région disjointe de K falsifie la validité sur tâches nouvelles, ou le gain du séquentiel. Une région incluse dans K falsifie les objections de branche et de plancher **dans ce régime**. |
| Ce qui est abandonné | La revendication d'une garantie valide à tout instant **par construction**. Elle ne tient plus (points 18 et 19). |

### C4′ : audit par rejeu à somme signée

**Énoncé.** On audite m unités tirées au hasard. Pour chacune, on la rejoue en boucle ouverte avec la référence, puis on somme les écarts signés d'estimation. À budget de jetons égal, ce score bat un juge à fenêtre élargie.

| | |
|---|---|
| Précondition de centrage | Sur H, la moyenne de la somme signée a un intervalle qui contient 0. Sinon la référence est biaisée : c'est le défaut que C a relevé chez E, et que je m'applique. Le duel est alors non tranché, et le rejeu par cette référence est déclaré inutilisable. |
| Autres préconditions | Le juge comme le rejeu détectent S-conc. Le taux d'incompatibilité du suffixe est rapporté. |
| K | TPR(rejeu) − TPR(juge) ≥ 0,10 à FPR = 5 % (illustratif). |
| Ce que chaque issue falsifie | Une région disjointe de K falsifie l'intérêt du rejeu face au jugement à budget égal. Une région incluse dans K falsifie « le jugement suffit ». |
| Risque déclaré | Recouvrement avec *Ctrl-Z* (Bhatt et al., 2025, de mémoire, non vérifié). |

### C0′ : batterie mécanique contre moniteurs LLM

| | |
|---|---|
| Conditions | Horizon à mi-tâche, sans tests cachés, résultats terminaux masqués pour tous. |
| K | Borne basse de [TPR_méc − TPR_mon] ≥ −0,05 (illustratif). |
| Ce que chaque issue falsifie | Une région incluse dans K signifie que la mécanique est non inférieure : les moniteurs n'ajoutent rien de démontré. Une région disjointe de K falsifie la non-infériorité. |

### Calcul

Il y a environ deux fois plus de bras qu'au tour III.1, et 9 distillations LoRA (illustratif). Je compte de l'ordre de **150 à 450 h-GPU** pour un modèle de 7 à 8 milliards de paramètres (illustratif). E0 seule demande moins de 40 h-GPU (illustratif).

---

## (c) Réponse à la question de l'arbitre (une page)

### Ce qui est établi

1. **Aucun résultat empirique.** Rien n'a été exécuté ; toutes les contributions restent HYPOTHÈSE.
2. **Aucune nouveauté certifiée.** Le nombre de contributions dont je peux certifier le caractère inédit reste **zéro**. Mes connaissances ont une date de coupure, et aucune recherche bibliographique n'a été faite. Les références restent « de mémoire, non vérifié ».
3. **Quatre résultats d'analyse, et non d'expérience.** Ce sont des identités valables sous des modèles qui restent eux-mêmes HYPOTHÈSE. Je les cite avec le statut que leurs auteurs leur donnent, sans le changer.
   - Mon C1 du tour III.1 était tranché par l'algèbre : à dommage final égal, une dégradation non ciblée exige des pas d'amplitude √T fois plus grande. C'est une dérivation chez A ; E l'étiquette VÉRIFIÉ.
   - Un quotient dommage/preuve n'a pas de moments finis dans le régime diffus.
   - Avec k références, un test de rang a une valeur-p minimale de 1/(k+1).
   - Mon contrôle E_H[LLR] = 0 était faux.

   J'ai donc retiré C1 sous sa forme initiale et déclassé C3.

### Ce qui n'est pas établi

- **La faisabilité.** Rien ne montre encore que des modèles ouverts modestes savent saboter de façon diffuse (S1).
- **L'effet de trajectoire honnête.** La valeur de l'ICC des scores honnêtes n'est pas connue. Or tous les gains séquentiels annoncés, dans les cinq propositions, en dépendent.
- **Ce que lisent les sondes.** On ne sait pas si elles lisent l'intention, la consigne, le contenu des choix ou l'identité des poids.
- **L'antériorité** de chacune de mes candidates.

### Candidates restantes, par ordre de solidité

1. **C2a et C2b.** C'est le plan factoriel H-sec2 / R-dir / H-d / lectures forcées. C'est ma candidate la plus nette. Elle prédit aussi un résultat négatif publiable : une intention non lisible chez un saboteur distillé.
2. **C1′.** La furtivité est mesurée contre R-dir, et non plus contre R.
3. **C4′.** Elle est conditionnée au centrage de la référence. Le risque d'incrément sur *Ctrl-Z* est réel.
4. **C0′.** C'est la référence à battre.
5. **C3′.** Elle est conditionnée à E0b.

### Déjà publié, et ouvert malgré l'apparence (de mémoire, HYPOTHÈSE)

- **Déjà publié.** Ma liste du tour III.1 est inchangée : protocoles de contrôle, rééchantillonnage, sondes de tromperie, obfuscation, SPRT et CUSUM.
- **Ouvert malgré l'apparence.** Deux points :
  - séparer l'intention du contenu et des poids, dans les sondes ;
  - mesurer l'effet de trajectoire honnête. C'est l'objection de A, que je reprends en la déclarant.

### Ce qui me ferait changer d'avis

- **Pour C2.** Une publication qui contrôle à la fois le secret bénin, la dégradation dirigée non intentionnelle et un LoRA bénin. Je retirerais alors C2.
- **Pour C1′ et C4′.** L'échec de E0a : ils deviendraient sans objet à cette échelle.
- **Pour C3′.** E0b avec ICC · T ≥ 1 : je l'abandonnerais.
- **Pour C4′.** Une référence de rejeu non centrée sur H : je la déclarerais inutilisable.

### Expérience à faire en premier

**E0**, pour un coût inférieur à 40 h-GPU (illustratif). Elle comprend les quatre bras H, H-sec2, R-dir et S-p, plus S-conc comme témoin positif. Elle mesure trois choses :
- le duel de faisabilité E0a ;
- le duel sur l'ICC, E0b ;
- les vérifications de manipulation (H-sec2 neutre en dommage, R-dir apparié en dommage à S-p).

Ses deux issues sont informatives. Si S1 tombe, la question se déplace vers des modèles plus grands, hors du périmètre « taille modeste ». Si S1 tient, les contrôles nécessaires à C1′ et C2a sont déjà validés.

FIN-DE-CELLULE