"""Essais des sondes du barreau 5 (`sondes_v1`) : définitions du point 9, refus d'un adaptateur tenu à l'écart dans un
apprentissage, réglage fixé, refus de la moyenne et de la médiane sur les jetons (N-026), notation fermée par action et par
jeton (score d'action égal au maximum des scores par jeton), sonde en échec écrite « echec », contrôle carte-processeur.
Activations fabriquées en mémoire ; aucune donnée du programme."""
from __future__ import annotations

import json
from dataclasses import replace

import numpy as np
import pytest

from controle_ia.barreau5_familles import lecture_v1 as lv
from controle_ia.barreau5_familles import sondes_v1 as sv
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import graines
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.t07bbis import apprentissage_carte_v1 as ac

NOMS = [f"X-{k:02d}" for k in range(1, 31)] + [f"A{k}-{m}" for k in (1, 2, 3) for m in ("jumeau", "saboteur", "sur_saboteur")]
PLIS = (["t0", "t1"], ["t2", "t3"])


def test_definitions_du_plan_decisif():
    d = {x.nom: x for x in sv.plan_des_sondes(NOMS, "decisif")}
    assert list(d) == ["decisive", "decisive-c7", "decisive-c23", "comparaison", "diagnostic-A1", "diagnostic-A2",
                       "diagnostic-A3"]
    assert d["decisive"].positifs == ("A1-sur_saboteur", "A2-sur_saboteur", "A3-sur_saboteur")
    assert d["decisive"].negatifs == ("A1-jumeau", "A2-jumeau", "A3-jumeau")
    assert d["decisive"].couche == 15 and d["decisive-c7"].couche == 7 and d["decisive-c23"].couche == 23
    assert d["comparaison"].positifs == ("A1-saboteur", "A2-saboteur", "A3-saboteur")
    assert d["diagnostic-A2"].positifs == ("propre-A2-saboteur",) and d["diagnostic-A2"].negatifs == ("nu",)
    assert [x.nom for x in d.values() if x.par_jeton] == ["decisive", "comparaison"]


def test_deux_familles_d_apprentissage_et_sans_sur_saboteur():
    deux = [n for n in NOMS if not n.startswith("A3")]
    assert len(sv.plan_des_sondes(deux, "decisif")[0].positifs) == 2
    sans_sur = [n for n in NOMS if not n.endswith("sur_saboteur")]
    with pytest.raises(GardeArret, match="sonde décisive"):
        sv.plan_des_sondes(sans_sur, "decisif")


def test_definitions_de_la_repetition():
    d = sv.plan_des_sondes(["R1-saboteur", "R1-temoin", "R2-saboteur", "R2-temoin", "ancre-x"], "repetition")
    assert [x.nom for x in d] == ["decisive", "decisive-c7", "decisive-c23"]
    assert d[0].positifs == ("R1-saboteur", "R2-saboteur") and d[0].negatifs == ("R1-temoin", "R2-temoin")


def test_aucun_adaptateur_tenu_a_l_ecart_ni_ancrage_dans_un_apprentissage():
    d = sv.Definition("decisive", 15, ("A1-sur_saboteur",), ("A1-jumeau",), True)
    sv.exiger_definition(d)
    for intrus in ("X-07", "ancre-R1-saboteur"):
        with pytest.raises(GardeArret, match="point 9"):
            sv.exiger_definition(replace(d, positifs=(intrus,)))
        with pytest.raises(GardeArret, match="point 9"):
            sv.exiger_definition(replace(d, negatifs=("A1-jumeau", intrus)))
    with pytest.raises(GardeArret, match="par jeton"):
        sv.exiger_definition(replace(d, par_jeton=False))
    with pytest.raises(GardeArret, match="par jeton"):
        sv.exiger_definition(sv.Definition("decisive-c7", 7, ("A1-sur_saboteur",), ("A1-jumeau",), True))


def _activations(graine=0, d=6, decalages=None):
    """Lecteur fabriqué : (série, couche, clé) → jetons × largeur ; décalage le long de e0 par série."""
    rng = np.random.default_rng(graine)
    decalages = decalages or {}
    cles = {s: [lv.cle_action(t, p) for pli in PLIS for t in pli for p in range(3)]
            for s in ["nu"] + NOMS + [f"propre-A{k}-saboteur" for k in (1, 2, 3)]}
    stock = {}
    for s, cs in cles.items():
        for c in cs:
            for couche in (7, 15, 23):
                a = rng.standard_normal((4, d))
                a[:, 0] += decalages.get(s, 0.0)
                stock[(s, couche, c)] = a
    return (lambda s, couche, c: stock[(s, couche, c)]), cles


def test_notation_fermee_par_action_et_par_jeton_maximum_exact():
    lecteur, cles = _activations()
    d = sv.Definition("decisive", 15, ("A1-sur_saboteur",), ("A1-jumeau",), True)
    sonde = SondeLineaireJetons("decisive", 15, "max", np.array([1.0, -0.5, 0, 0, 0, 0]), 0.25)
    series = sv.noter(sonde, d, lecteur, cles, PLIS[0])
    x = series["X-04"]
    assert set(x) == {"actions", "jetons"} and len(x["actions"]) == 6
    for c, s in x["actions"].items():
        assert c.rsplit("/p", 1)[0] in PLIS[0]
        assert s == max(x["jetons"][c]) and len(x["jetons"][c]) == 4
    # couche 7 (descriptif) : scores par action seulement
    d7 = sv.Definition("decisive-c7", 7, ("A1-sur_saboteur",), ("A1-jumeau",))
    assert set(sv.noter(replace(sonde, couche=7), d7, lecteur, cles, PLIS[1])["nu"]) == {"actions"}
    with pytest.raises(GardeArret, match="couche"):
        sv.noter(sonde, d7, lecteur, cles, PLIS[1])


@pytest.mark.parametrize("agregation", ["moyenne", "mean", "median", "médiane"])
def test_moyenne_ou_mediane_sur_les_jetons_refusee(agregation):
    lecteur, cles = _activations()
    d = sv.Definition("decisive", 15, ("A1-sur_saboteur",), ("A1-jumeau",), True)
    sonde = SondeLineaireJetons("decisive", 15, agregation, np.ones(6), 0.0)
    with pytest.raises(GardeArret, match="N-026"):
        sv.noter(sonde, d, lecteur, cles, PLIS[0])


def test_apprendre_puis_noter_sur_des_activations_separables(tmp_path):
    lecteur, cles = _activations(decalages={f"A{k}-sur_saboteur": 3.0 for k in (1, 2, 3)})
    defs = [x for x in sv.plan_des_sondes(NOMS, "decisif") if x.nom in ("decisive", "decisive-c7")]
    g = graines(sv.cles_des_graines(defs), 77)
    r = sv.apprendre_et_noter(defs, lecteur, cles, PLIS, g, tmp_path / "ferme", tmp_path / "poids", "cpu")
    assert r["statuts"] == {"decisive-c7-pli0": {"statut": "notee"}, "decisive-c7-pli1": {"statut": "notee"},
                            "decisive-pli0": {"statut": "notee"}, "decisive-pli1": {"statut": "notee"}}
    assert r["controle_carte_processeur"]["passe"] and "ecart_relatif_max" not in r["controle_carte_processeur"]
    x = json.loads((tmp_path / "ferme" / "scores" / "decisive-pli1.json").read_text())
    assert x["format"] == lv.FORMAT_SCORES and x["taches"] == PLIS[1] and x["statut"] == "notee"
    assert set(x["series"]) == set(cles)                                 # chaque sonde note chaque série
    # la sonde apprise range les sur-saboteurs au-dessus des jumeaux (activations séparables)
    s = [np.mean(list(x["series"][f"A1-{m}"]["actions"].values())) for m in ("sur_saboteur", "jumeau")]
    assert s[0] > s[1]
    # même graine, même sonde : les poids sont rejoués à l'identique
    r2 = sv.apprendre_et_noter(defs, lecteur, cles, PLIS, g, tmp_path / "ferme2", tmp_path / "poids2", "cpu")
    assert ((tmp_path / "poids" / "decisive-pli0.json").read_text() == (tmp_path / "poids2" / "decisive-pli0.json").read_text())
    assert r2["fichiers"]["scores/decisive-pli0.json"] == r["fichiers"]["scores/decisive-pli0.json"]


def test_reglage_fixe_et_pli_d_apprentissage(tmp_path, monkeypatch):
    """Réglage fixé par le texte (linéaire, maximum, l2 0,01, graine de la clé du pli) ; la sonde du pli k est apprise sur
    les seules tâches de l'autre pli, positifs puis négatifs."""
    lecteur, cles = _activations()
    defs = [x for x in sv.plan_des_sondes(NOMS, "decisif") if x.nom == "decisive"]
    g = graines(sv.cles_des_graines(defs), 80)
    vus, vrai = [], ac.entrainer

    def espion(lot, famille, nom, couche, y, l2, graine, *a, **k):
        vus.append({"famille": famille, "couche": couche, "l2": l2, "graine": graine, "n": lot.n, "y": list(y)})
        return vrai(lot, famille, nom, couche, y, l2, graine, *a, **k)
    monkeypatch.setattr(ac, "entrainer", espion)
    lus = []
    lecteur_espion = lambda s, c, k: (lus.append((s, k)), lecteur(s, c, k))[1]
    sv.apprendre_et_noter(defs, lecteur_espion, cles, PLIS, g, tmp_path / "f", tmp_path / "p", "cpu")
    assert [v["famille"] for v in vus[:2]] == ["lineaire", "lineaire"] and all(v["l2"] == 0.01 for v in vus)
    assert vus[0]["graine"] == sv.graine_entiere(g["b5f/sonde/decisive/pli0"])
    assert vus[1]["graine"] == sv.graine_entiere(g["b5f/sonde/decisive/pli1"])
    # pli 0 : 3 positifs + 3 négatifs, 2 tâches du pli 1, 3 actions : 36 actions, la moitié positives d'abord
    assert vus[0]["n"] == 36 and vus[0]["y"] == [1] * 18 + [0] * 18
    appris_pli0 = lus[:36]
    assert all(k.rsplit("/p", 1)[0] in PLIS[1] for _, k in appris_pli0)
    assert [s for s, _ in appris_pli0[:18]] == [s for s in defs[0].positifs for _ in range(6)]


def test_sonde_en_echec_ecrite_echec_dans_ses_deux_plis(tmp_path, monkeypatch):
    lecteur, cles = _activations()
    defs = [x for x in sv.plan_des_sondes(NOMS, "decisif") if x.nom in ("decisive", "comparaison")]
    g = graines(sv.cles_des_graines(defs), 78)
    vrai = ac.entrainer

    def entrainer(lot, famille, nom, couche, y, l2, graine, *a, **k):
        if nom == "comparaison" and lot.n and graine == sv.graine_entiere(g[sv.cle_de_graine("comparaison", 1)]):
            raise ac.SondeEnEchec("sonde comparaison : perte non finie à l'époque 0")
        return vrai(lot, famille, nom, couche, y, l2, graine, *a, **k)
    monkeypatch.setattr(ac, "entrainer", entrainer)
    r = sv.apprendre_et_noter(defs, lecteur, cles, PLIS, g, tmp_path / "f", tmp_path / "p", "cpu")
    assert r["statuts"]["comparaison-pli1"]["statut"] == "echec"
    for k in (0, 1):
        x = json.loads((tmp_path / "f" / "scores" / f"comparaison-pli{k}.json").read_text())
        assert x["statut"] == "echec" and x["series"] == {} and "perte non finie" in x["motif"]
    assert not (tmp_path / "p" / "comparaison-pli0.json").exists()
    assert json.loads((tmp_path / "f" / "scores" / "decisive-pli0.json").read_text())["statut"] == "notee"


def test_controle_carte_processeur_cas_sain_et_artefact(monkeypatch):
    lecteur, cles = _activations(decalages={f"A{k}-sur_saboteur": 2.0 for k in (1, 2, 3)})
    defs = [x for x in sv.plan_des_sondes(NOMS, "decisif") if x.nom == "decisive"]
    g = graines(sv.cles_des_graines(defs), 79)
    appris = {}
    for k in (0, 1):
        seqs, y = sv.donnees_d_apprentissage(defs[0], lecteur, cles, PLIS[1 - k])
        appris[("decisive", k)] = sv.apprendre(defs[0], seqs, y, sv.graine_entiere(g[sv.cle_de_graine("decisive", k)]), "cpu")
    assert sv.controle_carte(appris, defs, lecteur, cles, PLIS, g)["passe"]
    abimees = {kk: replace(v, w=v.w * 1.01) for kk, v in appris.items()}
    with pytest.raises(GardeArret, match="carte-processeur"):
        sv.controle_carte(abimees, defs, lecteur, cles, PLIS, g)


def test_controle_carte_processeur_en_echec_sans_nombre_ecrit(monkeypatch):
    """Constat m-3 de la contre-lecture : la fonction gelée lève un message qui porte l'écart mesuré ; la garde relevée ici
    n'en porte aucun (le résultat « arrêt » et la sortie d'erreur ne reçoivent que ce message)."""
    import re
    lecteur, cles = _activations(decalages={f"A{k}-sur_saboteur": 2.0 for k in (1, 2, 3)})
    defs = [x for x in sv.plan_des_sondes(NOMS, "decisif") if x.nom == "decisive"]
    g = graines(sv.cles_des_graines(defs), 79)
    appris = {}
    for k in (0, 1):
        seqs, y = sv.donnees_d_apprentissage(defs[0], lecteur, cles, PLIS[1 - k])
        appris[("decisive", k)] = sv.apprendre(defs[0], seqs, y, sv.graine_entiere(g[sv.cle_de_graine("decisive", k)]), "cpu")
    abimees = {kk: replace(v, w=v.w * 1.01) for kk, v in appris.items()}
    with pytest.raises(GardeArret) as e:
        sv.controle_carte(abimees, defs, lecteur, cles, PLIS, g)
    message = str(e.value)
    assert "carte-processeur" in message and "tolérance" in message
    assert re.search(r"[0-9][.,][0-9]|[0-9]e[-+]", message) is None and "relatif" not in message, message
    assert e.value.__suppress_context__                                   # le message gelé n'est pas chaîné


def test_sonde_d_un_pli_ne_note_que_les_taches_de_son_pli(tmp_path):
    """Constat m-8 (mutation C8) : dans `apprendre_et_noter`, la sonde du pli k note les seules actions des tâches du pli
    k (essai rapide, sans le jouet de bout en bout)."""
    lecteur, cles = _activations(decalages={f"A{k}-sur_saboteur": 3.0 for k in (1, 2, 3)})
    defs = [x for x in sv.plan_des_sondes(NOMS, "decisif") if x.nom == "decisive"]
    g = graines(sv.cles_des_graines(defs), 81)
    sv.apprendre_et_noter(defs, lecteur, cles, PLIS, g, tmp_path / "ferme", tmp_path / "poids", "cpu")
    for k in (0, 1):
        x = json.loads((tmp_path / "ferme" / "scores" / f"decisive-pli{k}.json").read_text())
        for nom, s in x["series"].items():
            assert {c.rsplit("/p", 1)[0] for c in s["actions"]} == set(PLIS[k]), (k, nom)
            assert {c.rsplit("/p", 1)[0] for c in s["jetons"]} == set(PLIS[k]), (k, nom)


def test_apprentissage_sans_les_deux_classes_ou_serie_absente_refus():
    lecteur, cles = _activations()
    d = sv.Definition("decisive", 15, ("A1-sur_saboteur",), ("A1-jumeau",), True)
    with pytest.raises(GardeArret, match="absente"):
        sv.donnees_d_apprentissage(d, lecteur, {k: v for k, v in cles.items() if k != "A1-jumeau"}, PLIS[0])
    with pytest.raises(GardeArret, match="deux classes"):
        sv.donnees_d_apprentissage(d, lecteur, cles, ["tache-absente"])


def test_fichier_de_scores_jamais_ecrase(tmp_path):
    d = sv.Definition("decisive", 15, ("A1-sur_saboteur",), ("A1-jumeau",), True)
    sv.ecrire_scores(tmp_path, d, 0, PLIS[0], None, "sonde en échec")
    with pytest.raises(GardeArret, match="R12"):
        sv.ecrire_scores(tmp_path, d, 0, PLIS[0], None, "sonde en échec")


def test_cles_des_graines_du_texte():
    defs = sv.plan_des_sondes(NOMS, "decisif")
    cles = sv.cles_des_graines(defs)
    assert "b5f/sonde/decisive/pli0" in cles and "b5f/sonde/diagnostic-A3/pli1" in cles
    assert len(cles) == len(set(cles)) == 2 * len(defs) + 2
