"""r1 — inventaire des deux archives fermées, sans extraction ni exécution.

Usage : python3 -I r1_inventaire_archives.py ARCHIVE_M ARCHIVE_S SORTIE
Vérifie l'empreinte de chaque archive contre la valeur attendue, liste les membres
(type, taille, nom), signale liens, fichiers spéciaux, chemins absolus ou remontants,
et les noms interdits par la consigne (P3-consignes-v1.md, textes-actions-*, dossiers
donnees/, runs/, diag/), sans rien ouvrir d'autre que le flux de l'archive.
"""
import hashlib
import sys
import tarfile

ATTENDU = {
    "M": "a7bd419eb7e7d15c2edaf3985328b4847851c6f334f79369f29d84cb37dbe368",
    "S": "323cb0ddf0bc98ff2851bafd39d3ea78bc371504f627044f7bb6691b90a81df6",
}


def sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def main():
    arch = {"M": sys.argv[1], "S": sys.argv[2]}
    sortie = sys.argv[3]
    lignes = []
    for course, chemin in arch.items():
        e = sha256(chemin)
        lignes.append(f"## {course} {chemin}")
        lignes.append(f"sha256 {e} attendu {ATTENDU[course]} conforme {e == ATTENDU[course]}")
        if e != ATTENDU[course]:
            lignes.append("ARRET : empreinte non conforme")
            continue
        n_fic = n_dos = 0
        alertes = []
        interdits = []
        racines = {}
        with tarfile.open(chemin, "r:gz") as t:
            for m in t.getmembers():
                nom = m.name
                base = nom.rstrip("/").split("/")[-1]
                parties = nom.split("/")
                if m.isfile():
                    n_fic += 1
                elif m.isdir():
                    n_dos += 1
                else:
                    alertes.append(f"type non ordinaire : {nom} ({m.type!r})")
                if nom.startswith("/") or ".." in parties:
                    alertes.append(f"chemin absolu ou remontant : {nom}")
                if base == "P3-consignes-v1.md" or base.startswith("textes-actions-") or any(
                    p in ("donnees", "runs", "diag") for p in parties[:-1]
                ):
                    interdits.append(nom)
                r = "/".join(parties[:2])
                racines[r] = racines.get(r, 0) + 1
        lignes.append(f"fichiers {n_fic} dossiers {n_dos}")
        lignes.append(f"alertes {len(alertes)}")
        lignes.extend("  " + a for a in alertes)
        lignes.append(f"noms interdits par la consigne {len(interdits)}")
        lignes.extend("  " + a for a in interdits)
        lignes.append("membres par racine (deux premiers niveaux) :")
        for r in sorted(racines):
            lignes.append(f"  {racines[r]:5d}  {r}")
    with open(sortie, "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print("\n".join(lignes))


if __name__ == "__main__":
    main()
