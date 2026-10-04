"""Validation du harnais sur modèle réel (T0.4) : répétition complète sur modèle jouet, comparaison de deux
runs (rejeu entre processus), codage bfloat16 sans perte, gardes de lancement (cas sain + artefacts).
"""
import json

import numpy as np
import pytest
import torch

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.harnais import politique as P
from controle_ia.harnais import validation_reelle as V
from controle_ia.harnais.modeles import empreinte_poids, modele_jouet, tokeniseur_caracteres_chat

PETITE = dict(V.CONFIG_REPETITION,
              logique=dict(V.CONFIG_REPETITION["logique"], T=2, max_nouveaux=8),
              production=dict(V.CONFIG_REPETITION["production"], episodes=4, T=2, max_nouveaux=8),
              debit={"tailles_lot": [1, 4], "longueur_contexte": 32, "max_nouveaux": 4})


def test_repetition_complete_puis_rejeu_entre_runs(depot):
    s1 = V.executer(depot, "20261004-160000-repetition-jouet", entropie=77, config=PETITE, verifier_import=False)
    lecture = s1["lecture"]
    assert {k: v for k, v in lecture.items() if k != "audit_symetrie"} == {
        "format": "conforme", "logique_equivalence": "conforme", "logique_controle_negatif": "conforme",
        "production_equivalence": "conforme", "production_controle_negatif": "conforme",
        "rejeu_en_processus": "conforme"}
    r = json.loads((depot / s1["resume"]).read_text(encoding="utf-8"))["resultat"]
    prod = r["production"]
    assert prod["stockage"]["codage"] == "bfloat16-bits" and prod["stockage"]["octets_par_valeur"] == 2.0
    assert prod["plan_lots"] == [[0, 1], [2, 3]] and [e["par_jeton_conserve"] for e in prod["episodes"]] == [
        True, True, False, False]
    assert r["logique"]["equivalence"]["ecart_max"] <= 1e-4 < r["logique"]["equivalence"]["decale_min"]
    assert [m["taille_lot"] for m in r["debit"]["mesures"]] == [1, 4]
    assert all(m["jetons_generes"] == 4 * m["taille_lot"] for m in r["debit"]["mesures"])
    for e in prod["episodes"]:                       # gros tableaux hors git, scellés sur place, empreinte au résumé
        npz = depot / e["tableaux"]
        assert e["tableaux"].startswith("donnees/") and npz.is_file()
        assert npz.with_name(npz.name + ".sha256").read_text().split()[0] == e["tableaux_sha256"]
    committer(depot)
    s2 = V.executer(depot, "20261004-160100-repetition-jouet", config=PETITE, rejeu_de="20261004-160000-repetition-jouet",
                    verifier_import=False)
    assert s2["comparaison"]["identique"] and s2["comparaison"]["lecture"] == "conforme"
    assert (depot / "diag" / "20261004-160100-repetition-jouet" / "comparaison-20261004-160000-repetition-jouet.json").is_file()
    committer(depot)
    with pytest.raises(GardeArret, match="entropie"):
        V.executer(depot, "20261004-160200-repetition-jouet", entropie=78, config=PETITE,
                   rejeu_de="20261004-160000-repetition-jouet", verifier_import=False)


def test_comparaison_saine_et_artefacts(depot, monkeypatch):
    V.executer(depot, "20261004-170000-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    V.executer(depot, "20261004-170100-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    sain = V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170100-repetition-jouet")
    assert sain["identique"] and sain["differences"] == []
    committer(depot)
    V.executer(depot, "20261004-170200-repetition-jouet", entropie=6, config=PETITE, verifier_import=False)
    committer(depot)
    with pytest.raises(GardeArret, match="graines différentes"):
        V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170200-repetition-jouet")
    autre = dict(PETITE, production=dict(PETITE["production"], temperature=0.7))
    V.executer(depot, "20261004-170300-repetition-jouet", entropie=5, config=autre, verifier_import=False)
    committer(depot)
    with pytest.raises(GardeArret, match="configurations différentes"):
        V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170300-repetition-jouet")
    with pytest.raises(GardeArret, match="R12"):      # une comparaison ne se réécrit pas
        V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170100-repetition-jouet")
    # artefact : une empreinte d'épisode qui diffère à la relecture → différence nommée, lecture « contraire »
    V.executer(depot, "20261004-170400-repetition-jouet", entropie=5, config=PETITE, verifier_import=False)
    committer(depot)
    vrai = V.verifier_resultat

    def altere(racine, chemin):
        corps = vrai(racine, chemin)
        if "170400" in str(chemin):
            corps["resultat"]["production"]["episodes"][0]["empreintes"]["scores"] = "0" * 64
        return corps
    monkeypatch.setattr(V, "verifier_resultat", altere)
    c = V.comparer_runs(depot, "20261004-170000-repetition-jouet", "20261004-170400-repetition-jouet")
    assert not c["identique"] and c["lecture"] == "contraire"
    assert c["differences"] == [{"phase": "production", "episode": "episode-0", "empreinte": "scores"}]


def test_gardes_de_lancement(depot):
    with pytest.raises(GardeArret, match="sans préenregistrement"):
        V.executer(depot, "20261004-180000-validation-reelle", revision="0" * 40, verifier_import=False)
    with pytest.raises(GardeArret, match="révision figée"):
        V.valider_config(V.CONFIG_REELLE, "main")
    V.valider_config(V.CONFIG_REELLE, "0e9e39f249a16976918f6564b8830bc894c89659")
    for mauvaise, motif in ((dict(PETITE, logique=dict(PETITE["logique"], dtype="bfloat16")), "simple précision"),
                            (dict(PETITE, production=dict(PETITE["production"], episodes_equivalence=[9])), "hors de la production"),
                            (dict(PETITE, production=dict(PETITE["production"], lots_rejeu_en_processus=[5])), "lots de rejeu"),
                            (dict(PETITE, debit=dict(PETITE["debit"], tailles_lot=[64])), "plus de lignes"),
                            (dict(PETITE, logique=dict(PETITE["logique"], tolerance=0)), "tolérance")):
        with pytest.raises(GardeArret, match=motif):
            V.valider_config(mauvaise, None)
    # limite de durée : l'arrêt est consigné (arret.json scellé), puis propagé
    with pytest.raises(GardeArret, match="limite de durée"):
        V.executer(depot, "20261004-180100-repetition-jouet", entropie=1, config=dict(PETITE, limite_s=-1),
                   verifier_import=False)
    arret = json.loads((depot / "diag" / "20261004-180100-repetition-jouet" / "arret.json").read_text(encoding="utf-8"))
    assert arret["resultat"]["phase"] == "logique" and "limite de durée" in arret["resultat"]["motif"]


def test_lecture_audit_de_symetrie():
    def resume(nuls_logique, nuls_production):
        eq = lambda nuls: {"ecart_max": 0.0, "decale_min": 1.0, "ecarts_nuls": nuls, "jetons_compares": 10}
        return {"format": {"verifie": True}, "logique": {"equivalence": eq(nuls_logique)},
                "production": {"equivalence": eq(nuls_production), "rejeu_en_processus": [{"identique": True}]}}
    assert V.lire(resume(3, 9), V.CONFIG_REELLE)["audit_symetrie"] == "non déclenché"
    assert "logique" in V.lire(resume(10, 9), V.CONFIG_REELLE)["audit_symetrie"]
    assert "production" in V.lire(resume(3, 10), V.CONFIG_REELLE)["audit_symetrie"]
    assert V.lire(resume(3, 9), V.CONFIG_REELLE)["production_equivalence"] == "conforme"


def test_codage_bfloat16_sans_perte_et_refus():
    x = torch.randn(5, 7).to(torch.bfloat16).to(torch.float32).numpy()
    c = P.coder(x, "bfloat16-bits")
    assert c.dtype == np.uint16 and c.nbytes == x.nbytes // 2
    assert np.array_equal(P.decoder(c, "bfloat16-bits"), x)
    with pytest.raises(GardeArret, match="non représentables"):
        P.coder(np.array([1.0 + 2 ** -20], dtype=np.float32), "bfloat16-bits")
    with pytest.raises(GardeArret, match="inconnu"):
        P.coder(x, "float16")


def test_empreinte_des_poids_en_demi_precision():
    tok = tokeniseur_caracteres_chat()
    m = modele_jouet(3, len(tok), couches=2, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    e32 = empreinte_poids(m)
    e16 = empreinte_poids(m.to(torch.bfloat16))
    assert e32 != e16 and e16 == empreinte_poids(modele_jouet(3, len(tok), couches=2, largeur=32, tetes=4,
                                                              tetes_cle_valeur=2, intermediaire=64).to(torch.bfloat16))
