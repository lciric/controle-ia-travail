# Cellule C — Tour III.2 — Critique croisée de méthode

Les pièces des faits (A, B, C, D), la question de l'arbitre et les propositions A et B du tour III.1 sont présentes, intègres et non coupées (VÉRIFIÉ). 

---

## Sur la proposition A

### (a) Défauts de méthode : variables confondantes, vérités par construction, fuites

1. **Vérité par construction (tautologie générateur-objectif) dans E1.** 
   Dans son expérience E1, la proposition A modifie le générateur des mondes de la pièce B pour planter des « ponts conceptuels vrais » définis par « $\ge 2$ opérateurs latents non-moyeux partagés ou 1 opérateur rare » (RAPPORTÉ, proposition A § b-E1). Simultanément, elle définit la qualité de sa paire dans `O-paires` par $w_p = q_i q_j \cdot c_{ij}^\alpha \cdot (1 - s_{ij})^\beta$, où $c_{ij} = \langle k_i, k_j \rangle$ est le produit scalaire des vecteurs de concepts pondérés par la rareté inverse (RAPPORTÉ, A § b). 
   *Défaut :* Le score $c_{ij}$ calcule exactement la statistique suffisante de la loi qui a servi à planter la vérité (la somme pondérée par la rareté des cooccurrences d'opérateurs). Que $\alpha=1$ batte $\alpha=0$ dans ce monde modifié est **vrai par construction** dès que le bruit d'observation du lexique est inférieur à 1 (couverture de 0,90 à 0,45 selon pièce B § 5, RAPPORTÉ). Ce test ne valide pas l'hypothèse scientifique ; il vérifie seulement qu'un produit scalaire retrouve les paires plantées par un produit scalaire.

2. **Fuite entre construction et évaluation par seuillage dur des moyeux.**
   Pour défendre sa représentation contre la manipulation (E4), A ajoute la règle mécanique : « une étiquette présente dans plus de 25 % du vivier (le taux de moyeu de B § 5) sort du vecteur » (RAPPORTÉ, A § b-E4). 
   *Défaut :* Il s'agit d'une **fuite directe** des paramètres cachés du générateur de test (pièce B § 5 : « un moyeu présent dans 25 % des articles », RAPPORTÉ) vers la conception de l'instrument. De plus, c'est une **variable confondante** majeure dans E1 : si `O-paires` gagne, on ne peut pas savoir si le gain vient de la forme continue du noyau à deux espaces ou de la troncature franche à 25 % qui élimine les pièges moyeux par décret.

3. **Confusion dans la matrice de diversité $\Phi$ de `O-paires`.**
   A pose $\phi_p = [\text{indicatrice de la strate} ; \lambda \cdot (e_i + e_j)]$ (RAPPORTÉ, A § b). Elle affirme qu'à $\alpha = \beta = 0$, cela équivaut au tirage stratifié avec préférence de qualité. 
   *Défaut :* C'est algébriquement inexact pour $\lambda > 0$. Le terme $\lambda(e_i + e_j)$ pénalise les paires qui partagent un article (degré maximal 1 dans le graphe d'appariement), alors que le tirage stratifié de la pièce A (`tirage_stratifie`, VÉRIFIÉ) et de la pièce B (§ 5, RAPPORTÉ) autorise une fiche à appartenir à plusieurs paires si elle traverse plusieurs strates. La variable $\lambda$ confond donc la « diversité des strates de domaines » avec une « contrainte de couplage disjoint sur les fiches ».

4. **Ancrage lexical (R1+R3) confondant concept et surface.**
   A recommande de faire déclarer les concepts par le proposeur (R1) et d'exiger un ancrage vérifié par programme (R3 : symbole, formule, nom de théorème) dans le texte de la fiche (RAPPORTÉ, A § b-E4). 
   *Défaut :* Dans les mondes de la pièce B, un même opérateur latent a « un mot de surface différent dans chaque domaine » (pièce B § 5, RAPPORTÉ). Sur de vraies fiches, exiger une correspondance exacte de chaîne ou de symbole avec une liste fermée détruit la capacité à relier deux domaines qui nomment la même structure différemment, ou force le proposeur à réécrire son texte avec le jargon de la liste fermée, ce qui fuit dans le vecteur de domaine $d_i$.

### (b) Conditions mesurables (lois de probabilité) de perte de puissance ou de non-jugeabilité

1. **Effondrement du glouton déterminantal vers un tri statique (E1 et E2).**
   Dans `O-paires`, le gain marginal à l'étape gloutonne $t$ pour ajouter la paire $p$ est $\Delta_t(p) = \log(w_p^2 \det(I + \Phi_{Y_t}^T \Phi_{Y_t})^{-1}_{p} + \gamma)$. 
   *Condition de perte de puissance :* Si la variance de la loi log-qualité des paires $\text{Var}(\log w_p^2)$ sur la population des paires valides domine la pénalité maximale d'exclusion de strate — précisément, si pour deux paires $p, q$ de la même strate, la probabilité $\mathbb{P}(|\log w_p^2 - \log w_q^2| > \log(1 + (1+2\lambda^2)/\gamma))$ dépasse $1 - 1/k$ —, alors l'ordre glouton est déterminé à 100 % par la diagonale $w_p$. Le DPP dégénère en un tri statique (reproduisant exactement le défaut de la pièce B § 3 où la corrélation de rang avec $q$ est de 0,977, RAPPORTÉ). Dans ce régime, l'expérience E2 (glouton contre tirage indépendant $\propto w_p$) perd sa puissance à isoler l'effet du volume déterminantal, car le déterminant est algébriquement inactif.

2. **Dégénérescence de la troncature à 25 % (E1 et E4).**
   Soit $N$ la taille du vivier ($N=40$ dans la pièce B, RAPPORTÉ) et $p_{\text{moyeu}} = 0,25$ la probabilité marginale d'apparition d'un moyeu. Le nombre d'occurrences observées suit une loi binomiale $\mathcal{B}(N, p_{\text{moyeu}})$.
   *Condition de perte de puissance :* La probabilité qu'un vrai moyeu ait une fréquence empirique $\hat{p} \le 0,25$ vaut $\mathbb{P}(\mathcal{B}(40, 0{,}25) \le 10) \approx 0,584$ (calcul exact sur les paramètres de B). La garde de A laisse donc passer les vrais moyeux plus d'une fois sur deux. Inversement, si la loi de fréquence des vrais concepts suit une loi de Zipf-Mandelbrot de paramètre $s < 1$, les concepts structurants mais fréquents ($\hat{p} > 0,25$) sont purgés avec probabilité $\to 1$ quand $N \to \infty$, rendant la similarité $c_{ij}$ aveugle aux opérateurs fondamentaux.

3. **Non-jugeabilité du test de séparabilité linéaire (E4).**
   A teste si la représentation capte le concept et non le domaine par un « classifieur linéaire "domaine à partir du vecteur de concepts" $\le \text{hasard} + 0,10$ » (RAPPORTÉ, A § b-E4).
   *Condition de non-jugeabilité :* Soit $\mathbb{P}(K \mid D)$ la loi conditionnelle des concepts sachant le domaine. Si l'information mutuelle $I(K ; D) > 0$ mais que les supports des domaines dans l'espace des concepts sont non linéairement séparables (par exemple, chaque domaine utilise des *paires* exclusives d'opérateurs — un problème de type OU-exclusif — tout en ayant les mêmes fréquences marginales d'opérateurs simples $\mathbb{E}[k \mid D=d] = \mathbb{E}[k]$), alors tout classifieur linéaire aura une exactitude égale au hasard ($1/8$), validant H_A, alors même que le produit scalaire $c_{ij} = \langle k_i, k_j \rangle$ sur les paires reconstruira parfaitement les frontières de domaine. Le critère est aveugle aux dépendances d'ordre 2 qui sont pourtant celles que le noyau quadratique exploite.

4. **Sous-puissance statistique radicale sur la course 2 (E5).**
   Dans la pièce A (`recombiner`, VÉRIFIÉ), `max_paires = 3` par génération ; dans la pièce B (§ 1, RAPPORTÉ), le budget est de $K = 12$ paires tirées par bras. A exige dans E5 un gain d'au moins $+10$ points sur la part de filles promues (RAPPORTÉ, A § b-E5).
   *Condition de non-jugeabilité :* Sur deux lois binomiales indépendantes $\mathcal{B}(12, p_1)$ et $\mathcal{B}(12, p_2)$ avec $p_1 = 0,20$ et $p_2 = 0,30$ (écart de $+10$ points, illustratif), l'erreur type de la différence des proportions est $\sqrt{p_1(1-p_1)/12 + p_2(1-p_2)/12} \approx 0,175$ (17,5 points). La puissance d'un test au seuil $\alpha = 0,05$ pour détecter $+10$ points avec $K=12$ est inférieure à $15\%$ (calcul illustratif). E5 est statistiquement non jugeable à ce budget.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Témoin d'ablation « Stratifié + filtre de moyeux à 25 % ».** 
   Puisque A introduit une coupure dure des étiquettes fréquentes ($> 25\%$), l'absence d'un bras témoin appliquant cette même coupure au tirage stratifié standard et à `b_eloigne` est fatale : tout le gain de `O-paires` pourrait provenir de cette seule ligne de prétraitement.
2. **Contrôle de dépendance non linéaire (quadratique) dans E4.**
   Tester si la matrice de Gram des concepts $C_{ij} = \langle k_i, k_j \rangle$ prédit la matrice d'adjacence des domaines $D_{ij}$ (test de Mantel ou régression sur les paires), et non pas seulement si le vecteur individuel $k_i$ prédit linéairement $d_i$. Sans ce contrôle sur les paires, une fuite de domaine d'ordre 2 passe inaperçue.
3. **Contrôle d'invariance par re-paramétrisation monotone de la qualité $q$.**
   Remplacer $q$ par un classement par rang ou par $q^\eta$ dans le témoin `noyau_corrige` (v6.3) avant de conclure que le passage aux paires est indispensable (dans E3, A varie $\tau$ dans $\exp(-s_{ij}/\tau)$ mais laisse $q^2$ varier d'un facteur 9, ce qui continue d'écraser le déterminant).

---

## Sur la proposition B

### (a) Défauts de méthode : variables confondantes, vérités par construction, fuites

1. **Inversion de signe dans le noyau de lot $K$ de O3 (répulsion de fiches au lieu de répulsion de strates).**
   La proposition B définit son noyau de diversité sur les paires par $K_{(ij),(kl)} = \frac{1}{2}[S_{ik} S_{jl} + S_{il} S_{jk}] + \gamma \delta$, où $S$ est le Gram linéaire des domaines $S_{ik} = \langle d_i, d_k \rangle$, et affirme que cela « pénalise les lots dont les paires relient les mêmes couples de domaines » (RAPPORTÉ, proposition B § 1.3).
   *Défaut :* C'est mathématiquement inexact quant à l'échelle de la pénalité, ce qui crée une **variable confondante** entre « diversité de strates » et « non-chevauchement des fiches ». 
   Vérifions-le sur les chiffres de la pièce B (§ 5, RAPPORTÉ) : le cosinus de deux articles du *même* domaine vaut $S_{ik} = 0,54$ (et $S_{ii} = 1$). 
   - Si deux paires $(i,j)$ et $(k,l)$ sont dans la **même strate** (mêmes domaines respectifs, mais articles distincts) et relient des domaines éloignés ($S_{il} = S_{jk} = 0,03$), alors $K_{(ij),(kl)} = \frac{1}{2}(0,54 \times 0,54 + 0,03 \times 0,03) \approx 0,146$. Dans le déterminant $2 \times 2$, la pénalité relative est $K_{(ij),(kl)}^2 / K_{pp}^2 \approx 0,146^2 / (0,50)^2 \approx 8,5\%$.
   - Si en revanche deux paires **partagent un article** ($i=k$) mais vont vers deux domaines éloignés différents ($S_{jl} = 0,03$, donc **deux strates distinctes**), alors $K_{(ij),(il)} = \frac{1}{2}(1 \times 0,03 + 0,03 \times 0,03) \approx 0,015$. Mais si elles vont vers le même domaine ($S_{jl} = 0,54$), $K_{(ij),(il)} \approx 0,27$ (pénalité $\approx 29\%$).
   Comme dans la pièce B (§ 3), une pénalité de $8,5\%$ entre paires de la même strate est **écrasée** par la variance du score diagonal $r_p^2 = q_i q_j (1-D_{ij}^2)^\beta c_{ij}^{2\alpha}$ qui varie d'un facteur $> 9$. Le noyau $K$ de B ne stratifie donc **pas** les couples de domaines : il reproduit exactement l'erreur de la forme corrigée v6.3 à l'étage des paires !

2. **Dégénérescence du test E1 sur les mondes inchangés de la pièce B.**
   B refuse à juste titre une extension tautologique des mondes (S5), mais propose de tester E1 ($Z$ avec $\alpha > 0$ contre $Z_0$ avec $\alpha = 0$ et $O4$) directement sur les « mondes de la pièce B, avec les mêmes graines de construction » (RAPPORTÉ, B § b).
   *Défaut :* Dans les mondes de la pièce B (§ 5, RAPPORTÉ), chaque groupe ne partage qu'un opérateur latent, plus éventuellement le moyeu (présent à 25 %). La grande majorité des paires valides n'ont donc **qu'une seule** étiquette d'opérateur en commun. Or, sur un vecteur $k_i$ normalisé, si deux fiches ne partagent qu'une étiquette, leur cosinus $C_{ij}$ se réduit au produit de leurs poids IDF sur cette unique étiquette divisé par les normes — ce que capture déjà le bras $O4 = \text{b\_eloigne} \oplus \text{rareté}$. Sur ces mondes non modifiés, H_B (« l'éloignement de domaine et la rareté expliquent tout ») risque d'être **vraie par construction du générateur**, car le générateur de la pièce B ne contient pas de structure conceptuelle multi-opérateurs à capter.

3. **Fuite de domaine dans l'étiqueteur hors boucle R2 (S6 et § 2).**
   B recommande d'utiliser un modèle tiers hors boucle (R2) comme seule entrée du tirage (RAPPORTÉ, B § 2). Contrairement à A, B ne précise **pas** que le texte soumis à R2 est caviardé de ses marqueurs de domaine ou de son axe. 
   *Défaut :* Si R2 lit la fiche entière, ses représentations internes conditionnent l'extraction des concepts sur le domaine identifié (biais de cooccurrence du modèle de langage). Il y a alors **fuite** de l'espace des domaines vers l'espace des concepts avant le scellement.

4. **Confusion dans le bras (a') « code tel quel ».**
   En S1, B observe justement que la pièce A trie les paires issues des $k=4$ articles par `(s[i][j], -q_i*q_j, cle)` et garde `max_paires = 3`, alors que la pièce B tire $k=4$ paires par génération (VÉRIFIÉ sur A, RAPPORTÉ sur B). 
   *Défaut :* Si l'on ajoute (a') « code tel quel » dans le banc de test de B sans aligner le budget de paires tirées ($3 \times 3 = 9$ paires dans le code de A contre $4 \times 3 = 12$ paires dans B), le dénominateur de la précision et le budget du rappel changent : la variable « budget de tirage » confond la comparaison.

### (b) Conditions mesurables (lois de probabilité) de perte de puissance ou de non-jugeabilité

1. **Inertie déterminantale du noyau de Kronecker symétrisé $K$ (O3, E1).**
   Pour deux paires $p=(i,j)$ et $q=(k,l)$, le déterminant $2 \times 2$ de $L$ vaut $r_p^2 r_q^2 (K_{pp}K_{qq} - K_{pq}^2)$. 
   *Condition de perte de puissance :* Soit $\mu_S = \mathbb{E}[S_{ik} \mid \text{même domaine}]$ ($\mu_S = 0,54$ dans B). Pour des paires de domaines éloignés ($D_{ij} \approx 0,03$), $K_{pp} = \frac{1}{2}(1 + D_{ij}^2) + \gamma \approx 0,5 + \gamma$, et pour $p, q$ dans la même strate mais sans fiche commune, $K_{pq} \approx \frac{1}{2}\mu_S^2$. Le facteur de répulsion de strate vaut $1 - K_{pq}^2 / K_{pp}^2 \approx 1 - \mu_S^4$. 
   Dès que la distribution du score de paire $r_p^2$ vérifie $\text{Quantile}_{1-1/m}(r_p^2) / \text{Quantile}_{1-k/m}(r_p^2) > (1 - \mu_S^4)^{-1}$ (or $(1 - 0,54^4)^{-1} \approx 1,093$, soit un écart de $9,3\%$ seulement !), le glouton choisit systématiquement plusieurs paires dans la même strate dès qu'elles ont un score $r_p^2$ supérieur de $10\%$. Le noyau $K$ perd toute puissance de stratification dès que $\mu_S < 0,8$.

2. **Aveuglement du classifieur au centroïde le plus proche dans E4.**
   B mesure la fuite de domaine par « la précision d'un classifieur au centroïde le plus proche, qui prédit le domaine à partir du vecteur de concepts » et par le « ratio de similarité conceptuelle intra-domaine / inter-domaine » (RAPPORTÉ, B § 2).
   *Condition de non-jugeabilité :* Supposons que chaque domaine $d$ soit un mélange multimodal équiprobable de deux sous-thèmes opposés dans l'espace des concepts : $k \mid d \sim \frac{1}{2}\mathcal{N}(\mu_d, \Sigma) + \frac{1}{2}\mathcal{N}(-\mu_d, \Sigma)$ sur la sphère, avec $\mu_d \perp \mu_{d'}$. Alors :
   - Le centroïde théorique de chaque domaine est nul : $\mathbb{E}[k \mid d] = 0$. Le classifieur au centroïde le plus proche plafonne au niveau du hasard (fuite mesurée $\approx 0$).
   - L'espérance du produit scalaire intra-domaine vaut $\mathbb{E}[\langle k_i, k_j \rangle \mid d_i = d_j] = \frac{1}{2}\|\mu_d\|^2 - \frac{1}{2}\|\mu_d\|^2 = 0$, égale à l'espérance inter-domaine. Le ratio intra/inter vaut $1$.
   Pourtant, la probabilité qu'une paire intra-domaine ait une forte similarité $\mathbb{P}(\langle k_i, k_j \rangle > \tau \mid d_i = d_j)$ est proche de $1/2$, alors qu'elle est quasi nulle inter-domaine ! Les deux critères de B valident H_A (absence de fuite) alors que la queue supérieure de la distribution de $C_{ij}$ — la seule que le tirage glouton sélectionne — est composée à $100\%$ de paires du même domaine.

3. **Erreur de calcul d'échantillon pour le test d'équivalence TOST dans E1.**
   B calcule $N \approx 620$ (arrondi à 800 mondes) en utilisant la formule d'un test de supériorité unilatéral ($\alpha = 2,5\%$, puissance $90\%$, erreur type $\sigma/\sqrt{N}$ où $\sigma \approx 0,77 \times \sqrt{400} = 15,4$ points, RAPPORTÉ B § b-Puissance), et affirme : « Le test d'équivalence à $\pm 2$ donne un nombre voisin. »
   *Condition de perte de puissance :* C'est inexact pour une loi normale d'écart-type $\sigma = 15,4$ lorsque le vrai écart est nul ($\Delta = 0$). Pour un test TOST bilatéral aux bornes $\pm \delta$ avec $\delta = 2$ au seuil $\alpha = 0,025$ et puissance $1-\beta = 0,90$, la fonction de puissance à $\Delta = 0$ exige $N = (z_{1-\alpha} + z_{1-\beta/2})^2 (\sigma / \delta)^2 = (1,96 + 1,645)^2 \times (15,4 / 2)^2 \approx 13,0 \times 59,29 \approx 771$ mondes si la vraie différence est exactement $0,00$ ; mais dès que la vraie différence résiduelle entre $Z$ et $O4$ est de $\Delta = 0,5$ point (bruit de discrétisation), il faut $N \ge (1,96 + 1,28)^2 \times (15,4 / 1,5)^2 \approx 1\,105$ mondes. À 800 mondes, dès que $|\Delta| \ge 0,6$ point, la puissance du TOST tombe sous $80\%$ et l'expérience conclut « non concluant » par manque de puissance.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de stratification effective du noyau $K$ (mesure de concentration des strates).**
   En raison du défaut (a.1) et de la condition (b.1), il est fatal de ne pas enregistrer la métrique « strates distinctes par paire » (qui vaut $0,998$ pour le stratifié et $0,707$ pour la forme corrigée dans la pièce B § 1, RAPPORTÉ) sur le bras $Z_0$ ($\alpha=0$). Si $Z_0$ tombe sous $0,95$ de strates distinctes, le noyau de Kronecker $K$ de B est réfuté comme substitut au tirage stratifié avant même de regarder la précision.
2. **Contrôle des quantiles extrêmes (queue supérieure) dans E4.**
   Puisque le tirage ne retient que les $k$ paires de plus haut score, l'absence d'un contrôle mesurant la proportion de paires de même domaine (ou de même champ) *parmi le top-$k\%$ des valeurs de $C_{ij}$* (et non en moyenne ou par centroïde) est fatale : une fuite de domaine logée dans la variance conditionnelle de $C_{ij}$ invaliderait tout le tirage tout en passant le test E4 de B.
3. **Contrôle d'aveuglement au domaine pour l'étiqueteur R2.**
   Avant de sceller R2, passer un jeu de fiches jumelles où le vocabulaire de domaine a été substitué (par exemple, termes de finance remplacés par termes de physique à structure mathématique identique). Si la similarité $C_{ij}$ entre les jumelles tombe sous un seuil élevé (par exemple $0,80$, illustratif), R2 lit le domaine et non le concept, ce qui est fatal à la recommandation de la section 2.

FIN-DE-CELLULE