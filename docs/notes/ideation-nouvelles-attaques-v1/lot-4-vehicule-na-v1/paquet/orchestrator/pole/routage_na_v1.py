"""Véhicule NA-1, lot 4 — table des rôles et des clés, parts, pires par rôle et cumul par clé (`routage_na_v1`).

Lettre : V9 (`864f39a7…`), l. 383 (arrêt n° 12 : part d'une clé épuisée ; un rôle présenté sur une autre clé que la
sienne ; aucune bascule), l. 156 (le cumul par clé ne vit qu'au journal des arrêts n° 11 à n° 13), l. 402 (routage par
rôle, non par espèce) ; conception du véhicule v5 (`1b7f6822…`), § 2.3 (pas 1 et 2 ; table des rôles et des clés ;
`hors_course` ; Rigaud ; seconde table des lignes à part, que la seconde clause ne lit pas), § 2.9 (`hors_course`),
§ 2.10 (tables de routage des deux lignes à part), § 6.1 (arrêt n° 12 ; D11), § 6.2 (`hors_course`).

- **La table se lit à son empreinte** (arrêt n° 14 pour la table : un écart refuse, en nommant la pièce). Elle porte une
  marque : « course », « ligne à part » ou « artefact ». Une table marquée « artefact » (la table plantée de D11) n'est
  jamais chargée comme table de course ou de ligne à part : elle ne se lit qu'en la demandant comme artefact.
- **Routage par rôle** (`TableRolesCles.router`) : le couple (étiquette du rôle, nom d'adaptateur) doit être celui de la
  table, exactement. Un rôle absent de la table, un rôle routé vers `hors_course`, un adaptateur absent de la table, un
  envoi adressé à une clé sans part (Rigaud) ou à `hors_course`, un rôle présenté sur une autre clé ou un autre adaptateur
  que les siens : arrêt n° 12, seconde clause, qui dit la clé présentée.
- **Part de la clé** (`verifier_part`) : cumul compté sur la clé, plus le pire des appels en vol sur elle (zéro : les appels
  sont lancés l'un après l'autre ; le terme reste écrit), plus le pire de l'appel à lancer ; strictement au-delà de la part :
  arrêt n° 12, première clause. Une table de ligne à part ne lit pas les parts : elle lit le plafond de sa ligne, sur un
  cumul à elle.
- **Montants** en micro-dollars entiers (aucune somme de flottants) ; une part s'écrit au centime, un pire au
  micro-dollar ; un coût compté est arrondi au micro-dollar supérieur.
- Aucun message d'arrêt ne porte de montant : le cumul par clé et la part ne sont que des attributs de l'arrêt, pour le
  journal des arrêts n° 11 à n° 13 (V9, l. 156).

Format de la table (`table-roles-cles-na-v1`), JSON :
`{"format", "marque", "nom", "plafond_ligne_usd", "cles": [{"nom", "type", "part_usd", "adaptateurs", "relais"}],
"roles": [{"role", "sorte", "espece", "cle", "adaptateur"}]}`.

Bibliothèque standard, et `pole.relais` (adresse locale du relais).
"""

import dataclasses
import decimal
import hashlib
import json
import types

from pole.relais import RelaisInvalide, valider_url_relais

VERSION = "routage-na-v1"
FORMAT_TABLE = "table-roles-cles-na-v1"
MARQUE_COURSE, MARQUE_LIGNE_A_PART, MARQUE_ARTEFACT = "course", "ligne à part", "artefact"
MARQUES = (MARQUE_COURSE, MARQUE_LIGNE_A_PART, MARQUE_ARTEFACT)
TYPES_CLE = ("claude_sdk", "commande_externe", "kimi_protocole", "aucun")
SORTES_ROLE = ("proposeur", "portier", "juge")
CLE_HORS_COURSE = "hors_course"
NUMERO_ARRET_PART = 12
NUMERO_ARRET_EMPREINTE = 14
CLAUSE_PART, CLAUSE_ROUTAGE = "première", "seconde"
MICRO = 1_000_000
_CENT = decimal.Decimal("0.01")
_MICRO_D = decimal.Decimal("0.000001")


class TableRefusee(ValueError):
    """La table des rôles et des clés ne tient pas sa forme : rien ne se charge ; le message ne recopie aucune valeur."""


class EmpreinteTableDifferente(TableRefusee):
    """Arrêt n° 14 pour la table : son empreinte diffère de celle qui est écrite."""

    numero = NUMERO_ARRET_EMPREINTE

    def __init__(self, piece):
        super().__init__(f"arrêt n° {NUMERO_ARRET_EMPREINTE} : empreinte de la pièce « {piece} » différente de celle qui "
                         "est écrite ; refus")
        self.piece = piece


class MontantRefuse(ValueError):
    """Un montant qui n'est pas un nombre fini, positif, à la précision permise."""


class ArretPartCle(RuntimeError):
    """Arrêt n° 12 (V9, l. 383) : aucun appel neuf sur cette clé, arrêt nommé de la course, qui dit la clé ; aucune bascule.
    Le message ne porte aucun montant ; `cumul_micro`, `en_vol_micro`, `pire_micro` et `limite_micro` ne servent qu'au
    journal des arrêts n° 11 à n° 13."""

    numero = NUMERO_ARRET_PART

    def __init__(self, clause, cle, motif, *, role=None, cumul_micro=None, en_vol_micro=None, pire_micro=None,
                 limite_micro=None):
        super().__init__(f"arrêt n° {NUMERO_ARRET_PART}, {clause} clause : clé « {cle} » ; {motif} ; aucun appel neuf sur "
                         "cette clé, aucune bascule")
        self.clause, self.cle, self.motif, self.role = clause, cle, motif, role
        self.cumul_micro, self.en_vol_micro, self.pire_micro, self.limite_micro = (cumul_micro, en_vol_micro, pire_micro,
                                                                                   limite_micro)


# --- montants ----------------------------------------------------------------------------------------------------------

def _decimal(valeur):
    if isinstance(valeur, bool) or not isinstance(valeur, (int, float, str, decimal.Decimal)):
        raise MontantRefuse("montant : un nombre")
    try:
        d = decimal.Decimal(repr(valeur)) if isinstance(valeur, float) else decimal.Decimal(valeur)
    except decimal.InvalidOperation:
        raise MontantRefuse("montant illisible") from None
    if not d.is_finite() or d < 0:
        raise MontantRefuse("montant : fini et positif")
    return d


def micro_exact(valeur, pas=_MICRO_D):
    """Un montant écrit (part au centime, pire au micro-dollar), en micro-dollars ; une précision plus fine est refusée."""
    d = _decimal(valeur)
    if d != d.quantize(pas):
        raise MontantRefuse("montant plus fin que la précision permise")
    return int(d * MICRO)


def micro_cout(valeur):
    """Un coût compté par le noyau, en micro-dollars : le bruit des flottants ôté au nano-dollar, puis arrondi au
    micro-dollar supérieur (côté prudent)."""
    d = _decimal(valeur).quantize(decimal.Decimal("0.000000001"), rounding=decimal.ROUND_HALF_EVEN)
    return int(d.quantize(_MICRO_D, rounding=decimal.ROUND_CEILING) * MICRO)


def usd(micro):
    return f"{decimal.Decimal(micro) / MICRO:.6f}"


# --- la table ----------------------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class Cle:
    nom: str
    type: str
    part_micro: object
    adaptateurs: tuple
    relais: object

    @property
    def hors_course(self):
        return self.nom == CLE_HORS_COURSE

    @property
    def sans_part(self):
        return self.type == "aucun"


@dataclasses.dataclass(frozen=True)
class EntreeRole:
    role: str
    sorte: str
    espece: int
    cle: str
    adaptateur: str


@dataclasses.dataclass(frozen=True)
class TableRolesCles:
    sha256: str
    marque: str
    nom: str
    plafond_ligne_micro: object
    cles: types.MappingProxyType
    roles: types.MappingProxyType
    adaptateur_vers_cle: types.MappingProxyType

    def entree(self, role):
        return self.roles.get(role)

    def cle_de_adaptateur(self, nom_adaptateur):
        return self.adaptateur_vers_cle.get(nom_adaptateur)

    def compte_de(self, cle):
        """Le cumul où un appel de cette clé est compté : la clé, pour une table de course ; la ligne, pour une ligne à part."""
        return self.nom if self.marque == MARQUE_LIGNE_A_PART else cle

    def router(self, role, nom_adaptateur):
        """Pas 1 (§ 2.3) : rend l'entrée du rôle si le couple (rôle, adaptateur) est celui de la table ; sinon arrêt n° 12,
        seconde clause, qui dit la clé présentée. Recherche **par rôle**, jamais par espèce."""
        cle_presentee = self.cle_de_adaptateur(nom_adaptateur) if isinstance(nom_adaptateur, str) else None
        nom_presente = cle_presentee.nom if cle_presentee is not None else "adaptateur hors table"
        e = self.roles.get(role) if isinstance(role, str) else None
        if e is None:
            raise ArretPartCle(CLAUSE_ROUTAGE, nom_presente, "rôle absent de la table : il n'est sur aucune clé", role=role)
        if e.cle == CLE_HORS_COURSE:
            raise ArretPartCle(CLAUSE_ROUTAGE, nom_presente, "rôle routé vers hors_course : la course ne l'appelle jamais",
                               role=role)
        if cle_presentee is None:
            raise ArretPartCle(CLAUSE_ROUTAGE, nom_presente, "adaptateur absent de la table", role=role)
        if cle_presentee.hors_course or cle_presentee.sans_part:
            raise ArretPartCle(CLAUSE_ROUTAGE, nom_presente, "envoi adressé à une clé sans part ou hors course : tout envoi "
                               "y est refusé", role=role)
        if (e.cle, e.adaptateur) != (cle_presentee.nom, nom_adaptateur):
            raise ArretPartCle(CLAUSE_ROUTAGE, nom_presente, "rôle présenté sur une autre clé ou un autre adaptateur que "
                               "les siens", role=role)
        return e


def _texte(valeur, quoi):
    if type(valeur) is not str or not valeur or valeur != valeur.strip():
        raise TableRefusee(f"{quoi} : une chaîne non vide, sans blanc autour")
    return valeur


def _sans_double(paires):
    d = {}
    for k, v in paires:
        if k in d:
            raise TableRefusee("clé JSON en double")
        d[k] = v
    return d


def lire_table(octets, empreinte_attendue, marque_attendue, nom_piece="table des rôles et des clés"):
    """La table à son empreinte, de la marque attendue ; tout écart de forme est refusé, rien n'est réparé."""
    if marque_attendue not in MARQUES:
        raise TableRefusee("marque attendue inconnue")
    if not isinstance(octets, (bytes, bytearray)):
        raise TableRefusee("la table se lit en octets")
    octets = bytes(octets)
    sha = hashlib.sha256(octets).hexdigest()
    if type(empreinte_attendue) is not str or sha != empreinte_attendue:
        raise EmpreinteTableDifferente(nom_piece)
    try:
        obj = json.loads(octets.decode("utf-8"), object_pairs_hook=_sans_double)
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise TableRefusee("table illisible") from None
    cles_tete = {"format", "marque", "nom", "plafond_ligne_usd", "cles", "roles"}
    if not isinstance(obj, dict) or set(obj) != cles_tete:
        raise TableRefusee("clés de tête : " + ", ".join(sorted(cles_tete)))
    if obj["format"] != FORMAT_TABLE:
        raise TableRefusee("format inconnu")
    if obj["marque"] not in MARQUES:
        raise TableRefusee("marque inconnue")
    if obj["marque"] != marque_attendue:
        raise TableRefusee(f"table marquée « {obj['marque']} » là où une table « {marque_attendue} » est attendue")
    marque = obj["marque"]
    nom = _texte(obj["nom"], "nom de la table")
    if marque == MARQUE_LIGNE_A_PART:
        if obj["plafond_ligne_usd"] is None:
            raise TableRefusee("une table de ligne à part porte le plafond de sa ligne")
        try:
            plafond = micro_exact(obj["plafond_ligne_usd"], _CENT)
        except MontantRefuse:
            raise TableRefusee("plafond de la ligne : un montant au centime") from None
        if plafond <= 0:
            raise TableRefusee("plafond de la ligne : strictement positif")
    else:
        if obj["plafond_ligne_usd"] is not None:
            raise TableRefusee("seule une table de ligne à part porte un plafond de ligne")
        plafond = None
    if not isinstance(obj["cles"], list) or not obj["cles"]:
        raise TableRefusee("liste des clés vide ou invalide")
    cles, vers_cle = {}, {}
    for c in obj["cles"]:
        if not isinstance(c, dict) or set(c) != {"nom", "type", "part_usd", "adaptateurs", "relais"}:
            raise TableRefusee("une clé porte exactement nom, type, part_usd, adaptateurs, relais")
        n = _texte(c["nom"], "nom d'usage d'une clé")
        if n in cles:
            raise TableRefusee("nom d'usage de clé en double")
        if c["type"] not in TYPES_CLE:
            raise TableRefusee(f"clé « {n} » : type inconnu")
        if n == CLE_HORS_COURSE and c["type"] != "aucun":
            raise TableRefusee("hors_course : type « aucun »")
        if c["type"] == "aucun" or marque == MARQUE_LIGNE_A_PART:
            if c["part_usd"] is not None:
                raise TableRefusee(f"clé « {n} » : aucune part (clé sans part, ou table de ligne à part)")
            part = None
        else:
            try:
                part = micro_exact(c["part_usd"], _CENT)
            except MontantRefuse:
                raise TableRefusee(f"clé « {n} » : part au centime") from None
            if part <= 0:
                raise TableRefusee(f"clé « {n} » : part strictement positive")
        if not isinstance(c["adaptateurs"], list) or not all(type(a) is str and a for a in c["adaptateurs"]):
            raise TableRefusee(f"clé « {n} » : liste de noms d'adaptateur")
        if c["type"] != "aucun" and not c["adaptateurs"]:
            raise TableRefusee(f"clé « {n} » : au moins un adaptateur")
        for a in c["adaptateurs"]:
            if a in vers_cle:
                raise TableRefusee("nom d'adaptateur sur deux clés")
            vers_cle[a] = n
        relais = c["relais"]
        if c["type"] == "claude_sdk" and relais is None:
            raise TableRefusee(f"clé « {n} » : une clé Claude porte l'adresse locale de son relais")
        if relais is not None:
            try:
                valider_url_relais(relais)
            except RelaisInvalide:
                raise TableRefusee(f"clé « {n} » : adresse de relais non locale ou invalide") from None
        cles[n] = Cle(n, c["type"], part, tuple(c["adaptateurs"]), relais)
    if marque != MARQUE_LIGNE_A_PART and CLE_HORS_COURSE not in cles:
        raise TableRefusee("la table de la course porte la clé hors_course")
    if not isinstance(obj["roles"], list) or not obj["roles"]:
        raise TableRefusee("liste des rôles vide ou invalide")
    roles = {}
    for r in obj["roles"]:
        if not isinstance(r, dict) or set(r) != {"role", "sorte", "espece", "cle", "adaptateur"}:
            raise TableRefusee("un rôle porte exactement role, sorte, espece, cle, adaptateur")
        nr = _texte(r["role"], "étiquette d'un rôle")
        if nr in roles:
            raise TableRefusee("étiquette de rôle en double")
        if r["sorte"] not in SORTES_ROLE:
            raise TableRefusee(f"rôle « {nr} » : sorte inconnue")
        if type(r["espece"]) is not int or not 1 <= r["espece"] <= 6:
            raise TableRefusee(f"rôle « {nr} » : espèce de 1 à 6")
        if r["cle"] not in cles:
            raise TableRefusee(f"rôle « {nr} » : clé absente de la table")
        cle = cles[r["cle"]]
        if cle.sans_part and not cle.hors_course:
            raise TableRefusee(f"rôle « {nr} » : routé vers une clé sans part")
        if r["adaptateur"] not in cle.adaptateurs:
            raise TableRefusee(f"rôle « {nr} » : adaptateur qui n'est pas celui de sa clé")
        roles[nr] = EntreeRole(nr, r["sorte"], r["espece"], r["cle"], r["adaptateur"])
    return TableRolesCles(sha, marque, nom, plafond, types.MappingProxyType(cles), types.MappingProxyType(roles),
                          types.MappingProxyType({a: cles[n] for a, n in vers_cle.items()}))


def charger_table(chemin, empreinte_attendue, marque_attendue, nom_piece="table des rôles et des clés"):
    with open(chemin, "rb") as f:
        return lire_table(f.read(), empreinte_attendue, marque_attendue, nom_piece)


# --- parts, pires, cumul -----------------------------------------------------------------------------------------------

def lire_parts(table, parts):
    """Les parts d'une table de course (au centime, une par clé qui porte un rôle de la course) ; une table de ligne à part
    n'en lit aucune. Rend {clé: micro-dollars}."""
    attendues = sorted({e.cle for e in table.roles.values() if e.cle != CLE_HORS_COURSE})
    if table.marque == MARQUE_LIGNE_A_PART:
        if parts:
            raise TableRefusee("une ligne à part ne lit aucune part : elle lit le plafond de sa ligne")
        return {}
    if not isinstance(parts, dict) or sorted(parts) != attendues:
        raise TableRefusee("parts : exactement une par clé qui porte un rôle de la course")
    rendu = {}
    for cle, v in parts.items():
        try:
            rendu[cle] = micro_exact(v, _CENT)
        except MontantRefuse:
            raise TableRefusee(f"part de « {cle} » : un montant au centime") from None
        if rendu[cle] <= 0:
            raise TableRefusee(f"part de « {cle} » : strictement positive")
        if table.cles[cle].part_micro != rendu[cle]:
            raise TableRefusee(f"part de « {cle} » différente de celle de la table scellée")
    return rendu


def lire_pires(table, pires):
    """Le pire d'un appel, par étiquette de rôle, pour chaque rôle routé de la table (hors `hors_course`)."""
    attendus = sorted(r for r, e in table.roles.items() if e.cle != CLE_HORS_COURSE)
    if not isinstance(pires, dict) or sorted(pires) != attendus:
        raise TableRefusee("pires : exactement un par rôle routé de la table")
    rendu = {}
    for role, v in pires.items():
        try:
            rendu[role] = micro_exact(v)
        except MontantRefuse:
            raise TableRefusee(f"pire de « {role} » : un montant au micro-dollar") from None
        if rendu[role] <= 0:
            raise TableRefusee(f"pire de « {role} » : strictement positif")
    return rendu


class CumulParCle:
    """Le cumul compté par clé (table de course) ou par ligne (ligne à part), en micro-dollars, et le pire des appels en vol.
    Un seul objet par table, partagé par les générations d'une course : la part d'une clé vaut pour la course entière. Il ne
    vit qu'au journal des arrêts n° 11 à n° 13 (V9, l. 156) : ni M4 ni la composition ne le lisent."""

    def __init__(self, table):
        if not isinstance(table, TableRolesCles):
            raise TypeError("le cumul se construit sur une table lue par `lire_table`")
        self.table_sha256 = table.sha256
        comptes = [table.nom] if table.marque == MARQUE_LIGNE_A_PART else [
            n for n, c in table.cles.items() if not c.sans_part]
        self._cumul = {n: 0 for n in comptes}
        self._en_vol = {}
        self._jetons = 0

    def cumul(self, compte):
        return self._cumul[compte]

    def en_vol(self, compte):
        return sum(p for (c, p) in self._en_vol.values() if c == compte)

    def ajouter(self, compte, micro):
        if type(micro) is not int or micro < 0:
            raise MontantRefuse("un coût compté : des micro-dollars entiers, positifs")
        self._cumul[compte] += micro

    def ouvrir_vol(self, compte, pire_micro):
        self._jetons += 1
        self._en_vol[self._jetons] = (compte, pire_micro)
        return self._jetons

    def fermer_vol(self, jeton):
        self._en_vol.pop(jeton, None)

    def etat(self):
        """Pour le journal des arrêts n° 11 à n° 13 seulement : {compte: USD écrit au micro-dollar}."""
        return {n: usd(v) for n, v in sorted(self._cumul.items())}


def verifier_part(table, parts_micro, cumul, cle, role, pire_micro):
    """Pas 2 (§ 2.3) : cumul compté + pire des appels en vol + pire de l'appel à lancer, strictement au-delà de la part de la
    clé (ou du plafond de la ligne à part) : arrêt n° 12, première clause. Égal : permis."""
    if not isinstance(cumul, CumulParCle) or cumul.table_sha256 != table.sha256:
        raise TableRefusee("le cumul n'est pas celui de cette table")
    compte = table.compte_de(cle)
    limite = table.plafond_ligne_micro if table.marque == MARQUE_LIGNE_A_PART else parts_micro[cle]
    deja, vol = cumul.cumul(compte), cumul.en_vol(compte)
    if deja + vol + pire_micro > limite:
        quoi = "plafond de la ligne à part atteint pour cet appel" if table.marque == MARQUE_LIGNE_A_PART \
            else "part épuisée pour cet appel"
        raise ArretPartCle(CLAUSE_PART, cle, quoi, role=role, cumul_micro=deja, en_vol_micro=vol, pire_micro=pire_micro,
                           limite_micro=limite)
    return compte


__all__ = ("TableRolesCles", "EntreeRole", "Cle", "TableRefusee", "EmpreinteTableDifferente", "ArretPartCle",
           "MontantRefuse", "CumulParCle", "lire_table", "charger_table", "lire_parts", "lire_pires", "verifier_part",
           "micro_exact", "micro_cout", "usd", "CLE_HORS_COURSE", "MARQUES")
