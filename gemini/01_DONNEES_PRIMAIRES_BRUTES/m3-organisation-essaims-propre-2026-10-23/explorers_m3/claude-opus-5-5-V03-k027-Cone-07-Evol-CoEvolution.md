BASSIN_MATH: Hamilton-Multiniveau à Parenté de Poids (HAMPAR)

LOI_PROPOSEE: $\Delta\bar z=\underbrace{\mathrm{Cov}_k(W_k,z_k)}_{\text{inter-cellules}}+\underbrace{\mathbb E_k[\mathrm{Cov}_i(w_{ik},z_{ik})]}_{\text{intra}}$. Un rôle $s$ se réplique dans la cellule $k$ si et seulement si $\,B_s(1-r_k)>C_s$, avec $r_k=\rho(\varepsilon_i,\varepsilon_j)$ la parenté d'erreur. Les fréquences suivent le réplicateur-mutateur $\dot x_s=\sum_{s'}x_{s'}f_{s'}Q_{s's}-\bar f x_s$.

**1. Mécanisme d'auto-organisation hors-poids**
- **Population.** L'essaim est une population de cellules $k$, chacune formée de 3 à 5 agents.
- **Génotype.** Le génotype d'un agent est le triplet (prompt-rôle, famille de poids, budget).
- **Rôles.** Les rôles sont : explorateur, démolisseur Red-Team, vérificateur bibliographique.
- **Parenté.** $r_k$ est mesurée gratuitement par jev : c'est la corrélation des erreurs sur des items-sondes.
- **Monoculture contre chimère.** Une monoculture Claude ($r$ élevé) ne survit que si son bénéfice compense $1/(1-r)$. Sinon, la mutation $Q$ injecte un agent Gemini, ce qui produit une chimère.
- **Création de sous-agents.** Un démolisseur est créé lorsque $\mathrm{Cov}_i$ intra devient positive sans gain inter, signe de complaisance interne. Un explorateur est créé lorsque des niches MAP-Elites (axes nouveauté × sous-domaine) restent vides.
- **Topologie.** Seules les cellules communiquent, via un archive-élite. Les messages entre agents de cellules différentes sont interdits, ce qui limite la dérive H9.
- **Contrôle de la dérive.** Chaque délégation porte la consigne racine, contrôlée par jev : il faut une similarité $\ge\tau$, sinon la branche est éliminée.

**2. Fonction objectif et anti-Goodhart**

$$W_k=\frac{V_k}{\$_k}-\lambda\, r_k-\mu D_k-\nu P_k+\eta N_k$$

- $V_k$ : affirmations vérifiées sur un lot d'audit caché et tiré à chaque génération.
- $D_k$ : dérive de consigne mesurée par jev.
- $P_k$ : récitation, c'est-à-dire une citation absente ou non conforme dans Semantic Scholar ou Crossref.
- $N_k$ : nouveauté de niche MAP-Elites.

Mesures anti-Goodhart :
- Les seuils de jev sont tournés aléatoirement.
- Des canaris piégés détectent la flatterie du juge.
- La sélection se fait sur $W$ hors échantillon, jamais sur le score vu par les agents.

**3. Duel décisif ($H_A\perp H_B$)**

Le budget est fixe et identique pour tous les bras : 100 USD Claude et 20 USD Gemini par bras, sur 200 tâches pré-enregistrées.

Bras :
- **(A) HAMPAR.**
- **(B) Topologie fixe** avec la même chimère.
- **(C) Rôles i.i.d.**, tirés au hasard à chaque génération.
- **(N) Contrôle négatif** : HAMPAR dont les $W_k$ sont permutés aléatoirement.

Hypothèses :
- $H_A$ : le terme inter-cellules $\mathrm{Cov}_k$ est positif et le rendement $V/\$$ de A dépasse ceux de B et C.
- $H_B$ (orthogonale) : le gain provient seulement de la chimère. Ce cas est testé par B, qui possède la même composition mais aucune sélection.

Critères :
- La permutation N doit annuler le gain. Sinon, l'avantage est un artefact.
- A doit en outre réduire $r$ mesuré.
- Le test est bootstrap apparié avec $\alpha=0{,}01$.
