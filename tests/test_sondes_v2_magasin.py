"""Essais de la brique A (magasin d'activations gardées v1) : cas sains et artefacts, sur données fabriquées."""
import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes_v2 import magasin_v1 as mg

D = 8
POIDS_NU = {"type": "nu"}
POIDS_AD = {"type": "adaptateur", "empreinte_adaptateur": "ab" * 32, "dose": 0.5}


def _actions(n=6, champ_tous=False):
    out = []
    for i in range(n):
        champ = champ_tous or i % 2 == 0
        out.append(mg.Action(f"t{i % 3}-e{i}-p{i}", f"t{i % 3}", f"e{i}", i, 1000 + i, 3 if champ else None,
                             float(10 + i) if champ else None, 2 + i))
    return out


def _ecrire(dossier, ident="serie-a", poids=POIDS_NU, regle=None, actions=None, rng=None, decalage=0.0):
    rng = rng or np.random.default_rng(0)
    actions = actions or _actions()
    e = mg.EcrivainSerie(dossier, ident, poids, "textes-fabriques", regle or {"type": "toutes"}, D)
    donnees = {}
    for a in actions:
        j = rng.standard_normal((a.n_jetons, D)) + decalage
        av = {c: rng.standard_normal(D) for c in mg.COUCHES_AVANT_CHAMP} if a.a_un_champ else None
        e.ajouter(a, j, av)
        donnees[a.cle] = (j, av)
    e.clore()
    return donnees


def test_aller_retour_sain(tmp_path):
    donnees = _ecrire(tmp_path / "s")
    s = mg.Serie(tmp_path / "s", verifier_tout=True)
    assert s.cles == [a.cle for a in _actions()]
    for cle, (j, av) in donnees.items():
        lu = s.jetons(cle)
        assert lu.dtype == np.float32
        np.testing.assert_array_equal(lu, j.astype(np.float16).astype(np.float32))
        if av is not None:
            for c in mg.COUCHES_AVANT_CHAMP:
                np.testing.assert_array_equal(s.avant_champ(cle, c), av[c].astype(np.float16).astype(np.float32))
        else:
            with pytest.raises(GardeArret, match="pas de champ"):
                s.avant_champ(cle, 15)
    m = s.manifeste
    assert m["n_actions"] == 6 and m["n_actions_avec_champ"] == 3 and m["poids"] == POIDS_NU
    assert (tmp_path / "s" / "manifeste.json.sha256").is_file()
    # convention de clés de ActivationsDemi : c15/<clé>.npy
    assert (tmp_path / "s" / "c15" / f"{_actions()[0].cle}.npy").is_file()


def test_ecriture_deterministe_au_bit(tmp_path):
    _ecrire(tmp_path / "a")
    _ecrire(tmp_path / "b")
    fa, fb = (json.loads((tmp_path / x / "manifeste.json").read_text())["fichiers"] for x in "ab")
    assert fa == fb


def test_regle_part(tmp_path):
    acts = _actions()
    cles = [a.cle for a in acts[:3]]
    _ecrire(tmp_path / "s", regle={"type": "part", "part": "une_sur_dix", "cles": cles}, actions=acts[:3])
    assert mg.Serie(tmp_path / "s").regle["cles"] == sorted(cles)
    with pytest.raises(GardeArret, match="clés déclarées"):
        _ecrire(tmp_path / "t", regle={"type": "part", "part": "une_sur_dix", "cles": cles}, actions=acts[:2])


def test_dossier_existant_refuse(tmp_path):
    (tmp_path / "s").mkdir()
    with pytest.raises(GardeArret, match="R12"):
        mg.EcrivainSerie(tmp_path / "s", "x", POIDS_NU, "t", {"type": "toutes"}, D)


def test_cle_en_double_a_l_ecriture(tmp_path):
    a = _actions()[1]
    e = mg.EcrivainSerie(tmp_path / "s", "x", POIDS_NU, "t", {"type": "toutes"}, D)
    e.ajouter(a, np.zeros((a.n_jetons, D)))
    with pytest.raises(GardeArret, match="double"):
        e.ajouter(a, np.zeros((a.n_jetons, D)))


@pytest.mark.parametrize("forme", [(3, D), (4, D + 1), (4,)])
def test_forme_inattendue_a_l_ecriture(tmp_path, forme):
    a = mg.Action("k", "t", "e", 0, 0, None, None, 4)
    e = mg.EcrivainSerie(tmp_path / "s", "x", POIDS_NU, "t", {"type": "toutes"}, D)
    e.ajouter(a, np.zeros((4, D)))  # cas sain
    b = mg.Action("k2", "t", "e", 0, 0, None, None, 4)
    with pytest.raises(GardeArret, match="forme"):
        e.ajouter(b, np.zeros(forme))


def test_hors_demi_precision(tmp_path):
    a = mg.Action("k", "t", "e", 0, 0, None, None, 2)
    e = mg.EcrivainSerie(tmp_path / "s", "x", POIDS_NU, "t", {"type": "toutes"}, D)
    with pytest.raises(GardeArret, match="demi-précision"):
        e.ajouter(a, np.full((2, D), 1e6))
    with pytest.raises(GardeArret, match="demi-précision"):
        e.ajouter(a, np.full((2, D), np.nan))


def test_champ_et_avant_champ_vont_ensemble(tmp_path):
    e = mg.EcrivainSerie(tmp_path / "s", "x", POIDS_NU, "t", {"type": "toutes"}, D)
    a = mg.Action("k", "t", "e", 0, 0, 2, 5.0, 3)
    with pytest.raises(GardeArret, match="avant le champ"):
        e.ajouter(a, np.zeros((3, D)))
    with pytest.raises(GardeArret, match="avant le champ"):
        e.ajouter(a, np.zeros((3, D)), {7: np.zeros(D), 15: np.zeros(D)})
    b = mg.Action("k2", "t", "e", 0, 0, None, None, 3)
    with pytest.raises(GardeArret, match="sans champ"):
        e.ajouter(b, np.zeros((3, D)), {c: np.zeros(D) for c in mg.COUCHES_AVANT_CHAMP})
    with pytest.raises(GardeArret, match="vont ensemble"):
        mg.Action("k3", "t", "e", 0, 0, 2, None, 3).verifier()
    with pytest.raises(GardeArret, match="≥ 1"):
        mg.Action("k3", "t", "e", 0, 0, 0, 1.0, 3).verifier()


@pytest.mark.parametrize("cle", ["", "../x", "a b", "a/b"])
def test_cle_invalide(cle):
    with pytest.raises(GardeArret, match="clé"):
        mg.Action(cle, "t", "e", 0, 0, None, None, 1).verifier()


@pytest.mark.parametrize("poids", [{"type": "autre"}, {"type": "nu", "dose": 1},
                                   {"type": "adaptateur", "empreinte_adaptateur": "zz", "dose": 1},
                                   {"type": "adaptateur", "empreinte_adaptateur": "ab" * 32}])
def test_poids_refuses(tmp_path, poids):
    with pytest.raises(GardeArret):
        mg.EcrivainSerie(tmp_path / "s", "x", poids, "t", {"type": "toutes"}, D)


def test_empreinte_fausse_a_la_lecture(tmp_path):
    _ecrire(tmp_path / "s")
    s = mg.Serie(tmp_path / "s")
    cle = s.cles[0]
    s.jetons(cle)  # sain
    chemin = tmp_path / "s" / "c15" / f"{cle}.npy"
    octets = bytearray(chemin.read_bytes())
    octets[-1] ^= 0xFF
    chemin.write_bytes(bytes(octets))
    with pytest.raises(GardeArret, match="empreinte fausse"):
        s.jetons(cle)
    with pytest.raises(GardeArret, match="empreinte fausse"):
        mg.Serie(tmp_path / "s", verifier_tout=True)


def test_manifeste_altere(tmp_path):
    _ecrire(tmp_path / "s")
    m = tmp_path / "s" / "manifeste.json"
    m.write_text(m.read_text().replace('"n_actions": 6', '"n_actions": 7'))
    with pytest.raises(GardeArret, match="empreinte"):
        mg.Serie(tmp_path / "s")


def test_actions_alterees(tmp_path):
    _ecrire(tmp_path / "s")
    ja = tmp_path / "s" / "actions.jsonl"
    lignes = ja.read_text().splitlines()
    ja.write_text("\n".join(lignes + [lignes[0]]) + "\n")
    with pytest.raises(GardeArret, match="empreinte différente"):
        mg.Serie(tmp_path / "s")


def test_fichier_non_declare_ou_absent(tmp_path):
    _ecrire(tmp_path / "s")
    intrus = tmp_path / "s" / "c15" / "intrus.npy"
    np.save(intrus, np.zeros((1, D), dtype=np.float16))
    with pytest.raises(GardeArret, match="non déclaré"):
        mg.Serie(tmp_path / "s")
    intrus.unlink()
    mg.Serie(tmp_path / "s")  # sain de nouveau
    cle = mg.Serie(tmp_path / "s").cles[0]
    (tmp_path / "s" / "c15" / f"{cle}.npy").unlink()
    with pytest.raises(GardeArret, match="absent du disque"):
        mg.Serie(tmp_path / "s")


def test_cle_manquante(tmp_path):
    _ecrire(tmp_path / "s")
    with pytest.raises(GardeArret, match="clé manquante"):
        mg.Serie(tmp_path / "s").jetons("inconnue")


def test_intersection(tmp_path):
    acts = _actions()
    _ecrire(tmp_path / "a", "serie-a", actions=acts[:5])
    _ecrire(tmp_path / "b", "serie-b", poids=POIDS_AD, actions=acts[2:])
    a, b = mg.Serie(tmp_path / "a"), mg.Serie(tmp_path / "b")
    cles, eff = mg.intersection_cles(a, b)
    assert cles == sorted(x.cle for x in acts[2:5])
    assert eff == {"communes": 3, "par_serie": {"serie-a": {"total": 5, "hors_intersection": 2},
                                                "serie-b": {"total": 4, "hors_intersection": 1}}}


def test_intersection_desalignee(tmp_path):
    acts = _actions()
    autre = [mg.Action(acts[0].cle, "autre-tache", acts[0].episode, acts[0].pas, 0, acts[0].position_champ,
                       acts[0].valeur_declaree, acts[0].n_jetons)]
    _ecrire(tmp_path / "a", "serie-a", actions=acts[:1])
    _ecrire(tmp_path / "b", "serie-b", actions=autre)
    with pytest.raises(GardeArret, match="tache diffère"):
        mg.intersection_cles(mg.Serie(tmp_path / "a"), mg.Serie(tmp_path / "b"))
    with pytest.raises(GardeArret, match="même identifiant"):
        mg.intersection_cles(mg.Serie(tmp_path / "a"), mg.Serie(tmp_path / "a"))


def _dossier_demi(racine: Path, couches, actions, rng):
    """Écrit un dossier au format d'ActivationsDemi (c<couche>/<clé>.npy, float16), sans importer le lanceur."""
    for c in couches:
        (racine / f"c{c}").mkdir(parents=True)
    tableaux = {}
    for cle, n in actions:
        for c in couches:
            a = rng.standard_normal((n, D)).astype(np.float32).astype(np.float16)
            np.save(racine / f"c{c}" / f"{cle}.npy", a)
            tableaux[(c, cle)] = a
    return tableaux


def _lignes_demi(actions, avec_champ):
    return [{"cle": cle, "tache": "t", "episode": f"e{i}", "pas": i, "graine": i, "position_champ": 2 if avec_champ
             else None, "valeur_declaree": 3.0 if avec_champ else None, "indice_avant_champ": 1 if avec_champ else None}
            for i, (cle, n) in enumerate(actions)]


def test_adaptateur_activations_demi_sain(tmp_path):
    rng = np.random.default_rng(1)
    actions = [("k0", 3), ("k1", 5)]
    t = _dossier_demi(tmp_path / "demi", (7, 15, 23), actions, rng)
    mg.serie_depuis_activations_demi(tmp_path / "demi", _lignes_demi(actions, True), tmp_path / "s", "serie-demi",
                                     POIDS_AD, "textes", {"type": "toutes"})
    s = mg.Serie(tmp_path / "s", verifier_tout=True)
    for cle, n in actions:
        np.testing.assert_array_equal(s.jetons(cle), t[(15, cle)].astype(np.float32))  # sans perte
        for c in (7, 15, 23):
            np.testing.assert_array_equal(s.avant_champ(cle, c), t[(c, cle)][1].astype(np.float32))
    prov = s.manifeste["provenance"]
    assert prov["adaptateur"] == "ActivationsDemi" and len(prov["empreintes_sources"]) == 6


def test_adaptateur_activations_demi_compatible_lanceur(tmp_path):
    """Le format lu est celui qu'écrit `ActivationsDemi` (vérifié contre la classe elle-même si torch est là)."""
    lv2 = pytest.importorskip("controle_ia.t06.lanceur_v2")
    rng = np.random.default_rng(2)
    w = lv2.ActivationsDemi(tmp_path / "demi", [15])
    seg = rng.standard_normal((4, D)).astype(np.float32)
    w.ecrire("k0", {15: seg})
    mg.serie_depuis_activations_demi(tmp_path / "demi", _lignes_demi([("k0", 4)], False), tmp_path / "s", "x",
                                     POIDS_NU, "t", {"type": "toutes"})
    np.testing.assert_array_equal(mg.Serie(tmp_path / "s").jetons("k0"), w.lire("k0", 15))


def test_adaptateur_artefacts(tmp_path):
    rng = np.random.default_rng(3)
    actions = [("k0", 3)]
    _dossier_demi(tmp_path / "demi", (15,), actions, rng)
    # champ révélateur sans les couches 7 et 23
    with pytest.raises(GardeArret, match="absent"):
        mg.serie_depuis_activations_demi(tmp_path / "demi", _lignes_demi(actions, True), tmp_path / "s1", "x",
                                         POIDS_NU, "t", {"type": "toutes"})
    # indice hors du segment
    l = _lignes_demi(actions, False)
    l[0].update(position_champ=2, valeur_declaree=1.0, indice_avant_champ=9)
    _dossier_demi(tmp_path / "demi2", (7, 15, 23), actions, rng)
    with pytest.raises(GardeArret, match="hors du segment"):
        mg.serie_depuis_activations_demi(tmp_path / "demi2", l, tmp_path / "s2", "x", POIDS_NU, "t",
                                         {"type": "toutes"})
    # clé absente du dossier source
    with pytest.raises(GardeArret, match="absent"):
        mg.serie_depuis_activations_demi(tmp_path / "demi", _lignes_demi([("k9", 3)], False), tmp_path / "s3", "x",
                                         POIDS_NU, "t", {"type": "toutes"})
    # mauvaise précision à la source
    np.save(tmp_path / "demi" / "c15" / "k0.npy", np.zeros((3, D), dtype=np.float32))
    with pytest.raises(GardeArret, match="float16"):
        mg.serie_depuis_activations_demi(tmp_path / "demi", _lignes_demi(actions, False), tmp_path / "s4", "x",
                                         POIDS_NU, "t", {"type": "toutes"})
