"""Essais d'attaque, vérification des corrections du code v10 (bras A). Données synthétiques, registres fabriqués."""
import json, os, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v10 as A
from controle_ia.organismes_discrets import analyse_bras_a_v10 as an, arrets_bras_a_v10 as ar, configuration_bras_a_v10 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v10 as v, graines_bras_a_v10 as g
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {r}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:150]}"); return e
    except BaseException as e:
        print(f"PANNE   {nom} -> {type(e).__name__}: {str(e)[:100]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
lire = lambda p, c, go=None, fige=None: an.regle_de_discretion(p, c, go_de_la_reprise=go, registre_fige=fige)
GO = "GO-2099-01-01-01"
def ecrire_m(res):
    return v.ecrire_fichier_de_l_etape_m(journal=[], revision_refusee=False, gardees_lues=False, renvoi_de_la_base=an.RENVOI_DE_LA_BASE_VERIFIE,
                                         effectifs_de_la_base_conformes=True, resultat_de_discretion=res, lignes_c={1.0: "C6"})

print("=== question 2 : gabarit et rédactions")
print("   gabarit :", cf.CHOIX_DU_MOT_DE_LAZAR_DU_19_NOVEMBRE_2026)
for nom, val in ((cf.CHOIX_SCHEMA, cf.SCHEMA_LIBRE), (cf.CHOIX_SEUIL, cf.SEUIL_SUR_LES_CALCULES), (cf.CHOIX_INTERVALLE_IMPOSSIBLE, cf.INTERVALLE_INDECIS_D_OFFICE),
                 (cf.CHOIX_NON_AJUSTABLE, cf.NON_AJUSTABLE_ANOMALIE), (cf.CHOIX_ISSUE, cf.ISSUE_LIGNE_D_ARRET_DE_LA_COURSE), (cf.CHOIX_ISSUE, cf.ISSUE_DISCRETION_NON_LUE)):
    essai(f"configuration avec la rédaction retirée « {val} »", lambda: A.fichier_de_configuration(T, choix={nom: val}).name)
for val in (cf.INTERVALLE_COMME_DEGENERE, cf.INTERVALLE_ANOMALIE):
    essai(f"intervalle impossible « {val} » (point 19 ouvert)", lambda: A.fichier_de_configuration(T, choix={cf.CHOIX_INTERVALLE_IMPOSSIBLE: val}).name)
for val in (cf.NON_AJUSTABLE_AIRE_NON_CALCULABLE, cf.NON_AJUSTABLE_MODULE_CORRIGE, cf.NON_AJUSTABLE_EN_ATTENTE):
    essai(f"non ajustable « {val} » (point 20 ouvert)", lambda: A.fichier_de_configuration(T, choix={cf.CHOIX_NON_AJUSTABLE: val}).name)
c = A.fichier_de_configuration(T, choix={cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_EN_ATTENTE}); A.constat(T, c)
essai("« en attente », motif non ajustable rencontré", lambda: lire(A.piece(T, A.sortie({J: A.cas_b("juge", 1.0, motif=A.M_NON_AJUSTABLE)})), c))
print("   fichiers d'arrêt après :", len(list(A.dossier_des_arrets(c).glob("arret-*.json"))))
c = A.fichier_de_configuration(T, choix={cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_EN_ATTENTE}); A.constat(T, c)
essai("« en attente », motif non ajustable à la dose 1/4 seulement", lambda: lire(A.piece(T, A.sortie({("juge", 0.25): A.cas_b("juge", 0.25, motif=A.M_NON_AJUSTABLE)})), c))
c = A.fichier_de_configuration(T, choix={cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_EN_ATTENTE}); A.constat(T, c)
essai("« en attente », livraison sans ce motif", lambda: etat(lire(A.piece(T, A.sortie()), c)))

print("=== question 3 : seconde « première livraison »")
course = A.nouvelle_course(T)
c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
p1 = A.piece(T, A.sortie(piece_source="premiere"))
r1 = lire(p1, c1); ecrire_m(r1)
c2 = A.fichier_de_configuration(T, course=course, rang=2); A.constat(T, c2)
essai("rang 2 sans registre, après le rang 1 lu et son fichier (m) scellé", lambda: etat(lire(A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, egales=0)}, piece_source="seconde")), c2)))
course = A.nouvelle_course(T)
c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
pa = A.piece(T, A.sortie(piece_source="pa"))
pb = A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, egales=0)}, piece_source="pb"))
essai("rang 1 : première pièce lue (résultat rendu, fichier (m) pas encore écrit)", lambda: etat(lire(pa, c1)))
rb = essai("rang 1 : une AUTRE pièce lue sous la même configuration", lambda: lire(pb, c1))
if isinstance(rb, dict):
    print("   état de la seconde :", etat(rb))
    essai("   fichier (m) écrit avec la seconde", lambda: ecrire_m(rb).name)

print("=== question 3 : provenance")
course = A.nouvelle_course(T)
c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
mauvaise = A.piece(T, A.sortie(piece_source=A.provenance("autre", module="d" * 64)))
essai("pièce d'un autre module", lambda: lire(mauvaise, c1))
print("   constats de provenance :", [x.name[:40] for x in A.dossier_des_arrets(c1).glob("provenance-*.json")])
essai("la bonne pièce ensuite, même configuration, sans GO", lambda: etat(lire(A.piece(T, A.sortie()), c1)))
c2 = A.fichier_de_configuration(T, course=course, rang=2); A.constat(T, c2)
essai("la bonne pièce sous une configuration neuve sans GO", lambda: etat(lire(A.piece(T, A.sortie()), c2)))
c3 = A.fichier_de_configuration(A.nouveau_dossier(T, "autre-course"), rang=1); A.constat(T, c3)
essai("la bonne pièce dans une AUTRE course (autre dossier des arrêts)", lambda: etat(lire(A.piece(T, A.sortie()), c3)))
# erreur de rangement
course = A.nouvelle_course(T)
c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
d = A.nouveau_dossier(T, "sans-compagnon"); f = d / "sortie.json"; f.write_text(json.dumps(A.sortie()), encoding="utf-8")
essai("pièce sans compagnon", lambda: lire(f, c1))
print("   constats de rangement :", [x.name[:36] for x in A.dossier_des_arrets(c1).glob("erreur-de-rangement-*.json")])
from controle_ia.scellement import sceller; sceller(f)
essai("la même pièce, scellée ensuite", lambda: etat(lire(f, c1)))
course = A.nouvelle_course(T)
c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
essai("chemin vers un dossier (rien n'est consigné)", lambda: lire(A.nouveau_dossier(T, "un-dossier"), c1))
essai("puis une pièce quelconque, sans GO", lambda: etat(lire(A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, egales=0)})), c1)))

print("=== question 1 : M-1 et M-2 de la v9")
def course_avec_un_refus():
    course = A.nouvelle_course(T)
    c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
    p = A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None, egales=9)}))
    try: lire(p, c1)
    except GardeArret: pass
    fa = A.fichier_d_arret(A.dossier_des_arrets(c1), p)
    fige = A.registre(A.nouveau_dossier(T, "fige"), [A.ligne_de_reprise(GO, fa)])
    c2 = A.fichier_de_configuration(T, course=course, rang=2, pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige)})
    return course, c1, c2, fige
for nom, f_ligne in (("retrait, empreinte abrégée 16 signes", lambda cs: f"| GO-2099-12-31-09 | 2099 | révocation | configuration {cs[:16]} retirée |"),
                     ("retrait, empreinte abrégée 12 signes", lambda cs: f"| GO-2099-12-31-09 | 2099 | révocation | configuration {cs[:12]} retirée |"),
                     ("révocation « GO 2099-01-01-01 »", lambda cs: f"| GO-2099-12-31-09 | 2099 | révocation | GO 2099-01-01-01 retiré |"),
                     ("révocation « go_2099_01_01_01 »", lambda cs: f"| GO-2099-12-31-09 | 2099 | révocation | go_2099_01_01_01 retiré |"),
                     ("identifiant voisin « GO-2099-01-01-011 »", lambda cs: f"| GO-2099-12-31-09 | 2099 | révocation | GO-2099-01-01-011 retiré |")):
    course, c1, c2, fige = course_avec_un_refus(); cs = A.empreinte(c2)
    essai(f"constat, {nom}", lambda: (lambda r: (r[0]["configuration_inscrite"], r[0]["revocation_entree"], r[1] is not None))(A.constat_et_causes(T, c2, fige, lignes_de_plus=[f_ligne(cs)], ligne_de_go=GO)))
# rejeu : contrôle exigé ; contrôle sain ancien et révocation entrée sans contrôle refait
course, c1, c2, fige = course_avec_un_refus()
A.constat(T, c2, fige, ligne_de_go=GO)
p2 = A.piece(T, A.sortie())
vrai = an._regle
an._regle = lambda *a, **k: (_ for _ in ()).throw(KeyboardInterrupt("panne"))
essai("lecture interrompue après l'acte", lambda: lire(p2, c2, GO, fige))
an._regle = vrai
essai("rejeu sans contrôle", lambda: etat(lire(p2, c2, GO, fige)))
essai("contrôle sain", lambda: A.controle(T, c2, fige, ligne_de_go=GO)[1] is not None)
rev = f"| GO-2099-02-01-01 | 2099 | révocation | {GO} retiré |"
print("   (une révocation entre ensuite au registre, sans contrôle refait)")
essai("rejeu sur le contrôle sain, plus ancien que la révocation", lambda: etat(lire(p2, c2, GO, fige)))
course, c1, c2, fige = course_avec_un_refus()
A.constat(T, c2, fige, ligne_de_go=GO)
p2 = A.piece(T, A.sortie())
an._regle = lambda *a, **k: (_ for _ in ()).throw(KeyboardInterrupt("panne"))
essai("lecture interrompue après l'acte (2)", lambda: lire(p2, c2, GO, fige))
an._regle = vrai
essai("contrôle malsain (révocation)", lambda: A.controle(T, c2, fige, ligne_de_go=GO, lignes_de_plus=[rev])[2])
essai("rejeu après le contrôle malsain", lambda: etat(lire(p2, c2, GO, fige)))
essai("contrôle sain plus tardif (révocation absente du registre donné)", lambda: A.controle(T, c2, fige, ligne_de_go=GO, date_utc="2099-01-04T00:00:00Z")[1] is not None)
essai("rejeu après ce contrôle sain", lambda: etat(lire(p2, c2, GO, fige)))
# première livraison : contrôle facultatif
course = A.nouvelle_course(T); c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
essai("première livraison sans contrôle", lambda: etat(lire(A.piece(T, A.sortie()), c1)))

print("=== question 4 : la phrase de l'écart à R9")
fige = A.registre(A.nouveau_dossier(T, "r9"), [
    "| GO-2099-03-01-01 | 2099 | décision | écart à R9 accordé pour la table des identifiants opaques |",
    "| GO-2099-03-01-02 | 2099 | décision | aucun écart à R9 accordé pour la table des identifiants opaques |",
    "| GO-2099-03-01-03 | 2099 | décision | pas d'écart à R9 accordé pour la table des identifiants opaques avant le devis |",
    "| GO-2099-03-01-04 | 2099 | décision | écart à R9 : entropie propre de la table des identifiants opaques — accepter |",
    "| GO-2099-03-01-05 | 2099 | décision | ecart a R9 accorde pour la table des identifiants opaques |",
    "| GO-2099-03-01-06 | 2099 | décision | écart à R9 accordé pour la table des identifiants opaques ? à trancher |",
    "| GO-2099-03-01-07 | 2099 | décision | écart à R9 accordé pour la table des identifiants opaques, refusé : pas de devis |",
])
emp = A.empreinte(fige)
for k in range(1, 8):
    go = f"GO-2099-03-01-0{k}"
    essai(f"porte R9, {go}", lambda: g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=go, registre_fige=fige, sha256_au_scellement=emp)["go"])
