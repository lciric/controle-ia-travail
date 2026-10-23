BASSIN_MATH: Pari de Solomonoff sur Topologies filtré par Distance de Compression Normalisée (PST-NCD)

LOI_PROPOSEE: $w_{t+1}(\tau)\propto 2^{-L(\tau)}\,w_t(\tau)\,2^{\beta G_t(\tau)}$, avec $G_t(\tau)=\dfrac{L(D^\star\mid C)-L(D^\star\mid C,y_\tau)}{\$_\tau}$, sous la contrainte $\mathrm{NCD}(c_0,m_k)\le\epsilon$ à chaque délégation $k$.

1. **Mécanisme d'auto-organisation hors-poids**
   - **Topologies comme programmes.** Chaque topologie $\tau$ (graphe de communication, rôles, familles de modèles) s'écrit dans un DSL. Sa longueur $L(\tau)$ fixe un prior de Solomonoff, si bien que les topologies simples sont favorisées.
   - **Mutation.** L'essaim échantillonne $\tau\sim w_t$, puis la mute par ajout ou suppression d'arête, ou par changement de rôle ou de famille.
   - **Choix du sous-agent.** On calcule $\mathrm{NCD}(y_i,y_j)$ entre les sorties des agents avec gzip ou zstd, à coût nul.
     - Si $\mathrm{NCD}<\delta$, les erreurs sont probablement corrélées (H4′) : on spawne un démolisseur Red-Team d'une autre famille, ce qui crée une chimère.
     - Si $\mathrm{NCD}>1-\delta$, l'essaim diverge : on spawne un explorateur monoculturel chargé de consolider.
   - **Anti-dérive (H9).** Tout message $m_k$ vérifiant $\mathrm{NCD}(c_0,m_k)>\epsilon$ est rejeté et régénéré, où $c_0$ est la consigne racine.
   - **Allocation du budget.** Les dollars sont répartis au prorata de $w_t(\tau)\,\mathbb{E}[G]$, dans un pot Claude de 100 USD et un pot Gemini de 20 USD, séparés.

2. **Fonction objectif et anti-Goodhart**
   $$R(y)=\underbrace{\big[L(D^\star\mid C)-L(D^\star\mid C,y)\big]}_{\text{gain de compression scellé}}\cdot\mathbb{1}[\texttt{jev}(y)=\text{valide}]-\lambda\,\mathbb{1}\!\left[\tfrac{L(y\mid C)}{L(y)}<\rho\right]$$
   - **$C$** est le corpus récupéré via arXiv, Semantic Scholar et Crossref.
   - **Pénalité de récitation.** Le second terme pénalise toute sortie $y$ trop compressible connaissant $C$, ce qui signale une récitation de la mémoire paramétrique.
   - **Données scellées.** $D^\star$ est un ensemble de données de contrôle jamais montré aux agents ni au juge.
   - **Rôle du juge.** `jev-1.14.0` n'agit que comme garde binaire, pas comme gradient. Si le score du juge devient compressible à partir des seuls traits de surface de $y$, la règle est gelée par audit.

3. **Duel décisif ($H_A\perp H_B$)**
   - **Bras.** Budget constant de 120 USD par bras, 20 graines, tâches identiques.
     - **A** : PST-NCD.
     - **B** : topologie fixe, la meilleure sélectionnée a priori.
     - **C** : topologies i.i.d. tirées de $2^{-L}$, sans mise à jour.
     - **N (contrôle négatif)** : PST-NCD avec $G_t$ permuté aléatoirement.
   - **Hypothèses.**
     - $H_A$ : $R_A>R_B,R_C$.
     - $H_B$ : $R_N\approx R_C$, ce qui prouve que le gain vient du signal et non de la seule mutation.
   - **Métriques secondaires.**
     - Corrélation d'erreurs inter-agents.
     - Taux de rejets $\mathrm{NCD}$, mesure de la dérive.
     - Récitation, mesurée par $\rho$.
   - **Analyse.** Test de Wilcoxon apparié, préenregistré, avec correction de Holm.
   - **Critère de réfutation.** La loi est réfutée si $R_N\ge R_A$ ou si $R_A\le R_C$.
