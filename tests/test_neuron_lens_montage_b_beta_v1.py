"""Essais des gardes du montage de la tranche de l'ajustement de nos lentilles (texte gelé, fin de P.4) : dépense simulée à 45,0 et
67,5 USD, minuterie, empreinte de Drowse altérée. Les autres gardes du montage (banc, rows_sha256 altéré, 931 documents) sont essayées
dans `test_neuron_lens_controles_b_beta_v1.py`."""
import subprocess

import pytest

from controle_ia.neuron_lens import b_beta_lancer_v1 as L
from controle_ia.neuron_lens import controles_b_beta_v1 as cb


@pytest.fixture
def ctx(tmp_path):
    from controle_ia.manifeste import creer_manifeste
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / "f.txt").write_text("x")
    subprocess.run(["git", "-C", str(tmp_path), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(tmp_path), "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "x"], check=True)
    c = L.Contexte(tmp_path, "20261119-230000-neuron-lens-b-beta", tmp_path / "hf")
    creer_manifeste(tmp_path, c.run_id, {"essai": True}, list(cb.TACHES_INTERVALLES), entropie=cb.ENTROPIE)
    return c


# ---------------------------------------------------------------- gardes du montage (texte gelé, fin de P.4)

def test_depense_simulee_et_minuterie():
    from controle_ia.neuron_lens import garde_depense_v4 as gd
    assert gd.etat(44.99, 75.0) == "ok" and gd.etat(45.0, 75.0) == "compte_rendu" and gd.etat(67.5, 75.0) == "arret"
    assert gd.minuterie_s(2.62, 75.0, 1.0) == 91374  # texte gelé, liste d'arrêt : 91 374 s au prix exigé exact
    assert gd.minuterie_s(1.85, 75.0, 1.0) <= 129600 < gd.minuterie_s(1.84, 75.0, 1.0)  # borne haute de la minuterie v4


def test_drowse_altere_arrete_b0_avant_les_essais(ctx, monkeypatch, tmp_path):
    monkeypatch.setattr(L, "ORIGINAL_06", (L.ORIGINAL_06[0], cb.sha256_octets(b"x")))
    ctx.original_06.parent.mkdir(parents=True, exist_ok=True)
    ctx.original_06.write_bytes(b"x")
    appels = []
    ctx.executer = lambda *a, **k: appels.append(a) or {"code": 0, "duree_s": 0, "fin": ["1 passed"]}
    for dr in ({"version": "6.1.4", "roue_sha256": "0" * 64}, {"version": "6.1.3", "roue_sha256": cb.DROWSE_SHA256},
               {"version": "", "roue_sha256": ""}):
        with pytest.raises(L.Arret, match="Drowse"):
            L.etape_b0(ctx, drowse=lambda dr=dr: dr)
    assert appels == []  # aucun essai lancé : arrêt avant
