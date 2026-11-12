"""Générateur de mondes riches par programme, à graine scellée — prototype v2 (corrections E-5, E-6, E-12 (d), S-7 de la
contre-lecture `e7d5cda0…`). N'écrase pas la v1 (`../outils-v1/generateur_mondes_v1.py`, `46f3ac2d40ef…`).

Concepteur (Claude Opus 5.5), 12 novembre 2026. Aucun appel, aucun réseau ; aucune loi dans ce code.

Changements par rapport à la v1 :
- **trait latent compté à part** (classe « latente », 0 ou 1, probabilité 1/3), taille visée tirée dans [0,04 ; 0,08], poids
  du mélange tiré dans [0,3 ; 0,7] (E-5) ;
- **régularités retirées** (E-6) : sortes tirées uniformément pour chaque classe (forte : principale, interaction de seuil,
  interaction de sous-population, avec au moins une forte principale ; moyenne et faible : les cinq sortes observables) ;
  trait de condition d'une interaction de seuil tiré parmi les traits des **autres** effets ; seuils tirés en continu (six
  décimales : interaction de seuil dans [−0,5 ; 0,5], effet de seuil dans [−1,0 ; 1,2]) ;
- **régularités gardées et déclarées publiques** : au moins une forte est principale (K1 en a besoin) ; K1 est la loi du
  plus fort effet principal (elle est servie aux proposeurs de toute façon) ; un trait porte au plus un effet propre (le trait
  de condition excepté) ; un effet de sous-population ne touche qu'une sous-population ; au plus deux effets à seuil ;
  au moins deux traits leurres ;
- écriture privée par **liste blanche** de dossiers (S-7) au lieu d'une liste noire de fragments.
"""

import hashlib
import json
import os
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.join(os.path.dirname(ICI), "outils-v1")
for p in (V1, ICI):
    if p not in sys.path:
        sys.path.insert(0, p)
import monde_riche_outils_v1 as M  # noqa: E402
from generateur_mondes_v1 import engagement, graine_de_monde  # noqa: E402,F401

SORTES_OBSERVABLES = ("principal", "seuil", "interaction_seuil", "interaction_sous_population", "sous_population")
SORTES_FORTES = ("principal", "interaction_seuil", "interaction_sous_population")
CLASSES = {"forte": (0.10, 0.25), "moyenne": (0.04, 0.08), "faible": (0.02, 0.035), "latente": (0.04, 0.08)}


def tirer_gabarit_v2(rng):
    while True:
        g = [("forte", str(rng.choice(SORTES_FORTES))) for _ in range(2)]
        g += [("moyenne", str(rng.choice(SORTES_OBSERVABLES))) for _ in range(int(rng.integers(2, 4)))]
        g += [("faible", str(rng.choice(SORTES_OBSERVABLES))) for _ in range(int(rng.integers(2, 5)))]
        latent = bool(rng.random() < 1 / 3)
        sortes = [s for _, s in g]
        if not any(c == "forte" and s == "principal" for c, s in g):
            continue
        if sum(1 for s in sortes if s.startswith("interaction")) < 2:
            continue
        if sum(1 for s in sortes if s in ("seuil", "interaction_seuil")) > 2:
            continue
        if sum(1 for s in sortes if s != "sous_population") > 6:  # au moins deux leurres sur 8 traits
            continue
        return tuple(g), latent


def _dir(rng, K=3):
    v = rng.standard_normal(K)
    v -= v.mean()
    return v / np.linalg.norm(v)


def generer_monde_v2(graine, D=8, nsp=3, K=3, n_oracle=8000):
    """Devis tiré puis étalonné (bissection de l'échelle de chaque effet vers une taille visée tirée dans sa classe)."""
    rng = np.random.default_rng(np.random.SeedSequence(graine))
    gabarit, latent = tirer_gabarit_v2(rng)
    traits = [int(t) for t in rng.permutation(D)]
    effets, cibles = [], {}
    for i, (classe, ty) in enumerate(gabarit):
        eid = f"E{i + 1}"
        lo, hi = CLASSES[classe]
        cibles[eid] = float(rng.uniform(lo + 0.15 * (hi - lo), hi - 0.15 * (hi - lo)))
        e = {"id": eid, "classe": classe, "type": ty}
        if ty in ("principal", "seuil", "interaction_seuil", "interaction_sous_population"):
            e["trait"] = traits.pop(0)
        if ty == "principal":
            e["pente"] = _dir(rng, K).tolist()
        elif ty == "seuil":
            e.update(seuil=round(float(rng.uniform(-1.0, 1.2)), 6), decalage=_dir(rng, K).tolist())
        elif ty == "interaction_seuil":
            e.update(seuil=round(float(rng.uniform(-0.5, 0.5)), 6), pente=_dir(rng, K).tolist())
        elif ty == "interaction_sous_population":
            e.update(sous_population=int(rng.integers(0, nsp)), pente=_dir(rng, K).tolist())
        elif ty == "sous_population":
            e.update(sous_population=int(rng.integers(0, nsp)), decalage=_dir(rng, K).tolist())
        effets.append(e)
    # trait de condition des interactions de seuil : tiré parmi les traits des autres effets
    for e in effets:
        if e["type"] == "interaction_seuil":
            autres = sorted({x["trait"] for x in effets if "trait" in x and x is not e})
            e["trait_condition"] = int(rng.choice(autres))
    if latent:
        eid = f"E{len(effets) + 1}"
        lo, hi = CLASSES["latente"]
        cibles[eid] = float(rng.uniform(lo, hi))
        effets.append({"id": eid, "classe": "latente", "type": "latent",
                       "poids_melange": round(float(rng.uniform(0.3, 0.7)), 6), "decalage": _dir(rng, K).tolist()})
    utilises = {x.get("trait") for x in effets} | {x.get("trait_condition") for x in effets}
    spec = {"version": "monde-riche-spec-v1", "nombre_issues": K, "dimension": D, "sous_populations": nsp,
            "biais": np.round(rng.normal(0, 0.3, K), 6).tolist(), "effets": effets,
            "distracteurs": sorted(t for t in range(D) if t not in utilises)}
    Zg, Gg = M.tirer_instances(np.random.default_rng(np.random.SeedSequence([graine, 7])), n_oracle, D, nsp)
    fac = {e["id"]: 1.0 for e in effets}

    def info(eid, f):
        f2 = dict(fac, **{eid: f})
        Q = M.probas(M.compiler_monde(spec, facteurs=f2), Zg, Gg)
        Qm = M.probas(M.compiler_monde(spec, sans=(eid,), facteurs=f2), Zg, Gg)
        return float((Q * (np.log(np.maximum(Q, M.PLANCHER)) - np.log(np.maximum(Qm, M.PLANCHER)))).sum(axis=1).mean())

    for _ in range(3):
        for e in effets:
            lo, hi = 0.0, 12.0
            for _ in range(28):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if info(e["id"], mid) < cibles[e["id"]] else (lo, mid)
            fac[e["id"]] = 0.5 * (lo + hi)
    for e in effets:
        for c in ("pente", "decalage"):
            if c in e:
                e[c] = np.round(np.asarray(e[c]) * fac[e["id"]], 6).tolist()
    return spec


def generer_v2(graine, verifier, essais_max=8):
    """Tire, vérifie (fonction `verifier(spec) -> rapport`), retire si refus ; rend (spec, rapport, refus par contrôle)."""
    refus = []
    for k in range(essais_max):
        sous = int(np.random.SeedSequence(graine, spawn_key=(k,)).generate_state(1, dtype=np.uint64)[0])
        spec = generer_monde_v2(sous)
        r = verifier(spec)
        if r["conforme"]:
            return spec, r, refus
        refus.append(r["refus"]["controle"])
    return None, None, refus


def ecrire_prive(dossiers_permis, dossier, nom, objet):
    """Écrit seulement sous un dossier de la liste blanche `dossiers_permis` (chemins réels), sans écraser."""
    d = os.path.realpath(dossier)
    if not any(d == os.path.realpath(p) or d.startswith(os.path.realpath(p) + os.sep) for p in dossiers_permis):
        raise PermissionError("dossier hors de la liste blanche des dossiers privés")
    chemin = os.path.join(d, nom)
    octets = json.dumps(objet, sort_keys=True, ensure_ascii=False, indent=1).encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    h = hashlib.sha256(octets).hexdigest()
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {nom}\n")
    return h
