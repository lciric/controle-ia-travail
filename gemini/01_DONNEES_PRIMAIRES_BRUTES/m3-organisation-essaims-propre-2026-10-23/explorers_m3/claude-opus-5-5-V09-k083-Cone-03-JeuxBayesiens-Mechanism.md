BASSIN_MATH: Taxe de Clarke Informationnelle à Pivot Bregman (TCIP-B)

LOI_PROPOSEE: $\tau_i=S\big(q_{N},\omega\big)-S\big(q_{N\setminus i},\omega\big)-c_i$. On spawne un agent $k$ ssi $\mathbb{E}_{\mu}[\tau_k]>0$, et l'arête $i\to j$ survit ssi $\mathbb{E}[S(q_j\mid m_i)-S(q_j)]>p\cdot\text{tokens}_{ij}$. Ici $S$ est le log-score propre, $q_N$ l'agrégat bayésien de l'essaim et $\omega$ une vérité vérifiable différée.

**1. Mécanisme d'auto-organisation hors-poids**

Chaque agent émet des croyances probabilistes sur des propositions atomiques, par exemple « l'article X existe et soutient Y ». Il est rémunéré par un paiement pivot de Groves-Clarke : sa contribution marginale au score de l'agrégat, calculée par leave-one-out.

- **Coût des clones.** Deux clones de même famille de poids (H4') ont des signaux corrélés. Retirer l'un ne coûte presque rien, donc $\tau_i\approx 0$ moins le coût : le mécanisme facture automatiquement la monoculture.
- **Monoculture ou chimère.** La chimère n'est retenue que si son information conditionnelle, de type Blackwell, couvre son prix. Ce prix est de $p_{Claude}=1/100$ et $p_{Gemini}=1/20$ par USD de budget normalisé.
- **Explorateur ou démolisseur.** Un explorateur est spawné quand la valeur pivot espérée de nouvelles propositions dépasse celle de la réfutation. Un démolisseur Red-Team est spawné quand l'entropie de $q_N$ reste haute sur des propositions déjà émises.
- **Apprentissage sans réentraînement.** L'essaim met à jour un prior bayésien $\mu$ (Beta-Bernoulli) sur les $\tau$ de chaque couple (rôle, famille, prompt). La topologie mute par échantillonnage de Thompson sur ces postérieurs.
- **Dérive de consigne (H9).** Tout contrat de délégation embarque le hash de la consigne racine. Le sous-agent n'est scoré que sur des propositions dérivées de cette racine.

**2. Fonction objectif et anti-Goodhart**

$$R=\sum_{t}\Big[\log q_{N}(\omega_t)-\lambda\,\mathrm{KL}\big(q_N\,\|\,q_{\text{jev}}\big)\mathbb{1}_{\text{audit}}\Big]-\beta\sum_i c_i$$

- **Vérité terrain externe.** $\omega_t$ est résolu par Crossref, arXiv et Semantic Scholar (existence, DOI, citation effective), et non par un juge.
- **Rôle limité de jev.** jev-1.14.0 sert seulement de sonde aléatoire cachée, sur environ 20 % des items tirés après coup.
- **Effet anti-Goodhart.** Un score propre rend la vraie croyance optimale, et la récitation de la mémoire paramétrique d'un article inexistant est pénalisée en $\log$.

**3. Duel décisif $H_A\perp H_B$ (plan factoriel 2×2)**

Le budget est constant à 120 USD par bras, avec 400 propositions vérifiables pré-enregistrées et 5 graines.

- **Facteur A : taxe pivot activée ou désactivée.** Sans taxe, le paiement est le score individuel.
- **Facteur B : topologie adaptative ou fixe.** La topologie fixe est une étoile de 6 agents i.i.d.
- **Contrôle négatif.** Les $\tau_i$ sont permutés aléatoirement entre agents, à budget égal. On attend une performance égale à l'essaim i.i.d.
- **$H_A$ (la taxe pivot améliore la qualité).** Elle augmente le log-score et réduit le taux de citations hallucinées (test de Wilcoxon apparié, $\alpha=0{,}01$).
- **$H_B$ (l'adaptation améliore l'efficience).** Elle augmente le score par USD.
- **Orthogonalité.** Elle est testée par une interaction ANOVA non significative.
- **Critère de réfutation.** TCIP-B est réfuté si le bras (A on, B on) ne bat pas le bras fixe et le contrôle permuté.
