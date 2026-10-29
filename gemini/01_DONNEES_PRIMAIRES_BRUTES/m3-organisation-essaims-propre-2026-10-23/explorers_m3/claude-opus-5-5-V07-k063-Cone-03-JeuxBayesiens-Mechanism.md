BASSIN_MATH: Bourse Déterminantielle à Délégation Ensembliste (BDDE)

LOI_PROPOSEE: $b_i^{t+1}=B_f\cdot\frac{[\Delta_i^{\mathrm{VCG}}]_+}{\sum_{j\in f}[\Delta_j^{\mathrm{VCG}}]_+}$ avec $\Delta_i^{\mathrm{VCG}}=W(S)-W(S\setminus i)$ et $W(S)=\sum_{(i,j)\in S,\,f_i\neq f_j}\big|\det M_{ij}\big|-\lambda\sum_{f_i=f_j}\big|\det M_{ij}\big|$, sous contrainte de délégation $a_k\in D_k=[\theta_k-\delta_k,\theta_k+\delta_k]$.

**1. Mécanisme d'auto-organisation hors-poids**

Chaque agent répond à un lot partagé de $T$ micro-tâches discrètes : verdicts, choix de références, classes jev. On note $M_{ij}$ la matrice de comptage conjointe des réponses de $i$ et $j$. Le déterminant DMI (Kong 2020) est dominant-véridique sur tâches multiples.

- **Lutte contre H4'.** Il récompense l'information croisée inter-familles et pénalise la co-information intra-famille ($\lambda>0$), car des poids partagés gonflent artificiellement $\det M$.
- **Topologie.** L'arête $i\to j$ existe si $|\det M_{ij}|>\tau$. Un explorateur est engendré quand la valeur d'information bayésienne $\mathbb E[\max_a U\mid s]-\max_a\mathbb E[U]$ dépasse son coût. Un démolisseur Red-Team est engendré quand la variance des pivots $\Delta^{\mathrm{VCG}}$ explose.
- **Arbitrage chimère/monoculture.** On passe en chimère si $\Delta W_{\mathrm{chim}}$ par USD dépasse $\Delta W_{\mathrm{mono}}$ par USD.
- **Lutte contre H9.** Chaque délégation hérite d'un ensemble de Holmström $D_k$ dont la largeur $\delta_k$ décroît avec la profondeur, ce qui borne la dérive de consigne.
- **Apprentissage.** Il porte uniquement sur les prompts, les arêtes et les budgets (100 USD Claude, 20 USD Gemini), mis à jour à chaque époque.

**2. Fonction objectif et dispositif anti-Goodhart**

$$R_i=\underbrace{|\det M_{i,-f_i}|}_{\text{DMI croisé}}+\mathbb 1_{\mathrm{audit}}\,\eta\,S_{\mathrm{sph}}(p_i,\ \mathrm{jev})-\mu\,\mathbb 1[a_i\notin D_i]-c\cdot\mathrm{USD}_i$$

- **Score sphérique propre.** $S_{\mathrm{sph}}(p,y)=p_y/\|p\|_2$.
- **Audit aléatoire.** jev intervient avec une probabilité secrète $q\sim\mathrm{Beta}$ sur des tâches tirées a posteriori. Viser jev seul ne domine donc jamais la véracité, puisque le terme DMI reste majoritaire.
- **Anti-récitation.** Les tâches portent sur des articles postérieurs au cutoff, vérifiés par arXiv, Semantic Scholar et Crossref.

**3. Duel décisif ($H_A\perp H_B$)**

- **Hypothèses.** $H_A$ : le gain provient du DMI conditionné à la famille. $H_B$ : le gain provient des ensembles de délégation.
- **Plan factoriel 2×2.** Facteurs : DMI on/off et délégation on/off.
- **Comparaisons à budget constant de 120 USD.** On compare (a) BDDE, (b) un essaim fixe à topologie figée, (c) un essaim i.i.d. à arêtes et budgets aléatoires.
- **Contrôle négatif.** Le DMI est calculé sur des tâches permutées, ce qui détruit l'information tout en conservant les marginales.
- **Mesures.** Exactitude sur 300 tâches post-cutoff vérifiées par graphe, corrélation d'erreurs inter-agents $\rho_{\mathrm{err}}$, et dérive $\|a-\theta\|$ à profondeur 3.
- **Critère de validation.** BDDE doit battre (b) et (c) avec $p<0.01$ (bootstrap apparié). Le contrôle permuté ne doit pas différer de (c). Les effets $A$ et $B$ doivent être additifs, avec une interaction non significative.
