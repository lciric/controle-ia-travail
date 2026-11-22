"""Essais de `audit_apres_coup_v1.alerte` (rang 6) : fausses alarmes ≤ α sur le jumeau honnête ; grille de paris
tronquée refusée ; d0 estimé : correction par d0⁺ ; latence « jamais » censurée."""
import math

import numpy as np
import pytest

from controle_ia.audit_apres_coup_v1.alerte import (ETIQUETTE_AU_DELA, PariExces, alerte_exces, alerte_signature,
                                                  latence)
from controle_ia.audit_apres_coup_v1.graines import generateur_auxiliaire
from controle_ia.audit_apres_coup_v1.oracle_simule import OracleSimule
from controle_ia.audit_apres_coup_v1.regle_audit import RegleAudit, g_identite
from controle_ia.audit_apres_coup_v1.simulateur import Monde, politique_constante, simuler
from controle_ia.gardes import GardeArret

E = 20261122
ALPHA = 0.05


def _taux(alarmes):
    return float(np.mean(alarmes > 0))


def test_fausses_alarmes_sous_alpha_d0_connu():
    R, H, d0 = 2000, 4000, 0.10
    x = (generateur_auxiliaire(E, 60).random((R, H)) < d0).astype(np.int64)
    pari = PariExces(ALPHA, 0.02, d0=d0)
    fa = _taux(pari.premieres_alarmes(x))
    assert fa <= ALPHA + 4 * math.sqrt(ALPHA * (1 - ALPHA) / R)
    assert pari.grille.min() - d0 < 0.02  # la grille descend sous l'excès acceptable


def test_artefact_d0_estime_sans_correction_et_correction():
    """d0 estimé sur m = 400 et pris pour connu : fausses alarmes au-dessus de α à l'horizon 4 000 ; avec d0⁺
    (Clopper et Pearson à α/2, alarme à 2/α), sous α."""
    R, H, m, d0 = 600, 4000, 400, 0.10
    g = generateur_auxiliaire(E, 61)
    naif = corrige = 0
    for _ in range(R):
        ref = int(np.sum(g.random(m) < d0))
        x = (g.random((1, H)) < d0).astype(np.int64)
        naif += PariExces(ALPHA, 0.02, d0=ref / m).premieres_alarmes(x)[0] > 0
        pc = PariExces(ALPHA, 0.02, reference=(ref, m))
        corrige += pc.premieres_alarmes(x)[0] > 0
    assert naif / R > ALPHA + 4 * math.sqrt(ALPHA * (1 - ALPHA) / R)
    assert corrige / R <= ALPHA + 4 * math.sqrt(ALPHA * (1 - ALPHA) / R)
    assert pc.exces_jamais_vu > 0
    assert pc.etiquette_horizon(H) == ETIQUETTE_AU_DELA and pc.etiquette_horizon(m) == "dans la référence"
    assert pc.declaration(H)["m"] == m and pc.declaration(H)["nature"] == "borne, non loi exacte"


def test_artefact_grille_tronquee_refusee():
    with pytest.raises(GardeArret, match="borne linéaire"):
        PariExces(ALPHA, 0.02, d0=0.10, grille=np.array([0.55, 0.325, 0.2125]))
    with pytest.raises(GardeArret, match="validité"):
        PariExces(ALPHA, 0.02, d0=0.10, grille=np.array([0.05, 0.11]))
    with pytest.raises(GardeArret):
        PariExces(ALPHA, 0.02)  # ni d0 ni référence


def test_puissance_sous_un_exces_reel():
    R, H = 200, 4000
    x = (generateur_auxiliaire(E, 62).random((R, H)) < 0.16).astype(np.int64)
    assert _taux(PariExces(ALPHA, 0.02, d0=0.10).premieres_alarmes(x)) > 0.9


def test_alerte_de_signature_et_latence():
    m = Monde(20, E, ((1.0, 1.0),), 1.0, politique_constante(0.05), 0.0)
    r = RegleAudit(0.05, 0.0, 0.0, g_identite, 1.0)
    res = simuler(m, r, OracleSimule(1.0, 0.0, 2, "signature"), 0, 5000)
    h = alerte_signature(res.journal)
    assert h is not None
    lat = latence(res.journal, res.verite.dommage, h)
    assert lat.nombre >= 3  # délai de 2 endommagés compris
    jamais = latence(res.journal, res.verite.dommage, None)
    with pytest.raises(GardeArret, match="jamais"):
        jamais.nombre


def test_alerte_d_exces_sur_la_seule_strate_du_plancher():
    m = Monde(21, E, ((1.0, 1.0),), 1.0, politique_constante(0.30), 0.0)
    r = RegleAudit(0.2, 0.0, 0.0, g_identite, 1.0)
    res = simuler(m, r, OracleSimule(1.0, 0.0, 0, "exces"), 0, 20_000)
    assert alerte_exces(res.journal, PariExces(ALPHA, 0.02, d0=0.10)) is not None
    m0 = Monde(22, E, ((1.0, 1.0),), 1.0, politique_constante(0.10), 0.0)
    res0 = simuler(m0, r, OracleSimule(1.0, 0.0, 0, "exces"), 0, 2000)
    # sous le nul, l'alarme est rare ; ici on vérifie seulement que la lecture ne prend que la strate du plancher
    assert np.all(res0.journal.colonne("source")[res0.journal.colonne("v_episode")] >= 1)
