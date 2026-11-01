# -*- coding: utf-8 -*-
"""Essais de l'implémentation B (implementation_b.py).

Sources des valeurs attendues : uniquement « specification-statistique-decisive-v1.md » (vecteurs du § 4, du § 5.5,
tableau et listes du § 12, tables des § 8 à § 10), lue directement quand c'est possible plutôt que recopiée.
Lancer : python3 -m pytest -q   (depuis le dossier implementation-b/).
"""
from __future__ import annotations

import ast
import copy
import hashlib
import json
import math
import statistics
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import implementation_b as ib   # noqa: E402

DOSSIER = Path(__file__).resolve().parent
ENTREES = DOSSIER / "entrees"
P_SPEC = ENTREES / "specification-statistique-decisive-v1.md"
P_RES = ENTREES / "resultats-regles-defense.json"
P_ANA = ENTREES / "analyse-regles-defense.json"
R4 = ib.NOMS_VARIANTES[4]


# =============================================================================================
# Pièces communes
# =============================================================================================
@pytest.fixture(scope="session")
def texte_spec() -> str:
    return P_SPEC.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def analyse_a() -> dict:
    return ib.lire_json_octets(P_ANA.read_bytes(), "A")


@pytest.fixture(scope="session")
def e1_original() -> dict:
    return ib.lire_json_octets(P_RES.read_bytes(), "E1")


@pytest.fixture(scope="session")
def sortie_originale() -> dict:
    """Analyse de la course originale, racine imposée 20266201, avec l'essai « contre elle-même » (§ 12)."""
    return ib.analyser_fichiers(resultats=P_RES, racine=20266201, analyse_originale=P_ANA, resultats_originaux=P_RES)


@pytest.fixture()
def b_petit(monkeypatch):
    """Réduit B (nombre de rééchantillonnages) pour les essais de plomberie sur pièces synthétiques."""
    monkeypatch.setattr(ib, "B", 200)


def fabriquer_e1(graine=0, rho=111, rho_t=222, *, nb_poids_purs=0, nb_cos_eleves=0, effet_r3=0.10,
                 derive_fpr=0.0, melanger=True) -> dict:
    """Pièce synthétique au format E1 : 200 tâches, cinq variantes, tous les champs lus par l'implémentation."""
    rng = np.random.default_rng(graine)
    bonus = {"R0": 0.0, "R1": -0.01, "R2": 0.0, "R3": effet_r3, R4: 0.01}
    taches = []
    for c in (1, 2):
        for i in range(100):
            base = rng.uniform(0.05, 0.25)
            regles = {}
            for nom in ib.NOMS_VARIANTES:
                std = float(np.clip(base + bonus[nom] + rng.normal(0, 0.01), 0.0, 1.0))
                ren = float(np.clip(std + rng.normal(0, 0.0005), 0.0, 1.0))
                v = min(std, ren)
                if nom == "R3" and i < nb_poids_purs:
                    w = [0.0] * 9
                    w[4] = 1.0
                else:
                    w = [float(x) for x in rng.dirichlet(np.ones(9))]
                if nom == R4 and i < nb_cos_eleves:
                    cos = [float(x) for x in rng.uniform(0.9995, 1.0, 8)]
                else:
                    cos = [float(x) for x in rng.uniform(-1.0, 0.9, 8)]
                regles[nom] = {
                    "V_iii_final": v, "V_iii_standard": std, "V_iii_renforce": ren,
                    "ii_final": float(np.clip(0.5 + rng.normal(0, 0.05), 0, 1)),
                    "exploitabilite_finale": 1.0 - v,
                    "exploitabilite_moyenne_tours": float(np.clip(1.0 - v + rng.normal(0, 0.01), 0, 1)),
                    "fpr_final": 0.01 + derive_fpr + float(rng.normal(0, 0.0005)),
                    "lam": 0.3 if nom == R4 else None, "reference": "moyenne" if nom == R4 else None,
                    "poids_finaux": w,
                    "par_tour": {"cos_consecutif": cos, "exploitabilite": [float(x) for x in rng.uniform(0.7, 0.9, 8)]},
                }
            taches.append({"code_delta": c, "instance": i, "delta": 1.4 if c == 1 else 1.6, "racine": rho,
                           "racine_tenue": rho_t, "config_sha256": "0" * 64, "regles": regles})
    if melanger:
        ordre = rng.permutation(len(taches))
        taches = [taches[j] for j in ordre]
    return {"run_id": "synthetique", "manifeste_sha256": "0" * 64,
            "resultat": {"temps": {"mur_s": 0.0}, "resultats": taches}}


def taches_de(e1):
    return e1["resultat"]["resultats"]


def tache(e1, c, i):
    return next(t for t in taches_de(e1) if t["code_delta"] == c and t["instance"] == i)


def bornes(bas8, haut8, bas_e=None, haut_e=None):
    return {"B8": (bas8, haut8), "E8": (bas8 if bas_e is None else bas_e, haut8 if haut_e is None else haut_e)}


def ecrire_avec_compagnon(chemin: Path, octets: bytes) -> str:
    chemin.write_bytes(octets)
    sha = hashlib.sha256(octets).hexdigest()
    Path(str(chemin) + ".sha256").write_text(f"{sha}  {chemin.name}\n", encoding="utf-8")
    return sha


# =============================================================================================
# Constantes, libellés, indépendance
# =============================================================================================
def test_constantes_binaires64():
    assert ib.N == 100 and ib.B == 20_000
    assert ib.P == (0.003125, 0.00625, 0.0125, 0.025, 0.05, 0.95, 0.975, 0.9875, 0.99375, 0.996875)
    assert ib.DEUX_ALPHA == 0.02 and ib.M == 0.02 and ib.S5 == 0.02 and ib.TAU == 0.05 and ib.EPS == 1e-9
    assert ib.SEUIL_T3_POIDS_PUR == 1.0 - 1e-9
    assert ib.CLES_QUANTILES == ("q0.003125", "q0.00625", "q0.0125", "q0.025", "q0.05",
                                 "q0.95", "q0.975", "q0.9875", "q0.99375", "q0.996875")


def test_z_etoile_est_le_quantile_0_99375_de_la_loi_normale():
    assert abs(statistics.NormalDist().inv_cdf(0.99375) - ib.Z_ETOILE) < 1e-12


def test_bornes_B2_B8_E8():
    q = {cle: float(i) for i, cle in enumerate(ib.CLES_QUANTILES)}
    b = ib.bornes_depuis_statistique({"quantiles": q})
    assert b["B2"] == (q["q0.00625"], q["q0.99375"])
    assert b["B8"] == (q["q0.003125"], q["q0.996875"])
    assert b["E8"] == (q["q0.00625"], q["q0.99375"])


def test_les_libelles_sont_ceux_de_la_specification(texte_spec):
    libelles = [ib.A_DEGENERE, ib.A_CONFIRMEE, ib.A_REFUTEE, ib.A_NON_DEMONTREE, ib.EQUIVALENT, ib.INCERTAIN,
                *ib.LIBELLES_TABLE_C.values(), ib.V_SANTE, ib.V_DEGENERE, ib.V_IMPRECIS, ib.V_REPLIQUEE,
                ib.V_HR1_SIGNE, ib.V_HR1_PETIT, ib.V_HR0_INTERET, ib.V_HR0_NON_NUL, ib.V_NON_REPLIQUEE,
                ib.V_HR3_SANS_VERDICT, ib.V_AUDIT_ATTENTE, ib.V_ARTEFACT, ib.O_CONFIRMEE, ib.O_REFUTEE,
                ib.O_NON_TRANCHEE, *ib.ISSUES.values()]
    for lib in libelles:
        assert f"« {lib} »" in texte_spec or lib in texte_spec, lib
    # tables B et B′ : les six libellés génériques de la spécification, avec R_k pour la variante
    for gabarit in ("R_k > R2", "R2 > R_k", "R_k ≳ R2", "R2 ≳ R_k", "≈", "?"):
        assert f"« {gabarit} »" in texte_spec
    cb = [ib.classe_table_B("R_k", bornes(*b))["classe"] for b in
          [(0.03, 0.06), (-0.06, -0.03), (-0.01, 0.01), (0.001, 0.05), (-0.05, -0.001), (-0.01, 0.03)]]
    assert cb == ["R_k > R2", "R2 > R_k", "≈", "R_k ≳ R2", "R2 ≳ R_k", "?"]
    cbp = [ib.classe_table_Bprime("R_k", bornes(*b))["classe"] for b in
           [(0.03, 0.06), (-0.06, -0.03), (-0.01, 0.01), (0.001, 0.05), (-0.05, -0.001), (-0.01, 0.03)]]
    assert cbp == ["R2 > R_k", "R_k > R2", "≈", "R2 ≳ R_k", "R_k ≳ R2", "?"]


def test_variantes_codes_et_libelles():
    assert ib.NOMS_VARIANTES == ("R0", "R1", "R2", "R3", "R4[moyenne,λ=0.3]")
    assert [ib.RANG[n] for n in ib.NOMS_VARIANTES] == [0, 1, 2, 3, 4]
    assert ib.libelle_contraste("R3", "V") == "R3 - R2 (V_iii_final)"
    assert ib.libelle_contraste(R4, "Xbarre") == "R4[moyenne,λ=0.3] - R2 (exploitabilite_moyenne_tours)"
    assert len(ib.TOUS_LES_CONTRASTES) == 16
    # codes de générateur donnés en exemple dans le § 5.4
    assert ib.code_generateur("V", "R3") == 203
    assert ib.code_generateur("V", "R0") == 200
    assert ib.code_generateur("V", R4) == 204
    assert ib.code_generateur("ii", "R0") == 300
    assert ib.code_generateur("Xbarre", "R1") == 1001


def test_le_module_n_importe_rien_du_depot_ni_du_reseau():
    arbre = ast.parse((DOSSIER / "implementation_b.py").read_text(encoding="utf-8"))
    importes = set()
    for noeud in ast.walk(arbre):
        if isinstance(noeud, ast.Import):
            importes |= {a.name.split(".")[0] for a in noeud.names}
        elif isinstance(noeud, ast.ImportFrom):
            importes.add(noeud.module.split(".")[0])
    assert importes <= {"__future__", "argparse", "hashlib", "json", "math", "os", "platform", "re", "sys", "time",
                        "pathlib", "numpy"}, importes
    source = (DOSSIER / "implementation_b.py").read_text(encoding="utf-8")
    for interdit in ("socket", "urllib", "requests", "subprocess", "arene_", "scipy"):
        assert interdit not in source


# =============================================================================================
# Règle D (§ 4)
# =============================================================================================
@pytest.mark.parametrize("h, attendu", [(h, (a, b)) for (h, a, b) in ib.VECTEURS_REGLE_D])
def test_regle_d_vecteurs_d_essai_du_paragraphe_4(h, attendu):
    assert ib.regle_d_derivation(h) == attendu


def test_regle_d_vecteurs_en_dur_recopies_de_la_specification(texte_spec):
    # les trois vecteurs écrits dans la spécification (lus dans son texte, pas dans le code)
    for h in ("d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d", "0" * 64, "f" * 64):
        assert h in texte_spec or h[0] * 64 == h
    for entier in ib.ENTIERS_DES_VECTEURS:
        assert str(entier) in texte_spec
    assert len(ib.ENTIERS_DES_VECTEURS) == 6


def test_regle_d_cas_sain_differe_des_racines_de_la_course_originale():
    h = ib.VECTEURS_REGLE_D[0][0]
    assert ib.regle_d_derivation(h) == (11786724493248295725, 9136419304016434890)
    assert ib.regle_d_derivation(h) != (20266201, 20266202)


def test_regle_d_les_entiers_des_vecteurs_sont_interdits_comme_racines():
    for h, a, b in ib.VECTEURS_REGLE_D:
        with pytest.raises(ib.Arret):
            ib.regle_d(h)            # (rho, rho_t) sont deux des six entiers interdits
        with pytest.raises(ib.Arret):
            ib.regle_d_gardes(a, b)


@pytest.mark.parametrize("rho, rho_t, doit_arreter", [
    (5, 5, True),                              # rho == rho_t
    (20261201, 7, True), (7, 20261202, True), (20266201, 7, True), (7, 20266202, True),
    (20261000, 7, True), (7, 20269999, True),  # bornes de la plage, incluses
    (20265000, 7, True),
    (20260999, 7, False), (20270000, 7, False),   # juste hors de la plage
    (11786724493248295725, 7, True),           # un des six entiers des vecteurs
    (7, 4616211851522120706, True),
    (123456789, 987654321, False),
])
def test_regle_d_gardes(rho, rho_t, doit_arreter):
    if doit_arreter:
        with pytest.raises(ib.Arret):
            ib.regle_d_gardes(rho, rho_t)
    else:
        ib.regle_d_gardes(rho, rho_t)


@pytest.mark.parametrize("h", ["", "0" * 63, "0" * 65, "F" * 64, "g" * 64, " " + "0" * 63])
def test_regle_d_exige_64_hexadecimaux_minuscules(h):
    with pytest.raises(ib.Arret):
        ib.regle_d_derivation(h)


def test_regle_d_depuis_octets_utilise_l_empreinte_des_octets_exacts():
    octets = "préenregistrement de test λ\n".encode("utf-8")
    h, rho, rho_t = ib.regle_d_depuis_octets(octets)
    assert h == hashlib.sha256(octets).hexdigest()
    assert (rho, rho_t) == ib.regle_d_derivation(h)
    h2, rho2, _ = ib.regle_d_depuis_octets(octets + b" ")
    assert h2 != h and rho2 != rho


def test_regle_d_sans_cle_de_descendance_et_mots_64_bits():
    h = "ab" * 32
    e = int(h, 16)
    ss = np.random.SeedSequence(e)
    assert ss.spawn_key == ()
    mots = ss.generate_state(2, dtype=np.uint64)
    assert ib.regle_d_derivation(h) == (int(mots[0]), int(mots[1]))


# =============================================================================================
# Générateur (§ 5.4, § 5.5)
# =============================================================================================
@pytest.mark.parametrize("v", ib.VECTEURS_GENERATEUR)
def test_generateur_vecteurs_d_essai_du_paragraphe_5_5(v):
    c, code = v["cle"][0], v["cle"][1]
    ind = ib.indices_reechantillonnage(20266201, c, code)
    assert ind.shape == (20000, 100) and ind.dtype == np.int64
    assert ind.min() >= 0 and ind.max() <= 99
    assert [int(x) for x in ind[0, :10]] == v["ligne0_dix_premiers"]
    assert [int(x) for x in ind[-1, -5:]] == v["derniere_ligne_cinq_derniers"]


def test_generateur_vecteurs_en_dur_sont_ceux_de_la_specification(texte_spec):
    for v in ib.VECTEURS_GENERATEUR:
        assert ", ".join(str(x) for x in v["ligne0_dix_premiers"]) in texte_spec
        assert ", ".join(str(x) for x in v["derniere_ligne_cinq_derniers"]) in texte_spec


def test_generateur_depend_de_la_racine_du_budget_et_du_code():
    a = ib.indices_reechantillonnage(20266201, 1, 203)[0, :10]
    assert not np.array_equal(a, ib.indices_reechantillonnage(20266202, 1, 203)[0, :10])
    assert not np.array_equal(a, ib.indices_reechantillonnage(20266201, 2, 203)[0, :10])
    assert not np.array_equal(a, ib.indices_reechantillonnage(20266201, 1, 204)[0, :10])
    assert np.array_equal(a, ib.indices_reechantillonnage(20266201, 1, 203)[0, :10])


def test_generateur_accepte_une_racine_de_64_bits():
    ind = ib.indices_reechantillonnage(2 ** 64 - 1, 1, 203)
    assert ind.shape == (20000, 100)


# =============================================================================================
# Quantiles de type 7 (§ 5.6)
# =============================================================================================
def test_quantile_type7_egal_a_numpy_lineaire():
    rng = np.random.default_rng(3)
    mu = rng.normal(size=20000)
    tri = np.sort(mu)
    ref = np.quantile(mu, ib.P, method="linear")
    mes = [ib.quantile_type7(tri, p) for p in ib.P]
    assert np.max(np.abs(np.array(mes) - ref)) < 1e-14


def test_quantile_type7_cas_limites():
    tri = np.array([1.0, 2.0, 4.0])
    assert ib.quantile_type7(tri, 0.0) == 1.0
    assert ib.quantile_type7(tri, 1.0) == 4.0            # f >= B-1 : dernier élément
    assert ib.quantile_type7(tri, 0.5) == 2.0
    assert ib.quantile_type7(tri, 0.75) == 3.0           # 2 + 0.5 * (4 - 2)
    assert ib.quantile_type7(np.array([5.0]), 0.3) == 5.0


# =============================================================================================
# Statistique sur la course originale (§ 12)
# =============================================================================================
def test_tableau_de_controle_du_paragraphe_12(sortie_originale, texte_spec):
    rangees = ib.lire_table_12(texte_spec)
    assert len(rangees) == 10
    for r in rangees:
        stat = sortie_originale["resultat"][str(r["budget"])]["contrastes_contre_R2"][
            ib.libelle_contraste(r["variante"], r["mesure"])]
        for cle in ("moyenne", "ecart_type"):
            assert abs(stat[cle] - r[cle]) <= 1e-9
        for cle in ("q0.003125", "q0.00625", "q0.99375", "q0.996875"):
            assert abs(stat["quantiles"][cle] - r[cle]) <= 1e-9


def test_quelques_valeurs_du_paragraphe_12_recopiees_a_la_main(sortie_originale):
    s = sortie_originale["resultat"]["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]
    assert abs(s["moyenne"] - 0.10448042252007811) <= 1e-12
    assert abs(s["ecart_type"] - 0.05656582805294246) <= 1e-12
    assert abs(s["quantiles"]["q0.003125"] - 0.08961294692052145) <= 1e-12
    assert abs(s["quantiles"]["q0.996875"] - 0.1195334438923409) <= 1e-12
    s = sortie_originale["resultat"]["2"]["contrastes_contre_R2"]["R0 - R2 (V_iii_final)"]
    assert abs(s["quantiles"]["q0.00625"] - (-0.005623565481548155)) <= 1e-12


def test_16_contrastes_par_budget_identiques_a_l_analyse_de_reference(sortie_originale, analyse_a):
    for c in ("1", "2"):
        assert len(sortie_originale["resultat"][c]["contrastes_contre_R2"]) == 16
        for lib, sb in sortie_originale["resultat"][c]["contrastes_contre_R2"].items():
            sa = analyse_a["resultat"][c]["contrastes_contre_R2"][lib]
            assert set(sb) == {"moyenne", "ecart_type", "n", "quantiles", "zeros_exacts"}
            assert set(sb["quantiles"]) == set(ib.CLES_QUANTILES)
            assert sb["n"] == sa["n"] == 100 and sb["zeros_exacts"] == sa["zeros_exacts"]
            assert abs(sb["moyenne"] - sa["moyenne"]) <= 1e-9
            assert abs(sb["ecart_type"] - sa["ecart_type"]) <= 1e-9
            for cle in ib.CLES_QUANTILES:
                assert abs(sb["quantiles"][cle] - sa["quantiles"][cle]) <= 1e-9


def test_comparaison_automatique_a_la_reference(sortie_originale, analyse_a):
    cmp_ = ib.comparer_a_reference(sortie_originale, analyse_a, analyse_a)
    assert cmp_["concordance"] is True
    assert cmp_["ecart_maximal_absolu"] <= 1e-9
    assert cmp_["discordance_a_arret"] is False and cmp_["alertes_de_discordance"] == []
    assert cmp_["classes"]["identiques"] and cmp_["classes"]["nombre_de_classes_comparees"] == 25
    assert cmp_["verdicts_regles_originales"]["identiques"] and cmp_["z_pi"]["ok"]
    niveaux = [d["niveau"] for c in ("1", "2") for d in cmp_["detail_par_contraste"][c].values()]
    assert niveaux.count("arrêt") == 10 and niveaux.count("alerte") == 22


def test_statistique_d_un_contraste_a_la_main():
    d = np.array([0.1, -0.1, 0.0, 0.2] * 25)
    st = ib.statistique_contraste(d, 20266201, 1, 203)
    assert st["moyenne"] == pytest.approx(0.05)
    assert st["ecart_type"] == pytest.approx(math.sqrt(sum((x - 0.05) ** 2 for x in d) / 99))
    assert st["zeros_exacts"] == 25 and st["n"] == 100
    assert st["quantiles"]["q0.003125"] < st["moyenne"] < st["quantiles"]["q0.996875"]
    qs = [st["quantiles"][c] for c in ib.CLES_QUANTILES]
    assert qs == sorted(qs)


# =============================================================================================
# Classes sur la course originale (§ 12) et table A (§ 8)
# =============================================================================================
def test_classes_de_la_course_originale(sortie_originale):
    at = ib._attendus_12(sortie_originale)
    assert at["ok"], json.dumps(at, ensure_ascii=False, default=str)[:600]
    cl = sortie_originale["classes"]
    assert (cl["table_A"]["ligne"], cl["table_A"]["classe"]) == (2, "HR1 confirmée")
    assert [cl["table_B"]["R1"][c]["classe"] for c in "12"] == ["R2 ≳ R1", "?"]
    assert [cl["table_Bprime"]["R1"][c]["classe"] for c in "12"] == ["R2 > R1", "R2 ≳ R1"]
    assert [cl["table_C"]["R3"][c]["ligne"] for c in "12"] == [1, 1]
    assert sortie_originale["classes_a_la_frontiere"] == []


def test_controles_de_sante_de_la_course_originale(sortie_originale):
    s = sortie_originale["sante"]
    assert s["etat_global"] == {"T2": False, "T3": False, "T4": False, "T5": False, "T6": False}
    assert [s[c]["T3"]["nb_taches_poids_pur"] for c in "12"] == [0, 0]
    assert [s[c]["T4"]["nb_taches_cos_moyen_ge_0_999"] for c in "12"] == [5, 2]
    assert round(max(s[c]["T5"]["plus_grand_standard_moins_renforce"] for c in "12"), 5) == 0.00039
    assert round(max(s[c]["T5"]["plus_grand_abs_ecart_de_contraste"] for c in "12"), 5) == 0.00043
    assert round(max(s[c]["T6"]["plus_grand_abs_ecart_a_alpha"] for c in "12"), 5) == 0.00019
    assert all(s[c]["garde_coherence_V"] == "ok" for c in "12")


def test_verdicts_de_la_course_originale(sortie_originale):
    v = sortie_originale["verdicts_regles_originales"]
    assert {k: v[k]["verdict"] for k in ("HR1", "HR0", "HR3", "HR2")} == {
        "HR1": "HR1 confirmée", "HR0": "réfutée", "HR3": "confirmée", "HR2": "non tranchée"}
    assert v["T2_T3_T5_T6_effectivement_non_declenches"] is True


def test_essai_des_gardes_de_la_replication_contre_elle_meme(sortie_originale):
    eg = sortie_originale["ecart_de_replication"]["contrastes_primaires"]
    assert len(eg) == 4 and all(e["g"] == 0.0 for e in eg.values())
    assert all(e["z"] == 0.0 for e in eg.values())
    d = sortie_originale["declencheurs_audit"]
    assert d["TR2_trop_propre"] is True and d["TR1_ecart_de_replication"] is False
    assert sortie_originale["comptes_graines_neuves"]["comptes"] == {k: 200 for k in ("R0", "R1", "R2", "R3", "R4")}
    assert sortie_originale["comptes_graines_neuves"]["arret_graines_non_neuves"] is True
    assert sortie_originale["lecture_autorisee"] is False and len(sortie_originale["arrets"]) == 1
    assert set(sortie_originale["verdicts_apres_declencheurs"].values()) == {"non jugeable (audit en attente)"}
    assert sortie_originale["issue_globale_brute"]["issue"] == "non jugeable (plomberie)"


@pytest.mark.parametrize("entree, ligne, classe", [
    # budget 1 et 2 : (est, bas, haut) ; moyennes de V communes
    (dict(e1=(0.10, 0.09, 0.12), e2=(0.12, 0.11, 0.13)), 2, "HR1 confirmée"),
    (dict(e1=(0.02, 0.001, 0.05), e2=(0.02, 0.001, 0.05)), 2, "HR1 confirmée"),           # est == m compte (≥)
    (dict(e1=(0.0199999, 0.001, 0.05), e2=(0.10, 0.09, 0.12)), 4, "HR1 non démontrée"),   # est < m
    (dict(e1=(0.10, 0.0, 0.12), e2=(0.12, 0.11, 0.13)), 4, "HR1 non démontrée"),          # bas == 0 : pas > 0
    (dict(e1=(0.10, 0.09, 0.12), e2=(0.05, -0.03, 0.0)), 4, "HR1 non démontrée"),         # haut == 0 : pas < 0
    (dict(e1=(0.10, 0.09, 0.12), e2=(-0.05, -0.09, -0.001)), 3, "HR1 réfutée"),           # haut < 0 dans un budget
    (dict(e1=(-0.05, -0.09, -0.001), e2=(0.10, 0.09, 0.12)), 3, "HR1 réfutée"),
    (dict(e1=(0.01, -0.02, 0.04), e2=(0.01, -0.02, 0.04)), 4, "HR1 non démontrée"),
])
def test_table_A_lignes(entree, ligne, classe):
    def mk(t, moy=0.12):
        return {"est": t[0], "bas_B2": t[1], "haut_B2": t[2], "moyennes_V": {n: moy for n in ib.NOMS_VARIANTES}}
    r = ib.classe_table_A({1: mk(entree["e1"]), 2: mk(entree["e2"])})
    assert (r["ligne"], r["classe"]) == (ligne, classe)


def test_table_A_jeu_degenere():
    def mk(moy, t=(0.10, 0.09, 0.12), exceptions=None):
        m = {n: moy for n in ib.NOMS_VARIANTES}
        m.update(exceptions or {})
        return {"est": t[0], "bas_B2": t[1], "haut_B2": t[2], "moyennes_V": m}
    ok = mk(0.12)
    # les cinq moyennes ≤ 2α = 0,02 (inclus) à un budget : ligne 1, même si l'effet est positif
    assert ib.classe_table_A({1: mk(0.02), 2: ok})["ligne"] == 1
    assert ib.classe_table_A({1: ok, 2: mk(0.0)})["ligne"] == 1
    assert ib.classe_table_A({1: mk(0.0200001), 2: ok})["ligne"] == 2
    assert ib.classe_table_A({1: mk(0.01, exceptions={"R3": 0.03}), 2: ok})["ligne"] == 2   # une seule variante au-dessus
    # le jeu dégénéré l'emporte sur « réfutée »
    ref = (-0.05, -0.09, -0.001)
    assert ib.classe_table_A({1: mk(0.01, ref), 2: ok})["ligne"] == 1
    assert ib.classe_table_A({1: mk(0.01), 2: ok})["classe"] == "non concluant : jeu dégénéré"


# =============================================================================================
# Tables B, B′, C (§ 8) : chaque ligne et l'égalité aux seuils
# =============================================================================================
CAS_B = [
    (bornes(0.03, 0.06), 1),
    (bornes(0.0200001, 0.06), 1),
    (bornes(0.02, 0.05, 0.0, 0.04), 4),              # bas == m : pas strictement supérieur
    (bornes(-0.06, -0.03), 2),
    (bornes(-0.05, -0.02, -0.03, -0.01), 5),         # haut == -m : pas strictement inférieur
    (bornes(-0.015, 0.015, -0.01, 0.01), 3),
    (bornes(-0.02, 0.01), 6),                        # bas(E8) == -m : pas strictement supérieur
    (bornes(-0.01, 0.02), 6),                        # haut(E8) == m : pas strictement inférieur
    (bornes(-0.01, 0.03), 6),
    (bornes(0.001, 0.05), 4),
    (bornes(0.0, 0.05), 6),                          # bas == 0 : pas > 0
    (bornes(-0.05, -0.001), 5),
    (bornes(-0.05, 0.0), 6),                         # haut == 0 : pas < 0
    (bornes(0.001, 0.01), 3),                        # étroit autour de 0 : équivalence avant la ligne 4
    (bornes(-0.01, -0.001), 3),
    (bornes(-0.03, 0.01, -0.0199, 0.0199), 3),       # E8 plus étroit que B8 : équivalence
    (bornes(0.03, 0.06, -0.001, 0.001), 1),          # la ligne 1 passe avant la ligne 3
]


@pytest.mark.parametrize("b, ligne", CAS_B)
def test_table_B_et_Bprime_lignes(b, ligne):
    rb = ib.classe_table_B("R3", b)
    rp = ib.classe_table_Bprime("R3", b)
    assert rb["ligne"] == rp["ligne"] == ligne
    attendu_b = {1: "R3 > R2", 2: "R2 > R3", 3: "≈", 4: "R3 ≳ R2", 5: "R2 ≳ R3", 6: "?"}[ligne]
    attendu_p = {1: "R2 > R3", 2: "R3 > R2", 3: "≈", 4: "R2 ≳ R3", 5: "R3 ≳ R2", 6: "?"}[ligne]
    assert rb["classe"] == attendu_b and rp["classe"] == attendu_p


@pytest.mark.parametrize("bas, haut, ligne", [
    (-0.06, -0.03, 1), (-0.015, -0.005, 2), (-0.03, -0.005, 3), (0.001, 0.05, 4), (-0.01, 0.02, 5), (-0.03, 0.03, 6),
    (-0.03, -0.02, 3),      # haut == -S5 : pas < -S5 ; haut < 0 ; bas ≤ -S5
    (-0.02, 0.03, 6),       # bas == -S5 : pas > -S5
    (0.0, 0.01, 5),         # bas == 0 : pas > 0 mais > -S5
    (-0.01, 0.0, 5),        # haut == 0 : pas < 0
])
def test_table_C_lignes(bas, haut, ligne):
    r = ib.classe_table_C({"B8": (bas, haut), "E8": (bas, haut)})
    assert r["ligne"] == ligne and r["classe"] == ib.LIBELLES_TABLE_C[ligne]


def test_frontiere_numerique_marque_les_quantites_a_moins_de_epsilon():
    r = ib.classe_table_B("R3", bornes(ib.M + 0.5e-9, 0.06))
    assert r["ligne"] == 1 and r["frontiere"] is True
    assert r["comparaisons_a_la_frontiere"][0]["quantite"] == "bas(B8)"
    assert ib.classe_table_B("R3", bornes(ib.M + 2e-9, 0.06))["frontiere"] is False
    # inclusif : |x - seuil| <= epsilon ; seuil 0 et x = epsilon exactement
    r = ib.classe_table_B("R3", bornes(1e-9, 0.05))
    assert r["ligne"] == 4 and r["frontiere"] is True
    r = ib.classe_table_B("R3", bornes(1.0000001e-9, 0.05))
    assert r["ligne"] == 4 and r["frontiere"] is False
    # seul le chemin évalué compte : la ligne 1 décide, la comparaison de la ligne 3 n'est pas faite
    r = ib.classe_table_B("R3", bornes(0.05, 0.06, -ib.M + 1e-12, ib.M - 1e-12))
    assert r["ligne"] == 1 and r["frontiere"] is False
    # table C et table A
    assert ib.classe_table_C({"B8": (-ib.S5 + 1e-10, 0.05), "E8": (0, 0)})["frontiere"] is True
    a = ib.classe_table_A({c: {"est": ib.M + 1e-10, "bas_B2": 0.01, "haut_B2": 0.1,
                               "moyennes_V": {n: 0.12 for n in ib.NOMS_VARIANTES}} for c in (1, 2)})
    assert a["ligne"] == 2 and a["frontiere"] is True


# =============================================================================================
# Verdicts du § 9 (règles de la course originale)
# =============================================================================================
def _classes_synth(b0=("≈", "≈"), b4=("R4 ≳ R2", "R4 ≳ R2"), bp1=("R2 > R1", "R2 ≳ R1"), ligne_a=2):
    def par_c(labels):
        return {str(c): {"classe": labels[c - 1], "ligne": 1, "frontiere": False} for c in (1, 2)}
    return {"table_A": {"ligne": ligne_a, "classe": ib.A_CONFIRMEE, "frontiere": False},
            "table_B": {"R0": par_c(b0), "R4": par_c(b4)}, "table_Bprime": {"R1": par_c(bp1)}}


ETAT_OK = {"T2": False, "T3": False, "T4": False, "T5": False, "T6": False}


@pytest.mark.parametrize("b0, attendu", [
    (("R2 > R0", "R2 > R0"), "confirmée"), (("R2 > R0", "≈"), "réfutée"), (("≈", "≈"), "réfutée"),
    (("R0 ≳ R2", "R2 > R0"), "réfutée"), (("R0 > R2", "R2 > R0"), "réfutée"),
    (("R2 > R0", "R2 ≳ R0"), "non tranchée"), (("R2 ≳ R0", "R2 ≳ R0"), "non tranchée"),
    (("?", "R2 > R0"), "non tranchée"), (("?", "?"), "non tranchée"),
])
def test_verdict_HR0_original(b0, attendu):
    assert ib.verdicts_regles_originales(_classes_synth(b0=b0), ETAT_OK)["HR0"]["verdict"] == attendu


@pytest.mark.parametrize("b4, t4, attendu", [
    (("R4 > R2", "≈"), False, "confirmée"), (("R4 ≳ R2", "R4 ≳ R2"), False, "confirmée"),
    (("R4 ≳ R2", "?"), False, "non tranchée"), (("R4 ≳ R2", "R2 > R4"), False, "réfutée"),
    (("R2 ≳ R4", "R4 > R2"), False, "non tranchée"),            # « R2 ≳ R4 » ne réfute pas au § 9
    (("R2 ≳ R4", "R2 ≳ R4"), False, "non tranchée"),
    (("R4 > R2", "R4 > R2"), True, "sans verdict (R4 ≈ défense figée)"),
])
def test_verdict_HR3_original(b4, t4, attendu):
    etat = dict(ETAT_OK, T4=t4)
    assert ib.verdicts_regles_originales(_classes_synth(b4=b4), etat)["HR3"]["verdict"] == attendu


@pytest.mark.parametrize("bp1, attendu", [
    (("R2 > R1", "R2 > R1"), "confirmée"), (("R2 > R1", "R2 ≳ R1"), "non tranchée"), (("R2 > R1", "≈"), "réfutée"),
    (("R1 ≳ R2", "?"), "réfutée"), (("R1 > R2", "R2 > R1"), "réfutée"), (("?", "?"), "non tranchée"),
])
def test_verdict_HR2_original(bp1, attendu):
    assert ib.verdicts_regles_originales(_classes_synth(bp1=bp1), ETAT_OK)["HR2"]["verdict"] == attendu


# =============================================================================================
# Verdicts bruts de la réplication (§ 10.1)
# =============================================================================================
def _pb(e1, e2):
    return {c: {"est": e[0], "bas_B2": e[1], "haut_B2": e[2]} for c, e in ((1, e1), (2, e2))}


JEU_OK = {1: False, 2: False}


@pytest.mark.parametrize("etat, jeu, pb, ligne", [
    (dict(ETAT_OK, T2=True), JEU_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T3=True), JEU_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T5=True), JEU_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T6=True), JEU_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T4=True), JEU_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 3),    # T4 ne bloque pas HR1
    (ETAT_OK, {1: False, 2: True}, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 2),
    (ETAT_OK, JEU_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 3),
    (ETAT_OK, JEU_OK, _pb((0.05, 0.001, 0.09), (0.05, 0.001, 0.09)), 3),            # est == τ compte (≥)
    (ETAT_OK, JEU_OK, _pb((0.1, 0.09, 0.12), (-0.05, -0.09, -0.001)), 4),
    (ETAT_OK, JEU_OK, _pb((0.1, 0.09, 0.12), (0.01, -0.01, 0.04)), 5),              # haut ∈ [0 ; τ)
    (ETAT_OK, JEU_OK, _pb((0.1, 0.09, 0.12), (0.01, 0.0, 0.0)), 5),                 # haut == 0 : pas < 0, mais < τ
    (ETAT_OK, JEU_OK, _pb((0.1, 0.09, 0.12), (0.04999, 0.001, 0.09)), 6),           # est < τ mais haut ≥ τ
    (ETAT_OK, JEU_OK, _pb((0.1, 0.09, 0.12), (0.08, 0.0, 0.2)), 6),                 # bas == 0 : pas > 0
    (ETAT_OK, JEU_OK, _pb((0.04, 0.001, 0.05), (0.1, 0.09, 0.12)), 6),              # haut == τ : pas < τ
])
def test_verdict_HR1_replication_lignes(etat, jeu, pb, ligne):
    r = ib.verdict_HR1_replication(etat, pb, jeu)
    assert r["ligne"] == ligne
    textes = {1: "non jugeable (santé)", 2: "non jugeable (jeu dégénéré)", 3: "répliquée",
              4: "non répliquée (signe inversé)", 5: "non répliquée (effet démontré inférieur à 0,05)",
              6: "non jugeable (imprécis)"}
    assert r["verdict"] == textes[ligne]


@pytest.mark.parametrize("etat, k, ligne", [
    (dict(ETAT_OK, T2=True), ("≈", "≈"), 1), (dict(ETAT_OK, T5=True), ("≈", "≈"), 1), (dict(ETAT_OK, T6=True), ("≈", "≈"), 1),
    (dict(ETAT_OK, T3=True), ("≈", "≈"), 4),                                           # T3 ne bloque pas HR0
    (ETAT_OK, ("R2 > R0", "≈"), 2), (ETAT_OK, ("≈", "R2 > R0"), 2), (ETAT_OK, ("R2 > R0", "R2 ≳ R0"), 2),
    (ETAT_OK, ("R2 ≳ R0", "≈"), 3), (ETAT_OK, ("R2 ≳ R0", "R0 > R2"), 3),
    (ETAT_OK, ("≈", "≈"), 4), (ETAT_OK, ("R0 ≳ R2", "R0 > R2"), 4), (ETAT_OK, ("≈", "R0 ≳ R2"), 4),
    (ETAT_OK, ("≈", "?"), 5), (ETAT_OK, ("?", "?"), 5),
])
def test_verdict_HR0_replication_lignes(etat, k, ligne):
    r = ib.verdict_HR0_replication(etat, {1: k[0], 2: k[1]})
    assert r["ligne"] == ligne
    assert r["verdict"] == {1: "non jugeable (santé)", 2: "non répliquée (le réentraînement l'emporte d'un effet d'intérêt)",
                            3: "non répliquée (le réentraînement l'emporte, effet démontré non nul)",
                            4: "répliquée", 5: "non jugeable (imprécis)"}[ligne]


@pytest.mark.parametrize("etat, k, ligne", [
    (dict(ETAT_OK, T2=True), ("R4 > R2", "R4 > R2"), 1), (dict(ETAT_OK, T5=True, T4=True), ("R4 > R2", "R4 > R2"), 1),
    (dict(ETAT_OK, T4=True), ("R4 > R2", "R4 > R2"), 2),
    (ETAT_OK, ("R2 > R4", "R4 > R2"), 3), (ETAT_OK, ("R4 > R2", "R2 ≳ R4"), 3),
    (ETAT_OK, ("R4 > R2", "≈"), 4), (ETAT_OK, ("R4 ≳ R2", "R4 ≳ R2"), 4),
    (ETAT_OK, ("R4 ≳ R2", "?"), 5), (ETAT_OK, ("?", "?"), 5),
])
def test_verdict_HR3_replication_lignes(etat, k, ligne):
    r = ib.verdict_HR3_replication(etat, {1: k[0], 2: k[1]})
    assert r["ligne"] == ligne
    assert r["verdict"] == {1: "non jugeable (santé)", 2: "sans verdict (R4 ≈ défense figée)", 3: "non répliquée",
                            4: "répliquée", 5: "non jugeable (imprécis)"}[ligne]


@pytest.mark.parametrize("etat, lg, ligne", [
    (dict(ETAT_OK, T2=True), (4, 4), 1), (dict(ETAT_OK, T6=True), (4, 4), 1), (dict(ETAT_OK, T4=True), (4, 4), 2),
    (ETAT_OK, (4, 4), 2), (ETAT_OK, (1, 4), 3), (ETAT_OK, (4, 2), 3), (ETAT_OK, (3, 5), 3),
    (ETAT_OK, (5, 4), 4), (ETAT_OK, (6, 6), 4), (ETAT_OK, (5, 5), 4),
])
def test_verdict_lois_tenues_ii_replication_lignes(etat, lg, ligne):
    r = ib.verdict_ii_replication(etat, {1: lg[0], 2: lg[1]})
    # T4 ne bloque pas ce verdict : (4, 4) avec T4 donne la ligne 2
    assert r["ligne"] == ligne
    assert r["verdict"] == {1: "non jugeable (santé)", 2: "répliquée", 3: "non répliquée (signe inversé)",
                            4: "non jugeable (imprécis)"}[ligne]


# =============================================================================================
# Écart de réplication et déclencheurs d'audit (§ 10.2)
# =============================================================================================
def _faux_contrastes(est, s):
    out = {}
    for c in "12":
        out[c] = {}
        for nom, mes in (("R3", "V"), ("R0", "V")):
            out[c][ib.libelle_contraste(nom, mes)] = {"moyenne": est, "ecart_type": s}
    return out


def _fausse_analyse(est, s):
    return {"resultat": {c: {"contrastes_contre_R2": {k: dict(v) for k, v in d.items()}}
                         for c, d in _faux_contrastes(est, s).items()}}


def test_sigma_et_z():
    assert ib.sigma_pi(0.06, 0.08) == pytest.approx(0.01)
    e = ib.ecart_replication(_faux_contrastes(0.13, 0.06), _fausse_analyse(0.10, 0.08))
    assert len(e) == 4
    for v in e.values():
        assert v["g"] == pytest.approx(0.03) and v["sigma"] == pytest.approx(0.01) and v["z"] == pytest.approx(3.0)
        assert v["est_or"] == 0.10 and v["s_or"] == 0.08 and v["est_rep"] == 0.13 and v["s_rep"] == 0.06


def test_z_non_defini_quand_sigma_nul():
    e = ib.ecart_replication(_faux_contrastes(0.2, 0.0), _fausse_analyse(0.1, 0.0))
    assert all(v["z"] is None and v["sigma"] == 0.0 for v in e.values())
    d = ib.declencheurs_audit(e, {"1": "≈", "2": "≈"}, {"HR1": {"verdict": "répliquée"}, "HR0": {"verdict": "répliquée"}})
    assert d["TR1_ecart_de_replication"] is True        # |g| > z* × 0


def test_TR1_dans_les_deux_sens_et_au_seuil():
    vb = {"HR1": {"verdict": "répliquée"}, "HR0": {"verdict": "répliquée"}}
    kappa = {"1": "≈", "2": "≈"}
    seuil = ib.Z_ETOILE * 0.01
    for signe in (+1, -1):
        e = ib.ecart_replication(_faux_contrastes(0.10 + signe * (seuil + 1e-6), 0.06), _fausse_analyse(0.10, 0.08))
        assert ib.declencheurs_audit(e, kappa, vb)["TR1_ecart_de_replication"] is True
        e = ib.ecart_replication(_faux_contrastes(0.10 + signe * (seuil - 1e-6), 0.06), _fausse_analyse(0.10, 0.08))
        assert ib.declencheurs_audit(e, kappa, vb)["TR1_ecart_de_replication"] is False


def test_TR1_se_declenche_sur_un_seul_contraste():
    c = _faux_contrastes(0.10, 0.06)
    c["2"][ib.libelle_contraste("R0", "V")]["moyenne"] = 0.10 + 0.05
    e = ib.ecart_replication(c, _fausse_analyse(0.10, 0.08))
    vb = {"HR1": {"verdict": "répliquée"}, "HR0": {"verdict": "répliquée"}}
    assert ib.declencheurs_audit(e, {"1": "≈", "2": "≈"}, vb)["TR1_ecart_de_replication"] is True


def test_TR2_trop_propre_exige_les_quatre_ecarts_petits_et_strictement():
    vb = {"HR1": {"verdict": "répliquée"}, "HR0": {"verdict": "répliquée"}}
    kappa = {"1": "≈", "2": "≈"}
    e = ib.ecart_replication(_faux_contrastes(0.1005, 0.06), _fausse_analyse(0.10, 0.08))
    assert ib.declencheurs_audit(e, kappa, vb)["TR2_trop_propre"] is True
    # un seul des quatre écarts dépasse 0,001 : TR2 exige que les quatre soient strictement sous 0,001
    for g_un, attendu in ((2.0 ** -10, True), (2.0 ** -9, False)):     # 0,000977 puis 0,001953 (exacts en binaire)
        c = _faux_contrastes(0.5, 0.06)
        c["1"][ib.libelle_contraste("R3", "V")]["moyenne"] = 0.5 + g_un
        e = ib.ecart_replication(c, _fausse_analyse(0.5, 0.08))
        assert e["(R3, V, c=1)"]["g"] == g_un
        assert ib.declencheurs_audit(e, kappa, vb)["TR2_trop_propre"] is attendu


@pytest.mark.parametrize("kappa, attendu", [
    ({"1": "R0 > R2", "2": "≈"}, True), ({"1": "≈", "2": "R0 ≳ R2"}, True), ({"1": "≈", "2": "≈"}, False),
    ({"1": "R2 > R0", "2": "R2 ≳ R0"}, False), ({"1": "?", "2": "R0 ≳ R2"}, True), ({"1": "R0 > R2", "2": "R0 > R2"}, True),
])
def test_TR3_defense_figee_plus_belle(kappa, attendu):
    e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
    vb = {"HR1": {"verdict": "répliquée"}, "HR0": {"verdict": "répliquée"}}
    assert ib.declencheurs_audit(e, kappa, vb)["TR3_defense_figee_plus_belle"] is attendu


@pytest.mark.parametrize("v1, v0, attendu", [
    ("non répliquée (signe inversé)", "répliquée", True), ("répliquée", "non répliquée (le réentraînement l'emporte d'un effet d'intérêt)", True),
    ("répliquée", "répliquée", False), ("non jugeable (imprécis)", "non jugeable (santé)", False),
    ("non répliquée (effet démontré inférieur à 0,05)", "non jugeable (imprécis)", True),
])
def test_TR4_non_replication(v1, v0, attendu):
    e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
    d = ib.declencheurs_audit(e, {"1": "≈", "2": "≈"}, {"HR1": {"verdict": v1}, "HR0": {"verdict": v0}})
    assert d["TR4_non_replication"] is attendu


def test_effet_des_declencheurs_et_hr2_non_concerne():
    vb = {"HR1": {"verdict": "répliquée"}, "HR0": {"verdict": "répliquée"}, "HR3": {"verdict": "répliquée"},
          "lois_tenues_ii": {"verdict": "répliquée"}}
    assert ib.verdicts_apres_declencheurs(vb, {"au_moins_un": False}) == {
        "HR1": "répliquée", "HR0": "répliquée", "HR3": "répliquée", "lois_tenues_ii": "répliquée"}
    apres = ib.verdicts_apres_declencheurs(vb, {"au_moins_un": True})
    assert set(apres) == {"HR1", "HR0", "HR3", "lois_tenues_ii"} and set(apres.values()) == {"non jugeable (audit en attente)"}


def test_analyse_originale_absente_d_un_contraste_est_un_arret():
    with pytest.raises(ib.Arret):
        ib.ecart_replication(_faux_contrastes(0.1, 0.06), {"resultat": {"1": {"contrastes_contre_R2": {}}, "2": {}}})


# =============================================================================================
# Issue globale (§ 10.4)
# =============================================================================================
@pytest.mark.parametrize("hr1, hr0, kw, ligne", [
    ("répliquée", "répliquée", dict(plomberie_fausse=True), 1),
    ("répliquée", "répliquée", dict(arret=True), 1),
    ("répliquée", "répliquée", dict(discordance_ab=True), 1),
    ("non répliquée (signe inversé)", "répliquée", dict(arret=True), 1),               # la ligne 1 passe avant la ligne 4
    ("non jugeable (audit en attente)", "répliquée", {}, 2),
    ("répliquée", "non jugeable (audit en attente)", {}, 2),
    ("non jugeable (artefact)", "répliquée", {}, 3),
    ("répliquée", "non jugeable (artefact)", {}, 3),
    ("non jugeable (audit en attente)", "non jugeable (artefact)", {}, 2),              # ligne 2 avant ligne 3
    ("non répliquée (signe inversé)", "répliquée", {}, 4),
    ("non répliquée (effet démontré inférieur à 0,05)", "non jugeable (imprécis)", {}, 4),
    ("répliquée", "répliquée", {}, 5),
    ("répliquée", "non répliquée (le réentraînement l'emporte d'un effet d'intérêt)", {}, 6),
    ("répliquée", "non répliquée (le réentraînement l'emporte, effet démontré non nul)", {}, 6),
    ("répliquée", "non jugeable (imprécis)", {}, 7),
    ("répliquée", "non jugeable (santé)", {}, 7),
    ("non jugeable (imprécis)", "répliquée", {}, 8),
    ("non jugeable (santé)", "non jugeable (santé)", {}, 8),
])
def test_issue_globale_lignes(hr1, hr0, kw, ligne):
    r = ib.issue_globale(hr1, hr0, **kw)
    assert r["ligne"] == ligne and r["issue"] == ib.ISSUES[ligne]


# =============================================================================================
# Contrôle « graines neuves » (§ 10.3)
# =============================================================================================
def _donnees_v(valeurs):
    return {c: {"champs": {nom: {"V_iii_final": np.array(valeurs[(c, nom)], dtype=float)} for nom in ib.NOMS_VARIANTES}}
            for c in (1, 2)}


def test_graines_neuves_egalite_au_bit():
    base = {(c, nom): np.linspace(0.1, 0.2, 100) for c in (1, 2) for nom in ib.NOMS_VARIANTES}
    autre = {k: v + 1e-3 for k, v in base.items()}
    assert set(ib.comptes_graines_neuves(_donnees_v(base), _donnees_v(autre)).values()) == {0}
    assert set(ib.comptes_graines_neuves(_donnees_v(base), _donnees_v(base)).values()) == {200}
    # 0.0 et -0.0 sont égaux en valeur mais pas au bit
    z = {k: np.zeros(100) for k in base}
    nz = {k: -np.zeros(100) for k in base}
    assert set(ib.comptes_graines_neuves(_donnees_v(z), _donnees_v(nz)).values()) == {0}
    # un seul bit de différence
    d = {k: v.copy() for k, v in base.items()}
    d[(1, "R3")][5] = np.nextafter(d[(1, "R3")][5], 1.0)
    cpt = ib.comptes_graines_neuves(_donnees_v(base), _donnees_v(d))
    assert cpt["R3"] == 199 and cpt["R0"] == 200


def test_graines_neuves_seuil_strictement_superieur_a_10(b_petit, analyse_a):
    e1 = fabriquer_e1(1)
    e4 = copy.deepcopy(e1)
    cibles = {"R0": 10, "R1": 11}       # nombre de tâches (budget 1) laissées identiques à E1
    for t in taches_de(e4):
        for nom, m in cibles.items():
            if not (t["code_delta"] == 1 and t["instance"] < m):
                v = t["regles"][nom]
                v["V_iii_standard"] += 0.001
                v["V_iii_renforce"] += 0.001
                v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
        for nom in ("R2", "R3", R4):    # décalage total : zéro égalité
            v = t["regles"][nom]
            v["V_iii_standard"] += 0.002
            v["V_iii_renforce"] += 0.002
            v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
    r = ib.analyser_donnees(e1, 20266201, e4_analyse=analyse_a, e4_resultats=e4)
    comptes = r["comptes_graines_neuves"]
    assert comptes["comptes"]["R0"] == 10 and comptes["comptes"]["R1"] == 11 and comptes["comptes"]["R3"] == 0
    assert comptes["variantes_au_dessus_du_seuil"] == ["R1"] and comptes["arret_graines_non_neuves"] is True
    assert r["lecture_autorisee"] is False and len(r["arrets"]) == 1
    # à 10 exactement : pas d'arrêt
    cibles["R1"] = 10
    e4b = copy.deepcopy(e1)
    for t in taches_de(e4b):
        for nom in ib.NOMS_VARIANTES:
            if not (t["code_delta"] == 1 and t["instance"] < 10 and nom in ("R0", "R1")):
                v = t["regles"][nom]
                v["V_iii_standard"] += 0.001
                v["V_iii_renforce"] += 0.001
                v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
    r = ib.analyser_donnees(e1, 20266201, e4_analyse=analyse_a, e4_resultats=e4b)
    assert r["comptes_graines_neuves"]["comptes"]["R0"] == 10 and r["comptes_graines_neuves"]["comptes"]["R1"] == 10
    assert r["comptes_graines_neuves"]["arret_graines_non_neuves"] is False and r["lecture_autorisee"] is True


# =============================================================================================
# Contrôles de santé sur pièces synthétiques (§ 7)
# =============================================================================================
def _analyse_synth(b_petit_fixture=None, **kw):
    e1 = fabriquer_e1(**kw)
    return ib.analyser_donnees(e1, 20266201)


def test_synthetique_sain(b_petit):
    r = _analyse_synth(graine=5)
    assert r["sante"]["etat_global"] == {"T2": False, "T3": False, "T4": False, "T5": False, "T6": False}
    assert r["verdicts_regles_originales"]["HR1"]["verdict"] == "HR1 confirmée"
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "répliquée"
    assert r["issue_globale_brute"] is None and r["lecture_autorisee"] is True


def test_T3_melange_degenere_strictement_plus_de_50_taches(b_petit):
    assert _analyse_synth(graine=6, nb_poids_purs=50)["sante"]["1"]["T3"]["nb_taches_poids_pur"] == 50
    assert _analyse_synth(graine=6, nb_poids_purs=50)["sante"]["etat_global"]["T3"] is False
    r = _analyse_synth(graine=6, nb_poids_purs=51)
    assert r["sante"]["1"]["T3"]["declenche"] and r["sante"]["etat_global"]["T3"]
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "non jugeable (santé)"
    assert r["verdicts_bruts_replication"]["HR0"]["verdict"] != "non jugeable (santé)"      # T3 ne bloque que HR1


def test_T3_poids_a_un_moins_epsilon():
    e1 = fabriquer_e1(7, melanger=False)
    for c, i in ((1, 0), (1, 1), (1, 2)):
        w = [0.0] * 9
        w[0] = 1.0 - (1e-9 if i == 0 else (2e-9 if i == 1 else 0.5e-9))
        w[1] = 1.0 - w[0]
        tache(e1, c, i)["regles"]["R3"]["poids_finaux"] = w
    donnees = ib.extraire_donnees(sorted([t for t in taches_de(e1) if t["code_delta"] == 1], key=lambda t: t["instance"]), 1)
    nb = sum(1 for w in donnees["poids_R3"] if max(w) >= ib.SEUIL_T3_POIDS_PUR)
    assert nb == 2          # 1 − 1e-9 inclus (≥), 1 − 2e-9 exclu, 1 − 0,5e-9 inclus


def test_T4_regularisation_degeneree_ne_bloque_que_HR3(b_petit):
    r = _analyse_synth(graine=8, nb_cos_eleves=51)
    assert r["sante"]["1"]["T4"]["nb_taches_cos_moyen_ge_0_999"] == 51 and r["sante"]["etat_global"]["T4"]
    vb = r["verdicts_bruts_replication"]
    assert vb["HR3"]["verdict"] == "sans verdict (R4 ≈ défense figée)"
    assert vb["HR1"]["verdict"] == "répliquée"
    assert r["verdicts_regles_originales"]["HR3"]["verdict"] == "sans verdict (R4 ≈ défense figée)"
    r = _analyse_synth(graine=8, nb_cos_eleves=50)
    assert r["sante"]["etat_global"]["T4"] is False


def test_T4_un_seul_budget_suffit(b_petit):
    e1 = fabriquer_e1(9, melanger=False)
    for t in taches_de(e1):
        if t["code_delta"] == 2 and t["instance"] < 60:
            t["regles"][R4]["par_tour"]["cos_consecutif"] = [1.0] * 8
    r = ib.analyser_donnees(e1, 20266201)
    assert r["sante"]["1"]["T4"]["declenche"] is False and r["sante"]["2"]["T4"]["declenche"] is True
    assert r["sante"]["etat_global"]["T4"] is True


def test_T5_optimiseur_deux_conditions(b_petit):
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):                                   # R3 : standard − renforcé > 0,01
        v = t["regles"]["R3"]
        v["V_iii_standard"] = v["V_iii_renforce"] + 0.02
        v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
    r = ib.analyser_donnees(e1, 20266201)
    assert r["sante"]["1"]["T5"]["declenche"] and r["sante"]["etat_global"]["T5"]
    # condition de contraste : (standard − renforcé) de R0 et de R2 décalés de la même façon -> a − b = 0 pour R0, mais
    # standard − renforcé > 0,01 pour les deux variantes : la première condition est la seule à répondre
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):
        for nom in ("R2",):
            v = t["regles"][nom]
            v["V_iii_standard"] = min(1.0, v["V_iii_renforce"] + 0.02)
            v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
    r = ib.analyser_donnees(e1, 20266201)
    assert r["sante"]["1"]["T5"]["declenche"]      # R2 : standard − renforcé = 0,02 > 0,01
    # standard − renforcé NÉGATIF et grand : la première condition n'est pas bilatérale (« > 0,01 ») ; le contraste l'est
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):
        for nom in ib.NOMS_VARIANTES:
            v = t["regles"][nom]
            v["V_iii_standard"] = max(0.0, v["V_iii_renforce"] - 0.05)
            v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
    r = ib.analyser_donnees(e1, 20266201)
    assert min(r["sante"]["1"]["T5"]["standard_moins_renforce"].values()) < -0.01
    assert r["sante"]["1"]["T5"]["declenche"] is False       # contraste a−b ≈ 0 et première condition unilatérale
    # condition 2 seule : un décalage de standard sur R3 seul, compensé pour garder standard − renforcé ≤ 0,01 sur R3 ?
    # (|a − b| > 0,01 avec standard − renforcé ≤ 0,01 exige que R2 ait un écart négatif)
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):
        v2, v3 = t["regles"]["R2"], t["regles"]["R3"]
        v2["V_iii_standard"] = max(0.0, v2["V_iii_renforce"] - 0.03)
        v2["V_iii_final"] = min(v2["V_iii_standard"], v2["V_iii_renforce"])
        v3["V_iii_standard"] = v3["V_iii_renforce"] + 0.005
        v3["V_iii_final"] = min(v3["V_iii_standard"], v3["V_iii_renforce"])
    r = ib.analyser_donnees(e1, 20266201)
    t5 = r["sante"]["1"]["T5"]
    assert max(t5["standard_moins_renforce"].values()) <= 0.01 and t5["plus_grand_abs_ecart_de_contraste"] > 0.01
    assert t5["declenche"] is True


def test_T6_derive_des_fausses_alertes(b_petit):
    assert _analyse_synth(graine=11, derive_fpr=0.0)["sante"]["etat_global"]["T6"] is False
    assert _analyse_synth(graine=11, derive_fpr=0.002)["sante"]["etat_global"]["T6"] is True
    assert _analyse_synth(graine=11, derive_fpr=-0.002)["sante"]["etat_global"]["T6"] is True     # bilatéral
    r = _analyse_synth(graine=11, derive_fpr=0.002)
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "non jugeable (santé)"
    assert r["verdicts_bruts_replication"]["HR0"]["verdict"] == "non jugeable (santé)"
    assert r["verdicts_bruts_replication"]["HR3"]["verdict"] == "non jugeable (santé)"
    assert r["verdicts_bruts_replication"]["lois_tenues_ii"]["verdict"] == "non jugeable (santé)"


def test_T2_les_quatre_conditions(b_petit):
    # trop beau : une variante avec moyenne de V >= 0,99
    e1 = fabriquer_e1(12)
    for t in taches_de(e1):
        v = t["regles"]["R0"]
        v["V_iii_standard"] = v["V_iii_renforce"] = v["V_iii_final"] = 0.995
    r = ib.analyser_donnees(e1, 20266201)
    assert r["sante"]["1"]["T2"]["une_variante_moy_V_ge_0_99"] and r["sante"]["etat_global"]["T2"]
    # jeu trop mauvais : les cinq moyennes de V <= 0,02
    e1 = fabriquer_e1(12)
    for t in taches_de(e1):
        for nom in ib.NOMS_VARIANTES:
            v = t["regles"][nom]
            v["V_iii_standard"] = v["V_iii_renforce"] = v["V_iii_final"] = 0.01
    r = ib.analyser_donnees(e1, 20266201)
    assert r["sante"]["1"]["T2"]["cinq_variantes_moy_V_le_0_02"] and r["sante"]["1"]["jeu_degenere"]
    # la ligne « jeu dégénéré » du HR1 est masquée par la ligne « santé » (T2 contient la même condition)
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "non jugeable (santé)"
    assert r["classes"]["table_A"]["classe"] == "non concluant : jeu dégénéré"
    # est de (R3, V) > 0,30
    r = _analyse_synth(graine=12, effet_r3=0.35)
    assert r["sante"]["1"]["T2"]["est_R3_V_gt_0_30"] and r["sante"]["etat_global"]["T2"]
    # |est(k, X̄)| > 0,30 pour une variante autre que R2
    e1 = fabriquer_e1(12)
    for t in taches_de(e1):
        t["regles"]["R1"]["exploitabilite_moyenne_tours"] = 1.0
        t["regles"]["R2"]["exploitabilite_moyenne_tours"] = 0.2
    r = ib.analyser_donnees(e1, 20266201)
    assert r["sante"]["1"]["T2"]["un_abs_est_Xbarre_gt_0_30"]
    # bilatéral : -0,5
    e1 = fabriquer_e1(12)
    for t in taches_de(e1):
        t["regles"]["R1"]["exploitabilite_moyenne_tours"] = 0.2
        t["regles"]["R2"]["exploitabilite_moyenne_tours"] = 0.8
    assert ib.analyser_donnees(e1, 20266201)["sante"]["1"]["T2"]["un_abs_est_Xbarre_gt_0_30"]


# =============================================================================================
# Gardes d'entrée : chacune est un arrêt (§ 5.1, § 5.2, § 7)
# =============================================================================================
def _doit_arreter(e1, **kw):
    with pytest.raises(ib.Arret):
        ib.analyser_donnees(e1, 20266201, **kw)


def test_gardes_structure(b_petit):
    base = fabriquer_e1(20)
    ib.analyser_donnees(base, 20266201)       # la pièce de départ est saine

    e1 = copy.deepcopy(base)
    e1["resultat"]["resultats"].pop()                                          # 199 tâches
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    tache(e1, 1, 7)["instance"] = 8                                            # instance en double (et 7 manquante)
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    tache(e1, 2, 3)["instance"] = 100                                          # instance hors de 0..99
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    tache(e1, 1, 3)["instance"] = 3.0                                          # entier attendu
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    tache(e1, 1, 3)["instance"] = True
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    tache(e1, 1, 3)["code_delta"] = 3
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    tache(e1, 1, 3)["code_delta"] = 2                                          # 99 tâches au budget 1, 101 au budget 2
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    del tache(e1, 1, 3)["config_sha256"]
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    e1["clef_en_trop"] = 1
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    e1["resultat"]["cle_en_plus"] = {}                                         # `resultat` « contient » : lu « au moins »
    ib.analyser_donnees(e1, 20266201)

    e1 = copy.deepcopy(base)
    del e1["resultat"]["temps"]
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    del e1["run_id"]
    _doit_arreter(e1)


def test_gardes_variantes(b_petit):
    base = fabriquer_e1(21)
    e1 = copy.deepcopy(base)
    del tache(e1, 1, 3)["regles"]["R1"]
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    tache(e1, 1, 3)["regles"]["R5"] = copy.deepcopy(tache(e1, 1, 3)["regles"]["R1"])
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    t = tache(e1, 2, 9)
    r = t["regles"]
    t["regles"] = {"R1": r["R0"], "R0": r["R1"], "R2": r["R2"], "R3": r["R3"], R4: r[R4]}   # ordre des clés
    _doit_arreter(e1)

    e1 = copy.deepcopy(base)
    t = tache(e1, 2, 9)
    t["regles"]["R4[moyenne,lambda=0.3]"] = t["regles"].pop(R4)            # nom de variante différent
    _doit_arreter(e1)


@pytest.mark.parametrize("champ", ["V_iii_final", "ii_final", "exploitabilite_finale", "exploitabilite_moyenne_tours"])
def test_gardes_intervalle_0_1_a_1e_12_pres(b_petit, champ):
    base = fabriquer_e1(22)
    for valeur, doit in ((1.0 + 5e-13, False), (-5e-13, False), (1.0 + 2e-12, True), (-2e-12, True), (1.5, True)):
        e1 = copy.deepcopy(base)
        v = tache(e1, 1, 4)["regles"]["R2"]
        v[champ] = valeur
        if champ == "V_iii_final":
            v["V_iii_standard"] = v["V_iii_renforce"] = valeur
        if doit:
            _doit_arreter(e1)
        else:
            ib.analyser_donnees(e1, 20266201)


@pytest.mark.parametrize("valeur", [float("nan"), float("inf"), -float("inf"), "0.5", None, True])
def test_gardes_valeurs_non_finies_ou_mal_typees(b_petit, valeur):
    for champ in ("V_iii_standard", "ii_final", "fpr_final", "V_iii_renforce"):
        e1 = fabriquer_e1(23)
        tache(e1, 1, 4)["regles"]["R3"][champ] = valeur
        _doit_arreter(e1)


def test_garde_de_coherence_de_V(b_petit):
    e1 = fabriquer_e1(24)
    v = tache(e1, 2, 4)["regles"]["R0"]
    v["V_iii_final"] = np.nextafter(v["V_iii_final"], 1.0)         # un seul bit de différence avec min(standard, renforcé)
    _doit_arreter(e1)
    e1 = fabriquer_e1(24)
    v = tache(e1, 1, 4)["regles"]["R3"]
    v["V_iii_final"] = max(v["V_iii_standard"], v["V_iii_renforce"]) + 0.001
    _doit_arreter(e1)


def test_gardes_poids_et_cosinus(b_petit):
    e1 = fabriquer_e1(25)
    tache(e1, 1, 4)["regles"]["R3"]["poids_finaux"] = []
    _doit_arreter(e1)
    e1 = fabriquer_e1(25)
    tache(e1, 1, 4)["regles"]["R3"]["poids_finaux"] = [0.5, float("nan")]
    _doit_arreter(e1)
    e1 = fabriquer_e1(25)
    tache(e1, 1, 4)["regles"][R4]["par_tour"]["cos_consecutif"] = [0.1] * 7
    _doit_arreter(e1)
    e1 = fabriquer_e1(25)
    tache(e1, 1, 4)["regles"][R4]["par_tour"]["cos_consecutif"] = [0.1] * 9
    _doit_arreter(e1)
    e1 = fabriquer_e1(25)
    del tache(e1, 1, 4)["regles"][R4]["par_tour"]
    _doit_arreter(e1)


def test_la_lecture_json_refuse_les_cles_dupliquees_et_le_json_invalide():
    with pytest.raises(ib.Arret):
        ib.lire_json_octets(b'{"a": 1, "a": 2}', "test")
    with pytest.raises(ib.Arret):
        ib.lire_json_octets(b'{"a": ', "test")
    with pytest.raises(ib.Arret):
        ib.lire_json_octets(b"\xff\xfe", "test")


def test_lecture_exacte_des_entiers_de_64_bits_et_des_decimaux():
    obj = ib.lire_json_octets(b'{"r": 18446744073709551615, "x": 0.1, "y": 1e-9, "z": 11786724493248295725}', "t")
    assert obj["r"] == 2 ** 64 - 1 and isinstance(obj["r"], int)
    assert obj["z"] == 11786724493248295725
    assert obj["x"] == 0.1 and obj["y"] == 1e-9


# =============================================================================================
# Fichiers, empreintes, compagnons (§ 3)
# =============================================================================================
def test_empreinte_et_compagnon(tmp_path):
    f = tmp_path / "pieces.json"
    sha = ecrire_avec_compagnon(f, b'{"a": 1}')
    octets, s = ib.lire_fichier_verifie(f, "t")
    assert octets == b'{"a": 1}' and s == sha
    avert = []
    (tmp_path / "pieces.json.sha256").write_text(f"{sha}  autre-nom.json\n", encoding="utf-8")
    ib.lire_fichier_verifie(f, "t", avertissements=avert)
    assert len(avert) == 1                                                       # nom différent : simple avertissement
    f.write_bytes(b'{"a": 2}')                                                   # fichier modifié après scellement
    with pytest.raises(ib.Arret):
        ib.lire_fichier_verifie(f, "t")


@pytest.mark.parametrize("contenu", ["", "abc  pieces.json\n", "A" * 64 + "  pieces.json\n", "0" * 64 + " pieces.json\n",
                                     "0" * 64 + "  pieces.json\n" + "0" * 64 + "  pieces.json\n", "0" * 64 + "\n"])
def test_compagnon_mal_forme(tmp_path, contenu):
    f = tmp_path / "pieces.json"
    f.write_bytes(b"{}")
    Path(str(f) + ".sha256").write_text(contenu, encoding="utf-8")
    with pytest.raises(ib.Arret):
        ib.lire_fichier_verifie(f, "t")


def test_compagnon_absent_et_fichier_absent(tmp_path):
    f = tmp_path / "pieces.json"
    f.write_bytes(b"{}")
    with pytest.raises(ib.Arret):
        ib.lire_fichier_verifie(f, "t")
    with pytest.raises(ib.Arret):
        ib.lire_fichier_verifie(tmp_path / "inexistant.json", "t", attendue="0" * 64)


def test_compagnon_sans_extension_est_accepte(tmp_path):
    f = tmp_path / "pieces.json"
    f.write_bytes(b"{}")
    (tmp_path / "pieces.sha256").write_text(f"{hashlib.sha256(b'{}').hexdigest()}  pieces.json\n", encoding="utf-8")
    ib.lire_fichier_verifie(f, "t")


def test_E1_sans_compagnon_ni_empreinte_est_un_arret(tmp_path):
    e1 = fabriquer_e1(30)
    f = tmp_path / "res.json"
    f.write_text(json.dumps(e1), encoding="utf-8")
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(resultats=f, racine=1234567)


def test_E4_alteree_est_un_arret(tmp_path):
    e1 = fabriquer_e1(31)
    f = tmp_path / "res.json"
    ecrire_avec_compagnon(f, json.dumps(e1).encode("utf-8"))
    altere = tmp_path / "analyse-alteree.json"
    altere.write_bytes(P_ANA.read_bytes().replace(b"0.10448042252007811", b"0.10448042252007812"))
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(resultats=f, racine=1234567, analyse_originale=altere)


# =============================================================================================
# Mode réplication de bout en bout (pièces synthétiques + vraie course originale comme E4)
# =============================================================================================
def _monter_replication(tmp_path, *, texte=None, avec_companions=True, **kw_e1):
    """Fabrique E3 (préenregistrement), E2 (manifeste), E1 (résultats) cohérents avec la règle D."""
    texte = texte or "Préenregistrement de réplication — texte de test (λ).\n"
    octets3 = texte.encode("utf-8")
    h = hashlib.sha256(octets3).hexdigest()
    rho, rho_t = ib.regle_d(h)
    e3 = tmp_path / "prereg-replication-v1.md"
    e3.write_bytes(octets3)
    e2d = {"config": {"racine": rho, "racine_tenue": rho_t, "prereg_sha256": h, "lambda": 0.3, "reference": "moyenne",
                      "config": {"n_instances": 100}}, "preenregistrement": {"sha256": h}}
    e2 = tmp_path / "manifeste.json"
    e2.write_bytes(json.dumps(e2d).encode("utf-8"))
    e1d = fabriquer_e1(rho=rho, rho_t=rho_t, **kw_e1)
    e1 = tmp_path / "resultats-replication.json"
    e1.write_bytes(json.dumps(e1d).encode("utf-8"))
    if avec_companions:
        for f in (e3, e2, e1):
            Path(str(f) + ".sha256").write_text(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n", encoding="utf-8")
    return dict(e1=e1, e2=e2, e3=e3, h=h, rho=rho, rho_t=rho_t, e1d=e1d, e2d=e2d)


def _lancer(m, **extra):
    return ib.analyser_fichiers(resultats=m["e1"], prereg=m["e3"], manifeste=m["e2"], analyse_originale=P_ANA,
                                resultats_originaux=P_RES, **extra)


def test_replication_de_bout_en_bout(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=40)
    r = _lancer(m)
    assert r["mode"].startswith("réplication") and r["empreinte_H"] == m["h"]
    assert r["racines"]["rho"] == str(m["rho"]) and r["racines"]["rho_t"] == str(m["rho_t"])
    assert isinstance(r["racines"]["rho"], str) and r["racine_de_reechantillonnage"] == str(m["rho"])
    assert r["racines_lues_dans_E1"] == {"racine": [m["rho"]], "racine_tenue": [m["rho_t"]]}
    assert r["lecture_autorisee"] is True and r["arrets"] == []
    assert r["comptes_graines_neuves"]["arret_graines_non_neuves"] is False
    assert all(v < 10 for v in r["comptes_graines_neuves"]["comptes"].values())
    roles = [f["role"] for f in r["empreintes_fichiers"]]
    assert len(roles) == 5 and any("E3" in x for x in roles) and any("E2" in x for x in roles)
    assert r["issue_globale_brute"]["ligne"] in range(2, 9) and r["issue_globale_apres_declencheurs"]["ligne"] in range(2, 9)
    assert set(r["verdicts_bruts_replication"]) >= {"HR1", "HR0", "HR3", "lois_tenues_ii", "HR2"}
    assert len(r["ecart_de_replication"]["contrastes_primaires"]) == 4
    json.dumps(r, allow_nan=False)           # sortie entièrement sérialisable


def test_replication_les_racines_servent_au_reechantillonnage(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=41)
    r = _lancer(m)
    r2 = ib.analyser_donnees(m["e1d"], m["rho"])
    r3 = ib.analyser_donnees(m["e1d"], m["rho"] + 1)
    lib = "R3 - R2 (V_iii_final)"
    assert r["resultat"]["1"]["contrastes_contre_R2"][lib] == r2["resultat"]["1"]["contrastes_contre_R2"][lib]
    assert r["resultat"]["1"]["contrastes_contre_R2"][lib]["quantiles"] != r3["resultat"]["1"]["contrastes_contre_R2"][lib]["quantiles"]
    assert r["resultat"]["1"]["contrastes_contre_R2"][lib]["moyenne"] == r3["resultat"]["1"]["contrastes_contre_R2"][lib]["moyenne"]


def test_replication_arret_si_le_manifeste_ment_sur_les_racines(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=42)
    for cle, val in (("racine", m["rho"] + 1), ("racine_tenue", m["rho_t"] + 1)):
        d = copy.deepcopy(m["e2d"])
        d["config"][cle] = val
        m["e2"].write_bytes(json.dumps(d).encode("utf-8"))
        Path(str(m["e2"]) + ".sha256").write_text(f"{hashlib.sha256(m['e2'].read_bytes()).hexdigest()}  {m['e2'].name}\n")
        with pytest.raises(ib.Arret):
            _lancer(m)


def test_replication_arret_si_le_manifeste_ne_donne_pas_H(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=43)
    d = copy.deepcopy(m["e2d"])
    d["preenregistrement"]["sha256"] = "0" * 64
    m["e2"].write_bytes(json.dumps(d).encode("utf-8"))
    Path(str(m["e2"]) + ".sha256").write_text(f"{hashlib.sha256(m['e2'].read_bytes()).hexdigest()}  {m['e2'].name}\n")
    with pytest.raises(ib.Arret):
        _lancer(m)


def test_replication_arret_si_une_tache_porte_une_autre_racine(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=44)
    e1d = copy.deepcopy(m["e1d"])
    tache(e1d, 2, 50)["racine"] = 20266201
    m["e1"].write_bytes(json.dumps(e1d).encode("utf-8"))
    Path(str(m["e1"]) + ".sha256").write_text(f"{hashlib.sha256(m['e1'].read_bytes()).hexdigest()}  {m['e1'].name}\n")
    with pytest.raises(ib.Arret):
        _lancer(m)
    e1d = copy.deepcopy(m["e1d"])
    tache(e1d, 1, 0)["racine_tenue"] = m["rho_t"] + 1
    m["e1"].write_bytes(json.dumps(e1d).encode("utf-8"))
    Path(str(m["e1"]) + ".sha256").write_text(f"{hashlib.sha256(m['e1'].read_bytes()).hexdigest()}  {m['e1'].name}\n")
    with pytest.raises(ib.Arret):
        _lancer(m)


def test_replication_arret_si_le_texte_scelle_a_change(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=45)
    m["e3"].write_bytes(m["e3"].read_bytes() + b" ")          # le compagnon ne correspond plus
    with pytest.raises(ib.Arret):
        _lancer(m)


def test_replication_arret_sans_compagnons_ou_sans_E4(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=46, avec_companions=False)
    with pytest.raises(ib.Arret):
        _lancer(m)
    (tmp_path / "bis").mkdir()
    m = _monter_replication(tmp_path / "bis", graine=47)
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(resultats=m["e1"], prereg=m["e3"], manifeste=m["e2"])
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(resultats=m["e1"], prereg=m["e3"])
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(resultats=m["e1"], racine=5, prereg=m["e3"], manifeste=m["e2"],
                             analyse_originale=P_ANA, resultats_originaux=P_RES)
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(resultats=m["e1"])


def test_replication_avertit_sur_lambda_reference_et_n_instances(tmp_path, b_petit):
    m = _monter_replication(tmp_path, graine=48)
    d = copy.deepcopy(m["e2d"])
    d["config"]["lambda"] = 0.5
    d["config"]["config"]["n_instances"] = 50
    d["config"]["prereg_sha256"] = "1" * 64
    m["e2"].write_bytes(json.dumps(d).encode("utf-8"))
    Path(str(m["e2"]) + ".sha256").write_text(f"{hashlib.sha256(m['e2'].read_bytes()).hexdigest()}  {m['e2'].name}\n")
    r = _lancer(m)
    assert len(r["avertissements"]) == 3


# =============================================================================================
# Ligne de commande
# =============================================================================================
def _cli(*args):
    return subprocess.run([sys.executable, str(DOSSIER / "implementation_b.py"), *map(str, args)],
                          capture_output=True, text=True, encoding="utf-8")


def test_cli_analyser_la_course_originale_sans_essai_contre_elle_meme(tmp_path):
    sortie = tmp_path / "sortie.json"
    p = _cli("analyser", "--resultats", P_RES, "--racine", 20266201, "--sortie", sortie)
    assert p.returncode == 0, p.stderr
    r = json.loads(sortie.read_text(encoding="utf-8"))
    assert r["lecture_autorisee"] is True and r["ecart_de_replication"] is None
    assert r["verdicts_regles_originales"]["HR1"]["verdict"] == "HR1 confirmée"
    # jamais écrasé
    p2 = _cli("analyser", "--resultats", P_RES, "--racine", 20266201, "--sortie", sortie)
    assert p2.returncode == 4 and "existe déjà" in p2.stderr


def test_cli_essai_contre_elle_meme_rend_le_code_3_mais_ecrit_la_sortie(tmp_path):
    sortie = tmp_path / "sortie-3.json"
    p = _cli("analyser", "--resultats", P_RES, "--racine", 20266201, "--analyse-originale", P_ANA,
             "--resultats-originaux", P_RES, "--sortie", sortie)
    assert p.returncode == 3 and "graines non neuves" in p.stderr
    r = json.loads(sortie.read_text(encoding="utf-8"))
    assert r["lecture_autorisee"] is False and r["comptes_graines_neuves"]["arret_graines_non_neuves"] is True


def test_cli_arret_ne_laisse_aucune_sortie(tmp_path):
    f = tmp_path / "res.json"
    f.write_bytes(P_RES.read_bytes()[:-5])                      # tronqué : empreinte fausse
    sortie = tmp_path / "sortie-arret.json"
    p = _cli("analyser", "--resultats", f, "--racine", 20266201, "--sortie", sortie)
    assert p.returncode == 2 and "ARRÊT" in p.stderr and not sortie.exists()


def test_cli_regle_d(tmp_path):
    p = _cli("regle-d", "--empreinte", "d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d")
    out = json.loads(p.stdout)
    assert out["rho"] == "11786724493248295725" and out["rho_t"] == "9136419304016434890"
    assert p.returncode == 2 and out["gardes"].startswith("ARRÊT")       # ce sont des entiers interdits comme racines
    f = tmp_path / "p.md"
    ecrire_avec_compagnon(f, "texte sain\n".encode("utf-8"))
    p = _cli("regle-d", "--prereg", f)
    out = json.loads(p.stdout)
    assert p.returncode == 0 and out["gardes"] == "ok" and out["H"] == hashlib.sha256(b"texte sain\n").hexdigest()
    assert out["E_decimal"] == str(int(out["H"], 16))


# =============================================================================================
# Comparaison avec la référence (§ 11)
# =============================================================================================
def test_comparer_detecte_une_discordance_sur_un_contraste_a_arret(sortie_originale, analyse_a):
    a = copy.deepcopy(analyse_a)
    a["resultat"]["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]["quantiles"]["q0.00625"] += 5e-9
    cmp_ = ib.comparer_a_reference(sortie_originale, a, analyse_a)
    assert cmp_["discordance_a_arret"] is True and cmp_["concordance"] is False
    assert cmp_["ecart_maximal_absolu_contrastes_a_arret"] == pytest.approx(5e-9, rel=1e-3)


def test_comparer_tolere_moins_de_epsilon(sortie_originale, analyse_a):
    a = copy.deepcopy(analyse_a)
    a["resultat"]["2"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"]["moyenne"] += 5e-10
    a["resultat"]["2"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"]["ecart_type"] += 5e-10
    cmp_ = ib.comparer_a_reference(sortie_originale, a, analyse_a)
    assert cmp_["discordance_a_arret"] is False and cmp_["concordance"] is True


def test_comparer_alerte_sur_les_onze_autres_contrastes(sortie_originale, analyse_a):
    a = copy.deepcopy(analyse_a)
    lib = "R3 - R2 (exploitabilite_finale)"
    a["resultat"]["1"]["contrastes_contre_R2"][lib]["quantiles"]["q0.95"] += 1e-6
    cmp_ = ib.comparer_a_reference(sortie_originale, a, analyse_a)
    assert cmp_["discordance_a_arret"] is False and cmp_["alertes_de_discordance"] == [lib]


def test_comparer_zeros_exacts_ou_n_differents_sont_des_discordances(sortie_originale, analyse_a):
    a = copy.deepcopy(analyse_a)
    a["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (V_iii_final)"]["zeros_exacts"] += 1
    assert ib.comparer_a_reference(sortie_originale, a, analyse_a)["discordance_a_arret"] is True


def test_comparer_contraste_absent_de_A(sortie_originale, analyse_a):
    a = copy.deepcopy(analyse_a)
    del a["resultat"]["2"]["contrastes_contre_R2"]["R4[moyenne,λ=0.3] - R2 (V_iii_final)"]
    cmp_ = ib.comparer_a_reference(sortie_originale, a, analyse_a)
    assert cmp_["discordance_a_arret"] is True and cmp_["concordance"] is False and len(cmp_["contrastes_absents_de_A"]) == 1


def test_comparer_classe_differente_est_signalee(sortie_originale, analyse_a):
    a = copy.deepcopy(analyse_a)
    # un décalage de A qui fait changer de classe : borne basse de R3 sur V ramenée sous la marge
    q = a["resultat"]["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]["quantiles"]
    q["q0.003125"] = 0.01
    cmp_ = ib.comparer_a_reference(sortie_originale, a, analyse_a)
    assert cmp_["classes"]["identiques"] is False
    assert cmp_["classes"]["differences"][0]["chemin"] == "table_B/R3/budget 1"
    assert cmp_["concordance"] is False


# =============================================================================================
# Divers
# =============================================================================================
def test_sortie_jamais_ecrasee(tmp_path):
    f = tmp_path / "x.json"
    sha = ib.ecrire_json_neuf(f, {"a": 1})
    assert sha == hashlib.sha256(f.read_bytes()).hexdigest()
    with pytest.raises(FileExistsError):
        ib.ecrire_json_neuf(f, {"a": 2})
    assert json.loads(f.read_text(encoding="utf-8")) == {"a": 1}
    with pytest.raises(ValueError):
        ib.ecrire_json_neuf(tmp_path / "y.json", {"a": float("nan")})


def test_analyse_deterministe(b_petit):
    e1 = fabriquer_e1(50)
    a = ib.analyser_donnees(e1, 20266201)
    b = ib.analyser_donnees(copy.deepcopy(e1), 20266201)
    assert a == b


def test_l_ordre_des_taches_dans_le_fichier_est_sans_effet(b_petit):
    e1 = fabriquer_e1(51, melanger=False)
    e2 = fabriquer_e1(51, melanger=True)
    a, b = ib.analyser_donnees(e1, 20266201), ib.analyser_donnees(e2, 20266201)
    assert a["resultat"] == b["resultat"]


def test_apparier_par_instance_et_non_par_position(b_petit):
    """Les différences appariées sont faites instance par instance : on décale une seule instance de R2 et on
    vérifie que la moyenne du contraste bouge de la valeur attendue."""
    e1 = fabriquer_e1(52, melanger=False)
    ref = ib.analyser_donnees(e1, 20266201)["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"]["moyenne"]
    v = tache(e1, 1, 37)["regles"]["R2"]
    v["ii_final"] = v["ii_final"] - 0.01 if v["ii_final"] > 0.01 else v["ii_final"] + 0.01
    nouv = ib.analyser_donnees(e1, 20266201)["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"]["moyenne"]
    assert abs(abs(nouv - ref) - 0.0001) < 1e-12


def test_les_rapports_markdown_et_json_de_validation_se_construisent(tmp_path):
    rapport = ib.valider_originale(DOSSIER, tmp_path)
    assert rapport["conclusion"]["validation_reussie"] is True
    md = ib.rapport_markdown(rapport)
    assert md.startswith("# Validation") and "RÉUSSIE" in md
    assert (tmp_path / ib.NOM_SORTIE_B).exists()
    with pytest.raises(FileExistsError):
        ib.valider_originale(DOSSIER, tmp_path)           # jamais écrasé


def test_delta_incoherent_est_un_avertissement_pas_un_arret(b_petit):
    e1 = fabriquer_e1(60)
    assert ib.analyser_donnees(e1, 20266201)["avertissements"] == []
    tache(e1, 2, 5)["delta"] = 1.4
    r = ib.analyser_donnees(e1, 20266201)
    assert len(r["avertissements"]) == 1 and "delta" in r["avertissements"][0]


def test_comparer_tolere_une_difference_de_classe_marquee_a_la_frontiere(sortie_originale):
    classes_b = sortie_originale["classes"]
    classes_a = copy.deepcopy(classes_b)
    classes_a["table_B"]["R3"]["1"].update({"ligne": 4, "classe": "R3 ≳ R2", "frontiere": True})
    cmp_ = ib.comparer_classes(classes_b, classes_a)
    assert cmp_["identiques"] is True and len(cmp_["differences"]) == 1 and cmp_["differences_hors_frontiere"] == []
    assert cmp_["differences"][0]["classe_retenue_pour_la_lecture"] == [4, "R3 ≳ R2"]     # on retient la classe de A
    classes_a["table_B"]["R3"]["1"]["frontiere"] = False                                   # sans frontière : discordance
    assert ib.comparer_classes(classes_b, classes_a)["identiques"] is False
    # même règle pour les verdicts
    v_b = {k: {"verdict": "x", "frontiere": False} for k in ("HR1", "HR0", "HR3", "HR2")}
    v_a = copy.deepcopy(v_b)
    v_a["HR0"] = {"verdict": "y", "frontiere": True}
    assert ib.comparer_verdicts(v_b, v_a)["identiques"] is True
    v_a["HR0"]["frontiere"] = False
    assert ib.comparer_verdicts(v_b, v_a)["identiques"] is False


def test_entier_trop_grand_est_un_arret_et_non_une_exception_brute():
    with pytest.raises(ib.Arret):
        ib._nombre(10 ** 400, "valeur")
