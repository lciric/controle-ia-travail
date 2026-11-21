# -*- coding: utf-8 -*-
"""Essais du programme de vérification de la sortie de l'auteur des mondes — v5.

v5 : ceux de la v4 (rejoués sur la sortie factice v5), et ceux du contrôle par l'aire :
- les trois issues (conforme, unité brute constatée, non lisible), chacune avec ses essais
  et sa mutation ;
- l'écart de plus de 0,001 compté et nommé ;
- le saboteur non converti hors de l'issue conforme ;
- l'exactitude du moteur d'aire contre des formes fermées (normale, Laplace, mélange de
  normales, Cauchy).

v4 : ceux de la v3, tous rejoués ; le compte rendu de la dérive de F porte tout ce que le
contrôle demande, dit qui le fera (R1), et signale la première tranche à 299 quand
plusieurs la contiennent (R2), avec un essai et une mutation.

v3 : ceux de la v2, tous rejoués, et ceux de D1 (plafond de témoins en faute du point 1),
D2 (dérive de F lue dans T09 par la règle de la mère, F écartée sinon), D3 (monde M non
converti) et de la tranche voisine sans boucle, chacun avec sa mutation.

Ceux de la v1, tous rejoués (cas sain, un artefact au moins par garde, erreurs
d'usage, mutation de chaque garde), et ceux de la v2 :
- chaque branche du motif de valeur de clé du lanceur v9 prise par une chaîne
  inventée, et un essai de parité qui lit les branches dans le lanceur lui-même ;
- la mutation de chaque motif de clé (le motif réécrit pour ne plus rien prendre) ;
- C1 (profondeur), C2 (vérité non exacte), C3 (budget), N2 (tirets), borne de taille,
  chacun avec ses essais et sa mutation.

Aucune chaîne d'essai ne recopie une valeur réelle. Les préfixes de clé sont composés
par concaténation (« "g" + "hp_" ») : le texte de ce fichier ne contient aucun préfixe
en clair.

Lancement : /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider \
    --basetemp=DOSSIER/essais-tmp DOSSIER/test_verifier_sortie_auteur_mondes_v4.py

Développeur du programme de vérification de la sortie des mondes, modèle O.
"""

import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

import fabriquer_sorties_factices_v5 as fab
from fabriquer_sorties_factices_v5 import Brut

ICI = Path(__file__).resolve().parent
PROGRAMME = ICI / "verifier_sortie_auteur_mondes_v5.py"
MOTIFS = ICI / "motifs-noms-refuses-essai-v1.txt"
SORTIE_SAINE = ICI / "sortie-factice-saine-v5.json"
SORTIE_UNITE_BRUTE = ICI / "sortie-factice-essai-unite-brute-v5.json"
LANCEUR = Path("/home/user/controle-ia-travail-organisme/scripts/lancer_course_auto_conception_v9.py")
EMPREINTE_LANCEUR = "1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12"
VERITE = Path("/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/"
              "dev-verite-temoins-mondes/calculer_verite_temoins_imposes_v1.py")
EMPREINTE_VERITE = "4857343c3388e5045a49dd690d661b3fb2069949691af079f3db21e2db58bf59"
BORNE = 52000          # erratum 1 du mandat v3, borne finale, mot de la mère
PLAFOND_TEMOINS = 40   # erratum 1 : imposés, libres et bloc à l'écart compris
OBSERVATIONS_SAINES = set()
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
    """`code` : un code du programme (P…, E…, O…), ou Z_LISIBLE (lisible, code 0, tout tenu
    au point 1), ou Z_CODE_3 (rien n'est jugé, aucun rapport). `motif` : le motif de clé
    qui doit prendre la chaîne (point 5)."""

    def __init__(self, nom, code, fabrique, attendus=None, sortie=None, monde=None, motif=None):
        self.nom, self.code, self.fabrique = nom, code, fabrique
        self.attendus = attendus or {code}
        self.monde, self.motif = monde, motif
        if sortie is None:
            if code.startswith(("P1", "P2")):
                sortie = 2
            elif code.startswith(("P3", "P5")):
                sortie = 1
            elif code == "Z_CODE_3":
                sortie = 3
            else:
                sortie = 0
        self.sortie = sortie


def controler(a, retour, rap):
    if a.code == "Z_CODE_3":
        assert retour == 3 and rap is None
        return
    assert rap is not None, "aucun rapport écrit"
    assert retour == a.sortie == rap["code_de_sortie"]
    if a.code == "Z_LISIBLE":
        assert rap["verdict_d_ensemble"] == "lisible"
        assert all(p["verdict"] == "tenu" for p in rap["points"].values())
        assert codes_observes(rap) == OBSERVATIONS_SAINES
        assert rap["ecartes"] == []
    elif a.code.startswith("P"):
        point = a.code[1]
        assert rap["points"][POINT[point]]["verdict"] == "manque"
        assert codes(rap, point) == a.attendus
        if a.motif:
            assert a.motif in {f.get("motif") for f in rap["points"][POINT[point]]["fautes"] if f["code"] == a.code}
    elif a.code.startswith("E"):
        assert rap["verdict_d_ensemble"] == "lisible"
        assert rap["points"]["1_forme"]["verdict"] == "tenu"
        assert rap["points"]["2_completude"]["verdict"] == "tenu"
        assert any(e["monde"] == a.monde and a.code in e["raisons"] for e in rap["ecartes"])
    else:
        assert rap["verdict_d_ensemble"] == "lisible"
        assert a.code in codes_observes(rap)


# ---------------------------------------------------------------------------
# Fabriques d'artefacts
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
        g["temoins"] = []  # v3 : sans témoins, pour rester sous le plafond de 40 (D1)
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


def libre_nomme(tid, a_l_ecart):
    """Un témoin libre qui porte l'identifiant d'un témoin imposé : une copie de LB1 en tête,
    ou le témoin LK1 du bloc à l'écart, renommé."""
    def r(d):
        if a_l_ecart:
            next(x for x in ecart(d)["temoins"] if x["id"] == "LK1")["id"] = tid
        else:
            t = copy.deepcopy(tem(d, "LB1"))
            t["id"] = tid
            d["temoins"].append(t)
    return r


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


def verite_de_e(changement):
    def r(d):
        v = fam(d, "E")["verite"]
        for cle, valeur in changement.items():
            if valeur is RETIRER:
                v.pop(cle)
            else:
                v[cle] = valeur
    return r


RETIRER = object()


def budget(valeur):
    def r(d):
        d["monde_M"]["budget_b_propose"] = valeur
    return r


def imbrication(ouvrant, fermant, profondeur):
    """Objet libre imbriqué dans le jumeau sain de B, écrit dans le texte (le sérialiseur
    récursif du fabricant n'irait pas si profond)."""
    def fabrique():
        d = sain()
        fam(d, "B")["jumeau_sain"] = {"nid": "__NID__"}
        return texte(d).replace('"__NID__"', ouvrant * profondeur + "1" + fermant * profondeur, 1)
    return fabrique


def temoins_en_plus(total):
    """Porte le nombre de témoins (en tête et bloc à l'écart) à `total` par des copies de LB1."""
    def r(d):
        compte = len(d["temoins"]) + sum(len(f.get("temoins", [])) for f in d["a_l_ecart"])
        for i in range(total - compte):
            t = copy.deepcopy(tem(d, "LB1"))
            t["id"] = "LBX%d" % i
            d["temoins"].append(t)
    return r


def temoins_a_l_ecart_en_plus(nombre):
    """Ajoute `nombre` témoins au bloc à l'écart (copies de LK1, monde K) : 39 + 2 = 41."""
    def r(d):
        for i in range(nombre):
            t = copy.deepcopy(next(x for x in ecart(d)["temoins"] if x["id"] == "LK1"))
            t["id"] = "LKX%d" % i
            ecart(d)["temoins"].append(t)
    return r


def valeurs_de_t09(valeurs):
    def r(d):
        tem(d, "T09")["valeurs_de_plus"] = {k: Brut(v) for k, v in valeurs.items()}
    return r


def decalages_de(fid, valeurs):
    def r(d):
        fam(d, fid)["saboteur"]["decalages"] = [Brut(v) for v in valeurs]
    return r


def loi_de_b(loi):
    def r(d):
        for tr in fam(d, "B")["tranches"]:
            tr["loi_honnete"] = loi
    return r


STUDENT_NU_2 = {"type": "student", "parametres": {"nu": Brut("2.0"), "mu": Brut("0.0"), "echelle": Brut("1.0")}}
BERNOULLI = {"type": "bernoulli", "parametres": {"p": Brut("0.5")}}


def a_la_taille(total):
    """Sortie saine portée à exactement `total` caractères par une remarque de « x »."""
    def fabrique():
        d = sain()
        d["remarques"].append("")
        manque = total - len(texte(d))
        assert manque > 0
        d["remarques"][-1] = "x" * manque
        t = texte(d)
        assert len(t) == total
        return t
    return fabrique


# Chaînes inventées. Les préfixes sont composés pour ne jamais paraître en clair dans ce fichier.
CLE_SK = "s" + "k-" + "Ab3x" * 6
CHAINE_MELANGEE = "Zq9" * 12
BLOC_PRIVE = "-----BEGIN " + "PRIVATE " + "KEY-----"
# Une chaîne par branche du lanceur v9, à la longueur minimale qu'il exige, collée à des lettres
# (le lanceur ne demande aucune frontière de mot).
BRANCHE_SK_SEGMENT = "zz" + "s" + "k-" + "qrs" + "-" + "Z"      # segment inventé, quel qu'il soit
BRANCHE_SK_20 = "zz" + "s" + "k-" + "a" * 20
BRANCHE_GH_20 = "zz" + "g" + "hp_" + "b" * 20
BRANCHE_HF_20 = "zz" + "h" + "f_" + "c" * 20
BRANCHE_A_K_12 = "zz" + "AK" + "IA" + "Q" * 12 + "zz"
BRANCHE_AIZA_20 = "zz" + "AI" + "za" + "d" * 20
BRANCHE_PORTEUR_16 = "zz" + "Bea" + "rer " + "e" * 16
CHAINE_PAT = "githu" + "b_pat_" + "f" * 20
CHAINE_XOX = "xo" + "xb-" + "g" * 10
CHAINE_JETON = "e" + "yJ" + "h" * 8 + "." + "i" * 8 + "." + "j" * 8
CHAINE_AFFECTATION = "mot_de" + "_passe = " + "k" * 8

ARTEFACTS = [
    # ---- point 1, forme ----
    Artefact("taille", "P1_TAILLE", f_(remarque("x" * 40100))),
    Artefact("taille_juste_au_dessus", "P1_TAILLE", a_la_taille(BORNE + 1)),
    Artefact("taille_a_la_borne", "Z_LISIBLE", a_la_taille(BORNE)),
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
    Artefact("cle_en_trop_verite_non_exacte", "P1_CLE_EN_TROP", f_(verite_de_e({"mode": "approchee", "commentaire": "x"}))),
    Artefact("cle_manquante_temoin", "P1_CLE_MANQUANTE", f_(lambda d: tem(d, "T01").pop("formule"))),
    Artefact("cle_manquante_premier_niveau", "P1_CLE_MANQUANTE", f_(lambda d: d.pop("remarques"))),
    Artefact("verite_exacte_sans_expression", "P1_CLE_MANQUANTE", f_(verite_de_e({"expression": RETIRER}))),
    Artefact("ordre_des_cles", "P1_ORDRE_DES_CLES", f_(ordre_inverse)),
    Artefact("version_forme", "P1_VERSION_FORME", f_(lambda d: d.__setitem__("version_forme", "mondes-plantes-seuil-et-moniteurs-v2"))),
    Artefact("sorte_inconnue", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: tem(d, "T01").__setitem__("sorte", "doit_peut_etre"))),
    Artefact("apostrophe_typographique", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: tem(d, "T14").__setitem__("portee_de_la_garantie", "conditionnelle a l’issue"))),
    Artefact("structure_inconnue", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: fam(d, "E")["tranches"][0]["loi_honnete"]["parametres"].__setitem__("structure", "ar2"))),
    Artefact("marque_a_l_ecart_fausse", "P1_CHAMP_FERME_INVALIDE", f_(lambda d: ecart(d).__setitem__("tenue_a_l_ecart", False))),
    Artefact("n_en_texte", "P1_TYPE_INVALIDE", f_(lambda d: tem(d, "T01").__setitem__("n", "300"))),
    Artefact("valeur_vraie_en_texte", "P1_TYPE_INVALIDE", f_(lambda d: tem(d, "LA2").__setitem__("valeur_vraie", "0.4321"))),
    Artefact("valeur_vraie_nulle", "P1_TYPE_INVALIDE", f_(lambda d: tem(d, "LA2").__setitem__("valeur_vraie", None))),
    Artefact("k_non_entier", "P1_TYPE_INVALIDE", f_(lambda d: tem(d, "LA2").__setitem__("regle", {"type": "k_ieme_plus_grand", "k": Brut("1.5")}))),
    Artefact("verite_en_liste", "P1_TYPE_INVALIDE", f_(lambda d: fam(d, "E").__setitem__("verite", ["exacte"]))),
    Artefact("verite_exacte_expression_nombre", "P1_TYPE_INVALIDE", f_(verite_de_e({"expression": 3}))),
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
    Artefact("budget_hors_liste", "P1_BUDGET_HORS_LISTE", f_(budget(Brut("0.15")))),
    Artefact("budget_sept_pour_cent", "P1_BUDGET_HORS_LISTE", f_(budget(7))),
    Artefact("budget_chaine_hors_liste", "P1_BUDGET_HORS_LISTE", f_(budget("7 %"))),
    Artefact("budget_chaine_sans_pour_cent", "P1_BUDGET_HORS_LISTE", f_(budget("0.05"))),
    Artefact("deux_objets_temoins", "P1_A_L_ECART_OBJET_TEMOINS_EN_DOUBLE", f_(deux_objets_temoins)),
    # ---- point 2, complétude ----
    Artefact("temoin_en_double", "P2_IDENTIFIANT_DE_TEMOIN_EN_DOUBLE", f_(lambda d: d["temoins"].append(copy.deepcopy(tem(d, "LB1"))))),
    Artefact("t05_absent", "P2_TEMOIN_IMPOSE_ABSENT", f_(lambda d: sans_temoin(d, "T05"))),
    Artefact("t05_a_l_ecart", "P2_TEMOIN_IMPOSE_ABSENT", f_(t05_a_l_ecart),
             attendus={"P2_TEMOIN_IMPOSE_ABSENT", "P2_IDENTIFIANT_IMPOSE_RESERVE"}),
    Artefact("libre_nomme_t05_en_tete", "P2_IDENTIFIANT_IMPOSE_RESERVE", f_(libre_nomme("T05", False)),
             attendus={"P2_IDENTIFIANT_IMPOSE_RESERVE", "P2_IDENTIFIANT_DE_TEMOIN_EN_DOUBLE"}),
    Artefact("libre_nomme_t07_a_l_ecart", "P2_IDENTIFIANT_IMPOSE_RESERVE", f_(libre_nomme("T07", True)),
             attendus={"P2_IDENTIFIANT_IMPOSE_RESERVE", "P2_IDENTIFIANT_DE_TEMOIN_EN_DOUBLE"}),
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
    Artefact("verite_approchee_e", "E_VERITE_NON_EXACTE", f_(verite_de_e({"mode": "approchee"})), monde="E"),
    Artefact("verite_mode_nul", "E_VERITE_NON_EXACTE", f_(verite_de_e({"mode": None})), monde="E"),
    Artefact("verite_mode_vide", "E_VERITE_NON_EXACTE", f_(verite_de_e({"mode": ""})), monde="E"),
    Artefact("verite_sans_mode", "E_VERITE_NON_EXACTE", f_(verite_de_e({"mode": RETIRER})), monde="E"),
    Artefact("verite_non_exacte_sans_expression", "E_VERITE_NON_EXACTE", f_(verite_de_e({"mode": "approchee", "expression": RETIRER})), monde="E"),
    Artefact("verite_nulle_g", "E_VERITE_NON_EXACTE", f_(lambda d: fam(d, "G").__setitem__("verite", None)), monde="G"),
    Artefact("verite_approchee_s", "E_VERITE_NON_EXACTE", f_(lambda d: d["monde_S"]["verite"].__setitem__("mode", "approchee")), monde="S"),
    Artefact("verite_approchee_a_l_ecart", "E_VERITE_NON_EXACTE", f_(lambda d: ecart(d)["verite"].__setitem__("mode", "approchee")), monde="a_l_ecart[0]"),
    Artefact("b_sans_doit_mourir", "E_SANS_TEMOIN_DOIT_MOURIR", f_(lambda d: sans_temoin(d, "LB1")), monde="B"),
    Artefact("m_sans_doit_mourir", "E_SANS_TEMOIN_DOIT_MOURIR", f_(lambda d: sans_temoin(d, "LM1")), monde="M"),
    Artefact("d_sans_doit_tenir", "E_SANS_TEMOIN_DOIT_TENIR", f_(lambda d: sans_temoin(d, "LD2")), monde="D"),
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
    # ---- point 5, motifs : noms ----
    Artefact("nom_de_modele", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", f_(remarque("produit par modele-fictif-alpha"))),
    Artefact("nom_de_modele_echappe", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", lambda: texte(sain()).replace("Sortie factice", "Sortie mod\\u0065le-fictif-beta", 1)),
    Artefact("nom_de_fournisseur_en_cle", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", f_(lambda d: fam(d, "B")["jumeau_sain"].__setitem__("fournisseur-fictif-x", Brut("1.0")))),
    Artefact("nom_de_modele_sortie_illisible", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", lambda: "modele-fictif-gamma\n" + texte(sain()), sortie=2),
    Artefact("nom_de_modele_trait_insecable", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", f_(remarque("produit par modele‑fictif‑delta"))),
    Artefact("nom_de_modele_tiret_cadratin", "P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR", f_(remarque("produit par modele—fictif—epsilon"))),
    # ---- point 5, motifs : chaînes en forme de clé (v1) ----
    Artefact("cle_a_prefixe", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque("cle " + CLE_SK)), motif="prefixe_sk"),
    Artefact("longue_chaine_melangee", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque("jeton " + CHAINE_MELANGEE)), motif="longue_chaine_melangee"),
    Artefact("bloc_de_cle_privee", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BLOC_PRIVE)), motif="bloc_de_cle_privee"),
    # ---- point 5 : les sept branches du lanceur v9, une chaîne inventée chacune (v2) ----
    Artefact("lanceur_sk_segment", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BRANCHE_SK_SEGMENT)), motif="prefixe_sk_segment"),
    Artefact("lanceur_sk_20", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BRANCHE_SK_20)), motif="prefixe_sk"),
    Artefact("lanceur_gh_20", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BRANCHE_GH_20)), motif="prefixe_gh"),
    Artefact("lanceur_h_f_20", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BRANCHE_HF_20)), motif="prefixe_hf"),
    Artefact("lanceur_a_k_12", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BRANCHE_A_K_12)), motif="prefixe_akia"),
    Artefact("lanceur_aiza_20", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BRANCHE_AIZA_20)), motif="prefixe_aiza"),
    Artefact("lanceur_porteur_16", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(BRANCHE_PORTEUR_16)), motif="porteur"),
    # ---- point 5 : les autres motifs de clé, chacun sa chaîne (v2) ----
    Artefact("cle_pat", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(CHAINE_PAT)), motif="prefixe_pat"),
    Artefact("cle_xox", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(CHAINE_XOX)), motif="prefixe_xox"),
    Artefact("cle_jeton_trois_segments", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(CHAINE_JETON)), motif="jeton_a_trois_segments"),
    Artefact("cle_affectation", "P5_CHAINE_DE_FORME_DE_CLE", f_(remarque(CHAINE_AFFECTATION)), motif="affectation_de_secret"),
    Artefact("cle_dans_une_cle_libre", "P5_CHAINE_DE_FORME_DE_CLE", f_(lambda d: fam(d, "B")["jumeau_sain"].__setitem__(BRANCHE_HF_20, Brut("1.0"))), motif="prefixe_hf"),
    # ---- C1 : profondeur ----
    Artefact("imbrication_995", "Z_LISIBLE", imbrication('{"a": ', "}", 995)),
    Artefact("imbrication_trop_profonde", "Z_CODE_3", imbrication("[", "]", 100000)),
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
    Artefact("temoins_au_dela_du_plafond", "P1_TEMOINS_AU_DELA_DU_PLAFOND", f_(temoins_en_plus(PLAFOND_TEMOINS + 1))),
    Artefact("plafond_par_le_bloc_a_l_ecart", "P1_TEMOINS_AU_DELA_DU_PLAFOND", f_(temoins_a_l_ecart_en_plus(2))),
    # ---- D2 : dérive de F lue dans T09 (règle de la mère), F écartée sinon ----
    Artefact("derive_t09_sans_valeurs_de_plus", "E_DERIVE_SANS_DECALAGE_LISIBLE", f_(lambda d: tem(d, "T09").pop("valeurs_de_plus")), monde="F"),
    Artefact("derive_t09_deux_cles_libres", "E_DERIVE_SANS_DECALAGE_LISIBLE", f_(valeurs_de_t09({"note_a": "1.0", "note_b": "2.0"})), monde="F"),
    Artefact("derive_t09_deux_cles_nommees", "E_DERIVE_SANS_DECALAGE_LISIBLE", f_(valeurs_de_t09({"decalage_a": "0.5", "derive_b": "0.6"})), monde="F"),
    Artefact("derive_t09_seule_cle_exclue", "E_DERIVE_SANS_DECALAGE_LISIBLE", f_(valeurs_de_t09({"couverture_qui_reste": "0.4321"})), monde="F"),
    Artefact("derive_t09_cle_nommee_exclue_par_a", "E_DERIVE_SANS_DECALAGE_LISIBLE",
             f_(valeurs_de_t09({"taux_de_derive": "0.0300", "note_a": "1.0", "note_b": "2.0"})), monde="F"),
    Artefact("derive_t09_seule_cle_libre", "Z_LISIBLE", f_(valeurs_de_t09({"couverture_x": "0.4321", "delta": "0.5"}))),
    Artefact("derive_t09_taux_exclu", "Z_LISIBLE", f_(valeurs_de_t09({"taux_triple": "0.0300", "probabilite_y": "0.4321", "ecart": "0.5"}))),
    Artefact("derive_t09_cle_nommee_parmi_libres", "Z_LISIBLE", f_(valeurs_de_t09({"note_libre": "1.0", "decalage_x": "0.5"}))),
    Artefact("derive_t09_noms_accentues", "Z_LISIBLE", f_(valeurs_de_t09({"Probabilité_y": "0.4321", "Décalage_X": "0.5", "note": "1.0"}))),
    Artefact("derive_t09_noms_en_majuscules", "Z_LISIBLE", f_(valeurs_de_t09({"COUVERTURE": "0.4321", "DERIVE": "0.5", "note": "1.0"}))),
    Artefact("temoins_au_plafond", "Z_LISIBLE", f_(temoins_en_plus(PLAFOND_TEMOINS))),
    Artefact("trois_familles_libres", "O_FAMILLES_LIBRES_AU_DELA_DE_DEUX", f_(familles_libres_trois)),
    Artefact("m_sans_conditionnel", "O_MONDE_M_SANS_TEMOIN_CONDITIONNEL", f_(lambda d: tem(d, "LM2").__setitem__("portee_de_la_garantie", fab.TOUS))),
    Artefact("p_echec_differents", "O_P_ECHEC_DIFFERENT_ENTRE_C_ET_I", f_(lambda d: fam(d, "I").__setitem__("p_echec", Brut("0.0600")))),
    Artefact("p_echec_hors_intervalle", "O_P_ECHEC_HORS_DE_L_INTERVALLE", f_(lambda d: [fam(d, x).__setitem__("p_echec", Brut("0.2000")) for x in "CI"])),
    Artefact("imposee_fausse", "O_IMPOSEE_INCOHERENTE", f_(lambda d: fam(d, "A").__setitem__("imposee", False))),
    Artefact("jumeau_sur_saine", "O_JUMEAU_SAIN_SUR_FAMILLE_SAINE", f_(lambda d: fam(d, "A").__setitem__("jumeau_sain", {"mu": Brut("0.0")}))),
    Artefact("mention_dans_non_calcule", "O_MENTION_POSSIBLE_DANS_NON_CALCULE", f_(lambda d: d["non_calcule"].append("famille E : vérité approchée seulement"))),
    # ---- v5 : contrôle par l'aire ----
    Artefact("aire_conforme_factice_saine", "Z_LISIBLE", sain),
    Artefact("aire_ecart_nomme", "O_SABOTEUR_ECART_D_AIRE_AU_DELA_DE_0_001", f_(decalages_de("A", ["0.7012", "1.2000", "2.3262"]))),
    Artefact("aire_unite_brute", "O_SABOTEUR_UNITE_BRUTE_CONSTATEE", lambda: fab.sortie_unite_brute()),
    Artefact("aire_aucune_unite", "O_SABOTEUR_NON_LISIBLE", f_(decalages_de("A", ["0.1", "0.2", "0.3"]))),
    Artefact("aire_ecart_type_indefini", "O_SABOTEUR_NON_LISIBLE", f_(loi_de_b(STUDENT_NU_2))),
    Artefact("aire_loi_hors_du_controle", "O_SABOTEUR_NON_LISIBLE", f_(loi_de_b(BERNOULLI))),
    Artefact("budget_en_pour_cent", "O_BUDGET_HORS_FORME_FRACTION", f_(budget(5))),
    Artefact("budget_chaine_avec_espace", "O_BUDGET_HORS_FORME_FRACTION", f_(budget("5 %"))),
    Artefact("budget_chaine_collee", "O_BUDGET_HORS_FORME_FRACTION", f_(budget("5%"))),
    Artefact("budget_chaine_espace_insecable", "O_BUDGET_HORS_FORME_FRACTION", f_(budget("5 %"))),
]
PAR_NOM = {a.nom: a for a in ARTEFACTS}


@pytest.mark.parametrize("a", ARTEFACTS, ids=[a.nom for a in ARTEFACTS])
def test_artefact(a, tmp_path):
    retour, rap = jouer(a.fabrique(), tmp_path)
    controler(a, retour, rap)


def test_noms_d_artefacts_uniques():
    assert len(PAR_NOM) == len(ARTEFACTS)


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
    assert rap["sortie_auteur"]["caracteres"] <= BORNE
    assert rap["sortie_auteur"]["borne_caracteres"] == BORNE
    assert [(x["famille"], x["issue"], x["ecarts_au_dela_de_0_001"]) for x in rap["controle_par_l_aire"]] == \
        [(f, "conforme", 0) for f in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "a_l_ecart[0]"]]


def test_fichier_unite_brute_egal_au_fabricant():
    assert SORTIE_UNITE_BRUTE.read_text(encoding="utf-8") == texte(fab.sortie_unite_brute())


def test_aire_issue_b_sur_la_factice_d_essai(tmp_path):
    retour, rap = jouer(SORTIE_UNITE_BRUTE.read_bytes(), tmp_path)
    assert retour == 0
    issues = {x["famille"]: (x["issue"], x["raison"]) for x in rap["controle_par_l_aire"]}
    assert issues["A"] == ("unite_brute_constatee", None)
    assert all(v == ("conforme", None) for k, v in issues.items() if k != "A")


@pytest.mark.parametrize("nom,famille,raison", [
    ("aire_aucune_unite", "A", "aucune_unite_ne_realise_les_aires"),
    ("aire_ecart_type_indefini", "B", "ecart_type_indefini"),
    ("aire_loi_hors_du_controle", "B", "loi_hors_du_controle"),
])
def test_aire_issue_c_et_sa_raison(nom, famille, raison, tmp_path):
    retour, rap = jouer(PAR_NOM[nom].fabrique(), tmp_path)
    assert retour == 0 and rap["verdict_d_ensemble"] == "lisible"
    issues = {x["famille"]: (x["issue"], x["raison"]) for x in rap["controle_par_l_aire"]}
    assert issues[famille] == ("non_lisible", raison)


def test_aire_ecart_nomme_par_tranche_et_par_aire(tmp_path):
    retour, rap = jouer(PAR_NOM["aire_ecart_nomme"].fabrique(), tmp_path)
    obs = [o for o in rap["observations"] if o["code"] == "O_SABOTEUR_ECART_D_AIRE_AU_DELA_DE_0_001"]
    assert sorted((o["chemin"], o["tranche"]) for o in obs) == \
        [("familles[0].saboteur.decalages[1]", 1), ("familles[0].saboteur.decalages[1]", 2), ("familles[0].saboteur.decalages[1]", 3)]
    assert {x["famille"]: x["issue"] for x in rap["controle_par_l_aire"]}["A"] == "conforme"


def charger_le_programme():
    import importlib.util
    spec = importlib.util.spec_from_file_location("programme_v5", PROGRAMME)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("d", [0.0, 0.3, 0.9, 1.7, 3.2])
def test_moteur_d_aire_contre_formes_fermees(d):
    """Le moteur numérique (quadrature) contre des formes fermées, à 1e-6."""
    import math
    from statistics import NormalDist
    p = charger_le_programme()
    z = NormalDist()
    # Laplace(0, b) : 1 − ½ e^(−d/b)(1 + d/(2b))
    b = 1.3
    assert abs(p.aire_realisee(p.LaplaceA(0.0, b), d) - (1 - 0.5 * math.exp(-d / b) * (1 + d / (2 * b)))) < 1e-6
    # mélange de normales : Σ w_i w_j Φ((d + μ_i − μ_j)/√(σ_i² + σ_j²))
    w, m, s = [0.7, 0.3], [0.0, 1.5], [1.0, 2.0]
    mel = p.MelangeA(w, [p.NormaleA(mi, si) for mi, si in zip(m, s)])
    attendu = sum(wi * wj * z.cdf((d + mi - mj) / math.sqrt(si * si + sj * sj))
                  for wi, mi, si in zip(w, m, s) for wj, mj, sj in zip(w, m, s))
    assert abs(p.aire_realisee(mel, d) - attendu) < 1e-6
    # Cauchy (Student à un degré), échelle γ : X − Y de Cauchy d'échelle 2γ
    g = 0.8
    assert abs(p.aire_realisee(p.StudentA(1.0, 0.0, g), d) - (0.5 + math.atan(d / (2 * g)) / math.pi)) < 1e-6
    # normale : forme fermée du programme contre NormalDist
    assert abs(p.aire_realisee(p.NormaleA(0.0, 2.0), d) - z.cdf(d / (2.0 * math.sqrt(2.0)))) < 1e-12


def test_moteur_d_aire_reseau_contre_la_fabrique():
    p = charger_le_programme()
    loi = p.ReseauA(p.NormaleA(0.0, 1.0), 0.25)
    kmin, masses = fab.reseau_arrondi_normal(0.25)
    aire_fab = fab.aire_reseau(0.25, kmin, masses)
    for d in (0.1, 0.25, 0.6, 1.0, 1.37):
        assert abs(p.aire_realisee(loi, d) - aire_fab(d)) < 1e-9


def test_budget_en_fraction_sans_observation(tmp_path):
    retour, rap = jouer(f_(budget(Brut("0.10")))(), tmp_path)
    assert retour == 0 and codes_observes(rap) == OBSERVATIONS_SAINES


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
    d["remarques"] += ["produit par modele-fictif-alpha", "cle " + CLE_SK, BRANCHE_HF_20, "la famille K est tenue a l'ecart"]
    fam(d, "B")["jumeau_sain"]["fournisseur-fictif-x"] = Brut("1.0")
    retour, rap = jouer(d, tmp_path)
    brut = (tmp_path / "rapport.json").read_text(encoding="utf-8")
    assert retour == 1
    for interdit in ("modele-fictif", "fournisseur-fictif", "s" + "k-", "h" + "f_", "factice", "retiree", "tenue a l'ecart"):
        assert interdit not in brut
    assert not re.search(r"(?<![A-Za-z0-9_])K(?![A-Za-z0-9_])", brut)


def test_sortie_saine_par_python3_systeme(tmp_path):
    """La commande du mandat : python3 -I -B PROGRAMME SORTIE RAPPORT (motifs par défaut)."""
    rapport = tmp_path / "rapport.json"
    r = subprocess.run(["python3", "-I", "-B", str(PROGRAMME), str(SORTIE_SAINE), str(rapport)],
                       capture_output=True, text=True, timeout=120)
    assert r.returncode == 0
    assert json.loads(rapport.read_text(encoding="utf-8"))["motifs"]["nombre"] == 3


def test_exception_imprevue_sans_trace_de_la_sortie(tmp_path):
    """C1 : le code 3 n'imprime ni trace ni contenu de la sortie."""
    sortie = tmp_path / "s.json"
    sortie.write_text(imbrication("[", "]", 100000)(), encoding="utf-8")
    r = lancer(sortie, tmp_path / "r.json", "--motifs", MOTIFS)
    assert r.returncode == 3 and not (tmp_path / "r.json").exists()
    assert "Traceback" not in r.stderr and "factice" not in r.stderr


# ---------------------------------------------------------------------------
# Parité avec le lanceur v9 : chaque branche de MOTIF_VALEUR_DE_CLE, lue dans le lanceur,
# donne une chaîne minimale (fabriquée ici, jamais écrite dans ce fichier) que le
# programme prend comme chaîne en forme de clé.
# ---------------------------------------------------------------------------

def branches_du_lanceur():
    octets = LANCEUR.read_bytes()
    assert hashlib.sha256(octets).hexdigest() == EMPREINTE_LANCEUR
    t = octets.decode("utf-8")
    debut = t.index("MOTIF_VALEUR_DE_CLE = re.compile(")
    fin = t.index("\nNOM_DE_VARIABLE", debut)
    motif = "".join(re.findall(r'r"((?:[^"\\]|\\.)*)"', t[debut:fin]))
    assert motif.startswith("(") and motif.endswith(")")
    return motif, motif[1:-1].split("|")


def chaine_minimale(branche):
    sortie, i = [], 0
    while i < len(branche):
        ch = branche[i]
        if ch == "\\":
            atome = " " if branche[i + 1] == "s" else branche[i + 1]
            i += 2
        elif ch == "[":
            j = branche.index("]", i + 1)
            assert branche[i + 1] != "^"
            atome = branche[i + 1]
            i = j + 1
        else:
            atome = ch
            i += 1
        n = 1
        q = re.match(r"\{(\d+)(?:,\d*)?\}|[+*?]", branche[i:])
        if q:
            n = int(q.group(1)) if q.group(1) else (1 if q.group(0) == "+" else 0)
            i += len(q.group(0))
        sortie.append(atome * n)
    return "".join(sortie)


def test_lanceur_a_sept_branches():
    _, branches = branches_du_lanceur()
    assert len(branches) == 7


@pytest.mark.parametrize("rang", range(7))
def test_parite_avec_le_lanceur(rang, tmp_path):
    motif, branches = branches_du_lanceur()
    chaine = "zz" + chaine_minimale(branches[rang])
    assert re.search(motif, chaine), "la chaîne fabriquée doit être prise par le lanceur lui-même"
    d = sain()
    d["remarques"].append(chaine)
    retour, rap = jouer(d, tmp_path)
    assert retour == 1
    prises = {f.get("motif") for f in rap["points"]["5_motifs"]["fautes"] if f["code"] == "P5_CHAINE_DE_FORME_DE_CLE"}
    assert prises - {"longue_chaine_melangee"}, "prise par un motif à préfixe"
    assert codes(rap, "5") == {"P5_CHAINE_DE_FORME_DE_CLE"}


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
RE_ENTREE_DE_MOTIF = re.compile(r'^    \("([a-z_]+)", re\.compile\(r"(.*)"\)\),$', re.M)
SI_LONGUE_CHAINE = "        if longue_chaine_melangee(chaine):"


def source():
    return PROGRAMME.read_text(encoding="utf-8")


def gardes_du_programme():
    return sorted({(m.group(1), m.group(2)) for m in RE_GARDE.finditer(source())})


def motifs_du_programme():
    debut = source().index("MOTIFS_DE_CLE = (")
    fin = source().index("\n)\n", debut)
    return [m.group(1) for m in RE_ENTREE_DE_MOTIF.finditer(source()[debut:fin])] + ["longue_chaine_melangee"]


def test_chaque_garde_a_son_artefact_et_reciproquement():
    dans_le_programme = {code for _, code in gardes_du_programme()}
    dans_les_essais = {a.code for a in ARTEFACTS if not a.code.startswith("Z_")}
    assert dans_le_programme == dans_les_essais


def test_chaque_motif_de_cle_a_son_artefact_et_reciproquement():
    noms = motifs_du_programme()
    assert len(noms) == len(set(noms)) == 13
    assert set(noms) == {a.motif for a in ARTEFACTS if a.motif}


def tuer(mutant_texte, concernes, tmp_path):
    mutant = tmp_path / "mutant.py"
    mutant.write_text(mutant_texte, encoding="utf-8")
    assert concernes
    for a in concernes:
        retour, rap = jouer(a.fabrique(), tmp_path / a.nom, programme=mutant)
        with pytest.raises(AssertionError):
            controler(a, retour, rap)


@pytest.mark.parametrize("methode,code", gardes_du_programme(), ids=[c for _, c in gardes_du_programme()])
def test_mutation(methode, code, tmp_path):
    s = source()
    ancien = '.%s("%s"' % (methode, code)
    assert ancien in s
    tuer(s.replace(ancien, '.%s("%s"' % (NEUTRE[methode], code)), [a for a in ARTEFACTS if a.code == code], tmp_path)


@pytest.mark.parametrize("nom", motifs_du_programme())
def test_mutation_de_motif_de_cle(nom, tmp_path):
    s = source()
    if nom == "longue_chaine_melangee":
        assert s.count(SI_LONGUE_CHAINE) == 1
        mute = s.replace(SI_LONGUE_CHAINE, "        if False:")
    else:
        lignes = [m for m in RE_ENTREE_DE_MOTIF.finditer(s) if m.group(1) == nom]
        assert len(lignes) == 1
        m = lignes[0]
        mute = s[:m.start(2)] + "(?!x)x" + s[m.end(2):]
    tuer(mute, [a for a in ARTEFACTS if a.motif == nom], tmp_path)


PARCOURS_ITERATIF = '''    pile = [("valeur", valeur, chemin)]
    while pile:
        sorte, x, ici = pile.pop()
        if sorte == "cle":
            visite(x, ici)
        elif isinstance(x, dict):
            enfants = []
            for k, v in x.items():
                sous = ici + "." + nom_sur(k) if ici else nom_sur(k)
                enfants.append(("cle", k, sous))
                enfants.append(("valeur", v, sous))
            pile.extend(reversed(enfants))
        elif isinstance(x, list):
            pile.extend(reversed([("valeur", v, "%s[%d]" % (ici, i)) for i, v in enumerate(x)]))
        elif isinstance(x, str):
            visite(x, ici)'''
PARCOURS_RECURSIF_V1 = '''    if isinstance(valeur, dict):
        for k, v in valeur.items():
            ici = chemin + "." + nom_sur(k) if chemin else nom_sur(k)
            visite(k, ici)
            parcourir(v, ici, visite)
    elif isinstance(valeur, list):
        for i, v in enumerate(valeur):
            parcourir(v, "%s[%d]" % (chemin, i), visite)
    elif isinstance(valeur, str):
        visite(valeur, chemin)'''
VERITE_V2 = '''    if v.get("mode") == MODE_EXACT:
        verifier_cles(c, v, CLES_VERITE, chemin)
        champ_texte(c, v, "expression", chemin)
    else:
        verifier_cles(c, v, (), chemin, CLES_VERITE)'''
VERITE_V1 = '''    verifier_cles(c, v, CLES_VERITE, chemin)
    champ_texte(c, v, "mode", chemin)
    champ_texte(c, v, "expression", chemin)'''

MUTATIONS_DES_CORRECTIONS = {
    "C1_parcours_recursif_de_la_v1": ([(PARCOURS_ITERATIF, PARCOURS_RECURSIF_V1)], ["imbrication_995"]),
    "C1_garde_d_exception_retiree": ([("    except Exception:  # garde v2 (C1) : exception imprévue",
                                       "    except ZeroDivisionError:  # mutation")], ["imbrication_trop_profonde"]),
    "C2_verite_stricte_de_la_v1": ([(VERITE_V2, VERITE_V1)],
                                   ["verite_mode_nul", "verite_mode_vide", "verite_sans_mode", "verite_non_exacte_sans_expression"]),
    "C3_budget_en_fraction_seule": ([('            return "pour_cent"', "            return None"),
                                     ('            return "chaine"', "            return None")],
                                    ["budget_en_pour_cent", "budget_chaine_avec_espace", "budget_chaine_collee",
                                     "budget_chaine_espace_insecable"]),
    "N2_tirets_non_replies": ([("    t = t.translate(TIRETS_REPLIES)", "    pass")],
                              ["nom_de_modele_trait_insecable", "nom_de_modele_tiret_cadratin"]),
    "borne_relevee_a_62000": ([("TAILLE_MAX_CARACTERES = 52000", "TAILLE_MAX_CARACTERES = 62000")], ["taille_juste_au_dessus"]),
    "borne_baissee_a_51999": ([("TAILLE_MAX_CARACTERES = 52000", "TAILLE_MAX_CARACTERES = 51999")], ["taille_a_la_borne"]),
    "plafond_releve_a_41": ([("TEMOINS_MAX = 40", "TEMOINS_MAX = 41")], ["temoins_au_dela_du_plafond"]),
    "plafond_baisse_a_39": ([("TEMOINS_MAX = 40", "TEMOINS_MAX = 39")], ["temoins_au_plafond"]),
    "aire_a_lecture_retenue_en_unite_brute": (
        [("            lues = [aire_realisee(loi, d * ecart_type) for d in decalages] if ecart_type is not None else None",
          "            lues = [aire_realisee(loi, d) for d in decalages] if ecart_type is not None else None")],
        ["aire_conforme_factice_saine"]),
    "aire_b_sans_repli_sur_l_unite_brute": (
        [("    if all(dans(t[\"brutes\"], TOLERANCE_AIRE_CONFORME) for t in tranches):",
          "    if False:")],
        ["aire_unite_brute"]),
    "aire_tolerance_conforme_resserree": ([("TOLERANCE_AIRE_CONFORME = 0.005", "TOLERANCE_AIRE_CONFORME = 0.0015")],
                                          ["aire_ecart_nomme"]),
    "aire_seuil_d_ecart_nomme_releve": ([("SEUIL_ECART_D_AIRE_NOMME = 0.001", "SEUIL_ECART_D_AIRE_NOMME = 0.002")],
                                        ["aire_ecart_nomme"]),
    "D1_bloc_a_l_ecart_non_compte": ([('                nombre_de_temoins += len(o["temoins"])', "                pass")],
                                     ["plafond_par_le_bloc_a_l_ecart"]),
    "D2_sans_exclusion_des_noms": ([("    restantes = [k for k in cles if not any(m in normaliser(k) for m in MOTS_EXCLUS_DU_DECALAGE)]",
                                     "    restantes = list(cles)")],
                                   ["derive_t09_seule_cle_libre", "derive_t09_taux_exclu"]),
    "D2_sans_repli_par_le_nom": ([("        nommees = [k for k in restantes if any(m in normaliser(k) for m in MOTS_DU_DECALAGE)]",
                                   "        nommees = []")],
                                 ["derive_t09_cle_nommee_parmi_libres"]),
    "E1_repli_parmi_toutes_les_cles": ([("        nommees = [k for k in restantes if any(m in normaliser(k) for m in MOTS_DU_DECALAGE)]",
                                         "        nommees = [k for k in cles if any(m in normaliser(k) for m in MOTS_DU_DECALAGE)]")],
                                       ["derive_t09_cle_nommee_exclue_par_a"]),
    "E1_noms_compares_sans_normalisation": ([("normaliser(k) for m in MOTS_EXCLUS_DU_DECALAGE", "k for m in MOTS_EXCLUS_DU_DECALAGE"),
                                             ("normaliser(k) for m in MOTS_DU_DECALAGE", "k for m in MOTS_DU_DECALAGE")],
                                            ["derive_t09_noms_accentues", "derive_t09_noms_en_majuscules"]),
}


@pytest.mark.parametrize("nom", sorted(MUTATIONS_DES_CORRECTIONS))
def test_mutation_des_corrections(nom, tmp_path):
    remplacements, artefacts = MUTATIONS_DES_CORRECTIONS[nom]
    s = source()
    for ancien, nouveau in remplacements:
        assert s.count(ancien) == 1, ancien
        s = s.replace(ancien, nouveau)
    tuer(s, [PAR_NOM[n] for n in artefacts], tmp_path)


# ---------------------------------------------------------------------------
# Correspondance vers l'entrée du recalcul (mode --vers-recalcul)
# ---------------------------------------------------------------------------

CODES_DE_FORME_DU_RECALCUL = {
    "version_entree", "identifiant_double", "forme_du_temoin", "cles_du_temoin", "garantie_hors_liste",
    "grandeur_hors_liste", "champ_ferme_population", "forme_de_regle", "regle_hors_grammaire",
    "parametres_de_regle", "risque_inattendu", "risque_absent", "cles_de_lois", "suite_absente",
    "loi_de_lecture_absente", "loi_de_calibration_absente", "voisine_absente", "taille_absente",
    "forme_de_loi", "loi_hors_grammaire", "parametres_de_loi", "nombre_non_rationnel", "entier_attendu",
    "constante_json", "saboteurs_requis_sans_gain", "puissance_sans_saboteur_unique",
}


def sain_convertible():
    """v3 : la sortie factice saine v3 telle quelle (son T09 porte déjà un décalage lisible ; le
    monde M n'est plus converti, D3). Remplissages de forme, aucune valeur vraie."""
    return sain()


def jouer_correspondance(contenu, dossier, programme=PROGRAMME):
    dossier.mkdir(parents=True, exist_ok=True)
    sortie, entree = dossier / "sortie.json", dossier / "entree-recalcul.json"
    rendu = Path(str(entree) + ".correspondance.json")
    for p in (sortie, entree, rendu):
        if p.exists():
            p.unlink()
    if isinstance(contenu, dict):
        contenu = texte(contenu)
    sortie.write_text(contenu, encoding="utf-8")
    r = subprocess.run([sys.executable, "-I", "-B", str(programme), "--vers-recalcul", str(sortie), str(entree),
                        "--motifs", str(MOTIFS)], capture_output=True, text=True, timeout=120)
    lu = json.loads(rendu.read_text(encoding="utf-8")) if rendu.exists() else None
    return r.returncode, (entree if entree.exists() else None), lu


def ligne_de(rendu, tid):
    return next(x for x in rendu["temoins"] if x.get("temoin") == tid)


def g_(fonction, base=sain_convertible):
    def fabrique():
        d = base()
        fonction(d)
        return d
    return fabrique


def tailles_entieres(d):
    for tr in fam(d, "H")["tranches"]:
        tr["loi_honnete"]["parametres"]["tailles_de_famille"] = 7


ARTEFACTS_CORRESPONDANCE = [
    ("monde_m_sans_gamma", "NC_MONDE_M_SANS_GAMMA", sain, "LM1"),
    ("monde_m_sans_gamma_signal_somme", "NC_MONDE_M_SANS_GAMMA", g_(lambda d: tem(d, "LM2").__setitem__("signal", "somme")), "LM2"),
    ("derive_sans_champ", "NC_DERIVE_SANS_CHAMP", g_(lambda d: tem(d, "T09").pop("valeurs_de_plus")), "T09"),
    ("derive_sans_champ_temoin_libre_de_f", "NC_DERIVE_SANS_CHAMP", g_(valeurs_de_t09({"note_a": "1.0", "note_b": "2.0"})), "LF2"),
    ("loi_autre", "NC_LOI_AUTRE", g_(lambda d: fam(d, "B")["tranches"][0].__setitem__(
        "loi_honnete", {"type": "autre", "parametres": {"definition": "définition factice"}})), "LB1"),
    ("composantes_ambigues", "NC_COMPOSANTES_AMBIGUES", g_(lambda d: fam(d, "C").__setitem__("p_echec", Brut("0.0600"))), "T14"),
    ("pas_de_composante", "NC_PAS_DE_COMPOSANTE_D_ECHEC", g_(lambda d: tem(d, "LA2").__setitem__("population_de_calibration", "honnetes_qui_echouent")), "LA2"),
    ("tailles_de_famille", "NC_TAILLES_DE_FAMILLE", g_(tailles_entieres), "LH2"),
    ("saboteur_en_unite_brute", "NC_SABOTEUR_EN_UNITE_BRUTE", lambda: fab.sortie_unite_brute(), "T05"),
    ("saboteur_non_lisible", "NC_SABOTEUR_NON_LISIBLE", g_(decalages_de("A", ["0.1", "0.2", "0.3"])), "T07"),
]


def controler_correspondance(code, tid, retour, rendu):
    assert retour == 0 and rendu is not None
    ligne = ligne_de(rendu, tid)
    assert ligne["statut"] == "non_converti" and ligne["raison"] == code


@pytest.mark.parametrize("nom,code,fabrique,tid", ARTEFACTS_CORRESPONDANCE, ids=[a[0] for a in ARTEFACTS_CORRESPONDANCE])
def test_correspondance_artefact(nom, code, fabrique, tid, tmp_path):
    retour, _, rendu = jouer_correspondance(fabrique(), tmp_path)
    controler_correspondance(code, tid, retour, rendu)


RE_NON_CONVERTIBLE = re.compile(r'raise NonConvertible\("(NC_[A-Z_]+)"\)')


def test_chaque_non_convertible_a_son_artefact():
    assert set(RE_NON_CONVERTIBLE.findall(source())) == {a[1] for a in ARTEFACTS_CORRESPONDANCE}


@pytest.mark.parametrize("code", sorted(set(RE_NON_CONVERTIBLE.findall(PROGRAMME.read_text(encoding="utf-8")))))
def test_mutation_de_non_convertible(code, tmp_path):
    mutant = tmp_path / "mutant.py"
    mutant.write_text(source().replace('raise NonConvertible("%s")' % code, "pass"), encoding="utf-8")
    for nom, c_, fabrique, tid in ARTEFACTS_CORRESPONDANCE:
        if c_ != code:
            continue
        retour, _, rendu = jouer_correspondance(fabrique(), tmp_path / nom, programme=mutant)
        with pytest.raises((AssertionError, StopIteration)):
            controler_correspondance(code, tid, retour, rendu)


def test_correspondance_de_la_sortie_saine_telle_quelle(tmp_path):
    retour, entree, rendu = jouer_correspondance(texte(sain()), tmp_path)
    assert retour == 0 and entree is not None
    non = {x["temoin"]: x["raison"] for x in rendu["temoins"] if x["statut"] == "non_converti"}
    assert non == {"LM1": "NC_MONDE_M_SANS_GAMMA", "LM2": "NC_MONDE_M_SANS_GAMMA"}
    assert rendu["comptes"] == {"convertis": 37, "non_convertis": 2}
    assert rendu["derive_de_F"] == {
        "statut": "lue", "temoin": "T09", "n_du_temoin": 299, "rang_de_la_cle": 2, "valeur_transmise": "0.4456",
        "unite_du_decalage": "ecarts types de la loi de la tranche associée à T09",
        "tranche_associee_a_T09": {"rang": 2, "n_calibration_contient_299": True, "rangs_des_tranches_a_299": [2],
                                   "regle": "la première tranche dont n_calibration contient 299 ; "
                                            "si aucune, la première tranche, signalée"},
        "loi_de_la_tranche": '{"type": "normale", "parametres": {"mu": 0.25, "sigma": 1.0}}',
        "loi_de_la_tranche_format": "texte JSON d'une loi de la grammaire, nombres écrits tels quels",
        "controle": {"par": "programme de vérité v2, mode --recalculer",
                     "critere": "sous la loi de la tranche associée à T09, le seuil au quantile à 99 % "
                                "(taux de départ de 1 %) a, sous la même loi décalée de la valeur "
                                "transmise, un taux de 3 %",
                     "taux_de_depart": "0.01", "taux_vise": "0.03", "tolerance": "0.001",
                     "nature_de_la_tolerance": "absolue", "fait_par_ce_programme": False}}
    t09 = next(t for t in json.loads(entree.read_text(encoding="utf-8"))["temoins"] if t["id"] == "T09")
    assert t09["lois"]["lecture"]["type"] == "decalage" and t09["lois"]["lecture"]["parametres"]["delta_en_ecarts_types"] == 0.4456


def test_correspondance_controle_par_l_aire_au_compte_rendu(tmp_path):
    retour, _, rendu = jouer_correspondance(SORTIE_UNITE_BRUTE.read_text(encoding="utf-8"), tmp_path)
    assert retour == 0
    cpa = rendu["controle_par_l_aire"]
    assert cpa["tolerance_conforme"] == "0.005" and cpa["ecart_nomme_au_dela_de"] == "0.001"
    a = next(x for x in cpa["familles"] if x["famille"] == "A")
    assert a["issue"] == "unite_brute_constatee" and a["mot_de_la_mere_requis"] is True
    assert all(abs(x - c_) <= 0.005 for t in a["tranches"] for x, c_ in zip(t["aires_unite_brute"], (0.69, 0.80, 0.95)))
    non = {x["temoin"]: x["raison"] for x in rendu["temoins"] if x["statut"] == "non_converti" and "temoin" in x}
    assert non["T05"] == non["T07"] == "NC_SABOTEUR_EN_UNITE_BRUTE"


def test_correspondance_tranche_de_t09_absente(tmp_path):
    """Aucune tranche de F ne joue 299 : la première tranche est transmise, et c'est dit."""
    d = sain()
    fam(d, "F")["tranches"][1]["n_calibration"] = [300]
    retour, _, rendu = jouer_correspondance(d, tmp_path)
    assert retour == 0
    tr = rendu["derive_de_F"]["tranche_associee_a_T09"]
    assert (tr["rang"], tr["n_calibration_contient_299"], tr["rangs_des_tranches_a_299"]) == (1, False, [])


def plusieurs_tranches_a_299(d):
    fam(d, "F")["tranches"][1]["n_calibration"] = [299]
    fam(d, "F")["tranches"][2]["n_calibration"] = [200, 299, 300, 400]


def test_correspondance_plusieurs_tranches_a_299(tmp_path):
    """R2 : si plusieurs tranches de F contiennent 299, la première est prise, et c'est signalé."""
    d = sain()
    plusieurs_tranches_a_299(d)
    retour, _, rendu = jouer_correspondance(d, tmp_path)
    assert retour == 0
    tr = rendu["derive_de_F"]["tranche_associee_a_T09"]
    assert (tr["rang"], tr["n_calibration_contient_299"], tr["rangs_des_tranches_a_299"]) == (2, True, [2, 3])
    assert rendu["derive_de_F"]["loi_de_la_tranche"] == '{"type": "normale", "parametres": {"mu": 0.25, "sigma": 1.0}}'


def test_mutation_derniere_tranche_a_299(tmp_path):
    ancien = "        rang_tranche = rangs_a_299[0] if rangs_a_299 else None"
    s = source()
    assert s.count(ancien) == 1
    mutant = tmp_path / "mutant.py"
    mutant.write_text(s.replace(ancien, "        rang_tranche = rangs_a_299[-1] if rangs_a_299 else None"), encoding="utf-8")
    d = sain()
    plusieurs_tranches_a_299(d)
    retour, _, rendu = jouer_correspondance(d, tmp_path / "essai", programme=mutant)
    assert rendu["derive_de_F"]["tranche_associee_a_T09"]["rang"] != 2


def test_mutation_tranche_de_t09(tmp_path):
    ancien = 'N_DE_T09 = TABLE_DES_TEMOINS_IMPOSES["T09"]["n"]'
    s = source()
    assert s.count(ancien) == 1
    mutant = tmp_path / "mutant.py"
    mutant.write_text(s.replace(ancien, "N_DE_T09 = 300"), encoding="utf-8")
    retour, _, rendu = jouer_correspondance(sain(), tmp_path / "essai", programme=mutant)
    assert rendu["derive_de_F"]["tranche_associee_a_T09"]["rang"] != 2


def test_correspondance_derive_illisible_dit_f_a_ecarter(tmp_path):
    d = sain()
    tem(d, "T09").pop("valeurs_de_plus")
    retour, _, rendu = jouer_correspondance(d, tmp_path)
    assert retour == 0
    assert rendu["derive_de_F"] == {"statut": "illisible_F_a_ecarter"}
    assert {"monde": "F", "raisons": ["E_DERIVE_SANS_DECALAGE_LISIBLE"]} in rendu["verification"]["ecartes"]


def voisine_de_ld1(n):
    def r(d):
        t = tem(d, "LD1")
        t.update({"n": n, "regle": {"type": "plus_grand_de_la_tranche_voisine"}, "garantie": "en moyenne",
                  "risque_ou_niveau": None, "grandeur": "taux_moyen"})
    return r


@pytest.mark.parametrize("n,attendu", [(40, 300), (300, 400), (400, 300)])
def test_tranche_voisine_sans_boucle(n, attendu, tmp_path):
    """D : tranches à 40, 300 et 400. La voisine est la suivante ; pour la dernière, la précédente."""
    retour, entree, rendu = jouer_correspondance(g_(voisine_de_ld1(n))(), tmp_path)
    assert retour == 0
    ld1 = next(t for t in json.loads(entree.read_text(encoding="utf-8"))["temoins"] if t["id"] == "LD1")
    assert ld1["lois"]["voisine"]["n"] == attendu
    assert "CH1B_TRANCHE_VOISINE_SUIVANTE_OU_PRECEDENTE" in ligne_de(rendu, "LD1")["choix"]


def test_mutation_tranche_voisine_circulaire(tmp_path, monkeypatch):
    ancien = "        voisine = tranches[i_lecture + 1 if i_lecture + 1 < len(tranches) else i_lecture - 1]"
    s = source()
    assert s.count(ancien) == 1
    mutant = tmp_path / "mutant.py"
    mutant.write_text(s.replace(ancien, "        voisine = tranches[(i_lecture + 1) % len(tranches)]"), encoding="utf-8")
    retour, entree, rendu = jouer_correspondance(g_(voisine_de_ld1(400))(), tmp_path / "essai", programme=mutant)
    ld1 = next(t for t in json.loads(entree.read_text(encoding="utf-8"))["temoins"] if t["id"] == "LD1")
    assert ld1["lois"]["voisine"]["n"] != 300


def test_correspondance_acceptee_par_le_programme_de_verite(tmp_path):
    """La correspondance de la sortie factice convertible est acceptée par le mode --recalculer du
    programme de vérité, sans aucun refus de forme. Seuls les statuts et les codes sont lus ;
    aucune valeur calculée n'est lue ni recopiée."""
    assert hashlib.sha256(VERITE.read_bytes()).hexdigest() == EMPREINTE_VERITE
    retour, entree, rendu = jouer_correspondance(texte(sain_convertible()), tmp_path)
    assert retour == 0 and rendu["comptes"] == {"convertis": 37, "non_convertis": 2}
    donnees = json.loads(entree.read_text(encoding="utf-8"))
    assert set(donnees) == {"version_entree", "temoins"} and len(donnees["temoins"]) == 37
    sortie_verite = tmp_path / "sortie-verite.json"
    r = subprocess.run(["python3", "-I", "-B", str(VERITE), "--recalculer", str(entree), str(sortie_verite)],
                       capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0, r.stderr[-2000:]
    resultat = json.loads(sortie_verite.read_text(encoding="utf-8"))
    statuts = {cle: (v["statut"], v.get("code")) for cle, v in resultat["temoins"].items()}
    assert len(statuts) == 37
    refus_de_forme = {cle: code for cle, (statut, code) in statuts.items() if statut == "refuse" and code in CODES_DE_FORME_DU_RECALCUL}
    assert refus_de_forme == {}
    assert all(statut == "calcule" for statut, _ in statuts.values()), {k: v for k, v in statuts.items() if v[0] != "calcule"}
    sortie_verite.unlink()


def test_correspondance_refuse_une_sortie_illisible(tmp_path):
    retour, entree, rendu = jouer_correspondance("Voici :\n" + texte(sain_convertible()), tmp_path)
    assert retour == 2 and entree is None and rendu is None


def test_correspondance_exception_imprevue(tmp_path):
    retour, entree, rendu = jouer_correspondance(imbrication("[", "]", 100000)(), tmp_path)
    assert retour == 3 and entree is None and rendu is None


def test_correspondance_n_ecrase_jamais(tmp_path):
    (tmp_path / "entree-recalcul.json").write_text("ancien", encoding="utf-8")
    sortie = tmp_path / "s.json"
    sortie.write_text(texte(sain_convertible()), encoding="utf-8")
    r = lancer("--vers-recalcul", sortie, tmp_path / "entree-recalcul.json", "--motifs", MOTIFS)
    assert r.returncode == 3 and (tmp_path / "entree-recalcul.json").read_text(encoding="utf-8") == "ancien"


def test_correspondance_choix_declares(tmp_path):
    retour, _, rendu = jouer_correspondance(texte(sain_convertible()), tmp_path)
    assert "CH2_ECHEC_PAR_POIDS_EGAL_A_P_ECHEC" in ligne_de(rendu, "T14")["choix"]
    assert "CH7_DERIVE_DE_F_LUE_DANS_T09" in ligne_de(rendu, "T09")["choix"]
    assert "CH8B_TAILLES_DU_MANDAT_POUR_T10_T11" in ligne_de(rendu, "T11")["choix"]
    assert "CH9_T07_TAILLE_DE_PLUS_400" in ligne_de(rendu, "T07")["choix"]
    assert "CH5_SABOTEUR_DECALAGE_DE_LA_LOI_HONNETE" in ligne_de(rendu, "T05")["choix"]
    assert all(x["chemin"].startswith("a_l_ecart") == ("temoin" not in x) for x in rendu["temoins"])


MUTATIONS_DE_LA_CORRESPONDANCE = {
    "garde_d_illisibilite_retiree": (
        'if resultat["verdict_d_ensemble"] != "lisible":  # garde : sortie illisible, rien n\'est converti',
        "if False:", test_correspondance_refuse_une_sortie_illisible),
    "garde_d_exception_retiree": (
        "    except Exception:  # garde v2 : exception imprévue pendant la correspondance",
        "    except ZeroDivisionError:  # mutation", test_correspondance_exception_imprevue),
}


@pytest.mark.parametrize("nom", sorted(MUTATIONS_DE_LA_CORRESPONDANCE))
def test_mutation_de_la_correspondance(nom, tmp_path, monkeypatch):
    ancien, nouveau, essai = MUTATIONS_DE_LA_CORRESPONDANCE[nom]
    s = source()
    assert s.count(ancien) == 1
    mutant = tmp_path / "mutant.py"
    mutant.write_text(s.replace(ancien, nouveau), encoding="utf-8")
    monkeypatch.setattr(sys.modules[__name__], "PROGRAMME", mutant)
    monkeypatch.setattr(sys.modules[__name__], "jouer_correspondance",
                        lambda contenu, dossier, programme=mutant: _jouer_correspondance_origine(contenu, dossier, mutant))
    with pytest.raises(AssertionError):
        essai(tmp_path / "essai")


_jouer_correspondance_origine = jouer_correspondance
