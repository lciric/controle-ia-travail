"""Calculs v3 (correction V-1 de la vérification courte `0d64ed1d…`) : **une tranche de choix par groupe, commune à tous les
candidats** du représentant (même épisodes pour chaque candidat), tirée de la tâche du groupe (empreintes canoniques triées
de ses membres). Le reste est la v2, importée telle quelle (`../outils-v2/`, scellés).

Exécution **par parties d'un monde, un seul processus** (aucun pool) : chaque partie écrit sa sortie, scellée aussitôt par
l'opérateur ; `resume` agrège. Le déterminisme vient des parcours triés ; `python3 -I` ignore `PYTHONHASHSEED` (V-2) : la
graine de hachage est aléatoire à chaque lancement et la sortie le dit (`graine_de_hachage`).

Usage : `python3 -I -B puissance_monde_riche_v3.py representant|doublons|generations-a2 RANG SORTIE.json`
        `python3 -I -B puissance_monde_riche_v3.py resume COMMANDE DOSSIER SORTIE.json`
"""
import datetime, glob, hashlib, json, math, os, sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.join(os.path.dirname(ICI), "outils-v2")
V1 = os.path.join(os.path.dirname(ICI), "outils-v1")
for p in (V1, V2, ICI):
    if p not in sys.path:
        sys.path.insert(0, p)
import monde_riche_outils_v1 as M  # noqa: E402
import monde_riche_outils_v2 as M2  # noqa: E402
import puissance_monde_riche_v2 as P2  # noqa: E402

P1 = P2.P1
EPISODES_CHOIX = 400


def tranche_de_choix(monde, D, nsp, cle_groupe):
    """Une tranche de 400 épisodes frais, tirée de la tâche du groupe, hors tirages du juge et hors tranche du test de mort."""
    rng = P1.rng_de("choix-v3", cle_groupe)
    Z, G = M.tirer_instances(rng, EPISODES_CHOIX, D, nsp)
    Y = M.tirer_issues(rng, M.probas(monde, Z, G))
    return Z, G, Y


def statistique(loi, Z, G, Y):
    """Statistique gelée du test de mort (gain moyen de log-score sur la marginale empirique, comptes + 0,5)."""
    K = 3
    c = np.bincount(Y, minlength=K) + 0.5
    marg = c / c.sum()
    P = M.probas(loi, Z, G)
    return float(np.mean(np.log(np.maximum(P[np.arange(len(Y)), Y], M.PLANCHER)) - np.log(marg[Y])))


def representant_v3(groupe, lois, dg, can, monde, D, nsp):
    """Règle v2 (couverture dirigée ; égalité → tranche de choix ; puis empreinte) avec **une** tranche par groupe."""
    cle_groupe = "|".join(sorted(can[i] for i in groupe))
    cache = {}

    def choix(i):
        if "t" not in cache:
            cache["t"] = tranche_de_choix(monde, D, nsp, cle_groupe)
        return statistique(lois[i], *cache["t"])
    return M2.representant_v2(groupe, dg, can, statistique_de_choix=choix)


# --- parties --------------------------------------------------------------------------------------------------------------

def partie_representant(w):
    spec, cibles, loi, o, k1, eid_k1, infos = P2.preparer_monde_v2(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    ids = [e["id"] for e in spec["effets"]]
    fortes = sorted(i for i in ids if cibles[i][0] == "forte")
    moy = sorted(i for i in ids if cibles[i][0] == "moyenne")
    L = M.monde_restreint(spec, fortes + moy[:1])
    U = P2.UNIFORME
    var = {"loi": L,
           "diluee-0.5": {"type": "melange", "composantes": [L, U], "poids": [0.5, 0.5]},
           "diluee-0.2": {"type": "melange", "composantes": [L, U], "poids": [0.2, 0.8]},
           "diluee-0.05": {"type": "melange", "composantes": [L, U], "poids": [0.05, 0.95]},
           "temperee-0.3": {"type": "transformee", "base": L, "puissance": 0.3},
           "temperee-2.0": {"type": "transformee", "base": L, "puissance": 2.0}}
    noms = sorted(var)
    lois = [var[n] for n in noms]
    gains = [o.gain(l) for l in lois]
    Zref, Gref = M.tirer_instances(P1.rng_de("rep-ref", w), 2000, D, nsp)
    mats = M2.matrices(lois, Zref, Gref, nsp)
    out = {"monde": w, "gains": {n: round(g, 4) for n, g in zip(noms, gains)}, "cas": []}

    def un_cas(nom_cas, membres):
        sub = (mats[0][np.ix_(membres, membres)], mats[1][np.ix_(membres, membres)], [mats[2][i] for i in membres])
        gs, (dg, ds, can) = M2.grouper_v2([lois[i] for i in membres], Zref, Gref, nsp, mats=sub)
        for g in gs:
            if len(g) < 2:
                continue
            gm = [membres[i] for i in g]
            best = max(gains[i] for i in gm)
            r, info = representant_v3(g, [lois[i] for i in membres], dg, can, loi, D, nsp)
            r = membres[r]
            out["cas"].append({"monde": w, "cas": nom_cas, "membres": [noms[i] for i in gm], "meilleur_gain": round(best, 4),
                               "regle_v3": noms[r], "perte_v3": round(best - gains[r], 4), "departage": info["departage"],
                               "sous_g0_alors_que_le_meilleur_au_dessus": bool(gains[r] < 0.02 <= best)})

    un_cas("six-variantes", list(range(len(noms))))
    i_loi = noms.index("loi")
    for j in range(len(noms)):
        if j != i_loi:
            un_cas(f"paire-loi+{noms[j]}", [i_loi, j])
    return out


def partie_doublons(w):
    """Comme `puissance_monde_riche_v2._doublons_monde_v2`, représentants par la règle v3."""
    spec, cibles, loi, o, k1, eid_k1, infos = P2.preparer_monde_v2(w)
    D, nsp = spec["dimension"], spec["sous_populations"]
    rng = P1.rng_de("doublons-v2", w)
    Zref, Gref = M.tirer_instances(P1.rng_de("doublons-ref", w), 2000, D, nsp)
    ids = [e["id"] for e in spec["effets"]]
    fortes = sorted(i for i in ids if cibles[i][0] == "forte")
    moy = sorted(i for i in ids if cibles[i][0] == "moyenne")
    faibles = sorted(i for i in ids if cibles[i][0] == "faible")
    base_S = sorted(set(fortes) | {moy[0]})
    # mêmes tirages que la v2 pour les paires (rng consommé dans le même ordre), puis la génération de 24 cartes
    for s in (0.05, 0.1, 0.2, 0.3):
        P1._bruiter(spec, base_S, s, rng)
    idees = [base_S, sorted(set(fortes) | {moy[1]}), sorted({fortes[0]} | set(faibles[:2]))]
    cartes, verite = [], []
    for k, S in enumerate(idees):
        for v in range(6):
            cartes.append(P1._bruiter(spec, S, 0.15, rng))
            verite.append(f"idee-{k}")
    for v in range(6):
        S = sorted(set(rng.choice(ids, size=int(rng.integers(2, 5)), replace=False).tolist()))
        cartes.append(P1._bruiter(spec, S, 0.15, rng))
        verite.append("|".join(S))
    gs, (dg, ds, can) = M2.grouper_v2(cartes, Zref, Gref, nsp)
    seuil = math.log(P2.M_DESSIN / M.ALPHA)
    les = {i: M.log_e_arrete(M.juger(c, [k1], loi, D, nsp, P1.rng_de("doublons-juge", w, i), n=400)["traj"], seuil)
           for i, c in enumerate(cartes)}
    r_cartes = M.e_bh(les, P2.M_DESSIN)
    les_g = {gi: M.log_e_groupe([les[i] for i in g]) for gi, g in enumerate(gs)}
    r_groupes = M.e_bh(les_g, P2.M_DESSIN)
    reps = [gs[g][0] if len(gs[g]) == 1 else representant_v3(gs[g], cartes, dg, can, loi, D, nsp)[0] for g in r_groupes]
    return {"monde": w, "generation_24": {"groupes": len(gs), "groupes_purs": sum(1 for g in gs if len({verite[i] for i in g}) == 1),
                                          "retenues_par_carte": len(r_cartes), "idees_par_carte": len({verite[i] for i in r_cartes}),
                                          "groupes_retenus": len(r_groupes), "idees_par_groupe": len({verite[i] for i in reps})}}


def partie_generations_a2(w):
    """Condition « regroupement » de `_generations_course_v2`, représentants par la règle v3 (la condition « sans » ne change pas)."""
    original = M2.representant_v2
    spec_loi = {}

    def rep_v3(groupe, dg, can, statistique_de_choix=None):
        # même règle que v2, mais la tranche de choix est commune au groupe : on remplace la fonction de choix par une
        # statistique sur une tranche unique tirée de la tâche du groupe
        lois, monde, D, nsp = spec_loi["cartes"], spec_loi["monde"], spec_loi["D"], spec_loi["nsp"]
        return representant_v3(groupe, lois, dg, can, monde, D, nsp)

    # on rejoue `_generations_course_v2` en interceptant la création des cartes de chaque génération
    vrai_grouper = M2.grouper_v2

    def grouper_capture(cartes, Zref, Gref, nsp, **k):
        spec_loi["cartes"] = cartes
        return vrai_grouper(cartes, Zref, Gref, nsp, **k)

    spec, cibles, loi, o, k1, eid_k1, infos = P2.preparer_monde_v2(w)
    spec_loi.update(monde=loi, D=spec["dimension"], nsp=spec["sous_populations"])
    M2.representant_v2, M2.grouper_v2 = rep_v3, grouper_capture
    try:
        return P2._generations_course_v2((w, "A2", 3, 400, P2.M_DESSIN))
    finally:
        M2.representant_v2, M2.grouper_v2 = original, vrai_grouper


def resume(commande, dossier):
    parts = [json.load(open(p))["resultat"] for p in sorted(glob.glob(os.path.join(dossier, f"{commande}-v3-monde-*.json")))]
    if commande == "representant":
        cas = [c for m in parts for c in m["cas"]]
        pertes = [c["perte_v3"] for c in cas]
        return {"mondes": len(parts), "groupes_regroupes": len(cas), "perte_max": round(max(pertes), 4),
                "perte_mediane": round(float(np.median(pertes)), 4), "groupes_perte_sup_0.01": sum(p > 0.01 for p in pertes),
                "situations_perte_sup_0.01": sorted({f'monde {c["monde"]} : {c["regle_v3"]}' for c in cas if c["perte_v3"] > 0.01}),
                "sous_g0_a_tort": sum(c["sous_g0_alors_que_le_meilleur_au_dessus"] for c in cas),
                "departages": {k: sum(c["departage"] == k for c in cas) for k in ("couverture", "tranche de choix", "empreinte")},
                "detail_pertes": [c for c in cas if c["perte_v3"] > 0.01]}
    if commande == "doublons":
        return {"mondes": len(parts), **{k: round(float(np.mean([m["generation_24"][k] for m in parts])), 2) for k in parts[0]["generation_24"]}}
    out = {"mondes": len(parts)}
    for g in range(3):
        hs = [(m["generations"][g], m["composantes"]) for m in parts]
        out[str(g + 1)] = {"retenues_moyen": round(float(np.mean([h["retenues"] for h, _ in hs])), 2),
                           "archive_moyen": round(float(np.mean([h["archive"] for h, _ in hs])), 2),
                           "part_captee_moyenne": round(float(np.mean([len(h["captes"]) / c for h, c in hs])), 3),
                           "fausses_decouvertes_total": int(sum(h["fausses_decouvertes"] for h, _ in hs)),
                           "retenues_total": int(sum(h["retenues"] for h, _ in hs))}
    return out


if __name__ == "__main__":
    out = sys.argv[-1]
    if os.path.exists(out):
        sys.exit("refus : sortie existante")
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    cmd = sys.argv[1]
    if cmd == "resume":
        res = resume(sys.argv[2], sys.argv[3])
    else:
        res = {"representant": partie_representant, "doublons": partie_doublons,
               "generations-a2": partie_generations_a2}[cmd](int(sys.argv[2]))
    with open(out, "x", encoding="utf-8") as f:
        json.dump({"version": "puissance-monde-riche-v3", "commande": sys.argv[1:-1], "debut_utc": debut,
                   "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                   "graine_de_hachage": "aléatoire (python -I ignore PYTHONHASHSEED) ; déterminisme par parcours triés"
                   if sys.flags.isolated else os.environ.get("PYTHONHASHSEED", "aléatoire"),
                   "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "resultat": res}, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False)[:1500])
