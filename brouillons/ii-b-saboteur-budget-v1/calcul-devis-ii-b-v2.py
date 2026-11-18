"""Arithmétique du devis du saboteur à budget (ii-b), course exploratoire — devis brouillon 3 (processeur, aucune donnée lue).

Nom neuf (R12) : `calcul-devis-ii-b-v1.py` (bb7dd00e…) et sa sortie (15d5fcc0…) restent tels quels ; ce script reprend leurs
hypothèses de durée à l'identique et ajoute :
- le juge de T0.8 hors des totaux : le code v3 (`origin/prep/iib-code-v3`, `d88e3d94`, `iib/configuration_v1.py`) refuse une
  configuration qui annonce sa forme scellée et ne joue aucune passe ; il reste une ligne d'option, chiffrée à part ;
- les deux variantes de plafond côte à côte (A : ligne 80, configuration 75, repli H200 NVL ; B : ligne 60, configuration 55,
  A100 seule), contre la ligne d'accord inscrite (GO-2026-11-10-08 : 60 USD, échéance 2026-11-27, « option B de M7 ; coupure à
  55 USD ») ;
- la coupure par pièce (carte, stockage, téléchargement) et par point d'arrêt (épreuves de l'oracle, contrôle du tour 4, fin des
  tours sans assez d'acceptés, course entière) ;
- les heures de carte disponibles avant la coupure de la configuration, à chaque prix ;
- le calendrier : fin du GO (lendemain 00:00 UTC de l'échéance, règle du code, `t06/session_v3.verifier_calendrier_v3`),
  échéance de la minuterie proposée (deux heures avant), dernière création sans nœud au pire cas.

Sources des entrées (citées par le devis brouillon 2, `959df451…`, section 1, non relues ici sauf mention) :
- débit d'épisode 43,3 s et durées fixes : lecture A de 7a (`lecture-A-exploratoire-non-opposable-v1.md`, `3c84c419…`, § 4) ;
- distillation : 7a, 14 min 51 s pour 160 transcriptions × 3 époques ;
- jumeau honnête : NON MESURÉ (0,5 / 1,0 / 1,5 s par action attendu, 3,0 s au pire) ;
- prix : A100 SXM4 80 Go 1,12 USD/h central (consigne de la mère), relevés 1,009 à 1,2133 (T0.6 candidat 12 r3, `c24e268e…`),
  borne 1,30 (configuration du candidat 12, brouillon 5, `b7a5c1ba…` ; et code v3 : `carte.course.prix_max_usd_h` = 1,3), pire
  1,40 ; H200 NVL relevés 4,441 et 4,669, borne 4,70 (mêmes sources ; code v3 : `carte.relance.prix_max_usd_h` = 4,7) ;
- stockage ≤ 0,08 USD/h et téléchargement ≤ 0,05 USD/Go : code v3, `STOCKAGE_MAX_USD_H`, `TELECHARGEMENT_MAX_USD_GO` ;
- marge de la minuterie de l'instance : 1 800 s (amorce v3, `MINUTERIE_MARGE_S`), consignation bornée à 2 400 s (amorce v3).
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
JUGE_UNE_PASSE_S = 0.3
STOCKAGE_USD_H, TELECH_USD_GO = 0.08, 0.05
STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU = 24, 20
STOCKAGE_H, TELECH_GO = 48, 40
VARIANTES = {"A": {"ligne": 80, "configuration": 75, "repli_h200": True},
             "B": {"ligne": 60, "configuration": 55, "repli_h200": False}}
LIGNE_INSCRITE = {"go": "GO-2026-11-10-08", "plafond": 60, "echeance": date(2026, 11, 27)}
MARGE_MINUTERIE_H = 1800 / 3600
AVANCE_ECHEANCE_MINUTERIE_H = 2.0      # proposée : échéance de la minuterie = fin du GO − 2 h (consignation 2 400 s + marge 1 800 s)
ETAPES_ARRET = ("fixe", "étalonnage : épisodes", "étalonnage : jumeau")


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


def usd(total_h: float, prix: float, stockage_h: float, telech_go: float) -> dict:
    c, s, t = total_h * prix, stockage_h * STOCKAGE_USD_H, telech_go * TELECH_USD_GO
    return {"carte": c, "stockage": s, "telechargement": t, "total": c + s + t}


def ligne_usd(nom: str, total_h: float, prix: float, stockage_h: float, telech_go: float) -> dict:
    u = usd(total_h, prix, stockage_h, telech_go)
    print(f"  {nom} : {total_h:.2f} h × {prix:.4g} USD/h = carte {u['carte']:.1f} + stockage arrêté ≤ {u['stockage']:.1f} "
          f"({stockage_h} h) + téléchargement ≤ {u['telechargement']:.1f} ({telech_go} Go) = {u['total']:.1f} USD")
    return u


def imprimer_heures(nom: str, h: dict) -> None:
    print(f"\n## {nom}")
    for k, v in h.items():
        print(f"  {k} : {v:.2f} h")


def main() -> None:
    print("Devis (ii-b), brouillon 3 — arithmétique (calcul v2) ; heures de carte ; USD ; juge de T0.8 hors des totaux")

    scen = {"bas": heures(6, 0.5, 96), "central": heures(10, 1.0, 96), "haut": heures(12, 1.5, 127),
            "P1": heures(12, 3.0, 127, lent=2.0)}
    imprimer_heures("Attendu bas : 6 tours, jumeau 0,5 s/action, 96 acceptés", scen["bas"])
    imprimer_heures("Attendu central : 10 tours, jumeau 1,0 s/action, 96 acceptés", scen["central"])
    imprimer_heures("Attendu haut : 12 tours, jumeau 1,5 s/action, 127 acceptés", scen["haut"])
    imprimer_heures("Pire P1 : hôte deux fois plus lent, 12 tours, jumeau 3,0 s/action, 127 acceptés", scen["P1"])

    print("\n## Attendu, en USD (stockage arrêté 24 h, téléchargement 20 Go)")
    ligne_usd("bas à 1,0889", scen["bas"]["total"], 1.0889, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)
    ligne_usd("central à 1,12", scen["central"]["total"], 1.12, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)
    ligne_usd("central à 1,30", scen["central"]["total"], 1.30, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)
    ligne_usd("haut à 1,30", scen["haut"]["total"], 1.30, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU)

    print("\n## Pire cas, en USD (stockage arrêté 48 h, téléchargement 40 Go)")
    p1 = {p: ligne_usd(f"P1 à {p}", scen["P1"]["total"], p, STOCKAGE_H, TELECH_GO) for p in (1.30, 1.40, 2.10)}
    h200 = {p: ligne_usd(f"H200 NVL d'emblée (durées du haut de l'attendu) à {p}", scen["haut"]["total"], p, STOCKAGE_H, TELECH_GO)
            for p in (4.441, 4.669, 4.70)}
    ligne_usd("P1 joué sur H200 NVL à 4,70", scen["P1"]["total"], 4.70, STOCKAGE_H, TELECH_GO)

    print("\n## Coupure par point d'arrêt (heures de carte ; USD au prix indiqué, stockage arrêté et téléchargement de l'attendu)")
    for nom_s, (tours, t_j, lent, prix, st, tg) in {
            "central": (10, 1.0, 1.0, 1.12, STOCKAGE_H_ATTENDU, TELECH_GO_ATTENDU),
            "P1": (12, 3.0, 2.0, 1.40, STOCKAGE_H, TELECH_GO)}.items():
        print(f" scénario {nom_s} ({prix} USD/h, stockage {st} h, téléchargement {tg} Go) :")
        h_ep = sum(v for k, v in heures(0, t_j, 0, lent).items() if k in ETAPES_ARRET)
        ligne_usd("arrêt aux épreuves de l'oracle (fin de l'étalonnage)", h_ep, prix, st, tg)
        h4 = heures(4, t_j, 0, lent)["total"]
        ligne_usd("arrêt au contrôle du tour 4 (rien n'est distillé)", h4, prix, st, tg)
        h12 = heures(12, t_j, 0, lent)["total"]
        ligne_usd("arrêt à la fin du tour 12, moins de 48 acceptés (rien n'est distillé)", h12, prix, st, tg)
        ligne_usd("course entière", scen[nom_s]["total"], prix, st, tg)

    print("\n## Pièces (central à 1,12 USD/h, 24 h de stockage arrêté, 20 Go)")
    for k, v in scen["central"].items():
        if k != "total":
            print(f"  {k} : {v:.2f} h ; {v * 1.12:.2f} USD")
    print(f"  stockage arrêté : {STOCKAGE_H_ATTENDU * STOCKAGE_USD_H:.2f} USD ; téléchargement : {TELECH_GO_ATTENDU * TELECH_USD_GO:.2f} USD")

    print("\n## Variantes de plafond, côte à côte, contre la ligne inscrite")
    for v, d in VARIANTES.items():
        print(f" variante {v} : ligne {d['ligne']} USD, configuration {d['configuration']} USD, repli H200 NVL : "
              f"{'oui' if d['repli_h200'] else 'non'} ; ligne inscrite {LIGNE_INSCRITE['go']} = {LIGNE_INSCRITE['plafond']} USD : "
              f"{'conforme' if d['ligne'] == LIGNE_INSCRITE['plafond'] else 'NON conforme (ligne neuve exigée)'}")
        for prix in (1.12, 1.30, 1.40):
            dispo = (d["configuration"] - TELECH_GO * TELECH_USD_GO) / prix
            print(f"   à {prix} USD/h : {dispo:.1f} h de carte avant la coupure de la configuration (téléchargement 40 Go déduit) ; "
                  f"P1 ({scen['P1']['total']:.2f} h) {'couvert' if dispo >= scen['P1']['total'] else 'NON couvert'}, marge "
                  f"{dispo - scen['P1']['total']:.1f} h")
        if d["repli_h200"]:
            dispo = (d["configuration"] - TELECH_GO * TELECH_USD_GO) / 4.70
            print(f"   H200 NVL à 4,70 : {dispo:.2f} h avant la coupure ; haut de l'attendu {scen['haut']['total']:.2f} h, marge "
                  f"{dispo - scen['haut']['total']:.2f} h ; P1 {scen['P1']['total']:.2f} h NON couvert")
        reste = d["ligne"] - d["configuration"]
        print(f"   ligne − configuration = {reste} USD ; stockage arrêté 48 h = {STOCKAGE_H * STOCKAGE_USD_H:.2f} USD : "
              f"{'couvert' if reste >= STOCKAGE_H * STOCKAGE_USD_H else 'NON couvert'}")
        for nom, u in (("P1 à 1,40", p1[1.40]), ("P1 à 2,10", p1[2.10]), ("H200 d'emblée à 4,70", h200[4.70])):
            if nom.startswith("H200") and not d["repli_h200"]:
                print(f"   {nom} : sans objet (aucun repli)")
                continue
            print(f"   {nom} : {u['total']:.1f} USD ≤ ligne {d['ligne']} ? {'oui' if u['total'] <= d['ligne'] else 'non'}")

    print("\n## Calendrier")
    fin_go = datetime.combine(LIGNE_INSCRITE["echeance"] + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc)
    ech = fin_go - timedelta(hours=AVANCE_ECHEANCE_MINUTERIE_H)
    print(f"  fin du GO (lendemain 00:00 UTC de l'échéance) : {fin_go.isoformat()} ; secondes : {int(fin_go.timestamp())}")
    print(f"  échéance proposée de la minuterie (fin du GO − {AVANCE_ECHEANCE_MINUTERIE_H:g} h) : {ech.isoformat()} ; "
          f"secondes : {int(ech.timestamp())}")
    for nom in ("haut", "P1"):
        der = ech - timedelta(hours=scen[nom]["total"])
        print(f"  dernière création pour finir le scénario {nom} ({scen[nom]['total']:.2f} h) avant l'échéance de la minuterie : "
              f"{der.isoformat(timespec='minutes')}")
    dernier_jour = date(2026, 11, 25)
    fin_p1 = datetime.combine(dernier_jour, datetime.max.time(), tzinfo=timezone.utc).replace(microsecond=0) + \
        timedelta(hours=scen["P1"]["total"])
    print(f"  dernier jour de création proposé {dernier_jour} : création à 23:59:59 → fin de P1 vers {fin_p1.isoformat(timespec='minutes')} "
          f"({'avant' if fin_p1 <= ech else 'APRÈS'} l'échéance de la minuterie)")

    print("\n## Option hors des totaux : juge de T0.8 (le code v3 ne le joue pas)")
    print(f"  une passe sans raisonnement : {N_EVAL_EP * T * JUGE_UNE_PASSE_S / 3600:.2f} h (hôte nominal) ; "
          f"avec raisonnement (400 jetons au plus, {EP_S / T:.2f} s par action) : {N_EVAL_EP * T * EP_S / T / 3600:.2f} h")


if __name__ == "__main__":
    main()
