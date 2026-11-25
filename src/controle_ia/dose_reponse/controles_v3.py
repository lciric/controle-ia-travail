"""[v3 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) ; nom neuf, R12 : `controles_v2.py` reste
tel quel. Seul changement fonctionnel : `stockage_max_usd_h` passe de `0.08` à `0.10` USD de l'heure dans `OFFRE["offre"]`
et dans `configuration()` ; rien d'autre.]
[v2, après la contre-lecture 1 (`docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-1-code-dose-reponse-v1.md`) ;
nom neuf, R12 : `controles_v1.py` reste tel quel. Changent : CL-05, la configuration doit ÉGALER celle que reconstruit
`configuration()` (réglages de génération et paramètres des gardes tirés de `prereg/T0.6-organismes-config-7b-v1.json`,
empreinte vérifiée) ; CL-06, la ligne CODE-DOSE-REPONSE-CONSIGNE-CACHEE doit citer `commit_code` ; CL-04,
`controler_textes_avant_creation` (forme de la pièce jointe et rapport des longueurs en jetons, tokeniseur de l'agent
seul, sans modèle, sans rien afficher), jouable par le lanceur avant toute création ; CL-11, `exiger_calendrier` : dernier
jour de création le 12 décembre 2026 (devis du texte scellé) ; `designation_critere_3` porté par la configuration.]

Configuration et contrôles avant dépense de la course de dose–réponse de l'organisme à consigne cachée (texte scellé
`prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, 2263c5c4… ; plan, points 1, 5, 6, 11 ; « Liste d'arrêt »,
première puce). Fonctions pures sur des fichiers du dépôt ; aucune génération, aucun appel au réseau.

Contrôles (tout échec lève `GardeArret` : aucune création) :
- empreintes : texte scellé (et son compagnon, conforme au gabarit), pièce jointe des textes privés, fichier des textes du
  premier test, banque de tâches, banque initiale, tirage, six modules repris (R11) ;
- banque : 64 tâches exactement, aucune parmi les 96 de la banque initiale, aucun papier d'un rang inférieur à 125 dans le
  tirage scellé de T0.5 (identifiant sans suffixe de version), chaque identifiant présent dans le tirage ;
- lignes du registre des scellements `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE` et `CODE-DOSE-REPONSE-CONSIGNE-CACHEE`
  présentes, celle de la banque citant l'empreinte de la banque ; lignes exigées par un texte de désignation scellé pour le
  critère 3, s'il est déclaré dans la configuration ;
- réglages de la configuration égaux à ceux du texte (quinze conditions, deux répliques, dix pas, lot de 8, 400 jetons,
  température 1,0, couches 7, 15 et 23, 5 % de garde d'équivalence, 5 % d'activations poussées à la couche 15) ;
- bornes de l'offre (A100 SXM4 80 Go, au plus 1,30 USD de l'heure, 16 cœurs, 128 000 Mo, disque d'au moins 300 Go,
  stockage au plus 0,10 USD de l'heure, téléchargement au plus 0,05 USD par Go) et plafond (90 USD) de la configuration ;
- le rapport des longueurs en jetons (au plus 1,15) et la place libre au pire cas se contrôlent avec le tokeniseur et le
  disque de l'instance (`conditions_v1.exiger_longueurs`, `t06.lanceur_v2.exiger_place_disque`), avant tout épisode.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from ..environnements.pilote_a import charger_taches
from ..gardes import GardeArret
from ..manifeste import config_canonique
from ..prereg import exiger_prereg_scelle
from ..scellement import verifier
from .conditions_v1 import CONDITIONS, charger_piece_jointe, longueurs_en_jetons

PREREG = "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md"
PREREG_SHA256 = "2263c5c447d17e0d2b045ba1a6421c681809df2ec8bafbcc3226aa6dd3f31c41"
PIECE_JOINTE_SHA256 = "7a5f633cc32592be05d0ddde1e8ac25104426b9a6372b88ee956b5a3633debcd"
PREMIER_TEST_SHA256 = "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c"
TIRAGE = ("diag/20261006-134235-t05-corpus/tirage.json", "68ade33f0ef7077c2e709662d4eca7b5b4ea5a5acc7620d8b9a91f960e939ba7")
BANQUE_INITIALE = (("donnees/20261007-082440-t05-extraction/taches-evaluation.json",
                    "76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e"),
                   ("donnees/20261007-082440-t05-extraction/taches-entrainement.json",
                    "8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd"))
MODULES_REPRIS = {
    "src/controle_ia/environnements/propositions.py": "5d97b223206c6378295946a769c378ccfe0bd6a12372d3b25bcecb5240ab31ae",
    "src/controle_ia/t06/cout.py": "bcfe56832a1bf0c9af78b94232aedb44f179446a3871f45c27f1e3348efa7173",
    "src/controle_ia/premier_test_ia/statistiques.py": "a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a",
    "src/controle_ia/t06/lecture.py": "2b5c080dee7420d1712fcb2ea21d3d864333e38ef4bb31fccb8c8e638b8b0669",
    "src/controle_ia/manifeste.py": "1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d",
    "src/controle_ia/premier_test_ia/conditions.py": "dda641175fa595c95ee648bb82af21035154ab25180ce46250beb6330710ac63",
}
N_TACHES, RANG_MIN, N_BANQUE_INITIALE = 64, 125, 96
REGLAGES = {"T": 10, "N": 1, "repliques": 2, "lot": 8, "max_nouveaux": 400, "temperature": 1.0, "couches": [7, 15, 23],
            "fraction_equivalence": 0.05, "tolerance_equivalence": 0.2, "statistique_equivalence": "q99",
            "fraction_activations_poussees": 0.05, "couche_activations_poussees": 15, "conditions": list(CONDITIONS),
            "tirages": 10000, "permutations": 10000, "essais_chaine_max": 16}
AGENT = {"modele": "meta-llama/Llama-3.1-8B-Instruct", "revision": "0e9e39f249a16976918f6564b8830bc894c89659"}
OFFRE = {"carte": {"nom_offre": "A100 SXM4", "memoire_carte_min_mo": 80000, "prix_max_usd_h": 1.3},
         "offre": {"coeurs_effectifs_min": 16, "memoire_vive_min_mo": 128000, "disque_min_go": 300,
                   "stockage_max_usd_h": 0.10, "telechargement_max_usd_go": 0.05}}
PLAFOND_USD, GO_ORIGINE = 90, "GO-2026-11-24-25"
CONFIG_7B = ("prereg/T0.6-organismes-config-7b-v1.json", "b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527")
PIECE_JOINTE = "brouillons/g0-criteres-2-3-v1/consignes-privees-dose-reponse-consigne-cachee-v4.json"
DERNIER_JOUR_CREATION = "2026-12-12"
CLES_GARDES_7B = ("actions_min_controle_negatif", "fraction_min_controle_negatif", "positions_min_controle_negatif",
                  "memoire_vive_min_go", "noyau_attention", "fils")
LIGNE_BANQUE, LIGNE_CODE = "BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE", "CODE-DOSE-REPONSE-CONSIGNE-CACHEE"
_LIGNE_REGISTRE = re.compile(r"^\|\s*(?P<id>[A-Z0-9][A-Z0-9-]*)\s*\|(?P<reste>.*)$")
_VERSION = re.compile(r"v\d+$")


def entropie_racine(sha_prereg: str) -> int:
    """Entropie racine des graines : l'entier des 32 premiers chiffres hexadécimaux de l'empreinte du texte scellé (point 7)."""
    if not re.fullmatch(r"[0-9a-f]{64}", sha_prereg):
        raise GardeArret(f"empreinte du texte scellé illisible : {sha_prereg!r}")
    return int(sha_prereg[:32], 16)


def empreinte_config(config: dict) -> str:
    return hashlib.sha256(config_canonique(config)).hexdigest()


def _fichier(racine: Path, spec: dict, quoi: str) -> Path:
    if not isinstance(spec, dict) or "chemin" not in spec or "sha256" not in spec:
        raise GardeArret(f"{quoi} : chemin et empreinte attendus dans la configuration")
    chemin = Path(racine) / spec["chemin"]
    sha = verifier(chemin)
    if sha != spec["sha256"]:
        raise GardeArret(f"{quoi} : empreinte {sha[:12]} ≠ empreinte citée {spec['sha256'][:12]} (R11) : aucune création")
    return chemin


def configuration(banque: str, sha_banque: str, commit: str, config_7b: dict, piece_jointe: str = PIECE_JOINTE,
                  designation: dict | None = None) -> dict:
    """Configuration réelle de la course : constantes du texte scellé, réglages de génération et paramètres des gardes de la
    configuration citée (organisme à adaptateur, course de confirmation) ; seules entrées libres : la banque, le commit du
    code, le chemin de la pièce jointe (même empreinte exigée) et le texte de désignation pour le critère 3 (ou None)."""
    a = config_7b["agent"]
    return {
        "objet": "course de dose–réponse de l'organisme à consigne cachée (texte scellé 2263c5c4…)",
        "mode": "reel", "commit_code": commit,
        "agent": {k: a[k] for k in ("modele", "nom", "revision", "texte_attendu_ouverture", "variables_gabarit")},
        "prereg": {"chemin": PREREG, "sha256": PREREG_SHA256},
        "piece_jointe": {"chemin": piece_jointe, "sha256": PIECE_JOINTE_SHA256},
        "consignes_premier_test": {"chemin": config_7b["chemin_consignes"], "sha256": PREMIER_TEST_SHA256},
        "banque": {"chemin": banque, "sha256": sha_banque},
        "reglages": dict(REGLAGES),
        **{k: config_7b[k] for k in CLES_GARDES_7B},
        "modules_repris": dict(MODULES_REPRIS),
        "lancement": {"go_origine": GO_ORIGINE, "go_admis": [GO_ORIGINE], "plafond_usd": PLAFOND_USD, "compte_rendu_usd": 72,
                      "dernier_jour_creation": DERNIER_JOUR_CREATION,
                      "carte": {"course": {"nom": "A100 SXM4 80 Go", "nom_offre": "A100 SXM4", "memoire_carte_min_mo": 80000,
                                           "prix_max_usd_h": 1.3}},
                      "offre": {"coeurs_effectifs_min": 16, "disque_min_go": 300, "etiquette": "dose-reponse-v1",
                                "memoire_vive_min_mo": 128000, "stockage_max_usd_h": 0.10, "telechargement_go_prevu": 40,
                                "telechargement_max_usd_go": 0.05}},
        "designation_critere_3": designation,
        "source_des_reglages": {"chemin": CONFIG_7B[0], "sha256": CONFIG_7B[1]},
    }


def charger_config_7b(racine: Path) -> dict:
    return json.loads(_fichier(racine, {"chemin": CONFIG_7B[0], "sha256": CONFIG_7B[1]},
                               "configuration de l'organisme à adaptateur").read_text(encoding="utf-8"))


def exiger_config(config: dict, racine: Path) -> None:
    """CL-05 : la configuration égale, clé pour clé, celle que reconstruit `configuration()` à partir de ses seules entrées
    libres ; puis les contrôles de la v1 (réglages, agent, texte, empreintes, offre). Aucun repli."""
    try:
        attendue = configuration(config["banque"]["chemin"], config["banque"]["sha256"], config["commit_code"],
                                 charger_config_7b(racine), config["piece_jointe"]["chemin"], config.get("designation_critere_3"))
    except (KeyError, TypeError) as e:
        raise GardeArret(f"configuration illisible ({e.__class__.__name__} : {e})") from None
    if config != attendue:
        ecarts = sorted(k for k in set(config) | set(attendue) if config.get(k) != attendue.get(k))
        raise GardeArret(f"configuration ≠ configuration reconstruite (clés {ecarts}) : aucune création")
    if not re.fullmatch(r"[0-9a-f]{40}", str(config["commit_code"])):
        raise GardeArret("commit_code : 40 caractères hexadécimaux")
    _exiger_config_v1(config)


def _exiger_config_v1(config: dict) -> None:
    """Réglages et constantes de la configuration égaux à ceux du texte scellé ; aucun repli."""
    for k, v in REGLAGES.items():
        if config.get("reglages", {}).get(k) != v:
            raise GardeArret(f"réglage {k} : {config.get('reglages', {}).get(k)!r} ≠ {v!r} (texte scellé)")
    for k, v in AGENT.items():
        if config.get("agent", {}).get(k) != v:
            raise GardeArret(f"agent : {k} {config.get('agent', {}).get(k)!r} ≠ {v!r} (aucun changement de modèle)")
    if config.get("prereg") != {"chemin": PREREG, "sha256": PREREG_SHA256}:
        raise GardeArret("configuration : texte scellé autre que celui de la course")
    if config.get("piece_jointe", {}).get("sha256") != PIECE_JOINTE_SHA256:
        raise GardeArret("configuration : empreinte de la pièce jointe autre que celle du texte scellé")
    if config.get("consignes_premier_test", {}).get("sha256") != PREMIER_TEST_SHA256:
        raise GardeArret("configuration : empreinte des textes du premier test autre que celle du texte scellé")
    if config.get("modules_repris") != MODULES_REPRIS:
        raise GardeArret("configuration : modules repris autres que ceux de l'en-tête du texte scellé")
    if config.get("mode") not in ("reel", "jouet"):
        raise GardeArret(f"mode {config.get('mode')!r} : reel ou jouet")
    exiger_offre(config)


def exiger_offre(config: dict) -> dict:
    """Bornes de l'offre et plafond de la configuration (plan, point 11 ; devis) ; une configuration plus large est refusée."""
    l = config.get("lancement")
    if not isinstance(l, dict):
        raise GardeArret("configuration sans section « lancement »")
    if l.get("go_origine") != GO_ORIGINE or l.get("plafond_usd") != PLAFOND_USD:
        raise GardeArret(f"lancement : GO {l.get('go_origine')!r} et plafond {l.get('plafond_usd')!r} ≠ {GO_ORIGINE}, {PLAFOND_USD} USD")
    if set(l.get("carte", {})) != {"course"}:
        raise GardeArret("lancement : une seule carte, « course » (aucune relance sur une carte plus chère)")
    c, o = l["carte"]["course"], l.get("offre", {})
    if c.get("nom_offre") != OFFRE["carte"]["nom_offre"]:
        raise GardeArret(f"carte {c.get('nom_offre')!r} ≠ {OFFRE['carte']['nom_offre']}")
    if not (isinstance(c.get("memoire_carte_min_mo"), (int, float)) and c["memoire_carte_min_mo"] >= OFFRE["carte"]["memoire_carte_min_mo"]):
        raise GardeArret("mémoire de la carte sous 80 Go")
    if not (isinstance(c.get("prix_max_usd_h"), (int, float)) and 0 < c["prix_max_usd_h"] <= OFFRE["carte"]["prix_max_usd_h"]):
        raise GardeArret(f"prix maximal de la carte {c.get('prix_max_usd_h')!r} hors de ]0 ; 1,30] USD de l'heure")
    for k in ("coeurs_effectifs_min", "memoire_vive_min_mo", "disque_min_go"):
        if not (isinstance(o.get(k), (int, float)) and o[k] >= OFFRE["offre"][k]):
            raise GardeArret(f"offre : {k} {o.get(k)!r} sous {OFFRE['offre'][k]}")
    for k in ("stockage_max_usd_h", "telechargement_max_usd_go"):
        if not (isinstance(o.get(k), (int, float)) and 0 <= o[k] <= OFFRE["offre"][k]):
            raise GardeArret(f"offre : {k} {o.get(k)!r} au-delà de {OFFRE['offre'][k]}")
    return l


def exiger_offre_lue(offre: dict, config: dict) -> dict:
    """Une offre relue dans la liste de l'outil de location (champs de vastai) respecte les bornes de la configuration."""
    l = exiger_offre(config)
    c, o = l["carte"]["course"], l["offre"]
    faute = []
    if str(offre.get("gpu_name", "")).replace("_", " ") != c["nom_offre"]:
        faute.append(f"carte {offre.get('gpu_name')!r}")
    if int(offre.get("num_gpus", 0)) != 1:
        faute.append(f"{offre.get('num_gpus')} cartes")
    if float(offre.get("gpu_ram", 0)) < c["memoire_carte_min_mo"]:
        faute.append(f"mémoire de carte {offre.get('gpu_ram')}")
    if float(offre.get("cpu_ram", 0)) < o["memoire_vive_min_mo"]:
        faute.append(f"mémoire vive {offre.get('cpu_ram')}")
    if float(offre.get("cpu_cores_effective", 0)) < o["coeurs_effectifs_min"]:
        faute.append(f"cœurs {offre.get('cpu_cores_effective')}")
    if float(offre.get("disk_space", 0)) < o["disque_min_go"]:
        faute.append(f"disque {offre.get('disk_space')}")
    prix_carte = float(offre.get("dph_total", 1e9)) - float(offre.get("storage_total_cost", 0))
    if prix_carte > c["prix_max_usd_h"]:
        faute.append(f"prix de la carte {prix_carte:.3f}")
    if float(offre.get("storage_total_cost", 1e9)) > o["stockage_max_usd_h"]:
        faute.append(f"stockage {offre.get('storage_total_cost')}")
    if float(offre.get("inet_down_cost", 1e9)) > o["telechargement_max_usd_go"]:
        faute.append(f"téléchargement {offre.get('inet_down_cost')}")
    if faute:
        raise GardeArret("offre hors des bornes du point 11 : " + ", ".join(faute) + " : aucune création")
    return {"prix_carte_usd_h": prix_carte, "conforme": True}


def identifiant_sans_version(identifiant: str) -> str:
    return _VERSION.sub("", str(identifiant))


def controler_banque(racine: Path, config: dict) -> dict:
    """Banque de la course : 64 tâches, aucune des 96, aucun rang inférieur à 125 (plan, point 1, contrôle avant dépense)."""
    racine = Path(racine)
    banque = charger_taches(_fichier(racine, config.get("banque"), "banque de tâches"))
    ids = [t["identifiant"] for t in banque]
    if len(ids) != N_TACHES:
        raise GardeArret(f"banque : {len(ids)} tâches, {N_TACHES} exigées : aucune création")
    initiales = set()
    for chemin, sha in BANQUE_INITIALE:
        for t in charger_taches(_fichier(racine, {"chemin": chemin, "sha256": sha}, f"banque initiale {Path(chemin).name}")):
            initiales.add(identifiant_sans_version(t["identifiant"]))
    if len(initiales) != N_BANQUE_INITIALE:
        raise GardeArret(f"banque initiale : {len(initiales)} identifiants, {N_BANQUE_INITIALE} attendus")
    communes = sorted(i for i in ids if identifiant_sans_version(i) in initiales)
    if communes:
        raise GardeArret(f"banque : tâche(s) de la banque initiale : {communes[:5]} : aucune création")
    tirage = json.loads(_fichier(racine, {"chemin": TIRAGE[0], "sha256": TIRAGE[1]}, "tirage de T0.5").read_text(encoding="utf-8"))
    ordre = [identifiant_sans_version(x) for x in tirage["resultat"]["ordre"]]
    rang = {x: k for k, x in enumerate(ordre)}
    absents = sorted(i for i in ids if identifiant_sans_version(i) not in rang)
    if absents:
        raise GardeArret(f"banque : identifiant(s) absent(s) du tirage scellé : {absents[:5]} : aucune création")
    bas = sorted((rang[identifiant_sans_version(i)], i) for i in ids if rang[identifiant_sans_version(i)] < RANG_MIN)
    if bas:
        raise GardeArret(f"banque : papier(s) de rang inférieur à {RANG_MIN} : {bas[:5]} : aucune création")
    return {"taches": len(ids), "rang_min": min(rang[identifiant_sans_version(i)] for i in ids),
            "rang_max": max(rang[identifiant_sans_version(i)] for i in ids), "banque_initiale": len(initiales),
            "sha256": config["banque"]["sha256"]}


def controler_modules(racine: Path) -> dict:
    for chemin, sha in MODULES_REPRIS.items():
        lu = hashlib.sha256((Path(racine) / chemin).read_bytes()).hexdigest()
        if lu != sha:
            raise GardeArret(f"module repris {chemin} : empreinte {lu[:12]} ≠ {sha[:12]} (texte scellé, en-tête) : aucune création")
    return {"modules": len(MODULES_REPRIS)}


def lignes_registre(registre: Path) -> dict:
    sortie = {}
    for l in Path(registre).read_text(encoding="utf-8").splitlines():
        m = _LIGNE_REGISTRE.match(l)
        if m:
            sortie.setdefault(m["id"], []).append(l)
    return sortie


def controler_registre(racine: Path, config: dict) -> dict:
    """Lignes du registre des scellements exigées avant toute création (« Liste d'arrêt », première puce)."""
    reg = lignes_registre(Path(racine) / "registres" / "scellements-v1.md")
    for nom in (LIGNE_BANQUE, LIGNE_CODE):
        if nom not in reg:
            raise GardeArret(f"ligne {nom} absente de registres/scellements-v1.md : aucune création")
    if not any(config["banque"]["sha256"] in l for l in reg[LIGNE_BANQUE]):
        raise GardeArret(f"ligne {LIGNE_BANQUE} : empreinte de la banque {config['banque']['sha256'][:12]} non citée")
    if not any(str(config.get("commit_code")) in l for l in reg[LIGNE_CODE]):
        raise GardeArret(f"ligne {LIGNE_CODE} : commit du code {str(config.get('commit_code'))[:12]} non cité (CL-06) : aucune création")
    d = config.get("designation_critere_3")
    exigees = []
    if d is not None:
        _fichier(racine, d, "texte de désignation de la course pour le critère 3")
        exigees = list(d.get("lignes_registre", []))
        manquantes = [x for x in exigees if x not in reg]
        if manquantes:
            raise GardeArret(f"lignes exigées par le texte de désignation absentes : {manquantes} : aucune création")
    return {"lignes": [LIGNE_BANQUE, LIGNE_CODE] + exigees}


def exiger_calendrier(jour: str) -> str:
    """CL-11 : aucune création après le dernier jour de création du devis (12 décembre 2026)."""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(jour)) or str(jour) > DERNIER_JOUR_CREATION:
        raise GardeArret(f"jour {jour} au-delà du dernier jour de création {DERNIER_JOUR_CREATION} (devis) : aucune création")
    return str(jour)


def controler_textes_avant_creation(racine: Path, config: dict, tok) -> dict:
    """CL-04, avant toute création : forme stricte de la pièce jointe (sous son empreinte) et rapport des longueurs en
    jetons des huit consignes (tokeniseur de l'agent, sans modèle) ; rien n'est affiché, seuls des comptes sont rendus."""
    pj = charger_piece_jointe(Path(racine) / config["piece_jointe"]["chemin"], config["piece_jointe"]["sha256"])
    r = longueurs_en_jetons(tok, {c: pj[c] for c in pj if c != "sha256"})
    if not r["conforme"]:
        raise GardeArret(f"rapport des longueurs en jetons des huit consignes {r['rapport']:.4f} > 1,15 : aucune création")
    return {"forme": "conforme", "rapport": round(r["rapport"], 4), "longueur_min": min(r["longueurs"].values()),
            "longueur_max": max(r["longueurs"].values())}


def charger_tokeniseur_agent(config: dict):
    """Tokeniseur seul de l'agent, à la révision figée (aucun poids chargé)."""
    from transformers import AutoTokenizer
    return AutoTokenizer.from_pretrained(config["agent"]["modele"], revision=config["agent"]["revision"])


def controles_avant_depense(racine: Path, config: dict, registre: bool = True) -> dict:
    """Tous les contrôles sur fichiers ; `registre=False` seulement pour éprouver le code avant l'inscription des lignes."""
    racine = Path(racine)
    exiger_config(config, racine)
    sha = exiger_prereg_scelle(racine / PREREG)
    if sha != PREREG_SHA256:
        raise GardeArret(f"texte scellé : empreinte {sha[:12]} ≠ {PREREG_SHA256[:12]}")
    _fichier(racine, config["piece_jointe"], "pièce jointe des textes privés")
    _fichier(racine, config["consignes_premier_test"], "textes du premier test")
    sortie = {"prereg_sha256": sha, "entropie": str(entropie_racine(sha)), "modules": controler_modules(racine),
              "banque": controler_banque(racine, config), "offre": "conforme", "config_sha256": empreinte_config(config)}
    sortie["registre"] = controler_registre(racine, config) if registre else "non contrôlé (épreuve du code)"
    return sortie
