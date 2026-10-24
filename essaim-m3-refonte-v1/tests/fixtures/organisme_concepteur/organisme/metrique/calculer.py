import json, os


def calculer(dossier_sorties):
    chemin = os.path.join(dossier_sorties, "reponses_test.json")
    if not os.path.exists(chemin):
        raise FileNotFoundError("reponses_test.json absent des sorties")
    rep = json.load(open(chemin, encoding="utf-8"))
    if not rep:
        return 0.0
    confs = [float(v.get("confiance", 0.0)) for v in rep.values() if isinstance(v, dict)]
    return sum(confs) / len(confs)
