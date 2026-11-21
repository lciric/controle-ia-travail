import time, sys
import numpy as np
from controle_ia.iib import jouet_v5 as jo, oracle_v5 as ov, regenere_v5 as rg, jumeau_v5 as jm, configuration_v5 as cf, epreuve_centrage_v5 as ec, regle_v5 as rv, controle_premier_cout_v5 as pc
cfg = cf.gabarit("jouet")
t0 = time.time()
def etal(entropie, n_taches=32):
    g = jm.Graines(entropie)
    m = jo.ModeleJouetDeLangue()
    lignes = {("P","h"): [], ("N","h"): [], ("P","r"): [], ("N","r"): []}
    for k in range(n_taches):
        for e in range(2):
            ep = f"t{k}/e{e}"
            ga = [g.entiers(f"iib/etalonnage/honnete/{ep}", 10)]
            h = rg.jouer_lot(m, [jo.EnvironnementJouet(f"t{k}")], [ep], ga, 400, 1.0)[0]
            r = rg.jouer_regeneres(m, [jo.EnvironnementJouet(f"t{k}")], [ep], ga, g, cfg, [h])[0]
            oh = ov.oracles_episode(m, jo.EnvironnementJouet(f"t{k}"), h["actions"], g, cfg, "etalonnage-honnete", ep)
            orr = ov.oracles_episode(m, jo.EnvironnementJouet(f"t{k}"), r["actions"], g, cfg, "etalonnage-regenere", ep)
            for o in "PN":
                lignes[(o,"h")] += oh["sorties"][o]; lignes[(o,"r")] += orr["sorties"][o]
    return lignes
L = etal(1)
print("jeu", round(time.time()-t0,2)); t0 = time.time()
for o in "PN":
    r = ec.epreuve_du_centrage(o, L[("P","h")], L[("N","h")], L[("N","r")], cfg)
    print(o, r["passe"], {k: (round(v["probabilite"],4) if v["probabilite"] is not None else None, v["effectif"]) for k, v in r["composantes"].items()}, r["composantes"].get("pente_de_fuite",{}).get("pente"))
print("centrage", round(time.time()-t0,2))
from controle_ia.iib import epreuves_v5 as ev
for o in "PN":
    for ph in "hr":
        eps = ev.par_episode(L[(o,ph)])
        acc = [rv.accepter(v, cfg["regle"][o], o) for v in eps.values()]
        print(o, ph, sum(a["accepte"] for a in acc), {m: sum(a["motif"]==m for a in acc) for m in rv.MOTIFS}, np.mean([l["exces"] for l in L[(o,ph)] if l["bornable"]]).round(3), sum(l["bornable"] for l in L[(o,ph)]))
print(pc.controle([l for l in L[("P","h")] if l["pas"]==0], pc.GROUPE_DE_VALIDITE, cfg)["phrase"])
