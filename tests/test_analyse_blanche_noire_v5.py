"""Analyse appariée, version 5 du code (texte scellé `analyse-blanche-noire-v3`, inchangé ; addendum 1 « gardes des
analyses », relance v4 de R1 ; après la contre-lecture 1 : K1, K2) : essais R5 sur données **synthétiques** (données
jouets des essais v1 ; R1 aux formats exacts du fournisseur pour la relance v4, écrivains des essais de la version 4) —
jamais les vraies données de R1, R2, R4. Chaque garde neuve éprouvée sur un cas sain et sur un artefact (`texte`,
`table-comparee`, `provenance`, lues sur les constantes v5) ; **K1** : aucun `.npz` ouvert avant les gardes (piège sur
`numpy.load`) ; même calcul et même issue que la version 3 à entropie égale ; R1 nul pour un motif fermé ; mode décisif
(texte qui gouverne inchangé, copie sous un autre nom refusée ; addendum unique, bloc propre ; **K2** liste close :
les trois manifestes de la course v3 gelés tolérés, sœurs sous l'addendum tolérées, quatrième manifeste qui cite le
texte → arrêt, toléré altéré → arrêt, commande inconnue → arrêt, second passage → arrêt ; arrêt distinct nommé) ;
fermeture des importations (aucun module du paquet principal) ; empreintes réelles des manifestes de la course v3."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.analyse_blanche_noire import constantes as C
from controle_ia.analyse_blanche_noire import constantes_v3 as C3
from controle_ia.analyse_blanche_noire import constantes_v4 as C4
from controle_ia.analyse_blanche_noire import constantes_v5 as C5
from controle_ia.analyse_blanche_noire import entrees_v5 as EN5
from controle_ia.analyse_blanche_noire import lecture as LB1
from controle_ia.analyse_blanche_noire import lecture_v3 as LB3
from controle_ia.analyse_blanche_noire import lecture_v4 as LB4
from controle_ia.analyse_blanche_noire import lecture_v5 as LB5
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, graines
from controle_ia.scellement import empreinte, sceller
from test_analyse_blanche_noire_v1 import _donnees, _ecrire_r2, _ecrire_run
from test_analyse_blanche_noire_v3 import _fiche
from test_analyse_blanche_noire_v4 import ADDENDUM_R1, RUN, RUN_REJEU, _bloc, _ecrire_r1_v4, _texte_jouet
from test_analyse_blanche_noire_v4 import constantes_reduites  # noqa: F401  (fixture automatique de la version 4, reprise)

RACINE = Path(__file__).resolve().parents[1]
PASSAGES_V3_ATTENDUS = {
    "20261103-072723-analyse-principale-r1-r2-v1": "0587c398cc05f279251bbe747c3deaff1dee29cb191c94ce30090ce50a5e4643",
    "20261103-072805-analyse-par-episode-v1": "79f2a758e0c36f1d4aaa54a78e039ffc802074fe03e222120aff81a78f1a2083",
    "20261103-072840-analyse-blanche-noire-v3": "91f711c6eb903ca470b972a953ac12cdde31f211412a5629725895537d550adf",
}
TEXTE_PRINCIPALE = "prereg/analyse-principale-r1-r2-v1.md"
TEXTE_EPISODE = "prereg/analyse-par-episode-v1.md"


def _pieces_v5(depot, monkeypatch) -> dict:
    sha_add = _texte_jouet(depot, ADDENDUM_R1, "addendum v4 jouet de R1")
    monkeypatch.setattr(C5, "ADDENDUM_V4", {"chemin": ADDENDUM_R1, "sha256": sha_add})
    rep = depot / C5.RESULTAT_REPARATION_V4
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text(json.dumps({"etape": "reparation", "voie": "lot_fidele", "episodes": []}) + "\n", encoding="utf-8")
    sha_rep = sceller(rep)
    p = depot / C5.TABLE_V4
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"version": 4, "resultat_reparation_sha256": sha_rep, "voie": "lot_fidele",
                             "temoin": {"chemin": "x", "sha256": "0" * 64, "lecture": "jouet"}, "episodes": []},
                            sort_keys=True, indent=1) + "\n", encoding="utf-8")
    return {"addendum": sha_add, "reparation": sha_rep, "table": sceller(p)}


def _source_v5(depot, monkeypatch, seed=1, fiche="fiche.json", juge=True, **k):
    d = _donnees(seed, **k)
    sha = _ecrire_run(depot, RUN, d)
    monkeypatch.setattr(C, "EMPREINTES_P3", sha)
    pieces = _pieces_v5(depot, monkeypatch)
    f = {"format": C3.FORMAT_FICHE, "redaction": "essai synthétique",
         "R1": _ecrire_r1_v4(depot, d, sha["textes"], pieces["table"]), "R2": _ecrire_r2(depot, "r2", d) if juge else None,
         "motif_R1": None, "motif_R2": None if juge else "sorties_non_livrees", "R4": None}
    _fiche(depot, f, fiche)
    return d, f, pieces


def _analyser5(depot, run="20261105-140000-analyse-bn-v5", fiche="fiche.json"):
    return LB5.analyser_v5(depot, fiche, run, None, entropie=777, autoriser_depot_sale=True)


def _piege_npz(monkeypatch):
    etat = {"garde_faite": False, "appels_npz": 0, "appels_npz_avant_garde": 0}
    vrai_load, garde = np.load, LB5.exiger_reception_v4

    def piege(*a, **k):
        if not etat["garde_faite"]:
            etat["appels_npz_avant_garde"] += 1
            raise AssertionError("K1 : numpy.load appelé avant les gardes de réception")
        etat["appels_npz"] += 1
        return vrai_load(*a, **k)

    def garde_enveloppee(*a, **k):
        r = garde(*a, **k)
        etat["garde_faite"] = True
        return r
    monkeypatch.setattr(np, "load", piege)
    monkeypatch.setattr(LB5, "exiger_reception_v4", garde_enveloppee)
    return etat


def _manifeste_v3_jouet(depot, run, prereg_rel, commande, config=None):
    creer_manifeste(depot, run, config or {"mode": "jouet"}, ["x"], entropie=1, decisif=True,
                    prereg=depot / prereg_rel, commande=commande, autoriser_depot_sale=True)
    return hashlib.sha256((depot / "runs" / run / "manifeste.json").read_bytes()).hexdigest()


# ------------------------------------------------------------------------------------------------ constantes, liste fermée
def test_constantes_v5_gelees_liste_close_et_fermeture_des_importations():
    assert C5.ADDENDUM_V4 == C4.ADDENDUM_V4 == {"chemin": "prereg/R1-addendum-relance-v4.md",
                                                "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"}
    assert C5.TEXTE == {"chemin": "prereg/analyse-blanche-noire-v3.md",
                        "sha256": "1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9"}
    assert empreinte(RACINE / C5.TEXTE["chemin"]) == C5.TEXTE["sha256"]                 # texte scellé, inchangé
    assert (C5.COMMANDE_REJEU_V4, C5.TABLE_V4, C5.RESULTAT_REPARATION_V4, C5.ADDENDUM) == (
        C4.COMMANDE_REJEU_V4, C4.TABLE_V4, C4.RESULTAT_REPARATION_V4, C4.ADDENDUM)
    assert C5.VERSION == "analyse-blanche-noire-v3 (code v5)" and C5.TITRE_LISTE.endswith("(code v5)")
    assert C5.COMMANDE == "python -m controle_ia.analyse_blanche_noire.lecture_v5"
    assert C5.PASSAGES_V3 == PASSAGES_V3_ATTENDUS                                        # K2, liste close gelée
    for run, sha in C5.PASSAGES_V3.items():
        assert empreinte(RACINE / "runs" / run / "manifeste.json") == sha, run
    assert C5.COMMANDES_ADDENDUM == ("python -m controle_ia.analyse_principale_r1_r2.lecture_v8",
                                     "python -m controle_ia.analyse_principale_r1_r2.lecture_v9", C5.COMMANDE)
    assert C5.NOM_SORTIE == C3.NOM_SORTIE and C5.FORMAT_FICHE == C3.FORMAT_FICHE and C5.cles_de_graines() == C3.cles_de_graines()
    assert C5.empreinte_constantes() not in (C3.empreinte_constantes(), C4.empreinte_constantes())
    assert C5.constantes_courantes()["v1_v3"] == C3.constantes_courantes() and "PASSAGES_V3" in C5.constantes_courantes()["v5"]
    assert LB5.issue_v5 is LB3.issue_v3 and LB5.calculer_p3 is LB3.calculer_p3 and LB5.calculer_r4 is LB3.calculer_r4
    assert issubclass(LB5.PassageHorsListe, GardeArret) and LB5.CODE_FIN_PASSAGE == 2
    for c in LB5.FICHIERS_PAQUET + LB5.FICHIERS_ESSAIS + LB5.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LB3.FICHIERS_PAQUET) < set(LB5.FICHIERS_PAQUET) and set(LB3.FICHIERS_ESSAIS) < set(LB5.FICHIERS_ESSAIS)
    assert not any("_v4" in c for c in LB5.FICHIERS_PAQUET + LB5.FICHIERS_ESSAIS)      # version 4 remplacée
    assert len(set(LB5.FICHIERS_PAQUET) | set(LB5.FICHIERS_ESSAIS) | set(LB5.FICHIERS_REUTILISES)) == 31
    with pytest.raises(GardeArret, match="titre"):
        LB5.exiger_code_cite("rien")
    with pytest.raises(GardeArret, match="liste fermée"):                               # bloc présent, liste v4 seulement
        LB5.exiger_code_cite("\n\n".join(["# t", _bloc(C5.TITRE_LISTE, LB4.FICHIERS_PAQUET + LB4.FICHIERS_ESSAIS
                                                      + LB4.FICHIERS_REUTILISES)]))
    autre = "\n".join([C5.TITRE_LISTE.replace("secondaire", "autre"), f"- `src/x.py` : `{'0' * 64}`"])
    bloc = LB5.liste_fermee_de("\n\n".join(["# t", autre, C5.TITRE_LISTE, f"- `src/a.py` : `{'1' * 64}`", "## H", "h"]),
                               C5.TITRE_LISTE)
    assert "src/a.py" in bloc and "src/x.py" not in bloc and "## H" not in bloc
    # fermeture des importations : la version 5 ne charge aucun module du paquet principal (interpréteur neuf)
    code = ("import sys, controle_ia.analyse_blanche_noire.lecture_v5; "
            "print(sorted(m for m in sys.modules if m == 'controle_ia' or m.startswith('controle_ia.')))")
    env = dict(os.environ, PYTHONPATH=str(RACINE / "src"))
    sortie = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, env=env, check=True).stdout
    charges = json.loads(sortie.replace("'", '"'))
    assert not any("analyse_principale" in m for m in charges)
    attendus = {f"controle_ia.{c[len('src/controle_ia/'):-3].replace('/', '.')}" for c in LB5.FICHIERS_PAQUET + LB5.FICHIERS_REUTILISES}
    attendus = {m[:-len(".__init__")] if m.endswith(".__init__") else m for m in attendus}
    assert set(charges) == attendus


# ------------------------------------------------------------------------------------------------ gardes de réception
def test_reception_v5_cas_sain_et_artefacts(depot, monkeypatch):
    d, f, pieces = _source_v5(depot, monkeypatch, seed=12)
    sha_t = C.EMPREINTES_P3["textes"]
    r = EN5.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])                 # cas sain
    assert r["table"]["sha256"] == pieces["table"] and r["reparation"]["sha256"] == pieces["reparation"]
    assert r["texte"] == C5.ADDENDUM_V4 and r["commande"] == C5.COMMANDE_REJEU_V4 and r["run_rejeu"] == RUN_REJEU
    _texte_jouet(depot, "prereg/R1-addendum-relance-v3.md", "addendum v3 jouet de R1")
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-a", prereg_run="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="garde texte"):                                # autre texte qui gouverne
        EN5.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    with monkeypatch.context() as mp:
        mp.setattr(C5, "ADDENDUM_V4", dict(C5.ADDENDUM_V4, sha256="0" * 64))           # même chemin, autre empreinte
        with pytest.raises(GardeArret, match="garde texte"):
            EN5.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-b", table_sha_tok="0" * 64)
    with pytest.raises(GardeArret, match="table_sha256"):
        EN5.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    rep = depot / C5.RESULTAT_REPARATION_V4
    comp = Path(str(rep) + ".sha256")
    octets, sceau = rep.read_bytes(), comp.read_text(encoding="utf-8")
    comp.unlink()
    rep.write_bytes(octets + b"\n")
    sceller(rep)
    with pytest.raises(GardeArret, match="resultat_reparation_sha256"):                # table qui cite un autre résultat
        EN5.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])
    rep.write_bytes(octets)
    comp.write_text(sceau, encoding="utf-8")
    comp_table = depot / (C5.TABLE_V4 + ".sha256")
    sceau_table = comp_table.read_text(encoding="utf-8")
    comp_table.unlink()
    with pytest.raises(GardeArret, match="empreinte compagnon"):                       # sceau de la table absent
        EN5.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])
    comp_table.write_text(sceau_table, encoding="utf-8")
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-c", addendum_tok="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="tokenisation.addendum"):
        EN5.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-d",
                      commande="python -m controle_ia.runs_nuit.rejeu_activations_v3")
    with pytest.raises(GardeArret, match="commande du manifeste"):
        EN5.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-e", tokenisation=False)
    with pytest.raises(GardeArret, match="sans clé tokenisation"):
        EN5.exiger_reception_v4(depot, e["manifeste"]["chemin"])


# ------------------------------------------------------------------------------------------------ K1, bout en bout
def test_v5_k1_meme_calcul_que_v3_artefact_et_R1_nul(depot, monkeypatch):
    d, f, pieces = _source_v5(depot, monkeypatch, seed=7)
    _fiche(depot, dict(f, R1=_ecrire_r1_v4(depot, d, C.EMPREINTES_P3["textes"], pieces["table"], run=RUN_REJEU + "-p",
                                           addendum_tok="prereg/R1-addendum-relance-v3.md")), "fiche-p.json")
    # artefact (K1) : provenance fausse → arrêt avant P3 et R1, aucun .npz ouvert, rien d'écrit
    with monkeypatch.context() as mp:
        etat = _piege_npz(mp)
        with pytest.raises(GardeArret, match="garde provenance"):
            _analyser5(depot, "20261105-140002-x", "fiche-p.json")
        assert etat == {"garde_faite": False, "appels_npz": 0, "appels_npz_avant_garde": 0}
    assert not (depot / "runs" / "20261105-140002-x").exists()
    # cas sain (K1) : les gardes rendent, puis seulement les chargeurs ouvrent les .npz
    with monkeypatch.context() as mp:
        etat = _piege_npz(mp)
        r5 = _analyser5(depot)
        assert etat["garde_faite"] and etat["appels_npz"] > 0 and etat["appels_npz_avant_garde"] == 0
    r3 = LB3.analyser_v3(depot, "fiche.json", "20261105-140001-analyse-bn-v3", None, entropie=777, autoriser_depot_sale=True)
    assert r5["P3"] == r3["P3"] and r5["issue"] == r3["issue"] and r5["mode"] == "complet" and r5["version"] == C5.VERSION
    assert r5["reception_v4"]["table"]["sha256"] == pieces["table"] and r5["reception_v4"]["run_rejeu"] == RUN_REJEU
    assert r5["P3"]["bras"]["i"]["lu"] and not r5["P3"]["fidelite"]["independante"]["ratee"]
    man = json.loads((depot / "runs" / "20261105-140000-analyse-bn-v5" / "manifeste.json").read_text(encoding="utf-8"))
    assert man["commande"] == C5.COMMANDE and man["config"]["addendum"] is None
    assert man["config"]["constantes_sha256"] == C5.empreinte_constantes()
    assert man["config"]["constantes"]["v5"]["PASSAGES_V3"] == PASSAGES_V3_ATTENDUS
    sortie = depot / "diag" / "20261105-140000-analyse-bn-v5" / "analyse-blanche-noire-v3.json"
    assert json.loads(sortie.read_text(encoding="utf-8"))["resultat"]["reception_v4"] == r5["reception_v4"]
    assert sortie.with_suffix(".md").exists() and (sortie.parent / "analyse-blanche-noire-v3.md.sha256").exists()
    # R1 nul pour un motif fermé : (i) non lu, aucune garde de réception
    _fiche(depot, dict(f, R1=None, motif_R1="rejeu_non_conforme"), "fiche-r1m.json")
    r = _analyser5(depot, "20261105-140003-x", "fiche-r1m.json")
    assert r["reception_v4"] is None and not r["P3"]["bras"]["i"]["lu"] and "non_lue" in r["P3"]["comparaisons"]["i-L"]


# ------------------------------------------------------------------------------------------------ K2, mode décisif
def test_mode_decisif_v5_liste_close_des_passages(depot, monkeypatch):
    d, f, pieces = _source_v5(depot, monkeypatch, seed=15)
    appels = []
    monkeypatch.setattr(LB1, "exiger_code_importe_sous", appels.append)
    f3 = LB3.FICHIERS_PAQUET + LB3.FICHIERS_ESSAIS + LB3.FICHIERS_REUTILISES
    ligne_v3 = f"Empreinte des constantes (v3) : `{C3.empreinte_constantes()}`"
    sha_t = _texte_jouet(depot, C5.TEXTE["chemin"], ligne_v3, _bloc("## Code", f3))
    texte = {"chemin": C5.TEXTE["chemin"], "sha256": sha_t}
    monkeypatch.setattr(C5, "TEXTE", texte)
    shutil.copy(depot / C5.TEXTE["chemin"], depot / "prereg/bn-v3-copie.md")           # S1 : même texte, autre nom
    sceller(depot / "prereg/bn-v3-copie.md")
    _texte_jouet(depot, TEXTE_PRINCIPALE, "texte jouet principal")
    _texte_jouet(depot, TEXTE_EPISODE, "texte jouet par épisode")
    # course v3 simulée : les trois manifestes gelés (K2) ; seul celui de la secondaire cite ce texte
    runs_v3 = list(C5.PASSAGES_V3)
    passages = {runs_v3[0]: _manifeste_v3_jouet(depot, runs_v3[0], TEXTE_PRINCIPALE, "python -m controle_ia.analyse_principale_r1_r2.lecture_v2"),
                runs_v3[1]: _manifeste_v3_jouet(depot, runs_v3[1], TEXTE_EPISODE, "python -m controle_ia.analyse_principale_r1_r2.lecture_v5"),
                runs_v3[2]: _manifeste_v3_jouet(depot, runs_v3[2], C5.TEXTE["chemin"], C3.COMMANDE)}
    monkeypatch.setattr(C5, "PASSAGES_V3", passages)
    f5 = LB5.FICHIERS_PAQUET + LB5.FICHIERS_ESSAIS + LB5.FICHIERS_REUTILISES
    ligne_v5 = f"Empreinte des constantes (analyse secondaire, code v5) : `{C5.empreinte_constantes()}`"
    autre = _bloc("### Liste fermée du code — analyse principale (code v8)", f5[:3])
    sha_a = _texte_jouet(depot, C5.ADDENDUM, ligne_v5, autre, _bloc(C5.TITRE_LISTE, f5))
    creer_manifeste(depot, "20261105-150000-analyse-principale-r1-r2-v1",
                    {"addendum": {"chemin": C5.ADDENDUM, "sha256": sha_a}}, ["x"], entropie=2, decisif=True,
                    prereg=depot / TEXTE_PRINCIPALE, commande="python -m controle_ia.analyse_principale_r1_r2.lecture_v8",
                    autoriser_depot_sale=True)
    committer(depot)
    with pytest.raises(GardeArret, match="texte passé"):
        LB5.analyser_v5(depot, "fiche.json", "20261105-160001-x", "prereg/bn-v3-copie.md")
    with pytest.raises(GardeArret, match="empreinte citée"):
        LB5.exiger_code_cite("\n\n".join(["# a", ligne_v5, _bloc(C5.TITRE_LISTE, f5, alterer=True)]))
    with pytest.raises(GardeArret, match="entropie"):
        LB5.analyser_v5(depot, "fiche.json", "20261105-160002-x", C5.TEXTE["chemin"], entropie=5)
    lus = len(list((depot / "runs").glob("*/manifeste.json")))
    r = LB5.analyser_v5(depot, "fiche.json", "20261105-160003-analyse-blanche-noire-v3", C5.TEXTE["chemin"])
    assert appels and r["statut"] == "décisif" and int(r["entropie"]) == LB1.entropie_de(sha_t)
    lien = r["lien_au_preenregistrement"]
    assert lien["sha256"] == sha_t and lien["addendum"]["sha256"] == sha_a and lien["versions"] == C3.VERSIONS_EXIGEES
    assert set(lien["addendum"]["code_cite"]["fichiers"]) == set(f5)
    assert lien["passages"] == {"manifestes_lus": lus, "autres_analyses_sous_l_addendum": 1,
                                "passages_anterieurs_du_texte_hors_addendum": 1,
                                "toleres": [runs_v3[2], "20261105-150000-analyse-principale-r1-r2-v1"]}
    assert r["reception_v4"]["table"]["sha256"] == pieces["table"]
    man = json.loads((depot / "runs" / "20261105-160003-analyse-blanche-noire-v3" / "manifeste.json")
                     .read_text(encoding="utf-8"))
    assert man["decisif"] and man["preenregistrement"]["sha256"] == sha_t and man["commande"] == C5.COMMANDE
    assert man["config"]["addendum"] == {"chemin": C5.ADDENDUM, "sha256": sha_a}
    attendu = graines(C5.cles_de_graines(), LB1.entropie_de(sha_t))
    assert set(man["graines"]) == set(attendu) and all(man["graines"][k] == attendu[k] for k in attendu)
    committer(depot)
    with pytest.raises(LB5.PassageHorsListe, match="second passage : 20261105-160003-analyse-blanche-noire-v3"):
        LB5.analyser_v5(depot, "fiche.json", "20261105-160004-x", C5.TEXTE["chemin"])
    assert not (depot / "runs" / "20261105-160004-x").exists()
    garde = lambda **k: LB5.exiger_premier_passage_v5(depot, C5.ADDENDUM, sha_a, texte, commande="autre commande", **k)
    assert garde()["autres_analyses_sous_l_addendum"] == 2                             # sain, vu d'une commande sœur
    quatrieme = "20261104-000000-analyse-blanche-noire-v3"                            # quatrième manifeste qui cite le texte
    _manifeste_v3_jouet(depot, quatrieme, C5.TEXTE["chemin"], C3.COMMANDE)
    with pytest.raises(LB5.PassageHorsListe, match=f"hors liste close : {quatrieme} cite le texte"):
        garde()
    with pytest.raises(LB5.PassageHorsListe, match=quatrieme):
        LB5.analyser_v5(depot, "fiche.json", "20261105-160005-x", C5.TEXTE["chemin"])
    shutil.rmtree(depot / "runs" / quatrieme)
    with pytest.raises(LB5.PassageHorsListe, match=f"hors liste close : {runs_v3[2]} cite le texte"):   # toléré altéré
        garde(passages_v3={**passages, runs_v3[2]: "0" * 64})
    p2 = depot / "runs" / runs_v3[2] / "manifeste.json"
    octets = p2.read_bytes()
    p2.write_bytes(octets + b"\n")
    with pytest.raises(LB5.PassageHorsListe, match=runs_v3[2]):
        garde()
    p2.write_bytes(octets)
    creer_manifeste(depot, "20261105-160007-inconnue", {"addendum": {"chemin": C5.ADDENDUM, "sha256": sha_a}}, ["x"],
                    entropie=3, decisif=True, prereg=depot / TEXTE_PRINCIPALE, commande="python -m controle_ia.autre",
                    autoriser_depot_sale=True)
    with pytest.raises(LB5.PassageHorsListe, match="20261105-160007-inconnue cite l'addendum .* commande"):
        garde()
    shutil.rmtree(depot / "runs" / "20261105-160007-inconnue")
    (depot / "runs" / "20261105-160008-illisible").mkdir()
    (depot / "runs" / "20261105-160008-illisible" / "manifeste.json").write_text("{{" + sha_t, encoding="utf-8")
    with pytest.raises(LB5.PassageHorsListe, match="illisible 20261105-160008-illisible"):
        garde()
    shutil.rmtree(depot / "runs" / "20261105-160008-illisible")
    assert garde()["manifestes_lus"] == lus + 1
    monkeypatch.setattr(C5, "TABLE_V4", "prereg/autre-table.json")                 # constantes ≠ empreinte citée
    with pytest.raises(GardeArret, match="constantes gelées"):
        LB5.exiger_code_cite((depot / C5.ADDENDUM).read_text(encoding="utf-8"))
