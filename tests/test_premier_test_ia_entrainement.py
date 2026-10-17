"""Entraînement de P3 sur le modèle jouet : empans du gabarit jouet, extraction, 5 familles × couches, sonde principale
choisie sur la validation, planchers ; faits trop courts exclus et comptés ; ex aequo départagés par l'ordre."""
import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import FormatChat
from controle_ia.harnais.modeles import modele_jouet, regler_determinisme, tokeniseur_caracteres_chat
from controle_ia.premier_test_ia import entrainement as en
from controle_ia.premier_test_ia.empans import jetons_message_utilisateur, jetons_reponse_forcee

regler_determinisme(1)
TOK = tokeniseur_caracteres_chat()
FMT = FormatChat(TOK, fins={TOK.convert_tokens_to_ids("<|im_end|>"), TOK.eos_token_id})


def test_empans_gabarit_jouet():
    r = jetons_reponse_forcee(FMT, "", "Pretend.", "The sky is blue.")
    assert r["fin"] - r["debut"] == len("The sky is blue.") - 5
    assert TOK.decode(r["ids"][r["debut"]:r["fin"]]) == "The sky is "
    u = jetons_message_utilisateur(FMT, "", "  hello world  ", 4)
    assert u["fin"] - u["debut"] == 4 and len(u["ids"]) == u["fin"] and u["jetons_texte"] == len("hello world")
    with pytest.raises(GardeArret):
        jetons_reponse_forcee(FMT, "", "Pretend.", "abcd")


def test_preparer_tromperie_exclut_les_faits_courts():
    ex = [{"groupe": "fait-0", "utilisateur": "H", "reponse": "abc", "y": 0},
          {"groupe": "fait-0", "utilisateur": "D", "reponse": "abc", "y": 1},
          {"groupe": "fait-1", "utilisateur": "H", "reponse": "The sky is blue.", "y": 0}]
    sortie, exclus = en.preparer_tromperie(FMT, ex)
    assert exclus == ["fait-0"] and len(sortie) == 1 and sortie[0]["groupe"] == "fait-1"


def test_entrainer_concept_jouet():
    modele = modele_jouet(5, len(TOK), couches=4, largeur=32, tetes=4, tetes_cle_valeur=2, intermediaire=64)
    rng = np.random.default_rng(0)
    textes = [("aaaa bbbb cccc" if k % 2 else "xxxx yyyy zzzz") + f" {k}" for k in range(40)]
    ex = en.preparer_enjeux(FMT, [{"texte": t, "y": k % 2, "groupe": f"g{k // 2}"} for k, t in enumerate(textes)], 8)
    seqs = en.extraire(modele, ex, [0, 2])
    assert set(seqs) == {0, 2} and len(seqs[0]) == 40 and seqs[0][0].shape == (8, 32)
    idx_e, idx_v = list(range(0, 40, 2)) + list(range(1, 30, 2)), list(range(31, 40, 2)) + [30, 32, 34]
    graines = {n: k for k, n in enumerate(en.noms_des_sondes("enjeux", [0, 2]))}
    r = en.entrainer_concept("enjeux", seqs, [e["y"] for e in ex], idx_e, idx_v, [0, 2], graines)
    assert len(r["sondes"]) == 10 and r["principale"] in r["aires_validation"]
    assert r["aires_validation"][r["principale"]] == max(r["aires_validation"].values())
    assert r["identite_validation"]["sondes_controlees"] == 10
    p = next(s for s in r["sondes"] if s.nom == r["principale"])
    pl = en.plancher_de(p, seqs, idx_e, 7, 3)
    assert len(pl) == 7 and all(s.couche == p.couche and s.agregation == p.agregation for s in pl)
    with pytest.raises(GardeArret, match="deux classes"):
        en.entrainer_concept("enjeux", seqs, [e["y"] for e in ex], idx_e, [1, 3], [0, 2], graines)


def test_ex_aequo_departages_par_l_ordre(monkeypatch):
    seqs = {0: [np.ones((2, 3)) * k for k in range(8)]}
    y = [k % 2 for k in range(8)]
    monkeypatch.setattr(en, "aire_sous_courbe", lambda s, yy: 0.7)
    graines = {n: 0 for n in en.noms_des_sondes("c", [0])}
    r = en.entrainer_concept("c", seqs, y, [0, 1, 2, 3, 4, 5], [6, 7], [0], graines)
    assert r["principale"] == "c-difference_moyennes-c0"
