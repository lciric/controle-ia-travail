"""Tables condensees par modele d'erreur x attaque (etendue sur les quatre couples k x T), lues dans ../sorties.
Aucun calcul nouveau. Usage : python3 -B tables_condensees_v1.py"""
import glob
import json
import os

from grille_commun_v1 import ATTAQUES, EFFETS, MODELES

d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sorties")
ab = [json.load(open(f)) for f in glob.glob(os.path.join(d, "ab_*_p0.json"))]
cc = [json.load(open(f)) for f in glob.glob(os.path.join(d, "c_*_p0.json"))]
et = lambda xs: f"{min(xs):.3f} à {max(xs):.3f}" if xs else "—"  # noqa: E731
print("### C-P3a et C-P3b, passe 0 (R = 1000, B = 1000, seuil 0,0638) : étendue du taux sur les couples k × T\n")
print("| modèle d'erreur | attaque | cases | C-P3a, trois lectures | C-P3b, trois lectures | C-P3a, deux lectures | C-P3b, deux lectures | plus grande erreur de Monte-Carlo (trois lectures) | essais non lisibles sous la lecture (ii), a / b |")
print("|---|---|---|---|---|---|---|---|---|")
for m in list(MODELES):
    for a in ATTAQUES:
        x = [r for r in ab if r["modele"] == m and r["attaque"] == a]
        if not x:
            continue
        g = lambda c: [r["taux"][c] for r in x]  # noqa: E731
        em = max(max(r["erreur_mc"]["conj3_a"], r["erreur_mc"]["conj3_b"]) for r in x)
        nl = et([r["part_essais_non_lisibles_ii"]["a"] for r in x]) + " / " + et([r["part_essais_non_lisibles_ii"]["b"] for r in x])
        print(f"| {m} ({MODELES[m]['doc']}) | {ATTAQUES[a]:.2f} | {len(x)} | {et(g('conj3_a'))} | {et(g('conj3_b'))} | {et(g('conj2_a'))} | {et(g('conj2_b'))} | {em:.3f} | {nl} |")
print("\n### C-P3c, passe 0 (R = 8000, seuil 0,0549) : étendue du taux aux trois lectures jointes sur les couples k × T ; entre parenthèses, nombre de cases au-dessus du seuil\n")
bras = ["bruit", "insertion_kP3_lie", "insertion_kP1_lie", "contenu_kP3_lie", "contenu_kP1_lie", "insertion_kP3_fort", "contenu_kP3_fort", "insertion_S_separe_kP3_lie"]
print("| modèle d'erreur | attaque | " + " | ".join(bras) + " | deux lectures, insertion_kP3_lie |")
print("|---|---|" + "---|" * (len(bras) + 1))
for m in list(MODELES):
    for a in ATTAQUES:
        x = [r for r in cc if r["modele"] == m and r["attaque"] == a]
        cells = []
        for b in bras:
            v = [r["taux"][f"{b}|conj3"] for r in x if r["taux"][f"{b}|conj3"] is not None]
            n = sum(1 for r in x if r["taux"][f"{b}|conj3"] is not None and r["taux"][f"{b}|conj3"] > r["seuil_clause"])
            cells.append(f"{et(v)} ({n}/{len(v)})" if v else "non défini")
        v2 = [r["taux"]["insertion_kP3_lie|conj2"] for r in x]
        print(f"| {m} | {ATTAQUES[a]:.2f} | " + " | ".join(cells) + f" | {et(v2)} |")
print(f"\nPlus grande erreur de Monte-Carlo d'un taux de C-P3c (cases nulles) : {max(v for r in cc if r['modele'] not in EFFETS for v in r['erreur_mc'].values() if v is not None):.4f}")
