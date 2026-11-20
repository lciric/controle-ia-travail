"""Essais d'attaque, partie 2 : autres voies vers deux résultats ; M-2/M-3 ; reprise (n)."""
import contextlib, io, json, shutil, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v12 as A
with contextlib.redirect_stdout(io.StringIO()):
    import test_analyse_bras_a_v12 as TA
from controle_ia.organismes_discrets import analyse_bras_a_v12 as an, arrets_bras_a_v12 as ar, configuration_bras_a_v12 as cf
from controle_ia.organismes_discrets import graines_bras_a_v12 as g
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {str(r)[:200]}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:200]}"); return e
    except BaseException as e:
        print(f"PANNE   {nom} -> {type(e).__name__}: {str(e)[:120]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
lire = lambda p, c, go=None, fige=None: an.regle_de_discretion(p, c, go_de_la_reprise=go, registre_fige=fige)
REPERE = lambda note: A.sortie({J: A.cas_a("juge", 1.0, egales=0)}, piece_source=note)

print("=== voies vers deux résultats dans une même course (falsifications du dossier)")
course = A.nouvelle_course(T); c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
essai("pièce A", lambda: etat(lire(A.piece(T, A.sortie(piece_source="A")), c1)))
d = Path(c1).parent
print("   contenu de livraison-1 :", sorted(p.name for p in d.iterdir()))
print("   contenu des arrêts :", sorted(p.name for p in (course / "arrets").iterdir()))
m = d / an.NOM_DU_FICHIER_DE_L_ETAPE_M
sauve = {p.name: p.read_bytes() for p in d.iterdir()}
for p in list(d.glob(an.NOM_DU_FICHIER_DE_L_ETAPE_M + "*")): p.unlink()
essai("fichier (m) et compagnon effacés, pièce B", lambda: etat(lire(A.piece(T, REPERE("B")), c1)))
for p in list((course / "arrets").iterdir()): p.unlink()
essai("+ dossier des arrêts vidé, pièce B", lambda: etat(lire(A.piece(T, REPERE("B")), c1)))
for p in list(d.iterdir()):
    if p.name not in (cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION, cf.NOM_DU_FICHIER_DE_LA_CONFIGURATION + ".sha256", cf.NOM_DU_CONSTAT_DE_LANCEMENT, cf.NOM_DU_CONSTAT_DE_LANCEMENT + ".sha256"):
        print("     reste :", p.name)

print("=== M-2/M-3 : configuration abandonnée, retrait, et retrait d'une configuration lue")
c_ab = A.fichier_de_configuration(T, course=A.nouvelle_course(T), rang=1)
c_ok = A.fichier_de_configuration(T, course=A.nouvelle_course(T), rang=1, statistique_agregateur="autre (essai)")
assert A.empreinte(c_ab) != A.empreinte(c_ok)
ins_ab = A.ligne_d_inscription(c_ab, go="GO-2099-12-30-01")
P = g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE
sha = A.empreinte(c_ab)
for nom, plus in (("inscription abandonnée seule", [ins_ab]),
                  ("+ ligne de reprise quelconque après", [ins_ab, f"| GO-2099-12-30-02 | 2099 | décision | {P} |"]),
                  ("+ révocation, abrégé 16", [ins_ab, f"| GO-2099-12-30-03 | 2099 | révocation | {sha[:16]} retirée |"]),
                  ("+ décision (pas révocation) citant l'empreinte entière", [ins_ab, f"| GO-2099-12-30-03 | 2099 | décision | {sha} retirée |"]),
                  ("+ **Révocation** en gras, empreinte entière", [ins_ab, f"| GO-2099-12-30-03 | 2099 | **Révocation** | {sha} |"]),
                  ("+ révocation AVANT l'inscription", [f"| GO-2099-12-30-03 | 2099 | révocation | {sha} |", ins_ab]),
                  ("+ révocation qui cite l'empreinte en majuscules", [ins_ab, f"| GO-2099-12-30-03 | 2099 | révocation | {sha.upper()} |"]),
                  ("+ révocation hors table (sans barres)", [ins_ab, f"GO-2099-12-30-03 révocation {sha}"]),
                  ("+ révocation, empreinte entière", [ins_ab, f"| GO-2099-12-30-03 | 2099 | révocation | {sha} |"])):
    essai(nom, lambda: (lambda r: f"sain={r[1] is not None} causes={r[2]}")(A.constat_et_causes(T, c_ok, lignes_de_plus=plus)))

# la configuration c1 de la course plus haut a été LUE ; une révocation la retire ; une autre configuration part
c_lue = A.fichier_de_configuration(T, course=(cr := A.nouvelle_course(T)), rang=1, statistique_agregateur="lue (essai)")
A.constat(T, c_lue); essai("configuration lue : pièce A", lambda: etat(lire(A.piece(T, A.sortie(piece_source="A")), c_lue)))
c_neuve = A.fichier_de_configuration(T, course=A.nouvelle_course(T), rang=1, statistique_agregateur="neuve (essai)")
ins_lue = A.ligne_d_inscription(c_lue, go="GO-2099-12-29-01")
essai("constat d'une autre configuration, la lue encore inscrite", lambda: A.constat_et_causes(T, c_neuve, lignes_de_plus=[ins_lue])[2])
r = essai("constat, la lue « révoquée » après sa lecture", lambda: A.constat_et_causes(T, c_neuve, lignes_de_plus=[ins_lue, f"| GO-2099-12-29-02 | 2099 | révocation | {A.empreinte(c_lue)} |"])[1])
if not isinstance(r, BaseException) and r is not None:
    essai("seconde course : pièce B (« repère »)", lambda: etat(lire(A.piece(T, REPERE("B")), c_neuve)))

print("=== reprise de l'étape (n) : deux résultats de l'étape (n) ?")
X = TA.ArretALEtapeN(T)
go1 = "GO-2099-05-02-01"; c, fg = X.reprise(X.L.piece, go1)
f, decl = X.scores(); s1 = X.sortie_refaite(decl)
essai("reprise (n) 1, cohérente", lambda: X.ouvrir(s1, c, go1, fg)["reprise"]["ligne_de_go"])
essai("lecture du fichier refait 1", lambda: type(X.lire(f, s1, c)).__name__)
essai("issues 1", lambda: X.issues(s1, c)["grandeurs_de_l_etape_n"])
go2 = "GO-2099-05-02-02"
r2 = essai("seconde ligne qui cite le même fichier d'arrêt d'origine", lambda: X.reprise(X.L.piece, go2))
if isinstance(r2, tuple):
    c2, fg2 = r2
    f2, decl2 = X.scores(); s2 = X.sortie_refaite(decl2)
    essai("reprise (n) 2", lambda: X.ouvrir(s2, c2, go2, fg2)["reprise"]["ligne_de_go"])
    essai("issues 2", lambda: X.issues(s2, c2)["grandeurs_de_l_etape_n"])
print("   fichiers des grandeurs (n) :", sorted(p.parent.name for p in X.course.glob("livraison-*/" + "grandeurs-de-l-etape-n-bras-a.json")))
print("   (m) intacte :", X.etape_m_intacte())
