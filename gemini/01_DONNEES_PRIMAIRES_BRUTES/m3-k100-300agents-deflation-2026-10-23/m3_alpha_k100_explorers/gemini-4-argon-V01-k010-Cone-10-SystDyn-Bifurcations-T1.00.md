BASSIN_MATH: ErgoHystérésis-Lyapunov-Catastrophe
LOI_PROPOSEE: L'essaim évolue sur une variété de contrôle $M$ par dynamique de Langevin hors-équilibre $\dot{\mathbf{x}} = -\nabla V(\mathbf{x}; \mu) + \sqrt{2T(\lambda_1)}\xi(t)$, forçant des bifurcations pli ($\det(\nabla^2 V)=0$) dès que l'exposant de Lyapunov maximal $\lambda_1 \le 0$.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
L'état des $N$ agents $\mathbf{x}_i \in \mathcal{G}_{\text{cit}}$ suit un flot ergodique guidé par `jev-1.14.0` (Coût=0), qui évalue la matrice jacobienne locale $J(\mathbf{x}_i)$ sur le graphe bibliographique. L'exposant de Lyapunov maximal $\lambda_1(t) = \lim_{\tau\to\infty} \frac{1}{\tau} \ln \frac{\|\delta \mathbf{x}(\tau)\|}{\|\delta \mathbf{x}(0)\|}$ mesure la divergence des trajectoires sémantiques.
- **Bifurcation & Hystérésis** : Si $\lambda_1 < 0$ (piège dans un attracteur trivial/monoculture), le paramètre de contrôle $\mu$ (température de prompt et hybridation chimérique) croît jusqu'à la catastrophe pli $\mu_c$, détruisant le bassin d'attraction. Le retour à $\mu < \mu_c$ s'opère avec hystérésis pour stabiliser le nouvel attracteur étrange.
- **Allocation budgétaire (100$ Claude, 20$ Gemini)** : Déclenchée uniquement par condition de transversalité aux points selles ($\lambda_1 > \lambda_{\text{seuil}}$ et $\|\nabla V\|_{jev} \approx 0$). Gemini cartographie la variété instable (20$) ; Claude (100$) synthétise l'homoclinicité inter-silos.

2. **Fonction objectif anti-vernis** :
$$\mathcal{L}(\mathbf{x}_A, \mathbf{x}_B) = d_{\text{erg}}(\mu_A, \mu_B) \cdot |\det[J_{jev}(H_A), J_{jev}(H_B)]| \cdot \Theta(\lambda_1)$$
Où $d_{\text{erg}}$ est la distance de Wasserstein entre les mesures invariantes de Sinai-Ruelle-Bowen (SRB) des silos $A$ et $B$ sur $\mathcal{G}_{\text{cit}}$. Le déterminant mesure l'orthogonalité causale stricte ($H_A \perp H_B$) via les gradients de falsifiabilité extraits par `jev-1.14.0`. $\Theta(\lambda_1)$ annule le score de tout consensus mou ($\lambda_1 \le 0$).

3. **Pont inédit & Duel ($H_A \perp H_B$)** :
- **Pont** : Couplage entre la *synchronisation chaotique d'oscillateurs de Kuramoto à délai* (Yeung & Strogatz, 1999) `(référence à vérifier)` et l'*effondrement soudain
