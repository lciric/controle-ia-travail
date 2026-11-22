"""Véhicule NA-1, lot 7 — outils communs du lot (`commun_na_lot7_v1`) : empreintes, écriture scellée sans écrasement,
lecture scellée, fichier en ajout seul et sa relecture.

**Copie déclarée.** `relire_ajout_seul` et `FichierAjoutSeul` reprennent la règle de `portier_na_v1` (lot 5, ses
lignes 247 à 321 : rang sans trou, chaînage par l'empreinte de la ligne précédente, forme canonique `sort_keys`, compagnon
`.sha256` au format de `sha256sum`), sans l'importer : le lot 7 s'éprouve ici sans la chaîne des lots 1 à 6. Sur la chaîne
entière, le lot 8 peut lui substituer `portier_na_v1.relire_ajout_seul` ; les deux lisent les mêmes octets de la même façon
(rien n'est réparé, toute rupture est refusée). `ecrire_json_scelle` suit `outils.ecrire_json_scelle` de l'orchestrateur
(`a41b7b50…`, JSON indenté de deux, clés triées) ; elle refuse d'écraser, toujours.

Aucun message d'erreur ne recopie un contenu. Bibliothèque standard seule.
"""

import hashlib
import json
import os

VERSION = "commun-na-lot7-v1"


class ScelleRefuse(RuntimeError):
    """Un fichier scellé absent, sans compagnon, ou dont le compagnon ne porte pas l'empreinte ; rien n'est réparé."""


class AjoutSeulRefuse(RuntimeError):
    """Écriture ou relecture refusée d'un fichier en ajout seul ; le message ne recopie aucun contenu."""


def sha256_octets(octets):
    return hashlib.sha256(octets).hexdigest()


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for morceau in iter(lambda: f.read(1 << 16), b""):
            h.update(morceau)
    return h.hexdigest()


def octets_json(objet):
    """Octets du JSON écrit par ce lot : indenté de deux, clés triées, UTF-8, aucun NaN, fin de ligne finale."""
    return (json.dumps(objet, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def ecrire_scelle(chemin, octets):
    """Écrit `octets` et son compagnon `.sha256` ; refuse d'écraser l'un ou l'autre (R12). Rend l'empreinte."""
    if os.path.exists(chemin) or os.path.exists(chemin + ".sha256"):
        raise ScelleRefuse("fichier existant : on n'écrase jamais (R12)")
    with open(chemin, "xb") as f:
        f.write(octets)
    empreinte = sha256_octets(octets)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{empreinte}  {os.path.basename(chemin)}\n")
    return empreinte


def ecrire_json_scelle(chemin, objet):
    return ecrire_scelle(chemin, octets_json(objet))


def lire_scelle(chemin, empreinte_attendue=None):
    """Lit un fichier et vérifie son compagnon ; si `empreinte_attendue` est donnée, l'exige aussi. Rend les octets."""
    if not os.path.isfile(chemin):
        raise ScelleRefuse(f"fichier absent : {os.path.basename(chemin)}")
    if not os.path.isfile(chemin + ".sha256"):
        raise ScelleRefuse(f"fichier non scellé (compagnon absent) : {os.path.basename(chemin)}")
    with open(chemin, "rb") as f:
        octets = f.read()
    with open(chemin + ".sha256", encoding="utf-8") as f:
        mots = f.read().split()
    if not mots or mots[0] != sha256_octets(octets):
        raise ScelleRefuse(f"le compagnon ne porte pas l'empreinte du fichier : {os.path.basename(chemin)}")
    if empreinte_attendue is not None and sha256_octets(octets) != empreinte_attendue:
        raise ScelleRefuse(f"empreinte différente de celle qui est attendue : {os.path.basename(chemin)}")
    return octets


def lire_json_scelle(chemin, empreinte_attendue=None):
    octets = lire_scelle(chemin, empreinte_attendue)
    try:
        return json.loads(octets.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        raise ScelleRefuse(f"JSON illisible : {os.path.basename(chemin)}") from None


def _ligne_canonique(ligne):
    return (json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")


def relire_ajout_seul(chemin, exiger_sceau=False):
    """Relit un fichier en ajout seul (règle du lot 5) : rangs sans trou, chaînage, forme canonique, compagnon s'il existe
    (exigé si demandé). Rend un tuple de dictionnaires."""
    try:
        with open(chemin, "rb") as f:
            octets = f.read()
    except OSError:
        raise AjoutSeulRefuse(f"fichier illisible ou absent : {os.path.basename(chemin)}") from None
    if octets and not octets.endswith(b"\n"):
        raise AjoutSeulRefuse("fichier coupé au milieu d'une ligne")
    lignes, precedente = [], "aucune"
    for i, brute in enumerate(octets.splitlines(keepends=True), start=1):
        try:
            ligne = json.loads(brute.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            raise AjoutSeulRefuse(f"ligne {i} illisible") from None
        if not isinstance(ligne, dict) or ligne.get("rang") != i or ligne.get("precedente") != precedente \
                or _ligne_canonique(ligne) != brute:
            raise AjoutSeulRefuse(f"ligne {i} : rang, chaînage ou forme rompus")
        precedente = sha256_octets(brute)
        lignes.append(ligne)
    compagnon = chemin + ".sha256"
    if exiger_sceau and not os.path.exists(compagnon):
        raise AjoutSeulRefuse(f"fichier non scellé : {os.path.basename(chemin)}")
    if os.path.exists(compagnon):
        with open(compagnon, encoding="utf-8") as f:
            mots = f.read().split()
        if not mots or mots[0] != sha256_octets(octets):
            raise AjoutSeulRefuse(f"le compagnon ne porte pas l'empreinte du fichier : {os.path.basename(chemin)}")
    return tuple(lignes)


class FichierAjoutSeul:
    """Un fichier de lignes JSON, créé neuf, écrit en ajout seul, relu et comparé avant chaque ajout ; chaque ligne porte
    son rang et l'empreinte de la précédente ; scellé par un compagnon `.sha256` (règle du lot 5)."""

    CHAMPS_PERMIS = ()
    VERSION = VERSION

    def __init__(self, dossier, nom_fichier):
        if type(nom_fichier) is not str or os.path.basename(nom_fichier) != nom_fichier or not nom_fichier.endswith(".jsonl"):
            raise AjoutSeulRefuse("un nom de fichier simple, fini par « .jsonl »")
        if not os.path.isdir(dossier):
            raise AjoutSeulRefuse("le dossier doit exister")
        self.chemin = os.path.join(dossier, nom_fichier)
        if os.path.exists(self.chemin) or os.path.exists(self.chemin + ".sha256"):
            raise AjoutSeulRefuse("fichier existant : on n'écrase jamais (R12)")
        with open(self.chemin, "xb"):
            pass
        self._taille, self._empreinte, self._precedente, self._rang, self._scelle = 0, sha256_octets(b""), "aucune", 0, False

    def _verifier_intact(self):
        try:
            with open(self.chemin, "rb") as f:
                present = f.read()
        except OSError:
            raise AjoutSeulRefuse("le fichier n'est plus lisible : écriture refusée") from None
        if len(present) != self._taille or sha256_octets(present) != self._empreinte:
            raise AjoutSeulRefuse("le fichier ne porte plus ce qui y a été écrit : écriture refusée")
        return present

    def ajouter(self, champs):
        if self._scelle:
            raise AjoutSeulRefuse("fichier scellé : aucun ajout")
        if set(champs) - set(self.CHAMPS_PERMIS):
            raise AjoutSeulRefuse("champ hors de la liste fermée")
        present = self._verifier_intact()
        ligne = dict(champs, rang=self._rang + 1, precedente=self._precedente, version=self.VERSION)
        octets = _ligne_canonique(ligne)
        with open(self.chemin, "ab") as f:
            f.write(octets)
            f.flush()
            os.fsync(f.fileno())
        self._taille += len(octets)
        self._empreinte = sha256_octets(present + octets)
        self._precedente = sha256_octets(octets)
        self._rang += 1
        return ligne

    def sceller(self):
        if self._scelle:
            raise AjoutSeulRefuse("déjà scellé")
        self._verifier_intact()
        with open(self.chemin + ".sha256", "x", encoding="utf-8") as f:
            f.write(f"{self._empreinte}  {os.path.basename(self.chemin)}\n")
        self._scelle = True
        return self._empreinte

    @property
    def scelle(self):
        return self._scelle
