"""Téléchargement des seules données publiques de l'étalonnage court de la prédiction
de liens entre littératures (version 1).

À n'exécuter qu'après scellement du préenregistrement (R1) : le script refuse de
partir si le préenregistrement scellé ou son empreinte compagnon manque ou ne
correspond pas.

Sorties (hors dépôt, jamais versées) : un dossier de données neuf passé en argument.
Journal versé : `journal-telechargement-v1.json` (noms, tailles, empreintes, licences).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ICI = Path(__file__).resolve().parent
PREREG = ICI / "prereg-rang4-etalonnage-pont-v1.md"

SOURCES = {
    "relation2pubtator3.gz": {
        "url": "https://ftp.ncbi.nlm.nih.gov/pub/lu/PubTator3/relation2pubtator3.gz",
        "licence": "domaine public (United States Government Work, README.txt de PubTator3)",
    },
    "scimuse_full_dynamic_graph.zip": {
        "url": "https://zenodo.org/records/13900962/files/scimuse_full_dynamic_graph.zip?download=1",
        "licence": "CC BY 4.0 (notice Zenodo 13900962)",
        "md5": "9e0546256c44ef2708c0fe9260a036a8",
    },
}
DEPOT_SCIMUSE = "https://github.com/artificial-scientist-lab/scimuse"
COMMIT_SCIMUSE = "0be934a2b04aa8177ab62ea2829c19a3f10772e5"
FICHIERS_SCIMUSE = ["graph_feature_plot/evaluation_feature_dataset.csv", "concept", "LICENSE"]


class ErreurTelechargement(RuntimeError):
    pass


def empreintes(chemin: Path) -> tuple[str, str]:
    h, m = hashlib.sha256(), hashlib.md5()
    with chemin.open("rb") as f:
        for bloc in iter(lambda: f.read(1 << 22), b""):
            h.update(bloc)
            m.update(bloc)
    return h.hexdigest(), m.hexdigest()


def verifier_prereg_scelle() -> str:
    compagnon = PREREG.with_name(PREREG.name + ".sha256")
    if not PREREG.is_file() or not compagnon.is_file():
        raise ErreurTelechargement("préenregistrement scellé ou empreinte compagnon absent : aucun téléchargement")
    attendu = compagnon.read_text(encoding="utf-8").split()[0]
    obtenu = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if attendu != obtenu:
        raise ErreurTelechargement("empreinte du préenregistrement non conforme : aucun téléchargement")
    return obtenu


def telecharger(url: str, cible: Path, essais: int = 4) -> None:
    for k in range(essais):
        try:
            tmp = cible.with_suffix(cible.suffix + ".partiel")
            with urllib.request.urlopen(url, timeout=120) as r, tmp.open("wb") as f:
                while True:
                    bloc = r.read(1 << 22)
                    if not bloc:
                        break
                    f.write(bloc)
            tmp.rename(cible)
            return
        except Exception as e:  # réseau : relance bornée, journalisée
            print(f"essai {k + 1} échoué pour {url} : {e}", file=sys.stderr)
            time.sleep(2 ** (k + 1))
    raise ErreurTelechargement(f"téléchargement impossible : {url}")


def main(dossier: str) -> None:
    empreinte_prereg = verifier_prereg_scelle()
    d = Path(dossier)
    d.mkdir(parents=True, exist_ok=True)
    journal = {"prereg_sha256": empreinte_prereg, "date_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "fichiers": []}
    for nom, s in SOURCES.items():
        cible = d / nom
        if not cible.exists():
            telecharger(s["url"], cible)
        sha, md5 = empreintes(cible)
        if "md5" in s and md5 != s["md5"]:
            raise ErreurTelechargement(f"somme MD5 non conforme pour {nom} : {md5}")
        journal["fichiers"].append({"nom": nom, "url": s["url"], "licence": s["licence"], "octets": cible.stat().st_size, "sha256": sha, "md5": md5})
    depot = d / "scimuse"
    if not depot.exists():
        subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", DEPOT_SCIMUSE, str(depot)], check=True,
                       env={"GIT_LFS_SKIP_SMUDGE": "1", "PATH": "/usr/bin:/bin"})
    for nom in FICHIERS_SCIMUSE:
        contenu = subprocess.run(["git", "-C", str(depot), "show", f"{COMMIT_SCIMUSE}:{nom}"], check=True, capture_output=True).stdout
        cible = d / ("scimuse_" + nom.replace("/", "__"))
        cible.write_bytes(contenu)
        sha, md5 = empreintes(cible)
        journal["fichiers"].append({"nom": nom, "url": f"{DEPOT_SCIMUSE}@{COMMIT_SCIMUSE}", "licence": "MIT (LICENSE du dépôt SciMuse)", "octets": cible.stat().st_size, "sha256": sha, "md5": md5})
    sortie = ICI / "journal-telechargement-v1.json"
    sortie.write_text(json.dumps(journal, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(journal, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
