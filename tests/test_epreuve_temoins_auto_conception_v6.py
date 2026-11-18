"""Essais du programme d'épreuve des témoins v6 (lanceur v6, additif v2f) : les essais v5 portés ; toutes les fonctions
identiques à l'octet à celles de la v5 sauf `charger_lanceur` et `refuser_si_rapport_existe` ; `VERSION`, `LANCEUR` et les
deux chemins changent.

Texte des essais v5 :

Essais du programme d'épreuve des témoins v5 (tentative neuve de la course d'auto-conception, additif v2e) — hors ligne,
aucun appel, aucun relais réel, aucune clé, aucun réseau hors de la boucle locale.

(v5) Les essais du v4 portés au v5 (lanceur v5, chemins `course-v3/`, pièce de départ v2e remplie pour l'essai) ; fonctions du
    v4 identiques à l'octet ; puis les changements de la v5, chacun sain, artefact et mutation : rapport v5 déjà présent → refus
    avant tout ; mot de reprise du lanceur v5 exigé avant tout appel (et avant la sonde du bac) ; plafond de 5 USD entier sous la
    ligne neuve ; tentatives v3 et v4 rapportées à côté (empreintes épinglées vérifiées).

Texte des essais v4 :

(a) Les essais du v3 (`tests/test_epreuve_temoins_auto_conception_v3.py`) portés au v4 : lecture gelée, témoins, hors ligne
    de bout en bout, refus d'un environnement avec clé, câblage des dossiers d'appel sous la sortie interdite (adaptateurs
    **réels** de la copie épinglée, jusqu'à `construire_options`, fonction pure), mutations.
(b) Gardes neuves, chacune sur un cas sain et sur un artefact (R5), et une mutation par garde :
    - bac à sable sondé avant tout appel (`exiger_bac_a_sable`) : sain (sonde rendant actif et /proc neuf) ; artefacts (bac
      absent, /proc neuf absent) → refus ; et, dans `reel()`, la sonde précède la procédure des relais, la porte à blanc, la
      transmission des plafonds et le premier appel ;
    - borne du relais d'Argon (`verifier_borne_argon` et `verifier_procedure_relais` du lanceur v4 à 2 × appels + marge) :
      sain (24 pour 11 jugements) ; artefacts (15, la borne de la tentative v3 ; 23 ; état différent des arguments ; relais
      non neuf) → refus avant tout appel ;
    - manques techniques (`qualifier_verdict`) : la tentative v3 rejouée sur ses verdicts bruts et ses causes techniques → « non
      conclue » ; un verdict lu et faux à côté → « échouée » reste ; jamais « réussie » par requalification ;
    - rapport v4 déjà présent → refus avant tout (une reprise unique) ;
    - décision de reprise GO-2026-11-18-36 exigée au registre de main (type, auteur, période, périmètre) ; plafond de 5 USD
      au total, tentative v3 comprise (dépense lue dans son rapport scellé, retranchée ; budget transmis aux portes).
(c) `lire_epreuve` identique à l'octet à celle du v3 (et donc de la v2)."""
import hashlib
import importlib.util
import inspect
import json
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.dont_write_bytecode = True
RACINE = Path(__file__).resolve().parents[1]


def _charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


L = _charger("lancer_course_auto_conception_v6", RACINE / "scripts" / "lancer_course_auto_conception_v6.py")
CHEMIN_E4 = RACINE / "scripts" / "epreuve_temoins_auto_conception_v6.py"   # v5 : le programme essayé (nom gardé pour les mutants)
E = _charger("epreuve_temoins_auto_conception_v6", CHEMIN_E4)
E3 = _charger("epreuve_temoins_auto_conception_v3_pour_essai_v6", RACINE / "scripts" / "epreuve_temoins_auto_conception_v3.py")
E4 = _charger("epreuve_temoins_auto_conception_v4_pour_essai_v6", RACINE / "scripts" / "epreuve_temoins_auto_conception_v4.py")
E5 = _charger("epreuve_temoins_auto_conception_v5_pour_essai_v6", RACINE / "scripts" / "epreuve_temoins_auto_conception_v5.py")

FIXE = json.loads((RACINE / L.PIECES["configuration"][0]).read_text())
TEMOINS = {t["id"]: t for t in json.loads((RACINE / L.PIECES["temoins"][0]).read_text())["temoins"]}
ITEMS = FIXE["items_juge"]
COURSE = RACINE / "docs/notes/organisme-auto-conception-v1/course-v2"
DECL_EPREUVE_V3 = COURSE / "declaration-relais-epreuve-temoins-auto-conception-v3.json"
RAPPORT_V3 = COURSE / "epreuve-temoins-reelle-auto-conception-v3.json"


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
    if str(ORCH) not in sys.path:
        sys.path.insert(0, str(ORCH))
    return _charger("ideation_v8_pour_essai_epreuve_v6", ORCH / L.LANCEUR_ORCHESTRATEUR)


def _verdicts(fonction):
    out = {}
    for tid, t in TEMOINS.items():
        its = fonction(t)
        out[tid] = {"items": its, "notable": all(its.values())}
    return out


def _mutant(tmp_path, ancien, nouveau, nom):
    src = CHEMIN_E4.read_text(encoding="utf-8")
    assert src.count(ancien) == 1, ancien
    p = tmp_path / f"{nom}.py"
    p.write_text(src.replace(ancien, nouveau), encoding="utf-8")
    return _charger(nom, p)


# --- (a) essais portés du v3 ---------------------------------------------------------------------------------------------------


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
    assert s["regle_de_seuil_sur_le_champ_lu_erreurs_min"] >= 1
    if MATIERE is not None:
        assert s["identifiants_absents_de_la_matiere"] == []


@avec_matiere
@avec_orchestrateur
def test_epreuve_hors_ligne_bout_en_bout(tmp_path):
    m = tmp_path / "matiere-v3.md"
    m.write_bytes(MATIERE)
    rap = E.hors_ligne(tmp_path / "epreuve", m, E.orchestrateur_present(L.ORCHESTRATEURS_CANDIDATS))
    assert rap["version"] == "epreuve_temoins_auto_conception_v6"
    assert rap["conclusion"]["verdict"] == "témoins éprouvés hors ligne"
    assert rap["lectures"]["parfait"]["verdict"] == "réussie" and rap["juges_au_hasard_reussis"] == 0
    assert all(rap["lectures"][n]["verdict"] == "échouée" for n in ("longueur", "indulgent", "severe", "champ"))
    assert rap["artefact_aiguilleur_tout_concret"] == "échouée"


def test_epreuve_reelle_refuse_un_environnement_avec_cle(monkeypatch):
    monkeypatch.setenv("UNE_API_KEY", "x")
    with pytest.raises(Exception) as e:
        E.reel()
    assert type(e.value).__name__ == "Refus" and "UNE_API_KEY" in str(e.value)


@pytest.mark.parametrize("nom", ["lire_epreuve", "verite", "jouer", "servir", "identifiant_servi", "controles_statiques", "hors_ligne",
                                 "charger_orchestrateur", "fiche_servie", "JugeFactice", "AiguilleurFactice", "ecrire_scelle",
                                 "dossier_des_appels", "verifier_dossiers_d_appel", "preparer_appels", "orchestrateur_present"])
def test_fonctions_identiques_au_v3(nom):
    assert inspect.getsource(getattr(E, nom)) == inspect.getsource(getattr(E3, nom))


def test_lire_epreuve_identique_a_l_octet():
    assert inspect.getsource(E.lire_epreuve).encode("utf-8") == inspect.getsource(E3.lire_epreuve).encode("utf-8")


def test_constantes_identiques_au_v3_sauf_les_chemins_neufs():
    for nom in ("PLAFOND_EPREUVE_USD", "TEMOINS", "CONSIGNE_JUGE", "CONSIGNE_AIGUILLEUR", "CONSIGNE_PROPOSEUR", "CONFIGURATION",
                "ETAPE", "RACINE_GRAINES", "CHAMP_LU", "N_JUGES_AU_HASARD", "BORNE_CHAMP", "BORNE_CARTE"):
        assert getattr(E, nom) == getattr(E3, nom), nom
    assert E.DECLARATION_EPREUVE == RACINE / L.COURSE_V3 / "declaration-relais-epreuve-temoins-auto-conception-v6.json"
    assert E.RAPPORT_REEL == RACINE / L.COURSE_V3 / "epreuve-temoins-reelle-auto-conception-v6.json"
    assert E.LANCEUR.name == "lancer_course_auto_conception_v6.py" and E.RAPPORT_TENTATIVE_V3 == RAPPORT_V3
    assert E.RAPPORT_TENTATIVE_V4 == COURSE / "epreuve-temoins-reelle-auto-conception-v4.json"
    assert E.SHA_TENTATIVE_V4 == "980e888898c180b347d526d75bdc41d531ec26943c043a96e44c24c0853337be"
    for nom in ("GO_REPRISE", "SHA_TENTATIVE_V3", "STATUTS_TECHNIQUES", "MOTIF_NON_PARTI", "ID_CATALOGUE"):
        assert getattr(E, nom) == getattr(E4, nom), nom
    # (pas d'essai d'absence des fichiers réels : la session d'exécution les écrit ; l'essai v3 du même nom échoue depuis
    # l'épreuve v3 pour cette seule raison)


GABARIT_V2E = RACINE / L.COURSE_V3 / "piece-de-depart-gabarit-auto-conception-v2f.json"   # v6 : gabarit v2f


def piece_v2e_remplie(tmp_path) -> Path:
    """v5 : le gabarit v2e rempli pour l'essai (lignes de GO neuves, mot de reprise, crédit, sonde nommée), scellé hors dépôt."""
    o = json.loads(GABARIT_V2E.read_text(encoding="utf-8"))
    o.update(statut="rempli pour l'essai", go_course="GO-2026-11-19-01", go_epreuve="GO-2026-11-19-02",
             credit_declare_cle_claude_usd=150.0, ecrit_le="2026-11-19T08:00:00Z")
    o["tentative_neuve"]["mot_de_reprise"] = "GO-2026-11-19-01"
    o["especes_optionnelles"]["astra"].update(sonde_du_jour="essai", sonde_du_jour_rapport="docs/x/sonde-essai.json")
    p = tmp_path / "piece-de-depart-auto-conception-v2e.json"
    p.write_text(json.dumps(o, ensure_ascii=False, indent=1), encoding="utf-8")
    Path(str(p) + ".sha256").write_text(f"{L.sha256_fichier(p)}  {p.name}\n", encoding="utf-8")
    return p


def fournisseurs_epreuve(tmp_path) -> dict:
    r = L.Reglages.production()
    r.piece_de_depart = piece_v2e_remplie(tmp_path)                       # v5 : la pièce neuve n'existe qu'au remplissage
    depart = L.verifier_piece_de_depart(r)
    decl = L.verifier_declaration(json.loads(DECL_EPREUVE_V3.read_text(encoding="utf-8")), FIXE, depart)
    arrets = tmp_path / "arrets-credit"
    arrets.mkdir()
    decl = L.envelopper_commandes(decl, sys.executable, RACINE / L.PIECES["garde_credit"][0], arrets)
    assert sorted(decl["fournisseurs"]) == ["argon", "claude"]
    return decl["fournisseurs"]


def plan_epreuve() -> list:
    ps = FIXE["plafonds_session"]
    return [("aiguilleur", FIXE["aiguilleur"], "ca", float(ps["aiguilleur"]), False)] + \
        [(j["etiquette"], j, "cj", float(ps["juge"]), True) for j in FIXE["juges"]]


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


def test_v4_sain_chaque_role_de_l_epreuve(epreuve_reelle_simulee):
    m = epreuve_reelle_simulee
    ads, portes, appels, controle = E.preparer_appels(m["v8"], m["fournisseurs"], m["sortie"], m["base"], m["plan"], TEMOINS,
                                                      refus=L.Refus)
    assert appels == Path(os.path.realpath(m["sortie"])) / "sortie" / "appels"
    assert sorted(controle) == sorted(["aiguilleur"] + [j["etiquette"] for j in FIXE["juges"]])
    assert not (m["sortie"] / "sortie").exists()


def test_artefact_dossier_hors_chemin_interdit_refuse(epreuve_reelle_simulee):
    m = epreuve_reelle_simulee
    ads, _ = m["v8"].adaptateurs_reels_v56({"fournisseurs": m["fournisseurs"]}, str(m["sortie"] / "sortie"), m["base"])
    with pytest.raises(L.Refus, match="refusé par la garde de l'orchestrateur avant tout appel"):
        E.verifier_dossiers_d_appel(ads, m["plan"], TEMOINS, m["sortie"] / "appels", refus=L.Refus)


# --- (b1) bac à sable sondé avant tout appel -------------------------------------------------------------------------------------


def _faux_orchestrateur_bac(tmp_path, actif, proc_neuf):
    """Une copie factice qui ne contient que `pole/adaptateurs.py` avec `etat_bac_a_sable_detaille`, comme la sonde du lanceur
    l'importe (sous-processus `-I -B`)."""
    o = tmp_path / f"orch-bac-{actif}-{proc_neuf}"
    (o / "pole").mkdir(parents=True)
    (o / "pole" / "__init__.py").write_text("", encoding="utf-8")
    (o / "pole" / "adaptateurs.py").write_text(
        "def etat_bac_a_sable_detaille():\n"
        f"    return {{'actif': {actif}, 'proc_neuf': {proc_neuf}, 'motif': 'faux bac (essai)'}}\n", encoding="utf-8")
    return o


def _reglages_sonde(exiger=True):
    r = L.Reglages.production()
    r.exiger_bac_a_sable = exiger
    return r


ENV_SONDE = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8"}


def test_bac_sain_accepte(tmp_path):
    etat = E.exiger_bac_a_sable(L, _reglages_sonde(), _faux_orchestrateur_bac(tmp_path, True, True), ENV_SONDE)
    assert etat["actif"] is True and etat["proc_neuf"] is True


@pytest.mark.parametrize("actif,proc_neuf", [(False, False), (True, False)])
def test_bac_absent_ou_sans_proc_neuf_refuse(tmp_path, actif, proc_neuf):
    with pytest.raises(L.Refus, match="bac à sable"):
        E.exiger_bac_a_sable(L, _reglages_sonde(), _faux_orchestrateur_bac(tmp_path, actif, proc_neuf), ENV_SONDE)
    # même si le réglage du lanceur n'exigeait pas le bac : l'épreuve l'exige elle-même
    with pytest.raises(L.Refus, match="bac à sable"):
        E.exiger_bac_a_sable(L, _reglages_sonde(False), _faux_orchestrateur_bac(tmp_path / "b", actif, proc_neuf), ENV_SONDE)


@avec_orchestrateur
def test_bac_sonde_reelle_de_l_orchestrateur_epingle():
    """La sonde réelle (commande de l'orchestrateur épinglé). Dans ce conteneur, le bac est installé : elle doit passer. Si
    bwrap manque, elle doit refuser — les deux issues sont acceptées, jamais une sonde muette."""
    import shutil
    if shutil.which("bwrap") and shutil.which("socat"):
        etat = E.exiger_bac_a_sable(L, _reglages_sonde(), ORCH, ENV_SONDE)
        assert etat["actif"] is True and etat["proc_neuf"] is True
    else:
        with pytest.raises(L.Refus, match="bac à sable"):
            E.exiger_bac_a_sable(L, _reglages_sonde(), ORCH, ENV_SONDE)


def test_environnement_de_sonde_sans_cle():
    env = E.environnement_de_sonde({"PATH": "/bin", "HOME": "/h", "UNE_API_KEY": "x", "GEMINI_API_KEY": "y", "LANG": "C"})
    assert env == {"PATH": "/bin", "HOME": "/h", "LANG": "C"}


def _positions(src, *motifs):
    return [src.index(m) for m in motifs]


def test_reel_sonde_le_bac_avant_les_relais_les_portes_la_transmission_et_les_appels():
    src = inspect.getsource(E.reel)
    p = _positions(src, "exiger_bac_a_sable(", "verifier_procedure_relais(", "porte_a_blanc(", "preparer_appels(", ".transmettre(",
                   "jouer_avec_incidents(")
    assert p == sorted(p)


def test_mutation_bac_sans_exigence_attrapee(tmp_path):
    M = _mutant(tmp_path, '    if not (etat.get("actif") is True and etat.get("proc_neuf") is True):\n',
                '    if False:\n', "epreuve_v6_mutant_bac")
    # le lanceur n'exige pas le bac (réglage d'essai) : seule la garde de l'épreuve tient ; mutée, elle laisse passer
    M.exiger_bac_a_sable(L, _reglages_sonde(False), _faux_orchestrateur_bac(tmp_path, False, False), ENV_SONDE)
    with pytest.raises(L.Refus):
        E.exiger_bac_a_sable(L, _reglages_sonde(False), _faux_orchestrateur_bac(tmp_path / "b", False, False), ENV_SONDE)


def test_mutation_reel_sans_sonde_attrapee(tmp_path):
    M = _mutant(tmp_path, '    bac = exiger_bac_a_sable(L, r, Path(orch["chemin"]), environnement_de_sonde(os.environ))\n',
                '    bac = {"actif": None}\n', "epreuve_v6_mutant_reel_bac")
    assert "exiger_bac_a_sable(" not in inspect.getsource(M.reel)
    with pytest.raises(ValueError):
        _positions(inspect.getsource(M.reel), "exiger_bac_a_sable(")


# --- (b2) borne du relais d'Argon ------------------------------------------------------------------------------------------------


def _procedure(args, etat, appels=0):
    return {"relais_vivants": {"argon": {"max_appels": args, "etat": {"appels": appels, "max_appels": etat,
                                                                       "variable_cle_encore_presente": False}}}}


def test_borne_requise_chiffree():
    n = len(TEMOINS) * sum(1 for j in FIXE["juges"] if j["fournisseur"] == "argon")
    assert n == 11 and L.appels_relais_gemini_requis(n) == 24 == 2 * 11 + L.MARGE_APPELS_RELAIS_GEMINI


def test_borne_argon_saine():
    assert E.verifier_borne_argon(_procedure(24, 24), 24, L.Refus) == {"max_appels_args": 24, "max_appels_etat": 24, "requis": 24}
    assert E.verifier_borne_argon(_procedure(30, 30), 24, L.Refus)["max_appels_args"] == 30


@pytest.mark.parametrize("args,etat,appels,motif", [(15, 15, 0, "15"), (23, 23, 0, "23"), (24, 15, 0, "état"),
                                                     (24, None, 0, "illisible"), (None, 24, 0, "illisible"),
                                                     (24, 24, 1, "non neuf")])
def test_borne_argon_artefacts_refuses(args, etat, appels, motif):
    with pytest.raises(L.Refus, match=motif):
        E.verifier_borne_argon(_procedure(args, etat, appels), 24, L.Refus)


def test_tentative_v3_aurait_ete_refusee_avant_tout_appel():
    """La procédure scellée du rapport v3 (borne 15, lue par PID et par l'état) est refusée par la garde v4."""
    proc = json.loads(RAPPORT_V3.read_text(encoding="utf-8"))["procedure"]
    with pytest.raises(L.Refus, match="15"):
        E.verifier_borne_argon(proc, L.appels_relais_gemini_requis(11), L.Refus)


def test_controle_du_relais_argon_par_pid_a_la_borne_doublee():
    """`controler_relais_argon` du lanceur v4, appelé par `verifier_procedure_relais` avec la borne de l'épreuve : arguments lus
    par PID (factices), état factice ; 15 refusé, 24 accepté."""
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        prog = Path(d) / "relais_gemini_v2.py"
        prog.write_text("# factice\n", encoding="utf-8")
        for borne, ok in ((15, False), (23, False), (24, True)):
            r = L.Reglages.production()
            r.programmes_relais = dict(L.PROGRAMMES_RELAIS, argon=("relais_gemini_v2.py", L.sha256_fichier(prog)))
            r.lire_cmdline = lambda pid, b=borne: [sys.executable, str(prog), "--port", "8788", "--max-appels", str(b),
                                                   "--modele", "gemini-4-argon", "--variable-cle", "GEMINI_API_KEY"]
            r.lire_etat_relais = lambda url, b=borne: {"appels": 0, "max_appels": b, "variable_cle_encore_presente": False}
            b = {"type": "commande_externe", "nom_cle": "GEMINI_API_KEY"}
            meta = {"pid_relais": 4242, "url_etat_relais": "http://127.0.0.1:8788"}
            if ok:
                assert L.controler_relais_argon(r, b, meta, L.appels_relais_gemini_requis(11))["max_appels"] == borne
            else:
                with pytest.raises(L.Refus, match="countTokens"):
                    L.controler_relais_argon(r, b, meta, L.appels_relais_gemini_requis(11))


def test_reel_exige_la_borne_doublee_avant_la_porte():
    src = inspect.getsource(E.reel)
    assert "requis_argon = L.appels_relais_gemini_requis(n_argon)" in src
    assert "L.verifier_procedure_relais(r, decl, pieces, fixe, requis_argon," in src
    p = _positions(src, "verifier_borne_argon(", "porte_a_blanc(", ".transmettre(", "jouer_avec_incidents(")
    assert p == sorted(p)


def test_mutation_borne_simple_attrapee(tmp_path):
    M = _mutant(tmp_path, "        if v < requis:\n", "        if v < requis // 2:\n", "epreuve_v6_mutant_borne")
    M.verifier_borne_argon(_procedure(15, 15), 24, L.Refus)          # la mutation laisse passer la borne de la tentative v3
    with pytest.raises(L.Refus):
        E.verifier_borne_argon(_procedure(15, 15), 24, L.Refus)


def test_mutation_reel_borne_non_doublee_attrapee(tmp_path):
    M = _mutant(tmp_path, "    requis_argon = L.appels_relais_gemini_requis(n_argon)\n", "    requis_argon = n_argon\n",
                "epreuve_v6_mutant_reel_borne")
    assert "requis_argon = L.appels_relais_gemini_requis(n_argon)" not in inspect.getsource(M.reel)


# --- (b3) manques techniques → « non conclue » ---------------------------------------------------------------------------------


def _v3_brut():
    o = json.loads(RAPPORT_V3.read_text(encoding="utf-8"))
    return o["verdicts"], o["classes"]


def _incidents_v3():
    """Causes techniques de la tentative v3 (sortie d'erreur versée et journal du relais) : aucun appel Claude parti (bac
    absent) ; Argon t08 à t11 refusés par le relais (429)."""
    inc = {"aiguilleur": {t: {"statut": "erreur"} for t in TEMOINS}, "juge-opus": {t: {"statut": "erreur"} for t in TEMOINS},
           "juge-argon": {t: {"statut": "erreur"} for t in ("t08", "t09", "t10", "t11")}}
    return inc


def test_tentative_v3_requalifiee_non_conclue_sans_toucher_la_lecture():
    verdicts, classes = _v3_brut()
    lecture = E.lire_epreuve(verdicts, classes, TEMOINS, ITEMS)
    assert lecture["verdict"] == "échouée"                                  # lecture gelée : inchangée
    sortes = E.manques_par_sorte(lecture, _incidents_v3())
    assert sortes["autres"] == [] and len(sortes["techniques"]) == 11 + 11 + 4
    assert E.qualifier_verdict(lecture, _incidents_v3(), None, [], True) == "non conclue"
    assert lecture["par_juge"]["juge-argon"]["manques"] == [{"temoin": t, "motif": "verdict illisible ou absent"}
                                                            for t in ("t08", "t09", "t10", "t11")]


def test_sans_incident_la_tentative_v3_reste_echouee():
    verdicts, classes = _v3_brut()
    lecture = E.lire_epreuve(verdicts, classes, TEMOINS, ITEMS)
    assert E.qualifier_verdict(lecture, {}, None, [], True) == "échouée"
    partiels = _incidents_v3()
    del partiels["juge-argon"]["t11"]
    assert E.qualifier_verdict(lecture, partiels, None, [], True) == "échouée"   # un manque non technique suffit


def test_verdict_lu_et_faux_a_cote_d_incidents_reste_echouee():
    a = {tid: "niveau_methode" for tid in TEMOINS}
    v = {"juge-opus": _verdicts(lambda t: E.verite(t, ITEMS)), "juge-argon": _verdicts(lambda t: {k: True for k in ITEMS})}
    v["juge-opus"]["t02"] = None
    lecture = E.lire_epreuve(v, a, TEMOINS, ITEMS)
    inc = {"juge-opus": {"t02": {"statut": "erreur"}}}
    assert E.manques_par_sorte(lecture, inc)["autres"]
    assert E.qualifier_verdict(lecture, inc, None, [], True) == "échouée"


def test_jamais_reussie_par_requalification():
    a = {tid: "niveau_methode" for tid in TEMOINS}
    parfait = {"juge-opus": _verdicts(lambda t: E.verite(t, ITEMS)), "juge-argon": _verdicts(lambda t: E.verite(t, ITEMS))}
    lecture = E.lire_epreuve(parfait, a, TEMOINS, ITEMS)
    assert E.qualifier_verdict(lecture, _incidents_v3(), None, [], True) == "réussie"   # aucun manque : rien à requalifier
    for tid in TEMOINS:
        parfait["juge-argon"][tid] = None
    lecture = E.lire_epreuve(parfait, a, TEMOINS, ITEMS)
    assert E.qualifier_verdict(lecture, {"juge-argon": {t: {} for t in TEMOINS}}, None, [], True) == "non conclue"
    assert E.qualifier_verdict(lecture, {}, None, [], True) == "échouée"


def test_regles_du_v3_gardees():
    a = {tid: "niveau_methode" for tid in TEMOINS}
    parfait = {"juge-opus": _verdicts(lambda t: E.verite(t, ITEMS)), "juge-argon": _verdicts(lambda t: E.verite(t, ITEMS))}
    lecture = E.lire_epreuve(parfait, a, TEMOINS, ITEMS)
    assert E.qualifier_verdict(lecture, {}, "plafond", [], True) == "non conclue"
    assert E.qualifier_verdict(lecture, {}, None, ["juge-opus"], True) == "non conclue"
    assert E.qualifier_verdict(lecture, {}, None, [], False) == "non conclue"


class _Ad:
    def __init__(self, statuts):
        self.statuts, self.k = list(statuts), 0

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        s = self.statuts[self.k]
        self.k += 1
        texte = '```json\n{"classe": "niveau_methode", "categorie": "x"}\n```' if s == "ok" else ""
        return SimpleNamespace(statut=s, texte_brut=texte, texte_final=texte, cout_declare_usd=0.0, modele_servi="m" if s == "ok" else None,
                               erreur="sandbox required but unavailable" if s == "erreur" else None)


def test_jouer_avec_incidents_consigne_le_statut_technique_seulement(tmp_path):
    o = {"entree_une_fiche": lambda consigne, fiche, interdites, mode, ident: "entrée",
         "lire_classe": lambda texte: ("niveau_methode", None), "lire_verdict": lambda texte, items: None}
    trois = dict(list(sorted(TEMOINS.items()))[:4])
    lus, cout, servis, statuts, inc = E.jouer_avec_incidents(o, _Ad(["ok", "erreur", "refus", "tours_epuises"]), "aiguilleur", "m",
                                                             "c", trois, ITEMS, [], tmp_path, 0.25, juge=False, L=L)
    ids = sorted(trois)
    assert lus[ids[0]] == "niveau_methode" and all(lus[t] is None for t in ids[1:])
    assert statuts == dict(zip(ids, ["ok", "erreur", "refus", "tours_epuises"]))
    assert list(inc) == [ids[1]] and inc[ids[1]]["statut"] == "erreur" and "sandbox" in inc[ids[1]]["erreur"]


def test_reel_qualifie_sans_toucher_lire_epreuve():
    src = inspect.getsource(E.reel)
    assert "lecture = lire_epreuve(verdicts, classes, temoins, items)" in src
    assert 'lecture["verdict"] = qualifier_verdict(lecture, incidents, motif_arret, changes' in src
    assert '"verdict_lecture_gelee": verdict_lecture_gelee' in src and '"tentatives_precedentes": tentatives_precedentes()' in src


def test_mutation_requalification_trop_large_attrapee(tmp_path):
    M = _mutant(tmp_path, '        if sortes["techniques"] and not sortes["autres"]:\n', '        if sortes["techniques"]:\n',
                "epreuve_v6_mutant_qualif")
    verdicts, classes = _v3_brut()
    lecture = E.lire_epreuve(verdicts, classes, TEMOINS, ITEMS)
    partiels = _incidents_v3()
    del partiels["juge-argon"]["t11"]
    assert M.qualifier_verdict(lecture, partiels, None, [], True) == "non conclue"     # muté : masque un manque non technique
    assert E.qualifier_verdict(lecture, partiels, None, [], True) == "échouée"


def test_mutation_requalification_absente_attrapee(tmp_path):
    M = _mutant(tmp_path, '            return "non conclue"\n    return v\n', '            pass\n    return v\n', "epreuve_v6_mutant_qualif2")
    verdicts, classes = _v3_brut()
    lecture = E.lire_epreuve(verdicts, classes, TEMOINS, ITEMS)
    assert M.qualifier_verdict(lecture, _incidents_v3(), None, [], True) == "échouée"
    assert E.qualifier_verdict(lecture, _incidents_v3(), None, [], True) == "non conclue"


# --- (b4) rapport v4 déjà présent ----------------------------------------------------------------------------------------------


def test_rapport_v4_absent_sain_et_present_refuse(tmp_path, monkeypatch):
    faux = tmp_path / "epreuve-temoins-reelle-auto-conception-v4.json"
    monkeypatch.setattr(E, "RAPPORT_REEL", faux)
    E.refuser_si_rapport_existe(L.Refus)                                      # sain : absent
    faux.write_text("{}", encoding="utf-8")
    with pytest.raises(L.Refus, match="déjà été jouée"):
        E.refuser_si_rapport_existe(L.Refus)
    faux.unlink()
    Path(str(faux) + ".sha256").write_text("x", encoding="utf-8")
    with pytest.raises(L.Refus, match="déjà été jouée"):
        E.refuser_si_rapport_existe(L.Refus)


def test_reel_refuse_le_rapport_existant_avant_tout(monkeypatch, tmp_path):
    faux = tmp_path / "epreuve-temoins-reelle-auto-conception-v4.json"
    faux.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(E, "RAPPORT_REEL", faux)
    for n in [n for n in os.environ if n in L.NOMS_DE_CLE or L.MOTIF_NOM_DE_CLE.search(n)]:
        monkeypatch.delenv(n)
    with pytest.raises(Exception) as e:
        E.reel()                     # `reel()` recharge le lanceur v4 : sa classe Refus est neuve, on la reconnaît par son nom
    assert type(e.value).__name__ == "Refus" and "déjà été jouée" in str(e.value)


def test_mutation_sans_garde_du_rapport_attrapee(tmp_path, monkeypatch):
    M = _mutant(tmp_path, "    refuser_si_rapport_existe(L.Refus)                                       # v5 : une seule épreuve à ce chemin\n",
                "", "epreuve_v6_mutant_rapport")
    assert "refuser_si_rapport_existe(" not in inspect.getsource(M.reel)
    src = inspect.getsource(E.reel)
    assert src.index("refuser_si_rapport_existe(") < src.index("L.Reglages.production()")


def test_tentative_precedente_rapportee():
    t = E.tentative_precedente()
    assert t["present"] and t["sha256"] == L.sha256_fichier(RAPPORT_V3) and t["verdict_ecrit"] == "échouée"
    assert t["cout_usd"] == 0.132289 and sorted(k for k, v in t["verdicts"]["juge-argon"].items() if v) == \
        ["t01", "t02", "t03", "t04", "t05", "t06", "t07"]


# --- (b5, v5) tentative neuve : fonctions du v4 identiques, mot de reprise du lanceur v5, plafond entier, tentatives rapportées -


@pytest.mark.parametrize("nom", ["exiger_bac_a_sable", "environnement_de_sonde", "verifier_borne_argon", "_motif_court",
                                 "jouer_avec_incidents", "manques_par_sorte", "qualifier_verdict", "verifier_mot_de_reprise",
                                 "depense_tentative_v3", "budget_de_la_reprise", "tentative_precedente", "lire_epreuve", "verite",
                                 "jouer", "servir", "controles_statiques", "hors_ligne", "preparer_appels",
                                 "verifier_dossiers_d_appel", "dossier_des_appels", "JugeFactice", "AiguilleurFactice"])
def test_fonctions_identiques_au_v4(nom):
    assert inspect.getsource(getattr(E, nom)) == inspect.getsource(getattr(E4, nom))


def test_tentatives_precedentes_rapportees_v3_et_v4():
    t = E.tentatives_precedentes()
    assert [x["version"] for x in t] == ["v3", "v4"] and all(x["present"] and x["conforme"] for x in t)
    v3, v4 = t
    assert v3["sha256"] == E.SHA_TENTATIVE_V3 and v3["verdict_ecrit"] == "échouée" and v3["cout_usd"] == 0.132289
    assert v4["sha256"] == E.SHA_TENTATIVE_V4 and v4["verdict_ecrit"] == "réussie" and v4["cout_usd"] == 1.204591
    assert v3["go"] == v4["go"] == "GO-2026-11-18-21" and v4["horodatage_utc"].startswith("2026-11-18")
    assert sorted(v4["verdicts"]) == ["juge-argon", "juge-opus"] and len(v4["classes"]) == 11


def test_tentative_d_une_autre_empreinte_dite_jamais_masquee(tmp_path, monkeypatch):
    faux = tmp_path / "epreuve-temoins-reelle-auto-conception-v4.json"
    faux.write_bytes(E.RAPPORT_TENTATIVE_V4.read_bytes() + b"\n")
    monkeypatch.setattr(E, "RAPPORT_TENTATIVE_V4", faux)
    v4 = E.tentatives_precedentes()[1]
    assert v4["present"] and v4["conforme"] is False and v4["sha256_epingle"] == E.SHA_TENTATIVE_V4 and "verdicts" not in v4
    monkeypatch.setattr(E, "RAPPORT_TENTATIVE_V4", tmp_path / "absent.json")
    assert E.tentatives_precedentes()[1] == {"chemin": str(tmp_path / "absent.json"), "present": False, "version": "v4"}


def test_mutation_tentative_v4_omise_attrapee(tmp_path):
    M = _mutant(tmp_path, '            dict(_resume_tentative(RAPPORT_TENTATIVE_V4, SHA_TENTATIVE_V4), version="v4")]\n',
                "            ]\n", "epreuve_v6_mutant_tentatives")
    assert [x["version"] for x in M.tentatives_precedentes()] == ["v3"]          # muté : l'épreuve v4 disparaîtrait du rapport
    assert [x["version"] for x in E.tentatives_precedentes()] == ["v3", "v4"]


def test_reel_v5_mot_de_reprise_avant_tout_appel_et_plafond_entier():
    src = inspect.getsource(E.reel)
    assert 'mot_de_reprise = L.verifier_mot_de_reprise(registre["texte"], aujourd_hui, depart)' in src
    assert "budget = PLAFOND_EPREUVE_USD\n" in src and "p.transmettre(ETAPE, budget)" in src
    assert "if cumul + plafond_session > budget + 1e-9:" in src
    # la reprise v4 (GO-2026-11-18-36, retranchement de la tentative v3) n'est plus jouée par `reel`
    for ancien in ("verifier_mot_de_reprise(registre[\"texte\"], aujourd_hui, L.Refus)", "depense_tentative_v3(",
                   "budget_de_la_reprise(", "tentative_precedente()"):
        assert ancien not in src, ancien
    p = _positions(src, "refuser_si_rapport_existe(", "L.verifier_piece_de_depart(", "L.verifier_go(", "L.verifier_mot_de_reprise(",
                   "exiger_bac_a_sable(", "verifier_procedure_relais(", "porte_a_blanc(", ".transmettre(", "jouer_avec_incidents(")
    assert p == sorted(p)
    assert '"tentatives_precedentes": tentatives_precedentes()' in src and '"budget_epreuve_usd": budget' in src


def test_mutation_reel_sans_mot_de_reprise_attrapee(tmp_path):
    M = _mutant(tmp_path, '    mot_de_reprise = L.verifier_mot_de_reprise(registre["texte"], aujourd_hui, depart)\n',
                '    mot_de_reprise = None\n', "epreuve_v6_mutant_mot")
    assert "verifier_mot_de_reprise(" not in inspect.getsource(M.reel)
    assert "L.verifier_mot_de_reprise(" in inspect.getsource(E.reel)


def test_mot_de_reprise_du_lanceur_v5_sain_et_artefacts():
    """La garde que `reel` appelle (`verifier_mot_de_reprise` du lanceur v5) : saine sur la ligne neuve qui dit « tentative
    neuve », refusée sans ces mots, sur une ligne consommée, ou différente de la ligne de la course."""
    import datetime as _dt
    ligne = ("| GO-2026-11-19-01 | 2026-11-19 | calcul | Course d'auto-conception de l'organisme d'idéation, tentative neuve | "
             "90 USD | 2026-11-22 | Lazar | R-1 |")
    depart = {"go_course": "GO-2026-11-19-01", "tentative_neuve": {"course_close": L.COURSE_CLOSE_ADMISE[0],
                                                                   "mot_de_reprise": "GO-2026-11-19-01"}}
    jour = _dt.date(2026, 11, 19)
    assert L.verifier_mot_de_reprise(ligne + "\n", jour, depart)["id"] == "GO-2026-11-19-01"
    with pytest.raises(L.Refus, match="tentative neuve"):
        L.verifier_mot_de_reprise(ligne.replace(", tentative neuve", "") + "\n", jour, depart)
    with pytest.raises(L.Refus, match="différent"):
        L.verifier_mot_de_reprise(ligne + "\n", jour, dict(depart, go_course="GO-2026-11-19-03"))
    consommee = {"go_course": "GO-2026-11-18-20", "tentative_neuve": {"mot_de_reprise": "GO-2026-11-18-20"}}
    with pytest.raises(L.Refus, match="consommée"):
        L.verifier_mot_de_reprise(ligne.replace("GO-2026-11-19-01", "GO-2026-11-18-20") + "\n", jour, consommee)


def test_reel_refuse_sans_piece_de_depart_neuve_avant_tout(monkeypatch, tmp_path):
    """Dans le dépôt tel qu'il est (pièce de départ v2e non encore écrite), `reel()` s'arrête à la pièce : aucun appel."""
    if (RACINE / L.PIECE_DE_DEPART).exists():
        pytest.skip("pièce de départ v2e déjà écrite par la session d'exécution")
    monkeypatch.setattr(E, "RAPPORT_REEL", tmp_path / "absent.json")
    for n in [n for n in os.environ if n in L.NOMS_DE_CLE or L.MOTIF_NOM_DE_CLE.search(n)]:
        monkeypatch.delenv(n)
    with pytest.raises(Exception) as e:
        E.reel()
    assert type(e.value).__name__ == "Refus" and "pièce de départ" in str(e.value)


def test_v6_fonctions_toutes_identiques_a_la_v5_et_constantes():
    for nom, objet in vars(E5).items():
        if (inspect.isfunction(objet) or inspect.isclass(objet)) and getattr(objet, "__module__", None) == E5.__name__ \
                and nom not in ("charger_lanceur", "refuser_si_rapport_existe"):     # nom du module du lanceur ; message
            assert inspect.getsource(getattr(E, nom)) == inspect.getsource(objet), nom
    for nom in ("PLAFOND_EPREUVE_USD", "TEMOINS", "CONFIGURATION", "RAPPORT_TENTATIVE_V3", "RAPPORT_TENTATIVE_V4", "SHA_TENTATIVE_V3",
                "SHA_TENTATIVE_V4", "STATUTS_TECHNIQUES", "RACINE_GRAINES", "CHAMP_LU", "ETAPE"):
        assert getattr(E, nom) == getattr(E5, nom), nom
    assert (E.VERSION, E.LANCEUR.name) == ("epreuve_temoins_auto_conception_v6", "lancer_course_auto_conception_v6.py")
    assert E.RAPPORT_REEL != E5.RAPPORT_REEL and E.DECLARATION_EPREUVE != E5.DECLARATION_EPREUVE
