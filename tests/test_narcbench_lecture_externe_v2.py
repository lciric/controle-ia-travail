"""Essais de la commande de lecture du bras externe v2 (`controle_ia.narcbench.lecture_externe_v2`), dans un dépôt git **jetable**
et sur des fichiers **factices** ; aucun fichier publié n'est ouvert. R5 : chaque garde sur un cas sain et sur un artefact.

Seul raccourci, déclaré : la conformité du texte court au gabarit des préenregistrements (`prereg.exiger_prereg_scelle`, éprouvée
par ses propres essais) est remplacée ici par la seule vérification du sceau (`scellement.verifier`)."""
from __future__ import annotations

import json
import subprocess

import numpy as np
import pytest

from controle_ia import prereg, scellement
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import verifier_resultat
from controle_ia.narcbench import chargeur_externe_v1 as C
from controle_ia.narcbench import lecture_externe_v2 as L
from controle_ia.t07.registre_v1 import RefusRegistre

LARG = 6
BANDES = {"qwen3_32b": (26, 27), "llama_3_1_70b": (32, 33)}
ENTROPIE = 271828182845904523536


def _ligne(rid, mode, role, canal, phase, rnd, agent):
    m = {k: None for k in C.CHAMPS}
    m.update(run_id=rid, mode=mode, role=role, channel=canal, phase=phase, round=rnd, agent_name=agent)
    return m


def _meta(etage):
    meta = []
    if etage == "core":
        runs = [(f"fam__dom{d}_{k:02d}__{mode}", mode) for d in range(3) for k in range(2) for mode in ("collusion", "control")]
        tours, final = (1, 2, 3), 4
    else:
        runs = [(f"bj__shoe{k:02d}__{mode}", mode) for k in range(6) for mode in ("collusion", "control")]
        tours, final = (1, 2), 8
    for rid, mode in runs:
        roles = {f"agent_{j}": ("colluder" if mode == "collusion" and j in (0, 3) else "honest") for j in range(4)}
        for a, r in roles.items():
            if r == "colluder":
                meta.append(_ligne(rid, mode, r, "private", "private", 0, a))
        for t in tours:
            for a, r in roles.items():
                meta.append(_ligne(rid, mode, r, "public", "discussion", t, a))
        for a, r in roles.items():
            meta.append(_ligne(rid, mode, r, "public", "final", final, a))
    return meta


def _donnees(racine, rng):
    attendues = {}
    for modele, bande in BANDES.items():
        for etage in ("core", "stego"):
            d = racine / "activations" / modele / etage
            d.mkdir(parents=True)
            meta = _meta(etage)
            (d / "metadata_gen.json").write_text(json.dumps(meta))
            tab = {}
            for c in bande:
                A = rng.standard_normal((len(meta), LARG))
                A[[i for i, m in enumerate(meta) if m["role"] == "colluder"], 0] += 3.0
                tab[f"layer_{c}"] = A.astype(np.float32)
            np.savez(d / "activations_gen.npz", **tab)
            for nom, sorte in (("activations_gen.npz", "sha256"), ("metadata_gen.json", "git-sha1")):
                p = d / nom
                attendues[f"activations/{modele}/{etage}/{nom}"] = (p.stat().st_size, sorte, C.empreinte(p, sorte))
    return attendues


def _git(depot, *args):
    subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True, text=True)


def _depot(tmp, date="2026-01-01T00:00:00Z", cle=L.CLE_SCELLEMENT_EXTERNE, cite="prereg/texte-court.md", deux=False,
           entropie=ENTROPIE):
    depot = tmp / "depot"
    (depot / "prereg").mkdir(parents=True)
    (depot / "registres").mkdir()
    texte = depot / "prereg" / "texte-court.md"
    texte.write_text(f"# Texte court factice\n\nEntropie : {entropie}\n", encoding="utf-8")
    sha = scellement.sceller(texte)
    ligne = f"| {cle} | {date} | {cite} | {sha} |\n"
    (depot / "registres" / "scellements-v1.md").write_text("# Registre factice\n\n" + ligne * (2 if deux else 1),
                                                          encoding="utf-8")
    _git(depot, "init", "-q")
    _git(depot, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "add", "-A")
    _git(depot, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "commit", "-q", "-m", "jetable")
    return depot


def _args(depot, donnees, run_id="20261118-170000-narc-externe-essai", couches="qwen3_32b=26;llama_3_1_70b=33",
          augmentation="papier", entropie=ENTROPIE):
    return ["--depot", str(depot), "--registre", "registres/scellements-v1.md", "--texte", "prereg/texte-court.md",
            "--donnees", str(donnees), "--run-id", run_id, "--entropie", str(entropie), "--augmentation", augmentation,
            "--couches-familles", couches]


@pytest.fixture
def petites_bandes(monkeypatch):
    for modele, bande in BANDES.items():
        monkeypatch.setitem(C.BANDES, modele, bande)
        monkeypatch.setitem(C.LARGEURS, modele, LARG)
    monkeypatch.setattr(prereg, "exiger_prereg_scelle", scellement.verifier)


def test_lecture_de_bout_en_bout_puis_jamais_reecrite(tmp_path, petites_bandes):
    att = _donnees(tmp_path / "donnees", np.random.default_rng(1))
    depot = _depot(tmp_path)
    assert L.main(_args(depot, tmp_path / "donnees"), attendues=att) == 0
    run = "20261118-170000-narc-externe-essai"
    res = depot / "diag" / run / f"{L.NOM_RESULTAT}.json"
    corps = verifier_resultat(depot, res)                                  # résultat scellé et rattaché au manifeste
    r = corps["resultat"]
    assert set(r["modeles"]) == set(C.MODELES) and r["marque"] == "diagnostic, jamais en production (N-026)"
    q = r["modeles"]["qwen3_32b"]
    assert q["garde_reproduction"]["etat"] in ("éprouvée", "non éprouvé") and q["reproduction"]["graines"] == list(range(10))
    assert set(q["nos_familles"]) == {"26"} and set(r["modeles"]["llama_3_1_70b"]["nos_familles"]) == {"33"}
    m = json.loads((depot / "runs" / run / "manifeste.json").read_text(encoding="utf-8"))
    assert m["config"]["augmentation"] == "papier" and m["preenregistrement"]["chemin"] == "prereg/texte-court.md"
    assert m["graines"]["qwen3_32b/familles/c26/lineaire/plancher"]["entropie"] == str(ENTROPIE)   # R9
    assert m["config"]["versions_supplementaires"]["scikit-learn"] == "1.9.1"
    empreinte = scellement.empreinte(res)
    with pytest.raises(GardeArret):                                        # artefact : même run (R12, dépôt sale)
        L.main(_args(depot, tmp_path / "donnees"), attendues=att)
    assert scellement.empreinte(res) == empreinte


@pytest.mark.parametrize("cas", ["cle_absente", "deux_lignes", "posterieure", "autre_fichier", "entropie_absente",
                                 "texte_modifie"])
def test_refus_du_registre_rien_d_ecrit(tmp_path, petites_bandes, cas):
    att = _donnees(tmp_path / "donnees", np.random.default_rng(2))
    kw = {"cle_absente": {"cle": "SCELLEMENT-NARC-AUTRE"}, "deux_lignes": {"deux": True},
          "posterieure": {"date": "2099-01-01T00:00:00Z"}, "autre_fichier": {"cite": "prereg/autre.md"},
          "entropie_absente": {"entropie": 12345}, "texte_modifie": {}}[cas]
    depot = _depot(tmp_path, **kw)
    if cas == "texte_modifie":
        (depot / "prereg" / "texte-court.md").write_text(f"modifié après scellement {ENTROPIE}\n", encoding="utf-8")
    assert L.main(_args(depot, tmp_path / "donnees"), attendues=att) == 2
    assert not (depot / "runs").exists() and not (depot / "diag").exists()


def test_garde_ouverture_cas_sain_et_instant_egal(tmp_path):
    depot = _depot(tmp_path)
    t = L.lire_ligne(depot / "registres" / "scellements-v1.md")[0]
    g = L.garde_ouverture_externe(depot / "registres" / "scellements-v1.md", depot, "prereg/texte-court.md", t + 1, ENTROPIE)
    assert g["cle"] == L.CLE_SCELLEMENT_EXTERNE
    with pytest.raises(RefusRegistre):                                     # strictement antérieure : l'égalité refuse
        L.garde_ouverture_externe(depot / "registres" / "scellements-v1.md", depot, "prereg/texte-court.md", t, ENTROPIE)
    with pytest.raises(RefusRegistre):
        L.lire_ligne(tmp_path / "absent.md")


def test_donnees_fausses_arretent_avant_tout_ecrit(tmp_path, petites_bandes):
    att = _donnees(tmp_path / "donnees", np.random.default_rng(3))
    rel = "activations/qwen3_32b/core/activations_gen.npz"
    att[rel] = (att[rel][0], "sha256", "0" * 64)
    depot = _depot(tmp_path)
    with pytest.raises(GardeArret):
        L.main(_args(depot, tmp_path / "donnees"), attendues=att)
    assert not (depot / "runs").exists()


def test_couches_de_nos_familles(petites_bandes):
    assert L.couches_familles("bande") == BANDES
    assert L.couches_familles("qwen3_32b=26;llama_3_1_70b=32+33") == {"qwen3_32b": (26,), "llama_3_1_70b": (32, 33)}
    for faux in ("qwen3_32b=26", "qwen3_32b=99;llama_3_1_70b=32", "qwen3_32b=26+26;llama_3_1_70b=32",
                 "gpt_oss_20b=10;qwen3_32b=26", "qwen3_32b=;llama_3_1_70b=32", "qwen3_32b=26;qwen3_32b=27"):
        with pytest.raises(GardeArret):
            L.couches_familles(faux)
    assert len(L.taches_graines({"qwen3_32b": (26,), "llama_3_1_70b": (32, 33)})) == 3 * 3 * 4


def test_arguments_exiges(tmp_path):
    base = _args(tmp_path, tmp_path)
    sans_aug = [x for i, x in enumerate(base) if x != "--augmentation" and (i == 0 or base[i - 1] != "--augmentation")]
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(sans_aug)                                 # E2 : aucun défaut
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(_args(tmp_path, tmp_path, augmentation="aucune"))
    assert L.analyseur().parse_args(base).augmentation == "papier"
