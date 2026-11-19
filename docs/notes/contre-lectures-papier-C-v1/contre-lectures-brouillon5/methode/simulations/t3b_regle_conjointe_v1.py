"""T3b : regle conjointe proposee pour C-P1 (correction du constat sur le calibrage) : « vers la cible » (resp. « vers
la moyenne ») exige la meme conclusion sur la loi nette calibree (texte) ET sur la loi nette sans calibrage (rho = 1).
Memes modeles que T3 (S : bruit sur v0 ; D : v0 exact et compression kappa de toute insertion) ; graine neuve."""
import sys
import numpy as np
from t3_compression_temoins_v1 import essai
rng = np.random.default_rng(np.random.SeedSequence(0xB5D3).spawn(1)[0])
print("modele kappa  T  lambda | texte : P(cible) P(moyenne) | conjointe : P(cible) P(moyenne)")
for modele, kappa in (("S", 0.0), ("D", 0.08), ("D", 0.16)):
    for T in (45, 60):
        for lam in (1.0, 0.5):
            L = [essai(rng, T, modele, kappa, 0.4, 0.10, lam, 1000) for _ in range(300)]
            f = lambda x: np.mean([o["cal"][x] for o in L])
            cj = lambda x: np.mean([o["cal"][x] and o["brut"][x] for o in L])
            print(f"  {modele}   {kappa:.2f}  {T:3d}  {lam:.1f}  |  {f('cible'):.3f}  {f('moy'):.3f}   |  {cj('cible'):.3f}  {cj('moy'):.3f}")
            sys.stdout.flush()
