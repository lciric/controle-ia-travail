"""Rejeu des programmes de l'auteur (`essai_regret_*_v1.py`) et comparaison à ses sorties scellées — v1.

Statut : mise au point exploratoire, aucune revendication. Outil du réfutateur ; aucun fichier de l'auteur n'est modifié.

Deux voies de rejeu :
1. rejeu complet : les cinq programmes de l'auteur sont copiés à l'octet dans un dossier de travail hors du dépôt (ses
   programmes refusent d'écraser leurs sorties), puis lancés tels quels (`python -I -B essai_regret_..._v1.py ...`) ;
   `comparer DOSSIER` compare chaque sortie rejouée à la sortie scellée de même nom, champs de durée exclus ;
2. rejeu par tranches, pour un essai de puissance qui ne tient pas en dix minutes sur la machine partagée :
   `tranche DOSE DEBUT FIN` appelle la fonction de jugement de l'auteur (`essai_regret_juge_v1.juger`, importée du dossier,
   empreintes vérifiées) sur les mondes DEBUT..FIN−1 de la dose, avec les graines mêmes de son programme
   (SeedSequence(2026111503, spawn_key=(indice de la dose,)), un enfant par monde, 500 échantillons d'importance) ;
   `comparer` rassemble les tranches et refait l'agrégat de `essai_regret_puissance_v1.py` (comptes, taux, intervalles,
   comptes appariés, médianes), puis le compare à la sortie scellée.

Sorties : `rejeu-sorties/rejeu_regret_v1--d<DOSE>--<DEBUT>-<FIN>.json` ; `rejeu_regret_v1.json` (jamais écrasées).
"""
import hashlib
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIES_AUTEUR = os.path.join(ICI, "sorties")
TRANCHES = os.path.join(ICI, "rejeu-sorties")
ENTROPIE_PUISSANCE = 2026111503          # lue dans essai_regret_puissance_v1.py
DOSES = (0.1, 0.2, 0.35)                 # idem
PROGRAMMES = ("essai_regret_banc_v1.py", "essai_regret_juge_v1.py", "essai_regret_bornes_v1.py",
              "essai_regret_taille_v1.py", "essai_regret_puissance_v1.py")


def empreinte(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def scellee(chemin):
    """Empreinte du compagnon .sha256, et vérification que le fichier lui est égal."""
    attendu = open(chemin + ".sha256", encoding="utf-8").read().split()[0]
    if empreinte(chemin) != attendu:
        raise SystemExit(f"{chemin} : empreinte différente de son compagnon")
    return attendu


def _un(arg):
    dose, graine = arg
    sys.path.insert(0, ICI)
    import essai_regret_juge_v1 as jg
    res, maxlw, info = jg.juger("decouverte", graine, methodes_v9r=True, dose=dose, nb_is=500)
    return {"res": res, "maxlw": maxlw, "ecart_max_certificat": info["ecart_max_certificat"]}


def tranche(dose, debut, fin):
    for p in PROGRAMMES[:2]:
        scellee(os.path.join(ICI, p))
    os.makedirs(TRANCHES, exist_ok=True)
    chemin = os.path.join(TRANCHES, f"rejeu_regret_v1--d{dose}--{debut}-{fin}.json")
    if os.path.exists(chemin):
        raise SystemExit(f"refus d'écraser {chemin}")
    ss = np.random.SeedSequence(ENTROPIE_PUISSANCE, spawn_key=(DOSES.index(dose),))
    graines = [int(c.generate_state(1)[0]) for c in ss.spawn(500)]
    t0 = time.time()
    with Pool(3) as pool:
        mondes = pool.map(_un, [(dose, g) for g in graines[debut:fin]], chunksize=4)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump({"outil": "rejeu_regret_v1.py", "dose": dose, "debut": debut, "fin": fin, "graines": graines[debut:fin],
                   "empreintes_programmes_auteur": {p: empreinte(os.path.join(ICI, p)) for p in PROGRAMMES[:2]},
                   "mondes": mondes, "duree_s": round(time.time() - t0, 1)}, f, ensure_ascii=False)
    print("écrit", chemin, round(time.time() - t0, 1), "s")


def _sans_durees(d):
    if isinstance(d, dict):
        return {k: _sans_durees(v) for k, v in d.items() if not k.startswith("duree")}
    if isinstance(d, list):
        return [_sans_durees(x) for x in d]
    return d


def _differences(a, b, chemin=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                out.append([f"{chemin}/{k}", str(a.get(k, "absent")), str(b.get(k, "absent"))])
            else:
                out += _differences(a[k], b[k], f"{chemin}/{k}")
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)):
            out += _differences(x, y, f"{chemin}[{i}]")
    elif a != b:
        out.append([chemin, str(a), str(b)])
    return out


def comparer(dossier):
    sys.path.insert(0, ICI)
    import essai_regret_banc_v1 as bc
    chemin = os.path.join(ICI, "rejeu_regret_v1.json")
    if os.path.exists(chemin):
        raise SystemExit(f"refus d'écraser {chemin}")
    progs = {}
    for p in PROGRAMMES:
        progs[p] = {"empreinte_scellee": scellee(os.path.join(ICI, p)),
                    "empreinte_de_la_copie_rejouee": empreinte(os.path.join(dossier, p)) if os.path.exists(os.path.join(dossier, p)) else None}
        progs[p]["copie_a_l_octet"] = progs[p]["empreinte_scellee"] == progs[p]["empreinte_de_la_copie_rejouee"]
    complets, tranches = {}, {}
    for nom in sorted(os.listdir(SORTIES_AUTEUR)):
        if not nom.endswith(".json"):
            continue
        pa = os.path.join(SORTIES_AUTEUR, nom)
        h = scellee(pa)
        a = json.load(open(pa, encoding="utf-8"))
        pr = os.path.join(dossier, "sorties", nom)
        if os.path.exists(pr):
            d = _differences(_sans_durees(a), _sans_durees(json.load(open(pr, encoding="utf-8"))))
            complets[nom] = {"empreinte_sortie_auteur": h, "empreinte_sortie_rejouee": empreinte(pr),
                             "identique_hors_durees": not d, "nombre_de_differences": len(d), "differences": d[:30]}
        elif a.get("essai") == "essai_regret_puissance_v1":
            dose = a["dose"]
            fichiers = sorted(f for f in (os.listdir(TRANCHES) if os.path.isdir(TRANCHES) else [])
                              if f.startswith(f"rejeu_regret_v1--d{dose}--"))
            morceaux = sorted((json.load(open(os.path.join(TRANCHES, f), encoding="utf-8")) for f in fichiers),
                              key=lambda m: m["debut"])
            mondes = [w for m in morceaux for w in m["mondes"]]
            couverts = [(m["debut"], m["fin"]) for m in morceaux]
            if not mondes or couverts[0][0] != 0 or couverts[-1][1] != a["mondes"] or any(
                    x[1] != y[0] for x, y in zip(couverts, couverts[1:])):
                tranches[nom] = {"empreinte_sortie_auteur": h, "rejoue": False, "tranches": couverts}
                continue
            nb = len(mondes)
            methodes = [k for k in mondes[0]["res"] if not k.startswith("R1-La-sous")]
            ref = np.array([w["res"]["MAX-v9r"] for w in mondes])
            refLa = np.array([w["res"]["MAX-La"] for w in mondes])
            lignes = {}
            for mth in methodes:                      # même agrégat que essai_regret_puissance_v1.main
                v = np.array([w["res"][mth] for w in mondes])
                k = int(v.sum())
                lignes[mth] = {"promues": k, "mondes": nb, "taux": round(k / nb, 4), "intervalle_95": bc.clopper_pearson(k, nb),
                               "promues_par_elle_seule_contre_MAX-v9r": int((v & ~ref).sum()),
                               "promues_par_MAX-v9r_seul": int((~v & ref).sum()),
                               "promues_par_elle_seule_contre_MAX-La": int((v & ~refLa).sum()),
                               "promues_par_MAX-La_seul": int((~v & refLa).sum()),
                               "log_W_max_mediane": round(float(np.median([w["maxlw"][mth] for w in mondes])), 3)}
            refait = {"lignes": lignes,
                      "R1_La_lots_sous_le_maximum_exact": int(sum(w["res"]["R1-La-sous-le-maximum"] for w in mondes)),
                      "ecart_certificat_max": round(max(w["ecart_max_certificat"] for w in mondes), 6)}
            d = _differences({k: a[k] for k in refait}, refait)
            tranches[nom] = {"empreinte_sortie_auteur": h, "rejoue": True, "tranches": couverts,
                             "fichiers_tranches": {f: empreinte(os.path.join(TRANCHES, f)) for f in fichiers},
                             "champs_compares": list(refait), "identique": not d, "nombre_de_differences": len(d),
                             "differences": d[:30]}
        else:
            complets[nom] = {"empreinte_sortie_auteur": h, "rejoue": False}
    sortie = {"outil": "rejeu_regret_v1.py", "statut": "mise au point exploratoire, aucune revendication",
              "programmes": progs, "rejeu_complet(programmes de l'auteur lancés tels quels)": complets,
              "rejeu_par_tranches(fonction de jugement de l'auteur, agrégat refait)": tranches}
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    for nom, v in {**complets, **tranches}.items():
        print(nom, {k: v[k] for k in v if k in ("identique_hors_durees", "identique", "rejoue", "nombre_de_differences")})


if __name__ == "__main__":
    if sys.argv[1] == "tranche":
        tranche(float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif sys.argv[1] == "comparer":
        comparer(sys.argv[2])
    else:
        raise SystemExit(__doc__)
