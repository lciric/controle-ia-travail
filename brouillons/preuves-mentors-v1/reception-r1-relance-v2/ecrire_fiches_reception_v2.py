#!/usr/bin/env python3
"""Réception de la relance de R1 sur la table de tokenisation v3 — script v2 : fiche de réception, puis fiches des analyses.

Version 2 de `reception-r1-relance-v1/ecrire_fiches_reception_v1.py` (non modifié, R12), pour l'addendum v3 de R1 scellé
(`prereg/R1-addendum-relance-v3.md`, 88e262e2…, commit de scellement 139a81d3), selon notre concordance sur son
brouillon 2 (`concordance-addendum-r1-v3-brouillon2-v1.md`, 8482b4cd…, section « De notre côté », R-1 à R-5).
Deux sous-commandes :

`avant-recuperation` — écrit la **fiche de réception** (document de contrôles de conv-audit, en Markdown, distinct des
  deux fiches JSON des analyses) depuis les seuls textes scellés, lus par `git show <commit>:<chemin>` et vérifiés par
  empreinte et par compagnon au même commit : addendum v3, configuration v5 (empreinte du fichier et empreinte
  canonique), table v3 (version, entrées, comptes), parent, code au commit de scellement, nos trois analyses scellées et
  nos pièces citées. Les attendus de la course (manifeste, résultat, fichiers, juges) sont dérivés de la table et de la
  configuration, puis confrontés aux « Attentes de réception » du texte scellé : une attente absente du texte arrête.
  Refus si le dépôt porte une référence `calcul/…` ou une référence dont le nom contient `donnees` : rien de la sortie
  n'existe ici ni n'est lu. La session scelle la fiche **avant la récupération** des sorties de la course (C-1 ;
  addendum v3, E8 (e) ; GO-2026-11-02-27).

`apres-versement` — relit la fiche de réception scellée (compagnon égal ; empreinte égale à celle envoyée au canal) et
  son bloc d'attendus, puis écrit les deux fiches JSON des analyses scellées aux clés exactes de leurs lecteurs
  (`entrees_v1.lire_fiche`, commit cité a8b7fdb2 ; `entrees_v3.lire_fiche_v3`, commit cité 326601cf), comme la v1 :
  noms attendus seulement, empreintes calculées et confrontées aux compagnons, aucun `.npz` ouvert. En plus de la v1,
  il **compare et refuse** (au lieu de noter) : manifeste du rejeu (commande, `decisif`, texte qui gouverne lu dans la
  clé réelle `preenregistrement` — `manifeste.py` l. 104 —, empreinte canonique de la configuration et son recalcul,
  table citée par la configuration, commit lancé, arbre propre, entropie) ; résultat (rattachement au manifeste,
  `tokenisation.table_sha256`, `tokenisation.addendum` = `prereg/R1-addendum-relance-v2.md` à l'identique, comptes fixés
  par la table) ; runs et empreintes des scores des juges cités par l'addendum v3 ; reprise E21 notée.

Lecture du résultat : seules les clés de `CHEMINS_LUS` sont gardées, dès le chargement (`filtrer`) ; leurs noms sont
écrits dans `redaction.cles_lues`, leurs valeurs ne sont pas recopiées (elles égalent les attendus) ; les valeurs
observées de P-R5 et les lectures de l'instrument (`INTERDITS`) ne sont ni gardées, ni écrites, ni affichées ; toute
fiche est passée à `exiger_sans_fuite` avant écriture (aucune clé interdite, aucun nombre : la fiche ne contient que
chemins, empreintes, pointeurs et motifs, analyse secondaire scellée l. 24). Épisodes non inversibles : liste vide,
fixée (E2, E19).
Tout écart : code 2, « ARRÊT [garde] : … », aucune fiche écrite (R5 ; aucun repli silencieux). Une fiche existante n'est
jamais écrasée (R12). Bibliothèque standard seulement (`python -I`) ; `git` en lecture seule (`show`, `rev-parse`,
`for-each-ref`).
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

NOM_SCRIPT = "ecrire_fiches_reception_v2.py"
FORMAT_PRINCIPALE = "fiche-reception-principale-r1-r2-v1"
FORMAT_SECONDAIRE = "fiche-reception-blanche-noire-v3"
FORMAT_ATTENDUS = "attendus-reception-r1-relance-v3-v1"
DEBUT_BLOC, FIN_BLOC = "<!-- attendus-machine : debut -->", "<!-- attendus-machine : fin -->"
SORTIE_FICHE = "brouillons/preuves-mentors-v1/reception-r1-relance-v2/fiche-reception-r1-relance-v3-v1.md"
SUFFIXE = ".sha256"

# ------------------------------------------------------------------ textes scellés (chemins, commits, empreintes)
COMMIT_SCELLEMENT = "139a81d37fbd2255aff8d27698f84b47b9433221"   # addendum v3 et configuration v5 scellés (un commit)
COMMIT_PRINCIPALE = "83ce7a91f681b36668a9f91424d53ebd632b50b1"   # `prereg/analyse-principale-r1-r2-v1.md` scellé
COMMIT_SECONDAIRE = "7a238666630a6d6dca064e8da6b309320060200d"   # `prereg/analyse-blanche-noire-v3.md` scellé
REF_TETE = "HEAD"   # texte par épisode (son commit 52eb34c8 est hors du clone superficiel) et nos pièces citées
COMMIT_CODE_CITE = "f921fcec10539f1565fab410624a926efdfec12e"
ADDENDUM_V3 = "prereg/R1-addendum-relance-v3.md"
ADDENDUM_V2 = "prereg/R1-addendum-relance-v2.md"   # provenance de la table v3 (`tokenisation.addendum`, E16)
CONFIG_V5 = "prereg/R1-rejeu-config-v5.json"
TABLE_V3 = "prereg/R1-table-tokenisation-v3.json"
PARENT = "prereg/R1-R2-rejeu-p3-v1.md"
NOTRE = "brouillons/preuves-mentors-v1"
# nom : (référence (option de la ligne de commande), chemin, sha256 du fichier, compagnon exigé au même commit, rôle)
PIECES = {
    "addendum_v3": ("scellement", ADDENDUM_V3,
                    "88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4", True, "texte qui gouverne la course"),
    "configuration_v5": ("scellement", CONFIG_V5,
                         "acad6253f3c9f4d93c45a453ae8f5dcb122049a979cf43000d47c5f9c1edd4b8", True, "configuration du rejeu"),
    "table_v3": ("scellement", TABLE_V3,
                 "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423", True, "table de tokenisation v3"),
    "parent": ("scellement", PARENT,
               "80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea", True, "préenregistrement parent"),
    "module_v3": ("scellement", "src/controle_ia/runs_nuit/rejeu_activations_v3.py",
                  "0581cf9a32e054e5044809f80078e3d33e3de27a22830e40ca8aa45a03ca2adc", False,
                  "module de la relance (sans compagnon, en-tête de l'addendum v3)"),
    "manifeste_py": ("scellement", "src/controle_ia/manifeste.py",
                     "1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d", False,
                     "écriture du manifeste (sans compagnon ; concordance § 0)"),
    "script_instance": ("scellement", "scripts/r1_relance_instance_v3.sh",
                        "24744794808832e30cb8fa47c45a19de5a530d5ce06db1bd0557a17d3e35e4eb", True, "script d'instance v3"),
    "amorce": ("scellement", "scripts/amorce_instance_r1_relance_v3.sh",
               "82f386876d3e606e6d8d7d6c388e42a822266d7cf899d448991b8af456badef7", True, "amorce v3"),
    "principale": ("principale", "prereg/analyse-principale-r1-r2-v1.md",
                   "8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537", True, "analyse principale scellée"),
    "secondaire": ("secondaire", "prereg/analyse-blanche-noire-v3.md",
                   "1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9", True, "analyse secondaire scellée"),
    "par_episode": ("tete", "prereg/analyse-par-episode-v1.md",
                    "26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4", True, "lecture par épisode scellée"),
    "concordance_b2": ("tete", f"{NOTRE}/analyse-principale-r1-r2-v1/concordance-addendum-r1-v3-brouillon2-v1.md",
                       "8482b4cd39348104e80187b1470001f71fc6d857fc75344a32529b6dd37ade0b", True,
                       "notre concordance sur le brouillon 2 (R-1 à R-5)"),
    "verdict_graine": ("tete", f"{NOTRE}/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md",
                       "64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68", True,
                       "verdict du rejeu à graine (réserve HG-2)"),
    "procedure_v1": ("tete", f"{NOTRE}/reception-r1-relance-v1/procedure-reception-lecture-r1-relance-v1.md",
                     "d85bd5e467ef9a735db05afb661093e5513db7925eb9d1a573154c4fc13ff01b", True,
                     "procédure de réception v1 (arrêt de la première course)"),
    "reserve_n2": ("tete", f"{NOTRE}/analyse-blanche-noire-v3/reserve-N2-bras-moyenne-v1.md",
                   "c82b4d009cbfcdf34ceeaeb5870fb8b5f76dbfc40bb4cfce90a792f1b12aae42", True,
                   "réserve N2 (lecteur de la secondaire)"),
}
CONFIG_CANONIQUE = "1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4"
CONFIG_ATTENDUE = {"mode": "reel", "nom_sortie": "activations-p3-rejeu-v1", "couches": [7, 15, 23], "T": 10,
                   "seuil_non_conformes": 10, "chemin_table_tokenisation": TABLE_V3,
                   "table_tokenisation_sha256": PIECES["table_v3"][2], "chemin_prereg_parent": PARENT,
                   "prereg_parent_sha256": PIECES["parent"][2]}
LIGNE_104 = '"preenregistrement": prereg_info,'           # `manifeste.py` l. 104 : clé du texte qui gouverne
COMMANDE = "python -m controle_ia.runs_nuit.rejeu_activations_v3"   # `rejeu_activations_v3.COMMANDE` (l. 65)
ENTROPIE = "36410133060804533274328900142752730279"                # en-tête de l'addendum v3
CONFORMES_LONGUEUR, CONTEXTES_CONFORMES = 2236, 1782               # pré-vol (addendum v3, « Prédiction », étape 3)
RUN_PREMIERE_COURSE = "20261102-002114-r1-rejeu-reel"
ARRET_PREMIERE_COURSE = "c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07"   # procédure v1, étape C
BRANCHES_SOURCE = {"course": "calcul/r1-relance-v3-reel-v1", "reprise_e21": "calcul/r1-relance-v3-reel-v2"}
BRANCHE_VERSEMENT = "calcul/r1-r2-reel-v1"
JUGES = {"juge3b": ("20261102-004328-r2-juge3b-reel", "scores-juge3b-p3-v1.npz",
                    "10838eea884baefd1921aa7fb6f603b288fd02d46ed177845ebbda6291cdd354"),
         "juge8b": ("20261102-005048-r2-juge8b-reel", "scores-juge8b-p3-v1.npz",
                    "1ebbeff89fe7ff4a6da834651b0701b0cfde8cce9781ca6e2318224d872e8d4b")}
# méthodes de la table v3, ordre du code (`resolution_graine_v1.CORRIGEES_V3` = `resolution_tokenisation_v1.CORRIGEES`
# plus « identifiants ») ; v1 = étapes 1 à 3, v2 = extension C-6 (`rejeu_activations_v3.methode_resolution`)
METHODES_V1 = ("fins", "une_paire", "deux_paires")
METHODES_V2 = ("trois_paires", "quatre_paires_meme_action", "copie", "fenetre", "fenetre_et_paire", "deux_fenetres",
               "fin_et_paire", "fin_et_fenetre", "fin_et_deux_paires", "deux_fins_et_paire")
METHODES_V3 = METHODES_V1 + METHODES_V2 + ("identifiants",)

# ------------------------------------------------------------------ formats du fournisseur (inchangés depuis la v1)
NOM_SORTIE_R1 = CONFIG_ATTENDUE["nom_sortie"]
FICHIERS_R1 = {"moyenne": f"{NOM_SORTIE_R1}.npz", "maximum": f"{NOM_SORTIE_R1}-maximum.npz",
               "complement": f"{NOM_SORTIE_R1}-complement-hors-cout.npz"}
RESULTAT_R1, RESULTAT_JUGE, ARRET = "rejeu-activations.json", "juge-actions.json", "arret.json"
MOTIFS_R1_NUL = {"non conforme": "rejeu_non_conforme", "echec": "rejeu_en_echec", "échec": "rejeu_en_echec"}
MOTIFS_R2_NUL = ("sorties_non_livrees", "garde_N029_du_kit")
POINTEURS_R1 = {"fidelite_conforme": ["resultat", "verdict_fidelite"], "regle_repli": ["resultat", "regle_repli_appliquee"],
                "textes_sha256": ["resultat", "textes_sha256"], "couches": ["resultat", "couches"],
                "contexte_rejeu": ["resultat", "contexte"], "regle_empan": ["resultat", "regle_empan"],
                "modele": ["resultat", "modele"]}
POINTEURS_R2 = {"invite_sha256": ["resultat", "invite_sha256"], "contexte_juge": ["resultat", "contexte"],
                "modele": ["resultat", "juge"]}
CLES_TOKENISATION_LUES = ("addendum", "version_table", "table_sha256", "corrections_verifiees_au_chargement",
                          "trajectoires_identiques_base", "signales", "corrections_par_methode",
                          "par_methode_resolution", "episodes_non_resolus", "actions_non_resolues",
                          "fideles_parmi_non_resolues", "seuil_non_conformes")
# clés lues du résultat du rejeu ; aucune autre valeur n'est gardée (règle P-R5 de la fiche de réception, section 6)
CHEMINS_LUS = (("run_id",), ("manifeste_sha256",), ("resultat", "verdict_fidelite"), ("resultat", "fichiers"),
               ("resultat", "empreintes_p3", "episodes"), ("resultat", "empreintes_p3", "trajectoires_identiques"),
               ("resultat", "fidelite_toutes", "actions"), ("resultat", "fidelite_toutes", "conformes_longueur"),
               ("resultat", "fidelite_toutes", "contextes_conformes")) + tuple(
    ("resultat", "tokenisation", k) for k in CLES_TOKENISATION_LUES)
CHEMINS_LUS_ARRET = (("run_id",), ("manifeste_sha256",), ("resultat", "verdict_fidelite"))
# valeurs observées de P-R5 et lectures de l'instrument : jamais gardées, écrites ni affichées avant les analyses
INTERDITS = ("fideles", "notees", "fideles_parmi_contextes_conformes", "notees_contextes_conformes", "egalite_exacte",
             "ecart_max", "ecart_mediane", "part_fideles_parmi_notees", "p_r5_au_moins_90_pour_cent",
             "fidelite_echantillon", "controle_negatif", "activations_identiques_au_bit", "lecture",
             "regle_repli_appliquee")
CLES_ATTENDUS = {"format", "textes", "manifeste", "resultat", "fichiers_rejeu", "juges", "run_premiere_course",
                 "branches_source", "branche_versement", "episodes_non_inversibles_declares", "N_A", "interdits"}
_LIGNE = re.compile(r"^([0-9a-f]{64})  (\S.*)$")
_RUN = re.compile(r"^[0-9]{8}-[0-9]{6}-[A-Za-z0-9_.-]+$")
_RUN_REJEU = re.compile(r"^[0-9]{8}-[0-9]{6}-r1-rejeu-reel$")    # `run` du script d'instance v3, MODE=reel
_HEX40, _HEX64 = re.compile(r"[0-9a-f]{40}"), re.compile(r"[0-9a-f]{64}")


class Arret(Exception):
    def __init__(self, garde: str, message: str):
        super().__init__(f"[{garde}] {message}")
        self.garde = garde


class Controles:
    """Gardes passées, dans l'ordre (écrites dans les fiches) ; une garde fausse arrête avec son nom (R5)."""

    def __init__(self):
        self.passees = []

    def exiger(self, garde: str, condition, message) -> None:
        if not condition():
            raise Arret(garde, message() if callable(message) else message)
        if garde not in self.passees:
            self.passees.append(garde)


def empreinte_octets(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def empreinte(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def config_canonique(config) -> bytes:
    """Règle de `controle_ia.manifeste.config_canonique` (clés triées, séparateurs compacts), recopiée."""
    return json.dumps(config, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def normaliser(texte: str) -> str:
    return " ".join(texte.split())


def milliers(n: int) -> str:
    return f"{n:,}".replace(",", " ")


def ligne_compagnon(texte: str, nom: str, garde: str, quoi: str) -> str:
    lignes = [x for x in texte.splitlines() if x.strip()]
    m = _LIGNE.match(lignes[0]) if len(lignes) == 1 else None
    if m is None:
        raise Arret(garde, f"{quoi} : compagnon illisible")
    if m.group(2) != nom:
        raise Arret(garde, f"{quoi} : compagnon au nom {m.group(2)!r} au lieu de {nom!r}")
    return m.group(1)


# ================================================================== mode « avant la récupération »
def git(depot: Path, *args: str) -> bytes:
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True)
    if r.returncode != 0:
        raise Arret("piece", f"`git {' '.join(args)}` impossible ({r.stderr.decode('utf-8', 'replace').strip()[:160]}) : "
                             "R11, vérifier le commit et le chemin avant de conclure")
    return r.stdout


def lire_pieces(depot: Path, refs: dict) -> dict:
    lues = {}
    for nom, (ref, chemin, _, avec_compagnon, _) in PIECES.items():
        contenu = git(depot, "show", f"{refs[ref]}:{chemin}")
        comp = git(depot, "show", f"{refs[ref]}:{chemin}{SUFFIXE}").decode("utf-8") if avec_compagnon else None
        lues[nom] = {"contenu": contenu, "compagnon": comp, "commit": refs[ref], "chemin": chemin}
    return lues


def controler_configuration(ctl: Controles, octets: bytes) -> dict:
    try:
        config = json.loads(octets)
    except ValueError:
        config = None
    ctl.exiger("config-table", lambda: isinstance(config, dict) and all(
        config.get(k) == v for k, v in CONFIG_ATTENDUE.items()), lambda: "configuration v5 : " + "; ".join(
        f"{k} = {(config or {}).get(k)!r} (attendu {v!r})" for k, v in CONFIG_ATTENDUE.items()
        if not isinstance(config, dict) or config.get(k) != v))
    canon = empreinte_octets(config_canonique(config))
    ctl.exiger("canonique", lambda: canon == CONFIG_CANONIQUE,
               lambda: f"empreinte canonique de la configuration v5 {canon[:12]}… ≠ citée {CONFIG_CANONIQUE[:12]}…")
    return config


def controler_table(ctl: Controles, octets: bytes, config: dict) -> dict:
    try:
        t = json.loads(octets)
    except ValueError:
        t = None
    ecarts = []
    if not isinstance(t, dict) or not isinstance(t.get("episodes"), list) or not isinstance(t.get("comptes"), dict):
        ecarts.append("structure (episodes, comptes) absente")
    else:
        c, ents = t["comptes"], t["episodes"]
        meth = [e.get("methode") for e in ents if isinstance(e, dict)]
        if t.get("version") != 3:
            ecarts.append(f"version {t.get('version')!r} ≠ 3")
        if len(meth) != len(ents) or len(set(e.get("episode") for e in ents)) != len(ents):
            ecarts.append("entrée hors de forme ou épisode en double")
        if "non_resolu" in meth or c.get("non_resolu") != 0 or t.get("resultat_hors_table") != []:
            ecarts.append("entrée `non_resolu` ou épisode hors table (règle B sans objet exige 0, E2)")
        if any(m not in METHODES_V3 for m in meth):
            ecarts.append(f"méthode inconnue {sorted(set(meth) - set(METHODES_V3))}")
        if any(c.get(m) != meth.count(m) for m in METHODES_V3):
            ecarts.append("comptes par méthode ≠ entrées")
        if not (len(ents) == c.get("signales") == t.get("corrections_verifiees")):
            ecarts.append("entrées, signalés et corrections vérifiées différents")
        if c.get("identiques_apres_table") != (c.get("identiques_base") or 0) + len(ents) or \
                c.get("identiques_apres_table") != c.get("conformes_longueur"):
            ecarts.append("trajectoires identiques après la table ≠ base + corrections, ou ≠ conformes en longueur (E4)")
        for k in ("textes_sha256", "fiches_sha256", "scores_sha256"):
            if t.get(k) != config.get(k):
                ecarts.append(f"{k} de la table ≠ configuration")
    ctl.exiger("table", lambda: not ecarts, lambda: "table v3 : " + " ; ".join(ecarts))
    return t


def deriver_attendus(table: dict, config: dict, refs: dict) -> dict:
    c, T = table["comptes"], int(config["T"])
    par_methode = {m: int(c[m]) for m in METHODES_V3}
    corrigees = sum(par_methode.values())
    comptes = {
        "empreintes_p3.episodes": c["episodes"],
        "empreintes_p3.trajectoires_identiques": c["identiques_apres_table"],
        "fidelite_toutes.actions": c["episodes"] * T,
        "fidelite_toutes.conformes_longueur": CONFORMES_LONGUEUR,
        "fidelite_toutes.contextes_conformes": CONTEXTES_CONFORMES,
        "tokenisation.version_table": table["version"],
        "tokenisation.corrections_verifiees_au_chargement": table["corrections_verifiees"],
        "tokenisation.trajectoires_identiques_base": c["identiques_base"],
        "tokenisation.signales": c["signales"],
        "tokenisation.corrections_par_methode": par_methode,
        "tokenisation.par_methode_resolution": {"v1": sum(par_methode[m] for m in METHODES_V1),
                                                "v2": sum(par_methode[m] for m in METHODES_V2),
                                                "identifiants": par_methode["identifiants"],
                                                "aucune": c["episodes"] - corrigees},
        "tokenisation.episodes_non_resolus": [],
        "tokenisation.actions_non_resolues": 0,
        "tokenisation.fideles_parmi_non_resolues": 0,
        "tokenisation.seuil_non_conformes": config["seuil_non_conformes"],
    }
    textes = {nom: {"chemin": ch, "commit": refs[ref], "sha256": sha} for nom, (ref, ch, sha, _, _) in PIECES.items()}
    textes["configuration_v5"]["sha256_canonique"] = CONFIG_CANONIQUE
    return {
        "format": FORMAT_ATTENDUS,
        "textes": textes,
        "manifeste": {"commande": COMMANDE, "decisif": True,
                      "preenregistrement": {"chemin": ADDENDUM_V3, "sha256": PIECES["addendum_v3"][2]},
                      "config_sha256": CONFIG_CANONIQUE, "chemin_table_tokenisation": TABLE_V3,
                      "table_tokenisation_sha256": PIECES["table_v3"][2], "commit": refs["scellement"],
                      "depot_propre": True, "reserves": [], "entropie": ENTROPIE},
        "resultat": {"verdict_fidelite": "conforme", "tokenisation.table_sha256": PIECES["table_v3"][2],
                     "tokenisation.addendum": ADDENDUM_V2, "comptes": comptes},
        "fichiers_rejeu": dict(FICHIERS_R1),
        "juges": {k: {"run": r, "fichier": f, "sha256": s} for k, (r, f, s) in JUGES.items()},
        "run_premiere_course": RUN_PREMIERE_COURSE, "arret_premiere_course_sha256": ARRET_PREMIERE_COURSE,
        "branches_source": dict(BRANCHES_SOURCE), "branche_versement": BRANCHE_VERSEMENT,
        "episodes_non_inversibles_declares": [], "N_A": "sans objet (E19 de l'addendum v3 ; concordance § 7)",
        "interdits": list(INTERDITS),
    }


def fragments_du_texte(att: dict) -> list:
    """Attentes que le texte scellé doit porter, à l'identique après normalisation des blancs (étape 3, en-tête, E16)."""
    c, m = att["resultat"]["comptes"], att["manifeste"]
    pm, pr = c["tokenisation.corrections_par_methode"], c["tokenisation.par_methode_resolution"]
    non_nulles = ", ".join(f"{k} {v}" for k, v in pm.items() if v)
    juges = att["juges"]
    return [
        f"manifeste : `commande` = `{m['commande']}`, `preenregistrement.chemin` = `{m['preenregistrement']['chemin']}` "
        "et `preenregistrement.sha256` = empreinte de ce texte scellé, `decisif` vrai ;",
        f"`verdict_fidelite` = « {att['resultat']['verdict_fidelite']} » ;",
        f"`empreintes_p3.episodes` = {milliers(c['empreintes_p3.episodes'])}, `empreintes_p3.trajectoires_identiques` = "
        f"{milliers(c['empreintes_p3.trajectoires_identiques'])} ;",
        f"`fidelite_toutes.actions` = {milliers(c['fidelite_toutes.actions'])}, `conformes_longueur` = "
        f"{milliers(c['fidelite_toutes.conformes_longueur'])}, `contextes_conformes` = "
        f"{milliers(c['fidelite_toutes.contextes_conformes'])} ;",
        f"`tokenisation.table_sha256` = `{att['resultat']['tokenisation.table_sha256']}`, `version_table` = "
        f"{c['tokenisation.version_table']}, `corrections_verifiees_au_chargement` = "
        f"{c['tokenisation.corrections_verifiees_au_chargement']}, `trajectoires_identiques_base` = "
        f"{c['tokenisation.trajectoires_identiques_base']}, `signales` = {c['tokenisation.signales']},",
        f"`corrections_par_methode` = {non_nulles} (0 pour les autres méthodes), `par_methode_resolution` = "
        f"v1 {pr['v1']}, v2 {pr['v2']}, identifiants {pr['identifiants']}, aucune {pr['aucune']}, "
        f"`episodes_non_resolus` = {json.dumps(c['tokenisation.episodes_non_resolus'])}, `actions_non_resolues` = "
        f"{c['tokenisation.actions_non_resolues']}, `fideles_parmi_non_resolues` = "
        f"{c['tokenisation.fideles_parmi_non_resolues']}, `seuil_non_conformes` = {c['tokenisation.seuil_non_conformes']}, "
        f"`addendum` = `{att['resultat']['tokenisation.addendum']}` (E16)",
        "le texte qui gouverne la course est celui du champ `preenregistrement` du manifeste de run (clés `chemin` et "
        "`sha256`, `src/controle_ia/manifeste.py` l. 104)",
        f"Entropie : `{m['entropie']}`",
        f"Configuration du rejeu (empreinte canonique) : `{m['config_sha256']}`",
        f"Table de tokenisation (empreinte du fichier) : `{m['table_tokenisation_sha256']}`",
        f"Chemin de la configuration du rejeu : `{CONFIG_V5}`",
        f"Chemin de la table de tokenisation : `{m['chemin_table_tokenisation']}`",
        f"Chemin du préenregistrement parent : `{PARENT}`",
        f"Commit du code d'analyse : `{COMMIT_CODE_CITE}`",
        *(f"`donnees/{j['run']}/{j['fichier']}`, `{j['sha256']}`" for j in juges.values()),
        f"`{att['branches_source']['course']}`", f"`{att['branches_source']['reprise_e21']}`",
        f"`{att['branche_versement']}`", "GO-2026-11-02-27",
    ]


def references_de_calcul(depot: Path) -> tuple:
    refs = [x for x in git(depot, "for-each-ref", "--format=%(refname)").decode("utf-8").splitlines() if x]
    return refs, [r for r in refs if re.search(r"(^|/)calcul/", r)], [r for r in refs if "donnees" in r]


def construire_avant(a) -> tuple:
    ctl = Controles()
    depot = Path(a.depot).resolve()
    refs_lues, calcul, donnees = references_de_calcul(depot)
    ctl.exiger("recuperation", lambda: not calcul and not donnees,
               lambda: f"références {calcul + donnees} présentes : une récupération a déjà eu lieu, la fiche de réception "
                       "s'écrit et se scelle avant (C-1) : nœud, rien n'est écrit")
    refs = {}
    for nom, ref in (("scellement", a.commit_scellement), ("principale", a.commit_principale),
                     ("secondaire", a.commit_secondaire), ("tete", a.ref_tete)):
        refs[nom] = git(depot, "rev-parse", "--verify", f"{ref}^{{commit}}").decode("utf-8").strip()
    lues = lire_pieces(depot, refs)
    config = controler_configuration(ctl, lues["configuration_v5"]["contenu"])
    table = controler_table(ctl, lues["table_v3"]["contenu"], config)
    lignes = lues["manifeste_py"]["contenu"].decode("utf-8", "replace").splitlines()
    ctl.exiger("ligne-104", lambda: len(lignes) >= 104 and lignes[103].strip() == LIGNE_104,
               lambda: f"manifeste.py l. 104 = {lignes[103].strip() if len(lignes) >= 104 else None!r} ≠ {LIGNE_104!r} : "
                       "la clé du texte qui gouverne n'est pas celle qu'attend la fiche")
    att = deriver_attendus(table, config, refs)
    texte = normaliser(lues["addendum_v3"]["contenu"].decode("utf-8"))
    manquants = [f for f in fragments_du_texte(att) if normaliser(f) not in texte]
    ctl.exiger("attentes-texte", lambda: not manquants,
               lambda: "le texte scellé ne porte pas ces attentes (la fiche ne peut pas les attendre) : "
                       + " | ".join(manquants))
    for nom, x in lues.items():
        h = empreinte_octets(x["contenu"])
        ctl.exiger("piece", lambda: h == PIECES[nom][2],
                   lambda: f"{nom} ({x['chemin']} à {x['commit'][:12]}) : sha256 {h[:12]}… ≠ cité {PIECES[nom][2][:12]}…")
    for nom, x in lues.items():
        if x["compagnon"] is None:
            continue
        sceau = ligne_compagnon(x["compagnon"], Path(x["chemin"]).name, "compagnon", nom)
        ctl.exiger("compagnon", lambda: sceau == empreinte_octets(x["contenu"]),
                   lambda: f"{nom} : compagnon {sceau[:12]}… ≠ fichier au même commit (sceau faux)")
    constat = {"references_lues": len(refs_lues), "calcul": calcul, "donnees": donnees, "refs": refs,
               "methodes": {m: n for m, n in att["resultat"]["comptes"]["tokenisation.corrections_par_methode"].items() if n},
               "table": {k: table["comptes"][k] for k in ("episodes", "conformes_longueur", "identiques_base", "signales",
                                                          "identiques_apres_table", "non_resolu")},
               "corrections_verifiees": table["corrections_verifiees"], "fins_du_format": table.get("fins_du_format"),
               "resultat_graine_sha256": table.get("resultat_graine_sha256"), "table_v2_sha256": table.get("table_v2_sha256")}
    return att, constat, ctl


def rendre_fiche(att: dict, constat: dict, ctl: Controles, qui: str, quand: str, sha_script: str) -> str:
    t, m, r = att["textes"], att["manifeste"], att["resultat"]
    c = r["comptes"]
    lignes_pieces = "\n".join(
        f"| {nom} — {PIECES[nom][4]} | `{x['chemin']}` | `{x['commit'][:12]}` | `{x['sha256']}` | "
        f"{'compagnon égal au même commit' if PIECES[nom][3] else 'sans compagnon (déclaré)'} |" for nom, x in t.items())
    lignes_comptes = "\n".join(f"| `resultat.{k}` | `{json.dumps(v, ensure_ascii=False)}` |" for k, v in c.items())
    interdits = ", ".join(f"`{k}`" for k in INTERDITS)
    bloc = json.dumps(att, indent=1, ensure_ascii=False, sort_keys=True)
    return f"""# Fiche de réception de la relance de R1 sur la table de tokenisation v3 (addendum v3 de R1) — v1

- **Ce document** : la fiche de réception de conv-audit, c'est-à-dire son document de contrôles (règle C-1 de notre
  concordance `8482b4cd…` ; addendum v3, E8 (e), étape 3 et « Liste d'arrêt » ; GO-2026-11-02-27). Il est distinct des
  deux fiches JSON de nos analyses scellées (`prereg/fiche-reception-principale-r1-r2-v1.json`,
  `prereg/fiche-reception-blanche-noire-v3.json`), qui s'écrivent après le versement, par le même script en mode
  « après le versement », qui relit cette fiche.
- **Écrite par** `{NOM_SCRIPT}` (sha256 `{sha_script}`), mode « avant la récupération », le {quand} (horloge du système,
  temps universel), pour : {qui}.
- **Moment du scellement : avant toute récupération des sorties de la course** par session-depot (C-1). La session la
  scelle (`python -m controle_ia.scellement sceller`), la commite, la pousse, puis envoie au canal son chemin et son
  empreinte ; session-depot vérifie l'empreinte (compagnon `.sha256` égal) ; sans ce message, rien n'est récupéré. La
  création de l'instance n'en dépend pas (addendum v3, E8 (d)). Étape 0 de la procédure de réception v2.
- **Constat à l'écriture** : {constat['references_lues']} références lues dans le dépôt ; aucune `calcul/…` ; aucune dont
  le nom contient `donnees`. Aucune sortie de la course n'existe ici ; rien n'en a été lu. Commits résolus : scellement
  `{constat['refs']['scellement']}`, principale `{constat['refs']['principale']}`, secondaire
  `{constat['refs']['secondaire']}`, tête de la branche de travail `{constat['refs']['tete']}`.
- **Gardes passées par le script** : {', '.join(ctl.passees)}.

## 1. Textes qui encadrent la réception (lus par `git show <commit>:<chemin>`, empreintes recalculées)

| pièce | chemin | commit | sha256 | sceau |
|---|---|---|---|---|
{lignes_pieces}

- Configuration v5 : empreinte canonique `{t['configuration_v5']['sha256_canonique']}` (JSON aux clés triées, séparateurs
  compacts : règle de `manifeste.config_canonique`) ; elle cite la table v3 (chemin et empreinte), le parent (chemin et
  empreinte), `nom_sortie` = `{CONFIG_ATTENDUE['nom_sortie']}`, couches {CONFIG_ATTENDUE['couches']},
  `seuil_non_conformes` = {CONFIG_ATTENDUE['seuil_non_conformes']} (sans effet, E3), mode `reel`.
- Table v3 (structure et comptes seulement) : version 3 ; {constat['table']['episodes']} épisodes,
  {constat['table']['conformes_longueur']} conformes en longueur, {constat['table']['identiques_base']} identiques à la
  base, {constat['table']['signales']} signalés, {constat['corrections_verifiees']} corrections vérifiées,
  {constat['table']['identiques_apres_table']} trajectoires identiques après la table, `non_resolu` =
  {constat['table']['non_resolu']} ; méthodes : {', '.join(f'{k} {v}' for k, v in constat['methodes'].items())} ;
  fins du format {constat['fins_du_format']} ; `resultat_graine_sha256` = `{constat['resultat_graine_sha256']}` ;
  `table_v2_sha256` = `{constat['table_v2_sha256']}`.
- Code : commit cité par l'addendum v3 `{COMMIT_CODE_CITE}` ; le script ne voit que le commit de scellement (empreintes
  ci-dessus) ; l'identité de l'arbre `src`, `tests`, `scripts` entre les deux est vérifiée par la procédure v2 (étape 0).
  `manifeste.py` l. 104 au commit de scellement : `{LIGNE_104}` (clé réelle du texte qui gouverne).
- Les « Attentes de réception » de l'addendum v3 (étape 3), son en-tête (entropie, empreintes, chemins, commit du code),
  E16 et la section « R2 » portent mot pour mot les valeurs des sections 3 à 5 (garde `attentes-texte`).
- Concordance de conv-audit sur la **version scellée** : condition du lancement chez session-depot (chemin et empreinte
  consignés dans `docs/notes/runs-r1-r2-r4-v1/concordance-relance-v3-consignee-v1.md`) ; non citée ici, elle est la
  précondition P2 de la procédure v2, vérifiée avant l'étape A.

## 2. Ce qui sera lancé, puis versé (rappel du texte scellé ; constaté à la réception)

- GO-2026-11-02-27 (plafond 60 USD, échéance 2026-11-16) ; commit lancé = commit de scellement `{m['commit']}` ;
  course poussée sur `{att['branches_source']['course']}` (ou `{att['branches_source']['reprise_e21']}` après une reprise
  E21) ; puis versement à l'octet sur `{att['branche_versement']}` par un commit neuf, en avance rapide, sans réécriture.
- Voie de réception de conv-audit : la seule refspec
  `+refs/heads/{att['branche_versement']}:refs/remotes/origin/{att['branche_versement']}` ; jamais de `git merge` d'une
  branche `calcul/…` ; `git for-each-ref refs/remotes | grep -c donnees` = 0 après la récupération.
- Run lu : le seul nommé par le message de versement de session-depot, de la forme `AAAAMMJJ-HHMMSS-r1-rejeu-reel`,
  autre que la première course `{att['run_premiere_course']}` (arrêtée ; son `arret.json`, haché par un tube et jamais
  ouvert, doit rester `{att['arret_premiere_course_sha256']}`). Juges : ceux déjà versés, non relancés (section 5).

## 3. Manifeste du rejeu `runs/<run>/manifeste.json` (sceau vérifié ; tout écart arrête)

| clé | attendu | garde |
|---|---|---|
| `run_id` | le run nommé par le fournisseur | `rattachement` |
| `commande` | `{m['commande']}` | `commande` |
| `decisif` | `true` | `decisif` |
| `preenregistrement` (clé réelle, `manifeste.py` l. 104) | `{json.dumps(m['preenregistrement'], ensure_ascii=False)}` | `texte` |
| `config_sha256` | `{m['config_sha256']}`, égal au recalcul canonique de `config` | `configuration` |
| `config.chemin_table_tokenisation`, `config.table_tokenisation_sha256` | `{m['chemin_table_tokenisation']}`, `{m['table_tokenisation_sha256']}` | `configuration` |
| `commit` | `{m['commit']}` (commit de scellement lancé) | `commit` |
| `depot_propre`, `reserves` | `true`, `[]` | `commit` |
| `graines.fidelite.entropie` | `{m['entropie']}` (même entropie, aussi après une reprise E21) | `entropie` |

## 4. Résultat `diag/<run>/rejeu-activations.json` (sceau, rattachement au manifeste ; tout écart arrête)

| clé | attendu |
|---|---|
| `run_id`, `manifeste_sha256` | le run ; l'empreinte du fichier du manifeste (garde `rattachement`) |
| `resultat.verdict_fidelite` | « {r['verdict_fidelite']} » ; sinon le run porte `arret.json` (section 7) |
| `resultat.tokenisation.table_sha256` | `{r['tokenisation.table_sha256']}` : **comparée, refus sinon** (garde `table-comparee`) |
| `resultat.tokenisation.addendum` | `{r['tokenisation.addendum']}` **à l'identique** : provenance de la table v3 (E16), jamais le texte qui gouverne, qui se lit dans `preenregistrement` du manifeste (section 3) ; toute autre valeur signale un autre code : arrêt (garde `provenance`) |
| `resultat.fichiers` | les empreintes des trois `.npz` versés, égales à leurs compagnons |
{lignes_comptes}

Les comptes ci-dessus sont fixés par la table et la configuration (et le pré-vol pour 2 236 et 1 782), quasi certains :
un écart signale une autre course ou une autre table (garde `comptes`) : arrêt, nœud de Lazar.

## 5. Fichiers attendus (noms exacts, empreintes égales aux compagnons ; un nom en plus ou en moins arrête)

- `runs/<run>/manifeste.json` ; `diag/<run>/rejeu-activations.json` (ou `diag/<run>/arret.json` seul, sans `donnees/<run>`) ;
  `donnees/<run>/{FICHIERS_R1['moyenne']}`, `donnees/<run>/{FICHIERS_R1['maximum']}`,
  `donnees/<run>/{FICHIERS_R1['complement']}` ; chacun avec son compagnon `.sha256`.
- Juges (R2 ne se relance pas ; addendum v3, « R2 ») : `donnees/{att['juges']['juge3b']['run']}/{att['juges']['juge3b']['fichier']}`
  = `{att['juges']['juge3b']['sha256']}` ; `donnees/{att['juges']['juge8b']['run']}/{att['juges']['juge8b']['fichier']}`
  = `{att['juges']['juge8b']['sha256']}` ; avec leurs `runs/<juge>/manifeste.json` et `diag/<juge>/juge-actions.json`
  (garde `juges`). Aucun `.npz` n'est ouvert par la réception.

## 6. Non lu avant les analyses (valeurs observées de P-R5 et lectures de l'instrument)

- Clés du résultat jamais gardées, écrites ni affichées par le script : {interdits} (sous `resultat`,
  `resultat.fidelite_toutes`, `resultat.tokenisation`, `resultat.empreintes_p3`). Elles sont lues par nos analyses
  scellées elles-mêmes, après le scellement de nos fiches JSON.
- Ni la session ni le script n'ouvrent les traces de l'instance (`traces/…/r1-rejeu.json` y recopie la sortie standard
  du module, P-R5 comprise), ni la ligne de journal `etape=fin fideles=… notees=…`. Le message de versement ne doit pas
  la relayer ; s'il le fait, la session le déclare au registre (« vu avant les analyses ») et aux lecteurs R13.

## 7. Règles

- **Épisodes non inversibles déclarés : aucun** (liste vide fixée : E2, E19). **N-A : sans objet** pour le lecteur R13 de
  la principale (E19 ; concordance `8482b4cd…` § 7 ; aucune décision nouvelle de Lazar).
- **Réserve sur HG-2** (addendum v3, « Hypothèse » et ligne ajoutée des critères gelés ; verdict `64fab1a5…`) : rapportée
  à côté des résultats, sans changer aucune classe.
- **Arrêt de la course** : `diag/<run>/arret.json` seul (aucun `donnees/<run>`) ; seuls `verdict_fidelite` (motif fermé :
  « non conforme » → `rejeu_non_conforme`, « echec » → `rejeu_en_echec`) et le rattachement sont lus ; fiches `R1: null`
  avec ce motif ; les contrôles du manifeste (section 3) valent aussi pour un run arrêté.
- **Reprise E21** (une seule, erreur d'infrastructure, aucun fichier d'activations écrit) : le message de versement nomme
  la course arrêtée, l'empreinte de son `arret.json` s'il existe et le message d'annonce de la reprise, fait avant la
  création ; la branche source est alors `{att['branches_source']['reprise_e21']}` ; la course arrêtée est notée dans
  les fiches JSON, rien n'en est ouvert ; on lit la seule course nommée ; mêmes commit et entropie (section 3) ; les
  lignes `etape=fidelite lecture=…` et `etape=controle_negatif lecture=…` de son journal, si elles existent, vont aux
  lecteurs R13, rapportées à côté (réserve d'instrument si elles diffèrent).
- **Tout écart** à cette fiche arrête la réception : rien n'est lancé, rien n'est corrigé à la main, Lazar est prévenu
  (écart au texte scellé ou autre course : nœud). Une fiche scellée ne se réécrit pas : version nouvelle, nom nouveau.

## 8. Bloc d'attendus (lu par le mode « après le versement » ; mêmes valeurs que les sections 3 à 7)

{DEBUT_BLOC}
```json
{bloc}
```
{FIN_BLOC}
"""


# ================================================================== mode « après le versement »
def extraire_bloc(texte: str):
    if texte.count(DEBUT_BLOC) != 1 or texte.count(FIN_BLOC) != 1:
        return None
    corps = texte.split(DEBUT_BLOC, 1)[1].split(FIN_BLOC, 1)[0].strip()
    if not (corps.startswith("```json") and corps.endswith("```")):
        return None
    return corps[len("```json"):-3]


def lire_attendus(ctl: Controles, fiche: Path, sha_annoncee: str) -> tuple:
    comp = Path(str(fiche) + SUFFIXE)
    ctl.exiger("fiche", lambda: fiche.is_file(), f"fiche de réception {fiche} absente (R11 : vérifier sur disque)")
    ctl.exiger("fiche", lambda: comp.is_file(),
               f"fiche de réception non scellée : {comp.name} absent (C-1 : scellée avant la récupération)")
    h = empreinte(fiche)
    sceau = ligne_compagnon(comp.read_text(encoding="utf-8"), fiche.name, "fiche", "fiche de réception")
    ctl.exiger("fiche", lambda: h == sceau, f"fiche de réception {h[:12]}… ≠ son compagnon {sceau[:12]}… (modifiée)")
    ctl.exiger("fiche", lambda: h == sha_annoncee,
               f"fiche de réception {h[:12]}… ≠ empreinte envoyée au canal {sha_annoncee[:12]}…")
    bloc = extraire_bloc(fiche.read_text(encoding="utf-8"))
    try:
        att = json.loads(bloc) if bloc is not None else None
    except ValueError:
        att = None
    ctl.exiger("attendus", lambda: isinstance(att, dict) and att.get("format") == FORMAT_ATTENDUS
               and CLES_ATTENDUS <= set(att), "bloc d'attendus absent, répété, illisible ou d'un autre format")
    return att, h


def lire_compagnon(c: Path, nom: str) -> str:
    return ligne_compagnon(c.read_text(encoding="utf-8"), nom, "fichiers", str(c))


def fichier_verifie(racine: Path, rel: str, inventaire: dict) -> dict:
    """Empreinte calculée, égale au compagnon du fournisseur ; sinon arrêt. Rien n'est ouvert autrement."""
    p = racine / rel
    if not p.is_file():
        raise Arret("fichiers", f"{rel} absent sur disque (R11 : vérifier sur disque et par `git ls-tree` avant de conclure)")
    c = Path(str(p) + SUFFIXE)
    if not c.is_file():
        raise Arret("fichiers", f"{rel} : compagnon {c.name} absent")
    h, attendue = empreinte(p), lire_compagnon(c, p.name)
    if h != attendue:
        raise Arret("fichiers", f"{rel} : empreinte calculée {h[:12]}… ≠ compagnon {attendue[:12]}…")
    inventaire[rel] = h
    return {"chemin": rel, "sha256": h}


def noms(racine: Path, dossier: str) -> set:
    d = racine / dossier
    if not d.is_dir():
        raise Arret("fichiers", f"dossier {dossier} absent")
    return {p.name for p in d.iterdir() if p.is_file()}


def exiger_noms(racine: Path, dossier: str, attendus: set) -> None:
    presents, avec = noms(racine, dossier), attendus | {n + SUFFIXE for n in attendus}
    if presents - avec:
        raise Arret("fichiers", f"{dossier} : nom(s) inattendu(s) {sorted(presents - avec)} (rien n'est deviné : nœud)")
    if avec - presents:
        raise Arret("fichiers", f"{dossier} : fichier(s) attendu(s) absent(s) {sorted(avec - presents)}")


def exiger_run(nom: str, quoi: str) -> str:
    if not _RUN.match(nom or ""):
        raise Arret("forme", f"{quoi} : nom de run {nom!r} hors du format AAAAMMJJ-HHMMSS-<nom>")
    return nom


def lire_json(p: Path, ouverts: list) -> dict:
    ouverts.append(str(p))
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Arret("forme", f"{p} : JSON illisible ({type(e).__name__})") from None
    if not isinstance(doc, dict):
        raise Arret("forme", f"{p} : objet JSON attendu")
    return doc


def resoudre(doc, chemin):
    v = doc
    for k in chemin:
        if isinstance(v, dict) and k in v:
            v = v[k]
        else:
            raise Arret("forme", f"clé {'.'.join(map(str, chemin))} absente du fichier du fournisseur")
    return v


def filtrer(doc, chemins) -> dict:
    """Du document chargé, seules les valeurs des chemins nommés sont gardées et rendues ; le document entier n'est
    jamais rendu, écrit ni affiché (règle P-R5 de la fiche de réception, section 6)."""
    garde = {}  # filtre
    for ch in chemins:
        garde[".".join(ch)] = resoudre(doc, ch)
    return garde


def cles_interdites(obj, acc=None) -> set:
    acc = set() if acc is None else acc
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in INTERDITS:
                acc.add(k)
            cles_interdites(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            cles_interdites(v, acc)
    return acc


def nombres_dans(obj, acc=None) -> list:
    acc = [] if acc is None else acc
    if isinstance(obj, dict):
        for v in obj.values():
            nombres_dans(v, acc)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            nombres_dans(v, acc)
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        acc.append(obj)
    return acc


def exiger_sans_fuite(ctl: Controles, *sorties) -> None:
    """Garde « P-R5 » sur les fiches JSON avant écriture : aucune clé interdite, aucun nombre (la fiche ne contient que
    chemins, empreintes, pointeurs et motifs : analyse secondaire scellée, l. 24 ; le nombre n'est jamais affiché)."""
    trouvees = sorted(cles_interdites(list(sorties)))
    ctl.exiger("P-R5", lambda: not trouvees,
               lambda: f"une sortie porterait des valeurs non lues avant les analyses (clés {trouvees}) : rien n'est écrit")
    nombres = nombres_dans(list(sorties))
    ctl.exiger("P-R5", lambda: not nombres,
               lambda: f"une fiche porterait {len(nombres)} nombre(s), or elle ne contient que chemins, empreintes, pointeurs "
                       "et motifs (analyse secondaire, l. 24) : rien n'est écrit")


def controler_manifeste(ctl: Controles, m: dict, rejeu: str, att: dict) -> None:
    am = att["manifeste"]
    ctl.exiger("rattachement", lambda: m.get("run_id") == rejeu, lambda: f"manifeste : run_id {m.get('run_id')!r} ≠ {rejeu}")
    ctl.exiger("texte", lambda: m.get("preenregistrement") == am["preenregistrement"],
               lambda: f"texte qui gouverne (clé `preenregistrement`, manifeste.py l. 104) = {m.get('preenregistrement')!r}"
                       f" ≠ attendu {am['preenregistrement']!r}")
    ctl.exiger("commande", lambda: m.get("commande") == am["commande"],
               lambda: f"commande du manifeste {m.get('commande')!r} ≠ {am['commande']!r}")
    ctl.exiger("decisif", lambda: m.get("decisif") is True, lambda: f"manifeste : decisif = {m.get('decisif')!r} ≠ true")
    cfg = m.get("config") if isinstance(m.get("config"), dict) else {}
    ctl.exiger("configuration", lambda: cfg.get("chemin_table_tokenisation") == am["chemin_table_tokenisation"]
               and cfg.get("table_tokenisation_sha256") == am["table_tokenisation_sha256"],
               lambda: f"table citée par la configuration du manifeste {cfg.get('chemin_table_tokenisation')!r}, "
                       f"{str(cfg.get('table_tokenisation_sha256'))[:12]}… ≠ table v3 attendue")
    ctl.exiger("configuration", lambda: m.get("config_sha256") == am["config_sha256"],
               lambda: f"empreinte canonique de la configuration {str(m.get('config_sha256'))[:12]}… ≠ attendue "
                       f"{am['config_sha256'][:12]}…")
    canon = empreinte_octets(config_canonique(m.get("config")))
    ctl.exiger("configuration", lambda: canon == m.get("config_sha256"),
               lambda: f"recalcul canonique de `config` {canon[:12]}… ≠ `config_sha256` du manifeste")
    ctl.exiger("commit", lambda: m.get("commit") == am["commit"],
               lambda: f"commit du manifeste {m.get('commit')!r} ≠ commit de scellement lancé {am['commit']}")
    ctl.exiger("commit", lambda: m.get("depot_propre") is True and m.get("reserves") == [],
               lambda: f"arbre non propre au lancement (depot_propre = {m.get('depot_propre')!r}, réserves {m.get('reserves')!r})")
    graine = (m.get("graines") or {}).get("fidelite") if isinstance(m.get("graines"), dict) else None
    ctl.exiger("entropie", lambda: isinstance(graine, dict) and graine.get("entropie") == am["entropie"],
               lambda: f"entropie de la graine « fidelite » {(graine or {}).get('entropie')!r} ≠ citée {am['entropie']}")


def controler_resultat(ctl: Controles, lus: dict, sha_manifeste: str, rejeu: str, att: dict) -> None:
    ar = att["resultat"]
    ctl.exiger("rattachement", lambda: lus["run_id"] == rejeu and lus["manifeste_sha256"] == sha_manifeste,
               lambda: f"{RESULTAT_R1} : run_id {lus['run_id']!r} ou manifeste {str(lus['manifeste_sha256'])[:12]}… "
                       "≠ run et manifeste versés")
    ctl.exiger("table-comparee", lambda: lus["resultat.tokenisation.table_sha256"] == ar["tokenisation.table_sha256"],
               lambda: f"tokenisation.table_sha256 = {str(lus['resultat.tokenisation.table_sha256'])[:12]}… ≠ table v3 "
                       f"{ar['tokenisation.table_sha256'][:12]}… : autre table, rien n'est lancé")
    ctl.exiger("provenance", lambda: lus["resultat.tokenisation.addendum"] == ar["tokenisation.addendum"],
               lambda: f"tokenisation.addendum = {lus['resultat.tokenisation.addendum']!r} ≠ {ar['tokenisation.addendum']!r} "
                       "à l'identique (E16 : autre code)")
    ecarts = [k for k, v in ar["comptes"].items() if lus["resultat." + k] != v]
    ctl.exiger("comptes", lambda: not ecarts, lambda: "comptes ≠ fiche : " + " ; ".join(
        f"{k} = {lus['resultat.' + k]!r} (attendu {ar['comptes'][k]!r})" for k in ecarts))


def controler_e21(ctl: Controles, a, rejeu: str, att: dict) -> dict:
    if a.course_arretee_e21:
        x = a.course_arretee_e21
        ctl.exiger("e21", lambda: bool(_RUN_REJEU.match(x)) and x not in (rejeu, att["run_premiere_course"]),
                   f"course arrêtée E21 {x!r} : nom hors forme, ou égal au run lu ou à la première course")
        ctl.exiger("e21", lambda: bool(a.annonce_e21), "reprise E21 sans le message d'annonce fait avant la création")
        ctl.exiger("e21", lambda: a.arret_e21_sha256 == "absent" or bool(_HEX64.fullmatch(a.arret_e21_sha256 or "")),
                   "reprise E21 : empreinte de l'arret.json de la course arrêtée (64 hex) ou « absent » exigée")
        ctl.exiger("e21", lambda: a.branche_source == att["branches_source"]["reprise_e21"],
                   f"reprise E21 : branche source {a.branche_source!r} ≠ {att['branches_source']['reprise_e21']!r}")
        return {"reprise": True, "course_arretee": x, "arret_json_sha256": a.arret_e21_sha256, "annonce": a.annonce_e21,
                "branche_source": a.branche_source, "lue": False}
    ctl.exiger("e21", lambda: not a.annonce_e21 and not a.arret_e21_sha256
               and a.branche_source == att["branches_source"]["course"],
               f"sans reprise E21 : ni annonce ni arret.json de course arrêtée, branche source "
               f"{att['branches_source']['course']!r} (reçu {a.branche_source!r})")
    return {"reprise": False, "branche_source": a.branche_source}


def construire_apres(racine: Path, a) -> tuple:
    ctl = Controles()
    att, sha_fiche = lire_attendus(ctl, Path(a.fiche_reception).resolve(), a.fiche_reception_sha256)
    inventaire, ouverts, notes = {}, [], []
    rejeu = exiger_run(a.rejeu, "rejeu")
    ctl.exiger("nom-rejeu", lambda: bool(_RUN_REJEU.match(rejeu)) and rejeu != att["run_premiere_course"],
               f"run {rejeu!r} : un run de la relance s'appelle AAAAMMJJ-HHMMSS-r1-rejeu-reel et n'est pas la première "
               f"course {att['run_premiere_course']}")
    e21 = controler_e21(ctl, a, rejeu, att)
    exiger_noms(racine, f"runs/{rejeu}", {"manifeste.json"})
    manifeste_rejeu = fichier_verifie(racine, f"runs/{rejeu}/manifeste.json", inventaire)
    controler_manifeste(ctl, lire_json(racine / manifeste_rejeu["chemin"], ouverts), rejeu, att)
    diag = noms(racine, f"diag/{rejeu}")
    a_resultat, a_arret = RESULTAT_R1 in diag, ARRET in diag
    if a_resultat == a_arret:
        raise Arret("fichiers", f"diag/{rejeu} : il faut exactement un de {RESULTAT_R1} et {ARRET} (présents : {sorted(diag)})")
    r1_p = r1_s = motif_r1 = None
    lus = {}
    fichiers_r1 = att["fichiers_rejeu"]
    if a_resultat:
        exiger_noms(racine, f"diag/{rejeu}", {RESULTAT_R1})
        exiger_noms(racine, f"donnees/{rejeu}", set(fichiers_r1.values()))
        res = fichier_verifie(racine, f"diag/{rejeu}/{RESULTAT_R1}", inventaire)
        r1_p = {k: fichier_verifie(racine, f"donnees/{rejeu}/{n}", inventaire) for k, n in fichiers_r1.items()}
        r1_p["resultat"] = res
        r1_s = {"moyenne": r1_p["moyenne"], "maximum": r1_p["maximum"], "manifeste": res, "pointeurs": POINTEURS_R1}
        doc = lire_json(racine / res["chemin"], ouverts)
        for ch in POINTEURS_R1.values():          # existence seulement : aucune valeur gardée
            resoudre(doc, ch)
        lus = filtrer(doc, CHEMINS_LUS)
        del doc
        if lus["resultat.verdict_fidelite"] != att["resultat"]["verdict_fidelite"]:
            raise Arret("forme", f"{RESULTAT_R1} livré avec verdict_fidelite = {lus['resultat.verdict_fidelite']!r} : "
                                 "hors du format annoncé, nœud")
        controler_resultat(ctl, lus, manifeste_rejeu["sha256"], rejeu, att)
        declares = lus["resultat.fichiers"] if isinstance(lus["resultat.fichiers"], dict) else {}
        for k, n in fichiers_r1.items():
            if declares.get(n) != r1_p[k]["sha256"]:
                raise Arret("fichiers", f"{RESULTAT_R1} : empreinte de {n} déclarée par le fournisseur ≠ fichier versé")
    else:
        exiger_noms(racine, f"diag/{rejeu}", {ARRET})
        if (racine / "donnees" / rejeu).exists():
            raise Arret("fichiers", f"donnees/{rejeu} existe alors que le rejeu s'est arrêté : hors du format annoncé")
        arret = fichier_verifie(racine, f"diag/{rejeu}/{ARRET}", inventaire)
        lus = filtrer(lire_json(racine / arret["chemin"], ouverts), CHEMINS_LUS_ARRET)
        ctl.exiger("rattachement", lambda: lus["run_id"] == rejeu and lus["manifeste_sha256"] == manifeste_rejeu["sha256"],
                   f"{ARRET} : run_id ou manifeste ≠ run et manifeste versés")
        v = lus["resultat.verdict_fidelite"]
        if v not in MOTIFS_R1_NUL:
            raise Arret("forme", f"{ARRET} : verdict_fidelite {v!r} hors de {sorted(MOTIFS_R1_NUL)} : nœud")
        motif_r1 = MOTIFS_R1_NUL[v]
        notes.append({"arret": arret, "verdict_fidelite": v})
    r2_p = r2_s = motif_r2 = None
    if a.juge3b == "absent":
        if a.motif_R2 not in MOTIFS_R2_NUL:
            raise Arret("forme", f"juge 3B absent : --motif-R2 parmi {MOTIFS_R2_NUL} exigé, preuve dans --preuve-R2")
        if not a.preuve_R2:
            raise Arret("forme", "juge 3B absent : --preuve-R2 (constat ou chemin et empreinte) exigé")
        motif_r2 = a.motif_R2
        notes.append({"motif_R2": motif_r2, "preuve": a.preuve_R2})
    else:
        juges = {}
        for cle, run in (("juge3b", a.juge3b), ("juge8b", a.juge8b)):
            if run == "absent":
                juges[cle] = None
                continue
            run = exiger_run(run, cle)
            j = att["juges"][cle]
            ctl.exiger("juges", lambda: run == j["run"], f"run du {cle} {run!r} ≠ run cité par l'addendum v3 {j['run']!r}")
            exiger_noms(racine, f"runs/{run}", {"manifeste.json"})
            fichier_verifie(racine, f"runs/{run}/manifeste.json", inventaire)
            exiger_noms(racine, f"diag/{run}", {RESULTAT_JUGE})
            exiger_noms(racine, f"donnees/{run}", {j["fichier"]})
            juges[cle] = {"fichier": fichier_verifie(racine, f"donnees/{run}/{j['fichier']}", inventaire),
                          "resultat": fichier_verifie(racine, f"diag/{run}/{RESULTAT_JUGE}", inventaire)}
            sha_vue = juges[cle]["fichier"]["sha256"]
            ctl.exiger("juges", lambda: sha_vue == j["sha256"],
                       f"scores du {cle} {sha_vue[:12]}… ≠ empreinte citée par l'addendum v3 (section R2) {j['sha256'][:12]}…")
            doc = lire_json(racine / juges[cle]["resultat"]["chemin"], ouverts)
            if doc.get("run_id") != run:
                raise Arret("forme", f"{RESULTAT_JUGE} de {run} : run_id ≠")
            if resoudre(doc, ["resultat", "fichier"]) != j["fichier"] or resoudre(doc, ["resultat", "sha256"]) != sha_vue:
                raise Arret("fichiers", f"{RESULTAT_JUGE} de {run} : fichier ou empreinte déclarés ≠ fichier versé")
            if cle == "juge3b":
                for ch in POINTEURS_R2.values():
                    resoudre(doc, ch)
                print("contexte déclaré du juge 3B (à juger par la session, règle d'équité ; non écrit dans la fiche) :",
                      json.dumps(resoudre(doc, POINTEURS_R2["contexte_juge"]), ensure_ascii=False))
        r2_p = {"juge3b": juges["juge3b"], "juge8b": juges["juge8b"],
                "motif_juge8b": None if juges["juge8b"] is not None else "non_livre"}
        r2_s = {"fichier": juges["juge3b"]["fichier"], "manifeste": juges["juge3b"]["resultat"], "pointeurs": POINTEURS_R2}
    redaction = {
        "qui": a.qui, "quand_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "script": {"nom": NOM_SCRIPT, "sha256": empreinte(Path(__file__))},
        "fiche_reception": {"chemin": a.fiche_reception, "sha256": sha_fiche},
        "commit_versement_calcul_r1_r2_reel_v1": a.commit_versement,
        "addendum_v3": {"chemin": att["manifeste"]["preenregistrement"]["chemin"],
                        "sha256": att["manifeste"]["preenregistrement"]["sha256"],
                        "commit_scellement": att["manifeste"]["commit"],
                        "lu_dans": "clé `preenregistrement` du manifeste (manifeste.py l. 104)"},
        "provenance_table": {"cle": "tokenisation.addendum", "valeur": att["resultat"]["tokenisation.addendum"],
                             "sens": "addendum qui a construit la table v3 (E16), non le texte qui gouverne la course"},
        "runs": {"rejeu": rejeu, "juge3b": a.juge3b, "juge8b": a.juge8b},
        "e21": e21,
        "episodes_non_inversibles_declares": list(att["episodes_non_inversibles_declares"]), "N_A": att["N_A"],
        "controles": list(ctl.passees),
        "cles_lues": sorted(lus),
        "valeurs_des_cles_lues": "non recopiées : égales aux attendus de la fiche de réception (gardes de `controles`) ; "
                                 "la fiche ne contient que chemins, empreintes, pointeurs et motifs (analyse secondaire, l. 24)",
        "non_lus_avant_analyses": "liste de la fiche de réception, section 6 et bloc d'attendus (`interdits`)",
        "ce_qui_a_ete_ouvert": ouverts, "aucun_npz_ouvert": True, "compagnons_verifies": inventaire, "notes": notes,
    }
    principale = {"format": FORMAT_PRINCIPALE, "redaction": redaction, "R1": r1_p, "motif_R1": motif_r1,
                  "R2": r2_p, "motif_R2": motif_r2}
    secondaire = {"format": FORMAT_SECONDAIRE, "redaction": dict(redaction, manifeste_rejeu=manifeste_rejeu),
                  "R1": r1_s, "motif_R1": motif_r1, "R2": r2_s, "motif_R2": motif_r2, "R4": None}
    exiger_sans_fuite(ctl, principale, secondaire)
    redaction["controles"] = list(ctl.passees)
    secondaire["redaction"]["controles"] = list(ctl.passees)
    return principale, secondaire


def ecrire(p: Path, contenu: str) -> str:
    if p.exists():
        raise Arret("R12", f"{p} existe déjà : R12 interdit d'écraser (version nouvelle = nom nouveau)")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contenu, encoding="utf-8")
    return empreinte(p)


def en_json(contenu: dict) -> str:
    return json.dumps(contenu, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


# ================================================================== ligne de commande
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sous = ap.add_subparsers(dest="mode", required=True)
    av = sous.add_parser("avant-recuperation", help="écrire la fiche de réception (avant toute récupération)")
    av.add_argument("--depot", required=True, help="dépôt git où lire les textes scellés (lecture seule)")
    av.add_argument("--commit-scellement", default=COMMIT_SCELLEMENT)
    av.add_argument("--commit-principale", default=COMMIT_PRINCIPALE)
    av.add_argument("--commit-secondaire", default=COMMIT_SECONDAIRE)
    av.add_argument("--ref-tete", default=REF_TETE, help="référence où lire le texte par épisode et nos pièces citées")
    av.add_argument("--sortie", default=SORTIE_FICHE, help="chemin de la fiche, relatif au dépôt (jamais écrasée)")
    av.add_argument("--qui", required=True)
    ap_ = sous.add_parser("apres-versement", help="écrire les deux fiches JSON des analyses (après le versement)")
    ap_.add_argument("--racine", required=True, help="racine de l'arbre où les sorties sont versées")
    ap_.add_argument("--fiche-reception", required=True, help="fiche de réception scellée (chemin)")
    ap_.add_argument("--fiche-reception-sha256", required=True, help="empreinte envoyée au canal (64 hex)")
    ap_.add_argument("--rejeu", required=True, help="nom du run R1 relancé, donné par le fournisseur (jamais deviné)")
    ap_.add_argument("--juge3b", required=True, help="nom du run du juge 3B, ou `absent`")
    ap_.add_argument("--juge8b", required=True, help="nom du run du juge 8B, ou `absent`")
    ap_.add_argument("--motif-R2", default=None, choices=MOTIFS_R2_NUL)
    ap_.add_argument("--preuve-R2", default=None)
    ap_.add_argument("--qui", required=True)
    ap_.add_argument("--commit-versement", required=True, help="40 caractères du commit de FETCH_HEAD")
    ap_.add_argument("--branche-source", default=BRANCHES_SOURCE["course"], help="branche de la course versée")
    ap_.add_argument("--course-arretee-e21", default=None, help="reprise E21 : nom de la course arrêtée")
    ap_.add_argument("--arret-e21-sha256", default=None, help="reprise E21 : empreinte de son arret.json, ou `absent`")
    ap_.add_argument("--annonce-e21", default=None, help="reprise E21 : message d'annonce (numéro, empreinte)")
    ap_.add_argument("--sortie-principale", default="prereg/fiche-reception-principale-r1-r2-v1.json")
    ap_.add_argument("--sortie-secondaire", default="prereg/fiche-reception-blanche-noire-v3.json")
    ap_.add_argument("--sans-secondaire", action="store_true", help="n'écrire que la fiche principale")
    a = ap.parse_args(argv)
    try:
        if a.mode == "avant-recuperation":
            att, constat, ctl = construire_avant(a)
            quand = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d à %H:%M:%S UTC")
            texte = rendre_fiche(att, constat, ctl, a.qui, quand, empreinte(Path(__file__)))
            p = Path(a.depot).resolve() / a.sortie
            h = ecrire(p, texte)
            print(f"gardes passées : {', '.join(ctl.passees)}")
            print(f"fiche de réception : {a.sortie} {h}")
            print("à sceller avant toute récupération des sorties de la course (C-1), puis chemin et empreinte au canal")
            return 0
        if not _HEX40.fullmatch(a.commit_versement) or not _HEX64.fullmatch(a.fiche_reception_sha256):
            raise Arret("forme", "commit de versement (40 hex) ou empreinte de la fiche de réception (64 hex) hors de forme")
        racine = Path(a.racine).resolve()
        principale, secondaire = construire_apres(racine, a)
        cibles = [(racine / a.sortie_principale, principale)] + \
                 ([] if a.sans_secondaire else [(racine / a.sortie_secondaire, secondaire)])
        for p, _ in cibles:
            if p.exists():
                raise Arret("R12", f"{p} existe déjà : R12 interdit d'écraser (version nouvelle = nom nouveau)")
        for (p, contenu), nom in zip(cibles, ("principale", "secondaire")):
            print(f"fiche {nom} : {p.relative_to(racine)} {ecrire(p, en_json(contenu))}")
        red = principale["redaction"]
        print(f"gardes passées : {', '.join(red['controles'])}")
        print(f"fichiers vérifiés contre leur compagnon : {len(red['compagnons_verifies'])}")
        print(f"ouverts : {red['ce_qui_a_ete_ouvert']}")
        return 0
    except Arret as e:
        print(f"ARRÊT {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
