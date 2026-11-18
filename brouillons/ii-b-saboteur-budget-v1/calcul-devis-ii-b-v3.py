"""Arithmétique du devis du saboteur à budget (ii-b), course exploratoire — devis brouillon 4 (processeur, aucune donnée lue).

Nom neuf (R12) : `calcul-devis-ii-b-v2.py` (d869c8e8…) et sa sortie (abe794be…) restent tels quels. Ce script reprend leurs
hypothèses de durée à l'identique (fonction `heures`) et corrige ou ajoute, d'après la contre-lecture de l'ordre et du devis
(`docs/notes/barreau8-iib-v1/contre-lecture-ordre-et-devis-iib-v1.md`, `d398bf5c…`) :
- D-M1 : dernière commande de création à 23:00 UTC le 2026-11-25 (l'amorce rejoue le calendrier à l'heure de l'instance) ;
- D-M2 : les deux branches de l'activité interne, chiffrées (ordres de grandeur, hypothèses écrites ci-dessous) ;
- D-m1 : heures avant la coupure avec la formule du code (prix de l'offre + prix du stockage, `t06/session_v3.py` l. 95-100, lu
  par le contre-lecteur, non relu ici) ;
- D-m2 : plafond tenu par les gardes (coupure + consignation bornée + stockage à l'arrêt) ;
- D-m6 : essais du jetoniseur réel sur la carte (option).

Sources des entrées de durée et de prix : celles du calcul v2 (devis brouillon 2, § 1, `959df451…`, et code v3 `d88e3d94`).
Hypothèses propres aux deux branches de l'activité interne (contre-lecture, § 5.2 ; aucune n'est mesurée) :
- taille cachée 4 096, 32 couches (architecture publique du modèle, non relue sur pièce) ; un vecteur en demi-précision : 8 192 octets ;
- capture pendant les épisodes : aucun surcoût de durée (7a capturait sur la moitié des actions à 43,3 s par épisode : devis
  brouillon 2, § 1) ; morceaux de moins de 90 Mo (amorce v3, `MORCEAU_MAX_OCTETS` 90 000 000) ;
- passe de capture : une passe avant (sans génération) par épisode, 1,5 à 3,0 s par épisode : hypothèse du rédacteur, sans source ;
- recalcul plus tard, sur une location à part : durées fixes du devis (1,0 h ; 2,0 h hôte lent), stockage arrêté 24 h / 48 h,
  téléchargement 20 / 40 Go.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

EP_S = 43.3
FIXE_H = {"amorce, format et disque": 0.07, "suite ciblée": 0.58, "création, image et modèle (non relevé en 7a)": 0.25,
          "écriture, scellement, poussées": 0.10}
DIST_S_PAR_TRANSCRIPTION_EPOQUE = 891 / 480
EPOQUES = 3
N_ETALONNAGE_EP = 64 + 32
EP_PAR_TOUR = 32
N_EVAL_EP = 4 * 64
T = 10
ANCRAGE_ACTIONS = 320
STOCKAGE_USD_H, TELECH_USD_GO = 0.08, 0.05
STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU = 24, 20
STOCKAGE_H, TELECH_GO = 48, 40
COUPURE, LIGNE = 55, 60
CONSIGNATION_S = 2400
FIN_GO = datetime(2026, 11, 28, tzinfo=timezone.utc)
ECHEANCE_MINUTERIE = FIN_GO - timedelta(hours=2)
DERNIERE_COMMANDE = datetime(2026, 11, 25, 23, 0, tzinfo=timezone.utc)
JETONISEUR_SUR_CARTE_H = 0.1          # D-m6 : « quelques minutes » (contre-lecture) ; hypothèse du rédacteur, 6 min
OCTETS_VECTEUR, COUCHES = 4096 * 2, 32
MORCEAU_MAX = 90_000_000
PASSE_S = (1.5, 3.0)


def heures(tours: int, t_j: float, n_acc: int, lent: float = 1.0) -> dict:
    h = {"fixe": sum(FIXE_H.values()),
         "étalonnage : épisodes": N_ETALONNAGE_EP * EP_S / 3600,
         "étalonnage : jumeau": N_ETALONNAGE_EP * T * t_j / 3600,
         "maître : épisodes": tours * EP_PAR_TOUR * EP_S / 3600,
         "filtrage : jumeau du maître (et ancrage)": (tours * EP_PAR_TOUR * T + ANCRAGE_ACTIONS) * t_j / 3600,
         "distillation (élève et témoin-jumeau)": (2 * n_acc * EPOQUES * DIST_S_PAR_TRANSCRIPTION_EPOQUE / 3600 + 0.01) if n_acc else 0.0,
         "évaluation : épisodes": (N_EVAL_EP * EP_S / 3600) if n_acc else 0.0,
         "évaluation : jumeau (lecture 1)": (N_EVAL_EP * T * t_j / 3600) if n_acc else 0.0}
    h = {k: v * lent for k, v in h.items()}
    h["total"] = sum(h.values())
    return h


def usd(h: float, prix: float, st: float, tg: float) -> float:
    return h * prix + st * STOCKAGE_USD_H + tg * TELECH_USD_GO


def main() -> None:
    print("Devis (ii-b), brouillon 4 — arithmétique (calcul v3) ; heures de carte ; USD")
    central, haut, p1 = heures(10, 1.0, 96), heures(12, 1.5, 127), heures(12, 3.0, 127, lent=2.0)
    print("\n## Rappel (identique au calcul v2)")
    print(f"  central {central['total']:.2f} h : {usd(central['total'], 1.12, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU):.1f} USD à 1,12")
    print(f"  haut {haut['total']:.2f} h : {usd(haut['total'], 1.30, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU):.1f} USD à 1,30")
    print(f"  P1 {p1['total']:.2f} h : {usd(p1['total'], 1.30, STOCKAGE_H, TELECH_GO):.1f} USD à 1,30 ; "
          f"{usd(p1['total'], 1.40, STOCKAGE_H, TELECH_GO):.1f} USD à 1,40")

    print("\n## D-m1 : heures avant la coupure de 55 USD, formule du code (prix de l'offre + stockage 0,08 ; téléchargement 40 Go déduit)")
    for prix in (1.12, 1.30, 1.40):
        dispo = (COUPURE - TELECH_GO * TELECH_USD_GO) / (prix + STOCKAGE_USD_H)
        print(f"  à {prix} + 0,08 USD/h : {dispo:.1f} h ; marge sur P1 ({p1['total']:.2f} h) : {dispo - p1['total']:.1f} h")

    print("\n## D-m2 : plafond tenu par les gardes")
    for prix in (1.30, 1.40):
        consig = CONSIGNATION_S / 3600 * (prix + STOCKAGE_USD_H)
        tot = COUPURE + consig + STOCKAGE_H * STOCKAGE_USD_H
        print(f"  à {prix} : coupure {COUPURE} + consignation ≤ {consig:.2f} + stockage arrêté 48 h {STOCKAGE_H * STOCKAGE_USD_H:.2f} "
              f"= au plus {tot:.2f} USD ; sous la ligne {LIGNE} : {'oui' if tot <= LIGNE else 'NON'}, marge {LIGNE - tot:.2f}")
        h_max = (LIGNE - COUPURE - consig) / STOCKAGE_USD_H
        print(f"    heures d'arrêt au plus avant de dépasser la ligne : {h_max:.0f} h")

    print("\n## D-M1 : dernière commande de création")
    for nom, h in (("haut", haut), ("P1", p1)):
        fin = DERNIERE_COMMANDE + timedelta(hours=h["total"])
        print(f"  création {DERNIERE_COMMANDE.isoformat(timespec='minutes')} + {nom} {h['total']:.2f} h → fin "
              f"{fin.isoformat(timespec='minutes')} ; avant l'échéance de la minuterie ({ECHEANCE_MINUTERIE.isoformat(timespec='minutes')}) : "
              f"{'oui' if fin <= ECHEANCE_MINUTERIE else 'NON'}, marge {(ECHEANCE_MINUTERIE - fin).total_seconds() / 3600:.1f} h")

    print("\n## D-m6 : essais du jetoniseur réel sur la carte (option, si joués par l'amorce)")
    print(f"  + {JETONISEUR_SUR_CARTE_H:.2f} h : {JETONISEUR_SUR_CARTE_H * 1.12:.2f} USD à 1,12 ; "
          f"{JETONISEUR_SUR_CARTE_H * 2 * 1.40:.2f} USD au pire (hôte ×2, 1,40)")

    print("\n## D-M2 : activité interne — branche A (enregistrer pendant la course)")
    act_eval = N_EVAL_EP * T
    act_tout = (N_ETALONNAGE_EP + 12 * EP_PAR_TOUR + N_EVAL_EP) * T
    print(f"  actions : évaluation {act_eval} ; toutes phases au plus {act_tout}")
    for nom, n in (("évaluation", act_eval), ("toutes phases", act_tout)):
        par_couche = n * OCTETS_VECTEUR
        print(f"  {nom}, un vecteur par action : {par_couche / 1e6:.0f} Mo par couche ; {par_couche * COUCHES / 1e9:.2f} Go pour {COUCHES} couches "
              f"({-(-par_couche * COUCHES // MORCEAU_MAX)} morceaux de 90 Mo) ; tous les jetons générés (400 au plus par action) : "
              f"{par_couche * 400 / 1e9:.1f} Go par couche")
    ep_eval, ep_tout = N_EVAL_EP, N_ETALONNAGE_EP + 12 * EP_PAR_TOUR + N_EVAL_EP
    bas_h, haut_h = ep_eval * PASSE_S[0] / 3600, ep_tout * PASSE_S[1] / 3600
    print(f"  capture pendant les épisodes : 0 h de plus (hypothèse : comme 7a)")
    print(f"  passe de capture après l'évaluation : {bas_h:.2f} h ({ep_eval} épisodes × {PASSE_S[0]} s) à {haut_h:.2f} h "
          f"({ep_tout} épisodes × {PASSE_S[1]} s) ; {bas_h * 1.12:.2f} à {haut_h * 1.40:.2f} USD ; au pire (hôte ×2) "
          f"{2 * haut_h:.2f} h, {2 * haut_h * 1.40:.2f} USD")
    p1_a = p1["total"] + 2 * haut_h
    print(f"  P1 avec passe finale : {p1_a:.2f} h ; {usd(p1_a, 1.40, STOCKAGE_H, TELECH_GO):.1f} USD à 1,40 ; "
          f"heures avant la coupure à 1,40 + 0,08 : {(COUPURE - TELECH_GO * TELECH_USD_GO) / 1.48:.1f} h, marge "
          f"{(COUPURE - TELECH_GO * TELECH_USD_GO) / 1.48 - p1_a:.1f} h")

    print("\n## D-M2 : activité interne — branche B (garder de quoi recalculer, passe plus tard sur une location à part)")
    print("  pendant la course : 0 h, 0 USD de plus")
    for nom, fixe, passe, prix, st, tg in (("attendu", 1.0, (bas_h, haut_h), 1.12, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU),
                                           ("pire (hôte ×2)", 2.0, (2 * bas_h, 2 * haut_h), 1.40, STOCKAGE_H, TELECH_GO)):
        h_b, h_h = fixe + passe[0], fixe + passe[1]
        print(f"  plus tard, {nom} : {h_b:.2f} à {h_h:.2f} h ; {usd(h_b, prix, st, tg):.1f} à {usd(h_h, prix, st, tg):.1f} USD "
              f"(stockage {st} h, téléchargement {tg} Go)")


if __name__ == "__main__":
    main()
