"""Bâtit un kit de contre-lecture : chaque fichier EN ENTIER, précédé de son chemin, de sa taille et de son empreinte
SHA-256, puis vérifie, en relisant le kit, que chaque contenu inclus a bien l'empreinte annoncée (aucune troncature).

Classe C (outil de la mère, 28 novembre 2026). Bibliothèque standard seule. Garde de lecture : refuse tout fichier
d'activations ou de poids et tout chemin gardé.

    python batir_kit_v1.py SORTIE TITRE ENTREE [ENTREE…]
ENTREE : « chemin » (arbre de travail), « commit:chemin » (lu par git show), ou « =nom:chemin_local » (fichier
d'extrait déjà écrit, présenté sous « nom »).
"""
import hashlib, re, subprocess, sys, pathlib

GARDES = (re.compile(r"\.(npz|npy|safetensors)$"), re.compile(r"consignes-privees"), re.compile(r"ii-b-saboteur-budget"),
          re.compile(r"P3-consignes"), re.compile(r"src/controle_ia/iib/"), re.compile(r"reserve-pour-lazar"),
          re.compile(r"clef-de-la-mere"))
DEBUT = "===== DÉBUT DU FICHIER "
FIN = "===== FIN DU FICHIER "


def lire(entree):
    if entree.startswith("="):
        nom, chemin = entree[1:].split(":", 1)
        return nom, pathlib.Path(chemin).read_bytes()
    for g in GARDES:
        if g.search(entree):
            raise SystemExit(f"garde de lecture : {entree} refusé")
    if re.match(r"^[0-9a-f]{7,40}:", entree):
        return entree, subprocess.run(["git", "show", entree], check=True, capture_output=True).stdout
    return entree, pathlib.Path(entree).read_bytes()


def main():
    sortie, titre, entrees = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3:]
    morceaux, table = [], []
    for e in entrees:
        nom, octets = lire(e)
        h = hashlib.sha256(octets).hexdigest()
        table.append((nom, len(octets), h))
        morceaux.append((nom, octets, h))
    tete = [f"# {titre}", "",
            "Chaque fichier est inclus EN ENTIER entre deux marqueurs ; la ligne de début donne sa taille en octets et son "
            "empreinte SHA-256. Un lecteur peut vérifier qu'aucun n'est tronqué.", "",
            "| n° | fichier | octets | SHA-256 |", "|---|---|---|---|"]
    tete += [f"| {i} | `{n}` | {o} | `{h}` |" for i, (n, o, h) in enumerate(table, 1)]
    corps = ("\n".join(tete) + "\n\n").encode("utf-8")
    for nom, octets, h in morceaux:
        corps += f"{DEBUT}{nom} — {len(octets)} octets — sha256 {h} =====\n".encode("utf-8") + octets
        corps += f"\n{FIN}{nom} =====\n\n".encode("utf-8")
    sortie.write_bytes(corps)
    # vérification par relecture
    k = sortie.read_bytes()
    pos, n = 0, 0
    for nom, octets, h in morceaux:
        marque = f"{DEBUT}{nom} — {len(octets)} octets — sha256 {h} =====\n".encode("utf-8")
        i = k.index(marque, pos) + len(marque)
        contenu = k[i:i + len(octets)]
        assert hashlib.sha256(contenu).hexdigest() == h, f"troncature ou altération : {nom}"
        assert k[i + len(octets):].startswith(f"\n{FIN}{nom} =====".encode("utf-8")), f"marqueur de fin manquant : {nom}"
        pos, n = i + len(octets), n + 1
    print(f"{n} fichiers inclus et vérifiés ; {len(k)} octets ; sha256 du kit {hashlib.sha256(k).hexdigest()}")


if __name__ == "__main__":
    main()
