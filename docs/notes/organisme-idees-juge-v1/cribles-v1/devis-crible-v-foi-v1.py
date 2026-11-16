"""Devis, durées, borne par appel et garde de départ du crible (v), version qui fera foi v1.

Applique les règles écrites d'avance du brouillon 9 (`crible-v-brouillon9.md`,
c574e39d700aaff64c59efd0319aaf565c906ff2518304c6c2f2a752dcd5da23) : section « Devis »
(règle d'avance du devis refait (a) à (d), règle de B_a puis de M, budget de pire cas),
section « Taille » (probabilité d'atteindre le minimum, à titre d'information), ligne
« coût d'un appel » de la liste d'arrêt (tolérance de la réflexion de Pr-1).

Entrées : recopiées à la main de la seule section « Pour les cribles » du verdict du
pilote MR-2 v14 (transmise par la consigne de la mère), et des lignes 478 à 480 de
`registres/depenses.md` (base des prix des montants : prix de la configuration).
Aucune donnée lue par ce programme : bibliothèque standard seule, arithmétique exacte
(fractions), aucun tirage, aucun appel, aucune dépense.
"""

from fractions import Fraction as F
from math import comb, ceil

def D(x):
    return F(str(x))

def usd(x, n=6):
    return f"{float(x):.{n}f}"

print("Devis du crible (v), version qui fera foi v1 — sortie")
print()

# ---------------------------------------------------------------- 1. coûts du pilote
# Montants au prix de la configuration v12 (registre des dépenses, l. 479-480 :
# « prix de la configuration, la console de Lazar fait foi »).
cout_config = {
    "Pr-1 argon": D("2.471620"),
    "Pr-2 opus55": D("1.057336"),
    "Pr-3 astra": D("1.671750"),
    "Pr-4 fable52": D("10.019552"),
}
appels = {k: 4 for k in cout_config}
machine_pilote = D("0.082018")
epreuve_cles = D("0.001164")      # registre, l. 480
machine_v13 = D("0.074757")       # registre, l. 480
total_rapproche = D("15.378197")
somme = sum(cout_config.values()) + machine_pilote
print("1. Rapprochement des montants transmis")
print(f"  quatre proposeurs + machine 60918148 : {usd(somme)} USD")
print(f"  + épreuve des clés {usd(epreuve_cles)} + machine v13 {usd(machine_v13)} : "
      f"{usd(somme + epreuve_cles + machine_v13)} USD ; total transmis {usd(total_rapproche)} ; "
      f"écart {usd(somme + epreuve_cles + machine_v13 - total_rapproche)}")
print()

# Rapport prix de la configuration / prix public, par proposeur (entrée et sortie,
# USD par million) : Pr-1 10/50 contre 2/10 jusqu'au 30 novembre (rapport 5 aux deux) ;
# Pr-2 4/20, Pr-3 10/50, Pr-4 8/40 : égaux (rapport 1).
rapport_cfg_pub = {"Pr-1 argon": F(5), "Pr-2 opus55": F(1), "Pr-3 astra": F(1), "Pr-4 fable52": F(1)}
cout_public = {k: v / rapport_cfg_pub[k] for k, v in cout_config.items()}

print("2. Attendu par appel = moyenne des coûts de tous les appels du pilote (règle (b))")
moy_pub, moy_cfg = {}, {}
for k in cout_config:
    moy_cfg[k] = cout_config[k] / appels[k]
    moy_pub[k] = cout_public[k] / appels[k]
    print(f"  {k:13s} : {appels[k]} appels ; total public {usd(cout_public[k])} ; "
          f"moyenne publique {usd(moy_pub[k])} ; moyenne configuration {usd(moy_cfg[k])} USD")
tronq = D("5.585992")
compl = cout_config["Pr-4 fable52"] - tronq
print(f"  Pr-4 : deux tronqués {usd(tronq)} (moyenne {usd(tronq / 2)}), deux complets {usd(compl)} "
      f"(moyenne {usd(compl / 2)}) ; plafond de session 3,00")
print("  fourchette par appel (plus petit, plus grand coût d'un appel) : coûts par appel non transmis ;"
      " bornes seules : plus petit <= moyenne <= plus grand")
print()

N = 20
credits = ["Pr-2 opus55", "Pr-4 fable52"]
hors = ["Pr-1 argon", "Pr-3 astra"]
print(f"3. Attendu du crible, N = {N} mondes, 4 N = {4 * N} appels (proposeurs seuls)")
for nom, moy in (("prix public", moy_pub), ("prix de la configuration", moy_cfg)):
    c = N * sum(moy[k] for k in credits)
    h = N * sum(moy[k] for k in hors)
    print(f"  {nom:24s} : par proposeur " + " ; ".join(f"{k.split()[0]} {usd(N * moy[k], 4)}" for k in cout_config)
          + f" ; crédits {usd(c, 4)} ; hors crédits {usd(h, 4)} ; total {usd(c + h, 4)} ; part sur crédits {usd(c / (c + h), 4)}")
print()

# ---------------------------------------------------------------- 4. durées
dur = {  # monde -> proposeur -> secondes (relevé), et tronqué ou non
    1: {"argon": D("96.004"), "astra": D("80.106"), "fable52": D("388.807"), "opus55": D("109.396")},
    2: {"argon": D("38.287"), "astra": D("61.164"), "fable52": D("430.542"), "opus55": D("54.737")},
    3: {"argon": D("75.664"), "astra": D("78.847"), "fable52": D("553.242"), "opus55": D("72.991")},
    4: {"argon": D("47.464"), "astra": D("34.411"), "fable52": D("510.008"), "opus55": D("36.425")},
}
tronques = {(3, "fable52"), (4, "fable52")}
repondus = [(w, p, s) for w, d in dur.items() for p, s in d.items() if (w, p) not in tronques]
assert len(repondus) == 14
plus_long_rep = max(repondus, key=lambda t: t[2])
print("4. Borne par appel B_a (règle : plus petit multiple de 300 s >= 1,5 x plus long appel répondu, au plus 3 600 s)")
print(f"  plus long appel répondu : monde {plus_long_rep[0]}, {plus_long_rep[1]}, {usd(plus_long_rep[2], 3)} s ;"
      f" 1,5 x = {usd(F(3, 2) * plus_long_rep[2], 4)} s")
B_a = 300 * ceil(F(3, 2) * plus_long_rep[2] / 300)
assert B_a <= 3600
print(f"  B_a = {B_a} s")
plus_long_tout = max(s for d in dur.values() for s in d.values())
print(f"  plus long appel du pilote, tronqués compris : {usd(plus_long_tout, 3)} s ; appels du pilote au-delà de B_a : "
      f"{sum(1 for d in dur.values() for s in d.values() if s > B_a)}")
print()

print("5. Taux d'appels répondus du pilote lu avec cette B_a (section « Taille », à titre d'information)")
n_rep, n_tr, n_ech = 14, 2, 0
r = F(n_rep, n_rep + n_tr + n_ech)
print(f"  répondus {n_rep}, tronqués {n_tr}, en échec {n_ech} (aucun au-delà de B_a) : r = {n_rep}/16 = {usd(r, 4)}")
def p_complet(ra, rb, rc, rd):
    # monde complet : au moins un appel répondu dans chaque moitié (b = Pr-1, Pr-2 ; e = Pr-3, Pr-4)
    return (1 - (1 - ra) * (1 - rb)) * (1 - (1 - rc) * (1 - rd))
def p_au_moins(k, n, p):
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))
pc = p_complet(r, r, r, r)
print(f"  taux commun r : P(monde complet) = {usd(pc, 4)} ; P(monde à quatre appels) = {usd(r ** 4, 4)} ;"
      f" P(n_c >= 16 sur 20) = {usd(p_au_moins(16, 20, pc), 4)}")
rp = {"argon": F(4, 4), "opus55": F(4, 4), "astra": F(4, 4), "fable52": F(2, 4)}
pc2 = p_complet(rp["argon"], rp["opus55"], rp["astra"], rp["fable52"])
print(f"  taux par proposeur (4 appels chacun ; Pr-1 1, Pr-2 1, Pr-3 1, Pr-4 1/2) : P(monde complet) = {usd(pc2, 4)} ;"
      f" P(monde à quatre appels) = {usd(rp['argon'] * rp['opus55'] * rp['astra'] * rp['fable52'], 4)} ;"
      f" P(n_c >= 16 sur 20) = {usd(p_au_moins(16, 20, pc2), 4)}")
print("  (appels indépendants supposés ; l'abandon d'un fournisseur après une panne de relais n'est pas compté)")
print()

print("6. Budget de pire cas (règle de la section « Devis ») : barrières 6 000 s + 3 x (mise en place +")
print("   génération de 20 mondes + mesure de 20 mondes + rapatriement) + 3 x énumération du placebo + ceil(20/M) x B_a <= 61 200 s")
print("   Les quatre durées du journal d'états ne sont pas dans la section transmise : D = leur somme plus l'énumération ;")
print("   pour chaque case, plus grande valeur de D qui tient sous 17 h (D_max) ; D_max < 0 : non lançable quel que soit D")
barr = 100 * 60
plafond = 17 * 3600
grille = sorted({B_a, 1800, 2400, 3000, 3600})
for b in grille:
    cases = []
    for M in (1, 2):
        reste = plafond - barr - ceil(F(N, M)) * b
        dmax = F(reste, 3)
        cases.append(f"M = {M} : appels {ceil(F(N, M)) * b} s, D_max = {usd(dmax, 1)} s ({usd(dmax / 3600, 3)} h)"
                     if reste >= 0 else f"M = {M} : appels {ceil(F(N, M)) * b} s, non lançable")
    print(f"  B_a = {b:4d} s{' (règle)' if b == B_a else ''} : " + " ; ".join(cases))
print("  M retenu (règle) : 1 si D <= D_max(B_a, M = 1), sinon 2 si D <= D_max(B_a, M = 2), sinon « non lançable » et mot de la mère")
print()

print("7. Machine dans l'attendu (règle (b)) : termes sans le facteur trois, appels à ceil(N/M) x moyenne, sur les mondes")
print("   du pilote, du plus long des quatre appels d'un monde (au plus B_a), x prix horaire relu")
plus_long_monde = {w: min(max(d.values()), B_a) for w, d in dur.items()}
moy_pl = sum(plus_long_monde.values()) / len(plus_long_monde)
print("  plus long appel par monde : " + " ; ".join(f"{w} : {usd(s, 3)} s" for w, s in plus_long_monde.items())
      + f" ; moyenne {usd(moy_pl, 5)} s")
prix_h = D("0.052222")
for M in (1, 2):
    t_app = ceil(F(N, M)) * moy_pl
    t_conn = barr + t_app
    print(f"  M = {M} : appels {usd(t_app, 3)} s ; avec les barrières {usd(t_conn / 3600, 4)} h, soit {usd(t_conn / 3600 * prix_h, 6)} USD"
          f" (sans les quatre durées non relevées) ; borne haute à 17 h : {usd(17 * prix_h, 6)} USD")
somme_par_monde = sum(max(d.values()) for d in dur.values())
print(f"  somme sur les 4 mondes du plus long appel : {usd(somme_par_monde, 3)} s ; manifeste du run 12:14:34 -> 12:59:07 = 2673 s ;"
      f" écart {usd(2673 - somme_par_monde, 3)} s (information, non compté par la règle)")
print()

print("8. Tolérance de la réflexion de Pr-1 (ligne « coût d'un appel ») : n'existe que si le plus grand rapport")
print("   coût compté / plafond (2,34) mesuré sur les appels de Pr-1 du pilote dépasse 1")
pl1 = D("2.34")
print(f"  total compté de Pr-1 sur 4 appels {usd(cout_config['Pr-1 argon'])} ; moyenne {usd(moy_cfg['Pr-1 argon'])} ; "
      f"rapport moyen {usd(moy_cfg['Pr-1 argon'] / pl1, 4)} ; rapport par appel non transmis")
print(f"  pour qu'un appel dépasse 2,34, les trois autres devraient coûter ensemble au plus {usd(cout_config['Pr-1 argon'] - pl1)} USD")
print("  aucun dépassement observé dans la section transmise : tolérance non retenue, l'arrêt reste (règle écrite)")
print()

print("9. Pires cas (règle (a), inchangés) et enveloppe de GO-2026-11-15-06 (1 275 USD au pire)")
plaf = {"Pr-1": D("2.34"), "Pr-2": D("2.00"), "Pr-3": D("2.34"), "Pr-4": D("3.00")}
pire = {k: N * v for k, v in plaf.items()}
kv1 = pire["Pr-2"] + pire["Pr-4"] + D("4.39")
kv2 = pire["Pr-1"] + pire["Pr-3"] + D("3.00") + D("3.68")
print(f"  kv1 (crédits) {usd(kv1, 2)} ; kv2 (hors crédits) {usd(kv2, 2)} ; total {usd(kv1 + kv2, 2)} USD")
engage = F(0)
print(f"  lignes « calcul » déjà inscrites sous GO-2026-11-15-06 : 0 ; dépense déjà portée : {usd(engage, 2)}")
print(f"  ce crible seul : {usd(engage + kv1 + kv2, 2)} <= 1275 : {engage + kv1 + kv2 <= 1275}")
iii = D("263") + D("7")
print(f"  avec le crible (iii) tel que son brouillon 8 le chiffre (263 au pire + 7 de sonde) : {usd(kv1 + kv2 + iii, 2)} <= 1275 : {kv1 + kv2 + iii <= 1275}")
autres = D("123") + D("483") + D("243")
tot5 = kv1 + kv2 + iii + autres
print(f"  avec (i) 123, (ii) 483, (iv) 243 de la note (plafonds de 2,00 non refaits) : {usd(tot5, 2)} ; reste sous 1275 : {usd(1275 - tot5, 2)}")
