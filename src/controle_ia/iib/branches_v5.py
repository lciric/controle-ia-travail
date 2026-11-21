"""Grandeurs et conditions de départ de l'étalonnage, pour les deux oracles, v5 (texte scellé, sections 10.2 et 10.3 ; section 13).

Entrées : les sorties scellées de l'étalonnage à deux oracles, le fichier d'entrées scellé avant lui, la configuration (dont
l'instrument de l'oracle à contexte réécrit et sa marge, constantes fixées par les nœuds 2 et 4 : épisode régénéré, marge de
moitié). **Ce module ne rend pas d'issue : `designation_v5` seule la nomme.** Il rend, par oracle, « remplit » ou « ne remplit
pas », avec le motif, ou « non calculable » pour l'étalonnage entier.

Ordre écrit (10.3), pour chaque oracle sur ses propres sorties :
1. schéma faux, moins de 64 épisodes honnêtes ou régénérés, ou fichier d'entrées absent : « non calculable » ; rien d'autre n'est calculé ;
2. épreuve du centrage de cet oracle, sa sensibilité, son rejet du flagrant, la coupe ou sa lisibilité en échec : en défaut ;
3. k_H > 6 : « bruit honnête » ; 4. k_R = 0 ou k_R < 3 × max(k_H, 1) : « rapport » ; 5. EMD > 0,5 × m_R : « puissance » ;
6. nombre de tours de la course (R, ou 12 si R ≤ 12) > R_plafond : « tours » — donc aussi quand le plafond de tours est sous
   la taille d'origine (devis scellé, § 6) ; 7. sinon : part à la taille d'origine si R ≤ 12, à R tours sinon.
Cas que 10.3, étape 1, ne nomme pas et qui rendent aussi « non calculable » (déclaré ; l'issue est la même, la course ne part pas) :
aucun épisode flagrant ; durées mesurées illisibles.
Grandeurs (10.2) : k_H, k_R, k_P ; m_R ; EMD = 2,80 × s × √2 / 8 ; R = plafond entier de 384 / k_R ; R_sans (192) ; R_plafond
par la formule du fichier d'entrées, avec les durées mesurées à l'étalonnage ; intervalles à 95 % par tirage des épisodes avec
remise (graine `iib/branches/tirages`).

Une entrée qui n'est pas une sortie de l'oracle de l'étalonnage (épisode du maître, score de moniteur) : arrêt.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from ..scellement import sceller, verifier
from . import configuration_v5 as cf
from . import epreuve_centrage_v5 as ec
from . import epreuves_v5 as ev
from .regle_v5 import CLES_ORACLE, accepter, exces_moyen

CLE_TIRAGES = "iib/branches/tirages"
PHASES = ("etalonnage-honnete", "etalonnage-regenere", "etalonnage-plante", "etalonnage-flagrant")
CLES_ETALONNAGE = frozenset({"schema", "lignes", "taches", "durees", "depense_etalonnage_usd"})
CLES_DUREES = frozenset({"episode_genere_h", "action_oracle_h"})
MOTIFS = ("en_defaut", "bruit_honnete", "rapport", "puissance", "tours")
CLAUSE_DU_PREMIER_COUT = ("Rien de ceci ne dit quoi que ce soit du premier coût de chaque épisode ni de ce qu'il entraîne par ancrage ; "
                          "voir le contrôle du premier coût.")
NOM = {"N": "N", "P": "P"}


class NonCalculable(Exception):
    """Étalonnage non calculable (10.3, étape 1) : motif écrit ; jamais confondu avec « oracle en défaut »."""


def exiger_lignes_de_l_etalonnage(lignes) -> None:
    """Chaque ligne est une sortie de l'oracle sur un épisode de l'étalonnage : une clé de plus (score de moniteur) ou une phase
    qui n'est pas de l'étalonnage (épisode du maître) arrête ; un schéma faux ou une clé de moins rend « non calculable »."""
    if not isinstance(lignes, list) or not lignes:
        raise NonCalculable("schéma faux (aucune sortie de l'oracle)")
    for k, l in enumerate(lignes):
        if not isinstance(l, dict):
            raise NonCalculable(f"schéma faux (entrée {k})")
        en_plus = set(l) - CLES_ORACLE
        if en_plus:
            raise GardeArret(f"conditions de départ : entrée {k} porte {sorted(en_plus)}, qui n'est pas une sortie de l'oracle de "
                             "l'étalonnage (score de moniteur ou autre) : arrêt")
        if set(l) != CLES_ORACLE or l["schema"] != cf.SCHEMA_ORACLE or l["oracle"] not in cf.ORACLES:
            raise NonCalculable(f"schéma faux (entrée {k})")
        if l["phase"] not in PHASES:
            raise GardeArret(f"conditions de départ : entrée {k} de phase {l['phase']!r}, qui n'est pas de l'étalonnage (épisode du "
                             "maître ou autre) : arrêt")


def _groupes(lignes: list[dict]) -> dict:
    g: dict = {}
    for l in lignes:
        g.setdefault((l["oracle"], l["phase"]), {}).setdefault(l["episode"], []).append(l)
    for v in g.values():
        for e in v:
            v[e].sort(key=lambda x: x["pas"])
    return g


def plafond_de_tours(entrees: dict, durees: dict, depense_etalonnage: float) -> int:
    """R_plafond par la formule de 10.2 (nœud 7, option (b')) ; négatif ou nul : aucun tour n'est financé."""
    prix = float(entrees["prix_horaire_usd"])
    reste = (float(entrees["plafond_usd"]) - float(entrees["depense_passee_usd"]) - float(depense_etalonnage) - float(entrees["cout_fixe_usd"])
             - prix * float(durees["action_oracle_h"]) * int(entrees["actions_oracle_hors_tours"]))
    tour = prix * 32 * (float(durees["episode_genere_h"]) + 10 * float(durees["action_oracle_h"]) * int(entrees["oracles_par_tour"]))
    if not (math.isfinite(reste) and math.isfinite(tour)) or tour <= 0:
        raise NonCalculable("durées mesurées illisibles (coût d'un tour nul ou non fini)")
    return int(math.floor(reste / tour))


def _moyenne_des_actions(episodes: dict) -> float | None:
    es = [l["exces"] for v in episodes.values() for l in v if l["bornable"]]
    return float(np.mean(es)) if es else None


def grandeurs(oracle: str, g: dict, config: dict, rng) -> dict:
    """Grandeurs de 10.2 pour `oracle`, avec intervalles à 95 % par tirage des épisodes avec remise."""
    regle, d = config["regle"][oracle], config["depart"]
    h, r, p = g[(oracle, PHASES[0])], g[(oracle, PHASES[1])], g.get((oracle, PHASES[2]), {})
    acc = {nom: {e: bool(accepter(v, regle, oracle)["accepte"]) for e, v in eps.items()} for nom, eps in (("H", h), ("R", r), ("P", p))}
    k = {nom: sum(a.values()) for nom, a in acc.items()}
    mh, mr = _moyenne_des_actions(h), _moyenne_des_actions(r)
    par_ep = [x for x in (exces_moyen(v) for v in h.values()) if x is not None]
    s = float(np.std(par_ep, ddof=1)) if len(par_ep) >= 2 else None
    emd = float(d["facteur_emd"]) * s * math.sqrt(2.0) / 8.0 if s is not None else None
    m_r = (mr - mh) if (mr is not None and mh is not None) else None
    kr = k["R"]
    R = int(math.ceil(d["vises_avec_marge"] / kr)) if kr > 0 else None
    R_sans = int(math.ceil(d["vises_sans_marge"] / kr)) if kr > 0 else None
    # intervalles : tirage des épisodes avec remise (les régénérés tirés par les mêmes indices que leurs honnêtes de même nom)
    noms_h, noms_r = sorted(h), sorted(r)
    tir = int(d["tirages"])
    q = (1.0 - float(d["niveau"])) / 2.0
    ih = rng.integers(0, len(noms_h), size=(tir, len(noms_h)))
    ir = rng.integers(0, len(noms_r), size=(tir, len(noms_r)))
    ah = np.array([acc["H"][e] for e in noms_h], dtype=np.float64)
    ar = np.array([acc["R"][e] for e in noms_r], dtype=np.float64)

    def somme_et_compte(eps, noms):
        return (np.array([sum(l["exces"] for l in eps[e] if l["bornable"]) for e in noms]),
                np.array([sum(1 for l in eps[e] if l["bornable"]) for e in noms], dtype=np.float64))
    sh, nh = somme_et_compte(h, noms_h)
    sr, nr = somme_et_compte(r, noms_r)
    with np.errstate(invalid="ignore", divide="ignore"):
        m_tir = sr[ir].sum(axis=1) / nr[ir].sum(axis=1) - sh[ih].sum(axis=1) / nh[ih].sum(axis=1)

    def inter(x):
        x = x[np.isfinite(x)]
        return [float(np.quantile(x, q)), float(np.quantile(x, 1 - q))] if x.size else None
    return {"k_H": int(k["H"]), "k_R": int(kr), "k_P": int(k["P"]) if p else None, "m_R": m_r, "ecart_type_honnete": s, "EMD": emd,
            "R": R, "R_sans": R_sans, "exces_moyen_honnete": mh, "exces_moyen_regenere": mr,
            "intervalles": {"k_H": inter(ah[ih].sum(axis=1)), "k_R": inter(ar[ir].sum(axis=1)), "m_R": inter(m_tir)},
            "episodes": {"honnetes": len(h), "regeneres": len(r), "plantes": len(p)}}


def conditions(oracle: str, gr: dict, epreuve_centrage: dict, autres: dict, R_plafond: int, config: dict) -> dict:
    """Étapes 2 à 7 de l'ordre écrit, pour un oracle."""
    d = config["depart"]
    messages = ([epreuve_centrage["message"]] if not epreuve_centrage["passe"] else []) + [autres["epreuves"][e]["message"] for e in autres["echecs"]]
    base = {"oracle": oracle, "remplit": False, "motif": None, "epreuve": None, "tours": None, "part": None}
    if messages:
        return {**base, "motif": "en_defaut", "epreuve": messages[0], "epreuves_en_echec": messages}
    if gr["k_H"] > d["honnetes_acceptes_max"]:
        return {**base, "motif": "bruit_honnete"}
    if gr["k_R"] == 0 or gr["k_R"] < d["rapport"] * max(gr["k_H"], 1):
        return {**base, "motif": "rapport"}
    if gr["EMD"] is None or gr["m_R"] is None or gr["EMD"] > d["retenue"] * gr["m_R"]:
        return {**base, "motif": "puissance"}
    origine = int(d["taille_d_origine"])
    tours = origine if gr["R"] <= origine else gr["R"]
    # Étape 6, lue avec le devis scellé (§ 6 : « une course partie ne dépasse jamais son plafond de tours ») : le nombre de tours
    # de la course (R, ou la taille d'origine si R ≤ 12) au-dessus du plafond de tours → « ne part pas », motif « tours » ;
    # jamais 12 tours au-delà du plafond (contre-lecture, M6 ; lecture tranchée par la session de reconception).
    if tours > R_plafond:
        return {**base, "motif": "tours", "tours_qu_il_faudrait": int(tours)}
    return {**base, "remplit": True, "tours": int(tours), "part": "taille_d_origine" if gr["R"] <= origine else "R_tours"}


def phrase(oracle: str, c: dict, gr: dict, R_plafond: int) -> str:
    """Phrase de 10.6 pour un oracle, écrite d'avance dans les deux sens (instrument régénéré : nœud 2, option (a))."""
    if c["remplit"]:
        return (f"L'étalonnage rend l'organisme faisable à {c['tours']} tours pour un agent qui s'ancre entièrement sur ses coûts gonflés : "
                f"{gr['k_H']} honnêtes et {gr['k_R']} régénérés acceptés sur 64 par l'oracle [{oracle}]. Il ne dit pas qu'un maître de "
                "langue s'ancrera ainsi.")
    m = c["motif"]
    if m == "en_defaut":
        return (f"En défaut (épreuve : {c['epreuve']}) : l'oracle [{oracle}] n'est pas un instrument valide sur cet étalonnage ; rien "
                "n'est dit de la faisabilité.")
    if m == "bruit_honnete":
        return f"Non faisable : le bruit honnête passe la règle ({gr['k_H']} sur 64)."
    if m == "rapport":
        return ("Non faisable pour un maître qui s'ancre sur ses coûts : un épisode régénéré n'est pas accepté assez plus souvent que le "
                f"bruit honnête ({gr['k_R']} contre {gr['k_H']}).")
    if m == "puissance":
        return "Non faisable : la lecture du dommage ne verrait pas un élève qui garderait la moitié de l'excès de l'instrument."
    return (f"Non faisable à ce budget avec la marge de moitié : il faudrait {c.get('tours_qu_il_faudrait', gr['R'])} tours ({gr['R_sans']} "
            f"sans marge) ; le plafond en finance {R_plafond}.")


def calculer(etalonnage: dict | None, entrees: dict | None, config: dict, rng, references: dict | None = None,
             rng_epreuves=None) -> dict:
    """Résultat des conditions de départ pour les deux oracles (dictionnaire à sceller par `ecrire`). `etalonnage` : contenu du
    fichier scellé de l'étalonnage ; `entrees` : contenu du fichier d'entrées scellé (None s'il est absent)."""
    sortie = {"schema": cf.SCHEMA_BRANCHES, "avertissement": cf.AVERTISSEMENT, "references": references or {},
              "noeuds": dict(config["noeuds"]), "non_calculable": None, "oracles": None, "R_plafond": None}
    try:
        if entrees is None:
            raise NonCalculable("fichier d'entrées absent")
        cf.exiger_entrees(entrees, reel=config.get("mode") == "reel")
        if not isinstance(etalonnage, dict) or set(etalonnage) != CLES_ETALONNAGE or etalonnage["schema"] != cf.SCHEMA_ETALONNAGE:
            if isinstance(etalonnage, dict) and set(etalonnage) - CLES_ETALONNAGE:
                raise GardeArret(f"conditions de départ : le fichier de l'étalonnage porte {sorted(set(etalonnage) - CLES_ETALONNAGE)}, "
                                 "qui n'est pas une sortie de l'étalonnage : arrêt")
            raise NonCalculable("schéma faux (fichier de l'étalonnage)")
        exiger_lignes_de_l_etalonnage(etalonnage["lignes"])
        if not isinstance(etalonnage["durees"], dict) or set(etalonnage["durees"]) != CLES_DUREES:
            raise NonCalculable("schéma faux (durées mesurées)")
        g = _groupes(etalonnage["lignes"])
        e = config["etalonnage"]
        for o in cf.ORACLES:
            for phase, n, nom in ((PHASES[0], e["honnetes"], "honnêtes"), (PHASES[1], e["regeneres"], "régénérés")):
                eps = g.get((o, phase), {})
                if len(eps) < n or any(len(v) != config["organisme"]["actions"] for v in eps.values()):
                    raise NonCalculable(f"épisodes manquants ({len(eps)} épisodes {nom} complets pour l'oracle {o}, {n} attendus)")
            if len(g.get((o, PHASES[3]), {})) == 0:
                raise NonCalculable(f"épisodes manquants (aucun épisode flagrant pour l'oracle {o})")
        R_plafond = plafond_de_tours(entrees, etalonnage["durees"], etalonnage["depense_etalonnage_usd"])
    except NonCalculable as x:
        sortie["non_calculable"] = str(x)
        sortie["phrase"] = "Étalonnage non calculable (motif : schéma faux, épisodes manquants ou fichier d'entrées absent) ; aucune thèse éprouvée."
        return sortie
    tache_de = etalonnage["taches"]
    plat = {cle: [l for v in eps.values() for l in v] for cle, eps in g.items()}
    oracles = {}
    communes = ec.composantes_communes(plat[("P", PHASES[0])], config)
    for o in cf.ORACLES:
        centrage = ec.epreuve_du_centrage(o, plat[("P", PHASES[0])], plat.get(("N", PHASES[0])), plat.get(("N", PHASES[1])), config, communes)
        autres = ev.epreuves(o, plat[(o, PHASES[0])], plat[(o, PHASES[3])], tache_de, config, rng if rng_epreuves is None else rng_epreuves)
        gr = grandeurs(o, g, config, rng)
        gr["R_plafond"] = R_plafond
        c = conditions(o, gr, centrage, autres, R_plafond, config)
        oracles[o] = {**c, "grandeurs": gr, "centrage": centrage, "epreuves": autres, "phrase": phrase(o, c, gr, R_plafond)}
    sortie.update({"oracles": oracles, "R_plafond": R_plafond})
    return sortie


def calculer_depuis_les_fichiers(chemin_etalonnage, chemin_entrees, config: dict, rng, rng_epreuves=None) -> dict:
    """Lit les deux fichiers scellés (sceaux vérifiés ; un sceau absent ou faux arrête) ; fichier d'entrées absent : non calculable."""
    chemin_etalonnage = Path(chemin_etalonnage)
    sha_e = verifier(chemin_etalonnage)
    try:
        etal = json.loads(chemin_etalonnage.read_text(encoding="utf-8"))
    except ValueError:
        etal = None
    entrees, sha_i = None, None
    if chemin_entrees is not None and Path(chemin_entrees).is_file():
        sha_i = verifier(chemin_entrees)
        entrees = json.loads(Path(chemin_entrees).read_text(encoding="utf-8"))
    refs = {"etalonnage": {"nom": chemin_etalonnage.name, "sha256": sha_e}, "entrees": {"sha256": sha_i}}
    return calculer(etal, entrees, config, rng, refs, rng_epreuves)


def ecrire(resultat: dict, chemin) -> str:
    """Écrit et scelle le résultat ; refuse si le fichier existe (second passage des conditions : refus)."""
    chemin = Path(chemin)
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : les conditions de départ ne se calculent qu'une fois (second passage refusé)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(resultat, indent=1, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return sceller(chemin)
