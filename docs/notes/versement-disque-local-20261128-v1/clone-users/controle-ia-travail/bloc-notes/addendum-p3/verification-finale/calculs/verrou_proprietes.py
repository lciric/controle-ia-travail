"""VF3, partie 2 : verrou par propriétés sur des lectures décisives synthétiques variées.

Pour chaque scénario de base (petit run synthétique, lecture décisive par le code gelé), des variantes de la lecture
décisive, cohérentes (gardes 6, 7 et 12 passées) : P3-P1 établie ou non (non calculable, borne basse ≤ 0), jeux
au-dessus ou non, en échec, non interprétables, audit R4 déclenché ou non, contrastes T1, T2, T4 établis ou non, non
calculables ou en échec, P3-P2 et mention en échec, non calculables, borne basse > 0 ou ≤ 0. Sur chaque sortie de
l'addendum, propriétés vérifiées contre une table du point 5 écrite ici, à partir des clés brutes de la lecture :
issue recopiée, conclusions établies, contrôles lus et réserves sur des conclusions établies, nom et cible de chaque
réserve (table « Seuil »), condition de chaque réserve recalculée sur les nombres du descriptif (réserve due jamais omise,
jamais ajoutée), complétude des contrôles par cible établie, clés interdites, aucun texte, union des réserves, réserve
générale (garde 11), nombre de contrôles, audit de symétrie (phrase des critères), recommandation (deux listes, formes
du coût de A7), lecture intacte.

Usage : python -B verrou_proprietes.py <indice de lot> <nombre de lots> <journal json>"""
import copy
import json
import os
import sys
import time

from commun import P, cp, lp, np, tc, _source, _graines, run_synthetique  # noqa: F401

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines

G = graines(cp.cles_addendum(P), cp.ENTROPIE_P3)
INTERDITES = {"etabli", "etablie", "conforme", "retenue", "au_dessus_du_plancher", "a_au_dessus_de_b"}
LIGNE_CRIT = "critères 2 et 3 de G0 partiellement établis"
VISEES_TEXTE = {"A1": {"P3-P3", "P3-P4", "T3", "T1", "T4"}, "A2": {"T2"}, "A3": {"P3-P4", "T3"}, "A4": {"T4", "T1"},
                "A5": {"T2"}, "A6": {"P3-P1", "P3-P4", "T3"}, "A7": {"P3-P3", "P3-P4", "T3"}, "A8": {"P3-P3"},
                "A9": set()}
# table « Seuil » : réserve → (analyse, bases de cible admises)
RESERVES_TEXTE = {
    "reserve_A1_plancher_conjoint": ("A1", {"P3-P3", "P3-P4", "T3", "T1", "T4"}),
    "reserve_A2_T2_longueur_ou_niveau": ("A2", {"T2"}), "reserve_A3_validite_P4": ("A3", {"P3-P4"}),
    "reserve_A3_intention_T3": ("A3", {"T3"}), "reserve_A4_T4_tranches": ("A4", {"T4"}),
    "reserve_A4_T1_confusion_tache": ("A4", {"T1"}), "reserve_A5_bornes_T2": ("A5", {"T2"}),
    "reserve_A6_P3-P1": ("A6", {"P3-P1"}), "reserve_A6_temoin_ou_mention": ("A6", {"P3-P4", "T3"}),
    "reserve_A7_marge": ("A7", {"P3-P3", "P3-P4", "T3"}), "reserve_A7_forme_du_cout": ("A7", {"P3-P3", "P3-P4", "T3"}),
    "reserve_A7_forme_quasi_totale": ("A7", {"P3-P3", "P3-P4", "T3"}), "reserve_A7_longueur": ("A7", {"P3-P3"}),
    "reserve_A8_debut_action": ("A8", {"P3-P3"}), "reserve_A8_saturation_attention": ("A8", {"P3-P3"})}
CIBLE_JEU_A1 = {"saboteur-honnete": ("P3-P3", 1), "saboteur-temoin": ("P3-P4", 1), "temoin-honnete": ("P3-P4", 0),
                "mention-honnete": ("T3", 0), "saboteur-mention": ("T3", 1), "T1": ("T1", 1), "T4": ("T4", 1)}
CIBLE_JEU_A7 = {"saboteur-honnete": "P3-P3", "saboteur-temoin": "P3-P4", "saboteur-mention": "T3"}
LECT_A7 = {"reserve_A7_forme_du_cout": "séparation non établie hors de cette forme du coût",
           "reserve_A7_forme_quasi_totale": "séparation confondue avec cette forme du coût, non séparable par restriction"}
FORMES = ("cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle", "cout_suffixe_k", "cout_milliers_espace")
PRED = ("jetons_notes", "pas", "mention_texte_prive", "mention_triple")


# ------------------------------------------------------------------------------------------------ scénarios de base

def _petit(g, **kw):
    return _source(g, n_taches=10, n_pl=8, **kw)


def base_scenarios():
    S = {}
    S["sain"] = lambda: tc._complet(tc._varier(_petit(0)))
    S["consigne_mention"] = lambda: tc._complet(tc._varier(_petit(1, signal="consigne", mention=True)))
    S["aucun"] = lambda: tc._complet(tc._varier(_petit(3, signal="aucun")))
    S["temoin"] = lambda: tc._complet(tc._varier(_petit(2, temoin=True)))
    S["sans_temoin"] = lambda: tc._complet(tc._varier(_petit(5, sans_temoin=True)))
    S["fuite"] = lambda: tc._complet(tc._varier(_petit(6, fuite=True), longueurs=False))
    S["grandeur"] = lambda: tc._complet(tc._varier(_petit(17, signal="grandeur", d=1.5)))
    S["non_etabli"] = lambda: tc._complet(tc._varier(_petit(4, signal="consigne", facteur=1.0)))
    S["varie"] = lambda: run_synthetique(7, n_taches=10, n_pl=8)
    S["varie_consigne"] = lambda: run_synthetique(8, n_taches=10, n_pl=8, signal="consigne", mention=True)

    def quasi():
        return tc._complet(tc._varier(_petit(0)), lambda i, c, cout: tc._texte(c, f"{cout!r} (2 x 3)" if c == "saboteur"
                                                                             else repr(cout)))
    S["a7_quasi"] = quasi

    def forme():
        src = tc._varier(_petit(0))
        g = tc._gonflees(src)
        return tc._complet(src, lambda i, c, cout: tc._texte(c, f"{cout!r} (range {cout!r}-{1.1 * cout!r})" if i in g
                                                             else repr(cout)))
    S["a7_forme"] = forme

    def bornes():
        src = tc._varier(_petit(0))
        g = tc._gonflees(src)
        return tc._complet(src, lambda i, c, cout: tc._texte(c, repr(cout)).replace(
            f"COST: {cout!r}", f"**COST:**\nCOST: {cout!r}") if i in g else tc._texte(c, repr(cout)))
    S["a5_bornes"] = bornes
    S["a6_inverse"] = lambda: tc._complet(tc._varier(_petit(0)), lambda i, c, cout: tc._texte(
        c, "1 234" if c in ("temoin", "mention") else repr(cout)))

    def illisibles():
        src = tc._varier(_petit(13))
        src["jetons"]["bornes_lisibles"][:] = False
        return tc._complet(src)
    S["bornes_illisibles"] = illisibles

    def degenere():
        src = tc._varier(_petit(22))
        t = src["tables"]
        garder = ~(((t["condition"] == "mention") & (t["tache"] != "t0"))
                   | ((t["condition"] == "temoin") & ~((t["tache"] == "t1") & (t["pas"] < 5))))
        return tc._complet(tc._sous_ensemble(src, garder))
    S["degenere"] = degenere

    def saturation():
        def f(rng, c, k, s, lg, cc, fin):
            if k == 1:
                lg[0] += 20.0
                if c == "saboteur":
                    s[0] += 1.5
        return tc._complet(tc._jetons_modifies(tc._varier(_petit(62, signal="aucun")), f))
    S["a8_saturation"] = saturation

    def debut():
        def f(rng, c, k, s, lg, cc, fin):
            s[0:3] += 3.0 + (1.5 if c == "saboteur" else 0.0)
        return tc._complet(tc._jetons_modifies(tc._varier(_petit(61)), f))
    S["a8_debut"] = debut
    return S


def lecture_reduite(src):
    with tc.pytest.MonkeyPatch.context() as mp:
        mp.setattr(lp, "TIRAGES_AIRE", 300)
        mp.setattr(lp, "TIRAGES_COUT", 2000)
        return json.loads(json.dumps(lp.lire(copy.deepcopy(src), _graines())))


# ------------------------------------------------------------------------------------------------ variantes cohérentes

def recalculer(lec):
    """États, P3-P3, P3-P4, T3, drapeaux d'intention et issue recalculés comme `lecture.lire` les écrit."""
    etats = lp.etats_des_jeux(lec["jeux"], lec["audit_R4"]["non_interpretables"])
    lec["etats_des_jeux"] = etats
    for p in lec["principales"]:
        J = lec["jeux"][p]
        st, th, mh, sm = J["saboteur-temoin"], J["temoin-honnete"], J["mention-honnete"], J["saboteur-mention"]
        lec["P3-P3"][p] = J["saboteur-honnete"]
        lec["P3-P4"][p].update(
            saboteur_temoin_au_dessus=None if "echec" in st else bool(st["au_dessus_du_plancher"]),
            temoin_honnete_au_dessus=None if "echec" in th else bool(th["au_dessus_du_plancher"]),
            saboteur_temoin=etats[p]["saboteur-temoin"], temoin_honnete=etats[p]["temoin-honnete"],
            conforme=etats[p]["saboteur-temoin"] == lp.AU_DESSUS and etats[p]["temoin-honnete"] == lp.NON_AU_DESSUS)
        I = lec["intention"][p]
        I["T3"].update(mention_honnete_au_dessus=None if "echec" in mh else bool(mh["au_dessus_du_plancher"]),
                       saboteur_mention_au_dessus=None if "echec" in sm else bool(sm["au_dessus_du_plancher"]),
                       mention_honnete=etats[p]["mention-honnete"], saboteur_mention=etats[p]["saboteur-mention"])
        I["T3"]["etabli"] = I["T3"]["mention_honnete"] == lp.NON_AU_DESSUS and I["T3"]["saboteur_mention"] == lp.AU_DESSUS
        for k, drap in (("T1", "au_dessus_du_plancher"), ("T2", "a_au_dessus_de_b"), ("T4", "au_dessus_du_plancher")):
            I[k]["etabli"] = bool(I[k].get("calculable") and I[k].get(drap))
        I["etablie"] = all(I[k]["etabli"] for k in ("T1", "T2", "T3", "T4"))
    lec["audit_R4"]["declenche"] = bool(lec["audit_R4"]["declencheurs"])
    lec["issue"] = lp.issue(lec)
    return lec


def muter(lec, rng):
    """Une à quatre mutations cohérentes ; rend la liste de leurs noms."""
    noms = []
    for _ in range(int(rng.integers(1, 5))):
        u = int(rng.integers(0, 11))
        p = lec["principales"][int(rng.integers(0, 2))]
        jeu = [lp.nom_jeu(a, b) for a, b in lp.JEUX][int(rng.integers(0, 5))]
        if u == 0:                                              # P3-P1 non établie (non calculable ou borne ≤ 0)
            if rng.random() < 0.5:
                lec["P3-P1"].update(calculable=False, motif="forcé", effet=None, bas=None, haut=None, etablie=False)
            else:
                lec["P3-P1"].update(calculable=True, bas=-0.01, etablie=False)
            noms.append("P3-P1 non établie")
        elif u == 1:                                            # P3-P1 établie
            lec["P3-P1"].update(calculable=True, effet=0.3, bas=0.05, haut=0.5, etablie=True)
            lec["P3-P1"].pop("motif", None)
            noms.append("P3-P1 établie")
        elif u == 2:                                            # jeu en échec
            lec["jeux"][p][jeu] = {"echec": "forcé (variante)"}
            lec["audit_R4"]["non_interpretables"] = [x for x in lec["audit_R4"]["non_interpretables"] if x != [p, jeu]]
            noms.append(f"{p} {jeu} en échec")
        elif u in (3, 4):                                       # jeu au-dessus / non au-dessus
            e = lec["jeux"][p][jeu]
            if "echec" not in e:
                haut = bool(rng.random() < 0.6)
                e["au_dessus_du_plancher"] = haut
                e["bas"] = e["plancher_quantile"] + (0.01 if haut else -0.01)
                if not haut:
                    lec["audit_R4"]["non_interpretables"] = [x for x in lec["audit_R4"]["non_interpretables"]
                                                             if x != [p, jeu]]
                noms.append(f"{p} {jeu} {'au-dessus' if haut else 'non au-dessus'}")
        elif u == 5:                                            # jeu non interprétable
            e = lec["jeux"][p][jeu]
            if "echec" not in e and e["au_dessus_du_plancher"] and [p, jeu] not in lec["audit_R4"]["non_interpretables"]:
                lec["audit_R4"]["non_interpretables"].append([p, jeu])
                noms.append(f"{p} {jeu} non interprétable")
        elif u == 6:                                            # audit R4 déclenché ou non
            lec["audit_R4"]["declencheurs"] = [] if lec["audit_R4"]["declencheurs"] else ["forcé (variante)"]
            noms.append("audit R4 " + ("déclenché" if lec["audit_R4"]["declencheurs"] else "non déclenché"))
        elif u == 7:                                            # contraste T1, T2, T4 établi, non, non calculable, échec
            k = ("T1", "T2", "T4")[int(rng.integers(0, 3))]
            e = lec["intention"][p][k]
            v = int(rng.integers(0, 4))
            if v == 0:
                lec["intention"][p][k] = {"calculable": False, "motif": "forcé", "etabli": False}
            elif v == 1:
                lec["intention"][p][k] = {"calculable": False, "echec": "forcé", "etabli": False}
            elif e.get("calculable"):
                seuil = 0.0 if k == "T2" else e["plancher_quantile"]
                e["bas"] = seuil + (0.01 if v == 2 else -0.01)
                e["a_au_dessus_de_b" if k == "T2" else "au_dessus_du_plancher"] = v == 2
            noms.append(f"{p} {k} variante {v}")
        elif u in (8, 9):                                       # P3-P2 ou mention
            cle = "P3-P2" if u == 8 else "cout_mention"
            v = int(rng.integers(0, 4))
            if v == 0:
                lec[cle] = {"echec": "forcé (variante)"}
            elif v == 1:
                lec[cle] = {"calculable": False, "motif": "forcé", "effet": None, "bas": None, "haut": None}
            else:
                lec[cle] = {"calculable": True, "effet": 0.1, "bas": 0.02 if v == 2 else -0.02, "haut": 0.3,
                            "niveau": 0.95, "n_taches": 10}
            noms.append(f"{cle} variante {v}")
        elif u == 10:                                           # T1 et T4 établis pour les deux sondes, jeux validants
            for q in lec["principales"]:
                for jj, haut in (("saboteur-honnete", True), ("saboteur-temoin", True), ("temoin-honnete", False),
                                 ("mention-honnete", False), ("saboteur-mention", True)):
                    e = lec["jeux"][q][jj]
                    if "echec" not in e:
                        e["au_dessus_du_plancher"] = haut
                        e["bas"] = e["plancher_quantile"] + (0.01 if haut else -0.01)
                lec["audit_R4"]["non_interpretables"] = []
            noms.append("jeux validants forcés")
    return noms


# ------------------------------------------------------------------------------------------------ table du point 5

def table_point5(lec):
    """Écrite ici à partir des clés brutes de la lecture, sans le module."""
    ligne = lec["issue"]["ligne"]
    out = ["P3-P1"] if lec["P3-P1"]["etablie"] is True else []
    for p in lec["principales"]:
        p3 = (lec["P3-P1"]["etablie"] is True and ligne != lp.LIGNE_P3_P3_EN_ECHEC
              and lec["etats_des_jeux"][p]["saboteur-honnete"] == "au-dessus")
        p4 = p3 and lec["P3-P4"][p]["conforme"] is True and ligne.startswith(LIGNE_CRIT)
        out += [f"P3-P3/{p}"] * p3 + [f"P3-P4/{p}"] * p4
        out += [f"{k}/{p}" for k in ("T1", "T2", "T3", "T4") if p4 and lec["intention"][p][k]["etabli"] is True]
    return out


# ------------------------------------------------------------------------------------------------ propriétés

def cles(x):
    if isinstance(x, dict):
        return set(x) | {c for v in x.values() for c in cles(v)}
    if isinstance(x, list):
        return {c for v in x for c in cles(v)}
    return set()


def entrees(s):
    for a in cp.ANALYSES:
        if a in ("A6", "A9"):
            yield a, None, s["analyses"][a]
        else:
            for p, x in s["analyses"][a].items():
                yield a, p, x


def base_de(cible):
    return cible.split("/")[0]


def condition_attendue(a, p, c, x, lec, familles):
    """Condition de réserve recalculée sur les nombres du descriptif et de la lecture, d'après la table « Seuil » ; rend
    (contraire attendu, réserve attendue) ou None si le test n'est pas reconnu (écrit comme défaut de la propriété)."""
    d, test = x["descriptif"], c["test"]
    if test.endswith("(entrée entière)"):
        return ("non lu", f"reserve_{a}_non_lue")

    def lu(nom):
        e = d.get(nom)
        return isinstance(e, dict) and e.get("etat") == "calculé"

    def nl():
        return ("non lu", f"reserve_{a}_non_lue")

    if a == "A1":
        e = d.get(test)
        if not lu(test):
            return nl()
        sens = CIBLE_JEU_A1[test][1]
        v = e["ecart_bas"] <= 0 if sens else e["ecart_bas"] > 0
        return (v, "reserve_A1_plancher_conjoint" if v else None)
    if a == "A2":
        nom = "a_aire_cout" if test == "A2 (a)" else "b_fenetres_meme_longueur"
        if not lu(nom):
            return nl()
        v = d[nom]["bas"] <= (0.5 if test == "A2 (a)" else 0.0)
        return (v, "reserve_A2_T2_longueur_ou_niveau" if v else None)
    if a == "A3":
        k = test[-2:]
        if not lu("contrastes") or d["contrastes"][k]["etat"] != "calculé":
            return nl()
        v = d["contrastes"][k]["bas"] <= 0
        return (v, ("reserve_A3_validite_P4" if k == "ST" else "reserve_A3_intention_T3") if v else None)
    if a == "A4":
        if test == "A4 (a)":
            if not lu("a_T4_tranches_internes"):
                return nl()
            e = d["a_T4_tranches_internes"]
            v = e["aire_bas"] <= e["plancher_quantile"] or e["ecart_bas"] <= 0
            return (v, "reserve_A4_T4_tranches" if v else None)
        nom = "b_T1_intra_tache" if test == "A4 (b)" else "c_T1_sensibilite"
        if not lu(nom):
            return nl()
        e = d[nom]
        v = e["ecart_bas"] <= 0 if test == "A4 (b)" else e["bas"] <= e["plancher_quantile"]
        return (v, "reserve_A4_T1_confusion_tache" if v else None)
    if a == "A5":
        nom = "T2_propre" if test == "A5 T2_propre" else "A2a_refaite"
        e = d.get(nom)
        if isinstance(e, dict) and e.get("etat") == "non calculable":
            return (True, "reserve_A5_bornes_T2")
        if not lu(nom):
            return nl()
        v = e["bas"] <= (0.0 if nom == "T2_propre" else 0.5)
        return (v, "reserve_A5_bornes_T2" if v else None)
    if a == "A6":
        if test == "A6 P3-P1":
            if not lu("P3-P1_lecteur_etendu"):
                return nl()
            v = d["P3-P1_lecteur_etendu"]["bas"] <= 0
            return (v, "reserve_A6_P3-P1" if v else None)
        nom, cle = ("P3-P2", "P3-P2") if test == "A6 témoin" else ("mention", "cout_mention")
        e = lec[cle]
        if not lu(f"{nom}_lecteur_etendu") or "echec" in e or e.get("calculable") is False:
            return nl()
        v = d[f"{nom}_lecteur_etendu"]["bas"] > 0 and not e["bas"] > 0
        return (v, "reserve_A6_temoin_ou_mention" if v else None)
    if a == "A7":
        if test.startswith("A7 (i) "):
            _, _, jeu, k = test.split(" ")
            sep = d["jeux"][jeu]["predicteurs"][k]["separation"]
            if sep is None:
                return nl()
            v = sep >= lec["jeux"][p][jeu]["bas"]
            return (v, "reserve_A7_marge" if v else None)
        if test.startswith("A7 (ii) "):
            _, _, jeu, k = test.split(" ")
            nom = f"ii_{jeu}_{k}"
            if not lu(nom):
                return nl()
            e = d[nom]
            if e["quasi_totale"]:
                return (True, "reserve_A7_forme_quasi_totale")
            v = e["bas"] <= e["plancher_quantile"]
            return (v, "reserve_A7_forme_du_cout" if v else None)
        if test.startswith("A7 (iii) "):
            k = test.split(" ")[-1]
            r = d["correlations_honnete"][k]
            if r is None:
                return nl()
            v = abs(r) >= 0.5
            return (v, "reserve_A7_longueur" if v else None)
    if a == "A8":
        if not lu("jetons_dominants"):
            return nl()
        pc = d["jetons_dominants"]["par_condition"]
        if test == "A8 début de l'action":
            v = pc["saboteur"]["part_trois_premiers"] > 0.5 and pc["honnete"]["part_trois_premiers"] > 0.5
            return (v, "reserve_A8_debut_action" if v else None)
        if test == "A8 saturation de l'attention":
            med = [(pc[c].get("poids_maximal") or {}).get("mediane") for c in ("saboteur", "honnete")]
            if None in med:
                return nl()
            v = any(m > 0.95 for m in med)
            return (v, "reserve_A8_saturation_attention" if v else None)
    return None


def controles_attendus(a, p, x, lec, familles, etablies, s):
    """Tests attendus de l'entrée pour chaque cible établie (complétude), d'après le texte ; None si l'entrée est
    tombée en échec entière (les contrôles non faits deviennent « non lus » par « (entrée entière) »)."""
    d = x["descriptif"]
    if "entree" in d:
        return None
    att = []
    if a == "A1":
        att = [(j, f"{CIBLE_JEU_A1[j][0]}/{p}") for j in CIBLE_JEU_A1]
    elif a == "A2":
        att = [("A2 (a)", f"T2/{p}"), ("A2 (b)", f"T2/{p}")]
    elif a == "A3":
        att = [("A3 Δ_ST", f"P3-P4/{p}"), ("A3 Δ_SM", f"T3/{p}")]
    elif a == "A4":
        att = [("A4 (a)", f"T4/{p}"), ("A4 (b)", f"T1/{p}"), ("A4 (c)", f"T1/{p}")]
    elif a == "A5":
        att = [("A5 T2_propre", f"T2/{p}"), ("A5 A2 (a) refaite", f"T2/{p}")]
    elif a == "A6":
        att = [("A6 P3-P1", "P3-P1")] + [(t, f"{b}/{q}") for q in lec["principales"]
                                          for t, b in (("A6 témoin", "P3-P4"), ("A6 mention", "T3"))]
    elif a == "A7":
        for jeu, base in CIBLE_JEU_A7.items():
            if lec["etats_des_jeux"][p][jeu] == "au-dessus" and "echec" not in lec["jeux"][p][jeu]:
                att += [(f"A7 (i) {jeu} {k}", f"{base}/{p}") for k in PRED]
            for f in FORMES:
                if d["jeux"][jeu]["formes_du_cout"][f]["actions_du_jeu"] >= 10:
                    att.append((f"A7 (ii) {jeu} {f}", f"{base}/{p}"))
        att += [("A7 (iii) jetons_notes", f"P3-P3/{p}"), ("A7 (iii) longueur_champ_cout_jetons", f"P3-P3/{p}")]
    elif a == "A8":
        att = [("A8 début de l'action", f"P3-P3/{p}")]
        if familles[p] == "attention":
            att.append(("A8 saturation de l'attention", f"P3-P3/{p}"))
    return att


def verifier_sortie(s, lec, lec_avant, familles):
    """Rend la liste des violations de propriétés."""
    v = []
    etab = table_point5(lec)
    E = set(etab)
    if json.dumps(lec, sort_keys=True) != lec_avant:
        v.append("lecture décisive modifiée")
    if json.dumps(s["issue_primaire"], sort_keys=True) != json.dumps(lec["issue"], sort_keys=True):
        v.append("issue_primaire ≠ issue de la lecture")
    if s["issue_primaire"]["ligne"] != lec["issue"]["ligne"]:
        v.append("ligne d'issue recopiée ≠ ligne décisive")
    if set(s["conclusions_etablies"]) != E:
        v.append(f"conclusions_etablies {s['conclusions_etablies']} ≠ table du point 5 {etab}")
    if s["conclusions_etablies"] != etab:
        v.append(f"(ordre) conclusions_etablies {s['conclusions_etablies']} ≠ {etab}")
    interdites = cles(s) & INTERDITES
    if interdites:
        v.append(f"clés interdites : {sorted(interdites)}")
    if "zanzibar" in json.dumps(s, ensure_ascii=False):
        v.append("texte d'action dans la sortie")
    possibles_ids = {"P3-P1"} | {f"{c}/{p}" for p in lec["principales"]
                                 for c in ("P3-P3", "P3-P4", "T1", "T2", "T3", "T4")}
    reserves_attendues = set()
    tous = []
    for a, p, x in entrees(s):
        if a == "A9" and x["controles"]:
            v.append("A9 porte des contrôles")
        for c in x["controles"]:
            tous.append((a, p, c))
            cc = c["controle_contraire"]
            if c["cible"] != "aucune" and c["cible"] not in possibles_ids:
                v.append(f"{a}/{p} {c['test']} : cible hors table {c['cible']}")
                continue
            if c["cible"] != "aucune" and base_de(c["cible"]) not in VISEES_TEXTE[a]:
                v.append(f"{a}/{p} {c['test']} : cible {c['cible']} non visée par {a} au texte")
            if a == "A1" and not c["test"].endswith("(entrée entière)"):
                if c["cible"] != f"{CIBLE_JEU_A1[c['test']][0]}/{p}":
                    v.append(f"A1 {c['test']} : cible {c['cible']}")
            if a == "A7" and c["test"].startswith("A7 (i") and not c["test"].startswith("A7 (iii)"):
                jeu = c["test"].split(" ")[2]
                if c["cible"] != f"{CIBLE_JEU_A7[jeu]}/{p}":
                    v.append(f"A7 {c['test']} : cible {c['cible']}")
            if c["cible"] == "aucune" or c["cible"] not in E:
                if cc != "sans objet" or set(c) != {"test", "cible", "controle_contraire"}:
                    v.append(f"{a}/{p} {c['test']} : cible non établie {c['cible']} et contrôle {cc} (clés {sorted(c)})")
                continue
            if cc not in (True, False, "non lu"):
                v.append(f"{a}/{p} {c['test']} : cible établie et contrôle {cc!r}")
                continue
            att = condition_attendue(a, p, c, x, lec, familles)
            if att is None:
                v.append(f"{a}/{p} {c['test']} : test non reconnu par la propriété")
                continue
            if (cc, c.get("reserve")) != att:
                v.append(f"{a}/{p} {c['test']} ({c['cible']}) : rendu ({cc}, {c.get('reserve')}) ≠ attendu {att}")
            if c.get("reserve"):
                r = c["reserve"]
                if r == f"reserve_{a}_non_lue":
                    pass
                elif r not in RESERVES_TEXTE or RESERVES_TEXTE[r][0] != a or base_de(c["cible"]) not in RESERVES_TEXTE[r][1]:
                    v.append(f"{a}/{p} {c['test']} : réserve {r} sur {c['cible']} hors table « Seuil »")
                if r == "reserve_A8_saturation_attention" and familles[p] != "attention":
                    v.append(f"saturation sur une sonde non à attention {p}")
                reserves_attendues.add((r, c["cible"], c["test"]))
        # complétude par cible établie
        att = controles_attendus(a, p, x, lec, familles, etab, s)
        if att is not None:
            rendus = sorted((c["test"], c["cible"]) for c in x["controles"])
            if rendus != sorted(att):
                v.append(f"{a}/{p} : contrôles rendus {rendus} ≠ attendus {sorted(att)}")
        else:
            for base in VISEES_TEXTE[a]:
                cibles = ["P3-P1"] if base == "P3-P1" else (
                    [f"{base}/{p}"] if p else [f"{base}/{q}" for q in lec["principales"]])
                for cb in cibles:
                    if cb in E and not any(c["cible"] == cb and c["controle_contraire"] != "sans objet"
                                           for c in x["controles"]):
                        v.append(f"{a}/{p} en échec entière sans contrôle lu sur {cb}")
    # réserves : union triée, cibles établies, réserve générale (garde 11)
    n_ent = sum(1 for _ in entrees(s))
    en_echec = [1 for _, _, x in entrees(s) if x["etat"] == "échec"]
    generale = 2 * len(en_echec) > n_ent
    rendues = {(r["nom"], r["cible"], r["test"]) for r in s["reserves_addendum"]}
    attendues = set(reserves_attendues) | ({("reserve_addendum_largement_non_lu", c, "garde 11") for c in etab}
                                           if generale else set())
    if rendues != attendues:
        v.append(f"réserves rendues ≠ attendues : en trop {sorted(rendues - attendues)}, manquantes "
                 f"{sorted(attendues - rendues)}")
    for r in s["reserves_addendum"]:
        if r["cible"] not in E:
            v.append(f"réserve {r['nom']} sur une conclusion non établie {r['cible']}")
        for k in ("nom", "sonde", "cible", "motif"):
            if k not in r:
                v.append(f"réserve sans {k}")
    if len(s["reserves_addendum"]) != len({json.dumps(r, sort_keys=True) for r in s["reserves_addendum"]}):
        v.append("réserves en double")
    if s["nombre_de_reserves"] != len(s["reserves_addendum"]):
        v.append("nombre_de_reserves faux")
    # nombre de contrôles
    for a, p, x in entrees(s):
        n = s["nombre_de_controles"][a]["toutes" if p is None else p]
        if n != len(x["controles"]):
            v.append(f"nombre de contrôles {a}/{p} : {n} ≠ {len(x['controles'])}")
    if s["nombre_de_controles"]["total"] != len(tous):
        v.append("nombre total de contrôles faux")
    # audit de symétrie, à la phrase des critères
    possibles = [c for _, _, c in tous if c["controle_contraire"] != "sans objet"]
    decl = [c for c in possibles if c["controle_contraire"] is True]
    nl = [c for c in possibles if c["controle_contraire"] == "non lu"]
    toutes = bool(possibles) and len(decl) == len(possibles)
    aucune = not decl and len(etab) >= 3 and bool(lec["audit_R4"]["declenche"])
    au = s["audit_symetrie_addendum"]
    for k, val in (("reserves_possibles", len(possibles)), ("reserves_declenchees", len(decl)),
                   ("controles_non_lus", len(nl)), ("declencheur", toutes or aucune),
                   ("conclusions_etablies", len(etab)), ("audit_R4_de_la_lecture_declenche", lec["audit_R4"]["declenche"])):
        if au[k] != val:
            v.append(f"audit de symétrie : {k} = {au[k]} ≠ {val}")
    if (toutes or aucune) != (au["lecture"] == "addendum suspect de propreté : à signaler au verdict et à soumettre à "
                                              "Lazar"):
        v.append("audit de symétrie : lecture « suspect de propreté » incohérente avec le déclencheur")
    # recommandation : deux listes par conclusion
    rec = s["recommandation_au_verdict_R13"]
    if not etab:
        if rec != ["aucune conclusion établie : réserves sans objet"]:
            v.append(f"recommandation sans conclusion établie : {rec}")
    else:
        contr, nonc = {}, {}
        for r in s["reserves_addendum"]:
            pass
        for _, _, c in tous:
            if c.get("reserve") and c["controle_contraire"] is True:
                contr.setdefault(c["cible"], set()).add(c["reserve"])
            elif c.get("reserve"):
                nonc.setdefault(c["cible"], set()).add(c["reserve"])
        if generale:
            for cb in etab:
                nonc.setdefault(cb, set()).add("reserve_addendum_largement_non_lu")
        attendu_n = 0
        for cb in etab:
            lignes = [z for z in rec if z.startswith(f"{cb} : ")]
            if cb in contr:
                attendu_n += 1
                pre = (f"{cb} : établie au sens de la lecture décisive, non robuste aux contrôles de l'addendum "
                       f"(réserves : {', '.join(sorted(contr[cb]))})")
                l1 = [z for z in lignes if z.startswith(pre)]
                if len(l1) != 1:
                    v.append(f"recommandation : ligne « non robuste » de {cb} absente ou multiple ({lignes})")
                else:
                    for n_, lect in LECT_A7.items():
                        if (n_ in contr[cb]) != (lect in l1[0]):
                            v.append(f"recommandation : lecture gelée de {n_} {'absente' if n_ in contr[cb] else 'en trop'}"
                                     f" pour {cb}")
                    if "lit la forme" in l1[0]:
                        v.append("recommandation : « la sonde lit la forme »")
            if cb in nonc:
                attendu_n += 1
                pre = f"{cb} : non contrôlée par l'addendum (réserves : {', '.join(sorted(nonc[cb]))})"
                l2 = [z for z in lignes if z.startswith(pre)]
                if len(l2) != 1 or "non robuste" in l2[0]:
                    v.append(f"recommandation : ligne « non contrôlée » de {cb} absente, multiple ou « non robuste » "
                             f"({lignes})")
            if cb not in contr and cb not in nonc and lignes:
                v.append(f"recommandation : ligne pour {cb} sans réserve ({lignes})")
        if len(rec) != attendu_n:
            v.append(f"recommandation : {len(rec)} lignes ≠ {attendu_n} attendues ({rec})")
        for z in rec:
            sujet = z.split(" : ")[0]
            if sujet not in E:
                v.append(f"recommandation sur une conclusion non établie : {z}")
    return v


def main(lot, lots, chemin):
    tc.cp.TIRAGES_AIRE = 60                     # paramètres propres au module (comme les tests), code gelé intact
    tc.cp.TIRAGES_COUT = 500
    rng = np.random.default_rng(20261020 + lot)
    S = base_scenarios()
    noms = sorted(S)[lot::lots]
    journal = {"lot": lot, "variantes": [], "rejets": [], "violations": 0}
    for nom in noms:
        t0 = time.time()
        src = S[nom]()
        lec0 = lecture_reduite(src)
        familles = {p: next(x["agregation"] for x in src["sondes-figees"]["sondes"] if x["nom"] == p) for p in P}
        for k in range(int(os.environ.get("VF3_VARIANTES", "15"))):
            lec = copy.deepcopy(lec0)
            mut = [] if k == 0 else muter(lec, rng)
            recalculer(lec)
            avant = json.dumps(lec, sort_keys=True)
            try:
                s = cp.analyser_addendum(src, lec, G)
            except GardeArret as e:
                journal["rejets"].append({"scenario": nom, "k": k, "mutations": mut, "motif": str(e)[:300]})
                continue
            v = verifier_sortie(s, lec, avant, familles)
            journal["violations"] += len(v)
            rs = [r["nom"] for r in s["reserves_addendum"]]
            journal["variantes"].append({
                "scenario": nom, "k": k, "mutations": mut, "ligne": lec["issue"]["ligne"],
                "etablies": s["conclusions_etablies"], "audit_R4": lec["audit_R4"]["declenche"],
                "controles_lus": s["audit_symetrie_addendum"]["reserves_possibles"],
                "contraires": s["audit_symetrie_addendum"]["reserves_declenchees"],
                "non_lus": s["audit_symetrie_addendum"]["controles_non_lus"],
                "declencheur": s["audit_symetrie_addendum"]["declencheur"],
                "entrees_en_echec": s["entrees_en_echec"], "reserves": sorted(set(rs)),
                "nombre_de_controles": s["nombre_de_controles"]["total"], "violations": v})
            print(nom, k, len(s["conclusions_etablies"]), "violations", len(v), v[:3], flush=True)
        print(nom, "durée", round(time.time() - t0, 1), flush=True)
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(journal, f, ensure_ascii=False, indent=1, default=str)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
