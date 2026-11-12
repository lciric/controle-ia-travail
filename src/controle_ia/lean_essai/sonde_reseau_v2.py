"""Sonde du réseau sortant, classée par la cause de l'échec — essai Lean (D-1a), v2. Autonome (bibliothèque standard).

v2 (R-2415) : copie de `sonde_reseau_v1.py` (inchangée, R12 ; l'exécuteur du bac l'importe toujours) dont seule change la
sonde du résolveur système. Au premier essai, `example.com` a été lu « ouverte » après la coupure : la réponse venait du cache
de systemd-resolved, rempli par la sonde « avant ». La v2 demande **un nom aléatoire jamais demandé** sous `example.com`
(`<32 hexadécimaux>.example.com`, tiré à chaque appel ; aucune réponse en cache possible) et classe :
« ouverte » si une adresse revient ou si la réponse « ce nom n'existe pas » revient (EAI_NONAME, EAI_NODATA : un serveur a
répondu) ; « fermée » si la résolution échoue faute de réponse (EAI_AGAIN) ; « indéterminée » pour toute autre cause, qui
est toujours un écart.

Texte de la v1 :
Sonde du réseau sortant, classée par la cause de l'échec — essai Lean (D-1a), v1. Autonome (bibliothèque standard).

Classes : « ouverte » (une réponse est revenue, même un refus RST venu de l'extérieur), « fermée » (paquet jeté sans réponse,
refus local EPERM, aucune route locale), « indéterminée » (cause qui ne tranche pas, par exemple EHOSTUNREACH, qui peut venir
d'un routeur extérieur). Aucune cible n'est un nom à résoudre, sauf la sonde DNS du résolveur système, classée à part.
Cas sain (R5) : la boucle locale, ouverte par un serveur de la sonde elle-même, doit être lue « ouverte » ; avant la coupure,
les cibles extérieures doivent aussi être lues « ouvertes » (la sonde sait voir une sortie ouverte).

Usage : `python3 sonde_reseau_v2.py --attendu ouverte|fermee` ; code 0 si chaque cible a la classe attendue (la boucle
locale toujours « ouverte »), 1 sinon ; le relevé JSON va sur la sortie standard.
"""
from __future__ import annotations

import argparse
import errno
import json
import secrets
import socket
import struct
import sys
import threading

CIBLES_TCP = [("1.1.1.1", 443), ("9.9.9.9", 443), ("8.8.8.8", 443)]
CIBLES_DNS = ["1.1.1.1", "185.12.64.1", "185.12.64.2"]  # deux résolveurs de Hetzner, que son pare-feu laisse passer
NOM_DNS = "example.com"


def sonde_tcp(hote: str, port: int, delai: float = 5.0) -> tuple[str, str]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(delai)
    try:
        s.connect((hote, port))
        return "ouverte", "connexion établie"
    except socket.timeout:
        return "fermée", "sans réponse (paquet jeté)"
    except ConnectionRefusedError:
        return "ouverte", "refus RST revenu : la sortie passe"
    except PermissionError:
        return "fermée", "refus local (EPERM)"
    except OSError as e:
        if e.errno in (errno.ENETUNREACH, errno.EADDRNOTAVAIL):
            return "fermée", f"aucune route locale ({errno.errorcode.get(e.errno)})"
        return "indéterminée", f"{type(e).__name__} {errno.errorcode.get(e.errno)}"
    finally:
        s.close()


def _requete_dns(nom: str) -> bytes:
    entete = struct.pack(">HHHHHH", 0x4c33, 0x0100, 1, 0, 0, 0)
    question = b"".join(bytes([len(p)]) + p.encode() for p in nom.split(".")) + b"\x00" + struct.pack(">HH", 1, 1)
    return entete + question


def sonde_dns(serveur: str, delai: float = 5.0) -> tuple[str, str]:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(delai)
    try:
        s.sendto(_requete_dns(NOM_DNS), (serveur, 53))
        donnees, _ = s.recvfrom(512)
        return "ouverte", f"réponse de {len(donnees)} octets"
    except socket.timeout:
        return "fermée", "sans réponse"
    except PermissionError:
        return "fermée", "refus local (EPERM)"
    except OSError as e:
        if e.errno in (errno.ENETUNREACH, errno.EADDRNOTAVAIL):
            return "fermée", f"aucune route locale ({errno.errorcode.get(e.errno)})"
        if e.errno == errno.ECONNREFUSED:
            return "ouverte", "ICMP « port injoignable » revenu"
        return "indéterminée", f"{type(e).__name__} {errno.errorcode.get(e.errno)}"
    finally:
        s.close()


CODES_REPONSE_NEGATIVE = {getattr(socket, n) for n in ("EAI_NONAME", "EAI_NODATA") if hasattr(socket, n)}
CODES_SANS_REPONSE = {getattr(socket, n) for n in ("EAI_AGAIN",) if hasattr(socket, n)}


def nom_jamais_demande() -> str:
    return f"{secrets.token_hex(16)}.{NOM_DNS}"


def sonde_resolveur_systeme(nom: str | None = None) -> tuple[str, str]:
    nom = nom or nom_jamais_demande()
    try:
        socket.gethostbyname(nom)
        return "ouverte", "adresse revenue pour un nom jamais demandé"
    except socket.gaierror as e:
        if e.errno in CODES_REPONSE_NEGATIVE:
            return "ouverte", f"réponse « nom inexistant » revenue ({e.errno})"
        if e.errno in CODES_SANS_REPONSE:
            return "fermée", f"aucune réponse ({e.errno})"
        return "indéterminée", f"résolution impossible, cause qui ne tranche pas ({e.errno})"


def sonde_boucle_locale() -> tuple[str, str]:
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind(("127.0.0.1", 0))
    serveur.listen(1)
    port = serveur.getsockname()[1]
    t = threading.Thread(target=lambda: serveur.accept()[0].close(), daemon=True)
    t.start()
    try:
        return sonde_tcp("127.0.0.1", port, 3.0)
    finally:
        serveur.close()


def relever() -> list[dict]:
    r = [{"cible": "boucle locale (sain)", **dict(zip(("classe", "cause"), sonde_boucle_locale()))}]
    r += [{"cible": f"tcp {h}:{p}", **dict(zip(("classe", "cause"), sonde_tcp(h, p)))} for h, p in CIBLES_TCP]
    r += [{"cible": f"dns udp {s}:53", **dict(zip(("classe", "cause"), sonde_dns(s)))} for s in CIBLES_DNS]
    r.append({"cible": f"résolveur système (nom aléatoire sous {NOM_DNS})",
              **dict(zip(("classe", "cause"), sonde_resolveur_systeme()))})
    return r


def juger(releve: list[dict], attendu: str) -> list[str]:
    """Écarts au relevé attendu ; la boucle locale doit toujours être « ouverte » ; « indéterminée » est toujours un écart."""
    cible_ext = "ouverte" if attendu == "ouverte" else "fermée"
    ecarts = []
    for x in releve:
        voulu = "ouverte" if x["cible"].startswith("boucle locale") else cible_ext
        if x["classe"] != voulu:
            ecarts.append(f"{x['cible']} : {x['classe']} ({x['cause']}), {voulu} attendue")
    return ecarts


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--attendu", choices=["ouverte", "fermee"], required=True)
    a = ap.parse_args(argv)
    releve = relever()
    ecarts = juger(releve, a.attendu)
    json.dump({"attendu": a.attendu, "releve": releve, "ecarts": ecarts}, sys.stdout, ensure_ascii=False, indent=1)
    sys.stdout.write("\n")
    return 0 if not ecarts else 1


if __name__ == "__main__":
    sys.exit(main())
