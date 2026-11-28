"""Cherche des passages dans la v5, retours à la ligne et retraits ramenés à un espace.

Usage : python3 -B -I trouver_v1.py V5 FICHIER_JSON
FICHIER_JSON : liste d'objets {"id": ..., "ancien": ..., "attendu": n (facultatif, 1 par
défaut)}. Pour chacun, imprime le nombre d'occurrences exactes dans le texte normalisé.
Code de sortie 1 si un compte diffère de l'attendu. Aucune écriture.
"""
import hashlib
import json
import re
import sys


def normaliser(texte):
    return re.sub(r"\s*\n\s*", " ", texte)


def main():
    chemin_v5, chemin_json = sys.argv[1], sys.argv[2]
    brut = open(chemin_v5, "rb").read()
    print("v5 sha256", hashlib.sha256(brut).hexdigest())
    texte = normaliser(brut.decode("utf-8"))
    cas = json.load(open(chemin_json, encoding="utf-8"))
    mauvais = 0
    for c in cas:
        attendu = c.get("attendu", 1)
        n = texte.count(c["ancien"])
        statut = "OK" if n == attendu else "ECHEC"
        if n != attendu:
            mauvais += 1
        print(f"{statut} {c['id']} occurrences={n} attendu={attendu}")
    print(f"total={len(cas)} echecs={mauvais}")
    sys.exit(1 if mauvais else 0)


if __name__ == "__main__":
    main()
