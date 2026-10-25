"""Correction C-12 (v3 des corrections, sur la v5 de Gemini) : un statut non « OK » de `rechercher` ou de
`telecharger` ne bloque plus l'organisme. Dans la v5, `_consigner_erreur` était appelé en tenant `_VERROU`, qu'il
reprend ; `threading.Lock` n'étant pas réentrant, le fil restait bloqué. L'essai surveille l'appel dans un fil à part
(5 s au plus) : sur la v5 non corrigée il échoue au lieu de bloquer la suite des essais."""
import importlib
import sys
import threading
import types
from pathlib import Path

RACINE_ORGANISME = Path(__file__).resolve().parents[1]
if str(RACINE_ORGANISME) not in sys.path:
    sys.path.insert(0, str(RACINE_ORGANISME))

STATUTS_RECHERCHE = ("PLAFOND", "ECHEC_RECHERCHE", "SOURCE_INCONNUE", "ANOMALIE", "INDISPONIBLE", "REFUSE_FUITE")
STATUTS_TELECHARGEMENT = ("SANS_TEXTE", "PLAFOND", "ECHEC_TELECHARGEMENT", "ANOMALIE", "INDISPONIBLE", "REFUSE_FUITE")


def _client(statut):
    m = types.ModuleType("noyau_client")
    m.especes = lambda: ["GEMINI_ARGON"]
    m.budget = lambda: {"appels_restants": 0, "usd_restants": 0.0, "recherches_restantes": 1, "sources": ["arxiv"],
                        "telechargements_restants": 1, "octets_restants": 1000}
    m.appeler = lambda *a, **k: {"statut": "PLAFOND", "texte": ""}
    m.rechercher = lambda requete, n=5, role="", source="arxiv": {"statut": statut, "source": source, "resultats": [],
                                                                  "identifiant": None, "echec": statut}
    m.telecharger = lambda reference, role="": {"statut": statut, "texte": "", "octets": 0, "identifiant": None,
                                                "echec": statut}
    return m


def _rend_la_main(fonction, delai_s=5.0):
    fini = threading.Event()

    def cible():
        fonction()
        fini.set()

    fil = threading.Thread(target=cible, daemon=True)
    fil.start()
    fil.join(delai_s)
    return fini.is_set()


def test_c12_un_statut_non_ok_ne_bloque_pas_et_reste_consigne(monkeypatch):
    for op, statuts in (("rechercher", STATUTS_RECHERCHE), ("telecharger", STATUTS_TELECHARGEMENT)):
        for statut in statuts:
            monkeypatch.setitem(sys.modules, "noyau_client", _client(statut))
            import principal
            importlib.reload(principal)
            principal._ETAT["erreurs"] = []
            compteurs, journal = {}, []
            if op == "rechercher":
                appel = lambda: principal._enregistrer_recherche("requete d'essai", 5, "essai", "arxiv", journal, compteurs)
            else:
                appel = lambda: principal._enregistrer_telechargement("2501.00001", "essai", journal, compteurs)
            assert _rend_la_main(appel), f"{op} {statut} : l'organisme reste bloqué (verrou repris)"
            assert len(journal) == 1 and journal[0]["statut"] == statut
            assert any(statut in e for e in principal._ETAT["erreurs"]), f"{op} {statut} : repli non consigné"