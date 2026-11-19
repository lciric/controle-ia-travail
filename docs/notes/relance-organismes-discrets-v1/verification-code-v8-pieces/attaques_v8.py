"""Essais d'attaque, vérification des corrections du code v8 (bras A). Données synthétiques, registres fabriqués."""
import copy, json, os, sys, tempfile
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v8 as A
from controle_ia.organismes_discrets import analyse_bras_a_v8 as an, arrets_bras_a_v8 as ar, configuration_bras_a_v8 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v8 as v, graines_bras_a_v8 as g, depots_bras_a_v8 as dp
from controle_ia.gardes import GardeArret
CL = A.constat_de_lancement
T = Path(tempfile.mkdtemp())

def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {r}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:140]}"); return e
    except BaseException as e:
        print(f"PANNE   {nom} -> {type(e).__name__}: {str(e)[:80]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
REFUSEE = lambda egales=9: A.sortie({J: A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None, egales=egales)})

class Panne:
    """Fait tomber une fois l'un des trois temps de `depots.ecrire_et_sceller`, pour les pièces dont le nom contient `motif`."""
    def __init__(self, temps, motif):
        self.temps, self.motif, self.vrai = temps, motif, getattr(dp, temps)
    def __enter__(self):
        vrai, motif, temps = self.vrai, self.motif, self.temps
        def en_panne(*a, **k):
            if motif in str(a[0]):
                setattr(dp, temps, vrai)
                raise KeyboardInterrupt(f"panne au temps {temps}")
            return vrai(*a, **k)
        setattr(dp, self.temps, en_panne)
    def __exit__(self, *x):
        setattr(dp, self.temps, self.vrai)

TEMPS = ("_ecrire_le_provisoire", "_poser_le_compagnon", "_renommer")

print("=== C-2 : pannes à chaque temps d'écriture")
for temps in TEMPS:
    course = A.nouvelle_course(T)
    c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
    p = A.piece(T, REFUSEE())
    with Panne(temps, "arret-de-la-lecture"):
        essai(f"fichier d'arrêt, panne au temps {temps}", lambda: an.regle_de_discretion(p, c1, go_de_la_reprise=None, registre_fige=None))
    essai("   dossier lisible après la panne (compte)", lambda: {k: x for k, x in an.compte_des_livraisons(c1).items() if k in ("livraisons_refusees", "restes_d_ecritures_interrompues")})
    essai("   la même lecture relancée", lambda: an.regle_de_discretion(p, c1, go_de_la_reprise=None, registre_fige=None))
    essai("   dossier après la relance", lambda: {k: x for k, x in an.compte_des_livraisons(c1).items() if k in ("livraisons_refusees", "restes_d_ecritures_interrompues")})

def course_avec_un_refus():
    course = A.nouvelle_course(T)
    c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
    p = A.piece(T, REFUSEE())
    try: an.regle_de_discretion(p, c1, go_de_la_reprise=None, registre_fige=None)
    except GardeArret: pass
    fa = A.fichier_d_arret(A.dossier_des_arrets(c1), p)
    fige = A.registre(A.nouveau_dossier(T, "fige"), [A.ligne_de_reprise("GO-2099-01-01-01", fa), A.ligne_de_reprise("GO-2099-01-01-02", fa)])
    c2 = A.fichier_de_configuration(T, course=course, rang=2, pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige)})
    return course, c1, c2, fige

for temps in TEMPS:
    course, c1, c2, fige = course_avec_un_refus()
    A.constat(T, c2, fige)
    p2 = A.piece(T, A.sortie())
    with Panne(temps, "reprise-de-la-lecture"):
        essai(f"acte de reprise, panne au temps {temps}", lambda: an.regle_de_discretion(p2, c2, go_de_la_reprise="GO-2099-01-01-01", registre_fige=fige))
    essai("   relance, même ligne", lambda: (etat(r := an.regle_de_discretion(p2, c2, go_de_la_reprise="GO-2099-01-01-01", registre_fige=fige)), r.get("rejeu_sous_le_meme_acte")))

print("=== rejeu après panne pendant la lecture (acte scellé)")
course, c1, c2, fige = course_avec_un_refus(); A.constat(T, c2, fige)
p2 = A.piece(T, A.sortie())
vrai = an._regle
an._regle = lambda *a, **k: (_ for _ in ()).throw(KeyboardInterrupt("panne pendant la lecture"))
essai("lecture interrompue après l'acte", lambda: an.regle_de_discretion(p2, c2, go_de_la_reprise="GO-2099-01-01-01", registre_fige=fige))
an._regle = vrai
essai("rejeu sous une autre ligne", lambda: etat(an.regle_de_discretion(p2, c2, go_de_la_reprise="GO-2099-01-01-02", registre_fige=fige)))
essai("rejeu sans ligne", lambda: etat(an.regle_de_discretion(p2, c2, go_de_la_reprise=None, registre_fige=fige)))
r = essai("rejeu sous la même ligne", lambda: an.regle_de_discretion(p2, c2, go_de_la_reprise="GO-2099-01-01-01", registre_fige=fige))
if isinstance(r, dict): print("   état :", etat(r), "| rejeu_sous_le_meme_acte :", r.get("rejeu_sous_le_meme_acte"))
# configuration voisine aux mêmes empreintes et à d'autres chaînes (limite écrite, relevé A.2)
c3 = A.fichier_de_configuration(A.nouveau_dossier(T, "autre"), pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige)}, statistique_agregateur="autre (essai)")
print("   (la configuration voisine est dans une autre course : non essayée sur le même acte)")

print("=== étape (m) : pannes à l'écriture des deux fichiers")
for temps in TEMPS:
    for motif in ("constats-de-l-etape-m", "etats-des-moniteurs"):
        course = A.nouvelle_course(T)
        c = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c)
        p = A.piece(T, A.sortie())
        res = an.regle_de_discretion(p, c, go_de_la_reprise=None, registre_fige=None)
        ecrire = lambda: v.ecrire_fichier_de_l_etape_m(journal=[], revision_refusee=False, gardees_lues=False,
                                                         renvoi_de_la_base=an.RENVOI_DE_LA_BASE_VERIFIE, effectifs_de_la_base_conformes=True,
                                                         resultat_de_discretion=res, lignes_c={1.0: "C6"})
        with Panne(temps, motif):
            essai(f"étape (m), {motif}, panne au temps {temps}", lambda: ecrire().name)
        essai("   relecture de la règle après la panne", lambda: etat(an.regle_de_discretion(p, c, go_de_la_reprise=None, registre_fige=None)))
        essai("   écriture relancée", lambda: ecrire().name)
        essai("   relecture après le fichier (m)", lambda: etat(an.regle_de_discretion(p, c, go_de_la_reprise=None, registre_fige=None)))

print("=== constat de lancement")
course, c1, c2, fige = course_avec_un_refus()
lfig = A.registre(A.nouveau_dossier(T, "x"), []).read_text().splitlines()  # en-tête seul
essai("sain", lambda: (lambda r: (r[0]["configuration_inscrite"], r[0]["revocation_entree"], r[1] is not None))(A.constat(T, c2, fige)))
course, c1, c2, fige = course_avec_un_refus()
essai("configuration non inscrite", lambda: (lambda r: (r[0]["configuration_inscrite"], r[1]))(A.constat(T, c2, fige, inscrite=False)))
essai("   analyse sans constat", lambda: an.regle_de_discretion(A.piece(T, A.sortie()), c2, go_de_la_reprise="GO-2099-01-01-01", registre_fige=fige))
for nom, rev in (("révocation bien formée", "| GO-2099-02-01-01 | 2099-02-01 | révocation | GO-2099-01-01-01 retiré |"),
                 ("révocation sans accent", "| GO-2099-02-01-01 | 2099-02-01 | revocation | GO-2099-01-01-01 retiré |"),
                 ("retrait écrit comme une décision", "| GO-2099-02-01-01 | 2099-02-01 | décision | GO-2099-01-01-01 est révoqué |"),
                 ("révocation d'une ligne voisine GO-…-011", "| GO-2099-02-01-01 | 2099-02-01 | révocation | GO-2099-01-01-011 retiré |")):
    course, c1, c2, fige = course_avec_un_refus()
    essai(f"constat, {nom}", lambda: (lambda r: (r[0]["revocation_entree"], r[1] is not None))(A.constat(T, c2, fige, lignes_de_plus=[rev])))
# constat sain, puis révocation entrée : le constat ne peut pas être refait, l'ancien reste
course, c1, c2, fige = course_avec_un_refus()
A.constat(T, c2, fige)
p2 = A.piece(T, A.sortie())
an._regle = lambda *a, **k: (_ for _ in ()).throw(KeyboardInterrupt("panne pendant la lecture"))
essai("lecture interrompue (constat sain)", lambda: an.regle_de_discretion(p2, c2, go_de_la_reprise="GO-2099-01-01-01", registre_fige=fige))
an._regle = vrai
rev = "| GO-2099-02-01-01 | 2099-02-01 | révocation | GO-2099-01-01-01 retiré |"
essai("révocation entrée, constat refait", lambda: (lambda r: (r[0]["revocation_entree"], r[1]))(A.constat(T, c2, fige, lignes_de_plus=[rev])))
essai("rejeu de la lecture sous la ligne révoquée, sur l'ancien constat sain", lambda: etat(an.regle_de_discretion(p2, c2, go_de_la_reprise="GO-2099-01-01-01", registre_fige=fige)))
# inscription par une ligne qui retire la configuration
course, c1, c2, fige = course_avec_un_refus()
retrait = f"| GO-2099-12-31-09 | 2099-12-31 | révocation | configuration {A.empreinte(c2)} retirée |"
essai("« inscrite » par une ligne qui la retire", lambda: (lambda r: (r[0]["configuration_inscrite"], r[1] is not None))(A.constat(T, c2, fige, inscrite=False, lignes_de_plus=[retrait])))
# valeurs fictives
course = A.nouvelle_course(T)
cfz = A.fichier_de_configuration(T, course=course, rang=1, pieces={cf.MODULE_DU_COTE_HABILITE: "0" * 64})
essai("module fictif dans la configuration", lambda: A.constat(T, cfz))
course, c1, c2, fige = course_avec_un_refus()
essai("ligne GO-0000-00-00-00 étrangère au constat", lambda: A.constat(T, c2, fige, lignes_de_plus=["| GO-0000-00-00-00 | 2099 | exemple | exemple fictif |"])[1] is not None)
fa = next(A.dossier_des_arrets(c1).glob("arret-*.json"))
fige_z = A.registre(A.nouveau_dossier(T, "figez"), [A.ligne_de_reprise("GO-0000-00-00-00", fa)])
cz = A.fichier_de_configuration(T, course=course, rang=3, pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige_z)})
essai("ligne d'accord GO-0000-00-00-00 dans l'état figé", lambda: A.constat(T, cz, fige_z))
# constat écrit à la main (limite écrite)
course = A.nouvelle_course(T)
cm = A.fichier_de_configuration(T, course=course, rang=1)
A.ecrire_scelle(Path(cm).parent / cf.NOM_DU_CONSTAT_DE_LANCEMENT, {"date_utc": "x", "sha256_de_la_configuration": A.empreinte(cm), "sha256_du_registre_fige": None,
               "commit_du_registre_courant": "y", "configuration_inscrite": True, "revocation_entree": False})
essai("constat écrit à la main (date 'x', commit 'y')", lambda: etat(an.regle_de_discretion(A.piece(T, A.sortie()), cm, go_de_la_reprise=None, registre_fige=None)))

print("=== M-1, M-3, M-5")
course = A.nouvelle_course(T); c = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c)
e = A.cas_a("juge", 0.75, egales=999); s = A.sortie({("juge", 0.75): e})
texte = json.dumps(s).replace(json.dumps(e["valeur_p_bas"]), "0.5", 1)
essai("M-3 : 0,5 contre 1 000/2 001 (écart égal au demi-pas)", lambda: an.regle_de_discretion(A.piece(T, texte), c, go_de_la_reprise=None, registre_fige=None))
texte = json.dumps(A.sortie()).replace('"effectifs": {"honnete": 1280,', '"effectifs": {"honnete": 1280, "honnete": 1280,', 1)
course = A.nouvelle_course(T); c = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c)
essai("M-5 : doublon dans effectifs", lambda: an.regle_de_discretion(A.piece(T, texte), c, go_de_la_reprise=None, registre_fige=None))
