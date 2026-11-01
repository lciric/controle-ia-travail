"""Lecture gelée de la simulation d'essaim : applique mécaniquement les critères du préenregistrement
(section « Critères de lecture gelés »), avec des intervalles exacts de Clopper-Pearson de niveau 1 − γ.

Verdict de cellule : « conforme », « contraire », « non concluant ». Verdict de prédiction : « confirmée »
(toutes conformes), « réfutée » (au moins une contraire), « non concluante » (sinon) — `verdict` de T0.3.
Une contraire statistique appelle une réplication (graines neuves, 5 × R) ; une contraire trajectorielle,
un audit du code et de la preuve. Fusion d'une réplication : `simulation_t03.lecture.fusionner`.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import stats

from ..simulation_t03.lecture import fusionner, verdict  # noqa: F401  (règle de réplication de T0.3)
from . import calibrage as cal
from . import statistiques as S

BORNES_AUDIT = (0.3, 3.0)       # variance admise des écarts réduits (R4), comme T0.3
FORMES_CLOSES = ("somme", "max", "comptage", "agent_moyenne", "agent_comptage", "pas_moyenne", "coelev_comptage")


def _se(p: float, R: int) -> float:
    return math.sqrt(max(p * (1.0 - p), 1.0 / R) / R)


# --- critères (renvoient (état, écart réduit, détails)) ; chaque cellule statistique consigne son taux p, son
#     intervalle exact ic, et la référence (taux p_ref et intervalle ic_ref, ou valeur) ---
def _deux(k, R, k0, R0, g):
    (b, h), (b0, h0) = cal.intervalle_cp(k, R, g), cal.intervalle_cp(k0, R0, g)
    return (b, h), (b0, h0), {"p": k / R, "ic": [b, h], "p_ref": k0 / R0, "ic_ref": [b0, h0], "R": R, "R_ref": R0}


def _un(k, R, v, g):
    b, h = cal.intervalle_cp(k, R, g)
    return (b, h), {"p": k / R, "ic": [b, h], "valeur": v, "R": R}


def egal(k, R, k0, R0, g):
    (b, h), (b0, h0), d = _deux(k, R, k0, R0, g)
    p, p0 = k / R, k0 / R0
    etat = "conforme" if (b <= h0 and b0 <= h) else "contraire"
    return etat, (p - p0) / math.sqrt(_se(p, R) ** 2 + _se(p0, R0) ** 2), d


def egal_valeur(k, R, v, g):
    (b, h), d = _un(k, R, v, g)
    return ("conforme" if b <= v <= h else "contraire"), (k / R - v) / _se(v, R), d


def au_dessus(k, R, k0, R0, g):
    (b, h), (b0, h0), d = _deux(k, R, k0, R0, g)
    return ("conforme" if b > h0 else "contraire" if h < b0 else "non concluant"), None, d


def au_plus(k, R, k0, R0, g):
    (b, h), (b0, h0), d = _deux(k, R, k0, R0, g)
    return ("conforme" if b <= h0 else "contraire"), None, d


def en_dessous(k, R, k0, R0, g):
    (b, h), (b0, h0), d = _deux(k, R, k0, R0, g)
    return ("conforme" if h < b0 else "contraire" if b > h0 else "non concluant"), None, d


CRITERES_SENS = {"au_dessus": au_dessus, "au_plus": au_plus, "en_dessous": en_dessous}


def au_dessus_valeur(k, R, v, g):
    (b, h), d = _un(k, R, v, g)
    return ("conforme" if b > v else "contraire" if h < v else "non concluant"), None, d


def au_plus_valeur(k, R, v, g):
    (b, h), d = _un(k, R, v, g)
    return ("conforme" if b <= v else "contraire"), None, d


def au_moins_valeur(k, R, v, g):
    (b, h), d = _un(k, R, v, g)
    return ("conforme" if h >= v else "contraire"), None, d


def region(k, bas, haut):
    return ("conforme" if bas <= k <= haut else "contraire"), None, {"region": [bas, haut]}


def trajectoriel(violations):
    return ("conforme" if violations == 0 else "contraire"), None, {"violations": int(violations)}


class Lecteur:
    def __init__(self, resultats: dict, grille: dict):
        self.r = resultats
        self.g = grille
        self.alpha = float(grille["alpha"])
        self.q = float(grille["q"])
        self.gamma = float(grille["lecture"]["gamma"])
        self.predictions: dict[str, dict] = {}
        self.z_formes: list[float] = []
        self.z_egalites: list[float] = []

    def cellule(self, pred, nom, fonction, *args, genre="statistique", forme_close=False, egalite=False, **details):
        etat, z, d = fonction(*args)
        if forme_close and z is not None and 0.01 <= d["valeur"] <= 0.99:
            self.z_formes.append(float(z))
        if egalite and z is not None:
            self.z_egalites.append(float(z))
        self.predictions.setdefault(pred, {"cellules": []})["cellules"].append(
            {"nom": nom, "etat": etat, "z": None if z is None else round(float(z), 3), "genre": genre, **d, **details})

    def p0(self, cfg: str, alarme: str) -> tuple[int, int]:
        c = self.r["calibrage"][cfg]
        return c["alarmes_p0"][alarme], c["R0"]

    def seuils(self, cfg: str) -> dict:
        return {a: tuple(v) for a, v in self.r["calibrage"][cfg]["seuils"].items()}

    # --- classe C : HE1 (G_A), HE2 (G_T, échappement), HE5 (T2) ---
    def classe_C(self):
        g = self.gamma
        for c in self.r["C"]["cellules"]:
            cfg, nom, genre, groupe, R = c["cfg"], c["nom"], c["genre"], c["groupe"], c["R"]
            K, T = c["K"], c["T"]
            tag = f"{cfg}/{nom}"
            viol = sum(c["valeurs_differentes"].values()) + sum(c["discordances"].values())
            if genre.startswith("rebrassage"):
                for a, k in c["alarmes"].items():
                    self.cellule("HE5.1", f"{tag}/{a}", egal, k, R, *self.p0(cfg, a), g, egalite=True)
            if groupe == "agents":
                self.cellule("HE1.1", tag, trajectoriel, viol, genre="trajectoriel",
                             valeurs_differentes=c["valeurs_differentes"], discordances=c["discordances"])
                if genre != "rebrassage_agents":
                    for a in c["invariantes"]:
                        self.cellule("HE1.2", f"{tag}/{a}", egal, c["alarmes"][a], R, *self.p0(cfg, a), g, egalite=True)
                sens = c.get("lecture_par_agent")
                for a in ("agent_moyenne", "agent_comptage") if sens else ():
                    self.cellule("HE1.3", f"{tag}/{a}", CRITERES_SENS[sens], c["alarmes"][a], R, *self.p0(cfg, a), g)
            elif groupe == "temps":
                v = viol + c.get("viol_hors_synchro", 0) + c.get("viol_valeurs_hautes", 0) + \
                    c.get("viol_compte_pas", 0) + c.get("viol_borne_coelev", 0)
                self.cellule("HE2.1", tag, trajectoriel, v, genre="trajectoriel",
                             valeurs_differentes=c["valeurs_differentes"], discordances=c["discordances"],
                             **{k: c[k] for k in c if k.startswith("viol_")})
                if genre == "synchro":
                    for a in c["invariantes"]:
                        self.cellule("HE2.2", f"{tag}/{a}", egal, c["alarmes"][a], R, *self.p0(cfg, a), g, egalite=True)
                    self._bornes_synchro(c)
                    for a in c.get("lecture_au_dessus", []):
                        self.cellule("HE2.4", f"{tag}/{a}", au_dessus, c["alarmes"][a], R, *self.p0(cfg, a), g)
                    for a, sens in c.get("lecture_e", {}).items():
                        self.cellule("HE2.5", f"{tag}/{a}", CRITERES_SENS[sens], c["alarmes"][a], R, *self.p0(cfg, a), g)
            elif groupe == "tout":
                self.cellule("HE5.2", tag, trajectoriel, viol, genre="trajectoriel",
                             valeurs_differentes=c["valeurs_differentes"], discordances=c["discordances"])

    def _bornes_synchro(self, c):
        """HE2.3 : bornes inférieures exactes (r = 1) ; la co-élévation continue utilise le seuil du run."""
        if int(c["r"]) != 1:
            return
        cfg, K, T, m, R = c["cfg"], c["K"], c["T"], int(c["m"]), c["R"]
        s = self.seuils(cfg)
        tag = f"{cfg}/{c['nom']}"
        lb = cal.borne_synchro(K, T, m, self.q, s["coelev_comptage"])
        self.cellule("HE2.3", f"{tag}/coelev_comptage≥borne", au_moins_valeur, c["alarmes"]["coelev_comptage"], R, lb,
                     self.gamma, borne=lb)
        if m == K:
            cT = s["pas_moyenne"][0]
            lb_p = (1.0 - stats.norm.cdf(cT / math.sqrt(K)) ** T) ** K
            self.cellule("HE2.3", f"{tag}/pas_moyenne≥borne", au_moins_valeur, c["alarmes"]["pas_moyenne"], R, lb_p,
                         self.gamma, borne=lb_p)
            if "coelev_somme3" in c["alarmes"]:
                c3 = s["coelev_somme3"][0]
                p3 = 1.0 - stats.norm.cdf(c3 / S.M_COELEV) ** T
                lb_s = float(stats.binom.sf(S.M_COELEV - 1, K, p3))
                self.cellule("HE2.3", f"{tag}/coelev_somme3≥borne", au_moins_valeur, c["alarmes"]["coelev_somme3"], R,
                             lb_s, self.gamma, borne=lb_s)

    # --- classe M : HE4 (formes closes, cas sain, L4) ---
    def classe_M(self):
        g = self.gamma
        pred = {"concentre": "HE4.1", "synchro": "HE4.2", "temps": "HE4.3"}
        for c in self.r["M"]["cellules"]:
            cfg, R = c["cfg"], c["R"]
            K, T, B, m = c["K"], c["T"], float(c["B"]), int(c["m"])
            th = cal.puissances_decalage(cal.motif(c["genre"], K, T, B, m), self.q, self.alpha, self.seuils(cfg))
            for a in FORMES_CLOSES:
                if a in c["alarmes"]:
                    self.cellule(pred[c["genre"]], f"{cfg}/{c['nom']}/{a}", egal_valeur, c["alarmes"][a], R, th[a], g,
                                 forme_close=True, p=c["alarmes"][a] / R, p_th=th[a])
            if c["genre"] == "synchro":
                v = sum(1 for e in c["L4_ecart_max"].values() if e > c["L4_tolerance"]) + sum(c["L4_discordances"].values())
                self.cellule("HE4.4", f"{cfg}/{c['nom']}", trajectoriel, v, genre="trajectoriel",
                             ecart_max=c["L4_ecart_max"], discordances=c["L4_discordances"])

    # --- HE3 : validité séquentielle ---
    def HE3(self):
        g = self.gamma
        lec = self.g["HE3"]["lecture"]
        for c in self.r["HE3"]["cellules"]:
            cfg, nom, R, loi = c["cfg"], c["loi_nom"], c["R"], c["loi"]
            K, T = c["K"], c["T"]
            tag = f"{cfg}/{nom}"
            k = c["alarmes"]
            if loi["type"] == "iid":
                for a in ("e_coelev_ville", "e_pas_ville"):
                    self.cellule("HE3.1", f"{tag}/{a}", au_plus_valeur, k[a], R, self.alpha, g)
            elif loi["type"] == "equicorrelation":
                self.cellule("HE3.2", f"{tag}/e_coelev_ville", au_plus_valeur, k["e_coelev_ville"], R, self.alpha, g)
                self.cellule("HE3.3", f"{tag}/e_pas_ville>iid", au_dessus, k["e_pas_ville"], R,
                             *self.p0(cfg, "e_pas_ville"), g)
            elif loi["type"] == "effet_episode":
                for a in ("e_coelev_ville", "e_pas_ville"):
                    self.cellule("HE3.3", f"{tag}/{a}>iid", au_dessus, k[a], R, *self.p0(cfg, a), g)
            for a in lec["depasse"].get(nom, []):
                self.cellule("HE3.4", f"{tag}/{a}>α", au_dessus_valeur, k[a], R, self.alpha, g)
            conf = c["conforme"]
            bas, haut, taux = cal.region_conforme(conf["L"], conf["n_test"], conf["K"], self.alpha, g)
            for s, liste in conf["alarmes_par_tirage"].items():
                tot = int(sum(liste))
                n = conf["L"] * conf["n_test"]
                self.cellule("HE3.5", f"{tag}/{s}", region, tot, bas, haut, taux=tot / n, taux_theorique=taux)
            if loi["type"] != "iid":
                th = cal.fausses_alarmes_reference(loi, K, T, self.q, self.alpha, self.seuils(cfg))
                for a in FORMES_CLOSES:
                    if a in k and a in th:
                        self.cellule("HE3.6", f"{tag}/{a}", egal_valeur, k[a], R, th[a], g, forme_close=True,
                                     p=k[a] / R, p_th=th[a])

    # --- HE6 : synchronisation sous P₀ corrélée, seuils sur essaims entiers de la loi ---
    def HE6(self):
        g = self.gamma
        sens_par_loi = self.g["HE6"]["lecture"]
        for c in self.r["HE6"]["cellules"]:
            tag = f"{c['cfg']}/{c['loi_nom']}/{c['nom']}"
            v = sum(c["valeurs_differentes"].values()) + sum(c["discordances"].values()) + \
                sum(c[k] for k in c if k.startswith("viol_"))
            self.cellule("HE6.1", tag, trajectoriel, v, genre="trajectoriel",
                         valeurs_differentes=c["valeurs_differentes"], discordances=c["discordances"])
            for a in c["invariantes"]:
                self.cellule("HE6.2", f"{tag}/{a}", egal, c["alarmes"][a], c["R"], c["alarmes_p0"][a], c["R0"], g,
                             egalite=True)
            for a, sens in sens_par_loi.get(c["loi_nom"], {}).get(c["nom"], {}).items():
                self.cellule("HE6.3", f"{tag}/{a}", CRITERES_SENS[sens], c["alarmes"][a], c["R"], c["alarmes_p0"][a],
                             c["R0"], g, sens=sens)

    def audit_symetrie(self) -> dict:
        sortie = {"bornes": list(BORNES_AUDIT)}
        for nom, liste in (("formes_closes", self.z_formes), ("egalites", self.z_egalites)):
            z = np.array(liste)
            s2 = float(z.var(ddof=1)) if z.size > 1 else float("nan")
            sortie[nom] = {"n": int(z.size), "variance_z": s2, "moyenne_z": float(z.mean()) if z.size else float("nan"),
                           "hors_bornes": bool(z.size > 1 and not (BORNES_AUDIT[0] <= s2 <= BORNES_AUDIT[1]))}
        sortie["audit_declenche"] = sortie["formes_closes"]["hors_bornes"] or sortie["egalites"]["hors_bornes"]
        return sortie

    def lire(self) -> dict:
        if "C" in self.r:
            self.classe_C()
        if "M" in self.r:
            self.classe_M()
        if "HE3" in self.r:
            self.HE3()
        if "HE6" in self.r:
            self.HE6()
        sortie = {}
        for pred in sorted(self.predictions):
            cel = self.predictions[pred]["cellules"]
            sortie[pred] = {"verdict": verdict(cel), "n_cellules": len(cel),
                            "n_conformes": sum(x["etat"] == "conforme" for x in cel),
                            "n_contraires": sum(x["etat"] == "contraire" for x in cel),
                            "a_repliquer": [x["nom"] for x in cel if x["etat"] == "contraire" and x["genre"] == "statistique"],
                            "a_auditer": [x["nom"] for x in cel if x["etat"] == "contraire" and x["genre"] == "trajectoriel"],
                            "cellules": cel}
        return {"predictions": sortie, "audit_symetrie": self.audit_symetrie(), "gamma": self.gamma}


def lire(resultats: dict, grille: dict) -> dict:
    return Lecteur(resultats, grille).lire()


BLOCS_DE = {"HE1": ("C",), "HE2": ("C",), "HE5": ("C",), "HE4": ("M",), "HE3": ("HE3",), "HE6": ("HE6",)}

LIGNES_E = [
    {"enonce": "Théorème, axe des agents : contre un attaquant qui conserve le multi-ensemble des scores de chaque pas, "
               "toute statistique invariante par permutation des agents d'un pas a une puissance égale à son taux de "
               "fausse alarme",
     "lecture": ("Vérifié en simulation, sans exception dans le panneau : valeurs identiques au bit près, trajectoire par "
                 "trajectoire, et puissance égale au taux sous P₀ à l'intervalle exact près, pour la somme, le max, le "
                 "comptage, la moyenne par pas, la co-élévation (comptage et somme des 3 plus hauts), sa version "
                 "séquentielle en e-valeurs (processus cumulé et détecteur e) et le processus e lu aux frontières de pas. "
                 "La co-élévation n'y échappe pas : elle est fonction des multi-ensembles des pas."),
     "exiges": ["HE1.1", "HE1.2", "HE5.1"], "complementaires": ["HE1.3"]},
    {"enonce": "Dual, axe du temps : contre un attaquant qui conserve le multi-ensemble des scores de chaque agent, "
               "la surveillance par agent (max, moyenne, comptage dans le temps, puis max entre agents) a une puissance "
               "égale à son taux de fausse alarme",
     "lecture": ("Vérifié en simulation : valeurs identiques au bit près sous permutation du temps de chaque agent, "
                 "puissance égale au taux sous P₀ sous synchronisation ; la surveillance par agent est aveugle à une "
                 "menace qui ne change que le moment des actions de chaque agent."),
     "exiges": ["HE2.1", "HE2.2", "HE5.1"], "complementaires": []},
    {"enonce": "HE2 : la co-élévation a une puissance supérieure à son taux de fausse alarme quand la menace est "
               "concentrée dans le temps mais étalée entre agents d'un même pas",
     "lecture": ("Vrai, et voici sous quelle invariance : la co-élévation est invariante sous le groupe engendré par les "
                 "permutations des agents dans chaque pas et la relabellisation des pas (produit en couronne S_K ≀ S_T), "
                 "pas sous les permutations indépendantes du temps de chaque agent (G_T). Elle échappe donc au théorème "
                 "contre un attaquant de G_T (synchronisation : multi-ensemble de chaque agent conservé ; bornes exactes "
                 "atteintes, puissance au-dessus de son taux) ; elle n'y échappe pas contre un attaquant de G_A, ni contre "
                 "un rebrassage uniforme (T2)."),
     "exiges": ["HE1.1", "HE1.2", "HE2.1", "HE2.2", "HE2.3", "HE2.4"], "complementaires": ["HE5.1"]},
    {"enonce": "HE2, version séquentielle : l'e-valeur construite sur la co-élévation échappe-t-elle au théorème contre "
               "la synchronisation ?",
     "lecture": ("Non : sous synchronisation, le processus e cumulé et le détecteur e sur les comptes de co-élévation restent "
                 "au plus à leur taux sous P₀, et passent en dessous quand tous les agents se synchronisent. La "
                 "synchronisation conserve le total des comptes (fonction des multi-ensembles par agent) et le concentre "
                 "sur un pas ; Σ_t log(1 + λ(C_t − Kq)) est Schur-concave en (C_t), donc la concentration l'abaisse. "
                 "L'échappement de la co-élévation tient à sa lecture en maximum sur les pas, pas à la co-élévation "
                 "elle-même."),
     "exiges": ["HE2.5"], "complementaires": []},
    {"enonce": "Surveillance par agent contre statistique de niveau essaim : laquelle détecte quoi",
     "lecture": ("Aucune ne domine : la surveillance par agent détecte un routage des scores hauts vers un agent (G_A) et un "
                 "budget étalé dans le temps d'un agent ; la co-élévation et la moyenne par pas détectent la "
                 "synchronisation (G_T) et un budget étalé entre agents d'un même pas ; le max ne détecte que la menace "
                 "concentrée ; la somme détecte tout budget également, faiblement (L1) ; un relais tournant entre agents "
                 "sous multi-ensemble de pas conservé n'est vu par aucune (la surveillance par agent passe même sous son "
                 "taux)."),
     "exiges": ["HE1.2", "HE1.3", "HE2.4", "HE4.1", "HE4.2", "HE4.3"], "complementaires": ["HE2.3"]},
    {"enonce": "L4 : pour une règle fonction des seules sommes aux frontières de pas, la répartition du budget entre agents "
               "à un même pas est exactement invariante",
     "lecture": "Vérifié trajectoire par trajectoire (somme, moyenne par pas, processus e aux frontières de pas).",
     "exiges": ["HE4.4"], "complementaires": []},
    {"enonce": "HE3 : la version séquentielle garde le taux nominal sous effets d'épisode si calibrée sur essaims honnêtes "
               "entiers, et le dépasse sinon",
     "lecture": ("Calibrée sur essaims honnêtes entiers (conforme), elle tient le taux exact 1 − ⌈(K + 1)(1 − α)⌉/(K + 1) "
                 "sous toutes les lois de la grille. Au seuil de Ville, elle tient α sous la loi de référence ; sous effet "
                 "d'épisode, elle dépasse son taux bien spécifié. L'e-valeur linéaire sur les comptes de co-élévation reste "
                 "valide sous corrélation entre agents d'un même pas (copies à poids partagés), à la différence du processus "
                 "e sur les sommes ; les seuils calibrés sur cases supposées indépendantes s'écartent de α dans les deux "
                 "sens (formes closes)."),
     "exiges": ["HE3.1", "HE3.2", "HE3.3", "HE3.5", "HE3.6"], "complementaires": ["HE3.4"]},
    {"enonce": "HE6 : sous corrélation entre copies d'un même pas (poids partagés), la co-élévation calibrée sur essaims "
               "honnêtes entiers garde-t-elle sa puissance contre la synchronisation, et la surveillance par agent "
               "reste-t-elle aveugle ?",
     "lecture": ("Surveillance par agent : aveugle, même quand P₀ n'est pas invariante sous G_T (T1 est trajectoriel). "
                 "Co-élévation et moyenne par pas, calibrées sur essaims corrélés entiers : elles détectent encore la "
                 "synchronisation de tous les agents, mais une synchronisation de la moitié de l'essaim sous forte "
                 "corrélation les fait passer sous leur taux de fausse alarme — les maxima synchronisés sont arrachés au "
                 "pas où la corrélation les faisait co-élever naturellement. Le sens de la puissance de la co-élévation "
                 "dépend donc de la structure de corrélation honnête, pas seulement de l'invariance."),
     "exiges": ["HE6.1", "HE6.2", "HE6.3"], "complementaires": []},
]


def enonces_du_programme(lecture: dict) -> list[dict]:
    """Table E gelée : une lecture prononcée seulement si toutes ses prédictions exigées sont confirmées."""
    v = {k: x["verdict"] for k, x in lecture["predictions"].items()}
    sortie = []
    for ligne in LIGNES_E:
        etablie = all(v.get(k) == "confirmée" for k in ligne["exiges"])
        sortie.append({"enonce": ligne["enonce"],
                       "lecture": ligne["lecture"] if etablie else "non établi : voir " + ", ".join(ligne["exiges"]),
                       "exiges": ligne["exiges"], "complementaires": ligne["complementaires"],
                       "verdicts": {k: v.get(k, "absente") for k in ligne["exiges"] + ligne["complementaires"]}})
    return sortie
