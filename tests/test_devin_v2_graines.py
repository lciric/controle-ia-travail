"""Essais de la pièce 1 — graines (dérivation par tâche), version 2.

Aucune racine tirée de l'entropie du système : les racines sont fixes ou dérivées
de RACINE ; la source du système est remplacée par des octets fixes (C2 à C4)."""
import numpy as np
import pytest

from controle_ia.devin_v2 import RefusDevin
from controle_ia.devin_v2 import graines
from controle_ia.devin_v2.graines import (RacineScellee, empreinte_racine, generateur_tache, graine_tache,
                                          tirer_racine, verifier_invariance_ordre, verifier_racine_absente,
                                          verifier_racine_revelee)

RACINE = 0xC3A5_1F0E_9B7D_2468_ACE0_1357_9BDF_0246  # 128 bits, fixe pour l'essai
IDS = [f"tache-{k}" for k in range(25)]


def tirage_par_tache(ids):
    return {i: generateur_tache(RACINE, i).random(3) for i in ids}


def tirage_graine_globale(ids):
    rng = np.random.default_rng(np.random.SeedSequence(RACINE))
    return {i: rng.random(3) for i in ids}


def test_ordre_logique_croissant():
    a = RacineScellee("a", racine_derivee("a"))
    b = RacineScellee("b", racine_derivee("b"))
    assert b.ordre > a.ordre


def test_cas_sain_memes_tirages_quand_l_ordre_change():
    verifier_invariance_ordre(tirage_par_tache, IDS, graine_tache(RACINE, "permutation"))
    g = graine_tache(RACINE, "tache-3")
    assert g.spawn_key[0] == graine_tache(RACINE, "tache-3").spawn_key[0]
    assert isinstance(g, np.random.SeedSequence) and g.entropy == RACINE


def test_artefact_graine_globale_refusee():
    with pytest.raises(RefusDevin, match="graine globale"):
        verifier_invariance_ordre(tirage_graine_globale, IDS, graine_tache(RACINE, "permutation"))


def test_taches_distinctes_flux_distincts():
    a = generateur_tache(RACINE, "x").random(4)
    b = generateur_tache(RACINE, "y").random(4)
    assert not np.array_equal(a, b)
    assert np.array_equal(generateur_tache(RACINE, 7).random(4), generateur_tache(RACINE, 7).random(4))


@pytest.mark.parametrize("racine", [12345, 2**100, -1, True, 3.5])
def test_aucun_repli_racine_courte_ou_mal_typee(racine):
    with pytest.raises(RefusDevin):
        graine_tache(racine, "t")


@pytest.mark.parametrize("ident", [True, -3, 2.5, None])
def test_aucun_repli_identifiant_invalide(ident):
    with pytest.raises(RefusDevin):
        graine_tache(RACINE, ident)


def racine_derivee(nom):
    return int.from_bytes(graine_tache(RACINE, nom).generate_state(4, dtype=np.uint32).tobytes(), "big") | (1 << 127)


def test_tirer_racine_lit_la_source_du_systeme(monkeypatch):
    """Chemin câblé : `tirer_racine` lit os.urandom (remplacé ici par des octets fixes)."""
    appels = []

    def octets_fixes(k):
        appels.append(k)
        return bytes(range(0x80, 0x80 + k))

    monkeypatch.setattr(graines.os, "urandom", octets_fixes)
    r = tirer_racine()
    assert appels == [16] and r == int.from_bytes(bytes(range(0x80, 0x90)), "big")
    assert RacineScellee("x").racine_interne() == r


def test_racine_scellee_revelation_apres_fin_seulement():
    r = RacineScellee("essai", racine_derivee("essai"))
    assert r.racine_interne().bit_length() >= 120
    assert str(r.racine_interne()) not in repr(r)
    with pytest.raises(RefusDevin, match="avant la fin"):
        r.reveler()
    r.declarer_fin()
    verifier_racine_revelee(r.reveler(), r.empreinte)
    with pytest.raises(RefusDevin, match="empreinte"):
        verifier_racine_revelee(r.reveler() + 1, r.empreinte)


def test_racine_en_clair_dans_un_texte_refusee():
    r = racine_derivee("en clair")
    verifier_racine_absente(r, ["manifeste : empreinte " + empreinte_racine(r)])
    for forme in (str(r), format(r, "x"), hex(r)):
        with pytest.raises(RefusDevin, match="en clair"):
            verifier_racine_absente(r, ["rien", f"racine = {forme}"])
