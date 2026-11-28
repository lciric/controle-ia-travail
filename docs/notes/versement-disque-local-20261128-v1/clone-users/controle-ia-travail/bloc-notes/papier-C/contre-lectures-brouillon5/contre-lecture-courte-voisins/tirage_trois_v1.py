"""Tirage de trois papiers parmi les 20 voisins restants (hors Kumaran 2507.03120, ChatInject 2509.22830, Chen 2507.21509).
Graine : numpy.random.SeedSequence(20261021) ; generateur numpy.random.default_rng(SeedSequence) ; choice sans remise
sur la liste triee des identifiants (sans numero de version ; Poonia et Jain : identifiant de l'anthologie ACL)."""
import sys, numpy as np
IDS = [
 "2607.00415", "2607.05545",                                   # note joswin-huqu
 "2602.21262", "2608.11247", "2602.15456", "2508.15815", "2510.01228", "2601.17577",  # note panin-sept (sans Kumaran)
 "2601.04790", "2505.13488", "2504.09946", "2509.21305", "2508.14918", "2508.02087", "2606.01637",
 "2025.findings-emnlp.1335",                                    # note second-rang (sans Chen)
 "2502.15851", "2406.12935", "2411.11407", "2510.19687",       # note cp02 (sans ChatInject)
]
assert len(IDS) == 20 and len(set(IDS)) == 20
liste = sorted(IDS)
ss = np.random.SeedSequence(20261021)
rng = np.random.default_rng(ss)
idx = rng.choice(len(liste), size=3, replace=False)
print("numpy", np.__version__)
print("entropie", ss.entropy)
for i, x in enumerate(liste):
    print(i, x)
print("indices tires", [int(i) for i in idx])
print("papiers tires", [liste[int(i)] for i in idx])
