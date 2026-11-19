"""Journal scellé des décisions du banc A, ligne 1 (version 1).

Préenregistrement qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`,
sha256 523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9 (plan d'analyse, « Journal scellé des décisions du
banc »).

Forme : un fichier par course et par classe, compressé (xz, préréglage 6, sans horodatage : deux exécutions rendent les mêmes
octets), une ligne JSON canonique par entrée. Trois sortes de lignes : l'en-tête (première ligne), les objets longs (lois,
textes, issues de jugement), écrits une fois sous leur empreinte, et les décisions. Chaque ligne porte l'empreinte de la
ligne précédente (« precedente » ; la première porte 64 zéros) : une ligne ôtée ou modifiée rompt la chaîne.
Une décision porte : la partie (« tronc » ou « bras=<nom> »), le nom du mécanisme, les empreintes des fichiers de code qui le
portent, ses entrées exactes (en valeurs ; les objets longs par leur clé dans la table du même fichier) et sa sortie.

Bibliothèque standard seule ; aucune connexion.
"""

import lzma
import hashlib
import json
import os

VERSION = "journal-ligne1-v1"
ZERO = "0" * 64


class JournalRompu(RuntimeError):
    """Chaîne d'empreintes rompue, objet dont l'empreinte ne correspond pas à son contenu, ou ligne illisible (garde A16)."""


def canonique(objet):
    """Octets du JSON canonique (clés triées, séparateurs compacts, UTF-8, aucun NaN) : la règle de `outils.json_canonique`."""
    return json.dumps(objet, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def empreinte(objet):
    return hashlib.sha256(canonique(objet)).hexdigest()


class Journal:
    """Écrit un journal ; `fermer()` rend l'empreinte du fichier compressé et écrit son compagnon `.sha256`."""

    def __init__(self, chemin, entete):
        if os.path.exists(chemin):
            raise FileExistsError(f"journal {chemin} déjà présent : on n'écrase jamais (R12)")
        self.chemin = chemin
        self._brut = open(chemin, "wb")
        self._gz = lzma.LZMAFile(self._brut, mode="wb", format=lzma.FORMAT_XZ, preset=6)
        self._precedente = ZERO
        self._vus = set()
        self.nombre_lignes = 0
        self.octets_bruts = 0
        self._ecrire(dict(entete, sorte="entete", version_journal=VERSION))

    def _ecrire(self, ligne):
        ligne = dict(ligne, precedente=self._precedente, n=self.nombre_lignes)
        octets = canonique(ligne)
        self._gz.write(octets + b"\n")
        self._precedente = hashlib.sha256(octets).hexdigest()
        self.nombre_lignes += 1
        self.octets_bruts += len(octets) + 1

    def objet(self, valeur):
        """Écrit l'objet une fois ; rend sa clé (empreinte de son JSON canonique)."""
        cle = empreinte(valeur)
        if cle not in self._vus:
            self._vus.add(cle)
            self._ecrire({"sorte": "objet", "cle": cle, "valeur": valeur})
        return cle

    def decision(self, partie, decision, mecanisme, code, entrees, sortie):
        self._ecrire({"sorte": "decision", "partie": partie, "decision": decision, "mecanisme": mecanisme, "code": code,
                      "entrees": entrees, "sortie": sortie})

    def fermer(self):
        self._gz.close()
        self._brut.close()
        h = hashlib.sha256()
        with open(self.chemin, "rb") as f:
            for bloc in iter(lambda: f.read(1 << 20), b""):
                h.update(bloc)
        sha = h.hexdigest()
        with open(self.chemin + ".sha256", "w", encoding="utf-8") as f:
            f.write(f"{sha}  {os.path.basename(self.chemin)}\n")
        return sha


class JournalNul:
    """Même interface, rien d'écrit (étalonnage des forces et de la grille, qui ne sont pas des courses)."""

    nombre_lignes = 0
    octets_bruts = 0

    def objet(self, valeur):
        return empreinte(valeur)

    def decision(self, *a, **k):
        return None

    def fermer(self):
        return None


def lire(chemin):
    """Lit un journal et vérifie la chaîne et la table des objets ; rend (en-tête, objets, décisions). Lève `JournalRompu`."""
    entete, objets, decisions = None, {}, []
    precedente = ZERO
    with lzma.open(chemin, "rb") as f:
        for i, brut in enumerate(f):
            octets = brut.rstrip(b"\n")
            try:
                ligne = json.loads(octets)
            except ValueError as e:
                raise JournalRompu(f"{chemin} : ligne {i} illisible ({e})") from e
            if ligne.get("precedente") != precedente or ligne.get("n") != i:
                raise JournalRompu(f"{chemin} : chaîne rompue à la ligne {i}")
            if canonique(ligne) != octets:
                raise JournalRompu(f"{chemin} : ligne {i} non canonique")
            precedente = hashlib.sha256(octets).hexdigest()
            sorte = ligne.get("sorte")
            if i == 0:
                if sorte != "entete":
                    raise JournalRompu(f"{chemin} : première ligne sans en-tête")
                entete = ligne
            elif sorte == "objet":
                if empreinte(ligne["valeur"]) != ligne["cle"]:
                    raise JournalRompu(f"{chemin} : objet {ligne['cle'][:12]}… dont l'empreinte ne correspond pas")
                objets[ligne["cle"]] = ligne["valeur"]
            elif sorte == "decision":
                decisions.append(ligne)
            else:
                raise JournalRompu(f"{chemin} : sorte de ligne inconnue {sorte!r}")
    if entete is None:
        raise JournalRompu(f"{chemin} : journal vide")
    return entete, objets, decisions
