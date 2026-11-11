"""Client de l'API de Hetzner Cloud pour la machine de l'essai Lean — v3 (contre-lecture courte `1fea30ab…`, R-2302).

- CLC2-03 : un corps non UTF-8 est converti en `ErreurHetzner` ; l'absence d'un serveur n'est constatée que par **deux lectures**
  (`GET /servers/N` rend 404 **et** l'identifiant manque à l'inventaire).
- CLC2-04 : création avec une **étiquette unique** (`creation=<jeton>`) ; recherche par étiquette si la réponse se perd.
- CLC2-06 : lecture du serveur : ses pare-feux doivent être **exactement** celui attendu, à l'état « applied » ; puis la seule
  règle sortante de coupure.
- Note 6 : devise « EUR » exigée ; liste des types sans page suivante (sinon arrêt).
"""
from __future__ import annotations

import http.client
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

from controle_ia.gardes import GardeArret

from . import garde_go_v1
from .hetzner_v1 import API, ETIQUETTES, NOM_MACHINE, ErreurHetzner, regles_coupure, regles_installation  # noqa: F401
from .hetzner_v2 import ClientHetzner2

ETIQUETTE_CREATION = "creation"


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
            return e.code, json.loads(e.read().decode("utf-8", errors="replace"))
        except (ValueError, OSError, http.client.HTTPException):
            return e.code, {"error": {"code": "illisible", "message": ""}}
    except urllib.error.URLError as e:
        raise ErreurHetzner(f"API de Hetzner injoignable ({type(e.reason).__name__})") from None
    except (OSError, http.client.HTTPException, ValueError) as e:   # ValueError : JSON ou UTF-8 illisible
        raise ErreurHetzner(f"échange avec l'API de Hetzner interrompu ou illisible ({type(e).__name__})") from None


class ClientHetzner3(ClientHetzner2):
    def __init__(self, transport=transport_urllib, dormir=time.sleep):
        super().__init__(transport=transport, dormir=dormir)

    def types_serveurs(self) -> list[dict]:
        d = self._req("GET", "/server_types?per_page=50")
        if d.get("meta", {}).get("pagination", {}).get("next_page"):
            raise GardeArret("liste des types de serveur sur plusieurs pages : lecture incomplète refusée")
        return d.get("server_types", [])

    def prix_horaire_eur(self, type_serveur: str, lieu: str) -> dict:
        prix = super().prix_horaire_eur(type_serveur, lieu)
        if prix.get("devise") != "EUR":
            raise GardeArret(f"devise des prix {prix.get('devise')!r}, « EUR » attendue")
        return prix

    def absence_confirmee(self, ident: int) -> bool:
        """Deux lectures : `GET /servers/N` rend 404, et l'identifiant manque à l'inventaire."""
        if self.serveur(ident) is not None:
            return False
        return all(i != int(ident) for i, _ in self.inventaire())

    def chercher_par_etiquette(self, jeton: str) -> list[tuple[int, str]]:
        selecteur = urllib.parse.quote(f"{ETIQUETTE_CREATION}={jeton}", safe="")
        d = self._req("GET", f"/servers?label_selector={selecteur}&per_page=50")
        return [(s["id"], s["name"]) for s in d.get("servers", [])]

    def creer_serveur_etiquete(self, go_id: str, chemin_registre, aujourdhui, type_serveur: str, image: str,
                               emplacement: str, cles_ssh: list[int], pare_feux: list[int], jeton: str,
                               nom: str = NOM_MACHINE) -> dict:
        garde_go_v1.autoriser_creation_machine(go_id, chemin_registre, aujourdhui)
        if any(n == nom for _, n in self.inventaire()):
            raise GardeArret(f"un serveur nommé {nom!r} existe déjà : un seul serveur par pas")
        corps = {"name": nom, "server_type": type_serveur, "image": image, "location": emplacement,
                 "ssh_keys": cles_ssh, "firewalls": [{"firewall": f} for f in pare_feux],
                 "labels": dict(ETIQUETTES, go=go_id, **{ETIQUETTE_CREATION: jeton}), "start_after_create": True,
                 "public_net": {"enable_ipv4": True, "enable_ipv6": False}}
        return self._req("POST", "/servers", corps)


def verifier_coupure_nuage(client: ClientHetzner3, pare_feu: int, serveur: int) -> dict:
    """CLC2-06 : le serveur porte exactement le pare-feu attendu, appliqué ; ce pare-feu a pour seule règle sortante
    ICMP vers 192.0.2.1/32 (refus implicite du reste) et s'applique au serveur."""
    s = client.serveur(serveur)
    if s is None:
        raise GardeArret(f"serveur {serveur} absent")
    portes = s.get("public_net", {}).get("firewalls", [])
    if [(f.get("id"), f.get("status")) for f in portes] != [(pare_feu, "applied")]:
        raise GardeArret(f"pare-feux du serveur {portes} ≠ le seul pare-feu {pare_feu} à l'état « applied »")
    f = client.lire_pare_feu(pare_feu)
    sortantes = [r for r in f.get("rules", []) if r.get("direction") == "out"]
    if [(r.get("protocol"), r.get("destination_ips")) for r in sortantes] != [("icmp", ["192.0.2.1/32"])]:
        raise GardeArret(f"pare-feu {pare_feu} : règles sortantes {sortantes} ≠ la seule règle de coupure")
    appliques = [a for a in f.get("applied_to", []) if a.get("type") == "server"
                 and a.get("server", {}).get("id") == serveur]
    if not appliques:
        raise GardeArret(f"pare-feu {pare_feu} non appliqué au serveur {serveur}")
    return {"pare_feu": pare_feu, "serveur": serveur, "pare_feux_du_serveur": portes, "regles": f.get("rules", [])}
