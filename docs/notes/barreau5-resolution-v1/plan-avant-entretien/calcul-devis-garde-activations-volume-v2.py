#!/usr/bin/env python3
"""Barreau 5 : devis de la garde des activations de la relecture sur un volume de stockage — calcul v2.

Ce qui change depuis le calcul v1 (a3049f4b…), après la contre-lecture du devis v1 (1d0e7861…) :
- l'adresse IPv4 publique de chaque serveur de séance est comptée (correction A-3) ; les chiffres sans elle,
  ceux de la v1, sont imprimés à côté ;
- le coût par jour de la garde sans séance est imprimé en USD (correction A-1) ;
- les offres qui ne manquent que la borne du stockage sont comptées (correction A-4) ;
- un bloc d'objets de contrôle éprouve la règle « le cumul reste sous le plafond » sur des cas où elle est fausse
  par construction et sur un cas où elle est vraie ; le programme sort en code 1 si un rendu diffère de l'attendu.

Aucune donnée du programme n'est lue. Deux entrées, versées à côté : la grille de prix de Hetzner relevée le
2026-11-21 à 10:56:21Z (`GET /v1/pricing` : prix publics et taux de taxe du compte, aucune donnée du projet) et le
relevé public des offres du loueur de cartes du même jour, 10:55:20Z.
Lancer : `.venv/bin/python -I docs/notes/barreau5-resolution-v1/plan-avant-entretien/calcul-devis-garde-activations-volume-v2.py`.

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


def main() -> int:
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
    ipv4_ht = next(float(pr["price_hourly"]["net"]) for ip in p["primary_ips"] if ip["type"] == "ipv4"
                   for pr in ip["prices"] if pr["location"] == LIEU)
    ipv4_mois_ht = next(float(pr["price_monthly"]["net"]) for ip in p["primary_ips"] if ip["type"] == "ipv4"
                        for pr in ip["prices"] if pr["location"] == LIEU)

    print("Barreau 5 — garde des activations sur un volume de stockage — calcul v2")
    print(f"Grille : {grille.name} ; devise {p['currency']} ; taxe {fr(float(p['vat_rate']), 0)} % ; taux employé {fr(TAUX)} USD pour 1 EUR (convention, non relevé)")
    print()

    print("Bloc 1 — prix relevés")
    print(f"   volume : {fr(go_mois_ht, 4)} EUR hors taxe par Go et par mois ({fr(go_mois_ttc, 5)} toutes taxes)")
    for nom in (SERVEUR_BAS, SERVEUR_HAUT):
        h, m = serveurs[nom]
        print(f"   serveur {nom} à {LIEU} : {fr(h, 4)} EUR hors taxe de l'heure ({fr(h * tva, 5)} toutes taxes) ; plafond mensuel {fr(m)} hors taxe")
    print(f"   adresse IPv4 publique d'un serveur à {LIEU} : {fr(ipv4_ht, 4)} EUR hors taxe de l'heure ({fr(ipv4_ht * tva, 5)} toutes taxes) ; plafond mensuel {fr(ipv4_mois_ht)} hors taxe")
    print()

    vol_mois = GO_VOLUME * go_mois_ttc
    vol_jour = vol_mois / JOURS_PAR_MOIS
    print("Bloc 2 — le volume, toutes taxes")
    for nom, go in ((f"{GO_VOLUME} Go (≈ 152 à 166 Go d'activations)", GO_VOLUME), (f"{GO_REPLI_1} Go (repli 1, ≈ 44 Go)", GO_REPLI_1)):
        mois = go * go_mois_ttc
        print(f"   {nom} : {fr(mois)} EUR par mois, soit {fr(mois * TAUX)} USD ; par jour {fr(mois / JOURS_PAR_MOIS, 3)} EUR, soit {fr(mois / JOURS_PAR_MOIS * TAUX)} USD")
    print()

    def seance(nom: str, heures: float, adresse: bool = True) -> float:
        return heures * (serveurs[nom][0] + (ipv4_ht if adresse else 0.0)) * tva

    print("Bloc 3 — le serveur, par séance (versement ou relecture), toutes taxes, adresse IPv4 comprise")
    for nom in (SERVEUR_BAS, SERVEUR_HAUT):
        print(f"   {nom} : " + " ; ".join(f"{t} h = {fr(seance(nom, t), 3)} EUR" for t in HEURES_SERVEUR))
    print(f"   part de l'adresse IPv4 : {fr(seance(SERVEUR_BAS, 24) - seance(SERVEUR_BAS, 24, False), 3)} EUR par séance de 24 h ; {fr(SEANCES_PLAFOND * (seance(SERVEUR_BAS, 24) - seance(SERVEUR_BAS, 24, False)), 3)} EUR pour {SEANCES_PLAFOND} séances de 24 h")
    print()

    def scenarios(adresse: bool):
        bas = vol_mois * ECHEANCE_JOURS[0] / JOURS_PAR_MOIS + seance(SERVEUR_BAS, HEURES_SERVEUR[0], adresse)
        attendu = vol_mois + seance(SERVEUR_BAS, HEURES_SERVEUR[1], adresse)
        pire = vol_mois + SEANCES_PLAFOND * seance(SERVEUR_HAUT, HEURES_SERVEUR[2], adresse)
        return bas, attendu, pire

    print("Bloc 4 — scénarios, adresse IPv4 comprise (entre parenthèses : sans elle, chiffres du calcul v1)")
    (bas, attendu, pire), (bas1, attendu1, pire1) = scenarios(True), scenarios(False)
    print(f"   bas : volume gardé {ECHEANCE_JOURS[0]} jours (jusqu'au 1er décembre), une séance de {HEURES_SERVEUR[0]} h sur {SERVEUR_BAS} : {fr(bas)} EUR = {fr(bas * TAUX)} USD ({fr(bas1)} EUR = {fr(bas1 * TAUX)} USD)")
    print(f"   attendu : volume gardé un mois entier (jusqu'au 21 décembre), une séance de {HEURES_SERVEUR[1]} h sur {SERVEUR_BAS} : {fr(attendu)} EUR = {fr(attendu * TAUX)} USD ({fr(attendu1)} EUR = {fr(attendu1 * TAUX)} USD)")
    print(f"   pire cas sous les coupures : un mois entier, {SEANCES_PLAFOND} séances de {HEURES_SERVEUR[2]} h sur {SERVEUR_HAUT} : {fr(pire)} EUR = {fr(pire * TAUX)} USD ({fr(pire1)} EUR = {fr(pire1 * TAUX)} USD)")
    plafond = math.ceil(pire * TAUX)
    print(f"   plafond proposé : {plafond} USD ; marge sur le pire cas : {fr(plafond - pire * TAUX)} USD")
    oubli1 = vol_mois + serveurs[SERVEUR_HAUT][1] * tva
    oubli = oubli1 + ipv4_mois_ht * tva
    print(f"   ce que la minuterie évite : un serveur {SERVEUR_HAUT} laissé en marche un mois entier, {fr(oubli)} EUR = {fr(oubli * TAUX)} USD (sans l'adresse : {fr(oubli1)} EUR = {fr(oubli1 * TAUX)} USD)")
    print(f"   chaque mois de garde de plus, volume seul : {fr(vol_mois)} EUR = {fr(vol_mois * TAUX)} USD")
    print(f"   garde sans séance après l'échéance ou au plafond, volume seul : {fr(vol_jour, 3)} EUR = {fr(vol_jour * TAUX)} USD par jour ; {fr(7 * vol_jour * TAUX)} USD par semaine")
    print()

    print("Bloc 5 — autres lieux")
    boite = BOITE_EUR_HT * tva
    print(f"   boîte de stockage de 1 To (page publique : {fr(BOITE_EUR_HT)} EUR hors taxe par mois) : {fr(boite)} EUR toutes taxes = {fr(boite * TAUX)} USD par mois, sans serveur pour le dépôt ; volume de {GO_VOLUME} Go : {fr(vol_mois * TAUX)} USD par mois, soit {fr(vol_mois / boite, 1)} fois plus")
    print("   frais d'installation de la boîte, mode de commande, lecture depuis un serveur du projet : NON vérifiés")
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
    print(f"   prix de stockage le plus bas vu : {fr(min(o['storage_cost'] for o in liste), 2)} USD par Go et par mois, soit {fr(min(o['storage_cost'] for o in liste) * 300 / 730, 4)} USD/h à 300 Go")
    proches = sorted((o for o in liste if refus(o, 300) == ["stockage"]), key=lambda o: o["dph_total"])
    print(f"   offres refusées pour le seul stockage : {len(proches)}")
    for o in proches:
        print(f"      {fr(o['dph_total'], 4)} USD/h, stockage {fr(o['storage_cost'], 2)} USD par Go et par mois, soit {fr(o['storage_cost'] * 300 / 730, 4)} USD/h à 300 Go ; sortie de données {fr(o['inet_up_cost'], 4)} USD/Go, soit {fr(166 * o['inet_up_cost'])} USD pour 166 Go")
    print()

    print("Bloc 7 — objets de contrôle de la règle « le cumul reste sous le plafond »")
    print("   attendu écrit avant le rejeu ; « faux » : le cas doit dépasser le plafond ; « vrai » : il doit tenir dessous")
    h24 = seance(SERVEUR_HAUT, 24)
    objets = (
        ("vrai par construction : un mois de volume, trois séances de 24 h sur le serveur haut", vol_mois + 3 * h24, True),
        ("faux par construction : une quatrième séance de 24 h", vol_mois + 4 * h24, False),
        ("faux par construction : une séance sans minuterie, serveur haut laissé un mois", oubli, False),
        ("faux par construction : le pire cas, puis dix jours de garde sans séance après l'échéance", pire + 10 * vol_jour, False),
    )
    conforme = True
    for nom, eur, attendu_sous in objets:
        rendu = eur * TAUX <= plafond
        conforme = conforme and (rendu == attendu_sous)
        print(f"   {nom} : {fr(eur)} EUR = {fr(eur * TAUX)} USD ; sous {plafond} USD attendu : {'oui' if attendu_sous else 'non'} ; rendu : {'oui' if rendu else 'non'}")
    print(f"   objets de contrôle : {"tous conformes à l'attendu" if conforme else "ÉCART"}")
    return 0 if conforme else 1


if __name__ == "__main__":
    sys.exit(main())
