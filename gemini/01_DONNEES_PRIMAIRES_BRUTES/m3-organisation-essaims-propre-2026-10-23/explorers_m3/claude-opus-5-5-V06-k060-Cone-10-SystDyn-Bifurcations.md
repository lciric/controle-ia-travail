BASSIN_MATH: Ombrage de Bowen à Cliquet de Pesin et Angles d'Oseledets (OBP-AO)

LOI_PROPOSEE: $\dot w_k = w_k\big(\tfrac{h_k}{c_k}-\bar h\big)$, avec $h_k=\sum_i\lambda_i^{+}(k)$ (Pesin). On spawne un démolisseur si $d_{sh}>\delta^*$. On impose une chimère si $\angle(E^u_a,E^u_b)<\theta^*$.

**1. Mécanisme d'auto-organisation hors-poids**

L'état de l'essaim est $x_t=(w,G,b)$ : les poids de rôles sur le simplexe, le graphe de délégation et le budget restant. Chaque rôle $k$ (explorateur, démolisseur, vérificateur) induit une application $F_k$ sur l'espace des croyances, plongé par `jev-1.14.0`.

- **Allocation des rôles.** Les spectres de Lyapunov $\lambda_i(k)$ sont estimés par perturbations de consignes. Par la formule de Pesin, $h_k$ mesure la production d'information. La dynamique réplicatrice ci-dessus alloue le budget proportionnellement à $h_k/c_k$, où $c_k$ est le coût en USD.
- **Démolisseur Red-Team.** Chaque chaîne de délégations forme une ε-pseudo-orbite de la consigne racine. D'après le lemme d'ombrage de Bowen, la dérive (H9) reste bornée tant qu'une orbite vraie la suit à distance $\delta^*$. Si la distance d'ombrage $d_{sh}$ dépasse $\delta^*$, l'essaim spawne un démolisseur et élague la branche.
- **Monoculture ou chimère.** Lorsque les sous-espaces instables d'Oseledets de deux agents sont presque alignés, leurs erreurs sont corrélées (H4'). Si l'angle descend sous $\theta^*$, l'agent est remplacé par un agent d'une autre famille de poids.
- **Bifurcation.** Le paramètre de contrôle est $\mu=b/b_0$. Au nœud-col $\mu_c$, la branche exploratrice disparaît et l'essaim bascule en mode consolidation.
- **Mémoire.** Les seuils $\delta^*$, $\theta^*$ et $\mu_c$ ainsi que les graphes $G$ efficaces sont journalisés. Ils servent d'apprentissage hors-poids entre épisodes.

**2. Fonction objectif et anti-Goodhart**

$$R=\frac{\Delta I_{ext}}{\Delta\mathrm{USD}}-\alpha\,\Lambda_J-\beta\,d_{sh}-\gamma\max_{a\neq b}\cos\angle(E^u_a,E^u_b)$$

- $\Delta I_{ext}$ ne compte que les affirmations vérifiées par arXiv, Semantic Scholar ou Crossref et absentes des sorties à froid. La récitation de la mémoire paramétrique est donc nulle en gain.
- $\Lambda_J$ est l'exposant de Lyapunov du juge, $\Lambda_J=\lim\frac1n\log\|\partial\,\mathrm{jev}/\partial\,\mathrm{texte}\|$. Une forte sensibilité du score à des paraphrases neutres signale une exploitation du juge (Goodhart) et est pénalisée.
- La rubrique de `jev` est tournée et en partie cachée à chaque épisode.

**3. Duel décisif ($H_A\perp H_B$)**

Quatre bras, chacun avec un budget identique (100 USD Claude et 20 USD Gemini) et 30 graines :

- **(A)** OBP-AO ;
- **(F)** topologie fixe ;
- **(I)** topologies tirées i.i.d. ;
- **(N)** contrôle négatif : OBP-AO dont les signaux $h_k$, $d_{sh}$ et les angles d'Oseledets sont permutés aléatoirement.

Les hypothèses sont pré-enregistrées :

- **$H_A$** : $\mathbb E[\Delta I_{ext}/\mathrm{USD}]_A>\max(F,I)$, avec une dérive H9 plus faible.
- **$H_B$** : $N\approx I$. Cette égalité prouve que le gain vient des signaux dynamiques et non de la simple adaptativité.

L'évaluation est confiée à un juge croisé aveugle et indépendant de `jev`. Le test retenu est un test de permutation avec correction de Holm.

**Critère de rejet** : la loi est réfutée si $A\le F$, ou si $N\approx A$.
