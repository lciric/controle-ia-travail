#!/usr/bin/env python3
"""Barreau 5 : devis de la garde des activations de la relecture sur un volume de stockage — calcul v1.

Aucune donnée du programme n'est lue. Deux entrées, versées à côté : la grille de prix de Hetzner relevée le
2026-11-21 à 10:56:21Z (`GET /v1/pricing`, prix publics, aucune donnée du projet) et le relevé public des offres
du loueur de cartes du même jour, 10:55:20Z (chemin en second argument, sinon celui du devis du lot honnête neuf).
Lancer : `.venv/bin/python -I docs/notes/barreau5-resolution-v1/plan-avant-entretien/calcul-devis-garde-activations-volume-v1.py`.

Tailles : texte scellé du barreau 5, « Données gardées » (≈ 152 Go ; 166 Go avec les quatre ancrages ; replis 44 et
4,4 Go) et devis scellé, § 5. Taux de change : 1,25 USD pour 1 EUR, convention de `registres/depenses.md`, l. 422 ;
le taux du jour n'est PAS relevé. Durées de marche du serveur : choix de ce devis, non mesurés.
"""
import json
import math
import sys
from pathlib import Path

TAUX = 1.25                     # USD pour 1 EUR, convention du registre des dépenses (l. 422)
GO_VOLUME = 200
GO_REPLI_1 = 50                 # volume pour le repli 1 (≈ 44 Go)
JOURS_PAR_MOIS = 30
SERVEUR_BAS, SERVEUR_HAUT = "cx23", "ccx13"
LIEU = "hel1"
HEURES_SERVEUR = (6, 12, 24)    # bas, attendu, coupure par séance (minuterie de destruction)
SEANCES_PLAFOND = 3             # versement, puis deux relectures au plus sous la ligne
ECHEANCE_JOURS = (9, 30)        # jusqu'au 1er décembre ; jusqu'au 21 décembre (un mois entier compté)
BOITE_EUR_HT = 3.20             # boîte de stockage de 1 To, page publique relevée le 2026-11-21 à 10:55:40Z


def fr(x: float, d: int = 2) -> str:
    return f"{x:.{d}f}".replace(".", ",")


def main() -> None:
    ici = Path(__file__).resolve().parent
    grille = Path(sys.argv[1]) if len(sys.argv) > 1 else ici / "releve-grille-prix-hetzner-2026-11-21T1056Z-v1.json"
    offres = Path(sys.argv[2]) if len(sys.argv) > 2 else (
        ici.parents[3] / "prereg/papier-dopamine-moniteur-v1/releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json")
    p = json.loads(grille.read_text(encoding="utf-8"))["pricing"]
    tva = 1 + float(p["vat_rate"]) / 100
    go_mois_ht = float(p["volume"]["price_per_gb_month"]["net"])
    go_mois_ttc = float(p["volume"]["price_per_gb_month"]["gross"])
    serveurs = {}
    for st in p["server_types"]:
        for pr in st["prices"]:
            if pr["location"] == LIEU:
                serveurs[st["name"]] = (float(pr["price_hourly"]["net"]), float(pr["price_monthly"]["net"]))

    print("Barreau 5 — garde des activations sur un volume de stockage — calcul v1")
    print(f"Grille : {grille.name} ; devise {p['currency']} ; taxe {fr(float(p['vat_rate']), 0)} % ; taux employé {fr(TAUX)} USD pour 1 EUR (convention, non relevé)")
    print()

    print("Bloc 1 — prix relevés")
    print(f"   volume : {fr(go_mois_ht, 4)} EUR hors taxe par Go et par mois ({fr(go_mois_ttc, 5)} toutes taxes)")
    for nom in (SERVEUR_BAS, SERVEUR_HAUT):
        h, m = serveurs[nom]
        print(f"   serveur {nom} à {LIEU} : {fr(h, 4)} EUR hors taxe de l'heure ({fr(h * tva, 5)} toutes taxes) ; plafond mensuel {fr(m)} hors taxe")
    print()

    print("Bloc 2 — le volume, toutes taxes")
    for nom, go in ((f"{GO_VOLUME} Go (≈ 152 à 166 Go d'activations)", GO_VOLUME), (f"{GO_REPLI_1} Go (repli 1, ≈ 44 Go)", GO_REPLI_1)):
        mois = go * go_mois_ttc
        print(f"   {nom} : {fr(mois)} EUR par mois, soit {fr(mois * TAUX)} USD ; par jour {fr(mois / JOURS_PAR_MOIS, 3)} EUR")
    print()

    print("Bloc 3 — le serveur, par séance (versement ou relecture), toutes taxes")
    for nom in (SERVEUR_BAS, SERVEUR_HAUT):
        h = serveurs[nom][0] * tva
        print(f"   {nom} : " + " ; ".join(f"{t} h = {fr(t * h, 3)} EUR" for t in HEURES_SERVEUR))
    print()

    print("Bloc 4 — scénarios")
    vol_mois = GO_VOLUME * go_mois_ttc
    bas = vol_mois * ECHEANCE_JOURS[0] / JOURS_PAR_MOIS + HEURES_SERVEUR[0] * serveurs[SERVEUR_BAS][0] * tva
    attendu = vol_mois + HEURES_SERVEUR[1] * serveurs[SERVEUR_BAS][0] * tva
    pire = vol_mois + SEANCES_PLAFOND * HEURES_SERVEUR[2] * serveurs[SERVEUR_HAUT][0] * tva
    print(f"   bas : volume gardé {ECHEANCE_JOURS[0]} jours (jusqu'au 1er décembre), une séance de {HEURES_SERVEUR[0]} h sur {SERVEUR_BAS} : {fr(bas)} EUR = {fr(bas * TAUX)} USD")
    print(f"   attendu : volume gardé un mois entier (jusqu'au 21 décembre), une séance de {HEURES_SERVEUR[1]} h sur {SERVEUR_BAS} : {fr(attendu)} EUR = {fr(attendu * TAUX)} USD")
    print(f"   pire cas sous les coupures : un mois entier, {SEANCES_PLAFOND} séances de {HEURES_SERVEUR[2]} h sur {SERVEUR_HAUT} : {fr(pire)} EUR = {fr(pire * TAUX)} USD")
    plafond = math.ceil(pire * TAUX)
    print(f"   plafond proposé : {plafond} USD")
    oubli = vol_mois + serveurs[SERVEUR_HAUT][1] * tva
    print(f"   ce que la minuterie évite : un serveur {SERVEUR_HAUT} laissé en marche un mois entier, {fr(oubli)} EUR = {fr(oubli * TAUX)} USD")
    print(f"   chaque mois de garde de plus, volume seul : {fr(vol_mois)} EUR = {fr(vol_mois * TAUX)} USD")
    print()

    print("Bloc 5 — autres lieux, pour mémoire")
    boite = BOITE_EUR_HT * tva
    print(f"   boîte de stockage de 1 To (page publique : {fr(BOITE_EUR_HT)} EUR hors taxe par mois) : {fr(boite)} EUR toutes taxes = {fr(boite * TAUX)} USD par mois, sans serveur ; frais d'installation et mode de commande NON vérifiés")
    print(f"   repli 1 sur un volume de {GO_REPLI_1} Go : {fr(GO_REPLI_1 * go_mois_ttc)} EUR = {fr(GO_REPLI_1 * go_mois_ttc * TAUX)} USD par mois")
    print("   repli 2 : sans dépense (≈ 4,4 Go en morceaux sur la branche de lecture)")
    print("   disque de l'instance arrêtée : jusqu'à 0,08 USD de l'heure, ≈ 58 USD par mois (devis scellé, § 5 (d))")
    print()

    print(f"Bloc 6 — constat du marché des cartes pour l'instance de relecture ({offres.name})")
    liste = [o for o in json.loads(offres.read_text(encoding="utf-8"))["offers"] if o.get("gpu_ram", 0) >= 80000]

    def refus(o, disque):
        r = []
        if o["dph_total"] > 1.30:
            r.append("prix")
        if o["cpu_cores_effective"] < 16:
            r.append("cœurs")
        if o["cpu_ram"] < 128000:
            r.append("mémoire")
        if o["disk_space"] < disque:
            r.append("disque")
        if o["cuda_max_good"] < 13.0:
            r.append("CUDA")
        if o.get("storage_cost", 0) * disque / 730 > 0.08:
            r.append("stockage")
        return r

    for disque in (150, 300):
        ok = sorted(o["dph_total"] for o in liste if not refus(o, disque))
        print(f"   disque d'au moins {disque} Go : {len(ok)} offre(s) conforme(s) sur {len(liste)} cartes de 80 Go : {', '.join(fr(x, 4) for x in ok) or 'aucune'}")
    compte = {}
    for o in liste:
        for r in refus(o, 300):
            compte[r] = compte.get(r, 0) + 1
    print("   motifs de refus à 300 Go (une offre peut en porter plusieurs) : " + ", ".join(f"{k} {v}" for k, v in sorted(compte.items())))
    proches = [o for o in liste if refus(o, 300) == ["stockage"]]
    for o in proches:
        print(f"   refusée pour le seul stockage : {fr(o['dph_total'], 4)} USD/h, stockage {fr(o['storage_cost'], 2)} USD par Go et par mois, soit {fr(o['storage_cost'] * 300 / 730, 4)} USD/h à 300 Go ; sortie de données {fr(o['inet_up_cost'], 4)} USD/Go, soit {fr(166 * o['inet_up_cost'])} USD pour 166 Go")


if __name__ == "__main__":
    main()
