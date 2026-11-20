"""Contre-lecture S : recalcul indépendant des nombres du plafond de l'étage 2 à 200 témoins (fractions exactes).
Aucune importation du code du développeur ni du calcul v2 ; tarifs lus dans le texte du rapport (constantes ci-dessous).
Usage : python3 -I -B refaire_plafond_cl_v1.py
"""
from fractions import Fraction as F

PLAFOND = F(8836, 100)
RESERVE = F(60, 100)
TARIF = {"O": F(3431597, 47000000), "A": F(51253, 2000000)}
FACTEUR_PIRE = F(3431597, 1739000)
N = 200


def envois():
    """Liste (bloc, rang_temoin, juge, rendu), dans l'ordre : P, A, B (rang 1..200, lecture d'abord)."""
    s = []
    for t in (1, 2):
        s += [("P", t, "O", 1), ("P", t, "A", 1)]
    for t in range(1, N + 1):
        s += [("A", t, "O", 1), ("A", t, "A", 1)]
    for t in range(1, N + 1):
        s += [("B", t, "O", 2), ("B", t, "A", 2), ("B", t, "A", 3)]
    return s


def jouer(facteur, refus=0, tous=False):
    cum, partis, restants = F(0), 0, refus
    obtenus, dernier, interdit = set(), None, None
    for e in envois():
        cout = TARIF[e[2]] * facteur
        if tous:
            tentatives = [None, None]
        elif restants > 0:
            tentatives = [None, cout]
            restants -= 1
        else:
            tentatives = [cout]
        stop = False
        for k, c in enumerate(tentatives, 1):
            if not (cum + RESERVE <= PLAFOND):
                interdit = (e, k, cum)
                stop = True
                break
            partis += 1
            cum += RESERVE if c is None else c
            dernier = (e, k)
            if c is not None:
                obtenus.add(e)
                break
        if stop:
            break
    b_complets = [t for t in range(1, N + 1)
                  if all(("B", t, j, r) in obtenus for j, r in (("O", 2), ("A", 2), ("A", 3)))]
    a_complets = sum(1 for t in range(1, N + 1) if ("A", t, "O", 1) in obtenus and ("A", t, "A", 1) in obtenus)
    return {"partis": partis, "cumul": cum, "dernier": dernier, "interdit": interdit, "obtenus": len(obtenus),
            "A": a_complets, "B": len(b_complets), "B_lecture": sum(1 for t in b_complets if t <= 100),
            "B_etal": sum(1 for t in b_complets if t > 100)}


def dec(x, n=4):
    q = round(x * 10 ** n)
    s = str(abs(q)).rjust(n + 1, "0")
    return ("-" if q < 0 else "") + s[:-n] + "." + s[-n:]


def ligne(nom, r):
    print(nom, "| partis", r["partis"], "| cumul", dec(r["cumul"]), "| A", r["A"], "| B", r["B"],
          "(lecture", r["B_lecture"], ", etal", r["B_etal"], ")", "| dernier", r["dernier"], "| interdit",
          None if r["interdit"] is None else (r["interdit"][0], r["interdit"][1], dec(r["interdit"][2])))


if __name__ == "__main__":
    print("plan", len(envois()))
    pire = jouer(FACTEUR_PIRE)
    ligne("pire cas", pire)
    assert pire["partis"] == 996 and dec(pire["cumul"]) == "87.7701" and pire["A"] == 200 and pire["B"] == 197
    assert pire["dernier"][0] == ("B", 198, "O", 2) and pire["interdit"][0] == ("B", 198, "A", 2)
    tout = jouer(F(1), tous=True)
    ligne("tout refuse", tout)
    assert tout["partis"] == 147 and dec(tout["cumul"], 2) == "88.20" and tout["obtenus"] == 0
    print("dernier envoi tout refuse bloc A rang", tout["dernier"][0][1], "(le rang est l'ordre tire du bloc A)")
    # factices de refus : estimation (facteur 2669827104/3633259223), haut (1), pire
    f_est = F(2669827104, 3633259223)
    for nom, f, rs in (("estimation", f_est, (0, 1, 10, 100)), ("haut", F(1), (0, 1, 10, 80, 100)),
                       ("pire", FACTEUR_PIRE, (0, 1, 10, 40, 80, 100))):
        for r in rs:
            ligne(f"{nom} refus={r}", jouer(f, refus=r))
    # attendus du calcul v2 (sortie scellee) pour trois lignes
    attendus = {("estimation", 100): (935, 143), ("haut", 80): (963, 159), ("pire", 10): (934, 173),
                ("pire", 100): (385, 0), ("pire", 80): (490, 2)}
    for (nom, r), (p, b) in attendus.items():
        f = {"estimation": f_est, "haut": F(1), "pire": FACTEUR_PIRE}[nom]
        x = jouer(f, refus=r)
        assert (x["partis"], x["B"]) == (p, b), (nom, r, x["partis"], x["B"])
        print("accord calcul v2 :", nom, r, p, b)
    # seuil d'arret de la plomberie : trois fois le tarif
    p3 = jouer(F(3))
    ligne("trois fois le tarif", p3)
    assert p3["partis"] == 630 and dec(p3["cumul"]) == "87.9542" and p3["B"] == 75
    # frontiere exacte : 147 envois a 0,60 -> 88,20 ; 148e interdit
    print("OK")
