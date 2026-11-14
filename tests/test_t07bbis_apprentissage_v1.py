"""Essais R5 de `t07bbis.apprentissage_carte_v1` et `t07bbis.validation_imbriquee_v1` (B bis, plan, points 4 à 8 ;
« Épreuves » : égalité carte-processeur, garde de débit (cas sain : médiane 2 s ; artefact : médiane 20 s simulée), tâche du
pli lu dans un apprentissage (refus), moyenne sur les jetons (refus)). Activations synthétiques seulement ; « cuda » n'est
pas disponible ici : l'apprentissage est éprouvé sur processeur (même code, appareil en paramètre)."""
from __future__ import annotations

import numpy as np
import pytest
import torch

from controle_ia.gardes import GardeArret
from controle_ia.harnais.formats import _ids
from controle_ia.harnais.modeles import tokeniseur_caracteres
from controle_ia.sondes import familles as fam
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.t06.test_croise import partition_plis
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import commun_v1 as cm
from controle_ia.t07bbis import validation_imbriquee_v1 as vi


def _sacs(rng, n=24, d=6, signal=1.0):
    seqs, y = [], []
    for i in range(n):
        t = int(rng.integers(2, 7))
        x = rng.standard_normal((t, d))
        if i % 2:
            x[int(rng.integers(0, t)), 0] += 2.0 * signal
        seqs.append(x.astype(np.float32))
        y.append(i % 2)
    return seqs, np.array(y)


@pytest.mark.parametrize("famille,l2", [("lineaire", 1e-3), ("lineaire", 1e-1), ("attention", 1e-2)])
def test_egalite_au_paquet_gele_sondes_familles_sur_jouet(famille, l2):
    rng = np.random.default_rng(1)
    seqs, y = _sacs(rng)
    lot = ac.LotCarte(seqs, "cpu")
    s = ac.entrainer(lot, famille, "s", 15, y, l2, 1234)
    ref = fam.entrainer(famille, "s", 15, seqs, y, cm.AGREGATION_DE[famille], 1234, fam.Reglages(l2=l2))
    eval_seqs, _ = _sacs(rng, n=40)
    assert ac.ecart_relatif(ac.scores(s, eval_seqs), ac.scores(ref, eval_seqs)) <= 1e-9
    assert s.agregation == ref.agregation and (s.q is None) == (ref.q is None)


def test_controle_carte_processeur_sain_et_artefact():
    rng = np.random.default_rng(2)
    seqs, y = _sacs(rng)
    reglage = {"famille": "attention", "couche": 7, "l2": 1e-2, "nom": "attention-c7-l2_0.01"}
    s = ac.entrainer(ac.LotCarte(seqs, "cpu"), "attention", "s", 7, y, 1e-2, 9)
    ctrl, _ = _sacs(rng, n=30)
    assert ac.controle_carte_processeur(s, seqs, y, reglage, 9, ctrl)["ecart_relatif_max"] <= 1e-9
    faux = SondeLineaireJetons(s.nom, s.couche, s.agregation, s.w * 1.01, s.b, s.q, s.famille)
    with pytest.raises(GardeArret, match="erreur de chaîne"):
        ac.controle_carte_processeur(faux, seqs, y, reglage, 9, ctrl)


def test_carte_sans_algorithmes_deterministes_refus():
    assert not torch.are_deterministic_algorithms_enabled()
    with pytest.raises(GardeArret, match="déterministes"):
        ac.LotCarte(_sacs(np.random.default_rng(3))[0], "cuda")


def test_moyenne_sur_les_jetons_refus():
    for a in ("moyenne", "mediane", "mean"):
        with pytest.raises(GardeArret, match="N-026"):
            cm.exiger_agregation(a)
    seqs, y = _sacs(np.random.default_rng(4))
    s = SondeLineaireJetons("m", 1, "moyenne", np.ones(6), 0.0, None, "lineaire")
    with pytest.raises(GardeArret, match="N-026"):
        ac.scores(s, seqs)
    with pytest.raises(GardeArret):
        ac.entrainer(ac.LotCarte(seqs, "cpu"), "difference_moyennes", "m", 1, y, 1e-3, 0)


def test_perte_non_finie_sonde_en_echec():
    seqs, y = _sacs(np.random.default_rng(5))
    with pytest.raises(ac.SondeEnEchec):
        ac.entrainer(ac.LotCarte(seqs, "cpu"), "lineaire", "x", 1, y, float("inf"), 0, epoques=3)


def test_plis_internes_reels_et_artefact():
    g = cm.Graines(2 ** 100 + 12345)
    t = [f"e{i}" for i in range(32)]
    p = vi.plis_internes(t, g.rng("bbis/interne/e0"))
    assert len(p) == 4 and all(len(x) == 8 for x in p) and sorted(sum(p, [])) == sorted(t)
    assert p == vi.plis_internes(t, cm.Graines(2 ** 100 + 12345).rng("bbis/interne/e0"))
    with pytest.raises(GardeArret, match="32 tâches"):
        vi.plis_internes(t[:16], g.rng("bbis/interne/e1"))


def test_aire_sur_l_instance_refusee_sur_une_tache_du_pli_lu():
    assert vi.aire_apprentissage([1.0, 0.0], [1, 0], ["e1", "e2"], ["e5"]) == 1.0
    with pytest.raises(GardeArret, match="pli lu"):
        vi.aire_apprentissage([1.0, 0.0], [1, 0], ["e1", "e5"], ["e5"])
    with pytest.raises(GardeArret, match="pli lu"):
        vi.exiger_disjonction(["e1", "e5"], ["e5"], "vocabulaire")


def test_choix_du_reglage_ex_aequo():
    regs = cm.grille((7, 15, 23))
    aires = {r["nom"]: 0.6 for r in regs}
    aires["attention-c23-l2_0.001"] = 0.70
    aires["lineaire-c7-l2_0.01"] = 0.696
    aires["lineaire-c15-l2_0.001"] = 0.6951
    assert vi.choisir_reglage(aires, regs, (7, 15, 23))["nom"] == "lineaire-c15-l2_0.001"
    aires["lineaire-c15-l2_0.001"] = 0.694
    assert vi.choisir_reglage(aires, regs, (7, 15, 23))["nom"] == "lineaire-c7-l2_0.01"
    aires = {r["nom"]: None for r in regs}
    with pytest.raises(GardeArret, match="aucun réglage"):
        vi.choisir_reglage(aires, regs, (7, 15, 23))


def _garde(mediane, total=2460, debut=0.0, maintenant=1800.0):
    return vi.GardeDebit(total, debut, horloge=lambda: maintenant), [mediane] * 20


def test_garde_de_debit_sain_2_s_et_artefact_20_s():
    g, durees = _garde(2.0)
    for i, d in enumerate(durees):
        g.noter(d, cm.FAMILLES[i % 2])
    assert g.verifiee and g.journal[-1]["garde_debit"]["projete_h"] < 11
    g, durees = _garde(20.0)
    with pytest.raises(vi.ArretDebit, match="11 h"):
        for i, d in enumerate(durees):
            g.noter(d, cm.FAMILLES[i % 2])
    g, durees = _garde(2.0)
    with pytest.raises(GardeArret, match="entrelacées"):
        for i, d in enumerate(durees):
            g.noter(d, "lineaire" if i < 15 else "attention")
    assert vi.apprentissages_prevus(5, 18, 4, 100) == 2460


class ActsJouet:
    """Activations synthétiques : composante « texte » commune à une action et à ses jumeaux ; composante « état » ajoutée
    sous l'adaptateur saboteur (O[S_d], A_d) et chez l'instruit (consigne)."""

    def __init__(self, n_taches=8, T=3, d=6, doses=(0.5, 1.0), graine=0):
        rng = np.random.default_rng(graine)
        self.tokeniseur = tokeniseur_caracteres()
        self.couches = (1, 2, 3)
        u, v = np.eye(d)[0], np.eye(d)[1]
        self._d, self._t, self._c = {}, {}, {}
        conds = ["honnete", "saboteur", "temoin", "T100"] + [cm.nom_dose(x) for x in doses]
        for c in conds:
            for ti in range(n_taches):
                for p in range(T):
                    k = f"{c}__t{ti:03d}__p{p}"
                    self._t[k], self._c[k] = f"e{ti}", c
                    base = rng.standard_normal((int(rng.integers(3, 7)), d))
                    etat = np.zeros(d)
                    if c.startswith("S"):
                        etat = 1.5 * float(c[1:]) / 100 * u
                    elif c == "saboteur":
                        etat = 1.5 * v
                    self._d[("O", k)] = base + etat
                    if c.startswith("S"):
                        self._d[(f"J{c[1:]}", k)] = base
                    if c == "saboteur":
                        self._d[("Jinstruit", k)] = base
                    if c == "honnete":
                        for x in doses:
                            self._d[(f"A{cm.centiemes(x)}", k)] = base + 0.3 * float(x) * u
                        self._d[("AT", k)] = base
        self._texte = "ACTION: ADD\nTITLE: x\nCOST: 12 hours"

    def cles(self, serie, condition):
        return sorted(k for (s, k) in self._d if s == serie and self._c[k] == condition)

    def tache(self, cle):
        return self._t[cle]

    def lire(self, serie, cle, couche):
        return (self._d[(serie, cle)] * (1.0 + 0.1 * int(couche))).astype(np.float32)

    def texte(self, cle):
        return self._texte

    def ids(self, cle):
        return _ids(self.tokeniseur, self._texte)


@pytest.fixture(scope="module")
def sources_jouet():
    acts = ActsJouet()
    g = cm.Graines(2 ** 100 + 7, reelle=False)
    ctx = vi.Contexte(acts, g, acts.couches, "cpu", reelle=False, epoques=40)
    taches = sorted({acts.tache(k) for k in acts.cles("O", "honnete")})
    plis = partition_plis(taches, 3)
    sorties = {}
    for cellule, pos in (("P-S100", "S100"), ("P-instruit", "saboteur")):
        plan = vi.plan_de_notation(cellule, pos, (0.5, 1.0))
        for k in (0, 1):
            sorties[(cellule, k)] = (pos, vi.apprendre_source(ctx, cellule, pos, plan, k, plis, taches, n_reetiquetages=3,
                                                              n_directions=10))
    return ctx, plis, sorties


def test_source_de_bout_en_bout_sur_jouet(sources_jouet):
    ctx, plis, sorties = sources_jouet
    pos, r = sorties[("P-S100", 0)]
    t = r["tableaux"]
    assert r["meta"]["n_plancher"] == 10 and len(r["meta"]["empreintes_deux_premieres"]) == 2
    assert "aire" not in str(sorted(r["meta"])) and not any("aire" in k for k in t)
    for g in ("O-S100", "O-honnete", "J100-S100", "A100-honnete", "O-T100", "AT-honnete", "O-saboteur", "Jinstruit-saboteur"):
        assert t[f"{g}__plancher"].shape == (10, t[f"{g}__cles"].size)
    assert t["O-S100__nul"].shape[0] == 3 and t["nul__echanges"].shape == (3, 8)
    assert "O-S100__sc_sonde" in t and "J100-S100__enc" in t and "app_enc__enc" in t
    assert set(t["O-S100__taches"]) == {x for x, p in plis.items() if p == 0}
    _, ri = sorties[("P-instruit", 1)]
    assert "O-temoin__plancher" in ri["tableaux"] and "J50-S50__enc" in ri["tableaux"]


def test_controle_a_la_marche_sur_jouet(sources_jouet):
    ctx, plis, sorties = sources_jouet
    r = vi.controle_a_la_marche(ctx, sorties, plis, n_actions=12)
    assert r["ecart_relatif_max"] <= 1e-4 and r["actions"] == 12


def test_epoques_autres_refusees_en_marche_reelle():
    with pytest.raises(GardeArret, match="époques"):
        vi.Contexte(None, None, (7, 15, 23), epoques=40)
