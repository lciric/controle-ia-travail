"""Relance v4 de R1 sur la table version 4 (`runs_nuit.rejeu_activations_v4`), en mode jouet sur un dépôt jetable, sans
aucun téléchargement.

Table v4 jouet construite par la chaîne même de la v4 (`resolution_graine_lot_v2` : témoin sur le lot 1, réparation à
plusieurs cibles du lot 0, dont les quatre épisodes ne sont pas entièrement conformes en longueur, table v4 écrite et
scellée), sur le P3 jouet des tests existants. Cas sain : empreinte de table citée **ou** « construite-en-session » ;
8 trajectoires identiques sur 8, 4 corrections « identifiants » revérifiées au chargement, aucune action non conforme,
fidélité et contrôle négatif lus. Comparé à la v3 sur la même P3 jouet (table v3 vide) : la v4 garde tout ce que la v3
gardait et ajoute les actions réparées. Artefacts (R5) : table v3 donnée à la v4 (version citée), empreinte citée
fausse, entrée retirée (règle A : manquant), entrée en trop, identifiants falsifiés (revérification au chargement) ;
règle A v4 et règle B unitaires (signalés, non conformes, non retrouvés déclarés hors de la règle B) ; configuration."""
import copy
import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.runs_nuit import rejeu_activations_v3 as rc
from controle_ia.runs_nuit import rejeu_activations_v4 as rd
from controle_ia.runs_nuit import resolution_graine_lot_v2 as rv
from controle_ia.scellement import sceller, verifier

from test_premier_test_ia_run import entropie_fixe  # noqa: F401  (fixture réutilisée)
from test_resolution_graine_lot_v1 import _preparer
from test_resolution_graine_lot_v2 import _config_v4, _table_v3_jouet
from test_runs_nuit_v1 import RUN_P3, source  # noqa: F401  (fixture réutilisée)
from test_runs_nuit_v2 import _config_v2


def _ecrire(p: Path, t: dict) -> str:
    p.write_text(json.dumps(t, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return sceller(p)


def _arret(depot, run):
    return json.loads((depot / "diag" / run / "arret.json").read_text(encoding="utf-8"))["resultat"]


def test_regle_a_etendue_et_regle_b_unitaires():
    ent = lambda e, m="identifiants": {"episode": e, "methode": m}          # noqa: E731
    table = {"episodes": [ent("s1", "fins"), ent("s2", "non_resolu"), ent("n1"), ent("n2", "non_resolu")]}
    corr, nr, nret = rd.classer_episodes_v4(["s1", "s2"], ["n1", "n2"], table, 1)
    assert sorted(corr) == ["n1", "s1"] and nr == ["s2"] and nret == ["n2"]
    # les non retrouvés v4 ne comptent pas dans la règle B (seuil 1 : un signalé non résolu passe, pas deux)
    with pytest.raises(GardeArret, match="au-delà du seuil"):
        rd.classer_episodes_v4(["s1", "s2", "s3"], ["n1", "n2"], {"episodes": table["episodes"] + [ent("s3", "non_resolu")]},
                               1)
    rd.classer_episodes_v4(["s1", "s2"], ["n1", "n2"], table, 1)
    with pytest.raises(GardeArret, match="manquants \\['n2'\\]"):
        rd.classer_episodes_v4(["s1", "s2"], ["n1", "n2"], {"episodes": table["episodes"][:3]}, 1)
    with pytest.raises(GardeArret, match="en trop \\['x'\\]"):
        rd.classer_episodes_v4(["s1", "s2"], ["n1", "n2"], {"episodes": table["episodes"] + [ent("x")]}, 1)
    with pytest.raises(GardeArret, match="à la fois"):
        rd.classer_episodes_v4(["s1"], ["s1"], {"episodes": [ent("s1")]}, 1)
    # la v3 refusait une table qui couvre les non conformes (en trop)
    from controle_ia.runs_nuit.resolution_tokenisation_v1 import classer_episodes
    with pytest.raises(GardeArret, match="en trop"):
        classer_episodes(["s1", "s2"], table, 1)


def test_configuration_et_constantes():
    assert rd.VERSION_TABLE == 4 and rd.ADDENDUM == "prereg/R1-addendum-relance-v4.md"
    assert rd.COMMANDE.endswith("rejeu_activations_v4") and rd.CLES == rc.CLES and rd.CONFIG_CITEE == rc.CONFIG_CITEE
    assert rd.controle_negatif is rc.controle_negatif and rd.methode_resolution is rc.methode_resolution
    base = {k: None for k in rd.CLES}
    base.update(mode="jouet", couches=[0, 2], tolerance_fidelite=0.02, n_fidelite_par_condition=1,
                chemin_table_tokenisation="t.json", seuil_non_conformes=10)
    for sha in (None, "", "0" * 63, "g" * 64, "construite en session", 12):
        with pytest.raises(GardeArret, match="table_tokenisation_sha256"):
            rd.exiger_config({**base, "table_tokenisation_sha256": sha})
    rd.exiger_config({**base, "table_tokenisation_sha256": "0" * 64})
    rd.exiger_config({**base, "table_tokenisation_sha256": rd.TABLE_EN_SESSION})
    with pytest.raises(GardeArret, match="table_tokenisation_sha256"):
        rc.exiger_config({**base, "table_tokenisation_sha256": rd.TABLE_EN_SESSION})     # la v3 ne l'admet pas
    with pytest.raises(GardeArret, match="empreinte citée absente"):
        rd.charger_table("t.json", None)


@pytest.fixture
def chaine_v4(source, tmp_path):
    """Témoin, réparation et table v4 jouets (chaîne de la v4), puis la configuration du rejeu v4."""
    from conftest import committer

    depot, f, c, tp, pieces0, fmt_j, cl, connus, autres = _preparer(source, tmp_path)
    t3 = _table_v3_jouet(depot, tmp_path, tmp_path / "table0.json")
    committer(depot)
    conf = _config_v4(depot, f, c, tp, t3)
    rv.executer(conf, depot, "20261104-130000-v4-temoin-jouet", None, rv.ETAPE_TEMOIN, autoriser_depot_sale=True,
                entropie_essai=3)
    committer(depot)
    ch_t = depot / "diag" / "20261104-130000-v4-temoin-jouet" / "resolution-graine-lot-v2-temoin.json"
    rv.executer(conf, depot, "20261104-130100-v4-reparation-jouet", None, rv.ETAPE_REPARATION, str(ch_t),
                autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    ch_r = depot / "diag" / "20261104-130100-v4-reparation-jouet" / "resolution-graine-lot-v2-reparation.json"
    p4 = tmp_path / "table-v4.json"
    rv.ecrire_table_v4(rv.construire_table_v4(conf, depot, None, str(ch_r), fmt=fmt_j), p4)
    committer(depot)
    return depot, f, c, t3, p4, autres


def test_relance_v4_saine_en_session_et_citee_puis_artefacts(chaine_v4, tmp_path):
    from conftest import committer

    depot, f, c, t3, p4, autres = chaine_v4
    t4 = json.loads(p4.read_text(encoding="utf-8"))
    # ---- cas sain, table « construite-en-session »
    conf = _config_v2(depot, f, c, p4, table_tokenisation_sha256=rd.TABLE_EN_SESSION)
    r = rd.executer(conf, depot, "20261104-140000-r1-rejeu-v4-jouet", None, autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    tk = r["tokenisation"]
    assert r["verdict_fidelite"] == "conforme" and tk["version_table"] == 4 and tk["table_sha256"] == verifier(p4)
    assert tk["table_empreinte_citee"] is False and tk["non_conformes"] == 4 and tk["episodes_non_retrouves_v4"] == []
    assert tk["corrections_verifiees_au_chargement"] == t4["corrections_verifiees"] >= 4
    assert tk["par_methode_resolution"]["identifiants"] >= 4 and tk["addendum"] == rd.ADDENDUM
    assert r["empreintes_p3"]["trajectoires_identiques"] == 8 == r["empreintes_p3"]["activations_identiques_au_bit"]
    ft = r["fidelite_toutes"]
    assert ft["conformes_longueur"] == ft["actions"] == ft["contextes_conformes"] == 16
    nom = conf["nom_sortie"]
    with np.load(depot / "donnees" / "20261104-140000-r1-rejeu-v4-jouet" / f"{nom}-maximum.npz") as z:
        assert z["trajectoire_identique"].all() and z["conforme_longueur"].all() and z["maximum"].shape[0] == 16
        fideles_v4 = z["fidele"].copy()
    # ---- même P3 sous la v3 (table v3 jouet, sans les réparations) : la v4 garde tout ce que la v3 gardait
    conf3 = _config_v2(depot, f, c, t3, table_tokenisation_sha256=verifier(t3))
    r3 = rc.executer(conf3, depot, "20261104-140100-r1-rejeu-v3-jouet", None, autoriser_depot_sale=True,
                     entropie_essai=3)
    committer(depot)
    with np.load(depot / "donnees" / "20261104-140100-r1-rejeu-v3-jouet" / f"{nom}-maximum.npz") as z:
        fideles_v3 = z["fidele"].copy()
    assert r3["empreintes_p3"]["trajectoires_identiques"] == 4
    assert (fideles_v4 | ~fideles_v3).all() and fideles_v4.sum() > fideles_v3.sum()
    # ---- empreinte citée : saine ; fausse → refus avant le manifeste
    conf_c = _config_v2(depot, f, c, p4, table_tokenisation_sha256=verifier(p4), n_fidelite_par_condition=2)
    rc_ = rd.executer(conf_c, depot, "20261104-140200-r1-rejeu-v4-jouet", None, autoriser_depot_sale=True,
                      entropie_essai=3)
    committer(depot)
    assert rc_["tokenisation"]["table_empreinte_citee"] is True
    with pytest.raises(GardeArret, match="empreinte citée"):
        rd.executer({**conf_c, "table_tokenisation_sha256": "0" * 64}, depot, "20261104-140300-r1-rejeu-v4-jouet",
                    None, autoriser_depot_sale=True, entropie_essai=3)
    assert not (depot / "runs" / "20261104-140300-r1-rejeu-v4-jouet").exists()
    # ---- table v3 donnée à la v4 : refusée, version citée
    with pytest.raises(GardeArret, match="version 3"):
        rd.executer(_config_v2(depot, f, c, t3, table_tokenisation_sha256=rd.TABLE_EN_SESSION), depot,
                    "20261104-140400-r1-rejeu-v4-jouet", None, autoriser_depot_sale=True, entropie_essai=3)
    # ---- entrée retirée (manquant) ; entrée « identifiants » falsifiée (revérification au chargement)
    for k, (nom_t, mut, motif) in enumerate((
            ("manquant", lambda t: t["episodes"].pop(), "manquants"),
            ("falsifiee", lambda t: next(x for x in t["episodes"] if x["methode"] == "identifiants")["actions"][0]
             .__setitem__("p3", list(reversed(next(x for x in t["episodes"] if x["methode"] == "identifiants")
                                              ["actions"][0]["p3"])) + [4]), "action corrigée non conforme|empreinte"))):
        t = copy.deepcopy(t4)
        mut(t)
        if nom_t == "manquant":
            t["comptes"]["identifiants"] -= 1
            t["comptes"]["identiques_apres_table"] -= 1
        p = tmp_path / f"table-v4-{nom_t}.json"
        _ecrire(p, t)
        committer(depot)
        run = f"20261104-14050{k}-r1-rejeu-v4-jouet"
        with pytest.raises(GardeArret, match=motif):
            rd.executer(_config_v2(depot, f, c, p, table_tokenisation_sha256=rd.TABLE_EN_SESSION), depot, run, None,
                        autoriser_depot_sale=True, entropie_essai=3)
        a = _arret(depot, run)
        assert a["verdict_fidelite"] == "echec"
        assert not (depot / "donnees" / run).exists()
