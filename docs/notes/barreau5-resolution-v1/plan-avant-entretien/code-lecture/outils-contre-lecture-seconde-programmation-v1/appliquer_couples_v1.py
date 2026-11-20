"""Applique les couples de `couples_contre_lecture_v1.py` à des copies, dans `/dev/shm`, sans toucher le dépôt.

Pour chaque fichier visé : lecture du fichier du dépôt, vérification de son empreinte, application des couples dans
l'ordre, chacun exigé une seule fois dans le texte en cours ; écriture de la copie corrigée sous
`/dev/shm/b5f-contre-lecture-seconde-v1/` ; empreintes avant et après imprimées. Refus au premier couple introuvable ou
trouvé plusieurs fois.

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python -B <ce fichier>
"""
from __future__ import annotations

import hashlib
import importlib.util
import os
import sys

RACINE = "/home/user/controle-ia-travail"
ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER = "/dev/shm/b5f-contre-lecture-seconde-v1"
EMPREINTES = {
    "src/controle_ia/barreau5_familles/seconde_programmation_v2.py":
        "29c71ef98d86dd2ebd19d4cfd2c89f6b893e105c2f8444a4288f7abcb7c55af7",
    "tests/test_barreau5_familles_seconde_programmation_v2.py":
        "c0e1b3fcebfdca90654942e8d2aab79bbe18787a1de020a0b8b2b1afd08cc0ac",
    "src/controle_ia/barreau5_familles/lecture_v1.py":
        "d877d2dea0ddd4707324139aaa63e4bdae1f89a2aa23bea145adf4175a62c0df",
}


def main() -> int:
    spec = importlib.util.spec_from_file_location("couples_contre_lecture_v1", os.path.join(ICI, "couples_contre_lecture_v1.py"))
    couples = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(couples)
    os.makedirs(DOSSIER, exist_ok=False)
    for fichier, attendue in EMPREINTES.items():
        with open(os.path.join(RACINE, fichier), "rb") as f:
            octets = f.read()
        avant = hashlib.sha256(octets).hexdigest()
        if avant != attendue:
            print(f"refus : {fichier} a l'empreinte {avant}, {attendue} attendue")
            return 1
        texte = octets.decode("utf-8")
        for nom, cible, ancien, neuf in couples.COUPLES:
            if cible != fichier:
                continue
            n = texte.count(ancien)
            if n != 1:
                print(f"refus : couple « {nom} » : « avant » trouvé {n} fois dans {fichier}")
                return 1
            texte = texte.replace(ancien, neuf)
            print(f"appliqué : {nom}")
        copie = os.path.join(DOSSIER, os.path.basename(fichier))
        with open(copie, "w", encoding="utf-8") as f:
            f.write(texte)
        print(f"{fichier} : {avant} -> {hashlib.sha256(texte.encode('utf-8')).hexdigest()} ({copie})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
