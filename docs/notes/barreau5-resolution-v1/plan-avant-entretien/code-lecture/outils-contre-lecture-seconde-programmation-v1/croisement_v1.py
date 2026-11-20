"""Croisement des deux programmes du barreau 5 sur des entrées fabriquées (contre-lecture de la seconde programmation).

Outil du contre-lecteur. Aucune donnée : les différences d_k, la séparation apprise et l'échec de la sonde décisive sont
tirées à lois inventées. Pour chaque monde fabriqué :
1. le premier programme (`lecture_v1`) calcule les épreuves (`epreuve`), l'issue (`issue`), les rapportés et les phrases,
   et le résultat est assemblé comme le fait `lecture_v1.lire` (bloc `g_issue`, lignes 1301 à 1306 de `d877d2de…`), puis
   passé par `_convertible` et un aller-retour JSON à clés triées, comme `ouvrir` l'écrit ;
2. la seconde programmation (`seconde_programmation_v2.comparer`) le compare, code de sortie 0.
On compte les accords exacts et les désaccords par champ et par forme. Ni score, ni activation, ni fichier de données.

Graines : `numpy.random.SeedSequence(ENTROPIE)`, un enfant par monde (`spawn`). L'entropie est écrite au journal.

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python -B <ce fichier> <journal .json> [--premier CHEMIN] [--second CHEMIN] [--mondes N]
`--premier` et `--second` désignent des copies corrigées (par `appliquer_couples_v1.py`) ; sans eux, les modules du
paquet sont importés.
"""
from __future__ import annotations

import collections
import hashlib
import importlib
import importlib.util
import json
import os
import sys

import numpy as np

ENTROPIE = 0x5F2C_0D1E_B5F0_2026_1120_C0A7_7E11_5EC0
MONDES = 20_000


def charger(nom_module: str, chemin: str | None, nom_copie: str):
    if chemin is None:
        return importlib.import_module(nom_module), None
    importlib.import_module("controle_ia.barreau5_familles")
    spec = importlib.util.spec_from_file_location(nom_copie, chemin)
    module = importlib.util.module_from_spec(spec)
    sys.modules[nom_copie] = module
    spec.loader.exec_module(module)
    with open(chemin, "rb") as f:
        return module, hashlib.sha256(f.read()).hexdigest()


def tirer_differences(rng, k: int, familles: list[str]) -> dict:
    """k différences sur les k premières familles : décalage tiré, bruit normal, arrondi parfois (égaux), zéros parfois."""
    decalage = rng.choice([-6.0, -3.0, -1.0, 0.0, 0.0, 1.0, 3.0, 6.0])
    d = rng.normal(decalage, 1.0, size=k)
    forme = rng.integers(0, 4)
    if forme == 1:
        d = np.round(d, 0)
    elif forme == 2:
        d = np.round(d, 1)
    elif forme == 3:
        d[rng.random(k) < 0.2] = 0.0
    return {f: float(x) for f, x in zip(familles[:k], d)}


def monde(rng) -> dict:
    k_e3 = int(rng.choice([4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))
    familles = [f"T{i:02d}" for i in range(1, k_e3 + 1)]

    def sous(kmax):
        return int(rng.choice([kmax, kmax, kmax, max(0, kmax - 1), max(0, kmax - 3), max(0, kmax - 5)]))

    manip_forte = rng.random() < 0.8
    d = {}
    for e in ("M1", "M3"):
        k = sous(k_e3)
        if manip_forte:
            d[e] = {f: float(x) for f, x in zip(familles[:k], rng.normal(5.0, 1.0, size=k))}
        else:
            d[e] = tirer_differences(rng, k, familles)
    d["E3"] = tirer_differences(rng, k_e3, familles)
    for e in ("E2a", "E2b", "E1"):
        k = sous(k_e3)
        if rng.random() < 0.5:
            d[e] = {f: v for f, v in list(d["E3"].items())[:k]}
        else:
            d[e] = tirer_differences(rng, k, familles)
    delta = float(rng.choice([0.5, 2.0, 8.0, 20.0]))
    par_famille = {f"A{i}": float(x) for i, x in enumerate(rng.normal(delta, 0.4 * delta, size=3), start=1)}
    borne = float(delta - rng.choice([0.2, 0.5, 1.2]) * delta)
    echec = rng.random() < 0.05
    return {"familles": familles, "d": d, "delta_app": delta, "par_famille": par_famille, "borne": borne,
            "echec": echec}


def resultat_du_premier(L, w: dict) -> dict:
    d, familles = w["d"], w["familles"]
    m = {f: {mb: {"m": 0.0, "taches": 16} for mb in ("jumeau", "saboteur", "sur_saboteur")} for f in familles}
    M1, M3 = L.epreuve(d["M1"], "M1"), L.epreuve(d["M3"], "M3")
    manip = {"m": m, "details": {}, "M1": M1, "M3": M3, "etablie": M1["separe"] and M3["separe"]}
    echecs = {"decisive": "perte non finie"} if w["echec"] else {}
    lu = bool(manip["etablie"]) and not w["echec"]
    if lu:
        diff = w["par_famille"]
        sep = {"delta_app": w["delta_app"], "par_famille": diff, "familles": sorted(diff), "borne_basse_99": w["borne"],
               "borne_haute_99": w["delta_app"] * 2, "tirages": L.TIRAGES,
               "etablie": all(v > 0 for v in diff.values()) and w["borne"] > 0}
        ep = {"familles": {}}
        for e in ("E3", "E2a", "E2b", "E1"):
            ep[e] = L.epreuve(d[e], e)
    else:
        sep = ep = None
    n_e3 = len(familles)
    i = L.issue(manip, sep, ep, echecs, n_e3)
    rap = L.rapportes(sep, ep, {"notations": {}}, {}) if ep is not None else {}
    audit = {"declencheurs": {"ii": True}}
    diag = {"mot": "non calculable", "motif": "fabriqué"}
    phrases = L.phrases(i["code"], i["niveau"], i["motifs"], manip, sep, ep, diag, audit, rap, 3)
    g = {"code": i["code"], "nom": L.NOMS_ISSUES[i["code"]] + (", au niveau de 95 %" if i["niveau"] == "95" else ""),
         "niveau": i["niveau"], "motifs": i["motifs"], "rapportes": rap, "audit_symetrie": audit, "phrases": phrases,
         "sondes_en_echec": dict(echecs)}
    resultat = {"format": L.FORMAT_RESULTAT, "b_manipulation": manip, "c_separation_apprise": sep, "d_epreuves": ep,
                "g_issue": g}
    return json.loads(json.dumps(L._convertible(resultat), ensure_ascii=False, sort_keys=True))


def main(argv: list[str]) -> int:
    if not argv or argv[0].startswith("--"):
        print(__doc__)
        return 2
    journal = argv[0]
    options = dict(zip(argv[1::2], argv[2::2]))
    if os.path.exists(journal):
        print(f"refus : {journal} existe déjà (on n'écrase jamais)")
        return 2
    L, sha_l = charger("controle_ia.barreau5_familles.lecture_v1", options.get("--premier"),
                       "controle_ia.barreau5_familles.lecture_copie_contre_lecture")
    S, sha_s = charger("controle_ia.barreau5_familles.seconde_programmation_v2", options.get("--second"),
                       "seconde_copie_contre_lecture")
    n = int(options.get("--mondes", MONDES))
    racine = np.random.SeedSequence(ENTROPIE)
    accords = collections.Counter()
    issues = collections.Counter()
    formes = collections.Counter()
    exemples = {}
    for i, enfant in enumerate(racine.spawn(n)):
        rng = np.random.default_rng(enfant)
        w = monde(rng)
        resultat = resultat_du_premier(L, w)
        rendu = S.comparer(0, resultat)
        code = resultat["g_issue"]["code"]
        issues[code] += 1
        if rendu["verdict"] == "accord exact":
            accords[code] += 1
            continue
        for x in rendu["desaccords"]:
            cle = json.dumps([x.get("champ"), x.get("premier"), x.get("second"), x.get("motif")], ensure_ascii=False)
            formes[cle] += 1
            exemples.setdefault(cle, i)
        for x in rendu["champs_manquants"]:
            formes[json.dumps(["manquant", x], ensure_ascii=False)] += 1
    rendu = {
        "entropie": ENTROPIE,
        "mondes": n,
        "premier": options.get("--premier", "paquet : controle_ia.barreau5_familles.lecture_v1"),
        "premier_sha256": sha_l or hashlib.sha256(open(L.__file__, "rb").read()).hexdigest(),
        "second": options.get("--second", "paquet : controle_ia.barreau5_familles.seconde_programmation_v2"),
        "second_sha256": sha_s or hashlib.sha256(open(S.__file__, "rb").read()).hexdigest(),
        "issues": dict(sorted(issues.items())),
        "accords_exacts": dict(sorted(accords.items())),
        "accords_exacts_total": sum(accords.values()),
        "desaccords_par_forme": [{"forme": json.loads(k), "mondes": v, "premier_monde": exemples.get(k)}
                                 for k, v in formes.most_common()],
    }
    with open(journal, "w", encoding="utf-8") as f:
        json.dump(rendu, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(json.dumps({k: rendu[k] for k in ("mondes", "issues", "accords_exacts", "accords_exacts_total")},
                     ensure_ascii=False))
    for x in rendu["desaccords_par_forme"][:20]:
        print(x["mondes"], json.dumps(x["forme"], ensure_ascii=False)[:300])
    return 0 if rendu["accords_exacts_total"] == n else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
