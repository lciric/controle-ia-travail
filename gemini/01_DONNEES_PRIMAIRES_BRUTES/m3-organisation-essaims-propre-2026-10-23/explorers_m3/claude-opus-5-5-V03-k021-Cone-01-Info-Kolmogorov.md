BASSIN_MATH: Coude de Structure Préquentiel de Kolmogorov (CSP-K)

LOI_PROPOSEE: $S^*_t=\arg\min_{S}\big[\,L(S)+L_{\text{preq}}(D_{>t}\mid S)\,\big]$ sous $\sum_{i\in S}c_i\le B$, avec $b_i\propto\Delta_i/c_i$ et $\Delta_i=L_{\text{preq}}(D_{>t}\mid S\setminus i)-L_{\text{preq}}(D_{>t}\mid S)$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids de l'essaim**

L'essaim est traité comme un modèle en deux parties. La topologie $S$ (agents, arêtes, consignes) constitue la partie « structure » $L(S)$. Les données futures $D_{>t}$ sont des articles arXiv postérieurs à la coupure, datés par Crossref, et elles forment la partie « bruit » $L_{\text{preq}}$. Ces données sont codées préquentiellement par les log-probabilités de `jev-1.14.0`, qui sert de compresseur gratuit.

L'essaim suit la fonction de structure $h(\alpha)$ et s'arrête à son coude.

- **Explorateur.** Si le déficit d'aléa $\delta=L_{\text{preq}}-\hat K$ reste élevé, une structure manque encore. On spawne alors un explorateur.
- **Démolisseur Red-Team.** Si $L(S)$ croît sans baisse de $L_{\text{preq}}$, l'essaim sur-ajuste. On spawne alors un démolisseur chargé d'élaguer les agents dont $\Delta_i\le0$.
- **Arbitrage monoculture/chimère.** On calcule la distance de compression normalisée $\mathrm{NCD}(y_a,y_b)$ entre les sorties des agents. Si elle est inférieure à $\tau$ (corrélation de type H4'), le second agent est remplacé par une famille de poids différente, Gemini ou Claude.
- **Dérive de consigne (H9).** Une arête de délégation est coupée si $K(c_k\mid c_0)/K(c_0)>\rho$.
- **Récitation de la mémoire paramétrique.** Une sortie est rejetée si $C(y\mid\text{corpus S2})/C(y)<\epsilon$, c'est-à-dire si elle se compresse presque entièrement par la littérature existante.

**2. Fonction objectif et anti-Goodhart**

$$R_t=-\Big[L(S)+\sum_{x\in D_{>t}}-\log p_S(x\mid x_{<})\Big]-\lambda\,\mathbb{1}[\text{récit.}]-\mu\,\overline{\mathrm{NCD}^{-1}}$$

Trois propriétés protègent ce signal contre la loi de Goodhart :

- Le juge ne voit jamais $D_{>t}$ avant le scellement des prédictions, ce qui en fait un signal préquentiel.
- Le score est une longueur de code, qu'il est impossible de flatter rhétoriquement.
- On applique une rotation aléatoire des segments de $D_{>t}$ à chaque époque.

**3. Duel décisif de validation M3 ($H_A\perp H_B$)**

Le budget est identique pour tous les bras : 100 USD Claude et 20 USD Gemini. Quatre bras sont comparés :

- (a) CSP-K ;
- (b) essaim fixe, hiérarchique ;
- (c) essaim i.i.d., à topologie aléatoire de même taille moyenne ;
- (d) contrôle négatif : CSP-K avec des $\Delta_i$ permutés aléatoirement.

Le protocole repose sur 20 graines et 200 articles scellés.

- **$H_A$ :** $L_{\text{preq}}(a)<\min(b,c)$ d'au moins 5 % (bootstrap, $p<0{,}01$).
- **$H_B$ :** $L_{\text{preq}}(d)\approx L_{\text{preq}}(c)$. Ce résultat prouve que le gain provient de l'information réelle contenue dans $\Delta_i$, et non de l'adaptativité seule.

La réfutation est pré-enregistrée : si (d) bat (b), le mécanisme est invalidé.
