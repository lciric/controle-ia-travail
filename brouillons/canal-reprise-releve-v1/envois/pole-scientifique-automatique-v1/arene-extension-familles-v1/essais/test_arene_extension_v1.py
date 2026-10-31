"""Essais de `arene_extension_v1.py` : chaque garde (R5) avec un cas sain et un artefact, vérifiés par leur motif ;
contrôle par l'arbre syntaxique qu'aucune garde n'est sans essai nommé ; refus des racines déjà employées (liste
recoupée avec le dossier de l'arène) ; certificats de non-couverture vérifiés indépendamment (recherche sur la sphère,
moniteur riche d'une vue, Monte-Carlo) ; selle de la couche exacte vérifiée des deux côtés ; union exacte contre
Monte-Carlo ; Q3b : identités, formule contre Monte-Carlo, taux de fausses alertes exact du partage ; reproductibilité
bit à bit ; témoins PUR et U ; attaquant indépendant ; arrêt par PID ; refus de la décision sans calcul décisif du
pilote principal ni préenregistrement scellé, pour la bonne raison, sur des copies temporaires.
Racines des essais du code seulement : RACINE_TESTS = 20265001, RACINE_TESTS_BIS = 20265002.

Les essais du scellement écrivent des fichiers et leurs compagnons `.sha256` dans le dossier temporaire de pytest
(hors dépôt), jamais dans le dépôt.

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider \
        brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-extension-familles-v1/essais/test_arene_extension_v1.py
"""
from __future__ import annotations

import ast
import json
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from dataclasses import asdict
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from scipy.optimize import check_grad
from scipy.special import ndtr, ndtri

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))
import arene_extension_v1 as ae  # noqa: E402
from controle_ia import gardes  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

DEPOT = ae.DEPOT
ARENE = ICI.parent.parent / "arene-melange-equilibre-v1"
BROUILLON1 = ICI.parent / "preenregistrement-arene-extension-familles-v1-brouillon1.md"
PETITE = ae.replace(
    ae.CONFIG_V1, T=4, n_propre_entr=500, n_attaque_entr=500, n_cal=4000, n_fpr=4000, n_eval=4000, n_mc=64,
    n_mc_final=64, departs=1, departs_final=1, departs_renforce=2, iter_renforce=30, iter_max=30, iter_entr=300,
    departs_entr=3, unites_Bp=3, tol_fpr=0.02, audit_departs=2, audit_n_mc=32, audit_iter=10, audit_es_generations=3,
    audit_es_lambda=2, grille_exacte=2001, L_max=3, grille_partage=21, grille_x=101)
Z99 = float(ndtri(0.99))


@pytest.fixture(autouse=True)
def sans_autorisation():
    ae._AUTORISATION_DECISION["prereg_sha256"] = None
    yield
    ae._AUTORISATION_DECISION["prereg_sha256"] = None
    gardes.SIGNAL_TERM_RECU.clear()


def leve(motif):
    return pytest.raises(GardeArret, match=re.escape(motif))


def sans_temps(x):
    if isinstance(x, dict):
        return {k: sans_temps(v) for k, v in x.items() if "cpu" not in k}
    if isinstance(x, list):
        return [sans_temps(v) for v in x]
    return x


# =================================================================================================================
# Contrôle par l'arbre syntaxique : chaque `raise GardeArret` a un motif unique et un essai nommé
# =================================================================================================================
MOTIFS = {
    "δ invalides (positifs": "test_config_sain_et_artefacts",
    "d = 2 × d_vue et J = 2": "test_config_sain_et_artefacts",
    "rayons des modes invalides": "test_config_sain_et_artefacts",
    "angle des témoins hors": "test_config_sain_et_artefacts",
    "α ou θ* hors": "test_config_sain_et_artefacts",
    "B′ sans moniteurs non linéaires": "test_config_sain_et_artefacts",
    "effectif non positif": "test_config_sain_et_artefacts",
    "bornes du générateur de Q3b": "test_config_sain_et_artefacts",
    "sans autorisation : préenregistrement": "test_gen_garde_racine_de_decision",
    "réservée à la décision de l'extension": "test_racines_essai_artefacts",
    "déjà employée dans l'arène": "test_racines_essai_artefacts",
    "plage du pilote b4": "test_racines_essai_artefacts",
    "hors de la plage de l'extension": "test_racines_essai_artefacts",
    "bloc de configuration canonique absent": "test_identite_prereg_sain_et_artefacts",
    "bloc de configuration illisible": "test_identite_prereg_sain_et_artefacts",
    "préenregistrement sans l'identifiant": "test_identite_prereg_sain_et_artefacts",
    "absent ou différent du code": "test_identite_prereg_sain_et_artefacts",
    "configuration différente du code": "test_identite_prereg_sain_et_artefacts",
    "empreinte de la configuration du code absente": "test_identite_prereg_sain_et_artefacts",
    "empreinte du fichier de code exécuté absente": "test_identite_prereg_sain_et_artefacts",
    "bibliothèque modifiée après gel": "test_identite_prereg_sain_et_artefacts",
    "du processus absente du texte": "test_identite_prereg_sain_et_artefacts",
    "--instances": "test_identite_prereg_sain_et_artefacts",
    "--configs": "test_identite_prereg_sain_et_artefacts",
    "analyse scellée absente": "test_run_principal_sain_et_artefacts",
    "manifeste non décisif": "test_run_principal_sain_et_artefacts",
    "matrice de gains invalide": "test_jeu_sain_et_artefacts",
    "programme linéaire non résolu": "test_jeu_solveur_artefacts",
    "valeurs primale et duale": "test_jeu_solveur_artefacts",
    "poids de mélange invalides": "test_jeu_sain_et_artefacts",
    "centres non opposés": "test_couche_exacte_gardes",
    "selle du jeu restreint non vérifiée": "test_couche_exacte_gardes",
    "un mode déplace la vue de l'autre": "test_couche_exacte_gardes",
    "boule contenant l'origine de sa vue": "test_couche_exacte_gardes",
    "valeur du jeu 2 × 2 ≠ formule fermée": "test_couche_exacte_gardes",
    "segment des centres trop proche": "test_couche_exacte_gardes",
    "couche exacte : famille inconnue": "test_couche_exacte_gardes",
    "régime non couvrable non tenu": "test_garde_regime_sain_et_artefacts",
    "régime témoin non tenu": "test_garde_regime_sain_et_artefacts",
    "paramètres de moniteur non finis": "test_moniteur_gardes",
    "scores propres non finis": "test_moniteur_gardes",
    "variance nulle : seuil non calibrable": "test_moniteur_gardes",
    "moniteur non calibré": "test_moniteur_gardes",
    "« ou » composite : aucun moniteur": "test_ou_composite_sain_et_artefacts",
    "« ou » composite : score propre": "test_ou_composite_sain_et_artefacts",
    "défense vide": "test_defense_empilee_egale_boucle_et_gradient",
    "maxout sans graine": "test_entrainement_gardes",
    "entraînement logistique : paramètres": "test_entrainement_gardes",
    "entraînement par détection : paramètres": "test_entrainement_gardes",
    "loi d'attaque non finie": "test_admissibilite_sain_et_artefacts",
    "coordonnée non libre modifiée": "test_admissibilite_sain_et_artefacts",
    "hors de la boule du mode": "test_admissibilite_sain_et_artefacts",
    "aucun départ n'a donné de point fini": "test_meilleure_reponse_departs_non_finis",
    "départs de l'attaquant au point non fini": "test_garde_departs_finis",
    "contexte : famille inconnue": "test_bras_et_familles_inconnus",
    "taux de fausses alertes mesuré": "test_garde_fausses_alertes_sain_et_artefact",
    "bras sans trajectoire": "test_bras_et_familles_inconnus",
    "témoin inconnu": "test_bras_et_familles_inconnus",
    "bras inconnu pour le régime": "test_bras_et_familles_inconnus",
    "non reproductible bit à bit": "test_garde_convergence_et_identite_tour0",
    "plafond de temps processeur": "test_plafond_de_temps_processeur",
    "entraînements non convergés": "test_garde_convergence_et_identite_tour0",
    "l'optimiseur du déplacement rend moins": "test_prix_gardes",
    "Q3b : paramètres invalides": "test_prix_gardes",
    "gain de la lecture jointe au-dessus": "test_prix_gardes",
    "audit : bras": "test_audit_sain_et_artefacts",
    "audit : V reconstruit": "test_audit_sain_et_artefacts",
    "processus de travail encore vivants": "test_arret_par_pid_sain_et_artefact",
    "processus de travail sans préenregistrement": "test_travail_refuse_racine_de_decision_sans_prereg",
    "audit : tâche absente": "test_audit_sain_et_artefacts",
    "existe déjà : R12": "test_cli_refuse_d_ecraser",
    "apparu pendant l'exécution": "test_cli_refuse_d_ecraser",
    "audit-essai :": "test_charger_pilote_refuse_pilote_etranger",
}


def test_chaque_garde_a_son_essai():
    src = Path(ae.__file__).read_text(encoding="utf-8")
    sites = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call) and \
                getattr(node.exc.func, "id", None) == "GardeArret":
            sites.append((node.lineno, ast.get_source_segment(src, node)))
    vus = []
    for ligne, seg in sites:
        trouves = [m for m in MOTIFS if m in seg]
        assert len(trouves) == 1, f"garde l. {ligne} : motifs {trouves} (exactement un attendu)"
        vus += trouves
    assert sorted(vus) == sorted(MOTIFS), "motif sans garde ou garde comptée deux fois"
    for nom_essai in set(MOTIFS.values()):
        assert callable(globals().get(nom_essai)), f"essai {nom_essai} absent"
    assert len(sites) == len(MOTIFS) == 73


# =================================================================================================================
# Configuration, racines, autorisation de décision
# =================================================================================================================
def test_config_sain_et_artefacts():
    ae.exiger_config(ae.CONFIG_V1)
    ae.exiger_config(PETITE)
    for mauvais, motif in ((dict(deltas=(1.4, 1.0)), "δ invalides (positifs"), (dict(deltas=()), "δ invalides (positifs"),
                           (dict(deltas=(0.0, 1.0)), "δ invalides (positifs"),
                           (dict(d=7), "d = 2 × d_vue et J = 2"), (dict(J=3), "d = 2 × d_vue et J = 2"),
                           (dict(R_min=1.2), "rayons des modes invalides"),
                           (dict(R_min=5.0, R_max=4.0), "rayons des modes invalides"),
                           (dict(gamma_max_deg=90.0), "angle des témoins hors"),
                           (dict(alpha=0.0), "α ou θ* hors"), (dict(theta_couverture=1.0), "α ou θ* hors"),
                           (dict(unites_Bp=1), "B′ sans moniteurs non linéaires"),
                           (dict(T=3), "effectif non positif"), (dict(n_eval=0), "effectif non positif"),
                           (dict(sD_min=0.0), "bornes du générateur de Q3b"),
                           (dict(kappa_min=2.0, kappa_max=1.0), "bornes du générateur de Q3b")):
        with leve(motif):
            ae.exiger_config(ae.replace(PETITE, **mauvais))
    with leve("δ invalides (positifs"):
        ae.exiger_config(None)


def test_racines_essai_sain():
    for r in (ae.RACINE_TESTS, ae.RACINE_TESTS_BIS, ae.RACINE_ESSAI, ae.RACINE_ESSAI_PRIX, ae.RACINE_TEMPS,
              *ae.RACINES_RESERVEES):
        ae.exiger_racine_essai(r)
    assert not set(ae.RACINES_DEJA_EMPLOYEES) & {ae.RACINE_TESTS, ae.RACINE_TESTS_BIS, ae.RACINE_ESSAI,
                                                 ae.RACINE_ESSAI_PRIX, ae.RACINE_TEMPS, *ae.RACINES_RESERVEES,
                                                 *ae.RACINES_DECISION}


@pytest.mark.parametrize("r, motif", [(ae.RACINE_Q3, "réservée à la décision de l'extension"),
                                      (ae.RACINE_PRIX, "réservée à la décision de l'extension"),
                                      (20261201, "déjà employée dans l'arène"), (20261202, "déjà employée dans l'arène"),
                                      (20261291, "déjà employée dans l'arène"), (20261311, "déjà employée dans l'arène"),
                                      (20262291, "déjà employée dans l'arène"), (20269731, "déjà employée dans l'arène"),
                                      (20269742, "déjà employée dans l'arène"),
                                      (20264001, "plage du pilote b4"), (20264500, "plage du pilote b4"),
                                      (20264999, "plage du pilote b4"),
                                      (20265000, "hors de la plage de l'extension"),
                                      (20266000, "hors de la plage de l'extension"),
                                      (20261400, "hors de la plage de l'extension")])
def test_racines_essai_artefacts(r, motif):
    with leve(motif):
        ae.exiger_racine_essai(r)


def test_toutes_les_racines_deja_employees_refusees_et_liste_recoupee_avec_l_arene():
    """Chaque racine de la liste est refusée ; et tout nombre 2026xxxx des textes et codes du dossier de l'arène
    (brouillons, LISEZMOI, journaux, contre-lectures, essais ; hors JSON) figure dans la liste (aucune racine oubliée)."""
    for r in ae.RACINES_DEJA_EMPLOYEES:
        with leve("déjà employée dans l'arène"):
            ae.exiger_racine_essai(r)
    trouves = set()
    for f in ARENE.rglob("*"):
        if f.is_file() and f.suffix in (".md", ".py", ".txt"):
            trouves |= {int(x) for x in re.findall(r"\b2026\d{4}\b", f.read_text(encoding="utf-8"))}
    # la session parallèle (pilote b4, fichiers v4 du même dossier) écrit ses racines dans sa plage et cite la plage de
    # l'extension par ses bornes : les deux plages sont couvertes par les gardes de plage ; tout le reste doit figurer
    # nommément dans la liste
    hors_plages = {r for r in trouves if not (ae.PLAGE_B4[0] <= r <= ae.PLAGE_B4[1])
                   and not (ae.PLAGE_EXTENSION[0] <= r <= ae.PLAGE_EXTENSION[1])}
    assert hors_plages and hors_plages <= set(ae.RACINES_DEJA_EMPLOYEES), sorted(hors_plages - set(ae.RACINES_DEJA_EMPLOYEES))
    assert {r for r in trouves if ae.PLAGE_EXTENSION[0] <= r <= ae.PLAGE_EXTENSION[1]} <= {20265001, 20265999}
    for r in trouves:                                                 # aucune ne passe la garde, sauf les bornes citées
        if r not in (20265001, 20265999):
            with pytest.raises(GardeArret):
                ae.exiger_racine_essai(r)
    # racines employées par décalage dans le code des essais v2 et v3 (RACINE_TESTS + 1000), absentes des textes
    assert {20262291, 20262297, 20262313} <= set(ae.RACINES_DEJA_EMPLOYEES)


def test_gen_garde_racine_de_decision():
    ae.gen(ae.RACINE_TESTS, 1, 2)                                   # sain
    for r in ae.RACINES_DECISION:
        with leve("sans autorisation : préenregistrement"):
            ae.gen(r, 1, 2)
    with leve("sans autorisation : préenregistrement"):
        ae.executer_tache("N2", 0, 1, ae.RACINE_Q3, PETITE)
    with leve("sans autorisation : préenregistrement"):
        ae.configurations_prix(ae.RACINE_PRIX, [0], PETITE)
    ae._AUTORISATION_DECISION["prereg_sha256"] = "0" * 64           # autorisation posée (simulée) : la graine part
    assert ae.gen(ae.RACINE_Q3, 1, 2).integers(10) >= 0


def test_travail_refuse_racine_de_decision_sans_prereg():
    with leve("processus de travail sans préenregistrement"):
        ae._travail(("tache", "N2", 0, 1, ae.RACINE_Q3, asdict(PETITE), None, None))
    with leve("processus de travail sans préenregistrement"):
        ae._travail(("audit", "NV", 0, 1, ae.RACINE_Q3, asdict(PETITE), None, {}))


def test_cli_refuse_racines_interdites(tmp_path):
    for r, motif in ((ae.RACINE_Q3, "réservée à la décision de l'extension"), (20261311, "déjà employée dans l'arène"),
                     (20264100, "plage du pilote b4")):
        with leve(motif):
            ae.main(["essai", "--instances", "0:1", "--sortie", str(tmp_path / "x.json"), "--racine", str(r)])
        with leve(motif):
            ae.main(["prix", "--configs", "0:1", "--sortie", str(tmp_path / "y.json"), "--racine", str(r)])
    assert not (tmp_path / "x.json").exists() and not (tmp_path / "y.json").exists()


def test_cli_refuse_d_ecraser(tmp_path):
    f = tmp_path / "deja.json"
    f.write_text("{}")
    with leve("existe déjà : R12"):
        ae.main(["essai", "--instances", "0:1", "--sortie", str(f)])
    with leve("existe déjà : R12"):
        ae.main(["prix", "--configs", "0:1", "--sortie", str(f)])
    with leve("apparu pendant l'exécution"):
        ae._ecrire_nouveau(f, {"a": 1})
    g = tmp_path / "neuf.json"
    ae._ecrire_nouveau(g, {"a": 1})                                   # sain
    assert g.read_text().strip().startswith("{") and f.read_text() == "{}"


# =================================================================================================================
# Préenregistrement, identité, calcul décisif du pilote principal
# =================================================================================================================
def texte_prereg(cfg, marqueur=False):
    from controle_ia.prereg import SECTIONS

    corps = {s: "Contenu d'essai." for s in SECTIONS}
    corps["Contre-lecture"] = f"Contre-lecteur fictif ; brouillon relu {'a' * 64} ; rapport {'b' * 64}."
    if marqueur:
        corps["Seuil"] = "À REMPLIR"
    return ("# Préenregistrement d'essai (dossier temporaire)\n\n" + ae.bloc_identite(cfg) + "\n\n" +
            "\n\n".join(f"## {k}\n\n{v}" for k, v in corps.items()) + "\n")


def test_identite_prereg_sain_et_artefacts():
    cfg = PETITE
    ok = texte_prereg(cfg)
    ae.exiger_identite_prereg(ok, cfg)
    ae.exiger_identite_prereg(ok, cfg, f"0:{cfg.n_instances}", f"0:{cfg.n_configs}")
    code = ae.empreinte_fichier(ae.__file__)
    lib = ae.empreinte_fichier(DEPOT / ae.FICHIERS_BIBLIOTHEQUE[1])
    bloc = re.search(re.escape(ae.DEBUT_CONFIG) + r".*?" + re.escape(ae.FIN_CONFIG), ok, re.S).group(0)
    ligne_cfg = next(li for li in ok.splitlines() if cfg.empreinte() in li and "Configuration" in li)
    artefacts = [
        (ok.replace(bloc, ""), "bloc de configuration canonique absent"),
        (ok.replace('"T": 4', '"T": 4,,'), "bloc de configuration illisible"),
        (ok.replace(ae.IDENTIFIANT_PREREG, "PREREG-AUTRE"), "préenregistrement sans l'identifiant"),
        (ok.replace(f"RACINE_Q3 = {ae.RACINE_Q3} ", "RACINE_Q3 = 20265999 "), "absent ou différent du code"),
        (ok.replace('"T": 4', '"T": 5'), "configuration différente du code"),
        (ok.replace(ligne_cfg, "- Configuration : (absente)"), "empreinte de la configuration du code absente"),
        (ok.replace(code, "1" * 64), "empreinte du fichier de code exécuté absente"),
        (ok.replace(lib, "2" * 64), "bibliothèque modifiée après gel"),
        (ok.replace(f"numpy {np.__version__}", "numpy 1.26.0"), "du processus absente du texte"),
    ]
    for texte, motif in artefacts:
        assert texte != ok
        with leve(motif):
            ae.exiger_identite_prereg(texte, cfg)
    with leve("--instances"):
        ae.exiger_identite_prereg(ok, cfg, "0:99")
    with leve("--configs"):
        ae.exiger_identite_prereg(ok, cfg, None, "0:7")
    with pytest.raises(GardeArret, match=r"T : texte 5 ≠ code 4"):
        ae.exiger_identite_prereg(ok.replace('"T": 4', '"T": 5'), cfg)


def test_prereg_scelle_refus_pour_la_bonne_raison(tmp_path):
    from controle_ia.scellement import sceller

    cfg = PETITE
    p1 = tmp_path / "p1.md"
    p1.write_text(texte_prereg(cfg), encoding="utf-8")
    with pytest.raises(GardeArret, match=r"empreinte compagnon p1\.md\.sha256 absente"):
        ae.autoriser_decision(p1, cfg)
    p3 = tmp_path / "p3.md"
    p3.write_text(texte_prereg(cfg, marqueur=True), encoding="utf-8")
    sceller(p3)
    with pytest.raises(GardeArret, match=r"scellé mais non conforme"):
        ae.autoriser_decision(p3, cfg)
    assert ae._AUTORISATION_DECISION["prereg_sha256"] is None
    p5 = tmp_path / "p5.md"
    p5.write_text(texte_prereg(cfg), encoding="utf-8")
    sha = sceller(p5)
    assert ae.autoriser_decision(p5, cfg) == sha == ae._AUTORISATION_DECISION["prereg_sha256"]
    ae.gen(ae.RACINE_Q3, 0)


def _faux_run_principal(depot: Path, run_id: str, decisif=True, racine=20261201):
    """Run principal factice dans un dossier temporaire : manifeste scellé + analyse scellée rattachée."""
    from controle_ia import manifeste as man
    from controle_ia.scellement import sceller

    config = {"racine": racine, "essai": True}
    d = depot / "runs" / run_id
    d.mkdir(parents=True)
    m = {"run_id": run_id, "decisif": decisif, "config": config,
         "config_sha256": __import__("hashlib").sha256(man.config_canonique(config)).hexdigest()}
    (d / "manifeste.json").write_text(json.dumps(m), encoding="utf-8")
    sceller(d / "manifeste.json")
    man.ecrire_resultat(depot, d / "manifeste.json", "analyse-arene", {"faux": True})


def test_run_principal_sain_et_artefacts(tmp_path):
    _faux_run_principal(tmp_path, "20991231-000000-principal")
    corps = ae.exiger_run_principal(tmp_path, "20991231-000000-principal")             # sain
    assert corps["resultat"] == {"faux": True}
    with leve("analyse scellée absente"):
        ae.exiger_run_principal(tmp_path, "20991231-000001-absent")
    _faux_run_principal(tmp_path, "20991231-000002-essai", decisif=False)
    with leve("manifeste non décisif"):
        ae.exiger_run_principal(tmp_path, "20991231-000002-essai")
    _faux_run_principal(tmp_path, "20991231-000003-autre", racine=20261311)
    with leve("manifeste non décisif"):
        ae.exiger_run_principal(tmp_path, "20991231-000003-autre")
    f = tmp_path / "diag" / "20991231-000000-principal" / "analyse-arene.json"
    f.write_text(f.read_text() + " ")                                                 # artefact : analyse modifiée
    with pytest.raises(GardeArret, match=r"≠ scellée"):
        ae.exiger_run_principal(tmp_path, "20991231-000000-principal")


def test_decision_refusee_sans_calcul_decisif_principal_puis_sans_prereg(tmp_path, monkeypatch):
    """La décision part d'abord sur la garde du pilote principal (aucun run principal dans le dépôt aujourd'hui) ; avec
    un run principal factice, elle part sur le scellement du préenregistrement (copie temporaire du brouillon 1)."""
    from controle_ia.scellement import sceller

    run_id = "20990101-000000-extension-essai-garde-v1"
    args = ["decision", "--prereg", str(tmp_path / "p.md"), "--run-principal", "20990101-000000-inexistant",
            "--instances", f"0:{ae.CONFIG_V1.n_instances}", "--configs", f"0:{ae.CONFIG_V1.n_configs}", "--run-id",
            run_id]
    with leve("analyse scellée absente"):
        ae.main(args)
    _faux_run_principal(tmp_path, "20990101-000000-principal-factice")
    monkeypatch.setattr(ae, "DEPOT", tmp_path)
    if BROUILLON1.is_file():
        copie = tmp_path / "copie-brouillon1.md"
        shutil.copyfile(BROUILLON1, copie)
        args2 = ["decision", "--prereg", str(copie), "--run-principal", "20990101-000000-principal-factice",
                 "--instances", f"0:{ae.CONFIG_V1.n_instances}", "--configs", f"0:{ae.CONFIG_V1.n_configs}",
                 "--run-id", run_id]
        with pytest.raises(GardeArret, match=r"empreinte compagnon copie-brouillon1\.md\.sha256 absente"):
            ae.main(args2)
        sceller(copie)
        with pytest.raises(GardeArret, match=r"scellé mais non conforme"):
            ae.main(args2)
    assert not (DEPOT / "runs" / run_id).exists() and ae._AUTORISATION_DECISION["prereg_sha256"] is None


def test_brouillon1_non_conforme_au_validateur_et_identite_du_code():
    """Le brouillon 1 garde ses marqueurs : le validateur refuse de le sceller ; son bloc d'identité est celui du code
    et de la configuration remis."""
    from controle_ia.prereg import problemes

    if not BROUILLON1.is_file():
        pytest.skip("brouillon 1 pas encore écrit")
    p = problemes(BROUILLON1)
    assert any("Seuil" in x for x in p) and any("Contre-lecture" in x for x in p)
    ae.exiger_identite_prereg(BROUILLON1.read_text(encoding="utf-8"), ae.CONFIG_V1,
                              f"0:{ae.CONFIG_V1.n_instances}", f"0:{ae.CONFIG_V1.n_configs}")


def test_cli_identite(capsys):
    ae.main(["identite"])
    sortie = capsys.readouterr().out
    assert ae.CONFIG_V1.empreinte() in sortie and ae.empreinte_fichier(ae.__file__) in sortie
    assert ae.extraire_configuration(sortie) == json.loads(json.dumps(asdict(ae.CONFIG_V1)))


# =================================================================================================================
# Jeu à somme nulle et poids
# =================================================================================================================
def test_jeu_sain_et_artefacts():
    p, q, v = ae.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))
    assert np.allclose(p, [0.5, 0.5]) and np.allclose(q, [0.5, 0.5]) and abs(v - 0.5) < 1e-9
    p, q, v = ae.resoudre_jeu(np.array([[0.6, 0.0], [0.2, 0.4]]))
    assert np.allclose(p, [0.25, 0.75]) and abs(v - 0.3) < 1e-9
    for G in (np.array([[np.nan, 0.1]]), np.array([[1.2, 0.1]]), np.array([0.1, 0.2])):
        with leve("matrice de gains invalide"):
            ae.resoudre_jeu(G)
    ae.exiger_poids([0.25, 0.75])
    for pp in ([0.5, 0.4], [1.2, -0.2], [np.nan, 1.0]):
        with leve("poids de mélange invalides"):
            ae.exiger_poids(pp)


def test_jeu_solveur_artefacts(monkeypatch):
    vrai = ae.linprog
    monkeypatch.setattr(ae, "linprog", lambda *a, **k: SimpleNamespace(status=2, message="simulé", fun=0.0,
                                                                        x=np.zeros(3)))
    with leve("programme linéaire non résolu"):
        ae.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))
    appels = []

    def decale(*a, **k):
        r = vrai(*a, **k)
        appels.append(1)
        if len(appels) == 2:
            r.fun += 0.01
        return r
    monkeypatch.setattr(ae, "linprog", decale)
    with leve("valeurs primale et duale"):
        ae.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))


# =================================================================================================================
# Familles et couche exacte : formules, certificats vérifiés indépendamment, selle, union
# =================================================================================================================
def familles(i=0, racine=None):
    return ae.generer_familles(i, ae.RACINE_TESTS if racine is None else racine, ae.CONFIG_V1)


def test_familles_structure_et_appariement():
    cfg = ae.CONFIG_V1
    for i in range(5):
        f = familles(i)
        R = [np.linalg.norm(c) for c in f["N2"].centres]
        assert all(cfg.R_min <= r <= cfg.R_max for r in R)
        for nom in ("C2", "NV", "CV"):                                     # appariement : mêmes rayons
            assert np.allclose([np.linalg.norm(c) for c in f[nom].centres], R)
        assert np.allclose(f["N2"].centres[1] / R[1], -f["N2"].centres[0] / R[0])
        c1, c2 = f["C2"].centres
        gam = np.degrees(np.arccos(c1 @ c2 / (R[0] * R[1])))
        assert cfg.gamma_min_deg - 1e-9 <= gam <= cfg.gamma_max_deg + 1e-9
        assert np.all(f["NV"].centres[0][3:] == 0) and np.all(f["NV"].centres[1][:3] == 0)
        assert np.all(f["CV"].centres[:, 3:] == 0) and f["CV"].libres == ((0, 1, 2), (0, 1, 2))
    assert not np.allclose(familles(0)["N2"].centres, familles(0, ae.RACINE_TESTS_BIS)["N2"].centres)


def test_couche_exacte_formules_et_certificats():
    cfg = ae.CONFIG_V1
    for i in range(6):
        f = familles(i)
        for dl in cfg.deltas:
            r = [np.linalg.norm(c) - dl for c in f["N2"].centres]
            a, b = ndtr(np.array(r) - Z99), ndtr(-np.array(r) - Z99)
            ex = ae.couche_exacte(f["N2"], dl, cfg)
            assert abs(ex["V_pur"] - ndtr(-dl - Z99)) < 1e-15
            assert abs(ex["V_mel"] - (a[0] * a[1] - b[0] * b[1]) / (a[0] + a[1] - b[0] - b[1])) < 1e-9
            assert ex["V_pur"] < cfg.theta_couverture <= ex["V_union"] and ex["V_mel"] < ex["V_union"]
            nv = ae.couche_exacte(f["NV"], dl, cfg)
            an = ndtr(np.array([np.linalg.norm(c) - dl for c in f["NV"].centres]) - Z99)
            assert nv["V_pur"] == cfg.alpha
            assert abs(nv["V_mel"] - (an[0] * an[1] - cfg.alpha ** 2) / (an.sum() - 2 * cfg.alpha)) < 1e-12
            for nom in ("C2", "CV"):
                c = ae.couche_exacte(f[nom], dl, cfg)
                c1, c2 = f[nom].centres
                ts = np.linspace(0, 1, 200001)
                rho = np.min(np.linalg.norm(c1[None] + ts[:, None] * (c2 - c1)[None], axis=1))
                assert abs(c["V_pur"] - ndtr(rho - dl - Z99)) < 1e-6
                assert c["selle_certifiee"] and c["VT_exact"] == 0.0 and c["V_pur"] >= cfg.theta_couverture


def test_certificat_N2_par_recherche_sur_la_sphere():
    """Indépendant de la formule : pour 200 000 directions tirées (et les directions ⊥ u), le pire cas exact sur la
    famille (min_j Φ(w·c_j − δ − z), exact pour des boules) ne dépasse jamais V_pur = Φ(−δ − z)."""
    cfg = ae.CONFIG_V1
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(77,)))
    for i in range(3):
        fam = familles(i)["N2"]
        W = g.standard_normal((200000, cfg.d))
        W /= np.linalg.norm(W, axis=1, keepdims=True)
        for dl in cfg.deltas:
            pire = np.min(ndtr(W @ fam.centres.T - dl - Z99), axis=1)
            assert pire.max() <= ndtr(-dl - Z99) + 1e-15
            u = fam.centres[0] / np.linalg.norm(fam.centres[0])
            Wp = W - np.outer(W @ u, u)
            Wp /= np.linalg.norm(Wp, axis=1, keepdims=True)
            assert np.allclose(np.min(ndtr(Wp @ fam.centres.T - dl - Z99), axis=1), ndtr(-dl - Z99))


def test_certificat_NV_moniteur_riche_d_une_vue():
    """Un maxout à 12 unités lisant la vue 1, entraîné contre les deux modes, détecte le mode 2 (vue 1 propre par
    construction) au taux α à l'erreur d'échantillonnage près ; il ne peut pas faire mieux, quelle que soit sa taille."""
    cfg = PETITE
    ctx = ae.Contexte("NV", 0, 2, ae.RACINE_TESTS, cfg)
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(78,)))
    Xp = g.standard_normal((3000, 6))
    Xa = np.vstack([c + g.standard_normal((1500, 6)) for c in ctx.fam.centres])
    W, b, ok, _ = ae.entrainer(Xp[:, :3], Xa[:, :3], 12, cfg, np.random.default_rng(3), [])
    Wf = np.zeros((12, 6))
    Wf[:, :3] = W
    m = ae.Moniteur(Wf, b, (0, 1, 2)).calibrer(g.standard_normal((200000, 6)), cfg.alpha)
    mode2 = ctx.fam.centres[1].copy()
    mode2[3:] *= 1 - ctx.delta / np.linalg.norm(mode2[3:])            # pire point du mode 2 (vue 1 inchangée : propre)
    n = 400000
    taux = float(np.mean(m.detecte(mode2 + g.standard_normal((n, 6)))))
    fpr = float(np.mean(m.detecte(g.standard_normal((n, 6)))))
    assert abs(taux - fpr) < 4 * np.sqrt(2 * 0.01 * 0.99 / n) and abs(fpr - cfg.alpha) < 0.002
    assert ctx.fam.libres[1] == (3, 4, 5) and np.all(ctx.fam.centres[1][:3] == 0)


def test_selle_exacte_verifiee_des_deux_cotes():
    """N2 et NV : contre p* (défenseur), aucun des 200 000 points tirés dans les boules ne fait descendre la détection
    sous V ; contre q* (attaquant aux pires points), aucune direction ou vue ne la fait monter au-dessus."""
    cfg = ae.CONFIG_V1
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(79,)))
    for i in range(2):
        f = familles(i)
        for dl in cfg.deltas:
            ex = ae.couche_exacte(f["N2"], dl, cfg)
            c1, c2 = f["N2"].centres
            u = c1 / np.linalg.norm(c1)
            p, q, V = np.array(ex["p"]), np.array(ex["q"]), ex["V_mel"]
            for c in (c1, c2):
                v = g.standard_normal((200000, 6))
                mu = c + v / np.linalg.norm(v, axis=1, keepdims=True) * dl * g.uniform(0, 1, (200000, 1)) ** (1 / 6)
                det = p[0] * ndtr(mu @ u - Z99) + p[1] * ndtr(-(mu @ u) - Z99)
                assert det.min() >= V - 1e-9
            W = g.standard_normal((200000, 6))
            W /= np.linalg.norm(W, axis=1, keepdims=True)
            r1, r2 = np.linalg.norm(c1) - dl, np.linalg.norm(c2) - dl
            gain = q[0] * ndtr(r1 * (W @ u) - Z99) + q[1] * ndtr(-r2 * (W @ u) - Z99)
            assert gain.max() <= V + 1e-9
            nv = ae.couche_exacte(f["NV"], dl, cfg)
            a = [ndtr(np.linalg.norm(c) - dl - Z99) for c in f["NV"].centres]
            qn = np.array(nv["q"])
            for v in range(2):                                          # meilleure vue contre q* (NP dans la vue)
                assert qn[v] * a[v] + (1 - qn[v]) * cfg.alpha <= nv["V_mel"] + 1e-12


def test_union_exacte_contre_monte_carlo():
    cfg = ae.CONFIG_V1
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(80,)))
    n = 400000
    f = familles(1)
    dl = 1.4
    ex = ae.couche_exacte(f["N2"], dl, cfg)
    c1, c2 = f["N2"].centres
    u = c1 / np.linalg.norm(c1)
    a1 = ex["alpha1_union"]
    t1, t2 = ndtri(1 - a1), ndtri(1 - (cfg.alpha - a1))
    X0 = g.standard_normal((n, 6))
    assert abs(np.mean((X0 @ u > t1) | (X0 @ u < -t2)) - cfg.alpha) < 4 * np.sqrt(0.01 / n)
    dets = []
    for c in (c1, c2):
        mu = c * (1 - dl / np.linalg.norm(c))
        X = mu + g.standard_normal((n, 6))
        dets.append(np.mean((X @ u > t1) | (X @ u < -t2)))
    assert abs(min(dets) - ex["V_union"]) < 4 * np.sqrt(0.25 / n)
    nv = ae.couche_exacte(f["NV"], dl, cfg)
    a1 = nv["alpha1_union"]
    a2 = 1 - (1 - cfg.alpha) / (1 - a1)
    t1, t2 = ndtri(1 - a1), ndtri(1 - a2)
    w1 = f["NV"].centres[0] / np.linalg.norm(f["NV"].centres[0])
    w2 = f["NV"].centres[1] / np.linalg.norm(f["NV"].centres[1])
    assert abs(np.mean((X0 @ w1 > t1) | (X0 @ w2 > t2)) - cfg.alpha) < 4 * np.sqrt(0.01 / n)
    dets = []
    for c in f["NV"].centres:
        mu = c * (1 - dl / np.linalg.norm(c))
        X = mu + g.standard_normal((n, 6))
        dets.append(np.mean((X @ w1 > t1) | (X @ w2 > t2)))
    assert abs(min(dets) - nv["V_union"]) < 4 * np.sqrt(0.25 / n)


def test_garde_regime_sain_et_artefacts():
    cfg = ae.CONFIG_V1
    ae.exiger_regime("N2", {"V_pur": 0.001, "V_union": 0.7}, cfg)                      # sains
    ae.exiger_regime("C2", {"V_pur": 0.6, "V_union": None}, cfg)
    with leve("régime non couvrable non tenu"):
        ae.exiger_regime("NV", {"V_pur": 0.01, "V_union": 0.45}, cfg)
    with leve("régime non couvrable non tenu"):
        ae.exiger_regime("N2", {"V_pur": 0.55, "V_union": 0.8}, cfg)
    with leve("régime témoin non tenu"):
        ae.exiger_regime("CV", {"V_pur": 0.42, "V_union": None}, cfg)
    with leve("régime non couvrable non tenu"):                                        # rayons trop petits : union < θ*
        ae.couche_exacte(familles(0)["N2"], 1.4, ae.replace(cfg, theta_couverture=0.95))
    with leve("régime témoin non tenu"):
        ae.couche_exacte(familles(0)["C2"], 1.4, ae.replace(cfg, theta_couverture=0.95))


def test_couche_exacte_gardes(monkeypatch):
    cfg = ae.CONFIG_V1
    f = familles(0)
    mauvais = ae.Famille("N2", np.stack([f["N2"].centres[0], f["C2"].centres[1]]), f["N2"].libres, "champ",
                         f["N2"].vues)
    with leve("centres non opposés"):
        ae.exact_N2(mauvais, 1.0, cfg)
    with leve("centres non opposés"):
        ae.exact_N2(f["N2"], 5.0, cfg)
    nv = f["NV"]
    fuite = nv.centres.copy()
    fuite[0, 4] = 0.3
    with leve("un mode déplace la vue de l'autre"):
        ae.exact_NV(ae.Famille("NV", fuite, nv.libres, "vues", nv.vues), 1.0, cfg)
    with leve("boule contenant l'origine de sa vue"):
        ae.exact_NV(nv, 5.0, cfg)
    c = f["C2"]
    with leve("segment des centres trop proche"):
        ae.exact_couvrable(ae.Famille("C2", np.stack([c.centres[0], -c.centres[0]]), c.libres, "champ", c.vues), 1.0,
                           cfg)
    with leve("couche exacte : famille inconnue"):
        ae.couche_exacte(ae.Famille("ZZ", c.centres, c.libres, "champ", c.vues), 1.0, cfg)
    vrai = ae.resoudre_jeu
    monkeypatch.setattr(ae, "resoudre_jeu", lambda M: (np.array([1.0, 0.0]), np.array([0.5, 0.5]), float(M[0, 0])))
    with leve("selle du jeu restreint non vérifiée"):
        ae.exact_N2(f["N2"], 1.0, cfg)
    monkeypatch.setattr(ae, "resoudre_jeu", lambda M: (*vrai(M)[:2], vrai(M)[2] + 0.01))
    with leve("valeur du jeu 2 × 2 ≠ formule fermée"):
        ae.exact_NV(nv, 1.0, cfg)
    monkeypatch.setattr(ae, "resoudre_jeu", vrai)
    ae.exact_N2(f["N2"], 1.0, cfg)                                                     # sains
    ae.exact_NV(nv, 1.0, cfg)


# =================================================================================================================
# Moniteurs, « ou » composite, défense empilée, entraînement
# =================================================================================================================
def test_moniteur_gardes():
    Xcal = np.random.default_rng(0).standard_normal((500, 2))
    ae.Moniteur(np.array([[1.0, 0.0]]), np.array([0.0])).calibrer(Xcal, 0.01).detecte(Xcal)     # sain
    with leve("paramètres de moniteur non finis"):
        ae.Moniteur(np.array([[np.nan, 1.0]]), np.array([0.0]))
    with leve("moniteur non calibré"):
        ae.Moniteur(np.array([[1.0, 0.0]]), np.array([0.0])).detecte(np.zeros((2, 2)))
    with leve("variance nulle : seuil non calibrable"):
        ae.Moniteur(np.zeros((1, 2)), np.zeros(1)).calibrer(np.ones((10, 2)), 0.01)
    X = Xcal.copy()
    X[3, 0] = np.inf
    with leve("scores propres non finis"):
        ae.Moniteur(np.array([[1.0, 0.0]]), np.array([0.0])).calibrer(X, 0.01)
    m = ae.Moniteur(np.array([[0, 0, 0, 1.0, 2.0, 0]]), np.zeros(1), (3, 4, 5))
    assert m.nb_parametres == 4 and ae.Moniteur(np.ones((9, 6)), np.zeros(9)).nb_parametres == 63


def test_ou_composite_sain_et_artefacts():
    g = np.random.default_rng(6)
    Xcal, Xf = g.standard_normal((20000, 6)), g.standard_normal((20000, 6))
    mons = [ae.Moniteur(g.standard_normal((k, 6)), g.standard_normal(k)).calibrer(Xcal, 0.01) for k in (1, 3)]
    ou = ae.MoniteurOu(mons, Xcal, 8.0).calibrer(Xcal, 0.01)
    assert ou.nb_parametres == 7 + 21 and abs(float(np.mean(ou.detecte(Xf))) - 0.01) < 0.004
    x0 = Xf[0]
    assert check_grad(lambda x: ou.score(x[None])[0], lambda x: ou.score_et_grad(x[None])[1][0], x0) < 1e-5
    with leve("« ou » composite : aucun moniteur"):
        ae.MoniteurOu([], Xcal, 8.0)
    with leve("« ou » composite : score propre"):
        ae.MoniteurOu([mons[0], ae.Moniteur(np.zeros((2, 6)), np.zeros(2))], Xcal, 8.0)


def test_defense_empilee_egale_boucle_et_gradient():
    g = np.random.default_rng(7)
    Xcal = g.standard_normal((20000, 6))
    mons = [ae.Moniteur(g.standard_normal((k, 6)), g.standard_normal(k)).calibrer(Xcal, 0.01) for k in (1, 3, 3, 1)]
    poids = [0.1, 0.4, 0.0, 0.5]
    D = ae.Defense(list(zip(mons, poids)))
    assert D.empile
    Z = g.standard_normal((300, 6))
    mu = g.standard_normal(6)
    X = mu + Z
    boucle = sum(p * np.mean(m.detecte(X)) for m, p in zip(mons, poids) if p > 0)
    assert abs(D.taux(X) - boucle) < 1e-12
    ou = ae.MoniteurOu(mons[:2], Xcal, 8.0).calibrer(Xcal, 0.01)
    D2 = ae.Defense([(ou, 1.0)])
    assert not D2.empile
    for DD in (D, D2):
        f = (lambda m_: DD.lisse_et_grad(m_ + Z, 0.25)[0])
        gr = (lambda m_: DD.lisse_et_grad(m_ + Z, 0.25)[1])
        assert check_grad(f, gr, mu) < 1e-6
    with leve("défense vide"):
        ae.Defense([(mons[0], 0.0)])


def test_entrainement_gardes(monkeypatch):
    cfg = PETITE
    g = np.random.default_rng(1)
    Xp, Xa = g.standard_normal((300, 3)), g.standard_normal((300, 3)) + 1.5
    W, b, ok, fun = ae.entrainer(Xp, Xa, 1, cfg, None, [np.ones(3) / np.sqrt(3)])
    W2, b2, _, _ = ae.entrainer(Xp, Xa, 2, cfg, np.random.default_rng(2), [np.ones(3) / np.sqrt(3)])
    assert W.shape == (1, 3) and W2.shape == (2, 3) and fun < 0
    with leve("maxout sans graine"):
        ae.entrainer(Xp, Xa, 2, cfg, None)
    vrai_min = ae.minimize

    def detection_nan(f, x0, *a, **k):
        r = vrai_min(f, x0, *a, **k)
        if f is ae.objectif_detection:
            r.x = np.full_like(r.x, np.nan)
        return r
    monkeypatch.setattr(ae, "minimize", detection_nan)
    with leve("entraînement par détection : paramètres"):
        ae.entrainer(Xp, Xa, 1, cfg, None)
    monkeypatch.setattr(ae, "minimize", vrai_min)
    monkeypatch.setattr(ae, "_logistique", lambda *a, **k: SimpleNamespace(x=np.full(4, np.nan), fun=np.nan,
                                                                          success=False))
    with leve("entraînement logistique : paramètres"):
        ae.entrainer(Xp, Xa, 1, cfg, None)


def test_entrainement_une_vue_garde_la_bonne_vue():
    ctx = ae.Contexte("CV", 0, 1, ae.RACINE_TESTS, PETITE)
    m = ctx.entrainer(5, 1, list(ctx.fam.centres), np.array([0.5, 0.5]), 1, True)
    assert m.vue == (0, 1, 2) and np.all(m.W[:, 3:] == 0)                 # CV : les deux modes dans la vue 1
    ctx = ae.Contexte("NV", 0, 1, ae.RACINE_TESTS, PETITE)
    m = ctx.entrainer(5, 1, list(ctx.fam.centres), np.array([0.0, 1.0]), 3, True)
    assert m.vue == (3, 4, 5) and np.all(m.W[:, :3] == 0)                 # NV : contre le mode 2, la vue 2


# =================================================================================================================
# Attaquant
# =================================================================================================================
def test_admissibilite_sain_et_artefacts():
    fam = familles(0)["NV"]
    c = fam.centres[0]
    ae.exiger_admissible(c * (1 - 1.0 / np.linalg.norm(c)), fam, 0, 1.0)               # sain : bord de la boule
    nan = c.copy()
    nan[1] = np.nan
    with leve("loi d'attaque non finie"):
        ae.exiger_admissible(nan, fam, 0, 1.0)
    fuite = c.copy()
    fuite[4] = 0.1
    with leve("coordonnée non libre modifiée"):
        ae.exiger_admissible(fuite, fam, 0, 1.0)
    with leve("hors de la boule du mode"):
        ae.exiger_admissible(c * 0.5, fam, 0, 1.0)


def test_meilleure_reponse_baisse_la_detection_et_reste_admissible():
    cfg = ae.replace(PETITE, n_mc=256)
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(81,)))
    Xcal = g.standard_normal((20000, 6))
    f = familles(0)
    u = f["N2"].centres[0] / np.linalg.norm(f["N2"].centres[0])
    m = ae.Moniteur(u[None, :], np.zeros(1)).calibrer(Xcal, 0.01)
    mu, j, info = ae.meilleure_reponse(ae.Defense([(m, 1.0)]), f["N2"], 1.0, cfg, g, g)
    assert j == 1 and abs(mu @ u + np.linalg.norm(f["N2"].centres[1]) + 1.0) < 1e-3     # fuit derrière le moniteur
    w1 = np.zeros(6)
    w1[:3] = f["NV"].centres[0][:3] / np.linalg.norm(f["NV"].centres[0][:3])
    mv = ae.Moniteur(w1[None, :], np.zeros(1), (0, 1, 2)).calibrer(Xcal, 0.01)
    mu, j, _ = ae.meilleure_reponse(ae.Defense([(mv, 1.0)]), f["NV"], 1.0, cfg, g, g)
    assert j == 1 and np.all(mu[:3] == 0)                                             # NV : l'autre vue
    for jj, c in enumerate(f["C2"].centres):
        assert np.linalg.norm(c) > 1.0
    ae.exiger_admissible(mu, f["NV"], j, 1.0)


def test_meilleure_reponse_departs_non_finis(monkeypatch):
    cfg = PETITE
    g = np.random.default_rng(3)
    f = familles(0)["C2"]
    m = ae.Moniteur(np.ones((1, 6)), np.zeros(1)).calibrer(g.standard_normal((4000, 6)), 0.01)
    vrai_min = ae.minimize
    compte = {"n": 0}

    def un_sur_deux(fn, x0, *a, **k):
        r = vrai_min(fn, x0, *a, **k)
        if k.get("method") == "SLSQP":
            compte["n"] += 1
            if compte["n"] % 2 == 0:
                r.x = np.full_like(r.x, np.nan)
        return r
    monkeypatch.setattr(ae, "minimize", un_sur_deux)
    mu, j, info = ae.meilleure_reponse(ae.Defense([(m, 1.0)]), f, 1.0, cfg, g, g, n_departs=1)
    assert info["non_finis"] == info["departs"] // 2 and info["departs"] == 6
    ae.exiger_admissible(mu, f, j, 1.0)

    def tous_nan(fn, x0, *a, **k):
        r = vrai_min(fn, x0, *a, **k)
        if k.get("method") == "SLSQP":
            r.x = np.full_like(r.x, np.nan)
        return r
    monkeypatch.setattr(ae, "minimize", tous_nan)
    with leve("aucun départ n'a donné de point fini"):
        ae.meilleure_reponse(ae.Defense([(m, 1.0)]), f, 1.0, cfg, g, g)


def test_garde_departs_finis():
    ae.exiger_departs_finis(0, 0, PETITE)
    ae.exiger_departs_finis(5, 100, PETITE)
    with leve("départs de l'attaquant au point non fini"):
        ae.exiger_departs_finis(6, 100, PETITE)


# =================================================================================================================
# Tâches : gardes, reproductibilité, témoins, indicateurs
# =================================================================================================================
def test_garde_fausses_alertes_sain_et_artefact():
    ctx = ae.Contexte("N2", 0, 1, ae.RACINE_TESTS, PETITE)
    m = ae.Moniteur(np.array([[1.0, 0, 0, 0, 0, 0]]), np.zeros(1)).calibrer(ctx.Xcal, PETITE.alpha)
    ctx.exiger_fpr(ae.Defense([(m, 1.0)]))
    m.t -= 1.0
    with leve("taux de fausses alertes mesuré"):
        ctx.exiger_fpr(ae.Defense([(m, 1.0)]))


def test_garde_convergence_et_identite_tour0():
    ae.exiger_convergence(1, 100, PETITE)
    ae.exiger_convergence(10, 100, PETITE)
    with leve("entraînements non convergés"):
        ae.exiger_convergence(11, 100, PETITE)
    a = ae.Moniteur(np.array([[1.0, 2.0]]), np.array([0.5])).calibrer(np.random.default_rng(0).standard_normal((99, 2)),
                                                                     0.01)
    b = ae.Moniteur(a.W.copy(), a.b.copy())
    b.t = a.t
    ae.exiger_meme_moniteur(a, b)
    b.W[0, 0] += 1e-12
    with leve("non reproductible bit à bit"):
        ae.exiger_meme_moniteur(a, b)


def test_plafond_de_temps_processeur():
    ae.exiger_plafond(time.process_time(), PETITE, "sain")
    with leve("plafond de temps processeur"):
        ae.exiger_plafond(time.process_time() - 1000.0, PETITE, "artefact")
    with leve("plafond de temps processeur"):
        ae.executer_tache("NV", 0, 1, ae.RACINE_TESTS, ae.replace(PETITE, plafond_cpu_tache_s=0.0))


def test_bras_et_familles_inconnus():
    with leve("contexte : famille inconnue"):
        ae.Contexte("ZZ", 0, 1, ae.RACINE_TESTS, PETITE)
    ctx = ae.Contexte("N2", 0, 1, ae.RACINE_TESTS, PETITE)
    M = ctx.entrainer(0, 0, list(ctx.fam.centres), np.array([0.5, 0.5]), 1, False)
    with leve("bras sans trajectoire"):
        ae.trajectoire("PUR_B", ctx, M)
    etat = ae.trajectoire("B", ctx, ae.Moniteur(M.W.copy(), M.b.copy()).calibrer(ctx.Xcal, PETITE.alpha))
    ae.defense_temoin("PUR_B", etat, ctx)                                            # sain
    with leve("témoin inconnu"):
        ae.defense_temoin("C3", etat, ctx)
    with leve("bras inconnu pour le régime"):
        ae.executer_tache("N2", 0, 1, ae.RACINE_TESTS, PETITE, bras=("AV",))
    with leve("bras inconnu pour le régime"):
        ae.executer_tache("NV", 0, 1, ae.RACINE_TESTS, PETITE, bras=("B",))


def test_temoins_pur_et_union_nombres_aleatoires_communs():
    """PUR : moniteur de poids maximal ; U : « ou » du support (un seul moniteur au support : lui-même) ; un mélange
    pur et son PUR ont le même V au bit près (graines du bras source)."""
    ctx = ae.Contexte("C2", 0, 1, ae.RACINE_TESTS, PETITE)
    M = ctx.entrainer(0, 0, list(ctx.fam.centres), np.array([0.5, 0.5]), 1, False)
    etat = ae.trajectoire("B", ctx, ae.Moniteur(M.W.copy(), M.b.copy()).calibrer(ctx.Xcal, PETITE.alpha))
    mons = etat["moniteurs"]
    pur = dict(etat, defense_finale=[(m, 1.0 if k == 1 else 0.0) for k, m in enumerate(mons)])
    (mp, w), = ae.defense_temoin("PUR_B", pur, ctx)
    (mu, w2), = ae.defense_temoin("U_B", pur, ctx)
    assert mp is mons[1] and mu is mons[1] and w == w2 == 1.0
    v_src = ae.phase_finale(pur["defense_finale"], ctx, pur, 2)["V_final"]
    v_pur = ae.phase_finale([(mp, 1.0)], ctx, pur, 2)["V_final"]
    assert v_src == v_pur
    mix = dict(etat, defense_finale=[(m, 0.5 if k in (0, 2) else 0.0) for k, m in enumerate(mons)])
    (ou, _), = ae.defense_temoin("U_B", mix, ctx)
    assert isinstance(ou, ae.MoniteurOu) and ou.membres == [mons[0], mons[2]]
    (m0, _), = ae.defense_temoin("PUR_B", mix, ctx)
    assert m0 is mons[0]                                                              # égalité : plus petit indice


def test_indicateurs_cycle_sain_et_valeur_nulle():
    T = 8
    H = np.tile(np.linspace(0.2, 0.9, T), (T + 1, 1))
    u = np.array([1.0, 0, 0, 0, 0, 0])
    alt = [u * (1 if t % 2 else -1) for t in range(T)]
    cy = ae.indicateurs_cycle(H, [0.1] * T, alt, [t % 2 for t in range(T)])
    assert cy["I3_retours"] == 1.0 and cy["I4_changements"] == 1.0 and cy["I1_progres"] == 0.0
    assert abs(cy["I3_nul"] - 0.7345238095) < 1e-9 and cy["I4_nul"] == 0.5
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(82,)))
    sims = [ae.indicateurs_cycle(H, [0.0] * T, list(g.standard_normal((T, 6))), list(g.integers(0, 2, T)))
            for _ in range(20000)]
    assert abs(np.mean([s["I3_retours"] for s in sims]) - ae.I3_NUL_T8) < 0.005        # valeur nulle d'I3
    assert abs(np.mean([s["I4_changements"] for s in sims]) - 0.5) < 0.005


def test_reproductibilite_bit_a_bit_et_autre_racine():
    a = ae.executer_tache("NV", 0, 2, ae.RACINE_TESTS, PETITE)
    b = ae.executer_tache("NV", 0, 2, ae.RACINE_TESTS, PETITE)
    c = ae.executer_tache("NV", 0, 2, ae.RACINE_TESTS_BIS, PETITE)
    assert sans_temps(a) == sans_temps(b)
    assert sans_temps(a)["bras"] != sans_temps(c)["bras"]
    assert set(a["bras"]) == set(ae.BRAS_DU_REGIME["vues"])
    for x in a["bras"].values():
        assert abs(x["fpr_final"] - PETITE.alpha) <= PETITE.tol_fpr


# =================================================================================================================
# Analyse et lecture mécanique
# =================================================================================================================
def test_classer_effet_et_etalonnage():
    def q(lo, hi, elo=None, ehi=None):
        return {"q0.0125": lo, "q0.9875": hi, "q0.025": lo if elo is None else elo, "q0.975": hi if ehi is None else ehi}
    m = 0.02
    assert ae.classer_effet(q(0.03, 0.2), m) == "> m"
    assert ae.classer_effet(q(-0.2, -0.03), m) == "< −m"
    assert ae.classer_effet(q(-0.01, 0.01), m) == "≈ 0"
    assert ae.classer_effet(q(0.001, 0.05), m) == "≳ 0"
    assert ae.classer_effet(q(-0.05, -0.001), m) == "≲ 0"
    assert ae.classer_effet(q(-0.05, 0.05), m) == "?"
    assert ae.classer_etalonnage(q(-0.02, 0.01), 0.03) == "étalonnée"
    assert ae.classer_etalonnage(q(-0.09, -0.04), 0.03) == "biais bas"
    assert ae.classer_etalonnage(q(0.04, 0.09), 0.03) == "biais haut"
    assert ae.classer_etalonnage(q(-0.05, 0.0), 0.03) == "?"


def _analyse_factice(vt_nc, vt_tem, cal):
    def bloc(vt, cl, vp):
        qq = {f"q{p:g}": vt for p in ae.QUANTILES}
        qc = {f"q{p:g}": cl for p in ae.QUANTILES}
        return {"grandeurs": {"VT_B": {"quantiles": qq}, "VT_BpV": {"quantiles": qq}, "CAL_B": {"quantiles": qc},
                              "CAL_BpV": {"quantiles": qc}}, "bras": {}, "indicateurs": {}, "exact": {"V_pur": vp}}
    pf = {}
    for cd in ("1", "2"):
        pf[f"N2|{cd}"], pf[f"NV|{cd}"] = bloc(vt_nc, cal, 0.0), bloc(vt_nc, cal, 0.01)
        pf[f"C2|{cd}"], pf[f"CV|{cd}"] = bloc(vt_tem, 0.0, 0.7), bloc(vt_tem, 0.0, 0.7)
    return {"par_famille": pf}


def test_lire_tables_verdicts_atteignables():
    m, tau = 0.02, 0.03
    assert ae.lire_tables(_analyse_factice(0.4, 0.0, -0.01), m, tau)["E5"].startswith("tirage utile")
    assert ae.lire_tables(_analyse_factice(0.0, 0.0, -0.01), m, tau)["E5"].startswith("instrument incapable")
    assert ae.lire_tables(_analyse_factice(0.4, 0.1, -0.01), m, tau)["E5"].startswith("instrument qui fabrique")
    assert ae.lire_tables(_analyse_factice(0.4, 0.0, -0.1), m, tau)["E5"].startswith("tirage montré, étalonnage")
    assert ae.lire_tables(_analyse_factice(0.4, 0.015, -0.01), m, tau)["E5"] == "non tranché"


def test_analyse_et_lecture_sur_taches_reelles():
    res = [ae.executer_tache(f, i, 1, ae.RACINE_TESTS, PETITE) for f in ae.FAMILLES for i in (0, 1)]
    an = ae.analyser(res, ae.RACINE_TESTS)
    for f in ae.FAMILLES:
        bloc = an["par_famille"][f"{f}|1"]
        assert bloc["n"] == 2 and bloc["exact"]["part_selle_certifiee"] == 1.0
        assert ("VT_B" if ae.REGIME[f] == "champ" else "VT_BpV") in bloc["grandeurs"]
    assert "VT_B N2-C2|1" in an["regime"] and "VT_BpV NV-CV|1" in an["regime"]
    lt = ae.lire_tables(an, 0.02, 0.03)
    assert set(lt["E1"]) == {f"{f}|1" for f in ae.FAMILLES} and isinstance(lt["E5"], str)


# =================================================================================================================
# Q3b : identités, formule contre Monte-Carlo, taux de fausses alertes exact, gardes
# =================================================================================================================
def test_prix_identites_et_bords():
    cfg = ae.replace(ae.CONFIG_V1, grille_partage=41, grille_x=201)
    for Ra, sD, kap, b0 in ((3.0, 3.0, 0.8, 0.3), (2.6, 2.2, 0.0, 0.0), (3.4, 3.8, 1.4, 0.9)):
        for L in (1, 4):
            r = ae.gains_prix(Ra, sD, kap, b0, L, cfg)
            assert r["G_joint"] <= min(r["G_act"], r["G_comp"]) + 1e-12 and r["dilemme"] >= -1e-12
            assert abs(r["G_comp"] - ndtr(Z99 - b0)) < 1e-9 and r["x_comp"] < 1e-6
    r = ae.gains_prix(2.6, 2.2, 0.0, 0.0, 3, cfg)                    # comportement inutile : la jointe = activations
    assert abs(r["G_joint"] - r["G_act"]) < 1e-9 and abs(r["alpha_act_joint"] - cfg.alpha) < 1e-12


def test_prix_formule_contre_monte_carlo():
    cfg = ae.CONFIG_V1
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(83,)))
    n = 400000
    for Ra, sD, kap, b0, L, aa, x in ((3.0, 3.0, 0.8, 0.3, 4, 0.006, 1.2), (2.7, 2.5, 1.2, 0.0, 2, 0.01, 1.8),
                                      (3.3, 3.5, 0.4, 0.8, 1, 0.003, 0.5)):
        sim, ana = ae.verifier_gain_mc(Ra, sD, kap, b0, L, aa, x, cfg, n, g)
        assert abs(sim - ana) < 4 * np.sqrt(0.25 / n)


def test_prix_taux_de_fausses_alertes_exact_du_partage():
    cfg = ae.CONFIG_V1
    g = np.random.default_rng(np.random.SeedSequence(ae.RACINE_TESTS, spawn_key=(84,)))
    n = 1000000
    for L, aa in ((1, 0.01), (4, 0.004), (8, 0.0), (3, 0.0099)):
        t = ae.seuil_vues(aa, L)
        ab = 1 - (1 - cfg.alpha) / (1 - aa)
        zb = float("inf") if ab <= 0 else ndtri(1 - ab)
        S = g.standard_normal((n, L))
        b = g.standard_normal(n)
        assert abs(np.mean((S > t).any(1) | (b > zb)) - cfg.alpha) < 4 * np.sqrt(0.01 / n)


def test_prix_gardes(monkeypatch):
    cfg = ae.replace(ae.CONFIG_V1, grille_partage=11, grille_x=101)
    ae.gains_prix(3.0, 3.0, 0.5, 0.5, 2, cfg)                                         # sain
    for bad in ((0.0, 3.0, 0.5, 0.5, 2), (3.0, 0.0, 0.5, 0.5, 2), (3.0, 3.0, -0.1, 0.5, 2), (3.0, 3.0, 0.5, 0.5, 0)):
        with leve("Q3b : paramètres invalides"):
            ae.gains_prix(*bad, cfg)
    vrai = ae._maximiser_1d
    monkeypatch.setattr(ae, "_maximiser_1d", lambda f, a, b, n: (0.0, -1e9))
    with leve("l'optimiseur du déplacement rend moins"):
        ae.gains_prix(3.0, 3.0, 0.5, 0.5, 2, cfg)
    monkeypatch.setattr(ae, "_maximiser_1d", vrai)
    vrai_g = ae.gain_maximal
    appels = {"n": 0}

    def fausse(*a, **k):
        appels["n"] += 1
        g_, x_ = vrai_g(*a, **k)
        return (0.01, x_) if appels["n"] <= 2 else (0.9, x_)
    monkeypatch.setattr(ae, "gain_maximal", fausse)
    with leve("gain de la lecture jointe au-dessus"):
        ae.gains_prix(3.0, 3.0, 0.5, 0.5, 2, cfg)


def test_prix_executer_et_analyser():
    cfg = ae.replace(PETITE, grille_partage=11, grille_x=101)
    res = ae.executer_prix(ae.RACINE_TESTS, range(4), cfg)
    assert len(res) == 4 and all(len(c["par_L"]) == cfg.L_max for c in res)
    an = ae.analyser_prix(res, ae.RACINE_TESTS, 0.02)
    assert set(an["par_L"]) == {"1", "2", "3"} and an["n_configs"] == 4
    assert res == ae.executer_prix(ae.RACINE_TESTS, range(4), cfg)                    # déterministe


# =================================================================================================================
# Attaquant indépendant (audit) et pilote étranger
# =================================================================================================================
def test_audit_sain_et_artefacts():
    src = ae.executer_tache("NV", 0, 1, ae.RACINE_TESTS, PETITE)
    a = ae.auditer_tache("NV", 0, 1, ae.RACINE_TESTS, PETITE, src)                  # sain
    for b, x in a["bras"].items():
        assert x["V_audit"] <= x["V_source"] == src["bras"][b]["V_final"]
    faux = json.loads(json.dumps(src))
    faux["bras"]["BpV"]["V_final"] += 1e-6
    with leve("audit : V reconstruit"):
        ae.auditer_tache("NV", 0, 1, ae.RACINE_TESTS, PETITE, faux)
    del faux["bras"]["DV"]
    with leve("audit : bras"):
        ae.auditer_tache("NV", 0, 1, ae.RACINE_TESTS, PETITE, faux)
    with leve("audit : tâche absente"):
        ae.auditer([("NV", 0, 1)], ae.RACINE_TESTS, PETITE, {}, processus=1)
    j = ae.juger_audit([a], 0.02, 0.01)
    assert "NV|1" in j["par_famille"] and isinstance(j["artefact"], bool)


def test_juger_audit_sain_et_artefact():
    def t(src, aud):
        return {"famille": "N2", "code_delta": 1,
                "bras": {"B": {"V_source": src, "V_audit": aud}, "PUR_B": {"V_source": 0.0, "V_audit": 0.0},
                         "U_B": {"V_source": 0.8, "V_audit": 0.8}}}
    assert not ae.juger_audit([t(0.40, 0.395)], 0.02, 0.01)["artefact"]               # écart 0,005 : sain
    assert ae.juger_audit([t(0.40, 0.38)], 0.02, 0.01)["artefact"]                    # écart 0,02 > m/2
    assert ae.juger_audit([t(0.025, 0.015)], 0.02, 0.05)["artefact"]                  # classe changée


def test_charger_pilote_refuse_pilote_etranger(tmp_path):
    cfg = ae.CONFIG_V1
    ok = {"mode": "essai", "manifeste": {"racine": ae.RACINE_ESSAI, "config_sha256": cfg.empreinte()}}
    f = tmp_path / "ok.json"
    f.write_text(json.dumps(ok))
    ae.charger_pilote(f, cfg)                                                         # sain
    for mauvais in ({**ok, "mode": "prix"}, {**ok, "manifeste": {**ok["manifeste"], "config_sha256": "0" * 64}}):
        g = tmp_path / f"m{len(list(tmp_path.iterdir()))}.json"
        g.write_text(json.dumps(mauvais))
        with leve("audit-essai :"):
            ae.charger_pilote(g, cfg)
    h = tmp_path / "decision.json"
    h.write_text(json.dumps({**ok, "manifeste": {**ok["manifeste"], "racine": ae.RACINE_Q3}}))
    with leve("réservée à la décision de l'extension"):
        ae.charger_pilote(h, cfg)


# =================================================================================================================
# Processus de travail : arrêt par PID (R10), aucun orphelin, signal TERM
# =================================================================================================================
def test_arret_par_pid_sain_et_artefact(tmp_path, capsys):
    p = subprocess.Popen(["sleep", "60"])
    try:
        pids = [(p.pid, ae._debut_processus(p.pid))]
        assert ae.processus_vivant(*pids[0]) and not ae.processus_vivant(p.pid, "0")
        with leve("processus de travail encore vivants"):
            ae.exiger_aucun_orphelin(pids)
        f = tmp_path / "pids.txt"
        f.write_text("# essai\n" + "".join(f"{a} {b}\n" for a, b in pids))
        assert ae.lire_pids(f) == pids
        with leve("processus de travail encore vivants"):
            ae.main(["orphelins", "--pids", str(f)])
        ae.main(["orphelins", "--pids", str(f), "--arreter"])
        assert "aucun processus" in capsys.readouterr().out
        ae.exiger_aucun_orphelin(pids)
    finally:
        p.kill()
        p.wait()


def test_lancer_consigne_pids_sans_orphelin(tmp_path):
    f = tmp_path / "pids-travail.txt"
    res, temps = ae.executer([0], ae.RACINE_TESTS, PETITE, processus=2, familles=("NV",), fichier_pids=f)
    pids = ae.lire_pids(f)
    assert len(res) == 2 and len(pids) == 2 and not any(ae.processus_vivant(a, b) for a, b in pids)
    with leve("existe déjà : R12"):
        ae.executer([0], ae.RACINE_TESTS, PETITE, processus=2, familles=("NV",), fichier_pids=f)


def test_signal_term_arrete_le_pool_par_pid(tmp_path):
    f = tmp_path / "pids-term.txt"
    minuterie = threading.Timer(4.0, lambda: signal.raise_signal(signal.SIGTERM))
    minuterie.start()
    try:
        with pytest.raises(GardeArret, match=re.escape(gardes.MOTIF_TERM)):
            ae.executer(range(6), ae.RACINE_TESTS, PETITE, processus=2, familles=("N2",), fichier_pids=f)
    finally:
        minuterie.cancel()
    pids = ae.lire_pids(f)
    assert len(pids) == 2 and not any(ae.processus_vivant(a, b) for a, b in pids)
    assert signal.getsignal(signal.SIGTERM) is not gardes.lever_sur_term
