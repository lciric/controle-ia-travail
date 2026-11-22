"""Commit local de la course de T0.8 (consigne de la chaîne de lancement v3, `6f52c4db…`, § 3.5) — v1. Bibliothèque standard
et git seuls (jouable par le python3 de l'image, avant toute installation) ; ne lit le contenu d'aucun fichier de données.

`manifeste.creer_manifeste` exige un arbre propre et le texte scellé sous la racine, et consigne la tête ; le texte scellé cite
le commit du code et ne peut donc pas s'y trouver : la tête de la course est un enfant du commit du code, fait par l'amorce avant
la course. Conditions tenues ici :
(i) son seul parent est le commit cité (`COMMIT_CODE_T08`) ;
(ii) il n'ajoute que les entrées de la course, le texte scellé, la configuration réelle et leurs compagnons — rien sous un
     chemin gelé (`course_v1.exiger_code_au_commit` : tout, hors `prereg`, `brouillons`, `registres`, `docs`, `diag`, `runs`,
     `donnees`, `livrables`, `papiers`, `traces`, `CLAUDE.md`), rien d'autre ; la liste attendue est écrite **avant** le commit,
     à partir de la configuration (entrées), du guide de classification chargé par le code, du texte et de la configuration ;
(iii) les entrées viennent de la branche d'entrée seule (l'amorce les y prend ; `branche_conforme` exige que sa liste soit
     exactement la liste attendue) ;
(iv) la branche de sortie part de ce commit (vérifié après la poussée par `verifier_distant`) ;
(v) auteur, date et message fixés par l'amorce (date du commit de la branche d'entrée) : il se refait à l'identique.

    python3 -I -B -c "import sys; sys.path.insert(0, 'src'); from controle_ia.lancement_t08 import commit_local_v1 as c; sys.exit(c.main(sys.argv[1:]))" \
        attendus CONFIG.json PREREG|- > LISTE        (liste attendue, une ligne par chemin, triée)
        branche RACINE REF_ENTREE LISTE              (la branche d'entrée porte exactement la liste)
        verifier RACINE COMMIT LISTE                 (tête : un parent, = COMMIT ; ajouts = liste hors fichiers suivis, rien de gelé)
        verifier-distant DEPOT REF_SORTIE COMMIT REF_ENTREE   (exécutante, après la poussée, par les noms seuls)
Codes : 0 conforme ; 1 écart (motif sur la dernière ligne) ; 2 usage.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

GUIDE = ("docs/sources/invites-2606.08892-v1/index.json",
         "docs/sources/invites-2606.08892-v1/invites/H1-classification.txt")
# chemins exclus de la comparaison au commit cité (`harnais.validation_reelle.CHEMINS_GELES`) : un ajout ne peut être que là
NON_GELES = ("prereg", "brouillons", "registres", "docs", "diag", "runs", "donnees", "livrables", "papiers", "traces")
NON_GELES_FICHIERS = ("CLAUDE.md",)


class Ecart(Exception):
    pass


def _git(racine, *a) -> str:
    r = subprocess.run(["git", "-c", "core.quotePath=false", "-C", str(racine), *a], capture_output=True)
    if r.returncode != 0:
        raise Ecart(f"git {' '.join(a[:2])} : {r.stderr.decode('utf-8', 'replace').strip()[:300]}")
    return r.stdout.decode("utf-8", "surrogateescape")


def gele(chemin: str) -> bool:
    p = chemin.split("/")
    return not (p[0] in NON_GELES and len(p) > 1 or chemin in NON_GELES_FICHIERS)


def attendus(config: dict, prereg: str | None, chemin_config: str) -> list[str]:
    """Liste attendue de la branche d'entrée et du commit local, avant tout commit : entrées de la configuration, guide de
    classification, configuration et texte scellé (si la course en a un), chacun avec son compagnon."""
    e = config.get("entrees")
    if not isinstance(e, dict) or not e:
        raise Ecart("configuration sans entrées")
    base = sorted({x["chemin"] for x in e.values()} | set(GUIDE) | {chemin_config} | ({prereg} if prereg else set()))
    liste = sorted(base + [c + ".sha256" for c in base])
    for c in liste:
        if c.startswith("/") or ".." in c.split("/") or gele(c):
            raise Ecart(f"chemin attendu {c} sous un chemin gelé ou illisible : il changerait le code comparé au commit cité")
    return liste


def branche_conforme(racine, ref: str, liste: list[str]) -> None:
    noms = sorted(n for n in _git(racine, "ls-tree", "-r", "-z", "--name-only", ref).split("\0") if n)
    if noms != sorted(liste):
        raise Ecart(f"branche d'entrée ≠ liste attendue (en trop {sorted(set(noms) - set(liste))[:4]}, manquants "
                    f"{sorted(set(liste) - set(noms))[:4]})")


def ajouts_attendus(racine, commit: str, liste: list[str]) -> list[str]:
    """Les chemins de la liste qui ne sont pas suivis au commit cité (ceux qui le sont doivent y être identiques)."""
    suivis = {n for n in _git(racine, "ls-tree", "-r", "-z", "--name-only", commit, "--", *liste).split("\0") if n}
    return sorted(set(liste) - suivis)


def verifier(racine, commit: str, liste: list[str], tete: str = "HEAD") -> dict:
    parents = _git(racine, "rev-list", "--parents", "-n", "1", tete).split()
    if parents[1:] != [commit]:
        raise Ecart(f"commit local {parents[0][:12]} : parents {[p[:12] for p in parents[1:]]} ; un seul, le commit cité "
                    f"{commit[:12]}, exigé")
    etats = [l.split("\t", 1) for l in _git(racine, "diff", "--name-status", "--no-renames", commit, parents[0]).splitlines() if l]
    autres = [c for s, c in etats if s != "A"]
    if autres:
        raise Ecart(f"commit local : chemins modifiés ou retirés {autres[:4]} : il n'ajoute que des fichiers")
    ajoutes = sorted(c for _, c in etats)
    geles = [c for c in ajoutes if gele(c)]
    if geles:
        raise Ecart(f"commit local : fichier(s) sous un chemin gelé {geles[:4]}")
    att = ajouts_attendus(racine, commit, liste)
    if ajoutes != att:
        raise Ecart(f"commit local : ajouts ≠ liste déclarée (en trop {sorted(set(ajoutes) - set(att))[:4]}, manquants "
                    f"{sorted(set(att) - set(ajoutes))[:4]})")
    return {"commit_local": parents[0], "parent": commit, "ajouts": len(ajoutes)}


def verifier_distant(depot, ref_sortie: str, commit: str, ref_entree: str) -> dict:
    """Exécutante, après la poussée, par les noms seuls : sur la première lignée de la branche de sortie, le premier commit
    après le commit cité a ce seul parent ; ses ajouts sont exactement les fichiers de la branche d'entrée non suivis au
    commit cité ; aucun n'est sous un chemin gelé."""
    lignee = _git(depot, "rev-list", "--first-parent", "--reverse", f"{commit}..{ref_sortie}").split()
    if not lignee:
        raise Ecart(f"{ref_sortie} ne descend pas du commit cité {commit[:12]}")
    liste = sorted(n for n in _git(depot, "ls-tree", "-r", "-z", "--name-only", ref_entree).split("\0") if n)
    r = verifier(depot, commit, liste, tete=lignee[0])
    return {**r, "commits_apres": len(lignee)}


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 3 and argv[0] == "attendus":
            cfg = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
            print("\n".join(attendus(cfg, None if argv[2] == "-" else argv[2], argv[1])))
            return 0
        if len(argv) == 4 and argv[0] == "branche":
            branche_conforme(argv[1], argv[2], Path(argv[3]).read_text(encoding="utf-8").split())
            print("branche d'entrée conforme à la liste attendue")
            return 0
        if len(argv) == 4 and argv[0] == "verifier":
            r = verifier(argv[1], argv[2], Path(argv[3]).read_text(encoding="utf-8").split())
            print(f"commit local {r['commit_local']} conforme : parent {r['parent']}, {r['ajouts']} ajouts déclarés, rien de gelé")
            return 0
        if len(argv) == 5 and argv[0] == "verifier-distant":
            r = verifier_distant(argv[1], argv[2], argv[3], argv[4])
            print(f"commit du manifeste {r['commit_local']} conforme : parent {r['parent']}, {r['ajouts']} ajouts déclarés, "
                  f"rien de gelé, {r['commits_apres']} commit(s) sur la branche de sortie")
            return 0
    except (Ecart, OSError, ValueError, KeyError) as e:
        print(f"ÉCART : {e}")
        return 1
    print("usage : attendus | branche | verifier | verifier-distant (voir l'en-tête)", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
