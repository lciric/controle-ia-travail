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


CHAMPS_VUE = ("lignee", "generation", "phase", "score", "statut", "cout_usd", "n_appels", "successeur", "metrique_proposee",
              "n_reponses_test", "empreinte_organisme", "quand_utc", "refus_noyau", "problemes_successeur", "relance", "impose", "famille")


class Archive:
    """`racine/` : archive complète, pour le noyau et l'audit (dont `juge/` : réponses de test, scores, score final).
    `vue/` : ce qu'un organisme peut lire — le code des générations, leurs résumés publics et leurs dossiers de
    travail sans les réponses de test ni les fichiers du juge ni le journal du noyau (constat de session-depot :
    sinon un organisme apprend le juge ou recopie les réponses d'une autre lignée)."""

    def __init__(self, racine: pathlib.Path, vue: pathlib.Path | None = None):
        self.racine = pathlib.Path(racine)
        self.racine.mkdir(parents=True, exist_ok=True)
        self.index = self.racine / "index.jsonl"
        self.vue = pathlib.Path(vue) if vue is not None else self.racine.parent / (self.racine.name + "_vue")
        self.vue.mkdir(parents=True, exist_ok=True)
        try:  # CR-01 : l'archive complète (vérités, juge, journaux) est au noyau seul ; la vue est lisible par les organismes
            os.chmod(self.racine, 0o700)
            os.chmod(self.vue, 0o755)
        except OSError:
            pass

    @staticmethod
    def nom_generation(generation: int, phase: str | None = None) -> str:
        """`gNNN` pour une génération notée ; `cNNN` pour une ronde de la phase de conception (jamais notée)."""
        return f"{'c' if phase == 'conception' else 'g'}{generation:03d}"

    def dossier(self, lignee: str, generation: int, phase: str | None = None) -> pathlib.Path:
        d = self.racine / lignee / self.nom_generation(generation, phase)
        if d.exists():
            raise FileExistsError(f"génération déjà archivée : {d} (rien n'est réécrit)")
        d.mkdir(parents=True)
        return d

    def deposer(self, lignee: str, generation: int, organisme: pathlib.Path, dossier_travail: pathlib.Path,
                journal_appels: pathlib.Path | None, score: dict, resume: dict, score_final: dict | None = None,
                phase: str | None = None) -> dict:
        d = self.dossier(lignee, generation, phase)
        empreinte = archiver_organisme(organisme, d / "organisme.tar.gz")
        travail = d / "travail"
        shutil.copytree(dossier_travail, travail, symlinks=False,
                        ignore=shutil.ignore_patterns("noyau_client.py", "lanceur.py", "__pycache__"))
        juge = d / "juge"
        juge.mkdir()
        if journal_appels and journal_appels.exists():
            shutil.copy2(journal_appels, d / "journal-appels.jsonl")
            sceller(d / "journal-appels.jsonl")
        (juge / "score.json").write_text(json.dumps(score, ensure_ascii=False, indent=1), encoding="utf-8")
        sceller(juge / "score.json")
        if score_final is not None:
            (juge / "score-final.json").write_text(json.dumps(score_final, ensure_ascii=False, indent=1), encoding="utf-8")
            sceller(juge / "score-final.json")
        if (travail / "reponses_test.json").exists():
            shutil.move(str(travail / "reponses_test.json"), str(juge / "reponses_test.json"))
            sceller(juge / "reponses_test.json")
        ligne = {"lignee": lignee, "generation": generation, "phase": phase, "score": score.get("score"), "statut": resume.get("statut"),
                 "cout_usd": resume.get("cout_usd"), "n_appels": resume.get("n_appels"), "chemin": str(d.relative_to(self.racine)),
                 "empreinte_organisme": empreinte, "successeur": resume.get("successeur"),
                 "impose": resume.get("impose"), "famille": resume.get("famille"),
                 "problemes_successeur": [str(x)[:200] for x in (resume.get("problemes_successeur") or [])][:10],
                 "relance": bool(resume.get("relance")), "invalide": bool(resume.get("invalide")),
                 "quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        complet = {**resume, **ligne}
        (d / "resume.json").write_text(json.dumps(complet, ensure_ascii=False, indent=1), encoding="utf-8")
        sceller(d / "resume.json")
        with self.index.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")
        # vue pour les organismes : code, résumé public, travail sans le juge ni le journal du noyau
        v = self.vue / lignee / self.nom_generation(generation, phase)
        v.mkdir(parents=True, exist_ok=True)
        shutil.copy2(d / "organisme.tar.gz", v / "organisme.tar.gz")
        shutil.copy2(d / "organisme.tar.gz.sha256", v / "organisme.tar.gz.sha256")
        (v / "resume.json").write_text(json.dumps({k: complet.get(k) for k in CHAMPS_VUE}, ensure_ascii=False, indent=1), encoding="utf-8")
        shutil.copytree(travail, v / "travail", symlinks=False, ignore=shutil.ignore_patterns("noyau", "juge", "reponses_test.json", "attaques.json"))
        # la vue est en lecture seule pour tous (dossiers 0555, fichiers 0444) : les organismes, sous un autre utilisateur, lisent sans écrire
        for f in [v] + list(v.rglob("*")):
            try:
                os.chmod(f, 0o555 if f.is_dir() else 0o444)
            except OSError:
                pass
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
        return [{"generation": l["generation"], "phase": l.get("phase"), "lignee": l["lignee"], "score": l["score"], "statut": l["statut"],
                 "cout_usd": l["cout_usd"], "n_appels": l["n_appels"], "successeur": l.get("successeur"),
                 "problemes_successeur": l.get("problemes_successeur", []), "relance": l.get("relance", False), "invalide": l.get("invalide", False)}
                for l in self.lignes(lignee)]
