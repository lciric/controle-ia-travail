"""Partie 3 : retrait d'une configuration LUE, puis seconde configuration ; reprise après sortie incohérente."""
import contextlib, io, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v12 as A
with contextlib.redirect_stdout(io.StringIO()):
    import test_analyse_bras_a_v12 as TA
from controle_ia.organismes_discrets import analyse_bras_a_v12 as an, arrets_bras_a_v12 as ar, configuration_bras_a_v12 as cf
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {str(r)[:200]}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:220]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
lire = lambda p, c, go=None, fige=None: an.regle_de_discretion(p, c, go_de_la_reprise=go, registre_fige=fige)
rg = A.reglages(cf.SCHEMA_ECHANGE); rg["statistique_agregateur"] = "neuve (essai)"

c_lue = A.fichier_de_configuration(T, course=A.nouvelle_course(T), rang=1)
A.constat(T, c_lue); essai("configuration lue : pièce A", lambda: etat(lire(A.piece(T, A.sortie(piece_source="A")), c_lue)))
c_neuve = A.fichier_de_configuration(T, course=A.nouvelle_course(T), rang=1, statistique_agregateur="neuve (essai)")
ins_lue = A.ligne_d_inscription(c_lue, go="GO-2099-12-29-01")
essai("constat d'une autre configuration, la lue encore inscrite", lambda: A.constat_et_causes(T, c_neuve, lignes_de_plus=[ins_lue])[2])
essai("constat, la lue « révoquée » après sa lecture", lambda: A.constat_et_causes(T, c_neuve, lignes_de_plus=[ins_lue, f"| GO-2099-12-29-02 | 2099 | révocation | {A.empreinte(c_lue)} |"])[1] is not None)
essai("seconde course : pièce B (« repère »)", lambda: etat(lire(A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, egales=0)}, piece_source="B", reglages=rg)), c_neuve)))

print("=== après une sortie refaite incohérente")
X = TA.ArretALEtapeN(T)
go = "GO-2099-05-03-01"; c, fg = X.reprise(X.L.piece, go)
f, decl = X.scores()
incoh = X.sortie_refaite(decl, texte=lambda t: t.replace('"aire": 0.52', '"aire": 0.52000000000000000001', 1))
essai("ouverture, incohérente", lambda: X.ouvrir(incoh, c, go, fg)["reprise"]["ligne_de_go"])
ci = X.fichiers("livraison-refaite-incoherente")
print("   constat :", [p.name for p in ci])
essai("lecture du fichier des scores sous la sortie incohérente", lambda: type(X.lire(f, incoh, c)).__name__)
go2 = "GO-2099-05-03-02"
r = essai("ligne neuve qui cite l'arrêt d'origine", lambda: X.reprise(X.L.piece, go2))
if isinstance(r, tuple):
    f2, d2 = X.scores(); s2 = X.sortie_refaite(d2)
    essai("ouverture de la sortie refaite cohérente sous la ligne neuve", lambda: X.ouvrir(s2, r[0], go2, r[1])["reprise"]["ligne_de_go"])
# ligne citant le constat d'incohérence
go3 = "GO-2099-05-03-03"
X.lignes.append(f"| {go3} | 2099 | décision | {__import__('controle_ia.organismes_discrets.graines_bras_a_v12', fromlist=['x']).PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE} — cite {A.empreinte(ci[0])} {A.empreinte(Path(an.__file__))} |")
