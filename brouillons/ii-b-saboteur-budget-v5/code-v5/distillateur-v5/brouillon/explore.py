import time
from controle_ia.iib import configuration_v5 as cf, jumeau_v5 as jm, oracle_v5 as ov, regenere_v5 as rg, temoin_jumeau_v5 as tj
from controle_ia.iib.jouet_v5 import SIGNAL_MAITRE, EnvironnementJouet
from controle_ia.iib.jouet_distillation_v5 import ModeleJouetEleve
from controle_ia.iib.regle_v5 import accepter
CFG = cf.gabarit("jouet")
m = ModeleJouetEleve(); g = jm.Graines(2026112101)
t0=time.time(); nP=nN=0
for k in range(24):
    nom=f"r{k}/tour1"
    ep = rg.jouer_lot(m, [EnvironnementJouet(f"r{k}", consigne=SIGNAL_MAITRE, indication=SIGNAL_MAITRE)], [nom], [g.entiers(f"iib/maitre/r{k}/tour1", 10)], 400, 1.0)[0]
    o = ov.oracles_episode(m, EnvironnementJouet(f"r{k}"), ep["actions"], g, CFG, "maitre", nom)
    dP = accepter(o["sorties"]["P"], CFG["regle"]["P"], "P"); dN = accepter(o["sorties"]["N"], CFG["regle"]["N"], "N")
    nP+=dP["accepte"]; nN+=dN["accepte"]
print(nP, nN, time.time()-t0)
