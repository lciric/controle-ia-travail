"""Essais d'attaque, vérification des corrections du code v9 (bras A). Données synthétiques, registres fabriqués."""
import contextlib, io, json, os, subprocess, sys, tempfile
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v9 as A
from controle_ia.organismes_discrets import analyse_bras_a_v9 as an, arrets_bras_a_v9 as ar, configuration_bras_a_v9 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v9 as v, graines_bras_a_v9 as g, depots_bras_a_v9 as dp
from controle_ia.gardes import GardeArret
CL = A.constat_de_lancement
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {r}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:150]}"); return e
    except BaseException as e:
        print(f"PANNE   {nom} -> {type(e).__name__}: {str(e)[:80]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
REFUSEE = lambda egales=9: A.sortie({J: A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None, egales=egales)})
GO = "GO-2099-01-01-01"

def course_avec_un_refus():
    course = A.nouvelle_course(T)
    c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
    p = A.piece(T, REFUSEE())
    try: an.regle_de_discretion(p, c1, go_de_la_reprise=None, registre_fige=None)
    except GardeArret: pass
    fa = A.fichier_d_arret(A.dossier_des_arrets(c1), p)
    fige = A.registre(A.nouveau_dossier(T, "fige"), [A.ligne_de_reprise(GO, fa), A.ligne_de_reprise("GO-2099-01-01-02", fa)])
    c2 = A.fichier_de_configuration(T, course=course, rang=2, pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige)})
    return course, c1, c2, fige

print("=== C-1 et M-2 : lignes neuves reconnues par le sens")
for nom, ligne in (("révocation bien formée", f"| GO-2099-02-01-01 | 2099-02-01 | révocation | {GO} retiré |"),
                   ("révocation sans accent", f"| GO-2099-02-01-01 | 2099-02-01 | revocation | {GO} retiré |"),
                   ("décision qui dit l'accord révoqué", f"| GO-2099-02-01-01 | 2099-02-01 | décision | {GO} est révoqué |"),
                   ("identifiant écrit en minuscules", f"| GO-2099-02-01-01 | 2099-02-01 | décision | {GO.lower()} retiré |"),
                   ("identifiant voisin GO-…-011", f"| GO-2099-02-01-01 | 2099-02-01 | révocation | {GO}1 retiré |"),
                   ("identifiant écrit sans tiret après GO", f"| GO-2099-02-01-01 | 2099-02-01 | révocation | GO 2099-01-01-01 retiré |"),
                   ("hors de la table", f"Révocation : {GO} retiré")):
    course, c1, c2, fige = course_avec_un_refus()
    essai(f"constat, {nom}", lambda: (lambda r: (r[0]["revocation_entree"], r[1] is not None, r[2]))(A.constat_et_causes(T, c2, fige, lignes_de_plus=[ligne], ligne_de_go=GO)))
course, c1, c2, fige = course_avec_un_refus()
cs = A.empreinte(c2)
for nom, ligne in (("retrait de la configuration, empreinte entière", f"| GO-2099-12-31-09 | 2099-12-31 | révocation | configuration {cs} retirée |"),
                   ("retrait de la configuration, empreinte abrégée (16 signes)", f"| GO-2099-12-31-09 | 2099-12-31 | révocation | configuration {cs[:16]}… retirée |")):
    course, c1, c2, fige = course_avec_un_refus(); cs = A.empreinte(c2)
    ligne = ligne.replace("{cs}", cs)
    l2 = f"| GO-2099-12-31-09 | 2099-12-31 | révocation | configuration {cs if 'entière' in nom else cs[:16] + '…'} retirée |"
    essai(f"constat, {nom}", lambda: (lambda r: (r[0]["configuration_inscrite"], r[0]["revocation_entree"], r[1] is not None, r[2]))(A.constat_et_causes(T, c2, fige, lignes_de_plus=[l2], ligne_de_go=GO)))

print("=== M-4 / brouillon 31 : révocation entrée entre une panne et le rejeu, mode de contrôle")
course, c1, c2, fige = course_avec_un_refus()
A.constat(T, c2, fige, ligne_de_go=GO)
cons = Path(c2).parent / cf.NOM_DU_CONSTAT_DE_LANCEMENT
avant = A.empreinte(cons)
p2 = A.piece(T, A.sortie())
vrai = an._regle
an._regle = lambda *a, **k: (_ for _ in ()).throw(KeyboardInterrupt("panne pendant la lecture"))
essai("lecture interrompue après l'acte", lambda: an.regle_de_discretion(p2, c2, go_de_la_reprise=GO, registre_fige=fige))
an._regle = vrai
rev = f"| GO-2099-02-01-01 | 2099-02-01 | revocation | {GO} retiré |"
r = essai("contrôle, révocation mal orthographiée entrée", lambda: (lambda r: (r[0]["revocation_entree"], r[1], r[2]))(A.constat_et_causes(T, c2, fige, lignes_de_plus=[rev], ligne_de_go=GO, mode=CL.MODE_CONTROLE)))
print("   constat d'origine intact :", A.empreinte(cons) == avant)
essai("rejeu lancé quand même (sans tenir compte du contrôle)", lambda: etat(an.regle_de_discretion(p2, c2, go_de_la_reprise=GO, registre_fige=fige)))
# en ligne de commande : code de sortie, une ligne JSON, la ligne nommée par son identifiant
reg = A.registre(A.nouveau_dossier(T, "courant"), A.lignes_figees(fige) + [A.ligne_d_inscription(c2), rev])
env = dict(os.environ, PYTHONPATH="/home/user/controle-ia-travail/src")
x = subprocess.run([sys.executable, str(A._SCRIPT), str(c2), str(reg), "--commit", "0123abc", "--date-utc", "2099-02-02T00:00:00Z",
                    "--registre-fige", str(fige), "--ligne-de-go", GO, "--controle"], capture_output=True, text=True, env=env)
print("   ligne de commande --controle : code", x.returncode, "| sortie :", x.stdout.strip()[:120], "| erreur :", x.stderr.strip()[:200])
print("   le texte de la ligne fautive (« retiré ») paraît-il sur la sortie ?", "retiré" in x.stdout + x.stderr)
print("   constat d'origine intact :", A.empreinte(cons) == avant)

print("=== constat : autres")
course = A.nouvelle_course(T); cm = A.fichier_de_configuration(T, course=course, rang=1)
A.constat_a_la_main(cm, date_utc="x", commit_du_registre_courant="y")
essai("constat écrit à la main (date 'x', commit 'y')", lambda: etat(an.regle_de_discretion(A.piece(T, A.sortie()), cm, go_de_la_reprise=None, registre_fige=None)))
course, c1, c2, fige = course_avec_un_refus()
A.constat(T, c2, fige, ligne_de_go=GO)
essai("analyse sous une autre ligne que celle du constat", lambda: etat(an.regle_de_discretion(A.piece(T, A.sortie()), c2, go_de_la_reprise="GO-2099-01-01-02", registre_fige=fige)))
course, c1, c2, fige = course_avec_un_refus()
essai("ligne de GO fictive donnée au programme", lambda: A.constat(T, c2, fige, ligne_de_go="GO-0000-00-00-00"))
essai("ligne fictive étrangère au constat", lambda: A.constat(T, c2, fige, ligne_de_go=GO, lignes_de_plus=["| GO-0000-00-00-00 | 2099 | exemple | rien |"])[1] is not None)
course, c1, c2, fige = course_avec_un_refus()
essai("révocation fictive de la ligne employée", lambda: A.constat(T, c2, fige, ligne_de_go=GO, lignes_de_plus=[f"| GO-0000-00-00-00 | 2099 | révocation | {GO} |"]))

print("=== écarts du complément 1")
course, c1, c2, fige = course_avec_un_refus(); A.constat(T, c2, fige, ligne_de_go=GO)
r = an.regle_de_discretion(A.piece(T, A.sortie()), c2, go_de_la_reprise=GO, registre_fige=fige)
acte = next(A.dossier_des_arrets(c2).glob("reprise-*.json"))
print("   acte de reprise, champs :", sorted(json.loads(acte.read_text())))
s = A.sortie(); s["piece_source"] = {"module": "d" * 64}
course, c1, c2, fige = course_avec_un_refus(); A.constat(T, c2, fige, ligne_de_go=GO)
c2b = A.fichier_de_configuration(T, course=course, rang=3, pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige)}, cle_du_module_dans_piece_source="module")
A.constat(T, c2b, fige, ligne_de_go=GO)
essai("piece_source d'un autre module (livraison refaite)", lambda: an.regle_de_discretion(A.piece(T, s), c2b, go_de_la_reprise=GO, registre_fige=fige))
print("   actes de reprise dans le dossier après ce refus :", len(list(A.dossier_des_arrets(c2b).glob("reprise-*.json"))), "| fichiers d'arrêt :", len(list(A.dossier_des_arrets(c2b).glob("arret-*.json"))))
s3 = A.sortie(); s3["piece_source"] = "texte"
essai("piece_source qui n'est pas un objet (clé inscrite)", lambda: an.regle_de_discretion(A.piece(T, s3), c2b, go_de_la_reprise=GO, registre_fige=fige))

print("=== agrégateur : un seul nombre par dose")
s = A.sortie(); s["agregateur_somme_sans_etat"] = {A.forme(d): {"a": 0.111, "b": 0.222, "c": 0.333} for d in an.QUATRE_DOSES}
s["agregateur_maximum_sans_etat"] = {A.forme(d): [0.444] for d in an.QUATRE_DOSES}
course = A.nouvelle_course(T); c = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c)
r = an.regle_de_discretion(A.piece(T, s), c, go_de_la_reprise=None, registre_fige=None)
txt = repr(r)
print("   somme :", r["agregateur"]["somme"], "| maximum :", r["agregateur"]["maximum"], "| un nombre du contenu dans le résultat ?", any(n in txt for n in ("0.111", "0.222", "0.333", "0.444")))
s = A.sortie(); s["agregateur_somme_sans_etat"] = {A.forme(d): 0.5 for d in an.QUATRE_DOSES[1:]}
course = A.nouvelle_course(T); c = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c)
essai("agrégateur à trois doses", lambda: an.regle_de_discretion(A.piece(T, s), c, go_de_la_reprise=None, registre_fige=None)["agregateur"]["somme"])

print("=== M-1 : valeur ajustée exacte")
ECRIT = "0.0033333333333333333343"
e = A.cas_a("juge", 1.0, egales=6); s = A.sortie({J: e}); t = json.dumps(s)
for champ in ("valeur_p_haut", "valeur_p_pour_la_famille"):
    t = t.replace(f'"{champ}": {json.dumps(e[champ])}', f'"{champ}": {ECRIT}', 1)
course = A.nouvelle_course(T); c = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c)
j = an.regle_de_discretion(A.piece(T, t), c, go_de_la_reprise=None, registre_fige=None)["lectures"]["dose-1.00"]["juge"]
print("   état :", j["etat"], "| ajustée :", j["valeur_p_haut_holm"], "| arrondie :", j.get("valeur_p_haut_holm_arrondie"), "| > 0,05 ?", Fraction(j["valeur_p_haut_holm"]) > Fraction(1, 20))
