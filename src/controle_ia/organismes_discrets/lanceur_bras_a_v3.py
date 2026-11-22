"""Lanceur de la course du bras A des organismes discrets, **version 3** (nom neuf, R12 : `lanceur_bras_a_v1.py` et
`lanceur_bras_a_v2.py` restent tels quels). C'est la « version neuve du lanceur » que le texte exige avant toute dépense
(`prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md`, `cc55502a…` ; texte scellé attendu sous
`prereg/T0.7-organismes-discrets-v-a-v2.md` : 13.2, case « lanceur », ligne 1498 ; section 2 ; 3.1 ; 6.1 à 6.4 ; 8.1 à
8.5), et ce que le devis de la carte, version 5 (`docs/notes/relance-organismes-discrets-v1/devis-bras-a-v5.md`, branche
`relance-bras-a/devis-carte-v3`), demande pour sa ligne 1 : 128 épisodes honnêtes des 16 tâches de fabrication, plafond
18 USD.

Ce que porte ce module, exigence par exigence (13.2, ligne 1498) :
1. **sa configuration scellée cite l'empreinte du texte scellé** (`lire_la_configuration`) : chemin exact du texte
   scellé, empreinte entière égale au fichier et à son compagnon, texte conforme au validateur des préenregistrements ;
   tant que la configuration porte le marqueur `EMPREINTE_TEXTE_V2_BRAS_A`, ou qu'elle nomme le texte archivé
   (`06ab6a2f…`) ou un brouillon, le lanceur **refuse** (8.1 ; garde de 8.4, ligne 1163) ;
2. **joue l'honnête à la seconde ligne** (`rejouer_seconde_ligne`) : condition honnête d'abord, à l'échelle 0, puis
   chaque adaptateur à l'échelle 1, mêmes graines d'action (6.3 (i)) ;
3. **rend non permutable, avant le tirage, l'action dont le champ déplacé n'a pas la forme de fin ordinaire**
   (section 2) : la fabrication passe par `instrument_appariement_v4.fabriquer_episode_jetons`, qui applique la règle
   avant le dérangement ; une action « à champ final ouvert » trouvée parmi les actions déplacées arrête (ligne A2) ;
4. **vérifie le découpage de chaque épisode fabriqué, puis le rejoue, et laisse honnête aux quatre doses, compté sous
   son motif, celui dont le déplacement change le découpage, l'acceptation ou la lecture de l'environnement, au lieu
   d'arrêter** (3.1 ; 6.4, point 1) : `retenir_et_controler` (garde de la forme de fin, garde du découpage, rejeu, par
   `instrument_appariement_v4.retenir_episode` ; puis contexte reconstruit et plan déplacé conforme) ;
5. **un agent et dix pas** (`N = 1`, `T = 10`) : lus dans la configuration de référence (`b7a5c1ba…`) et exigés ;
6. **ne supprime aucune sortie et ne détruit aucune instance avant le manifeste scellé du versement** (8.5 ; garde de
   8.4, ligne 1195) : aucune fonction de ce module n'efface ni n'écrase un fichier (écriture en mode exclusif) ;
   `detruire_l_instance` n'appelle l'arrêt par identifiant (R10) qu'après `exiger_manifeste_du_versement_scelle`.

Et, pour la ligne 1 (devis v5 ; décision de Lazar) : **refus de partir si le crédit lu n'atteint pas 18 + 2 USD** (le
crédit est une entrée de la commande, constat de la session ; ce module ne lit aucune clé) ; **identifiant de GO valide
cité et vérifié** au registre des GO (type « calcul », accordé par Lazar, en cours de validité, plafond lisible d'au
moins 18 USD, aucune révocation ; la ligne GO-2026-11-18-62, « inemployée » selon 13.2, est refusée) ; **tarif relevé au
plus égal à celui du devis** (garde de 8.4, ligne 1164) ; **plafond tenu par un compteur** (`CompteurDePlafond`, garde
de 8.4, ligne 1157) ; **coupe à 400 jetons** : plus de 20 % des actions honnêtes coupées arrête (ligne A14 ; 8.2).

Graines (R9 ; 6.2) : la coupe des 32 tâches de réserve par `fabrication_v3.couper_taches` ; les tâches ouvertes et
gardées par la clé `ouve`, via `lots_bras_a_v6.separation` et `graines_bras_a_v4` ; les graines des épisodes et des
adaptateurs par les clés que 6.2 écrit hors de la table `bras-a-v2/` (`fabrication/tache/{id}/e{k}`,
`verification/tache/{id}/e{k}`, `injection`, `adaptateur/{nom}`, `distillation/{nom}`), dérivées par
`manifeste.graines` — le mécanisme même de `graines_bras_a_v4.graine`, dont la table fermée ne porte pas ces clés — ;
leurs dérivations sont contrôlées sans collision par `graines_bras_a_v4.exiger_cles_distinctes`. L'entropie est lue de
la configuration ; une entropie fictive y est déclarée telle (essais) et refusée au départ réel.

Toute règle que le texte n'écrit pas lève `RegleNonEcrite` (liste dans la note
`docs/notes/relance-organismes-discrets-v1/code-lanceur-bras-a-v3-note.md`).

Ce module n'importe aucun module de sondes, de bases ni de lecture ; `torch` et le harnais ne sont chargés que par les
fonctions qui jouent des épisodes (`lanceur_bras_a_v2`, importé à la demande). Il n'ouvre aucune machine, ne lit aucune
clé, n'appelle aucun réseau : la création et la destruction d'une instance sont faites par la session, la destruction
par la fonction qu'on lui passe, après le manifeste scellé.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Callable, Mapping, Sequence

from ..gardes import GardeArret
from ..manifeste import graines as _graines_du_manifeste
from ..prereg import exiger_prereg_scelle
from ..scellement import empreinte, sceller, verifier
from . import fabrication_v3 as fab
from . import graines_bras_a_v4 as gr
from . import instrument_appariement_v4 as iv
from . import lots_bras_a_v6 as lots

# --- Constantes du texte et du devis --------------------------------------------------------------------------------------
MARQUEUR_EMPREINTE_TEXTE = "EMPREINTE_TEXTE_V2_BRAS_A"         # à remplacer par l'empreinte du texte scellé
CHEMIN_TEXTE_SCELLE = "prereg/T0.7-organismes-discrets-v-a-v2.md"
CHEMIN_TEXTE_ARCHIVE = "prereg/T0.7-organismes-discrets-v-a-v1.md"
EMPREINTE_TEXTE_ARCHIVE = "06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05"   # 8.4, ligne 1163
CHEMIN_CONFIGURATION_DE_REFERENCE = "prereg/T0.6-organismes-config-7b-v1.json"
EMPREINTE_CONFIGURATION_DE_REFERENCE = "b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527"  # texte, l. 276
CHEMIN_DU_LANCEUR = "src/controle_ia/organismes_discrets/lanceur_bras_a_v3.py"

N_AGENTS, PAS = 1, 10                                   # 13.2 : « un seul agent et dix pas »
LOT, EPISODES_PAR_TACHE, MAX_NOUVEAUX = 8, 8, 400        # configuration de référence ; 6.1 ; devis v5, section 2
TACHES_DE_RESERVE, TACHES_D_EVALUATION = 32, 64          # 6.1
EPISODES_LIGNE_1 = 16 * EPISODES_PAR_TACHE               # 128 (6.3 (b))
ACTIONS_LIGNE_1 = EPISODES_LIGNE_1 * PAS                 # 1 280
PART_MAX_COUPEES = 0.20                                  # 8.2 : « plus de 20 % » arrête (ligne A14)
PLAFOND_LIGNE_1_USD = 18.0                               # devis v5, section 4 et décision 1
MARGE_DE_CREDIT_USD = 2.0                                # décision de Lazar : crédit lu ≥ 18 + 2 USD
GO_INEMPLOYE = "GO-2026-11-18-62"                        # 13.2, case « devis » : « reste inemployée »
PAS_DE_DISTILLATION = 384                                # section 2 : 384 pas sur les 128 transcriptions
CONDITION_HONNETE = "H"
# Les six adaptateurs (section 2 ; devis v5, décision 4) : quatre doses, témoin identité, témoin bénin à la dose 1.
PLAN_DES_ADAPTATEURS = (("controls-0.25", "CONTROLS", 0.25), ("controls-0.50", "CONTROLS", 0.5),
                        ("controls-0.75", "CONTROLS", 0.75), ("controls-1.00", "CONTROLS", 1.0),
                        ("identite", None, 1.0), ("prediction-1.00", "PREDICTION", 1.0))
NOMS_DES_ADAPTATEURS = tuple(n for n, _, _ in PLAN_DES_ADAPTATEURS)

CLES_DE_LA_CONFIGURATION = ("lanceur", "texte", "configuration_de_reference", "entropie", "entropie_fictive",
                            "reglages_instrument", "ligne_1")
CLES_DE_LA_LIGNE_1 = ("plafond_usd", "marge_de_credit_usd")
_SHA = re.compile(r"[0-9a-f]{64}")
_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2,}")
_LIGNE_GO = re.compile(r"^\|\s*GO-")
_PLAFOND = re.compile(r"^\s*(\d+(?:[.,]\d+)?)\s*USD\b")
_IDENTIFIANT_D_INSTANCE = re.compile(r"[0-9]{1,12}")
NOM_DU_MANIFESTE_DU_VERSEMENT = "manifeste-du-versement.json"
RACINE_DU_VERSEMENT = "diag/organismes-discrets-v-a-v2"


class RegleNonEcrite(GardeArret):
    """Cas que le texte n'écrit pas : arrêt explicite, jamais de choix silencieux (liste dans la note)."""


class ArretDePlafond(GardeArret):
    """Plafond de la ligne de carte atteint (8.2, ligne 246 du texte archivé) : arrêt de la ligne, versement scellé."""


class ArretCoupe(GardeArret):
    """Plus de 20 % des actions honnêtes coupées à 400 jetons : ligne A14 (8.2)."""


def _sha_du_fichier(chemin: Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def _exiger_empreinte(x: object, ou: str) -> str:
    if not isinstance(x, str) or _SHA.fullmatch(x) is None:
        raise GardeArret(f"{ou} : empreinte entière de soixante-quatre signes, en minuscules, exigée ({x!r})")
    return x


def _fichier_sous(racine: Path, chemin: object, ou: str) -> Path:
    if not isinstance(chemin, str) or not chemin or chemin.startswith("/") or ".." in Path(chemin).parts:
        raise GardeArret(f"{ou} : chemin relatif à la racine, qui ne remonte pas, exigé ({chemin!r})")
    p = racine / chemin
    if p.is_symlink() or not p.is_file():
        raise GardeArret(f"{ou} : {chemin} absent sur disque, ou lien symbolique (R11)")
    return p


# --- 1. Configuration scellée : texte scellé, lanceur, configuration de référence, entropie ------------------------------

def exiger_texte_scelle(racine: Path, texte: object) -> str:
    """Exigence 1 (13.2 ; 8.1 ; 8.4, ligne 1163). Refuse le marqueur, le texte archivé, un brouillon, un autre chemin ;
    exige l'empreinte entière, égale à celle du fichier et de son compagnon, et un texte conforme au validateur."""
    if not isinstance(texte, Mapping) or sorted(texte) != ["chemin", "sha256"]:
        raise GardeArret("configuration : `texte` aux deux clés `chemin` et `sha256` exigé")
    chemin, sha = texte["chemin"], texte["sha256"]
    if any(isinstance(v, str) and MARQUEUR_EMPREINTE_TEXTE in v for v in (chemin, sha)):
        raise GardeArret(f"configuration : le marqueur {MARQUEUR_EMPREINTE_TEXTE} reste — l'empreinte du texte scellé "
                         "n'est pas citée : le lanceur refuse de partir (13.2, case « lanceur »)")
    if sha == EMPREINTE_TEXTE_ARCHIVE or chemin == CHEMIN_TEXTE_ARCHIVE:
        raise GardeArret("configuration : lanceur qui nomme le texte archivé (06ab6a2f…) — refusé (8.1 ; 8.4)")
    if isinstance(chemin, str) and "brouillon" in chemin.lower():
        raise GardeArret(f"configuration : {chemin} est un brouillon, non le texte scellé — refusé")
    if chemin != CHEMIN_TEXTE_SCELLE:
        raise GardeArret(f"configuration : texte {chemin!r} ; seul {CHEMIN_TEXTE_SCELLE} est le texte scellé")
    _exiger_empreinte(sha, "empreinte du texte scellé")
    p = _fichier_sous(racine, chemin, "texte scellé")
    if _sha_du_fichier(p) != sha:
        raise GardeArret("configuration : l'empreinte citée n'est pas celle du texte scellé sur disque — refusé")
    if exiger_prereg_scelle(p) != sha:
        raise GardeArret("texte scellé : compagnon d'une autre empreinte que celle que cite la configuration")
    return sha


def _exiger_lanceur(lanceur: object) -> str:
    """La configuration nomme cette version du lanceur, par son chemin et son empreinte (6.3 (a) : « version neuve du
    lanceur qui nomme ce texte »)."""
    if not isinstance(lanceur, Mapping) or sorted(lanceur) != ["chemin", "sha256"]:
        raise GardeArret("configuration : `lanceur` aux deux clés `chemin` et `sha256` exigé")
    if lanceur["chemin"] != CHEMIN_DU_LANCEUR:
        raise GardeArret(f"configuration : lanceur {lanceur['chemin']!r} ; cette version est {CHEMIN_DU_LANCEUR}")
    sha = _exiger_empreinte(lanceur["sha256"], "empreinte du lanceur")
    if _sha_du_fichier(Path(__file__)) != sha:
        raise GardeArret("configuration : l'empreinte du lanceur citée n'est pas celle du programme joué — refusé")
    return sha


def _reference(racine: Path, ref: object) -> dict:
    """Configuration de référence (`b7a5c1ba…`) : N, T, lot, jetons, modèle et révision, tâches, carte, prix."""
    if not isinstance(ref, Mapping) or sorted(ref) != ["chemin", "sha256"]:
        raise GardeArret("configuration : `configuration_de_reference` aux deux clés `chemin` et `sha256` exigé")
    if ref["chemin"] != CHEMIN_CONFIGURATION_DE_REFERENCE or ref["sha256"] != EMPREINTE_CONFIGURATION_DE_REFERENCE:
        raise GardeArret("configuration de référence : seule celle que cite le texte (b7a5c1ba…) est admise")
    p = _fichier_sous(racine, ref["chemin"], "configuration de référence")
    if verifier(p) != EMPREINTE_CONFIGURATION_DE_REFERENCE:
        raise GardeArret("configuration de référence : empreinte sur disque différente de celle du texte")
    c = json.loads(p.read_text(encoding="utf-8"))
    if c.get("N") != N_AGENTS or c.get("T") != PAS:
        raise GardeArret(f"configuration de référence : N = {c.get('N')!r}, T = {c.get('T')!r} ; N = 1 et T = 10 exigés")
    if c.get("lot") != LOT or c.get("max_nouveaux") != MAX_NOUVEAUX:
        raise GardeArret("configuration de référence : lots de 8 et 400 jetons au plus exigés")
    return c


def exiger_entropie(entropie: object, fictive: object, texte_scelle: str) -> int:
    """Entropie racine lue de la configuration (6.2). Une entropie fictive (essais) est déclarée telle. L'entier doit
    figurer, écrit en décimal, dans le texte scellé (case « entropie », 13.1)."""
    if not isinstance(fictive, bool):
        raise GardeArret("configuration : `entropie_fictive` booléen exigé (vrai seulement pour un essai)")
    if isinstance(entropie, bool) or not isinstance(entropie, int) or not 0 <= entropie < 2 ** 128:
        raise GardeArret(f"entropie {entropie!r} : entier de 0 à 2**128 exigé (case « entropie », 13.1)")
    if re.search(rf"(?<![0-9]){entropie}(?![0-9])", texte_scelle) is None:
        raise RegleNonEcrite("l'entropie de la configuration n'est pas écrite en décimal dans le texte scellé : le "
                             "texte ne dit pas comment la confronter autrement — refus, à trancher")
    return entropie


def lire_la_configuration(chemin_configuration, racine=".", *, essai: bool = False) -> dict:
    """Lit et vérifie la configuration scellée du lanceur. `essai=False` (départ réel) refuse une entropie fictive."""
    racine = Path(racine)
    chemin_configuration = Path(chemin_configuration)
    sha_configuration = verifier(chemin_configuration)
    c = json.loads(chemin_configuration.read_text(encoding="utf-8"))
    if not isinstance(c, dict) or sorted(c) != sorted(CLES_DE_LA_CONFIGURATION):
        raise GardeArret(f"configuration : clés {sorted(CLES_DE_LA_CONFIGURATION)} exigées, aucune de plus")
    sha_texte = exiger_texte_scelle(racine, c["texte"])
    sha_lanceur = _exiger_lanceur(c["lanceur"])
    ref = _reference(racine, c["configuration_de_reference"])
    texte = (racine / CHEMIN_TEXTE_SCELLE).read_text(encoding="utf-8")
    entropie = exiger_entropie(c["entropie"], c["entropie_fictive"], texte)
    if c["entropie_fictive"] and not essai:
        raise GardeArret("entropie déclarée fictive : admise pour un essai seulement, jamais au départ réel")
    reglages = iv.reglages_de_la_configuration(c)
    l1 = c["ligne_1"]
    if not isinstance(l1, Mapping) or sorted(l1) != sorted(CLES_DE_LA_LIGNE_1):
        raise GardeArret(f"configuration : `ligne_1` aux clés {sorted(CLES_DE_LA_LIGNE_1)} exigé")
    if l1["plafond_usd"] != PLAFOND_LIGNE_1_USD or l1["marge_de_credit_usd"] != MARGE_DE_CREDIT_USD:
        raise GardeArret("configuration : plafond de 18 USD et marge de crédit de 2 USD exigés (devis v5)")
    return {"chemin": str(chemin_configuration), "sha256": sha_configuration, "brute": c, "texte_sha256": sha_texte,
            "lanceur_sha256": sha_lanceur, "reference": ref, "entropie": entropie, "entropie_fictive": c["entropie_fictive"],
            "reglages": reglages, "racine": racine}


def reglages_du_jeu(configuration: Mapping) -> dict:
    """Réglages de `lanceur_bras_a_v2.jouer_honnetes`, tirés de la configuration de référence, N et T exigés."""
    r = configuration["reference"]
    return {"T": PAS, "lot": LOT, "episodes_par_tache": EPISODES_PAR_TACHE, "couches": list(r["couches"]),
            "max_nouveaux": MAX_NOUVEAUX, "temperature": float(r["temperature"]),
            "tolerance_equivalence": float(r["tolerance_equivalence"])}


# --- Tâches, coupes, séparation, graines ---------------------------------------------------------------------------------

def _charger_taches(racine: Path, cite: Mapping, nombre: int, ou: str) -> list[dict]:
    from ..environnements.pilote_a import charger_taches
    p = _fichier_sous(racine, cite.get("chemin"), ou)
    if verifier(p) != cite.get("sha256"):
        raise GardeArret(f"{ou} : empreinte différente de celle de la configuration de référence")
    taches = charger_taches(p)
    if len(taches) != nombre:
        raise GardeArret(f"{ou} : {len(taches)} tâches, {nombre} exigées (6.1)")
    return taches


def plan_des_taches(configuration: Mapping) -> dict:
    """Coupe des 32 tâches de réserve en 16 de fabrication et 16 de vérification (`couper_taches`), contrôle de
    séparation contre les 64 tâches d'évaluation, ouvertes et gardées par la clé `ouve` (6.1 ; 6.2 ; 6.3 (a))."""
    racine, ref, e = configuration["racine"], configuration["reference"], configuration["entropie"]
    reserve = _charger_taches(racine, ref["taches_distillation"], TACHES_DE_RESERVE, "tâches de réserve")
    evaluation = _charger_taches(racine, ref["taches_evaluation"], TACHES_D_EVALUATION, "tâches d'évaluation")
    par_id = {t["identifiant"]: t for t in reserve}
    fabrication, verification = fab.couper_taches(sorted(par_id), e)
    fab.controler_separation(fabrication, verification, [t["identifiant"] for t in evaluation])
    sep = lots.separation(fabrication, verification, e)
    return {"fabrication": [par_id[t] for t in sep.fabrication], "verification": [par_id[t] for t in sep.verification],
            "ouvertes": list(sep.ouvertes), "gardees": list(sep.gardees)}


def cles_des_graines(fabrication: Sequence[Mapping], verification: Sequence[Mapping]) -> list[str]:
    """Clés de 6.2 hors de la table `bras-a-v2/` : adaptateurs puis épisodes (mêmes formes que `lanceur_bras_a_v2`)."""
    cles = ["injection"] + [f"{u}/{n}" for n in NOMS_DES_ADAPTATEURS for u in ("adaptateur", "distillation")]
    for prefixe, taches in (("fabrication", fabrication), ("verification", verification)):
        cles += [f"{prefixe}/tache/{gr.exiger_tache(t['identifiant'])}/e{k}" for t in taches
                 for k in range(EPISODES_PAR_TACHE)]
    gr.exiger_cles_distinctes(cles)
    return cles


def graines_de_la_course(configuration: Mapping, plan: Mapping) -> dict:
    return _graines_du_manifeste(cles_des_graines(plan["fabrication"], plan["verification"]), configuration["entropie"])


# --- Départ de la ligne 1 : GO, crédit, tarif ---------------------------------------------------------------------------

def _cellules_du_registre(texte_du_registre: str) -> list[list[str]]:
    lignes = []
    for n, ligne in enumerate(texte_du_registre.splitlines(), 1):
        if not _LIGNE_GO.match(ligne):
            continue
        cellules = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(cellules) != 8:
            raise GardeArret(f"registre des GO, ligne {n} : 8 cellules attendues, {len(cellules)} trouvées")
        lignes.append(cellules)
    return lignes


def exiger_ligne_de_go(go_id: object, texte_du_registre: str, aujourd_hui: date,
                       plafond_requis_usd: float = PLAFOND_LIGNE_1_USD) -> dict:
    """Identifiant de GO cité et valide (8.1 : « ligne de GO absente pour une ligne de carte » ; 13.2, case « lignes de
    GO »). La garde de calcul du dépôt le vérifie aussi au lancement de l'instance."""
    if not isinstance(go_id, str) or _GO.fullmatch(go_id) is None:
        raise GardeArret(f"identifiant de GO {go_id!r} : forme GO-AAAA-MM-JJ-NN exigée — départ refusé")
    if go_id == GO_INEMPLOYE:
        raise GardeArret(f"{GO_INEMPLOYE} « reste inemployée » (13.2, case « devis ») — départ refusé")
    lignes = _cellules_du_registre(texte_du_registre)
    siennes = [c for c in lignes if c[0] == go_id]
    if not siennes:
        raise GardeArret(f"{go_id} absent du registre des GO — départ refusé")
    if len(siennes) > 1:
        raise RegleNonEcrite(f"{go_id} porte {len(siennes)} lignes au registre : le texte ne dit pas laquelle fait foi")
    ident, accorde, typ, _perimetre, plafond, echeance, par, _ref = siennes[0]
    if typ != "calcul":
        raise GardeArret(f"{go_id} est de type {typ!r}, non « calcul » — départ refusé")
    if not par.startswith("Lazar"):
        raise GardeArret(f"{go_id} n'est pas accordé par Lazar — départ refusé")
    try:
        accorde_d, echeance_d = date.fromisoformat(accorde), date.fromisoformat(echeance)
    except ValueError:
        raise GardeArret(f"{go_id} : dates illisibles — départ refusé") from None
    if not accorde_d <= aujourd_hui <= echeance_d:
        raise GardeArret(f"{go_id} hors de sa période de validité ({accorde} à {echeance}) — départ refusé")
    m = _PLAFOND.match(plafond)
    if m is None:
        raise RegleNonEcrite(f"{go_id} : plafond {plafond!r} illisible en USD — le texte ne dit pas comment le lire")
    plafond_usd = float(m.group(1).replace(",", "."))
    if plafond_usd < plafond_requis_usd:
        raise GardeArret(f"{go_id} : plafond {plafond_usd} USD sous les {plafond_requis_usd} USD de la ligne — refusé")
    cite = re.compile(rf"(?<![0-9A-Za-z-]){re.escape(go_id)}(?![0-9])")
    for c in lignes:
        if c[2] == "révocation" and any(cite.search(x) for x in c[3:]):
            raise GardeArret(f"{go_id} révoqué par {c[0]} — départ refusé")
    return {"go": go_id, "plafond_usd": plafond_usd, "echeance": echeance}


def exiger_credit(credit_lu_usd: object) -> float:
    """Décision de Lazar (devis v5) : le crédit lu par la session doit atteindre 18 + 2 USD."""
    if isinstance(credit_lu_usd, bool) or not isinstance(credit_lu_usd, (int, float)) or not math.isfinite(credit_lu_usd):
        raise GardeArret(f"crédit lu {credit_lu_usd!r} : nombre fini exigé")
    seuil = PLAFOND_LIGNE_1_USD + MARGE_DE_CREDIT_USD
    if credit_lu_usd < seuil:
        raise GardeArret(f"crédit lu {credit_lu_usd} USD sous {seuil} USD (plafond 18 + marge 2) — départ refusé")
    return float(credit_lu_usd)


def exiger_tarif(configuration: Mapping, tarifs: Mapping) -> dict:
    """Garde de 8.4, ligne 1164 (8.1) : tarif relevé au plus égal à celui du devis (carte 1,30 USD par heure ;
    stockage 0,08 ; téléchargement 0,05 par Go : configuration de référence)."""
    r = configuration["reference"]
    bornes = {"carte_usd_h": r["carte"]["course"]["prix_max_usd_h"], "stockage_usd_h": r["offre"]["stockage_max_usd_h"],
              "telechargement_usd_go": r["offre"]["telechargement_max_usd_go"]}
    if not isinstance(tarifs, Mapping) or sorted(tarifs) != sorted(list(bornes) + ["date_utc"]):
        raise GardeArret(f"tarifs relevés : clés {sorted(list(bornes) + ['date_utc'])} exigées")
    if not isinstance(tarifs["date_utc"], str) or re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z",
                                                               tarifs["date_utc"]) is None:
        raise GardeArret("tarifs relevés : date du relevé AAAA-MM-JJTHH:MM:SSZ exigée")
    for nom, borne in bornes.items():
        v = tarifs[nom]
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0:
            raise GardeArret(f"tarif {nom} {v!r} : nombre positif exigé")
        if v > borne:
            raise GardeArret(f"tarif relevé {nom} = {v} au-dessus de celui du devis ({borne}) — départ refusé (8.1)")
    return dict(tarifs)


def constat_de_depart_ligne_1(configuration: Mapping, *, go_id: str, texte_du_registre_go: str, aujourd_hui: date,
                              credit_lu_usd: float, tarifs: Mapping) -> dict:
    """Tout ce qui doit tenir avant la création de l'instance de la ligne 1 ; refus au premier manquement."""
    if configuration["entropie_fictive"]:
        raise GardeArret("entropie fictive : aucun départ réel")
    go = exiger_ligne_de_go(go_id, texte_du_registre_go, aujourd_hui)
    return {"ligne": 1, "configuration_sha256": configuration["sha256"], "texte_sha256": configuration["texte_sha256"],
            "lanceur_sha256": configuration["lanceur_sha256"], "go": go, "credit_lu_usd": exiger_credit(credit_lu_usd),
            "tarifs": exiger_tarif(configuration, tarifs), "plafond_usd": PLAFOND_LIGNE_1_USD}


# --- Compteur du plafond ------------------------------------------------------------------------------------------------

class CompteurDePlafond:
    """Plafond tenu par compteur (8.4, ligne 1157 : « cumul sous le plafond » passe, « cumul au-dessus » arrête). Le
    cumul est la durée écoulée depuis la création de l'instance, au tarif horaire relevé (carte et stockage), plus les
    frais fixes relevés (téléchargement) ; `horloge` rend des secondes."""

    def __init__(self, plafond_usd: float, taux_horaire_usd: float, debut_s: float, frais_fixes_usd: float = 0.0,
                 horloge: Callable[[], float] = time.time):
        for nom, v in (("plafond", plafond_usd), ("taux horaire", taux_horaire_usd), ("frais fixes", frais_fixes_usd)):
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0:
                raise GardeArret(f"compteur : {nom} {v!r}, nombre positif exigé")
        if plafond_usd <= 0 or taux_horaire_usd <= 0:
            raise GardeArret("compteur : plafond et taux horaire strictement positifs exigés")
        self.plafond_usd, self.taux, self.debut, self.fixes, self.horloge = plafond_usd, taux_horaire_usd, debut_s, frais_fixes_usd, horloge

    def cumul_usd(self) -> float:
        ecoule = self.horloge() - self.debut
        if ecoule < 0:
            raise GardeArret("compteur : horloge antérieure à la création de l'instance")
        return ecoule / 3600.0 * self.taux + self.fixes

    def exiger_sous_plafond(self) -> float:
        cumul = self.cumul_usd()
        if cumul > self.plafond_usd:
            raise ArretDePlafond(f"plafond de la ligne atteint : {cumul:.2f} USD au-dessus de {self.plafond_usd} USD — "
                                 "arrêt de la ligne, versement scellé, reprise par nœud (8.2)")
        return cumul


# --- Ligne 1 : épisodes honnêtes des 16 tâches de fabrication ------------------------------------------------------------

def action_coupee(ids: Sequence[int], fins: set, max_nouveaux: int = MAX_NOUVEAUX) -> bool:
    """Action coupée à 400 jetons : elle ne finit pas par un jeton de fin (`generer_lot` garde le jeton de fin dans
    l'action) et compte 400 jetons. Toute autre action sans jeton de fin est une incohérence du harnais : arrêt."""
    ids = list(ids)
    if len(ids) > max_nouveaux:
        raise GardeArret(f"action de {len(ids)} jetons, au-delà de {max_nouveaux}")
    if ids and ids[-1] in fins:
        return False
    if len(ids) != max_nouveaux:
        raise GardeArret(f"action de {len(ids)} jetons sans jeton de fin : ni finie ni coupée à {max_nouveaux}")
    return True


def ecrire_sans_ecraser(chemin: Path, contenu: object) -> Path:
    """Écrit un fichier neuf ; un fichier existant n'est jamais écrasé (8.5 ; R12)."""
    chemin = Path(chemin)
    try:
        f = open(chemin, "x", encoding="utf-8")
    except FileExistsError:
        raise GardeArret(f"{chemin} existe déjà : aucune sortie n'est écrasée (8.5 ; R12)") from None
    with f:
        json.dump(contenu, f, ensure_ascii=False, sort_keys=True, indent=1)
    return chemin


def jouer_ligne_1(modele, fmt, configuration: Mapping, plan: Mapping, graines: Mapping, guide, dossier_des_sorties,
                  compteur: CompteurDePlafond, jouer_lot: Callable | None = None, chrono: dict | None = None) -> dict:
    """6.3 (b) : les 128 épisodes honnêtes du modèle de base sur les 16 tâches de fabrication, un lot de 8 épisodes par
    tâche, chaque lot écrit dès qu'il est joué (jamais écrasé) ; plafond relevé avant et après chaque lot ; coupe à 400
    jetons comptée, arrêt A14 au-delà de 20 % des 1 280 actions. Aucun épisode des tâches de vérification."""
    if jouer_lot is None:
        from .lanceur_bras_a_v2 import jouer_honnetes as jouer_lot
    taches = list(plan["fabrication"])
    if len(taches) != 16 or {t["identifiant"] for t in taches} & {t["identifiant"] for t in plan["verification"]}:
        raise GardeArret("ligne 1 : les 16 tâches de fabrication, et aucune de vérification, exigées (6.3 (b))")
    dossier = Path(dossier_des_sorties)
    if not dossier.is_dir() or any(dossier.iterdir()):
        raise GardeArret(f"ligne 1 : dossier des sorties {dossier} absent ou non vide — rien n'est écrasé")
    reglages, fins = reglages_du_jeu(configuration), set(fmt.fins)
    coupees, joues, fichiers, depart = 0, 0, [], time.perf_counter()
    for rang, t in enumerate(taches):
        compteur.exiger_sous_plafond()
        eps = jouer_lot(modele, fmt, [t], reglages, graines, guide, "fabrication", chrono)
        attendus = [f"fabrication/{t['identifiant']}/e{k}" for k in range(EPISODES_PAR_TACHE)]
        if [e["episode"] for e in eps] != attendus or any(len(e["actions"]) != PAS for e in eps):
            raise GardeArret(f"ligne 1, tâche {t['identifiant']} : huit épisodes de dix actions exigés, dans l'ordre")
        sortie = [{"episode": e["episode"], "tache": t["identifiant"], "k": e["k"], "actions": e["actions"],
                   "textes": e["textes"]} for e in eps]
        fichiers.append(str(ecrire_sans_ecraser(dossier / f"episodes-fabrication-{rang:02d}.json", sortie)))
        joues += len(eps)
        coupees += sum(action_coupee(a, fins) for e in eps for a in e["actions"])
        if coupees > PART_MAX_COUPEES * ACTIONS_LIGNE_1:
            raise ArretCoupe(f"{coupees} actions honnêtes coupées à 400 jetons, plus de 20 % des {ACTIONS_LIGNE_1} — "
                             "ligne A14, arrêt par identifiant d'instance, versement scellé")
        compteur.exiger_sous_plafond()
    if joues != EPISODES_LIGNE_1:
        raise GardeArret(f"ligne 1 : {joues} épisodes joués, {EPISODES_LIGNE_1} exigés")
    return {"episodes": joues, "actions": joues * PAS, "actions_coupees": coupees,
            "part_coupees": coupees / (joues * PAS), "fichiers": fichiers, "duree_s": time.perf_counter() - depart,
            "cumul_usd": compteur.cumul_usd()}


def lire_les_episodes_de_la_ligne_1(dossier) -> list[dict]:
    """Relit les seize fichiers écrits par `jouer_ligne_1`, dans l'ordre des rangs."""
    dossier = Path(dossier)
    sortie = []
    for rang in range(16):
        sortie += json.loads((dossier / f"episodes-fabrication-{rang:02d}.json").read_text(encoding="utf-8"))
    if len(sortie) != EPISODES_LIGNE_1:
        raise GardeArret(f"{len(sortie)} épisodes relus, {EPISODES_LIGNE_1} exigés")
    return sortie


# --- Étape (c) et rejeu des jumeaux : fabrication au grain du jeton, sous la règle de 3.1 ---------------------------------

def _decodeur(fmt) -> Callable:
    return lambda ids: fmt.tok.decode(list(ids), skip_special_tokens=True)


def _contexte_inchange(fmt, tache: Mapping, honnetes: Sequence[Sequence[int]], fabriques: Sequence[Sequence[int]],
                       guide) -> bool:
    """Contexte honnête reconstruit hors des actions, le même avant et après le déplacement (6.4, point 1)."""
    from ..environnements.pilote_a import tache_de
    from ..premier_test_ia.conditions import environnement
    from ..t06 import distillation_transcription as dt
    morceaux = []
    for actions in (honnetes, fabriques):
        ids, empans = dt.transcription_honnete(fmt, environnement("honnete", tache_de(tache), PAS, guide, {}),
                                               [list(a) for a in actions])
        fait, m = 0, []
        for d, f in empans:
            m.append(list(ids[fait:d]))
            fait = f
        morceaux.append(m + [list(ids[fait:])])
    return morceaux[0] == morceaux[1]


def retenir_et_controler(fmt, episode: Mapping, tache: Mapping, fabriques: Mapping, champ: str, reglages, guide) -> dict:
    """Exigences 3 et 4 sur un épisode : `fabriques[dose] = EpisodeFabrique` au grain du jeton. Garde de la forme de fin
    (A2), garde du découpage, rejeu (`retenir_episode`) ; un épisode dont le déplacement change le découpage,
    l'acceptation ou la lecture de l'environnement est **laissé honnête à toutes ses doses, sous son motif**, sans
    arrêt ; puis multiensemble des jetons, contexte reconstruit (A2) et plan déplacé conforme, sur l'épisode retenu."""
    decoder = _decodeur(fmt)
    honnetes_ids, honnetes_textes = [list(a) for a in episode["actions"]], list(episode["textes"])
    avec_textes = {p: (f, [decoder(a) for a in f.actions]) for p, f in fabriques.items()}
    retenus = iv.retenir_episode(honnetes_textes, avec_textes, champ, reglages)
    sortie = {}
    for p, r in retenus.items():
        ids = honnetes_ids if r.laisse_honnete else [list(a) for a in fabriques[p].actions]
        if sorted(x for a in ids for x in a) != sorted(x for a in honnetes_ids for x in a):
            raise GardeArret(f"épisode {episode['episode']} : multiensemble des jetons non conservé (A2)")
        if [decoder(a) for a in ids] != list(r.textes):
            raise GardeArret(f"épisode {episode['episode']} : textes retenus différents du décodage des jetons (A2)")
        iv.exiger_contexte_reconstruit(r, _contexte_inchange(fmt, tache, honnetes_ids, ids, guide))
        iv.exiger_plan_deplace_conforme(honnetes_textes, r)
        sortie[p] = (r, ids)
    return sortie


def fabriquer_condition(fmt, episodes: Sequence[Mapping], taches: Mapping[str, Mapping], champ: str | None,
                        doses: Sequence[float], entropie: int, reglages, guide) -> dict[float, dict]:
    """Transcriptions d'une condition, au grain du jeton. `champ=None` : témoin identité (aucun déplacement).
    Rend, par dose : épisodes retenus (identifiants, textes, déplacements, motif) et bilan des comptes par motif."""
    decoder = _decodeur(fmt)
    par_dose = {float(p): {"episodes": [], "retenus": [], "fabriques": []} for p in doses}
    for ep in episodes:
        triplets = []
        for ids, texte in zip(ep["actions"], ep["textes"]):
            if decoder(ids) != texte:
                raise GardeArret(f"épisode {ep['episode']} : texte d'une action différent du décodage de ses jetons")
            triplets.append((list(ids), fab.decalages_par_decodage(decoder, ids, texte), texte))
        fabriques = {float(p): iv.fabriquer_episode_jetons(triplets, float(p), champ, entropie, ep["tache"], ep["k"])
                     for p in doses}
        if champ is None:
            for p, f in fabriques.items():
                if not f.laisse_honnete or f.deplacements:
                    raise GardeArret("témoin identité : un déplacement a été fait")
                par_dose[p]["episodes"].append(dict(ep, deplacements={}, laisse_honnete=True, motif=None))
                par_dose[p]["fabriques"].append(f)
            continue
        for p, (r, ids) in retenir_et_controler(fmt, ep, taches[ep["tache"]], fabriques, champ, reglages, guide).items():
            par_dose[p]["episodes"].append({"episode": ep["episode"], "tache": ep["tache"], "k": ep["k"], "actions": ids,
                                            "textes": list(r.textes), "deplacements": {str(i): j for i, j in r.deplacements.items()},
                                            "laisse_honnete": r.laisse_honnete, "motif": r.motif})
            par_dose[p]["retenus"].append((ep["textes"], r))
            par_dose[p]["fabriques"].append(fabriques[p])
    for p, d in par_dose.items():
        motifs = {m: sum(e["motif"] == m for e in d["episodes"]) for m in iv.MOTIFS_LAISSE_HONNETE}
        d["bilan"] = dict(fab.bilan(d.pop("fabriques")), motifs_laisses_honnetes=motifs,
                          episodes_laisses_honnetes_retenus=sum(e["laisse_honnete"] for e in d["episodes"]))
        retenus = d.pop("retenus")
        if champ is not None and len(retenus) == EPISODES_LIGNE_1:
            d["bilan"]["dose_recue"] = iv.bilan_dose_recue(
                [(iv.verite_par_construction(h, r), r) for h, r in retenus], p, champ)
    return par_dose


def fabriquer_les_six(fmt, episodes: Sequence[Mapping], taches: Mapping[str, Mapping], entropie: int, reglages,
                      guide) -> dict[str, dict]:
    """Étape (c) : transcriptions des six adaptateurs sur les 128 épisodes honnêtes de fabrication. Les quatre doses
    sont fabriquées ensemble, par épisode, pour qu'un motif trouvé à l'une laisse l'épisode honnête aux quatre."""
    if len(episodes) != EPISODES_LIGNE_1:
        raise GardeArret(f"étape (c) : {len(episodes)} épisodes, {EPISODES_LIGNE_1} exigés")
    doses = fabriquer_condition(fmt, episodes, taches, "CONTROLS", iv.DOSES_FABRIQUEES, entropie, reglages, guide)
    sortie = {f"controls-{p:.2f}": doses[p] for p in iv.DOSES_FABRIQUEES}
    sortie["identite"] = fabriquer_condition(fmt, episodes, taches, None, (1.0,), entropie, reglages, guide)[1.0]
    sortie["prediction-1.00"] = fabriquer_condition(fmt, episodes, taches, "PREDICTION", (1.0,), entropie, reglages,
                                                    guide)[1.0]
    if tuple(sortie) != NOMS_DES_ADAPTATEURS:
        raise GardeArret("étape (c) : les six adaptateurs, dans l'ordre du texte, exigés")
    return sortie


def fabriquer_jumeaux_de_verification(fmt, episodes: Sequence[Mapping], taches: Mapping[str, Mapping], entropie: int,
                                      reglages, guide) -> dict:
    """Étape (i) : jumeaux déplacés à la dose 1 des épisodes honnêtes de vérification, chacun rejoué (3.1) ; un épisode
    laissé honnête n'a pas de jumeau."""
    return fabriquer_condition(fmt, episodes, taches, "CONTROLS", (1.0,), entropie, reglages, guide)[1.0]


def empreinte_des_transcriptions(episodes: Sequence[Mapping]) -> str:
    """Empreinte des transcriptions d'un adaptateur (6.3 (c) ; contrôle 4 de 6.4) : identifiants de chaque action."""
    h = hashlib.sha256()
    for ep in episodes:
        h.update(ep["episode"].encode("utf-8"))
        for a in ep["actions"]:
            h.update(b"|" + ",".join(str(int(x)) for x in a).encode("ascii"))
    return h.hexdigest()


# --- Seconde ligne : refabrication identique, distillation, rejeu (l'honnête d'abord) ------------------------------------

def exiger_refabrication_identique(refaites: Mapping[str, Mapping], empreintes_scellees: Mapping[str, str]) -> None:
    """Contrôle 4 de 6.4 : transcriptions refabriquées sur la machine, empreinte égale à celle scellée en (c)."""
    if tuple(refaites) != NOMS_DES_ADAPTATEURS or sorted(empreintes_scellees) != sorted(NOMS_DES_ADAPTATEURS):
        raise GardeArret("refabrication : les six adaptateurs exigés, des deux côtés")
    for nom in NOMS_DES_ADAPTATEURS:
        if empreinte_des_transcriptions(refaites[nom]["episodes"]) != _exiger_empreinte(empreintes_scellees[nom], nom):
            raise GardeArret(f"refabrication de {nom} : empreinte différente de celle scellée en (c) — arrêt avant "
                             "distillation (6.4, point 4)")


def distiller_les_six(modele, fmt, refaites: Mapping[str, Mapping], empreintes_scellees: Mapping[str, str],
                      configuration: Mapping, graines: Mapping, guide, pad_id: int, progres=None) -> dict:
    """Seconde ligne : refabrication identique d'abord, puis un adaptateur par condition, 384 pas chacun (section 2),
    base inchangée vérifiée par empreinte. Mêmes appels que `lanceur_bras_a_v2.distiller_tous`, sur les transcriptions
    de cette version."""
    from ..organismes import lora as lo
    from ..t06 import distillation_transcription as dt
    from . import lanceur_bras_a_v2 as l2
    exiger_refabrication_identique(refaites, empreintes_scellees)
    ref = configuration["reference"]
    a, d = ref["adaptateur"], dict(ref["distillation"], pas_declares=PAS_DE_DISTILLATION)
    cfg = dict(reglages_du_jeu(configuration), adaptateur=a, distillation=d)
    jeux = {nom: l2.exemples(fmt, refaites[nom]["episodes"], cfg, guide) for nom in NOMS_DES_ADAPTATEURS}
    for nom, jeu in jeux.items():
        if l2.pas_calcules(len(jeu), cfg) != PAS_DE_DISTILLATION:
            raise GardeArret(f"adaptateur {nom} : {l2.pas_calcules(len(jeu), cfg)} pas calculés ≠ {PAS_DE_DISTILLATION} "
                             "(section 2) : arrêt avant distillation")
    lo.injecter(modele, a["rang"], a["alpha"], l2.graine_entiere(graines["injection"]), tuple(a["cibles"]))
    dt.adaptateurs_en_simple_precision(modele)
    base = lo.empreinte_base(modele)
    sortie = {}
    for nom in NOMS_DES_ADAPTATEURS:
        lo.charger_etat(modele, dt.etat_initial(modele, a["rang"], a["alpha"], l2.graine_entiere(graines[f"adaptateur/{nom}"])))
        lo.fixer_dose(modele, 1.0)
        journal = dt.distiller_transcriptions(modele, jeux[nom], pad_id, d["epoques"], d["pas"], d["lot"],
                                              l2.graine_entiere(graines[f"distillation/{nom}"]), d["norme_max"], progres=progres)
        if lo.empreinte_base(modele) != base:
            raise GardeArret(f"adaptateur {nom} : la base a changé pendant la distillation")
        sortie[nom] = {"etat": {k: v.detach().to("cpu").clone() for k, v in lo.etat_lora(modele).items()},
                       "empreinte": lo.empreinte_adaptateurs(modele), "journal": journal,
                       "empreinte_des_transcriptions": empreintes_scellees[nom]}
    return {"adaptateurs": sortie, "empreinte_base": base}


def rejouer_seconde_ligne(modele, fmt, verification: Sequence[Mapping], configuration: Mapping, graines: Mapping, guide,
                          adaptateurs: Mapping, chrono=None, rejouer: Callable | None = None) -> dict:
    """Exigence 2 : sur les 16 tâches de vérification, la condition honnête **d'abord**, à l'échelle 0 (base au bit
    près), puis chaque adaptateur à l'échelle 1, mêmes graines d'action (6.3 (i) ; `lanceur_bras_a_v2.rejouer`)."""
    if rejouer is None:
        from .lanceur_bras_a_v2 import rejouer
    if tuple(adaptateurs) != NOMS_DES_ADAPTATEURS:
        raise GardeArret(f"rejeu : les six adaptateurs {NOMS_DES_ADAPTATEURS}, dans cet ordre, exigés")
    if len(verification) != 16:
        raise GardeArret("rejeu : les 16 tâches de vérification exigées (nœud 11)")
    sortie = rejouer(modele, fmt, list(verification), reglages_du_jeu(configuration), graines, guide, adaptateurs, chrono)
    if tuple(sortie) != (CONDITION_HONNETE,) + NOMS_DES_ADAPTATEURS:
        raise GardeArret("rejeu : la condition honnête d'abord, puis les six adaptateurs, exigés (6.3 (i))")
    for condition, eps in sortie.items():
        if len(eps) != EPISODES_LIGNE_1 or any(len(e["actions"]) != PAS for e in eps):
            raise GardeArret(f"rejeu, condition {condition} : 128 épisodes de dix actions exigés")
    return sortie


# --- Versement, manifeste scellé, destruction (8.5) -----------------------------------------------------------------------

def nom_du_dossier_de_versement(ligne: str, etat: str, quand: datetime) -> str:
    """`diag/organismes-discrets-v-a-v2/<ligne ou lot>-<état>-<date UTC>/` (8.5)."""
    for nom, v in (("ligne", ligne), ("état", etat)):
        if not isinstance(v, str) or re.fullmatch(r"[a-z0-9][a-z0-9-]*", v) is None:
            raise GardeArret(f"versement : {nom} {v!r}, minuscules, chiffres et tirets exigés")
    if not isinstance(quand, datetime) or quand.tzinfo is None:
        raise GardeArret("versement : date UTC avec fuseau exigée")
    return f"{RACINE_DU_VERSEMENT}/{ligne}-{etat}-{quand.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"


def inventaire(dossier) -> list[dict]:
    """Noms, tailles et empreintes de tout ce que porte le dossier (8.5), sans rien ouvrir d'autre ; lien refusé."""
    dossier = Path(dossier)
    sortie = []
    for p in sorted(dossier.rglob("*")):
        if p.is_symlink():
            raise GardeArret(f"versement : {p} est un lien symbolique — non suivi, à dire dans les manquants")
        if p.is_file() and p.name not in (NOM_DU_MANIFESTE_DU_VERSEMENT, NOM_DU_MANIFESTE_DU_VERSEMENT + ".sha256"):
            sortie.append({"nom": p.relative_to(dossier).as_posix(), "taille": p.stat().st_size, "sha256": empreinte(p)})
    return sortie


def sceller_le_versement(dossier, manifeste_de_ligne: Mapping, manquants: Sequence[Mapping] = ()) -> str:
    """Manifeste du versement : inventaire, manifeste de la ligne, ce qui manque et pourquoi ; écrit sans écraser puis
    scellé. Rend son empreinte."""
    dossier = Path(dossier)
    for m in manquants:
        if not isinstance(m, Mapping) or sorted(m) != ["nom", "pourquoi"] or not all(isinstance(v, str) and v for v in m.values()):
            raise GardeArret("versement : chaque manquant porte `nom` et `pourquoi`")
    contenu = {"inventaire": inventaire(dossier), "manifeste_de_la_ligne": dict(manifeste_de_ligne),
               "manquants": [dict(m) for m in manquants]}
    if not contenu["inventaire"] and not contenu["manquants"]:
        raise GardeArret("versement vide et sans manquant déclaré : refusé")
    chemin = ecrire_sans_ecraser(dossier / NOM_DU_MANIFESTE_DU_VERSEMENT, contenu)
    return sceller(chemin)


def exiger_manifeste_du_versement_scelle(dossier) -> str:
    """Garde de 8.4, ligne 1195 : manifeste scellé, intact, et chaque pièce inventoriée encore là, à son empreinte."""
    chemin = Path(dossier) / NOM_DU_MANIFESTE_DU_VERSEMENT
    if not chemin.is_file():
        raise GardeArret("destruction ou suppression demandée sans manifeste scellé du versement — refusée (8.5)")
    sha = verifier(chemin)
    contenu = json.loads(chemin.read_text(encoding="utf-8"))
    if contenu.get("inventaire") != inventaire(dossier):
        raise GardeArret("versement : le dossier ne répond plus à l'inventaire scellé — destruction refusée")
    return sha


def detruire_l_instance(identifiant: object, dossier_du_versement, arreter_par_identifiant: Callable[[str], object]) -> dict:
    """Arrêt par identifiant d'instance (R10), **après** le manifeste scellé du versement (8.5). La fonction passée fait
    l'arrêt (commande de la session) ; ce module n'en a aucune."""
    sha = exiger_manifeste_du_versement_scelle(dossier_du_versement)
    if not isinstance(identifiant, str) or _IDENTIFIANT_D_INSTANCE.fullmatch(identifiant) is None:
        raise GardeArret(f"identifiant d'instance {identifiant!r} : chiffres seuls exigés (R10, jamais un motif)")
    retour = arreter_par_identifiant(identifiant)
    return {"instance": identifiant, "manifeste_du_versement_sha256": sha, "retour": retour}


def manifeste_de_la_ligne_1(configuration: Mapping, constat_de_depart: Mapping, graines: Mapping, resume: Mapping | None,
                            commit: str, arret: str | None) -> dict:
    """Manifeste de la course pour la ligne 1 (6.2, dernier alinéa) : configuration et empreinte, versions, graines
    (états de contrôle), commit, prix, durée, comptes ; et l'arrêt, s'il y en a un."""
    from ..manifeste import versions
    if not isinstance(commit, str) or re.fullmatch(r"[0-9a-f]{40}", commit) is None:
        raise GardeArret("manifeste : commit entier de quarante signes exigé")
    return {"ligne": 1, "configuration": {"chemin": configuration["chemin"], "sha256": configuration["sha256"]},
            "texte_sha256": configuration["texte_sha256"], "lanceur_sha256": configuration["lanceur_sha256"],
            "entropie": str(configuration["entropie"]), "graines": dict(graines), "versions": versions(), "commit": commit,
            "depart": dict(constat_de_depart), "resume": None if resume is None else dict(resume), "arret": arret}


# --- Commande : constat de départ de la ligne 1 (aucun réseau, aucune clé) -----------------------------------------------

def _main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Constat de départ de la ligne 1 du bras A (aucune instance créée ici).")
    p.add_argument("--configuration", required=True)
    p.add_argument("--racine", default=".")
    p.add_argument("--go", required=True)
    p.add_argument("--registre-go", default="registres/go.md")
    p.add_argument("--credit-lu-usd", type=float, required=True)
    p.add_argument("--tarif-carte-usd-h", type=float, required=True)
    p.add_argument("--tarif-stockage-usd-h", type=float, required=True)
    p.add_argument("--tarif-telechargement-usd-go", type=float, required=True)
    p.add_argument("--date-du-releve-utc", required=True)
    a = p.parse_args(argv)
    configuration = lire_la_configuration(a.configuration, a.racine)
    constat = constat_de_depart_ligne_1(
        configuration, go_id=a.go, texte_du_registre_go=Path(a.registre_go).read_text(encoding="utf-8"),
        aujourd_hui=datetime.now(timezone.utc).date(), credit_lu_usd=a.credit_lu_usd,
        tarifs={"carte_usd_h": a.tarif_carte_usd_h, "stockage_usd_h": a.tarif_stockage_usd_h,
                "telechargement_usd_go": a.tarif_telechargement_usd_go, "date_utc": a.date_du_releve_utc})
    print(json.dumps(constat, ensure_ascii=False, sort_keys=True, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(_main())
