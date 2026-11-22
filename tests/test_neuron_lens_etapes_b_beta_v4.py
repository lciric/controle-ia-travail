"""Essai discriminant des moitiés exportées (vérification courte de la commande v3, V-m1) : les lentilles des moitiés sont tirées des
sommes de **chaque** moitié du fichier d'ajustement ; des sommes distinctes donnent des matrices distinctes (A2 tient), des sommes égales
des matrices égales (A2 les voit). Remplace, sans le réécrire, `test_export_moities_egales_vues_par_a2` de l'essai v3. Joué dans le
conteneur, non embarqué (lanceur v2 inchangé)."""
import sys
from pathlib import Path

import pytest

torch = pytest.importorskip("torch")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_neuron_lens_etapes_b_beta_v2 as T  # noqa: E402
from test_neuron_lens_etapes_b_beta_v2 import ctx, resultat  # noqa: E402,F401

from controle_ia.neuron_lens import b_beta_lancer_v2 as L  # noqa: E402
from controle_ia.neuron_lens import controles_b_beta_v2 as cb  # noqa: E402


@pytest.mark.parametrize("egales", [True, False])
def test_moities_exportees(ctx, egales):
    f = ctx.voisin / "data/fits" / cb.FIT_NOMS["R"]
    g = torch.Generator().manual_seed(0)
    sums = {}
    for t, n in (("out", 31), ("mid", 32)):
        a = torch.randn(n, T.D, T.D, generator=g) * 466
        sums[(t, 0)] = a
        sums[(t, 1)] = a.clone() if egales else torch.randn(n, T.D, T.D, generator=g) * 466
    torch.save({"meta": {"lens": "R", "model": L.LLAMA, "docs": 932, "rows_sha256": cb.ROWS_SHA256, "full_length": True},
                "state": {"sums": sums, "n_docs": [466, 466]}, "next_doc": 932}, f)
    resultat(ctx, "ajustement-R", {"sha256": L.sha256(f)})
    moy = {None: (sums[("out", 0)] + sums[("out", 1)]) / 932, 0: sums[("out", 0)] / 466, 1: sums[("out", 1)] / 466}
    for spec, (nom, moitie) in L.EXPORTS.items():  # chaque export = la moyenne de SA moitié (ce que ferait Drowse)
        ctx.voisin_py.lentilles[spec] = {l: moy[moitie][l].clone() for l in range(31)}
    ctx.voisin_py.lentilles["npR"] = {l: torch.randn(T.D, T.D, generator=g) for l in range(31)}

    def effet(cmd, cwd, fh):
        home = ctx.voisin / "data/lenses" / cmd[cmd.index("--name") + 1] / "local/r"
        home.mkdir(parents=True, exist_ok=True)
        (home / "manifest.json").write_text("{}")
    ctx.executer = T.executer_ok(effet)
    r = L.etape_export(ctx)  # (o) tient dans les deux cas
    mm = {int(l): tuple(v) for l, v in r["matrices_moities"].items()}
    ok, pb = cb.controles_a2_a3({"R": [466, 466]}, list(cb.ROWS_SHA256_MOITIES), {"R|out": 1.0}, mm)
    if egales:
        assert all(a == b for a, b in mm.values()) and not ok and any("égales" in p for p in pb)
    else:
        assert all(a != b for a, b in mm.values()) and ok, pb
