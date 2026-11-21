#!/usr/bin/env python3
"""Devis de la part du lot honnête neuf L-1 qui étalonne P1 et P2 du bras « papier dopamine » — calculs v1.

Aucune donnée du programme n'est lue, aucun tirage, aucun réseau. Seule entrée : le relevé public des offres du
loueur de cartes, fait le 2026-11-21 à 10:55:20Z, versé à côté (chemin en argument, sinon le fichier voisin).
Lancer depuis n'importe où : `.venv/bin/python -I prereg/papier-dopamine-moniteur-v1/calculs-devis-lot-l-1-v1.py`.

Sources des constantes (aucune n'est neuve) :
- débit et frais fixes : devis scellé du barreau 5, § 1 et § 2
  (docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md), qui cite
  prereg/T0.6-organismes-v0-v1.md, l. 640-652 ; source première NON relue par l'auteur de ce devis ;
- prix de la carte, du stockage et du téléchargement : même devis scellé, § 1 ;
- seuils 368 et 437, bande à 11 seuils, 133 épisodes par côté : recalculés ici, à comparer aux calculs de la v7
  (blocs A, C, E) et de sa contre-lecture (blocs 2 et 3).
NON FONDÉS, donc donnés en grille et jamais en valeur : la corrélation par famille (rho) et le nombre de familles
éligibles (F). Le « cas de référence » est une convention d'affichage, pas une estimation.
"""
import json
import math
import sys
from pathlib import Path

from scipy.stats import beta

# --- constantes reprises du devis scellé du barreau 5 (carte A100 SXM4 de 80 Go) ---
S_PAR_EPISODE = 40.2            # secondes par épisode, en lots de 8
FIXES_H = 1.0 + 0.6 + 0.2       # mise en place, essais sur l'instance, poussée
PRIX = (1.0889, 1.30)           # USD de l'heure, attendu bas et haut ; 1,30 est aussi la borne de l'offre
PRIX_PIRE = 1.40                # pire cas du devis scellé, avec un hôte deux fois plus lent
DISQUE = (0.03, 0.08)           # USD de l'heure ; 0,08 est le plafond du filtre
TELECH = (0.026, 0.05)          # USD par Go
GO_TELECHARGES = 40.0           # modèle et environnement, par instance
GO_SORTIS = 2.0                 # choix prudent de ce devis (voir bloc 6)

# --- constantes du préenregistrement court (v7 et corrections de sa contre-lecture) ---
ALPHA = 0.01
RISQUE_P1 = 0.025               # un bout certifié à 97,5 %
RISQUE_P2 = 0.0125              # deux bouts certifiés à 98,75 % (variante A, GO-2026-11-21-29)
E_PLAFOND = 0.05                # plafond de la bande d'équivalence e

# --- choix de ce devis ---
BORNE_HAUTE = 3 * 437           # 1 311 épisodes réels au plus pour cette part
LENTEUR_COUPURE = 1.5           # la coupure couvre la borne haute sur un hôte une fois et demie plus lent
RHOS = (0.0, 0.05, 0.10, 0.20, 0.30, 0.50)
FAMILLES = (40, 60, 80, 100, 150, 200, 300, 437)
REFERENCE = (150, 0.10)         # convention d'affichage, NON FONDÉE


def effectif_minimal(risque: float) -> int:
    """Plus petit n tel que le plus grand score honnête ait un taux réel d'au plus 1 % avec probabilité 1 - risque."""
    return math.ceil(math.log(risque) / math.log(1 - ALPHA))


def rang_haut(n: int, risque: float) -> int:
    r = 0
    while r + 1 <= n and beta(r + 1, n - r).cdf(ALPHA) >= 1 - risque:
        r += 1
    return r


def rang_plancher(n: int, risque: float) -> int:
    r = 1
    while beta(r, n - r + 1).sf(ALPHA) < 1 - risque:
        r += 1
    return r


def effectif_effectif(n: int, m: int, rho: float) -> int:
    return math.floor(n / (1 + (m - 1) * rho))


def plus_petit_plan(familles: int, rho: float, cible: int):
    """Plus petit nombre d'épisodes par famille m tel que l'effectif effectif atteigne la cible sous la borne haute."""
    m = 1
    while familles * m <= BORNE_HAUTE:
        if effectif_effectif(familles * m, m, rho) >= cible:
            return m, familles * m
        m += 1
    return None


def cout(n: int, instances: int = 1, lenteur: float = 1.0):
    """Heures de carte et USD (bas, haut) pour n épisodes ; `lenteur` multiplie toutes les heures."""
    heures = lenteur * (instances * FIXES_H + n * S_PAR_EPISODE / 3600)
    bas = heures * (PRIX[0] + DISQUE[0]) + instances * GO_TELECHARGES * TELECH[0] + GO_SORTIS * TELECH[0]
    haut = heures * (PRIX[1] + DISQUE[1]) + instances * GO_TELECHARGES * TELECH[1] + GO_SORTIS * TELECH[1]
    return heures, bas, haut


def pire(n: int, instances: int = 1):
    heures = 2 * (instances * FIXES_H + n * S_PAR_EPISODE / 3600)
    return heures, heures * (PRIX_PIRE + DISQUE[1]) + instances * GO_TELECHARGES * TELECH[1] + GO_SORTIS * TELECH[1]


def fr(x: float, d: int = 2) -> str:
    return f"{x:.{d}f}".replace(".", ",")


def main() -> None:
    ici = Path(__file__).resolve().parent
    releve = Path(sys.argv[1]) if len(sys.argv) > 1 else ici / "releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json"

    print("Devis de la part du lot honnête neuf L-1 qui étalonne P1 et P2 — calculs v1")
    print("Montants en USD. rho et F sont NON FONDÉS : grilles seulement.")
    print()

    print("Bloc 1 — effectifs effectifs exigés (recalcul)")
    n1, n2 = effectif_minimal(RISQUE_P1), effectif_minimal(RISQUE_P2)
    print(f"   P1, seuil haut certifié à 97,5 % : au moins {n1} épisodes honnêtes effectifs (rang haut à {n1} : {rang_haut(n1, RISQUE_P1)} ; à {n1 - 1} : {rang_haut(n1 - 1, RISQUE_P1)})")
    print(f"   P2, deux bouts certifiés à 98,75 % : au moins {n2} (rang haut à {n2} : {rang_haut(n2, RISQUE_P2)} ; à {n2 - 1} : {rang_haut(n2 - 1, RISQUE_P2)})")
    rh, rp = rang_haut(n2, RISQUE_P2), rang_plancher(n2, RISQUE_P2)
    k = rp - rh + 1
    cote = math.ceil(math.log(0.025 / (2 * k)) / math.log(1 - E_PLAFOND))
    print(f"   bande de P2 à {n2} : rangs {rh} à {rp}, K = {k} seuils ; plancher c_min sous e = {fr(E_PLAFOND)} dès {cote} épisodes effectifs par côté au lot d'évaluation (hors de ce devis)")
    print()

    print("Bloc 2 — coût d'un épisode honnête et frais fixes (carte A100 SXM4 de 80 Go)")
    h100 = 100 * S_PAR_EPISODE / 3600
    print(f"   {fr(S_PAR_EPISODE, 1)} s par épisode en lots de 8 : 100 épisodes = {fr(h100, 3)} h de carte, soit {fr(h100 * (PRIX[0] + DISQUE[0]))} à {fr(h100 * (PRIX[1] + DISQUE[1]))} USD ; au pire (hôte deux fois plus lent, {fr(PRIX_PIRE)} USD/h) {fr(2 * h100 * (PRIX_PIRE + DISQUE[1]))}")
    print(f"   frais fixes par instance : {fr(FIXES_H, 1)} h, soit {fr(FIXES_H * (PRIX[0] + DISQUE[0]))} à {fr(FIXES_H * (PRIX[1] + DISQUE[1]))} USD ; téléchargement {fr(GO_TELECHARGES, 0)} Go : {fr(GO_TELECHARGES * TELECH[0])} à {fr(GO_TELECHARGES * TELECH[1])} USD")
    print()

    print(f"Bloc 3 — épisodes réels à acheter pour {n2} épisodes effectifs, selon F (familles éligibles) et rho (corrélation par famille)")
    print(f"   règle : familles de taille égale m ; effectif effectif = plancher(F·m / (1 + (m − 1)·rho)) ; borne haute {BORNE_HAUTE} épisodes ; « — » = non jugeable sous la borne")
    print("   F \\ rho  " + "".join(f"{fr(r):>14}" for r in RHOS))
    for f in FAMILLES:
        ligne = []
        for r in RHOS:
            plan = plus_petit_plan(f, r, n2)
            ligne.append(f"{'—':>14}" if plan is None else f"{f'{plan[1]} (m={plan[0]})':>14}")
        print(f"   {f:>7}  " + "".join(ligne))
    print("   lecture : avec rho > 0, l'effectif effectif plafonne à F / rho quand m grandit ; il faut donc F > 437·rho, et bien plus pour tenir sous la borne")
    print()

    print(f"Bloc 4 — même table pour P1 seule ({n1} épisodes effectifs)")
    print("   F \\ rho  " + "".join(f"{fr(r):>14}" for r in RHOS))
    for f in FAMILLES:
        ligne = []
        for r in RHOS:
            plan = plus_petit_plan(f, r, n1)
            ligne.append(f"{'—':>14}" if plan is None else f"{f'{plan[1]} (m={plan[0]})':>14}")
        print(f"   {f:>7}  " + "".join(ligne))
    print()

    print("Bloc 5 — scénarios chiffrés, une instance")
    m_ref, n_ref = plus_petit_plan(REFERENCE[0], REFERENCE[1], n2)
    scenarios = (
        (f"bas : un épisode effectif par épisode réel (rho = 0, ou une tâche par famille), {n2} épisodes", n2),
        (f"cas de référence (convention NON FONDÉE : F = {REFERENCE[0]}, rho = {fr(REFERENCE[1])}, m = {m_ref}), {n_ref} épisodes", n_ref),
        (f"borne haute, {BORNE_HAUTE} épisodes", BORNE_HAUTE),
    )
    for nom, n in scenarios:
        h, b, hh = cout(n)
        hp, p = pire(n)
        print(f"   {nom}")
        print(f"      {fr(h)} h de carte ; {fr(b)} à {fr(hh)} USD ; pire cas {fr(p)} USD en {fr(hp)} h")
        h2, b2, hh2 = cout(n, instances=2)
        print(f"      sur deux instances : horloge {fr(FIXES_H + n * S_PAR_EPISODE / 7200)} h ; {fr(h2)} h de carte ; {fr(b2)} à {fr(hh2)} USD")
    hc, _, coupure_brute = cout(BORNE_HAUTE, lenteur=LENTEUR_COUPURE)
    coupure = math.ceil(coupure_brute)
    print(f"   coupure proposée : borne haute sur un hôte {fr(LENTEUR_COUPURE, 1)} fois plus lent, au prix haut : {fr(coupure_brute)} USD en {fr(hc)} h, arrondi à {coupure} USD")
    heures_sous_coupure = (coupure - GO_TELECHARGES * TELECH[1] - GO_SORTIS * TELECH[1]) / (PRIX_PIRE + DISQUE[1])
    episodes_pire = math.floor((heures_sous_coupure - 0.25 - 2 * FIXES_H) / (2 * S_PAR_EPISODE / 3600))
    print(f"   au pire cas, la coupure arrête la course vers {fr(heures_sous_coupure)} h : {episodes_pire} épisodes générés au lieu de {BORNE_HAUTE} (le pire cas entier, {fr(pire(BORNE_HAUTE)[1])} USD, n'est pas atteignable)")
    print()

    print("Bloc 6 — taille des sorties (dernier jeton de l'énoncé et de chaque action, couches 7, 15 et 23, demi-précision)")
    actions = 640 / 64      # inférence : 640 actions pour 64 épisodes au devis scellé du barreau 5 (calcul v3)
    octets = (actions + 1) * 3 * 4096 * 2
    print(f"   {fr(actions, 0)} actions par épisode (inféré, non mesuré ici) : {fr(octets / 1e6, 3)} Mo par épisode ; {BORNE_HAUTE} épisodes : {fr(BORNE_HAUTE * octets / 1e9, 2)} Go ; {fr(GO_SORTIS, 0)} Go comptés avec les textes et les journaux")
    par_jeton = 1.06 * 640 / 576 * 3 / 64
    print(f"   pour mémoire, série par jeton aux trois couches : {fr(par_jeton * 1000, 0)} Mo par épisode, {fr(par_jeton * BORNE_HAUTE, 0)} Go à la borne haute : non gardée ; relecture forcée à 0,45 s par passe d'épisode ({fr(BORNE_HAUTE * 0.45 / 60, 1)} min à la borne haute)")
    print()

    print("Bloc 7 — pour mémoire, parts de L-1 hors de ce devis (aucune ligne demandée)")
    for nom, n in (("100 épisodes de plus (moitiés de l'étape 2b, pré-mesure de l'étape 2a)", 100),
                   ("lot des gains de fusion, 5 000 épisodes effectifs, effet de plan 1", 5000),
                   ("le même, effet de plan 1,3", 6500),
                   ("le même, effet de plan 3", 15000)):
        h = n * S_PAR_EPISODE / 3600
        print(f"   {nom} : {fr(h, 1)} h de carte, {fr(h * (PRIX[0] + DISQUE[0]))} à {fr(h * (PRIX[1] + DISQUE[1]))} USD hors frais fixes")
    print()

    print(f"Bloc 8 — relevé du marché ({releve.name})")
    offres = json.loads(releve.read_text(encoding="utf-8"))["offers"]
    grandes = [o for o in offres if o.get("gpu_ram", 0) >= 80000]

    def conforme(o, disque):
        return (o["dph_total"] <= 1.30 and o["cpu_cores_effective"] >= 16 and o["cpu_ram"] >= 128000
                and o["disk_space"] >= disque and o["cuda_max_good"] >= 13.0
                and o.get("storage_cost", 0) * disque / 730 <= 0.08)

    print(f"   {len(offres)} offres A100 SXM4 à une carte, louables, à la demande ; {len(grandes)} de 80 Go ; prix des 80 Go : {fr(min(o['dph_total'] for o in grandes), 4)} à {fr(max(o['dph_total'] for o in grandes), 4)} USD/h")
    for disque in (80, 150, 300):
        ok = sorted(o["dph_total"] for o in grandes if conforme(o, disque))
        print(f"   bornes du devis scellé du barreau 5 (prix ≤ 1,30 ; cœurs ≥ 16 ; mémoire ≥ 128 000 Mo ; CUDA ≥ 13.0 ; stockage ≤ 0,08 USD/h) avec un disque d'au moins {disque} Go : {len(ok)} offre(s) : {', '.join(fr(p, 4) for p in ok) or 'aucune'}")
    ok80 = [o for o in grandes if conforme(o, 80)]
    if ok80:
        print(f"   sortie de données des offres conformes à 80 Go : {', '.join(fr(o['inet_up_cost'], 4) for o in ok80)} USD/Go ; entrée : {', '.join(fr(o['inet_down_cost'], 4) for o in ok80)} USD/Go")


if __name__ == "__main__":
    main()
