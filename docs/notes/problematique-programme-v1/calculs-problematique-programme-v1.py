#!/usr/bin/env python3
"""Rang des mécanismes par le produit impact x coût x faisabilité x rapidité, et sensibilité de ce rang.

Pièce de travail (classe C), compagnon de `reponse-fable-problematique-v1.md` (§ 4). Bibliothèque standard seule,
aucun tirage, aucune donnée du programme : les notes ci-dessous sont des JUGEMENTS du concepteur, sur quatre échelles
de 1 à 5 où le plus haut est le meilleur (coût : 5 = 0 USD ; rapidité : 5 = heures à jours). Le script ne mesure
rien : il dit seulement ce que l'ordre doit aux notes, en déplaçant chaque note d'un cran, une à la fois.

Rejeu : python3 -I calculs-problematique-programme-v1.py > calculs-problematique-programme-v1.txt
"""

# (nom, impact, coût, faisabilité, rapidité)
MECANISMES = [
    ("plancher d'audit au hasard, et bilan de la pince (même garantie)", 5, 5, 5, 5),
    ("ligne d'arrêt « aucun score du suspect dans l'étalonnage », loi exacte à deux lots", 4, 5, 5, 5),
    ("loi de la référence honnête : mondes plantés, prévision scellée", 5, 5, 4, 4),
    ("netteté de la référence, mesurée sans aucune attaque", 4, 5, 4, 4),
    ("audit des tolérances de nos textes scellés", 3, 5, 4, 5),
    ("courbe de transport entre régimes et inventaire des régimes", 3, 5, 5, 4),
    ("recapture, à une et à deux mâchoires", 4, 4, 4, 4),
    ("seuil des témoins du régime d'usage", 4, 3, 5, 4),
    ("agrégateur adaptatif sur rangs exacts (mondes plantés)", 3, 5, 4, 4),
    ("bilan du produit fermé contre le jumeau honnête", 4, 4, 3, 3),
    ("hasard du défenseur : test de permutation sur une condition tirée au sort", 3, 4, 3, 4),
    ("dissociation « passera le contrôle » / « a bien fait la tâche » chez l'honnête", 5, 4, 3, 3),
    ("canal des poids (saboteur à adaptateur seulement)", 2, 5, 3, 4),
    ("rang contre des tirages du jumeau (nul propre à chaque acte)", 4, 2, 3, 3),
    ("attestation causale de la sonde par micro-interventions secrètes", 5, 3, 2, 2),
    ("passage obligé : bascule en profondeur", 5, 4, 1, 3),
    ("dilemme valeur-issue (réussite attendue lue contre issue calculée)", 3, 3, 2, 3),
    ("passage obligé : sondes de conséquences attendues", 3, 3, 2, 2),
    ("banc public à vérité plantée", 5, 1, 3, 2),
]
FACTEURS = ("impact", "coût", "faisabilité", "rapidité")
TEMOIN_BAS = ("masse manquante des familles d'attaque (occupé, garantie nulle face à un adversaire qui choisit)", 1, 5, 1, 5)


def produit(notes):
    p = 1
    for n in notes:
        p *= n
    return p


def rangs(table):
    """Rang de compétition (1 = meilleur) : les ex aequo partagent le meilleur rang."""
    prods = [produit(m[1:]) for m in table]
    return [1 + sum(1 for q in prods if q > p) for p in prods]


def main():
    base = rangs(MECANISMES)
    prods = [produit(m[1:]) for m in MECANISMES]
    n = len(MECANISMES)
    rmin, rmax = list(base), list(base)
    essais = 0
    sorties_top5 = [0] * n
    for i in range(n):
        for k in range(4):
            for d in (-1, +1):
                v = MECANISMES[i][1 + k] + d
                if not 1 <= v <= 5:
                    continue
                essais += 1
                t = [list(m) for m in MECANISMES]
                t[i][1 + k] = v
                r = rangs([tuple(m) for m in t])
                for j in range(n):
                    rmin[j] = min(rmin[j], r[j])
                    rmax[j] = max(rmax[j], r[j])
                    if base[j] <= 5 and r[j] > 5:
                        sorties_top5[j] += 1
    print("A. Produit et rang (jugements du concepteur, échelles de 1 à 5, plus haut = mieux)")
    ordre = sorted(range(n), key=lambda j: (-prods[j], j))
    for j in ordre:
        m = MECANISMES[j]
        print(f"  rang {base[j]:2d}  produit {prods[j]:3d}  I{m[1]} C{m[2]} F{m[3]} R{m[4]}  {m[0]}")
    print()
    print(f"B. Sensibilité : chaque note déplacée d'un cran, une à la fois ({essais} essais, bornes 1 et 5 respectées)")
    for j in ordre:
        extra = f" ; sort des cinq premiers dans {sorties_top5[j]} essais sur {essais}" if base[j] <= 5 else ""
        print(f"  rang {base[j]:2d}, de {rmin[j]:2d} à {rmax[j]:2d}{extra}  {MECANISMES[j][0]}")
    print()
    print("C. Objets de contrôle du classement")
    haut = MECANISMES[0]
    t = MECANISMES + [TEMOIN_BAS]
    r = rangs(t)
    print(f"  témoin qui doit finir dernier : rang {r[-1]} sur {len(t)} (produit {produit(TEMOIN_BAS[1:])}) : {TEMOIN_BAS[0]}")
    print(f"  témoin qui doit finir premier : rang {base[0]} (produit {produit(haut[1:])}), jamais au-delà du rang {rmax[0]} : {haut[0]}")
    print()
    print("D. File des paris : faisabilité de 2 ou moins, ou coût de 1, rangés par l'impact puis par le produit")
    paris = [j for j in range(n) if MECANISMES[j][3] <= 2 or MECANISMES[j][2] == 1]
    for j in sorted(paris, key=lambda j: (-MECANISMES[j][1], -prods[j], j)):
        m = MECANISMES[j]
        print(f"  impact {m[1]}  produit {prods[j]:3d}  {m[0]}")
    print()
    print("E. Ce que le produit ne sait pas : les dépendances et ce qui fausse nos chiffres (lu dans la note, § 4)")
    print("  ordre retenu dans la note pour les cinq premiers : plancher ; loi de la référence honnête ; témoins du")
    print("  régime d'usage (avec la ligne d'arrêt) ; recapture ; netteté de la référence.")
    retenus = [0, 2, 7, 6, 3]
    print("  rangs par le produit nu de ces cinq-là : " + ", ".join(str(base[j]) for j in retenus))


if __name__ == "__main__":
    main()
