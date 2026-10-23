BASSIN_MATH: Dualite-Fenchel-Bregman-Kantorovich-Torsion-DuallyFlat (DFBK-TDF)
LOI_PROPOSEE: L'essaim évolue via une descente de miroir de Bregman couplée à une régularisation d'orthogonalité d'Amari sur le fibré des potentiels duals de Kantorovich induits par le classifieur illimité `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Soit le graphe bibliographique $\mathcal{G}=(V,E)$. Le classifieur `jev-1.14.0` projette gratuitement chaque article $v \in V$ dans le simplexe de probabilité $\Delta^d$, munissant $\mathcal{G}$ d'une structure de variété statistique dualement plate $(\mathcal{M}, g^{FR}, \nabla^{(\alpha)}, \nabla^{(-\alpha)})$ avec $\alpha = \pm 1$. Les sous-essaims (Gemini : éclaireurs $\nabla^{(1)}$-exponentiels à 20$ ; Claude : synthétiseurs $\nabla^{(-1)}$-mélange à 100$) optimisent un couple de potentiels de Kantorovich $(\phi, \psi)$ sur $V \times V$ via la loi de mise à jour hors-poids par gradient naturel d'Amari :
$$\theta_{t+1} = \theta_t - \eta \, G_{FR}^{-1}(\theta_t) \nabla_\theta \left[ \sup_{\phi - \psi \le c_\mathcal{G}} \int_V \phi \, d\mu_A + \int_V \psi \, d\mu_B - \epsilon D_\Phi(\mu_A \| \mu_B) \right]$$
où $D_\Phi$ est la divergence de Bregman générée par le potentiel convexe de Shannon évalué par `jev-1.14.0`, et $c_\mathcal{G}$ la distance de plus court chemin sur le graphe de citations. Le budget LLM payant est alloué exclusivement aux arêtes saturant la contrainte duale $\phi(u) - \psi(v) = c_\mathcal{G}(u,v)$ où la torsion de la connexion de Levi-Civita par rapport à $\nabla^{(1)}$ excède un seuil critique $\tau$.

2. **Fonction objectif anti-vernis** :
On maximise le produit de la distance de Kantorovich-Rubinstein inter-silos et de la déviation d'orthogonalité de Pythagore généralisée entre les hypothèses $H_A$ et $H_B$ :
$$\mathcal{J}(H_A, H_B) = \| \phi^* - \psi^* \|_{\text{Lip}(\mathcal{G})} \times \exp\left( - \left| D_\Phi(P_{AB} \| P_A) + D_\Phi(P_A \| P_B) - D_\Phi(P_{AB} \| P_B) \right| \right)$$
où $P_{AB}$ est la distribution conjointe empirique des activations sur Llama-3.1 évaluée par `jev-1.14.0`. Par le théorème de Pythagore d'Amari, l'exposant s'annule si et seulement si
