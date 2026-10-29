BASSIN_MATH: Loi d'Ancrage Généalogique par Arrêt de Shiryaev (LAGAS)

LOI_PROPOSEE: $V_t(\pi)=\max\big\{g(\pi),\ \max_{a\in\{\text{expl},\text{dém}\},\,m\in\{\text{mono},\text{chim}\}} -c_{a,m}(1+\lambda_C,\lambda_G)+\mathbb E[V_{t+1}(\pi')\mid a,m]\big\}$, avec ré-ancrage forcé au temps $\tau=\inf\{t: R_t\ge A\}$, où $R_t=(1+R_{t-1})\,\ell_t$ est la statistique de Shiryaev–Roberts.

1. **Mécanisme d'auto-organisation hors-poids**
La tâche forme un arbre généalogique de délégations. Chaque nœud $v$ maintient une croyance $\pi_v$ sur la véracité d'une affirmation, ainsi qu'un filtre particulaire (N=500) sur la corrélation latente d'erreurs $\rho_{f,f'}$ entre familles de poids, alimenté par les désaccords observés.
- **Spawn** : un explorateur est créé tant que l'équation de Bellman préfère continuer. Un démolisseur Red-Team est créé lorsque le SPRT de Wald sur l'affirmation reste entre $B$ et $A$ après $k$ votes concordants, ce qui signale une suspicion de consensus corrélé (H4').
- **Monoculture ou chimère** : ce choix est confié à un bandit contextuel Thompson à fenêtre glissante, de contexte $(\hat\rho,\text{profondeur},\text{coût})$. La chimère est choisie lorsque $\hat\rho_{\text{mono}}$ postérieur dépasse le gain de coût.
- **Dérive (H9)** : `jev-1.14.0`, gratuit, mesure à chaque délégation $\ell_t$, le rapport de vraisemblance « sortie conforme / dérivée » par rapport à la consigne racine. Au temps $\tau$, la branche est coupée et re-déléguée depuis la racine.
- **Apprentissage** : les priors du bandit, les particules et les seuils $A,B$ persistent entre missions dans une mémoire externe, sans réentraînement des poids.
- **Budget** : les multiplicateurs de Lagrange $\lambda_C$ (Claude, 100 USD) et $\lambda_G$ (Gemini, 20 USD) sont mis à jour par sous-gradient.

2. **Fonction objectif et anti-Goodhart**
$r=\sum_i \mathbb 1[\text{affirmation }i\text{ vérifiée par graphe arXiv/S2/Crossref}]-\beta\,\mathrm{KL}(\text{jev}\,\|\,\text{graphe})-\gamma\,\text{récitation}-\lambda\cdot\text{USD}$.
- La récitation est mesurée par l'absence de DOI résolu.
- Un CUSUM $S_t=\max(0,S_{t-1}+d_t-\kappa)$ suit le désaccord $d_t$ entre jev et le graphe. Lorsqu'il franchit $h$, le poids de jev est gelé et des requêtes-canaris cachées sont injectées. Le juge ne peut donc jamais constituer seul la récompense.

3. **Duel décisif ($H_A\perp H_B$)**
- **Hypothèses** : $H_A$ : LAGAS bat les essaims de contrôle à budget égal. $H_B$ : le gain provient du seul volume d'appels.
- **Bras testés**, tous à 120 USD : (i) LAGAS ; (ii) topologie fixe (arbre de profondeur 3) ; (iii) spawn i.i.d. aléatoire ; (iv) contrôle négatif : LAGAS alimenté par un signal jev permuté.
- **Corpus** : 300 tâches de revue comportant des citations fausses implantées et des dérives de consigne implantées à une profondeur connue.
- **Métriques** :
  - précision vérifiée par USD ;
  - délai de détection de dérive $\mathbb E[\tau-\nu]$ ;
  - $\hat\rho$ inter-agents sur les erreurs.
- **Règle de décision** : un SPRT préenregistré par paires ($\alpha=\beta=0{,}05$). $H_A$ n'est acceptée que si (i) bat (ii) et (iii), et si (iv) s'effondre au niveau de (iii), ce qui prouve que le gain vient du signal et non du volume d'appels.
