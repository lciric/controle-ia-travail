"""Mesure des durées unitaires du calcul du banc complet MR-2 (pièce d'appui du devis v4 du banc), sur la graine de
développement **publique** r = 0 de la conception v4 (`cle("monde-mr1-v4-calibration-developpement", 0)`).

Aucun monde de calibration ni de course, aucun secret, aucun appel de modèle, aucun réseau, aucune machine louée. Importe
`outils-v4/monde_riche_v4.py` (scellé, `4b165847…`) sans le modifier ; ne mesure que des durées (horloge murale, un
processus), jamais une issue qui décide. Le juge mesuré est le **juge simplifié** de la conception (outils v1) : le juge de la
course n'est pas écrit ; ses durées se mesurent à l'essai à blanc du lanceur du banc (garde de durée du devis v4).

Usage : `ulimit -v 6000000; OMP_NUM_THREADS=2 python3 -I -B mesure-durees-banc-mr2-v1.py SORTIE.json` (refuse d'écraser).
"""
import datetime
import hashlib
import json
import os
import platform
import statistics
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(ICI), "outils-v4"))
import numpy as np  # noqa: E402

import monde_riche_v4 as R4  # noqa: E402  (installe la sorte interaction_xor dans les outils v1, comme en v4)

M, M2, P1 = R4.M, R4.M2, R4.P1
RANG = 0
REPETITIONS = 3


def chrono(f, *a, **k):
    t0 = time.perf_counter()
    r = f(*a, **k)
    return r, round(time.perf_counter() - t0, 3)


def main(sortie):
    if os.path.exists(sortie):
        sys.exit("refus : sortie existante")
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    charge_debut = os.getloadavg()
    out = {"graine_publique": "cle('monde-mr1-v4-calibration-developpement', 0)", "tirages": []}

    # 1. Tirages et vérification (C0 à C8 v4), comme `generer_v4`, durée de chaque pas
    graine = P1.cle("monde-mr1-v4-calibration-developpement", RANG)
    spec = None
    for k in range(8):
        sous = int(np.random.SeedSequence(graine, spawn_key=(k,)).generate_state(1, dtype=np.uint64)[0])
        s, d_gen = chrono(R4.generer_monde_v4, sous)
        r, d_ver = chrono(R4.verifier_v4, s)
        out["tirages"].append({"tirage": k, "generation_s": d_gen, "verification_s": d_ver,
                               "conforme": r["conforme"], "refus": (r.get("refus") or {}).get("controle"),
                               "composantes": len(s["effets"])})
        if r["conforme"]:
            spec = s
            break
    if spec is None:
        sys.exit("aucun tirage conforme : mesure impossible")
    D, nsp = spec["dimension"], spec["sous_populations"]
    loi = M.compiler_monde(spec)

    # 2. Oracle (12 000 instances), K1
    o, out["oracle_12000_s"] = chrono(M.Oracle, loi, D, nsp, n=12000, graine=P1.cle("oracle-v4", RANG))
    (k1, eid_k1, infos), out["k1_et_informations_s"] = chrono(M.k1_du_monde, spec, o)
    ids = [e["id"] for e in spec["effets"]]

    # 3. Lois synthétiques (cartes bruitées, modèle de proposeurs de la conception), archives de 1, 8 et 17 lois
    rng = P1.rng_de("mesure-durees-banc-mr2-v1", RANG)

    def carte():
        S = sorted(set(rng.choice(ids, size=int(rng.integers(2, len(ids) + 1)), replace=False).tolist()))
        return P1._bruiter(spec, S, 0.15, rng)

    archive17 = [k1] + [carte() for _ in range(16)]
    jugee = P1._bruiter(spec, ids, 0.15, rng)
    jugements = {}
    for n in (200, 400, 800):
        for kk in (1, 8, 17):
            ds = []
            for rep in range(REPETITIONS):
                _, d = chrono(M.juger, jugee, archive17[:kk], loi, D, nsp,
                              P1.rng_de("mesure-durees-banc-mr2-v1-juge", RANG, n, kk, rep), n=n)
                ds.append(d)
            jugements[f"n={n}|archive={kk}"] = {"durees_s": ds, "mediane_s": round(statistics.median(ds), 3)}
    out["jugement_juge_simplifie"] = jugements

    # 4. Pièces de l'oracle : attribution d'une loi, enveloppe d'une archive
    _, out["attribution_une_loi_s"] = chrono(o.attribution, jugee, spec)
    _, out["enveloppe_archive_8_s"] = chrono(o.gain_enveloppe, archive17[:8])
    _, out["enveloppe_archive_17_s"] = chrono(o.gain_enveloppe, archive17)

    # 5. Regroupement de 24 cartes sur 1 500 et 2 000 instances publiques
    cartes = [carte() for _ in range(24)]
    for ninst in (1500, 2000):
        Zr, Gr = M.tirer_instances(P1.rng_de("mesure-durees-banc-mr2-v1-ref", RANG, ninst), ninst, D, nsp)
        _, out[f"regroupement_24_cartes_{ninst}_instances_s"] = chrono(M2.grouper_v2, cartes, Zr, Gr, nsp)

    # 6. Générations simulées complètes (code v4 inchangé, n = 400, masquage vrai) : une, puis trois
    _, out["course_1_generation_n400_s"] = chrono(R4.course, spec, RANG, 1, True)
    _, out["course_3_generations_n400_s"] = chrono(R4.course, spec, RANG, 3, True)
    _, out["course_1_generation_n800_s"] = chrono(R4.course, spec, RANG, 1, True, n=800)

    fin = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    res = {"version": "mesure-durees-banc-mr2-v1", "debut_utc": debut, "fin_utc": fin,
           "charge_moyenne_debut": [round(x, 2) for x in charge_debut],
           "charge_moyenne_fin": [round(x, 2) for x in os.getloadavg()],
           "processeurs_visibles": os.cpu_count(), "omp_num_threads": os.environ.get("OMP_NUM_THREADS"),
           "versions": {"python": platform.python_version(), "numpy": np.__version__},
           "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "monde_riche_v4_sha256": hashlib.sha256(open(R4.__file__, "rb").read()).hexdigest(),
           "mesures": out}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(res, ensure_ascii=False)[:3000])


if __name__ == "__main__":
    main(sys.argv[1])
