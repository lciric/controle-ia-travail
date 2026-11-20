"""Essai final (annexe C ; liste d'arrêt, point 1) : à la fin de la suite d'essais, aucune graine des couches « decisif » ou
« confirmation » n'a été dérivée dans ce processus ; toute tentative de le faire a été refusée et consignée. Ce fichier est nommé
pour être joué le dernier (ordre alphabétique des fichiers d'essais).

Code v3, correction C1 : l'essai passe aussi joué seul. Il provoque lui-même, en fin d'essai, une demande de graine de chacune
des deux couches décisives sans autorisation ; chacune doit être refusée et consignée, et rien ne doit avoir été dérivé. Les
refus déjà consignés par les autres essais du même processus (suite entière) sont lus de même."""

import pytest

from controle_ia.heritage_etage_processeur_v1 import graines as GR


def test_zz_aucune_graine_decisive_derivee():
    derivees = GR.couches_derivees()
    assert "decisif" not in derivees and "confirmation" not in derivees, derivees
    assert all(GR.couche_de(e) not in GR.COUCHES_DECISIVES for _, e in GR.JOURNAL)
    assert set(derivees) <= {"essai", "essai-de-forme"}, derivees  # aucun étalonnage, aucune couche mécanique ni d'audit
    # les refus consignés par les autres essais sont tous des refus de couches décisives (essais des refus)
    assert all(r.split("|", 1)[0] in ("couche=decisif", "couche=confirmation") for r in GR.REFUS)
    # le verrou, éprouvé ici même : une demande par couche décisive, refusée, consignée, rien de dérivé
    journal_avant, refus_avant = list(GR.JOURNAL), list(GR.REFUS)
    g = GR.Graines()
    demandees = []
    for couche in GR.COUCHES_DECISIVES:
        e = GR.etiquette(couche=couche, famille="essai-final", role="verrou")
        demandees.append(e)
        with pytest.raises(GR.GraineRefusee):
            g.generateur(e)
    assert GR.REFUS == refus_avant + demandees
    assert GR.JOURNAL == journal_avant and g.etiquettes == []
    assert GR.REFUS and all(r.split("|", 1)[0] in ("couche=decisif", "couche=confirmation") for r in GR.REFUS)
    assert set(GR.couches_derivees()) <= {"essai", "essai-de-forme"}
