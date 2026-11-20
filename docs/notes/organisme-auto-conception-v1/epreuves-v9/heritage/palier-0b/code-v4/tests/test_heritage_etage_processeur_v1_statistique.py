"""Essais de la couche statistique, de l'étalonnage, des tirages et de l'analyse : la fréquence des lois vraies est celle de leur
monde ; garde 22 (étalonnage sans lecture) ; garde 26, taille réalisée (réglage étalonné, réglage faussé de 20 %) ;
reproductibilité à l'octet des sorties d'une case ; couches décisives refusées sans autorisation ; analyse sur des sorties
plantées (sceaux, règles de lecture, n, m, M10, M11). Graines « essai » ; aucun taux n'est calculé sur un tirage simulé."""

import inspect
import os

import numpy as np
import pytest

from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, graines, prop
from controle_ia.heritage_etage_processeur_v1 import analyse as AN
from controle_ia.heritage_etage_processeur_v1 import etalonnage as ET
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import rangs_signes as RS
from controle_ia.heritage_etage_processeur_v1 import statistique as ST
from controle_ia.heritage_etage_processeur_v1 import tirages as TI
from controle_ia.heritage_etage_processeur_v1.tirages import LECTURES


def _simuler(g, f, nom, dose, S, famille, **reglage):
    res = ST.simuler({b: g.g(couche="essai", famille=famille, bras=b, role="echantillonnage") for b in "123"},
                     g.g(couche="essai", famille=famille, role="monde"), g.g(couche="essai", famille=famille, role="source"),
                     prop(nom, **reglage), dose, 0.25, f, S)
    return res


def test_frequence_d_une_loi_vraie_est_celle_de_son_monde():
    g = graines()
    a = _simuler(g, FREQUENCES_D_ESSAI, "lecteur-heritage", 0.5, 3000, "strates", K=128)
    b = _simuler(g, dict(FREQUENCES_D_ESSAI, p_tient_vraie_source=0.5), "lecteur-heritage", 0.5, 3000, "strates", K=128)
    c = _simuler(g, dict(FREQUENCES_D_ESSAI, p_tient_vraie_cible=0.5), "lecteur-heritage", 0.5, 3000, "strates", K=128)
    assert np.array_equal(a["bras"]["1"]["M1"], b["bras"]["1"]["M1"])  # la strate source ne touche pas le bras 1
    assert b["bras"]["3"]["M1"].mean() < a["bras"]["3"]["M1"].mean()  # elle règle ce que le lecteur compose au bras 3
    assert not np.array_equal(a["bras"]["1"]["fausses_tenues"], c["bras"]["1"]["fausses_tenues"]) or \
        not np.array_equal(a["bras"]["1"]["vraies_tenues"], c["bras"]["1"]["vraies_tenues"])


def test_garde_22_etalonnage_sans_lecture():
    g = graines()
    ligne = ET.etalonner(g, "essai", "lecteur-tenue", lambda x: prop("lecteur-tenue", tau=x), "tau", 0.25, 1.0,
                         FREQUENCES_D_ESSAI, 2000)
    assert set(ligne) <= ET.CLES_PERMISES and ligne["atteignable"] is True
    assert ET.verifier_sortie([ligne])
    assert RS.VERROU_ETALONNAGE["leve"] is False
    with ET.verrou():
        with pytest.raises(RS.TestVerrouille):
            RS.valeur_p_bilaterale([1, 2, 3])
        with pytest.raises(RS.TestVerrouille):
            RS.regle_de_validite([1, 2, 3, 4, 5])
    with pytest.raises(ET.ArretEtalonnage):
        ET.verifier_sortie([dict(ligne, taux_de_rejet=0.04)])
    with pytest.raises(ET.ArretEtalonnage):
        ET.verifier_sortie(dict(ligne, valeur_p=0.2))
    source = inspect.getsource(ET)
    for interdit in ("valeur_p_bilaterale(", "valeur_p_unilaterale(", "lire_tirage(", "regle_de_validite(", "holm("):
        assert interdit not in source


def test_note_d8_ecart_type_nul_ou_taille_non_finie_arrete_l_etalonnage(monkeypatch):
    """Code v4, note D8 (B7) : sur des écarts-types plantés, non tirés — un écart-type entre jumelles nul, ou une taille réduite
    non finie, arrête l'étalonnage et n'est pas « non atteignable » ; un écart-type positif laisse la dichotomie ou la mention
    « non atteignable » comme avant."""
    def plante(sd, ecart):
        def jumelles(graines, couche, base, prop, dose, taux, f, S, bras, *a, **k):
            return ({"1": 0.0, "2": 0.0, "3": ecart(prop)}, {b: sd for b in bras})
        monkeypatch.setattr(ET, "jumelles", jumelles)

    fab = lambda x: prop("lecteur-heritage", K=x)  # noqa: E731
    plante(0.0, lambda p: 1.0)
    with pytest.raises(ET.ArretEtalonnage, match="note D8 : écart-type entre jumelles nul"):
        ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 1.0, FREQUENCES_D_ESSAI, 10)
    with pytest.raises(ET.ArretEtalonnage, match="note D8"):
        ET.ecart_type_sans_reglage(graines(), "essai", "sourd-egal", prop("sourd-egal"), 0.25, 0.25, FREQUENCES_D_ESSAI, 10,
                                   ("1", "2", "3"))
    plante(1.0, lambda p: float("nan"))
    with pytest.raises(ET.ArretEtalonnage, match="taille réduite non finie"):
        ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 1.0, FREQUENCES_D_ESSAI, 10)
    plante(1.0, lambda p: p["K"] / 256.0)  # taille 1 au réglage maximal : 0,5 atteignable, 1,5 non atteignable
    assert ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 1.5, FREQUENCES_D_ESSAI, 10)["statut"] == \
        "non atteignable"
    ligne = ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 0.5, FREQUENCES_D_ESSAI, 10)
    assert ligne["statut"] == "atteint" and abs(ligne["taille_estimee"] - 0.5) <= 0.02
    assert ET.ecart_type_sans_reglage(graines(), "essai", "sourd-egal", prop("sourd-egal"), 0.25, 0.25, FREQUENCES_D_ESSAI,
                                      10, ("1", "2", "3"))["ecart_type_jumelles"] == 1.0


def test_garde_26_taille_realisee_reglage_etalonne_et_faussé():
    g = graines()
    base = dict(famille="garde-26", proposeur="lecteur-tenue", dose=0.25)

    def taille(tau, role):
        moy, sd = ET.jumelles(g, "essai", dict(base, retrait=role), prop("lecteur-tenue", tau=tau), 0.25, 0.25,
                              FREQUENCES_D_ESSAI, 10000, ("1", "2", "3"))
        return ET.taille(moy, sd, "tenue")

    e_et, cible, sd_gele = taille(1.0, "etalonnage")
    e_dec, _, _ = taille(1.0, "decisif-simule")
    t, tenue = AN.taille_realisee(e_dec, sd_gele, cible)
    assert tenue and ET.taille_tenue(t, cible)
    e_faux, _, _ = taille(1.2, "decisif-simule")
    t_faux, tenue_faux = AN.taille_realisee(e_faux, sd_gele, cible)
    assert not tenue_faux and abs(t_faux - cible) > 0.05


def test_reproductibilite_a_l_octet_des_sorties_d_une_case(tmp_path):
    case = {"famille": "B", "proposeur": "lecteur-heritage", "config": prop("lecteur-heritage", K=64), "dose": 0.5,
            "taux": 0.25, "taille": 1.0, "bras": ("1", "2", "3")}
    a = TI.jouer_case(graines(), "essai", case, FREQUENCES_D_ESSAI, 3, str(tmp_path / "a"), grille=(10, 12))
    b = TI.jouer_case(graines(), "essai", case, FREQUENCES_D_ESSAI, 3, str(tmp_path / "b"), grille=(10, 12))
    assert a == b
    nom = TI.nom_de_case(case)
    for f in sorted(os.listdir(tmp_path / "a" / nom)):
        assert (tmp_path / "a" / nom / f).read_bytes() == (tmp_path / "b" / nom / f).read_bytes(), f
    desc, tab = AN.lire_case(str(tmp_path / "a" / nom))
    assert tab["M1-bras-3"].shape == (3, 12) and tab["lecture-rejette"].shape == (3, 2)
    with open(tmp_path / "a" / nom / "M1-bras-2.npy", "r+b") as fh:
        fh.seek(-1, 2)
        fh.write(b"\x07")
    with pytest.raises(AN.ArretAnalyse):
        AN.lire_case(str(tmp_path / "a" / nom))


def test_couches_decisives_refusees_sans_autorisation(tmp_path):
    case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
            "bras": ("1", "2", "3")}
    for couche in ("decisif", "confirmation"):
        with pytest.raises(GR.GraineRefusee):
            TI.lancer_famille(graines(), couche, [case], lambda c: FREQUENCES_D_ESSAI, 10, str(tmp_path / couche), "0" * 40, {})
        assert not os.path.exists(tmp_path / couche)
        with pytest.raises(GR.GraineRefusee):
            TI.simuler_case(graines(), couche, case, FREQUENCES_D_ESSAI, 1)
    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()


def test_manifeste_d_un_lancement(tmp_path):
    """Règle R9 : un lancement (couche « essai », deux tirages) écrit un manifeste scellé : configuration et empreinte,
    versions, racine, étiquettes, commit, fichiers gelés."""
    import json
    case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
            "bras": ("1", "2", "3")}
    TI.lancer_famille(graines(), "essai", [case], lambda c: FREQUENCES_D_ESSAI, 2, str(tmp_path / "run"), "0" * 40,
                      {"frequences": "a" * 64})
    m = json.loads((tmp_path / "run" / "manifeste.json").read_text(encoding="utf-8"))
    assert set(m) >= {"configuration", "configuration_sha256", "versions", "racine", "etiquettes", "commit", "fichiers_geles"}
    assert m["racine"] == 2026111902 and m["etiquettes"]["nombre"] > 0 and m["etiquettes"]["couches"] == ["couche=essai"]
    assert (tmp_path / "run" / "manifeste.json.sha256").exists()
    # code v4, choix 12 : la liste entière des étiquettes, triée, dans un fichier scellé à côté du manifeste, dont l'empreinte
    # (inscrite au manifeste) est celle de la liste et se rejoue à la main
    import hashlib
    liste = tmp_path / "run" / "manifeste-etiquettes.txt"
    octets = liste.read_bytes()
    lignes = octets.decode("utf-8").split("\n")
    assert m["etiquettes"]["fichier"] == "manifeste-etiquettes.txt" and lignes == sorted(lignes)
    assert len(lignes) == m["etiquettes"]["nombre"] and all(l.startswith("couche=essai|") for l in lignes)
    assert hashlib.sha256(octets).hexdigest() == m["etiquettes"]["sha256"] == m["etiquettes"]["fichier_sha256"]
    assert (tmp_path / "run" / "manifeste-etiquettes.txt.sha256").read_text(encoding="ascii").split()[0] == m["etiquettes"]["sha256"]
    assert TI.verifier_manifeste(str(tmp_path / "run" / "manifeste.json")) == m["etiquettes"]["nombre"]
    # artefacts : une étiquette retirée de la liste (compagnon refait), puis une liste altérée sans refaire son compagnon
    liste.write_bytes(b"\n".join(octets.split(b"\n")[1:]))
    (tmp_path / "run" / "manifeste-etiquettes.txt.sha256").write_text(
        f"{hashlib.sha256(liste.read_bytes()).hexdigest()}  manifeste-etiquettes.txt\n", encoding="ascii")
    with pytest.raises(TI.ArretTirages, match="ne rejoue pas"):
        TI.verifier_manifeste(str(tmp_path / "run" / "manifeste.json"))
    liste.write_bytes(octets + b"\n")
    with pytest.raises(TI.ArretTirages, match="compagnon"):
        TI.verifier_manifeste(str(tmp_path / "run" / "manifeste.json"))


def test_rapport_r_sur_des_valeurs_plantees():
    rng = np.random.default_rng(9)
    servis = rng.normal(2.0, 1.0, 4000)
    repli = rng.normal(0.4, 1.0, 4000)
    R, ic, positif = AN.rapport_R(repli, servis, rng, B=200)
    assert positif and abs(R - 0.2) < 0.05 and ic[0] < R < ic[1] and ic[1] < 0.8
    assert AN.rapport_R(repli, rng.normal(0.0, 1.0, 4000), rng, B=200)[2] is False


def test_essai_de_forme_borne_et_nomme(tmp_path):
    case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
            "bras": ("1", "2", "3")}
    with pytest.raises(TI.ArretTirages):
        TI.essai_de_forme(graines(), case, FREQUENCES_D_ESSAI, 201, (10, 12), str(tmp_path))
    with pytest.raises(TI.ArretTirages):
        TI.essai_de_forme(graines(), case, FREQUENCES_D_ESSAI, 2, (10, 12, 14), str(tmp_path))
    r = TI.essai_de_forme(graines(), case, FREQUENCES_D_ESSAI, 2, (10, 12), str(tmp_path))
    assert all(os.listdir(tmp_path)) and all(n.startswith("essai-de-forme-") for n in os.listdir(tmp_path))
    assert r["duree_s"] >= 0 and "case.json" in r["fichiers"]


# --- analyse sur des sorties plantées ------------------------------------------------------------------------------------


def test_regles_de_lecture_sur_des_valeurs_plantees():
    grille = (10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 44, 48)
    p = dict(zip(grille, (0.5, 0.79, 0.81, 0.79, 0.8, 0.85, 0.9, 0.9, 0.95, 0.97, 0.98, 0.99)))
    assert AN.atteint_a_partir_de(p, grille) == 20
    p48 = dict(p)
    p48[48] = 0.7
    assert AN.atteint_a_partir_de(p48, grille) is None
    q = dict(zip(grille, [0.9] * 12))
    assert AN.n_de_l_etage({("heritage", 0.5): p, ("tenue", 0.5): q}) == 20
    assert AN.n_de_l_etage({("heritage", 0.5): q, ("tenue", 0.5): q}) == 10
    assert AN.n_de_l_etage({("heritage", 0.5): p48, ("tenue", 0.5): q}) is None
    c3 = {k: (0.9 if k >= 8 else 0.5) for k in range(5, 17)}
    c4 = {k: k != 11 for k in range(5, 17)}
    assert AN.m_de_l_etage(c3, c4) == 12
    assert AN.part_m10(1.0, -0.5) == 1.0 and abs(AN.part_m10(1.0, 0.25) - 0.8) < 1e-12 and AN.part_m10(-1.0, 0.3) == 0.0
    assert AN.s7({0.25: (0.85, 0.95), 0.5: (0.81, 0.9)}, {0.25: True, 0.5: True}) == "presque autant"
    assert AN.s7({0.25: (0.1, 0.3), 0.5: (0.2, 0.79)}, {0.25: True, 0.5: True}) == "le repli coûte"
    assert AN.s7({0.25: (0.1, 0.3), 0.5: (0.7, 0.9)}, {0.25: True, 0.5: True}) == "indécis"
    assert AN.s7({0.25: (0.1, 0.3)}, {0.25: False}) == "sans objet"
    toutes = {g: (True, True) for g in range(1, 28)}
    table = AN.table_des_criteres({(10, 0.25, 0.25): "tenue"}, {(5, "sourd-egal", 0.25): "tenue"},
                                  {("heritage", 0.5): q, ("tenue", 0.5): q}, c3, {(0.5, 10): 0.9}, {**toutes, 17: None})
    assert table["C6"].startswith("non établi") and table["C2_n"] == 10 and table["issue"].startswith("non prononcée")
    table_tenue = AN.table_des_criteres({(10, 0.25, 0.25): "tenue"}, {}, {}, c3, {(0.5, 10): 0.9}, toutes)
    assert table_tenue["C6"] == "tenu"
    table2 = AN.table_des_criteres({(10, 0.25, 0.25): "en échec"}, {}, {}, c3, {(0.5, 10): 0.7}, {**toutes, 1: (True, False)})
    assert table2["C1"] == "en échec" and table2["C5"] == "en échec" and table2["C6"] == "en échec"
    # note D4 (code v3) : une table des gardes incomplète arrête, au lieu de passer « C6 tenu »
    for incomplete in ({1: (True, True), 17: None}, {g: v for g, v in toutes.items() if g != 9}, {**toutes, 5: None}):
        with pytest.raises(AN.ArretAnalyse, match="table des gardes incomplète"):
            AN.table_des_criteres({(10, 0.25, 0.25): "tenue"}, {}, {}, c3, {(0.5, 10): 0.9}, incomplete)


def test_point_4_et_taux_sur_des_sorties_plantees():
    T, S = 10, 12
    sorties = {b: {"M1": np.zeros((T, S), dtype=np.int16)} for b in "123"}
    sorties["3"]["M1"][:, :3] = 1  # trois différences non nulles sur douze, à chaque tirage
    zeros = AN.part_de_differences_nulles(sorties, "3", "2", (10, 12))
    assert zeros == {10: 0.7, 12: 0.75}
    lect = np.zeros((T, 2), dtype=np.int8)
    lect[:7, 1] = LECTURES["établi"]
    assert AN.puissance_etabli(lect, (10, 12)) == {10: 0.0, 12: 0.7}
    t = AN.taux_par_nombre(lect == LECTURES["établi"], (10, 12))
    assert t[12]["compte"] == 7 and t[12]["tirages"] == 10 and t[12]["intervalle"][0] < 0.7 < t[12]["intervalle"][1]
    D = {"2": {"D": np.zeros((T, S)), "I": np.zeros((T, S))}, "3": {"D": np.ones((T, S)), "I": -np.ones((T, S))}}
    assert AN.m10_par_nombre(D, (10,))[10]["part"] == 1.0
