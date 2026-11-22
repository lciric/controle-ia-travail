import sys, traceback
from controle_ia.oracles_plantes_v1.parametres import charger
from controle_ia.oracles_plantes_v1.banque import construire_mondes
from controle_ia.oracles_plantes_v1.tests_de_mort import appliquer_batterie, sortie_de_texte, t2_contre_exemple
from controle_ia.oracles_plantes_v1.lignee import Registre
p,_ = charger()
ms = construire_mondes(11, p)
f3 = ms[8]; f1 = ms[0]; f2 = ms[4]
print("F3", f3.PU, f3.QU, f3.U0, f3.U1, f3.AV, f3.BV, f3.V0, "N", f3.N)
def essai(m, t, **kw):
    try:
        r = appliquer_batterie(sortie_de_texte(t), m, **kw)
        print(repr(t), "->", r.statut, [ (i.test,i.type.value) for i in r.issues])
        return r
    except Exception as e:
        print(repr(t), "-> EXCEPTION", type(e).__name__, e)
for t in ["(pour tout n dans NAT, u(n) >= 0) et vrai",
          "(pour tout n dans NAT, u(n) >= 0) implique faux",
          "(pour tout n dans NAT, u(n) >= 1) ou faux",
          "(pour tout n dans NAT, u(n) >= 1)",
          ]:
    essai(f3, t)
import tempfile, os
d = tempfile.mkdtemp()
reg = Registre(os.path.join(d, "r.jsonl"))
essai(f3, "pour tout n dans NAT, u(n) + 0 * w(n - 1) > 0", registre=reg)
essai(f3, "pour tout n dans NAT, u(n) > 0", registre=reg)
C0 = f3.U1**2 - f3.U0*f3.u(2)
from controle_ia.oracles_plantes_v1.mondes import lit
essai(f3, f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) + w(n - 1) - w(n - 1) = {lit(C0)} * (-QU)^n", registre=reg)
essai(f3, f"pour tout n dans NAT, u(n + 1)^2 - u(n) * u(n + 2) = {lit(C0)} * (-QU)^n", registre=reg)
