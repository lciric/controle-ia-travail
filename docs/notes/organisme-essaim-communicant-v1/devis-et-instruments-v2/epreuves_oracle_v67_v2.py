#!/usr/bin/env python3
"""Épreuves de l'oracle v2 : (1) les épreuves de la v1 rejouées sur la v2 ; (2) épreuve neuve : champ de verdict de nom
non listé (`promu`, `rang`, `log_w`) glissé dans l'arbre d'une loi, jouée sur la v1 (pour dire ce qui se passe) et sur la v2.
Aucun appel. Usage : python3 -I -B epreuves_oracle_v67_v2.py DOSSIER_NEUF"""
import copy
import importlib.util
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.join(os.path.dirname(ICI), "essaim-devis-instruments-v1")


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


O1 = charger("oracle_v1", os.path.join(V1, "oracle_toutes_cartes_v67_v1.py"))
O2 = charger("oracle_v2", os.path.join(ICI, "oracle_toutes_cartes_v67_v2.py"))
sys.path.insert(0, O2.OUTILS)
import monde_riche_outils_v1 as M  # noqa: E402
import puissance_monde_riche_v1 as P1  # noqa: E402


def journal(cartes):
    return {"releve": {"bras": "artefact", "cartes": cartes}}


def cartes_base(verdicts):
    lois = [("G1-a-01", 1, "a", P1.S_V1), ("G1-a-02", 1, "a", M.fausses_couvertes(P1.K1_SV1)["F1-copie"]),
            ("G1-b-01", 1, "b", M.fausses_couvertes(P1.K1_SV1)["F2-melee-uniforme"]), ("G2-a-01", 2, "a", {"type": "inconnu", "x": 1}),
            ("G2-b-01", 2, "b", {"type": "melange", "composantes": [P1.S_V1, {"type": "fixe", "probas": [1, 1, 1]}], "poids": [0.9, 0.1]}),
            ("G2-b-02", 2, "b", M.fausses_couvertes(P1.K1_SV1)["F4-temperee-inclinee"])]
    return [{"identifiant": i, "generation": g, "proposeur": p, "loi": copy.deepcopy(loi), "promue": pr, "verdict": ve, "gardien": "CANARI-VERDICT-7f3a"}
            for (i, g, p, loi), (pr, ve) in zip(lois, verdicts)]


def lancer(O, argv):
    try:
        return O.main(["x"] + argv)
    except SystemExit as ex:
        return ex.code


def main(argv):
    d = argv[1]
    os.makedirs(d, exist_ok=False)
    res = []

    def ecrire(nom, obj):
        p = os.path.join(d, nom)
        with open(p, "x", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
        return p

    v1 = [(True, "survit"), (False, None), (True, "éliminée"), (False, None), (False, None), (True, "survit")]
    v2 = [(False, None), (True, "survit"), (False, "survit"), (True, "éliminée"), (True, "survit"), (False, None)]
    a1, a2 = ecrire("a1.json", journal(cartes_base(v1))), ecrire("a2-permutes.json", journal(cartes_base(v2)))
    s1, s2 = os.path.join(d, "v2-sortie-a1.json"), os.path.join(d, "v2-sortie-a2.json")
    c1, c2 = lancer(O2, ["--essai", a1, s1]), lancer(O2, ["--essai", a2, s2])
    k1 = json.load(open(s1))["cartes"]
    k2 = json.load(open(s2))["cartes"]
    cl = {c["identifiant"]: c["classe"] for c in k1}
    att = {"G1-a-01": "vraie", "G1-a-02": "fausse", "G1-b-01": "fausse", "G2-a-01": "rien", "G2-b-01": "vraie", "G2-b-02": "fausse"}
    res.append({"epreuve": "v2 : vrai, faux (dont transformée inclinée), malformé par construction", "attendu": att, "rendu": cl, "tenue": c1 == 0 and cl == att})
    res.append({"epreuve": "v2 : invariance aux verdicts permutés", "attendu": True, "rendu": k1 == k2, "tenue": c2 == 0 and k1 == k2})
    res.append({"epreuve": "v2 : canari absent de la sortie", "attendu": False, "rendu": "CANARI" in open(s1).read(), "tenue": "CANARI" not in open(s1).read()})
    garde = O2.LISTE_BLANCHE
    O2.LISTE_BLANCHE = garde + ("promue",)
    sm = os.path.join(d, "v2-mutation.json")
    cm = lancer(O2, ["--essai", a1, sm])
    O2.LISTE_BLANCHE = garde
    res.append({"epreuve": "v2 : mutation de la liste blanche (promue)", "attendu": 3, "rendu": cm, "tenue": cm == 3 and not os.path.exists(sm)})
    for nom_champ, ou in (("promu", "racine"), ("rang", "si_sinon"), ("log_w", "softmax_feuille"), ("log_w_max", "racine")):
        cartes = cartes_base(v1)
        if ou == "racine":
            cartes[0]["loi"] = dict(P1.S_V1, **{nom_champ: 1})
        elif ou == "si_sinon":
            cartes[0]["loi"] = {"type": "si_sinon", "condition": {"indice": 0, "seuil": 0.0}, "si": P1.S_V1, "sinon": P1.K1_SV1, nom_champ: 1}
        else:
            cartes[0]["loi"] = {"type": "melange", "composantes": [dict(P1.S_V1, **{nom_champ: 7.5}), P1.K1_SV1], "poids": [0.5, 0.5]}
        a = ecrire(f"a5-{nom_champ}-{ou}.json", journal(cartes))
        sv1, sv2 = os.path.join(d, f"v1-sortie-a5-{nom_champ}-{ou}.json"), os.path.join(d, f"v2-sortie-a5-{nom_champ}-{ou}.json")
        r1, r2 = lancer(O1, ["--essai", a, sv1]), lancer(O2, ["--essai", a, sv2])
        listee = nom_champ in O1.LISTE_NOIRE
        res.append({"epreuve": f"champ « {nom_champ} » glissé dans l'arbre ({ou}), sur la v1", "attendu": "refus 3 si listé, sinon constaté",
                    "rendu": {"code": r1, "sortie_ecrite": os.path.exists(sv1), "nom_dans_la_liste_noire_v1": listee},
                    "tenue": (r1 == 3) if listee else None, "constat": None if listee else ("le champ PASSE la v1" if r1 == 0 else "refusé")})
        res.append({"epreuve": f"champ « {nom_champ} » glissé dans l'arbre ({ou}), sur la v2", "attendu": "refus 3, aucune sortie",
                    "rendu": {"code": r2, "sortie_ecrite": os.path.exists(sv2)}, "tenue": r2 == 3 and not os.path.exists(sv2)})
    sr = os.path.join(d, "v2-source-reelle.json")
    cr = lancer(O2, [O2.CHEMIN_SOURCE_CITE, sr])
    res.append({"epreuve": "v2 : source réelle au chemin cité", "attendu": "calcul si présente", "rendu": {"code": cr, "present": os.path.isfile(O2.CHEMIN_SOURCE_CITE)}, "tenue": None})
    with open(os.path.join(d, "epreuves-oracle-v67-v2.json"), "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    for r in res:
        print(r["tenue"], r["epreuve"], json.dumps(r["rendu"], ensure_ascii=False), r.get("constat") or "")
    return 0 if all(r["tenue"] in (True, None) for r in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
