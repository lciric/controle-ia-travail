"""Lecture des sorties de `vastai` 1.8.3 pour le lanceur v9 de SPARKS-EXP7-NUL (contre-lecture du delta v8, points 10, 11,
14 à 18 et 31). Bibliothèque standard seule ; lue par son chemin (`python3 -I -B vast_lecture.py …`).

Règles communes :
- toute sortie brute est lue puis **effacée** (avec son compagnon `.err` de la sortie d'erreur), qu'elle soit lisible ou
  non : rien n'en est versé ni gardé (R-1480 ; point 16 : `extra_env` porte les jetons en clair) ;
- seuls des champs nommés sont imprimés, jamais la sortie brute ;
- le JSON est lu **strict** (le fichier entier, `json.loads`) : toute autre forme est « illisible », jamais « absente ».

Règle de l'offre et des prix (point 11), écrite ici et appliquée par `offres` :
- recherche : `vastai search offers 'num_gpus=1 rentable=true verified=true' -o dph_total --raw` ;
- gardées : `resource_type` = « gpu », `num_gpus` = 1, `dph_total` > 0, `storage_cost` ≥ 0, `id` entier ; triées par
  `dph_total` croissant puis `id` ; au plus `N_OFFRES` (4) retenues, essayées dans cet ordre (« no_such_ask » : la suivante) ;
- `PRIX_CARTE` = `dph_total` (USD/h) de l'offre retenue ;
- `PRIX_STOCKAGE` = `storage_cost` (USD par Go et par mois) × `DISQUE_GO` (20) ÷ 730 (heures par mois), en USD/h.

Inventaire (point 10) : `vastai show instances --raw` rend une **liste** d'instances (ou `{"instances": [...]}`) ;
`vastai show instance <id> --raw` rend `{"instances": null}` pour une instance introuvable. L'instance est cherchée par son
identifiant entier (égalité, jamais un motif) : absente de la liste ou `"instances": null` → « absente ».

Boucle de redémarrage (point 31 d) : au moins trois inventaires sur au moins 300 s ; « arrêtée » si les trois derniers sont
« exited » avec `cur_state` « stopped » ; « absente » si le dernier est « absente » ; « indécis » s'il manque des lectures ;
sinon « boucle ».

    python3 -I -B vast_lecture.py offres BRUT RETENUES
    python3 -I -B vast_lecture.py offre RETENUES RANG                       → OFFRE= PRIX_CARTE= PRIX_STOCKAGE=
    python3 -I -B vast_lecture.py inventaire BRUT ID ATTENDU [JOURNAL]
    python3 -I -B vast_lecture.py boucle JOURNAL ID
    python3 -I -B vast_lecture.py journal-amorce BRUT
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

N_OFFRES = 4
DISQUE_GO = 20
HEURES_PAR_MOIS = 730
DUREE_MIN_BOUCLE_S = 300
REGLE = ("PRIX_CARTE = dph_total ; PRIX_STOCKAGE = storage_cost × 20 ÷ 730 ; resource_type gpu, num_gpus 1 ; "
         "dph_total croissant ; au plus 4 offres")
ETATS = ("absente", "exited", "running", "loading", "created", "stopped", "offline", "scheduling", "en_creation")


class Illisible(ValueError):
    pass


def _effacer(brut: Path) -> None:
    for p in (Path(brut), Path(str(brut) + ".err")):
        try:
            p.unlink()
        except FileNotFoundError:
            pass


def _json_strict(brut: Path):
    try:
        t = Path(brut).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        raise Illisible("sortie absente ou illisible") from None
    finally:
        _effacer(brut)
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        raise Illisible(f"sortie non JSON (longueur {len(t)})") from None


def _nombre(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def filtrer_offres(donnees) -> list[dict]:
    if not isinstance(donnees, list):
        raise Illisible("liste d'offres attendue")
    gardees = []
    for o in donnees:
        if not isinstance(o, dict):
            raise Illisible("offre qui n'est pas un objet")
        if (o.get("resource_type") == "gpu" and o.get("num_gpus") == 1 and isinstance(o.get("id"), int)
                and not isinstance(o.get("id"), bool) and _nombre(o.get("dph_total")) and o["dph_total"] > 0
                and _nombre(o.get("storage_cost")) and o["storage_cost"] >= 0 and o.get("rentable", True) is not False):
            gardees.append(o)
    gardees.sort(key=lambda o: (o["dph_total"], o["id"]))
    return [{"rang": k + 1, "id": o["id"], "dph_total": o["dph_total"], "storage_cost": o["storage_cost"],
             "resource_type": o["resource_type"], "prix_carte": round(float(o["dph_total"]), 6),
             "prix_stockage_heure": round(float(o["storage_cost"]) * DISQUE_GO / HEURES_PAR_MOIS, 6)}
            for k, o in enumerate(gardees[:N_OFFRES])]


def offres(brut: Path, retenues: Path) -> list[dict]:
    r = filtrer_offres(_json_strict(brut))
    Path(retenues).write_text(json.dumps({"regle": REGLE, "disque_go": DISQUE_GO, "offres": r}, indent=1) + "\n",
                              encoding="utf-8")
    return r


def offre(retenues: Path, rang: int) -> dict:
    d = json.loads(Path(retenues).read_text(encoding="utf-8"))
    for o in d["offres"]:
        if o["rang"] == rang:
            return o
    raise Illisible(f"aucune offre au rang {rang} (offres retenues : {len(d['offres'])})")


def lire_inventaire(donnees, ident: int) -> dict:
    if isinstance(donnees, dict) and "instances" in donnees:
        if donnees["instances"] is None:
            return {"id": ident, "etat": "absente", "cur_state": None, "dph_total": None}
        donnees = donnees["instances"]
    if not isinstance(donnees, list) or not all(isinstance(i, dict) for i in donnees):
        raise Illisible("liste d'instances attendue")
    if any(not isinstance(i.get("id"), int) or isinstance(i.get("id"), bool) for i in donnees):
        raise Illisible("identifiant d'instance non entier dans la liste")      # jamais « absente » par défaut de forme
    propres = [i for i in donnees if i["id"] == ident]
    if not propres:
        return {"id": ident, "etat": "absente", "cur_state": None, "dph_total": None}
    if len(propres) > 1:
        raise Illisible(f"{len(propres)} instances au même identifiant")
    i = propres[0]
    a = i.get("actual_status")
    if a is None:
        etat = "en_creation"
    elif isinstance(a, str) and re.fullmatch(r"[a-z_]{1,30}", a):
        etat = a
    else:
        raise Illisible("actual_status illisible")
    c = i.get("cur_state")
    c = c if isinstance(c, str) and re.fullmatch(r"[a-z_]{1,30}", c) else None
    d = i.get("dph_total") if _nombre(i.get("dph_total")) else None
    return {"id": ident, "etat": etat, "cur_state": c, "dph_total": d}


def inventaire(brut: Path, ident: int, journal: Path | None = None, maintenant: int | None = None) -> dict:
    try:
        r = lire_inventaire(_json_strict(brut), ident)
    except Illisible:
        r = {"id": ident, "etat": "illisible", "cur_state": None, "dph_total": None}
    if journal is not None:
        with open(journal, "a", encoding="utf-8") as j:
            j.write(f"{int(time.time()) if maintenant is None else maintenant} {ident} {r['etat']} {r['cur_state'] or '-'}\n")
    return r


def boucle(journal: Path, ident: int) -> str:
    lignes = []
    for l in Path(journal).read_text(encoding="utf-8").splitlines() if Path(journal).exists() else []:
        p = l.split()
        if len(p) == 4 and p[0].isdigit() and p[1] == str(ident):
            lignes.append((int(p[0]), p[2], p[3]))
    if lignes and lignes[-1][1] == "absente":
        return "absente"
    if len(lignes) < 3 or lignes[-1][0] - lignes[-3][0] < DUREE_MIN_BOUCLE_S:
        return "indecis"
    if all(e == "exited" and c == "stopped" for _, e, c in lignes[-3:]):
        return "arretee"
    return "boucle"


def journal_amorce(brut: Path) -> tuple[list[str], int, int]:
    try:
        t = Path(brut).read_text(encoding="utf-8", errors="replace")
    except OSError:
        t = ""
    finally:
        _effacer(brut)
    lignes = [l.strip()[:200] for l in t.splitlines() if "AMORCE V5" in l]
    redem = sum(1 for l in lignes if re.search(r"AMORCE V5.*: redémarrage", l))
    boucles = sum(1 for l in lignes if "boucle de redémarrage présumée" in l)
    return lignes, redem, boucles


def main(argv: list[str]) -> int:
    try:
        q = argv[0]
        if q == "offres":
            r = offres(Path(argv[1]), Path(argv[2]))
            print(f"RÈGLE : {REGLE}")
            for o in r:
                print(f"rang {o['rang']} : id {o['id']}, dph_total {o['dph_total']}, storage_cost {o['storage_cost']}, "
                      f"resource_type {o['resource_type']} → PRIX_CARTE {o['prix_carte']} PRIX_STOCKAGE {o['prix_stockage_heure']}")
            if not r:
                print("AUCUNE OFFRE CONFORME : rien ne part")
                return 9
        elif q == "offre":
            o = offre(Path(argv[1]), int(argv[2]))
            print(f"OFFRE={o['id']} PRIX_CARTE={o['prix_carte']} PRIX_STOCKAGE={o['prix_stockage_heure']}")
        elif q == "inventaire":
            if not re.fullmatch(r"[0-9]{1,12}", argv[2]):
                raise Illisible("identifiant d'instance : chiffres seuls (R10)")
            att = argv[3]
            if att not in ETATS:
                raise Illisible(f"état attendu {att!r}")
            r = inventaire(Path(argv[1]), int(argv[2]), Path(argv[4]) if len(argv) > 4 else None)
            print(f"INVENTAIRE : instance {r['id']}, état {r['etat']}"
                  + (f" (cur_state {r['cur_state']})" if r["cur_state"] else "")
                  + (f", dph_total {r['dph_total']}" if r["dph_total"] is not None else "") + f", attendu {att}")
            return 0 if r["etat"] == att else 6
        elif q == "boucle":
            v = boucle(Path(argv[1]), int(argv[2]))
            print(f"BOUCLE : instance {argv[2]}, verdict {v}")
            return {"arretee": 0, "absente": 0, "indecis": 6, "boucle": 8}[v]
        elif q == "journal-amorce":
            lignes, redem, boucles = journal_amorce(Path(argv[1]))
            for l in lignes:
                print(l)
            print(f"REDEMARRAGES={redem} BOUCLE_PRESUMEE={boucles}")
        else:
            raise IndexError
    except (Illisible, IndexError, ValueError, KeyError, OSError, json.JSONDecodeError) as err:
        print(f"LECTURE REFUSÉE : {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
