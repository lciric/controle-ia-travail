import numpy as np, time
rng = np.random.default_rng(0)
N, K = 1200, 201
X = rng.normal(size=(N, K)); Xt = np.ascontiguousarray(X.T)
I = rng.integers(0, N, N)
def t(f, n=50):
    s = time.perf_counter()
    for _ in range(n): f()
    return (time.perf_counter() - s) / n * 1e3
print("gather (n,K)", t(lambda: X[I]))
print("gather (K,n)", t(lambda: Xt[:, I]))
A = X[I]; B = Xt[:, I]
print("argsort axis0 stable", t(lambda: np.argsort(A, axis=0, kind="stable")))
print("argsort axis0 quick", t(lambda: np.argsort(A, axis=0)))
print("argsort axis1 quick (K,n)", t(lambda: np.argsort(B, axis=1)))
print("argsort axis1 stable (K,n)", t(lambda: np.argsort(B, axis=1, kind="stable")))
print("sort axis1 (K,n)", t(lambda: np.sort(B, axis=1)))
