"""Diagnostic du juge (processeur seul, racines d'essai) : liste des textes plantés d'une racine, par famille, strate et gabarit."""
import sys, time
from controle_ia.oracles_plantes_v6 import banque, parametres
p, _ = parametres.charger()
r = int(sys.argv[1])
t0 = time.time()
B = banque.construire_banque(r, p)
print("racine", r, "mondes", len(B), "temps", round(time.time() - t0, 1), "s")
for w, (m, pl) in enumerate(B):
    fam = getattr(m, "famille", None) or type(m).__name__
    print(f"--- monde {w} famille {fam} N={getattr(m, 'N', '?')}")
    for x in pl:
        if x.etiquette in ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE"):
            print(f"  [{x.etiquette:14s}] {x.gabarit:45s} | {x.texte}")
