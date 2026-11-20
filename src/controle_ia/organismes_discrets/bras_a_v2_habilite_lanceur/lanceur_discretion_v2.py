"""Lanceur de l'étape de discrétion du bras A des organismes discrets, côté moniteurs — version 2.

Version 2, après la contre-lecture habilitée de la version 1 (`docs/notes/bras-a-moniteurs-v1/contre-lecture-habilitee-
lanceur-discretion-v1.md`, ae7618d1…, partie 6, C1 à C11) et deux décisions de la mère :
- C1, C2 : la reprise est comptée et inscrite à **chaque** relance après l'engagement de la table (un relevé scellé par
  relance, sous `production/reprises/`, jamais dans le dossier des morceaux) ;
- C3 : la pièce source de la base et ses modules gelés sont vérifiés à l'étape 1, avant toute production ;
- C4 : la configuration de la base relue à l'étape de discrétion est celle que désigne la ligne `CONFIG-BRAS-A-V2` ;
- C5 : quatre modules de plus cités par empreinte (chargement des modèles, format de conversation, lecture du score,
  logits de la dernière position) ;
- C6 : `relever-fins` accepte une configuration dont seuls les jetons de fin sont nuls ;
- C7 : un énoncé bordé de blancs est refusé (l'agent le voit sans eux) ;
- C8 : gardes éprouvées par artefact (essais) ; une relecture redondante de la table devient une assertion ;
- C9 : le manifeste du lanceur porte les versions, le commit du code et les réglages de déterminisme de la carte ;
- C11 : les empreintes des fichiers sont vérifiées avant l'import du module d'entrée ;
- remarque 4 : le nom du manifeste du lanceur porte l'identifiant de l'exécution ;
- décision de la mère (1) : **toutes les sorties de lecture** de chaque moniteur (identifiants générés, états, masse,
  jetons, score) sont écrites et scellées dès leur production, par morceau, sous `production/lectures-completes-
  <moniteur>/`, sous identifiants opaques ; aucune étape ne les lit, hors la reprise d'un morceau dont seule la lecture
  complète a été scellée ;
- décision de la mère (2) : les clés neuves du bras A (engagement, manifestes de production, reprises) vont dans un
  registre propre au bras, `registre_du_bras` de la configuration ; le registre des scellements garde les clés de la
  base (`CONFIG-BRAS-A-V2`, `TABLE-B-BRAS-A-V2`, `ISSUE-MOTS-ET-COUT-BRAS-A`) et le journal des ouvertures.

Version 1 :

Écrit d'après l'extrait du lanceur pour le développeur habilité, v3 (`docs/notes/relance-organismes-discrets-v1/
extrait-lanceur-etape-discretion-pour-le-developpeur-v3.md`, `5d2a48c0…`), demande 18 de la relance. Il n'importe, du
code de la relance, que le module d'entrée (`entree_lanceur_discretion_bras_a_v2`, `cb668bb9…`), par les noms que
l'extrait donne.

Trois sous-commandes, parce que la base « mots et coût » exige, entre l'extraction et elle, un arbre de dépôt propre et
la ligne `CONFIG-BRAS-A-V2` versée, et, entre elle et les autres moniteurs, la ligne `ISSUE-MOTS-ET-COUT-BRAS-A` inscrite
après sa lecture ; ces versements et cette lecture sont faits par la session principale, hors du lanceur :

- `extraire` : extraction des six conditions lues pour la base (`extraction_base_v2`), sous un dossier neuf de la
  racine ; inscrit la ligne `CONFIG-BRAS-A-V2` qui désigne la configuration écrite ;
- `base` : la base, par son lanceur inscrit (`scripts/lancer_mots_et_cout_bras_a_v2.sh --mode reel`) ;
- `discretion` : les six étapes de l'extrait, **en une seule exécution**, sans rendre la main entre la production des
  scores, les ouvertures et la lecture commune :
  1. garde de production (`TABLE-B-BRAS-A-V2` et `ISSUE-MOTS-ET-COUT-BRAS-A` au registre), sinon refus ;
  2. table des identifiants opaques : entropie propre prise au système, admise par le module d'entrée avant le tirage
     (écart à R9 accordé, GO-2026-11-19-97) ; fichier de la table scellé dans le dossier tenu à part ; son empreinte,
     l'engagement, inscrite au registre, datée, avant toute production ;
  3. préparation (`preparation_des_lectures_v3`) : seule à lire les textes des actions et la table ; **aucune position
     tirée** ; fichiers de demandes à trois champs dans le dossier des demandes, bilans dans le dossier à part ;
  4. production des deux moniteurs à modèle de langue (`moniteurs_langue_v3`), sur le seul fichier des demandes, avec
     la consigne et l'engagement, dans l'ordre des identifiants opaques, par morceaux d'un lot scellés dès leur
     production ; garde de production appelée juste avant le premier appel ; manifeste de production scellé et inscrit
     au registre dès son écriture ;
  5. cinq lignes `OUVERTURE-MONITEUR-BRAS-A` au journal (`autres_moniteurs_v11.inscrire_ouverture`), l'empreinte des
     scores étant lue au manifeste de production ;
  6. lecture commune (`autres_moniteurs_v11.lire_les_cinq`), seule à rouvrir la table, avec l'entropie de la
     configuration du bras ; sortie et fichier des rangs dans deux dossiers disjoints.

Écriture : chaque fichier que le lanceur scelle s'écrit sous un dossier provisoire (`.provisoire/<exécution>`, dans son
dossier final), y est scellé, puis passe à son nom, le compagnon d'abord, le fichier ensuite : une panne ne laisse
jamais, sous un nom attendu, un fichier sans compagnon. Un reste provisoire n'est lu ni écrasé par aucune étape. Rien
n'est supprimé ni écrasé. Les fichiers que les modules appelés écrivent eux-mêmes (table, demandes, bilans, production,
extraction, rangs, sortie) le sont sous ce dossier provisoire, puis posés de même.

Reprise après une panne de transport : les morceaux de scores déjà produits restent scellés, sans être ouverts ; la
reprise est comptée et inscrite au registre (`REPRISE-PRODUCTION-BRAS-A`) ; seuls les morceaux restés sans réponse sont
redemandés. Aucune reprise n'est permise après une ligne d'ouverture d'un des cinq moniteurs.

Le lanceur ne joue aucun épisode de l'agent : la garde d'équivalence du jeu d'épisodes ne le concerne pas. Il ne tire
lui-même aucune graine : les graines des lectures sont dérivées par la préparation de l'entropie de la configuration du
bras, celles de la lecture commune par elle-même, de la même entropie ; seule la table a son entropie propre.

    PYTHONPATH=src python -B -m controle_ia.organismes_discrets.bras_a_v2_habilite_lanceur.lanceur_discretion_v2 \\
        {extraire|base|discretion} --racine DEPOT --config CONFIG.json
    ... relever-fins --racine DEPOT --config CONFIG.json     (jetons de fin du moniteur boîte noire, sans les poids)
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import importlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ... import manifeste as manifeste_du_depot
from ...gardes import GardeArret
from ...scellement import sceller
from ..bras_a_v2_habilite import autres_moniteurs_v11 as A
from ..bras_a_v2_habilite import extraction_base_v2 as X
from ..bras_a_v2_habilite import moniteurs_langue_v3 as ML
from ..bras_a_v2_habilite_preparation import preparation_des_lectures_v3 as P

VERSION = "lanceur-discretion-bras-a-v2"
MODULE_D_ENTREE = "controle_ia.organismes_discrets.entree_lanceur_discretion_bras_a_v2"
# Tout ce que le lanceur appelle, par chemin sous la racine : la configuration scellée en donne l'empreinte entière.
MODULES_APPELES = {
    "entree": "src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v2.py",
    "lecture_commune": "src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v11.py",
    "moniteurs_a_modele_de_langue": "src/controle_ia/organismes_discrets/bras_a_v2_habilite/moniteurs_langue_v3.py",
    "extraction": "src/controle_ia/organismes_discrets/bras_a_v2_habilite/extraction_base_v2.py",
    "preparation": "src/controle_ia/organismes_discrets/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py",
    "base": "scripts/mots_et_cout_bras_a_v2.py",
    "lanceur_de_la_base": "scripts/lancer_mots_et_cout_bras_a_v2.sh",
    "piece_source": "scripts/mots_et_cout_t06_v3.py",
    "consigne": ML.CONSIGNE_CHEMIN,
    "chargement_des_modeles": "src/controle_ia/harnais/modeles.py",
    "format_de_conversation": "src/controle_ia/harnais/formats.py",
    "lecture_du_score": "src/controle_ia/bases/scores_jetons.py",
    "derniere_position": "src/controle_ia/environnements/pilote_a.py",
}
IMPORTES = {"lecture_commune": A, "moniteurs_a_modele_de_langue": ML, "extraction": X, "preparation": P}
CLES_CONFIG = ("version", "mode", "texte_scelle", "go_de_lazar", "registre", "registre_du_bras", "registre_des_accords",
               "registre_des_accords_fige", "modules", "rejeu", "configuration_du_bras", "taches", "permutation",
               "forme_du_fichier_par_unite", "statistique_agregateur", "n_permutations", "n_tirages", "dossiers",
               "lecture", "chargement", "fins_moniteur_boite_noire")
DOSSIERS = ("extraction", "a_part", "demandes", "production", "rangs", "sortie", "lanceur")
CLES_CHARGEMENT = ("dtype", "attention", "hors_ligne", "cache", "variables_gabarit")
MODES = ("reel", "jouet")
PROVISOIRE = ".provisoire"
CLE_CONFIG_BRAS = "CONFIG-BRAS-A-V2"
CLE_ENGAGEMENT = "ENGAGEMENT-TABLE-OPAQUE-BRAS-A"
CLE_MANIFESTE = {A.BOITE_NOIRE: "MANIFESTE-PRODUCTION-BRAS-A-MONITEUR-BOITE-NOIRE",
                 A.JUGE: "MANIFESTE-PRODUCTION-BRAS-A-JUGE"}
CLE_REPRISE = "REPRISE-PRODUCTION-BRAS-A"
ORDRE_DES_OUVERTURES = (A.LEXICAL, A.SURFACE, A.BOITE_NOIRE, A.AGREGATEUR, A.JUGE)
_SHA = re.compile(r"^[0-9a-f]{64}$")
_COMMIT = re.compile(r"^[0-9a-f]{40}$")
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
_MORCEAU = re.compile(r"^morceau-(\d{5})\.jsonl$")
# Une sortie de lecture complète, telle que la rend `moniteurs_langue_v3.lire_avec_raisonnement` : ces champs, tous.
CHAMPS_LECTURE_COMPLETE = ("cle", "balise", "jointure", "jointure_de_la_coupe", "jetons_contexte", "jetons_generes",
                           "ids_generes", "cas", "score", "masse", "masse_faible", "anomalie")
ENTETE_DU_REGISTRE_DU_BRAS = ("# Registre du bras A des organismes discrets (étape de discrétion) — lignes ajoutées, "
                              "jamais réécrites\n\n| clé | date | chemin | sha256 |\n|---|---|---|---|\n")


# ============================================================================================ outils de fichier
def _sha(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def _scelle(chemin: Path, attendu: str | None = None) -> str:
    """Empreinte d'un fichier scellé : fichier et compagnon présents, égaux (et égaux à `attendu` s'il est donné)."""
    chemin = Path(chemin)
    compagnon = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not compagnon.is_file():
        raise GardeArret(f"{chemin.name} : fichier ou compagnon absent")
    vue = _sha(chemin)
    if compagnon.read_text(encoding="utf-8").split()[:1] != [vue]:
        raise GardeArret(f"{chemin.name} : empreinte ≠ compagnon")
    if attendu is not None and vue != attendu:
        raise GardeArret(f"{chemin.name} : empreinte ≠ celle attendue (configuration scellée ou registre)")
    return vue


# Chaque exécution écrit ses provisoires dans un sous-dossier à elle : un reste d'une exécution interrompue n'est ni lu
# ni écrasé par la suivante.
EXECUTION = f"{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{os.getpid()}"


def provisoire(dossier: Path) -> Path:
    return Path(dossier) / PROVISOIRE / EXECUTION


def poser(dossier: Path, nom: str) -> Path:
    """Fait passer un fichier scellé de `dossier/.provisoire/<exécution>/nom` à `dossier/nom` : le compagnon d'abord,
    puis le fichier. Une pose de la même exécution interrompue entre les deux (compagnon posé, fichier encore
    provisoire, même empreinte) est achevée ; toute autre présence sous le nom final est refusée (R12)."""
    dossier = Path(dossier)
    src, final = provisoire(dossier) / nom, dossier / nom
    src_c, final_c = Path(str(src) + ".sha256"), Path(str(final) + ".sha256")
    if final.exists():
        raise GardeArret(f"{final.name} existe déjà sous son nom final : on n'écrase jamais (R12)")
    if final_c.exists():
        if not (src.is_file() and final_c.read_text(encoding="utf-8").split()[:1] == [_sha(src)]):
            raise GardeArret(f"{final_c.name} posé sans son fichier, qui n'est pas le provisoire : arrêt")
    else:
        _scelle(src)
        os.rename(src_c, final_c)
    os.rename(src, final)
    _scelle(final)
    return final


# ============================================================================================ registre
def _maintenant() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lignes_du_registre(registre: Path, cle: str, *, absent_permis: bool = False) -> list[dict]:
    """Lignes `| CLÉ | date | chemin | sha256 |` de la clé donnée. `absent_permis` : le registre du bras, créé à sa
    première ligne, peut ne pas exister encore (aucune ligne)."""
    registre = Path(registre)
    if not registre.is_file():
        if absent_permis:
            return []
        raise GardeArret(f"registre {registre.name} absent")
    sortie = []
    for l in registre.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) == 4 and c[0] == cle and _DATE.fullmatch(c[1]):
            sortie.append({"cle": c[0], "date": c[1], "chemin": c[2], "sha256": c[3]})
    return sortie


def inscrire(registre: Path, cle: str, chemin: str, sha: str, *, unique: bool = True, creer: bool = False) -> str:
    """Ajoute une ligne datée au registre ; jamais réécrite. `unique` : refus si la clé y est déjà. `creer` : le
    registre du bras est créé, avec son en-tête, à sa première ligne."""
    if not (_SHA.fullmatch(sha) and chemin and "|" not in chemin and "\n" not in chemin):
        raise GardeArret(f"ligne {cle} : chemin ou empreinte hors format")
    if unique and lignes_du_registre(registre, cle, absent_permis=creer):
        raise GardeArret(f"registre : ligne {cle} déjà inscrite : jamais réécrite")
    registre = Path(registre)
    if creer and not registre.exists():
        registre.parent.mkdir(parents=True, exist_ok=True)
        registre.write_text(ENTETE_DU_REGISTRE_DU_BRAS, encoding="utf-8")
    ligne = f"| {cle} | {_maintenant()} | {chemin} | {sha} |"
    with open(registre, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    return ligne


def _relatif(racine: Path, chemin: Path) -> str:
    return Path(chemin).resolve().relative_to(Path(racine).resolve()).as_posix()


# ============================================================================================ configuration
def _chemin_relatif(x, quoi: str) -> str:
    if not (isinstance(x, str) and x and not x.startswith("/") and ".." not in Path(x).parts):
        raise GardeArret(f"configuration : {quoi} : chemin relatif à la racine, sans « .. », attendu")
    return x


def _fichier_cite(x, quoi: str) -> dict:
    if not (isinstance(x, dict) and set(x) == {"chemin", "sha256"} and isinstance(x["sha256"], str)
            and _SHA.fullmatch(x["sha256"])):
        raise GardeArret(f"configuration : {quoi} : {{chemin, sha256}} attendu, empreinte entière en minuscules")
    _chemin_relatif(x["chemin"], quoi)
    return x


def exiger_dossiers_disjoints(dossiers: dict[str, Path]) -> None:
    """Les dossiers du lanceur sont deux à deux disjoints : ni l'un égal à l'autre, ni l'un dans l'autre."""
    vus = [(n, Path(d).resolve()) for n, d in dossiers.items()]
    for i, (n1, d1) in enumerate(vus):
        for n2, d2 in vus[i + 1:]:
            if d1 == d2 or d1 in d2.parents or d2 in d1.parents:
                raise GardeArret(f"configuration : dossiers « {n1} » et « {n2} » : disjoints exigés")


def lire_la_configuration(chemin: Path, *, cli: bool = False, fins_a_relever: bool = False) -> tuple[dict, str]:
    """Configuration scellée du lanceur : compagnon vérifié ; clés fermées ; aucune valeur à fixer laissée nulle. Mode
    réel : 2 000 permutations et 2 000 tirages. Les deux modes exigent l'échange par paire et la forme « rang ».
    `fins_a_relever` (sous-commande `relever-fins` seule) : les jetons de fin du moniteur boîte noire peuvent être nuls ;
    la configuration de relevé et la configuration finale portent deux noms (R12)."""
    sha = _scelle(Path(chemin))
    c = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if not isinstance(c, dict) or tuple(c) != CLES_CONFIG:
        raise GardeArret(f"configuration : clés {list(CLES_CONFIG)} attendues, dans cet ordre, aucune autre")
    nulles = [k for k, v in c.items() if v is None and not (fins_a_relever and k == "fins_moniteur_boite_noire")]
    if nulles:
        raise GardeArret(f"configuration : valeurs à fixer laissées nulles : {nulles}")
    if c["version"] != VERSION or c["mode"] not in MODES or (cli and c["mode"] != "reel"):
        raise GardeArret(f"configuration : version {VERSION} et mode réel attendus (le mode jouet ne sert qu'aux essais)")
    _fichier_cite(c["texte_scelle"], "texte scellé")
    if not (isinstance(c["go_de_lazar"], str) and re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", c["go_de_lazar"])):
        raise GardeArret("configuration : identifiant de la ligne d'accord hors format")
    for k in ("registre", "registre_du_bras", "registre_des_accords"):
        _chemin_relatif(c[k], k)
    if len({Path(c[k]).as_posix() for k in ("registre", "registre_du_bras", "registre_des_accords")}) != 3:
        raise GardeArret("configuration : registre des scellements, registre du bras et registre des accords : "
                         "trois fichiers distincts attendus")
    f = c["registre_des_accords_fige"]
    if not (isinstance(f, dict) and set(f) == {"chemin", "sha256", "commit"} and isinstance(f["commit"], str)
            and _COMMIT.fullmatch(f["commit"])):
        raise GardeArret("configuration : registre des accords figé {chemin, sha256, commit} attendu")
    _fichier_cite({"chemin": f["chemin"], "sha256": f["sha256"]}, "registre des accords figé")
    if not (isinstance(c["modules"], dict) and set(c["modules"]) == set(MODULES_APPELES.values())
            and all(isinstance(s, str) and _SHA.fullmatch(s) for s in c["modules"].values())):
        raise GardeArret("configuration : modules appelés : chacun par son empreinte entière en minuscules, tous, "
                         "aucun autre")
    for k in ("rejeu", "configuration_du_bras", "taches"):
        _fichier_cite(c[k], k)
    if c["permutation"] != A.PERMUTATION_PAR_PAIRE:
        raise GardeArret(f"configuration : schéma de permutation « {A.PERMUTATION_PAR_PAIRE} » attendu")
    if c["forme_du_fichier_par_unite"] != "rang":
        raise GardeArret("configuration : fichier par unité en forme « rang » attendu")
    if c["statistique_agregateur"] not in A.STATISTIQUES_EPISODE:
        raise GardeArret("configuration : statistique de l'agrégateur hors de sa liste")
    for k in ("n_permutations", "n_tirages"):
        if not (isinstance(c[k], int) and not isinstance(c[k], bool) and c[k] >= 1):
            raise GardeArret(f"configuration : {k} entier ≥ 1 attendu")
    if c["mode"] == "reel" and (c["n_permutations"], c["n_tirages"]) != (A.N_PERMUTATIONS, A.N_TIRAGES):
        raise GardeArret(f"configuration : mode réel : {A.N_PERMUTATIONS} permutations et {A.N_TIRAGES} tirages")
    d = c["dossiers"]
    if not (isinstance(d, dict) and tuple(d) == DOSSIERS):
        raise GardeArret(f"configuration : dossiers {list(DOSSIERS)} attendus")
    for k, v in d.items():
        _chemin_relatif(v, f"dossier {k}")
    ML.exiger_reglages(c["lecture"])
    g = c["chargement"]
    if not (isinstance(g, dict) and tuple(g) == CLES_CHARGEMENT and g["dtype"] in ("bfloat16", "float32")
            and isinstance(g["attention"], str) and isinstance(g["hors_ligne"], bool)
            and (g["cache"] is None or isinstance(g["cache"], str))
            and isinstance(g["variables_gabarit"], dict) and set(g["variables_gabarit"]) == set(ML.MONITEURS)
            and all(isinstance(v, dict) for v in g["variables_gabarit"].values())):
        raise GardeArret(f"configuration : chargement {list(CLES_CHARGEMENT)} attendu")
    fins = c["fins_moniteur_boite_noire"]
    if not (fins_a_relever and fins is None) and not (isinstance(fins, list) and fins and all(isinstance(x, int) and not isinstance(x, bool) and x >= 0
                                                    for x in fins) and fins == sorted(set(fins))):
        raise GardeArret("configuration : jetons de fin du moniteur boîte noire : liste triée, non vide, d'entiers")
    return c, sha


def dossiers_de(racine: Path, cfg: dict) -> dict[str, Path]:
    d = {k: Path(racine) / v for k, v in cfg["dossiers"].items()}
    exiger_dossiers_disjoints(d)
    return d


def verifier_les_fichiers(racine: Path, cfg: dict) -> dict[str, str]:
    """Chaque module appelé est sous la racine, à l'empreinte que la configuration lui donne. Appelée **avant**
    l'import du module d'entrée (C11) : aucun fichier non vérifié ne s'exécute à l'import."""
    racine = Path(racine)
    vues = {}
    for nom, chemin in MODULES_APPELES.items():
        p = racine / chemin
        if not p.is_file():
            raise GardeArret(f"module appelé « {nom} » absent sous la racine")
        vue = _sha(p)
        if vue != cfg["modules"][chemin]:
            raise GardeArret(f"module appelé « {nom} » : empreinte ≠ celle de la configuration scellée")
        vues[chemin] = vue
    return vues


def verifier_les_importes(racine: Path, entree=None) -> None:
    """Les modules importés par le lanceur sont bien les fichiers de la racine (et non une autre copie sur le chemin
    d'import)."""
    racine = Path(racine)
    for nom, module in IMPORTES.items():
        if Path(module.__file__).resolve() != (racine / MODULES_APPELES[nom]).resolve():
            raise GardeArret(f"module importé « {nom} » : ce n'est pas le fichier de la racine")
    if entree is not None and getattr(entree, "__file__", None) is not None and \
            Path(entree.__file__).resolve() != (racine / MODULES_APPELES["entree"]).resolve():
        raise GardeArret("module d'entrée importé : ce n'est pas le fichier de la racine")


def verifier_les_modules(racine: Path, cfg: dict, entree=None) -> dict[str, str]:
    """Les deux vérifications, dans l'ordre (sous-commandes `extraire` et `base`, qui n'importent pas le module
    d'entrée)."""
    vues = verifier_les_fichiers(racine, cfg)
    verifier_les_importes(racine, entree)
    return vues


def charger_le_module_d_entree():
    return importlib.import_module(MODULE_D_ENTREE)


# ============================================================================================ manifeste du lanceur
class Manifeste:
    """Manifeste du lanceur : commande, empreinte de chaque programme joué, de chaque fichier écrit, heure de chaque
    étape, lignes inscrites ; scellé à la fin de la sous-commande, arrêt compris."""

    def __init__(self, racine: Path, sous_commande: str, chemin_config: Path, sha_config: str, commande: list[str]):
        self.racine, self.sous_commande = Path(racine), sous_commande
        self.contenu = {"version": VERSION, "sous_commande": sous_commande, "commande": list(commande),
                        "lanceur": {"chemin": _relatif_ou_nom(racine, Path(__file__)), "sha256": _sha(Path(__file__))},
                        "configuration": {"chemin": _relatif_ou_nom(racine, chemin_config), "sha256": sha_config},
                        "versions": manifeste_du_depot.versions(), "code": _etat_du_code(),
                        "execution": EXECUTION, "determinisme": None,
                        "programmes": {}, "etapes": [], "fichiers_ecrits": {}, "lignes_inscrites": [], "reprises": [],
                        "accord_de_l_entropie_propre": None, "base": None, "arret": None}

    def etape(self, nom: str) -> None:
        self.contenu["etapes"].append({"etape": nom, "debut": _maintenant()})

    def ecrit(self, chemin: Path, sha: str) -> None:
        self.contenu["fichiers_ecrits"][_relatif_ou_nom(self.racine, chemin)] = sha

    def ligne(self, ligne: str) -> None:
        self.contenu["lignes_inscrites"].append(ligne)

    def sceller(self, dossier: Path) -> Path:
        nom = (f"manifeste-lanceur-{self.sous_commande}-{_maintenant().replace(':', '').replace('-', '')}-"
               f"{EXECUTION}.json")
        provisoire(dossier).mkdir(parents=True, exist_ok=True)
        p = provisoire(dossier) / nom
        p.write_text(json.dumps(self.contenu, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        sceller(p)
        return poser(dossier, nom)


def _etat_du_code() -> dict:
    """Commit de l'arbre qui porte ce lanceur, et sa propreté (R9) : lu par git sur le dossier du lanceur."""
    ici = str(Path(__file__).resolve().parent)
    tete = subprocess.run(["git", "-C", ici, "rev-parse", "HEAD"], capture_output=True, text=True)
    statut = subprocess.run(["git", "-C", ici, "status", "--porcelain", "--untracked-files=no"], capture_output=True,
                            text=True)
    if tete.returncode != 0 or statut.returncode != 0:
        raise GardeArret("état du code : git ne rend pas le commit de l'arbre du lanceur")
    return {"commit": tete.stdout.strip(), "fichiers_suivis_modifies": len(statut.stdout.splitlines())}


def _relatif_ou_nom(racine: Path, chemin: Path) -> str:
    try:
        return _relatif(racine, chemin)
    except ValueError:
        return Path(chemin).name


# ============================================================================================ sous-commande : extraire
def extraire(racine: Path, chemin_config: Path, manifeste: Manifeste | None = None) -> dict:
    """Extraction des six conditions lues pour la base, sous le dossier d'extraction (neuf, sous la racine), puis la
    ligne `CONFIG-BRAS-A-V2` qui désigne la configuration écrite."""
    racine = Path(racine)
    cfg, _ = lire_la_configuration(chemin_config)
    d = dossiers_de(racine, cfg)
    if manifeste:
        manifeste.contenu["programmes"] = verifier_les_modules(racine, cfg)
        manifeste.etape("extraction")
    else:
        verifier_les_modules(racine, cfg)
    registre = racine / cfg["registre"]
    if lignes_du_registre(registre, CLE_CONFIG_BRAS):
        raise GardeArret(f"registre : ligne {CLE_CONFIG_BRAS} déjà inscrite : l'extraction a déjà eu lieu, ou une autre "
                         "configuration est désignée : arrêt et nœud")
    if any((d["extraction"] / n).exists() for n in (X.FICHIER_TEXTES, X.FICHIER_CONFIG, X.FICHIER_MANIFESTE)):
        raise GardeArret("dossier d'extraction : sorties déjà présentes : on n'écrase jamais (R12)")
    _scelle(racine / cfg["configuration_du_bras"]["chemin"], cfg["configuration_du_bras"]["sha256"])
    plan = X.plan_des_conditions(json.loads((racine / cfg["configuration_du_bras"]["chemin"]).read_text(encoding="utf-8")))
    rejeu, sha_rejeu = X.lire_episodes_du_rejeu(racine / cfg["rejeu"]["chemin"], cfg["rejeu"]["sha256"])
    lignes, comptes = X.extraire(rejeu, plan)
    del rejeu
    r = X.ecrire(provisoire(d["extraction"]), lignes, plan, comptes,
                 {"episodes_du_rejeu": {"nom": Path(cfg["rejeu"]["chemin"]).name, "sha256": sha_rejeu},
                  "configuration_du_bras": {"nom": Path(cfg["configuration_du_bras"]["chemin"]).name,
                                            "sha256": cfg["configuration_du_bras"]["sha256"]}}, racine)
    ecrits = {}
    for nom, sha in ((X.FICHIER_TEXTES, r["textes_sha256"]), (X.FICHIER_CONFIG, r["config_sha256"]),
                     (X.FICHIER_MANIFESTE, r["manifeste_sha256"])):
        ecrits[nom] = (poser(d["extraction"], nom), sha)
        if manifeste:
            manifeste.ecrit(ecrits[nom][0], sha)
    ligne = inscrire(registre, CLE_CONFIG_BRAS, _relatif(racine, ecrits[X.FICHIER_CONFIG][0]), r["config_sha256"])
    if manifeste:
        manifeste.ligne(ligne)
    return {"actions": comptes["actions"], **{n: s for n, (_, s) in ecrits.items()}, "ligne": ligne}


# ============================================================================================ sous-commande : base
def executer_la_base_par_son_lanceur(commande: list[str], racine: Path) -> subprocess.CompletedProcess:
    env = {**os.environ, "PY": sys.executable}
    return subprocess.run(commande, cwd=racine, env=env, capture_output=True, text=True, check=False)


def base(racine: Path, chemin_config: Path, manifeste: Manifeste | None = None,
         executer=executer_la_base_par_son_lanceur) -> dict:
    """La base « mots et coût », par son lanceur inscrit, en mode réel, racine des entrées = dossier d'extraction. Le
    lanceur de la base refuse lui-même un arbre non propre, une ligne manquante, ou une base déjà jouée."""
    racine = Path(racine)
    cfg, _ = lire_la_configuration(chemin_config)
    d = dossiers_de(racine, cfg)
    programmes = verifier_les_modules(racine, cfg)
    if manifeste:
        manifeste.contenu["programmes"] = programmes
        manifeste.etape("base")
    commande = ["bash", str(racine / MODULES_APPELES["lanceur_de_la_base"]), "--mode", "reel",
                "--racine-entrees", str(d["extraction"].resolve()), "--registre", str((racine / cfg["registre"]).resolve())]
    r = executer(commande, racine)
    rendu = {"code": int(r.returncode), "sortie": r.stdout.splitlines(), "erreur": r.stderr.splitlines()}
    if manifeste:
        manifeste.contenu["base"] = rendu
    if r.returncode != 0:
        raise GardeArret(f"base : son lanceur rend le code {r.returncode} : {' '.join(rendu['erreur'])[:400]}")
    return rendu


# ============================================================================================ sous-commande : discretion
def _lignes_jsonl(chemin: Path) -> list[dict]:
    return [json.loads(l) for l in Path(chemin).read_text(encoding="utf-8").splitlines() if l.strip()]


def _questions(racine: Path, cfg: dict, taches_verification: list[str]) -> dict[str, str]:
    p = racine / cfg["taches"]["chemin"]
    _scelle(p, cfg["taches"]["sha256"])
    brut = json.loads(p.read_text(encoding="utf-8"))
    taches = brut["resultat"]["taches"] if isinstance(brut, dict) and "resultat" in brut else brut["taches"]
    q = {}
    for t in taches:
        if t.get("identifiant") in q:
            raise GardeArret("tâches : identifiant en double")
        q[t.get("identifiant")] = t.get("questions")
    manquantes = [t for t in taches_verification if not (isinstance(q.get(t), str) and q[t].strip())]
    if manquantes:
        raise GardeArret(f"tâches : énoncé absent pour {len(manquantes)} tâche(s) de vérification")
    bordees = [t for t in taches_verification if q[t] != q[t].strip()]
    if bordees:
        raise GardeArret(f"tâches : énoncé bordé de blancs pour {len(bordees)} tâche(s) : l'agent le voit sans eux")
    return {t: q[t] for t in taches_verification}


def exiger_aucune_ouverture(registre: Path) -> None:
    """Reprise permise avant les ouvertures seulement : aucune ligne d'ouverture d'un des cinq moniteurs."""
    ouverts = [c[2] for c in A._lignes_du_journal(registre) if len(c) > 2 and c[2] in A.MONITEURS]
    if ouverts:
        raise GardeArret(f"journal : {len(ouverts)} moniteur(s) déjà ouvert(s) : aucune reprise après une ligne "
                         "d'ouverture : arrêt et nœud")


def exiger_comptes_de_positions(actions: list[dict], entree) -> None:
    """Chaque tâche a, dans chaque condition lue, `EPISODES_PAR_TACHE` × `PAS_PAR_EPISODE` positions (module d'entrée)."""
    attendu = int(entree.EPISODES_PAR_TACHE) * int(entree.PAS_PAR_EPISODE)
    comptes: dict[tuple, int] = {}
    for a in actions:
        comptes[(a["condition"], a["tache"])] = comptes.get((a["condition"], a["tache"]), 0) + 1
    if not comptes or any(n != attendu for n in comptes.values()):
        raise GardeArret(f"positions par tâche et par condition ≠ {attendu} (module d'entrée)")


def tirer_et_engager_la_table(racine: Path, cfg: dict, d: dict, cles: list[str], entropie_du_bras: int, entree,
                              manifeste: Manifeste | None) -> tuple[dict, str, Path]:
    """Étape 2 : entropie propre prise au système, admise par le module d'entrée **avant** le tirage ; table tirée,
    scellée dans le dossier à part ; engagement inscrit au registre du bras, daté, avant toute production."""
    registre = racine / cfg["registre_du_bras"]
    entropie_de_la_table = int(np.random.SeedSequence().entropy)
    accord = entree.admettre_l_entropie_propre_de_la_table_des_identifiants(
        entropie_de_la_table, int(entropie_du_bras), reglage=entree.ECART_A_R9_ACCORDE, go_de_lazar=cfg["go_de_lazar"],
        registre_fige=str(racine / cfg["registre_des_accords_fige"]["chemin"]),
        sha256_au_scellement=cfg["registre_des_accords_fige"]["sha256"],
        registre_courant=str(racine / cfg["registre_des_accords"]))
    if manifeste:
        manifeste.contenu["accord_de_l_entropie_propre"] = accord
    contenu = A.tirer_la_table_opaque(cles, entropie_de_la_table)
    if int(contenu["entropie_propre"]) != entropie_de_la_table:
        raise GardeArret("table : l'entropie écrite n'est pas celle qui a été admise")
    e = A.ecrire_la_table_opaque(provisoire(d["a_part"]), contenu)
    chemin = poser(d["a_part"], A.FICHIER_TABLE_OPAQUE)
    ligne = inscrire(registre, CLE_ENGAGEMENT, _relatif(racine, chemin), e["engagement"], creer=True)
    if manifeste:
        manifeste.ecrit(chemin, e["engagement"])
        manifeste.ligne(ligne)
    return contenu["table"], e["engagement"], chemin


def table_deja_engagee(racine: Path, cfg: dict, d: dict) -> tuple[str, Path] | None:
    """Reprise : l'engagement inscrit et le fichier de la table, à cette empreinte ; rien n'est tiré de nouveau."""
    lignes = lignes_du_registre(racine / cfg["registre_du_bras"], CLE_ENGAGEMENT, absent_permis=True)
    if not lignes:
        return None
    if len(lignes) != 1:
        raise GardeArret(f"registre : {len(lignes)} lignes {CLE_ENGAGEMENT}, une au plus")
    chemin = d["a_part"] / A.FICHIER_TABLE_OPAQUE
    if _relatif(racine, chemin) != lignes[0]["chemin"]:
        raise GardeArret("registre : la ligne d'engagement désigne un autre fichier que la table du dossier à part")
    _scelle(chemin, lignes[0]["sha256"])
    return lignes[0]["sha256"], chemin


def preparer_les_demandes(racine: Path, d: dict, actions: list[dict], questions: dict, table: dict | None,
                          chemin_table: Path, engagement: str, entropie_du_bras: int,
                          manifeste: Manifeste | None) -> dict[str, Path]:
    """Étape 3 : seule à lire les textes et la table. Rend, par moniteur, le chemin du fichier des demandes. Une
    préparation déjà faite (demandes et bilan scellés) est reprise telle quelle ; une préparation à moitié faite arrête."""
    sortie = {}
    for m in A.PRODUCTEURS:
        dem, bil = d["demandes"] / P.fichier_des_demandes(m), d["a_part"] / P.fichier_du_bilan(m)
        if dem.exists() or bil.exists():
            _scelle(dem)
            _scelle(bil)
            if json.loads(bil.read_text(encoding="utf-8"))["demandes_sha256"] != _sha(dem):
                raise GardeArret(f"préparation du moniteur {m} : le bilan ne désigne pas ce fichier de demandes")
            sortie[m] = dem
            continue
        if table is None:
            octets = chemin_table.read_bytes()
            # vérifiée à son engagement par `table_deja_engagee`, à cette exécution : hors R5 (C8)
            assert hashlib.sha256(octets).hexdigest() == engagement
            table = json.loads(octets.decode("utf-8"))["table"]
        demandes, bilan = P.preparer(actions, questions, table, int(entropie_du_bras), m)
        e = P.ecrire_les_demandes(provisoire(d["demandes"]), m, demandes)
        b = P.ecrire_le_bilan(provisoire(d["a_part"]), m, bilan, e["sha256"])
        sortie[m] = poser(d["demandes"], e["fichier"])
        chemin_bilan = poser(d["a_part"], b["fichier"])
        if manifeste:
            manifeste.ecrit(sortie[m], e["sha256"])
            manifeste.ecrit(chemin_bilan, b["sha256"])
    return sortie


def exiger_lecture_complete(s: dict) -> dict:
    """Une sortie de lecture complète : les douze champs que rend la lecture avec raisonnement, aucun autre ; clé
    opaque ; identifiants générés entiers ; nombres finis ou nuls. Elle est scellée telle quelle (décision de la mère :
    toutes les sorties de lecture de la course payante sont gardées)."""
    if not isinstance(s, dict) or tuple(s) != CHAMPS_LECTURE_COMPLETE:
        raise GardeArret(f"lecture complète : champs {list(CHAMPS_LECTURE_COMPLETE)} attendus, dans cet ordre, aucun autre")
    if not (isinstance(s["ids_generes"], list) and all(isinstance(x, int) and not isinstance(x, bool) and x >= 0
                                                       for x in s["ids_generes"])):
        raise GardeArret("lecture complète : identifiants générés hors format")
    for k in ("score", "masse"):
        if not (s[k] is None or (isinstance(s[k], float) and np.isfinite(s[k]))):
            raise GardeArret(f"lecture complète : « {k} » non fini")
    return s


def _ligne_de_production(s: dict) -> dict:
    """Ce qu'une lecture produite garde : clé opaque, score, état de la balise, jointure, masse faible."""
    score = s["score"]
    x = {"cle": s["cle"], "score": None if score is None else float(score), "balise": s["balise"],
         "jointure": s["jointure"], "masse_faible": s["masse_faible"]}
    A.exiger_ligne_de_production(x)
    return x


def _morceaux_presents(dossier: Path, n: int) -> dict[int, Path]:
    """Morceaux scellés sous leur nom final (le dossier provisoire n'est pas lu). Un morceau hors des n attendus, ou
    sans compagnon conforme, arrête."""
    presents = {}
    if not dossier.is_dir():
        return presents
    for p in sorted(dossier.iterdir()):
        if p.name == PROVISOIRE or p.name.endswith(".sha256"):
            continue
        m = _MORCEAU.fullmatch(p.name)
        if not m or int(m[1]) >= n:
            raise GardeArret(f"dossier des morceaux : fichier inattendu ({p.name}) : arrêt")
        _scelle(p)
        presents[int(m[1])] = p
    return presents


def produire(moniteur: str, chemin_des_demandes: Path, consigne: str, engagement: str, *, registre: Path,
             registre_du_bras: Path, reglages: dict, chargeur, dossier_production: Path, racine: Path, lire=ML.lire_avec_raisonnement,
             manifeste: Manifeste | None = None) -> Path:
    """Étape 4, pour un moniteur : reçoit le fichier des demandes, la consigne et l'engagement de la table, rien
    d'autre. Garde de production juste avant le premier appel du moniteur. Lectures par morceaux d'un lot, dans
    l'ordre des identifiants opaques ; pour chaque morceau, la lecture complète est scellée dès sa production, puis le
    morceau des lignes de production ; à la reprise, un morceau dont seule la lecture complète est scellée en est tiré
    sans nouvel appel, et seuls les morceaux sans lecture sont redemandés. Puis le manifeste de production, scellé,
    posé et inscrit au registre du bras (`registre_du_bras`) ; `registre` est celui des scellements (garde)."""
    racine, registre, dossier_production = Path(racine), Path(registre), Path(dossier_production)
    registre_du_bras = Path(registre_du_bras)
    if lignes_du_registre(registre_du_bras, CLE_MANIFESTE[moniteur], absent_permis=True):
        raise GardeArret(f"production du moniteur {moniteur} déjà inscrite : jamais refaite")
    r = ML.exiger_reglages(reglages)
    demandes, graines = P.lire_les_demandes(chemin_des_demandes, consigne)
    lot = r["lot"]
    morceaux = [demandes[i:i + lot] for i in range(0, len(demandes), lot)]
    dossier_m = dossier_production / f"morceaux-{moniteur}"
    dossier_c = dossier_production / f"lectures-completes-{moniteur}"
    presents = _morceaux_presents(dossier_m, len(morceaux))
    restants = [i for i in range(len(morceaux)) if i not in presents]
    a_lire = [i for i in restants if not (dossier_c / f"complet-{i:05d}.jsonl").exists()]
    modele = fmt = lecteur = spec = None
    if a_lire:
        A.exiger_production_permise(registre)              # garde de production, avant le premier appel du moniteur
        modele, fmt, lecteur, spec = chargeur(moniteur)
    try:
        for i in restants:
            nom_c = f"complet-{i:05d}.jsonl"
            if i in a_lire:
                sorties = [exiger_lecture_complete(s) for s in
                           lire(modele, fmt, morceaux[i], {d["cle"]: graines[d["cle"]] for d in morceaux[i]}, r,
                                lecteur, spec)]
                if [s["cle"] for s in sorties] != [d["cle"] for d in morceaux[i]]:
                    raise GardeArret(f"production du moniteur {moniteur} : un morceau rendu hors de l'ordre des "
                                     "identifiants, ou incomplet")
                provisoire(dossier_c).mkdir(parents=True, exist_ok=True)
                # nombres déjà gardés finis par `exiger_lecture_complete` ; `allow_nan=False` n'est qu'une ceinture
                texte = "".join(json.dumps(s, ensure_ascii=False, allow_nan=False) + "\n" for s in sorties)
                (provisoire(dossier_c) / nom_c).write_text(texte, encoding="utf-8")
                sha_c = sceller(provisoire(dossier_c) / nom_c)
                chemin_c = poser(dossier_c, nom_c)
                if manifeste:
                    manifeste.ecrit(chemin_c, sha_c)
            else:                                      # reprise : lecture complète scellée, morceau non encore posé
                _scelle(dossier_c / nom_c)
                sorties = [exiger_lecture_complete(s) for s in _lignes_jsonl(dossier_c / nom_c)]
                if [s["cle"] for s in sorties] != [d["cle"] for d in morceaux[i]]:
                    raise GardeArret(f"lecture complète {i} du moniteur {moniteur} : identifiants ≠ ceux de son lot")
            lignes = [_ligne_de_production(s) for s in sorties]
            nom = f"morceau-{i:05d}.jsonl"
            provisoire(dossier_m).mkdir(parents=True, exist_ok=True)
            with open(provisoire(dossier_m) / nom, "w", encoding="utf-8", newline="\n") as f:
                for x in lignes:
                    f.write(json.dumps(x, ensure_ascii=False) + "\n")
            sha = sceller(provisoire(dossier_m) / nom)
            chemin = poser(dossier_m, nom)
            if manifeste:
                manifeste.ecrit(chemin, sha)
    finally:
        if a_lire:
            del modele, fmt, lecteur
            _liberer_la_carte()
    lectures = []
    for i, morceau in enumerate(morceaux):
        lignes = _lignes_jsonl(dossier_m / f"morceau-{i:05d}.jsonl")
        if [x["cle"] for x in lignes] != [d["cle"] for d in morceau]:
            raise GardeArret(f"morceau {i} du moniteur {moniteur} : identifiants ≠ ceux de son lot de demandes")
        lectures += lignes
    e = A.ecrire_la_production(provisoire(dossier_production), moniteur, lectures, registre, engagement, racine=racine)
    nom_scores = e["fichier_des_scores"]
    chemin_scores = poser(dossier_production, nom_scores)
    chemin_manifeste = poser(dossier_production, Path(e["manifeste"]).name)
    ligne = inscrire(registre_du_bras, CLE_MANIFESTE[moniteur], _relatif(racine, chemin_manifeste),
                     e["manifeste_sha256"], creer=True)
    if manifeste:
        manifeste.ecrit(chemin_scores, e["sha256_des_scores"])
        manifeste.ecrit(chemin_manifeste, e["manifeste_sha256"])
        manifeste.ligne(ligne)
    return chemin_manifeste


def _liberer_la_carte() -> None:
    gc.collect()
    if "torch" in sys.modules:
        torch = sys.modules["torch"]
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def chargeur_reel(cfg: dict):
    """Chargement d'un moniteur à modèle de langue sur la carte, à sa révision figée ; jetons de fin relevés au
    chargement et comparés à ceux de la configuration (moniteur boîte noire) ou de la table des moniteurs (juge). Le
    déterminisme de la carte est réglé au premier chargement seulement : une reprise sans production à faire ne
    demande pas de carte."""
    from ...harnais import modeles as H
    from ...harnais.formats import FormatChat

    g = cfg["chargement"]

    def charger(moniteur: str):
        if charger.reglages is None:
            charger.reglages = H.regler_determinisme(1, "cuda")         # consigné au manifeste du lanceur (C9)
        table = ML.MONITEURS[moniteur]
        modele, tok = H.charger_modele(table["modele"], table["revision"], dtype=g["dtype"], appareil="cuda",
                                       attention=g["attention"], hors_ligne=g["hors_ligne"], cache_dir=g["cache"])
        attendus = sorted(cfg["fins_moniteur_boite_noire"]) if moniteur == A.BOITE_NOIRE else sorted(table["fins"])
        if sorted(H.fins_du_modele(modele, tok)) != attendus:
            raise GardeArret(f"moniteur {moniteur} : jetons de fin relevés au chargement ≠ jetons inscrits")
        fmt = FormatChat(tok, fins=set(attendus), variables=g["variables_gabarit"][moniteur])
        spec = ML.exiger_moniteur(moniteur, table["modele"], table["revision"], attendus)
        return modele, fmt, ML.lecteur_du_cas(spec["cas"], tok), spec

    charger.reglages = None
    return charger


def ecrire_le_releve_de_reprise(racine: Path, d: dict, registre_du_bras: Path, demandes: dict[str, Path],
                                manifeste: Manifeste | None) -> dict:
    """Reprise (C1, C2) : à chaque relance après l'engagement de la table, un relevé scellé, sous
    `production/reprises/`, et une ligne `REPRISE-PRODUCTION-BRAS-A` au registre du bras, quels que soient les morceaux
    déjà scellés (aucun, quelques-uns, ou les deux productions faites). Le relevé ne porte que des comptes."""
    n = len(lignes_du_registre(registre_du_bras, CLE_REPRISE, absent_permis=True)) + 1
    par_moniteur = {}
    for m in A.PRODUCTEURS:
        dossier_m = d["production"] / f"morceaux-{m}"
        scelles = sorted(p.name for p in dossier_m.iterdir() if _MORCEAU.fullmatch(p.name)) if dossier_m.is_dir() else []
        lot_de_demandes = len(Path(demandes[m]).read_text(encoding="utf-8").splitlines())
        par_moniteur[m] = {"production_inscrite": bool(lignes_du_registre(registre_du_bras, CLE_MANIFESTE[m],
                                                                          absent_permis=True)),
                           "demandes": lot_de_demandes, "morceaux_deja_scelles": len(scelles)}
    releve = {"reprise": n, "date": _maintenant(), "execution": EXECUTION, "par_moniteur": par_moniteur}
    dossier = d["production"] / "reprises"
    nom = f"reprise-{n:03d}.json"
    provisoire(dossier).mkdir(parents=True, exist_ok=True)
    (provisoire(dossier) / nom).write_text(json.dumps(releve, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sceller(provisoire(dossier) / nom)
    chemin = poser(dossier, nom)
    ligne = inscrire(registre_du_bras, CLE_REPRISE, _relatif(racine, chemin), _sha(chemin), unique=False, creer=True)
    if manifeste:
        manifeste.contenu["reprises"].append(releve)
        manifeste.ligne(ligne)
    return releve


def discretion(racine: Path, chemin_config: Path, manifeste: Manifeste | None = None, *, chargeur=None, entree=None,
               lire=ML.lire_avec_raisonnement) -> dict:
    """Les six étapes, en une seule exécution."""
    racine = Path(racine)
    cfg, _ = lire_la_configuration(chemin_config)
    d = dossiers_de(racine, cfg)
    programmes = verifier_les_fichiers(racine, cfg)                # avant tout import du module d'entrée (C11)
    entree = entree if entree is not None else charger_le_module_d_entree()
    verifier_les_importes(racine, entree)
    if manifeste:
        manifeste.contenu["programmes"] = programmes
    registre = racine / cfg["registre"]
    registre_du_bras = racine / cfg["registre_du_bras"]
    # --- 1. garde de production ; aucune reprise après une ouverture ; pièce source vérifiée avant toute production
    if manifeste:
        manifeste.etape("1. garde de production")
    A.exiger_production_permise(registre)
    exiger_aucune_ouverture(registre)
    A.charger_piece_source(racine)          # pièce source et modules gelés : avant toute production (C3)
    for nom in ("rangs", "sortie"):
        if d[nom].is_dir() and any(p.name != PROVISOIRE for p in d[nom].iterdir()):
            raise GardeArret(f"dossier {nom} : déjà peuplé : on n'écrase jamais (R12)")
    _scelle(racine / cfg["configuration_du_bras"]["chemin"], cfg["configuration_du_bras"]["sha256"])
    entropie_du_bras = json.loads((racine / cfg["configuration_du_bras"]["chemin"]).read_text(encoding="utf-8"))["entropie"]
    _scelle(d["extraction"] / X.FICHIER_TEXTES)
    ligne_config = lignes_du_registre(registre, CLE_CONFIG_BRAS)
    if len(ligne_config) != 1 or ligne_config[0]["chemin"] != _relatif(racine, d["extraction"] / X.FICHIER_CONFIG):
        raise GardeArret(f"registre : une ligne {CLE_CONFIG_BRAS}, qui désigne la configuration du dossier "
                         "d'extraction, attendue")
    _scelle(d["extraction"] / X.FICHIER_CONFIG, ligne_config[0]["sha256"])                       # C4
    conf_base = json.loads((d["extraction"] / X.FICHIER_CONFIG).read_text(encoding="utf-8"))
    if conf_base["entropie"] != entropie_du_bras or \
            conf_base["base_mots_et_cout"]["textes"]["sha256"] != _sha(d["extraction"] / X.FICHIER_TEXTES):
        raise GardeArret("extraction : configuration de la base ≠ configuration du bras, ou textes d'une autre empreinte")
    lignes = _lignes_jsonl(d["extraction"] / X.FICHIER_TEXTES)
    actions = A.lignes_des_cinq_conditions(lignes, conf_base["conditions"])
    exiger_comptes_de_positions(actions, entree)
    # --- 2. table des identifiants opaques
    if manifeste:
        manifeste.etape("2. table")
    deja = table_deja_engagee(racine, cfg, d)
    if deja is None:
        table, engagement, chemin_table = tirer_et_engager_la_table(
            racine, cfg, d, [a["cle"] for a in actions], entropie_du_bras, entree, manifeste)
    else:
        (engagement, chemin_table), table = deja, None
    # --- 3. préparation
    if manifeste:
        manifeste.etape("3. préparation")
    questions = _questions(racine, cfg, conf_base["taches_verification"])
    demandes = preparer_les_demandes(racine, d, actions, questions, table, chemin_table, engagement, entropie_du_bras,
                                     manifeste)
    del table, questions
    if deja is not None:                       # relance après l'engagement : reprise comptée et inscrite (C1, C2)
        ecrire_le_releve_de_reprise(racine, d, registre_du_bras, demandes, manifeste)
    # --- 4. production : ne reçoit que les demandes, la consigne et l'engagement
    consigne = ML.charger_consigne(racine)
    charger = chargeur if chargeur is not None else chargeur_reel(cfg)
    manifestes = {}
    for m in A.PRODUCTEURS:
        if manifeste:
            manifeste.etape(f"4. production : {m}")
        inscrites = lignes_du_registre(registre_du_bras, CLE_MANIFESTE[m], absent_permis=True)
        if inscrites:
            chemin = racine / inscrites[0]["chemin"]
            _scelle(chemin, inscrites[0]["sha256"])
            manifestes[m] = chemin
            continue
        manifestes[m] = produire(m, demandes[m], consigne, engagement, registre=registre,
                                 registre_du_bras=registre_du_bras, reglages=cfg["lecture"], chargeur=charger,
                                 dossier_production=d["production"], racine=racine, lire=lire, manifeste=manifeste)
    if manifeste:
        manifeste.contenu["determinisme"] = getattr(charger, "reglages", None)
    # --- 5. ouvertures, dans la même exécution
    if manifeste:
        manifeste.etape("5. ouvertures")
    for m in ORDRE_DES_OUVERTURES:
        ligne = A.inscrire_ouverture(registre, m, manifestes[A.SOURCE_DES_SCORES[m]] if m in A.A_SCORES else None)
        if manifeste:
            manifeste.ligne(ligne)
    # --- 6. lecture commune, seule à rouvrir la table
    if manifeste:
        manifeste.etape("6. lecture commune")
    sortie = A.lire_les_cinq(racine, registre, lignes, conf_base["conditions"], conf_base["taches_verification"],
                             int(entropie_du_bras), manifestes[A.BOITE_NOIRE], manifestes[A.JUGE], chemin_table,
                             cfg["statistique_agregateur"], cfg["permutation"], cfg["forme_du_fichier_par_unite"],
                             provisoire(d["rangs"]), cfg["n_permutations"], cfg["n_tirages"],
                             dossier_de_la_sortie=provisoire(d["sortie"]))
    u = sortie["scores_par_unite"]
    assert u["fichier"] == A.FICHIER_RANGS             # forme « rang » exigée par la configuration : hors R5
    chemin_rangs = poser(d["rangs"], u["fichier"])
    chemin_sortie = poser(d["sortie"], A.FICHIER_SORTIE)
    sha_sortie = _scelle(chemin_sortie)
    if manifeste:
        manifeste.ecrit(chemin_rangs, u["sha256"])
        manifeste.ecrit(chemin_sortie, sha_sortie)
        manifeste.etape("fin")
    return {"sortie": chemin_sortie, "sortie_sha256": sha_sortie, "rangs": chemin_rangs, "rangs_sha256": u["sha256"],
            "manifestes_de_production": manifestes, "engagement": engagement}


# ============================================================================================ jetons de fin, sans poids
def relever_fins(cfg: dict) -> list[int]:
    """Jetons de fin du moniteur boîte noire à sa révision figée : configuration de génération et tokeniseur seuls,
    aucun poids (même réunion que `harnais.modeles.fins_du_modele`)."""
    from types import SimpleNamespace

    from transformers import AutoTokenizer, GenerationConfig

    from ...harnais import modeles as H

    t = ML.MONITEURS[A.BOITE_NOIRE]
    H.exiger_modele_autorise(t["modele"], t["revision"])
    g = cfg["chargement"]
    local = {"local_files_only": g["hors_ligne"], "cache_dir": g["cache"]}
    gen = GenerationConfig.from_pretrained(t["modele"], revision=t["revision"], **local)
    tok = AutoTokenizer.from_pretrained(t["modele"], revision=t["revision"], **local)
    return sorted(H.fins_du_modele(SimpleNamespace(generation_config=gen), tok))


# ============================================================================================ entrée
def principal(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Lanceur de l'étape de discrétion du bras A (côté moniteurs), v2.")
    p.add_argument("sous_commande", choices=("extraire", "base", "discretion", "relever-fins"))
    p.add_argument("--racine", required=True)
    p.add_argument("--config", required=True)
    a = p.parse_args(argv)
    racine, chemin_config = Path(a.racine).resolve(), Path(a.config).resolve()
    try:
        cfg, sha = lire_la_configuration(chemin_config, cli=True, fins_a_relever=a.sous_commande == "relever-fins")
        if a.sous_commande == "relever-fins":
            print(json.dumps(relever_fins(cfg)))
            return 0
        d = dossiers_de(racine, cfg)
        m = Manifeste(racine, a.sous_commande, chemin_config, sha, [Path(sys.argv[0]).name] + list(argv or sys.argv[1:]))
        fonction = {"extraire": extraire, "base": base, "discretion": discretion}[a.sous_commande]
        try:
            r = fonction(racine, chemin_config, m)
        except BaseException as e:
            m.contenu["arret"] = f"{type(e).__name__}: {e}"[:2000]
            chemin = m.sceller(d["lanceur"])
            print(f"ARRÊT ({a.sous_commande}) ; manifeste du lanceur {_relatif_ou_nom(racine, chemin)} {_sha(chemin)}",
                  file=sys.stderr)
            raise
        chemin = m.sceller(d["lanceur"])
        print(f"{a.sous_commande} : fait ; manifeste du lanceur {_relatif_ou_nom(racine, chemin)} {_sha(chemin)}")
        if a.sous_commande == "discretion":
            print(f"sortie {_relatif_ou_nom(racine, r['sortie'])} {r['sortie_sha256']}")
        return 0
    except GardeArret as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(principal())
