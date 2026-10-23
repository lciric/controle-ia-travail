**Note d'intégrité (Règle 2) :** Les paramètres d'instruction `{lettre}`, `{autres}`, `{mots}` et `{marqueur}` ne sont pas résolus ; les propositions des autres modèles sont absentes ; les résumés des articles `[arXiv:2403.00447v3]` et `[arXiv:2010.00268v1]` sont visiblement coupés à la fin.

### 1. Complémentarité de Préconditions & Compilation Tensorielle
* **Constat de base :** L'amplification transitoire sous perturbations aversives répétées passe de $0.49$ à $0.65$ (OBSERVÉ-NON-AUDITÉ). Une projection orthogonale brute sur le sous-espace de la sonde linéaire $S_{\text{TD}}$ induit une discontinuité dans le flux résiduel de `Llama-3.1-8B-Instruct` (couches $\ell \in [2, 22]$), ce qui excite les modes non-normaux adjacents (HYPOTHÈSE).
* **Sélection et Ancrage :** Pour éliminer cette discontinuité tout en maintenant l'invariance du sous-espace sûr, nous sélectionnons `[arXiv:2403.00447v3]` (référence à vérifier). Ancrage exact : *« Specifically, we prove that trajectories of CBF-based dynamics uniformly converge to trajectories of PDSs, as a CBF-parameter approaches infinity. »* (référence à vérifier) [STATUT : RAPPORTÉ].
* **Opérateur compilé :** Soit $h_\ell^{(t)} \in \mathbb{R}^{d}$ l'activation à la couche $\ell$ et au token $t$, et $U \in \mathbb{R}^{d \times k}$ une base orthonormée du sous-espace aversif de rang faible $S_{\text{TD}}$. On définit la fonction barrière de contrôle (CBF) par $B(h_\ell^{(t)}) = \tau - \|U^\top h_\ell^{(t)}\|_2^2$, avec le seuil de sécurité $\tau = 0.20$ `illustratif`. La dynamique discontinue du système dynamique projeté (PDS) est approximée de manière Lipschitz-continue sur le tenseur par l'opérateur d'amortissement de paramètre $\gamma = 15.0$ `illustratif` (HYPOTHÈSE) :
$$\tilde{h}_\ell^{(t)} = h_\ell^{(t)} - \frac{1}{1 + \gamma \max(0, B(h_\ell^{(t)}))} U U^\top h_\ell^{(t)}$$

### 2. Inférence Forte et Spécification EEC Sans Zone Morte
Conformément à la règle B4, nous opposons deux hypothèses exclusives sur l'effet de cet opérateur continu face aux perturbations aversives répétées :
* **$H_A$ (Amortissement continu des modes non-normaux) :** L'approximation continue par CBF ($\gamma = 15.0$ `illustratif`) dissipe l'amplification transitoire le long des couches $2$ à $22$ sans générer de rebond spectral, ramenant la métrique d'amplification sous le niveau initial de $0.49$ (OBSERVÉ-NON-AUDITÉ).
* **$H_B$ (Excitation résiduelle ou défaillance de rang) :** L'amplification ($0.49 \to 0.65$, OBSERVÉ-NON-AUDITÉ) est gouvernée par une dynamique hors du sous-espace $S_{\text{TD}}$ ou la relaxation continue ($\gamma < \infty$) laisse filtrer l'énergie aversive ; l'amplification reste supérieure ou égale à $0.60$ `illustratif`.

**Fonction pure d'évaluation :**
```python
def compute_O(data: dict) -> float:
    """
    data['h_perturbed']: Tensor de forme (T, L, d) pour T perturbations, L=21 couches (2 à 22).
    data['U']: Tensor de forme (d, k) représentant la base S_TD.
    Retourne le ratio maximal d'amplification transitoire inter-couches.
    """
    h = data['h_perturbed']
    U = data['U']
    proj_energy = ((h @ U) ** 2).sum(dim=-1).sqrt()  # Forme: (T, L)
    transient_gain = proj_energy[:, -1] / (proj_energy[:, 0] + 1e-8)
    return float(transient_gain.max().item())
```

* **Intervalles disjoints :**
  * $\hat{I}_A = [0.00 \text{ illustratif}, 0.48 \text{ illustratif}]$ (falsifie $H_B$, valide l'amortissement par CBF).
  * $\hat{I}_B = [0.60 \text{ illustratif}, 2.00 \text{ illustratif}]$ (falsifie $H_A$, prouve l'inefficacité de la barrière de rang faible).
  * Condition de séparation sans zone morte locale : $\text{dist}(\hat{I}_A, \hat{I}_B) = 0.60 - 0.48 = 0.12 > 0,10$ `illustratif`.

* **Contrôle de permutation/ablation ($R_S$) :**
  On remplace l'opérateur $U$ par une matrice orthogonale aléatoire $U_{\text{perm}} \in \mathbb{R}^{d \times k}$ générée par décomposition QR d'une matrice gaussienne (destruction de l'alignement avec $S_{\text{TD}}$). Le test d'intégrité exige que `compute_O` avec $U_{\text{perm}}$ tombe dans $\hat{I}_B$ ($\ge 0.60$ `illustratif`). Si le contrôle aléatoire tombe dans $\hat{I}_A$, l'expérience entière est invalidée par artefact de régularisation globale (HYPOTHÈSE).

{marqueur}
FIN-PONT-M2
