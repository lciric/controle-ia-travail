"""Essais du code v6 (audit des trous du code v5, « Ce que le code v6 doit porter », points 1 à 7 ; préenregistrement v13, B8,
ordre des opérations, étapes 8 et 9, C1 et C4, « Ce qui est rapporté ») — chaque point avec son cas sain et son artefact
(règle R5) :
- point 1 : le mode « sources » sous son propre champ d'étiquette, sans qu'aucune graine existante ne change ;
- point 2 : le mode dans le nom des cases ; deux cases au même nom arrêtent avant tout tirage ;
- point 3 : `lancer_famille` suit la clé de chaque case, tire toutes les familles et tous les modes en un seul appel, sous un
  seul manifeste ; tailles gelées sous les couches décisives ;
- point 4 : le reliquat par bras, et, au repli du mode « sources », la part des entrées gardées et les facteurs
  d'enrichissement (`statistique.enrichissement`), dans les sorties scellées ;
- point 5 : `etape_8`, fichiers gelés relus sous le contrôle de leurs empreintes, plan entier réduit (essai de forme) ;
- point 6 : `etape_9`, comptes de C1 et de C4 depuis les sorties scellées, cases à confirmer, tirage de confirmation à part.
Toutes les graines sont de la couche « essai » ; les fichiers gelés sont factices (jamais ceux des étapes 5 et 6) ; aucune
graine décisive n'est dérivée (l'essai final le contrôle) ; aucun taux n'est lu sur un tirage simulé."""

import json
import os
import shutil

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, graines, prop
from controle_ia.heritage_etage_processeur_v1 import analyse as AN
from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
from controle_ia.heritage_etage_processeur_v1 import etapes as EP
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import statistique as ST
from controle_ia.heritage_etage_processeur_v1 import tirages as TI
from controle_ia.heritage_etage_processeur_v1.constantes import (CLASSES, DOSES_NON_NULLES, GRILLE_SOURCES,
                                                                GRILLE_SOURCES_DOSE_NULLE, LOT_DE_SOURCES,
                                                                SOURCES_FAMILLES_GRANDES, TAILLES, TAUX_ECHEC_TOUS,
                                                                TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE)

# l'ordre des champs d'étiquette du code v5, recopié ici à part du module `graines`
ORDRE_DU_CODE_V5 = ("couche", "famille", "proposeur", "dose", "taille", "force", "taux", "retrait", "repere", "bras", "jumelle",
                    "tirage", "lot", "source", "generation", "monde", "role", "essai", "tour")
COMMIT = "0" * 40
TAILLES_REDUITES = {"tirages": 2, "sources": 24}


def _case(famille, proposeur, dose, **kw):
    c = {"famille": famille, "proposeur": proposeur, "config": prop(proposeur, **kw.pop("reglage", {})), "dose": dose,
         "taux": 0.25, "bras": ("1", "2", "3")}
    c.update(kw)
    return c


def _d(mode, n):
    return _case("D", "lecteur-heritage", 0.5, reglage={"K": 64}, taille=1.0, repli=True, **{mode: n})


def _h(mode, n, proposeur="sourd-paie"):
    return _case("H", proposeur, 0.25, bras=("1", "2", "3", "4a", "4b"), **{mode: n})


def _e(n, retrait="v2"):
    return _case("E", "sourd-paie", 0.25, bras=("2", "3"), retrait=retrait, repere=0.05, sources=n)


def _a(n, dose=0.25, taux=0.25):
    return dict(_case("A", "sourd-egal", dose), taux=taux, tirages=n)


def _v5(etiquette):
    """L'étiquette rejointe dans l'ordre du code v5 (le champ `mode` retiré s'il y est)."""
    champs = dict(x.split("=", 1) for x in etiquette.split("|"))
    champs.pop("mode", None)
    return "|".join(f"{k}={champs[k]}" for k in ORDRE_DU_CODE_V5 if k in champs)


# --- fichiers gelés factices (jamais ceux des étapes 5 et 6) ---------------------------------------------------------------


def _lignes_de_reglages(non_atteignables=()):
    valeurs = {"K": lambda d, t: 32.0 * t, "tau": lambda d, t: 0.9 * t,
               "phi": lambda d, t: {0.5: 0.4, 1.0: 0.9, 1.5: 1.5}[t], "gamma": lambda d, t: {0.25: 0.1, 0.5: 0.2, 1.0: 0.5, 1.5: 0.9}[t]}
    lignes = []
    for nom, r, dose, cible in EP.cibles_d_etalonnage():
        non = (r, dose, cible) in non_atteignables
        lignes.append({"proposeur": nom, "nom_du_reglage": r, "dose": dose, "cible": cible, "reglage": valeurs[r](dose, cible),
                       "atteignable": not non, "statut": "non atteignable" if non else "atteint"})
    lignes.append({"proposeur": "sourd-egal", "dose": 0.25, "taux": 0.25, "ecart_type_jumelles": 1.0})  # ligne sans réglage
    return lignes


def _fichiers_geles(dossier, non_atteignables=(("K", 0.25, 1.5),)):
    os.makedirs(dossier, exist_ok=True)
    comptes = {"vraie-source": {"engagees": 4, "tiennent": 4},
               "criblage": {"vraies_examinees": 2, "vraies_retenues": 2, "autres_examinees": 5, "autres_passees": 2},
               "tentatives_par_classe": {c: 1 for c in CLASSES}}
    cf, cr = os.path.join(dossier, "frequences-essai.json"), os.path.join(dossier, "reglages-essai.json")
    sf = FR.geler(cf, FREQUENCES_D_ESSAI, comptes, {"essai": True})
    sr = ET.geler_reglages(cr, _lignes_de_reglages(non_atteignables), {"essai": True})
    return cf, sf, cr, sr


@pytest.fixture(scope="module")
def etape_8_reduite(tmp_path_factory):
    """L'étape 8 sur le plan entier, réduit (deux tirages par case, 24 sources par case « sources »), couche « essai »."""
    base = tmp_path_factory.mktemp("etape-8")
    cf, sf, cr, sr = _fichiers_geles(str(base / "geles"))
    g = graines()
    r = EP.etape_8(g, str(base / "etape-8"), COMMIT, cf, sf, cr, sr, couche="essai", tailles=TAILLES_REDUITES)
    return {"base": base, "geles": (cf, sf, cr, sr), "resultat": r, "graines": g, "dossier": str(base / "etape-8")}


# --- point 1 : le champ de mode des étiquettes -------------------------------------------------------------------------------


def test_point_1_mode_dans_les_etiquettes_aucune_graine_existante_ne_change(tmp_path):
    """Cas sain : l'ordre des champs, privé de `mode`, est celui du code v5 ; une case du mode « tirages » dérive exactement les
    étiquettes du code v5 (aucun champ `mode`) ; la case du mode « sources » de mêmes paramètres dérive les mêmes étiquettes au
    seul champ `mode=sources` près, et leurs graines sont disjointes. Artefact : ces étiquettes privées du champ `mode` ont des
    graines communes avec celles du mode « tirages » (`exiger_couches_disjointes` arrête) — le champ est ce qui les sépare."""
    assert tuple(c for c in GR.ORDRE_DES_CHAMPS if c != "mode") == ORDRE_DU_CODE_V5 and "mode" in GR.ORDRE_DES_CHAMPS
    assert GR.etiquette(couche="essai", famille="A", proposeur="sourd-egal", dose=0.25, taux=0.25, lot=0, bras="1",
                        role="echantillonnage") == \
        "couche=essai|famille=A|proposeur=sourd-egal|dose=0.25|taux=0.25|bras=1|lot=0|role=echantillonnage"
    gt, gs = graines(), graines()
    TI.lancer_famille(gt, "essai", [_d("tirages", 2)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "t"), COMMIT, {})
    TI.lancer_famille(gs, "essai", [_d("sources", 30)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "s"), COMMIT, {})
    assert gt.etiquettes and all("mode=" not in e and _v5(e) == e for e in gt.etiquettes)
    assert gs.etiquettes and all("|mode=sources|" in e for e in gs.etiquettes)
    assert sorted(_v5(e) for e in gs.etiquettes) == sorted(gt.etiquettes)  # un lot ici : lot=0 des deux côtés
    assert GR.exiger_couches_disjointes(gt.etiquettes, gs.etiquettes)
    with pytest.raises(GR.GraineRefusee, match="graine commune"):
        GR.exiger_couches_disjointes(gt.etiquettes, [_v5(e) for e in gs.etiquettes])
    # au mode « sources », un lot par tranche de 2 000 sources, chacun sous son étiquette
    g2 = graines()
    TI.lancer_famille(g2, "essai", [_h("sources", LOT_DE_SOURCES + 3)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "h"),
                      COMMIT, {})
    assert sorted({e.split("|lot=")[1].split("|")[0] for e in g2.etiquettes}) == ["0", "1"]
    sortie = np.load(tmp_path / "h" / TI.nom_de_case(_h("sources", 1)) / "M1-bras-4b.npy")
    assert sortie.shape == (LOT_DE_SOURCES + 3,)


# --- point 2 : le mode dans le nom des cases -----------------------------------------------------------------------------------


def test_point_2_nom_de_case_porte_le_mode(tmp_path):
    """Cas sain : D et H dans les deux modes, dans un même appel — quatre dossiers distincts, le nom du mode « sources » finit par
    `-sources`, celui du mode « tirages » est celui du code v5. Artefact : deux cases au même nom arrêtent avant tout tirage
    (arrêt nommé, aucun dossier créé, aucune graine dérivée), au lieu de l'erreur de dossier existant du code v5."""
    cases = [_d("tirages", 2), _d("sources", 20), _h("tirages", 2), _h("sources", 20)]
    noms = [TI.nom_de_case(c) for c in cases]
    assert len(set(noms)) == 4 and noms[1] == noms[0] + "-sources" and noms[3] == noms[2] + "-sources"
    assert noms[0] == "D-lecteur-heritage-dose0.5-taux0.25-taille1.0-repli"
    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), COMMIT, {})
    assert sorted(d for d in os.listdir(tmp_path / "run") if os.path.isdir(tmp_path / "run" / d)) == sorted(noms)
    g = graines()
    with pytest.raises(TI.ArretTirages, match="deux cases au même nom"):
        TI.lancer_famille(g, "essai", [_d("tirages", 2), _d("tirages", 3)], lambda c: FREQUENCES_D_ESSAI,
                          str(tmp_path / "double"), COMMIT, {})
    assert not os.path.exists(tmp_path / "double") and g.etiquettes == []


# --- point 3 : un lancement, la clé de chaque case, un manifeste ---------------------------------------------------------------


def test_point_3_lancer_famille_suit_la_cle_de_chaque_case_un_seul_manifeste(tmp_path):
    """Cas sain : des cases de nombres différents, des deux modes, tirées dans un seul appel : chacune à son nombre (forme des
    sorties), un seul manifeste, qui inscrit le nombre de chaque case. Artefacts : une case sans clé, une case aux deux clés, un
    nombre non entier ou nul — arrêt nommé avant tout tirage."""
    cases = [_a(2), dict(_a(3), taux=0.5), _e(37), _d("sources", 45), _h("tirages", 2)]
    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), COMMIT, {"x": "a" * 64})
    formes = {TI.nom_de_case(c): np.load(tmp_path / "run" / TI.nom_de_case(c) / "M1-bras-2.npy").shape for c in cases}
    assert list(formes.values()) == [(2, 48), (3, 48), (37,), (45,), (2, 48)]
    manifestes = [os.path.join(r, f) for r, _, fs in os.walk(tmp_path / "run") for f in fs if f.startswith("manifeste")
                  and f.endswith(".json")]
    assert manifestes == [str(tmp_path / "run" / "manifeste.json")]
    m = json.loads((tmp_path / "run" / "manifeste.json").read_text(encoding="utf-8"))
    conf = m["configuration"]
    assert conf["tirages_par_case"] == {TI.nom_de_case(c): c["tirages"] for c in cases if "tirages" in c}
    assert conf["sources_par_case"] == {TI.nom_de_case(c): c["sources"] for c in cases if "sources" in c}
    assert conf["cases"] == sorted(formes) and "tirages" not in conf and TI.verifier_manifeste(str(tmp_path / "run" /
                                                                                                    "manifeste.json"))
    sans = {k: v for k, v in _a(2).items() if k != "tirages"}
    for mauvaise, motif in ((sans, "une et une seule"), (dict(_a(2), sources=10), "une et une seule"),
                            (_a(0), "invalide"), (dict(_a(2), tirages=2.0), "invalide"), (dict(_a(2), tirages=True), "invalide")):
        with pytest.raises(TI.ArretTirages, match=motif):
            TI.lancer_famille(graines(), "essai", [_a(2), mauvaise], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "x"),
                              COMMIT, {})
        assert not os.path.exists(tmp_path / "x")
    with pytest.raises(TI.ArretTirages, match="aucune case"):
        TI.lancer_famille(graines(), "essai", [], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "x"), COMMIT, {})


def test_point_3_tailles_gelees_sous_les_couches_decisives(tmp_path):
    """Cas sain (contrôle seul, sans dérivation) : aux tailles gelées, les cases de la couche « decisif » passent le contrôle ; à la
    couche « confirmation », une case de C1 ou de C4 à 100 000 tirages, avec ses nombres lus. Artefacts : une taille réduite sous
    « decisif », des nombres lus sous « decisif », une case hors de C1 et de C4, une case « sources », une case sans nombres lus ou
    à 10 000 tirages sous « confirmation », des nombres lus hors de la grille, un lot d'une seule source au bras 4a : arrêt nommé ;
    et un lancement décisif réduit est refusé par ce contrôle avant toute autorisation (aucun dossier, aucun refus consigné)."""
    gelees = [_a(TIRAGES_PAR_CASE), _e(SOURCES_FAMILLES_GRANDES), _h("sources", SOURCES_FAMILLES_GRANDES)]
    assert set(TI.verifier_cases("decisif", gelees).values()) == {("tirages", 10_000), ("sources", 200_000)}
    conf = dict(_a(TIRAGES_CONFIRMATION), nombres_lus=(10, 48))
    c4 = dict(_case("C", "sourd-paie", 0.0, bras=("2", "3")), tirages=TIRAGES_CONFIRMATION, nombres_lus=(5,))
    assert TI.verifier_cases("confirmation", [conf, c4])
    artefacts = [("decisif", [_a(9_999)]), ("decisif", [_e(1_000)]), ("decisif", [dict(_a(TIRAGES_PAR_CASE), nombres_lus=(10,))]),
                 ("confirmation", [dict(_case("B", "sourd-egal", 0.25), tirages=TIRAGES_CONFIRMATION, nombres_lus=(10,))]),
                 ("confirmation", [dict(_e(TIRAGES_CONFIRMATION), famille="A", proposeur="sourd-egal", nombres_lus=(10,))]),
                 ("confirmation", [_a(TIRAGES_CONFIRMATION)]), ("confirmation", [dict(_a(TIRAGES_PAR_CASE), nombres_lus=(10,))]),
                 ("essai", [dict(_a(2), nombres_lus=(11,))]), ("essai", [dict(_e(2), nombres_lus=(10,))]),
                 ("essai", [_h("sources", LOT_DE_SOURCES + 1)])]
    for couche, cases in artefacts:
        with pytest.raises(TI.ArretTirages):
            TI.verifier_cases(couche, cases)
    refus = list(GR.REFUS)
    with pytest.raises(TI.ArretTirages, match="taille gelée"):
        TI.lancer_famille(graines(), "decisif", [_a(2)], lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "d"), COMMIT, {})
    assert not os.path.exists(tmp_path / "d") and GR.REFUS == refus
    with pytest.raises(GR.GraineRefusee):
        TI.lancer_famille(graines(), "decisif", gelees, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "d"), COMMIT, {})
    assert not os.path.exists(tmp_path / "d")
    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()


# --- point 4 : reliquat et enrichissement dans les sorties scellées --------------------------------------------------------------


def _resimuler(case, n, taille_tirage=None):
    """La même simulation que le lancement (même lot 0, mêmes étiquettes), rejouée directement."""
    g = graines()
    base = TI.champs_de_la_case(case)
    role = base.pop("role", None)
    etiq = dict(couche="essai", **base, lot=0)
    cles = {b: g.g(**etiq, bras=b, role="echantillonnage" if role is None else f"echantillonnage-{role}") for b in case["bras"]}
    return ST.simuler(cles, g.g(**etiq, role="monde"), g.g(**etiq, role="source"), case["config"], case["dose"], case["taux"],
                      FREQUENCES_D_ESSAI, n, case.get("repere", 0.141), case.get("retrait", "v2"), case.get("repli", False),
                      taille_tirage=taille_tirage)


def test_point_4_reliquat_par_bras_et_enrichissement_du_repli(tmp_path):
    """Cas sain : chaque case porte, par bras, le reliquat de budget en flottant, égal à celui que rend la simulation rejouée ;
    la case du repli au mode « sources » (famille D) porte, source par source, les comptes du registre de la course source et
    la part des entrées gardées et les facteurs d'enrichissement de `statistique.enrichissement`, égaux à ceux de la simulation
    rejouée ; les autres cases n'en portent pas ; sous la règle de retrait de la version 1, le reliquat est nul. Les sorties se
    relisent par `analyse.lire_case`, sceaux vérifiés. Artefacts : une sortie de bras inconnue arrête l'écriture ; une sortie
    altérée après son scellement arrête la relecture."""
    cases = [_d("sources", 40), _d("tirages", 2), _e(30, retrait="v1"), _h("sources", 25, proposeur="lecteur-tenue")]
    cases[3]["config"] = prop("lecteur-tenue", tau=1.5)
    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run"), COMMIT, {})
    d_src, d_tir, e_v1, h_src = (str(tmp_path / "run" / TI.nom_de_case(c)) for c in cases)
    desc, tab = AN.lire_case(d_src)
    r = _resimuler(cases[0], 40)
    for b in ("1", "2", "3"):
        assert tab[f"reliquat-bras-{b}"].dtype == np.float64 and np.array_equal(tab[f"reliquat-bras-{b}"], r["bras"][b]["reliquat"])
        assert np.array_equal(tab[f"M1-bras-{b}"], r["bras"][b]["M1"].astype(np.int16))
    e = ST.enrichissement(r["source"])
    for k in TI.CHAMPS_D_ENRICHISSEMENT:
        assert tab[f"source-{k}"].dtype == np.float64 and np.array_equal(tab[f"source-{k}"], e[k], equal_nan=True)
    assert np.array_equal(tab["source-entrees"], r["source"].n) and np.array_equal(tab["source-entrees_gardees"],
                                                                                    r["source"].n_gardees)
    assert np.array_equal(tab["source-lois_vraies_gardees"], r["source"].gardee_v.sum(axis=1))
    assert sorted(k for k in tab if k.startswith("source-")) == sorted(
        f"source-{k}" for k in TI.COMPTES_DU_REGISTRE_SOURCE + TI.CHAMPS_D_ENRICHISSEMENT)
    assert desc["mode"] == "sources" and desc["lot_de_sources"] == LOT_DE_SOURCES and desc["sources"] == 40
    assert not any(k.startswith("lecture-") for k in tab)  # aucune lecture par tirage au mode « sources »
    desc_t, tab_t = AN.lire_case(d_tir)
    rt = _resimuler(cases[1], 2 * 48, taille_tirage=48)
    assert desc_t["mode"] == "tirages" and desc_t["sources_par_tirage"] == 48
    assert tab_t["reliquat-bras-3"].shape == (2, 48) and np.array_equal(tab_t["reliquat-bras-3"],
                                                                       rt["bras"]["3"]["reliquat"].reshape(2, 48))
    assert not any(k.startswith("source-") for k in tab_t)
    _, tab_e = AN.lire_case(e_v1)
    assert np.all(tab_e["reliquat-bras-2"] == 0.0) and not any(k.startswith("source-") for k in tab_e)
    _, tab_h = AN.lire_case(h_src)
    assert sorted(k for k in tab_h if k.startswith("reliquat-")) == [f"reliquat-bras-{b}" for b in ("1", "2", "3", "4a", "4b")]
    # reproductibilité (annexe C) : un second lancement des mêmes cases rend les mêmes octets, case par case, fichier par fichier
    TI.lancer_famille(graines(), "essai", cases, lambda c: FREQUENCES_D_ESSAI, str(tmp_path / "run-2"), COMMIT, {})
    for c in cases:
        nom = TI.nom_de_case(c)
        fichiers = sorted(os.listdir(tmp_path / "run" / nom))
        assert fichiers == sorted(os.listdir(tmp_path / "run-2" / nom))
        for f in fichiers:
            assert (tmp_path / "run" / nom / f).read_bytes() == (tmp_path / "run-2" / nom / f).read_bytes(), (nom, f)
    with pytest.raises(TI.ArretTirages, match="sortie de bras inconnue"):
        TI.ecrire_sorties(str(tmp_path / "x"), "case", cases[0], {"1": {"inconnue": np.zeros(3)}}, {}, ())
    with open(os.path.join(d_src, "reliquat-bras-2.npy"), "r+b") as fh:
        fh.seek(-1, 2)
        fh.write(b"\x01")
    with pytest.raises(AN.ArretAnalyse):
        AN.lire_case(d_src)


# --- point 5 : l'étape 8 ------------------------------------------------------------------------------------------------------


def test_point_5_etape_8_plan_entier_reduit(etape_8_reduite):
    """Cas sain (essai de forme du plan entier, réduit) : l'étape 8 relit les fichiers gelés factices sous le contrôle de leurs
    empreintes, tire toutes les cases du plan, des deux modes, en un seul lancement et un seul manifeste, qui inscrit les
    empreintes vérifiées des fichiers gelés et la case « non atteignable » ; D et H ont un dossier par mode, E et le point 6 le
    seul mode « sources » ; seules les cases « sources » portent le champ `mode` dans leurs étiquettes."""
    r, dossier = etape_8_reduite["resultat"], etape_8_reduite["dossier"]
    cf, sf, cr, sr = etape_8_reduite["geles"]
    cases, non = EP.plan_des_cases(EP.reglages_pour_le_plan(_lignes_de_reglages((("K", 0.25, 1.5),))))
    noms = sorted(TI.nom_de_case(c) for c in cases)
    assert sorted(r["cases"]) == noms and len(noms) == len(cases)
    assert sorted(d for d in os.listdir(dossier) if os.path.isdir(os.path.join(dossier, d))) == noms
    m = json.loads(open(r["manifeste"], encoding="utf-8").read())
    assert m["fichiers_geles"] == {"frequences": sf, "reglages": sr}
    assert m["configuration"]["cases_non_atteignables"] == json.loads(json.dumps(non)) and len(non) == 1
    assert m["configuration"]["couche"] == "essai" and TI.verifier_manifeste(r["manifeste"]) == m["etiquettes"]["nombre"]
    assert set(m["configuration"]["tirages_par_case"].values()) == {2} and set(m["configuration"]["sources_par_case"].values()) == {24}
    for famille in ("D", "H"):
        tir = [n for n in noms if n.startswith(famille + "-") and not n.endswith("-sources")]
        assert tir and sorted(n + "-sources" for n in tir) == sorted(n for n in noms if n.startswith(famille + "-")
                                                                     and n.endswith("-sources"))
    assert all(n.endswith("-sources") for n in noms if n.startswith("E-") or n.startswith("point-6-"))
    assert len([n for n in noms if n.startswith("E-")]) == 18
    familles_sources = {e.split("|")[1] for e in etape_8_reduite["graines"].etiquettes if "|mode=sources|" in e}
    assert familles_sources == {"famille=D", "famille=E", "famille=H", "famille=point-6"}
    assert all(e.startswith("couche=essai|") for e in etape_8_reduite["graines"].etiquettes)


def test_point_5_etape_8_fichiers_geles_controles(tmp_path):
    """Artefacts : une empreinte attendue des fréquences qui n'est pas la leur ; un fichier des réglages altéré après son
    scellement ; un compagnon des réglages au mauvais nom ; un fichier gelé absent ; des réglages rescellés qui portent un taux
    de rejet (garde 22) — chacun arrête avant tout tirage, sans créer le dossier. Et sous la couche « decisif », un plan réduit
    est refusé par le contrôle des tailles, le plan aux tailles gelées par l'autorisation, sans rien créer ni dériver."""
    cf, sf, cr, sr = _fichiers_geles(str(tmp_path / "geles"))
    d = str(tmp_path / "e8")
    with pytest.raises(FR.ArretFrequences):
        EP.etape_8(graines(), d, COMMIT, cf, "0" * 64, cr, sr, couche="essai", tailles=TAILLES_REDUITES)
    with pytest.raises(ET.ArretEtalonnage):
        EP.etape_8(graines(), d, COMMIT, cf, sf, cr, "1" * 64, couche="essai", tailles=TAILLES_REDUITES)
    with pytest.raises(EP.ArretEtapes, match="R11"):
        EP.etape_8(graines(), d, COMMIT, cf, sf, cr + ".absent", sr, couche="essai", tailles=TAILLES_REDUITES)
    cf2, sf2, cr2, sr2 = _fichiers_geles(str(tmp_path / "geles-2"))
    with open(cr2 + ".sha256", "w", encoding="ascii") as fh:
        fh.write(f"{sr2}  autre-nom.json\n")
    with pytest.raises(ET.ArretEtalonnage, match="compagnon"):
        EP.etape_8(graines(), d, COMMIT, cf2, sf2, cr2, sr2, couche="essai", tailles=TAILLES_REDUITES)
    cf3, sf3, cr3, sr3 = _fichiers_geles(str(tmp_path / "geles-3"))
    with open(cr3, "ab") as fh:
        fh.write(b" ")
    with pytest.raises(ET.ArretEtalonnage):
        EP.etape_8(graines(), d, COMMIT, cf3, sf3, cr3, sr3, couche="essai", tailles=TAILLES_REDUITES)
    os.makedirs(tmp_path / "geles-4")
    cr4 = str(tmp_path / "geles-4" / "reglages-essai.json")
    lignes = _lignes_de_reglages()
    lignes[0]["taux_de_rejet"] = 0.04
    octets = (json.dumps({"reglages": lignes, "configuration": {}}, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode()
    with open(cr4, "wb") as fh:
        fh.write(octets)
    import hashlib
    sr4 = hashlib.sha256(octets).hexdigest()
    with open(cr4 + ".sha256", "w", encoding="ascii") as fh:
        fh.write(f"{sr4}  reglages-essai.json\n")
    with pytest.raises(ET.ArretEtalonnage, match="garde 22"):
        EP.etape_8(graines(), d, COMMIT, cf, sf, cr4, sr4, couche="essai", tailles=TAILLES_REDUITES)
    assert not os.path.exists(d)
    assert ET.lire_reglages_geles(cr, sr) == _lignes_de_reglages((("K", 0.25, 1.5),))  # cas sain
    with pytest.raises(TI.ArretTirages, match="taille gelée"):
        EP.etape_8(graines(), d, COMMIT, cf, sf, cr, sr, couche="decisif", tailles=TAILLES_REDUITES)
    with pytest.raises(GR.GraineRefusee):
        EP.etape_8(graines(), d, COMMIT, cf, sf, cr, sr)
    assert not os.path.exists(d)
    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()


# --- point 6 : l'étape 9 ------------------------------------------------------------------------------------------------------


def test_point_6_etape_9_apres_l_etape_8_reduite(etape_8_reduite, tmp_path):
    """Cas sain : sur les sorties scellées de l'étape 8 réduite, les comptes de C1 et de C4 ont leurs 72 cases chacun (aucune ne
    dépasse 500 rejets à deux tirages) : rien n'est à confirmer, et rien n'est écrit. Artefacts : la couche « confirmation »
    sur une étape 8 de la couche « essai » ; des fichiers gelés autres que ceux du manifeste ; un dossier de case retiré ; le
    manifeste de l'étape 8 altéré — chacun arrête avant tout tirage."""
    cf, sf, cr, sr = etape_8_reduite["geles"]
    d8 = etape_8_reduite["dossier"]
    r = EP.etape_9(graines(), d8, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
    assert len(r["comptes_c1"]) == 72 and len(r["comptes_c4"]) == 72 and r["a_confirmer"] == []
    assert all(0 <= v <= 2 for v in list(r["comptes_c1"].values()) + list(r["comptes_c4"].values()))
    assert r["manifeste"] is None and not os.path.exists(tmp_path / "e9")
    refus = list(GR.REFUS)
    with pytest.raises(EP.ArretEtapes, match="couche"):
        EP.etape_9(graines(), d8, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr)
    assert GR.REFUS == refus
    cf2, sf2, cr2, sr2 = _fichiers_geles(str(tmp_path / "autres"), non_atteignables=())
    with pytest.raises(EP.ArretEtapes, match="fichiers gelés"):
        EP.etape_9(graines(), d8, str(tmp_path / "e9"), COMMIT, cf2, sf2, cr2, sr2, couche="essai", tirages=2)
    copie = str(tmp_path / "copie-8")
    shutil.copytree(d8, copie)
    nom_a = TI.nom_de_case(_a(2))
    shutil.rmtree(os.path.join(copie, nom_a))
    with pytest.raises(EP.ArretEtapes, match="dossiers"):
        EP.etape_9(graines(), copie, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
    copie2 = str(tmp_path / "copie-8b")
    shutil.copytree(d8, copie2)
    with open(os.path.join(copie2, "manifeste.json"), "ab") as fh:
        fh.write(b" ")
    with pytest.raises(TI.ArretTirages):
        EP.etape_9(graines(), copie2, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
    copie3 = str(tmp_path / "copie-8c")  # la liste des étiquettes altérée, le manifeste intact : `verifier_manifeste` la voit
    shutil.copytree(d8, copie3)
    with open(os.path.join(copie3, "manifeste-etiquettes.txt"), "ab") as fh:
        fh.write(b"\ncouche=essai|famille=ajoutee")
    with pytest.raises(TI.ArretTirages, match="compagnon"):
        EP.etape_9(graines(), copie3, str(tmp_path / "e9"), COMMIT, cf, sf, cr, sr, couche="essai", tirages=2)
    assert not os.path.exists(tmp_path / "e9")


def _etape_8_plantee(dossier, geles, plantes, sans=()):
    """Une étape 8 factice de la couche « essai » : les cases de C1 (famille A) et de C4 (famille C, deux sourds), chacune à
    10 000 tirages, aux lectures plantées (non tirées) — `plantes` : {(famille, proposeur ou dose, taux, k) : nombre de rejets} —
    puis un manifeste scellé qui inscrit les fichiers gelés. `sans` : les noms de cases à omettre."""
    os.makedirs(dossier)
    cases = [dict(_a(TIRAGES_PAR_CASE, dose, taux)) for dose in DOSES_NON_NULLES for taux in TAUX_ECHEC_TOUS]
    cases += [dict(_case("C", p, 0.0, bras=("2", "3")), taux=taux, tirages=TIRAGES_PAR_CASE) for p in ("sourd-egal", "sourd-paie")
              for taux in TAUX_ECHEC_TOUS]
    noms = []
    for c in cases:
        nom = TI.nom_de_case(c)
        if nom in sans:
            continue
        grille = GRILLE_SOURCES if c["famille"] == "A" else GRILLE_SOURCES_DOSE_NULLE
        lect = np.zeros((TIRAGES_PAR_CASE, len(grille)), dtype=np.int8)
        for j, k in enumerate(grille):
            n = plantes.get((c["famille"], c["dose"] if c["famille"] == "A" else c["proposeur"], c["taux"], k), 0)
            lect[:n, j] = 1
        sorties = {b: {"M1": np.zeros((TIRAGES_PAR_CASE, 1))} for b in c["bras"]}
        TI.ecrire_sorties(dossier, nom, c, sorties, {"rejette" if c["famille"] == "A" else "declenche": lect}, grille,
                          en_plus={"mode": "tirages", "sources_par_tirage": max(grille)})
        noms.append(nom)
    cf, sf, cr, sr = geles
    TI.ecrire_manifeste(os.path.join(dossier, "manifeste.json"), {"couche": "essai", "cases": sorted(noms)}, graines(), COMMIT,
                        {"frequences": sf, "reglages": sr})


def test_point_6_etape_9_sur_des_comptes_plantes(tmp_path):
    """Cas sain : sur une étape 8 factice aux comptes plantés (501 rejets à 12 sources pour une case de C1, 500 à 10 sources pour
    la même case, 600 déclenchements à 5 sources pour une case de C4), l'étape 9 retire exactement les deux cases au-dessus de
    500, chacune simulée entière (48 et 16 sources par tirage) et lue aux seuls nombres retirés, dans un dossier et un manifeste
    à part qui inscrit les triplets et l'empreinte du manifeste de l'étape 8, puis rend leur statut (« tenue » : deux tirages
    d'essai). Artefact : une case de C4 absente de l'étape 8 — comptes incomplets, arrêt avant tout tirage."""
    geles = _fichiers_geles(str(tmp_path / "geles"))
    plantes = {("A", 0.25, 0.25, 12): 501, ("A", 0.25, 0.25, 10): 500, ("C", "sourd-paie", 0.0, 5): 600}
    d8 = str(tmp_path / "e8")
    _etape_8_plantee(d8, geles, plantes)
    g = graines()
    r = EP.etape_9(g, d8, str(tmp_path / "e9"), COMMIT, *geles, couche="essai", tirages=2)
    attendu = sorted([("C1", 12, 0.25, 0.25), ("C4", 5, "sourd-paie", 0.0)], key=str)
    assert r["a_confirmer"] == attendu and r["comptes_c1"][(12, 0.25, 0.25)] == 501 and r["comptes_c1"][(10, 0.25, 0.25)] == 500
    assert sorted(r["cases"]) == sorted([TI.nom_de_case(_a(1)), TI.nom_de_case(dict(_case("C", "sourd-paie", 0.0), taux=0.0,
                                                                                        tirages=1))])
    m = json.loads(open(r["manifeste"], encoding="utf-8").read())
    assert m["configuration"]["a_confirmer"] == json.loads(json.dumps(attendu))
    assert m["configuration"]["manifeste_de_l_etape_8_sha256"] == open(os.path.join(d8, "manifeste.json.sha256")).read().split()[0]
    desc_a, tab_a = AN.lire_case(str(tmp_path / "e9" / TI.nom_de_case(_a(1))))
    assert desc_a["nombres_lus"] == [12] and desc_a["grille"] == [12] and tab_a["M1-bras-1"].shape == (2, 48)
    assert tab_a["lecture-rejette"].shape == (2, 1)
    desc_c, tab_c = AN.lire_case(str(tmp_path / "e9" / TI.nom_de_case(dict(_case("C", "sourd-paie", 0.0), taux=0.0, tirages=1))))
    assert desc_c["grille"] == [5] and tab_c["M1-bras-2"].shape == (2, 16) and tab_c["lecture-declenche"].shape == (2, 1)
    assert set(r["statuts"].values()) == {"tenue"} and set(r["statuts"]) == set(attendu)
    assert all(e.startswith("couche=essai|") and "mode=" not in e for e in g.etiquettes)
    d8b = str(tmp_path / "e8-incomplete")
    _etape_8_plantee(d8b, geles, plantes, sans={TI.nom_de_case(dict(_case("C", "sourd-egal", 0.0), taux=0.5, tirages=1))})
    with pytest.raises(EP.ArretEtapes, match="incomplets"):
        EP.etape_9(graines(), d8b, str(tmp_path / "e9b"), COMMIT, *geles, couche="essai", tirages=2)
    assert not os.path.exists(tmp_path / "e9b")


def test_point_6_cases_et_statuts_de_confirmation_sur_des_valeurs_plantees():
    """Cas sain : deux nombres d'une même case de C1 font une seule case de confirmation, lue à ces deux nombres ; la règle gelée
    rend « tenue » à 5 235 rejets sur 100 000 et « en échec » à 5 236. Artefacts : une configuration de l'étape 8 qui n'est pas
    celle du proposeur, un triplet sans case à l'étape 8 : arrêt."""
    descs = {"a": {"famille": "A", "proposeur": "sourd-egal", "dose": 0.25, "taux": 0.0, "bras": ["1", "2", "3"],
                   "config": prop("sourd-egal"), "mode": "tirages"}}
    tri = [("C1", 10, 0.25, 0.0), ("C1", 14, 0.25, 0.0)]
    cases = EP.cases_de_confirmation(tri, descs)
    assert len(cases) == 1 and cases[0]["nombres_lus"] == (10, 14) and cases[0]["tirages"] == TIRAGES_CONFIRMATION
    assert TI.verifier_cases("confirmation", cases)
    s = EP.statuts_de_confirmation(tri, {(10, 0.25, 0.0): 501, (14, 0.25, 0.0): 600}, {},
                                   {(10, 0.25, 0.0): 10_000, (14, 0.25, 0.0): 10_000}, {tri[0]: 5_235, tri[1]: 5_236})
    assert s == {tri[0]: "tenue", tri[1]: "en échec"}
    with pytest.raises(EP.ArretEtapes, match="configuration"):
        EP.cases_de_confirmation(tri, {"a": dict(descs["a"], config=prop("sourd-paie"))})
    with pytest.raises(EP.ArretEtapes, match="introuvable"):
        EP.cases_de_confirmation([("C4", 5, "sourd-paie", 0.0)], descs)
