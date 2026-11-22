"""Grille du devis v9 de la tranche de l'ajustement de nos lentilles (B-β) : pire cas et plafond selon le lieu de rangement et le prix
exigé (§ 4), offres recevables aux relevés du 2026-11-18 avec le lieu L1 (§ 7, décision 1), attendus (§ 7, décision 4).

Lancement : `python3 -I -B docs/notes/neuron-lens-v1/devis-b-beta/grille_devis_b_beta_v9.py` ; lit les deux relevés TSV du dossier,
aucun appel au loueur, aucun réseau.

Bases (devis v8, § 4, vérifiées par la contre-lecture de la v8) :
- périmètre entier, heures au pire : L2 25,1 h (ajustement 13,1 h + sauvegardes 0,5 h + copies vers L2 0,5 h ; copie de fin 0,5 h) ;
  L3 24,6 h (sans les copies vers L2) ; L1 24,1 h (sans copie) ; trafic réservé à 0,04 USD/Go : L2 85 Go, L3 42 Go, L1 25 Go ;
- notre lentille R seulement : 1 000 passages (6,56 h au pire) et la moitié des sauvegardes et des copies : L1 17,31 h, L3 17,56 h,
  L2 17,81 h ; trafic L1 25 Go, L3 33,6 Go, L2 55,1 Go ;
- heures attendues avec L1 : 8,5 à 12,9 h (périmètre entier) ; 5,65 à 8,7 h (R seulement) ;
- pire cas = heures × prix exigé + trafic réservé ; plafond = plus petit entier C tel que 0,9 × C ≥ pire cas ; « une relance » = une
  heure de plus ; prix minimal = (0,9 × C − trafic réservé) / 36 h.
"""
import csv
import math
import pathlib

ICI = pathlib.Path(__file__).resolve().parent
ENTIER = {"L1": (24.1, 25.0), "L3": (24.6, 42.0), "L2": (25.1, 85.0)}
R_SEUL = {"L1": (17.31, 25.0), "L3": (17.56, 33.6), "L2": (17.81, 55.1)}
PRIX = (2.25, 2.49, 2.62, 3.00, 4.25)
RELEVES = (("2026-11-18T01:57:42Z", "releve-prix-vast-h100-20261118T015742Z-v2.tsv"),
           ("2026-11-18T02:22:05Z", "releve-prix-vast-h100-20261118T022205Z-v3.tsv"))
FILTRE_DEBUT = "gpu_name=H100_SXM num_gpus=1 cpu_ram>=64"


def fr(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")


def plafond(pire):
    return math.ceil(pire / 0.9 - 1e-9)


def ligne_lieu(h, go, p):
    f = go * 0.04
    pc, pc1 = h * p + f, (h + 1) * p + f
    c, c1 = plafond(pc), plafond(pc1)
    return pc, c, pc1, c1, (0.9 * c - f) / 36.0


def offres_filtre(chemin):
    with open(chemin, encoding="utf-8") as fh:
        lignes = [x for x in fh.read().splitlines() if x and not x.startswith("#")]
    tete = lignes[0].split("\t")
    vues = {}
    for x in lignes[1:]:
        d = dict(zip(tete, x.split("\t")))
        if d["requete"].startswith(FILTRE_DEBUT):
            vues[d["machine_id"]] = d
    return list(vues.values())


def recevables(offres, p, c, f, borne=False):
    pmin = (0.9 * c - f) / 36.0
    out = []
    for d in offres:
        prix = float(d["prix_avec_200_go"])
        ok = (d["verification"] == "verified" and prix <= p and float(d["inet_up_mbit"]) >= 200
              and float(d["inet_up_cost_usd_go"]) <= 0.04 and float(d["inet_down_cost_usd_go"]) <= 0.04)
        if ok and (borne or prix >= pmin):
            out.append(f"{d['lieu']} {fr(prix, 4)}")
    return out


print("Table du § 4 (périmètre entier) : prix exigé | L1 | L3 | L2 (pire cas ; plafond ; avec une relance ; plafond ; prix minimal)")
for p in PRIX:
    cells = []
    for lieu in ("L1", "L3", "L2"):
        pc, c, pc1, c1, pmin = ligne_lieu(*ENTIER[lieu], p)
        cells.append(f"{fr(pc)} ; {c} ; {fr(pc1)} ; {c1} ; {fr(pmin, 2)}")
    print(f"| {fr(p, 2)} | " + " | ".join(cells) + " |")
print()
print("Notre lentille R seulement :")
for p in PRIX:
    cells = []
    for lieu in ("L1", "L3", "L2"):
        pc, c, pc1, c1, pmin = ligne_lieu(*R_SEUL[lieu], p)
        cells.append(f"{lieu} {fr(pc)} ; {c} ; {fr(pc1)} ; {c1}")
    print(f"  {fr(p, 2)} : " + " | ".join(cells))
print()
for lieu, (h, go) in ENTIER.items():
    f = go * 0.04
    print(f"68 USD gardés, {lieu} : prix exigé maximal {fr((0.9 * 68 - f) / h, 3)} ; avec une relance {fr((0.9 * 68 - f) / (h + 1), 3)}")
print()
OPTIONS_L1 = (("1a", 2.49, 68), ("1b", 2.62, 72), ("1c", 3.00, 82), ("1d", 4.25, 115))
for heure, nom in RELEVES:
    offres = offres_filtre(ICI / nom)
    print(f"Relevé {heure} ({nom}), filtre complet : " + " ; ".join(f"{d['lieu']} {fr(float(d['prix_avec_200_go']), 4)}" for d in offres))
    for o, p, c in OPTIONS_L1:
        print(f"  ({o}) L1 {fr(p, 2)} / {c} : règle du refus {recevables(offres, p, c, 1.0)} ; borne haute {recevables(offres, p, c, 1.0, True)}")
print()
for nom, (lo, hi) in (("entier, L1", (8.5, 12.9)), ("R seulement, L1", (5.65, 8.7))):
    for etiquette, prix, trafic_go in (("Japon 2,0380", 2.0380, 0.0), ("Lettonie 2,3236", 2.3236, 0.0026), ("prix exigé 3,00", 3.00, 0.04)):
        print(f"attendu {nom}, {etiquette} : {fr(lo * prix)} à {fr(hi * prix + 25 * trafic_go)} USD")
