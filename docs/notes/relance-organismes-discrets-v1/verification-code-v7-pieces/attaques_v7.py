"""Essais d'attaque, vérification des corrections du code v7 (bras A). Données synthétiques ; registre fabriqué."""
import copy, json, os, sys, tempfile, traceback
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v7 as A
from controle_ia.organismes_discrets import analyse_bras_a_v7 as an, arrets_bras_a_v7 as ar, configuration_bras_a_v7 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v7 as v, graines_bras_a_v7 as g
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {r}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:150]}"); return e
    except BaseException as e:
        print(f"ERREUR  {nom} -> {type(e).__name__}: {str(e)[:150]}"); return e
J = ("juge", 1.0)
etat = lambda res: res["etats"][1.0]["juge"]
r = lambda change=None, **k: A.regle(T, change, **k)

print("--- C-1 : contrôles désormais écrits au texte")
e = A.cas_a("juge", 1.0, egales=5); e["valeur_p_haut"] = round(e["valeur_p_haut"], 4); e["valeur_p_pour_la_famille"] = e["valeur_p_haut"]; e["valeur_p_bas"] = round(e["valeur_p_bas"], 4)
essai("valeurs p arrondies a 4 decimales", lambda: etat(r({J: e})))
e = A.cas_a("juge", 1.0, egales=5); e["valeur_p_haut"] = round(e["valeur_p_haut"], 3); e["valeur_p_pour_la_famille"] = e["valeur_p_haut"]
essai("valeur p haute arrondie a 3 decimales (ecart sous le demi-pas)", lambda: etat(r({J: e})))
essai("valeur p 0,3 avec zero aire au moins egale", lambda: etat(r({J: A.cas_a("juge", 1.0, egales=0, valeur_p_haut=0.3, valeur_p_pour_la_famille=0.3)})))
essai("famille = p_haut + 2^-60", lambda: etat(r({J: dict(A.cas_a("juge", 1.0, egales=5), valeur_p_pour_la_famille=A.cas_a("juge", 1.0, egales=5)["valeur_p_haut"] + 2**-60)})))
essai("aire 1.2", lambda: etat(r({J: A.cas_a("juge", 1.0, aire=1.2, pli0=1.19, pli1=1.21)})))
essai("borne rendue sans quantile", lambda: etat(r({J: A.cas_a("juge", 1.0, quantile_borne_haute=None)})))
essai("borne nulle, quantile rendu (non lu)", lambda: r({("juge", 0.25): A.cas_a("juge", 0.25, borne=None)})["lectures"]["dose-0.25"]["juge"]["rapport"]["borne_haute"])
s = A.sortie(); s["lectures"] = [x for d in reversed(list(s["lectures"])) for x in reversed(list(s["lectures"][d].values()))]
essai("lectures en liste, ordre inverse", lambda: etat(r(contenu=s)))
s = A.sortie(); s["lectures"]["dose-1.00"]["juge"] = A.cas_a("classifieur-lexical", 1.0)
essai("lecture hors de sa place", lambda: etat(r(contenu=s)))

print("--- M-4 : trace d'appel")
e = A.cas_a("juge", 1.0, aire=0.7123, pli0=0.7011, pli1=0.7235, egales=7, borne_haute=None, quantile_borne_haute=None)
try:
    r({J: e})
except ar.ArretDeLaLectureDeLaDiscretion as x:
    vus, tb = [], x.__traceback__
    while tb is not None:
        for k, val in list(dict(tb.tb_frame.f_locals).items()):
            if "0.7123" in repr(val)[:200000]: vus.append((tb.tb_frame.f_code.co_name, k))
        tb = tb.tb_next
    print("   cause/contexte :", x.__cause__, x.__context__, "| variables de la trace qui portent l'aire 0.7123 :", vus)

print("--- M-5 : reprise retouchee dans le resultat")
res = r()
y = copy.deepcopy(res); y["reprise"] = {"ligne_de_go": "GO-2099-01-01-01", "sha256_de_la_livraison_refusee": "a" * 64, "sha256_de_l_acte": "b" * 64}
essai("reprise inventee dans le resultat", lambda: an.etats_pour_la_table_c(y, 1.0)["juge d'une autre lignée"])
y = copy.deepcopy(res); y["etats"][1.0]["juge"] = an.REPERE; y["lectures"]["dose-1.00"]["juge"]["etat"] = an.REPERE
essai("etat retouche (C-1 de la v5)", lambda: an.etats_pour_la_table_c(y, 1.0)["juge d'une autre lignée"])

print("--- C-2 et M-3 : livraison refaite, registre attendu")
arr = A.nouveau_dossier(T, "arrets")
p_ref = A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None)}))
c0 = A.fichier_de_configuration(A.nouveau_dossier(T, "c"))
essai("premiere livraison refusee", lambda: an.regle_de_discretion(p_ref, c0, dossier_des_arrets=arr, go_de_la_reprise=None))
fa = A.fichier_d_arret(arr, p_ref)
print("   fichier d'arret :", sorted(json.loads(fa.read_text())))
reg = A.registre(A.nouveau_dossier(T, "reg"), [
    A.ligne_de_reprise("GO-2099-01-01-01", fa, plus=", après la livraison refusée du 20 novembre"),
    A.ligne_de_reprise("GO-2099-01-01-02", fa),
    "| GO-2099-01-01-03 | 2099-01-01 | décision | Livraison refaite du côté habilité accordée pour le bras A — refusé : module non contre-lu |",
    A.ligne_de_reprise("GO-2099-01-01-04", fa, plus=f" ; configuration {'d'*64}"),
])
g.REGISTRE_DES_ACCORDS = reg
emp = A.empreinte(reg)
cfg = lambda attendu=emp: A.fichier_de_configuration(A.nouveau_dossier(T, "c"), pieces={cf.REGISTRE_ATTENDU: attendu})
essai("registre attendu null, reprise", lambda: an.regle_de_discretion(A.piece(T, A.sortie()), cfg(None), dossier_des_arrets=arr, go_de_la_reprise="GO-2099-01-01-02"))
essai("registre d'une autre empreinte (perime)", lambda: an.regle_de_discretion(A.piece(T, A.sortie()), cfg("e" * 64), dossier_des_arrets=arr, go_de_la_reprise="GO-2099-01-01-02"))
essai("ligne 'refusé :'", lambda: g.ligne_d_accord("GO-2099-01-01-03", g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE, sha256_attendu_du_registre=emp)[:30])
essai("ligne qui nomme 'la livraison refusée'", lambda: g.ligne_d_accord("GO-2099-01-01-01", g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE, sha256_attendu_du_registre=emp)[:30])
essai("ligne qui cite quatre empreintes (dont la configuration)", lambda: etat(an.regle_de_discretion(A.piece(T, A.sortie()), cfg(), dossier_des_arrets=arr, go_de_la_reprise="GO-2099-01-01-04")))
r2 = essai("livraison refaite sur GO-02", lambda: etat(an.regle_de_discretion(A.piece(T, A.sortie()), cfg(), dossier_des_arrets=arr, go_de_la_reprise="GO-2099-01-01-02")))
essai("une 2e livraison refaite sur la meme ligne GO-02", lambda: etat(an.regle_de_discretion(A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, egales=3)})), cfg(), dossier_des_arrets=arr, go_de_la_reprise="GO-2099-01-01-02")))
essai("une 2e livraison refaite sur GO-01 (meme fichier d'arret, deja repris)", lambda: etat(an.regle_de_discretion(A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, egales=4)})), cfg(), dossier_des_arrets=arr, go_de_la_reprise="GO-2099-01-01-01")))
print("   compte :", an.compte_des_livraisons(arr))
# panne entre l'acte et la fin de la lecture
arr2 = A.nouveau_dossier(T, "arrets2")
p2 = A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None, egales=9)}))
essai("refus (dossier 2)", lambda: an.regle_de_discretion(p2, c0, dossier_des_arrets=arr2, go_de_la_reprise=None))
fa2 = A.fichier_d_arret(arr2, p2)
reg2 = A.registre(A.nouveau_dossier(T, "reg2"), [A.ligne_de_reprise("GO-2099-02-02-01", fa2), A.ligne_de_reprise("GO-2099-02-02-02", fa2)])
g.REGISTRE_DES_ACCORDS = reg2
cfg2 = A.fichier_de_configuration(A.nouveau_dossier(T, "c"), pieces={cf.REGISTRE_ATTENDU: A.empreinte(reg2)})
p_refaite = A.piece(T, A.sortie())
vrai = an._regle
def panne(*a, **k): raise KeyboardInterrupt("panne simulee")
an._regle = panne
essai("panne pendant la lecture de la livraison refaite", lambda: an.regle_de_discretion(p_refaite, cfg2, dossier_des_arrets=arr2, go_de_la_reprise="GO-2099-02-02-01"))
an._regle = vrai
essai("relecture apres la panne, meme ligne", lambda: etat(an.regle_de_discretion(p_refaite, cfg2, dossier_des_arrets=arr2, go_de_la_reprise="GO-2099-02-02-01")))
essai("relecture apres la panne, ligne neuve", lambda: etat(an.regle_de_discretion(p_refaite, cfg2, dossier_des_arrets=arr2, go_de_la_reprise="GO-2099-02-02-02")))
# panne entre l'écriture de l'acte et son scellement
arr3 = A.nouveau_dossier(T, "arrets3")
p3 = A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None, egales=11)}))

try: an.regle_de_discretion(p3, c0, dossier_des_arrets=arr3, go_de_la_reprise=None)
except GardeArret: pass
fa3 = A.fichier_d_arret(arr3, p3)
reg3 = A.registre(A.nouveau_dossier(T, "reg3"), [A.ligne_de_reprise("GO-2099-03-03-01", fa3)])
g.REGISTRE_DES_ACCORDS = reg3
cfg3 = A.fichier_de_configuration(A.nouveau_dossier(T, "c"), pieces={cf.REGISTRE_ATTENDU: A.empreinte(reg3)})
vrai_sceller = an.sceller
def sceller_en_panne(chemin):
    if "reprise-" in str(chemin): raise KeyboardInterrupt("panne avant le scellement de l'acte")
    return vrai_sceller(chemin)
an.sceller = sceller_en_panne
essai("panne entre l'ecriture de l'acte et son scellement", lambda: an.regle_de_discretion(A.piece(T, A.sortie()), cfg3, dossier_des_arrets=arr3, go_de_la_reprise="GO-2099-03-03-01"))
an.sceller = vrai_sceller
essai("le dossier apres cette panne (toute lecture)", lambda: an.compte_des_livraisons(arr3))

print("--- M-1 : constats de l'etape (m)")
res = A.regle(T)
d = A.nouveau_dossier(T, "m-a15")
contenu = an._contenu_du_fichier_de_l_etape_m(res, {1.0: "C6"})
f = A.ecrire_scelle(d / an.NOM_DU_FICHIER_DE_L_ETAPE_M, json.dumps(contenu, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
base_c = {"etape": "m", "journal_de_la_table_a": ["A15"], "lignes_de_la_table_a": [], "renvoi_de_la_base": an.RENVOI_DE_LA_BASE_VERIFIE,
          "effectifs_de_la_base_conformes": True, "sha256_de_la_livraison": res["livraison"]["sha256"],
          "sha256_de_la_configuration": res["configuration"]["sha256"], "sha256_du_fichier_de_l_etape_m": A.empreinte(f)}
A.ecrire_scelle(d / an.NOM_DU_FICHIER_DES_CONSTATS_DE_L_ETAPE_M, base_c)
essai("constats a la main, journal ['A15']", lambda: an.exiger_fichier_de_l_etape_m(f, piece_scellee=res["livraison"]["chemin"], configuration_scellee=res["configuration"]["chemin"])[1]["journal_de_la_table_a"])
d = A.nouveau_dossier(T, "m-a7")
f = A.ecrire_scelle(d / an.NOM_DU_FICHIER_DE_L_ETAPE_M, json.dumps(contenu, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
A.ecrire_scelle(d / an.NOM_DU_FICHIER_DES_CONSTATS_DE_L_ETAPE_M, dict(base_c, journal_de_la_table_a=["A7"], sha256_du_fichier_de_l_etape_m=A.empreinte(f)))
print("   lire_table_a(['A7'], revision_refusee=True) :", v.lire_table_a(["A7"], True, False).lignes, "| sans le reglage :", v.lire_table_a(["A7"]).lignes)
essai("constats a la main, journal ['A7'] dont la revision a ete refusee (releve B.18)", lambda: an.exiger_fichier_de_l_etape_m(f, piece_scellee=res["livraison"]["chemin"], configuration_scellee=res["configuration"]["chemin"])[1]["journal_de_la_table_a"])
essai("ecriture sous ['A7'] revision refusee", lambda: v.ecrire_fichier_de_l_etape_m(A.nouveau_dossier(T, "w"), journal=["A7"], revision_refusee=True, gardees_lues=False,
      renvoi_de_la_base=an.RENVOI_DE_LA_BASE_VERIFIE, effectifs_de_la_base_conformes=True, resultat_de_discretion=res, lignes_c={1.0: "C6"}).name)

print("--- M-2 : issues, dossier donne par l'appelant")
arr4 = A.nouveau_dossier(T, "arrets4")
p4 = A.piece(T, A.sortie({J: A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None, egales=13)}))
try: an.regle_de_discretion(p4, c0, dossier_des_arrets=arr4, go_de_la_reprise=None)
except GardeArret: pass
ra, lb = v.lire_table_a([]), {0.5: "B8", 0.75: "B8", 1.0: "B9"}
essai("issues : vrai dossier, piece refusee", lambda: v.issues(ra, lb, {}, True, True, True, dossier_des_arrets=arr4, piece_scellee=p4, configuration_scellee=c0, fichier_de_l_etape_m=None)["discretion"])
essai("issues : dossier vide neuf, piece None, renvoi dit non verifie", lambda: v.issues(ra, lb, {}, False, True, True, dossier_des_arrets=A.nouveau_dossier(T, "vide"), piece_scellee=None, configuration_scellee=c0, fichier_de_l_etape_m=None)["discretion"])

print("--- M-7 : contenus rendus tels quels")
s = A.sortie({J: A.cas_a("juge", 1.0, effectifs={"texte": "ACTION: score 0.93"})}); s["exclues"] = {"x": "texte libre"}
essai("effectifs et exclues de texte", lambda: r(contenu=s)["lectures"]["dose-1.00"]["juge"]["effectifs"])
