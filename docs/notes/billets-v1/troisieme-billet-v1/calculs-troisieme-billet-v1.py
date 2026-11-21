"""Calculs cités par `propositions-troisieme-billet-fable-v1.md` (troisième billet, candidat A :
la référence honnête).

Aucune donnée du programme n'est lue, aucun fichier n'est ouvert. Blocs A à D : lois normales
exactes. Bloc E : tirages ; graines par `numpy.random.SeedSequence`, dérivées par bloc et
écrites en sortie (R9). Tout est une illustration sous supposition écrite, pas une mesure.
Le bloc A refait, par un code écrit à part, les valeurs du bloc A de
`docs/notes/percee-controle-securite-v1/calculs-percee-controle-securite-v1.txt`.

Lancer : python calculs-troisieme-billet-v1.py > calculs-troisieme-billet-v1.txt
"""
import platform
from math import ceil, sqrt

import numpy as np
import scipy
from scipy.stats import norm

NIVEAU = 0.01
Z = norm.ppf(1.0 - NIVEAU)
RACINE = 2026112118  # graine racine de cette pièce (jour et heure UTC du mandat)
INFINI = float("inf")


def part_cachee(n, m, mu, puissance=0.5):
    """Plus grande part d'actes sabotés que le test unilatéral de niveau NIVEAU sur la
    moyenne de n actes surveillés, comparée à la moyenne de m scores honnêtes de référence,
    détecte avec une probabilité inférieure à `puissance`.
    Scores honnêtes N(0,1), sabotés N(mu,1), indépendants : la statistique centrée réduite
    suit N(f mu / sqrt(1/n + 1/m), 1)."""
    besoin = Z + norm.ppf(puissance)
    inverse_m = 0.0 if m == INFINI else 1.0 / m
    return min(1.0, besoin * sqrt(1.0 / n + inverse_m) / mu)


def ecart_depuis_aire(aire):
    """Écart mu entre un acte saboté et un acte honnête, en écarts types de l'honnête, pour un
    moniteur d'aire sous la courbe `aire`, sous lois normales de même variance."""
    return sqrt(2.0) * norm.ppf(aire)


def bloc_a():
    print("A. Part d'actes sabotés qui reste cachée (puissance < 0,5, niveau 1 %),")
    print("   sous supposition : un score par acte, honnête N(0,1), saboté N(mu,1), mu = 0,5,")
    print("   actes indépendants ; test sur la moyenne des n actes contre la moyenne de la référence.")
    mu = 0.5
    horizons = [100, 1_000, 10_000, 100_000, 1_000_000]
    for nom, m in [("référence exacte", INFINI), ("m = 400 fixe", 400), ("m = 2 000 fixe", 2_000)]:
        cases = " | ".join(f"n = {n:>9,} : {100 * part_cachee(n, m, mu):6.2f} %".replace(",", " ")
                           for n in horizons)
        print(f"   {nom:<18} | {cases}")
    for m in (400, 2_000, 10_000):
        print(f"   plancher à n infini, m = {m:>6} : z / (mu racine de m) = "
              f"{100 * Z / (mu * sqrt(m)):5.2f} %")
    print("   À n = m, la part cachée vaut racine de 2 fois son plancher ; allonger encore le")
    print(f"   déploiement ne la baisse plus que de {100 * (1 - 1 / sqrt(2)):.1f} % au mieux.")
    print("   À n = 4 m : " f"{100 * (sqrt(1.25) - 1):.1f} % au-dessus du plancher ; "
          "à n = 10 m : " f"{100 * (sqrt(1.1) - 1):.1f} %.")
    # Contrôle : l'objet où la conclusion doit être fausse (référence exacte : pas de plancher).
    rapport = part_cachee(1_000_000, INFINI, mu) / part_cachee(10_000, INFINI, mu)
    print(f"   Contrôle, référence exacte : part cachée à 10^6 actes / à 10^4 actes = {rapport:.4f}"
          " (attendu 0,1000 : loi en racine, aucun plancher).")
    rapport = part_cachee(1_000_000, 400, mu) / part_cachee(10_000, 400, mu)
    print(f"   Contrôle, m = 400 : le même rapport = {rapport:.4f} (attendu proche de 1 : plancher).")
    print()


def bloc_b():
    print("B. « Exactement » : à quelle précision faut-il connaître la moyenne honnête ?")
    print("   Sous supposition : lois normales de même variance (mu = racine de 2 fois le quantile")
    print("   normal de l'aire sous la courbe), actes indépendants, niveau 1 %, puissance 0,5.")
    print("   tolérance = p x mu : écart, en écarts types de l'honnête, que p d'actes sabotés")
    print("   ajoutent à la moyenne ; m_min = (z / (p mu))^2 : taille de référence sous laquelle")
    print("   la part p reste cachée à tout horizon (n infini). Avec une référence exacte, c'est")
    print("   aussi le nombre d'actes surveillés qu'il faut : les deux tailles jouent le même rôle.")
    aires = [0.60, 0.70, 0.77, 0.90, 0.95, 0.99]
    parts = [0.005, 0.01, 0.02, 0.05, 0.10]
    entete = "   aire   mu     | " + " | ".join(f"p = {100 * p:4.1f} %        " for p in parts)
    print(entete)
    for aire in aires:
        mu = ecart_depuis_aire(aire)
        cases = []
        for p in parts:
            tolerance = p * mu
            m_min = ceil((Z / tolerance) ** 2)
            cases.append(f"{tolerance:6.4f} ; {m_min:>9,}".replace(",", " "))
        print(f"   {aire:4.2f}  {mu:6.4f} | " + " | ".join(cases))
    print("   (chaque case : tolérance ; m_min.)")
    facteur = ((Z + norm.ppf(0.8)) / Z) ** 2
    print(f"   Pour une puissance de 0,8 au lieu de 0,5, multiplier m_min par {facteur:.3f}.")
    mu = ecart_depuis_aire(0.77)
    m_repere = f"{ceil((Z / (0.02 * mu)) ** 2):,}".replace(",", " ")
    print(f"   Repère cité dans la note : aire 0.77 et p = 2 % : tolérance {0.02 * mu:.4f} ; "
          f"m_min = {m_repere}.")
    print()


def bloc_c():
    print("C. Un écart systématique b entre l'honnête surveillé et sa référence ne se moyenne pas.")
    print("   Sous supposition : scores normaux de variance 1, indépendants ; test de niveau 1 %")
    print("   réglé comme si la référence était juste ; fausse alerte réelle sous l'honnête :")
    print("   Phi(-z + b / racine de (1/n + 1/m)).")
    ecarts = [0.01, 0.02, 0.05, 0.10]
    horizons = [100, 1_000, 10_000, 100_000]
    for nom, m in [("référence de moyenne connue, décalée de b", INFINI), ("m = 10 000, décalée de b", 10_000)]:
        print(f"   {nom}")
        for b in ecarts:
            cases = []
            for n in horizons:
                inverse_m = 0.0 if m == INFINI else 1.0 / m
                fausse = norm.cdf(-Z + b / sqrt(1.0 / n + inverse_m))
                cases.append(f"n = {n:>7,} : {fausse:6.4f}".replace(",", " "))
            print(f"     b = {b:4.2f} | " + " | ".join(cases))
    print("   Contrôle : b = 0,05, moyenne connue : 0.2281 à 1 000 actes et 0.9962 à 10 000 sont")
    print("   les deux valeurs du bloc A3 de la note du protocole X sur le contrôle diffus.")
    print("   Contrôle, b = 0 : fausse alerte = " f"{norm.cdf(-Z):.4f} (attendu 0,0100).")
    print()


def bloc_d():
    print("D. Deux sorties, et leur prix (sous les mêmes suppositions).")
    print("   Témoins honnêtes vérifiés, entrelacés à taux p (m = p n) : la loi en racine revient,")
    print("   multipliée par racine de (1 + 1/p).")
    for p in (0.01, 0.05, 0.20):
        print(f"     p = {p:4.2f} : facteur {sqrt(1.0 + 1.0 / p):5.2f}")
    print("   Nul par acte (rang parmi K tirages d'un jumeau de confiance sur le même début) :")
    print("   non recalculé ici ; voir le bloc C de la sortie citée en tête (efficacité 0,743 à")
    print("   K = 4 et 0,923 à K = 19, pour mu = 0,5).")
    print()


def bloc_e():
    print("E. Contrôles par tirages (graines écrites ; R9).")
    # E1 : le test sur la moyenne, à l'endroit où la formule annonce une puissance de 0,5.
    graine_e1 = np.random.SeedSequence([RACINE, 1])
    rng = np.random.default_rng(graine_e1)
    n, m, mu, repetitions = 2_000, 400, 0.5, 20_000
    k = round(part_cachee(n, m, mu) * n)
    seuil = Z * sqrt(1.0 / n + 1.0 / m)
    alertes_nul = 0
    alertes_sabotage = 0
    for _ in range(repetitions):
        reference = rng.standard_normal(m).mean()
        honnete = rng.standard_normal(n).mean()
        alertes_nul += (honnete - reference) > seuil
        reference = rng.standard_normal(m).mean()
        sabote = (rng.standard_normal(n).sum() + mu * k) / n
        alertes_sabotage += (sabote - reference) > seuil
    print(f"   E1 test sur la moyenne, n = {n}, m = {m}, mu = {mu}, {k} actes sabotés, "
          f"{repetitions} répétitions, graine [{RACINE}, 1] :")
    print(f"      fausse alerte {alertes_nul / repetitions:.4f} (attendu 0,01) ; "
          f"détection {alertes_sabotage / repetitions:.4f} (attendu 0,5 à l'arrondi de {k} actes près)")

    # E2 : le même plancher avec un test de rangs et une loi honnête à queues lourdes.
    print("   E2 test de rangs (Mann-Whitney, approximation normale du nul), loi honnête de Student")
    print("      à 3 degrés de liberté ; 10 % d'actes sabotés, décalés de 1 ; niveau 1 % ;")
    print("      4 000 répétitions par case ; graine [RACINE, 2, numéro de case].")
    part, decalage, repetitions = 0.10, 1.0, 4_000

    def taux_alerte(n, m, sabote, graine, repetitions):
        rng = np.random.default_rng(graine)
        ecart_type_nul = sqrt((n + m + 1) / (12.0 * n * m))
        k = round(part * n) if sabote else 0
        alertes = 0
        for _ in range(repetitions):
            reference = np.sort(rng.standard_t(3, size=m))
            surveille = rng.standard_t(3, size=n)
            surveille[:k] += decalage
            w = np.searchsorted(reference, surveille).mean() / m
            alertes += (w - 0.5) / ecart_type_nul > Z
        return alertes / repetitions

    case = 0
    for nom, regle in [("référence fixe, m = 400", lambda n: 400),
                       ("référence qui suit, m = n", lambda n: n)]:
        lignes_nul, lignes_sab = [], []
        for n in (400, 4_000, 40_000):
            m = regle(n)
            case += 1
            nul = taux_alerte(n, m, False, np.random.SeedSequence([RACINE, 2, case]), repetitions)
            case += 1
            sab = taux_alerte(n, m, True, np.random.SeedSequence([RACINE, 2, case]), repetitions)
            lignes_nul.append(f"n = {n:>6} : {nul:.4f}")
            lignes_sab.append(f"n = {n:>6} : {sab:.4f}")
        print(f"      {nom:<26} fausse alerte | " + " | ".join(lignes_nul))
        print(f"      {nom:<26} détection     | " + " | ".join(lignes_sab))
    print("      Lecture attendue, écrite avant le tirage : avec la référence fixe, la détection")
    print("      plafonne loin de 1 quand n est multiplié par cent ; avec la référence qui suit,")
    print("      elle tend vers 1. Le plancher ne tient donc ni à la loi normale ni au test sur la")
    print("      moyenne. Erreur type d'une case : au plus 0,008 (4 000 répétitions) ; 0,0016 pour")
    print("      une fausse alerte de 0,01.")

    # E3 : audit ajouté APRÈS lecture de E2 (règle de symétrie, R4). La case « référence fixe,
    # n = 400, fausse alerte » sortait à 0,0155, soit 3,5 erreurs types au-dessus de 0,01, alors
    # que la case jumelle (m = n = 400, autre graine) sortait à 0,0083. Même configuration,
    # dix fois plus de répétitions, trois graines neuves : si le test était mal réglé, les
    # trois valeurs resteraient au-dessus de 0,01.
    print("   E3 audit de la case de E2 sortie à 3,5 erreurs types (ajouté après lecture de E2) :")
    print("      n = m = 400, nul, 40 000 répétitions par graine, erreur type 0,0005.")
    valeurs = []
    for numero in (1, 2, 3):
        valeur = taux_alerte(400, 400, False, np.random.SeedSequence([RACINE, 3, numero]), 40_000)
        valeurs.append(valeur)
        print(f"      graine [{RACINE}, 3, {numero}] : fausse alerte {valeur:.4f}")
    print(f"      moyenne des trois : {sum(valeurs) / 3:.4f} (attendu 0,01). Lecture : le test est")
    print("      bien réglé ; la case de E2 est un écart de tirage, gardée telle quelle.")
    print()


def main():
    print("Calculs du troisième billet, candidat A (la référence honnête) - v1")
    print(f"Python {platform.python_version()}, numpy {np.__version__}, scipy {scipy.__version__}")
    print(f"Niveau {NIVEAU}, seuil unilatéral z = {Z:.4f} ; graine racine {RACINE}")
    print("Toutes les entrées sont des suppositions d'illustration ; aucune n'est une mesure.")
    print()
    bloc_a()
    bloc_b()
    bloc_c()
    bloc_d()
    bloc_e()


if __name__ == "__main__":
    main()
