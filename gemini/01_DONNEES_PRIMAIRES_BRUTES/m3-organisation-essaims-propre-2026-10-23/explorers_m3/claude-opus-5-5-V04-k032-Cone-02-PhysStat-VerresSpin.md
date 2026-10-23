BASSIN_MATH: Décimation par Survey Propagation sous Chaos de Couplage (DSP-CC)

LOI_PROPOSEE: $\sigma_i^\star=\arg\max_\sigma W_i(\sigma)$ avec $W_i(\sigma)\propto e^{-y\,\Delta E_i(\sigma)}\prod_{a\ni i}(1-\eta_{a\to i}^{\neq\sigma})$. On décime l'agent le plus polarisé, puis on applique la règle de spawn $\Sigma(y^\star)>0\Rightarrow$ Explorateur et $q_{ff}-q_{fg}>\delta\Rightarrow$ Démolisseur chimérique.

**1. Mécanisme d'auto-organisation hors-poids**
- **Modèle.** Les agents $i$ appartiennent aux familles $f\in\{F,O,G\}$ (Fable, Opus, Gemini). Leurs rôles $\sigma_i$ sont des variables, les sous-tâches $a$ sont des contraintes.
- **Couplages.** Les couplages $J_{ij}=-\mathrm{corr}(\epsilon_i,\epsilon_j)$ sont estimés gratuitement par `jev-1.14.0` sur des énoncés témoins, où $\epsilon_i$ désigne l'erreur de l'agent $i$. L'Hamiltonien est $H=-\sum J_{ij}\delta_{\sigma_i\sigma_j}-\sum_i h_i(\sigma_i)+\lambda\sum_i c_i$.
- **Messages.** Les messages de cavité suivent TAP avec réaction d'Onsager : $m_i=\tanh\big(\beta h_i+\beta\sum_j J_{ij}m_j-\beta^2 m_i\sum_j J_{ij}^2(1-m_j^2)\big)$. Le terme d'Onsager retire l'écho de l'agent $i$ renvoyé par ses voisins.
- **Topologie.** Seules les arêtes de survey $\eta_{a\to i}$ non triviales définissent qui parle à qui.
- **Complexité.** La complexité $\Sigma(y)$, logarithme du nombre d'amas, mesure la phase du système :
  - Si $\Sigma>0$ (phase 1RSB clusterisée), on spawne un Explorateur.
  - Si le recouvrement d'erreur intra-famille $q_{ff}$ dépasse le recouvrement inter-famille $q_{fg}$, on est dans un régime de corrélation de type H4'. On spawne alors un Démolisseur Red-Team d'une autre famille, ce qui produit une chimère.
  - Sinon, la monoculture, moins coûteuse, est conservée.
- **Budget.** Le budget suit $\lambda$ et est réajusté pour saturer 100 USD (Claude) et 20 USD (Gemini).
- **Apprentissage sans poids.** L'apprentissage consiste uniquement à mettre à jour $J$, $h$ et la mémoire de surveys.

**2. Objectif et anti-Goodhart**

$$R=\Big[\tfrac{N_{\text{vérif}}}{\$}-\beta\,q_{EA}^{err}-\mu\,(1-m_0)-\nu\,\rho_{\text{récit}}\Big]\cdot\mathbb 1\big[\mathrm{corr}(R_J,R_{\tilde J})>\rho^\star\big]$$

- $N_{\text{vérif}}$ compte les affirmations dont le chemin DOI est vérifié via Semantic Scholar et Crossref.
- $m_0$ est l'aimantation sur la consigne racine (champ externe), mesurée par `jev-1.14.0` après chaque délégation. Ce terme contre la dérive H9.
- $\rho_{\text{récit}}$ est la fraction d'affirmations sans ancrage bibliographique récupéré. Ce terme contre la récitation de la mémoire paramétrique.
- La porte de chaos de couplage contre Goodhart : on perturbe le juge en $\tilde J=J+\xi$ (consignes et graines permutées). Une récompense qui ne survit pas au chaos est annulée.

**3. Duel décisif $H_A\perp H_B$**
- **Hypothèses.** $H_A$ : DSP-CC bat les alternatives. $H_B$ : les gains viennent du seul budget ou du hasard.
- **Bras à budget identique.** Quatre bras disposent chacun de 100 USD Claude et 20 USD Gemini :
  - (i) DSP-CC ;
  - (ii) essaim fixe hiérarchique ;
  - (iii) essaim i.i.d. à rôles tirés au hasard ;
  - (iv) contrôle négatif : DSP-CC avec $J$ permuté aléatoirement, donc calcul identique mais structure détruite.
- **Protocole.** On utilise 60 tâches `controle-ia` pré-enregistrées et un ordre randomisé.
- **Mesures.** On mesure $N_{\text{vérif}}/\$$, $q_{EA}^{err}$ et $m_0$.
- **Test statistique.** On applique un test de permutation apparié avec $\alpha=0{,}01$.
- **Critères de décision.**
  - $H_A$ est validée si (i) dépasse (ii), (iii) et (iv), et si (iv) n'est pas meilleur que (iii).
  - Si (iv) égale (i), la structure de couplage est inutile : la loi est réfutée.
- **Signature de transition de phase.** $\Sigma$ doit s'annuler au point où le gain marginal d'un Explorateur devient nul.
