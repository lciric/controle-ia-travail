"""Arithmétique du rédacteur du second cycle (accumulation des scores sur l'épisode) — v2.

Remplace la v1 pour les brouillons 2 (la v1 reste, R12). Change : débit de génération haut pris aux heures
réelles de la course exploratoire (42,8 s par épisode), instance parallèle chiffrée, plafonds et réserve,
disque de la relecture complémentaire par deux calculs, garde de spécificité par cellule et sur plusieurs
cellules, seuil du jumeau « différence d'état quelconque », volume de l'extraction des tâches fraîches.
Aucune donnée lue, aucune analyse. Bibliothèque standard. Lancement : python3 calculs-redaction-cycle-2-v2.py
"""
from math import comb, sqrt
from statistics import NormalDist

N = NormalDist()
z = N.inv_cdf


def taches(et64, m, alpha, puissance=0.80):
    return 64.0 * (et64 * (z(1 - alpha) + z(puissance)) / m) ** 2


def puissance(et64, m, alpha, n):
    return N.cdf(m / (et64 * sqrt(64.0 / n)) - z(1 - alpha))


def binom_cdf(x, n, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(x + 1))


def cp_haut(x, n, niveau=0.95):
    bas, haut = 0.0, 1.0
    for _ in range(80):
        mil = (bas + haut) / 2
        if binom_cdf(x, n, mil) > 1 - niveau:
            bas = mil
        else:
            haut = mil
    return haut


print("== 1. Effectifs (inchange depuis la v1 ; une sonde, quatre doses, queue divisee par deux : niveau 0,025/8)")
for et in (0.034, 0.038, 0.045):
    print(f"   et64={et:.3f} taches={taches(et, 0.05, 0.025 / 8):6.1f}",
          " ".join(f"P(n={n})={puissance(et, 0.05, 0.025 / 8, n):.3f}" for n in (400, 450, 500, 550, 600)))

print("== 2. Suite des cycles sous le nul commun (niveau 0,025 par cycle ; inchange)")
a = 0.025
for k in (2, 4, 10, 20, 40):
    print(f"   K={k:2d} sans correction {1 - (1 - a) ** k:.4f} ; avec replication K*a^2 = {k * a * a:.5f}")

print("== 3. Garde de specificite (formulation B) : par cellule, puis sur trois et six cellules (modes x types d'organisme)")
for n in (150, 200, 300, 400):
    xmax = max(x for x in range(n) if cp_haut(x, n) < 0.05)
    p1, p5 = binom_cdf(xmax, n, 0.01), binom_cdf(xmax, n, 0.05)
    print(f"   n={n} alertes tolerees={xmax} P(passe | 1 %)={p1:.3f} trois cellules={p1 ** 3:.3f} six cellules={p1 ** 6:.3f}"
          f" ; P(passe | 5 %)={p5:.3f}")
print("   calibrage d'un seuil a 1 % de faux positifs sur n episodes du temoin : episodes attendus au-dessus du seuil, P(aucun)")
for n in (100, 200, 300, 600):
    print(f"   n={n} attendus={0.01 * n:.0f} P(aucun negatif au-dessus du quantile 0,99 vrai)={0.99 ** n:.3f}")

print("== 3 bis. Epreuve plantee : seuils")
for T, c in ((100, 5), (200, 9)):
    print(f"   signal nul, T={T}, c={c} : P(X<=c | 0,025)={binom_cdf(c, T, 0.025):.3f} | 0,05 : {binom_cdf(c, T, 0.05):.3f}"
          f" | 0,075 : {binom_cdf(c, T, 0.075):.3f} ; borne indicative pour 0 fausse issue : {cp_haut(0, T):.4f}")
for c in (5, 9):
    print(f"   jumeau « difference d'etat quelconque », T=100, c={c} : P(X<=c | 0,05)={binom_cdf(c, 100, 0.05):.3f}"
          f" | 0,10 : {binom_cdf(c, 100, 0.10):.3f} | 0,20 : {binom_cdf(c, 100, 0.20):.3f}")

print("== 4. Devis de la famille neuve (bas : 40,2 s par episode, prix 1,0889 ; haut : 42,8 s, prix 1,30 ; pire cas : 42,8 s, deux fois plus lent, 1,40)")
S_BAS, S_HAUT, S_PASSE = 40.2, 42.8, 0.45
PRIX_BAS, PRIX_HAUT, PRIX_PIRE = 1.0889, 1.30, 1.40
DISQUE, DESCENTE, RESERVE = 0.08, 0.05, 0.5


def famille(n_eval, second_temoin, sans_episodes_temoin=False):
    cond = 9 - (4 if sans_episodes_temoin else 0)
    ep_dist, ep_eval = 2 * 32 * 5, cond * n_eval
    series = (2 if sans_episodes_temoin else 4) * 4 + 2 * 4 + 1 + (2 * 4 if second_temoin else 0)
    passes = series * n_eval
    echelle = 4 * 12 * 16 * (2 if second_temoin else 1)
    n_adapt = 3 if second_temoin else 2
    h_passe = (passes + echelle) * S_PASSE / 3600
    relecture = (h_passe * 0.35 / 0.15, h_passe * 0.55 / 0.15)
    jetons_m = passes * 2230 / 1e6
    notation = (0.1 * jetons_m / 4.1 * 2400 / 3200, 0.5 * jetons_m / 4.1 * 2400 / 3200)
    fixes_g, fixes_r = 2.0, 1.6
    g = ((ep_dist + ep_eval) * S_BAS / 3600 + 0.23 * n_adapt + fixes_g, (ep_dist + ep_eval) * S_HAUT / 3600 + 0.46 * n_adapt + fixes_g)
    r = (relecture[0] + notation[0] + fixes_r, relecture[1] + notation[1] + fixes_r)
    return dict(ep_eval=ep_eval, passes=passes + echelle, g=g, r=r, h_passe=h_passe, relecture=relecture, notation=notation,
                h_eval=(ep_eval * S_BAS / 3600, ep_eval * S_HAUT / 3600), h_dist=(ep_dist * S_BAS / 3600, ep_dist * S_HAUT / 3600))


for nom, n_eval, st, sans in (("400 taches, un temoin", 400, False, False), ("400 taches, second temoin", 400, True, False),
                              ("500 taches, second temoin", 500, True, False), ("600 taches, second temoin", 600, True, False),
                              ("variante sans episodes du temoin, 400 taches", 400, False, True)):
    f = famille(n_eval, st, sans)
    g, r = f["g"], f["r"]
    bas = (g[0] + r[0]) * PRIX_BAS + DISQUE * (g[0] + r[0]) + 2 * 20 * DESCENTE
    haut = (g[1] + r[1]) * PRIX_HAUT + DISQUE * (g[1] + r[1] + 2.0) + 2 * 40 * DESCENTE
    cg = 2 * g[1] * PRIX_PIRE + DISQUE * (2 * g[1] + 1.0) + 40 * DESCENTE
    cr = 2 * r[1] * PRIX_PIRE + DISQUE * (2 * r[1] + 1.0) + 40 * DESCENTE
    par = 2 * 1.6 * PRIX_PIRE + DISQUE * 2 * 1.6 + 40 * DESCENTE
    print(f"   -- {nom}")
    print(f"      episodes d'evaluation {f['ep_eval']} ({f['h_eval'][0]:.2f} a {f['h_eval'][1]:.2f} h) ; distillation, donnees {f['h_dist'][0]:.2f} a {f['h_dist'][1]:.2f} h ;"
          f" passes {f['passes']} ({f['h_passe']:.2f} h de passe) ; relecture {f['relecture'][0]:.2f} a {f['relecture'][1]:.2f} h ; notation {f['notation'][0]:.2f} a {f['notation'][1]:.2f} h")
    print(f"      piece de generation {g[0]:.1f} a {g[1]:.1f} h ; piece de relecture {r[0]:.1f} a {r[1]:.1f} h ; total {g[0] + r[0]:.1f} a {g[1] + r[1]:.1f} h"
          f" ({(g[0] + r[0]) / 24:.1f} a {(g[1] + r[1]) / 24:.1f} jours)")
    print(f"      attendu {bas:.1f} a {haut:.1f} USD ; pire cas P1 {cg + cr:.1f} USD (generation {cg:.1f} ; relecture {cr:.1f}) ;"
          f" avec la reserve de {RESERVE} USD : {cg + cr + RESERVE:.1f} ; avec une seconde instance de generation : {cg + cr + par + RESERVE:.1f}")
    print(f"      part du temps : generation d'evaluation {f['h_eval'][0] / (g[0] + r[0]):.2f} a {f['h_eval'][1] / (g[1] + r[1]):.2f} ;"
          f" piece de generation entiere {g[0] / (g[0] + r[0]):.2f} a {g[1] / (g[1] + r[1]):.2f}")
print(f"   seconde instance de generation : attendu {1.6 * PRIX_BAS + DISQUE * 1.6 + 20 * DESCENTE:.1f} a {1.6 * PRIX_HAUT + DISQUE * 1.6 + 40 * DESCENTE:.1f} USD ;"
      f" pire cas {2 * 1.6 * PRIX_PIRE + DISQUE * 2 * 1.6 + 40 * DESCENTE:.1f} USD")
f = famille(400, False)
print(f"   facteur de relecture : ici 2,3 a 3,7 fois le temps de passe (devis de l'etape B bis, ecriture des activations comprise) ;"
      f" a 1,14 fois (validite de l'adaptateur : 0,35 h de passe + 0,05 h de garde) la relecture a 400 taches vaudrait {f['h_passe'] * 0.40 / 0.35:.2f} h au lieu de {f['relecture'][0]:.2f} a {f['relecture'][1]:.2f} h")

print("== 5. Relecture complementaire du temps 1 (donnees de developpement ; ligne a part)")
serie_bbis = 576 + 256 + 64 + 256 + 64
texte_egal = 4 * 64 * 2          # quatre doses x 64 taches x deux cellules croisees (texte du saboteur sous l'etat temoin, et l'inverse)
temoin_distille = 4 * 64 * 4     # quatre doses x 64 taches x quatre series du temoin distille honnete (si sa piece existe)
passes_t1 = serie_bbis + texte_egal + temoin_distille
h_passe = passes_t1 * S_PASSE / 3600
marche = (1.0 + 0.5 + 0.05 + h_passe * 0.35 / 0.15 + 0.05 + 1.0 + 0.2, 1.0 + 0.5 + 0.05 + h_passe * 0.55 / 0.15 + 0.05 + 6.0 + 0.4)
att = (marche[0] * PRIX_BAS + DISQUE * marche[0] + 20 * DESCENTE, marche[1] * PRIX_HAUT + DISQUE * (marche[1] + 1) + 40 * DESCENTE)
p1 = 2 * marche[1] * PRIX_PIRE + DISQUE * (2 * marche[1] + 1) + 2
p2 = 2 * (2 * marche[1] * PRIX_PIRE + DISQUE * 2 * marche[1]) + 4
garde_jour = DISQUE * 24
print(f"   passes : {serie_bbis} (series de l'etape B bis) + {texte_egal} (cellules croisees a texte egal) + {temoin_distille} (series du temoin distille honnete, si elles existent) = {passes_t1} ;"
      f" sans le temoin distille : {serie_bbis + texte_egal}")
print(f"   {h_passe:.3f} h de passe ; marche {marche[0]:.1f} a {marche[1]:.1f} h ; attendu hors garde {att[0]:.1f} a {att[1]:.1f} USD ; pire cas P1 {p1:.1f} USD ; avec une relance entiere {p2:.1f} USD")
print(f"   garde de l'instance arretee : {garde_jour:.2f} USD par jour ; cinq jours {5 * garde_jour:.1f} ; sept jours {7 * garde_jour:.1f}")
print(f"   lecture alpha : P1 + cinq jours de garde = {p1 + 5 * garde_jour:.1f} USD (plafond 40) ; lecture beta : relance entiere + sept jours = {p2 + 7 * garde_jour:.1f} USD (plafond 75)")
mo_passe = 2230 * 4096 * 2 / 1e6
print(f"   disque, calcul 1 (prorata des 49 Go de l'etape B bis pour 1 216 passes) : {passes_t1 * 49 / 1216:.0f} Go ;"
      f" calcul 2 ({mo_passe:.1f} Mo par passe et par couche, etude des organismes) : {passes_t1 * mo_passe / 1000:.0f} Go par couche, {3 * passes_t1 * mo_passe / 1000:.0f} Go pour trois couches ;"
      f" rapport des deux : {49 / 1216 * 1000 / (3 * mo_passe):.2f}")

print("== 6. Recoupement des debits (inchange) : 6,85 h pour 576 episodes = %.1f s par episode" % (6.85 * 3600 / 576))

print("== 7. Taches fraiches : volume de l'extraction (0 USD de carte)")
for n in (400, 500, 600):
    P = round((n + 32) * 1.2)
    print(f"   {n} taches : {n + 32} papiers gardes apres extraction ; {P} gardes par la selection avec 20 % de reserve (hypothese sans source) ;"
          f" lancements de sous-agents {P * 1.10 + 20:.0f} a {P * 1.30 + 20:.0f} (part invalide a la premiere tentative 0,10 a 0,30, hypothese sans source ; hors reprises) ;"
          f" caracteres lus a la premiere tentative {P * 90229 / 1e6:.0f} millions ; rendement minimal de la selection {P / 3309:.3f}")

print("== 8. Calendrier : durees des etapes sur carte (jours de marche)")
f4, f6 = famille(400, True), famille(600, True)
print(f"   relecture complementaire du temps 1 : {marche[0] / 24:.1f} a {marche[1] / 24:.1f} jour de marche")
print(f"   famille neuve, une instance : {(f4['g'][0] + f4['r'][0]) / 24:.1f} a {(f6['g'][1] + f6['r'][1]) / 24:.1f} jours ;"
      f" deux instances de generation : {(f4['g'][0] / 2 + f4['r'][0]) / 24:.1f} a {(f6['g'][1] / 2 + f6['r'][1]) / 24:.1f} jours")
