"""Essais de la couche mécanique (B2) : le lecteur ne compose rien dans une course source et l'ensemble exclu d'un générateur
sain y est vide ; garde 13 (générateur et copies) ; gardes 23 et 24 (S8) ; garde 27 (bras de diagnostic) ; le multiplicateur de
la tenue ne s'applique pas aux entrées étrangères du bras 4b ; huit fréquences et strate vide ; reproductibilité à l'octet d'une
source. Graines de la couche « essai ». Code v3 : copie servie au bras 4b contrôlée (C2) ; strate du passage exigée comme
`strates_requises` l'exige (C3) ; compteurs du jeu à sources étrangères (note D7)."""

import os

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, graines, prop
from controle_ia.heritage_etage_processeur_v1 import equivalence as EQ
from controle_ia.heritage_etage_processeur_v1 import executeur as EX
from controle_ia.heritage_etage_processeur_v1 import frequences as FR
from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
from controle_ia.heritage_etage_processeur_v1 import mondes as MO
from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
from controle_ia.heritage_etage_processeur_v1 import registre as R
from controle_ia.heritage_etage_processeur_v1 import statistique as ST
from controle_ia.heritage_etage_processeur_v1.constantes import CLES_FREQUENCES, REGLAGES_ETAPE_4

LECTEUR = dict(K=REGLAGES_ETAPE_4["K"])


def _jouer(g, dossier, nom, dose, source, famille, bras=("1", "2", "3"), **kw):
    p = prop(nom, **(LECTEUR if nom.startswith("lecteur") else {}))
    ctx = MC.ContexteSource(g, dict(couche="essai", famille=famille, proposeur=nom, dose=dose, source=source), p, dose, 0.25,
                            os.path.join(dossier, f"{famille}-{nom}-{dose}-{source}"), **kw)
    return MC.jouer_source(ctx, bras), ctx


@pytest.fixture(scope="module")
def couches(tmp_path_factory):
    """Lecteur réglé pour l'héritage à la dose 0,5 : douze sources pour les fréquences, vingt-quatre sources rejouées sous
    d'autres graines pour les moyennes (comme les étapes 4 et 6 bis), puis la couche statistique sur 20 000 sources."""
    g = graines()
    d = str(tmp_path_factory.mktemp("mecanique"))
    freqs = MC.Frequences()
    premiere = None
    for s in range(12):
        out, _ = _jouer(g, d, "lecteur-heritage", 0.5, s, "frequences")
        freqs.fusionner(out["frequences"])
        premiere = premiere or out
    f = FR.frequences_gelees(freqs.comptes())
    m1 = {b: [] for b in "123"}
    for s in range(24):
        out, _ = _jouer(g, d, "lecteur-heritage", 0.5, s, "reprise")
        for b in "123":
            m1[b].append(out["bras"][b]["mesure"]["M1"])
    return {"f": f, "comptes": freqs.comptes(), "m1": m1, "premiere": premiere, "g": g, "dossier": d}


def _stat(g, f, nom, dose, S, famille):
    p = prop(nom, **(LECTEUR if nom.startswith("lecteur") else {}))
    res = ST.simuler({b: g.g(couche="essai", famille=famille, bras=b, role="echantillonnage") for b in "123"},
                     g.g(couche="essai", famille=famille, role="monde"), g.g(couche="essai", famille=famille, role="source"),
                     p, dose, 0.25, f, S)
    return {b: res["bras"][b]["M1"] for b in "123"}


def test_course_source_sans_composition_et_ensemble_exclu_vide(tmp_path):
    out, _ = _jouer(graines(), str(tmp_path), "lecteur-heritage", 0.5, 0, "course-source")
    assert out["exclu"] == []
    source = out["suite"].source.nom
    assert not any(cle[1] == source for cle in out["frequences"].criblage)  # aucune composition criblée dans la course source
    assert all(e["provenance"]["origine"] == "course-source" for e in out["registre_source"].entrees)
    # le lecteur, servi d'entrées de sa propre course, n'y compose rien
    m = out["suite"].source
    vue = out["registre_source"].vue("entiere")
    parts = P.PartsServies({dd["nom"]: m.part_servie(dd["nom"]) for dd in m.domaines})
    t = P.proposer(prop("lecteur-heritage", K=256), vue, m, parts, 40, np.random.default_rng(1), 0, "source")
    assert all(o == "base" for _, _, o in t)
    # le même lecteur, au bras 3, compose les entrées héritées
    t3 = P.proposer(prop("lecteur-heritage", K=256), vue, out["suite"].cibles[0], P.PartsServies(
        {dd["nom"]: out["suite"].cibles[0].part_servie(dd["nom"]) for dd in out["suite"].cibles[0].domaines}),
        40, np.random.default_rng(1), 0, "3")
    assert any(o == "composition" for _, _, o in t3)


def test_huit_frequences_et_garde_24_cas_sain(couches):
    f = couches["f"]
    assert sorted(f) == sorted(CLES_FREQUENCES)
    assert f["p_tient_non_plantee_copie"] is None  # aucun copieur joué : strate vide
    assert FR.verifier_s8_i(f)
    r = FR.rapport(couches["comptes"])
    for s in ("vraie-source", "vraie-cible", "fausse", "non-plantee-base", "non-plantee-composition", "non-plantee",
              "vraie-dependante", "vraie-independante"):
        assert r[s]["lois"] > 0 and r[s]["intervalle"] is not None


def test_garde_24_executeur_qui_rend_tient_a_toute_loi(tmp_path):
    g = graines()
    out, _ = _jouer(g, str(tmp_path), "sourd-paie", 0.25, 0, "garde-24", executeur=EX.Executeur(toujours_tient=True))
    f = FR.frequences_gelees(out["frequences"].comptes())
    assert f["p_tient_fausse"] == 1.0
    with pytest.raises(FR.ArretFrequences):
        FR.verifier_s8_i(f)


def test_strate_vide_dont_la_couche_statistique_a_besoin_arrete():
    f = dict(FREQUENCES_D_ESSAI, p_tient_non_plantee_copie=None)
    g = graines()
    _stat(g, f, "lecteur-heritage", 0.5, 200, "strate-ok")  # le lecteur n'a pas besoin de la strate « copie »
    with pytest.raises(FR.ArretFrequences):
        _stat(g, f, "copieur", 0.5, 200, "strate-vide")
    sans_composition = dict(f, p_tient_non_plantee_composition=None)
    with pytest.raises(FR.ArretFrequences):
        _stat(g, sans_composition, "lecteur-heritage", 0.5, 200, "strate-vide-2")
    _stat(g, sans_composition, "sourd-paie", 0.5, 200, "strate-ok-2")
    with pytest.raises(FR.ArretFrequences):
        FR.exiger_strates({k: v for k, v in f.items() if k != "p_faux_passage"}, prop("sourd-paie"), 0.5, ("1", "2", "3"))


def test_passage_vraie_exige_seulement_quand_les_strates_requises_l_exigent():
    """Code v3, C3 : `statistique.Mondes` n'exige `p_passage_vraie` que si `frequences.strates_requises` l'exige (un lecteur
    aux bras 3 ou 4a, à dose non nulle) ; ailleurs la strate vide ne bloque rien et ne change aucun nombre ; employée sans
    avoir été tirée, elle arrête."""
    g = graines()
    sans_passage = dict(FREQUENCES_D_ESSAI, p_passage_vraie=None)
    assert "p_passage_vraie" not in FR.strates_requises(prop("sourd-paie"), 0.5, ("1", "2", "3"))
    a = _stat(g, sans_passage, "sourd-paie", 0.5, 200, "passage-non-requis")
    b = _stat(g, FREQUENCES_D_ESSAI, "sourd-paie", 0.5, 200, "passage-non-requis")
    assert all(np.array_equal(a[x], b[x]) for x in "123")
    lecteur = prop("lecteur-heritage", **LECTEUR)
    assert "p_passage_vraie" in FR.strates_requises(lecteur, 0.5, ("1", "2", "3"))
    with pytest.raises(FR.ArretFrequences):
        _stat(g, sans_passage, "lecteur-heritage", 0.5, 200, "passage-requis")
    m = ST.Mondes(g.g(couche="essai", famille="passage-non-tire", role="monde"), 50, 0.5, sans_passage, False)
    assert all(p is None for p in m.passage)
    src = ST.course_source(g.g(couche="essai", famille="passage-non-tire", role="source"), lecteur, m, sans_passage, 0.25)
    with pytest.raises(FR.ArretFrequences, match="non tirés"):
        ST.jouer_bras(g.g(couche="essai", famille="passage-non-tire", bras="3", role="echantillonnage"), lecteur, m,
                      sans_passage, 0.25, "3", src)


def test_garde_23_equivalence_s8_ii(couches):
    g, f = couches["g"], couches["f"]
    rng = g.g(couche="essai", famille="garde-23", role="intervalle")
    sain = _stat(g, f, "lecteur-heritage", 0.5, 20000, "garde-23-sain")
    moy = {("lecteur-heritage", b, 0.5): (float(np.mean(couches["m1"][b])), 24) for b in "123"}
    detail = EQ.garde_equivalence(moy, {("lecteur-heritage", b, 0.5): sain[b] for b in "123"}, rng)
    assert all(v["intervalle"][0] <= v["moyenne_mecanique"] <= v["intervalle"][1] for v in detail.values())
    decale = dict(f, p_tient_vraie_source=f["p_tient_vraie_source"] / 2.0)
    fautif = _stat(g, decale, "lecteur-heritage", 0.5, 20000, "garde-23-fautif")
    sort, _, _ = EQ.decalage_sort_de_l_intervalle(sain["3"], fautif["3"], 24, rng)
    assert sort, "le décalage planté ne sort pas de l'intervalle à 24 sources : l'artefact ne dit rien"
    with pytest.raises(EQ.ArretEquivalence):
        EQ.garde_equivalence({("lecteur-heritage", "3", 0.5): moy[("lecteur-heritage", "3", 0.5)]},
                             {("lecteur-heritage", "3", 0.5): fautif["3"]}, rng)


def test_garde_13_generateur_et_copies(tmp_path):
    g = graines()
    sain, _ = _jouer(g, str(tmp_path), "copieur", 0.5, 0, "garde-13")
    assert sain["exclu"] == []
    # aucune loi appariée par une copie : aux bras 2 et 3, toutes les tentatives de la génération finale sont des copies
    assert sain["bras"]["3"]["mesure"]["M1"] == 0 and sain["bras"]["2"]["mesure"]["M1"] == 0
    assert sain["bras"]["1"]["mesure"]["M1"] > 0  # sans registre, la recherche de base retrouve des lois
    # générateur fautif planté : les lois vraies de la source recopiées dans les domaines indépendants du monde final (une
    # seule ne suffit pas à rendre l'artefact sûr : la course source peut ne pas l'avoir engagée)
    fautif, _ = _jouer(g, str(tmp_path), "copieur", 0.5, 0, "garde-13-fautif", faute="lois-de-la-source-recopiees")
    textes_source = {l["texte"] for l in fautif["suite"].source.lois.values() if l["type"] == "vraie"}
    engagees_a_la_source = {MC.json_canonique(MC.loi_du_texte(e["tentative"]["engagement"]["test_de_mort"]["test"]))
                            for e in fautif["registre_source"].entrees}
    attendu = sorted(i for i, l in fautif["suite"].finale.lois.items() if l["texte"] in textes_source & engagees_a_la_source)
    assert attendu and fautif["exclu"] == attendu
    for b in "123":  # les lois recopiées ne comptent pour aucun bras
        assert not set(attendu) & set(fautif["bras"][b]["mesure"]["appariees"])
    assert any(fautif["bras"][b]["mesure"]["exclues_appariees"] for b in "123")


def test_garde_27_bras_de_diagnostic_et_tenue_sans_effet_au_bras_4b(tmp_path):
    g = graines()
    bases = [dict(couche="essai", famille="garde-27", proposeur="lecteur-tenue", dose=0.25, source=k) for k in range(2)]
    suites = MO.generer_jeu_avec_etrangeres(g, bases, 0.25)
    assert suites[0].etrangere is suites[1].source and suites[1].etrangere is suites[0].source
    premieres, secondes = MC.jouer_jeu_diagnostic(g, bases, prop("lecteur-tenue", tau=2.0), 0.25, 0.25, str(tmp_path), suites)
    for k in range(2):
        e = premieres[(k + 1) % 2]
        r4a = secondes[k]["bras"]["4a"]["registre"]
        assert r4a.entrees[:len(e["registre_source"].entrees)] == e["registre_source"].entrees
        assert secondes[k]["bras"]["4b"]["entrees_servies"] == [len(v) for v in e["vues_bras_2"]]
    sha_propre, sha_etr = premieres[0]["sha_registre_source"], premieres[1]["sha_registre_source"]
    assert sha_propre != sha_etr
    assert R.verifier_registre_etranger("4a", sha_etr, sha_etr, sha_propre)
    assert R.verifier_registre_etranger("3", sha_propre, sha_etr, sha_propre)
    with pytest.raises(R.ArretRegistre, match="source propre servi au bras 4a"):
        R.verifier_registre_etranger("4a", sha_propre, sha_etr, sha_propre)
    with pytest.raises(R.ArretRegistre, match="pas l'empreinte du registre étranger"):
        R.verifier_registre_etranger("4a", "f" * 64, sha_etr, sha_propre)
    for b in ("1", "2", "3"):
        with pytest.raises(R.ArretRegistre):
            R.verifier_registre_etranger(b, sha_etr, sha_etr, sha_propre)
    # défaut du dossier versé : au bras 4b, le multiplicateur de la tenue ne s'applique pas aux entrées étrangères
    vue_etrangere = premieres[1]["vues_bras_2"][3]
    assert P.propre_gardee(vue_etrangere, 1, "2") is True
    assert P.propre_gardee(vue_etrangere, 0, "4b") is False
    assert P.propre_gardee(premieres[0]["vues_bras_2"][3], 0, "2") is True
    # note D7 (code v3) : les compteurs de B1 (iii) du jeu portent aussi les mondes sources tirés
    assert all(s.compteurs.tirages["sous-loi-source"][1] > 0 for s in suites)
    # code v3, C2 : au bras 4b, chaque copie servie est contrôlée par son origine et par l'empreinte déposée avec elle (cas
    # sain : chaque génération du jeu ci-dessus, et ici les quatre vues de la source 1 servies à la source 0)
    copie = MC.copie_scellee_4b(premieres[1])
    assert copie["source"] == 1 and copie["empreintes"] == premieres[1]["empreintes_vues_bras_2"]
    assert copie["empreintes"] == [R.empreinte_vue(v) for v in premieres[1]["vues_bras_2"]]
    assert vue_etrangere and all(R.verifier_vue_etrangere_4b(v, s, 0, 1) for v, s in zip(copie["vues"], copie["empreintes"]))
    # artefact : le registre propre du bras 2 servi au bras 4b (ce serait le bras 2)
    propre = MC.copie_scellee_4b(premieres[0])
    with pytest.raises(R.ArretRegistre, match="copie déposée au bras 4b venue de la source propre"):
        R.verifier_vue_etrangere_4b(propre["vues"][0], propre["empreintes"][0], 0, propre["source"])
    with pytest.raises(R.ArretRegistre, match="entrée de la source propre servie au bras 4b"):
        R.verifier_vue_etrangere_4b(propre["vues"][3], propre["empreintes"][3], 0, 1)
    ctx = MC.ContexteSource(g, bases[0], prop("lecteur-tenue", tau=2.0), 0.25, 0.25, str(tmp_path / "artefact-4b"))
    with pytest.raises(R.ArretRegistre, match="venue de la source propre"):
        MC.jouer_source(ctx, ("4b",), suite=suites[0], copie_etrangere_4b=propre)
    # artefact : copie altérée après le dépôt (une entrée changée) : l'empreinte ne tient plus
    alteree = [dict(e) for e in copie["vues"][3]]
    alteree[0] = dict(alteree[0], gardee=not alteree[0]["gardee"])
    with pytest.raises(R.ArretRegistre, match="n'a pas l'empreinte de la vue du bras 2"):
        R.verifier_vue_etrangere_4b(alteree, copie["empreintes"][3], 0, 1)
    # artefact : entrées d'une autre origine (la course de la source étrangère, non son bras 2)
    course = premieres[1]["registre_source"].vue("entiere")
    with pytest.raises(R.ArretRegistre, match="pas du bras 2 de la source étrangère"):
        R.verifier_vue_etrangere_4b(course, R.empreinte_vue(course), 0, 1)
    with pytest.raises(MC.ArretMecanique, match="incomplète"):
        MC.copie_scellee_4b(secondes[0])  # une sortie sans bras 2 joué n'a rien à déposer


def test_reproductibilite_a_l_octet_d_une_source(tmp_path):
    g = graines()
    a, _ = _jouer(g, str(tmp_path / "a"), "lecteur-heritage", 0.25, 3, "repro")
    b, _ = _jouer(g, str(tmp_path / "b"), "lecteur-heritage", 0.25, 3, "repro")
    for x in ("1", "2", "3"):
        assert a["bras"][x]["registre"].octets() == b["bras"][x]["registre"].octets()
        with open(a["bras"][x]["registre"].chemin, "rb") as fa, open(b["bras"][x]["registre"].chemin, "rb") as fb:
            assert fa.read() == fb.read()
        assert a["bras"][x]["mesure"] == b["bras"][x]["mesure"]
    assert a["registre_source"].octets() == b["registre_source"].octets()
