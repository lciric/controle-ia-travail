"""Piste nommée par le réfutateur, non adoptée : « un instant de rejet par famille » — mesure exploratoire — v1.

Réfutation, mise au point exploratoire, aucune revendication. Le lemme A de l'auteur borne tout dénominateur unique qui
domine tous les membres à un instant donné. Il ne borne pas une règle qui rejette chaque famille du nul à son propre
instant. Règle mesurée ici :
    promotion si, pour chaque famille F du nul, il existe un instant lu s_F avec  log q(y_1..s_F) − V_F(s_F) ≥ log(1/α),
où V_F(s) est le maximum certifié de la famille F sur les s premiers tirages. Statistique : min_F max_s [log q − V_F(s)],
au lieu de max_s min_F [log q − V_F(s)] pour le juge (v9). Par l'inégalité du minimax elle vaut au moins celle du v9.
Validité (trois lignes) : si le monde est le membre θ* de la famille F*, la promotion exige un instant s avec
log q(y_1..s) − V_F*(s) ≥ log(1/α), donc Λ_s = q(y_1..s)/P_θ*(y_1..s) ≥ 1/α à un instant lu ; par Ville, la probabilité
en est au plus α. Le choix de s_F après les tirages est permis : Ville borne tous les instants à la fois.
Réserve dite : la règle est un test de niveau α pour la carte seule ; elle ne donne pas une valeur e (le maximum courant
d'une martingale n'en est pas une), donc elle ne se branche pas telle quelle sur la règle e-BH du juge.

Mesures : (1) sur les mondes de puissance de l'auteur (ses graines, son banc lu seul), maxima par famille encadrés à
10⁻⁴ nat par le solveur du réfutateur, sans élagage : promotions du v9, de la règle, appariées ; comparaison de mon v9
aux promotions scellées de l'auteur, monde par monde ; (2) taille : copies de l'auteur (cas « sommet » et « interieur »)
et mondes tranchants du réfutateur avec carte « loterie ».
Usage : python piste_instant_par_famille_v1.py puissance DOSE MONDES SORTIE.json [processus]
        python piste_instant_par_famille_v1.py taille MONDES SORTIE.json [processus]"""
import json, os, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np  # noqa: E402
import banc_universelle_v1 as b  # noqa: E402  (banc de l'auteur)
import attaque_universelle_v1 as a  # noqa: E402  (solveur du réfutateur)

DOSES = ("0.25", "0.40", "0.55")
CAS_TAILLE_AUTEUR = ("interieur", "sommet", "extreme", "bruite", "sous_population", "grille", "v8")


def statistiques(G, lq, T, pi0=None):
    """Rend (v9 certifié, règle certifiée, v9 borne haute, règle borne haute) : maxima sur les instants lus."""
    n = len(lq)
    Wq = np.zeros((len(T), n))
    for i, t in enumerate(T):
        Wq[i, :t] = 1.0
    lot = a.Lot(G, Wq, pi0=pi0, elaguer=False)
    att, cert = lot.converger(800)
    cum = Wq @ lq
    bas, haut = cum[:, None] - cert, cum[:, None] - att          # (instants, familles)
    return float(bas.min(1).max()), float(bas.max(0).min()), float(haut.min(1).max()), float(haut.max(0).min())


def monde_auteur(args):
    sorte, cas, i_cas, r, dense = args
    entropie = 20261115201 if sorte == "puissance" else 20261115101
    s_monde, _ = np.random.SeedSequence(entropy=entropie, spawn_key=(i_cas, r)).spawn(2)
    w = b.preparer(b.monde(cas, s_monde))
    G = a.composantes(w["Ak"], w["y"], b.masques(w["z"], w["g"], w["arch"], "v9"), b.K)
    out = {"huit": statistiques(G, w["lq"], b.INSTANTS)}
    if dense:
        out["vingt"] = statistiques(G, w["lq"], b.INSTANTS_DENSES)
    return out


def monde_tranchant(args):
    cas, r = args
    i_cas = a.CAS_TAILLE.index(cas)
    s_monde, s_issues, s_parts = np.random.SeedSequence(entropy=a.ENTROPIE_TAILLE, spawn_key=(i_cas, r)).spawn(3)
    parts = a.tirer_parts(np.random.default_rng(s_parts), 200)
    w = a.monde_tranchant(np.random.default_rng(s_monde), a.CAS_TRANCHANTS[cas], parts)
    y = a.tirer_issues(np.random.default_rng(s_issues), w["P"])
    if not any(bool(y[i] == 2) for i, _ in w["paris"]):
        return None                                      # pari perdu : la carte a une vraisemblance presque nulle
    Q = a.carte_loterie(w["P"], [(i, 2) for i, _ in w["paris"]])
    idx = np.arange(200)
    lq = np.log(np.maximum(Q[idx, y], a.PLANCHER))
    G = a.composantes(w["S"][idx, :, y], y, w["masques"], w["K"])
    ip, pim, sans_coupure = w["membre"]
    pi0 = np.full((G.shape[0], G.shape[2]), 1.0 / G.shape[2])
    for p in range(G.shape[0]):
        if p == ip or sans_coupure:
            pi0[p] = 0.98 * pim + 0.02 / G.shape[2]
    simple = float(np.max(np.cumsum(lq - np.log(w["P"][idx, y]))[np.array(w["instants"]) - 1]))
    return statistiques(G, lq, w["instants"], pi0) + (simple,)


def compter(valeurs, seuil=a.SEUIL):
    v = np.array(valeurs)
    return v >= seuil


def main():
    sorte = sys.argv[1]
    import multiprocessing as mp
    t0 = time.time()
    if sorte == "puissance":
        dose, R, sortie = sys.argv[2], int(sys.argv[3]), sys.argv[4]
        processus = int(sys.argv[5]) if len(sys.argv) > 5 else 2
        if os.path.exists(sortie):
            raise SystemExit("sortie existante, jamais écrasée")
        i_cas = DOSES.index(dose)
        dense = dose == "0.40"
        with mp.get_context("fork").Pool(processus) as pool:
            res = pool.map(monde_auteur, [("puissance", ("neuve", float(dose)), i_cas, r, dense) for r in range(R)], chunksize=4)
        ref = json.load(open(os.path.join(ICI, f"sortie-puissance-{dose}-a-v1.json")))
        doc = {"essai": "piste « un instant de rejet par famille », puissance, mondes de l'auteur", "dose": float(dose), "mondes": R,
               "graines": {"entropie": 20261115201, "spawn_key": f"({i_cas}, r), r = 0..{R - 1} (graines de l'auteur)"}}
        for cle, nom_ref in (("huit", "v9"), ("vingt", "v9_dense")):
            if cle not in res[0]:
                continue
            v9 = compter([x[cle][0] for x in res]); regle = compter([x[cle][1] for x in res])
            regle_haut = compter([x[cle][3] for x in res])
            auteur = np.array([c == "1" for c in ref["par_monde"][nom_ref]["promue"][:R]])
            doc[f"instants_{cle}"] = {
                "v9_refutateur": {"promotions": int(v9.sum()), "taux": round(float(v9.mean()), 5)},
                "regle": {"promotions": int(regle.sum()), "taux": round(float(regle.mean()), 5),
                          "intervalle_clopper_pearson_95": a.clopper_pearson(int(regle.sum()), R)},
                "regle_borne_haute": {"promotions": int(regle_haut.sum())},
                "apparie_regle_contre_v9": {"seule_la_regle": int((regle & ~v9).sum()), "seul_le_v9": int((~regle & v9).sum()),
                                            "ecart_de_taux": round(float(regle.mean() - v9.mean()), 5)},
                "v9_de_l_auteur_sur_les_memes_mondes": {"promotions": int(auteur.sum()),
                                                         "promue_chez_l_auteur_seul": int((auteur & ~v9).sum()),
                                                         "promue_chez_le_refutateur_seul": int((~auteur & v9).sum())}}
    else:
        R, sortie = int(sys.argv[2]), sys.argv[3]
        processus = int(sys.argv[4]) if len(sys.argv) > 4 else 2
        if os.path.exists(sortie):
            raise SystemExit("sortie existante, jamais écrasée")
        doc = {"essai": "piste « un instant de rejet par famille », taille", "copies_de_l_auteur": {}, "tranchant": {}}
        with mp.get_context("fork").Pool(processus) as pool:
            for cas in ("interieur", "sommet", "grille"):
                i_cas = CAS_TAILLE_AUTEUR.index(cas)
                res = pool.map(monde_auteur, [("taille", cas, i_cas, r, False) for r in range(150)], chunksize=4)
                regle = np.array([x["huit"][1] for x in res]); haut = np.array([x["huit"][3] for x in res])
                doc["copies_de_l_auteur"][cas] = {"mondes": 150, "graines": {"entropie": 20261115101, "spawn_key": f"({i_cas}, r)"},
                                                  "promotions_de_la_regle": int((regle >= a.SEUIL).sum()),
                                                  "plus_grande_statistique_certifiee": float(regle.max()),
                                                  "plus_grande_borne_haute": float(haut.max())}
            for cas in ("tranchant_v9", "tranchant_moitie"):
                res = [x for x in pool.map(monde_tranchant, [(cas, r) for r in range(R)], chunksize=50) if x is not None]
                v9 = compter([x[0] for x in res]); regle = compter([x[1] for x in res]); simple = compter([x[4] for x in res])
                doc["tranchant"][cas] = {
                    "mondes": R, "paris_gagnes": len(res),
                    "graines": {"entropie": a.ENTROPIE_TAILLE, "spawn_key": f"({a.CAS_TAILLE.index(cas)}, r), r = 0..{R - 1}"},
                    "v9": {"promotions": int(v9.sum()), "taux": round(int(v9.sum()) / R, 5)},
                    "regle": {"promotions": int(regle.sum()), "taux": round(int(regle.sum()) / R, 5),
                              "intervalle_clopper_pearson_95": a.clopper_pearson(int(regle.sum()), R)},
                    "rapport_de_vraisemblance_simple": {"promotions": int(simple.sum()), "taux": round(int(simple.sum()) / R, 5)},
                    "regle_promue_sans_que_le_rapport_simple_passe": int((regle & ~simple).sum())}
    doc["duree_s"] = round(time.time() - t0, 1)
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(json.dumps(doc, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    main()
