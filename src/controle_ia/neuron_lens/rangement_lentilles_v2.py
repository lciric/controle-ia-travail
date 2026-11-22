"""Rangement de nos lentilles réajustées au dépôt privé de la plateforme de modèles (lieu L2) — v2.

v2 (2026-11-22) = v1 (`rangement_lentilles_v1.py`, `15bcf304…`, gardée sans modification) corrigée selon la contre-lecture du lanceur v4
(`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/contre-lecture-lanceur-v4-commande-v9-v1.md`, `2b223595…`), et cela seul :
- C-1 (bloquante) : **attente entre les essais d'un même fichier** (`ATTENTES_S` : 60 s avant le deuxième essai, 300 s avant le
  troisième, essais comptés sur toute la course), au lieu d'essais en rafale ; attente remplaçable pour les essais (`attendre`). Une
  borne d'attente cumulée par appel (`ATTENTE_MAX_APPEL_S`, 1 200 s) : une reprise qui la dépasserait n'est pas faite dans l'appel,
  son essai n'est pas compté, elle reste à la clôture (une coupure longue ne retient pas la course plus de 20 minutes par appel ;
  nœud N-5 de la correction) ;
- C-3 : libellé de la vérification à l'arrivée : l'empreinte que rend la plateforme peut n'être que celle que l'envoyeur déclare
  (relevés de la plateforme, § 3) ; le libellé le dit ; la seule vérification propre reste la relecture en flux de la session ;
- C-2 : `relire` rend **4, « relecture sans objet »**, quand l'inventaire clos ne prévoit aucun fichier à ranger (`prevus` vide et
  `non_copies` vide : course arrêtée avant la fin de l'ajustement de R) ; une sortie neuve le dit. En v1 : code 2, lu comme un échec.
Le texte de la v1, gardé ci-dessous, vaut pour le reste (le lanceur qui l'importe est désormais `b_beta_lancer_v5.py`).

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
ATTENTES_S = (60, 300)  # v2 (C-1) : attente avant le deuxième, puis avant le troisième essai d'un même fichier
ATTENTE_MAX_APPEL_S = 1200  # v2 (C-1, nœud N-5) : attente cumulée au plus par appel ; au-delà, la reprise reste à la clôture
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


def _dormir(secondes: float) -> None:
    """v2 (C-1) : la vraie attente entre deux essais d'un même fichier (remplacée par les essais, qui n'attendent jamais)."""
    time.sleep(secondes)


def _court(e: BaseException) -> str:
    return f"{type(e).__name__}: {e}"[:300]


def envoyer_verifie(transport, depot: str, fichiers: list[dict], message: str, deja: dict | None = None,
                    empreinte=sha256_fichier, horloge=time.time, attendre=None) -> dict:
    """Copie vérifiée de `fichiers` (chacun : `local`, `depot` (chemin dans le dépôt), `sha256`, `taille` attendus). Rend, par chemin
    dans le dépôt : `copie_faite`, `essais` (cumulés avec `deja`), `revision`, `verification`, `erreurs`, `attentes_s` ; et, pour
    l'appel, `attente_totale_s`. Rien n'est levé. v2 (C-1) : avant le k-ième essai d'un fichier (k ≥ 2, compté sur la course),
    `attendre(ATTENTES_S[k - 2])` ; si l'attente cumulée de l'appel dépassait alors `ATTENTE_MAX_APPEL_S`, la reprise n'est pas faite
    (ni comptée) et reste à la clôture (`reprise_remise`). `attendre` absent : `_dormir` (la vraie attente)."""
    attendre = attendre if attendre is not None else _dormir
    deja = deja or {}
    out = {"depot": depot, "fichiers": {}, "refus": None, "attente_totale_s": 0}
    pb = probleme_depot(depot)
    try:
        if not pb and not transport.prive(depot):
            pb = ["dépôt de rangement non privé : aucun envoi (des poids dérivés ne se publient pas)"]
    except Exception as e:  # noqa: BLE001 — consigné : aucun envoi
        pb = [f"dépôt de rangement illisible : {_court(e)}"]
    for f in fichiers:
        r = {"local": str(f["local"]), "sha256": f["sha256"], "taille": f["taille"], "copie_faite": False,
             "essais": int(deja.get(f["depot"], 0)), "revision": None, "verification": None, "erreurs": [], "attentes_s": []}
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
            if r["essais"] >= 1:  # v2 (C-1) : une reprise attend, jamais en rafale
                pause = ATTENTES_S[min(r["essais"], len(ATTENTES_S)) - 1]
                if out["attente_totale_s"] + pause > ATTENTE_MAX_APPEL_S:
                    r["reprise_remise"] = True
                    r["erreurs"].append(f"essai {r['essais'] + 1} remis à la clôture : borne d'attente de l'appel "
                                        f"({ATTENTE_MAX_APPEL_S} s) atteinte")
                    break
                attendre(pause)
                out["attente_totale_s"] += pause
                r["attentes_s"].append(pause)
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
                         verification="taille rendue et empreinte déclarée par l'envoyeur, relues à la révision rendue "
                                      "(non recalculée par la plateforme : relecture en flux maintenue)" if s else
                         "taille seulement (empreinte non rendue) : relecture en flux exigée")
            except Exception as e:  # noqa: BLE001 — consigné ; reprise si le compte le permet
                r["erreurs"].append(f"essai {r['essais']} : {_court(e)}")
        if not r["copie_faite"] and not r.get("reprise_remise"):
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
    code 0 si tous égaux, 1 sinon, 2 si la relecture n'a pas pu commencer, 4 (v2, C-2) si elle est sans objet : inventaire clos dont
    `prevus` et `non_copies` sont vides (aucun fichier à ranger ; aucune clé n'est alors lue). La clé n'est lue que par le nom de sa
    variable."""
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
        if inv.get("prevus") == {} and inv.get("non_copies") == []:  # v2 (C-2) : rien à ranger, donc rien à relire
            vide = {"sans_objet": True, "toutes_egales": None, "fichiers": {}, "cle_nom": a.cle_nom,
                    "note": "inventaire clos sans fichier à ranger (prevus vide) : relecture sans objet",
                    "lentilles": inv.get("lentilles"), "run_id": inv.get("run_id"), "numero": inv.get("numero")}
            with open(a.sortie, "x", encoding="utf-8") as fh:
                fh.write(json.dumps(vide, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
            sortie("RELECTURE SANS OBJET : inventaire clos sans fichier à ranger")
            return 4
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
