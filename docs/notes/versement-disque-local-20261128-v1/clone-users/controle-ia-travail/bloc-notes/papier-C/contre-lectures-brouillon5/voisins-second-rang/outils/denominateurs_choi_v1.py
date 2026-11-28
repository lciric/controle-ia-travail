"""Compatibilité des pourcentages des tableaux 1 et 3 de Choi et al. (2601.04790v1, p. 5 et p. 7)
avec le nombre d'exemples déclaré p. 3 (FairEval : 80 ; Topical-Chat : 60).
Un pourcentage affiché à une décimale est compatible avec n exemples s'il existe un entier k
tel que |100 k / n - x| <= 0,05. Valeurs recopiées des tableaux (texte extrait du PDF empreinté).
Usage : python3 -I -B denominateurs_choi_v1.py
"""


def compatible(x, n):
    return any(abs(100 * k / n - x) <= 0.05 + 1e-9 for k in range(n + 1))


LIGNES = [
    ("Tableau 1, p. 5, Management, DeepSeek R1, colonnes FairEval (t1 t4 t8 t12)", [78.1, 90.6, 90.6, 93.8]),
    ("Tableau 3, p. 7, Management, GPT-4o, colonnes FairEval (t1 t4 t8 t12)", [55.0, 48.3, 51.7, 48.3]),
    ("Tableau 3, p. 7, Management, GPT-4o, colonnes Topical-Chat (t1 t4 t8 t12)", [70.0, 75.0, 73.8, 70.0]),
    ("Témoin : Tableau 1, p. 5, Judge, GPT-4o, colonnes FairEval", [86.3, 85.0, 83.8, 85.0]),
    ("Témoin : Tableau 1, p. 5, Judge, GPT-4o, colonnes Topical-Chat", [58.3, 65.0, 60.0, 56.7]),
]

for nom, valeurs in LIGNES:
    print(nom)
    for x in valeurs:
        print(f"  {x:5.1f} : 80 -> {compatible(x, 80)!s:5}  60 -> {compatible(x, 60)!s:5}  32 -> {compatible(x, 32)!s:5}")
