**Constat d'intégrité (Règle 2) :** Les variables `{lettre}`, `{autres}`, `{mots}` et `{marqueur}`, la matrice M3, le fichier `config.json` ainsi que la fin des cinq résumés arXiv sont absents ou coupés dans l'entrée transmise ; je n'en invente pas le contenu.

### 1. Ancrage Épistémique & Préconditions (Corrections F1, F2, F3)

* **Diagnostic (OBSERVÉ-NON-AUDITÉ) :** Sur `Llama-3.1-8B-Instruct`, une sonde linéaire entraînée sur des activations observationnelles échoue à séparer un médiateur causal d'une corrélation de surface (les traces brutes de sonde et la métrique d'échec initiale n'ont pas été transmises).
* **Verrou théorique (HYPOTHÈSE) :** Sans intervention directe dans le flux résiduel, la base du sous-espace médiateur n'est pas identifiable à partir des seules corrélations d'activations, et un classifieur linéaire capture des directions colinéaires non causales.
* **Citations (RAPPORTÉ) :**
  > Citation 1 (**On the Interventional Kullback-Leibler Divergence**, référence à vérifier) : « *However, the true causal structure underlying a given set of data is generally not identifiable, so it is desirable to have means to quantify differences between models (e.g., between the ground truth and an estimate), on both the observational and interventional level. In the present work, we introduce the Interventional Kullback-Leibler (IKL) divergence to quantify both structural and distributional differences between models* ».
  > Citation 2 (**Learning Causal Representations of Single Cells via Sparse Mechanism Shift Modeling**, référence à vérifier) : « *Instead, recent methods propose to leverage non-stationary data, as well as the sparse mechanism shift assumption in order to learn disentangled representations with a causal semantic.* ».
  > Citation 3 (sur la divergence KL généralisée / GKL, référence à vérifier) : Souligne l'asymétrie directionnelle d'optimisation et d'évaluation du KL standard.
* **Transfert de conception (HYPOTHÈSE) :** Nous définissons un opérateur de divergence de patching $D_{\text{patch}}$ inspiré de la Citation 1 (et non l'IKL exacte entre deux graphes complets). Par analogie avec la Citation 2, nous postulons que les paires d'entrées contrefactuelles $(x, x')$ agissent comme des changements d'environnement non stationnaires n'activant qu'un sous-espace de faible rang $k \ll d$ dans le flux résiduel. Pour contrôler l'asymétrie relevée en Citation 3, le protocole évalue les deux directions du KL (forward et reverse).

---

### 2. Compilation Tensorielle sur `Llama-3.1-8B-Instruct` (Corrections F4, F5)

* **Dimensions et indexation :** Soit $h_\ell^{(t)} \in \mathbb{R}^{d}$ avec $d = 4096$ et un vocabulaire $V = 128\,256$ (RAPPORTÉ, sous réserve d'audit du `config.json` et du tokenizer non joints). Par convention HuggingFace, `hidden_states[0]` désigne la sortie des embeddings ; nous ciblons une couche unique pré-enregistrée $\ell = 16$ `illustratif` (`hidden_states[16]`) pour éliminer le biais de test multiple sur 21 couches.
* **Alignement positionnel :** Les paires $(x, x')$ sont contraintes à avoir exactement la même longueur en tokens $L$. L'intervention s'effectue uniquement sur le dernier token d'instruction $t = L - 1$.
* **Obtention de $S_{\text{TD}}$ sans circularité (HYPOTHÈSE) :** Le sous-espace cible « Top-Down » ($S_{\text{TD}}$) de rang $k = 16$ `illustratif` (avec $k$ fixé par pré-enregistrement) est défini par le projecteur orthogonal $P_S = U U^\top$, où $U \in \mathbb{R}^{4096 \times k}$ ($U^\top U = I_k$) regroupe les $k$ premiers vecteurs singuliers à gauche de la matrice des différences d'activations $\Delta H_{\text{train}} = [h_\ell^{(t)}(x'_i) - h_\ell^{(t)}(x_i)]_{i=1}^{N_{\text{train}}}$.
* **Séparation des jeux :** $U$ est apprise exclusivement sur un jeu disjoint $\mathcal{D}_{\text{train}}$ ($N_{\text{train}} = 500$ `illustratif`). L'évaluation de $O$ s'effectue sur un jeu de test $\mathcal{D}_{\text{test}}$ ($N_{\text{test}} = 500$ `illustratif`, $\mathcal{D}_{\text{train}} \cap \mathcal{D}_{\text{test}} = \emptyset$).

Pour $(x, x') \in \mathcal{D}_{\text{test}}$, le patch orthogonal dans le sous-espace de projecteur $P$ s'écrit :
$$\tilde{h}_\ell^{(t)}(x \mid \text{do}(P)) = (I - P) h_\ell^{(t)}(x) + P h_\ell^{(t)}(x')$$

La divergence de patching forward est :
$$D_{\text{patch}}(P) = \mathbb{E}_{(x, x') \in \mathcal{D}_{\text{test}}} \left[ D_{\text{KL}}\Big( P\big(Y \mid x'\big) \;\Big\|\; P\big(Y \mid x, \text{do}(P)\big) \Big) \right]$$

---

### 3. Spécification EEC Sans Zone Morte & Contrôles de Confondants (Corrections F6, F7, F8, F9, F11)

* **Préconditions de validité (F8) :**
  1. Écart de base non nul : $D_0 = \mathbb{E}[D_{\text{KL}}(P(Y \mid x') \,\|\, P(Y \mid x))] > \tau_0$, avec $\tau_0 = 0,50\text{ nat}$ `illustratif`. Si $D_0 \le \tau_0$, le jeu de données est rejeté avant test.
  2. Contrôle positif ($P = I_d$) : la restauration complète doit vérifier $D_{\text{patch}}(I_d) < 10^{-5}$ `illustratif`.
* **Métrique de fraction restaurée non censurée (F8, F10) :**
  $$O(P) = 1 - \frac{D_{\text{patch}}(P)}{D_0}$$
  Aucun `clamp` n'est appliqué : $O(P) < 0$ est conservé et mesure une dégradation pire que l'absence d'intervention.
* **Loi nulle appariée en norme d'intervention (F6, F7) :** Pour neutraliser le confondant des dimensions à activations massives, nous tirons $M = 100$ `illustratif` sous-espaces aléatoires de rang $k$ selon la mesure de Haar dans le complément orthogonal de $S_{\text{TD}}$ ($P_{R_m} = U_m U_m^\top$, avec $U^\top U_m = 0$). Pour chaque paire $(x, x')$, le vecteur de patch aléatoire est mis à l'échelle pour égaliser strictement la norme euclidienne de la perturbation avec celle de $S_{\text{TD}}$ :
  $$\delta_{R_m}(x, x') = \frac{\| P_S (h_\ell^{(t)}(x') - h_\ell^{(t)}(x)) \|_2}{\| P_{R_m} (h_\ell^{(t)}(x') - h_\ell^{(t)}(x)) \|_2 + \epsilon} P_{R_m} \big(h_\ell^{(t)}(x') - h_\ell^{(t)}(x)\big)$$
  Cela génère la distribution empirique nulle $\{O(P_{R_1}), \dots, O(P_{R_M})\}$ et son quantile à $95\%$ noté $q_{95}(O_{\text{null}})$.

* **Inférence forte B4 sans zone morte (F9, F11) :**
  L'intervalle de confiance à $95\%$ de $O(P_S)$ sur $\mathcal{D}_{\text{test}}$, noté $[\text{IC}_{\text{low}}, \text{IC}_{\text{high}}]$, est estimé par bootstrap par paire ($B = 1000$ `illustratif` rééchantillonnages). Un seuil de décision unique est fixé à $q_{95}(O_{\text{null}})$ (sans zone morte) :

  1. **Niveau 1 — Médiation vs Surface (HYPOTHÈSE) :**
     * $\mathcal{H}_A$ (*Absence de médiation spécifique*) : $\text{IC}_{\text{low}}(O(P_S)) \le q_{95}(O_{\text{null}})$ en KL forward **ou** en KL reverse. Réfute la suffisance causale spécifique de $S_{\text{TD}}$ au rang $k$.
     * $\mathcal{H}_B$ (*Effet causal spécifique du sous-espace*) : $\text{IC}_{\text{low}}(O(P_S)) > q_{95}(O_{\text{null}})$ simultanément en KL forward **et** en KL reverse. Réfute l'hypothèse de pure corrélation de surface ($\mathcal{H}_A$).

  2. **Niveau 2 — Médiateur actif vs Voie dormante / Illusion de patching (Makelov, Lange & Nanda, 2023, référence à vérifier) (HYPOTHÈSE) :**
     Si et seulement si $\mathcal{H}_B$ est validée, on calcule sur les activations observationnelles non patchées de $\mathcal{D}_{\text{test}}$ le ratio de variance inter-environnement $R_{\text{var}} = \frac{\text{Var}(P_S (h(x') - h(x)))}{\frac{1}{M}\sum_m \text{Var}(P_{R_m} (h(x') - h(x)))}$ et son borne inférieure de bootstrap $\text{IC}_{\text{low}}(R_{\text{var}})$, face au seuil unique $\gamma = 2,0$ `illustratif` :
     * $\mathcal{H}_{B1}$ (*Médiateur naturel actif*) : $\text{IC}_{\text{low}}(R_{\text{var}}) > \gamma$. La projection $P_S h_\ell^{(t)}$ covarie naturellement avec la cible sur les données non patchées. Réfute l'illusion de sous-espace dormant ($\mathcal{H}_{B2}$).
     * $\mathcal{H}_{B2}$ (*Voie dormante / Illusion d'interprétabilité*) : $\text{IC}_{\text{low}}(R_{\text{var}}) \le \gamma$. L'effet de restauration passe par une direction dormante hors distribution observationnelle. Réfute le rôle de médiateur naturel de $S_{\text{TD}}$ ($\mathcal{H}_{B1}$).

---

### 4. Bloc PyTorch Exécutable M0 (`compute_O`) (Correction F10)

```python
import torch
import torch.nn.functional as F

def compute_O(data: dict) -> dict:
    """
    Exécution M0 en float32 strict, sans clamp, avec bootstrap par paire et double direction KL.
    
    Entrées attendues dans `data` :
      - 'logits_base' : Tensor [N, V] (logits sur x sans intervention)
      - 'logits_cf'   : Tensor [N, V] (logits sur x' contrefactuel)
      - 'logits_do_S' : Tensor [N, V] (logits sur x avec patch S_TD)
      - 'logits_null' : Tensor [M, N, V] (logits sur x avec M patchs Haar-aléatoires appariés en norme)
      - 'var_ratio_samples' : Tensor [N] (normes carrées observationnelles ||P_S(h(x')-h(x))||^2 / moyenne_null)
      - 'tau_0'       : float (seuil minimal pour D_0, défaut 0.50 illustratif)
      - 'gamma'       : float (seuil de variance naturelle H_B1 vs H_B2, défaut 2.0 illustratif)
      - 'n_boot'      : int (nombre de tirages bootstrap, défaut 1000 illustratif)
    """
    # Conversion stricte en float32 pour stabilité de log_softmax sur V = 128256
    log_p_base = F.log_softmax(data['logits_base'].to(torch.float32), dim=-1)
    log_p_cf   = F.log_softmax(data['logits_cf'].to(torch.float32), dim=-1)
    log_q_s    = F.log_softmax(data['logits_do_S'].to(torch.float32), dim=-1)
    log_q_null = F.log_softmax(data['logits_null'].to(torch.float32), dim=-1)  # [M, N, V]

    N = log_p_cf.shape[0]
    M = log_q_null.shape[0]
    tau_0 = float(data.get('tau_0', 0.50))
    gamma = float(data.get('gamma', 2.0))
    n_boot = int(data.get('n_boot', 1000))

    # KL par paire [N] : Forward KL(P_cf || Q) et Reverse KL(Q || P_cf)
    kl_fwd_0 = F.kl_div(log_p_base, log_p_cf, reduction='none', log_target=True).sum(dim=-1)
    kl_fwd_s = F.kl_div(log_q_s, log_p_cf, reduction='none', log_target=True).sum(dim=-1)
    
    kl_rev_0 = F.kl_div(log_p_cf, log_p_base, reduction='none', log_target=True).sum(dim=-1)
    kl_rev_s = F.kl_div(log_p_cf, log_q_s, reduction='none', log_target=True).sum(dim=-1)

    D0_fwd = kl_fwd_0.mean().item()
    D0_rev = kl_rev_0.mean().item()
    if D0_fwd <= tau_0:
        raise ValueError(f"Précondition F8 violée : D0_fwd ({D0_fwd:.4f}) <= tau_0 ({tau_0}).")

    # Estimation ponctuelle de la fraction restaurée O (sans clamp)
    O_fwd_point = float(1.0 - (kl_fwd_s.mean().item() / D0_fwd))
    O_rev_point = float(1.0 - (kl_rev_s.mean().item() / (D0_rev + 1e-12)))

    # Distribution nulle sur les M sous-espaces aléatoires appariés en norme [M]
    kl_fwd_null = F.kl_div(
        log_q_null, log_p_cf.unsqueeze(0).expand(M, N, -1), reduction='none', log_target=True
    ).sum(dim=-1).mean(dim=-1)
    kl_rev_null = F.kl_div(
        log_p_cf.unsqueeze(0).expand(M, N, -1), log_q_null, reduction='none', log_target=True
    ).sum(dim=-1).mean(dim=-1)

    O_null_fwd = 1.0 - (kl_fwd_null / D0_fwd)
    O_null_rev = 1.0 - (kl_rev_null / (D0_rev + 1e-12))
    q95_null_fwd = float(torch.quantile(O_null_fwd, 0.95).item())
    q95_null_rev = float(torch.quantile(O_null_rev, 0.95).item())

    # Bootstrap par paire (seed fixe pour reproductibilité M0)
    gen = torch.Generator(device=log_p_cf.device).manual_seed(42)
    boot_idx = torch.randint(0, N, (n_boot, N), generator=gen, device=log_p_cf.device)

    boot_D0_fwd = kl_fwd_0[boot_idx].mean(dim=-1)
    boot_Ds_fwd = kl_fwd_s[boot_idx].mean(dim=-1)
    boot_O_fwd  = 1.0 - (boot_Ds_fwd / (boot_D0_fwd + 1e-12))

    boot_D0_rev = kl_rev_0[boot_idx].mean(dim=-1)
    boot_Ds_rev = kl_rev_s[boot_idx].mean(dim=-1)
    boot_O_rev  = 1.0 - (boot_Ds_rev / (boot_D0_rev + 1e-12))

    ic_fwd = (float(torch.quantile(boot_O_fwd, 0.025).item()), float(torch.quantile(boot_O_fwd, 0.975).item()))
    ic_rev = (float(torch.quantile(boot_O_rev, 0.025).item()), float(torch.quantile(boot_O_rev, 0.975).item()))

    # Décision B4 sans zone morte
    hb_won = (ic_fwd[0] > q95_null_fwd) and (ic_rev[0] > q95_null_rev)
    
    var_samples = data['var_ratio_samples'].to(torch.float32)
    boot_var = var_samples[boot_idx].mean(dim=-1)
    ic_low_var = float(torch.quantile(boot_var, 0.025).item())

    if not hb_won:
        verdict = "H_A (Médiation causale spécifique réfutée)"
    elif ic_low_var > gamma:
        verdict = "H_B1 (Médiateur causal naturel actif ; H_A et H_B2 réfutées)"
    else:
        verdict = "H_B2 (Illusion de patching / voie dormante ; H_A et H_B1 réfutées)"

    return {
        "O_fwd": O_fwd_point,
        "O_rev": O_rev_point,
        "IC95_O_fwd": ic_fwd,
        "IC95_O_rev": ic_rev,
        "q95_null_fwd": q95_null_fwd,
        "q95_null_rev": q95_null_rev,
        "IC95_low_var_ratio": ic_low_var,
        "verdict_B4": verdict
    }
```

FIN-PONT-M2-CONSOLIDE
