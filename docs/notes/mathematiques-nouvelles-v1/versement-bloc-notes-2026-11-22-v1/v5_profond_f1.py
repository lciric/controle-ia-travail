import sys
from controle_ia.oracles_plantes_v5.parametres import charger
from controle_ia.oracles_plantes_v5.banque import construire_banque
from controle_ia.oracles_plantes_v5.evaluation import parcourir
p,_ = charger()
for racine in [int(x) for x in sys.argv[1:]]:
    banque = construire_banque(racine, p)
    for m, plantes in banque:
        fact = {"F1": 5, "F2": 10, "F3": 6}[m.famille]
        B = fact * m.N
        if m.famille == "F1":
            m.vt_max = B + 2; m._vt = {0: m._vt[0]}
        if m.famille == "F3":
            m.indice_max = 4000
        for pl in plantes:
            if pl.etiquette != "VERITE_PLANTEE": continue
            f = m.analyser(pl.texte)
            bad = None; nh = 0
            try:
                for inst, st in parcourir(m.ev, f, B):
                    if st in ("F", "I"): bad = (inst, st); break
                    nh += st == "H"
            except Exception as e:
                bad = ("EXC", repr(e))
            if bad or nh:
                print(racine, m.famille, m.indice, pl.gabarit, "B", B, "bad", bad, "H", nh)
    print("racine", racine, "faite")
