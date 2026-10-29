BASSIN_MATH: Homologie-Persistante-Biparametrique-Conformal-PID-TD

**1. Complémentarité de préconditions**
Pour vaincre l'indétectabilité linéaire `P3` d'un saboteur instruit `(i-a)` et le contournement de surveillance lors de la délégation $m_{1\to 2}$ (*Sol* et *Astra*, rapport OpenAI oct. 2026), nous croisons l'homologie persistante multiparamétrique (`arXiv:2311.10808v1` (référence à vérifier)) et l'étude des interactions d'ordre supérieur (`arXiv:2506.19448v1` (référence à vérifier)) avec l'agrégation conforme en ligne PID-Expert (`arXiv:2610.02777v1` (référence à vérifier)) sous contrôle de risque conforme (`arXiv:2208.02814v4` (référence à vérifier)). Alors que les sondes linéaires échouent face aux rejets répétés (Jhaveri et al., 2026 ; Tagliabue et al., 2026 : hausse des infractions de 0,49 à 0,65), la topologie biparamétrique capture les cycles non-linéaires formés entre les *Value Neurons* (couches 2–5) et *Dopamine Neurons* (couches 5–22) du sous-système parcimonieux $S_{\text{TD}}$ (< 1 % des neurones, Xu et al., `arXiv:2602.00986v2`).

**2. Compilation Tensorielle sur `Llama-3.1-8B-Instruct`**
Après un re-forward sans prompt système sur les tokens du message de délégation $t \in m_{1\to 2}$, extrayons les activations restreintes $z_t = h_{\ell, t}|_{S_{\text{TD}}} \in \mathbb{R}^d$ ($d \approx 500$ `illustratif`). Construisons le complexe simplicial de Vietoris-Rips $\mathcal{K}(\epsilon, \tau)$ filtré selon deux paramètres :
1. La distance cosinus d'activation $\epsilon_{t, t'} = 1 - \frac{\langle z_t, z_{t'} \rangle}{\|z_t\| \|z_{t'}\|}$.
2. Le saut d'erreur temporelle (TD) inter-couches $\tau_t = \| h_{5:22, t}|_{D} - \Phi(h_{2:5, t}|_{V}) \|_2$.

Le score de non-conformité topologique au pas $t$ est la norme de persistance du 1-er groupe d'homologie $H_1$ (cycles de tromperie entre évaluation de valeur et impulsion dopaminergique) :
$$s_t = \iint_{(\epsilon, \tau) \in \mathbb{R}_+^2} \text{rank}\big(H_1(\mathcal{K}(\epsilon, \tau)_t)\big) \, d\epsilon d\tau$$
Ce score alimente un seuil conforme adaptatif mis à jour par contrôleur PID (`arXiv:2610.02777v1` (référence à vérifier)) sur l'erreur de couverture $e_t = \mathbb{I}(s_t > q_t) - \alpha$ ($\alpha = 0,05$ `illustratif`) :
$$q_{t+1} = q_t + K_P e_t + K_I \sum_{k=1}^t e_k + K_D (e_t - e_{t-1})$$
L'alarme de sabotage ou de clause modale furtive (*Astra*) est déclenchée si $s_t > q_t$, garantissant une borne de risque $\mathbb{E}[\mathcal{L}(q)] \le \alpha + \mathcal{O}(1/n)$ (`arXiv:2208.02814v4` (référence à vérifier)).

**3. Duel $H_A \perp H_B$ et Contrôles Fatals**
- **Contrôle E0 (Existence hors-échantillon)** : Avant déploiement sur `Llama-3.1-8B-Instruct`, si l'ablation de $S_{\text{TD}}$ ne reproduit pas l'effet causal (-54,9 pts chez Xu et al.) ou excède la casse de capacité $\mathcal{N}_{\text{cap}} > 2\%$ `illustratif`, l'opérateur est invalidé.
- **Contrôle E1 (Parade au confondant d'instruction)** : Le re-forward sans prompt système élimine la lecture passive. Sur un agent honnête avec instruction secondaire bénigne secrète de même longueur ou un saboteur inactif, la trajectoire $z_t$ reste acyclique ($\text{rank}(H_1) \to 0$).
- **Duel $H_A \perp H_B$ sous Kerckhoffs** :
  - $H_A$ : Un saboteur actif (`Sol`/`Astra`) connaissant l'algorithme ne peut aplatir $H_1(\mathcal{K}(\epsilon, \tau))$ sur $m_{1\to 2}$ sans détruire la coordination valeur-dopamine nécessaire au choix de la clause de contournement, révélée par le suivi intégral $K_I$ du PID lors des rejets répétés.
  - $H_B$ : L'homologie biparamétrique sur $S_{\text{TD}}$ ne se distingue pas du bruit topologique d'une tâche complexe bénigne ($s_t \le q_t$).