"""Rejeu partiel du script de certificat de l'auteur : mêmes fonctions, mêmes graines, les 40 premiers problèmes."""
import json, math, sys
A = sys.argv[1]; sys.path.insert(0, A)
import numpy as np
import essai_confiance_banc_v1 as bc
import essai_confiance_certificat_v1 as ce
ref = json.load(open(A + '/sorties/certificat-v1.json'))
lignes = []
for r in range(40):
    rng = np.random.default_rng(np.random.SeedSequence(entropy=ce.RACINE, spawn_key=(r,)))
    Ls = [bc.softmax_par(rng) for _ in range(3)]
    def tirer(n, theta_monde):
        z, g = bc.tirer_plan(rng, n)
        Lz = np.stack([bc.probas_softmax(p, z) for p in Ls], axis=1)
        m = z[:, 0] > 0.3
        P = bc.probas_membre(Lz, m, *theta_monde)
        y = bc.tirer_issues(rng, P)
        return bc.lignes(Lz, y), y, m
    t1 = (0.1, rng.dirichlet(np.ones(3)), np.stack([rng.dirichlet(np.ones(3)) for _ in range(2)]))
    t2 = (0.1, rng.dirichlet(np.ones(3)), np.stack([rng.dirichlet(np.ones(3)) for _ in range(2)]))
    Ae, ye, me = tirer(40, t1)
    Ac, yc, mc = tirer(40, t2)
    Vc, _, _ = bc.em_certifie(Ac, yc, np.ones((1, 40)), mc[None, :], 2000)
    supc = float(Vc[0, 0])
    for rayon in (0.5, 2.0, 5.0, -1.0):
        kappa = supc - rayon
        B, U0, _, _ = bc.borne_sur_ensemble(Ae, ye, me[None, :], Ac, yc, mc[None, :], [kappa])
        b = float(B[0, 0])
        rf = ce.reference(Ae, ye, me, Ac, yc, mc, kappa, rng)
        lignes.append({"probleme": r, "rayon": rayon, "borne": b, "reference": rf})
dmax_b = dmax_r = 0.0; n = 0
for x, y in zip(lignes, ref['lignes']):
    assert x['probleme'] == y['probleme'] and x['rayon'] == y['rayon']
    n += 1
    for k in ('borne', 'reference'):
        if math.isfinite(x[k]) and math.isfinite(y[k]):
            d = abs(x[k] - y[k])
            if k == 'borne': dmax_b = max(dmax_b, d)
            else: dmax_r = max(dmax_r, d)
        else:
            assert x[k] == y[k], (x, y)
out = {"lignes_comparees": n, "ecart_max_borne": dmax_b, "ecart_max_reference": dmax_r}
json.dump(out, open(sys.argv[2], 'w')); print(out)
