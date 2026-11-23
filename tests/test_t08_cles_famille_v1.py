"""R-5131 (tentative 1 de la course de T0.8, préalable P3) : familles de clés `SCELLEMENT-T08[-V<n>]` et
`CODE-T08[-V<n>]` au registre des scellements. Une seule ligne de chaque famille correspond (empreinte du texte passé ;
commit du marqueur), ni zéro ni deux ; une clé `…-V` mal formée arrête ; antériorité inchangée. Essais sur
`lecture_v1.passage_a_blanc_reel` (P3) et `controles_texte_et_registre` (lecture), registre factice."""
from __future__ import annotations

import re

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import empreinte
from controle_ia.t08 import entrees_v1 as en
from controle_ia.t08 import lecture_v1 as lv

import test_t08_gardes_corrections_v1 as G

D1, D2, D3 = "2026-11-20T09:00:00Z", "2026-11-20T10:00:00Z", "2026-11-20T11:00:00Z"


def _monde(tmp_path, version: int):
    """Texte scellé de la version `version` (1, 2 ou 3) : mêmes marqueurs sauf le commit du code."""
    mq = G._marqueurs()
    commits = {1: "b" * 40, 2: "c" * 40, 3: "d" * 40}
    mq = dict(mq, COMMIT_CODE_T08=commits[version])
    p = G._prereg(tmp_path, mq, f"texte-v{version}.md")
    return mq, p, commits


def _lignes(mq, shas: dict, commits: dict, *versions, plus=()):
    """Lignes du registre : les lignes de 7b et de la pièce, et pour chaque version la paire SCELLEMENT/CODE."""
    l = [x for x in G._lignes_reelles(mq, "0" * 64) if x[0] not in ("SCELLEMENT-T08", "CODE-T08")]
    dates = {1: D1, 2: D2, 3: D3}
    for v in versions:
        suf = "" if v == 1 else f"-V{v}"
        l += [(f"SCELLEMENT-T08{suf}", dates[v], f"prereg/texte-v{v}.md", shas[v]),
              (f"CODE-T08{suf}", dates[v], f"docs/empreintes-v{v}.md", commits[v])]
    return l + list(plus)


def _shas(tmp_path, commits):
    out = {}
    for v in (1, 2, 3):
        mq = dict(G._marqueurs(), COMMIT_CODE_T08=commits[v])
        out[v] = empreinte(G._prereg(tmp_path, mq, f"texte-v{v}.md"))
    return out


def test_famille_cas_sains(tmp_path):
    """v1 seul ; v1 et v2, la v2 seule correspond ; v1, v2, v3 (registre réel attendu au rendez-vous), la v3 seule
    correspond. La ligne `SCELLEMENT-T08-BASE-A` n'est pas de la famille."""
    mq1, p1, commits = _monde(tmp_path, 1)
    shas = _shas(tmp_path, commits)
    base_a = [("SCELLEMENT-T08-BASE-A", D1, "prereg/T0.8-base-A.md", "a" * 64)]
    r = lv.passage_a_blanc_reel(mq1, G._registre(tmp_path, "v1", _lignes(mq1, shas, commits, 1, plus=base_a)), p1,
                                G.MAINTENANT)
    assert r["SCELLEMENT-T08"]["cle"] == "SCELLEMENT-T08" and r["CODE-T08"]["cle"] == "CODE-T08"
    mq2, p2, _ = _monde(tmp_path, 2)
    r = lv.passage_a_blanc_reel(mq2, G._registre(tmp_path, "v12", _lignes(mq2, shas, commits, 1, 2, plus=base_a)), p2,
                                G.MAINTENANT)
    assert (r["SCELLEMENT-T08"]["cle"], r["CODE-T08"]["cle"]) == ("SCELLEMENT-T08-V2", "CODE-T08-V2")
    assert r["CODE-T08"]["commit"] == "c" * 40 and r["SCELLEMENT-T08"]["sha256"] == shas[2]
    mq3, p3, _ = _monde(tmp_path, 3)
    reg = G._registre(tmp_path, "v123", _lignes(mq3, shas, commits, 1, 2, 3, plus=base_a))
    r = lv.passage_a_blanc_reel(mq3, reg, p3, G.MAINTENANT)
    assert (r["SCELLEMENT-T08"]["cle"], r["CODE-T08"]["cle"]) == ("SCELLEMENT-T08-V3", "CODE-T08-V3")
    assert r["registre"]["mal_formees_lues"] == []                 # CODE-T08-V<n> à la forme « commit » : lue
    # antériorité inchangée : la ligne retenue (v3) postérieure au passage arrête
    tard = [x if x[0] != "CODE-T08-V3" else (x[0], "2026-11-20T12:00:01Z", *x[2:]) for x in
            _lignes(mq3, shas, commits, 1, 2, 3)]
    with pytest.raises(GardeArret, match="ligne CODE-T08-V3 .* non antérieure"):
        lv.passage_a_blanc_reel(mq3, G._registre(tmp_path, "tard", tard), p3, G.MAINTENANT)


def test_famille_artefacts(tmp_path):
    """Deux lignes qui correspondent ; aucune ; clé mal formée (`SCELLEMENT-T08-VX`, `CODE-T08-V0`, `CODE-T08-V02`)."""
    mq2, p2, commits = _monde(tmp_path, 2)
    shas = _shas(tmp_path, commits)
    cas = {
        "deux lignes SCELLEMENT à l'empreinte du texte": (
            _lignes(mq2, shas, commits, 1, 2, plus=[("SCELLEMENT-T08-V3", D3, "prereg/x.md", shas[2])]),
            r"famille SCELLEMENT-T08 : 2 lignes"),
        "deux lignes CODE qui citent le commit": (
            _lignes(mq2, shas, commits, 1, 2, plus=[("CODE-T08-V3", D3, "docs/x.md", commits[2])]),
            r"famille CODE-T08 : 2 lignes"),
        "aucune ligne SCELLEMENT à l'empreinte du texte": (_lignes(mq2, shas, commits, 1), "autre texte scellé"),
        "aucune ligne CODE qui cite le commit": (
            [x for x in _lignes(mq2, shas, commits, 1, 2) if x[0] != "CODE-T08-V2"], "ne cite pas le commit"),
        "clé SCELLEMENT-T08-VX": (
            _lignes(mq2, shas, commits, 1, 2, plus=[("SCELLEMENT-T08-VX", D3, "prereg/x.md", "9" * 64)]),
            "clé SCELLEMENT-T08-VX mal formée"),
        "clé CODE-T08-V0": (_lignes(mq2, shas, commits, 1, 2, plus=[("CODE-T08-V0", D3, "docs/x.md", "9" * 64)]),
                            "clé CODE-T08-V0 mal formée"),
        "clé CODE-T08-V02": (_lignes(mq2, shas, commits, 1, 2, plus=[("CODE-T08-V02", D3, "docs/x.md", "9" * 64)]),
                             "clé CODE-T08-V02 mal formée"),
        "aucune ligne de la famille CODE": (
            [x for x in _lignes(mq2, shas, commits, 1, 2) if not x[0].startswith("CODE-T08")], "ligne CODE-T08 absente"),
    }
    for nom, (lignes, motif) in cas.items():
        reg = G._registre(tmp_path, re.sub(r"[^A-Za-z0-9]", "-", nom), lignes)
        with pytest.raises(GardeArret, match=motif):
            lv.passage_a_blanc_reel(mq2, reg, p2, G.MAINTENANT)


def test_lignes_famille_direct(tmp_path):
    """`entrees_v1.lignes_famille` : famille et non-famille ; base inconnue refusée."""
    p = G._registre(tmp_path, "direct", [("SCELLEMENT-T08", D1, "a", "1" * 64), ("SCELLEMENT-T08-V2", D2, "b", "2" * 64),
                                         ("SCELLEMENT-T08-BASE-A", D1, "c", "3" * 64), ("CODE-T08-V2", D2, "d", "e" * 40)])
    reg = en.lire_registre_scellements(p)
    assert sorted(en.lignes_famille(reg, "SCELLEMENT-T08")) == ["SCELLEMENT-T08", "SCELLEMENT-T08-V2"]
    assert en.lignes_famille(reg, "CODE-T08") == {"CODE-T08-V2": {"date": "2026-11-20T10:00:00+00:00", "chemin": "d",
                                                                  "sha256": None, "commit": "e" * 40}}
    with pytest.raises(GardeArret, match="inconnue"):
        en.lignes_famille(reg, "COURSE-T08")
