"""Entrées FACTICES de la forme de 7b pour la répétition de la commande de la phase B du compte 3 (v2).

Écrit le 2026-11-16 par le préparateur de la commande (sous-agent de la session mère, même modèle qu'elle). **Aucune donnée du
programme** : tout est tiré par graine par la fabrique des essais de la pièce « mots et coût »
(`scripts/fabrique_factice_mots_et_cout_t06_v1.py`, citée par la ligne `CODE-MOTS-ET-COUT-T06`), à la configuration scellée de 7b
(`prereg/T0.6-organismes-config-7b-v1.json` : une configuration scellée avant la course, non une donnée). Aucun fichier de 7a, de 7b
ou de T0.7 n'est lu.

    PYTHONPATH=<dépôt>/src python -P -B fabrique_depots_jouets_phase_b_v2.py <dépôt> <dossier de sortie neuf>

Écrit, sous le dossier de sortie, cinq jeux d'entrées au nom de run réel de 7b (`20261111-151701-t06-reel`), qui partagent le même
manifeste factice (donc la même ligne `RUN-CONFIRMATION-T06` jouet) :
- `saines/` : cinq fichiers et leurs compagnons, tels que la fabrique les écrit (la pièce rend le code 0) ;
- `effectifs/` : les dix dernières actions retirées des mesures et des textes, empreintes de `episodes-t06.json` remises d'accord
  (la pièce refuse à la lecture des entrées : code 2, rien d'écrit) ;
- `jetons/` : un nombre de jetons négatif dans les mesures, empreintes remises d'accord (la pièce passe ses contrôles d'entrée,
  écrit son manifeste, puis s'arrête au calcul des traits : code 3, fichier d'arrêt seul) ;
- `arret/` : les entrées saines, plus un `diag/<run>/arret.json` factice (la branche jouet porte une course « arrêtée ») ;
- `compagnon-faux/` : les entrées saines, le compagnon de `lecture-cout-t06.json` faux.
N'imprime que des noms et des empreintes.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

import numpy as np

RUN = "20261111-151701-t06-reel"
GRAINE = 2026111602


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sceller(p: Path) -> str:
    h = sha(p)
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def accorder_episodes(racine: Path) -> None:
    """Remet d'accord les empreintes des mesures et des textes dans `episodes-t06.json` (même enveloppe, même écriture)."""
    e = racine / "diag" / RUN / "episodes-t06.json"
    corps = json.loads(e.read_text(encoding="utf-8"))
    corps["resultat"]["mesures_sha256"] = sha(racine / "donnees" / RUN / "mesures-t06.npz")
    corps["resultat"]["textes_sha256"] = sha(racine / "donnees" / RUN / "textes-actions-t06.jsonl")
    e.write_text(json.dumps(corps, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sceller(e)


def recrire_mesures(racine: Path, transformer) -> None:
    m = racine / "donnees" / RUN / "mesures-t06.npz"
    with np.load(m, allow_pickle=False) as z:
        colonnes = {k: z[k] for k in z.files}
    colonnes = transformer(colonnes)
    with open(m, "wb") as f:
        np.savez(f, **colonnes)
    sceller(m)


def main(argv: list[str]) -> int:
    depot, sortie = Path(argv[0]).resolve(), Path(argv[1])
    if sortie.exists():
        print(f"ARRÊT : {sortie} existe déjà")
        return 1
    spec = importlib.util.spec_from_file_location("fabrique_factice", depot / "scripts" / "fabrique_factice_mots_et_cout_t06_v1.py")
    fab = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = fab
    spec.loader.exec_module(fab)
    saines = sortie / "saines"
    saines.mkdir(parents=True)
    fab.fabriquer(saines, RUN, fab.config_scellee(depot), graine=GRAINE)
    # effectifs : dix dernières actions retirées (mesures et textes), empreintes d'accord
    d = sortie / "effectifs"
    shutil.copytree(saines, d)
    recrire_mesures(d, lambda c: {k: v[:-10] for k, v in c.items()})
    t = d / "donnees" / RUN / "textes-actions-t06.jsonl"
    lignes = t.read_text(encoding="utf-8").splitlines(keepends=True)
    t.write_text("".join(lignes[:-10]), encoding="utf-8")
    sceller(t)
    accorder_episodes(d)
    # jetons : un nombre de jetons négatif (types et effectifs inchangés)
    d = sortie / "jetons"
    shutil.copytree(saines, d)

    def negatif(c):
        j = c["jetons"].copy()
        j[0] = -5
        return {**c, "jetons": j}

    recrire_mesures(d, negatif)
    accorder_episodes(d)
    # arret : course « arrêtée » (fichier factice de plus sur la branche jouet)
    d = sortie / "arret"
    shutil.copytree(saines, d)
    a = d / "diag" / RUN / "arret.json"
    a.write_text('{"jouet": "course arrêtée (factice)"}\n', encoding="utf-8")
    sceller(a)
    # compagnon-faux : compagnon de lecture-cout-t06.json faux
    d = sortie / "compagnon-faux"
    shutil.copytree(saines, d)
    (d / "diag" / RUN / "lecture-cout-t06.json.sha256").write_text(f"{'0' * 64}  lecture-cout-t06.json\n", encoding="utf-8")
    for jeu in ("saines", "effectifs", "jetons", "arret", "compagnon-faux"):
        fichiers = sorted(p for p in (sortie / jeu).rglob("*") if p.is_file())
        print(f"{jeu} : {len(fichiers)} fichiers ; manifeste {sha(sortie / jeu / 'runs' / RUN / 'manifeste.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
