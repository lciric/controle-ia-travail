BASSIN_MATH: Loi du Noyau Commun de Wyner et du Déficit Structurel (NoWyDS)

LOI_PROPOSEE: $\mathcal{G}_{t+1}=\arg\max_{\mathcal{G}}\sum_{e\in\mathcal{G}}\frac{\Delta L_{\mathrm{MDL}}(\mathcal{B}\mid y_e)-\lambda\,\hat C_W(y_e;y_{\mathcal{G}\setminus e})}{c_e}$ sous $\sum_e c_e\le B$, où $\hat C_W$ est l'information commune de Wyner estimée par compression.

**1. Mécanisme d'auto-organisation hors-poids**

- **Mémoire évolutive.** Chaque agent $e$ (modèle × rôle × consigne) produit des sorties $y_e$. L'essaim n'apprend qu'à travers une bibliothèque de consignes et de topologies. Cette bibliothèque est versionnée et mutée par sélection, jamais par gradient.
- **Communication.** Une arête $i\to j$ existe si $\mathrm{NCD}(y_i,y_j)$ est intermédiaire, entre 0,3 et 0,7. Les sorties sont alors complémentaires sans être étrangères.
- **Monoculture ou chimère.** $\hat C_W$ est estimé par $\min_W[\,|Z(W)|+|Z(y_i|W)|+|Z(y_j|W)|\,]-|Z(y_i,y_j)|$, avec un compresseur $Z$ et `jev-1.14.0` comme quantificateur gratuit. Si $\hat C_W$ intra-famille dépasse $\tau$ (symptôme H4'), on chimérise en remplaçant l'agent par un modèle d'une autre famille. Sinon, on garde la monoculture, moins chère.
- **Explorateur.** On spawne un explorateur lorsque le déficit de Kolmogorov $\delta=L(\text{modèle})+L(\mathcal{B}|\text{modèle})-L^*(\mathcal{B})$ stagne. Cela signale un modèle de la littérature trop simple.
- **Démolisseur Red-Team.** On spawne un démolisseur lorsque $L(\mathcal{B}|y_e)$ chute trop vite. Une chute trop rapide signale un surapprentissage ou une récitation.
- **Garde anti-dérive (H9).** Toute délégation $k$ est rejetée si $\mathrm{NCD}(\text{consigne}_0,\text{consigne}_k)>\epsilon_d$.

**2. Fonction objectif anti-Goodhart**

$$R_e=\frac{L(\mathcal{B}_{\text{test}})-L(\mathcal{B}_{\text{test}}\mid y_e)}{c_e}-\lambda\,\hat C_W(y_e;y_{-e})-\mu\,\big[1-\mathrm{NCD}(y_e,\,y_e^{\varnothing})\big].$$

- $\mathcal{B}_{\text{test}}$ est un sous-graphe de citations futures tiré d'arXiv, Semantic Scholar et Crossref, gelé et caché. La récompense mesure un gain de compression sur ce sous-graphe, pas une note de juge.
- $y_e^{\varnothing}$ est la sortie produite sans sources. Le terme en $\mu$ pénalise donc la récitation de la mémoire paramétrique.
- Le juge LLM n'intervient que comme veto binaire. Il est audité par une concordance de rang avec $R_e$. Si ce rang diverge, le juge est soupçonné d'être goodhartisé et il est ignoré.
- Le budget est alloué selon $c_e\propto R_e^+$, séparément pour l'enveloppe Claude (100 USD) et l'enveloppe Gemini (20 USD).

**3. Duel décisif $H_A\perp H_B$**

- **Hypothèses.**
  - $H_A$ : NoWyDS réduit $L(\mathcal{B}_{\text{test}})$ davantage que les témoins.
  - $H_B$ : le gain vient du seul effet chimère.
- **Bras, tous à 120 USD :**
  1. NoWyDS ;
  2. essaim fixe chimérique ;
  3. essaim i.i.d. monoculture ;
  4. contrôle négatif : NoWyDS dont $\hat C_W$ est calculé sur des sorties permutées aléatoirement.
- **Protocole.** On utilise 30 questions de contrôle de l'IA et 5 graines par bras. Le critère principal est le gain de compression sur les citations postérieures à la date de coupure des modèles. Le test est un test de permutation apparié, avec correction de Holm.
- **Décision.**
  - $H_A$ est validée si l'on observe NoWyDS > bras 4 > bras 2 ≈ bras 3, avec $p<0{,}01$.
  - $H_B$ l'emporte si NoWyDS ≈ bras 2.
- **Indépendance des hypothèses.** Un plan factoriel croise topologie (adaptative ou fixe) et composition (chimère ou monoculture). Il sépare les deux effets, ce qui rend les hypothèses orthogonales.
