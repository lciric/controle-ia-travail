# -*- coding: utf-8 -*-
"""Essais du programme de vérification de la sortie de l'auteur des mondes — v1.

Un cas sain ; pour chaque garde, au moins un artefact qui la fait tomber (R5) ;
les erreurs d'usage ; puis les mutations : chaque garde neutralisée dans une
copie du programme fait échouer son essai.

Lancement : /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider \
    --basetemp=DOSSIER/essais-tmp DOSSIER/test_verifier_sortie_auteur_mondes_v1.py

Développeur du programme de vérification de la sortie des mondes, modèle O.
"""

import copy
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

import fabriquer_sorties_factices_v1 as fab
from fabriquer_sorties_factices_v1 import Brut

ICI = Path(__file__).resolve().parent
PROGRAMME = ICI / "verifier_sortie_auteur_mondes_v1.py"
MOTIFS = ICI / "motifs-noms-refuses-essai-v1.txt"
SORTIE_SAINE = ICI / "sortie-factice-saine-v1.json"
OBSERVATIONS_SAINES = {"O_PLUS_DE_VINGT_HUIT_TEMOINS"}
POINT = {"1": "1_forme", "2": "2_completude", "3": "3_coherence", "5": "5_motifs"}


# ---------------------------------------------------------------------------
# Outils
# ---------------------------------------------------------------------------

def texte(d):
    return fab.serialiser(d) + "\n"


def jouer(contenu, dossier, programme=PROGRAMME, motifs=MOTIFS):
    dossier.mkdir(parents=True, exist_ok=True)
    sortie = dossier / "sortie.json"
    rapport = dossier / "rapport.json"
    for p in (sortie, rapport):
        if p.exists():
            p.unlink()
    if isinstance(contenu, dict):
        contenu = texte(contenu)
    if isinstance(contenu, str):
        contenu = contenu.encode("utf-8")
    sortie.write_bytes(contenu)
    r = subprocess.run([sys.executable, "-I", "-B", str(programme), str(sortie), str(rapport),
                        "--motifs", str(motifs)], capture_output=True, text=True, timeout=120)
    rap = json.loads(rapport.read_text(encoding="utf-8")) if rapport.exists() else None
    return r.returncode, rap


def codes(rap, point):
    return {f["code"] for f in rap["points"][POINT[point]]["fautes"]}


def codes_observes(rap):
    return {o["code"] for o in rap["observations"]}


def tem(d, tid):
    return next(t for t in d["temoins"] if t["id"] == tid)


def fam(d, fid):
    return next(f for f in d["familles"] if f["id"] == fid)


def ecart(d):
    return d["a_l_ecart"][0]


def sans_temoin(d, tid):
    d["temoins"] = [t for t in d["temoins"] if t["id"] != tid]
    return d


def copie_de_famille(f, nouvel_id, imposee=False):
    g = copy.deepcopy(f)
    g["id"] = nouvel_id
    g["nom"] = "copie d'essai " + nouvel_id
    g["imposee"] = imposee
    if "temoins" in g:
        for i, t in enumerate(g["temoins"]):
            t["id"] = "C%s%d" % (nouvel_id, i)
            t["monde"] = nouvel_id
    return g


def lignes_de_table(f):
    return [{"monde": f["id"], "supposition_cassee": s} for s in (f["suppositions_cassees"] or ["aucune"])]


def sain():
    return fab.sortie_saine()


class Artefact:
    def __init__(self, nom, code, fabrique, attendus=None, sortie=None, monde=None):
        self.nom, self.code, self.fabrique = nom, code, fabrique
        self.attendus = attendus or {code}
        self.monde = monde
        if sortie is None:
            if code.startswith(("P1", "P2")):
                sortie = 2
            elif code.startswith(("P3", "P5")):
                sortie = 1
            else:
                sortie = 0
        self.sortie = sortie


def controler(a, retour, rap):
    assert rap is not None, "aucun rapport écrit"
    assert retour == a.sortie == rap["code_de_sortie"]
    if a.code.startswith("P"):
        point = a.code[1]
        assert rap["points"][POINT[point]]["verdict"] == "manque"
        assert codes(rap, point) == a.attendus
    elif a.code.startswith("E"):
        assert rap["verdict_d_ensemble"] == "lisible"
        assert any(e["monde"] == a.monde and a.code in e["raisons"] for e in rap["ecartes"])
    else:
        assert rap["verdict_d_ensemble"] == "lisible"
        assert a.code in codes_observes(rap)


# ---------------------------------------------------------------------------
# Artefacts
# ---------------------------------------------------------------------------

def f_(fonction):
    """Applique `fonction` en place à une copie saine et rend la copie (le retour de la fonction est ignoré)."""
    def fabrique():
        d = sain()
        fonction(d)
        return d
    return fabrique


def ordre_inverse(d):
    cles = list(d)
    cles[1], cles[2] = cles[2], cles[1]
    contenu = dict(d)
    d.clear()
    for k in cles:
        d[k] = contenu[k]


def deplacer_g_a_l_ecart(d):
    g = fam(d, "G")
    d["familles"].remove(g)
    g["temoins"] = [t for t in d["temoins"] if t["monde"] == "G"]
    d["temoins"] = [t for t in d["temoins"] if t["monde"] != "G"]
    d["a_l_ecart"].append(g)


def retirer_g(d):
    d["familles"].remove(fam(d, "G"))
    d["temoins"] = [t for t in d["temoins"] if t["monde"] != "G"]
    d["table"] = [r for r in d["table"] if r["monde"] != "G"]


def trois_a_l_ecart(d):
    for nid in ("X", "Y"):
        g = copie_de_famille(ecart(d), nid)
        d["a_l_ecart"].append(g)
        d["table"] += lignes_de_table(g)


def vider_a_l_ecart(d):
    d["a_l_ecart"] = []
    d["table"] = [r for r in d["table"] if r["monde"] != "K"]


def aucun_de_marge(d):
    for t in d["temoins"]:
        if t["sorte"] == "de_marge":
            t["sorte"], t["issue_attendue"] = "doit_tenir", "tient"


def temoin_vers_z(d):
    t = copy.deepcopy(tem(d, "LB1"))
    t["id"], t["monde"] = "LZ9", "Z"
    d["temoins"].append(t)


def t05_a_l_ecart(d):
    t = tem(d, "T05")
    sans_temoin(d, "T05")
    t["monde"] = "K"
    ecart(d)["temoins"].append(t)


def famille_m(d):
    d["familles"].append(copie_de_famille(fam(d, "A"), "M"))


def famille_b_en_double(d):
    d["familles"].append(copy.deepcopy(fam(d, "B")))


def deux_objets_temoins(d):
    d["a_l_ecart"] += [{"temoins": []}, {"temoins": []}]


def loi_autre_sans_definition(d):
    fam(d, "A")["tranches"][0]["loi_honnete"] = {"type": "autre", "parametres": {"a": Brut("1.0")}}


def melange_boiteux(d):
    fam(d, "C")["tranches"][0]["loi_honnete"]["parametres"]["poids"] = [Brut("1.0")]


def couple_a_trois_marges(d):
    fam(d, "A")["tranches"][0]["loi_honnete"] = {
        "type": "couple", "parametres": {"marges": [fab.normale()] * 3, "dependance": "independance"}}


def remarque(texte_):
    def r(d):
        d["remarques"].append(texte_)
    return r


def interface_plus(cle, ajout):
    def r(d):
        d["interface"][cle] += ajout
    return r


def lk1_en_tete(d):
    t = next(x for x in ecart(d)["temoins"] if x["id"] == "LK1")
    ecart(d)["temoins"].remove(t)
    d["temoins"].append(t)


def retirer_temoin_a_l_ecart(tid):
    def r(d):
        ecart(d)["temoins"] = [t for t in ecart(d)["temoins"] if t["id"] != tid]
    return r


def familles_libres_trois(d):
    for nid in ("J", "L"):
        g = copie_de_famille(fam(d, "A"), nid)
        d["familles"].append(g)
        d["table"] += lignes_de_table(g)


CLE_SK = "sk-" + "Ab3x" * 6
CHAINE_MELANGEE = "Zq9" * 12
BLOC_PRIVE = "-----BEGIN " + "PRIVATE KEY-----"

ARTEFACTS = [
    # ---- point 1, forme ----
    Artefact("taille", "P1_TAILLE", f_(remarque("x" * 40100))),
    Artefact("utf8", "P1_UTF8", lambda: texte(sain()).encode("utf-8").replace(b"Sortie factice", b"Sortie \xff factice")),
    Artefact("texte_avant", "P1_TEXTE_AUTOUR_DE_L_OBJET", lambda: "Voici la sortie :\n" + texte(sain())),
    Artefact("bloc_de_code", "P1_TEXTE_AUTOUR_DE_L_OBJET", lambda: "```json\n" + texte(sain()) + "```\n"),
    Artefact("texte_apres", "P1_TEXTE_AUTOUR_DE_L_OBJET", lambda: texte(sain()) + "Fin.\n"),
    Artefact("marque_d_ordre", "P1_TEXTE_AUTOUR_DE_L_OBJET", lambda: "﻿" + texte(sain())),
    Artefact("cle_dupliquee", "P1_CLE_DUPLIQUEE", lambda: '{"version_forme": "x", ' + texte(sain())[1:]),
    Artefact("nan", "P1_NOMBRE_NON_FINI", lambda: texte(sain()).replace("0.4321", "NaN", 1)),
    Artefact("infini", "P1_NOMBRE_NON_FINI", lambda: texte(sain()).replace("0.4321", "1e999", 1)),
    Artefact("commentaire", "P1_JSON_INVALIDE", lambda: texte(sain()).replace('"temoins": [', '"temoins": [ // commentaire\n', 1)),
    Artefact("virgule_finale", "P1_JSON_INVALIDE", lambda: texte(sain()).replace('"non_calcule": []', '"non_calcule": [1,]', 1)),
    Artefact("pas_un_objet", "P1_PAS_UN_OBJET", lambda: "[" + texte(sain()) + "]"),
    Artefact("cle_en_trop_temoin", "P1_CLE_EN_TROP", f_(lambda d: tem(d, "T01").__setitem__("commentaire", "x"))),
    Artefact("cle_en_trop_famille_marquee", "P1_CLE_EN_TROP", f_(lambda d: fam(d, "B").__setitem__("tenue_a_l_ecart", True))),
    Artefact("cle_en_trop_premier_niveau", "P1_CLE_EN_TROP", f_(lambda d: d.__setitem__("en_plus", 1))),
    Artefact("cle_manquante_temoin", "P1_CLE_MANQUANTE", f_(lambda d: tem(d, "T01").pop("formule"))),
    Artefact("cle_manquante_premier_niveau", "P1_CLE_MANQUANTE", f_(lambda d: d.pop("remarques"))),
    Artefact("ordre_des_cles", "P1_ORDRE_DES_CLES", f_(ordre_inverse)),
    Artefact("version_forme", "P1_VERSION_FORME", f_(lambda d: d.__setitem__("version_forme", "mondes-plantes-seuil-et-moniteurs-v2"))),
    Artefact("sorte_inconnue", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: tem(d, "T01").__setitem__("sorte", "doit_peut_etre"))),
    Artefact("apostrophe_typographique", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: tem(d, "T14").__setitem__("portee_de_la_garantie", "conditionnelle a l’issue"))),
    Artefact("structure_inconnue", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: fam(d, "E")["tranches"][0]["loi_honnete"]["parametres"].__setitem__("structure", "ar2"))),
    Artefact("marque_a_l_ecart_fausse", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: ecart(d).__setitem__("tenue_a_l_ecart", False))),
    Artefact("n_en_texte", "P1_TYPE_INVALIDE", f_(lambda d: tem(d, "T01").__setitem__("n", "300"))),
    Artefact("valeur_vraie_en_texte", "P1_TYPE_INVALIDE", f_(lambda d: tem(d, "LA2").__setitem__("valeur_vraie", "0.4321"))),
    Artefact("k_non_entier", "P1_TYPE_INVALIDE", f_(lambda d: tem(d, "LA2").__setitem__("regle", {"type": "k_ieme_plus_grand", "k": Brut("1.5")}))),
    Artefact("supposition_accentuee", "P1_SUPPOSITION_HORS_LISTE", f_(lambda d: fam(d, "B").__setitem__("suppositions_cassees", ["forme réguliere de la queue"]))),
    Artefact("supposition_de_table", "P1_SUPPOSITION_HORS_LISTE", f_(lambda d: d["table"][0].__setitem__("supposition_cassee", "aucun"))),
    Artefact("supposition_en_double", "P1_SUPPOSITION_EN_DOUBLE", f_(lambda d: fam(d, "B").__setitem__("suppositions_cassees", [fab.S_QUEUE, fab.S_QUEUE]))),
    Artefact("loi_inconnue", "P1_LOI_HORS_GRAMMAIRE", f_(lambda d: fam(d, "A")["tranches"][0].__setitem__("loi_honnete", {"type": "pareto", "parametres": {"alpha": Brut("2.0")}}))),
    Artefact("melange_boiteux", "P1_LOI_HORS_GRAMMAIRE", f_(melange_boiteux)),
    Artefact("couple_a_trois_marges", "P1_LOI_HORS_GRAMMAIRE", f_(couple_a_trois_marges)),
    Artefact("autre_sans_definition", "P1_DEFINITION_MANQUANTE", f_(loi_autre_sans_definition)),
    Artefact("regle_inconnue", "P1_REGLE_HORS_GRAMMAIRE", f_(lambda d: tem(d, "LA2").__setitem__("regle", {"type": "seuil_adaptatif"}))),
    Artefact("signal_nul_sur_m", "P1_SIGNAL_INCOHERENT", f_(lambda d: tem(d, "LM1").__setitem__("signal", None))),
    Artefact("signal_hors_m", "P1_SIGNAL_INCOHERENT", f_(lambda d: tem(d, "T01").__setitem__("signal", "valeur"))),
    Artefact("valeurs_de_plus_t01", "P1_VALEURS_DE_PLUS_NON_PERMISES", f_(lambda d: tem(d, "T01").__setitem__("valeurs_de_plus", {"a": Brut("0.5000")}))),
    Artefact("valeurs_de_plus_texte", "P1_VALEURS_DE_PLUS_NON_NUMERIQUES", f_(lambda d: tem(d, "T05").__setitem__("valeurs_de_plus", {"a": "x"}))),
    Artefact("identifiant_de_famille", "P1_IDENTIFIANT_DE_FAMILLE", f_(lambda d: ecart(d).__setitem__("id", "KK"))),
    Artefact("p_echec_sur_a", "P1_P_ECHEC_HORS_C_ET_I", f_(lambda d: fam(d, "A").__setitem__("p_echec", Brut("0.0500")))),
    Artefact("p_echec_a_l_ecart", "P1_P_ECHEC_HORS_C_ET_I", f_(lambda d: ecart(d).__setitem__("p_echec", Brut("0.0500")))),
    Artefact("deux_tranches", "P1_TRANCHES_PAS_TROIS", f_(lambda d: fam(d, "A")["tranches"].pop())),
    Artefact("deux_decalages", "P1_DECALAGES_PAS_TROIS", f_(lambda d: fam(d, "A")["saboteur"]["decalages"].pop())),
    Artefact("deux_populations", "P1_POPULATIONS_PAS_TROIS", f_(lambda d: d["monde_M"]["populations"].pop())),
    Artefact("budget_hors_liste", "P1_BUDGET_HORS_LISTE", f_(lambda d: d["monde_M"].__setitem__("budget_b_propose", Brut("0.15")))),
    Artefact("budget_en_pourcent", "P1_BUDGET_HORS_LISTE", f_(lambda d: d["monde_M"].__setitem__("budget_b_propose", 5))),
    Artefact("deux_objets_temoins", "P1_A_L_ECART_OBJET_TEMOINS_EN_DOUBLE", f_(deux_objets_temoins)),
    # ---- point 2, complétude ----
    Artefact("temoin_en_double", "P2_IDENTIFIANT_DE_TEMOIN_EN_DOUBLE", f_(lambda d: d["temoins"].append(copy.deepcopy(tem(d, "LB1"))))),
    Artefact("t05_absent", "P2_TEMOIN_IMPOSE_ABSENT", f_(lambda d: sans_temoin(d, "T05") and None)),
    Artefact("t05_a_l_ecart", "P2_TEMOIN_IMPOSE_ABSENT", f_(t05_a_l_ecart)),
    Artefact("famille_en_double", "P2_IDENTIFIANT_DE_FAMILLE_EN_DOUBLE", f_(famille_b_en_double)),
    Artefact("famille_nommee_m", "P2_IDENTIFIANT_DE_FAMILLE_RESERVE", f_(famille_m)),
    Artefact("famille_g_absente", "P2_FAMILLE_IMPOSEE_ABSENTE", f_(retirer_g)),
    Artefact("famille_g_a_l_ecart", "P2_FAMILLE_IMPOSEE_A_L_ECART", f_(deplacer_g_a_l_ecart),
             attendus={"P2_FAMILLE_IMPOSEE_A_L_ECART", "P2_FAMILLE_IMPOSEE_ABSENTE"}),
    Artefact("p_echec_de_c_nul", "P2_P_ECHEC_ABSENT", f_(lambda d: fam(d, "C").__setitem__("p_echec", None))),
    Artefact("aucune_famille_a_l_ecart", "P2_NOMBRE_DE_FAMILLES_A_L_ECART", f_(vider_a_l_ecart)),
    Artefact("trois_familles_a_l_ecart", "P2_NOMBRE_DE_FAMILLES_A_L_ECART", f_(trois_a_l_ecart)),
    Artefact("aucun_de_marge", "P2_AUCUN_TEMOIN_DE_MARGE", f_(aucun_de_marge)),
    Artefact("temoin_sur_monde_z", "P2_TEMOIN_RATTACHE_A_UN_MONDE_ABSENT", f_(temoin_vers_z)),
    Artefact("temoin_a_l_ecart_sur_a", "P2_TEMOIN_RATTACHE_A_UN_MONDE_ABSENT", f_(lambda d: ecart(d)["temoins"][0].__setitem__("monde", "A"))),
    # ---- écarts : présents sans vérité exacte ou sans leurs deux témoins ----
    Artefact("verite_approchee_e", "E_VERITE_NON_EXACTE", f_(lambda d: fam(d, "E")["verite"].__setitem__("mode", "approchee")), monde="E"),
    Artefact("verite_nulle_g", "E_VERITE_NON_EXACTE", f_(lambda d: fam(d, "G").__setitem__("verite", None)), monde="G"),
    Artefact("verite_approchee_s", "E_VERITE_NON_EXACTE", f_(lambda d: d["monde_S"]["verite"].__setitem__("mode", "approchee")), monde="S"),
    Artefact("verite_approchee_a_l_ecart", "E_VERITE_NON_EXACTE", f_(lambda d: ecart(d)["verite"].__setitem__("mode", "approchee")), monde="a_l_ecart[0]"),
    Artefact("b_sans_doit_mourir", "E_SANS_TEMOIN_DOIT_MOURIR", f_(lambda d: sans_temoin(d, "LB1") and None), monde="B"),
    Artefact("m_sans_doit_mourir", "E_SANS_TEMOIN_DOIT_MOURIR", f_(lambda d: sans_temoin(d, "LM1") and None), monde="M"),
    Artefact("d_sans_doit_tenir", "E_SANS_TEMOIN_DOIT_TENIR", f_(lambda d: sans_temoin(d, "LD2") and None), monde="D"),
    Artefact("a_l_ecart_sans_doit_tenir", "E_SANS_TEMOIN_DOIT_TENIR", f_(retirer_temoin_a_l_ecart("LK2")), monde="a_l_ecart[0]"),
    # ---- point 3, cohérence ----
    Artefact("table_monde_z", "P3_TABLE_MONDE_INCONNU", f_(lambda d: d["table"].append({"monde": "Z", "supposition_cassee": "aucune"}))),
    Artefact("table_monde_m", "P3_TABLE_MONDE_INCONNU", f_(lambda d: d["table"].append({"monde": "M", "supposition_cassee": "aucune"}))),
    Artefact("table_ligne_en_double", "P3_TABLE_LIGNE_EN_DOUBLE", f_(lambda d: d["table"].append(dict(d["table"][1])))),
    Artefact("table_sans_b", "P3_TABLE_NE_REDIT_PAS", f_(lambda d: d.__setitem__("table", [r for r in d["table"] if r["monde"] != "B"]))),
    Artefact("table_sans_s", "P3_TABLE_NE_REDIT_PAS", f_(lambda d: d.__setitem__("table", [r for r in d["table"] if r["monde"] != "S"]))),
    Artefact("table_a_en_trop", "P3_TABLE_NE_REDIT_PAS", f_(lambda d: d["table"].append({"monde": "A", "supposition_cassee": fab.S_QUEUE}))),
    Artefact("jumeau_nul", "P3_JUMEAU_SAIN_ABSENT", f_(lambda d: fam(d, "B").__setitem__("jumeau_sain", None))),
    Artefact("jumeau_vide", "P3_JUMEAU_SAIN_ABSENT", f_(lambda d: fam(d, "B").__setitem__("jumeau_sain", {}))),
    Artefact("hors_table_qui_casse", "P3_HORS_TABLE_CASSE_UNE_DES_SEPT", f_(lambda d: fam(d, "B").__setitem__("hors_table", True))),
    Artefact("interface_loi_normale", "P3_INTERFACE_PORTE_UNE_LOI", f_(interface_plus("entree", " ; la loi est normale"))),
    Artefact("interface_arrondis", "P3_INTERFACE_PORTE_UNE_LOI", f_(interface_plus("entree", " ; scores arrondis"))),
    Artefact("interface_sigma", "P3_INTERFACE_PORTE_UN_PARAMETRE", f_(interface_plus("sens_du_score", ", sigma vaut un"))),
    Artefact("interface_famille_b", "P3_INTERFACE_NOMME_UNE_FAMILLE", f_(interface_plus("entree", " (famille B)"))),
    Artefact("interface_nom_de_b", "P3_INTERFACE_NOMME_UNE_FAMILLE", f_(interface_plus("entree", " ; queue lourde factice"))),
    Artefact("a_l_ecart_dans_remarque", "P3_FAMILLE_A_L_ECART_NOMMEE_HORS_DE_SON_BLOC", f_(remarque("la famille K est tenue a l'ecart"))),
    Artefact("nom_a_l_ecart_dans_remarque", "P3_FAMILLE_A_L_ECART_NOMMEE_HORS_DE_SON_BLOC", f_(remarque("voir la Famille d'essai retirée du regard"))),
    Artefact("temoin_a_l_ecart_en_tete", "P3_FAMILLE_A_L_ECART_NOMMEE_HORS_DE_SON_BLOC", f_(lk1_en_tete)),
    Artefact("cle_libre_a_l_ecart", "P3_FAMILLE_A_L_ECART_NOMMEE_HORS_DE_SON_BLOC", f_(lambda d: fam(d, "B")["jumeau_sain"].__setitem__("K", Brut("1.0")))),
    # ---- point 5, motifs ----
    Artefact("nom_de_modele", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", f_(remarque("produit par modele-fictif-alpha"))),
    Artefact("nom_de_modele_echappe", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", lambda: texte(sain()).replace("Sortie factice", "Sortie mod\\u0065le-fictif-beta", 1)),
    Artefact("nom_de_fournisseur_en_cle", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", f_(lambda d: fam(d, "B")["jumeau_sain"].__setitem__("fournisseur-fictif-x", Brut("1.0")))),
    Artefact("nom_de_modele_sortie_illisible", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", lambda: "modele-fictif-gamma\n" + texte(sain()), sortie=2),
    Artefact("cle_a_prefixe", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque("cle " + CLE_SK))),
    Artefact("longue_chaine_melangee", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque("jeton " + CHAINE_MELANGEE))),
    Artefact("bloc_de_cle_privee", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BLOC_PRIVE))),
    # ---- observations (ne décident de rien) ----
    Artefact("deux_decimales", "O_PROBABILITE_A_MOINS_DE_QUATRE_DECIMALES", f_(lambda d: tem(d, "T01").__setitem__("valeur_vraie", Brut("0.43")))),
    Artefact("poids_mal_sommes", "O_POIDS_DU_MELANGE_NE_SOMMENT_PAS_A_UN", f_(lambda d: fam(d, "C")["tranches"][0]["loi_honnete"]["parametres"].__setitem__("poids", [Brut("0.9"), Brut("0.05")]))),
    Artefact("trente_et_un_mots", "O_PLUS_DE_TRENTE_MOTS", f_(lambda d: fam(d, "A").__setitem__("raison", " ".join(["mot"] * 31)))),
    Artefact("limite_sur_deux_lignes", "O_LIMITE_MONDE_M_SUR_PLUSIEURS_LIGNES", f_(lambda d: d["monde_M"].__setitem__("limite_monde_M", "ligne un\nligne deux"))),
    Artefact("onze_remarques", "O_PLUS_DE_DIX_REMARQUES", f_(lambda d: d["remarques"].extend(["remarque factice"] * 10))),
    Artefact("t01_k4", "O_ECART_A_LA_TABLE_DES_TEMOINS_IMPOSES", f_(lambda d: tem(d, "T01").__setitem__("regle", {"type": "k_ieme_plus_grand", "k": 4}))),
    Artefact("t05_sans_valeurs_de_plus", "O_VALEURS_DE_PLUS_ABSENTES", f_(lambda d: tem(d, "T05").pop("valeurs_de_plus"))),
    Artefact("sorte_et_issue", "O_SORTE_ET_ISSUE_DISCORDANTES", f_(lambda d: tem(d, "LA2").__setitem__("issue_attendue", "morte_invalide"))),
    Artefact("sans_gain_libre", "O_MORTE_SANS_GAIN_HORS_T05_T07", f_(lambda d: tem(d, "LA1").__setitem__("issue_attendue", "morte_sans_gain"))),
    Artefact("plus_de_vingt_huit", "O_PLUS_DE_VINGT_HUIT_TEMOINS", sain),
    Artefact("trois_familles_libres", "O_FAMILLES_LIBRES_AU_DELA_DE_DEUX", f_(familles_libres_trois)),
    Artefact("m_sans_conditionnel", "O_MONDE_M_SANS_TEMOIN_CONDITIONNEL", f_(lambda d: tem(d, "LM2").__setitem__("portee_de_la_garantie", fab.TOUS))),
    Artefact("p_echec_differents", "O_P_ECHEC_DIFFERENT_ENTRE_C_ET_I", f_(lambda d: fam(d, "I").__setitem__("p_echec", Brut("0.0600")))),
    Artefact("p_echec_hors_intervalle", "O_P_ECHEC_HORS_DE_L_INTERVALLE", f_(lambda d: [fam(d, x).__setitem__("p_echec", Brut("0.2000")) for x in "CI"] and None)),
    Artefact("imposee_fausse", "O_IMPOSEE_INCOHERENTE", f_(lambda d: fam(d, "A").__setitem__("imposee", False))),
    Artefact("jumeau_sur_saine", "O_JUMEAU_SAIN_SUR_FAMILLE_SAINE", f_(lambda d: fam(d, "A").__setitem__("jumeau_sain", {"mu": Brut("0.0")}))),
    Artefact("mention_dans_non_calcule", "O_MENTION_POSSIBLE_DANS_NON_CALCULE", f_(lambda d: d["non_calcule"].append("famille E : vérité approchée seulement"))),
]


@pytest.mark.parametrize("a", ARTEFACTS, ids=[a.nom for a in ARTEFACTS])
def test_artefact(a, tmp_path):
    retour, rap = jouer(a.fabrique(), tmp_path)
    controler(a, retour, rap)


# ---------------------------------------------------------------------------
# Cas sain et propriétés d'ensemble
# ---------------------------------------------------------------------------

def test_fichier_sain_egal_au_fabricant():
    assert SORTIE_SAINE.read_text(encoding="utf-8") == texte(sain())


def test_cas_sain(tmp_path):
    retour, rap = jouer(SORTIE_SAINE.read_bytes(), tmp_path)
    assert retour == 0 and rap["code_de_sortie"] == 0
    assert rap["verdict_d_ensemble"] == "lisible"
    assert all(p["verdict"] == "tenu" and not p["fautes"] for p in rap["points"].values())
    assert rap["ecartes"] == [] and rap["hors_table"] == []
    assert codes_observes(rap) == OBSERVATIONS_SAINES
    assert rap["forme_du_bloc_a_l_ecart"] == "temoins_dans_chaque_famille"
    d = sain()
    assert rap["lignes_de_table_des_familles_a_l_ecart"] == [i for i, r in enumerate(d["table"]) if r["monde"] == "K"]
    assert rap["sortie_auteur"]["caracteres"] <= 40000


def test_famille_sans_verite_exacte_ecartee_sans_rendre_illisible(tmp_path):
    d = sain()
    fam(d, "E")["verite"]["mode"] = "approchee"
    retour, rap = jouer(d, tmp_path)
    assert retour == 0 and rap["verdict_d_ensemble"] == "lisible"
    assert rap["points"]["2_completude"]["verdict"] == "tenu"
    assert rap["ecartes"] == [{"monde": "E", "raisons": ["E_VERITE_NON_EXACTE"]}]


def test_famille_libre_sans_temoins_ecartee_sans_rendre_illisible(tmp_path):
    d = sain()
    g = copie_de_famille(fam(d, "A"), "J")
    d["familles"].append(g)
    d["table"] += lignes_de_table(g)
    retour, rap = jouer(d, tmp_path)
    assert retour == 0 and rap["verdict_d_ensemble"] == "lisible"
    assert rap["ecartes"] == [{"monde": "J", "raisons": ["E_SANS_TEMOIN_DOIT_MOURIR", "E_SANS_TEMOIN_DOIT_TENIR"]}]


def test_point_1_manque_laisse_2_et_3_non_juges(tmp_path):
    retour, rap = jouer("Voici :\n" + texte(sain()), tmp_path)
    assert retour == 2 and rap["verdict_d_ensemble"] == "illisible"
    assert rap["points"]["2_completude"]["verdict"] == "non_juge"
    assert rap["points"]["3_coherence"]["verdict"] == "non_juge"
    assert rap["points"]["5_motifs"]["verdict"] == "tenu"


def test_point_2_manque_laisse_3_juge(tmp_path):
    d = sans_temoin(sain(), "T05")
    d["table"].append({"monde": "Z", "supposition_cassee": "aucune"})
    retour, rap = jouer(d, tmp_path)
    assert retour == 2
    assert codes(rap, "3") == {"P3_TABLE_MONDE_INCONNU"}


def test_formes_admises(tmp_path):
    """Loi `autre` avec sa définition, couple gaussien sous ses deux écritures,
    témoins tenus à l'écart dans un objet à part, marque `tenue_a_l_ecart`."""
    d = sain()
    fam(d, "B")["tranches"][0]["loi_honnete"] = {"type": "autre", "parametres": {"definition": "définition factice complète"}}
    fam(d, "B")["tranches"][1]["loi_honnete"] = {"type": "autre", "parametres": {}, "definition": "définition factice"}
    fam(d, "A")["tranches"][0]["loi_honnete"] = {
        "type": "couple", "parametres": {"marges": [fab.normale(), fab.normale()], "dependance": "gaussienne", "rho": Brut("0.3")}}
    fam(d, "A")["tranches"][1]["loi_honnete"] = {
        "type": "couple", "parametres": {"marges": [fab.normale(), fab.normale()], "dependance": {"type": "gaussienne", "rho": Brut("0.3")}}}
    k = ecart(d)
    k["tenue_a_l_ecart"] = True
    d["a_l_ecart"].append({"temoins": k.pop("temoins")})
    retour, rap = jouer(d, tmp_path)
    assert retour == 0, rap["points"]
    assert rap["a_lire_par_une_personne_type_autre"] == ["B"]
    assert rap["forme_du_bloc_a_l_ecart"] == "objet_temoins_a_part"


def test_rapport_ne_recopie_ni_texte_ni_famille_a_l_ecart(tmp_path):
    d = sain()
    d["remarques"] += ["produit par modele-fictif-alpha", "cle " + CLE_SK, "la famille K est tenue a l'ecart"]
    fam(d, "B")["jumeau_sain"]["fournisseur-fictif-x"] = Brut("1.0")
    retour, rap = jouer(d, tmp_path)
    brut = (tmp_path / "rapport.json").read_text(encoding="utf-8")
    assert retour == 1
    for interdit in ("modele-fictif", "fournisseur-fictif", "sk-", "factice", "retiree", "tenue a l'ecart"):
        assert interdit not in brut
    assert not re.search(r"(?<![A-Za-z0-9_])K(?![A-Za-z0-9_])", brut)


def test_sortie_saine_par_python3_systeme(tmp_path):
    """La commande du mandat : python3 -I -B PROGRAMME SORTIE RAPPORT (motifs par défaut)."""
    rapport = tmp_path / "rapport.json"
    r = subprocess.run(["python3", "-I", "-B", str(PROGRAMME), str(SORTIE_SAINE), str(rapport)],
                       capture_output=True, text=True, timeout=120)
    assert r.returncode == 0
    assert json.loads(rapport.read_text(encoding="utf-8"))["motifs"]["nombre"] == 3


# ---------------------------------------------------------------------------
# Erreurs d'usage : code 3, aucun rapport, aucun repli silencieux
# ---------------------------------------------------------------------------

def lancer(*args):
    return subprocess.run([sys.executable, "-I", "-B", str(PROGRAMME)] + [str(a) for a in args],
                          capture_output=True, text=True, timeout=120)


def test_erreur_sortie_absente(tmp_path):
    r = lancer(tmp_path / "absente.json", tmp_path / "r.json", "--motifs", MOTIFS)
    assert r.returncode == 3 and not (tmp_path / "r.json").exists()


def test_erreur_rapport_existant_jamais_ecrase(tmp_path):
    (tmp_path / "r.json").write_text("ancien", encoding="utf-8")
    r = lancer(SORTIE_SAINE, tmp_path / "r.json", "--motifs", MOTIFS)
    assert r.returncode == 3 and (tmp_path / "r.json").read_text(encoding="utf-8") == "ancien"


def test_erreur_motifs_absents(tmp_path):
    r = lancer(SORTIE_SAINE, tmp_path / "r.json", "--motifs", tmp_path / "absent.txt")
    assert r.returncode == 3 and not (tmp_path / "r.json").exists()


def test_erreur_motifs_vides(tmp_path):
    vide = tmp_path / "vide.txt"
    vide.write_text("# rien\n\n", encoding="utf-8")
    r = lancer(SORTIE_SAINE, tmp_path / "r.json", "--motifs", vide)
    assert r.returncode == 3 and not (tmp_path / "r.json").exists()


def test_erreur_motif_invalide(tmp_path):
    faux = tmp_path / "faux.txt"
    faux.write_text("modele-(\n", encoding="utf-8")
    r = lancer(SORTIE_SAINE, tmp_path / "r.json", "--motifs", faux)
    assert r.returncode == 3 and not (tmp_path / "r.json").exists()


def test_erreur_arguments(tmp_path):
    assert lancer(SORTIE_SAINE).returncode == 3
    assert lancer(SORTIE_SAINE, tmp_path / "a.json", tmp_path / "b.json").returncode == 3
    assert lancer(SORTIE_SAINE, tmp_path / "a.json", "--motifs", MOTIFS, "--motifs", MOTIFS).returncode == 3
    assert not (tmp_path / "a.json").exists()


# ---------------------------------------------------------------------------
# Couverture et mutations
# ---------------------------------------------------------------------------

RE_GARDE = re.compile(r'\.(rapporte|ecarte|observe)\("([A-Z0-9_]+)"')
NEUTRE = {"rapporte": "neutre", "ecarte": "neutre_ecart", "observe": "neutre_observation"}


def gardes_du_programme():
    return sorted({(m.group(1), m.group(2)) for m in RE_GARDE.finditer(PROGRAMME.read_text(encoding="utf-8"))})


def test_chaque_garde_a_son_artefact_et_reciproquement():
    dans_le_programme = {code for _, code in gardes_du_programme()}
    dans_les_essais = {a.code for a in ARTEFACTS}
    assert dans_le_programme == dans_les_essais


@pytest.mark.parametrize("methode,code", gardes_du_programme(), ids=[c for _, c in gardes_du_programme()])
def test_mutation(methode, code, tmp_path):
    source = PROGRAMME.read_text(encoding="utf-8")
    ancien = '.%s("%s"' % (methode, code)
    assert ancien in source
    mutant = tmp_path / "mutant.py"
    mutant.write_text(source.replace(ancien, '.%s("%s"' % (NEUTRE[methode], code)), encoding="utf-8")
    concernes = [a for a in ARTEFACTS if a.code == code]
    assert concernes
    for a in concernes:
        retour, rap = jouer(a.fabrique(), tmp_path / a.nom, programme=mutant)
        with pytest.raises(AssertionError):
            controler(a, retour, rap)
