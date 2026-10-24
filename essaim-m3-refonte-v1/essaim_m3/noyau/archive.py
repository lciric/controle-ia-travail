"""Archive des générations : tout est gardé, scellé, jamais réécrit (R6, R12).

`archive/<lignée>/g<NNN>/` : l'organisme (archive tar et empreinte), le contexte reçu, le dossier de travail entier
(réponses, successeur, conception, journaux de l'organisme), le journal des appels du noyau, le score externe et un
résumé. `archive/index.jsonl` : une ligne par génération, ajoutée, jamais modifiée. L'organisme lit l'archive en
lecture seule : c'est sa mémoire inter-générations s'il le souhaite, et celle de toutes les lignées.
"""
from __future__ import annotations

import datetime as _dt
import gzip
import hashlib
import json
import os
import pathlib
import shutil
import tarfile


def empreinte_fichier(chemin: pathlib.Path) -> str:
    h = hashlib.sha256()
    with chemin.open("rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def sceller(chemin: pathlib.Path) -> pathlib.Path:
    compagnon = chemin.with_name(chemin.name + ".sha256")
    compagnon.write_text(f"{empreinte_fichier(chemin)}  {chemin.name}\n", encoding="utf-8")
    return compagnon


def archiver_organisme(organisme: pathlib.Path, cible: pathlib.Path) -> str:
    """Archive tar reproductible (dates et propriétaires neutralisés) de `organisme/` ; rend son empreinte."""
    def neutraliser(info: tarfile.TarInfo) -> tarfile.TarInfo:
        info.uid = info.gid = 0
        info.uname = info.gname = ""
        info.mtime = 0
        return info
    with open(cible, "wb") as brut, gzip.GzipFile(filename="", mode="wb", fileobj=brut, mtime=0, compresslevel=6) as gz, \
            tarfile.open(fileobj=gz, mode="w") as tar:
        for f in sorted(organisme.rglob("*")):
            if f.is_file():
                tar.add(f, arcname=str(pathlib.Path("organisme") / f.relative_to(organisme)), filter=neutraliser)
    sceller(cible)
    return empreinte_fichier(cible)


class Archive:
    def __init__(self, racine: pathlib.Path):
        self.racine = pathlib.Path(racine)
        self.racine.mkdir(parents=True, exist_ok=True)
        self.index = self.racine / "index.jsonl"

    def dossier(self, lignee: str, generation: int) -> pathlib.Path:
        d = self.racine / lignee / f"g{generation:03d}"
        if d.exists():
            raise FileExistsError(f"génération déjà archivée : {d} (rien n'est réécrit)")
        d.mkdir(parents=True)
        return d

    def deposer(self, lignee: str, generation: int, organisme: pathlib.Path, dossier_travail: pathlib.Path,
                journal_appels: pathlib.Path | None, score: dict, resume: dict) -> dict:
        d = self.dossier(lignee, generation)
        empreinte = archiver_organisme(organisme, d / "organisme.tar.gz")
        travail = d / "travail"
        shutil.copytree(dossier_travail, travail, symlinks=False,
                        ignore=shutil.ignore_patterns("noyau_client.py", "lanceur.py", "__pycache__"))
        if journal_appels and journal_appels.exists():
            shutil.copy2(journal_appels, d / "journal-appels.jsonl")
            sceller(d / "journal-appels.jsonl")
        (d / "score.json").write_text(json.dumps(score, ensure_ascii=False, indent=1), encoding="utf-8")
        sceller(d / "score.json")
        ligne = {"lignee": lignee, "generation": generation, "score": score.get("score"), "statut": resume.get("statut"),
                 "cout_usd": resume.get("cout_usd"), "n_appels": resume.get("n_appels"), "chemin": str(d.relative_to(self.racine)),
                 "empreinte_organisme": empreinte, "successeur": resume.get("successeur"),
                 "quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        (d / "resume.json").write_text(json.dumps({**resume, **ligne}, ensure_ascii=False, indent=1), encoding="utf-8")
        sceller(d / "resume.json")
        with self.index.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")
        # lecture seule pour tout ce qui vient d'être déposé (efficace hors root ; consigné sinon)
        for f in d.rglob("*"):
            try:
                os.chmod(f, 0o555 if f.is_dir() else 0o444)
            except OSError:
                pass
        return ligne

    def lignes(self, lignee: str | None = None) -> list[dict]:
        if not self.index.exists():
            return []
        out = [json.loads(l) for l in self.index.read_text(encoding="utf-8").splitlines() if l.strip()]
        return [l for l in out if lignee is None or l["lignee"] == lignee]

    def historique(self, lignee: str) -> list[dict]:
        return [{"generation": l["generation"], "lignee": l["lignee"], "score": l["score"], "statut": l["statut"],
                 "cout_usd": l["cout_usd"], "n_appels": l["n_appels"]} for l in self.lignes(lignee)]
