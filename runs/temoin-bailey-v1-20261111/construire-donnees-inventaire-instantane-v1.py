"""Construit le corps de création du serveur d'INVENTAIRE PAR INSTANTANÉ d'un poste Hetzner du témoin de Bailey, v1 (mot
de Lazar du 19 novembre 2026 : « avant toute destruction, inventaire et versement scellé de tout ce qui reste sur la
machine »). Les données de démarrage ne portent aucun secret : le serveur pousse avec la clé de déploiement présente sur
le disque copié du poste.

Usage : construire-donnees-inventaire-instantane-v1.py <cible> <identifiant de l'instantané> <heure d'extinction, epoch>
        <dossier de sortie, neuf, hors du dépôt>
Vérifie l'empreinte de `inventaire-instantane-v1.sh` contre son compagnon ; remplit `@@CIBLE@@` (lettres, chiffres,
tirets) et `@@HEURE@@` (entier) ; refuse s'il reste un `@@` ou si le résultat dépasse 32 Kio ; écrit le corps JSON
(`image` : l'instantané ; nom `inventaire-instantane-<cible>-v1`) et imprime son empreinte et celle du script rempli."""
import hashlib
import json
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "inventaire-instantane-v1.sh"


def main() -> int:
    cible, image, heure, dossier = sys.argv[1], sys.argv[2], sys.argv[3], Path(sys.argv[4])
    if not re.fullmatch(r"[a-z0-9-]{3,40}", cible) or not image.isdigit() or not heure.isdigit():
        print("cible, instantané ou heure mal formés : rien n'est construit", file=sys.stderr)
        return 2
    attendu = (ICI / "inventaire-instantane-v1.sh.sha256").read_text(encoding="utf-8").split()[0]
    octets = SCRIPT.read_bytes()
    if hashlib.sha256(octets).hexdigest() != attendu:
        print("empreinte du script différente de son compagnon : rien n'est construit", file=sys.stderr)
        return 2
    texte = octets.decode("utf-8").replace("@@CIBLE@@", cible).replace("@@HEURE@@", heure)
    if "@@" in texte or len(texte.encode()) > 32 * 1024:
        print("bloc non rempli ou script trop long : rien n'est construit", file=sys.stderr)
        return 2
    if dossier.exists():
        print("dossier de sortie déjà présent (R12) : rien n'est construit", file=sys.stderr)
        return 2
    dossier.mkdir(mode=0o700, parents=True)
    corps = {"name": f"inventaire-instantane-{cible}-v1", "server_type": "cx23", "location": "fsn1", "image": int(image),
             "start_after_create": True, "user_data": texte,
             "labels": {"programme": "controle-ia", "poste": f"inventaire-instantane-{cible}-v1"}}
    sortie = dossier / "creation-hetzner-v1.json"
    sortie.write_text(json.dumps(corps), encoding="utf-8")
    print(f"construit : {sortie} ; script rempli {hashlib.sha256(texte.encode()).hexdigest()} ; "
          f"script sans remplissage {attendu}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
