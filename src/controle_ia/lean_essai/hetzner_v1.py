"""Client minimal de l'API de Hetzner Cloud pour la machine de l'essai Lean (D-1a) — v1.

- Jeton lu **par son nom** (`HCLOUD_TOKEN`) au moment de chaque requête ; jamais affiché, écrit, journalisé ni mis dans un
  message d'erreur.
- Destruction **par identifiant** (R10), après lecture du nom du serveur : un serveur dont le nom n'est pas celui attendu n'est
  jamais touché (inventaire par identifiants et noms seulement).
- Création : la commande cite le GO de l'outillage, vérifié dans `registres/go.md` (`garde_go_v1.autoriser_creation_machine`) ;
  refus si un serveur du même nom existe ; IPv6 coupé à la création.
- Pare-feu du nuage : règles d'installation (entrée TCP 22 depuis la seule adresse du poste ; aucune règle sortante, donc sortie
  ouverte) et de coupure (même entrée, plus une seule règle sortante ICMP vers 192.0.2.1/32, adresse de documentation qui ne
  mène nulle part : la sortie bascule en refus implicite ; même dessin que la machine jetable v3, § 2.2.3).
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from datetime import date

from controle_ia.gardes import GardeArret

from . import garde_go_v1

API = "https://api.hetzner.cloud/v1"
NOM_MACHINE = "lean-outillage-d1a"
ETIQUETTES = {"essai": "lean", "pas": "d1a", "go": "GO-2026-11-10-13"}


class ErreurHetzner(RuntimeError):
    pass


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
        texte = e.read().decode("utf-8", errors="replace")
        try:
            return e.code, json.loads(texte)
        except json.JSONDecodeError:
            return e.code, {"error": {"code": "illisible", "message": texte[:200]}}
    except urllib.error.URLError as e:
        raise ErreurHetzner(f"API de Hetzner injoignable ({type(e.reason).__name__})") from None


def regles_installation(ip_poste: str) -> list[dict]:
    if "/" in ip_poste or not ip_poste:
        raise GardeArret("adresse du poste : une adresse IPv4 seule attendue")
    return [{"direction": "in", "protocol": "tcp", "port": "22", "source_ips": [ip_poste + "/32"],
             "description": "SSH depuis le seul poste"}]


def regles_coupure(ip_poste: str) -> list[dict]:
    return regles_installation(ip_poste) + [
        {"direction": "out", "protocol": "icmp", "destination_ips": ["192.0.2.1/32"],
         "description": "seule règle sortante : bascule la sortie en refus implicite"}]


class ClientHetzner:
    def __init__(self, transport=transport_urllib, dormir=time.sleep):
        self.transport = transport
        self.dormir = dormir

    def _req(self, methode: str, chemin: str, corps: dict | None = None, attendus=(200, 201, 204)) -> dict:
        statut, d = self.transport(methode, chemin, corps)
        if statut not in attendus:
            err = d.get("error", {}) if isinstance(d, dict) else {}
            raise ErreurHetzner(f"{methode} {chemin} : statut {statut} ({err.get('code')}: {str(err.get('message'))[:200]})")
        return d

    # -- lecture ----------------------------------------------------------------------------------------------------------
    def serveur(self, ident: int) -> dict | None:
        statut, d = self.transport("GET", f"/servers/{int(ident)}", None)
        if statut == 404:
            return None
        if statut != 200:
            raise ErreurHetzner(f"GET /servers/{ident} : statut {statut}")
        return d["server"]

    def inventaire(self) -> list[tuple[int, str]]:
        """Identifiants et noms seulement."""
        sortie, page = [], 1
        while True:
            d = self._req("GET", f"/servers?per_page=50&page={page}")
            sortie += [(s["id"], s["name"]) for s in d.get("servers", [])]
            suivante = d.get("meta", {}).get("pagination", {}).get("next_page")
            if not suivante:
                return sortie
            page = suivante

    def types_serveurs(self) -> list[dict]:
        return self._req("GET", "/server_types?per_page=50").get("server_types", [])

    # -- destruction (R10) --------------------------------------------------------------------------------------------------
    def supprimer_serveur(self, ident: int, nom_attendu: str = NOM_MACHINE) -> str:
        s = self.serveur(ident)
        if s is None:
            return "absent"
        if s.get("name") != nom_attendu:
            raise GardeArret(f"serveur {ident} nommé {s.get('name')!r}, {nom_attendu!r} attendu : aucun autre serveur touché")
        self._req("DELETE", f"/servers/{int(ident)}")
        return "suppression demandée"

    def attendre_absence(self, ident: int, delai_s: float = 300.0, pas_s: float = 5.0) -> bool:
        ecoule = 0.0
        while ecoule <= delai_s:
            if self.serveur(ident) is None:
                return True
            self.dormir(pas_s)
            ecoule += pas_s
        return False

    # -- création -----------------------------------------------------------------------------------------------------------
    def creer_serveur(self, go_id: str, chemin_registre, aujourdhui: date, type_serveur: str, image: str,
                      emplacement: str, cles_ssh: list[int], pare_feux: list[int], nom: str = NOM_MACHINE) -> dict:
        garde_go_v1.autoriser_creation_machine(go_id, chemin_registre, aujourdhui)
        if any(n == nom for _, n in self.inventaire()):
            raise GardeArret(f"un serveur nommé {nom!r} existe déjà : un seul serveur par pas")
        corps = {"name": nom, "server_type": type_serveur, "image": image, "location": emplacement,
                 "ssh_keys": cles_ssh, "firewalls": [{"firewall": f} for f in pare_feux],
                 "labels": dict(ETIQUETTES, go=go_id), "start_after_create": True,
                 "public_net": {"enable_ipv4": True, "enable_ipv6": False}}
        return self._req("POST", "/servers", corps)

    def creer_cle_ssh(self, nom: str, cle_publique: str) -> int:
        return self._req("POST", "/ssh_keys", {"name": nom, "public_key": cle_publique, "labels": ETIQUETTES})["ssh_key"]["id"]

    def supprimer_cle_ssh(self, ident: int) -> None:
        self._req("DELETE", f"/ssh_keys/{int(ident)}")

    def creer_pare_feu(self, nom: str, regles: list[dict]) -> int:
        return self._req("POST", "/firewalls", {"name": nom, "rules": regles, "labels": ETIQUETTES})["firewall"]["id"]

    def poser_regles(self, ident: int, regles: list[dict]) -> None:
        self._req("POST", f"/firewalls/{int(ident)}/actions/set_rules", {"rules": regles})

    def supprimer_pare_feu(self, ident: int) -> None:
        self._req("DELETE", f"/firewalls/{int(ident)}")
