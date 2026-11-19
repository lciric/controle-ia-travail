"""Resume des sorties de la grille (aucun calcul nouveau : lecture des JSON de ../sorties et mise en tables).

Marques, pour le taux de la lecture jointe du texte (conj3) compare au seuil de la clause 0,05 + 2 racine(0,05 x 0,95 / R) :
  « > » : au-dessus du seuil ;  « ~ » : sous le seuil de moins de deux erreurs de Monte-Carlo (comparaison non nette) ;
  «   » : sous le seuil d'au moins deux erreurs de Monte-Carlo (comparaison nette).
Usage : python3 -B resume_grille_v1.py [DOSSIER_SORTIES]
"""
import glob
import json
import os
import sys

from grille_commun_v1 import ATTAQUES, EFFETS, MODELES, versions

ORDRE_M = list(MODELES) + list(EFFETS)
ORDRE_A = list(ATTAQUES)


def marque(p, e, s):
    if p > s:
        return ">"
    if p + 2 * e > s:
        return "~"
    return " "


def cle(r):
    return (ORDRE_M.index(r["modele"]), ORDRE_A.index(r["attaque"]), r["k"], r["T"], r["passe"])


def f3(p, e=None, m=""):
    if p is None:
        return "non défini"
    return f"{p:.3f}" + (f" ± {e:.3f}" if e is not None else "") + (f" {m}" if m.strip() else "")


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sorties")
    v = versions()
    print(f"python {v['python']} ; numpy {v['numpy']} ; scipy {v['scipy']}")
    ab = sorted((json.load(open(f)) for f in glob.glob(os.path.join(d, "ab_*.json"))), key=cle)
    cc = sorted((json.load(open(f)) for f in glob.glob(os.path.join(d, "c_*.json"))), key=cle)
    print(f"\n## C-P3a et C-P3b ({len(ab)} sorties)\n")
    print("| modèle | attaque | k | T | passe | R | seuil | C-P3a trois lectures | C-P3b trois lectures | lecture (ii) a / b |"
          " deux lectures a / b | rr seule a / b | cal a / b | brut a / b | part max. de tirages dégénérés A / B |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    bilan = {}
    for r in ab:
        t, e, s = r["taux"], r["erreur_mc"], r["seuil_clause"]
        ma, mb = marque(t["conj3_a"], e["conj3_a"], s), marque(t["conj3_b"], e["conj3_b"], s)
        nul = r["modele"] not in EFFETS
        if nul:
            for st, mq in (("a", ma), ("b", mb)):
                b = bilan.setdefault((r["passe"], st), dict(n=0, sup=[], flou=[], lo=1, hi=0, lo2=1, hi2=0, lo_ii=1, hi_ii=0))
                b["n"] += 1
                b["lo"], b["hi"] = min(b["lo"], t[f"conj3_{st}"]), max(b["hi"], t[f"conj3_{st}"])
                b["lo2"], b["hi2"] = min(b["lo2"], t[f"conj2_{st}"]), max(b["hi2"], t[f"conj2_{st}"])
                b["lo_ii"], b["hi_ii"] = min(b["lo_ii"], t[f"conj3_ii_{st}"]), max(b["hi_ii"], t[f"conj3_ii_{st}"])
                nom = f"{r['modele']} {r['attaque']} k{r['k']} T{r['T']} ({t[f'conj3_{st}']:.3f})"
                if mq == ">":
                    b["sup"].append(nom)
                elif mq == "~":
                    b["flou"].append(nom)
        dg = r["part_max_tirages_degeneres"]
        print(f"| {r['modele']} | {r['attaque']} | {r['k']} | {r['T']} | {r['passe']} | {r['R']} | {s:.4f} |"
              f" {f3(t['conj3_a'], e['conj3_a'], ma)} | {f3(t['conj3_b'], e['conj3_b'], mb)} |"
              f" {t['conj3_ii_a']:.3f} / {t['conj3_ii_b']:.3f} | {t['conj2_a']:.3f} / {t['conj2_b']:.3f} |"
              f" {t['rr_a']:.3f} / {t['rr_b']:.3f} | {t['cal_a']:.3f} / {t['cal_b']:.3f} |"
              f" {t['brut_a']:.3f} / {t['brut_b']:.3f} | {dg['A']:.3f} / {dg['B']:.3f} |")
    print("\nBilan des cases nulles (scénarios d'effet P3 et P6 exclus) :")
    for (p, st), b in sorted(bilan.items()):
        print(f"- passe {p}, C-P3{st} : {b['n']} cases ; trois lectures {b['lo']:.3f} à {b['hi']:.3f} ; lecture (ii)"
              f" {b['lo_ii']:.3f} à {b['hi_ii']:.3f} ; deux lectures {b['lo2']:.3f} à {b['hi2']:.3f} ;"
              f" au-dessus du seuil : {b['sup'] or 'aucune'} ; non nettes : {b['flou'] or 'aucune'}")

    print(f"\n## C-P3c ({len(cc)} sorties) : taux de « établie » aux trois lectures jointes, par bras du modèle\n")
    bras = ["bruit", "insertion_kP3_lie", "insertion_kP1_lie", "contenu_kP3_lie", "contenu_kP1_lie",
            "insertion_kP3_fort", "contenu_kP3_fort", "insertion_S_separe_kP3_lie"]
    print("| modèle | attaque | k | T | passe | R | seuil | " + " | ".join(bras) +
          " | deux lectures : insertion_kP3_lie / contenu_kP3_lie | une lecture (cal) : bruit / insertion_kP3_lie / contenu_kP3_lie |")
    print("|---|---|---|---|---|---|---|" + "---|" * (len(bras) + 2))
    bil = {}
    for r in cc:
        t, e, s = r["taux"], r["erreur_mc"], r["seuil_clause"]
        cells = []
        for b in bras:
            p, er = t[f"{b}|conj3"], e[f"{b}|conj3"]
            if p is None:
                cells.append("non défini")
                continue
            mq = marque(p, er, s)
            cells.append(f3(p, er, mq))
            if r["modele"] not in EFFETS:
                x = bil.setdefault((r["passe"], b), dict(n=0, sup=0, flou=0, lo=1, hi=0, noms=[]))
                x["n"] += 1
                x["lo"], x["hi"] = min(x["lo"], p), max(x["hi"], p)
                if mq == ">":
                    x["sup"] += 1
                    x["noms"].append(f"{r['modele']} {r['attaque']} k{r['k']} T{r['T']}")
                elif mq == "~":
                    x["flou"] += 1
        d2 = " / ".join(f3(t[f"{b}|conj2"]) for b in ("insertion_kP3_lie", "contenu_kP3_lie"))
        d1 = " / ".join(f3(t[f"{b}|cal"]) for b in ("bruit", "insertion_kP3_lie", "contenu_kP3_lie"))
        print(f"| {r['modele']} | {r['attaque']} | {r['k']} | {r['T']} | {r['passe']} | {r['R']} | {s:.4f} | "
              + " | ".join(cells) + f" | {d2} | {d1} |")
    print("\nBilan des cases nulles par bras (scénarios d'effet exclus) :")
    for (p, b), x in sorted(bil.items()):
        print(f"- passe {p}, {b} : {x['n']} cases définies ; {x['lo']:.3f} à {x['hi']:.3f} ; au-dessus du seuil : {x['sup']} ;"
              f" non nettes : {x['flou']}")
    print("\nCases nulles au-dessus du seuil, par bras et par modèle × attaque (nombre sur les quatre couples k × T) :")
    for (p, b), x in sorted(bil.items()):
        if not x["noms"]:
            continue
        cpt = {}
        for nm in x["noms"]:
            m_a = " ".join(nm.split()[:2])
            cpt[m_a] = cpt.get(m_a, 0) + 1
        print(f"- passe {p}, {b} : " + " ; ".join(f"{k_} {v_}/4" for k_, v_ in cpt.items()))
    ex = sum(r["essais_avec_ex_aequo"] for r in cc)
    print(f"\nEssais avec ex æquo exacts dans un gain d'écart (tous bras définis) : {ex}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
