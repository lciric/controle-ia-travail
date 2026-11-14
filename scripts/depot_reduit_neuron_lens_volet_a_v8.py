"""Dépôt réduit à l'arbre utile pour la course du volet A de « Neuron Lens » — v8 (v7 avec l'amorce v4 : essai à blanc v3 ; v7 : v6 avec l'amorce v3, commande v6, et garde
des secrets élargie aux jetons `gho_`, `ghs_`, `ghu_`, `ghr_` et `github_pat_` : contre-lecture 7, remarque 10 ; v6 : v5 avec l'amorce v2, commande v5 ; v5 : v4 + script d'amorce de la machine `scripts/amorce_neuron_lens_volet_a_v1.sh`,
commande v4 sans ssh, R-2752 ; mode des fichiers exécutables conservé ; v4 : v3 avec le lanceur v3 et la garde de dépense v3, après la contre-lecture 4 ;
v3 : v2 avec les pièces d'après la contre-lecture 3 : assemblage v4,
extraction v2, lanceur v2, garde v2 ; l'assemblage v3 et l'extraction v1 restent dans l'arbre parce que `volet_a_chargement_v1` importe
la classe `Ressources` de l'assemblage v3 ; v2 : v1 + `.gitignore` des caches et de l’environnement : sans lui, l’arbre est sale sur la machine et le manifeste refuse ; décision de la mère R-2737 : aucun historique
de la branche sur la machine louée).

Prend chaque fichier de la liste **au commit donné** (`git show <commit>:<chemin>`, jamais l'arbre de travail), vérifie le compagnon
`.sha256` de chaque fichier qui en a un, écrit l'arbre dans un dossier neuf, y crée un dépôt git d'**un seul commit** (auteur
générique, date fixée), puis un paquet `git bundle` de ce seul commit. Rend la liste exacte (chemin, empreinte, taille), l'empreinte
de la liste, le commit réduit et l'empreinte du paquet, pour la demande de feu. Aucune clé ; garde des secrets sur tout l'arbre.

Usage : `python scripts/depot_reduit_neuron_lens_volet_a_v8.py <commit-source> <dossier-sortie-neuf>`
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
NL = "src/controle_ia/neuron_lens/"
MODULES_SCELLES = [NL + m for m in (
    "decisions_volet_a_v4.py", "volet_a_donnees_v1.py", "volet_a_extraction_v1.py", "volet_a_sondes_v2.py", "volet_a_lectures_v2.py",
    "volet_a_course_v3.py", "volet_a_course_v4.py", "volet_a_extraction_v2.py", "volet_a_chargement_v1.py", "volet_a_lancer_v3.py",
    "garde_depense_v3.py")]
ESSAIS = ["tests/" + t for t in (
    "test_neuron_lens_volet_a_donnees_v1.py", "test_neuron_lens_volet_a_donnees_v2.py", "test_neuron_lens_volet_a_extraction_v1.py",
    "test_neuron_lens_volet_a_sondes_v2.py", "test_neuron_lens_volet_a_lectures_v2.py", "test_neuron_lens_volet_a_course_v4.py",
    "test_neuron_lens_volet_a_extraction_v2.py", "test_neuron_lens_volet_a_chargement_v1.py", "test_neuron_lens_volet_a_lancer_v3.py",
    "test_neuron_lens_garde_depense_v3.py")]
SOURCES_C = "docs/sources/neuron-lens-v2-contrastes-20261114/"
DONNEES_SCELLEES = [
    "docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md",
    "docs/notes/neuron-lens-v1/addendum-empreintes-v3.md",
    "docs/notes/neuron-lens-v1/outils/comptes-avant-scellement-v1.json",
    "docs/sources/neuron-lens-v2-addendum-20261114/kept-qwen3-8b.txt",
    *(SOURCES_C + f for f in ("jbb-harmful-behaviors.csv", "jbb-benign-behaviors.csv", "advbench-harmful_behaviors.csv",
                              "repe-facts_true_false.csv", "qwen3-8b-tokenizer.json")),
    "requirements-neuron-lens-volet-a-v1.txt",
    "scripts/amorce_neuron_lens_volet_a_v4.sh",
]
SANS_SCEAU = ["pyproject.toml", "tests/conftest.py", "src/controle_ia/__init__.py", "src/controle_ia/scellement.py",
              "src/controle_ia/manifeste.py", "src/controle_ia/gardes.py", "src/controle_ia/prereg.py", NL + "__init__.py"]
SCELLES = MODULES_SCELLES + ESSAIS + DONNEES_SCELLEES
SECRETS = re.compile(rb"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|gh[opsur]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})")


def liste_fichiers():
    return sorted(SANS_SCEAU + SCELLES + [c + ".sha256" for c in SCELLES])


def _show(commit, chemin, racine=RACINE):
    return subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], check=True, capture_output=True).stdout


def construire(commit: str, sortie: Path, racine=RACINE) -> dict:
    sortie = Path(sortie)
    if sortie.exists():
        raise SystemExit(f"{sortie} existe : dossier neuf exigé (R12)")
    commit = subprocess.run(["git", "-C", str(racine), "rev-parse", commit], check=True, capture_output=True,
                            text=True).stdout.strip()
    arbre = sortie / "depot"
    contenu = {c: _show(commit, c, racine) for c in liste_fichiers()}
    for c in SCELLES:  # compagnon : « <empreinte>  <nom> »
        attendue = contenu[c + ".sha256"].decode().split()[0]
        if hashlib.sha256(contenu[c]).hexdigest() != attendue:
            raise SystemExit(f"compagnon non conforme : {c}")
    if any(SECRETS.search(b) for b in contenu.values()):
        raise SystemExit("garde des secrets : motif trouvé dans l'arbre réduit")
    # écrit par ce script (pas pris au commit) : l'environnement et les caches de la machine ne salissent pas l'arbre, que le
    # manifeste exige propre ; `runs/` et `diag/` restent suivis (écrits après le manifeste, rapatriés)
    contenu[".gitignore"] = b"__pycache__/\n.venv/\n.pytest_cache/\n"
    for c, b in contenu.items():
        (arbre / c).parent.mkdir(parents=True, exist_ok=True)
        (arbre / c).write_bytes(b)
        if c.endswith(".sh"):
            (arbre / c).chmod(0o755)
    env = dict(os.environ, GIT_AUTHOR_NAME="neuron-lens", GIT_AUTHOR_EMAIL="neuron-lens@example.invalid",
               GIT_COMMITTER_NAME="neuron-lens", GIT_COMMITTER_EMAIL="neuron-lens@example.invalid",
               GIT_AUTHOR_DATE="2026-11-14T00:00:00Z", GIT_COMMITTER_DATE="2026-11-14T00:00:00Z")
    g = lambda *a: subprocess.run(["git", "-C", str(arbre), *a], check=True, capture_output=True, text=True, env=env).stdout.strip()
    g("init", "-q", "-b", "course")
    g("add", "-A")
    g("commit", "-q", "-m", f"Neuron Lens, volet A : arbre réduit de {commit}")
    commit_reduit = g("rev-parse", "HEAD")
    paquet = sortie / "neuron-lens-volet-a-reduit.bundle"
    g("bundle", "create", str(paquet), "course")
    lignes = [[c, hashlib.sha256(b).hexdigest(), len(b)] for c, b in sorted(contenu.items())]
    texte_liste = "".join(f"{e}  {c}\n" for c, e, _ in lignes).encode()
    (sortie / "liste-fichiers.sha256").write_bytes(texte_liste)
    rapport = {"commit_source": commit, "commit_reduit": commit_reduit, "n_fichiers": len(lignes),
               "liste_sha256": hashlib.sha256(texte_liste).hexdigest(),
               "paquet": paquet.name, "paquet_sha256": hashlib.sha256(paquet.read_bytes()).hexdigest(), "fichiers": lignes}
    (sortie / "rapport.json").write_text(json.dumps(rapport, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return rapport


if __name__ == "__main__":
    r = construire(sys.argv[1], Path(sys.argv[2]))
    print(json.dumps({k: v for k, v in r.items() if k != "fichiers"}, indent=2, ensure_ascii=False))
