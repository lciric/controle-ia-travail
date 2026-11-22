"""Essai du correctif (4) de `scripts/checks/lens_compare.py` (comparaison des lentilles neurone par neurone), v2.

Pièce du texte gelé de la tranche de l'ajustement de nos lentilles (`texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, P.2). Remplace
la v1 (`essai-lens_compare-llama-v1.py`), selon la contre-lecture `contre-lecture-correctif-4-et-essai-llama-miniature-v1.md`.

À jouer SUR LA MACHINE seulement, à B0, depuis la racine de l'arbre voisin (commit 849bfe16) corrigé par
`lens_compare-llama-v2.diff`, jamais dans le conteneur de la session (règle R-2710) :

    NEURON_LENS_ROOT=$PWD NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct python -m pytest -q -rs <chemin>/essai-lens_compare-llama-v2.py

Attendu : tous les tests passent, aucun sauté. Aucun poids réel, aucun réseau : tokeniseur, poids, jetons gardés et lentilles sont
des doubles synthétiques ; la fonction de lecture `read` est celle du dépôt.
- Cas sain : le fichier corrigé (empreinte `c974cc1a…`) passe les contrôles statiques et le contrôle fonctionnel.
- Artefacts : le fichier publié (empreinte `37b30e98…`, lu par `git show HEAD:scripts/checks/lens_compare.py`) échoue aux six
  contrôles statiques ; sept copies fautives du fichier corrigé échouent chacune au contrôle statique ou au contrôle fonctionnel.
Valeurs attendues des doubles (graine 0), recalculées hors du voisin par l'autrice : accord du premier jeton 4/14 ; sans
l'indexation par les jetons gardés, 7/14.
"""
import ast
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import types
from pathlib import Path

import pytest

ROOT = Path(os.environ.get("NEURON_LENS_ROOT", ".")).resolve()
sys.path.insert(0, str(ROOT))
ATTENDU = "meta-llama/Llama-3.1-8B-Instruct"
SHA_CORRIGE = "c974cc1aa58f81f4b77e63db7cf6905d1a3b6172652a3dc51bf6f0605bacc77a"
SHA_PUBLIE = "37b30e98c9771c03ed452ff0ff36b3667c382201fa726180497c03a2b9daf6cd"
CHEMIN = ROOT / "scripts" / "checks" / "lens_compare.py"


def statiques(src: str) -> list[str]:
    fautes, arbre = [], ast.parse(src)
    noeuds = list(ast.walk(arbre))
    if any(isinstance(n, ast.Constant) and n.value == "Qwen/Qwen3-8B" for n in noeuds):
        fautes.append("modèle Qwen écrit en dur")
    if not any(isinstance(n, ast.ImportFrom) and n.module == "neuron_lens.catalog" and any(a.name == "MODEL" for a in n.names)
               for n in noeuds):
        fautes.append("MODEL non importé de neuron_lens.catalog")
    if any(isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign)) and any(
            isinstance(t, ast.Name) and t.id == "MODEL" for t in (n.targets if isinstance(n, ast.Assign) else [n.target]))
           for n in noeuds):
        fautes.append("MODEL réaffecté")
    appels = [n for n in noeuds if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "kept"]
    if not appels or any(len(c.args) != 1 or not isinstance(c.args[0], ast.Name) or c.args[0].id != "MODEL" for c in appels):
        fautes.append("kept() appelé sans MODEL")
    dev = [n for n in noeuds if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "dev" for t in n.targets)]
    if not dev or "torch.cuda.is_available()" not in ast.unparse(dev[0].value):
        fautes.append("périphérique cuda absent de l'affectation de dev")
    ouvertures = [n for n in noeuds if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "open"]
    if not any(len(o.args) == 2 and isinstance(o.args[1], ast.Constant) and o.args[1].value == "x"
               and "args.json" in ast.unparse(o.args[0]) for o in ouvertures):
        fautes.append("--json absent ou ouvert sans création exclusive")
    return fautes


def charger(chemin: Path):
    spec = importlib.util.spec_from_file_location(f"lc_{hashlib.sha256(str(chemin).encode()).hexdigest()[:8]}", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def fonctionnel(chemin: Path) -> list[str]:
    import torch
    from neuron_lens.readout import read
    if os.environ.get("NEURON_LENS_MODEL") != ATTENDU:
        return ["NEURON_LENS_MODEL n'est pas " + ATTENDU]
    m = charger(chemin)
    if m.MODEL != ATTENDU:
        return [f"MODEL vaut {m.MODEL}"]
    g = torch.Generator().manual_seed(0)
    d, f, v, layer = 8, 7, 20, 2
    lm, gam, wd = torch.randn(v, d, generator=g), torch.rand(d, generator=g) + 0.5, torch.randn(d, f, generator=g)
    keep = torch.randperm(v, generator=g)[:14]
    lentilles = {"A": {layer: torch.eye(d)}, "B": {layer: torch.eye(d) + 0.5 * torch.randn(d, d, generator=g)}}
    poids = {"lm_head.weight": lm, "model.norm.weight": gam, m.down_proj(layer): wd}
    vus = []

    class Tok:
        def decode(self, ids):
            return "t" + "-".join(map(str, ids))

    m.tensors = lambda model, names: (vus.append(("tensors", model)), {k: poids[k] for k in names})[1]
    m.kept = lambda model: (vus.append(("kept", model)), keep)[1]
    m.load_lens = lambda s, model: (vus.append(("lens", model)), lentilles[s])[1]
    m.AutoTokenizer = types.SimpleNamespace(from_pretrained=lambda model: (vus.append(("tok", model)), Tok())[1])
    with tempfile.TemporaryDirectory() as tmp:
        sortie = os.path.join(tmp, "lc.json")
        argv, sys.argv = sys.argv, ["lens_compare.py", "--lenses", "A,B", "--layers", str(layer), "--samples", "0",
                                    "--json", sortie]
        try:
            m.main()
        finally:
            sys.argv = argv
        res = json.load(open(sortie))
    fautes = [f"{k} chargé pour {x}" for k, x in vus if x != ATTENDU]
    if {k for k, _ in vus} != {"tensors", "kept", "lens", "tok"}:
        fautes.append(f"chargements vus : {sorted({k for k, _ in vus})}")
    if res.get("model") != ATTENDU:
        fautes.append(f"modèle écrit {res.get('model')}")
    paire = res["layers"][str(layer)]["A vs B"]
    dev = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    un, ga, w = lm[keep].to(dev, torch.float16), gam.to(dev), wd.to(dev, torch.float32)
    ia = torch.cat([read(s * w, un, ga, lentilles["A"][layer])[1] for s in (1, -1)])
    ib = torch.cat([read(s * w, un, ga, lentilles["B"][layer])[1] for s in (1, -1)])
    top1 = (ia[:, 0] == ib[:, 0]).float().mean().item()
    ov = torch.tensor([len(set(x.tolist()) & set(y.tolist())) / ia.shape[1] for x, y in zip(ia, ib)]).mean().item()
    if not 0 < top1 < 1:
        fautes.append(f"essai non discriminant : accord recalculé {top1}")
    if abs(paire["top1_agree"] - top1) > 1e-12 or abs(paire["top10_overlap"] - ov) > 1e-12 or paire["rows"] != 2 * f:
        fautes.append(f"écrit {paire} contre recalcul {top1}, {ov}")
    return fautes


FAUTIVES = {  # remplacement dans le fichier corrigé -> la copie doit échouer
    "modèle réaffecté": ("# correctif (4) : le modèle de NEURON_LENS_MODEL, comme kept()\n",
                         "# correctif (4)\nMODEL = MODEL.replace('meta-llama', 'Qwen')\n"),
    "valeur arrondie": ('"top1_agree": top1.item()', '"top1_agree": round(top1.item(), 2)'),
    "recouvrement faux": ('"top10_overlap": overlap.item()', '"top10_overlap": top1.item()'),
    "jetons gardés non indexés": ('w["lm_head.weight"][keep]', 'w["lm_head.weight"][:len(keep)]'),
    "cuda en commentaire seulement": ('torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")',
                                      'torch.device("mps" if torch.backends.mps.is_available() else "cpu")  # torch.cuda.is_available()'),
    "écrasement permis": ('open(args.json, "x")', 'open(args.json, "w")'),
    "kept sans modèle": ("keep = kept(MODEL)", "keep = kept()"),
}


def test_empreinte_du_fichier_corrige():
    assert hashlib.sha256(CHEMIN.read_bytes()).hexdigest() == SHA_CORRIGE


def test_cas_sain():
    src = CHEMIN.read_text(encoding="utf-8")
    assert statiques(src) == []
    assert fonctionnel(CHEMIN) == []


def test_artefact_fichier_publie():
    publie = subprocess.run(["git", "-C", str(ROOT), "show", "HEAD:scripts/checks/lens_compare.py"],
                            check=True, capture_output=True).stdout
    assert hashlib.sha256(publie).hexdigest() == SHA_PUBLIE
    assert len(statiques(publie.decode("utf-8"))) == 6


@pytest.mark.parametrize("nom", sorted(FAUTIVES))
def test_artefacts_copies_fautives(nom, tmp_path):
    a, b = FAUTIVES[nom]
    src = CHEMIN.read_text(encoding="utf-8")
    assert src.count(a) == 1, nom
    copie = tmp_path / "lens_compare.py"
    copie.write_text(src.replace(a, b), encoding="utf-8")
    fautes = statiques(copie.read_text(encoding="utf-8"))
    if not fautes:
        fautes = fonctionnel(copie)
    assert fautes, f"copie fautive « {nom} » non détectée"
