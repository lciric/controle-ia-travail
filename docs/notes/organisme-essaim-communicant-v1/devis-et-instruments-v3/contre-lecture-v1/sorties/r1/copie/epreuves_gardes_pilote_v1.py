#!/usr/bin/env python3
"""Épreuves (R5) des gardes du lanceur du pilote : pour chaque garde, un cas sain (la course va au bout, code 0) et au
moins un artefact qui doit la déclencher (code attendu, ligne d'arrêt au journal, dépense jamais au-delà du plafond).
Faux client local seulement ; aucun appel, aucun réseau. Graines : SeedSequence(20261124).spawn(…) (R9).

Usage : python -I -B epreuves_gardes_pilote_v1.py SORTIE.json DOSSIER_JOURNAUX_NEUF
Les mêmes cas sont rejoués par `test_gardes_pilote_essaim_v1.py` (pytest)."""
import json
import math
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import garde_pilote_essaim_v1 as GP  # noqa: E402
import lanceur_pilote_essaim_v1 as L  # noqa: E402

RACINE_GRAINES = 20261124


def prix_kimi():
    import calcul_devis_essaim_v3 as C3  # lit les pièces du dépôt à leur empreinte
    prix, src = C3.tarifs()
    return prix["kimi"], src["kimi"]


# --- fournisseurs d'entrée et faux clients ------------------------------------------------------------------------------------
def entree_taille(octets_par_role):
    return lambda appel: "x" * octets_par_role[appel["role"]]


ENTREE_ATTENDUE = {"proposeur": int((9000 + 3200) * 3.3), "message": int(3000 * 3.3)}   # section D attendu + surcroît supposé
ENTREE_AU_PLAFOND = dict(GP.PLAFOND_ENTREE_OCTETS)


class FauxClient:
    """Comportement réglable ; `defaut(appel, texte, max_tokens, k)` rend l'usage du k-ième appel effectif."""

    def __init__(self, rng=None, echecs=(), usage=None, exception_au=None):
        self.k = 0
        self.rng = rng
        self.echecs = set(echecs)       # indices de tentative qui échouent (ErreurFournisseur)
        self.tentative = 0
        self.usage = usage
        self.exception_au = exception_au

    def appeler(self, appel, texte, max_tokens):
        t = self.tentative
        self.tentative += 1
        if self.exception_au is not None and t == self.exception_au:
            raise ValueError("faute du client (artefact)")
        if t in self.echecs:
            raise L.ErreurFournisseur(f"délai dépassé (artefact, tentative {t})")
        k = self.k
        self.k += 1
        if self.usage is not None:
            u = self.usage(appel, texte, max_tokens, k)
        else:
            octets = len(texte.encode("utf-8"))
            s = int(self.rng.integers(3000, 12801)) if appel["role"] == "proposeur" else int(self.rng.integers(200, 401))
            u = {"entree": math.ceil(octets / 3.3), "sortie": min(s, max_tokens)}
        return {"usage": u, "texte": "", "fin": "stop"}


def au_plafond(appel, texte, max_tokens, k):
    return {"entree": GP.PLAFOND_ENTREE_JETONS[appel["role"]], "sortie": max_tokens}


def modifie_au(k0, champ, valeur, base=None):
    def f(appel, texte, max_tokens, k):
        u = (base or (lambda a, t, m, kk: {"entree": math.ceil(len(t.encode()) / 3.3), "sortie": min(6000, m)}))(appel, texte, max_tokens, k)
        if k == k0:
            u = dict(u)
            if valeur is None:
                u.pop(champ)
            else:
                u[champ] = valeur(appel, texte, max_tokens) if callable(valeur) else valeur
        return u
    return f


# --- cas ----------------------------------------------------------------------------------------------------------------------
def cas(prix):
    ss = np.random.SeedSequence(RACINE_GRAINES).spawn(8)
    P = GP.plan_pstd()
    borne = GP.borne_pire(P, prix)["pire_usd"]
    plan13 = list(P)
    i = max(k for k, a in enumerate(plan13) if a["monde"] == 0 and a["role"] == "message")
    plan13.insert(i + 1, {"id": "w00-a-g3-message-99", "monde": 0, "bras": "a", "generation": 3, "role": "message"})
    return [
        # nom, garde visée, plan, client, entrée, kwargs, code attendu
        ("sain : P-std entier, faux client réaliste", "toutes", P, lambda: FauxClient(np.random.default_rng(ss[0])), entree_taille(ENTREE_ATTENDUE), {}, 0),
        ("sain : tous les appels au plafond de jetons, aucune relance", "sortie, entrée, dépense", P, lambda: FauxClient(usage=au_plafond), entree_taille(ENTREE_AU_PLAFOND), {}, 0),
        ("sain : 74 relances (10 % de 744), course entière", "relances", P, lambda: FauxClient(np.random.default_rng(ss[1]), echecs=range(0, 148, 2)), entree_taille(ENTREE_ATTENDUE), {}, 0),
        ("artefact : max_tokens 24 001 demandé au proposeur", "sortie (avant)", P, lambda: FauxClient(np.random.default_rng(ss[2])), entree_taille(ENTREE_ATTENDUE), {"max_tokens_par_role": {"proposeur": 24001}}, 10),
        ("artefact : max_tokens 2 001 demandé au message", "sortie (avant)", P, lambda: FauxClient(np.random.default_rng(ss[2])), entree_taille(ENTREE_ATTENDUE), {"max_tokens_par_role": {"message": 2001}}, 10),
        ("artefact : sortie rendue 24 001 au 100e appel", "sortie (après)", P, lambda: FauxClient(usage=modifie_au(100, "sortie", 24001)), entree_taille(ENTREE_ATTENDUE), {}, 10),
        ("artefact : sortie rendue 2 001 sur le premier message", "sortie (après)", P, lambda: FauxClient(usage=modifie_au(8, "sortie", lambda a, t, m: m + 1)), entree_taille(ENTREE_ATTENDUE), {}, 10),
        ("artefact : entrée de 64 961 octets au proposeur", "entrée (avant)", P, lambda: FauxClient(np.random.default_rng(ss[3])), entree_taille({"proposeur": GP.PLAFOND_ENTREE_OCTETS["proposeur"] + 1, "message": 9900}), {}, 11),
        ("artefact : entrée rendue 23 201 jetons au 50e appel", "entrée (après)", P, lambda: FauxClient(usage=modifie_au(50, "entree", 23201)), entree_taille(ENTREE_AU_PLAFOND), {}, 11),
        ("artefact : 13e message dans le monde 0 (plan fautif)", "messages", plan13, lambda: FauxClient(np.random.default_rng(ss[4])), entree_taille(ENTREE_ATTENDUE), {}, 12),
        ("artefact : 75 relances", "relances", P, lambda: FauxClient(np.random.default_rng(ss[5]), echecs=range(0, 150, 2)), entree_taille(ENTREE_ATTENDUE), {}, 13),
        ("artefact : un appel qui échoue sans fin", "relances", P, lambda: FauxClient(np.random.default_rng(ss[5]), echecs=range(10, 10 ** 6)), entree_taille(ENTREE_ATTENDUE), {}, 13),
        ("artefact : plafond de dépense abaissé à 50 USD", "dépense", P, lambda: FauxClient(np.random.default_rng(ss[6])), entree_taille(ENTREE_ATTENDUE), {"plafond_depense": 50.0}, 14),
        ("sain : pire extrême (tout au plafond, 74 échecs comptés à la réserve dure) : dépense sous la borne", "dépense", P, lambda: FauxClient(usage=au_plafond, echecs=range(0, 148, 2)), entree_taille(ENTREE_AU_PLAFOND), {}, 0),
        ("artefact : usage sans champ « sortie »", "facturation hors borne", P, lambda: FauxClient(usage=modifie_au(7, "sortie", None)), entree_taille(ENTREE_ATTENDUE), {}, 16),
        ("artefact : entrée rendue 5 000 jetons pour 1 000 octets (H3)", "facturation hors borne", P, lambda: FauxClient(usage=modifie_au(3, "entree", 5000)), entree_taille({"proposeur": 1000, "message": 1000}), {}, 16),
        ("artefact : sortie rendue au-delà du max_tokens envoyé, sous le plafond", "facturation hors borne", P, lambda: FauxClient(usage=modifie_au(5, "sortie", lambda a, t, m: m + 1)), entree_taille(ENTREE_ATTENDUE), {"max_tokens_par_role": {"proposeur": 16000}}, 16),
        ("artefact : erreur inattendue du client", "erreur inattendue", P, lambda: FauxClient(np.random.default_rng(ss[7]), exception_au=20), entree_taille(ENTREE_ATTENDUE), {}, 17),
        ("artefact : aucun client injecté", "client", P, lambda: None, entree_taille(ENTREE_ATTENDUE), {}, 20),
    ], borne


def cas_plan_direct(prix):
    """Garde du plan, éprouvée directement (le lanceur suit le plan par construction)."""
    P = GP.plan_pstd()
    out = []
    g = GP.Garde(P, prix)
    g.avant(P[0], "x" * 100, 24000)
    g.apres(P[0], {"entree": 30, "sortie": 10})
    out.append(("sain : deuxième appel du plan accepté", P[1], g, 0))
    g2 = GP.Garde(P, prix)
    out.append(("artefact : appel hors plan (sauté)", P[5], g2, 15))
    g3 = GP.Garde(P, prix)
    g3.avant(P[0], "x" * 100, 24000)
    g3.apres(P[0], {"entree": 30, "sortie": 10})
    out.append(("artefact : premier appel rejoué sans échec", P[0], g3, 15))
    g4 = GP.Garde(P, prix)
    out.append(("artefact : identifiant inventé", {"id": "w00-a-g1-proposeur-99", "monde": 0, "bras": "a", "generation": 1, "role": "proposeur"}, g4, 15))
    res = []
    for nom, appel, garde, attendu in out:
        try:
            garde.avant(appel, "x" * 100, 24000)
            code = 0
        except GP.ArretCourse as ex:
            code = ex.code
        res.append({"cas": nom, "garde": "plan", "code_attendu": attendu, "code_rendu": code, "tenu": code == attendu})
    return res


def jouer(dossier, prix):
    os.makedirs(dossier, exist_ok=False)
    liste, borne = cas(prix)
    res = []
    for k, (nom, garde, plan, fab, entree, kw, attendu) in enumerate(liste):
        jr = os.path.join(dossier, f"journal-{k:02d}.jsonl")
        code, g = L.courir(plan, fab(), entree, jr, prix, **kw)
        lignes = [json.loads(x) for x in open(jr, encoding="utf-8")]
        derniere = lignes[-1]
        plafond = (g.plafond_depense if g else None)
        depense = (g.depense if g else 0.0)
        ligne_ok = (derniere["evenement"] == "fin" and code == 0) or (derniere["evenement"] == "arret" and derniere["code"] == code)
        res.append({"cas": nom, "garde": garde, "code_attendu": attendu, "code_rendu": code, "ligne_de_journal": derniere,
                    "journal": os.path.basename(jr), "depense_usd": round(depense, 6), "plafond_usd": plafond,
                    "depense_sous_plafond": plafond is None or depense <= plafond + 1e-9, "appels_joues": g.prochain if g else 0,
                    "relances": g.relances if g else 0,
                    "tenu": code == attendu and ligne_ok and (plafond is None or depense <= plafond + 1e-9)})
    res += cas_plan_direct(prix)
    return res, borne


def main(argv):
    if len(argv) != 3 or os.path.exists(argv[1]) or os.path.exists(argv[2]):
        print("usage : epreuves_gardes_pilote_v1.py SORTIE.json DOSSIER_JOURNAUX (neufs)", file=sys.stderr)
        return 2
    prix, src = prix_kimi()
    res, borne = jouer(argv[2], prix)
    out = {"version": "epreuves-gardes-pilote-v1", "prix_kimi_usd_par_million": list(prix), "source_prix": src,
           "graines": f"SeedSequence({RACINE_GRAINES}).spawn(8)", "numpy": np.__version__,
           "borne_pire_pstd": GP.borne_pire(GP.plan_pstd(), prix), "cas": res, "tenus": sum(r["tenu"] for r in res), "total": len(res)}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    for r in res:
        print("TENU  " if r["tenu"] else "CASSÉ ", r["code_attendu"], r["code_rendu"], r["cas"], r.get("depense_usd", ""))
    print(json.dumps(out["borne_pire_pstd"], ensure_ascii=False))
    return 0 if all(r["tenu"] for r in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
