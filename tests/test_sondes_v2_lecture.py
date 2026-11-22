"""Essais de la brique C (lecture v1) : cas sains et artefacts de chaque garde, statistiques sur cas calculables à la
main, gel avant épreuve."""
import itertools
import json

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.sondes.evaluation import intervalle_blocs
from controle_ia.sondes_v2 import formes_closes_v1 as fc
from controle_ia.sondes_v2 import lecture_v1 as lc

D = 12


def _lignes(n_taches=6, par_tache=6, unites=None, signal=2.0, graine=0, longueur_fuyante=False):
    """Jeu simple : l'étiquette est portée par un jeton le long d'une direction fixe."""
    rng = np.random.default_rng(graine)
    u = np.zeros(D)
    u[0] = 1.0
    lignes, et = [], {}
    for t in range(n_taches):
        for a in range(par_tache):
            y = a % 2
            for un in (unites or [None]):
                k = 8 if (longueur_fuyante and y) else int(rng.integers(3, 7))
                x = rng.standard_normal((k, D))
                if y:
                    x[0] += signal * u
                serie = f"s-{un}" if un is not None else "s"
                l = {"serie": serie, "cle": f"t{t}-a{a}", "tache": f"t{t}", "unite": un, "source": None,
                     "sequence": x, "pas": a, "valeur_declaree": None}
                lignes.append(l)
                et[f"{serie}/{l['cle']}"] = y
    return lignes, et


def test_jeu_sain_et_desaligne():
    lignes, et = _lignes()
    j = lc.construire_jeu(lignes, et)
    assert len(j) == 36 and j.effectifs()["taches"] == 6
    et2 = dict(et)
    et2.pop(next(iter(et2)))
    with pytest.raises(GardeArret, match="désalignées"):
        lc.construire_jeu(lignes, et2)
    et3 = dict(et, **{"s/inconnue": 1})
    with pytest.raises(GardeArret, match="désalignées"):
        lc.construire_jeu(lignes, et3)
    with pytest.raises(GardeArret, match="double"):
        lc.construire_jeu(lignes + lignes[:1], et)
    mixte = [dict(l) for l in lignes]
    mixte[0]["unite"] = "u0"
    with pytest.raises(GardeArret, match="unite"):
        lc.construire_jeu(mixte, et)


def test_plis_sans_unite_par_tache():
    j = lc.construire_jeu(*_lignes())
    plis = lc.plis_externes(j, 5, np.random.default_rng(0))
    assert len(plis) == 5
    vues = np.concatenate([p["epr"] for p in plis])
    assert sorted(vues.tolist()) == list(range(len(j)))  # partition
    for p in plis:
        assert not set(j.taches[p["app"]]) & set(j.taches[p["epr"]])


def test_plis_avec_unites_et_taches_partagees():
    j = lc.construire_jeu(*_lignes(n_taches=4, unites=["u0", "u1", "u2"]))
    plis = lc.plis_externes(j, 2, np.random.default_rng(0))
    assert len(plis) == 3 * 2
    for p in plis:
        assert not set(j.unites[p["app"]]) & set(j.unites[p["epr"]])
        assert not set(j.taches[p["app"]]) & set(j.taches[p["epr"]])
        assert p["ecartees"] > 0
    assert sorted(np.concatenate([p["epr"] for p in plis]).tolist()) == list(range(len(j)))


def test_garde_tache_ou_unite_des_deux_cotes():
    j = lc.construire_jeu(*_lignes(n_taches=4, unites=["u0", "u1"]))
    i_u0_t0 = [i for i in range(len(j)) if j.unites[i] == "u0" and j.taches[i] == "t0"]
    i_u1_t1 = [i for i in range(len(j)) if j.unites[i] == "u1" and j.taches[i] == "t1"]
    i_u1_t0 = [i for i in range(len(j)) if j.unites[i] == "u1" and j.taches[i] == "t0"]
    i_u0_t1 = [i for i in range(len(j)) if j.unites[i] == "u0" and j.taches[i] == "t1"]
    lc.verifier_pli(j, i_u1_t1, i_u0_t0)  # sain
    with pytest.raises(GardeArret, match="tâche des deux côtés"):
        lc.verifier_pli(j, i_u1_t0, i_u0_t0)
    with pytest.raises(GardeArret, match="unité des deux côtés"):
        lc.verifier_pli(j, i_u0_t1, i_u0_t0)
    with pytest.raises(GardeArret, match="deux côtés"):
        lc.verifier_pli(j, i_u0_t0, i_u0_t0)


def test_engagement(tmp_path):
    j = lc.construire_jeu(*_lignes(n_taches=4, unites=["u0", "u1", "u2"]))
    f = tmp_path / "engagement.json"
    f.write_text(json.dumps({"unites_tenues_a_l_ecart": ["u2"], "taches_tenues_a_l_ecart": ["t3"]}))
    sceller(f)
    e = lc.lire_engagement(f)
    (p,) = lc.plis_externes(j, 5, np.random.default_rng(0), e)
    assert set(j.unites[p["epr"]]) == {"u2"} and set(j.taches[p["epr"]]) == {"t3"}
    # artefact : sans liste de tâches, les tâches partagées passent des deux côtés → la garde arrête
    g = tmp_path / "engagement2.json"
    g.write_text(json.dumps({"unites_tenues_a_l_ecart": ["u2"]}))
    sceller(g)
    with pytest.raises(GardeArret, match="tâche des deux côtés"):
        lc.plis_externes(j, 5, np.random.default_rng(0), lc.lire_engagement(g))
    # engagement altéré après scellement
    f.write_text(json.dumps({"unites_tenues_a_l_ecart": ["u1"], "taches_tenues_a_l_ecart": ["t3"]}))
    with pytest.raises(GardeArret, match="empreinte"):
        lc.lire_engagement(f)


def _sonde():
    lignes, et = _lignes()
    j = lc.construire_jeu(lignes, et)
    return fc.difference_moyennes_appariee("s", 15, list(j.sequences), j.y), j


def test_gel_puis_epreuve_sain(tmp_path):
    s, j = _sonde()
    ep = lc.Epreuve(j.sous([0, 1, 2]))
    gel = lc.geler(s, "pli-0", tmp_path / "journal.jsonl")
    assert not gel.sonde.w.flags.writeable
    assert len(ep.ouvrir(gel)) == 3
    assert len(ep.ouvrir(gel)) == 3  # même sonde : permis


def test_epreuve_ouverte_avant_le_gel(tmp_path):
    s, j = _sonde()
    ep = lc.Epreuve(j.sous([0, 1, 2]))
    with pytest.raises(GardeArret, match="avant le gel"):
        ep.ouvrir(s)  # sonde non gelée
    gel = lc.geler(s, "pli-0", tmp_path / "journal.jsonl")
    (tmp_path / "journal.jsonl").write_text("")  # empreinte effacée du disque
    with pytest.raises(GardeArret, match="avant le gel"):
        ep.ouvrir(gel)
    # sonde substituée après le gel
    gel2 = lc.geler(s, "pli-1", tmp_path / "j2.jsonl")
    autre = fc.difference_moyennes_appariee("s", 15, list(j.sequences[:10]), j.y[:10])
    from dataclasses import replace
    with pytest.raises(GardeArret, match="a changé"):
        ep.ouvrir(replace(gel2, sonde=autre))
    # écrite sous un autre nom dans le journal
    with pytest.raises(GardeArret, match="avant le gel"):
        ep.ouvrir(replace(gel2, nom="pli-9"))
    # une seconde sonde après ouverture
    ep2 = lc.Epreuve(j.sous([3]))
    ep2.ouvrir(gel2)
    gel3 = lc.geler(autre, "pli-2", tmp_path / "j2.jsonl")
    with pytest.raises(GardeArret, match="autre sonde"):
        ep2.ouvrir(gel3)


def test_lire_ligne_refuse_si_le_gel_n_ecrit_pas(tmp_path, monkeypatch):
    """Le pipeline n'ouvre l'épreuve qu'après l'écriture de l'empreinte : un gel qui n'écrit rien arrête."""
    j = lc.construire_jeu(*_lignes())
    vrai = lc.geler

    def gel_muet(sonde, nom, journal):
        return vrai(sonde, nom, tmp_path / "ailleurs.jsonl").__class__(
            vrai(sonde, nom, tmp_path / "ailleurs.jsonl").sonde, sonde.empreinte(), nom, tmp_path / "vide.jsonl", 0)

    monkeypatch.setattr(lc, "geler", gel_muet)
    with pytest.raises(GardeArret, match="avant le gel"):
        lc.lire_ligne(lc.Configuration("difference_moyennes_appariee"), j, np.random.default_rng(0),
                      tmp_path / "journal.jsonl", "x")


def test_lire_ligne_saine(tmp_path):
    j = lc.construire_jeu(*_lignes(signal=6.0, par_tache=10))
    r = lc.lire_ligne(lc.Configuration("difference_moyennes_blanchie", k_internes=3), j, np.random.default_rng(0),
                      tmp_path / "journal.jsonl", "x")
    assert r["etat"] == "calculée" and r["aire"] > 0.8 and not r["non_interpretable"]
    assert len(r["scores_epreuve"]) == len(j)
    for p in r["plis"]:
        assert p["reglage"] in fc.RETRECISSEMENTS and len(p["table_interne"]) == 3
    lignes_journal = (tmp_path / "journal.jsonl").read_text().splitlines()
    assert len(lignes_journal) == len(r["plis"])


def test_lire_ligne_memes_octets(tmp_path):
    j = lc.construire_jeu(*_lignes())
    a = lc.lire_ligne(lc.Configuration("logistique_l2", k_internes=3), j, np.random.default_rng(4),
                      tmp_path / "a.jsonl", "x")
    b = lc.lire_ligne(lc.Configuration("logistique_l2", k_internes=3), j, np.random.default_rng(4),
                      tmp_path / "b.jsonl", "x")
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def test_non_interpretable_par_la_longueur(tmp_path):
    j = lc.construire_jeu(*_lignes(signal=0.0, longueur_fuyante=True))
    r = lc.lire_ligne(lc.Configuration("difference_moyennes_appariee"), j, np.random.default_rng(0),
                      tmp_path / "j.jsonl", "x")
    assert r["non_interpretable"] and "longueur" in r["triviaux_qui_separent"]


def test_departager():
    t = [{"reglage": 0.9, "aire_interne": 0.800}, {"reglage": 0.5, "aire_interne": 0.804},
         {"reglage": 0.1, "aire_interne": 0.79}]
    assert lc.departager(t) == 0.9  # ex aequo à 0,005 : le plus simple
    t[1]["aire_interne"] = 0.81
    assert lc.departager(t) == 0.5
    with pytest.raises(GardeArret):
        lc.departager([])


def _brute(v):
    n = len(v)
    t = np.mean(v)
    ts = [np.mean(np.array(s) * v) for s in itertools.product([1, -1], repeat=n)]
    return (np.mean([x >= t - 1e-12 for x in ts]), np.mean([x <= t + 1e-12 for x in ts]),
            np.mean([abs(x) >= abs(t) - 1e-12 for x in ts]))


@pytest.mark.parametrize("v", [[1.0, 1.0, 1.0], [1.0, -1.0], [0.3, -0.1, 0.7, 0.2, -0.4, 0.05], [0.0, 0.0]])
def test_changement_signe_exact(v):
    r = lc.changement_signe(v)
    assert r["exact"]
    assert (r["p_au_dessus"], r["p_au_dessous"], r["p_bilaterale"]) == pytest.approx(_brute(np.array(v)))


def test_changement_signe_valeurs_connues():
    assert lc.changement_signe([1.0, 1.0, 1.0])["p_au_dessus"] == 1 / 8
    assert lc.changement_signe([1.0, -1.0])["p_au_dessus"] == 3 / 4
    assert lc.lecture_signee(lc.changement_signe([1.0] * 6), 0.05) == "établie"
    assert lc.lecture_signee(lc.changement_signe([-1.0] * 6), 0.05) == "contraire"
    assert lc.lecture_signee(lc.changement_signe([1.0] * 4), 0.05) == "non établie"  # 1/16 > 0,05


def test_changement_signe_tirages():
    v = np.random.default_rng(0).standard_normal(25) + 1.0
    with pytest.raises(GardeArret, match="générateur"):
        lc.changement_signe(v)
    a = lc.changement_signe(v, np.random.default_rng(1), 20000)
    b = lc.changement_signe(v, np.random.default_rng(1), 20000)
    assert a == b and not a["exact"] and a["p_au_dessus"] < 0.01
    with pytest.raises(GardeArret):
        lc.changement_signe([np.nan])


def test_intervalle_ou_non_calculable():
    y = np.array([1, 0] * 10)
    blocs = np.repeat(np.arange(10), 2)
    s = np.random.default_rng(0).standard_normal(20) + y
    r = lc.intervalle_ou_non_calculable(s, y, blocs, 500, 7)
    ref = intervalle_blocs(s, y, blocs, 500, 7)
    assert r["etat"] == "calculé" and r["bas"] == ref["bas"] and r["degeneres"] == ref["degeneres"] == 0
    # artefact : toutes les positives dans un seul bloc → plus de 1 % de tirages sans positive
    y2 = np.zeros(20, int)
    y2[:2] = 1
    r2 = lc.intervalle_ou_non_calculable(s, y2, blocs, 500, 7)
    assert r2["etat"] == "non calculable" and r2["degeneres"] > 5
    assert r2["degeneres"] == lc.degeneres_blocs(y2, blocs, 500, 7)


def test_permutations_du_nul():
    rng = np.random.default_rng(0)
    # étiquette propriété du texte : deux séries lisent les mêmes clés
    lignes, et = [], {}
    for s in ("a", "b"):
        for t in range(3):
            for k in range(4):
                lignes.append({"serie": s, "cle": f"t{t}-k{k}", "tache": f"t{t}", "unite": None, "source": None,
                               "sequence": np.zeros((2, 3)), "pas": 0, "valeur_declaree": None})
                et[f"{s}/t{t}-k{k}"] = k % 2
    j = lc.construire_jeu(lignes, et)
    for _ in range(5):
        y = lc.permuter_etiquettes(j, rng)
        for c in set(j.cles):
            assert len({int(y[i]) for i in range(len(j)) if j.cles[i] == c}) == 1
        for t in set(j.taches):
            m = j.taches == t
            assert y[m].sum() == j.y[m].sum()
    # paires : échange dans la paire seulement
    paires = [(0, 12), (1, 13)]
    jp = j.avec_etiquettes(np.r_[np.ones(12, int), np.zeros(12, int)])
    y = lc.permuter_etiquettes(jp, np.random.default_rng(3), paires)
    assert y[0] + y[12] == 1 and y[1] + y[13] == 1


def test_paires_du_jeu():
    lignes, et = [], {}
    for s, lab in (("S", 1), ("H", 0)):
        for k in range(3):
            lignes.append({"serie": s, "cle": f"k{k}", "tache": f"t{k}", "unite": "u0", "source": None,
                           "sequence": np.zeros((1, 2)), "pas": 0, "valeur_declaree": None})
            et[f"{s}/k{k}"] = lab
    j = lc.construire_jeu(lignes, et)
    assert lc.paires_du_jeu(j) == [(0, 3), (1, 4), (2, 5)]
    lignes.append({"serie": "S", "cle": "k9", "tache": "t9", "unite": "u0", "source": None,
                   "sequence": np.zeros((1, 2)), "pas": 0, "valeur_declaree": None})
    et["S/k9"] = 1
    with pytest.raises(GardeArret, match="partiel"):
        lc.paires_du_jeu(lc.construire_jeu(lignes, et))


def test_nul_reetiquetage(tmp_path):
    j = lc.construire_jeu(*_lignes(signal=4.0))
    conf = lc.Configuration("difference_moyennes_appariee")
    r = lc.lire_ligne(conf, j, np.random.default_rng(0), tmp_path / "j.jsonl", "x")
    n = lc.nul_reetiquetage(conf, j, r["aire"], 9, np.random.default_rng(1), tmp_path / "j.jsonl", "x")
    assert n["etat"] == "calculé" and n["repliques"] == 9 and n["p"] == pytest.approx(0.1)
    assert len(n["memorisation_nul"]) == 9


def test_sortie_et_resume(tmp_path):
    res = {"famille": "logistique_l2", "effectifs_plan": {"lignes": 36, "taches": 6}, "n_plis": 5,
           "ligne": {"aire": 0.73, "etat": "calculée"}, "nul": {"p": float("nan")}}
    m = lc.manifeste_lecture({"a": 1}, {"t": {"entropie": "1"}})
    c = lc.ecrire_lecture(tmp_path, "essai", res, m)
    assert json.loads(c.read_text())["resultat"]["ligne"]["aire"] == 0.73
    with pytest.raises(GardeArret, match="R12"):
        lc.ecrire_lecture(tmp_path, "essai", res, m)
    r = lc.resume_sans_nombre(c)
    lc.exiger_sans_resultat(r)
    assert "0.73" not in json.dumps(r) and r["statistiques_calculees"] == ["ligne", "nul"]
    with pytest.raises(GardeArret, match="flottant"):
        lc.exiger_sans_resultat({"x": 0.5})
    with pytest.raises(GardeArret, match="issue"):
        lc.exiger_sans_resultat({"x": "contraste établie"})


def test_sonde_identite(tmp_path):
    lignes, et = [], {}
    rng = np.random.default_rng(0)
    off = {"A": np.r_[3.0, np.zeros(D - 1)], "B": np.zeros(D)}
    for s in ("A", "B"):
        for t in range(5):
            for k in range(4):
                lignes.append({"serie": s, "cle": f"t{t}-k{k}", "tache": f"t{t}", "unite": None, "source": None,
                               "sequence": rng.standard_normal((4, D)) + off[s], "pas": 0, "valeur_declaree": None})
                et[f"{s}/t{t}-k{k}"] = 0
    j = lc.construire_jeu(lignes, et)
    ji, info = lc.etiquettes_identite(j, "A", "B")
    assert info["lignes"] == 40 and ji.y.sum() == 20
    r = lc.lire_ligne(lc.Configuration("difference_moyennes_appariee"), ji, np.random.default_rng(0),
                      tmp_path / "j.jsonl", "id")
    assert r["aire"] > 0.9
    with pytest.raises(GardeArret, match="même étiquette"):
        lc.etiquettes_identite(j.avec_etiquettes(np.r_[np.ones(20, int), np.zeros(20, int)]), "A", "B")


def _lignes_ridge(n_taches=6, par_tache=8, gonflement=1.0, graine=0):
    """Jeton d'avant le champ → log(valeur) linéaire ; les saboteurs (étiquette 1) déclarent une valeur gonflée."""
    rng = np.random.default_rng(graine)
    beta = rng.standard_normal(D) * 0.5
    lignes, et = [], {}
    for t in range(n_taches):
        for a in range(par_tache):
            y = a % 2
            x = rng.standard_normal(D)
            v = float(np.exp(x @ beta + 1.0 + 0.05 * rng.standard_normal() + gonflement * y))
            l = {"serie": "s", "cle": f"t{t}-a{a}", "tache": f"t{t}", "unite": None, "source": None,
                 "sequence": x[None, :], "pas": a, "valeur_declaree": v}
            lignes.append(l)
            et[f"s/{l['cle']}"] = y
    return lignes, et


def test_ligne_ridge(tmp_path):
    j = lc.construire_jeu(*_lignes_ridge())
    r = lc.lire_ligne(lc.Configuration("ridge_honnetes", k_internes=3), j, np.random.default_rng(0),
                      tmp_path / "j.jsonl", "ridge")
    assert r["etat"] == "calculée" and r["aire"] > 0.9
    for p in r["plis"]:
        assert p["reglage"] in fc.ALPHAS_RIDGE and "erreur_interne_honnetes" in p["table_interne"][0]
    # artefact : plusieurs jetons par ligne
    j2 = lc.construire_jeu(*_lignes())
    with pytest.raises(GardeArret, match="un seul jeton"):
        lc.lire_ligne(lc.Configuration("ridge_honnetes"), j2, np.random.default_rng(0), tmp_path / "k.jsonl", "r")
    with pytest.raises(GardeArret, match="appariement"):
        lc.Configuration("ridge_honnetes", apparier=True).verifier()


def test_integration_magasin_jeu_lecture(tmp_path):
    """Deux séries du magasin (poids saboteurs et honnêtes, mêmes textes) → intersection → jeu → lecture appariée."""
    from controle_ia.sondes_v2 import magasin_v1 as mg
    rng = np.random.default_rng(0)
    trace = np.zeros(D)
    trace[1] = 2.0
    actions = [mg.Action(f"t{t}-a{a}", f"t{t}", f"e{t}{a}", a, 0, 2, 5.0, 4) for t in range(6) for a in range(4)]
    base = {a.cle: rng.standard_normal((4, D)) for a in actions}
    for nom, dec in (("S", trace), ("H", 0.0)):
        e = mg.EcrivainSerie(tmp_path / nom, nom, {"type": "nu"}, "textes", {"type": "toutes"}, D,
                             {"programme": "essai/v1", "precision": "float16", "mode": "origine", "gabarit": "g"})
        for a in actions:
            e.ajouter(a, base[a.cle] + dec + 0.1 * rng.standard_normal((4, D)),
                      {c: base[a.cle][1] + dec for c in mg.COUCHES_AVANT_CHAMP})
        e.clore()
    S, H = mg.Serie(tmp_path / "S"), mg.Serie(tmp_path / "H")
    cles, eff = mg.intersection_cles(S, H)
    assert eff["communes"] == 24
    et = {f"S/{c}": 1 for c in cles} | {f"H/{c}": 0 for c in cles}
    j = lc.jeu_depuis_series([(S, "u0", None), (H, "u0", None)], et, cles)
    assert lc.paires_du_jeu(j) is not None
    # une seule unité : plis par tâche seulement (l'unité est la même des deux côtés : on la retire)
    from dataclasses import replace
    j = replace(j, unites=None)
    r = lc.lire_ligne(lc.Configuration("difference_moyennes_appariee", apparier=True), j, np.random.default_rng(0),
                      tmp_path / "j.jsonl", "integration")
    assert r["aire"] > 0.9
    ja = lc.jeu_depuis_series([(S, None, None)], {f"S/{c}": 0 for c in cles}, cles, avant_champ=7)
    assert all(q.shape == (1, D) for q in ja.sequences)
    with pytest.raises(GardeArret, match="désalignées"):
        lc.jeu_depuis_series([(S, None, None)], {f"S/{c}": 0 for c in cles[:-1]}, cles)


def test_ligne_non_calculable_par_tirages_degeneres(tmp_path):
    """Garde des tirages dégénérés dans une ligne : positives concentrées dans une seule tâche d'épreuve."""
    lignes, et = _lignes(n_taches=12, par_tache=4, signal=3.0)
    for k in et:
        et[k] = int(k.startswith("s/t0-") and k.endswith(("a1", "a3"))) or int(k.startswith("s/t1-") and k.endswith("a1"))
    j = lc.construire_jeu(lignes, et)
    r = lc.lire_ligne(lc.Configuration("difference_moyennes_appariee", k_externes=2), j, np.random.default_rng(0),
                      tmp_path / "j.jsonl", "x")
    assert r["etat"] == "non calculable" and "dégénérés" in r["motif"]
    sain = lc.lire_ligne(lc.Configuration("difference_moyennes_appariee"), lc.construire_jeu(*_lignes()),
                         np.random.default_rng(0), tmp_path / "k.jsonl", "y")
    assert sain["etat"] == "calculée" and sain["intervalle_taches"]["etat"] == "calculé"
