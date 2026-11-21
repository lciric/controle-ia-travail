"""Épreuves (R5) du second addendum d'écart de B bis (EC-8 révisé) : contrôle carte-processeur v4, mesure de dispersion entre deux
ordres de calcul, lecture v3, registre v2, marche v4, lanceur et amorce v4. Données **fabriquées** seulement (aucune donnée de 7a
ni de 7b, aucune activation, aucune sortie de course) ; processeur seulement.

- A. Chaque fichier copié = le précédent + un différentiel déclaré (`aide_t07bbis_differentiels_v4.COUPLES`), égalité exacte.
- B. Contrôle v4 : (1) le contrôle v3 arrête la carte émulée sur le jeu des quasi-copies sans erreur de chaîne ; (2) la v4 passe sur
  le même jeu, information à 300 époques au-dessus de 10⁻⁴, lue par `lecture_v3` (discriminant « écart ») ; (3) **cas sain du
  régime anisotrope** (réserve R-E) : sans quasi-copie, 300 époques divergentes, la v4 passe ; (4) cas sain de la forme de la
  répétition (discriminant « accord ») ; (5) artefacts à 3 époques : arrêt ; (6) non-déterminisme de chaque famille : arrêt ;
  (7) sonde de contrôle en échec : arrêt ; (8) horizon hors bornes : refus.
- C. Lecture v3 : champ du contrôle (cas sain et artefacts) ; R-PILE étendue à la linéaire, résumé de la dispersion ; point (7).
- D. Registre : ligne `CODE-BBIS` remplacée une seule fois (lecture et écriture, ordre propre) ; garde de création (course de plus).
- E. Mesure de dispersion (jouet) : scores fermés de l'ordre 2, ordre inverse réellement joué, aucune aire écrite, échec d'une
  sonde, erreur d'exécution (mesure « non faite », rien de partiel), garde qui arrête, clés désalignées, compte des apprentissages.
- F. Marche v4 et lecture v3 de bout en bout en mode jouet, avec une ligne `CODE-BBIS` remplacée (si la chaîne de T0.6 est là).
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest
import torch

import aide_t07bbis_differentiels_v4 as dif
import aide_t07bbis_jeux_v4 as J
from controle_ia.gardes import GardeArret
from controle_ia.sondes import familles as fam
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import commun_v1 as cm
from controle_ia.t07bbis import lecture_v3 as lv3
from controle_ia.t07bbis import registre_bbis_v2 as rb2
from controle_ia.t07bbis import validation_imbriquee_v3 as v3
from controle_ia.t07bbis import validation_imbriquee_v4 as v4

RACINE = Path(__file__).resolve().parents[1]
ORIGINE = ac.entrainer
G_LIN, G_ATT = 11, 13


def graine_de(f):
    return G_LIN if f == "lineaire" else G_ATT


@pytest.fixture(scope="module", autouse=True)
def reglages_torch():
    avant, fils = torch.are_deterministic_algorithms_enabled(), torch.get_num_threads()
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(min(4, fils))
    yield
    torch.use_deterministic_algorithms(avant)
    torch.set_num_threads(fils)


# ------------------------------------------------------------------------------------------------------------ A. différentiels

@pytest.mark.parametrize("neuf", sorted(dif.COUPLES))
def test_A_version_neuve_egale_a_la_precedente_plus_le_differentiel_declare(neuf):
    ancien, couples = dif.COUPLES[neuf]
    assert (RACINE / neuf).read_text(encoding="utf-8") == dif.appliquer((RACINE / ancien).read_text(encoding="utf-8"), couples)


def test_A_amorce_et_lanceur_v4():
    t = (RACINE / "scripts/amorce_bbis_v4.sh").read_text(encoding="utf-8")
    motifs = t.split("MOTIFS='", 1)[1].split("'", 1)[0].splitlines()
    for v in ("v1", "v2", "v3", "v4"):
        assert f"/scripts/amorce_bbis_{v}.sh*" in motifs and f"/scripts/lancer_bbis_{v}.sh*" in motifs
    assert t.count("controle_ia.t07bbis.marche_v4") == 3 and "t07bbis.marche_v3" not in t
    assert re.findall(r"^BR_SORTIE=(.*)$", t, re.M) == ["donnees/t07-etape-b-bis-v2"]
    assert re.findall(r"^MIN_ESSAIS=(\d+)$", t, re.M) == [str(dif.MIN_ESSAIS_V4)] and dif.MIN_ESSAIS_V4 > 115
    lz = (RACINE / "scripts/lancer_bbis_v4.sh").read_text(encoding="utf-8")
    assert lz.count("amorce_bbis_v4.sh") == 7 and "amorce_bbis_v3" not in lz
    assert "controle_ia.t07bbis.registre_bbis_v2" in lz and "-m controle_ia.t07bbis.registre_bbis_v1" not in lz
    assert v4.EPOQUES_CONTROLE == lv3.EPOQUES_CONTROLE_V4 and v4.CHAMP_O2 == lv3.CHAMP_O2


# ------------------------------------------------------------------------------------------------------------ B. contrôle v4

@pytest.fixture(scope="module")
def quasi_copies():
    app, y, ctrl, _ = J.jeu_residuel("residuel", 640, 256, 1024, 40, 120, 0.2, 0.9, 300.0, 1, gabarits=0.4)
    return app, y, ctrl


@pytest.fixture(scope="module")
def anisotrope():
    app, y, ctrl, _ = J.jeu_anisotrope(13)
    return app, y, ctrl


@pytest.fixture(scope="module")
def repetition():
    app, y, ctrl, _ = J.jeu_residuel("repetition", 320, 128, 256, 40, 120, 0.5, 0.0, 0.0, 2)
    return app, y, ctrl


def _doc(r, variante=None):
    return {"controle_carte_processeur": {**r, "cellule": "P-x", "pli": 0}, "variante": variante}


def test_B1_le_controle_v3_arrete_la_carte_emulee_sans_erreur_de_chaine(quasi_copies, monkeypatch):
    app, y, ctrl = quasi_copies
    monkeypatch.setattr(ac, "entrainer", J.carte_emulee(ac, app, ORIGINE))
    lot = ac.LotCarte(app, "cpu")
    finale = ac.entrainer(lot, "lineaire", "sonde-essai", 15, y, 1e-3, G_LIN)
    with pytest.raises(GardeArret, match=r"lineaire à 300 époques : contrôle carte-processeur : écart relatif") as e:
        v3.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",), sondes_300={"lineaire": finale})
    assert float(re.search(r"écart relatif ([0-9.e+-]+) >", str(e.value)).group(1)) > 0.1


@pytest.mark.parametrize("jeu", ["quasi_copies", "anisotrope"])
def test_B2_B3_la_v4_passe_malgre_300_epoques_divergentes(jeu, request, monkeypatch):
    app, y, ctrl = request.getfixturevalue(jeu)
    monkeypatch.setattr(ac, "entrainer", J.carte_emulee(ac, app, ORIGINE))
    lot = ac.LotCarte(app, "cpu")
    finale = ac.entrainer(lot, "lineaire", "sonde-essai", 15, y, 1e-3, G_LIN)
    familles = ("lineaire", "attention") if jeu == "quasi_copies" else ("lineaire",)
    r = v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=familles, sondes_300={"lineaire": finale})
    print(f"\n[{jeu}] " + " ; ".join(f"{f} à 3 époques {r[f]['ecart_relatif_max']:.3e}" for f in familles)
          + f" ; information à 300 époques {r['lineaire']['ecart_300_information']['ecart_relatif_max']:.3e}")
    for f in familles:
        assert r[f]["epoques"] == 3 and r[f]["ecart_relatif_max"] <= 1e-6 and r[f"determinisme_{f}"]["egal_au_bit"] is True
    assert r["version_controle"] == "v4" and r["lineaire"]["ecart_300_information"]["decide"] is False
    assert r["lineaire"]["ecart_300_information"]["ecart_relatif_max"] > 1e-4         # 300 époques divergentes
    lu = lv3.exiger_controle_carte(_doc(r, None if jeu == "quasi_copies" else "r1"))
    assert set(lu["ecarts"]) == set(familles) and lu["discriminant"] == lv3.DISCRIMINANT["ecart"]


def test_B4_cas_sain_forme_de_la_repetition(repetition):
    app, y, ctrl = repetition
    r = v4.controle_deux_horizons(ac.LotCarte(app, "cpu"), app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire", "attention"))
    assert max(r["lineaire"]["ecart_relatif_max"], r["attention"]["ecart_relatif_max"]) <= 1e-4
    assert r["lineaire"]["ecart_300_information"]["ecart_relatif_max"] <= 1e-4
    assert lv3.exiger_controle_carte(_doc(r))["discriminant"] == lv3.DISCRIMINANT["accord"]


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
def test_B5_artefacts_a_3_epoques_arretent(repetition, monkeypatch, quoi, famille):
    app, y, ctrl = repetition
    lot = ac.LotCarte(app, "cpu")
    _artefact(monkeypatch, quoi)
    with pytest.raises(GardeArret, match=rf"{famille} à 3 époques : contrôle carte-processeur : écart relatif"):
        v4.controle_deux_horizons(lot, app, y, 15, 1e-3, graine_de, ctrl, familles=(famille,))


def test_B5_lot_d_autres_donnees_arrete(repetition):
    app, y, ctrl = repetition
    autre, _, _, _ = J.jeu_residuel("repetition", 320, 8, 256, 40, 120, 0.5, 0.0, 0.0, 3)
    with pytest.raises(GardeArret, match=r"lineaire à 3 époques : contrôle carte-processeur"):
        v4.controle_deux_horizons(ac.LotCarte(autre, "cpu"), app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",))


@pytest.mark.parametrize("famille", ["lineaire", "attention"])
def test_B6_non_determinisme_a_300_epoques_arrete(repetition, monkeypatch, famille):
    app, y, ctrl = repetition

    def entrainer(lot, f, nom, couche, y, l2, graine, epoques=300, pas=0.05):
        s = ORIGINE(lot, f, nom, couche, y, l2, graine, epoques=epoques, pas=pas)
        if nom.endswith("-bis"):
            w = s.w.copy()
            w[0] = np.nextafter(w[0], np.inf)
            return fam.SondeLineaireJetons(s.nom, s.couche, s.agregation, w, s.b, s.q, s.famille)
        return s
    monkeypatch.setattr(ac, "entrainer", entrainer)
    with pytest.raises(GardeArret, match=rf"{famille} à 300 époques réapprise sur la carte : paramètres différents au bit près"):
        v4.controle_deux_horizons(ac.LotCarte(app, "cpu"), app, y, 15, 1e-3, graine_de, ctrl, familles=(famille,))


@pytest.mark.parametrize("ou", ["e3", "e300", "e300-bis"])
def test_B7_sonde_de_controle_en_echec_arrete(repetition, monkeypatch, ou):
    app, y, ctrl = repetition

    def entrainer(lot, famille, nom, couche, y, l2, graine, epoques=300, pas=0.05):
        if nom.endswith(f"-{ou}"):
            raise ac.SondeEnEchec(f"sonde {nom} : perte non finie à l'époque 0")
        return ORIGINE(lot, famille, nom, couche, y, l2, graine, epoques=epoques, pas=pas)
    monkeypatch.setattr(ac, "entrainer", entrainer)
    with pytest.raises(GardeArret, match=r"sonde (de contrôle )?en échec.*erreur de chaîne"):
        v4.controle_deux_horizons(ac.LotCarte(app, "cpu"), app, y, 15, 1e-3, graine_de, ctrl, familles=("lineaire",))


def test_B8_horizon_hors_bornes_refuse(repetition):
    app, y, ctrl = repetition
    for h in (0, 300):
        with pytest.raises(GardeArret, match="horizon du contrôle"):
            v4.controle_deux_horizons(ac.LotCarte(app, "cpu"), app, y, 15, 1e-3, graine_de, ctrl, epoques_controle=h)


# ------------------------------------------------------------------------------------------------------------ C. lecture v3

SAIN = {"lineaire": {"ecart_relatif_max": 2e-8, "epoques": 3, "ecart_300_information": {"ecart_relatif_max": 1.004,
                                                                                         "epoques": 300, "decide": False}},
        "attention": {"ecart_relatif_max": 3e-7, "epoques": 3}, "determinisme_lineaire": {"egal_au_bit": True, "epoques": 300},
        "determinisme_attention": {"egal_au_bit": True, "epoques": 300}, "version_controle": "v4", "cellule": "P-S50", "pli": 0}


def _sondes(controle, variante=None, sources=None, dispersion=None):
    d = {"controle_carte_processeur": controle, "variante": variante,
         "sources": sources if sources is not None else {"P-S50": {"e0": {"famille": "lineaire",
                                                                          "enc": {"reglage": "lineaire-c7-l2_0.1"}}}}}
    if dispersion is not None:
        d["dispersion_ordres_calcul"] = dispersion
    return d


def test_C1_champ_du_controle_v4_sain_et_artefacts():
    r = lv3.exiger_controle_carte(_sondes(SAIN))
    assert r["ecarts"] == {"lineaire": 2e-8, "attention": 3e-7} and r["determinisme"] == {"lineaire": True, "attention": True}
    assert r["discriminant"] == lv3.DISCRIMINANT["ecart"] and r["information_300"]["ecart_relatif_max"] == 1.004
    lin = {k: v for k, v in SAIN.items() if k not in ("attention", "determinisme_attention")}
    assert lv3.exiger_controle_carte(_sondes(lin, variante="r1"))["ecarts"] == {"lineaire": 2e-8}
    refus = {**SAIN["lineaire"]["ecart_300_information"], "ecart_relatif_max": None, "refus": "écart non fini"}
    assert (lv3.exiger_controle_carte(_sondes({**SAIN, "lineaire": {**SAIN["lineaire"], "ecart_300_information": refus}}))
            ["discriminant"] == lv3.DISCRIMINANT["ecart"])
    sans = lambda *ks: {k: v for k, v in SAIN.items() if k not in ks}
    artefacts = [None, sans("version_controle"), {**SAIN, "version_controle": "v3"},
                 {**SAIN, "lineaire": {**SAIN["lineaire"], "epoques": 300}}, {**SAIN, "attention": {**SAIN["attention"], "epoques": 300}},
                 sans("determinisme_lineaire"), {**SAIN, "determinisme_lineaire": {"egal_au_bit": False}}, sans("determinisme_attention"),
                 {**SAIN, "lineaire": {k: v for k, v in SAIN["lineaire"].items() if k != "ecart_300_information"}},
                 {**SAIN, "lineaire": {**SAIN["lineaire"], "ecart_300_information": {"ecart_relatif_max": 1.0, "decide": True}}},
                 {**SAIN, "lineaire": {**SAIN["lineaire"], "ecart_300_information": {"ecart_relatif_max": True, "decide": False}}},
                 {**SAIN, "attention": {"sans_objet": "simulé"}}, {**SAIN, "lineaire": {**SAIN["lineaire"], "ecart_relatif_max": 2e-4}},
                 {**SAIN, "lineaire": {**SAIN["lineaire"], "ecart_relatif_max": float("nan")}}]
    for a in artefacts:
        with pytest.raises(lv3.RefusLecture, match="arrêt de la lecture"):
            lv3.exiger_controle_carte(_sondes(a))


def test_C2_r_pile_etendue_a_la_lineaire_et_point_7():
    r = lv3.reserve_pile(_sondes(SAIN))                                     # linéaires seulement : la v2 n'écrivait rien
    assert len(r) == 1 and r[0].startswith(lv3.RESERVES_FIXES["R-PILE"]) and "linéaires : P-S50 e0, P-S50 e0 (ENC)" in r[0]
    assert "mesure non faite" not in r[0] and r[0].endswith(": non lue")
    att = {"P-S50": {"e0": {"famille": "attention", "enc": {"reglage": "lineaire-c7-l2_0.1"}},
                     "e1": {"famille": "lineaire", "enc": {"reglage": "attention-c15-l2_0.01"}}},
           "P-S100": {"e0": {"echec": "x", "famille": "attention"}}}
    r = lv3.reserve_pile(_sondes(SAIN, sources=att), {"non_faite": "RuntimeError: mémoire"})
    assert "linéaires : P-S50 e0 (ENC), P-S50 e1" in r[0] and "« attention » : P-S50 e0, P-S50 e1 (ENC)" in r[0]
    assert r[0].endswith("mesure non faite (RuntimeError: mémoire)") and "P-S100" not in r[0]
    d = {"cellules_lues": 10, "ecart_max": 0.0312, "cellule_ecart_max": "P-S25", "plis_reglage_change": 3, "plis_compares": 10}
    assert lv3.phrase_dispersion(d).endswith("écart absolu maximal 0.0312 (P-S25) sur 10 cellules lues ; réglage retenu changé "
                                             "dans 3 plis sur 10")
    assert lv3.reserve_pile(_sondes(SAIN, sources={"P-S50": {"e0": {"echec": "x"}}})) == []
    assert lv3.RESERVES_FIXES["R-PILE"].startswith("R-PILE : sonde finale (linéaire ou « attention ») reproductible au bit près")
    assert "(7) une aire de sonde, linéaire ou « attention », est celle d'une sonde parmi celles" in lv3.SECTION_D
    assert "elle est mesurée entre deux ordres de calcul de la carte, comme information seulement" in lv3.SECTION_D


# ------------------------------------------------------------------------------------------------------------ D. registre

def _t(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def _l(cle, date, chemin="registres/x.json", sha="a" * 64):
    return f"| {cle} | {date} | {chemin} | {sha} |\n"


def _registre(tmp_path, *lignes):
    p = tmp_path / f"registre-{len(list(tmp_path.glob('registre-*.md')))}.md"
    p.write_text("# essai\n\n" + "".join(lignes), encoding="utf-8")
    return p


BASE = [_l("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z"), _l("CODE-BBIS", "2026-11-16T12:57:51Z", "registres/c1.json"),
        _l("GO-BBIS", "2026-11-16T12:58:51Z")]


def test_D1_code_bbis_remplacee_une_seule_fois_a_la_lecture(tmp_path):
    p = _registre(tmp_path, *BASE, _l("CODE-BBIS", "2026-11-17T09:00:00Z", "registres/c2.json", "b" * 64))
    r = lv3.lire_lignes(p, lv3.CLES_PROPRES, ("CODE-BBIS",), propre=True, remplacables=lv3.REMPLACABLES_PROPRES)
    assert r["CODE-BBIS"]["chemin"] == "registres/c2.json" and r["CODE-BBIS"]["remplace"]["chemin"] == "registres/c1.json"
    lv3.exiger_ordre_propre(r)
    with pytest.raises(lv3.RefusLecture, match="en double"):                     # sans le droit de remplacer : refus (v2)
        lv3.lire_lignes(p, lv3.CLES_PROPRES, ("CODE-BBIS",), propre=True)
    trois = _registre(tmp_path, *BASE, _l("CODE-BBIS", "2026-11-17T09:00:00Z"), _l("CODE-BBIS", "2026-11-17T10:00:00Z"))
    avant = _registre(tmp_path, *BASE, _l("CODE-BBIS", "2026-11-16T12:57:51Z"))
    go2 = _registre(tmp_path, *BASE, _l("GO-BBIS", "2026-11-17T09:00:00Z"))
    for q, motif in ((trois, "en double"), (avant, "pas strictement postérieure"), (go2, "en double")):
        with pytest.raises(lv3.RefusLecture, match=motif):
            lv3.lire_lignes(q, lv3.CLES_PROPRES, ("CODE-BBIS",), propre=True, remplacables=lv3.REMPLACABLES_PROPRES)
    avant_go = _registre(tmp_path, BASE[0], BASE[1], _l("CODE-BBIS", "2026-11-16T12:58:00Z"), BASE[2])
    r = lv3.lire_lignes(avant_go, lv3.CLES_PROPRES, (), propre=True, remplacables=lv3.REMPLACABLES_PROPRES)
    with pytest.raises(lv3.RefusLecture, match="CODE-BBIS .* pas strictement antérieure|GO-BBIS .* pas strictement antérieure"):
        lv3.exiger_ordre_propre(r)
    sc = _registre(tmp_path, *BASE, _l("SCORES-BBIS", "2026-11-17T08:00:00Z"), _l("CODE-BBIS", "2026-11-17T09:00:00Z"))
    with pytest.raises(lv3.RefusLecture, match="pas strictement antérieure à SCORES-BBIS"):
        lv3.exiger_ordre_propre(lv3.lire_lignes(sc, lv3.CLES_PROPRES, (), propre=True, remplacables=lv3.REMPLACABLES_PROPRES))
    simple = lv3.lire_lignes(_registre(tmp_path, *BASE), lv3.CLES_PROPRES, (), propre=True, remplacables=lv3.REMPLACABLES_PROPRES)
    assert "remplace" not in simple["CODE-BBIS"]
    lv3.exiger_ordre_propre(simple)


def test_D2_ecriture_du_remplacement_et_garde_de_creation(tmp_path):
    d = tmp_path / "depot"
    (d / "registres").mkdir(parents=True)
    ajouter = lambda cle, date: rb2.ajouter_ligne_propre(d, rb2.REGISTRE_PROPRE, cle, _t(date), "registres/x.json", "a" * 64)
    ajouter("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z")
    ajouter("CODE-BBIS", "2026-11-16T12:57:51Z")
    with pytest.raises(GardeArret, match="déjà présente"):                       # avant GO-BBIS : refus
        ajouter("CODE-BBIS", "2026-11-16T12:58:00Z")
    ajouter("GO-BBIS", "2026-11-16T12:58:51Z")
    feu = "feu écrit : GO-2026-11-14-09"
    with pytest.raises(GardeArret, match="seconde relance : seulement sous le second addendum"):
        rb2.exiger_creation(d, feu + " ; GO-2026-11-16-11", _t("2026-11-17T10:00:00Z"), 2)   # CODE-BBIS non remplacée
    ajouter("CODE-BBIS", "2026-11-17T09:00:00Z")
    for cle in ("CODE-BBIS", "GO-BBIS", "SCELLEMENT-BBIS"):
        with pytest.raises(GardeArret, match="déjà présente"):
            ajouter(cle, "2026-11-17T09:30:00Z")
    assert rb2.cles_bbis_presentes(d / rb2.REGISTRE_PROPRE).count("CODE-BBIS") == 2
    assert rb2.exiger_creation(d, feu + " ; GO-2026-11-16-11", _t("2026-11-17T10:00:00Z"), 2)["relances"] == 2
    with pytest.raises(GardeArret, match="seconde relance"):
        rb2.exiger_creation(d, feu, _t("2026-11-17T10:00:00Z"), 2)                # feu sans GO-2026-11-16-11
    with pytest.raises(GardeArret, match="troisième relance est exclue"):
        rb2.exiger_creation(d, feu + " ; GO-2026-11-16-11", _t("2026-11-17T10:00:00Z"), 3)
    with pytest.raises(GardeArret, match="21 novembre"):
        rb2.exiger_creation(d, feu + " ; GO-2026-11-16-11", _t("2026-11-21T12:00:01Z"), 2)
    with pytest.raises(GardeArret, match="feu écrit"):
        rb2.exiger_creation(d, "GO-2026-11-16-11", _t("2026-11-17T10:00:00Z"), 2)
    ajouter("SCORES-BBIS", "2026-11-17T20:00:00Z")
    e = tmp_path / "depot2"
    (e / "registres").mkdir(parents=True)
    for cle, date in (("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z"), ("CODE-BBIS", "2026-11-16T12:57:51Z"),
                      ("GO-BBIS", "2026-11-16T12:58:51Z"), ("SCORES-BBIS", "2026-11-16T20:00:00Z")):
        rb2.ajouter_ligne_propre(e, rb2.REGISTRE_PROPRE, cle, _t(date), "registres/x.json", "a" * 64)
    with pytest.raises(GardeArret, match="déjà présente"):                       # après SCORES-BBIS : refus
        rb2.ajouter_ligne_propre(e, rb2.REGISTRE_PROPRE, "CODE-BBIS", _t("2026-11-17T09:00:00Z"), "registres/x.json", "a" * 64)


# ------------------------------------------------------------------------------------------------------------ E. mesure

@pytest.fixture(scope="module")
def sources_jouet():
    from test_t07bbis_apprentissage_v1 import ActsJouet
    from controle_ia.t06.test_croise import partition_plis
    acts = ActsJouet()
    g = cm.Graines(2 ** 100 + 7, reelle=False)
    ctx = v4.Contexte(acts, g, acts.couches, "cpu", reelle=False, epoques=10, n_plis_internes=3)
    taches = sorted({acts.tache(k) for k in acts.cles("O", "honnete")})
    plis = partition_plis(taches, 3)
    sorties = {}
    for cellule, pos in (("P-S100", "S100"), ("P-instruit", "saboteur")):
        for k in (0, 1):
            sorties[(cellule, k)] = (pos, v4.apprendre_source(ctx, cellule, pos, v4.plan_de_notation(pos, (0.5, 1.0)), k, plis,
                                                              taches, n_reetiquetages=2, n_directions=4))
    return ctx, plis, sorties


def _copie(sorties):
    return {c: (p, {**r, "tableaux": dict(r["tableaux"]), "meta": dict(r["meta"])}) for c, (p, r) in sorties.items()}


def _cles_dict(x):
    if isinstance(x, dict):
        for k, v in x.items():
            yield str(k)
            yield from _cles_dict(v)
    elif isinstance(x, list):
        for v in x:
            yield from _cles_dict(v)


def test_E1_mesure_scores_fermes_de_l_ordre_2_sans_aire(sources_jouet):
    ctx, plis, sorties = sources_jouet
    s = _copie(sorties)
    resume = v4.mesurer_dispersion(ctx, s, plis, (0.5, 1.0))
    assert resume["decide"] is False and set(resume["sources"].values()) == {"jouée"} and len(resume["sources"]) == 4
    for (cellule, k), (pos, res) in s.items():
        groupes = [v4.nom_groupe(g) for g in v4.plan_de_notation(pos, (0.5, 1.0))["sonde"]]
        for g in groupes:
            o2, o1 = res["tableaux"][f"{g}__sonde_o2"], res["tableaux"][f"{g}__sonde"]
            assert o2.shape == o1.shape and np.all(np.isfinite(o2))
        m = res["meta"]["ordre2"]
        assert m["ordre"] == "inverse" and m["reglage"] and "echec" not in m and "o2__w" in res["tableaux"]
        assert not any(c.startswith("aire") for c in _cles_dict(m)) and not any(c.startswith("aire") for c in _cles_dict(resume))
        assert "ordre2" not in sorties[(cellule, k)][1]["meta"]                  # l'original n'est pas touché (copie)


def test_E2_l_ordre_inverse_est_joue_et_les_comptes_sont_ceux_declares(sources_jouet, monkeypatch):
    ctx, plis, sorties = sources_jouet
    vus, n = [], {"entrainements": 0}
    vrai_lot, vrai_ent = ac.LotCarte, ac.entrainer

    class Espion(vrai_lot):
        def __init__(self, sequences, appareil="cpu"):
            vus.append([np.asarray(x) for x in sequences])
            super().__init__(sequences, appareil)

    def compte(*a, **k):
        n["entrainements"] += 1
        return vrai_ent(*a, **k)
    monkeypatch.setattr(ac, "LotCarte", Espion)
    monkeypatch.setattr(ac, "entrainer", compte)
    pos, res = sorties[("P-S100", 0)]
    o2 = v4.apprendre_recette_ordre2(ctx, "sonde", "P-S100", 0, ("O", pos), ("O", cm.H),
                                     sorted(t for t, p in plis.items() if p != 0), sorted(t for t, p in plis.items() if p == 0),
                                     res["meta"]["plis_internes"])
    finale = vus[-1]
    assert len(finale) == len(res["sequences_app"]) and o2["reglage"]["couche"] in ctx.couches
    a_app = v4.v1._actions(ctx.acts, [("O", pos), ("O", cm.H)], sorted(t for t, p in plis.items() if p != 0))
    seq_app = [np.asarray(x) for x in v4.v1._sequences(ctx.acts, a_app, o2["reglage"]["couche"])]
    assert all(np.array_equal(a, b) for a, b in zip(finale, seq_app[::-1]))           # ordre inverse, mêmes actions
    assert not np.array_equal(finale[0], seq_app[0])
    grille = len(cm.grille(ctx.couches, ctx.familles))
    assert n["entrainements"] == grille * len(res["meta"]["plis_internes"]) + 1
    assert v4.apprentissages_mesure(5, 18, 4) == 5 * 2 * (18 * 4 + 1)


def test_E3_erreur_d_execution_mesure_non_faite_sans_rien_de_partiel(sources_jouet, monkeypatch):
    ctx, plis, sorties = sources_jouet
    s = _copie(sorties)
    vrai = v4.apprendre_recette_ordre2
    appels = []

    def panne(*a, **k):
        appels.append(1)
        if len(appels) == 2:
            raise RuntimeError("CUDA out of memory (simulée)")
        return vrai(*a, **k)
    monkeypatch.setattr(v4, "apprendre_recette_ordre2", panne)
    r = v4.mesurer_dispersion(ctx, s, plis, (0.5, 1.0))
    assert r["non_faite"].startswith("RuntimeError: CUDA out of memory") and "sources" not in r
    for _, res in s.values():
        assert not [n for n in res["tableaux"] if "o2" in n] and "ordre2" not in res["meta"]


def test_E4_une_garde_arrete_la_marche(sources_jouet, monkeypatch):
    ctx, plis, sorties = sources_jouet

    def garde(*a, **k):
        raise GardeArret("tâche du pli lu dans un apprentissage (simulée)")
    monkeypatch.setattr(v4, "apprendre_recette_ordre2", garde)
    with pytest.raises(GardeArret, match="simulée"):
        v4.mesurer_dispersion(ctx, _copie(sorties), plis, (0.5, 1.0))


def test_E5_sonde_de_l_ordre_2_en_echec_et_cles_desalignees(sources_jouet, monkeypatch):
    ctx, plis, sorties = sources_jouet
    s = _copie(sorties)
    vrai = ac.entrainer

    def echec(lot, famille, nom, *a, **k):
        if nom == "sonde-ordre2-P-S100-e1":
            raise ac.SondeEnEchec("perte non finie (simulée)")
        return vrai(lot, famille, nom, *a, **k)
    monkeypatch.setattr(ac, "entrainer", echec)
    r = v4.mesurer_dispersion(ctx, s, plis, (0.5, 1.0))
    assert r["sources"]["P-S100/e1"].startswith("échec") and "perte non finie" in s[("P-S100", 1)][1]["meta"]["ordre2"]["echec"]
    assert not [n for n in s[("P-S100", 1)][1]["tableaux"] if "o2" in n] and "O-S100__sonde_o2" in s[("P-S100", 0)][1]["tableaux"]
    monkeypatch.setattr(ac, "entrainer", vrai)
    t = _copie(sorties)
    t[("P-S100", 0)][1]["tableaux"]["O-S100__cles"] = t[("P-S100", 0)][1]["tableaux"]["O-S100__cles"][::-1]
    with pytest.raises(GardeArret, match="clés du groupe O-S100 différentes"):
        v4.mesurer_dispersion(ctx, t, plis, (0.5, 1.0))


# ------------------------------------------------------------------------------------------------------------ F. bout en bout

def test_F_marche_v4_et_lecture_v3_de_bout_en_bout_en_mode_jouet(tmp_path_factory):
    import aide_t07bbis_jouet_v1 as aide
    from controle_ia.scellement import empreinte, sceller
    from controle_ia.t07bbis import marche_v4
    if not aide.disponible():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    run_b, entropie = "20261118-090000-bbis-jouet", 2 ** 100 + 11
    d = aide.course_jouet(tmp_path_factory.mktemp("depot-bbis-v4"))
    r = marche_v4.marche(d, aide.RUN, run_b, entropie, d.parent / f"{d.name}-travail", "cpu",
                         essai={"epoques": 15, "n_plis_internes": 3, "n_directions": 12, "n_reetiquetages": 3, "n_controle": 6,
                                "n_chemin": 3})
    assert r.get("scores_ecrits"), r
    doc = json.loads((d / r["sondes_bbis"]).read_text(encoding="utf-8"))
    c = doc["controle_carte_processeur"]
    assert c["version_controle"] == "v4" and c["lineaire"]["epoques"] == 3 and c["attention"]["epoques"] == 3
    assert c["determinisme_lineaire"]["egal_au_bit"] and c["determinisme_attention"]["egal_au_bit"]
    disp = doc["dispersion_ordres_calcul"]
    assert disp["decide"] is False and "non_faite" not in disp and set(disp["sources"].values()) <= {"jouée"}
    assert all("ordre2" in m for par in doc["sources"].values() for m in par.values() if "echec" not in m)
    assert not any(k.startswith("aire") for k in _cles_dict({k: v for k, v in doc.items() if k != "plis"}))
    v = d / "docs" / "verdicts" / "verdict-p3bis-jouet.md"
    v.parent.mkdir(parents=True)
    v.write_text("verdict jouet\n", encoding="utf-8")
    sha_issue = aide.sceller_json(d, "docs/verdicts/issue-p3bis-jouet.json",
                                  {"issue": "vu", "ligne": 5, "verdict": "docs/verdicts/verdict-p3bis-jouet.md",
                                   "verdict_sha256": empreinte(v)})
    sha_m = (d / "runs" / aide.RUN / "manifeste.json.sha256").read_text(encoding="utf-8").split()[0]
    (d / "registres").mkdir(exist_ok=True)
    (d / rb2.REGISTRE_PARTAGE).write_text(
        "# registre jouet\n\n" + _l("RUN-CONFIRMATION-T06", "2026-11-12T05:00:00Z", f"runs/{aide.RUN}/manifeste.json", sha_m)
        + _l("VERDICT-P3BIS", "2026-11-13T05:00:00Z", "docs/verdicts/issue-p3bis-jouet.json", sha_issue), encoding="utf-8")
    sha_abs = aide.sceller_json(d, "registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json", {"absents": True})
    fiche = lambda e: {"commit": "c" * 40, "fichiers": {"src/x.py": "a" * 64}, "entropie": str(e),
                       "epreuve_niveau": {"chemin": "e.json", "sha256": "b" * 64, "niveau_decisif_retenu": 0.99},
                       "niveau_decisif": 0.99}
    sha_f1 = aide.sceller_json(d, "registres/t07-etape-b-bis/code-bbis-v1.json", fiche(2 ** 100 + 99))
    sha_f2 = aide.sceller_json(d, "registres/t07-etape-b-bis/code-bbis-v2.json", fiche(entropie))
    g = d / "registres" / "go-extraits" / "GO-BBIS-v1.md"
    g.parent.mkdir(parents=True)
    g.write_text("| GO-2026-11-14-09 | extrait jouet |\n", encoding="utf-8")
    for cle, date, chemin, sha in [("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z", cm.TEXTE, cm.TEXTE_SHA256),
                                   ("ABSENCE-B-BBIS", "2026-11-14T12:30:30Z", "registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json",
                                    sha_abs),
                                   ("CODE-BBIS", "2026-11-16T12:57:51Z", "registres/t07-etape-b-bis/code-bbis-v1.json", sha_f1),
                                   ("GO-BBIS", "2026-11-16T12:58:51Z", "registres/go-extraits/GO-BBIS-v1.md", sceller(g)),
                                   ("CODE-BBIS", "2026-11-17T10:00:00Z", "registres/t07-etape-b-bis/code-bbis-v2.json", sha_f2),
                                   ("SCORES-BBIS", "2026-11-18T20:00:00Z", r["sondes_bbis"], r["sondes_bbis_sha256"])]:
        rb2.ajouter_ligne_propre(d, rb2.REGISTRE_PROPRE, cle, _t(date), chemin, sha)
    aide.git(d, "add", "-A")
    aide.git(d, "commit", "-q", "-m", "registres jouets de B bis (CODE-BBIS remplacée)")
    res = lv3.lire(d, aide.RUN, run_b, _t("2026-11-19T09:00:00Z"), essai={"n_directions": 12, "n_nul": 3, "n_tirages": 60})
    assert "garde" not in res, res.get("garde")
    assert res["lignes"]["propres"]["CODE-BBIS"]["chemin"].endswith("code-bbis-v2.json")
    assert res["controle_carte_processeur"]["version_controle"] == "v4" and res["controle_carte_processeur"]["discriminant"]
    dl = res["dispersion_ordres_calcul"]
    assert dl["decide"] is False and dl["cellules_lues"] >= 1 and dl["plis_compares"] >= 1
    for nom, cel in dl["cellules"].items():
        if "difference" in cel:
            assert abs(cel["aire_ordre2"] - cel["aire_ordre1"] - cel["difference"]) < 1e-12
    assert sum(x.startswith("R-PILE") for x in res["reserves"]) == 1
    pile = next(x for x in res["reserves"] if x.startswith("R-PILE"))
    assert "écart absolu maximal" in pile and "(7) une aire de sonde, linéaire ou « attention »" in res["section_D"]
    etats_sans = {n: cel.get("etat") for n, cel in res["cellules"].items()}
    assert etats_sans and all(e is not None for e in etats_sans.values())     # les états sont ceux des critères gelés
