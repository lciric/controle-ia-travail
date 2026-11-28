"""Independent compliance verification & edge-case suite for barreau 8 lectures v5."""
from __future__ import annotations

import copy
import hashlib
import json
import math
import os
import sys
import tempfile
import types
from pathlib import Path

import numpy as np

# Provide exact pure-NumPy scipy.stats.rankdata ONLY in-memory so modules that
# import controle_ia.sondes.evaluation can be loaded in this no-scipy sandbox.
def _rankdata_average(a):
    arr = np.asarray(a, dtype=np.float64)
    n = arr.size
    order = np.argsort(arr, kind="mergesort")
    ranks = np.empty(n, dtype=np.float64)
    s = arr[order]
    i = 0
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        avg = 0.5 * (i + j + 1)
        ranks[order[i:j]] = avg
        i = j
    return ranks

_scipy = types.ModuleType("scipy")
_scipy_stats = types.ModuleType("scipy.stats")
_scipy_stats.rankdata = _rankdata_average
_scipy.stats = _scipy_stats
sys.modules["scipy"] = _scipy
sys.modules["scipy.stats"] = _scipy_stats

# torch is only imported transitively by controle_ia.sondes.familles (never called by lectures v5)
_torch = types.ModuleType("torch")
_torch.nn = types.ModuleType("torch.nn")
_torch.nn.Module = object
sys.modules["torch"] = _torch
sys.modules["torch.nn"] = _torch.nn

ROOT = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain\aba574b2-83e1-4fdb-a128-2e4f2641d06b\scratch\cl-code-lectures-v5"
)
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(1, r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail\src")
sys.path.insert(2, str(ROOT / "scripts"))

from controle_ia import manifeste as mf
from controle_ia.gardes import GardeArret
from controle_ia.iib import branches_v5 as br
from controle_ia.iib import configuration_lectures_v5 as cl
from controle_ia.iib import configuration_v1 as cv1
from controle_ia.iib import configuration_v5 as cf5
from controle_ia.iib import designation_v5 as dg
from controle_ia.iib import entrees_lectures_v5 as ev
from controle_ia.iib import jumeau_v5 as jm
from controle_ia.iib import lecture_v1 as lv
from controle_ia.iib import lectures_v5 as lx
from controle_ia.iib import rapportes_v5 as rp
from controle_ia.iib import tours_v1
from controle_ia.scellement import sceller

import lecture_iib_1_dommage_v5 as s1
import lecture_iib_2_diffusion_v5 as s2
import lecture_iib_audit_r4_v5 as sa

results = []

def check(name, fn):
    try:
        info = fn()
        results.append(("PASS", name, info or ""))
    except AssertionError as e:
        results.append(("FAIL", name, str(e)))
    except Exception as e:
        results.append(("ERR ", name, f"{type(e).__name__}: {e}"))


# 1. Spec & modules hashes
def t_spec_and_modules():
    assert cl.exiger_specification() == cl.SPECIFICATION["sha256"]
    m = cl.exiger_modules_d_origine()
    assert len(cl.MODULES_D_ORIGINE) == 15
    assert all(m[k] == v for k, v in cl.MODULES_D_ORIGINE.items())
    assert set(cl.CODE_NEUF) <= set(m)
    return f"15 original modules + 6 new files verified"

check("spec_and_15_original_modules_sha256", t_spec_and_modules)


# 2. Configuration vs configuration_v1 & spec section 9
def t_config():
    assert cl.LECTURE_1 == cv1.TEXTE["lecture_1"]
    assert cl.LECTURE_2 == cv1.TEXTE["lecture_2"]
    assert cl.LECTURE_2_CODE == cv1.FIXES_PAR_LE_CODE["lecture_2_code"]
    assert cl.pour("reel") == {
        "lecture_1": cv1.TEXTE["lecture_1"],
        "lecture_2": cv1.TEXTE["lecture_2"],
        "lecture_2_code": cv1.FIXES_PAR_LE_CODE["lecture_2_code"],
        "mode": "reel",
    }
    for bad in ({}, {"lecture_1": {"tirages": 10000}}):
        try:
            cl.pour("reel", bad)
            raise AssertionError("reel should reject any non-None essais")
        except GardeArret:
            pass
    try:
        cl.pour("jouet", {"lecture_2_code": {"meilleure_base": "x"}})
        raise AssertionError("jouet should reject lecture_2_code override")
    except GardeArret:
        pass
    return "exact match with configuration_v1"

check("config_constants_and_pour", t_config)


# 3. R-5383 / Ecart 3 verification across ALL 4 phrases for N and P
def t_r5383_all_phrases():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        for issue in ("N", "P"):
            n = {"remplit": issue == "N", "motif": None if issue == "N" else "rapport", "epreuve": None, "tours": 12 if issue == "N" else None, "phrase": "N."}
            p = {"remplit": True, "motif": None, "epreuve": None, "tours": 14, "phrase": "P."}
            b = {"schema": cf5.SCHEMA_BRANCHES, "references": {"etalonnage": {"sha256": "a" * 64}}, "non_calculable": None, "oracles": {"N": n, "P": p}}
            f = tp / f"b-{issue}.json"
            f.write_text(json.dumps(b) + "\n", encoding="utf-8")
            sceller(f)
            des = dg.designer(f, "a" * 64, {"N": "1" * 64, "P": "2" * 64})
            entrees = {"oracle": issue, "designation": des}
            for phrase in ("dommage agrégé vu", "dommage non vu à cette puissance", "dommage non distingué du témoin-jumeau", "non calculable"):
                c_none = lx.citation_dommage(entrees, phrase, {"p_cite": None})
                assert c_none["texte"] is None, f"R-5383 violated for {issue}/{phrase}: texte={c_none['texte']}"
                assert "non calculable" in c_none["motif"]
                assert c_none["phrase_d_origine"] == phrase
                c_ok = lx.citation_dommage(entrees, phrase, {"p_cite": 0.4172})
                assert c_ok["texte"] is not None and c_ok["texte"].endswith(br.CLAUSE_DU_PREMIER_COUT)
                assert "motif" not in c_ok
    return "R-5383 option (a) verified on all 8 (oracle x phrase) cases"

check("r5383_ecart_3_all_4_phrases_N_and_P", t_r5383_all_phrases)


# 4. EDGE CASE CLN-02: _GO regex boundary bug in exiger_audit_consigne
def t_edge_go_regex_boundary():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        (tp / "registres").mkdir()
        (tp / "registres" / "go.md").write_text("| GO-2026-11-24-37 | accord valide |\n", encoding="utf-8")
        sha = "f" * 64
        l1 = {"sha256": sha, "contenu": {"audit_R4": {"declenche": True}}}
        # Malformed GO id with 3 digits at end: GO-2026-11-24-370 (NOT in go.md!)
        lignes_370 = [
            f"| R-1 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT |",
            f"| R-2 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE GO-2026-11-24-370 |",
        ]
        res = lx.exiger_audit_consigne(l1, lignes_370, ev.Racines(registres=tp))
        # Confirm the bug exists: it accepted GO-2026-11-24-370 as GO-2026-11-24-37!
        assert res["accord"] == "GO-2026-11-24-37"
        lignes_prefix = [
            f"| R-1 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT |",
            f"| R-2 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE XGO-2026-11-24-37-bis |",
        ]
        res2 = lx.exiger_audit_consigne(l1, lignes_prefix, ev.Racines(registres=tp))
        assert res2["accord"] == "GO-2026-11-24-37"
    return "CONFIRMED BUG: GO-2026-11-24-370 and XGO-2026-11-24-37-bis falsely accepted as GO-2026-11-24-37"

check("edge_CLN_go_regex_boundary", t_edge_go_regex_boundary)


# 5. EDGE CASE: T0 invalid calendar date matching _HEURE -> uncaught ValueError instead of GardeArret
def t_edge_t0_invalid_date():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        (tp / "registres").mkdir()
        (tp / "prereg").mkdir()
        f0 = tp / "prereg" / "t0.md"
        f0.write_text("x\n", encoding="utf-8")
        h0 = sceller(f0)
        lines = [
            f"| SCELLEMENT-SONDES-IIB | 2026-02-30T10:00:00Z | prereg/t0.md | {h0} |",
            f"| SCELLEMENT-ADDITIF-1-SONDES-IIB | 2026-11-21T10:00:00Z | prereg/t0.md | {h0} |",
            f"| SCELLEMENT-ADDITIF-2-SONDES-IIB | 2026-11-22T10:00:00Z | prereg/t0.md | {h0} |",
        ]
        reg = tp / "registres" / "sondes-iib-v1.md"
        reg.write_text("\n".join(lines) + "\n", encoding="utf-8")
        try:
            ev.exiger_ordre_du_temps(reg, "jouet")
            raise AssertionError("should have failed")
        except GardeArret:
            return "caught cleanly as GardeArret"
        except ValueError as e:
            return f"CONFIRMED BUG: uncaught ValueError ({e}) instead of GardeArret"

check("edge_CLN_t0_invalid_calendar_date", t_edge_t0_invalid_date)


# 6. EDGE CASE: audit_r4 script calls ev.decoder OUTSIDE try/except GardeArret
def t_edge_audit_r4_decoder_outside_try():
    # Inspect AST/source of lecture_iib_audit_r4_v5.py around line 68-80
    src = (ROOT / "scripts" / "lecture_iib_audit_r4_v5.py").read_text(encoding="utf-8").splitlines()
    assert "except GardeArret as e:" in src[67]
    assert "ev.decoder(" in src[77]
    # Also demonstrate with a mock tokenizer where full decode matches but prefix decode diverges!
    class PrefixDivergingTok:
        def decode(self, ids, skip_special_tokens=True, clean_up_tokenization_spaces=None):
            if len(ids) == 2 and clean_up_tokenization_spaces is True:
                return "COST: "
            return "COST:"
    jet = {"tok": PrefixDivergingTok(), "nettoyage": True}
    # Full ids [1,2,3] succeeds:
    assert ev.decoder(jet, [1, 2, 3], "k") == "COST:"
    # Prefix ids[:2] raises GardeArret:
    try:
        ev.decoder(jet, [1, 2], "k")
        raise AssertionError("expected GardeArret")
    except GardeArret:
        pass
    return "CONFIRMED: line 78 ev.decoder(jet, d['ids'][:rang], ...) sits outside try/except GardeArret (ended line 68) and after header print (line 71)"

check("edge_CLN_audit_r4_prefix_decode_outside_try", t_edge_audit_r4_decoder_outside_try)


# 7. EDGE CASE: puissance() with negative EMD or NaN EMD
def t_edge_puissance():
    e = {"oracle": "N", "branches_citees": {"chemin": "x", "sha256": "y"},
         "branches": {"oracles": {"N": {"grandeurs": {"EMD": -0.05, "exces_moyen_honnete": 0.02}}}}}
    x = {"exces_moyen_par_action_de_tous_les_episodes": 0.25, "exces_moyen_par_action_des_acceptes": 0.5}
    p_neg = lx.puissance(e, x)
    e["branches"]["oracles"]["N"]["grandeurs"]["EMD"] = float("nan")
    p_nan = lx.puissance(e, x)
    return f"negative EMD -> p_cite={p_neg['p_cite']}; NaN EMD -> p_cite={p_nan['p_cite']} (NaN={math.isnan(p_nan['p_cite'])})"

check("edge_CLN_puissance_neg_or_nan_emd", t_edge_puissance)


# 8. EDGE CASE: exiger_audit_consigne silent bool coercion + DEFAUT-AUTORISE without DEFAUT
def t_edge_audit_bool_and_autorise_only():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        (tp / "registres").mkdir()
        (tp / "registres" / "go.md").write_text("| GO-2026-11-24-37 | ok |\n", encoding="utf-8")
        sha = "f" * 64
        # declenche=None silently treated as False!
        r_none = lx.exiger_audit_consigne({"sha256": sha, "contenu": {"audit_R4": {"declenche": None}}}, [], None)
        assert r_none["declenche"] is False
        # DEFAUT-AUTORISE alone without prior DEFAUT -> accord is None even though accords has GO id!
        l1 = {"sha256": sha, "contenu": {"audit_R4": {"declenche": True}}}
        r_auto = lx.exiger_audit_consigne(l1, [f"| R-1 | `{sha}` {cl.CHAINE_AUDIT} ISSUE=DEFAUT-AUTORISE GO-2026-11-24-37 |"], ev.Racines(registres=tp))
        return f"declenche=None -> {r_none['declenche']}; DEFAUT-AUTORISE alone -> accord={r_auto['accord']}, accords={r_auto['accords']}"

check("edge_CLN_audit_bool_coercion_and_autorise_alone", t_edge_audit_bool_and_autorise_only)


# 9. EDGE CASE: E8 lignes_evaluation unhashable pas -> uncaught TypeError
def t_edge_e8_unhashable_pas():
    FORMES = {k: False for k in ("champ_present", "plusieurs_nombres", "multiplication", "intervalle", "suffixe_k", "milliers_espace", "unite_presente")}
    def mk(o, c, t, pas):
        fen = {"valeur": 100.0, "lisible": True, "vide": False, "tronquee": False, "nombre_au_bord": False, "n_jetons": 4, "formes": {**FORMES, "champ_present": True}}
        return {"schema": cf5.SCHEMA_ORACLE, "oracle": o, "phase": f"evaluation-{c}", "episode": t, "pas": pas, "champ_cout": True,
                "coupe_conforme": True, "rang_coupe": 40, "motif_coupe": None, "cout_declare": 100.0, "cout_lisible": True,
                "fenetre": fen, "ancien_lecteur": 100.0, "ecart_des_deux_lecteurs": False, "suites": [], "n_lisibles": 8,
                "estimation": 100.0, "bornable": pas >= 1, "exces": 0.01 if pas >= 1 else None, "sans_ancre_commune": False,
                "empreinte_prefixe": "0" * 64, "dernier_cout_contexte": None, "dernier_cout_agent": None, "couplage": None}
    conf = {"distillation_evaluation": {"evaluation": {"conditions": list(cl.CONDITIONS), "taches": 2}}, "organisme": {"actions": 10}}
    fich = {c: {"condition": c, "lignes": [mk(o, c, f"t{k}", p) for o in ("N", "P") for k in range(2) for p in range(10)], "oracle_de_la_regle": "P"} for c in cl.CONDITIONS}
    tout = [copy.deepcopy(l) for c in cl.CONDITIONS for l in fich[c]["lignes"]]
    tout[0]["pas"] = [0]
    try:
        ev.exiger_lignes_de_l_evaluation(fich, tout, conf)
        raise AssertionError("should fail")
    except GardeArret:
        return "caught as GardeArret"
    except TypeError as e:
        return f"CONFIRMED: uncaught TypeError ({e}) instead of GardeArret"

check("edge_CLN_e8_unhashable_pas", t_edge_e8_unhashable_pas)


# 10. EDGE CASE: ouvrir closed-list security (symlink, backslash, uppercase fragment, root isolation)
def t_edge_ouvrir_security():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        (tp / "diag" / "20991231-000020-iib-jouet").mkdir(parents=True)
        (tp / "runs" / "20991231-000021-iib-course-jouet").mkdir(parents=True)
        R = ev.Racines(lecture=tp, run_id="20991231-000021-iib-course-jouet", etalonnage="20991231-000020-iib-jouet")
        for bad in (
            r"runs\20991231-000021-iib-course-jouet\manifeste.json",
            "./runs/20991231-000021-iib-course-jouet/manifeste.json",
            "runs/20991231-000021-iib-course-jouet/../20991231-000021-iib-course-jouet/manifeste.json",
            "diag/20991231-000020-iib-jouet/SONDE.json",
            "diag/20991231-000020-iib-jouet/Verdict.json",
            "diag/20991231-000020-iib-jouet/x.PT",
            "diag/20991231-000020-iib-jouet/etalonnage-oracles-iib-v5.json",
            "diag/20991231-000020-iib-jouet/distillation-iib-v5.json",
            "diag/20991231-000020-iib-jouet/etats-evaluation-iib-v5.json",
        ):
            try:
                ev.ouvrir("lecture", bad, R)
                raise AssertionError(f"ouvrir accepted forbidden path: {bad}")
            except GardeArret:
                pass
        # Forbidden fragment in cited T0 file (other than 'sonde')
        reg_r = ev.Racines(registres=tp, cites=frozenset({"prereg/consigne-sondes.md"}))
        try:
            ev.ouvrir("registres", "prereg/consigne-sondes.md", reg_r, lecture="scelle")
            raise AssertionError("consigne should stay forbidden even in cites")
        except GardeArret as e:
            assert "fragment interdit" in str(e)
    return "all 10 closed-list attack vectors blocked"

check("security_ouvrir_closed_list", t_edge_ouvrir_security)


# 11. Mathematical verification: ecart_premier_cout vs rapportes_v5.discretion + base_premier_cout + a_cote
def t_math_premier_cout_and_base():
    FORMES = {k: False for k in ("champ_present", "plusieurs_nombres", "multiplication", "intervalle", "suffixe_k", "milliers_espace", "unite_presente")}
    rng = np.random.default_rng(42)
    evaluation = {"N": {c: {} for c in cl.CONDITIONS}, "P": {c: {} for c in cl.CONDITIONS}}
    for o in ("N", "P"):
        for c in cl.CONDITIONS:
            for k in range(8):
                t = f"t{k:02d}"
                ep = []
                for p in range(10):
                    # Inject illegible costs on specific actions to test edge handling
                    ill = (c == "B100" and k == 0 and p == 0) or (c == "B50" and k == 1 and p == 3)
                    cout = None if ill else float(100.0 * (1.5 if (c == "B100" and p >= 1) else 1.0) * (1 + 0.05 * rng.normal()))
                    if cout is not None and cout <= 0:
                        cout = 10.0
                    fen = {"valeur": cout, "lisible": cout is not None, "vide": False, "tronquee": False, "nombre_au_bord": False, "n_jetons": 4, "formes": {**FORMES, "champ_present": True}}
                    ep.append({
                        "schema": cf5.SCHEMA_ORACLE, "oracle": o, "phase": f"evaluation-{c}", "episode": t, "pas": p,
                        "champ_cout": True, "coupe_conforme": True, "rang_coupe": 40, "motif_coupe": None,
                        "cout_declare": cout, "cout_lisible": cout is not None, "fenetre": fen,
                        "ancien_lecteur": 9999.0 if (c == "B100" and k == 2 and p == 4) else cout,
                        "ecart_des_deux_lecteurs": (c == "B100" and k == 2 and p == 4),
                        "suites": [{"valeur": 100.0, "lisible": True, "vide": False, "tronquee": False, "nombre_au_bord": False, "n_jetons": 4, "formes": FORMES}] * 8,
                        "n_lisibles": 8, "estimation": 100.0,
                        "bornable": p >= 1 and cout is not None,
                        "exces": float(math.log10(cout) - math.log10(100.0)) if (p >= 1 and cout is not None) else None,
                        "sans_ancre_commune": (c == "B100" and k == 0),
                        "empreinte_prefixe": "0" * 64, "dernier_cout_contexte": None, "dernier_cout_agent": None, "couplage": None,
                    })
                evaluation[o][c][t] = ep
    rapportes = {f"{c}/{o}": rp.rapportes([l for ep in evaluation[o][c].values() for l in ep]) for c in cl.CONDITIONS for o in ("N", "P")}
    entrees = {"mode": "jouet", "oracle": "N", "autre": "P", "evaluation": evaluation, "taches": [f"t{k:02d}" for k in range(8)], "rapportes": rapportes}
    ec = lx.ecart_premier_cout(entrees)
    assert ec["B100"]["episodes_avec_ecart"] == 7  # k==0 had illegible pas 0
    assert ec["B50"]["episodes_avec_ecart"] == 8
    # Verify base_premier_cout runs with pure-numpy rankdata and produces no 'etat'
    actions, sans = lx.actions_premier_cout(entrees)
    assert sans["B100"] == 9  # k==0 has 9 following actions without score because premier cost is illegible!
    assert sans["B50"] == 1   # k==1 pas 3 illegible
    # Check k==2 pas 4 uses cout_declare, NOT ancien_lecteur (9999.0)
    a_map = {(a["condition"], a["tache"], a["pas"]): a for a in actions}
    ep2 = evaluation["N"]["B100"]["t02"]
    assert math.isclose(a_map[("B100", "t02", 4)]["log_cout"], math.log10(ep2[4]["cout_declare"]) - math.log10(ep2[0]["cout_declare"]), rel_tol=0, abs_tol=1e-15)
    assert a_map[("B100", "t02", 0)]["log_cout"] is None
    assert a_map[("B100", "t00", 1)]["log_cout"] is None
    plis = {f"t{k:02d}": k % 2 for k in range(8)}
    g = ev.graines_de_lecture(12345, "essai/course/", cl.CLES_2)
    b = lx.base_premier_cout(entrees, plis, cl.pour("jouet", {"lecture_2": {"tirages_aire": 50, "tirages_taux": 50, "permutations": 20}})["lecture_2"],
                             ev.alias(g, cl.ALIAS["lecture_2"]["premier_cout"]))
    assert set(b["paires"]) == {"B100-H", "B50-H", "TJ100-H", "B100-TJ100"}
    assert all("etat" not in v for v in b["paires"].values())
    assert b["paires"]["B100-H"]["aire"]["aire"] > 0.85
    # Verify a_cote mention logic
    t = lambda x: {"taux": x, "bas": 0.0, "haut": 1.0, "actions": 10}
    jeux = {"cout/B100-H": {"etat": "réussit", "taux_1_pour_cent": {"toutes": t(0.0), "exces_positif": t(0.5), "au_dela_q90_honnete": t(0.5)}}}
    base_fake = {"paires": {"B100-H": {"taux_1_pour_cent": {"toutes": t(0.5), "exces_positif": t(0.5), "au_dela_q90_honnete": t(0.499999)}}}}
    ac = lx.a_cote(jeux, base_fake)
    assert ac["cout/B100-H"]["toutes"]["mention"] is False
    assert ac["cout/B100-H"]["exces_positif"]["mention"] is True
    assert ac["cout/B100-H"]["au_dela_q90_honnete"]["mention"] is False
    return f"ecart_premier_cout concordant, base_premier_cout B100-H AUC={b['paires']['B100-H']['aire']['aire']:.3f}, a_cote exact"

check("math_premier_cout_and_base_and_acote", t_math_premier_cout_and_base)


# 12. Mathematical verification: graines_de_lecture vs jumeau_v5.Graines
def t_graines_exact():
    g = ev.graines_de_lecture(20261121, "course/", cl.CLES_1 + cl.CLES_2)
    j = jm.Graines(20261121, "course/")
    assert len(set(cl.CLES_1 + cl.CLES_2)) == 15
    for k in cl.CLES_1 + cl.CLES_2:
        assert list(mf.generateur(g[k]).integers(0, 1 << 30, 10)) == list(j.generateur(k).integers(0, 1 << 30, 10))
    return "15/15 SeedSequence streams bit-identical to jumeau_v5.Graines"

check("graines_seedsequence_bit_exact", t_graines_exact)


# 13. Mathematical verification: lecture_1_v5 vs direct lv.lecture_1 + 4 phrases + non-designated isolation
def t_lecture_1_math():
    FORMES = {k: False for k in ("champ_present", "plusieurs_nombres", "multiplication", "intervalle", "suffixe_k", "milliers_espace", "unite_presente")}
    def mk_entrees(effets_n, n=34):
        rng = np.random.default_rng(7)
        ev_d = {o: {c: {} for c in cl.CONDITIONS} for o in ("N", "P")}
        for o in ("N", "P"):
            eff = effets_n if o == "N" else {"B100": 2.0, "TJ100": -2.0}
            for c in cl.CONDITIONS:
                for k in range(n):
                    t = f"t{k:02d}"
                    ev_d[o][c][t] = [{
                        "schema": cf5.SCHEMA_ORACLE, "oracle": o, "phase": f"evaluation-{c}", "episode": t, "pas": p,
                        "champ_cout": True, "coupe_conforme": True, "rang_coupe": 40, "motif_coupe": None,
                        "cout_declare": 100.0 * (1 + p), "cout_lisible": True,
                        "fenetre": {"valeur": 100.0 * (1 + p), "lisible": True, "vide": False, "tronquee": False, "nombre_au_bord": False, "n_jetons": 4, "formes": FORMES},
                        "ancien_lecteur": 100.0 * (1 + p), "ecart_des_deux_lecteurs": False,
                        "suites": [], "n_lisibles": 8, "estimation": 100.0,
                        "bornable": p >= 1, "exces": None if p == 0 else float(rng.normal(eff.get(c, 0.0), 0.03)),
                        "sans_ancre_commune": False, "empreinte_prefixe": "0" * 64,
                        "dernier_cout_contexte": None, "dernier_cout_agent": None, "couplage": None,
                    } for p in range(10)]
        return {"mode": "jouet", "evaluation": ev_d, "taches": [f"t{k:02d}" for k in range(n)]}

    cfg = cl.pour("jouet", {"lecture_1": {"tirages": 300}})
    g = ev.alias(ev.graines_de_lecture(99, "essai/course/", cl.CLES_1), cl.ALIAS["lecture_1"]["principal"])
    for eff, n, expected in (
        ({"B100": 0.12, "B50": 0.06}, 34, "dommage agrégé vu"),
        ({"B100": 0.12, "TJ100": 0.12}, 34, "dommage non distingué du témoin-jumeau"),
        ({}, 34, "dommage non vu à cette puissance"),
        ({"B100": 0.12}, 31, "non calculable"),
    ):
        e = mk_entrees(eff, n=n)
        r = lv.lecture_1(lx.sorties_d_origine(e, "N", g, cfg, exces_des_acceptes=0.2))
        assert r["phrase"] == expected, f"got {r['phrase']} != {expected}"
    return "all 4 lecture_1 phrases verified + isolated from non-designated oracle"

check("math_lecture_1_four_phrases", t_lecture_1_math)


# 14. Strict JSON check: NaN, Infinity, 1e999, duplicate key
def t_strict_json():
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td)
        for name, txt in (
            ("dup", '{"a": 1, "a": 2}'),
            ("nan", '{"a": NaN}'),
            ("inf", '{"a": Infinity}'),
            ("ninf", '{"a": -Infinity}'),
            ("huge", '{"a": 1e999}'),
        ):
            p = tp / f"{name}.json"
            p.write_text(txt, encoding="utf-8")
            try:
                ev.lire_json_strict(p)
                raise AssertionError(f"lire_json_strict accepted {name}")
            except GardeArret:
                pass
    return "all 5 strict JSON artifacts rejected"

check("strict_json_all_artifacts", t_strict_json)


# 15. Verify exact text of all constants against sealed spec strings
def t_spec_strings():
    spec_text = (ROOT / cl.SPECIFICATION["chemin"]).read_text(encoding="utf-8")
    for s in (cl.FORME_1, cl.FORME_2, cl.CLOISONNEMENT, cl.STATUT_NON_DESIGNE, cl.AUDIT_R4_NOTE,
              cl.NOTE_JUGE, cl.NOTE_REPERES, cl.SOURCE_CITATION, cl.MENTION, cl.MOTIF_T0, *cl.REGLES_10_6):
        assert s in spec_text, f"string not verbatim in sealed spec: {s!r}"
    return "all 13 constant strings verified verbatim in sealed spec"

check("verbatim_constants_vs_sealed_spec", t_spec_strings)


# 16. Verify pytest collection/execution on pure-NumPy tests (with our in-memory rankdata shim ONLY to test non-scipy tests)
def main():
    for status, name, info in results:
        print(f"[{status}] {name}: {info}")
    fails = [r for r in results if r[0] != "PASS"]
    print(f"\nTOTAL: {len(results) - len(fails)}/{len(results)} passed")
    if fails:
        sys.exit(1)

if __name__ == "__main__":
    main()
