"""Dépôt réduit à l'arbre utile pour la course de la tranche B-α de « Neuron Lens » — v5 (v4 avec le lanceur v2, ses essais v2 et l'amorce v4). v4 : v3 avec l'amorce B-α v3. v3 : v2 avec l'amorce B-α v2. v2 : v1 + la référence publiée de Qwen3-8B que
lisent les essais du code des verdicts (B.3) : sans elle, ils échouent dans l'arbre réduit — essai d'intégration du 2026-11-15). v1 :
pièce 5 du § 6 du devis B-α v2 ; même méthode que le dépôt réduit v10 du volet A.

Prend chacun de nos fichiers **au commit donné** (`git show <commit>:<chemin>`, jamais l'arbre de travail) et vérifie le compagnon
`.sha256` de chaque fichier qui en a un ; prend le code du dépôt voisin `stdlogits/neuron-lens` **au commit `849bfe16`** par
`git archive` de la copie de lecture (arbre `b22006e9…` exigé), placé sous `voisin/neuron-lens/`, **sans les correctifs** (le lanceur
les applique et vérifie les empreintes avant et après) ; écrit l'arbre dans un dossier neuf, y crée un dépôt git d'**un seul commit**
(auteur générique, date fixée), puis un paquet `git bundle` de ce seul commit. Rend la liste exacte (chemin, empreinte, taille),
l'empreinte de la liste, le commit réduit et l'empreinte du paquet, pour la demande de feu. Aucune clé ; garde des secrets sur tout
l'arbre ; aucun fichier de plus de 95 Mo.

Usage : `python scripts/depot_reduit_neuron_lens_b_alpha_v5.py <commit-source> <dossier-sortie-neuf> [<copie-de-lecture-du-voisin>]`
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tarfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
VOISIN_LECTURE = Path("/home/user/stdlogits/neuron-lens")
COMMIT_VOISIN = "849bfe1678e28becceb1e3864afe5fc8297d02e4"
ARBRE_VOISIN = "b22006e91067d517b758cf755246fd8d2f5c2ca4"
NL = "src/controle_ia/neuron_lens/"
CORR = "docs/notes/neuron-lens-v1/correctifs/"
MODULES_SCELLES = [NL + m for m in (
    "verdicts_b_alpha_v3.py", "controles_b0_v2.py", "grandeurs_b_alpha_v1.py", "addendum_partie2_b_alpha_v1.py", "b_alpha_lancer_v2.py",
    "balayage_arbre_v1.py", "suivi_vast_v6.py")]
ESSAIS = ["tests/" + t for t in (
    "test_neuron_lens_verdicts_b_alpha_v3.py", "test_neuron_lens_grandeurs_b_alpha_v1.py", "test_neuron_lens_addendum_partie2_b_alpha_v1.py",
    "test_neuron_lens_b_alpha_lancer_v2.py", "test_neuron_lens_balayage_arbre_v1.py")]
CONFIG_NP = "docs/sources/neuron-lens-b-alpha-neuronpedia-config-20261115/"
DONNEES_SCELLEES = [
    "docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md",
    "docs/notes/neuron-lens-v1/addendum-empreintes-v3.md",
    "docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v2.md",
    "docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json",
    *(CORR + f for f in ("06_activations-llama-v2.diff", "lenses-neuronpedia-llama-v2.diff", "provenance-chat-llama-v1.diff",
                         "causal_lens-graine-v1.diff", "essai-06_activations-llama-v3.py", "essai-lenses-neuronpedia-v3.py",
                         "essai-causal_lens-graine-v1.py", "essai-crochets-causal_lens-llama-v1.py")),
    *(CONFIG_NP + f for f in ("jlens-Salesforce-wikitext-config.yaml", "jpp-Salesforce-wikitext-CREDIT.md",
                              "jpp-Salesforce-wikitext-config.yaml", "rlens-Salesforce-wikitext-CREDIT.md",
                              "rlens-Salesforce-wikitext-config.yaml")),
    "requirements-neuron-lens-b-alpha-v1.txt",
    "scripts/amorce_neuron_lens_b_alpha_v4.sh",
]
SANS_SCEAU = ["pyproject.toml", "tests/conftest.py", "src/controle_ia/__init__.py", "src/controle_ia/scellement.py",
              "src/controle_ia/manifeste.py", "src/controle_ia/gardes.py", "src/controle_ia/prereg.py", NL + "__init__.py"]
SCELLES = MODULES_SCELLES + ESSAIS + DONNEES_SCELLEES
SECRETS = re.compile(rb"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|gh[opsur]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})")
LIMITE = 95 * 1024 * 1024


def liste_fichiers():
    return sorted(SANS_SCEAU + SCELLES + [c + ".sha256" for c in SCELLES])


def _show(commit, chemin, racine=RACINE):
    return subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], check=True, capture_output=True).stdout


def voisin(copie: Path) -> dict:
    """{chemin sous voisin/neuron-lens/ : contenu} du dépôt voisin à COMMIT_VOISIN (arbre exigé), modes exécutables gardés à part."""
    arbre = subprocess.run(["git", "-C", str(copie), "rev-parse", f"{COMMIT_VOISIN}^{{tree}}"], check=True, capture_output=True,
                           text=True).stdout.strip()
    if arbre != ARBRE_VOISIN:
        raise SystemExit(f"arbre du dépôt voisin {arbre} ≠ {ARBRE_VOISIN}")
    brut = subprocess.run(["git", "-C", str(copie), "archive", "--format=tar", COMMIT_VOISIN], check=True, capture_output=True).stdout
    out, executables = {}, set()
    with tarfile.open(fileobj=io.BytesIO(brut)) as t:
        for m in t.getmembers():
            if m.isdir():
                continue
            if not m.isfile():
                raise SystemExit(f"dépôt voisin : entrée non ordinaire refusée : {m.name}")
            c = "voisin/neuron-lens/" + m.name
            out[c] = t.extractfile(m).read()
            if m.mode & 0o111:
                executables.add(c)
    return {"fichiers": out, "executables": executables}


def construire(commit: str, sortie: Path, racine=RACINE, copie_voisin=VOISIN_LECTURE) -> dict:
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
    v = voisin(copie_voisin)
    if set(v["fichiers"]) & set(contenu):
        raise SystemExit("collision de chemins entre nos fichiers et le dépôt voisin")
    contenu |= v["fichiers"]
    trouves = sorted(c for c, b in contenu.items() if SECRETS.search(b))
    if trouves:
        raise SystemExit(f"garde des secrets : motif trouvé dans l'arbre réduit : {trouves}")
    gros = sorted(c for c, b in contenu.items() if len(b) > LIMITE)
    if gros:
        raise SystemExit(f"fichiers de plus de 95 Mo : {gros}")
    # écrit par ce script : l'environnement et les caches de la machine ne salissent pas l'arbre (le manifeste l'exige propre)
    contenu[".gitignore"] = b"__pycache__/\n.venv/\n.pytest_cache/\n"
    for c, b in contenu.items():
        (arbre / c).parent.mkdir(parents=True, exist_ok=True)
        (arbre / c).write_bytes(b)
        if c.endswith(".sh") or c in v["executables"]:
            (arbre / c).chmod(0o755)
    env = dict(os.environ, GIT_AUTHOR_NAME="neuron-lens", GIT_AUTHOR_EMAIL="neuron-lens@example.invalid",
               GIT_COMMITTER_NAME="neuron-lens", GIT_COMMITTER_EMAIL="neuron-lens@example.invalid",
               GIT_AUTHOR_DATE="2026-11-15T00:00:00Z", GIT_COMMITTER_DATE="2026-11-15T00:00:00Z")
    g = lambda *a: subprocess.run(["git", "-C", str(arbre), *a], check=True, capture_output=True, text=True, env=env).stdout.strip()
    g("init", "-q", "-b", "course")
    g("add", "-A")
    g("commit", "-q", "-m", f"Neuron Lens, tranche B-α : arbre réduit de {commit} et code voisin à {COMMIT_VOISIN}")
    commit_reduit = g("rev-parse", "HEAD")
    if g("status", "--porcelain"):
        raise SystemExit("arbre réduit non propre après le commit")
    paquet = sortie / "neuron-lens-b-alpha-reduit.bundle"
    g("bundle", "create", str(paquet), "course")
    lignes = [[c, hashlib.sha256(b).hexdigest(), len(b)] for c, b in sorted(contenu.items())]
    texte_liste = "".join(f"{e}  {c}\n" for c, e, _ in lignes).encode()
    (sortie / "liste-fichiers.sha256").write_bytes(texte_liste)
    rapport = {"commit_source": commit, "commit_reduit": commit_reduit, "commit_voisin": COMMIT_VOISIN, "arbre_voisin": ARBRE_VOISIN,
               "n_fichiers": len(lignes), "n_fichiers_voisin": len(v["fichiers"]),
               "liste_sha256": hashlib.sha256(texte_liste).hexdigest(),
               "paquet": paquet.name, "paquet_sha256": hashlib.sha256(paquet.read_bytes()).hexdigest(), "fichiers": lignes}
    (sortie / "rapport.json").write_text(json.dumps(rapport, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return rapport


if __name__ == "__main__":
    r = construire(sys.argv[1], Path(sys.argv[2]), copie_voisin=Path(sys.argv[3]) if len(sys.argv) > 3 else VOISIN_LECTURE)
    print(json.dumps({k: v for k, v in r.items() if k != "fichiers"}, indent=2, ensure_ascii=False))
