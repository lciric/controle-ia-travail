"""Essais du schéma de permutation des étiquettes des épisodes, version 4 du code (brouillon 17, 6.9 et 8.4 ; demande
du coordinateur, non tranchée par Lazar) : réglage obligatoire, un cas sain et un artefact par schéma (R5), paire
incomplète, rang en double, nombre de permutations distinctes (rapporté, sans énumération complète), paires gardées
par un rééchantillonnage de tâches entières. Données synthétiques ;
graines par `SeedSequence` (R9)."""
import inspect

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import permutation_etiquettes_bras_a_v4 as pe

ENTROPIE = 20261119
LIBRE, ECHANGE = pe.SCHEMA_LIBRE, pe.SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE


def rng(n=0):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(n,)))


def episodes(taches=16, rangs=8):
    return [(f"tache-{t:02d}", r, c) for t in range(taches) for r in range(rangs) for c in (0, 1)]


def test_schema_obligatoire_sans_defaut():
    """Le réglage est obligatoire : aucun paramètre `schema` n'a de valeur par défaut ; absent, vide ou approchant, il
    est refusé."""
    for f in (pe.permutations_des_etiquettes, pe.exiger_episodes, pe.nombre_de_permutations_distinctes,
              pe.exiger_permutation_conforme):
        assert inspect.signature(f).parameters["schema"].default is inspect.Parameter.empty
    assert pe.exiger_schema(LIBRE) == "libre" and pe.exiger_schema(ECHANGE) == "echange dans chaque paire"
    for fautif in (None, "", "Libre", "echange", "échange dans chaque paire", True, 0, ("libre",)):
        with pytest.raises(GardeArret, match="aucun schéma par défaut"):
            pe.exiger_schema(fautif)
        with pytest.raises(GardeArret):
            pe.permutations_des_etiquettes(fautif, episodes(), 10, rng())
    with pytest.raises(TypeError):
        pe.permutations_des_etiquettes(episodes=episodes(), n=10, rng=rng())           # schéma omis


def test_schema_libre_cas_sain_et_artefact():
    """Schéma libre. Cas sain : dans chaque tâche, les seize étiquettes sont rebattues, huit et huit gardés, les paires
    ignorées (des rangs portent deux fois la même étiquette). Artefacts : étiquettes passées d'une tâche à l'autre ;
    rang en double."""
    eps = episodes()
    r = pe.permutations_des_etiquettes(LIBRE, eps, 200, rng(1))
    e = r["etiquettes"]
    assert e.shape == (200, 256) and not r["moins_de_distinctes_que_de_tirages"] and r["schema"] == LIBRE
    assert r["distinctes_possibles"] == 12870 ** 16
    for ligne in e[:50]:
        pe.exiger_permutation_conforme(LIBRE, eps, ligne)                                # cas sain
    assert np.all(e.reshape(200, 16, 16).sum(axis=2) == 8)                               # effectifs gardés par tâche
    paires = e.reshape(200, 128, 2)
    assert np.any(paires[:, :, 0] == paires[:, :, 1])                                    # les paires sont ignorées
    assert len({ligne.tobytes() for ligne in e}) == 200 and np.array_equal(e, pe.permutations_des_etiquettes(LIBRE, eps, 200, rng(1))["etiquettes"])
    entre_taches = np.array([c for _, _, c in eps])
    entre_taches[0], entre_taches[17] = 1, 0                                              # un honnête de la tâche 0 contre un dosé de la tâche 1
    with pytest.raises(GardeArret, match="entre tâches"):
        pe.exiger_permutation_conforme(LIBRE, eps, entre_taches)
    with pytest.raises(GardeArret, match="rang en double"):
        pe.permutations_des_etiquettes(LIBRE, eps + [("tache-00", 3, 1)], 10, rng())
    # une paire incomplète ne gêne pas le schéma libre, qui ignore les paires
    assert pe.permutations_des_etiquettes(LIBRE, eps[:-1], 10, rng())["etiquettes"].shape == (10, 255)


def test_schema_echange_dans_chaque_paire_cas_sain_et_artefact():
    """Échange dans chaque paire. Cas sain : chaque paire honnête/dosé de même rang garde ses deux étiquettes, échangées
    ou non, à pile ou face. Artefacts : paire incomplète ; rang en double ; permutation libre donnée pour un échange."""
    eps = episodes()
    r = pe.permutations_des_etiquettes(ECHANGE, eps, 400, rng(2))
    e = r["etiquettes"]
    assert e.shape == (400, 256) and not r["moins_de_distinctes_que_de_tirages"] and r["distinctes_possibles"] == 2 ** 128
    assert pe.nombre_de_permutations_distinctes(episodes(taches=1), ECHANGE) == 256        # 2⁸ par tâche
    paires = e.reshape(400, 128, 2)
    assert np.all(paires.sum(axis=2) == 1)                                               # une étiquette de chaque dans la paire
    echanges = paires[:, :, 0] == 1
    assert 0.45 < echanges.mean() < 0.55 and 0.3 < echanges.mean(axis=0).min() and echanges.mean(axis=0).max() < 0.7
    for ligne in e[:50]:
        pe.exiger_permutation_conforme(ECHANGE, eps, ligne)                              # cas sain
        pe.exiger_permutation_conforme(LIBRE, eps, ligne)                                # un échange est aussi une permutation libre
    assert np.array_equal(e, pe.permutations_des_etiquettes(ECHANGE, eps, 400, rng(2))["etiquettes"])
    for incomplet in (eps[:-1], eps[1:], eps + [("tache-00", 8, 0)]):
        with pytest.raises(GardeArret, match="paire incomplète"):
            pe.permutations_des_etiquettes(ECHANGE, incomplet, 10, rng())
    for double in (eps + [("tache-00", 3, 1)], eps + [eps[0]]):
        with pytest.raises(GardeArret, match="rang en double"):
            pe.permutations_des_etiquettes(ECHANGE, double, 10, rng())
    libre = pe.permutations_des_etiquettes(LIBRE, eps, 5, rng(3))["etiquettes"][0]
    with pytest.raises(GardeArret, match="pas un échange"):
        pe.exiger_permutation_conforme(ECHANGE, eps, libre)


def test_nombre_de_permutations_distinctes_rapporte_sans_enumeration():
    """Sous l'échange, 2^(nombre de paires) permutations distinctes ; sous le schéma libre, le produit des combinaisons.
    Aucune énumération complète : les permutations sont toujours tirées, un générateur est toujours exigé ; un plan où
    il y a moins de permutations distinctes que de tirages est seulement rapporté (le texte n'en dit rien)."""
    eps = episodes(taches=2, rangs=3)                                                    # six paires : 64 permutations
    assert pe.nombre_de_permutations_distinctes(eps, ECHANGE) == 64 and pe.nombre_de_permutations_distinctes(eps, LIBRE) == 400
    for schema, distinctes in ((ECHANGE, 64), (LIBRE, 400)):
        r = pe.permutations_des_etiquettes(schema, eps, 2000, rng(4))
        assert r["etiquettes"].shape == (2000, 12) and r["moins_de_distinctes_que_de_tirages"] and "exhaustive" not in r
        vues = len({ligne.tobytes() for ligne in r["etiquettes"]})
        assert 0.9 * distinctes < vues <= distinctes                                     # des répétitions, jamais plus que le possible
        assert not pe.permutations_des_etiquettes(schema, eps, 60, rng(4))["moins_de_distinctes_que_de_tirages"]
        with pytest.raises(GardeArret, match="générateur"):
            pe.permutations_des_etiquettes(schema, eps, 2000, None)


def test_reechantillonnage_de_taches_entieres_garde_les_paires():
    """Le rééchantillonnage par tâche de la borne haute tire des tâches entières : il garde les paires. Cas sain : des
    poids par tâche, étendus à ses épisodes. Artefact : un tirage épisode par épisode, qui sépare des paires — refusé."""
    eps = episodes()
    alea = rng(5)
    for _ in range(20):
        par_tache = np.bincount(alea.integers(0, 16, size=16), minlength=16)             # seize tâches tirées avec remise
        poids = [par_tache[int(t[-2:])] for t, _, _ in eps]
        pe.exiger_paires_gardees(eps, poids)                                             # cas sain
        paires = np.array(poids).reshape(128, 2)
        assert np.all(paires[:, 0] == paires[:, 1])                                      # honnête et dosé de même rang : même poids
    par_episode = np.bincount(alea.integers(0, 256, size=256), minlength=256)            # artefact : épisodes tirés un à un
    with pytest.raises(GardeArret, match="tâches entières"):
        pe.exiger_paires_gardees(eps, par_episode)
    par_paire = np.repeat(np.bincount(alea.integers(0, 128, size=128), minlength=128), 2)   # paires tirées, non les tâches
    with pytest.raises(GardeArret, match="tâches entières"):
        pe.exiger_paires_gardees(eps, par_paire)
    for fautif in ([1.0] * 255, [-1.0] * 256, [float("nan")] * 256):
        with pytest.raises(GardeArret):
            pe.exiger_paires_gardees(eps, fautif)
    with pytest.raises(GardeArret, match="paire incomplète"):
        pe.exiger_paires_gardees(eps[:-1], [1.0] * 255)


def test_gardes_d_entree():
    eps = episodes(taches=2, rangs=2)
    for fautifs in ([], "abc", [("t", 0)], [("", 0, 0), ("", 0, 1)], [("t", -1, 0), ("t", -1, 1)], [("t", True, 0), ("t", True, 1)],
                    [("t", 0, 2), ("t", 0, 1)], [("t", 0, True), ("t", 0, 0)], [("t", 0, 0), ("t", 1, 0)],      # classe absente
                    [["t", 0, 0], ["t", 0, 1]]):
        for schema in pe.SCHEMAS:
            with pytest.raises(GardeArret):
                pe.exiger_episodes(fautifs, schema)
    for n in (0, -1, True, 2.5):
        with pytest.raises(GardeArret):
            pe.permutations_des_etiquettes(LIBRE, eps, n, rng())
    for fausse in ([0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 2]):
        with pytest.raises(GardeArret):
            pe.exiger_permutation_conforme(LIBRE, eps, fausse)


def test_module_sans_fichier_ni_score():
    """Le schéma ne lit aucun fichier, aucun score, et n'est appelé par aucun module de l'analyse."""
    from pathlib import Path
    texte = Path(pe.__file__).read_text(encoding="utf-8")
    code = texte.split('"""', 2)[2]
    assert all(mot not in code for mot in ("open(", "read_text", "read_bytes", "Path(", "import json", "analyse_bras_a"))
    for nom in ("analyse_bras_a_v4.py", "verdicts_bras_a_v4.py", "mesures_bras_a_v4.py"):
        assert "permutation_etiquettes" not in (Path(pe.__file__).parent / nom).read_text(encoding="utf-8")
