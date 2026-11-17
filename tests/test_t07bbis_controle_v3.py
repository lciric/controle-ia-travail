"""Essais R5 du contrôle carte-processeur v3 (`t07bbis.validation_imbriquee_v3` ; brouillon 6, plan, point 5 et liste d'arrêt ;
R-2919, voie (b) du majeur M2) et des versions neuves de la course (`marche_v3`, `scripts/amorce_bbis_v3.sh`,
`scripts/lancer_bbis_v3.sh`) et de la lecture (`lecture_v2` : R-PILE, point (7) de la section D, lecture du champ du contrôle ;
majeur M1).

- Chaque version neuve = la précédente + un différentiel déclaré (`aide_t07bbis_differentiels_v3.COUPLES`) : l'essai la refait et
  exige l'égalité exacte ; les essais des versions précédentes valent donc hors de ces lignes.
- Contrôle : aucune issue « sans objet » ; une sonde apprise pour le contrôle en échec (3 ou 300 époques, déterminisme compris)
  arrête ; tirage du couple parmi les sondes finales finies (toutes finies : même couple **et mêmes actions** que la v1, listes
  comparées élément par élément — m4 ; une non finie : tirage parmi les autres, même graine ; aucune : arrêt ; une seule fois).
- Lecture v2 : R-PILE écrite dès qu'une sonde finale lue est « attention » (cas sain : aucune ; cas déclenché : sonde ou ENC) ;
  point (7) ; champ du contrôle : sain, « sans objet », absent, non numérique, au-dessus de 10⁻⁴, déterminisme absent : arrêt.
- Marche v3 et lecture v2 de bout en bout en mode jouet (si la chaîne de T0.6 est présente).
Activations synthétiques seulement ; sur processeur."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest

import aide_t07bbis_differentiels_v3 as dif
from controle_ia.gardes import GardeArret
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.t07bbis import apprentissage_carte_v1 as ac
from controle_ia.t07bbis import commun_v1 as cm
from controle_ia.t07bbis import lecture_v2 as lv2
from controle_ia.t07bbis import validation_imbriquee_v1 as vi1
from controle_ia.t07bbis import validation_imbriquee_v3 as vi3

RACINE = Path(__file__).resolve().parents[1]
COURSE = ("src/controle_ia/t07bbis/validation_imbriquee_v3.py", "src/controle_ia/t07bbis/marche_v3.py",
          "scripts/amorce_bbis_v3.sh", "scripts/lancer_bbis_v3.sh", "src/controle_ia/t07bbis/lecture_v2.py")


@pytest.mark.parametrize("neuf", COURSE)
def test_version_neuve_egale_a_la_precedente_plus_le_differentiel_declare(neuf):
    ancien, couples = dif.COUPLES[neuf]
    assert (RACINE / neuf).read_text(encoding="utf-8") == dif.appliquer((RACINE / ancien).read_text(encoding="utf-8"), couples)


def test_amorce_v3_motifs_marche_v3_et_minimum_releve():
    t = (RACINE / "scripts/amorce_bbis_v3.sh").read_text(encoding="utf-8")
    motifs = t.split("MOTIFS='", 1)[1].split("'", 1)[0].splitlines()
    for v in ("v1", "v2", "v3"):
        assert f"/scripts/amorce_bbis_{v}.sh*" in motifs and f"/scripts/lancer_bbis_{v}.sh*" in motifs
    assert "/tests/test_t07bbis_*" in motifs and "/tests/aide_t07bbis_*" in motifs and "/*" in motifs
    assert t.count("controle_ia.t07bbis.marche_v3") == 3 and "t07bbis.marche_v2" not in t
    assert re.findall(r"^MIN_ESSAIS=(\d+)$", t, re.M) == [str(dif.MIN_ESSAIS_V3)] and dif.MIN_ESSAIS_V3 > 87


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
    return vi3.controle_deux_horizons(lot, seqs, y, 15, 1e-2, graine_de or GRAINES.__getitem__, ctrl,
                                      sondes_300=s300, epoques=k.pop("epoques", 40), **k)


def _cles(x):
    if isinstance(x, dict):
        for k, v in x.items():
            yield k
            yield from _cles(v)


def test_controle_v3_cas_sain_sans_aucune_issue_sans_objet():
    seqs, y, ctrl, lot, s300 = _jeu()
    r = _controle(seqs, y, ctrl, ac.LotCarte(seqs, "cpu"), s300)            # lot reconstruit, comme la course
    assert r["lineaire"]["epoques"] == 40 and r["attention"]["epoques"] == 3 and r["determinisme_attention"]["egal_au_bit"]
    assert max(r["lineaire"]["ecart_relatif_max"], r["attention"]["ecart_relatif_max"]) <= 1e-9
    assert "sans_objet" not in set(_cles(r))
    assert _controle(seqs, y, ctrl, lot, s300, familles=("lineaire",))["familles"] == ["lineaire"]      # variante (r1)


@pytest.mark.parametrize("cas", ["attention-3", "lineaire-300", "attention-300", "determinisme"])
def test_sonde_de_controle_en_echec_arrete(monkeypatch, cas):
    seqs, y, ctrl, lot, s300 = _jeu()
    vrai = ac.entrainer

    def echec(lot_, famille, nom, *a, epoques=cm.EPOQUES, **k):
        if ((cas == "attention-3" and famille == "attention" and epoques == 3)
                or (cas == "lineaire-300" and famille == "lineaire" and epoques == 40)
                or (cas == "attention-300" and famille == "attention" and epoques == 40 and not nom.endswith("-bis"))
                or (cas == "determinisme" and nom.endswith("-bis"))):
            raise ac.SondeEnEchec("perte non finie (simulée)")
        return vrai(lot_, famille, nom, *a, epoques=epoques, **k)
    monkeypatch.setattr(ac, "entrainer", echec)
    fournies = None if cas in ("lineaire-300", "attention-300") else s300            # sondes apprises par le contrôle
    with pytest.raises(GardeArret, match="erreur de chaîne"):
        _controle(seqs, y, ctrl, lot, fournies)


def test_artefacts_autre_graine_poids_alteres_non_determinisme(monkeypatch):
    seqs, y, ctrl, lot, s300 = _jeu()
    appels = []

    def alternee(f):
        appels.append(f)
        return GRAINES[f] + (len(appels) % 2)
    with pytest.raises(GardeArret, match="erreur de chaîne"):
        _controle(seqs, y, ctrl, lot, None, graine_de=alternee)
    lin = s300["lineaire"]
    faux = {"lineaire": SondeLineaireJetons(lin.nom, lin.couche, lin.agregation, lin.w * 1.01, lin.b, lin.q, lin.famille),
            "attention": s300["attention"]}
    with pytest.raises(GardeArret, match=r"lineaire à 40 époques : .*erreur de chaîne"):
        _controle(seqs, y, ctrl, lot, faux)
    vrai = ac.entrainer

    def instable(lot_, famille, nom, *a, **k):
        s = vrai(lot_, famille, nom, *a, **k)
        if nom.endswith("-bis"):
            s.w[0] = np.nextafter(s.w[0], np.inf)
        return s
    monkeypatch.setattr(ac, "entrainer", instable)
    with pytest.raises(GardeArret, match="non déterministe"):
        _controle(seqs, y, ctrl, lot, s300)


# ------------------------------------------------------------------------------------------------------------ tirage

@pytest.fixture(scope="module")
def jouet():
    from test_t07bbis_apprentissage_v1 import ActsJouet
    from controle_ia.t06.test_croise import partition_plis
    acts = ActsJouet()
    g = cm.Graines(2 ** 100 + 7, reelle=False)
    ctx = vi3.Contexte(acts, g, acts.couches, "cpu", reelle=False, epoques=10, n_plis_internes=3)
    taches = sorted({acts.tache(k) for k in acts.cles("O", "honnete")})
    plis = partition_plis(taches, 3)
    pos = {"P-S100": "S100", "P-instruit": "saboteur"}
    couples = [(c, k) for c in ("P-S100", "P-instruit") for k in (0, 1)]
    res = {(c, k): vi3.apprendre_source(ctx, c, pos[c], vi3.plan_de_notation(pos[c], (0.5, 1.0)), k, plis, taches,
                                        n_reetiquetages=2, n_directions=4) for c, k in couples}
    return ctx, plis, pos, res, couples


def _graines():
    return cm.Graines(2 ** 100 + 7, reelle=False)


def test_tirage_toutes_finies_meme_couple_et_memes_actions_que_la_v1(jouet, monkeypatch):
    ctx, plis, pos, res, couples = jouet
    vues = []
    vrai = vi1._sequences

    def espion(acts, actions, couche):
        vues.append(list(actions))
        return vrai(acts, actions, couche)
    monkeypatch.setattr(vi1, "_sequences", espion)
    c1 = vi1.ControleCarte(_graines(), couples, n_actions=10)
    r1 = c1.apres(ctx, *c1.couple, pos[c1.couple[0]], res[c1.couple], plis)
    c3 = vi3.ControleCarte(_graines(), couples, n_actions=10)
    r3 = c3.jouer(ctx, {c: (pos[c[0]], res[c]) for c in couples}, plis)
    assert c3.couple == c1.couple and r3["tirage"] == {"couples": 4, "sondes_finales_finies": 4}
    assert len(vues) == 2 and vues[0] == vues[1] and len(vues[0]) == r1["actions"] == r3["actions"] == 10      # m4
    assert r3["attention"]["epoques"] == 3 and r3["determinisme_attention"]["egal_au_bit"] and "sans_objet" not in set(_cles(r3))
    with pytest.raises(GardeArret, match="une seule fois"):
        c3.jouer(ctx, {c: (pos[c[0]], res[c]) for c in couples}, plis)


def test_tirage_parmi_les_sondes_finales_finies_meme_graine_et_aucune_arret(jouet):
    ctx, plis, pos, res, couples = jouet
    tire_v1 = vi1.ControleCarte(_graines(), couples).couple
    s = res[tire_v1]["sonde"]
    nan = {**res[tire_v1], "sonde": SondeLineaireJetons(s.nom, s.couche, s.agregation, s.w * np.nan, s.b, s.q, s.famille)}
    for manque in ({"echec": "sonde finale en échec (simulée)"}, nan):
        sources = {c: (pos[c[0]], manque if c == tire_v1 else res[c]) for c in couples}
        finis = [c for c in sorted(couples) if c != tire_v1]
        attendu = finis[int(_graines().rng("bbis/egalite-carte").integers(0, len(finis)))]
        c3 = vi3.ControleCarte(_graines(), couples, n_actions=10)
        r = c3.jouer(ctx, sources, plis)
        assert c3.couple == attendu != tire_v1 and r["tirage"]["sondes_finales_finies"] == 3
    with pytest.raises(GardeArret, match="aucun des 4 couples"):
        vi3.ControleCarte(_graines(), couples).jouer(ctx, {c: (pos[c[0]], {"echec": "x"}) for c in couples}, plis)
    assert not vi3.sonde_finie({"echec": "x"}) and not vi3.sonde_finie(nan) and vi3.sonde_finie(res[tire_v1])


# ------------------------------------------------------------------------------------------------------------ lecture v2

def _doc(controle, variante=None, sources=None):
    return {"controle_carte_processeur": controle, "variante": variante,
            "sources": sources if sources is not None else {"P-S50": {"e0": {"famille": "lineaire", "enc": {"reglage": "lineaire-c7-l2_0.1"}}}}}


SAIN = {"lineaire": {"ecart_relatif_max": 2e-8, "epoques": 300}, "attention": {"ecart_relatif_max": 3e-7, "epoques": 3},
        "determinisme_attention": {"egal_au_bit": True, "epoques": 300}, "cellule": "P-S50", "pli": 0}


def test_lecture_v2_champ_du_controle_sain_et_artefacts():
    r = lv2.exiger_controle_carte(_doc(SAIN))
    assert r["ecarts"] == {"lineaire": 2e-8, "attention": 3e-7} and r["determinisme_attention"]
    assert lv2.exiger_controle_carte(_doc({"lineaire": {"ecart_relatif_max": 1e-9}}, variante="r1"))["ecarts"] == {"lineaire": 1e-9}
    artefacts = [None, {**SAIN, "attention": {"sans_objet": "sonde de contrôle en échec"}},
                 {**SAIN, "sans_objet": "sonde du couple tiré en échec"}, {k: v for k, v in SAIN.items() if k != "attention"},
                 {**SAIN, "lineaire": {"ecart_relatif_max": "2e-8"}}, {**SAIN, "lineaire": {"ecart_relatif_max": float("nan")}},
                 {**SAIN, "attention": {"ecart_relatif_max": 2e-4}}, {**SAIN, "lineaire": {"ecart_relatif_max": True}},
                 {k: v for k, v in SAIN.items() if k != "determinisme_attention"},
                 {**SAIN, "determinisme_attention": {"egal_au_bit": False}}]
    for a in artefacts:
        with pytest.raises(lv2.RefusLecture, match="arrêt de la lecture"):
            lv2.exiger_controle_carte(_doc(a))


def test_lecture_v2_r_pile_et_point_7_de_la_section_d():
    assert lv2.reserve_pile(_doc(SAIN)) == []                                   # aucune sonde « attention » lue
    att = {"P-S50": {"e0": {"famille": "attention", "enc": {"reglage": "lineaire-c7-l2_0.1"}},
                     "e1": {"famille": "lineaire", "enc": {"reglage": "attention-c15-l2_0.01"}}},
           "P-S100": {"e0": {"echec": "x", "famille": "attention"}}}
    r = lv2.reserve_pile(_doc(SAIN, sources=att))
    assert len(r) == 1 and r[0].startswith(lv2.RESERVES_FIXES["R-PILE"]) and "P-S50 e0, P-S50 e1 (ENC)" in r[0]
    assert lv2.RESERVES_FIXES["R-PILE"].startswith("R-PILE : sonde « attention » reproductible au bit près sur la même pile")
    assert "(7) une aire de la famille « attention » est celle d'une sonde parmi celles" in lv2.SECTION_D
    assert lv2.SECTION_D.count("(6) le libellé d'information ne dit pas « plafond tient » ; (7)") == 1
    b6 = RACINE / "brouillons" / "T0.7-etape-B-bis-v1" / "T0.7-etape-B-bis-v1-brouillon6.md"
    if b6.exists():                                                             # phrase recopiée du texte (hors de l'instance)
        t = b6.read_text(encoding="utf-8")
        assert lv2.RESERVES_FIXES["R-PILE"].split(" : ", 1)[1] in t
        assert ("(7) une aire de la famille « attention » est celle d'**une** sonde parmi celles que rendrait le même "
                "apprentissage sous d'autres arrondis (réserve R-PILE)") in t


# ------------------------------------------------------------------------------------------------------------ bout en bout

def _t(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def _ligne(cle, date, chemin, sha):
    return f"| {cle} | {date} | {chemin} | {sha} |\n"


def test_marche_v3_et_lecture_v2_de_bout_en_bout_en_mode_jouet(tmp_path_factory):
    import aide_t07bbis_jouet_v1 as aide
    from controle_ia.scellement import empreinte, sceller
    from controle_ia.t07bbis import marche_v3
    from controle_ia.t07bbis import registre_bbis_v1 as rb
    if not aide.disponible():
        pytest.skip("chaîne de T0.6 absente de ce clone")
    run_b, entropie = "20261118-090000-bbis-jouet", 2 ** 100 + 11
    d = aide.course_jouet(tmp_path_factory.mktemp("depot-bbis-v3"))
    r = marche_v3.marche(d, aide.RUN, run_b, entropie, d.parent / f"{d.name}-travail", "cpu",
                         essai={"epoques": 15, "n_plis_internes": 3, "n_directions": 12, "n_reetiquetages": 3, "n_controle": 6,
                                "n_chemin": 3})
    assert r.get("scores_ecrits"), r
    doc = json.loads((d / r["sondes_bbis"]).read_text(encoding="utf-8"))
    c = doc["controle_carte_processeur"]
    assert c["lineaire"]["epoques"] == 15 and c["attention"]["epoques"] == 3 and c["determinisme_attention"]["egal_au_bit"]
    assert c["tirage"]["sondes_finales_finies"] == c["tirage"]["couples"] and "sans_objet" not in set(_cles(c))
    v = d / "docs" / "verdicts" / "verdict-p3bis-jouet.md"
    v.parent.mkdir(parents=True)
    v.write_text("verdict jouet\n", encoding="utf-8")
    sha_issue = aide.sceller_json(d, "docs/verdicts/issue-p3bis-jouet.json",
                                  {"issue": "vu", "ligne": 5, "verdict": "docs/verdicts/verdict-p3bis-jouet.md",
                                   "verdict_sha256": empreinte(v)})
    sha_m = (d / "runs" / aide.RUN / "manifeste.json.sha256").read_text(encoding="utf-8").split()[0]
    (d / "registres").mkdir(exist_ok=True)
    (d / rb.REGISTRE_PARTAGE).write_text(
        "# registre jouet\n\n" + _ligne("RUN-CONFIRMATION-T06", "2026-11-12T05:00:00Z", f"runs/{aide.RUN}/manifeste.json", sha_m)
        + _ligne("VERDICT-P3BIS", "2026-11-13T05:00:00Z", "docs/verdicts/issue-p3bis-jouet.json", sha_issue), encoding="utf-8")
    sha_abs = aide.sceller_json(d, "registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json", {"absents": True})
    sha_fiche = aide.sceller_json(d, "registres/t07-etape-b-bis/code-bbis-v1.json",
                                  {"commit": "c" * 40, "fichiers": {"src/x.py": "a" * 64}, "entropie": str(entropie),
                                   "epreuve_niveau": {"chemin": "e.json", "sha256": "b" * 64, "niveau_decisif_retenu": 0.99},
                                   "niveau_decisif": 0.99})
    g = d / "registres" / "go-extraits" / "GO-BBIS-v1.md"
    g.parent.mkdir(parents=True)
    g.write_text("| GO-2026-11-14-09 | extrait jouet |\n", encoding="utf-8")
    for cle, date, chemin, sha in [("SCELLEMENT-BBIS", "2026-11-14T12:30:30Z", cm.TEXTE, cm.TEXTE_SHA256),
                                   ("ABSENCE-B-BBIS", "2026-11-14T12:30:30Z", "registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json",
                                    sha_abs),
                                   ("CODE-BBIS", "2026-11-17T10:00:00Z", "registres/t07-etape-b-bis/code-bbis-v1.json", sha_fiche),
                                   ("GO-BBIS", "2026-11-17T11:00:00Z", "registres/go-extraits/GO-BBIS-v1.md", sceller(g)),
                                   ("SCORES-BBIS", "2026-11-18T20:00:00Z", r["sondes_bbis"], r["sondes_bbis_sha256"])]:
        rb.ajouter_ligne_propre(d, rb.REGISTRE_PROPRE, cle, _t(date), chemin, sha)
    aide.git(d, "add", "-A")
    aide.git(d, "commit", "-q", "-m", "registres jouets de B bis")
    res = lv2.lire(d, aide.RUN, run_b, _t("2026-11-19T09:00:00Z"), essai={"n_directions": 12, "n_nul": 3, "n_tirages": 60})
    assert "garde" not in res and res["controle_carte_processeur"]["determinisme_attention"]
    assert "(7)" in res["section_D"]
    attention = any(m.get("famille") == "attention" or str((m.get("enc") or {}).get("reglage", "")).startswith("attention-")
                    for par in doc["sources"].values() for m in par.values() if "echec" not in m)
    assert any(x.startswith("R-PILE") for x in res["reserves"]) == attention
    faux = {**doc, "controle_carte_processeur": {**c, "attention": {"sans_objet": "simulé"}}}
    with pytest.raises(lv2.RefusLecture, match="sans objet"):
        lv2.exiger_controle_carte(faux)
