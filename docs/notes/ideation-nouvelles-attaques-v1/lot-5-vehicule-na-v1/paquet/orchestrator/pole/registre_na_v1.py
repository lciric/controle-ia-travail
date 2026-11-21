"""Véhicule NA-1, lot 5 — registre des tentatives, registre servi, garde du coffre (`registre_na_v1`).

Lettre : V9 (`864f39a7…`), l. 62 et 63 (registre servi : trois champs fermés, nom, énoncé d'une ligne, classe « passée » ;
pour « au coffre » et « hors case », le seul compte par case ; ordre tiré par graine ; taille bornée), l. 308 (clés 12 et
13), l. 311 (ordre des identifiants : octets UTF-8), l. 376 (arrêt n° 5) ; conception du véhicule v5 (`1b7f6822…`),
§ 0 bis (D5 ; 07:21Z, règles 1 et 2), § 2.6, § 6.1 (arrêt n° 5), § 6.2 (lignes de compte du registre servi), § 9, point 3.

**Registre des tentatives** : dans le dossier de sortie, en ajout seul (`portier_na_v1.FichierAjoutSeul`). Pour chaque fiche
rendue : son identifiant, sa génération, l'identifiant de sa case, sa classe. Pour une fiche « passée », en plus : ses trois
champs fermés, son nom et son énoncé d'une ligne. **Le nom est l'identifiant de la fiche ; l'énoncé est son champ `idee`
sur une ligne, blancs ramenés à une seule espace, sans coupe (D5).** Rien d'un juge, rien du coût, rien de l'espèce : la
liste des champs est fermée.

**Registre servi** (fabriqué au départ des générations 2 et 3, à partir de toutes les générations précédentes) :
- une ligne par tentative « passée » ;
- pour « au coffre » et « hors case », une ligne de compte par case servie et par classe, **écrite toujours, compte nul
  compris** (07:21Z, règle 2) ;
- ordre : rangées par identifiant (octets UTF-8 ; à identifiant égal, « au coffre » puis « hors case »), puis permutées par
  la clé 12 ou 13 (`tirage_na_v4.permutation_registre`). **Que les lignes de compte soient permutées avec les autres est
  une proposition non tranchée (§ 9, point 3)** : l'appelant le dit (`permuter_comptes`), sans valeur par défaut ; s'il dit
  non, les lignes de tentative sont permutées seules et les lignes de compte suivent, rangées.

**Forme d'une ligne** (brouillon d'essai, déclaré ici ; à écrire à l'additif) :
- `tentative : <nom> ; <champ fermé 1> ; <champ fermé 2> ; <champ fermé 3> ; passée ; <énoncé en chaîne JSON>` ;
- `compte : <identifiant de case> ; au coffre ; <n>` et `compte : <identifiant de case> ; hors case ; <n>`.
L'énoncé est écrit en chaîne JSON (guillemets, échappements) pour qu'aucun champ en plus ne puisse s'y cacher ; les octets
sont joints par une fin de ligne, une fin de ligne finale ; un registre sans ligne fait zéro octet (la section est alors
omise par `requete_na_v3`).

**Garde du coffre** (arrêt n° 5) : après chaque génération, part « au coffre » parmi les fiches rendues **strictement
au-dessus d'un quart** (comparaison entière : 4 × coffre > rendues) : aux générations 1 et 2, la génération suivante ne
part pas (`ArretGardeCoffre`) ; à la troisième, le dépassement est consigné et rendu, sans arrêt.

Aucun message d'erreur ne recopie un énoncé, un nom ou un champ. Bibliothèque standard, et les modules des lots 1 et 5.
"""

import dataclasses
import hashlib
import json

from pole import contrat_fiche_na_v1 as ct
from pole import identifiants_na_v1 as ident
from pole import portier_na_v1 as pt
from pole import tirage_na_v4 as tn

VERSION = "registre-na-v1"
TETE_TENTATIVE = "tentative : "
TETE_COMPTE = "compte : "
SEPARATEUR = " ; "
CLASSES_COMPTEES = (pt.AU_COFFRE, pt.HORS_CASE)
NUMERO_ARRET_COFFRE = 5


class RegistreRefuse(RuntimeError):
    """Un registre qui ne se fabrique pas (lignes incohérentes, génération hors de 2 et 3) ; rien n'est retiré, rien n'est
    réparé ; le message ne recopie aucun contenu."""


class ArretGardeCoffre(RuntimeError):
    """Arrêt n° 5 : strictement plus d'un quart des fiches rendues d'une génération au coffre ; la génération suivante ne
    part pas."""

    numero = NUMERO_ARRET_COFFRE

    def __init__(self, generation, au_coffre, rendues):
        super().__init__(f"arrêt n° {NUMERO_ARRET_COFFRE}, garde du coffre : génération {generation}, {au_coffre} fiches au "
                         f"coffre sur {rendues} rendues, strictement plus d'un quart ; la génération suivante ne part pas")
        self.generation, self.au_coffre, self.rendues = generation, au_coffre, rendues


def enonce_sur_une_ligne(idee):
    """D5 : le champ `idee` sur une ligne : tout blanc (fins de ligne comprises) ramené à une seule espace, blancs de tête et
    de queue retirés, **sans coupe**."""
    if type(idee) is not str:
        raise RegistreRefuse("l'énoncé se tire d'une chaîne")
    return " ".join(idee.split())


# --- registre des tentatives -------------------------------------------------------------------------------------------

class RegistreTentatives(pt.FichierAjoutSeul):
    """Le registre des tentatives, en ajout seul, dans le dossier de sortie."""

    CHAMPS_PERMIS = ("identifiant", "generation", "case", "classe") + ct.CHAMPS_FERMES + ("nom", "enonce")
    VERSION = "registre-tentatives-na-v1"

    def ajouter_fiche(self, issue):
        """Une ligne pour une fiche rendue, classée par le portier (`portier_na_v1.IssueFiche`)."""
        if not isinstance(issue, pt.IssueFiche):
            raise RegistreRefuse("seule une fiche classée par le portier entre au registre")
        if issue.generation not in (1, 2, 3):
            raise RegistreRefuse("génération hors de 1 à 3")
        if issue.classe not in pt.CLASSES_FICHE:
            raise RegistreRefuse("classe inconnue")
        champs = {"identifiant": issue.identifiant, "generation": issue.generation, "case": issue.identifiant_case,
                  "classe": issue.classe}
        if issue.classe == pt.PASSEE:
            for c in ct.CHAMPS_FERMES:
                champs[c] = issue.contenu[c]
            champs["nom"] = issue.identifiant
            champs["enonce"] = enonce_sur_une_ligne(issue.contenu["idee"])
        return self.ajouter(champs)


def lire_registre_tentatives(chemin, exiger_sceau=False):
    """Relit le registre des tentatives (rangs, chaînage, sceau s'il est exigé) ; rend ses lignes."""
    return pt.relire_ajout_seul(chemin, exiger_sceau=exiger_sceau)


# --- registre servi ----------------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class RegistreServi:
    """Le registre servi d'une génération : ses octets, leur empreinte et leur taille, ses comptes de lignes."""

    generation: int
    octets: bytes
    sha256: str
    taille: int
    lignes_tentative: int
    lignes_compte: int
    comptes_permutes: bool

    @property
    def lignes(self):
        return self.lignes_tentative + self.lignes_compte


def ligne_tentative(nom, fermes, enonce):
    return TETE_TENTATIVE + SEPARATEUR.join([nom, *fermes, pt.PASSEE, json.dumps(enonce, ensure_ascii=False)])


def ligne_compte(identifiant_case, classe, n):
    return TETE_COMPTE + SEPARATEUR.join([identifiant_case, classe, str(n)])


def fabriquer_registre_servi(lignes, cases_servies, generation, *, permuter_comptes, racine=tn.RACINE_ECRITE,
                             racine_attendue=tn.RACINE_ECRITE):
    """Le registre servi de la génération `generation` (2 ou 3), à partir des lignes du registre des tentatives des
    générations précédentes et des cases servies à chacune d'elles (`{g: [identifiants]}`)."""
    if generation not in (2, 3):
        raise RegistreRefuse("le registre servi se fabrique aux générations 2 et 3")
    if type(permuter_comptes) is not bool:
        raise RegistreRefuse("`permuter_comptes` est dit, vrai ou faux (proposition non tranchée)")
    precedentes = list(range(1, generation))
    if not isinstance(cases_servies, dict) or sorted(cases_servies) != precedentes:
        raise RegistreRefuse("les cases servies de chaque génération précédente, et d'elles seules")
    cases = []
    for g in precedentes:
        for c in cases_servies[g]:
            try:
                ident.rang_du_mot_de_case(c)
            except ident.MotRefuse:
                raise RegistreRefuse("identifiant de case qui n'est pas un mot de trois syllabes") from None
            if c in cases:
                raise RegistreRefuse("case servie deux fois")
            cases.append(c)
    tentatives, comptes, noms = [], {(c, k): 0 for c in cases for k in CLASSES_COMPTEES}, set()
    for l in lignes:
        if not isinstance(l, dict) or l.get("generation") not in (1, 2, 3):
            raise RegistreRefuse("ligne du registre des tentatives mal formée")
        if l["generation"] >= generation:
            continue
        if l.get("case") not in cases:
            raise RegistreRefuse("tentative d'une case qui n'a pas été servie à sa génération")
        classe = l.get("classe")
        if classe == pt.PASSEE:
            nom = l.get("nom")
            if nom != l.get("identifiant") or nom in noms:
                raise RegistreRefuse("tentative passée : le nom est l'identifiant, une fois")
            noms.add(nom)
            fermes = [l.get(c) for c in ct.CHAMPS_FERMES]
            if not all(type(v) is str for v in fermes) or type(l.get("enonce")) is not str:
                raise RegistreRefuse("tentative passée : champs fermés et énoncé")
            tentatives.append((nom, ligne_tentative(nom, fermes, l["enonce"])))
        elif classe in CLASSES_COMPTEES:
            comptes[(l["case"], classe)] += 1
        else:
            raise RegistreRefuse("classe inconnue au registre des tentatives")
    rang_classe = {k: i for i, k in enumerate(CLASSES_COMPTEES)}
    lignes_compte = [((c, rang_classe[k]), ligne_compte(c, k, n)) for (c, k), n in comptes.items()]

    def cle(e):
        return (e[0][0].encode("utf-8"), e[0][1]) if isinstance(e[0], tuple) else (e[0].encode("utf-8"), -1)

    if permuter_comptes:
        rangees = sorted(tentatives + lignes_compte, key=cle)
        perm = tn.permutation_registre(generation, len(rangees), racine, racine_attendue)
        ordre = [rangees[i][1] for i in perm]
    else:
        rangees = sorted(tentatives, key=cle)
        perm = tn.permutation_registre(generation, len(rangees), racine, racine_attendue)
        ordre = [rangees[i][1] for i in perm] + [e[1] for e in sorted(lignes_compte, key=cle)]
    octets = ("\n".join(ordre) + "\n").encode("utf-8") if ordre else b""
    return RegistreServi(generation, octets, hashlib.sha256(octets).hexdigest(), len(octets), len(tentatives),
                         len(lignes_compte), permuter_comptes)


# --- garde du coffre (arrêt n° 5) ---------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ConstatCoffre:
    generation: int
    au_coffre: int
    rendues: int
    depasse: bool
    consigne: bool  # vrai à la troisième génération quand la garde dépasse : consigné, sans arrêt


def garde_du_coffre(lignes, generation):
    """Arrêt n° 5 sur les lignes du registre des tentatives de la génération `generation` : strictement plus d'un quart au
    coffre parmi les fiches rendues ; générations 1 et 2 : arrêt ; génération 3 : consigné."""
    if generation not in (1, 2, 3):
        raise RegistreRefuse("génération hors de 1 à 3")
    de_g = [l for l in lignes if isinstance(l, dict) and l.get("generation") == generation]
    rendues = len(de_g)
    au_coffre = sum(1 for l in de_g if l.get("classe") == pt.AU_COFFRE)
    depasse = 4 * au_coffre > rendues
    if depasse and generation in (1, 2):
        raise ArretGardeCoffre(generation, au_coffre, rendues)
    return ConstatCoffre(generation, au_coffre, rendues, depasse, depasse and generation == 3)
