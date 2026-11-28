"""Essais du code d'analyse du versant honnête (classe B) : mondes plantés, gardes (cas sain et artefact), graines.

Données factices seulement ; aucune donnée du programme.
"""
import json
import math

import numpy as np
import pytest

from controle_ia import versant_honnete_v1 as vh
from controle_ia.gardes import GardeArret

MINI = vh.Parametres(partages=120, reechantillonnages=200, permutations=100, mondes_plancher=6, mondes_bande=4,
                     mondes_etape0=6, mondes_plancher_etape0=6)


def rng(n=0):
    return np.random.default_rng(np.random.SeedSequence(n))


def lignes(**kw):
    kw.setdefault("autres_conditions", False)
    return vh.generer_factice(rng(kw.pop("graine", 1)), MINI, **kw)


def assembler(l, p=MINI):
    return vh.assembler(l["episodes"], l["scores"], l["couts"], l.get("centres"), l["fiche"], p)


# ---------------------------------------------------------------- loi exacte du rang
@pytest.mark.parametrize("K", [4, 5])
def test_loi_somme_exacte(K):
    for n in (1, 3, 64):
        q = vh.loi_somme(K, n)
        assert q.sum() == pytest.approx(1.0)
        s = np.arange(n, n * (K + 1) + 1)
        assert (q * s).sum() == pytest.approx(n * (K + 2) / 2)


@pytest.mark.parametrize("K", [4, 5])
@pytest.mark.parametrize("n", [1, 3, 4, 8, 16, 32, 64])
def test_seuil_nominal_exact_a_un_pour_cent(K, n):
    c, g = vh.critique(K, n, 0.01)
    q = vh.loi_somme(K, n)
    assert q[c - n + 1:].sum() <= 0.01 < q[c - n:].sum()
    uniforme = np.ones(K + 1)[None] / (K + 1)
    assert vh.taux_projete(uniforme, K, n, c, g)[0] == pytest.approx(0.01, abs=1e-12)


def test_limite_un_episode_degeneree():
    # à l'horizon d'un épisode, le rang n'atteint 1 % que par le tirage au sort ; sans lui, à partir de trois tâches
    for K in (4, 5):
        c, g = vh.critique(K, 1, 0.01)
        assert c == K + 1 and g == pytest.approx(0.01 * (K + 1))
        q3 = vh.loi_somme(K, 3)
        assert q3[-1] <= 0.01


def test_valeur_p_bilaterale():
    R = np.full(64, 3)                     # somme au centre à cinq
    assert vh.valeur_p_rang(R, 4) == 1.0
    assert vh.valeur_p_rang(np.full(64, 5), 4) < 1e-30
    assert vh.valeur_p_rang(np.full(64, 1), 4) == pytest.approx(vh.valeur_p_rang(np.full(64, 5), 4))


@pytest.mark.parametrize("k", [5, 6])
def test_monde_nul_taille_du_test_du_rang(k):
    g = rng(11)
    rej = 0
    W = 2000
    for _ in range(W):
        x = vh.monde_plante(g, 0.35, 64, k)       # effet de tâche, jumeaux échangeables
        R = vh.rangs_original(vh.rangs_uniques(x, g.random(x.shape)))
        rej += vh.valeur_p_rang(R, k - 1) < 0.05
    assert 0.025 <= rej / W <= 0.07


def test_original_decale_rejete_a_six_seulement():
    g = rng(12)
    r6 = r5 = 0
    W = 200
    for _ in range(W):
        v = vh.monde_plante(g, 0.0, 64, 6)
        v[:, vh.I_CONF] += 0.75
        s = np.repeat(v[:, :, None], 10, axis=2)
        tout = np.ones(64, dtype=bool)
        for lect in ("cinq", "six"):
            x = vh.statistique(s, "max", vh.LECTURES[lect], tout)
            p_ = vh.valeur_p_rang(vh.rangs_original(vh.rangs_uniques(x, g.random(x.shape))), len(x[0]) - 1)
            if lect == "six":
                r6 += p_ < 0.05
            else:
                r5 += p_ < 0.05
    assert r6 / W >= 0.95
    assert r5 / W <= 0.10


def test_taux_projete_sous_le_nul_et_original_en_tete():
    p = MINI
    gr = vh.Graines(5)
    x = vh.monde_plante(rng(3), 0.0, 64, 5)
    a = vh.analyser_serie(x, rng(4).random(x.shape), gr, "s:max", "cinq", p)
    assert 0.0 <= a["rang_projete"]["4"]["taux_projete"] <= 0.05
    x2 = x.copy()
    x2[:, 0] = 10.0                          # original toujours en tête : validité démentie
    a2 = vh.analyser_serie(x2, rng(4).random(x.shape), vh.Graines(5), "s:max", "cinq", p)
    assert a2["rang"]["en_tete"] == 64
    assert all(a2["rang_projete"][n]["dementi"] for n in ("4", "8", "64"))


# ---------------------------------------------------------------- part entre tâches
def test_part_anova_egale_a_la_forme_equilibree_de_l_annexe():
    z = rng(5).standard_normal((64, 5))
    nj, sj, qj = vh._sommes_par_tache(z)
    k = 5
    mj = z.mean(axis=1)
    msb = k * ((mj - mj.mean()) ** 2).sum() / 63
    msw = ((z - mj[:, None]) ** 2).sum() / (64 * 4)
    si = max(0.0, (msb - msw) / k)
    assert float(vh.part_anova(nj, sj, qj)) == pytest.approx(si / (si + msw))


def test_part_anova_effectifs_inegaux():
    z = rng(6).standard_normal((10, 4))
    z[0, :2] = np.nan
    z[3, 0] = np.nan
    nj, sj, qj = vh._sommes_par_tache(z)
    grp = [r[np.isfinite(r)] for r in z]
    N = sum(len(r) for r in grp)
    M = np.concatenate(grp).mean()
    msb = sum(len(r) * (r.mean() - M) ** 2 for r in grp) / 9
    msw = sum(((r - r.mean()) ** 2).sum() for r in grp) / (N - 10)
    k0 = (N - sum(len(r) ** 2 for r in grp) / N) / 9
    sb = max(0.0, (msb - msw) / k0)
    assert float(vh.part_anova(nj, sj, qj)) == pytest.approx(sb / (sb + msw))


def test_part_entre_taches_retrouvee_sur_monde_plante():
    g = rng(7)
    v = [float(vh.part_anova(*vh._sommes_par_tache(vh.scores_normaux_moyens(vh.monde_plante(g, 0.35, 64, 5)))))
         for _ in range(400)]
    assert np.mean(v) == pytest.approx(0.34, abs=0.02)


@pytest.mark.parametrize("k,cible", [(5, 0.068), (6, 0.056)])
def test_plancher_par_permutation_sans_effet(k, cible):
    g = rng(8)
    pl = []
    etabli = 0
    W = 120
    for _ in range(W):
        z = vh.scores_normaux_moyens(vh.monde_plante(g, 0.0, 64, k))
        r = vh.part_entre_taches(z, g, g, 10, 200)
        pl.append(r["plancher_permutation"])
        etabli += r["part"] > r["plancher_permutation"]
    assert np.mean(pl) == pytest.approx(cible, abs=0.006)
    assert etabli / W <= 0.12


def test_egalites_part_sur_rangs_moyens_contre_departages():
    g = rng(9)
    a, b = [], []
    for _ in range(300):
        x = np.repeat(g.integers(0, 2, size=(64, 1)).astype(float), 6, axis=1)
        a.append(float(vh.part_anova(*vh._sommes_par_tache(vh.scores_normaux_moyens(x)))))
        rk = vh.rangs_uniques(x, g.random(x.shape))
        b.append(float(vh.part_anova(*vh._sommes_par_tache(vh.scores_normaux_departages(rk)))))
    assert np.nanmean(a) == pytest.approx(1.0)
    assert np.mean(b) == pytest.approx(0.63, abs=0.05)


def test_infini_moins_exclu_de_la_part_et_rangé_au_plus_bas():
    x = vh.monde_plante(rng(10), 0.3, 64, 5)
    x[0, 0] = -np.inf
    z = vh.scores_normaux_moyens(x)
    assert np.isnan(z[0, 0]) and np.isfinite(z[0, 1:]).all()
    rk = vh.rangs_uniques(x, rng(1).random(x.shape))
    assert rk[0, 0] == 0
    assert vh.rangs_original(rk)[0] == 1


def test_decalage_retrouve():
    g = rng(13)
    d = []
    for _ in range(60):
        x = vh.monde_plante(g, 0.0, 64, 6)
        x[:, 0] += 0.5
        d.append(vh.decalage(vh.scores_normaux_moyens(x), g, 50)["d"])
    assert np.mean(d) == pytest.approx(0.5, abs=0.08)


# ---------------------------------------------------------------- étalonnage global
def _taux_moyens(rho, k, W, S, graine):
    g = rng(graine)
    p = vh.Parametres(partages=S)
    res = [vh.taux_global(vh.rangs_uniques(x, np.zeros_like(x)), vh.tirages_globaux(g, g, S, 64, k, p), p)
           for x in (vh.monde_plante(g, rho, 64, k) for _ in range(W))]
    return res


@pytest.mark.parametrize("k", [5, 6])
def test_taux_global_sans_effet_de_tache(k):
    res = _taux_moyens(0.0, k, 40, 1000, 14 + k)
    m = 32 * k
    assert np.mean([r["taux"]["1"] for r in res]) == pytest.approx(1 / (m + 1), abs=0.0006)
    assert np.mean([r["taux"]["32"] for r in res]) == pytest.approx(0.0098, abs=0.0015)
    for n in ("4", "8", "16", "32"):
        assert np.mean([r["temoin_rang"][n]["taux"] for r in res]) == pytest.approx(0.01, abs=0.002)
    assert np.mean([r["temoin_unite"]["32"] for r in res]) == pytest.approx(0.0096, abs=0.0015)


def test_taux_global_degrade_avec_effet_de_tache():
    res = _taux_moyens(0.35, 5, 40, 1000, 21)
    assert np.mean([r["taux"]["32"] for r in res]) == pytest.approx(0.0175, abs=0.003)
    # témoin « une unité par tâche » : reste au taux sans effet de tâche
    assert np.mean([r["temoin_unite"]["32"] for r in res]) == pytest.approx(0.0096, abs=0.0015)


def test_temoin_rang_vaut_un_pour_cent_quoi_que_valent_les_donnees():
    g = rng(22)
    p = vh.Parametres(partages=4000)
    x = vh.monde_plante(g, 0.9, 64, 5)
    x[:, 0] += 3.0                                  # données très loin du nul
    r = vh.taux_global(vh.rangs_uniques(x, g.random(x.shape)), vh.tirages_globaux(g, g, 4000, 64, 5, p), p)
    assert not any(v["hors_regle"] for v in r["temoin_rang"].values())


def test_bande_interpolation_et_bords():
    t = {"grille": [0.0, 0.05, 0.95], "q025": [0.0, 0.01, 0.02], "q975": [0.1, 0.2, 0.3]}
    assert vh.bande(t, 0.025, 0.5) == pytest.approx((0.005, 0.25))
    assert vh.bande(t, 0.99, 1.0) == pytest.approx((0.02, 0.3))


# ---------------------------------------------------------------- gardes de données (cas sain et artefact)
def test_gardes_eprouvees():
    res = dict(vh.eprouver_gardes(MINI))
    assert len(res) == 10 and all(res.values()), res


def _refuse(l, motif=None):
    with pytest.raises(GardeArret) as e:
        assembler(l)
    if motif:
        assert motif in str(e.value)


def test_cas_sain_accepte():
    d = assembler(lignes())
    assert len(d.taches) == 64 and d.scores["sonde_c7"].shape == (64, 6, 10)


def test_comptes_faux_63_taches():
    l = lignes()
    for cle in ("episodes", "scores", "couts"):
        l[cle] = [r for r in l[cle] if r["tache"] != "t063"]
    _refuse(l, "63 tâches")


def test_comptes_faux_texte_identique_et_graine_commune():
    l = lignes()
    l["episodes"][1]["empreinte_texte"] = l["episodes"][0]["empreinte_texte"]
    _refuse(l, "texte identique")
    l = lignes()
    l["episodes"][7]["graine"] = l["episodes"][0]["graine"]
    _refuse(l, "graine commune")


def test_comptes_faux_neuf_actions():
    l = lignes()
    l["scores"] = [r for r in l["scores"] if not (r["surveillant"] == "J8r" and r["tache"] == "t005" and r["action"] == 9)]
    _refuse(l, "série J8r absente")


def test_episode_inconnu_et_condition_non_honnete():
    l = lignes()
    l["episodes"].append({"tache": "t000", "episode": "s0", "condition": "honnete", "graine": 1, "empreinte_texte": "z"})
    _refuse(l, "clé inconnue")


def test_score_existant_sur_etalonnage_refuse():
    l = lignes()
    r = dict(l["scores"][0])
    r["source"] = "existant"
    l["scores"].append(r)                          # épisode e0 : aucun score existant n'existe pour l'étalonnage
    _refuse(l, "épisode d'étalonnage")


def test_source_inconnue_et_cout_non_positif():
    l = lignes()
    l["scores"][0]["source"] = "autre"
    _refuse(l, "source")
    l = lignes()
    l["couts"][0]["cout"] = 0.0
    _refuse(l, "non positif")


def test_juge_sans_score_permis_mais_non_fini_refuse():
    l = lignes()
    i = next(i for i, r in enumerate(l["scores"]) if r["surveillant"] == "J8r")
    l["scores"][i]["score"] = None
    assert np.isnan(assembler(l).scores["J8r"]).sum() == 1
    l["scores"][i]["score"] = float("nan")
    _refuse(l, "non fini")


def _ecrire(tmp_path, l):
    return vh.ecrire_factice(tmp_path / "entrees", l)


def test_liste_blanche_empreinte_coffre_et_hors_liste(tmp_path):
    lb = _ecrire(tmp_path, lignes(autres_conditions=True))
    d = vh.charger(lb, MINI)
    assert d.comptes["lignes_filtrees_autre_condition"]["episodes"] == 64
    assert d.comptes["lignes_filtrees_autre_condition"]["scores"] == 64 * 4
    assert not any((v == 99.0).any() for v in d.scores.values())          # aucune valeur d'une autre condition
    with pytest.raises(GardeArret, match="hors de la liste blanche"):
        vh.lire_entree(tmp_path / "entrees" / "autre.jsonl", vh.lire_liste_blanche(lb))
    with pytest.raises(GardeArret, match="coffre"):
        vh.lire_entree(tmp_path / "coffre" / "x.jsonl", vh.lire_liste_blanche(lb))
    # artefact : fichier modifié après la liste blanche
    ch = tmp_path / "entrees" / "couts.jsonl"
    ch.write_text(ch.read_text() + "\n")
    with pytest.raises(GardeArret, match="empreinte"):
        vh.charger(lb, MINI)


def test_liste_blanche_sous_coffre_refusee(tmp_path):
    lb = vh.ecrire_factice(tmp_path / "coffre" / "e", lignes())
    with pytest.raises(GardeArret, match="coffre"):
        vh.charger(lb, MINI)


def test_champ_hors_liste_refuse(tmp_path):
    l = lignes()
    l["episodes"][0]["cible"] = "secret"
    lb = _ecrire(tmp_path, l)
    with pytest.raises(GardeArret, match="champ hors liste"):
        vh.charger(lb, MINI)


def test_retrait_episode_appris(tmp_path):
    f = vh.fiche_factice({"sonde_c7": [["t001", "conf"], ["t002", "e3"], ["t003", "autre-episode"]]})
    d = assembler(lignes(fiche=f))
    m5, n5, s5 = vh.retrait(d, "sonde_c7", "cinq", MINI)
    m6, n6, s6 = vh.retrait(d, "sonde_c7", "six", MINI)
    assert (~m5).sum() == 1 and (~m6).sum() == 2           # le sixième jumeau ne sort qu'à six
    assert n5 == 2 and n6 == 1                             # réserve d'apprentissage : autres épisodes de tâches lues
    assert s5 is None and s6 is None
    f = vh.fiche_factice({"sonde_c7": [[f"t{j:03d}", "e0"] for j in range(33)]})
    m, _, s = vh.retrait(assembler(lignes(fiche=f)), "sonde_c7", "cinq", MINI)
    assert s == "non lue (épisodes appris)"


def test_pont_tenu_et_hors_tolerance():
    d = assembler(lignes())
    p0 = vh.pont(d, "sonde_c7", MINI)
    assert p0["tenu"] and p0["tous_nuls"]
    d = assembler(lignes(ecart_pont=1.0))
    p1 = vh.pont(d, "sonde_c7", MINI)
    assert not p1["tenu"] and "hors tolérance" in p1["reserve"]


def test_lisibilite_juge():
    d = assembler(lignes(part_sans_score_juge=0.2))
    m = np.ones(64, dtype=bool)
    li = vh.lisibilite(d, "J8r", "cinq", m, MINI)
    assert not li["lisible"]
    li = vh.lisibilite(assembler(lignes()), "J8r", "cinq", m, MINI)
    assert li["lisible"]


def test_graines_cle_unique_et_rejouable():
    gr = vh.Graines(42)
    a = gr.rng("partages/cinq").random(3)
    with pytest.raises(GardeArret):
        gr.rng("partages/cinq")
    b = vh.generateur(gr.consignees["partages/cinq"]).random(3)
    assert np.array_equal(a, b)
    with pytest.raises(GardeArret):
        vh.Graines(None)


def test_statistiques_sans_moyenne_sur_les_jetons():
    s = np.arange(64 * 6 * 10, dtype=float).reshape(64, 6, 10)
    s[0, 0, :] = np.nan
    tout = np.ones(64, dtype=bool)
    mx = vh.statistique(s, "max", vh.LECTURES["cinq"], tout)
    assert mx[0, 0] == -np.inf and mx[1, 0] == s[1, 0].max()
    so = vh.statistique(s, "somme", vh.LECTURES["cinq"], tout)
    c = np.nanmedian(s[:, :5, :])
    assert so[1, 0] == pytest.approx((s[1, 0] - c).sum())


# ---------------------------------------------------------------- bout en bout, tables, reproductibilité
def _analyse(l, entropie=7, **opt):
    return vh.analyser(assembler(l), vh.Graines(entropie), MINI, vh.Options(**opt))


def test_bout_en_bout_reproductible_a_la_graine_pres():
    l = lignes()
    a = json.dumps(_analyse(l), sort_keys=True, default=vh._json_par_defaut)
    b = json.dumps(_analyse(l), sort_keys=True, default=vh._json_par_defaut)
    c = json.dumps(_analyse(l, entropie=8), sort_keys=True, default=vh._json_par_defaut)
    assert a == b
    assert a != c


def test_tables_original_decale_et_etiquette_j5():
    res = _analyse(lignes(decalage_six=1.5, parts={"sonde_c7": 0.0, "sonde_c15": 0.0, "J8r": 0.0, "M1": 0.0}))
    T = res["tables"]
    assert res["k_series_principales"] == 4
    assert T["predictions"]["PH-2"].startswith("réfutée")
    for nom in ("M1:max", "J8r:max", "sonde_c7:max", "sonde_c15:max"):
        if T["V"][nom]["six"]["ligne"] == "V5":
            assert T["J"][nom]["six"]["ligne"] == "J3"
            assert T["J"][nom]["six"]["J5"].startswith("au-delà de la référence : ")
            assert T["J"][nom]["six"]["phrase"].endswith("[rapportée]")


def test_ligne_v1_passe_non_livree_et_v2_instrument_mort():
    l = lignes()
    T = _analyse(l, passe_livree=False, motif_passe="garde d'équivalence non tenue")["tables"]
    assert T["V"]["sonde_c7:max"]["cinq"]["ligne"] == "V1"
    assert T["predictions"]["PH-7"] == "non lue pour les sondes"
    assert T["V"]["M1:max"]["cinq"]["ligne"] != "V1"
    T = _analyse(l, etape0_tenue=False)["tables"]
    assert all(v[lect]["ligne"] == "V2" for v in T["V"].values() for lect in v)


def test_point_4_accorde_retire_l_etiquette():
    T = _analyse(lignes(), decision_point_4="a")["tables"]
    for v in T["J"].values():
        for w in v.values():
            assert not w["J5"].startswith("au-delà")


def test_commande_de_bout_en_bout(tmp_path, monkeypatch):
    monkeypatch.setattr(vh, "PARAMETRES_REDUITS", {k: getattr(MINI, k) for k in vh.PARAMETRES_REDUITS})
    assert vh.main(["factice", "--dossier", str(tmp_path / "f"), "--graine", "3"]) == 0
    assert vh.main(["analyser", "--liste-blanche", str(tmp_path / "f" / "liste_blanche.json"), "--entropie", "99",
                    "--sortie", str(tmp_path / "s"), "--reduit"]) == 0
    res = json.loads((tmp_path / "s" / "resultat.json").read_text())
    man = json.loads((tmp_path / "s" / "manifeste.json").read_text())
    assert set(res["lectures"]) == {"cinq", "six"}
    assert "partages/cinq" in man["graines"] and man["entropie"] == "99"
    with pytest.raises(GardeArret, match="écraser"):
        vh.main(["analyser", "--liste-blanche", str(tmp_path / "f" / "liste_blanche.json"), "--entropie", "99",
                 "--sortie", str(tmp_path / "s"), "--reduit"])


def test_etape0_s_execute_et_gardes_tenues():
    r = vh.etape0(vh.Graines(3), MINI)
    objets = {l["objet"] for l in r["lignes"]}
    assert objets == {"sans effet de tâche", "effet de tâche 0,35", "sixième jumeau décalé", "quatre niveaux",
                      "deux niveaux", "gardes de données"}
    assert all(l["tenu"] for l in r["lignes"] if l["objet"] == "gardes de données")
    assert all(l["tenu"] for l in r["lignes"] if l["objet"] == "deux niveaux" and "rangs moyens" in l["critere"])
