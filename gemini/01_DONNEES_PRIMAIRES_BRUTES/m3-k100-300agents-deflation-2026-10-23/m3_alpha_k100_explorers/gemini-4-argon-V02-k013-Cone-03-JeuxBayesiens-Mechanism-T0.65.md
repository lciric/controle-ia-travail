BASSIN_MATH: Mécanisme-VCG-PeerTruthSerum-BergemannMorris (VCG-PTS-BM)
LOI_PROPOSEE: L'allocation du budget API est régie par une enchère dynamique de Vickrey-Clarke-Groves (VCG) couplée à un Peer Truth Serum (PTS) évalué par `jev-1.14.0`, sous contrainte d'obéissance bayésienne de Bergemann-Morris (BM).

1. **Loi d'apprentissage & d'auto-organisation hors-poids de l'essaim**
Le graphe bibliographique $G=(V,E)$ est exploré gratuitement par un essaim d'éclaireurs `jev-1.14.0` qui extraient des paires de nœuds $(u,v)$ et génèrent un espace de signaux $\Sigma$ définissant une structure d'information de Bergemann-Morris $(\Sigma, \pi : \Theta \to \Delta(\Sigma))$, où $\Theta$ est l'état latent de validité mécanique sur Llama-3.1-8B/70B. Les agents génératifs $i \in \{1..N\}$ (20$ Gemini = éclaireurs bayésiens rapides ; 100$ Claude = synthétiseurs d'intervention causale) ont un type privé $\theta_i = \text{KL}(P(\Theta | s_i) \parallel P(\Theta))$ mesuré par `jev-1.14.0`. L'allocation des appels API $a \in \{0,1\}^N$ sous contrainte budgétaire $B=120\$$ maximise le bien-être informationnel via un mécanisme VCG dynamique. Le transfert de budget virtuel (qui module le contexte système et la température hors-poids) est :
$$t_i(\hat{\theta}) = \max_{a} \sum_{j \neq i} \hat{\theta}_j(a) - \sum_{j \neq i} \hat{\theta}_j(a^*) + \alpha \cdot \text{PTS}_i(x_i, y_{\text{jev}})$$
où le score Peer Truth Serum $\text{PTS}_i = \frac{\mathbb{I}(x_i = y_{\text{jev}})}{P_0(y_{\text{jev}})} - 1$ utilise l'évaluation hors-ligne illimitée de `jev-1.14.0` ($y_{\text{jev}}$) et la distribution a priori du graphe $P_0$, rendant la révélation d'associations rares ($P_0 \ll 1$) mais structurellement vraies strictement dominante.

2. **Fonction objectif anti-vernis**
L'utilité sociale $W(u,v, H_A, H_B)$ soumise à la condition d'obéissance de Bergemann-Morris ($\sum_{\theta, s_{-i}} \pi(s|\theta) [U_i(H_A, \theta) - U_i(H_B, \theta)] \ge 0$) s'écrit :
$$J(u,v) = d_{\text{eff}}(u,v) \cdot \left(1 - \cos(\vec{e}_u^{\text{jev}}, \vec{e}_v^{\text{jev}})\right) \cdot \mathcal{J
