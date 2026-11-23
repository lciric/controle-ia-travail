"""Demande au loueur de cartes l'adresse et le port de copie d'une instance ARRÊTÉE de relecture — v1 (22 novembre 2026,
classe B). Procédure : `../procedure-transfert-activations-b5f-v1.md`, § 5. Accord : GO-2026-11-22-117.

Même requête que `vastai copy C.<ID>:<chemin> local:<chemin>` du client du loueur (version 1.11.2, lue dans
`vastai/cli/commands/storage.py` et `vastai/api/storage.py`) : `storage.copy(client, "C.<ID>", "local", source,
destination)` ; mais ce programme ne lance PAS rsync : il imprime seulement l'adresse et le port rendus, puis la commande
rsync à jouer SUR LE SERVEUR DE TRANSFERT (et non ici). La clé VAST_API_KEY est lue par son nom, jamais imprimée ; la
réponse brute n'est jamais imprimée (seuls `src_addr` et `src_port` sortent, après contrôle de leur forme).
Usage : demande_rsync_vast_v1.py ID RUN_ID MONTAGE
  ID : identifiant de l'instance de relecture ; RUN_ID : AAAAMMJJ-HHMMSS-b5f-lecture ; MONTAGE : point de montage du volume
  sur le serveur (`/mnt/HC_Volume_<id>`).
Mode « sonde » : SONDE=1 demande le seul fichier `inventaire-activations.json` (quelques centaines de kilo-octets).
"""
from __future__ import annotations

import os
import re
import shlex
import sys

ACCORD = "GO-2026-11-22-117"
_RUN = re.compile(r"^[0-9]{8}-[0-9]{6}-b5f-lecture$")
_ADDR = re.compile(r"^[A-Za-z0-9.-]{1,253}$")
_MONTAGE = re.compile(r"^/mnt/HC_Volume_[0-9]+$")


class Refus(Exception):
    pass


def chemins(ident: str, run_id: str, montage: str, sonde: bool) -> tuple[str, str]:
    if not str(ident).isdigit():
        raise Refus("identifiant d'instance numérique attendu (R10)")
    if _RUN.fullmatch(str(run_id)) is None:
        raise Refus("identifiant de marche AAAAMMJJ-HHMMSS-b5f-lecture attendu")
    if _MONTAGE.fullmatch(str(montage)) is None:
        raise Refus("point de montage /mnt/HC_Volume_<id> attendu (jamais /root ni /, consigne du loueur)")
    base = f"/root/b5f-lecture-v1/depot/donnees/{run_id}"
    if sonde:   # hors du dossier vérifié : la sonde n'y compterait pas « en trop »
        return f"{base}/inventaire-activations.json", f"{montage}/b5f-activations-v1/sonde-{run_id}/"
    return f"{base}/activations/", f"{montage}/b5f-activations-v1/{run_id}/activations/"


def reduire_reponse(rj) -> tuple[str, int]:
    """Seuls l'adresse et le port sortent ; toute autre forme est un refus (rien n'est imprimé de la réponse)."""
    if not isinstance(rj, dict) or rj.get("success") is not True:
        raise Refus("le loueur refuse la copie (réponse non imprimée ; relancer avec la console du loueur pour le motif)")
    addr, port = rj.get("src_addr"), rj.get("src_port")
    if not (isinstance(addr, str) and _ADDR.fullmatch(addr)):
        raise Refus("adresse de copie absente ou illisible")
    try:
        port = int(port)
    except (TypeError, ValueError):
        raise Refus("port de copie absent ou illisible") from None
    if not 1 <= port <= 65535:
        raise Refus("port de copie hors de 1 à 65535")
    return addr, port


def commande_rsync(addr: str, port: int, ident: str, source: str, dest: str) -> str:
    """Forme du client du loueur (`vastai_kaalia@ADRESSE::C.<ID>/<chemin source>`), sans compression (activations en
    demi-précision : peu compressibles) et avec reprise (`--partial`) ; aucune liste de noms à l'écran."""
    ssh = f"ssh -p {port} -o StrictHostKeyChecking=accept-new -o ServerAliveInterval=30"
    return (f"mkdir -p {shlex.quote(dest)} && rsync -a --partial --info=progress2,stats2 -e {shlex.quote(ssh)} "
            f"{shlex.quote(f'vastai_kaalia@{addr}::C.{ident}/{source}')} {shlex.quote(dest)}")


def principal(argv: list[str], client=None) -> str:
    if len(argv) != 3:
        raise Refus("usage : demande_rsync_vast_v1.py ID RUN_ID MONTAGE")
    ident, run_id, montage = argv
    source, dest = chemins(ident, run_id, montage, os.environ.get("SONDE") == "1")
    if client is None:
        if not os.environ.get("VAST_API_KEY"):
            raise Refus("VAST_API_KEY absente (par le nom)")
        from vastai.api.client import VastClient
        client = VastClient(api_key=os.environ["VAST_API_KEY"], client_type="cli")
    from vastai.api import storage
    try:
        rj = storage.copy(client, src_id=f"C.{ident}", dst_id="local", src_path=source, dst_path=dest)
    except Exception as e:   # noqa: BLE001 — le motif seul, sans la réponse
        raise Refus(f"requête refusée ({type(e).__name__})") from None
    addr, port = reduire_reponse(rj)
    return (f"adresse {addr}, port {port} (instance {ident}) ; à jouer SUR LE SERVEUR DE TRANSFERT, sous ssh -A depuis "
            f"le poste :\n{commande_rsync(addr, port, ident, source, dest)}")


if __name__ == "__main__":
    try:
        print(principal(sys.argv[1:]))
    except Refus as e:
        print(f"DEMANDE REFUS : {e}", file=sys.stderr)
        sys.exit(2)
