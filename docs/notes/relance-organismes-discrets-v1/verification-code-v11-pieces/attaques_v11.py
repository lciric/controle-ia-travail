"""Essais d'attaque, vérification des corrections du code v11 (bras A). Données synthétiques, registres fabriqués."""
import contextlib, io, json, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v11 as A
with contextlib.redirect_stdout(io.StringIO()):
    import test_analyse_bras_a_v11 as TA
from controle_ia.organismes_discrets import analyse_bras_a_v11 as an, arrets_bras_a_v11 as ar, configuration_bras_a_v11 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v11 as v, graines_bras_a_v11 as g
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {r}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:160]}"); return e
    except BaseException as e:
        print(f"PANNE   {nom} -> {type(e).__name__}: {str(e)[:100]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
lire = lambda p, c, go=None, fige=None: an.regle_de_discretion(p, c, go_de_la_reprise=go, registre_fige=fige)
REPERE = lambda note: A.sortie({J: A.cas_a("juge", 1.0, egales=0)}, piece_source=note)

print("=== C-1 rejoué : « ne repère pas » puis « repère »")
course = A.nouvelle_course(T); c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
essai("rang 1, pièce A", lambda: etat(lire(A.piece(T, A.sortie(piece_source="A")), c1)))
essai("rang 1, pièce B d'une autre empreinte", lambda: etat(lire(A.piece(T, REPERE("B")), c1)))
essai("rang 2 sans registre figé (lecture de la configuration)", lambda: cf.lire_la_configuration_scellee(A.fichier_de_configuration(T, course=course, rang=2)))

print("=== autre voie : un arrêt à l'étape (n), puis une livraison refaite qui relit l'étape (m)")
base = TA.en_rangs(TA.lignes_de_scores("juge", "dose-0.50", pas=1, taches=TA.VER[:2]))
L = TA.Livraison(T, [dict(base[0], champ_de_plus=1)] + base[1:])
print("   rang 1 lu, fichier (m) scellé ; états du juge à la dose 1 :", L.resultat["etats"][1.0]["juge"])
essai("étape (n) : fichier des rangs fautif", lambda: L.lire())
course = Path(L.configuration).parent.parent
fa = A.fichier_d_arret(L.arrets, L.piece)
print("   fichier d'arrêt de l'étape (n) :", fa.exists())
fige = A.registre(A.nouveau_dossier(T, "fige"), [A.ligne_de_reprise("GO-2099-01-01-01", fa)])
c2 = A.fichier_de_configuration(T, course=course, rang=2, pieces={cf.REGISTRE_ATTENDU: A.empreinte(fige)})
A.constat(T, c2, fige, ligne_de_go="GO-2099-01-01-01")
r2 = essai("livraison refaite (pièce B, « repère ») sur la ligne qui cite l'arrêt de l'étape (n)", lambda: lire(A.piece(T, REPERE("B")), c2, "GO-2099-01-01-01", fige))
if isinstance(r2, dict):
    print("   état du juge dans la seconde lecture :", etat(r2), "| le fichier (m) du rang 1 existe toujours :", (Path(L.configuration).parent / an.NOM_DU_FICHIER_DE_L_ETAPE_M).exists())
    essai("   fichier (m) du rang 2 écrit (seconde table C dans la course)", lambda: v.ecrire_fichier_de_l_etape_m(journal=[], revision_refusee=False, gardees_lues=False,
          renvoi_de_la_base=an.RENVOI_DE_LA_BASE_VERIFIE, effectifs_de_la_base_conformes=True, resultat_de_discretion=r2, lignes_c={1.0: "C4"}).parent.name)

print("=== question 4 : un contrôle fait avant le premier départ sert au rejeu")
course = A.nouvelle_course(T); c1 = A.fichier_de_configuration(T, course=course, rang=1); A.constat(T, c1)
essai("contrôle sain avant le premier départ", lambda: A.controle(T, c1)[1] is not None)
pA = A.piece(T, A.sortie(piece_source="A"))
vrai = an._regle
an._regle = lambda *a, **k: (_ for _ in ()).throw(KeyboardInterrupt("panne"))
essai("première lecture interrompue (après son ouverture)", lambda: lire(pA, c1))
an._regle = vrai
rev = "| GO-2099-02-01-01 | 2099 | révocation | configuration " + A.empreinte(c1) + " retirée |"
print("   (une ligne qui retire la configuration entre au registre ; aucun contrôle refait)")
essai("rejeu sur le contrôle d'avant le premier départ", lambda: etat(lire(pA, c1)))

print("=== question 3 / A.1 : configuration inscrite puis abandonnée")
course = A.nouvelle_course(T); c_ab = A.fichier_de_configuration(T, course=course, rang=1)
c_ok = A.fichier_de_configuration(A.nouvelle_course(T), rang=1, statistique_agregateur="moyenne (essai)")
ins_ab = A.ligne_d_inscription(c_ab, go="GO-2099-12-30-01")
essai("constat de la configuration suivante, rang 1, registre portant l'inscription abandonnée", lambda: A.constat(T, c_ok, lignes_de_plus=[ins_ab])[1] is not None)
reprise_quelconque = "| GO-2099-12-30-02 | 2099 | décision | " + g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE + " |"
essai("… avec une ligne de reprise quelconque, sans empreinte, placée après", lambda: A.constat(T, c_ok, lignes_de_plus=[ins_ab, reprise_quelconque])[1] is not None)

print("=== question 2 : phrases d'accord, révocation, porte de l'écart à R9")
P9 = g.PHRASE_DE_L_ACCORD_DE_L_ECART_A_R9
lignes = [f"| GO-2099-03-01-01 | 2099 | décision | {P9} |", f"| GO-2099-03-01-02 | 2099 | décision | **{P9}** |",
          f"| GO-2099-03-01-03 | 2099 | décision | {P9}. |", f"| GO-2099-03-01-04 | 2099 | décision | {P9} ? |",
          f"| GO-2099-03-01-05 | 2099 | décision | aucun {P9} |", f"| GO-2099-03-01-06 | 2099 | révocation | {P9} |",
          f"| GO-2099-03-01-07 | 2099 | décision | `{P9}` |", f"| GO-2099-03-01-08 | 2099 | décision | {P9.upper()} |",
          f"| GO-2099-03-01-09 | 2099 | décision | {P9} | note |", f"| GO-2099-03-01-10 | 2099 | décision | « {P9} » |",
          f"| GO-2099-03-01-11 | 2099 | décision | {P9} ! |", f"| GO-2099-03-01-12 | décision | {P9} |"]
fige = A.registre(A.nouveau_dossier(T, "r9"), lignes); emp = A.empreinte(fige)
for k in range(1, 13):
    go = f"GO-2099-03-01-{k:02d}"
    essai(f"porte R9, {lignes[k-1][:90]}", lambda: g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, reglage=g.ECART_A_R9_ACCORDE, go_de_lazar=go,
          registre_fige=fige, sha256_au_scellement=emp, registre_courant=fige)["go"])
courant = A.registre(A.nouveau_dossier(T, "r9c"), A.lignes_figees(fige) + ["| GO-2099-04-01-01 | 2099 | décision | GO-2099-03-01-01 suspendu |"])
essai("porte R9 : ligne entrée depuis l'état figé qui la nomme", lambda: g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, reglage=g.ECART_A_R9_ACCORDE,
      go_de_lazar="GO-2099-03-01-01", registre_fige=fige, sha256_au_scellement=emp, registre_courant=courant)["go"])
courant2 = A.registre(A.nouveau_dossier(T, "r9d"), A.lignes_figees(fige)[1:])
essai("porte R9 : registre courant qui a perdu une ligne de l'état figé", lambda: g.admettre_l_entropie_propre_de_la_table_des_identifiants(1, 2, reglage=g.ECART_A_R9_ACCORDE,
      go_de_lazar="GO-2099-03-01-01", registre_fige=fige, sha256_au_scellement=emp, registre_courant=courant2)["go"])

print("=== M-5 et memes_choix")
course = A.nouvelle_course(T); c1 = A.fichier_de_configuration(T, course=course, rang=1, choix={cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_EN_ATTENTE}); A.constat(T, c1)
essai("« en attente », motif rencontré", lambda: lire(A.piece(T, A.sortie({J: A.cas_b("juge", 1.0, motif=A.M_NON_AJUSTABLE)}, piece_source="X")), c1))
print("   constat « pièce en attente » :", [x.name[:44] for x in A.dossier_des_arrets(c1).glob("piece-en-attente-*.json")])
essai("ensuite une autre pièce, sans GO", lambda: etat(lire(A.piece(T, A.sortie(piece_source="Y")), c1)))
course = A.nouvelle_course(T)
A.fichier_de_configuration(T, course=course, rang=1, choix={cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_EN_ATTENTE})
A.fichier_de_configuration(T, course=course, rang=2, choix={cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_AIRE_NON_CALCULABLE}, pieces={cf.REGISTRE_ATTENDU: "e" * 64})
c3 = A.fichier_de_configuration(T, course=course, rang=3, choix={cf.CHOIX_NON_AJUSTABLE: cf.NON_AJUSTABLE_MODULE_CORRIGE}, pieces={cf.REGISTRE_ATTENDU: "f" * 64})
essai("rang 3 « module corrigé » après rang 2 « aire non calculable »", lambda: cf.exiger_configurations_de_la_course(cf.lire_la_configuration_scellee(c3)) and "admis")
