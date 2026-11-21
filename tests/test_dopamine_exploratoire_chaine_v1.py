"""La chaîne entière sur le modèle jouet (processeur) : étape 1 (tranche, génération, extraction, noyau, blocs sous
l'horloge, relecture forcée), coupure et reprise ; étape 2a ; gardes de la tranche, de la génération, de l'horloge et de
la vérité plantée (exploratoire)."""
import json
import subprocess

import numpy as np
import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")

from controle_ia.dopamine_exploratoire import course_v1, generation_v1, jouet_v1, math500_v1, sonde_v1  # noqa: E402
from controle_ia.dopamine_exploratoire.stockage_v1 import ecrire_jsonl  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import lire_manifeste, verifier_resultat  # noqa: E402

RJ = dict(generation_v1.RECETTE_TABLEAU_6, max_jetons=12)
RS = dict(sonde_v1.RECETTE_TABLEAU_7, epoques=10, cachee=8)
RUN1 = "20261121-120000-dopamine-exploratoire-jouet-etape-1"
RUN2A = "20261121-120100-dopamine-exploratoire-jouet-etape-2a"
ENTETE = "<|im_start|>assistant\n"
TRANCHE_LIBRE = {"questions": 32, "plafond_max": 99, "longueur_moyenne_max": 1e9, "reussite_min": 0.0,
                 "reussite_max": 1.0}
GEN_LIBRE = {"part_plafond_max": 1.0, "part_sans_boite_max": 1.0}


@pytest.fixture
def depot(tmp_path):
    d = tmp_path / "depot"
    d.mkdir()
    for c in (["init", "-q"], ["config", "user.email", "e@invalid"], ["config", "user.name", "essai"]):
        subprocess.run(["git", "-C", str(d), *c], check=True)
    (d / "LISEZ-MOI").write_text("essai\n")
    subprocess.run(["git", "-C", str(d), "add", "."], check=True)
    subprocess.run(["git", "-C", str(d), "commit", "-q", "-m", "init"], check=True)
    return d


class Compteur:
    def __init__(self, g):
        self.g, self.appels, self.nom = g, 0, g.nom

    def generer(self, inv, gr):
        self.appels += 1
        return self.g.generer(inv, gr)


def _config1(**k):
    base = dict(modele="jouet", jeu={"nom": "jouet", "sha256": "0" * 64}, generateur_nom="transformers", jouet=True,
                invite="litteral", entete=ENTETE, recette_generation=RJ, recette_sonde=RS, taux=(0.0, 0.9),
                decoupage={"mode": "plis", "plis": 2}, graines_supplementaires=1, borne_basse_plantee=0.0,
                tranche=TRANCHE_LIBRE, seuils_generation=GEN_LIBRE, taille_lot=16)
    base.update(k)
    return course_v1.config_etape1(**base)


def _contextes(depot, d, n=4):
    eps = []
    for i in range(n):
        en = d.encoder(math500_v1.invite(f"{i}+{i}", "litteral"))
        ids, pos, txt = list(en), [len(en) - 1], []
        for a in ("12", "\\boxed{1}"):
            ids += d.encoder(a)
            pos.append(len(ids) - 1)
            txt.append(a)
            ids += d.encoder("\n")
        eps.append({"id": f"ep-{i}", "famille": f"f{i % 2}", "etiquette": "honnete", "recompense": i % 2, "ids": ids,
                    "ids_enonce": en, "positions": pos, "textes_actions": txt})
    f = depot / "contextes.jsonl"
    ecrire_jsonl(f, eps)
    return f, {e["id"] for e in eps}


def test_etape1_de_bout_en_bout_coupure_reprise_et_blocs(depot, monkeypatch):
    modele, dec = jouet_v1.modele_jouet(0)
    qs = jouet_v1.questions_jouets(64)
    ctx, liste = _contextes(depot, dec)
    config = _config1()
    chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, RUN1, config, entropie=2026, autoriser_depot_sale=True)
    gen = Compteur(generation_v1.GenerateurTransformers(modele, dec, RJ, math500_v1.ARRETS_QWEN_BOXED, jouet=True))
    st = course_v1.etape_generer(depot, RUN1, config, chemin_m, m, qs, dec, gen)
    assert st["questions"] == 64 and gen.appels == 2          # tranche (2 lots), puis le reste (2 lots) en un appel
    tranche = verifier_resultat(depot, depot / "diag" / RUN1 / "etape1-tranche-exploratoire.json")["resultat"]
    assert tranche["stats"]["questions"] == 32 and tranche["arret"] == [] and tranche["projection_fin_noyau_s"] > 0
    assert (depot / "donnees" / RUN1 / "invite-question-0.txt").read_text().endswith(ENTETE)

    # coupure au milieu du noyau : la quatrième sonde lève
    vraie, appels = sonde_v1.entrainer, {"n": 0}

    def coupee(*a, **k):
        appels["n"] += 1
        if appels["n"] == 4:
            raise KeyboardInterrupt("coupure simulée")
        return vraie(*a, **k)
    monkeypatch.setattr(sonde_v1, "entrainer", coupee)
    with pytest.raises(KeyboardInterrupt):
        course_v1.etape_suite(depot, RUN1, config, chemin_m, m, qs, modele, "cpu", None, dec, ctx, liste)
    monkeypatch.setattr(sonde_v1, "entrainer", vraie)

    # reprise : même manifeste ; rien de régénéré ; les trois sondes scellées relues
    chemin_m2, m2 = course_v1.ouvrir_ou_reprendre(depot, RUN1, config)
    assert m2["graines"] == m["graines"]
    course_v1.etape_generer(depot, RUN1, config, chemin_m2, m2, qs, dec, gen)
    assert gen.appels == 2
    compte = {"n": 0}

    def comptee(*a, **k):
        compte["n"] += 1
        return vraie(*a, **k)
    monkeypatch.setattr(sonde_v1, "entrainer", comptee)
    fin = course_v1.etape_suite(depot, RUN1, config, chemin_m2, m2, qs, modele, "cpu", None, dec, ctx, liste)
    # noyau : 2 (plantée) + 6 (couches 2 à 4) + 2 (permutées) − 3 scellées ; blocs : 6 + 6 + 6 + 6 + 4
    assert compte["n"] == (2 + 6 + 2 - 3) + 6 + 6 + 6 + 6 + 4

    res_fin = verifier_resultat(depot, fin)["resultat"]
    assert res_fin["mode"] == "exploratoire" and res_fin["blocs_faits"] == list(course_v1.BLOCS)
    man, _ = lire_manifeste(chemin_m)
    assert man["config"]["mode"] == "exploratoire" and man["config"]["go_course"] == "GO-2026-11-21-48"
    noy = verifier_resultat(depot, depot / "diag" / RUN1 / "etape1-noyau-exploratoire.json")["resultat"]
    assert noy["questions"] == 64 and 0 < noy["reussites"] < 64
    assert len(noy["principal"][0]["plis"]) == 2 and sum(p["validation"] for p in noy["principal"][0]["plis"]) == 64
    assert set(noy["principal"][0]["mis_en_commun"]["aires"]) == {"2", "3", "4"}
    assert 0 <= noy["comparateurs_sans_critere"]["confiance_jeton"]["aire"] <= 1
    assert noy["verite_plantee"]["force"] == 4.0
    poids = sorted((depot / "donnees" / RUN1 / "sondes" / "poids").glob("*.npz"))
    assert len(poids) == 10 and np.load(poids[0])["0_weight"].dtype == np.float16
    em = verifier_resultat(depot, depot / "diag" / RUN1 / "etape1-bloc-validation-emboitee-exploratoire.json")
    assert len(em["resultat"]["plis"]) == 2
    cp = verifier_resultat(depot, depot / "diag" / RUN1 / "etape1-bloc-couches-programme-exploratoire.json")
    assert set(cp["resultat"]["aires_par_couche_mise_en_commun"]) == {"7", "15", "23"}
    rl = verifier_resultat(depot, depot / "diag" / RUN1 / "etape1-bloc-relecture-forcee-exploratoire.json")
    assert rl["resultat"]["episodes"] == 4 and rl["resultat"]["couches"] == [7, 15, 23]
    assert (depot / "donnees" / RUN1 / "relecture-forcee" / "couche-23.npy").exists()
    s0 = np.load(depot / "donnees" / RUN1 / "etats-s0" / "couche-03.npy")
    assert s0.shape == (64, 16) and s0.dtype == np.float16


def test_horloge_sain_et_artefact():
    h = course_v1.Horloge(1000.0, maintenant=lambda: 900.0)
    assert h.peut_lancer("bloc") and not h.peut_lancer("bloc", duree_prevue_s=200)
    h2 = course_v1.Horloge(1000.0, maintenant=lambda: 1001.0)
    assert not h2.peut_lancer("bloc")
    with pytest.raises(GardeArret, match="horloge"):
        h2.exiger("bloc")
    with pytest.raises(GardeArret):
        course_v1.Horloge(-5)


def test_blocs_non_lances_apres_l_arret_des_lancements(depot, monkeypatch):
    modele, dec = jouet_v1.modele_jouet(0)
    qs = jouet_v1.questions_jouets(64)
    config = _config1(blocs=("graines_supplementaires", "relecture_forcee"))
    chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, RUN1, config, entropie=1, autoriser_depot_sale=True)
    gen = generation_v1.GenerateurTransformers(modele, dec, RJ, math500_v1.ARRETS_QWEN_BOXED, jouet=True)
    course_v1.etape_generer(depot, RUN1, config, chemin_m, m, qs, dec, gen)
    t = {"v": 0.0}
    h = course_v1.Horloge(1e12, maintenant=lambda: t["v"])
    vraie = course_v1.noyau

    def noyau_puis_horloge_passee(*a, **k):
        r = vraie(*a, **k)
        t["v"] = 2e12                                # l'arrêt des lancements tombe pendant le noyau
        return r
    monkeypatch.setattr(course_v1, "noyau", noyau_puis_horloge_passee)
    ctx, liste = _contextes(depot, dec)
    fin = course_v1.etape_suite(depot, RUN1, config, chemin_m, m, qs, modele, "cpu", h, dec, ctx, liste)
    res = verifier_resultat(depot, fin)["resultat"]
    assert res["blocs_faits"] == []
    assert [b["bloc"] for b in res["blocs_non_faits"]] == ["graines_supplementaires", "relecture_forcee"]
    assert all("horloge" in b["motif"] for b in res["blocs_non_faits"])


def test_regle_de_la_tranche_arrete(depot):
    modele, dec = jouet_v1.modele_jouet(0)
    qs = jouet_v1.questions_jouets(48)
    config = _config1(tranche=dict(TRANCHE_LIBRE, reussite_min=0.99))
    chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, RUN1, config, entropie=1, autoriser_depot_sale=True)
    gen = Compteur(generation_v1.GenerateurTransformers(modele, dec, RJ, math500_v1.ARRETS_QWEN_BOXED, jouet=True))
    with pytest.raises(GardeArret, match="tranche de mesure"):
        course_v1.etape_generer(depot, RUN1, config, chemin_m, m, qs, dec, gen)
    assert gen.appels == 1                            # seule la tranche a tourné
    d = verifier_resultat(depot, depot / "diag" / RUN1 / "etape1-tranche-exploratoire.json")["resultat"]
    assert d["arret"] and "réussite" in d["arret"][0]
    assert course_v1.regle_tranche({"questions": 32, "au_plafond": 4, "longueur_moyenne": 100, "reussites": 16},
                                   course_v1.TRANCHE, None, None) == ["4 réponses au plafond (≥ 4)"]
    assert course_v1.regle_tranche({"questions": 32, "au_plafond": 3, "longueur_moyenne": 100, "reussites": 16},
                                   course_v1.TRANCHE, 2000.0, 1000.0) == ["fin du noyau projetée au-delà de l'arrêt "
                                                                           "des lancements"]
    assert course_v1.regle_tranche({"questions": 32, "au_plafond": 3, "longueur_moyenne": 2400, "reussites": 16},
                                   course_v1.TRANCHE, 900.0, 1000.0) == []


def test_seuils_de_generation_arretent_avant_extraction(depot):
    modele, dec = jouet_v1.modele_jouet(0)
    qs = jouet_v1.questions_jouets(32)
    config = _config1(seuils_generation={"part_plafond_max": 1.0, "part_sans_boite_max": 0.0})
    chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, RUN1, config, entropie=1, autoriser_depot_sale=True)
    gen = generation_v1.GenerateurTransformers(modele, dec, RJ, math500_v1.ARRETS_QWEN_BOXED, jouet=True)
    with pytest.raises(GardeArret, match="sans boîte"):
        course_v1.etape_generer(depot, RUN1, config, chemin_m, m, qs, dec, gen)


def test_garde_d_invite_dans_la_course(depot):
    modele, dec = jouet_v1.modele_jouet(0)
    config = _config1(entete="<|start_header_id|>assistant<|end_header_id|>\n\n")      # en-tête d'un autre gabarit
    chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, RUN1, config, entropie=1, autoriser_depot_sale=True)
    gen = generation_v1.GenerateurTransformers(modele, dec, RJ, (), jouet=True)
    with pytest.raises(GardeArret, match="en-tête"):
        course_v1.etape_generer(depot, RUN1, config, chemin_m, m, jouet_v1.questions_jouets(32), dec, gen)


def _etats_jouets(n, rng):
    return [rng.standard_normal((int(rng.integers(3, 9)), 16)).astype(np.float16) * np.float16(8) for _ in range(n)]


def test_verite_plantee_lue_par_la_chaine_et_garde_d_arret(depot):
    """Objet vrai : issue injectée à force 4 dans tous les états, sonde à la recette du tableau 7 (assez de pas) : borne
    basse ≥ 0,9. Objet faux : force 0 (rien d'injecté) : la garde arrête le noyau."""
    rng = np.random.default_rng(11)
    seqs = {3: _etats_jouets(96, rng)}
    r = np.array([0, 1] * 48)
    cfg = _config1(recette_sonde=dict(sonde_v1.RECETTE_TABLEAU_7, epoques=1000, cachee=8), borne_basse_plantee=0.9,
                   decoupage={"mode": "plis", "plis": 2}, taux=(0.0,))
    chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, RUN1, cfg, entropie=5, autoriser_depot_sale=True)
    d = course_v1.dossier_course(depot, RUN1)
    p = course_v1.controle_plante(cfg, m, chemin_m, depot, seqs, r, d, "cpu")
    assert p["intervalle_95"][0] >= 0.9, p["intervalle_95"]
    cfg0 = _config1(recette_sonde=dict(sonde_v1.RECETTE_TABLEAU_7, epoques=5, cachee=8), borne_basse_plantee=0.9,
                    decoupage={"mode": "plis", "plis": 2}, taux=(0.0,), force_verite_plantee=0.0)
    run0 = RUN1.replace("120000", "120001")
    chemin0, m0 = course_v1.ouvrir_ou_reprendre(depot, run0, cfg0, entropie=5, autoriser_depot_sale=True)
    with pytest.raises(GardeArret, match="chaîne est fausse"):
        course_v1.controle_plante(cfg0, m0, chemin0, depot, seqs, r, course_v1.dossier_course(depot, run0), "cpu")
    assert (depot / "diag" / run0 / "etape1-noyau-arret-exploratoire.json").exists()


def test_reprise_refusee_si_la_configuration_change(depot):
    course_v1.ouvrir_ou_reprendre(depot, RUN1, _config1(), entropie=1)
    with pytest.raises(GardeArret, match="autre configuration"):
        course_v1.ouvrir_ou_reprendre(depot, RUN1, _config1(graines_supplementaires=2))


def test_refus_sans_marque_exploratoire_ou_hors_plis(depot):
    with pytest.raises(GardeArret, match="exploratoire"):
        course_v1.ouvrir_ou_reprendre(depot, "20261121-120000-dopamine-jouet", _config1(), entropie=1)
    c = _config1()
    c["mode"] = "decisif"
    with pytest.raises(GardeArret, match="mode"):
        course_v1.ouvrir_ou_reprendre(depot, RUN1, c, entropie=1)
    with pytest.raises(GardeArret, match="plis"):
        _config1(decoupage={"mode": "part"})
    with pytest.raises(GardeArret, match="bloc"):
        _config1(blocs=("autre",))


def test_etape2a_de_bout_en_bout(depot):
    modele, dec = jouet_v1.modele_jouet(1)
    qs = jouet_v1.questions_jouets(60, graine=3, familles=10)
    gen = generation_v1.GenerateurTransformers(modele, dec, RJ, math500_v1.ARRETS_QWEN_BOXED, jouet=True)
    inv = [dec.encoder(math500_v1.invite(q["probleme"], "litteral")) for q in qs]
    sorties = gen.generer(inv, list(range(len(qs))))
    episodes = [{"id": q["id"], "famille": q["famille"], "jetons_invite": i, "jetons_reponse": s["jetons"],
                 "recompense": math500_v1.noter(s["texte"], q["reponse_attendue"])["recompense"]}
                for q, i, s in zip(qs, inv, sorties)]
    config = course_v1.config_etape2a(modele="jouet", episodes={"chemin": "jouet", "sha256": "0" * 64}, jouet=True,
                                      recette_sonde=dict(RS, epoques=20), plis_familles=5)
    chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, RUN2A, config, entropie=7)
    diag = course_v1.executer_etape2a(depot, RUN2A, config, chemin_m, m, episodes, modele, "cpu")
    res = verifier_resultat(depot, diag)["resultat"]
    assert res["mode"] == "exploratoire" and res["familles"] == 10 and set(res["couches"]) == {"7", "15", "23"}
    for c in res["couches"].values():
        assert -1 <= c["correlation_pas_suivant"]["rho"] <= 1 and c["taille_effective_pas"] > 0
        a = c["alerte_par_famille"]
        assert a["familles"] == 10 and 1 <= a["taille_effective"] <= 60 and abs(a["taux_alerte"] - 0.2) < 0.1
        assert 0 <= c["taux_alerte_entre_lots"]["taux_b"] <= 1
    idx = json.loads((depot / "donnees" / RUN2A / "etats" / "couche-23" / "lot-00000.index.json").read_text())
    assert idx["couche"] == 23
    assert not (depot / "donnees" / RUN2A / "etats" / "couche-02").exists()     # couches 2 à 4 jamais sur des épisodes


def test_plis_par_famille_disjoints():
    fam = np.repeat([f"f{i}" for i in range(6)], 3)
    plis = course_v1.plis_par_famille(fam, 3, 0)
    for app, val in plis:
        assert set(fam[app]).isdisjoint(fam[val])
    assert sorted(np.concatenate([v for _, v in plis]).tolist()) == list(range(18))
    with pytest.raises(GardeArret):
        course_v1.plis_par_famille(fam, 7, 0)


def test_config_2a_refuse_un_score_inconnu():
    with pytest.raises(GardeArret):
        course_v1.config_etape2a(modele="jouet", episodes={}, score="autre")


def test_generation_groupee_rend_les_memes_lots(depot):
    """Huit lots par appel ou un seul : mêmes lots, mêmes réponses (graine par question) ; reprise d'un groupe coupé."""
    modele, dec = jouet_v1.modele_jouet(0)
    qs = jouet_v1.questions_jouets(80)
    sorties = {}
    for k, lpa in ((0, 1), (1, 8)):
        run = RUN1.replace("120000", f"12010{k}")
        config = _config1(lots_par_appel=lpa)
        chemin_m, m = course_v1.ouvrir_ou_reprendre(depot, run, config, entropie=3, autoriser_depot_sale=True)
        gen = Compteur(generation_v1.GenerateurTransformers(modele, dec, RJ, math500_v1.ARRETS_QWEN_BOXED, jouet=True))
        course_v1.etape_generer(depot, run, config, chemin_m, m, qs, dec, gen)
        assert gen.appels == (1 + 3 if lpa == 1 else 1 + 1)
        d = course_v1.dossier_course(depot, run) / "generations"
        sorties[lpa] = {f.name: [(x["id"], x["jetons_reponse"]) for x in
                                 (json.loads(l) for l in f.read_text().splitlines())]
                        for f in sorted(d.glob("lot-*.jsonl"))}
    assert sorties[1] == sorties[8] and len(sorties[8]) == 5
    with pytest.raises(GardeArret, match="lots par appel"):
        course_v1._generer_groupes([], {}, dec, None, depot, None, 0)
