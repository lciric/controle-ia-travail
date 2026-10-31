*Note d'intégrité (Règle 2) : La pièce `E3-T2-critique-croisee-A` est absente (statut : jamais lancée) ; je n'en invente pas le contenu.*

---

## (a) Réponse aux critiques visant la proposition C

### 1. Sur le transfert du seuil hors-pli (*out-of-fold*) vers la sonde finale $w_{\text{full}}$ et la perte de la garantie Beta exacte (B.a.1, B.c.3, D.a.1, D.a.2, D.b.1, D.b.2, D.c.1)
- **Statut : ACCEPTÉE et TRANSFORMÉE EN TEST (avec abandon de $w_{\text{full}}$ au profit d'un ensemble de plis figés ou du repli strict sur (B)).**
- **Raison :** B et D ont raison. Les scores hors-pli agrégés proviennent du mélange $\bar{G} = K^{-1}\sum_j G_j$ de $K$ sondes distinctes $w^{(-j)}$ ; l'égalité du quantile $q_{0,99}(\bar{G}) = q_{0,99}(F_{\text{full}})$ est une `HYPOTHÈSE` non garantie si la variance résiduelle n'est pas isotrope, et le chevauchement des plis brise la loi exacte $\text{Beta}(k, n+1-k)$. De plus (D.a.2), choisir l'hyperparamètre de régularisation sur ces mêmes plis crée une fuite de sélection.
- **Correction :** La loi $\text{Beta}(k, n+1-k)$ (`VÉRIFIÉ`) n'est exacte que pour un classifieur unique figé évalué sur un échantillon de calibration strictement disjoint (*split conformal*). Je retire donc l'Option C de la recommandation principale au profit de l'**Option (B) pure** (découpage disjoint sur Bailey seul), où la sonde est figée avant toute lecture du seuil. La validité du transfert hors-pli est transformée en test empirique dans l'Expérience 1 corrigée.

### 2. Sur l'inversion algébrique de la monotonie entre $X_{(1)}$ et $X_{(7)}$ dans l'Expérience 3 (D.a.5) et la résolution à petit $N_{\text{dir}}$ (B.b.3)
- **Statut : ACCEPTÉE.**
- **Raison :** La critique D.a.5 identifie une erreur de signe dans ma formulation du tour III.1. En notant $X_{(1)} \ge X_{(3)} \ge X_{(7)}$ les $1^{\text{er}}$, $3^{\text{e}}$ et $7^{\text{e}}$ plus grands scores bénins sur 300, $X_{(1)}$ est le seuil de détection le plus élevé : il produit le moins de fausses alertes ($\approx 0,33\%$) mais laisse passer le plus d'entrées adverses (rappel $R_d(t)$ plus bas). Comme une direction est comptée lorsque $R_d(t) < \tau$, la fonction $N_{\text{dir}}(t)$ est **croissante** en $t$, donc $N_{\text{dir}}(X_{(1)}) \ge N_{\text{dir}}(X_{(3)}) \ge N_{\text{dir}}(X_{(7)})$. Le seuil conservateur (pire cas donnant la borne inférieure du nombre de directions) est $t_{\text{strict}} = X_{(7)}$, et la borne supérieure est $t_{\text{lâche}} = X_{(1)}$. Ma différence non signée $N_{\text{dir}}(X_{(7)}) - N_{\text{dir}}(X_{(1)})$ était donc $\le 0$ par construction. Par ailleurs, B.b.3 note à juste titre qu'un écart relatif explose ou manque de résolution si $N_{\text{dir}}(X_{(3)})$ est proche de 0.
- **Correction :** Dans l'Expérience 3 corrigée et dans le rapport de sensibilité de (B), le numérateur est inversé en $N_{\text{dir}}(X_{(1)}) - N_{\text{dir}}(X_{(7)}) \ge 0$, et le dénominateur est complété par un seuil de variation absolue des rappels individuels $R_d(X_{(7)}) - R_d(X_{(1)})$ pour ne pas dépendre d'un petit compte $N_{\text{dir}}$.

### 3. Sur le statut de l'intervalle Beta ($[0,0021 ; 0,0238]$) et de la bande $[N_{\text{dir}}(X_{(7)}), N_{\text{dir}}(X_{(1)})]$ (D.a.3, D.a.4)
- **Statut : ACCEPTÉE.**
- **Raison :** D a raison sur les deux points de vocabulaire statistique : (1) le support de la variable aléatoire de couverture $U \sim \text{Beta}(3, 298)$ est $(0, 1)$, donc $[0,0021 ; 0,0238]$ (`VÉRIFIÉ`) est un intervalle de couverture à $95\%$ et non une borne déterministe ; (2) évaluer $N_{\text{dir}}$ en $X_{(7)}, X_{(3)}, X_{(1)}$ fournit une analyse de sensibilité déterministe balayant les seuils dont les taux moyens ($\approx 2,33\%, 1,0\%, 0,33\%$) encadrent l'intervalle à $95\%$, et non un intervalle de confiance formel sur $N_{\text{dir}}$.
- **Correction :** Terminologie rectifiée dans toute la proposition : on distingue l'intervalle de confiance de Clopper-Pearson/Beta à $95\%$ sur le taux de fausses alertes et la « fourchette de sensibilité aux statistiques d'ordre $(X_{(7)}, X_{(3)}, X_{(1)})$ » sur $N_{\text{dir}}$.

### 4. Sur la sous-puissance du test de l'Expérience 2 à $n_1 = 200$ et l'erreur logique « non-rejet $\Rightarrow$ validation » (B.a.2, B.b.2, D.a.7, D.b.3, D.b.4)
- **Statut : ACCEPTÉE et TRANSFORMÉE EN TEST (inversion du fardeau de la preuve par test d'équivalence TOST).**
- **Raison :** B et D démontrent tous deux le point décisif : avec seulement 200 bénins de Bailey hors-entraînement (`val` + `test`, fait `RAPPORTÉ`), observer 2 dépassements donne un intervalle de Clopper-Pearson à $95\%$ de $[0,0012 ; 0,0356]$ (`VÉRIFIÉ` d'après la ligne `mesure n=200` des faits), qui est plus large que l'intervalle cible $[0,0021 ; 0,0238]$ de $n=300$. Un test de supériorité classique ($p_{\text{KS}} > 0,05$) n'a pas la puissance requise dans la queue à $99\%$ et confond absence de preuve et preuve d'absence.
- **Correction :** Deux conséquences majeures :
  1. Sur le plan méthodologique (Question 2 de l'arbitre), cette impossibilité mathématique de certifier la queue à $99\%$ d'un jeu externe avec seulement 200 bénins de référence ($[0,0012 ; 0,0356]$) est la **preuve formelle qu'il faut rejeter (A) au profit de (B)**.
  2. Dans l'Expérience 2 corrigée, la charge de la preuve est inversée via une procédure d'équivalence **TOST** (*Two One-Sided Tests*) : l'hypothèse nulle est le décalage de domaine, et l'Option (A) n'est validée que si l'intervalle de confiance à $90\%$ de l'écart de quantile et du taux croisé tombe **entièrement à l'intérieur** de la marge d'équivalence.

### 5. Sur l'insuffisance du contrôle à $50\%$ de permutation, l'insuffisance du cosinus seul et le déséquilibre $400/800$ (B.a.3, B.a.5, B.b.1, D.a.8, D.c.3)
- **Statut : ACCEPTÉE.**
- **Raison :**
  1. Permuter $50\%$ des étiquettes laisse un signal linéaire non nul ; le contrôle négatif doit utiliser une **permutation de $100\%$ des étiquettes** ainsi que des répétitions appariées à taille égale ($400$ vs $400$ disjoints) pour mesurer le bruit de rééchantillonnage pur (D.c.3).
  2. B.b.1 montre exactement que $\cos(w_{800}, w_{400}) \ge 0,95$ ne suffit pas si la densité $f_S(t_{0,01})$ est raide : une faible rotation angulaire $\delta\theta$ déplace le quantile de $\Delta t \propto \delta\theta \cdot \sigma_\perp$. Il faut donc contrôler directement l'écart de taux de fausses alertes croisé et le rappel à FPR $= 1\%$ fixé.
  3. B.a.5 note que passer de $800/800$ à $400$ bénins / $800$ nuisibles modifie le ratio de classes ($1:2$), ce qui déplace l'ordonnée à l'origine et, sous régularisation $\ell_2$, peut faire tourner $w$ si la perte n'est pas repondérée par l'inverse des fréquences de classe ($w_{\text{bénin}} = 2, w_{\text{nuisible}} = 1$).
- **Correction :** Ces trois corrections sont intégrées dans le protocole de l'Expérience 1 corrigée.

### 6. Sur la séparation entre optimisation et évaluation des entrées adverses (D.a.6, D.b.5, D.c.4)
- **Statut : ACCEPTÉE (pour le protocole d'évaluation de l'Expérience 3).**
- **Raison :** D souligne que si les mêmes 200 entrées adverses servent à optimiser une direction et à mesurer son rappel final par rapport à $\tau$, la mesure souffre d'un biais d'optimisation in-sample.
- **Correction :** Les faits (`RAPPORTÉ`) stipulent que le jeu de Bailey contient $800 / 100 / 100$ nuisibles (`train / val / test`) et que la taille d'échantillon exige « au moins 200 adverses » par direction. Dans l'Expérience 3 corrigée, l'optimisation des directions sur le pilote s'effectue sur un sous-ensemble disjoint des nuisibles d'entraînement (ou sur `val`), et la lecture des rappels aux seuils $(X_{(7)}, X_{(3)}, X_{(1)})$ se fait exclusivement sur **200 entrées nuisibles verrouillées hors-optimisation** (`val + test` = 200 nuisibles de Bailey, fait `RAPPORTÉ`).

### 7. Sur les contrôles négatifs hors-portée de D-ML-1 : sonde sur modèle `base` vs `instruct` et juge StrongREJECT sur sorties incohérentes (B.c.1, B.c.2)
- **Statut : REJETÉE comme condition bloquante de la décision D-ML-1 (car fixée par le préenregistrement v3), mais ACCEPTÉE comme contrôle de validité de l'Expérience 3.**
- **Raison du rejet partiel :** La question de l'arbitre porte exclusivement sur la décision **D-ML-1 (taille et découpage du jeu bénin : A vs B)** au sein du préenregistrement `P-041-malleabilite-v3.md` où le modèle public de 8B et le juge StrongREJECT affiné (score $> 0,5$) sont déjà fermés (`RAPPORTÉ`). Remplacer le modèle par un modèle `base` dépasse le mandat de D-ML-1.
- **Ce qui est retenu :** En revanche, l'objection B.c.2 (des directions qui détruisent la cohérence du texte et font chuter le score StrongREJECT sous $0,5$ par simple bafouillage) affecte directement la lecture des seuils $\tau = 20\%$ et $5\%$ dans l'Expérience 3. J'ajoute donc dans l'Expérience 3 corrigée un contrôle négatif par **directions aléatoires de même norme d'intervention** pour vérifier que la chute sous le seuil de la sonde et le score StrongREJECT $> 0,5$ ne sont pas l'artefact d'une dégradation aveugle.

---

## (b) Expériences corrigées (en inférence forte $H_A$ contre $H_B$)

*Note sur les seuils numériques (réponse à B.a.4) : Conformément à la Règle 4 du protocole, toute valeur numérique absente des faits porte obligatoirement la marque `illustratif`. Pour éviter toute ambiguïté entre exemple décoratif et règle de décision, chaque seuil marqué `illustratif` ci-dessous constitue la **valeur de coupure préenregistrée proposée à l'arbitre** pour falsifier $H_A$ ou $H_B$.*

### Expérience 1 (corrigée) : Suffisance de $n_{\text{train}} = 400$ bénins repondérés contre $800$ bénins pour l'entraînement de la sonde linéaire
- **Objectif :** Tester si la réduction du jeu bénin d'entraînement de 800 à 400 (Option B) dégrade la queue bénigne à $1\%$ ou le rappel nuisible de la sonde.
- **Hypothèses exclusives :**
  - **$H_A$ (Stabilité à $n=400$ repondéré)** : En entraînant la sonde linéaire avec pondération des classes ($2:1$ pour compenser $400$ bénins face à $800$ nuisibles) et régularisation $\ell_2$ fixée par validation croisée imbriquée, la perte de rappel à $\text{FPR} = 1\%$ et la dérive du quantile bénin à $99\%$ par rapport à la sonde entraînée sur $800/800$ restent inférieures au bruit d'échantillonnage intrinsèque à taille égale.
  - **$H_B$ (Dégradation géométrique de la queue en haute dimension)** : Réduire les bénins d'entraînement de 800 à 400 alourdit la queue des scores bénins hors-échantillon et fait chuter le rappel sur nuisibles au seuil de $1\%$ au-delà de la tolérance.
- **Protocole et métriques :**
  1. Sur les $800$ bénins `train` et $800$ nuisibles `train` de Bailey (`RAPPORTÉ`), entraîner la sonde de référence $w_{800}$.
  2. Tirer $M = 50$ (`illustratif`) partitions aléatoires des $800$ bénins `train` en deux moitiés disjointes de $400$ bénins : $B_{400}^{(m,1)}$ et $B_{400}^{(m,2)}$. Entraîner $w_{400}^{(m,1)}$ et $w_{400}^{(m,2)}$ face aux $800$ nuisibles avec pondération $w_{\text{bénin}}=2, w_{\text{nuisible}}=1$.
  3. Évaluer sur les **200 bénins et 200 nuisibles hors-entraînement** (`val + test` de Bailey, `RAPPORTÉ`) :
     - La perte moyenne de rappel $\Delta \text{TPR}_{1\%} = \text{TPR}_{1\%}(w_{800}) - \overline{\text{TPR}}_{1\%}(w_{400})$, où le seuil à $1\%$ de chaque sonde est son propre $2^{\text{e}}$ plus grand score sur les 200 bénins `val+test`.
     - Le déplacement de queue inter-sondes : le taux de fausses alertes de $w_{400}^{(m,1)}$ lorsqu'on lui applique le seuil calibré sur $w_{400}^{(m,2)}$ (et le cosinus $\cos(w_{800}, w_{400}^{(m,1)})$ à titre diagnostique).
- **Contrôles négatifs et de variance nulle :**
  1. *Contrôle négatif absolu* : Permutation de **$100\%$ des étiquettes** (bénin/nuisible) sur l'entraînement $\rightarrow$ vérifie que $\text{TPR}_{1\%}$ chute autour de $1\%$ ($\le 3\%$, `illustratif`) et $\cos \approx 0$.
  2. *Ligne de base de variance à taille égale* : Écart moyen $|\text{TPR}_{1\%}(w_{400}^{(m,1)}) - \text{TPR}_{1\%}(w_{400}^{(m,2)})|$ entre deux sondes entraînées sur deux lots disjoints de 400 bénins.
  3. *Test subsidiaire de l'Option C (hors-pli)* : Vérifier sur les 200 bénins `val+test` si le seuil hors-pli à $1\%$ des plis de $w_{800}$ appliqué à $w_{800}$ donne exactement le même nombre de dépassements (à $\pm 1$ près sur 200, `illustratif`) qu'un seuil calibré hors-échantillon.
- **Règle de décision et falsification :**
  - Si $\Delta \text{TPR}_{1\%} \le 2,0$ points de pourcentage (`illustratif`) ET $\cos(w_{800}, w_{400}) \ge 0,95$ (`illustratif`) : **$H_B$ est falsifiée** $\rightarrow$ la sonde à 400 bénins de l'Option (B) est validée.
  - Si $\Delta \text{TPR}_{1\%} > 2,0$ points ou $\cos < 0,95$ : **$H_A$ est falsifiée** $\rightarrow$ l'entraînement à 400 bénins dégrade la sonde ; on conserve alors les **800 bénins de `train` pour la sonde**, ou un découpage asymétrique **600 (sonde) / 200 (seuil) / 200 (mesure)** (dont les intervalles exacts sont déjà servis dans les faits : seuil $n=200 \rightarrow [0,0012 ; 0,0275]$ et mesure $n=200 \rightarrow [0,0012 ; 0,0356]$, `VÉRIFIÉ`).

### Expérience 2 (corrigée) : Test d'équivalence distributionnelle (TOST) de la queue à $99\%$ d'un jeu bénin externe (Option A)
- **Objectif :** Éviter l'erreur logique du non-rejet en imposant à tout jeu externe $D_{\text{ext}}$ ($N=2000$) de prouver positivement son équivalence de queue avec Bailey.
- **Hypothèses exclusives :**
  - **$H_A$ (Incompatibilité / Décalage de domaine — hypothèse par défaut)** : Le quantile à $99\%$ des scores de la sonde $w_{800}$ sur le jeu externe $D_{\text{ext}}$ s'écarte du quantile à $99\%$ des bénins de Bailey d'au moins $\pm \delta_q$, ou induit un taux de fausses alertes hors de $[0,0021 ; 0,0238]$ (`RAPPORTÉ`).
  - **$H_B$ (Équivalence de queue certifiée)** : La loi des scores sur $D_{\text{ext}}$ est équivalente à celle de Bailey dans la queue supérieure à l'intérieur strict de la marge d'équivalence préenregistrée.
- **Protocole et métriques :**
  - *Pour augmenter la puissance au-delà de $n_1 = 200$ sans aucun biais in-sample* (réponse à B.b.2 et D.b.3) : on calcule les scores des **1 000 bénins de Bailey** de manière strictement hors-échantillon en évaluant les 200 bénins `val+test` et, par validation croisée stratifiée à 5 plis de taille 800, l'intégralité des 1 000 bénins de Bailey contre les 2 000 bénins de $D_{\text{ext}}$ évalués par les mêmes sondes.
  - On applique une procédure **TOST (deux tests unilatéraux à $\alpha = 5\%$)** par bootstrap non paramétrique ($10\,000$ répliques, `illustratif`) sur l'écart standardisé du quantile à $99\%$ : $\Delta q_{0,99} = \frac{\hat{q}_{0,99}(D_{\text{ext}}) - \hat{q}_{0,99}(\text{Bailey})}{\sigma_{\text{Bailey}}}$, et on calcule l'intervalle de confiance de Clopper-Pearson à $90\%$ du taux de dépassement croisé $\hat{\alpha}_{\text{croisé}}$ des 1 000 scores hors-échantillon de Bailey au seuil $99\%$ de $D_{\text{ext}}$.
- **Contrôles négatifs :**
  1. *Contrôle interne $H_B$ vrai (hors-entraînement)* : Diviser les 1 000 scores hors-échantillon de Bailey en deux lots aléatoires de 500 vs 500 $\rightarrow$ vérifie la probabilité empirique que le TOST conclue à l'équivalence sous même distribution.
  2. *Contrôle positif de dérive de queue ($H_A$ vrai)* : Remplacer $10\%$ de $D_{\text{ext}}$ par des requêtes bénignes longues ou frontières (ex. filtrées par longueur $> 90^{\text{e}}$ centile) $\rightarrow$ le TOST doit refuser l'équivalence.
- **Règle de décision et falsification :**
  - Si l'intervalle de confiance à $90\%$ de $\Delta q_{0,99}$ est entièrement inclus dans $[-0,15 ; +0,15]$ (`illustratif`) ET que l'intervalle de Clopper-Pearson à $90\%$ de $\hat{\alpha}_{\text{croisé}}$ est entièrement inclus dans $[0,0048 ; 0,0171]$ (l'intervalle à $95\%$ de $n=1000$ des faits `RAPPORTÉ`) : **$H_A$ est falsifiée** $\rightarrow$ le jeu externe est certifié pour l'Option (A).
  - Sinon : **$H_B$ est falsifiée (ou non démontrée par manque de puissance)** $\rightarrow$ l'Option (A) est rejetée au profit de (B).

### Expérience 3 (corrigée) : Sensibilité monotone du compte de directions entre $X_{(7)}$ et $X_{(1)}$ sur entrées adverses hors-optimisation (Option B)
- **Objectif :** Tester si le bruit de calibration à $n=300$ bénins ($[0,0021 ; 0,0238]$, `RAPPORTÉ`) rend instable la lecture aux seuils de rappel $\tau < 20\%$ et $\tau < 5\%$.
- **Hypothèses exclusives :**
  - **$H_A$ (Stabilité de lecture à $n=300$)** : Les directions de camouflage optimisées ne s'accumulent pas dans la bande de seuil $[X_{(7)}, X_{(1)}]$ ; la variation du nombre de directions validées et des rappels individuels entre $X_{(7)}$ et $X_{(1)}$ reste bornée sous le seuil de tolérance.
  - **$H_B$ (Effet de falaise près du seuil)** : Une proportion importante des directions optimisées possède un rappel sur adverses très sensible au déplacement du seuil entre $X_{(7)}$ (taux moyen $\approx 2,33\%$) et $X_{(1)}$ (taux moyen $\approx 0,33\%$).
- **Protocole et métriques (corrigés des critiques D.a.5, D.a.6 et B.b.3) :**
  1. Sur un pilote de $D = 50$ directions cherchées (`illustratif`), optimiser chaque direction uniquement sur un sous-ensemble des nuisibles de `train` (avec objectif de marge continue, sans arrêt anticipé sur $X_{(3)}$).
  2. Verrouiller les **200 entrées nuisibles hors-entraînement** (`val` 100 + `test` 100 de Bailey, `RAPPORTÉ`) qui n'ont jamais servi à l'optimisation des directions. Ne conserver comme entrées adverses valides que celles dont la sortie générée sous perturbation reste jugée nuisible par StrongREJECT ($> 0,5$, `RAPPORTÉ`).
  3. Pour les 300 bénins de seuil de (B), extraire les statistiques d'ordre ordonnées $X_{(1)} \ge X_{(3)} \ge X_{(7)}$. Par monotonie décroissante du rappel $R_d(t)$ en fonction du seuil $t$, on a de façon garantie :
     $$N_{\text{dir}}(X_{(1)}) \ge N_{\text{dir}}(X_{(3)}) \ge N_{\text{dir}}(X_{(7)})$$
  4. Calculer deux métriques positives :
     - L'amplitude relative du compte : $\Delta_{\tau}^{+} = \frac{N_{\text{dir}}(X_{(1)}) - N_{\text{dir}}(X_{(7)})}{\max(10, N_{\text{dir}}(X_{(3)}))}$ (le dénominateur plancher à $10$, `illustratif`, corrige la perte de puissance à petit $N_{\text{dir}}$ signalée par B.b.3).
     - Le décalage médian de rappel par direction : $M_{\Delta R} = \text{médiane}_{d} \big( R_d(X_{(7)}) - R_d(X_{(1)}) \big) \ge 0$.
- **Contrôles négatifs (corrigés de B.c.2 et D.c.4) :**
  1. *Contrôle de perturbation aléatoire de même norme (anti-bafouillage)* : Appliquer 50 directions aléatoires isotropes de même norme d'activation sur les 200 nuisibles `val+test` et mesurer conjointement le score de la sonde et le score StrongREJECT $\rightarrow$ vérifie que les directions comptées ne sont pas de simples destructions de génération.
  2. *Contrôle sans optimisation* : Rappels des 200 nuisibles non perturbés en $X_{(7)}, X_{(3)}, X_{(1)}$.
- **Règle de décision et falsification :**
  - Si $\Delta_{20\%}^{+} \le 0,15$ et $\Delta_{5\%}^{+} \le 0,15$ ET $M_{\Delta R} \le 0,05$ ($5$ points de rappel, `illustratif`) : **$H_B$ est falsifiée** $\rightarrow$ la lecture à $n=300$ est stable.
  - Si $\Delta_{20\%}^{+} > 0,15$ ou $\Delta_{5\%}^{+} > 0,15$ ou $M_{\Delta R} > 0,05$ : **$H_A$ est falsifiée** $\rightarrow$ le seuil ponctuel $X_{(3)}$ est trop instable seul ; le résultat principal rapporté doit obligatoirement être le couple conservateur/nominal $\big(N_{\text{dir}}(X_{(7)}), N_{\text{dir}}(X_{(3)})\big)$.

---

## (c) Réponse à la question de l'arbitre (Synthèse en une page)

### 1. Ce qui est établi
- **Exactitude mathématique des intervalles servis (`VÉRIFIÉ`)** : Dans `calcul-taux-fausses-alertes-benins-v1.sortie.txt` (`RAPPORTÉ`), les intervalles de `mesure` ($[0,0048 ; 0,0183]$ pour $10/1000$ ; $[0,0021 ; 0,0289]$ pour $3/300$ ; $[0,0012 ; 0,0356]$ pour $2/200$) sont les intervalles exacts de Clopper-Pearson à $95\%$ ($\text{Beta}(0,025 ; k, n-k+1)$ et $\text{Beta}(0,975 ; k+1, n-k)$). Les intervalles de `seuil` ($[0,0048 ; 0,0171]$ pour $n=1000, k=10$ ; $[0,0021 ; 0,0238]$ pour $n=300, k=3$ ; $[0,0012 ; 0,0275]$ pour $n=200, k=2$) sont les quantiles à $2,5\%$ et $97,5\%$ de la loi exacte de couverture hors-échantillon $\text{Beta}(k, n+1-k)$ d'un seuil fixé sur la $k$-ième statistique d'ordre continue d'une sonde figée.
- **Impossibilité de certifier un jeu externe (Option A) avec les 200 bénins restants de Bailey (`VÉRIFIÉ`)** : Si l'on garde 800 bénins de Bailey pour entraîner la sonde (`RAPPORTÉ`), il ne reste que $100 + 100 = 200$ bénins (`val + test`) de Bailey pour tester si un jeu externe (Option A) possède la même queue à $99\%$. Or, à $n=200$, $2/200$ fausses alertes donnent un intervalle de Clopper-Pearson à $95\%$ de $[0,0012 ; 0,0356]$ (`VÉRIFIÉ`), qui est **plus large** que l'incertitude de calibration de l'Option B à $n=300$ ($[0,0021 ; 0,0238]$). On ne peut donc pas prouver statistiquement sur 200 bénins qu'un jeu externe ne biaise pas le seuil à $1\%$ davantage que le bruit d'échantillonnage de (B).
- **Limite des méthodes de validation croisée (Option C écartée comme garantie exacte)** : Calibrer le seuil sur des scores hors-pli (*out-of-fold*) de $K$ sondes puis l'appliquer à une sonde finale unique $w_{\text{full}}$ ne conserve pas la garantie exacte $\text{Beta}(k, n+1-k)$ sans une hypothèse supplémentaire d'invariance des queues entre plis (`HYPOTHÈSE`).
- **Indépendance de la résolution des rappels $\tau$ vis-à-vis de $n_{\text{bénin}}$ (`RAPPORTÉ`)** : La granularité de lecture de $\tau < 50\%, 20\%, 5\%$ dépend du nombre d'entrées **adverses** évaluées ($\ge 200$ adverses hors-optimisation, soit $10/200$ à $5\%$), et non de $n=300$ bénins qui gouverne uniquement la position du seuil $t$ de la sonde.

### 2. Ce qui n'est pas établi (Statut : `HYPOTHÈSE`)
- **Stabilité de la sonde linéaire entre 800 et 400 bénins d'entraînement** : On ignore si diviser par deux les bénins d'entraînement (de 800 à 400 face à 800 nuisibles dans l'Option B) déforme l'hyperplan en haute dimension et dégrade le rappel de base à $\text{FPR} = 1\%$.
- **Pente locale des rappels adverses entre $X_{(7)}$ et $X_{(1)}$** : On ignore si les directions de camouflage optimisées passent franchement sous le seuil ou s'accumulent dans la zone d'incertitude $[X_{(7)}, X_{(1)}]$ de $n=300$.
- **Existence d'un réservoir public identique à Bailey** : Les jeux bénins publics candidats (`Alpaca`, `UltraChat`, `OR-Bench`, `XSTest` — statut `HYPOTHÈSE`) présentent un risque de décalage de domaine (*domain shift* lexical ou de longueur) capable de fausser systématiquement le quantile à $99\%$.

### 3. Décision recommandée, quoi rapporter pour (B), pire cas et expérience à faire en premier
- **Choix recommandé : Option (B) sur le seul jeu de Bailey**, car son erreur de calibration est sans biais et de loi exacte connue ($\text{Beta}(3, 298)$), contrairement au biais systématique non borné de (A).
  - *Sous-découpage selon le résultat de l'Expérience 1* : Si 400 bénins (repondérés $2:1$) suffisent à entraîner la sonde sans perte de rappel à $1\%$, adopter **400 (sonde) / 300 (seuil) / 300 (mesure)**. Si 400 bénins dégradent la sonde, adopter **600 (sonde) / 200 (seuil) / 200 (mesure)** (intervalles exacts déjà calculés dans les faits : $[0,0012 ; 0,0275]$ au seuil et $[0,0012 ; 0,0356]$ en mesure, `RAPPORTÉ`).
- **Ce qu'il faut rapporter dans (B) pour que $\tau = 20\%$ et $5\%$ soient interprétables** :
  Enregistrer les scores de la sonde sur 200 entrées adverses **hors-optimisation** (`val + test`) pour chaque direction cherchée, et rapporter systématiquement le nombre de directions $N_{\text{dir}}$ lu à trois statistiques d'ordre du lot de seuil ($n=300$, avec $X_{(1)} \ge X_{(3)} \ge X_{(7)}$) :
  1. **$t_{\text{strict}} = X_{(7)}$** ($7^{\text{e}}$ plus grand score bénin, $\approx 2,33\%$ de FPR moyen, couvrant la borne haute $0,0238$) $\rightarrow$ donne la **borne inférieure conservatrice** $N_{\text{dir}}(X_{(7)})$ ;
  2. **$t_{\text{nom}} = X_{(3)}$** ($3/300 = 1,0\%$ nominal) $\rightarrow$ valeur centrale $N_{\text{dir}}(X_{(3)})$ ;
  3. **$t_{\text{lâche}} = X_{(1)}$** ($1^{\text{er}}$ plus grand score bénin, $\approx 0,33\%$ de FPR moyen, près de la borne basse $0,0021$) $\rightarrow$ donne la **borne supérieure** $N_{\text{dir}}(X_{(1)})$.
  Rapporter également le taux de fausses alertes réalisé sur les 300 bénins de mesure verrouillés avec son intervalle de Clopper-Pearson à $95\%$.
- **Pire cas de (B) et condition de bascule vers (A)** : Le pire cas est un écart massif entre $N_{\text{dir}}(X_{(7)})$ et $N_{\text{dir}}(X_{(1)})$ ($\Delta_{5\%}^{+} > 15\%$ sur le pilote) combiné à une dégradation de la sonde à $n_{\text{train}}=400$. Je ne changerais d'avis en faveur de (A) que si le script exact ayant généré les bénins de Bailey permet d'extraire 2 000 bénins supplémentaires de la **même source mère** et que ce lot passe le test d'équivalence TOST de l'Expérience 2.
- **Expérience à faire en premier (immédiate, $< 2$ minutes de GPU et $< 30$ secondes CPU, `illustratif`)** :
  Lancer l'**Expérience 1 corrigée** sur les fichiers de Bailey déjà sur disque (`800 train` + `200 val/test`, `RAPPORTÉ`) : comparer la sonde entraînée sur 800 bénins à 50 sondes entraînées sur 400 bénins (repondérés $2:1$) en mesurant leur perte de rappel à $\text{FPR} = 1\%$ sur les 200 nuisibles et 200 bénins `val+test`. Cela tranche immédiatement et sans versement externe si le découpage $400/300/300$ de (B) est sain dès l'étape de la sonde.

FIN-DE-CELLULE