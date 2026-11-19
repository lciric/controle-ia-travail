#!/usr/bin/env python3
"""Barreau 5, plan d'avant l'entretien : arithmétique du devis du brouillon 2 (v2).

Écrit par le rédacteur de la reprise (19 novembre 2026). La version 1 (scellée, 27682fdf…) chiffrait le plan du
brouillon 1 (8 familles tenues à l'écart à trois membres, 64 tâches de vérification) ; celle-ci chiffre le plan du
brouillon 2 : 10 familles tenues à l'écart à trois membres (jumeau, saboteur, sur-saboteur), 3 familles d'apprentissage
à deux membres, vérification du coût sur 32 tâches (64 pour les saboteurs d'apprentissage).
Aucun chiffre neuf : débits et prix du préenregistrement des organismes (prereg/T0.6-organismes-v0-v1.md, « Devis »,
l. 640-652) repris par le texte de validité de l'adaptateur (prereg/validite-adaptateur-v1.md, l. 206-224).
Aucune donnée du programme n'est lue. Sortie : texte sur la sortie standard.
"""
S_EPISODE = 40.2            # s par épisode généré, lots de 8
S_PASSE = 0.45              # s par passe d'épisode en relecture forcée
H_DISTILLATION = (0.23, 0.46)
H_FIXE_FORMATION = 1.0 + 0.6 + 0.2      # mise en place, essais, poussée
H_FIXE_LECTURE = 1.0 + 0.3
PRIX = (1.0889, 1.30)       # USD par heure de carte, attendu
PRIX_PIRE = 1.40            # avec un hôte deux fois plus lent
DISQUE = (0.03, 0.08)       # USD par heure (stockage de l'instance) ; 0,08 est le plafond du filtre
TELECH_GO, TELECH = 40, (0.026, 0.05)
GO_PAR_SERIE = 1.06 * 640 / 576         # une couche, 640 actions, par jeton, demi-précision
DEBIT_SORTIE = (100e6, 30e6)            # octets par seconde, supposé


def h_episodes(n):
    return n * S_EPISODE / 3600.0


def famille(membres, episodes_eval):
    bas = h_episodes(160) + membres * H_DISTILLATION[0] + h_episodes(episodes_eval)
    haut = h_episodes(160) + membres * H_DISTILLATION[1] + h_episodes(episodes_eval)
    return bas, haut


def usd(h_bas, h_haut, instances):
    bas = h_bas * (PRIX[0] + DISQUE[0]) + instances * TELECH_GO * TELECH[0]
    haut = h_haut * (PRIX[1] + DISQUE[1]) + instances * TELECH_GO * TELECH[1]
    pire = 2 * h_haut * (PRIX_PIRE + DISQUE[1]) + instances * TELECH_GO * TELECH[1]
    return bas, haut, pire


def formation(nom, repartition, taches_verif=32):
    """repartition : liste d'instances, chacune (familles tenues à l'écart, familles d'apprentissage)."""
    fe = famille(3, 3 * taches_verif)
    fa = famille(2, 64 + taches_verif)
    print(f"== {nom}")
    print(f"   une famille tenue à l'écart : {fe[0]:.2f} à {fe[1]:.2f} h ; une famille d'apprentissage : {fa[0]:.2f} à {fa[1]:.2f} h")
    tb = th = 0.0
    ub = uh = up = 0.0
    horloge = (0.0, 0.0)
    for k, (ne, na) in enumerate(repartition, 1):
        b = H_FIXE_FORMATION + ne * fe[0] + na * fa[0]
        h = H_FIXE_FORMATION + ne * fe[1] + na * fa[1]
        u = usd(b, h, 1)
        print(f"   instance {k} ({ne} tenue(s) à l'écart, {na} d'apprentissage) : {b:.2f} à {h:.2f} h ; {u[0]:.1f} à {u[1]:.1f} USD ; pire {u[2]:.1f}")
        tb += b; th += h; ub += u[0]; uh += u[1]; up += u[2]
        horloge = (max(horloge[0], b), max(horloge[1], h))
    ne = sum(r[0] for r in repartition); na = sum(r[1] for r in repartition)
    print(f"   total : {3 * ne + 2 * na} adaptateurs, {ne + na} tirages ; {tb:.1f} à {th:.1f} h de carte ; horloge {horloge[0]:.1f} à {horloge[1]:.1f} h ; "
          f"{ub:.1f} à {uh:.1f} USD (centre {(ub + uh) / 2:.1f}) ; pire {up:.1f}")
    return tb, th, ub, uh, up


def activations(adaptateurs, saboteurs_app=3):
    nominal = adaptateurs * 3 * GO_PAR_SERIE
    egal = adaptateurs * GO_PAR_SERIE
    nu = 3 * GO_PAR_SERIE
    propres = saboteurs_app * 3 * GO_PAR_SERIE
    return {"nominal_trois_couches": nominal, "norme_egale_couche_15": egal, "modele_nu_trois_couches": nu,
            "textes_propres_des_saboteurs_d_apprentissage": propres, "total": nominal + egal + nu + propres,
            "repli_1_couche_15_nominal_et_modele_nu": (adaptateurs + 1) * GO_PAR_SERIE,
            "repli_2_un_dixieme_couche_15_nominal_et_modele_nu": (adaptateurs + 1) * GO_PAR_SERIE / 10}


def lecture(nom, adaptateurs, go):
    par_adaptateur = 30 + 64 * S_PASSE + 12 * 16 * S_PASSE + 64 * S_PASSE + 20     # chargement et gardes, nominale, recherche, norme égale, écritures
    communs = h_episodes(64)
    b = H_FIXE_LECTURE + communs + adaptateurs * par_adaptateur / 3600 + 0.25 + go * 1e9 / DEBIT_SORTIE[0] / 3600
    h = H_FIXE_LECTURE + communs + adaptateurs * par_adaptateur / 3600 + 0.60 + go * 1e9 / DEBIT_SORTIE[1] / 3600
    sortie = (go * TELECH[0], go * TELECH[1])
    u = usd(b, h, 1)
    print(f"== {nom} : {adaptateurs} adaptateurs, {go:.1f} Go sortis ; {par_adaptateur:.0f} s par adaptateur ; {b:.2f} à {h:.2f} h ; "
          f"{u[0] + sortie[0]:.1f} à {u[1] + sortie[1]:.1f} USD (dont sortie des activations {sortie[0]:.1f} à {sortie[1]:.1f}) ; pire {u[2] + sortie[1]:.1f}")
    return b, h, u[0] + sortie[0], u[1] + sortie[1], u[2] + sortie[1]


def main():
    print("# plan nominal du brouillon 2")
    f = formation("Formation, nominal : 10 familles tenues à l'écart, 3 d'apprentissage, 7 instances",
                  [(2, 0)] * 5 + [(0, 2), (0, 1)])
    formation("Formation, même plan sur 4 instances", [(3, 0), (3, 0), (2, 1), (2, 2)])
    formation("Formation, même plan sur 5 instances", [(3, 0), (3, 0), (2, 0), (2, 0), (0, 3)])
    formation("Formation, même plan sur 13 instances", [(1, 0)] * 10 + [(0, 1)] * 3)
    formation("Formation, même plan, vérification du coût sur 64 tâches partout (pour mémoire)", [(2, 0)] * 5 + [(0, 2), (0, 1)], taches_verif=64)
    print("# plans réduits")
    formation("Coupe : 9 familles tenues à l'écart, 3 d'apprentissage, 7 instances", [(2, 0)] * 4 + [(1, 0), (0, 2), (0, 1)])
    formation("Coupe : 8 familles tenues à l'écart, 3 d'apprentissage, 6 instances", [(2, 0)] * 4 + [(0, 2), (0, 1)])
    p = formation("Plancher : 8 familles tenues à l'écart, 2 d'apprentissage, 5 instances", [(2, 0)] * 4 + [(0, 2)])
    print("# activations gardées (Go)")
    a36 = activations(36)
    a28 = activations(28, 2)
    for nom, a in (("nominal, 36 adaptateurs", a36), ("plancher, 28 adaptateurs", a28)):
        print(f"== {nom} : " + " ; ".join(f"{k} {v:.1f}" for k, v in a.items()))
    print("# relecture et notation")
    l1 = lecture("Relecture, nominal, tout gardé", 36, a36["total"])
    l2 = lecture("Relecture, nominal, repli 1 (couche 15, série nominale et modèle nu)", 36, a36["repli_1_couche_15_nominal_et_modele_nu"])
    l3 = lecture("Relecture, nominal, repli 2 (un dixième)", 36, a36["repli_2_un_dixieme_couche_15_nominal_et_modele_nu"])
    lecture("Relecture, plancher, tout gardé", 28, a28["total"])
    r = lecture("Répétition générale sur les quatre adaptateurs existants (rien de gardé hors scores)", 4, 0.5)
    print("# ensemble, nominal")
    for nom, l in (("tout gardé", l1), ("repli 1", l2), ("repli 2", l3)):
        print(f"== formation + relecture ({nom}) + répétition : {f[0] + l[0] + r[0]:.1f} à {f[1] + l[1] + r[1]:.1f} h ; "
              f"{f[2] + l[2] + r[2]:.1f} à {f[3] + l[3] + r[3]:.1f} USD ; pire {f[4] + l[4] + r[4]:.1f}")
    print(f"== plancher + relecture (tout gardé, 28) : voir lignes ci-dessus ; formation {p[2]:.1f} à {p[3]:.1f} USD, pire {p[4]:.1f}")
    print("# crédit")
    credit = 21.97
    for plafond in (200.0, 170.0):
        print(f"== plafond {plafond:.0f} USD : recharge pour porter le crédit au plafond = {plafond - credit:.2f} USD")
    print(f"== débit de 7 cartes au prix haut, stockage compris : {7 * (PRIX[1] + DISQUE[1]):.2f} USD par heure ; le crédit de {credit} USD tient {credit / (7 * (PRIX[1] + DISQUE[1])):.1f} h")
    print("# témoin à changement bénin du même champ (option, 10 adaptateurs de plus, aucun tirage)")
    print(f"== formation : {10 * (H_DISTILLATION[0] + h_episodes(32)):.1f} à {10 * (H_DISTILLATION[1] + h_episodes(32)):.1f} h ; "
          f"{10 * (H_DISTILLATION[0] + h_episodes(32)) * (PRIX[0] + DISQUE[0]):.1f} à {10 * (H_DISTILLATION[1] + h_episodes(32)) * (PRIX[1] + DISQUE[1]):.1f} USD")


if __name__ == "__main__":
    main()
