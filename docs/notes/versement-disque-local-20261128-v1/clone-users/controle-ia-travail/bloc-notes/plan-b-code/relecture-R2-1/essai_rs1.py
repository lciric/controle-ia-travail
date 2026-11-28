import sys
sys.path.insert(0, sys.argv[1])
from controle_ia.environnements.rubrique import lire_une_note, _ENTIER, _FRACTION
from controle_ia.environnements.rubrique_simplifiee import controle_suite, lire_reponse_rs1
print("ENTIER", _ENTIER.pattern, "FRACTION", _FRACTION.pattern)
for v in ["3 / 4", "3 /5", "3/ 5", "3 out of 5", "3 (out of 5)", "3/5 (solid)", "4 (2 weak points)", "3, solid",
          "3; 4", "3 and 4", "3 (4)", "3/5, 4/5", "3 4", "3 vs 4", "3 & 4", "3, 4/5", "3,4", "3;4", "3(4)",
          "3 to 4", "3 or 4", "3 - 4", "3 -4", "3 – 4", "+3", "−1", "3.0 to 4.0", "3.0, 4", "3/5 - 4/5", "3 (or 4)",
          "4/5 or 5/5", "3 ⁄ 5", "3 =4", "3 + 1", "3 +1", "3/5 and 4/5", "3and4", "3 And 4", "3 AND 4"]:
    print(repr(v), "suite:", controle_suite(v), "gelée:", lire_une_note(v, 0, 5))
