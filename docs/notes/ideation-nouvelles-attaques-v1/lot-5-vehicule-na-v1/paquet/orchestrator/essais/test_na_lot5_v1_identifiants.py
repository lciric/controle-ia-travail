"""Essais du réencodage des identifiants, dans les deux sens (lot 5 du véhicule NA-1 ; conception v5, § 5.2 et § 6.2,
ligne « réencodage, dans les deux sens »). Le module est celui du lot 1 (`identifiants_na_v1`, `38d9860b…`), repris tel
quel, jamais réécrit (mot de la mère). Données factices seules."""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aides_na_lot5_v1 as A5  # noqa: E402
from pole import identifiants_na_v1 as ident  # noqa: E402
from pole import lecteur_fiches_na_v1 as lf  # noqa: E402
from pole import portier_na_v1 as pt  # noqa: E402

ECHANTILLONS_6 = [bytes(6), bytes([255] * 6), bytes([1, 2, 3, 4, 5, 6]), bytes([128, 0, 0, 0, 0, 1]),
                  bytes([0, 0, 0, 0, 0, 1]), bytes([7, 0, 255, 128, 1, 9])]
ECHANTILLONS_5 = [bytes(5), bytes([255] * 5), bytes([7, 0, 255, 128, 1]), bytes([0, 0, 0, 0, 1])]


class TestDeuxSens:
    @pytest.mark.parametrize("octets", ECHANTILLONS_6)
    def test_six_octets_encoder_puis_decoder(self, octets):
        mot = ident.encoder_identifiant_fiche(octets)
        assert len(mot) == 18 and ident.decoder_octets(mot, 6) == octets

    @pytest.mark.parametrize("octets", ECHANTILLONS_5)
    def test_cinq_octets_encoder_puis_decoder(self, octets):
        mot = ident.encoder_identifiant_juge(octets)
        assert len(mot) == 14 and ident.decoder_octets(mot, 5) == octets

    @pytest.mark.parametrize("octets", ECHANTILLONS_6)
    def test_decoder_puis_encoder_rend_le_mot(self, octets):
        mot = ident.encoder_octets(octets)
        assert ident.encoder_octets(ident.decoder_octets(mot, 6)) == mot

    def test_bornes(self):
        assert ident.encoder_octets(bytes(6)) == "ga" * 9
        assert ident.encoder_octets(bytes(5)) == "ga" * 7
        haut6 = ident.encoder_octets(bytes([255] * 6))
        assert ident.decoder_octets(haut6, 6) == bytes([255] * 6)

    def test_ordre_des_octets_premier_le_plus_fort(self):
        # 0x000000000001 vaut 1 : une seule syllabe de rang 1 à la fin ; inversé, l'entier serait 2**40.
        assert ident.encoder_octets(bytes([0, 0, 0, 0, 0, 1])) == "ga" * 8 + "ge"
        assert ident.encoder_octets(bytes([1, 0, 0, 0, 0, 0])) != "ga" * 8 + "ge"

    def test_aucune_suite_hexadecimale(self):
        for o in ECHANTILLONS_6 + ECHANTILLONS_5:
            assert not ident.porte_suite_hexadecimale(ident.encoder_octets(o))

    def test_jeton_du_noyau_reencode(self):
        assert ident.reencoder_jeton_noyau("F0700ff8001", "F", 5) == ident.encoder_identifiant_juge(bytes.fromhex("0700ff8001"))


class TestRefus:
    @pytest.mark.parametrize("mot", ["ga" * 8 + "fa", "ga" * 8 + "Ga", "ga" * 8 + "g1", "ga" * 8 + "ab"])
    def test_hors_alphabet(self, mot):
        with pytest.raises(ident.MotRefuse):
            ident.decoder_octets(mot, 6)

    @pytest.mark.parametrize("mot", ["ga" * 8, "ga" * 10, "ga" * 9 + "g"])
    def test_mauvaise_longueur(self, mot):
        with pytest.raises(ident.MotRefuse):
            ident.decoder_octets(mot, 6)

    def test_entier_au_dela_de_la_borne(self):
        mot = ident.encoder_entier(256 ** 6, 9)
        with pytest.raises(ident.MotRefuse):
            ident.decoder_octets(mot, 6)
        mot5 = ident.encoder_entier(256 ** 5, 7)
        with pytest.raises(ident.MotRefuse):
            ident.decoder_octets(mot5, 5)

    def test_le_portier_refuse_un_identifiant_qui_ne_se_decode_pas(self, tmp_path):
        d = tmp_path / "s"
        d.mkdir()
        p, _ = A5.portier(str(d), [])
        fiche = lf.lire_fiches(A5.en_lignes(A5.contenu())).fiches[0]
        for mauvais in [ident.encoder_entier(256 ** 6, 9), "ga" * 7, "F0123456789ab"]:
            with pytest.raises(pt.PortierRefuse):
                p.classer_fiche(fiche, identifiant=mauvais, case=A5.CASE)
