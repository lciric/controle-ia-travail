"""Essais de la configuration de course v2 du lanceur de l'étape de discrétion du bras A, version 2.

La v2 remplace le marqueur de la v1 par l'empreinte du texte scellé du bras A (`prereg/T0.7-organismes-discrets-v-a-v2.md`,
`main`, commit `68b2aa636`), et fixe deux valeurs que le texte fixe : la statistique de l'agrégateur (ligne 933, 6.10) et
les cinq réglages de la lecture (ligne 925, 6.10). Cinq valeurs restent vides (pièce compagnon `…-course-v2-valeurs-a-
remplir.md`) : le lanceur la refuse tant qu'elles manquent. L'empreinte du texte est vérifiée contre le fichier réel :
dans l'arbre s'il y est, sinon au commit scellé, lu par git ; s'il est introuvable, l'essai échoue (pas de repli).
Chaque garde a un cas sain et un artefact (R5).

    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider \\
        tests/test_bras_a_v2_habilite_config_lanceur_discretion_v2_course_v2.py
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v11 as A
from controle_ia.organismes_discrets.bras_a_v2_habilite import moniteurs_langue_v3 as ML
from controle_ia.organismes_discrets.bras_a_v2_habilite_lanceur import lanceur_discretion_v2 as L
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "docs/notes/bras-a-moniteurs-v1"
CONFIG_V1 = DOSSIER / "config-lanceur-discretion-bras-a-v2-course-v1.json"
CONFIG_V2 = DOSSIER / "config-lanceur-discretion-bras-a-v2-course-v2.json"
NOTE_V2 = DOSSIER / "config-lanceur-discretion-bras-a-v2-course-v2-valeurs-a-remplir.md"
TEXTE = "prereg/T0.7-organismes-discrets-v-a-v2.md"
SHA_TEXTE = "b4fbfb4e6cddfdc4775119a3e42a61045460ce8cee18a341834155ef1367a0cd"
COMMIT_DU_TEXTE = "68b2aa636"
RANGS = "donnees/bras-a-v2-discretion/rangs-par-unite"
LECTURE = {"max_nouveaux": 400, "temperature": 1.0, "regle_balise_absente": "imposer", "masse_min": 0.5, "lot": 8}
A_REMPLIR = ["registre_des_accords_fige", "rejeu", "configuration_du_bras", "taches", "fins_moniteur_boite_noire"]
FACTICES = {
    "registre_des_accords_fige": {"chemin": "registres/go-fige-essai.md", "sha256": "f" * 64, "commit": "c" * 40},
    "rejeu": {"chemin": "essai/rejeu.jsonl", "sha256": "1" * 64},
    "configuration_du_bras": {"chemin": "essai/bras.json", "sha256": "2" * 64},
    "taches": {"chemin": "essai/taches.json", "sha256": "3" * 64},
    "fins_moniteur_boite_noire": [1, 2],
}


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _v2() -> dict:
    return json.loads(CONFIG_V2.read_text(encoding="utf-8"))


def octets_du_texte_reel() -> bytes:
    """Le texte scellé du bras A tel qu'il est : dans l'arbre, ou au commit scellé de `main`, lu par git. Introuvable :
    l'essai échoue."""
    chemin = RACINE / TEXTE
    if chemin.is_file():
        return chemin.read_bytes()
    r = subprocess.run(["git", "-C", str(RACINE), "show", f"{COMMIT_DU_TEXTE}:{TEXTE}"], capture_output=True)
    if r.returncode != 0:
        pytest.fail(f"texte scellé introuvable (ni dans l'arbre, ni au commit {COMMIT_DU_TEXTE} : récupérer `main`)")
    return r.stdout


def _copie_scellee(tmp_path: Path, cfg: dict, nom: str) -> Path:
    p = tmp_path / nom
    p.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(p)
    return p


def test_v2_scellee_et_trois_valeurs_changees_depuis_la_v1():
    assert Path(str(CONFIG_V2) + ".sha256").read_text(encoding="utf-8").split()[0] == _sha(CONFIG_V2.read_bytes())
    c, v1 = _v2(), json.loads(CONFIG_V1.read_text(encoding="utf-8"))
    assert tuple(c) == L.CLES_CONFIG
    assert {k for k in c if c[k] != v1[k]} == {"texte_scelle", "statistique_agregateur", "lecture"}
    assert "EMPREINTE_TEXTE_V2_BRAS_A" not in CONFIG_V2.read_text(encoding="utf-8")
    assert c["texte_scelle"] == {"chemin": TEXTE, "sha256": SHA_TEXTE}
    assert c["dossiers"]["rangs"] == RANGS and c["dossiers"] == v1["dossiers"] and c["modules"] == v1["modules"]


def test_valeurs_fixees_par_le_texte():
    c = _v2()
    assert c["statistique_agregateur"] == "moyenne" and c["statistique_agregateur"] in A.STATISTIQUES_EPISODE
    assert c["lecture"] == LECTURE and ML.exiger_reglages(c["lecture"]) == LECTURE
    with pytest.raises(GardeArret, match="réglages de la lecture"):                          # artefact
        ML.exiger_reglages({**LECTURE, "lot": 0})


def test_empreinte_du_texte_contre_le_fichier_reel(tmp_path):
    """Cas sain : le texte réel, posé avec son compagnon, passe la garde d'empreinte du lanceur à l'empreinte de la
    configuration. Artefact : un octet changé, compagnon refait : refusé par la même garde."""
    octets = octets_du_texte_reel()
    assert _sha(octets) == _v2()["texte_scelle"]["sha256"] == SHA_TEXTE
    sain = tmp_path / "sain" / Path(TEXTE).name
    sain.parent.mkdir()
    sain.write_bytes(octets)
    sceller(sain)
    assert L._scelle(sain, _v2()["texte_scelle"]["sha256"]) == SHA_TEXTE
    artefact = tmp_path / "artefact" / Path(TEXTE).name
    artefact.parent.mkdir()
    artefact.write_bytes(octets + b"\n")
    sceller(artefact)
    with pytest.raises(GardeArret, match="celle attendue"):
        L._scelle(artefact, _v2()["texte_scelle"]["sha256"])


def test_v2_refusee_tant_que_cinq_valeurs_manquent():
    assert [k for k, v in _v2().items() if v is None] == A_REMPLIR
    with pytest.raises(GardeArret, match="laissées nulles") as e:
        L.lire_la_configuration(CONFIG_V2, cli=True)
    assert all(k in str(e.value) for k in A_REMPLIR)
    note = NOTE_V2.read_text(encoding="utf-8")
    assert all(note.count(f"| `{k}` |") == 1 for k in A_REMPLIR)


def test_v2_admise_une_fois_les_cinq_remplies(tmp_path):
    """Cas sain : les cinq valeurs remplies (factices), le lanceur admet la configuration ; il ne reste rien d'autre
    à fixer. Artefact : une seule laissée vide, refus."""
    c = {**_v2(), **FACTICES}
    cfg, _ = L.lire_la_configuration(_copie_scellee(tmp_path, c, "config-v2-remplie.json"), cli=True)
    assert cfg["lecture"] == LECTURE and cfg["texte_scelle"]["sha256"] == SHA_TEXTE
    for k in A_REMPLIR:
        with pytest.raises(GardeArret, match="laissées nulles"):
            L.lire_la_configuration(_copie_scellee(tmp_path, {**c, k: None}, f"config-v2-sans-{k}.json"), cli=True)
