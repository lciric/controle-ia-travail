#!/usr/bin/env python3
"""Contre-lecture du devis du brouillon 2 (barreau 5, familles jumelles) : arithmétique refaite, v1.

Écrite par le contre-lecteur (Claude Opus 5.5) le 19 novembre 2026, sans reprendre le script du rédacteur. Mêmes débits
et prix d'entrée (ceux des textes scellés : `prereg/validite-adaptateur-v1.md` l. 204-226, `prereg/T0.6-organismes-v0-v1.md`
« Devis ») : 40,2 s par épisode en lots de 8, 0,45 s par passe forcée, distillation 0,23 à 0,46 h, carte 1,0889 à 1,30 USD
de l'heure (pire 1,40, hôte deux fois plus lent), stockage 0,03 à 0,08 USD de l'heure, transfert 0,026 à 0,05 USD le Go,
40 Go descendus par instance. Ajouts du contre-lecteur, chacun marqué : postes que le devis du brouillon ne compte pas.
Aucune donnée du programme n'est lue. Sortie : texte sur la sortie standard.
"""
EPISODE_S, PASSE_S = 40.2, 0.45
DIST_H = (0.23, 0.46)
PRIX, PRIX_PIRE = (1.0889, 1.30), 1.40
STOCK = (0.03, 0.08)
TRANSFERT = (0.026, 0.05)
DESCENTE_GO = 40
FIXE_FORMATION_H = 1.0 + 0.6 + 0.2
FIXE_LECTURE_H = 1.0 + 0.3
GO_SERIE = 1.06 / 576 * 640          # une couche, 640 actions, par jeton, demi-précision (sous-ensemble de 7b)


def h(episodes):
    return episodes * EPISODE_S / 3600


def famille(membres, eval_episodes):
    return tuple(h(160) + membres * d + h(eval_episodes) for d in DIST_H)


def dollars(heures, instances=1, sortie_go=0.0):
    bas = heures[0] * (PRIX[0] + STOCK[0]) + instances * DESCENTE_GO * TRANSFERT[0] + sortie_go * TRANSFERT[0]
    haut = heures[1] * (PRIX[1] + STOCK[1]) + instances * DESCENTE_GO * TRANSFERT[1] + sortie_go * TRANSFERT[1]
    pire = 2 * heures[1] * (PRIX_PIRE + STOCK[1]) + instances * DESCENTE_GO * TRANSFERT[1] + sortie_go * TRANSFERT[1]
    return bas, haut, pire


def instance(n_tenues, n_app):
    t, a = famille(3, 3 * 32), famille(2, 64 + 32)
    return tuple(FIXE_FORMATION_H + n_tenues * t[i] + n_app * a[i] for i in (0, 1))


def main():
    print("# 1. Formation, sept instances (5 × deux familles tenues à l'écart ; 1 × deux d'apprentissage ; 1 × une)")
    rep = [(2, 0)] * 5 + [(0, 2), (0, 1)]
    hs = [instance(*r) for r in rep]
    tot_h = (sum(x[0] for x in hs), sum(x[1] for x in hs))
    us = [dollars(x) for x in hs]
    tot_u = tuple(sum(u[i] for u in us) for i in range(3))
    print(f"   heures de carte {tot_h[0]:.2f} à {tot_h[1]:.2f} ; horloge {max(x[0] for x in hs):.2f} à {max(x[1] for x in hs):.2f} h")
    print(f"   USD attendu {tot_u[0]:.1f} à {tot_u[1]:.1f} ; pire {tot_u[2]:.1f}")
    print(f"   instance à deux familles tenues : {hs[0][0]:.2f} à {hs[0][1]:.2f} h ; pire {us[0][2]:.1f} USD ; coupure du devis 26")

    print("# 2. Relecture et notation, une instance (tout gardé)")
    adaptateurs = 36
    par_adaptateur_s = 30 + 64 * PASSE_S + 12 * 16 * PASSE_S + 64 * PASSE_S + 20
    go = adaptateurs * 4 * GO_SERIE + 3 * GO_SERIE + 3 * 3 * GO_SERIE
    base = (FIXE_LECTURE_H + h(64) + adaptateurs * par_adaptateur_s / 3600,) * 2
    sondes = (0.25, 0.60)
    sortie = (go * 1e9 / 100e6 / 3600, go * 1e9 / 30e6 / 3600)
    lect = (base[0] + sondes[0] + sortie[0], base[1] + sondes[1] + sortie[1])
    ul = dollars(lect, 1, go)
    print(f"   {par_adaptateur_s:.0f} s par adaptateur ; {go:.1f} Go d'activations ; {lect[0]:.2f} à {lect[1]:.2f} h ; "
          f"{ul[0]:.1f} à {ul[1]:.1f} USD ; pire {ul[2]:.1f}")
    # ajouts du contre-lecteur
    kl_s = 64 * PASSE_S                      # loi du modèle nu recalculée pour la divergence, par adaptateur (si non gardée)
    nu_force_s = 64 * PASSE_S               # série du modèle nu relue par le même chemin forcé
    propres_s = 3 * 64 * PASSE_S            # épisodes propres des saboteurs d'apprentissage relus
    ancrage_s = 4 * par_adaptateur_s        # quatre adaptateurs existants relus comme points d'ancrage (nœud 3)
    ancrage_go = 4 * 3 * GO_SERIE
    contr_s = 2 * 300                       # contrôle carte-processeur d'une sonde (forme de l'étape B bis), supposé 10 min
    ajout_h = (adaptateurs * kl_s + nu_force_s + propres_s + ancrage_s + contr_s) / 3600
    lect2 = (lect[0] + ajout_h, lect[1] + ajout_h + ancrage_go * 1e9 / 30e6 / 3600)
    ul2 = dollars(lect2, 1, go + ancrage_go)
    print(f"   + postes non comptés (divergence {adaptateurs * kl_s / 3600:.2f} h ; modèle nu forcé {nu_force_s / 3600:.3f} h ; "
          f"épisodes propres {propres_s / 3600:.3f} h ; ancrages {ancrage_s / 3600:.2f} h et {ancrage_go:.1f} Go ; "
          f"contrôle carte-processeur {contr_s / 3600:.2f} h) : {lect2[0]:.2f} à {lect2[1]:.2f} h ; {ul2[0]:.1f} à {ul2[1]:.1f} USD ; "
          f"pire {ul2[2]:.1f} ; coupure du devis 24")

    print("# 3. Répétition générale (quatre adaptateurs existants)")
    rep_h = tuple(FIXE_LECTURE_H + h(64) + 4 * par_adaptateur_s / 3600 + s + 0.5 * 1e9 / d / 3600
                  for s, d in ((0.25, 100e6), (0.60, 30e6)))
    ur = dollars(rep_h, 1, 0.5)
    print(f"   {rep_h[0]:.2f} à {rep_h[1]:.2f} h ; {ur[0]:.1f} à {ur[1]:.1f} USD ; pire {ur[2]:.1f} ; coupure du devis 7")

    print("# 4. Ensemble")
    ens = tuple(tot_u[i] + ul2[i] + ur[i] for i in range(3))
    print(f"   attendu {ens[0]:.1f} à {ens[1]:.1f} USD ; pire {ens[2]:.1f} ; plafond demandé 200 ; coupures 169 + 24 + 7 = 200")
    print(f"   sans répétition ni ancrages : attendu {tot_u[0] + ul[0]:.1f} à {tot_u[1] + ul[1]:.1f}")

    print("# 5. Crédit")
    credit = 21.97
    debit_7 = 7 * (PRIX[1] + STOCK[1])
    print(f"   sept cartes au prix haut : {debit_7:.2f} USD de l'heure ; crédit de {credit} USD : {credit / debit_7:.2f} h")
    print(f"   recharge pour porter le crédit au plafond de 200 : {200 - credit:.2f} USD ; "
          f"avec la relecture des quatre cases de GO-2026-11-19-62 (coupure 8,5) en plus : {208.5 - credit:.2f} USD")

    print("# 6. Disque de l'instance de relecture et plafond du stockage")
    for disque in (150, 250, 450):
        print(f"   {disque} Go : un stockage à 0,08 USD de l'heure au plus exige au plus {0.08 * 730 / disque:.3f} USD le Go-mois")

    print("# 7. Activations gardées")
    print(f"   par série {GO_SERIE:.3f} Go ; nominal trois couches {adaptateurs * 3 * GO_SERIE:.1f} ; norme égale {adaptateurs * GO_SERIE:.1f} ; "
          f"modèle nu {3 * GO_SERIE:.1f} ; épisodes propres {9 * GO_SERIE:.1f} ; total {go:.1f} Go ; avec ancrages {go + ancrage_go:.1f} Go")
    print(f"   repli 1 (couche 15, nominal, modèle nu) {(adaptateurs + 1) * GO_SERIE:.1f} Go ; repli 2 (un dixième) {(adaptateurs + 1) * GO_SERIE / 10:.2f} Go")


if __name__ == "__main__":
    main()
