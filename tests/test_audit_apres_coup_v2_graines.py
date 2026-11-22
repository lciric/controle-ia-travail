"""Essais de `audit_apres_coup_v2.graines` (rang 1) : même graine, mêmes octets ; flux séparés ; jeton de provenance."""
import numpy as np
import pytest

from controle_ia.audit_apres_coup_v2 import graines as gr
from controle_ia.gardes import GardeArret

E = 20261122


def test_meme_graine_memes_octets():
    a = gr.Flux(E, 1, 2).tirer("piece", 1000).tobytes()
    b = gr.Flux(E, 1, 2).tirer("piece", 1000).tobytes()
    assert a == b
    assert gr.generateur_episode(E, 1, 2, 3, "score").random(5).tobytes() == \
        gr.generateur_episode(E, 1, 2, 3, "score").random(5).tobytes()


def test_flux_derives_par_tache_et_par_canal():
    assert gr.Flux(E, 1, 2).tirer("piece", 10).tobytes() != gr.Flux(E, 1, 3).tirer("piece", 10).tobytes()
    assert gr.generateur_episode(E, 1, 2, 3, "score").random(3).tobytes() != \
        gr.generateur_episode(E, 1, 2, 4, "score").random(3).tobytes()


def test_tirage_par_morceaux_egal_au_tirage_d_un_coup():
    f1, f2 = gr.Flux(E, 0, 0), gr.Flux(E, 0, 0)
    a = np.concatenate([f1.tirer("oracle", 300), f1.tirer("oracle", 700)])
    assert a.tobytes() == f2.tirer("oracle", 1000).tobytes()


def test_artefact_flux_partage_entre_score_et_piece():
    """Artefact : un flux partagé entre le score et la pièce. Les flux de canaux distincts ne coïncident jamais, et
    tirer des scores en plus ne change aucun octet de la pièce."""
    f = gr.Flux(E, 0, 0)
    assert f.tirer("score", 100).tobytes() != gr.Flux(E, 0, 0).tirer("piece", 100).tobytes()
    f1, f2 = gr.Flux(E, 0, 0), gr.Flux(E, 0, 0)
    f1.tirer("score", 5000)
    assert f1.tirer("piece", 100).tobytes() == f2.tirer("piece", 100).tobytes()


def test_refus_canal_et_cle():
    with pytest.raises(GardeArret):
        gr.indice_canal("verdict")
    with pytest.raises(GardeArret):
        gr.flux_tache(E, -1, 0, "score")


def _derivation_jouet(entropie, cle):
    return gr.generateur_auxiliaire(entropie, "essais", 77, *cle).random(16).tobytes()


gr.enregistrer_derivation("jouet_essais_v2", _derivation_jouet)
VERITE = gr.declarer_verite("a" * 64, "essais : vérité jouet")


def test_jeton_monde_plante_admis():
    contenu, jeton = gr.emettre_jeton(E, (1, 2), "jouet_essais_v2", VERITE)
    gr.verifier_provenance(contenu, jeton)


def test_artefact_entree_sans_jeton_refusee():
    with pytest.raises(GardeArret, match="hors monde planté"):
        gr.verifier_provenance(b"poids lus d'un fichier de sonde", None)


def test_artefact_contenu_reel_sous_jeton_valide_refuse():
    contenu, jeton = gr.emettre_jeton(E, (1, 2), "jouet_essais_v2", VERITE)
    faux = bytes(len(contenu))
    with pytest.raises(GardeArret, match="hors monde planté"):
        gr.verifier_provenance(faux, jeton)
    # jeton forgé à l'empreinte du faux contenu : la re-dérivation depuis la graine le refuse
    forge = gr.JetonProvenance(jeton.provenance, jeton.entropie, jeton.cle, jeton.derivation,
                               gr.empreinte_octets(faux), VERITE)
    with pytest.raises(GardeArret, match="re-dérivé"):
        gr.verifier_provenance(faux, forge)


def test_artefact_verite_non_declaree_refusee():
    contenu, jeton = gr.emettre_jeton(E, (1, 2), "jouet_essais_v2", "b" * 64)
    with pytest.raises(GardeArret, match="vérité plantée non déclarée"):
        gr.verifier_provenance(contenu, jeton)


def test_espaces_de_graines_distincts():
    """I-4 : chaque espace, aux clés des essais, rend des premiers octets deux à deux distincts ; un espace inconnu ou
    réservé aux canaux est refusé."""
    vus = {}
    for nom in gr.ESPACES:
        if nom in ("canal", "canal_episode"):
            continue
        vus[nom] = gr.generateur_auxiliaire(E, nom, 9, 3).random(4).tobytes()
    vus["canal"] = gr.flux_tache(E, 9, 3, "piece").random(4).tobytes()
    vus["canal_episode"] = gr.generateur_episode(E, 9, 3, 0, "piece").random(4).tobytes()
    assert len(set(vus.values())) == len(vus)
    with pytest.raises(GardeArret):
        gr.generateur_auxiliaire(E, "inconnu", 1)
    with pytest.raises(GardeArret):
        gr.generateur_auxiliaire(E, "canal", 1)


def test_refus_jeton_sans_verite():
    with pytest.raises(GardeArret):
        gr.emettre_jeton(E, (1,), "jouet_essais_v2", "")
