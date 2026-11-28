import sys
sys.path.insert(0, "tests")
from controle_ia.environnements import juges
vrai = juges.charger_invite
juges.charger_invite = lambda i, *a, **k: ("## Scoring Rubric\nSPECIFICITY: <score>\nCOHERENCE: <score>\n" if i == "H4" else vrai(i, *a, **k))
import test_plan_b_juges_simplifies as T
from controle_ia.environnements import juges_simplifies as js, requalifier_juges as rq
from controle_ia.harnais.modeles import modele_jouet
m = modele_jouet(5, len(T.TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
for base in (70, 80, 90, 100):
    dem = [{"cle": f"k{i}", "questions": "Why do routers matter?", "ensemble": f"PROPOSAL 1: idée {i}", "classification": None} for i in range(4)]
    g = {d["cle"]: base + i for i, d in enumerate(dem)}
    L = js.jouer_lot_de_notations(m, T.FMT, dem, g, "b0", [0, 1, 2], 30, 1.0, 1e-5, "q99")
    D = js.jouer_lot_de_notations(m, T.FMT, dem, g, "b0", [0, 1, 2], 30, 1.0, 1e-5, "q99", decalage_positions=1)
    for x, y in zip(L, D):
        r = x["rapport"]; n = r["positions_capturees"]; z = r["controle_negatif_zone_generee"]
        pos = None if z is None else min(v["positions"] for v in z.values())
        print(base, x["notation"]["jetons_reponse"], n, r["longueurs_contexte"], pos, rq.k_angle_mort(n-1), max(r["ecarts_q99"].values()), None if z is None else min(v["q99"] for v in z.values()), max(y["rapport"]["ecarts_q99"].values()))
