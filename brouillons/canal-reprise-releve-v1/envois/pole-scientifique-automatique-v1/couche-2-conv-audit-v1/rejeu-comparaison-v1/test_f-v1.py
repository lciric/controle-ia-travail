import sys, importlib.util
spec = importlib.util.spec_from_file_location("sim", sys.argv[1]); sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)
# garde effective (delta=0.10) contre garde neutralisée (delta=1.0 : delta - g >= 0.8, certifiée en quelques unités)
for disj in (False, True):
    for (n,kc) in ((48,20),(64,16)):
        for d in (0.10, 1.0):
            r = sim.calibrage_memes_taches(sim.rng_de(777,"Ftest",disj,n,kc,d), 400, n, kc, 10, 0.3, 0.0, delta=d, disjoint=disj)
            print(f"disjoint={disj} n={n} K_cal={kc} delta={d}: promotion a tort = {r:.3f}")
print("garde seule, n=48, K=10, delta=0.10:", sim.garde(sim.rng_de(777,"g48"), 1000, 48, 10, 0.10, groupe=True))
