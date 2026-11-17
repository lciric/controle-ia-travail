"""Devis et comptes exacts du crible (ii) « proposeurs en série », brouillon 1.

Processeur seul, bibliothèque standard, fractions exactes ; aucune donnée de crible, aucun tirage, aucun appel.
Entrées recopiées (chaque nombre porte sa source) :
  [VERDICT-PC] section « Pour les cribles » et « Dépense rapprochée » du verdict v2 du pilote MR-2 v14
      (verdict-issue-pilote-mr2-v14-v2.md, e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d,
       branche verdict/pilote-mr2-v74-v14-v1, lu par git show) ;
  [NOTE] conception-idees-originales-v1.md (2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3), § 3 (ii), § 4 ;
  [CRIBLE-III] crible-iii-version-foi-v1.md (pire 270 avec sa sonde) ; [CRIBLE-V] crible-v-version-foi-v2.md (pire 204,67) ;
  plafonds de session et bornes de sortie : bloc gelé du pilote, tels que recopiés par [CRIBLE-III] et [CRIBLE-V].
Lancer : python3 -I devis-crible-ii-brouillon1.py
"""
from fractions import Fraction as F
from math import comb


def u(x, n=6):
    return f"{float(x):.{n}f}"


def titre(t):
    print()
    print("§ " + t)


# --- entrées du pilote ([VERDICT-PC]) -------------------------------------------------------------------------------
COUT_4 = {  # dollars des quatre appels de chaque proposeur, prix de la configuration (dépense rapprochée)
    "opus55": F("1.057336"), "argon": F("2.47162"), "astra": F("1.67175"), "fable52": F("10.019552"),
}
REPONDUS = {"opus55": (4, 4), "argon": (4, 4), "astra": (4, 4), "fable52": (2, 4)}
DUREES = {  # secondes, monde puis proposeur ([VERDICT-PC], « Pour les cribles »)
    "argon": ["96.004", "38.287", "75.664", "47.464"],
    "astra": ["80.106", "61.164", "78.847", "34.411"],
    "fable52": ["388.807", "430.542", "553.242", "510.008"],
    "opus55": ["109.396", "54.737", "72.991", "36.425"],
}
TRONQUES = {("fable52", 2), ("fable52", 3)}  # mondes 3 et 4 (indices 2 et 3)
MACHINE_USD, MACHINE_TAUX = F("0.082018"), F("0.052222")  # USD et USD par heure
PUBLIC_SUR_CONFIG = {"opus55": F(1), "argon": F(1, 5), "astra": F(1), "fable52": F(1)}  # [CRIBLE-V], table des proposeurs
PLAFOND = {"opus55": F(2), "argon": F("2.34"), "astra": F("2.34"), "fable52": F(3)}
BORNE_SORTIE = {"opus55": 89000, "argon": 36000, "astra": 36000, "fable52": 64000}
PRIX_CONFIG = {"opus55": (F(4), F(20)), "argon": (F(10), F(50))}  # USD par million, entrée / sortie

titre("0. Contrôles de cohérence des entrées")
n_app = sum(len(v) for v in DUREES.values())
somme_d = sum(F(x) for v in DUREES.values() for x in v)
print("appels", n_app, "; somme des durées", u(somme_d, 3), "s")
h_machine = MACHINE_USD / MACHINE_TAUX
print("machine du pilote", u(h_machine, 4), "h =", u(h_machine * 3600, 1), "s ; hors appels",
      u(h_machine * 3600 - somme_d, 1), "s")
print("total des quatre proposeurs", u(sum(COUT_4.values())), "USD (verdict : 15,302276 avec la machine, sans les autres)")
print("quatre proposeurs + machine", u(sum(COUT_4.values()) + MACHINE_USD))

titre("1. Attendu par appel (moyenne de tous les appels du pilote, règle (b) de [CRIBLE-V])")
moy = {}
for p, c in COUT_4.items():
    moy[p] = c / 4
    print(p, "configuration", u(moy[p]), "; public", u(moy[p] * PUBLIC_SUR_CONFIG[p]), "; répondus",
          f"{REPONDUS[p][0]} sur {REPONDUS[p][1]}", "; part moyenne du plafond", u(moy[p] / PLAFOND[p], 4))

titre("2. Tronquage (règle de [CRIBLE-III] : plus grand appel au-dessus de 80 % de la borne de sortie)")
p = "opus55"
borne_sortie_max = COUT_4[p] / PRIX_CONFIG[p][1] * 10**6  # tout le coût mis en sortie : borne supérieure
print(p, "sortie du plus grand appel <=", u(borne_sortie_max, 0), "jetons ; 80 % de la borne :", int(0.8 * BORNE_SORTIE[p]),
      "; règle déclenchée :", borne_sortie_max > F(8, 10) * BORNE_SORTIE[p])
octets_max = (PLAFOND[p] - BORNE_SORTIE[p] * PRIX_CONFIG[p][1] / 10**6) / (PRIX_CONFIG[p][0] / 10**6) - 1024
print(p, "octets servis au plus sous le plafond de session (règle du code, (octets + 1 024) x entrée + borne x sortie) :",
      u(octets_max, 0))
pa = "argon"
octets_max_a = (PLAFOND[pa] - BORNE_SORTIE[pa] * PRIX_CONFIG[pa][1] / 10**6) / (PRIX_CONFIG[pa][0] / 10**6) - 1024
print(pa, "octets servis au plus sous le plafond de session (même règle, prix de la configuration) :", u(octets_max_a, 0))

titre("3. Appels du crible")
N = 20
formes = {
    "variante, rang 1 commun (P1 sert aux trois bras)": {"P": 4, "S": 3, "Q": 3},
    "forme de [NOTE], trois bras de quatre sessions": {"P": 4, "S": 4, "Q": 4},
}
for nom, f in formes.items():
    print(nom, ": par monde", sum(f.values()), "; en tout", N * sum(f.values()))

titre("4. Devis de la variante « crédits de Claude au maximum » (Pr-2 opus55 aux quatre places, rang 1 commun)")
m2 = moy["opus55"]
marge = F("0.05")  # entrée supplémentaire supposée par appel des rangs 2 à 4 (haut de fourchette)
lignes = [("parallèle P1 à P4", 4 * N, 0), ("série S2 à S4", 3 * N, 1), ("placebo Q2 à Q4", 3 * N, 1)]
att_tot, haut_tot, pire_tot = F(0), F(0), F(0)
for nom, n, sup in lignes:
    att, haut, pire = n * m2, n * (m2 + sup * marge), n * PLAFOND["opus55"]
    att_tot += att; haut_tot += haut; pire_tot += pire
    print(nom, n, "appels : attendu", u(att, 4), "; haut", u(haut, 4), "; pire", u(pire, 2))
print("proposeurs (crédits de Claude) : attendu", u(att_tot, 4), "; haut", u(haut_tot, 4), "; pire", u(pire_tot, 2))
sonde_n = 4
sonde_att, sonde_pire = sonde_n * m2, sonde_n * PLAFOND["opus55"]
print("sonde des gabarits (4 appels de opus55) : attendu", u(sonde_att, 4), "; pire", u(sonde_pire, 2))

titre("5. Durées et machine")
d2 = [F(x) for x in DUREES["opus55"]]
moy_d2, max_d2 = sum(d2) / 4, max(d2)
plus_long_repondu = max(F(x) for p_, v in DUREES.items() for i, x in enumerate(v) if (p_, i) not in TRONQUES)
B = 300
while B < F(3, 2) * plus_long_repondu:
    B += 300
B_o = 300
while B_o < F(3, 2) * max_d2:
    B_o += 300
print("opus55 : moyenne", u(moy_d2, 3), "s ; plus long", u(max_d2, 3), "s")
print("plus long appel répondu du pilote (tous proposeurs)", u(plus_long_repondu, 3), "s ; règle de [CRIBLE-V] : B_a =", B,
      "s ; même règle sur opus55 seul :", B_o, "s")
# phase 1 : 4 vagues de 20 sessions (une par file) ; phase 2 : par file, 4 mondes l'un après l'autre, 3 tours chacun
vague_att = max_d2  # attendu d'une vague de quatre appels pris au plus long des quatre appels du pilote (prudent)
ph1_att, ph2_att = 4 * vague_att, 4 * 3 * moy_d2
ph1_pire, ph2_pire = 4 * B, 4 * 3 * B
hors = h_machine * 3600 - somme_d
print("phase 1 : attendu", u(ph1_att, 1), "s ; pire", ph1_pire, "s")
print("phase 2 (une file) : attendu", u(ph2_att, 1), "s ; pire", ph2_pire, "s")
print("appels attendus", u(ph1_att + ph2_att, 1), "s ; pire des appels", ph1_pire + ph2_pire, "s =",
      u(F(ph1_pire + ph2_pire, 3600), 3), "h ; garde de départ (pire + 2 h)", u(F(ph1_pire + ph2_pire + 7200, 3600), 3), "h")
mach_att = (ph1_att + ph2_att + hors) / 3600 * MACHINE_TAUX
mach_att_gen = (ph1_att + ph2_att + hors + 3600) / 3600 * MACHINE_TAUX
print("machine attendue", u(mach_att, 6), "USD (temps hors appels du pilote compris) ;", u(mach_att_gen, 6),
      "avec une heure de génération de mondes en plus ; 17 h :", u(17 * MACHINE_TAUX, 4), "; pire 3,00")

titre("6. Totaux de la variante")
tot_att = att_tot + mach_att
print("crédits de Claude : attendu", u(att_tot, 4), "(haut", u(haut_tot, 4) + ") ; pire", u(pire_tot, 2))
print("hors crédits (machine) : attendu", u(mach_att, 4), "à", u(mach_att_gen, 4), "; pire 3.00")
print("total : attendu", u(tot_att, 4), "; pire", u(pire_tot + 3, 2))
print("avec la sonde : crédits attendu", u(att_tot + sonde_att, 4), "pire", u(pire_tot + sonde_pire, 2),
      "; total pire", u(pire_tot + sonde_pire + 3, 2))

titre("7. Formes écartées, information seulement")
m1c, m1p = moy["argon"], moy["argon"] * PUBLIC_SUR_CONFIG["argon"]
for nom, n in (("Pr-1 argon, rang 1 commun", 200), ("Pr-1 argon, forme de [NOTE]", 240)):
    print(nom, ": attendu public", u(n * m1p, 4), "; configuration", u(n * m1c, 4), "; pire", u(n * PLAFOND["argon"] + 3, 2),
          "(hors crédits)")
print("Pr-2 opus55, forme de [NOTE] (240 appels) : attendu", u(240 * m2, 4), "; pire", u(240 * PLAFOND["opus55"] + 3, 2))
print("[NOTE] : 63,30 attendus, 483,00 au pire")

titre("8. Enveloppe de GO-2026-11-15-06 (1 275 USD au pire)")
autres = {"(iii) version qui fera foi v1, sonde comprise": F(270), "(v) version qui fera foi v2, sonde neuve comprise": F("204.67"),
          "(i) [NOTE]": F(123), "(iv) [NOTE]": F(243)}
s = sum(autres.values())
for k, v in autres.items():
    print(k, u(v, 2))
print("quatre autres :", u(s, 2), "; reste pour (ii) :", u(1275 - s, 2))
ii = pire_tot + sonde_pire + 3
print("(ii) variante, sonde comprise :", u(ii, 2), "; cumul", u(s + ii, 2), "; tient :", s + ii <= 1275)
for nom, v in (("(ii) forme de [NOTE] sur opus55, avec sonde", 240 * PLAFOND["opus55"] + sonde_pire + 3),
               ("(ii) Pr-1 rang 1 commun", 200 * PLAFOND["argon"] + 3), ("(ii) [NOTE]", F(483))):
    print(nom, u(v, 2), "; cumul", u(s + v, 2), "; tient :", s + v <= 1275)

titre("9. Test des rangs signés exact (permutation des signes), seuil bilatéral")
for alpha in (F(25, 1000), F(5, 100)):
    n = 1
    while F(2, 2**n) > alpha:
        n += 1
    print("niveau", u(alpha, 3), ": au moins", n, "écarts non nuls, tous du même signe (p =", u(F(2, 2**n), 5) + ")")

titre("10. Signe seul (écarts de 0 ou +-1) : seuil exact et puissance à n = 20, bilatéral 0,025")


def binom_queue(n, k, p):
    return sum(comb(n, j) * p**j * (1 - p)**(n - j) for j in range(k, n + 1))


def seuil_signe(m, alpha):  # plus petit k tel que 2 P(Bin(m, 1/2) >= k) <= alpha
    for k in range(m + 1):
        if 2 * binom_queue(m, k, F(1, 2)) <= alpha:
            return k
    return None


alpha = F(25, 1000)
for a, b in ((F(3, 10), F(1, 10)), (F(4, 10), F(1, 10)), (F(5, 10), F(1, 10)), (F(35, 100), F(5, 100))):
    puissance = F(0)
    for m in range(0, 21):  # m écarts non nuls
        pm = comb(20, m) * (a + b)**m * (1 - a - b)**(20 - m)
        k = seuil_signe(m, alpha)
        if k is not None:
            puissance += pm * binom_queue(m, k, a / (a + b))
    print("P(+1) =", u(a, 2), "P(-1) =", u(b, 2), ": puissance (côté +)", u(puissance, 3))

titre("11. Probabilité d'atteindre le minimum (16 mondes complets sur 20 pour une comparaison principale)")
for pp in ("1", "0.99", "0.98", "0.97", "0.95", "0.90"):
    p_ = F(pp)
    q7, q10 = p_**7, p_**10
    print("p par appel", pp, ": comparaison (7 appels)", u(binom_queue(20, 16, q7), 4), "; monde entier (10 appels)",
          u(binom_queue(20, 16, q10), 4))
