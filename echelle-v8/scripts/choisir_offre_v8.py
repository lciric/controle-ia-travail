#!/usr/bin/env python3
"""Choix de l'offre, plafond de durée et contrôle du prix relu, comparaison d'échelle v8 (lignée « session-depot »,
27 octobre 2026), copie de `choisir_offre_v7.py` sous un nom nouveau (R12) après la contre-lecture n° 7, sans
changement de calcul. Depuis la v7 (contre-lecture n° 6) : le commentaire de MARGE dit la latence qu'elle couvre (CLU-03). Depuis la v5 (contre-lecture n° 4) : descente comptée pour 165 Go (157,19 Go de poids relus sur
le Hub, trace `tailles-modeles-v1.json`, plus les roues pip et l'image ; CLW-10). Depuis la v4 (contre-lecture n° 3) :
  - CLZ-03 : le prix relu après la création est admis jusqu'à TOLERANCE_PRIX × l'offre ; la durée plafonnée et la
    dépense au pire sont donc calculées à ce prix majoré, location, stockage, descente et remontée comprises ;
  - CLZ-05 : la remontée des résultats (≈ 0,3 Go, comptée 1 Go) entre dans le pire ; débit de descente d'au moins
    DEBIT_MIN_MBPS (le 70B pèse ≈ 141 Go : ≈ 10 min à 2 000 Mb/s, ≈ 27 min à 700) ;
  - CLZ-04 : la comparaison du prix relu est une fonction testée (`verifier_prix_relu`), appelée par
    `controler_prix_v8.sh` (option --prix-relu).
Unités de Vast : gpu_ram en Mo ; inet_down en Mb/s ; dph_total = location + stockage, en USD/h ; storage_total_cost
= stockage seul, en USD/h, qui court encore entre l'arrêt et la destruction ; inet_down_cost et inet_up_cost en USD/Go.

  T = TOLERANCE_PRIX ; fixe = T × (DESCENTE_GO × descente + MONTEE_GO × remontée + STOCKAGE_APRES_H × stockage) + MARGE
  durée plafonnée = min(7 200 s, (plafond − fixe) / (T × dph_total)), au moins DUREE_MIN_S
  pire = durée plafonnée × T × dph_total + fixe ≤ plafond

    python -I -B choisir_offre_v8.py OFFRES_BRUT OFFRE_SORTIE PRIX_MAX DESCENTE_MAX PLAFOND_GO JOURNAL OFFRES_RELUES
      sortie standard : « id dph_total inet_down_cost duree_max_s pire » ; codes : 0 choisie ; 3 aucune ; 2 illisible.
    python -I -B choisir_offre_v8.py --prix-relu OFFRE_JSON < réponse de « vastai show instance ID --raw »
      lignes de contrôle sur la sortie standard ; codes : 0 conforme ; 1 non conforme ou illisible.
"""
import json
import math
import sys

DESCENTE_GO = 165          # Go descendus : poids 16,07 + 141,12 Go (trace tailles-modeles-v1.json), roues et image
MONTEE_GO = 1              # Go remontés (résultats ≈ 0,3 Go, comptés large ; CLZ-05)
STOCKAGE_APRES_H = 24.0    # heures de stockage entre l'arrêt et la destruction, au plus (CLY-03)
MARGE = 0.20               # USD : latence de la surveillance ; couvre 195,9 s au prix le plus haut admis (1,05 × 3,5 USD/h),
                           # la surveillance demande l'arrêt au plus 60 s après le plafond, puis 30 s d'appel : 90 s (CLU-03)
TOLERANCE_PRIX = 1.05      # prix relu admis jusqu'à 5 % au-dessus de l'offre ; tout le pire est compté à ce prix (CLZ-03)
DUREE_PLAFOND_S = 7200
DUREE_MIN_S = 4500         # en dessous, le run (≈ 1 h attendue) n'a pas la marge voulue
DEBIT_MIN_MBPS = 2000      # descente (CLZ-05)
CARTES_MIN, CARTES_MAX, RAM_CARTE_MIN_MO, RAM_TOTALE_MIN_MO = 2, 4, 46000, 160000
CHAMPS_PRIX = ("dph_total", "storage_total_cost", "inet_down_cost", "inet_up_cost")
EXTRAIT = ("id", "machine_id", "host_id", "gpu_name", "gpu_ram", "num_gpus", "cuda_max_good", "cpu_ram", "dph_base",
           "dph_total", "storage_total_cost", "inet_down", "inet_down_cost", "inet_up_cost", "reliability2",
           "geolocation")


def nombre(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def entier(v):
    return isinstance(v, int) and not isinstance(v, bool)


def evaluer(o, prix_max, descente_max, plafond):
    """None si non conforme ; sinon (coût estimé, durée plafonnée en s, dépense au pire, attendu si détruite vite)."""
    if not (isinstance(o, dict) and entier(o.get("id")) and nombre(o.get("gpu_ram")) and entier(o.get("num_gpus"))):
        return None
    if not (CARTES_MIN <= o["num_gpus"] <= CARTES_MAX and o["gpu_ram"] >= RAM_CARTE_MIN_MO
            and o["gpu_ram"] * o["num_gpus"] >= RAM_TOTALE_MIN_MO):
        return None
    if not (nombre(o.get("cuda_max_good")) and o["cuda_max_good"] >= 13.0):
        return None
    if not (nombre(o.get("inet_down")) and o["inet_down"] >= DEBIT_MIN_MBPS):
        return None
    dph, desc, mont, stock = (o.get(k) for k in ("dph_total", "inet_down_cost", "inet_up_cost", "storage_total_cost"))
    if not (nombre(dph) and 0 < dph <= prix_max and nombre(desc) and 0 <= desc <= descente_max
            and nombre(mont) and 0 <= mont and nombre(stock) and 0 <= stock < dph):
        return None
    t = TOLERANCE_PRIX
    fixe = t * (DESCENTE_GO * desc + MONTEE_GO * mont + STOCKAGE_APRES_H * stock) + MARGE
    duree = min(DUREE_PLAFOND_S, math.floor((plafond - fixe) / (t * dph) * 3600))
    if duree < DUREE_MIN_S:
        return None
    pire = round(duree / 3600 * t * dph + fixe, 4)
    if pire > plafond:
        return None
    estime = round(1.5 * dph + DESCENTE_GO * desc + MONTEE_GO * mont + STOCKAGE_APRES_H * stock, 4)
    rapide = round(1.5 * dph + DESCENTE_GO * desc + MONTEE_GO * mont + 1.0 * stock, 4)
    return estime, duree, pire, rapide


def verifier_prix_relu(instance, offre, tolerance=TOLERANCE_PRIX):
    """(conforme, lignes). dph_total relu : obligatoire, au plus tolérance × l'offre. Les autres prix : au plus
    tolérance × l'offre s'ils sont relus ; absents de la réponse, ils sont consignés « non relus ». Un prix de l'offre
    illisible, ou un prix relu présent mais illisible : non conforme."""
    if not isinstance(instance, dict) or not isinstance(offre, dict):
        return False, ["réponse ou offre illisible"]
    ok, lignes = True, []
    for k in CHAMPS_PRIX:
        o, r = offre.get(k), instance.get(k)
        if not nombre(o):
            return False, lignes + [f"{k} de l'offre illisible"]
        if r is None and k != "dph_total":
            lignes.append(f"{k} non relu (absent de la réponse)")
            continue
        if not nombre(r):
            ok = False
            lignes.append(f"{k} relu illisible")
            continue
        conforme = r <= tolerance * o + 1e-12
        ok = ok and conforme
        lignes.append(f"{k} relu {r:.6f} ; offre {o:.6f} ; {'conforme' if conforme else 'au-delà de la tolérance'}")
    return ok, lignes


def principal(argv):
    if argv[:1] == ["--prix-relu"]:
        if len(argv) != 2:
            print("usage : choisir_offre_v8.py --prix-relu OFFRE_JSON < instance", file=sys.stderr)
            return 1
        try:
            offre = json.load(open(argv[1], encoding="utf-8"))
        except Exception:
            offre = None
        try:
            instance = json.loads(sys.stdin.read())
        except Exception:
            instance = None
        ok, lignes = verifier_prix_relu(instance, offre)
        for ligne in lignes:
            print(f"prix relu : {ligne}")
        print(f"prix relu : {'conforme' if ok else 'non conforme'} (tolérance {TOLERANCE_PRIX})")
        return 0 if ok else 1
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
            f"USD/Go, remontée {o['inet_up_cost']:.4f} USD/Go, stockage {o['storage_total_cost']:.4f} USD/h, débit "
            f"{o['inet_down']:.0f} Mb/s, estimé {e[0]:.2f} USD, plafond {e[1]} s, pire {e[2]:.2f} USD)"
            for _, _, o, e in notees) or "aucune") + "\n")
    if not notees:
        print(f"aucune offre conforme au plafond de {plafond} USD", file=sys.stderr)
        return 3
    _, _, o, e = notees[0]
    json.dump({**{k: o.get(k) for k in EXTRAIT}, "estime": e[0], "duree_max_s": e[1], "pire": e[2],
               "attendu_destruction_rapide": e[3], "tolerance_prix": TOLERANCE_PRIX},
              open(sortie, "w", encoding="utf-8"), indent=1)
    print(o["id"], o["dph_total"], o["inet_down_cost"], e[1], e[2])
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
