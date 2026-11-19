"""Mise à l'abri générique de restes d'exécution (règle R-3661 : récupérer ce qui est récupérable).

Copie (jamais déplacement) des fichiers de chaque source vers un dossier d'archive neuf du dépôt, et inventaire par
chemin, taille et empreinte SHA-256. Aucun contenu n'est lu ni imprimé : copie d'octets et empreintes seulement.
Les fichiers d'outillage sans réponse de modèle (cache de greffons, sauvegardes de configuration, journaux de npm,
configuration de l'outil) sont inventoriés mais non copiés, avec leur motif.

Usage : python -B scripts/archiver_restes_v2.py DESTINATION ETIQUETTE=SOURCE [ETIQUETTE=SOURCE …]
(SOURCE : un dossier ou un fichier).
"""
import hashlib
import json
import os
import shutil
import sys

NON_COPIES = [
    (".claude/plugins/", "cache du catalogue de greffons de l'outil"),
    (".claude/backups/", "sauvegardes de la configuration de l'outil"),
    (".claude.json", "configuration de l'outil (identifiants de compte local possibles)"),
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
        if rel == prefixe.rstrip("/") or rel.startswith(prefixe) or ("/" + prefixe) in ("/" + rel):
            return motif
    return None


def fichiers_de(source):
    if os.path.isfile(source):
        yield source, os.path.basename(source)
        return
    for racine, dossiers, fichiers in os.walk(source):
        dossiers.sort()
        for nom in sorted(fichiers):
            chemin = os.path.join(racine, nom)
            if os.path.islink(chemin):
                continue
            yield chemin, os.path.relpath(chemin, source)


def main(destination, paires):
    if os.path.exists(destination):
        raise SystemExit(f"{destination} existe déjà : arrêt (R12)")
    sources = []
    for p in paires:
        etiquette, _, source = p.partition("=")
        if not etiquette or not source or not os.path.exists(source):
            raise SystemExit(f"paire invalide ou source absente : {p}")
        sources.append((etiquette, source))
    lignes = []
    for etiquette, source in sources:
        for chemin, rel in fichiers_de(source):
            somme = empreinte(chemin)
            entree = {"etiquette": etiquette, "source": chemin, "relatif": rel,
                      "octets": os.path.getsize(chemin), "sha256": somme}
            motif = motif_non_copie(rel)
            if motif:
                entree.update(copie=False, motif=motif)
            else:
                cible = os.path.join(destination, etiquette, rel)
                os.makedirs(os.path.dirname(cible), exist_ok=True)
                shutil.copy2(chemin, cible)
                if empreinte(cible) != somme:
                    raise SystemExit(f"copie infidèle : {chemin}")
                entree.update(copie=True, archive=os.path.join(etiquette, rel))
            lignes.append(entree)
    os.makedirs(destination, exist_ok=True)
    with open(os.path.join(destination, "inventaire-v1.json"), "w", encoding="utf-8") as f:
        json.dump({"sources": dict(sources), "fichiers": lignes}, f, ensure_ascii=False, indent=1)
    copies = [x for x in lignes if x["copie"]]
    print(f"fichiers={len(lignes)} copies={len(copies)} octets_copies={sum(x['octets'] for x in copies)} "
          f"non_copies={len(lignes) - len(copies)} plus_gros={max((x['octets'] for x in copies), default=0)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
