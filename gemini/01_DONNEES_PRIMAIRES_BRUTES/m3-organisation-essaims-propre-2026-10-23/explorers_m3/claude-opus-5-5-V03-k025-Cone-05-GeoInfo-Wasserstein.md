BASSIN_MATH: Loi de Projection Alternée e/m à Défaut Pythagoricien (PAPD)

LOI_PROPOSEE: $\Delta_i=D_{KL}(q^\star\|p_i)-D_{KL}(q^\star\|r_i)-D_{KL}(r_i\|p_i)$, avec $r_i=\Pi^{(m)}_{\mathcal M}p_i$ ; si $|\Delta_i|>\tau$ alors on spawne un agent, puis $\theta_i\leftarrow\theta_i-\eta\,G(\theta_i)^{-1}\nabla_\theta D_{KL}(r_i\|p_{\theta_i})$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **Représentation des agents.** Chaque agent $i$ est une distribution $p_i$ sur $K$ classes de thèses, estimée gratuitement par `jev-1.14.0`. Son paramètre hors-poids $\theta_i$ regroupe le prompt, la mémoire et les exemples ; il vit dans une famille e-plate $\mathcal E$.
- **Variété des preuves.** $\mathcal M$ est la variété m-plate des mélanges compatibles avec les preuves vérifiées par arXiv, Semantic Scholar et Crossref.
- **Apprentissage.** On alterne une m-projection (ancrage sur les preuves) et une e-projection, via le gradient naturel d'Amari où $G$ désigne la métrique de Fisher-Rao.
- **Détection des conflits.** En géométrie duale plate, le théorème de Pythagore donne $\Delta_i=0$. Un défaut non nul signale une région où les preuves se contredisent ou ne sont pas plates.
- **Choix du sous-agent.** Si $\Delta_i<-\tau$, on spawne un démolisseur Red-Team. Si $\Delta_i>\tau$, on spawne un explorateur.
- **Topologie de communication.** On calcule le plan de transport optimal $\pi^\star$ de Wasserstein-1 sur le graphe des thèses entre les $p_i$. L'arête $i\to j$ est activée si $\pi^\star_{ij}\,d_{FR}(p_i,p_j)>\kappa$.
- **Monoculture ou chimère.** Si deux agents de même famille de poids vérifient $d_{FR}<\varepsilon$, ce qui signale H4', l'un d'eux est remplacé par un agent d'une autre famille.
- **Anti-dérive (H9).** Tout descendant doit satisfaire $d_{FR}(p_{\text{enfant}},p_{\text{racine}})\le\rho$. L'ancrage se fait sur la racine et non sur le parent.

**2. Fonction objectif et anti-Goodhart**

$$R=\frac{W_1(p_{\text{essaim}}^{t},q^\star)-W_1(p_{\text{essaim}}^{t+1},q^\star)}{c_t}-\lambda\,\big|J_{\text{pub}}-J_{\text{secret}}\big|-\mu\,\mathbb 1[\text{non sourcé}]$$

- $q^\star$ est ancrée uniquement sur des références vérifiées via les API bibliographiques, et $c_t$ est le coût dépensé à l'étape $t$.
- `jev` est évalué sur une partition publique et sur une partition secrète tournante. Tout écart entre les deux est pénalisé, ce qui contre la loi de Goodhart.
- Une thèse sans source vérifiable rapporte zéro et déclenche la pénalité, ce qui neutralise la récitation de la mémoire paramétrique.
- Le budget est alloué par descente miroir : $b\leftarrow b\odot e^{\eta R}/Z$, sous les plafonds de 100 USD pour Claude et 20 USD pour Gemini.

**3. Duel décisif de validation M3 ($H_A\perp H_B$)**

- **Hypothèses.** $H_A$ : PAPD réduit $W_1$ par dollar. $H_B$ : un essaim fixe ou i.i.d. fait aussi bien.
- **Conditions.** On compare quatre bras à budget identique sur 60 questions préenregistrées :
  - PAPD ;
  - une topologie fixe ;
  - des agents i.i.d. ;
  - un contrôle négatif PAPD où les $\Delta_i$ sont permutés aléatoirement.
- **Critère de victoire.** PAPD doit dépasser les trois autres bras sur $W_1$ final (test apparié de Wilcoxon, $p<0.01$) et sur le rappel de références validées par Crossref.
- **Critères de réfutation.** La loi est réfutée si le contrôle permuté égale PAPD. Elle l'est aussi si l'écart $|J_{\text{pub}}-J_{\text{secret}}|$ de PAPD est supérieur à celui des témoins.
