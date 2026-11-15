"""Complément de l'attaque du réfutateur — lecture dense — v1.

Mise au point exploratoire, aucune revendication. Processeur seul. Ce programme importe `attaque_libre_v1.py` (même dossier,
jamais modifié) et rejoue les MÊMES mondes (mêmes graines, mêmes tirages frais) deux fois : avec les 8 instants du juge
(25, 50, ..., 200), puis avec des instants plus serrés (tous les `PAS` tirages ; `PAS` divise 25, donc les 8 instants du juge
sont parmi eux). Rien d'autre ne change : même classe du nul, même dénominateur certifié, même seuil log(1/alpha).

Pourquoi : le concepteur conclut qu'aucune voie de son angle n'est à la fois valide sur toute la classe du nul v9 et plus
puissante que lui. Or la borne de Ville vaut pour TOUS les instants de 1 à n à la fois (preuve du nul limité, théorème 1,
pas 4 ; contre-lecture, correction p2 : fixer peu d'instants n'est pas nécessaire au théorème). Lire plus d'instants garde
donc la garantie sur la classe entière, et ne peut que promouvoir plus, monde pour monde. Ce programme mesure de combien.

Le cas « carte tout ou rien » (N4) n'est pas rejoué ici : sa carte est écrite d'après le premier instant lu.

Usage :
  python attaque_libre_lecture_dense_v1.py lot CAS LOT MONDES PAS SORTIE.json
  python attaque_libre_lecture_dense_v1.py fusion SORTIE.json LOT1.json LOT2.json ...
"""
import json
import os
import platform
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import attaque_libre_v1 as a  # noqa: E402

BRAS = ("v9", "v9_par_membre", "La", "Ld", "grille", "une_cellule_seule", "v8log_seul", "v9_complet", "v9_par_membre_complet",
        "La_complet", "Ld_complet", "grille_complet", "rapport_au_monde")


def mode_lot(cas, lot, W, pas, sortie):
    if cas.startswith("N4"):
        raise SystemExit("cas N4 non rejoué en lecture dense (carte écrite d'après le premier instant lu)")
    if 25 % pas:
        raise SystemExit("PAS doit diviser 25")
    t0 = time.time()
    instants_juge = a.INSTANTS.copy()
    ref = a.un_lot(cas, lot, W)
    a.INSTANTS = np.arange(pas, a.N + 1, pas)
    dense = a.un_lot(cas, lot, W)
    a.INSTANTS = instants_juge
    out = dict(version="attaque_libre_lecture_dense_v1", mode="lot", cas=cas, genre=ref["genre"], description=ref["description"],
               classes_qui_contiennent_le_monde=ref["classes_qui_contiennent_le_monde"], lot=lot, mondes=W, pas=pas,
               instants_juge=instants_juge.tolist(), nombre_instants_denses=int(a.N // pas),
               graines=ref["graines"], niveau=ref["niveau"],
               bits_juge={k: v for k, v in ref["bits"].items() if k in BRAS},
               bits_dense={k: v for k, v in dense["bits"].items() if k in BRAS},
               bits_dense_au_pire={k: v for k, v in dense["bits_au_pire"].items() if k in BRAS},
               instants_indecis_dense=dense["instants_indecis"], domination_violee_dense=dense["domination_violee"],
               emboitement_viole_dense=dense["emboitement_viole"],
               duree_s=round(time.time() - t0, 1), python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(cas, lot, W, pas, {k: (round(out["bits_juge"][k].count("1") / W, 4), round(v.count("1") / W, 4))
                             for k, v in out["bits_dense"].items()}, out["duree_s"])


def apparie(x, y, n):
    gagne = sum(1 for u, v in zip(x, y) if u == "1" and v == "0")
    perd = sum(1 for u, v in zip(x, y) if u == "0" and v == "1")
    return dict(promue_seulement_par_le_bras=gagne, promue_seulement_par_la_reference=perd, gain_apparie=round((gagne - perd) / n, 4))


def mode_fusion(sortie, fichiers):
    par = {}
    lus = []
    for f in fichiers:
        d = json.load(open(f, encoding="utf-8"))
        lus.append(dict(fichier=os.path.basename(f), sha256=a.empreinte_fichier(f), cas=d["cas"], lot=d["lot"], pas=d["pas"],
                        mondes=d["mondes"], duree_s=d["duree_s"]))
        par.setdefault((d["cas"], d["pas"]), []).append(d)
    res = {}
    for (cas, pas), ds in sorted(par.items(), key=lambda kv: (a.CAS[kv[0][0]]["no"], kv[0][1])):
        ds.sort(key=lambda d: d["lot"])
        if [d["lot"] for d in ds] != list(range(len(ds))):
            raise SystemExit(f"lots non contigus pour {cas}")
        bj = {k: "".join(d["bits_juge"][k] for d in ds) for k in ds[0]["bits_juge"]}
        bd = {k: "".join(d["bits_dense"][k] for d in ds) for k in ds[0]["bits_dense"]}
        bp = {k: "".join(d["bits_dense_au_pire"][k] for d in ds) for k in ds[0]["bits_dense_au_pire"]}
        n = len(bj["v9"])
        classes = ds[0]["classes_qui_contiennent_le_monde"]
        e = dict(description=ds[0]["description"], genre=ds[0]["genre"], mondes=n, pas=pas,
                 nombre_instants_denses=ds[0]["nombre_instants_denses"], classes_qui_contiennent_le_monde=classes,
                 graines=[d["graines"]["spawn_key"] for d in ds],
                 taux_juge={k: a.taux([x == "1" for x in v]) for k, v in bj.items()},
                 taux_dense={k: a.taux([x == "1" for x in v]) for k, v in bd.items()},
                 taux_dense_au_pire={k: a.taux([x == "1" for x in v]) for k, v in bp.items()},
                 instants_indecis_dense={k: sum(d["instants_indecis_dense"][k] for d in ds) for k in ds[0]["instants_indecis_dense"]},
                 domination_violee_dense={k: sum(d["domination_violee_dense"][k] for d in ds) for k in ds[0]["domination_violee_dense"]},
                 # la lecture dense contient les instants du juge : une carte promue aux 8 instants et pas en lecture dense
                 # ne peut venir que d'une partition indécise
                 promue_aux_instants_du_juge_et_pas_en_dense={k: sum(1 for u, v in zip(bj[k], bd[k]) if u == "1" and v == "0")
                                                              for k in bd},
                 apparie={})
        if ds[0]["genre"] == "taille":
            e["taille_dense"] = {k: dict(borne_haute_ic95_au_pire=e["taux_dense_au_pire"][k]["ic95"][1],
                                         sous_le_niveau=bool(e["taux_dense_au_pire"][k]["ic95"][1] <= a.ALPHA))
                                 for k in ("v9", "v9_par_membre", "La", "Ld", "grille")
                                 if (k in classes or (k == "v9_par_membre" and "v9" in classes))}
        for k in bd:
            e["apparie"][f"{k}_dense_contre_{k}_juge"] = apparie(bd[k], bj[k], n)
        for x, y in (("v9", "La"), ("v9_par_membre", "La"), ("v9_complet", "La_complet"), ("v9_par_membre_complet", "La_complet"),
                     ("v9_complet", "v8log_seul"), ("v9_par_membre_complet", "v8log_seul")):
            if x in bd and y in bj:
                e["apparie"][f"{x}_dense_contre_{y}_juge"] = apparie(bd[x], bj[y], n)
        e["bits_juge"], e["bits_dense"], e["bits_dense_au_pire"] = bj, bd, bp
        res[f"{cas}|pas={pas}"] = e
    out = dict(version="attaque_libre_lecture_dense_v1", mode="fusion", racine=a.RACINE, cas=res, lots_lus=lus,
               programme_importe=dict(fichier="attaque_libre_v1.py", sha256=a.empreinte_fichier(os.path.join(ICI, "attaque_libre_v1.py"))),
               python=platform.python_version(), numpy=np.__version__)
    json.dump(out, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, e in res.items():
        print(k, e["mondes"], {b: (e["taux_juge"][b]["taux"], v["taux"]) for b, v in e["taux_dense"].items()})


if __name__ == "__main__":
    if sys.argv[1] == "lot":
        mode_lot(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
    elif sys.argv[1] == "fusion":
        mode_fusion(sys.argv[2], sys.argv[3:])
    else:
        raise SystemExit(__doc__)
