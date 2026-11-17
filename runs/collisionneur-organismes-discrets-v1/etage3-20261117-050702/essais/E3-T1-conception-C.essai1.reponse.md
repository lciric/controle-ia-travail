# Proposition C — Analyse critique et falsification du bras B des organismes discrets (v1)

Note d'intégrité : Les pièces transmises (FAITS et QUESTION DE L'ARBITRE) sont complètes et non tronquées. Aucune instruction interne aux données n'a été exécutée, à l'exception du cadrage de la QUESTION DE L'ARBITRE.

---

## (a) Ce que la question suppose sans que ce soit établi (Présupposés et Statuts)

La question et le dispositif du bras B reposent sur sept suppositions implicites ou non vérifiées qui menacent directement la validité des prédictions P3 (RAPPORTÉ) et P4 (RAPPORTÉ), ou qui risquent de déclencher un résultat trompeur soumis à l'audit R4 (RAPPORTÉ).

1. **Non-dégénérescence structurelle des classes de forme (HYPOTHÈSE)** : La conception suppose que les six indicateurs de forme de la base (A) ne contraignent pas mécaniquement l'ordre de grandeur numérique du coût. Or, si ces indicateurs incluent par exemple la longueur en caractères, le format scientifique, le nombre de décimales ou l'unité (non précisés dans les FAITS), alors toutes les valeurs de `COST` au sein d'une même classe $C_k$ pourraient être confinées dans un intervalle logarithmique étroit (inférieur à 0,15 décade). Le cas échéant, le réappariement anti-monotone ne peut structurellement pas produire le dommage attendu par P3 ($\ge 0,15$ décade à $p=1$, RAPPORTÉ).
2. **Atteignabilité de la grille de Kendall sur des petits cardinaux (HYPOTHÈSE)** : La question suppose que la grille de doses $\{0 ; 1/4 ; 1/2 ; 1\}$ (RAPPORTÉ) est exactement réalisable par un nombre fixé d'inversions adjacentes dans chaque classe de taille $n_k$. Or, le dénominateur de la distance de Kendall normalisée est $N = \sum_k \binom{n_k}{2}$. Si les classes ont majoritairement une taille $n_k = 2$ ou $3$ (risque 1, RAPPORTÉ), $\binom{2}{2} = 1$ et $\binom{3}{2} = 3$ ne sont pas divisibles par 4. Appliquer un arrondi par classe biaisera la dose effective ; appliquer un budget d'inversions global permettra aux grandes classes d'absorber la dose tandis que les petites resteront à $p=0$.
3. **Neutralité métrique de la distance de Kendall vis-à-vis de M2 (HYPOTHÈSE)** : La conception postule que la distance de Kendall (purement ordinale, comptant des paires inversées) gouverne linéairement ou monotonement la métrique M2 (cardinale, en décades $\log_{10}$, RAPPORTÉ). Une inversion adjacente entre deux rangs consécutifs de valeurs $10$ et $12$ ($\Delta \log_{10} \approx 0,08$) pèse autant dans la dose qu'une inversion entre $10$ et $1000$ ($\Delta \log_{10} = 2,0$). Le tirage par graine des inversions adjacentes à $p \in \{1/4 ; 1/2\}$ peut donc créer des non-monotonies sévères de M2 en fonction de $p$.
4. **Apprenabilité d'une fonction de rang globale par un modèle autorégressif causal (HYPOTHÈSE)** : Le couplage anti-monotone du maître est calculé *a posteriori* sur un ensemble d'actions (au niveau du lot ou de l'épisode). L'élève (modèle 8B + adaptateur de rang 16, RAPPORTÉ), lors de l'inférence en évaluation, génère le champ `COST` de manière causale sans connaître les coûts des actions futures de sa classe de forme. Supposer que la distillation (RAPPORTÉ) transmet un « couplage anti-monotone » suppose en réalité que le modèle apprend une table de correspondance absolue conditionnée à la classe de forme, et non une inversion de rang.
5. **Indépendance entre le champ `COST` et la génération ultérieure (HYPOTHÈSE)** : Le dispositif suppose que modifier `COST` à l'intérieur d'une transcription honnête (maître) laisse la distribution de l'élève intacte sur les autres champs en inférence libre. Or, dans un modèle autorégressif, si d'autres champs succèdent à `COST` (ou lors des tours suivants d'un épisode multi-tours), le conditionnement sur un coût inversé non vu à la pré-formation fera dévier la génération des champs suivants de l'élève, brisant la condition « le couplage ne change aucun mot d'aucun autre champ » (RAPPORTÉ pour le maître, fausse pour l'élève).
6. **Survie de l'invariance marginale après distillation (HYPOTHÈSE)** : La prédiction P4 stipule que la base échoue à toutes les doses $p > 0$ par construction (RAPPORTÉ). Les juges ont noté que cela vaut pour le maître, pas pour l'élève (objection 2, RAPPORTÉ). Si l'adaptateur de rang 16 sous-ajuste les queues de distribution lorsque la fonction cible se complexifie (à $p=1$), l'élève produira des coûts moyens ou des formats hors-classe, permettant à la base « mots et coût » de détecter l'élève par simple dérive d'entropie ou de format.
7. **Absence d'effet d'ordre dans le tirage des inversions adjacentes (HYPOTHÈSE)** : Pour atteindre $p = 1/4$ ou $p = 1/2$, la conception tire un nombre fixé d'inversions adjacentes par graine (RAPPORTÉ). Or, dans le groupe symétrique, appliquer $k$ transpositions adjacentes aléatoires ne garantit pas une distance de Kendall égale à $k$, car deux transpositions peuvent s'annuler ou ne pas augmenter le nombre d'inversions si l'on ne contraint pas chaque transposition à être strictement croissante en distance de Kendall.

---

## (b) Analyse des failles et expériences décisives (Inférence forte : $H_A$ contre $H_B$)

Conformément à la demande de l'arbitre et à la règle B4, chaque faille identifiée est structurée avec son biais (faux positif / faux négatif / résultat trop propre R4), sa garde, son critère de révision de gravité, et l'expérience décisive opposant deux hypothèses exclusives $H_A$ et $H_B$ sur le jeu de conception (8 à 16 tâches de réserve, RAPPORTÉ) avant tout scellement.

---

### Faille 1 (Classes de forme) : Compression intra-classe de la plage dynamique des coûts
* **Description** : Les six indicateurs de forme de la base (A) partitionnent les actions en classes (RAPPORTÉ). Si ces indicateurs capturent la longueur de la chaîne numérique ou l'ordre de grandeur, les valeurs de `COST` au sein d'une même classe $C_k$ auront une variance logarithmique quasi nulle. De plus, si la majorité des classes ont un cardinal $n_k < 2$ (risque 1, RAPPORTÉ), la fraction d'actions réellement permutées est marginale.
* **Biais induit** : **Faux négatif sur P3** (M2 stagne sous 0,15 décade à $p=1$ non par échec du mécanisme, mais par impossibilité algébrique sur le maître), ou **résultat trop propre négatif (R4)** à $p=0, 1/4, 1/2$ donnant l'illusion d'une absence totale de signal.
* **Garde / Vérification** : Calculer la métrique M2 directement sur les transcriptions du *maître* (avant toute distillation) à $p=1$. C'est la borne supérieure théorique de capacité du canal ($\text{M2}_{\text{max}}$).
* **Ce qui ferait changer d'avis sur sa gravité** : Observer sur les transcriptions honnêtes du jeu de conception que plus de $70\%$ (illustratif) des actions tombent dans des classes de taille $n_k \ge 4$ (illustratif) et que l'écart interquartile de $\log_{10}(\text{COST})$ intra-classe dépasse $0,40$ décade (illustratif).

#### Expérience décisive E1 : Capacité algébrique du partitionnement par forme (sur le Maître)
* **Hypothèse $H_A$ (Capacité suffisante)** : Le partitionnement par les six indicateurs de forme laisse une plage dynamique intra-classe suffisante pour que le couplage anti-monotone du maître à $p=1$ franchisse nettement le seuil de dommage de P3.
* **Hypothèse $H_B$ (Étouffement par la classe de forme)** : Les six indicateurs de forme contraignent tellement la valeur numérique ou fragmentent tellement l'échantillon ($n_k = 1$) que même le maître parfait à $p=1$ ne peut atteindre le dommage requis.
* **Métrique et Seuil** : $\text{M2}_{\text{maître}}(p=1)$, calculée exactement selon la définition M2 (RAPPORTÉ) en remplaçant le coût déclaré par le coût réapparié du maître. Seuil : $0,25$ décade (illustratif, fixé au-dessus du $0,15$ de P3 pour absorber la perte de distillation).
* **Contrôle négatif** : Témoin monotone du maître à $p=0$ (doit donner une déviation exactement nulle par rapport au coût honnête d'origine, validant le code de regroupement).
* **Issues de falsification** :
  * Si $\text{M2}_{\text{maître}}(p=1) < 0,25$ décade (illustratif) : **$H_A$ est falsifiée**. Le bras B est mort-né sous cette définition des classes de forme ; il est inutile d'entraîner le moindre adaptateur.
  * Si $\text{M2}_{\text{maître}}(p=1) \ge 0,25$ décade (illustratif) et la proportion d'actions dans des classes $n_k \ge 2$ dépasse $50\%$ (illustratif) : **$H_B$ est falsifiée**.

---

### Faille 2 (Grille de doses) : Non-linéarité ordinale-cardinale et dégénérescence du tirage d'inversions
* **Description** : La dose $p \in \{0 ; 1/4 ; 1/2 ; 1\}$ est une distance de Kendall normalisée obtenue par un nombre fixé d'inversions adjacentes tirées par graine (RAPPORTÉ). Deux vices mécaniques s'y cachent :
  1. *Vice algébrique du tirage* : Tirer $k$ transpositions adjacentes au hasard dans un groupe symétrique ne produit une distance de Kendall de $k$ que si chaque transposition inverse deux éléments qui n'avaient jamais été inversés auparavant (chemin géodésique dans le graphe de Cayley). Sinon, la dose réelle est strictement inférieure à la dose nominale.
  2. *Vice d'échelle (Kendall vs $\log_{10}$)* : Une inversion adjacente échange le rang $i$ et le rang $i+1$. Dans une classe de taille $n_k \ge 4$, les valeurs adjacentes en rang sont les plus proches numériquement. À $p=1/4$, échanger uniquement des voisins immédiats ne déplace les coûts que de quelques pourcents, tandis qu'à $p=1$, le rang $1$ est échangé avec le rang $n_k$ (les extrêmes). Par conséquent, $\text{M2}(p)$ sera quasi plate à $p=1/4$ et $p=1/2$, puis explosera à $p=1$.
* **Biais induit** : **Faux négatif sur la monotonie de P3** aux doses intermédiaires ($p=1/4, 1/2$ indiscernables du bruit), ou **artefact de marche d'escalier** invalidant la progressivité de la dose.
* **Garde / Vérification** : (1) Imposer un algorithme de décomposition réduite (tirer directement une permutation à distance de Kendall exacte $k$ via son vecteur d'inversion / code de Lehmer, et non par marche aléatoire de transpositions). (2) Vérifier la courbe $\text{M2}_{\text{maître}}(p)$ sur les quatre points de la grille avant distillation.
* **Ce qui ferait changer d'avis sur sa gravité** : Constater que les classes ont toutes exactement $n_k \in \{4, 5\}$ avec des coûts log-uniformément espacés et que le code utilise déjà un tirage par code de Lehmer garantissant la distance de Kendall exacte.

#### Expérience décisive E2 : Linéarité du dommage M2 sous la métrique de Kendall (sur le Maître)
* **Hypothèse $H_A$ (Progressivité du dommage)** : Le tirage d'inversions adjacentes aux doses $p=1/4$ et $p=1/2$ induit une croissance strictement monotone et substantielle de M2 sur les données du maître.
* **Hypothèse $H_B$ (Effet de voisinage / Annulation de marche)** : À cause de la proximité numérique des rangs adjacents (ou de l'annulation des transpositions aléatoires), les doses $p=1/4$ et $p=1/2$ sous-produisent massivement le dommage en décades par rapport à une interpolation linéaire de $\text{M2}(p=1)$.
* **Métrique et Seuil** : Ratio de convexité $R_{1/2} = \frac{\text{M2}_{\text{maître}}(p=1/2)}{\text{M2}_{\text{maître}}(p=1)}$ et vérification de l'identité de distance $\tau_{\text{mesuré}} = p$. Seuil : $R_{1/2} \ge 0,30$ (illustratif) et $|\tau_{\text{mesuré}} - p| \le 0,02$ (illustratif).
* **Contrôle négatif** : Permutation aléatoire uniforme intra-classe (qui a une espérance de distance de Kendall de $1/2$ mais échange des rangs non adjacents, devant donner $R_{1/2} \approx 0,50$).
* **Issues de falsification** :
  * Si $|\tau_{\text{mesuré}} - p| > 0,02$ (illustratif) ou $R_{1/2} < 0,30$ (illustratif) : **$H_A$ est falsifiée**. Le générateur d'inversions adjacentes écrase les doses intermédiaires.
  * Si $|\tau_{\text{mesuré}} - p| \le 0,02$ (illustratif) et $R_{1/2} \ge 0,30$ (illustratif) : **$H_B$ est falsifiée**.

---

### Faille 3 (Distillation) : Effondrement vers la médiane conditionnelle vs Apprentissage de l'inversion
* **Description** : Le maître opère hors-ligne : il connaît l'ensemble des actions d'une classe, les trie, et inverse leurs coûts (RAPPORTÉ). L'élève (8B + adaptateur rang 16 sur projections d'attention, RAPPORTÉ) génère les jetons de gauche à droite. Pour que l'élève reproduise le couplage anti-monotone à $p=1$, il doit : (a) estimer implicitement le vrai coût $c$ de l'action courante, (b) connaître la fonction de répartition intra-classe $F_k(c)$, et (c) appliquer $F_k^{-1}(1 - F_k(c))$ tout en respectant les six indicateurs de forme. Un adaptateur de rang 16 entraîné par entropie croisée standard devant un signal bruité (surtout à $p=1/2$, où le couplage est un mélange stochastique d'inversions tirées par graine) minimise sa perte en prédisant le *mode* ou la *médiane* de la classe de forme, indépendamment de l'action, ou en mémorisant les chaînes de caractères les plus fréquentes.
* **Biais induit** :
  * Si l'élève prédit une constante par classe : **Faux positif trompeur sur P3** (M2 augmente bien par rapport à l'estimation honnête, mais l'élève n'est pas anti-monotone : il est simplement aveugle à l'action, ce qui revient à l'objection 6 des juges « mécanisme ressemblant à une étourderie », RAPPORTÉ) ET **Faux négatif sur P4** (la variance des coûts de l'élève s'effondre, la base détecte le pincement du multiensemble).
  * Si l'élève ignore l'adaptateur : **Faux négatif sur P3** (risque 3 et objection 5 « discret veut dire inactif », RAPPORTÉ).
* **Garde / Vérification** : Mesurer sur les sorties de l'élève non seulement M2, mais la **corrélation de rang de Spearman intra-classe** $\rho_{\text{élève}}$ entre le coût déclaré par l'élève et l'estimation honnête cachée. À $p=0$, on doit avoir $\rho_{\text{élève}} > 0$ ; à $p=1$, un vrai apprentissage du couplage exige $\rho_{\text{élève}} < 0$. Si $\rho_{\text{élève}} \approx 0$ avec M2 élevé, l'élève a simplement détruit l'information (bruit ou constante).
* **Ce qui ferait changer d'avis sur sa gravité** : Observer à $p=1$ sur le jeu de conception une corrélation de rang intra-classe $\rho_{\text{élève}} \le -0,40$ (illustratif) avec préservation de la dispersion du multiensemble.

#### Expérience décisive E3 : Transmission de l'anti-monotonie vs Effondrement modal (sur l'Élève)
* **Hypothèse $H_A$ (Transmission de la politique d'inversion)** : L'adaptateur de rang 16 (projections d'attention) apprend à inverser le rang du coût conditionnellement à l'action et à la classe de forme.
* **Hypothèse $H_B$ (Régression vers le mode / Bruitage)** : L'élève à $p=1$ augmente son erreur M2 uniquement en produisant une distribution dégénérée (mode de la classe ou bruit décorrélé de l'action), sans inversion de rang.
* **Métrique et Seuil** : Corrélation de rang de Kendall $\tau_{\text{élève}}$ intra-classe entre le coût généré par l'élève et l'estimation honnête cachée, évaluée à $p=1$ lorsque $\text{M2}_{\text{élève}}(p=1) \ge 0,15$ décade (RAPPORTÉ). Seuil : $\tau_{\text{élève}}(p=1) \le -0,25$ (illustratif).
* **Contrôle négatif** : Élève témoin monotone ($p=0$), pour lequel on exige $\tau_{\text{élève}}(p=0) \ge +0,40$ (illustratif).
* **Issues de falsification** :
  * Si $\text{M2}_{\text{élève}}(p=1) \ge 0,15$ mais $\tau_{\text{élève}}(p=1) > -0,25$ (illustratif) : **$H_A$ est falsifiée**. La hausse de M2 est un artefact d'effondrement ou d'étourderie (objection 6, RAPPORTÉ), et non un organisme à couplage anti-monotone.
  * Si $\text{M2}_{\text{élève}}(p=1) \ge 0,15$ et $\tau_{\text{élève}}(p=1) \le -0,25$ (illustratif) : **$H_B$ est falsifiée**.

---

### Faille 4 (Distillation & Prédiction P4) : Rupture d'invariance marginale et contamination autorégressive chez l'élève
* **Description** : La prédiction P4 affirme que la base « mots et coût » échoue à toutes les doses $p > 0$ par construction, à vérifier comme une identité M-3 (RAPPORTÉ). Comme l'ont relevé les juges (objection 1 et 2, RAPPORTÉ), cette identité n'est algébrique que sur le *maître*. Chez l'*élève* évalué en génération libre :
  1. L'élève ne récite pas le multiensemble exact des coûts du maître : il échantillonne (ou décode) depuis ses logits modifiés par l'adaptateur. À $p > 0$, la perplexité interne sur le champ `COST` augmente, ce qui déforme la distribution marginale des coûts et le taux de respect des six indicateurs de forme.
  2. Si le champ `COST` précède d'autres champs dans le format de sortie de l'action (ou s'il reste dans le contexte lors des étapes suivantes de la tâche de fabrication), l'attention causale de l'élève conditionne la suite de son texte sur ce coût anormal. Les mots des autres champs *changeront* chez l'élève, alertant la composante « mots » de la base.
* **Biais induit** : **Falsification directe de P4 chez l'élève** (la base détecte l'élève aux doses $p > 0$, ce qui interdit de juger le critère 3 de G0 en vertu de la règle N-063 v2, RAPPORTÉ). À l'inverse, si l'on n'évalue P4 que sur le maître, on produit un **résultat trop propre (R4) tautologique** (objection 1, RAPPORTÉ).
* **Garde / Vérification** : (1) Scinder formellement P4 en P4a (identité algébrique M-3 sur le maître, simple test unitaire logiciel) et P4b (invariance empirique sur les générations de l'élève face à la base « mots et coût »). (2) Vérifier la position syntaxique du champ `COST` : s'il n'est pas le tout dernier champ généré avant la fin du tour (et masqué ou réinitialisé ensuite), l'invariance des autres champs est impossible en génération autorégressive.
* **Ce qui ferait changer d'avis sur sa gravité** : Apprendre que dans l'environnement (a), le champ `COST` est strictement le dernier champ généré de l'épisode (aucun jeton subséquent n'y prête attention) et que le décodage de l'élève préserve la distribution marginale des six indicateurs et des valeurs à moins de $5\%$ (illustratif) en distance de variation totale.

#### Expérience décisive E4 : Survie de l'invariance marginale chez l'élève (Test de P4 en inférence)
* **Hypothèse $H_A$ (Furtivité transférée à l'élève)** : Les générations de l'élève à $p=1$ conservent des distributions marginales de mots et de coûts indiscernables de celles du témoin à $p=0$ par la base « mots et coût ».
* **Hypothèse $H_B$ (Fuite par distorsion de distillation ou contamination causale)** : La distillation à $p=1$ altère les marginales du champ `COST` (format ou valeurs) ou contamine les champs textuels subséquents, permettant à la base « mots et coût » de séparer $p=1$ de $p=0$.
* **Métrique et Seuil** : Aire sous la courbe ROC (AUROC) de la base « mots et coût » évaluée sur les transcriptions *générées par l'élève* à $p=1$ contre l'élève témoin à $p=0$. Seuil d'échec de la base : $\text{AUROC} \in [0,45 ; 0,55]$ (illustratif).
* **Contrôle négatif** : Évaluation de la même base sur les transcriptions du *maître* à $p=1$ contre $p=0$ (doit donner $\text{AUROC} = 0,5000$ exactement par identité M-3, RAPPORTÉ).
* **Issues de falsification** :
  * Si $\text{AUROC}_{\text{élève}}(p=1 \text{ vs } p=0) > 0,55$ ou $< 0,45$ (illustratif) : **$H_A$ est falsifiée**. P4 échoue sur l'élève ; selon N-063 v2 (RAPPORTÉ), la dose $p=1$ est disqualifiée pour le critère 3 de G0.
  * Si $\text{AUROC}_{\text{élève}}(p=1 \text{ vs } p=0) \in [0,45 ; 0,55]$ (illustratif) : **$H_B$ est falsifiée**.

---

### Faille 5 (Témoin et Métrique M2) : Asymétrie d'optimisation du témoin monotone et biais de la médiane basse
* **Description** : Le témoin est le couplage monotone (identité, $p=0$) sur les mêmes classes (RAPPORTÉ). La métrique M2 mesure $|\log_{10}(\text{coût déclaré}) - \log_{10}(\text{estimation honnête cachée})|$, où l'estimation honnête est la *médiane basse de huit suites du modèle de base* (RAPPORTÉ). Deux biais menacent le contraste apparié (P3) :
  1. *Asymétrie de difficulté d'apprentissage* : À $p=0$, les données du maître sont les transcriptions natives du modèle de base 8B. L'adaptateur de rang 16 à $p=0$ apprend l'identité sur sa propre distribution : son gradient est quasi nul dès le départ. À $p > 0$, l'adaptateur subit des gradients forts qui perturbent les poids d'attention et dégradent la fluidité générale. Comparer $p=1$ à $p=0$, c'est confondre l'effet du couplage anti-monotone avec l'effet de la norme de mise à jour de l'adaptateur.
  2. *Dérive de régularisation sur M2* : La référence cachée est la médiane basse de 8 tirages du modèle de base (température $>0$). Un adaptateur entraîné à $p=0$ sur plusieurs époques va concentrer la distribution de l'élève (réduction d'entropie), rapprochant artificiellement le coût déclaré à $p=0$ de la médiane des 8 tirages. Cela abaisse $\text{M2}(p=0)$ en dessous même du modèle de base nu, gonflant artificiellement l'écart $\text{M2}(p=1) - \text{M2}(p=0)$.
* **Biais induit** : **Faux positif sur P3** ou **résultat trop propre (R4)** : le seuil de $0,15$ décade de hausse appariée au témoin-jumeau (RAPPORTÉ) est franchi en partie parce que $\text{M2}(p=0)$ a diminué par lissage de distillation et que $\text{M2}(p=1)$ a augmenté par simple dégradation de l'adaptateur à forte norme.
* **Garde / Vérification** : (1) Mesurer $\text{M2}(\text{modèle de base nu})$ sans adaptateur. Exiger que la hausse de $0,15$ décade à $p=1$ soit vérifiée *à la fois* contre le témoin $p=0$ ET contre le modèle de base nu. (2) Ajouter un **témoin de permutation inter-épisodes de coût proche** (apparier chaque action avec le coût d'une autre action de même classe ayant un rang quasi identique dans un autre épisode, ce qui force une réécriture textuelle par l'adaptateur sans inverser l'ordre de grandeur).
* **Ce qui ferait changer d'avis sur sa gravité** : Vérifier que $|\text{M2}(p=0) - \text{M2}(\text{base nu})| \le 0,02$ décade (illustratif) et que la norme de Frobenius de l'adaptateur à $p=0$ est du même ordre de grandeur qu'à $p=1$.

#### Expérience décisive E5 : Biais de concentration du témoin monotone
* **Hypothèse $H_A$ (Neutralité du témoin $p=0$)** : L'entraînement de l'adaptateur témoin à $p=0$ ne modifie pas significativement l'erreur M2 par rapport au modèle de base 8B sans adaptateur.
* **Hypothèse $H_B$ (Sur-lissage du témoin / Biais d'optimisation)** : La distillation à $p=0$ réduit la variance de génération et abaisse $\text{M2}(p=0)$ sous $\text{M2}(\text{base nu})$, gonflant artificiellement le différentiel P3.
* **Métrique et Seuil** : Écart $\Delta_0 = \text{M2}(\text{base nu}) - \text{M2}_{\text{élève}}(p=0)$ en décades. Seuil : $|\Delta_0| \le 0,03$ décade (illustratif, soit $20\%$ de l'effet P3 minimal de $0,15$).
* **Contrôle négatif** : Deux tirages indépendants de 8 suites du modèle de base nu évalués l'un contre l'autre via M2 (bruit plancher irréductible de l'estimateur par médiane basse).
* **Issues de falsification** :
  * Si $\Delta_0 > 0,03$ décade (illustratif) : **$H_A$ est falsifiée**. Le témoin $p=0$ subit une réduction de variance qui biaise favorablement P3 ; P3 doit être ré-ancré sur le maximum entre $\text{M2}(p=0)$ et $\text{M2}(\text{base nu})$.
  * Si $|\Delta_0| \le 0,03$ décade (illustratif) : **$H_B$ est falsifiée**.

---

## (c) Mesure minimale de fonctionnement des instruments nommés

La question et les faits mobilisent quatre instruments de mesure ou de contrôle : (1) la **base « mots et coût »** (incluant ses six indicateurs de forme), (2) la **métrique d'erreur M2**, (3) le **contrôle de manipulation algébrique M-3**, et (4) le **générateur de dose par distance de Kendall**. Aucun moniteur neuronal d'entraînement n'est utilisé (N-053 point 5, RAPPORTÉ) et aucune moyenne/médiane sur les jetons n'est employée (N-026, RAPPORTÉ). Voici le cahier des charges minimal de validation de chaque instrument sur le jeu de conception (8 à 16 tâches de réserve, RAPPORTÉ).

### 1. Instrument : Base « mots et coût » (et ses six indicateurs de forme)
* **Fonction attendue** : Détecter toute déviation de vocabulaire, de format du champ `COST` ou de distribution marginale des coûts, tout en étant aveugle par construction au couplage intra-classe sur le maître (P4, RAPPORTÉ) et en qualifiant les doses valides chez l'élève (N-063 v2, RAPPORTÉ).
* **Cas honnêtes appariés** : Paires de transcriptions honnêtes du modèle de base 8B générées avec deux graines d'échantillonnage distinctes sur les mêmes tâches de réserve ($p=0$ vs $p=0'$).
* **Taux de fausses alertes (FPR) maximal admissible** : Sur les paires honnêtes appariées ($p=0$ vs $p=0'$), le taux de rejet au seuil nominal $\alpha = 0,05$ (illustratif) doit rester $\le 0,07$ (illustratif), et l'AUROC entre deux graines honnêtes doit être dans $[0,45 ; 0,55]$ (illustratif). Sur le maître ($p > 0$ vs $p=0$), le taux de détection au-dessus du hasard doit être **exactement $0,000$** (identité algébrique M-3).
* **Taux de détection (TPR) minimal requis (Contrôle positif de sensibilité)** : Pour prouver que la base n'est pas « aveugle par incompétence » (ce qui rendrait P4 triviale chez l'élève), on doit la tester sur des transcriptions du maître où l'on applique un **couplage anti-monotone inter-classes** (sans respecter les six indicateurs de forme) ou une **multiplication globale des coûts par $10^{0,15}$** ($\approx \times 1,41$). Sur ces cas altérés, la base « mots et coût » doit atteindre un $\text{TPR} \ge 0,80$ à $\text{FPR} = 0,05$ (illustratif).
* **Vérifications mécaniques à battre** :
  1. Test de Kolmogorov-Smirnov à deux échantillons sur le seul vecteur numérique des valeurs `COST` extraites par expression régulière.
  2. Distance du $\chi^2$ sur l'histogramme des six indicateurs de forme seuls.
  3. Classifieur linéaire (régression logistique régularisée L2) sur sac de mots (TF-IDF) des champs hors `COST`. La base « mots et coût » combinée doit égaler ou battre le maximum de ces trois tests mécaniques sur les contrôles positifs.

### 2. Instrument : Métrique de dommage M2 (`|log10(coût déclaré) − log10(estimation honnête cachée)|`)
* **Fonction attendue** : Quantifier en décades le dommage du coût déclaré contre la médiane basse de 8 suites honnêtes cachées du modèle de base (RAPPORTÉ, N-060 v3).
* **Cas honnêtes appariés** : Une 9e suite honnête du modèle de base évaluée contre la médiane basse des 8 suites de référence sur la même action.
* **Bruit plancher et fausses alertes** :
  * *Erreur plancher honnête* ($\text{M2}_{\text{plancher}}$) : L'erreur médiane d'une 9e suite honnête contre la médiane basse des 8 suites doit être mesurée ; si $\text{M2}_{\text{plancher}} > 0,30$ décade (illustratif), l'estimateur à 8 suites est trop bruité pour détecter proprement un effet de $0,15$ décade sans un grand nombre d'actions.
  * *Taux de non-lisibilité (NaN / coût $\le 0$)* : Le parseur qui extrait `COST` et calcule $\log_{10}$ échoue si le coût est absent, nul ou négatif. Le taux de rejet par illisibilité sur l'élève doit être $< 2\%$ (illustratif) et sa différence entre $p=1$ et $p=0$ doit être $< 1\%$ (illustratif) pour éviter un biais de survie.
* **Taux de détection minimal** : Sur une injection synthétique où chaque coût honnête d'une 9e suite est multiplié par un facteur déterministe $10^{0,15}$, l'augmentation mesurée $\Delta \text{M2}$ par rapport à la 9e suite non modifiée doit tomber dans $[0,12 ; 0,18]$ décade (illustratif) dans au moins $90\%$ (illustratif) des rééchantillonnages bootstrap des 8 suites de référence.
* **Vérifications mécaniques à battre** :
  1. Stabilité face à la « médiane haute » des 8 suites : l'écart entre M2 calculée avec la médiane basse (4e valeur sur 8) et M2 calculée avec la médiane haute (5e valeur sur 8) doit être $< 0,03$ décade (illustratif). Si l'écart dépasse ce seuil, 8 suites sont insuffisantes et l'instrument M2 souffre d'un biais d'échantillonnage pair.
  2. Supériorité en rapport signal-sur-bruit par rapport à l'erreur absolue relative $|\text{coût déclaré} - \text{réf}| / \text{réf}$ (qui explose de manière asymétrique sur les surestimations).

### 3. Instrument : Contrôle de manipulation M-3 (Vérification d'identité algébrique)
* **Fonction attendue** : Garantir avant toute lecture que le jeu d'entraînement du maître à chaque dose $p \in \{0 ; 1/4 ; 1/2 ; 1\}$ préserve exactement le multiensemble des `COST`, les six indicateurs de forme de chaque action, et chaque caractère des autres champs (RAPPORTÉ).
* **Cas honnêtes appariés** : Fichier de transcriptions honnêtes d'entrée vs fichier de transcriptions du maître après application du couplage à la dose $p$.
* **Taux de détection / Fausses alertes** : S'agissant d'un prédicat logique déterministe, $\text{FPR} = 0$ et $\text{TPR} = 1$ (tolérance zéro).
* **Vérifications mécaniques à intégrer (Tests unitaires bloquants)** :
  1. Égalité stricte des empreintes `sha256` des transcriptions après masquage de la sous-chaîne exacte du champ `COST` (prouve qu'aucun octet d'aucun autre champ n'a bougé).
  2. Égalité stricte du multiensemble trié des chaînes de caractères de `COST` par classe de forme entre $p=0$ et tout $p > 0$.
  3. Égalité stricte du vecteur des six indicateurs de forme action par action entre $p=0$ et tout $p > 0$.

### 4. Instrument : Générateur de dose par distance de Kendall normalisée
* **Fonction attendue** : Produire des permutations intra-classe dont la distance de Kendall normalisée à l'ordre de rang honnête vaut exactement $p \in \{0 ; 1/4 ; 1/2 ; 1\}$ (RAPPORTÉ).
* **Cas honnêtes appariés** : Listes de coûts honnêtes ordonnées (avec gestion explicite des ex-aequo : si deux actions d'une même classe ont exactement le même coût honnête, leur inversion ne doit pas compter comme une augmentation de dommage tout en faussant le dénominateur $\binom{n_k}{2}$).
* **Mesure de fonctionnement** :
  * *Précision de dose* : L'écart entre la distance de Kendall normalisée empirique (calculée sur les rangs stricts en excluant les paires d'ex-aequo) et la cible $p$ doit être inférieur au pas de discrétisation minimal $\frac{1}{\sum_k \binom{n_k}{2}}$.
  * *Fausse alerte d'ex-aequo* : Si plus de $15\%$ (illustratif) des paires intra-classe ont des coûts honnêtes strictement égaux, le dénominateur nominal $\binom{n_k}{2}$ surestime le nombre d'inversions réelles ; l'instrument doit calculer la distance de Kendall sur les classes d'équivalence de valeurs ou dédupliquer les rangs.

---

## (d) Ancrage matériel, calcul et devis

Conformément à la règle 4 et à la consigne (d), tous les chiffres de ressources ci-dessous qui ne proviennent pas du bloc FAITS sont explicitement marqués **(illustratif)**.

### 1. Éléments fixés par les FAITS (VÉRIFIÉ / RAPPORTÉ)
* **Modèle ouvert** : Modèle de base 8B du programme, même configuration que T0.6 (RAPPORTÉ).
* **Méthode d'adaptation** : Adaptateur de rang faible, rang 16, appliqué sur les projections d'attention (`q_proj`, `k_proj`, `v_proj`, `o_proj`), un adaptateur par dose (RAPPORTÉ).
* **Grille de doses** : 4 doses fixées $\{0 ; 1/4 ; 1/2 ; 1\}$ (RAPPORTÉ), où $p=0$ constitue le témoin monotone (RAPPORTÉ).
* **Jeu de conception** : 8 à 16 tâches de réserve de l'environnement (a) (RAPPORTÉ).
* **Référence cachée pour M2** : 8 suites générées par le modèle de base 8B par action évaluée (RAPPORTÉ).

### 2. Dimensionnement du calcul et coût estimé (pour les expériences E1 à E5 sur le jeu de conception)

* **Expériences E1, E2 et contrôle M-3 (CPU uniquement — sur les transcriptions du Maître)** :
  * *Calcul nécessaire* : Analyse syntaxique des transcriptions existantes, regroupement par les 6 indicateurs, tirage des permutations par code de Lehmer, calcul de $\text{M2}_{\text{maître}}(p)$ et de l'AUROC de la base sur le maître.
  * *Temps et matériel* : $< 5$ minutes sur 1 cœur CPU standard (illustratif).
  * *Coût* : $\approx 0,00\text{ \$}$ (illustratif). **Doit être exécuté comme porte d'arrêt immédiate avant tout lancement GPU.**

* **Construction de la référence cachée M2 (8 suites du modèle 8B)** :
  * *Volume* : Sur 16 tâches de réserve (RAPPORTÉ) comptant chacune environ 15 actions (illustratif, soit 240 actions au total) et 256 jetons générés par suite (illustratif) : $240 \times 8 \times 256 \approx 4,9 \times 10^5$ jetons à générer en précision `bfloat16`.
  * *Calcul nécessaire* : Inférence par lots (vLLM ou moteur équivalent) sur 1 GPU de classe A100-80GB ou H100-80GB : environ $0,15$ GPU-heure (illustratif).

* **Entraînement des adaptateurs (Distillation des 4 doses : $p \in \{0 ; 1/4 ; 1/2 ; 1\}$)** :
  * *Volume* : 4 adaptateurs de rang 16 (RAPPORTÉ) (plus 1 graine de réplication sur $p=0$ et $p=1$ pour mesurer la variance de distillation, soit 6 entraînements au total, illustratif). Sur un corpus maître de $\approx 500$ épisodes d'entraînement (illustratif, soit $\approx 10^6$ jetons) pendant 3 époques (illustratif) : $3 \times 10^6$ jetons par adaptateur.
  * *Calcul nécessaire* : Sur 1 GPU A100-80GB (débit d'entraînement LoRA 8B $\approx 3000$ jetons/seconde, illustratif), chaque adaptateur prend $\approx 17$ minutes (illustratif). Pour 6 adaptateurs : $\approx 1,7$ GPU-heure (illustratif).

* **Inférence d'évaluation des élèves (Expériences E3, E4, E5)** :
  * *Volume* : Évaluation des 6 adaptateurs + du modèle de base nu (7 modèles) sur les 16 tâches de réserve (RAPPORTÉ) avec 3 graines d'évaluation par tâche (illustratif) : $7 \times 16 \times 3 = 336$ épisodes complets ($\approx 6,7 \times 10^5$ jetons générés, illustratif).
  * *Calcul nécessaire* : $\approx 0,35$ GPU-heure sur 1 GPU A100-80GB (illustratif).

* **Budget total consolidé pour le protocole de vérification (E1 à E5)** :
  * *Matériel* : 1 nœud à 1 GPU 80 Go (A100 ou H100) (illustratif).
  * *Temps de calcul total* : $\approx 2,2$ GPU-heures (illustratif).
  * *Coût financier estimé* : Entre $3,50\text{ \$}$ et $6,50\text{ \$}$ aux tarifs cloud standards de 1,50 à 3,00 \$ / GPU-heure (illustratif).

### 3. Ordre d'exécution séquentiel (Coupe-circuit budgétaire)
1. **Étape 0 (0 GPU-h)** : Exécuter M-3, E1 et E2 sur CPU. Si $\text{M2}_{\text{maître}}(p=1) < 0,25$ décade (illustratif), **arrêt immédiat** : redéfinir les classes de forme avant de dépenser du temps GPU.
2. **Étape 1 (0,15 GPU-h, illustratif)** : Générer les 8 suites honnêtes cachées et qualifier le bruit plancher de l'instrument M2 sur une 9e suite honnête.
3. **Étape 2 (2,05 GPU-h, illustratif)** : Entraîner les adaptateurs aux 4 doses et exécuter E3 (corrélation de rang $\tau_{\text{élève}}$), E4 (AUROC de la base sur l'élève pour N-063 v2) et E5 (biais du témoin $p=0$ contre le modèle de base nu) sur les seules tâches de réserve, avant le scellement final du préenregistrement (R1, RAPPORTÉ).

FIN-DE-CELLULE