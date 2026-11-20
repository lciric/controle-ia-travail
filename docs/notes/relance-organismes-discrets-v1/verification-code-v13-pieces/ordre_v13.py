"""Version 13, ordre des gardes : un constat d'écart sous un contrôle de lancement malsain."""
import contextlib, io, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v13 as A
with contextlib.redirect_stdout(io.StringIO()):
    import test_analyse_bras_a_v13 as TA
from controle_ia.organismes_discrets import analyse_bras_a_v13 as an, arrets_bras_a_v12 as ar
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {str(r)[:160]}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:200]}"); return e
incoh_t = lambda t: t.replace('"aire": 0.52', '"aire": 0.52000000000000000001', 1)
X = TA.ArretALEtapeN(T)
g = "GO-2099-08-01-01"; c, fg = X.reprise(X.L.piece, g)
rev = f"| GO-2099-08-01-09 | 2099 | révocation | {g} révoquée |"
r = essai("contrôle, la ligne de GO révoquée au registre courant", lambda: A.controle(T, c, fg, ligne_de_go=g, lignes_de_plus=[rev]))
print("   contrôle sain ?", (not isinstance(r, BaseException)) and not r[2], "| causes :", None if isinstance(r, BaseException) else r[2])
_, d = X.scores(); inc = X.sortie_refaite(d, texte=incoh_t)
essai("sortie incohérente sous le contrôle malsain", lambda: X.ouvrir(inc, c, g, fg))
print("   constats d'écart :", len(X.fichiers("livraison-refaite-incoherente")), "| actes :", len(X.fichiers("reprise-")))
_, d2 = X.scores(); s2 = X.sortie_refaite(d2)
essai("sortie cohérente sous le contrôle malsain", lambda: X.ouvrir(s2, c, g, fg))
print("   actes :", len(X.fichiers("reprise-")))
essai("issues de la sortie incohérente", lambda: X.issues(inc, c))
essai("issues de la livraison d'origine", lambda: X.issues(X.L.piece, X.L.configuration)["grandeurs_de_l_etape_n"])
essai("contrôle refait, sain", lambda: A.controle(T, c, fg, ligne_de_go=g, date_utc="2099-01-05T00:00:00Z")[2])
essai("sortie incohérente, contrôle sain", lambda: X.ouvrir(inc, c, g, fg))
essai("sortie cohérente, contrôle sain", lambda: X.ouvrir(s2, c, g, fg)["reprise"]["ligne_de_go"])
print("   constats d'écart :", len(X.fichiers("livraison-refaite-incoherente")), "| actes :", len(X.fichiers("reprise-")), "| (m) intacte :", X.etape_m_intacte())
# un constat d'écart planté à la main, pour une sortie COHÉRENTE : bloque-t-il la reprise ?
Y = TA.ArretALEtapeN(T)
h = "GO-2099-08-02-01"; k, j = Y.reprise(Y.L.piece, h)
_, e = Y.scores(); t = Y.sortie_refaite(e)
import json
from controle_ia.scellement import sceller
p = Y.dossier / an.NOM_DES_CONSTATS_D_INCOHERENCE.format(A.empreinte(t)[:16])
p.write_text(json.dumps({"evenement": an.EVENEMENT_DE_LIVRAISON_REFAITE_INCOHERENTE, "sha256_de_la_livraison_refaite": A.empreinte(t),
                         "sha256_de_la_livraison_d_origine": A.empreinte(Y.L.piece), "sha256_de_la_configuration": A.empreinte(k)}), encoding="utf-8")
sceller(p)
essai("constat d'écart planté pour une sortie cohérente", lambda: Y.ouvrir(t, k, h, j))
