#!/usr/bin/env python3
"""Barreau 5, plan d'avant l'entretien : arithmétique du devis des familles jumelles (v1).

Aucun chiffre neuf : débits et prix viennent de textes scellés et de registres, cités dans le devis.
  - 40,2 s par épisode en lots de 8 ; 0,45 s par passe d'épisode en relecture forcée ; distillation de 480 pas :
    0,23 à 0,46 h (prereg/T0.6-organismes-v0-v1.md, « Devis » ; prereg/validite-adaptateur-v1.md l. 206) ;
  - mise en place 1,0 h, essais sur l'instance 0,6 h (formation) ou 0,3 h (relecture), poussée 0,2 h (même devis) ;
  - carte A100 SXM4 80 Go : 1,0889 à 1,30 USD de l'heure attendus, 1,22 relevé le 19 novembre (registres/depenses.md),
    1,40 au pire avec un hôte deux fois plus lent ; téléchargement 0,026 à 0,05 USD par Go, 40 Go prévus par instance.
Sortie : texte sur la sortie standard.
"""
from __future__ import annotations

EPISODE_H = 40.2 / 3600.0
PASSE_H = 0.45 / 3600.0
DISTILL = (0.23, 0.46)
PRIX = (1.0889, 1.22, 1.30)          # bas, relevé du jour, borne haute attendue
PRIX_PIRE, LENTEUR_PIRE = 1.40, 2.0
TELECH_GO, TELECH_USD_GO = 40.0, (0.026, 0.05)
DISQUE_USD = (0.25, 0.6)
MISE_EN_PLACE, ESSAIS_FORMATION, ESSAIS_LECTURE, POUSSEE = 1.0, 0.6, 0.3, 0.2


def famille(membres: int, taches_manip: int):
    """Heures de carte d'une famille : 160 épisodes de distillation, puis par membre une distillation et les épisodes
    de la vérification de manipulation (un épisode par tâche, dose 1)."""
    base = 160 * EPISODE_H + membres * taches_manip * EPISODE_H
    return base + membres * DISTILL[0], base + membres * DISTILL[1]


def formation(n_ecart: int, n_app: int, taches_manip: int, repartition: list[tuple[int, int]]):
    """`repartition` : par instance, (familles tenues à l'écart, familles d'apprentissage)."""
    assert sum(a for a, _ in repartition) == n_ecart and sum(b for _, b in repartition) == n_app
    fe, fa = famille(3, taches_manip), famille(2, taches_manip)
    fixes = MISE_EN_PLACE + ESSAIS_FORMATION + POUSSEE
    inst = [(fixes + a * fe[0] + b * fa[0], fixes + a * fe[1] + b * fa[1]) for a, b in repartition]
    bas, haut = sum(x for x, _ in inst), sum(y for _, y in inst)
    n = len(repartition)
    usd_bas = bas * PRIX[0] + n * (TELECH_GO * TELECH_USD_GO[0] + DISQUE_USD[0])
    usd_centre = 0.5 * (bas + haut) * PRIX[1] + n * (TELECH_GO * 0.5 * sum(TELECH_USD_GO) + 0.5 * sum(DISQUE_USD))
    usd_haut = haut * PRIX[2] + n * (TELECH_GO * TELECH_USD_GO[1] + DISQUE_USD[1])
    pire = haut * LENTEUR_PIRE * PRIX_PIRE + n * (TELECH_GO * TELECH_USD_GO[1] + 2 * DISQUE_USD[1])
    return {"instances": n, "heures_par_instance": [(round(x, 2), round(y, 2)) for x, y in inst],
            "horloge_max_h": (round(max(x for x, _ in inst), 1), round(max(y for _, y in inst), 1)),
            "heures_total": (round(bas, 1), round(haut, 1)), "usd": (round(usd_bas, 1), round(usd_centre, 1), round(usd_haut, 1)),
            "usd_pire": round(pire, 1), "adaptateurs": 3 * n_ecart + 2 * n_app, "tirages_de_donnees": n_ecart + n_app,
            "pire_par_instance": [round(y * LENTEUR_PIRE * PRIX_PIRE + TELECH_GO * TELECH_USD_GO[1] + 2 * DISQUE_USD[1], 1)
                                  for _, y in inst]}


def lecture(adaptateurs: int, go_activations: float, debit_mo_s=(100.0, 30.0)):
    par_adaptateur = (64 * 2 + 12 * 16 + 64) * PASSE_H + 20.0 / 3600.0     # nominale + nu pour la divergence, dichotomie, norme égale, chargement
    communs = MISE_EN_PLACE + ESSAIS_LECTURE + 64 * EPISODE_H + 0.03 + POUSSEE / 2
    sondes = (0.25, 0.6)                                                   # apprentissage (16 sondes) et notation de toutes les séries
    televers = tuple(go_activations * 1000.0 / d / 3600.0 for d in debit_mo_s)
    bas = communs + adaptateurs * par_adaptateur + sondes[0] + televers[0]
    haut = communs + adaptateurs * par_adaptateur + sondes[1] + televers[1]
    sortie_go = (go_activations * TELECH_USD_GO[0], go_activations * TELECH_USD_GO[1])
    usd_bas = bas * PRIX[0] + TELECH_GO * TELECH_USD_GO[0] + sortie_go[0] + 0.6
    usd_haut = haut * PRIX[2] + TELECH_GO * TELECH_USD_GO[1] + sortie_go[1] + 1.2
    pire = haut * LENTEUR_PIRE * PRIX_PIRE + TELECH_GO * TELECH_USD_GO[1] + sortie_go[1] + 2.4
    return {"heures": (round(bas, 2), round(haut, 2)), "par_adaptateur_s": round(par_adaptateur * 3600),
            "usd": (round(usd_bas, 1), round(usd_haut, 1)), "usd_pire": round(pire, 1),
            "sortie_des_activations_usd": tuple(round(x, 1) for x in sortie_go)}


def stockage(adaptateurs: int, saboteurs_app: int):
    serie_couche = 1.18                                # Go : 640 actions, une couche, par jeton, demi-précision (1,06 Go pour 576)
    nominal = adaptateurs * 3 * serie_couche
    egal = adaptateurs * serie_couche
    nu = 3 * serie_couche
    propres = saboteurs_app * 3 * serie_couche
    return {"nominal_trois_couches": round(nominal, 1), "norme_egale_couche_15": round(egal, 1), "modele_nu": round(nu, 1),
            "textes_propres_des_saboteurs_d_apprentissage": round(propres, 1), "total_go": round(nominal + egal + nu + propres, 1),
            "repli_couche_15_seule_go": round(adaptateurs * 2 * serie_couche + serie_couche, 1),
            "repli_un_dixieme_couche_15_nominal_go": round((adaptateurs + 1) * serie_couche / 10, 1)}


def main():
    plans = {
        "nominal : 8 familles tenues à l'écart, 3 d'apprentissage, 64 tâches de manipulation, 6 instances":
            formation(8, 3, 64, [(2, 0)] * 4 + [(0, 2), (0, 1)]),
        "même plan sur 4 instances":
            formation(8, 3, 64, [(2, 1), (2, 1), (2, 1), (2, 0)]),
        "même plan sur 11 instances (une famille par instance)":
            formation(8, 3, 64, [(1, 0)] * 8 + [(0, 1)] * 3),
        "coupe 1 : 8 et 3, 32 tâches de manipulation, 6 instances":
            formation(8, 3, 32, [(2, 0)] * 4 + [(0, 2), (0, 1)]),
        "coupe 2 : 6 familles tenues à l'écart, 3 d'apprentissage, 32 tâches, 5 instances":
            formation(6, 3, 32, [(2, 0)] * 3 + [(0, 2), (0, 1)]),
        "plancher : 5 familles tenues à l'écart, 2 d'apprentissage, 32 tâches, 4 instances":
            formation(5, 2, 32, [(2, 0), (2, 0), (1, 1), (0, 1)]),
    }
    for nom, f in plans.items():
        print(f"== Formation, {nom}")
        for k, v in f.items():
            print(f"   {k} : {v}")
    for nom, (n, s) in {"nominal (30 adaptateurs)": (30, 3), "plancher (19 adaptateurs)": (19, 2)}.items():
        st = stockage(n, s)
        print(f"== Activations gardées, {nom}")
        for k, v in st.items():
            print(f"   {k} : {v}")
        le = lecture(n, st["total_go"])
        print(f"== Relecture et notation, {nom}, tout gardé")
        for k, v in le.items():
            print(f"   {k} : {v}")
        le2 = lecture(n, st["repli_un_dixieme_couche_15_nominal_go"])
        print(f"== Relecture et notation, {nom}, repli au dixième")
        for k, v in le2.items():
            print(f"   {k} : {v}")
    rep = (MISE_EN_PLACE + ESSAIS_LECTURE + 64 * EPISODE_H + 4 * ((64 * 2 + 12 * 16 + 64) * PASSE_H + 20 / 3600) + 0.3 + POUSSEE)
    print("== Répétition générale sur les quatre adaptateurs existants")
    print(f"   heures : {rep:.2f} ; usd : {rep * PRIX[0] + 1.0:.1f} à {rep * PRIX[2] + 2.0:.1f} ; pire : {rep * LENTEUR_PIRE * PRIX_PIRE + 2.0:.1f}")


if __name__ == "__main__":
    main()
