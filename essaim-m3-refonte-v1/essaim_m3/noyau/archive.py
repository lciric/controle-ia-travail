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

from . import fichiers as _fichiers


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
              "n_reponses_test", "empreinte_organisme", "quand_utc", "refus_noyau", "problemes_successeur", "relance", "impose", "famille",
              "question_ouverte")


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
                phase: str | None = None, dossier_noyau: pathlib.Path | None = None, dossier_corpus: pathlib.Path | None = None,
                gid: int | None = None, reponses_lues: dict | None = None) -> dict:
        """`dossier_noyau`, `dossier_corpus` (CE3-07) : dossiers du noyau tenus hors du dossier de travail de l'organisme,
        recopiés dans l'archive sous `travail/noyau` et `travail/corpus` (même disposition qu'avant). Les mêmes noms créés par
        l'organisme dans son dossier sont réservés : écartés et consignés. `gid` (CE3-06) : groupe de la lignée ; la vue est
        alors lisible par elle seule (dossiers 0550, fichiers 0440, à root) ; None : lisible par tous (simulation hors root,
        mémoire partagée). `reponses_lues` (RV-01) : pour une génération notée, les réponses que le juge a retenues
        ({identifiant: étiquette}, `{}` s'il n'en a retenu aucune) et le problème éventuel, écrits et scellés sous
        `juge/reponses-lues.json` : la lecture de H-G1 ne lit que ce fichier, avec la règle du juge."""
        d = self.dossier(lignee, generation, phase)
        empreinte = archiver_organisme(organisme, d / "organisme.tar.gz")
        travail = d / "travail"
        # R-372 : root ne suit aucun lien de l'organisme ; liens, tubes, sockets, fichiers à plusieurs liens durs écartés et consignés
        reserves = [n for n in ("noyau", "corpus") if os.path.lexists(pathlib.Path(dossier_travail) / n)]
        ecartes = _fichiers.copier_sans_liens(dossier_travail, travail, ignorer=("noyau_client.py", "lanceur.py", "__pycache__"),
                                              ignorer_racine=("noyau", "corpus"))
        ecartes = sorted(ecartes + [f"{n} : nom réservé au noyau (CE3-07), non archivé" for n in reserves])
        for nom, source in (("noyau", dossier_noyau), ("corpus", dossier_corpus)):
            if source is not None and _fichiers.vrai_dossier(source):
                restes_noyau = _fichiers.copier_sans_liens(source, travail / nom)
                if restes_noyau:  # dossiers écrits par le seul noyau : rien d'autre que des fichiers ordinaires
                    raise RuntimeError(f"dépôt de {lignee} g{generation} : éléments non ordinaires dans {nom} : {restes_noyau[:5]}")
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
        if reponses_lues is not None:
            (juge / "reponses-lues.json").write_text(json.dumps(reponses_lues, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
            sceller(juge / "reponses-lues.json")
        ligne = {"lignee": lignee, "generation": generation, "phase": phase, "score": score.get("score"), "statut": resume.get("statut"),
                 "cout_usd": resume.get("cout_usd"), "n_appels": resume.get("n_appels"), "chemin": str(d.relative_to(self.racine)),
                 "empreinte_organisme": empreinte, "successeur": resume.get("successeur"),
                 "impose": resume.get("impose"), "famille": resume.get("famille"),
                 "problemes_successeur": [str(x)[:200] for x in (resume.get("problemes_successeur") or [])][:10],
                 "relance": bool(resume.get("relance")), "invalide": bool(resume.get("invalide")),
                 "n_elements_ecartes": len(ecartes), "question_ouverte": (resume.get("question_ouverte") or None),
                 "quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        complet = {**resume, **ligne, "elements_ecartes": [str(x)[:200] for x in ecartes[:200]]}
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
        restes = _fichiers.copier_sans_liens(travail, v / "travail", ignorer=("noyau", "juge", "reponses_test.json", "attaques.json"))
        if restes:  # impossible après la première copie : l'archive ne contient que des fichiers ordinaires
            raise RuntimeError(f"vue de {lignee} g{generation} : éléments non ordinaires dans l'archive : {restes[:5]}")
        # vue en lecture seule : lisible par la seule lignée (groupe `gid`, CE3-06) ou par tous sans isolation d'utilisateur
        for f in [v] + list(v.rglob("*")):
            try:
                if gid is not None:
                    os.chown(f, 0, gid, follow_symlinks=False)
                    os.chmod(f, 0o550 if f.is_dir() else 0o440)
                else:
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

    def importer_conception(self, origine: pathlib.Path, lignee: str, gid: int | None = None) -> list[dict]:
        """Bras apparié adaptatif (`--depuis` sans `--gel`) : recopie dans cette archive les rondes de conception (`cNNN`)
        de `lignee` archivées dans la course d'origine, pour que la génération 0 relancée voie dans `historique` et dans
        sa vue ce que la même génération 0 voyait dans la course d'origine (sinon le bras apparié a moins d'information que
        le bras d'origine, en plus de ce que l'on compare). Dossiers copiés tels quels (scellés par l'origine), lignes
        d'index marquées `importee` (jamais notées, jamais comptées dans la dépense ni dans les scores), vue reconstruite
        avec le même filtre que `deposer`. Rend les lignes importées. Rien n'est réécrit : une ronde déjà présente refuse.
        `gid` (RV-03, CE3-06) : groupe de la lignée ; la vue importée et `archive_vue/<lignée>` sont alors lisibles par elle
        seule dès l'import (mêmes droits que `deposer`), avant même son premier passage."""
        origine = pathlib.Path(origine)
        index = origine / "archive" / "index.jsonl"
        if not index.is_file():
            raise FileExistsError(f"course d'origine sans archive : {index}")
        importees = []
        for l in (json.loads(x) for x in index.read_text(encoding="utf-8").splitlines() if x.strip()):
            if l["lignee"] != lignee or l.get("phase") != "conception":
                continue
            source = origine / "archive" / l["chemin"]
            d = self.dossier(lignee, int(l["generation"]), "conception")  # refuse si déjà présente (rien n'est réécrit)
            d.rmdir()
            restes = _fichiers.copier_sans_liens(source, d)  # R-372 : aucune copie de root ne suit un lien
            if restes:
                raise RuntimeError(f"import de {l['chemin']} : éléments non ordinaires dans l'archive d'origine : {restes[:5]}")
            ligne = {**l, "importee": True, "course_origine": str(origine), "chemin": str(d.relative_to(self.racine)),
                     "quand_utc": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
            with self.index.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")
            v = self.vue / lignee / self.nom_generation(int(l["generation"]), "conception")
            v.mkdir(parents=True, exist_ok=True)
            # R-396 : la réponse à la question ouverte de la ronde, recopiée dans la vue de l'origine par `archiver_reponse`
            # (`cNNN/reponse-question.md`), l'est aussi ici : le bras apparié voit au même endroit ce que voyait l'origine
            for nom in ("organisme.tar.gz", "organisme.tar.gz.sha256", "reponse-question.md"):
                if (d / nom).is_file():
                    shutil.copy2(d / nom, v / nom)
            resume = json.loads((d / "resume.json").read_text(encoding="utf-8")) if (d / "resume.json").is_file() else ligne
            (v / "resume.json").write_text(json.dumps({k: resume.get(k) for k in CHAMPS_VUE}, ensure_ascii=False, indent=1), encoding="utf-8")
            if (d / "travail").is_dir():
                _fichiers.copier_sans_liens(d / "travail", v / "travail", ignorer=("noyau", "juge", "reponses_test.json", "attaques.json"))
            for f in [v] + list(v.rglob("*")):
                try:
                    if gid is not None:
                        os.chown(f, 0, gid, follow_symlinks=False)
                        os.chmod(f, 0o550 if f.is_dir() else 0o440)
                    else:
                        os.chmod(f, 0o555 if f.is_dir() else 0o444)
                except OSError:
                    pass
            importees.append(ligne)
        if gid is not None and (self.vue / lignee).is_dir():
            try:
                os.chown(self.vue / lignee, 0, gid, follow_symlinks=False)
                os.chmod(self.vue / lignee, 0o750)
            except OSError:
                pass
        return importees

    def lignes(self, lignee: str | None = None) -> list[dict]:
        if not self.index.exists():
            return []
        out = [json.loads(l) for l in self.index.read_text(encoding="utf-8").splitlines() if l.strip()]
        return [l for l in out if lignee is None or l["lignee"] == lignee]

    def historique(self, lignee: str) -> list[dict]:
        return [{"generation": l["generation"], "phase": l.get("phase"), "lignee": l["lignee"], "score": l["score"], "statut": l["statut"],
                 "cout_usd": l["cout_usd"], "n_appels": l["n_appels"], "successeur": l.get("successeur"),
                 "problemes_successeur": l.get("problemes_successeur", []), "relance": l.get("relance", False), "invalide": l.get("invalide", False),
                 **({"question_ouverte": l["question_ouverte"]} if l.get("question_ouverte") else {})}
                for l in self.lignes(lignee)]
