"""Essais R5 de la sonde réseau v2 (R-2415) : résolveur système interrogé sur un nom aléatoire jamais demandé (le cache de
systemd-resolved a donné un faux « ouverte » au premier essai). Aucun réseau : `socket.gethostbyname` est remplacé ; seule la
boucle locale tourne pour de vrai."""
import socket

import pytest

from controle_ia.lean_essai import sonde_reseau_v1 as R1
from controle_ia.lean_essai import sonde_reseau_v2 as R


def faux_resolveur(monkeypatch, effet):
    demandes = []

    def gethostbyname(nom):
        demandes.append(nom)
        if isinstance(effet, Exception):
            raise effet
        return effet
    monkeypatch.setattr(R.socket, "gethostbyname", gethostbyname)
    return demandes


def test_nom_jamais_demande_a_chaque_appel(monkeypatch):
    demandes = faux_resolveur(monkeypatch, "93.184.215.14")
    for _ in range(3):
        R.sonde_resolveur_systeme()
    assert len(set(demandes)) == 3
    for nom in demandes:
        tete, _, reste = nom.partition(".")
        assert reste == R.NOM_DNS and len(tete) == 32 and all(c in "0123456789abcdef" for c in tete)
    assert R.NOM_DNS not in demandes   # jamais le nom fixe que le cache a déjà vu


def test_cache_rempli_avant_ne_trompe_plus(monkeypatch):
    """L'artefact du premier essai : seul `example.com` est en cache (rempli par la sonde « avant ») ; réseau coupé, tout
    autre nom reste sans réponse. La v1 lit « ouverte », la v2 lit « fermée »."""
    sans_reponse = socket.gaierror(socket.EAI_AGAIN, "Temporary failure in name resolution")

    def cache(nom):
        if nom == "example.com":
            return "93.184.215.14"
        raise sans_reponse
    monkeypatch.setattr(socket, "gethostbyname", cache)
    assert R1.sonde_resolveur_systeme()[0] == "ouverte"   # le faux positif de la v1
    assert R.sonde_resolveur_systeme()[0] == "fermée"


@pytest.mark.parametrize("effet, classe", [
    ("198.51.100.1", "ouverte"),                                                       # sain : réponse revenue
    (socket.gaierror(socket.EAI_NONAME, "Name or service not known"), "ouverte"),      # sain : « nom inexistant » revenu
    (socket.gaierror(socket.EAI_AGAIN, "Temporary failure"), "fermée"),                # artefact : aucune réponse
    (socket.gaierror(socket.EAI_FAIL, "Non-recoverable failure"), "indéterminée"),     # ne tranche pas : écart
])
def test_classes_du_resolveur(monkeypatch, effet, classe):
    faux_resolveur(monkeypatch, effet)
    assert R.sonde_resolveur_systeme()[0] == classe


def test_juger_avant_et_apres(monkeypatch):
    monkeypatch.setattr(R, "sonde_tcp", lambda h, p, delai=5.0: ("fermée", "jeté") if h != "127.0.0.1" else ("ouverte", "ok"))
    monkeypatch.setattr(R, "sonde_dns", lambda s, delai=5.0: ("fermée", "jeté"))
    monkeypatch.setattr(R, "sonde_boucle_locale", lambda: ("ouverte", "connexion établie"))
    faux_resolveur(monkeypatch, socket.gaierror(socket.EAI_AGAIN, "x"))
    releve = R.relever()
    assert releve[0]["classe"] == "ouverte" and R.juger(releve, "fermee") == []
    faux_resolveur(monkeypatch, socket.gaierror(socket.EAI_NONAME, "x"))
    ecarts = R.juger(R.relever(), "fermee")
    assert len(ecarts) == 1 and ecarts[0].startswith("résolveur système")
    faux_resolveur(monkeypatch, socket.gaierror(socket.EAI_FAIL, "x"))
    assert len(R.juger(R.relever(), "ouverte")) == 7   # « indéterminée » est un écart dans les deux sens
