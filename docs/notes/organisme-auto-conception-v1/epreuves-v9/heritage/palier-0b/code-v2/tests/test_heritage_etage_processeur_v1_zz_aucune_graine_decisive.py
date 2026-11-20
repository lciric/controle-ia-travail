"""Essai final (annexe C ; liste d'arrêt, point 1) : à la fin de la suite d'essais, aucune graine des couches « decisif » ou
« confirmation » n'a été dérivée dans ce processus ; toute tentative de le faire a été refusée et consignée. Ce fichier est nommé
pour être joué le dernier (ordre alphabétique des fichiers d'essais)."""

from controle_ia.heritage_etage_processeur_v1 import graines as GR


def test_zz_aucune_graine_decisive_derivee():
    derivees = GR.couches_derivees()
    assert "decisif" not in derivees and "confirmation" not in derivees, derivees
    assert all(GR.couche_de(e) not in GR.COUCHES_DECISIVES for _, e in GR.JOURNAL)
    assert set(derivees) <= {"essai", "essai-de-forme"}, derivees  # aucun étalonnage, aucune couche mécanique ni d'audit
    # les refus consignés sont tous des refus de couches décisives (essais des refus)
    assert GR.REFUS and all(r.split("|", 1)[0] in ("couche=decisif", "couche=confirmation") for r in GR.REFUS)
