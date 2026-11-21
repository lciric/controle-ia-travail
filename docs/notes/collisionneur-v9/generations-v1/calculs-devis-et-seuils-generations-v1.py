#!/usr/bin/env python3
"""Annexe de calcul de conception-generations-jusqu-au-plateau-v1.md (même dossier). Sans réseau, sans clé, sans écriture.

Charge la table des espèces et les fonctions de pire cas du script collisionneur_v9_v7.py (empreinte contrôlée, aucun
envoi : le script n'est qu'importé) et recalcule les chiffres que la note marque « calcul de cette note » :
1. le pire cas de sortie d'une cellule (plafond de sortie plus provision de réflexion, au prix de sortie), par espèce et
   par tour, sans relance et avec relance ;
2. une borne des tours III.2 et III.3, toutes cellules à envoyer, à la manière de `devis-reprise` (critique non écrite
   bornée par le plafond de sortie de son auteur), sous des longueurs SUPPOSÉES, pour la comparer aux chiffres du rapport
   du développeur de la version 7 (section 3.2, dossier « mathématiques ») ;
3. le surcoût d'entrée de l'état d'une génération : N réponses au tour III.1, une critique au tour III.2 ;
4. le total au pire d'une génération, par composition, à la manière du rapport, puis (4 bis) la borne stricte avant tout
   envoi, où tout texte de la génération est borné par le plafond de sortie de son auteur ;
5. ce que les seuils du plateau veulent dire en nombres d'entrées de registre.

Aucun dossier de course n'a été lu : les longueurs ci-dessous sont des hypothèses, écrites en clair. Avant toute course, le
devis exact se fait sur les longueurs réelles des cellules scellées (commande `devis-generation` du mandat).

Lancement : python3 -B calculs-devis-et-seuils-generations-v1.py CHEMIN/collisionneur_v9_v7.py
"""
import hashlib
import importlib.util
import math
import sys

sys.dont_write_bytecode = True

EMPREINTE_V7 = "319a7b66b5b975ccd1506def5e988e8bf3e0b8bb94afc6f2d6bd397829ae1724"
COMPOSITIONS = (
    ("cinq espèces (Fable, Opus, Argon, Astra, Carbon)", ["fable", "opus", "argon", "astra", "carbon"]),
    ("quatre espèces (Fable, Opus, Argon, Carbon)", ["fable", "opus", "argon", "carbon"]),
)
# Longueurs SUPPOSÉES, en caractères.
SOCLE = 20000          # préambule, faits, consigne et question d'un prompt
CONCEPTION = 30000     # une conception écrite du tour III.1
# Une réponse du tour III.3 transmise par l'état : 3 500 mots × 7 caractères (borne large de la commande `devis`) ; un
# milieu ; 14 401 jetons × 4,5 caractères (plus long texte de Carbon relevé par la réflexion d'Opus, section 3, à la borne
# CAR_SORTIE_MAX du script).
REPONSES = (24500, 45000, 65000)
# Une critique du tour III.2 transmise à son auteur : 3 000 mots × 7 ; un milieu ; même borne haute.
CRITIQUES = (21000, 45000, 65000)
# Plafond d'une pièce de l'état posé par la note (section 4.2) : la borne haute ci-dessus.
PIECE_MAX = 65000
# Rapport du développeur de la version 7, section 3.2, dossier « mathématiques » (cinq espèces, dix cellules à envoyer).
RAPPORT_V7 = {"tour2": 9.50, "tour3": 18.95, "avec_relances": 60.81}
# Seuils du plateau posés par la note (section 5).
SEUIL_RENOUVELLEMENT = 0.25
SEUIL_RENOUVELLEMENT_LIGNEE = 0.50
SEUIL_NEUVES = 0.15


def charger(chemin):
    """Importe le script de la version 7 après contrôle de son empreinte ; rien n'est exécuté hors des définitions."""
    with open(chemin, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != EMPREINTE_V7:
        sys.exit(f"empreinte du script inattendue : {h} (attendue {EMPREINTE_V7}) ; rien n'est calculé")
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v7", chemin)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["collisionneur_v9_v7"] = mod
    spec.loader.exec_module(mod)
    return mod


def pire(mod, m, caracteres, plafond):
    """Pire cas d'un envoi, à la manière de `devis-reprise` : entrée projetée à RATIO_PROJECTION_ENTREE caractères par
    jeton, plus la tolérance de la garde ; plafond de sortie et provision au prix de sortie."""
    garde = mod.garde_entree(math.ceil(caracteres / mod.RATIO_PROJECTION_ENTREE))
    return mod.cout_pire_garde(m, garde, plafond)


def calculer(mod, nom, especes):
    mod.fixer_composition(especes, nom_cle_anthropic="CLE_FACTICE")
    lettres, modeles = mod.LETTRES, mod.MODELES
    n = len(lettres)
    print(f"\n=== {nom} ===")
    print("1. Pire cas de sortie d'une cellule, USD (plafond + provision, au prix de sortie)")
    sortie = relance = 0.0
    for l in lettres:
        m = modeles[l]
        s = (m["max"] + m["provision"]) / 1e6 * m["prix"][1]
        r = (m["max_relance"] + m["provision"]) / 1e6 * m["prix"][1]
        sortie, relance = sortie + s, relance + r
        print(f"   {l} {m['espece']:7s} plafond {m['max']:6d}, relance {m['max_relance']:6d}, provision "
              f"{m['provision']:6d}, prix {m['prix'][0]:g} / {m['prix'][1]:g} : {s:.3f} (relance {r:.3f})")
    print(f"   par tour : {sortie:.3f} sans relance ; relances en plus : {relance:.3f}")

    autres = {l: [x for x in lettres if x != l] for l in lettres}
    borne_critique = {l: modeles[l]["max"] * mod.CAR_SORTIE_MAX[modeles[l]["fournisseur"]] for l in lettres}
    car2 = {l: SOCLE + sum(CONCEPTION + mod.SURCOUT_BLOC for _ in autres[l]) for l in lettres}
    car3 = {l: SOCLE + CONCEPTION + mod.SURCOUT_BLOC + sum(borne_critique[x] + mod.SURCOUT_BLOC for x in autres[l])
            for l in lettres}
    t2 = sum(pire(mod, modeles[l], car2[l], modeles[l]["max"]) for l in lettres)
    t3 = sum(pire(mod, modeles[l], car3[l], modeles[l]["max"]) for l in lettres)
    r23 = sum(pire(mod, modeles[l], c[l], modeles[l]["max"]) + pire(mod, modeles[l], c[l], modeles[l]["max_relance"])
              for c in (car2, car3) for l in lettres)
    print(f"2. Tours III.2 et III.3, toutes cellules à envoyer, longueurs supposées (socle {SOCLE}, conception "
          f"{CONCEPTION} caractères)")
    print(f"   tour III.2 {t2:.2f} + tour III.3 {t3:.2f} = {t2 + t3:.2f} USD sans relance ; {r23:.2f} avec relances")
    if n == 5:
        print(f"   rapport de la version 7 (mathématiques) : {RAPPORT_V7['tour2']:.2f} + {RAPPORT_V7['tour3']:.2f} = "
              f"{RAPPORT_V7['tour2'] + RAPPORT_V7['tour3']:.2f} sans relance ; {RAPPORT_V7['avec_relances']:.2f} avec "
              f"relances ; écart du recalcul : {100 * ((t2 + t3) / (RAPPORT_V7['tour2'] + RAPPORT_V7['tour3']) - 1):+.1f} % "
              f"et {100 * (r23 / RAPPORT_V7['avec_relances'] - 1):+.1f} %")

    base1 = sum(pire(mod, modeles[l], SOCLE, modeles[l]["max"]) for l in lettres)
    base1_rel = sum(pire(mod, modeles[l], SOCLE, modeles[l]["max_relance"]) for l in lettres)
    print(f"3. Tour III.1 sans état (comme à la génération 1) : {base1:.2f} USD sans relance ; relances en plus : "
          f"{base1_rel:.2f}")
    etats, critiques = [], []
    for longueur in REPONSES:
        avec = sum(pire(mod, modeles[l], SOCLE + n * (longueur + mod.SURCOUT_BLOC), modeles[l]["max"]) for l in lettres)
        jetons = math.ceil((SOCLE + n * (longueur + mod.SURCOUT_BLOC)) / mod.RATIO_PROJECTION_ENTREE)
        etats.append(avec - base1)
        print(f"   état de {n} réponses de {longueur} caractères : + {avec - base1:.2f} USD d'entrée au tour III.1 "
              f"({jetons} jetons d'entrée projetés par prompt)")
    for longueur in CRITIQUES:
        plus = sum(pire(mod, modeles[l], car2[l] + longueur + mod.SURCOUT_BLOC, modeles[l]["max"])
                   - pire(mod, modeles[l], car2[l], modeles[l]["max"]) for l in lettres)
        critiques.append(plus)
        print(f"   critique précédente de {longueur} caractères rendue à son auteur : + {plus:.2f} USD d'entrée au "
              f"tour III.2")

    print("4. Total au pire d'une génération à partir de la deuxième, USD")
    suite, suite_rel = (t2 + t3, r23)
    source = "recalcul"
    if n == 5:
        suite, suite_rel = RAPPORT_V7["tour2"] + RAPPORT_V7["tour3"], RAPPORT_V7["avec_relances"]
        source = "rapport de la version 7"
    for etiquette, e, c in (("bas", etats[0], critiques[0]), ("milieu", etats[1], critiques[1]),
                            ("haut", etats[2], critiques[2])):
        sans = base1 + e + suite + c
        avec = (base1 + e) + (base1_rel + e) + suite_rel + 2 * c
        print(f"   longueurs {etiquette:6s} : {sans:.2f} sans relance ; {avec:.2f} si chaque cellule était relancée "
              f"(tours III.2 et III.3 : {source})")
    print(f"   rappel, sans état ni critique rendue (une génération 1) : {base1 + suite:.2f} sans relance ; "
          f"{base1 + base1_rel + suite_rel:.2f} avec relances")

    # Borne stricte avant tout envoi : rien de la génération n'est écrit ; toute conception et toute critique est bornée
    # par le plafond de sortie de son auteur (comme `devis-reprise` borne une critique non écrite) ; chaque pièce de
    # l'état est au plafond de pièce de la note (section 4.2).
    s1 = {l: SOCLE + n * (PIECE_MAX + mod.SURCOUT_BLOC) for l in lettres}
    s2 = {l: SOCLE + sum(borne_critique[x] + mod.SURCOUT_BLOC for x in autres[l]) + PIECE_MAX + mod.SURCOUT_BLOC
          for l in lettres}
    s3 = {l: SOCLE + borne_critique[l] + mod.SURCOUT_BLOC + sum(borne_critique[x] + mod.SURCOUT_BLOC for x in autres[l])
          for l in lettres}
    stricts = [sum(pire(mod, modeles[l], c[l], modeles[l]["max"]) for l in lettres) for c in (s1, s2, s3)]
    strict_rel = sum(pire(mod, modeles[l], c[l], modeles[l]["max"]) + pire(mod, modeles[l], c[l], modeles[l]["max_relance"])
                     for c in (s1, s2, s3) for l in lettres)
    plus_long = max(math.ceil(c[l] / mod.RATIO_PROJECTION_ENTREE) for c in (s1, s2, s3) for l in lettres)
    print(f"4 bis. Borne stricte avant tout envoi (tout texte de la génération au plafond de sortie de son auteur, pièce "
          f"d'état à {PIECE_MAX} caractères)")
    print(f"   tour III.1 {stricts[0]:.2f} + tour III.2 {stricts[1]:.2f} + tour III.3 {stricts[2]:.2f} = "
          f"{sum(stricts):.2f} USD sans relance ; {strict_rel:.2f} avec relances ; plus long prompt projeté : "
          f"{plus_long} jetons d'entrée")
    return n


def seuils(n_lignees):
    print(f"\n5. Lecture des seuils en nombres d'entrées, {n_lignees} lignées")
    for par_lignee in (3, 4, 5, 6, 8):
        total = n_lignees * par_lignee
        print(f"   {par_lignee} entrées par lignée ({total} en tout) : plateau si au plus "
              f"{math.floor(SEUIL_RENOUVELLEMENT * total + 1e-9)} entrées touchées sur le cycle, au plus "
              f"{math.floor(SEUIL_RENOUVELLEMENT_LIGNEE * par_lignee + 1e-9)} dans une même lignée, au plus "
              f"{math.floor(SEUIL_NEUVES * total + 1e-9)} entrées neuves, premier choix tenu dans "
              f"{n_lignees - 1} lignées au moins")


def principal(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    mod = charger(argv[1])
    print(f"Script chargé : {mod.VERSION}, sha256 {EMPREINTE_V7}")
    print(f"Constantes lues dans le script : {mod.RATIO_PROJECTION_ENTREE:g} caractères par jeton d'entrée projeté, "
          f"tolérance de la garde {mod.TOLERANCE_COMPTE}, caractères par jeton de sortie au plus {mod.CAR_SORTIE_MAX}, "
          f"{mod.SURCOUT_BLOC} caractères de balises par pièce")
    tailles = [calculer(mod, nom, especes) for nom, especes in COMPOSITIONS]
    for n in sorted(set(tailles), reverse=True):
        seuils(n)


if __name__ == "__main__":
    principal(sys.argv)
