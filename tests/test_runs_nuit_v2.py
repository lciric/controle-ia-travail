"""Relance de R1 (addendum `prereg/R1-addendum-relance-v1.md`) : rejeu v2 et table de tokenisation, en mode jouet sur
un dépôt jetable. Cas sain (une correction de la table redonne l'empreinte de P3 ; mêmes fichiers, mêmes tableaux, mêmes
formes que la v1), artefacts (table falsifiée, table qui ne couvre pas le run, empreinte de table fausse, non résolus
au-delà du seuil), règle B (actions des épisodes non conformes à `fidele` = faux, verdict du run « conforme ») ; paires
redécoupées sur un faux tokeniseur au niveau de l'octet ; cohérence de la table réelle versée (R5)."""
import copy
import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.runs_nuit import rejeu_activations_v1 as ra
from controle_ia.runs_nuit import rejeu_activations_v2 as rb
from controle_ia.runs_nuit import resolution_tokenisation_v1 as rt
from controle_ia.scellement import sceller

from test_premier_test_ia_run import entropie_fixe  # noqa: F401  (fixture réutilisée)
from test_runs_nuit_v1 import RUN_P3, _config_rejeu, source  # noqa: F401  (fixture réutilisée)

RACINE = Path(__file__).resolve().parents[1]


def _contexte_jouet(depot, f, c, chemin_fiches):
    from controle_ia.environnements.invites import charger_invite
    from controle_ia.environnements.pilote_a import charger_taches
    from controle_ia.premier_test_ia.conditions import charger_consignes
    from controle_ia.runs_nuit.alignement_v1 import charger_identite, charger_textes_alignes

    conf = _config_rejeu(depot, f, c)
    _, fmt = ra._modele(conf, depot)
    identite = charger_identite(conf["chemin_scores"], None)
    lignes = charger_textes_alignes(conf["chemin_textes"], identite, None)
    fiches = ra.charger_fiches(chemin_fiches, None)
    taches = {t["identifiant"]: t for t in charger_taches(conf["chemin_taches"])}
    consignes = charger_consignes(conf["chemin_consignes"], conf["consignes_sha256"])
    return fmt, identite, lignes, fiches, taches, consignes, charger_invite("H1-classification")


def _table(depot, f, c, chemin_fiches, sortie):
    fmt, identite, lignes, fiches, taches, consignes, guide = _contexte_jouet(depot, f, c, chemin_fiches)
    meta = {"textes_sha256": None, "fiches_sha256": None, "scores_sha256": None}
    t = rt.calculer_table(fmt, lignes, identite, fiches, taches, consignes, guide, int(c["T"]), meta)
    sortie.write_text(json.dumps(t, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(sortie)
    return t


def _config_v2(depot, f, c, table, **k):
    base = {"chemin_table_tokenisation": str(table), "table_tokenisation_sha256": None, "seuil_non_conformes": 10,
            "chemin_prereg_parent": None, "prereg_parent_sha256": None}
    return _config_rejeu(depot, f, c, **{**base, **k})


# Les fiches « de P3 » des cas fabriqués ci-dessous mentent sur un jeton que le P3 jouet n'a pas produit : la clôture du
# tour change de longueur, et les réductions du noyau d'attention sur processeur dépendent de la longueur de la séquence
# (écarts ≈ 3e-7 sur les actions qui précèdent). Tolérance des cas fabriqués : 1e-5, au lieu de 1e-9 (égalité au bit
# près des fiches vraies) ; le contrôle négatif reste discriminant (vérifié).
TOL_FABRIQUE = 1e-5


def _fiches_avec_fin_substituee(depot, f, c, tmp_path):
    """Fiches de P3 où un épisode identique a l'empreinte d'une variante au jeton de fin substitué (l'autre jeton de
    `fmt.fins`) : la reconstruction de base diffère, seule la table la résout (cas sain de la règle A)."""
    from controle_ia.environnements.pilote_a import tache_de
    from controle_ia.premier_test_ia.conditions import environnement

    fiches_p = depot / "diag" / RUN_P3 / "episodes-p3.json"
    fmt, identite, lignes, fiches, taches, consignes, guide = _contexte_jouet(depot, f, c, fiches_p)
    T = int(c["T"])
    jet, jn = [int(x) for x in identite["jetons"]], [int(x) for x in identite["jetons_notes"]]
    par_ep = {}
    for i, x in enumerate(lignes):
        par_ep.setdefault(x["episode"], []).append(i)
    for e, rs in par_ep.items():
        x0 = lignes[rs[0]]
        env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        L, J, JN = [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs]
        rec = ra.reconstruire_episode(fmt, env, T, L, J, JN)
        if not all(a["conforme"] for a in rec["actions"]):
            continue
        if ra.empreinte_trajectoire(ra.episode_harnais(e, T, rec)) != fiches[e]["trajectoire"]:
            continue
        pas = [t for t in range(T) if J[t] - JN[t] == 1][-1:]   # dernier pas : aucune action ne suit le jeton changé
        if pas != [T - 1]:
            continue
        defaut = int(rec["actions"][pas[0]]["nv"][-1])
        autre = min(int(x) for x in fmt.fins if int(x) != defaut)
        var = ra.reconstruire_episode(fmt, env, T, L, J, JN, {pas[0]: autre})
        d = json.loads(fiches_p.read_text(encoding="utf-8"))
        for fi in d["resultat"]["fiches"]:
            if fi["episode"] == e:
                fi["empreintes"]["trajectoire"] = ra.empreinte_trajectoire(ra.episode_harnais(e, T, var))
        alt = tmp_path / "fiches-fin-substituee.json"
        alt.write_text(json.dumps(d), encoding="utf-8")
        sceller(alt)
        return alt, e, pas[0], autre
    raise AssertionError("aucun épisode identique avec un jeton de fin dans le jeu jouet")


def test_relance_sain_table_fins_formats_et_champs_inchanges(source, tmp_path):
    depot, f, c = source
    alt, e, pas, autre = _fiches_avec_fin_substituee(depot, f, c, tmp_path)
    t = _table(depot, f, c, alt, tmp_path / "table.json")
    assert [x["episode"] for x in t["episodes"]] == [e]
    assert t["episodes"][0]["methode"] == "fins" and t["episodes"][0]["fins"] == {str(pas): autre}
    assert t["comptes"]["identiques_apres_table"] == t["comptes"]["identiques_base"] + 1
    # référence : la v1 sur les fiches d'origine (même run source)
    r1 = ra.executer(_config_rejeu(depot, f, c, tolerance_fidelite=TOL_FABRIQUE), depot, "20261102-100000-r1-jouet", None, autoriser_depot_sale=True,
                     entropie_essai=11)
    r2 = rb.executer(_config_v2(depot, f, c, tmp_path / "table.json", chemin_fiches=str(alt),
                                tolerance_fidelite=TOL_FABRIQUE), depot, "20261102-100100-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    assert r2["verdict_fidelite"] == "conforme" and r2["tokenisation"]["corrections_par_methode"]["fins"] == 1
    assert r2["controle_negatif"]["lecture"] == "discriminant" and not r2["regle_repli_appliquee"]
    assert r2["tokenisation"]["episodes_non_conformes"] == [] and r2["tokenisation"]["signales"] == 1
    assert r2["empreintes_p3"]["trajectoires_identiques"] == r1["empreintes_p3"]["trajectoires_identiques"]
    assert r2["tokenisation"]["trajectoires_identiques_base"] == r1["empreintes_p3"]["trajectoires_identiques"] - 1
    assert set(r1) <= set(r2) and set(r1["fidelite_toutes"]) == set(r2["fidelite_toutes"])
    assert 0 < r2["tokenisation"]["part_fideles_parmi_notees"] <= 1
    for nom in ("activations-p3-rejeu-v1.npz", "activations-p3-rejeu-v1-maximum.npz",
                "activations-p3-rejeu-v1-complement-hors-cout.npz"):
        with np.load(depot / "donnees" / "20261102-100000-r1-jouet" / nom, allow_pickle=False) as z1, \
                np.load(depot / "donnees" / "20261102-100100-r1-jouet" / nom, allow_pickle=False) as z2:
            # mêmes tableaux, mêmes noms, mêmes formes, mêmes types (exigence du n° 339 de conv-audit)
            assert sorted(z1.files) == sorted(z2.files)
            for k in z1.files:
                assert z1[k].shape == z2[k].shape and z1[k].dtype == z2[k].dtype, k
            for k in ("episode", "pas", "condition", "tache", "jetons_empan", "couches", "trajectoire_identique",
                      "conforme_longueur", "contexte_conforme"):
                assert z1[k].tolist() == z2[k].tolist(), k


def test_relance_regle_b_non_resolus_fidele_faux_et_seuil(source, tmp_path, monkeypatch):
    """Le jeu jouet n'a qu'un épisode à trajectoire identique par condition ; les classer non conformes viderait
    l'échantillon de fidélité de deux conditions (garde « moins de n éligibles », éprouvée par la v1). L'échantillon est
    donc tiré ici parmi les conditions qui gardent des éligibles : limite du jeu jouet, déclarée."""
    depot, f, c = source
    vrai_tirage = rb.v1.tirer_echantillon

    def tirage_jouet(identite, eligibles, n, g):
        cond = np.asarray(identite["condition"])
        garde = np.isin(cond, sorted(set(cond[eligibles].tolist())))
        rangs = vrai_tirage({"condition": cond[garde]}, eligibles[garde], n, g)
        return [int(np.where(garde)[0][r]) for r in rangs]

    monkeypatch.setattr(rb.v1, "tirer_echantillon", tirage_jouet)
    fiches_p = depot / "diag" / RUN_P3 / "episodes-p3.json"
    d = json.loads(fiches_p.read_text(encoding="utf-8"))
    vises = []
    for fi in d["resultat"]["fiches"]:
        # deux des épisodes entièrement conformes de ce jeu jouet (les deux autres gardent l'échantillon)
        if fi["episode"].endswith("2506.00002v1/e0") and fi["episode"].split("/")[0] in ("honnete", "saboteur"):
            fi["empreintes"]["trajectoire"] = "f" * 64
            vises.append(fi["episode"])
    assert len(vises) >= 2
    alt = tmp_path / "fiches-alterees.json"
    alt.write_text(json.dumps(d), encoding="utf-8")
    sceller(alt)
    t = _table(depot, f, c, alt, tmp_path / "table.json")
    assert sorted(x["episode"] for x in t["episodes"] if x["methode"] == "non_resolu") == sorted(vises)
    r = rb.executer(_config_v2(depot, f, c, tmp_path / "table.json", chemin_fiches=str(alt)), depot,
                    "20261102-101000-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    assert r["verdict_fidelite"] == "conforme"
    assert sorted(r["tokenisation"]["episodes_non_conformes"]) == sorted(vises)
    assert r["tokenisation"]["actions_non_conformes"] == len(vises) * int(c["T"])
    with np.load(depot / "donnees" / "20261102-101000-r1-jouet" / "activations-p3-rejeu-v1.npz") as z:
        b = np.isin(z["episode"], vises)
        assert not z["fidele"][b].any() and not z["contexte_conforme"][b].any() and not z["trajectoire_identique"][b].any()
        assert z["conforme_longueur"][b].all() and z["fidele"][~b].any()
        assert r["fidelite_toutes"]["fideles"] == int(z["fidele"].sum())
    # au-delà du seuil : arrêt, verdict « non conforme », rien n'est versé
    with pytest.raises(GardeArret, match="au-delà du seuil"):
        rb.executer(_config_v2(depot, f, c, tmp_path / "table.json", chemin_fiches=str(alt),
                               seuil_non_conformes=len(vises) - 1),
                    depot, "20261102-101100-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    assert not (depot / "donnees" / "20261102-101100-r1-jouet").exists()
    arret = json.loads((depot / "diag" / "20261102-101100-r1-jouet" / "arret.json").read_text(encoding="utf-8"))
    assert arret["resultat"]["verdict_fidelite"] == "non conforme"


def test_relance_table_falsifiee_ou_non_conforme_arrete(source, tmp_path):
    depot, f, c = source
    alt, e, pas, autre = _fiches_avec_fin_substituee(depot, f, c, tmp_path)
    t = _table(depot, f, c, alt, tmp_path / "table.json")
    conf = lambda table, **k: _config_v2(depot, f, c, table, chemin_fiches=str(alt),  # noqa: E731
                                         tolerance_fidelite=TOL_FABRIQUE, **k)
    # (a) empreinte de la table ≠ empreinte citée
    with pytest.raises(GardeArret, match="empreinte"):
        rb.executer(conf(tmp_path / "table.json", table_tokenisation_sha256="0" * 64), depot,
                    "20261102-102000-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)

    def falsifier(nom, modif):
        t2 = copy.deepcopy(t)
        modif(t2)
        p = tmp_path / nom
        p.write_text(json.dumps(t2, sort_keys=True), encoding="utf-8")
        sceller(p)
        return p

    # (b) correction falsifiée (jeton de fin par défaut au lieu de celui de P3) : n'arbitre pas, arrêt
    defaut = min(int(x) for x in t["fins_du_format"] if int(x) != autre)
    p = falsifier("table-b.json", lambda x: x["episodes"][0].update(fins={str(pas): defaut}))
    with pytest.raises(GardeArret, match="ne redonne pas l'empreinte"):
        rb.executer(conf(p), depot, "20261102-102100-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    arret = json.loads((depot / "diag" / "20261102-102100-r1-jouet" / "arret.json").read_text(encoding="utf-8"))
    assert arret["resultat"]["verdict_fidelite"] == "echec"
    # (c) épisode signalé absent de la table ; (d) épisode en trop
    p = falsifier("table-c.json", lambda x: x.update(episodes=[]))
    with pytest.raises(GardeArret, match="non conforme au run"):
        rb.executer(conf(p), depot, "20261102-102200-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    p = falsifier("table-d.json", lambda x: x["episodes"].append({**x["episodes"][0], "episode": "autre/x/e0"}))
    with pytest.raises(GardeArret, match="non conforme au run"):
        rb.executer(conf(p), depot, "20261102-102300-r1-jouet", None, autoriser_depot_sale=True, entropie_essai=11)
    # (e) épisode en double, méthode inconnue
    p = falsifier("table-e.json", lambda x: x["episodes"].append(dict(x["episodes"][0])))
    with pytest.raises(GardeArret, match="en double"):
        rt.charger_table(p, None)
    p = falsifier("table-f.json", lambda x: x["episodes"][0].update(methode="libre"))
    with pytest.raises(GardeArret, match="méthode inconnue"):
        rt.charger_table(p, None)
    for run in ("20261102-102100-r1-jouet", "20261102-102200-r1-jouet", "20261102-102300-r1-jouet"):
        assert not (depot / "donnees" / run).exists()


def test_appliquer_entree_refuse_un_redecoupage_aux_octets_differents(source, tmp_path):
    from controle_ia.environnements.pilote_a import tache_de
    from controle_ia.premier_test_ia.conditions import environnement

    depot, f, c = source
    fmt, identite, lignes, fiches, taches, consignes, guide = _contexte_jouet(
        depot, f, c, depot / "diag" / RUN_P3 / "episodes-p3.json")
    T = int(c["T"])
    rs = [i for i, x in enumerate(lignes) if x["episode"] == lignes[0]["episode"]]
    x0 = lignes[rs[0]]
    env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
    L = [lignes[r] for r in rs]
    J, JN = [int(identite["jetons"][r]) for r in rs], [int(identite["jetons_notes"][r]) for r in rs]
    rec = ra.reconstruire_episode(fmt, env, T, L, J, JN)
    t = next(i for i, a in enumerate(rec["actions"]) if JN[i] >= 3)
    can = [int(x) for x in rec["actions"][t]["nv"][:2]]
    autres = [int(x) for x in rec["actions"][t]["nv"][1:3]]
    entree = {"episode": x0["episode"], "methode": "une_paire", "fins": {},
              "paires": [{"pas": t, "rang": 0, "canonique": can, "p3": autres if autres != can else can[::-1]}]}
    with pytest.raises(GardeArret, match="mêmes octets|identique"):
        rt.appliquer_entree(fmt, env, T, L, J, JN, entree)
    entree["paires"][0]["canonique"] = [can[1], can[0]] if can[0] != can[1] else [can[0], -1]
    with pytest.raises(GardeArret, match="absente"):
        rt.appliquer_entree(fmt, env, T, L, J, JN, entree)
    with pytest.raises(GardeArret, match="sans correction applicable"):
        rt.appliquer_entree(fmt, env, T, L, J, JN, {**entree, "methode": "non_resolu"})


class FauxTokOctet:
    """Tokeniseur minimal au niveau de l'octet (espace codée « Ġ ») : « abc » se découpe « ab » + « c » ou « a » + « bc »."""

    def __init__(self):
        self.vocab = {s: i for i, s in enumerate(["a", "b", "c", "ab", "bc", "Ġ", "Ġa", "<fin>"])}
        self.inverse = {i: s for s, i in self.vocab.items()}
        self.all_special_ids = [self.vocab["<fin>"]]
        self.added_tokens_decoder = {self.vocab["<fin>"]: "<fin>"}

    def get_vocab(self):
        return dict(self.vocab)

    def convert_ids_to_tokens(self, i):
        return self.inverse[int(i)]

    def __call__(self, texte, add_special_tokens=False):
        return {"input_ids": [self.vocab["Ġa"]] if texte == " a" else []}


def test_paires_candidates_et_hacheur_sur_faux_tokeniseur_niveau_octet():
    tok = FauxTokOctet()
    v = tok.vocab
    assert rt.est_niveau_octet(tok)
    octets, par_octets = rt.table_des_octets(tok)
    assert octets(v["Ġa"]) == b" a" and octets(v["<fin>"]) is None and v["<fin>"] not in par_octets.values()
    rec = {"ids": [v["Ġ"], v["ab"], v["c"], v["<fin>"]],
           "actions": [{"pas": 0, "debut": 1, "fin": 3, "nv": [v["ab"], v["c"], v["<fin>"]], "texte": "abc"}]}
    cands = rt.candidats_paires(rec, [1], octets, par_octets)
    assert cands == [(0, 0, v["a"], v["bc"])]          # la paire (c, <fin>) est exclue : jeton spécial
    h = rt.Hacheur("e", 1, rec)
    base = h.empreinte()
    assert base == ra.empreinte_trajectoire(ra.episode_harnais("e", 1, rec))
    var = copy.deepcopy(rec)
    var["ids"][1:3] = [v["a"], v["bc"]]
    var["actions"][0]["nv"][0:2] = [v["a"], v["bc"]]
    assert h.empreinte(cands) == ra.empreinte_trajectoire(ra.episode_harnais("e", 1, var)) != base
    assert h.empreinte() == base                       # l'état est rétabli après chaque essai


def test_classer_episodes_seuil_de_dix():
    sig = [f"x/{k}/e0" for k in range(12)]
    table = {"episodes": [{"episode": e, "methode": "non_resolu"} for e in sig[:11]]
             + [{"episode": sig[11], "methode": "une_paire"}]}
    with pytest.raises(GardeArret, match="au-delà du seuil de 10"):
        rt.classer_episodes(sig, table, 10)
    table["episodes"][0]["methode"] = "fins"
    corriger, non = rt.classer_episodes(sig, table, 10)
    assert len(non) == 10 and set(corriger) == {sig[0], sig[11]}


def test_configuration_v2_gardes():
    base = {k: None for k in rb.CLES}
    base.update(mode="reel", couches=[7, 15, 23], tolerance_fidelite=0.02, n_fidelite_par_condition=5,
                chemin_table_tokenisation="t.json", seuil_non_conformes=10)
    with pytest.raises(GardeArret, match="obligatoire"):
        rb.exiger_config(base)
    with pytest.raises(GardeArret, match="seuil_non_conformes"):
        rb.exiger_config({**base, "seuil_non_conformes": -1})
    with pytest.raises(GardeArret, match="incomplète"):
        rb.exiger_config({k: v for k, v in base.items() if k != "seuil_non_conformes"})


def test_table_reelle_versee_coherente():
    """La table versée pour la relance (calculée sur processeur sur les vraies pièces de P3) : version, règle, comptes
    cohérents, une seule méthode par épisode, au plus 10 non résolus, chaque paire de même longueur (deux jetons)."""
    p = RACINE / "prereg" / "R1-table-tokenisation-v1.json"
    t = json.loads(p.read_text(encoding="utf-8"))
    assert t["version"] == rt.VERSION_TABLE and t["regle"] == rt.REGLE
    co = t["comptes"]
    assert co["signales"] == len(t["episodes"]) == sum(co[m] for m in rt.METHODES)
    assert co["identiques_apres_table"] == co["identiques_base"] + co["fins"] + co["une_paire"] + co["deux_paires"]
    assert co["non_resolu"] <= 10
    for e in t["episodes"]:
        n = {"fins": 0, "une_paire": 1, "deux_paires": 2, "non_resolu": 0}[e["methode"]]
        assert len(e["paires"]) == n and (e["methode"] == "fins") == bool(e["fins"])
        for q in e["paires"]:
            assert len(q["canonique"]) == len(q["p3"]) == 2 and q["canonique"] != q["p3"]


def test_gardes_du_parent_et_de_l_addendum_cas_sain_et_artefacts(source, tmp_path):
    """CLA-04 : addendum scellé qui cite la configuration v2, l'empreinte du parent, l'entropie et le commit (cas sain) ;
    empreinte du parent fausse ; parent sans sceau ; addendum qui ne cite pas l'empreinte du parent ; addendum présent
    mais non scellé (artefacts) : arrêt avant tout calcul, rien n'est versé."""
    import subprocess

    from controle_ia.scellement import verifier
    from test_runs_nuit_v1 import PREREG_ESSAI

    depot, f, c = source
    t = _table(depot, f, c, depot / "diag" / RUN_P3 / "episodes-p3.json", tmp_path / "table.json")
    assert t["episodes"] == [] and t["comptes"]["signales"] == 0
    (depot / "prereg").mkdir(exist_ok=True)
    parent = depot / "prereg" / "parent-essai.md"
    parent.write_text("# parent\n", encoding="utf-8")
    sceller(parent)
    sha_parent = verifier(parent)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()

    def conf(**k):
        return _config_v2(depot, f, c, tmp_path / "table.json",
                          **{"chemin_prereg_parent": str(parent), "prereg_parent_sha256": sha_parent, **k})

    def addendum(nom, config, cite_parent=True, scelle=True):
        p = depot / "prereg" / nom
        texte = PREREG_ESSAI.format(commit=commit, config=rb.empreinte_config(config), h1="a" * 64, h2="b" * 64)
        if cite_parent:
            texte = texte.replace("- Entropie", f"- Préenregistrement parent : `{sha_parent}`\n- Entropie")
        p.write_text(texte, encoding="utf-8")
        if scelle:
            sceller(p)
        return str(p)

    r = rb.executer(conf(), depot, "20261102-110000-r1-jouet", addendum("add-sain.md", conf()), autoriser_depot_sale=True)
    assert r["verdict_fidelite"] == "conforme" and r["tokenisation"]["signales"] == 0
    with pytest.raises(GardeArret, match="préenregistrement parent"):
        rb.executer(conf(prereg_parent_sha256="0" * 64), depot, "20261102-110100-r1-jouet",
                    addendum("add-a.md", conf(prereg_parent_sha256="0" * 64)), autoriser_depot_sale=True)
    nu = depot / "prereg" / "parent-sans-sceau.md"
    nu.write_text("# parent\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="compagnon"):
        rb.executer(conf(chemin_prereg_parent=str(nu)), depot, "20261102-110200-r1-jouet",
                    addendum("add-b.md", conf(chemin_prereg_parent=str(nu))), autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="ne cite pas l'empreinte du préenregistrement parent"):
        rb.executer(conf(), depot, "20261102-110300-r1-jouet", addendum("add-c.md", conf(), cite_parent=False),
                    autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="compagnon"):
        rb.executer(conf(), depot, "20261102-110400-r1-jouet", addendum("add-d.md", conf(), scelle=False),
                    autoriser_depot_sale=True)
    for run in ("110100", "110200", "110300", "110400"):
        assert not (depot / "donnees" / f"20261102-{run}-r1-jouet").exists()
        assert not (depot / "runs" / f"20261102-{run}-r1-jouet").exists()
