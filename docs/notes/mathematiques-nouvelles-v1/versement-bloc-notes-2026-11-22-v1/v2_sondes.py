import os, tempfile, json, copy
import numpy as np
from controle_ia.gardes import GardeArret
from controle_ia.oracles_plantes_v2.parametres import charger
from controle_ia.oracles_plantes_v2.banque import construire_banque
from controle_ia.oracles_plantes_v2.tests_de_mort import appliquer_batterie, sortie_de_texte, t5_redite, appliquer_t6
from controle_ia.oracles_plantes_v2.normalisation import normaliser
from controle_ia.oracles_plantes_v2.lignee import Registre, rejouer
from controle_ia.oracles_plantes_v2.cles import octets_json, verifier_absence_fuite
from controle_ia.oracles_plantes_v2.mondes import lit
p,_ = charger()
banque = construire_banque(11, p)
f3, pl3 = banque[8]
def reg():
    return Registre(os.path.join(tempfile.mkdtemp(), "r.jsonl"))
def essai(m, t, **kw):
    try:
        r = appliquer_batterie(sortie_de_texte(t), m, **kw)
        print("  ", t[:110], "->", r.statut, [(i.test, i.type.value) for i in r.issues][-2:])
        return r
    except Exception as e:
        print("  ", t[:110], "-> EXCEPTION", type(e).__name__, e)
print("R1")
for t in ["(pour tout n dans NAT, u(n) >= 0) et vrai", "(pour tout n dans NAT, u(n) >= 1) ou faux",
          "vrai et (pour tout n dans NAT, u(n) >= 0)", "non (pour tout n dans NAT, u(n) >= 0)",
          "pour tout n dans NAT, (pour tout m dans NAT, u(n + m) >= 0)"]:
    essai(f3, t)
print("R2")
R = reg()
C0 = f3.U1**2 - f3.U0*f3.u(2)
essai(f3, f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) + w(n - 1) - w(n - 1) = {lit(C0)} * (-QU)^n", registre=R)
essai(f3, f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = {lit(C0)} * (-QU)^n", registre=R)
essai(f3, "pour tout n dans NAT, w(n - 1) * 0 = 0", registre=R)
essai(f3, "pour tout n dans NAT, n + 1 > n", registre=R)
print("R13 vacuité qui empoisonne « V »")
R = reg()
essai(f3, "pour tout n dans NAT, n > N + 5 implique 0 = 0", registre=R)
essai(f3, "pour tout n dans NAT, n + 1 > n", registre=R)
essai(f3, "1 = 1", registre=R)
print("R3")
def fo(t): return normaliser(f3.analyser(t), f3, f3.ev)
a = "pour tout n dans NAT, n >= 1 implique mod(w(30 * n), w(n)) = 0"
b = "pour tout n dans NAT, n >= 1 implique mod(w(30 * n), w(3 * n)) = 0"
print("  ", t5_redite(fo(b), f3, [fo(a)]).type.value)
print("R4")
d = tempfile.mkdtemp(); ch = os.path.join(d, "l.jsonl")
r = Registre(ch); r.inscrire("a"*64, "vivante", "b", "x"); r.inscrire("a"*64, "morte", "T6", "y")
lignes = open(ch).read().splitlines()
open(ch, "w").write(lignes[0] + "\n")
try: print("  ", rejouer(ch))
except GardeArret as e: print("   troncature refusée")
open(ch, "w").write(lignes[0] + "\n" + lignes[1].replace('"morte"', '"vivante"') + "\n")
try: print("  ", rejouer(ch))
except GardeArret as e: print("   modification refusée")
os.remove(ch + ".tete.json")
try: print("   sans tête :", rejouer(ch))
except GardeArret as e: print("   tête retirée refusée")
print("R6")
for servi in ({"items": [{"instance": {"n": 17}}]}, {"x": {"n": 17}}):
    try:
        verifier_absence_fuite(octets_json(servi), [json.dumps({"n": 17}, sort_keys=True)]); print("   non détectée")
    except GardeArret: print("   détectée")
