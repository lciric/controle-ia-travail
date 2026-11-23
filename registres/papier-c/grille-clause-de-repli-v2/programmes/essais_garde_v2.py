"""Essais de la garde de completude (R5) : un cas sain et des artefacts, sur des sorties synthetiques construites
depuis la liste finie (aucun taux reel lu ni employe ; les taux synthetiques valent 0).

Usage : python3 -B essais_garde_v2.py LISTE.md
Sortie : une ligne par essai, « attendu » et « obtenu » ; code 0 si tous les essais donnent l'attendu.
"""
import copy
import sys

from liste_et_garde_v2 import CLE_A, CLE_B, CLE_C, CLE_I, GardeCompletude, lire_liste, verifier_completude


def synthetiques(cases):
    out = []
    for c in cases:
        base = dict(modele=c["modele"], attaque=c["attaque"], k=c["k"], T=c["T"], passe=0,
                    juges=[list(j) for j in c["juges"]], g=[c["g"]] * 3)
        ab = dict(base, programme="grille_ab_v2.py", R=1000, B=1000, taux={CLE_A: 0.0, CLE_B: 0.0})
        cc = dict(base, programme="grille_c_v2.py", R=8000, contenu_defini="C" in c["bras_c"],
                  taux={CLE_I: 0.0, CLE_C: 0.0 if "C" in c["bras_c"] else None})
        nom = f"{c['modele']}_{c['attaque']}_k{c['k']}_T{c['T']}_p0.json"
        out += [("ab_" + nom, ab), ("c_" + nom, cc)]
    return out


def essai(nom, sorties, cases, attendu_sain):
    try:
        bilan = verifier_completude(cases, sorties)
        obtenu = "saine"
        detail = "; ".join(f"{k} {v['couvertes']}/{v['liste']}" for k, v in bilan.items())
    except GardeCompletude as e:
        obtenu = "echec"
        detail = " | ".join(str(e).splitlines()[1:])
    attendu = "saine" if attendu_sain else "echec"
    ok = obtenu == attendu
    print(f"[{'OK' if ok else 'FAUX'}] {nom} : attendu {attendu}, obtenu {obtenu} ({detail})")
    return ok


def main():
    cases = lire_liste(sys.argv[1])
    s = synthetiques(cases)
    oks = [essai("cas sain : 144 + 144 sorties conformes", s, cases, True)]
    # artefact 1 : une case manquante (C-P3a et C-P3b, case 034)
    a1 = [x for x in s if x[0] != "ab_E40_g20_k5_T30_p0.json"]
    oks.append(essai("artefact 1 : sortie ab de la case 034 retiree", a1, cases, False))
    # artefact 2 : une case en double (C-P3c, case 001)
    a2 = s + [("c_E30_g00_k3_T30_p0.json", copy.deepcopy(dict(s)["c_E30_g00_k3_T30_p0.json"]))]
    oks.append(essai("artefact 2 : sortie c de la case 001 en double", a2, cases, False))
    # artefact 3 : effectif reduit (C-P3c, case 002, R = 4000)
    a3 = copy.deepcopy(s)
    for nom, x in a3:
        if nom == "c_E30_g00_k3_T45_p0.json":
            x["R"] = 4000
    oks.append(essai("artefact 3 : case 002 de C-P3c a R = 4 000", a3, cases, False))
    # artefact 4 : bras « contenu » absent la ou la liste le demande (case 109)
    a4 = copy.deepcopy(s)
    for nom, x in a4:
        if nom == "c_MH_g00_k3_T30_p0.json":
            x["taux"][CLE_C] = None
            x["contenu_defini"] = False
    oks.append(essai("artefact 4 : case 109 sans bras « contenu »", a4, cases, False))
    print("ESSAIS DE LA GARDE :", "TOUS CONFORMES" if all(oks) else "ECHEC")
    return 0 if all(oks) else 1


if __name__ == "__main__":
    sys.exit(main())
