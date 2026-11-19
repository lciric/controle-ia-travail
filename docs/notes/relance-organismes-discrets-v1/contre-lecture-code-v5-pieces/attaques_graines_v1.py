"""Essais d'attaque des graines (C-7, M-2). Synthétique."""
import tempfile
from pathlib import Path
import numpy as np
from controle_ia.organismes_discrets import graines_bras_a_v5 as g, analyse_bras_a_v5 as an
from controle_ia.gardes import GardeArret
def essai(nom, f):
    try: print("PASSE  ", nom, "->", f())
    except GardeArret as e: print("REFUS  ", nom, "->", str(e)[:120])
# C-7 : jeton du module, générateur du système
t = g.TirageAClef(g._JETON, "bras-a-v2/perm/page", 0, np.random.default_rng(), False)
essai("C-7 tirage fabrique avec le jeton du module et un generateur du systeme", lambda: an.page(np.arange(10).reshape(5, 2) * 1.0, t, n=50)[1] > 0)
t2 = object.__new__(g.TirageAClef); object.__setattr__(t2, "cle", "bras-a-v2/perm/page"); object.__setattr__(t2, "entropie", 0)
object.__setattr__(t2, "cote_habilite", False); object.__setattr__(t2, "_generateur", np.random.default_rng())
essai("C-7 tirage fabrique par object.__new__", lambda: an.page(np.arange(10).reshape(5, 2) * 1.0, t2, n=50)[1] > 0)
# réemploi d'un même tirage : deux intervalles différents
tir = g.tirage_de(g.cle("boot", "taches", "lot-decisif"), 7)
vals = {f"t{i}": float(i) for i in range(16)}
a, b = an.intervalle_rapporte(vals, tir)["percentiles"], an.intervalle_rapporte(vals, tir)["percentiles"]
print("REEMPLOI d'un meme tirage a cle : memes percentiles ?", a == b)
# M-2 : ligne de GO qui refuse, mais nomme R9 et les identifiants
d = Path(tempfile.mkdtemp()); r = d / "go.md"
r.write_text("| GO-2026-11-20-01 | 2026-11-20 | décision | Lazar refuse l'écart à R9 pour la table des identifiants | — |\n", encoding="utf-8")
essai("M-2 ligne de GO qui REFUSE l'ecart (mots presents)", lambda: g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar="GO-2026-11-20-01", registre_des_go=r)["go"])
