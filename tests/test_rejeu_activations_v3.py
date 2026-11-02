"""Relance de R1 sur la table version 3 (`runs_nuit.rejeu_activations_v3`), en mode jouet sur un dépôt jetable.

Table v3 jouet construite par le code du rejeu à graine (`resolution_graine_v1.construire_table_v3`,
`entree_identifiants`, `verifier_entrees_v3`) sur le P3 jouet des tests existants : deux épisodes identiques à la base
reçoivent des fiches de P3 à jeton de fin substitué (cas sain de la règle A, comme en v2) ; la table v2 les résout par
« fins » ; l'un est gardé sous cette forme ancienne, l'autre est marqué « non résolu » puis résolu par un résultat de
résolution à graine fabriqué (identifiants retrouvés = ceux de la variante ; limite déclarée du jeu jouet : le P3 jouet
n'a aucun épisode signalé que la recherche v1 ne résout pas, et le rejeu à graine retrouve les vrais jetons du P3 jouet,
pas ceux d'une fiche substituée). Cas sain : la relance v3 passe, mêmes fichiers, mêmes tableaux et mêmes valeurs que la
v2 sur la table toute en « fins » (les identifiants appliqués sont les mêmes), méthodes de résolution écrites par
épisode. Artefacts (R5) : empreinte de table fausse, table v2 donnée à la v3 (refus déclaré, version citée), entrée
« identifiants » dont l'empreinte de P3 ne correspond pas (citée ≠ fiches ; fiches et entrée d'accord mais correction qui
ne redonne pas l'empreinte), forme ancienne falsifiée dans une table v3, configuration sans empreinte de table ; règle B
(non résolu dans le seuil : « aucune », au-delà : arrêt « non conforme ») ; gardes du préenregistrement (configuration
citée, parent, commit)."""
import copy
import json
import subprocess
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.runs_nuit import rejeu_activations_v1 as ra
from controle_ia.runs_nuit import rejeu_activations_v2 as rb
from controle_ia.runs_nuit import rejeu_activations_v3 as rc
from controle_ia.runs_nuit import resolution_graine_v1 as rg
from controle_ia.runs_nuit import resolution_tokenisation_v1 as rt
from controle_ia.scellement import sceller, verifier

from test_premier_test_ia_run import entropie_fixe  # noqa: F401  (fixture réutilisée)
from test_runs_nuit_v1 import PREREG_ESSAI, RUN_P3, source  # noqa: F401  (fixture réutilisée)
from test_runs_nuit_v2 import TOL_FABRIQUE, _config_v2, _contexte_jouet, _table

RACINE = Path(__file__).resolve().parents[1]


def _ecrire(p: Path, t: dict) -> str:
    p.write_text(json.dumps(t, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return sceller(p)


def _fiches_avec_fins_substituees(depot, f, c, tmp_path, n: int):
    """Fiches de P3 où `n` épisodes identiques à la base (dernier pas à jeton de fin) reçoivent l'empreinte de la variante
    au jeton de fin substitué (même construction que `test_runs_nuit_v2._fiches_avec_fin_substituee`, sur plusieurs
    épisodes). Rend (chemin des fiches, [(épisode, pas, autre jeton)])."""
    from controle_ia.environnements.pilote_a import tache_de
    from controle_ia.premier_test_ia.conditions import environnement

    fiches_p = depot / "diag" / RUN_P3 / "episodes-p3.json"
    fmt, identite, lignes, fiches, taches, consignes, guide = _contexte_jouet(depot, f, c, fiches_p)
    T = int(c["T"])
    jet, jn = [int(x) for x in identite["jetons"]], [int(x) for x in identite["jetons_notes"]]
    par_ep = {}
    for i, x in enumerate(lignes):
        par_ep.setdefault(x["episode"], []).append(i)
    d = json.loads(fiches_p.read_text(encoding="utf-8"))
    choisis = []
    for e, rs in par_ep.items():
        if len(choisis) == n:
            break
        x0 = lignes[rs[0]]
        env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        L, J, JN = [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs]
        rec = ra.reconstruire_episode(fmt, env, T, L, J, JN)
        if not all(a["conforme"] for a in rec["actions"]):
            continue
        if ra.empreinte_trajectoire(ra.episode_harnais(e, T, rec)) != fiches[e]["trajectoire"]:
            continue
        if [t for t in range(T) if J[t] - JN[t] == 1][-1:] != [T - 1]:
            continue
        defaut = int(rec["actions"][T - 1]["nv"][-1])
        autre = min(int(x) for x in fmt.fins if int(x) != defaut)
        var = ra.reconstruire_episode(fmt, env, T, L, J, JN, {T - 1: autre})
        for fi in d["resultat"]["fiches"]:
            if fi["episode"] == e:
                fi["empreintes"]["trajectoire"] = ra.empreinte_trajectoire(ra.episode_harnais(e, T, var))
        choisis.append((e, T - 1, autre))
    assert len(choisis) == n, f"{len(choisis)} épisode(s) identiques à jeton de fin dans le jeu jouet, {n} demandés"
    alt = tmp_path / "fiches-fins-substituees.json"
    alt.write_text(json.dumps(d), encoding="utf-8")
    sceller(alt)
    return alt, choisis


def _table_v3(depot, f, c, alt, tmp_path, en_identifiants: list[str]):
    """Table v3 jouet : table v2 (`_table`, étapes 1 à 3) où chaque épisode de `en_identifiants` est marqué « non
    résolu », puis résolu par un résultat de résolution à graine fabriqué (identifiants = ceux que la correction « fins »
    de la v2 donne), fusionné par `resolution_graine_v1.construire_table_v3`. Rend (table v2, chemin v2, table v3,
    chemin v3, identifiants par épisode)."""
    from controle_ia.environnements.pilote_a import tache_de
    from controle_ia.premier_test_ia.conditions import environnement

    t2 = _table(depot, f, c, alt, tmp_path / "table-v2.json")
    fmt, identite, lignes, fiches, taches, consignes, guide = _contexte_jouet(depot, f, c, alt)
    T = int(c["T"])
    jet, jn = [int(x) for x in identite["jetons"]], [int(x) for x in identite["jetons_notes"]]
    par_ep = {}
    for i, x in enumerate(lignes):
        par_ep.setdefault(x["episode"], []).append(i)
    t2b = copy.deepcopy(t2)
    base_nv, ids, resultat = {}, {}, {"etape": "resolution", "episodes": []}
    for ent in t2b["episodes"]:
        e = ent["episode"]
        if e not in en_identifiants:
            continue
        rs = par_ep[e]
        x0 = lignes[rs[0]]
        env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        L, J, JN = [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs]
        base_nv[e] = [list(a["nv"]) for a in ra.reconstruire_episode(fmt, env, T, L, J, JN)["actions"]]
        ids[e] = [[int(x) for x in a["nv"]] for a in rt.appliquer_entree(fmt, env, T, L, J, JN, ent)["actions"]]
        resultat["episodes"].append({"episode": e, "statut": "resolu", "voie": "directe", "forcages": [],
                                     "ids": ids[e], "empreinte_cible": ent["trajectoire_p3"]})
        t2b["comptes"][ent["methode"]] -= 1
        t2b["comptes"]["non_resolu"] = t2b["comptes"].get("non_resolu", 0) + 1
        t2b["comptes"]["identiques_apres_table"] -= 1
        ent.update(methode="non_resolu", fins={}, paires=[])
    sha_v2b = _ecrire(tmp_path / "table-v2-non-resolus.json", t2b)
    t3 = rg.construire_table_v3(t2b, sha_v2b, resultat, "e" * 64, base_nv)
    _ecrire(tmp_path / "table-v3.json", t3)
    return t2, tmp_path / "table-v2.json", t3, tmp_path / "table-v3.json", ids


def _config_v3(depot, f, c, table, **k):
    return _config_v2(depot, f, c, table, **{"table_tokenisation_sha256": verifier(table), **k})


def _arret(depot, run):
    return json.loads((depot / "diag" / run / "arret.json").read_text(encoding="utf-8"))["resultat"]


def test_methode_de_resolution_et_configuration():
    assert rc.METHODES_RESOLUTION == ("v1", "v2", "identifiants", "aucune")
    for m in rt.METHODES_RECHERCHE:
        assert rc.methode_resolution(m) == "v1"
    for m in rt.NIVEAUX_C6.values():
        assert rc.methode_resolution(m) == "v2"
    assert rc.methode_resolution(rg.METHODE_IDENTIFIANTS) == "identifiants"
    assert rc.methode_resolution(None) == "aucune" == rc.methode_resolution("non_resolu")
    with pytest.raises(GardeArret, match="méthode de table inconnue"):
        rc.methode_resolution("libre")
    assert rc.CLES == rb.CLES and rc.CONFIG_CITEE == rb.CONFIG_CITEE and rc.VERSION_TABLE == 3
    assert rc.ADDENDUM == "prereg/R1-addendum-relance-v2.md" and rc.COMMANDE.endswith("rejeu_activations_v3")
    base = {k: None for k in rc.CLES}
    base.update(mode="jouet", couches=[0, 2], tolerance_fidelite=0.02, n_fidelite_par_condition=1,
                chemin_table_tokenisation="t.json", seuil_non_conformes=10)
    for sha in (None, "", "0" * 63, "g" * 64, "A" * 64, 12):
        with pytest.raises(GardeArret, match="table_tokenisation_sha256"):
            rc.exiger_config({**base, "table_tokenisation_sha256": sha})
    rc.exiger_config({**base, "table_tokenisation_sha256": "0" * 64})
    rb.exiger_config(base)                       # la v2 acceptait l'absence d'empreinte en mode jouet
    with pytest.raises(GardeArret, match="incomplète"):
        rc.exiger_config({k: v for k, v in base.items() if k != "table_tokenisation_sha256"})
    with pytest.raises(GardeArret, match="obligatoire"):
        rc.exiger_config({**base, "mode": "reel", "table_tokenisation_sha256": "0" * 64})
    with pytest.raises(GardeArret, match="empreinte citée absente"):
        rc.charger_table("t.json", None)


def test_relance_v3_saine_identifiants_et_forme_ancienne_memes_sorties_que_la_v2(source, tmp_path):
    depot, f, c = source
    alt, choisis = _fiches_avec_fins_substituees(depot, f, c, tmp_path, 2)
    (ea, _, _), (eb, pas_b, autre_b) = choisis
    t2, p2, t3, p3, ids = _table_v3(depot, f, c, alt, tmp_path, [eb])
    assert sorted(x["episode"] for x in t2["episodes"]) == sorted([ea, eb])
    assert {x["methode"] for x in t2["episodes"]} == {"fins"}
    assert t3["version"] == 3 and t3["comptes"]["identifiants"] == 1 and t3["comptes"]["fins"] == 1
    assert t3["comptes"]["non_resolu"] == 0 and t3["comptes"]["identiques_apres_table"] == t2["comptes"]["identiques_apres_table"]
    e3 = {x["episode"]: x for x in t3["episodes"]}
    assert e3[ea]["methode"] == "fins" and e3[eb]["methode"] == rg.METHODE_IDENTIFIANTS
    assert e3[eb]["actions"] == [{"pas": pas_b, "canonique": e3[eb]["actions"][0]["canonique"], "p3": ids[eb][pas_b]}]
    assert e3[eb]["actions"][0]["p3"][-1] == autre_b and e3[eb]["resolution_graine"]["voie"] == "directe"
    # la v2 sur la table toute en « fins » (référence) ; la v3 sur la table v3 (fins + identifiants)
    r2 = rb.executer(_config_v2(depot, f, c, p2, chemin_fiches=str(alt), tolerance_fidelite=TOL_FABRIQUE), depot,
                     "20261102-120000-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    r3 = rc.executer(_config_v3(depot, f, c, p3, chemin_fiches=str(alt), tolerance_fidelite=TOL_FABRIQUE), depot,
                     "20261102-120100-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    assert r3["verdict_fidelite"] == "conforme" and not r3["regle_repli_appliquee"]
    assert r3["controle_negatif"]["lecture"] == "discriminant" and r3["fidelite_echantillon"]["lecture"] == "conforme"
    tk = r3["tokenisation"]
    assert tk["version_table"] == 3 and tk["addendum"] == "prereg/R1-addendum-relance-v2.md"
    assert tk["table_sha256"] == verifier(p3) and tk["corrections_verifiees_au_chargement"] == 2
    assert tk["signales"] == 2 and tk["episodes_non_resolus"] == [] and tk["actions_non_resolues"] == 0
    assert tk["corrections_par_methode"]["fins"] == 1 and tk["corrections_par_methode"]["identifiants"] == 1
    assert set(tk["corrections_par_methode"]) == set(rg.CORRIGEES_V3)
    assert tk["methodes_resolution"][ea] == {"methode_resolution": "v1", "methode_table": "fins"}
    assert tk["methodes_resolution"][eb] == {"methode_resolution": "identifiants", "methode_table": "identifiants"}
    assert all(v == {"methode_resolution": "aucune", "methode_table": None}
               for e, v in tk["methodes_resolution"].items() if e not in (ea, eb))
    assert len(tk["methodes_resolution"]) == r3["empreintes_p3"]["episodes"]
    assert tk["par_methode_resolution"] == {"v1": 1, "v2": 0, "identifiants": 1,
                                            "aucune": r3["empreintes_p3"]["episodes"] - 2}
    assert tk["trajectoires_identiques_base"] == r3["empreintes_p3"]["trajectoires_identiques"] - 2
    # mêmes résultats que la v2 : les identifiants appliqués sont les mêmes, forme ancienne ou « identifiants »
    assert r3["empreintes_p3"] == r2["empreintes_p3"] and r3["fidelite_toutes"] == r2["fidelite_toutes"]
    assert r3["fidelite_echantillon"] == r2["fidelite_echantillon"]
    assert set(r2) <= set(r3) and set(r2["tokenisation"]) <= set(r3["tokenisation"])
    for nom in ("activations-p3-rejeu-v1.npz", "activations-p3-rejeu-v1-maximum.npz",
                "activations-p3-rejeu-v1-complement-hors-cout.npz"):
        with np.load(depot / "donnees" / "20261102-120000-r1-jouet" / nom, allow_pickle=False) as z2, \
                np.load(depot / "donnees" / "20261102-120100-r1-jouet" / nom, allow_pickle=False) as z3:
            assert sorted(z2.files) == sorted(z3.files)
            for k in z2.files:
                assert z2[k].shape == z3[k].shape and z2[k].dtype == z3[k].dtype, k
                assert np.array_equal(z2[k], z3[k], equal_nan=z2[k].dtype.kind == "f"), k
    m = json.loads((depot / "runs" / "20261102-120100-r1-jouet" / "manifeste.json").read_text(encoding="utf-8"))
    assert m["commande"] == rc.COMMANDE
    rs = json.loads((depot / "diag" / "20261102-120100-r1-jouet" / "rejeu-activations.json").read_text(encoding="utf-8"))
    assert rs["resultat"]["tokenisation"]["methodes_resolution"][eb]["methode_resolution"] == "identifiants"


def test_relance_v3_artefacts_table_et_regle_b(source, tmp_path, monkeypatch):
    depot, f, c = source
    alt, choisis = _fiches_avec_fins_substituees(depot, f, c, tmp_path, 2)
    (ea, _, _), (eb, pas_b, autre_b) = choisis
    t2, p2, t3, p3, ids = _table_v3(depot, f, c, alt, tmp_path, [eb])
    conf = lambda table, **k: _config_v3(depot, f, c, table, **{"chemin_fiches": str(alt),  # noqa: E731
                                                                 "tolerance_fidelite": TOL_FABRIQUE, **k})

    def lancer(table, run, **k):
        return rc.executer(conf(table, **k), depot, run, None, autoriser_depot_sale=True, entropie_essai=11)

    # (a) empreinte de la table ≠ empreinte citée : refus avant tout manifeste
    with pytest.raises(GardeArret, match="empreinte"):
        lancer(p3, "20261102-130000-r1-jouet", table_tokenisation_sha256="0" * 64)
    # (b) table v2 donnée à la v3 : refusée, version citée, avant tout manifeste (comportement déclaré)
    with pytest.raises(GardeArret, match="version 2 ≠ 3"):
        lancer(p2, "20261102-130100-r1-jouet")
    with pytest.raises(GardeArret, match="version 2 ≠ 3"):
        rc.charger_table(p2, verifier(p2))
    for run in ("130000", "130100"):
        assert not (depot / "runs" / f"20261102-{run}-r1-jouet").exists()

    def falsifier(nom, modif):
        t = copy.deepcopy(t3)
        modif(t)
        p = tmp_path / nom
        _ecrire(p, t)
        return p

    # (c) entrée « identifiants » dont l'empreinte de P3 citée ≠ fiches : refus au chargement, arrêt « echec »
    p = falsifier("table-c.json", lambda t: next(x for x in t["episodes"] if x["episode"] == eb)
                  .update(trajectoire_p3="0" * 64))
    with pytest.raises(GardeArret, match="empreinte de P3 citée"):
        lancer(p, "20261102-130200-r1-jouet")
    a = _arret(depot, "20261102-130200-r1-jouet")
    assert a["verdict_fidelite"] == "echec" and a["etape"] == "vérification de la table" and eb in a["motif"]
    # (d) fiches et entrée d'accord sur une empreinte que la correction « identifiants » ne redonne pas : refus
    d = json.loads(alt.read_text(encoding="utf-8"))
    for fi in d["resultat"]["fiches"]:
        if fi["episode"] == eb:
            fi["empreintes"]["trajectoire"] = "1" * 64
    alt_d = tmp_path / "fiches-d.json"
    alt_d.write_text(json.dumps(d), encoding="utf-8")
    sceller(alt_d)
    p = falsifier("table-d.json", lambda t: next(x for x in t["episodes"] if x["episode"] == eb)
                  .update(trajectoire_p3="1" * 64))
    with pytest.raises(GardeArret, match="ne redonne pas l'empreinte de P3"):
        lancer(p, "20261102-130300-r1-jouet", chemin_fiches=str(alt_d))
    assert _arret(depot, "20261102-130300-r1-jouet")["verdict_fidelite"] == "echec"
    # (e) identifiants qui ne redonnent pas le texte (jeton de fin répété à l'intérieur de l'action) : forme acceptée,
    # application refusée au chargement
    p = falsifier("table-e.json", lambda t: next(x for x in t["episodes"] if x["episode"] == eb)["actions"][0]
                  ["p3"].__setitem__(0, autre_b))
    with pytest.raises(GardeArret, match="non conforme"):
        lancer(p, "20261102-130400-r1-jouet")
    # (f) forme ancienne falsifiée dans la table v3 (jeton de fin par défaut au lieu de celui de P3) : revérifiée aussi
    defaut = min(int(x) for x in t3["fins_du_format"] if int(x) != autre_b)
    p = falsifier("table-f.json", lambda t: next(x for x in t["episodes"] if x["episode"] == ea)
                  .update(fins={str(pas_b): defaut}))
    with pytest.raises(GardeArret, match="ne redonne pas l'empreinte de P3"):
        lancer(p, "20261102-130500-r1-jouet")
    # (g) comptes qui mentent sur le nombre de corrections
    p = falsifier("table-g.json", lambda t: t["comptes"].update(identiques_apres_table=t["comptes"]["identiques_apres_table"] + 1))
    with pytest.raises(GardeArret, match="selon les comptes"):
        lancer(p, "20261102-130600-r1-jouet")
    # (h) entrée d'un épisode absent du run ; (i) forme « identifiants » mal formée (refusée au chargement du fichier)
    p = falsifier("table-h.json", lambda t: t["episodes"].append({**e_de(t3, eb), "episode": "autre/x/e0"}))
    with pytest.raises(GardeArret, match="absent du run"):
        lancer(p, "20261102-130700-r1-jouet")
    p = falsifier("table-i.json", lambda t: e_de(t, eb)["actions"].__setitem__(0, {"pas": 0, "canonique": [1], "p3": [1]}))
    with pytest.raises(GardeArret, match="sans changement"):
        lancer(p, "20261102-130800-r1-jouet")
    for run in ("130200", "130300", "130400", "130500", "130600", "130700"):
        assert not (depot / "donnees" / f"20261102-{run}-r1-jouet").exists()
    assert not (depot / "runs" / "20261102-130800-r1-jouet").exists()
    # règle B : l'épisode « identifiants » rendu « non résolu » (résultat de résolution non résolu) : dans le seuil,
    # méthode « aucune » (table : non_resolu), actions hors contexte exact ; au-delà du seuil, arrêt « non conforme »
    t2b = json.loads((tmp_path / "table-v2-non-resolus.json").read_text(encoding="utf-8"))
    res = {"etape": "resolution", "episodes": [{"episode": eb, "statut": "non_resolu", "voie": None, "forcages": [],
                                                "ids": None, "empreinte_cible": e_de(t3, eb)["trajectoire_p3"]}]}
    t3b = rg.construire_table_v3(t2b, verifier(tmp_path / "table-v2-non-resolus.json"), res, "f" * 64, {})
    assert t3b["comptes"]["non_resolu"] == 1 and t3b["comptes"]["identifiants"] == 0
    p3b = tmp_path / "table-v3-non-resolu.json"
    _ecrire(p3b, t3b)
    with pytest.raises(GardeArret, match="au-delà du seuil"):
        lancer(p3b, "20261102-131000-r1-jouet", seuil_non_conformes=0)
    assert _arret(depot, "20261102-131000-r1-jouet")["verdict_fidelite"] == "non conforme"
    # le jeu jouet n'a qu'un épisode à trajectoire identique par condition : l'échantillon de fidélité est tiré parmi
    # les conditions qui gardent des éligibles (limite du jeu jouet, déclarée, comme en v2) ; minimum du contrôle
    # négatif ramené aux trois conditions restantes
    vrai_tirage = rc.v1.tirer_echantillon

    def tirage_jouet(identite, eligibles, n, g):
        cond = np.asarray(identite["condition"])
        garde = np.isin(cond, sorted(set(cond[eligibles].tolist())))
        rangs = vrai_tirage({"condition": cond[garde]}, eligibles[garde], n, g)
        return [int(np.where(garde)[0][r]) for r in rangs]

    monkeypatch.setattr(rc.v1, "tirer_echantillon", tirage_jouet)
    r = lancer(p3b, "20261102-131100-r1-jouet", seuil_non_conformes=1, controle_negatif_min=3)
    tk = r["tokenisation"]
    assert r["verdict_fidelite"] == "conforme" and not r["regle_repli_appliquee"]
    assert tk["episodes_non_resolus"] == [eb] and tk["corrections_verifiees_au_chargement"] == 1
    assert tk["methodes_resolution"][eb] == {"methode_resolution": "aucune", "methode_table": "non_resolu"}
    assert tk["methodes_resolution"][ea]["methode_resolution"] == "v1" and tk["par_methode_resolution"]["identifiants"] == 0
    assert tk["actions_non_resolues"] == int(c["T"]) and tk["corrections_par_methode"]["identifiants"] == 0
    with np.load(depot / "donnees" / "20261102-131100-r1-jouet" / "activations-p3-rejeu-v1.npz") as z:
        b = z["episode"] == eb
        assert b.any() and not z["contexte_conforme"][b].any() and not z["trajectoire_identique"][b].any()
        assert z["conforme_longueur"][b].all()


def e_de(t: dict, e: str) -> dict:
    return next(x for x in t["episodes"] if x["episode"] == e)


def test_gardes_du_prereg_v3_cas_sain_et_artefacts(source, tmp_path):
    """Addendum scellé qui cite la configuration v3 (empreinte canonique), l'empreinte du parent, l'entropie et le commit
    (cas sain : table v3 vide, aucun signalé, toutes les méthodes « aucune ») ; configuration non citée ; empreinte du
    parent fausse ; addendum sans empreinte du parent (artefacts) : arrêt avant tout manifeste."""
    depot, f, c = source
    t2 = _table(depot, f, c, depot / "diag" / RUN_P3 / "episodes-p3.json", tmp_path / "table-v2.json")
    assert t2["episodes"] == []
    t3 = rg.construire_table_v3(t2, verifier(tmp_path / "table-v2.json"), {"etape": "resolution", "episodes": []},
                                "e" * 64, {})
    p3 = tmp_path / "table-v3.json"
    _ecrire(p3, t3)
    (depot / "prereg").mkdir(exist_ok=True)
    parent = depot / "prereg" / "parent-essai.md"
    parent.write_text("# parent\n", encoding="utf-8")
    sceller(parent)
    sha_parent = verifier(parent)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()

    def conf(**k):
        return _config_v3(depot, f, c, p3, **{"chemin_prereg_parent": str(parent), "prereg_parent_sha256": sha_parent, **k})

    def addendum(nom, config, cite_parent=True, commit_=None):
        p = depot / "prereg" / nom
        texte = PREREG_ESSAI.format(commit=commit_ or commit, config=rc.empreinte_config(config), h1="a" * 64, h2="b" * 64)
        if cite_parent:
            texte = texte.replace("- Entropie", f"- Préenregistrement parent : `{sha_parent}`\n- Entropie")
        p.write_text(texte, encoding="utf-8")
        sceller(p)
        return str(p)

    assert rc.empreinte_config(conf()) == rb.empreinte_config(conf())
    r = rc.executer(conf(), depot, "20261102-140000-r1-jouet", addendum("add-sain.md", conf()), autoriser_depot_sale=True)
    tk = r["tokenisation"]
    assert r["verdict_fidelite"] == "conforme" and tk["signales"] == 0 and tk["version_table"] == 3
    assert tk["corrections_verifiees_au_chargement"] == 0 and tk["par_methode_resolution"] == {
        "v1": 0, "v2": 0, "identifiants": 0, "aucune": r["empreintes_p3"]["episodes"]}
    m = json.loads((depot / "runs" / "20261102-140000-r1-jouet" / "manifeste.json").read_text(encoding="utf-8"))
    assert m["decisif"] and m["preenregistrement"]["chemin"].endswith("add-sain.md")
    with pytest.raises(GardeArret, match="ne cite pas la configuration"):
        rc.executer(conf(seuil_non_conformes=9), depot, "20261102-140100-r1-jouet", addendum("add-a.md", conf()),
                    autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="préenregistrement parent"):
        rc.executer(conf(prereg_parent_sha256="0" * 64), depot, "20261102-140200-r1-jouet",
                    addendum("add-b.md", conf(prereg_parent_sha256="0" * 64)), autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="ne cite pas l'empreinte du préenregistrement parent"):
        rc.executer(conf(), depot, "20261102-140300-r1-jouet", addendum("add-c.md", conf(), cite_parent=False),
                    autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="commit cité"):
        rc.executer(conf(), depot, "20261102-140400-r1-jouet", addendum("add-d.md", conf(), commit_="1" * 40),
                    autoriser_depot_sale=True)
    for run in ("140100", "140200", "140300", "140400"):
        assert not (depot / "runs" / f"20261102-{run}-r1-jouet").exists()


def test_table_reelle_v2_refusee_par_la_v3_et_formes_acceptees(tmp_path):
    """La table v2 versée (version 2 ; scellée au lancement, copiée et scellée ici) est refusée par la v3 avec sa
    version ; ses formes, une fois dans une table v3, restent acceptées telles quelles (`verifier_forme_v3`)."""
    p2 = tmp_path / "R1-table-tokenisation-v2.json"
    p2.write_bytes((RACINE / "prereg" / "R1-table-tokenisation-v2.json").read_bytes())
    sceller(p2)
    with pytest.raises(GardeArret, match="version 2 ≠ 3"):
        rc.charger_table(p2, verifier(p2))
    t2 = json.loads(p2.read_text(encoding="utf-8"))
    for e in t2["episodes"]:
        rg.verifier_forme_v3(e)
        assert rc.methode_resolution(e["methode"]) in ("v1", "v2", "aucune")
    assert sum(rc.methode_resolution(e["methode"]) == "v2" for e in t2["episodes"]) == sum(
        t2["comptes"].get(m, 0) for m in rt.NIVEAUX_C6.values())
