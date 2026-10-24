"""Le génome de l'essaim : son organisation, ses règles d'apprentissage, son signal de récompense interne, ses
boucles — tout ce que l'essaim décide lui-même, génération après génération.

Ce que faisait Gemini (B-05, B-19, B-22) : un « génome » JSON demandé au modèle ; sur échec d'analyse, le schéma
d'exemple codé en dur était pris pour un génome (« … », `ALPHA_MONO_1`, températures d'exemple) ; l'architecture
finale était une concaténation de textes ; un point de reprise chargeait n'importe quel JSON avec deux listes.

Ici :
- le génome est un objet validé contre un schéma strict ; un espace réservé (`...`, `$$...$$`, identifiants
  d'exemple) est une erreur ; un génome invalide n'est jamais remplacé par un exemple : l'étape rend un statut ;
- l'essaim choisit ses règles dans des **menus de règles réellement implémentées** (routage, mise à jour,
  récompense, sélection, boucles, mémoire) et en fixe les paramètres ; il peut proposer une règle hors menu : elle
  est consignée comme proposition pour Lazar (nœud « modifier le programme ») et n'est pas exécutée (B-14) ;
- chaque génome porte sa génération, son parent, son auteur (espèce, appel) et une justification ; les différences
  entre générations sont listées.
"""
from __future__ import annotations

import copy
import json
import re

from .especes import ESPECES, famille_de

ROLES = ("exploration", "attaque", "verification", "synthese")

MENUS = {
    "routage.regle": ["epsilon-glouton", "softmax", "uniforme"],
    "apprentissage.regle_mise_a_jour": ["moyenne-incrementale", "exponentielle"],
    "apprentissage.selection_generation": ["garder-si-meilleur", "garder-toujours", "tournoi"],
    "apprentissage.ingestion.statuts_admis": ["verifie-code", "verifie-verificateur", "non-verifie"],
    "recompense.forme": ["anti-echec-unilaterale", "brier", "comptage-verifie", "nouveaute-ponderee"],
}

BORNES = {
    "routage.epsilon_min": (0.0, 1.0), "routage.temperature": (0.01, 5.0),
    "apprentissage.taux": (0.01, 1.0), "apprentissage.ingestion.seuil_couvert": (0.05, 0.9),
    "recompense.gamma_cout": (0.0, 1.0), "recompense.poids_nouveaute": (0.0, 1.0),
    "boucles.locales_max": (1, 8), "boucles.globales_max": (1, 6), "boucles.alpha_e": (0.001, 0.2),
    "boucles.puissance_min": (0.3, 0.95), "boucles.n_canaris": (8, 14),
    "boucles.mitose.cellules_min": (2, 8), "boucles.mitose.cellules_max": (3, 16), "boucles.mitose.k_arret": (1, 4),
    "boucles.mitose.quantile_bruit": (0.5, 0.99),
    "memoire.r_max": (2, 12),
}

ESPACES_RESERVES = re.compile(r"^\s*(\.\.\.|…|\$\$\.\.\.\$\$|ALPHA_MONO_\d|ALPHA_HYBRIDE_\d|MONO_\d|HYBRIDE_\d|"
                              r"Concept math[ée]matique \d.*|Mod[èe]le \d|\[.*\])\s*$", re.I)


def genome_base() -> dict:
    """Génome de référence, **non adaptatif**, pour le bras témoin seulement : il ne change jamais de génération."""
    return {
        "version": 1, "generation": 0, "parent": None, "auteur": {"etape": "base", "espece": None, "id_appel": None},
        "organisation": {
            "castes": [
                {"id": "explo-fable", "espece": "CLAUDE_FABLE_5_1", "role": "exploration", "effectif": 1, "cible": "exploration libre", "angles": [0.25, 0.75]},
                {"id": "explo-argon", "espece": "GEMINI_ARGON", "role": "exploration", "effectif": 1, "cible": "exploration libre", "angles": [0.5]},
                {"id": "att-opus", "espece": "CLAUDE_OPUS_5_5", "role": "attaque", "effectif": 1, "cible": "failles", "angles": [0.5]},
                {"id": "att-argon", "espece": "GEMINI_ARGON", "role": "attaque", "effectif": 1, "cible": "failles", "angles": [0.5]},
                {"id": "verif-argon", "espece": "GEMINI_ARGON", "role": "verification", "effectif": 1, "cible": "verdicts", "angles": [0.0]},
                {"id": "verif-opus", "espece": "CLAUDE_OPUS_5_5", "role": "verification", "effectif": 1, "cible": "verdicts", "angles": [0.0]},
                {"id": "synth-opus", "espece": "CLAUDE_OPUS_5_5", "role": "synthese", "effectif": 1, "cible": "synthèse", "angles": [0.0]},
            ],
            "hybrides": [],
        },
        "routage": {"regle": "uniforme", "epsilon_min": 0.05, "temperature": 0.5},
        "apprentissage": {"regle_mise_a_jour": "moyenne-incrementale", "taux": 0.3,
                          "ingestion": {"statuts_admis": ["verifie-code", "verifie-verificateur"], "seuil_couvert": 0.35},
                          "selection_generation": "garder-toujours"},
        "recompense": {"forme": "comptage-verifie", "gamma_cout": 0.0, "poids_nouveaute": 0.0},
        "boucles": {"locales_max": 2, "globales_max": 1, "alpha_e": 0.05, "puissance_min": 0.6, "n_canaris": 12,
                    "mitose": {"cellules_min": 3, "cellules_max": 6, "k_arret": 2, "quantile_bruit": 0.95}},
        "memoire": {"r_max": 6, "relevement_quadratique": False},
        "justification": "génome témoin fixe, écrit par l'humain ; jamais modifié par l'essaim",
    }


def _chemin(d: dict, chemin: str):
    cur = d
    for k in chemin.split("."):
        if not isinstance(cur, dict) or k not in cur:
            return None
        cur = cur[k]
    return cur


def _texte_reserve(x) -> bool:
    return isinstance(x, str) and (not x.strip() or bool(ESPACES_RESERVES.match(x)))


def valider(genome) -> list[str]:
    """Liste des problèmes ; vide si le génome est valide. Jamais de correction silencieuse."""
    p: list[str] = []
    if not isinstance(genome, dict):
        return ["le génome n'est pas un objet"]
    org = genome.get("organisation")
    if not isinstance(org, dict) or not isinstance(org.get("castes"), list):
        p.append("organisation.castes absente")
        castes = []
    else:
        castes = org["castes"]
    if len(castes) < 2:
        p.append("moins de deux castes")
    ids, roles, familles = set(), set(), set()
    for i, c in enumerate(castes):
        if not isinstance(c, dict):
            p.append(f"caste {i} : pas un objet"); continue
        cid = c.get("id")
        if not isinstance(cid, str) or _texte_reserve(cid):
            p.append(f"caste {i} : identifiant manquant ou réservé")
        elif cid in ids:
            p.append(f"caste {cid} : identifiant en double")
        ids.add(cid)
        if c.get("espece") not in ESPECES:
            p.append(f"caste {cid} : espèce inconnue {c.get('espece')!r}")
        else:
            familles.add(famille_de(c["espece"]))
        if c.get("role") not in ROLES:
            p.append(f"caste {cid} : rôle inconnu {c.get('role')!r}")
        else:
            roles.add(c["role"])
        eff = c.get("effectif")
        if not isinstance(eff, int) or not 1 <= eff <= 4:
            p.append(f"caste {cid} : effectif hors de [1, 4]")
        if _texte_reserve(c.get("cible")):
            p.append(f"caste {cid} : cible vide ou réservée")
        angles = c.get("angles")
        if not isinstance(angles, list) or not angles or not all(isinstance(a, (int, float)) and 0 <= a <= 1 for a in angles):
            p.append(f"caste {cid} : angles absents ou hors de [0, 1]")
    for r in ("exploration", "attaque", "verification", "synthese"):
        if r not in roles:
            p.append(f"aucune caste de rôle {r}")
    if len(familles) < 2:
        p.append("une seule famille de fournisseur parmi les castes (constat 39 : verdicts corrélés)")
    hyb = org.get("hybrides", []) if isinstance(org, dict) else []
    if not isinstance(hyb, list):
        p.append("organisation.hybrides n'est pas une liste")
    else:
        for h in hyb:
            if not isinstance(h, dict) or not isinstance(h.get("especes"), list) or len(h["especes"]) != 2 \
                    or any(e not in ESPECES for e in h["especes"]) or _texte_reserve(h.get("id")) or _texte_reserve(h.get("cible")):
                p.append(f"hybride invalide : {h!r}"[:120])
    for chemin, menu in MENUS.items():
        val = _chemin(genome, chemin)
        if chemin.endswith("statuts_admis"):
            if not isinstance(val, list) or not val or any(v not in menu for v in val):
                p.append(f"{chemin} : hors menu {menu}")
        elif val not in menu:
            p.append(f"{chemin} : {val!r} hors menu {menu}")
    for chemin, (lo, hi) in BORNES.items():
        val = _chemin(genome, chemin)
        if not isinstance(val, (int, float)) or isinstance(val, bool) or not lo <= val <= hi:
            p.append(f"{chemin} : {val!r} hors de [{lo}, {hi}]")
    if not isinstance(_chemin(genome, "memoire.relevement_quadratique"), bool):
        p.append("memoire.relevement_quadratique : booléen attendu")
    m = _chemin(genome, "boucles.mitose")
    if isinstance(m, dict) and isinstance(m.get("cellules_min"), int) and isinstance(m.get("cellules_max"), int) \
            and m["cellules_min"] > m["cellules_max"]:
        p.append("boucles.mitose : cellules_min > cellules_max")
    if _texte_reserve(genome.get("justification")):
        p.append("justification vide ou réservée")
    return p


def castes_par_role(genome: dict, role: str) -> list[dict]:
    return [c for c in genome["organisation"]["castes"] if c["role"] == role]


def especes_par_role(genome: dict, role: str) -> list[str]:
    return [c["espece"] for c in castes_par_role(genome, role)]


def differences(g1: dict, g2: dict, prefixe: str = "") -> list[str]:
    sortie = []
    cles = set(g1.keys()) | set(g2.keys()) if isinstance(g1, dict) and isinstance(g2, dict) else set()
    if not cles:
        return [prefixe] if g1 != g2 else []
    for k in sorted(cles):
        a, b = g1.get(k), g2.get(k)
        chemin = f"{prefixe}.{k}" if prefixe else k
        if isinstance(a, dict) and isinstance(b, dict):
            sortie += differences(a, b, chemin)
        elif a != b:
            sortie.append(chemin)
    return sortie


def menus_texte() -> str:
    lignes = ["Règles réellement implémentées (choisis et paramètre ; une règle hors menu est consignée comme "
              "proposition et n'est pas exécutée) :"]
    for k, v in MENUS.items():
        lignes.append(f"- {k} ∈ {v}")
    for k, (lo, hi) in BORNES.items():
        lignes.append(f"- {k} ∈ [{lo}, {hi}]")
    lignes.append(f"- caste.espece ∈ {sorted(ESPECES)} ; caste.role ∈ {list(ROLES)} ; au moins deux familles de "
                  "fournisseur ; au moins une caste par rôle.")
    return "\n".join(lignes)


def prompt_proposition(contexte: str, genome_courant: dict | None, historique_externe: list[dict],
                       connaissances: list[str], retours: list[str]) -> str:
    courant = json.dumps(genome_courant, ensure_ascii=False, indent=1) if genome_courant else "(aucun : première génération)"
    hist = "\n".join(f"- génération {h['generation']} : score externe {h['score']:.3f} ({h.get('verdict', '')})"
                     for h in historique_externe) or "- (aucun score encore)"
    conn = "\n".join(f"- {c}" for c in connaissances[:40]) or "- (aucune encore)"
    rets = "\n".join(f"- {r}" for r in retours) or "- (aucun)"
    squelette = json.dumps({k: v for k, v in genome_base().items() if k not in ("version", "generation", "parent", "auteur")},
                           ensure_ascii=False, indent=1)
    return (
        "Tu es l'étage M0 de l'essaim : tu décides toi-même l'organisation de l'essaim pour la prochaine génération, "
        "ses règles d'apprentissage, son signal de récompense interne, ses boucles locales et globales et les paramètres "
        "de sa mémoire. Le seul juge que tu ne contrôles pas est le score externe (tâches à vérité terrain que tu ne "
        "vois pas) : c'est lui qui dit si une génération est devenue plus compétente.\n\n"
        f"CONTEXTE DE LA MISSION :\n{contexte}\n\n"
        f"GÉNOME COURANT :\n{courant}\n\n"
        f"HISTORIQUE DU SCORE EXTERNE :\n{hist}\n\n"
        f"CONNAISSANCES VÉRIFIÉES ACQUISES :\n{conn}\n\n"
        f"RETOURS DU DERNIER CYCLE :\n{rets}\n\n"
        f"{menus_texte()}\n\n"
        "Propose le génome complet de la prochaine génération, avec une justification courte. Les valeurs doivent être "
        "concrètes (aucun « … »). Réponds par un seul bloc ```json … ``` ayant exactement la forme suivante :\n"
        f"```json\n{squelette}\n```"
    )


def proposition_vers_genome(d, parent: dict | None, generation: int, auteur: dict) -> tuple[dict | None, list[str]]:
    """Construit le génome de la génération suivante à partir d'une proposition analysée ; rend (génome, problèmes)."""
    if not isinstance(d, dict):
        return None, ["proposition illisible"]
    g = copy.deepcopy(d)
    g["version"] = (parent.get("version", 0) + 1) if parent else 1
    g["generation"] = int(generation)
    g["parent"] = f"v{parent['version']}" if parent else None
    g["auteur"] = dict(auteur)
    problemes = valider(g)
    return (g if not problemes else None), problemes
