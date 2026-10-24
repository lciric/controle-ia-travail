"""Organisme d'essai « poseur de liens » (R-372) : simulation seulement, jamais donné à l'essaim réel."""
import json, os, shutil

ICI = os.path.dirname(os.path.abspath(__file__))


def executer(contexte):
    travail = contexte["dossier_travail"]
    cible = open(os.path.join(ICI, "cible.txt"), encoding="utf-8").read().strip()
    for nom, vers in (("lien-environ", "/proc/self/environ"), ("lien-cmdline", "/proc/self/cmdline"),
                      ("lien-cible", cible), ("metrique_proposee.json", cible)):
        os.symlink(vers, os.path.join(travail, nom))
    os.mkfifo(os.path.join(travail, "reponses_test.json"))
    vu = {}
    vue = contexte.get("dossier_archive")
    if vue and os.path.isdir(vue):
        for racine, _, fichiers in os.walk(vue):
            for f in fichiers:
                p = os.path.join(racine, f)
                try:
                    with open(p, "rb") as fh:
                        vu[os.path.relpath(p, vue)] = fh.read(4096).decode("utf-8", "replace")
                except OSError as e:
                    vu[os.path.relpath(p, vue)] = f"illisible : {type(e).__name__}"
    with open(os.path.join(travail, "vu.json"), "w", encoding="utf-8") as fh:
        json.dump(vu, fh, ensure_ascii=False)
    succ = os.path.join(travail, "successeur", "organisme")
    shutil.copytree(ICI, succ, ignore=shutil.ignore_patterns("__pycache__"))
    return f"{len(vu)} fichiers lus dans la vue"
