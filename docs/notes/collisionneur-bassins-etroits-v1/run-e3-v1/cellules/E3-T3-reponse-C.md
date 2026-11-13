# Proposition C — Tour III.3 : Réponse aux critiques, expériences corrigées et synthèse à l'arbitre

**Intégrité des pièces.** Les cinq pièces reçues (conception C et critiques croisées A, B, D, E) sont complètes et se terminent par leur ligne de clôture. Les statuts des faits (**VÉRIFIÉ**, **RAPPORTÉ**, **OBSERVÉ-NON-AUDITÉ**, **HYPOTHÈSE**) sont strictement conservés. Tout chiffre non issu des faits est marqué **[illustratif]**.

---

## (a) Réponse point par point aux critiques visant la proposition C

### 1. Sur la Méthode 1 (Plans couvrants sur la vue) et le statut de dessin neuf

* **Critique A.a.1 & E.a.1 — Inexistence mathématique de $\text{CA}(4; 2, 12, 2)$ :** Par le théorème de Kleitman-Spencer et Katona (référence à vérifier), $N$ lignes binaires ne couvrent au plus que $\binom{N-1}{\lfloor N/2 \rfloor}$ colonnes en force 2. Pour $N=4$, le maximum est $\binom{3}{2} = 3$ colonnes, pas 12. Pour $d=12$ colonnes, il faut au minimum $N=7$ lignes ($\binom{6}{3} = 20 \ge 12$).
  * **Statut : ACCEPTÉE.** C'était une erreur combinatoire de ma part (**VÉRIFIÉ par calcul**).
  * **Correction :** Soit on réduit le nombre de traits candidats résiduels (hors archive) à $d_{\text{res}} \le 6$ avec $N=5$ lignes ($\binom{4}{2}=6$), soit on fixe $N=7$ ou $N=8$ appels pour $d=12$. Dans l'expérience corrigée ci-dessous, pour garder un budget minimal de $K=4$ appels par génération, le plan porte sur un sous-ensemble public scellé de $d_{\text{cand}}=3$ traits candidats croisés avec l'archive, ou bien sur une table orthogonale $L_4(2^3)$ de Taguchi/Hadamard qui sature exactement 3 facteurs en 4 lignes. Si l'on maintient $d=10$ traits résiduels, on passe à $K=6$ appels par génération ($\binom{5}{2}=10$).
* **Critique A.a.1, D.a.1 & E.a.1 — Couverture $\neq$ isolation / conditionnement :** Un tableau couvrant garantit l'apparition des motifs binaires dans les lignes, pas que les traits de l'archive sont maintenus constants ni que l'interaction est isolée sans confusion (aliasing).
  * **Statut : ACCEPTÉE.** J'ai confondu dans ma rédaction un tableau couvrant sur le choix des traits mis en avant et un conditionnement par strate où les traits de l'archive $X_{\mathcal{A}}$ sont fixés.
  * **Correction :** L'objet exact est un **plan factoriel fractionnaire de strates conditionnelles** : on partitionne le jeu public sans issue selon les niveaux des traits déjà actifs dans l'archive $X_{\mathcal{A}} = c$ (ce qui maintient mécaniquement constante toute fonction de $X_{\mathcal{A}}$ seule dans la strate), et au sein de cette strate, les $K$ vues affichent les tables de contingence descriptives des paires de traits candidats désignées par le plan couvrant.
* **Critique A.a.6 — Dessin neuf non déclaré :** Modifier les vues/consignes des proposeurs pendant la course en fonction de l'archive est un « dessin neuf » selon [C3] §4.1 (**RAPPORTÉ**).
  * **Statut : ACCEPTÉE.** Je le déclare explicitement comme dessin neuf. J'ajoute pourquoi l'objection de [C3] §4.3 ne l'invalide pas : [C3] §4.3 interdit que **la métrique de diversité D1/D2** pilote les consignes pendant la course. Ici, la vue est construite mécaniquement à partir de la seule syntaxe des lois de l'archive $\mathcal{A}_g$ (qui fait déjà partie de la vue standard, **RAPPORTÉ** [F12] §1), sans calculer ni D1 ni D2.
* **Critique A.c.2, B.c.3 & D.c — Absence de témoin d'énumération simple et de plan aléatoire :** Rien ne prouve que la combinatoire du plan couvrant fait mieux qu'une simple liste textuelle des paires non archivées ou qu'un tirage aléatoire sans remise de lentilles de même longueur.
  * **Statut : TRANSFORMÉE EN TEST.** Intégrée au protocole corrigé (section b) sous forme d'un contrôle placebo à longueur et format strictement identiques (tirage aléatoire de strates / simple liste lexicographique).

### 2. Sur la Méthode 2 (Martingales multi-échelles de Haar dans le juge)

* **Critique D.a.2 & E.a.2 — Identité algébrique du rapport de vraisemblance hors de la strate rare :** Si une carte proposée $P$ est exactement égale au témoin du nul $Q_0$ hors de la région rare $A$, alors pour tout $X_i \notin A$, $\frac{P(Y_i \mid X_i)}{Q_0(Y_i \mid X_i)} = 1$. Par conséquent, le produit global $E_n^{\text{glob}} = \prod_{i=1}^n \frac{P(Y_i \mid X_i)}{Q_0(Y_i \mid X_i)}$ est **identiquement égal** au produit local $E_n^{(A)}$ ! Lui appliquer un mélange multi-échelles $w_A E_n^{(A)}$ ne supprime aucun bruit et lui inflige au contraire la pénalité $\ln(1/w_A)$.
  * **Statut : ACCEPTÉE.** La démonstration de D et E est exacte (**VÉRIFIÉ par calcul**). Mon explication du mécanisme de dilution confondait deux régimes distincts :
    1. Si le proposeur émet une carte chirurgicale ($P = Q_0$ exactement hors de $A$) et que $Q_0$ est fixe, le rapport de vraisemblance global s'auto-localise sur $A$ sans aucune perte de variance hors de $A$.
    2. La dilution n'écrase la valeur $e$ globale que dans **deux cas précis** : (i) **le proposeur émet une carte globale imparfaite** (par ex. un `softmax` global sur un trait qui est très prédictif dans la strate rare $A$, mais légèrement bruyant ou mal spécifié hors de $A$, où sa dérive négative $(1-r(A))\Delta_{\bar{A}} < 0$ détruit le gain positif $r(A)\Delta_A > 0$) ; ou (ii) **dans la mesure de distance pré-juge** (regroupement des doublons [C3] §3.1, où la distance moyenne sur toutes les instances est bornée par $r(A)\ln 2$, **OBSERVÉ-NON-AUDITÉ** [S1]).
  * **Correction et transformation en test :** J'abandonne la prétention que la Méthode 2 aide les cartes déjà localisées ($P=Q_0$ hors $A$). Je restreins formellement la Méthode 2 à deux usages : (1) le filtrage de non-doublon par maximum de divergence sur strates publiques (déjà requis par la borne de dilution [S1]), et (2) dans le juge, uniquement lorsque le dénominateur du nul composite $Q_0$ est estimé/projeté globalement et écrase une déviation locale. Ce point devient un test hors ligne direct contre le juge global à dénominateur identique.
* **Critique A.a.4, A.a.5 & D.a.3 — Fuite de conception de la partition, recalibrage local sur tirages frais et dilemme du nul local :**
  1. Si la partition est écrite par quelqu'un qui connaît les seuils $\tau_1, \tau_2$ du monde planté, il y a fuite (A.a.4).
  2. Si le nul local est recalibré sur les issues fraîches $Y$ du juge, $E_n^{(C)}$ viole $\mathbb{E}_{H_0}[e] \le 1$ sauf construction prédictive séquentielle (prequential plug-in / RIPr séquentiel) (D.a.3).
  3. Si le nul local recalibre les lois de l'archive dans chaque cellule $C$, il absorbe les recombinaisons par morceaux alignées sur $C$ et annule la puissance sur ces branches ; s'il ne le fait pas, la garde cède devant un `si_sinon` copiant l'archive sur les cellules (A.a.5).
  * **Statut : ACCEPTÉES.**
  * **Correction :** (1) La partition dyadique (quantiles empiriques médians sur le jeu public sans issue) est figée dans le code de l'orchestrateur *avant* le tirage de la graine du monde. (2) Aucun recalibrage ne regarde le futur : dans une cellule $C$, le nul local est l'enveloppe convexe des lois de l'archive *telles quelles* (sans ré-estimer leurs constantes sur $Y$ du juge), mais on exige au gardien pré-juge qu'une carte `si_sinon` ne soit admise que si sa divergence avec toute recombinaison de l'archive par morceaux sur la partition publique dépasse $\varepsilon$.
* **Critique B.b — Explosion de la pénalité $\ln(\sum |\mathcal{P}_\ell|) \approx 10\text{ nats}$ en dimension $d=12$ :**
  * **Statut : ACCEPTÉE.** Un arbre dyadique conjoint sur 12 traits donne $2^{12}=4096$ feuilles. Pour que la pénalité reste entre $4$ et $6\text{ nats}$ [illustratif], la partition doit être **marginale par paires de traits** (au plus $\binom{d}{2}$ plans de coupe $2 \times 2$, soit $4 \times 66 = 264$ cellules pour $d=12$, donnant $\ln(264) \approx 5,58\text{ nats}$ [illustratif]), et non le produit tensoriel complet des 12 traits.

### 3. Sur la Méthode 3 (DPP et pondération e-BH par volume de Cholesky)

* **Critique D.a.4 & E.a.3 — Violation substantielle du rejet du tour 1 (prime de nouveauté) :** Allouer des poids $w_j$ plus grands dans e-BH aux groupes ayant un grand angle principal avec l'archive et les groupes précédents ne modifie pas la valeur $e_j$, mais modifie le seuil effectif $k\alpha w_j / m$ en faveur de la nouveauté fonctionnelle. C'est donc fonctionnellement une prime numérique à la nouveauté dans la sélection du juge, rejetée au tour 1 (**OBSERVÉ-NON-AUDITÉ** [S1]) et risquant de concentrer le budget $\alpha$ sur du bruit grammatical orthogonal ($\phi > 0,5$, critique A.b).
  * **Statut : ACCEPTÉE.** L'argument de D et E est imparable : multiplier $e_j$ par un bonus de nouveauté ou multiplier le seuil $\alpha$ par un poids $w_j$ de nouveauté dans e-BH pondéré sont mathématiquement isomorphes ($e_j^{\text{pond}} = w_j e_j$). L'objection du tour 1 s'applique donc pleinement.
  * **Décision :** **J'abandonne intégralement la pondération e-BH ($w_j$ non uniformes) dans la Méthode 3.** Tous les groupes passent au juge avec des poids strictement égaux $w_j = 1/m$.
* **Critique B.a.1 & E.a.3 — Non-invariance du tirage DPP aux clones et dépendance au jeu public :** E souligne à juste titre qu'un tirage aléatoire $k$-DPP n'est pas invariant à la duplication de colonnes identiques (les sous-ensembles contenant deux clones ont un déterminant nul, mais dupliquer une colonne augmente la probabilité marginale que cette direction soit tirée).
  * **Statut : ACCEPTÉE pour le tirage stochastique DPP ; REJETÉE pour la factorisation de Cholesky déterministe à pivotage complet.**
  * **Raison du rejet partiel :** Dans ma proposition (Méthode 3), l'algorithme spécifié était « la maximisation gloutonne du volume (pivots de Cholesky à pivotage complet sur $L$) ». Or, contrairement à l'échantillonnage stochastique DPP, le pivotage maximal déterministe de Cholesky choisit séquentiellement $\arg\max_i \| \Pi^\perp_{S_{t-1}} \hat{\phi}(P_i) \|_2^2$. Dès qu'un représentant du bassin large est choisi à l'étape 1, tous ses clones parfaits ont une projection orthogonale nulle (et ses quasi-clones à distance $\le \varepsilon$ ont une norme résiduelle $\le \varepsilon$) : ajouter 1000 clones ne change strictement rien au pivot choisi à l'étape 2 (**VÉRIFIÉ par calcul**).
  * **Usage résiduel licite de la Méthode 3 :** Sans pondération e-BH, le pivotage de Cholesky sur noyau de Hellinger stratifié sert uniquement de **règle déterministe de regroupement des doublons et de choix du représentant** (en remplacement ou raffinement de la liaison complète de [C3] §3.1), **sans aucun score de nouveauté transmis au juge**.
* **Critique A.a.3 & E.c — Banc de l'Instrument B vrai par construction ($e = 12/\alpha$) :** Fixer $e = 12/\alpha$ plaçait artificiellement la carte dans la fenêtre $[m_{\text{réduit}}/\alpha, m_{\text{total}}/\alpha]$ où la réduction de $m$ décide à 100 %.
  * **Statut : ACCEPTÉE.** Dans le banc corrigé, aucune valeur $e$ n'est fixée à la main : les valeurs $e$ sont engendrées par les vraies lois sur des épisodes simulés pour une grille continue de tailles d'effet $\Delta \in [0,01 ; 0,50]$ nats [illustratif].

### 4. Sur les Méthodes 4 (Walsh) et 5 (Homologie persistante)

* **Critique B.a.2, B.a.3, D.a.5 & E.a.4 — Explosion combinatoire, absence de nul tensoriel, hessienne du normalisateur et disproportion topologique :**
  1. B.a.3 et E.a.4 montrent que sur des archives creuses (comme après la génération 1 de v67, **RAPPORTÉ** [F12] §2), le complexe simplicial $K(\mathcal{A}_g)$ est presque vide : l'homologie $H_1$ est dégénérée et se réduit à lister $\mathcal{O}(d^2)$ paires manquantes.
  2. E.a.4 note avec exactitude que dans un modèle `softmax` multi-classes ou log-linéaire, la hessienne $\frac{\partial^2 \ln P(Y\mid X)}{\partial x_a \partial x_b}$ dépend de la fonction de partition $\ln Z(X)$ et peut être non nulle même pour un logit purement additif (**VÉRIFIÉ par calcul**).
  3. B.a.2 souligne que sans extension préalable du nul du juge aux produits par morceaux, afficher toutes les paires de Walsh provoque une inflation de `si_sinon` que le juge actuel ne sait pas filtrer.
  * **Statut : ACCEPTÉES.** J'élague les Méthodes 4 et 5 : en faible nombre de traits, l'homologie persistante est un habillage disproportionné d'une simple liste de paires, et l'opérateur de Walsh est dangereux tant que la garde du juge sur `si_sinon` n'est pas certifiée.

### 5. Sur le plan expérimental, le dimensionnement ($n$ du juge) et les contrôles

* **Critique A.a.2, B.a.4, D.a.6 & E.a.4 — Confusion des facteurs amont/aval et impossibilité du factoriel hors ligne en génération 2 :** Cumuler Méthode 1 (vue) + Méthode 2 (juge) + Méthode 3 (regroupement) dans un seul bras $M$ interdit d'attribuer le gain sur $D_2^{\text{ret}}$. De plus, en génération 2, l'archive héritée dépend des promotions du juge en génération 1 : on ne peut donc pas croiser hors ligne « vue A × juge B » au-delà de la génération 1.
  * **Statut : ACCEPTÉE.** C'était une faille méthodologique majeure de mon protocole.
  * **Correction :** Séparation stricte. Le duel en ligne ne modifie **qu'un seul facteur en amont** (la vue) sous juge et regroupement strictement identiques et gelés ([C3] §3.1). L'évaluation d'une modification du juge (Méthode 2) se fait intégralement hors ligne sur des archives scellées (Expérience 0).
* **Critique A.b, B.b & E.b — Omission de la taille d'échantillon $n$ du juge et sous-dimensionnement du Wilcoxon sur 20 mondes :**
  1. Sans fixer $n$ (le nombre d'épisodes frais du juge), la condition de détectabilité $n \cdot r(A) \cdot \Delta \ge \operatorname{kl}(1-\beta, \alpha) + \ln(1/w_A)$ (forme exacte donnée par E.b) est non évaluable.
  2. Sur 20 mondes avec un score discret $\{0,1,2,3\}$ et $B_3$ conditionné au succès préalable de $B_1$ en G1, les ex-æquo tuent la puissance du test de Wilcoxon, et la zone $[+0,30 ; +0,60]$ laissait le duel sans conclusion.
  * **Statut : ACCEPTÉE.** Dans l'expérience corrigée ci-dessous, $n$ est explicitement fixé, le duel en ligne est ramené à 1 seule génération post-archive pour éliminer l'effet de trajectoire (critique A.a.3 sur B applicable ici), et l'hypothèse est formulée avec une frontière nette et un calcul d'erreur-type.
* **Critique D.b & E.a.4 — Mauvaise définition de la fausse découverte oracle sur les traits de bruit :** Une carte qui contient un trait de bruit $X_6$ mais capte aussi un vrai bassin étroit $B_1$ améliore réellement la prédiction sous l'oracle : la classer mécaniquement en fausse découverte à cause de la présence syntaxique de $X_6$ biaise la mesure.
  * **Statut : ACCEPTÉE.** La définition est corrigée par ablation prédictive sous l'oracle : une carte promue est une fausse découverte au sens de l'oracle si et seulement si son gain de log-vraisemblance sous la vraie loi du monde par rapport à la meilleure recombinaison de l'archive est $\le 0$ (ou si l'ablation des vrais traits plantés laisse son score inchangé).

---

## (b) Expériences corrigées (banc hors ligne et duel décisif en ligne)

Conformément au consensus du tour 1 (**OBSERVÉ-NON-AUDITÉ** [S1]) et à N-045, le protocole est scindé en deux expériences indépendantes, sans mélange de facteurs.

### Expérience 0 corrigée : Banc de métrologie hors ligne de la garde et de la dilution (0 appel LLM)

**Objectif :** Trancher hors ligne si le juge multi-échelles par paires de strates (Méthode 2 corrigée) bat le juge global ([F12] §1) sur des cartes à effet localisé, **sans céder** sur les recombinaisons par morceaux (`si_sinon`) alignées sur les cellules.

* **Paramètres scellés :**
  * $d = 12$ traits publics tirés selon deux régimes : (R1) loi produit indépendante $\mathcal{U}([-1, 1]^{12})$ ; (R2) loi gaussienne corrélée ($\rho_{ij} = 0,4^{|i-j|}$ [illustratif]) pour tester la critique B.c / E.c.
  * Taille des tirages frais du juge fixée à **$n = 2000$ épisodes** [illustratif] par génération. Niveau $\alpha = 0,05$.
  * Partition $\mathcal{P}$ scellée avant tirage des mondes : les $12$ coupures médianes marginales et les $\binom{12}{2} = 66$ quadrants médians $2 \times 2$ (total $|\mathcal{P}| = 1 + 24 + 264 = 289$ cellules ; poids $w_{\text{glob}} = 1/2$, et $w_C = \frac{1}{2 \times 288}$ pour chaque cellule locale, soit une pénalité maximale $\ln(1/w_C) = \ln(576) \approx 6,36\text{ nats}$ [illustratif]).
* **Jeux de cartes synthétiques testés (500 réplications par cellule du banc) :**
  1. **Contrôle Nul strict ($H_0^{\text{strict}}$) :** Monde réduit à l'archive $\mathcal{A}_1$. Cartes aléatoires dans la grammaire.
  2. **Contrôle de Garde hors-nul ($H_0^{\text{copie-cellule}}$ — critique A.c.3 / D.c) :** Monde réduit à $\mathcal{A}_1$ (composée de deux lois $L_a, L_b$). Cartes synthétiques de forme `si_sinon(X_1 > 0, L_a, L_b)` exactement alignées sur une frontière de la partition $\mathcal{P}$ (la classe où le juge actuel cède, **RAPPORTÉ** [F12] §1).
  3. **Contrôle de Parité pure ($H_0^{\text{parité}}$ — critique B.c.1) :** Monde avec interaction pure d'ordre 3 ($Y \sim \text{Bernoulli}(1/2 + \delta \text{sign}(X_1 X_2 X_3))$) et cartes d'ordre $\le 2$.
  4. **Signal Chirurgical ($H_1^{\text{chir}}$ — critique D.a.2 / E.a.2) :** Bassin étroit sur la strate $A = \{X_1 > 0, X_2 > 0\}$ de masse $r(A) = 0,05$ [illustratif] avec grille de profondeur $\Delta \in \{0,05 ; 0,10 ; 0,20 ; 0,30\}\text{ nats}$ [illustratif] (soit $n \cdot r(A) \cdot \Delta \in \{5 ; 10 ; 20 ; 30\}\text{ nats}$). La carte testée vaut $P = P_*$ sur $A$ et **exactement $P = Q_0$ hors de $A$**.
  5. **Signal Global Bruyant ($H_1^{\text{bruyant}}$) :** Même monde, mais la carte testée applique sa formule sur tout $\mathcal{X}$ : elle gagne $\Delta_A = +0,25\text{ nat}$ sur $A$ ($r(A)=0,05$) mais perd $\Delta_{\bar{A}} = -0,02\text{ nat}$ hors de $A$ (dérive globale nette $0,05(0,25) - 0,95(0,02) = -0,0065 < 0$).
* **Duel d'inférence forte (B4) pour l'Expérience 0 :**
  * $H_A$ : Sur $H_0^{\text{strict}}$ et $H_0^{\text{copie-cellule}}$, le juge muni du filtre pré-juge de recombinaison par cellule respecte $\Pr(E \ge 1/\alpha) \le 0,05$ (critère de queue substitué à la moyenne empirique suivant la critique A.b / E.b), **et** sur $H_1^{\text{bruyant}}$, la puissance à $\Delta_A = 0,25\text{ nat}$ dépasse celle du juge global d'au moins $+0,30$ [illustratif].
  * $H_B$ : Soit $\Pr_{H_0^{\text{copie-cellule}}}(E \ge 1/\alpha) > 0,05$ (garde brisée), soit la perte de puissance sur $H_1^{\text{chir}}$ due à la pénalité $\ln(576) \approx 6,36\text{ nats}$ dépasse $-0,15$ par rapport au juge global (auquel cas la Méthode 2 est abandonnée au profit du juge global).

---

### Expérience 1 corrigée : Duel en ligne à 1 facteur (Structuration combinatoire de la vue contre Énumération et Vue standard)

Pour éliminer les quatre défauts relevés par A, B, D et E (confusion amont/aval, impossibilité du plan $4 \times 12$, dérive d'archive entre générations, absence de témoin d'énumération simple), l'expérience en ligne porte **exclusivement sur le mécanisme amont (la vue)** en **une seule génération** au-dessus d'une archive scellée $\mathcal{A}_1$, avec **exactement le même regroupement et le même juge** ([C3] §3.1) dans tous les bras.

* **Architecture du monde planté (100 mondes indépendants à graine scellée, $d=8$ traits publics) :**
  * **Archive initiale $\mathcal{A}_1$ fournie dans la vue :** contient la loi vraie du bassin large $B_0$ portant sur $(X_1, X_2)$.
  * **Traits résiduels candidats :** 6 traits $(X_3, \dots, X_8)$.
  * **Bassins étroits plantés :**
    * $B_1$ (composante conditionnelle v4, **RAPPORTÉ** [C4] §2.1) : effet de $X_3$ dont le signe dépend de $\text{sign}(X_1)$ (nul en moyenne).
    * $B_2$ (composante hors-dictionnaire continu, critique A.c / B.c / D.c sur l'alignement) : effet monotone de $X_4$ confiné à la strate non centrée $X_2 > +0,6$ ($r(A) \approx 0,20$, $\Delta = 0,15\text{ nat}$ [illustratif]).
  * **Traits de bruit pur :** $(X_5, X_6, X_7, X_8)$ indépendants de $Y$.
  * **Taille d'échantillon du juge :** $n = 2000$ épisodes frais par monde ($n \cdot r(A) \cdot \Delta \approx 60\text{ nats} \gg \ln(m/\alpha)$ [illustratif], garantissant une puissance du juge $\pi_J > 0,95$ dès qu'une carte couvrant $B_1$ ou $B_2$ est émise).
* **Budget par monde et par bras :** $K = 5$ appels d'un même modèle bon marché (Argon ou Astra, N-045) en sessions neuves sans historique, $6$ cartes par appel ($M = 30$ cartes par monde).
  * *Justification mathématique de $K=5$ (correction de la critique A.a.1 / E.a.1) :* Pour $d_{\text{res}} = 6$ traits candidats $(X_3 \dots X_8)$, le nombre maximal de facteurs binaires couverts en force $t=2$ par $N=5$ lignes est $\binom{5-1}{\lfloor 5/2 \rfloor} = \binom{4}{2} = 6$ (**VÉRIFIÉ par calcul**). Le tableau couvrant $\text{CA}(5; 2, 6, 2)$ existe donc exactement :
    $$M_{\text{CA}} = \begin{pmatrix} 1 & 1 & 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 & 1 & 0 \\ 0 & 1 & 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 & 1 \end{pmatrix} \text{ (ou ses compléments équilibrés par strate de } (X_1, X_2)\text{).}$$
* **Les 3 bras à coût, longueur de jetons ($L_{\text{tok}}$) et juge strictement identiques :**
  1. **Bras $T_0$ (Témoin standard [C3]) :** Les 5 appels reçoivent la vue standard + un résumé statistique global du jeu public sans issue de longueur exacte $L_{\text{tok}}$.
  2. **Bras $T_{\text{énum}}$ (Témoin d'énumération simple / Placebo — critique A.c.2, B.c.3, D.c) :** Les 5 appels reçoivent la vue standard + la liste textuelle lexicographique complète des paires $(X_a, X_b)$ avec $a \in \{1,2\}, b \in \{3\dots 8\}$ et des statistiques marginales en vrac, formatée exactement à $L_{\text{tok}}$ jetons.
  3. **Bras $M_1$ (Plan couvrant de strates conditionnelles — Méthode 1 corrigée) :** Chacun des 5 appels $k \in \{1\dots 5\}$ reçoit la vue standard + la lentille descriptive n°$k$ (de longueur exacte $L_{\text{tok}}$) qui stratifie le jeu public sans issue selon les signes de l'archive $(X_1, X_2)$ et affiche les tables de contingence des 3 traits candidats activés par la ligne $k$ de $M_{\text{CA}}$.
* **Contrôle négatif sur 50 mondes Nuls/Additifs (critique B.c / Observation transversale de B) :** 50 mondes supplémentaires où $B_1 = B_2 = 0$ (seul $B_0$ archivé existe) et où les traits $(X_1 \dots X_8)$ sont corrélés ($\rho = 0,4$ [illustratif]). On y mesure le taux de cartes `si_sinon` brutes émises et le taux de fausses promotions par monde (FWER sous $H_0$ complet).
* **Métriques lues aux trois étages ([C3] §4.1, critique A.b) :**
  * Pour chaque monde $i \in \{1\dots 100\}$, on lit la couverture oracle $Y_i \in \{0 ; 0,5 ; 1\}$ (proportion des 2 bassins étroits $B_1, B_2$ couverts) aux trois étages : propositions brutes ($D_2^{\text{brut}}$), représentants ($D_2^{\text{rep}}$) et retenues ($D_2^{\text{ret}}$).
  * Différences appariées par monde : $\Delta_1 = D_2^{\text{ret}}(M_1) - D_2^{\text{ret}}(T_0)$ et $\Delta_2 = D_2^{\text{ret}}(M_1) - D_2^{\text{ret}}(T_{\text{énum}})$.
* **Règle de décision en inférence forte (sans zone d'indécision aveugle, critique E préambule) :**
  * Sur $R=100$ mondes appariés, l'erreur-type d'une différence de proportions est $\operatorname{SE} \le \frac{1}{2\sqrt{100}} = 0,05$ [illustratif] (demi-largeur d'IC à 95 % $\approx 0,10$).
  * **$H_A$ (Spécificité combinatoire du plan couvrant) :** $\mathbb{E}[\Delta_1] \ge +0,15$ **et** $\mathbb{E}[\Delta_2] \ge +0,10$, **et** sur les 50 mondes nuls corrélés, la proportion de mondes avec $\ge 1$ fausse découverte promue est $\le 0,06$ (garde intacte). *Si la borne inférieure de l'IC à 95 % de $\Delta_1$ dépasse $+0,05$ et celle de $\Delta_2$ dépasse $0$, $H_B$ est réfutée.*
  * **$H_B$ (Nullité du plan couvrant ou suffisance de l'énumération simple) :** $\mathbb{E}[\Delta_1] < +0,15$ ou $\mathbb{E}[\Delta_2] < +0,10$ ou fausse découverte $> 0,06$. *Si la borne supérieure de l'IC à 95 % de $\Delta_2$ est $< +0,10$, la machinerie du plan couvrant est réfutée au profit de la simple énumération textuelle ($T_{\text{énum}}$) ou du témoin ($T_0$).*
* **Coût matériel total de l'Expérience 1 corrigée :** $(100 + 50)\text{ mondes} \times 3\text{ bras} \times 5\text{ appels} = 2250\text{ appels}$ d'un modèle bon marché ($\approx 6,7\text{ M}$ jetons d'entrée, coût API estimé entre **$10\text{ \$}$ et $35\text{ \$}$ [illustratif]**).

---

## (c) Réponse finale à l'arbitre (en une page)

### 1. Ce qui est établi (par les faits et par les preuves mathématiques de ce tour)
* **Dans les faits transmis :**
  1. Lors de la course v67, la génération 1 a promu 11 variantes d'un même constat, et la génération 2 n'a promu aucune carte grâce à la garde contre les copies (**RAPPORTÉ**, [F12] §2).
  2. Le juge statistique actuel (valeurs $e$ + e-BH) contrôle le nul des lois de l'archive et de leurs recombinaisons couvertes, mais **cède hors de cette classe**, notamment face aux compositions par morceaux `si_sinon` et `melange` (**RAPPORTÉ**, [F12] §1). Toute pression vers la variété pousse vers cette zone vulnérable (**OBSERVÉ-NON-AUDITÉ**, [S1]).
  3. L'organisme appelle déjà les proposeurs en **session neuve sans historique** à chaque génération (**RAPPORTÉ**, [C3] §5.1). Le blocage par accumulation d'historique sur 24h observé par Bespoke Labs ($\rho = 0,84$, **RAPPORTÉ** [B]) est donc déjà neutralisé par construction ; ici, l'enfermement dans un bassin large provient du prieur intrinsèque des modèles face à une même vue statique.
* **Mathématiquement établi au cours de ce tour (VÉRIFIÉ par calcul) :**
  1. **Barrière de parité / d'interaction sans parent :** Tant que les proposeurs ne voient pas les issues $Y$ ni les résidus du juge (contrainte N-053), une composante conditionnelle d'ordre $k$ dont toutes les marges d'ordre $<k$ sont nulles (condition parente non détectable) exige $\Omega(\binom{d}{k})$ propositions à l'aveugle. Un gain mathématique en amont n'existe que sous une **hypothèse de hiérarchie héréditaire** (cas du monde v4 où la condition parente est déjà archivée, **RAPPORTÉ** [C4] §2.1).
  2. **Auto-localisation du rapport de vraisemblance :** Si une carte proposée $P$ ne diffère du nul $Q_0$ que sur une strate rare $A$ de masse $r(A)$ ($P = Q_0$ hors de $A$), alors la valeur $e$ globale est *identiquement égale* à la valeur $e$ restreinte à $A$ (les rapports hors de $A$ valent $1$). Un juge multi-échelles ne réduit donc pas la variance pour une carte déjà localisée ; il n'aide que les cartes globalement mal spécifiées hors de $A$, et paie en contrepartie un coût d'entrée logarithmique $\ln(|\mathcal{P}|)$. Quel que soit le juge, aucune détection à puissance $1-\beta$ n'est possible si $n \cdot r(A) \cdot \Delta_{\text{KL}}(A) < \operatorname{kl}(1-\beta, \alpha)$.
  3. **Incompatibilité de la pondération e-BH par nouveauté :** Pondérer les seuils de e-BH par l'orthogonalité prédictive d'un groupe ($w_j$ issus d'un DPP) est mathématiquement équivalent à multiplier la valeur $e$ par une prime de nouveauté, ce qui viole le rejet du tour 1 (**OBSERVÉ-NON-AUDITÉ** [S1]) et expose le budget de test aux cartes grammaticalement aberrantes. En revanche, le pivotage déterministe de Cholesky sur la matrice de Gram Hellinger par strates publiques fournit un choix de représentant strictement invariant à la multiplication des clones, sans toucher aux poids du juge.
  4. **Borne de Kleitman-Spencer sur les plans de vues :** $N$ appels binaires de force 2 ne peuvent couvrir simultanément que $\binom{N-1}{\lfloor N/2 \rfloor}$ facteurs candidats (soit 6 traits candidats pour $N=5$ appels).

### 2. Ce qui n'est pas établi (HYPOTHÈSES à trancher)
1. **Sensibilité générative des modèles aux vues combinatoires (HYPOTHÈSE) :** On ignore si présenter des tables descriptives stratifiées par l'archive ou la liste des paires de traits non croisées élève la probabilité brute $\Pi_v(B_{\text{étroit}})$ qu'un modèle émette la bonne loi conditionnelle, ou si le modèle ignore ces tableaux.
2. **Suffisance d'une simple énumération textuelle (HYPOTHÈSE) :** Même si structurer la vue aide, il n'est pas établi qu'un plan couvrant orthogonal ($\text{CA}(N; 2, d, 2)$) fasse mieux qu'une simple liste lexicographique des paires de traits absentes de l'archive.
3. **Effet secondaire sur la garde (HYPOTHÈSE) :** On ignore dans quelle mesure afficher les interactions manquantes dans la vue incite les proposeurs à émettre massivement des cartes `si_sinon` sur des traits corrélés sans interaction réelle, forçant la brèche connue du juge actuel.

### 3. L'expérience à faire en premier (la moins chère et la plus discriminante)

Conformément à la règle « d'abord un banc hors ligne, puis le bon marché à budget égal » ([S1], N-045), l'action immédiate comporte deux pas :

1. **Étape 0 (0 $, 0 appel LLM, < 30 min CPU [illustratif]) — Certification hors ligne de la garde sur recombinaisons par cellule :** Injecter au juge actuel 500 cartes synthétiques `si_sinon(X_1 > 0, L_a, L_b)` recombinaisons pures de deux lois de l'archive sur des mondes nuls à traits corrélés. Vérifier qu'un filtre mécanique pré-juge (rejetant toute carte dont la divergence Hellinger conditionnelle par strate publique au nul local de l'archive est $< \varepsilon$) ramène le taux de fausses promotions sous $\alpha = 0,05$.
2. **Étape 1 ($\approx 15\text{ \$}$ [illustratif], 1 modèle bon marché, 1 seule génération post-archive) — Test de sensibilité et de spécificité de la vue :**
   Sur 100 mondes v4 ($d=8$, 1 bassin large déjà dans l'archive $\mathcal{A}_1$, 2 bassins étroits conditionnels dont 1 hors-dictionnaire, $n=2000$ épisodes au juge) et 50 mondes purement additifs à traits corrélés (contrôle de fausse alerte), comparer à longueur de contexte $L_{\text{tok}}$ et juge strictement identiques ($K=5$ appels/monde) :
   * **Bras $T_0$ :** Vue standard.
   * **Bras $T_{\text{énum}}$ :** Vue standard + simple liste lexicographique des paires de traits non croisées avec l'archive.
   * **Bras $M_1$ :** Vue standard + les 5 lentilles du plan couvrant $\text{CA}(5; 2, 6, 2)$ stratifiées par l'archive.
   * **Verdict :** Si sur les 50 mondes additifs le taux de fausses promotions dépasse $6\%$, toute incitation aux interactions est bloquée jusqu'au renforcement du nul. Si $M_1$ ne bat pas $T_0$ d'au moins $+15$ points de couverture brute et retenue, toute structuration mathématique de la vue est abandonnée. Si $M_1$ bat $T_0$ mais ne bat pas $T_{\text{énum}}$ d'au moins $+10$ points, on retient la simple liste textuelle des paires non archivées et on abandonne les plans couvrants.

FIN-DE-CELLULE