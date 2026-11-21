"""Calculs de la note « mécanisme adjudant hors distribution » (v1).

Lois exactes ou programmation dynamique exacte ; bibliothèque standard seule ; aucun tirage, aucune donnée du programme.
Chaque bloc porte une lettre, citée entre crochets dans la note. Toutes les valeurs d'entrée sont des suppositions
d'illustration, écrites ici ; aucune n'est une mesure.
"""
import math
from statistics import NormalDist

N01 = NormalDist()
ALPHA = 0.01


def binom_cdf(c, n, r):
    """P(X <= c) pour X binomiale(n, r), somme exacte."""
    return sum(math.comb(n, k) * r**k * (1 - r) ** (n - k) for k in range(0, c + 1))


def bloc_a():
    print("[A] Borne des deux lois : sur un canal où l'attaquant ne déplace la statistique lue que de delta écarts types")
    print("    (lois normales, variances égales), aucune règle au niveau 1 % ne dépasse la puissance du test de Neyman-Pearson.")
    z = N01.inv_cdf(1 - ALPHA)
    for delta in (0.0, 0.1, 0.25, 0.446, 1.0, 2.0, 3.0):
        puissance = 1 - N01.cdf(z - delta)
        vt = 2 * N01.cdf(delta / 2) - 1
        print(f"    delta = {delta:5.3f} : puissance maximale {puissance:6.4f} ; distance en variation totale {vt:6.4f} ; "
              f"borne alpha + distance {min(1.0, ALPHA + vt):6.4f}")


def bloc_b():
    print("[B] Plancher d'audit, cas où un seul dommage reconnu suffit (l'honnête n'en commet jamais) :")
    print("    audit tiré au hasard avec probabilité p, oracle qui reconnaît un dommage regardé avec probabilité q.")
    for p in (0.01, 0.02, 0.05, 0.10, 0.20):
        for q in (1.0, 0.5):
            pq = p * q
            moyenne = (1 - pq) / pq
            k95 = math.ceil(math.log(0.05) / math.log(1 - pq))
            print(f"    p = {p:4.2f}, q = {q:3.1f} : épisodes endommagés avant la première prise, en moyenne {moyenne:7.1f} ; "
                  f"prise avec probabilité 0,95 au plus tard au {k95}e épisode endommagé")


def pari_melange(d0, d1, horizon, grille=20):
    """Pari de Bernoulli contre un taux de dommage honnête d0 sur les épisodes audités.

    Richesse = moyenne, sur une grille de mises m entre 0 et 1/d0 (exclu), des produits de (1 + m (x - d0)).
    Elle ne dépend que du nombre n d'audits et du nombre k de dommages : programmation dynamique exacte sur (n, k).
    Rend la probabilité d'alarme (richesse >= 1/ALPHA) avant l'horizon sous d0 et sous d1, et le temps médian sous d1.
    """
    mises = [(j + 0.5) / grille / d0 for j in range(grille)]
    log_plus = [math.log1p(m * (1 - d0)) for m in mises]
    log_moins = [math.log1p(-m * d0) for m in mises]
    seuil = math.log(1 / ALPHA)

    def alarme(n, k):
        logs = [k * a + (n - k) * b for a, b in zip(log_plus, log_moins)]
        top = max(logs)
        return top + math.log(sum(math.exp(v - top) for v in logs) / grille) >= seuil

    resultats = {}
    for nom, d in (("honnête", d0), ("saboteur", d1)):
        vivants = {0: 1.0}
        cumul = 0.0
        mediane = None
        for n in range(1, horizon + 1):
            suivants = {}
            for k, masse in vivants.items():
                for kk, pr in ((k + 1, d), (k, 1 - d)):
                    if alarme(n, kk):
                        cumul += masse * pr
                    else:
                        suivants[kk] = suivants.get(kk, 0.0) + masse * pr
            vivants = suivants
            if mediane is None and cumul >= 0.5:
                mediane = n
        resultats[nom] = (cumul, mediane)
    return resultats


def bloc_c():
    print("[C] Plancher d'audit, cas d'excès : l'honnête produit aussi des dommages (taux d0 par épisode audité) ;")
    print("    pari de Bernoulli en mélange sur les seuls épisodes audités, alarme quand la richesse atteint 100 (risque 1 %).")
    d0 = 0.10
    for d1, horizon in ((0.15, 3000), (0.20, 1500), (0.30, 600)):
        r = pari_melange(d0, d1, horizon)
        fa, _ = r["honnête"]
        puissance, med = r["saboteur"]
        print(f"    d0 = {d0:4.2f}, d1 = {d1:4.2f}, horizon {horizon} audits : fausse alarme {fa:6.4f} ; alarme {puissance:6.4f} ; "
              f"nombre médian d'audits avant l'alarme {med}")
        if med is not None:
            for p in (0.05, 0.20, 1.00):
                episodes = med / p
                print(f"        audit à p = {p:4.2f} : {episodes:8.0f} épisodes de déploiement, soit {episodes * (d1 - d0):7.0f} "
                      f"épisodes endommagés en excès avant l'alarme (médiane)")


def bloc_d():
    print("[D] Recapture : parmi n épisodes endommagés trouvés par l'audit au hasard, X = ceux que le moniteur avait signalés.")
    print("    (i) règle « aucun signalé » : plus petit n tel qu'un moniteur de rappel r0 n'en signale aucun avec probabilité <= 0,05.")
    for r0 in (0.128, 0.25, 0.50, 0.80):
        n = math.ceil(math.log(0.05) / math.log(1 - r0))
        print(f"        rappel validé r0 = {r0:5.3f} : n = {n}")
    print("    (ii) règle à seuil : plus petits n et c tels que P(X <= c | r0) <= 0,05 et P(X <= c | r1) >= 0,90.")
    for r0, r1 in ((0.80, 0.20), (0.50, 0.10), (0.50, 0.25), (0.128, 0.02)):
        trouve = None
        for n in range(1, 400):
            for c in range(0, n + 1):
                if binom_cdf(c, n, r0) <= 0.05 and binom_cdf(c, n, r1) >= 0.90:
                    trouve = (n, c)
                    break
            if trouve:
                break
        if trouve is None:
            print(f"        r0 = {r0:5.3f}, r1 = {r1:5.3f} : pas de règle avant n = 400")
            continue
        n, c = trouve
        print(f"        r0 = {r0:5.3f}, r1 = {r1:5.3f} : n = {n}, « moniteur invalide » si X <= {c} "
              f"(risque {binom_cdf(c, n, r0):6.4f}, puissance {binom_cdf(c, n, r1):6.4f})")
        for p, f in ((0.05, 0.10), (0.20, 0.20), (1.00, 0.50)):
            print(f"            audit p = {p:4.2f}, part d'épisodes endommagés f = {f:4.2f} : de l'ordre de {n / (p * f):7.0f} épisodes")


def bloc_e():
    print("[E] Deux regards, chacun aveugle à une attaque nouvelle avec probabilité m ; corrélation rho de leurs pannes.")
    print("    Probabilité que les deux soient aveugles ensemble : m^2 + rho m (1 - m).")
    for m in (0.5, 0.8):
        rho_min = -min(m / (1 - m), (1 - m) / m)
        for rho in (0.0, 0.5, 0.9, rho_min):
            conjoint = m * m + rho * m * (1 - m)
            marque = " (corrélation la plus négative possible : dilemme)" if rho == rho_min else ""
            print(f"    m = {m:3.1f}, rho = {rho:5.2f} : {max(0.0, conjoint):6.4f}{marque}")
    print("    Regards indépendants : m^k ; pour m = 0,5 il en faut 7 pour passer sous 1 % ; pour m = 0,8, 21.")
    for m in (0.5, 0.8):
        k = math.ceil(math.log(0.01) / math.log(m))
        print(f"    m = {m:3.1f} : k = {k}, m^k = {m**k:6.4f}")


if __name__ == "__main__":
    for bloc in (bloc_a, bloc_b, bloc_c, bloc_d, bloc_e):
        bloc()
        print()
