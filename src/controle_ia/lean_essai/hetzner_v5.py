"""Client de l'API de Hetzner Cloud pour la machine de l'essai Lean — v5 (contre-lecture courte des points « machine » de la
v4, `918662a7…`, décision R-2323).

- CLC4-01 : emplacement du serveur lu par `location` (forme actuelle), avec repli explicite sur `datacenter.location`
  (ancienne forme ; le journal public des changements de Hetzner la dit retirée des réponses « Servers » au 1ᵉʳ juillet 2026,
  affirmation non vérifiée sur une réponse réelle). Aucune `KeyError` possible : (None, "aucune") si aucune forme n'est
  lisible ; de même pour le type et l'heure de création.
- CLC4-05 : un refus durable (statut 401 : jeton inconnu ; 403 : droit manquant, jeton en lecture seule) lève `RefusDurable`,
  distinct d'une erreur passagère ; la minuterie v5 borne les refus durables et s'arrête bruyamment.
- Poste local (procédure v5) : clé SSH et pare-feu du nuage étiquetés au jeton de la création (`essai`, `pas`, `go`,
  `creation`), que la mère relit par son propre jeton pour prouver le même projet.
Reste du client : `hetzner_v4` (et v3, v2, v1).
"""
from __future__ import annotations

import time
from datetime import datetime

from controle_ia.gardes import GardeArret

from .hetzner_v1 import ETIQUETTES, NOM_MACHINE, ErreurHetzner, regles_coupure, regles_installation  # noqa: F401
from .hetzner_v3 import ETIQUETTE_CREATION, verifier_coupure_nuage  # noqa: F401
from .hetzner_v4 import TYPES_PERMIS, ClientHetzner4, CreationRefusee, transport_urllib  # noqa: F401

STATUTS_REFUS_DURABLE = (401, 403)


class RefusDurable(ErreurHetzner):
    """L'API refuse la requête pour une raison qui ne passera pas d'elle-même (401 ou 403)."""


def _nom(x) -> str | None:
    if isinstance(x, dict):
        x = x.get("name")
    return x.strip() if isinstance(x, str) and x.strip() else None


def lieu_du_serveur(s) -> tuple[str | None, str]:
    """(lieu, source) : `location.name` (forme actuelle), sinon `datacenter.location.name` (ancienne forme), sinon
    (None, "aucune"). Jamais d'exception, quelle que soit la forme de la réponse."""
    if not isinstance(s, dict):
        return None, "aucune"
    lieu = _nom(s.get("location"))
    if lieu:
        return lieu, "location"
    dc = s.get("datacenter")
    lieu = _nom(dc.get("location")) if isinstance(dc, dict) else None
    if lieu:
        return lieu, "datacenter.location"
    return None, "aucune"


def type_du_serveur(s) -> str | None:
    return _nom(s.get("server_type")) if isinstance(s, dict) else None


def creation_du_serveur(s) -> datetime | None:
    brut = s.get("created") if isinstance(s, dict) else None
    if not isinstance(brut, str):
        return None
    try:
        d = datetime.fromisoformat(brut.replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo is not None else None


class ClientHetzner5(ClientHetzner4):
    def __init__(self, transport=transport_urllib, dormir=time.sleep):
        super().__init__(transport=transport, dormir=dormir)

    @staticmethod
    def _refus(methode: str, chemin: str, statut: int) -> RefusDurable:
        return RefusDurable(f"{methode} {chemin.split('?')[0]} : statut {statut} (refus durable : jeton inconnu, ou sans droit "
                            "d'écriture)")

    def _req(self, methode: str, chemin: str, corps: dict | None = None, attendus=(200, 201, 204)) -> dict:
        statut, d = self.transport(methode, chemin, corps)
        if statut in STATUTS_REFUS_DURABLE:
            raise self._refus(methode, chemin, statut)
        if statut not in attendus:
            err = d.get("error", {}) if isinstance(d, dict) else {}
            raise ErreurHetzner(f"{methode} {chemin} : statut {statut} ({err.get('code')}: {str(err.get('message'))[:200]})")
        return d if isinstance(d, dict) else {}

    def serveur(self, ident: int) -> dict | None:
        statut, d = self.transport("GET", f"/servers/{int(ident)}", None)
        if statut == 404:
            return None
        if statut in STATUTS_REFUS_DURABLE:
            raise self._refus("GET", f"/servers/{int(ident)}", statut)
        if statut != 200 or not isinstance(d, dict) or not isinstance(d.get("server"), dict):
            raise ErreurHetzner(f"GET /servers/{int(ident)} : statut {statut} ou réponse sans serveur")
        return d["server"]

    # -- accès du poste local : clé SSH et pare-feu étiquetés -------------------------------------------------------------
    def creer_cle_ssh_etiquetee(self, nom: str, cle_publique: str, etiquettes: dict) -> dict:
        k = self._req("POST", "/ssh_keys", {"name": nom, "public_key": cle_publique, "labels": etiquettes}).get("ssh_key", {})
        return {"id": int(k["id"]), "nom": k.get("name"), "empreinte": k.get("fingerprint")}

    def creer_pare_feu_etiquete(self, nom: str, regles: list[dict], etiquettes: dict) -> dict:
        f = self._req("POST", "/firewalls", {"name": nom, "rules": regles, "labels": etiquettes}).get("firewall", {})
        return {"id": int(f["id"]), "nom": f.get("name")}

    def ips_primaires_libres(self) -> list[tuple[int, str]]:
        """Adresses IP primaires du projet attribuées à aucun serveur (facturées seules) : identifiants et noms."""
        d = self._req("GET", "/primary_ips?per_page=50")
        if d.get("meta", {}).get("pagination", {}).get("next_page"):
            raise GardeArret("plus de 50 adresses IP primaires : lecture incomplète refusée")
        return [(int(x["id"]), x.get("name")) for x in d.get("primary_ips", []) if x.get("assignee_id") is None]

    def lire_cle_ssh(self, ident: int) -> dict | None:
        statut, d = self.transport("GET", f"/ssh_keys/{int(ident)}", None)
        if statut == 404:
            return None
        if statut in STATUTS_REFUS_DURABLE:
            raise self._refus("GET", f"/ssh_keys/{int(ident)}", statut)
        if statut != 200 or not isinstance(d, dict) or not isinstance(d.get("ssh_key"), dict):
            raise ErreurHetzner(f"GET /ssh_keys/{int(ident)} : statut {statut}")
        return d["ssh_key"]
