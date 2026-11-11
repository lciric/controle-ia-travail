"""Client de l'API de Hetzner Cloud pour la machine de l'essai Lean — v2 (contre-lecture `2077ae26…`, R-2300).

- CLL-05 : le transport attrape aussi `OSError` (délai de lecture, connexion fermée) et `http.client.HTTPException`, toujours
  convertis en `ErreurHetzner` sans le jeton ; la minuterie v2 réessaie la destruction.
- CLL-06 : prix horaire **lu dans l'API** (type et lieu, TTC) plus l'adresse IPv4 primaire (`/pricing`), jamais déclaré.
- CLL-13 : lecture du pare-feu du nuage et contrôle qu'il porte la règle de coupure et s'applique au serveur.
Reste du client (inventaire, destruction par identifiant après lecture du nom, création avec IPv6 coupé) : `hetzner_v1`.
"""
from __future__ import annotations

import http.client
import json
import os
import time
import urllib.error
import urllib.request

from controle_ia.gardes import GardeArret

from .hetzner_v1 import API, ETIQUETTES, NOM_MACHINE, ClientHetzner, ErreurHetzner, regles_coupure, regles_installation  # noqa: F401


def transport_urllib(methode: str, chemin: str, corps: dict | None = None, delai: float = 30.0) -> tuple[int, dict]:
    jeton = os.environ.get("HCLOUD_TOKEN")
    if not jeton:
        raise ErreurHetzner("HCLOUD_TOKEN absent de l'environnement")
    donnees = None if corps is None else json.dumps(corps).encode("utf-8")
    req = urllib.request.Request(API + chemin, data=donnees, method=methode)
    req.add_header("Authorization", "Bearer " + jeton)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=delai) as r:
            texte = r.read().decode("utf-8")
            return r.status, (json.loads(texte) if texte.strip() else {})
    except urllib.error.HTTPError as e:
        try:
            texte = e.read().decode("utf-8", errors="replace")
            return e.code, json.loads(texte)
        except (json.JSONDecodeError, OSError, http.client.HTTPException):
            return e.code, {"error": {"code": "illisible", "message": ""}}
    except urllib.error.URLError as e:
        raise ErreurHetzner(f"API de Hetzner injoignable ({type(e.reason).__name__})") from None
    except (OSError, http.client.HTTPException, json.JSONDecodeError) as e:
        raise ErreurHetzner(f"échange avec l'API de Hetzner interrompu ({type(e).__name__})") from None


class ClientHetzner2(ClientHetzner):
    def __init__(self, transport=transport_urllib, dormir=time.sleep):
        super().__init__(transport=transport, dormir=dormir)

    def prix_horaire_eur(self, type_serveur: str, lieu: str) -> dict:
        """Prix horaire TTC du type au lieu, plus l'adresse IPv4 primaire au même lieu ; absent ⇒ arrêt (rien de deviné)."""
        types = {t["name"]: t for t in self.types_serveurs()}
        if type_serveur not in types:
            raise GardeArret(f"type {type_serveur!r} absent de l'API")
        prix = [p for p in types[type_serveur].get("prices", []) if p.get("location") == lieu]
        if len(prix) != 1:
            raise GardeArret(f"prix du type {type_serveur!r} au lieu {lieu!r} introuvable")
        serveur = float(prix[0]["price_hourly"]["gross"])
        tarifs = self._req("GET", "/pricing").get("pricing", {})
        ipv4 = [p for x in tarifs.get("primary_ips", []) if x.get("type") == "ipv4"
                for p in x.get("prices", []) if p.get("location") == lieu]
        if len(ipv4) != 1:
            raise GardeArret(f"prix de l'adresse IPv4 primaire au lieu {lieu!r} introuvable")
        adresse = float(ipv4[0]["price_hourly"]["gross"])
        return {"serveur": serveur, "ipv4": adresse, "total": serveur + adresse, "devise": tarifs.get("currency")}

    def lire_pare_feu(self, ident: int) -> dict:
        return self._req("GET", f"/firewalls/{int(ident)}")["firewall"]


def verifier_coupure_nuage(client: ClientHetzner2, pare_feu: int, serveur: int) -> dict:
    """CLL-13 : avant la phase « après », le pare-feu du nuage porte une seule règle sortante (ICMP vers 192.0.2.1/32 : refus
    implicite du reste) et s'applique au serveur. Rend le relevé à consigner."""
    f = client.lire_pare_feu(pare_feu)
    sortantes = [r for r in f.get("rules", []) if r.get("direction") == "out"]
    if [(r.get("protocol"), r.get("destination_ips")) for r in sortantes] != [("icmp", ["192.0.2.1/32"])]:
        raise GardeArret(f"pare-feu {pare_feu} : règles sortantes {sortantes} ≠ la seule règle de coupure")
    appliques = [a for a in f.get("applied_to", []) if a.get("type") == "server"
                 and a.get("server", {}).get("id") == serveur]
    if not appliques:
        raise GardeArret(f"pare-feu {pare_feu} non appliqué au serveur {serveur}")
    return {"pare_feu": pare_feu, "serveur": serveur, "regles": f.get("rules", []), "applique": appliques}
