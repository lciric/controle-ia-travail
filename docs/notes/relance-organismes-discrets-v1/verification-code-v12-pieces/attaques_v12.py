"""Essais d'attaque, vérification des corrections du code v12 (bras A). Données synthétiques, registres fabriqués."""
import contextlib, io, json, shutil, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v12 as A
with contextlib.redirect_stdout(io.StringIO()):
    import test_analyse_bras_a_v12 as TA
from controle_ia.organismes_discrets import analyse_bras_a_v12 as an, arrets_bras_a_v12 as ar, configuration_bras_a_v12 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v12 as v, graines_bras_a_v12 as g
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {r}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:170]}"); return e
    except BaseException as e:
        print(f"PANNE   {nom} -> {type(e).__name__}: {str(e)[:100]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
lire = lambda p, c, go=None, fige=None: an.regle_de_discretion(p, c, go_de_la_reprise=go, registre_fige=fige)
REPERE = lambda note: A.sortie({J: A.cas_a("juge", 1.0, egales=0)}, piece_source=note)
ecrire_m = lambda r, lc: v.ecrire_fichier_de_l_etape_m(journal=[], revision_refusee=False, gardees_lues=False, renvoi_de_la_base=an.RENVOI_DE_LA_BASE_VERIFIE,
                                                      effectifs_de_la_base_conformes=True, resultat_de_discretion=r, lignes_c=lc)

print("=== C-1 de la v11 rejoué : arrêt à l'étape (n), puis livraison refaite qui relit l'étape (m)")
base = TA.en_rangs(TA.lignes_de_scores("juge", "dose-0.50", pas=1, taches=TA.VER[:2]))
L = TA.Livraison(T, [dict(base[0], champ_de_plus=1)] + base[1:])
essai("étape (n) : fichier des rangs fautif", lambda: L.lire())
course = Path(L.configuration).parent.parent
fa = A.fichier_d_arret(L.arrets, L.piece)
fige = A.registre(A.nouveau_dossier(T, "fige"), [A.ligne_de_reprise("GO-2099-01-01-01", fa)])
c2 = A.fichier_de_configuration(T, course=course, rang=2, pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige)})
A.constat(T, c2, fige, ligne_de_go="GO-2099-01-01-01")
essai("livraison refaite B (« repère ») lue à l'étape (m) sous la ligne qui cite l'arrêt de (n)", lambda: etat(lire(A.piece(T, REPERE("B")), c2, "GO-2099-01-01-01", fige)))
essai("la pièce d'origine A redonnée à l'étape (m) sous la même ligne", lambda: etat(lire(L.piece, c2, "GO-2099-01-01-01", fige)))
print("   fichiers (m) dans la course :", sorted(p.parent.name for p in course.glob(f"livraison-*/{an.NOM_DU_FICHIER_DE_L_ETAPE_M}")))

print("=== question 2 : la même configuration copiée dans un autre dossier de course")
course1 = A.nouvelle_course(T); c1 = A.fichier_de_configuration(T, course=course1, rang=1); A.constat(T, c1)
essai("course 1 : pièce A", lambda: etat(r1 := lire(A.piece(T, A.sortie(piece_source="A")), c1)))
course2 = A.nouvelle_course(T); (course2 / "livraison-1").mkdir()
for nom in (cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION, cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION + ".sha256"):
    shutil.copy(Path(c1).parent / nom, course2 / "livraison-1" / nom)
c1b = course2 / "livraison-1" / cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION
print("   même empreinte :", A.empreinte(c1b) == A.empreinte(c1))
essai("constat de la copie (même inscription au registre)", lambda: A.constat(T, c1b)[1] is not None)
essai("course 2 : pièce B (« repère »), sans ligne de GO", lambda: etat(lire(A.piece(T, REPERE("B")), c1b)))
# variante : la copie dans la même course, sous un autre rang
course3 = A.nouvelle_course(T); c31 = A.fichier_de_configuration(T, course=course3, rang=1); A.constat(T, c31)
lire(A.piece(T, A.sortie(piece_source="A3")), c31)
(course3 / "livraison-2").mkdir()
for nom in (cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION, cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION + ".sha256"):
    shutil.copy(Path(c31).parent / nom, course3 / "livraison-2" / nom)
essai("la même configuration copiée en livraison-2 de la même course", lambda: etat(lire(A.piece(T, REPERE("B3")), course3 / "livraison-2" / cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION)))
# variante : le dossier des arrêts de la course 1 vidé dans une copie de la course entière
course4 = T / "course-copie"; shutil.copytree(course1, course4)
for p in (course4 / "arrets").iterdir(): p.unlink()
essai("course 1 copiée, dossier des arrêts vidé, pièce B", lambda: etat(lire(A.piece(T, REPERE("B4")), course4 / "livraison-1" / cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION)))

print("=== M-1 de la v11 : contrôle d'avant le premier départ")
course = A.nouvelle_course(T); c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
A.controle(T, c1)
pA = A.piece(T, A.sortie(piece_source="A"))
vrai = an._regle
an._regle = lambda *a, **k: (_ for _ in ()).throw(KeyboardInterrupt("panne"))
essai("première lecture interrompue", lambda: lire(pA, c1))
an._regle = vrai
essai("rejeu sur le contrôle d'avant le premier départ", lambda: etat(lire(pA, c1)))
essai("contrôle refait, sain", lambda: A.controle(T, c1, date_utc="2099-01-04T00:00:00Z")[1] is not None)
essai("rejeu sous le contrôle refait", lambda: etat(lire(pA, c1)))

print("=== question 3 : reprise de l'étape (n), sortie refaite incohérente")
X = TA.ArretALEtapeN(T)
go = "GO-2099-05-01-01"; c, fg = X.reprise(X.L.piece, go)
f, decl = X.scores()
incoh = X.sortie_refaite(decl, texte=lambda t: t.replace('"aire": 0.52', '"aire": 0.52000000000000000001', 1))
essai("ouverture de la reprise (n), lectures refaites à un écart près", lambda: X.ouvrir(incoh, c, go, fg))
print("   actes de reprise :", len(X.fichiers("reprise-")), "| constats d'incohérence :", len(X.fichiers("livraison-refaite-incoherente")))
f2, decl2 = X.scores()
saine = X.sortie_refaite(decl2)
essai("une sortie refaite cohérente, sous la même ligne", lambda: X.ouvrir(saine, c, go, fg))
essai("issues pour la sortie incohérente", lambda: X.issues(incoh, c)["grandeurs_de_l_etape_n"])
go2 = "GO-2099-05-01-02"
essai("ligne neuve qui cite le constat d'incohérence", lambda: X.reprise(X.fichiers("livraison-refaite-incoherente")[0] if False else X.L.piece, go2))
