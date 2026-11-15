"""Balayage d'un arbre de fichiers à la recherche des secrets de la machine, avant toute poussée — v1 (tranche B-α de « Neuron Lens »).

L'amorce B-α l'appelle avant chaque `git add` de l'arbre des résultats : si un fichier contient la valeur d'un secret (lue par son NOM
dans l'environnement, jamais affichée), sous l'une des formes de `suivi_vast_v6.formes` (brute, adresse, base 64 standard et « url-safe »,
seule ou dans l'en-tête `x-access-token:<secret>`, aux trois alignements), rien n'est poussé. Secrets balayés : `GH_TOKEN`, `HF_TOKEN`,
`HUGGING_FACE_HUB_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN_2` (ceux qui ont au moins 8 caractères). `GH_TOKEN` est exigé (la poussée en a
besoin ; sans lui le balayage serait vide).

Usage : `python -m controle_ia.neuron_lens.balayage_arbre_v1 <dossier ou fichier>…` ; code 0 : rien trouvé ; 1 : forme trouvée (les
chemins seuls sont écrits) ; 2 : balayage impossible (secret exigé absent, chemin absent, lecture impossible).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from controle_ia.neuron_lens.suivi_vast_v6 import formes

NOMS = ("GH_TOKEN", "HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2")
EXIGE = "GH_TOKEN"


def motifs(env=os.environ) -> list[bytes]:
    if len(env.get(EXIGE, "")) < 8:
        raise ValueError(f"balayage refusé : {EXIGE} absent de l'environnement (le balayage serait vide)")
    return sorted({f.encode() for k in NOMS if len(env.get(k, "")) >= 8 for f in formes(env[k])})


def fichiers(chemins):
    for c in map(Path, chemins):
        if not c.exists():
            raise FileNotFoundError(f"chemin absent : {c}")
        if c.is_file():
            yield c
        else:
            yield from sorted(p for p in c.rglob("*") if p.is_file() and ".git" not in p.relative_to(c).parts)


def balayer(chemins, env=os.environ) -> list[str]:
    """Chemins des fichiers qui contiennent une forme de secret (vide = rien trouvé)."""
    m = motifs(env)
    trouves = []
    for f in fichiers(chemins):
        b = f.read_bytes()
        if any(x in b for x in m):
            trouves.append(str(f))
    return trouves


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print("usage : balayage_arbre_v1 <chemin>…", file=sys.stderr)
        return 2
    try:
        t = balayer(argv)
    except (ValueError, OSError) as e:
        print(f"BALAYAGE IMPOSSIBLE : {e}", file=sys.stderr)
        return 2
    for f in t:
        print(f"FORME DE SECRET TROUVEE : {f}")
    return 1 if t else 0


if __name__ == "__main__":
    sys.exit(main())
