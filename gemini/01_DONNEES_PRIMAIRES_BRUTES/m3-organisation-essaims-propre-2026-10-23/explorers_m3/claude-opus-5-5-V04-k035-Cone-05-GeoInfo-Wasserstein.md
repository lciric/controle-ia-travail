BASSIN_MATH: Volume de Fisher Transporté D-Optimal (VFT-D)

LOI_PROPOSEE: $w_{t+1}=\Pi_\Delta\!\left[w_t\odot\exp\!\big(\eta\,G(w_t)^{-1}\nabla_w \mathcal{R}\big)\right]$, avec $\mathcal{R}(w)=\frac{\log\det\big(I_0+\sum_a w_a \hat I_a\big)}{c(w)}-\lambda\,\max_{a} W_1^{\mathcal{G}}(\mu_a,\mu_{\text{racine}})$ et $G(w)=\mathrm{diag}(1/w)$, la métrique de Fisher-Rao du simplexe.

**1. Auto-organisation hors-poids**

Chaque agent $a$ (famille, rôle, consigne) est une « sonde » d'un paramètre d'hypothèse $\theta$. Sa matrice de Fisher empirique est $\hat I_a=\mathbb{E}[s_a s_a^\top]$, où $s_a$ est la sensibilité des scores `jev-1.14.0` de ses sorties aux perturbations de $\theta$. Ce calcul est gratuit.

- **Corrélation H4'.** Deux agents de même famille ont des $\hat I_a$ quasi colinéaires. Le terme $\log\det$ n'ajoute alors presque rien, et le budget migre donc mécaniquement vers la chimère. La monoculture n'est conservée que si son volume par dollar domine.
- **Spawn d'un explorateur.** On en crée un lorsque $\lambda_{\min}(I)<\tau$. Il est dirigé selon le vecteur propre associé, c'est-à-dire la direction épistémique non sondée.
- **Spawn d'un démolisseur Red-Team.** On en crée un lorsque $\lambda_{\max}$ croît plus vite que l'accord avec les ancres bibliographiques, signe d'une confiance suspecte.
- **Topologie.** L'arête $a\to b$ existe si $\mathrm{tr}(\hat I_a^{-1}\hat I_b)$ est grand, c'est-à-dire si $b$ complète $a$.

**2. Objectif et anti-Goodhart**

$$\mathcal{R}=\frac{\log\det I_{\text{held}}(w)}{c(w)}-\lambda\,W_1^{\mathcal{G}}-\beta\,\rho_{\text{mém}}-\gamma\cos\!\big(\tilde\nabla\mathcal{R},\nabla\,\text{jev}\big)$$

- **Dérive H9.** $W_1^{\mathcal{G}}$ est le transport optimal, sur le graphe Semantic Scholar/Crossref, entre la distribution de citations d'une sous-consigne déléguée et celle de la racine.
- **Récitation.** $\rho_{\text{mém}}$ est la fraction d'affirmations sans chemin vérifiable dans le graphe arXiv.
- **Goodhart.** $I_{\text{held}}$ est estimée sur une partition de juges tenue secrète et tournante. Le dernier terme pénalise tout gradient naturel aligné sur le juge lui-même.
- **Coût.** $c(w)$ facture séparément les budgets Claude (100 USD) et Gemini (20 USD), sous forme de contraintes de Lagrange.

**3. Duel décisif ($H_A \perp H_B$)**

À budget identique de 120 USD, sur 60 questions `controle-ia` dont les réponses sont vérifiées a posteriori par des experts aveugles, on compare quatre bras :

- **A, VFT-D** : la loi proposée.
- **B, essaim fixe** : même mélange final de familles, topologie figée.
- **C, i.i.d.** : allocation uniforme aléatoire.
- **D, contrôle négatif** : VFT-D avec des matrices $\hat I_a$ permutées entre agents, c'est-à-dire une géométrie détruite.

Les mesures sont les suivantes :

- **Critère principal** : log-score des affirmations validées.
- **Critères secondaires** : corrélation inter-agents des erreurs, et $W_1$ de dérive.

Les hypothèses s'opposent ainsi :

- **$H_A$** : $A>B,C,D$ avec $p<0{,}01$ après correction de Holm, et $D\approx C$. Le gain vient bien de la géométrie de Fisher.
- **$H_B$** : $A\approx D$. Le gain proviendrait de la seule adaptativité, ce qui réfuterait la loi.
