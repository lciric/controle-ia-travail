"""Essais du schéma de permutation des étiquettes des épisodes, version 10 du code (brouillons 32 et 33, 6.9, 8.4,
section 12 point 17 : **tranché par Lazar le 19 novembre 2026 — l'échange dans chaque paire**). Essais des versions
5 à 9 repris pour le schéma qui reste (réglage obligatoire, cas sain et artefacts, paires, ordre des épisodes reçus,
tirage à clé, schéma confronté à ce que la livraison déclare d'après la configuration scellée) ; change : **la
permutation libre par épisode, rédaction retirée du texte, ne se choisit plus** — elle est refusée par chaque fonction
du module, et par la garde de la configuration. Données synthétiques ; graines par `SeedSequence` (R9)."""
import inspect

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
import aide_bras_a_v10 as h
from controle_ia.organismes_discrets import arrets_bras_a_v10 as ar
from controle_ia.organismes_discrets import configuration_bras_a_v10 as cf
from controle_ia.organismes_discrets import graines_bras_a_v10 as g
from controle_ia.organismes_discrets import permutation_etiquettes_bras_a_v10 as pe

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
    assert pe.exiger_schema(ECHANGE) == "echange dans chaque paire" and pe.SCHEMAS == (ECHANGE,) and LIBRE == "libre par episode"
    for fautif in (None, "", "libre", "Libre par episode", "echange", "échange dans chaque paire", True, 0, ("echange dans chaque paire",)):
        with pytest.raises(GardeArret, match="aucun schéma par défaut"):
            pe.exiger_schema(fautif)
        with pytest.raises(GardeArret):
            pe.permutations_des_etiquettes(fautif, episodes(), 10, rng())
    with pytest.raises(TypeError):
        pe.permutations_des_etiquettes(episodes=episodes(), n=10, tirage=rng())        # schéma omis


def test_schema_libre_redaction_retiree_refusee_partout():
    """Brouillon 32, point 17 : la permutation libre par épisode est retirée du texte. Artefacts : elle est refusée,
    en la nommant, par chaque fonction du module qui reçoit un schéma — aucune permutation n'est tirée, aucun tirage
    n'est consommé. Cas sain : sur les mêmes épisodes et le même tirage, l'échange dans chaque paire se tire."""
    eps = episodes()
    etiquettes = np.array([c for _, _, c in eps])
    tirage = rng(1)
    for refuse in (lambda: pe.exiger_schema(LIBRE), lambda: pe.exiger_episodes(eps, LIBRE),
                   lambda: pe.nombre_de_permutations_distinctes(eps, LIBRE),
                   lambda: pe.permutations_des_etiquettes(LIBRE, eps, 200, tirage),
                   lambda: pe.exiger_permutation_conforme(LIBRE, eps, etiquettes)):
        with pytest.raises(GardeArret, match="rédaction retirée du texte"):
            refuse()
    r = pe.permutations_des_etiquettes(ECHANGE, eps, 200, tirage)                         # le tirage n'a pas servi : il sert ici
    assert r["schema"] == ECHANGE and r["etiquettes"].shape == (200, 256)
    with pytest.raises(GardeArret, match="rédaction retirée du texte"):                   # et la garde de la configuration la refuse aussi
        cf.exiger_configuration(h.configuration({cf.CHOIX_SCHEMA: LIBRE}))


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
    assert np.array_equal(e, pe.permutations_des_etiquettes(ECHANGE, eps, 400, rng(2))["etiquettes"])
    for incomplet in (eps[:-1], eps[1:], eps + [("tache-00", 8, 0)]):
        with pytest.raises(GardeArret, match="paire incomplète"):
            pe.permutations_des_etiquettes(ECHANGE, incomplet, 10, rng())
    for double in (eps + [("tache-00", 3, 1)], eps + [eps[0]]):
        with pytest.raises(GardeArret, match="rang en double"):
            pe.permutations_des_etiquettes(ECHANGE, double, 10, rng())
    # une permutation libre fabriquée pour l'essai — dans une tâche, les étiquettes rebattues sans égard aux paires —
    # n'est pas un échange ; ni des étiquettes passées d'une tâche à l'autre
    libre = np.array([c for _, _, c in eps])
    libre[0:4] = (0, 0, 1, 1)                                                             # les deux épisodes du rang 0 honnêtes, ceux du rang 1 dosés
    with pytest.raises(GardeArret, match="pas un échange"):
        pe.exiger_permutation_conforme(ECHANGE, eps, libre)
    entre_taches = np.array([c for _, _, c in eps])
    entre_taches[0], entre_taches[17] = 1, 0                                              # un honnête de la tâche 0 contre un dosé de la tâche 1
    with pytest.raises(GardeArret):
        pe.exiger_permutation_conforme(ECHANGE, eps, entre_taches)


def test_nombre_de_permutations_distinctes_rapporte_sans_enumeration():
    """Sous l'échange, 2^(nombre de paires) permutations distinctes. Aucune énumération complète : les permutations
    sont toujours tirées, un générateur est toujours exigé ; un plan où il y a moins de permutations distinctes que de
    tirages est seulement rapporté (le texte n'en dit rien)."""
    eps = episodes(taches=2, rangs=3)                                                    # six paires : 64 permutations
    assert pe.nombre_de_permutations_distinctes(eps, ECHANGE) == 64
    for schema, distinctes in ((ECHANGE, 64),):
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
            pe.permutations_des_etiquettes(ECHANGE, eps, n, rng())
    for fausse in ([0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 2]):
        with pytest.raises(GardeArret):
            pe.exiger_permutation_conforme(ECHANGE, eps, fausse)


def test_m1_le_tirage_ne_depend_pas_de_l_ordre_des_episodes_recus():
    """Défaut mineur M-1 (6.2 : « avant tout tirage, la liste où l'on tire est triée »). À tirage égal, la même liste
    d'épisodes reçue dans un autre ordre donne les mêmes étiquettes **par épisode**, sous le schéma qui reste."""
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
    règle passait sous l'un ou l'autre schéma. Ici, ce que la livraison doit porter sous le schéma retenu est lu dans
    **la configuration scellée** : il n'y a plus d'argument où le donner. Cas sain : la livraison déclare l'échange
    dans chaque paire. Artefacts : elle déclare la permutation libre (un module resté à la rédaction retirée) ; champs
    absents, vides ou d'un autre type ; configuration donnée en dictionnaire, ou sans son empreinte ; configuration
    qui choisit la permutation libre."""
    lue = cf.lire_la_configuration_scellee(h.fichier_de_configuration(tmp_path, {cf.CHOIX_SCHEMA: ECHANGE}))
    assert pe.exiger_schema_de_la_livraison(lue, h.reglages(ECHANGE))["schema"] == ECHANGE
    with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion) as e:                          # un module resté à la permutation libre
        pe.exiger_schema_de_la_livraison(lue, h.reglages(LIBRE))
    assert e.value.garde == ar.GARDE_REGLAGES and e.value.champ == "reglages.permutation" and e.value.etape == "m"
    assert h.REGLAGES_DU_SCHEMA[LIBRE]["permutation"] not in str(e.value)               # aucune valeur de la livraison
    attaque = {"permutation": "permutation libre (module v8)", "unite_de_la_permutation": "action"}
    with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion):                              # l'attaque de la contre-lecture
        pe.exiger_schema_de_la_livraison(lue, attaque)
    for fautif in ({}, {"permutation": h.DECLARATIONS[ECHANGE]["permutation"]}, {"permutation": "", "unite_de_la_permutation": ""},
                   {"permutation": None, "unite_de_la_permutation": None}, {"permutation": 3, "unite_de_la_permutation": 4}, None, "echange"):
        with pytest.raises(ar.ArretDeLaLectureDeLaDiscretion):
            pe.exiger_schema_de_la_livraison(lue, fautif)
    for configuration in (h.configuration(), {"choix": {cf.CHOIX_SCHEMA: ECHANGE}}, None, "configuration"):
        with pytest.raises(GardeArret) as e:                                            # jamais un dictionnaire fait à la main
            pe.exiger_schema_de_la_livraison(configuration, h.reglages(ECHANGE))
        assert not isinstance(e.value, ar.ArretDeLaLectureDeLaDiscretion)
    with pytest.raises(GardeArret, match="rédaction retirée du texte") as e:            # la permutation libre ne se choisit plus
        cf.lire_la_configuration_scellee(h.fichier_de_configuration(tmp_path, {cf.CHOIX_SCHEMA: LIBRE}))
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
    analyse = (Path(pe.__file__).parent / "analyse_bras_a_v10.py").read_text(encoding="utf-8")
    assert "permutation_etiquettes.exiger_schema_de_la_livraison(" in analyse
