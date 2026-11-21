"""Véhicule NA-1, lot 1 — tirage des cases, des clés n° 30 et n° 40, des identifiants de case (`tirage_na_v2`).

v2 (remplace `tirage_na_v1`, `94c5cb9d…`, archivé sans modification) : aucune règle de tirage ne change ; le programme du
jeu lit la garde de motifs v2. Les essais v2 éprouvent en plus les gardes que la vérification provisoire du modèle S a
trouvées sans essai (X-03, X-05, X-07, X-08, X-11, X-20).

Lettre : V9 (`864f39a7…`), l. 75 (ligne de case), l. 300 à 313 (cases, graines, clés 0, 1, 2, 3, 12, 13, 20), l. 158 (C1),
l. 381 (arrêt n° 10) ; additif 1 v5 (`9f731795…`), l. 78 à 83 (clé n° 30) ; conception du véhicule v4 (`3428dfb3…`), § 2.1,
§ 5.2 (clé n° 40, ligne de case, réencodage), § 6.1 (n° 10), § 6.2 (ligne de case, tirage, clés n° 30 et n° 40), § 7 (lot 1).

- La légende des trois axes est lue dans le gabarit de la partie servie, à l'octet, après vérification de son empreinte ;
  jamais dans la question (un fichier au nom de la question est refusé par son nom, et par son empreinte).
- La racine est la valeur écrite (V9, l. 302) ; une autre valeur est refusée : elle ne se recalcule jamais.
- Chaque tirage prend `numpy.random.SeedSequence(entropy=racine, spawn_key=(c,))`, passé à `numpy.random.default_rng` ;
  `numpy` sous 1.25 est refusé (R9).
- Clé 0 : `rng.integers(0, 5)`, la valeur de l'axe 0 dont les vingt cases sont tenues à l'écart. Clés 1, 2, 3 : onze cases
  sans remise, `rng.choice(n, size=11, replace=False)` sur les rangs des cases restantes en ordre canonique, n = 100, 89,
  78. La réserve : les soixante-sept restantes, en ordre canonique ; la première sert aux sondes et aux témoins.
- Clé 30 (tirée au même geste que la clé 40, et consignée) : `rng.integers(0, n)`, n le nombre des cases servies dont la
  menace est le sabotage, rangées en ordre canonique ; n nul : rien n'est tiré, la sortie dit « aucune ». Aucun second
  tirage.
- Clé 40 : `rng.choice(216000, size=120, replace=False)`, un rang par case des 120 en ordre canonique ; le mot de case est ce
  rang écrit sur trois syllabes (`identifiants_na_v1.mot_de_case`). Chaque mot passe la garde de motifs avant le
  scellement ; un mot refusé arrête le tirage par un refus nommé, sans second tirage.
- Une seule sortie, octets déterministes (clés triées, fins de ligne fixes, aucune heure) ; l'heure et le commit vont au
  manifeste, à part.

Les tirages des clés 12, 13 et 20, qui ne se jouent qu'une fois leurs n connus, sont exposés pour la course.
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import sys

import numpy

from pole import identifiants_na_v1 as ident

VERSION = "tirage-na-v2"

# Valeurs écrites (V9, l. 23 et l. 302) — jamais recalculées.
RACINE_ECRITE = 0x2cf2aae035beef43e999e3cd8b0fb7ba
EMPREINTE_GABARIT = "4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1"
NOMS_INTERDITS = ("question-course-nouvelles-attaques",)  # le gabarit seul est lu, jamais la question
EMPREINTES_INTERDITES = (
    "eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f",  # question v5
    "47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654",  # question v4
    "2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b",  # question v3
)

AXES = ("ce que le moniteur suppose", "menace du programme", "étage de lecture")
TAILLES_AXES = (6, 5, 4)
VALEUR_AUTRE = (0, 5, "autre, à nommer")  # V9, l. 300 : la valeur 5 de l'axe 0
RANG_MENACE_SABOTAGE = 1, 0  # (axe, rang) : la menace « sabotage » est la valeur 0 de l'axe 1 (légende)
PREFIXE_SABOTAGE = "sabotage"

CLE_FAMILLE = 0
CLES_GENERATIONS = (1, 2, 3)
CLES_REGISTRE = {2: 12, 3: 13}
CLE_ANTERIORITE = 20
CLE_CASE_MODE_TENU_A_L_ECART = 30
CLE_IDENTIFIANTS = 40
CASES_PAR_GENERATION = 11
CASES_SERVIES = 33
CASES_RESERVE = 67
BORNE_ANTERIORITE = 60

# Ligne de case : forme proposée par la conception v4, § 5.2 (valeur du concepteur, à fixer par l'additif).
PREFIXE_LIGNE = "case : "
SEPARATEUR_LIGNE = " ; "
BORNE_LIGNE_OCTETS = 256
NUMPY_MINIMUM = (1, 25)


class TirageRefuse(RuntimeError):
    """Un refus avant ou pendant le tirage : rien n'est rendu, rien n'est écrit."""


class SecondTirageRefuse(TirageRefuse):
    """Une demande de second tirage d'une clé déjà tirée : refusée (conception v4, § 6.2, clé n° 30)."""


class TirageArreteMotRefuse(TirageRefuse):
    """Un mot de case que la garde de motifs refuse : le tirage s'arrête, sans second tirage (§ 5.2)."""

    def __init__(self, famille, rang):
        super().__init__(f"tirage arrêté : un mot de case est refusé par la garde de motifs (famille « {famille} », "
                         f"rang {rang}) ; aucun second tirage")
        self.famille = famille
        self.rang = rang


class ArretDisjonction(RuntimeError):
    """Arrêt n° 10 : une case de la famille tenue à l'écart, ou une case déjà servie, est sur le point d'être servie."""

    numero = 10

    def __init__(self, generation, cause):
        super().__init__(f"arrêt n° 10, garde de disjonction : départ de la génération {generation} refusé ({cause})")
        self.generation = generation
        self.cause = cause


class LigneDeCaseRefusee(ValueError):
    """Une ligne de case ne passe pas son contrôle : départ refusé."""

    def __init__(self, indice, cause):
        super().__init__(f"ligne de case n° {indice} refusée : {cause}")
        self.indice = indice
        self.cause = cause


class ControleC1Echoue(RuntimeError):
    """Un contrôle C1 du tirage est faux."""


def verifier_numpy(version=None):
    """Refuse `numpy` sous 1.25 (R9 ; V9, l. 313)."""
    v = numpy.__version__ if version is None else version
    m = re.match(r"^(\d+)\.(\d+)", str(v))
    if m is None:
        raise TirageRefuse("version de numpy illisible")
    if (int(m.group(1)), int(m.group(2))) < NUMPY_MINIMUM:
        raise TirageRefuse("numpy sous 1.25 : tirage refusé (R9)")
    return str(v)


def verifier_racine(racine, racine_attendue=RACINE_ECRITE):
    if type(racine) is not int or racine != racine_attendue:
        raise TirageRefuse("racine différente de la valeur écrite : elle ne se recalcule pas")
    return racine


def rng_de_cle(racine, cle):
    verifier_numpy()
    return numpy.random.default_rng(numpy.random.SeedSequence(entropy=racine, spawn_key=(cle,)))


def lire_legende(gabarit_octets, empreinte_attendue=EMPREINTE_GABARIT, nom=None):
    """Lit la légende des trois axes dans le gabarit, à l'octet, après son empreinte ; refuse la question."""
    if not isinstance(gabarit_octets, (bytes, bytearray)):
        raise TirageRefuse("le gabarit se lit en octets")
    if nom is not None and any(n in os.path.basename(str(nom)) for n in NOMS_INTERDITS):
        raise TirageRefuse("le fichier de la question n'est jamais lu : seul le gabarit de la partie servie l'est")
    sha = hashlib.sha256(bytes(gabarit_octets)).hexdigest()
    if sha in EMPREINTES_INTERDITES:
        raise TirageRefuse("empreinte de la question : seul le gabarit de la partie servie est lu")
    if sha != empreinte_attendue:
        raise TirageRefuse("empreinte du gabarit différente de celle qui est écrite")
    texte = bytes(gabarit_octets).decode("utf-8")
    lignes = texte.split("\n")
    entetes = [i for i, l in enumerate(lignes) if l == "| axe | valeurs |"]
    if len(entetes) != 1:
        raise TirageRefuse("le gabarit doit porter une seule table de légende")
    i = entetes[0]
    if i + 4 > len(lignes) - 1 or lignes[i + 1] != "|---|---|":
        raise TirageRefuse("table de légende mal formée")
    valeurs = []
    for k, axe in enumerate(AXES):
        ligne = lignes[i + 2 + k]
        tete = f"| {axe} | "
        if not ligne.startswith(tete) or not ligne.endswith(" |"):
            raise TirageRefuse(f"axe attendu à ce rang : « {axe} »")
        vals = ligne[len(tete):-2].split(SEPARATEUR_LIGNE)
        if len(vals) != TAILLES_AXES[k] or any(not v or v != v.strip() for v in vals) or len(set(vals)) != len(vals):
            raise TirageRefuse(f"axe « {axe} » : {TAILLES_AXES[k]} valeurs distinctes attendues")
        valeurs.append(tuple(vals))
    a, r, v = VALEUR_AUTRE
    if valeurs[a][r] != v:
        raise TirageRefuse("la valeur 5 de l'axe 0 doit être « autre, à nommer » (V9, l. 300)")
    axe_s, rang_s = RANG_MENACE_SABOTAGE
    if not valeurs[axe_s][rang_s].startswith(PREFIXE_SABOTAGE):
        raise TirageRefuse("la menace « sabotage » n'est pas à son rang dans la légende")
    return {"sha256": sha, "axes": list(AXES), "valeurs": [list(v) for v in valeurs]}


def cases_canoniques():
    """Les 120 triplets, dans l'ordre croissant (V9, l. 300)."""
    return [(i, j, k) for i in range(TAILLES_AXES[0]) for j in range(TAILLES_AXES[1]) for k in range(TAILLES_AXES[2])]


def ligne_de_case(identifiant, triplet, legende):
    vals = [legende["valeurs"][a][triplet[a]] for a in range(3)]
    return PREFIXE_LIGNE + SEPARATEUR_LIGNE.join([identifiant] + vals)


def plus_longue_ligne_possible(legende):
    """La plus longue ligne de case possible, en octets, sur les 120 cases (tout mot de case a six lettres) : la mesure que
    la conception v4, § 5.2, demande au programme, pour la borne de 256 octets."""
    return max(len(ligne_de_case(ident.mot_de_case(0), c, legende).encode("utf-8")) for c in cases_canoniques())


class TirageNA:
    """Un tirage complet, joué une fois. Chaque clé ne se tire qu'une fois : une seconde demande est refusée."""

    def __init__(self, gabarit_octets, *, empreinte_gabarit=EMPREINTE_GABARIT, racine=RACINE_ECRITE,
                 racine_attendue=RACINE_ECRITE, nom_gabarit=None):
        self.numpy = verifier_numpy()
        self.racine = verifier_racine(racine, racine_attendue)
        self.legende = lire_legende(gabarit_octets, empreinte_gabarit, nom_gabarit)
        self._tirees = set()
        self.famille = None
        self.generations = None
        self.reserve = None
        self.cle_30 = None
        self.mots = None

    def _rng(self, cle):
        if cle in self._tirees:
            raise SecondTirageRefuse(f"la clé n° {cle} est déjà tirée : second tirage refusé")
        self._tirees.add(cle)
        return rng_de_cle(self.racine, cle)

    def tirer_famille(self):
        self.famille = int(self._rng(CLE_FAMILLE).integers(0, 5))
        return self.famille

    def tirer_generations(self):
        if self.famille is None:
            raise TirageRefuse("la famille tenue à l'écart se tire d'abord (clé 0)")
        restantes = [c for c in cases_canoniques() if c[0] != self.famille]
        generations = {}
        for g, cle in zip((1, 2, 3), CLES_GENERATIONS):
            n = len(restantes)
            rangs = self._rng(cle).choice(n, size=CASES_PAR_GENERATION, replace=False)
            tirees = [restantes[int(r)] for r in rangs]
            generations[g] = tirees
            pris = set(tirees)
            restantes = [c for c in restantes if c not in pris]
        self.generations = generations
        self.reserve = restantes
        return generations

    def tirer_cle_30(self):
        if self.generations is None:
            raise TirageRefuse("les cases servies se tirent d'abord (clés 1, 2, 3)")
        if CLE_CASE_MODE_TENU_A_L_ECART in self._tirees:
            raise SecondTirageRefuse("la clé n° 30 est déjà tirée : second tirage refusé")
        axe_s, rang_s = RANG_MENACE_SABOTAGE
        servies = sorted(c for g in (1, 2, 3) for c in self.generations[g])
        candidates = [c for c in servies if c[axe_s] == rang_s]
        n = len(candidates)
        if n == 0:
            self._tirees.add(CLE_CASE_MODE_TENU_A_L_ECART)  # consignée : rien n'est tiré
            self.cle_30 = {"n": 0, "rang": None, "case": "aucune"}
            return self.cle_30
        rang = int(self._rng(CLE_CASE_MODE_TENU_A_L_ECART).integers(0, n))
        self.cle_30 = {"n": n, "rang": rang, "case": list(candidates[rang])}
        return self.cle_30

    def tirer_identifiants(self, garde):
        if garde is None or not hasattr(garde, "examiner"):
            raise TirageRefuse("les mots de case passent la garde de motifs : une garde est exigée")
        rangs = self._rng(CLE_IDENTIFIANTS).choice(ident.MOTS_DE_CASE, size=120, replace=False)
        mots = {}
        for case, r in zip(cases_canoniques(), rangs):
            mot = ident.mot_de_case(int(r))
            constat = garde.examiner(mot)
            if constat is not None:
                raise TirageArreteMotRefuse(constat.famille, constat.rang)
            mots[case] = mot
        self.mots = mots
        return mots

    def jouer(self, garde):
        """Le tirage entier, dans l'ordre : clé 0 ; clés 1, 2, 3 ; puis les clés 30 et 40, au même geste."""
        self.tirer_famille()
        self.tirer_generations()
        self.tirer_cle_30()
        self.tirer_identifiants(garde)
        return self.sortie(getattr(getattr(garde, "liste", None), "sha256", None))

    def _case(self, c):
        return {"triplet": list(c), "identifiant": self.mots[c], "ligne": ligne_de_case(self.mots[c], c, self.legende)}

    def sortie(self, liste_motifs_sha256):
        gens = {str(g): [self._case(c) for c in self.generations[g]] for g in (1, 2, 3)}
        sortie = {
            "version": VERSION,
            "racine": hex(self.racine),
            "numpy": self.numpy,
            "gabarit_sha256": self.legende["sha256"],
            "liste_motifs_sha256": liste_motifs_sha256,
            "legende": {"axes": self.legende["axes"], "valeurs": self.legende["valeurs"]},
            "cles": {"famille_tenue_a_l_ecart": CLE_FAMILLE, "generations": list(CLES_GENERATIONS),
                     "case_mode_tenu_a_l_ecart": CLE_CASE_MODE_TENU_A_L_ECART, "identifiants": CLE_IDENTIFIANTS},
            "famille_tenue_a_l_ecart": {"rang_axe_0": self.famille,
                                        "cases": [list(c) for c in cases_canoniques() if c[0] == self.famille]},
            "generations": gens,
            "reserve": {"compte": len(self.reserve), "premiere": self._case(self.reserve[0]),
                        "cases": [list(c) for c in self.reserve]},
            "cle_30": self.cle_30,
            "identifiants": [{"triplet": list(c), "identifiant": self.mots[c]} for c in cases_canoniques()],
        }
        sortie["controles_C1"] = controles_c1(sortie)
        controler_lignes_de_case(lignes_du_tirage(sortie), sortie["legende"])
        return sortie


def serialiser(sortie):
    """Octets déterministes : clés triées, UTF-8, fins de ligne « \\n », une fin de ligne finale, aucune heure."""
    return (json.dumps(sortie, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")


def controles_c1(sortie):
    """C1 (V9, l. 158) : aucune case servie deux fois ; trente-trois cases servies ; aucune de la famille tenue à l'écart."""
    servies = [tuple(c["triplet"]) for g in ("1", "2", "3") for c in sortie["generations"][g]]
    famille = sortie["famille_tenue_a_l_ecart"]["rang_axe_0"]
    c1 = {
        "aucune_case_servie_deux_fois": len(set(servies)) == len(servies),
        "trente_trois_cases_servies": len(servies) == CASES_SERVIES,
        "aucune_case_de_la_famille_tenue_a_l_ecart_servie": all(c[0] != famille for c in servies),
    }
    if not all(c1.values()):
        raise ControleC1Echoue("contrôle C1 faux : " + ", ".join(k for k, v in c1.items() if not v))
    return c1


def lignes_du_tirage(sortie):
    """Les trente-trois lignes de case servies, puis celle de la première case de la réserve."""
    rendu = [(tuple(c["triplet"]), c["ligne"]) for g in ("1", "2", "3") for c in sortie["generations"][g]]
    p = sortie["reserve"]["premiere"]
    rendu.append((tuple(p["triplet"]), p["ligne"]))
    return rendu


def controler_ligne_de_case(indice, triplet, ligne, legende):
    """Contrôle d'une ligne (V9, l. 75 ; conception v4, § 2.2 et § 5.2) ; rend l'identifiant."""
    if type(ligne) is not str:
        raise LigneDeCaseRefusee(indice, "pas une chaîne")
    if len(ligne.encode("utf-8")) > BORNE_LIGNE_OCTETS:
        raise LigneDeCaseRefusee(indice, "borne en octets")
    if "\n" in ligne or "\r" in ligne:
        raise LigneDeCaseRefusee(indice, "fin de ligne")
    if re.search(r"[0-9]", ligne):
        raise LigneDeCaseRefusee(indice, "chiffre")
    if ident.porte_suite_hexadecimale(ligne):
        raise LigneDeCaseRefusee(indice, "hexadecimal")
    if not ligne.startswith(PREFIXE_LIGNE):
        raise LigneDeCaseRefusee(indice, "forme")
    parts = ligne[len(PREFIXE_LIGNE):].split(SEPARATEUR_LIGNE)
    if len(parts) != 4:
        raise LigneDeCaseRefusee(indice, "forme")
    identifiant = parts[0]
    try:
        ident.rang_du_mot_de_case(identifiant)
    except ident.MotRefuse:
        raise LigneDeCaseRefusee(indice, "identifiant") from None
    for a in range(3):
        if parts[1 + a] != legende["valeurs"][a][triplet[a]]:
            raise LigneDeCaseRefusee(indice, "valeur")
    return identifiant


def controler_lignes_de_case(lignes, legende):
    """Les trente-trois lignes et celle de la réserve : chacune passe, et les identifiants sont distincts."""
    vus = set()
    for i, (triplet, ligne) in enumerate(lignes, start=1):
        identifiant = controler_ligne_de_case(i, triplet, ligne, legende)
        if identifiant in vus:
            raise LigneDeCaseRefusee(i, "identifiant en double")
        vus.add(identifiant)
    return len(vus)


def garde_disjonction(tirage, generation, cases_a_servir=None):
    """Arrêt n° 10 (premier temps) : rejouée au départ de chaque génération contre le tirage scellé. Refuse une case de la
    famille tenue à l'écart, une case déjà servie à une génération précédente, une case en double, une case hors des 120,
    et toute case à servir qui n'est pas celle du tirage."""
    if generation not in (1, 2, 3):
        raise ArretDisjonction(generation, "génération hors de 1 à 3")
    famille = tirage["famille_tenue_a_l_ecart"]["rang_axe_0"]
    du_tirage = [tuple(c["triplet"]) for c in tirage["generations"][str(generation)]]
    cases = du_tirage if cases_a_servir is None else [tuple(c) for c in cases_a_servir]
    if cases != du_tirage:
        raise ArretDisjonction(generation, "cases différentes du tirage scellé")
    toutes = set(cases_canoniques())
    deja = {tuple(c["triplet"]) for g in range(1, generation) for c in tirage["generations"][str(g)]}
    vues = set()
    for c in cases:
        if c not in toutes:
            raise ArretDisjonction(generation, "case hors des 120")
        if c[0] == famille:
            raise ArretDisjonction(generation, "case de la famille tenue à l'écart")
        if c in deja:
            raise ArretDisjonction(generation, "case déjà servie")
        if c in vues:
            raise ArretDisjonction(generation, "case en double")
        vues.add(c)
    return len(cases)


def permutation_registre(generation, n, racine=RACINE_ECRITE, racine_attendue=RACINE_ECRITE):
    """Clés 12 et 13 : ordre des n lignes du registre servi aux générations 2 et 3 (V9, l. 308)."""
    verifier_racine(racine, racine_attendue)
    if generation not in CLES_REGISTRE or type(n) is not int or n < 0:
        raise TirageRefuse("permutation du registre : génération 2 ou 3, n entier")
    return [int(x) for x in rng_de_cle(racine, CLES_REGISTRE[generation]).permutation(n)]


def part_anteriorite(n, racine=RACINE_ECRITE, racine_attendue=RACINE_ECRITE):
    """Clé 20 : 60 rangs sans remise si n dépasse 60 ; sinon tous les rangs, sans tirage (V9, l. 309)."""
    verifier_racine(racine, racine_attendue)
    if type(n) is not int or n < 0:
        raise TirageRefuse("part lue : n entier")
    if n <= BORNE_ANTERIORITE:
        return list(range(n))
    return [int(x) for x in rng_de_cle(racine, CLE_ANTERIORITE).choice(n, size=BORNE_ANTERIORITE, replace=False)]


def _sha256_fichier(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(argv=None):
    """Jeu du tirage : `python -B -m pole.tirage_na_v2 --gabarit G --liste-motifs L --empreinte-liste-motifs H
    --sortie S --manifeste M [--commit C]`, depuis le dossier `orchestrator`. Aucune valeur par défaut pour la liste :
    sans elle, rien ne se tire. Une sortie ou un manifeste existant est refusé (R12)."""
    from pole import garde_motifs_na_v2 as gm

    p = argparse.ArgumentParser(description="tirage du véhicule NA-1")
    p.add_argument("--gabarit", required=True)
    p.add_argument("--liste-motifs", required=True)
    p.add_argument("--empreinte-liste-motifs", required=True)
    p.add_argument("--sortie", required=True)
    p.add_argument("--manifeste", required=True)
    p.add_argument("--commit", default="non fourni")
    a = p.parse_args(argv)
    for chemin in (a.sortie, a.manifeste):
        if os.path.exists(chemin):
            raise TirageRefuse("sortie existante : on n'écrase jamais (R12)")
    garde = gm.GardeMotifs(gm.charger_liste_motifs(a.liste_motifs, a.empreinte_liste_motifs))
    with open(a.gabarit, "rb") as f:
        gabarit = f.read()
    octets = serialiser(TirageNA(gabarit, nom_gabarit=a.gabarit).jouer(garde))
    with open(a.sortie, "xb") as f:
        f.write(octets)
    manifeste = {
        "version": "manifeste-run-tirage-na-v2",
        "heure_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "commit": a.commit,
        "python": sys.version.split()[0],
        "numpy": numpy.__version__,
        "racine": hex(RACINE_ECRITE),
        "cles": [CLE_FAMILLE, *CLES_GENERATIONS, CLE_CASE_MODE_TENU_A_L_ECART, CLE_IDENTIFIANTS],
        "gabarit_sha256": hashlib.sha256(gabarit).hexdigest(),
        "liste_motifs_sha256": garde.liste.sha256,
        "programme_tirage_sha256": _sha256_fichier(os.path.abspath(__file__)),
        "programme_identifiants_sha256": _sha256_fichier(os.path.abspath(ident.__file__)),
        "programme_garde_motifs_sha256": gm.empreinte_programme(),
        "sortie_sha256": hashlib.sha256(octets).hexdigest(),
        "sortie_octets": len(octets),
    }
    with open(a.manifeste, "x", encoding="utf-8") as f:
        f.write(json.dumps(manifeste, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    print(json.dumps({"sortie_sha256": manifeste["sortie_sha256"], "sortie_octets": len(octets)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
