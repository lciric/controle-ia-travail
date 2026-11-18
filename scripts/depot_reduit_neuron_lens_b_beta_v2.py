"""Dépôt réduit à l'arbre utile pour la course de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale) — v2.

v2 = v1 (`depot_reduit_neuron_lens_b_beta_v1.py`, `731bc401…`) avec le code de course v2, ses essais (étapes câblées, gardes du
montage) et `garde_depense_v4.py` que ceux-ci importent.

Même méthode que le dépôt réduit v12 de la tranche des lentilles publiques (`depot_reduit_neuron_lens_b_alpha_v12.py`, contre-lu), sauf :
le code voisin n'est **pas** mis dans l'arbre (le lanceur le clone sur la machine au commit épinglé `849bfe16` et en vérifie l'arbre
`b22006e9…` : l'essai du correctif (4) exige un dépôt git à ce commit) ; et le `.gitignore` écrit ici exclut ce que la course crée dans
l'arbre (`voisin/`, `voisin-banc/`, `originaux/`), pour que le manifeste trouve l'arbre propre.

Prend chacun de nos fichiers **au commit donné** (`git show <commit>:<chemin>`, jamais l'arbre de travail), vérifie le compagnon `.sha256`
de chaque fichier scellé, écrit l'arbre dans un dossier neuf, y crée un dépôt git d'**un seul commit** (auteur générique, date fixée), puis
un paquet `git bundle`. Rend la liste exacte (chemin, empreinte, taille), l'empreinte de la liste, le commit réduit et l'empreinte du
paquet, pour la demande de feu. Aucune clé ; garde des secrets sur tout l'arbre ; aucun fichier de plus de 95 Mo.

Usage : `python scripts/depot_reduit_neuron_lens_b_beta_v2.py <commit-source> <dossier-sortie-neuf>`
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
CA = "docs/notes/neuron-lens-v1/correctifs/"
CB = "docs/notes/neuron-lens-v1/correctifs-b-beta/"
MODULES_SCELLES = [NL + m for m in (
    "controles_b_beta_v2.py", "verdicts_b_beta_v4.py", "grandeurs_b_alpha_v1.py", "verdicts_b_alpha_v3.py", "addendum_partie2_b_beta_v2.py",
    "b_beta_lancer_v2.py", "controles_b0_v2.py", "balayage_arbre_v1.py", "suivi_vast_v6.py", "garde_depense_v4.py")]
ESSAIS = ["tests/" + t for t in (
    "test_neuron_lens_verdicts_b_beta_v4.py", "test_neuron_lens_controles_b_beta_v2.py", "test_neuron_lens_b_beta_lancer_v2.py",
    "test_neuron_lens_etapes_b_beta_v2.py", "test_neuron_lens_montage_b_beta_v2.py",
    "test_neuron_lens_grandeurs_b_alpha_v1.py", "test_neuron_lens_verdicts_b_alpha_v3.py", "test_neuron_lens_balayage_arbre_v1.py")]
DONNEES_SCELLEES = [
    "docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md",
    "docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md",
    "docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md",
    "diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json",
    "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json",
    "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/reads_at_firings_qwen3-8b.json",
    *(CA + f for f in ("06_activations-llama-v2.diff", "lenses-neuronpedia-llama-v2.diff", "provenance-chat-llama-v1.diff",
                       "causal_lens-graine-v1.diff", "essai-06_activations-llama-v3.py", "essai-lenses-neuronpedia-v3.py",
                       "essai-causal_lens-graine-v1.py", "essai-crochets-causal_lens-llama-v1.py")),
    *(CB + f for f in ("lens_compare-llama-v2.diff", "essai-lens_compare-llama-v2.py", "essai-transport-llama-miniature-v3.py")),
    "requirements-neuron-lens-b-beta-v2.txt",
    "scripts/amorce_neuron_lens_b_beta_v2.sh",
]
SANS_SCEAU = ["pyproject.toml", "tests/conftest.py", "src/controle_ia/__init__.py", "src/controle_ia/scellement.py",
              "src/controle_ia/manifeste.py", "src/controle_ia/gardes.py", "src/controle_ia/prereg.py", NL + "__init__.py"]
SCELLES = MODULES_SCELLES + ESSAIS + DONNEES_SCELLEES
SECRETS = re.compile(rb"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|gh[opsur]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})")
LIMITE = 95 * 1024 * 1024
GITIGNORE = b"__pycache__/\n.venv/\n.pytest_cache/\n/voisin/\n/voisin-banc/\n/originaux/\n"


def liste_fichiers():
    return sorted(SANS_SCEAU + SCELLES + [c + ".sha256" for c in SCELLES])


def _show(commit, chemin, racine=RACINE):
    return subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], check=True, capture_output=True).stdout


def construire(commit: str, sortie: Path, racine=RACINE) -> dict:
    sortie = Path(sortie)
    if sortie.exists():
        raise SystemExit(f"{sortie} existe : dossier neuf exigé (R12)")
    commit = subprocess.run(["git", "-C", str(racine), "rev-parse", commit], check=True, capture_output=True, text=True).stdout.strip()
    arbre = sortie / "depot"
    contenu = {c: _show(commit, c, racine) for c in liste_fichiers()}
    for c in SCELLES:  # compagnon : « <empreinte>  <nom> »
        if hashlib.sha256(contenu[c]).hexdigest() != contenu[c + ".sha256"].decode().split()[0]:
            raise SystemExit(f"compagnon non conforme : {c}")
    trouves = sorted(c for c, b in contenu.items() if SECRETS.search(b))
    if trouves:
        raise SystemExit(f"garde des secrets : motif trouvé dans l'arbre réduit : {trouves}")
    gros = sorted(c for c, b in contenu.items() if len(b) > LIMITE)
    if gros:
        raise SystemExit(f"fichiers de plus de 95 Mo : {gros}")
    contenu[".gitignore"] = GITIGNORE
    for c, b in contenu.items():
        (arbre / c).parent.mkdir(parents=True, exist_ok=True)
        (arbre / c).write_bytes(b)
        if c.endswith(".sh"):
            (arbre / c).chmod(0o755)
    env = dict(os.environ, GIT_AUTHOR_NAME="neuron-lens", GIT_AUTHOR_EMAIL="neuron-lens@example.invalid",
               GIT_COMMITTER_NAME="neuron-lens", GIT_COMMITTER_EMAIL="neuron-lens@example.invalid",
               GIT_AUTHOR_DATE="2026-11-19T00:00:00Z", GIT_COMMITTER_DATE="2026-11-19T00:00:00Z")
    g = lambda *a: subprocess.run(["git", "-C", str(arbre), *a], check=True, capture_output=True, text=True, env=env).stdout.strip()
    g("init", "-q", "-b", "course")
    g("add", "-A")
    g("commit", "-q", "-m", f"Neuron Lens, ajustement de nos lentilles : arbre réduit de {commit}")
    commit_reduit = g("rev-parse", "HEAD")
    if g("status", "--porcelain"):
        raise SystemExit("arbre réduit non propre après le commit")
    paquet = sortie / "neuron-lens-b-beta-reduit.bundle"
    g("bundle", "create", str(paquet), "course")
    lignes = [[c, hashlib.sha256(b).hexdigest(), len(b)] for c, b in sorted(contenu.items())]
    texte_liste = "".join(f"{e}  {c}\n" for c, e, _ in lignes).encode()
    (sortie / "liste-fichiers.sha256").write_bytes(texte_liste)
    rapport = {"commit_source": commit, "commit_reduit": commit_reduit, "n_fichiers": len(lignes),
               "liste_sha256": hashlib.sha256(texte_liste).hexdigest(), "paquet": paquet.name,
               "paquet_sha256": hashlib.sha256(paquet.read_bytes()).hexdigest(), "fichiers": lignes}
    (sortie / "rapport.json").write_text(json.dumps(rapport, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return rapport


if __name__ == "__main__":
    r = construire(sys.argv[1], Path(sys.argv[2]))
    print(json.dumps({k: v for k, v in r.items() if k != "fichiers"}, indent=2, ensure_ascii=False))
