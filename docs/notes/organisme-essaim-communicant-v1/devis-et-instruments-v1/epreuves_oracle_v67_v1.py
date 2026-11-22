#!/usr/bin/env python3
"""Épreuves (R5) de `oracle_toutes_cartes_v67_v1.py` : cas sain, artefacts vrai et faux par construction, invariance aux
verdicts, mutations qui lisent un verdict, source réelle. Aucun appel. Usage : python3 -I -B epreuves_oracle_v67_v1.py DOSSIER
(DOSSIER neuf : artefacts et sorties y sont écrits ; le résultat des épreuves dans DOSSIER/epreuves-oracle-v67-v1.json)."""
import copy
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import oracle_toutes_cartes_v67_v1 as O  # noqa: E402

sys.path.insert(0, O.OUTILS)
import monde_riche_outils_v1 as M  # noqa: E402
import puissance_monde_riche_v1 as P1  # noqa: E402


def journal(cartes):
    return {"releve": {"bras": "artefact", "cartes": cartes, "plantees": [{"nom": "V1", "loi": P1.S_V1, "promue": True}]},
            "journal": [{"evenement": "generation", "depense": 1.0}]}


def cartes_base(verdicts):
    lois = [("G1-a-01", 1, "a", P1.S_V1),                                 # vraie par construction : la loi du monde
            ("G1-a-02", 1, "a", M.fausses_couvertes(P1.K1_SV1)["F1-copie"]),  # fausse par construction : copie de K1
            ("G1-b-01", 1, "b", M.fausses_couvertes(P1.K1_SV1)["F2-melee-uniforme"]),  # fausse : K1 mêlée à l'uniforme
            ("G2-a-01", 2, "a", {"type": "inconnu", "x": 1}),               # malformée : rien
            ("G2-b-01", 2, "b", {"type": "melange", "composantes": [P1.S_V1, {"type": "fixe", "probas": [1, 1, 1]}],
                                 "poids": [0.9, 0.1]})]                     # vraie : le monde à peine dilué
    out = []
    for (i, g, p, loi), (pr, ve) in zip(lois, verdicts):
        out.append({"identifiant": i, "generation": g, "proposeur": p, "loi": copy.deepcopy(loi),
                    "promue": pr, "retenue": pr, "verdict": ve, "gardien": "CANARI-VERDICT-7f3a"})
    return out


def lancer(argv):
    try:
        return O.main(["x"] + argv)
    except SystemExit as ex:
        return ex.code


def lire_cartes(chemin):
    d = json.load(open(chemin, encoding="utf-8"))
    return d["cartes"], d["comptes"]


def main(argv):
    dossier = argv[1]
    os.makedirs(dossier, exist_ok=False)
    res = []

    def ecrire(nom, obj):
        p = os.path.join(dossier, nom)
        with open(p, "x", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
        return p

    v1 = [(True, "survit"), (False, None), (True, "éliminée"), (False, None), (False, None)]
    v2 = [(False, None), (True, "survit"), (False, "survit"), (True, "éliminée"), (True, "survit")]  # verdicts permutés
    a1 = ecrire("artefact-a1.json", journal(cartes_base(v1)))
    a2 = ecrire("artefact-a2-verdicts-permutes.json", journal(cartes_base(v2)))
    sans = journal([{k: v for k, v in c.items() if k in O.LISTE_BLANCHE} for c in cartes_base(v1)])
    a3 = ecrire("artefact-a3-sans-verdicts.json", sans)

    s1 = os.path.join(dossier, "sortie-a1.json")
    code = lancer(["--essai", a1, s1])
    cartes, comptes = lire_cartes(s1)
    classes = {c["identifiant"]: c["classe"] for c in cartes}
    attendu = {"G1-a-01": "vraie", "G1-a-02": "fausse", "G1-b-01": "fausse", "G2-a-01": "rien", "G2-b-01": "vraie"}
    res.append({"epreuve": "artefacts vrai, faux et malformé par construction", "attendu": attendu,
                "rendu": classes, "code": code, "tenue": code == 0 and classes == attendu, "fichier": s1})
    canari = "CANARI-VERDICT-7f3a" in open(s1, encoding="utf-8").read()
    res.append({"epreuve": "canari du champ de verdict absent de la sortie", "attendu": False, "rendu": canari,
                "tenue": not canari, "fichier": s1})

    s2, s3 = os.path.join(dossier, "sortie-a2.json"), os.path.join(dossier, "sortie-a3.json")
    c2, c3 = lancer(["--essai", a2, s2]), lancer(["--essai", a3, s3])
    k2, _ = lire_cartes(s2)
    k3, _ = lire_cartes(s3)
    res.append({"epreuve": "invariance : verdicts permutés puis supprimés", "attendu": "cartes identiques à a1",
                "rendu": {"permutes_identiques": k2 == cartes, "supprimes_identiques": k3 == cartes},
                "code": [c2, c3], "tenue": c2 == 0 and c3 == 0 and k2 == cartes and k3 == cartes, "fichier": [s2, s3]})

    garde = O.LISTE_BLANCHE
    O.LISTE_BLANCHE = garde + ("promue",)
    sm = os.path.join(dossier, "sortie-mutation-liste-blanche.json")
    cm = lancer(["--essai", a1, sm])
    O.LISTE_BLANCHE = garde
    res.append({"epreuve": "mutation : la liste blanche lit « promue »", "attendu": "refus code 3, aucune sortie",
                "rendu": {"code": cm, "sortie_ecrite": os.path.exists(sm)}, "tenue": cm == 3 and not os.path.exists(sm)})

    O.LISTE_BLANCHE = garde + ("verdict",)
    sm2 = os.path.join(dossier, "sortie-mutation-verdict.json")
    cm2 = lancer(["--essai", a1, sm2])
    O.LISTE_BLANCHE = garde
    res.append({"epreuve": "mutation : la liste blanche lit « verdict »", "attendu": "refus code 3, aucune sortie",
                "rendu": {"code": cm2, "sortie_ecrite": os.path.exists(sm2)}, "tenue": cm2 == 3 and not os.path.exists(sm2)})

    cachee = cartes_base(v1)
    cachee[0]["loi"] = {"type": "transformee", "base": P1.S_V1, "puissance": 1.0, "log_w_max": 9.9}
    a4 = ecrire("artefact-a4-score-cache-dans-la-loi.json", journal(cachee))
    sm3 = os.path.join(dossier, "sortie-a4.json")
    cm3 = lancer(["--essai", a4, sm3])
    res.append({"epreuve": "score du juge caché dans un arbre de loi", "attendu": "refus code 3, aucune sortie",
                "rendu": {"code": cm3, "sortie_ecrite": os.path.exists(sm3)}, "tenue": cm3 == 3 and not os.path.exists(sm3)})

    sr = os.path.join(dossier, "sortie-source-reelle.json")
    cr = lancer([O.CHEMIN_SOURCE_CITE, sr])
    res.append({"epreuve": "source réelle au chemin cité par l'analyse", "attendu": "calcul si présente à l'empreinte 21bc75f4…",
                "rendu": {"code": cr, "sortie_ecrite": os.path.exists(sr), "present_sur_disque": os.path.isfile(O.CHEMIN_SOURCE_CITE)},
                "tenue": None, "fichier": sr if os.path.exists(sr) else None})

    sf = os.path.join(dossier, "sortie-empreinte-fausse.json")
    cf = lancer([a1, sf])
    res.append({"epreuve": "artefact présenté comme source réelle (empreinte fausse)", "attendu": "refus code 2, aucune sortie",
                "rendu": {"code": cf, "sortie_ecrite": os.path.exists(sf)}, "tenue": cf == 2 and not os.path.exists(sf)})

    with open(os.path.join(dossier, "epreuves-oracle-v67-v1.json"), "x", encoding="utf-8") as f:
        json.dump({"epreuves": res, "comptes_a1": comptes}, f, ensure_ascii=False, indent=1)
    for r in res:
        print(r["tenue"], r["epreuve"], json.dumps(r["rendu"], ensure_ascii=False))
    return 0 if all(r["tenue"] in (True, None) for r in res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
