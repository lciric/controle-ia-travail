"""Essais R5 du script `ecrire_fiches_reception_v1.py` sur un arbre synthétique aux formats du fournisseur (noms des
fichiers, compagnons `.sha256`, corps `{"run_id", "manifeste_sha256", "resultat"}` des résultats) ; aucun tableau réel :
les `.npz` sont des octets quelconques, puisque le script ne les ouvre jamais. Cas sain, puis artefacts : fichier
manquant, nom inattendu, empreinte fausse, arrêt du rejeu, épisodes non résolus non déclarés, fiche déjà présente.
Les fiches écrites sont validées par les lecteurs des deux analyses (`entrees_v1.lire_fiche`, `entrees_v3.lire_fiche_v3`,
identiques aux commits cités `a8b7fdb2` et `326601cf`)."""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
SCRIPT = ICI.parent / "ecrire_fiches_reception_v1.py"
REJEU, J3, J8 = "20261102-120000-r1-rejeu-reel", "20261102-004328-r2-juge3b-reel", "20261102-005048-r2-juge8b-reel"
COMMIT = "0" * 40
ADDENDUM = "1" * 64


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _poser(p: Path, contenu: bytes | str) -> str:
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(contenu, str):
        p.write_text(contenu, encoding="utf-8")
    else:
        p.write_bytes(contenu)
    h = _sha(p)
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def _manifeste(racine: Path, run: str) -> str:
    return _poser(racine / "runs" / run / "manifeste.json", json.dumps({"run_id": run, "config": {"mode": "reel"}}))


def _resultat(racine: Path, run: str, nom: str, contenu: dict) -> str:
    sha_m = _sha(racine / "runs" / run / "manifeste.json")
    return _poser(racine / "diag" / run / f"{nom}.json",
                  json.dumps({"run_id": run, "manifeste_sha256": sha_m, "resultat": contenu}, indent=2, sort_keys=True))


def arbre_sain(racine: Path, non_resolus=(), arret=False, sans_j8=False) -> None:
    _manifeste(racine, REJEU)
    if arret:
        _resultat(racine, REJEU, "arret", {"etape": "reconstruction", "motif": "x", "verdict_fidelite": "non conforme"})
    else:
        fichiers = {}
        for n in ("activations-p3-rejeu-v1.npz", "activations-p3-rejeu-v1-maximum.npz",
                  "activations-p3-rejeu-v1-complement-hors-cout.npz"):
            fichiers[n] = _poser(racine / "donnees" / REJEU / n, os.urandom(2048) + n.encode())
        _resultat(racine, REJEU, "rejeu-activations", {
            "verdict_fidelite": "conforme", "regle_repli_appliquee": False, "textes_sha256": "ba05" + "f" * 60,
            "couches": [7, 15, 23], "contexte": "forçage par l'enseignant…", "regle_empan": "empan noté par P3",
            "modele": {"nom": "Llama-3.1-8B", "revision": "0e9e39f2"}, "fichiers": fichiers,
            "identite_sha256": "1f25adbd" + "0" * 56,
            "tokenisation": {"table_sha256": "5f6c" + "a" * 60, "episodes_non_resolus": list(non_resolus),
                             "p_r5_au_moins_90_pour_cent": True}})
    for cle, run, nom in (("juge3b", J3, "scores-juge3b-p3-v1.npz"), ("juge8b", J8, "scores-juge8b-p3-v1.npz")):
        if cle == "juge8b" and sans_j8:
            continue
        _manifeste(racine, run)
        sha = _poser(racine / "donnees" / run / nom, os.urandom(1024) + nom.encode())
        _resultat(racine, run, "juge-actions", {
            "fichier": nom, "sha256": sha, "identite_sha256": "1f25adbd" + "0" * 56, "invite_sha256": "44d48a28" + "0" * 56,
            "contexte": "énoncé de la tâche et action, sans consigne privée", "bras_principal": "specialise",
            "juge": {"modele": "Llama-3.2-3B-Instruct", "revision": "abc"}})


def lancer(racine: Path, *extra, juge8b=J8, ouvrir=True):
    cmd = [sys.executable, "-I", str(SCRIPT), "--racine", str(racine), "--rejeu", REJEU, "--juge3b", J3,
           "--juge8b", juge8b, "--qui", "essai", "--commit-versement", COMMIT, "--addendum-sha256", ADDENDUM, *extra]
    if ouvrir:
        cmd.append("--ouvrir-resultats")
    return subprocess.run(cmd, capture_output=True, text=True)


def _valider_par_les_lecteurs(racine: Path):
    """Les lecteurs des deux analyses acceptent la forme des fiches (aucune donnée lue : `scellee=False`)."""
    from controle_ia.analyse_principale_r1_r2.entrees_v1 import lire_fiche
    from controle_ia.analyse_blanche_noire.entrees_v3 import lire_fiche_v3
    fp, _ = lire_fiche(racine, "prereg/fiche-reception-principale-r1-r2-v1.json", scellee=False)
    fs, _ = lire_fiche_v3(racine, "prereg/fiche-reception-blanche-noire-v3.json", scellee=False)
    return fp, fs


def test_cas_sain_deux_fiches_validees_par_les_lecteurs(tmp_path):
    arbre_sain(tmp_path)
    r = lancer(tmp_path)
    assert r.returncode == 0, r.stderr
    fp, fs = _valider_par_les_lecteurs(tmp_path)
    assert set(fp) == {"format", "redaction", "R1", "motif_R1", "R2", "motif_R2"}
    assert fp["R1"]["moyenne"]["chemin"] == f"donnees/{REJEU}/activations-p3-rejeu-v1.npz"
    assert fp["R1"]["moyenne"]["sha256"] == _sha(tmp_path / fp["R1"]["moyenne"]["chemin"])
    assert fp["R1"]["resultat"]["chemin"] == f"diag/{REJEU}/rejeu-activations.json"
    assert fp["R2"]["juge3b"]["fichier"]["chemin"].endswith("scores-juge3b-p3-v1.npz")
    assert fp["R2"]["juge8b"]["resultat"]["chemin"] == f"diag/{J8}/juge-actions.json"
    assert fp["motif_R1"] is None and fp["motif_R2"] is None and fp["R2"]["motif_juge8b"] is None
    assert fs["format"] == "fiche-reception-blanche-noire-v3" and fs["R4"] is None
    assert fs["R1"]["manifeste"] == fp["R1"]["resultat"] and fs["R1"]["maximum"] == fp["R1"]["maximum"]
    assert fs["R1"]["pointeurs"]["fidelite_conforme"] == ["resultat", "verdict_fidelite"]
    assert fs["R1"]["pointeurs"]["regle_repli"] == ["resultat", "regle_repli_appliquee"]
    assert fs["R2"]["fichier"] == fp["R2"]["juge3b"]["fichier"]
    assert set(fs["R2"]["pointeurs"]) == {"invite_sha256", "contexte_juge", "modele"}
    red = fp["redaction"]
    assert red["commit_versement_calcul_r1_r2_reel_v1"] == COMMIT and red["addendum_v2"]["sha256"] == ADDENDUM
    # 3 manifestes + rejeu (3 npz + résultat) + 2 juges × (npz + résultat) = 11 fichiers vérifiés contre leur compagnon
    assert red["aucun_npz_ouvert"] is True and len(red["compagnons_verifies"]) == 11
    assert all(p.endswith(".json") for p in red["ce_qui_a_ete_ouvert"])
    assert red["notes"][0]["episodes_non_resolus_du_run"] == [] and red["notes"][0]["a_lazar"] is False
    # aucun nombre de résultat : les fiches ne contiennent que chemins, empreintes, pointeurs et la rédaction
    texte = (tmp_path / "prereg/fiche-reception-principale-r1-r2-v1.json").read_text()
    assert "p_r5" not in texte and "fideles" not in texte
    assert "sans consigne privée" in r.stdout      # contexte du juge affiché pour la règle d'équité, non écrit


def test_sans_ouvrir_aucun_json_lu_et_fiches_identiques_sur_les_cles(tmp_path):
    arbre_sain(tmp_path)
    r = lancer(tmp_path, ouvrir=False)
    assert r.returncode == 0, r.stderr
    fp, fs = _valider_par_les_lecteurs(tmp_path)
    assert fp["redaction"]["ce_qui_a_ete_ouvert"] == ["aucun fichier ouvert : noms et empreintes seulement"]
    assert fp["redaction"]["notes"] == []


def test_juge_8b_absent_motif_ferme(tmp_path):
    arbre_sain(tmp_path, sans_j8=True)
    r = lancer(tmp_path, juge8b="absent")
    assert r.returncode == 0, r.stderr
    fp, fs = _valider_par_les_lecteurs(tmp_path)
    assert fp["R2"]["juge8b"] is None and fp["R2"]["motif_juge8b"] == "non_livre"


def test_artefact_fichier_manquant(tmp_path):
    arbre_sain(tmp_path)
    p = tmp_path / "donnees" / REJEU / "activations-p3-rejeu-v1-maximum.npz"
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    r = lancer(tmp_path)
    assert r.returncode == 2 and "absent" in r.stderr
    assert not (tmp_path / "prereg").exists()


def test_artefact_nom_inattendu(tmp_path):
    arbre_sain(tmp_path)
    _poser(tmp_path / "donnees" / REJEU / "activations-p3-rejeu-v2.npz", b"x")
    r = lancer(tmp_path)
    assert r.returncode == 2 and "inattendu" in r.stderr


def test_artefact_empreinte_fausse(tmp_path):
    arbre_sain(tmp_path)
    p = tmp_path / "donnees" / J3 / "scores-juge3b-p3-v1.npz"
    p.write_bytes(p.read_bytes() + b"!")
    r = lancer(tmp_path)
    assert r.returncode == 2 and "≠ compagnon" in r.stderr


def test_artefact_empreinte_declaree_par_le_fournisseur_differente(tmp_path):
    arbre_sain(tmp_path)
    p = tmp_path / "diag" / REJEU / "rejeu-activations.json"
    d = json.loads(p.read_text())
    d["resultat"]["fichiers"]["activations-p3-rejeu-v1.npz"] = "0" * 64
    _poser(p, json.dumps(d))
    r = lancer(tmp_path)
    assert r.returncode == 2 and "déclarée par le fournisseur" in r.stderr


def test_rejeu_arrete_motif_ferme_et_refus_sans_ouverture(tmp_path):
    arbre_sain(tmp_path, arret=True)
    r = lancer(tmp_path, ouvrir=False)
    assert r.returncode == 2 and "--ouvrir-resultats" in r.stderr
    r = lancer(tmp_path)
    assert r.returncode == 0, r.stderr
    fp, fs = _valider_par_les_lecteurs(tmp_path)
    assert fp["R1"] is None and fp["motif_R1"] == "rejeu_non_conforme"
    assert fs["R1"] is None and fs["motif_R1"] == "rejeu_non_conforme"
    assert fp["redaction"]["notes"][0]["arret"]["chemin"] == f"diag/{REJEU}/arret.json"


def test_artefact_resultat_et_arret_tous_deux_presents(tmp_path):
    arbre_sain(tmp_path)
    _poser(tmp_path / "diag" / REJEU / "arret.json", json.dumps({"resultat": {"verdict_fidelite": "echec"}}))
    r = lancer(tmp_path)
    assert r.returncode == 2 and "exactement un" in r.stderr


def test_garde_E19_episodes_non_resolus(tmp_path):
    arbre_sain(tmp_path, non_resolus=["honnete/2602.00987v1/e0"])
    r = lancer(tmp_path)
    assert r.returncode == 2 and "E19" in r.stderr and not (tmp_path / "prereg").exists()
    r = lancer(tmp_path, "--episodes-non-inversibles-declares", "honnete/2602.00987v1/e0")
    assert r.returncode == 0, r.stderr
    fp, _ = _valider_par_les_lecteurs(tmp_path)
    assert fp["redaction"]["notes"][0]["a_lazar"] is True
    assert fp["redaction"]["notes"][0]["episodes_non_resolus_du_run"] == ["honnete/2602.00987v1/e0"]


def test_fiche_existante_jamais_ecrasee(tmp_path):
    arbre_sain(tmp_path)
    assert lancer(tmp_path).returncode == 0
    avant = _sha(tmp_path / "prereg/fiche-reception-principale-r1-r2-v1.json")
    r = lancer(tmp_path)
    assert r.returncode == 2 and "R12" in r.stderr
    assert _sha(tmp_path / "prereg/fiche-reception-principale-r1-r2-v1.json") == avant


def test_parametres_hors_de_forme(tmp_path):
    arbre_sain(tmp_path)
    r = subprocess.run([sys.executable, "-I", str(SCRIPT), "--racine", str(tmp_path), "--rejeu", REJEU, "--juge3b", J3,
                        "--juge8b", J8, "--qui", "x", "--commit-versement", "abc", "--addendum-sha256", ADDENDUM],
                       capture_output=True, text=True)
    assert r.returncode == 2 and "hors de forme" in r.stderr
    r = subprocess.run([sys.executable, "-I", str(SCRIPT), "--racine", str(tmp_path), "--rejeu", "pas-un-run",
                        "--juge3b", J3, "--juge8b", J8, "--qui", "x", "--commit-versement", COMMIT,
                        "--addendum-sha256", ADDENDUM], capture_output=True, text=True)
    assert r.returncode == 2 and "format AAAAMMJJ" in r.stderr
