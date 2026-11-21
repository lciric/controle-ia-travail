"""Essais R5 du contrôle carte-processeur aux deux horizons (`t07bbis.validation_imbriquee_v2` ; brouillon 4 du texte de B bis,
plan, point 5 ; R-2917) et des versions neuves qui l'appellent dans la course (`marche_v2`, `scripts/amorce_bbis_v2.sh`,
`scripts/lancer_bbis_v2.sh`).

- Chaque version neuve est **la v1 plus un différentiel déclaré ici** (couples « ancien, nouveau, nombre d'occurrences ») : l'essai
  refait la v2 depuis la v1 et exige l'égalité exacte ; les essais de la v1 (blocs marqués de l'amorce et du lanceur, gardes de la
  marche) valent donc pour la v2 hors de ces lignes.
- Contrôle : cas sain (deux familles ; linéaire à l'horizon de la marche, attention à 3 époques, déterminisme de l'attention) ;
  artefacts : autre graine entre la carte et le processeur, poids altérés de 1 % (linéaire, puis attention à 3 époques),
  non-déterminisme simulé (seconde sonde « attention » perturbée d'un arrondi) ; variante (r1) ; horizon hors bornes ; sonde de
  contrôle en échec (« sans objet », sans arrêt) ; même tirage du couple et des actions que la v1 ; marche de bout en bout en mode
  jouet (si la chaîne de T0.6 est présente).
Activations synthétiques seulement ; « cuda » n'est pas disponible ici : le contrôle est éprouvé sur processeur (même code)."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import commun_v1 as cm
from controle_ia.t07bbis import validation_imbriquee_v1 as vi1
from controle_ia.t07bbis import validation_imbriquee_v2 as vi2

RACINE = Path(__file__).resolve().parents[1]
ENTETE_MARCHE = ("« Données gardées »), v2 : la v1, dont l'apprentissage appelle `validation_imbriquee_v2` (contrôle\n"
                 "carte-processeur aux deux horizons : linéaire à 300 époques, attention à 3 époques, déterminisme de l'attention à\n"
                 "300 époques ; brouillon 4 du texte, plan, point 5 ; R-2917) ; rien d'autre ne change (la v1 reste, R12).\n")
COUPLES = {
    "src/controle_ia/t07bbis/marche_v2.py": ("src/controle_ia/t07bbis/marche_v1.py", [
        ("« Données gardées »), v1.\n", ENTETE_MARCHE, 1),
        ("(`validation_imbriquee_v1.apprendre_source`,", "(`validation_imbriquee_v2.apprendre_source`, celle de la v1,", 1),
        ("scripts/amorce_bbis_v1.sh", "scripts/amorce_bbis_v2.sh", 3),
        ("interface lue par `validation_imbriquee_v1`", "interface lue par `validation_imbriquee_v2` (celle de la v1)", 1),
        ("python -m controle_ia.t07bbis.marche_v1", "python -m controle_ia.t07bbis.marche_v2", 2),
        ("from . import validation_imbriquee_v1 as vi", "from . import validation_imbriquee_v2 as vi", 1)]),
    "scripts/amorce_bbis_v2.sh": ("scripts/amorce_bbis_v1.sh", [
        ("# Amorce de l'instance de l'étape B bis de T0.7, v1 (",
         "# Amorce de l'instance de l'étape B bis de T0.7, v2 (la v1, dont la marche est `controle_ia.t07bbis.marche_v2` :\n"
         "# contrôle carte-processeur aux deux horizons, R-2917 ; blocs marqués identiques à ceux de la v1 ; la v1 reste, R12) (", 1),
        ("passée par scripts/lancer_bbis_v1.sh", "passée par scripts/lancer_bbis_v2.sh", 1),
        ("#   8. marche (`controle_ia.t07bbis.marche_v1`,", "#   8. marche (`controle_ia.t07bbis.marche_v2`,", 1),
        ("(lancer_bbis_v1.sh verifier-destruction)", "(lancer_bbis_v2.sh verifier-destruction)", 1),
        ("/scripts/lancer_bbis_v1.sh*\n", "/scripts/lancer_bbis_v1.sh*\n/scripts/amorce_bbis_v2.sh*\n/scripts/lancer_bbis_v2.sh*\n", 1),
        ("-m controle_ia.t07bbis.marche_v1 \\", "-m controle_ia.t07bbis.marche_v2 \\", 1)]),
    "scripts/lancer_bbis_v2.sh": ("scripts/lancer_bbis_v1.sh", [
        ("# Chaîne de session de l'étape B bis de T0.7, v1 (",
         "# Chaîne de session de l'étape B bis de T0.7, v2 (la v1, qui passe l'amorce v2 : marche v2, contrôle carte-processeur\n"
         "# aux deux horizons, R-2917 ; la v1 reste, R12) (", 1),
        ("amorce_bbis_v1.sh", "amorce_bbis_v2.sh", 7),
        ("lancer_bbis_v1.sh", "lancer_bbis_v2.sh", 3)]),
}


def appliquer(texte: str, couples) -> str:
    for ancien, nouveau, n in couples:
        assert texte.count(ancien) == n, (ancien[:70], texte.count(ancien), n)
        texte = texte.replace(ancien, nouveau)
    return texte


@pytest.mark.parametrize("v2", sorted(COUPLES))
def test_v2_egale_a_la_v1_plus_le_differentiel_declare(v2):
    v1, couples = COUPLES[v2]
    attendu = appliquer((RACINE / v1).read_text(encoding="utf-8"), couples)
    assert (RACINE / v2).read_text(encoding="utf-8") == attendu


def test_amorce_v2_extrait_les_deux_versions_et_lance_la_marche_v2():
    t = (RACINE / "scripts/amorce_bbis_v2.sh").read_text(encoding="utf-8")
    motifs = t.split("MOTIFS='", 1)[1].split("'", 1)[0].splitlines()
    for p in ("/scripts/amorce_bbis_v1.sh*", "/scripts/lancer_bbis_v1.sh*", "/scripts/amorce_bbis_v2.sh*",
              "/scripts/lancer_bbis_v2.sh*", "/tests/test_t07bbis_*", "/src/"):
        assert p in motifs
    assert t.count("controle_ia.t07bbis.marche_v2") == 3 and "controle_ia.t07bbis.marche_v1" not in t
    assert "MIN_ESSAIS=87\n" in t                                           # inchangé


# ------------------------------------------------------------------------------------------------------------ contrôle

def _sacs(rng, n=24, d=6):
    seqs, y = [], []
    for i in range(n):
        t = int(rng.integers(2, 7))
        x = rng.standard_normal((t, d))
        if i % 2:
            x[int(rng.integers(0, t)), 0] += 2.0
        seqs.append(x.astype(np.float32))
        y.append(i % 2)
    return seqs, np.array(y)


GRAINES = {"lineaire": 11, "attention": 12}


def _jeu(epoques=40):
    rng = np.random.default_rng(3)
    seqs, y = _sacs(rng)
    ctrl, _ = _sacs(rng, n=20)
    lot = ac.LotCarte(seqs, "cpu")
    s300 = {f: ac.entrainer(lot, f, f"s-{f}", 15, y, 1e-2, GRAINES[f], epoques=epoques) for f in cm.FAMILLES}
    return seqs, y, ctrl, lot, s300


def _controle(seqs, y, ctrl, lot, s300=None, graine_de=None, **k):
    return vi2.controle_deux_horizons(lot, seqs, y, 15, 1e-2, graine_de or GRAINES.__getitem__, ctrl,
                                      sondes_300=s300, epoques=k.pop("epoques", 40), **k)


def test_controle_deux_horizons_cas_sain():
    seqs, y, ctrl, lot, s300 = _jeu()
    r = _controle(seqs, y, ctrl, lot, s300)
    assert r["familles"] == ["lineaire", "attention"] and r["tolerance"] == cm.TOLERANCE_CARTE
    assert r["lineaire"]["epoques"] == 40 and r["lineaire"]["ecart_relatif_max"] <= 1e-9
    assert r["attention"]["epoques"] == vi2.EPOQUES_CONTROLE_ATTENTION == 3 and r["attention"]["ecart_relatif_max"] <= 1e-9
    assert r["determinisme_attention"] == {"epoques": 40, "egal_au_bit": True}
    assert r["lineaire"]["reglage"] == "lineaire-c15-l2_0.01" and r["attention"]["reglage"] == "attention-c15-l2_0.01"
    r2 = _controle(seqs, y, ctrl, lot, None)                                 # sondes de 300 époques apprises par le contrôle
    assert r2["lineaire"]["ecart_relatif_max"] == r["lineaire"]["ecart_relatif_max"]


def test_artefact_autre_graine_entre_carte_et_processeur():
    seqs, y, ctrl, lot, _ = _jeu()
    appels = []

    def alternee(f):                                       # la carte et le processeur ne reçoivent pas la même graine
        appels.append(f)
        return GRAINES[f] + (len(appels) % 2)
    with pytest.raises(GardeArret, match="erreur de chaîne"):
        _controle(seqs, y, ctrl, lot, None, graine_de=alternee)


def test_artefact_poids_alteres_de_1_pour_cent(monkeypatch):
    seqs, y, ctrl, lot, s300 = _jeu()
    lin = s300["lineaire"]
    faux = {"lineaire": SondeLineaireJetons(lin.nom, lin.couche, lin.agregation, lin.w * 1.01, lin.b, lin.q, lin.famille),
            "attention": s300["attention"]}
    with pytest.raises(GardeArret, match=r"lineaire à 40 époques : .*erreur de chaîne"):
        _controle(seqs, y, ctrl, lot, faux)
    vrai = ac.entrainer

    def altere_a_3(lot_, famille, nom, *a, epoques=cm.EPOQUES, **k):
        s = vrai(lot_, famille, nom, *a, epoques=epoques, **k)
        if famille == "attention" and epoques == 3:
            return SondeLineaireJetons(s.nom, s.couche, s.agregation, s.w * 1.01, s.b, s.q, s.famille)
        return s
    monkeypatch.setattr(ac, "entrainer", altere_a_3)
    with pytest.raises(GardeArret, match=r"attention à 3 époques : .*erreur de chaîne"):
        _controle(seqs, y, ctrl, lot, s300)


def test_artefact_non_determinisme_simule(monkeypatch):
    seqs, y, ctrl, lot, s300 = _jeu()
    vrai = ac.entrainer

    def instable(lot_, famille, nom, *a, **k):
        s = vrai(lot_, famille, nom, *a, **k)
        if nom.endswith("-bis"):                            # seconde sonde « attention » de 300 époques
            s.w[0] = np.nextafter(s.w[0], np.inf)
        return s
    monkeypatch.setattr(ac, "entrainer", instable)
    with pytest.raises(GardeArret, match="non déterministe"):
        _controle(seqs, y, ctrl, lot, s300)
    with pytest.raises(GardeArret, match="non déterministe"):          # sans sonde fournie : deux apprentissages du contrôle
        _controle(seqs, y, ctrl, lot, None)


def test_variante_r1_horizon_et_sonde_de_controle_en_echec(monkeypatch):
    seqs, y, ctrl, lot, s300 = _jeu()
    r = _controle(seqs, y, ctrl, lot, s300, familles=("lineaire",))
    assert r["familles"] == ["lineaire"] and "attention" not in r and "determinisme_attention" not in r
    for ep_att in (0, 40, 41):
        with pytest.raises(GardeArret, match="horizon"):
            _controle(seqs, y, ctrl, lot, s300, epoques_attention=ep_att)
    with pytest.raises(GardeArret, match="familles"):
        _controle(seqs, y, ctrl, lot, s300, familles=("perceptron",))
    vrai = ac.entrainer

    def echec_a_3(lot_, famille, nom, *a, epoques=cm.EPOQUES, **k):
        if famille == "attention" and epoques == 3:
            raise ac.SondeEnEchec("perte non finie (simulée)")
        return vrai(lot_, famille, nom, *a, epoques=epoques, **k)
    monkeypatch.setattr(ac, "entrainer", echec_a_3)
    r = _controle(seqs, y, ctrl, lot, s300)
    assert "sans_objet" in r["attention"] and r["lineaire"]["ecart_relatif_max"] <= 1e-9 and "determinisme_attention" not in r


def test_controle_carte_v2_meme_tirage_que_la_v1_et_deux_horizons_sur_jouet():
    from test_t07bbis_apprentissage_v1 import ActsJouet
    from controle_ia.t06.test_croise import partition_plis
    acts = ActsJouet()
    g = cm.Graines(2 ** 100 + 7, reelle=False)
    ctx = vi2.Contexte(acts, g, acts.couches, "cpu", reelle=False, epoques=10, n_plis_internes=3)
    taches = sorted({acts.tache(k) for k in acts.cles("O", "honnete")})
    plis = partition_plis(taches, 3)
    couples = [(c, k) for c in ("P-S100", "P-instruit") for k in (0, 1)]
    c1, c2 = vi1.ControleCarte(cm.Graines(2 ** 100 + 7, reelle=False), couples, n_actions=10), vi2.ControleCarte(g, couples, 10)
    assert c1.couple == c2.couple
    cellule, k = c2.couple
    pos = {"P-S100": "S100", "P-instruit": "saboteur"}[cellule]
    res = vi2.apprendre_source(ctx, cellule, pos, vi2.plan_de_notation(pos, (0.5, 1.0)), k, plis, taches, n_reetiquetages=2,
                               n_directions=4)
    r = c2.apres(ctx, cellule, k, pos, res, plis)
    assert r is c2.resultat and (r["cellule"], r["pli"]) == c2.couple and r["actions"] == 10
    assert r["lineaire"]["epoques"] == 10 and r["attention"]["epoques"] == 3 and r["determinisme_attention"]["egal_au_bit"]
    assert r["reglage_retenu"] == res["reglage"]["nom"] and max(r["lineaire"]["ecart_relatif_max"],
                                                                 r["attention"]["ecart_relatif_max"]) <= 1e-4
    r1 = c1.apres(ctx, cellule, k, pos, res, plis)                       # la v1 tire les mêmes actions de contrôle
    assert r1["actions"] == r["actions"] and c2.apres(ctx, cellule, k, pos, res, plis) is None   # joué une seule fois


def test_marche_v2_de_bout_en_bout_en_mode_jouet(tmp_path_factory):
    import aide_t07bbis_jouet_v1 as aide
    from controle_ia.t07bbis import marche_v2
    if not aide.disponible():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    d = aide.course_jouet(tmp_path_factory.mktemp("depot-bbis-v2"))
    essai = {"epoques": 15, "n_plis_internes": 3, "n_directions": 12, "n_reetiquetages": 3, "n_controle": 6, "n_chemin": 3}
    r = marche_v2.marche(d, aide.RUN, "20261118-090000-bbis-jouet", 2 ** 100 + 11, d.parent / f"{d.name}-travail", "cpu",
                         essai=essai)
    assert r.get("scores_ecrits"), r
    c = json.loads((d / r["sondes_bbis"]).read_text(encoding="utf-8"))["controle_carte_processeur"]
    assert c["lineaire"]["epoques"] == 15 and c["attention"]["epoques"] == 3 and c["determinisme_attention"]["egal_au_bit"]
    assert max(c["lineaire"]["ecart_relatif_max"], c["attention"]["ecart_relatif_max"]) <= 1e-4 and c["actions"] == 6
