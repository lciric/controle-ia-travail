"""Ligne `CODE-ACCB6` : contrôle du code exécuté contre le fichier qu'elle cite — v1 (fichier neuf, R-2272 de la session mère ;
couple proposé au texte du barreau 6, rapport du développeur, § 7, « non mis en œuvre », repris ici).

Le fichier cité par la ligne `CODE-ACCB6` du registre propre `registres/accumulation-b6-v1.md` porte
`{"commit": "<40 caractères hexadécimaux>", "fichiers": {"src/controle_ia/accumulation_b6/<nom>.py": "<sha256>", …}, "entropie": <entier>}`
(forme contrôlée par `garde_v1.lire_fichier_code` : clés exactement, entropie de 128 bits). `controler_code` vérifie, dans le dépôt git
qui porte le paquet **effectivement importé** (`dossier_du_paquet`, le dossier de ce module) :

1. le paquet importé est le dossier `src/controle_ia/accumulation_b6/` de ce dépôt (sinon non vérifiable) ;
2. chaque chemin listé est `src/controle_ia/accumulation_b6/<nom>.py` (aucun sous-dossier) et chaque empreinte a 64 caractères ;
3. le commit cité existe et est la tête ou un de ses ancêtres (`git merge-base --is-ancestor`) ;
4. les fichiers `*.py` du paquet au commit cité sont exactement ceux de la liste, chacun à l'empreinte écrite (contenu au commit) ;
5. les fichiers `*.py` du paquet importé sont exactement ceux de la liste, chacun à l'empreinte écrite (contenu sur le disque).

Tout défaut → `RefusRegistre` : la lecture (`lecture_v1.lire`) le rend en refus avant tout calcul et avant le manifeste (code 2,
ligne `REFUS-ACCB6` au journal propre). Ce contrôle ne lit que le dépôt du code et le fichier cité ; il n'ouvre rien de la course.
Il ne vérifie pas les modules importés hors du paquet (`t07`, `sondes`, `manifeste`, `scellement`, `gardes`) : déclaré (point ouvert
du complément du rapport).

    PYTHONPATH=src python -m controle_ia.accumulation_b6.code_accb6_v1 ecrire DEPOT COMMIT SORTIE   # fichier de CODE-ACCB6 (aide)
    PYTHONPATH=src python -m controle_ia.accumulation_b6.code_accb6_v1 verifier RACINE              # contrôle seul, rien d'écrit

`ecrire` liste les fichiers `*.py` du paquet au commit donné (empreintes du contenu au commit) et tire l'entropie de 128 bits
(`numpy.random.SeedSequence().entropy`, R9) ; le scellement (`.sha256`) et la ligne `CODE-ACCB6` restent à faire par la session mère.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from ..t07 import registre_v1 as rg
from . import garde_v1 as gv

PREFIXE = "src/controle_ia/accumulation_b6/"
COMMIT = re.compile(r"[0-9a-f]{40}")


def dossier_du_paquet() -> Path:
    """Dossier du paquet effectivement importé (celui de ce module)."""
    return Path(__file__).resolve().parent


def _git(depot: Path, *args: str) -> tuple[int, bytes]:
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True)
    return r.returncode, r.stdout


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _du_paquet(chemin: str) -> bool:
    return isinstance(chemin, str) and chemin.startswith(PREFIXE) and chemin.endswith(".py") and "/" not in chemin[len(PREFIXE):]


def controler_code(racine: Path, entree: dict, dossier_code: Path | None = None) -> dict:
    """Contrôles 1 à 5 (docstring du module). `entree` : ligne `CODE-ACCB6` vérifiée (`chemin`, `date`, …) ; `dossier_code` : dossier
    du paquet à contrôler (défaut : le paquet importé ; essais seulement). Rend le rapport ; tout défaut → `RefusRegistre`."""
    d = gv.lire_fichier_code(Path(racine) / entree["chemin"])
    fautifs = [p for p, s in d["fichiers"].items() if not (_du_paquet(p) and rg.SHA.fullmatch(s))]
    if fautifs:
        raise rg.RefusRegistre(f"CODE-ACCB6 : entrées {fautifs[:5]} : chemin {PREFIXE}<nom>.py et empreinte sha256 attendus")
    dossier = Path(dossier_code).resolve() if dossier_code is not None else dossier_du_paquet()
    c, top = _git(dossier, "rev-parse", "--show-toplevel")
    if c != 0:
        raise rg.RefusRegistre(f"CODE-ACCB6 : le paquet importé ({dossier}) n'est pas dans un dépôt git : code non vérifiable")
    depot = Path(top.decode("utf-8").strip()).resolve()
    if dossier != (depot / PREFIXE).resolve():
        raise rg.RefusRegistre(f"CODE-ACCB6 : le paquet importé ({dossier}) n'est pas {PREFIXE} du dépôt {depot} : code non vérifiable")
    tete = _git(depot, "rev-parse", "HEAD")[1].decode("utf-8").strip()
    commit = d["commit"]
    if not COMMIT.fullmatch(commit) or _git(depot, "cat-file", "-e", f"{commit}^{{commit}}")[0] != 0:
        raise rg.RefusRegistre(f"CODE-ACCB6 : commit cité {commit[:12]}… absent du dépôt du paquet importé")
    if _git(depot, "merge-base", "--is-ancestor", commit, tete)[0] != 0:
        raise rg.RefusRegistre(f"CODE-ACCB6 : commit cité {commit[:12]}… ni la tête ({tete[:12]}…) ni un de ses ancêtres")
    _, liste = _git(depot, "ls-tree", "--name-only", commit, "--", PREFIXE)
    au_commit = {p for p in liste.decode("utf-8").splitlines() if _du_paquet(p)}
    ecrits = set(d["fichiers"])
    if au_commit != ecrits:
        raise rg.RefusRegistre(f"CODE-ACCB6 : fichiers du paquet au commit cité ≠ liste écrite (en plus au commit : "
                               f"{sorted(au_commit - ecrits)[:5]} ; absents du commit : {sorted(ecrits - au_commit)[:5]})")
    importes = {PREFIXE + f.name for f in dossier.glob("*.py")}
    if importes != ecrits:
        raise rg.RefusRegistre(f"CODE-ACCB6 : fichiers du paquet importé ≠ liste écrite (en plus : {sorted(importes - ecrits)[:5]} ; "
                               f"absents : {sorted(ecrits - importes)[:5]})")
    ecarts = []
    for p, s in sorted(d["fichiers"].items()):
        code, blob = _git(depot, "show", f"{commit}:{p}")
        if code != 0 or _sha(blob) != s:
            ecarts.append(f"{p} au commit cité")
        if _sha((dossier / Path(p).name).read_bytes()) != s:
            ecarts.append(f"{p} dans le paquet importé")
    if ecarts:
        raise rg.RefusRegistre(f"CODE-ACCB6 : empreintes différentes de la liste écrite : {ecarts[:6]}")
    return {"commit": commit, "tete_du_depot": tete, "fichiers": len(ecrits), "date_ligne": entree.get("date"),
            "paquet_importe": str(dossier),
            "verifie": "commit ancêtre de la tête ; fichiers du paquet au commit et dans le paquet importé égaux à la liste"}


def ecrire_fichier_code(depot: Path, commit: str, sortie: Path, entropie: int | None = None) -> Path:
    """Écrit le fichier de `CODE-ACCB6` pour `commit` du dépôt `depot` : fichiers `*.py` du paquet au commit (empreintes du contenu
    au commit) et entropie de 128 bits (tirée ici si `entropie` est nul ; donnée : essais). Refuse d'écraser un fichier (R12)."""
    import numpy as np
    depot, sortie = Path(depot), Path(sortie)
    if sortie.exists():
        raise rg.RefusRegistre(f"{sortie} existe déjà : jamais réécrit (R12)")
    c, plein = _git(depot, "rev-parse", "--verify", f"{commit}^{{commit}}")
    if c != 0:
        raise rg.RefusRegistre(f"commit {commit!r} introuvable dans {depot}")
    commit = plein.decode("utf-8").strip()
    _, liste = _git(depot, "ls-tree", "--name-only", commit, "--", PREFIXE)
    fichiers = {}
    for p in sorted(x for x in liste.decode("utf-8").splitlines() if _du_paquet(x)):
        code, blob = _git(depot, "show", f"{commit}:{p}")
        if code != 0:
            raise rg.RefusRegistre(f"{p} illisible au commit {commit[:12]}…")
        fichiers[p] = _sha(blob)
    if not fichiers:
        raise rg.RefusRegistre(f"aucun fichier {PREFIXE}*.py au commit {commit[:12]}…")
    e = int(np.random.SeedSequence().entropy) if entropie is None else int(entropie)
    if not 0 < e < 2 ** 128:
        raise rg.RefusRegistre(f"entropie {e} : 0 < e < 2^128 attendu")
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(json.dumps({"commit": commit, "fichiers": fichiers, "entropie": e}, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    gv.lire_fichier_code(sortie)                                 # la forme écrite est celle que la garde exige
    return sortie


def main(argv: list[str]) -> int:
    """`ecrire DEPOT COMMIT SORTIE` (code 0 ; 2 refus) ; `verifier RACINE` : ligne `CODE-ACCB6` du registre propre (forme, sceau,
    fichier cité) et contrôle du paquet importé, rien d'écrit (code 0 conforme, 2 refus)."""
    if len(argv) == 4 and argv[0] == "ecrire":
        try:
            p = ecrire_fichier_code(Path(argv[1]), argv[2], Path(argv[3]))
        except rg.RefusRegistre as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
        d = json.loads(p.read_text(encoding="utf-8"))
        print(f"{p} : commit {d['commit']}, {len(d['fichiers'])} fichiers, entropie écrite (à sceller, puis ligne CODE-ACCB6)")
        return 0
    if len(argv) == 2 and argv[0] == "verifier":
        racine = Path(argv[1])
        try:
            lignes, _ = rg.lire_registre_detail(racine / gv.REGISTRE_PROPRE, (gv.CODE_ACCB6,), (gv.SCELLEMENT_ACCB6, gv.LECTURE_ACCB6))
            _, date, chemin, sha = lignes[gv.CODE_ACCB6]
            rg.sceau_conforme(racine / chemin, sha)
            r = controler_code(racine, {"chemin": chemin, "date": date})
        except rg.RefusRegistre as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
        print(f"CODE-ACCB6 conforme : commit {r['commit']}, {r['fichiers']} fichiers, tête du dépôt {r['tete_du_depot']}")
        return 0
    print("usage : python -m controle_ia.accumulation_b6.code_accb6_v1 ecrire DEPOT COMMIT SORTIE | verifier RACINE", file=sys.stderr)
    return 2


__all__ = ["controler_code", "ecrire_fichier_code", "dossier_du_paquet", "PREFIXE"]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
