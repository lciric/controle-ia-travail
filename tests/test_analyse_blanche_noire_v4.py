"""Analyse appariée, version 4 du code (texte scellé `analyse-blanche-noire-v3`, inchangé ; addendum 1 « gardes des
analyses », relance v4 de R1) : essais R5 sur données **synthétiques** (données jouets des essais v1 ; R1 aux formats
exacts du fournisseur pour la relance v4 : manifeste du rejeu décisif sous un texte scellé, commande
`rejeu_activations_v4`, résultat `rejeu-activations.json` rattaché, pointeurs `["resultat", …]` de la fiche réelle, clé
`tokenisation`, table v4 scellée qui cite le sceau du résultat de réparation scellé) — jamais les vraies données de R1,
R2, R4. Chaque garde neuve éprouvée sur un cas sain et sur un artefact (`texte`, `table-comparee`, `provenance`) ; même
calcul et même issue que la version 3 à entropie égale ; R1 nul pour un motif fermé ; mode décisif (texte qui gouverne
inchangé par chemin et empreinte, copie sous un autre nom refusée ; addendum unique, bloc propre ; passages antérieurs et
autres analyses tolérés ; second passage refusé) ; fermeture des importations (aucun module du paquet principal)."""
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.analyse_blanche_noire import constantes as C
from controle_ia.analyse_blanche_noire import constantes_v3 as C3
from controle_ia.analyse_blanche_noire import constantes_v4 as C4
from controle_ia.analyse_blanche_noire import entrees_v4 as EN4
from controle_ia.analyse_blanche_noire import lecture as LB1
from controle_ia.analyse_blanche_noire import lecture_v3 as LB3
from controle_ia.analyse_blanche_noire import lecture_v4 as LB4
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat, graines
from controle_ia.scellement import empreinte, sceller
from test_analyse_blanche_noire_v1 import D, RUN, _donnees, _ecrire_npz, _ecrire_r2, _ecrire_run
from test_analyse_blanche_noire_v3 import _fiche

RACINE = Path(__file__).resolve().parents[1]
RUN_REJEU = "20261105-021737-r1-v4-rejeu-reel"
ADDENDUM_R1 = "prereg/R1-addendum-relance-v4.md"
SECTIONS = ["## Hypothèse", "h", "## Prédiction chiffrée et signe attendu", "p", "## Métrique", "m", "## Seuil", "s",
            "## Plan d'analyse", "a", "## Critères de lecture gelés", "c", "## Liste d'arrêt", "l",
            "## Contre-lecture", f"relu `{'a' * 64}`, rapport `{'b' * 64}`"]


@pytest.fixture(autouse=True)
def constantes_reduites(monkeypatch):
    for nom, v in (("DIMENSION", D), ("TIRAGES", 400), ("N_PLANCHER", 20), ("DECOUPAGES", 2),
                   ("PERMUTATIONS_NEGATIF", 2), ("RUN_P3", RUN)):
        monkeypatch.setattr(C, nom, v)
    monkeypatch.setattr(C3, "INVITE_JUGE_SHA256", "ab" * 32)                      # invite des données jouets (J3)


# ------------------------------------------------------------------------------------------------ textes et pièces jouets
def _texte_jouet(depot, chemin, *lignes) -> str:
    p = depot / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n\n".join(["# Préenregistrement jouet", *lignes, *SECTIONS]) + "\n", encoding="utf-8")
    return sceller(p)


def _bloc(titre, fichiers, alterer=False) -> str:
    lignes = [f"- `{c}` : `{empreinte(RACINE / c)}`" for c in fichiers]
    if alterer:
        lignes[-1] = lignes[-1][:-3] + ("0" if lignes[-1][-3] != "0" else "1") + lignes[-1][-2:]
    return "\n".join([titre, *lignes])


def _pieces_v4(depot, monkeypatch) -> dict:
    sha_add = _texte_jouet(depot, ADDENDUM_R1, "addendum v4 jouet de R1")
    monkeypatch.setattr(C4, "ADDENDUM_V4", {"chemin": ADDENDUM_R1, "sha256": sha_add})
    rep = depot / C4.RESULTAT_REPARATION_V4
    rep.parent.mkdir(parents=True, exist_ok=True)
    rep.write_text(json.dumps({"etape": "reparation", "voie": "lot_fidele", "episodes": []}) + "\n", encoding="utf-8")
    sha_rep = sceller(rep)
    p = depot / C4.TABLE_V4
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"version": 4, "resultat_reparation_sha256": sha_rep, "voie": "lot_fidele",
                             "temoin": {"chemin": "x", "sha256": "0" * 64, "lecture": "jouet"}, "episodes": []},
                            sort_keys=True, indent=1) + "\n", encoding="utf-8")
    return {"addendum": sha_add, "reparation": sha_rep, "table": sceller(p)}


def _ecrire_r1_v4(depot, d, sha_textes, sha_table, *, run=RUN_REJEU, prereg_run=ADDENDUM_R1,
                  commande=C4.COMMANDE_REJEU_V4, addendum_tok=ADDENDUM_R1, table_sha_tok=None, tokenisation=True,
                  verdict="conforme", repli=False):
    """R1 au format réel de la fiche v3 : deux fichiers, « manifeste » = résultat scellé et rattaché du rejeu
    (`diag/<run>/rejeu-activations.json`), pointeurs dans `resultat`, clé `tokenisation`."""
    t = {k: d["tables"][k] for k in C.IDENTITE}
    n = d["tables"]["jetons_notes"].shape[0]
    dd = depot / "donnees" / run
    fm = dd / "activations-p3-rejeu-v1.npz"
    sha_m = _ecrire_npz(fm, moyenne=d["moyenne"], jetons_empan=d["tables"]["jetons_notes"],
                        jetons_empan_rejeu=d["tables"]["jetons_notes"], fidele=np.ones(n, dtype=bool), **t)
    fx = dd / "activations-p3-rejeu-v1-maximum.npz"
    sha_x = _ecrire_npz(fx, maximum=d["maximum"], **t)
    m, _ = creer_manifeste(depot, run, {"mode": "jouet", "chemin_table_tokenisation": C4.TABLE_V4}, ["fidelite"],
                           entropie=12, decisif=True, prereg=depot / prereg_run, commande=commande,
                           autoriser_depot_sale=True)
    res = {"verdict_fidelite": verdict, "regle_repli_appliquee": repli, "textes_sha256": sha_textes,
           "couches": [7, 15, 23], "contexte": "forçage, contexte exact", "fichiers": {fm.name: sha_m, fx.name: sha_x}}
    if tokenisation:
        res["tokenisation"] = {"version_table": 4, "table_sha256": sha_table if table_sha_tok is None else table_sha_tok,
                               "table_empreinte_citee": False, "addendum": addendum_tok, "non_conformes": 89,
                               "signales": 22}
    p = ecrire_resultat(depot, m, "rejeu-activations", res)
    return {"moyenne": {"chemin": str(fm.relative_to(depot)), "sha256": sha_m},
            "maximum": {"chemin": str(fx.relative_to(depot)), "sha256": sha_x},
            "manifeste": {"chemin": str(p.relative_to(depot)), "sha256": empreinte(p)},
            "pointeurs": {"fidelite_conforme": ["resultat", "verdict_fidelite"],
                          "textes_sha256": ["resultat", "textes_sha256"], "couches": ["resultat", "couches"],
                          "contexte_rejeu": ["resultat", "contexte"], "regle_repli": ["resultat", "regle_repli_appliquee"]}}


def _source_v4(depot, monkeypatch, seed=1, fiche="fiche.json", juge=True, **k):
    d = _donnees(seed, **k)
    sha = _ecrire_run(depot, RUN, d)
    monkeypatch.setattr(C, "EMPREINTES_P3", sha)
    pieces = _pieces_v4(depot, monkeypatch)
    f = {"format": C3.FORMAT_FICHE, "redaction": "essai synthétique",
         "R1": _ecrire_r1_v4(depot, d, sha["textes"], pieces["table"]), "R2": _ecrire_r2(depot, "r2", d) if juge else None,
         "motif_R1": None, "motif_R2": None if juge else "sorties_non_livrees", "R4": None}
    _fiche(depot, f, fiche)
    return d, f, pieces


def _analyser4(depot, run="20261105-140000-analyse-bn-v4", fiche="fiche.json"):
    return LB4.analyser_v4(depot, fiche, run, None, entropie=777, autoriser_depot_sale=True)


# ------------------------------------------------------------------------------------------------ constantes, liste fermée
def test_constantes_v4_gelees_liste_fermee_et_fermeture_des_importations():
    assert C4.ADDENDUM_V4 == {"chemin": "prereg/R1-addendum-relance-v4.md",
                              "sha256": "0f10881b32fa4c0e5ec1eb02cf88fbd0fcb6ad13f70b59abc2d84e45a99f61c8"}
    assert C4.TEXTE == {"chemin": "prereg/analyse-blanche-noire-v3.md",
                        "sha256": "1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9"}
    assert empreinte(RACINE / C4.TEXTE["chemin"]) == C4.TEXTE["sha256"]                 # texte scellé, inchangé
    assert C4.COMMANDE_REJEU_V4 == "python -m controle_ia.runs_nuit.rejeu_activations_v4"
    assert C4.TABLE_V4 == "prereg/R1-table-tokenisation-v4.json"
    assert C4.RESULTAT_REPARATION_V4 == ("diag/20261104-234729-r1-v4-reparation-reel/"
                                         "resolution-graine-lot-v3-reparation.json")
    assert C4.ADDENDUM == "prereg/addendum-1-gardes-analyses-r1-v4-v1.md"
    assert C4.NOM_SORTIE == C3.NOM_SORTIE and C4.FORMAT_FICHE == C3.FORMAT_FICHE and C4.cles_de_graines() == C3.cles_de_graines()
    assert C4.empreinte_constantes() != C3.empreinte_constantes() and C4.constantes_courantes()["v1_v3"] == C3.constantes_courantes()
    assert LB4.issue_v4 is LB3.issue_v3 and LB4.calculer_p3 is LB3.calculer_p3 and LB4.calculer_r4 is LB3.calculer_r4
    for c in LB4.FICHIERS_PAQUET + LB4.FICHIERS_ESSAIS + LB4.FICHIERS_REUTILISES:
        assert (RACINE / c).is_file(), c
    assert set(LB3.FICHIERS_PAQUET) < set(LB4.FICHIERS_PAQUET) and set(LB3.FICHIERS_ESSAIS) < set(LB4.FICHIERS_ESSAIS)
    assert len(set(LB4.FICHIERS_PAQUET) | set(LB4.FICHIERS_ESSAIS) | set(LB4.FICHIERS_REUTILISES)) == 31
    with pytest.raises(GardeArret, match="titre"):
        LB4.exiger_code_cite("rien")
    with pytest.raises(GardeArret, match="liste fermée"):                               # bloc présent, liste v3 seulement
        LB4.exiger_code_cite("\n\n".join(["# t", _bloc(C4.TITRE_LISTE, LB3.FICHIERS_PAQUET + LB3.FICHIERS_ESSAIS
                                                      + LB3.FICHIERS_REUTILISES)]))
    autre = "\n".join([C4.TITRE_LISTE.replace("secondaire", "autre"), f"- `src/x.py` : `{'0' * 64}`"])
    bloc = LB4.liste_fermee_de("\n\n".join(["# t", autre, C4.TITRE_LISTE, f"- `src/a.py` : `{'1' * 64}`", "## H", "h"]),
                               C4.TITRE_LISTE)
    assert "src/a.py" in bloc and "src/x.py" not in bloc and "## H" not in bloc
    # fermeture des importations : la version 4 ne charge aucun module du paquet principal (interpréteur neuf)
    code = ("import sys, controle_ia.analyse_blanche_noire.lecture_v4; "
            "print(sorted(m for m in sys.modules if m == 'controle_ia' or m.startswith('controle_ia.')))")
    env = dict(os.environ, PYTHONPATH=str(RACINE / "src"))
    sortie = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, env=env, check=True).stdout
    charges = json.loads(sortie.replace("'", '"'))
    assert not any("analyse_principale" in m for m in charges)
    attendus = {f"controle_ia.{c[len('src/controle_ia/'):-3].replace('/', '.')}" for c in LB4.FICHIERS_PAQUET + LB4.FICHIERS_REUTILISES}
    attendus = {m[:-len(".__init__")] if m.endswith(".__init__") else m for m in attendus}
    assert set(charges) == attendus


# ------------------------------------------------------------------------------------------------ gardes de réception
def test_reception_v4_cas_sain_et_artefacts(depot, monkeypatch):
    d, f, pieces = _source_v4(depot, monkeypatch, seed=12)
    sha_t = C.EMPREINTES_P3["textes"]
    r = EN4.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])                 # cas sain
    assert r["table"]["sha256"] == pieces["table"] and r["reparation"]["sha256"] == pieces["reparation"]
    assert r["texte"] == C4.ADDENDUM_V4 and r["commande"] == C4.COMMANDE_REJEU_V4 and r["run_rejeu"] == RUN_REJEU
    _texte_jouet(depot, "prereg/R1-addendum-relance-v3.md", "addendum v3 jouet de R1")
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-a", prereg_run="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="garde texte"):                                # autre texte qui gouverne
        EN4.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    with monkeypatch.context() as mp:
        mp.setattr(C4, "ADDENDUM_V4", dict(C4.ADDENDUM_V4, sha256="0" * 64))           # même chemin, autre empreinte
        with pytest.raises(GardeArret, match="garde texte"):
            EN4.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-b", table_sha_tok="0" * 64)
    with pytest.raises(GardeArret, match="table_sha256"):
        EN4.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    rep = depot / C4.RESULTAT_REPARATION_V4
    comp = Path(str(rep) + ".sha256")
    octets, sceau = rep.read_bytes(), comp.read_text(encoding="utf-8")
    comp.unlink()
    rep.write_bytes(octets + b"\n")
    sceller(rep)
    with pytest.raises(GardeArret, match="resultat_reparation_sha256"):                # table qui cite un autre résultat
        EN4.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])
    rep.write_bytes(octets)
    comp.write_text(sceau, encoding="utf-8")
    comp_table = depot / (C4.TABLE_V4 + ".sha256")
    sceau_table = comp_table.read_text(encoding="utf-8")
    comp_table.unlink()
    with pytest.raises(GardeArret, match="empreinte compagnon"):                       # sceau de la table absent
        EN4.exiger_reception_v4(depot, f["R1"]["manifeste"]["chemin"])
    comp_table.write_text(sceau_table, encoding="utf-8")
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-c", addendum_tok="prereg/R1-addendum-relance-v3.md")
    with pytest.raises(GardeArret, match="tokenisation.addendum"):
        EN4.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-d",
                      commande="python -m controle_ia.runs_nuit.rejeu_activations_v3")
    with pytest.raises(GardeArret, match="commande du manifeste"):
        EN4.exiger_reception_v4(depot, e["manifeste"]["chemin"])
    e = _ecrire_r1_v4(depot, d, sha_t, pieces["table"], run=RUN_REJEU + "-e", tokenisation=False)
    with pytest.raises(GardeArret, match="sans clé tokenisation"):
        EN4.exiger_reception_v4(depot, e["manifeste"]["chemin"])


# ------------------------------------------------------------------------------------------------ bout en bout
def test_v4_meme_calcul_que_v3_reception_artefact_et_R1_nul(depot, monkeypatch):
    d, f, pieces = _source_v4(depot, monkeypatch, seed=7)
    r4 = _analyser4(depot)
    r3 = LB3.analyser_v3(depot, "fiche.json", "20261105-140001-analyse-bn-v3", None, entropie=777, autoriser_depot_sale=True)
    assert r4["P3"] == r3["P3"] and r4["issue"] == r3["issue"] and r4["mode"] == "complet" and r4["version"] == C4.VERSION
    assert r4["reception_v4"]["table"]["sha256"] == pieces["table"] and r4["reception_v4"]["run_rejeu"] == RUN_REJEU
    assert r4["P3"]["bras"]["i"]["lu"] and not r4["P3"]["fidelite"]["independante"]["ratee"]
    man = json.loads((depot / "runs" / "20261105-140000-analyse-bn-v4" / "manifeste.json").read_text(encoding="utf-8"))
    assert man["commande"] == C4.COMMANDE and man["config"]["addendum"] is None
    assert man["config"]["constantes_sha256"] == C4.empreinte_constantes()
    sortie = depot / "diag" / "20261105-140000-analyse-bn-v4" / "analyse-blanche-noire-v3.json"
    assert json.loads(sortie.read_text(encoding="utf-8"))["resultat"]["reception_v4"] == r4["reception_v4"]
    assert sortie.with_suffix(".md").exists() and (sortie.parent / "analyse-blanche-noire-v3.md.sha256").exists()
    # artefact de bout en bout : provenance fausse → arrêt après le chargement de R1, avant le manifeste
    _fiche(depot, dict(f, R1=_ecrire_r1_v4(depot, d, C.EMPREINTES_P3["textes"], pieces["table"], run=RUN_REJEU + "-p",
                                           addendum_tok="prereg/R1-addendum-relance-v3.md")), "fiche-p.json")
    with pytest.raises(GardeArret, match="garde provenance"):
        _analyser4(depot, "20261105-140002-x", "fiche-p.json")
    assert not (depot / "runs" / "20261105-140002-x").exists()
    # R1 nul pour un motif fermé : (i) non lu, aucune garde de réception
    _fiche(depot, dict(f, R1=None, motif_R1="rejeu_non_conforme"), "fiche-r1m.json")
    r = _analyser4(depot, "20261105-140003-x", "fiche-r1m.json")
    assert r["reception_v4"] is None and not r["P3"]["bras"]["i"]["lu"] and "non_lue" in r["P3"]["comparaisons"]["i-L"]


# ------------------------------------------------------------------------------------------------ mode décisif
def test_mode_decisif_v4_texte_inchange_addendum_unique_et_passages(depot, monkeypatch):
    d, f, pieces = _source_v4(depot, monkeypatch, seed=15)
    appels = []
    monkeypatch.setattr(LB1, "exiger_code_importe_sous", appels.append)
    f3 = LB3.FICHIERS_PAQUET + LB3.FICHIERS_ESSAIS + LB3.FICHIERS_REUTILISES
    ligne_v3 = f"Empreinte des constantes (v3) : `{C3.empreinte_constantes()}`"
    sha_t = _texte_jouet(depot, C4.TEXTE["chemin"], ligne_v3, _bloc("## Code", f3))
    monkeypatch.setattr(C4, "TEXTE", {"chemin": C4.TEXTE["chemin"], "sha256": sha_t})
    import shutil
    shutil.copy(depot / C4.TEXTE["chemin"], depot / "prereg/bn-v3-copie.md")           # S1 : même texte, autre nom
    sceller(depot / "prereg/bn-v3-copie.md")
    creer_manifeste(depot, "20261103-072840-analyse-blanche-noire-v3", {"mode": "jouet"}, ["x"], entropie=1,
                    decisif=True, prereg=depot / C4.TEXTE["chemin"], commande=C3.COMMANDE, autoriser_depot_sale=True)
    f4 = LB4.FICHIERS_PAQUET + LB4.FICHIERS_ESSAIS + LB4.FICHIERS_REUTILISES
    ligne_v4 = f"Empreinte des constantes (analyse secondaire, code v4) : `{C4.empreinte_constantes()}`"
    autre = _bloc("### Liste fermée du code — analyse principale (code v6)", f4[:3])
    sha_a = _texte_jouet(depot, C4.ADDENDUM, ligne_v4, autre, _bloc(C4.TITRE_LISTE, f4))
    creer_manifeste(depot, "20261105-150000-analyse-principale-r1-r2-v1",
                    {"addendum": {"chemin": C4.ADDENDUM, "sha256": sha_a}}, ["x"], entropie=2, decisif=True,
                    prereg=depot / C4.TEXTE["chemin"], commande="python -m controle_ia.analyse_principale_r1_r2.lecture_v6",
                    autoriser_depot_sale=True)
    committer(depot)
    with pytest.raises(GardeArret, match="texte passé"):
        LB4.analyser_v4(depot, "fiche.json", "20261105-160001-x", "prereg/bn-v3-copie.md")
    with pytest.raises(GardeArret, match="empreinte citée"):
        LB4.exiger_code_cite("\n\n".join(["# a", ligne_v4, _bloc(C4.TITRE_LISTE, f4, alterer=True)]))
    with pytest.raises(GardeArret, match="entropie"):
        LB4.analyser_v4(depot, "fiche.json", "20261105-160002-x", C4.TEXTE["chemin"], entropie=5)
    r = LB4.analyser_v4(depot, "fiche.json", "20261105-160003-analyse-blanche-noire-v3", C4.TEXTE["chemin"])
    assert appels and r["statut"] == "décisif" and int(r["entropie"]) == LB1.entropie_de(sha_t)
    lien = r["lien_au_preenregistrement"]
    assert lien["sha256"] == sha_t and lien["addendum"]["sha256"] == sha_a and lien["versions"] == C3.VERSIONS_EXIGEES
    assert set(lien["addendum"]["code_cite"]["fichiers"]) == set(f4)
    assert lien["passages"] == {"manifestes_lus": 4, "autres_analyses_sous_l_addendum": 1,
                                "passages_anterieurs_du_texte_hors_addendum": 1}
    assert r["reception_v4"]["table"]["sha256"] == pieces["table"]
    man = json.loads((depot / "runs" / "20261105-160003-analyse-blanche-noire-v3" / "manifeste.json")
                     .read_text(encoding="utf-8"))
    assert man["decisif"] and man["preenregistrement"]["sha256"] == sha_t and man["commande"] == C4.COMMANDE
    assert man["config"]["addendum"] == {"chemin": C4.ADDENDUM, "sha256": sha_a}
    attendu = graines(C4.cles_de_graines(), LB1.entropie_de(sha_t))
    assert set(man["graines"]) == set(attendu) and all(man["graines"][k] == attendu[k] for k in attendu)
    committer(depot)
    with pytest.raises(GardeArret, match="second passage"):
        LB4.analyser_v4(depot, "fiche.json", "20261105-160004-x", C4.TEXTE["chemin"])
    monkeypatch.setattr(C4, "TABLE_V4", "prereg/autre-table.json")                 # constantes ≠ empreinte citée
    with pytest.raises(GardeArret, match="constantes gelées"):
        LB4.exiger_code_cite((depot / C4.ADDENDUM).read_text(encoding="utf-8"))
