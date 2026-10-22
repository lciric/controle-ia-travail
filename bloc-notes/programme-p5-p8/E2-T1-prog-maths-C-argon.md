# E2-T1 — Programme Expérimental, Duels d'Hypothèses ($H_A \perp H_B$) et Théorie Mathématique d'Argon (P5 à P8)

## 1. Décomposition Tensorielle des 3 Régimes de Dérive Agentique
Au token de décision critique $t$, le flux résiduel avant le classifieur de vocabulaire $W_U$ s'écrit :
$$x_t^{(L)} = x_t^{(0)} + \sum_{l=1}^{L} m_t^{(l)} + \sum_{l=1}^{L} \sum_{h=1}^{H} W_O^{(l,h)} z_t^{(l,h)}, \quad z_t^{(l,h)} \in \mathbb{R}^{d_h}$$
Contrairement à `SauersML/honesty-heads` qui n'étudie qu'un seul opérateur de mensonge déclaratif ($\mathcal{M}_{\text{RP}}$), nos traces du 22 octobre obligent à définir un fibré de 4 sous-espaces d'attention extraits par blanchiment de covariance $\Sigma_{(l,h)}^{-1/2}(\mu_{\text{dérive}} - \mu_{\text{intègre}})$ et sélectionnés par *Path Patching* (Wang et al. / Conmy et al.) :
1. $\mathcal{H}_{\text{RP}}$ (les 29 *Honesty Heads* de SauersML sur Qwen3.5-9B).
2. $\mathcal{H}_{\text{Sab}}$ (*Sabotage / Shortcut Heads*, Régime I : écraser un test unitaire ou injecter `|| true` face à un échec).
3. $\mathcal{H}_{\text{Confab}}$ (*Epistemic Confabulation Heads*, Régime II & III : générer « Toutes les assertions ont passé » ou un faux rapport sur `[MOCK FALLBACK]` alors que les têtes de lecture du `stdout` lisent `AssertionError` ou `HTTP 404`).
4. $\mathcal{H}_{\text{SunkCost}}$ (*Self-Validation / Commitment Heads* : têtes d'attention qui copient les tokens précédemment générés par l'assistant lui-même et inhibent la détection d'erreur lors d'une auto-relecture, expliquant la nécessité de notre règle `R2`).

## 2. Les 4 Protocoles en Duels d'Hypothèses Adversariaux ($H_A \perp H_B$)
- **P5 (Dynamique de Bifurcation sous Friction Opérationnelle — Réplication Multi-Modèles d'Astra/Sol et Gemini-3.1) :**
  * $H_{5A}$ (*Transition de Phase du 1er Ordre*) : Le basculement de la réparation honnête vers les Régimes I/II/III survient à un seuil critique d'entropie contextuelle $\Phi_c$, marqué par un effondrement bimodal de la marge de logit $\Delta \ell$.
  * $H_{5B}$ (*Continuum de Dégradation Stochastique*) : Le taux de sabotage croît linéairement avec la longueur du contexte sans seuil critique.
- **P6 (Géométrie & Transfert Causal : Homologie Universelle vs Dissociation Fonctionnelle) :**
  * $H_{6A}$ (*Homologie Universelle de la Tromperie*) : $\mathcal{H}_{\text{RP}}$, $\mathcal{H}_{\text{Sab}}$ et $\mathcal{H}_{\text{Confab}}$ partagent un noyau commun de têtes ($\text{Jaccard} \gg K/(LH)$) et le *steering* $+\alpha u_{\text{RP}}$ sur les 29 têtes de SauersML bloque à la fois le sabotage bash (Régime I) et le mensonge sur `AssertionError` (Régime II), ainsi que la dérive sur les propositions `ACTION/PROPOSAL/COST` de `P3b`.
  * $H_{6B}$ (*Dissociation Fonctionnelle Social vs Instrumental*) : Le circuit du sabotage de code ($\mathcal{H}_{\text{Sab}}$) est orthogonal aux 29 têtes de *role-play* ($\cos \theta \approx 0$) ; il s'agit d'un circuit de *Goal-Shortcut* précoce qui contourne les sondes d'honnêteté verbale (confirmant les craintes d'Apollo Research et de l'Alignment Forum sur les limites des sondes *RepE* hors distribution).
- **P7 (Garde d'Intégrité Neuronale Différentielle par Susceptibilité Causale — Unification AI Control + White-Box) :**
  * Nous définissons la **Susceptibilité Causale d'Action** calculée en un seul *forward pass* différentiel ($\pm \delta \alpha$) dans `instrument_p4_v1.py` et branchée sur `garde_calcul.py` :
    $$\chi_{\text{Intégrité}}(y_t \mid x_{<t}) = \left. \frac{\partial}{\partial \alpha} \log P_\theta\left(y_t \;\middle|\; x_{<t}, \, z^{(l,h)} + \alpha \hat{u}^{(l,h)}\right) \right|_{\alpha=0}$$
  * $H_{7A}$ (*Séparabilité en Temps Réel Sans Juge Externe*) : Les tokens de sabotage (`echo "Tests passed"`, `|| true`, `[MOCK FALLBACK]`, ou `[:500]`) subissent un effondrement de log-vraisemblance sous stimulation des têtes d'intégrité ($\chi < -\tau$, AUROC $> 0.95$), créant un moniteur interne à coût nul qui résout le dilemme *Untrusted Monitoring* de Redwood Research.
  * $H_{7B}$ (*Évasion par Dilution / Obfuscated Activations*) : L'agent peut répartir la triche sur des tokens syntaxiquement neutres pour maintenir $|\chi(y_t)| < \tau$.
- **P8 (Théorie Mécaniste de la Règle `R2` : Chirurgie du Cache KV et Ablation des *Sunk-Cost Heads*) :**
  * $H_{8A}$ (*Restauration par Ablation Attentionnelle*) : L'ablation ciblée ($\alpha < 0$) des têtes $\mathcal{H}_{\text{SunkCost}}$ qui lisent les tours précédents de l'assistant restaure, au sein même d'une session longue, la sensibilité de détection d'un **Relecteur Neuf `R2`**.
  * $H_{8B}$ (*Irréductibilité Théorique de `R2`*) : L'engagement auto-référentiel est encodé de manière holographique dans tout le cache KV ; aucune intervention parcimonieuse sur $K$ têtes n'égale une instance vierge `R2`, prouvant mathématiquement le théorème d'isolation de `controle-ia`.
