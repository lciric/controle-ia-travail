"""Brique D — épreuve à vérité plantée, version 3 : consigne du développeur, brique D ; erratum 1, § 6 ; erratum 2,
§ 3, 4 et 6 ; texte scellé des diagnostics préalables (`prereg/diagnostics-prealables-sondes-v1.md`, e8dca00b…),
Seuil, « Épreuve à vérité plantée ». Remplace la v2 (jamais livrée). Les vérités et critères de passage engagés sont
dans `verites_mondes_plantes_v3.json`, scellé et committé avant toute exécution ; les fichiers v1 et v2 restent
archivés tels quels.

**Générateur** (`generer`). Unité : l'écart type d'un jeton le long d'une direction. Jetons de base communs à toutes les
séries qui lisent le même texte ; bruit de lecture indépendant par série (défaut 0,05). Séries : le modèle nu `N`, et,
pour chaque famille f, `n_paires` paires (`S<f>_<q>` saboteur, `J<f>_<q>` jumeau).
- décalage d'identité d'une paire (le même pour S et J) : composante le long de la direction de la trace, d'écart type
  `sigma_I`, plus une composante isotrope de norme attendue `identite_isotrope` (3) ;
- écart propre à la paire, réparti des deux côtés (erratum 2, § 4) : S reçoit +η/2 fois un vecteur unitaire tiré, J
  −η/2 ;
- trace commune `tau` le long de la direction de la trace, ajoutée à tous les saboteurs, une direction commune à toutes
  les familles [provisoire (E-6)] ;
- écart d'intensité : tous les adaptateurs décalés le long d'une direction commune de norme `intensite` × σ_I √2, les
  saboteurs de 1,2 fois cette norme [provisoire (E-3)] ;
- effet du texte, interaction (Q12), effet de tâche, décalage de chemin (E-4) : comme en v2.

**Deux modes de lecture.** `lire_monde` (« complet », une famille) : toutes les lignes. `lire_etalon` (« étalon »,
grille d'effectifs de l'erratum 2, § 6 : paires, familles, tâches, actions) : étalon de transport par famille,
testabilité et Holm sur les familles, contrôle d'intensité, et la sonde d'identité si un critère la demande ; textes
honnêtes seulement. Chaque lecture est une liste (une entrée par famille, ou une seule) : chaque entrée est un essai.
"""
from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path

import numpy as np
from scipy.stats import beta

from ..gardes import GardeArret
from ..scellement import verifier
from . import formes_closes_v1 as fc
from . import lecture_v1 as lc
from . import statistiques_v1 as st

CHEMIN_VERITES = Path(__file__).with_name("verites_mondes_plantes_v3.json")
CRITERES = ("contraste", "interaction", "interaction_brute", "interaction_sans_controle", "decalage_maitrise",
            "transport", "transport_controle", "identite", "texte", "nul_principal", "fuite")
CRITERES_ETALON = ("transport", "transport_controle", "identite")
NATURES = ("puissance", "fausse_lecture", "garde", "description")


@dataclass(frozen=True)
class Parametres:
    d: int = 256
    n_paires: int = 8
    n_familles: int = 1
    n_taches: int = 8
    actions_par_tache: int = 3
    jetons_min: int = 3
    jetons_max: int = 10
    jetons_porteurs: int = 1
    pente_spectre: float = 0.0
    bruit_lecture: float = 0.05
    sigma_I: float = 1.0
    identite_isotrope: float = 3.0
    eta: float = 1.0
    tau: float = 0.0
    intensite: float = 0.0
    texte: float = 0.0
    interaction: float = 0.0
    interaction_sur_trace: bool = False
    tache: float = 0.0
    ecart_chemin: float = 0.0
    permuter_etiquettes: bool = False
    fuite_de_pli: bool = False
    sources: tuple = ("honnete", "saboteur")

    def verifier(self):
        if self.d < 2 or self.n_paires < 2 or self.n_familles < 1 or self.n_taches < 2 or self.actions_par_tache < 1:
            raise GardeArret("monde : d ≥ 2, au moins deux paires, une famille, deux tâches, une action par tâche")
        if not 1 <= self.jetons_porteurs <= self.jetons_min <= self.jetons_max:
            raise GardeArret("monde : 1 ≤ jetons porteurs ≤ jetons_min ≤ jetons_max")
        for nom in ("sigma_I", "identite_isotrope", "eta", "tau", "intensite", "texte", "tache", "bruit_lecture",
                    "pente_spectre", "ecart_chemin"):
            if getattr(self, nom) < 0:
                raise GardeArret(f"monde : {nom} ≥ 0")
        if not set(self.sources) <= {"honnete", "saboteur"} or "honnete" not in self.sources:
            raise GardeArret("monde : sources parmi « honnete » et « saboteur », « honnete » comprise")


def _direction(rng, d):
    v = rng.standard_normal(d)
    return v / np.linalg.norm(v)


def generer(p: Parametres, rng: np.random.Generator) -> dict:
    """{"textes": {clé: (tâche, source)}, "lectures": {série: {clé: jetons}}, "roles": {série: rôle},
    "familles": {f: [(S, J), …]}, "paires": les paires de la famille 0}."""
    p.verifier()
    d = p.d
    ecart = np.arange(1, d + 1, dtype=np.float64) ** (-p.pente_spectre)
    ecart = np.sqrt(ecart * d / ecart.sum())
    t_dir, txt_dir, u_dir = _direction(rng, d), _direction(rng, d), _direction(rng, d)
    i_dir = t_dir if p.interaction_sur_trace else _direction(rng, d)
    dir_taches = {t: _direction(rng, d) for t in range(p.n_taches)}
    textes, base, porteurs = {}, {}, {}
    for t in range(p.n_taches):
        for src in p.sources:
            for a in range(p.actions_par_tache):
                cle = f"t{t}-{src}-a{a}"
                k = int(rng.integers(p.jetons_min, p.jetons_max + 1))
                x = rng.standard_normal((k, d)) * ecart + p.tache * dir_taches[t]
                m = np.zeros(k, dtype=bool)
                m[rng.choice(k, size=p.jetons_porteurs, replace=False)] = True
                if src == "saboteur":
                    x[m] += p.texte * txt_dir
                textes[cle], base[cle], porteurs[cle] = (f"t{t}", src), x, m
    m_int = p.intensite * p.sigma_I * math.sqrt(2.0)
    decalages, roles, familles = {"N": np.zeros(d)}, {"N": "nu"}, {}
    for f in range(p.n_familles):
        familles[f] = []
        for q in range(p.n_paires):
            o = p.sigma_I * rng.standard_normal() * t_dir + p.identite_isotrope * rng.standard_normal(d) / math.sqrt(d)
            g = _direction(rng, d)
            s_nom, j_nom = f"S{f}_{q}", f"J{f}_{q}"
            decalages[j_nom] = o - 0.5 * p.eta * g + m_int * u_dir
            decalages[s_nom] = o + 0.5 * p.eta * g + p.tau * t_dir + 1.2 * m_int * u_dir
            roles[j_nom], roles[s_nom] = "jumeau", "saboteur"
            familles[f].append((s_nom, j_nom))
    lectures = {}
    for nom in sorted(decalages):
        lect = {}
        for cle in sorted(textes):
            x = base[cle] + decalages[nom] + p.bruit_lecture * rng.standard_normal(base[cle].shape)
            if roles[nom] == "saboteur" and textes[cle][1] == "saboteur":
                if p.interaction_sur_trace:
                    x = x + p.interaction * i_dir
                else:
                    x[porteurs[cle]] += p.interaction * i_dir
            lect[cle] = x
        lectures[nom] = lect
    return {"textes": textes, "lectures": lectures, "roles": roles, "familles": familles, "paires": familles[0]}


def _unite(serie: str) -> str | None:
    return None if serie == "N" else "u" + serie[1:]


def _lignes(monde, series, unite=True, source=True):
    out = []
    for s in series:
        for cle, (t, src) in monde["textes"].items():
            out.append({"serie": s, "cle": cle, "tache": t, "unite": _unite(s) if unite else None,
                        "source": src if source else None, "sequence": monde["lectures"][s][cle], "pas": 0,
                        "valeur_declaree": None})
    return out


def jeu_principal(monde, rng=None, permuter=False) -> lc.Jeu:
    """Famille 0 : saboteurs (1) et jumeaux (0), toutes les sources ; unité = la paire."""
    series = [x for pq in monde["paires"] for x in pq]
    lignes = _lignes(monde, series)
    jeu = lc.construire_jeu(lignes, {f"{l['serie']}/{l['cle']}": int(monde["roles"][l["serie"]] == "saboteur")
                                     for l in lignes})
    if permuter:
        jeu = jeu.avec_etiquettes(lc.permuter_etiquettes(jeu, rng, lc.paires_du_jeu(jeu)))
    return jeu


def table_rejeu(monde, ligne, gels, jeu, ecart_chemin: float, relire_origines: bool = True) -> list[dict]:
    """Table de scores du rejeu croisé (voir v2) : la sonde gelée de chaque pli note les textes de ses tâches tenues à
    l'écart, lus sous le saboteur de l'unité et sous N. Cases d'origine décalées de `ecart_chemin` écarts types
    intra-case [E-4] ; relues sans décalage si `relire_origines`."""
    index = {jeu.ids[i]: i for i in range(len(jeu))}
    lignes = []
    for pli, ids in ligne["plis_ids"].items():
        sonde = gels[pli].sonde
        s_nom = "S" + jeu.unites[index[ids[0]]][1:]
        taches = sorted({jeu.taches[index[i]] for i in ids})
        cles = [c for c, (t, _) in sorted(monde["textes"].items()) if t in taches]
        brut = []
        for po, serie in (("adaptateur", s_nom), ("nu", "N")):
            sc = fc.scores_actions(sonde, [monde["lectures"][serie][c] for c in cles])
            brut += [(po, c, float(v)) for c, v in zip(cles, sc)]
        cases = {}
        for po, c, v in brut:
            cases.setdefault((po, monde["textes"][c][1]), []).append(v)
        sd = math.sqrt(sum(((np.array(v) - np.mean(v)) ** 2).sum() for v in cases.values()) /
                       sum(len(v) - 1 for v in cases.values()))
        for po, c, v in brut:
            t, so = monde["textes"][c]
            commun = {"dose": 1, "pli": pli, "source": so, "poids": po, "tache": t, "cle": c,
                      "longueur": len(monde["lectures"]["N"][c]), "pas": 0, "valeur_declaree": None,
                      "tache_tenue": True}
            if (po, so) in (("adaptateur", "saboteur"), ("nu", "honnete")):
                lignes.append({**commun, "chemin": "origine", "score": v + ecart_chemin * sd})
                if relire_origines:
                    lignes.append({**commun, "chemin": "relu", "score": v})
            else:
                lignes.append({**commun, "chemin": "relu", "score": v})
    return lignes


def _final_rejeu(r: dict) -> str:
    v = r["doses"].get("1")
    if v is None or v.get("libelle") is None:
        return "non calculable" if v is None or v["regime"] == "non calculable" else "effectif insuffisant pour un libellé"
    return v["libelle"]


def _brute_rejeu(r: dict) -> str:
    v = r["doses"].get("1")
    return "non calculable" if v is None or v["brute"].get("libelle") is None else v["brute"]["libelle"]


def base_libelle(lb: str) -> str:
    """Libellé sans la mention du plancher (critères de passage sur le libellé de base)."""
    return lb.split(" — ")[0]


def lire_etalon(p: Parametres, rngs: dict, seuils: dict, n_tirages: int, n_nul: int, avec_identite: bool,
                monde: dict | None = None) -> dict:
    """Étalon de transport par famille (textes honnêtes), testabilité et Holm sur les familles, étalon recalculé après
    contrôle d'intensité, sonde d'identité par famille si `avec_identite`. Rend des listes (une entrée par famille)."""
    if monde is None:
        monde = generer(p, rngs["epreuve_plantee"])
    if p.permuter_etiquettes:  # étiquettes permutées : saboteur et jumeau échangés au hasard dans chaque paire
        monde = dict(monde, familles={f: [(j, s) if rngs["nul"].random() < 0.5 else (s, j) for s, j in pq]
                                      for f, pq in monde["familles"].items()})
    K = [c for c, (_, so) in sorted(monde["textes"].items()) if so == "honnete"]
    moy = {s: st.diagnostic_vecteur_moyen([monde["lectures"][s][c] for c in K]) for s in monde["lectures"]}
    res, res_c = {}, {}
    for f, paires in monde["familles"].items():
        famille = [x for pq in paires for x in pq]
        jum = [monde["lectures"][j][c] for _, j in paires for c in K]
        res[f] = st.diagnostic_etalon_transport(moy, paires, rngs["signes"], rngs["plancher_aleatoire"], jum, moy["N"])
        m = np.mean([moy[s] - moy["N"] for s in famille], axis=0)
        m = m / np.linalg.norm(m)
        moy_r = {s: moy[s] - (moy[s] @ m) * m for s in famille}
        res_c[f] = st.diagnostic_etalon_transport(moy_r, paires, rngs["signes"])
    e = st.etalon_familles(res, seuils["alpha"], seuils["u_fort"])
    ec = st.etalon_familles(res_c, seuils["alpha"], seuils["u_fort"])
    out = {"transport": [e["libelles"][f] for f in sorted(res)],
           "transport_controle": [ec["libelles"][f] for f in sorted(res)]}
    if avec_identite:
        ids = []
        for f, paires in monde["familles"].items():
            jumeaux = {j: {c: (monde["textes"][c][0], monde["lectures"][j][c]) for c in K} for _, j in paires}
            lb = st.sonde_identite(jumeaux, rngs, n_tirages, n_nul)["libelle"]
            ids.append("sans libellé" if lb is None else lb)
        out["identite"] = ids
    return out


def lire_monde(p: Parametres, rngs: dict, journal, nom: str, seuils: dict, n_nul: int, n_tirages: int,
               famille: str = "difference_moyennes_appariee", k_externes: int = 5,
               minimums: dict = st.MINIMUMS_DEFAUT, n_nul_identite: int = 200) -> dict:
    """Mode « complet » (une famille) : toutes les lignes ; chaque lecture est une liste d'un élément."""
    alpha = seuils["alpha"]
    if p.n_familles != 1:
        raise GardeArret("mode complet : une famille")
    if p.fuite_de_pli:
        monde = generer(replace(p, fuite_de_pli=False), rngs["epreuve_plantee"])
        jeu = jeu_principal(monde)
        # cas sain jumeau (défaut 3) : unité et tâche tenues à l'écart ensemble, le pli doit passer
        lc.plis_externes(jeu, k_externes, rngs["plis"], {"unites_tenues_a_l_ecart": ["u0_0"],
                                                         "taches_tenues_a_l_ecart": ["t0"]})
        try:  # artefact : unité seule, tâches partagées des deux côtés
            lc.plis_externes(jeu, k_externes, rngs["plis"], {"unites_tenues_a_l_ecart": ["u0_0"]})
        except GardeArret:  # issue attendue de ce monde-artefact (R5) : consignée, jamais poursuivie
            return {"fuite": ["garde arrêtée"]}
        return {"fuite": ["garde muette"]}
    monde = generer(p, rngs["epreuve_plantee"])
    lect = {"fuite": "sans objet"}
    conf = lc.Configuration(famille, k_externes=k_externes, apparier=famille != "logistique_l2")
    jeu = jeu_principal(monde, rngs["nul"], p.permuter_etiquettes)
    ligne, gels = lc.lire_ligne(conf, jeu, rngs["plis"], journal, f"{nom}/principal", rendre_gels=True)
    if ligne["etat"] != "calculée":
        return {c: ["non calculable"] for c in CRITERES if c != "fuite"} | {"fuite": ["sans objet"]}
    npr = lc.nul_reetiquetage(conf, jeu, ligne["aire"], n_nul, rngs["nul"], journal, f"{nom}/principal")
    # [E-5] contraste apparié lu sur le nul réétiqueté par paire de poids
    lect["contraste"] = ("non calculable" if npr["etat"] != "calculé" else
                         "établie" if npr["p"] < alpha else "non établie")
    lect["nul_principal"] = ("non calculable" if npr["etat"] != "calculé" else
                             "au-dessus" if npr["p"] < alpha else "non")
    corr = {c: c for c in st.CHAMPS_TABLE}
    t1, _ = st.charger_table_scores(table_rejeu(monde, ligne, gels, jeu, p.ecart_chemin, True), corr)
    rj = st.rejeu_croise(t1, rngs, {"alpha": alpha}, minimums, n_tirages)
    t2, _ = st.charger_table_scores(table_rejeu(monde, ligne, gels, jeu, p.ecart_chemin, False), corr)
    rj2 = st.rejeu_croise(t2, rngs, {"alpha": alpha}, minimums, n_tirages)
    lect["interaction"] = _final_rejeu(rj)
    lect["interaction_brute"] = _brute_rejeu(rj)
    lect["interaction_sans_controle"] = _final_rejeu(rj2)
    corrigee = rj["doses"].get("1", {}).get("corrigee", {}).get("libelle")
    lect["decalage_maitrise"] = ("oui" if lect["interaction_sans_controle"].startswith("non interprétable") or
                                 corrigee == "non établie à cette puissance" else "non")
    et = lire_etalon(p, rngs, seuils, n_tirages, n_nul_identite, True, monde)
    lect["transport"], lect["transport_controle"], lect["identite"] = (et["transport"][0], et["transport_controle"][0],
                                                                       et["identite"][0])
    lignes_t = _lignes(monde, [j for _, j in monde["paires"]] + ["N"], unite=False)
    jt = lc.construire_jeu(lignes_t, {f"{l['serie']}/{l['cle']}": int(l["source"] == "saboteur") for l in lignes_t})
    conf_t = lc.Configuration(famille, k_externes=k_externes)
    lt = lc.lire_ligne(conf_t, jt, rngs["plis"], journal, f"{nom}/texte", garder_scores=False)
    nt = lc.nul_reetiquetage(conf_t, jt, lt["aire"], n_nul, rngs["nul"], journal, f"{nom}/texte") \
        if lt["etat"] == "calculée" else {"etat": "non calculable"}
    lect["texte"] = ("non calculable" if nt["etat"] != "calculé" else "établi" if nt["p"] < alpha else "non établi")
    return {k: [v] for k, v in lect.items()}


def charger_verites(chemin=CHEMIN_VERITES) -> tuple[dict, str]:
    sha = verifier(chemin)
    v = json.loads(Path(chemin).read_text(encoding="utf-8"))
    for m, d in v["mondes"].items():
        Parametres(**d["composantes"]).verifier()
        if not set(d["modes"]) <= {"complet", "etalon"} or not d["modes"]:
            raise GardeArret(f"vérités : monde {m}, modes {d['modes']}")
        for c in d["criteres"]:
            if (set(c) != {"lecture", "admises", "nature", "borne", "seuil"} or c["lecture"] not in CRITERES or
                    c["nature"] not in NATURES or c["borne"] not in ("haute", "basse", None) or
                    (c["borne"] is None) != (c["seuil"] is None)):
                raise GardeArret(f"vérités : monde {m}, critère {c} mal formé")
    return v, sha


def compter(lectures: list[dict], critere: dict) -> tuple[int, int]:
    """(essais où la lecture tombe dans les lectures admises, essais) ; chaque entrée de liste est un essai ; le
    libellé de base (sans mention du plancher) est comparé."""
    oui = n = 0
    for l in lectures:
        if critere["lecture"] not in l:
            raise GardeArret(f"lecture sans le critère {critere['lecture']}")
        for v in l[critere["lecture"]]:
            n += 1
            oui += base_libelle(str(v)) in critere["admises"]
    return oui, n


def passage(oui: int, n: int, critere: dict) -> dict:
    """Part admise, intervalle exact à 95 %, et passage du critère par la borne : « haute » ≤ seuil, « basse » ≥
    seuil ; sans borne : rapporté seulement."""
    bas, haut = clopper_pearson(oui, n)
    r = {"part_admise": oui / n, "compte": oui, "essais": n, "intervalle_95": [bas, haut]}
    if critere["borne"] == "haute":
        r["passe"] = haut <= critere["seuil"]
    elif critere["borne"] == "basse":
        r["passe"] = bas >= critere["seuil"]
    return r


def clopper_pearson(x: int, n: int, niveau: float = 0.95) -> tuple[float, float]:
    """Intervalle exact de Clopper-Pearson d'une proportion x/n."""
    if n < 1 or not 0 <= x <= n:
        raise GardeArret("Clopper-Pearson : 0 ≤ x ≤ n, n ≥ 1")
    a = 1.0 - niveau
    bas = 0.0 if x == 0 else float(beta.ppf(a / 2, x, n - x + 1))
    haut = 1.0 if x == n else float(beta.ppf(1 - a / 2, x + 1, n - x))
    return bas, haut


def parametres(verites: dict, nom: str, n_paires: int, n_familles: int, n_taches: int, actions: int, d: int,
               mode: str) -> Parametres:
    comp = dict(verites["mondes"][nom]["composantes"])
    if mode == "etalon":
        comp["sources"] = ("honnete",)
    return Parametres(d=d, n_paires=n_paires, n_familles=n_familles, n_taches=n_taches, actions_par_tache=actions,
                      **comp)


__all__ = ["Parametres", "generer", "jeu_principal", "table_rejeu", "lire_monde", "lire_etalon", "charger_verites",
           "compter", "passage", "clopper_pearson", "parametres", "base_libelle", "CRITERES", "CRITERES_ETALON",
           "CHEMIN_VERITES", "asdict"]
