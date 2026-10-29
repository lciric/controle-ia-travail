BASSIN_MATH: ControleImpulsionnel-Snell-Shiryayev-FeynmanKac
LOI_PROPOSEE: L'allocation des appels LLM est un problème de contrôle impulsionnel sur l'enveloppe de Snell du processus de Shiryayev-Roberts gouvernant un essaim de diffusions branchantes de Feynman-Kac évaluées gratuitement par `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
L'essaim d'hypothèses est un système de diffusions branchantes à champ moyen de Feynman-Kac sur le graphe bibliographique gratuit $\mathcal{G}=(V,E)$. Une population d'états non-génératifs $(x_t^i)_{i=1}^N \in V \times V$ évolue par marche aléatoire biaisée. À chaque pas $t$, `jev-1.14.0` calcule sans coût le potentiel de sélection $V(x_t^i) = \log \frac{P_{\text{jev}}(\text{Causal}|x_t^i)}{P_{\text{jev}}(\text{Vernis}|x_t^i)}$. Les particules dupliquent/meurent à taux proportionnel à $\exp(V(x_t^i)) - \frac{1}{N}\sum_j \exp(V(x_t^j))$.
Pour détecter l'émergence d'un pont profond sans gaspiller le budget ($B_{\text{Gemini}}=20\$$, $B_{\text{Claude}}=100\$$), on calcule la statistique de détection de rupture de Shiryayev-Roberts $R_t = \sum_{k=1}^t \prod_{s=k}^t \Lambda_s$, où $\Lambda_s = \frac{1}{N}\sum_{i=1}^N \exp(V(x_s^i))$ est la vraisemblance marginale de Feynman-Kac. L'appel aux LLM est un contrôle impulsionnel $(\tau_m, \xi_m)_{m \ge 1}$ résolvant l'inéquation quasi-variationnelle de Hamilton-Jacobi-Bellman (HJB-QVI) sur l'enveloppe de Snell :
$$ \min \left\{ -\frac{\partial u}{\partial t} - \mathcal{L}_{\text{FK}} u, \; u(R, B) - \max_{\xi \in \{\text{Gem, Cla}\}} [u(\Gamma_\xi(R), B - c_\xi) + \mathcal{J}(x^*)] \right\} = 0 $$
Dès que $R_t$ franchit la frontière libre d'arrêt optimal $\partial \mathcal{C}_{\text{Gem}}$, un agent Gemini ($c_{\text{Gem}}$) hybride les sous-graphes. Si $R_t$ franchit $\partial \mathcal{C}_{\text{Cla}}$, un agent Claude ($c_{\text{Cla}}$) synthétise le protocole expérimental sur Llama-3.1.

2. **Fonction objectif anti-vernis** :
Le gain d'impulsion $\mathcal{J}(u,v)$ maximise le produit de la distance de résistance effective $d_{\Omega}(u,v)$ (temps de commute sur $\mathcal{G}$ pénalisant les raccourcis intra-silos) et de la courb
