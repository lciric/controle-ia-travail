# Consolidation M2 → M1 — Proposition {lettre} — Silo-M2-1 : détecteur de sous-espace adaptatif sur fouillis à moyenne non nulle

## 0. Pièces manquantes ou douteuses (règle 2)
- `{lettre}`, `{autres}`, `{mots}`, `{marqueur}` ne sont toujours pas instanciés ; aucune proposition adverse jointe, B1 reste sans objet. Faute de limite connue, je reste aussi bref que le code le permet.
- La « matrice de prédation apprise en M3 » n'est pas jointe ; je ne suppose rien de son contenu.
- Les résumés restent tronqués, l'encodage corrompu ; je ne m'appuie que sur les phrases présentes.
- `S_TD` reste non défini : HYPOTHÈSE conservée, $H\in\mathbb R^{d\times r}$, colonnes parcimonieuses.
- `arXiv:2605.07434` : référence à vérifier (existence), format d'identifiant non contesté (F16 admis).

## 1. Réponses aux 16 failles

| Faille | Correction retenue |
|---|---|
| F1 | Modèle repris tel que le résumé le permet : $x=\mu+H\theta+c$ sous $H_1$, $\mu$ **commun** aux données secondaires et primaire. La « dérive » est redéfinie comme le terme $H\theta$ restreint à $\mathrm{span}(H)$. HYPOTHÈSE déclarée : toute composante de dérive hors $\mathrm{span}(H)$ n'est pas modélisée et peut dégrader le détecteur ; elle est traitée par le contrôle du complément orthogonal (F15). |
| F2 | Le nom « Rao » est retiré de la statistique. Celle implémentée (numérateur projeté, dénominateur $1+\delta^\top\hat S^{-1}\delta$) est étiquetée **HYPOTHÈSE : forme GLRT de type Kelly pour sous-espace**. Elle sera remplacée par la formule du texte intégral quand il sera disponible ; le protocole n'en dépend pas car tous les seuils sont calibrés empiriquement, jamais par loi analytique. |
| F3 | « Seul des trois », « $k=0$ » et « Rao ≡ LMP » retirés (sans source). Justification résiduelle du choix : la statistique n'exige aucun exemple de dérive étiqueté — propriété partagée par GLRT ; le choix du test est un paramètre d'implémentation, pas un résultat. |
| F4 | $\hat S$ normalisé par $K_{est}-1$, cohérent avec le code. Toute lecture « perte d'un DOF » de l'ablation 3 est supprimée. L'ablation $\hat\mu=0$ ne teste plus que « la dérive est un décalage de moyenne relatif à la référence ». |
| F5 | Renvoi à 1502.07523 retiré. Issue B renvoie à une formulation propre (§3). |
| F6 | Préconditions (gaussien, complexe, i.i.d.) déclarées **non transférées**. Seuils calibrés sur hold-out ; $K_{\text{eff}}$ estimé par moyennes par blocs et rapporté ; conditionnement de $\hat S+\lambda I$ rapporté. Le « ≳ 8 000 tokens » devient un chiffre de pilote, illustratif. |
| F7 | Convention fixée : `hidden_states[0]` = plongements, `hidden_states[ℓ]` = sortie du bloc $\ell$, $\ell\in\{1,\dots,32\}$ (RAPPORTÉ, config publique, à recouper). Toutes les couches sont prises ; multiplicité contrôlée par F10. |
| F8 | Formes : `test[ℓ] : [M,T,d]`, `ref_est[ℓ] : [K_est,d]`, `ref_hold[ℓ] : [M_h,T,d]`, `test_null[ℓ] : [M,T,d]`. Le hold-out et le test ont le même $|T|$ ; la covariance $R/|T|+R/K$ de $x$ est donc absorbée par la calibration empirique au lieu d'une remise à l'échelle analytique. Condition $|T|=1$ ajoutée (F13). |
| F9 | float64 obligatoire ; BOS et les `n_skip` premiers tokens exclus en amont (RAPPORTÉ : Sun, Chen, Kolter, Liu, 2024, *Massive Activations in Large Language Models*) ; `cond` rapporté. |
| F10 | Seuil calibré sur la loi hold-out du **maximum** familial (couches × coordonnées si $H$ inconnu, couches sinon). $O$ est la $P_D$ familiale à $P_{FA}$ familial $\alpha$. |
| F11 | Permutation à $\hat\mu,\hat S$ **figés** ; critère : $O_{perm}\le\alpha+2\sqrt{\alpha(1-\alpha)/M}$ (marge binomiale, illustratif). |
| F12 | Jeu `test_null` : même distribution que la référence, positions appariées, sans dérive. Exigé : $P_D(\text{test\_null})\le$ même borne qu'en F11. |
| F13 | Prémisse « la sonde linéaire échoue » : **absente des pièces**, statut HYPOTHÈSE-À-FOURNIR par l'arbitre. Condition $|T|=1$ appariée à la sonde. Falsifications réécrites en $\neg H_A$ / $\neg H_B$ (§3). |
| F14 | $K_{est}$ fixé a priori par un pilote et pré-enregistré ; aucun doublement en cours. La zone intermédiaire déclare « non concluant à $K_{est}$ fixé » et ne réfute rien. |
| F15 | Contrôle ajouté : $H_\perp$ = base du complément orthogonal de $\mathrm{span}(H)$, restreinte à $r$ directions aléatoires. Attendu si la détection passe par $S_{TD}$ : $O(H)\gg O(H_\perp)$ et $O(H)\gg O(H_{\text{aléatoire}})$. |
| F16 | Affirmations procédurales retirées. |

## 2. Protocole final M1

**Données.** `Llama-3.1-8B-Instruct`, $d=4096$ (RAPPORTÉ). Pour chaque couche : activations float64, BOS + `n_skip` tokens exclus. Trois ensembles de fenêtres de longueur $|T|\in\{1,T_0\}$ : `ref_est` (tokens, pas fenêtres), `ref_hold`, `test_null`, `test` (fenêtres présumées dérivées).

**Statistique** (HYPOTHÈSE, forme Kelly-sous-espace) : $\delta=x-\hat\mu$,
$t=\dfrac{\delta^\top\hat S^{-1}H(H^\top\hat S^{-1}H)^{-1}H^\top\hat S^{-1}\delta}{1+\delta^\top\hat S^{-1}\delta}$ ; si $H$ inconnu, $H=e_j$ et max sur $j$.

**Calibration.** $t_{\max}$ = max sur couches (et $j$) par fenêtre hold-out ; seuil = quantile $1-\alpha$, $\alpha=0{,}01$ (illustratif). $O=P_D$ familiale sur `test`.

**Pré-enregistrement.** $K_{est}$, $\lambda$, `n_skip`, $|T|$ fixés par pilote avant lecture de `test`.

## 3. Hypothèses exclusives (B4)
- $H_A$ : la dérive est séparable au second ordre dans $\mathrm{span}(H)$ — $O\ge 0{,}60$ à $|T|=1$ **et** tous les contrôles passent (illustratif).
- $H_B$ : non séparable au second ordre — $O\le 0{,}30$ à $|T|=1$ et $|T|=T_0$, contrôles passés.
- Issue A ⇒ $\neg H_B$ : réfute « aucun décalage de moyenne/covariance détectable dans $\mathrm{span}(H)$ ». Lien avec la sonde : seulement si la prémisse F13 est fournie avec statut.
- Issue B ⇒ $\neg H_A$ : réfute « la dérive est un signal de sous-espace additif visible au second ordre à ce $K_{est}$ ». Issue B ne distingue pas « dérive hors $\mathrm{span}(H)$ » de « dérive d'ordre supérieur » ; ce point est explicitement laissé ouvert.
- $]0{,}30;0{,}60[$ : non concluant à $K_{est}$ fixé.

## 4. Code PyTorch `compute_O`

```python
import math
import torch

def _fit_reference(ref_est, lam):
    """ref_est: [K,d]. Retourne mu, facteur de Cholesky L de (S+lam*I), cond, K_eff (batch means)."""
    Y = ref_est.to(torch.float64)
    K, d = Y.shape
    mu = Y.mean(0)
    Yc = Y - mu
    S = Yc.T @ Yc / (K - 1)
    if lam is None:                      # illustratif : 1e-3 * trace/d
        lam = 1e-3 * S.diagonal().mean().item()
    S = S + lam * torch.eye(d, dtype=Y.dtype, device=Y.device)
    L = torch.linalg.cholesky(S)
    ev = torch.linalg.eigvalsh(S)
    cond = (ev[-1] / ev[0]).item()
    # K_eff par moyennes de blocs (F6) : var(moyenne bloc) ~ sigma^2/(b/ac) ; estimation sur la trace
    b = max(16, K // 64)
    nb = K // b
    bm = Yc[: nb * b].reshape(nb, b, d).mean(1)
    var_bm = bm.var(0, unbiased=True).sum().item()
    var_tok = Yc.var(0, unbiased=True).sum().item()
    k_eff = K * var_tok / max(var_bm * b, 1e-12)
    return mu, L, cond, min(k_eff, float(K))

def _stat(x, mu, L, H=None):
    """x: [N,d] (fenêtres déjà moyennées sur |T|). H: [d,r] ou None (coordonnées).
    HYPOTHÈSE : forme GLRT de type Kelly pour sous-espace, en attente du texte intégral."""
    delta = x.to(torch.float64) - mu                                    # [N,d]
    z = torch.linalg.solve_triangular(L, delta.T, upper=False).T        # z = L^{-1} delta
    denom = 1.0 + (z * z).sum(1)                                        # [N]
    if H is not None:
        A = torch.linalg.solve_triangular(L, H.to(torch.float64), upper=False)  # [d,r]
        Q, _ = torch.linalg.qr(A)
        num = ((z @ Q) ** 2).sum(1)
        return num / denom                                              # [N]
    w = torch.cholesky_solve(delta.T, L).T                              # S^{-1} delta, [N,d]
    sinv_diag = torch.cholesky_inverse(L).diagonal()
    num = w ** 2 / sinv_diag                                            # [N,d]
    return (num / denom[:, None]).max(1).values                         # max_j, [N]

def _family_max(windows, fits, H):
    """windows: {l: [N,T,d]} ; fits: {l: (mu,L)} ; retourne t_max sur couches, [N]."""
    out = None
    for l, (mu, L) in fits.items():
        x = windows[l].to(torch.float64).mean(1)                        # moyenne sur |T|
        t = _stat(x, mu, L, None if H is None else H[l])
        out = t if out is None else torch.maximum(out, t)
    return out

def compute_O(data, alpha=0.01, lam=None, n_perm=20, diag=None) -> float:
    """
    data = {"ref_est": {l:[K,d]}, "ref_hold": {l:[M_h,T,d]}, "test": {l:[M,T,d]},
            "test_null": {l:[M,T,d]}, "H": {l:[d,r]} ou None}
    Exclusion BOS/n_skip et float64 : à appliquer en amont.
    Retourne O = P_D familiale à P_FA familial alpha ; diagnostics dans `diag` (dict).
    """
    H = data.get("H")
    fits, conds, keffs = {}, {}, {}
    for l, Y in data["ref_est"].items():
        mu, L, cond, keff = _fit_reference(Y, lam)
        fits[l] = (mu, L); conds[l] = cond; keffs[l] = keff
    t_hold = _family_max(data["ref_hold"], fits, H)
    thr = torch.quantile(t_hold, 1.0 - alpha).item()                    # seuil du max familial (F10)
    t_test = _family_max(data["test"], fits, H)
    O = (t_test > thr).double().mean().item()
    M = t_test.numel()
    bound = alpha + 2.0 * math.sqrt(alpha * (1 - alpha) / M)            # marge binomiale, illustratif
    # F12 : test nul apparié
    pfa_null = (_family_max(data["test_null"], fits, H) > thr).double().mean().item()
    # F11 : permutation hold/test à mu,S figés
    pool = torch.cat([t_hold, t_test]); n_h = t_hold.numel()
    perm_rates = []
    g = torch.Generator().manual_seed(0)
    for _ in range(n_perm):
        p = pool[torch.randperm(pool.numel(), generator=g)]
        thr_p = torch.quantile(p[:n_h], 1.0 - alpha)
        perm_rates.append((p[n_h:] > thr_p).double().mean().item())
    O_perm = float(sum(perm_rates) / len(perm_rates))
    if diag is not None:
        diag.update(dict(threshold=thr, O=O, pfa_null=pfa_null, O_perm=O_perm, bound=bound,
                         cond=conds, K_eff=keffs, controls_pass=(pfa_null <= bound and O_perm <= bound)))
    return O
```

**Usage des contrôles (hors fonction, mêmes données) :** appeler `compute_O` avec `H`, puis avec `H_random` (même $r$, même parcimonie) et `H_perp` (F15), puis `H=None` ; répéter à $|T|=1$ et $|T|=T_0$ ; ablation $\hat\mu=0$ en passant `ref_est` centré sur zéro artificiellement. Tout résultat est OBSERVÉ-NON-AUDITÉ jusqu'à audit.

**Réfutable après consolidation :** séparabilité au second ordre à $|T|=1$ ; CFAR familial $\le\alpha$ sous permutation à statistiques figées et sur test nul apparié ; préférence pour $S_{TD}$ face à son complément orthogonal ; faisabilité à $K_{est}$ pré-enregistré compte tenu de $K_{\text{eff}}$.

FIN-PONT-M2-CONSOLIDE
