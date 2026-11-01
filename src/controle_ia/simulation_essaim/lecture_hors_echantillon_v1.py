"""Lecture gelée du préenregistrement hors échantillon (`essaim-hors-echantillon-v1`).

Critères, intervalles exacts, verdicts, réplication : ceux de la version 1 (`lecture`, `simulation_t03.lecture`),
importés tels quels. Ajout : le critère « dans la bande » (HS.3) — conforme si haut(IC) ≥ borne basse et
bas(IC) ≤ borne haute de la forme close de Bonferroni (`bornes_synchro_v1`), contraire sinon.

Prédictions :
- HS.1 à HS.5 (famille S, loi de référence, configurations neuves) ;
- HQ.1 à HQ.7 (famille Q, équicorrélation) ;
- HP.1 à HP.5 (famille P, loi honnête réelle de P3).
Les prédictions de sens et de valeur (HS.4, HS.5, HQ.4 à HQ.7, HP.4, HP.5) sont lues dans la grille scellée
(`grille["predictions"]`), écrite avant tout calcul par `generer_grille_v1.py` (règles du préenregistrement).
"""
from __future__ import annotations

import math

from scipy import stats

from . import bornes_synchro_v1 as BS
from . import calibrage as cal
from . import statistiques as S
from .lecture import (CRITERES_SENS, BORNES_AUDIT, au_dessus_valeur, au_moins_valeur, egal, region,  # noqa: F401
                      trajectoriel, verdict, fusionner)

VERSION = "lecture_hors_echantillon_v1"
INVARIANTES_T = ("somme", "max", "comptage", "agent_moyenne", "agent_comptage")

STATUTS = {
    "HS.1": "preuve (T1, trajectoriel) ; instrument", "HS.2": "preuve (T1) ; instrument",
    "HS.3": "forme close exacte (bornes de Bonferroni, calculées sans tirage)",
    "HS.4": "conséquence de la forme close HS.3 (signe) ; contredit la lecture « frontière à ⌈K/2⌉ »",
    "HS.5": "heuristique (Schur-concavité) ; généralisation à T = 10 d'un effet vu en v1",
    "HQ.1": "preuve (T1, trajectoriel) ; instrument", "HQ.2": "preuve (T1) ; instrument",
    "HQ.3": "borne exacte (quadrature)", "HQ.4": "conséquence de la borne exacte HQ.3 (signe)",
    "HQ.5": "heuristique : extrapolation à c = 0,3 du mécanisme conjecturé de HE6.3 (vu en v1)",
    "HQ.6": "rejouée : cellule signalée par le lecteur R13, vue au run décisif v1",
    "HQ.7": "heuristique : généralisation de HQ.6 à c = 0,3",
    "HP.1": "preuve (T1, trajectoriel, toute loi) ; instrument", "HP.2": "preuve (T1) ; instrument",
    "HP.3": "preuve (échangeabilité des essaims entiers)",
    "HP.4": "modèle de substitution gaussien (moments déclarés), marge 0,15",
    "HP.5": "modèle de substitution gaussien (moments déclarés), marge 0,015 : co-élévation et moyenne par pas",
    "HP.6": "modèle de substitution gaussien (moments déclarés), marge 0,015 : e-valeur cumulée et détecteur e",
}


def dans_bande(k, R, bas_th, haut_th, g):
    b, h = cal.intervalle_cp(k, R, g)
    mil = 0.5 * (bas_th + haut_th)
    se = math.sqrt(max(mil * (1 - mil), 1.0 / R) / R)
    etat = "conforme" if (h >= bas_th and b <= haut_th) else "contraire"
    return etat, (k / R - mil) / se, {"p": k / R, "ic": [b, h], "valeur": mil, "bande": [bas_th, haut_th], "R": R}


class LecteurHO:
    def __init__(self, resultats: dict, grille: dict):
        self.r, self.g = resultats, grille
        self.alpha, self.q = float(grille["alpha"]), float(grille["q"])
        self.gamma = float(grille["lecture"]["gamma"])
        self.predictions: dict[str, list] = {}
        self.z_formes, self.z_egalites = [], []
        self.cellules_nommees: dict[str, dict] = {}

    def cellule(self, pred, nom, fonction, *args, genre="statistique", forme_close=False, egalite=False, **details):
        etat, z, d = fonction(*args)
        if forme_close and z is not None and 0.01 <= d["valeur"] <= 0.99:
            self.z_formes.append(float(z))
        if egalite and z is not None:
            self.z_egalites.append(float(z))
        self.predictions.setdefault(pred, []).append(
            {"nom": nom, "etat": etat, "z": None if z is None else round(float(z), 3), "genre": genre, **d, **details})

    def _commun(self, fam, tag, c, k0, R0):
        """Trajectoriel (identités, sémantique de la synchronisation) et égalités des alarmes G_T-invariantes."""
        v = sum(c["valeurs_differentes"].values()) + sum(c["discordances"].values()) + \
            sum(c[x] for x in c if x.startswith("viol_"))
        self.cellule(f"{fam}.1", tag, trajectoriel, v, genre="trajectoriel")
        for a in c["invariantes"]:
            self.cellule(f"{fam}.2", f"{tag}/{a}", egal, c["alarmes"][a], c["R"], k0[a], R0, self.gamma, egalite=True)
        self.cellules_nommees[tag] = {"c": c, "k0": k0, "R0": R0}

    # --- famille S ---
    def S(self):
        for c in self.r["S"]["cellules"]:
            cfg = c["cfg"]
            cal_ = self.r["S"]["calibrage"][cfg]
            tag = f"S/{cfg}/{c['nom']}"
            self._commun("HS", tag, c, cal_["alarmes_p0"], cal_["R0"])
            K, T, m = c["K"], c["T"], int(c["m"])
            seuil = tuple(cal_["seuils"]["coelev_comptage"])
            bas, haut = BS.bornes_puissance(K, T, m, self.q, seuil)
            self.cellule("HS.3", f"{tag}/coelev_comptage∈bande", dans_bande, c["alarmes"]["coelev_comptage"], c["R"],
                         bas, haut, self.gamma, forme_close=True)
            if m == K:
                cT = cal_["seuils"]["pas_moyenne"][0]
                lb = (1.0 - stats.norm.cdf(cT / math.sqrt(K)) ** T) ** K
                self.cellule("HS.3", f"{tag}/pas_moyenne≥borne", au_moins_valeur, c["alarmes"]["pas_moyenne"], c["R"],
                             lb, self.gamma, borne=lb)

    # --- famille Q ---
    def Q(self):
        for x in self.r["Q"]["lois"]:
            calib = x["calibrage"]
            for c in x["cellules"]:
                tag = f"Q/{x['cfg']}/{x['loi_nom']}/{c['nom']}"
                self._commun("HQ", tag, c, calib["alarmes_p0"], calib["R0"])
                seuil = tuple(calib["seuils"]["coelev_comptage"])
                lb = BS.borne_synchro_correlee(c["K"], c["T"], int(c["m"]), float(x["loi"]["c"]), self.q, seuil)
                self.cellule("HQ.3", f"{tag}/coelev_comptage≥borne", au_moins_valeur, c["alarmes"]["coelev_comptage"],
                             c["R"], lb, self.gamma, borne=lb)

    # --- famille P ---
    def P(self):
        for x in self.r["P"]["sondes"]:
            calib = x["calibrage"]
            for c in x["cellules"]:
                self._commun("HP", f"P/{x['sonde']}/{c['nom']}", c, calib["alarmes_p0"], calib["R0"])
            conf = x["conforme"]
            bas, haut, taux = cal.region_conforme(conf["L"], conf["n_test"], conf["K"], self.alpha, self.gamma)
            for s, liste in conf["alarmes_par_tirage"].items():
                tot = int(sum(liste))
                self.cellule("HP.3", f"P/{x['sonde']}/conforme/{s}", region, tot, bas, haut,
                             taux=tot / (conf["L"] * conf["n_test"]), taux_theorique=taux)

    # --- prédictions de sens et de valeur, lues dans la grille ---
    def listees(self):
        for p in self.g["predictions"]:
            tag = p["cellule"]
            if tag.split("/")[0] not in self.r:      # famille non rejouée (réplication) : rien à lire
                continue
            if tag not in self.cellules_nommees:
                self.cellule(p["pred"], f"{tag}/{p['alarme']}", trajectoriel, 1, genre="trajectoriel",
                             absente=True)              # cellule de la grille absente : contraire, audit
                continue
            d = self.cellules_nommees[tag]
            k, R = d["c"]["alarmes"][p["alarme"]], d["c"]["R"]
            if p["sens"] == "au_moins_x":
                self.cellule(p["pred"], f"{tag}/{p['alarme']}≥{p['valeur']}", au_dessus_valeur, k, R,
                             float(p["valeur"]), self.gamma, sens=p["sens"])
            else:
                self.cellule(p["pred"], f"{tag}/{p['alarme']}", CRITERES_SENS[p["sens"]], k, R, d["k0"][p["alarme"]],
                             d["R0"], self.gamma, sens=p["sens"])

    def audit(self) -> dict:
        import numpy as np

        sortie = {"bornes": list(BORNES_AUDIT)}
        for nom, liste in (("formes_closes", self.z_formes), ("egalites", self.z_egalites)):
            z = np.array(liste)
            s2 = float(z.var(ddof=1)) if z.size > 1 else float("nan")
            sortie[nom] = {"n": int(z.size), "variance_z": s2, "moyenne_z": float(z.mean()) if z.size else float("nan"),
                           "hors_bornes": bool(z.size > 1 and not (BORNES_AUDIT[0] <= s2 <= BORNES_AUDIT[1]))}
        sortie["audit_declenche"] = sortie["formes_closes"]["hors_bornes"] or sortie["egalites"]["hors_bornes"]
        return sortie

    def lire(self) -> dict:
        for fam in ("S", "Q", "P"):
            if fam in self.r:
                getattr(self, fam)()
        self.listees()
        sortie = {}
        for pred in sorted(self.predictions):
            cel = self.predictions[pred]
            sortie[pred] = {"verdict": verdict(cel), "statut": STATUTS.get(pred, "?"), "n_cellules": len(cel),
                            "n_conformes": sum(x["etat"] == "conforme" for x in cel),
                            "n_contraires": sum(x["etat"] == "contraire" for x in cel),
                            "a_repliquer": [x["nom"] for x in cel if x["etat"] == "contraire" and x["genre"] == "statistique"],
                            "a_auditer": [x["nom"] for x in cel if x["etat"] == "contraire" and x["genre"] == "trajectoriel"],
                            "cellules": cel}
        return {"predictions": sortie, "audit_symetrie": self.audit(), "gamma": self.gamma, "version": VERSION}


def lire(resultats: dict, grille: dict) -> dict:
    return LecteurHO(resultats, grille).lire()


BLOCS_DE = {"HS": ("S",), "HQ": ("Q",), "HP": ("P",)}

LIGNES_E = [
    {"enonce": "Dual, axe du temps, sous les trois lois (référence, corrélée, P3 réelle) : la surveillance par agent est "
               "aveugle à la synchronisation",
     "lecture": "Vérifié : identités au bit près et taux égal au taux sous P₀, sous chaque loi, cellules neuves.",
     "exiges": ["HS.1", "HS.2", "HQ.1", "HQ.2", "HP.1", "HP.2"]},
    {"enonce": "Frontière de la co-élévation sous la loi de référence : « au-dessus de son taux pour m ≥ ⌈K/2⌉ et pas "
               "en dessous » ?",
     "lecture": ("Non comme frontière : la puissance suit la forme close exacte (bornes de Bonferroni) et dépasse déjà "
                 "son taux à m/K = 0,3 ; ⌈K/2⌉ n'était qu'une condition suffisante aux tailles de v1. La « frontière » "
                 "est une fonction de (K, T, q), sans saut à ⌈K/2⌉."),
     "exiges": ["HS.3", "HS.4"]},
    {"enonce": "Version séquentielle sous la loi de référence, T = 10 : au plus à son taux, en dessous à m = K",
     "lecture": "Reproduit à des tailles neuves (heuristique de Schur-concavité, non démontrée).",
     "exiges": ["HS.5"]},
    {"enonce": "Sous corrélation entre copies : la frontière se déplace",
     "lecture": ("Borne exacte respectée ; la co-élévation reste au-dessus de son taux là où la borne l'impose, et une "
                 "synchronisation partielle sous c = 0,3 la fait passer sous son taux (mécanisme de HE6.3 étendu)."),
     "exiges": ["HQ.3", "HQ.4", "HQ.5"]},
    {"enonce": "Sous corrélation entre copies : la version séquentielle échappe-t-elle à la synchronisation partielle ?",
     "lecture": ("Oui : sous c = 0,4 (cellule signalée, rejouée) et c = 0,3, m = 5, l'e-valeur cumulée et le détecteur e "
                 "passent au-dessus de leur taux. La ligne « n'échappe pas » de v1 ne vaut que sous la loi indépendante."),
     "exiges": ["HQ.6", "HQ.7"]},
    {"enonce": "Loi honnête réelle de P3 : le calibrage sur essaims honnêtes entiers garde son taux",
     "lecture": "Vérifié : région conforme exacte respectée pour chaque sonde.",
     "exiges": ["HP.3"]},
    {"enonce": "Loi honnête réelle de P3 : la co-élévation détecte la synchronisation totale avec une puissance ≥ x",
     "lecture": "Vérifié aux valeurs x préenregistrées (modèle de substitution moins 0,15), pour chaque sonde.",
     "exiges": ["HP.4"]},
    {"enonce": "Loi honnête réelle de P3 : la frontière ⌈K/2⌉ tient-elle ?",
     "lecture": ("Non : le sens de la puissance de la co-élévation et de l'e-valeur sous synchronisation partielle suit le "
                 "profil moyen des pas de la sonde (modèle de substitution confirmé), pas la règle m ≥ ⌈K/2⌉."),
     "exiges": ["HP.5"]},
    {"enonce": "Loi honnête réelle de P3 : la version séquentielle « n'échappe pas » à la synchronisation ?",
     "lecture": ("Non établi en général : selon la sonde, l'e-valeur cumulée passe au-dessus (profil culminant en fin "
                 "d'épisode) ou en dessous (profil culminant au début) de son taux, comme le modèle de substitution "
                 "le prédisait."),
     "exiges": ["HP.6"]},
]

PHRASE_PORTEE = ("Simulation sur matrices de scores (synthétiques, et épisodes honnêtes réels de P3 rééchantillonnés "
                 "indépendamment) : la menace est un motif choisi dans la matrice, pas une idée qui se propage ; les "
                 "agents d'un essaim P3 sont indépendants (aucun vrai essaim n'a été observé).")


def enonces(lecture: dict) -> list[dict]:
    v = {k: x["verdict"] for k, x in lecture["predictions"].items()}
    return [{"enonce": l["enonce"], "exiges": l["exiges"],
             "lecture": l["lecture"] if all(v.get(k) == "confirmée" for k in l["exiges"])
             else "non établi : voir " + ", ".join(l["exiges"]),
             "verdicts": {k: v.get(k, "absente") for k in l["exiges"]}} for l in LIGNES_E]
