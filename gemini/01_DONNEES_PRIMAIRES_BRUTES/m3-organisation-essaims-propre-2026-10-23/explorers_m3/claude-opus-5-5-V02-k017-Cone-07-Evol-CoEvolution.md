BASSIN_MATH: Seuil Kimura-Eigen de Parenté (SKEP)
LOI_PROPOSEE: $x_g^{t+1}=\sum_{h}x_h^{t}W_hQ_{hg}/\bar{W}_t$ ; $k_t=\lceil(1-\bar{r}_t)/(s_t-\bar{r}_t)\rceil$ (chimère ssi $s_t\le\rho_{CC}$) ; $\ell{d}<\ln\sigma/(-\ln{q})$ avec $m=\lceil{L}/\ell\rceil$ sous-tâches ; $T=\min\{t:\mathrm{Cov}_t(W,\Phi)+\mathbb{E}_t[W\Delta\Phi]\le\kappa\bar{W}_t\}$.

1. **Mécanisme d'Auto-Organisation (Essaim + Collisionneur Adaptatif)**

Chaque agent est un génotype $g=(e,\pi,\gamma)$, défini par son espèce, son prompt-rôle et sa cellule MAP-Elites (sous-tâche×source). L'apprentissage, sans toucher aux poids, suit un réplicateur-mutateur d'Eigen : $Q$ mute les prompts, les rôles et la topologie, et recombine entre espèces. Les élites sont héritées en contexte et les dollars suivent $x$ sous les contraintes $(k_t,\varphi_t)$.

**Parenté (H4').** $r_{ij}$, la corrélation des erreurs vérifiées par graphe, fixe $N_e=k/(1+(k-1)\bar{r})$. La sélection bat la dérive (Kimura-Moran) ssi $N_es_t\ge1$, où $s_t=W_{\max}/\bar{W}-1$, d'où $k_t$.

**Monoculture ou chimère.** Comme $N_e^{\mathrm{mono}}<1/\rho_{CC}$, la chimère s'impose ssi $s_t\le\rho_{CC}$. Sa fraction Gemini vaut $\varphi_t=\min\{\varphi:\bar{r}(\varphi)<s_t\}$, avec $\bar{r}(\varphi)=(1-\varphi)^2\rho_{CC}+2\varphi(1-\varphi)\rho_{CG}+\varphi^2\rho_{GG}$. Sans solution, la branche quasi-neutre est abandonnée. Gemini ne sert qu'aux chimères et à la prédation.

**Prédation Reine Rouge (allèles appariés).** Le critique $p$ attaque l'hôte $h$ avec l'intensité $a_{ph}\propto{x_h}(1-r_{ph})$, ce qui crée une sélection fréquence-dépendante négative contre la fixation. Il n'est payé que pour des réfutations vérifiées.

**Division (H9).** La consigne $I_0$ est figée en $L$ contraintes. Une sous-tâche portant $\ell$ de ces contraintes survit à $d$ délégations ssi $\sigma{q}^{\ell{d}}>1$, où $q$ est la fidélité par contrainte et $\sigma$ la supériorité des copies fidèles. Au-delà, $I_0$ est réinjectée verbatim (rétromutation).

**Tours.** $T$ survient quand la sélection de Price ne couvre plus la charge mutationnelle (dérive H9) et le coût $\kappa$.

2. **Fonction Objectif & Anti-Goodhart**

$w(y)=\mathbf{1}[V\ge1]\,(V-\beta{F}+\eta_t[\Delta_J]_{+}+\nu\mathcal{N})-c(y)$, avec $W=\exp(w/\epsilon)$, $\epsilon$ le bruit de mesure et $\Phi=V-\beta{F}$ le trait vérifié.

$V$ compte les assertions ancrées par un identifiant DOI/arXiv/S2 récupéré en session, à ≤2 sauts des articles-graines : la récitation paramétrique vaut zéro. $F$ compte les références réfutées ou sans provenance, avec $\beta\ge1$. $\Delta_J=J(y)-\max_{a\in\mathcal{A}}J(a(y))$ porte sur des contrefactuels mécaniques $\mathcal{A}$ (vidage, suppression, permutation d'entités, jargon). Avec $\eta_t=\max\{0,\mathrm{Cov}_t(\Delta_J,V)/\mathrm{Var}_t(\Delta_J)\}$, un `jev-1.14.0` goodhartisé perd sa covariance de Price avec $V$ et s'éteint. $\mathcal{N}$ récompense une cellule MAP-Elites nouvelle ou améliorée. Ainsi $w(\varnothing)=-c(\varnothing)<w(y)$ dès que $\Phi(y)>c(y)-c(\varnothing)$.

3. **Duel Décisif de Validation M3 ($H_A \perp H_B$)**

$H_A$ (SKEP) prédit que l'effet chimère change de signe en $s=\rho_{CC}$ et que la rétention de consigne s'effondre au seuil $\sigma{q}^{\ell{d}}=1$. $H_B$ (capacité lisse) prédit un bonus Gemini constant et une décroissance géométrique sans rupture.

Un tour 0 commun (monoculture Claude, 6 USD) mesure $\hat{s}_0,\hat\rho_{CC}$. Ensuite, 96 tâches `controle-ia`, stratifiées par $S=\mathbf{1}[\hat{s}_0\le\hat\rho_{CC}]$, sont randomisées 1:1 entre M (18 USD Claude) et X (12 USD Claude + 6 USD Gemini). En intention de traiter, crashs et troncatures comptent $\Phi=0$ dans leur bras. Le critère est $\Phi$/USD vérifié par graphe, jev exclu. $H_A$ gagne ssi un test de Gail-Simon confirme $\tau_{S=1}>0\ge\tau_{S=0}$, sinon $H_B$ gagne. En secondaire, $d\in\{1,\dots,6\}$ est randomisé et le BIC oppose régression segmentée et décroissance géométrique. La réserve pour M2/M1 est de 64 USD Claude et 14 USD Gemini.
