"""Essais R5 du repli en deux temps de la variante B (`src/controle_ia/t07/repli_etapes_v1.py` ; ordre d'exécution de l'étape A,
brouillon 2) : `repli-seul` (recalcul et garde d'équivalence, rapport scellé, rien d'ouvert) puis relecture du rapport avant
`etape-a-apres-repli`. Run jouet de T0.6 de `tests/test_t07_repli_recalcul_v1.py` (chaîne réelle en mode jouet, aucun
téléchargement). L'étape A après le repli est jouée de bout en bout par la répétition jouet de l'ordre (script
`scripts/repetition_jouet_variante_b_t07_v1.py`)."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from controle_ia.t07 import repli_etapes_v1 as rt
from controle_ia.t07 import repli_recalcul_v1 as rr
from test_t07_repli_recalcul_v1 import RUN, run_jouet  # noqa: F401  (fixture de module)
from test_t07_sondes_neuves_v1 import construire_complet


@pytest.fixture
def config(depot):
    return construire_complet(depot).config


@pytest.fixture
def racine(run_jouet, tmp_path):  # noqa: F811
    """Copie du dépôt du run jouet (activations retirées) : chaque essai recalcule dans la sienne."""
    d = tmp_path / "depot"
    shutil.copytree(run_jouet[0], d)
    return d


def test_repli_seul_puis_relecture_cas_sain(racine, config):
    """Cas sain : garde d'équivalence passée, rapport scellé sous `replis-t07/`, activations écrites ; aucune ligne de registre, aucun
    journal d'ouverture, aucun manifeste de T0.7 ; relecture conforme (même run, même manifeste, activations présentes)."""
    r = rt.repli_seul(racine, RUN, config, instant=1_800_000_000)
    assert r["chemin"].startswith(rt.DOSSIER + "/") and r["rapport"]["garde_equivalence"]["ecart_max"] == 0.0
    assert (racine / "donnees" / RUN / "activations").is_dir()
    assert not list(racine.glob("runs/*-t07-*")) and not list(racine.glob("registres/*.ouvertures.md"))
    lu = rt.lire_rapport(racine, Path(r["chemin"]), RUN)
    assert lu["garde_equivalence"] == r["rapport"]["garde_equivalence"]


def test_repli_seul_refus_et_arret(racine, config, monkeypatch, capsys):
    """Artefacts : activations déjà présentes → refus (R12), rien d'écrit ; empan décalé d'un jeton → garde d'équivalence en échec,
    code 3 par la commande (R11)."""
    (racine / "donnees" / RUN / "activations").mkdir()
    with pytest.raises(rt.RefusRepli, match="existe déjà"):
        rt.repli_seul(racine, RUN, config, instant=1_800_000_000)
    assert not (racine / rt.DOSSIER).exists()
    (racine / "donnees" / RUN / "activations").rmdir()
    monkeypatch.setattr(rr, "EMPAN_DECALAGE", 1)
    cfg = racine / "config-t07.json"
    cfg.write_text(json.dumps(config), encoding="utf-8")
    assert rt.main(["repli-seul", str(racine), RUN, str(cfg)]) == rt.CODE_ARRET
    assert "ARRÊT (R11, repli)" in capsys.readouterr().err


@pytest.mark.parametrize("cas", ["sceau", "run", "manifeste", "activations"])
def test_relecture_du_rapport_artefacts(racine, config, cas):
    """Artefacts de la relecture : rapport retouché (sceau) ; autre run ; manifeste de 7b changé depuis le recalcul ; activations
    absentes → refus (code 2), l'étape A ne s'ouvre pas."""
    r = rt.repli_seul(racine, RUN, config, instant=1_800_000_000)
    p = racine / r["chemin"]
    run = RUN
    if cas == "sceau":
        p.write_text(p.read_text(encoding="utf-8") + " ", encoding="utf-8")
    elif cas == "run":
        run = "20261110-070001-t06-jouet"
    elif cas == "manifeste":
        m = racine / "runs" / RUN / "manifeste.json"
        m.write_text(m.read_text(encoding="utf-8") + " ", encoding="utf-8")
    else:
        shutil.rmtree(racine / "donnees" / RUN / "activations")
    with pytest.raises(rt.RefusRepli):
        rt.lire_rapport(racine, Path(r["chemin"]), run)
