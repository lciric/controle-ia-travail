import sys, time, numpy as np, torch
sys.path.insert(0, "tests")
import aide_t07bbis_jeux_v4 as J
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
torch.use_deterministic_algorithms(True); torch.set_num_threads(4)
O = ac.entrainer
def essai(nom, app, y, ctrl):
    t=time.time()
    lot = ac.LotCarte(app, "cpu")
    a = O(lot, "lineaire", "a", 15, y, 1e-3, 11)
    b = J.carte_emulee(ac, app, O)(lot, "lineaire", "b", 15, y, 1e-3, 11)
    e = ac.ecart_relatif(ac.scores(a, ctrl), ac.scores(b, ctrl))
    print(nom, f"{e:.3e}", round(time.time()-t,1), flush=True)
app,y,ctrl,_ = J.jeu_residuel("residuel", 640, 256, 1024, 40, 120, 0.2, 0.9, 300.0, 1, gabarits=0.4)
essai("quasi-copies c1", app, y, ctrl)
for c in (11,12,13,14,21,22):
    sig = 0.0 if c > 20 else 0.3
    app,y,ctrl,_ = J.jeu_anisotrope(c, signal=sig)
    essai(f"aniso c{c}", app, [int(v) for v in y] and y, ctrl)
