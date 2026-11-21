"""Essais de la lecture gelée de l'idée 1.2 sur des sorties fabriquées (aucune donnée du banc) : chaque étage, chaque
condition de l'étage 1 sur un cas sain et sur un artefact, ordre de la principale, qualifications, scellement."""
import copy
import json
import math

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v1 as LB
from controle_ia.organisme_idees_juge import rejeu_v1 as R

RAC = 123456789
RE = 300


def _bras_vide(nom):
    return {"blocs": [10 if nom == "F125" else 8] * 24, "tirages": 6000 if nom == "F125" else 4800,
            "log_e": [-1.0] * 24, "promues": [], "arrets": ["fin"] * 24}


def fabriquer(p=None, nT=750, nN=500, graine=0, meme_tirage=False):
    """p : {bras: probabilité qu'une porteuse (carte 0) soit promue dans une génération T}."""
    p = p or {"F": 0.4, "F-arret": 0.4, "A": 0.6, "P": 0.4, "P-prime": 0.4, "F125": 0.4}
    rng = np.random.default_rng(graine)
    jeu, oracle = [], []
    for fam, n in (("N", nN), ("T", nT)):
        for x in range(n):
            g = x if fam == "T" else (x if x < nN // 2 else B.BORNE_M0 + x - nN // 2)
            cel = g % 10
            sortes = B.SORTES[fam]
            cartes = [{"indice": i, "sorte": sortes[i], "empreinte_loi": f"{fam}{g}-{i}", "trajectoire": [-1.0] * 32}
                      for i in range(24)]
            if fam == "N":
                for c in cartes:
                    c["log_lambda"] = [0.0] * 32
            bras = {nom: _bras_vide(nom) for nom in (R.BRAS_N if fam == "N" else R.BRAS_T)}
            if fam == "T":
                u = rng.random()
                for nom, pr in p.items():
                    if (u if meme_tirage else rng.random()) < pr:
                        bras[nom]["promues"] = [0]
            jeu.append({"famille": fam, "g": g, "cellule": cel, "type": "V1", "dose": 0.25, "dose_haute": bool(cel % 2),
                        "monde": None, "positions": list(range(24)), "oracle_scelle_sha256": "o" * 64, "cartes": cartes,
                        "bras": bras})
            classes = ["porteuse"] * 6 + ["fausse"] * 18 if fam == "T" else ["porteuse sans gain" if s == "porteuses construites" else "fausse" for s in sortes]
            oracle.append({"famille": fam, "g": g, "cartes": [{"indice": i, "sorte": sortes[i], "empreinte_loi": f"{fam}{g}-{i}",
                                                               "classe": classes[i], "gain": 0.0} for i in range(24)]})
    return {"run_id": "r", "manifeste_sha256": "m" * 64, "sha256": {"oracle": "o" * 64, "jeu": "j" * 64},
            "oracle": {"generations": oracle}, "jeu": {"generations": jeu}}


def lire(s, **k):
    return LB.lire(s, RAC, RE, n_attendus={"N": 500, "T": 750}, **k)


def _gens(s, fam):
    return [g for g in s["jeu"]["generations"] if g["famille"] == fam]


def test_seuils_de_l_annexe_B_et_statistiques():
    assert LB.seuils_validite(500) == (13, 39)
    assert LB.seuils_validite(500, bras=5) == (13, 38)
    assert LB.seuils_validite(250) == (4, 23)
    assert LB.statut_validite(13, 13, 39) == "tenue" and LB.statut_validite(39, 13, 39) == "non tenue"
    assert LB.statut_validite(14, 13, 39) == "non jugeable"
    assert LB.clopper_pearson(0, 10)[0] == 0.0 and LB.clopper_pearson(10, 10)[1] == 1.0
    b, h = LB.clopper_pearson(5, 10)
    assert b == pytest.approx(0.187, abs=1e-3) and h == pytest.approx(0.813, abs=1e-3)
    m = LB.mcnemar_exact([1, 1, 0, 0], [1, 0, 0, 0])
    assert m["a_seul"] == 1 and m["b_seul"] == 0 and m["p_bilaterale"] == 1.0
    rs = LB.Reechantillonneur(RAC, 50)
    assert (rs.indices(30) == LB.Reechantillonneur(RAC, 50).indices(30)).all()
    assert (rs.indices(30)[7] == B.generateur(RAC, 99, 7).integers(0, 30, size=30)).all()


def test_cas_sain_gain_de_structure():
    r = lire(fabriquer())
    V = r["etage_1"]["validite"]
    assert V["defauts_etage_1"] == [] and V["intervalles_comptes"] == 49
    assert V["seuils"] == {"tenue_si_au_plus": 13, "non_tenue_si_au_moins": 39}
    assert all(b["statut"] == "tenue" for b in V["bras"].values())
    assert r["etage_2"]["verdict"] == "dans la zone utile"
    assert r["etage_3"]["verdict"] == "gain" and r["etage_4"]["verdict"] == "de structure"
    assert r["verdict"] == "gain"
    assert set(r["predictions"]) >= {f"Q{k}" for k in range(1, 10)}


@pytest.mark.parametrize("artefact", ["membre exact N", "membre exact T", "domination", "non tenue", "borne basse"])
def test_etage_1_garantie_mise_en_defaut(artefact):
    s = fabriquer()
    N = _gens(s, "N")
    if artefact == "membre exact N":
        N[3]["bras"]["A"]["promues"] = [9]
    elif artefact == "membre exact T":
        _gens(s, "T")[5]["bras"]["F"]["promues"] = [7]
    elif artefact == "domination":
        N[300]["cartes"][4]["trajectoire"][20] = 0.5
    elif artefact == "non tenue":
        for g in N[:39]:
            g["bras"]["G"]["promues"] = [22]
    elif artefact == "borne basse":
        for g in N:
            for i in (22, 23):
                g["bras"]["P"]["log_e"][i] = math.log(5.0)
    r = lire(s)
    assert r["verdict"] == "garantie mise en défaut"
    assert "famille_T" not in r and "etage_3" not in r       # rien d'autre n'est lu


def test_etage_1_bis_non_jugeable_et_audit_par_monde():
    s = fabriquer()
    N = _gens(s, "N")
    for g in N[:14]:
        g["bras"]["F"]["promues"] = [23]
    for g in N[:250]:                                          # monde M₀ seul : moyenne haute, réunie sous 1
        for i in (22, 23):
            g["bras"]["A"]["log_e"][i] = math.log(1.5)
    for g in N[250:]:
        for i in (22, 23):
            g["bras"]["A"]["log_e"][i] = math.log(0.2)
    r = lire(s)
    assert r["etage_1_bis"]["non_jugeables"] == ["F"]
    assert "réserve" in r["verdict"]
    assert any(x[0] == "M0" and x[1] == "A" and x[2] == "nulles" for x in r["etage_1"]["validite"]["audit_ecrit_requis_par_monde"])


def test_principale_dans_l_ordre():
    assert lire(fabriquer({"F": 0.5, "F-arret": 0.5, "A": 0.5, "P": 0.5, "P-prime": 0.5, "F125": 0.5}, meme_tirage=True))["verdict"] == "pas de gain"
    r = lire(fabriquer({"F": 0.5, "F-arret": 0.5, "A": 0.53, "P": 0.5, "P-prime": 0.5, "F125": 0.5}, meme_tirage=True))
    d = r["etage_3"]["C_A-C_F"]                 # A ⊇ F, environ 3 % de générations de plus : borne basse > 0, estimation < 0,05
    assert d["bas"] > 0 and d["estimation"] < 0.05 and d["haut"] >= 0.02 and r["verdict"] == "non tranché"
    s = fabriquer()
    for g in _gens(s, "T")[:300]:
        g["bras"]["A"]["promues"] = sorted(set(g["bras"]["A"]["promues"]) | {16})   # fausses promues sous A
    assert lire(s)["verdict"] == "nuisible"
    assert lire(fabriquer({"F": 0.6, "F-arret": 0.6, "A": 0.4, "P": 0.4, "P-prime": 0.4, "F125": 0.4}))["verdict"] == "nuisible"


def test_qualifications():
    base = {"F": 0.3, "F-arret": 0.3, "A": 0.6, "P": 0.3, "P-prime": 0.3, "F125": 0.3}
    assert lire(fabriquer(dict(base, F125=0.85)))["etage_4"]["verdict"] == "d'effectif seulement"
    assert lire(fabriquer(dict(base, P=0.85)))["etage_4"]["verdict"] == "sans effet de ciblage"
    assert lire(fabriquer(dict(base, P=0.85, F125=0.85)))["etage_4"]["verdict"] == "d'effectif seulement et sans effet de ciblage"


def test_hors_de_la_zone_utile():
    r = lire(fabriquer({"F": 0.02, "F-arret": 0.02, "A": 0.3, "P": 0.02, "P-prime": 0.02, "F125": 0.02}))
    assert r["verdict"] == "hors de la zone utile" and r["etage_3"]["verdict"].startswith("non lu")


def _ecrire(dossier, s, oracle_sha=None):
    dossier.mkdir(parents=True)
    for nom in ("oracle", "jeu"):
        corps = {"run_id": s["run_id"], "manifeste_sha256": s["manifeste_sha256"], "resultat": s[nom]}
        (dossier / f"{nom}.json").write_text(json.dumps(corps), encoding="utf-8")


def test_lecture_refusee_avant_scellement_puis_acceptee(tmp_path):
    s = fabriquer(nT=20, nN=10)
    d = tmp_path / "run"
    _ecrire(d, s)
    with pytest.raises(GardeArret, match="avant scellement"):
        LB.charger_sortie(d)
    sha_o = sceller(d / "oracle.json")
    with pytest.raises(GardeArret, match="avant scellement"):
        LB.charger_sortie(d)
    sceller(d / "jeu.json")
    with pytest.raises(GardeArret, match="autre oracle"):        # jeu rattaché à un autre oracle que celui scellé
        LB.ecrire_lecture(d, RAC, reechantillons=50)
    s2 = copy.deepcopy(s)
    for g in s2["jeu"]["generations"]:
        g["oracle_scelle_sha256"] = sha_o
    d2 = tmp_path / "run2"
    _ecrire(d2, s2)
    sceller(d2 / "oracle.json"); sceller(d2 / "jeu.json")
    chemin = LB.ecrire_lecture(d2, RAC, reechantillons=50)          # sain
    assert chemin.with_name(chemin.name + ".sha256").is_file()
    with pytest.raises(GardeArret, match="R12"):
        LB.ecrire_lecture(d2, RAC, reechantillons=50)


def test_apparier_refuse_des_cartes_differentes():
    s = fabriquer(nT=20, nN=10)
    s["oracle"]["generations"][0]["cartes"][3]["empreinte_loi"] = "autre"
    with pytest.raises(GardeArret, match="cartes de l'oracle"):
        LB.lire(s, RAC, 50)


def test_run_incomplet_refuse():
    s = fabriquer(nT=20, nN=10)
    with pytest.raises(GardeArret, match="run incomplet"):
        LB.lire(s, RAC, 50, n_attendus={"N": 500, "T": 750})
