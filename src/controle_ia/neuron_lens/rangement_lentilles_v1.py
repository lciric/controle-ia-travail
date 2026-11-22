"""Rangement de nos lentilles réajustées au dépôt privé de la plateforme de modèles (lieu L2) — v1.

Écrit pour le lanceur v4 du réajustement (`b_beta_lancer_v4.py`, devis du réajustement v9, § 5, points 3 et 5 d ; critère d'identité v8,
§ 4, point 5 et § 5). Trois usages :
- **sur la machine** (`envoyer_verifie`) : empreinte de chaque fichier recalculée en flux et exigée égale à celle que porte le résultat de
  l'étape qui l'a produit ; dépôt exigé **privé** avant tout envoi ; envoi par le chemin du fichier (aucune copie sur le disque) ;
  à l'arrivée, taille et empreinte que la plateforme rend relues à la révision du dépôt notée ; au plus deux reprises par fichier,
  comptées sur toute la course (`deja` : essais déjà faits) ; aucune exception ne sort, chaque échec est consigné ;
- **dans le conteneur de la session** (`relire`, ligne de commande `relire`) : relecture au lieu de rangement à une révision donnée,
  en flux (téléchargement passé directement au calcul d'empreinte, rien n'est écrit sur le disque) ou, seulement si la mère l'a établi
  (devis v9, § 5, point 9), par l'empreinte que rend la plateforme ;
- partout : le nom du dépôt est passé en variable (`DEPOT_RANGEMENT`) ou en argument, **jamais écrit dans le code** ; la clé est lue
  par le nom de sa variable, jamais imprimée, jamais écrite.

Aucun appel réseau à l'import. Le transport réel (`TransportHub`) n'est **pas essayé** avant la course (aucune requête permise à
l'écriture : déclaré) ; les essais jouent un faux transport (`tests/test_neuron_lens_b_beta_lancer_v4.py`).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

VARIABLE_DEPOT = "DEPOT_RANGEMENT"
REPRISES = 2  # devis v9, § 5, point 3 : au plus deux reprises par fichier
_DEPOT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,95}/[A-Za-z0-9][A-Za-z0-9_.-]{0,95}$")
_REVISION = re.compile(r"^[0-9a-f]{40}$")
_SHA = re.compile(r"^[0-9a-f]{64}$")
BLOC = 1 << 24


def probleme_depot(nom: str) -> list[str]:
    """Le dépôt de rangement : « compte/nom », sans espace ni chemin."""
    if not _DEPOT.match(nom or ""):
        return [f"{VARIABLE_DEPOT} absent ou mal formé (« compte/nom » attendu)"]
    return []


def sha256_fichier(chemin) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as fh:
        while b := fh.read(BLOC):
            h.update(b)
    return h.hexdigest()


def sha256_flux(morceaux) -> tuple[str, int]:
    """Empreinte et taille d'un flux d'octets, sans rien écrire."""
    h, n = hashlib.sha256(), 0
    for b in morceaux:
        h.update(b)
        n += len(b)
    return h.hexdigest(), n


class TransportHub:
    """Transport réel par `huggingface_hub` (version épinglée de la course, 1.33.0 ; aucun paquet ajouté). La clé est celle de
    l'environnement (`HF_TOKEN`), lue par la bibliothèque elle-même ; `cle` n'est passée que pour la relecture de la session."""

    def __init__(self, cle: str | None = None):
        self.cle = cle

    def _api(self):
        from huggingface_hub import HfApi
        return HfApi(token=self.cle)

    def prive(self, depot: str) -> bool:
        return self._api().repo_info(depot, repo_type="model").private is True

    def envoyer(self, chemin_local: Path, chemin_depot: str, depot: str, message: str) -> str:
        info = self._api().upload_file(path_or_fileobj=str(chemin_local), path_in_repo=chemin_depot, repo_id=depot,
                                       repo_type="model", commit_message=message)
        return info.oid

    def info(self, depot: str, chemins: list[str], revision: str) -> dict:
        out = {}
        for f in self._api().get_paths_info(depot, chemins, revision=revision, repo_type="model"):
            lfs = getattr(f, "lfs", None)
            out[f.path] = {"taille": getattr(f, "size", None), "sha256": getattr(lfs, "sha256", None) if lfs else None}
        return out

    def flux(self, depot: str, chemin: str, revision: str):
        from huggingface_hub import hf_hub_url
        from huggingface_hub.utils import build_hf_headers, get_session
        url = hf_hub_url(depot, chemin, revision=revision, repo_type="model")
        with get_session().stream("GET", url, headers=build_hf_headers(token=self.cle), follow_redirects=True,
                                  timeout=600) as r:
            r.raise_for_status()
            yield from r.iter_bytes(BLOC)


def _court(e: BaseException) -> str:
    return f"{type(e).__name__}: {e}"[:300]


def envoyer_verifie(transport, depot: str, fichiers: list[dict], message: str, deja: dict | None = None,
                    empreinte=sha256_fichier, horloge=time.time) -> dict:
    """Copie vérifiée de `fichiers` (chacun : `local`, `depot` (chemin dans le dépôt), `sha256`, `taille` attendus). Rend, par chemin
    dans le dépôt : `copie_faite`, `essais` (cumulés avec `deja`), `revision`, `verification`, `erreurs`. Rien n'est levé."""
    deja = deja or {}
    out = {"depot": depot, "fichiers": {}, "refus": None}
    pb = probleme_depot(depot)
    try:
        if not pb and not transport.prive(depot):
            pb = ["dépôt de rangement non privé : aucun envoi (des poids dérivés ne se publient pas)"]
    except Exception as e:  # noqa: BLE001 — consigné : aucun envoi
        pb = [f"dépôt de rangement illisible : {_court(e)}"]
    for f in fichiers:
        r = {"local": str(f["local"]), "sha256": f["sha256"], "taille": f["taille"], "copie_faite": False,
             "essais": int(deja.get(f["depot"], 0)), "revision": None, "verification": None, "erreurs": []}
        out["fichiers"][f["depot"]] = r
        if pb:
            r["erreurs"] += pb
            continue
        try:
            p = Path(f["local"])
            loc, t = empreinte(p), p.stat().st_size
        except Exception as e:  # noqa: BLE001
            r["erreurs"].append(f"empreinte locale illisible : {_court(e)}")
            continue
        if loc != f["sha256"] or t != f["taille"]:
            r["erreurs"].append("fichier changé depuis le résultat de son étape : aucun envoi")
            continue
        while not r["copie_faite"] and r["essais"] < 1 + REPRISES:
            r["essais"] += 1
            try:
                rev = transport.envoyer(p, f["depot"], depot, message)
                if not _REVISION.match(str(rev or "")):
                    raise ValueError(f"révision rendue illisible : {str(rev)[:60]!r}")
                vu = transport.info(depot, [f["depot"]], rev).get(f["depot"])
                if not vu or vu.get("taille") != f["taille"]:
                    raise ValueError(f"taille à l'arrivée {None if not vu else vu.get('taille')} ≠ {f['taille']}")
                s = vu.get("sha256")
                if s is not None and s != f["sha256"]:
                    raise ValueError("empreinte rendue par la plateforme différente de l'empreinte calculée sur la machine")
                r.update(copie_faite=True, revision=rev, ordre=horloge(),
                         verification="taille et empreinte rendues par la plateforme" if s else
                         "taille seulement (empreinte non rendue) : relecture en flux exigée")
            except Exception as e:  # noqa: BLE001 — consigné ; reprise si le compte le permet
                r["erreurs"].append(f"essai {r['essais']} : {_court(e)}")
        if not r["copie_faite"]:
            r["erreurs"].append(f"copie non faite après {r['essais']} essai(s) sur {1 + REPRISES} permis")
    out["refus"] = pb[0] if pb else None
    out["toutes_faites"] = bool(fichiers) and all(r["copie_faite"] for r in out["fichiers"].values())
    return out


def relire(transport, depot: str, attendus: dict, revision: str, mode: str = "flux") -> dict:
    """Relecture au lieu de rangement (critère v8, § 4, point 5) : `attendus` = {chemin dans le dépôt : {"sha256", "taille"}}.
    `mode` « flux » (défaut) recalcule l'empreinte du téléchargement sans l'écrire ; « plateforme » lit celle que rend la plateforme
    (permis seulement si la mère a établi qu'elle la recalcule à la réception, devis v9, § 5, point 9)."""
    if mode not in ("flux", "plateforme"):
        raise ValueError(f"mode {mode!r}")
    if probleme_depot(depot) or not _REVISION.match(revision or ""):
        raise ValueError("dépôt ou révision mal formés")
    if not attendus or any(not _SHA.match(str(a.get("sha256", ""))) or not isinstance(a.get("taille"), int)
                           for a in attendus.values()):
        raise ValueError("empreintes attendues absentes ou mal formées")
    out = {"depot": depot, "revision": revision, "mode": mode, "fichiers": {}}
    for chemin, a in sorted(attendus.items()):
        r = {"sha256_attendue": a["sha256"], "taille_attendue": a["taille"], "egal": False, "erreur": None}
        try:
            if mode == "flux":
                r["sha256_lue"], r["taille_lue"] = sha256_flux(transport.flux(depot, chemin, revision))
            else:
                vu = transport.info(depot, [chemin], revision).get(chemin) or {}
                r["sha256_lue"], r["taille_lue"] = vu.get("sha256"), vu.get("taille")
            r["egal"] = r["sha256_lue"] == a["sha256"] and r["taille_lue"] == a["taille"]
        except Exception as e:  # noqa: BLE001 — une relecture impossible est un échec, jamais un succès
            r["erreur"] = _court(e)
        out["fichiers"][chemin] = r
    out["toutes_egales"] = all(r["egal"] for r in out["fichiers"].values())
    return out


def attendus_depuis_inventaire(inventaire: dict) -> tuple[str, str, dict]:
    """(dépôt, révision, attendus) tirés d'un inventaire clos de la machine : la dernière révision notée est celle où tous les
    fichiers copiés sont présents (chaque envoi est un commit sur le même dépôt, aucun n'en efface un autre)."""
    copies = inventaire.get("copies") or {}
    attendus, revisions, depots = {}, [], set()
    for lentille in sorted(copies):
        c = copies[lentille]
        depots.add(c.get("depot"))
        for chemin, f in sorted((c.get("fichiers") or {}).items()):
            if f.get("copie_faite"):
                attendus[chemin] = {"sha256": f["sha256"], "taille": f["taille"]}
                revisions.append((float(f.get("ordre") or 0), f["revision"]))
    if len(depots) != 1 or not attendus:
        raise ValueError(f"inventaire : dépôts {sorted(map(str, depots))} ou aucune copie faite")
    return depots.pop(), max(revisions)[1], attendus


def main(argv=None, transport=None, env=os.environ, sortie=print) -> int:
    """`relire --inventaire <inventaire clos> --cle-nom <variable> --sortie <json neuf> [--mode flux|plateforme] [--revision <rev>]` :
    code 0 si tous égaux, 1 sinon, 2 si la relecture n'a pas pu commencer. La clé n'est lue que par le nom de sa variable."""
    p = argparse.ArgumentParser(description="Relecture au lieu de rangement (session)")
    p.add_argument("commande", choices=("relire",))
    p.add_argument("--inventaire", type=Path, required=True)
    p.add_argument("--cle-nom", required=True)
    p.add_argument("--sortie", type=Path, required=True)
    p.add_argument("--mode", choices=("flux", "plateforme"), default="flux")
    p.add_argument("--revision")
    a = p.parse_args(argv)
    if a.sortie.exists():
        sortie(f"{a.sortie} existe déjà : on n'écrase jamais (R12)")
        return 2
    try:
        inv = json.loads(a.inventaire.read_text(encoding="utf-8"))
        if inv.get("clos") is not True:
            raise ValueError("inventaire non clos")
        depot, revision, attendus = attendus_depuis_inventaire(inv)
        cle = env.get(a.cle_nom, "")
        if len(cle) < 8:
            raise ValueError(f"clé {a.cle_nom} absente de l'environnement")
        t = transport if transport is not None else TransportHub(cle)
        r = relire(t, depot, attendus, a.revision or revision, a.mode)
    except (ValueError, OSError, KeyError, TypeError) as e:
        sortie(f"RELECTURE IMPOSSIBLE : {type(e).__name__}: {e}"[:400])
        return 2
    r["cle_nom"] = a.cle_nom
    with open(a.sortie, "x", encoding="utf-8") as fh:
        fh.write(json.dumps(r, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    sortie(json.dumps({"toutes_egales": r["toutes_egales"], "n": len(r["fichiers"]), "revision": r["revision"]}))
    return 0 if r["toutes_egales"] else 1


if __name__ == "__main__":
    sys.exit(main())
