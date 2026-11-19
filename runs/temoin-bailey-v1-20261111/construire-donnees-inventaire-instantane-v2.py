"""Construit le corps de création du serveur d'INVENTAIRE PAR INSTANTANÉ d'un poste Hetzner du témoin de Bailey, v2 (R12 ;
la v1 reste telle quelle : son constructeur refusait toujours, le motif « @@ » restant dans le script rempli). Mot de Lazar
du 19 novembre 2026 : « avant toute destruction, inventaire et versement scellé de tout ce qui reste sur la machine ».
Les données de démarrage ne portent aucun secret.

Usage : construire-donnees-inventaire-instantane-v2.py <cible> <identifiant de l'instantané> <heure d'arrêt, epoch>
        <dossier de sortie, neuf, hors du dépôt>
Gardes : cible en lettres minuscules, chiffres et tirets, de 3 à 38 caractères (nom du serveur au plus 63) ; instantané
entier ; heure sur 10 chiffres, postérieure au 17 novembre 2026 et au plus égale à maintenant ; empreinte du script
égale à son compagnon (`scellement.verifier`) ; aucun « @@ » après remplissage ; script rempli d'au plus 32 Kio ; dossier
de sortie neuf (R12). Écrit le corps JSON et imprime l'empreinte du script rempli : la marque du serveur doit porter la
même (`script_sha256`). La réponse de création porte un `root_password` (aucune clé ssh) : ne jamais l'imprimer."""
import hashlib
import json
import re
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "inventaire-instantane-v2.sh"


def main() -> int:
    if len(sys.argv) != 5:
        print(__doc__, file=sys.stderr)
        return 2
    cible, image, heure, dossier = sys.argv[1], sys.argv[2], sys.argv[3], Path(sys.argv[4])
    if not re.fullmatch(r"[a-z0-9-]{3,38}", cible) or not re.fullmatch(r"[0-9]{1,12}", image):
        print("cible ou instantané mal formés : rien n'est construit", file=sys.stderr)
        return 2
    if not re.fullmatch(r"[0-9]{10}", heure) or not (1794873600 <= int(heure) <= int(time.time())):
        print("heure d'arrêt mal formée ou invraisemblable : rien n'est construit", file=sys.stderr)
        return 2
    comp = (ICI / "inventaire-instantane-v2.sh.sha256").read_text(encoding="utf-8").split()
    octets = SCRIPT.read_bytes()
    if len(comp) != 2 or comp[1] != SCRIPT.name or hashlib.sha256(octets).hexdigest() != comp[0]:
        print("compagnon du script absent, mal formé ou différent : rien n'est construit", file=sys.stderr)
        return 2
    texte = octets.decode("utf-8")
    if texte.count("@@CIBLE@@") != 1 or texte.count("@@HEURE@@") != 1:
        print("blocs à remplir absents ou en double : rien n'est construit", file=sys.stderr)
        return 2
    texte = texte.replace("@@CIBLE@@", cible).replace("@@HEURE@@", heure)
    if "@@" in texte or len(texte.encode()) > 32 * 1024:
        print("bloc non rempli ou script trop long : rien n'est construit", file=sys.stderr)
        return 2
    if dossier.exists():
        print("dossier de sortie déjà présent (R12) : rien n'est construit", file=sys.stderr)
        return 2
    dossier.mkdir(mode=0o700, parents=True)
    nom = f"inventaire-instantane-{cible}-v2"
    corps = {"name": nom, "server_type": "cx23", "location": "fsn1", "image": int(image), "start_after_create": True,
             "user_data": texte, "labels": {"programme": "controle-ia", "poste": nom}}
    sortie = dossier / "creation-hetzner-v2.json"
    sortie.write_text(json.dumps(corps), encoding="utf-8")
    print(f"construit : {sortie} ; serveur {nom} ; script rempli {hashlib.sha256(texte.encode()).hexdigest()} ; "
          f"script sans remplissage {comp[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
