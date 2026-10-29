BASSIN_MATH: Réponse Linéaire de Ruelle à Pôles de Résonance (RLR-PR)

LOI_PROPOSEE: $b_k^{t+1} \propto \big[\hat\chi_k^{\mathrm{fait}} - \lambda\,\hat\chi_k^{\mathrm{cons}} - \mu \sum_{l\neq k}\rho_{kl}\big]_+ / c_k$, avec $\hat\chi_k^{\epsilon}=\partial_\epsilon\,\mathbb{E}_{\mu_\epsilon}[\varphi_k]\big|_{\epsilon=0}$ (formule de Ruelle).

**1. Mécanisme d'auto-organisation hors-poids**

L'essaim est traité comme un système dynamique $x_{t+1}=f_\epsilon(x_t)$ : $x$ regroupe la topologie, les rôles, les familles et la mémoire externe. Il possède une mesure invariante $\mu_\epsilon$, et $\varphi_k$ désigne le score `jev-1.14.0` des sorties de l'agent $k$. Deux perturbations sont injectées par paires à graines communes :

- **ε-fait** : une citation contrefactuelle plantée, vérifiable via Crossref ou Semantic Scholar ;
- **ε-cons** : une paraphrase neutre de la consigne.

Un bon agent répond fortement aux faits, ce qui signale une lecture effective des preuves plutôt qu'une récitation paramétrique. Il répond faiblement à la paraphrase, ce qui signale l'absence de dérive (H9).

La matrice de susceptibilités croisées $\rho_{kl}=\cos(\hat\chi_k,\hat\chi_l)$ mesure la corrélation des erreurs (H4'). Elle dicte l'arbitrage suivant :

- **Bascule vers la chimère** : si le $\rho$ intra-famille dépasse 0,6, on remplace par un agent de l'autre famille.
- **Monoculture** : elle est conservée tant que $\rho<0{,}3$, car elle est moins chère.
- **Topologie** : l'arête $k\to l$ est maintenue si $\hat\chi_l$ répond aux messages de $k$ au-delà d'un seuil.
- **Spawn d'un explorateur** : il est déclenché lorsque le premier pôle de résonance de Ruelle $z_1$ de $\hat\chi(\omega)$, estimé par Padé sur l'autocorrélation, approche le cercle unité ($|z_1|>0{,}9$). Ce ralentissement critique annonce une bifurcation.
- **Spawn d'un démolisseur Red-Team** : il est déclenché lorsque $\hat\chi^{\mathrm{fait}}\approx 0$, c'est-à-dire lorsque l'agent est rigide et récite.

**2. Fonction objectif et anti-Goodhart**

$$R=\sum_k \frac{\hat\chi_k^{\mathrm{fait}}-\lambda\hat\chi_k^{\mathrm{cons}}}{c_k}-\mu\,\lambda_{\max}(\rho)-\nu\,\mathbb{1}\big[|z_1|>0{,}97\big].$$

Le signal porte sur une **dérivée** et non sur un niveau. Gonfler $\varphi$ (Goodhart sur le juge) laisse $\chi$ inchangé, puisque les différences appariées annulent le biais.

Les perturbations sont secrètes et tirées aléatoirement. Leur vérité terrain provient des graphes bibliographiques, jamais du juge. Le budget est découpé en 100 USD pour Claude et 20 USD pour Gemini, chaque enveloppe étant normalisée séparément.

**3. Duel décisif de validation ($H_A \perp H_B$)**

**Bras comparés**, tous au même budget (120 USD) et aux mêmes graines :

- **$H_A$** : RLR-PR ;
- **$H_B$ fixe** : topologie figée ;
- **$H_B$ i.i.d.** : agents indépendants avec vote majoritaire ;
- **Contrôle négatif** : RLR-PR avec $\hat\chi$ permutés entre agents. Ce bras a un surcoût identique mais une information nulle.

**Critère** : sur 200 tâches tenues à l'écart, contenant des erreurs bibliographiques plantées, on mesure le taux de détection vérifié par API ainsi que la dérive de consigne. Celle-ci est définie comme la distance `jev` entre la consigne racine et la sortie de profondeur 3.

**Règle de décision** : $H_A$ gagne si sa détection dépasse celle de chaque bras de plus de 10 points (Wilcoxon apparié, Holm, $\alpha=0{,}01$) et si le contrôle permuté ne fait pas mieux que le bras fixe. Toute autre issue réfute la loi.
