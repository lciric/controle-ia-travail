BASSIN_MATH: Normalisation Divisive Carandini-Heeger sur Erreurs de Prédiction (NDCH-EP)

LOI_PROPOSEE: $d_i=\dfrac{\big(G_i\,\pi_i\,\varepsilon_i^2\big)^{n}}{\sigma^{n}+\sum_{j\neq i}W_{ij}\big(G_j\,\pi_j\,\varepsilon_j^2\big)^{n}}$, avec $b_i=B_f\,\dfrac{d_i/c_i}{\sum_{k\in f} d_k/c_k}$ et $W_{ij}=\rho\big(\varepsilon_i,\varepsilon_j\big)_+$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids de l'essaim**

Avant chaque tour, chaque agent $i$ prédit le verdict de `jev-1.14.0` sur sa propre sortie. Son erreur de prédiction est $\varepsilon_i$, et sa précision $\pi_i=1/\widehat{\mathrm{Var}}(\varepsilon_i)$ est mise à jour en ligne. $G_i$ désigne le gain épistémique attendu, c'est-à-dire l'information mutuelle entre la sortie et l'état caché du problème, estimée par `jev`.

Le noyau d'inhibition latérale $W_{ij}$ correspond à la corrélation positive des erreurs. Deux agents de même famille qui se trompent ensemble s'inhibent donc mutuellement, ce qui neutralise $H4'$.

L'apprentissage repose sur la mise à jour de $W$, de $\pi$ et des consignes en mémoire externe, sans aucun gradient sur les poids.

La topologie suit le principe « $i$ parle à $j$ si et seulement si $W_{ij}<\theta$ » : seuls les canaux décorrélés transmettent des messages.

Deux règles gouvernent la création de sous-agents :
- un **explorateur** est créé si $\max_i d_i>\tau_{\uparrow}$, ce qui signale une surprise non expliquée ;
- un **démolisseur Red-Team**, issu d'une autre famille, est créé si $\mathrm{Var}(d)<\tau_{\downarrow}$, ce qui signale un consensus suspect.

L'arbitrage entre monoculture et chimère se fait ainsi : si le bloc intra-famille de $W$ dépasse le bloc inter-familles, l'essaim recrute en chimère, sinon il reste monoculturel.

Le budget $b_i$ est réparti par famille, avec $B_{\text{Claude}}=100$ et $B_{\text{Gemini}}=20$ USD, et chaque agent est pondéré par l'inverse de son coût $c_i$.

**2. Fonction objectif et anti-Goodhart**

$$R=-F+\lambda\sum_i G_i-\beta\,I\big(y;\phi_{\text{jev}}\big)-\gamma\,\mathrm{KL}\big(p_{\text{délégué}}\,\|\,p_{\text{racine}}\big)-\eta\,\mathrm{Rec}$$

- $F=\mathrm{KL}\big(q\,\|\,p\big)-\mathbb{E}_q\big[\ln p(o)\big]$ est l'énergie libre variationnelle.
- $I(y;\phi_{\text{jev}})$ pénalise toute sortie qui exploite les caractéristiques internes du juge (anti-Goodhart).
- Le terme $\mathrm{KL}$ mesure la dérive de consigne entre la consigne déléguée et la consigne racine ($H9$).
- $\mathrm{Rec}$ est la fraction d'affirmations non vérifiables via Crossref, arXiv ou Semantic Scholar, ce qui pénalise la récitation de la mémoire paramétrique.
- Le juge est régulièrement rotaté sur des ensembles de validation cachés.

**3. Duel décisif de validation M3 ($H_A \perp H_B$)**

Le protocole compare quatre bras à budget identique de 120 USD, sur $N=60$ tâches préenregistrées :
- **A** : NDCH-EP complet ;
- **B** : essaim à topologie fixe ;
- **C** : allocation i.i.d. uniforme ;
- **D** (contrôle négatif) : NDCH-EP avec le noyau $W$ permuté aléatoirement.

Le critère principal est le nombre d'affirmations vérifiées et non triviales par dollar, évalué sur un juge tenu à l'écart.

Les deux hypothèses sont formulées comme suit :
- $H_A$ : A > D, ce qui montre que l'inhibition par corrélation réelle est causale ;
- $H_B$ : A > max(B, C), ce qui montre que l'auto-organisation bat les essaims fixe et i.i.d.

L'analyse utilise un test de permutation apparié avec correction de Holm à α = 0,05. La falsification est acquise si D ≈ A ou si C ≥ A.
