BASSIN_MATH: Clonage de Grandes Déviations à Lyapunov Incliné (CGD-LI)

LOI_PROPOSEE: $\mathcal{L}_s f(\tau)=\sum_{\tau'}P(\tau\to\tau')\,e^{s\,\Lambda_T(\tau')}f(\tau')$, avec $\psi(s)=\log\rho(\mathcal{L}_s)$. Chaque agent est cloné avec un poids $\propto e^{s\Lambda_T}$ ou tué sinon, et l'inclinaison est mise à jour par $\dot s=\eta\,(\psi''(s)-\kappa)$.

**1. Auto-organisation hors-poids**

- **Exposant local.** $\Lambda_T$ est l'exposant de Lyapunov à temps fini du verdict d'un agent. On le mesure par la divergence des scores `jev` sous $k$ perturbations métamorphiques : paraphrases, permutation d'entités, retrait de citations.
- **Spawn.** Si $\Lambda_T>\epsilon$, l'affirmation est fragile et l'agent spawne un démolisseur Red-Team. Si $\Lambda_T\approx0$ alors que la perturbation devait changer la réponse, il s'agit de récitation paramétrique ; l'agent spawne un explorateur, ancré sur arXiv, Semantic Scholar et Crossref.
- **Topologie.** Le graphe « qui parle à qui » suit le vecteur propre droit $r_s$ de $\mathcal{L}_s$ : les agents sont reliés en priorité aux nœuds de forte masse $r_s$.
- **Monoculture ou chimère.** On mesure le cosinus entre les vecteurs de Lyapunov covariants d'une même famille. Si $\cos>c$, les erreurs sont corrélées ($H4'$) et l'essaim impose des clones chimériques croisant les familles. Sinon, la monoculture est conservée, car elle est moins chère.
- **Dérive $H9$.** Soit $\lambda_{H9}$ l'exposant du produit des jacobiens de l'embedding de la consigne le long de la chaîne de délégation. La profondeur est plafonnée à $d^*=\lfloor\log(\delta/\delta_0)/\lambda_{H9}\rfloor$.
- **Budget.** La part de chaque famille $f$ est $B_f\propto \sum_{i\in f} r_s(i)/c_f$, sous les contraintes $\le100$ USD pour Claude et $\le20$ USD pour Gemini.

**2. Objectif et anti-Goodhart**

$$J=\mathbb{E}[V_{\text{ext}}]-\beta\,\big|\psi_{\text{jev}}(s)-\psi_{\text{ext}}(s)\big|-\gamma\,\text{Coût}$$

- $V_{\text{ext}}$ est l'existence et la cohérence des références vérifiées dans les graphes bibliographiques, un signal non manipulable par génération.
- $\psi_{\text{jev}}$ et $\psi_{\text{ext}}$ sont les fonctions génératrices de cumulants calculées respectivement avec le juge et avec la vérification externe.
- Leur écart détecte Goodhart : si l'essaim optimise le juge, les deux spectres divergent.
- `jev` n'est qu'un observable perturbatif, jamais une récompense directe.

**3. Duel M3 ($H_A\perp H_B$)**

Les trois bras ont le même budget, le même nombre de clones et les mêmes tâches. Des erreurs bibliographiques sont injectées à l'aveugle.

- **A — CGD-LI** : la loi complète.
- **B — Essaim fixe** : topologie statique.
- **C — Contrôle négatif i.i.d.** : clonage avec des $\Lambda_T$ permutés aléatoirement, ce qui donne le même calcul sans structure dynamique.

Les deux hypothèses rivales font des prédictions orthogonales :

- **$H_A$ (structure dynamique)** : le gain sur le taux d'erreurs injectées détectées et sur $V_{\text{ext}}$ apparaît seulement pour $s>s_c$. Ce seuil $s_c$ est le pic de $\psi''$, signature d'une bifurcation de phase dynamique.
- **$H_B$ (simple surplus de calcul)** : le gain est plat en $s$ et identique entre A et C.

**Protocole** : balayage de $s\in[-2,2]$ sur 30 graines, avec un test de rupture de pente au point $s_c$.

**Réfutation** : si C égale A, ou si le gain ne présente aucune rupture au point $s_c$, la loi CGD-LI est rejetée.
