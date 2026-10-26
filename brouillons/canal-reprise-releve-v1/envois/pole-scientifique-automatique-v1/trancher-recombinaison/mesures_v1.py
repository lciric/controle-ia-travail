"""Mesures communes (v1) : opérateur-pont choisi après tirage, classes de pièges, mesures par monde,
moyennes et intervalles à 95 % par rééchantillonnage apparié sur les mondes (bibliothèque standard)."""
from collections import Counter


def frequences_etiquettes(monde):
    df = Counter()
    for a in monde["arts"]:
        df.update(a["etiquettes"].keys())
    return df


def etiquette_pont(monde, x, df):
    """Opérateur choisi après tirage, identique pour toutes les méthodes : l'étiquette partagée la plus rare
    (départage par nom). None si la paire ne partage aucune étiquette (monde sans étiquettes)."""
    partage = monde["paires"][x]["partage"]
    return min(partage, key=lambda m: (df[m], m)) if partage else None


def classe_pont(monde, x, m):
    """Nature de l'opérateur-pont : vrai_op (opérateur latent commun, pont ou non selon la relation),
    moyeu, homonyme, parasite, autre, sans_etiquette."""
    p = monde["paires"][x]
    ai, aj = monde["arts"][p["i"]], monde["arts"][p["j"]]
    if m is None:
        return "sans_etiquette"
    if m.startswith("h"):
        return "moyeu"
    if m in ai["ops"] and m in aj["ops"]:
        return "vrai_op"
    provs = {ai["etiquettes"].get(m), aj["etiquettes"].get(m)}
    if "homonyme" in provs:
        return "homonyme"
    if "parasite" in provs:
        return "parasite"
    return "autre"


def mesurer(monde, sortie, df):
    """Mesures d'une méthode sur un monde ; sortie = liste d'indices de paires acceptées (budget k x G)."""
    n_out = len(sortie)
    if n_out == 0:
        return None
    paires, arts, vrais = monde["paires"], monde["arts"], monde["vrais"]
    tp = [x for x in sortie if x in vrais]
    classes = Counter(classe_pont(monde, x, etiquette_pont(monde, x, df)) for x in sortie)
    strates = {frozenset((arts[paires[x]["i"]]["dom_obs"], arts[paires[x]["j"]]["dom_obs"])) for x in sortie}
    par_meca = Counter(paires[x]["mecanisme"] for x in vrais)
    trouves_meca = Counter(paires[x]["mecanisme"] for x in tp)
    return {
        "n_sortie": n_out,
        "precision": len(tp) / n_out,
        "rappel": len(tp) / len(vrais) if vrais else None,
        "rappel_greffe": trouves_meca["greffe"] / par_meca["greffe"] if par_meca["greffe"] else None,
        "rappel_jumeau": trouves_meca["jumeau"] / par_meca["jumeau"] if par_meca["jumeau"] else None,
        "precision_placebo": sum(1 for x in sortie if x in monde["placebo"]) / n_out,
        "part_eloignes": sum(1 for x in sortie if paires[x]["eloigne"]) / n_out,
        "part_proches": sum(1 for x in sortie if paires[x]["proche"]) / n_out,
        "strates_distinctes": len(strates) / n_out,
        "piege_homonyme": classes["homonyme"] / n_out,
        "piege_moyeu": classes["moyeu"] / n_out,
        "piege_parasite": classes["parasite"] / n_out,
        "piege_incompatible": sum(1 for x in sortie if not paires[x]["compat_vraie"]) / n_out,
    }


def moyenne_ic(valeurs, rng, b=2000):
    """Moyenne sur les mondes et intervalle percentile à 95 % (rééchantillonnage des mondes, b tirages)."""
    v = [x for x in valeurs if x is not None]
    n = len(v)
    if n == 0:
        return None
    stats = sorted(sum(rng.choices(v, k=n)) / n for _ in range(b))
    return {"moyenne": sum(v) / n, "ic95": [stats[int(0.025 * b)], stats[int(0.975 * b) - 1]], "n_mondes": n}


def difference_ic(va, vb, rng, b=2000):
    """Écart apparié A - B : mêmes mondes, mondes où les deux sont définis."""
    d = [x - y for x, y in zip(va, vb) if x is not None and y is not None]
    return moyenne_ic(d, rng, b)
