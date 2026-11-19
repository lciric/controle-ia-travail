"""Essais d'attaque v6 : fichier de l'étape (m) et ses constats (M-3), fichier des rangs (M-4), arrêts consignés,
issue d'un arrêt (M-6), ligne d'accord (M-2). Synthétique."""
import contextlib, io, json, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
sys.path.insert(0, "/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v6")
import aide_bras_a_v6 as A
from controle_ia.organismes_discrets import analyse_bras_a_v6 as an, arrets_bras_a_v6 as ar, configuration_bras_a_v6 as cf
from controle_ia.organismes_discrets import verdicts_bras_a_v6 as v, graines_bras_a_v6 as g
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
with contextlib.redirect_stdout(io.StringIO()):
    import attaques_regle_v6 as R
essai = R.essai
T = Path(tempfile.mkdtemp())
res = A.regle(T)
conf = res["configuration"]["chemin"]

# M-3 : constats écrits à la main, journal sous A15, lignes déclarées vides
d = A.nouveau_dossier(T, "a15")
contenu = an._contenu_du_fichier_de_l_etape_m(res, {1.0: "C6"})
f = A.ecrire_scelle(d / an.NOM_DU_FICHIER_DE_L_ETAPE_M, json.dumps(contenu, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
emp = A.empreinte(f)
c = {"etape": "m", "journal_de_la_table_a": ["A15"], "lignes_de_la_table_a": [], "renvoi_de_la_base": an.RENVOI_DE_LA_BASE_VERIFIE,
     "effectifs_de_la_base_conformes": True, "sha256_de_la_livraison": res["livraison"]["sha256"],
     "sha256_de_la_configuration": "f" * 64, "sha256_du_fichier_de_l_etape_m": emp}
A.ecrire_scelle(d / an.NOM_DU_FICHIER_DES_CONSTATS_DE_L_ETAPE_M, c)
essai("M-3 constats a la main : journal ['A15'], lignes [] declarees, configuration inventee", lambda: an.exiger_fichier_de_l_etape_m(f)[1]["journal_de_la_table_a"])
print("   lire_table_a(['A15']).lignes =", v.lire_table_a(["A15"]).lignes)

# fichier des rangs : livraison avec rangs ; piece d'une autre livraison
# arrêt consigné : contenu du fichier d'arrêt
arr = A.nouveau_dossier(T, "arrets")
e = A.cas_a("juge", 1.0, aire=0.7123, pli0=0.7011, pli1=0.7235, egales=7, borne_haute=None, quantile_borne_haute=None)
essai("arret consigne (borne nulle au cas A)", lambda: A.regle(T, {("juge", 1.0): e}, dossier=arr))
for x in sorted(arr.iterdir()):
    t = x.read_text()
    print("   fichier d'arret :", x.name, "| porte un nombre de la livraison ?", any(n in t for n in ("0.7123", "0.7011", "0.7235", "2000", "1280")), "|", t.replace("\n", " ")[:300])
# relire la même livraison : refusée ; une autre sans GO : refusée ; GO inconnu : refusé
essai("livraison deja refusee, relue", lambda: an.regle_de_discretion(A.piece(T, A.sortie({("juge", 1.0): e})), conf, dossier_des_arrets=arr, go_de_la_reprise=None))
essai("livraison refaite sans GO", lambda: A.regle(T, dossier=arr, go=None)["etats"][1.0]["juge"])
essai("livraison refaite, GO absent du registre", lambda: A.regle(T, dossier=arr, go="GO-2099-12-31-99")["etats"][1.0]["juge"])
# phrase d'accord : une ligne qui accorde en mentionnant la livraison refusée
import controle_ia.organismes_discrets.graines_bras_a_v6 as gg
reg = A.registre(A.nouveau_dossier(T, "reg"), [
    "| GO-2099-01-01-01 | 2099-01-01 | décision | Livraison refaite du côté habilité accordée pour le bras A, après la livraison refusée du 20 novembre (module v9 contre-lu) |",
    "| GO-2099-01-01-02 | 2099-01-01 | décision | Livraison refaite du côté habilité accordée pour le bras A |"])
gg.REGISTRE_DES_ACCORDS = reg
essai("ligne d'accord qui mentionne « la livraison refusée »", lambda: g.ligne_d_accord("GO-2099-01-01-01", g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE)[:40])
essai("ligne d'accord a la lettre", lambda: g.ligne_d_accord("GO-2099-01-01-02", g.PHRASE_DE_L_ACCORD_D_UNE_LIVRAISON_REFAITE)[:40])
essai("une meme ligne d'accord ouvre une 2e livraison refaite", lambda: A.regle(T, dossier=arr, go="GO-2099-01-01-02")["etats"][1.0]["juge"])
e2 = A.cas_a("juge", 1.0, borne_haute=None, quantile_borne_haute=None, egales=8)
essai("…qui est refusee aussi", lambda: A.regle(T, {("juge", 1.0): e2}, dossier=arr, go="GO-2099-01-01-02"))
essai("…puis une 3e, sur la meme ligne", lambda: A.regle(T, dossier=arr, go="GO-2099-01-01-02")["etats"][1.0]["juge"])

# issue d'un arrêt : les trois valeurs, arrêt en (m) et en (n)
ra = v.lire_table_a([])
lb = {0.5: "B8", 0.75: "B8", 1.0: "B9"}
for issue in cf.VALEURS_DES_CHOIX[cf.CHOIX_ISSUE]:
    cfg = A.fichier_de_configuration(T, {cf.CHOIX_ISSUE: issue})
    for etape, lc in (("m", {}), ("n", {0.5: "C6", 0.75: "C5"})):
        k = {"garde": ar.GARDE_FORME, "champ": "borne_haute", "cas": "A", "etape": etape, "moniteur": "juge", "dose": "dose-1.00"}
        if etape == "n":
            k.update(garde=ar.GARDE_RANGS, champ="rang", cas=ar.AUCUN_CAS, moniteur=None, dose=None)
        essai(f"issue « {issue} », arret en ({etape})", lambda: {x: y for x, y in v.issues(ra, lb, lc, True, True, True, arret=k, configuration_scellee=cfg).items()
                                                               if x in ("desappariement", "discretion", "grandeurs_de_l_etape_n")})
# arrêt sans configuration
essai("issues avec arret et sans configuration", lambda: v.issues(ra, lb, {}, True, True, True, arret={"garde": ar.GARDE_FORME, "champ": "aire", "cas": "A", "etape": "m", "moniteur": "juge", "dose": "dose-1.00"}, configuration_scellee=None))
# issues sans arrêt, avec renvoi non vérifié : « non lue » par fausse déclaration (porte de la v5)
essai("issues sans arret, renvoi declare non verifie", lambda: v.issues(ra, lb, {}, False, True, True, arret=None, configuration_scellee=None)["discretion"])
# constat porteur d'un nombre
essai("constat avec un champ 'aire=0.7'", lambda: ar.exiger_constat({"garde": ar.GARDE_FORME, "champ": "aire=0.7", "cas": "A", "etape": "m", "moniteur": "juge", "dose": "dose-1.00"}))
