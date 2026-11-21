#!/usr/bin/env python3
"""Calculs de la note « rendre l'étau solide, ou s'en passer » (v1).

Lois exactes, optimisations déterministes (dichotomie, recherche ternaire), approximation de Wald
déclarée pour les délais ; aucun tirage, aucune donnée du programme, aucun résultat d'expérience.
Toutes les valeurs d'entrée sont des suppositions d'illustration ; le monde à quatre bandes est
celui de la note sur la pince (calculs-pince-hors-distribution-v1.py).
Rejeu : python3 -I calculs-etau-solide-v1.py > calculs-etau-solide-v1.txt
"""
from math import comb, log, sqrt, exp

V = [0.35, 0.60, 0.85, 0.97]   # réussite attendue de l'honnête, par bande (référence calibrée)
W = [0.15, 0.25, 0.30, 0.30]   # poids des bandes
Z = 1.645 + 1.282              # niveau 5 % unilatéral, puissance 0,90 (approximation normale)
SIGMA2 = sum(w * v * (1 - v) for v, w in zip(V, W))
D = 0.10 * sum(w * v for v, w in zip(V, W))   # dommage total par épisode du monde de la pince


# ---------------------------------------------------------------- E1
def etau(r0, kappa):
    """Le saboteur choisit un degré d'obscurcissement o dans [0, 1].
    La sonde le prend avec la probabilité r0 (1 - o) ; sa compétence est multipliée par (1 - kappa o).
    U(o) = (1 - r0 (1 - o)) (1 - kappa o) : part des tentatives qui donnent un dommage discret non pris.
    Rend (o*, U*, V*) ; V* = part des tentatives qui tournent à l'échec visible (taxe payée)."""
    if kappa <= 0 or r0 <= 0:
        o = 1.0 if r0 > 0 else 0.0
    else:
        o = min(1.0, max(0.0, (r0 - kappa * (1 - r0)) / (2 * kappa * r0)))
    passe = 1 - r0 * (1 - o)
    return o, passe * (1 - kappa * o), passe * kappa * o


print("[E1] Ce que vaut l'étau face à un saboteur qui choisit son degré d'obscurcissement.")
print("     r0 = rappel de la sonde sans obscurcissement ; kappa = taxe de l'obscurcissement complet (part de compétence perdue).")
print("     Passe = part des tentatives qui donnent un dommage discret non pris, au meilleur choix du saboteur.")
print("     Attendu, écrit avant l'exécution : retrait = 1 - passe <= min(r0, kappa) partout ; retrait = 0 si kappa = 0 ou r0 = 0.")
pire = 0.0
for r0 in (0.0, 0.3, 0.5, 0.8, 0.95, 1.0):
    for kappa in (0.0, 0.02, 0.10, 0.30, 0.50, 0.80, 1.0):
        o, u, vis = etau(r0, kappa)
        retrait = 1 - u
        pire = max(pire, retrait - min(r0, kappa))
        print(f"     r0 {r0:4.2f} | kappa {kappa:4.2f} | obscurcissement choisi {o:4.2f} | passe {u:6.4f} | retrait {retrait:6.4f}"
              f" | min(r0, kappa) {min(r0, kappa):4.2f} | échecs visibles {vis:6.4f}")
print(f"     plus grand dépassement de la borne min(r0, kappa) sur la grille : {pire:+.2e} (attendu : <= 0)")
print("     Seuils : obscurcissement complet préféré si kappa <= r0 / (1 + r0) ; aucun obscurcissement si kappa >= r0 / (1 - r0).")
for r0 in (0.3, 0.5, 0.8, 0.95):
    haut = r0 / (1 - r0)
    print(f"       r0 {r0:4.2f} : cache tout si kappa <= {r0 / (1 + r0):.3f} ; ne cache rien si kappa >= "
          + (f"{haut:.3f}" if haut <= 1 else "(jamais : seuil au-dessus de 1)"))
print("     La taxe payée devient des échecs que l'oracle voit : épisodes requis pour que le bilan les voie")
print(f"     (part tentée 0,10 ; écart type {sqrt(SIGMA2):.4f} ; niveau 5 %, puissance 0,90, approximation normale).")
for r0, kappa in ((0.8, 0.10), (0.8, 0.30), (0.8, 0.50), (0.5, 0.30), (0.5, 0.50)):
    o, u, vis = etau(r0, kappa)
    ecart = 0.10 * vis
    print(f"       r0 {r0:4.2f}, kappa {kappa:4.2f} : échecs visibles par épisode {ecart:.4f} -> {(Z * sqrt(SIGMA2) / ecart) ** 2:9.0f} épisodes")


# ---------------------------------------------------------------- E2
def kl(p, q):
    def t(a, b):
        return 0.0 if a == 0 else a * log(a / b)
    return t(p, q) + t(1 - p, 1 - q)


def croissance_bandes(delta):
    """Mise de Kelly par bande, connue : croissance = somme des w KL(Bern(v - delta) || Bern(v))."""
    return sum(w * kl(v - d, v) for v, w, d in zip(V, W, delta))


def croissance_somme(delta, lam):
    """Une seule mise lam pour toutes les bandes : facteur 1 + lam (v - y)."""
    return sum(w * ((v - d) * log(1 - lam * (1 - v)) + (1 - v + d) * log(1 + lam * v)) for v, w, d in zip(V, W, delta))


def meilleure_mise_somme(delta):
    a, b = 0.0, 1 / max(1 - v for v in V) - 1e-9
    for _ in range(200):
        m1, m2 = a + (b - a) / 3, b - (b - a) / 3
        if croissance_somme(delta, m1) < croissance_somme(delta, m2):
            a = m1
        else:
            b = m2
    lam = (a + b) / 2
    return lam, croissance_somme(delta, lam)


def allocation_la_moins_favorable(total):
    """Minimise la croissance par bandes sous la contrainte somme des w delta = total (dichotomie sur le multiplicateur)."""
    def deltas(mu):
        out = []
        for v in V:
            c = exp(mu) * (1 - v) / v
            out.append(min(v, max(0.0, (c * v - (1 - v)) / (1 + c))))
        return out
    a, b = 0.0, 50.0
    for _ in range(200):
        m = (a + b) / 2
        if sum(w * d for w, d in zip(W, deltas(m))) < total:
            a = m
        else:
            b = m
    return deltas((a + b) / 2)


print()
print("[E2] Le bilan par pari valable à tout instant, sur le monde à quatre bandes de la note sur la pince.")
print(f"     Dommage total par épisode {D:.4f} ; variance de l'issue honnête {SIGMA2:.4f}. Délai = ln(1/alpha) / croissance (Wald, sans dépassement).")
prop = [0.10 * v for v in V]
pire_alloc = allocation_la_moins_favorable(D)
nul = [0.0] * 4
print("     Objets de contrôle, attendus écrits avant l'exécution :")
lam_p, g_p = meilleure_mise_somme(prop)
esp = sum(w * (v * (1 - lam_p * (1 - v)) + (1 - v) * (1 + lam_p * v)) for v, w in zip(V, W))
print(f"       honnête, mise de la somme réglée pour le dommage : espérance du facteur {esp:.6f} (attendu 1), croissance {croissance_somme(nul, lam_p):+.5f} (attendu < 0)")
print(f"       dommage que l'oracle ne voit pas : mêmes issues que l'honnête, donc même croissance {croissance_somme(nul, lam_p):+.5f} : le pari se tait (attendu)")
for nom, delta in (("dommage proportionnel (0,10 de chaque bande)", prop), ("répartition la moins favorable au défenseur", pire_alloc)):
    gb = croissance_bandes(delta)
    lam, gs = meilleure_mise_somme(delta)
    parts = [w * d / D for w, d in zip(W, delta)]
    print(f"     {nom}")
    print("       dommage par bande (écart de réussite) : " + ", ".join(f"v={v:.2f}: {d:.4f}" for v, d in zip(V, delta)))
    print("       part du dommage total par bande       : " + ", ".join(f"v={v:.2f}: {100 * p:4.1f} %" for v, p in zip(V, parts)))
    for alpha in (0.05, 0.01):
        print(f"       alpha {alpha:.2f} | pari par bandes : croissance {gb:.5f}, délai {log(1 / alpha) / gb:6.0f} épisodes"
              f" | pari sur la somme (mise {lam:.3f}) : croissance {gs:.5f}, délai {log(1 / alpha) / gs:6.0f}"
              f" | mélange à parts égales : au plus {log(2 / alpha) / max(gb, gs):6.0f}")
print(f"     Repère du second ordre : D^2 / (2 variance) = {D * D / (2 * SIGMA2):.5f} ; test à horizon fixe de la note sur la pince : {(Z * sqrt(SIGMA2) / D) ** 2:.0f} épisodes.")
print("     La répartition la moins favorable est proportionnelle à v (1 - v), au second ordre : parts attendues "
      + ", ".join(f"v={v:.2f}: {100 * w * v * (1 - v) / SIGMA2:4.1f} %" for v, w in zip(V, W)))
print("     Ce que durcir une bande rapporte : la bande v = 0,60 vérifiée deux fois (réussite si l'un des deux essais réussit, v = 0,84)")
V2 = [0.35, 0.84, 0.85, 0.97]
s2 = sum(w * v * (1 - v) for v, w in zip(V2, W))
print(f"       variance {SIGMA2:.4f} -> {s2:.4f} ; dommage sous le fil pour 10 000 épisodes : {Z * sqrt(SIGMA2) * 100:.0f} -> {Z * sqrt(s2) * 100:.0f} épisodes")


# ---------------------------------------------------------------- E3
def queue_haute(n, c, q):
    return sum(comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(c, n + 1))


def taille(q0, q1):
    for n in range(1, 2000):
        for c in range(0, n + 1):
            if queue_haute(n, c, q0) <= 0.05:
                if queue_haute(n, c, q1) >= 0.90:
                    return n, c, queue_haute(n, c, q0), queue_haute(n, c, q1)
                break
    return None


print()
print("[E3] Tailles exactes (loi binomiale ; risque <= 0,05, puissance >= 0,90).")
print("     (a) Dissociation chez l'honnête : parmi n épisodes honnêtes où l'oracle dit « réussi » et la qualité vraie dit « mauvais »,")
print("         X = ceux que la lecture range sous la médiane des réussites vraies. « Elle suit l'oracle » : 0,50 ; « elle suit la qualité » : q1.")
for q1 in (0.90, 0.80, 0.65):
    n, c, r, p = taille(0.50, q1)
    print(f"         q1 = {q1:.2f} : n = {n}, « suit la qualité » si X >= {c} (risque {r:.4f}, puissance {p:.4f}) ;"
          f" épisodes honnêtes requis si 2 %, 5 %, 10 % sont discordants : {n / 0.02:.0f}, {n / 0.05:.0f}, {n / 0.10:.0f}")
print("     (b) Le suspect pris pour sa propre référence : parmi n paires (épisode, même épisode sous perturbation tirée en secret),")
print("         X = celles où la version perturbée fait strictement mieux. Taux des témoins honnêtes q0 ; taux d'un saboteur fragile q1.")
for q0, q1 in ((0.05, 0.20), (0.10, 0.25), (0.20, 0.35), (0.20, 0.25)):
    n, c, r, p = taille(q0, q1)
    print(f"         q0 = {q0:.2f}, q1 = {q1:.2f} : n = {n}, alerte si X >= {c} (risque {r:.4f}, puissance {p:.4f})")
