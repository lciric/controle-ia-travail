"""Coût de calcul par carte (inférence universelle) — v1 : temps mural moyen d'une évaluation par méthode, un seul
processus, sur 20 mondes « interieur » et 20 mondes de découverte (λ = 0,40). Graines : SeedSequence(entropy=20261115301,
spawn_key=(i, r)). Usage : python essai_universelle_cout_v1.py SORTIE.json. Mise au point exploratoire."""
import hashlib, json, os, platform, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np  # noqa: E402
import banc_universelle_v1 as b  # noqa: E402

ENTROPIE = 20261115301


def main():
    sortie = sys.argv[1]
    if os.path.exists(sortie):
        raise SystemExit("sortie existante")
    temps = {}
    for i, cas in enumerate(("interieur", ("neuve", 0.40))):
        for r in range(20):
            s_monde, s_sous = np.random.SeedSequence(entropy=ENTROPIE, spawn_key=(i, r)).spawn(2)
            w = b.preparer(b.monde(cas, s_monde)); sous = b.sous_ensembles(s_sous)
            for m in b.METHODES:
                t0 = time.perf_counter()
                b.evaluer(w, sous, (m,))
                temps.setdefault(str(cas), {}).setdefault(m, []).append(time.perf_counter() - t0)
    doc = {"essai": "cout", "version": "v1", "graines": {"entropie": ENTROPIE, "spawn_key": "(i, r), i ∈ {0, 1}, r < 20"},
           "temps_moyen_s_par_carte": {c: {m: round(float(np.mean(v)), 4) for m, v in d.items()} for c, d in temps.items()},
           "note": "penalise_* et melange_a_priori comptent le calcul du v9 qu'ils réutilisent ; un seul processus, machine partagée",
           "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "empreintes_code": {f: hashlib.sha256(open(os.path.join(ICI, f), "rb").read()).hexdigest()
                               for f in ("banc_universelle_v1.py", os.path.basename(__file__))}}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(json.dumps(doc["temps_moyen_s_par_carte"], ensure_ascii=False))


if __name__ == "__main__":
    main()
