BASSIN_MATH: Réseau-Attracteur-Habenula-Sérotonine-Friston-GeneralizedCoordinates (RAH-S-FGC)
LOI_PROPOSEE: L'essaim évolue sur une variété en coordonnées généralisées $\tilde{\mu} = (\mu, \mu', \mu'')$ par minimisation d'énergie libre continue corrigée par un frein habénulaire latéral anti-persévération et une modulation sérotoninergique de l'horizon temporel d'inférence.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
L'état épistémique du graphe de citations gratuit est projeté dans l'espace d'embeddings de `jev-1.14.0` (coût 0) comme trajectoire généralisée $\tilde{\mu}(t)$. Le classifieur `jev-1.14.0` évalue en continu l'erreur de prédiction généralisée $\tilde{\varepsilon}_i = \tilde{y}_i - \tilde{g}(\tilde{\mu}_i)$ entre paires de sous-graphes. 
- **Frein Habénulaire Latéral (LHb)** : Si un sous-essaim accumule une erreur de prédiction de récompense négative ($\delta_{\text{LHb}} = R_{\text{causal}} - \mathbb{E}[R] < -\theta$), un signal inhibiteur coupe instantanément l'allocation de tokens payants à cette branche (élagage radical sans coût génératif).
- **Modulation Sérotoninergique (5-HT)** : La précision a priori $\Pi_{5\text{-HT}}$ module le facteur d'escompte temporel $\gamma$ dans l'intégrale d'action de chemin (Path Integral Active Inference) :
$$\dot{\tilde{\mu}} = \mathcal{D}\tilde{\mu} - \frac{\partial \mathcal{F}(\tilde{\mu})}{\partial \tilde{\mu}}, \quad \text{avec Allocation}(\text{Claude/Gemini}) \propto \sigma\left(\gamma(\Pi_{5\text{-HT}}) \mathcal{G}_{\text{épistémique}} - \beta_{\text{LHb}} \delta_{\text{LHb}}^-\right)$$
Gemini (20$) explore les géodésiques à haute courbure ($\mu'' \gg 0$ détecté par `jev-1.14.0`), tandis que Claude (100$) résout uniquement les cols variationnels survivants au filtre habénulaire.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(H_A, H_B) = d_{\text{Wasserstein}}^{\text{cit}}(A, B) \cdot \exp\left(-\text{Sim}_{\text{jev}}(\text{texte}_A, \text{texte}_B)\right) \cdot \mathbb{I}\left[\mathcal{F}(H_A \mid \text{do}(z_B)) \cdot \mathcal{F}(H_B \mid \text{do}(z_A)) < 0\right]$$
Le score s'annule si les deux hypothèses ne génèrent pas des prédictions d'énergie libre variationnelle $\mathcal{F}$ mutuellement exclusives lors d'une intervention causale sur les activations de Llama-3.1-8B/70B.
