"""Grille du devis v10 de la tranche de l'ajustement de nos lentilles (B-β) — v10.

v10 = v9 (`grille_devis_b_beta_v9.py`, `74908a2a…`) étendue selon la vérification courte de la v9 (M-1, M-2, m-7, m-9) : marge sous
l'arrêt dur de chaque plafond ; plafond « avec une relance » et sa marge ; option au prix écrit dans le mot de Lazar (2,25 USD/h) ; prix
exigé de 2,39 (les 68 USD gardés, une relance comptée) ; heures d'arrêt de la garde selon le prix déclaré (prix exigé, ou prix lu à la
création) ; offres recevables avec chaque plafond, aux deux règles de la minuterie ; périmètre « notre lentille R seulement » à tous les
prix. Le docstring de la v9 disait les heures attendues « vérifiées par la contre-lecture de la v8 » : c'est faux, elles sont dérivées par la
fille (ci-dessous).

Lancement : `python3 -I -B docs/notes/neuron-lens-v1/devis-b-beta/grille_devis_b_beta_v10.py` ; lit les deux relevés TSV du dossier,
aucun appel au loueur, aucun réseau.

Bases :
- périmètre entier, heures au pire (devis v8, § 4, vérifiées par les contre-lectures de la v8 et de la v9) : L2 25,1 h ; L3 24,6 h (sans
  les copies vers L2, 0,5 h) ; L1 24,1 h (sans copie : ni copies vers L2, ni copie de fin, 0,5 h chacune) ; trafic réservé à 0,04 USD/Go :
  L2 85 Go, L3 42 Go, L1 25 Go ;
- notre lentille R seulement (dérivation de la fille, devis v9, § 7) : 1 000 passages (6,56 h au pire) et la moitié des sauvegardes et
  des copies : L1 17,31 h, L3 17,56 h, L2 17,81 h ; trafic L1 25 Go, L3 33,6 Go, L2 55,1 Go ;
- heures attendues (dérivation de la fille) : périmètre entier 8,9 à 13,4 h avec L2 (devis v8, § 4) ; avec L1, moins les copies vers L2
  (0,2 h attendues) et la copie de fin (0,2 à 0,3 h) : 8,5 à 12,9 h ; R seulement avec L1 : 5,65 à 8,7 h ;
- pire cas = heures × prix exigé + trafic réservé ; plafond minimal = plus petit entier C tel que 0,9 × C ≥ pire cas ; « avec une relance »
  = une heure d'ajustement de plus ; marge = 0,9 × C − pire cas ; prix minimal (règle du refus de la minuterie v4) = (0,9 × C − trafic
  réservé) / 36 h ; heures d'arrêt de la garde = (0,9 × C − trafic réservé) / prix déclaré.
"""
import math
import pathlib

ICI = pathlib.Path(__file__).resolve().parent
ENTIER = {"L1": (24.1, 25.0), "L3": (24.6, 42.0), "L2": (25.1, 85.0)}
R_SEUL = {"L1": (17.31, 25.0), "L3": (17.56, 33.6), "L2": (17.81, 55.1)}
PRIX = (2.25, 2.39, 2.49, 2.62, 3.00, 4.25)
RELEVES = (("2026-11-18T01:57:42Z", "releve-prix-vast-h100-20261118T015742Z-v2.tsv"),
           ("2026-11-18T02:22:05Z", "releve-prix-vast-h100-20261118T022205Z-v3.tsv"))
FILTRE_DEBUT = "gpu_name=H100_SXM num_gpus=1 cpu_ram>=64"


def fr(x, d=1):
    return f"{x:.{d}f}".replace(".", ",")


def plafond(pire):
    return math.ceil(pire / 0.9 - 1e-9)


def calcul(h, go, p):
    f = go * 0.04
    pc, pc1 = h * p + f, (h + 1) * p + f
    c, c1 = plafond(pc), plafond(pc1)
    return {"f": f, "pire": pc, "C": c, "marge": 0.9 * c - pc, "pire1": pc1, "C1": c1, "marge1": 0.9 * c1 - pc1,
            "pmin": (0.9 * c - f) / 36.0, "pmin1": (0.9 * c1 - f) / 36.0}


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


def recevables(offres, p, c, f, borne):
    pmin = (0.9 * c - f) / 36.0
    out = []
    for d in offres:
        prix = float(d["prix_avec_200_go"])
        ok = (d["verification"] == "verified" and prix <= p and float(d["inet_up_mbit"]) >= 200
              and float(d["inet_up_cost_usd_go"]) <= 0.04 and float(d["inet_down_cost_usd_go"]) <= 0.04)
        if ok and (borne or prix >= pmin):
            out.append(f"{d['lieu'].split(',')[0]} {fr(prix, 2)}")
    return ", ".join(out) or "aucune"


print("A. Périmètre entier : prix exigé, lieu : pire cas ; plafond minimal ; marge | avec une relance : pire cas ; plafond ; marge | "
      "prix minimal (refus) au plafond minimal ; avec une relance")
for p in PRIX:
    for lieu in ("L1", "L3", "L2"):
        r = calcul(*ENTIER[lieu], p)
        print(f"  {fr(p, 2)} {lieu} : {fr(r['pire'])} ; {r['C']} ; {fr(r['marge'], 2)} | {fr(r['pire1'])} ; {r['C1']} ; "
              f"{fr(r['marge1'], 2)} | {fr(r['pmin'], 2)} ; {fr(r['pmin1'], 2)}")
print()
print("B. Notre lentille R seulement : prix exigé, lieu : pire cas ; plafond minimal ; marge | avec une relance : pire cas ; plafond ; marge")
for p in PRIX:
    cells = []
    for lieu in ("L1", "L3", "L2"):
        r = calcul(*R_SEUL[lieu], p)
        cells.append(f"{lieu} {fr(r['pire'])} ; {r['C']} ; {fr(r['marge'], 2)} | {fr(r['pire1'])} ; {r['C1']} ; {fr(r['marge1'], 2)}")
    print(f"  {fr(p, 2)} : " + " || ".join(cells))
print()
print("C. 68 USD gardés, prix exigé maximal (sans relance ; avec une relance)")
for lieu, (h, go) in ENTIER.items():
    f = go * 0.04
    print(f"  {lieu} : {fr((0.9 * 68 - f) / h, 3)} ; {fr((0.9 * 68 - f) / (h + 1), 3)}")
print()
OPTIONS = (("1a", 2.25, "prix écrit dans le mot"), ("1b", 2.49, "68 USD gardés, sans relance"), ("1b'", 2.39, "68 USD gardés, une relance comptée"),
           ("1c", 2.62, "offre du Montana du 17"), ("1d", 3.00, "lecture de la v6"), ("1e", 4.25, "prix de Tchéquie"))
print("D. Options de la décision 1 avec L1 : plafond minimal (marge) ; avec une relance (marge) ; heures d'arrêt de la garde au prix exigé "
      "déclaré (plafond minimal ; avec une relance)")
for o, p, nom in OPTIONS:
    r = calcul(*ENTIER["L1"], p)
    if o in ("1b", "1b'"):
        c = c1 = 68
        r.update({"C": 68, "C1": 68, "marge": 0.9 * 68 - r["pire"], "marge1": 0.9 * 68 - r["pire1"],
                  "pmin": (0.9 * 68 - r["f"]) / 36.0, "pmin1": (0.9 * 68 - r["f"]) / 36.0})
    hg, hg1 = (0.9 * r["C"] - r["f"]) / p, (0.9 * r["C1"] - r["f"]) / p
    print(f"  ({o}) {nom}, {fr(p, 2)} : {r['C']} ({fr(r['marge'], 2)}) ; {r['C1']} ({fr(r['marge1'], 2)}) ; garde {fr(hg, 2)} h ; {fr(hg1, 2)} h")
    for heure, fichier in RELEVES:
        offres = offres_filtre(ICI / fichier)
        print(f"      {heure} : plafond minimal, refus : {recevables(offres, p, r['C'], r['f'], False)} ; borne haute : "
              f"{recevables(offres, p, r['C'], r['f'], True)} | avec une relance, refus : {recevables(offres, p, r['C1'], r['f'], False)}")
print()
print("E. Heures d'arrêt de la garde avec le prix lu à la création déclaré, L1, plafond minimal de (1d) 82 et (1a) 62")
for nom, prix in (("Japon", 2.0380), ("Lettonie", 2.3236), ("Montana", 2.7514)):
    print(f"  {nom} {fr(prix, 4)} : 82 USD → {fr((0.9 * 82 - 1.0) / prix, 1)} h ; 62 USD → {fr((0.9 * 62 - 1.0) / prix, 1)} h "
          f"(pire cas en heures : 24,1 ; avec une relance : 25,1)")
print()
print("F. Attendus (USD)")
for nom, (lo, hi) in (("entier, L1", (8.5, 12.9)), ("R seulement, L1", (5.65, 8.7))):
    for etiquette, prix, trafic in (("Japon 2,04", 2.0380, 0.0), ("Lettonie 2,32", 2.3236, 0.0026), ("Montana 2,75", 2.7514, 0.0195),
                                    ("prix exigé 2,25", 2.25, 0.04), ("prix exigé 3,00", 3.00, 0.04)):
        print(f"  {nom}, {etiquette} : {fr(lo * prix)} à {fr(hi * prix + 25 * trafic)}")
