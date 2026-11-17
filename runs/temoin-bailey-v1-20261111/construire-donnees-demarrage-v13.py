"""Construit les données de démarrage (cloud-init) du poste Hetzner du témoin de Bailey, v13 (R12 ; v1 à v12 restent telles
quelles). v13 = v12 dont seuls changent le script assemblé (`poste-hetzner-v13.sh`) et le nom du serveur.

Lit `poste-hetzner-v1.sh`, y remplace les blocs de secrets par : la clé privée de déploiement GitHub
(`~/.ssh/deploiement_poste_bailey`), la clé `ssh` de session enregistrée sur Vast (`~/.ssh/id_ed25519`, identifiant
1864483), et VAST_API_KEY et HF_TOKEN lus dans l'environnement. Écrit le résultat dans un fichier de droits 600 hors du
dépôt (argument), puis le corps JSON de la création (même dossier). **N'imprime aucun secret** : seulement la taille,
l'empreinte du script sans secrets et la liste des blocs remplacés. Refuse si un secret manque, si un délimiteur de
bloc apparaît dans un secret, ou si le résultat dépasse 32 Kio (limite de Hetzner).
"""
import json
import os
import sys
from hashlib import sha256
from pathlib import Path

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "poste-hetzner-v13.sh"


def main() -> int:
    dossier = Path(sys.argv[1])
    dossier.mkdir(mode=0o700, parents=True, exist_ok=True)
    texte = SCRIPT.read_text(encoding="utf-8")
    secrets = {
        "@@CLE_DEPLOIEMENT@@": Path.home().joinpath(".ssh/deploiement_poste_bailey").read_text().strip(),
        "@@CLE_VAST@@": Path.home().joinpath(".ssh/id_ed25519").read_text().strip(),
    }
    vast, hf = os.environ.get("VAST_API_KEY", ""), os.environ.get("HF_TOKEN", "")
    if not vast or not hf:
        print("VAST_API_KEY ou HF_TOKEN absent : rien n'est construit", file=sys.stderr)
        return 2
    for v in (vast, hf):
        if any(c in v for c in "'\"\n$`\\ "):
            print("caractère inattendu dans une clé : rien n'est construit", file=sys.stderr)
            return 2
    secrets["@@SECRETS@@"] = f"VAST_API_KEY={vast}\nHF_TOKEN={hf}"
    for bloc, valeur in secrets.items():
        if texte.count(bloc) != 1 or "@@" in valeur:
            print(f"bloc {bloc} absent, en double, ou délimiteur dans la valeur : rien n'est construit", file=sys.stderr)
            return 2
        texte = texte.replace(bloc, valeur)
    if len(texte.encode()) > 32 * 1024:
        print("données de démarrage au-delà de 32 Kio : rien n'est construit", file=sys.stderr)
        return 2
    corps = {"name": "poste-temoin-bailey-v13", "server_type": "cx23", "location": "fsn1", "image": "debian-12",
             "start_after_create": True, "user_data": texte,
             "labels": {"programme": "controle-ia", "poste": "temoin-bailey-v13"}}
    sortie = dossier / "creation-hetzner-v1.json"
    fd = os.open(sortie, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(corps, f)
    print(f"construit : {sortie} ({sortie.stat().st_size} octets) ; script sans secrets "
          f"{sha256(SCRIPT.read_bytes()).hexdigest()} ; blocs remplacés : {sorted(secrets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
