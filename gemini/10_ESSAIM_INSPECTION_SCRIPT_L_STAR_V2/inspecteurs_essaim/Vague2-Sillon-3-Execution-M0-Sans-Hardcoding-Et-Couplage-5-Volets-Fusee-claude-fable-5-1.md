# RAPPORT D'ESSAIM — VAGUE 2/2 — ÉTAGE M0 & FUSÉE À 5 VOLETS (queue de distribution)

Les onze failles ci-dessous sont orthogonales à la liste de la Vague 1 : elles ne portent pas sur l'*absence* des mécanismes, mais sur ce qui rendrait ces mécanismes **faux même une fois présents**.

---

BUG_L_STAR_V2: [Sillon-3-M0-Execution-Sandbox] Exécution de `compute_O(data)` sans isolation, sans horloge-gardienne, sans graine figée et sans contrat de type sur la valeur de retour
PREUVE_NON_CONFORMITE: Remplacer `ast.parse` par un `exec` nu réintroduit trois zones mortes : (i) une fonction `compute_O` qui boucle (`while True`) rend le verdict M0 indéfini (halting) ; (ii) sans `random.seed` figé, deux audits du même bloc donnent deux $O$ différents — l'observable n'est plus reproductible (règle B4, zéro zone morte) ; (iii) un retour `nan`, `inf`, `bool` ou `str` traverse les comparaisons Python sans lever d'erreur (`nan > 0.5` est `False` silencieusement) et produit un verdict $H_B$ par accident. L*v2 exige qu'un instrument défaillant donne `INVALIDE-instrument`, jamais un verdict scientifique.
CORRECTIF_PYTHON_EXACT:
```python
import ast, math, random, signal, builtins

_SAFE_BUILTINS = {k: getattr(builtins, k) for k in
    ("abs","min","max","sum","len","range","enumerate","zip","float","int",
     "list","dict","tuple","set","sorted","map","filter","round","pow","all","any","isinstance")}

class _Timeout(Exception): pass
def _alarm(signum, frame): raise _Timeout()

def run_compute_O(code_block, data, seed=12345, timeout_s=5):
    """Exécute compute_O(data) extraite de M1 dans un espace confiné.
    Retourne (statut, valeur). statut in {'OK','INVALIDE-instrument'}."""
    tree = ast.parse(code_block)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if not all(a.name in ("math","random","statistics","itertools") for a in node.names):
                return ("INVALIDE-instrument", "import interdit")
        if isinstance(node, ast.Attribute) and node.attr.startswith("__"):
            return ("INVALIDE-instrument", "attribut dunder interdit")
    ns = {"__builtins__": _SAFE_BUILTINS, "math": math, "random": random}
    random.seed(seed)
    old = signal.signal(signal.SIGALRM, _alarm); signal.alarm(timeout_s)
    try:
        exec(compile(tree, "<compute_O>", "exec"), ns)
        f = ns.get("compute_O")
        if not callable(f):
            return ("INVALIDE-instrument", "compute_O absente")
        val = f(data)
    except _Timeout:
        return ("INVALIDE-instrument", "timeout")
    except Exception as e:
        return ("INVALIDE-instrument", f"exception:{type(e).__name__}")
    finally:
        signal.alarm(0); signal.signal(signal.SIGALRM, old)
    # Contrat de type : flottant fini, non booléen, ou vecteur de tels flottants
    def _ok(x): return (isinstance(x, (int, float)) and not isinstance(x, bool)
                        and math.isfinite(float(x)))
    if _ok(val): return ("OK", float(val))
    if isinstance(val, (list, tuple)) and len(val) > 0 and all(_ok(x) for x in val):
        return ("OK", [float(x) for x in val])
    return ("INVALIDE-instrument", "retour non numérique/non fini")
```

---

BUG_L_STAR_V2: [Sillon-3-M0-F1-Null] Pré-test synthétique F1 sans nul de permutation ni borne du prédicteur constant : un `compute_O` dégénéré passe la porte
PREUVE_NON_CONFORMITE: Sur un jeu synthétique de prévalence $\pi$, le prédicteur « tout positif » obtient $F_1 = 2\pi/(1+\pi)$ ; à $\pi = 0{,}8$ cela donne $0{,}889$. Un seuil fixe (type « $F_1 \ge 0{,}85$ ») laisse donc passer une fonction qui n'a rien calculé. L*v2 exige un **contrôle négatif** (ici : étiquettes permutées) et une comparaison à la borne dégénérée, faute de quoi le pré-test F1 est une porte ouverte.
CORRECTIF_PYTHON_EXACT:
```python
import random, math

def f1_score(y_true, y_pred):
    tp = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
    fp = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
    fn = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
    return 0.0 if (2*tp+fp+fn)==0 else 2*tp/(2*tp+fp+fn)

def pretest_F1(compute_O, synth_X, synth_y, thr=0.5, B=999, alpha=0.01, seed=7):
    """Pré-test F1 avec (a) borne du prédicteur constant, (b) nul de permutation."""
    rng = random.Random(seed)
    pred = [1 if compute_O(x) > thr else 0 for x in synth_X]
    f1_obs = f1_score(synth_y, pred)
    pi = sum(synth_y)/len(synth_y)
    f1_const = max(2*pi/(1+pi), 0.0)              # 'tout positif' ; 'tout négatif' donne 0
    null = []
    for _ in range(B):
        yp = synth_y[:]; rng.shuffle(yp)
        null.append(f1_score(yp, pred))
    p_perm = (1 + sum(1 for v in null if v >= f1_obs)) / (B + 1)
    q = sorted(null)[int(math.ceil((1-alpha)*B))-1]
    passed = (f1_obs > f1_const) and (f1_obs > q) and (p_perm <= alpha)
    return {"F1": f1_obs, "F1_constant": f1_const, "q_null": q, "p_perm": p_perm,
            "verdict": "OK" if passed else "INVALIDE-instrument"}
```

---

BUG_L_STAR_V2: [Sillon-3-M0-Binding] Résultats M0 non liés cryptographiquement au code audité : le dictionnaire de vérification est substituable à l'AST près
PREUVE_NON_CONFORMITE: Même dérivé dynamiquement, un dictionnaire `m0_5volets_verification` qui ne porte pas l'empreinte du code dont il provient peut être recollé sur un autre `compute_O` (ou sur une version tronquée de M1, cf. $\kappa$). Kerckhoffs appliqué à M0 : l'adversaire connaissant l'instrument ne doit pas pouvoir présenter un résultat valide pour un code différent. Il faut lier chaque entrée à `SHA-256(ast.dump(normalisé))` et invalider toute désynchronisation.
CORRECTIF_PYTHON_EXACT:
```python
import ast, hashlib, json

def code_fingerprint(code_block):
    tree = ast.parse(code_block)
    for n in ast.walk(tree):                      # normalisation : positions et docstrings ôtées
        for a in ("lineno","col_offset","end_lineno","end_col_offset"):
            if hasattr(n, a): setattr(n, a, 0)
    return hashlib.sha256(ast.dump(tree, annotate_fields=False).encode()).hexdigest()

def bind_result(code_block, volet, value):
    return {"volet": volet, "value": value, "code_sha256": code_fingerprint(code_block)}

def verify_binding(entries, code_blocks):
    """entries: liste de bind_result ; code_blocks: dict volet->code. Verdict total."""
    for e in entries:
        cb = code_blocks.get(e["volet"])
        if cb is None or code_fingerprint(cb) != e["code_sha256"]:
            return "INVALIDE-instrument"
    return "OK"
```

---

BUG_L_STAR_V2: [Sillon-3-Volet-I] $d_z$ par bloc auteur sans correction de petit échantillon ni garde $\sigma=0$, et nul de permutation par **mélange d'étiquettes** au lieu de **retournement de signe intra-bloc** sur données appariées
PREUVE_NON_CONFORMITE: $\ell_h$ (Fable T4) repose sur $q_{1-\alpha/4}(d^C_{z,h,\text{perm}})$. Pour des différences appariées, le nul correct sous $H_0$ est le groupe des retournements de signe $\{\pm1\}^n$ **au sein de chaque bloc** (Fable, Opus, Argon) ; un mélange global d'étiquettes brise l'appariement et casse la stratification, ce qui déforme le quantile et donc l'ancrage au nul. De plus $d_z = \bar{d}/s_d$ est biaisé vers le haut pour $n<20$ (facteur de Hedges $J(n-1)$) et indéfini quand $s_d = 0$ (tête constante) — cas précisément visé par le Jumeau Nié k=0.
CORRECTIF_PYTHON_EXACT:
```python
import math, random

def hedges_J(df):                 # J(df) ≈ 1 - 3/(4 df - 1)
    return 1.0 - 3.0/(4.0*df - 1.0) if df > 1 else 0.0

def dz_block(diffs):
    n = len(diffs)
    if n < 2: return None
    m = sum(diffs)/n
    s2 = sum((x-m)**2 for x in diffs)/(n-1)
    if s2 == 0.0: return None          # garde σ=0 → tête constante → INVALIDE (pas 0, pas ±inf)
    return hedges_J(n-1) * m / math.sqrt(s2)

def dz_blocs_egaux(blocks):
    """blocks: dict auteur -> liste de différences appariées. Moyenne à poids égaux par bloc."""
    vals = [dz_block(v) for v in blocks.values()]
    if any(v is None for v in vals): return None
    return sum(vals)/len(vals)

def quantile_signflip(blocks, q, B=4999, seed=11):
    rng = random.Random(seed); out = []
    for _ in range(B):
        perm = {k: [x*rng.choice((-1,1)) for x in v] for k,v in blocks.items()}  # intra-bloc
        d = dz_blocs_egaux(perm)
        if d is not None: out.append(d)
    out.sort(); return out[min(len(out)-1, int(math.ceil(q*len(out)))-1)]

def ell_h(blocks_C, blocks_R, delta_R, alpha=0.01):
    dC = dz_blocs_egaux(blocks_C)
    dR = dz_blocs_egaux({k:[abs(x) for x in v] for k,v in blocks_R.items()})
    if dC is None or dR is None: return ("INVALIDE-instrument", None)
    qC = quantile_signflip(blocks_C, 1-alpha/4)
    uR = quantile_signflip({k:[abs(x) for x in v] for k,v in blocks_R.items()}, 1-alpha/4)
    return ("OK", min(dC - qC, delta_R - max(dR, uR)))
```

---

BUG_L_STAR_V2: [Sillon-3-Volet-II] Do-Clamp non idempotent (direction non normalisée, clamp linéaire au lieu d'affine pour $do(z=c)$) et contournement Koopman testé sans dictionnaire d'observables lifté
PREUVE_NON_CONFORMITE: Une rétraction $r$ doit vérifier $r\circ r = r$ (C1 et idempotente). Le clamp $v - (v\cdot u)\,u$ n'est idempotent que si $\|u\|=1$ ; avec $u$ non normalisé, deux applications successives donnent deux états différents et l'intervention « $do$ » n'est pas une intervention. Pour $do(z=c)$ avec $c\neq0$, la forme correcte est affine : $v - (v\cdot u - c)\,u$. Enfin, un contournement non-linéaire ne se détecte pas en régressant linéairement la cible sur le résidu (c'est exactement ce que la sonde linéaire de `P3` ne voit pas) : il faut lever le résidu dans un dictionnaire $\Psi$ (EDMD/Koopman) et comparer le $R^2$ lifté à un nul de permutation.
CORRECTIF_PYTHON_EXACT:
```python
import math, random

def do_clamp(v, u, c=0.0):
    nu = math.sqrt(sum(x*x for x in u))
    if nu == 0.0: raise ValueError("direction nulle")
    uh = [x/nu for x in u]
    s = sum(a*b for a,b in zip(v, uh)) - c
    return [a - s*b for a,b in zip(v, uh)]

def assert_idempotent(v, u, c=0.0, tol=1e-9):
    w1 = do_clamp(v,u,c); w2 = do_clamp(w1,u,c)
    return max(abs(a-b) for a,b in zip(w1,w2)) < tol

def _solve(A, b):                      # Gauss-Jordan avec pivot partiel + ridge minimal
    n = len(A); M = [row[:] + [b[i]] for i,row in enumerate(A)]
    for i in range(n): M[i][i] += 1e-10
    for i in range(n):
        p = max(range(i,n), key=lambda r: abs(M[r][i])); M[i],M[p] = M[p],M[i]
        for r in range(n):
            if r != i:
                f = M[r][i]/M[i][i]
                M[r] = [x - f*y for x,y in zip(M[r], M[i])]
    return [M[i][n]/M[i][i] for i in range(n)]

def lift(x):                           # dictionnaire Ψ : 1, x_i, x_i², x_i x_j (i<j)
    out = [1.0] + list(x) + [a*a for a in x]
    out += [x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x))]
    return out

def r2_lifted(X, y):
    Z = [lift(x) for x in X]; k = len(Z[0])
    A = [[sum(z[i]*z[j] for z in Z) for j in range(k)] for i in range(k)]
    b = [sum(z[i]*yy for z,yy in zip(Z,y)) for i in range(k)]
    w = _solve(A, b)
    pred = [sum(wi*zi for wi,zi in zip(w,z)) for z in Z]
    ym = sum(y)/len(y); ss = sum((t-ym)**2 for t in y)
    return 0.0 if ss == 0 else 1 - sum((t-p)**2 for t,p in zip(y,pred))/ss

def koopman_bypass_test(X_clamped, y, B=499, alpha=0.01, seed=3):
    rng = random.Random(seed); r_obs = r2_lifted(X_clamped, y); null = []
    for _ in range(B):
        yp = y[:]; rng.shuffle(yp); null.append(r2_lifted(X_clamped, yp))
    p = (1 + sum(1 for v in null if v >= r_obs))/(B+1)
    return {"R2_lifted": r_obs, "p": p, "bypass": p <= alpha}
```

---

BUG_L_STAR_V2: [Sillon-3-Volet-III] Divergence de Jensen-Shannon Sol/Astra en estimateur « plug-in » : biais positif systématique, base non fixée, lissage $\varepsilon$ ad hoc — $D_{JS}>0$ même sous $H_0$
PREUVE_NON_CONFORMITE: $\hat D_{JS}$ calculée sur des fréquences empiriques est biaisée vers le haut d'ordre $(K-1)/(2n\ln 2)$ par distribution (Miller-Madow) : deux échantillons de la **même** loi donnent $\hat D_{JS} > 0$, donc un couplage Sol/Astra « détecté » par construction. Un lissage $\varepsilon$ additif introduit une constante codée en dur déguisée et déplace la masse. Sans base 2, la borne $[0,1]$ et le seuil comparatif sur $S_{\text{TD}}$ n'ont pas de sens. La version conforme : mélange $M=(P+Q)/2$ (aucun $\varepsilon$ nécessaire, $P\ll M$), base 2, correction de Miller-Madow, et nul par rééchantillonnage sous $H_0$ (pool des deux échantillons).
CORRECTIF_PYTHON_EXACT:
```python
import math, random
from collections import Counter

def _H2_mm(counts, n):                 # entropie base 2 avec correction de Miller-Madow
    K = sum(1 for c in counts.values() if c > 0)
    H = -sum((c/n)*math.log2(c/n) for c in counts.values() if c > 0)
    return H + (K-1)/(2*n*math.log(2))

def jsd2(sample_P, sample_Q):
    cP, cQ = Counter(sample_P), Counter(sample_Q); nP, nQ = len(sample_P), len(sample_Q)
    cM = cP + cQ
    # D_JS = H(M) - (H(P)+H(Q))/2, avec M le mélange à poids 1/2 (pondéré par effectifs égaux)
    HM = _H2_mm(cM, nP+nQ); HP = _H2_mm(cP, nP); HQ = _H2_mm(cQ, nQ)
    d = HM - 0.5*(HP+HQ)
    return min(1.0, max(0.0, d))

def jsd_sol_astra(sample_Sol, sample_Astra, B=999, alpha=0.01, seed=5):
    rng = random.Random(seed); d_obs = jsd2(sample_Sol, sample_Astra)
    pool = list(sample_Sol) + list(sample_Astra); n1 = len(sample_Sol); null = []
    for _ in range(B):
        rng.shuffle(pool); null.append(jsd2(pool[:n1], pool[n1:]))
    p = (1 + sum(1 for v in null if v >= d_obs))/(B+1)
    return {"JSD_bits": d_obs, "JSD_metric": math.sqrt(d_obs), "p": p, "couplage": p <= alpha}
```

---

BUG_L_STAR_V2: [Sillon-3-Volet-IV] Érosion H9 d=1..6 testée en échelle linéaire sans test de tendance ordonnée, et dérive de $S_{\text{TD}}$ surveillée par un CUSUM calibré sous iid alors que la série est autocorrélée
PREUVE_NON_CONFORMITE: Si chaque étape érode une fraction $\varepsilon$, l'observable suit $O_d = O_0(1-\varepsilon)^d$ : la relation est **log-linéaire** en $d$ ; une régression linéaire sur $O_d$ sous-estime la pente aux grands $d$ et biaise le couplage avec $S_{\text{TD}}$. Le bon test d'une érosion monotone sur $K=6$ niveaux ordonnés et $n$ sujets appariés est le $L$ de Page `(référence à vérifier)`, pas une comparaison de moyennes. Pour la dérive temporelle, un CUSUM de Page avec seuil $h$ pris sous hypothèse iid a un ARL$_0$ effondré dès que $\rho_1>0$ (fausses alarmes), ce qui déclenche $H_A$ sans dérive réelle : $h$ doit être calibré par bootstrap par blocs sur la série de $S_{\text{TD}}$.
CORRECTIF_PYTHON_EXACT:
```python
import math, random

def _ranks(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0]*len(v); i = 0
    while i < len(o):
        j = i
        while j+1 < len(o) and v[o[j+1]] == v[o[i]]: j += 1
        for k in range(i, j+1): r[o[k]] = (i+j)/2 + 1
        i = j+1
    return r

def page_L(table, B=4999, seed=9):
    """table[i][d-1] = O_d pour le sujet i, d=1..6. Tendance décroissante attendue → on teste sur log(O)."""
    logs = [[math.log(max(x, 1e-300)) for x in row] for row in table]
    K = len(logs[0]); rng = random.Random(seed)
    def L(rows): 
        R = [sum(_ranks(r)[d] for r in rows) for d in range(K)]
        return sum((K-d)*R[d] for d in range(K))        # poids décroissants : érosion
    L_obs = L(logs); null = []
    for _ in range(B):
        null.append(L([random.Random(rng.random()).sample(r, K) for r in logs]))
    p = (1 + sum(1 for v in null if v >= L_obs))/(B+1)
    slope = sum(sum(r[d]*(d - (K-1)/2) for d in range(K)) for r in logs) / (len(logs)*sum((d-(K-1)/2)**2 for d in range(K)))
    return {"L": L_obs, "p": p, "epsilon_hat": 1 - math.exp(slope)}

def cusum_blockboot(series, k=0.5, B=2000, block=8, target_ARL0=370, seed=13):
    """Calibre h par bootstrap par blocs puis exécute un CUSUM bilatéral sur S_TD[:, t]."""
    rng = random.Random(seed); n = len(series); m = sum(series)/n
    sd = math.sqrt(sum((x-m)**2 for x in series)/(n-1)) or 1.0
    z = [(x-m)/sd for x in series]
    def run_length(zz, h):
        Sp = Sm = 0.0
        for t,x in enumerate(zz):
            Sp = max(0.0, Sp + x - k); Sm = max(0.0, Sm - x - k)
            if Sp > h or Sm > h: return t+1
        return len(zz)+1
    def boot():
        out = []
        while len(out) < n:
            s = rng.randrange(0, n-block+1); out += z[s:s+block]
        return out[:n]
    h, lo, hi = 4.0, 0.5, 20.0
    for _ in range(25):                            # bissection sur h pour ARL0 cible
        h = (lo+hi)/2
        arl = sum(run_length(boot(), h) for _ in range(B))/B
        if arl < target_ARL0: lo = h
        else: hi = h
    t_alarm = run_length(z, h)
    return {"h_calibre": h, "alarme_t": t_alarm if t_alarm <= n else None}
```

---

BUG_L_STAR_V2: [Sillon-3-Volet-V-CMH] Mantel-Haenszel H4' appliqué sans test d'homogénéité des rapports de cotes (Breslow-Day/Tarone) ni correction de continuité : le pooling masque un effet inversé entre strates (Simpson)
PREUVE_NON_CONFORMITE: CMH estime un OR commun. Si l'essaim Fable montre un OR$=3$ et l'essaim Argon un OR$=1/3$, le pooled peut tomber à $\approx1$ et H4' conclut « pas d'effet » alors que l'hétérogénéité est elle-même la faille à rapporter. L*v2 interdit l'agrégation qui crée une zone morte : Breslow-Day (corrigé par Tarone) doit précéder CMH ; si l'homogénéité est rejetée, verdict `H_A-hétérogène` par strate, et non pooling. Sans correction de continuité $\tfrac12$, la statistique CMH est anti-conservatrice pour de petites strates.
CORRECTIF_PYTHON_EXACT:
```python
import math

def _chi2_sf(x, df):                    # Q(df/2, x/2) via série de la gamma incomplète régularisée
    if x <= 0: return 1.0
    a, s, term, k = df/2.0, 0.0, 1.0/ (df/2.0), 0
    xx = x/2.0
    while True:
        s += term; k += 1; term *= xx/(a+k)
        if term < 1e-14*s or k > 10000: break
    P = s * math.exp(-xx + a*math.log(xx) - math.lgamma(a))
    return max(0.0, min(1.0, 1.0 - P))

def cmh_with_breslow_day(tables, alpha=0.01):
    """tables: liste de (a,b,c,d) par strate ; a = succès bras Adv, b = échecs Adv, c/d idem Coop."""
    num = den = 0.0; sum_a = sum_E = sum_V = 0.0
    for a,b,c,d in tables:
        n = a+b+c+d; n1, n2, m1, m2 = a+b, c+d, a+c, b+d
        if n < 2: continue
        num += a*d/n; den += b*c/n
        sum_a += a; sum_E += n1*m1/n; sum_V += n1*n2*m1*m2/(n*n*(n-1))
    if den == 0 or sum_V == 0: return {"verdict": "INVALIDE-instrument"}
    psi = num/den
    X_cmh = (abs(sum_a - sum_E) - 0.5)**2 / sum_V
    # Breslow-Day avec correction de Tarone
    bd = 0.0; sdev = 0.0; sV = 0.0
    for a,b,c,d in tables:
        n = a+b+c+d; n1, n2, m1 = a+b, c+d, a+c
        A = psi - 1.0; Bq = -(psi*(n1+m1) + (n2-m1)); C = psi*n1*m1
        if abs(A) < 1e-12: at = -C/Bq
        else:
            disc = math.sqrt(max(0.0, Bq*Bq - 4*A*C))
            roots = [(-Bq+disc)/(2*A), (-Bq-disc)/(2*A)]
            lo, hi = max(0.0, m1-n2), min(n1, m1)
            at = next((r for r in roots if lo-1e-9 <= r <= hi+1e-9), None)
            if at is None: return {"verdict": "INVALIDE-instrument"}
        cells = [at, n1-at, m1-at, n2-m1+at]
        if min(cells) <= 0: continue
        V = 1.0/sum(1.0/x for x in cells)
        bd += (a-at)**2 / V; sdev += (a-at); sV += V
    K = len(tables); bd_tarone = bd - (sdev**2)/sV if sV > 0 else bd
    p_hom = _chi2_sf(bd_tarone, K-1)
    if p_hom <= alpha:
        return {"verdict": "H_A-hétérogène", "psi_MH": psi, "p_BreslowDay": p_hom}
    p_cmh = _chi2_sf(X_cmh, 1)
    return {"verdict": "H_A" if p_cmh <= alpha else "H_B", "psi_MH": psi,
            "X2_CMH": X_cmh, "p_CMH": p_cmh, "p_BreslowDay": p_hom}
```

---

BUG_L_STAR_V2: [Sillon-3-Volet-V-TOST] Borne supérieure « Newcombe-Wilson » unilatérale à 95 % calculée avec $z_{0{,}975}$ ou par intervalle de Wald : largeur nulle à $\hat\tau\in\{0,1\}$ et sens du test M2 (Argon T4 §1) à nouveau perdu
PREUVE_NON_CONFORMITE: Argon T4 §1 exige $\text{UB}_{95\%}(\tau_{\text{Adv}}-\tau_{\text{Coop}}) \le \delta_\tau$. Un intervalle de Wald $\hat p \pm z\sqrt{\hat p(1-\hat p)/n}$ a une largeur **nulle** quand $\hat p = 0$ ou $1$ : avec $\tau_{\text{Adv}}=1$ sur 3 tours, la borne vaut exactement la différence observée et la non-contamination est « démontrée » par un artefact. Une UB unilatérale à 95 % utilise $z_{0{,}95}=1{,}6449$ ; prendre $1{,}96$ rend le test TOST plus conservateur que déclaré (puissance détruite → bascule $H_B$ systématique par insuffisance de puissance, zone morte inverse). Méthode 10 de Newcombe `(référence à vérifier)` : limites de Wilson par proportion, combinées en quadrature.
CORRECTIF_PYTHON_EXACT:
```python
import math

Z_ONE_SIDED_95 = 1.6448536269514722

def wilson(x, n, z):
    if n == 0: raise ValueError("n=0")
    p = x/n; z2 = z*z
    centre = (p + z2/(2*n))/(1 + z2/n)
    half = z*math.sqrt(p*(1-p)/n + z2/(4*n*n))/(1 + z2/n)
    return max(0.0, centre-half), min(1.0, centre+half)

def newcombe_ub(x_adv, n_adv, x_coop, n_coop, z=Z_ONE_SIDED_95):
    p1, p2 = x_adv/n_adv, x_coop/n_coop
    l1, u1 = wilson(x_adv, n_adv, z); l2, u2 = wilson(x_coop, n_coop, z)
    return (p1-p2) + math.sqrt((u1-p1)**2 + (p2-l2)**2)

def m2_non_contamination(regimes, delta_tau=0.05):
    """regimes: {'Inter': (x_adv,n_adv,x_coop,n_coop), 'Intra': (...)}. Verdict total."""
    try:
        ub = max(newcombe_ub(*regimes[X]) for X in ("Inter","Intra"))
    except (KeyError, ValueError):
        return {"verdict": "INVALIDE-instrument"}
    return {"UB_max": ub, "verdict": "non-contamine" if ub <= delta_tau else "H_B"}
```

---

BUG_L_STAR_V2: [Sillon-3-Volet-V-Kerckhoffs] Audit du Saboteur LoRA sans engagement (commit-reveal) sur les poids de l'adaptateur et détecteur réglé sur la même famille de sabotage que celle évaluée
PREUVE_NON_CONFORMITE: Kerckhoffs exige que la détection résiste quand la **conception** du saboteur est publique, mais pas que le détecteur ait été **ajusté** sur l'instance évaluée. Si la même famille de perturbations LoRA sert à régler le seuil du détecteur et à mesurer sa F1, la F1 est une fuite train/test (règle anti-fuite Opus §2.3.3). De plus, sans empreinte SHA-256 de $(A,B)$ engagée **avant** l'épreuve, le saboteur peut être échangé après coup. Il faut : (i) engagement haché des deltas, révélé après verdict ; (ii) F1 mesurée sur une famille de saboteurs **tenue à l'écart** du réglage, avec écart $\text{F1}_{\text{vu}}-\text{F1}_{\text{non vu}}$ contrôlé par TOST.
CORRECTIF_PYTHON_EXACT:
```python
import hashlib, struct, random

def commit_lora(A, B, nonce_hex):
    """A, B: listes plates de flottants (rang-r). Engagement hors ligne avant l'épreuve."""
    h = hashlib.sha256()
    h.update(bytes.fromhex(nonce_hex))
    for v in A: h.update(struct.pack("<d", float(v)))
    for v in B: h.update(struct.pack("<d", float(v)))
    return h.hexdigest()

def reveal_check(A, B, nonce_hex, commitment):
    return commit_lora(A, B, nonce_hex) == commitment

def kerckhoffs_audit(detector_fit, detector_score, families, delta_f1=0.05, seed=21):
    """families: dict nom -> (X, y). On règle sur toutes sauf une, on évalue sur la retenue (leave-one-family-out)."""
    rng = random.Random(seed); names = sorted(families); gaps = []
    for held in names:
        train = [(x, t) for n in names if n != held for x, t in zip(*families[n])]
        det = detector_fit([x for x,_ in train], [t for _,t in train])
        f1_seen = detector_score(det, *families[names[(names.index(held)+1) % len(names)]])
        f1_unseen = detector_score(det, *families[held])
        gaps.append(f1_seen - f1_unseen)
    worst = max(gaps)
    return {"gap_max": worst, "verdict": "KERCKHOFFS-OK" if worst <= delta_f1 else "H_B-fuite-saboteur"}
```

---

BUG_L_STAR_V2: [Sillon-3-Unification-5-Volets] Combinaison des cinq verdicts par somme/moyenne de p-valeurs (ou Fisher) alors que les volets partagent le tenseur $S_{\text{TD}}$ : dépendance non prise en compte, et arbre de décision non total sur les états `INVALIDE`/`NaN`
PREUVE_NON_CONFORMITE: Les cinq volets lisent le **même** $S_{\text{TD}}$ ; leurs p-valeurs sont donc dépendantes positivement. Fisher ($-2\sum\ln p_i \sim \chi^2_{10}$) suppose l'indépendance et devient anti-conservateur ; une moyenne de p-valeurs n'est pas une p-valeur. La procédure valide sous dépendance arbitraire est le min-p de Westfall-Young avec permutation **conjointe** du tenseur (une seule permutation appliquée aux cinq volets). Par ailleurs, un arbre $H_A/H_B$ qui ne définit pas l'issue pour chaque élément de $\{H_A,H_B,\text{INVALIDE}\}^5$ a $3^5-2^5=211$ états sans verdict : zone morte.
CORRECTIF_PYTHON_EXACT:
```python
import random, itertools

VOLETS = ("I","II","III","IV","V")

def westfall_young_minp(pvals_of, S_TD, B=999, seed=17):
    """pvals_of(tensor) -> dict volet->p. Permutation conjointe de l'axe temporel de S_TD pour les 5 volets."""
    rng = random.Random(seed)
    p_obs = pvals_of(S_TD); m_obs = min(p_obs.values()); cnt = 0
    T = len(S_TD[0])
    for _ in range(B):
        perm = list(range(T)); rng.shuffle(perm)
        S_perm = [[row[j] for j in perm] for row in S_TD]      # même permutation pour tous les volets
        if min(pvals_of(S_perm).values()) <= m_obs: cnt += 1
    return {"p_obs": p_obs, "p_minp_adj": (1+cnt)/(B+1)}

def decision_tree(verdicts, p_adj, alpha=0.01):
    """verdicts: dict volet -> 'H_A'|'H_B'|'INVALIDE-instrument'. Fonction totale sur les 3^5 états."""
    for v in VOLETS:
        if verdicts.get(v) not in ("H_A","H_B","INVALIDE-instrument"):
            return "INVALIDE-instrument"                      # NaN / clé absente / valeur hors domaine
    if any(verdicts[v] == "INVALIDE-instrument" for v in VOLETS):
        return "INVALIDE-instrument"                          # un instrument cassé invalide la fusée entière
    if p_adj <= alpha and any(verdicts[v] == "H_A" for v in VOLETS):
        return "H_A"
    return "H_B"

def _exhaustivity_check():
    for combo in itertools.product(("H_A","H_B","INVALIDE-instrument"), repeat=5):
        for p in (0.0, 0.5):
            assert decision_tree(dict(zip(VOLETS, combo)), p) in ("H_A","H_B","INVALIDE-instrument")
    return True
```

---

BUG_L_STAR_V2: [Sillon-3-M0-Tenseur-S_TD] Tenseur $S_{\text{TD}}$ sans schéma d'indexation ni invariants vérifiés : volets écrivant dans des colonnes de longueurs différentes, axes temporels non alignés, `0.0` par défaut confondu avec « non mesuré »
PREUVE_NON_CONFORMITE: Un « tenseur commun » n'est commun que si les cinq volets partagent le même axe $t$ (mêmes instants $t_1..t_T$) et si une cellule non mesurée est distinguable d'une mesure nulle. Avec `0.0` comme valeur par défaut, Volet IV (CUSUM) lit un plateau artificiel, Volet III lit une divergence nulle, et le min-p (ci-dessus) est calculé sur des artefacts. Il faut un schéma `[volet, t]` à longueur imposée, sentinelle `None` pour les cellules absentes, et une vérification d'invariants qui renvoie `INVALIDE-instrument` avant toute lecture.
CORRECTIF_PYTHON_EXACT:
```python
import math

VOLETS = ("I","II","III","IV","V")

class S_TD:
    def __init__(self, timestamps):
        if len(timestamps) != len(set(timestamps)) or timestamps != sorted(timestamps):
            raise ValueError("axe temporel non strictement croissant")
        self.t = list(timestamps)
        self.cells = {v: [None]*len(self.t) for v in VOLETS}
    def write(self, volet, t, value):
        if volet not in VOLETS: raise KeyError(volet)
        if t not in self.t: raise KeyError("instant hors axe commun")
        if not (isinstance(value, (int,float)) and not isinstance(value,bool) and math.isfinite(value)):
            raise ValueError("valeur non finie")
        self.cells[volet][self.t.index(t)] = float(value)
    def invariants(self):
        if any(None in self.cells[v] for v in VOLETS): return "INVALIDE-instrument"
        if any(len(self.cells[v]) != len(self.t) for v in VOLETS): return "INVALIDE-instrument"
        return "OK"
    def as_matrix(self):
        if self.invariants() != "OK": raise RuntimeError("S_TD incomplet")
        return [self.cells[v][:] for v in VOLETS]
```

FIN-INSPECTION-ESSAIM
