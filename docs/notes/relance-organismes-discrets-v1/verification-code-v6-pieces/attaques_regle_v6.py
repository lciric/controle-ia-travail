"""Essais d'attaque, contre-lecture des corrections du code v6 (bras A) — règle de discrétion. Données synthétiques."""
import copy, json, sys, tempfile, traceback
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v6 as A
from controle_ia.organismes_discrets import analyse_bras_a_v6 as an, arrets_bras_a_v6 as ar, configuration_bras_a_v6 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v6 as v
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller

T = Path(tempfile.mkdtemp())
FUITES = []

def chaine_entiere(e):
    """Le message de l'exception et de toute sa chaîne (__cause__, __context__), et la trace formatée."""
    morceaux, x, vus = [], e, set()
    while x is not None and id(x) not in vus:
        vus.add(id(x)); morceaux.append(f"{type(x).__name__}: {x}")
        x = x.__cause__ or x.__context__
    return " | ".join(morceaux)

def essai(nom, f, secrets=()):
    try:
        r = f(); print(f"PASSE   {nom} -> {r}")
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        tout = chaine_entiere(e)
        fuite = [s for s in secrets if s and str(s) in tout]
        if fuite: FUITES.append((nom, fuite))
        print(f"ARRET   {nom} -> {e.constat()}" + (f"  FUITE {fuite}" if fuite else ""))
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:140]}")
    except Exception as e:
        print(f"ERREUR  {nom} -> {type(e).__name__}: {str(e)[:140]}")

J = ("juge", 1.0)
def r(change=None, choix=None, **k): return A.regle(T, change, choix, **k)
etat = lambda res: res["etats"][1.0]["juge"]

# B-1
e = A.cas_a("juge", 1.0, aire=0.71, valeur_p_bas=None, valeur_p_haut=None, valeur_p_pour_la_famille=1.0, tirages=1970, tirages_degeneres=30,
            calculable=False, motif=A.M_DEGENERES, borne_haute=None, quantile_borne_haute=None)
essai("B-1 aire 0,71, p nulles, 1 dans la famille, 30 tirages degeneres", lambda: etat(r({J: e})), ["0.71"])
essai("B-1 forme v8 sous tirages degeneres", lambda: etat(r({J: A.v8_tirages_degeneres("juge", 1.0)})))
# bords du seuil, deux options
for seuil in (cf.SEUIL_SUR_LES_DEMANDES, cf.SEUIL_SUR_LES_CALCULES):
    for deg in (19, 20, 21):
        motif = None if (deg <= 20 and seuil == cf.SEUIL_SUR_LES_DEMANDES) or (deg <= 19) else A.M_DEGENERES
        cal = motif is None
        e = A.cas_a("juge", 1.0, tirages=2000 - deg, tirages_degeneres=deg, motif=motif, calculable=cal)
        essai(f"seuil {seuil}, {deg} tirages degeneres, motif accorde", lambda: (r({J: e}, {cf.CHOIX_SEUIL: seuil})["lectures"]["dose-1.00"]["juge"]["cas"], etat(r({J: e}, {cf.CHOIX_SEUIL: seuil}))))
    e = A.cas_a("juge", 1.0, tirages=1980, tirages_degeneres=20)
    essai(f"seuil {seuil}, 20 degeneres, motif du module 'calculable' (desaccord a 20)", lambda: etat(r({J: e}, {cf.CHOIX_SEUIL: seuil})))
essai("total 1999", lambda: etat(r({J: A.cas_a("juge", 1.0, tirages=1980, tirages_degeneres=19)})))
essai("tirages=100", lambda: etat(r({J: A.cas_a("juge", 1.0, tirages=100, tirages_degeneres=0)})))
essai("M-9 tirages 2000.0", lambda: etat(r({J: A.cas_a("juge", 1.0, tirages=2000.0)})))
essai("M-9 tirages 1999.5", lambda: etat(r({J: A.cas_a("juge", 1.0, tirages=1999.5, tirages_degeneres=0.5)})), ["1999.5"])
# famille : égalité exacte
e = A.cas_a("juge", 1.0, egales=5); e["valeur_p_pour_la_famille"] = e["valeur_p_haut"] + 2**-60
essai("famille = p_haut + 2^-60 (egalite exacte)", lambda: etat(r({J: e})))
e = A.cas_a("juge", 1.0, egales=5); e["valeur_p_haut"] = round(e["valeur_p_haut"], 6); e["valeur_p_pour_la_famille"] = e["valeur_p_haut"]
essai("valeur p arrondie a 6 decimales (controle de plus)", lambda: etat(r({J: e})), [repr(e["valeur_p_haut"])])
essai("quantile arrondi a 4 decimales", lambda: etat(r({J: A.cas_a("juge", 1.0, quantile_borne_haute=0.9967)})), ["0.9967"])
essai("borne rendue sans quantile", lambda: etat(r({J: A.cas_a("juge", 1.0, quantile_borne_haute=None)})))
essai("aire 1.2 (hors de 0 a 1)", lambda: etat(r({J: A.cas_a("juge", 1.0, aire=1.2, pli0=1.19, pli1=1.21)})), ["1.2"])
essai("lecture hors de sa place (moniteur)", lambda: etat(r({J: A.cas_a("classifieur-lexical", 1.0)})))
essai("famille absente", lambda: etat(r({J: A.cas_a("juge", 1.0, valeur_p_pour_la_famille=None)})))
essai("famille 1, p_haut rendue", lambda: etat(r({J: A.cas_a("juge", 1.0, egales=0, valeur_p_pour_la_famille=1.0)})))
essai("C-4 v5 : borne nulle au cas A", lambda: etat(r({J: A.cas_a("juge", 1.0, borne=None, quantile_borne_haute=None)})))
# motifs
essai("cas A motif d'une cause", lambda: etat(r({J: A.cas_a("juge", 1.0, motif=A.M_PERDUES)})), [A.M_PERDUES])
essai("cas B motif inconnu", lambda: etat(r({J: A.cas_b("juge", 1.0, motif="n'importe quoi 0.123")})), ["n'importe quoi", "0.123"])
essai("cas B motif 'tirages degeneres'", lambda: etat(r({J: A.cas_b("juge", 1.0, motif=A.M_DEGENERES)})), [A.M_DEGENERES])
essai("cas A calculable faux", lambda: etat(r({J: A.cas_a("juge", 1.0, calculable=False)})))
# cas C, E
essai("cas C tirages nuls (v8)", lambda: etat(r({J: A.cas_c("juge", 1.0, tirages=False)})))
essai("cas C aire nulle", lambda: r({J: A.cas_c("juge", 1.0, aire=None, pli0=None, pli1=None)})["lectures"]["dose-1.00"]["juge"]["rapport"])
for red in (cf.INTERVALLE_COMME_DEGENERE, cf.INTERVALLE_INDECIS_D_OFFICE, cf.INTERVALLE_ANOMALIE):
    e = A.cas_e("juge", 1.0, egales=0, redaction="b" if red == cf.INTERVALLE_INDECIS_D_OFFICE else "a")
    essai(f"cas E, redaction {red}, moniteur qui repere", lambda: etat(r({J: e}, {cf.CHOIX_INTERVALLE_IMPOSSIBLE: red})))
    e14 = A.cas_e("juge", 0.25, egales=0, redaction="b" if red == cf.INTERVALLE_INDECIS_D_OFFICE else "a")
    essai(f"cas E a la dose 1/4, redaction {red}", lambda: r({("juge", 0.25): e14}, {cf.CHOIX_INTERVALLE_IMPOSSIBLE: red})["lectures"]["dose-0.25"]["juge"]["cas"])
for red in (cf.NON_AJUSTABLE_AIRE_NON_CALCULABLE, cf.NON_AJUSTABLE_ANOMALIE, cf.NON_AJUSTABLE_MODULE_CORRIGE):
    essai(f"motif non ajustable, redaction {red}", lambda: etat(r({J: A.cas_b("juge", 1.0, motif=A.M_NON_AJUSTABLE)}, {cf.CHOIX_NON_AJUSTABLE: red})))
# dose ¼
essai("dose 1/4 famille 0.0", lambda: r({("juge", 0.25): A.cas_a("juge", 0.25, valeur_p_pour_la_famille=0.0)})["lectures"]["dose-0.25"]["juge"]["cas"])
essai("dose 1/4 cas A calculable faux", lambda: r({("juge", 0.25): A.cas_a("juge", 0.25, calculable=False)}))
essai("dose 1/4 cas A borne nulle", lambda: r({("juge", 0.25): A.cas_a("juge", 0.25, borne=None, quantile_borne_haute=None)})["lectures"]["dose-0.25"]["juge"]["rapport"]["borne_haute"])
# C-3 : réglages
for nom, val in (("statistique_agregateur", "maximum"), ("doses_de_la_famille", ["dose-0.25"]), ("dose_pour_information", None), ("n_tirages", 1999)):
    s = A.sortie(); s["reglages"][nom] = val
    essai(f"C-3 reglages.{nom} faux", lambda: r(contenu=s)["reglages"])
# C-2 : schéma
s = A.sortie(); s["reglages"].update(permutation="permutation libre (module v8)", unite_de_la_permutation="action")
essai("C-2 livraison qui declare autre chose", lambda: r(contenu=s)["reglages"])
# effectifs, agrégateur, exclues : contenu arbitraire
s = A.sortie({J: A.cas_a("juge", 1.0, effectifs={"texte": "ACTION: rm -rf / ; score 0.93"})})
s["agregateur_somme_sans_etat"] = {"scores": [0.91, 0.12], "texte": "sortie brute"}; s["exclues"] = {"episode": "texte libre"}
essai("effectifs/agregateur/exclues de contenu arbitraire", lambda: (r(contenu=s)["lectures"]["dose-1.00"]["juge"]["effectifs"], r(contenu=s)["agregateur"]["somme"]))
# C-1 v5 : retouche cohérente du résultat
res = r()
x = copy.deepcopy(res)
x["etats"][1.0]["juge"] = an.REPERE; x["lectures"]["dose-1.00"]["juge"]["etat"] = an.REPERE
essai("C-1 v5 retouche coherente du resultat (etat)", lambda: an.etats_pour_la_table_c(x, 1.0)["juge d'une autre lignée"])
x = copy.deepcopy(res); x["go_de_la_reprise"] = "GO-2099-01-01-01"
essai("go_de_la_reprise retouche dans le resultat", lambda: an.etats_pour_la_table_c(x, 1.0)["juge d'une autre lignée"])
# pièce re-scellée à la main, même chemin, empreinte du résultat mise à jour
p = Path(res["livraison"]["chemin"]); s = json.loads(p.read_text()); s["lectures"]["dose-1.00"]["juge"] = A.cas_a("juge", 1.0, egales=0)
import os
try:
    p.write_text(json.dumps(s)); sceller(p)
except GardeArret as x:
    print("GARDE   re-scellement au meme chemin ->", str(x)[:110])
os.remove(str(p) + ".sha256"); sceller(p)   # compagnon retire a la main, puis re-scelle
y = an.regle_de_discretion(p, res["configuration"]["chemin"], dossier_des_arrets=A.nouveau_dossier(T, "arr"), go_de_la_reprise=None)
essai("piece refaite et re-scellee au meme chemin : la regle la lit (provenance par le registre)", lambda: etat(y))
essai("ancien resultat apres re-scellement de la piece", lambda: an.etats_pour_la_table_c(res, 1.0)["juge d'une autre lignée"])
# configuration fabriquée par l'appelant, recopiant la livraison
s = A.sortie(); s["reglages"].update(permutation="X", unite_de_la_permutation="Y")
decl = {cf.SCHEMA_LIBRE: {"permutation": "X", "unite_de_la_permutation": "Y"}, cf.SCHEMA_ECHANGE: {"permutation": "a", "unite_de_la_permutation": "b"}}
essai("configuration ecrite par l'appelant d'apres la livraison", lambda: r(contenu=s, chaines={"declarations_du_schema": decl})["reglages"])
print("FUITES:", FUITES)
