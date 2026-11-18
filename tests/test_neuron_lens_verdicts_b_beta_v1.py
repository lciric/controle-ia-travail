"""Essais (R5) du code des verdicts de la tranche de l'ajustement de nos lentilles — cas de P.4 du texte gelé
`docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` (`f5d46860…`), table principale et table des branches (part du code
des verdicts ; les gardes du montage sont essayées dans la commande)."""
import copy
import hashlib
import json
from pathlib import Path

import pytest

from controle_ia.neuron_lens import verdicts_b_beta_v1 as V

RACINE = Path(__file__).resolve().parents[1]
REF = RACINE / "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee"
SHA = {"causal_lens_qwen3-8b.json": "8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3",
       "reads_at_firings_qwen3-8b.json": "ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd"}


def charger(nom):
    p = REF / nom
    assert hashlib.sha256(p.read_bytes()).hexdigest() == SHA[nom]
    return json.loads(p.read_text())


def sain() -> V.Entrees:
    """Cas (i) : référence publiée de Qwen3-8B ramenée à 32 couches ; B-1 par moitiés factices saines (0,05 ; 0,90) ; série repère =
    `npR` du même fichier ; n = 64 ; aucune garde de machine en défaut."""
    t = V.depuis_reference_qwen(charger("causal_lens_qwen3-8b.json")["targets"])
    rs, si = V.reads_depuis_reference_qwen(charger("reads_at_firings_qwen3-8b.json"))
    return V.Entrees(score=t, n={c: [64] * 32 for c in V.CIBLES}, repere_npR=list(t["steer 1x"]["npR"]["r_med"]),
                     stabilite={k: [0.05] * nb for k, nb in V.CIBLES_STABILITE.items()},
                     accord={l: 0.90 for l in V.COUCHES_ACCORD}, read_S=rs, silent=si,
                     gardes={g: False for g in V.GARDES_MACHINE + ("identite",)})


def poser(e, cible, lentille, cle, couches_, valeur):
    for l in couches_:
        e.score[cible][lentille][cle][l] = valeur


A1_SAIN = {"temoin_distinct": True, "normes_non_nulles": True}


def graine1(e):
    """Sortie de la graine 1 simulée : la même table que la graine 0 (verdicts gardés)."""
    return A1_SAIN | {"score": copy.deepcopy(e.score), "n": copy.deepcopy(e.n)}


# ---------------------------------------------------------------- cas (i) et valeurs de B-5

def test_i_reference():
    e = sain()
    assert V.declencheurs(e) == []
    v = V.verdict(e)
    assert v.verdict == V.REPRODUIT and v.defauts == [] and v.reserves == []
    for k in ("B-1", "B-2", "B-3", "B-5", "B-7"):
        assert v.mesures[k]["verdict"] == "reproduit", k
    assert v.mesures["B-6"]["verdict"] == "accord"
    b5 = v.mesures["B-5"]
    assert abs(b5["read_S_0"] - 0.8481) < 1e-4 and abs(b5["moyenne_1_7"] - 0.2248) < 1e-4
    assert abs(b5["moyenne_12_23"] - 0.0271) < 1e-4 and abs(b5["ecart"] - 0.1977) < 1e-4
    assert b5["silent_0"] < 5e-4 and abs(b5["silent_moyen_1_7"] - 0.240) < 1e-3  # « 0,000 » à trois décimales


# ---------------------------------------------------------------- (ii)

def test_ii_a():
    e = sain()
    poser(e, "steer 1x", V.NOTRE_R, "pass", range(16, 28), 0.40)
    v = V.verdict(e)
    assert v.mesures["B-2"]["verdict"] == "non reproduit"
    assert v.mesures["B-3"]["verdict"] == "reproduit" and v.mesures["B-7"]["verdict"] == "reproduit"
    assert v.verdict == V.NON_REPRODUIT and "défaut dans notre lentille" in v.reserves


def test_ii_b():
    e = sain()
    poser(e, "steer 1x", V.NOTRE_R, "control_med", [10], 0.20)
    v = V.verdict(e)
    assert v.verdict == V.CHAINE and any(x.startswith("(a)") for x in v.defauts)


def test_ii_c():
    e = sain()
    for c in V.CIBLES:
        e.score[c][V.NOTRE_R]["r_med"] = list(e.score[c]["logit"]["r_med"])
    v = V.verdict(e)
    assert v.verdict == V.CHAINE and any(x.startswith("(e) repli") for x in v.defauts)


@pytest.mark.parametrize("garde", ["identite", "h", "o", "p", "g", "q", "r", "s", "d", "f", "i", "k", "n"])
def test_gardes_de_machine(garde):
    """(ii-d) identité ; (ii-e) 30 couches → (h) ; (iv-b) → (n) ; (viii-b) → (o) ; (viii-c) → (p) ; (viii-d) → (g) ; et chaque
    autre garde constatée sur la machine : toute garde en défaut donne la chaîne en défaut, sans verdict de mesure."""
    e = sain()
    e.gardes[garde] = True
    v = V.verdict(e)
    assert v.verdict == V.CHAINE and len(v.defauts) == 1


# ---------------------------------------------------------------- (iii) B-5

def test_iii_a():
    e = sain()
    e.read_S[0] = 0.25
    v = V.verdict(e)
    assert v.mesures["B-5"]["verdict"] == "non reproduit" and v.verdict == V.PARTIEL


def test_iii_b():
    e = sain()
    for l in range(1, 8):
        e.read_S[l] = 0.05
    for l in range(12, 24):
        e.read_S[l] = 0.05
    v = V.verdict(e)
    assert v.mesures["B-5"]["verdict"] == "non reproduit" and v.verdict == V.PARTIEL


def test_iii_c():
    e = sain()
    e.silent[0] = 0.45
    v = V.verdict(e)
    assert v.mesures["B-5"]["verdict"] == "non lisible" and v.verdict == V.PARTIEL


@pytest.mark.parametrize("extreme", ["haut", "bas"])
def test_iii_d_e(extreme):
    e = sain()
    if extreme == "haut":
        e.read_S[0] = 1.0
    else:
        e.read_S = [0.0] * 32
    assert "A4" in V.declencheurs(e)
    v = V.verdict(e, {"A4": {"permutation_ok": True, "lentille_S_ok": True}})
    assert v.verdict != V.CHAINE
    assert v.mesures["B-5"]["verdict"] == ("reproduit" if extreme == "haut" else "non reproduit")
    v2 = V.verdict(e, {"A4": {"permutation_ok": False, "lentille_S_ok": True}})
    assert v2.verdict == V.CHAINE and any(x.startswith("(m)") for x in v2.defauts)


# ---------------------------------------------------------------- (iv) B-6 et A6

def test_iv_a():
    e = sain()
    poser(e, "steer 1x", "npR", "r_med", [10], round(e.score["steer 1x"][V.NOTRE_R]["r_med"][10] - 0.20, 4))
    e.repere_npR = list(e.score["steer 1x"]["npR"]["r_med"])  # la série repère suit la publique : (j) tenue
    v = V.verdict(e)
    assert v.mesures["B-6"]["verdict"] == "désaccord" and "écart de corpus" in v.reserves and v.verdict == V.REPRODUIT
    e2 = copy.deepcopy(e)
    poser(e2, "steer 1x", V.MOITIES[0], "r_med", [10], round(e2.score["steer 1x"][V.NOTRE_R]["r_med"][10] + 0.10, 4))
    v2 = V.verdict(e2)
    assert "écart d'ajustement" in v2.reserves and v2.verdict == V.REPRODUIT


# ---------------------------------------------------------------- (v) A1

def test_v_a1():
    e = sain()
    poser(e, "steer 1x", V.NOTRE_R, "r_med", [3], 0.96)
    assert "A1" in V.declencheurs(e)
    assert V.verdict(e, {"A1": graine1(e)}).verdict in (V.REPRODUIT, V.PARTIEL)
    g = graine1(e)
    poser_g = g["score"]["steer 1x"][V.NOTRE_R]["pass"]
    for l in range(16, 28):
        poser_g[l] = 0.40
    v = V.verdict(e, {"A1": g})
    assert v.mesures["B-2"]["verdict"] == "autre"
    v = V.verdict(e, {"A1": graine1(e) | {"temoin_distinct": False}})
    assert v.verdict == V.CHAINE and any(x.startswith("(l)") for x in v.defauts)
    assert V.verdict(e, {"A1": V.NON_JOUE}).verdict == V.NON_CONCLU
    g = graine1(e)
    g["score"]["steer 1x"]["logit"]["control_med"][5] = 0.2
    v = V.verdict(e, {"A1": g})
    assert v.verdict == V.CHAINE and any("graine 1" in x for x in v.defauts)


def test_a1_zeros_du_temoin():
    e = sain()
    poser(e, "steer 1x", V.NOTRE_R, "control_med", [5, 9], 0.0)
    assert "A1" in V.declencheurs(e)
    e = sain()
    poser(e, "steer 1x", V.NOTRE_R, "control_med", [5], 0.0)
    assert "A1" not in V.declencheurs(e)
    e = sain()
    poser(e, "ablate pos", "J", "control_med", [5, 9], 0.0)
    assert "A1" not in V.declencheurs(e)


# ---------------------------------------------------------------- (vi) B-1, A2, A3

def test_vi_a():
    assert V.verdict(sain()).mesures["B-1"]["verdict"] == "reproduit"


def test_vi_b():
    e = sain()
    e.stabilite[("R", "out")][4] = 0.25
    assert "A3" in V.declencheurs(e)
    v = V.verdict(e, {"A3": {"controles_ok": True}})
    assert v.mesures["B-1"]["verdict"] == "non reproduit" and v.verdict == V.PARTIEL
    v = V.verdict(e, {"A3": {"controles_ok": False}})
    assert v.verdict == V.CHAINE and any(x.startswith("(g)") for x in v.defauts)


def test_vi_c():
    e = sain()
    e.accord[12] = 0.50
    assert "A3" in V.declencheurs(e)
    v = V.verdict(e, {"A3": {"controles_ok": True}})
    assert v.mesures["B-1"]["verdict"] == "non reproduit" and v.verdict == V.PARTIEL


def test_vi_d():
    e = sain()
    e.stabilite[("S", "mid")][3] = 0.0
    assert "A2" in V.declencheurs(e)
    assert V.verdict(e, {"A2": {"controles_ok": False}}).verdict == V.CHAINE
    assert V.verdict(e, {"A2": {"controles_ok": True}}).mesures["B-1"]["verdict"] == "reproduit"


def test_vi_e():
    e = sain()
    e.accord = {l: 1.0 for l in V.COUCHES_ACCORD}
    assert "A2" in V.declencheurs(e)
    assert V.verdict(e, {"A2": {"controles_ok": True}}).mesures["B-1"]["verdict"] == "reproduit"


# ---------------------------------------------------------------- (vii) et branches de (j)

def test_vii_et_branches_j():
    e = sain()
    for l in (4, 9, 14):
        e.repere_npR[l] = round(e.repere_npR[l] + 0.06, 4)
    assert any(x.startswith("(j)") for x in V.verdict(e).defauts)
    e = sain()
    for l in (4, 9):
        e.repere_npR[l] = round(e.repere_npR[l] + 0.06, 4)
    assert V.verdict(e).defauts == []
    e = sain()
    e.repere_npR[4] = round(e.repere_npR[4] + 0.11, 4)
    assert any(x.startswith("(j)") for x in V.verdict(e).defauts)


# ---------------------------------------------------------------- (x) A5, (xi), rangs 2 et 3

def test_x_a5():
    e = sain()
    poser(e, "ablate win", V.NOTRE_R, "r_med", range(8, 14), 0.45)
    assert "A5" in V.declencheurs(e)
    v = V.verdict(e, {"A5": graine1(e)})
    assert v.mesures["B-7"]["verdict"] == "non reproduit" and v.verdict == V.REPRODUIT
    g = graine1(e)
    for l in range(8, 14):
        g["score"]["ablate win"][V.NOTRE_R]["r_med"][l] = 0.10
    v = V.verdict(e, {"A5": g})
    assert v.mesures["B-7"]["verdict"] == "autre" and v.verdict == V.REPRODUIT
    assert V.verdict(e, {"A5": V.NON_JOUE}).mesures["B-7"]["verdict"] == "autre"


def test_xi_tout_negatif():
    e = sain()
    poser(e, "steer 1x", V.NOTRE_R, "pass", range(16, 28), 0.40)
    lg = e.score["steer 1x"]["logit"]["r_med"]
    for l in range(4, 16):
        e.score["steer 1x"][V.NOTRE_R]["r_med"][l] = round(lg[l] - 0.01, 4)
    v = V.verdict(e)
    assert v.mesures["B-2"]["verdict"] == "non reproduit" and v.mesures["B-3"]["verdict"] == "non reproduit"
    assert v.verdict == V.NON_REPRODUIT and "défaut dans notre lentille" in v.reserves


def test_rang_2_prime_sur_rang_3():
    e = sain()
    e.stabilite[("R", "out")][4] = 0.25
    poser(e, "steer 1x", V.NOTRE_R, "pass", range(16, 28), 0.40)
    assert V.verdict(e, {"A3": V.NON_JOUE}).verdict == V.NON_CONCLU


def test_chaine_prime_sur_tout():
    e = sain()
    e.gardes["k"] = True
    e.stabilite[("R", "out")][4] = 0.25
    assert V.verdict(e, {"A3": V.NON_JOUE}).verdict == V.CHAINE


# ---------------------------------------------------------------- refus (R5)

def test_refus_valeur_non_ecrite_a_4_decimales():
    e = sain()
    e.score["steer 1x"][V.NOTRE_R]["r_med"][3] = 0.123456
    with pytest.raises(ValueError):
        V.verdict(e)


def test_refus_audit_sans_resultat():
    e = sain()
    e.read_S[0] = 1.0
    with pytest.raises(ValueError):
        V.verdict(e)


def test_refus_garde_non_renseignee():
    e = sain()
    del e.gardes["q"]
    with pytest.raises(ValueError):
        V.verdict(e)


def test_refus_valeur_non_finie_b1():
    e = sain()
    e.stabilite[("R", "mid")][2] = float("nan")
    with pytest.raises(ValueError):
        V.verdict(e)
