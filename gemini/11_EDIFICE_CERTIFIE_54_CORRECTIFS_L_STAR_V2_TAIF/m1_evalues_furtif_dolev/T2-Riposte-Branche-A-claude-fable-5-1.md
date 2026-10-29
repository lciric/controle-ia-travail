# DOSSIER SOUVERAIN — TOUR 2 · BRANCHE A · `claude-fable-5-1`
## Riposte et consolidation : substrat $S_{\text{TD}}$ non circulaire, 5 Volets Unifiés, campagne 72 h GPU / 500 USD

---

### 0. Avertissement de rigueur et tableau de riposte

**0.1 Conventions maintenues.** Toute référence hors socle porte `(référence à vérifier)` ; tout seuil numérique porte `illustratif` et sera remplacé, avant la Phase 1, par la valeur calibrée en Phase 0 puis **engagée** cryptographiquement (§ 2.3, `leaf_hash` du JSON des seuils publié avant la première exécution). Le white space est *revendiqué sous réserve de recherche exhaustive* ; il porte sur le couplage inférentiel, jamais sur un composant isolé.

**0.2 Intégrité du code.** Chaque bloc ci-dessous a été écrit pour passer `python -m py_compile` ; aucun commentaire d'audit n'est inséré à l'intérieur d'une fonction (réponse à la Faille 3 de `gemini-4-argon` sur la `SyntaxError` dans `edmd_koopman`). La Faille 1 du même auditeur est arrivée tronquée (« Volet I (§ 0. »*) ; je la traite par la seule reformulation possible de § 0 : la définition de $S_{\text{TD}}$ (0.4) est désormais non circulaire, invariante aux signes, et dotée d'une variante cross-fit.

**0.3 Tableau de riposte (faille → correctif → section).**

| Faille | Correctif | § |
|---|---|---|
| G2, C1, C2 (centrage, double usage) | Gram non centré $D^\top D$, invariant aux retournements de signe ; variante cross-fit par blocs | 2.0, 2.1 |
| C3 (plan incohérent, bras $\sigma_r^0$ inutilisé) | Plan à **quatre** bras A/C/B/L : $\sigma_r^0$ = pivot C des deux contrastes ; contrôle par *jumeau lexical* L à distance d'édition appariée | 2.1 |
| C4 (détecteur $\max_k$ non calibré, PAD) | Statistique scalaire d'énergie, nul par permutation deux-échantillons, longueurs naturelles | 2.1 |
| C5 (dynamique $F$ ignorée) | Théorème de confinement sous hypothèse $H_\Delta$ de dérive bornée, vérifiée en Phase 0 | 2.2 |
| C6 (projection liftée non réalisable) | Koopman identifie, l'opérateur agit sur $x$ seulement ; réalification des modes complexes | 2.2 |
| C7 (`rand-parc` $L_\infty$ biaisé) | Bras `rand-dir` : direction aléatoire de rang $q$, norme $L_2$ appariée | 2.2 |
| C8 (IC contenant 0) | TOST apparié, marge pré-enregistrée | 2.1, 2.2 |
| G4, C9 (JSD incohérente, biais MM résiduel) | $\text{JSD}_{1/2}$ sur fréquences normalisées, centrée et seuillée par bootstrap paramétrique ; Miller-Madow réservé à l'entropie univariée | 2.3 |
| G5, C10 (Merkle sans séparation de domaine) | RFC 6962 : préfixes `0x00`/`0x01`, arbre non équilibré sans duplication, taille engagée dans la tête signée | 2.3 |
| C11 (« cône sûr ») | Terme supprimé : $T$ est l'identité sur $\bar B(c,a)$ | 2.2 |
| G6, C15 (quantile adaptatif asservi) | Régulateur supprimé ; seuil gelé en Phase I ; adaptation interdite sans étiquette | 2.4 |
| G7 (censure à droite dans `calibrate_h`) | ARL par chaîne de Markov de Brook-Evans, validation MC où les trajectoires censurées sont conservées comme bornes inférieures | 2.4 |
| C12 (pré-blanchiment in-sample) | Phases I/II séparées, inflation de $h$ par bootstrap paramétrique de l'erreur d'estimation | 2.4 |
| C13 (variance JT incomplète) | Formule complète à trois termes | 2.4 |
| C14 (JT sur mesures répétées) | Test de Page par blocs = chaînes, nul exact par permutation intra-chaîne ; JT relégué au cas « une profondeur par chaîne » | 2.4 |
| G3, C16 (fuite inter-paires / intra-famille) | Cross-fitting *leave-one-family-out*, un épisode par strate, nul CMH par permutation conditionnelle | 2.5 |

**0.4 Définition opératoire de $S_{\text{TD}}$ (corrigée).** Au rang $k=0$ (dernier token avant le premier token d'action), flux résiduel $h\in\mathbb R^d$ de la couche $\ell^\*$. Pour chaque item $i$, contraste apparié $\delta_i = h_i^{A} - h_i^{C}$ entre le bras *intention* A et le pivot *Jumeau Nié* C (§ 2.1). $S_{\text{TD}}$ est le sous-espace engendré par les $r$ vecteurs propres dominants de la matrice de Gram **non centrée** $G = \sum_i \delta_i\delta_i^\top$, $r\le\lfloor 0{,}01\,d\rfloor$ (`illustratif` : $r\le 40$ pour $d=4096$). Propriété clé : $G$ est invariante par tout retournement de signe de ligne $\delta_i\mapsto -\delta_i$, donc $U_{\text{TD}}$ est une fonction de $\{\delta_i\delta_i^\top\}$ seulement et le test par retournement de signe de § 2.1 reste exact avec $U_{\text{TD}}$ figé. Le vecteur $\hat\mu/\|\hat\mu\|$ (moyenne des contrastes) est fourni comme direction secondaire pour contrôler que $u_1$ et $\hat\mu$ sont alignés (cosinus rapporté).

---

## 1. CARTE D'ANTÉRIORITÉ ET BASELINES ANTI-STRAWMAN (consolidée)

Règle : chaque volet affronte la baseline la plus forte de sa lignée, implémentée sur le même tenseur.

**Volet I.** Lignées couvertes et lacunes : sondes contrastives CCS (Burns et al., arXiv:2212.03827, référence à vérifier) et mass-mean (Marks & Tegmark, arXiv:2310.06824, référence à vérifier) opèrent sur des paires fait/négation sans plan à pivot ni nul apparié exact ; sondes de tromperie (Goldowsky-Dill et al., arXiv:2502.03407 ; Hubinger et al., arXiv:2401.05566, références à vérifier) fournissent une accuracy, non une séparation intention/lexie garantie en niveau ; Future Lens (arXiv:2311.04897, référence à vérifier) décode le futur lexical, pas une décision ; INLP/CausaLM (arXiv:2004.07667 ; arXiv:2005.13407, références à vérifier) retirent des corrélations sans ancrage à $k=0$. Baselines : `B-I.1` mass-mean sur $h_{k=0}$ ; `B-I.2` régression logistique ; `B-I.3` **jumeau lexical** (défini § 2.1, remplace le sac-de-mots naïf) ; `B-I.4` couches $\ell^\*\pm4$ (`illustratif`).

**Volet II.** LEACE (arXiv:2306.03819, référence à vérifier) possède l'idempotence affine — ce n'est pas notre apport ; ablation de refus (Arditi et al., arXiv:2406.11717, référence à vérifier), ITI/ActAdd (arXiv:2306.03341 ; arXiv:2308.10248, références à vérifier), R-LACE (arXiv:2201.12091, référence à vérifier), Conceptors (arXiv:1403.3369, référence à vérifier), ReFT (arXiv:2404.03592, référence à vérifier) : aucune borne sous rejets répétés avec dynamique du modèle explicitée ; EDMD (Williams, Kevrekidis, Rowley 2015, référence à vérifier) jamais utilisé comme *identificateur* de directions de dérive conversationnelle. Baselines : `B-II.1` LEACE par tour ; `B-II.2` Arditi ; `B-II.3` ActAdd à norme $L_2$ appariée ; `B-II.4` sans intervention (dérive `0,49 → 0,65`, Jhaveri/Tagliabue 2026, référence à vérifier, `illustratif`) ; **`B-II.5` `rand-dir`** : direction aléatoire de rang $q$, norme $L_2$ appariée.

**Volet III.** StruQ, Instruction Hierarchy, Spotlighting (arXiv:2402.06363 ; arXiv:2404.13208 ; arXiv:2403.14720, références à vérifier) ; CaMeL, IsolateGPT (arXiv:2503.18813 ; arXiv:2403.04960, références à vérifier) ; Llama Guard, Progent, TaskShield (arXiv:2312.06674 ; arXiv:2504.11703 ; arXiv:2412.16682, références à vérifier) ; RFC 6962 (référence à vérifier) pour le journal Merkle ; Lin 1991 pour la JSD généralisée et Miller 1955 / Paninski 2003 pour la correction d'entropie (références à vérifier). Baselines : `B-III.1` StruQ ; `B-III.2` Spotlighting ; `B-III.3` Llama Guard ; `B-III.4` enveloppe sans Merkle ni JSD ; `B-III.5` JSD plug-in non centrée.

**Volet IV.** Page 1954 ; Lu & Reynolds JQT 2001 (CUSUM sur résidus AR(1) — antériorité directe) ; Brook & Evans 1972 (ARL par chaîne de Markov) ; BOCPD (arXiv:0710.3742) ; e-détecteurs (Shin, Ramdas, Rinaldo, arXiv:2203.03532) ; Page 1963 (test $L$ par blocs) ; Macaroons NDSS 2014 ; RFC 8693 (toutes références à vérifier). Baselines : `B-IV.1` CUSUM brut ; `B-IV.2` BOCPD ; `B-IV.3` e-détecteur ; `B-IV.4` régression linéaire sur $d$.

**Volet V.** AI Control (arXiv:2312.06942, référence à vérifier) ; résilience MAS (arXiv:2408.00989 ; arXiv:2406.14711, références à vérifier) ; collusion secrète (arXiv:2402.07510, référence à vérifier) ; PBFT (Castro & Liskov 1999, référence à vérifier) ; HMP (Wilson PNAS 2019 ; Vovk & Wang 2020, références à vérifier) ; RFA (arXiv:1912.13445, référence à vérifier). Baselines : `B-V.1` $\chi^2$ poolé (démonstration de Simpson obligatoire) ; `B-V.2` médiane géométrique ; `B-V.3` vote majoritaire ; `B-V.4` auditeur intra-famille.

---

## 2. PROTOCOLE MATHÉMATIQUE ET CODE

Conventions : `numpy`, `scipy`, `hashlib`, `hmac`, `json`. Tout est testable sur données synthétiques avant GPU.

### 2.0 Substrat commun

```python
import numpy as np

def fit_S_TD(D, frac=0.01):
    """D : (n, d) contrastes appariés delta_i = h_i^A - h_i^C, NON centrés.
    Base orthonormée des r vecteurs propres dominants de G = D^T D (frac illustratif).
    G est invariante par delta_i -> -delta_i : U est une fonction des {delta_i delta_i^T}."""
    D = np.asarray(D, np.float64)
    r = max(1, int(np.floor(frac * D.shape[1])))
    w, V = np.linalg.eigh(D.T @ D)
    order = np.argsort(-w)[:r]
    U = V[:, order]
    mu = D.mean(0)
    cos_mu_u1 = abs(mu @ U[:, 0]) / (np.linalg.norm(mu) + 1e-12)
    return U, cos_mu_u1

def fit_S_TD_crossfit(D, blocks, frac=0.01, seed=0):
    """Variante B : base ajustée sur une moitié des blocs, test sur l'autre moitié."""
    rng = np.random.default_rng(seed)
    ub = np.unique(blocks).copy(); rng.shuffle(ub)
    fit_mask = np.isin(blocks, ub[: len(ub) // 2])
    U, _ = fit_S_TD(D[fit_mask], frac)
    return U, ~fit_mask

def project_TD(H, U):
    return np.asarray(H, np.float64) @ U
```

### 2.1 Volet I — plan à quatre bras, $d_z$ de Hedges, nul exact, jumeau lexical, canal subliminal

**Plan contrôlé (reformulé).** Un gabarit à longueur fixe contient un créneau `S_int` (clause d'intention) et un créneau `S_act` (clause d'acte). Dans un décodeur causal, tout le contexte est visible à $k=0$ ; je ne prétends donc plus à une « surface identique » mais à une **distance d'édition appariée** :

- **C — $\sigma_r^0$ Jumeau Nié** (pivot) : `S_int` = intention niée par un unique token de négation, `S_act` = aucun acte ;
- **A — `P2` Saboteur Inactif** : `S_int` = intention affirmée (C moins le token de négation), `S_act` = aucun acte ;
- **B — `P4` Acte Imposé** : `S_int` identique à C, `S_act` = acte exécuté sous contrainte ;
- **L — Jumeau lexical** : identique à A, plus le même token de négation inséré dans une clause décorative sans portée sur l'intention.

Contrastes : $\delta^{\text{int}}_i = \langle h^A_i - h^C_i, u_1\rangle$ (intention, édition = 1 token), $\delta^{\text{act}}_i = \langle h^B_i - h^C_i, u_1\rangle$ (acte), $\delta^{\text{lex}}_i = \langle h^L_i - h^A_i, u_1\rangle$ (même token, sans intention). Le bras $\sigma_r^0$ intervient donc dans **tous** les contrastes comme pivot. Le volet est certifié si (i) $\delta^{\text{int}}$ est significatif au nul exact, (ii) $\delta^{\text{lex}}$ est *équivalent à zéro* au sens TOST, (iii) l'angle entre la direction intention et la direction acte dépasse une marge pré-enregistrée (`illustratif` : $\cos \le 0{,}5$).

**Statistique.** $d_z = J(\nu)\,\bar\delta/s_\delta$, $J(\nu)=1-3/(4\nu-1)$, $\nu=n-1$ (vérifié sain par l'audit). Nul exact : retournement de signe de blocs entiers ($2^B$ configurations), $U_{\text{TD}}$ figé licitement par invariance du Gram.

```python
from itertools import product

def hedges_dz(delta):
    delta = np.asarray(delta, float); nu = len(delta) - 1
    return (1.0 - 3.0 / (4.0 * nu - 1.0)) * delta.mean() / delta.std(ddof=1)

def signflip_block_test(delta_blocks, n_mc=None, seed=0, exact_max_B=20):
    """Nul exact par retournement de signe de blocs (exact_max_B illustratif)."""
    B = len(delta_blocks)
    obs = hedges_dz(np.concatenate(delta_blocks))
    exact = (n_mc is None) and (B <= exact_max_B)
    if exact:
        configs, total = product([1, -1], repeat=B), 2 ** B
    else:
        rng = np.random.default_rng(seed)
        configs, total = (rng.choice([1, -1], B) for _ in range(n_mc)), n_mc
    hits = 0
    for s in configs:
        d = np.concatenate([si * blk for si, blk in zip(s, delta_blocks)])
        hits += abs(hedges_dz(d)) >= abs(obs)
    p = hits / total if exact else (hits + 1) / (total + 1)
    return obs, p

def tost_paired(delta, margin, n_boot=5000, seed=0):
    """Équivalence appariée : IC bootstrap à 90 % de la moyenne inclus dans ]-margin, margin[
    <=> TOST au niveau 5 %. margin pré-enregistrée (illustratif : 0.1 écart-type)."""
    rng = np.random.default_rng(seed); delta = np.asarray(delta, float); n = len(delta)
    means = np.array([delta[rng.integers(0, n, n)].mean() for _ in range(n_boot)])
    lo, hi = np.percentile(means, [5, 95])
    return delta.mean(), (lo, hi), bool(lo > -margin and hi < margin)

def direction_angle(D_int, D_act):
    """Cosinus entre les directions dominantes intention (A-C) et acte (B-C)."""
    u_int, _ = fit_S_TD(D_int, frac=1e-9); u_act, _ = fit_S_TD(D_act, frac=1e-9)
    return abs(float(u_int[:, 0] @ u_act[:, 0]))

def max_energy_perm_test(E_test, E_ctrl, n_perm=5000, seed=0):
    """Détecteur de canal subliminal (C4 corrigé).
    E_* : (n, K) énergies ||U_TD^T h_k||^2 aux K positions précédant k=0, longueurs
    naturelles appariées (aucun PAD). Standardisation par position sur le contrôle,
    statistique scalaire par séquence m_i = max_k z_ik, nul par permutation des étiquettes."""
    mu, sd = E_ctrl.mean(0), E_ctrl.std(0, ddof=1) + 1e-12
    m_test = ((E_test - mu) / sd).max(1); m_ctrl = ((E_ctrl - mu) / sd).max(1)
    obs = m_test.mean() - m_ctrl.mean()
    pool = np.concatenate([m_test, m_ctrl]); n1 = len(m_test)
    rng = np.random.default_rng(seed); hits = 0
    for _ in range(n_perm):
        rng.shuffle(pool)
        hits += (pool[:n1].mean() - pool[n1:].mean()) >= obs
    return obs, (hits + 1) / (n_perm + 1)
```

**Critère (illustratif) :** $p_{\text{exact}}(\delta^{\text{int}}) < 0{,}01$ et $|d_z^{\text{int}}|\ge0{,}5$ ; TOST sur $\delta^{\text{lex}}$ concluant à l'équivalence (marge $0{,}1\,s_\delta$) ; $\cos(u_{\text{int}},u_{\text{act}})\le0{,}5$ ; canal subliminal : $p_{\text{perm}} \ge 0{,}05$ sur les prompts bénins (absence de fuite positionnelle). Faute de quoi le volet est invalidé.

### 2.2 Volet II — `Do-Clamp` : identification Koopman, projection réalisable dans $\mathbb R^d$, confinement sous dynamique bornée, bras `rand-dir`

**Identification (EDMD).** Dictionnaire $\Psi(x)=[x;\phi(x)]\in\mathbb R^m$ ; $K$ par moindres carrés ridge sur paires de tours $(x_t,x_{t+1})$. Les modes de $K^\top$ de module $\ge1$ (`illustratif`) ne servent qu'à **identifier** des directions : on extrait leur composante état $v_x\in\mathbb C^d$, on réalifie ($\mathrm{span}\{\Re v_x,\Im v_x\}$ pour une paire conjuguée, un seul représentant par paire), puis on orthonormalise par QR dans $\mathbb R^d$. L'opérateur n'agit jamais sur $[x;\phi(x)]$ (C6 corrigé).

**Opérateur.** $U_x\in\mathbb R^{d\times q}$ orthonormée, consigne $c$ :
$$P_{\text{do}}(x)=c+(I-U_xU_x^\top)(x-c),\qquad Q=I-U_xU_x^\top,\ Q^2=Q.$$

**Rétraction radiale $C^1$.** $v=x-c$, $\rho=\|v\|$, $r(\rho)=\rho$ si $\rho\le a$, sinon $a+(R-a)\tanh\!\big(\tfrac{\rho-a}{R-a}\big)$ ; $T(x)=c+v\,r(\rho)/\rho$. $T$ est l'identité sur la **boule fermée** $\bar B(c,a)$ et bornée par $R$ (toute mention de « cône » est retirée, C11).

**Théorème de confinement (sous $H_\Delta$, C5 corrigé).** Soit $F$ la dynamique du modèle et des rejets entre deux interventions, $\mathcal C=T\circ P_{\text{do}}$, et $z_{t+1}=\mathcal C(F(z_t))$. Hypothèse $H_\Delta$ : $\|F(z)-z\|\le\Delta$ pour tout $z\in\bar B(c,R)$, avec $\Delta<R-a$. Alors :

1. *(Annulation exacte le long de $U_x$.)* $U_x^\top(z_{t+1}-c)=U_x^\top T(\cdot)$ est colinéaire à $U_x^\top Q(\cdot)=0$ : la composante de dérive identifiée est nulle à **chaque** tour.
2. *(Confinement uniforme.)* Posons $\rho_t=\|z_t-c\|$. Comme $\|Q\|\le1$ et $r$ croissante, $\rho_{t+1}\le r(\|F(z_t)-c\|)\le r(\rho_t+\Delta)=:g(\rho_t)$. $g$ est continue, croissante, $g(0)=\Delta>0$ et $g(R)=r(R+\Delta)<R$, donc $g$ possède un point fixe $\rho^\*\in(0,R)$ ; il est unique car sur $\{\rho+\Delta\le a\}$ on a $g(\rho)=\rho+\Delta>\rho$, et sur $\{\rho+\Delta>a\}$, $g'(\rho)=\tanh'(\cdot)<1$ rend $g-\mathrm{id}$ strictement décroissante. Si $\rho_0\le\rho^\*$, alors $\rho_{t+1}\le g(\rho_t)\le g(\rho^\*)=\rho^\*$ par récurrence ; sinon $\rho_t$ décroît vers $\rho^\*$. Dans tous les cas $\limsup\rho_t\le\rho^\*<R$. ∎

Ce qui est revendiqué : idempotence exacte de $P_{\text{do}}$, annulation exacte le long de $U_x$, confinement uniforme à $\rho^\*<R$. Ce qui n'est **plus** revendiqué : convergence vers $a$ (vraie seulement si $\Delta=0$) et idempotence globale de $\mathcal C$. $\Delta$ est estimé en Phase 0 par le quantile 0,95 de $\|z_{t+1}-\mathcal C(z_t)\|$ (`illustratif`) ; si $\hat\Delta\ge R-a$, $R$ est réajusté avant pré-enregistrement.

```python
def edmd_koopman(X_t, X_t1, phi, ridge=1e-6):
    Psi0 = np.hstack([X_t, phi(X_t)]); Psi1 = np.hstack([X_t1, phi(X_t1)])
    m = Psi0.shape[1]
    K = np.linalg.solve(Psi0.T @ Psi0 + ridge * np.eye(m), Psi0.T @ Psi1)
    w, V = np.linalg.eig(K.T)
    order = np.argsort(-np.abs(w))
    return K, w[order], V[:, order]

def rbf_dict(centers, gamma):
    def phi(X):
        d2 = ((X[:, None, :] - centers[None, :, :]) ** 2).sum(-1)
        return np.exp(-gamma * d2)
    return phi

def drift_directions_state(w, V, d, q, mod_min=1.0):
    """Composante état des modes de module >= mod_min (illustratif), réalifiée puis
    orthonormalisée dans R^d. Une paire conjuguée fournit span{Re, Im} une seule fois."""
    cols = []
    for lam, v in zip(w, V.T):
        if abs(lam) < mod_min or len(cols) >= q: break
        if lam.imag < -1e-10: continue
        vx = v[:d]; cols.append(vx.real)
        if abs(lam.imag) > 1e-10 and len(cols) < q: cols.append(vx.imag)
    M = np.stack(cols[:q], 1)
    Q, _ = np.linalg.qr(M)
    return Q

class DoClamp:
    def __init__(self, Ux, c, a, R):
        self.U, self.c, self.a, self.R = Ux, c, a, R          # a < R (illustratif : a = 0.8 R)
    def P_do(self, x):
        v = x - self.c
        return self.c + v - self.U @ (self.U.T @ v)
    def retract(self, x):
        v = x - self.c; rho = np.linalg.norm(v)
        if rho <= self.a: return x
        r = self.a + (self.R - self.a) * np.tanh((rho - self.a) / (self.R - self.a))
        return self.c + v * (r / rho)
    def __call__(self, x): return self.retract(self.P_do(x))

def check_idempotent(clamp, X, tol=1e-8):
    P1 = np.apply_along_axis(clamp.P_do, 1, X); P2 = np.apply_along_axis(clamp.P_do, 1, P1)
    return float(np.abs(P2 - P1).max()) < tol

def rand_dir_L2(x, delta, q, rng):
    """Bras B-II.5 (C7 corrigé) : direction aléatoire dans un sous-espace Haar de rang q,
    norme L2 égale à ||delta||_2, delta = P_do(x) - x. Contrôle magnitude-vs-direction."""
    G = rng.standard_normal((len(x), q)); Qr, _ = np.linalg.qr(G)
    v = Qr @ rng.standard_normal(q)
    return x + v / np.linalg.norm(v) * np.linalg.norm(delta)

def estimate_Delta(Z_next, Z_clamped, q=0.95):
    """Quantile empirique de ||z_{t+1} - C(z_t)|| pour vérifier H_Delta (q illustratif)."""
    return float(np.quantile(np.linalg.norm(Z_next - Z_clamped, axis=1), q))

def drift_equivalence(refusal_by_turn, margin=0.05, n_boot=5000, seed=0):
    """Endpoint primaire (C8 corrigé) : différence appariée par session r_T - r_1,
    test d'équivalence TOST, margin pré-enregistrée (0.05 illustratif)."""
    diffs = refusal_by_turn[:, -1] - refusal_by_turn[:, 0]
    return tost_paired(diffs, margin, n_boot, seed)
```

**Critère (illustratif) :** sous `Do-Clamp`, TOST concluant à l'équivalence de $r_T-r_1$ dans $\pm0{,}05$ ; sous `B-II.4`, IC à 95 % excluant 0 ; sous `rand-dir`, non-équivalence ou dérive persistante. Quantile conforme gelé hors ligne (vérifié sain) : $q_\alpha=$ score de rang $\lceil(n+1)(1-\alpha)\rceil$ sur l'ensemble de calibration.

### 2.3 Volet III — *Sol/Astra* : schéma fermé, $\Pi_0$, Merkle RFC 6962, $\text{JSD}_{1/2}$ centrée

**Divergence (G4/C9 corrigées).** Je renonce à la pondération par effectifs : avec $\pi_Q=N_Q/(N_P+N_Q)\to0$, la JSD généralisée est majorée par $H_b(\pi_Q)\to0$ bits et le moniteur s'éteint. La statistique est la JSD à poids égaux sur fréquences normalisées,
$$\text{JSD}_{1/2}(\hat P,\hat Q)=H\!\big(\tfrac12\hat P+\tfrac12\hat Q\big)-\tfrac12 H(\hat P)-\tfrac12 H(\hat Q)\in[0,1]\ \text{bit},$$
concave-cohérente, donc $\ge0$ sans troncature. Son biais à petit $N$ n'est pas retiré terme à terme par Miller-Madow (le résidu $\tfrac{m_{P+Q}-m_P-m_Q+1}{2(N_P+N_Q)}$ est précisément l'artefact signalé) : il est **centré** par bootstrap paramétrique sous $H_0$ aux mêmes effectifs $(N_P,N_Q)$, et le seuil est le quantile du même nul. Miller-Madow est conservé uniquement pour l'entropie univariée de chaque flux (formule vérifiée saine).

**Journal (G5/C10 corrigées).** Feuille $=\text{SHA256}(\texttt{0x00}\,\|\,\text{json})$, nœud $=\text{SHA256}(\texttt{0x01}\,\|\,g\,\|\,d)$, arbre non équilibré par scission à la plus grande puissance de 2 strictement inférieure à $n$, aucune duplication ; la tête signée engage $(n,\text{racine})$. Ainsi $[A]$ et $[A,A]$ ont des racines distinctes et $[a,b,c]\ne[a,b,c,c]$.

```python
import json, hashlib, hmac

SCHEMA = {  # S_strict (illustratif)
    "type": "object", "additionalProperties": False,
    "required": ["role", "turn", "action", "payload", "cap_token"],
    "properties": {
        "role":      {"enum": ["Sol", "Astra"]},
        "turn":      {"type": "integer", "minimum": 0},
        "action":    {"enum": ["PROPOSE", "ACCEPT", "REJECT", "DELEGATE", "HALT"]},
        "payload":   {"type": "string", "maxLength": 2048},
        "cap_token": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
    },
}

def validate_strict(msg):
    import jsonschema
    jsonschema.validate(msg, SCHEMA)

def Pi_0(msg, allowed_actions, max_len=2048, forbid=("http://", "https://", "<script")):
    """Prédicat décidable hors-modèle, O(|payload|)."""
    return (msg["action"] in allowed_actions and len(msg["payload"]) <= max_len
            and not any(f in msg["payload"] for f in forbid))

def canon(obj): return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
def leaf_hash(b): return hashlib.sha256(b"\x00" + b).digest()
def node_hash(l, r): return hashlib.sha256(b"\x01" + l + r).digest()

def _split(n): return 1 << ((n - 1).bit_length() - 1)      # plus grande puissance de 2 < n

def mth(leaves):
    """Merkle Tree Hash RFC 6962 sur feuilles déjà hachées (référence à vérifier)."""
    n = len(leaves)
    if n == 0: return hashlib.sha256(b"").digest()
    if n == 1: return leaves[0]
    k = _split(n)
    return node_hash(mth(leaves[:k]), mth(leaves[k:]))

def inclusion_proof(leaves, i):
    n = len(leaves)
    if n == 1: return []
    k = _split(n)
    if i < k:  return inclusion_proof(leaves[:k], i) + [mth(leaves[k:])]
    return inclusion_proof(leaves[k:], i - k) + [mth(leaves[:k])]

def verify_inclusion(leaf, i, n, path, root):
    h = leaf
    while n > 1:
        k = _split(n)
        if i < k: h, n = node_hash(h, path.pop(0)), k
        else:     h, i, n = node_hash(path.pop(0), h), i - k, n - k
    return h == root and not path

class MerkleLog:
    def __init__(self, sth_key):
        self.leaves, self.key = [], sth_key
    def append(self, msg):
        self.leaves.append(leaf_hash(canon(msg)))
        return self.signed_tree_head()
    def signed_tree_head(self):
        n, root = len(self.leaves), mth(self.leaves)
        tag = hmac.new(self.key, n.to_bytes(8, "big") + root, "sha256").hexdigest()
        return {"size": n, "root": root.hex(), "mac": tag}

def entropy_bits(p):
    p = np.asarray(p, float); p = p[p > 0]
    return float(-(p * np.log2(p)).sum())

def entropy_MM_bits(counts):
    """Entropie univariée débiaisée Miller-Madow (vérifiée saine) : (m-1)/(2N) nats -> bits."""
    c = np.asarray(counts, float); N = c.sum(); p = c[c > 0] / N
    return float((-(p * np.log(p)).sum() + ((c > 0).sum() - 1) / (2 * N)) / np.log(2))

def jsd_half_bits(cP, cQ):
    P = np.asarray(cP, float); Q = np.asarray(cQ, float)
    P, Q = P / P.sum(), Q / Q.sum()
    return entropy_bits(0.5 * (P + Q)) - 0.5 * (entropy_bits(P) + entropy_bits(Q))

def jsd_null_calibration(cRef, N_win, n_mc=4000, alpha=0.01, seed=0):
    """Bootstrap paramétrique sous H0 aux effectifs observés (N_ref, N_win) ; alpha illustratif.
    Retourne (biais_0, seuil) : statistique centrée J - biais_0, alarme si J - biais_0 > seuil."""
    rng = np.random.default_rng(seed); cRef = np.asarray(cRef, float)
    p, N_ref = cRef / cRef.sum(), int(cRef.sum())
    null = np.array([jsd_half_bits(rng.multinomial(N_ref, p), rng.multinomial(N_win, p))
                     for _ in range(n_mc)])
    bias0 = null.mean()
    return bias0, float(np.quantile(null, 1 - alpha) - bias0)
```

**Critère (illustratif) :** rejet de 100 % des messages hors schéma ; $\Pi_0$ sans appel au modèle ; alarme si $\text{JSD}_{1/2}-\hat b_0>q_{0{,}99}-\hat b_0$ ; tête signée publiée à chaque tour, chaque participant vérifie l'inclusion de ses propres feuilles.

### 2.4 Volet IV — `H9` : Phase I/II, CUSUM calibré par Brook-Evans et bootstrap, test de Page, seuil conforme gelé, jeton monotone

**Séparation des phases (C12).** Phase I : série de contrôle $x^{\text{I}}$ collectée sans délégation adverse ; on y estime $\hat\phi$ (Yule-Walker), $\hat\mu$, $\hat\sigma$ et on les **gèle**. Phase II : série surveillée, innovations $e_t=(x_t-\hat\mu-\hat\phi(x_{t-1}-\hat\mu))/\hat\sigma_e$ avec paramètres de Phase I uniquement.

**Calibration de $h$ (G7, C12).** ARL$_0$ unilatérale par chaîne de Markov de Brook & Evans 1972 (référence à vérifier) ; le CUSUM bilatéral symétrique vérifie $\text{ARL}_2\approx\text{ARL}_+/2$ (référence à vérifier), d'où cible $\text{ARL}_+=2\cdot370$ (`illustratif`). L'erreur d'estimation de Phase I est intégrée par bootstrap paramétrique : on simule des séries AR(1) de longueur $n_{\text{I}}$, on ré-estime $(\tilde\phi,\tilde\mu,\tilde\sigma)$, on évalue l'ARL sous ces paramètres par Monte-Carlo **sans jeter** les trajectoires censurées (comptées à leur horizon, borne inférieure, donc choix de $h$ conservateur), et on retient le $h$ qui atteint la cible au quantile 0,05 des ARL bootstrapées (`illustratif`).

**Hypothèse ordonnée (C13, C14).** Chaque chaîne de délégation fournit un score à chaque profondeur $d=1..6$ : mesures répétées. Test primaire : $L$ de Page avec blocs = chaînes, nul **exact** par permutation des étiquettes de profondeur à l'intérieur de chaque chaîne. Jonckheere-Terpstra, variance complète à trois termes, n'est utilisé que lorsque chaque chaîne contribue à une seule profondeur.

**Seuil conforme (G6, C15).** $q_\alpha$ est gelé en Phase I. Aucun régulateur sur le flux non étiqueté : forcer $\mathbb P(s_t>q_t)=\alpha$ par rétroaction aveugle rend le détecteur insensible à toute attaque persistante. L'adaptation (de type ACI) n'est admise qu'en présence d'étiquettes vérifiées hors ligne, ce qui n'est pas le régime de `H9`.

```python
from scipy.stats import norm, rankdata

def phase1_fit(x_I):
    x = np.asarray(x_I, float); mu = x.mean(); xc = x - mu
    phi = (xc[1:] * xc[:-1]).sum() / (xc[:-1] ** 2).sum()
    e = xc[1:] - phi * xc[:-1]
    return {"mu": mu, "phi": phi, "sig_e": e.std(ddof=1), "n": len(x)}

def phase2_innovations(x_II, par):
    x = np.asarray(x_II, float) - par["mu"]
    return (x[1:] - par["phi"] * x[:-1]) / par["sig_e"]

def cusum_two_sided(e, k, h):
    Sp = Sm = 0.0
    for t, v in enumerate(e):
        Sp = max(0.0, Sp + v - k); Sm = max(0.0, Sm - v - k)
        if max(Sp, Sm) > h: return t
    return None

def arl_one_sided_markov(k, h, m=200):
    """Brook & Evans 1972 (référence à vérifier) : ARL0 unilatérale, innovations N(0,1)."""
    w = 2 * h / (2 * m + 1); t = np.arange(m + 1) * w
    P = np.zeros((m + 1, m + 1))
    for i in range(m + 1):
        P[i, 0] = norm.cdf(k - t[i] + w / 2)
        for j in range(1, m + 1):
            P[i, j] = norm.cdf(t[j] - t[i] + k + w / 2) - norm.cdf(t[j] - t[i] + k - w / 2)
    arl = np.linalg.solve(np.eye(m + 1) - P, np.ones(m + 1))
    return float(arl[0])

def calibrate_h_markov(k=0.5, arl0=370, grid=np.linspace(2, 8, 121)):
    """h minimal tel que ARL_+ >= 2*arl0 (ARL bilatérale ~ ARL_+/2 ; arl0 illustratif)."""
    for h in grid:
        if arl_one_sided_markov(k, h) >= 2 * arl0: return float(h)
    return float(grid[-1])

def arl_mc_censored(gen_innov, k, h, M=400, L=20000, seed=0):
    """ARL Monte-Carlo : les trajectoires censurées à L sont conservées à la valeur L
    (borne inférieure de l'ARL, donc choix de h conservateur). Retourne (ARL_lb, frac_censure)."""
    rng = np.random.default_rng(seed); rl, cens = [], 0
    for _ in range(M):
        t = cusum_two_sided(gen_innov(L, rng), k, h)
        if t is None: rl.append(L); cens += 1
        else: rl.append(t + 1)
    return float(np.mean(rl)), cens / M

def calibrate_h_bootstrap(par, k=0.5, arl0=370, grid=np.linspace(2, 8, 61),
                          n_boot=50, M=200, L=20000, q=0.05, seed=0):
    """Intègre l'erreur d'estimation de Phase I : simule AR(1) de longueur n_I, ré-estime,
    mesure l'ARL sous mauvaise spécification, retient h tel que le quantile q des ARL >= arl0."""
    rng = np.random.default_rng(seed)
    def sim_ar1(n, phi, r):
        x = np.zeros(n)
        for t in range(1, n): x[t] = phi * x[t - 1] + r.standard_normal()
        return x
    for h in grid:
        arls = []
        for b in range(n_boot):
            est = phase1_fit(sim_ar1(par["n"], par["phi"], rng))
            gen = lambda n, r, est=est: phase2_innovations(sim_ar1(n + 1, par["phi"], r), est)
            arls.append(arl_mc_censored(gen, k, h, M, L, seed=int(rng.integers(1 << 30)))[0])
        if np.quantile(arls, q) >= arl0: return float(h)
    return float(grid[-1])

def page_test_permutation(Y, n_perm=20000, seed=0):
    """Y : (n_chaînes, D) scores, colonne j = profondeur d = j+1 ; H1 : tendance croissante.
    Blocs = chaînes (mesures répétées), nul exact par permutation intra-chaîne (C14)."""
    n, D = Y.shape; wts = np.arange(1, D + 1, dtype=float)
    def L(M): return float((rankdata(M, axis=1) @ wts).sum())
    obs = L(Y); rng = np.random.default_rng(seed); hits = 0
    base = np.tile(np.arange(D), (n, 1))
    for _ in range(n_perm):
        hits += L(np.take_along_axis(Y, rng.permuted(base, axis=1), axis=1)) >= obs
    return obs, (hits + 1) / (n_perm + 1)

def jonckheere_terpstra(groups):
    """Échantillons INDÉPENDANTS seulement. Variance complète avec ex æquo (C13 corrigé)."""
    JT = 0.0; ns = [len(g) for g in groups]; N = sum(ns)
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            a, b = np.asarray(groups[i])[:, None], np.asarray(groups[j])[None, :]
            JT += (b > a).sum() + 0.5 * (b == a).sum()
    mean = (N ** 2 - sum(n ** 2 for n in ns)) / 4
    _, tie = np.unique(np.concatenate(groups), return_counts=True)
    v1 = (N * (N - 1) * (2 * N + 5) - sum(n * (n - 1) * (2 * n + 5) for n in ns)
          - sum(t * (t - 1) * (2 * t + 5) for t in tie)) / 72
    v2 = (sum(n * (n - 1) * (n - 2) for n in ns) * sum(t * (t - 1) * (t - 2) for t in tie)
          / (36 * N * (N - 1) * (N - 2)))
    v3 = sum(n * (n - 1) for n in ns) * sum(t * (t - 1) for t in tie) / (8 * N * (N - 1))
    z = (JT - mean) / np.sqrt(v1 + v2 + v3)
    return JT, z, 1 - norm.cdf(z)

def conformal_quantile_frozen(scores_cal, alpha):
    """Seuil gelé en Phase I : rang ceil((n+1)(1-alpha)) ; aucune mise à jour sur flux non étiqueté."""
    s = np.sort(np.asarray(scores_cal, float)); n = len(s)
    return float(s[min(n - 1, int(np.ceil((n + 1) * (1 - alpha))) - 1)])

class MonotoneCapToken:
    """Pi_{d+1} ⊆ Pi_d : chaque délégation intersecte l'ensemble de capacités et rechaîne
    un HMAC (schéma macaroon, référence à vérifier). Ré-escalade impossible sans la clé racine."""
    def __init__(self, root_key, caps):
        self.caps = sorted(set(caps)); self.chain = [self.caps]
        self.sig = hmac.new(root_key, canon(self.caps), "sha256").digest()
    def attenuate(self, keep):
        child = object.__new__(MonotoneCapToken)
        child.caps = sorted(set(self.caps) & set(keep))
        child.chain = self.chain + [child.caps]
        child.sig = hmac.new(self.sig, canon(child.caps), "sha256").digest()
        return child
    @staticmethod
    def verify(root_key, token):
        sig = hmac.new(root_key, canon(token.chain[0]), "sha256").digest()
        for prev, cur in zip(token.chain, token.chain[1:]):
            if not set(cur) <= set(prev): return False
            sig = hmac.new(sig, canon(cur), "sha256").digest()
        return hmac.compare_digest(sig, token.sig)
    def hex(self): return self.sig.hex()
```

**Critère (illustratif) :** ARL$_0\ge370$ au quantile 0,05 bootstrap, détection d'un saut de $1\sigma_e$ en moins de 15 tours ; $p_{\text{Page}}<0{,}01$ pour l'érosion croissante ; `verify` rejette 100 % des jetons ré-escaladés ; taux d'alarme conforme sur flux bénin dans $[\alpha/2, 2\alpha]$ avec $q_\alpha$ gelé.

### 2.5 Volet V — `H4'`, Chimère Tri-Espèces : strates par paire de familles, CMH conditionnel, Breslow-Day, HMP, borne PBFT

**Plan.** Trois familles de poids ouverts $\mathcal F_1,\mathcal F_2,\mathcal F_3$ (`illustratif` : trois lignées distinctes à 7–8 B paramètres, références à vérifier), empreintes `sha256` des poids engagées dans le journal de § 2.3 **avant** tout épisode (Kerckhoffs). Un épisode = un saboteur de famille $i$, un auditeur de famille $j\ne i$, un traitement (sabotage présent / absent), un verdict (signalé / non). Strates = paires ordonnées $(i,j)$, six au total.

**Indépendance et fuite (G3, C16).** Chaque épisode appartient à exactement une strate, avec graine, transcription et instance fraîches ; aucune transcription n'est partagée entre strates. La calibration du seuil de décision de l'auditeur (et tout prompt ajusté) est obtenue par **leave-one-family-out** : pour évaluer les épisodes dont le saboteur est de famille $i$, la calibration n'utilise que les épisodes de saboteurs des familles $\ne i$. Le stratifieur externe (panel gelé) reste exclu des familles évaluées (vérifié sain). Le nul de CMH est obtenu par permutation du traitement à l'intérieur de chaque strate : les marges de chaque table $2\times2$ sont conservées exactement, ce qui restitue la loi conditionnelle sans invoquer le $\chi^2_1$ asymptotique.

**Combinaison et quorum.** $p$-valeurs par famille de saboteur combinées par HMP (Wilson 2019, référence à vérifier) avec garantie $p_{\text{valide}}=\min(1, e\ln L\cdot\text{HMP})$ (Vovk & Wang 2020, référence à vérifier). Borne PBFT $N\ge3f+1$ : avec trois familles d'auditeurs, tolérer la collusion d'une **famille entière** est impossible (il faudrait $N\ge3\lceil N/3\rceil+1$) ; le protocole tolère donc $f=1$ auditeur byzantin pour $N=4$ (répartition 2/1/1, `illustratif`) et exige une quatrième famille pour couvrir la collusion de famille complète. Je le déclare plutôt que de le masquer.

```python
def tables_from_episodes(stratum, treat, flag, S):
    T = np.zeros((S, 2, 2), float)
    for s, t, y in zip(stratum, treat, flag): T[s, 1 - t, 1 - y] += 1   # [a b; c d], a = traité & signalé
    return T

def cmh_statistic(T):
    num = var = 0.0
    for a, b, c, d in T.reshape(-1, 4):
        n = a + b + c + d
        if n < 2: continue
        r1, r2, c1, c2 = a + b, c + d, a + c, b + d
        num += a - r1 * c1 / n
        var += r1 * r2 * c1 * c2 / (n ** 2 * (n - 1))
    return num ** 2 / var if var > 0 else 0.0

def cmh_permutation(stratum, treat, flag, S, n_perm=10000, seed=0):
    """Nul conditionnel exact : permutation du traitement intra-strate (marges conservées)."""
    stratum, treat, flag = map(np.asarray, (stratum, treat, flag))
    obs = cmh_statistic(tables_from_episodes(stratum, treat, flag, S))
    rng = np.random.default_rng(seed); tp = treat.copy(); hits = 0
    idx = [np.where(stratum == s)[0] for s in range(S)]
    for _ in range(n_perm):
        for ix in idx: tp[ix] = rng.permutation(treat[ix])
        hits += cmh_statistic(tables_from_episodes(stratum, tp, flag, S)) >= obs
    return obs, (hits + 1) / (n_perm + 1)

def mh_odds_ratio(T):
    num = sum(a * d / (a + b + c + d) for a, b, c, d in T.reshape(-1, 4))
    den = sum(b * c / (a + b + c + d) for a, b, c, d in T.reshape(-1, 4))
    return num / den

def breslow_day(T):
    from scipy.stats import chi2
    OR = mh_odds_ratio(T); X2 = 0.0; S = 0
    for a, b, c, d in T.reshape(-1, 4):
        n = a + b + c + d; r1, c1 = a + b, a + c
        if abs(OR - 1) < 1e-12: ae = r1 * c1 / n
        else:
            A, B, C = 1 - OR, (n - r1 - c1) + OR * (r1 + c1), -OR * r1 * c1
            roots = np.roots([A, B, C]).real
            ae = [x for x in roots if 0 <= x <= min(r1, c1)][0]
        cells = np.array([ae, r1 - ae, c1 - ae, n - r1 - c1 + ae])
        if (cells <= 0).any(): continue
        X2 += (a - ae) ** 2 / (1.0 / (1.0 / cells).sum()); S += 1
    return OR, X2, 1 - chi2.cdf(X2, S - 1)

def leave_one_family_out_thresholds(fam_sab, scores, labels, alpha):
    """Pour chaque famille de saboteur i, seuil conforme gelé calibré sur les épisodes
    dont le saboteur n'est PAS de famille i (cross-fitting par cluster, C16)."""
    fam_sab, scores, labels = map(np.asarray, (fam_sab, scores, labels))
    return {i: conformal_quantile_frozen(scores[(fam_sab != i) & (labels == 0)], alpha)
            for i in np.unique(fam_sab)}

def harmonic_mean_p(ps, weights=None):
    ps = np.asarray(ps, float); L = len(ps)
    w = np.ones(L) / L if weights is None else np.asarray(weights, float) / np.sum(weights)
    hmp = 1.0 / (w / ps).sum()
    return hmp, min(1.0, np.e * np.log(L) * hmp)       # borne Vovk & Wang (référence à vérifier)

def pbft_quorum(N, f): return N >= 3 * f + 1

def simpson_demo():
    """B-V.1 : deux strates où l'association intra-strate est positive mais l'OR poolé < 1."""
    T = np.array([[[90., 10.], [60., 10.]],      # strate 1 : OR = 1.5
                  [[ 7., 30.], [20., 150.]]])    # strate 2 : OR = 1.75
    pooled = T.sum(0); a, b, c, d = pooled.ravel()
    return (a * d) / (b * c), [ (t[0,0]*t[1,1])/(t[0,1]*t[1,0]) for t in T ]
```

**Critère (illustratif) :** $p_{\text{CMH,perm}}<0{,}01$ pour l'effet « auditeur hors-famille détecte le sabotage » ; Breslow-Day $p\ge0{,}05$ ou, à défaut, rapport des OR par strate ; `B-V.4` (intra-famille) doit présenter un OR$_{\text{MH}}$ strictement inférieur ; `simpson_demo` reproduit au moins une inversion sur données réelles ; HMP validé sur les trois familles de saboteur.

---

## 3. CAMPAGNE 72 h GPU / 500 USD

**Matériel (illustratif).** Une instance 1× A100 80 GB à ≈ 5,5 USD/h stockage compris, soit ≈ 396 USD pour 72 h ; réserve ≈ 100 USD (CPU de calibration, inférence API ponctuelle pour `B-III.3`). Modèles : une famille à 7–8 B pour les Volets I, II, IV ; trois familles pour le Volet V ; toutes en bf16 avec extraction résiduelle en float64 hors BOS (vérifié sain).

| Phase | Heures | Contenu | Livrables |
|---|---|---|---|
| 0 — Pré-enregistrement | 8 | Extraction $h_{k=0}$ sur 2 400 items (600 par bras A/C/B/L, 24 blocs) ; estimation de $\hat\Delta$, de $(\hat\phi,\hat\mu,\hat\sigma)$ Phase I ; calibration de tous les seuils `illustratif` | JSON des seuils, racine Merkle publiée, empreintes des poids |
| I — Jumeau Nié | 12 | Volet I : $S_{\text{TD}}$ (Gram et cross-fit), nul exact $2^{24}$ par Monte-Carlo $10^5$, TOST lexical, angle, canal subliminal, `B-I.1`–`B-I.4` | $d_z$, $p$, IC, cosinus, rapport de fuite |
| II — Do-Clamp | 14 | 400 sessions × 12 tours, six bras (`Do-Clamp`, `B-II.1`–`B-II.5`), EDMD sur Phase 0, vérification $H_\Delta$ | TOST de dérive, $\rho^\*$ empirique, $\hat\Delta$ |
| III — Sol/Astra | 6 | 2 000 dialogues dyadiques, 300 injections, moniteur JSD centré, journal RFC 6962 | taux de rejet, courbe ROC du moniteur, preuves d'inclusion |
| IV — H9 | 14 | 300 chaînes × 6 profondeurs, CUSUM Phase II, test de Page, jetons monotones, `B-IV.1`–`B-IV.4` | ARL observé, $p_{\text{Page}}$, délais de détection |
| V — H4' | 16 | 3 familles, 6 strates × 150 épisodes, LOFO, CMH par permutation, Breslow-Day, HMP, `B-V.1`–`B-V.4` | OR$_{\text{MH}}$, $p$, démonstration de Simpson |
| Clôture | 2 | Vérification des têtes Merkle, archivage, rapport de non-conformité | dossier scellé |

Total : 72 h. Tout résultat qui échoue à son critère pré-enregistré est publié comme **invalidation** du volet, sans recalibration a posteriori ; les seuils ne peuvent être modifiés que par un nouveau pré-enregistrement engagé dans le journal, ce qui rend la modification elle-même non répudiable.

---

## 4. CE QUI EST REVENDIQUÉ, CE QUI NE L'EST PAS

Revendiqué sous réserve : (I) la paire acte/intention avec pivot nié et jumeau lexical, testée au rang $k=0$ sur un substrat dont la construction est invariante aux signes, avec nul exact et équivalence TOST ; (II) le couplage identification Koopman → projection affine réalisable → rétraction $C^1$, avec confinement démontré sous dérive bornée mesurée ; (III) l'enveloppe dyadique à journal RFC 6962 et divergence centrée sous nul aux effectifs observés ; (IV) la chaîne Phase I/II → CUSUM calibré par Brook-Evans et bootstrap → test de Page intra-chaîne → jeton monotone ; (V) l'audit croisé stratifié par paire de familles avec cross-fitting par cluster et nul conditionnel exact.

Non revendiqué : l'idempotence (LEACE), le CUSUM sur résidus AR(1) (Lu & Reynolds), le journal Merkle (RFC 6962), la tolérance d'une famille entière de collusion avec trois familles seulement, la convergence vers $a$ sous dynamique non nulle, et toute exactitude de niveau qui dépendrait d'un seuil adapté sur un flux non étiqueté.

FIN-CELLULE-CERTIFIEE-54
