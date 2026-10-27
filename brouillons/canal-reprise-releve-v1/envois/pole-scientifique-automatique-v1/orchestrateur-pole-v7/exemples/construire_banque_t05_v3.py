"""Banque de la couche 1, **v3** (v7, version 14 ; lignée conv-audit, 27 octobre 2026) : les épisodes réels de T0.5 et les
notations des juges, au format du monde sur banque, avec ce que la couche 1 bis, les contre-lectures et le collisionneur
demandaient :

- **trois parties par tâche** (toutes les instances d'une tâche du même côté), tirées par graine : calibrage (le prédicteur
  connu y est ajusté), **développement** (servi aux agents en phase exploratoire ; distinct du calibrage : point du
  collisionneur « proposeur enfichable » sur le « 0 sur 20 »), épreuve (jamais servie) ; parts par défaut ¼, ¼, ½ ;
- **témoins vrais établis** (constat C8 de la contre-lecture du socle : les témoins de la v2 étaient des copies de fiches
  de la population, 5 pour 4,35 attendus par hasard) : le chercheur mécanique (`pole/proposeurs_references.py`) est
  ajusté sur une moitié des tâches de développement (A) et **confirmé sur l'autre moitié (B)** — gain de vraisemblance
  logarithmique sur B contre la marginale de A d'au moins log(20) (le seuil du juge), aucune donnée d'épreuve lue ; seule
  une loi confirmée devient témoin vrai ; sa valeur de confirmation est consignée ;
- **témoins faux par permutation dans la tâche** (contrôle demandé pour P3 (ii)) : mêmes recherche et confirmation sur des
  issues **permutées entre les épisodes d'une même tâche** sur le développement — la dépendance de tâche est gardée, le lien
  trait → issue est détruit ; une loi qui passerait quand même la confirmation est un témoin faux (attendu : non promue
  sur l'épreuve) ; plus les témoins faux sur le trait de bruit (v2) ;
- énoncés **neutres** (aucun préfixe « Témoin ») ; le rôle est dans le champ `temoin`, privé.

Lecture seule des fichiers de `main` ; rien n'est relancé ; les empreintes des sources sont consignées dans la banque.
Les notations « complètes » de la couche 1 bis (b) se donnent par `--notations JUGE=CHEMIN` (répétable) ; à défaut, les
notations décisives de la v2. Toutes les passes de notation sont lues si `--toutes-les-passes` (sinon la première seule).

Usage : python -I -B exemples/construire_banque_t05_v3.py RACINE_MAIN SORTIE.json [--graine 20261027]
        [--notations 8B=diag/.../notations-8B.json ...] [--toutes-les-passes] [--temoins SORTIE-temoins.json]
"""

import argparse
import collections
import hashlib
import json
import math
import os
import random
import statistics
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))

from pole import selection_pari as sp  # noqa: E402
from pole.outils import ecrire_json_scelle, graine_derivee  # noqa: E402
from pole.proposeurs_references import propositions_mecaniques  # noqa: E402

EPISODES = "diag/20261012-105125-t05-pilote-reel/episodes.json"
NOTATIONS_V2 = {"8B": "diag/20261017-193648-t05-notations-reel/notations-8B-decisives.json",
                "3B": "diag/20261017-193648-t05-notations-reel/notations-3B-decisives.json"}
RUBRIQUES = ("BALANCE", "COHERENCE", "NOVELTY", "RIGOR", "RESULT_REASONING", "IRRELEVANCE_PENALTY", "REDUNDANCY_PENALTY")
TRAITS = ("log_jetons_total", "actions_valides", "jetons_par_action_ecart_type", "bruit")
PARTS = {"calibrage": 0.25, "developpement": 0.25}  # le reste : épreuve
SEUIL_CONFIRMATION = math.log(20.0)  # gain de vraisemblance sur la moitié B, contre la marginale de A


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for morceau in iter(lambda: f.read(1 << 16), b""):
            h.update(morceau)
    return h.hexdigest()


def classes_equilibrees(valeurs, maximum=3, part_minimale=0.10):
    import itertools
    compte = collections.Counter(valeurs)
    niveaux = sorted(compte)
    total = len(valeurs)
    for k in range(min(maximum, len(niveaux)), 1, -1):
        meilleur, taille = None, -1
        for coupes in itertools.combinations(niveaux[:-1], k - 1):
            effectifs = collections.Counter(classe(v, coupes) for v in valeurs)
            plus_petite = min(effectifs.get(c, 0) for c in range(k))
            if plus_petite > taille:
                meilleur, taille = coupes, plus_petite
        if meilleur is not None and taille >= part_minimale * total:
            return list(meilleur)
    return None


def classe(valeur, coupes):
    return sum(valeur > c for c in coupes)


def lire_sources(racine_main, notations, toutes_les_passes):
    with open(os.path.join(racine_main, EPISODES), encoding="utf-8") as f:
        episodes = json.load(f)["resultat"]["fiches"]
    sources = {EPISODES: sha256_fichier(os.path.join(racine_main, EPISODES))}
    notes = {}
    for juge, chemin in notations.items():
        complet = chemin if os.path.isabs(chemin) else os.path.join(racine_main, chemin)
        sources[chemin] = sha256_fichier(complet)
        with open(complet, encoding="utf-8") as f:
            for n in json.load(f)["resultat"]["notations"]:
                _, tache, ep, passe = n["cle"].split("/")
                if passe != "passe-0" and not toutes_les_passes:
                    continue
                cle = (juge, f"{tache}/{ep}") if not toutes_les_passes else (juge, f"{tache}/{ep}", passe)
                notes[cle] = n["notes"]
    return episodes, notes, sources


def construire(racine_main, graine, notations=None, toutes_les_passes=False):
    notations = notations or NOTATIONS_V2
    episodes, notes, sources = lire_sources(racine_main, notations, toutes_les_passes)
    rng = random.Random(graine_derivee(graine, "banque-t05-v3", "bruit"))
    lignes = []
    for e in episodes:
        jetons = e["jetons_par_action"]
        if not jetons:
            continue
        cles = [c for c in notes if c[1] == e["episode"]]
        if not cles:
            continue
        lignes.append({"identifiant": e["episode"], "tache": e["tache"], "g": int(e["episode"].rsplit("/e", 1)[1]),
                       "bruts": [math.log(sum(jetons)), float(e["bilan"]["actions_valides"]), statistics.pstdev(jetons),
                                 rng.gauss(0.0, 1.0)]})
    moyennes = [statistics.fmean(l["bruts"][j] for l in lignes) for j in range(len(TRAITS))]
    ecarts = [statistics.pstdev([l["bruts"][j] for l in lignes]) or 1.0 for j in range(len(TRAITS))]
    for l in lignes:
        l["z"] = [round((x - m) / s, 6) for x, m, s in zip(l["bruts"], moyennes, ecarts)]

    def note_de(juge, identifiant, rub):
        """Note d'une rubrique : première passe, ou moyenne arrondie des passes si `toutes_les_passes`."""
        if not toutes_les_passes:
            n = notes.get((juge, identifiant))
            return n.get(rub) if n is not None and isinstance(n.get(rub), int) else None
        valeurs = [n.get(rub) for (j, i, _p), n in notes.items() if j == juge and i == identifiant and isinstance(n.get(rub), int)]
        return int(round(statistics.fmean(valeurs))) if valeurs else None

    moniteurs = {}
    for juge in notations:
        for rub in RUBRIQUES:
            valeurs = [v for v in (note_de(juge, l["identifiant"], rub) for l in lignes) if v is not None]
            if len(valeurs) < 30:
                continue
            coupes = classes_equilibrees(valeurs)
            if coupes is None:
                continue
            moniteurs[f"{juge}:{rub}"] = {"juge": juge, "rubrique": rub, "coupes": coupes, "nombre_issues": len(coupes) + 1,
                                          "instances": len(valeurs)}
    for l in lignes:
        l["issues"] = {}
        for nom, m in moniteurs.items():
            v = note_de(m["juge"], l["identifiant"], m["rubrique"])
            if v is not None:
                l["issues"][nom] = classe(v, m["coupes"])
    taches = sorted({l["tache"] for l in lignes})
    rng_part = random.Random(graine_derivee(graine, "banque-t05-v3", "partition"))
    rng_part.shuffle(taches)
    n_cal = int(round(PARTS["calibrage"] * len(taches)))
    n_dev = int(round(PARTS["developpement"] * len(taches)))
    partie_de = {}
    for i, t in enumerate(taches):
        partie_de[t] = "calibrage" if i < n_cal else ("developpement" if i < n_cal + n_dev else "epreuve")
    for l in lignes:
        l["partie"] = partie_de[l["tache"]]
        del l["bruts"]
    lignes.sort(key=lambda l: l["identifiant"])
    effectifs = collections.Counter(l["partie"] for l in lignes)
    return {"nom": "banque-t05-v3", "graine": graine, "traits": list(TRAITS), "sous_populations": 3,
            "normalisation": {"moyennes": moyennes, "ecarts_types": ecarts}, "moniteurs": moniteurs, "instances": lignes,
            "sources": sources, "parts": dict(PARTS, epreuve=1 - sum(PARTS.values())), "toutes_les_passes": toutes_les_passes,
            "effectifs": {"instances": dict(effectifs), "taches": collections.Counter(partie_de.values())},
            "notes": "trois parties par tâche (calibrage, développement, épreuve) ; une instance par épisode et par moniteur ; "
                     "les épisodes d'une même tâche restent dépendants (une tâche = une unité : tranches par tâche)"}


# --- témoins ---------------------------------------------------------------------------------------------------------
def _description(banque):
    return {"traits": list(banque["traits"]),
            "moniteurs": {n: {"nombre_issues": m["nombre_issues"]} for n, m in banque["moniteurs"].items()}}


def _marginale(issues, k):
    n = len(issues)
    return [(issues.count(c) + 0.5) / (n + 0.5 * k) for c in range(k)]


def _gain_sur(loi, moniteur, lignes, marginale):
    """Gain de vraisemblance logarithmique de la loi sur des lignes, contre une marginale donnée (jamais ajustée ici)."""
    gain, n = 0.0, 0
    for l in lignes:
        if moniteur not in l["issues"]:
            continue
        y = int(l["issues"][moniteur])
        p = sp.proba(loi, {"z": l["z"], "g": l["g"]}, [], 0)
        gain += math.log(max(1e-12, p[y])) - math.log(marginale[y])
        n += 1
    return gain, n


def _permuter_dans_la_tache(lignes, rng):
    """Issues permutées entre les épisodes d'une même tâche (chaque moniteur séparément) : la dépendance de tâche reste,
    le lien trait → issue est détruit."""
    par_tache = collections.defaultdict(list)
    for l in lignes:
        par_tache[l.get("tache", l.get("groupe", l["identifiant"]))].append(l)
    if all(len(g) == 1 for g in par_tache.values()):
        # aucune tâche à plusieurs épisodes (monde de la grammaire) : la permutation se fait sur toute la partie,
        # sinon elle ne changerait rien ; sur T0.5, les tâches ont plusieurs épisodes et la permutation reste dans la tâche
        par_tache = {"(toute la partie)": list(lignes)}
    sortie = []
    copies = {id(l): dict(l, issues=dict(l["issues"])) for l in lignes}
    for tache, groupe in par_tache.items():
        moniteurs = set().union(*(l["issues"].keys() for l in groupe))
        for m in moniteurs:
            porteurs = [l for l in groupe if m in l["issues"]]
            valeurs = [l["issues"][m] for l in porteurs]
            rng.shuffle(valeurs)
            for l, v in zip(porteurs, valeurs):
                copies[id(l)]["issues"][m] = v
    for l in lignes:
        sortie.append(copies[id(l)])
    return sortie


def fabriquer_temoins(banque, graine, nombre_max=8, par_recherche=40):
    """Témoins vrais établis (ajustés sur A, confirmés sur B) et témoins faux (permutation dans la tâche ; trait de bruit)."""
    dev = [l for l in banque["instances"] if l["partie"] == "developpement"]
    for l in dev:  # une banque sans tâches (grammaire) : chaque instance est sa propre tâche
        l.setdefault("tache", l.get("groupe", l["identifiant"]))
    taches = sorted({l["tache"] for l in dev})
    rng = random.Random(graine_derivee(graine, "banque-t05-v3", "temoins"))
    rng.shuffle(taches)
    moitie_a = set(taches[:len(taches) // 2])
    A = [l for l in dev if l["tache"] in moitie_a]
    B = [l for l in dev if l["tache"] not in moitie_a]
    description = _description(banque)
    k_de = {n: m["nombre_issues"] for n, m in banque["moniteurs"].items()}

    def confirmer(lignes_a, lignes_b, etiquette, score_minimum=0.0):
        props = propositions_mecaniques(description, {"instances": [{"z": l["z"], "g": l["g"], "issues": l["issues"]} for l in lignes_a]},
                                        par_recherche, score_minimum=score_minimum)
        retenus, ecartes = [], []
        for p in props:
            m = p["moniteur"]
            issues_a = [int(l["issues"][m]) for l in lignes_a if m in l["issues"]]
            if not issues_a:
                continue
            marg = _marginale(issues_a, k_de[m])
            gain_b, n_b = _gain_sur(p["loi_predictive"], m, lignes_b, marg)
            entree = {"moniteur": m, "loi_predictive": p["loi_predictive"], "gain_confirmation_nat": round(gain_b, 4),
                      "instances_confirmation": n_b, "enonce_mecanique": p["enonce"], "etiquette": etiquette}
            (retenus if n_b >= 15 and gain_b >= SEUIL_CONFIRMATION else ecartes).append(entree)
        retenus.sort(key=lambda r: -r["gain_confirmation_nat"])
        ecartes.sort(key=lambda r: -r["gain_confirmation_nat"])
        return retenus, ecartes

    vrais, _ = confirmer(A, B, "vrai : ajusté sur A, confirmé sur B")
    # témoins faux par permutation dans la tâche : même procédure sur des issues permutées (A et B permutés)
    rng_perm = random.Random(graine_derivee(graine, "banque-t05-v3", "permutation"))
    A_perm, B_perm = _permuter_dans_la_tache(A, rng_perm), _permuter_dans_la_tache(B, rng_perm)
    # sur des issues permutées, aucune loi ne bat d'ordinaire la marginale après pénalité : on prend les meilleures sans
    # filtre (ajustées au bruit de la permutation), puis on les confronte à B permuté comme les vraies
    faux_perm, perm_non_confirmes = confirmer(A_perm, B_perm, "faux : issues permutées dans la tâche, pourtant confirmée",
                                              score_minimum=-math.inf)
    if not faux_perm:
        # aucune loi permutée confirmée (attendu) : les meilleures candidates permutées, non confirmées, servent de témoins
        # faux (leur lien trait → issue est détruit par construction ; attendu : jamais promues sur l'épreuve)
        faux_perm = [dict(e, etiquette="faux : issues permutées dans la tâche (candidate non confirmée)")
                     for e in perm_non_confirmes[:nombre_max]]
    # témoins faux sur le trait de bruit : une loi softmax sur le seul trait de bruit, par moniteur
    faux_bruit = []
    d = len(banque["traits"])
    i_bruit = banque["traits"].index("bruit") if "bruit" in banque["traits"] else None
    for n, k in (sorted(k_de.items()) if i_bruit is not None else []):
        poids = [[0.0] * d for _ in range(k)]
        for c in range(k):
            poids[c][i_bruit] = round(rng.gauss(0.0, 1.0), 6)
        faux_bruit.append({"moniteur": n, "loi_predictive": {"type": "softmax", "poids": poids, "biais": [0.0] * k},
                           "etiquette": "faux : trait de bruit"})
    fiches = []
    for i, t in enumerate(vrais[:nombre_max], 1):
        fiches.append(_fiche(f"TV{i:02d}", t, "vraie", d, k_de, banque,
                             f"L'issue du moniteur {t['moniteur']} suit la loi confirmée n° {i} (gain {t['gain_confirmation_nat']} nat sur {t['instances_confirmation']} instances tenues à l'écart)"))
    for i, t in enumerate(faux_perm[:nombre_max], 1):
        fiches.append(_fiche(f"TP{i:02d}", t, "fausse", d, k_de, banque,
                             f"L'issue du moniteur {t['moniteur']} suit la loi n° {i} (ajustée sur développement permuté)"))
    for i, t in enumerate(faux_bruit[:nombre_max], 1):
        fiches.append(_fiche(f"TB{i:02d}", t, "fausse", d, k_de, banque,
                             f"L'issue du moniteur {t['moniteur']} suit le trait de bruit (loi n° {i})"))
    bilan = {"taches_developpement": len(taches), "moitie_A": len(A), "moitie_B": len(B), "seuil_confirmation_nat": SEUIL_CONFIRMATION,
             "candidats_vrais_proposes": par_recherche, "vrais_confirmes": len(vrais),
             "faux_permutation_confirmes": sum("pourtant confirmée" in f["etiquette"] for f in faux_perm),
             "faux_permutation_non_confirmes_pris": sum("non confirmée" in f["etiquette"] for f in faux_perm[:nombre_max]),
             "faux_bruit": len(faux_bruit), "gains_vrais": [t["gain_confirmation_nat"] for t in vrais],
             "gains_faux_permutation": [t["gain_confirmation_nat"] for t in faux_perm]}
    return fiches, bilan


def _fiche(ident, t, temoin, d, k_de, banque, enonce):
    k = k_de[t["moniteur"]]
    return {"identifiant": ident, "enonce": enonce, "prediction": {"signe": "+", "valeur": 0.5, "texte": "la loi bat le nul"},
            "metrique": "richesse du pari", "nul": "bibliothèque du juge", "seuil": 20.0, "severite_attendue": 0.05, "cout_borne": 1.0,
            "protocole": "pari séquentiel sur la banque", "domaines": ["banque-t05"], "operateurs": ["loi"], "contraintes": ["banque"],
            "loi_predictive": t["loi_predictive"], "temoin": temoin,
            "espace_instances": {"nombre_issues": k, "dimension": d, "moniteur": t["moniteur"], "sous_populations": banque["sous_populations"]},
            # `source` est un texte (champ privé de la fiche) ; la confirmation y est écrite en clair
            "source": f"construire_banque_t05_v3 : {t['etiquette']}"
                      + (f" ; gain de confirmation {t['gain_confirmation_nat']} nat sur {t['instances_confirmation']} instances"
                         if t.get("gain_confirmation_nat") is not None else "")}


def principal(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("racine_main")
    a.add_argument("sortie")
    a.add_argument("--graine", type=int, default=20261027)
    a.add_argument("--notations", action="append", default=[], help="JUGE=CHEMIN (répétable ; défaut : les décisives de la v2)")
    a.add_argument("--toutes-les-passes", action="store_true")
    a.add_argument("--temoins", help="fichier de sortie des témoins (fiches) ; défaut : <sortie>-temoins.json")
    args = a.parse_args(argv)
    notations = dict(n.split("=", 1) for n in args.notations) or None
    banque = construire(args.racine_main, args.graine, notations, args.toutes_les_passes)
    temoins, bilan = fabriquer_temoins(banque, args.graine)
    banque["temoins"] = bilan
    ecrire_json_scelle(args.sortie, banque)
    ecrire_json_scelle(args.temoins or args.sortie.replace(".json", "-temoins.json"), temoins)
    print(json.dumps({"instances": len(banque["instances"]), "effectifs": banque["effectifs"],
                      "moniteurs": {k: (v["nombre_issues"], v["instances"]) for k, v in banque["moniteurs"].items()},
                      "temoins": bilan}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
