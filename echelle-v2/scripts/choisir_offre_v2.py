#!/usr/bin/env python3
"""Choix de l'offre et plafond de durée de la comparaison d'échelle v2 (lignée « session-depot », 26 octobre 2026),
extrait du lanceur pour être testé (R5, CLX-07). Lit la réponse brute de `vastai search offers --raw`, relit la
conformité localement (unités de Vast : gpu_ram en Mo ; dph_total = location + stockage, en USD/h ; storage_total_cost
= stockage seul, en USD/h, qui court encore entre l'arrêt et la destruction ; inet_down_cost en USD/Go), et garde
l'offre au coût estimé le plus bas dont la **dépense au pire** tient sous le plafond du GO :

  pire = durée plafonnée × dph_total + DESCENTE_GO × inet_down_cost + STOCKAGE_APRES_H × storage_total_cost + MARGE
  durée plafonnée = min(7 200 s, (plafond − descente − stockage après arrêt − marge) / dph_total), au moins DUREE_MIN_S.

    python -I -B choisir_offre_v2.py OFFRES_BRUT OFFRE_SORTIE PRIX_MAX DESCENTE_MAX PLAFOND_GO JOURNAL OFFRES_RELUES
Sortie standard : « id dph_total inet_down_cost duree_max_s pire ». Codes : 0 choisie ; 3 aucune conforme ; 2 illisible.
"""
import json
import math
import sys

DESCENTE_GO = 160          # Go descendus (8B ≈ 16 Go, 70B ≈ 141 Go)
STOCKAGE_APRES_H = 3.0     # heures de stockage entre l'arrêt et la destruction, au plus
MARGE = 0.20               # USD
DUREE_PLAFOND_S = 7200
DUREE_MIN_S = 4500         # en dessous, le run (≈ 1 h attendue) n'a pas la marge voulue
CARTES_MIN, CARTES_MAX, RAM_CARTE_MIN_MO, RAM_TOTALE_MIN_MO = 2, 4, 46000, 160000
EXTRAIT = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cuda_max_good", "cpu_ram", "dph_base",
           "dph_total", "storage_total_cost", "inet_down", "inet_down_cost", "reliability2", "geolocation")


def nombre(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def entier(v):
    return isinstance(v, int) and not isinstance(v, bool)


def evaluer(o, prix_max, descente_max, plafond):
    """None si non conforme ; sinon (coût estimé, durée plafonnée en s, dépense au pire)."""
    if not (isinstance(o, dict) and entier(o.get("id")) and nombre(o.get("gpu_ram")) and entier(o.get("num_gpus"))):
        return None
    if not (CARTES_MIN <= o["num_gpus"] <= CARTES_MAX and o["gpu_ram"] >= RAM_CARTE_MIN_MO
            and o["gpu_ram"] * o["num_gpus"] >= RAM_TOTALE_MIN_MO):
        return None
    if not (nombre(o.get("cuda_max_good")) and o["cuda_max_good"] >= 13.0):
        return None
    dph, desc, stock = o.get("dph_total"), o.get("inet_down_cost"), o.get("storage_total_cost")
    if not (nombre(dph) and 0 < dph <= prix_max and nombre(desc) and 0 <= desc <= descente_max
            and nombre(stock) and 0 <= stock < dph):
        return None
    fixe = DESCENTE_GO * desc + STOCKAGE_APRES_H * stock + MARGE
    duree = min(DUREE_PLAFOND_S, math.floor((plafond - fixe) / dph * 3600))
    if duree < DUREE_MIN_S:
        return None
    pire = round(duree / 3600 * dph + fixe, 4)
    if pire > plafond:
        return None
    estime = round(1.5 * dph + DESCENTE_GO * desc + STOCKAGE_APRES_H * stock, 4)
    return estime, duree, pire


def principal(argv):
    brut, sortie, prix_max, descente_max, plafond, journal, relues = argv
    prix_max, descente_max, plafond = float(prix_max), float(descente_max), float(plafond)
    try:
        offres = json.load(open(brut, encoding="utf-8"))
        assert isinstance(offres, list)
    except Exception:
        print("offres : réponse illisible", file=sys.stderr)
        return 2
    json.dump([{k: o.get(k) for k in EXTRAIT} if isinstance(o, dict) else {"illisible": type(o).__name__} for o in offres],
              open(relues, "w", encoding="utf-8"), indent=1)
    vus = [repr(o.get("id")) for o in offres if isinstance(o, dict)]
    if len(vus) != len(set(vus)):
        print("offres : identifiant en double (ambigu)", file=sys.stderr)
        return 2
    notees = []
    for o in offres:
        e = evaluer(o, prix_max, descente_max, plafond)
        if e is not None:
            notees.append((e[0], o["id"], o, e))
    notees.sort(key=lambda t: (t[0], t[1]))
    with open(journal, "a", encoding="utf-8") as j:
        j.write("offres conformes relues : " + (", ".join(
            f"{o['id']} ({o['num_gpus']} × {o['gpu_name']}, {o['dph_total']:.4f} USD/h, descente {o['inet_down_cost']:.4f} "
            f"USD/Go, stockage {o['storage_total_cost']:.4f} USD/h, estimé {e[0]:.2f} USD, plafond {e[1]} s, pire {e[2]:.2f} USD)"
            for _, _, o, e in notees) or "aucune") + "\n")
    if not notees:
        print(f"aucune offre conforme au plafond de {plafond} USD", file=sys.stderr)
        return 3
    _, _, o, e = notees[0]
    json.dump({**{k: o.get(k) for k in EXTRAIT}, "estime": e[0], "duree_max_s": e[1], "pire": e[2]},
              open(sortie, "w", encoding="utf-8"), indent=1)
    print(o["id"], o["dph_total"], o["inet_down_cost"], e[1], e[2])
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
