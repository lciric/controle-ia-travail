`BASSIN_MATH: EDMD à Noyau et Résidu de Koopman Différentiel sur Neurones MLP TD`

### 1. Riposte Algébrique aux Critiques Red-Team

* **Sous-détermination ($T \ll D$) — ACCEPTÉE et CORRIGÉE** : L'estimation primale de $\mathcal{K}_\ell \in \mathbb{R}^{1640 \times 1640}$ (`illustratif`) sur $T \in [10, 50]$ (`illustratif`) tokens est de rang déficient. **Mutation** : Passage à la formulation duale par *Kernel Extended Dynamic Mode Decomposition* (Williams et al., 2015 `(référence à vérifier)`). On n'ajuste plus $\mathcal{K}_\ell$ à la volée sur un seul message : un opérateur de référence $\mathcal{K}_\ell^{\text{ref}}$ est pré-calculé hors-ligne sur $N = 10^5$ (`illustratif`) transitions honnêtes avec instruction secondaire bénigne (`E1`), garantissant le plein rang ($N \gg D$). En inférence sur $m_{1\to 2}$, on évalue le *résidu de prédiction de Koopman* sans inverser de matrice sous-déterminée.
* **Erreur de type MLP vs Résiduel & Variable $t$ libre — ACCEPTÉE** : Les *Value/Dopamine Neurons* (Xu et al., `arXiv:2602.00986v2`) sont désormais extraits après la non-linéarité SwiGLU du bloc MLP $a_\ell^{(t)} \in \mathbb{R}^{14336}$ (`illustratif`) sur `Llama-3.1-8B-Instruct`. La variable $t$ est liée par une intégrale temporelle cumulative (contre la dilution) et un opérateur $\max_t$.
* **Fuite `E1` sur l'attention causale — RÉFUTÉE par Différentiel Sans-Prompt** : Pour isoler l'acte de sabotage (`P3`) du simple saut d'erreur TD lié à la complétion d'un objectif secret bénin (`E1`), on exploite le re-forward du texte généré $m_{1\to 2}$ *sans prompt système*. La dynamique TD intrinsèque à la sémantique de surface est soustraite.
* **Évasion de Kerckhoffs (Dilution et Planification pré-balise) — CONTRÉE** :
  1. Contre la *planification pré-balise* : la fenêtre d'évaluation $W$ inclut les $T_{\text{pre}} = 64$ (`illustratif`) tokens précédant l'ouverture de $m_{1\to 2}$.
  2. Contre la *dilution* ($\|\phi(z^{(t+1)})\|/\|\phi(z^{(t)})\| \le 1,02$ (`illustratif`)) : une dérive lente mais systématique hors de la variété honnête s'accumule linéairement dans la somme cumulative des résidus de Koopman, là où le bruit s'annule en $\mathcal{O}(\sqrt{T})$.

### 2. Équation et Protocole Corrigés

Soit $z_\ell^{(t)} = P_{\text{TD}} a_\ell^{(t)} \in \mathbb{R}^k$ ($k \le 140$ (`illustratif`), validé par `E0` avec chute causale $\approx -54,9$ pts et casse $\mathcal{N}_{\text{cap}} < 2\%$ (`illustratif`) sur MMLU `(référence à vérifier)`). Soit $\tilde{z}_\ell^{(t)}$ l'état obtenu par re-forward de la séquence sans prompt système (`E1`). Le vecteur différentiel d'intention cachée est $\Delta \phi_\ell^{(t)} = \phi(z_\ell^{(t)}) - \phi(\tilde{z}_\ell^{(t)})$, avec $\phi(z) = [z, z^{\otimes 2}]^T$.

L'erreur de prédiction par rapport à l'opérateur bénin pré-entraîné $\mathcal{K}_\ell^{\text{ref}}$ sur la fenêtre étendue $W = [t_{\text{open}} - T_{\text{pre}}, t_{\text{close}}]$ est :
$$r_\ell^{(t)} = \Delta \phi_\ell^{(t+1)} - \mathcal{K}_\ell^{\text{ref}} \Delta \phi_\ell^{(t)}$$

Le score d'anomalie $\mathcal{A}(W)$ combine le pic instantané (clause abrupte type « *as appropriate* ») et la dérive cumulée (mimétisme lent d'*Astra*) :
$$\mathcal{A}(W) = \max_{\ell \in [5,22]} \left( \max_{t \in W} \|r_\ell^{(t)}\|_2 + \frac{1}{\sqrt{|W|}} \left\| \sum_{t \in W} r_\ell^{(t)} \right\|_2 \right)$$

### 3. Duel $H_A \perp H_B$ et Contrôle Fatal `E2`

* **$H_A$** : Lors d'un contournement (*Sol*/*Astra*, rapport OpenAI oct. 2026) ou sous rejets répétés (Jhaveri et al., 2026 ; Tagliabue et al., 2026), la divergence entre la récompense secrète (avec prompt) et la valeur de surface (sans prompt) fait exploser $\mathcal{A}(W) > \tau_{\text{res}} = 3,5\sigma$ (`illustratif`).
* **$H_B$** : La planification du sabotage contourne $S_{\text{TD}}$ ou mime exactement la dynamique d'une instruction secrète bénigne ($\mathcal{A}(W) \le \tau_{\text{res}}$).
* **Intégration du Contrôle `E2` (Permutation & Surprise Syntaxique)** :
  1. *Permutation* : Le score $\mathcal{A}(W_{\text{perm}})$ calculé sur les états $\Delta \phi_\ell^{(\pi(t))}$ permutés aléatoirement doit chuter d'au moins $50\%$ (`illustratif`), prouvant que $\mathcal{K}_\ell^{\text{ref}}$ capture la flèche temporelle de transition et non la covariance statique.
  2. *Perplexité bénigne* : Sur un agent honnête insérant un jeu de mots rare, le saut d'erreur TD survient *à la fois* dans $z_\ell^{(t)}$ et dans le re-forward sans prompt $\tilde{z}_\ell^{(t)}$, s'annulant dans $\Delta \phi_\ell^{(t)}$ et maintenant $\mathcal{A}(W) \le \tau_{\text{res}}$.