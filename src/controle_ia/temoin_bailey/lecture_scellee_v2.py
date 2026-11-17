"""Lecture scellée v2 — témoin de Bailey, addendum 7, § 3 (`prereg/temoin-attaque-publiee-bailey-v1-addendum-7-…`).

La v2 remplace la v1 (`lecture_scellee_v1`, gardée sans changement, R12) après la vérification adverse v7 de l'addendum
(`docs/notes/reproduction-attaque-publiee-v1/verification-adverse-addendum-7-bailey-v7.md`) : (1) l'empreinte du
dossier porte les répertoires (vides compris) et refuse les liens symboliques et les entrées spéciales ; (2) un `src/`
modifié hors commit est un refus, jamais une valeur comparable ; (3) l'attendu porte le commit nommé et l'arbre `src/`
de ce commit, et il est écrit par le code lui-même, seulement en cas de succès ; (4) l'empreinte de l'environnement porte
l'interpréteur et `sys.path` ; (5) un contrôle final mécanique (`--controler`).

Seul geste permis sur un dossier réel après la clôture de la confirmation. Le code, et lui seul, joue
`lecture_v8.valider` puis `lecture_v8.lire` (graine `analyse_v3.graines()["reechantillonnage"]`) et rend une sortie
scellée qui porte l'issue. Règles, toutes mécaniques :

1. **Sortie neuve** : si la sortie, ou son compagnon `.sha256`, existe déjà, refus sans rien jouer ni rien écrire (R12).
2. **Empreintes attendues** (`--attendu`, écrit par `--calculer-attendu … --vers …`) : `commit` (40 chiffres
   hexadécimaux) ; `code` = `git rev-parse <commit>:src`, égal à l'arbre `src/` de la tête, `src/` sans modification
   ni fichier non suivi ; `dossier` = liste des entrées du dossier (répertoires, vides compris ; fichiers avec
   l'empreinte de leurs octets ; un lien symbolique ou une autre entrée : refus) ; `environnement` = interpréteur,
   version, `sys.path`, distributions installées. Un écart, une forme non conforme, ou des empreintes incalculables :
   issue « refus : empreintes », aucune exécution.
3. **Une exécution ; une seconde à l'identique seulement après un refus (`GardeArret`) ou une erreur**, empreintes
   recalculées et égales à l'attendu avant elle. Une exécution qui aboutit n'est jamais rejouée ; un état « pas de
   verdict » ou « non interprétable » rendu par le code est une exécution qui aboutit.
4. **Issue** : « aboutie » (sortie de la première exécution qui aboutit) ; « refus ou erreur » (deux échecs, ou sortie
   non sérialisable) ; « refus : empreintes ». Pour un refus, le texte de la `GardeArret` ; pour toute autre exception,
   son type et le lieu (fichier, ligne), sans le message.
5. **Retour** : sur la sortie standard, une seule ligne JSON : empreinte de la sortie et issue ; aucune valeur.
6. **Contrôle** (`--controler S --attendu A --dossier D --empreinte H`) : rend « conforme » si et seulement si la
   sortie S est scellée et intacte, son empreinte est H, son champ `attendu` est le fichier A et son champ `dossier`
   est D ; sinon « écart ». Il ne rend aucune autre valeur.

Usage (avec `python -B`, l'interpréteur et les variables de la commande consignée) :
`PYTHONPATH=src python -B -m controle_ia.temoin_bailey.lecture_scellee_v2 --calculer-attendu D --commit C --vers A`
puis `… --dossier D --sortie S --attendu A`, puis `… --controler S --attendu A --dossier D --empreinte H`.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata as md
import json
import platform
import re
import subprocess
import sys
import traceback
from dataclasses import asdict, is_dataclass
from pathlib import Path

import numpy as np

from controle_ia import scellement
from controle_ia.gardes import GardeArret
from controle_ia.temoin_bailey import analyse_v3 as an
from controle_ia.temoin_bailey import lecture_v8 as lc

DEPOT = Path(__file__).resolve().parents[3]
VERSION = "lecture_scellee_v2"
ISSUE_ABOUTIE = "aboutie"
ISSUE_REFUS = "refus ou erreur"
ISSUE_EMPREINTES = "refus : empreintes"
CLES = ("commit", "code", "dossier", "environnement")
FORMES = {"commit": r"[0-9a-f]{40}", "code": r"[0-9a-f]{40}", "dossier": r"[0-9a-f]{64}", "environnement": r"[0-9a-f]{64}"}


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def empreinte_dossier(d: Path) -> str:
    """Empreinte de la liste triée de toutes les entrées de `d` : répertoires (vides compris) par leur chemin relatif,
    fichiers par (chemin relatif, sha256 des octets) ; lien symbolique ou entrée d'un autre type : refus. Ne décode
    rien ; ne suit aucun lien."""
    d = Path(d)
    if d.is_symlink() or not d.is_dir():
        raise GardeArret(f"lecture scellée : dossier absent ou lien ({d})")
    entrees = []
    for p in sorted(d.rglob("*")):
        rel = p.relative_to(d).as_posix()
        if p.is_symlink():
            raise GardeArret(f"lecture scellée : lien symbolique dans le dossier ({rel})")
        if p.is_dir():
            entrees.append(["d", rel])
        elif p.is_file():
            entrees.append(["f", rel, _sha(p.read_bytes())])
        else:
            raise GardeArret(f"lecture scellée : entrée ni fichier ni répertoire ({rel})")
    return _sha(json.dumps(entrees, ensure_ascii=False).encode())


def _git(depot: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(depot), *args], capture_output=True, text=True, check=True).stdout


def arbre_src_propre(depot: Path = DEPOT) -> str:
    """Arbre `src/` de la tête ; refus si `src/` porte une modification ou un fichier non suivi."""
    if _git(depot, "status", "--porcelain", "--untracked-files=all", "--", "src").strip():
        raise GardeArret("lecture scellée : src/ modifié hors commit")
    return _git(depot, "rev-parse", "HEAD:src").strip()


def arbre_src_du_commit(commit: str, depot: Path = DEPOT) -> str:
    if not re.fullmatch(FORMES["commit"], str(commit)):
        raise GardeArret("lecture scellée : commit non conforme (40 chiffres hexadécimaux)")
    return _git(depot, "rev-parse", f"{commit}:src").strip()


def empreinte_environnement() -> str:
    dists = sorted(f"{d.metadata['Name']}=={d.version}" for d in md.distributions() if d.metadata["Name"])
    return _sha("\n".join([sys.executable, platform.python_version(), *sys.path, "--", *dists]).encode())


def calculer_attendu(dossier: Path, commit: str, depot: Path = DEPOT) -> dict:
    """Ne fait que des empreintes d'octets ; ne lit aucune note. Refus si la tête n'a pas l'arbre `src/` du commit."""
    code = arbre_src_propre(depot)
    if code != arbre_src_du_commit(commit, depot):
        raise GardeArret("lecture scellée : arbre src/ de la tête différent de celui du commit nommé")
    return {"commit": commit, "code": code, "dossier": empreinte_dossier(dossier),
            "environnement": empreinte_environnement()}


def attendu_conforme(attendu) -> bool:
    return (isinstance(attendu, dict) and set(attendu) == set(CLES)
            and all(isinstance(attendu[k], str) and re.fullmatch(FORMES[k], attendu[k]) for k in CLES))


def _en_json(o):
    if isinstance(o, np.generic):
        return o.item()
    if isinstance(o, np.ndarray):
        return o.tolist()
    if is_dataclass(o) and not isinstance(o, type):
        return asdict(o)
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    if isinstance(o, Path):
        return str(o)
    raise TypeError(f"valeur non sérialisable : {type(o).__name__}")


def _lieu(e: BaseException) -> str:
    cadres = traceback.extract_tb(e.__traceback__)
    du_depot = [c for c in cadres if str(DEPOT) in (c.filename or "")]
    c = (du_depot or cadres or [None])[-1]
    return f"{Path(c.filename).name}:{c.lineno}" if c is not None else "inconnu"


def une_execution(dossier: Path) -> dict:
    v = lc.valider(dossier)
    return lc.lire(v, an.graines()["reechantillonnage"])


def jouer(dossier: Path, attendu: dict, executer=une_execution, calculer=calculer_attendu) -> dict:
    """Règles 2 à 4 ; rend la sortie (sans l'écrire)."""
    sortie = {"version": VERSION, "dossier": str(dossier), "attendu": attendu, "executions": []}
    if not attendu_conforme(attendu):
        sortie["issue"] = ISSUE_EMPREINTES
        sortie["attendu_non_conforme"] = True
        return sortie
    for n in (1, 2):
        try:
            e = calculer(dossier, attendu["commit"])
        except Exception as x:  # noqa: BLE001 — empreintes incalculables ou refusées : refus, sans exécution
            echec = {"n": n, "echec_empreintes": type(x).__name__, "lieu": _lieu(x)}
            if isinstance(x, GardeArret):
                echec["message"] = str(x)
            sortie["executions"].append(echec)
            sortie["issue"] = ISSUE_EMPREINTES
            return sortie
        if e != attendu:
            sortie["executions"].append({"n": n, "empreintes": e})
            sortie["issue"] = ISSUE_EMPREINTES
            return sortie
        try:
            res = executer(dossier)
        except GardeArret as x:
            sortie["executions"].append({"n": n, "empreintes": e, "echec": "GardeArret", "message": str(x)})
            continue
        except Exception as x:  # noqa: BLE001 — toute erreur est un échec, rapporté sans son message
            sortie["executions"].append({"n": n, "empreintes": e, "echec": type(x).__name__, "lieu": _lieu(x)})
            continue
        sortie["executions"].append({"n": n, "empreintes": e, "aboutie": True})
        sortie["issue"] = ISSUE_ABOUTIE
        sortie["lecture"] = res
        return sortie
    sortie["issue"] = ISSUE_REFUS
    return sortie


def controler(sortie: Path, attendu: Path, dossier: str, empreinte: str) -> bool:
    """Règle 6 : vrai si et seulement si tout concorde ; ne rend aucune autre valeur."""
    try:
        if scellement.verifier(sortie) != empreinte:
            return False
        d = json.loads(Path(sortie).read_text(encoding="utf-8"))
        a = json.loads(Path(attendu).read_text(encoding="utf-8"))
        return d.get("version") == VERSION and d.get("attendu") == a and d.get("dossier") == str(dossier)
    except Exception:  # noqa: BLE001 — tout défaut est un écart
        return False


def _ecrire_neuf(chemin: Path, texte: str) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "x", encoding="utf-8") as f:  # « x » : jamais d'écrasement, même en course
        f.write(texte)


def principal(argv: list[str] | None = None, executer=une_execution, calculer=calculer_attendu) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dossier")
    ap.add_argument("--sortie")
    ap.add_argument("--attendu")
    ap.add_argument("--calculer-attendu")
    ap.add_argument("--commit")
    ap.add_argument("--vers")
    ap.add_argument("--controler")
    ap.add_argument("--empreinte")
    a = ap.parse_args(argv)
    if a.calculer_attendu:
        if not (a.commit and a.vers):
            ap.error("--calculer-attendu exige --commit et --vers")
        v = Path(a.vers)
        if v.exists():
            print(json.dumps({"issue": "refus : attendu déjà présent (R12)"}, ensure_ascii=False))
            return 3
        att = calculer(Path(a.calculer_attendu), a.commit)  # une GardeArret sort en erreur, sans rien écrire
        _ecrire_neuf(v, json.dumps(att, sort_keys=True))
        print(json.dumps({"attendu": str(v), "empreinte_attendu": scellement.sceller(v)}, ensure_ascii=False))
        return 0
    if a.controler:
        if not (a.attendu and a.dossier and a.empreinte):
            ap.error("--controler exige --attendu, --dossier et --empreinte")
        ok = controler(Path(a.controler), Path(a.attendu), a.dossier, a.empreinte)
        print(json.dumps({"controle": "conforme" if ok else "écart"}, ensure_ascii=False))
        return 0 if ok else 2
    if not (a.dossier and a.sortie and a.attendu):
        ap.error("--dossier, --sortie et --attendu sont exigés")
    s = Path(a.sortie)
    if s.exists() or scellement.compagnon(s).exists():
        print(json.dumps({"issue": "refus : sortie déjà présente (R12)", "sortie": str(s)}, ensure_ascii=False))
        return 3
    try:
        attendu = json.loads(Path(a.attendu).read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001 — attendu illisible : refus mécanique, écrit
        attendu = None
    sortie = jouer(Path(a.dossier), attendu, executer=executer, calculer=calculer)
    try:
        texte = json.dumps(sortie, ensure_ascii=False, sort_keys=True, indent=1, default=_en_json)
    except (TypeError, ValueError) as x:  # sortie non sérialisable : échec mécanique, la lecture n'est pas écrite
        sortie = {**{k: v for k, v in sortie.items() if k != "lecture"}, "issue": ISSUE_REFUS,
                  "echec_sortie": type(x).__name__}
        texte = json.dumps(sortie, ensure_ascii=False, sort_keys=True, indent=1, default=str)
    _ecrire_neuf(s, texte)
    h = scellement.sceller(s)
    print(json.dumps({"empreinte_sortie": h, "issue": sortie["issue"]}, ensure_ascii=False))
    return 0 if sortie["issue"] == ISSUE_ABOUTIE else 2


if __name__ == "__main__":
    sys.exit(principal())
