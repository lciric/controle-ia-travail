"""Véhicule NA-1, lot 6 v5 — registre des tentatives **v4, minimal** : le registre v3 du lot 5 (`registre_na_v3`,
`17f453b1…`), plus le champ fermé `id_tentative` de l'erratum 3 à l'interface (`registre_na_v4`).

Pourquoi ici : l'erratum 3 (§ 1, § 4) veut le champ au registre, écrit par le lot 5 et produit par le lot 6. Le registre v3
le refuse (liste fermée des champs, `verifier_ligne`), et le lot 5 n'est pas à moi : cette v4 vit dans le dossier du lot 6
v5, **sans toucher aux fichiers du lot 5**, et le dit. Elle ne change **aucune règle** du v3 : chaque ligne, ramenée à la
forme du v3 (sans `id_tentative`, version du v3), est vérifiée par le code du v3 lui-même (`verifier_ligne`,
`chaines_de`) ; le registre servi, la garde du coffre et les comptes sont ceux du v3, sur les lignes ramenées.

**Ce que la v4 ajoute** (erratum 3, § 1) :
- `id_tentative` : `T` + génération sur deux chiffres + `-` + numéro de chaîne sur quatre chiffres + `-` + rang de repli
  (`^T[0-9]{2}-[0-9]{4}-[0-2]$`) ;
- sur chaque ligne `tentative`, son identifiant ; sur chaque ligne `fiche`, celui de la tentative qui l'a servie ;
- numéro de chaîne : 0001 à la première chaîne de la génération, puis +1 à chaque chaîne, sans trou ; rang = `rang_repli` ;
- refus (`RegistreRefuse`) : ligne sans `id_tentative`, ou hors de sa forme, ou d'une autre génération, ou d'un autre rang
  que `rang_repli`, ou numéro hors de la suite ; fiche dont l'identifiant n'est pas celui de sa tentative ; identifiant écrit
  deux fois ; une ligne du v3 (sans le champ) est dite ancien format ;
- unicité dans la course : `verifier_unicite_course` sur les registres de toutes les générations.

Bibliothèque standard, et les modules du lot 5 v1 et v3.
"""

import re

from pole import portier_na_v1 as pt
from pole import registre_na_v3 as rg3

VERSION = "registre-na-v4"
VERSION_LIGNE = "registre-tentatives-na-v4"
CHAMP_ID = "id_tentative"
FORME_ID = re.compile(r"^T[0-9]{2}-[0-9]{4}-[0-2]$")
CHAMPS_LIGNE = rg3.CHAMPS_LIGNE + (CHAMP_ID,)
RegistreRefuse = rg3.RegistreRefuse


class RegistreAncienFormatV4(rg3.RegistreAncienFormat):
    """Une ligne du registre v3 (ou plus ancien), sans `id_tentative`, donnée au registre v4."""


def id_tentative(generation, numero_chaine, rang):
    """L'identifiant d'une tentative (erratum 3, § 1)."""
    if type(generation) is not int or not 1 <= generation <= 99:
        raise RegistreRefuse("identifiant de tentative : génération de 1 à 99")
    if type(numero_chaine) is not int or not 1 <= numero_chaine <= 9999:
        raise RegistreRefuse("identifiant de tentative : numéro de chaîne de 1 à 9999")
    if type(rang) is not int or rang not in rg3.RANGS_REPLI:
        raise RegistreRefuse("identifiant de tentative : rang de repli 0, 1 ou 2")
    return f"T{generation:02d}-{numero_chaine:04d}-{rang}"


def lire_id(v):
    """(génération, numéro de chaîne, rang) d'un identifiant à la forme ; sinon `RegistreRefuse`."""
    if type(v) is not str or not FORME_ID.match(v):
        raise RegistreRefuse("identifiant de tentative absent ou hors de sa forme")
    return int(v[1:3]), int(v[4:8]), int(v[9])


def vers_v3(ligne):
    """La ligne ramenée à la forme du v3 : sans `id_tentative`, version du v3 (pour le code du v3, inchangé)."""
    l = {k: v for k, v in ligne.items() if k != CHAMP_ID}
    if "version" in l:
        l["version"] = rg3.VERSION_LIGNE
    return l


def lignes_v3_de(lignes):
    """Toutes les lignes d'un registre v4 relu, ramenées à la forme du v3 ; une ligne sans version v4 est refusée."""
    rendu = []
    for l in lignes:
        if not isinstance(l, dict) or l.get("version") != VERSION_LIGNE:
            raise RegistreAncienFormatV4("une ligne qui n'est pas du registre v4")
        rendu.append(vers_v3(l))
    return rendu


def verifier_ids(lignes, generation):
    """Les identifiants d'une suite de lignes (ordre du fichier) : forme, génération, rang, numéro de chaîne suivi d'un
    seul cran, fiche à l'identifiant de sa tentative, aucun identifiant de tentative deux fois. Rend le dernier numéro."""
    dernier, vus, courant = 0, set(), None
    for l in lignes:
        if not isinstance(l, dict) or CHAMP_ID not in l:
            raise RegistreAncienFormatV4("une ligne sans `id_tentative` (registre v3 ou plus ancien)")
        g, n, r = lire_id(l[CHAMP_ID])
        if g != generation:
            raise RegistreRefuse("identifiant de tentative d'une autre génération")
        if r != l.get("rang_repli"):
            raise RegistreRefuse("identifiant de tentative : rang autre que `rang_repli`")
        if l.get("type_ligne") == rg3.TYPE_FICHE:
            if courant is None or l[CHAMP_ID] != courant:
                raise RegistreRefuse("fiche : l'identifiant n'est pas celui de la tentative qui l'a servie")
            continue
        if l[CHAMP_ID] in vus:
            raise RegistreRefuse("identifiant de tentative écrit deux fois")
        if r == 0:
            if n != dernier + 1:
                raise RegistreRefuse("numéro de chaîne hors de la suite (0001, puis +1 par chaîne)")
            dernier = n
        elif n != dernier:
            raise RegistreRefuse("repli : numéro de chaîne autre que celui de sa chaîne")
        vus.add(l[CHAMP_ID])
        courant = l[CHAMP_ID]
    return dernier


class RegistreTentativesV4(pt.FichierAjoutSeul):
    """Le registre des tentatives d'une génération, v4 : celui du v3, plus `id_tentative`."""

    CHAMPS_PERMIS = CHAMPS_LIGNE
    VERSION = VERSION_LIGNE

    def __init__(self, dossier_sortie, nom_fichier, *, generation, cases_servies, modeles_demandes):
        self.contexte = rg3.contexte_de(generation=generation, cases_servies=cases_servies,
                                        modeles_demandes=modeles_demandes)
        super().__init__(dossier_sortie, nom_fichier)
        self._lignes_v3 = []
        self._lignes = []
        self.numero_chaine = 0

    def ajouter(self, champs):
        raise RegistreRefuse("écriture directe d'une ligne refusée : une chaîne s'écrit par `ajouter_chaine`")

    def ajouter_fiche(self, issue):
        raise rg3.RegistreAncienFormat("appel `ajouter_fiche` d'une fiche seule, sans sa tentative")

    def ajouter_chaine(self, tentatives, fiches=()):
        """Comme le v3 (mêmes entrées, mêmes vérifications, avant toute écriture), puis chaque ligne reçoit son
        `id_tentative` ; le numéro de chaîne est le suivant de la génération. Rend (lignes écrites, numéro)."""
        if not isinstance(tentatives, (list, tuple)) or not 1 <= len(tentatives) <= len(rg3.RANGS_REPLI):
            raise RegistreRefuse("une chaîne compte une à trois tentatives")
        fiches = tuple(fiches)
        prets = []
        for t in tentatives:
            if not isinstance(t, dict) or set(t) - set(rg3.CHAMPS_TENTATIVE):
                raise RegistreRefuse("tentative : un dictionnaire aux champs de l'interface")
            t = dict(t)
            t.setdefault("categorie_refus", None)
            if set(rg3.CHAMPS_TENTATIVE) - set(t):
                raise RegistreRefuse("tentative incomplète : un champ de l'interface manque")
            prets.append(t)
        if fiches and prets[-1]["classe_issue"] != pt.FICHES_RENDUES:
            raise RegistreRefuse("des fiches pour une tentative qui n'est pas « fiches rendues »")
        lignes = [rg3.RegistreTentativesV3._ligne(self, t, None) for t in prets] + \
                 [rg3.RegistreTentativesV3._ligne(self, prets[-1], f) for f in fiches]
        avant = len(rg3.chaines_de(self._lignes_v3, self.contexte))
        if len(rg3.chaines_de(self._lignes_v3 + lignes, self.contexte)) != avant + 1:
            raise RegistreRefuse("une chaîne commence au rang 0")
        numero = self.numero_chaine + 1
        g = self.contexte.generation
        avec_id = [dict(l, **{CHAMP_ID: id_tentative(g, numero, l["rang_repli"])}) for l in lignes]
        verifier_ids(self._lignes + avec_id, g)
        rendues = []
        for l, l3 in zip(avec_id, lignes):
            rendues.append(super().ajouter(l))
            self._lignes.append(l)
            self._lignes_v3.append(l3)
        self.numero_chaine = numero
        return rendues, numero


def lire_registre_tentatives_v4(chemin, *, generation, cases_servies, modeles_demandes, exiger_sceau=False):
    """Relit un registre v4 : fichier (rangs, chaînage, sceau s'il est exigé), version v4 de chaque ligne, identifiants,
    puis chaque ligne et la suite des chaînes par le code du v3. Rend ses lignes (avec `id_tentative`)."""
    contexte = rg3.contexte_de(generation=generation, cases_servies=cases_servies, modeles_demandes=modeles_demandes)
    lignes = pt.relire_ajout_seul(chemin, exiger_sceau=exiger_sceau)
    v3 = lignes_v3_de(lignes)
    verifier_ids(lignes, generation)
    rg3.chaines_de(v3, contexte)
    return lignes


def verifier_unicite_course(registres):
    """Erratum 3 : chaque identifiant de tentative est unique dans la course. `registres` : {génération: lignes}."""
    vus = set()
    for g, lignes in sorted(registres.items()):
        for l in lignes:
            if l.get("type_ligne") != rg3.TYPE_TENTATIVE:
                continue
            if l[CHAMP_ID] in vus:
                raise RegistreRefuse("identifiant de tentative écrit deux fois dans la course")
            vus.add(l[CHAMP_ID])
    return len(vus)


def fabriquer_registre_servi_v4(lignes, cases_servies, generation, **kw):
    return rg3.fabriquer_registre_servi_v3(lignes_v3_de(lignes), cases_servies, generation, **kw)


def garde_du_coffre_v4(lignes, generation):
    """N° 5, par le code du v3 (lignes `fiche` seules, fiches servies par repli comprises)."""
    return rg3.garde_du_coffre_v3(lignes_v3_de(lignes), generation)


__all__ = ["RegistreTentativesV4", "RegistreAncienFormatV4", "RegistreRefuse", "id_tentative", "lire_id", "vers_v3",
           "lignes_v3_de", "verifier_ids", "lire_registre_tentatives_v4", "verifier_unicite_course",
           "fabriquer_registre_servi_v4", "garde_du_coffre_v4", "CHAMP_ID", "FORME_ID", "VERSION", "VERSION_LIGNE"]
