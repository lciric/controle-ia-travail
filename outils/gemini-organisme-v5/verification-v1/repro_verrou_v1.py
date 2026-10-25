"""Reproduit (ou non) un blocage de _enregistrer_recherche / _enregistrer_telechargement d'un organisme Gemini.
Usage : python -I repro_verrou_v1.py RACINE_ORGANISME {rechercher|telecharger} STATUT
Sortie : RETOUR <statut> si la fonction rend la main ; sinon, au bout de 5 s, pile des fils (faulthandler) et code 1."""
import faulthandler, sys, types
racine, op, statut = sys.argv[1], sys.argv[2], sys.argv[3]
m = types.ModuleType("noyau_client")
m.especes = lambda: ["GEMINI_ARGON"]
m.budget = lambda: {"appels_restants": 1, "usd_restants": 1.0, "recherches_restantes": 1, "sources": ["arxiv"],
                    "telechargements_restants": 1, "octets_restants": 1000}
m.appeler = lambda *a, **k: {"statut": "PLAFOND", "texte": ""}
m.rechercher = lambda requete, n=5, role="", source="arxiv": {"statut": statut, "source": source, "resultats": [],
                                                              "identifiant": "r1", "echec": None if statut == "OK" else statut}
m.telecharger = lambda reference, role="": {"statut": statut, "texte": "texte" if statut == "OK" else "", "octets": 5,
                                            "identifiant": "t1", "echec": None if statut == "OK" else statut}
sys.modules["noyau_client"] = m
sys.path.insert(0, racine)
import principal
principal._ETAT["erreurs"] = []
compteurs = {}
faulthandler.dump_traceback_later(5, exit=True)
if op == "rechercher":
    r = principal._enregistrer_recherche("evaluation awareness", 5, "essai", "arxiv", [], compteurs)
else:
    r = principal._enregistrer_telechargement("2505.23836", "essai", [], compteurs)
faulthandler.cancel_dump_traceback_later()
print("RETOUR", r["statut"], "erreurs consignées :", len(principal._ETAT["erreurs"]))
