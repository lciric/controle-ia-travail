"""Essais d'attaque v6 des graines (M-1, M-2). Synthétique."""
import numpy as np
from controle_ia.organismes_discrets import graines_bras_a_v6 as g, analyse_bras_a_v6 as an
from controle_ia.gardes import GardeArret
def essai(nom, f):
    try: print("PASSE  ", nom, "->", f())
    except GardeArret as e: print("REFUS  ", nom, "->", str(e)[:110])
B = np.arange(10).reshape(5, 2) * 1.0
essai("jeton du module, generateur du systeme", lambda: an.page(B, g.TirageAClef(g._JETON, "bras-a-v2/perm/page", 0, np.random.default_rng(), False), n=50)[1] > 0)
t2 = object.__new__(g.TirageAClef)
for k, x in (("cle", "bras-a-v2/perm/page"), ("entropie", 0), ("cote_habilite", False), ("_generateur", np.random.default_rng())):
    object.__setattr__(t2, k, x)
essai("object.__new__", lambda: an.page(B, t2, n=50)[1] > 0)
essai("jeton + _inscrire (fraude par les noms prives)", lambda: an.page(B, g._inscrire(g.TirageAClef(g._JETON, "bras-a-v2/perm/page", 0, np.random.default_rng(), False)), n=50)[1] > 0)
t = g.tirage_de(g.cle("perm", "page"), 1)
a = t._generateur
object.__setattr__(t, "_generateur", np.random.default_rng())
essai("generateur remplace dans un tirage authentique (object.__setattr__)", lambda: an.page(B, t, n=50)[1] > 0)
tir = g.tirage_de(g.cle("boot", "taches", "lot-decisif"), 7)
vals = {f"t{i}": float(i) for i in range(16)}
an.intervalle_rapporte(vals, tir)
essai("reemploi d'un tirage", lambda: an.intervalle_rapporte(vals, tir)["percentiles"])
x1 = an.intervalle_rapporte(vals, g.tirage_de(g.cle("boot", "taches", "lot-decisif"), 7))["percentiles"]
x2 = an.intervalle_rapporte(vals, g.tirage_de(g.cle("boot", "taches", "lot-decisif"), 7))["percentiles"]
print("REJEU  deux tirages refaits de la meme cle : memes percentiles ?", x1 == x2)
essai("porte R9 : reglage refuse", lambda: g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, reglage=g.ECART_A_R9_REFUSE, go_de_lazar="GO-2026-11-19-70"))
essai("porte R9 : GO-2026-11-19-70 (registre du depot, sans la phrase)", lambda: g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar="GO-2026-11-19-70"))
print("registre lu :", g.REGISTRE_DES_ACCORDS)
