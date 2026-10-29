# Consolidation M2 → M1 — protocole final (prêt pour M0 PyTorch, Llama‑3.1)

**Pièces manquantes (une ligne chacune) :** `{lettre}`, `{autres}`, `{mots}` sont vides dans l'en‑tête ; `{marqueur}` est vide mais la mission demande explicitement `FIN-PONT-M2-CONSOLIDE`, que j'émets. La matrice de prédation M3, les règles L\*v2‑1 à 3, `S_TD` et le détail de l'échec de la sonde restent non transmis ; je ne les reconstruis pas. Les trois résumés 1301.2158, 2604.26748, 1310.7906 sont coupés ; accents corrompus (« ? ») lus à travers.

## 0. Ce que je retiens de l'attaque, ce que je rejette

Les huit failles sont acceptées. Je **rejette** un seul point implicite : la proposition initiale traitait l'échec de la sonde comme déjà structurel ; après F5 et F6, « sans mémoire » doit se lire **« décodeur sur la dernière position de la fenêtre »**, car $h_\ell^{(t)}$ intègre déjà le contexte causal. H_A est donc reformulée, pas seulement corrigée.

## 1. Ancrage (F2 corrigé)

- RAPPORTÉ (résumé 2407.21732, référence à vérifier) : la mémoire d'entrée/sortie affecte la communication zéro‑erreur. Rien de plus n'est retenu de cet article.
- VÉRIFIÉ (attribution) : la formule $\Theta=\sup_n \frac1n\log_2\alpha(G^{\boxtimes n})$ vient de Shannon, 1956, *The zero error capacity of a noisy channel*, canal sans mémoire. Le fait que $\alpha(G^{\boxtimes n})^{1/n}>\alpha(G)$ est possible sans mémoire est établi par Lovász, 1979, *On the Shannon capacity of a graph* ($\alpha(C_5)=2$, $\Theta(C_5)=\sqrt5$).
- HYPOTHÈSE de transfert : la mémoire, propriété du canal chez l'auteur, est ici placée dans le **décodeur**. C'est un changement d'objet assumé et déclaré ; il est falsifiable par le nul conditionnel (§4).

## 2. Hypothèses exclusives (B4)

Fixons une couche $\ell$, un départ $t_0$, une longueur $n$, un nombre de cellules $M$ commun.

- **H_A (code à mémoire séquentielle)** : la classe de contrordre est séparable à partir de la fenêtre $h_\ell^{(t_0..t_0+n-1)}$ **et** cette séparabilité dépend de la dépendance conjointe entre positions, pas seulement des marginales par position ni de la dernière position.
- **H_B (pas de code à mémoire)** : toute séparabilité de la fenêtre est reproduite soit par la dernière position seule (linéaire ou MLP), soit par le nul conditionnel qui conserve les marginales par position.

Observable principale (F1 corrigé) :
$$O(\ell,t_0,n)=\frac{\log_2\alpha(G_n)-\log_2\alpha(G_1)}{\log_2K}\in[-1;1],$$
avec $G_1$ construit sur la **dernière position** de la même fenêtre (F5) et $G_n$ sur la fenêtre concaténée, **même nombre $M$ de cellules**, partitions apprises sur une partition disjointe (F4).

Statistique de décision (F3) : $\Delta=O_{\text{réel}}-Q_{95}\big(O_{\text{nul}}\big)$, où $O_{\text{nul}}$ est la distribution sous le nul conditionnel.

## 3. Bras expérimentaux

| Bras | Entrée | Décodeur | Rôle |
|---|---|---|---|
| A | fenêtre $n$ positions | cellules $q_n$ (zéro‑erreur) + MLP (ε‑erreur) | mesure |
| B | dernière position | cellules $q_1$ + sonde linéaire | F5 |
| C | dernière position | MLP | F6 : si C atteint la précision de A, H_A falsifiée quel que soit $O$ |
| N | fenêtre reconstruite position par position depuis d'autres essais de même classe | comme A | F3 : nul canal sans mémoire conditionnel |

Version à erreur ε (F8) : précision test du MLP‑fenêtre contre MLP‑dernière‑position et contre MLP‑nul, mêmes partitions, mêmes seeds. Les deux versions sont rapportées côte à côte ; une divergence entre elles est déclarée, non arbitrée.

## 4. Critères (tous `illustratifs`, à préenregistrer avant M0)

- Couche préenregistrée : $\ell=16$ ; balayage secondaire 2–22 avec Bonferroni $0{,}05/21$ (F7).
- $t_0=1$ (après BOS), $n=8$, $M=64$, $K\le8$ donc $\alpha$ exact.
- Troncature : essai exclu si longueur $<t_0+n$ ; fraction exclue publiée ; si $>20\%$, on réduit $n$ et on le dit. Aucun remplissage (le padding fabrique des collisions).
- $\hat I_A$ : $\Delta\ge0{,}25$ **et** précision(C) $<$ précision(A) $-\,0{,}10$. $\hat I_B$ : $\Delta\le0{,}10$ **ou** précision(C) $\ge$ précision(A) $-\,0{,}10$. Entre les deux : non conclusif, déclaré tel quel.
- Courbe $O(N)$ pour $N\in\{50,100,200,400,\dots\}$ par classe (F4) ; une $O$ qui dérive de façon monotone avec $N$ sans plateau invalide l'estimateur zéro‑erreur et seul le bras ε est lu.
- Pré‑test synthétique obligatoire (F1) : générateur où la classe est codée (a) par parité d'un bit réparti sur les $n$ positions, (b) par la seule dernière position. Le protocole est jugé exécutable seulement si (a) tombe dans $\hat I_A$ et (b) dans $\hat I_B$. Sinon, il n'est pas lancé sur Llama.

Tenseurs (RAPPORTÉ de mémoire, à vérifier sur `config.json`) : 32 blocs, $d=4096$, `hidden_states` de longueur 33, indice 0 = embeddings ; la couche $\ell$ désigne `hidden_states[ℓ]`.

## 5. Code PyTorch `compute_O`

```python
import math, itertools, torch

def kmeans(X, M, iters=50, seed=0):
    g = torch.Generator().manual_seed(seed)
    C = X[torch.randperm(X.shape[0], generator=g)[:M]].clone()
    for _ in range(iters):
        a = torch.cdist(X, C).argmin(1)
        for j in range(M):
            s = X[a == j]
            if len(s): C[j] = s.mean(0)
    return C

def assign(X, C): return torch.cdist(X, C).argmin(1)

def confus_graph(cells, y, K):
    adj = [[False]*K for _ in range(K)]
    for u in cells.unique():
        cl = y[cells == u].unique().tolist()
        for i, j in itertools.combinations(cl, 2):
            adj[i][j] = adj[j][i] = True
    return adj

def alpha_exact(adj, K):                      # K <= 8, exact
    for r in range(K, 0, -1):
        for S in itertools.combinations(range(K), r):
            if all(not adj[i][j] for i, j in itertools.combinations(S, 2)):
                return r
    return 1

def windows(data, l, t0, n):
    H, L = data["H"][l], data["lengths"]      # H: [N, T, d]
    keep = L >= t0 + n
    return H[keep, t0:t0+n, :], data["labels"][keep], data["is_train"][keep], keep

def compute_O(data, l, t0, n, M=64, seed=0, W=None, y=None, tr=None):
    if W is None: W, y, tr, _ = windows(data, l, t0, n)
    K = int(y.max()) + 1
    X1 = W[:, -1, :]                          # derniere position (F5)
    Xn = W.reshape(W.shape[0], -1)            # fenetre concatenee
    C1, Cn = kmeans(X1[tr], M, seed=seed), kmeans(Xn[tr], M, seed=seed)  # meme M (F4)
    te = ~tr
    a1 = alpha_exact(confus_graph(assign(X1[te], C1), y[te], K), K)
    an = alpha_exact(confus_graph(assign(Xn[te], Cn), y[te], K), K)
    return (math.log2(an) - math.log2(a1)) / math.log2(K)   # F1 : [-1, 1]

def nul_conditionnel(W, y, seed):             # F3 : memoryless conditionnel
    g = torch.Generator().manual_seed(seed)
    Wn = W.clone()
    for c in y.unique():
        idx = (y == c).nonzero().squeeze(1)
        for t in range(W.shape[1]):
            Wn[idx, t, :] = W[idx[torch.randperm(len(idx), generator=g)], t, :]
    return Wn

def delta(data, l, t0, n, M=64, B=200, seed=0):
    W, y, tr, _ = windows(data, l, t0, n)
    O_reel = compute_O(data, l, t0, n, M, seed, W, y, tr)
    O_nul = torch.tensor([compute_O(data, l, t0, n, M, seed,
                          nul_conditionnel(W, y, seed + b), y, tr) for b in range(B)])
    return O_reel, O_nul, O_reel - torch.quantile(O_nul, 0.95).item()
```

Bras ε (F6/F8) : un `torch.nn.Sequential(Linear, GELU, Linear)` entraîné sur `Xn[tr]`, `X1[tr]` et `nul(Xn)[tr]`, précision lue sur `te` ; même split, même seed. Non reproduit ici faute de place.

## 6. Ce que chaque issue falsifie

- $\hat I_A$ : falsifie « une sonde mieux entraînée ou un MLP sur la dernière position suffirait » et falsifie « la séparabilité de la fenêtre vient des marginales par position ».
- $\hat I_B$ : falsifie « le canal subliminal est un code à mémoire séquentielle » ; l'échec de la sonde relève alors de la non‑linéarité (si C réussit), de la puissance (courbe $O(N)$) ou de la couche.
- Pré‑test synthétique négatif : falsifie l'opérateur lui‑même, avant toute donnée Llama.

**Statut global :** aucune valeur de $O$, $\Delta$ ou précision n'existe. Tout chiffre ci‑dessus est illustratif ; le pont reste HYPOTHÈSE, l'ancrage RAPPORTÉ, les attributions Shannon 1956 et Lovász 1979 VÉRIFIÉES.

FIN-PONT-M2-CONSOLIDE
