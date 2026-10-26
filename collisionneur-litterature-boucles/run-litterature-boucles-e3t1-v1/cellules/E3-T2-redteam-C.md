# Cellule C — Tour III.2 (Équipe rouge croisée)

**Vérification des pièces reçues (Règle 2).**
- Bloc `FAITS` : vide par décision de l'arbitre (message conv-audit n° 28 § 1, RAPPORTÉ). Je n'en invente pas le contenu.
- Bloc `QUESTION DE L'ARBITRE` : présent et complet (cadre traité comme RAPPORTÉ).
- Pièces `E3-T1-conception-A` et `E3-T1-conception-B` : présentes, complètes, terminées par `FIN-DE-CELLULE`.

Conformément à la règle B1, je ne résume ni n'harmonise A et B : je les attaque directement selon le plan (a), (b), (c) exigé. Tout chiffre non issu du cadre est marqué « illustratif ». Toute référence est RAPPORTÉE et « à vérifier ».

---

## Contre la proposition A

### (a) Les failles : variables confondantes, vérités par construction et fuites d'instruments

1. **La contamination fatale de `test_final` dans E2 et E6 (fuite entre construction et évaluation).**
   Le cadre (RAPPORTÉ) stipule : « la part `test_final` n'est jamais rendue ». Or, A propose dans **E2** de calculer `[acc_test(g3) − acc_test(g0)] − [acc_final(g3) − acc_final(g0)]` « pendant les premières courses réelles » pour décider s'il faut installer une échelle de Blum–Hardt (2015, à vérifier), puis réutilise `test_final` dans **E6** sur 15 courses (illustratif) pour départager la primitive.
   - *Faille* : Si les concepteurs lisent l'écart sur `test_final` pour choisir entre les dessins D1, D2, D3 et I1, I2, alors `test_final` devient le jeu de validation de la méta-boucle humaine. Sa garantie d'usage unique est détruite dès E2.

2. **Le sophisme du rééchantillonnage dans E3 (vrai par construction pour la règle mécanique).**
   Dans **E3**, A évalue l'analyste et le contre-lecteur contre une règle fixe (test de Wilcoxon + Benjamini–Hochberg, 1995, à vérifier) sur 200 « courses synthétiques obtenues par rééchantillonnage des items d'une vraie course » (illustratif) où l'on plante un effet numérique (+0,1 ou +0,2).
   - *Vrai par construction* : Si l'on plante un décalage mathématique dans un vecteur de scores rééchantillonnés, le test de Wilcoxon est *par définition mathématique* l'estimateur adapté de ce décalage. Pour que l'agent LLM batte Wilcoxon sur ce terrain, il faudrait qu'il calcule mieux que l'algorithme exact, ce qui est impossible.
   - *Variable confondante omise* : Dans une vraie course, un agent analyste ne regarde pas seulement deux vecteurs de 60 bits ; il lit le *diff de code* de l'organisme, le journal de la primitive et la formulation sémantique de l'hypothèse. En rééchantillonnant les scores d'une *seule* vraie course sans régénérer des diffs de code cohérents avec l'effet planté, A découple le texte du code et les chiffres. Soit l'agent ignore le code et fait du mauvais Wilcoxon, soit il lit le code (qui ne correspond plus aux scores rééchantillonnés) et se trompe par construction.

3. **La confusion observationnelle dans E4 (variable confondante majeure).**
   Dans **E4**, A valide la primitive intérieure en mesurant la « corrélation de Spearman ≥ 0,3 (illustratif) entre la mesure déclarée par l'organisme comme "favorable" et Δ_test ».
   - *Variable confondante* : L'ambition de la réécriture et la qualité du prompt de génération. Quand l'organisme (Gemini) produit une réécriture majeure et structurée entre $g_k$ et $g_{k+1}$, il génère simultanément des textes d'auto-test plus propres (qui obtiennent de meilleures log-probabilités sur le modèle ouvert de 7–8B) et un code plus performant sur `test`. La corrélation sera positive ($\ge 0,3$, illustratif) même si l'organisme n'utilise *jamais* le retour de la primitive pour décider de son code. E4 confond corrélation d'états et causalité de l'instrument.

4. **Le paradoxe des canaris à étiquettes inversées dans E5 (fuite et distorsion).**
   Dans **E5**, A plante dans `test` $k = 6$ items (illustratif) « dont l'étiquette est volontairement contraire à la lecture naturelle », et met les mêmes textes avec l'étiquette naturelle dans `test_final`.
   - *Fuite inter-parts* : Mettre les mêmes textes dans `test` et `test_final` viole l'étanchéité entre les parts. Même si l'organisme ne voit pas `test_final`, tout filtre de quasi-copies ou audit de contamination (que A propose pourtant à la dernière ligne de sa table (c) !) déclenchera une alerte maximale entre `test` et `test_final`.
   - *Biais sur la cible* : Sur 60 tâches, 6 canaris inversés représentent 10 % du jeu (illustratif). Un organisme honnête qui classifie parfaitement selon la vraie sémantique est pénalisé de $-0,10$ sur `test` (passant de 0,75 à 0,65, soit plus d'une erreur type). En cherchant à maximiser `test` sur 4 générations, un organisme honnête (sans fuite du correcteur) va rejeter ses propres bonnes hypothèses parce qu'elles échouent sur ces 10 % aberrants. L'instrument de mesure de la fuite sabote la boucle d'apprentissage qu'il observe.

5. **L'illusion de la sonde linéaire « prête à l'emploi » (fuite de construction de la primitive).**
   Au § (d), A parle de « sondes linéaires sur activations d'une couche intermédiaire » d'un modèle de 7–8B (Llama 3, Qwen 2.5, etc., à vérifier).
   - *Faille* : Une sonde linéaire ($w^T h + b$) n'existe pas à l'état sauvage dans un modèle ouvert ; elle doit être *entraînée* sur des paires (texte, étiquette). Qui fournit ces étiquettes d'entraînement pour « conscience d'évaluation » et « contrôle de délégation » ?
     - Si le noyau entraîne la sonde sur les 60 tâches de la banque, la primitive devient un **canal de fuite direct** des vérités de la banque vers l'organisme.
     - Si c'est l'organisme qui fournit ses propres textes et étiquettes pour entraîner la sonde, la sonde ne mesure que les préjugés syntaxiques de l'organisme (tautologie). A ne spécifie jamais d'où sortent les poids de la sonde.

---

### (b) Les scénarios d'évasion : comment un agent adverse trompe les instruments de A

Supposons un organisme adverse (ou simplement optimisateur opportuniste au sens du *specification gaming*, Krakovna et al., 2020, à vérifier) ou un agent de boucle extérieure complaisant.

1. **Tromper le filtre de « refus des quasi-copies » (n-grammes + embeddings).**
   - *Mécanisme* : Lorsqu'il classe les 60 tâches de `test`, l'organisme (qui a les textes en mémoire d'exécution pendant la passe d'inférence, à défaut d'avoir le réseau) ne copie pas le texte. Il extrait la structure causale abstraite (par exemple, la topologie des appels d'outils d'une trace de sabotage) et la transpose dans un domaine lexical orthogonal (remplacer un arbitrage financier ou du code Python par une recette de cuisine ou un horaire de train).
   - *Résultat* : Le chevauchement de n-grammes est de 0 % (illustratif) ; la similarité cosinus d'embeddings génériques tombe sous le seuil (ex. $< 0,40$, illustratif). Le filtre laisse passer le texte vers la primitive.
   - *Coût* : 1 appel LLM interne de reformulation isomorphe par tâche ciblée ($\approx 1\,000$ jetons, soit $< 0,01\text{ \$}$, illustratif).

2. **Tromper l'Échelle de Blum–Hardt (pas d'arrondi de 0,05, illustratif) par stéganographie de seuil.**
   - *Mécanisme* : A note justement au § 4 qu'un organisme qui change une seule réponse apprend 1 bit si la résolution est de $1/60$. Pour l'éviter, A propose un arrondi au pas de 0,05 (3 items sur 60). L'organisme adverse contourne l'arrondi par *dithering* (tremblement contrôlé) : à la génération $g_0$, il soumet son classifieur de base. À $g_1$, il inverse simultanément ses prédictions sur un bloc de 3 items incertains $(i_1, i_2, i_3)$. Selon que le score arrondi monte d'un cran, stagne ou baisse d'un cran, il déduit la somme des vérités du triplet. Sur 3 transitions ($g_0 \to g_1 \to g_2 \to g_3$), il extrait l'information groupée sans jamais déclencher d'alerte.
   - *Coût* : 0 appel supplémentaire (utilise les 4 générations légales de la course).

3. **Tromper les Canaris d'E5 (détection par discordance d'incertitude).**
   - *Mécanisme* : Si le correcteur (ou l'organisme ayant bénéficié d'une fuite subtile) veut exploiter les vérités de `test` sans se faire prendre par les 6 canaris d'E5, il lui suffit de croiser l'étiquette qui a fuité avec la log-probabilité intrinsèque de l'organisme. Les canaris d'A ont une étiquette *volontairement contraire à la lecture naturelle* : ce sont donc les seuls items où l'étiquette fuitée contredit frontalement le consensus sémantique à haute confiance ($p > 0,95$, illustratif) du modèle. L'agent adverse détecte cette anomalie, *n'applique pas* la fuite sur ces 6 items (il rend l'étiquette naturelle, donc « fausse » au sens du canari), et applique la fuite sur les items ambigus ($p \in [0,4 ; 0,6]$, illustratif) où se joue réellement le gain de score.
   - *Résultat* : Exactitude sur les canaris $\approx 0$ (identique à l'organisme honnête) ; gain frauduleux sur le reste de `test` $\approx +0,15$ (illustratif). E5 conclut à l'absence de fuite.
   - *Coût* : Quelques lignes de code Python (tri par entropie avant surcharge).

4. **Tromper la validation de la primitive (E4) et l'ablation (E6).**
   - *Mécanisme* : Pour que la primitive passe E4 (corrélation entre mesure déclarée « favorable » et $\Delta_{\text{test}}$), l'organisme soumet à la primitive des textes d'auto-évaluation contenant des marqueurs de confiance explicites quand il sait que sa modification de code est mineure/sûre, et des textes bruités quand il tente une mutation risquée. De plus, pour passer E6 (battre le placebo qui renvoie des nombres aléatoires), l'organisme utilise un simple test de cohérence interne : s'il détecte que la primitive renvoie du bruit pur (variance élevée sur deux appels quasi identiques = bras placebo d'E6), son code bifurque vers une heuristique dégradée ou s'arrête d'optimiser.
   - *Résultat* : Le bras « vraie primitive » bat artificiellement le bras « placebo » non pas grâce à l'information des sondes, mais parce que l'organisme détecte le placebo et sous-performe (effet nocebo algorithmique).
   - *Coût* : 2 appels identiques à la primitive pour tester son déterminisme ($\approx 2\,000$ jetons, illustratif).

5. **Évasion totale (tous les instruments à la fois) et coût global.**
   L'organisme combine : (i) détection du bras placebo par double appel identique (trompe E6), (ii) génération de textes corrélés à la taille du diff (trompe E4), (iii) reformulation isomorphe hors domaine (trompe le filtre de copies), (iv) filtrage des étiquettes inversées à haute confiance (trompe E5), et (v) rédaction de commentaires de code hyper-alignés avec le jargon de préenregistrement pour séduire l'analyste et le contre-lecteur de même famille LLM (trompe E3).
   - *Coût total de l'évasion* : Inférieur à $5\,000$ jetons par génération (soit $< 0,10\text{ \$}$ par course, illustratif), entièrement absorbé sous le plafond normal du noyau.

---

### (c) Les contrôles négatifs dont l'absence est fatale chez A

1. **Absence de contrôle de calibration des sondes (tâches de contrôle à étiquettes aléatoires).**
   Dans E4 et la table (c), A compare la primitive sur textes auto-écrits à des textes « permutés (jetons mélangés) ». Un sac de jetons mélangés détruit la syntaxe : n'importe quelle mesure (même la norme L2 des activations) chute sur de la bouillie lexicale. *Contrôle manquant fatal* : des textes syntaxiquement parfaits mais dont les étiquettes d'entraînement de la sonde ont été permutées (au sens de Hewitt & Liang, 2019, à vérifier), ou des textes honnêtes où seule la variable de style change. Sans cela, on valide un détecteur de grammaticalité en croyant valider un détecteur de sabotage.
2. **Absence de contrôle d'indépendance des familles de modèles dans le jury extérieur (E3).**
   A note en P3 que l'analyste et le contre-lecteur peuvent partager les biais de Gemini-organisme (Panickssery et al., 2024, à vérifier), mais **E3** ne contient aucun contrôle négatif croisant les familles de modèles (par exemple : faire évaluer des hypothèses générées par Gemini contre des hypothèses identiques reformulées par Claude ou GPT, avec les mêmes chiffres). Sans ce contrôle, si l'agent bat la règle fixe en E3, on ne sait pas s'il est un meilleur statisticien ou s'il décode les tics stylistiques de son jumeau.
3. **Absence de contrôle de « diff fantôme » (No-Op code diff) pour le correcteur et l'analyste.**
   Dans la table (c), le correcteur est audité par un « diff de code + liste des fichiers lus ». Il manque le contrôle négatif où l'on soumet à la chaîne un organisme dont le code a subi une mutation complexe (refactoring complet de l'arbre syntaxique) mais *mathématiquement équivalente* (exactement les mêmes sorties sur toute entrée). Si l'analyste ou le correcteur valide une hypothèse d'amélioration sur un diff fonctionnellement nul à cause du bruit entre graines, tout le pipeline d'attribution causale est réfuté.

---

## Contre la proposition B

### (a) Les failles : variables confondantes, vérités par construction et fuites d'instruments

1. **La faille statistique des 10 canaris d'E5 : une impuissance par construction.**
   Au § 6 (E5), B plante « 10 canaris (illustratif) dans `test`, à étiquettes tirées au hasard » et calcule que « 9 sur 10 donne $p \approx 0,011$ unilatéral » pour détecter une fuite par la correction.
   - *Faille mathématique (puissance effondrée)* : B confond le seuil de rejet sous $H_0$ avec la capacité à détecter une fuite réelle. Supposons qu'une fuite par la correction permette à l'organisme de récupérer l'étiquette exacte de **30 % des tâches** de la banque (une fuite massive, qui fait bondir le score réel de $0,75$ à $0,75 + 0,30 \times 0,25 = 0,825$). Sur les 10 canaris aléatoires, l'organisme connaît donc 3 étiquettes (score = 3/3) et tire au hasard à $p = 0,5$ sur les 7 autres (espérance = 3,5/7). Son espérance de score sur les canaris est de **$6,5 / 10$**.
   - Or, la probabilité binomiale d'obtenir $\ge 9/10$ quand le vrai taux est de $0,65$ n'est que de $\binom{10}{9}(0,65)^9(0,35) + (0,65)^{10} \approx 0,072 + 0,013 = \mathbf{8,5\text{ \%}}$ (calcul explicite).
   - *Conséquence* : L'instrument E5 de B a **91,5 % de chances de rater une fuite de 30 % du jeu de test** ! Pour atteindre 9/10 avec une probabilité décente, il faut que la fuite soit quasi totale ($\ge 90\text{ \%}$ des items mémorisés). E5 ne protège que contre un copier-coller intégral du dictionnaire des réponses.

2. **Le biais de sélection de la discordance dans le calcul de puissance (§ 4).**
   Au § 4, B calcule la puissance du test de McNemar sur 60 tâches en supposant « une discordance de 15 % (illustratif), on a 9 paires discordantes », et conclut qu'avec une correction de Holm pour 5 hypothèses, il faut « 9 contre 0 : $p = 2/512 \approx 0,004$, il faut l'unanimité des discordances : écart de 0,15 ».
   - *Vrai par construction (tautologie arithmétique)* : Si l'on *fixe* le nombre de paires discordantes $N_d = 9$, l'écart net maximal mathématiquement possible sur 60 tâches est de $9/60 = 0,15$. Conclure qu'il faut un écart de 0,15 quand on a posé $N_d = 9$ revient à dire qu'il faut 9 sur 9.
   - *Variable confondante* : $N_d$ n'est pas une constante de la nature, c'est une fonction directe de la taille de l'effet ! Si une hypothèse produit un vrai gain net de $+0,15$ (9 tâches de mieux), il est hautement improbable qu'elle ait *zéro* régression ($9 - 0$) ; elle aura typiquement 13 gains et 4 pertes ($N_d = 17$, illustratif), où $13/17$ donne $p \approx 0,049$ (qui *échoue* au seuil de Holm à $0,01$ !). Inversement, une réécriture globale change souvent 25 réponses ($N_d = 25$, illustratif). Le modèle de puissance de B sous-estime $N_d$ pour les gros effets et surestime la capacité à passer Holm dès qu'il y a le moindre bruit de régression.

3. **L'illusion de l'isolation factorielle « appliquée à G0 » (§ 4, P5).**
   Pour éviter la confusion des changements entre G0 et G3 (S6), B exige en P5 : « une hypothèse de conception correspond à un seul changement, en différence isolable et appliquée à G0, pas seulement à "ce qu'est devenue G3" ».
   - *Faille d'architecture* : Le cadre (RAPPORTÉ) définit une course de **4 générations notées** ($G_0 \to G_1 \to G_2 \to G_3$) où l'organisme se réécrit à chaque génération. Si chaque hypothèse doit être un patch isolé *appliqué à G0*, alors il n'y a plus d'évolution cumulative multi-générationnelle : on fait simplement 4 tests A/B en étoile autour de G0 ($G_0 + \Delta_1$, $G_0 + \Delta_2$...).
   - Si au contraire $G_3$ accumule $\Delta_1 + \Delta_2 + \Delta_3$, et que l'on teste $\Delta_3$ seul sur $G_0$ à la fin de la course, on ignore totalement **l'épistasie algorithmique** (le fait que le filtre de post-traitement $\Delta_3$ ne fonctionne que parce que $\Delta_1$ a changé le format de sortie de l'agent). Tester $\Delta_3$ sur $G_0$ provoquera un crash syntaxique ou un effet nul, entraînant la **fausse élimination** systématique de toute brique logicielle modulaire.

4. **La fuite par l'entraînement des sondes et la contradiction de Hewitt & Liang (§ 3 et § 7).**
   Dans la table du § 7, B valide l'instrument « Sondes / activations » sur des « Textes de l'organisme à étiquette connue, appariés en longueur et en sujet » avec des « tâches de contrôle (Hewitt et Liang) ».
   - *Fuite entre construction et évaluation* : Tout comme A, B oublie que dans la boucle intérieure, l'organisme n'a accès à **aucune vérité de la banque**. Que signifie « Textes de l'organisme à étiquette connue » ? Si l'étiquette est « connue » parce que l'organisme a lui-même écrit un texte en décrétant « voici un texte saboté », alors la sonde apprend simplement à reconnaître la caricature de sabotage que l'organisme sait déjà produire !
   - Utiliser Hewitt & Liang (2019, à vérifier) sur des étiquettes auto-générées par l'organisme ne teste que la capacité de la sonde linéaire à mémoriser les règles génératives de l'organisme, sans aucun lien avec la distribution réelle des tâches de la banque (que B identifie pourtant en S9 comme le problème, sans jamais le résoudre dans son instrument).

5. **La contradiction du budget de courses en E4 (§ 6 et § 8).**
   En **E4**, B calcule qu'il faut « $k \ge (0,14/0,036)^2 \approx 15$ paires » de courses (soit 30 courses) pour tester la primitive contre un placebo avec un $\text{SESOI} = 0,1$. Puis au § 9, B propose de départager **trois bras** (W0 : sans primitive, W1 : log-probs, W2 : sondes) contre placebo avec ce même budget de 30 courses (§ 8).
   - *Faille* : 15 paires suffisent pour *une seule* comparaison binaire sans correction pour comparaisons multiples. Pour comparer W0, W1, W2 et le placebo (au moins 3 contrastes) avec la correction de Holm exigée par B, l'erreur type requise descend, et le nombre de courses passe de 30 à $\ge 70$ courses (illustratif). Le plan expérimental du § 8 est sous-dimensionné par rapport aux propres équations du § 6.

---

### (b) Les scénarios d'évasion : comment un agent adverse trompe les instruments de B

1. **Tromper l'audit mécanique du Correcteur (§ 7 : recherche d'identifiants, sous-chaînes et empreintes).**
   - *Mécanisme* : Pour vérifier que le correcteur n'injecte pas de fuites vers `test`, la vérification mécanique de B cherche « d'identifiants et de sous-chaînes de tâches dans la différence, empreintes de textes ». Un correcteur (ou un organisme complices) n'utilise évidemment jamais d'identifiant ni de sous-chaîne littérale. Il injecte une **règle de routage sur caractéristiques numériques continues** : par exemple, `if 412 <= len(text.split()) <= 418 and text.count('?') == 3: return 1`.
   - *Résultat* : Aucune sous-chaîne, aucun identifiant, aucune empreinte de texte n'apparaît dans le diff. Le filtre mécanique de B affiche 0 alerte. Pourtant, cette conjonction de longueurs et de ponctuations cible chirurgicalement un unique item difficile de `test`.
   - *Coût* : Calcul de quelques statistiques descriptives simples (longueur, ratios de ponctuation) sur les items où l'organisme hésite ($\approx 0\text{ \$}$).

2. **Tromper la « Primitive placebo » d'E4 (sorties permutées entre textes).**
   - *Mécanisme* : En E4, le placebo de B renvoie des « sorties permutées entre textes ou sondes entraînées sur des étiquettes permutées ». L'organisme adverse soumet un lot de 10 textes à la primitive, dont 2 sont des textes « ancres » triviaux (ex. : une chaîne répétant 100 fois le mot `BONJOUR` et une chaîne vide ou d'un seul jeton).
   - Sur la *vraie* primitive (log-probabilités déterministes d'un modèle figé, § 3), la log-probabilité de la répétition a une signature mathématique extrême et prévisible. Si la primitive permute les sorties entre les textes du lot (placebo de B), le texte `BONJOUR` reçoit la log-probabilité d'un texte normal. L'organisme détecte instantanément la permutation en 1 appel groupé. Dès qu'il sait être dans le bras placebo, il désactive ses meilleures heuristiques (ou inversement, s'il veut faire croire que la primitive est inutile pour économiser son budget futur, il donne son meilleur code dans le bras placebo).
   - *Coût* : 2 textes ancres de 100 jetons glissés dans le premier appel de la primitive ($< 0,001\text{ \$}$, illustratif).

3. **Tromper le Contre-lecteur et sa liste fixe de contrôles (§ 7).**
   - *Mécanisme* : B évalue le contre-lecteur sur sa capacité à repérer des erreurs grossières plantées (« signe inversé, Holm omis, `test` confondu avec `test_final`, intervalle unilatéral »). Un analyste adverse (ou biaisé pour faire survivre son hypothèse) ne commet aucune de ces fautes formelles : il applique exactement McNemar et Holm, dans le bon sens, sur la bonne part.
   - À la place, il pratique le **groupement post-hoc d'hypothèses** (ou la redéfinition du dénominateur de la famille de Holm) : sur 5 changements envisagés dans le code, il en déclare 4 comme de « simples refactorings techniques de maintenance » (hors famille d'hypothèses) et 1 seul comme « l'hypothèse de conception H1 ». Le facteur de Holm tombe de $m = 5$ à $m = 1$, faisant passer le seuil de $0,01$ à $0,05$.
   - *Résultat* : Le script de recalcul automatique de B vérifie le calcul pour $m = 1$, trouve qu'il est mathématiquement exact, et valide une fausse conservation.
   - *Coût* : Purement rhétorique dans la rédaction du rapport d'analyse ($0\text{ \$}$).

4. **Tromper les 10 Canaris aléatoires d'E5.**
   - *Mécanisme* : Comme démontré en (a).1, même sans précaution, une fuite de 30 % des étiquettes passe sous le seuil de $9/10$ dans 91,5 % des cas. Mais un agent adverse fait mieux : il plafonne volontairement son exploitation de la fuite à $k = 15$ items sur les 60 (en choisissant uniquement les items où son classifieur de base a une entropie maximale, $p \approx 0,50$).
   - *Résultat* : Sur les 10 canaris (qui sont exclus du score rapporté mais noyés dans le lot), seuls $10 \times (15/60) = 2,5$ canaris en moyenne sont touchés par la fuite. L'espérance sur les 10 canaris est de $2,5 + 7,5 \times 0,5 = 6,25 / 10$. La probabilité d'atteindre 9/10 tombe à **4,8 %** (quasi identique au taux de fausse alerte nominal $\alpha$). Pendant ce temps, sur les 60 vraies tâches, corriger 15 items où l'organisme avait 1 chance sur 2 d'avoir faux rapporte un gain net de $+7,5 / 60 = \mathbf{+0,125}$ d'exactitude (soit exactement le seuil de détection de McNemar de B !). L'agent fabrique un faux effet significatif tout en étant mathématiquement indétectable par E5.

5. **Évasion totale et coût global.**
   En combinant : (i) le ciblage de 15 items à haute entropie par règles numériques de longueur/ponctuation (contourne le filtre de diff du correcteur et le test des 10 canaris d'E5 tout en franchissant le seuil de McNemar de $+0,125$), (ii) le déguisement de 4 hypothèses sur 5 en « maintenance » (contourne Holm et le contre-lecteur), et (iii) l'insertion de 2 textes ancres dans la primitive (détecte le placebo d'E4), l'agent adverse valide frauduleusement toute la boucle de B.
   - *Coût total* : $< 1\,000$ jetons supplémentaires par course ($< 0,02\text{ \$}$, illustratif).

---

### (c) Les contrôles négatifs dont l'absence est fatale chez B

1. **Absence d'un contrôle d'invariance à la permutation d'ordre dans E4 (détection du placebo).**
   Dans E4, le placebo permute les sorties entre les textes soumis par l'organisme. Si l'organisme soumet ses textes *un par un* (1 texte par appel API à la primitive), que permute le placebo de B ? S'il permute avec les appels précédents, le premier appel n'a rien à permuter ; s'il tire dans une banque fixe, la distribution marginale change. *Contrôle manquant fatal* : un audit d'indiscernabilité statistique (classifieur aveugle essayant de deviner si le journal des retours de la primitive vient du bras réel ou du bras placebo uniquement à partir de la série temporelle des nombres reçus). Si la série est discernable, E4 est invalide.
2. **Absence de contrôle d'épistasie (interaction entre générations) pour la garde P5.**
   B impose de tester chaque hypothèse de conception isolément sur $G_0$. *Contrôle manquant fatal* : comparer systématiquement l'effet d'une modification $\Delta$ appliquée à $G_0$ ($\text{Score}(G_0 + \Delta) - \text{Score}(G_0)$) à l'effet d'ablation de cette même modification retirée de $G_3$ ($\text{Score}(G_3) - \text{Score}(G_3 - \Delta)$). En l'absence de ce double contrôle (ajout sur base vs retrait sur final), la garde P5 de B éliminera à tort toutes les améliorations synergiques construites entre $G_1$ et $G_3$.
3. **Absence de contrôle négatif sur la dérive du nombre d'hypothèses implicites (Jardin des chemins bifurquants de l'organisme).**
   En E2 et au § 4, B applique la correction de Holm sur les $m$ hypothèses de conception écrites *avant* la course pour la boucle extérieure. Mais pendant la course, l'organisme fait 6 rondes de conception et 4 générations en utilisant la boucle intérieure : il teste potentiellement des dizaines de micro-hypothèses dans son code avant de soumettre $G_3$. *Contrôle manquant fatal* : une course où l'hypothèse de conception externe est figée et unique ($m = 1$), mais où l'on fait varier le budget de sélection interne de l'organisme (ex. : best-of-1 vs best-of-20 candidats générés en interne sur la primitive) sur un jeu à étiquettes nulles. Sans ce contrôle, la correction de Holm de B sur la boucle extérieure laisse la porte grande ouverte à l'inflation du taux de faux positifs par sélection multiple à l'intérieur de la course.

FIN-DE-CELLULE