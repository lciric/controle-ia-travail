"""Répétition sur carte de l'étape B bis, **données synthétiques seulement**, avant `CODE-BBIS` (mot de Lazar, R-2802 : écart
déclaré au texte scellé ; sous la ligne GO-2026-11-14-09, plafond de la répétition 3 USD, une seule machine), v2 : la v1, dont
le contrôle carte-processeur est celui de la course v2 (`t07bbis.validation_imbriquee_v2.controle_deux_horizons` : linéaire à
300 époques, attention à 3 époques, déterminisme de l'attention à 300 époques ; brouillon 4, plan, point 5 ; R-2917) ; quatrième
passe ; la v1 reste (R12).

Aucune donnée ni sortie de 7a, 7b, T0.7 ou P3-bis n'est lue : les jetons sont tirés ici. Le code de la course n'est pas changé :
ce script **appelle** `t07bbis.apprentissage_carte_v1` (`LotCarte`, `entrainer`, `controle_carte_processeur`),
`harnais.modeles.regler_determinisme`, le contrôle aux deux horizons et les constantes de la garde de débit
(`t07bbis.validation_imbriquee_v2`, qui reprend la v1,
`t07bbis.commun_v1`), tels quels.

Sous-commandes :
- `carte --sortie F.json [--appareil cuda] [--actions 640] [--largeur 4096] [--par-famille 3] [--tolerance 1e-4]` (sur la
  machine, par `scripts/amorce_repetition_bbis_v2.sh`) : jeu synthétique **de la taille de la course** par défaut (640 actions =
  32 tâches × 20 actions, longueurs de 150 à 297 jetons, ≈ 143 000 jetons × 4 096 dimensions : `devis-etape-b-bis-v3.md`, l. 17,
  `9431d300…` ; 1 fil de calcul comme la course, `prereg/T0.6-organismes-config-7b-v1.json`, `"fils": 1`, `b7a5c1ba…`) ;
  algorithmes déterministes (`regler_determinisme(1, appareil)`) ; apprentissages entrelacés des deux familles (couche 15,
  régularisations de la grille), durée de chacun ; déterminisme (premier réglage de chaque famille réappris : paramètres égaux au
  bit près) ; **contrôle carte-processeur** au seuil du texte (10⁻⁴, 256 actions de contrôle tirées à part), aux deux horizons de la
  course v2 (linéaire à 300 époques, attention à 3 époques, déterminisme de l'attention à 300 époques) ;
  projection de la garde de débit de la course (2 460 apprentissages ; variante (r1) : 1 240) à partir de la médiane mesurée.
  Codes fermés : 0 réussie ; 2 garde (arguments, carte absente, tolérance au-dessus du texte) ; 8 erreur d'apprentissage (torch
  compris) ; 9 contrôle carte-processeur au-delà du seuil ou apprentissage non déterministe. Le fichier de sortie est écrit dans
  tous les cas (état, motif, durées) ; **aucune aire** (rien n'est noté).
  Un état partiel est écrit avant les contrôles sur processeur (les durées sur la carte survivent à une interruption).
- Côté session, par `scripts/lancer_repetition_bbis_v2.sh` (code 0 accepté, 2 refus, motif écrit) :
  `offre-depuis-recherche RECHERCHE.json ID OFFRE.json` (offre construite **par programme** depuis la sortie de la recherche,
  jamais retapée) ; `offre OFFRE.json ID PRIX` ; `garde-commande ECHEANCE PRIX FEU MAINTENANT` (plafond **strictement** sous
  3 USD) ; `depense CUMUL PRIX` ; `identifiant ID` ; `creation CREATION.json` ; `etiquette`, `relire`, `trouver`, `absence`,
  `credit` (fichiers privés lus par programme, champs utiles seulement, jamais affichés, supprimés avec `--supprimer`).
- **Garde positive de destruction** (contre-lecture de sûreté M1, m1) : l'instance à détruire est celle du `new_contract` lu dans
  le fichier de création, **relue avec l'étiquette `bbis-t07-repetition-v1`** dans la liste des instances avant toute
  destruction ; identifiants en **entiers ASCII** seulement (`^[1-9][0-9]*$` ; refus de `060670453`, des chiffres pleine largeur,
  des espaces), comparés en entiers ; jamais une instance d'une autre session : la liste de la course
  (`registre_bbis_v1.INSTANCES_D_AUTRES_SESSIONS`, lue telle quelle) plus la liste propre de la répétition (60671759, course
  Neuron Lens en cours) ; témoins : 60480302 ou 60670453 seulement.

Graines (R9) : `numpy.random.SeedSequence(ENTROPIE_REPETITION, spawn_key=(cle_de_tache(clé),))`, clés
`bbis/repetition/donnees`, `bbis/repetition/controle`, `bbis/repetition/sonde/<famille>/<l2>` ; entropie fixe écrite ici
(répétition non décisive, déclaré).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import traceback
from pathlib import Path

GO_ID = "GO-2026-11-14-09"
MOT_REPETITION = "R-2802"
PLAFOND_USD = 3.0
QUART_D_HEURE = 0.25
ECHEANCE_MAX_S = 3 * 3600
RESERVE_FIN_S = 900        # l'amorce cesse le travail et pousse ses traces 15 min avant l'échéance (contre-lecture M-4)
ETIQUETTE = "bbis-t07-repetition-v1"
CARTE = "A100 SXM4 80GB"   # forme de OFFRE.json, écrite par `offre-depuis-recherche`
NOM_CARTE_OUTIL = "A100 SXM4"
MEMOIRE_CARTE_MIN_MO = 79000
OFFRE_MIN = {"coeurs": 16, "memoire_vive_mo": 128000, "disque_go": 60, "stockage_max_usd_h": 0.08, "prix_max_usd_h": 1.40}
DISQUE_GO = 60
# instances d'autres sessions : jamais détruites ; la liste de la course, lue telle quelle (liste unique,
# `registre_bbis_v1.INSTANCES_D_AUTRES_SESSIONS`, R-2789, R-2795), plus la liste propre de la répétition (contre-lecture de
# sûreté M1 : 60671759, course Neuron Lens en cours, même compte) ; témoins de l'absence : 60480302 ou 60670453 seulement
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from controle_ia.t07bbis.registre_bbis_v1 import INSTANCES_D_AUTRES_SESSIONS  # noqa: E402
# version CUDA servie par l'hôte (`cuda_max_good`) : même seuil et même garde que la course (13.0, roue torch cu130)
from controle_ia.t07bbis.registre_bbis_v1 import (  # noqa: E402,F401
    CUDA_MAX_GOOD_MIN, faute_cuda_hote, lire_offre_de_recherche, offre_construite)
from controle_ia.gardes import GardeArret  # noqa: E402
INSTANCES_PROPRES_REPETITION = ("60671759",)
TEMOINS = ("60480302", "60670453")
ENTROPIE_REPETITION = 0x6B0B1D5E2C4A48F1A3E7D2C9B85F0141
ACTIONS, LARGEUR, LONGUEURS = 640, 4096, (150, 297)
COUCHE = 15
CODES = {"reussie": 0, "garde": 2, "apprentissage": 8, "controle": 9}
ENTIER_ASCII = re.compile(r"[1-9][0-9]*", re.ASCII)
MOTIF_JETON = re.compile(r"(?:gh[pousr]_|github_pat_|hf_)[A-Za-z0-9_]{20,}", re.ASCII)


class Refus(Exception):
    """Refus d'une garde de la répétition (motif écrit, code 2)."""


# ------------------------------------------------------------------------------------------------------------ côté session

def entier_ascii(x, quoi: str = "identifiant") -> int:
    """Entier positif écrit en chiffres ASCII sans zéro de tête ni espace (refus de `060670453`, des chiffres pleine largeur, des
    espaces, des booléens) ; jamais `str.isdigit()` (contre-lecture de sûreté m1)."""
    if isinstance(x, bool):
        raise Refus(f"{quoi} {x!r} illisible : entier ASCII attendu")
    if isinstance(x, int):
        if x <= 0:
            raise Refus(f"{quoi} {x!r} illisible : entier positif attendu")
        return x
    if isinstance(x, str) and ENTIER_ASCII.fullmatch(x):
        return int(x)
    raise Refus(f"{quoi} {x!r} illisible : entier ASCII sans zéro de tête ni espace attendu")


PROTEGEES = frozenset(entier_ascii(p) for p in tuple(INSTANCES_D_AUTRES_SESSIONS) + INSTANCES_PROPRES_REPETITION)


def exiger_identifiant(ident) -> int:
    """Instance détruisable par la répétition : entier ASCII, jamais une instance d'une autre session."""
    n = entier_ascii(ident)
    if n in PROTEGEES:
        raise Refus(f"instance {n} d'une autre session : jamais détruite")
    return n


def lire_json(chemin, supprimer: bool = False):
    """JSON d'un fichier privé (liste des instances, utilisateur, création) ; rend (document, nombre de motifs de jeton vus) ; rien
    n'est affiché ; `supprimer` : le fichier, son compagnon `erreur.txt` et leur dossier jetable sont retirés après lecture."""
    chemin = Path(chemin)
    try:
        texte = chemin.read_text(encoding="utf-8")
    except OSError as e:
        raise Refus(f"{chemin.name} illisible ({type(e).__name__})") from None
    finally:
        if supprimer:
            for p in (chemin, chemin.parent / "erreur.txt"):
                try:
                    p.unlink()
                except OSError:
                    pass
            try:
                chemin.parent.rmdir()
            except OSError:
                pass
    vus = len(MOTIF_JETON.findall(texte))
    try:
        return json.loads(texte), vus
    except ValueError:
        raise Refus(f"{chemin.name} illisible (JSON attendu)") from None


def alerte_jetons(vus: int, quoi: str) -> None:
    if vus:
        print(f"BBIS REPETITION ALERTE : {vus} motif(s) de jeton dans {quoi} : révoquer le jeton aussitôt (jamais affiché)")


def instances(doc) -> list[dict]:
    """Liste des instances lue sans erreur : objets portant un `id` entier ASCII ; seuls `id`, `label`, `gpu_name`, `gpu_ram`,
    `dph_total` sont gardés."""
    liste = doc.get("instances") if isinstance(doc, dict) else doc
    if not isinstance(liste, list) or any(not isinstance(i, dict) or "id" not in i for i in liste):
        raise Refus("liste des instances illisible (liste d'objets portant « id » attendue)")
    sortie = []
    for i in liste:
        try:
            n = entier_ascii(i["id"], "identifiant listé")
        except Refus as e:
            raise Refus(f"liste des instances illisible : {e}") from None
        sortie.append({"id": n, **{k: i.get(k) for k in ("label", "gpu_name", "gpu_ram", "dph_total")}})
    return sortie


def lire_creation(doc) -> int:
    """`new_contract` de la sortie de `vastai create instance --raw`, lu par programme ; absent ou illisible : refus (ne jamais
    deviner un identifiant : `trouver` par l'étiquette)."""
    if not isinstance(doc, dict) or "new_contract" not in doc:
        raise Refus("fichier de création sans « new_contract » : ne pas deviner ; lire l'instance par son étiquette (trouver)")
    return exiger_identifiant(doc["new_contract"])


def exiger_etiquette(liste: list[dict], ident: int) -> dict:
    """Garde positive : l'instance à détruire est listée et porte l'étiquette de la répétition."""
    vues = [i for i in liste if i["id"] == ident]
    if len(vues) != 1:
        raise Refus(f"instance {ident} absente de la liste (ou en double) : rien à détruire sous ce nom ; vérifier l'absence")
    if vues[0]["label"] != ETIQUETTE:
        raise Refus(f"instance {ident} d'étiquette {vues[0]['label']!r} ≠ {ETIQUETTE} : jamais détruite par la répétition")
    return vues[0]


def relire_instance(liste: list[dict], ident: int) -> dict:
    """Après la création : l'instance porte l'étiquette, une A100 SXM4 80 Go, un prix au plus 1,40 USD/h ; sinon détruire."""
    i = exiger_etiquette(liste, ident)
    fautes = []
    if i["gpu_name"] != NOM_CARTE_OUTIL:
        fautes.append(f"carte {i['gpu_name']!r} ≠ {NOM_CARTE_OUTIL!r}")
    if i["gpu_ram"] is not None and not (isinstance(i["gpu_ram"], (int, float)) and i["gpu_ram"] >= MEMOIRE_CARTE_MIN_MO):
        fautes.append(f"mémoire de la carte {i['gpu_ram']!r} Mo < {MEMOIRE_CARTE_MIN_MO}")
    p = i["dph_total"]
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not 0 < p <= OFFRE_MIN["prix_max_usd_h"]:
        fautes.append(f"prix {p!r} USD/h hors de ]0 ; {OFFRE_MIN['prix_max_usd_h']}]")
    if fautes:
        raise Refus(f"instance {ident} hors borne ({' ; '.join(fautes)}) : la détruire aussitôt (detruire CREATION.json)")
    return i


def trouver_par_etiquette(liste: list[dict]) -> int:
    vues = [i["id"] for i in liste if i["label"] == ETIQUETTE]
    if len(vues) != 1:
        raise Refus(f"{len(vues)} instance(s) d'étiquette {ETIQUETTE} : une exactement attendue ; ne rien deviner")
    return exiger_identifiant(vues[0])


def exiger_absence(liste_doc, ident, temoin) -> dict:
    """Destruction prouvée par l'absence de l'instance dans la liste lue sans erreur, un témoin connu (60480302 ou 60670453)
    présent ; comparaison en entiers (jamais en chaînes)."""
    n = exiger_identifiant(ident)
    if str(temoin) not in TEMOINS:
        raise Refus(f"absence non prouvée : témoin {temoin!r} hors de {TEMOINS} : arrêt")
    t = entier_ascii(str(temoin))
    try:
        ids = {i["id"] for i in instances(liste_doc)}
    except Refus as e:
        raise Refus(f"absence non prouvée : {e} : arrêt") from None
    if t not in ids:
        raise Refus(f"absence non prouvée : témoin {t} absent de la liste ({len(ids)} instance(s)) : liste incomplète ou témoin "
                    "détruit ; arrêt, refaire la lecture avec l'autre témoin")
    if n in ids:
        raise Refus(f"absence non prouvée : instance {n} toujours dans la liste (témoin {t} présent) : destruction non faite ; "
                    "arrêt, refaire `vastai destroy instance ID -y` puis la vérification")
    return {"detruite": n, "temoin": t, "instances_listees": len(ids)}


def offre_depuis_recherche(doc, ident) -> dict:
    """Offre lue par programme dans la sortie de `vastai search offers --raw` par la fonction commune à la course
    (`registre_bbis_v1.lire_offre_de_recherche` : clés de l'outil, carte A100 SXM4 80 Go exactement, `cuda_max_good` au moins
    13.0 ; toute clé absente ou illisible → refus, jamais un défaut deviné), puis la borne de prix de la répétition."""
    n = entier_ascii(ident, "identifiant d'offre")
    try:
        o, fautes = lire_offre_de_recherche(doc, n)
    except GardeArret as e:
        raise Refus(str(e)) from None
    if not 0 < float(o["dph_total"]) <= OFFRE_MIN["prix_max_usd_h"]:
        fautes.append(f"prix {o['dph_total']!r} USD/h > {OFFRE_MIN['prix_max_usd_h']}")
    if fautes:
        raise Refus("offre hors des bornes de la répétition : " + " ; ".join(fautes))
    return offre_construite(o, n, DISQUE_GO, ETIQUETTE)


def exiger_offre(offre: dict, identifiant, prix: float) -> dict:
    """Machine de la classe de la course (A100 SXM4 80 Go exactement), étiquette de la répétition, identifiant et prix relevés le
    jour (au plus 1,40 USD de l'heure, pire cas du devis de B bis) ; version CUDA servie par l'hôte (`cuda_max_good`) au moins
    13.0, clé absente ou illisible : refus."""
    fautes = []
    if offre.get("carte") != CARTE:
        fautes.append(f"carte {offre.get('carte')!r} ≠ {CARTE!r} (celle de la course, exactement)")
    for cle in ("coeurs", "memoire_vive_mo", "disque_go"):
        try:
            v = float(offre.get(cle))
        except (TypeError, ValueError):
            v = -1.0
        if v < OFFRE_MIN[cle]:
            fautes.append(f"{cle} {offre.get(cle)!r} < {OFFRE_MIN[cle]}")
    try:
        st = float(offre.get("stockage_usd_h"))
    except (TypeError, ValueError):
        st = float("inf")
    if not st <= OFFRE_MIN["stockage_max_usd_h"]:
        fautes.append(f"stockage {offre.get('stockage_usd_h')!r} USD/h > {OFFRE_MIN['stockage_max_usd_h']}")
    if offre.get("etiquette") != ETIQUETTE:
        fautes.append(f"étiquette {offre.get('etiquette')!r} ≠ {ETIQUETTE}")
    f = faute_cuda_hote(offre.get("cuda_max_good"))
    if f:
        fautes.append(f)
    try:
        if entier_ascii(offre.get("id"), "id") != entier_ascii(str(identifiant), "identifiant d'offre"):
            raise Refus("différents")
    except Refus:
        fautes.append(f"identifiant {offre.get('id')!r} de l'offre décrite ≠ offre demandée {identifiant!r}")
    try:
        p_offre = float(offre.get("prix_usd_h"))
    except (TypeError, ValueError):
        p_offre = float("nan")
    if not (0 < float(prix) <= OFFRE_MIN["prix_max_usd_h"]) or p_offre != float(prix):
        fautes.append(f"prix {prix!r} USD/h (offre : {offre.get('prix_usd_h')!r}) : relevé du jour, au plus "
                      f"{OFFRE_MIN['prix_max_usd_h']} USD/h")
    if fautes:
        raise Refus("offre hors des bornes de la répétition : " + " ; ".join(fautes))
    return offre


MARGE_USD = 0.40       # stockage (≤ 0,08 USD/h) et téléchargements (≤ 0,05 USD par Go, ≈ 5 Go) : bornes du devis de B bis


def duree_max_h(prix: float) -> float:
    """Durée de carte jusqu'à l'échéance **à l'égalité** du plafond : (durée + un quart d'heure) × prix + marge = plafond (au plus
    3 h) ; toute échéance permise est strictement en deçà."""
    return min(ECHEANCE_MAX_S / 3600.0, (PLAFOND_USD - MARGE_USD) / float(prix) - QUART_D_HEURE)


def garde_commande(echeance: int, prix: float, feu: str, maintenant: int) -> dict:
    """Feu écrit de la mère portant la ligne de GO et le mot de la répétition ; échéance (minuterie de destruction) dans
    ]maintenant, maintenant + 3 h] et telle que (durée + un quart d'heure) × prix + marge soit **strictement** sous le plafond de
    3 USD (contre-lecture M-5) ; rend aussi le budget de travail (échéance − 15 min, réserve de fin de l'amorce)."""
    if not (isinstance(feu, str) and GO_ID in feu and MOT_REPETITION in feu):
        raise Refus(f"feu écrit de la mère portant {GO_ID} et {MOT_REPETITION} absent : aucune création")
    if not 0 < float(prix) <= OFFRE_MIN["prix_max_usd_h"]:
        raise Refus(f"prix {prix!r} USD/h hors de ]0 ; {OFFRE_MIN['prix_max_usd_h']}]")
    duree_h, dmax = (int(echeance) - int(maintenant)) / 3600.0, duree_max_h(prix)
    cout = (duree_h + QUART_D_HEURE) * float(prix) + MARGE_USD
    if not (0 < duree_h <= ECHEANCE_MAX_S / 3600.0 and cout < PLAFOND_USD):
        raise Refus(f"échéance dans {duree_h:.2f} h ({cout:.2f} USD au plus) : strictement moins de {dmax:.2f} h à "
                    f"{float(prix):g} USD/h (plafond {PLAFOND_USD:g} USD, strict)")
    return {"duree_h": duree_h, "cout_max_usd": cout, "plafond_usd": PLAFOND_USD, "duree_max_h": dmax,
            "budget_travail_min": (int(echeance) - int(maintenant) - RESERVE_FIN_S) / 60.0}


def garde_depense(cumul: float, prix: float) -> dict:
    """Garde de dépense de la course (`registre_bbis_v1.garde_depense`), appelée telle quelle à la coupure de 3 USD ; le cumul
    est celui de la répétition seule, stockage compris (contre-lecture m8)."""
    from controle_ia.gardes import GardeArret
    from controle_ia.t07bbis.registre_bbis_v1 import garde_depense as gd
    try:
        return gd(float(cumul), float(prix), coupure=PLAFOND_USD)
    except GardeArret as e:
        raise Refus(f"{e} (répétition : plafond {PLAFOND_USD:g} USD)") from None


def lire_credit(doc) -> float:
    """Crédit du compte (champ `credit` de `vastai show user --raw`, seul lu ; jamais affiché d'autre champ)."""
    c = doc.get("credit") if isinstance(doc, dict) else None
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise Refus("crédit illisible (champ « credit » attendu) : forme de l'outil à vérifier ; aucune location")
    return float(c)


# ------------------------------------------------------------------------------------------------------------ sur la carte

def _graine(cle: str):
    import numpy as np
    from controle_ia.manifeste import cle_de_tache
    return np.random.SeedSequence(ENTROPIE_REPETITION, spawn_key=(cle_de_tache(cle),))


def jeu_synthetique(n_actions: int, largeur: int, cle: str):
    """Actions synthétiques (jetons × largeur, simple précision comme les activations relues), deux classes égales ; un léger
    décalage des positifs le long d'une direction tirée (la sonde apprend quelque chose ; aucune aire n'est calculée)."""
    import numpy as np
    rng = np.random.default_rng(_graine(cle))
    u = rng.standard_normal(largeur).astype(np.float32)
    u /= np.linalg.norm(u)
    y = np.r_[np.ones(n_actions // 2, int), np.zeros(n_actions - n_actions // 2, int)]
    seqs = []
    for k in range(n_actions):
        n = int(rng.integers(LONGUEURS[0], LONGUEURS[1] + 1))
        x = rng.standard_normal((n, largeur), dtype=np.float32)
        if y[k]:
            x[: max(1, n // 4)] += 0.5 * u
        seqs.append(x)
    return seqs, y


def jouer_carte(sortie: Path, appareil: str = "cuda", n_actions: int = ACTIONS, largeur: int = LARGEUR, par_famille: int = 3,
                tolerance: float | None = None) -> int:
    debut = time.time()
    doc = {"texte": "prereg/T0.7-etape-B-bis-v1.md", "mot": MOT_REPETITION, "go": GO_ID, "donnees": "synthétiques seulement",
           "appareil": appareil, "actions": int(n_actions), "largeur": int(largeur), "longueurs": list(LONGUEURS),
           "fraction_de_la_course": None, "par_famille": int(par_famille), "aucune_aire": True, "etat": "en cours"}
    sortie = Path(sortie)
    if sortie.exists():
        print(f"BBIS REPETITION REFUS : {sortie} existe déjà (R12)")
        return CODES["garde"]

    def ecrire(etat: str, code: int, motif: str | None = None, pile: str | None = None) -> int:
        doc.update({"etat": etat, "code": code, "motif": motif, "pile": pile, "duree_totale_s": time.time() - debut})
        sortie.write_text(json.dumps(doc, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n", encoding="utf-8")
        print(f"BBIS REPETITION {etat.upper()} (code {code})" + (f" : {motif}" if motif else ""))
        return code

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
        import numpy as np
        from controle_ia.gardes import GardeArret
        from controle_ia.harnais.modeles import regler_determinisme
        from controle_ia.t07bbis import apprentissage_carte_v1 as ac
        from controle_ia.t07bbis import validation_imbriquee_v2 as vi
        from controle_ia.t07bbis.commun_v1 import (COUCHES_REELLES, FAMILLES, L2, N_ACTIONS_CONTROLE_CARTE, N_PLIS_INTERNES,
                                                   N_REETIQUETAGES, TOLERANCE_CARTE, VARIANTES, grille)
    except Exception as e:                                         # environnement incomplet : écrit, jamais une chute
        return ecrire("garde", CODES["garde"], f"import : {type(e).__name__}: {e}", traceback.format_exc()[-4000:])
    tol = TOLERANCE_CARTE if tolerance is None else float(tolerance)
    if not 0 < tol <= TOLERANCE_CARTE or int(par_famille) < 1 or int(par_famille) > len(L2) or int(n_actions) < 8:
        return ecrire("garde", CODES["garde"], f"tolérance {tol:g} (au plus celle du texte, {TOLERANCE_CARTE:g}), "
                      f"par famille {par_famille} (1 à {len(L2)}), actions {n_actions} (au moins 8)")
    doc.update({"tolerance": tol, "fraction_de_la_course": int(n_actions) * int(largeur) / (ACTIONS * LARGEUR)})
    try:
        doc["determinisme"] = regler_determinisme(1, appareil)
    except GardeArret as e:
        return ecrire("garde", CODES["garde"], f"réglages de la carte : {e}")
    etape = "jeu synthétique"
    try:
        t0 = time.perf_counter()
        seqs, y = jeu_synthetique(int(n_actions), int(largeur), "bbis/repetition/donnees")
        ctrl, _ = jeu_synthetique(min(N_ACTIONS_CONTROLE_CARTE, 4 * int(n_actions)), int(largeur), "bbis/repetition/controle")
        doc["jetons"] = int(sum(len(s) for s in seqs))
        doc["duree_jeu_s"] = time.perf_counter() - t0
        etape = "lot sur l'appareil"
        t0 = time.perf_counter()
        lot = ac.LotCarte(seqs, appareil)
        doc["duree_lot_s"] = time.perf_counter() - t0
        reglages = [r for r in grille([COUCHE], FAMILLES) if r["l2"] in L2[: int(par_famille)]]   # entrelacés : L, A, L, A…
        doc["apprentissages"], sondes = [], {}
        etape = "apprentissages"
        for r in reglages:
            g = int(_graine(f"bbis/repetition/sonde/{r['famille']}/{r['l2']}").generate_state(1)[0])
            t0 = time.perf_counter()
            s = ac.entrainer(lot, r["famille"], r["nom"], r["couche"], y, r["l2"], g)
            doc["apprentissages"].append({"reglage": r["nom"], "famille": r["famille"], "duree_s": time.perf_counter() - t0})
            sondes.setdefault(r["famille"], (r, g, s))
        etape = "déterminisme"
        doc["deterministe"] = {}
        for f, (r, g, s) in sondes.items():
            s2 = ac.entrainer(lot, r["famille"], r["nom"], r["couche"], y, r["l2"], g)
            egal = bool(np.array_equal(s.w, s2.w) and s.b == s2.b and (s.q is None or np.array_equal(s.q, s2.q)))
            doc["deterministe"][f] = egal
        durees = [a["duree_s"] for a in doc["apprentissages"]]
        med = float(np.median(durees))
        med_lin = float(np.median([a["duree_s"] for a in doc["apprentissages"] if a["famille"] == "lineaire"]))
        total = vi.apprentissages_prevus(5, len(grille(COUCHES_REELLES, FAMILLES)), N_PLIS_INTERNES, N_REETIQUETAGES)
        total_r1 = vi.apprentissages_prevus(5, len(grille(COUCHES_REELLES, VARIANTES["r1"]["familles"])), N_PLIS_INTERNES,
                                            VARIANTES["r1"]["n_reetiquetages"])
        proj = lambda n, m, relecture: relecture + (n - vi.N_PREMIERS) * m * vi.FACTEUR_DEBIT / 3600.0 + vi.MARGE_H
        doc["garde_de_debit"] = {
            "mediane_s": med, "mediane_lineaire_s": med_lin, "apprentissages_course": total, "apprentissages_r1": total_r1,
            "limite_h": vi.LIMITE_H, "relecture_h_devis": [0.35, 0.55],
            "projete_h": [proj(total, med, h) for h in (0.35, 0.55)],
            "projete_r1_h": [proj(total_r1, med_lin, h) for h in (0.35, 0.55)],
            "mediane_seuil_s": (vi.LIMITE_H - 0.55 - vi.MARGE_H) * 3600.0 / ((total - vi.N_PREMIERS) * vi.FACTEUR_DEBIT),
            "note": "durées au lot entier de 640 actions (sonde finale, nul) ; la validation interne apprend sur 480 : prudent"}
        doc["garde_de_debit"]["se_declencherait"] = max(doc["garde_de_debit"]["projete_h"]) > vi.LIMITE_H
        partiel = {**doc, "etat": "partiel (contrôles carte-processeur en cours)", "duree_totale_s": time.time() - debut}
        sortie.write_text(json.dumps(partiel, indent=1, ensure_ascii=False, sort_keys=True, default=str) + "\n", encoding="utf-8")
        etape = "contrôle carte-processeur"
        t0 = time.perf_counter()
        l2_c = float(reglages[0]["l2"])                    # premier réglage de chaque famille (couche 15), comme la v1

        def graine_de(f):
            return int(_graine(f"bbis/repetition/sonde/{f}/{l2_c}").generate_state(1)[0])
        try:                                               # la fonction de la course v2, telle quelle
            c = vi.controle_deux_horizons(lot, seqs, y, COUCHE, l2_c, graine_de, ctrl, familles=FAMILLES,
                                          sondes_300={f: s for f, (r, g, s) in sondes.items() if r["l2"] == l2_c},
                                          tolerance=tol, nom="repetition")
        except GardeArret as e:
            doc["controle_carte_processeur"] = {"arret": {"refus": str(e), "duree_s": time.perf_counter() - t0}}
            return ecrire("controle", CODES["controle"], str(e))
        doc["controle_carte_processeur"] = {f: c[f] for f in ("lineaire", "attention") if f in c}
        if "determinisme_attention" in c:                  # égalité au bit près : écart nul (lu par le résumé de l'amorce)
            doc["controle_carte_processeur"]["determinisme_attention"] = {**c["determinisme_attention"], "ecart_relatif_max": 0.0}
        doc["controle_parametres"] = {k: c[k] for k in ("tolerance", "couche", "l2", "familles")}
        doc["controle_parametres"]["duree_s"] = time.perf_counter() - t0
        if not all(doc["deterministe"].values()):
            return ecrire("controle", CODES["controle"], f"apprentissage non déterministe : {doc['deterministe']}")
    except Exception as e:                                         # torch compris : arrêt écrit, code fermé
        return ecrire("apprentissage", CODES["apprentissage"], f"{etape} : {type(e).__name__}: {e}"[:4000],
                      traceback.format_exc()[-6000:])
    return ecrire("reussie", CODES["reussie"])


# ------------------------------------------------------------------------------------------------------------ entrée

def _prive(a: list) -> tuple[list, bool]:
    return [x for x in a if x != "--supprimer"], "--supprimer" in a


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if a[:1] == ["carte"]:
        ap = argparse.ArgumentParser(description="répétition sur carte de B bis (données synthétiques)")
        ap.add_argument("--sortie", required=True)
        ap.add_argument("--appareil", default="cuda")
        ap.add_argument("--actions", type=int, default=ACTIONS)
        ap.add_argument("--largeur", type=int, default=LARGEUR)
        ap.add_argument("--par-famille", type=int, default=3)
        ap.add_argument("--tolerance", type=float, default=None)
        x = ap.parse_args(a[1:])
        return jouer_carte(Path(x.sortie), x.appareil, x.actions, x.largeur, x.par_famille, x.tolerance)
    a, supprimer = _prive(a)
    try:
        if a[:1] == ["offre"] and len(a) == 4:
            exiger_offre(lire_json(a[1])[0], a[2], float(a[3]))
            print("BBIS REPETITION OFFRE ACCEPTEE")
        elif a[:1] == ["offre-depuis-recherche"] and len(a) == 4:
            doc, vus = lire_json(a[1], supprimer)
            alerte_jetons(vus, "la sortie de la recherche")
            o = offre_depuis_recherche(doc, a[2])
            with open(a[3], "x", encoding="utf-8") as f:                   # R12 : jamais réécrit
                f.write(json.dumps(o, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
            print(f"BBIS REPETITION OFFRE ECRITE {a[3]} : offre {o['id']}, {o['carte']}, {o['prix_usd_h']:g} USD/h, "
                  f"stockage {o['stockage_usd_h']:.4f} USD/h, CUDA de l'hôte {o['cuda_max_good']:g}")
        elif a[:1] == ["garde-commande"] and len(a) == 5:
            r = garde_commande(int(a[1]), float(a[2]), a[3], int(a[4]))
            print(f"BBIS REPETITION COMMANDE PERMISE : {r['duree_h']:.2f} h au plus, {r['cout_max_usd']:.2f} USD au plus "
                  f"(strictement sous {PLAFOND_USD:g}), budget de travail {r['budget_travail_min']:.0f} min")
        elif a[:1] == ["depense"] and len(a) == 3:
            print(f"BBIS REPETITION DEPENSE {garde_depense(float(a[1]), float(a[2]))}")
        elif a[:1] == ["identifiant"] and len(a) == 2:
            print(f"BBIS REPETITION IDENTIFIANT {exiger_identifiant(a[1])}")
        elif a[:1] == ["creation"] and len(a) == 2:
            print(f"BBIS REPETITION INSTANCE {lire_creation(lire_json(a[1])[0])}")
        elif a[:1] in (["etiquette"], ["relire"]) and len(a) == 3:
            n = lire_creation(lire_json(a[1])[0])
            doc, vus = lire_json(a[2], supprimer)
            alerte_jetons(vus, "la liste des instances")
            if a[0] == "etiquette":
                exiger_etiquette(instances(doc), n)
                print(f"BBIS REPETITION INSTANCE DE LA REPETITION {n} (étiquette {ETIQUETTE})")
            else:
                i = relire_instance(instances(doc), n)
                print(f"BBIS REPETITION INSTANCE CONFORME {n} : {i['gpu_name']}, {i['dph_total']} USD/h, étiquette {i['label']}")
        elif a[:1] == ["trouver"] and len(a) == 3:
            doc, vus = lire_json(a[1], supprimer)
            alerte_jetons(vus, "la liste des instances")
            n = trouver_par_etiquette(instances(doc))
            with open(a[2], "x", encoding="utf-8") as f:
                f.write(json.dumps({"new_contract": n, "trouve_par_etiquette": ETIQUETTE}) + "\n")
            print(f"BBIS REPETITION INSTANCE TROUVEE {n} par l'étiquette {ETIQUETTE} : {a[2]}")
        elif a[:1] == ["absence"] and len(a) == 4:
            n = lire_creation(lire_json(a[1])[0])
            try:
                doc, vus = lire_json(a[3], supprimer)
            except Refus as e:
                raise Refus(f"absence non prouvée : {e} : arrêt") from None
            alerte_jetons(vus, "la liste des instances")
            r = exiger_absence(doc, n, a[2])
            print(f"BBIS DESTRUCTION PROUVEE {r['detruite']} : absente de la liste, témoin {r['temoin']} présent, "
                  f"{r['instances_listees']} instance(s) listée(s)")
        elif a[:1] == ["credit"] and len(a) == 2:
            doc, vus = lire_json(a[1], supprimer)
            alerte_jetons(vus, "la fiche de l'utilisateur")
            c = lire_credit(doc)
            print(f"BBIS REPETITION CREDIT {c:.2f} USD" + (" : suffisant (au moins 4 USD)" if c >= 4.0 else
                                                         " : insuffisant (moins de 4 USD) : aucune location"))
            if c < 4.0:
                return 2
        else:
            print("BBIS REPETITION REFUS : commande inconnue (carte … | offre FICHIER ID PRIX | offre-depuis-recherche RECHERCHE ID "
                  "OFFRE | garde-commande ECHEANCE PRIX FEU MAINTENANT | depense CUMUL PRIX | identifiant ID | creation CREATION | "
                  "etiquette CREATION LISTE | relire CREATION LISTE | trouver LISTE SORTIE | absence CREATION TEMOIN LISTE | "
                  "credit FICHIER ; --supprimer)")
            return 2
    except (Refus, ValueError, OSError) as e:
        print(f"BBIS REPETITION REFUS : {e}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
