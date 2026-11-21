#!/usr/bin/env python3
"""Limite dite de la règle, sur réseau factice : un décalage visé sur un multiple du pas.

Sous une loi arrondie, l'une des deux aires encadrantes d'une aire dite est une valeur de saut :
elle n'est réalisée que par un décalage posé exactement sur un multiple du pas. Un auteur qui vise
cette aire et écrit son nombre à quatre ou six décimales ne tombe pas sur le multiple : il tombe
sur le palier du dessous ou sur celui du dessus, selon le sens de l'arrondi d'écriture.

Ce programme le montre sur la normale réduite arrondie au pas 0,25, avec les classes et la règle
de `epreuve_note_ecart_v2_regle_v3_reseau_factice_v1.py` (même dossier). Illustration, non
opposable ; flottants ; de la main du concepteur ; non contre-lu. Aucune entrée extérieure.

Prédictions écrites avant la première exécution (constante ATTENDU) :
- nombre exact (flottant) : l'aire de saut, reçue « conforme au pas du réseau » ;
- nombre arrondi vers le bas, à quatre ou six décimales : le palier du dessous, encadrant, reçu ;
- nombre arrondi vers le haut, à quatre ou six décimales : le palier du dessus, non encadrant,
  non reçu, « aucune unité ne réalise les aires ».
Commande : python3 -I -B limite_decalage_vise_sur_un_multiple_du_pas_v1.py
"""
import importlib.util
import math
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location(
    "epreuve", os.path.join(ICI, "epreuve_note_ecart_v2_regle_v3_reseau_factice_v1.py"))
ep = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ep)

# (rang de l'aire dite, multiple du pas visé, nombres fixes des deux autres rangs)
CAS = (
    (0, 3, (None, 1.1902, 2.3688)),   # aire dite 0,69 : saut visé 0,7011, à 3 pas
    (1, 5, (0.7012, None, 2.3688)),   # aire dite 0,80 : saut visé 0,8104, à 5 pas
)
ATTENDU = {
    "exact": ep.A_BIS,
    "arrondi vers le bas, quatre décimales": ep.A_BIS,
    "arrondi vers le bas, six décimales": ep.A_BIS,
    "arrondi vers le haut, quatre décimales": ep.R3,
    "arrondi vers le haut, six décimales": ep.R3,
}


def main():
    loi = ep.LoiNormaleArrondie(0.25)
    print("Limite dite — décalage visé sur un multiple du pas — illustration, non opposable")
    print("Loi : %s ; écart type %s" % (loi.nom, ep.fr(loi.sigma, 6)))
    tenues = total = 0
    for rang, multiple, fixes in CAS:
        a = ep.AIRES_DITES[rang]
        (s, ns), (u, nu) = loi.encadrantes_nommees(a)
        exact = multiple * loi.pas / loi.sigma
        print()
        print("Aire dite %s : aires encadrantes %s (%s) et %s (%s) ; saut visé à %d pas ; nombre exact %s"
              % (ep.fr(a, 2), ep.fr(s), ns, ep.fr(u), nu, multiple, ep.fr(exact, 9)))
        ecritures = [("exact", exact)]
        for k, mot in ((4, "quatre"), (6, "six")):
            ecritures.append(("arrondi vers le bas, %s décimales" % mot, math.floor(exact * 10 ** k) / 10 ** k))
            ecritures.append(("arrondi vers le haut, %s décimales" % mot, math.ceil(exact * 10 ** k) / 10 ** k))
        for nom, nombre in ecritures:
            nombres = list(fixes)
            nombres[rang] = nombre
            aires = [loi.aire(x * loi.sigma) for x in nombres]
            issue = ep.classer_tranche(loi, aires)[rang][0]
            ok = issue == ATTENDU[nom]
            total += 1
            tenues += 1 if ok else 0
            print("  %s : nombre écrit %s ; aire réalisée %s (écart %s) -> %s — prédit : %s — PRÉDICTION %s"
                  % (nom, ep.fr(nombre, 9), ep.fr(aires[rang]), ep.fr(abs(aires[rang] - a)), issue,
                     ATTENDU[nom], "TENUE" if ok else "MANQUÉE"))
    print()
    print("Bilan : %d prédictions tenues sur %d" % (tenues, total))
    return 0 if tenues == total else 1


if __name__ == "__main__":
    sys.exit(main())
