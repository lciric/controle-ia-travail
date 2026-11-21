"""Lanceur de la **seconde passe** de la lecture des directions des sondes : lentille publique, lentille des logits, notre
lentille R (et ses deux moitiés), notre lentille S, comparaisons entre lentilles, reproduction de la première passe.

Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`).
Le texte décide, le code suit. Sous-commandes : `montage`, `recuperer`, `calcul`, `phrases`. Le lanceur n'inscrit aucune ligne
de registre et ne pousse rien ; il propose des lignes. Horloge : 10 heures ; espace : 8 Go libres au départ.

Ce qui est réemployé tel quel, par appel (R12 : aucun module existant n'est réécrit) : les entrées (`entrees_v3`, même liste
blanche, mêmes refus, mêmes empreintes), le montage (`montage_v1`), la lecture par une lentille R (`lecture_v1`), les nuls et
leurs graines (`nuls_v1` : **mêmes clés** que la première passe), la calibration (`audits_v1`), et, de `lanceur_v7` :
l'horloge, la garde d'espace, les écritures fermées, le versement et le nettoyage du dossier de travail, le rechargement du
montage, la garde de la fonction de lecture de la première passe, l'audit de la première passe, **le canal des messages
d'arrêt** (versement d'un arrêt cloisonné, ligne affichée aux mots fixes) et **la garde du fichier d'arrêt déjà présent**.

**Code de lecture différent de celui de la première passe** (`MODULES_DIFFERENTS`) : `statistiques_v4` (règle de départage à
la place de la garde d'égalité à trois étages) et ce lanceur. La reproduction le porte en tête.

**Canal des messages d'arrêt** (GO-2026-11-20-56, GO-2026-11-21-06) : une seule fonction, `ligne_affichee`, décide ce qui va
à la sortie d'erreur ; pour un arrêt cloisonné, des mots fixes, et le message entier dans le seul `arret.json`. La seconde
passe n'a pas de garde d'égalité : elle ne lève aucun des deux arrêts cloisonnés de la première ; le canal est gardé tel quel.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import torch

from .. import manifeste as mf
from ..scellement import verifier
from . import audits_v2 as au
from . import comparaisons_lentilles_v1 as co
from . import constantes_v1 as K
from . import constantes_v2 as K2
from . import entrees_v3 as en
from . import lanceur_v7 as l7
from . import lecture_entree_v1 as li
from . import lecture_v1 as le
from . import montage_v1 as mo
from . import montage_v2 as m2
from . import nos_lentilles_v1 as nl
from . import nuls_v1 as nu
from . import phrases_v2 as ph
from . import reproduction_v1 as rp
from . import statistiques_v4 as st
from .constantes_v1 import Arret, Refus

MODULES = ("__init__", "constantes_v1", "constantes_v2", "entrees_v2", "entrees_v3", "montage_v1", "montage_v2", "lecture_v1",
           "lecture_entree_v1", "nuls_v1", "statistiques_v1", "statistiques_v2", "statistiques_v3", "statistiques_v4", "audits_v1",
           "audits_v2", "phrases_v1", "phrases_v2", "nos_lentilles_v1", "comparaisons_lentilles_v1", "reproduction_v1",
           "lanceur_v7", "lanceur_seconde_passe_v1")
MODULES_DIFFERENTS = ("statistiques_v4", "lanceur_seconde_passe_v1")
CHEMIN_PAQUET = l7.CHEMIN_PAQUET
MARQUE = l7.MARQUE
ADDENDUM = {"chemin": K2.ADDENDUM, "sha256": K2.EMPREINTE_ADDENDUM}
TEXTE = {"chemin": K2.TEXTE_V2, "sha256": K2.EMPREINTE_TEXTE_V2}
DOSSIER_NOS_LENTILLES = "tenseurs/nos-lentilles"       # sous `tenseurs` : jamais copié par le versement (licence ; espace)
NOM_MONTAGE, NOM_TABLES, NOM_ENTREES = "montage-lentilles-bbis-v2.json", "tables-lentilles-bbis-v2.json", "entrees-lentilles-bbis-v2.json"
PREFIXE_LECTURES = "lectures-lentilles-bbis-v2"
MOTIF_CALIBRATION_D_UNE_LECTURE = "calibration du nul hors de ses bornes pour l'une des deux lentilles R"
SANS_OBJET_RHO = "sans objet : lecture exactement indépendante de la norme"


@dataclass
class Reglages(l7.Reglages):
    """Réglages de la première passe, plus ceux de la seconde. Les essais sur jouets en remplacent certains ; la ligne de
    commande n'en expose aucun."""
    disque_depart: int = K2.DISQUE_DEPART_OCTETS_V2
    horloge_s: float = K2.HORLOGE_S_V2
    forme_plongements: tuple = K2.FORME_PLONGEMENTS
    lentilles: dict = field(default_factory=lambda: {
        l: {"n_couches": K2.N_COUCHES_OUT[l], "largeur": K.LARGEUR, "couches": K.COUCHES, "n_docs": K2.N_DOCS,
            "next_doc": K2.NEXT_DOC, "meta": None} for l in K2.NOS_LENTILLES})
    piece_meta_s: str = K2.PIECE_META_S
    sha256_piece_meta_s: str = K2.EMPREINTE_PIECE_META_S
    cibles_corpus: object = None                        # point de branchement (nœud N-dev-1) : voir `montage_v2.cibles_du_corpus`


Contexte = l7.Contexte


def _horloge(ctx) -> l7.Horloge:
    return l7.Horloge(ctx.travail, limite_s=ctx.reglages.horloge_s, maintenant=ctx.maintenant)


def ligne_registre(cle: str, chemin: str, sha256: str, heure: str | None = None) -> str:
    """Ligne proposée pour le registre propre ; seules les clés ajoutées par la v2 sont permises."""
    if cle not in K2.CLES_V2:
        raise Refus(f"clé {cle!r} : hors des clés ajoutées par la v2")
    heure = heure or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f"| {cle} | {heure} | {chemin} | {sha256} |"


def empreintes_du_code() -> dict:
    ici = Path(__file__).resolve().parent
    return {f"{m}.py": mo.sha256_fichier(ici / f"{m}.py") for m in MODULES}


def exiger_fiche_code(racine_depot: Path, registre_propre: Path) -> dict:
    """« Liste d'arrêt », lignes de la v2 : `SCELLEMENT-LENTILLES-BBIS-V2` ou `GO-LENTILLES-BBIS-V2` absente ; code non cité par
    `CODE-LENTILLES-BBIS-V2` : rien de la seconde passe ne part. La fiche citée par la ligne porte : `commit`, `fichiers`
    (empreinte de chaque module de `MODULES`), `essais`, `contre_lecture` {chemin, sha256}, `addendum_concentration` {chemin,
    sha256} (égal à la ligne de l'addendum), `code_de_lecture_different_de_la_premiere_passe` (égal à `MODULES_DIFFERENTS` :
    version neuve **déclarée**), `essai_de_la_forme_de_l_archive` {`script`, `sortie`} (l'essai opposable, versé scellé).
    Appelée avant toute requête ou ouverture."""
    etat = nl.exiger_registre_v2(registre_propre)
    ligne = etat.derniere(K2.CLE_CODE_V2)
    p = Path(racine_depot) / str(ligne.chemin)
    if not p.is_file() or mo.sha256_fichier(p) != ligne.sha256:
        raise Refus(f"fiche citée par {K2.CLE_CODE_V2} absente ou d'une autre empreinte que la ligne : rien de la seconde passe ne part")
    try:
        fiche = json.loads(p.read_text(encoding="utf-8"))
        fichiers, lecture = fiche["fichiers"], fiche["contre_lecture"]
        forme = (isinstance(fichiers, dict) and isinstance(fiche["essais"], (dict, list)) and bool(lecture["chemin"])
                 and bool(lecture["sha256"]) and bool(str(fiche["commit"])))
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError):
        forme = False
    if not forme:
        raise Refus(f"fiche {K2.CLE_CODE_V2} d'une autre forme que les fiches CODE- du registre : rien de la seconde passe ne part")
    if fiche.get("addendum_concentration") != ADDENDUM:
        raise Refus(f"fiche {K2.CLE_CODE_V2} sans le chemin et l'empreinte de l'addendum de concentration scellé : rien de la "
                    "seconde passe ne part")
    if list(fiche.get("code_de_lecture_different_de_la_premiere_passe") or []) != list(MODULES_DIFFERENTS):
        raise Refus(f"fiche {K2.CLE_CODE_V2} : modules de lecture différents de ceux de la première passe non déclarés, ou autres "
                    f"que {', '.join(MODULES_DIFFERENTS)} : rien de la seconde passe ne part")
    essai = fiche.get("essai_de_la_forme_de_l_archive")
    for quoi in ("script", "sortie"):
        piece = essai.get(quoi) if isinstance(essai, dict) else None
        chemin = Path(racine_depot) / str((piece or {}).get("chemin"))
        if not isinstance(piece, dict) or not chemin.is_file() or mo.sha256_fichier(chemin) != piece.get("sha256"):
            raise Refus(f"fiche {K2.CLE_CODE_V2} : essai opposable de la forme de l'archive ({quoi}) non cité, absent ou d'une "
                        "autre empreinte : rien de la seconde passe ne part")
    ici = Path(__file__).resolve().parent
    for m in MODULES:
        nom = f"{CHEMIN_PAQUET}/{m}.py"
        if fichiers.get(nom) != mo.sha256_fichier(ici / f"{m}.py"):
            raise Refus(f"{nom} : empreinte absente de la fiche {K2.CLE_CODE_V2} ou différente : rien de la seconde passe ne part")
    return {"fiche": str(ligne.chemin), "sha256": ligne.sha256, "commit_de_la_fiche": str(fiche["commit"]), "addendum": dict(ADDENDUM),
            "code_de_lecture_different_de_la_premiere_passe": list(MODULES_DIFFERENTS),
            "essai_de_la_forme_de_l_archive": essai}


def _lecture(ctx, registre_propre: Path) -> tuple:
    """Registre, issue des nœuds, fiche de rangement, condition de lecture : ce qui se lit avant tout."""
    etat = nl.exiger_registre_v2(registre_propre)
    issue = nl.exiger_issue_des_noeuds(ctx.racine_depot, etat)
    fiche = nl.lire_fiche(ctx.racine_depot, etat)
    return etat, issue, fiche, nl.condition_de_lecture(fiche, etat, ctx.racine_depot)


# ========================================================================================================================================
# Montage de la seconde passe (plan, points 4 et 5)
# ========================================================================================================================================
def monter(ctx) -> dict:
    """Refait le montage de la première passe, avec : 8 Go libres au départ ; garde par les noms des variables
    d'environnement ; essai d'un octet de chacun de nos fichiers ; `model.embed_tokens.weight` ; nos lentilles lues en flux,
    vérifiées, contrôlées ; gardes de la fonction de lecture de notre R, de ses moitiés et de notre S. Ne touche aucune
    sonde. Rend le rapport, écrit aussi dans `diag/<run>/montage-lentilles-bbis-v2.json` (jamais la clé)."""
    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, ctx.registre_propre)
    etat_registre, issue, fiche, conditions = _lecture(ctx, ctx.registre_propre)
    noms_de_cles = m2.exiger_noms_des_variables(ctx.env)
    mo.exiger_sans_debogage(ctx.env)
    cle = mo.lire_cle(ctx.env)
    if ctx.travail.exists():
        raise Arret(f"{ctx.travail} existe déjà : le dossier de travail de cette chaîne est neuf (R12)")
    ctx.travail.parent.mkdir(parents=True, exist_ok=True)
    libre = l7.exiger_disque(ctx.travail.parent, r.disque_depart, "au départ de la seconde passe", ctx.mesure_disque)
    ctx.travail.mkdir()
    (ctx.travail / MARQUE).write_text("Dossier de travail de la seconde passe de la lecture des sondes de l'étape B bis par lentilles.\n")
    horloge = _horloge(ctx)
    hf_home = ctx.travail / "hf"
    transport = ctx.transport if ctx.transport is not None else mo.TransportRequests()
    rapport = {"run": ctx.run, "texte": dict(TEXTE), "addendum": dict(ADDENDUM), "versions": l7._versions(),
               "code": {"commit": l7._commit(ctx.racine_depot), "empreintes": empreintes_du_code(), "fiche_code": fiche_code},
               "machine": {"fils": os.cpu_count(), "octets_libres_au_depart": libre, "octets_de_memoire": l7._memoire()},
               "noms_des_variables_de_cle": noms_de_cles, "premiere_passe_au_montage": etat_registre.premiere_passe,
               "issue_des_noeuds": issue, "course_du_reajustement": conditions["course"],
               "critere_d_identite": {"chemin": K2.CRITERE_IDENTITE, "sha256": K2.EMPREINTE_CRITERE_IDENTITE,
                                      "version": K2.VERSION_CRITERE_IDENTITE},
               "fiche_de_rangement": dict(fiche["_ligne"]),
               "condition_de_lecture": {l: conditions[l].table() for l in K2.NOS_LENTILLES}}

    # réseau, avant tout flux long : un octet par hôte et par sorte de fichier, nos deux fichiers compris
    premier_poids = sorted(r.poids)[0]
    cibles = [mo.Cible("lentille publique", mo.url_fichier(r.depot_lentille, r.revision_lentille, r.fichier_lentille)),
              mo.Cible("fichier de poids à porte", mo.url_fichier(r.depot_llama, r.revision_llama, premier_poids), avec_cle=True),
              mo.Cible("dépôt du code voisin", r.url_voisin + "/info/refs?service=git-upload-pack", sorte="en-tête")]
    cibles += m2.cibles_de_nos_lentilles(fiche, conditions)
    rapport["essais_un_octet"] = mo.essais_un_octet(transport, cle, cibles)

    voisin = ctx.travail / "voisin"
    rapport["voisin"] = {"commit": mo.cloner_voisin(voisin, r.url_voisin, r.commit_voisin)}
    readout = voisin / "neuron_lens" / "readout.py"
    rapport["voisin"]["readout"] = mo.comparer_readout(readout, ctx.racine_depot / r.copie_readout, r.sha256_copie_readout)
    rapport["voisin"]["fichiers_corriges"] = mo.appliquer_correctifs(voisin, ctx.racine_depot, r.correctifs)
    rapport["essais_un_octet"] += mo.essais_un_octet(transport, cle, m2.cibles_du_corpus(voisin, transport, r.cibles_corpus))
    horloge.controler("essais d'un octet")

    petits = {}
    for nom, (taille, ident) in sorted(r.petits.items()):
        petits[nom] = mo.telecharger_petit(transport, mo.url_fichier(r.depot_llama, r.revision_llama, nom), nom, taille, ident, cle)
    if "tokenizer.json" in petits and hashlib.sha256(petits["tokenizer.json"]).hexdigest() != r.sha256_tokeniseur:
        raise Arret("SHA-256 du tokeniseur différent de celui du texte : arrêt ; message à la session principale")
    mo.poser_cache_tokeniseur(hf_home, {n: c for n, c in petits.items() if n.endswith(".json") and n != K.INDEX_LLAMA},
                              r.depot_llama, r.revision_llama)
    rapport["petits_fichiers"] = {n: {"taille": len(c), "identifiant_git": mo.identifiant_git(c)} for n, c in petits.items()}
    rapport["tie_word_embeddings"] = m2.cle_tie_word_embeddings(petits["config.json"]) if "config.json" in petits else None
    l7.essayer_tokeniseur_du_cache(ctx, voisin, hf_home)
    rapport["essai_du_tokeniseur_hors_ligne"] = {"tenu": True, "journal": "journal-essai-tokeniseur.txt"}

    # poids : les tenseurs de la première passe, plus les plongements
    m2.exiger_plongements_dans_l_index(petits[K.INDEX_LLAMA])
    voulus = (("lm_head.weight", "model.norm.weight") + tuple(f"model.layers.{c}.mlp.down_proj.weight" for c in r.couches)
              + (K2.TENSEUR_PLONGEMENTS,))
    par_fichier = mo.tenseurs_par_fichier(petits[K.INDEX_LLAMA], voulus)
    interface = mo.sha256_par_interface(transport, r.depot_llama, r.revision_llama, cle, tuple(par_fichier))
    tenseurs, poids = {}, {}
    for fichier, noms in par_fichier.items():
        if fichier not in r.poids:
            raise Arret(f"fichier de poids {fichier} absent de la table du texte : arrêt ; message à la session principale")
        sha, taille = interface[fichier]
        mo.exiger_pointeur(fichier, sha, taille, r.poids[fichier][1], r.poids[fichier][0])
        l7.exiger_disque(ctx.travail, r.disque_calcul, "pendant le montage", ctx.mesure_disque)
        tenseurs |= mo.lire_poids_en_flux(transport, mo.url_fichier(r.depot_llama, r.revision_llama, fichier), cle, noms,
                                          ctx.travail / "tenseurs", taille, sha)
        poids[fichier] = {"taille": taille, "sha256": sha, "identifiant_git_du_pointeur": r.poids[fichier][1], "tenseurs": list(noms)}
        horloge.controler(f"poids {fichier}")
    m2.exiger_forme_des_plongements(tenseurs[K2.TENSEUR_PLONGEMENTS], r.forme_plongements)
    rapport["poids"] = poids

    # lentille publique, comme à la première passe
    licences = {}
    for chemin, (taille, ident) in sorted(r.licences_lentille.items()):
        c = mo.telecharger_petit(transport, mo.url_fichier(r.depot_lentille, r.revision_lentille, chemin), chemin, taille, ident)
        licences[chemin] = {"taille": len(c), "identifiant_git": mo.identifiant_git(c)}
    mo.exiger_pointeur("lentille publique", r.sha256_lentille, r.taille_lentille, r.pointeur_lentille, r.taille_lentille)
    fichier_lentille = ctx.travail / "lentille-publique.pt"
    mo.telecharger_en_fichier(transport, mo.url_fichier(r.depot_lentille, r.revision_lentille, r.fichier_lentille),
                              fichier_lentille, r.taille_lentille, r.sha256_lentille)
    mo.exiger_fichier_lentille(fichier_lentille, r.taille_lentille, r.sha256_lentille)
    controle, matrices = mo.controler_lentille(fichier_lentille, r.largeur, r.couches_lentille, r.couches, r.couche_cible)
    (ctx.travail / "lentille").mkdir()
    for l, m in matrices.items():
        np.save(ctx.travail / "lentille" / f"J-{l}.npy", m)
    del matrices
    fichier_lentille.unlink()
    rapport["lentille_publique"] = {"depot": r.depot_lentille, "revision": r.revision_lentille, "fichier": r.fichier_lentille,
                                    "taille": r.taille_lentille, "sha256": r.sha256_lentille, "licences": licences, **controle}
    horloge.controler("lentille publique")

    jetons = mo.calculer_jetons_gardes(voisin, hf_home, ctx.travail, ctx.python, ctx.env)
    rapport["jetons_gardes"] = mo.exiger_jetons_gardes(jetons["ids"], r.n_jetons, r.sha256_jetons)
    horloge.controler("jetons gardés")

    # nos lentilles : flux à la révision de la fiche, `meta` et état, matrices
    nos, descriptions, rapport["nos_lentilles"] = {}, {}, {}
    publiques = m2.matrices_publiques(ctx.travail / "lentille", r.couches)
    for lettre in K2.NOS_LENTILLES:                     # R d'abord : le contrôle de S emploie les matrices de R
        cond = conditions[lettre]
        if not cond.lue:
            rapport["nos_lentilles"][lettre] = {"lue": False, "motif": cond.motif}
            continue
        l = fiche["lentilles"][lettre]
        l7.exiger_disque(ctx.travail, r.disque_calcul, "pendant le montage", ctx.mesure_disque)
        piece = ctx.racine_depot / r.piece_meta_s if lettre == "S" else None
        attendu = m2.attendu_de(lettre, r.lentilles, piece, r.sha256_piece_meta_s)
        dossier = ctx.travail / DOSSIER_NOS_LENTILLES / lettre
        description, etat_lentille = m2.monter_une_lentille(transport, cle, lettre, l, cond.palier, attendu, dossier)
        nos[lettre] = nl.charger_notre_lentille(dossier, description)
        controle_matrices = nl.controler_matrices(nos[lettre], publique=publiques, notre_r=nos.get("R"))
        descriptions[lettre] = description | {"empreintes_des_matrices_lues": dict(nos[lettre].empreintes_montage)}
        rapport["nos_lentilles"][lettre] = {
            "lue": True, "depot": l["depot"], "revision": l["revision"], "chemin": l["chemin"], "taille": description["taille"],
            "sha256_calcule_sur_le_flux": description["sha256"], "verdict_d_identite": cond.verdict,
            "chiffres_recopies_de_la_fiche": cond.chiffres, **etat_lentille, "controles_des_matrices": controle_matrices,
            "couches": {str(c): dict(v) for c, v in sorted(cond.couches.items())}}
        horloge.controler(f"notre lentille {lettre}")
    del publiques

    etat = {"tenseurs": tenseurs, "empreintes_matrices": controle["empreintes_matrices_gardees"],
            "readout": str(readout.relative_to(ctx.travail)), "point_de_capture": controle["provenance"].get("capture_point"),
            "nos_lentilles": descriptions, "premiere_passe_au_montage": etat_registre.premiere_passe,
            "fiche_de_rangement": dict(fiche["_ligne"])}
    (ctx.travail / "etat-montage.json").write_text(json.dumps(etat, indent=1, sort_keys=True))

    charge = charger_montage(ctx)
    rapport["lignes_de_sortie_egales"] = st.paires_de_lignes_egales(l7._np(charge.base.wu))
    rapport["plongements_lies"] = charge.lies
    graines = nu.Graines()
    rapport["garde_fonction_lecture"] = jouer_gardes_lecture(charge, graines, r)
    rapport["graines"] = {k: str(v) for k, v in sorted(graines.derivees.items())}
    horloge.controler("garde de la fonction de lecture")

    rapport["gardes"] = {"toutes_tenues": True, "liste": [
        "lignes de la v2 et place de la ligne de l'addendum de concentration", "issue des nœuds N12 et N17 recopiée par la pièce du GO",
        "fiche du code citée par CODE-LENTILLES-BBIS-V2", "fiche de rangement (empreinte, révisions, SHA-256, verdicts)",
        "condition de lecture de chaque lentille", "noms des variables d'environnement", "clé présente et non vide",
        "aucun mode de débogage", "espace disque au départ (8 Go)", "essais d'un octet (nos fichiers compris)", "commit du voisin",
        "readout.py égal à la copie versée", "empreintes des correctifs", "petits fichiers", "tokeniseur lu du cache hors ligne",
        "pointeurs des poids", "SHA-256 des flux de poids", "plongements présents à l'index et de la forme du texte",
        "licences, taille et SHA-256 de la lentille publique", "disposition, provenance et 31 matrices de la lentille publique",
        "jetons gardés (nombre, empreinte)", "SHA-256 et taille de nos fichiers calculés sur le flux", "forme de l'archive",
        "`meta` et état de nos lentilles", "contrôles des matrices de nos lentilles", "garde de la fonction de lecture (toutes lentilles)"]}
    rapport["duree_cumulee_s"] = horloge.ecoule()
    chemin = ctx.sortie / "diag" / ctx.run / NOM_MONTAGE
    sha = l7._ecrire_ferme(chemin, rapport)
    mo.aucune_occurrence([ctx.travail, ctx.sortie], cle)
    horloge.consigner()
    return {"chemin": str(chemin), "sha256": sha,
            "ligne_proposee": ligne_registre(K2.CLE_MONTAGE_V2, f"diag/{ctx.run}/{NOM_MONTAGE}", sha)}


@dataclass
class Charge:
    """Ce que le calcul de la seconde passe lit du dossier de travail monté : la charge de la première passe (`base`), les
    plongements des jetons gardés, et nos lentilles montées."""
    base: l7.Charge
    plongements: torch.Tensor
    centres: torch.Tensor
    lies: bool
    nos: dict
    etat: dict


def charger_montage(ctx) -> Charge:
    base = l7.charger_montage(ctx)
    etat = base.etat
    if "nos_lentilles" not in etat or K2.TENSEUR_PLONGEMENTS not in etat["tenseurs"]:
        raise Arret("montage de la seconde passe absent du dossier de travail : rien ne part")
    ids = base.ids_gardes
    e = torch.from_numpy(mo.charger_tenseur(ctx.travail / "tenseurs", etat["tenseurs"][K2.TENSEUR_PLONGEMENTS], lignes=ids))
    if e.shape != base.wu.shape:
        raise Arret("forme des plongements des jetons gardés inattendue : arrêt")
    nos = {}
    for lettre, description in etat["nos_lentilles"].items():
        lentille = nl.charger_notre_lentille(ctx.travail / DOSSIER_NOS_LENTILLES / lettre, description)
        lentille.empreintes_montage = dict(description["empreintes_des_matrices_lues"])
        nos[lettre] = lentille
    return Charge(base, e, li.centrer(e), li.plongements_lies(e, base.wu), nos, etat)


def _t(matrice: np.ndarray) -> torch.Tensor:
    return torch.from_numpy(np.ascontiguousarray(matrice))


def jouer_gardes_lecture(charge: Charge, graines: nu.Graines, r) -> list[dict]:
    """Plan, point 5 : la garde de la première passe (lentille publique, lentille des logits), puis, sur les mêmes 64 colonnes,
    notre R et chacune de ses moitiés (artefact : la matrice de la couche suivante), et notre S (chemin indépendant ; trois
    artefacts). Un échec : arrêt avant tout calcul."""
    sortie = l7.jouer_garde_lecture(charge.base, graines, r)
    couches = sorted(r.couches)
    for i, couche in enumerate(couches):
        suivante = couches[(i + 1) % len(couches)]
        w_down = charge.base.w_down(couche)
        colonnes = w_down[:, torch.as_tensor(nu.colonnes_garde(graines, couche, w_down.shape[1], r.n_colonnes_garde))]
        if "R" in charge.nos:
            for nom, moitie in ((K2.LENTILLE_NOTRE_R, None), (K2.MOITIE_PAIRE, 0), (K2.MOITIE_IMPAIRE, 1)):
                sortie.append(li.garde_fonction_lecture_notre_r(
                    charge.base.lire_voisin, colonnes, charge.base.gamma, charge.base.wu, _t(charge.nos["R"].matrice(couche, moitie)),
                    _t(charge.nos["R"].matrice(suivante, moitie)), nom, couche))
        if "S" in charge.nos:
            sortie.append(li.garde_fonction_lecture_entree(colonnes, _t(charge.nos["S"].matrice(couche)),
                                                           _t(charge.nos["S"].matrice(suivante)), charge.plongements,
                                                           charge.base.wu, couche, charge.lies))
    return sortie


# ========================================================================================================================================
# Calcul d'une couche
# ========================================================================================================================================
def _rangs(scores: torch.Tensor, ids, k: int = K.K_JETONS) -> torch.Tensor:
    return st.premiers_departages_colonnes(scores, ids, k)["rangs"]


class _Couche:
    """Calcul d'une couche pour toutes les lentilles qui y sont lues : lectures, nuls (les **mêmes** directions nulles pour
    toutes), témoins, garde du rapport à ε, pôles, témoin de couche, plongements seuls, comparaisons entre lentilles."""

    def __init__(self, couche: int, vecteurs: list, charge: Charge, conditions: dict, graines: nu.Graines, r, masques: dict,
                 tableaux: dict, comptes: st.ComptesEgalites, horloge, controle_disque):
        self.couche, self.vecteurs, self.charge, self.graines, self.r = int(couche), vecteurs, charge, graines, r
        self.masques, self.tableaux, self.comptes, self.horloge, self.controle_disque = masques, tableaux, comptes, horloge, controle_disque
        self.ids, base = charge.base.ids_gardes, charge.base
        self.matrices = {l: le.jacobienne_de(l, self.couche, base.publique) for l in K.LENTILLES}
        self.r_lue = "R" in charge.nos and conditions["R"].lue_a(self.couche)
        self.s_lue = "S" in charge.nos and conditions["S"].lue_a(self.couche)
        self.conditions = conditions
        self.lentilles = list(K.LENTILLES)
        self.moities: dict = {}
        if self.r_lue:
            m, indice, empreinte = charge.nos["R"].matrice_verifiee(self.couche)
            self.matrices[K2.LENTILLE_NOTRE_R] = (_t(m), indice, empreinte)
            self.lentilles.append(K2.LENTILLE_NOTRE_R)
            for nom, moitie in ((K2.MOITIE_PAIRE, 0), (K2.MOITIE_IMPAIRE, 1)):
                m, indice, empreinte = charge.nos["R"].matrice_verifiee(self.couche, moitie)
                self.moities[nom] = (_t(m), indice, empreinte)
        if self.s_lue:
            m, indice, empreinte = charge.nos["S"].matrice_verifiee(self.couche)
            self.matrices[K2.LENTILLE_NOTRE_S] = (_t(m), indice, empreinte)
            self.lentilles.append(K2.LENTILLE_NOTRE_S)
        self.rho: dict = {l: [] for l in self.lentilles + list(self.moities) if l != K2.LENTILLE_NOTRE_S}
        self.p_temoins: dict = {}
        self.p_recouvrement: dict = {}
        self.w_down = base.w_down(self.couche)

    # -- lectures -------------------------------------------------------------------------------------------------------------------------
    def _lire(self, v, lentille: str) -> torch.Tensor:
        """Scores de tous les jetons gardés, `[jetons, n]`. Notre S : une colonne non calculable arrête (nul ou témoin)."""
        if lentille == K2.LENTILLE_NOTRE_S:
            return li.lire_entree_exigee(v, self.matrices[lentille][0], self.charge.centres)
        matrice = self.moities[lentille][0] if lentille in self.moities else self.matrices[lentille][0]
        scores, rho = le.lire(v, matrice, self.charge.base.gamma, self.charge.base.wu)
        self.rho[lentille].append(float(rho.min()))
        return scores

    def _nul(self, u: torch.Tensor, t: torch.Tensor, lentille: str, nul: str, prefixe: str) -> dict:
        """Un nul lu par une lentille : résumé, témoins et leurs p, comptes d'égalités, vingt premiers des directions nulles
        (aux deux signes) et des témoins, qui portent les p de recouvrement."""
        a = self._lire(u, lentille)
        resume = st.resumer_nul(a, self.masques, self.ids)
        for nom, valeur in (("moyenne", resume.moyenne), ("ecart_type", resume.ecart_type), ("quantile_0_99", resume.quantile)):
            self.tableaux[f"nul__{prefixe}__{nom}"] = l7._np(valeur)
        self.tableaux[f"directions_nulles__{prefixe}__concentration"] = l7._np(resume.concentration)
        self.tableaux[f"directions_nulles__{prefixe}__compte_part"] = l7._np(resume.compte_part)
        self.tableaux[f"directions_nulles__{prefixe}__egalite_a_la_limite"] = l7._np(resume.egalite)
        self.tableaux[f"directions_nulles__{prefixe}__premiers"] = l7._np(resume.rangs_premiers).astype(np.int32)
        for nom, comptes in resume.familles.items():
            self.tableaux[f"directions_nulles__{prefixe}__famille_{nom}"] = l7._np(comptes)
        s_t = self._lire(t, lentille)
        p = st.p_temoins(s_t, resume)
        self.tableaux[f"temoins__{prefixe}__p"] = p
        self.p_temoins.setdefault((lentille, nul), []).append(p)
        self.comptes.liste_de_vingt(self.couche, lentille, nul, "nulle", resume.m, resume.n_egalites, resume.sans_objet)
        self.comptes.liste_de_vingt(self.couche, lentille, nul, "temoin", s_t.shape[1], int(st.egalites_par_colonne(s_t).sum()),
                                    resume.sans_objet)
        sortie = {"a": a, "resume": resume, "rangs": None, "rangs_t": None}
        if lentille in K2.LENTILLES_R:
            sortie["rangs"] = {"+": resume.rangs_premiers, "-": _rangs(-a, self.ids)}
            sortie["rangs_t"] = _rangs(s_t, self.ids)
            self.tableaux[f"temoins__{prefixe}__premiers"] = l7._np(sortie["rangs_t"]).astype(np.int32)
        return sortie

    def _signes(self, a: torch.Tensor, nuls: dict, lentille: str) -> dict:
        signes = {"+": st.lecture_signe(a, nuls, self.masques, self.ids), "-": st.lecture_signe(-a, nuls, self.masques, self.ids)}
        for t in signes.values():
            e = t["egalite_a_la_limite"]
            self.comptes.liste_de_vingt(self.couche, lentille, st.LISTE_PAR_SCORE, "lue", 1, int(e["par_score"]), e["sans_objet"])
            for nul, egalite in e["par_z"].items():
                self.comptes.liste_de_vingt(self.couche, lentille, f"liste par z sous le {nul}", "lue", 1, int(egalite), e["sans_objet"])
        return signes

    def _vingt(self, scores: torch.Tensor, lentille: str, liste: str) -> dict:
        """Vingt premiers d'un vecteur de scores, aux deux signes, listes départagées et comptées."""
        sortie = {}
        for s, f in (("+", 1.0), ("-", -1.0)):
            h = st.premiers_departages(f * scores, self.ids, K.K_JETONS)
            self.comptes.liste_de_vingt(self.couche, lentille, liste, "lue", 1, int(h["egalite"]), not h["objet"])
            sortie[s] = h
        return sortie

    # -- calcul ----------------------------------------------------------------------------------------------------------------------------
    def calculer(self) -> tuple[dict, list[dict]]:
        r, c, d = self.r, self.couche, self.r.largeur
        u_iso_np = nu.nul_isotrope(self.graines, c, d, r.m)
        u_iso = torch.from_numpy(u_iso_np)
        t_iso = torch.from_numpy(nu.temoins_isotropes(self.graines, c, d, r.n_temoins_isotrope))
        tirage = co.empreinte_tirage(u_iso_np)
        co.exiger_appariement({l: co.empreinte_tirage(u_iso) for l in self.lentilles + list(self.moities)})
        iso = {l: self._nul(u_iso, t_iso, l, K.NUL_ISOTROPE, f"couche{c}__{l}__{K.NUL_ISOTROPE}") for l in self.lentilles}
        iso_moities = {}
        for nom in self.moities:
            a_m = self._lire(u_iso, nom)
            iso_moities[nom] = {"+": _rangs(a_m, self.ids), "-": _rangs(-a_m, self.ids)}
            del a_m
        correlation_nulle = (co.correlation(iso[K.LENTILLE_PUBLIQUE]["a"], iso[K2.LENTILLE_NOTRE_R]["a"]) if self.r_lue else None)
        if self.r_lue:
            self.tableaux[f"correlation__couche{c}__{K.NUL_ISOTROPE}"] = l7._np(correlation_nulle)
            self._calibrer_recouvrement(iso, K.NUL_ISOTROPE)
        directions = []
        for sonde, nom_v, v_np in self.vecteurs:
            self.horloge.controler(f"couche {c}, {sonde.cle}/{nom_v}")
            self.controle_disque()
            ident = f"{sonde.cellule}__{sonde.pli}__{sonde.role}__{nom_v}"
            v = torch.from_numpy(np.asarray(v_np, dtype=np.float32))
            u_s = torch.from_numpy(nu.nul_signes(self.graines, v_np, sonde.cellule, sonde.pli, sonde.role, nom_v, r.m))
            t_s = torch.from_numpy(nu.temoins_signes(self.graines, v_np, c, sonde.cellule, sonde.pli, sonde.role, nom_v,
                                                     r.n_temoins_par_vecteur))
            ligne = {"sonde": sonde.cle, "cellule": sonde.cellule, "pli": sonde.pli, "role": sonde.role, "vecteur": nom_v,
                     "couche": c, "non_calculable": None, "norme": float(np.linalg.norm(np.asarray(v_np, np.float64))),
                     "lectures": {}, "_v": v_np, "_ident": ident,
                     "_ou": {"cellule": sonde.cellule, "pli": sonde.pli, "role": sonde.role, "vecteur": nom_v, "couche": c}}
            signes_nuls = {}
            for lentille in self.lentilles:
                _, indice, empreinte = self.matrices[lentille]
                if lentille == K2.LENTILLE_NOTRE_S:
                    scores, calculable = li.lire_entree(v, self.matrices[lentille][0], self.charge.centres)
                    if not bool(calculable[0]):
                        ligne["lectures"][lentille] = {"indice_matrice": indice, "empreinte_matrice": empreinte,
                                                       "non_calculable": li.MOTIF_NORME_NULLE}
                        continue
                    a, rho = scores[:, 0], None
                else:
                    scores, rho_v = le.lire(v, self.matrices[lentille][0], self.charge.base.gamma, self.charge.base.wu)
                    self.rho[lentille].append(float(rho_v.min()))
                    a, rho = scores[:, 0], float(rho_v[0])
                n_s = self._nul(u_s, t_s, lentille, K.NUL_SIGNES, f"{ident}__{lentille}__{K.NUL_SIGNES}")
                self.tableaux[f"scores__{ident}__{lentille}"] = l7._np(a)
                ligne["lectures"][lentille] = {
                    "indice_matrice": indice, "empreinte_matrice": empreinte,
                    "rapport_epsilon": rho if lentille != K2.LENTILLE_NOTRE_S else SANS_OBJET_RHO,
                    "signes": self._signes(a, {K.NUL_ISOTROPE: (iso[lentille]["a"], iso[lentille]["resume"]),
                                               K.NUL_SIGNES: (n_s["a"], n_s["resume"])}, lentille), "_a": a}
                signes_nuls[lentille] = {"rangs": n_s["rangs"], "rangs_t": n_s["rangs_t"], "a": n_s["a"] if lentille in co.PAIRE_PRINCIPALE else None}
                del n_s
            ligne["_moities"] = {}
            for nom in self.moities:
                a_m = self._lire(v, nom)[:, 0]
                self.tableaux[f"scores__{ident}__{nom}"] = l7._np(a_m)
                ligne["_moities"][nom] = self._vingt(a_m, nom, st.LISTE_PAR_SCORE)
            ligne["entre_lentilles"] = self._entre_lentilles(ligne, iso, signes_nuls, iso_moities, correlation_nulle)
            ligne["poles"] = self._poles(v, {K.NUL_ISOTROPE: u_iso, K.NUL_SIGNES: u_s})
            self._temoin_de_couche(v, ligne, ident)
            if self.s_lue and "signes" in ligne["lectures"][K2.LENTILLE_NOTRE_S]:
                ligne["plongements_seuls"] = self._plongements_seuls(v, ligne, ident)
            directions.append(ligne)
            del u_s, t_s, signes_nuls
        # garde du rapport à ε : lentille publique, lentille des logits, notre R et ses moitiés ; notre S n'est pas concernée
        garde = li.garde_rapport_epsilon({l: min(x) for l, x in self.rho.items() if x})
        if garde["repli"]:
            self._repli(directions)
        resume_couche = {"lentilles": {}, "independance_a_la_norme_tenue": not garde["repli"],
                         "repli_nuls_par_direction": garde["repli"], "garde_du_rapport_a_epsilon": garde,
                         "directions": len(directions), "empreinte_du_tirage_du_nul_isotrope": tirage,
                         "notre_r_lue": self.r_lue, "notre_s_lue": self.s_lue,
                         "calibration_du_recouvrement": {nul: co.calibration_recouvrement(p, r.m)
                                                         for nul, p in sorted(self.p_recouvrement.items()) if p}}
        for lentille in self.lentilles:
            _, indice, empreinte = self.matrices[lentille]
            minimum = min(self.rho[lentille]) if self.rho.get(lentille) else None
            resume_couche["lentilles"][lentille] = {
                "indice_matrice": indice, "empreinte_matrice": empreinte,
                "rapport_epsilon_minimal": minimum if lentille != K2.LENTILLE_NOTRE_S else None,
                "independance_tenue": (SANS_OBJET_RHO if lentille == K2.LENTILLE_NOTRE_S
                                       else None if minimum is None else le.independance_tenue(minimum)),
                "calibration": {nul: au.calibration(p, r.m) for (l, nul), p in sorted(self.p_temoins.items()) if l == lentille and p}}
        resume_couche["moities"] = {nom: {"indice_matrice": i, "empreinte_matrice": e,
                                          "rapport_epsilon_minimal": min(self.rho[nom]) if self.rho.get(nom) else None}
                                    for nom, (_, i, e) in self.moities.items()}
        for nom, motif in ((K2.LENTILLE_NOTRE_R, self.r_lue), (K2.LENTILLE_NOTRE_S, self.s_lue)):
            if not motif:
                lettre = "R" if nom == K2.LENTILLE_NOTRE_R else "S"
                cond = self.conditions[lettre]
                resume_couche.setdefault("lentilles_non_lues", {})[nom] = (
                    cond.motif or cond.couches.get(self.couche, {}).get("motif") or f"notre lentille {lettre} non montée")
        return resume_couche, directions

    # -- comparaisons entre lentilles (« Métrique », point 10) ---------------------------------------------------------------------
    def _calibrer_recouvrement(self, nuls: dict, nul: str) -> None:
        """p_O des témoins d'un nul contre ses M directions nulles (paire principale, signe +), mis en commun par (couche, nul)."""
        a, b = nuls[K.LENTILLE_PUBLIQUE], nuls[K2.LENTILLE_NOTRE_R]
        o_nuls = co.recouvrements_colonnes(a["rangs"]["+"], b["rangs"]["+"])
        self.p_recouvrement.setdefault(nul, []).append(co.p_recouvrement_temoins(a["rangs_t"], b["rangs_t"], o_nuls))

    def _paire(self, paire: tuple, rangs_v: dict, rangs_nuls: dict, signe: str) -> dict:
        c = co.comparer(paire, (rangs_v[paire[0]][signe], rangs_v[paire[1]][signe]),
                        {nul: (x[paire[0]][signe], x[paire[1]][signe]) for nul, x in rangs_nuls.items()})
        for t in c["nuls"].values():
            del t["recouvrements_nuls"]
        return c

    def _entre_lentilles(self, ligne: dict, iso: dict, signes_nuls: dict, iso_moities: dict, correlation_nulle) -> dict:
        if not self.r_lue:
            return {s: {"principale": co.non_calculable(co.MOTIF_LENTILLE_NON_LUE)} for s in ("+", "-")}
        rangs_v = {l: {s: ligne["lectures"][l]["signes"][s]["premiers_par_score"]["rangs_gardes"] for s in ("+", "-")}
                   for l in K2.LENTILLES_R}
        rangs_v |= {nom: {s: h[s]["rangs"].tolist() for s in ("+", "-")} for nom, h in ligne["_moities"].items()}
        nuls = {K.NUL_ISOTROPE: {l: iso[l]["rangs"] for l in K2.LENTILLES_R},
                K.NUL_SIGNES: {l: signes_nuls[l]["rangs"] for l in K2.LENTILLES_R}}
        self._calibrer_recouvrement(signes_nuls, K.NUL_SIGNES)
        a_pub, a_r = ligne["lectures"][K.LENTILLE_PUBLIQUE]["_a"], ligne["lectures"][K2.LENTILLE_NOTRE_R]["_a"]
        correlation = co.resume_correlation(float(co.correlation(a_pub, a_r)[0]), correlation_nulle)
        sortie = {}
        for s in ("+", "-"):
            principale = self._paire(co.PAIRE_PRINCIPALE, rangs_v, nuls, s)
            moities = self._paire(co.PAIRE_MOITIES, rangs_v, {K.NUL_ISOTROPE: iso_moities}, s)
            sortie[s] = {"principale": principale, "notre_r_et_logits": self._paire(co.PAIRE_LOGITS, rangs_v, nuls, s),
                         "moities": moities, "correlation": dict(correlation),
                         "deux_recouvrements": co.comparer_les_deux_recouvrements(principale["recouvrement"], moities["recouvrement"])}
        return sortie

    # -- pôles, témoin de couche, plongements seuls -------------------------------------------------------------------------------------
    def _poles(self, v: torch.Tensor, nuls: dict) -> dict:
        """Les dix pôles (ordre total du point 7), lus par la lentille publique et par notre R (dix premiers jetons chacun) ;
        jetons communs par pôle ; égalités à la limite comptées."""
        base = self.charge.base
        pa = st.poles_alignes(v, self.w_down, nuls)
        self.comptes.poles_par_cosinus(self.couche, "lue", 1, int(pa["egalite_a_la_limite"]), pa["sans_objet"])
        for p in pa["poles"]:
            colonne = self.w_down[:, p["neurone"]] * (1.0 if p["signe"] == "+" else -1.0)
            for lentille, cle in ((K.LENTILLE_PUBLIQUE, "lecture_publique"), (K2.LENTILLE_NOTRE_R, "lecture_notre_r")):
                if lentille not in self.matrices:
                    continue
                scores, _ = le.lire(colonne, self.matrices[lentille][0], base.gamma, base.wu)
                h = st.premiers_jetons_d_un_pole(scores[:, 0], self.ids)
                self.comptes.jetons_d_un_pole(self.couche, lentille, 1, int(h["egalite_a_la_limite"]), h["sans_objet"])
                p[cle] = {"ids": h["ids"], "chaines_echappees": [l7._echappe(base.chaines[i]) for i in h["rangs_gardes"]]}
            if "lecture_notre_r" in p:
                p["jetons_communs_entre_les_deux_lentilles_r"] = st.jetons_communs(p["lecture_publique"]["ids"], p["lecture_notre_r"]["ids"])
        maxima = pa.pop("maxima_nuls")
        return pa | {"_maxima": maxima}

    def _temoin_de_couche(self, v: torch.Tensor, ligne: dict, ident: str) -> None:
        """Jetons communs entre la lecture de v à sa couche et à chacune des deux autres couches, pour la lentille publique,
        notre R et notre S (leurs matrices des trois couches sont décodées) ; une lentille non lue à l'autre couche : écrit."""
        base, nos = self.charge.base, self.charge.nos
        for lentille in self.lentilles:
            lecture = ligne["lectures"][lentille]
            if lentille == K.LENTILLE_LOGITS or "_a" not in lecture:
                continue
            ici = self._vingt(lecture["_a"], lentille, f"témoin de couche, lecture à la couche {self.couche}")
            sortie = {}
            for autre in sorted(self.r.couches):
                if autre == self.couche:
                    continue
                if lentille == K.LENTILLE_PUBLIQUE:
                    b = le.lire(v, base.publique.matrice(autre)[0], base.gamma, base.wu)[0][:, 0]
                else:
                    lettre = "R" if lentille == K2.LENTILLE_NOTRE_R else "S"
                    if not self.conditions[lettre].lue_a(autre):
                        sortie[str(autre)] = {"non_calculable": co.MOTIF_LENTILLE_NON_LUE}
                        continue
                    m = _t(nos[lettre].matrice_verifiee(autre)[0])
                    if lettre == "R":
                        b = le.lire(v, m, base.gamma, base.wu)[0][:, 0]
                    else:
                        scores, calculable = li.lire_entree(v, m, self.charge.centres)
                        if not bool(calculable[0]):
                            sortie[str(autre)] = {"non_calculable": li.MOTIF_NORME_NULLE}
                            continue
                        b = scores[:, 0]
                self.tableaux[f"scores_temoin_de_couche__{ident}__{lentille}__c{autre}"] = l7._np(b)
                la_bas = self._vingt(b, lentille, f"témoin de couche, lecture à la couche {autre}")
                sortie[str(autre)] = {s: st.jetons_communs(ici[s]["rangs"].tolist(), la_bas[s]["rangs"].tolist()) for s in ("+", "-")}
            lecture["temoin_de_couche"] = sortie

    def _plongements_seuls(self, v: torch.Tensor, ligne: dict, ident: str) -> dict:
        """Référence « plongements seuls » : vingt premiers jetons et nombre de jetons communs avec les vingt premiers de notre
        S ; aucun nul, aucun p, aucun libellé."""
        scores, calculable = li.lire_plongements_seuls(v, self.charge.centres)
        if not bool(calculable[0]):
            return {"non_calculable": li.MOTIF_NORME_NULLE}
        self.tableaux[f"scores__{ident}__{K2.PLONGEMENTS_SEULS}"] = l7._np(scores[:, 0])
        h = self._vingt(scores[:, 0], K2.PLONGEMENTS_SEULS, st.LISTE_PAR_SCORE)
        par_s = ligne["lectures"][K2.LENTILLE_NOTRE_S]["signes"]
        return {s: {"ids": h[s]["ids"].tolist(), "scores": [float(x) for x in h[s]["valeurs"]],
                    "jetons_communs_avec_notre_s": st.jetons_communs(h[s]["ids"].tolist(), par_s[s]["premiers_par_score"]["ids"])}
                for s in ("+", "-")}

    # -- repli de la garde du rapport à ε -------------------------------------------------------------------------------------------------
    def _repli(self, directions: list[dict]) -> None:
        """Indépendance à la norme non tenue pour l'une des lentilles R ou une moitié : le nul isotrope est refait par vecteur
        (mêmes clés que la première passe) **pour la lentille publique, la lentille des logits et notre R** ; les lectures
        faites avec le nul partagé restent en table, « remplacées » ; le recouvrement des moitiés et son p sont « non
        calculables » à cette couche. Notre S garde le nul partagé."""
        r, c, nul = self.r, self.couche, K.NUL_ISOTROPE_PAR_DIRECTION
        refaites = [l for l in K2.LENTILLES_R if l in self.lentilles]
        for ligne in directions:
            v_np = ligne["_v"]
            arg = (ligne["cellule"], ligne["pli"], ligne["role"], ligne["vecteur"])
            self.horloge.controler(f"couche {c}, repli {ligne['sonde']}/{ligne['vecteur']}")
            u_d = torch.from_numpy(nu.nul_isotrope_par_direction(self.graines, v_np, *arg, r.m))
            t_d = torch.from_numpy(nu.temoins_isotropes_par_direction(self.graines, v_np, c, *arg, r.n_temoins_par_vecteur))
            par_direction = {}
            for lentille in refaites:
                n_d = self._nul(u_d, t_d, lentille, nul, f"{ligne['_ident']}__{lentille}__{nul}")
                lecture = ligne["lectures"][lentille]
                neuf = self._signes(lecture["_a"], {nul: (n_d["a"], n_d["resume"])}, lentille)
                for s in ("+", "-"):
                    lecture["signes"][s]["nuls"][K.NUL_ISOTROPE]["remplacee"] = True
                    lecture["signes"][s]["nuls"][nul] = neuf[s]["nuls"][nul]
                par_direction[lentille] = {"rangs": n_d["rangs"], "rangs_t": n_d["rangs_t"]}
                del n_d
            if self.r_lue:
                self._calibrer_recouvrement(par_direction, nul)
                for s in ("+", "-"):
                    e = ligne["entre_lentilles"][s]
                    for cle, paire in (("principale", co.PAIRE_PRINCIPALE), ("notre_r_et_logits", co.PAIRE_LOGITS)):
                        o_nuls = co.recouvrements_colonnes(par_direction[paire[0]]["rangs"][s], par_direction[paire[1]]["rangs"][s])
                        e[cle]["nuls"][K.NUL_ISOTROPE]["remplacee"] = True
                        e[cle]["nuls"][nul] = {"p": co.p_recouvrement(o_nuls, e[cle]["recouvrement"]), "mediane": co.mediane(o_nuls),
                                               "m": int(o_nuls.numel())}
                    e["moities"] = co.non_calculable(co.MOTIF_NUL_REFAIT) | {"recouvrement": e["moities"]["recouvrement"]}
            v = torch.from_numpy(np.asarray(v_np, dtype=np.float32))
            pa = st.poles_alignes(v, self.w_down, {nul: u_d})
            poles = ligne["poles"]
            poles["p"][K.NUL_ISOTROPE + "_remplacee"] = poles["p"].pop(K.NUL_ISOTROPE)
            poles["p"][nul] = pa["p"][nul]
            poles["_maxima"][nul] = pa["maxima_nuls"][nul]
            for ancien, neuf in zip(poles["poles"], pa["poles"]):
                ancien["rang_parmi_maxima_nuls"] |= neuf["rang_parmi_maxima_nuls"]


# ========================================================================================================================================
# Libellés, comparaisons, comptes, audit
# ========================================================================================================================================
def _nul_isotrope_en_vigueur(repli: bool, lentille: str) -> str:
    return K.NUL_ISOTROPE_PAR_DIRECTION if repli and lentille in K2.LENTILLES_R else K.NUL_ISOTROPE


def _etiqueter(directions: list[dict], couches: dict, chaines: list, ids_gardes: np.ndarray) -> list[dict]:
    """Libellés (« Seuil ») de chaque lecture, de sa part, de ses familles et de ses pôles, pour toute lentille ; une
    calibration hors de ses bornes rend « non calculables » les tables de cette couche, de cette lentille et de ce nul. Aucune
    borne p_bas ou p_haut : la valeur p est celle que donne le départage. Rend les lignes de lecture pour les déclencheurs."""
    rang_de = {int(i): n for n, i in enumerate(ids_gardes.tolist())}
    lignes = []
    for d in directions:
        info = couches[str(d["couche"])]
        repli = info["repli_nuls_par_direction"]
        for lentille, lecture in d["lectures"].items():
            if "signes" not in lecture:
                continue
            nul_iso = _nul_isotrope_en_vigueur(repli, lentille)
            cal = info["lentilles"][lentille]["calibration"]
            hors = [nul for nul in (nul_iso, K.NUL_SIGNES) if not cal[nul]["tenue"]]
            for signe, t in lecture["signes"].items():
                t["premiers_par_score"]["chaines_echappees"] = [l7._echappe(chaines[rang_de[i]]) for i in t["premiers_par_score"]["ids"]]
                for nul_table in t["nuls"].values():
                    if "premiers_par_z" in nul_table:
                        nul_table["premiers_par_z"]["chaines_echappees"] = [l7._echappe(chaines[rang_de[i]])
                                                                          for i in nul_table["premiers_par_z"]["ids"]]
                for nul in hors:
                    t["nuls"][nul] = {"non_calculable": au.MOTIF_CALIBRATION}
                if hors:
                    t |= {"libelle": None, "libelle_part": None, "non_calculable": au.MOTIF_CALIBRATION, "nul_isotrope_en_vigueur": nul_iso}
                    for f in t["familles"].values():
                        f["sur_representee"] = None
                else:
                    i, s = t["nuls"][nul_iso], t["nuls"][K.NUL_SIGNES]
                    t |= {"libelle": st.libelle(i["p_concentration"], s["p_concentration"]),
                          "libelle_part": st.libelle(i["p_part"], s["p_part"]), "nul_isotrope_en_vigueur": nul_iso}
                    for nom, f in t["familles"].items():
                        f["sur_representee"] = st.sur_representee(i["familles"][nom]["p"], s["familles"][nom]["p"])
                lignes.append({"sonde": d["sonde"], "role": d["role"], "vecteur": d["vecteur"], "signe": signe, "couche": d["couche"],
                               "lentille": lentille, "libelle": t["libelle"], "ids": t["premiers_par_score"]["ids"]})
        p = d["poles"]["p"]
        nul_poles = _nul_isotrope_en_vigueur(repli, K.LENTILLE_PUBLIQUE)
        d["poles"]["libelle"] = st.libelle(p[nul_poles], p[K.NUL_SIGNES])
        d["poles"]["nul_isotrope_en_vigueur"] = nul_poles
        d["accord_lentilles"] = {}
        for nom, paire in (("publique_et_logits", (K.LENTILLE_PUBLIQUE, K.LENTILLE_LOGITS)), ("notre_r_et_logits", (K2.LENTILLE_NOTRE_R, K.LENTILLE_LOGITS))):
            if all("signes" in d["lectures"].get(l, {}) for l in paire):
                d["accord_lentilles"][nom] = {s: st.jetons_communs(*(d["lectures"][l]["signes"][s]["premiers_par_score"]["ids"] for l in paire))
                                              for s in ("+", "-")}
    return lignes


def _comparaisons(directions: list[dict]) -> list[dict]:
    """Comparaisons appariées, descriptives (« Métrique », point 8) : celles de la première passe (`lanceur_v7._comparaisons`,
    mêmes paires), les jetons communs étant rendus pour **chaque lentille** qui lit les deux directions (lentille publique,
    lentille des logits, notre R, notre S)."""
    par_cle = {(d["cellule"], d["pli"], d["role"], d["vecteur"]): d for d in directions}
    sortie = l7._comparaisons(directions)
    for ligne in sortie:
        if ligne.get("cosinus") is None:
            continue
        da, db = par_cle[tuple(ligne["a"].split("/"))], par_cle[tuple(ligne["b"].split("/"))]
        for lentille in (K2.LENTILLE_NOTRE_R, K2.LENTILLE_NOTRE_S):
            if all("signes" in d["lectures"].get(lentille, {}) for d in (da, db)):
                ligne["jetons_communs"][lentille] = {
                    s: st.jetons_communs(da["lectures"][lentille]["signes"][s]["premiers_par_score"]["ids"],
                                         db["lectures"][lentille]["signes"][s]["premiers_par_score"]["ids"]) for s in ("+", "-")}
    return sortie


def _libeller_les_comparaisons(directions: list[dict], couches: dict, reproduction: dict) -> list[dict]:
    """Libellé de la paire principale, par direction et signe ; « non calculable » : calibration du recouvrement hors borne,
    lentille non lue à la couche, calibration d'une des deux lectures, ou libellé de la lentille publique différent d'une
    passe à l'autre. Rend les lignes de recouvrement pour les déclencheurs."""
    lignes = []
    for d in directions:
        info = couches[str(d["couche"])]
        nul_iso = _nul_isotrope_en_vigueur(info["repli_nuls_par_direction"], K2.LENTILLE_NOTRE_R)
        for signe, e in d["entre_lentilles"].items():
            p = e["principale"]
            if p.get("libelle") == co.NON_CALCULABLE:
                continue
            libelles = tuple(d["lectures"][l]["signes"][signe]["libelle"] for l in co.PAIRE_PRINCIPALE)
            calibration = info["calibration_du_recouvrement"]
            if rp.libelle_public_different(reproduction, d["sonde"], d["vecteur"], signe):
                p |= co.non_calculable(co.MOTIF_LIBELLE_DIFFERENT)
            elif not all(calibration[nul]["tenue"] for nul in (nul_iso, K.NUL_SIGNES)):
                p |= co.non_calculable(co.MOTIF_CALIBRATION_RECOUVREMENT)
            elif None in libelles:
                p |= {"libelle": co.NON_CALCULABLE, "motif": MOTIF_CALIBRATION_D_UNE_LECTURE}
            else:
                p_iso, p_signes = p["nuls"][nul_iso]["p"], p["nuls"][K.NUL_SIGNES]["p"]
                p["libelle_du_recouvrement"] = co.libelle_recouvrement(p_iso, p_signes)
                p |= co.libelle_comparaison(libelles[0], libelles[1], p["libelle_du_recouvrement"])
                p |= {"libelles": list(libelles), "nul_isotrope_en_vigueur": nul_iso}
            moities = e["moities"].get("recouvrement") if e["moities"].get("libelle") != co.NON_CALCULABLE else None
            lignes.append({"sonde": d["sonde"], "vecteur": d["vecteur"], "signe": signe, "couche": d["couche"],
                           "publique_et_notre_r": p["recouvrement"], "moities": moities,
                           "calculable": p.get("libelle") != co.NON_CALCULABLE})
    return lignes


def _comptes(directions: list[dict]) -> dict:
    """Comptes de libellés, chacun avec son attendu par le seul hasard (« Seuil »), et nombre total de lectures."""
    lectures = [t for d in directions for l in d["lectures"].values() if "signes" in l for t in l["signes"].values()]
    n = len(lectures)

    def compte(valeurs) -> dict:
        c: dict = {}
        for v in valeurs:
            c[str(v)] = c.get(str(v), 0) + 1
        return c
    sur = sum(1 for t in lectures for f in t["familles"].values() if f.get("sur_representee"))
    principales = [e["principale"] for d in directions for e in d["entre_lentilles"].values() if "recouvrement" in e["principale"]]
    return {"nombre_total_de_lectures": n,
            "concentration": {"comptes": compte(t["libelle"] for t in lectures), "attendu_par_hasard_au_plus": n * K.P_ISO_CONCENTREE},
            "part_au_dessus_du_nul": {"comptes": compte(t["libelle_part"] for t in lectures), "attendu_par_hasard_au_plus": n * K.P_ISO_CONCENTREE},
            "poles": {"comptes": compte(d["poles"]["libelle"] for d in directions), "nombre": len(directions),
                      "attendu_par_hasard_au_plus": len(directions) * K.P_ISO_CONCENTREE},
            "familles_sur_representees": {"compte": sur, "attendu_par_hasard_au_plus": n * 2 * K.P_FAMILLE},
            "comparaisons_entre_lentilles": {
                "nombre_de_lectures_comparees": len(principales), "libelles": compte(p.get("libelle") for p in principales),
                "recouvrements": compte(p.get("libelle_du_recouvrement") for p in principales),
                "attendu_par_hasard_au_plus_pour_au_dela_des_deux_nuls_et_lecture_commune": len(principales) * K.P_ISO_CONCENTREE},
            "note": "attendu par hasard : une espérance ; les nuls partagés corrèlent les p entre directions d'une couche et entre lentilles"}


def _audit(entrees, directions: list[dict], couches: dict, charge: Charge, conditions: dict, graines: nu.Graines, fiche: dict,
           reproduction: dict) -> dict:
    """Audit de symétrie de la seconde passe : celui de la première passe (`lanceur_v7._audit`, tel quel), plus la fiche de
    rangement et le verdict d'identité, les empreintes des matrices contre le montage, `meta`, l'orientation de K, plongements
    contre lignes de sortie, deux directions relues par notre R et par notre S sur un chemin indépendant en double précision.
    Issue écrite en réserve ; aucune table ne change."""
    base = charge.base
    audit = l7._audit(entrees, directions, couches, base, graines, charge.etat)
    relues = []
    if directions:
        ordre = graines.rng(nu.cle_essai("audit-chemin-independant")).permutation(len(directions))[:2]
        for i in sorted(int(x) for x in ordre):
            d = directions[i]
            ligne = {"direction": f"{d['sonde']}/{d['vecteur']}", "couche": d["couche"]}
            if "_a" in d["lectures"].get(K2.LENTILLE_NOTRE_R, {}):
                relue = au.relire_par_chemin_independant(d["_v"], charge.nos["R"].matrice(d["couche"]).astype(np.float64),
                                                        l7._np(base.gamma), l7._np(base.wu))
                ligne["notre_r"] = au.comparer_relecture(l7._np(d["lectures"][K2.LENTILLE_NOTRE_R]["_a"]), relue)
            if "_a" in d["lectures"].get(K2.LENTILLE_NOTRE_S, {}):
                k = charge.nos["S"].matrice(d["couche"])
                scores = li.relire_par_chemin_independant(d["_v"], k, l7._np(charge.plongements))[0]
                lue = l7._np(d["lectures"][K2.LENTILLE_NOTRE_S]["_a"])
                ordre_lu, ordre_relu = np.argsort(-lue, kind="stable")[:K.K_JETONS], np.argsort(-scores, kind="stable")[:K.K_JETONS]
                a_droite, _ = li.lire_entree(d["_v"], _t(k.T.copy()), charge.centres)
                ligne["notre_s"] = {"jetons_communs": len(set(ordre_lu.tolist()) & set(ordre_relu.tolist())),
                                    "ecart_maximal": float(np.max(np.abs(lue - scores))),
                                    "orientation_de_k": {"convention": "covecteur à gauche (c @ K)",
                                                         "jetons_communs_avec_k_a_droite": len(set(ordre_lu.tolist()) & set(
                                                             np.argsort(-l7._np(a_droite[:, 0]), kind="stable")[:K.K_JETONS].tolist()))}}
            relues.append(ligne)
    return audit | {"contenu": list(au.CONTENU_AUDIT_V2),
                    "fiche_de_rangement": dict(fiche["_ligne"]),
                    "verdicts_d_identite": {l: conditions[l].verdict for l in K2.NOS_LENTILLES},
                    "empreintes_des_matrices_egales_a_celles_du_montage": True,      # contrôlé à chaque lecture (`matrice_verifiee`)
                    "empreintes_des_matrices_lues": {l: dict(x.empreintes_montage) for l, x in charge.nos.items()},
                    "meta": {l: (charge.etat["nos_lentilles"][l]["meta"] or {}).get("lens") for l in charge.nos},
                    "plongements_et_lignes_de_sortie_egaux": charge.lies,
                    "directions_relues_par_nos_lentilles_sur_un_chemin_independant": relues,
                    "reproduction": {"etat": reproduction["etat"], "versions": l7._versions(), "modules_differents": list(MODULES_DIFFERENTS)}}


# ========================================================================================================================================
# Canal des messages d'arrêt et enveloppe du calcul
# ========================================================================================================================================
ARRETS_CLOISONNES = l7.ARRETS_CLOISONNES
exiger_aucun_fichier_d_arret = l7.exiger_aucun_fichier_d_arret
chemin_du_fichier_d_arret = l7.chemin_du_fichier_d_arret


def ligne_affichee(arret: Arret) -> str:
    """**La seule fonction qui décide ce qui va à la sortie d'erreur.** Arrêt cloisonné : des mots fixes, le nom de l'arrêt
    et le chemin du fichier d'arrêt, jamais le message (il est dans le seul `arret.json`). Tout autre arrêt : son message."""
    if l7.nom_d_arret_cloisonne(arret) is not None:
        return l7.ligne_d_arret_cloisonne(arret)
    return f"ARRÊT : {arret}"


def calculer(ctx, racine_entrees: Path, registre_bbis: Path, racine_premiere_passe: Path | None = None, nettoyage: bool = True) -> dict:
    """Enveloppe du calcul, celle de `lanceur_v7` : avant tout, la garde du fichier d'arrêt déjà présent ; à tout arrêt après
    le départ du calcul, ce qui existe est versé (tableaux écrits, fermés, scellés, marqués « interrompus, non lus » ; dossier
    de travail inventorié), rien n'est supprimé, puis l'arrêt est relevé tel quel. Un arrêt cloisonné est versé par
    `lanceur_v7.verser_arret_cloisonne` ; son message ne sort que dans `arret.json`."""
    exiger_aucun_fichier_d_arret(ctx)
    tableaux: dict = {}
    etat = {"parti": False}
    try:
        return _calculer(ctx, racine_entrees, registre_bbis, racine_premiere_passe, nettoyage, tableaux, etat)
    except Arret as arret:
        try:
            cloisonne = l7.nom_d_arret_cloisonne(arret) is not None
            if cloisonne:
                l7.verser_arret_cloisonne(ctx, arret, tableaux, etat["parti"])
        except BaseException as e:          # interruption entre l'arrêt et son relevé : sa trace ne porte pas le message
            raise e from None
        if cloisonne:
            raise
        if not etat["parti"]:
            raise                           # refus avant le départ : rien n'est versé
        dest = ctx.sortie / "versement" / ctx.run / "calcul-interrompu"
        try:
            morceaux = l7.ecrire_morceaux(tableaux, dest / "lectures-interrompues-non-lues") if tableaux else []
            l7._ecrire_ferme(dest / "arret.json", {"run": ctx.run, "motif": str(arret), "morceaux": morceaux,
                                                   "travail": l7.verser_travail(ctx.travail, ctx.sortie, ctx.run, "arret")})
        except Arret as e:
            raise Arret(f"{arret} ; versement à l'arrêt en échec ({e}) : rien n'est supprimé") from None
        raise


def _premiere_passe_en_vigueur(au_montage: str, au_calcul: str) -> tuple[str, str | None]:
    """L'état de la première passe est celui lu **au montage de la seconde**. Une passe lancée et non achevée au montage n'est
    pas reproduite, même si elle s'achève ensuite. Une passe jamais lancée au montage et lancée depuis n'est pas remplacée."""
    if au_montage == nl.PREMIERE_PASSE_JAMAIS_LANCEE and au_calcul != nl.PREMIERE_PASSE_JAMAIS_LANCEE:
        return nl.PREMIERE_PASSE_NON_ACHEVEE, "première passe lancée depuis le montage de la seconde : elle n'est pas remplacée"
    if au_montage == nl.PREMIERE_PASSE_NON_ACHEVEE and au_calcul == nl.PREMIERE_PASSE_ACHEVEE:
        return au_montage, ("première passe achevée depuis le montage de la seconde : ses phrases de la lentille publique et de la "
                            "lentille des logits sont celles de la première passe ; la reproduction n'est pas faite")
    return au_montage, None


def _ligne_de_la_seconde_course(fiche: dict, course: str, etat_registre) -> str | None:
    """La ligne d'ensemble de la lecture de la seconde course, recopiée de la fiche, quand cette lecture est inscrite et que la
    seconde course a été menée en entier : les renvois aux réserves tirées du verdict de la tranche y renvoient."""
    seconde = fiche.get("lecture_seconde_course")
    if (course == nl.COURSE_REJOUEE and etat_registre.presentes(K2.CLE_LECTURE_SECONDE_COURSE) and isinstance(seconde, dict)
            and isinstance(seconde.get("ligne_d_ensemble"), str)):
        return ph.exiger_sans_paraphrase_interdite(seconde["ligne_d_ensemble"])
    return None


def _calculer(ctx, racine_entrees: Path, registre_bbis: Path, racine_premiere_passe, nettoyage: bool, tableaux: dict, etat: dict) -> dict:
    """Plan, point 6, calcul de la seconde passe ; tout est écrit dans des fichiers fermés ; puis nettoyage (point 10)."""
    r = ctx.reglages
    fiche_code = exiger_fiche_code(ctx.racine_depot, ctx.registre_propre)
    etat_registre, issue, fiche, conditions = _lecture(ctx, ctx.registre_propre)
    en.exiger_scores_et_verdict(registre_bbis)
    if not (ctx.travail / MARQUE).is_file():
        raise Arret("dossier de travail monté absent : rien ne part")
    rapport_montage = ctx.sortie / "diag" / ctx.run / NOM_MONTAGE
    if not rapport_montage.is_file():
        raise Arret("rapport du montage de la seconde passe absent du dossier de sortie : rien ne part")
    etat["parti"] = True
    horloge = _horloge(ctx)
    horloge.controler("départ du calcul de la seconde passe")

    def controle_disque() -> None:
        l7.exiger_disque(ctx.travail, r.disque_calcul, "pendant le calcul", ctx.mesure_disque)
    controle_disque()
    for nom in (ctx.sortie / "diag" / ctx.run / NOM_TABLES, ctx.sortie / "runs" / ctx.run / "manifeste.json",
                ctx.sortie / "diag" / ctx.run / NOM_ENTREES):
        if nom.exists():
            raise Arret(f"{nom} existe déjà (R12)")
    charge = charger_montage(ctx)
    for lettre in K2.NOS_LENTILLES:
        if conditions[lettre].lue and lettre not in charge.nos:
            raise Arret(f"notre lentille {lettre} est lue selon le registre et la fiche, et n'a pas été montée : montage à refaire ; "
                        "rien ne part")
        if lettre in charge.nos and charge.etat["fiche_de_rangement"]["sha256"] != fiche["_ligne"]["sha256"]:
            raise Arret("fiche de rangement différente de celle du montage : montage à refaire ; rien ne part")
    premiere, note_premiere = _premiere_passe_en_vigueur(charge.etat["premiere_passe_au_montage"], etat_registre.premiere_passe)
    entrees = en.ouvrir_entrees(racine_entrees, registre_bbis, ctx.registre_propre, r.largeur)
    tables_un, scores_un = None, None
    if premiere == nl.PREMIERE_PASSE_ACHEVEE:
        if racine_premiere_passe is None:
            raise Arret("tables de la première passe : dossier non donné alors que TABLES-LENTILLES-BBIS est inscrite : rien ne part")
        tables_un = rp.ouvrir_tables_premiere_passe(racine_premiere_passe, ctx.registre_propre, etat_registre)
        memes_entrees = rp.exiger_memes_entrees(tables_un, entrees.sha256_e1, entrees.sha256_e2)
        scores_un = rp.scores_premiere_passe(racine_premiere_passe, tables_un)
    graines = nu.Graines()
    masques = st.masques_familles(charge.base.chaines)
    comptes = st.ComptesEgalites()
    tableaux["ids_gardes"] = charge.base.ids_gardes
    sondes_table, par_couche, non_calculables = [], {}, []
    for s in entrees.sondes:
        sondes_table.append({"cle": s.cle, "cellule": s.cellule, "pli": s.pli, "role": s.role, "lue": s.lue,
                             "motif": None if s.lue else f"non lue : {s.motif}", "famille": s.famille, "couche": s.couche,
                             "agregation": s.agregation, "empreinte": s.empreinte, "nom_en_clair": ph.nom_sonde(s.cellule, s.pli, s.role, "w")})
        for nom_v, v in s.vecteurs().items():
            motif = st.vecteur_calculable(v)
            if motif:
                non_calculables.append({"sonde": s.cle, "cellule": s.cellule, "pli": s.pli, "role": s.role, "vecteur": nom_v,
                                        "couche": s.couche, "non_calculable": motif})
            else:
                par_couche.setdefault(s.couche, []).append((s, nom_v, v))
    couches, directions = {}, []
    for couche in sorted(par_couche):
        calcul = _Couche(couche, par_couche[couche], charge, conditions, graines, r, masques, tableaux, comptes, horloge, controle_disque)
        couches[str(couche)], d = calcul.calculer()
        for ligne in d:
            for nom, m in ligne["poles"]["_maxima"].items():
                tableaux[f"poles__{ligne['_ident']}__maxima__{nom}"] = l7._np(m)
        directions += d
        horloge.controler(f"couche {couche}")
    lignes = _etiqueter(directions, couches, charge.base.chaines, charge.base.ids_gardes)
    comparaisons = _comparaisons(directions)
    # reproduction de la première passe (plan, point 11)
    if tables_un is not None:
        scores_deux = {nom: a for nom, a in tableaux.items() if nom.startswith("scores__") and nom.rsplit("__", 1)[1] in K.LENTILLES}
        reproduction = rp.comparer(tables_un, {"directions": l7._retirer_prives(directions)}, scores_un, scores_deux)
        reproduction |= {"entrees": memes_entrees, "tables_de_la_premiere_passe": dict(tables_un["_ligne"])}
    else:
        reproduction = rp.sans_comparaison(premiere)
    reproduction |= {"premiere_passe_au_montage": charge.etat["premiere_passe_au_montage"],
                     "premiere_passe_au_calcul": etat_registre.premiere_passe, "note": note_premiere,
                     "code_de_lecture_different_de_la_premiere_passe": list(MODULES_DIFFERENTS)}
    recouvrements = _libeller_les_comparaisons(directions, couches, reproduction)
    seuls = [{"sonde": d["sonde"], "vecteur": d["vecteur"], "signe": s, "ids": t["ids"]} for d in directions
             for s, t in (d.get("plongements_seuls") or {}).items() if isinstance(t, dict) and "ids" in t]
    premiere_passe = au.declencheurs_premiere_passe([l for l in lignes if l["lentille"] in K.LENTILLES],
                                                    [c for c in comparaisons if c.get("cosinus") is not None])
    seconde_passe = au.declencheurs(lignes, [x for x in recouvrements if x["calculable"]], seuls, reproduction)
    declencheurs = {"premiere_passe": premiere_passe, "seconde_passe": seconde_passe,
                    "audit_a_jouer": bool(premiere_passe["audit_a_jouer"] or seconde_passe["audit_a_jouer"])}
    audit = (_audit(entrees, directions, couches, charge, conditions, graines, fiche, reproduction)
             if declencheurs["audit_a_jouer"] else None)
    non_tenues = [(int(c), l) for c, info in couches.items() for l, v in info["lentilles"].items()
                  if info["repli_nuls_par_direction"] and v.get("independance_tenue") is False]
    tete = ph.tete(conditions, fiche, conditions["course"], bool(etat_registre.presentes(K2.CLE_LECTURE_SECONDE_COURSE)), reproduction,
                   MODULES_DIFFERENTS, issue["phrases_de_tete"], non_tenues)
    morceaux = l7.ecrire_morceaux(tableaux, ctx.sortie / "donnees" / ctx.run / PREFIXE_LECTURES)
    tables = {
        "run": ctx.run, "texte": dict(TEXTE), "addendum": dict(ADDENDUM), "passe": "seconde", "tete": tete,
        "entrees": {"course": entrees.course.run, "e1_sha256": entrees.sha256_e1, "e2_sha256": entrees.sha256_e2,
                    "empreinte_de_l_extrait_de_la_liste_blanche": entrees.empreinte_extrait, "extrait": entrees.extrait,
                    "entrees_decodees": list(entrees.entrees_decodees), "entrees_jamais_decodees": list(entrees.entrees_non_decodees)},
        "nos_lentilles": {"course_du_reajustement": conditions["course"],
                          "critere_d_identite": {"chemin": K2.CRITERE_IDENTITE, "sha256": K2.EMPREINTE_CRITERE_IDENTITE,
                                                 "version": K2.VERSION_CRITERE_IDENTITE},
                          "fiche_de_rangement": dict(fiche["_ligne"]), "issue_des_noeuds": issue,
                          "ligne_de_la_lecture_de_la_seconde_course": _ligne_de_la_seconde_course(fiche, conditions["course"], etat_registre),
                          "condition_de_lecture": {l: conditions[l].table() for l in K2.NOS_LENTILLES}},
        "sondes": sondes_table, "couches": couches, "directions": l7._retirer_prives(directions) + non_calculables,
        "comparaisons": comparaisons, "comptes_de_libelles": _comptes(directions), "egalites_a_la_limite": comptes.table(),
        "reproduction_de_la_premiere_passe": reproduction,
        "independance_a_la_norme_non_tenue": [{"couche": c, "lentille": l} for c, l in sorted(non_tenues)],
        "declencheurs_d_audit": declencheurs, "audit": audit, "fichiers_des_lectures": morceaux,
        "duree_cumulee_s": horloge.ecoule(),
        "conventions": {"ecart_type": "population (diviseur M)", "quantile": "0,99, interpolation linéaire",
                        "rang_empirique": "1 + nombre de scores nuls du même jeton strictement plus grands",
                        "p": "(1 + #{j : statistique(u_j) ≥ statistique(v)}) / (M + 1)", "m": r.m,
                        "statistique_des_directions_nulles": l7.STATISTIQUE_NULLE,
                        "comparaison_des_concentrations": l7.COMPARAISON_CONCENTRATIONS,
                        "regle_de_departage": st.REGLE_DEPARTAGE, "regle_des_poles": st.REGLE_POLES,
                        "loi_des_bornes_de_calibration": l7.LOI_CALIBRATION,
                        "calibration_du_recouvrement": "borne haute seule ; borne basse sans objet",
                        "porte_une_phrase": list(ph.PORTE_UNE_PHRASE), "reste_en_table": list(ph.RESTE_EN_TABLE)}}
    sha_tables = l7._ecrire_ferme(ctx.sortie / "diag" / ctx.run / NOM_TABLES, tables)
    chemins = en.chemins_permis(entrees.course.run)
    sha_entrees = l7._ecrire_ferme(ctx.sortie / "diag" / ctx.run / NOM_ENTREES, {
        "run": ctx.run, "course": entrees.course.run, "e1": {"chemin": chemins["e1"], "sha256": entrees.sha256_e1},
        "e2": {"chemin": chemins["e2"], "sha256": entrees.sha256_e2},
        "empreinte_de_l_extrait_de_la_liste_blanche": entrees.empreinte_extrait})
    montage = {"chemin": f"diag/{ctx.run}/{NOM_MONTAGE}", "sha256": verifier(rapport_montage)}
    config = {"texte": K2.EMPREINTE_TEXTE_V2, "addendum": K2.EMPREINTE_ADDENDUM, "m": r.m, "n_temoins_isotrope": r.n_temoins_isotrope,
              "n_temoins_par_vecteur": r.n_temoins_par_vecteur, "couches": list(r.couches), "largeur": r.largeur,
              "epsilon": K.EPSILON, "course_bbis": entrees.course.run, "regle_de_departage": st.REGLE_DEPARTAGE}
    nos = {l: {"revision": fiche["lentilles"][l].get("revision"), "sha256": charge.etat["nos_lentilles"][l]["sha256"],
               "empreintes_des_matrices_lues": charge.etat["nos_lentilles"][l]["empreintes_des_matrices_lues"]} for l in charge.nos}
    manifeste = {"run_id": ctx.run, "cree_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "commit": l7._commit(ctx.racine_depot), "code": empreintes_du_code(), "fiche_code": fiche_code, "config": config,
                 "rapport_du_montage": montage, "entrees_sha256": sha_entrees, "nos_lentilles": nos,
                 "config_sha256": hashlib.sha256(mf.config_canonique(config)).hexdigest(), "versions": l7._versions(),
                 "graines": {cle: {"entropie": str(graines.entropie), "spawn_key": [str(e)]} for cle, e in sorted(graines.derivees.items())},
                 "preenregistrement": dict(TEXTE), "addendum": dict(ADDENDUM), "tables_sha256": sha_tables}
    sha_manifeste = l7._ecrire_ferme(ctx.sortie / "runs" / ctx.run / "manifeste.json", manifeste)
    cle = (ctx.env if ctx.env is not None else os.environ).get(K.NOM_CLE)
    if cle and str(cle).strip():
        mo.aucune_occurrence([ctx.sortie, ctx.travail], mo.Cle(str(cle).strip()))
    horloge.consigner()
    versement = l7.nettoyer(ctx.travail, ctx.sortie, ctx.run) if nettoyage else None
    return {"versement_du_travail": versement, "tables": {"chemin": f"diag/{ctx.run}/{NOM_TABLES}", "sha256": sha_tables},
            "manifeste": {"chemin": f"runs/{ctx.run}/manifeste.json", "sha256": sha_manifeste}, "morceaux": morceaux,
            "lignes_proposees": [ligne_registre(K2.CLE_ENTREES_V2, f"diag/{ctx.run}/{NOM_ENTREES}", sha_entrees),
                                 ligne_registre(K2.CLE_TABLES_V2, f"diag/{ctx.run}/{NOM_TABLES}", sha_tables)],
            "empreinte_extrait": entrees.empreinte_extrait, "e1_sha256": entrees.sha256_e1}


# ========================================================================================================================================
# Phrases (étape du lecteur)
# ========================================================================================================================================
def rendre_phrases(tables: dict) -> dict:
    """Phrases gelées de la seconde passe, rendues mécaniquement à partir des tables fermées. Première passe lancée et non
    achevée : **aucune phrase gelée de la lentille publique ni de la lentille des logits** n'est écrite."""
    reproduction = tables["reproduction_de_la_premiere_passe"]
    ecrire_publique = reproduction["etat"] != rp.ETAT_NON_FAITE
    conditions = tables["nos_lentilles"]["condition_de_lecture"]
    palier = {K2.LENTILLE_NOTRE_R: conditions["R"]["palier"], K2.LENTILLE_NOTRE_S: conditions["S"]["palier"]}
    seconde = tables["nos_lentilles"].get("ligne_de_la_lecture_de_la_seconde_course")
    sortie = {"tete": tables["tete"], "directions": [], "comparaisons": [], "comparaisons_entre_lentilles": [], "non_lues": []}
    for s in tables["sondes"]:
        if not s["lue"]:
            sortie["non_lues"].append({"sonde": s["cle"], "phrase": ph.phrase_non_lue(s["motif"].removeprefix("non lue : "))})
    for d in tables["directions"]:
        nom = ph.nom_sonde(d["cellule"], d["pli"], d["role"], d["vecteur"])
        if d.get("non_calculable"):
            sortie["non_lues"].append({"sonde": f"{d['sonde']}/{d['vecteur']}", "phrase": ph.phrase_non_lue(d["non_calculable"])})
            continue
        for lentille, lecture in d["lectures"].items():
            if lentille in K.LENTILLES and not ecrire_publique:
                continue
            if "signes" not in lecture:
                sortie["non_lues"].append({"sonde": f"{d['sonde']}/{d['vecteur']}", "lentille": lentille,
                                           "phrase": ph.phrase_non_lue(lecture["non_calculable"])})
                continue
            for signe, t in lecture["signes"].items():
                ligne = {"sonde": d["sonde"], "vecteur": d["vecteur"], "lentille": lentille, "signe": signe, "phrases": [],
                         "renvois": ph.renvois(lentille, d["couche"], palier.get(lentille), seconde)}
                if t["libelle"] is None:
                    ligne["phrases"].append(ph.phrase_non_lue(t["non_calculable"]))
                else:
                    i, s = t["nuls"][t["nul_isotrope_en_vigueur"]], t["nuls"][K.NUL_SIGNES]
                    ligne["phrases"].append(ph.phrase_direction(lentille, nom, d["couche"], signe, t["libelle"], i["concentration"],
                                                                i["p_concentration"], s["p_concentration"],
                                                                t["premiers_par_score"]["chaines_echappees"]))
                    for famille, f in t["familles"].items():
                        ligne["phrases"].append(ph.phrase_famille(lentille, d["vecteur"], d["couche"], famille, f["n"],
                                                                  i["familles"][famille]["attendu"], i["familles"][famille]["p"],
                                                                  s["familles"][famille]["p"], f["sur_representee"]))
                sortie["directions"].append(ligne)
        p = d["poles"]
        for lentille, cle in ((K.LENTILLE_PUBLIQUE, "lecture_publique"), (K2.LENTILLE_NOTRE_R, "lecture_notre_r")):
            if (lentille == K.LENTILLE_PUBLIQUE and not ecrire_publique) or not all(cle in x for x in p["poles"]):
                continue
            phrase = ph.phrase_poles(lentille, p["libelle"], p["poles"], p["p"][p["nul_isotrope_en_vigueur"]], p["p"][K.NUL_SIGNES],
                                     [x[cle]["chaines_echappees"] for x in p["poles"]])
            ligne = {"sonde": d["sonde"], "vecteur": d["vecteur"], "poles": True, "lentille": lentille, "libelle": p["libelle"],
                     "phrases": [phrase] if phrase else [], "renvois": ph.renvois(lentille, d["couche"], palier.get(lentille), seconde)}
            if phrase is None:
                ligne["note"] = l7.NOTE_POLES_INTERMEDIAIRES
            sortie["directions"].append(ligne)
        for signe, e in d["entre_lentilles"].items():
            c = e["principale"]
            if c.get("libelle") is None:
                continue
            if c["libelle"] != co.NON_CALCULABLE:
                nul_iso = c["nul_isotrope_en_vigueur"]
                c = c | {"mediane": c["nuls"][nul_iso]["mediane"], "p": (c["nuls"][nul_iso]["p"], c["nuls"][K.NUL_SIGNES]["p"]),
                         "moities": e["moities"].get("recouvrement") if e["moities"].get("libelle") != co.NON_CALCULABLE
                         else "non calculable"}
            sortie["comparaisons_entre_lentilles"].append({
                "sonde": d["sonde"], "vecteur": d["vecteur"], "signe": signe, "libelle": c["libelle"],
                "phrase": ph.phrase_comparaison_entre_lentilles(nom, d["couche"], signe, c),
                "renvois": ph.renvois(K2.LENTILLE_NOTRE_R, d["couche"], palier[K2.LENTILLE_NOTRE_R], seconde)})
    for c in tables["comparaisons"]:
        a, b = c["a"].split("/"), c["b"].split("/")
        for lentille in ([K.LENTILLE_PUBLIQUE] if ecrire_publique else []) + [l for l in (K2.LENTILLE_NOTRE_R, K2.LENTILLE_NOTRE_S)
                                                                             if c["cosinus"] is not None and l in c["jetons_communs"]]:
            communs = None if c["cosinus"] is None else c["jetons_communs"][lentille]["+"]
            sortie["comparaisons"].append({"type": c["type"], "a": c["a"], "b": c["b"], "lentille": lentille,
                                           "phrase": ph.phrase_comparaison(ph.nom_sonde(*a), ph.nom_sonde(*b), c["cosinus"], communs)})
    return sortie


# ========================================================================================================================================
# Ligne de commande
# ========================================================================================================================================
def principal(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Seconde passe de la lecture des sondes de l'étape B bis par lentilles (texte scellé v2)")
    sp = p.add_subparsers(dest="commande", required=True)
    for nom in ("montage", "calcul"):
        s = sp.add_parser(nom)
        s.add_argument("--travail", required=True, type=Path)
        s.add_argument("--sortie", required=True, type=Path)
        s.add_argument("--run", required=True)
        s.add_argument("--depot", type=Path, default=Path("."))
        s.add_argument("--registre-propre", required=True, type=Path)
        if nom == "calcul":
            s.add_argument("--entrees", required=True, type=Path)
            s.add_argument("--registre-bbis", required=True, type=Path)
            s.add_argument("--premiere-passe", type=Path, default=None,
                           help="dossier qui porte les tables fermées de la première passe (chemin de leur ligne de registre)")
    s = sp.add_parser("recuperer")
    s.add_argument("--url", required=True)
    s.add_argument("--entrees", required=True, type=Path)
    s.add_argument("--registre-bbis", required=True, type=Path)
    s.add_argument("--registre-propre", required=True, type=Path)
    s.add_argument("--depot", type=Path, default=Path("."))
    s = sp.add_parser("phrases")
    s.add_argument("--tables", required=True, type=Path)
    s.add_argument("--sortie", required=True, type=Path)
    a = p.parse_args(argv)
    arret = None
    try:
        if a.commande == "recuperer":
            exiger_fiche_code(a.depot, a.registre_propre)
            en.recuperer_entrees(a.url, a.entrees, a.registre_bbis, a.registre_propre)
            rendu = {"entrees": str(a.entrees)}
        elif a.commande == "phrases":
            verifier(a.tables)
            rendu = {"sha256": l7._ecrire_ferme(a.sortie, rendre_phrases(json.loads(a.tables.read_text(encoding="utf-8"))))}
        else:
            ctx = Contexte(a.travail, a.sortie, a.run, a.depot, a.registre_propre, Reglages())
            rendu = monter(ctx) if a.commande == "montage" else calculer(ctx, a.entrees, a.registre_bbis, a.premiere_passe)
            if a.commande == "calcul":      # cloisonnement : l'opérateur ne voit que fichiers et empreintes
                rendu["morceaux"] = [{"fichier": m["fichier"], "sha256": m["sha256"]} for m in rendu["morceaux"]]
    except Arret as e:
        arret = e                           # rien d'autre dans ce bloc ; hors de lui, aucun arrêt n'est « en cours »
    if arret is not None:
        print(ligne_affichee(arret), file=sys.stderr)
        return 3
    print(json.dumps(rendu, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
