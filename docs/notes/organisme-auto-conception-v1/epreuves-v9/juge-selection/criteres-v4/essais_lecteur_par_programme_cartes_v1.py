# -*- coding: utf-8 -*-
"""Essais de lecteur_par_programme_cartes_v1.py — cartes SYNTHÉTIQUES, inventées ici ; aucune vraie carte.

Un témoin pour le critère D et un témoin pour la voie ; pour chaque garde, un cas sain et un artefact (R5).
Lancement : python3 -B -m pytest -q essais_lecteur_par_programme_cartes_v1.py
"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lecteur_par_programme_cartes_v1 as L  # noqa: E402

SENTINELLE = "ESPECE-SENTINELLE-NE-PAS-LIRE"
CONF = {"champ_refutation": "ce_qui_la_refuterait", "champs_voie": ["titre", "mecanisme"], "hors_choix": []}


def c(titre="Moulin", mecanisme="Un moulin tourne.", refut="Rien."):
    return {"titre": titre, "mecanisme": mecanisme, "ce_qui_la_refuterait": refut}


def lire(champs, conf=None):
    return L.lire_carte(champs, L.valider_configuration(dict(conf or CONF)))


# ---------------------------------------------------------------- témoin du critère D

def test_d_deux_quand_le_non_et_le_oui_nomment_une_decision():
    r = lire(c(mecanisme="Garder le moulin seulement si la farine double.", refut="La farine ne double pas : sinon couper le moulin."))
    assert r["D"] == 2 and r["non_nomme"] is True and r["oui_nomme"] is True and r["note"] == 2


def test_d_abandon_nomme_vaut_une_decision_meme_dit_brievement():
    bref = lire(c(mecanisme="Retenir le moulin si la farine double.", refut="Sinon, couper."))
    long_ = lire(c(mecanisme="Retenir le moulin si la farine double. " * 8,
                   refut="Dans le cas contraire, et après trois lectures concordantes, il faudra retirer le moulin du banc. " * 3))
    assert bref["D"] == 2 and long_["D"] == 2          # la longueur ne change pas la note


def test_d_un_quand_une_seule_issue_est_nommee():
    assert lire(c(mecanisme="Un moulin tourne.", refut="La base suffit."))["D"] == 1
    assert lire(c(mecanisme="Conserver le moulin si la farine double.", refut="La farine ne double pas."))["D"] == 1


def test_d_zero_quand_rien_n_est_nomme_et_null_quand_le_champ_est_vide():
    assert lire(c())["D"] == 0
    r = lire(c(refut="   "))
    assert r["D"] is None and r["note"] is None and r["non_nomme"] is None   # indécidable, jamais 0 par défaut


def test_d_insensible_aux_accents_et_a_la_casse():
    assert lire(c(mecanisme="RÉGLER le seuil.", refut="SINON : Désactiver le moulin."))["D"] == 2


# ---------------------------------------------------------------- témoin de la voie

def test_voie_instrument():
    r = lire(c(titre="Banc d'essai du moulin", mecanisme="Un instrument de rejeu : on rejoue chaque mouture pour l'audit."))
    assert r["voie"] == "I" and r["sous_strate"] is None


@pytest.mark.parametrize("texte,sous", [
    ("Un registre des tentatives hérité d'une course antérieure.", "a"),
    ("Le nul d'archive, formé des lois connues, contre le nul classique.", "b"),
    ("Ce qui est montré à la génération suivante : la note du juge masquée.", "c1"),
    ("Règle de survie : oubli programmé et réentrée sous quota.", "c2"),
    ("Le test de mort passe par une réimplémentation et un interprète.", "c3"),
    ("Multiplicité : correction de Bonferroni puis de Holm.", "d"),
    ("Juges croisés : agrégation fixe et erreurs corrélées du collège.", "e"),
])
def test_voie_question_du_programme_et_sous_strate(texte, sous):
    r = lire(c(mecanisme=texte))
    assert r["voie"] == "P" and r["sous_strate"] == sous


def test_voie_question_neuve_par_defaut_de_termes_et_non_par_silence():
    r = lire(c(mecanisme="Une girouette oriente le moulin selon le vent."))
    assert r["voie"] == "N" and max(r["termes_distincts"].values()) == 0
    assert lire(c(mecanisme="Un oubli."))["voie"] == "N"        # un seul terme : sous le seuil de deux


def test_voie_indecidable_rendue_null():
    egalite = lire(c(mecanisme="Instrument de rejeu ; oubli et réentrée."))          # I : 2, c2 : 2
    assert egalite["voie"] is None
    deux_sous = lire(c(mecanisme="Oubli et réentrée ; multiplicité et Bonferroni."))  # c2 : 2, d : 2
    assert deux_sous["voie"] == "P" and deux_sous["sous_strate"] is None
    vide = lire(c(titre=" ", mecanisme=""))
    assert vide["voie"] is None


def test_un_terme_repete_ne_compte_qu_une_fois():
    r = lire(c(mecanisme="Oubli, oubli, oubli, oubli, encore l'oubli."))
    assert r["termes_distincts"]["c2"] == 1 and r["voie"] == "N"


# ---------------------------------------------------------------- gardes

def test_champ_nomme_absent_refuse():
    lire(c())                                                    # cas sain
    sans = c()
    del sans["ce_qui_la_refuterait"]
    with pytest.raises(L.Refus):
        lire(sans)
    sans = c()
    del sans["mecanisme"]
    with pytest.raises(L.Refus):
        lire(sans)
    with pytest.raises(L.Refus):
        lire(dict(c(), mecanisme=["liste"]))


@pytest.mark.parametrize("conf", [
    {"champ_refutation": "", "champs_voie": ["titre"], "hors_choix": []},
    {"champ_refutation": "r", "champs_voie": [], "hors_choix": []},
    {"champ_refutation": "meta", "champs_voie": ["titre"], "hors_choix": []},
    {"champ_refutation": "r", "champs_voie": ["empreinte"], "hors_choix": []},
    {"champ_refutation": "r", "champs_voie": ["titre"]},
    {"champ_refutation": "r", "champs_voie": ["titre"], "hors_choix": [], "seuil": 1},
])
def test_configuration_refusee(conf):
    L.valider_configuration(dict(CONF))
    with pytest.raises(L.Refus):
        L.valider_configuration(conf)


def fiches():
    return {
        "s-1": {"contenu": c(mecanisme="Retenir le moulin si la farine double.", refut="Sinon couper."), "meta": {"proposeur": SENTINELLE}},
        "s-2": {"contenu": c(titre="Banc d'essai", mecanisme="Instrument de rejeu et d'audit."), "meta": {"proposeur": SENTINELLE}},
        "s-3": {"contenu": c(refut=""), "meta": {"proposeur": SENTINELLE}},
    }


def test_meta_jamais_lu_et_sortie_sans_texte_de_carte():
    acces = []

    class Espion(dict):
        def __getitem__(self, k):
            acces.append(k)
            return dict.__getitem__(self, k)

        def __contains__(self, k):
            acces.append(k)
            return dict.__contains__(self, k)

        def get(self, k, d=None):
            acces.append(k)
            return dict.get(self, k, d)

        def items(self):
            acces.append("<parcours>")
            return dict.items(self)

        def values(self):
            acces.append("<parcours>")
            return dict.values(self)

        def __iter__(self):
            acces.append("<parcours>")
            return dict.__iter__(self)

    f = {i: Espion(r) for i, r in fiches().items()}
    cartes = L.extraire(f, "fiches", [])
    lues, rapport = L.lire_tout(cartes, L.valider_configuration(dict(CONF)))
    assert set(acces) == {"contenu"}
    s = json.dumps({"cartes": lues, "rapport": rapport}, ensure_ascii=False)
    assert SENTINELLE not in s and "farine" not in s and "moulin" not in s
    assert rapport["cartes"] == 3 and rapport["D_indecidable"] == 1 and rapport["D"]["2"] == 1
    assert rapport["voie"]["I"] == 1


def test_formes_fiches_et_masque_et_hors_choix():
    f = fiches()
    assert sorted(L.extraire(f, "fiches", ["s-3"])) == ["s-1", "s-2"]
    masque = {"piece": "masque", "cartes": [{"id": i, "champs": [[k, v] for k, v in r["contenu"].items()]} for i, r in f.items()]}
    a = L.lire_tout(L.extraire(masque, "masque", []), dict(CONF))[0]
    b = L.lire_tout(L.extraire(f, "fiches", []), dict(CONF))[0]
    assert a == b
    with pytest.raises(L.Refus):
        L.extraire(masque, "masque", ["s-1"])            # une carte hors du choix ne doit pas avoir été masquée
    with pytest.raises(L.Refus):
        L.extraire(f, "autre", [])
    with pytest.raises(L.Refus):
        L.extraire({"s-1": {"meta": {}}}, "fiches", [])
    with pytest.raises(L.Refus):
        L.extraire({}, "fiches", [])
    masque["cartes"].append(masque["cartes"][0])
    with pytest.raises(L.Refus):
        L.extraire(masque, "masque", [])


def _ecrire(tmp, nom, obj):
    p = os.path.join(str(tmp), nom)
    with open(p, "w", encoding="utf-8") as fo:
        json.dump(obj, fo, ensure_ascii=False)
    with open(p, "rb") as fo:
        return p, L.sha_octets(fo.read())


def test_commande_cas_sain_empreinte_et_refus_d_ecraser(tmp_path, capsys):
    ca = _ecrire(tmp_path, "cartes.json", fiches())
    k = _ecrire(tmp_path, "conf.json", CONF)
    s = os.path.join(str(tmp_path), "lecture.json")
    assert L.main(["--cartes", *ca, "--forme", "fiches", "--configuration", *k, "--sortie", s]) == 0
    with open(s, encoding="utf-8") as fo:
        d = json.load(fo)
    assert d["lecteur"] == "programme" and [x["id"] for x in d["cartes"]] == ["s-1", "s-2", "s-3"]
    assert {"id", "voie", "note", "D"} <= set(d["cartes"][0])      # lisible par la statistique de famille scellée
    assert os.path.exists(s + ".sha256")
    assert L.main(["--cartes", *ca, "--forme", "fiches", "--configuration", *k, "--sortie", s]) == 2
    s2 = os.path.join(str(tmp_path), "autre.json")
    assert L.main(["--cartes", ca[0], "f" * 64, "--forme", "fiches", "--configuration", *k, "--sortie", s2]) == 2
    assert L.main(["--cartes", *ca, "--forme", "fiches", "--configuration", k[0], "zz", "--sortie", s2]) == 2
    assert not os.path.exists(s2)
    assert "REFUS" in capsys.readouterr().err
