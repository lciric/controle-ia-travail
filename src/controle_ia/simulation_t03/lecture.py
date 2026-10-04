"""Lecture gelée de T0.3 : applique mécaniquement les critères du préenregistrement
(prereg/T0.3-simulation-lemme-theoreme-v1.md, section « Critères de lecture gelés »).

Verdict de cellule : « conforme », « contraire », « non concluant ».
Verdict de prédiction : « confirmée » (toutes conformes), « réfutée » (au moins une contraire),
« non concluante » (sinon). Une contraire statistique appelle une réplication (graine neuve,
5 × R) ; une contraire trajectorielle appelle un audit du code et de la preuve.
"""
from __future__ import annotations

import math

import numpy as np

from . import calibrage as cal
from .lois import facteur_variance_ar1

Z = 4.0                 # seuil Monte-Carlo, en écarts-types
SEUIL_AU_MOINS = 0.99   # P4.3 et P7.2
ALPHA_DEFAUT = 0.05


def _v(p: float, R: int) -> float:
    """Variance d'une proportion, plancher d'un événement (évite un écart-type nul)."""
    return max(p * (1.0 - p), 1.0 / R) / R


def egal(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if abs(d) <= Z * se else "contraire"), d / se


def au_dessus(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if d > Z * se else "contraire" if d < -Z * se else "non concluant"), d / se


def en_dessous(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if d < -Z * se else "contraire" if d > Z * se else "non concluant"), d / se


def au_plus(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if d <= Z * se else "contraire"), d / se


def theorie(p, R, p_th):
    se = math.sqrt(_v(p_th, R))
    return ("conforme" if abs(p - p_th) <= Z * se else "contraire"), (p - p_th) / se


def au_plus_valeur(p, R, v):
    se = math.sqrt(_v(v, R))
    return ("conforme" if p <= v + Z * se else "contraire"), (p - v) / se


def au_dessus_valeur(p, R, v):
    se = math.sqrt(_v(v, R))
    return ("conforme" if p > v + Z * se else "contraire" if p < v - Z * se else "non concluant"), (p - v) / se


def au_moins(p, R, v):
    se = math.sqrt(_v(v, R))
    return ("conforme" if p >= v - Z * se else "contraire"), (p - v) / se


def trajectoriel(violations: int):
    return ("conforme" if violations == 0 else "contraire"), None


BLOCS_DE = {"P1": ("P1a", "P1b"), "P2": ("P2",), "P3": ("P3", "P34"), "P4": ("P4", "P43"),
            "P5": ("P5_temps", "P5_agents"), "P6": ("P6",), "P7": ("P7",), "P8": ("P8",)}


def verdict(cellules: list[dict]) -> str:
    etats = [c["etat"] for c in cellules]
    if not etats:
        return "non concluante"
    if any(e == "contraire" for e in etats):
        return "réfutée"
    return "confirmée" if all(e == "conforme" for e in etats) else "non concluante"


class Lecteur:
    def __init__(self, resultats: dict, alpha: float = ALPHA_DEFAUT):
        self.r = resultats
        self.alpha = alpha
        self.predictions: dict[str, dict] = {}
        self.z_theorie: list[float] = []

    def cellule(self, pred: str, nom: str, fonction, *args, genre: str = "statistique", theorique: bool = False,
                **details):
        etat, z = fonction(*args)
        if theorique and z is not None:
            p_th = args[-1]
            if 0.01 <= p_th <= 0.99:
                self.z_theorie.append(float(z))
        self.predictions.setdefault(pred, {"cellules": []})["cellules"].append(
            {"nom": nom, "etat": etat, "z": None if z is None else round(float(z), 3), "genre": genre, **details})

    def p0(self, cfg: str, alarme: str) -> tuple[float, int]:
        c = self.r["calibrage"][cfg]
        return c["alarmes_p0"][alarme] / c["R0"], c["R0"]

    # --- P1 ---
    def P1(self):
        a = self.alpha
        for g in self.r["P1a"]["groupes"]:
            n0, B, R = g["n0"], g["B"], g["R"]
            tag = f"{g['N']}x{g['T']}/B{B}"
            for c in g["cellules"]:
                v = c["disc_somme"] + c["disc_eterm"] + (1 if c["ecart_max"] > g["tolerance_ecart"] else 0)
                self.cellule("P1.1", f"{tag}/{c['schema']}/m{c['m']}/{c['genre']}", trajectoriel, v,
                             genre="trajectoriel", discordances_somme=c["disc_somme"],
                             discordances_eterm=c["disc_eterm"], ecart_max=c["ecart_max"])
            p_th = cal.puissance_somme(a, n0, B)
            self.cellule("P1.2", tag, theorie, g["alarmes_ref_somme"] / R, R, p_th, theorique=True,
                         p=g["alarmes_ref_somme"] / R, p_th=p_th)
        cel = self.r["P1b"]["cellules"]
        for c in cel:
            p_th = cal.puissance_somme(a, c["n0"], c["B"])
            self.cellule("P1.3", f"{c['N']}x{c['T']}/B{c['B']}", theorie, c["alarmes_somme"] / c["R"], c["R"], p_th,
                         theorique=True, p=c["alarmes_somme"] / c["R"], p_th=p_th)
        par = {(c["N"], c["T"], c["B"]): c for c in cel}
        Bs = sorted({c["B"] for c in cel})
        n0s = sorted({c["n0"] for c in cel if c["N"] == 1})
        for B in Bs:
            for n_a, n_b in zip(n0s[:-1], n0s[1:]):
                ca, cb = par[(1, n_a, B)], par[(1, n_b, B)]
                self.cellule("P1.3", f"décroissance/B{B}/{n_a}>{n_b}", au_dessus, ca["alarmes_somme"] / ca["R"], ca["R"],
                             cb["alarmes_somme"] / cb["R"], cb["R"])
            for c in cel:
                if c["N"] > 1 and c["B"] == B and (1, c["n0"], B) in par:
                    c1 = par[(1, c["n0"], B)]
                    self.cellule("P1.4", f"{c['N']}x{c['T']}~1x{c['n0']}/B{B}", egal, c["alarmes_somme"] / c["R"],
                                 c["R"], c1["alarmes_somme"] / c1["R"], c1["R"])

    # --- P2 ---
    def P2(self):
        a = self.alpha
        cel = self.r["P2"]["cellules"]
        p0, R0 = self.p0(self.r["P2"]["cfg"], "max")
        for c in cel:
            p_th = cal.puissance_max(a, c["n0"], c["B"], c["m"])
            self.cellule("P2.1", f"B{c['B']}/m{c['m']}", theorie, c["alarmes_max"] / c["R"], c["R"], p_th,
                         theorique=True, p=c["alarmes_max"] / c["R"], p_th=p_th)
        for B in sorted({c["B"] for c in cel}):
            seq = sorted([c for c in cel if c["B"] == B], key=lambda c: c["m"])
            for ca, cb in zip(seq[:-1], seq[1:]):
                self.cellule("P2.2", f"B{B}/m{cb['m']}≤m{ca['m']}", au_plus, cb["alarmes_max"] / cb["R"], cb["R"],
                             ca["alarmes_max"] / ca["R"], ca["R"])
            dern = seq[-1]
            self.cellule("P2.3", f"B{B}/m{dern['m']}", au_dessus, dern["alarmes_max"] / dern["R"], dern["R"], p0, R0)

    # --- P3 ---
    def P3(self):
        a = self.alpha
        for g in self.r["P3"]["groupes"]:
            tag = f"{g['N']}x{g['T']}/B{g['B']}"
            for m, viol in g["violations"].items():
                self.cellule("P3.1", f"{tag}/m{m}", trajectoriel, sum(viol.values()), genre="trajectoriel", **viol)
            p_th = cal.borne_terminale(a, g["n0"], g["B"], g["rho"])
            self.cellule("P3.3", tag, theorie, g["alarmes_terminal"] / g["R"], g["R"], p_th, theorique=True,
                         p=g["alarmes_terminal"] / g["R"], p_th=p_th)
        for c in self.r["P34"]["cellules"]:
            R = c["R"]
            ref = c["comptes"]["e_unilat_cal"]["a_temps"] / R
            for a_ in ("page", "detecteur_e"):
                self.cellule("P3.4", f"B{c['B']}/m{c['m']}/{a_}>e_unilat_cal", au_dessus,
                             c["comptes"][a_]["a_temps"] / R, R, ref, R)

    # --- P4 ---
    def P4(self):
        for c in self.r["P4"]["configs"]:
            tag, cfg = f"{c['N']}x{c['T']}", f"gauss_{c['N']}x{c['T']}"
            for arr, t in c["T1"].items():
                v = sum(t["valeurs_differentes"].values()) + sum(t["discordances"].values())
                self.cellule("P4.1", f"{tag}/{arr}", trajectoriel, v, genre="trajectoriel", **t)
            for arr, comptes in c["T2"].items():
                for al, k in comptes.items():
                    p0, R0 = self.p0(cfg, al)
                    self.cellule("P4.2", f"{tag}/{arr}/{al}", egal, k / c["R"], c["R"], p0, R0)
        p = self.r["P43"]
        p0, R0 = self.p0(p["cfg"], "dispersion_agents")
        self.cellule("P4.3", "rebrassage_total", au_moins, p["alarmes_total"] / p["R"], p["R"], SEUIL_AU_MOINS)
        self.cellule("P4.3", "rebrassage_intra_agent", egal, p["alarmes_intra_agent"] / p["R"], p["R"], p0, R0)

    # --- P5 ---
    def P5(self):
        t = self.r["P5_temps"]
        R, cfg = t["R"], t["cfg"]
        for arr, c in t["arrangements"].items():
            v = c["viol_page"] + c["viol_glissante"] + c["borne_sans_alarme"]
            self.cellule("P5.1", arr, trajectoriel, v, genre="trajectoriel", viol_page=c["viol_page"],
                         viol_glissante=c["viol_glissante"], borne_sans_alarme=c["borne_sans_alarme"])
        for arr, c in t["arrangements"].items():
            if c["r"] >= 5 and arr.startswith("bloc_"):
                for al in ("glissante_5", "page"):
                    p0, R0 = self.p0(cfg, al)
                    self.cellule("P5.2", f"{arr}/{al}", au_dessus, c["alarmes"][al] / R, R, p0, R0)
        for arr, cible in (("apparie_autocorr", "autocorr"), ("apparie_suites", "suites")):
            c = t["arrangements"][arr]
            incomplet = c["ecart_hors_tolerance"] / R > 0.01
            p0, R0 = self.p0(cfg, cible)
            if incomplet:
                self.cellule("P5.3", f"{arr}/{cible}", lambda: ("non concluant", None), ecart_hors_tolerance=c["ecart_hors_tolerance"])
            else:
                self.cellule("P5.3", f"{arr}/{cible}", au_plus, c["alarmes"][cible] / R, R, p0, R0)
            for al in ("glissante_5", "page"):
                p0l, R0l = self.p0(cfg, al)
                self.cellule("P5.3", f"{arr}/{al}", au_dessus, c["alarmes"][al] / R, R, p0l, R0l)
        a = self.r["P5_agents"]
        nom_ce = f"co_elevation_{a['mc']}"
        self.cellule("P5.4", f"{nom_ce}≥{a['mc']}·v({a['mc']})", trajectoriel, a["viol_co_elevation"],
                     genre="trajectoriel")
        p0, R0 = self.p0(a["cfg"], nom_ce)
        self.cellule("P5.5", nom_ce, au_dessus, a["alarmes"][nom_ce] / a["R"], a["R"], p0, R0)

    # --- P6 ---
    def P6(self):
        a = self.alpha
        for c in self.r["P6"]["cellules"]:
            loi, R, k, cfg = c["loi"], c["R"], c["alarmes"], c["cfg"]
            p = {al: n / R for al, n in k.items()}
            nom = c["nom"]
            if c["role"] == "copule_temps":
                phi, gauss = float(loi["phi"]), loi.get("marginale", "gauss") == "gauss"
                if phi > 0:
                    if gauss:
                        for al in ("somme", "e_unilat_ville"):
                            self.cellule("P6.1", f"{nom}/{al}", au_dessus, p[al], R, *self.p0(cfg, al))
                    self.cellule("P6.1", f"{nom}/max", au_plus, p["max"], R, *self.p0(cfg, "max"))
                    self.cellule("P6.1", f"{nom}/autocorr", au_dessus, p["autocorr"], R, *self.p0(cfg, "autocorr"))
                else:
                    if gauss:
                        for al in ("somme", "e_unilat_ville"):
                            self.cellule("P6.2", f"{nom}/{al}", en_dessous, p[al], R, *self.p0(cfg, al))
                    self.cellule("P6.2", f"{nom}/autocorr_abs", au_dessus, p["autocorr_abs"], R,
                                 *self.p0(cfg, "autocorr_abs"))
                if gauss:
                    p_th = cal.rejet_somme_sous_variance(a, facteur_variance_ar1(phi, int(loi["T"])))
                    self.cellule("P6.3", f"{nom}/somme", theorie, p["somme"], R, p_th, theorique=True,
                                 p=p["somme"], p_th=p_th)
            elif c["role"] == "equicorrelation":
                cc, N = float(loi["c"]), int(loi["N"])
                p_th = cal.rejet_somme_sous_variance(a, 1.0 + (N - 1) * cc)
                self.cellule("P6.4", f"{nom}/somme=théorie", theorie, p["somme"], R, p_th, theorique=True,
                             p=p["somme"], p_th=p_th)
                for al in ("somme", "e_unilat_ville", "co_elevation_N", "correlation_agents"):
                    self.cellule("P6.4", f"{nom}/{al}", au_dessus, p[al], R, *self.p0(cfg, al))
                self.cellule("P6.4", f"{nom}/max", au_plus, p["max"], R, *self.p0(cfg, "max"))
            elif c["role"] == "construction_2606":
                T = int(loi["T"])
                phi0 = float(self.r["calibrage"][cfg]["loi"]["phi"])
                rapport = facteur_variance_ar1(float(loi["phi"]), T) / facteur_variance_ar1(phi0, T)
                p_th = cal.rejet_somme_sous_variance(a, rapport)
                self.cellule("P6.5", f"{nom}/somme=théorie", theorie, p["somme"], R, p_th, theorique=True,
                             p=p["somme"], p_th=p_th)
                self.cellule("P6.5", f"{nom}/max", au_plus, p["max"], R, *self.p0(cfg, "max"))
                self.cellule("P6.5", f"{nom}/autocorr", au_dessus, p["autocorr"], R, *self.p0(cfg, "autocorr"))

    # --- P7 ---
    def P7(self):
        t = self.r["P7"]
        R, cfg = t["R"], t["cfg"]
        for arr, c in t["arrangements"].items():
            v = c["viol_inclusion_haute"] + c["viol_inclusion_basse"] + c["viol_sommes_partielles"]
            self.cellule("P7.1", arr, trajectoriel, v, genre="trajectoriel", **{k: c[k] for k in c if k.startswith("viol")})
            for al in ("page", "glissante_10"):
                self.cellule("P7.3", f"{arr}/{al}", au_dessus, c["alarmes"][al] / R, R, *self.p0(cfg, al))
        c = t["arrangements"]["tri_croissant"]
        self.cellule("P7.2", "tri_croissant/e_bilat_ville", au_moins, c["alarmes"]["e_bilat_ville"] / R, R,
                     SEUIL_AU_MOINS)

    # --- P8 ---
    def P8(self, bien_specifies, signe, depasse):
        a = self.alpha
        par_nom = {s["nom"]: s for s in self.r["P8"]["reglages"]}
        for s in self.r["P8"]["reglages"]:
            R, p = s["R"], s["alarmes"]["e_unilat_ville"] / s["R"]
            if s["nom"] in bien_specifies:
                self.cellule("P8.1", s["nom"], au_plus_valeur, p, R, a)
            if s["nom"] in signe:
                ref = par_nom[signe[s["nom"]]]
                self.cellule("P8.2", f"{s['nom']}>{ref['nom']}", au_dessus, p, R,
                             ref["alarmes"]["e_unilat_ville"] / ref["R"], ref["R"])
            if s["nom"] in depasse:
                self.cellule("P8.3", s["nom"], au_dessus_valeur, p, R, a)
            c = s["conforme"]
            for st, liste in c["alarmes_par_tirage"].items():
                taux = np.array(liste, dtype=float) / c["n_test"]
                se = max(float(taux.std(ddof=1)) / math.sqrt(c["L"]),
                         math.sqrt(a * (1 - a) / (c["L"] * c["n_test"])))
                d = float(taux.mean()) - c["taux_theorique"]
                etat = "conforme" if abs(d) <= Z * se else "contraire"
                self.cellule("P8.4", f"{s['nom']}/{st}", lambda e=etat, zz=d / se: (e, zz),
                             taux=float(taux.mean()), taux_theorique=c["taux_theorique"])

    def audit_symetrie(self) -> dict:
        z = np.array(self.z_theorie)
        s2 = float(z.var(ddof=1)) if z.size > 1 else float("nan")
        declenche = bool(z.size > 1 and (s2 < 0.3 or s2 > 3.0))
        return {"n": int(z.size), "variance_z": s2, "bornes": [0.3, 3.0], "audit_declenche": declenche}

    def lire(self, p8: dict) -> dict:
        for methode, blocs in BLOCS_DE.items():
            if all(x in self.r for x in blocs):
                getattr(self, methode)(**(p8 if methode == "P8" else {}))
        sortie = {}
        for pred in sorted(self.predictions):
            cel = self.predictions[pred]["cellules"]
            v = verdict(cel)
            a_repliquer = [c["nom"] for c in cel if c["etat"] == "contraire" and c["genre"] == "statistique"]
            a_auditer = [c["nom"] for c in cel if c["etat"] == "contraire" and c["genre"] == "trajectoriel"]
            sortie[pred] = {"verdict": v, "n_cellules": len(cel),
                            "n_conformes": sum(c["etat"] == "conforme" for c in cel),
                            "n_contraires": sum(c["etat"] == "contraire" for c in cel),
                            "a_repliquer": a_repliquer, "a_auditer": a_auditer, "cellules": cel}
        return {"predictions": sortie, "audit_symetrie": self.audit_symetrie(), "z_seuil": Z}


def lire(resultats: dict, alpha: float, p8: dict) -> dict:
    return Lecteur(resultats, alpha).lire(p8)


def fusionner(principale: dict, replication: dict) -> dict:
    """Règle de réplication gelée : une cellule statistique « contraire » de la lecture principale
    devient « non concluant » si sa réplication (graine neuve, 5 × R) est conforme ; elle reste
    « contraire » sinon, ou si elle n'a pas été répliquée. Les cellules trajectorielles ne changent pas."""
    import copy

    sortie = copy.deepcopy(principale)
    for pred, x in sortie["predictions"].items():
        rep = {c["nom"]: c for c in replication.get("predictions", {}).get(pred, {}).get("cellules", [])}
        for c in x["cellules"]:
            if c["etat"] == "contraire" and c["genre"] == "statistique" and c["nom"] in rep:
                c["replication"] = rep[c["nom"]]["etat"]
                if rep[c["nom"]]["etat"] == "conforme":
                    c["etat"] = "non concluant"
                    c["note"] = "contraire en lecture principale, conforme en réplication : bruit Monte-Carlo probable"
        x["verdict"] = verdict(x["cellules"])
        x["n_conformes"] = sum(c["etat"] == "conforme" for c in x["cellules"])
        x["n_contraires"] = sum(c["etat"] == "contraire" for c in x["cellules"])
    return sortie


def enonces_du_programme(lecture: dict) -> list[dict]:
    """Table gelée : comment chaque phrase du programme (section 3) et du brief (T0.3) se lit."""
    v = {k: x["verdict"] for k, x in lecture["predictions"].items()}

    def tous(*ks):
        return all(v.get(k) == "confirmée" for k in ks)

    lignes = [
        {"enonce": "Lemme : « la puissance ne dépend que de B et de la variance — pas de la répartition »",
         "lecture": ("exact pour la statistique terminale à n₀ fixé, la « variance » étant celle de la "
                     "statistique (n₀σ²) ; faux à variance par action fixée quand n₀ = NT varie ; faux pour la "
                     "lecture séquentielle, qui dépend du calendrier (borne inférieure invariante seulement)")
         if tous("P1.1", "P1.2", "P1.3", "P1.4", "P3.1", "P3.3") else "non établi : voir P1 et P3",
         "appui": ["P1.1", "P1.2", "P1.3", "P1.4", "P3.1", "P3.3"]},
        {"enonce": "Brief T0.3 : « celle du max par action s'effondre quand la fragmentation croît »",
         "lecture": ("exact, avec un plancher strictement au-dessus de α à n₀ fixé")
         if tous("P2.1", "P2.2", "P2.3") else "non établi : voir P2", "appui": ["P2.1", "P2.2", "P2.3"]},
        {"enonce": "Théorème : « toute statistique de marginales (max, moyenne, somme cumulée) a une puissance "
                   "égale au taux de faux positifs » (dommage dans la corrélation, marginale préservée)",
         "lecture": ("vrai en classe C (multi-ensemble préservé) pour les statistiques symétriques, et pour "
                     "toute statistique sous rebrassage uniforme ; faux en classe K (copule) : somme au-dessus "
                     "de α pour une dépendance positive, en dessous pour une négative, max à α ou en dessous")
         if tous("P4.1", "P4.2", "P6.1", "P6.2", "P6.3") else "non établi : voir P4 et P6",
         "appui": ["P4.1", "P4.2", "P6.1", "P6.2", "P6.3", "P6.4", "P6.5"]},
        {"enonce": "Théorème : « il faut un agrégateur d'autocorrélation (temps) ou de co-élévation (agents) »",
         "lecture": ("nécessaire en classe K (l'autocorrélation et la co-élévation détectent), insuffisant "
                     "face à un attaquant adaptatif de classe C : seules les statistiques locales (balayage, "
                     "Page, co-élévation) gardent une garantie (T3)")
         if tous("P5.1", "P5.3", "P6.1", "P6.4") else "non établi : voir P5 et P6",
         "appui": ["P5.1", "P5.2", "P5.3", "P5.4", "P5.5", "P6.1", "P6.4"]},
        {"enonce": "Brief T0.3 : « la somme cumulée échoue » (attaque à marginale préservée)",
         "lecture": ("exact pour la somme terminale en classe C ; exact au sens adverse pour la somme "
                     "séquentielle unilatérale (T4) ; faux en classe K")
         if tous("P4.1", "P7.1", "P6.1") else "non établi : voir P4, P6 et P7",
         "appui": ["P4.1", "P6.1", "P7.1", "P7.2", "P7.3"]},
        {"enonce": "Garde de G1 : « taux de faux positifs des agrégateurs toujours valides vérifié sur épisodes "
                   "honnêtes »",
         "lecture": ("décisive : la règle de Ville dépasse α sous effet épisode, corrélation entre agents ou σ "
                     "sous-estimé ; le calibrage conforme sur épisodes honnêtes entiers tient son taux")
         if tous("P8.1", "P8.2", "P8.3", "P8.4") else "non établi : voir P8",
         "appui": ["P8.1", "P8.2", "P8.3", "P8.4"]},
    ]
    return lignes
