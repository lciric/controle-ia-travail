"""Essai du correctif (4) de `scripts/checks/lens_compare.py` (texte gelé de la tranche de l'ajustement de nos lentilles,
`texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, P.2) — v1.

À jouer SUR LA MACHINE seulement, à B0, depuis la racine de l'arbre voisin au commit 849bfe16 corrigé (jamais dans le conteneur
de la session : règle R-2710). Aucun poids réel, aucun réseau : les fonctions de chargement sont remplacées par des doubles
synthétiques ; la fonction de lecture `read` est celle du dépôt.

    NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct python -I essai-lens_compare-llama-v1.py CHEMIN/lens_compare.py

Cas sain : le fichier corrigé passe les contrôles statiques (1) et le contrôle fonctionnel (2). Artefact : le fichier publié
(non corrigé) échoue aux contrôles statiques. Sortie 0 si tout passe, 1 sinon ; chaque contrôle imprimé.
"""
import ast
import importlib.util
import json
import os
import sys
import tempfile

ATTENDU = "meta-llama/Llama-3.1-8B-Instruct"


def statiques(src: str) -> list[str]:
    fautes = []
    arbre = ast.parse(src)
    if '"Qwen/Qwen3-8B"' in src or "'Qwen/Qwen3-8B'" in src:
        fautes.append("modèle Qwen écrit en dur")
    imports = [n for n in ast.walk(arbre) if isinstance(n, ast.ImportFrom) and n.module == "neuron_lens.catalog"]
    if not any(a.name == "MODEL" for n in imports for a in n.names):
        fautes.append("MODEL non importé de neuron_lens.catalog")
    appels = [n for n in ast.walk(arbre) if isinstance(n, ast.Call) and getattr(n.func, "id", None) == "kept"]
    if not appels or any(len(c.args) != 1 or getattr(c.args[0], "id", None) != "MODEL" for c in appels):
        fautes.append("kept() appelé sans MODEL")
    if "torch.cuda.is_available()" not in src:
        fautes.append("périphérique cuda absent")
    if '"--json"' not in src:
        fautes.append("argument --json absent")
    return fautes


def fonctionnel(chemin: str) -> list[str]:
    import torch
    from neuron_lens.readout import read
    if os.environ.get("NEURON_LENS_MODEL") != ATTENDU:
        return ["NEURON_LENS_MODEL n'est pas " + ATTENDU]
    spec = importlib.util.spec_from_file_location("lens_compare_essai", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    if m.MODEL != ATTENDU:
        return [f"MODEL vaut {m.MODEL}"]
    g = torch.Generator().manual_seed(0)
    d, f, v, layer = 8, 5, 20, 2
    poids = {"lm_head.weight": torch.randn(v, d, generator=g), "model.norm.weight": torch.rand(d, generator=g) + 0.5,
             m.down_proj(layer): torch.randn(d, f, generator=g)}
    lentilles = {"A": {layer: torch.eye(d)}, "B": {layer: torch.randn(d, d, generator=g)}}
    vus = {}

    class Tok:
        def decode(self, ids):
            return "t" + "-".join(map(str, ids))

    m.tensors = lambda model, names: (vus.setdefault("tensors", model), {k: poids[k] for k in names})[1]
    m.kept = lambda model: (vus.setdefault("kept", model), torch.arange(v))[1]
    m.load_lens = lambda s, model: (vus.setdefault("lens", model), lentilles[s])[1]
    m.AutoTokenizer.from_pretrained = staticmethod(lambda model: (vus.setdefault("tok", model), Tok())[1])
    sortie = os.path.join(tempfile.mkdtemp(), "lc.json")
    sys.argv = ["lens_compare.py", "--lenses", "A,B", "--layers", str(layer), "--samples", "0", "--json", sortie]
    m.main()
    fautes = [f"{k} chargé pour {x}" for k, x in vus.items() if x != ATTENDU]
    res = json.load(open(sortie))["layers"][str(layer)]["A vs B"]
    dev = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    un, ga, wd = poids["lm_head.weight"].to(dev, torch.float16), poids["model.norm.weight"].to(dev), poids[m.down_proj(layer)].to(dev)
    ia = torch.cat([read(s * wd, un, ga, lentilles["A"][layer])[1] for s in (1, -1)])
    ib = torch.cat([read(s * wd, un, ga, lentilles["B"][layer])[1] for s in (1, -1)])
    top1 = (ia[:, 0] == ib[:, 0]).float().mean().item()
    if abs(res["top1_agree"] - top1) > 1e-12 or res["rows"] != 2 * f:
        fautes.append(f"accord écrit {res} contre recalcul {top1}")
    return fautes


def main(chemin: str) -> int:
    src = open(chemin, encoding="utf-8").read()
    fautes = statiques(src)
    print("statiques :", fautes or "ok")
    if not fautes:
        f2 = fonctionnel(chemin)
        print("fonctionnel :", f2 or "ok")
        fautes += f2
    return 1 if fautes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
