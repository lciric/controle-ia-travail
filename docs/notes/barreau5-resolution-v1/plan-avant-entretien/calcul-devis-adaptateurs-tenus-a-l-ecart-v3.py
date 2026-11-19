#!/usr/bin/env python3
"""Barreau 5, devis du brouillon 3 : relecture rechiffrée (v3). La formation est inchangée (calcul v2, f13422a6…).

Changements : l'épreuve à poussée égale se calcule après coup (plus de recherche de facteur ni de série relue à norme
égale : 79 s par adaptateur au lieu de 194, plus 5 s de produits scalaires ; 42,4 Go d'activations de moins) ; les
postes ajoutés par la contre-lecture (constat m-8) sont comptés. Mêmes débits et prix que la v2. Aucune donnée lue.
"""
PRIX, PIRE, DISQUE, TELECH = (1.0889, 1.30), 1.40, (0.03, 0.08), (0.026, 0.05)
GO = 1.06 * 640 / 576


def lecture(nom, adaptateurs, go, ancrages=0):
    n = adaptateurs + ancrages
    par = 30 + 64 * 0.45 + 20 + 5
    fixe = 1.3 + 64 * 40.2 / 3600 + n * par / 3600 + 0.29 + 0.03 + 0.17
    b = fixe + 0.25 + go * 1e9 / 100e6 / 3600
    h = fixe + 0.60 + go * 1e9 / 30e6 / 3600
    ub = b * (PRIX[0] + DISQUE[0]) + 40 * TELECH[0] + go * TELECH[0]
    uh = h * (PRIX[1] + DISQUE[1]) + 40 * TELECH[1] + go * TELECH[1]
    up = 2 * h * (PIRE + DISQUE[1]) + 40 * TELECH[1] + go * TELECH[1]
    print(f"== {nom} : {n} adaptateurs, {par:.0f} s chacun, {go:.1f} Go sortis ; {b:.2f} à {h:.2f} h ; {ub:.1f} à {uh:.1f} USD ; pire {up:.1f}")
    return b, h, ub, uh, up


def main():
    tout = lambda n, sab=3: (n * 3 + 3 + sab * 3) * GO
    print(f"activations, 36 adaptateurs : nominal trois couches {36 * 3 * GO:.1f} ; modèle nu {3 * GO:.1f} ; textes propres {9 * GO:.1f} ; total {tout(36):.1f} Go ; "
          f"repli 1 (couche 15, nominal et modèle nu) {37 * GO:.1f} ; repli 2 (un dixième) {3.7 * GO:.1f}")
    l = lecture("Relecture, nominal, tout gardé", 36, tout(36))
    lecture("Relecture, nominal, tout gardé, avec les quatre ancrages", 36, tout(36) + 12 * GO, 4)
    lecture("Relecture, repli 1", 36, 37 * GO)
    lecture("Relecture, repli 2", 36, 3.7 * GO)
    lecture("Relecture, plancher 28 adaptateurs, tout gardé", 28, tout(28, 2))
    r = lecture("Répétition générale, quatre adaptateurs existants", 4, 0.5)
    f = (58.0, 66.3, 72.2, 105.5, 210.3)                     # formation nominale, calcul v2
    print(f"== ensemble : {f[0] + l[0] + r[0]:.1f} à {f[1] + l[1] + r[1]:.1f} h ; {f[2] + l[2] + r[2]:.1f} à {f[3] + l[3] + r[3]:.1f} USD ; pire {f[4] + l[4] + r[4]:.1f}")
    print(f"== recharge : plafond 200 − crédit 21,97 = {200 - 21.97:.2f} ; avec la relecture des quatre cases de la chaîne voisine (coupure 8,5) : {200 - 21.97 + 8.5:.2f}")


if __name__ == "__main__":
    main()
