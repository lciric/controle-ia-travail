"""Essais du contrôle carte-processeur v4 proposé (`validation_imbriquee_v4.py`, même dossier), sur données fabriquées seulement,
processeur seulement (aucune donnée de 7a ni de 7b, aucune activation, aucune sortie de la course).

Jouer : `PYTHONPATH=<dépôt>/src python -m pytest -q -p no:cacheprovider <ce fichier>`.

« Carte émulée » : sans carte, l'apprentissage « de la carte » (`apprentissage_carte_v1.entrainer`, code de la course appelé
tel quel) est joué sur un `LotCarte` des **mêmes actions dans un autre ordre** (permutation tirée, étiquettes permutées de même) :
même problème, même départ, seuls l'ordre des sommes sur les jetons et les actions (moyenne, écart type, perte, gradient) et donc
l'arrondi changent, ce que fait la carte, dont les réductions somment dans un autre ordre que le processeur.

Cas :
1. **Reproduction de l'arrêt sans erreur de chaîne** : sur le jeu « quasi-copies » (40 % de jetons de gabarit), le contrôle v3
   (linéaire à 300 époques) arrête la carte émulée avec un écart de l'ordre de 1 ;
2. **cas après correction** : sur le même jeu et la même carte émulée, le contrôle v4 passe (écart à 3 époques ≤ 10⁻⁴,
   déterminisme au bit près dans les deux familles) et écrit l'écart à 300 époques comme information ; le champ est lu par
   `lecture_v2.exiger_controle_carte` sans changement ;
3. cas sain sur le jeu de la forme de la répétition (apprentissage d'origine) ;
4. artefacts à 3 époques : poids altérés de 1 %, régularisation fausse, une étiquette inversée, lot d'autres données, autre
   graine de l'attention : arrêt ;
5. non-déterminisme de la linéaire à 300 époques : arrêt ; 6. sonde de contrôle en échec à 3 et à 300 époques : arrêt ;
7. lecture : écart à 3 époques au-dessus de 10⁻⁴ ou déterminisme absent : refus de la lecture.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import numpy as np
import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.sondes import familles as fam
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import lecture_v2
from controle_ia.t07bbis import validation_imbriquee_v3 as v3

ICI = Path(__file__).resolve().parent
ORIGINE = ac.entrainer
SORTIE = {}


def _charger(nom: str, fichier: str):
    spec = importlib.util.spec_from_file_location(nom, ICI / fichier)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


v4 = _charger("validation_imbriquee_v4_diagnostic", "validation_imbriquee_v4.py")
essai = _charger("essai_amplification_lineaire_v1_diagnostic", "essai-amplification-lineaire-v1.py")
G_LIN, G_ATT = 11, 13


def graine_de(f):
    return G_LIN if f == "lineaire" else G_ATT


@pytest.fixture(scope="module", autouse=True)
def reglages_torch():
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(4)
    yield


@pytest.fixture(scope="module")
def quasi_copies():
    app, y, ctrl, _ = essai.jeu("residuel", 640, 256, 1024, 40, 120, 0.2, 0.9, 300.0, gabarits=0.4)
    return app, y, ctrl


@pytest.fixture(scope="module")
def repetition():
    app, y, ctrl, _ = essai.jeu("repetition", 320, 128, 256, 40, 120, 0.5, 0.0, 0.0)
    return app, y, ctrl


def carte_emulee(app):
    """`entrainer` de la carte émulée : le lot reçu est remplacé par celui des mêmes actions permutées (une fois, gardé)."""
    perm = np.random.default_rng(np.random.SeedSequence(20261116, spawn_key=(7,))).permutation(len(app))
    lp = ac.LotCarte([app[i] for i in perm], "cpu")

    def entrainer(lot, famille, nom, couche, y, l2, graine, epoques=300, pas=0.05):
        if lot.n != len(app):
            raise GardeArret("carte émulée : lot inattendu")
        return ORIGINE(lp, famille, nom, couche, np.asarray(y)[perm], l2, graine, epoques=epoques, pas=pas)
    return entrainer


def test_1_reproduction_arret_v3_sans_erreur_de_chaine(quasi_copies, monkeypatch):
    app, y, ctrl = quasi_copies
    monkeypatch.setattr(ac, "entrainer", carte_emulee(app))
    lot = ac.LotCarte(app, "cpu")
    finale = ac.entrainer(lot, "lineaire", "sonde-diag", 15, y, 1e-3, G_LIN)
    with pytest.raises(GardeArret, match=r"lineaire à 300 époques : contrôle carte-processeur : écart relatif") as e:
        v3.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",),
                                  sondes_300={"lineaire": finale})
    ecart = float(re.search(r"écart relatif ([0-9.e+-]+) >", str(e.value)).group(1))
    SORTIE["v3_ecart_300"] = ecart
    print(f"\n[reproduction] v3 : {e.value}")
    assert ecart > 0.1                      # de l'ordre de 1, comme la course (1,004), sans aucune erreur de chaîne


def test_2_cas_apres_correction_v4_passe_et_se_lit(quasi_copies, monkeypatch):
    app, y, ctrl = quasi_copies
    monkeypatch.setattr(ac, "entrainer", carte_emulee(app))
    lot = ac.LotCarte(app, "cpu")
    finale = ac.entrainer(lot, "lineaire", "sonde-diag", 15, y, 1e-3, G_LIN)
    r = v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire", "attention"),
                                  sondes_300={"lineaire": finale})
    print(f"\n[après correction] linéaire à 3 époques {r['lineaire']['ecart_relatif_max']:.3e} ; attention à 3 époques "
          f"{r['attention']['ecart_relatif_max']:.3e} ; information à 300 époques "
          f"{r['lineaire']['ecart_300_information']['ecart_relatif_max']:.3e}")
    SORTIE["v4"] = {f: r[f]["ecart_relatif_max"] for f in ("lineaire", "attention")}
    assert r["lineaire"]["epoques"] == 3 and r["attention"]["epoques"] == 3
    assert r["lineaire"]["ecart_relatif_max"] <= 1e-4 and r["attention"]["ecart_relatif_max"] <= 1e-4
    assert r["determinisme_lineaire"]["egal_au_bit"] is True and r["determinisme_attention"]["egal_au_bit"] is True
    assert r["lineaire"]["ecart_300_information"]["decide"] is False
    assert r["lineaire"]["ecart_300_information"]["ecart_relatif_max"] > 1e-4      # l'information garde l'écart de la v3
    lu = lecture_v2.exiger_controle_carte({"controle_carte_processeur": {**r, "cellule": "P-x", "pli": 0}, "variante": None})
    assert set(lu["ecarts"]) == {"lineaire", "attention"} and lu["determinisme_attention"] is True


def test_3_cas_sain_forme_de_la_repetition(repetition):
    app, y, ctrl = repetition
    lot = ac.LotCarte(app, "cpu")
    r = v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire", "attention"))
    assert r["lineaire"]["ecart_relatif_max"] <= 1e-4 and r["attention"]["ecart_relatif_max"] <= 1e-4
    assert r["lineaire"]["ecart_300_information"]["ecart_relatif_max"] <= 1e-4


def _artefact(monkeypatch, quoi):
    def entrainer(lot, famille, nom, couche, y, l2, graine, epoques=300, pas=0.05):
        if epoques != 3:
            return ORIGINE(lot, famille, nom, couche, y, l2, graine, epoques=epoques, pas=pas)
        if quoi == "l2":
            return ORIGINE(lot, famille, nom, couche, y, l2 * 100.0, graine, epoques=epoques, pas=pas)
        if quoi == "etiquette":
            y2 = np.array(y).copy()
            y2[0] = 1 - y2[0]
            return ORIGINE(lot, famille, nom, couche, y2, l2, graine, epoques=epoques, pas=pas)
        if quoi == "graine" and famille == "attention":
            return ORIGINE(lot, famille, nom, couche, y, l2, graine + 1, epoques=epoques, pas=pas)
        s = ORIGINE(lot, famille, nom, couche, y, l2, graine, epoques=epoques, pas=pas)
        if quoi == "poids":
            return fam.SondeLineaireJetons(s.nom, s.couche, s.agregation, s.w * 1.01, s.b, s.q, s.famille)
        return s
    monkeypatch.setattr(ac, "entrainer", entrainer)


@pytest.mark.parametrize("quoi,famille", [("poids", "lineaire"), ("poids", "attention"), ("l2", "lineaire"),
                                          ("l2", "attention"), ("etiquette", "lineaire"), ("etiquette", "attention"),
                                          ("graine", "attention")])
def test_4_artefacts_a_3_epoques_arretent(repetition, monkeypatch, quoi, famille):
    app, y, ctrl = repetition
    lot = ac.LotCarte(app, "cpu")
    _artefact(monkeypatch, quoi)
    with pytest.raises(GardeArret, match=rf"{famille} à 3 époques : contrôle carte-processeur : écart relatif") as e:
        v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=(famille,))
    SORTIE.setdefault("artefacts", {})[f"{quoi}/{famille}"] = str(e.value)
    print(f"\n[artefact {quoi}/{famille}] {e.value}")


def test_4bis_lot_d_autres_donnees_arrete(repetition):
    app, y, ctrl = repetition
    autre, _, _, _ = essai.jeu("repetition", 320, 8, 256, 40, 120, 0.5, 0.0, 0.0, suffixe="autre-couche")
    lot = ac.LotCarte(autre, "cpu")                 # la carte apprend sur d'autres activations (autre couche, autre série)
    with pytest.raises(GardeArret, match=r"lineaire à 3 époques : contrôle carte-processeur"):
        v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",))


def test_5_non_determinisme_lineaire_a_300_epoques_arrete(repetition, monkeypatch):
    app, y, ctrl = repetition
    lot = ac.LotCarte(app, "cpu")

    def entrainer(lot, famille, nom, couche, y, l2, graine, epoques=300, pas=0.05):
        s = ORIGINE(lot, famille, nom, couche, y, l2, graine, epoques=epoques, pas=pas)
        if nom.endswith("-bis"):
            w = s.w.copy()
            w[0] = np.nextafter(w[0], np.inf)
            return fam.SondeLineaireJetons(s.nom, s.couche, s.agregation, w, s.b, s.q, s.famille)
        return s
    monkeypatch.setattr(ac, "entrainer", entrainer)
    with pytest.raises(GardeArret, match=r"lineaire à 300 époques réapprise sur la carte : paramètres différents au bit près"):
        v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",))


@pytest.mark.parametrize("ou", ["e3", "e300-bis"])
def test_6_sonde_de_controle_en_echec_arrete(repetition, monkeypatch, ou):
    app, y, ctrl = repetition
    lot = ac.LotCarte(app, "cpu")

    def entrainer(lot, famille, nom, couche, y, l2, graine, epoques=300, pas=0.05):
        if nom.endswith(f"-{ou}"):
            raise ac.SondeEnEchec(f"sonde {nom} : perte non finie à l'époque 0")
        return ORIGINE(lot, famille, nom, couche, y, l2, graine, epoques=epoques, pas=pas)
    monkeypatch.setattr(ac, "entrainer", entrainer)
    with pytest.raises(GardeArret, match=r"sonde (de contrôle )?en échec"):
        v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",))


def test_7_lecture_refuse_un_champ_v4_hors_tolerance(repetition):
    app, y, ctrl = repetition
    lot = ac.LotCarte(app, "cpu")
    r = v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",), informer_300=False)
    doc = {"controle_carte_processeur": {**r, "cellule": "P-x", "pli": 0}, "variante": "r1"}
    assert lecture_v2.exiger_controle_carte(doc)["ecarts"]["lineaire"] <= 1e-4
    mauvais = {**doc, "controle_carte_processeur": {**doc["controle_carte_processeur"],
                                                     "lineaire": {**r["lineaire"], "ecart_relatif_max": 2e-4}}}
    with pytest.raises(lecture_v2.RefusLecture):
        lecture_v2.exiger_controle_carte(mauvais)
    sans_det = {"controle_carte_processeur": {**r, "attention": {"ecart_relatif_max": 1e-9}, "cellule": "P-x", "pli": 0},
                "variante": None}                      # attention présente, déterminisme de l'attention absent
    with pytest.raises(lecture_v2.RefusLecture, match="déterminisme de l'attention"):
        lecture_v2.exiger_controle_carte(sans_det)


def test_8_horizon_hors_bornes_refuse(repetition):
    app, y, ctrl = repetition
    lot = ac.LotCarte(app, "cpu")
    with pytest.raises(GardeArret, match="horizon du contrôle"):
        v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, epoques_controle=300)
