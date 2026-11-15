"""Résumé des sorties du banc de l'angle « toute autre voie » — v1. Lit sorties/sortie-banc-cas*-v2.json (sorties de essai_libre_banc_v2.py) (chaque fichier
vérifié contre son compagnon .sha256 avant lecture), recolle les tranches d'un même cas (bits dans l'ordre des r),
calcule les taux et intervalles de Clopper-Pearson bilatéraux à 95 %, les comparaisons appariées de puissance (mêmes
tirages, mêmes instants), et la marge théorique d'une grille de poids (méthode Mc). Usage : python essai_libre_resume_v1.py SORTIE.json"""
import glob
import hashlib
import json
import math
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from essai_libre_commun_v1 import clopper  # noqa: E402

BRAS = ("v9", "La", "Ld", "grille", "A1", "A2", "Mc", "Md", "OU", "ET", "mixte")


def lire(chemin):
    h = hashlib.sha256(open(chemin, "rb").read()).hexdigest()
    attendu = open(chemin + ".sha256").read().split()[0]
    if h != attendu:
        raise SystemExit(f"empreinte non conforme : {chemin}")
    return json.load(open(chemin)), h


def main():
    sortie = sys.argv[1]
    par_cas = {}
    fichiers = []
    for ch in sorted(glob.glob(os.path.join(ICI, "sorties", "sortie-banc-cas*-v2.json"))):
        d, h = lire(ch)
        fichiers.append(dict(chemin=os.path.relpath(ch, ICI), sha256=h, cas=d["cas"], r=[d["r_debut"], d["r_fin"]],
                             duree_s=d["duree_s"], violations_emboitement=d["violations_emboitement"],
                             reste_certificat_max_par_nul=d["reste_certificat_max_par_nul"]))
        par_cas.setdefault(d["cas"], []).append(d)
    res = {}
    for cas, ds in sorted(par_cas.items()):
        ds.sort(key=lambda d: d["r_debut"])
        bornes = [(d["r_debut"], d["r_fin"]) for d in ds]
        for (a, b), (c, _) in zip(bornes, bornes[1:]):
            if b != c:
                raise SystemExit(f"tranches non contiguës pour le cas {cas}")
        bras = [b for b in BRAS if b in ds[0]["bits"]]
        bits = {b: "".join(d["bits"][b] for d in ds) for b in bras}
        n = len(bits["La"])
        e = dict(description=ds[0]["description"], mondes=n, r=[bornes[0][0], bornes[-1][1]],
                 duree_s_par_monde=round(sum(d["duree_s"] for d in ds) / n, 3),
                 violations_emboitement=sum(d["violations_emboitement"] for d in ds), taux={})
        e["avec_v9"] = ds[0]["avec_v9"]
        e["seuil_critique_grille_mediane_par_tranche"] = [d["seuil_critique_grille_quantiles"][1] for d in ds]
        e["seuil_critique_reechantillonnage_mediane_par_tranche"] = [d["seuil_critique_reechantillonnage_quantiles"][1] for d in ds]
        for b in bras:
            k = bits[b].count("1")
            e["taux"][b] = dict(promues=k, taux=round(k / n, 4), ic95=clopper(k, n))
        if cas >= 7:  # puissance : comparaisons appariées contre v9 et contre La
            comp = {}
            for ref in ("v9", "La"):
                for b in bras:
                    if b == ref:
                        continue
                    x, y = bits[b], bits[ref]
                    gagne = sum(1 for u, v in zip(x, y) if u == "1" and v == "0")
                    perd = sum(1 for u, v in zip(x, y) if u == "0" and v == "1")
                    comp[f"{b}_contre_{ref}"] = dict(promue_seulement_par_le_bras=gagne, promue_seulement_par_la_reference=perd,
                                                    gain_apparie=round((gagne - perd) / n, 4))
            e["apparie"] = comp
        res[str(cas)] = e
    # méthode Mc2 (essai_libre_projection_carte_v1.py) : mêmes mondes et mêmes tirages que le banc
    proj = {}
    for ch in sorted(glob.glob(os.path.join(ICI, "sorties", "sortie-projection-cas*-v1.json"))):
        d, h = lire(ch)
        fichiers.append(dict(chemin=os.path.relpath(ch, ICI), sha256=h, cas=d["cas"], r=[d["r_debut"], d["r_fin"]],
                             duree_s=d["duree_s"]))
        proj.setdefault(d["cas"], []).append(d)
    for cas, ds in sorted(proj.items()):
        ds.sort(key=lambda d: d["r_debut"])
        e = res[str(cas)]
        for k in ("Mc", "Mc2"):
            bits = "".join(d["bits"][k] for d in ds)
            nom = "Mc_recalcule" if k == "Mc" else "Mc2"
            e["taux"][nom] = dict(promues=bits.count("1"), taux=round(bits.count("1") / len(bits), 4),
                                  ic95=clopper(bits.count("1"), len(bits)), mondes=len(bits),
                                  r=[ds[0]["r_debut"], ds[-1]["r_fin"]])
            if cas >= 7:
                ref = "".join(dd["bits"]["La"] for dd in sorted(par_cas[cas], key=lambda d: d["r_debut"]))[:len(bits)]
                gagne = sum(1 for u, v in zip(bits, ref) if u == "1" and v == "0")
                perd = sum(1 for u, v in zip(bits, ref) if u == "0" and v == "1")
                e["apparie"][f"{nom}_contre_La"] = dict(promue_seulement_par_le_bras=gagne,
                                                         promue_seulement_par_la_reference=perd,
                                                         gain_apparie=round((gagne - perd) / len(bits), 4))
        e["seuil_projection_mediane_par_tranche"] = [d["seuil_projection_quantiles"][1] for d in ds]
    # marge d'une grille de poids (méthode Mc) : couverture multiplicative et couverture en variation totale
    n_tir, dim, plancher = 200, 7, 1e-6
    ratio = 2 ** (1 / n_tir)  # (rapport)^n <= 2 : une grille au niveau alpha/2 garde alpha hors grille
    par_dim_mult = math.log(1 / plancher) / math.log(ratio)
    dl1 = 2 * 0.025 / n_tir  # n * (1/2) * ||d theta||_1 <= 0,025
    par_dim_vt = 1 / (dl1 / dim)
    marge = dict(
        hypotheses="classe La : 3 lois connues par cellule, 2 cellules, 3 lois certaines communes ; 9 poids, 2 contraintes : "
                   "dimension 7 ; n = 200 ; poids planchers 1e-6 pour la couverture multiplicative",
        couverture_multiplicative=dict(rapport_max_par_tirage=ratio, points_par_dimension=round(par_dim_mult),
                                       log10_points_de_grille=round(dim * math.log10(par_dim_mult), 1)),
        couverture_variation_totale=dict(norme_l1_max=dl1, points_par_dimension=round(par_dim_vt),
                                         log10_points_de_grille=round(dim * math.log10(par_dim_vt), 1)),
    )
    out = dict(version="essai_libre_resume_v1", fichiers=fichiers, cas=res, marge_grille_Mc=marge)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for c, e in res.items():
        print(c, e["mondes"], {b: v["taux"] for b, v in e["taux"].items()})


if __name__ == "__main__":
    main()
