"""Essais des corrections CLA (contre-lecture R2 `contre-lecture-addendum-v3-et-corrections-v1.md` : CLA-03, CLA-04,
CLA-09 ; addendum v4, point (vii), ordre de gel). Chaque garde nouvelle a un cas sain et un artefact qui échoue vraiment
(R5). Plomberie seulement : lignes synthétiques, sources de code jouets, copies temporaires de l'addendum (aucun
compagnon n'est écrit pour le vrai addendum), mondes RACINE_VALIDATION aux indices 956000 à 956009 (hors de toute
plage du § 7) ; RACINE n'est jamais employée ; aucun contraste de décision, aucune moyenne de Δ(N, ·), aucun résultat de
V1 à V9 n'est calculé ni lu (seuls des égalités, des appartenances et des exceptions).
Usage : PYTHONPATH=<dépôt>/src python3 -B -m pytest -q -p no:cacheprovider essais/essais_cla_v2.py
"""
import hashlib
import shutil

import pytest

from jouets_v2 import ICI

import balayage_v2 as ba
import bras_v2 as br
import graines_v2 as gr
import invocation_unique_v2 as inv
import lecture_v2 as le
import mesures_v2 as ms
import monde_v2 as mo
from controle_ia.gardes import GardeArret
from controle_ia.scellement import compagnon, sceller

RV = gr.RACINE_VALIDATION
K_CLA = 956_000
VRAI_ADDENDUM = inv.DEPOT / "prereg" / inv.ADDENDUM


# --- CLA-04 : empreinte de l'addendum fixée dans le code -------------------------------------------------------

def _copie_addendum(tmp_path, suffixe=b""):
    """Copie temporaire du texte de l'addendum (octets), éventuellement modifiée, scellée DANS tmp_path seulement."""
    (tmp_path / "prereg").mkdir()
    copie = tmp_path / "prereg" / inv.ADDENDUM
    copie.write_bytes(VRAI_ADDENDUM.read_bytes() + suffixe)
    sceller(copie)
    return copie


def test_cla04_sain_texte_v4_scelle_accepte(tmp_path):
    assert inv.ADDENDUM == "addendum-ecarts-bisociation-deux-espaces-v2-v6.md"
    assert hashlib.sha256(VRAI_ADDENDUM.read_bytes()).hexdigest() == inv.EMPREINTE_ADDENDUM   # lecture seule
    _copie_addendum(tmp_path)
    assert inv.exiger_addendum_scelle(tmp_path) == inv.EMPREINTE_ADDENDUM


def test_cla04_artefact_texte_modifie_puis_rescelle_refuse(tmp_path, monkeypatch):
    # le compagnon concorde (texte modifié puis scellé à nouveau) : seule la constante peut l'arrêter
    copie = _copie_addendum(tmp_path, suffixe=b"\nligne ajoutee apres contre-lecture\n")
    assert compagnon(copie).is_file()
    with pytest.raises(GardeArret, match="texte autre que celui fixé"):
        inv.exiger_addendum_scelle(tmp_path)
    # et le vrai texte refusé si la constante du code diffère
    shutil.rmtree(tmp_path / "prereg")
    _copie_addendum(tmp_path)
    monkeypatch.setattr(inv, "EMPREINTE_ADDENDUM", "0" * 64)
    with pytest.raises(GardeArret, match="texte autre que celui fixé"):
        inv.exiger_addendum_scelle(tmp_path)


def test_cla04_le_vrai_addendum_n_est_pas_scelle_par_les_essais():
    # garde de procédure : aucun essai n'écrit de compagnon pour le vrai addendum (il est scellé à l'étape (5) du gel)
    assert not compagnon(VRAI_ADDENDUM).is_file()


# --- CLA-03 : identités entre toutes les paires de bras ------------------------------------------------------

def _ligne(sorties, exclu=None):
    return {"exclu": exclu, "bras": {b: {"_paires": list(p)} for b, p in sorties.items()}}


BASE = {"N": range(12), "b": range(1, 13), "a": range(2, 14), "d1": range(3, 15), "d1c": range(4, 16),
        "c": range(5, 17), "b_eloigne": range(6, 18), "N_global": range(7, 19), "N_beta0": range(8, 20),
        "N_q": range(9, 21)}


def test_cla03_sain_bras_differents_sur_un_monde_et_monde_exclu_ignore():
    # b égal à N sur deux mondes non exclus, différent sur un troisième : pas d'identité
    l1 = _ligne({**BASE, "b": range(12)})
    l2 = _ligne({**BASE, "b": range(12)})
    l3 = _ligne(BASE)
    assert inv.identites_paires([l1, l2, l3]) == []
    # b égal à N sur le seul monde EXCLU, différent ailleurs : le monde exclu ne crée pas d'identité
    assert inv.identites_paires([_ligne({**BASE, "b": range(12)}, exclu="moins de 12 paires valides"), l3]) == []
    # même ensemble de paires dans un autre ordre : pas identique (égalité des listes ordonnées, addendum (vi-b))
    assert inv.identites_paires([_ligne({**BASE, "b": list(reversed(range(12)))})]) == []
    assert inv.identites_a_N([l3]) == [] and le.identites_audit({"M_bien": inv.identites_paires([l3])}) == ({}, {})


def test_cla03_artefact_copies_sur_tous_les_mondes_non_exclus_rapportees_et_filtrees():
    copie = {**BASE, "N_global": range(12), "d1c": range(3, 15), "b_eloigne": range(1, 13), "N_q": range(12)}
    lignes = [_ligne(copie), _ligne(copie),
              _ligne({**BASE, "b_eloigne": range(40, 52)}, exclu="aucune vraie paire valide")]  # exclu : ignoré
    ident = inv.identites_paires(lignes)
    # rangées dans l'ordre de bras_v2.ORDRE_BRAS
    assert ident == [("N", "N_global"), ("N", "N_q"), ("b", "b_eloigne"), ("d1", "d1c"), ("N_global", "N_q")]
    assert inv.identites_a_N(lignes) == ["N_global", "N_q"]
    dec, rap = le.identites_audit({"M_bien": ident})
    assert dec == {"M_bien": [("N", "N_global")]}                   # N avec un bras de la liste du texte : déclenche
    assert rap == {"M_bien": [("N", "N_q"), ("b", "b_eloigne"), ("d1", "d1c"), ("N_global", "N_q")]}
    # d1c ≡ d1 hors NR : identité entre deux bras autres que N, rapportée sans déclencher (texte scellé : seules les
    # identités de N déclenchent ; addendum v4 (vi-b)) ; dans NR elle est en outre déclarée d'avance
    assert le.identites_audit({"NR_bien": [("d1", "d1c")]}) == ({}, {"NR_bien": [("d1", "d1c")]})
    # exception déclarée N ≡ N_β0 dans V_concepts_absents, non déclarée ailleurs
    assert le.identites_audit({"V_concepts_absents": [("N", "N_beta0")]})[0] == {}
    assert le.identites_audit({"M_moyen": [("N", "N_beta0")]})[0] == {"M_moyen": [("N", "N_beta0")]}
    # la chaîne complète jusqu'au déclencheur d'audit
    c = {("N-b", X): {"estimation": 0.0} for X in le.X2} | {("N-a", X): {"ub95": 1.0} for X in le.X2}
    d = le.declencheurs_audit(c, {"A3": True, "gain_controle": False}, {"M_bien": 0.1}, {"M_bien": 0.9},
                              {"M_bien": ident}, False, None, None)
    assert any("identités non déclarées" in x for x in d)
    d0 = le.declencheurs_audit(c, {"A3": True, "gain_controle": False}, {"M_bien": 0.1}, {"M_bien": 0.9},
                               {"M_bien": [p for p in ident if p != ("N", "N_global")]}, False, None, None)
    assert d0 == []


def test_cla03_sain_monde_reel_bras_absent_non_applicable():
    # d1c non applicable (absent des sorties) dans V_concepts_absents : ne forme de paire avec aucun bras
    lignes = [ms.executer_monde(mo.generer("V_concepts_absents", RV, i), "V_concepts_absents", RV, i,
                                ["N", "b", "d1", "d1c"]) for i in range(K_CLA, K_CLA + 3)]
    assert all(p[0] != "d1c" and p[1] != "d1c" for p in inv.identites_paires(lignes))


# --- CLA-09 : vue observée sans indicateur de condition ; préfixes d'étiquette refusés au balayage -------------

def test_cla09_sain_obs_sans_indicateurs_et_d1c_jamais_execute_en_NR_ni_concepts_absents():
    assert "nr" not in mo.Obs.__slots__ and "concepts_absents" not in mo.Obs.__slots__
    for cond in ("NR_bien", "V_concepts_absents", "M_bien"):
        w = mo.generer(cond, RV, K_CLA + 5)
        for nom in ("nr", "concepts_absents"):
            with pytest.raises(mo.AccesLatent):
                getattr(w.obs, nom)
    for cond in ("NR_bien", "NR_moyen", "V_concepts_absents"):
        r = ms.executer_monde(mo.generer(cond, RV, K_CLA + 6), cond, RV, K_CLA + 6, ["N", "d1", "d1c"])
        assert r["exclu"] or ("d1c" not in r["bras"] and "d1" in r["bras"])
    r = ms.executer_monde(mo.generer("M_bien", RV, K_CLA + 6), "M_bien", RV, K_CLA + 6, ["d1c"])
    assert r["exclu"] or len(r["bras"]["d1c"]["_paires"]) == 12


def test_cla09_artefact_bras_qui_lit_nr_leve_et_NON_APPLICABLES_seule_barriere(monkeypatch):
    def bras_curieux(obs, rng, aux):
        return [] if obs.nr else list(obs.valides[:12])
    w = mo.generer("NR_bien", RV, K_CLA + 7)
    with pytest.raises(mo.AccesLatent):
        ms.executer_monde(w, "NR_bien", RV, K_CLA + 7, ["N"], fonctions={**br.FONCTIONS, "N": bras_curieux})
    # sans NON_APPLICABLES, rien n'empêche plus d1c de tourner en NR : la table est bien la seule barrière
    monkeypatch.setattr(ms, "NON_APPLICABLES", {})
    r = ms.executer_monde(w, "NR_bien", RV, K_CLA + 7, ["d1", "d1c"])
    assert r["exclu"] or "d1c" in r["bras"]


SOURCES_PREFIXE = [
    "def f(obs, rng, aux):\n    return [x for x, p in enumerate(obs.pont) if p and p.startswith(P)]\n",
    "def f(obs, rng, aux):\n    return [x for x, p in enumerate(obs.pont) if p == 'co:R3']\n",
    "def f(obs, rng, aux):\n    return [x for x, p in enumerate(obs.pont) if p and p[:4] == 'co:R']\n",
    "def f(obs, rng, aux, k=1):\n    return [x for x, p in enumerate(obs.pont) if p == f'op:h{k}']\n",
    "def f(obs, rng, aux):\n    return [x for x, p in enumerate(obs.pont) if p and p.partition(':')[2][0] == 'R']\n",
]


def test_cla09_sain_balayage_modules_livres_et_lecture_opaque_des_etiquettes():
    assert ba.exiger_propre([ICI.parent / m for m in ba.MODULES_BRAS])
    opaque = ("def f(obs, rng, aux):\n    rare = min(obs.df, key=lambda m: (obs.df[m], m))\n"
              "    return [x for x, p in enumerate(obs.pont) if p == rare and 'eco: note' != p][:12]\n")
    assert ba.problemes(opaque) == []


@pytest.mark.parametrize("src", SOURCES_PREFIXE)
def test_cla09_artefact_balayage_refuse_les_prefixes_d_etiquette(src, tmp_path):
    pb = ba.problemes(src, "bras_artefact.py")
    assert pb and all(("préfixe" in p) for p in pb)
    f = tmp_path / "bras_artefact.py"
    f.write_text(src, encoding="utf-8")
    with pytest.raises(GardeArret):
        ba.exiger_propre([f])
