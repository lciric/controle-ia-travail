"""Lecture scellée — témoin de Bailey, addendum 7, § 3 (`prereg/temoin-attaque-publiee-bailey-v1-addendum-7-…`).

Seul geste permis sur un dossier réel après la clôture de la confirmation. Le script, et lui seul, joue
`lecture_v8.valider` puis `lecture_v8.lire` (graine `analyse_v3.graines()["reechantillonnage"]`) ; il rend une sortie
scellée qui porte l'issue. Aucun lecteur ne joue autre chose sur le dossier. Règles, toutes mécaniques :

1. **Sortie neuve** : si le fichier de sortie, ou son compagnon `.sha256`, existe déjà, refus sans rien jouer ni rien
   écrire (R12 : jamais d'écrasement ; la première sortie scellée fait foi).
2. **Empreintes attendues** (données par la note de clôture, fichier JSON `--attendu`) : arbre `src/` du dépôt
   (`git rev-parse HEAD:src`, `git status --porcelain -- src` vide), liste des empreintes des fichiers du dossier,
   environnement (version de l'interpréteur, liste des distributions installées). Un écart : issue « refus :
   empreintes », aucune exécution.
3. **Une exécution ; une seconde à l'identique seulement après un refus (`GardeArret`) ou une erreur**, empreintes
   recalculées et égales à l'attendu avant elle (sinon « refus : empreintes »). Une exécution qui aboutit n'est jamais
   rejouée ; un état « pas de verdict » ou « non interprétable » rendu par le code est une exécution qui aboutit.
4. **Issue** : « aboutie » (sortie de la première exécution qui aboutit) ; « refus ou erreur » (deux échecs, ou
   sortie non sérialisable) ; « refus : empreintes » (écart, ou empreintes incalculables). Pour un refus, le texte de
   la `GardeArret` ; pour toute autre exception, son type et le lieu (fichier, ligne) de la dernière ligne du code du
   dépôt, sans le message.
5. **Retour** : sur la sortie standard, une seule ligne JSON : empreinte de la sortie et issue ; aucune valeur.

Usage : `PYTHONPATH=src python -m controle_ia.temoin_bailey.lecture_scellee_v1 --dossier D --sortie S --attendu A`
(`--calculer-attendu D` écrit sur la sortie standard les empreintes de D et du code, pour la note de clôture ; il ne
lit aucune note : il ne fait que des empreintes d'octets).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata as md
import json
import platform
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
ISSUE_ABOUTIE = "aboutie"
ISSUE_REFUS = "refus ou erreur"
ISSUE_EMPREINTES = "refus : empreintes"


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def empreinte_dossier(d: Path) -> str:
    """Empreinte de la liste triée (chemin relatif, sha256 des octets) de tous les fichiers de `d`. Ne décode rien."""
    d = Path(d)
    if not d.is_dir():
        raise GardeArret(f"lecture scellée : dossier absent ({d})")
    lignes = [f"{p.relative_to(d).as_posix()}\t{_sha(p.read_bytes())}" for p in sorted(d.rglob("*")) if p.is_file()]
    return _sha("\n".join(lignes).encode())


def empreinte_code(depot: Path = DEPOT) -> str:
    """Arbre `src/` au commit courant ; refus si `src/` porte une modification non commitée."""
    statut = subprocess.run(["git", "-C", str(depot), "status", "--porcelain", "--", "src"], capture_output=True,
                            text=True, check=True).stdout
    if statut.strip():
        return "src/ modifié hors commit"
    return subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD:src"], capture_output=True, text=True,
                          check=True).stdout.strip()


def empreinte_environnement() -> str:
    dists = sorted(f"{d.metadata['Name']}=={d.version}" for d in md.distributions() if d.metadata["Name"])
    return _sha((platform.python_version() + "\n" + "\n".join(dists)).encode())


def empreintes(dossier: Path) -> dict:
    return {"code": empreinte_code(), "dossier": empreinte_dossier(dossier), "environnement": empreinte_environnement()}


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
    cadres = [c for c in traceback.extract_tb(e.__traceback__) if str(DEPOT) in (c.filename or "")]
    c = (cadres or traceback.extract_tb(e.__traceback__) or [None])[-1]
    return f"{Path(c.filename).name}:{c.lineno}" if c is not None else "inconnu"


def une_execution(dossier: Path) -> dict:
    v = lc.valider(dossier)
    return lc.lire(v, an.graines()["reechantillonnage"])


def jouer(dossier: Path, attendu: dict, executer=une_execution, calculer=empreintes) -> dict:
    """Règles 2 à 4 ; rend la sortie (sans l'écrire)."""
    sortie = {"version": "lecture_scellee_v1", "dossier": str(dossier), "attendu": attendu, "executions": []}
    for n in (1, 2):
        try:
            e = calculer(dossier)
        except Exception as x:  # noqa: BLE001 — empreintes incalculables : refus, sans exécution
            sortie["executions"].append({"n": n, "echec_empreintes": type(x).__name__, "lieu": _lieu(x)})
            sortie["issue"] = ISSUE_EMPREINTES
            return sortie
        if set(attendu) != set(e) or e != attendu:
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


def principal(argv: list[str] | None = None, executer=une_execution, calculer=empreintes) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dossier")
    ap.add_argument("--sortie")
    ap.add_argument("--attendu")
    ap.add_argument("--calculer-attendu")
    a = ap.parse_args(argv)
    if a.calculer_attendu:
        print(json.dumps(calculer(Path(a.calculer_attendu)), sort_keys=True))
        return 0
    if not (a.dossier and a.sortie and a.attendu):
        ap.error("--dossier, --sortie et --attendu sont exigés")
    s = Path(a.sortie)
    if s.exists() or scellement.compagnon(s).exists():
        print(json.dumps({"issue": "refus : sortie déjà présente (R12)", "sortie": str(s)}, ensure_ascii=False))
        return 3
    attendu = json.loads(Path(a.attendu).read_text(encoding="utf-8"))
    sortie = jouer(Path(a.dossier), attendu, executer=executer, calculer=calculer)
    try:
        texte = json.dumps(sortie, ensure_ascii=False, sort_keys=True, indent=1, default=_en_json)
    except (TypeError, ValueError) as x:  # sortie non sérialisable : échec mécanique, la lecture n'est pas écrite
        sortie = {**{k: v for k, v in sortie.items() if k != "lecture"}, "issue": ISSUE_REFUS,
                  "echec_sortie": type(x).__name__}
        texte = json.dumps(sortie, ensure_ascii=False, sort_keys=True, indent=1, default=str)
    s.parent.mkdir(parents=True, exist_ok=True)
    with open(s, "x", encoding="utf-8") as f:  # « x » : jamais d'écrasement, même en course
        f.write(texte)
    h = scellement.sceller(s)
    print(json.dumps({"empreinte_sortie": h, "issue": sortie["issue"]}, ensure_ascii=False))
    return 0 if sortie["issue"] == ISSUE_ABOUTIE else 2


if __name__ == "__main__":
    sys.exit(principal())
