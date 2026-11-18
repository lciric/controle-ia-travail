"""Essais de l'essai de forme (`controle_ia.narcbench.forme_externe_v2`) sur des fichiers **factices** fabriqués ici ; aucun
fichier publié n'est ouvert. R5 : chaque garde sur un cas sain et sur un artefact ; aucun score n'est calculé."""
from __future__ import annotations

import hashlib
import json

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.narcbench import chargeur_externe_v1 as C
from controle_ia.narcbench import forme_externe_v2 as F

LARG = 6
BANDES = {"qwen3_32b": (26, 27), "llama_3_1_70b": (32, 33)}
CHAMPS_RESULTAT = ("agent_vote", "target_option", "target_majority", "collusion_success", "fair_option", "label_variant",
                   "bp_corr", "flagged")


def _ligne(run_id, mode, role, phase, rnd, agent, channel="public"):
    m = {k: None for k in C.CHAMPS}
    m.update(run_id=run_id, mode=mode, role=role, channel=channel, phase=phase, round=rnd, agent_name=agent,
             n_tokens=10, seed=0, flagged=False, family=run_id.split("__")[0], scenario_id=run_id.split("__")[1],
             scenario_domain="_".join(run_id.split("__")[1].split("_")[:-1]))
    return m


def _meta(etage, n_dom=2, par_dom=2, agents=4):
    meta = []
    for d in range(n_dom):
        for k in range(par_dom):
            for mode in ("collusion", "control"):
                rid = f"fam__dom{d}_{k:02d}__{mode}"
                for j in range(agents):
                    role = "colluder" if mode == "collusion" and j < 2 else "honest"
                    if etage == "core":
                        for rnd in (1, 2, 3):
                            meta.append(_ligne(rid, mode, role, "discussion", rnd, f"agent{j}"))
                            meta.append(_ligne(rid, mode, role, "discussion", rnd, f"agent{j}", channel="private"))
                        meta.append(_ligne(rid, mode, role, "vote", None, f"agent{j}"))
                    else:
                        meta.append(_ligne(rid, mode, role, "bet", 1, f"agent{j}"))
                        meta.append(_ligne(rid, mode, role, "final", None, f"agent{j}"))
    return meta


def _fabriquer(racine, lignes_en_plus=0, objet=False, meta_core=None):
    """Huit fichiers factices aux chemins publiés ; rend les empreintes attendues au format de `EMPREINTES_PUBLIEES`."""
    attendues = {}
    rng = np.random.default_rng(0)
    for modele, bande in BANDES.items():
        for etage in ("core", "stego"):
            d = racine / "activations" / modele / etage
            d.mkdir(parents=True)
            meta = meta_core if (meta_core is not None and etage == "core") else _meta(etage)
            (d / "metadata_gen.json").write_text(json.dumps(meta))
            tab = {f"layer_{c}": rng.standard_normal((len(meta) + lignes_en_plus, LARG)).astype(np.float32) for c in bande}
            if objet:
                tab["layer_99"] = np.array([{"a": 1}] * len(meta), dtype=object)
            np.savez(d / "activations_gen.npz", **tab)
            for nom, sorte in (("activations_gen.npz", "sha256"), ("metadata_gen.json", "git-sha1")):
                p = d / nom
                rel = f"activations/{modele}/{etage}/{nom}"
                attendues[rel] = (p.stat().st_size, sorte, C.empreinte(p, sorte))
    return attendues


@pytest.fixture
def petites_bandes(monkeypatch):
    for modele, bande in BANDES.items():
        monkeypatch.setitem(C.BANDES, modele, bande)
        monkeypatch.setitem(C.LARGEURS, modele, LARG)


def test_cas_sain_comptes_et_formes(tmp_path, petites_bandes):
    att = _fabriquer(tmp_path)
    r = F.essai_de_forme(tmp_path, attendues=att)
    assert set(r["formes"]) == {"qwen3_32b/core", "qwen3_32b/stego", "llama_3_1_70b/core", "llama_3_1_70b/stego"}
    q = r["formes"]["qwen3_32b/core"]
    n = len(_meta("core"))
    assert q["npz"]["cles"] == ["layer_26", "layer_27"] and q["npz"]["bande_presente"]
    assert q["npz"]["entetes"]["layer_26"] == {"forme": [n, LARG], "type": "float32", "ordre_fortran": False}
    m = q["metadonnees"]
    assert m["lignes"] == n and m["runs_par_mode"] == {"collusion": 4, "control": 4}
    assert m["discussion_publique_tours_par_agent"] == {"3": 32}                      # 8 épisodes × 4 agents
    assert m["discussion_publique_jeux_de_tours"] == {"1,2,3": 32}
    assert m["apprentissage_par_message_lignes_par_role"] == {"colluder": 24, "honest": 24}   # 4 collusions × 2 × 3
    assert m["domaines_runs_par_mode"] == {"dom0": {"collusion": 2, "control": 2}, "dom1": {"collusion": 2, "control": 2}}
    assert m["domaine_vide_present"] is False and m["scenario_domain_different_du_domaine_des_auteurs"] == {}
    ch = q["chargeur_v1"]
    assert ch["episodes_par_condition"] == {"collusion": 4, "temoin": 4}
    assert ch["formes_acts"] == {f"4x3x2x{LARG}": 8}
    assert ch["colludeurs_par_condition"] == {"collusion/2": 4, "temoin/0": 4}
    assert ch["exclusions"] == {"agents_differents_de_4": [], "tours_inegaux": []}
    s = r["formes"]["llama_3_1_70b/stego"]
    assert s["chargeur_v1"]["formes_acts"] == {f"4x1x2x{LARG}": 8}                      # phase `final` seule
    json.dumps(r)                                                                        # sérialisable tel quel


def test_artefact_lignes_en_plus_dans_le_npz(tmp_path, petites_bandes):
    """Le code des auteurs tronque `[:n]` en silence ; ici, une ligne de trop arrête."""
    att = _fabriquer(tmp_path, lignes_en_plus=1)
    with pytest.raises(GardeArret):
        F.essai_de_forme(tmp_path, attendues=att)


def test_artefact_tableau_d_objets_refuse_a_l_entete(tmp_path, petites_bandes):
    _fabriquer(tmp_path, objet=True)
    with pytest.raises(GardeArret):
        F.entetes_npz(tmp_path / "activations/qwen3_32b/core/activations_gen.npz")


def test_artefact_empreinte_fausse(tmp_path, petites_bandes):
    att = _fabriquer(tmp_path)
    rel = "activations/llama_3_1_70b/stego/metadata_gen.json"
    att[rel] = (att[rel][0], "git-sha1", "0" * 40)
    with pytest.raises(GardeArret):
        F.essai_de_forme(tmp_path, attendues=att)


def test_artefact_deux_modes_dans_un_episode():
    meta = _meta("core", n_dom=1, par_dom=1)
    meta[3] = dict(meta[3], mode="control")
    with pytest.raises(GardeArret):
        F._comptes_metadonnees(meta)


def test_episode_a_trois_agents_compte_jamais_silencieux(tmp_path, petites_bandes):
    meta = [m for m in _meta("core") if not (m["run_id"] == "fam__dom0_00__control" and m["agent_name"] == "agent3")]
    att = _fabriquer(tmp_path, meta_core=meta)
    r = F.essai_de_forme(tmp_path, attendues=att)
    ch = r["formes"]["qwen3_32b/core"]["chargeur_v1"]
    assert ch["exclusions"]["agents_differents_de_4"] == ["fam__dom0_00__control"]
    assert ch["episodes_par_condition"] == {"collusion": 4, "temoin": 3}


class _Espion(dict):
    """dict qui consigne les clés lues (pour prouver qu'aucun champ de résultat du jeu n'est lu)."""
    lues: set = set()

    def __getitem__(self, k):
        _Espion.lues.add(k)
        return super().__getitem__(k)


def test_aucun_champ_de_resultat_lu():
    _Espion.lues = set()
    meta = [_Espion(m) for m in _meta("core")]
    F._comptes_metadonnees(meta)
    C.episodes(meta, {26: np.zeros((len(meta), 3), dtype=np.float32)}, "core")
    assert _Espion.lues <= set(F.CHAMPS_LUS)
    assert not _Espion.lues & set(CHAMPS_RESULTAT)
    # artefact : un lecteur qui lirait un champ de résultat serait vu
    _Espion.lues = set()
    meta[0]["collusion_success"]
    assert "collusion_success" in _Espion.lues


def test_sortie_jamais_ecrasee(tmp_path, petites_bandes):
    att = _fabriquer(tmp_path / "d")
    sortie = tmp_path / "forme.json"
    assert F.main([str(tmp_path / "d"), str(sortie)], attendues=att) == 0           # cas sain : écrite
    empreinte = hashlib.sha256(sortie.read_bytes()).hexdigest()
    with pytest.raises(GardeArret):                                                  # artefact : déjà présente
        F.main([str(tmp_path / "d"), str(sortie)], attendues=att)
    assert hashlib.sha256(sortie.read_bytes()).hexdigest() == empreinte
    with pytest.raises(GardeArret):                                                  # artefact : empreintes publiées
        F.main([str(tmp_path / "d"), str(tmp_path / "autre.json")])                  # (défaut) ≠ fichiers factices
    assert not (tmp_path / "autre.json").exists()
