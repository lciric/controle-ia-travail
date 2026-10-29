BASSIN_MATH: Réduction-Bayésienne-Hebbienne-Dirichlet (RBHD)
LOI_PROPOSEE: Topologie = matrice Dirichlet $a_{ij}$ (confiance i→j). Choix de politique $\pi^*=\arg\min_\pi G(\pi)$, $G=\underbrace{D_{KL}[q(o|\pi)\|p(o)]}_{\text{risque}}+\underbrace{\mathbb{E}_q[H(o|s)]}_{\text{ambiguïté}}-\underbrace{I(s;o|\pi)}_{\text{gain épistémique}}$ ; apprentissage hors-poids : $\Delta a_{ij}=\eta\,[\,G_{\text{prior}}-G_{\text{post}}\,]\,\mathbb{1}(i\!\to\!j)$ ; élagage par réduction bayésienne de modèle : supprimer l'arête si $\Delta F_{\text{réduit}}=\ln\frac{p(o|m_{-ij})}{p(o|m)}>0$.

**1. Auto-organisation.** Chaque arête de communication est un pa
