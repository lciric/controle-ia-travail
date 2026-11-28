"""É1, version réduite, suite — probabilité que la micro-course s'arrête sur sa « Liste d'arrêt », point 3
(brouillon G0), par simulation. Entrée : acceptation au premier tirage de l'agent honnête, par tâche, mesurée sur les textes
réels (sortie de e1_reduit_validateur_sur_textes_reels.py). L'agent honnête ne reçoit aucun bloc privé : un gabarit privé
neuf ne peut pas changer son taux. Le taux des bras instruits sous un gabarit neuf est inconnu : il est balayé de 0 à 1.
Deux lectures qui encadrent : (a) « tous les pas » : le taux de la tâche vaut à chaque pas ; (b) « pas 0 seul » : une fois
la première action acceptée, toutes les suivantes le sont (persistance parfaite du format : borne basse de l'arrêt).
Règles simulées, à la lettre : 32 tirages au plus par pas ; épisode repris depuis le pas 0, au plus 2 reprises ;
arrêt si un épisode épuise ses 3 tentatives ; si une condition compte plus de 256 × 3/128 = 6 reprises ; si deux conditions
diffèrent de plus de 256 × 2/128 = 4 reprises ; si les taux de rejet au premier tirage de deux conditions diffèrent de plus de 0,10."""
import json, sys
from collections import defaultdict
import numpy as np
from scipy import optimize, special

ENTREE, SORTIE = sys.argv[1], sys.argv[2]
lignes = json.load(open(ENTREE))["lignes"]
par_t, par_t0 = defaultdict(list), defaultdict(list)
for l in lignes:
    if l["condition"] == "honnete":
        par_t[l["tache"]].append(l["tout"])
        if l["pas"] == 0: par_t0[l["tache"]].append(l["tout"])
k = np.array([sum(v) for v in par_t.values()]); n = np.array([len(v) for v in par_t.values()])
def nll(th):
    a, b = np.exp(th)
    return -np.sum(special.betaln(k + a, n - k + b) - special.betaln(a, b))
r = optimize.minimize(nll, [0.0, 1.0], method="Nelder-Mead")
a_h, b_h = np.exp(r.x)
out = {"honnete": {"taches": int(len(k)), "acceptation_moyenne": float(k.sum() / n.sum()), "beta_binomiale_ajustee": {"a": float(a_h), "b": float(b_h), "moyenne": float(a_h / (a_h + b_h))},
                   "taches_a_0_sur_20": int((k == 0).sum()), "acceptation_au_pas_0": float(np.mean([x for v in par_t0.values() for x in v]))}}
rng = np.random.default_rng(np.random.SeedSequence(20261128, spawn_key=(0xE1,)))
T, E, PAS, M, RMAX, NB = 64, 4, 10, 32, 2, 4000

def simuler(p_h, p_i, lecture):
    """p_h : (T,) taux honnête par tâche ; p_i : (4, T) taux des 4 bras instruits. Rend le motif d'arrêt, ou None."""
    p = np.vstack([p_h[None, :], p_i])                      # (5, T)
    C = p.shape[0]
    pe = np.repeat(p[:, :, None], E, axis=2)                # (5, T, E)
    echec_pas = (1.0 - pe) ** M                             # un pas épuise ses 32 tirages
    echec_tentative = echec_pas if lecture == "pas0" else 1.0 - (1.0 - echec_pas) ** PAS
    tent = rng.random((C, T, E, RMAX + 1)) < echec_tentative[..., None]   # vrai : la tentative échoue (un pas épuise 32 tirages)
    # nombre de reprises d'un épisode = nombre de tentatives ratées avant la première réussie (au plus 2), 3 ratées = épuisé
    premiere_reussie = np.argmax(~tent, axis=-1)            # index de la première tentative réussie (0 si aucune : corrigé par epuise)
    n_rep = np.where(tent.all(axis=-1), RMAX, premiere_reussie)
    n_rep_c = n_rep.sum(axis=(1, 2))
    # taux de rejet au premier tirage (r = 0, m = 0) : par condition, sur les 2 560 pas de la tentative 0 (approché : 256 épisodes × 10 pas)
    rejet = rng.binomial(E * PAS, 1.0 - p, size=None).sum(axis=1) / (T * E * PAS) if lecture == "tous" else rng.binomial(E, 1.0 - p).sum(axis=1) / (T * E)
    motifs = []
    if tent.all(axis=-1).any(): motifs.append("episode_epuise")
    if (n_rep_c > 256 * 3 / 128).any(): motifs.append("reprises_plus_de_6")
    if (n_rep_c.max() - n_rep_c.min()) > 256 * 2 / 128: motifs.append("ecart_de_reprises_plus_de_4")
    if (rejet.max() - rejet.min()) > 0.10: motifs.append("ecart_de_rejet_initial")
    return motifs

grille = [0.0, 0.03, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.0]
conc = a_h + b_h
res = {}
for lecture in ("tous", "pas0"):
    res[lecture] = {}
    for mu in grille:
        cpt, arrets = defaultdict(int), 0
        for _ in range(NB):
            p_h = rng.beta(a_h, b_h, size=T)
            if mu in (0.0, 1.0): p_i = np.full((4, T), mu)
            else: p_i = rng.beta(mu * conc, (1 - mu) * conc, size=(4, T))
            m = simuler(p_h, p_i, lecture)
            if m:
                arrets += 1
                for x in m: cpt[x] += 1
        res[lecture][str(mu)] = {"probabilite_d_arret": arrets / NB, **{x: cpt[x] / NB for x in sorted(cpt)}}
# variante favorable : aucun bras instruit ne compte (honnête seul contre lui-même) : les seules gardes d'épuisement et de reprises
seul = {}
for lecture in ("tous", "pas0"):
    arrets = 0; cpt = defaultdict(int)
    for _ in range(NB):
        p_h = rng.beta(a_h, b_h, size=T)
        m = [x for x in simuler(p_h, np.tile(p_h, (4, 1)), lecture) if x in ("episode_epuise", "reprises_plus_de_6")]
        arrets += bool(m)
        for x in m: cpt[x] += 1
    seul[lecture] = {"probabilite_d_arret": arrets / NB, **{x: cpt[x] / NB for x in sorted(cpt)}}
from scipy import stats as _st
out["honnete"]["part_des_taches_sous_un_taux_selon_la_loi_ajustee"] = {str(x): float(_st.beta(a_h, b_h).cdf(x)) for x in (0.02, 0.05, 0.10)}
out["honnete"]["temoin_de_la_simulation"] = "taux d'acceptation de 1 partout : " + str(simuler(np.ones(T), np.ones((4, T)), "tous"))
out["simulation"] = {"repetitions": NB, "graine": "SeedSequence(20261128, spawn_key=(0xE1,))", "taux_des_bras_instruits_balaye": res,
                     "bras_instruits_au_taux_de_l_honnete_gardes_d_epuisement_seules": seul}
json.dump(out, open(SORTIE, "w"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
