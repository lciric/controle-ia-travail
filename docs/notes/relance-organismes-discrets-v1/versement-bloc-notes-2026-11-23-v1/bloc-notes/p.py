import sys; sys.path.insert(0,'tests'); sys.path.insert(0,'src')
from test_lots_bras_a_v2 import *
s=sep()
tous=plans(s.ouvertes)
kc=couverture(s,sans=tous[:40])
print(type(kc).__name__)
try:
    decisif(lot_honnete_couverture_=kc)
except Exception as e: print(type(e).__name__, str(e)[:100])
# 128 / 64 boundary
for n in (127,128,129):
    h=L.lot_honnete_appariement(s,E,n_jugeables(s.ouvertes,n)); print(n,h.comptes["controles-autre-tache"],h.empreinte[:8])
# ancre jumeaux with constat on ancre plans
kp=L.ancre_plans_honnetes(s,E,L.lot_honnete_appariement(s,E,n_jugeables(s.ouvertes,20)))
print(type(kp).__name__, type(L.ancre_jumeaux(s,E,deplacees(s.ouvertes))).__name__)
try: L.voie_de_service_du_juge(L.ancre_jumeaux(s,E,n_a_effet(s.ouvertes,10)))
except Exception as e: print(type(e).__name__, str(e)[:100])
# jumeaux couverture: swap set same size
lot=couverture(s, laisses=tous[:3])
d2=[p for p in tous if p not in tous[1:4]]
try:
    r=L.lot_jumeaux_couverture(s,E,lot,d2,tous[1:4]); print("accepté swap", len(r.appels))
except Exception as e: print(type(e).__name__, str(e)[:100])
