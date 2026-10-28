"""Essais (R5) des deux correctifs proposés pour l'étape 1 v10 (brouillon, sous-agent conv-audit, 25-26 octobre 2026).

1. BC5-01 : `charger_traits` exige l'égalité des identifiants (traits = banque servie) et ne sert un fichier `.npz`
   seul que s'il est décrit par le manifeste de son dossier, à l'empreinte de la banque de la course.
   Cas de la contre-lecture de la banque v5 (`banque/contre-lectures/banque-v5-cl1/essais/c4/`, traits factices
   aléatoires) : `sain_176_ids_v5.npz` accepté ; `artefact_espace_v3_200.npz` et `artefact_v5_plus_24_hors_banque.npz`
   refusés. Variables : ESSAI_V10_BANQUE_V5 (chemin de `banque-confrontation-v5.json`), ESSAI_V10_C4 (dossier c4) ;
   sans elles, ces essais sont sautés (et le disent).
2. R-441 : l'amorçage relance une fois au plafond de relance quand la réponse finit au plafond sans texte ; un second
   échec reste `AMORCAGE_INVALIDE` (aucun repli) ; une réponse saine ne relance pas.
"""
import hashlib
import json
import os
import pathlib
import shutil
import sys

import numpy as np
import pytest

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))

from essaim_m3.noyau import appels, boucle, cli, taches  # noqa: E402
from essaim_m3.simulateur import appelants_simules  # noqa: E402

cv = appels.cv
emp = lambda f: hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()  # noqa: E731


def _dossier_avec_manifeste(dossier, npz, banque_json, nom="couche16-dernier"):
    dossier.mkdir(parents=True)
    f = dossier / f"traits-{nom}.npz"
    shutil.copyfile(npz, f)
    f.with_name(f.name + ".sha256").write_text(f"{emp(f)}  {f.name}\n", encoding="utf-8")
    d = np.load(f, allow_pickle=False)
    m = {"sha256_banque": emp(banque_json), "n_taches": int(d["X"].shape[0]), "modele": "essai", "revision": "0" * 40,
         "max_jetons": 16384, "n_tronquees": 0, "factice": False,
         "fichiers": {nom: {"chemin": str(f), "sha256": emp(f), "forme": list(d["X"].shape)}}}
    fm = dossier / "manifeste-traits.json"
    fm.write_text(json.dumps(m), encoding="utf-8")
    fm.with_name(fm.name + ".sha256").write_text(f"{emp(fm)}  {fm.name}\n", encoding="utf-8")
    return dossier, f


BANQUE_V5 = os.environ.get("ESSAI_V10_BANQUE_V5")
C4 = os.environ.get("ESSAI_V10_C4")
sans_pieces = pytest.mark.skipif(not (BANQUE_V5 and C4), reason="ESSAI_V10_BANQUE_V5 ou ESSAI_V10_C4 absent : essais c4 sautés")


@sans_pieces
def test_bc5_01_cas_c4_sain_accepte_artefacts_refuses(tmp_path):
    banque_json = pathlib.Path(BANQUE_V5)
    banque = json.loads(banque_json.read_text(encoding="utf-8"))
    d, f = _dossier_avec_manifeste(tmp_path / "sain", pathlib.Path(C4) / "sain_176_ids_v5.npz", banque_json)
    vues, _ = cli.charger_traits(d, banque_json, banque)
    assert len(vues["couche16-dernier"]) == 176
    seul, _ = cli.charger_traits(f, banque_json, banque)  # fichier seul, décrit par son manifeste : accepté
    assert len(seul) == 176
    for nom, motif in (("artefact_espace_v3_200.npz", "sans traits"), ("artefact_v5_plus_24_hors_banque.npz", "hors de la banque")):
        d, f = _dossier_avec_manifeste(tmp_path / nom, pathlib.Path(C4) / nom, banque_json)
        for chemin in (d, f):
            with pytest.raises(ValueError, match=motif):
                cli.charger_traits(chemin, banque_json, banque)


@sans_pieces
def test_bc5_01_fichier_npz_sans_manifeste_ou_autre_banque_refuse(tmp_path):
    banque_json = pathlib.Path(BANQUE_V5)
    banque = json.loads(banque_json.read_text(encoding="utf-8"))
    nu = tmp_path / "nu" / "sain.npz"
    nu.parent.mkdir()
    shutil.copyfile(pathlib.Path(C4) / "sain_176_ids_v5.npz", nu)
    with pytest.raises(ValueError, match="aucun manifeste"):
        cli.charger_traits(nu, banque_json, banque)
    autre = tmp_path / "autre-banque.json"
    autre.write_text(banque_json.read_text(encoding="utf-8") + " ", encoding="utf-8")
    d, f = _dossier_avec_manifeste(tmp_path / "autre", pathlib.Path(C4) / "sain_176_ids_v5.npz", autre)
    with pytest.raises(ValueError, match="pas celle de la course"):
        cli.charger_traits(f, banque_json, banque)


def _noyau_amorcage(tmp_path, reponses_initiales):
    """Noyau de simulation, une lignée Gemini ; les premiers appels rendent `reponses_initiales`, puis le simulateur."""
    ss = np.random.SeedSequence(7)
    r1, r2 = (np.random.default_rng(s) for s in ss.spawn(2))
    banque = taches.banque_simulation(r1, 8, 8)
    doubles, _ = appelants_simules(r2)
    simule = doubles["gemini"]
    vus = []
    file_attente = list(reponses_initiales)

    def gemini(modele_id, prompt, max_tokens):
        vus.append(int(max_tokens))
        if file_attente:
            return file_attente.pop(0)
        return simule(modele_id, prompt, max_tokens)

    doubles = dict(doubles, gemini=gemini)
    n = boucle.Noyau(tmp_path / "run", "mission de test", banque, {"appels_max": 40, "usd_max": 5.0, "temps_max_s": 60},
                     10.0, 1, appelants=doubles, especes_amorcage=["GEMINI_ARGON"], entropie=7)
    return n, vus


def _vide(ident="gemini-4-argon"):
    return cv.Reponse(texte="", modele_servi=ident, fin="MAX_TOKENS", usage={"entree": 5, "sortie": 100}, types_blocs=["thought"])


def test_r441_amorcage_vide_relance_une_fois_au_plafond_de_relance(tmp_path):
    n, vus = _noyau_amorcage(tmp_path, [_vide()])
    am = n.amorcer()
    m = appels.modele_de("GEMINI_ARGON")
    assert am["gemini-argon"]["statut"] == "ORGANISME_VALIDE"
    assert vus == [int(m["max"]), int(m["max_relance"])]
    lignes = [json.loads(x) for x in pathlib.Path(am["gemini-argon"]["journal"]).read_text(encoding="utf-8").splitlines()]
    assert [x["role"] for x in lignes] == ["amorcage", "amorcage-relance"] and lignes[0]["statut"] == "VIDE"


def test_r441_amorcage_vide_deux_fois_reste_invalide_sans_autre_reprise(tmp_path):
    n, vus = _noyau_amorcage(tmp_path, [_vide(), _vide()])
    am = n.amorcer()
    assert am["gemini-argon"]["statut"] == "AMORCAGE_INVALIDE" and "gemini-argon" not in n.lignees
    assert len(vus) == 2 and any("VIDE" in p for p in am["gemini-argon"]["problemes"])


def test_r441_amorcage_sain_ne_relance_pas(tmp_path):
    n, vus = _noyau_amorcage(tmp_path, [])
    am = n.amorcer()
    assert am["gemini-argon"]["statut"] == "ORGANISME_VALIDE" and len(vus) == 1
