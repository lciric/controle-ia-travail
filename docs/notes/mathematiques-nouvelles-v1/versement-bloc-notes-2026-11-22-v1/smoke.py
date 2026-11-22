import time, numpy as np
from controle_ia.oracles_plantes_v1.famille_f1 import MondeF1
from controle_ia.oracles_plantes_v1.famille_f2 import MondeF2
from controle_ia.oracles_plantes_v1.famille_f3 import MondeF3
from controle_ia.oracles_plantes_v1.tests_de_mort import *
from controle_ia.oracles_plantes_v1.normalisation import normaliser
from controle_ia.oracles_plantes_v1.evaluation import instance_texte
cap = {"taille_entier_bits": 8192, "exposant_max": 512, "intervalle_max": 512, "factorielle_max": 300,
       "instances_max": 200000, "pas_max_f1": 60, "tours_max_f2": 300, "indice_max_facteur_f3": 10}
cfgs = {
 MondeF1: {"taille_espace": [4, 8], "denominateurs": [12, 20, 24], "borne_N": 4},
 MondeF2: {"moniteurs": [2, 3], "denominateur": 20, "alpha_num": [1, 6], "beta_num": [10, 19], "borne_N": 10},
 MondeF3: {"PU": [1, 3], "QU": [1, 3], "U0": [1, 4], "U1": [1, 6], "AV_choix": ["3/2", "2", "5/3", "5/2"], "BV": [0, 5], "V0": [1, 5], "borne_N": 15,
           "module_residu": [200, 2000], "essais_residu": 8, "premier_apparition_max": 3000},
}
for cls, cfg in cfgs.items():
    rng = np.random.default_rng(1)
    m = cls.tirer(rng, cfg, cap)
    print(cls.famille, m.p if cls.famille!='F2' else (m.alpha, m.beta))
    for nomg, gen in [("V", m.gabarits_verites), ("FT", m.gabarits_faux_tot), ("PG", m.gabarits_pieges), ("TT", m.temoins_triviaux), ("TG", m.temoins_grossiers)]:
        for nom, cands in gen(rng):
            for c in cands:
                if c is None: print("  ", nomg, nom, "None"); continue
                t0=time.time()
                r = appliquer_batterie(sortie_de_texte(c), m)
                t2 = t2_contre_exemple(r.arbre, m, 3*m.N) if r.arbre else None
                print("  ", nomg, nom, r.statut, "vb" if r.vraie_bornee else "", "triv" if r.triviale else "", [ (i.test, i.type.value, i.instance and instance_texte(i.instance)) for i in r.issues[1:3]], "3N:", t2 and t2.type.value, t2 and t2.instance and instance_texte(t2.instance), f"{time.time()-t0:.2f}s")
                break
