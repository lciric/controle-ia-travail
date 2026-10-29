**Constat d'intégrité (Règle 2) :** Les variables de consigne (`{lettre}`, `{autres}`, `{mots}`, `{marqueur}`), les propositions concurrentes et la fin des cinq résumés arXiv sont absentes ou coupées dans le prompt transmis.

### 1. Complémentarité de Préconditions & Ancrage d'Implication

* **Diagnostic (OBSERVÉ-NON-AUDITÉ) :** Sur `Llama-3.1-8B-Instruct` ($h_\ell^{(t)}, S_{\text{TD}}$ couches 2 à 22), une sonde linéaire entraînée sur des activations observationnelles i.i.d. échoue à isoler un médiateur causal parcimonieux d'une corrélation de surface, car la structure causale sous-jacente n'est pas identifiable sans intervention.
* **Ancrage (RAPPORTÉ) :** Nous compilons l'opérateur de **[arXiv:2302.05380v1] On the Interventional Kullback-Leibler Divergence** (référence à vérifier), couplé à l'hypothèse de **[arXiv:2211.03553v4] Learning Causal Representations of Single Cells via Sparse Mechanism Shift Modeling** (référence à vérifier).
  > Citation exacte 1 : « *However, the true causal structure underlying a given set of data is generally not identifiable, so it is desirable to have means to quantify differences between models (e.g., between the ground truth and an estimate), on both the observational and interventional level. In the present work, we introduce the Interventional Kullback-Leibler (IKL) divergence to quantify both structural and distributional differences between models* » (référence à vérifier).
  > Citation exacte 2 : « *Instead, recent methods propose to leverage non-stationary data, as well as the sparse mechanism shift assumption in order to learn disentangled representations with a causal semantic.* » (référence à vérifier).

### 2. Compilation Tensorielle sur `Llama-3.1-8B-Instruct`

Soit $h_\ell^{(t)} \in \mathbb{R}^{4096}$ (RAPPORTÉ) l'état caché à la couche $\ell \in \{2, \dots, 22\}$ et au token $t$. Soit $P_S \in \mathbb{R}^{4096 \times 4096}$ le projecteur orthogonal sur le sous-espace parcimonieux cible $S_{\text{TD}}$ de dimension $k = 16$ `illustratif`.

Pour un couple d'entrées (prompt source $x$, prompt contrefactuel $x'$), nous définissons l'opérateur de *clamp partiel* $\text{do}(S_{\text{TD}} \leftarrow P_S h_\ell^{(t)}(x'))$ qui remplace la composante $S_{\text{TD}}$ lors de la passe avant sur $x$ :
$$\tilde{h}_\ell^{(t)}(x \mid \text{do}(S_{\text{TD}})) = (I - P_S) h_\ell^{(t)}(x) + P_S h_\ell^{(t)}(x')$$

La divergence de Kullback-Leibler interventionnelle ($D_{\text{IKL}}$) mesure l'effet de médiation causale sur la distribution des logits de sortie $P(\cdot \mid \cdot)$ vers la cible contrefactuelle :
$$D_{\text{IKL}}(S_{\text{TD}}) = \mathbb{E}_{(x, x')} \left[ D_{\text{KL}}\Big( P\big(Y \mid x'\big) \;\Big\|\; P\big(Y \mid x, \text{do}(S_{\text{TD}} \leftarrow P_S h_\ell^{(t)}(x'))\big) \Big) \right]$$

### 3. Spécification EEC Sans Zone Morte (Inférence Forte B4)

* **Contrôle de permutation/ablation $R_S$ :** Soit $P_{\pi(S)}$ un sous-espace aléatoire de même rang $k=16$ `illustratif` obtenu par permutation orthogonale des axes de $h_\ell^{(t)}$ hors de $S_{\text{TD}}$. Le gain causal normalisé est :
$$O = \frac{D_{\text{IKL}}(S_{\text{R\_S}}) - D_{\text{IKL}}(S_{\text{TD}})}{D_{\text{IKL}}(S_{\text{R\_S}}) + \epsilon}$$

```python
import torch
import torch.nn.functional as F

def compute_O(data: dict) -> float:
    """
    data['logits_cf']: Tensor [N, V] (logits sur x')
    data['logits_do_S']: Tensor [N, V] (logits sur x avec clamp partiel S_TD)
    data['logits_do_RS']: Tensor [N, V] (logits sur x avec clamp permuté R_S)
    """
    p_cf = F.log_softmax(data['logits_cf'], dim=-1)
    q_s = F.log_softmax(data['logits_do_S'], dim=-1)
    q_rs = F.log_softmax(data['logits_do_RS'], dim=-1)
    
    ikl_s = F.kl_div(q_s, p_cf, reduction='batchmean', log_target=True)
    ikl_rs = F.kl_div(q_rs, p_cf, reduction='batchmean', log_target=True)
    
    O_val = (ikl_rs - ikl_s) / (ikl_rs + 1e-8)
    return float(torch.clamp(O_val, 0.0, 1.0).item())
```

* **Hypothèses exclusives (HYPOTHÈSE) :**
  * $\mathcal{H}_A$ (*Corrélation de surface*) : Le sous-espace $S_{\text{TD}}$ ne médiatise pas le mécanisme causal ; l'intervention $\text{do}(S_{\text{TD}})$ a un effet indistinguable de l'ablation permutée $R_S$. Intervalle : $\hat{I}_A = [0,00 ; 0,15]$ `illustratif`. Si $O \in \hat{I}_A$, la médiation causale parcimonieuse de $S_{\text{TD}}$ est réfutée.
  * $\mathcal{H}_B$ (*Médiation causale parcimonieuse*) : Le clamp partiel de $S_{\text{TD}}$ restaure la distribution contrefactuelle significativement mieux que $R_S$. Intervalle : $\hat{I}_B = [0,30 ; 1,00]$ `illustratif`. Si $O \in \hat{I}_B$, l'hypothèse de pure corrélation de surface est réfutée.
  * **Séparation stricte :** $\text{dist}(\hat{I}_A, \hat{I}_B) = 0,15 > 0,10$ `illustratif`. Toute mesure dans $]0,15 ; 0,30[$ `illustratif` invalide la suffisance du rang $k$ choisi et impose de doubler $k$ avant re-test.

{marqueur}
FIN-PONT-M2
