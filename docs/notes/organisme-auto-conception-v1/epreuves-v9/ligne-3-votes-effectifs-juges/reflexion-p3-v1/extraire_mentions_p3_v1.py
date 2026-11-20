"""Extraction des mentions utiles à la lecture de P3 dans les textes d'avant mesure — v1.

Lit seulement les fichiers passés en arguments (chemins complets), jamais un dossier. Bibliothèque standard seule.
Aucun tirage, aucune mesure de l'étage 1 lue. Rend un JSON : par fichier, son empreinte, la ligne de P3 (numéro,
empreinte de la ligne, texte), et, pour chaque terme, les numéros de ligne et un extrait court autour du terme.

Usage : python3 extraire_mentions_p3_v1.py SORTIE.json FICHIER [FICHIER ...]
"""
import hashlib
import json
import sys

TERMES = (
    "majorité fixe",
    "majorité stricte",
    "échangeable",
    "agrégation étalonnée",
    "poids égaux",
    "poids uniformes",
    "agrégation uniforme",
    "H-agrégation",
    "règle fixe",
    "P3",
)
MARGE = 170


def sha256_octets(b):
    return hashlib.sha256(b).hexdigest()


def extraits(ligne, terme):
    sortie = []
    debut = 0
    bas = ligne.lower()
    t = terme.lower()
    while True:
        i = bas.find(t, debut)
        if i < 0:
            break
        a = max(0, i - MARGE)
        z = min(len(ligne), i + len(terme) + MARGE)
        sortie.append(("…" if a > 0 else "") + ligne[a:z] + ("…" if z < len(ligne) else ""))
        debut = i + len(t)
    return sortie


def lire(chemin):
    with open(chemin, "rb") as f:
        brut = f.read()
    lignes = brut.decode("utf-8").split("\n")
    fiche = {"chemin": chemin, "sha256": sha256_octets(brut), "lignes": len(lignes), "ligne_P3": None, "mentions": {}}
    for n, ligne in enumerate(lignes, start=1):
        if ligne.startswith("- P3 (H-agrégation"):
            fiche["ligne_P3"] = {"numero": n, "sha256_de_la_ligne": sha256_octets(ligne.encode("utf-8")), "texte": ligne}
        for terme in TERMES:
            for e in extraits(ligne, terme):
                fiche["mentions"].setdefault(terme, []).append({"ligne": n, "extrait": e})
    return fiche


def main(argv):
    if len(argv) < 3:
        raise SystemExit("usage : python3 extraire_mentions_p3_v1.py SORTIE.json FICHIER [FICHIER ...]")
    sortie, fichiers = argv[1], argv[2:]
    fiches = [lire(c) for c in fichiers]
    lignes_p3 = {f["chemin"].rsplit("/", 1)[-1]: (f["ligne_P3"] or {}).get("sha256_de_la_ligne") for f in fiches}
    valeurs = {v for v in lignes_p3.values() if v is not None}
    resume = {
        "empreinte_de_la_ligne_P3_par_fichier": lignes_p3,
        "ligne_P3_identique_dans_tous_les_fichiers_qui_la_portent": len(valeurs) == 1,
        "comptes_de_mentions_par_fichier": {
            f["chemin"].rsplit("/", 1)[-1]: {t: len(f["mentions"].get(t, [])) for t in TERMES} for f in fiches
        },
    }
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump({"version": "extraire-mentions-p3-v1", "termes": list(TERMES), "resume": resume, "fichiers": fiches},
                  f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print(json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv)
