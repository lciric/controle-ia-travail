"""Validation du harnais sur modèle réel (T0.4) : répétition complète sur modèle jouet, comparaison de deux
runs (rejeu entre processus), codage bfloat16 sans perte, gardes de lancement et de fin de phase (cas sain +
artefacts), lecture gelée, empreintes des fichiers du modèle.
"""
import json
import subprocess
import time
from pathlib import Path

import numpy as np
import pytest
import torch

import controle_ia
from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.harnais import politique as P
from controle_ia.harnais import validation_reelle as V
from controle_ia.harnais.episode import EnvironnementJouet, jouer_episodes
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import (comparer_fichiers, empreinte_poids, exiger_type_des_poids, modele_jouet,
                                         sha1_git, tokeniseur_caracteres_chat)

PETITE = dict(V.CONFIG_REPETITION,
              logique=dict(V.CONFIG_REPETITION["logique"], T=2, max_nouveaux=8),
              production=dict(V.CONFIG_REPETITION["production"], episodes=4, T=2, max_nouveaux=8),
              debit={"tailles_lot": [1, 4], "longueur_contexte": 32, "max_nouveaux": 4})
LECTURE_SAINE = {"format": "conforme", "tests_instance": "sans objet", "logique_equivalence": "conforme",
                 "logique_controle_negatif": "conforme", "production_equivalence": "conforme",
                 "production_controle_negatif": "conforme", "rejeu_en_processus": "conforme",
                 "audit_symetrie": "non déclenché"}


def test_repetition_complete_puis_rejeu_entre_runs(depot):
    s1 = V.executer(depot, "20261004-160000-repetition-jouet", entropie=77, config=PETITE, verifier_import=False)
    assert s1["lecture"] == LECTURE_SAINE
    r = json.loads((depot / s1["resume"]).read_text(encoding="utf-8"))["resultat"]
    prod, lo = r["production"], r["logique"]
    assert prod["stockage"]["codage"] == "bfloat16-bits" and prod["stockage"]["octets_par_valeur_construction"] == 2
    assert prod["plan_lots"] == [[0, 1], [2, 3]] and [e["par_jeton_conserve"] for e in prod["episodes"]] == [
        False, True, True, False]
    assert lo["equivalence"]["ecart_max"] <= 1e-4 < lo["equivalence"]["controle_negatif"]["min_des_maxima"]
    assert lo["equivalence"]["couverture"]["lignes_echantillon"] == [1, 2] and lo["noyau_attention"] == "math"
    assert set(prod["repere_precision"]) == {"0", "1", "2"} and r["chargement"]["type_des_poids"] == "torch.float32"
    assert [m["taille_lot"] for m in r["debit"]["mesures"]] == [1, 4]
    assert all(m["jetons_generes"] == 4 * m["taille_lot"] for m in r["debit"]["mesures"])
    assert (depot / "diag" / "20261004-160000-repetition-jouet" / "logique-episode-3-trajectoire.json").is_file()
    for e in prod["episodes"]:                       # gros tableaux hors git, scellés sur place, empreinte au résumé
        npz = depot / e["tableaux"]
        assert e["tableaux"].startswith("donnees/") and npz.is_file()
        assert npz.with_name(npz.name + ".sha256").read_text().split()[0] == e["tableaux_sha256"]
        assert set(e["empreintes"]) == {"trajectoire", "activations", "logits", "vecteurs", "scores"}
    committer(depot)
    s2 = V.executer(depot, "20261004-160100-repetition-jouet", config=PETITE, rejeu_de="20261004-160000-repetition-jouet",
                    verifier_import=False)
    assert s2["comparaison"]["identique"] and s2["comparaison"]["lecture"] == "conforme"
    committer(depot)
    with pytest.raises(GardeArret, match="entropie"):
        V.executer(depot, "20261004-160200-repetition-jouet", entropie=78, config=PETITE,
                   rejeu_de="20261004-160000-repetition-jouet", verifier_import=False)
    # rejeu incompatible : refusé avant tout calcul (aucun run créé)
    autre = dict(PETITE, production=dict(PETITE["production"], temperature=0.7))
    with pytest.raises(GardeArret, match="configuration"):
        V.executer(depot, "20261004-160300-repetition-jouet", config=autre, rejeu_de="20261004-160000-repetition-jouet",
                   verifier_import=False)
    assert not (depot / "runs" / "20261004-160300-repetition-jouet").exists()


def test_comparaison_saine_et_artefacts(depot, monkeypatch):
    V.executer(depot, "20261004-170000-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    V.executer(depot, "20261004-170100-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    sain = V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170100-repetition-jouet")
    assert sain["identique"] and sain["differences"] == []
    committer(depot)
    with pytest.raises(GardeArret, match="R12"):      # une comparaison ne se réécrit pas
        V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170100-repetition-jouet")
    V.executer(depot, "20261004-170200-repetition-jouet", entropie=6, config=PETITE, verifier_import=False)
    committer(depot)
    with pytest.raises(GardeArret, match="graines différentes"):
        V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170200-repetition-jouet")
    # artefacts : relectures qui diffèrent (logits, capture, fichier npz, lecture) → différences nommées, « contraire »
    V.executer(depot, "20261004-170400-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    vrai = V.verifier_resultat

    def altere(racine, chemin):
        corps = vrai(racine, chemin)
        if "170400" in str(chemin):
            e = corps["resultat"]["production"]["episodes"][1]
            e["empreintes"]["logits"] = "0" * 64
            e["tableaux_sha256"] = "1" * 64
            e["equivalence"]["empreintes_capture"]["0,0"] = "2" * 64
            corps["resultat"]["lecture"]["format"] = "contraire"
        return corps
    monkeypatch.setattr(V, "verifier_resultat", altere)
    c = V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170400-repetition-jouet")
    assert not c["identique"] and c["lecture"] == "contraire"
    attendues = [{"phase": "production", "episode": "episode-1", "empreinte": "logits"},
                 {"phase": "production", "episode": "episode-1", "equivalence": "empreintes_capture"},
                 {"phase": "production", "episode": "episode-1", "motif": "fichier npz différent"}]
    assert c["differences"][:3] == attendues and c["differences"][3]["motif"] == "lectures différentes"


def test_gardes_de_lancement(depot, tmp_path_factory):
    with pytest.raises(GardeArret, match="sans préenregistrement"):
        V.executer(depot, "20261004-180000-validation-reelle", revision="0" * 40, verifier_import=False)
    with pytest.raises(GardeArret, match="révision figée"):
        V.valider_config(V.CONFIG_REELLE, "main")
    V.valider_config(V.CONFIG_REELLE, "0e9e39f249a16976918f6564b8830bc894c89659")
    for mauvaise, motif in ((dict(PETITE, logique=dict(PETITE["logique"], dtype="bfloat16")), "simple précision"),
                            (dict(PETITE, production=dict(PETITE["production"], episodes_equivalence=[9])), "hors de la phase"),
                            (dict(PETITE, production=dict(PETITE["production"], lots_rejeu_en_processus=[5])), "lots de rejeu"),
                            (dict(PETITE, debit=dict(PETITE["debit"], tailles_lot=[64])), "plus de lignes"),
                            (dict(PETITE, logique=dict(PETITE["logique"], noyau_attention="flash")), "noyau"),
                            (dict(PETITE, logique=dict(PETITE["logique"], tolerance=0)), "tolérance")):
        with pytest.raises(GardeArret, match=motif):
            V.valider_config(mauvaise, None)
    # limite de durée entre phases : l'arrêt est consigné (arret.json scellé, lecture partielle), puis propagé
    with pytest.raises(GardeArret, match="limite de durée"):
        V.executer(depot, "20261004-180100-repetition-jouet", entropie=1, config=dict(PETITE, limite_s=-1),
                   verifier_import=False)
    arret = json.loads((depot / "diag" / "20261004-180100-repetition-jouet" / "arret.json").read_text(encoding="utf-8"))
    assert arret["resultat"]["phase"] == "logique" and "limite de durée" in arret["resultat"]["motif"]
    assert arret["resultat"]["partiel"]["lecture_partielle"]["logique_equivalence"] == "non atteint"
    # mémoire vive (Rem-5) : cas sain, artefact, fichier illisible
    dehors = tmp_path_factory.mktemp("meminfo")
    meminfo = dehors / "meminfo"
    meminfo.write_text("MemTotal:       131072000 kB\n")
    assert V.exiger_memoire_vive(64, meminfo) == 134.2
    meminfo.write_text("MemTotal:       33554432 kB\n")
    with pytest.raises(GardeArret, match="< 64 Go"):
        V.exiger_memoire_vive(64, meminfo)
    with pytest.raises(GardeArret, match="illisible"):
        V.exiger_memoire_vive(64, dehors / "absent")
    assert V.exiger_memoire_vive(0) is None
    with pytest.raises(GardeArret, match="signal TERM"):        # délai externe (Rem-7)
        V._signal_term(15, None)


def test_garde_de_duree_dans_une_phase():
    """Rem-7 : la durée se vérifie à chaque pas (t, i), pas seulement entre les phases."""
    tok = tokeniseur_caracteres_chat()
    fmt = FormatChat(tok, fins={tok.convert_tokens_to_ids("<|im_end|>"), tok.eos_token_id})
    m = modele_jouet(3, len(tok), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    graines = [{(0, 0): 1, (0, 1): 2}]
    jouer_episodes(m, fmt, EnvironnementJouet(), ["e"], 1, 2, graines, [0, 1, 2], 4, echeance=time.perf_counter() + 600)
    with pytest.raises(GardeArret, match="limite de durée dépassée au pas 0"):
        jouer_episodes(m, fmt, EnvironnementJouet(), ["e"], 1, 2, graines, [0, 1, 2], 4, echeance=time.perf_counter() - 1)


def _preregistrement(depot, commit, revision="0e9e39f249a16976918f6564b8830bc894c89659", entropie=12345):
    p = depot / "prereg.md"
    p.write_text(f"- Commit du code d'analyse : `{commit}`\n- Révision du modèle : `{revision}`\n"
                 f"- Entropie : `{entropie}`\n", encoding="utf-8")
    return p


def test_gardes_code_cite_citations_et_import(depot):
    """Rem-8 : gardes de lancement testées (cas sain + artefacts)."""
    (depot / "src").mkdir()
    (depot / "src" / "module.py").write_text("x = 1\n")
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    p = _preregistrement(depot, commit)
    assert V.exiger_code_cite(depot, p) == commit
    assert V.exiger_citations(p, "0e9e39f249a16976918f6564b8830bc894c89659", None) == 12345
    assert V.exiger_citations(p, "0e9e39f249a16976918f6564b8830bc894c89659", 12345) == 12345
    with pytest.raises(GardeArret, match="révision"):
        V.exiger_citations(p, "1" * 40, None)
    with pytest.raises(GardeArret, match="entropie"):
        V.exiger_citations(p, "0e9e39f249a16976918f6564b8830bc894c89659", 999)
    (depot / "sans.md").write_text(f"- Commit du code d'analyse : `{commit}`\n")
    with pytest.raises(GardeArret, match="ne cite pas la révision"):
        V.exiger_citations(depot / "sans.md", "0e9e39f249a16976918f6564b8830bc894c89659", None)
    (depot / "src" / "module.py").write_text("x = 2\n")       # artefact : code modifié puis committé
    committer(depot)
    with pytest.raises(GardeArret, match="modifiés depuis le commit cité"):
        V.exiger_code_cite(depot, p)
    with pytest.raises(GardeArret, match="ne cite pas le commit"):
        V.exiger_code_cite(depot, depot / "README")
    racine = Path(controle_ia.__file__).resolve().parents[2]
    V.exiger_code_importe_sous(racine)                          # cas sain : le code vient de src/ du dépôt
    with pytest.raises(GardeArret, match="hors de la racine"):
        V.exiger_code_importe_sous(depot)


def test_sortie_des_tests_scellee_et_lue(depot, tmp_path_factory):
    """Rem-8 : la sortie de pytest sur l'instance devient un résultat scellé, rattaché au manifeste, et se lit."""
    dehors = tmp_path_factory.mktemp("sorties")                 # hors du dépôt, comme sur l'instance
    ok = dehors / "tests-ok.txt"
    ok.write_text("....\n170 passed in 50.12s\n")
    s = V.executer(depot, "20261004-190000-repetition-jouet", entropie=3, config=PETITE, sortie_tests=ok,
                   verifier_import=False)
    assert s["lecture"]["tests_instance"] == "conforme"
    corps = json.loads((depot / "diag" / "20261004-190000-repetition-jouet" / "tests-instance.json").read_text())
    assert corps["resultat"]["derniere_ligne"] == "170 passed in 50.12s"
    committer(depot)
    ko = dehors / "tests-ko.txt"
    ko.write_text("..F.\n1 failed, 169 passed in 50.12s\n")
    s = V.executer(depot, "20261004-190100-repetition-jouet", entropie=3, config=PETITE, sortie_tests=ko,
                   verifier_import=False)
    assert s["lecture"]["tests_instance"] == "contraire"


def test_lecture_couverture_controle_negatif_et_audit():
    def bilan(ecart=1e-6, minimum=1.0, actions=3, remplissage=5, finies=2, positions=40, lignes=(1, 6),
              zeros_gen=(1, 40), distincts=True, ulp=True):
        return {"tolerance": 1e-4, "ecart_max": ecart,
                "controle_negatif": {"actions": actions, "min_des_maxima": minimum},
                "couverture": {"jetons_remplissage": remplissage, "lignes_finies_avant": finies,
                               "positions_generees_comparees": positions, "lignes_echantillon": list(lignes)},
                "zeros": {"contexte": [5, 10], "generee": list(zeros_gen)},
                "sondes_audit": {"tableaux_distincts": distincts, "ulp_vu": ulp}}

    def resume(**kw):
        return {"format": {"verifie": True}, "logique": {"equivalence": bilan(**kw)},
                "production": {"equivalence": dict(bilan(), tolerance=0.1), "rejeu_en_processus": [{"identique": True}]}}
    assert V.lire(resume(), V.CONFIG_REELLE)["logique_equivalence"] == "conforme"
    assert V.lire(resume(ecart=2e-4), V.CONFIG_REELLE)["logique_equivalence"] == "contraire"
    for manque in ({"remplissage": 0}, {"finies": 0}, {"positions": 0}, {"lignes": (0, 0)}):
        assert V.lire(resume(**manque), V.CONFIG_REELLE)["logique_equivalence"] == "non concluant"
    assert V.lire(resume(minimum=5e-5), V.CONFIG_REELLE)["logique_controle_negatif"] == "contraire"
    assert V.lire(resume(actions=0), V.CONFIG_REELLE)["logique_controle_negatif"] == "non concluant"
    assert V.lire(resume(), V.CONFIG_REELLE)["audit_symetrie"] == "non déclenché"
    assert "réserve levée" in V.lire(resume(zeros_gen=(40, 40)), V.CONFIG_REELLE)["audit_symetrie"]
    assert "réserve maintenue" in V.lire(resume(zeros_gen=(40, 40), ulp=False), V.CONFIG_REELLE)["audit_symetrie"]
    partiel = V.lire({"format": {"verifie": True}}, V.CONFIG_REELLE)
    assert partiel["production_equivalence"] == "non atteint" and partiel["rejeu_en_processus"] == "non atteint"


def test_codage_bfloat16_sans_perte_et_refus():
    x = torch.randn(5, 7).to(torch.bfloat16).to(torch.float32).numpy()
    c = P.coder(x, "bfloat16-bits")
    assert c.dtype == np.uint16 and c.nbytes == x.nbytes // 2
    assert np.array_equal(P.decoder(c, "bfloat16-bits"), x)
    with pytest.raises(GardeArret, match="non représentables"):
        P.coder(np.array([1.0 + 2 ** -20], dtype=np.float32), "bfloat16-bits")
    with pytest.raises(GardeArret, match="inconnu"):
        P.coder(x, "float16")


def test_empreinte_et_type_des_poids_en_demi_precision():
    tok = tokeniseur_caracteres_chat()
    m = modele_jouet(3, len(tok), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    e32 = empreinte_poids(m)
    e16 = empreinte_poids(m.to(torch.bfloat16))
    assert e32 != e16 and e16 == empreinte_poids(modele_jouet(3, len(tok), couches=2, largeur=32, tetes=4,
                                                              tetes_cle_valeur=2, intermediaire=64).to(torch.bfloat16))
    exiger_type_des_poids(m, "bfloat16")
    m.lm_head.weight.data = m.lm_head.weight.data.float()       # artefact : un tenseur resté en simple précision
    with pytest.raises(GardeArret, match="float32"):
        exiger_type_des_poids(m, "bfloat16")


def test_empreintes_des_fichiers_du_modele(tmp_path):
    """Rem-6 : fichiers du modèle contre les empreintes publiées (sha256 des gros fichiers, identifiant git sinon)."""
    import hashlib
    (tmp_path / "config.json").write_bytes(b'{"a": 1}\n')
    (tmp_path / "poids.safetensors").write_bytes(b"\x00" * 1000)
    git = subprocess.run(["git", "hash-object", str(tmp_path / "config.json")], capture_output=True, text=True).stdout.strip()
    assert sha1_git(b'{"a": 1}\n') == git
    publies = {"config.json": {"git_sha1": git},
               "poids.safetensors": {"sha256": hashlib.sha256(b"\x00" * 1000).hexdigest()}}
    r = comparer_fichiers(tmp_path, publies)
    assert all(x["conforme"] for x in r.values()) and r["poids.safetensors"]["octets"] == 1000
    (tmp_path / "poids.safetensors").write_bytes(b"\x00" * 999 + b"\x01")      # artefact : poids altérés
    with pytest.raises(GardeArret, match="poids.safetensors"):
        comparer_fichiers(tmp_path, publies)
    (tmp_path / "poids.safetensors").write_bytes(b"\x00" * 1000)
    (tmp_path / "intrus.json").write_bytes(b"{}")                              # artefact : fichier inconnu du dépôt
    with pytest.raises(GardeArret, match="absent de la révision"):
        comparer_fichiers(tmp_path, publies)


def test_fichiers_du_modele_depuis_un_cache(tmp_path):
    """Le dossier de la révision se retrouve dans un cache au format de huggingface_hub, hors ligne."""
    from controle_ia.harnais.modeles import empreintes_fichiers_modele
    rev = "0e9e39f249a16976918f6564b8830bc894c89659"
    snap = tmp_path / "models--org--modele" / "snapshots" / rev
    snap.mkdir(parents=True)
    contenus = {n: f"{{\"{n}\": 1}}".encode() for n in ("config.json", "generation_config.json", "tokenizer.json",
                                                         "tokenizer_config.json")}
    contenus["model-00001-of-00001.safetensors"] = b"\x01" * 64
    publies = {}
    for n, c in contenus.items():
        (snap / n).write_bytes(c)
        publies[n] = ({"sha256": __import__("hashlib").sha256(c).hexdigest()} if n.endswith(".safetensors")
                      else {"git_sha1": sha1_git(c)})
    r = empreintes_fichiers_modele("org/modele", rev, publies=publies, cache_dir=str(tmp_path))
    assert set(r) == set(contenus) and all(x["conforme"] for x in r.values())
    with pytest.raises(GardeArret, match="absente du cache"):
        empreintes_fichiers_modele("org/modele", "1" * 40, publies=publies, cache_dir=str(tmp_path))
    (snap / "tokenizer.json").unlink()                                          # artefact : fichier essentiel manquant
    with pytest.raises(GardeArret, match="manquants"):
        empreintes_fichiers_modele("org/modele", rev, publies=publies, cache_dir=str(tmp_path))
