"""Client de l'API de Hetzner Cloud pour la machine de l'essai Lean — v4 (contre-lecture courte de la v3 `b6ca886d…`, R-2307).

- CLC3-07 (a) : recherche des serveurs de l'essai par les **étiquettes fixes** (`essai=lean,pas=d1a`), sans jeton ni journal.
- CLC3-08, note 5 : une création **refusée** par l'API (statut 4xx : rien n'a été créé) lève `CreationRefusee`, distincte d'une
  réponse perdue (transport) où le serveur a pu être créé.
- CLC3-10 : type de serveur limité à la liste du devis machine (`TYPES_PERMIS`, rapport de l'outillage v1, pièce MACHINE,
  `0706b12f…` : `ccx33` proposé, `ccx23` et `cx53` en variantes).
Reste du client : `hetzner_v3` (et v2, v1).
"""
from __future__ import annotations

import time
import urllib.parse

from controle_ia.gardes import GardeArret

from . import garde_go_v1
from .hetzner_v1 import ETIQUETTES, NOM_MACHINE, ErreurHetzner  # noqa: F401
from .hetzner_v3 import ETIQUETTE_CREATION, ClientHetzner3, transport_urllib, verifier_coupure_nuage  # noqa: F401

TYPES_PERMIS = ("ccx23", "ccx33", "cx53")


class CreationRefusee(RuntimeError):
    """L'API a refusé la création (statut 4xx) : aucun serveur n'a été créé."""


class ClientHetzner4(ClientHetzner3):
    def __init__(self, transport=transport_urllib, dormir=time.sleep):
        super().__init__(transport=transport, dormir=dormir)

    def chercher_par_etiquettes_fixes(self, pas: str = "d1a") -> list[tuple[int, str]]:
        selecteur = urllib.parse.quote(f"essai={ETIQUETTES['essai']},pas={pas}", safe="")
        d = self._req("GET", f"/servers?label_selector={selecteur}&per_page=50")
        if d.get("meta", {}).get("pagination", {}).get("next_page"):
            raise GardeArret("plus de 50 serveurs aux étiquettes de l'essai : lecture incomplète refusée")
        return [(s["id"], s["name"]) for s in d.get("servers", [])]

    def creer_serveur_etiquete(self, go_id: str, chemin_registre, aujourdhui, type_serveur: str, image: str,
                               emplacement: str, cles_ssh: list[int], pare_feux: list[int], jeton: str,
                               nom: str = NOM_MACHINE) -> dict:
        if type_serveur not in TYPES_PERMIS:
            raise GardeArret(f"type {type_serveur!r} hors de la liste du devis {TYPES_PERMIS}")
        garde_go_v1.autoriser_creation_machine(go_id, chemin_registre, aujourdhui)
        if any(n == nom for _, n in self.inventaire()):
            raise GardeArret(f"un serveur nommé {nom!r} existe déjà : un seul serveur par pas")
        corps = {"name": nom, "server_type": type_serveur, "image": image, "location": emplacement,
                 "ssh_keys": cles_ssh, "firewalls": [{"firewall": f} for f in pare_feux],
                 "labels": dict(ETIQUETTES, go=go_id, **{ETIQUETTE_CREATION: jeton}), "start_after_create": True,
                 "public_net": {"enable_ipv4": True, "enable_ipv6": False}}
        statut, d = self.transport("POST", "/servers", corps)
        if 400 <= statut < 500:
            err = d.get("error", {}) if isinstance(d, dict) else {}
            raise CreationRefusee(f"création refusée par l'API : statut {statut} ({err.get('code')})")
        if statut not in (200, 201):
            raise ErreurHetzner(f"POST /servers : statut {statut} (création incertaine)")
        return d
