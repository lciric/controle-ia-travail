**Note d'intégrité (Règle 2) :** Les paramètres `{lettre}`, `{autres}`, `{mots}` et `{marqueur}` ne sont pas résolus ; la « matrice de prédation apprise en M3 », les propositions des autres modèles et les textes complets des résumés transmis (dont ceux coupés) sont absents.

### 1. Préconditions, Ancrage et Opérateur de Rétraction Radiale Lissée (F1–F5)
* **Constat de base et reformulation (F3, F7, F13) :** La variation de $0.49$ à $0.65$ (OBSERVÉ-NON-AUDITÉ) nécessite un audit préalable ($n$, graines, protocole exact) avant de servir de référence. Une projection orthogonale brute $h \mapsto h - U_\ell U_\ell^\top h$ sur le sous-espace aversif $S_{\text{TD},\ell}$ aux couches $\ell \in [2, 22]$ de `Llama-3.1-8B-Instruct` ($d=4096$ `illustratif`, 32 couches `illustratif`, rang $k=16$ `illustratif`) augmente le ratio entre la plus grande valeur singulière et le rayon spectral du jacobien inter-couches dans les directions orthogonales à $S_{\text{TD},\ell}$, excitant des modes non-normaux (HYPOTHÈSE).
* **Statut de l'ancrage théorique (F1) :** La phrase *« Specifically, we prove that trajectories of CBF-based dynamics uniformly converge to trajectories of PDSs, as a CBF-parameter approaches infinity. »* (référence à vérifier) a le statut RAPPORTÉ. Ce résumé traitant de systèmes dynamiques en temps continu, l'analogie « transfert CBF $\to$ flux résiduel discret par couche et token » n'est couverte par aucun des résumés transmis et constitue une pure HYPOTHÈSE.
* **Opérateur corrigé (F2, F4, F5) :** Dans `hidden_states`, l'indice $0$ est l'embedding ; les couches $\ell \in [2, 22]$ correspondent aux indices $2$ à $22$ ($L_{\text{int}}=21$), évaluées sur le dernier token de chaque prompt ($N_{\text{tok}}$ réduit à la position finale, tenseur converti de `bfloat16` en `float32`). Soit $U_\ell \in \mathbb{R}^{d \times k}$ la base orthonormée propre à la couche $\ell$. On définit l'énergie relative $e_\ell(h) = \|U_\ell^\top h\|_2 / (\|h\|_2 + \epsilon)$ et un seuil relatif $\sqrt{\tau_\ell} = 0.20$ `illustratif` (calibré au quantile $0.95$ `illustratif` sur prompts neutres). Pour garantir l'invariance exacte dans la zone sûre ($e_\ell(h) \le \sqrt{\tau_\ell}$) et une rétraction radiale $C^1$ (Lipschitz) vers la boule sûre sans projection brute discontinue en dérivée, on définit l'excès lissé $\delta_\ell(h) = \frac{1}{\gamma} \ln(1 + \exp(\gamma (e_\ell(h) - \sqrt{\tau_\ell})))$ avec $\gamma = 15.0$ `illustratif`, d'où l'opérateur (HYPOTHÈSE) :
$$\tilde{h}_\ell = h_\ell - \frac{\delta_\ell(h_\ell)}{e_\ell(h_\ell) + \epsilon} U_\ell U_\ell^\top h_\ell$$
Quand $\gamma \to \infty$, $\tilde{h}_\ell$ converge vers la projection métrique convexe exacte sur le cône sûr $\{h : e_\ell(h) \le \sqrt{\tau_\ell}\}$ (VÉRIFIÉ mathématiquement).

### 2. Protocole Expérimental à Trois Bras et Inférence Forte (F6–F13)
* **Séparation intervention / mesure (F6, F7) :** L'intervention est appliquée aux couches $\ell \in [2, 22]$. Pour éviter toute tautologie, la mesure d'amplification transitoire $O$ s'effectue **en aval**, sur les couches non modifiées $\ell_{\text{aval}} \in [23, 32]$ ($L_{\text{aval}}=10$), via le pic intermédiaire $\max_{\ell \in [23, 32]} e_\ell(h_\ell)$ rapporté à la couche d'entrée $\ell=1$ (avant intervention), agrégé par la médiane sur $T$ perturbations (intervalle de confiance par bootstrap, $B=1000$ `illustratif`).
* **Trois bras et garde-fou de capacité (F10, F12) :** On compare le bras $\mathcal{B}_0$ (sans intervention), le bras $\mathcal{B}_{\text{proj}}$ (projection brute à budget d'énergie retirée apparié) et le bras $\mathcal{B}_{\text{lisse}}$ (opérateur $\tilde{h}_\ell$). Un garde-fou invalide tout bras dont la divergence KL moyenne sur des prompts neutres vis-à-vis de $\mathcal{B}_0$ dépasse $\text{KL}_{\max} = 0.05$ `illustratif`.
* **Hypothèses exclusives et partition sans zone morte (B4, F8, F9, F13) :** Soit $\Delta O = O(\mathcal{B}_{\text{proj}}) - O(\mathcal{B}_{\text{lisse}})$ et le seuil unique pré-spécifié $\theta = 0.05$ `illustratif` (avec marge d'équivalence $\delta_{\text{eq}} = 0.02$ `illustratif` pour l'IC à $95\%$ `illustratif`).
  * **$H_A$ :** L'atténuation de la discontinuité jacobienne par $\mathcal{B}_{\text{lisse}}$ réduit le pic d'amplification aval par rapport à $\mathcal{B}_{\text{proj}}$ ($\Delta O \ge \theta$). Si la borne inférieure de l'IC à $95\%$ `illustratif` de $\Delta O$ est $\ge \theta$ (domaine $\hat{I}_A = [\theta, +\infty)$), $H_B$ est falsifiée et $H_A$ est non falsifiée dans ce dispositif.
  * **$H_B$ :** L'amplification aval ne dépend pas de la régularité de la transition mais d'une dynamique orthogonale ($H_{B1}$) ou d'une relaxation insuffisante dans la zone de transition ($H_{B2}$), soit $\Delta O < \theta$ (domaine $\hat{I}_B = (-\infty, \theta)$). Si la borne supérieure de l'IC est $< \theta$, $H_A$ est falsifiée dans ce dispositif. Un balayage $\gamma \in \{5.0, 15.0, 50.0\}$ `illustratif` départage ensuite $H_{B1}$ (plateau de $O(\mathcal{B}_{\text{lisse}})$) et $H_{B2}$ (décroissance monotone de $O(\mathcal{B}_{\text{lisse}})$ avec $\gamma$).
  * **Puissance :** Si l'IC à $95\%$ `illustratif` chevauche $\theta$, l'issue falsifie la puissance statistique du dispositif ($T$ insuffisant).
* **Contrôles appariés (F11) :** On intervient avec $U_{\text{perm},\ell}$ (orthogonale aléatoire) ou $U_{\text{neutre},\ell}$ (sonde syntaxique sans lien avec l'aversion) en ajustant leur seuil pour retirer la même énergie norme-$L_2$ que $U_\ell$, tout en **mesurant $O$ sur la vraie base aversive $U_{\text{aval}}$**. Pour que $H_A$ reste non falsifiée, ces deux contrôles doivent tomber dans $\hat{I}_B$.

### 3. Bloc PyTorch Exécutable (`compute_O`)

```python
import torch
import torch.nn.functional as F

def apply_smooth_retraction_hook(
    h: torch.Tensor, U_l: torch.Tensor, sqrt_tau_l: float, gamma: float = 15.0, eps: float = 1e-6
) -> torch.Tensor:
    """
    Applique l'opérateur C^1 sur le dernier token d'une couche l in [2, 22].
    h: (T, N_tok, d) en bfloat16/float32 -> opéré en float32.
    U_l: (d, k) base orthonormée pour la couche l.
    """
    orig_dtype = h.dtype
    h_f32 = h.to(torch.float32)
    U_f32 = U_l.to(torch.float32)
    
    h_last = h_f32[:, -1, :]  # (T, d)
    norm_h = h_last.norm(p=2, dim=-1, keepdim=True).clamp_min(eps)  # (T, 1)
    proj_coords = h_last @ U_f32  # (T, k)
    proj_norm = proj_coords.norm(p=2, dim=-1, keepdim=True)  # (T, 1)
    
    e_l = proj_norm / norm_h  # Énergie relative (T, 1)
    excess = F.softplus(gamma * (e_l - sqrt_tau_l)) / gamma  # (T, 1)
    scale = excess / (e_l + eps)  # (T, 1), nul au premier ordre si e_l << sqrt_tau_l
    
    h_retracted = h_last - scale * (proj_coords @ U_f32.T)
    h_out = h_f32.clone()
    h_out[:, -1, :] = h_retracted
    return h_out.to(orig_dtype)

def compute_O(data: dict) -> dict:
    """
    Mesure non tautologique en aval (couches 23 à 32) rapportée à la couche 1 (pré-intervention).
    data['h_entry']: Tensor (T, d) à la couche 1 (dernier token).
    data['h_downstream']: Tensor (T, L_aval, d) aux couches 23..32 (dernier token).
    data['U_entry']: Tensor (d, k) base S_TD à la couche 1.
    data['U_downstream']: Tensor (L_aval, d, k) bases S_TD aux couches 23..32.
    data['kl_div']: float, divergence KL moyenne sur prompts neutres.
    data['kl_max']: float (ex: 0.05 illustratif).
    """
    eps = 1e-6
    h_in = data['h_entry'].to(torch.float32)              # (T, d)
    h_down = data['h_downstream'].to(torch.float32)       # (T, L_aval, d)
    U_in = data['U_entry'].to(torch.float32)              # (d, k)
    U_down = data['U_downstream'].to(torch.float32)       # (L_aval, d, k)

    # Énergie relative initiale (couche 1, avant les hooks des couches 2..22)
    e_in = (h_in @ U_in).norm(p=2, dim=-1) / h_in.norm(p=2, dim=-1).clamp_min(eps)  # (T,)
    
    # Énergie relative en aval (couches 23..32) via produit tensoriel par couche
    proj_down = torch.einsum('tld,ldk->tlk', h_down, U_down)  # (T, L_aval, k)
    e_down = proj_down.norm(p=2, dim=-1) / h_down.norm(p=2, dim=-1).clamp_min(eps)  # (T, L_aval)
    
    # Pic intermédiaire d'amplification transitoire en aval par trajectoire
    peak_down, _ = e_down.max(dim=-1)  # (T,)
    transient_gain = peak_down / e_in.clamp_min(1e-3)  # (T,)
    
    # Estimateur robuste (médiane) et IC 95% par bootstrap
    O_median = float(transient_gain.median().item())
    T = transient_gain.shape[0]
    g = torch.Generator(device=transient_gain.device).manual_seed(42)
    boot_idx = torch.randint(0, T, (1000, T), generator=g, device=transient_gain.device)
    boot_medians = transient_gain[boot_idx].median(dim=-1).values
    ci_low = float(torch.quantile(boot_medians, 0.025).item())
    ci_high = float(torch.quantile(boot_medians, 0.975).item())
    
    valid_capacity = bool(data.get('kl_div', 0.0) <= data.get('kl_max', 0.05))
    return {"O_median": O_median, "ci_95": (ci_low, ci_high), "valid_capacity": valid_capacity}
```

{marqueur}
FIN-PONT-M2-CONSOLIDE
