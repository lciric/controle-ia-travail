BASSIN_MATH: Appariement de Morse-Forman à Bascule de Cheeger (AMF-BC)

LOI_PROPOSEE: $V_t=\arg\max_{V\ \text{gradient discret}}|V|$ sur $K_t$ ; chaque cellule critique $\sigma\in C_k(V_t)$ reçoit un agent de rôle $\rho(k)$ et un budget $b_\sigma=B\cdot\frac{\mathrm{pers}(\sigma)}{\sum_{\tau}\mathrm{pers}(\tau)}$ ; la famille assignée vaut $f^*(\sigma)=\arg\min_f \mathrm{part}_f(\mathrm{st}\,\sigma)$ si $h_{\mathcal F}<h_0$, et la famille la moins chère sinon.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **Complexe des affirmations $K_t$.** Ses 0-cellules sont les affirmations, ses 1-cellules les liens de support ou d'attaque. Ses 2-cellules sont les triangles dont la cohérence est validée par `jev`.
- **Filtration et appariement.** Le complexe est filtré par la confiance `jev`. Un gradient de Forman $V_t$ apparie les cellules résolues. Les cellules critiques non appariées vérifient l'inégalité de Morse $|C_k|\ge\beta_k$ : ce sont exactement les tâches restantes.
- **Rôles selon la dimension.**
  - $\rho(0)$ = explorateur : une affirmation isolée exige un ancrage bibliographique via arXiv, Semantic Scholar ou Crossref.
  - $\rho(1)$ = démolisseur Red-Team : un cycle persistant signale une justification circulaire.
  - $\rho(2)$ = synthétiseur : un trou de cohérence reste à combler.
- **Mutation de la topologie.** Seuls les agents partageant une étoile $\mathrm{st}\,\sigma$ communiquent entre eux. La topologie change donc à chaque recalcul de $V_t$, sans aucun réentraînement des poids.
- **Bascule monoculture/chimère (contre H4').** $h_{\mathcal F}$ est la constante de Cheeger du graphe d'accord, estimée spectralement par $\lambda_2/2\le h$. Une valeur faible signifie que les accords se regroupent par famille de poids : on bascule alors en chimère.
- **Dérive de consigne (contre H9).** Chaque délégation forme une 1-chaîne issue de la consigne racine. Une arête dont le score `jev` de fidélité à la racine passe sous $\theta$ est élaguée.
- **Récitation de la mémoire paramétrique.** Une affirmation sans DOI vérifié reste critique en permanence.

**2. Fonction objectif et anti-Goodhart**

$$R_t=\frac{\sum_{\sigma\in C(V_{t-1})}\mathrm{pers}(\sigma)-\sum_{\sigma\in C(V_t)}\mathrm{pers}(\sigma)}{\mathrm{coût}_t}-\mu\,\mathbb 1[\text{suppression de cellule}]-\nu\,\|h_1^{\mathrm{harm}}\|^2$$

- Seul l'appariement compte comme progrès : supprimer une cellule pour réduire $\beta$ est puni.
- La part harmonique $h_1^{\mathrm{harm}}$ (noyau de $L_1$) mesure les cycles irréductibles dissimulés.
- Le juge est protégé par trois garde-fous : les prompts `jev` sont tirés dans une partition tournante, $R$ est recalculé sur une partition `jev` retenue, et tout écart entre les deux annule $R_t$.

**3. Duel décisif $H_A\perp H_B$ (budget fixe : 100 USD Claude et 20 USD Gemini par bras)**

- **Bras comparés :**
  - AMF-BC ;
  - arbre planificateur-ouvriers fixe ;
  - échantillonnage i.i.d. avec vote majoritaire ;
  - contrôle négatif : AMF-BC avec des persistances permutées aléatoirement (mêmes effectifs de rôles) ;
  - ablation : AMF-BC sans bascule de Cheeger.
- **Tâches :** 60 questions contenant des prémisses fausses injectées.
- **Métrique :** précision des affirmations vérifiées par DOI et par `jev` retenu.
- **$H_A$ (signal topologique causal) :** AMF-BC surpasse le bras fixe et le bras i.i.d., tandis que le contrôle permuté ne surpasse pas le bras fixe.
- **$H_B$ (bascule familiale) :** AMF-BC réduit la corrélation intra-famille des erreurs par rapport à l'ablation.
- **Orthogonalité :** les deux hypothèses sont testées par des ablations disjointes.
- **Analyse :** préenregistrement, bootstrap apparié sur les questions et correction de Holm.
