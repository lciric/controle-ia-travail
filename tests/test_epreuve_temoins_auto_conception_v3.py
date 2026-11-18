"""Essais du programme d'épreuve des témoins v3 (correctif v2c de la course d'auto-conception) — hors ligne, aucun appel,
aucun relais, aucune clé, aucun réseau.

(a) Les essais de l'épreuve portés de la v2 (`tests/test_lancer_course_auto_conception_v2.py`) au v3.
(b) Essai neuf par adaptateurs **réels** (classes de la copie épinglée de l'orchestrateur, construites par
    `adaptateurs_reels_v56` du lanceur v8, comme `reel()` les construit ; on s'arrête à `construire_options`, fonction pure) :
    le câblage de la v2 reproduit le défaut constaté en réel ; le v3 passe pour chaque rôle de l'épreuve (aiguilleur et juge
    Claude par le kit, juge Argon par commande externe) ; artefacts (R5) : un dossier d'appel hors des chemins interdits est
    refusé par la garde de l'orchestrateur et par la garde du v3 ; un dossier voisin lisible est refusé par la garde du v3.
(c) Mutation : le v3 où l'on remet `sortie / "appels"` échoue à l'essai neuf.
Rien d'autre ne change : les fonctions de lecture, de service et de contrôle du v3 sont celles de la v2, à l'octet."""
import hashlib
import importlib.util
import inspect
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

sys.dont_write_bytecode = True
RACINE = Path(__file__).resolve().parents[1]


def _charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


L = _charger("lancer_course_auto_conception_v3", RACINE / "scripts" / "lancer_course_auto_conception_v3.py")
CHEMIN_E3 = RACINE / "scripts" / "epreuve_temoins_auto_conception_v3.py"
E = _charger("epreuve_temoins_auto_conception_v3", CHEMIN_E3)
E2 = _charger("epreuve_temoins_auto_conception_v2_pour_essai_v3", RACINE / "scripts" / "epreuve_temoins_auto_conception_v2.py")

FIXE = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
TEMOINS = {t["id"]: t for t in json.loads((RACINE / L.PIECES["temoins"][0]).read_text())["temoins"]}
ITEMS = FIXE["items_juge"]
DECL_EPREUVE_V2 = RACINE / "docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-epreuve-temoins-auto-conception-v2.json"
MESSAGE_DU_DEFAUT = "le dossier de l'agent doit être sous un chemin interdit en lecture (sinon la fiche voisine reste lisible)"


def _matiere_v3():
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"{L.REF_MAIN}:{L.MATIERE[0]}"], capture_output=True)
    if p.returncode != 0 or hashlib.sha256(p.stdout).hexdigest() != L.MATIERE[1]:
        return None
    return p.stdout


MATIERE = _matiere_v3()
avec_matiere = pytest.mark.skipif(MATIERE is None, reason="matière v3 absente de refs/remotes/origin/main (fetch ciblé requis)")


def _orchestrateur():
    presents = [Path(o) for o in L.ORCHESTRATEURS_CANDIDATS if (Path(o) / "pole" / "fiches_v54.py").is_file()]
    return presents[0] if len(presents) == 1 else None


ORCH = _orchestrateur()
avec_orchestrateur = pytest.mark.skipif(ORCH is None, reason="copie de l'orchestrateur épinglé absente")


def _v8():
    """Le lanceur v8 de l'orchestrateur, chargé comme `reel()` le charge (aucun appel ; `-B`)."""
    if str(ORCH) not in sys.path:
        sys.path.insert(0, str(ORCH))
    return _charger("ideation_v8_pour_essai_epreuve_v3", ORCH / L.LANCEUR_ORCHESTRATEUR)


# --- (a) essais portés de la v2 --------------------------------------------------------------------------------------------------


def _verdicts(fonction):
    out = {}
    for tid, t in TEMOINS.items():
        its = fonction(t)
        out[tid] = {"items": its, "notable": all(its.values())}
    return out


def test_lecture_epreuve_parfait_et_artefacts():
    a = {tid: "niveau_methode" for tid in TEMOINS}
    assert E.lire_epreuve({"j": _verdicts(lambda t: E.verite(t, ITEMS))}, a, TEMOINS, ITEMS)["verdict"] == "réussie"
    assert E.lire_epreuve({"j": _verdicts(lambda t: {k: True for k in ITEMS})}, a, TEMOINS, ITEMS)["verdict"] == "échouée"
    assert E.lire_epreuve({"j": _verdicts(lambda t: {k: False for k in ITEMS})}, a, TEMOINS, ITEMS)["verdict"] == "échouée"
    un_manque = _verdicts(lambda t: E.verite(t, ITEMS))
    un_manque["t06"] = None
    assert E.lire_epreuve({"j": un_manque}, a, TEMOINS, ITEMS)["verdict"] == "échouée"
    parfait = _verdicts(lambda t: E.verite(t, ITEMS))
    assert E.lire_epreuve({"j": parfait}, dict(a, t03="a_corriger"), TEMOINS, ITEMS)["verdict"] == "échouée"
    assert E.lire_epreuve({"j": parfait}, dict(a, t07="concret"), TEMOINS, ITEMS)["verdict"] == "échouée"
    assert E.lire_epreuve({"j": parfait}, dict(a, t07="a_corriger"), TEMOINS, ITEMS)["verdict"] == "réussie"
    assert E.lire_epreuve({}, a, TEMOINS, ITEMS)["verdict"] == "échouée"


def test_temoins_couvrent_chaque_item_et_aucune_regle_de_longueur():
    s = E.controles_statiques(TEMOINS, ITEMS, (RACINE / L.PIECES["consigne_proposeur"][0]).read_text(), MATIERE)
    assert s["items_plantes_tous_couverts"] and s["bornes_tenues"] and s["champs_identiques"]
    assert s["regle_de_seuil_sur_la_longueur_erreurs_min"] >= 1 and not s["titres_de_temoin_dans_la_consigne_servie"]
    if MATIERE is not None:
        assert s["identifiants_absents_de_la_matiere"] == []
    assert sorted(TEMOINS["t01"]["contenu"]) == sorted(FIXE["champs_fiche"])


@avec_matiere
@avec_orchestrateur
def test_epreuve_hors_ligne_bout_en_bout(tmp_path):
    m = tmp_path / "matiere-v3.md"
    m.write_bytes(MATIERE)
    rap = E.hors_ligne(tmp_path / "epreuve", m, E.orchestrateur_present(L.ORCHESTRATEURS_CANDIDATS))
    assert rap["version"] == "epreuve_temoins_auto_conception_v3"
    assert rap["conclusion"]["verdict"] == "témoins éprouvés hors ligne"
    assert rap["lectures"]["parfait"]["verdict"] == "réussie" and rap["juges_au_hasard_reussis"] == 0
    assert all(rap["lectures"][n]["verdict"] == "échouée" for n in ("longueur", "indulgent", "severe"))
    assert rap["artefact_aiguilleur_tout_concret"] == "échouée"


def test_epreuve_reelle_refuse_un_environnement_avec_cle(monkeypatch):
    monkeypatch.setenv("UNE_API_KEY", "x")
    with pytest.raises(Exception) as e:
        E.reel()
    assert type(e.value).__name__ == "Refus" and "UNE_API_KEY" in str(e.value)


def test_temoins_v2_entrelaces_par_champ_lu():
    s = E.controles_statiques(TEMOINS, ITEMS, (RACINE / L.PIECES["consigne_proposeur"][0]).read_text(), MATIERE)
    assert s["regle_de_seuil_sur_le_champ_lu_erreurs_min"] >= 1
    assert "même dépense totale" in TEMOINS["t02"]["contenu"]["epreuve_monde_plante"]
    assert "jamais employée pour écarter" in TEMOINS["t03"]["contenu"]["module_change"]


# --- rien d'autre ne change -----------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("nom", ["lire_epreuve", "verite", "jouer", "servir", "identifiant_servi", "controles_statiques", "hors_ligne",
                                 "charger_orchestrateur", "fiche_servie", "JugeFactice", "AiguilleurFactice", "ecrire_scelle"])
def test_fonctions_identiques_a_la_v2(nom):
    assert inspect.getsource(getattr(E, nom)) == inspect.getsource(getattr(E2, nom))


def test_constantes_identiques_a_la_v2_sauf_les_chemins_neufs():
    for nom in ("PLAFOND_EPREUVE_USD", "TEMOINS", "CONSIGNE_JUGE", "CONSIGNE_AIGUILLEUR", "CONSIGNE_PROPOSEUR", "CONFIGURATION",
                "ETAPE", "RACINE_GRAINES", "CHAMP_LU", "N_JUGES_AU_HASARD", "BORNE_CHAMP", "BORNE_CARTE"):
        assert getattr(E, nom) == getattr(E2, nom), nom
    assert E.DECLARATION_EPREUVE.name == "declaration-relais-epreuve-temoins-auto-conception-v3.json" != E2.DECLARATION_EPREUVE.name
    assert E.RAPPORT_REEL.name == "epreuve-temoins-reelle-auto-conception-v3.json" != E2.RAPPORT_REEL.name
    assert E.LANCEUR.name == "lancer_course_auto_conception_v3.py"
    assert not E.RAPPORT_REEL.exists() and not E.DECLARATION_EPREUVE.exists()   # écrits par la session d'exécution seulement


# --- (b) essai neuf par adaptateurs réels -------------------------------------------------------------------------------------


def fournisseurs_epreuve(tmp_path) -> dict:
    """Blocs des relais de l'épreuve tels que `reel()` les remet à l'orchestrateur : la déclaration réelle de la v2 (format
    scellé, PID morts), vérifiée par `verifier_declaration` du lanceur v3 avec la pièce de départ scellée, puis enveloppée par
    la garde de crédit (`envelopper_commandes`)."""
    r = L.Reglages.production()
    depart = L.verifier_piece_de_depart(r)
    decl = L.verifier_declaration(json.loads(DECL_EPREUVE_V2.read_text(encoding="utf-8")), FIXE, depart)
    arrets = tmp_path / "arrets-credit"
    arrets.mkdir()
    decl = L.envelopper_commandes(decl, sys.executable, RACINE / L.PIECES["garde_credit"][0], arrets)
    assert sorted(decl["fournisseurs"]) == ["argon", "claude"]
    return decl["fournisseurs"]


def plan_epreuve() -> list:
    """Le plan de `reel()` (même expression) : l'aiguilleur, puis les juges de la configuration."""
    ps = FIXE["plafonds_session"]
    ca, cj = "consigne de l'aiguilleur", "consigne du juge"
    return [("aiguilleur", FIXE["aiguilleur"], ca, float(ps["aiguilleur"]), False)] + \
        [(j["etiquette"], j, cj, float(ps["juge"]), True) for j in FIXE["juges"]]


@pytest.fixture
def epreuve_reelle_simulee(tmp_path):
    if ORCH is None:
        pytest.skip("copie de l'orchestrateur épinglé absente")
    v8 = _v8()
    sortie = tmp_path / "epreuve-temoins-auto-conception-essai"
    sortie.mkdir()
    base = tmp_path / "pole-sessions-epreuve-essai"
    base.mkdir()
    return {"v8": v8, "sortie": sortie, "base": str(base), "fournisseurs": fournisseurs_epreuve(tmp_path), "plan": plan_epreuve()}


def test_cablage_de_la_v2_reproduit_le_defaut_constate(epreuve_reelle_simulee):
    """Diagnostic reproduit hors ligne : les chemins interdits remis par la v2 (`sortie/"sortie"`, base) et le dossier qu'elle
    passait (`sortie/"appels"/aiguilleur/t01`) → la garde de l'orchestrateur lève le message de la sortie d'erreur versée."""
    m = epreuve_reelle_simulee
    ads, _ = m["v8"].adaptateurs_reels_v56({"fournisseurs": m["fournisseurs"]}, str(m["sortie"] / "sortie"), m["base"])
    from pole.adaptateurs import construire_options
    with pytest.raises(ValueError, match="doit être sous un chemin interdit en lecture") as e:
        construire_options(os.path.abspath(str(m["sortie"] / "appels" / "aiguilleur" / "t01")), 0.25, 1,
                           url_relais=ads["claude"].url_relais, role="juge_ideation", interdire_lecture=ads["claude"].interdire_lecture)
    assert MESSAGE_DU_DEFAUT in str(e.value)
    versee = (RACINE / "docs/notes/organisme-auto-conception-v1/course-v2/epreuve-reelle-arret-avant-appel-2026-11-18-v1/"
              "epreuve-reelle.stderr.txt").read_text(encoding="utf-8")
    assert MESSAGE_DU_DEFAUT in versee and "/appels/aiguilleur/t01 hors de" in versee


def test_v3_sain_chaque_role_de_l_epreuve(epreuve_reelle_simulee):
    m = epreuve_reelle_simulee
    ads, portes, appels, controle = E.preparer_appels(m["v8"], m["fournisseurs"], m["sortie"], m["base"], m["plan"], TEMOINS,
                                                      refus=L.Refus)
    from pole.adaptateurs import AdaptateurClaudeSDK
    from pole.adaptateurs_v56 import AdaptateurCommandeExterneV56
    assert appels == Path(os.path.realpath(m["sortie"])) / "sortie" / "appels"
    assert isinstance(ads["claude"], AdaptateurClaudeSDK) and isinstance(ads["argon"], AdaptateurCommandeExterneV56)
    assert sorted(portes) == ["argon", "claude"]
    attendu = [os.path.realpath(m["base"]), os.path.realpath(m["sortie"] / "sortie")]
    assert ads["claude"].interdire_lecture == attendu
    assert sorted(controle) == sorted(["aiguilleur"] + [j["etiquette"] for j in FIXE["juges"]])
    for j in [FIXE["aiguilleur"]] + FIXE["juges"]:
        c = controle[j["etiquette"]]
        if j["fournisseur"] == "claude":
            assert c["dossiers"] == len(TEMOINS) == 11 and c["deny_read"] == attendu
            assert c["voisins_interdits"] == 3 * 11 - 1 and c["adaptateur"] == "AdaptateurClaudeSDK"
        else:
            assert c["adaptateur"] == "AdaptateurCommandeExterneV56" and c["controle"].startswith("sans objet")
    assert {j["fournisseur"] for j in [FIXE["aiguilleur"]] + FIXE["juges"]} == {"claude", "argon"}
    assert not (m["sortie"] / "sortie").exists()  # la garde n'écrit rien


def test_artefact_dossier_hors_chemin_interdit_refuse(epreuve_reelle_simulee):
    """R5 : un dossier d'appel hors des chemins interdits → la garde de l'orchestrateur refuse, et celle du v3 aussi, avant
    tout appel."""
    m = epreuve_reelle_simulee
    ads, _ = m["v8"].adaptateurs_reels_v56({"fournisseurs": m["fournisseurs"]}, str(m["sortie"] / "sortie"), m["base"])
    with pytest.raises(L.Refus, match="refusé par la garde de l'orchestrateur avant tout appel"):
        E.verifier_dossiers_d_appel(ads, m["plan"], TEMOINS, m["sortie"] / "appels", refus=L.Refus)
    with pytest.raises(L.Refus, match="fiche voisine"):
        E.verifier_dossiers_d_appel(ads, m["plan"], TEMOINS, m["sortie"].parent / "ailleurs", refus=L.Refus)


def test_artefact_voisin_lisible_refuse(epreuve_reelle_simulee):
    """R5 pour la garde neuve : liste interdite qui couvre le seul dossier de l'aiguilleur → son appel passe
    `construire_options`, mais les dossiers des juges restent lisibles : refus."""
    m = epreuve_reelle_simulee
    from pole.adaptateurs import AdaptateurClaudeSDK
    appels = E.dossier_des_appels(m["sortie"])
    ads = {"claude": AdaptateurClaudeSDK("http://127.0.0.1:8787", arme=True, interdire_lecture=[str(appels / "aiguilleur")]),
           "argon": object()}
    with pytest.raises(L.Refus, match="dossiers voisins lisibles"):
        E.verifier_dossiers_d_appel(ads, m["plan"], TEMOINS, appels, refus=L.Refus)


def test_reel_cable_la_garde_avant_la_transmission_et_les_appels():
    src = inspect.getsource(E.reel)
    assert cablage_conforme(src)
    i_prep, i_trans, i_jouer = src.index("preparer_appels("), src.index(".transmettre("), src.index("jouer(")
    assert i_prep < i_trans < i_jouer


def cablage_conforme(source_reel: str) -> bool:
    """`reel()` passe à `jouer` la racine rendue par `preparer_appels`, jamais un dossier bâti à part sous la sortie."""
    return ("adaptateurs, portes, appels, dossiers_d_appel = preparer_appels(" in source_reel
            and "interdites, appels, plafond_session, juge=juge)" in source_reel
            and 'sortie / "appels"' not in source_reel and "adaptateurs_reels_v56" not in source_reel)


# --- (c) mutation ---------------------------------------------------------------------------------------------------------------


LIGNE_V3 = '    return Path(os.path.realpath(os.path.abspath(str(sortie / "sortie")))) / "appels"\n'


def _mutant(tmp_path, ancien, nouveau, nom):
    src = CHEMIN_E3.read_text(encoding="utf-8")
    assert src.count(ancien) == 1
    p = tmp_path / f"{nom}.py"
    p.write_text(src.replace(ancien, nouveau), encoding="utf-8")
    return _charger(nom, p)


def test_mutation_sortie_appels_echoue_a_l_essai_neuf(epreuve_reelle_simulee, tmp_path):
    m = epreuve_reelle_simulee
    M = _mutant(tmp_path, LIGNE_V3, '    return sortie / "appels"\n', "epreuve_v3_mutant_appels")
    with pytest.raises(L.Refus, match="fiche voisine"):
        M.preparer_appels(m["v8"], m["fournisseurs"], m["sortie"], m["base"], m["plan"], TEMOINS, refus=L.Refus)
    # le v3 non muté passe sur les mêmes entrées
    E.preparer_appels(m["v8"], m["fournisseurs"], m["sortie"], m["base"], m["plan"], TEMOINS, refus=L.Refus)


def test_mutation_de_reel_vers_sortie_appels_echoue(tmp_path):
    M = _mutant(tmp_path, "interdites, appels, plafond_session, juge=juge)", 'interdites, sortie / "appels", plafond_session, juge=juge)',
                "epreuve_v3_mutant_reel")
    assert not cablage_conforme(inspect.getsource(M.reel))
