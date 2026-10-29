BASSIN_MATH: Loi de Menger-PCP à Coloration Anti-Collusion (MPCAC)

LOI_PROPOSEE: Une affirmation $a$ est acceptée ssi $\kappa_\chi(G_t, a) \ge 2\hat f_t + 1$ et $\Pr[\text{jev rejette } \pi_a \mid q \text{ sondes}] = 0$. Les arêtes sont mises à jour par $w_{ij} \leftarrow w_{ij}\, e^{-\eta(\rho_{ij} + \beta C_{ij})}$, avec $C_{ij} = P(e_i \wedge e_j) - P(e_i)P(e_j)$.

**1. Auto-organisation hors-poids**

Les agents sont des sommets colorés par famille de poids $\chi \in \{\text{fable}, \text{opus}, \text{argon}\}$. Une affirmation doit circuler par $\kappa_\chi$ chemins sommet-disjoints (Menger/Dolev) dont les couleurs internes sont distinctes. Chaque nœud produit un certificat $\pi$ découpé en lemmes atomiques, et `jev` en sonde $q$ positions secrètes, ce qui donne une solidité $\le \varepsilon^q$ (style PCP).

L'apprentissage porte sur la topologie, sans toucher aux poids :
- $\rho_{ij}$ est le taux de rejet PCP sur l'arête $i \to j$, qui capture la dérive de consigne $H9$ par délégation.
- $C_{ij}$ est l'excès de co-erreur, qui sert de détecteur de collusion ($H4'$).
- $\hat f_t = \max_\chi \text{rang}_\varepsilon(C_{\chi\chi})$ estime le nombre de fautes byzantines corrélées.

Règles de mutation :
- **Chimère contre monoculture.** On passe en chimère si $C_{\chi\chi} > \tau$, et on reste en monoculture sinon, car elle est moins coûteuse.
- **Explorateur.** On en engendre un si $\kappa_\chi$ est satisfait mais que la couverture du graphe bibliographique (arXiv, S2, Crossref) est inférieure à $\theta$.
- **Démolisseur Red-Team.** On en engendre un si $\rho \to 0$ trop vite, signe d'une facilité suspecte (Goodhart). Il attaque alors le lemme le moins sondé.

Contre la récitation paramétrique, chaque lemme doit citer un DOI vérifiable par Crossref. Le budget est réparti au prorata de $1/\text{coût}$ par chemin disjoint, avec une contrainte séparée : 100 USD côté Claude, 20 USD côté Gemini.

**2. Fonction objectif et anti-Goodhart**

$$R = \text{Acc}_{\text{scellée}} - \lambda \sum_{i<j} C_{ij}^{+} - \mu\,\$ - \nu\,\left|\text{Acc}_{\text{jev}} - \text{Acc}_{\text{scellée}}\right|$$

- $\text{Acc}_{\text{scellée}}$ est mesurée sur des positions de sonde tirées par une graine cachée et jamais réutilisées (secret de type Arthur).
- Le terme $\nu$ pénalise l'écart entre le juge visible et le juge caché, ce qui rend la sur-optimisation du juge non rentable.

**3. Duel décisif ($H_A \perp H_B$)**

Le protocole est pré-enregistré, avec un budget identique pour chaque bras (120 USD), $N = 200$ questions et 5 graines. Quatre bras sont comparés :
- (A) MPCAC ;
- (B) un essaim à topologie fixe ;
- (C) un échantillonnage i.i.d. avec vote majoritaire ;
- (D) un **contrôle négatif** : MPCAC avec des couleurs de famille permutées aléatoirement.

On injecte 20 % d'agents byzantins plantés, sous forme de consignes dérivées et de collusions coordonnées.

- $H_A$ : A surpasse B, C et D en $\text{Acc}_{\text{scellée}}$ et en taux de détection des byzantins.
- $H_B$ : l'avantage de A disparaît en D, ce qui montre que le gain provient de la coloration anti-collusion et non du simple surcroît de vérification.

Le test est un test de permutation apparié, avec correction de Holm et un seuil $\alpha = 0{,}01$. La loi est falsifiée si $A \approx D$.
