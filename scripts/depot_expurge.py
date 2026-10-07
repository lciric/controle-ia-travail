"""Copie expurgée du dépôt, à montrer à des évaluateurs (décision de Lazar, R-104).

Un seul commit, reproductible, tiré d'un commit cité du dépôt : sans les textes de tiers dont le code n'a pas besoin
(PDF d'arXiv, pages extraites par les lecteurs, texte complet d'un papier, transcriptions non utilisées, pages des
cartes de modèles, fichiers de travail des relecteurs de l'extraction, sorties de l'extraction), sans la candidature à
un autre fonds ni l'ancien paquet git. Les empreintes des fichiers retirés restent, et `EXPURGE.md` les liste. Les
invites transcrites ou adaptées dont le code a besoin restent, avec leur source : le README de la copie le dit.

Rien n'est poussé : le paquet git est écrit dans SORTIE. Sa mise en ligne sur un dépôt distant demande un GO de Lazar.
Le script n'écrit que dans SORTIE, qui ne doit pas exister ; il ne touche pas au dépôt.

    .venv/bin/python scripts/depot_expurge.py COMMIT SORTIE
"""
from __future__ import annotations

import fnmatch
import hashlib
import io
import json
import os
import subprocess
import sys
import tarfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]

# (motif sur le chemin suivi, motif du retrait) ; un fichier `.sha256` compagnon reste, sauf s'il est lui-même visé
RETRAITS = [
    ("docs/sources/pdf/*.pdf", "copie d'un PDF d'arXiv de tiers"),
    ("docs/sources/lecture-pdf-niveau1/*.tar", "fichiers de travail d'un lecteur : pages extraites des PDF de tiers"),
    ("docs/sources/lecture-pdf-niveau2/*.tar", "fichiers de travail d'un lecteur : pages extraites des PDF de tiers"),
    ("docs/sources/invites-2606.08892-v1/extrait.tar", "texte complet extrait d'un papier de tiers"),
    ("docs/sources/invites-2606.07054-v1/*.txt", "transcription d'une invite d'un papier de tiers, non utilisée par le code"),
    ("docs/sources/invites-2606.07054-v1/*.tar", "texte extrait d'un papier de tiers"),
    ("docs/sources/invites-2606.07054-v1/derivees/contre-verification-v1/*.tar",
     "fichiers de travail d'une contre-vérification : texte extrait d'un papier de tiers"),
    ("docs/sources/cartes-modeles-20261006/*.html", "page d'une carte de modèle (site tiers)"),
    ("docs/procedures/T0.5-extraction-v1/contre-lecture/*.tar", "fichiers de travail des relecteurs de l'extraction"),
    ("prereg/contre-lectures/T0.5-pilote-contre-lecture-1-verifications-v1.tar",
     "fichiers de travail d'un relecteur : pages extraites d'un PDF de tiers"),
    ("donnees/*", "sortie de l'extraction : texte dérivé de papiers de tiers"),
    ("livrables/candidature-ea-funds-v1/*", "candidature à un autre fonds, confidentielle"),
    ("livrables/candidature-ea-funds-v1.zip", "candidature à un autre fonds, confidentielle"),
    ("livrables/candidature-ea-funds-v1.zip.sha256", "candidature à un autre fonds, confidentielle"),
    ("livrables/controle-ia-v1.bundle", "ancien paquet git, historique non expurgé"),
    ("livrables/controle-ia-v1.bundle.sha256", "ancien paquet git, historique non expurgé"),
]

PARAGRAPHE_README = ("This private repository holds copies of third-party arXiv PDFs (`docs/sources/pdf/`) and extraction "
                     "outputs that contain text derived from those papers (`donnees/`). They are kept for verification "
                     "only, are not redistributable, and will be removed before any publication. Please do not copy them.")
REMPLACEMENT_README = ("This copy omits the third-party PDFs, the page texts extracted from them, and the outputs derived "
                       "from them; their SHA-256 hashes remain, and `EXPURGE.md` lists every omitted file. It keeps the "
                       "short prompt texts transcribed or adapted from two papers (arXiv 2606.08892 and 2606.07054), "
                       "because the code loads them; they are attributed to their sources. Please do not redistribute.")


def _git(*args: str, cwd: Path = RACINE, env: dict | None = None, entree: bytes | None = None) -> bytes:
    return subprocess.run(["git", *args], cwd=cwd, env=env, input=entree, capture_output=True, check=True).stdout


def motif_de(chemin: str) -> str | None:
    for motif, raison in RETRAITS:
        if fnmatch.fnmatchcase(chemin, motif):
            return raison
    return None


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    commit = _git("rev-parse", "--verify", argv[0] + "^{commit}").decode().strip()
    sortie = Path(argv[1]).resolve()
    if sortie.exists():
        print(f"{sortie} existe déjà : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    if RACINE.resolve() in (sortie, *sortie.parents):
        print("SORTIE ne doit pas être dans le dépôt", file=sys.stderr)
        return 2
    arbre = sortie / "controle-ia-expurge"
    arbre.mkdir(parents=True)
    retraits, gardes = [], 0
    with tarfile.open(fileobj=io.BytesIO(_git("archive", "--format=tar", commit))) as tar:
        for membre in tar.getmembers():
            if not membre.isfile():
                continue
            contenu = tar.extractfile(membre).read()
            raison = motif_de(membre.name)
            if raison:
                retraits.append({"chemin": membre.name, "sha256": hashlib.sha256(contenu).hexdigest(),
                                 "octets": len(contenu), "motif": raison})
                continue
            cible = arbre / membre.name
            cible.parent.mkdir(parents=True, exist_ok=True)
            cible.write_bytes(contenu)
            os.chmod(cible, membre.mode & 0o777)
            gardes += 1
    readme = arbre / "README.md"
    texte = readme.read_text(encoding="utf-8")
    if texte.count(PARAGRAPHE_README) != 1:
        print("paragraphe du README introuvable : arrêt (aucun paquet écrit)", file=sys.stderr)
        return 1
    readme.write_text(texte.replace(PARAGRAPHE_README, REMPLACEMENT_README), encoding="utf-8")
    pdf = sorted(r["chemin"] for r in retraits if r["chemin"].startswith("docs/sources/pdf/"))
    lignes = ["# What this copy omits", "",
              f"Copy of the private repository `controle-ia` at commit `{commit}`, made for evaluators by "
              "`scripts/depot_expurge.py` (same commit). Third-party texts that the code does not need are omitted, "
              "together with an application to another funder and an old git bundle. Their SHA-256 hashes remain "
              "(companion `.sha256` files, and the table below), so anyone holding the originals can check them.", "",
              "`python -m controle_ia.scellement verifier-arbre .` reports each omitted sealed file as an orphan "
              "hash; that is expected. The README's paragraph on third-party material was adapted for this copy.", "",
              f"- Files kept: {gardes}. Files omitted: {len(retraits)} ({sum(r['octets'] for r in retraits) / 1e6:.1f} MB).",
              "- Kept on purpose: the prompt texts transcribed from arXiv 2606.08892 "
              "(`docs/sources/invites-2606.08892-v1/`) and the prompt templates adapted from arXiv 2606.07054 "
              "(`docs/sources/invites-2606.07054-v1/derivees/`), which the code loads after checking their hashes.", "",
              "## arXiv papers whose PDF copies are omitted", ""]
    lignes += [f"- [{Path(p).stem}](https://arxiv.org/abs/{Path(p).stem})" for p in pdf]
    lignes += ["", "## Omitted files", "", "| path | SHA-256 | reason (in French) |", "|---|---|---|"]
    lignes += [f"| `{r['chemin']}` | `{r['sha256']}` | {r['motif']} |" for r in retraits]
    (arbre / "EXPURGE.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    date = _git("show", "-s", "--format=%cI", commit).decode().strip()
    env = dict(os.environ, GIT_AUTHOR_NAME="controle-ia (copie expurgée)", GIT_AUTHOR_EMAIL="copie-expurgee@invalid",
               GIT_COMMITTER_NAME="controle-ia (copie expurgée)", GIT_COMMITTER_EMAIL="copie-expurgee@invalid",
               GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
    _git("init", "-q", "-b", "main", cwd=arbre, env=env)
    _git("add", "-A", cwd=arbre, env=env)
    _git("-c", "commit.gpgsign=false", "commit", "-q", "-m",
         f"Copie expurgée de controle-ia au commit {commit} (textes de tiers omis ; voir EXPURGE.md)", cwd=arbre, env=env)
    copie = _git("rev-parse", "HEAD", cwd=arbre).decode().strip()
    paquet = sortie / f"controle-ia-expurge-{commit[:7]}.bundle"
    _git("bundle", "create", "-q", str(paquet), "main", cwd=arbre, env=env)
    bilan = {"commit_source": commit, "commit_copie": copie, "fichiers_gardes": gardes, "fichiers_retires": len(retraits),
             "paquet": paquet.name, "paquet_sha256": hashlib.sha256(paquet.read_bytes()).hexdigest(),
             "retraits": retraits}
    (sortie / "bilan.json").write_text(json.dumps(bilan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in bilan.items() if k != "retraits"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
