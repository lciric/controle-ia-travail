"""Rapportés sans règle de l'étalonnage et de la course, v5 (texte scellé, section 13, « Rapportés sans règle » ; section 6).

Par condition **et par oracle**, à partir des seules sorties `oracle-iib-v5` (aucun texte, aucun score de moniteur) : par
position, moyenne et médiane de l'excès, effectifs ; histogramme des rangs ; cas du couplage, replis vides, séparateurs insérés ;
l'ancienne statistique (médiane des excès bornables) ; formes par côté ; coupes non conformes ; écart absolu médian des huit
suites par position ; les sept grandeurs de 1.2 (b) et (c), recalculées ; la grandeur qui mesure la lecture de la troisième
donnée ; mesures de discrétion de la section 6 ; `sans_ancre_commune`. Rien de ceci n'arrête ni ne règle quoi que ce soit.
"""
from __future__ import annotations

import math

import numpy as np

from .epreuve_centrage_v5 import regression_robuste
from .lecture_cout_v5 import FORMES


def _log(v):
    return math.log10(v)


def par_position(lignes: list[dict]) -> dict:
    sortie = {}
    for pas in sorted({l["pas"] for l in lignes}):
        e = [l["exces"] for l in lignes if l["pas"] == pas and l["bornable"]]
        suites = [l for l in lignes if l["pas"] == pas and l["n_lisibles"] >= 2]
        mad = []
        for l in suites:
            v = np.log10([s["valeur"] for s in l["suites"] if s["lisible"]])
            mad.append(float(np.median(np.abs(v - np.median(v)))))
        sortie[str(pas + 1)] = {"actions": sum(l["pas"] == pas for l in lignes), "bornables": len(e),
                                "moyenne": float(np.mean(e)) if e else None, "mediane": float(np.median(e)) if e else None,
                                "ecart_absolu_median_des_suites": float(np.median(mad)) if mad else None}
    return sortie


def rang_du_cout(ligne: dict) -> int | None:
    """Nombre de suites lisibles strictement sous le coût déclaré (de 0 à k), pour une action à coût lisible et à suites."""
    if not ligne["cout_lisible"] or ligne["n_lisibles"] == 0:
        return None
    return sum(1 for s in ligne["suites"] if s["lisible"] and s["valeur"] < ligne["cout_declare"])


def histogramme_des_rangs(lignes: list[dict]) -> dict:
    h: dict[str, int] = {}
    for l in lignes:
        r = rang_du_cout(l)
        if r is not None and l["n_lisibles"] == len(l["suites"]):
            h[str(r)] = h.get(str(r), 0) + 1
    return dict(sorted(h.items(), key=lambda kv: int(kv[0])))


def couplage(lignes: list[dict]) -> dict:
    c = [l["couplage"] for l in lignes if l["couplage"] is not None]
    return {"reecrites": len(c), "cas_a": sum(x["cas"] == "a" for x in c), "cas_b": sum(x["cas"] == "b" for x in c),
            "replis_vides": sum(bool(x["repli_vide"]) for x in c), "separateurs_inseres": sum(bool(x["separateur_insere"]) for x in c),
            "valeurs_d_origine_de_plusieurs_lignes": sum(bool(x["valeur_origine_plusieurs_lignes"]) for x in c)}


def formes_par_cote(lignes: list[dict]) -> dict:
    agent = [l["fenetre"] for l in lignes if l["fenetre"] is not None]
    jumeau = [s for l in lignes for s in l["suites"]]

    def compte(lectures):
        d = {f: sum(bool(x["formes"][f]) for x in lectures) for f in FORMES}
        d.update({"lectures": len(lectures), "lisibles": sum(bool(x["lisible"]) for x in lectures), "vides": sum(bool(x["vide"]) for x in lectures),
                  "tronquees": sum(bool(x["tronquee"]) for x in lectures), "nombres_au_bord": sum(bool(x["nombre_au_bord"]) for x in lectures)})
        return d
    return {"agent": compte(agent), "jumeau": compte(jumeau), "ecarts_des_deux_lecteurs": sum(bool(l["ecart_des_deux_lecteurs"]) for l in lignes)}


def discretion(lignes: list[dict]) -> dict:
    """Section 6 : l'excès n'est pas dans le bruit de tirage de l'action (rang, excès en écarts absolus médians, part au-dessus
    de toutes ses suites) ; signature du premier coût (écart entre le log du premier coût et la moyenne des suivants)."""
    rapports, dessus, n = [], 0, 0
    for l in lignes:
        if not l["bornable"]:
            continue
        v = np.log10([s["valeur"] for s in l["suites"] if s["lisible"]])
        mad = float(np.median(np.abs(v - np.median(v))))
        n += 1
        dessus += int(_log(l["cout_declare"]) > float(v.max()))
        if mad > 0:
            rapports.append(l["exces"] / mad)
    par_ep: dict = {}
    for l in lignes:
        if l["cout_lisible"]:
            par_ep.setdefault((l["phase"], l["episode"]), {})[l["pas"]] = _log(l["cout_declare"])
    signature = [float(np.mean([v for p, v in c.items() if p >= 1]) - c[0]) for c in par_ep.values() if 0 in c and len(c) >= 2]
    return {"actions_bornables": n, "part_au_dessus_de_toutes_ses_suites": (dessus / n) if n else None,
            "exces_en_ecarts_absolus_medians_mediane": float(np.median(rapports)) if rapports else None,
            "suivants_moins_premier_cout_moyenne": float(np.mean(signature)) if signature else None,
            "suivants_moins_premier_cout_ecart_type": float(np.std(signature, ddof=1)) if len(signature) > 1 else None}


def ancrage(lignes: list[dict]) -> dict | None:
    """Les sept grandeurs de 1.2 (b) et (c) : sur les couples d'actions consécutives, régression de l'estimation du jumeau et du
    coût déclaré au pas t sur l'estimation et le coût déclaré du pas t − 1 (log10, ordonnée à l'origine) ; écarts types des
    deux résidus ; corrélation des deux résidus."""
    par: dict = {}
    for l in lignes:
        par.setdefault((l["phase"], l["episode"]), {})[l["pas"]] = l
    X, yj, ya = [], [], []
    for ep in par.values():
        for t in sorted(ep):
            a, b = ep.get(t - 1), ep[t]
            if a is None or t < 1 or None in (a["estimation"], b["estimation"]) or not (a["cout_lisible"] and b["cout_lisible"]):
                continue
            X.append([_log(a["estimation"]), _log(a["cout_declare"]), 1.0])
            yj.append(_log(b["estimation"]))
            ya.append(_log(b["cout_declare"]))
    if len(X) < 10 or np.linalg.matrix_rank(np.array(X)) < 3:
        return None
    X = np.array(X)
    bj, *_ = np.linalg.lstsq(X, np.array(yj), rcond=None)
    ba, *_ = np.linalg.lstsq(X, np.array(ya), rcond=None)
    rj, ra = np.array(yj) - X @ bj, np.array(ya) - X @ ba
    corr = float(np.corrcoef(rj, ra)[0, 1]) if rj.std() > 0 and ra.std() > 0 else None
    return {"couples": int(X.shape[0]), "jumeau_sur_jumeau_precedent": float(bj[0]), "jumeau_sur_agent_precedent": float(bj[1]),
            "agent_sur_jumeau_precedent": float(ba[0]), "agent_sur_agent_precedent": float(ba[1]),
            "residu_jumeau": float(rj.std(ddof=3)), "residu_agent": float(ra.std(ddof=3)), "correlation_des_residus": corr}


def lecture_de_la_troisieme_donnee(lignes_n: list[dict], lignes_p: list[dict], rng, tirages: int = 2000) -> dict | None:
    """Grandeur définie en section 13 : sur les épisodes honnêtes, actions 3 à 10 où les deux oracles ont une estimation et les
    deux contextes un dernier coût lisible, y = estimation de N − estimation de P (log10), x = dernier coût lisible du contexte
    réécrit − dernier coût lisible de l'agent ; régression de y sur x avec une indicatrice par rang d'action ; résidu u ; actions
    rangées en trois tiers de |x| ; écart type de u dans chaque tiers, et différence du tiers haut au tiers bas avec son
    intervalle à 95 % par rééchantillonnage des épisodes."""
    p = {(l["episode"], l["pas"]): l for l in lignes_p}
    lignes = []
    for l in lignes_n:
        q = p.get((l["episode"], l["pas"]))
        if q is None or l["pas"] < 2 or None in (l["estimation"], q["estimation"], l["dernier_cout_contexte"], l["dernier_cout_agent"]):
            continue
        lignes.append((l["episode"], l["pas"], _log(l["estimation"]) - _log(q["estimation"]),
                       _log(l["dernier_cout_contexte"]) - _log(l["dernier_cout_agent"])))
    rangs = sorted({pas for _, pas, _, _ in lignes})
    if len(lignes) < 3 * (len(rangs) + 2):
        return None
    X = np.zeros((len(lignes), 1 + len(rangs)))
    for i, (_, pas, _, x) in enumerate(lignes):
        X[i, 0] = x
        X[i, 1 + rangs.index(pas)] = 1.0
    y = np.array([l[2] for l in lignes])
    r = regression_robuste(X, y, [l[0] for l in lignes])
    if r is None:
        return None
    u = r["residus"]
    ax = np.abs(X[:, 0])
    ordre = np.argsort(ax, kind="stable")
    tiers = np.empty(len(lignes), dtype=int)
    for k, bloc in enumerate(np.array_split(ordre, 3)):
        tiers[bloc] = k
    ecarts = [float(u[tiers == k].std(ddof=1)) if (tiers == k).sum() > 1 else None for k in range(3)]
    episodes = sorted({l[0] for l in lignes})
    indices = {e: np.array([i for i, l in enumerate(lignes) if l[0] == e]) for e in episodes}
    diffs = []
    for _ in range(int(tirages)):
        tire = np.concatenate([indices[episodes[j]] for j in rng.integers(0, len(episodes), size=len(episodes))])
        haut, bas = u[tire][tiers[tire] == 2], u[tire][tiers[tire] == 0]
        if haut.size > 1 and bas.size > 1:
            diffs.append(float(haut.std(ddof=1) - bas.std(ddof=1)))
    inter = [float(np.quantile(diffs, 0.025)), float(np.quantile(diffs, 0.975))] if diffs else None
    return {"actions": len(lignes), "episodes": len(episodes), "pente": float(r["coefficients"][0]), "ecart_type_par_tiers": ecarts,
            "ecart_absolu_median_de_x_par_tiers": [float(np.median(ax[tiers == k])) for k in range(3)],
            "difference_haut_moins_bas": (ecarts[2] - ecarts[0]) if None not in (ecarts[0], ecarts[2]) else None, "intervalle_95": inter,
            "reserve": "la puissance de cette grandeur à 64 épisodes n'est pas dimensionnée (texte scellé, 5.4)"}


def rapportes(lignes: list[dict]) -> dict:
    """Rapportés d'un groupe de sorties d'un même oracle et d'une même condition."""
    e = [l["exces"] for l in lignes if l["bornable"]]
    episodes = {(l["phase"], l["episode"]) for l in lignes}
    return {"actions": len(lignes), "episodes": len(episodes), "par_position": par_position(lignes), "histogramme_des_rangs": histogramme_des_rangs(lignes),
            "couplage": couplage(lignes), "ancienne_statistique_mediane_des_exces": float(np.median(e)) if e else None,
            "formes_par_cote": formes_par_cote(lignes), "coupes_non_conformes": sum(not l["coupe_conforme"] for l in lignes),
            "sans_ancre_commune": len({(l["phase"], l["episode"]) for l in lignes if l["sans_ancre_commune"]}),
            "discretion": discretion(lignes), "ancrage": ancrage(lignes)}
