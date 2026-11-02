# -*- coding: utf-8 -*-
"""Essais de l'implémentation B, version 2 (implementation_b_v2.py).

Sources des valeurs attendues : uniquement « specification-statistique-decisive-v2.md » (vecteurs du § 4, du § 5.5,
tableau et listes du § 12, tables des § 8 à § 10), lue directement quand c'est possible plutôt que recopiée.
Chaque essai porte un préfixe de catégorie : c12_1 (course originale), c12_2 (branches : tables, verdicts, contrôles,
déclencheurs, issues, frontière), c12_3 (gardes de la réplication, comparaison A/B), c12_4 (entiers de 64 bits, règle D),
c12_5 (gardes d'entrée), mut (essais ajoutés pour tuer des mutations), base (constantes, générateur, quantiles, divers).
Lancer : /home/claude/controle-ia-travail/.venv/bin/python -m pytest -q   (depuis le dossier implementation-b/).
"""
from __future__ import annotations

import ast
import copy
import hashlib
import json
import math
import re
import statistics
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import implementation_b_v2 as ib   # noqa: E402

DOSSIER = Path(__file__).resolve().parent
ENTREES = DOSSIER / "entrees"
P_SPEC = ENTREES / "specification-statistique-decisive-v2.md"
P_RES = ENTREES / "resultats-regles-defense.json"
P_ANA = ENTREES / "analyse-regles-defense.json"
R4 = ib.NOMS_VARIANTES[4]
RHO, RHO_T = 20266201, 20266202
ETAT_OK = {"T2": False, "T3": False, "T4": False, "T5": False, "T6": False}
FRONT_OK = dict(ETAT_OK)
_CACHE: dict = {}


# =============================================================================================
# Pièces communes
# =============================================================================================
def pieces():
    """(analyse originale, résultats originaux) lus une seule fois ; ne jamais les modifier (deepcopy)."""
    if not _CACHE:
        _CACHE["ana"] = ib.lire_json_octets(P_ANA.read_bytes(), "A")
        _CACHE["res"] = ib.lire_json_octets(P_RES.read_bytes(), "E1")
    return _CACHE["ana"], _CACHE["res"]


@pytest.fixture(scope="session")
def texte_spec() -> str:
    return P_SPEC.read_text(encoding="utf-8")


@pytest.fixture(scope="session")
def analyse_a() -> dict:
    return pieces()[0]


@pytest.fixture(scope="session")
def e1_original() -> dict:
    return pieces()[1]


@pytest.fixture(scope="session")
def sortie_originale() -> dict:
    """Analyse de la course originale (racine 20266201) avec E5 = l'analyse de la course : l'original contre lui-même."""
    return ib.analyser_fichiers(mode="essai", resultats=P_RES, analyse_originale=P_ANA, resultats_originaux=P_RES,
                                analyse_A=P_ANA)


@pytest.fixture()
def b_petit(monkeypatch):
    """Réduit B (nombre de rééchantillonnages) pour les essais de plomberie sur pièces synthétiques."""
    monkeypatch.setattr(ib, "B", 200)


def fabriquer_e1(graine=0, rho=RHO, rho_t=RHO_T, *, nb_poids_purs=0, nb_cos_eleves=0, effet_r3=0.10,
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
                    "par_tour": {"cos_consecutif": cos},
                }
            taches.append({"code_delta": c, "instance": i, "delta": 1.4 if c == 1 else 1.6, "racine": rho,
                           "racine_tenue": rho_t, "config_sha256": ib.EMPREINTE_CONFIG, "regles": regles})
    if melanger:
        ordre = rng.permutation(len(taches))
        taches = [taches[j] for j in ordre]
    return {"run_id": "synthetique", "manifeste_sha256": "0" * 64,
            "resultat": {"temps": {"mur_s": 0.0}, "resultats": taches}}


def taches_de(e1):
    return e1["resultat"]["resultats"]


def tache(e1, c, i):
    return next(t for t in taches_de(e1) if t["code_delta"] == c and t["instance"] == i)


def fixer_V(v: dict, valeur: float):
    """Les trois champs de V d'une variante à la même valeur (V_final = min reste exact)."""
    v["V_iii_final"] = v["V_iii_standard"] = v["V_iii_renforce"] = valeur


def calc(e1, rho=RHO, rho_t=RHO_T):
    """Calcul de B sur un E1 synthétique (E4 = course originale), conclusion comprise, sans E5."""
    ana, res = pieces()
    s = ib.calculer_B(e1, rho, rho_t, ana, res)
    s["comparaison_A_B"] = {"evaluee": False}
    return ib.conclure(s)


def bornes(bas8, haut8, bas_e=None, haut_e=None):
    return {"B8": (bas8, haut8), "E8": (bas8 if bas_e is None else bas_e, haut8 if haut_e is None else haut_e)}


def ecrire_avec_compagnon(chemin: Path, octets: bytes) -> str:
    chemin.write_bytes(octets)
    sha = hashlib.sha256(octets).hexdigest()
    Path(str(chemin) + ".sha256").write_text(f"{sha}  {chemin.name}\n", encoding="utf-8")
    return sha


def resceller(chemin: Path) -> str:
    """Réécrit le compagnon d'un fichier (après modification volontaire du fichier)."""
    sha = hashlib.sha256(Path(chemin).read_bytes()).hexdigest()
    Path(str(chemin) + ".sha256").write_text(f"{sha}  {Path(chemin).name}\n", encoding="utf-8")
    return sha


def K(c1, c2=None):
    """Classes κ de (R0, V) ou κ′ de (R4, V) synthétiques, au format des classes de B."""
    c2 = c1 if c2 is None else c2
    return {1: {"classe": c1, "ligne": 1, "frontiere": False}, 2: {"classe": c2, "ligne": 1, "frontiere": False}}


# =============================================================================================
# Constantes, libellés, indépendance
# =============================================================================================
def test_base_constantes_binaires64():
    assert ib.N == 100 and ib.B == 20_000
    assert ib.P == (0.003125, 0.00625, 0.0125, 0.025, 0.05, 0.95, 0.975, 0.9875, 0.99375, 0.996875)
    assert ib.DEUX_ALPHA == 0.02 and ib.M == 0.02 and ib.S5 == 0.02 and ib.TAU == 0.05 and ib.EPS == 1e-9
    assert ib.G_GRAINES == 2
    assert ib.CLES_QUANTILES == ("q0.003125", "q0.00625", "q0.0125", "q0.025", "q0.05",
                                 "q0.95", "q0.975", "q0.9875", "q0.99375", "q0.996875")


def test_base_seuil_de_T3_point_15():
    assert ib.S_PUR == float.fromhex("0x1.fffffff768fa1p-1")
    assert ib.S_PUR == 1.0 - 1e-9 == float("0.999999999")


def test_base_bornes_de_l_intervalle_0_1_point_12():
    assert ib.BORNE_01_BAS == -1e-12 == -float("1e-12")
    assert ib.BORNE_01_HAUT == 1.0 + 1e-12 == float("1.000000000001")


def test_base_z_etoile_est_le_quantile_0_99375_de_la_loi_normale():
    assert abs(statistics.NormalDist().inv_cdf(0.99375) - ib.Z_ETOILE) < 1e-12


def test_base_bornes_B2_B8_E8():
    q = {cle: float(i) for i, cle in enumerate(ib.CLES_QUANTILES)}
    b = ib.bornes_depuis_statistique({"quantiles": q})
    assert b["B2"] == (q["q0.00625"], q["q0.99375"])
    assert b["B8"] == (q["q0.003125"], q["q0.996875"])
    assert b["E8"] == (q["q0.00625"], q["q0.99375"])


def test_base_les_constantes_de_la_specification_sont_dans_son_texte(texte_spec):
    for valeur in ("0x1.fffffff768fa1p-1", "2,497705474412374", ib.EMPREINTE_CONFIG, ib.EMPREINTE_RESULTATS_ORIGINAUX,
                   ib.EMPREINTE_ANALYSE_ORIGINALE):
        assert valeur in texte_spec
    assert hashlib.sha256(texte_spec.encode("utf-8")).hexdigest() == ib.EMPREINTE_SPECIFICATION_V2


def test_base_les_libelles_sont_ceux_de_la_specification(texte_spec):
    libelles = [ib.A_DEGENERE, ib.A_CONFIRMEE, ib.A_REFUTEE, ib.A_NON_DEMONTREE, ib.EQUIVALENT, ib.INCERTAIN,
                *ib.LIBELLES_TABLE_C.values(), ib.V_SANTE, ib.V_DEGENERE, ib.V_IMPRECIS, ib.V_REPLIQUEE,
                ib.V_HR1_SIGNE, ib.V_HR1_PETIT, ib.V_HR0_INTERET, ib.V_HR0_NON_NUL, ib.V_NON_REPLIQUEE,
                ib.V_HR3_SANS_VERDICT, ib.V_AUDIT_ATTENTE, ib.V_ARTEFACT, ib.O_CONFIRMEE, ib.O_REFUTEE,
                ib.O_NON_TRANCHEE, *ib.ISSUES.values()]
    for lib in libelles:
        assert f"« {lib} »" in texte_spec or lib in texte_spec, lib
    assert ib.MENTION_V0 in texte_spec
    for gabarit in ("R_k > R2", "R2 > R_k", "R_k ≳ R2", "R2 ≳ R_k", "≈", "?"):
        assert f"« {gabarit} »" in texte_spec
    cb = [ib.classe_table_B("R_k", bornes(*b))["classe"] for b in
          [(0.03, 0.06), (-0.06, -0.03), (-0.01, 0.01), (0.001, 0.05), (-0.05, -0.001), (-0.01, 0.03)]]
    assert cb == ["R_k > R2", "R2 > R_k", "≈", "R_k ≳ R2", "R2 ≳ R_k", "?"]
    cbp = [ib.classe_table_Bprime("R_k", bornes(*b))["classe"] for b in
           [(0.03, 0.06), (-0.06, -0.03), (-0.01, 0.01), (0.001, 0.05), (-0.05, -0.001), (-0.01, 0.03)]]
    assert cbp == ["R2 > R_k", "R_k > R2", "≈", "R2 ≳ R_k", "R_k ≳ R2", "?"]


def test_base_variantes_codes_et_libelles():
    assert ib.NOMS_VARIANTES == ("R0", "R1", "R2", "R3", "R4[moyenne,λ=0.3]")
    assert [ib.RANG[n] for n in ib.NOMS_VARIANTES] == [0, 1, 2, 3, 4]
    assert ib.libelle_contraste("R3", "V") == "R3 - R2 (V_iii_final)"
    assert ib.libelle_contraste(R4, "Xbarre") == "R4[moyenne,λ=0.3] - R2 (exploitabilite_moyenne_tours)"
    assert len(ib.TOUS_LES_CONTRASTES) == 16
    assert ib.code_generateur("V", "R3") == 203
    assert ib.code_generateur("V", "R0") == 200
    assert ib.code_generateur("V", R4) == 204
    assert ib.code_generateur("ii", "R0") == 300
    assert ib.code_generateur("Xbarre", "R1") == 1001


def test_base_le_module_n_importe_rien_du_depot_ni_du_reseau():
    source = (DOSSIER / "implementation_b_v2.py").read_text(encoding="utf-8")
    arbre = ast.parse(source)
    importes = set()
    for noeud in ast.walk(arbre):
        if isinstance(noeud, ast.Import):
            importes |= {a.name.split(".")[0] for a in noeud.names}
        elif isinstance(noeud, ast.ImportFrom):
            importes.add(noeud.module.split(".")[0])
    assert importes <= {"__future__", "argparse", "hashlib", "json", "math", "platform", "re", "subprocess", "sys",
                        "tempfile", "time", "xml", "pathlib", "numpy"}, importes
    for interdit in ("socket", "urllib", "requests", "controle_ia", "arene_", "scipy", "import os"):
        assert interdit not in source


# =============================================================================================
# Règle D (§ 4)
# =============================================================================================
@pytest.mark.parametrize("h, attendu", [(h, (a, b)) for (h, a, b) in ib.VECTEURS_REGLE_D])
def test_c12_4_regle_d_vecteurs_d_essai_du_paragraphe_4(h, attendu):
    assert ib.regle_d_derivation(h) == attendu


def test_c12_4_regle_d_vecteurs_recopies_de_la_specification(texte_spec):
    for h in ("d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d", "0" * 64, "f" * 64):
        assert h in texte_spec or h[0] * 64 == h
    for entier in ib.ENTIERS_DES_VECTEURS:
        assert str(entier) in texte_spec
    assert len(ib.ENTIERS_DES_VECTEURS) == 6


def test_c12_4_regle_d_cas_sain_differe_des_racines_de_la_course_originale():
    h = ib.VECTEURS_REGLE_D[0][0]
    assert ib.regle_d_derivation(h) == (11786724493248295725, 9136419304016434890)
    assert ib.regle_d_derivation(h) != (RHO, RHO_T)


def test_c12_4_regle_d_les_entiers_des_vecteurs_sont_interdits_comme_racines():
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
    (2 ** 64 - 59, 2 ** 64 - 60, False),       # deux entiers de plus de 2^63 sans lien avec F
    (123456789, 987654321, False),
])
def test_c12_4_regle_d_gardes(rho, rho_t, doit_arreter):
    if doit_arreter:
        with pytest.raises(ib.Arret):
            ib.regle_d_gardes(rho, rho_t)
    else:
        ib.regle_d_gardes(rho, rho_t)


@pytest.mark.parametrize("h", ["", "0" * 63, "0" * 65, "F" * 64, "g" * 64, " " + "0" * 63])
def test_c12_4_regle_d_exige_64_hexadecimaux_minuscules(h):
    with pytest.raises(ib.Arret):
        ib.regle_d_derivation(h)


def test_c12_4_regle_d_depuis_octets_utilise_l_empreinte_des_octets_exacts():
    octets = "préenregistrement de test λ\n".encode("utf-8")
    h, rho, rho_t = ib.regle_d_depuis_octets(octets)
    assert h == hashlib.sha256(octets).hexdigest()
    assert (rho, rho_t) == ib.regle_d_derivation(h)
    h2, rho2, _ = ib.regle_d_depuis_octets(octets + b" ")
    assert h2 != h and rho2 != rho


def test_c12_4_regle_d_sans_cle_de_descendance_et_mots_64_bits():
    h = "ab" * 32
    ss = np.random.SeedSequence(int(h, 16))
    assert ss.spawn_key == ()
    mots = ss.generate_state(2, dtype=np.uint64)
    assert ib.regle_d_derivation(h) == (int(mots[0]), int(mots[1]))


# =============================================================================================
# Générateur (§ 5.4, § 5.5)
# =============================================================================================
@pytest.mark.parametrize("v", ib.VECTEURS_GENERATEUR)
def test_base_generateur_vecteurs_d_essai_du_paragraphe_5_5(v):
    c, code = v["cle"][0], v["cle"][1]
    ind = ib.indices_reechantillonnage(20266201, c, code)
    assert ind.shape == (20000, 100) and ind.dtype == np.int64
    assert ind.min() >= 0 and ind.max() <= 99
    assert [int(x) for x in ind[0, :10]] == v["ligne0_dix_premiers"]
    assert [int(x) for x in ind[-1, -5:]] == v["derniere_ligne_cinq_derniers"]


def test_base_generateur_vecteurs_recopies_de_la_specification(texte_spec):
    for v in ib.VECTEURS_GENERATEUR:
        assert ", ".join(str(x) for x in v["ligne0_dix_premiers"]) in texte_spec
        assert ", ".join(str(x) for x in v["derniere_ligne_cinq_derniers"]) in texte_spec


def test_base_generateur_depend_de_la_racine_du_budget_et_du_code():
    a = ib.indices_reechantillonnage(20266201, 1, 203)[0, :10]
    assert not np.array_equal(a, ib.indices_reechantillonnage(20266202, 1, 203)[0, :10])
    assert not np.array_equal(a, ib.indices_reechantillonnage(20266201, 2, 203)[0, :10])
    assert not np.array_equal(a, ib.indices_reechantillonnage(20266201, 1, 204)[0, :10])
    assert np.array_equal(a, ib.indices_reechantillonnage(20266201, 1, 203)[0, :10])


def test_c12_4_generateur_accepte_une_racine_de_64_bits_et_la_distingue_de_sa_voisine():
    grand = 2 ** 64 - 59
    a = ib.indices_reechantillonnage(grand, 1, 203)
    assert a.shape == (20000, 100)
    assert float(grand) == float(grand + 1)           # un passage par le binaire64 les confondrait
    assert not np.array_equal(a[0], ib.indices_reechantillonnage(grand + 1, 1, 203)[0])


# =============================================================================================
# Quantiles de type 7 (§ 5.6) et statistique
# =============================================================================================
def test_base_quantile_type7_egal_a_numpy_lineaire():
    rng = np.random.default_rng(3)
    mu = rng.normal(size=20000)
    tri = np.sort(mu)
    ref = np.quantile(mu, ib.P, method="linear")
    mes = [ib.quantile_type7(tri, p) for p in ib.P]
    assert np.max(np.abs(np.array(mes) - ref)) < 1e-14


def test_base_quantile_type7_cas_limites():
    tri = np.array([1.0, 2.0, 4.0])
    assert ib.quantile_type7(tri, 0.0) == 1.0
    assert ib.quantile_type7(tri, 1.0) == 4.0            # f >= B-1 : dernier élément
    assert ib.quantile_type7(tri, 0.5) == 2.0
    assert ib.quantile_type7(tri, 0.75) == 3.0           # 2 + 0.5 * (4 - 2)
    assert ib.quantile_type7(np.array([5.0]), 0.3) == 5.0


def test_base_statistique_d_un_contraste_a_la_main():
    d = np.array([0.1, -0.1, 0.0, 0.2] * 25)
    st = ib.statistique_contraste(d, 20266201, 1, 203)
    assert st["moyenne"] == pytest.approx(0.05)
    assert st["ecart_type"] == pytest.approx(math.sqrt(sum((x - 0.05) ** 2 for x in d) / 99))
    assert st["zeros_exacts"] == 25 and st["n"] == 100
    assert st["quantiles"]["q0.003125"] < st["moyenne"] < st["quantiles"]["q0.996875"]
    qs = [st["quantiles"][c] for c in ib.CLES_QUANTILES]
    assert qs == sorted(qs)


# =============================================================================================
# Statistique, classes, contrôles et verdicts sur la course originale (§ 12.1)
# =============================================================================================
def test_c12_1_tableau_de_controle_lu_dans_la_specification(sortie_originale, texte_spec):
    rangees = ib.lire_table_12(texte_spec)
    assert len(rangees) == 10
    for r in rangees:
        stat = sortie_originale["resultat"][str(r["budget"])]["contrastes_contre_R2"][
            ib.libelle_contraste(r["variante"], r["mesure"])]
        for cle in ("moyenne", "ecart_type"):
            assert abs(stat[cle] - r[cle]) <= 1e-9
        for cle in ("q0.003125", "q0.00625", "q0.99375", "q0.996875"):
            assert abs(stat["quantiles"][cle] - r[cle]) <= 1e-9


def test_c12_1_quelques_valeurs_recopiees_a_la_main(sortie_originale):
    s = sortie_originale["resultat"]["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]
    assert abs(s["moyenne"] - 0.10448042252007811) <= 1e-12
    assert abs(s["ecart_type"] - 0.05656582805294246) <= 1e-12
    assert abs(s["quantiles"]["q0.003125"] - 0.08961294692052145) <= 1e-12
    assert abs(s["quantiles"]["q0.996875"] - 0.1195334438923409) <= 1e-12
    s = sortie_originale["resultat"]["2"]["contrastes_contre_R2"]["R0 - R2 (V_iii_final)"]
    assert abs(s["quantiles"]["q0.00625"] - (-0.005623565481548155)) <= 1e-12


def test_c12_1_16_contrastes_par_budget_identiques_a_l_analyse_de_reference(sortie_originale, analyse_a):
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


def test_c12_1_comparaison_automatique_a_la_reference(sortie_originale):
    cmp_ = sortie_originale["comparaison_A_B"]
    assert cmp_["evaluee"] is True and cmp_["concordance"] is True
    assert cmp_["ecart_maximal_absolu"] <= 1e-9
    assert cmp_["discordance_a_arret"] is False and cmp_["alertes_de_discordance"] == [] and cmp_["motifs"] == []
    assert cmp_["classes"]["identiques"] and cmp_["classes"]["nombre_de_classes_comparees"] == 25
    assert cmp_["verdicts_et_declencheurs"]["identiques"] and cmp_["z_pi"]["ok"]
    niveaux = [d["niveau"] for c in ("1", "2") for d in cmp_["detail_par_contraste"][c].values()]
    assert niveaux.count("arrêt") == 10 and niveaux.count("alerte") == 22


def test_c12_1_classes_de_la_course_originale(sortie_originale):
    at = ib._attendus_12(sortie_originale)
    assert at["ok"], json.dumps(at, ensure_ascii=False, default=str)[:600]
    cl = sortie_originale["classes"]
    assert (cl["table_A"]["ligne"], cl["table_A"]["classe"]) == (2, "HR1 confirmée")
    assert [cl["table_B"]["R1"][c]["classe"] for c in "12"] == ["R2 ≳ R1", "?"]
    assert [cl["table_Bprime"]["R1"][c]["classe"] for c in "12"] == ["R2 > R1", "R2 ≳ R1"]
    assert [cl["table_C"]["R3"][c]["ligne"] for c in "12"] == [1, 1]
    assert sortie_originale["classes_a_la_frontiere"] == []


def test_c12_1_controles_de_sante_de_la_course_originale(sortie_originale):
    s = sortie_originale["sante"]
    assert s["etat_global"] == ETAT_OK and s["frontiere_globale"] == FRONT_OK
    assert [s[c]["T3"]["nb_taches_poids_pur"] for c in "12"] == [0, 0]
    assert [s[c]["T4"]["nb_taches_cos_moyen_ge_0_999"] for c in "12"] == [5, 2]
    assert round(max(s[c]["T5"]["plus_grand_standard_moins_renforce"] for c in "12"), 5) == 0.00039
    assert round(max(s[c]["T5"]["plus_grand_abs_ecart_de_contraste"] for c in "12"), 5) == 0.00043
    assert round(max(s[c]["T6"]["plus_grand_abs_ecart_a_alpha"] for c in "12"), 5) == 0.00019
    assert all(s[c]["garde_coherence_V"] == "ok" for c in "12")
    assert all(not s[c][t]["declenche"] for c in "12" for t in ("T2", "T3", "T4", "T5", "T6"))


def test_c12_1_verdicts_de_la_course_originale(sortie_originale):
    v = sortie_originale["verdicts_regles_originales"]
    assert {k: v[k]["verdict"] for k in ("HR1", "HR0", "HR3", "HR2")} == {
        "HR1": "HR1 confirmée", "HR0": "réfutée", "HR3": "confirmée", "HR2": "non tranchée"}
    assert v["T2_T3_T5_T6_effectivement_non_declenches"] is True


def test_c12_3_artefact_l_original_contre_lui_meme(sortie_originale):
    s = sortie_originale
    eg = s["ecart_de_replication"]["contrastes_primaires"]
    assert len(eg) == 4 and all(e["g"] == 0.0 and e["z"] == 0.0 for e in eg.values())
    d = s["declencheurs_audit"]
    assert d["TR2"]["declenche"] is True and d["TR1"]["declenche"] is False and d["au_moins_un"]["declenche"] is True
    comptes = s["comptes_graines_neuves"]["comptes"]
    assert set(comptes) == {"R0", "R1", "R2", "R3", "R4"}
    assert all(set(par) == {"V_iii_final", "exploitabilite_moyenne_tours", "ii_final"} for par in comptes.values())
    assert [n for par in comptes.values() for n in par.values()] == [200] * 15
    assert s["comptes_graines_neuves"]["arret_graines_non_neuves"] is True
    assert s["lecture_autorisee"] is False and s["code_de_sortie"] == 3 and len(s["motifs_arret"]) == 1
    assert "graines non neuves" in s["motifs_arret"][0]
    assert {v["verdict"] for v in s["verdicts_apres_declencheurs"].values()} == {"non jugeable (audit en attente)"}
    assert s["issues_globales"]["brute"]["issue"] == "non jugeable (plomberie)"
    assert s["issues_globales"]["V0"] == "V0 : non évaluée par B" and s["issues_globales"]["brute"]["sous_reserve_de_V0"]
    assert s["issues_globales"]["apres_declencheurs"]["issue"] == "non jugeable (plomberie)"


# =============================================================================================
# § 12.2 — Table A (§ 8) : chaque ligne
# =============================================================================================
@pytest.mark.parametrize("entree, ligne, classe", [
    (dict(e1=(0.10, 0.09, 0.12), e2=(0.12, 0.11, 0.13)), 2, "HR1 confirmée"),
    (dict(e1=(0.02, 0.001, 0.05), e2=(0.02, 0.001, 0.05)), 2, "HR1 confirmée"),           # est == m compte (≥)
    (dict(e1=(0.0199999, 0.001, 0.05), e2=(0.10, 0.09, 0.12)), 4, "HR1 non démontrée"),   # est < m
    (dict(e1=(0.10, 0.0, 0.12), e2=(0.12, 0.11, 0.13)), 4, "HR1 non démontrée"),          # bas == 0 : pas > 0
    (dict(e1=(0.10, 0.09, 0.12), e2=(0.05, -0.03, 0.0)), 4, "HR1 non démontrée"),         # haut == 0 : pas < 0
    (dict(e1=(0.10, 0.09, 0.12), e2=(-0.05, -0.09, -0.001)), 3, "HR1 réfutée"),           # haut < 0 dans un budget
    (dict(e1=(-0.05, -0.09, -0.001), e2=(0.10, 0.09, 0.12)), 3, "HR1 réfutée"),
    (dict(e1=(0.01, -0.02, 0.04), e2=(0.01, -0.02, 0.04)), 4, "HR1 non démontrée"),
])
def test_c12_2_table_A_lignes(entree, ligne, classe):
    def mk(t, moy=0.12):
        return {"est": t[0], "bas_B2": t[1], "haut_B2": t[2], "moyennes_V": {n: moy for n in ib.NOMS_VARIANTES}}
    r = ib.classe_table_A({1: mk(entree["e1"]), 2: mk(entree["e2"])})
    assert (r["ligne"], r["classe"]) == (ligne, classe)


def test_c12_2_table_A_jeu_degenere():
    def mk(moy, t=(0.10, 0.09, 0.12), exceptions=None):
        m = {n: moy for n in ib.NOMS_VARIANTES}
        m.update(exceptions or {})
        return {"est": t[0], "bas_B2": t[1], "haut_B2": t[2], "moyennes_V": m}
    ok = mk(0.12)
    assert ib.classe_table_A({1: mk(0.02), 2: ok})["ligne"] == 1
    assert ib.classe_table_A({1: ok, 2: mk(0.0)})["ligne"] == 1
    assert ib.classe_table_A({1: mk(0.0200001), 2: ok})["ligne"] == 2
    assert ib.classe_table_A({1: mk(0.01, exceptions={"R3": 0.03}), 2: ok})["ligne"] == 2   # une seule variante au-dessus
    ref = (-0.05, -0.09, -0.001)
    assert ib.classe_table_A({1: mk(0.01, ref), 2: ok})["ligne"] == 1                         # l'emporte sur « réfutée »
    assert ib.classe_table_A({1: mk(0.01), 2: ok})["classe"] == "non concluant : jeu dégénéré"


# =============================================================================================
# § 12.2 — Tables B, B′, C : chaque ligne, chaque variante, égalité aux seuils
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


@pytest.mark.parametrize("k", ["R0", "R1", "R3", "R4"])
@pytest.mark.parametrize("b, ligne", CAS_B)
def test_c12_2_table_B_et_Bprime_lignes_pour_chaque_variante(k, b, ligne):
    rb = ib.classe_table_B(k, b)
    rp = ib.classe_table_Bprime(k, b)
    assert rb["ligne"] == rp["ligne"] == ligne
    attendu_b = {1: f"{k} > R2", 2: f"R2 > {k}", 3: "≈", 4: f"{k} ≳ R2", 5: f"R2 ≳ {k}", 6: "?"}[ligne]
    attendu_p = {1: f"R2 > {k}", 2: f"{k} > R2", 3: "≈", 4: f"R2 ≳ {k}", 5: f"{k} ≳ R2", 6: "?"}[ligne]
    assert rb["classe"] == attendu_b and rp["classe"] == attendu_p


@pytest.mark.parametrize("bas, haut, ligne", [
    (-0.06, -0.03, 1), (-0.015, -0.005, 2), (-0.03, -0.005, 3), (0.001, 0.05, 4), (-0.01, 0.02, 5), (-0.03, 0.03, 6),
    (-0.03, -0.02, 3),      # haut == -S5 : pas < -S5 ; haut < 0 ; bas ≤ -S5
    (-0.02, 0.03, 6),       # bas == -S5 : pas > -S5
    (0.0, 0.01, 5),         # bas == 0 : pas > 0 mais > -S5
    (-0.01, 0.0, 5),        # haut == 0 : pas < 0
])
def test_c12_2_table_C_lignes(bas, haut, ligne):
    r = ib.classe_table_C({"B8": (bas, haut), "E8": (bas, haut)})
    assert r["ligne"] == ligne and r["classe"] == ib.LIBELLES_TABLE_C[ligne]


def _imposer(e1, nom, champ, diffs, base_r2=None):
    """Impose, dans chaque tâche, valeur(nom, champ) = valeur(R2, champ) + diffs[instance] ; si `base_r2` est donné,
    R2 est d'abord fixé à cette valeur (pour rester dans [0 ; 1])."""
    for t in taches_de(e1):
        r2 = t["regles"]["R2"]
        if base_r2 is not None:
            if champ == "V_iii_final":
                fixer_V(r2, base_r2)
            else:
                r2[champ] = base_r2
        x = r2[champ] + diffs[t["instance"]]
        if champ == "V_iii_final":
            fixer_V(t["regles"][nom], x)
        else:
            t["regles"][nom][champ] = x


def _diffs(moy, amp):
    return [moy + (amp if i % 2 == 0 else -amp) for i in range(100)]


@pytest.mark.parametrize("nom, moy, amp, classe, ligne", [
    ("R0", 0.05, 0.0, "R0 > R2", 1), ("R0", -0.05, 0.0, "R2 > R0", 2), ("R0", 0.015, 0.03, "R0 ≳ R2", 4),
    ("R0", -0.015, 0.03, "R2 ≳ R0", 5), ("R0", 0.0, 0.1, "?", 6),
    (R4, 0.05, 0.0, "R4 > R2", 1), (R4, -0.05, 0.0, "R2 > R4", 2), (R4, 0.015, 0.03, "R4 ≳ R2", 4),
    (R4, -0.015, 0.03, "R2 ≳ R4", 5),
])
def test_c12_2_classes_nommees_de_la_table_B_de_bout_en_bout(b_petit, nom, moy, amp, classe, ligne):
    e1 = fabriquer_e1(70)
    _imposer(e1, nom, "V_iii_final", _diffs(moy, amp), base_r2=0.5)
    s = calc(e1)
    court = "R0" if nom == "R0" else "R4"
    for c in "12":
        assert s["classes"]["table_B"][court][c]["classe"] == classe, s["classes"]["table_B"][court][c]
        assert s["classes"]["table_B"][court][c]["ligne"] == ligne


@pytest.mark.parametrize("moy, amp, ligne", [
    (0.05, 0.0, 4), (-0.01, 0.0, 2), (-0.02, 0.05, 3), (0.0, 0.03, 5), (0.0, 0.1, 6), (-0.1, 0.0, 1),
])
def test_c12_2_table_C_lignes_de_bout_en_bout(b_petit, moy, amp, ligne):
    e1 = fabriquer_e1(71)
    _imposer(e1, "R0", "ii_final", _diffs(moy, amp), base_r2=0.5)
    s = calc(e1)
    assert [s["classes"]["table_C"]["R0"][c]["ligne"] for c in "12"] == [ligne, ligne]
    assert s["verdicts_bruts_replication"]["lignes_C_R0_ii"] == {"1": ligne, "2": ligne}
    v = s["verdicts_bruts_replication"]["lois_tenues_ii"]
    attendu = {4: ("répliquée", 2), 1: ("non répliquée (signe inversé)", 3), 2: ("non répliquée (signe inversé)", 3),
               3: ("non répliquée (signe inversé)", 3), 5: ("non jugeable (imprécis)", 4),
               6: ("non jugeable (imprécis)", 4)}[ligne]
    assert (v["verdict"], v["ligne"]) == attendu


# =============================================================================================
# § 12.2 — verdicts du § 9 (règles de la course originale)
# =============================================================================================
def _classes_synth(b0=("≈", "≈"), b4=("R4 ≳ R2", "R4 ≳ R2"), bp1=("R2 > R1", "R2 ≳ R1"), ligne_a=2):
    def par_c(labels):
        return {str(c): {"classe": labels[c - 1], "ligne": 1, "frontiere": False} for c in (1, 2)}
    return {"table_A": {"ligne": ligne_a, "classe": ib.A_CONFIRMEE, "frontiere": False},
            "table_B": {"R0": par_c(b0), "R4": par_c(b4)}, "table_Bprime": {"R1": par_c(bp1)}}


@pytest.mark.parametrize("b0, attendu", [
    (("R2 > R0", "R2 > R0"), "confirmée"), (("R2 > R0", "≈"), "réfutée"), (("≈", "≈"), "réfutée"),
    (("R0 ≳ R2", "R2 > R0"), "réfutée"), (("R0 > R2", "R2 > R0"), "réfutée"),
    (("R2 > R0", "R2 ≳ R0"), "non tranchée"), (("R2 ≳ R0", "R2 ≳ R0"), "non tranchée"),
    (("?", "R2 > R0"), "non tranchée"), (("?", "?"), "non tranchée"),
])
def test_c12_2_verdict_HR0_original(b0, attendu):
    assert ib.verdicts_regles_originales(_classes_synth(b0=b0), ETAT_OK, FRONT_OK)["HR0"]["verdict"] == attendu


@pytest.mark.parametrize("b4, t4, attendu", [
    (("R4 > R2", "≈"), False, "confirmée"), (("R4 ≳ R2", "R4 ≳ R2"), False, "confirmée"),
    (("R4 ≳ R2", "?"), False, "non tranchée"), (("R4 ≳ R2", "R2 > R4"), False, "réfutée"),
    (("R2 ≳ R4", "R4 > R2"), False, "non tranchée"),            # « R2 ≳ R4 » ne réfute pas au § 9
    (("R2 ≳ R4", "R2 ≳ R4"), False, "non tranchée"),
    (("R4 > R2", "R4 > R2"), True, "sans verdict (R4 ≈ défense figée)"),
])
def test_c12_2_verdict_HR3_original(b4, t4, attendu):
    etat = dict(ETAT_OK, T4=t4)
    assert ib.verdicts_regles_originales(_classes_synth(b4=b4), etat, FRONT_OK)["HR3"]["verdict"] == attendu


@pytest.mark.parametrize("bp1, attendu", [
    (("R2 > R1", "R2 > R1"), "confirmée"), (("R2 > R1", "R2 ≳ R1"), "non tranchée"), (("R2 > R1", "≈"), "réfutée"),
    (("R1 ≳ R2", "?"), "réfutée"), (("R1 > R2", "R2 > R1"), "réfutée"), (("?", "?"), "non tranchée"),
])
def test_c12_2_verdict_HR2_original(bp1, attendu):
    assert ib.verdicts_regles_originales(_classes_synth(bp1=bp1), ETAT_OK, FRONT_OK)["HR2"]["verdict"] == attendu


# =============================================================================================
# § 12.2 — verdicts bruts de la réplication (§ 10.1) : chaque ligne
# =============================================================================================
def _pb(e1, e2):
    return {c: {"est": e[0], "bas_B2": e[1], "haut_B2": e[2]} for c, e in ((1, e1), (2, e2))}


MV_OK = {"1": {n: 0.12 for n in ib.NOMS_VARIANTES}, "2": {n: 0.12 for n in ib.NOMS_VARIANTES}}
MV_DEGENERE = {"1": MV_OK["1"], "2": {n: 0.02 for n in ib.NOMS_VARIANTES}}


@pytest.mark.parametrize("etat, mv, pb, ligne", [
    (dict(ETAT_OK, T2=True), MV_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T3=True), MV_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T5=True), MV_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T6=True), MV_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 1),
    (dict(ETAT_OK, T4=True), MV_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 3),     # T4 ne bloque pas HR1
    (ETAT_OK, MV_DEGENERE, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 2),              # ligne gardée, inatteignable en pratique
    (ETAT_OK, MV_OK, _pb((0.1, 0.09, 0.12), (0.1, 0.09, 0.12)), 3),
    (ETAT_OK, MV_OK, _pb((0.05, 0.001, 0.09), (0.05, 0.001, 0.09)), 3),                # est == τ compte (≥)
    (ETAT_OK, MV_OK, _pb((0.1, 0.09, 0.12), (-0.05, -0.09, -0.001)), 4),
    (ETAT_OK, MV_OK, _pb((0.1, 0.09, 0.12), (0.01, -0.01, 0.04)), 5),                  # haut ∈ [0 ; τ)
    (ETAT_OK, MV_OK, _pb((0.1, 0.09, 0.12), (0.01, 0.0, 0.0)), 5),                     # haut == 0 : pas < 0, mais < τ
    (ETAT_OK, MV_OK, _pb((0.1, 0.09, 0.12), (0.04999, 0.001, 0.09)), 6),               # est < τ mais haut ≥ τ
    (ETAT_OK, MV_OK, _pb((0.1, 0.09, 0.12), (0.08, 0.0, 0.2)), 6),                     # bas == 0 : pas > 0
    (ETAT_OK, MV_OK, _pb((0.04, 0.001, 0.05), (0.1, 0.09, 0.12)), 6),                  # haut == τ : pas < τ
])
def test_c12_2_verdict_HR1_replication_lignes(etat, mv, pb, ligne):
    r = ib.verdict_HR1_replication(etat, FRONT_OK, pb, mv)
    assert r["ligne"] == ligne
    textes = {1: "non jugeable (santé)", 2: "non jugeable (jeu dégénéré)", 3: "répliquée",
              4: "non répliquée (signe inversé)", 5: "non répliquée (effet démontré inférieur à 0,05)",
              6: "non jugeable (imprécis)"}
    assert r["verdict"] == textes[ligne]


def test_c12_2_la_ligne_2_de_HR1_est_inatteignable_une_entree_qui_la_remplit_rend_sante(b_petit):
    """Une entrée qui remplit la condition de la ligne 2 (cinq variantes à V ≤ 2α à un budget) rend la ligne 1."""
    e1 = fabriquer_e1(72)
    for t in taches_de(e1):
        if t["code_delta"] == 2:
            for nom in ib.NOMS_VARIANTES:
                fixer_V(t["regles"][nom], 0.01)
    s = calc(e1)
    assert s["sante"]["2"]["jeu_degenere"] is True and s["sante"]["2"]["T2"]["declenche"] is True
    hr1 = s["verdicts_bruts_replication"]["HR1"]
    assert (hr1["ligne"], hr1["verdict"]) == (1, "non jugeable (santé)")
    assert s["classes"]["table_A"]["classe"] == "non concluant : jeu dégénéré"      # la Table A originale, elle, l'atteint


def test_c12_2_si_la_ligne_2_etait_atteinte_par_le_chemin_complet_c_est_une_erreur_interne(b_petit):
    e1 = fabriquer_e1(72)
    for t in taches_de(e1):
        for nom in ib.NOMS_VARIANTES:
            fixer_V(t["regles"][nom], 0.01)
    s = calc(e1)
    faux = copy.deepcopy(s["sante"])
    faux["etat_global"]["T2"] = False                     # incohérence artificielle entre T2 et le prédicat
    with pytest.raises(ib.ErreurInterne):
        ib.verdicts_bruts_replication(s["classes"], {c: s["resultat"][c]["contrastes_contre_R2"] for c in "12"}, faux,
                                      s["verdicts_regles_originales"])


@pytest.mark.parametrize("etat, k, ligne", [
    (dict(ETAT_OK, T2=True), ("≈", "≈"), 1), (dict(ETAT_OK, T5=True), ("≈", "≈"), 1), (dict(ETAT_OK, T6=True), ("≈", "≈"), 1),
    (dict(ETAT_OK, T3=True), ("≈", "≈"), 4),                                           # T3 ne bloque pas HR0
    (ETAT_OK, ("R2 > R0", "≈"), 2), (ETAT_OK, ("≈", "R2 > R0"), 2), (ETAT_OK, ("R2 > R0", "R2 ≳ R0"), 2),
    (ETAT_OK, ("R2 ≳ R0", "≈"), 3), (ETAT_OK, ("R2 ≳ R0", "R0 > R2"), 3),
    (ETAT_OK, ("≈", "≈"), 4), (ETAT_OK, ("R0 ≳ R2", "R0 > R2"), 4), (ETAT_OK, ("≈", "R0 ≳ R2"), 4),
    (ETAT_OK, ("≈", "?"), 5), (ETAT_OK, ("?", "?"), 5),
])
def test_c12_2_verdict_HR0_replication_lignes(etat, k, ligne):
    r = ib.verdict_HR0_replication(etat, FRONT_OK, K(*k))
    assert r["ligne"] == ligne
    assert r["verdict"] == {1: "non jugeable (santé)", 2: "non répliquée (le réentraînement l'emporte d'un effet d'intérêt)",
                            3: "non répliquée (le réentraînement l'emporte, effet démontré non nul)",
                            4: "répliquée", 5: "non jugeable (imprécis)"}[ligne]


@pytest.mark.parametrize("etat, k, ligne", [
    (dict(ETAT_OK, T2=True), ("R4 > R2", "R4 > R2"), 1), (dict(ETAT_OK, T5=True, T4=True), ("R4 > R2", "R4 > R2"), 1),
    (dict(ETAT_OK, T6=True), ("R4 > R2", "R4 > R2"), 1),
    (dict(ETAT_OK, T4=True), ("R4 > R2", "R4 > R2"), 2),
    (ETAT_OK, ("R2 > R4", "R4 > R2"), 3), (ETAT_OK, ("R4 > R2", "R2 ≳ R4"), 3),
    (ETAT_OK, ("R4 > R2", "≈"), 4), (ETAT_OK, ("R4 ≳ R2", "R4 ≳ R2"), 4),
    (ETAT_OK, ("R4 ≳ R2", "?"), 5), (ETAT_OK, ("?", "?"), 5),
])
def test_c12_2_verdict_HR3_replication_lignes(etat, k, ligne):
    r = ib.verdict_HR3_replication(etat, FRONT_OK, K(*k))
    assert r["ligne"] == ligne
    assert r["verdict"] == {1: "non jugeable (santé)", 2: "sans verdict (R4 ≈ défense figée)", 3: "non répliquée",
                            4: "répliquée", 5: "non jugeable (imprécis)"}[ligne]


def _kc(l1, l2):
    return {1: {"classe": "x", "ligne": l1, "frontiere": False}, 2: {"classe": "x", "ligne": l2, "frontiere": False}}


@pytest.mark.parametrize("etat, lg, ligne", [
    (dict(ETAT_OK, T2=True), (4, 4), 1), (dict(ETAT_OK, T6=True), (4, 4), 1), (dict(ETAT_OK, T5=True), (4, 4), 1),
    (dict(ETAT_OK, T4=True), (4, 4), 2),                                              # T4 ne bloque pas ce verdict
    (ETAT_OK, (4, 4), 2), (ETAT_OK, (1, 4), 3), (ETAT_OK, (4, 2), 3), (ETAT_OK, (3, 5), 3),
    (ETAT_OK, (5, 4), 4), (ETAT_OK, (6, 6), 4), (ETAT_OK, (5, 5), 4),
])
def test_c12_2_verdict_lois_tenues_ii_replication_lignes(etat, lg, ligne):
    r = ib.verdict_ii_replication(etat, FRONT_OK, _kc(*lg))
    assert r["ligne"] == ligne
    assert r["verdict"] == {1: "non jugeable (santé)", 2: "répliquée", 3: "non répliquée (signe inversé)",
                            4: "non jugeable (imprécis)"}[ligne]


# =============================================================================================
# § 12.2 — écart de réplication et déclencheurs d'audit (§ 10.2)
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


def _cl_r0(k1, k2, f1=False, f2=False):
    return {"table_B": {"R0": {"1": {"classe": k1, "frontiere": f1}, "2": {"classe": k2, "frontiere": f2}}}}


def _vb(v1="répliquée", v0="répliquée", f1=False, f0=False):
    return {"HR1": {"verdict": v1, "frontiere": f1}, "HR0": {"verdict": v0, "frontiere": f0}}


def test_c12_2_sigma_et_z():
    assert ib.sigma_pi(0.06, 0.08) == pytest.approx(0.01)
    e = ib.ecart_replication(_faux_contrastes(0.13, 0.06), _fausse_analyse(0.10, 0.08))
    assert len(e) == 4
    for v in e.values():
        assert v["g"] == pytest.approx(0.03) and v["sigma"] == pytest.approx(0.01) and v["z"] == pytest.approx(3.0)
        assert v["est_or"] == 0.10 and v["s_or"] == 0.08 and v["est_rep"] == 0.13 and v["s_rep"] == 0.06


def test_c12_2_z_non_defini_quand_sigma_nul():
    e = ib.ecart_replication(_faux_contrastes(0.2, 0.0), _fausse_analyse(0.1, 0.0))
    assert all(v["z"] is None and v["sigma"] == 0.0 for v in e.values())
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    assert d["TR1"]["declenche"] is True        # |g| > z* × 0


def test_c12_2_TR1_dans_les_deux_sens_et_au_seuil():
    seuil = ib.Z_ETOILE * 0.01
    for signe in (+1, -1):
        e = ib.ecart_replication(_faux_contrastes(0.10 + signe * (seuil + 1e-6), 0.06), _fausse_analyse(0.10, 0.08))
        assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())["TR1"]["declenche"] is True
        e = ib.ecart_replication(_faux_contrastes(0.10 + signe * (seuil - 1e-6), 0.06), _fausse_analyse(0.10, 0.08))
        assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())["TR1"]["declenche"] is False


def test_c12_2_TR1_se_declenche_sur_un_seul_contraste():
    c = _faux_contrastes(0.10, 0.06)
    c["2"][ib.libelle_contraste("R0", "V")]["moyenne"] = 0.10 + 0.05
    e = ib.ecart_replication(c, _fausse_analyse(0.10, 0.08))
    assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())["TR1"]["declenche"] is True


def test_c12_2_TR2_trop_propre_exige_les_quatre_ecarts_petits_et_strictement():
    e = ib.ecart_replication(_faux_contrastes(0.1005, 0.06), _fausse_analyse(0.10, 0.08))
    assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())["TR2"]["declenche"] is True
    for g_un, attendu in ((2.0 ** -10, True), (2.0 ** -9, False)):     # 0,000977 puis 0,001953 (exacts en binaire)
        c = _faux_contrastes(0.5, 0.06)
        c["1"][ib.libelle_contraste("R3", "V")]["moyenne"] = 0.5 + g_un
        e = ib.ecart_replication(c, _fausse_analyse(0.5, 0.08))
        assert e["(R3, V, c=1)"]["g"] == g_un
        assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())["TR2"]["declenche"] is attendu


@pytest.mark.parametrize("kappa, attendu", [
    (("R0 > R2", "≈"), True), (("≈", "R0 ≳ R2"), True), (("≈", "≈"), False),
    (("R2 > R0", "R2 ≳ R0"), False), (("?", "R0 ≳ R2"), True), (("R0 > R2", "R0 > R2"), True),
])
def test_c12_2_TR3_defense_figee_plus_belle(kappa, attendu):
    e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
    assert ib.declencheurs_audit(e, _cl_r0(*kappa), _vb())["TR3"]["declenche"] is attendu


@pytest.mark.parametrize("v1, v0, attendu", [
    ("non répliquée (signe inversé)", "répliquée", True),
    ("répliquée", "non répliquée (le réentraînement l'emporte d'un effet d'intérêt)", True),
    ("répliquée", "répliquée", False), ("non jugeable (imprécis)", "non jugeable (santé)", False),
    ("non répliquée (effet démontré inférieur à 0,05)", "non jugeable (imprécis)", True),
])
def test_c12_2_TR4_non_replication(v1, v0, attendu):
    e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
    assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb(v1, v0))["TR4"]["declenche"] is attendu


def test_c12_2_TR3_et_TR4_de_bout_en_bout(b_petit):
    e1 = fabriquer_e1(73)
    _imposer(e1, "R0", "V_iii_final", _diffs(0.05, 0.0), base_r2=0.5)
    s = calc(e1)
    assert s["declencheurs_audit"]["TR3"]["declenche"] is True and s["declencheurs_audit"]["au_moins_un"]["declenche"]
    assert s["verdicts_bruts_replication"]["HR0"]["verdict"] == "répliquée"
    assert {v["verdict"] for v in s["verdicts_apres_declencheurs"].values()} == {"non jugeable (audit en attente)"}
    # R3 sans effet : HR1 « non répliquée » (haut(B2) < τ ou < 0) -> TR4
    e1 = fabriquer_e1(74, effet_r3=0.0)
    s = calc(e1)
    assert s["verdicts_bruts_replication"]["HR1"]["verdict"].startswith("non répliquée")
    assert s["declencheurs_audit"]["TR4"]["declenche"] is True
    assert s["issues_globales"]["brute"]["issue"] == "échec de réplication du résultat positif"
    assert s["issues_globales"]["apres_declencheurs"]["issue"] == "en attente d'audit"


def test_c12_2_effet_des_declencheurs_et_hr2_non_concerne():
    vb = {k: {"verdict": "répliquée", "ligne": 4, "frontiere": False} for k in ib.CLES_VERDICTS_REPLICATION}
    aucun = {"au_moins_un": {"declenche": False, "frontiere": False}}
    assert {k: v["verdict"] for k, v in ib.verdicts_apres_declencheurs(vb, aucun).items()} == {
        "HR1": "répliquée", "HR0": "répliquée", "HR3": "répliquée", "lois_tenues_ii": "répliquée"}
    apres = ib.verdicts_apres_declencheurs(vb, {"au_moins_un": {"declenche": True, "frontiere": False}})
    assert set(apres) == {"HR1", "HR0", "HR3", "lois_tenues_ii"}
    assert {v["verdict"] for v in apres.values()} == {"non jugeable (audit en attente)"}


def test_c12_2_analyse_originale_absente_d_un_contraste_est_un_arret():
    with pytest.raises(ib.Arret):
        ib.ecart_replication(_faux_contrastes(0.1, 0.06), {"resultat": {"1": {"contrastes_contre_R2": {}}, "2": {}}})


# =============================================================================================
# § 12.2 — issues globales (§ 10.4) : chaque ligne
# =============================================================================================
@pytest.mark.parametrize("hr1, hr0, kw, ligne", [
    ("répliquée", "répliquée", dict(plomberie_fausse=True), 1),
    ("répliquée", "répliquée", dict(arret_controle=True), 1),
    ("non répliquée (signe inversé)", "répliquée", dict(arret_controle=True), 1),      # la ligne 1 passe avant la ligne 4
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
def test_c12_2_issue_globale_lignes(hr1, hr0, kw, ligne):
    r = ib.issue_globale(hr1, hr0, **kw)
    assert r["ligne"] == ligne and r["issue"] == ib.ISSUES[ligne]
    assert r["V0"] == "V0 : non évaluée par B" and r["sous_reserve_de_V0"] is True


def test_c12_2_l_issue_herite_de_la_marque_des_verdicts_qui_y_entrent():
    marque = lambda t, f: {"verdict": t, "frontiere": f}
    assert ib.issue_globale(marque("répliquée", True), marque("répliquée", False))["frontiere"] is True
    assert ib.issue_globale(marque("répliquée", False), marque("répliquée", True))["frontiere"] is True
    assert ib.issue_globale(marque("répliquée", False), marque("répliquée", False))["frontiere"] is False
    # ligne 1 (arrêt) : ne dépend pas des verdicts
    assert ib.issue_globale(marque("répliquée", True), marque("répliquée", True), arret_controle=True)["frontiere"] is False


# =============================================================================================
# § 12.2 — graines neuves (§ 10.3, CL-10) : unités
# =============================================================================================
def _donnees_champs(valeurs):
    """valeurs[(c, nom, champ)] -> tableau ; format interne de `extraire_donnees` (champs seulement)."""
    return {c: {"champs": {nom: {ch: np.array(valeurs[(c, nom, ch)], dtype=float) for ch in
                                 ("V_iii_final", "exploitabilite_moyenne_tours", "ii_final", "exploitabilite_finale")}
                           for nom in ib.NOMS_VARIANTES}} for c in (1, 2)}


def _base_valeurs():
    return {(c, nom, ch): np.linspace(0.1, 0.2, 100) for c in (1, 2) for nom in ib.NOMS_VARIANTES
            for ch in ("V_iii_final", "exploitabilite_moyenne_tours", "ii_final", "exploitabilite_finale")}


def test_c12_2_graines_neuves_egalite_au_bit_sur_les_trois_mesures():
    base = _base_valeurs()
    autre = {k: v + 1e-3 for k, v in base.items()}
    cpt = ib.comptes_graines_neuves(_donnees_champs(base), _donnees_champs(autre))
    assert [n for par in cpt.values() for n in par.values()] == [0] * 15
    cpt = ib.comptes_graines_neuves(_donnees_champs(base), _donnees_champs(base))
    assert [n for par in cpt.values() for n in par.values()] == [200] * 15
    z = {k: np.zeros(100) for k in base}
    nz = {k: -np.zeros(100) for k in base}                 # 0.0 et −0.0 : égaux en valeur, pas au bit
    cpt = ib.comptes_graines_neuves(_donnees_champs(z), _donnees_champs(nz))
    assert [n for par in cpt.values() for n in par.values()] == [0] * 15
    d = {k: v.copy() for k, v in base.items()}
    d[(1, "R3", "V_iii_final")][5] = np.nextafter(d[(1, "R3", "V_iii_final")][5], 1.0)   # un seul bit de différence
    cpt = ib.comptes_graines_neuves(_donnees_champs(base), _donnees_champs(d))
    assert cpt["R3"]["V_iii_final"] == 199 and cpt["R0"]["V_iii_final"] == 200 and cpt["R3"]["ii_final"] == 200


def test_c12_2_graines_neuves_ne_compte_pas_l_exploitabilite_finale():
    base = _base_valeurs()
    d = {k: v + (1e-3 if k[2] != "exploitabilite_finale" else 0.0) for k, v in base.items()}
    cpt = ib.comptes_graines_neuves(_donnees_champs(base), _donnees_champs(d))
    assert [n for par in cpt.values() for n in par.values()] == [0] * 15
    assert set(next(iter(cpt.values()))) == {"V_iii_final", "exploitabilite_moyenne_tours", "ii_final"}


@pytest.mark.parametrize("compte, arret", [(0, False), (1, False), (2, False), (3, True), (4, True), (200, True)])
def test_c12_2_graines_neuves_seuil_strictement_superieur_a_2(compte, arret):
    comptes = {nom: {ch: 0 for ch in ("V_iii_final", "exploitabilite_moyenne_tours", "ii_final")}
               for nom in ("R0", "R1", "R2", "R3", "R4")}
    comptes["R2"]["ii_final"] = compte
    r = ib.resume_graines_neuves(comptes)
    assert r["arret_graines_non_neuves"] is arret and r["seuil_G"] == 2
    assert (r["comptes_au_dessus_du_seuil"] != []) is arret


# =============================================================================================
# § 12.2 — contrôles de santé (§ 7), chaque condition, sur pièces synthétiques
# =============================================================================================
def test_c12_2_synthetique_sain(b_petit):
    r = calc(fabriquer_e1(graine=5))
    assert r["sante"]["etat_global"] == ETAT_OK
    assert r["verdicts_regles_originales"]["HR1"]["verdict"] == "HR1 confirmée"
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "répliquée"
    assert r["lecture_autorisee"] is True and r["code_de_sortie"] == 0 and r["motifs_arret"] == []


def test_c12_2_T3_melange_degenere_strictement_plus_de_50_taches(b_petit):
    assert calc(fabriquer_e1(graine=6, nb_poids_purs=50))["sante"]["1"]["T3"]["nb_taches_poids_pur"] == 50
    assert calc(fabriquer_e1(graine=6, nb_poids_purs=50))["sante"]["etat_global"]["T3"] is False
    r = calc(fabriquer_e1(graine=6, nb_poids_purs=51))
    assert r["sante"]["1"]["T3"]["declenche"] and r["sante"]["etat_global"]["T3"]
    assert r["sante"]["2"]["T3"]["declenche"]                  # les tâches pures sont dans les deux budgets
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "non jugeable (santé)"
    assert r["verdicts_bruts_replication"]["HR0"]["verdict"] != "non jugeable (santé)"      # T3 ne bloque que HR1


def test_c12_2_T3_un_seul_budget_suffit(b_petit):
    e1 = fabriquer_e1(6, melanger=False)
    for t in taches_de(e1):
        if t["code_delta"] == 2 and t["instance"] < 51:
            w = [0.0] * 9
            w[2] = 1.0
            t["regles"]["R3"]["poids_finaux"] = w
        if t["code_delta"] == 1:
            t["regles"]["R3"]["poids_finaux"] = [1.0 / 9] * 9
    r = calc(e1)
    assert r["sante"]["1"]["T3"]["declenche"] is False and r["sante"]["2"]["T3"]["declenche"] is True
    assert r["sante"]["etat_global"]["T3"] is True


def test_c12_2_T3_seuil_exact_s_pur_et_pas_de_marque(b_petit):
    """Le plus grand poids est comparé à S_PUR avec « ≥ » ; la comparaison porte sur une valeur brute : jamais marquée."""
    for poids, doit in ((ib.S_PUR, True), (float(np.nextafter(ib.S_PUR, 0.0)), False), (1.0, True), (1.0 - 2e-9, False)):
        e1 = fabriquer_e1(7, melanger=False)
        for t in taches_de(e1):
            if t["code_delta"] == 1 and t["instance"] < 51:
                w = [(1.0 - poids) / 8] * 9
                w[0] = poids
                t["regles"]["R3"]["poids_finaux"] = w
        r = calc(e1)
        assert r["sante"]["1"]["T3"]["nb_taches_poids_pur"] == (51 if doit else 0), poids
        assert r["sante"]["1"]["T3"]["frontiere"] is False
    assert r["sante"]["frontiere_globale"]["T3"] is False


def test_c12_2_T4_regularisation_degeneree_ne_bloque_que_HR3(b_petit):
    r = calc(fabriquer_e1(graine=8, nb_cos_eleves=51))
    assert r["sante"]["1"]["T4"]["nb_taches_cos_moyen_ge_0_999"] == 51 and r["sante"]["etat_global"]["T4"]
    vb = r["verdicts_bruts_replication"]
    assert vb["HR3"]["verdict"] == "sans verdict (R4 ≈ défense figée)" and vb["HR3"]["ligne"] == 2
    assert vb["HR1"]["verdict"] == "répliquée"
    assert r["verdicts_regles_originales"]["HR3"]["verdict"] == "sans verdict (R4 ≈ défense figée)"
    r = calc(fabriquer_e1(graine=8, nb_cos_eleves=50))
    assert r["sante"]["etat_global"]["T4"] is False


def test_c12_2_T4_un_seul_budget_suffit(b_petit):
    e1 = fabriquer_e1(9, melanger=False)
    for t in taches_de(e1):
        if t["code_delta"] == 2 and t["instance"] < 60:
            t["regles"][R4]["par_tour"]["cos_consecutif"] = [1.0] * 8
    r = calc(e1)
    assert r["sante"]["1"]["T4"]["declenche"] is False and r["sante"]["2"]["T4"]["declenche"] is True
    assert r["sante"]["etat_global"]["T4"] is True


def test_c12_2_T5_condition_a_unilaterale_et_condition_b_bilaterale(b_petit):
    # (a) R3 : standard − renforcé > 0,01 ; le contraste (b) est nul pour les variantes non touchées
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):
        v = t["regles"]["R3"]
        v["V_iii_standard"] = v["V_iii_renforce"] + 0.02
        v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
    t5 = calc(e1)["sante"]["1"]["T5"]
    assert t5["declenche"] and t5["a_unilaterale_declenche"] is True
    # standard − renforcé NÉGATIF et grand : (a) est unilatérale ; (b) (a−b) reste ≈ 0
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):
        for nom in ib.NOMS_VARIANTES:
            v = t["regles"][nom]
            v["V_iii_standard"] = max(0.0, v["V_iii_renforce"] - 0.05)
            v["V_iii_final"] = min(v["V_iii_standard"], v["V_iii_renforce"])
    r = calc(e1)
    t5 = r["sante"]["1"]["T5"]
    assert min(t5["standard_moins_renforce"].values()) < -0.01
    assert t5["declenche"] is False and t5["a_unilaterale_declenche"] is False and t5["b_bilaterale_declenche"] is False
    # (b) seule : R2 avec standard − renforcé = −0,03, R3 avec +0,005 -> |a − b| de R3 = 0,035 > 0,01
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):
        v2, v3 = t["regles"]["R2"], t["regles"]["R3"]
        v2["V_iii_standard"] = max(0.0, v2["V_iii_renforce"] - 0.03)
        v2["V_iii_final"] = min(v2["V_iii_standard"], v2["V_iii_renforce"])
        v3["V_iii_standard"] = v3["V_iii_renforce"] + 0.005
        v3["V_iii_final"] = min(v3["V_iii_standard"], v3["V_iii_renforce"])
    t5 = calc(e1)["sante"]["1"]["T5"]
    assert max(t5["standard_moins_renforce"].values()) <= 0.01 and t5["plus_grand_abs_ecart_de_contraste"] > 0.01
    assert t5["declenche"] is True and t5["b_bilaterale_declenche"] is True and t5["a_unilaterale_declenche"] is False
    # (b) dans l'autre sens : signe de (a − b) négatif
    e1 = fabriquer_e1(10)
    for t in taches_de(e1):
        v2, v3 = t["regles"]["R2"], t["regles"]["R3"]
        v2["V_iii_standard"] = v2["V_iii_renforce"] + 0.005
        v2["V_iii_final"] = min(v2["V_iii_standard"], v2["V_iii_renforce"])
        v3["V_iii_standard"] = max(0.0, v3["V_iii_renforce"] - 0.03)
        v3["V_iii_final"] = min(v3["V_iii_standard"], v3["V_iii_renforce"])
    t5 = calc(e1)["sante"]["1"]["T5"]
    assert t5["ecart_de_contraste"]["R3"]["a_moins_b"] < -0.01 and t5["b_bilaterale_declenche"] is True


def test_c12_2_T6_derive_des_fausses_alertes(b_petit):
    assert calc(fabriquer_e1(graine=11, derive_fpr=0.0))["sante"]["etat_global"]["T6"] is False
    assert calc(fabriquer_e1(graine=11, derive_fpr=0.002))["sante"]["etat_global"]["T6"] is True
    assert calc(fabriquer_e1(graine=11, derive_fpr=-0.002))["sante"]["etat_global"]["T6"] is True     # bilatéral
    r = calc(fabriquer_e1(graine=11, derive_fpr=0.002))
    for k in ("HR1", "HR0", "HR3", "lois_tenues_ii"):
        assert r["verdicts_bruts_replication"][k]["verdict"] == "non jugeable (santé)"


def test_c12_2_T2_les_quatre_conditions(b_petit):
    e1 = fabriquer_e1(12)          # trop beau : une variante avec moyenne de V >= 0,99
    for t in taches_de(e1):
        fixer_V(t["regles"]["R0"], 0.995)
    r = calc(e1)
    assert r["sante"]["1"]["T2"]["une_variante_moy_V_ge_0_99"] and r["sante"]["etat_global"]["T2"]
    e1 = fabriquer_e1(12)          # jeu trop mauvais : les cinq moyennes de V <= 0,02
    for t in taches_de(e1):
        for nom in ib.NOMS_VARIANTES:
            fixer_V(t["regles"][nom], 0.01)
    r = calc(e1)
    assert r["sante"]["1"]["T2"]["cinq_variantes_moy_V_le_0_02"] and r["sante"]["1"]["jeu_degenere"]
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "non jugeable (santé)"
    assert r["classes"]["table_A"]["classe"] == "non concluant : jeu dégénéré"
    r = calc(fabriquer_e1(graine=12, effet_r3=0.35))      # est de (R3, V) > 0,30
    assert r["sante"]["1"]["T2"]["est_R3_V_gt_0_30"] and r["sante"]["etat_global"]["T2"]
    e1 = fabriquer_e1(12)          # |est(k, X̄)| > 0,30 pour une variante autre que R2 (positif)
    for t in taches_de(e1):
        t["regles"]["R1"]["exploitabilite_moyenne_tours"] = 1.0
        t["regles"]["R2"]["exploitabilite_moyenne_tours"] = 0.2
    assert calc(e1)["sante"]["1"]["T2"]["un_abs_est_Xbarre_gt_0_30"]
    e1 = fabriquer_e1(12)          # négatif : bilatéral
    for t in taches_de(e1):
        t["regles"]["R1"]["exploitabilite_moyenne_tours"] = 0.2
        t["regles"]["R2"]["exploitabilite_moyenne_tours"] = 0.8
    assert calc(e1)["sante"]["1"]["T2"]["un_abs_est_Xbarre_gt_0_30"]


def test_c12_2_T2_ne_se_declenche_pas_pour_un_seul_budget_de_mauvais_et_se_declenche_pour_un_seul_budget_trop_beau(b_petit):
    e1 = fabriquer_e1(13)
    for t in taches_de(e1):
        if t["code_delta"] == 2:
            fixer_V(t["regles"]["R0"], 0.995)
    r = calc(e1)
    assert r["sante"]["1"]["T2"]["declenche"] is False and r["sante"]["2"]["T2"]["declenche"] is True
    assert r["sante"]["etat_global"]["T2"] is True


# =============================================================================================
# § 12.2 — frontière numérique : marque et héritage
# =============================================================================================
def test_c12_2_frontiere_numerique_marque_les_quantites_a_moins_de_epsilon():
    r = ib.classe_table_B("R3", bornes(ib.M + 0.5e-9, 0.06))
    assert r["ligne"] == 1 and r["frontiere"] is True and r["frontiere_propre"] is True
    assert r["comparaisons_a_la_frontiere"][0]["quantite"] == "bas(B8)"
    assert ib.classe_table_B("R3", bornes(ib.M + 2e-9, 0.06))["frontiere"] is False
    r = ib.classe_table_B("R3", bornes(1e-9, 0.05))                      # inclusif : |x − seuil| ≤ ε
    assert r["ligne"] == 4 and r["frontiere"] is True
    r = ib.classe_table_B("R3", bornes(1.0000001e-9, 0.05))
    assert r["ligne"] == 4 and r["frontiere"] is False
    # le chemin évalué seul compte : la ligne 1 décide, la comparaison de la ligne 3 n'est pas examinée
    r = ib.classe_table_B("R3", bornes(0.05, 0.06, -ib.M + 1e-12, ib.M - 1e-12))
    assert r["ligne"] == 1 and r["frontiere"] is False
    assert ib.classe_table_C({"B8": (-ib.S5 + 1e-10, 0.05), "E8": (0, 0)})["frontiere"] is True
    a = ib.classe_table_A({c: {"est": ib.M + 1e-10, "bas_B2": 0.01, "haut_B2": 0.1,
                               "moyennes_V": {n: 0.12 for n in ib.NOMS_VARIANTES}} for c in (1, 2)})
    assert a["ligne"] == 2 and a["frontiere"] is True


def test_c12_2_frontiere_sans_court_circuit_dans_une_ligne_examinee():
    """Ligne 3 de la table B : « bas(E8) > −m ET haut(E8) < m » ; la première comparaison est fausse mais la seconde,
    à la frontière, doit marquer quand même (aucun court-circuit)."""
    r = ib.classe_table_B("R3", bornes(-0.03, 0.01, -0.05, ib.M - 1e-10))
    assert r["ligne"] == 6 and r["frontiere"] is True
    assert any(p["quantite"] == "haut(E8)" for p in r["comparaisons_a_la_frontiere"])
    # table A, ligne 2 : « est ≥ m ET bas > 0 » aux deux budgets, tout est évalué même si le premier budget échoue
    a = ib.classe_table_A({1: {"est": 0.0, "bas_B2": -1.0, "haut_B2": 1.0, "moyennes_V": {n: 0.12 for n in ib.NOMS_VARIANTES}},
                           2: {"est": ib.M + 1e-10, "bas_B2": 0.5, "haut_B2": 1.0, "moyennes_V": {n: 0.12 for n in ib.NOMS_VARIANTES}}})
    assert a["ligne"] == 4 and a["frontiere"] is True
    # table C, ligne 2 : « haut < 0 ET bas > −S5 »
    r = ib.classe_table_C({"B8": (-ib.S5 + 1e-10, 0.5)})
    assert r["frontiere"] is True


def test_c12_2_la_comparaison_de_valeurs_brutes_ne_marque_pas_mais_cos_moyen_oui(b_petit):
    """§ 8 : cos_moyen (une moyenne calculée) compte ; le plus grand poids de R3 (valeur brute) non."""
    e1 = fabriquer_e1(80, melanger=False)
    tache(e1, 1, 3)["regles"][R4]["par_tour"]["cos_consecutif"] = [0.999 - 5e-10] * 8
    r = calc(e1)
    t4 = r["sante"]["1"]["T4"]
    assert t4["declenche"] is False and t4["frontiere"] is True and t4["nb_taches_a_la_frontiere"] == 1
    assert r["sante"]["frontiere_globale"]["T4"] is True and r["sante"]["frontiere_globale"]["T3"] is False
    assert r["sante"]["2"]["T4"]["frontiere"] is False
    # héritage : T4 entre dans HR3 (ligne 2 examinée) mais ni dans HR1 ni dans HR0 ni dans (ii)
    vb = r["verdicts_bruts_replication"]
    assert vb["HR3"]["frontiere"] is True and "T4" in vb["HR3"]["heritee_de"]
    assert vb["HR1"]["frontiere"] is False and vb["HR0"]["frontiere"] is False and vb["lois_tenues_ii"]["frontiere"] is False
    assert r["verdicts_regles_originales"]["HR3"]["frontiere"] is True
    # un cos_moyen à plus de ε du seuil : pas de marque
    e1 = fabriquer_e1(80, melanger=False)
    tache(e1, 1, 3)["regles"][R4]["par_tour"]["cos_consecutif"] = [0.999 - 5e-9] * 8
    assert calc(e1)["sante"]["1"]["T4"]["frontiere"] is False


@pytest.mark.parametrize("modif, controle", [
    ("T6", "T6"), ("T5", "T5"), ("T2", "T2"),
])
def test_c12_2_la_marque_d_un_controle_est_heritee_par_les_quatre_verdicts(b_petit, modif, controle):
    e1 = fabriquer_e1(81)
    if modif == "T6":                                   # |moy(fpr) − α| = 0,001 − 5e-10 pour R0 : pas déclenché, marqué
        for t in taches_de(e1):
            t["regles"]["R0"]["fpr_final"] = 0.011 - 5e-10
    elif modif == "T5":                                 # standard − renforcé = 0,01 − 5e-10 pour R3 : pas déclenché, marqué
        for t in taches_de(e1):
            for nom in ib.NOMS_VARIANTES:
                fixer_V(t["regles"][nom], 0.2)
            v = t["regles"]["R3"]
            v["V_iii_standard"] = 0.2 + 0.01 - 5e-10
    else:                                               # moy(R0, V) = 0,99 − 5e-10 : pas déclenché, marqué
        for t in taches_de(e1):
            fixer_V(t["regles"]["R0"], 0.99 - 5e-10)
    r = calc(e1)
    assert r["sante"]["etat_global"][controle] is False, r["sante"]["1"][controle]
    assert r["sante"]["frontiere_globale"][controle] is True
    vb = r["verdicts_bruts_replication"]
    for k in ("HR1", "HR0", "HR3", "lois_tenues_ii"):
        assert vb[k]["frontiere"] is True and controle in vb[k]["heritee_de"], (k, vb[k])
    for k in ("HR1", "HR0", "HR3"):
        assert r["verdicts_apres_declencheurs"][k]["frontiere"] is True
    assert r["issues_globales"]["brute"]["frontiere"] is True and r["issues_globales"]["apres_declencheurs"]["frontiere"] is True


def test_c12_2_la_marque_d_un_controle_declenche_de_justesse_est_heritee_aussi(b_petit):
    e1 = fabriquer_e1(81)
    for t in taches_de(e1):
        t["regles"]["R0"]["fpr_final"] = 0.011 + 5e-10   # |moy − α| = 0,001 + 5e-10 : déclenché ET marqué
    r = calc(e1)
    assert r["sante"]["etat_global"]["T6"] is True and r["sante"]["frontiere_globale"]["T6"] is True
    assert r["verdicts_bruts_replication"]["HR1"]["verdict"] == "non jugeable (santé)"
    assert r["verdicts_bruts_replication"]["HR1"]["frontiere"] is True


def test_c12_2_la_marque_d_une_classe_est_heritee_par_le_verdict_le_declencheur_et_l_issue(b_petit):
    """Classe (R0, V) à la frontière -> HR0 -> TR3 -> verdicts après déclencheurs -> issues."""
    e1 = fabriquer_e1(82)
    _imposer(e1, "R0", "V_iii_final", [0.02 + 5e-10] * 100, base_r2=0.5)
    r = calc(e1)
    cl = r["classes"]["table_B"]["R0"]
    assert cl["1"]["classe"] == "R0 > R2" and cl["1"]["frontiere"] is True
    assert r["classes_a_la_frontiere"] and "table_B/R0/budget 1" in r["classes_a_la_frontiere"]
    vb = r["verdicts_bruts_replication"]
    assert vb["HR0"]["verdict"] == "répliquée" and vb["HR0"]["frontiere"] is True
    assert "table_B/R0/budget 1" in vb["HR0"]["heritee_de"]
    assert vb["HR1"]["frontiere"] is False
    d = r["declencheurs_audit"]
    assert d["TR3"]["declenche"] is True and d["TR3"]["frontiere"] is True
    assert d["TR4"]["frontiere"] is True and d["au_moins_un"]["frontiere"] is True
    assert all(r["verdicts_apres_declencheurs"][k]["frontiere"] for k in ib.CLES_VERDICTS_REPLICATION)
    assert r["issues_globales"]["apres_declencheurs"]["frontiere"] is True


def test_c12_2_marques_des_declencheurs_TR1_et_TR2():
    seuil = ib.Z_ETOILE * ib.sigma_pi(0.06, 0.08)
    e = ib.ecart_replication(_faux_contrastes(0.10 + seuil + 5e-10, 0.06), _fausse_analyse(0.10, 0.08))
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    assert d["TR1"]["declenche"] is True and d["TR1"]["frontiere"] is True and d["au_moins_un"]["frontiere"] is True
    e = ib.ecart_replication(_faux_contrastes(0.10 + 0.001 - 5e-10, 0.06), _fausse_analyse(0.10, 0.08))
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    assert d["TR2"]["declenche"] is True and d["TR2"]["frontiere"] is True
    e = ib.ecart_replication(_faux_contrastes(0.10 + 0.05, 0.06), _fausse_analyse(0.10, 0.08))
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    assert d["TR1"]["frontiere"] is False and d["TR2"]["frontiere"] is False and d["au_moins_un"]["frontiere"] is False


def test_c12_2_marques_des_declencheurs_TR3_et_TR4_heritees():
    e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
    d = ib.declencheurs_audit(e, _cl_r0("R0 > R2", "≈", f1=True), _vb())
    assert d["TR3"]["frontiere"] is True and d["TR4"]["frontiere"] is False
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb(f0=True))
    assert d["TR4"]["frontiere"] is True and d["TR3"]["frontiere"] is False
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb(f1=True))
    assert d["TR4"]["frontiere"] is True


def test_c12_2_marque_des_verdicts_du_paragraphe_9(b_petit):
    cl = _classes_synth()
    cl["table_B"]["R0"]["1"]["frontiere"] = True
    v = ib.verdicts_regles_originales(cl, ETAT_OK, FRONT_OK)
    assert v["HR0"]["frontiere"] is True and v["HR1"]["frontiere"] is False and v["HR3"]["frontiere"] is False
    cl["table_A"]["frontiere"] = True
    assert ib.verdicts_regles_originales(cl, ETAT_OK, FRONT_OK)["HR1"]["frontiere"] is True
    # HR3 : T4 marqué est hérité ; si T4 est déclenché les classes de R4 ne sont plus examinées
    cl = _classes_synth()
    cl["table_B"]["R4"]["2"]["frontiere"] = True
    assert ib.verdicts_regles_originales(cl, ETAT_OK, FRONT_OK)["HR3"]["frontiere"] is True
    assert ib.verdicts_regles_originales(cl, dict(ETAT_OK, T4=True), FRONT_OK)["HR3"]["frontiere"] is False
    assert ib.verdicts_regles_originales(_classes_synth(), ETAT_OK, dict(FRONT_OK, T4=True))["HR3"]["frontiere"] is True


# =============================================================================================
# § 12.3 — cas (a) à (e)
# =============================================================================================
@pytest.fixture(scope="session")
def cas_12_3():
    ana, res = pieces()
    return ib.cas_synthetiques_12_3(P_RES.read_bytes(), ana, res)


def test_c12_3_b_cas_sain_aucun_declencheur_aucun_arret(cas_12_3):
    b = cas_12_3["b_cas_sain"]
    assert b["ok"] and b["comptes_max"] == 0 and b["TR1"] is False and b["TR2"] is False
    assert b["arret"] is False and b["code_de_sortie"] == 0 and b["lecture_autorisee"] is True


def test_c12_3_c_R3_decale_de_plus_0_06_declenche_TR1_avec_z_positif(cas_12_3):
    c = cas_12_3["c_R3_plus_0_06"]
    assert c["ok"] and c["TR1"] is True and all(v > 2.4977 for v in c["z_R3"].values()) and len(c["z_R3"]) == 2


def test_c12_3_d_R3_decale_de_moins_0_03_borne_a_zero_declenche_TR1_avec_z_negatif(cas_12_3):
    d = cas_12_3["d_R3_moins_0_03"]
    assert d["ok"] and d["TR1"] is True and all(v < -2.4977 for v in d["z_R3"].values()) and len(d["z_R3"]) == 2


def test_c12_3_e_trois_taches_identiques_arretent_deux_non(cas_12_3):
    e3, e2 = cas_12_3["e_3_taches_gardees"], cas_12_3["e_2_taches_gardees"]
    assert (e3["compte_R1_V"], e3["arret_graines_non_neuves"], e3["code_de_sortie"], e3["ok"]) == (3, True, 3, True)
    assert (e2["compte_R1_V"], e2["arret_graines_non_neuves"], e2["code_de_sortie"], e2["ok"]) == (2, False, 0, True)
    assert cas_12_3["ok"] is True


def _restaurer(e1_variante, e1_originale, champs, nom, k, c=1):
    """Remet à leur valeur originale exacte les `champs` de `nom` pour les k premières tâches du budget c."""
    orig = {(t["code_delta"], t["instance"]): t for t in e1_originale["resultat"]["resultats"]}
    for t in e1_variante["resultat"]["resultats"]:
        if t["code_delta"] == c and t["instance"] < k:
            for ch in champs:
                t["regles"][nom][ch] = orig[(c, t["instance"])]["regles"][nom][ch]


@pytest.mark.parametrize("champs, mesure, arrete", [
    (("V_iii_final", "V_iii_standard", "V_iii_renforce"), "V_iii_final", True),
    (("exploitabilite_moyenne_tours",), "exploitabilite_moyenne_tours", True),
    (("ii_final",), "ii_final", True),
    (("exploitabilite_finale",), None, False),
])
def test_c12_3_e_les_trois_mesures_comptent_et_pas_l_exploitabilite_finale(champs, mesure, arrete):
    """Cas (e) étendu : trois tâches d'une seule variante restent identiques à l'original sur V, X̄ ou (ii) : arrêt ;
    sur l'exploitabilité finale (non lue par la règle des graines neuves) : aucun arrêt."""
    ana, res = pieces()
    orig = ib.lire_json_octets(P_RES.read_bytes(), "E1")
    e1 = ib._variante(P_RES.read_bytes(), lambda t: ib._decaler_b(t, 0.01))
    for t in e1["resultat"]["resultats"]:                     # l'exploitabilité finale aussi décalée pour tout le monde
        for v in t["regles"].values():
            v["exploitabilite_finale"] += 1e-6
    _restaurer(e1, orig, champs, "R0", 3)
    s = ib.conclure({**ib.calculer_B(e1, ib.RACINE_COURSE_ORIGINALE, ib.RACINE_TENUE_COURSE_ORIGINALE, ana, res),
                     "comparaison_A_B": {"evaluee": False}})
    assert s["comptes_graines_neuves"]["arret_graines_non_neuves"] is arrete
    if mesure is not None:
        assert s["comptes_graines_neuves"]["comptes"]["R0"][mesure] == 3
    assert s["code_de_sortie"] == (3 if arrete else 0) and s["lecture_autorisee"] is (not arrete)


# =============================================================================================
# Réplication de bout en bout sur pièces synthétiques (E1, E2, E3, E5 et leurs compagnons)
# =============================================================================================
class Monte:
    """Pièces d'une réplication synthétique écrites dans un dossier temporaire."""


def _texte_et_racines(graine: int, grand: bool = True):
    i = 0
    while True:
        texte = f"Préenregistrement synthétique {graine}-{i} λ\n".encode("utf-8")
        h = hashlib.sha256(texte).hexdigest()
        rho, rho_t = ib.regle_d_derivation(h)
        try:
            ib.regle_d_gardes(rho, rho_t)
        except ib.Arret:
            i += 1
            continue
        if not grand or (rho > 2 ** 63 and rho_t > 2 ** 63):
            return texte, h, rho, rho_t
        i += 1


def monter(tmp_path: Path, graine: int = 0, *, grand: bool = True, effet_r3: float = 0.10, e1_modif=None,
           e1_octets=None, e2_modif=None, e5_modif=None, e5_octets=None, e3_octets=None, sceller=True) -> Monte:
    """Écrit E3 (préenregistrement), E2 (manifeste), E1 (résultats synthétiques) et E5 (analyse « de A », ici
    produite par B lui-même à partir de l'E1 sain), chacun avec son compagnon. `*_modif` : fonction appliquée à
    l'objet avant écriture ; `*_octets` : fonction appliquée aux octets après écriture JSON ; `sceller` : refait les
    compagnons après modification (pour tester la garde de contenu et non celle du compagnon)."""
    m = Monte()
    m.dossier = tmp_path
    texte, m.h, m.rho, m.rho_t = _texte_et_racines(graine, grand)
    m.p_e3 = tmp_path / "prereg.md"
    ecrire_avec_compagnon(m.p_e3, texte if e3_octets is None else e3_octets(texte))
    m.e2 = {"run_id": "synthetique", "config": {
        "racine": m.rho, "racine_tenue": m.rho_t, "racine_chaine": str(m.rho), "racine_tenue_chaine": str(m.rho_t),
        "prereg_sha256": m.h, "lambda": 0.3, "reference": "moyenne", "config": {"n_instances": 100},
        "config_sha256": ib.EMPREINTE_CONFIG}, "preenregistrement": {"sha256": m.h}}
    if e2_modif:
        e2_modif(m.e2)
    m.p_e2 = tmp_path / "manifeste.json"
    m.sha_e2 = ecrire_avec_compagnon(m.p_e2, json.dumps(m.e2, ensure_ascii=False).encode("utf-8"))
    m.e1 = fabriquer_e1(graine, m.rho, m.rho_t, effet_r3=effet_r3)
    m.e1["manifeste_sha256"] = m.sha_e2
    ana, res = pieces()
    sain = ib.calculer_B(m.e1, m.rho, m.rho_t, ana, res)
    m.e5 = {"run_id": "synthetique", "manifeste_sha256": m.sha_e2, "resultat": sain["resultat"]}
    m.e1_sain = copy.deepcopy(m.e1)
    if e1_modif:
        e1_modif(m.e1)
    octets_e1 = json.dumps(m.e1, ensure_ascii=False).encode("utf-8")
    if e1_octets:
        octets_e1 = e1_octets(octets_e1)
    m.p_e1 = tmp_path / "resultats.json"
    ecrire_avec_compagnon(m.p_e1, octets_e1)
    if e5_modif:
        e5_modif(m.e5)
    octets_e5 = json.dumps(m.e5, ensure_ascii=False).encode("utf-8")
    if e5_octets:
        octets_e5 = e5_octets(octets_e5)
    m.p_e5 = tmp_path / "analyse-A.json"
    ecrire_avec_compagnon(m.p_e5, octets_e5)
    return m


def lancer(m: Monte, **kw):
    return ib.analyser_fichiers(mode="replication", resultats=m.p_e1, analyse_originale=P_ANA, resultats_originaux=P_RES,
                                prereg=m.p_e3, manifeste=m.p_e2, analyse_A=m.p_e5, **kw)


def test_c12_3_replication_synthetique_saine_de_bout_en_bout(b_petit, tmp_path):
    m = monter(tmp_path)
    assert m.rho > 2 ** 63 and m.rho_t > 2 ** 63
    s = lancer(m)
    assert s["code_de_sortie"] == 0 and s["lecture_autorisee"] is True and s["motifs_arret"] == []
    assert s["comparaison_A_B"]["evaluee"] and s["comparaison_A_B"]["concordance"] is True
    assert s["comparaison_A_B"]["ecart_maximal_absolu"] == 0.0
    assert s["H"] == m.h and s["racine_de_reechantillonnage"] == str(m.rho)
    assert s["racines"]["rho"] == str(m.rho) and s["racines"]["rho_t"] == str(m.rho_t)
    assert s["manifeste_E2"]["run_id"] == "synthetique" and s["manifeste_E2"]["prereg_sha256"] == m.h
    assert s["verdicts_bruts_replication"]["HR1"]["verdict"] == "répliquée"
    assert s["comptes_graines_neuves"]["arret_graines_non_neuves"] is False
    roles = [f["role"] for f in s["empreintes_fichiers"]]
    assert roles == ["E1 résultats analysés", "E4 analyse originale", "E4 résultats originaux",
                     "E3 préenregistrement scellé", "E2 manifeste du run", "E5 analyse de A"]
    assert all(re.fullmatch(r"[0-9a-f]{64}", f["sha256"]) for f in s["empreintes_fichiers"])
    json.dumps(s, allow_nan=False)



def test_c12_3_les_cles_de_la_sortie_sont_celles_du_paragraphe_11_1(b_petit, tmp_path):
    s = lancer(monter(tmp_path))
    attendues = {"implementation", "specification", "mode", "H", "racines", "racine_de_reechantillonnage",
                 "manifeste_E2", "run_id", "resultat", "intervalles", "sante", "classes", "verdicts_regles_originales",
                 "verdicts_bruts_replication", "ecart_de_replication", "declencheurs_audit",
                 "verdicts_apres_declencheurs", "classes_a_la_frontiere", "comptes_graines_neuves", "comparaison_A_B",
                 "motifs_arret", "lecture_autorisee", "code_de_sortie", "issues_globales", "options",
                 "empreintes_fichiers", "ordre_des_lectures", "meta_non_deterministe"}
    assert attendues <= set(s), attendues - set(s)
    assert set(s["resultat"]) == {"1", "2"} and len(s["resultat"]["1"]["contrastes_contre_R2"]) == 16
    assert set(s["intervalles"]["1"]["R3 - R2 (V_iii_final)"]) == {"B2", "B8", "E8"}
    assert set(s["issues_globales"]) >= {"V0", "brute", "apres_declencheurs"}


def test_c12_3_E5_n_est_lue_qu_apres_le_calcul_de_B(b_petit, tmp_path):
    s = lancer(monter(tmp_path))
    j = s["ordre_des_lectures"]
    i_calcul = next(i for i, x in enumerate(j) if x.startswith("calcul de B terminé"))
    i_e5 = next(i for i, x in enumerate(j) if "E5" in x)
    assert i_calcul < i_e5 == len(j) - 1
    assert [x for x in j if "E5" in x] == ["lecture de E5 analyse de A"]


def test_c12_3_les_nombres_de_B_ne_dependent_pas_de_E5(b_petit, tmp_path):
    a = lancer(monter(tmp_path / "a" if (tmp_path / "a").mkdir() is None else tmp_path))
    deriv = lambda e5: e5["resultat"]["1"]["contrastes_contre_R2"]["R1 - R2 (exploitabilite_moyenne_tours)"].update(moyenne=9.9)
    (tmp_path / "b").mkdir()
    b = lancer(monter(tmp_path / "b", e5_modif=deriv))
    for cle in ("resultat", "intervalles", "classes", "sante", "verdicts_bruts_replication", "comptes_graines_neuves"):
        assert a[cle] == b[cle], cle
    assert b["comparaison_A_B"]["concordance"] is False


def _alterer(c, lib, champ, delta, quantile=None):
    def f(e5):
        stat = e5["resultat"][c]["contrastes_contre_R2"][lib]
        if quantile:
            stat["quantiles"][quantile] += delta
        else:
            stat[champ] += delta
    return f


@pytest.mark.parametrize("c, lib, champ, quantile", [
    ("1", "R3 - R2 (V_iii_final)", "moyenne", None), ("2", "R3 - R2 (V_iii_final)", "ecart_type", None),
    ("1", "R0 - R2 (V_iii_final)", "moyenne", None), ("2", "R0 - R2 (V_iii_final)", "moyenne", None),
    ("1", "R4[moyenne,λ=0.3] - R2 (V_iii_final)", "moyenne", None), ("2", "R0 - R2 (ii_final)", "moyenne", None),
    ("1", "R1 - R2 (exploitabilite_moyenne_tours)", "moyenne", None), ("2", "R1 - R2 (exploitabilite_moyenne_tours)", "ecart_type", None),
    ("1", "R3 - R2 (V_iii_final)", None, "q0.003125"), ("2", "R0 - R2 (V_iii_final)", None, "q0.996875"),
    ("1", "R0 - R2 (ii_final)", None, "q0.0125"), ("2", "R1 - R2 (exploitabilite_moyenne_tours)", None, "q0.95"),
])
def test_c12_3_discordance_de_niveau_arret_sur_chacun_des_cinq_contrastes_donne_le_code_3(b_petit, tmp_path, c, lib,
                                                                                         champ, quantile):
    m = monter(tmp_path, e5_modif=_alterer(c, lib, champ, 1e-6, quantile))
    s = lancer(m)
    assert s["comparaison_A_B"]["discordance_a_arret"] is True and s["comparaison_A_B"]["concordance"] is False
    assert s["code_de_sortie"] == 3 and s["lecture_autorisee"] is False
    assert any("discordance A/B" in x for x in s["motifs_arret"])
    assert any(lib in x for x in s["comparaison_A_B"]["motifs"])
    assert s["issues_globales"]["brute"]["ligne"] == 1


@pytest.mark.parametrize("c, lib, champ, quantile", [
    ("1", "R0 - R2 (exploitabilite_moyenne_tours)", "moyenne", None), ("2", "R3 - R2 (ii_final)", "ecart_type", None),
    ("1", "R1 - R2 (V_iii_final)", "moyenne", None), ("2", "R4[moyenne,λ=0.3] - R2 (exploitabilite_finale)", "moyenne", None),
    ("1", "R3 - R2 (exploitabilite_finale)", None, "q0.025"),
])
def test_c12_3_discordance_sur_un_des_onze_autres_contrastes_est_une_alerte_pas_un_arret(b_petit, tmp_path, c, lib, champ,
                                                                                         quantile):
    s = lancer(monter(tmp_path, e5_modif=_alterer(c, lib, champ, 1e-6, quantile)))
    cmp_ = s["comparaison_A_B"]
    assert cmp_["discordance_a_arret"] is False and cmp_["concordance"] is False
    assert [(a["budget"], a["contraste"]) for a in cmp_["alertes_de_discordance"]] == [(c, lib)]
    assert s["code_de_sortie"] == 0 and s["lecture_autorisee"] is True and s["motifs_arret"] == []


@pytest.mark.parametrize("delta, doit_arreter", [(0.0, False), (5e-10, False), (9e-10, False), (2e-9, True), (-2e-9, True),
                                                  (-9e-10, False)])
def test_c12_3_tolerance_de_concordance_1e_9_sur_un_contraste_a_arret(b_petit, tmp_path, delta, doit_arreter):
    """Contraste (R1, X̄) : un des cinq à arrêt, qui n'entre pas dans z_π (les deux contrastes primaires, eux, sont
    aussi soumis à |z_π(A) − z_π(B)| ≤ 1e-9, voir l'essai suivant)."""
    s = lancer(monter(tmp_path, e5_modif=_alterer("1", "R1 - R2 (exploitabilite_moyenne_tours)", "moyenne", delta)))
    assert s["comparaison_A_B"]["discordance_a_arret"] is doit_arreter
    assert s["comparaison_A_B"]["z_pi"]["ok"] is True
    assert s["code_de_sortie"] == (3 if doit_arreter else 0)


def test_c12_3_z_pi_de_A_et_de_B_doivent_concorder_a_1e_9_meme_si_la_moyenne_concorde_a_1e_9(b_petit, tmp_path):
    """Un écart de 5e-10 sur la moyenne d'un contraste primaire respecte la tolérance de la moyenne, mais déplace
    z_π d'environ 5e-10/σ_π >> 1e-9 : discordance de niveau arrêt (§ 11.2)."""
    s = lancer(monter(tmp_path, e5_modif=_alterer("1", "R3 - R2 (V_iii_final)", "moyenne", 5e-10)))
    cmp_ = s["comparaison_A_B"]
    assert cmp_["detail_par_contraste"]["1"]["R3 - R2 (V_iii_final)"]["ok"] is True
    assert cmp_["z_pi"]["ok"] is False and cmp_["discordance_a_arret"] is True and s["code_de_sortie"] == 3
    assert any("z_π" in x for x in cmp_["motifs"])


@pytest.mark.parametrize("modif", [lambda s: s.update(n=99), lambda s: s.update(zeros_exacts=s["zeros_exacts"] + 1)])
def test_c12_3_n_et_zeros_exacts_differents_sur_un_contraste_a_arret(b_petit, tmp_path, modif):
    s = lancer(monter(tmp_path, e5_modif=lambda e5: modif(e5["resultat"]["2"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"])))
    assert s["comparaison_A_B"]["discordance_a_arret"] is True and s["code_de_sortie"] == 3


def test_c12_3_discordance_de_classe_ou_de_verdict_hors_frontiere_arrete(b_petit, tmp_path):
    """E5 dont les nombres de (R3, V) changent la classe de la table A : discordance de classe et de verdict."""
    def faux(e5):
        for c in "12":
            st = e5["resultat"][c]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]
            st["moyenne"] = -0.05
            st["quantiles"] = {k: -0.05 + 0.001 * i for i, k in enumerate(st["quantiles"])}
    s = lancer(monter(tmp_path, e5_modif=faux))
    cmp_ = s["comparaison_A_B"]
    assert cmp_["classes"]["identiques"] is False and cmp_["verdicts_et_declencheurs"]["identiques"] is False
    assert any("classe différente hors frontière" in x for x in cmp_["motifs"])
    assert any("verdict ou déclencheur différent hors frontière" in x for x in cmp_["motifs"])
    assert s["code_de_sortie"] == 3


def test_c12_3_les_classes_verdicts_et_declencheurs_de_A_utilisent_les_controles_de_B(b_petit, tmp_path):
    """Point 14 : le désaccord éventuel ne vient jamais des contrôles de santé, que B recalcule depuis E1."""
    s = lancer(monter(tmp_path, effet_r3=0.0))
    assert s["comparaison_A_B"]["classes"]["identiques"] and s["comparaison_A_B"]["verdicts_et_declencheurs"]["identiques"]
    assert s["declencheurs_audit"]["TR4"]["declenche"] is True and s["code_de_sortie"] == 0


def test_c12_3_difference_a_la_frontiere_n_est_pas_un_arret_et_la_valeur_retenue_est_celle_de_A():
    cb = {"table_A": {"ligne": 2, "classe": "HR1 confirmée", "frontiere": True},
          "table_B": {"R0": {"1": {"ligne": 3, "classe": "≈", "frontiere": False}}}, "table_Bprime": {}, "table_C": {}}
    ca = {"table_A": {"ligne": 4, "classe": "HR1 non démontrée", "frontiere": False},
          "table_B": {"R0": {"1": {"ligne": 3, "classe": "≈", "frontiere": False}}}, "table_Bprime": {}, "table_C": {}}
    r = ib.comparer_classes(cb, ca)
    assert r["identiques"] is True and r["elements_a_la_frontiere"] == ["table_A"]
    d = r["differences"][0]
    assert d["chemin"] == "table_A" and d["a_la_frontiere"] is True and d["valeur_retenue_pour_la_lecture"] == [4, "HR1 non démontrée"]
    # la marque de l'un OU de l'autre côté suffit
    assert ib.comparer_classes(ca, cb)["identiques"] is True
    # sans marque : arrêt
    cb["table_A"]["frontiere"] = False
    assert ib.comparer_classes(cb, ca)["identiques"] is False


def test_c12_3_comparer_contrastes_ok_ne_vaut_que_dans_la_tolerance(sortie_originale, analyse_a):
    cb = {c: sortie_originale["resultat"][c]["contrastes_contre_R2"] for c in "12"}
    ca = ib.contrastes_depuis_analyse(analyse_a, "A")
    assert all(d["ok"] for c in "12" for d in ib.comparer_contrastes(cb, ca)[c].values())
    ca2 = copy.deepcopy(ca)
    ca2["1"]["R0 - R2 (V_iii_final)"]["quantiles"]["q0.0125"] += 1.5e-9
    det = ib.comparer_contrastes(cb, ca2)
    assert det["1"]["R0 - R2 (V_iii_final)"]["ok"] is False and det["1"]["R0 - R2 (V_iii_final)"]["niveau"] == "arrêt"
    assert det["1"]["R3 - R2 (V_iii_final)"]["ok"] is True
    assert [d["niveau"] for d in det["1"].values()].count("arrêt") == 5


def test_c12_3_les_options_n_alterent_aucun_seuil_et_la_valeur_est_ecrite(b_petit, tmp_path):
    s0 = lancer(monter(tmp_path))
    assert s0["options"] == {"mode": "replication", "plomberie_fausse_V0": False, "empreinte_E1_imposee_en_ligne_de_commande": None}
    assert s0["issues_globales"]["brute"]["ligne"] != 1
    (tmp_path / "b").mkdir()
    s1 = lancer(monter(tmp_path / "b"), plomberie_fausse=True)
    assert s1["options"]["plomberie_fausse_V0"] is True
    assert s1["issues_globales"]["brute"]["ligne"] == 1 and s1["issues_globales"]["apres_declencheurs"]["ligne"] == 1
    for cle in ("resultat", "classes", "sante", "verdicts_bruts_replication"):
        assert s0[cle] == s1[cle]
    # l'option n'entre pas dans le code de sortie (la ligne 1 est une issue, pas un arrêt de contrôle)
    assert s1["code_de_sortie"] == s0["code_de_sortie"] == 0
    flags = [a.dest for a in ib._parser()._subparsers._group_actions[0].choices["replication"]._actions]
    assert sorted(flags) == sorted(["help", "manifeste", "prereg", "resultats", "analyse_originale", "resultats_originaux",
                                    "analyse_A", "plomberie_fausse", "sortie"])


def test_c12_3_la_ligne_de_commande_ne_donne_aucun_moyen_de_changer_un_seuil_ou_de_forcer_une_racine():
    ap = ib._parser()
    for sous in ap._subparsers._group_actions[0].choices.values():
        for a in sous._actions:
            for opt in a.option_strings:
                assert not any(x in opt for x in ("seuil", "racine", "rho", "eps", "tolerance", "forcer", "force", "ignorer",
                                                  "sauter", "skip", "graines", "sans-"))


# --- ligne de commande, en processus ---------------------------------------------------------
def _argv(m: Monte, sortie: Path, extra=()):
    return ["replication", "--resultats", str(m.p_e1), "--manifeste", str(m.p_e2), "--prereg", str(m.p_e3),
            "--analyse-originale", str(P_ANA), "--resultats-originaux", str(P_RES), "--analyse-A", str(m.p_e5),
            "--sortie", str(sortie), *extra]


def test_c12_3_ligne_de_commande_code_0_sortie_ecrite_puis_refus_d_ecraser(b_petit, tmp_path, capsys):
    m = monter(tmp_path)
    out = tmp_path / "sortie.json"
    assert ib.main(_argv(m, out)) == 0
    contenu = out.read_bytes()
    obj = json.loads(contenu.decode("utf-8"))
    assert obj["code_de_sortie"] == 0 and obj["lecture_autorisee"] is True
    assert ib.main(_argv(m, out)) == 2                 # jamais écrasé
    assert out.read_bytes() == contenu
    assert "existe déjà" in capsys.readouterr().err


def test_c12_3_ligne_de_commande_discordance_donne_3_et_ecrit_quand_meme_la_sortie(b_petit, tmp_path):
    m = monter(tmp_path, e5_modif=_alterer("1", "R3 - R2 (V_iii_final)", "moyenne", 1e-6))
    out = tmp_path / "sortie.json"
    assert ib.main(_argv(m, out)) == 3
    obj = json.loads(out.read_text(encoding="utf-8"))
    assert obj["lecture_autorisee"] is False and obj["code_de_sortie"] == 3 and obj["motifs_arret"]


def test_c12_3_ligne_de_commande_une_garde_d_entree_donne_2_et_aucune_sortie(b_petit, tmp_path, capsys):
    m = monter(tmp_path, e5_modif=lambda e5: e5.update(run_id="autre"))
    out = tmp_path / "sortie.json"
    assert ib.main(_argv(m, out)) == 2
    assert not out.exists() and "ARRÊT" in capsys.readouterr().err


def test_c12_3_ligne_de_commande_essai_sur_la_course_originale_donne_3(tmp_path, capsys):
    out = tmp_path / "sortie.json"
    code = ib.main(["essai", "--resultats", str(P_RES), "--analyse-originale", str(P_ANA), "--resultats-originaux", str(P_RES),
                    "--analyse-A", str(P_ANA), "--sortie", str(out)])
    assert code == 3 and json.loads(out.read_text(encoding="utf-8"))["code_de_sortie"] == 3
    assert "graines non neuves" in capsys.readouterr().err


def test_c12_3_ligne_de_commande_regle_d(capsys):
    h = hashlib.sha256(b"x").hexdigest()
    assert ib.main(["regle-d", "--empreinte", h]) == 0
    sortie = json.loads(capsys.readouterr().out)
    rho, rho_t = ib.regle_d_derivation(h)
    assert sortie == {"H": h, "E_decimal": str(int(h, 16)), "rho": str(rho), "rho_t": str(rho_t), "gardes": "ok"}
    assert ib.main(["regle-d", "--empreinte", ib.VECTEURS_REGLE_D[0][0]]) == 2      # les entiers des vecteurs sont interdits
    assert "ARRÊT" in json.loads(capsys.readouterr().out)["gardes"]
    assert ib.main(["regle-d", "--empreinte", "xyz"]) == 2


def test_c12_3_modes_sans_les_pieces_obligatoires(tmp_path):
    base = dict(resultats=P_RES, analyse_originale=P_ANA, resultats_originaux=P_RES)
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(mode="replication", **base)                       # ni E3, ni E2, ni E5
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(mode="inconnu", **base)
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(mode="essai", prereg=P_ANA, **base)
    with pytest.raises(ib.Arret):
        ib.analyser_fichiers(mode="essai", resultats=P_RES, analyse_originale=None, resultats_originaux=P_RES)


def test_c12_3_en_replication_l_empreinte_de_E1_vient_du_compagnon_jamais_de_la_ligne_de_commande(b_petit, tmp_path):
    m = monter(tmp_path)
    with pytest.raises(ib.Arret, match="compagnon"):
        lancer(m, empreinte_E1="0" * 64)


# =============================================================================================
# § 12.4 — entiers de plus de 2^63 de bout en bout
# =============================================================================================
def test_c12_4_lecture_exacte_des_entiers_de_64_bits():
    o = ib.lire_json_octets(b'{"a": 18446744073709551557, "b": 9223372036854775809, "c": 1.5}', "t")
    assert o["a"] == 2 ** 64 - 59 and isinstance(o["a"], int) and o["b"] == 2 ** 63 + 1 and isinstance(o["c"], float)
    assert float(o["a"]) == float(2 ** 64 - 58)         # un passage par le binaire64 confondrait les voisins


def test_c12_4_racines_de_plus_de_2_puissance_63_de_bout_en_bout_jusqu_a_la_sortie(b_petit, tmp_path):
    m = monter(tmp_path)
    assert m.rho > 2 ** 63 and m.rho_t > 2 ** 63
    s = lancer(m)
    assert s["racine_de_reechantillonnage"] == str(m.rho) and s["racines"]["rho_t"] == str(m.rho_t)
    # le rééchantillonnage a bien utilisé l'entier exact
    st = s["resultat"]["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]
    d = np.array([t["regles"]["R3"]["V_iii_final"] - t["regles"]["R2"]["V_iii_final"]
                  for t in sorted([t for t in m.e1["resultat"]["resultats"] if t["code_delta"] == 1], key=lambda t: t["instance"])])
    ref = ib.statistique_contraste(d, m.rho, 1, 203)
    assert st["quantiles"] == ref["quantiles"]
    voisin = ib.statistique_contraste(d, m.rho + 1, 1, 203)
    assert voisin["quantiles"] != ref["quantiles"]


def test_c12_4_une_tache_dont_la_racine_n_est_pas_l_entier_exact_arrete(b_petit, tmp_path):
    def f(e1):
        e1["resultat"]["resultats"][17]["racine"] += 1          # même nombre à virgule, entier différent
    m = monter(tmp_path, e1_modif=f)
    assert float(m.rho) == float(m.rho + 1)
    with pytest.raises(ib.Arret, match="racine"):
        lancer(m)


def test_c12_4_une_racine_ecrite_en_nombre_a_virgule_arrete(b_petit, tmp_path):
    def f(e1):
        e1["resultat"]["resultats"][3]["racine_tenue"] = float(e1["resultat"]["resultats"][3]["racine_tenue"])
    with pytest.raises(ib.Arret, match="entier"):
        lancer(monter(tmp_path, e1_modif=f))
    (tmp_path / "b").mkdir()
    with pytest.raises(ib.Arret, match="entier"):
        lancer(monter(tmp_path / "b", e2_modif=lambda e2: e2["config"].update(racine=float(e2["config"]["racine"]))))


def test_c12_4_racines_de_E2_et_leurs_ecritures_decimales(b_petit, tmp_path):
    for i, (champ, delta) in enumerate((("racine", 1), ("racine_tenue", 1))):
        (tmp_path / str(i)).mkdir()
        with pytest.raises(ib.Arret, match="racine"):
            lancer(monter(tmp_path / str(i), e2_modif=lambda e2, ch=champ, dl=delta: e2["config"].update({ch: e2["config"][ch] + dl})))
    for i, champ in enumerate(("racine_chaine", "racine_tenue_chaine")):
        (tmp_path / f"c{i}").mkdir()
        with pytest.raises(ib.Arret, match="chaine|écriture"):
            lancer(monter(tmp_path / f"c{i}", e2_modif=lambda e2, ch=champ: e2["config"].update({ch: e2["config"][ch] + "0"})))
    # champs facultatifs de E2 : absents, ils ne bloquent pas
    (tmp_path / "d").mkdir()
    def sans(e2):
        del e2["config"]["racine_chaine"], e2["config"]["racine_tenue_chaine"]
    assert lancer(monter(tmp_path / "d", e2_modif=sans))["code_de_sortie"] == 0


# =============================================================================================
# § 12.5 — gardes d'entrée : cas sain puis cas artefact (arrêt, code 2, aucune sortie)
# =============================================================================================
def _ref(chemin, *cles):
    def f(obj):
        cur = obj
        for c in cles[:-1]:
            cur = cur[c]
        return cur, cles[-1]
    return f


def _touche_taches(fonction, indice=None):
    def f(e1):
        for k, t in enumerate(e1["resultat"]["resultats"]):
            if indice is None or k == indice:
                fonction(t)
    return f


def _supprimer_cle_tache(cle):
    return _touche_taches(lambda t: t.pop(cle), 5)


GARDES_E1 = [
    # (identifiant, modification de E1 (objet), motif de l'arrêt)
    ("run_id absent", lambda e1: e1.pop("run_id"), "run_id"),
    ("manifeste_sha256 absent", lambda e1: e1.pop("manifeste_sha256"), "manifeste_sha256"),
    ("run_id non texte", lambda e1: e1.update(run_id=3), "chaîne"),
    ("resultat absent", lambda e1: e1.pop("resultat"), "resultat"),
    ("temps absent", lambda e1: e1["resultat"].pop("temps"), "temps"),
    ("resultats absent", lambda e1: e1["resultat"].pop("resultats"), "resultats"),
    ("199 tâches", lambda e1: e1["resultat"]["resultats"].pop(), "200"),
    ("201 tâches", lambda e1: e1["resultat"]["resultats"].append(copy.deepcopy(e1["resultat"]["resultats"][0])), "200"),
    ("resultats pas une liste", lambda e1: e1["resultat"].update(resultats={}), "liste"),
    ("code_delta absent", _supprimer_cle_tache("code_delta"), "code_delta"),
    ("instance absente", _supprimer_cle_tache("instance"), "instance"),
    ("delta absent", _supprimer_cle_tache("delta"), "delta"),
    ("config_sha256 absent", _supprimer_cle_tache("config_sha256"), "config_sha256"),
    ("racine absente", _supprimer_cle_tache("racine"), "racine"),
    ("racine_tenue absente", _supprimer_cle_tache("racine_tenue"), "racine_tenue"),
    ("regles absent", _supprimer_cle_tache("regles"), "regles"),
    ("code_delta = 3", _touche_taches(lambda t: t.update(code_delta=3), 5), "code_delta"),
    ("code_delta booléen", _touche_taches(lambda t: t.update(code_delta=True), 5), "entier"),
    ("code_delta décimal", _touche_taches(lambda t: t.update(code_delta=1.0), 5), "entier"),
    ("instance dupliquée", _touche_taches(lambda t: t.update(instance=0), 5), "instances"),
    ("instance hors plage", _touche_taches(lambda t: t.update(instance=100), 5), "instances"),
    ("tâche déplacée de budget", _touche_taches(lambda t: t.update(code_delta=2 if t["code_delta"] == 1 else 1,
                                                                   delta=1.6 if t["code_delta"] == 1 else 1.4), 5), "tâches au lieu"),
    ("delta incohérent avec code_delta (budget 1)", _touche_taches(lambda t: t.update(delta=1.6) if t["code_delta"] == 1 else None), "delta"),
    ("delta incohérent (une tâche du budget 2)", lambda e1: next(t for t in e1["resultat"]["resultats"] if t["code_delta"] == 2).update(delta=1.4), "delta"),
    ("delta légèrement différent", _touche_taches(lambda t: t.update(delta=1.4000001), 5), "delta"),
    ("delta non numérique", _touche_taches(lambda t: t.update(delta="1.4"), 5), "nombre"),
    ("config_sha256 différent", _touche_taches(lambda t: t.update(config_sha256="0" * 64), 5), "config_sha256"),
    ("config_sha256 majuscules", _touche_taches(lambda t: t.update(config_sha256=t["config_sha256"].upper()), 5), "config_sha256"),
    ("config_sha256 non texte", _touche_taches(lambda t: t.update(config_sha256=None), 5), "chaîne"),
    ("racine d'une tâche différente", _touche_taches(lambda t: t.update(racine=t["racine"] - 1), 9), "racine"),
    ("racine_tenue d'une tâche différente", _touche_taches(lambda t: t.update(racine_tenue=t["racine_tenue"] + 1), 199), "racine"),
    ("variante en trop", _touche_taches(lambda t: t["regles"].update(R5=copy.deepcopy(t["regles"]["R2"])), 7), "variantes"),
    ("variante manquante", _touche_taches(lambda t: t["regles"].pop("R1"), 7), "variantes"),
    ("variantes dans un autre ordre", _touche_taches(lambda t: t.update(regles=dict(reversed(list(t["regles"].items())))), 7), "ordre"),
    ("champ de mesure absent", _touche_taches(lambda t: t["regles"]["R3"].pop("ii_final"), 7), "ii_final"),
    ("fpr_final absent", _touche_taches(lambda t: t["regles"]["R0"].pop("fpr_final"), 7), "fpr_final"),
    ("V_iii_standard absent", _touche_taches(lambda t: t["regles"]["R0"].pop("V_iii_standard"), 7), "V_iii_standard"),
    ("champ de mesure en texte", _touche_taches(lambda t: t["regles"]["R3"].update(ii_final="0.5"), 7), "nombre"),
    ("champ de mesure booléen", _touche_taches(lambda t: t["regles"]["R3"].update(ii_final=True), 7), "nombre"),
    ("champ de mesure nul", _touche_taches(lambda t: t["regles"]["R3"].update(ii_final=None), 7), "nombre"),
    ("mesure au-dessus de 1 + 1e-12", _touche_taches(lambda t: t["regles"]["R3"].update(ii_final=1.000000000002), 7), "hors de"),
    ("mesure en dessous de -1e-12", _touche_taches(lambda t: t["regles"]["R3"].update(exploitabilite_finale=-2e-12), 7), "hors de"),
    ("entier immense dans une mesure", _touche_taches(lambda t: t["regles"]["R3"].update(ii_final=10 ** 400), 7), "trop grand|hors de"),
    ("V_final différent du min", _touche_taches(lambda t: t["regles"]["R3"].update(V_iii_final=t["regles"]["R3"]["V_iii_final"] + 1e-6), 7), "min"),
    ("lam absent", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].pop("lam"), 7), "lam"),
    ("reference absente", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].pop("reference"), 7), "reference"),
    ("lam de R4 = 0.31", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(lam=0.31), 7), "lam"),
    ("lam de R4 = null", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(lam=None), 7), "lam"),
    ("lam de R4 texte", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(lam="0.3"), 7), "lam"),
    ("lam de R4 booléen", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(lam=True), 7), "lam"),
    ("reference de R4 = médiane", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(reference="médiane"), 7), "reference"),
    ("reference de R4 = null", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(reference=None), 7), "reference"),
    ("lam non nul pour R0", _touche_taches(lambda t: t["regles"]["R0"].update(lam=0.3), 7), "null"),
    ("reference non nulle pour R2", _touche_taches(lambda t: t["regles"]["R2"].update(reference="moyenne"), 7), "null"),
    ("lam = 0 pour R3", _touche_taches(lambda t: t["regles"]["R3"].update(lam=0), 7), "null"),
    ("poids_finaux absent", _touche_taches(lambda t: t["regles"]["R3"].pop("poids_finaux"), 7), "poids_finaux"),
    ("poids_finaux vide", _touche_taches(lambda t: t["regles"]["R3"].update(poids_finaux=[]), 7), "poids_finaux"),
    ("poids_finaux non numérique", _touche_taches(lambda t: t["regles"]["R3"].update(poids_finaux=["a"] * 9), 7), "nombre"),
    ("par_tour absent", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].pop("par_tour"), 7), "cos_consecutif"),
    ("cos_consecutif de 7 nombres", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"]["par_tour"].update(cos_consecutif=[0.1] * 7), 7), "8 nombres"),
    ("cos_consecutif de 9 nombres", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"]["par_tour"].update(cos_consecutif=[0.1] * 9), 7), "8 nombres"),
]


@pytest.mark.parametrize("ident, modif, motif", GARDES_E1, ids=[g[0] for g in GARDES_E1])
def test_c12_5_garde_E1_artefact_arrete(b_petit, tmp_path, ident, modif, motif):
    m = monter(tmp_path, e1_modif=modif)
    with pytest.raises(ib.Arret, match=motif):
        lancer(m)


GARDES_E1_SAINES = [
    ("clé supplémentaire au sommet de E1", lambda e1: e1.update(extra={"a": 1})),
    ("clé supplémentaire dans resultat", lambda e1: e1["resultat"].update(extra=[1])),
    ("clé supplémentaire dans une tâche", _touche_taches(lambda t: t.update(extra="x"))),
    ("mesure à -1e-12 exactement", _touche_taches(lambda t: t["regles"]["R3"].update(ii_final=-1e-12), 7)),
    ("mesure à 1 + 1e-12 exactement", _touche_taches(lambda t: t["regles"]["R3"].update(ii_final=1.000000000001), 7)),
    ("mesure à -5e-13", _touche_taches(lambda t: t["regles"]["R3"].update(exploitabilite_finale=-5e-13), 7)),
    ("lam de R4 écrit 0.30", _touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(lam=0.30))),
    ("tâches dans le désordre", lambda e1: e1["resultat"]["resultats"].reverse()),
    ("aucune modification", lambda e1: None),
]


@pytest.mark.parametrize("ident, modif", GARDES_E1_SAINES, ids=[g[0] for g in GARDES_E1_SAINES])
def test_c12_5_garde_E1_cas_sain_passe(b_petit, tmp_path, ident, modif):
    s = lancer(monter(tmp_path, e1_modif=modif))
    assert s["code_de_sortie"] in (0, 3) and "resultat" in s


def test_c12_5_une_tache_hors_des_200_est_traitee_comme_artefact_avec_delta_et_config(b_petit, tmp_path):
    """Les trois nouvelles gardes de E1 (point 13) : delta, config_sha256, lam/reference, chacune sain puis artefact."""
    sain = lancer(monter(tmp_path))
    assert sain["code_de_sortie"] == 0
    for i, (modif, motif) in enumerate((
            (_touche_taches(lambda t: t.update(delta=t["delta"] + 0.2)), "delta"),
            (_touche_taches(lambda t: t.update(config_sha256="a" * 64)), "config_sha256"),
            (_touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"].update(lam=0.2)), "lam"))):
        (tmp_path / str(i)).mkdir()
        with pytest.raises(ib.Arret, match=motif):
            lancer(monter(tmp_path / str(i), e1_modif=modif))


def _json_avec(remplacements):
    def f(octets):
        t = octets.decode("utf-8")
        for a, b in remplacements:
            assert a in t
            t = t.replace(a, b, 1)
        return t.encode("utf-8")
    return f


@pytest.mark.parametrize("octets, motif", [
    (_json_avec([('"run_id": "synthetique"', '"run_id": "a", "run_id": "synthetique"')]), "dupliquée"),
    (_json_avec([('"instance": 0,', '"instance": NaN,')]), "non finie"),
    (_json_avec([('"instance": 0,', '"instance": Infinity,')]), "non finie"),
    (_json_avec([('"instance": 0,', '"instance": -Infinity,')]), "non finie"),
    (lambda o: o + b"}", "illisible"),
    (lambda o: b"\xff\xfe" + o, "illisible"),
    (lambda o: b"", "illisible"),
    (lambda o: b"[]", "objet"),
], ids=["clé dupliquée", "NaN", "Infinity", "-Infinity", "JSON tronqué ou en trop", "octets non UTF-8", "fichier vide", "tableau"])
def test_c12_5_json_illisible_ou_ambigu_arrete(b_petit, tmp_path, octets, motif):
    with pytest.raises(ib.Arret, match=motif):
        lancer(monter(tmp_path, e1_octets=octets))


def test_c12_5_json_avec_espaces_et_retours_a_la_ligne_est_accepte(b_petit, tmp_path):
    s = lancer(monter(tmp_path, e1_octets=lambda o: b"\n  " + o.replace(b", ", b",\n  ") + b"\n\n"))
    assert s["code_de_sortie"] == 0


# --- compagnons ------------------------------------------------------------------------------
def _poser_compagnon(chemin: Path, texte):
    comp = Path(str(chemin) + ".sha256")
    if texte is None:
        comp.unlink()
    else:
        comp.write_bytes(texte if isinstance(texte, bytes) else texte.encode("utf-8"))


def _bon(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


@pytest.mark.parametrize("piece", ["p_e1", "p_e2", "p_e3", "p_e5"])
@pytest.mark.parametrize("variante, fabrique, motif", [
    ("absent", lambda c: None, "aucun fichier compagnon"),
    ("empreinte fausse", lambda c: f"{'0' * 64}  {c.name}\n", "empreinte"),
    ("nom de base faux", lambda c: f"{_bon(c)}  autre.json\n", "nomme"),
    ("un seul espace", lambda c: f"{_bon(c)} {c.name}\n", "format"),
    ("trois espaces", lambda c: f"{_bon(c)}   {c.name}\n", "format|nomme"),
    ("majuscules", lambda c: f"{_bon(c).upper()}  {c.name}\n", "format"),
    ("sans fin de ligne", lambda c: f"{_bon(c)}  {c.name}", "format"),
    ("fin de ligne Windows", lambda c: f"{_bon(c)}  {c.name}\r\n", "format"),
    ("deux lignes", lambda c: f"{_bon(c)}  {c.name}\n{_bon(c)}  {c.name}\n", "format"),
    ("chemin au lieu du nom de base", lambda c: f"{_bon(c)}  ./{c.name}\n", "format|nomme"),
    ("empreinte tronquée", lambda c: f"{_bon(c)[:63]}  {c.name}\n", "format"),
    ("compagnon vide", lambda c: "", "format"),
    ("marqueur binaire de sha256sum", lambda c: f"{_bon(c)} *{c.name}\n", "format"),
], ids=lambda x: x if isinstance(x, str) else "")
def test_c12_5_compagnon_artefact_arrete(b_petit, tmp_path, piece, variante, fabrique, motif):
    m = monter(tmp_path)
    chemin = getattr(m, piece)
    _poser_compagnon(chemin, fabrique(chemin))
    with pytest.raises(ib.Arret, match=motif):
        lancer(m)


def test_c12_5_compagnon_sain_exact_est_accepte_et_la_variante_sans_extension_ne_l_est_pas(b_petit, tmp_path):
    m = monter(tmp_path)
    assert lancer(m)["code_de_sortie"] == 0
    # le compagnon « <fichier sans extension>.sha256 » toléré en v1 ne l'est plus
    comp = Path(str(m.p_e1) + ".sha256")
    autre = tmp_path / "resultats.sha256"
    autre.write_bytes(comp.read_bytes())
    comp.unlink()
    with pytest.raises(ib.Arret, match="aucun fichier compagnon"):
        lancer(m)


def test_c12_5_fichier_modifie_apres_scellement_arrete(b_petit, tmp_path):
    m = monter(tmp_path)
    m.p_e1.write_bytes(m.p_e1.read_bytes() + b" ")
    with pytest.raises(ib.Arret, match="empreinte"):
        lancer(m)


def test_c12_5_fichier_absent_arrete(b_petit, tmp_path):
    m = monter(tmp_path)
    m.p_e2.unlink()
    with pytest.raises(ib.Arret):
        lancer(m)


@pytest.mark.parametrize("quoi", ["analyse", "resultats"])
def test_c12_5_E4_hors_empreinte_epinglee_arrete_meme_avec_compagnon(b_petit, tmp_path, quoi):
    m = monter(tmp_path)
    src = P_ANA if quoi == "analyse" else P_RES
    copie = tmp_path / ("E4-" + src.name)
    octets = src.read_bytes()
    ecrire_avec_compagnon(copie, octets[:-1] + (b" " if octets[-1:] != b" " else b"\n"))
    kw = dict(analyse_originale=copie if quoi == "analyse" else P_ANA, resultats_originaux=copie if quoi == "resultats" else P_RES)
    with pytest.raises(ib.Arret, match="empreinte"):
        ib.analyser_fichiers(mode="replication", resultats=m.p_e1, prereg=m.p_e3, manifeste=m.p_e2, analyse_A=m.p_e5, **kw)


def test_c12_5_E4_sain_sans_compagnon_est_accepte_car_epingle(b_petit, tmp_path):
    assert lancer(monter(tmp_path))["code_de_sortie"] == 0


# --- E2 (point 5) : liste fermée ---------------------------------------------------------------
def _e2_champ(chemin, valeur):
    def f(e2):
        cur = e2
        for c in chemin[:-1]:
            cur = cur[c]
        cur[chemin[-1]] = valeur
    return f


def _e2_sans(chemin):
    def f(e2):
        cur = e2
        for c in chemin[:-1]:
            cur = cur[c]
        del cur[chemin[-1]]
    return f


GARDES_E2 = [
    ("run_id différent de E1", _e2_champ(["run_id"], "autre"), "run_id"),
    ("run_id absent", _e2_sans(["run_id"]), "run_id"),
    ("racine différente", lambda e2: e2["config"].update(racine=e2["config"]["racine"] + 1), "racine"),
    ("racine_tenue différente", lambda e2: e2["config"].update(racine_tenue=e2["config"]["racine_tenue"] - 1), "racine"),
    ("racine absente", _e2_sans(["config", "racine"]), "racine"),
    ("racine texte", lambda e2: e2["config"].update(racine=str(e2["config"]["racine"])), "entier"),
    ("racine_chaine fausse", _e2_champ(["config", "racine_chaine"], "123"), "chaine|écriture"),
    ("racine_tenue_chaine fausse", _e2_champ(["config", "racine_tenue_chaine"], "123"), "chaine|écriture"),
    ("prereg_sha256 faux", _e2_champ(["config", "prereg_sha256"], "0" * 64), "H recalculé"),
    ("preenregistrement.sha256 faux", _e2_champ(["preenregistrement", "sha256"], "0" * 64), "H recalculé"),
    ("preenregistrement absent", _e2_sans(["preenregistrement"]), "preenregistrement"),
    ("prereg_sha256 absent", _e2_sans(["config", "prereg_sha256"]), "prereg_sha256"),
    ("lambda = 0.2", _e2_champ(["config", "lambda"], 0.2), "lambda"),
    ("lambda texte", _e2_champ(["config", "lambda"], "0.3"), "lambda"),
    ("lambda absent", _e2_sans(["config", "lambda"]), "lambda"),
    ("reference = médiane", _e2_champ(["config", "reference"], "médiane"), "reference"),
    ("reference absente", _e2_sans(["config", "reference"]), "reference"),
    ("n_instances = 99", _e2_champ(["config", "config", "n_instances"], 99), "n_instances"),
    ("n_instances décimal", _e2_champ(["config", "config", "n_instances"], 100.0), "n_instances"),
    ("n_instances absent", _e2_sans(["config", "config", "n_instances"]), "n_instances"),
    ("config_sha256 faux", _e2_champ(["config", "config_sha256"], "1" * 64), "config_sha256"),
    ("config_sha256 absent", _e2_sans(["config", "config_sha256"]), "config_sha256"),
    ("config absent", _e2_sans(["config"]), "config"),
]


@pytest.mark.parametrize("ident, modif, motif", GARDES_E2, ids=[g[0] for g in GARDES_E2])
def test_c12_5_garde_E2_artefact_arrete(b_petit, tmp_path, ident, modif, motif):
    with pytest.raises(ib.Arret, match=motif):
        lancer(monter(tmp_path, e2_modif=modif))


def test_c12_5_garde_E2_manifeste_sha256_de_E1_different_de_l_empreinte_de_E2(b_petit, tmp_path):
    def f(e1):
        e1["manifeste_sha256"] = "0" * 64
    with pytest.raises(ib.Arret, match="manifeste_sha256"):
        lancer(monter(tmp_path, e1_modif=f))


def test_c12_5_garde_E2_preenregistrement_E3_different_de_celui_du_manifeste(b_petit, tmp_path):
    m = monter(tmp_path)
    ecrire_avec_compagnon(m.p_e3, m.p_e3.read_bytes() + b"modifie\n")       # un autre texte scellé : un autre H
    with pytest.raises(ib.Arret):
        lancer(m)


def test_c12_5_garde_E2_cas_sain_complet_et_champs_supplementaires_permis(b_petit, tmp_path):
    s = lancer(monter(tmp_path, e2_modif=lambda e2: e2.update(extra={"a": 1}, config={**e2["config"], "extra": 2})))
    assert s["code_de_sortie"] == 0 and s["manifeste_E2"]["lambda"] == 0.3 and s["manifeste_E2"]["n_instances"] == 100


def test_c12_5_regle_D_artefact_racine_interdite_arrete_a_la_derivation(b_petit, tmp_path, monkeypatch):
    """Un texte scellé dont la dérivation tombe dans l'ensemble interdit F : arrêt (les entiers sont ceux des vecteurs)."""
    h = ib.VECTEURS_REGLE_D[0][0]
    monkeypatch.setattr(hashlib, "sha256", lambda o=b"": type("H", (), {"hexdigest": lambda self: h})())
    with pytest.raises(ib.Arret, match="interdit|vecteurs"):
        ib.regle_d_depuis_octets(b"n'importe quoi")


# --- E5 -------------------------------------------------------------------------------------
@pytest.mark.parametrize("ident, modif, motif", [
    ("run_id différent", lambda e5: e5.update(run_id="autre"), "run_id"),
    ("manifeste_sha256 différent", lambda e5: e5.update(manifeste_sha256="0" * 64), "manifeste_sha256"),
    ("run_id absent", lambda e5: e5.pop("run_id"), "run_id"),
    ("manifeste_sha256 absent", lambda e5: e5.pop("manifeste_sha256"), "manifeste_sha256"),
    ("contraste absent", lambda e5: e5["resultat"]["1"]["contrastes_contre_R2"].pop("R0 - R2 (ii_final)"), "absent"),
    ("budget absent", lambda e5: e5["resultat"].pop("2"), "absents"),
    ("quantile absent", lambda e5: e5["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"]["quantiles"].pop("q0.05"), "quantiles"),
    ("moyenne absente", lambda e5: e5["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"].pop("moyenne"), "moyenne"),
    ("n absent", lambda e5: e5["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"].pop("n"), "`n`"),
    ("zeros_exacts absent", lambda e5: e5["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"].pop("zeros_exacts"), "zeros_exacts"),
    ("moyenne en texte", lambda e5: e5["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"].update(moyenne="0.1"), "nombre"),
    ("resultat absent", lambda e5: e5.pop("resultat"), "absents"),
], ids=lambda x: x if isinstance(x, str) else "")
def test_c12_5_garde_E5_artefact_arrete(b_petit, tmp_path, ident, modif, motif):
    with pytest.raises(ib.Arret, match=motif):
        lancer(monter(tmp_path, e5_modif=modif))


def test_c12_5_E5_absente_en_replication_est_un_arret_et_son_compagnon_est_exige(b_petit, tmp_path):
    m = monter(tmp_path)
    with pytest.raises(ib.Arret, match="obligatoires"):
        ib.analyser_fichiers(mode="replication", resultats=m.p_e1, analyse_originale=P_ANA, resultats_originaux=P_RES,
                             prereg=m.p_e3, manifeste=m.p_e2, analyse_A=None)
    Path(str(m.p_e5) + ".sha256").unlink()
    with pytest.raises(ib.Arret, match="compagnon"):
        lancer(m)


def test_c12_5_E5_cas_sain_avec_champs_supplementaires(b_petit, tmp_path):
    s = lancer(monter(tmp_path, e5_modif=lambda e5: (e5.update(extra=1),
                                                    e5["resultat"]["1"]["contrastes_contre_R2"]["R0 - R2 (ii_final)"].update(extra=2))))
    assert s["comparaison_A_B"]["concordance"] is True


# --- sortie : jamais écrasée, jamais écrite après un arrêt d'entrée ------------------------
def test_c12_5_aucune_sortie_n_est_ecrite_apres_un_arret_d_entree_et_rien_n_est_ecrase(b_petit, tmp_path):
    m = monter(tmp_path, e1_modif=_touche_taches(lambda t: t.update(delta=9.0), 3))
    out = tmp_path / "s.json"
    assert ib.main(_argv(m, out)) == 2
    assert not out.exists()
    avant = sorted(p.name for p in tmp_path.iterdir())
    assert ib.main(_argv(m, out)) == 2
    assert sorted(p.name for p in tmp_path.iterdir()) == avant
    out.write_text("déjà là", encoding="utf-8")
    assert ib.main(_argv(monter(tmp_path / "x" if (tmp_path / "x").mkdir() is None else tmp_path), out)) == 2
    assert out.read_text(encoding="utf-8") == "déjà là"


def test_c12_5_ecrire_json_neuf_refuse_d_ecraser_et_refuse_nan(tmp_path):
    p = tmp_path / "a.json"
    sha = ib.ecrire_json_neuf(p, {"x": 1})
    assert sha == hashlib.sha256(p.read_bytes()).hexdigest()
    with pytest.raises(FileExistsError):
        ib.ecrire_json_neuf(p, {"x": 2})
    with pytest.raises(ValueError):
        ib.ecrire_json_neuf(tmp_path / "b.json", {"x": float("nan")})


def test_c12_5_la_sortie_de_B_est_un_json_strict_sans_nan(b_petit, tmp_path):
    s = lancer(monter(tmp_path))
    texte = json.dumps(s, allow_nan=False)
    assert "NaN" not in texte and "Infinity" not in texte


# =============================================================================================
# Essais rattachés aux mutations (campagne de mutations de B v2) et aux exigences neuves
# =============================================================================================
def test_mut_zeros_exacts_est_une_egalite_exacte_a_zero():
    d = np.array([0.0, 5e-13, -5e-13, 1e-300] * 25)
    st = ib.statistique_contraste(d, 20266201, 1, 203)
    assert st["zeros_exacts"] == 25 and st["n"] == 100
    d = np.array([-0.0, 0.0] * 50)
    assert ib.statistique_contraste(d, 20266201, 1, 203)["zeros_exacts"] == 100        # −0.0 == 0 pour ce compte


def _ecarts_deux_contrastes(g_premier, g_dernier):
    """Quatre contrastes primaires : le premier (R3, V, c=1) et le dernier (R0, V, c=2) ont les écarts donnés ; les deux
    autres un écart de 0,05 (ni petit ni à la frontière)."""
    c = _faux_contrastes(0.10 + 0.05, 0.06)
    c["1"][ib.libelle_contraste("R3", "V")]["moyenne"] = 0.10 + g_premier
    c["2"][ib.libelle_contraste("R0", "V")]["moyenne"] = 0.10 + g_dernier
    return ib.ecart_replication(c, _fausse_analyse(0.10, 0.08))


def test_mut_TR1_sans_court_circuit_une_marque_tardive_est_vue_meme_apres_un_declenchement():
    seuil = ib.Z_ETOILE * 0.01
    e = _ecarts_deux_contrastes(0.5, seuil + 5e-10)          # le premier contraste déclenche déjà
    assert list(e)[0] == "(R3, V, c=1)" and list(e)[-1] == "(R0, V, c=2)"
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    assert d["TR1"]["declenche"] is True and d["TR1"]["frontiere"] is True
    assert any("c=2" in p["quantite"] for p in d["TR1"]["comparaisons_a_la_frontiere"])


def test_mut_TR2_sans_court_circuit_une_marque_tardive_est_vue_meme_apres_un_contraste_non_petit():
    e = _ecarts_deux_contrastes(0.5, 0.001 - 5e-10)           # le premier contraste n'est pas « petit »
    d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    assert d["TR2"]["declenche"] is False and d["TR2"]["frontiere"] is True


def test_mut_TR3_un_seul_budget_suffit_et_chaque_budget_compte():
    e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
    assert ib.declencheurs_audit(e, _cl_r0("≈", "R0 > R2"), _vb())["TR3"]["declenche"] is True
    assert ib.declencheurs_audit(e, _cl_r0("R0 ≳ R2", "≈"), _vb())["TR3"]["declenche"] is True


def test_mut_TR4_chacun_des_deux_verdicts_suffit():
    e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
    assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb(v1="non répliquée (signe inversé)"))["TR4"]["declenche"] is True
    assert ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb(v0="non répliquée (le réentraînement l'emporte d'un effet d'intérêt)"))["TR4"]["declenche"] is True


@pytest.mark.parametrize("qui", ["TR1", "TR2", "TR3", "TR4"])
def test_mut_au_moins_un_compte_chacun_des_quatre_declencheurs(qui):
    if qui == "TR1":
        e = ib.ecart_replication(_faux_contrastes(0.30, 0.06), _fausse_analyse(0.10, 0.08))
        d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    elif qui == "TR2":
        e = ib.ecart_replication(_faux_contrastes(0.10, 0.06), _fausse_analyse(0.10, 0.08))
        d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb())
    elif qui == "TR3":
        e = ib.ecart_replication(_faux_contrastes(0.12, 0.06), _fausse_analyse(0.10, 0.08))
        d = ib.declencheurs_audit(e, _cl_r0("R0 > R2", "≈"), _vb())
    else:
        e = ib.ecart_replication(_faux_contrastes(0.12, 0.06), _fausse_analyse(0.10, 0.08))
        d = ib.declencheurs_audit(e, _cl_r0("≈", "≈"), _vb(v1="non répliquée (signe inversé)"))
    declenches = [k for k in ("TR1", "TR2", "TR3", "TR4") if d[k]["declenche"]]
    assert declenches == [qui], declenches
    assert d["au_moins_un"]["declenche"] is True


def test_mut_les_verdicts_apres_declencheurs_suivent_au_moins_un_et_pas_seulement_TR1():
    vb = {k: {"verdict": "répliquée", "ligne": 4, "frontiere": False} for k in ib.CLES_VERDICTS_REPLICATION}
    for qui in ("TR1", "TR2", "TR3", "TR4"):
        decl = {k: {"declenche": k == qui, "frontiere": False} for k in ("TR1", "TR2", "TR3", "TR4")}
        decl["au_moins_un"] = {"declenche": True, "frontiere": False}
        apres = ib.verdicts_apres_declencheurs(vb, decl)
        assert set(apres) == {"HR1", "HR0", "HR3", "lois_tenues_ii"}
        assert all(v["verdict"] == "non jugeable (audit en attente)" for v in apres.values())


def test_mut_un_controle_declenche_dans_un_seul_budget_declenche_l_etat_global_et_la_marque_globale():
    sante = {"1": {t: {"declenche": t == "T5", "frontiere": t == "T6"} for t in ("T2", "T3", "T4", "T5", "T6")},
             "2": {t: {"declenche": False, "frontiere": False} for t in ("T2", "T3", "T4", "T5", "T6")}}
    etat, front = ib.etats_globaux_sante(sante)
    assert etat == {"T2": False, "T3": False, "T4": False, "T5": True, "T6": False}
    assert front == {"T2": False, "T3": False, "T4": False, "T5": False, "T6": True}
    sante["1"], sante["2"] = sante["2"], sante["1"]
    assert ib.etats_globaux_sante(sante) == (etat, front)


def test_mut_issue_ligne_1_ne_depend_que_de_l_arret_et_de_l_option():
    assert ib.issue_globale("répliquée", "répliquée")["ligne"] == 5
    assert ib.issue_globale("répliquée", "répliquée", arret_controle=True)["ligne"] == 1
    assert ib.issue_globale("répliquée", "répliquée", plomberie_fausse=True)["ligne"] == 1
    assert ib.issue_globale("non répliquée (signe inversé)", "répliquée")["ligne"] == 4
    assert ib.issue_globale("non répliquée (effet démontré inférieur à 0,05)", "répliquée")["ligne"] == 4
    assert ib.issue_globale("non jugeable (imprécis)", "répliquée")["ligne"] == 8


def test_mut_graines_neuves_chaque_budget_compte():
    base = _base_valeurs()
    d = {k: v.copy() for k, v in base.items()}
    for k in d:
        if k[0] == 2:
            d[k] = d[k] + 1e-3                     # le budget 2 diffère, le budget 1 est identique
    cpt = ib.comptes_graines_neuves(_donnees_champs(base), _donnees_champs(d))
    assert [n for par in cpt.values() for n in par.values()] == [100] * 15
    d = {k: (v + 1e-3 if k[0] == 1 else v.copy()) for k, v in base.items()}
    cpt = ib.comptes_graines_neuves(_donnees_champs(base), _donnees_champs(d))
    assert [n for par in cpt.values() for n in par.values()] == [100] * 15


def test_mut_graines_neuves_chaque_mesure_arrete_a_elle_seule():
    base = _base_valeurs()
    for champ in ("V_iii_final", "exploitabilite_moyenne_tours", "ii_final"):
        d = {k: v.copy() for k, v in base.items()}
        d[(1, "R2", champ)] = base[(1, "R2", champ)].copy()            # identique pour R2 : 100 tâches égales
        cpt = ib.comptes_graines_neuves(_donnees_champs(base), _donnees_champs({
            k: (v if (k[1] == "R2" and k[2] == champ and k[0] == 1) else v + 1e-3) for k, v in base.items()}))
        assert cpt["R2"][champ] == 100 and sum(1 for par in cpt.values() for n in par.values() if n) == 1
        assert ib.resume_graines_neuves(cpt)["arret_graines_non_neuves"] is True


def test_mut_sortie_unique_sans_ecrasement_en_creation_exclusive(tmp_path):
    p = tmp_path / "s.json"
    p.write_text("avant", encoding="utf-8")
    with pytest.raises(FileExistsError):
        ib.ecrire_json_neuf(p, {"a": 1})
    assert p.read_text(encoding="utf-8") == "avant"


def test_mut_le_code_de_sortie_et_la_lecture_autorisee_suivent_les_motifs():
    base = {"comptes_graines_neuves": {"arret_graines_non_neuves": False, "comptes_au_dessus_du_seuil": []},
            "comparaison_A_B": {"evaluee": True, "discordance_a_arret": False, "motifs": []},
            "verdicts_bruts_replication": {"HR1": {"verdict": "répliquée", "frontiere": False},
                                           "HR0": {"verdict": "répliquée", "frontiere": False}},
            "verdicts_apres_declencheurs": {"HR1": {"verdict": "répliquée", "frontiere": False},
                                            "HR0": {"verdict": "répliquée", "frontiere": False}}}
    s = ib.conclure(copy.deepcopy(base))
    assert (s["code_de_sortie"], s["lecture_autorisee"], s["motifs_arret"]) == (0, True, [])
    b = copy.deepcopy(base)
    b["comptes_graines_neuves"] = {"arret_graines_non_neuves": True, "comptes_au_dessus_du_seuil":
                                   [{"variante": "R1", "mesure": "ii_final", "compte": 3}]}
    s = ib.conclure(b)
    assert (s["code_de_sortie"], s["lecture_autorisee"]) == (3, False) and "graines non neuves" in s["motifs_arret"][0]
    assert s["issues_globales"]["brute"]["ligne"] == 1 and s["issues_globales"]["apres_declencheurs"]["ligne"] == 1
    b = copy.deepcopy(base)
    b["comparaison_A_B"] = {"evaluee": True, "discordance_a_arret": True, "motifs": ["x"]}
    s = ib.conclure(b)
    assert (s["code_de_sortie"], s["lecture_autorisee"]) == (3, False) and "discordance A/B" in s["motifs_arret"][0]
    b = copy.deepcopy(base)
    b["comparaison_A_B"] = {"evaluee": False}
    assert ib.conclure(b)["code_de_sortie"] == 0


def test_c12_1_validation_complete_sur_la_course_originale_sans_la_suite_d_essais(tmp_path):
    """La commande « valider-originale » (sans relancer pytest) : tous les points du § 12.1, § 12.3 et les rapports."""
    dossier_sortie = tmp_path / "sortie"
    dossier_sortie.mkdir()
    rapport = ib.valider_originale(DOSSIER, dossier_sortie, executer_essais=False, mutations="n/a")
    cond = rapport["conclusion"]
    assert cond["validation_reussie"] is True, {k: v for k, v in cond.items() if not v}
    assert rapport["comparaison_A_B"]["ecart_maximal_absolu"] <= 1e-9
    assert rapport["cas_12_3_b_a_e"]["ok"] and rapport["cas_a_original_contre_lui_meme"]["ok"]
    assert (dossier_sortie / ib.NOM_SORTIE_B).is_file()
    md = ib.rapport_markdown(rapport)
    assert md.splitlines()[0].startswith("# ") and "**Verdict : validation RÉUSSIE.**" in md.splitlines()[2]
    for chaine in ("Table de correspondance", "Commande exacte", "Ambiguïtés restantes", "Fichiers ouverts", "claude-sonnet-5-5"):
        assert chaine in md
    json.dumps(rapport, allow_nan=False)
    pts = {str(p["point"]) for p in rapport["points_de_la_specification_0"]}
    assert {str(i) for i in range(1, 16)} <= pts and "CL-10" in pts
    assert len(rapport["table_de_correspondance_des_cles"]) >= 15


def test_c12_1_la_validation_refuse_d_ecraser_ses_sorties(tmp_path):
    (tmp_path / ib.NOM_VALIDATION_MD).write_text("déjà là", encoding="utf-8")
    code = ib.main(["valider-originale", "--dossier", str(DOSSIER), "--dossier-sortie", str(tmp_path)])
    assert code == 2 and (tmp_path / ib.NOM_VALIDATION_MD).read_text(encoding="utf-8") == "déjà là"
    assert not (tmp_path / ib.NOM_SORTIE_B).exists()


def test_mut_T2_est_R3_V_est_unilateral_un_effet_negatif_de_R3_ne_declenche_pas_cette_condition(b_petit):
    e1 = fabriquer_e1(90)
    _imposer(e1, "R3", "V_iii_final", [-0.4] * 100, base_r2=0.6)
    r = calc(e1)
    t2 = r["sante"]["1"]["T2"]
    assert t2["est_R3_V"] < -0.39 and t2["est_R3_V_gt_0_30"] is False
    assert t2["declenche"] is False and r["sante"]["etat_global"]["T2"] is False
    e1 = fabriquer_e1(90)
    _imposer(e1, "R3", "V_iii_final", [0.4] * 100, base_r2=0.1)
    assert calc(e1)["sante"]["1"]["T2"]["est_R3_V_gt_0_30"] is True


def _imposer_par_budget(e1, nom, champ, diffs_par_budget, base_r2=0.5):
    for t in taches_de(e1):
        r2 = t["regles"]["R2"]
        fixer_V(r2, base_r2) if champ == "V_iii_final" else r2.__setitem__(champ, base_r2)
        x = base_r2 + diffs_par_budget[t["code_delta"]][t["instance"]]
        if champ == "V_iii_final":
            fixer_V(t["regles"][nom], x)
        else:
            t["regles"][nom][champ] = x


def test_mut_les_lignes_de_la_table_C_sont_lues_budget_par_budget(b_petit):
    for (m1, m2), (l1, l2) in (((0.05, -0.1), (4, 1)), ((-0.1, 0.05), (1, 4))):
        e1 = fabriquer_e1(91)
        _imposer_par_budget(e1, "R0", "ii_final", {1: _diffs(m1, 0.0), 2: _diffs(m2, 0.0)})
        s = calc(e1)
        assert s["verdicts_bruts_replication"]["lignes_C_R0_ii"] == {"1": l1, "2": l2}
        assert s["verdicts_bruts_replication"]["lois_tenues_ii"]["verdict"] == "non répliquée (signe inversé)"
        assert s["verdicts_bruts_replication"]["lois_tenues_ii"]["ligne"] == 3


def test_mut_HR3_lit_les_classes_de_R4_et_HR0_celles_de_R0(b_petit):
    e1 = fabriquer_e1(92)
    _imposer(e1, "R0", "V_iii_final", _diffs(-0.05, 0.0), base_r2=0.5)        # R2 > R0 aux deux budgets
    _imposer(e1, R4, "V_iii_final", _diffs(0.05, 0.0), base_r2=0.5)           # R4 > R2 aux deux budgets
    s = calc(e1)
    vb = s["verdicts_bruts_replication"]
    assert vb["kappa_R0_V"] == {"1": "R2 > R0", "2": "R2 > R0"} and vb["kappa_prime_R4_V"] == {"1": "R4 > R2", "2": "R4 > R2"}
    assert vb["HR0"]["ligne"] == 2 and vb["HR3"]["verdict"] == "répliquée"
    assert s["verdicts_regles_originales"]["HR0"]["verdict"] == "confirmée"
    assert s["verdicts_regles_originales"]["HR3"]["verdict"] == "confirmée"
    e1 = fabriquer_e1(92)
    _imposer(e1, "R0", "V_iii_final", _diffs(0.05, 0.0), base_r2=0.5)
    _imposer(e1, R4, "V_iii_final", _diffs(-0.05, 0.0), base_r2=0.5)
    vb = calc(e1)["verdicts_bruts_replication"]
    assert vb["HR0"]["verdict"] == "répliquée" and vb["HR3"]["verdict"] == "non répliquée" and vb["HR3"]["ligne"] == 3


def test_mut_les_resultats_originaux_passent_par_les_memes_gardes_de_racine_que_E1(b_petit):
    ana, res = pieces()
    e1 = fabriquer_e1(93)
    mauvais = copy.deepcopy(res)
    mauvais["resultat"]["resultats"][11]["racine"] += 1
    with pytest.raises(ib.Arret, match="racine"):
        ib.calculer_B(e1, RHO, RHO_T, ana, mauvais)
    mauvais = copy.deepcopy(res)
    mauvais["resultat"]["resultats"][11]["delta"] = 9.0
    with pytest.raises(ib.Arret, match="delta"):
        ib.calculer_B(e1, RHO, RHO_T, ana, mauvais)


@pytest.mark.parametrize("modif, motif", [
    (_touche_taches(lambda t: t["regles"]["R0"].update(fpr_final=ast.literal_eval("1e999")), 4), "non finie|hors de"),
    (_touche_taches(lambda t: t["regles"]["R1"].update(V_iii_standard=ast.literal_eval("1e999")), 4), "non finie|min"),
    (_touche_taches(lambda t: t.update(delta=ast.literal_eval("1e999")), 4), "non finie|delta"),
    (_touche_taches(lambda t: t["regles"]["R3"].update(poids_finaux=[ast.literal_eval("1e999")] * 9), 4), "non finie"),
    (_touche_taches(lambda t: t["regles"]["R4[moyenne,λ=0.3]"]["par_tour"].update(cos_consecutif=[ast.literal_eval("1e999")] * 8), 4), "non finie"),
], ids=["fpr infini", "V standard infini", "delta infini", "poids infini", "cosinus infini"])
def test_c12_5_une_valeur_non_finie_ecrite_1e999_est_un_arret(b_petit, tmp_path, modif, motif):
    m = monter(tmp_path, e1_modif=modif, e1_octets=lambda o: o.replace(b"Infinity", b"1e999"))
    assert b"1e999" in m.p_e1.read_bytes()
    with pytest.raises(ib.Arret, match=motif):
        lancer(m)


def test_mut_une_sortie_existante_est_refusee_avant_tout_calcul(tmp_path, monkeypatch, capsys):
    """Le refus d'écraser est un arrêt d'entrée : il précède la lecture des fichiers et le calcul."""
    out = tmp_path / "s.json"
    out.write_text("déjà là", encoding="utf-8")
    def interdit(**kw):
        raise AssertionError("l'analyse ne devait pas être lancée")
    monkeypatch.setattr(ib, "analyser_fichiers", interdit)
    code = ib.main(["essai", "--resultats", str(P_RES), "--analyse-originale", str(P_ANA), "--resultats-originaux", str(P_RES),
                    "--sortie", str(out)])
    assert code == 2 and out.read_text(encoding="utf-8") == "déjà là" and "existe déjà" in capsys.readouterr().err
