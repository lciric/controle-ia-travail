"""B4 — l'enveloppe autour de l'étage, commune aux deux usages (exécuteur simulé, étage de l'organisme) : découpage d'une
génération en lots de douze tentatives au plus ; statut « non éprouvée (budget) » ; seuil scellé relu (garde 15) ; projection
du registre vers la fiche et sa garde (garde 11) ; classement écrit dans l'ordre du scellement ; tenue du budget d'épreuve ;
tirage des échecs de l'expérimentateur (B5), au même taux dans les trois bras (garde 19)."""

import numpy as np

from .constantes import COUT_EPREUVE_USD, TAILLE_LOT
from .executeur import verifier_seuil_scelle
from .registre import classement_de_l_enveloppe, projeter_vers_fiche, resultat_non_eprouvee, verifier_projection


class ArretEnveloppe(RuntimeError):
    pass


def lots(sequence, taille=TAILLE_LOT):
    sequence = list(sequence)
    return [sequence[i:i + taille] for i in range(0, len(sequence), taille)]


def lots_par_domaine(entrees, taille=TAILLE_LOT):
    """Les lots d'une génération : un lot ne porte qu'un domaine (l'étage n'a qu'une tranche par appel), douze tentatives au
    plus, dans l'ordre du scellement ; les domaines dans l'ordre de leur première tentative. Rend [(domaine, indices)]."""
    ordre, par_domaine = [], {}
    for i, e in enumerate(entrees):
        d = e["tentative"]["engagement"]["domaine"]
        if d not in par_domaine:
            ordre.append(d)
            par_domaine[d] = []
        par_domaine[d].append(i)
    return [(d, lot) for d in ordre for lot in lots(par_domaine[d], taille)]


def exiger_taux_egaux(taux_par_bras):
    """Garde 19 : le taux d'échec de l'expérimentateur est le même dans tous les bras ; sinon arrêt au lancement."""
    if len(set(float(t) for t in taux_par_bras.values())) != 1:
        raise ArretEnveloppe(f"garde 19 : taux d'échec différents entre bras {taux_par_bras} : arrêt au lancement")
    return True


def cartes_d_un_lot(entrees, lot, liste):
    """Projection des entrées d'un lot vers les cartes de l'étage, chacune vérifiée (gardes 11 et 15) ; classement de
    l'enveloppe dans l'ordre du scellement."""
    cartes = []
    for i in lot:
        e = entrees[i]
        verifier_seuil_scelle(e["tentative"]["engagement"])
        carte = projeter_vers_fiche(e, f"T-{i:04d}", liste)
        verifier_projection(carte, e, entrees, liste)
        cartes.append(carte)
    classement = classement_de_l_enveloppe(cartes)
    if [c["ident"] for c in classement] != [c["identifiant"] for c in cartes]:
        raise ArretEnveloppe("classement hors de l'ordre du scellement")
    return cartes, classement


def eprouver_generation(entrees, tranche_de, executeur, rng_echec, taux_echec, epreuves_payees, rng_budget,
                        liste="avec_description", cout_epreuve=COUT_EPREUVE_USD):
    """`entrees` : champs du proposeur, dans l'ordre du scellement. `tranche_de(domaine)` : tranche d'épreuve du monde en cours.
    `epreuves_payees` : nombre d'épreuves que le budget paie (si elles manquent, les éprouvées sont tirées par graine). Rend
    (liste de (resultat, gardee), journal des lots, échecs tirés)."""
    n = len(entrees)
    echecs = rng_echec.random(n) < taux_echec  # un tirage par tentative, avant toute épreuve
    if epreuves_payees >= n:
        eprouvees = np.ones(n, dtype=bool)
    else:
        eprouvees = np.zeros(n, dtype=bool)
        eprouvees[rng_budget.choice(n, int(epreuves_payees), replace=False)] = True
    sorties, journal = [None] * n, []
    for _, lot in lots_par_domaine(entrees):
        cartes, _ = cartes_d_un_lot(entrees, lot, liste)
        for i in lot:
            e = entrees[i]
            if not eprouvees[i]:
                sorties[i] = (resultat_non_eprouvee(), False)
                continue
            eng = e["tentative"]["engagement"]
            sorties[i] = executeur.eprouver(eng, e["tentative"]["engagement_sha256"], e["prediction_sha256"],
                                            tranche_de(eng["domaine"]), bool(echecs[i]), cout_epreuve)
        journal.append({"lot": len(journal), "tentatives": len(lot), "eprouvees": int(eprouvees[lot].sum()),
                        "cartes": [c["identifiant"] for c in cartes]})
    return sorties, journal, echecs
