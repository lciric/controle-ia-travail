"""Comptes exacts pour les brouillons 1 des cribles (v) et (iii) — v2 (la v1 reste en place, R12 ; la v2 la contient et ajoute
les points 5 à 9). Aucune donnée, aucun appel, aucun tirage ; bibliothèque standard seule ; quelques millisecondes.
1. Intervalles de Clopper-Pearson à 95 % bilatéraux pour x mondes sur 20.
2. Test des signes, n accords non nuls de 10 à 20 : plus petit c tel que P(X >= c | 1/2) <= niveau, niveaux 0,0125 et 0,025.
3. Puissance exacte du test des signes à n = 20 (niveau unilatéral 0,0125) pour p = 0,6 ; 0,7 ; 0,8 ; 0,9.
4. Part épargnée attendue par la règle de (v) selon le nombre k de mondes où elle appelle les chers, aux prix centraux.
5. Pour n mondes complets de 16 à 20 : plus petit W dont la borne basse de Clopper-Pearson (95 % bilatéral) dépasse 0,05.
6. Probabilité d'une « perte établie » (W >= seuil du point 5, n = 20) si chaque monde perd avec la probabilité p.
7. Part attendue d'ensembles tirés au hasard (taille uniforme sur 1, 2, 3 ; traits uniformes sans remise parmi 8) qui
   contiennent au moins un trait distracteur, pour d = 2, 3, 4 distracteurs.
8. Probabilité qu'au moins un de six ensembles tirés au hasard (indépendants, filtre ignoré) contienne une paire donnée.
9. Modèle de proposeurs synthétiques de la conception v4 (probabilité par carte de proposer une composante inconnue :
   forte 0,5 ; moyenne 0,25 ; faible 0,1 ; conditionnelle sans sa condition 0,02 ; cartes indépendantes) : probabilité que
   douze cartes de la moitié chère couvrent une composante que les douze de la moitié bon marché ont manquée."""
from math import comb


def queue_haute(n, c, p):
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(c, n + 1))


def cdf(n, x, p):
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(0, x + 1))


def bissection(f, lo=0.0, hi=1.0, tours=200):
    for _ in range(tours):
        mi = 0.5 * (lo + hi)
        if f(mi):
            hi = mi
        else:
            lo = mi
    return 0.5 * (lo + hi)


def clopper_pearson(x, n, a=0.05):
    bas = 0.0 if x == 0 else bissection(lambda p: queue_haute(n, x, p) >= a / 2)
    haut = 1.0 if x == n else bissection(lambda p: cdf(n, x, p) <= a / 2)
    return bas, haut


print("1. Clopper-Pearson 95 % bilatéral, x sur 20")
for x in range(0, 11):
    b, h = clopper_pearson(x, 20)
    print(f"  x = {x:2d} : [{b:.4f} ; {h:.4f}]")

print("2. Test des signes : plus petit c avec P(X >= c | n, 1/2) <= niveau")
for n in range(10, 21):
    out = []
    for niv in (0.0125, 0.025):
        c = min(c for c in range(n + 2) if queue_haute(n, c, 0.5) <= niv) if queue_haute(n, n, 0.5) <= niv else None
        out.append(f"niveau {niv} : c = {c}" + (f" (P = {queue_haute(n, c, 0.5):.4f})" if c is not None else " (impossible)"))
    print(f"  n = {n:2d} : " + " ; ".join(out))

print("3. Puissance du test des signes, n = 20, niveau unilatéral 0,0125 (c = 16)")
for p in (0.6, 0.7, 0.8, 0.9):
    print(f"  p = {p} : puissance {queue_haute(20, 16, p):.4f}")

print("4. Part épargnée attendue par la règle de (v), prix centraux (0,25 ; 0,80 ; 1,00 ; 1,60 USD par appel)")
bm, ch = 0.25 + 0.80, 1.00 + 1.60
for k in (0, 1, 2, 3, 4, 5, 10, 15, 20):
    tout = 20 * (bm + ch)
    regle = 20 * bm + k * ch
    print(f"  k = {k:2d} mondes appelés : épargne {1 - regle / tout:.4f} du coût des proposeurs")

print("5. Plus petit W dont la borne basse de Clopper-Pearson dépasse 0,05")
seuils = {}
for n in range(16, 21):
    w = min(x for x in range(n + 1) if clopper_pearson(x, n)[0] > 0.05)
    seuils[n] = w
    print(f"  n = {n} : W >= {w} (borne basse {clopper_pearson(w, n)[0]:.4f} ; à W - 1 : {clopper_pearson(w - 1, n)[0]:.4f})")

print("6. Probabilité d'une perte établie à n = 20 (W >= %d) si chaque monde perd avec la probabilité p" % seuils[20])
for p in (0.05, 0.10, 0.15, 0.20, 0.26, 0.35, 0.47):
    print(f"  p = {p:.2f} : {queue_haute(20, seuils[20], p):.4f}")

print("7. Part attendue d'ensembles au hasard (taille 1, 2 ou 3, uniforme) contenant au moins un distracteur, 8 traits")
for d in (2, 3, 4):
    parts = [1 - comb(8 - d, s) / comb(8, s) for s in (1, 2, 3)]
    print(f"  d = {d} : tailles 1, 2, 3 : " + ", ".join(f"{v:.4f}" for v in parts) + f" ; moyenne {sum(parts) / 3:.4f}")

print("8. Six ensembles au hasard, indépendants : probabilité qu'au moins un contienne une paire donnée de traits")
p_paire = (0 + 1 / comb(8, 2) + comb(6, 1) / comb(8, 3)) / 3
print(f"  par ensemble : {p_paire:.4f} ; sur six : {1 - (1 - p_paire) ** 6:.4f}")

print("9. Modèle synthétique : probabilité que la moitié chère (12 cartes) couvre ce que la moitié bon marché (12) a manqué")
for nom, p in (("forte", 0.5), ("moyenne", 0.25), ("faible", 0.1), ("conditionnelle sans condition", 0.02)):
    q12 = (1 - p) ** 12
    print(f"  {nom} (p = {p}) : manquée par les 12 premières {q12:.4f} ; ajoutée par les 12 autres {q12 * (1 - q12):.4f}")
for nom, compte in (("1 conditionnelle et 2 moyennes", {0.02: 1, 0.25: 2}),
                    ("1 conditionnelle et 3 moyennes", {0.02: 1, 0.25: 3}),
                    ("2 conditionnelles et 2 moyennes", {0.02: 2, 0.25: 2}),
                    ("1 conditionnelle, 2 moyennes et 2 faibles certifiées", {0.02: 1, 0.25: 2, 0.1: 2})):
    survie = 1.0
    for p, k in compte.items():
        q12 = (1 - p) ** 12
        survie *= (1 - q12 * (1 - q12)) ** k
    print(f"  monde à {nom} : probabilité d'au moins une composante ajoutée {1 - survie:.4f}")
