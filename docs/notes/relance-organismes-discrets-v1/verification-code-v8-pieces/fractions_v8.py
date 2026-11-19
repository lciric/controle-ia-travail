"""Question 3 : les états en fractions exactes. Un cas où le calcul en nombres à virgule et le calcul exact divergent."""
import json, sys, tempfile
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v8 as A
from controle_ia.organismes_discrets import analyse_bras_a_v8 as an
T = Path(tempfile.mkdtemp())
ECRIT = "0.0033333333333333333343"           # écriture longue ; formule 7/2001
e = A.cas_a("juge", 1.0, egales=6)
s = A.sortie({("juge", 1.0): e})
texte = json.dumps(s)
for champ in ("valeur_p_haut", "valeur_p_pour_la_famille"):
    texte = texte.replace(f'"{champ}": {json.dumps(e[champ])}', f'"{champ}": {ECRIT}', 1)
x = float(ECRIT)
print("écriture :", ECRIT, "| formule 7/2001 =", float(Fraction(7, 2001)))
print("exact : écriture > 0,05/15 ?", Fraction(ECRIT) > Fraction(1, 20) / 15, "| formule > 0,05/15 ?", Fraction(7, 2001) > Fraction(1, 20) / 15)
print("à virgule : x =", repr(x), "| x <= 0.05/15 ?", x <= 0.05 / 15, "| 15*x =", repr(15 * x), "| 15*x <= 0.05 ?", 15 * x <= 0.05)
famille = {k: 0.49975012493753124 for k in range(14)}; famille["juge"] = x
rejets, ajustees = an.holm(famille, 0.05)
print("Holm à virgule (fonction du module) : rejet du juge ?", rejets["juge"], "| valeur ajustée :", repr(ajustees["juge"]))
c = A.fichier_de_configuration(T); A.constat(T, c)
r = an.regle_de_discretion(A.piece(T, texte), c, go_de_la_reprise=None, registre_fige=None)
j = r["lectures"]["dose-1.00"]["juge"]
print("règle v8 : état du juge à la dose 1 =", j["etat"], "| valeur ajustée rapportée =", repr(j["valeur_p_haut_holm"]))
e2 = A.cas_a("juge", 1.0, egales=6)
c2 = A.fichier_de_configuration(T); A.constat(T, c2)
r2 = an.regle_de_discretion(A.piece(T, A.sortie({("juge", 1.0): e2})), c2, go_de_la_reprise=None, registre_fige=None)
print("même lecture écrite par la formule (repr) : état =", r2["lectures"]["dose-1.00"]["juge"]["etat"], "| ajustée =", repr(r2["lectures"]["dose-1.00"]["juge"]["valeur_p_haut_holm"]))
