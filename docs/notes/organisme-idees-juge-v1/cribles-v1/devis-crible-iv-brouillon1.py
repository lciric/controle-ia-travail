"""Devis et comptes exacts du crible (iv) « demi-générations », brouillon 1.

Processeur seul, bibliothèque standard, fractions exactes ; aucune donnée de crible, aucun tirage, aucun appel, aucun monde.
Entrées recopiées (chaque nombre porte sa source) :
  [VERDICT-PC] sections « Pour les cribles » et « Dépense rapprochée » du verdict v2 du pilote MR-2 v14
      (verdict-issue-pilote-mr2-v14-v2.md, e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d,
       branche verdict/pilote-mr2-v74-v14-v1, lu par git show) ;
  [NOTE] conception-idees-originales-v1.md (2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3), § 3 (iv), § 4 ;
  enveloppe : crible-iii-version-foi-v1.md (270 avec sa sonde), crible-v-version-foi-v2.md (204,67), crible-ii-brouillon1.md
      (411, 816a072f...), crible-i-brouillon1.md (127, a3c38ccc...) ;
  plafonds de session et bornes de sortie : bloc gelé du pilote, tels que recopiés par [CRIBLE-III] et [CRIBLE-V].
Valeurs SUPPOSÉES (aucune pièce ne les mesure ; dites comme telles dans le texte) : part d'entrée d'un appel (52 000 octets
servis, 3 octets par jeton) ; durée d'un tour de chaîne sur processeur (60 s attendues).
Lancer : python3 -I devis-crible-iv-brouillon1.py
"""
from fractions import Fraction as F
from math import comb


def u(x, n=6):
    return f"{float(x):.{n}f}"


def titre(t):
    print()
    print("§ " + t)


# --- entrées du pilote ([VERDICT-PC]) -------------------------------------------------------------------------------
COUT_4 = {"opus55": F("1.057336"), "argon": F("2.47162"), "astra": F("1.67175"), "fable52": F("10.019552")}
DUREES = {
    "argon": ["96.004", "38.287", "75.664", "47.464"],
    "astra": ["80.106", "61.164", "78.847", "34.411"],
    "fable52": ["388.807", "430.542", "553.242", "510.008"],
    "opus55": ["109.396", "54.737", "72.991", "36.425"],
}
TRONQUES = {("fable52", 2), ("fable52", 3)}
MACHINE_USD, MACHINE_TAUX = F("0.082018"), F("0.052222")
PUBLIC_SUR_CONFIG = {"opus55": F(1), "argon": F(1, 5)}
PLAFOND = {"opus55": F(2), "argon": F("2.34")}
BORNE_SORTIE = {"opus55": 89000}
PRIX_CONFIG = {"opus55": (F(4), F(20))}
N = 20

titre("0. Contrôles de cohérence des entrées")
somme_d = sum(F(x) for v in DUREES.values() for x in v)
h_machine = MACHINE_USD / MACHINE_TAUX
hors = h_machine * 3600 - somme_d
print("appels", sum(len(v) for v in DUREES.values()), "; somme des durées", u(somme_d, 3), "s")
print("machine du pilote", u(h_machine, 4), "h ; hors appels", u(hors, 1), "s")
print("quatre proposeurs + machine", u(sum(COUT_4.values()) + MACHINE_USD), "(verdict : 15,302276)")

titre("1. Attendu par appel de Pr-2 (moyenne des quatre appels du pilote, règle (b) de [CRIBLE-V]) et appel de trois cartes")
c6 = COUT_4["opus55"] / 4
print("appel de six cartes (mesuré, moyenne) c6 =", u(c6))
# SUPPOSÉ : texte servi de 52 000 octets à 3 octets par jeton, au prix d'entrée de 4 USD par million
entree = F(52000, 3) * PRIX_CONFIG["opus55"][0] / 10**6
c3_bas = entree + (c6 - entree) / 2
print("part d'entrée supposée", u(entree), "; sortie déduite", u(c6 - entree))
print("appel de trois cartes : prudent c3 = c6 =", u(c6), "; bas (sortie moitié, SUPPOSÉ)", u(c3_bas),
      "; rapport bas c3/c6", u(c3_bas / c6, 4))

titre("2. Taille servie (règle du code : (octets + 1 024) x entrée + borne x sortie <= plafond)")
p = "opus55"
octets_max = (PLAFOND[p] - BORNE_SORTIE[p] * PRIX_CONFIG[p][1] / 10**6) / (PRIX_CONFIG[p][0] / 10**6) - 1024
print("octets servis au plus :", u(octets_max, 0), "; ligne d'arrêt : 53 000 ; cible de la règle : 52 000")
print("cartes d'archive au plus dans un texte servi : bras 1 et 3, génération 2 : K1 + 6 ; bras 2, demi 2b : K1 + 9")

titre("3. Appels du crible")
appels = {"bras 1 (standard, 1 appel de six par génération)": 2, "bras 2 (demi-générations, 1a commun compris)": 4,
          "bras 3 (placebo, sans 1a commun)": 3}
for k, v in appels.items():
    print(k, ": par monde", v, "; en tout", N * v)
print("variante, 1a commun aux bras 2 et 3 : par monde", sum(appels.values()), "; en tout", N * sum(appels.values()))
print("forme de [NOTE] (sans appel commun) : par monde 10 ; en tout", N * 10)

titre("4. Garde d'égalité de dollars par monde (un appel des bras 2 ou 3 part si la dépense déjà faite du bras < $1(w))")
# coûts pris égaux à leur moyenne dans chaque monde : $1 = 2 c6 ; bras 2 : 1a, 1b, 2a, 2b de coût c3 chacun
for r in (F(1, 2), F(6, 10), c3_bas / c6, F(2, 3), F(8, 10), F(1)):
    c3 = r * c6
    k, depense = 0, F(0)
    while k < 4 and depense < 2 * c6:
        depense += c3
        k += 1
    print("c3/c6 =", u(r, 4), ": appels du bras 2 faits", k, "sur 4 ; dépense", u(depense, 4), "; rapport au bras 1",
          u(depense / (2 * c6), 4))
print("seuils : 2a part si c3 < c6 ; 2b part si 3 c3 < 2 c6, soit c3/c6 < 2/3 =", u(F(2, 3), 4))
print("dépassement borné : dépense d'un bras 2 ou 3 dans un monde <= $1(w) + un appel (plafond 2,00)")

titre("5. Devis (Pr-2, crédits de Claude)")
lignes = [("bras 1", 2 * N, c6, c6), ("bras 2 (1a commun compris)", 4 * N, c6, c3_bas), ("bras 3 (hors 1a)", 3 * N, c6, c3_bas)]
att, bas, plaf = F(0), F(0), F(0)
for nom, n, cp, cb in lignes:
    a_, b_ = n * (cp if nom == "bras 1" else c6), n * (cp if nom == "bras 1" else cb)
    att += a_; bas += b_; plaf += n * PLAFOND["opus55"]
    print(nom, n, "appels : attendu (tous faits, c6)", u(a_, 4), "; bas (c3 supposé)", u(b_, 4), "; plafonds", u(n * 2, 2))
print("proposeurs : attendu (tous faits)", u(att, 4), "; bas", u(bas, 4), "; plafonds x appels", u(plaf, 2))
# si c3 = c6, la garde coupe 2a et 2b des bras 2 et 3 : bras 2 fait 1a, 1b ; bras 3 fait 1a (commun), 1b'
coupe = (2 * N + 2 * N + 1 * N) * c6
print("si c3 = c6 (garde : bras 2 et 3 réduits à la génération 1) : 100 appels, attendu", u(coupe, 4))
borne_garde = N * (2 * PLAFOND["opus55"] + 2 * (2 * PLAFOND["opus55"] + PLAFOND["opus55"]))
print("borne par la garde (bras 1 <= 4 ; bras 2 et 3 <= $1 + 2 chacun, par monde) :", u(borne_garde, 2))
PART = F(240)
print("part du relais proposée (forme de [NOTE] : 80 + 80 + 80) :", u(PART, 2), "; coût moyen par appel qui l'atteint (180 appels) :",
      u(PART / 180, 4), "soit", u(PART / 180 / c6, 2), "fois c6")
sonde_att, sonde_pire = 3 * c6 + c6, 4 * PLAFOND["opus55"]
print("sonde des gabarits (3 appels de six cartes + 1 de trois cartes à archive de K1 + 9) : attendu", u(sonde_att, 4),
      "; pire", u(sonde_pire, 2))

titre("6. Durées et machine")
d2 = [F(x) for x in DUREES["opus55"]]
moy_d2, max_d2 = sum(d2) / 4, max(d2)
plus_long_repondu = max(F(x) for p_, v in DUREES.items() for i, x in enumerate(v) if (p_, i) not in TRONQUES)
B = 300
while B < F(3, 2) * plus_long_repondu:
    B += 300
print("opus55 : moyenne", u(moy_d2, 3), "s ; plus long", u(max_d2, 3), "s ; borne par appel (règle de [CRIBLE-V]) B_a =", B, "s")
chaine = F(60)  # SUPPOSÉ : un tour de chaîne sur processeur
monde_att = 2 * (moy_d2 + chaine) + 4 * (moy_d2 + chaine)  # bras 1, puis bras 2 (bras 3 en parallèle, plus court)
print("monde, attendu (tour de chaîne supposé 60 s) :", u(monde_att, 1), "s")
for F_files in (4, 5):
    mondes_par_file = -(-N // F_files)
    print("files", F_files, ": mondes par file", mondes_par_file, "; appels et chaîne attendus", u(mondes_par_file * monde_att, 1), "s")
    for Bc in (300, 600, 900):
        pire_monde = 6 * (B + Bc)
        pire = mondes_par_file * pire_monde
        print("   B_c =", Bc, "s : pire par monde", pire_monde, "s ; pire de la file", pire, "s =", u(F(pire, 3600), 3),
              "h ; garde de départ (pire + 2 h)", u(F(pire + 7200, 3600), 3), "h")
att_s = 4 * monde_att
mach_att = (att_s + hors) / 3600 * MACHINE_TAUX
mach_att_gen = (att_s + hors + 2 * 3600) / 3600 * MACHINE_TAUX
print("machine attendue (5 files)", u(mach_att, 6), "USD ;", u(mach_att_gen, 6), "avec deux heures de génération de mondes ;",
      "17 h :", u(17 * MACHINE_TAUX, 4), "; pire 3,00")

titre("7. Totaux de la variante")
print("crédits de Claude : attendu (tous faits)", u(att, 4), "; bas", u(bas, 4), "; pire (part)", u(PART, 2))
print("hors crédits (machine) : attendu", u(mach_att, 4), "à", u(mach_att_gen, 4), "; pire 3.00")
print("avec la sonde : crédits attendu", u(att + sonde_att, 4), "(bas", u(bas + sonde_att, 4) + ") ; pire", u(PART + sonde_pire, 2),
      "; total pire", u(PART + sonde_pire + 3, 2))
print("sonde partagée avec celle du crible (ii) (ses trois premiers appels) : pire", u(PART + PLAFOND["opus55"] + 3, 2),
      "; attendu de la sonde", u(c6, 4))

titre("8. Enveloppe de GO-2026-11-15-06 (1 275 USD au pire)")
autres = {"(iii) version qui fera foi v1, sonde comprise": F(270), "(v) version qui fera foi v2, sonde neuve comprise": F("204.67"),
          "(ii) brouillon 1, sonde comprise": F(411), "(i) brouillon 1": F(127)}
s = sum(autres.values())
for k, v in autres.items():
    print(k, u(v, 2))
print("quatre autres :", u(s, 2), "; reste pour (iv) :", u(1275 - s, 2))
for nom, v in (("(iv) variante, part 240, sonde propre", PART + sonde_pire + 3),
               ("(iv) variante, part 240, sonde partagée avec (ii)", PART + PLAFOND["opus55"] + 3),
               ("(iv) plafonds x appels (360), sonde propre", plaf + sonde_pire + 3),
               ("(iv) borne de la garde (320), sonde propre", borne_garde + sonde_pire + 3),
               ("(iv) [NOTE]", F(243))):
    print(nom, u(v, 2), "; cumul", u(s + v, 2), "; tient :", s + v <= 1275, "; marge", u(1275 - s - v, 2))

titre("9. Test des rangs signés exact (permutation des signes), seuil bilatéral")
for alpha in (F(25, 1000), F(5, 100)):
    n = 1
    while F(2, 2**n) > alpha:
        n += 1
    print("niveau", u(alpha, 3), ": au moins", n, "écarts non nuls, tous du même signe (p =", u(F(2, 2**n), 5) + ")")


def binom_queue(n, k, p):
    return sum(comb(n, j) * p**j * (1 - p)**(n - j) for j in range(k, n + 1))


def seuil_signe(m, alpha):
    for k in range(m + 1):
        if 2 * binom_queue(m, k, F(1, 2)) <= alpha:
            return k
    return None


titre("10. Signe seul (écarts de 0 ou +-1) : puissance à n = 20, bilatéral 0,025")
for a, b in ((F(3, 10), F(1, 10)), (F(4, 10), F(1, 10)), (F(5, 10), F(1, 10)), (F(35, 100), F(5, 100)), (F(2, 10), F(5, 100))):
    puissance = F(0)
    for m in range(0, 21):
        pm = comb(20, m) * (a + b)**m * (1 - a - b)**(20 - m)
        k = seuil_signe(m, F(25, 1000))
        if k is not None:
            puissance += pm * binom_queue(m, k, a / (a + b))
    print("P(+1) =", u(a, 2), "P(-1) =", u(b, 2), ": puissance (côté +)", u(puissance, 3))

titre("11. Probabilité d'atteindre le minimum (16 mondes complets sur 20 pour une comparaison principale)")
for pp in ("1", "0.99", "0.98", "0.97", "0.95"):
    p_ = F(pp)
    print("p par appel", pp, ": P1 (6 appels : bras 1 et 2)", u(binom_queue(20, 16, p_**6), 4),
          "; P2 (7 appels : bras 2 et 3, 1a commun)", u(binom_queue(20, 16, p_**7), 4))

titre("12. Formes écartées, information seulement")
m1p, m1c = COUT_4["argon"] / 4 * PUBLIC_SUR_CONFIG["argon"], COUT_4["argon"] / 4
print("forme de [NOTE], Pr-1 argon, 200 appels : attendu public", u(200 * m1p, 4), "; configuration", u(200 * m1c, 4),
      "(hors crédits) ; plafonds x appels", u(200 * PLAFOND["argon"], 2))
print("Pr-2, 200 appels sans appel commun : attendu", u(200 * c6, 4), "; plafonds x appels", u(200 * 2, 2))
print("[NOTE] : 30,30 attendus, 243,00 au pire")
