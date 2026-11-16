"""Devis, durées, bornes, garde de départ et information du crible (iii), version qui fera foi — v1.

Applique les règles écrites du brouillon 8 (`crible-iii-brouillon8.md`, `d3406878…`, section « Devis », table « Règle de mise
à jour d'après le pilote », règle de III-7 et section « Seuil ») aux seuls coûts et durées du pilote MR-2 v14 recopiés de la
section « Pour les cribles » de son verdict (rien d'autre du pilote n'est lu). Bibliothèque standard seule ; aucun appel,
aucune donnée de crible, aucun tirage. Lit en lecture seule `registres/go.md` et `registres/depenses.md` pour l'enveloppe.

Usage : python3 -I devis-crible-iii-version-foi-v1.py RACINE_DU_DEPOT
"""
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path

D = lambda s: F(s)  # noqa: E731 - nombres décimaux recopiés exactement


def f6(x):
    return f"{float(x):.6f}"


def f2(x):
    return f"{float(x):.2f}"


# --- 1. Recopié de la section « Pour les cribles » (seule part lisible du verdict du pilote) ---
DUREES = {  # (monde, proposeur) -> secondes
    (1, "argon"): D("96.004"), (1, "astra"): D("80.106"), (1, "fable52"): D("388.807"), (1, "opus55"): D("109.396"),
    (2, "argon"): D("38.287"), (2, "astra"): D("61.164"), (2, "fable52"): D("430.542"), (2, "opus55"): D("54.737"),
    (3, "argon"): D("75.664"), (3, "astra"): D("78.847"), (3, "fable52"): D("553.242"), (3, "opus55"): D("72.991"),
    (4, "argon"): D("47.464"), (4, "astra"): D("34.411"), (4, "fable52"): D("510.008"), (4, "opus55"): D("36.425"),
}
TRONQUES = {(3, "fable52"), (4, "fable52")}
DEBUT_UTC, FIN_UTC = (12, 14, 34), (12, 59, 7)  # 2026-11-16, manifeste du pilote
COUT = {"fable52": D("10.019552"), "opus55": D("1.057336"), "argon": D("2.471620"), "astra": D("1.671750")}
COUT_MACHINE, PRIX_MACHINE = D("0.082018"), D("0.052222")
COUT_TRONQUES_FABLE = D("5.585992")
TOTAL_RAPPROCHE = D("15.378197")
REPONDUS, TRONQUES_N, ECHECS = 14, 2, 0

# --- Constantes du brouillon 8 (inchangées) ---
PR2, PR4 = "opus55", "fable52"
PLAFOND = {PR2: D(2), PR4: D(3)}          # plafonds de session, bloc gelé du pilote
BORNE = {PR2: 89000, PR4: 64000}          # bornes de sortie
PRIX_SORTIE = {PR2: D(20) / 10**6, PR4: D(40) / 10**6}  # USD par jeton (public = configuration)
APPELS = {"S": (PR4, 20), "D passe 2": (PR4, 20), "H passe 2": (PR4, 20), "passe 1": (PR2, 20), "B passe 2": (PR2, 20)}
MACHINE_PIRE = D(3)
BORNE_APPEL, BORNE_MONDE, MONDES_PAR_FILE, FILES, N = 3000, 7200, 4, 5, 20
MARGE_FIN = 2 * 3600

print("== 0. Contrôles de cohérence de la section recopiée ==")
somme = sum(COUT.values()) + COUT_MACHINE
print("somme des postes (relais + machine) :", f6(somme), "; total rapproché :", f6(TOTAL_RAPPROCHE),
      "; écart :", f6(TOTAL_RAPPROCHE - somme))
print("appels : 16 =", REPONDUS + TRONQUES_N + ECHECS, "(répondus + tronqués + échecs)")
duree_totale = sum(DUREES.values())
span = (FIN_UTC[0] * 3600 + FIN_UTC[1] * 60 + FIN_UTC[2]) - (DEBUT_UTC[0] * 3600 + DEBUT_UTC[1] * 60 + DEBUT_UTC[2])
print("somme des 16 durées :", f"{float(duree_totale):.3f}", "s ; manifeste fin - début :", span, "s ; écart :",
      f"{float(span - duree_totale):.3f}", "s (les appels du pilote se sont suivis en série)")
h_machine = COUT_MACHINE / PRIX_MACHINE
print("heures de machine du pilote = coût / prix horaire :", f"{float(h_machine):.5f}", "h =",
      f"{float(h_machine * 3600):.1f}", "s ; hors appels :", f"{float(h_machine * 3600 - span):.1f}", "s")
hors_appels = h_machine * 3600 - span

print("\n== 1. Attendu par appel (règle : moyenne arithmétique par relais, prix public = configuration ici) ==")
moy = {}
for r in (PR2, PR4):
    n = sum(1 for (w, p) in DUREES if p == r)
    moy[r] = COUT[r] / n
    print(f"{r} : {f6(COUT[r])} / {n} = {f6(moy[r])} USD par appel (brouillon : {'0,80' if r == PR2 else '1,60'})")
print("fourchette (règle : plus petit et plus grand appel du pilote) : dollars par appel absents de la section lisible ;"
      " bornes qui s'en déduisent :")
c_complets = COUT[PR4] - COUT_TRONQUES_FABLE
print(f"  {PR4} : plus petit appel <= {f6(c_complets / 2)} (moyenne des 2 complets, {f6(c_complets)}) ;"
      f" plus grand >= {f6(COUT_TRONQUES_FABLE / 2)} (moyenne des 2 tronqués) ; tout appel <= plafond {f2(PLAFOND[PR4])}")
print(f"  {PR2} : plus petit <= {f6(moy[PR2])} <= plus grand <= {f6(COUT[PR2])} (total des 4)")

print("\n== 2. Sortie au-dessus de 80 % de la borne (règle : réserve de tronquage annoncée et sonde obligatoire) ==")
for r in (PR2, PR4):
    seuil = BORNE[r] * 8 // 10
    if any(p == r for (_, p) in TRONQUES):
        print(f"{r} : appel tronqué (raison d'arrêt = borne, [PILOTE] « Métrique ») : sortie = {BORNE[r]} > {seuil} : RÈGLE DÉCLENCHÉE")
    else:
        maxi = COUT[r] / PRIX_SORTIE[r]
        print(f"{r} : aucun tronqué ; sortie du plus grand appel <= coût total / prix de sortie = {float(maxi):.1f}"
              f" jetons {'<=' if maxi <= seuil else '>'} {seuil} : {'non déclenchée' if maxi <= seuil else 'INDÉTERMINÉ'}")

print("\n== 3. Taux de réussite par appel (information ; ne change ni N ni aucun seuil, R-2992) ==")
rep = {r: sum(1 for (w, p) in DUREES if p == r and (w, p) not in TRONQUES) for r in (PR2, PR4)}
for r in (PR2, PR4):
    print(f"{r} : {rep[r]} répondus sur 4")
p_commun = F(rep[PR2] + rep[PR4], 8)
print("deux relais ensemble (définition de « Seuil ») :", rep[PR2] + rep[PR4], "sur 8 =", f"{float(p_commun):.4f}")


def p_min(q, n=N, mini=16):
    return sum(comb(n, k) * q ** k * (1 - q) ** (n - k) for k in range(mini, n + 1))


for nom, q in (("taux commun p = 0,75, monde complet = p^5", p_commun ** 5),
               ("par relais, Pr-2 1,00 (2 appels) et Pr-4 0,50 (3 appels)", F(rep[PR2], 4) ** 2 * F(rep[PR4], 4) ** 3)):
    print(f"  {nom} : P(monde complet) = {float(q):.4f} ; P(n_c >= 16 sur 20) = {float(p_min(q)):.3e}")
q_rel = F(rep[PR2], 4) ** 2 * F(rep[PR4], 4) ** 3
# Arrêt « complets + en cours + non commencés < 16 » : déclenché au 5e monde non complet ; approximation : les 4 autres
# files ont chacune un monde en cours à cet instant, mené à son terme ; mondes commencés = min(20, K + 4).
pi = 1 - q_rel
esp = F(0)
p_tot = F(0)
for k in range(5, N + 1):
    pk = comb(k - 1, 4) * pi ** 5 * (1 - pi) ** (k - 5)
    p_tot += pk
    esp += pk * min(N, k + 4)
esp += (1 - p_tot) * N
p_tr = F(len(TRONQUES), 4)
p3 = sum(comb(20, k) * p_tr ** k * (1 - p_tr) ** (20 - k) for k in range(3, 21))
print(f"  réserve de l'étage 2 : P(3 tronqués ou plus sur les 20 appels d'un bras de Pr-4 | taux de tronquage {float(p_tr):.2f})"
      f" = {float(p3):.6f}")
cout_monde = 3 * moy[PR4] + 2 * moy[PR2]
print(f"  arrêt du minimum (par relais) : probabilité {float(p_tot):.6f} ; mondes commencés attendus ≈ {float(esp):.2f}"
      f" (approximation dite) ; dépense attendue ≈ {f2(esp * cout_monde)} USD ({f6(cout_monde)} par monde)")

print("\n== 4. Devis refait (attendu au coût moyen du pilote ; pire inchangé, plafonds) ==")
tot_att = {"crédits": F(0), "hors": F(0)}
tot_pire = {"crédits": F(0), "hors": F(0)}
for ligne, (r, n) in APPELS.items():
    a, p = n * moy[r], n * PLAFOND[r]
    tot_att["crédits"] += a
    tot_pire["crédits"] += p
    print(f"{ligne:10s} ({r}, {n} appels) : attendu {f6(a)} ; pire {f2(p)}")

print("\n== 5. Durées (règle : durée mesurée au pilote ; bornes de 3 000 s et 7 200 s inchangées) ==")
dur = {r: sorted(v for (w, p), v in DUREES.items() if p == r) for r in (PR2, PR4)}
for r in (PR2, PR4):
    print(f"{r} : min {float(dur[r][0]):.3f} ; moyenne {float(sum(dur[r]) / 4):.3f} ; max {float(dur[r][-1]):.3f} s")
mondes_pilote = {w: sum(v for (ww, p), v in DUREES.items() if ww == w) for w in (1, 2, 3, 4)}
print("mondes du pilote (4 appels en série) :", {w: f"{float(v):.3f}" for w, v in mondes_pilote.items()},
      "; moyenne", f"{float(sum(mondes_pilote.values()) / 4):.3f}", "s")
m2, m4 = sum(dur[PR2]) / 4, sum(dur[PR4]) / 4
chemin = {"attendu": m2 + m4, "bas": dur[PR2][0] + dur[PR4][0], "haut": dur[PR2][-1] + dur[PR4][-1]}
serie = 3 * m4 + 2 * m2
print("monde du crible, chemin critique passe 1 (Pr-2) puis D (Pr-4), S et H en même temps :",
      {k: f"{float(v):.2f}" for k, v in chemin.items()}, "s ; tout en série (information) :", f"{float(serie):.2f}", "s")
for k, v in chemin.items():
    print(f"  file de 4 mondes ({k}) : {float(4 * v):.1f} s = {float(4 * v / 60):.1f} min")
print(f"  file en série (information) : {float(4 * serie):.1f} s = {float(4 * serie / 60):.1f} min")
plus_long = max(DUREES.values())
print("appel le plus long du pilote :", f"{float(plus_long):.3f}", "s ;", "> 1 500 s : nœud" if plus_long > 1500 else
      "<= 1 500 s : aucun nœud, borne par appel 3 000 s inchangée")
print("deux étapes en série au pire :", 2 * BORNE_APPEL, "s <=", BORNE_MONDE, "s")
garde = MONDES_PAR_FILE * BORNE_MONDE + MARGE_FIN
print("pire cas d'une file :", MONDES_PAR_FILE * BORNE_MONDE, "s ; garde de départ :", garde, "s =", garde / 3600, "h (inchangée)")
print("machine : temps hors appels mesuré au pilote", f"{float(hors_appels):.1f}", "s ; prix relu", f6(PRIX_MACHINE), "USD/h")
mach = {}
for k, v in chemin.items():
    s = 4 * v + hors_appels
    mach[k] = s / 3600 * PRIX_MACHINE
    print(f"  machine ({k}) : {float(s):.1f} s = {float(s / 3600):.4f} h -> {f6(mach[k])} USD")
s_lit = FILES * chemin["attendu"] + hors_appels
print(f"  lecture littérale « durée par monde × cinq files » : {float(s_lit):.1f} s -> {f6(s_lit / 3600 * PRIX_MACHINE)} USD")
s_ser = 4 * serie + hors_appels
print(f"  file en série (information) : {float(s_ser):.1f} s -> {f6(s_ser / 3600 * PRIX_MACHINE)} USD")
s_pire = garde
print(f"  machine au pire de la garde (10 h) au prix relu : {f6(F(s_pire, 3600) * PRIX_MACHINE)} USD ; pire du devis {f2(MACHINE_PIRE)}")
tot_att["hors"] = mach["attendu"]
tot_pire["hors"] = MACHINE_PIRE

print("\n== 6. Totaux ==")
for k in ("crédits", "hors"):
    print(f"{k} : attendu {f6(tot_att[k])} ; pire {f2(tot_pire[k])}")
print(f"total : attendu {f6(tot_att['crédits'] + tot_att['hors'])} ; pire {f2(tot_pire['crédits'] + tot_pire['hors'])}")
sonde_att = 2 * moy[PR2] + moy[PR4]
sonde_pire = 2 * PLAFOND[PR2] + PLAFOND[PR4]
print(f"sonde des gabarits (obligatoire) : attendu {f6(sonde_att)} ; pire {f2(sonde_pire)} (sur crédits)")
print(f"avec la sonde : crédits attendu {f6(tot_att['crédits'] + sonde_att)} ; pire {f2(tot_pire['crédits'] + sonde_pire)} ;"
      f" total pire {f2(tot_pire['crédits'] + tot_pire['hors'] + sonde_pire)}")
print("parts : fable52", f2(60 * PLAFOND[PR4]), "(part 180) ; opus55", f2(40 * PLAFOND[PR2]), "(part 80) ;"
      " attendu fable52", f6(60 * moy[PR4]), "; opus55", f6(40 * moy[PR2]))

print("\n== 7. III-7 (règle écrite) ==")
print("sans sonde jouée : III-7 reste 1,05 à 1,25 ; dénominateur lu au pilote :", f6(moy[PR4]),
      "; une fois la sonde jouée : 1 + c1 /", f6(moy[PR4]), "± 0,05")
for c1 in (moy[PR2],):
    print(f"  information : si c1 valait le coût moyen d'un appel standard de {PR2} ({f6(c1)}) : {float(1 + c1 / moy[PR4]):.4f}")
print("  la fourchette 1,05 à 1,25 répond à c1 entre", f6(D("0.05") * moy[PR4]), "et", f6(D("0.25") * moy[PR4]), "USD")

print("\n== 8. Enveloppe de GO-2026-11-15-06 (1 275 USD au pire) ==")
racine = Path(sys.argv[1])
go = (racine / "registres/go.md").read_text(encoding="utf-8").splitlines()
lignes_calcul = [i + 1 for i, l in enumerate(go) if l.startswith("| GO-") and "GO-2026-11-15-06" in l
                 and l.split("|")[3].strip() == "calcul"]
dep = (racine / "registres/depenses.md").read_text(encoding="utf-8").splitlines()
lignes_dep = [i + 1 for i, l in enumerate(dep) if "GO-2026-11-15-06" in l]
print("lignes « calcul » de go.md qui citent GO-2026-11-15-06 :", lignes_calcul or "aucune")
print("lignes de depenses.md qui citent GO-2026-11-15-06 :", lignes_dep or "aucune")
engage = F(0)
iii = tot_pire["crédits"] + tot_pire["hors"] + sonde_pire
print("engagé sous l'enveloppe :", f2(engage), "; crible (iii) avec la sonde :", f2(iii), "; reste :", f2(1275 - engage - iii))
autres = {"(i) [NOTE]": D(123), "(ii) [NOTE]": D(483), "(iv) [NOTE]": D(243), "(v) brouillon 9, avec sa sonde neuve": D("204.67")}
print("autres cribles aux textes actuels (pire) :", {k: f2(v) for k, v in autres.items()}, "; somme", f2(sum(autres.values())))
print("cumul des cinq :", f2(sum(autres.values()) + iii), "contre 1 275 ; sans les deux sondes :",
      f2(sum(autres.values()) - D("8.07") + iii - sonde_pire))
print("attendus : (iii) avec la sonde", f2(tot_att["crédits"] + tot_att["hors"] + sonde_att), "contre 63,30 à [NOTE] ;"
      " enveloppe attendue de GO-2026-11-15-06 : 247,20")
