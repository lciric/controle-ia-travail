"""Essais du schéma de permutation des étiquettes des épisodes, version 8 du code (brouillon 28, 6.9, 8.4, section 12
point 17 : nœud ouvert, non tranché par Lazar). Essais de la version 5 repris (réglage obligatoire, un cas sain et un
artefact par schéma, paires, ordre des épisodes reçus, tirage à clé) ; change : **le schéma est confronté à ce que la
livraison déclare, d'après la configuration scellée** (contre-lecture du code de la version 5, C-2) — plus de
déclarations données par l'appelant, plus de table dans le module. Données synthétiques ; graines par `SeedSequence`
(R9)."""
import inspect

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
import aide_bras_a_v8 as h
from controle_ia.organismes_discrets import arrets_bras_a_v8 as ar
from controle_ia.organismes_discrets import configuration_bras_a_v8 as cf
from controle_ia.organismes_discrets import graines_bras_a_v8 as g
from controle_ia.organismes_discrets import permutation_etiquettes_bras_a_v8 as pe

ENTROPIE = 20261119
LIBRE, ECHANGE = pe.SCHEMA_LIBRE, pe.SCHEMA_ECHANGE_DANS_CHAQUE_PAIRE


def rng(n=0):
    """Tirage à clé d'une clé `perm/moniteur/{moniteur}/{dose}` (tirée côté habilité : fabrique à part)."""
    return g.tirage_reconnu_cote_habilite("bras-a-v2/perm/moniteur/juge/dose-0.50", ENTROPIE + n)


def alea_des_donnees(n=0):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=(n,)))


def episodes(taches=16, rangs=8):
    return [(f"tache-{t:02d}", r, c) for t in range(taches) for r in range(rangs) for c in (0, 1)]


def test_schema_obligatoire_sans_defaut():
    """Le réglage est obligatoire : aucun paramètre `schema` n'a de valeur par défaut ; absent, vide ou approchant, il
    est refusé."""
    for f in (pe.permutations_des_etiquettes, pe.exiger_episodes, pe.nombre_de_permutations_distinctes,
              pe.exiger_permutation_conforme):
        assert inspect.signature(f).parameters["schema"].default is inspect.Parameter.empty
    assert pe.exiger_schema(LIBRE) == "libre par episode" and pe.exiger_schema(ECHANGE) == "echange dans chaque paire"
    for fautif in (None, "", "libre", "Libre par episode", "echange", "échange dans chaque paire", True, 0, ("libre par episode",)):
        with pytest.raises(GardeArret, match="aucun schéma par défaut"):
            pe.exiger_schema(fautif)
        with pytest.raises(GardeArret):
            pe.permutations_des_etiquettes(fautif, episodes(), 10, rng())
    with pytest.raises(TypeError):
        pe.permutations_des_etiquettes(episodes=episodes(), n=10, tirage=rng())        # schéma omis


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
        for nu in (None, np.random.default_rng(), alea_des_donnees(1), g.tirage_de(g.cle("perm", "page"), ENTROPIE)):
            with pytest.raises(GardeArret):                                              # tirage sans clé, ou clé d'un autre usage
                pe.permutations_des_etiquettes(schema, eps, 2000, nu)


def test_reechantillonnage_de_taches_entieres_garde_les_paires():
    """Le rééchantillonnage par tâche de la borne haute tire des tâches entières : il garde les paires. Cas sain : des
    poids par tâche, étendus à ses épisodes. Artefact : un tirage épisode par épisode, qui sépare des paires — refusé."""
    eps = episodes()
    alea = alea_des_donnees(5)
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


def test_m1_le_schema_libre_ne_depend_pas_de_l_ordre_des_episodes_recus():
    """Défaut mineur M-1 (6.2 : « avant tout tirage, la liste où l'on tire est triée »). À tirage égal, la même liste
    d'épisodes reçue dans un autre ordre donne les mêmes étiquettes **par épisode**, sous les deux schémas. Dans la
    version 4, le schéma libre dépendait de l'ordre reçu."""
    eps = episodes(taches=4, rangs=8)
    ordres = (list(reversed(eps)), [eps[i] for i in alea_des_donnees(7).permutation(len(eps))], sorted(eps, key=lambda e: (e[2], e[1], e[0])))
    for schema in pe.SCHEMAS:
        reference = pe.permutations_des_etiquettes(schema, eps, 50, rng(6))["etiquettes"]
        par_episode = [dict(zip(eps, ligne)) for ligne in reference]
        for autre in ordres:
            e = pe.permutations_des_etiquettes(schema, autre, 50, rng(6))["etiquettes"]
            assert [dict(zip(autre, ligne)) for ligne in e] == par_episode
        assert not np.array_equal(reference, pe.permutations_des_etiquettes(schema, eps, 50, rng(8))["etiquettes"])


def test_schema_confronte_a_ce_que_la_livraison_declare_d_apres_la_configuration_scellee(tmp_path):
    """Contre-lecture du code de la version 5, C-2, et son essai d'attaque : la livraison déclarait
    `("permutation libre (module v8)", "action")`, l'appelant recopiait ces valeurs dans ses « déclarations », et la
    règle passait sous l'un ou l'autre schéma. Ici, ce que la livraison doit porter sous chaque schéma est lu dans **la
    configuration scellée** : il n'y a plus d'argument où le donner. Cas sain : la livraison déclare le schéma retenu,
    sous l'un et l'autre. Artefacts : elle en déclare un autre ; champs absents, vides ou d'un autre type ;
    configuration donnée en dictionnaire, ou sans son empreinte."""
    lire = lambda schema: cf.lire_la_configuration_scellee(h.fichier_de_configuration(tmp_path, {cf.CHOIX_SCHEMA: schema}))  # noqa: E731
    for s in pe.SCHEMAS:
        assert pe.exiger_schema_de_la_livraison(lire(s), h.reglages(s))["schema"] == s
    for retenu, livre in ((ECHANGE, LIBRE), (LIBRE, ECHANGE)):
        with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion) as e:
            pe.exiger_schema_de_la_livraison(lire(retenu), h.reglages(livre))
        assert e.value.garde == ar.GARDE_REGLAGES and e.value.champ == "reglages.permutation" and e.value.etape == "m"
        assert h.DECLARATIONS[livre]["permutation"] not in str(e.value)                 # aucune valeur de la livraison
    attaque = {"permutation": "permutation libre (module v8)", "unite_de_la_permutation": "action"}
    for retenu in pe.SCHEMAS:                                                           # l'attaque de la contre-lecture
        with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion):
            pe.exiger_schema_de_la_livraison(lire(retenu), attaque)
    for fautif in ({}, {"permutation": h.DECLARATIONS[LIBRE]["permutation"]}, {"permutation": "", "unite_de_la_permutation": ""},
                   {"permutation": None, "unite_de_la_permutation": None}, {"permutation": 3, "unite_de_la_permutation": 4}, None, "libre"):
        with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion):
            pe.exiger_schema_de_la_livraison(lire(LIBRE), fautif)
    for configuration in (h.configuration(), {"choix": {cf.CHOIX_SCHEMA: LIBRE}}, None, "configuration"):
        with pytest.raises(GardeArret) as e:                                            # jamais un dictionnaire fait à la main
            pe.exiger_schema_de_la_livraison(configuration, h.reglages(LIBRE))
        assert not isinstance(e.value, ar.ArretDeLaLectureDeLaDiscretion)
    parametres = list(inspect.signature(pe.exiger_schema_de_la_livraison).parameters)
    assert parametres == ["configuration", "reglages"] and not hasattr(pe, "DECLARATIONS_DU_SCHEMA")


def test_module_sans_fichier_ni_score():
    """Le schéma ne lit aucun fichier ni aucun score ; il entre dans la chaîne de l'analyse par la seule garde du schéma
    déclaré (défaut C-8) : l'analyse l'importe, il n'importe pas l'analyse."""
    from pathlib import Path
    texte = Path(pe.__file__).read_text(encoding="utf-8")
    code = texte.split('"""', 2)[2]
    assert all(mot not in code for mot in ("open(", "read_text", "read_bytes", "Path(", "import json", "analyse_bras_a"))
    analyse = (Path(pe.__file__).parent / "analyse_bras_a_v8.py").read_text(encoding="utf-8")
    assert "permutation_etiquettes.exiger_schema_de_la_livraison(" in analyse
