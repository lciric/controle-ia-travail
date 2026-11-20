"""Version 13 : une ligne non dépensée, puis une ligne neuve sur le même arrêt ; la première ouvre-t-elle encore ?"""
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
        print(f"GARDE   {nom} -> {str(e)[:230]}"); return e
incoh_t = lambda t: t.replace('"aire": 0.52', '"aire": 0.52000000000000000001', 1)
autres = TA.en_rangs(TA.lignes_de_scores("juge", "dose-0.50", pas=2, taches=TA.VER[:2]))

print("=== A : ligne 1 non dépensée (sortie incohérente), ligne 2 sur le même arrêt ouvre ; la ligne 1 rouvre-t-elle ?")
X = TA.ArretALEtapeN(T)
g1 = "GO-2099-07-01-01"; c1, f1 = X.reprise(X.L.piece, g1)
_, d = X.scores(); inc = X.sortie_refaite(d, texte=incoh_t)
essai("ligne 1, sortie incohérente", lambda: X.ouvrir(inc, c1, g1, f1))
g2 = "GO-2099-07-01-02"; c2, f2 = X.reprise(X.L.piece, g2)
fs2, d2 = X.scores(); s2 = X.sortie_refaite(d2)
essai("ligne 2, sortie cohérente", lambda: X.ouvrir(s2, c2, g2, f2)["reprise"]["ligne_de_go"])
fs3, d3 = X.scores(lignes=autres); s3 = X.sortie_refaite(d3)
essai("ligne 1 (rang 2), AUTRE sortie cohérente", lambda: X.ouvrir(s3, c1, g1, f1)["reprise"]["ligne_de_go"])
essai("lecture du fichier des scores 2", lambda: type(X.lire(fs2, s2, c2)).__name__)
essai("lecture du fichier des scores 3 sous la ligne 1", lambda: type(X.lire(fs3, s3, c1)).__name__)
print("   actes :", len(X.fichiers("reprise-")), "| constats d'écart :", len(X.fichiers("livraison-refaite-incoherente")))

print("=== B : deux lignes inscrites ensemble sur le même arrêt, aucune dépensée ; deux sorties cohérentes")
Y = TA.ArretALEtapeN(T)
h1 = "GO-2099-07-02-01"; k1, j1 = Y.reprise(Y.L.piece, h1)
h2 = "GO-2099-07-02-02"; k2, j2 = Y.reprise(Y.L.piece, h2)
a1, e1 = Y.scores(); t1 = Y.sortie_refaite(e1)
a2, e2 = Y.scores(lignes=autres); t2 = Y.sortie_refaite(e2)
essai("ligne 2 (rang 3), sortie 1", lambda: Y.ouvrir(t1, k2, h2, j2)["reprise"]["ligne_de_go"])
essai("ligne 1 (rang 2), sortie 2", lambda: Y.ouvrir(t2, k1, h1, j1)["reprise"]["ligne_de_go"])

print("=== C : la même sortie incohérente redonnée ; puis la même pièce à un octet près (autre empreinte)")
Z = TA.ArretALEtapeN(T)
z = "GO-2099-07-03-01"; kz, jz = Z.reprise(Z.L.piece, z)
_, dz = Z.scores(); iz = Z.sortie_refaite(dz, texte=incoh_t)
essai("incohérente", lambda: Z.ouvrir(iz, kz, z, jz))
essai("incohérente redonnée", lambda: Z.ouvrir(iz, kz, z, jz))
essai("issues de la livraison d'origine", lambda: Z.issues(Z.L.piece, Z.L.configuration)["grandeurs_de_l_etape_n"])
fz, dz2 = Z.scores(); sz = Z.sortie_refaite(dz2)
essai("cohérente ensuite", lambda: Z.ouvrir(sz, kz, z, jz)["reprise"]["ligne_de_go"])
essai("incohérente redonnée après l'acte", lambda: Z.ouvrir(iz, kz, z, jz))
print("   actes :", len(Z.fichiers("reprise-")), "| constats d'écart :", len(Z.fichiers("livraison-refaite-incoherente")), "| (m) intacte :", Z.etape_m_intacte())
