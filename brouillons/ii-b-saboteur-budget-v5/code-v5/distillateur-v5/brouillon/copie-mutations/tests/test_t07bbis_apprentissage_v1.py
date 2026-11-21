"""Essais R5 de `t07bbis.apprentissage_carte_v1` et `t07bbis.validation_imbriquee_v1` (B bis, plan, points 4 à 9 ; « Code neuf »,
épreuves : égalité carte-processeur sur jouet et sur échantillon ; garde de débit (cas sain : médiane 2 s ; artefact : médiane
20 s simulée) ; tâche du pli lu dans un apprentissage (refus) ; moyenne sur les jetons (refus) ; plus le choix du réglage, les plis
internes, le nul de réétiquetage, la notation sans aire). Activations synthétiques seulement ; « cuda » n'est pas disponible
ici : l'apprentissage est éprouvé sur processeur (même code, appareil en paramètre)."""
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


@pytest.mark.parametrize("famille,l2", [("lineaire", 1e-3), ("lineaire", 1e-1), ("attention", 1e-2), ("attention", 1e-3)])
def test_egalite_au_paquet_gele_sondes_familles_sur_jouet(famille, l2):
    rng = np.random.default_rng(1)
    seqs, y = _sacs(rng)
    s = ac.entrainer(ac.LotCarte(seqs, "cpu"), famille, "s", 15, y, l2, 1234)
    ref = fam.entrainer(famille, "s", 15, seqs, y, cm.AGREGATION_DE[famille], 1234, fam.Reglages(l2=l2))
    eval_seqs, _ = _sacs(rng, n=40)
    assert ac.ecart_relatif(ac.scores(s, eval_seqs), ac.scores(ref, eval_seqs)) <= 1e-9
    assert s.agregation == ref.agregation and (s.q is None) == (ref.q is None) and s.famille == ref.famille


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
    with pytest.raises(GardeArret, match="erreur de chaîne"):
        ac.controle_carte_processeur(s, seqs, y, reglage, 10, ctrl)            # autre graine : autre départ de q


def test_carte_sans_algorithmes_deterministes_refus(monkeypatch):
    monkeypatch.setattr(torch, "are_deterministic_algorithms_enabled", lambda: False)
    with pytest.raises(GardeArret, match="déterministes"):
        ac.LotCarte(_sacs(np.random.default_rng(3))[0], "cuda")
    monkeypatch.setattr(torch, "are_deterministic_algorithms_enabled", lambda: True)
    ac.exiger_deterministe("cuda")


def test_moyenne_sur_les_jetons_refus():
    seqs, y = _sacs(np.random.default_rng(4))
    for a in ("moyenne", "mediane", "mean"):
        s = SondeLineaireJetons("m", 1, a, np.ones(6), 0.0, None, "lineaire")
        with pytest.raises(GardeArret, match="N-026"):
            ac.scores(s, seqs)
    with pytest.raises(GardeArret, match="hors de la grille"):
        ac.entrainer(ac.LotCarte(seqs, "cpu"), "difference_moyennes", "m", 1, y, 1e-3, 0)
    lot = ac.LotCarte(seqs, "cpu")
    with pytest.raises(GardeArret, match="N-026"):
        ac._agreger(lot.X @ torch.zeros(lot.d, dtype=torch.float64), None, lot.idx, lot.n, "moyenne")


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
    for quoi in ("apprentissage", "réglage", "vocabulaire", "covariance du plancher"):
        with pytest.raises(GardeArret, match="pli lu"):
            vi.exiger_disjonction(["e1", "e5"], ["e5"], quoi)
    vi.exiger_disjonction(["e1", "e2"], ["e5"], "apprentissage")


def test_choix_du_reglage_ex_aequo():
    regs = cm.grille((7, 15, 23))
    aires = {r["nom"]: 0.6 for r in regs}
    aires["attention-c23-l2_0.001"] = 0.70
    aires["lineaire-c7-l2_0.01"] = 0.696
    aires["lineaire-c15-l2_0.001"] = 0.6951
    assert vi.choisir_reglage(aires, regs, (7, 15, 23))["nom"] == "lineaire-c15-l2_0.001"
    aires["lineaire-c15-l2_0.001"] = 0.694
    assert vi.choisir_reglage(aires, regs, (7, 15, 23))["nom"] == "lineaire-c7-l2_0.01"
    aires["attention-c23-l2_0.001"] = None                # inéligible : meilleure 0,696 ; 0,694 est ex aequo, couche 15 d'abord
    assert vi.choisir_reglage(aires, regs, (7, 15, 23))["nom"] == "lineaire-c15-l2_0.001"
    with pytest.raises(GardeArret, match="aucun réglage"):
        vi.choisir_reglage({r["nom"]: None for r in regs}, regs, (7, 15, 23))


def _garde(mediane, total=2460, debut=0.0, maintenant=1800.0):
    return vi.GardeDebit(total, debut, horloge=lambda: maintenant), [mediane] * 20


def test_garde_de_debit_sain_2_s_et_artefact_20_s():
    assert vi.apprentissages_prevus(5, 18, 4, 100) == 2460
    g, durees = _garde(2.0)
    for i, d in enumerate(durees):
        g.noter(d, cm.FAMILLES[i % 2])
    j = g.journal[-1]["garde_debit"]
    assert g.verifiee and j["projete_h"] < 11 and j["mediane_s"] == 2.0 and set(j) >= {"heures_ecoulees", "limite_h"}
    assert not any(str(k).startswith("aire") for e in g.journal for k in e["garde_debit"])
    g, durees = _garde(20.0)
    with pytest.raises(vi.ArretDebit, match="11 h"):
        for i, d in enumerate(durees):
            g.noter(d, cm.FAMILLES[i % 2])
    g, durees = _garde(2.0)
    with pytest.raises(GardeArret, match="entrelacées"):
        for i, d in enumerate(durees):
            g.noter(d, "lineaire" if i < 15 else "attention")
    g, durees = _garde(2.0)                              # variante (r1) : une seule famille
    for d in durees:
        g.noter(d, "lineaire")
    assert g.verifiee


class ActsJouet:
    """Activations synthétiques : composante « texte » commune à une action et à ses jumeaux ; composante « état » ajoutée sous
    l'adaptateur saboteur (O[S_d], A_d) et chez l'instruit."""

    def __init__(self, n_taches=12, T=3, d=6, doses=(0.5, 1.0), graine=0):
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
                    etat = 1.5 * float(c[1:]) / 100 * u if c.startswith("S") else (1.5 * v if c == "saboteur" else 0.0)
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
    ctx = vi.Contexte(acts, g, acts.couches, "cpu", reelle=False, epoques=10, n_plis_internes=3)
    taches = sorted({acts.tache(k) for k in acts.cles("O", "honnete")})
    plis = partition_plis(taches, 3)
    controle = vi.ControleCarte(g, [(c, k) for c in ("P-S100", "P-instruit") for k in (0, 1)], n_actions=10)
    sorties = {}
    for cellule, pos in (("P-S100", "S100"), ("P-instruit", "saboteur")):
        plan = vi.plan_de_notation(pos, (0.5, 1.0))
        for k in (0, 1):
            res = vi.apprendre_source(ctx, cellule, pos, plan, k, plis, taches, n_reetiquetages=3, n_directions=10)
            sorties[(cellule, k)] = (pos, res)
            controle.apres(ctx, cellule, k, pos, res, plis)
    return ctx, plis, sorties, controle


def test_source_de_bout_en_bout_sur_jouet_scores_seulement(sources_jouet):
    ctx, plis, sorties, _ = sources_jouet
    pos, r = sorties[("P-S100", 0)]
    t = r["tableaux"]
    assert r["meta"]["n_plancher"] == 10 and len(r["meta"]["empreintes_deux_premieres"]) == 2
    assert r["meta"]["noms_deux_premieres"][0].endswith("-bbis-plancher-0")
    assert not any(str(k).startswith("aire") for k in r["meta"]) and not any("aire" in k for k in t)
    for g in ("O-S100", "O-honnete", "J100-S100", "A100-honnete", "O-T100", "AT-honnete", "O-saboteur", "Jinstruit-saboteur"):
        assert t[f"{g}__plancher"].shape == (10, t[f"{g}__cles"].size) and np.all(np.isfinite(t[f"{g}__sonde"]))
    assert t["O-S100__nul"].shape == (3, t["O-S100__cles"].size) and t["nul__echanges"].shape == (3, 12)
    assert "O-S100__sc_sonde" in t and "J100-S100__enc" in t and "app_enc__enc" in t and t["app__nul"].shape[0] == 3
    lues = {x for x, p in plis.items() if p == 0}
    assert set(t["O-S100__taches"]) == lues and not (set(str(ctx.acts.tache(c)) for c in t["app__cles"]) & lues)
    assert np.array_equal(t["O-S100__cles"], np.array(ctx.acts.cles("O", "S100"))[[ctx.acts.tache(c) in lues
                                                                                   for c in ctx.acts.cles("O", "S100")]])
    _, ri = sorties[("P-instruit", 1)]
    assert "O-temoin__plancher" in ri["tableaux"] and "J50-S50__enc" in ri["tableaux"] and "O-S50__nul" in ri["tableaux"]
    assert ri["tableaux"]["Jinstruit-saboteur__sc_valide"].size if "Jinstruit-saboteur__sc_valide" in ri["tableaux"] else True


def test_meme_reetiquetage_dans_les_deux_plis_et_pour_l_apprentissage(sources_jouet):
    _, _, sorties, _ = sources_jouet
    a, b = sorties[("P-S100", 0)][1]["tableaux"], sorties[("P-S100", 1)][1]["tableaux"]
    assert np.array_equal(a["nul__echanges"], b["nul__echanges"]) and np.array_equal(a["nul__taches"], b["nul__taches"])
    c = sorties[("P-instruit", 0)][1]["tableaux"]
    assert not np.array_equal(a["nul__echanges"], c["nul__echanges"])            # graine propre par cellule


class _ActsSC:
    """Deux actions : l'une porte un champ COST lisible, l'autre non ; le jeton le plus haut est le dernier (dans le champ)."""

    def __init__(self):
        self.tokeniseur = tokeniseur_caracteres()
        self.textes = {"a": "ACTION: ADD\nTITLE: x\nCOST: 12 hours", "b": "ACTION: ADD\nTITLE: x\nno cost here"}

    def texte(self, k):
        return self.textes[k]

    def ids(self, k):
        return _ids(self.tokeniseur, self.textes[k])

    def lire(self, s, k, c):
        a = np.zeros((len(self.ids(k)), 3), dtype=np.float32)
        a[-1, 0] = 5.0
        return a


def test_lecture_sans_le_champ_du_cout_restreint_les_jetons(sources_jouet):
    """SC : seuls les jetons strictement avant le champ COST sont notés (cas sain) ; action sans champ : exclue (artefact)."""
    ctx, _, sorties, _ = sources_jouet
    t = sorties[("P-S100", 0)][1]["tableaux"]
    assert t["O-S100__sc_valide"].all() and np.all(np.isfinite(t["O-S100__sc_sonde"]))
    acts = _ActsSC()
    sonde = SondeLineaireJetons("s", 1, "max", np.array([1.0, 0.0, 0.0]), 0.0, None, "lineaire")
    plancher = [SondeLineaireJetons(f"p{j}", 1, "max", np.array([0.0, 1.0, 0.0]), 0.0, None, "plancher") for j in range(3)]
    r = vi._scores_sc(acts, sonde, plancher, [("O", "S100", "a"), ("O", "S100", "b")], 1)
    assert r["sc_valide"].tolist() == [True, False]
    assert r["sc_sonde"][0] == 0.0 and np.isnan(r["sc_sonde"][1]) and r["sc_plancher"].shape == (3, 2)
    assert ac.scores(sonde, [acts.lire("O", "a", 1)])[0] == 5.0


def test_controle_carte_tire_d_avance_et_joue_des_que_le_couple_est_appris(sources_jouet):
    ctx, plis, sorties, controle = sources_jouet
    r = controle.resultat
    assert r is not None and (r["cellule"], r["pli"]) == controle.couple and r["ecart_relatif_max"] <= 1e-4 and r["actions"] == 10
    assert controle.couple == vi.ControleCarte(cm.Graines(2 ** 100 + 7, reelle=False),
                                               [(c, k) for c in ("P-S100", "P-instruit") for k in (0, 1)]).couple


def test_epoques_plis_ou_familles_autres_refuses_en_marche_reelle():
    with pytest.raises(GardeArret, match="époques"):
        vi.Contexte(None, None, (7, 15, 23), epoques=40)
    with pytest.raises(GardeArret, match="plis internes"):
        vi.Contexte(None, None, (7, 15, 23), n_plis_internes=3)
    with pytest.raises(GardeArret, match="familles"):
        vi.Contexte(None, None, (7, 15, 23), familles=("attention",))
    assert vi.Contexte(None, None, (7, 15, 23), familles=("lineaire",)).familles == ("lineaire",)      # variante (r1)
    assert cm.VARIANTES["r1"] == {"familles": ("lineaire",), "n_reetiquetages": 50}
    assert len(cm.grille((7, 15, 23), ("lineaire",))) == 9 and cm.VARIANTES[None]["n_reetiquetages"] == cm.N_REETIQUETAGES


def test_plan_de_notation_des_sources():
    p = vi.plan_de_notation("S50", (0.25, 0.5, 0.75, 1.0))
    assert p["sonde"] == [("O", "S50"), ("O", "honnete"), ("J50", "S50"), ("A50", "honnete"), ("O", "T100"), ("AT", "honnete")]
    assert p["enc_positifs"] == ("J50", "S50") and p["sc"] == [("O", "S50"), ("O", "honnete"), ("J50", "S50")]
    s100 = vi.plan_de_notation("S100", (0.25, 0.5, 0.75, 1.0))
    assert ("O", "saboteur") in s100["sonde"] and ("O", "saboteur") in s100["nul"] and ("Jinstruit", "saboteur") in s100["enc"]
    i = vi.plan_de_notation("saboteur", (0.25, 0.5, 0.75, 1.0))
    assert ("O", "temoin") in i["sonde"] and ("A75", "honnete") in i["sonde"] and ("O", "S25") in i["nul"] and i["sc"] == []
    with pytest.raises(GardeArret):
        vi.plan_de_notation("S40", (0.25, 0.5))
