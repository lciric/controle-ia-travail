"""Mise à l'abri des restes des deux courses d'auto-conception (v4 du 18, v6 du 19 novembre 2026).

Copie (jamais déplacement) des fichiers survivants vers un dossier d'archive du dépôt, et inventaire
par chemin, taille et empreinte SHA-256. Aucun contenu n'est lu ni imprimé : le programme copie des
octets et calcule des empreintes. Les fichiers d'outillage sans rapport avec les réponses (caches
de greffons, sauvegardes de configuration, journaux de npm) sont inventoriés mais non copiés, avec
leur motif.

Usage : python -B scripts/archiver_courses_auto_conception_v4_v6_v1.py DESTINATION
"""
import hashlib
import json
import os
import shutil
import sys

SOURCES = [
    ("course-v4/sortie-orchestrateur",
     "/home/user/sorties-course-auto-conception-v4/20261118-171908-course-auto-conception-v4"),
    ("course-v4/execution-relais-et-epreuve", "/home/user/execution-auto-conception-v2d"),
    ("course-v6/sortie-orchestrateur",
     "/home/user/sorties-course-auto-conception-v6/20261119-001004-course-auto-conception-v6"),
    ("course-v6/execution-relais-et-epreuve", "/home/user/execution-auto-conception-v2f"),
]

# Motifs de non-copie (chemins relatifs à la source) : outillage, sans réponse de modèle.
NON_COPIES = [
    (".claude/plugins/", "cache du catalogue de greffons de l'outil, sans rapport avec la course"),
    (".claude/backups/", "sauvegardes de la configuration de l'outil, sans réponse de modèle"),
    (".claude.json", "configuration de l'outil (identifiants de compte local possibles), sans réponse de modèle"),
    (".npm/", "journaux de npm de l'outil"),
    (".claude/.last-cleanup", "horodatage de l'outil"),
]


def empreinte(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def motif_non_copie(rel):
    for prefixe, motif in NON_COPIES:
        if rel == prefixe or rel.startswith(prefixe) or ("/" + prefixe) in ("/" + rel):
            return motif
    return None


def main(destination):
    if os.path.exists(destination):
        raise SystemExit(f"{destination} existe déjà : arrêt (R12, on n'écrase jamais)")
    lignes = []
    for etiquette, source in SOURCES:
        if not os.path.isdir(source):
            raise SystemExit(f"source absente : {source}")
        for racine, dossiers, fichiers in os.walk(source):
            dossiers.sort()
            for nom in sorted(fichiers):
                chemin = os.path.join(racine, nom)
                rel = os.path.relpath(chemin, source)
                taille = os.path.getsize(chemin)
                somme = empreinte(chemin)
                motif = motif_non_copie(rel)
                entree = {"etiquette": etiquette, "source": chemin, "relatif": rel,
                          "octets": taille, "sha256": somme}
                if motif:
                    entree["copie"] = False
                    entree["motif"] = motif
                else:
                    cible = os.path.join(destination, etiquette, rel)
                    os.makedirs(os.path.dirname(cible), exist_ok=True)
                    shutil.copy2(chemin, cible)
                    if empreinte(cible) != somme:
                        raise SystemExit(f"copie infidèle : {chemin}")
                    entree["copie"] = True
                    entree["archive"] = os.path.join(etiquette, rel)
                lignes.append(entree)
    os.makedirs(destination, exist_ok=True)
    with open(os.path.join(destination, "inventaire-v1.json"), "w", encoding="utf-8") as f:
        json.dump({"sources": [s for _, s in SOURCES], "fichiers": lignes}, f, ensure_ascii=False, indent=1)
    copies = [x for x in lignes if x["copie"]]
    print(f"fichiers={len(lignes)} copies={len(copies)} octets_copies={sum(x['octets'] for x in copies)} "
          f"non_copies={len(lignes) - len(copies)} octets_non_copies={sum(x['octets'] for x in lignes if not x['copie'])}")
    print(f"plus_gros={max(x['octets'] for x in copies)}")


if __name__ == "__main__":
    main(sys.argv[1])
