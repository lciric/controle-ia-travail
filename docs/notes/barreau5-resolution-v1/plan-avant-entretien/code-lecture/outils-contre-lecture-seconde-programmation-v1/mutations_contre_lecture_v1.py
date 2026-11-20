"""Cinq mutations du contre-lecteur sur la seconde programmation (barreau 5), module v2 `29c71ef9…`, essais `c0e1b3fc…`.

Même mécanique que l'outil du programmeur : une copie mutée en un seul endroit, écrite dans `/dev/shm`, désignée aux
essais par `B5F_SECONDE_MODULE` ; « attrapée » si pytest sort en code 1. Le dépôt n'est pas modifié. Aucun aléa.

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python -B <ce fichier> <journal .json>
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys

RACINE = "/home/user/controle-ia-travail"
MODULE = RACINE + "/src/controle_ia/barreau5_familles/seconde_programmation_v2.py"
ESSAIS = RACINE + "/tests/test_barreau5_familles_seconde_programmation_v2.py"
DOSSIER = "/dev/shm/b5f-contre-lecture-mutations-v1"
MUTANT = "/dev/shm/b5f-contre-lecture-mutations-v1/mutant.py"

MUTATIONS = [
    ("X1", "        if familles_e3 is not None and familles_e3 != k_e3:", "        if False:",
     "le compte de familles de E3 donné doit égaler le nombre de différences"),
    ("X2", '"positifs": mien["positives"],', '"positifs": _lire(resultat, "positifs", e),',
     "comparateur : « signes seuls » (positifs) comparés"),
    ("X3", '"w_plus": mien["w_plus"],', '"w_plus": _lire(resultat, "w_plus", e),', "comparateur : W⁺ comparé"),
    ("X4", 'manquent = [e for e in ("E2a", "E2b", "E1") if verdicts[e] != SEPARE]',
     'manquent = [e for e in ("E2b", "E2a", "E1") if verdicts[e] != SEPARE]', "D : ordre des motifs, E2a avant E2b"),
    ("X5", "    if phrase_niveau is not attendue and phrase_niveau != attendue:", "    if False:",
     "comparateur : « au niveau de 95 % » présent si, et seulement si, le niveau est 95"),
]


def jouer(environnement: dict) -> int:
    commande = [sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", ESSAIS]
    return subprocess.run(commande, cwd=RACINE, env=environnement, capture_output=True, text=True).returncode


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print(f"refus : {journal} existe déjà (on n'écrase jamais)")
        return 2
    with open(MODULE, encoding="utf-8") as f:
        source = f.read()
    environnement = dict(os.environ)
    lignes = []
    os.makedirs(DOSSIER, exist_ok=False)
    try:
        with open(MUTANT, "w", encoding="utf-8") as f:
            f.write(source)
        environnement["B5F_SECONDE_MODULE"] = MUTANT
        sain = jouer(environnement)
        for nom, origine, mute, regle in MUTATIONS:
            n = source.count(origine)
            if n != 1:
                lignes.append({"nom": nom, "regle": regle, "etat": f"inapplicable ({n} occurrences)"})
                continue
            with open(MUTANT, "w", encoding="utf-8") as f:
                f.write(source.replace(origine, mute))
            code = jouer(environnement)
            lignes.append({"nom": nom, "regle": regle, "etat": "attrapée" if code == 1 else f"non attrapée (code {code})"})
    finally:
        if os.path.exists("/dev/shm/b5f-contre-lecture-mutations-v1/mutant.py"):
            os.remove("/dev/shm/b5f-contre-lecture-mutations-v1/mutant.py")
        os.rmdir("/dev/shm/b5f-contre-lecture-mutations-v1")
    rendu = {"module_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(), "cas_sain_code_de_sortie": sain,
             "mutations": len(lignes), "attrapees": sum(1 for x in lignes if x["etat"] == "attrapée"), "lignes": lignes}
    with open(journal, "w", encoding="utf-8") as f:
        json.dump(rendu, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps(rendu, ensure_ascii=False))
    return 0 if sain == 0 and rendu["attrapees"] == len(lignes) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
