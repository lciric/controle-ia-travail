"""Essais (R5) du programme qui écrit la configuration réelle de la course de T0.8
(`scripts/ecrire_configuration_course_t08_v1.py`), sur un texte scellé factice : cas sain (la configuration passe
`course_v1.exiger_course_reelle`) ; artefacts — marqueur absent du texte, phrase de « Machine » absente, marqueur restant,
GO non cité, plafond différent, sortie existante, texte altéré après scellement."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest

from controle_ia.scellement import sceller
from controle_ia.t08 import configuration_v1 as cf

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("config_t08", RACINE / "scripts" / "ecrire_configuration_course_t08_v1.py")
E = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(E)

RUN = "20261111-151701-t06-reel"
EMP = {"mesures-t06.npz": "a" * 64, "textes-actions-t06.jsonl": "b" * 64, "episodes-t06.json": "c" * 64,
       "manifeste.json": "d" * 64, "lecture-cout-t06.json": "e" * 64}


def marqueurs(**changes):
    m = {"COMMIT_CODE_T08": "1234567890abcdef1234567890abcdef12345678",
         "CODE_MOTS_ET_COUT_T06": {"commit": "f" * 40, "fichier_inscription": "registres/code-mots-et-cout-t06/x.json",
                                   "sha256_inscription": "9" * 64, "module": "scripts/mots_et_cout_t06_v3.py",
                                   "sha256_module": "8" * 64},
         "RUN_7B": {"run_id": RUN, "branche": "calcul/t06-confirmation-7b-v1", "manifeste_sha256": EMP["manifeste.json"]},
         "EMPREINTES_ENTREES_7B": dict(EMP), "ENTROPIE_T08": 271828182845904523536028747135266249775,
         "GO_T08": {"id": "GO-2026-11-10-12", "plafond_usd": 120},
         "LIGNE_DEPENSE_T08": "engagement : T0.8 bases boîte noire v0 (GO-2026-11-10-12) ; plafond 120 USD"}
    m.update(changes)
    return m


def texte(m, sans=(), plus=""):
    lignes = ["# Texte factice de T0.8", f"commit `{m['COMMIT_CODE_T08']}` ; entropie `{m['ENTROPIE_T08']}`",
              f"run `{m['RUN_7B']['run_id']}` ; GO `{m['GO_T08']['id']}`, prolongé par `GO-2026-11-22-79`"]
    lignes += [f"- `{k}` `{v}`" for k, v in m["EMPREINTES_ENTREES_7B"].items()]
    machine = ("**Machine** : une carte A100 SXM4 80 Go (même type que 7b), au plus 1,30 USD de l'heure, au moins 8 cœurs "
               "effectifs, 64 Go de mémoire vive, 100 Go de disque, stockage au plus 0,08 USD de l'heure, téléchargement au "
               "plus 0,05 USD par Go ; **aucune relance automatique sur H200**. Disque, téléchargement ≤ 40 Go × 0,05. Plafond "
               "proposé : **120 USD** cumulés, compte rendu à 40 USD.")
    for s in sans:
        machine = machine.replace(s, "")
    return "\n".join(lignes + [machine, plus]) + "\n"


def ecrire(tmp_path, m, t, nom="texte.md"):
    p = tmp_path / nom
    p.write_text(t, encoding="utf-8")
    sceller(p)
    mj = tmp_path / f"marqueurs-{nom}.json"
    mj.write_text(json.dumps(m), encoding="utf-8")
    return p, mj


def lancer(p, mj, sortie, go="GO-2026-11-10-12,GO-2026-11-22-79"):
    return E.main(["--texte", str(p), "--marqueurs", str(mj), "--go-admis", go, "--sortie", str(sortie)])


def test_cas_sain(tmp_path, capsys):
    m = marqueurs()
    p, mj = ecrire(tmp_path, m, texte(m))
    s = tmp_path / "prereg" / "T0.8-configuration-course-v1.json"
    assert lancer(p, mj, s) == 0
    c = json.loads(s.read_text(encoding="utf-8"))
    assert (tmp_path / "prereg" / "T0.8-configuration-course-v1.json.sha256").is_file()
    for k, v in cf.VALEURS_GELEES_COURSE.items():
        assert c[k] == v
    assert c["agent"] == cf.SPEC_AGENT_7B and c["juges"] == cf.SPEC_JUGES and c["marqueurs"] == m
    assert c["entrees"]["textes_7b"] == {"chemin": f"donnees/{RUN}/textes-actions-t06.jsonl", "sha256": "b" * 64,
                                         "phase": "course"}
    assert c["entrees"]["taches"]["sha256"] == cf.TACHES_EVALUATION_SHA256
    assert sorted(c["entrees"]) == sorted(("taches", "textes_7b", "episodes_7b", "manifeste_7b", "invite", "consignes"))
    l = c["lancement"]
    assert l["carte"] == {"course": {"nom": "A100 SXM4 80 Go", "nom_offre": "A100 SXM4", "memoire_carte_min_mo": 80000,
                                     "prix_max_usd_h": 1.3}}
    assert l["offre"] == {"coeurs_effectifs_min": 8, "disque_min_go": 100, "etiquette": "t08-v1", "memoire_vive_min_mo": 64000,
                          "stockage_max_usd_h": 0.08, "telechargement_go_prevu": 40, "telechargement_max_usd_go": 0.05}
    assert l["plafond_usd"] == 120 and l["compte_rendu_usd"] == 40 and l["go_admis"] == ["GO-2026-11-10-12", "GO-2026-11-22-79"]
    assert "relance" not in l["carte"]
    # même entrée, même sortie à l'octet (programme déterministe)
    s2 = tmp_path / "bis.json"
    assert lancer(p, mj, s2) == 0
    assert s2.read_bytes() == s.read_bytes()


@pytest.mark.parametrize("cas", ["valeur_absente", "phrase_absente", "marqueur_restant", "go_non_cite", "plafond",
                                 "go_ordre", "sortie_existante", "texte_altere"])
def test_artefacts(tmp_path, capsys, cas):
    m = marqueurs()
    t = texte(m)
    go = "GO-2026-11-10-12,GO-2026-11-22-79"
    if cas == "valeur_absente":
        t = t.replace(str(m["ENTROPIE_T08"]), "0")
    elif cas == "phrase_absente":
        t = texte(m, sans=("au moins 8 cœurs effectifs, ",))
    elif cas == "marqueur_restant":
        t = texte(m, plus="<<LIGNE_DEPENSE_T08>>")
    elif cas == "go_non_cite":
        go = "GO-2026-11-10-12,GO-2026-11-22-93"
    elif cas == "plafond":
        m = marqueurs(GO_T08={"id": "GO-2026-11-10-12", "plafond_usd": 200})
    elif cas == "go_ordre":
        go = "GO-2026-11-22-79,GO-2026-11-10-12"
    p, mj = ecrire(tmp_path, m, t)
    s = tmp_path / "sortie.json"
    if cas == "sortie_existante":
        s.write_text("{}\n")
    if cas == "texte_altere":
        p.write_text(t + "ajout\n", encoding="utf-8")
    assert lancer(p, mj, s, go) == 1
    assert "ARRÊT" in capsys.readouterr().err
    if cas != "sortie_existante":
        assert not s.exists()
