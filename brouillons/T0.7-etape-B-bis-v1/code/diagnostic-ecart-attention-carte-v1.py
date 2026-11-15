"""Diagnostic de l'écart carte-processeur de la famille « attention » (répétition sur carte du 15 novembre, troisième passe,
code 9 : écart relatif 2,131e-02 > 1e-04 ; « linéaire » 1,95e-08), v1. **Processeur seulement**, aucune machine, aucune dépense ;
**données synthétiques de la répétition seulement** (mêmes tirages : `scripts/repetition_carte_bbis_v1.jeu_synthetique`, clés
`bbis/repetition/donnees`, `bbis/repetition/controle`, graines `bbis/repetition/sonde/<famille>/<l2>`) ; aucune aire.

Sous-commandes (chacune dans son propre processus : l'instruction de calcul se choisit avant l'import de torch) :
- `repliques --actions N` : les répliques économes de `sondes.familles._normalisation` et `_sacs` (même ordre des sommes, mêmes
  opérations élément par élément ; elles évitent les copies transitoires qui dépassent la mémoire de cette machine au lot entier)
  sont égales aux originales **au bit près** (moyenne, écart type, jetons réduits, indices) ;
- `tirage` : départ q0 tiré par le chemin v1 (`t07bbis.apprentissage_carte_v1.entrainer`) et par le paquet gelé
  (`sondes.familles.entrainer`), relevé à l'appel de `torch.randn` (appareil, type, égalité au bit près) ; types de **tous** les
  tenseurs rendus par les opérations de torch du chemin v1 pendant deux époques (mode de fonctions de torch) ;
- `apprendre --chemin {v1,gele} --famille F [--flux philox]` : une sonde (réglage de la répétition, l2 = 10⁻³), paramètres
  repliés écrits en `.npz` ; `gele` = `sondes.familles.entrainer` tel quel (répliques économes branchées dans ce processus
  seulement) ; `--flux philox` : q0 tiré par un autre générateur à graine égale (simulation de la piste (a)) ;
- `pas-a-pas --famille F` : trajectoires menées en pas égal sur les mêmes jetons réduits (ceux du paquet gelé) : référence A
  (le calcul de `sondes.familles._entrainer`, opération par opération) ; B : pas d'Adam remplacé par le flottant suivant
  (0,05 + 6,9·10⁻¹⁸ : un arrondi) ; C (attention) : q0[0] remplacé par le flottant suivant (un arrondi) ; une perturbation de w0
  est écartée (w0 = 0 donne des scores tous égaux à la première époque : tout w0[0] ≠ 0 rompt l'égalité du maximum, ce n'est pas
  un arrondi) ; écarts à chaque époque (paramètres, sorties d'action sur le lot) et, aux
  époques relevées, écart relatif des scores sur les 256 actions de contrôle (mesure du contrôle carte-processeur) ;
- `comparer SORTIE.json --travail DOSSIER` : écarts relatifs des scores (mesure du contrôle, `apprentissage_carte_v1.ecart_relatif`)
  entre les sondes écrites, et assemblage de la sortie.

Mesure : max |a − b| / max(|b|, 1) sur les scores des actions de contrôle (celle de `controle_carte_processeur`).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
import time
from pathlib import Path

ARBRE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ARBRE / "src"))

L2 = 1e-3
EPOQUES_RELEVEES = (0, 1, 2, 3, 5, 10, 20, 30, 50, 75, 100, 150, 200, 250, 299)


def _rep():
    spec = importlib.util.spec_from_file_location("repetition_carte_bbis_v1", ARBRE / "scripts/repetition_carte_bbis_v1.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _graine(rep, famille: str) -> int:
    return int(rep._graine(f"bbis/repetition/sonde/{famille}/{L2}").generate_state(1)[0])


def _empreinte_sonde(w, b, q) -> str:
    import numpy as np
    h = hashlib.sha256()
    for t in (w, np.array([b]), q if q is not None else np.zeros(0)):
        h.update(np.ascontiguousarray(t, dtype=np.float64).tobytes())
    return h.hexdigest()


def _instruction():
    import torch
    return {"torch": torch.__version__, "capacite_aten": torch.backends.cpu.get_cpu_capability(),
            "ATEN_CPU_CAPABILITY": os.environ.get("ATEN_CPU_CAPABILITY"),
            "MKL_ENABLE_INSTRUCTIONS": os.environ.get("MKL_ENABLE_INSTRUCTIONS"), "fils": torch.get_num_threads()}


# ------------------------------------------------------------------------------------------------ répliques économes

def normalisation_econome(sequences):
    """`sondes.familles._normalisation` sans la concaténation : sommes des lignes accumulées dans le même ordre (la réduction de
    numpy sur l'axe 0 d'un tableau contigu ajoute les lignes une à une), mêmes opérations élément par élément."""
    import numpy as np
    N = sum(int(np.asarray(s).shape[0]) for s in sequences)
    acc = None
    for q in sequences:
        c = np.asarray(q, dtype=np.float64)
        acc = np.add.reduce(c, axis=0) if acc is None else np.add.reduce(np.vstack([acc[None, :], c]), axis=0)
    mu = acc / N
    acc2 = None
    for q in sequences:
        x = np.asarray(q, dtype=np.float64) - mu
        x = np.multiply(x, x, out=x)
        acc2 = np.add.reduce(x, axis=0) if acc2 is None else np.add.reduce(np.vstack([acc2[None, :], x]), axis=0)
    s = np.sqrt(acc2 / N)
    return mu, np.where(s > 1e-12, s, 1.0)


def sacs_econome(sequences, mu, s):
    """`sondes.familles._sacs` sans la concaténation (mêmes valeurs, tenseur contigu)."""
    import numpy as np
    import torch
    N = sum(len(q) for q in sequences)
    X = torch.empty((N, int(np.asarray(sequences[0]).shape[1])), dtype=torch.float64)
    a = 0
    for q in sequences:
        X[a:a + len(q)] = torch.from_numpy((np.asarray(q, dtype=np.float64) - mu) / s)
        a += len(q)
    idx = torch.tensor(np.concatenate([np.full(len(q), i) for i, q in enumerate(sequences)]), dtype=torch.long)
    return X, idx


def brancher_repliques():
    from controle_ia.sondes import familles as fam
    fam._normalisation, fam._sacs = normalisation_econome, sacs_econome


def cmd_repliques(x) -> dict:
    import numpy as np
    import torch
    from controle_ia.sondes import familles as fam
    rep = _rep()
    seqs, _ = rep.jeu_synthetique(x.actions, x.largeur, "bbis/repetition/donnees")
    mu0, s0 = fam._normalisation(seqs)
    mu1, s1 = normalisation_econome(seqs)
    X0, i0 = fam._sacs(seqs, mu0, s0)
    X1, i1 = sacs_econome(seqs, mu1, s1)
    return {"actions": x.actions, "largeur": x.largeur, "jetons": int(X0.shape[0]),
            "egal_au_bit": {"moyenne": bool(np.array_equal(mu0, mu1)), "ecart_type": bool(np.array_equal(s0, s1)),
                            "jetons_reduits": bool(torch.equal(X0, X1)), "indices": bool(torch.equal(i0, i1))}}


# ------------------------------------------------------------------------------------------------ tirage et types

def cmd_tirage(x) -> dict:
    import numpy as np
    import torch
    from torch.overrides import TorchFunctionMode
    from controle_ia.sondes import familles as fam
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    rep = _rep()
    seqs, y = rep.jeu_synthetique(x.actions, x.largeur, "bbis/repetition/donnees")
    g = _graine(rep, "attention")
    vus = {}
    vrai = torch.randn

    def releve(quoi):
        def randn(*a, **k):
            t = vrai(*a, **k)
            vus[quoi] = {"appareil": str(t.device), "type": str(t.dtype), "forme": list(t.shape),
                         "generateur": "explicite" if k.get("generator") is not None else "par défaut (processeur)",
                         "valeurs": t.clone()}
            return t
        return randn

    torch.randn = releve("v1")
    try:
        ac.entrainer(ac.LotCarte(seqs, "cpu"), "attention", "s", 15, y, L2, g, epoques=0)
        torch.randn = releve("gele")
        fam.entrainer("attention", "s", 15, seqs, y, "attention", g, fam.Reglages(l2=L2, epoques=0))
    finally:
        torch.randn = vrai
    egal = bool(torch.equal(vus["v1"]["valeurs"], vus["gele"]["valeurs"]))
    for v in vus.values():
        v.pop("valeurs")

    class Recensement(TorchFunctionMode):
        def __init__(self):
            super().__init__()
            self.types, self.hors_double = {}, []

        def __torch_function__(self, func, types, args=(), kwargs=None):
            r = func(*args, **(kwargs or {}))
            for t in (r if isinstance(r, (tuple, list)) else (r,)):
                if isinstance(t, torch.Tensor) and t.is_floating_point():
                    nom = getattr(func, "__name__", str(func))
                    self.types.setdefault(str(t.dtype), set()).add(nom)
                    if t.dtype != torch.float64:
                        self.hors_double.append({"operation": nom, "type": str(t.dtype), "forme": list(t.shape),
                                                 "valeur": float(t) if t.numel() == 1 else None})
            return r

    lot = ac.LotCarte(seqs, "cpu")
    with Recensement() as m:
        ac.entrainer(lot, "attention", "s", 15, y, L2, g, epoques=2)
    return {"graine": g, "q0": vus, "q0_egal_au_bit_v1_gele": egal,
            "operations_par_type_flottant_du_chemin_v1": {k: sorted(v) for k, v in m.types.items()},
            "sorties_hors_double_du_chemin_v1": m.hors_double,
            "note": "sorties hors double : compteurs de pas d'Adam (scalaires entiers, `state['step']`), aucun calcul"}


# ------------------------------------------------------------------------------------------------ apprentissage

def cmd_apprendre(x) -> dict:
    import numpy as np
    import torch
    from controle_ia.sondes import familles as fam
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE, EPOQUES, PAS
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(x.fils))
    rep = _rep()
    seqs, y = rep.jeu_synthetique(x.actions, x.largeur, "bbis/repetition/donnees")
    g = _graine(rep, x.famille)
    nom = f"{x.famille}-c15-l2_{L2!r}"
    t0 = time.perf_counter()
    if x.flux == "philox":                       # piste (a) : autre générateur à graine égale (ici Philox de numpy)
        vrai = torch.randn

        def randn(*a, **k):
            d = int(a[0])
            z = np.random.Generator(np.random.Philox(np.random.SeedSequence(g))).standard_normal(d)
            return torch.as_tensor(z, dtype=k.get("dtype", torch.float64))
        torch.randn = randn
    try:
        if x.chemin == "v1":
            lot = ac.LotCarte(seqs, "cpu")
            del seqs
            s = ac.entrainer(lot, x.famille, nom, 15, y, L2, g)
        else:
            brancher_repliques()
            s = fam.entrainer(x.famille, nom, 15, seqs, y, AGREGATION_DE[x.famille], g,
                              fam.Reglages(l2=L2, epoques=EPOQUES, pas=PAS))
    finally:
        if x.flux == "philox":
            torch.randn = vrai
    duree = time.perf_counter() - t0
    q = s.q if s.q is not None else np.zeros(0)
    np.savez(x.npz, w=s.w, b=np.array([s.b]), q=q)
    return {"chemin": x.chemin, "famille": x.famille, "flux": x.flux, "graine": g, "duree_s": duree, "npz": Path(x.npz).name,
            "empreinte_parametres": _empreinte_sonde(s.w, s.b, s.q), "instruction": _instruction()}


# ------------------------------------------------------------------------------------------------ pas à pas

def cmd_pas_a_pas(x) -> dict:
    import numpy as np
    import torch
    from controle_ia.sondes import familles as fam
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE, EPOQUES, PAS
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(int(x.fils))
    rep = _rep()
    seqs, y = rep.jeu_synthetique(x.actions, x.largeur, "bbis/repetition/donnees")
    g = _graine(rep, x.famille)
    agregation = AGREGATION_DE[x.famille]
    # le calcul de `sondes.familles._entrainer`, opération par opération (même ordre d'appel de torch.manual_seed)
    torch.manual_seed(g)
    mu, s = normalisation_econome(seqs)
    X, idx = sacs_econome(seqs, mu, s)
    n, d = len(seqs), X.shape[1]
    del seqs
    cible = torch.tensor(np.asarray(y, dtype=np.float64))
    q0 = torch.randn(d, dtype=torch.float64) * 0.01 if agregation == "attention" else None
    ctrl, _ = rep.jeu_synthetique(256, x.largeur, "bbis/repetition/controle")

    def trajectoire(perturbation):
        params = [torch.nn.Parameter(torch.zeros(d, dtype=torch.float64)),
                  torch.nn.Parameter(torch.zeros((), dtype=torch.float64))]
        if q0 is not None:
            q = q0.clone()
            if perturbation == "q0":
                q[0] = torch.nextafter(q[0], torch.tensor(np.inf, dtype=torch.float64))
            params.append(torch.nn.Parameter(q))
        pas = float(np.nextafter(PAS, 1.0)) if perturbation == "pas" else PAS
        return {"p": params, "opt": torch.optim.Adam(params, lr=pas), "nom": perturbation, "pas": pas}

    trajs = [trajectoire(None), trajectoire("pas")] + ([trajectoire("q0")] if q0 is not None else [])
    bce = torch.nn.BCEWithLogitsLoss()

    def sonde(t):
        wn = t["p"][0].detach().numpy()
        w_brut = wn / s
        qn = t["p"][2].detach().numpy() if len(t["p"]) > 2 else None
        return fam.SondeLineaireJetons("s", 15, agregation, w_brut, float(t["p"][1].detach()) - float(mu @ w_brut),
                                       (qn / s) if qn is not None else None, x.famille)

    def ecart_param(a, b):
        a, b = a.detach(), b.detach()
        return float((a - b).abs().max() / max(float(a.abs().max()), 1e-300))

    journal = {t["nom"] or "A": [] for t in trajs}
    t0 = time.perf_counter()
    for e in range(EPOQUES):
        sorties = []
        for t in trajs:
            w, b = t["p"][0], t["p"][1]
            q = t["p"][2] if len(t["p"]) > 2 else None
            t["opt"].zero_grad()
            sj = X @ w + b
            lj = X @ q if q is not None else None
            sa = fam._agreger(sj, lj, idx, n, agregation)
            perte = bce(sa, cible) + L2 * (w ** 2).sum()
            perte.backward()
            t["opt"].step()
            sorties.append((sa.detach().clone(), float(perte.detach())))
        ref_p, (ref_sa, ref_perte) = trajs[0]["p"], sorties[0]
        for t, (sa, perte) in zip(trajs[1:], sorties[1:]):
            ligne = {"epoque": e, "perte": perte, "perte_ref": ref_perte,
                     "ecart_w": ecart_param(t["p"][0], ref_p[0]),
                     "ecart_q": ecart_param(t["p"][2], ref_p[2]) if len(t["p"]) > 2 else None,
                     "ecart_sorties_lot": float(((sa - ref_sa).abs() / ref_sa.abs().clamp(min=1.0)).max())}
            if e in EPOQUES_RELEVEES:
                ligne["ecart_controle"] = ac.ecart_relatif(ac.scores(sonde(t), ctrl), ac.scores(sonde(trajs[0]), ctrl))
            journal[t["nom"]].append(ligne)
    finale = sonde(trajs[0])
    return {"famille": x.famille, "graine": g, "duree_s": time.perf_counter() - t0, "instruction": _instruction(),
            "empreinte_parametres_reference": _empreinte_sonde(finale.w, finale.b, finale.q),
            "perturbations": {"pas": f"pas d'Adam {trajs[1]['pas']!r} au lieu de {PAS!r} (flottant suivant)",
                              "q0": "q0[0] remplacé par le flottant suivant"},
            "journal": journal}


# ------------------------------------------------------------------------------------------------ comparaison

def charger(npz, famille):
    import numpy as np
    from controle_ia.sondes import familles as fam
    from controle_ia.t07bbis.commun_v1 import AGREGATION_DE
    z = np.load(npz)
    q = z["q"] if z["q"].size else None
    return fam.SondeLineaireJetons("s", 15, AGREGATION_DE[famille], z["w"], float(z["b"][0]), q, famille)


def cmd_comparer(x) -> dict:
    import numpy as np
    from controle_ia.t07bbis import apprentissage_carte_v1 as ac
    rep = _rep()
    ctrl, _ = rep.jeu_synthetique(256, x.largeur, "bbis/repetition/controle")
    trav = Path(x.travail)
    parts = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(trav.glob("*.json"))}
    paires = [("v1-attention", "gele-attention", "contrôle de la répétition rejoué sur processeur (chemin v1 contre paquet gelé)"),
              ("gele-attention-avx2", "gele-attention", "paquet gelé contre lui-même, autre jeu d'instructions (AVX2 contre AVX-512)"),
              ("gele-attention-philox", "gele-attention", "piste (a) simulée : q0 d'un autre générateur à graine égale"),
              ("v1-lineaire", "gele-lineaire", "contrôle de la répétition rejoué sur processeur (chemin v1 contre paquet gelé)"),
              ("gele-lineaire-avx2", "gele-lineaire", "paquet gelé contre lui-même, autre jeu d'instructions (AVX2 contre AVX-512)")]
    comparaisons = []
    for a, b, quoi in paires:
        if a not in parts or b not in parts:
            comparaisons.append({"a": a, "b": b, "quoi": quoi, "absent": True})
            continue
        f = parts[a]["famille"]
        sa, sb = charger(trav / parts[a]["npz"], f), charger(trav / parts[b]["npz"], f)
        ea = ac.scores(sa, ctrl)
        eb = ac.scores(sb, ctrl)
        comparaisons.append({
            "a": a, "b": b, "quoi": quoi, "famille": f, "ecart_relatif_controle": ac.ecart_relatif(ea, eb),
            "au_bit_pres": bool(np.array_equal(sa.w, sb.w) and sa.b == sb.b and (sa.q is None or np.array_equal(sa.q, sb.q))),
            "ecart_w": float(np.max(np.abs(sa.w - sb.w)) / np.max(np.abs(sb.w))),
            "ecart_q": None if sa.q is None else float(np.max(np.abs(sa.q - sb.q)) / np.max(np.abs(sb.q))),
            "max_abs_q": None if sb.q is None else float(np.max(np.abs(sb.q))),
            "max_abs_score": float(np.max(np.abs(eb)))})
    doc = {"objet": "diagnostic de l'écart carte-processeur de la famille attention (répétition B bis, 15 novembre)",
           "donnees": "synthétiques de la répétition seulement (mêmes graines) ; aucune aire", "parties": parts,
           "comparaisons": comparaisons}
    for p in ("pas-a-pas-attention", "pas-a-pas-lineaire"):
        if p in parts and "gele-" + parts[p]["famille"] in parts:
            doc.setdefault("reference_pas_a_pas_egale_au_paquet_gele", {})[parts[p]["famille"]] = (
                parts[p]["empreinte_parametres_reference"] == parts["gele-" + parts[p]["famille"]]["empreinte_parametres"])
    Path(x.sortie).write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return {"sortie": x.sortie}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("commande", choices=["repliques", "tirage", "apprendre", "pas-a-pas", "comparer"])
    ap.add_argument("sortie", nargs="?")
    ap.add_argument("--actions", type=int, default=640)
    ap.add_argument("--largeur", type=int, default=4096)
    ap.add_argument("--fils", type=int, default=4)
    ap.add_argument("--chemin", choices=["v1", "gele"], default="gele")
    ap.add_argument("--famille", choices=["lineaire", "attention"], default="attention")
    ap.add_argument("--flux", choices=["torch", "philox"], default="torch")
    ap.add_argument("--npz")
    ap.add_argument("--travail")
    x = ap.parse_args(argv)
    f = {"repliques": cmd_repliques, "tirage": cmd_tirage, "apprendre": cmd_apprendre, "pas-a-pas": cmd_pas_a_pas,
         "comparer": cmd_comparer}[x.commande]
    r = f(x)
    if x.commande != "comparer":
        texte = json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n"
        if x.sortie:
            Path(x.sortie).write_text(texte, encoding="utf-8")
        print(texte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
