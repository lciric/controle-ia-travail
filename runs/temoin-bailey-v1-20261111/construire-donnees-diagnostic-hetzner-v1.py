"""Construit les données de démarrage du serveur Hetzner de diagnostic (gabarit `diagnostic-hetzner-v1.sh`).
Écrit le script rempli à `--sortie` (hors du dépôt : il contient deux clés privées jetables). Refuse tout jeton restant."""
import argparse
import re
from pathlib import Path

ICI = Path(__file__).resolve().parent


def construire(cle_depot: str, cle_vast: str, hote: str, port: int, relais_hote: str, relais_port: int) -> str:
    t = (ICI / "diagnostic-hetzner-v1.sh").read_text(encoding="utf-8")
    for nom, cle in (("cle_depot", cle_depot), ("cle_vast", cle_vast)):
        if "PRIVATE KEY" not in cle or "@@" in cle:
            raise SystemExit(f"{nom} n'est pas une clé privée : rien n'est écrit")
    if not re.fullmatch(r"[A-Za-z0-9.-]+", hote) or not re.fullmatch(r"[A-Za-z0-9.-]+", relais_hote):
        raise SystemExit("hôte invalide : rien n'est écrit")
    t = t.replace("@@CLE_DEPLOIEMENT@@", cle_depot.strip()).replace("@@CLE_VAST@@", cle_vast.strip())
    t = t.replace("@@HOTE@@", hote).replace("@@PORT@@", str(int(port)))
    t = t.replace("@@RELAIS_HOTE@@", relais_hote).replace("@@RELAIS_PORT@@", str(int(relais_port)))
    restants = sorted(set(re.findall(r"@@[A-Z_]+@@", t)) - {"@@CLE_DEPLOIEMENT_FIN@@", "@@CLE_VAST_FIN@@"})
    if restants:
        raise SystemExit(f"jetons non remplacés {restants} : rien n'est écrit")
    if len(t.encode()) > 32 * 1024:
        raise SystemExit("données de démarrage > 32 Kio (limite Hetzner) : rien n'est écrit")
    return t


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    for a in ("--cle-depot", "--cle-vast", "--hote", "--relais-hote", "--sortie"):
        p.add_argument(a, required=True)
    p.add_argument("--port", type=int, required=True)
    p.add_argument("--relais-port", type=int, required=True)
    a = p.parse_args()
    s = Path(a.sortie)
    if s.exists():
        raise SystemExit("sortie déjà présente (R12) : rien n'est écrit")
    s.write_text(construire(Path(a.cle_depot).read_text(), Path(a.cle_vast).read_text(), a.hote, a.port,
                            a.relais_hote, a.relais_port), encoding="utf-8")
    s.chmod(0o600)
    print(f"écrit {s}")
