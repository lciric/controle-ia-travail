"""Démonstration de la contre-lecture 3 (CL3-01), données jouet seulement.

Un run décisif jouet de P4 est lancé sous un préenregistrement scellé ; AUCUN verdict complété de P3 n'est versé. La
lecture décisive est refusée (report), comme le veut le texte. La même lecture, sans `--prereg`, lit le run décisif et
écrit C1 : la garde « lecture refusée avant le verdict complété de P3 » se contourne en omettant un argument.
"""
import pytest

import instrument_p4_v1 as ip
import lecture_p4_v1 as lp
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import lire_manifeste
from test_gardes_p4_v1 import (ENTROPIE_JOUET, PREREG, candidat_jouet, code_sous_la_racine,  # noqa: F401
                               committer)


def test_lecture_sans_prereg_lit_un_run_decisif_sans_verdict_complete(tmp_path_factory, tmp_path, monkeypatch,
                                                                       code_sous_la_racine):  # noqa: F811
    c = candidat_jouet(tmp_path_factory, tmp_path / "d")
    d = c["depot"]
    monkeypatch.setattr(ip, "COMMIT_P3", c["tete"])
    r = ip.executer(c["config"], d, "20261020-180000-p4-decisif", c["prereg"])
    assert r["arret"] is None
    m, _ = lire_manifeste(d / "runs" / "20261020-180000-p4-decisif" / "manifeste.json")
    assert m["decisif"] is True
    committer(d, "run décisif, sans verdict complété de P3")
    # mode décisif : refusé (report), rien d'écrit
    with pytest.raises(GardeArret, match="verdict complété de P3 absent"):
        lp.analyser(d, "20261020-180000-p4-decisif", "20261020-181000-lecture-p4", PREREG, entropie=ENTROPIE_JOUET)
    assert not (d / "diag" / "20261020-181000-lecture-p4").exists()
    # même run, sans --prereg : lu, C1 calculé et écrit
    s = lp.analyser(d, "20261020-180000-p4-decisif", "20261020-182000-lecture-p4", None, entropie=ENTROPIE_JOUET)
    assert (d / "diag" / "20261020-182000-lecture-p4" / "lecture-p4.json").exists()
    print("\nDEMO CL3-01 : issue", s["issue"]["ligne"], "; C1 calculé :", lp.calcule(s.get("C1")),
          "; aire C1 :", (s.get("C1") or {}).get("aire"))
    assert s["issue"]["ligne"] != "L1"
